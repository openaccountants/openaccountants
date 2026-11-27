---
name: eu-oss-digital
description: Use this skill whenever a business sells digital services (electronically supplied services) B2C to consumers in other EU member states and needs to determine the correct VAT treatment. Trigger on phrases like "OSS", "One-Stop-Shop", "MOSS", "Mini One-Stop-Shop", "digital services VAT", "electronically supplied services", "B2C cross-border EU", "EU VAT on digital", "EUR 10,000 threshold", "destination country VAT rate", "non-Union OSS", or any request involving the VAT treatment of digital services sold to EU consumers. This skill contains the complete OSS rules, the EUR 10,000 threshold, destination VAT rate table, filing requirements, consumer location evidence rules, and the Union vs non-Union OSS distinction. ALWAYS read this skill before advising on any B2C digital services VAT question.
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-27
source_checked: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
category: cross-border
type: situation-rules
version: 1.2
---

# EU OSS Digital v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This skill determines the VAT route for 2026 B2C electronically supplied services (ESS) sold to EU consumers by EU and non-EU businesses. It covers classification, the small cross-border threshold, Union and non-Union OSS, destination rates, location evidence, registration, returns, corrections and input-tax recovery. OSS is an optional reporting scheme for covered taxable supplies; it does not make an exempt service taxable or replace the place-of-supply rules. Union OSS also covers eligible services beyond ESS and certain distance sales of goods. IOSS for imported goods is a separate scheme.

Use `eu-reverse-charge.md` for an actual B2B service, `vat-place-of-supply-master.md` for the wider framework, and the relevant country VAT skill for exemptions, national registration, product classification and the selected national OSS portal. The original [T1], [T2] and [T3] tags identify respectively an established-rule task, fact-sensitive review and a referral boundary. They do not confer accountant approval or remove professional review before filing.

### Quick reference

| Question | Answer and boundary | Official source |
|---|---|---|
| Home or destination place? | Article 59c permits home-state place only for a single-member-state seller with combined qualifying net TBE/distance-goods sales at or below EUR 10,000 in both current and preceding calendar years, without a destination option. Otherwise determine destination place, rate and any exemption | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Which scheme? | EU business/fixed-establishment services seller: Union OSS for eligible supplies outside establishment states. No EU business/fixed establishment: non-Union OSS for covered EU B2C services. OSS is optional; use all covered taxable supplies if elected | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| When file and pay? | Quarterly, by end of the following month; file even when there are no covered supplies. A correction-only return is not nil | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Which location evidence? | Apply the specific presumptions first; residual cases normally require 2 non-contradictory items (in words on the page). The separate EUR 100,000 small-evidence derogation has EU-establishment and independent-participant conditions | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |

## Ask the client first

1. Where are the seller's business and fixed establishments, and which establishment supplies the service? A VAT number alone does not establish a fixed establishment.
2. Is the customer non-taxable, or a business acting as such? Obtain the relevant VAT/status and use evidence. Unknown seller, customer status or service nature stops classification.
3. What precisely is supplied: automated digital content, a live activity, professional advice, physical goods or a bundle? Who contracts, sets terms, authorises payment and delivers it?
4. What is the combined net value of qualifying cross-border TBE services and intra-Community distance sales of goods in the current and preceding calendar years? Was a destination option exercised?
5. Where is the consumer under the applicable presumptions and evidence, and what specific rate/exemption applies there?
6. Is the seller using a confirmed cross-border SME exemption in that destination, or OSS? Obtain identification, effective dates, prior returns and any corrections or exclusion notices.

Sources: [Directive Articles 44-45, 54, 58-59c, 284 and OSS provisions](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Regulation Articles 7, 9a, 11, 18-24f](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).

## The method, step by step

### Step 1: What qualifies as ESS? [T1]


- **Electronically supplied service (ESS)**  -  A service delivered over the internet or electronic network, the nature of which renders its supply essentially automated, involving minimal human intervention, and impossible to ensure in the absence of information technology.  _(Implementing Regulation 282/2011 Article 7(1) and Annex I; VAT Directive Article 58)_

### ESS -- YES (qualifies) [T1]

| Category | Examples |
| --- | --- |
| Software and apps | Downloads of software, apps, games, updates, add-ons, SaaS |
| Digital content | E-books, online newspapers/magazines, digital music, streaming video/audio, podcasts |
| Online courses | Pre-recorded courses, automated e-learning with no live instructor |
| Cloud services | Web hosting, cloud storage, online backup |
| Advertising | Online advertising services (banner ads, search engine ads) |
| Digital images/templates | Stock photos, website templates, design files |
| Online gaming | MMO subscriptions, in-game purchases and automated online gambling; ESS classification does not settle any gambling exemption or rate |

### ESS -- NO (does NOT qualify) [T1]

| Category | Why Not ESS |
| --- | --- |
| Live online teaching/consulting | Significant human intervention is not ESS. A virtual educational or similar activity can nevertheless be taxable at the B2C consumer location under Article 54(1); ordinary professional consultation can follow Article 45 |
| Physical goods ordered online | Physical delivery = goods, not ESS |
| Professional services via email | Email is the medium, not the service itself |
| Telephone/fax services | Telecoms, not ESS (separate rules under Art 58) |
| Physical event tickets sold online | The event is the supply, not the online sale |
| Bespoke software development | Custom work involving significant human intervention fails the automation test; do not assume every software licence or custom configuration has that character |


Article 7 and Annex I require the actual automation/minimal-human-intervention facts for the YES categories: an internet delivery channel alone is insufficient. Email communication does not itself make the underlying service ESS (Directive Article 58). Live online teaching is excluded from ESS under Article 7(3)(j), but the destination rule for streamed/virtually available B2C educational and similar activities in Article 54(1), second subparagraph, applies in 2026; do not infer home-state taxation merely because the service is not ESS.

Sources: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 (Article 7 and Annex I); https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 45, 54 and 58).

### Step 2: The EUR 10,000 threshold [T1]

Apply Directive Article 59c, not the former Article 58(2) citation. Aggregate the qualifying cross-border telecommunications, broadcasting and electronic services (TBE) and intra-Community distance sales of goods, exclusive of VAT, across destinations. Do not count just ESS or reset the test for each country. The seller must be established, or in the absence of establishment have its permanent address/usual residence, only in 1 member state. The qualifying supplies must be to other member states as specified in Article 59c(1)(b).

| Test | Rule and conditions | Official source |
|---|---|---|
| Home-state place exception | Combined qualifying net supplies do not exceed EUR 10,000 in the current calendar year AND did not exceed it in the preceding calendar year; single-member-state seller and qualifying cross-border supplies required, Article 59c(1) | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Crossing the threshold | Destination place applies from the supply which exceeds EUR 10,000, not only the next quarter or the next year, Article 59c(2) | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Voluntary destination option | An otherwise qualifying seller may opt for destination treatment; option covers at least 2 calendar years (in words on the page), Article 59c(3) | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Excluded seller | Non-EU seller or seller established in more than 1 member state cannot use this home-state threshold exception; it is not a VAT registration exemption, Article 59c | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

If the exception applies and no destination option was chosen, use the applicable home-state domestic rate or exemption and national return. If destination applies, determine the destination rate or exemption before charging VAT. For taxable covered supplies, choose eligible OSS or meet the relevant local obligations; OSS itself is optional. Do not say all small sellers must register for OSS or charge destination VAT irrespective of relief.

Since 2025, an eligible EU-established small enterprise can use the separate cross-border SME exemption in participating destinations after the required prior notification/confirmation and EX identification. This requires Union annual turnover not exceeding EUR 100,000 in the current and preceding calendar years plus the destination's applicable national threshold, exclusions and transition conditions. It is not automatic and is unavailable to a seller established outside the EU. It can coexist with OSS for taxable supplies in other member states; exempt supplies are not declared as taxable OSS sales. Verify the confirmed state-by-state position before invoicing. [Commission SME scheme](https://sme-vat-rules.ec.europa.eu/sme-scheme/cross-border-sme-scheme_en); [Directive Article 284 and neighbors](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1).

### Step 3: How OSS works [T1]

| Feature | Union OSS | Non-Union OSS | Official source |
|---|---|---|---|
| Seller and services | Seller with EU business/fixed establishment; services to non-taxable customers taxable in a member state where the seller has neither. Goods have additional eligible routes under Article 369b, including a non-EU goods seller | Seller with neither EU business nor fixed establishment; all eligible B2C services taxable in the EU, not ESS alone. An EU VAT registration without an establishment does not itself disqualify it | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 358a-359, 369a-369b); https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en |
| Member State of Identification (MSI) | Business-establishment state; if business outside EU, a qualifying EU fixed-establishment state. With multiple EU fixed establishments, choose 1: Article 369a binds that choice for the calendar year concerned and the 2 following calendar years; review an actual establishment change under the registration rules | Any chosen EU member state; identification is for this special scheme, not general-purpose domestic registration | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 358a, 362, 369a, 369d); https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en |
| Covered supplies | All supplies covered by the selected scheme; no selective taxable destination countries. Services taxable in a state where seller is established stay on the relevant domestic return | All services covered by this scheme supplied within the EU; choose no selective taxable countries | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 359, 369b); https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en |
| Filing and payment | Quarterly electronic return to MSI, single payment referencing the return | Quarterly electronic return to chosen MSI, single payment referencing return | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 364, 367, 369f, 369i) |
| Due date | End of month following the quarter for return and payment | Same quarterly rule | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 364, 367, 369f, 369i) |
| Rate | Correct member-state-of-consumption rate for the actual taxable service; classification/exemption and regional rules first | Same; MSI's rate does not decide another destination's VAT | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en |
| Input tax | No input deduction in OSS. Recover via the domestic return where appropriate or Directive 2008/9/EC refund route subject to Article 369j | No input deduction in OSS. Article 368 uses Directive 86/560/EEC refund with specified restrictions disapplied; domestic return if registered there for other activities | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 368, 369j) |

For non-Union input refunds relating to covered services, Article 368 disapplies Directive 86/560/EEC Articles 2(2), 2(3) and 4(2); do not describe it simply as a more restrictive refund regime or impose a blanket reciprocity condition. Eligibility and input-tax restrictions still need the country rules. A seller required to register in a member state for other activities deducts eligible local input for covered activities through that state's ordinary return, not OSS.

Non-EU sellers (including the original US, UK, Australian and Indian examples) with taxable B2C EU digital supplies and no EU establishment can elect non-Union OSS or fulfil obligations directly in the consumption states. No EUR 10,000 Article 59c benefit applies. An EU fixed establishment changes the eligible scheme; incorporation or the country of a VAT number alone does not decide it. [Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [registration guidance](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en).

### Step 4: Destination rates [T1]

The following is the official EU standard-rate reference for all 27 member states read on 27 November 2026. It is not a complete digital-product classification table. Use the specific destination and regional rate for the actual service: software, automated SaaS, streaming and cloud ordinarily fall within the standard category, but do not infer every digital service is taxable at this rate.

| Country | Code | Standard rate | Scope and qualification | Official source |
|---|---|---|---|---|
| Austria | AT | 20% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Belgium | BE | 21% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Bulgaria | BG | 20% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Croatia | HR | 25% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Cyprus | CY | 19% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Czech Republic | CZ | 21% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Denmark | DK | 25% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Estonia | EE | 24% | Product classification and any exemption must be established before using the standard rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Finland | FI | 25.5% | Product classification and any exemption must be established before using the standard rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| France | FR | 20% | See qualified publication row below; standard rate is not the publication rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Germany | DE | 19% | See qualified publication row below; standard rate is not the publication rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Greece | GR | 24% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Hungary | HU | 27% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay; highest listed standard rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Ireland | IE | 23% | See qualified publication row below; standard rate is not the publication rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Italy | IT | 22% | See qualified publication row below; standard rate is not the publication rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Latvia | LV | 21% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Lithuania | LT | 21% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Luxembourg | LU | 17% | See qualified publication row below; standard rate is not the publication rate; lowest listed standard rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Malta | MT | 18% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Netherlands | NL | 21% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Poland | PL | 23% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Portugal | PT | 23% | See qualified publication row below; standard rate is not the publication rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Romania | RO | 21% | See qualified publication row below; standard rate is not the publication rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Slovakia | SK | 23% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Slovenia | SI | 22% | Product-specific reduced/exempt treatment not exhaustively researched; use the national overlay | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Spain | ES | 21% | See qualified publication row below; standard rate is not the publication rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Sweden | SE | 25% | See qualified publication row below; standard rate is not the publication rate | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |

The listed standard rates range from 17% in Luxembourg to 27% in Hungary (comparison derived from the official table). Regional rates and product-specific relief need the national overlay; this standard table excludes special territories.

| Publication destination | Qualified rate and conditions | Official legal/authority source |
|---|---|---|
| France | Metropolitan qualifying electronic book 5.5%, subject to fiscal book definition; qualifying digital press 2.1%, not the old 5.5% press rate. CGI 298 septies requires a digitised version of a qualifying publication or a legally recognised online press service; a news link alone is insufficient. The summary also excludes pornographic or violence-inciting publications; actual press eligibility must be established before applying that rate. Book/press classification and regional treatment differ | https://bofip.impots.gouv.fr/bofip/1437-PGP.html/identifiant=BOI-TVA-LIQ-30-10-40-20260729 ; https://entreprendre.service-public.gouv.fr/vosdroits/F37781 ; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179663/2026-04-28/ |
| Germany | 7% (in words on the page) for qualifying electronic publications under UStG12(2)(14); printed-product comparability/statutory category, youth-protection restrictions and exclusions for predominantly advertising, video or audible music apply; not every digital download | https://www.gesetze-im-internet.de/ustg_1980/__12.html |
| Ireland | 0% (in words on the page) qualifying e-books/audiobooks from 1 January 2024 and e-newspapers from 1 January 2023; qualifying e-periodicals use second reduced 9%. Predominantly advertising, video or audible music excluded; newspaper/book definitions matter; see Revenue electronic-publication manual for the exclusions | https://www.revenue.ie/en/vat/vat-on-services/electronic-services/electronic-publications/index.aspx ; https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx ; https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part03-taxable-transactions-goods-ica-services/Services/electronic-publications.pdf |
| Italy | 4% qualifying digital editorial products (numeral on page). ISBN/ISSN is necessary but insufficient: product must have the distinctive characteristics of a book or other listed editorial product. DPR 633/1972, Table A, Part II, item 18 excludes pornographic newspapers/periodicals and catalogues other than book-information catalogues; circular 20/E of 2016, pp. 40-41 supplies the digital conditions | https://www.finanze.gov.it/export/sites/finanze/.galleries/Documenti/Varie/circolare-20E-del-18-maggio-2016.pdf  ; https://def.giustiziatributaria.gov.it/DocTribFrontend/executePrintArticolo.do?codiceOrdinamento=0010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7B435D34E0-465D-4918-8ED2-52E6C45D6226%7D&idAttoNormativo=%7B75A4827C-3766-4ECC-9C45-00C8D6CDC552%7D |
| Luxembourg | 3% (in words on the page) under Articles 39-40 and Annex B, item 5 for qualifying electronic publications; excludes predominantly advertising, video/music and predominantly pornographic publications | https://pfi.public.lu/dam-assets/pdf/legislation/tva/loi/loi-tva-2026-01-01.pdf |
| Portugal | Mainland 6% under CIVA 18(1)(a), Lista I, item 2.1, qualifying electronic books and listed periodicals; exclude predominantly video/music, obscene/pornographic and other listed exclusions; autonomous regions need separate rates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/c-iva-listas.aspx |
| Romania | 11% for qualifying physical/electronic books, newspapers and magazines under amended Article 291(2)(g), excluding predominantly video, music or advertising | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| Spain | 4% under Article 91.Dos.1.2 for qualifying electronic books/newspapers/magazines; exclude wholly/mainly advertising and wholly/predominantly video/audible music. The statutory advertising test and bundled ancillary-item conditions must be checked | https://boe.es/buscar/act.php?id=BOE-A-1992-28740&p=20261007&tn=1 |
| Sweden | 6% for qualifying comparable electronic books/publications; predominantly advertising does not qualify. Product must be comparable to the listed printed publications; classification before rate | https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatserochundantagfranmoms.4.58d555751259e4d66168000409.html |

These publication rows require the stated national qualification. They are not an exhaustive reduced-rate list for every destination. Do not interpret the other standard-rate rows as a denial of publication relief.

### Step 5: Determine the consumer's location [T2]

Apply the relevant Regulation Articles 24a-24b presumption first. A physically required telephone booth, wi-fi hotspot, internet café or similar location has its own presumption; on an intra-EU passenger leg the defined departure country applies. Fixed-line supply points to installation, mobile supply to SIM country, and specified decoder/viewing-card cases to device location or the card destination. Do not replace these with an automatic billing-address preference.

For residual Article 24b(d) services, establish the location with 2 non-contradictory Article 24f items (in words on the page). Contradictory IP and billing evidence has no general “billing wins” rule: investigate the actual facts/presumption, obtain the required corroboration and refer unresolved conflicts. A seller may rebut specified 24a/24b(a)-(c) presumptions with 3 non-contradictory items (in words on the page) under24d; authorities may rebut misuse/abuse.

| Evidence | Actual relevance | Official source |
|---|---|---|
| Billing address | Customer billing address, 24f(a) | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| IP/geolocation | Device IP or other geolocation, 24f(b) | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Bank details | Payment account location or bank-held customer billing address, 24f(c); card issuer country alone must actually support these facts | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| SIM mobile country code | SIM/MCC details, 24f(d); also consider the specific mobile presumption | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Fixed land line | Location of line through which service is supplied, 24f(e) | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Other commercially relevant information | Article 24f(f); original delivery preferences, language and contract details are possible facts, not automatic proof of residence | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Small-evidence derogation | For residual 24b(d) supplies from an EU business/fixed establishment, aggregate net value not above EUR 100,000 in current AND preceding calendar years; 1 item (in words on the page) from 24f(a)-(e), supplied by another participant in the supply, neither seller nor customer. It ceases immediately on crossing; not a non-EU seller concession | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Records | Keep sufficiently detailed OSS records including location evidence for 10 years from year-end (in words for non-Union Directive 369; numeral 10 for Union Article 369k); electronic availability on request | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/record-keeping-and-audits-oss_en |

The EUR 100,000 evidence derogation is distinct from the EUR 10,000 place threshold; satisfying one does not establish the other. In the current Regulation, the 24b/24d/24f rules also cover the specified streamed/virtual Article 54(1) activities. [Regulation Articles 23-24f](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).

### Step 6: File, pay, correct and retain [T1]

| Quarter | Period | Return and payment deadline | Official source |
|---|---|---|---|
| Q1 | 1 January to 31 March | 30 April | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 364/367/369f/369i) |
| Q2 | 1 April to 30 June | 31 July | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (same articles) |
| Q3 | 1 July to 30 September | 31 October | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (same articles) |
| Q4 | 1 October to 31 December | 31 January following year | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (same articles) |

The dates are calendar applications of the end-of-following-month rule, not a national weekend extension: the Commission says the deadline is not extended for weekends or public holidays. Supply, rate and exemption classification must be completed before entries.

1. Register through the chosen MSI's national OSS portal, selecting the correct scheme and effective date. Normally coverage starts on the first day of the following calendar quarter; where the first covered supply is earlier, notify MSI no later than the 10th day of the following month (in words on the page) to apply from that first supply (Regulation 57d). Obtain accepted identification/effective date; unresolved late registration needs national handling.
2. For each consumption state, record the taxable amount excluding VAT, rate, VAT per rate and total; separate standard and reduced categories. Union goods dispatch/establishment branches need the additional Article 369g identifiers and breakdowns. Do not include exempt supplies, including zero-rated supplies (exempt with deduction), or input deductions in the OSS return. The Commission expressly excludes those supplies; Ireland’s 0% publication rate in the reference table is not a taxable OSS entry.
3. File quarterly even if there are no covered supplies. A nil return applies only where there are no supplies AND no corrections to earlier returns (Regulation 59a); a correction-only return is not a nil return.
4. File in EUR unless a non-euro MSI requires its currency; use the ECB rate on the last day of the quarter, or the next publication day if none is published then (Articles 366/369h). The original Sweden, Denmark and Poland illustrations are examples of non-euro MSI rules, not permission to choose any currency.
5. Submit and save confirmation and the unique return/payment reference. Pay the stated scheme VAT to the MSI account by the deadline, identifying that return; payment is specific to that return. Do not use an input-tax credit as an OSS deduction.
6. Corrections for current OSS periods go in a subsequent return's correction section, by consumption state, original period and VAT adjustment, within 3 years of the original due date (in words on the page). Earlier MOSS periods through Q2 of 2021 have the old amendment procedure. After the 3-year OSS window use the consumption state's direct assessment/amendment rules; cessation/exclusion/final-return corrections also have the direct-state rules in Regulation 61a. A negative balance for one consumption state cannot offset another state's VAT.
7. Reconcile the return and payment, track any destination refunds separately, retain records and respond electronically to audit requests. Interest/penalties are assessed under consumption state law and paid there; this skill does not invent a common EU penalty scale.

**Nil returns and exclusion:** missing 3 returns alone is not the complete legal test. Regulation 58b includes reminders for 3 immediately preceding return periods and failure to submit each within 10 days of its reminder. Persistent nonpayment requires reminders for the 3 immediately preceding periods and failure to pay the full VAT for each within 10 days of its reminder, except where less than EUR 100 remains unpaid for each period. The records ground requires failure to make records electronically available after a request and 1 month after a subsequent MSI reminder. Persistent noncompliance exclusion generally bars all special schemes for 2 years after the exclusion return period (in words on the page), subject to the intermediary-related exception for IOSS. Do not infer a safe harbour from these examples; review the actual notice and grounds. Direct destination obligations continue after exclusion.

Sources: [Commission return/payment guidance](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en); [registration](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en); [Directive 364-369k](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Regulation 57d,58-63c](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).

### Step 7: Non-Union MSI choice [T1]

Ireland, Netherlands, Luxembourg and Estonia are possible non-Union MSI choices under the any-member-state non-Union rule. They are not an official ranking or an exemption. The destination rate governs eligible taxable services, so choosing Luxembourg does not substitute its 17% standard rate for another state's rate. Choose the actual administrative portal/contact relationship and obtain valid special-scheme registration. No official popularity or portal-quality ranking is asserted. [Directive 358a](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Commission registration](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en).

## Boundary and exception table

### EC1: Mixed digital content and physical goods [T2]

The original e-book plus printed-workbook package needs a contract-specific single/multiple-supply assessment. Its composite classification, principal/ancillary outcome, goods/ESS route and rate are not established by this Guide. Do not file or invoice from the former generic bundle conclusion. Check this point with one of our partner accountants.

### EC2: Live-streamed course and recording [T2]

The original course has a live instructor answering questions and a later recording. A separately supplied automated recording can be ESS; human-led teaching is not ESS. The classification and rate of the combined live-course/recording bundle are not established here. Check this point with one of our partner accountants. For the live educational activity, test Article 54(1)'s virtual-consumer-location rule even though it is not ESS, plus the actual education exemption. Not every live consultation is such an activity. [Regulation 7 / Annex I](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1); [Directive 54/58](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1).

### EC3: Marketplace/platform deemed supplier [T3]

For the original freelancer selling through a payment-collecting marketplace, apply Article 9a to the platform's actual participation and contracts. A participating person is presumed to act in its own name on the provider's behalf unless the provider is explicitly identified as supplier in the contractual arrangements and on each relevant invoice and consumer bill/receipt. A person authorising the charge or delivery, or setting general supply terms, cannot identify someone else to rebut this presumption. A payment processor that does not participate in the underlying supply is excluded. If the platform is supplier, analyse both the provider-to-platform and platform-to-consumer legs: the first leg is not automatically an intra-EU reverse charge or VAT-free, and the second's place/exemption/scheme conditions still apply. Refer the contracts and actual roles before allocating collection responsibility. [Regulation 9a](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).

### EC4: UK seller after Brexit [T1]

The original UK seller without EU establishment has no Article 59c small-threshold benefit. For taxable eligible EU B2C services, it can choose non-Union OSS or fulfil the destination obligations directly. An actual EU fixed establishment changes scheme eligibility; UK nationality alone is not the test. [Directive 358a-359 and 59c](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1).

### EC5: Business claim without a VAT number [T2]

For ESS, Regulation 18(2) allows a supplier to regard an EU customer as non-taxable as long as the customer has not communicated an individual VAT number, irrespective of contrary information. This is permission in that special rule, not a universal declaration that every unnumbered business is legally a consumer. Article 18(1)(b) separately has a pending-registration route with other status proof and reasonable verification; Article 19 requires the actual use/capacity test. If later evidence changes the original treatment, obtain review of the original facts, invoice/credit note, place, liability, returns and timing. Do not automatically credit and re-invoice as reverse charge merely because a number arrives. [Regulation 18-19/25](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1); use `eu-reverse-charge.md` for a supported B2B conclusion.

## Worked cases

The original 5 scenarios follow, with the legal conditions restored. All prices are net illustrative inputs. Assume taxable supplies with no applicable exemption, correct consumer evidence, no conflicting use-and-enjoyment rule and no platform replacing the stated seller, unless a case expressly tests that issue.

### Test 1: Below threshold, EU seller

A German sole trader has EUR 8,000 qualifying cross-border automated-course sales across 5 EU countries this year and EUR 6,000 last year, no additional qualifying goods/TBE and establishment only Germany. Without a prior destination option, Article 59c permits home-state place; ordinary taxable courses use 19% German VAT and the domestic return. Destination treatment can be elected under its minimum 2-calendar-year rule. These turnover figures are scenario inputs, not national exemption thresholds.

### Test 2: Above threshold, EU seller

The same trader has EUR 12,000 qualifying current-year sales. Consider a net EUR 500 sale to France after, or itself taking the total above, EUR 10,000. No education/SME exemption applies. Destination standard 20% gives derived EUR 100 VAT and EUR 600 gross. Union OSS in Germany is an available reporting choice, with quarterly returns; direct French obligations are the alternative. Do not treat an OSS recommendation as a legal requirement.

### Test 3: Non-EU US seller

The original US SaaS company with EUR 50,000 sales across 10 EU countries and no EU business/fixed establishment has no EUR 10,000 benefit. It can elect non-Union OSS in 1 MSI, such as Ireland, for all covered taxable B2C services; otherwise fulfil each relevant destination's obligations. Use actual destination rates and quarterly returns if in the scheme.

### Test 4: E-book to France

For the original Italian seller's qualifying French metropolitan e-book supply through OSS, establish that French destination place applies and the book meets the fiscal definition. Net price EUR 15 at 5.5% gives derived VAT 0.825, rounded to EUR 0.83 at cent precision and gross EUR 15.83. EUR 15 as a gross price would instead produce about EUR 0.78 VAT; the original example is correct only on a net price assumption. Report under France/reduced rate.

### Test 5: Live professional consultation

For the original Maltese consultant's 1-hour live interactive Zoom professional consultation to a German private consumer, net EUR 200, no automation: not ESS. Assume ordinary professional advice, no Article 54 educational activity or other exception/exemption. Article 45 places it in Malta; taxable 18% gives derived EUR 36 VAT and EUR 236 gross on the Malta domestic return. If the original EUR 200 fee was VAT-inclusive instead, derived VAT is EUR 30.51 and net EUR 169.49. Do not apply this conclusion to a live virtual educational event merely because it is not ESS.

```oa-check
name: German seller crosses the common threshold with a French sale
inputs:
  earlier_qualifying_net_sales: 9800
  french_sale_net: 500
  threshold: 10000
  french_standard_rate: 0.20
steps:
  cumulative_qualifying_net_sales: earlier_qualifying_net_sales + french_sale_net
  excess_over_threshold: cumulative_qualifying_net_sales - threshold
  destination_vat_on_crossing_sale: french_sale_net * french_standard_rate
  gross_invoice: french_sale_net + destination_vat_on_crossing_sale
expected:
  cumulative_qualifying_net_sales: 10300
  excess_over_threshold: 300
  destination_vat_on_crossing_sale: 100
  gross_invoice: 600
```

The entire crossing supply follows destination treatment on the stated Article 59c facts; tax is not computed only on the EUR 300 excess. The case assumes prior-year eligibility, no destination option and no SME/education exemption.

```oa-check
name: Qualified French e-book at a net price
inputs:
  net_price: 15
  qualified_book_rate: 0.055
steps:
  unrounded_vat: net_price * qualified_book_rate
  vat_at_cent_precision: round(unrounded_vat, 2)
  gross_price: net_price + vat_at_cent_precision
expected:
  unrounded_vat: 0.825
  vat_at_cent_precision: 0.83
  gross_price: 15.83
```

Rate sources: Germany 19% https://www.gesetze-im-internet.de/ustg_1980/__12.html ; France 20% https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm ; qualifying French book 5.5% https://bofip.impots.gouv.fr/bofip/1437-PGP.html/identifiant=BOI-TVA-LIQ-30-10-40-20260729 ; Malta 18% (in words on the page),Cap. 406 Article 19 https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 . Prices, turnover numbers and percentage products in these examples are illustrative inputs or derived values, not additional legal figures.

## When to refuse or refer

- Never use OSS for an actual B2B service. Establish status/use first; use the reverse-charge skill where its conditions apply.
- Never keep home-state Article 59c place after its threshold is crossed or where its conditions fail; test destination exemption before charging destination VAT.
- Never deduct input VAT in an OSS return; use the actual domestic/refund route.
- Never treat non-Union special-scheme identification as domestic registration for every purpose.
- Never omit a required nil/correction-only return. The complete reminder and exclusion tests are in Step 6, not a shorthand “3 misses” rule.
- Never classify significant human-led services as automated ESS; separately test virtual-activity place and exemptions.
- Never discard required location evidence before the 10-year OSS retention period.

Unresolved establishment, status, evidence conflict, mixed supply, platform participation, reduced-rate qualification, exemption, late registration/correction or exclusion has no usable invoice/filing outcome here. Check this point with one of our partner accountants. Withhold an invoice/filing conclusion until the relevant facts and national portal requirements are established. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

## Filing and payment

Follow Step 6 through national OSS portal identification, quarterly sales/correction entries, electronic submission confirmation and referenced payment. Confirm the accepted scheme effective date, deadline, currency and destination amounts before submitting; track any consumption-state correction/refund or enforcement separately. Portal screen/field names and current national late-remedy rules are not invented here.

## Completion checklist

Confirm seller establishments, customer status/use, automation or virtual-activity classification, place/threshold/option, SME or other exemption, correct destination product rate, location presumption/evidence, scheme identification/effective date, return/correction totals, payment reference, input refund route and record retention. Retain unresolved facts for review.


This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. VAT rates and thresholds are subject to change. Always verify current rates before filing. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

If you would like a licensed accountant to review your VAT position, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.

## Sources

| Source and actual scope read | Official URL | Read on |
|---|---|---|
| EU VAT Directive, Read for Articles 44-45, 54, 58-59c, 284 and neighbors, 358-369k: place, threshold, SME relief, OSS eligibility, returns, refunds and records | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 | 2026-11-27 |
| EU Implementing Regulation, Read for Article 7 and Annex I, 9a, 11, 18-25, 57d-63c: ESS, platforms, status, location and scheme procedure | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 | 2026-11-27 |
| Commission OSS, Read for optional coverage, threshold, all covered supplies and scheme boundaries | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en | 2026-11-27 |
| Commission registration, Read for EU/non-EU eligibility, MSI choice, commencement and national portal route | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en | 2026-11-27 |
| Commission returns/payment, Read for deadlines, no extension, corrections, currency, negative balances and payment reference | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en | 2026-11-27 |
| Commission records/audit, Read for the 10-year record requirement and electronic availability | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/record-keeping-and-audits-oss_en | 2026-11-27 |
| Commission SME, Read for EU establishment, Union EUR 100,000 threshold, national limits, EX prior confirmation and OSS coexistence | https://sme-vat-rules.ec.europa.eu/sme-scheme/cross-border-sme-scheme_en | 2026-11-27 |
| EU Your Europe, Read for all 27 standard-rate rows and regional/category warnings | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm | 2026-11-27 |
| Germany UStG, Read for section 12(1) standard rate and 12(2)(14) publication conditions | https://www.gesetze-im-internet.de/ustg_1980/__12.html | 2026-11-27 |
| France BOFiP, Read for fiscal book definition and qualifying electronic-book conditions | https://bofip.impots.gouv.fr/bofip/1437-PGP.html/identifiant=BOI-TVA-LIQ-30-10-40-20260729 | 2026-11-27 |
| France Service Public, Read for books, qualifying press, exclusions and regional distinctions | https://entreprendre.service-public.gouv.fr/vosdroits/F37781 | 2026-11-27 |
| Ireland Revenue, Read for electronic publication categories, zero-rate commencement dates and exclusions | https://www.revenue.ie/en/vat/vat-on-services/electronic-services/electronic-publications/index.aspx | 2026-11-27 |
| Ireland Revenue, Read for current 2026 standard, reduced and second reduced rates | https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx | 2026-11-27 |
| Italy 20/E of 2016, Read for printed pp. 40-41: digital editorial products and ISBN/ISSN necessary but insufficient; real PDF recovered by ordinary direct fetch | https://www.finanze.gov.it/export/sites/finanze/.galleries/Documenti/Varie/circolare-20E-del-18-maggio-2016.pdf | 2026-11-27 |
| Italy current DPR 633/1972 Table A, Read for Part II rate header and item 18 publication categories/exclusions, with the source’s 2025-amendment note | https://def.giustiziatributaria.gov.it/DocTribFrontend/executePrintArticolo.do?codiceOrdinamento=0010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7B435D34E0-465D-4918-8ED2-52E6C45D6226%7D&idAttoNormativo=%7B75A4827C-3766-4ECC-9C45-00C8D6CDC552%7D | 2026-11-27 |
| Italy 2026 consolidated VAT law, Read for Articles 170-171: repeal and recast apply in 2027, so the 2026 reference remains DPR 633/1972 | https://www.gazzettaufficiale.it/eli/gu/2026/01/30/24/so/4/sg/pdf | 2026-11-27 |
| Luxembourg coordinated law 2026, Read for Articles 39-40 and Annex B, item 5: electronic publication conditions | https://pfi.public.lu/dam-assets/pdf/legislation/tva/loi/loi-tva-2026-01-01.pdf | 2026-11-27 |
| Portugal CIVA, Read for Article 18: mainland reduced rate and regional distinction | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx | 2026-11-27 |
| Portugal CIVA, Read for Lista I, item 2.1: electronic publications and neighboring exclusions | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/c-iva-listas.aspx | 2026-11-27 |
| Romania law 141/2025, Read for Article II, point 42, amending Article 291: rates and electronic publication conditions | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf | 2026-11-27 |
| Spain current law, Read for Article 91.Dos.1.2: rate, e-books, exclusions and ancillary items | https://boe.es/buscar/act.php?id=BOE-A-1992-28740&p=20261007&tn=1 | 2026-11-27 |
| Sweden tax authority, Read for books, comparable electronic publications and advertising exclusion | https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatserochundantagfranmoms.4.58d555751259e4d66168000409.html | 2026-11-27 |
| Malta Cap. 406, Read for Article 19: standard rate and neighboring special-rate scope | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | 2026-11-27 |
| France CGI 298 septies, digital publication eligibility; operative version ends 1 January 2027 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179663/2026-04-28/ | 2026-11-27 |
| Ireland Revenue electronic-publication manual, zero/second-reduced categories and exclusions | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part03-taxable-transactions-goods-ica-services/Services/electronic-publications.pdf | 2026-11-27 |

Not yet confirmed: national product relief outside the expressly sourced publication rows, actual-case education/gambling/SME and use-and-enjoyment overlays, unresolved mixed supplies/platform contracts/evidence and local late remedies. These outcomes are non-usable until established for the actual facts. Check this point with one of our partner accountants. No official popularity or portal-quality ranking is asserted.
