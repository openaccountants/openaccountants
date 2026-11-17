---
name: property-transfer-tax-matrix
description: "Cross-country property-transfer-tax method for 2026. Establish property location, transaction and instrument dates, property and purchaser classification, taxable value, local bands, foreign-buyer overlays and relief conditions before computing purchase duty. Covers UK SDLT/LBTT/LTT, German GrESt, Spanish ITP/AJD, French DMTO, Italian registration/VAT, Netherlands transfer tax, Portuguese IMT/stamp duty, Singapore BSD/ABSD/SSD, Hong Kong AVD, Australian state duty, NZ purchase eligibility, Japan registration/acquisition tax and Canadian provincial/municipal layers. Distinguishes verified dated branches from explicit non-usable source holds; this is not complete worldwide coverage. Annual property/vacancy taxes, disposal gains and indirect landholder/share transactions require separate analysis."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/property-transfer-tax-matrix"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Property Transfer Tax Matrix v0.2

## Scope

**Tax year: 2026. Not yet approved.** This is a cross-country calculation method loaded with `cross-border-workflow-base`. Read it before quoting purchase or transfer tax and identify any source hold that prevents that quotation. It covers the buyer-side real-estate transfer-tax job, foreign-buyer overlays, relief screens and the residential VAT-versus-transfer-tax branch. It is explicitly partial: only the dated branches below may be used. A source hold is not a rate or an exemption.

The reviewer is the customer of the output. Preserve the local conveyancing solicitor/notary/tax-practitioner sign-off before completion. Purchase-duty analysis does not replace the conveyance or establish a person's right to buy.

Annual council/property taxes (UK Council Tax, French taxe foncière, Spanish IBI, Italian IMU and German Grundsteuer), rental income, disposal gains, commercial new-build lease VAT/GST beyond the classification handoff, and ordinary share stamp duty remain outside this computation. Annual vacancy/foreign-owner charges and indirect landholder rules are flagged separately because they can still affect the transaction. The South African transfer-duty trigger from the old description is retained as H15; no South African rate is cleared here.

## Quick reference

- Use the property's actual country and subnational jurisdiction, not the buyer's home country.
- Check the effective/instrument/contract dates before selecting any 2026 table. Several schedules change within this year.
- Distinguish a marginal band, a flat whole-base rate, an average-rate computation, an additional whole-base charge and a sliding-relief formula.
- Establish every joint purchaser's legal/beneficial profile, portfolio and relief entitlement. Corporate/trust rules can override the ordinary individual calculation.
- Keep purchase duty, VAT, foreign-buyer charge and annual vacancy/ownership tax as separate lines. Do not calculate through H01-H15.

## Ask the client first

Get the country, Land/region/province/state/municipality and exact property address; legal property classification and actual/intended use; freehold/lease/share/part-interest form; seller's VAT status and construction/refurbishment history; price, market/assessed values, liabilities and linked transactions; contract, option acceptance, substantial-performance, deed/registration and completion dates; all purchaser and beneficial-owner names and ownership shares; citizenship, residence and visa facts under the relevant tax/foreign-investment test; individual/company/trust/developer status; worldwide and locally counted dwelling interests of purchasers and spouses; main-home replacement dates; prior first-home relief and actual relief declarations; corporate/control histories for indirect transfers; and any exemption/remission certificate. Ask for original documents, not merely a summary saying “first home” or “non-resident”.

## The method, step by step

1. Identify the land situs and all local charging layers. Separate acquisition tax from annual or seller/disposal tax.
2. Classify the instrument and determine its legal tax point. Preserve earlier-contract protections and mid-year changes.
3. Establish the taxable base under the specific rule, including part interests, linked instruments, assumed debt and market-value substitutions.
4. Choose the ordinary schedule for that property/date. Calculate marginal slices, flat charges or average rates exactly as labelled.
5. Test foreign/additional-home/corporate/trust/developer overlays and each joint buyer. Test exemptions and reliefs before concluding an amount; a held eligibility rule prevents a final relieved calculation.
6. Record each applicable amount, source and condition separately; recompute arithmetic and applicable statutory rounding. Do not net one tax against another without authority.
7. Identify the actual return, local submission route, deadline, payment and confirmation. A missing local filing procedure is a hold, not permission to guess a form or a deadline.
8. Hand the calculation, evidence, unresolved facts and required local sign-off to the conveyancing professional. A number is provisional if any necessary branch remains held.


### UK01: England and Northern Ireland: ordinary residential bands

For a freehold or lease premium on a single residential dwelling, calculate each portion, not the whole price at its marginal rate. These ordinary bands have applied since 1 April 2025 and are the current bands read for 2026. A new lease's rent, linked transactions, mixed use and corporate flat-rate rules need their own analysis. [Official source](https://www.gov.uk/stamp-duty-land-tax/residential-property-rates)

| Residential price portion (GBP) | Marginal rate | Source |
|---|---|---|
| Up to 125,000 | 0% | https://www.gov.uk/stamp-duty-land-tax/residential-property-rates |
| Over 125,000 to 250,000 | 2% | https://www.gov.uk/stamp-duty-land-tax/residential-property-rates |
| Over 250,000 to 925,000 | 5% | https://www.gov.uk/stamp-duty-land-tax/residential-property-rates |
| Over 925,000 to 1,500,000 | 10% | https://www.gov.uk/stamp-duty-land-tax/residential-property-rates |
| Over 1,500,000 | 12% | https://www.gov.uk/stamp-duty-land-tax/residential-property-rates |

First-time buyer relief requires all joint purchasers to qualify as first-time buyers and an intended main residence. For a qualifying purchase not exceeding GBP 500,000, the first GBP 300,000 is nil and the rest is charged at 5%. Above that total price there is no first-time relief. Do not infer first-time status merely from an empty current portfolio; its complete historical ownership test still requires the applicable relief rules. [Official source](https://www.gov.uk/stamp-duty-land-tax/residential-property-rates)

### UK02: England and Northern Ireland: additional homes and non-residence

The additional-property rules add five percentage points to each ordinary residential band where their conditions are met. Check worldwide dwelling interests, joint purchasers, spouses/civil partners, trusts and replacement of a main residence. The relevant acquired interest generally needs to cost at least GBP 40,000 and not be subject to a lease with more than 21 years remaining. A company can fall within the higher rates on its first dwelling. The source excludes specified short leases and particular spouse-only transfers and has an existing-main-home share-increase exception; do not charge the surcharge before these branches are excluded. Replacement and disposal rules can prevent the charge or allow a refund; a subsequent main-home sale normally has a 36-month limit. Do not promise a refund merely because a sale is planned. The HMRC page sets out extended-time exceptions and claim limits. [Official source](https://www.gov.uk/guidance/stamp-duty-land-tax-buying-an-additional-residential-property)

The residential non-resident surcharge is a further two percentage points, using the SDLT residence test rather than citizenship or ordinary income-tax residence alone. The ordinary individual test looks for at least 183 days of UK presence in the twelve months before purchase; buyer-type exceptions and refund rules still require their actual conditions. Check that test, joint-buyer treatment and any Crown-employment relief before calculating. For an ordinary individual purchase to which both surcharges apply, add them to every band. This can produce a top marginal rate of 19%; that is a derived sum of the ordinary top rate and both surcharges, not a separate statutory band. Certain corporate purchases instead face a special flat rate; never substitute the individual stack. [Official source](https://www.gov.uk/stamp-duty-land-tax/residential-property-rates) [Official source](https://www.gov.uk/guidance/stamp-duty-land-tax-buying-an-additional-residential-property)

For a notifiable ordinary transaction, submit the SDLT return and pay within 14 days of the effective date. Establish whether substantial performance moves that date before completion; do not assume all effective dates are completion dates. [Official source](https://www.gov.uk/guidance/stamp-duty-land-tax-buying-an-additional-residential-property)

### UK03: England and Northern Ireland: mixed use, relief and historic MDR

Non-residential or genuinely mixed-use freehold/premium consideration uses the following marginal bands. A dwelling's garden/grounds do not become non-residential simply because they include fields. A single transaction acquiring six or more dwellings falls within the HMRC non-residential guidance. New non-residential leases also require a separate rental net-present-value computation, not just this premium table. [Official source](https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates)

| Non-residential/mixed price portion (GBP) | Marginal rate | Source |
|---|---|---|
| Up to 150,000 | 0% | https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates |
| Over 150,000 to 250,000 | 2% | https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates |
| Over 250,000 | 5% | https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates |

MDR was abolished for transactions completing or substantially performed from June 2024, but HMRC also identifies protected old contracts. Do not turn that repeal into an unconditional refusal for every later effective date. The exact grandfathering, variations and anti-avoidance tests remain held under H01; no MDR amount may be calculated here. Preserve the old average-price method only as historical context requiring the applicable pre-repeal/protected-contract law. [Official source](https://www.gov.uk/guidance/stamp-duty-land-tax-relief-for-land-or-property-transactions)

Group and charity relief are separate applications with conditions and possible withdrawal. HMRC confirms group-company transactions can qualify and that charity relief depends on charitable use; the original ownership-percentage, acquisition and sub-sale statutory tests are not cleared by this summary. H01 holds those detailed tests, rather than granting a generic group exemption. [Official source](https://www.gov.uk/guidance/stamp-duty-land-tax-relief-for-land-or-property-transactions)

### UK04: Scotland: LBTT and ADS

Apply the ordinary residential price bands below to each slice. A qualifying first-time buyer relief increases the nil band to GBP 175,000; eligibility must be established separately, not inferred from an empty current portfolio. [Official source](https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property)

| Residential price portion (GBP) | LBTT marginal rate | Source |
|---|---|---|
| Up to 145,000 | 0% | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property |
| Over 145,000 to 250,000 | 2% | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property |
| Over 250,000 to 325,000 | 5% | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property |
| Over 325,000 to 750,000 | 10% | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property |
| Over 750,000 | 12% | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property |

ADS is an additional 8% of the relevant consideration, not an addition to individual marginal bands. The current rate took effect on 5 December 2024; the preceding rate was 6%. Check the protected pre-change contract rules, worldwide dwelling ownership, company/non-natural-person rules and the GBP 40,000 inclusive consideration threshold. Since April 2024, individual shares of a dwelling below that ownership-value threshold can be disregarded under the specified rules. Replacement/refund treatment depends on the separate main-residence conditions, disposal/acquisition dates and joint buyers; the ordinary replacement period is 36 months. H01 holds detailed first-time relief eligibility and filing instructions not established in this read. [Official source](https://revenue.scot/taxes/land-buildings-transaction-tax/additional-dwelling-supplement-ads)

### UK05: Wales: use separate main and higher-rate bands

The higher-rate thresholds are not the same as the main-rate thresholds. Apply each table by portions. The current higher rates started on 11 December 2024 and have protected earlier-contract rules. Companies generally pay higher residential rates; individuals must be tested under the actual higher-rate and main-residence-replacement conditions. H01 holds those detailed eligibility and filing procedures. [Official source](https://www.gov.wales/land-transaction-tax-rates-and-bands)

| Main residential price portion (GBP) | Marginal rate | Source |
|---|---|---|
| Up to 225,000 | 0% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 225,000 to 400,000 | 6% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 400,000 to 750,000 | 7.5% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 750,000 to 1,500,000 | 10% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 1,500,000 | 12% | https://www.gov.wales/land-transaction-tax-rates-and-bands |

| Higher residential price portion (GBP) | Marginal rate | Source |
|---|---|---|
| Up to 180,000 | 5% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 180,000 to 250,000 | 8.5% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 250,000 to 400,000 | 10% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 400,000 to 750,000 | 12.5% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 750,000 to 1,500,000 | 15% | https://www.gov.wales/land-transaction-tax-rates-and-bands |
| Over 1,500,000 | 17% | https://www.gov.wales/land-transaction-tax-rates-and-bands |

### DE01: Germany: Land rates, exemptions and notifications

Determine the Land where the property is situated. A federal statutory rate is not proof that every Land uses it. The actual current Saxony authority page confirms 5.5%; the current Hamburg service body also confirms 5.5%. The identified Bremen amendment still requires the actual complete body read before its rate is used. These correct the old combined Bayern/Sachsen row and the old Hamburg figure; Bremen remains held. The remaining Land-rate inventory is retained under H02 pending actual current Land-source reads. [Official source](https://www.steuern.sachsen.de/grunderwerb-und-grundsteuer-4009.html) [Hamburg](https://www.hamburg.de/service/info/11311613/n0/) [Bremen law](https://www.gesetzblatt.bremen.de/fastmedia/218/2025_02_05_GBl_Nr_0009_signed.pdf)

GrEStG section 3 includes an acquisition-value exemption not exceeding EUR 2,500, qualifying spouse/registered-partner and direct-line family transfers, estates and specified estate divisions. Gifts can still be taxable to the extent of deductible burdens. Do not assume every family or estate conveyance qualifies. The detailed acquired right, relationship and consideration need checking against that section. [Official source](https://www.gesetze-im-internet.de/grestg_1983/BJNR017770982.html)

The tax normally falls due one month after notice of assessment, subject to a longer period granted by the authority. Notary notification does not extinguish a separate party-notification duty. Sections 18-20 distinguish reporting persons and events; the share-deal reporting provisions changed during 2026, with commencement and pre-existing-contract rules in section 23. Do not apply the latest procedural deadline retrospectively to an earlier event. Exact reporting-route completion and earlier-period computations are held under H02. [Official source](https://www.gesetze-im-internet.de/grestg_1983/BJNR017770982.html)

### DE02: Germany: indirect ownership and restructuring

Do not reduce every German indirect transfer to a single share percentage and time window. Sections 1(2a) and 1(2b) address changes in partners/shareholders over ten years; sections 1(3) and 1(3a) address consolidation and economic ownership, with their own priority and attribution rules. The headline threshold for those current provisions is 90%, but listed-market exclusions, inheritance treatment, indirect attribution and pre-reform transitional holdings matter. Section 23 preserves specified old rules into 2026 and changes the application of the latest share-deal provisions after July 2026. Complex histories are held for event-by-event application rather than treated as safe below one headline threshold. [Official source](https://www.gesetze-im-internet.de/grestg_1983/BJNR017770982.html)

Sections 5-7 deal with particular co-ownership/partnership restructurings and partitions; they are not a general common-ownership exemption. Section 6a instead has a 95% dependent-company test and five-year before/after conditions for its qualifying restructuring scope. The old general group-percentage proposition must not be used for Germany. Apply the actual transaction and each holding-period condition; unresolved restructure calculations remain H02. [Official source](https://www.gesetze-im-internet.de/grestg_1983/BJNR017770982.html)

### ES01: Spain: regional purchase tax and VAT/AJD split

Identify the autonomous community and whether the seller's supply is a VAT-taxable first delivery or a subsequent/exempt delivery. Do not apply an illustrative region's rate nationwide, assume all previously occupied buildings are outside VAT, or add a generic AJD percentage without identifying the documented act and regional rule. Detailed national VAT/AJD classification and regional rates are held under H03 except the following Catalonia ordinary tariff. [Official source](https://atc.gencat.cat/es/tributs/itpajd/tpo/tarifes-tipus/)

Catalonia's current ordinary real-estate tariff uses the total property value to find an average rate, then applies that rate to the acquired taxable share. It is not simply the purchase of a share that reduces the band threshold. First rule out reduced-rate eligibility, large-holder status and whole-residential-building special treatment. [Official source](https://atc.gencat.cat/es/tributs/itpajd/tpo/tarifes-tipus/)

| Total property-value portions (EUR) | Ordinary marginal tariff used to find average rate | Source |
|---|---|---|
| Up to 600,000 | 10% | https://atc.gencat.cat/es/tributs/itpajd/tpo/tarifes-tipus/ |
| Over 600,000 to 900,000 | 11% | https://atc.gencat.cat/es/tributs/itpajd/tpo/tarifes-tipus/ |
| Over 900,000 to 1,500,000 | 12% | https://atc.gencat.cat/es/tributs/itpajd/tpo/tarifes-tipus/ |
| Over 1,500,000 | 13% | https://atc.gencat.cat/es/tributs/itpajd/tpo/tarifes-tipus/ |

A separate 20% special rate can displace that tariff for relevant large holders or whole residential buildings. The source includes ownership aggregation, excluded properties/buyers and a July 2026 change to stressed-area counting. Those complete special-rate eligibility calculations are not cleared by this matrix and remain H03. Do not use the ordinary table until the special-rate and reduced-rate branches have actually been excluded. [Official source](https://atc.gencat.cat/es/tributs/itpajd/tpo/tarifes-tipus/)

### ES02: Spain: share transfers and anti-avoidance

The current securities-law provision is Law 6/2023 article 338, not the old article number in the earlier matrix. Its general securities-transfer exemption has an anti-avoidance exception. It includes rebuttable presumptions concerning control of entities with Spanish non-business real estate, indirect controlled entities and specified recent contributions of property. A property-rich label alone does not establish the tax or base. Article 338 also specifies asset valuation, control aggregation and proportional bases. Refer an actual indirect transfer for that complete analysis; do not clear it as an ordinary exempt share sale or mechanically charge direct-purchase tax solely because the company owns property. [Official source](https://www.boe.es/buscar/act.php?id=BOE-A-2023-7053#a338)

### FR01: France: departmental DMTO is a dated local lookup

The official June 2026 departmental schedule has separate columns for the temporarily increased departmental rate and the ordinary CGI article 1594 D rate. Its increased-rate column excludes qualifying first-time acquirers and its local-relief columns vary. Therefore the old single combined purchase percentage and the statement that first-time reductions are generally unavailable are not usable national answers. Establish the département, effective date, purchaser/first-home conditions and local deliberation, then verify the other components before computing a combined total. The June schedule does not by itself establish every November local decision or the full combined base. [Official source](https://www.impots.gouv.fr/sites/default/files/media/1_metier/3_partenaire/notaires/dmto/dmto_2026-06.pdf)

New-building VAT/reduced DMTO, family SCI, divorce, forest/agricultural relief, notary payment/filing and property-rich share-transfer rules remain individually held under H04. They are not erased or inferred from this departmental table.

### IT01: Italy: resale and VAT residential branches

For residential transfers outside VAT, ordinary registration tax is 9%, or 2% where prima-casa relief is actually established, with a minimum registration tax of EUR 1,000 and separate mortgage/cadastral charges. For the residential branches in the official purchase guide, those two fixed charges are EUR 50 each. Do not treat every sale by a business as VAT-taxable: construction/refurbishment seller timing and options matter. [Official source](https://www1.agenziaentrate.gov.it/web_app_entrate/guida_acquisto_casa.html)

Where the residential sale is VAT-taxable, ordinary non-luxury housing is generally 10%; the specified luxury cadastral categories are 22%; qualifying prima-casa acquisitions are 4%. In these VAT branches the guide sets registration, mortgage and cadastral charges at EUR 200 each, and VAT is based on the price. None of these headline rates establishes the client's relief entitlement. [Official source](https://www1.agenziaentrate.gov.it/web_app_entrate/guida_acquisto_casa.html)

The cadastral price-value regime is conditional: an eligible natural-person non-business purchase of residential property/eligible appurtenances outside VAT, an express request in the deed and disclosure of the agreed price. It is not the universal tax base for all residential or commercial transactions. [Official source](https://www1.agenziaentrate.gov.it/web_app_entrate/guida_acquisto_casa.html)

Prima-casa eligibility includes the cadastral-category exclusions and municipality/ownership tests, but the fetched guide retains an outdated prior-home sale period and historical expatriate wording. The actual current sale-window amendment and all current relief qualifications are held under H05. Do not grant relief using the old four-condition summary. Ordinary/relieved figures above are branch references, not permission to calculate a relieved liability. The commercial registration/VAT-election branch is also held. [Official source](https://www1.agenziaentrate.gov.it/web_app_entrate/guida_acquisto_casa.html)

### NL01: Netherlands: current law resolves the old general page

The current 2026 Transfer Taxes Act article 14 expressly distinguishes dwelling acquisitions at 8%, qualifying natural-person main-home acquisitions at 2%, and the general 10.4% rate for other real estate. The generic older purchase page's all-other-property formulation does not override this statute. Assess property character, rights and any special statutory exception before applying a rate. [Official source](https://wetten.overheid.nl/BWBR0002740/2026-01-01#HoofdstukII_Afdeling3_Artikel14)

Article 15(1)(p) provides the starter exemption for an adult natural person younger than 35 at acquisition who has never used this exemption, will use the dwelling other than temporarily as a main residence and makes the required written declarations before acquisition. The total dwelling plus appurtenance value must not exceed EUR 555,000 in 2026. This is not a first-ever-home requirement. With joint purchasers, test each purchaser's entitlement; do not divide the property's value to evade the overall value cap. Notarial filing details remain H06. [Official source](https://wetten.overheid.nl/BWBR0002740/2026-01-01#HoofdstukII_Afdeling3_Artikel14) [Government explanation](https://www.rijksoverheid.nl/themas/bouwen-en-wonen/huis-kopen/vraag-en-antwoord/huis-kopen/vrijstelling-overdrachtsbelasting)

### PT01: Portugal: establish the rate regime before using a table

Use the higher of the relevant purchase/contract value and VPT, subject to the transaction-specific base rules. Distinguish mainland from Madeira/Azores, permanent own home from other housing, rustic land from other urban property, and purchaser residence. The Model 1 IMT declaration precedes the deed; payment/exemption proof is required at signing. The current AT procedure issues payment documents after submission and requires payment on assessment day or within the following 30 days. [Official source](https://info.portaldasfinancas.gov.pt/pt/apoio_ao_contribuinte/Cidadaos/Casa_e_propriedades/Compra_da_casa/Paginas/default.aspx)

The following 2026 circular table is only the mainland permanent-own-home ordinary branch. The last two rows are whole-base flat rates, not marginal slices. For progressive rows, use base times the stated rate less the stated deduction. It is not a non-resident, second-home, youth-exemption or islands table. [Official source](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf)

| Mainland permanent-home taxable base (EUR) | Ordinary rate and deduction (EUR) | Source |
|---|---|---|
| Up to 106,346 | 0% | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf |
| Over 106,346 to 145,470 | 2%, less 2,126.92 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf |
| Over 145,470 to 198,347 | 5%, less 6,491.02 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf |
| Over 198,347 to 330,539 | 7%, less 10,457.96 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf |
| Over 330,539 to 660,982 | 8%, less 13,763.35 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf |
| Over 660,982 to 1,150,853 | 6% of whole base | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf |
| Over 1,150,853 | 7.5% of whole base | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf |

Other housing and island transactions have their own separate circular tables. Do not transplant this table. Their separate tables are present in the circular, but the complete applicable island/other-home computations remain unconfirmed here under H07. Do not infer that they share the permanent-home table. Rustic property has a statutory 5% rate; other urban acquisitions outside the housing categories have 6.5%, reversing the old label order. The blacklist-entity rate has separate scope/exceptions and must not be confused with ordinary residence. [Official source](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cimt/Pages/cimt17.aspx)

Current article 17(10) also sets a 7.5% non-resident residential rule with specified exceptions for existing IRS residence, obtaining residence within two years, or qualifying capped-rent letting begun within six months and maintained for the required period. Article 17(11)-(12) provide reimbursement/application conditions. The current consolidated body proves these conditions exist; exact mid-year commencement, July amendment effects and the complete capped-rent/reimbursement calculation remain H07. Consequently do not apply the ordinary table to a non-resident or infer a full-year date boundary from the January circular. [Official source](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cimt/Pages/cimt17.aspx)

Stamp duty under TGIS item 1.1 is 0.8% on the relevant real-estate transfer base, subject to an actual exemption; credit can trigger a separate stamp duty. It is not included in IMT. [Official source](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/selo/Pages/ccod-selo-tabgiselo.aspx) [Official source](https://info.portaldasfinancas.gov.pt/pt/apoio_ao_contribuinte/Cidadaos/Casa_e_propriedades/Compra_da_casa/Paginas/default.aspx)

### SG01: Singapore: buyer duty

BSD uses the higher of consideration and market value, with acquisition/gift/trust and linked dependent-instrument rules. First classify residential and non-residential components. These are marginal slices, not flat whole-price rates. [Official source](https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/buyer%27s-stamp-duty-%28bsd%29)

| Price/value portion (SGD) | Residential BSD | Non-residential BSD | Source |
|---|---|---|---|
| First 180,000 | 1% | 1% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/buyer%27s-stamp-duty-%28bsd%29 |
| Next 180,000 | 2% | 2% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/buyer%27s-stamp-duty-%28bsd%29 |
| Next 640,000 | 3% | 3% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/buyer%27s-stamp-duty-%28bsd%29 |
| Next 500,000 | 4% | 4% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/buyer%27s-stamp-duty-%28bsd%29 |
| Next 1,500,000 | 5% | 5% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/buyer%27s-stamp-duty-%28bsd%29 |
| Remaining amount after the slices above | 6% | 5% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/buyer%27s-stamp-duty-%28bsd%29 |

The non-residential rate remains 5% above the preceding threshold; the extra residential top step does not apply to it. Additional buyer duty must be tested separately.

### SG02: Singapore: ABSD profiles are not a nationality-only test

Check the buyer's status at acquisition, every residential interest counted in Singapore, beneficial/trust ownership, joint buyers and remission/treaty entitlement. Generally the highest applicable joint-buyer rate applies to the whole acquired value. Do not count overseas properties as Singapore residential holdings. These current headline rates apply before any established remission. The source includes special FTA treatment, so a foreign passport alone does not prove the foreign-individual rate. [Official source](https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer%27s-stamp-duty-%28absd%29)

| Buyer profile, with no applicable remission | ABSD | Source |
|---|---|---|
| Singapore citizen, first residential property | 0% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer%27s-stamp-duty-%28absd%29 |
| Singapore citizen, second / third or later | 20% / 30% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer%27s-stamp-duty-%28absd%29 |
| Permanent resident, first / second / third or later | 5% / 30% / 35% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer%27s-stamp-duty-%28absd%29 |
| Foreign individual not entitled to preferential treatment | 60% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer%27s-stamp-duty-%28absd%29 |
| Entity or trustee acquisition | 65%, subject to its actual applicable rules/remission | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer%27s-stamp-duty-%28absd%29 |
| Qualifying housing-developer branch | 35% potentially remittable plus 5% non-remittable | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer%27s-stamp-duty-%28absd%29 |

Developer remission is conditional, not an automatic discount on completion. Identifiable-beneficiary trust refunds have their own conditions and claim deadline. H08 holds the complete developer/trust/FTA remission computations. Round duty as the actual IRAS rules require; do not apply a remission merely to improve the answer.

### SG03: Singapore: seller duty uses acquisition cohort

Residential SSD for property acquired from July 2025 changed to a four-year schedule. Use the acquisition date and disposal date of the relevant interest; accepted options, inherited interests, divorce transfers and rezoning can affect those dates. Apply duty to the higher of price and market value of the disposed interest. Exemptions must be separately established. [Official source](https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-residential-property)

| Residential acquisition cohort | Disposal holding interval | SSD | Source |
|---|---|---|---|
| From 11 March 2017 through 3 July 2025 | Up to one / over one to two / over two to three years | 12% / 8% / 4% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-residential-property |
| From 11 March 2017 through 3 July 2025 | Over three years | 0% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-residential-property |
| From 4 July 2025 | Up to one / over one to two / over two to three / over three to four years | 16% / 12% / 8% / 4% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-residential-property |
| From 4 July 2025 | Over four years | 0% | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-residential-property |

Industrial SSD is a different regime. For relevant industrial property acquired from 12 January 2013, its successive holding-period rates are 15%, 10% and 5% within the first, second and third years, then none. Do not use the old residential schedule or confuse the industrial last-year rate with its first-year rate. Public/compulsory/disposal exemptions require the actual listed conditions. Industrial and residential mixed components must be separated. [Official source](https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-industrial-property)

IRAS directs payment through myTax Portal. The seller's law firm must complete the SSD declaration. IRAS advises retaining it for at least five years and may request it for audit; it is not ordinarily submitted with the tax. The current payment deadline and execution-location filing rules, together with detailed remission/exemption applications, remain H08 rather than being inferred from the disposal date. [Official source](https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-residential-property)

### HK01: Hong Kong: corrected dates and current AVD schedule

The official BSD and SSD notices say instruments executed from 28 February 2024 are no longer subject to those duties. The old October 2023 abolition date must not be used. Earlier instruments still need their historical law, not the current abolition rule. [Official source](https://www.ird.gov.hk/eng/faq/bsd.htm) [Official source](https://www.ird.gov.hk/eng/faq/ssd.htm)

The actual AVD FAQ gives a new residential schedule for instruments executed from February 2026, including a new upper band. It is not sufficient to quote the old maximum rate or an old first-home/HKPR-only scale label. Use the full sliding relief, not just the ordinary percentage rows. The usable schedule below begins on 26 February 2026; earlier 2026 rates remain H09. [Official source](https://www.ird.gov.hk/eng/faq/avd.htm)

| Residential consideration/value (HKD), from that date | AVD, including marginal relief | Source |
|---|---|---|
| Up to 4,000,000 | 100 | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 4,000,000 to 4,323,780 | 100 plus 20% of excess over 4,000,000 | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 4,323,780 to 4,500,000 | 1.5% | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 4,500,000 to 4,935,480 | 67,500 plus 10% of excess over 4,500,000 | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 4,935,480 to 6,000,000 | 2.25% | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 6,000,000 to 6,642,860 | 135,000 plus 10% of excess over 6,000,000 | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 6,642,860 to 9,000,000 | 3% | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 9,000,000 to 10,080,000 | 270,000 plus 10% of excess over 9,000,000 | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 10,080,000 to 20,000,000 | 3.75% | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 20,000,000 to 21,739,120 | 750,000 plus 10% of excess over 20,000,000 | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 21,739,120 to 100,000,000 | 4.25% | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 100,000,000 to 109,574,470 | 4,250,000 plus 30% of excess over 100,000,000 | https://www.ird.gov.hk/eng/faq/avd.htm |
| Over 109,574,470 | 6.5% | https://www.ird.gov.hk/eng/faq/avd.htm |

Use the official integer-dollar boundaries/rounding when completing an actual instrument. The non-residential schedule shares the lower steps but its upper treatment differs: do not reuse the new residential upper band for non-residential property. Detailed exemptions, mixed property, historical non-resident/AVD transitions and stamping procedure remain H09.

### AU01: Australia: state-based duty, with a limited current WA overlay

There is no one Australian property-duty rate. Preserve separate NSW, Victoria, Queensland, WA, SA, Tasmania, ACT and NT analyses. Foreign-person definitions, reliefs, landholder duty and annual land tax must be tested separately. The actual interstate comparison is explicitly a fiscal-year snapshot, not proof that every figure continued unchanged throughout 2026. H10 therefore retains all original state/territory rate and surcharge topics without offering those old summaries as current calculations. [Official source](https://www.wa.gov.au/system/files/2025-11/ostr-2025-26.pdf)

The current WA authority page confirms an additional 7% for foreign persons acquiring residential property, with separate individual/corporation/trust definitions. Residential purpose includes intended conversion/development; specified aged-care, commercial-residential and retirement premises are excluded. Each land purchaser must complete the foreign-duty declaration even for commercial land. Actual development and spouse/de facto exemptions have their own conditions; they are not automatic. A foreign person can owe duty despite a visa that permits an indefinite but conditional stay. Full general WA duty and other state calculations remain H10. [Official source](https://www.wa.gov.au/government/publications/foreign-transfer-duty)

### NZ01: New Zealand: purchase eligibility is not a tax rate

The current LINZ guidance distinguishes unrestricted, consent-required and ineligible purchasers. New Zealand citizenship, residence-class visa plus ordinary residence, and Australian/Singaporean status have different consequences. Residential/lifestyle land and otherwise-sensitive land also differ. Consent must be obtained under the applicable route before an unconditional purchase/completion; the page recognises qualifying investor-visa housing pathways, so an absolute foreign-buyer ban is unsafe. Verify the actual buyer and land route, not simply tax residence. [Official source](https://www.linz.govt.nz/guidance/overseas-investment/buying-residential-property-live)

The old stamp-duty abolition proposition and bright-line history are retained under H11, not silently treated as verified purchase-tax or disposal-tax guidance. Bright-line tax is a disposal income-tax topic outside the core purchase-tax computation; a dated acquisition alone must not determine the period for a current disposal.

### JP01: Japan: acquisition tax and registration tax are separate

Registration tax is charged when registering the ownership transfer, using the fixed-asset assessed value. The NTA current table gives 1.5% for a land sale registration through 31 March 2029, ordinary building transfer registration at 2%, and a 0.3% qualifying residential-house transfer branch. The latter requires a qualifying house acquired by 31 March 2027, registration within one year of construction/acquisition, owner occupation and registered floor area of at least 50 square metres. Existing housing must also meet the stated seismic requirements or have been constructed from January 1982, together with the other applicable conditions. The municipal certificate must accompany the registration application; supplying it later does not obtain the relief. Other savings for particular certified housing have separate conditions and are not automatically included in that branch. [Official source](https://www.nta.go.jp/publication/pamph/koho/kurashi/html/05_1.htm)

The prefectural real-estate acquisition tax is a separate charge. The old land/building acquisition rates and their base reductions are held under H12 because the attempted prefectural source did not open. Never label the registration table as the acquisition-tax table. H12 also holds transaction-specific application of the time-limited housing reductions.

### CA01: Canada: Ontario and Toronto

Provincial and municipal layers are separate. Ontario's general rates are marginal on the value of consideration, which can include assumed liabilities and associated benefits. The highest residential step below applies only where the transfer contains the specified one or two single-family residences; do not apply it indiscriminately to commercial land. [Official source](https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax)

| Ontario price portion (CAD), ordinary current branch | Marginal rate | Source |
|---|---|---|
| Up to 55,000 | 0.5% | https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax |
| Over 55,000 to 250,000 | 1% | https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax |
| Over 250,000 to 400,000 | 1.5% | https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax |
| Over 400,000 to 2,000,000, qualifying residential branch | 2% | https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax |
| Over 2,000,000, qualifying one/two single-family residence branch | 2.5% | https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax |

For other property, the ordinary rate over CAD 400,000 remains 2%. Historical agreements and first-home refunds require separate tests. Ontario NRST is an additional 25% under its current branch for foreign nationals, foreign corporations or taxable trustees acquiring the relevant residential interests; citizenship/permanent residence/registered-Indian exclusions and earlier agreement/assignment transitions matter. It is applied to the same consideration rather than to the consideration plus LTT. It is not a surcharge on every person who lives outside Ontario. Detailed exemptions/refunds are H13. [Official source](https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax) [Official source](https://www.ontario.ca/document/non-resident-speculation-tax)

Toronto adds MLTT. Its current residential table changed during April 2026 and has additional upper bands; the old summary ending at the previous ordinary top rate is incomplete. From that change, one/two single-family residences use these marginal steps in addition to Ontario LTT. [Official source](https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/)

| Toronto MLTT residential price portion (CAD), from 1 April 2026 | Marginal rate | Source |
|---|---|---|
| Up to 55,000 / over 55,000 to 250,000 / over 250,000 to 400,000 | 0.5% / 1% / 1.5% | https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/ |
| Over 400,000 to 2,000,000 / over 2,000,000 to 3,000,000 | 2% / 2.5% | https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/ and https://www.toronto.ca/legdocs/municode/1184_760.pdf |
| Over 3,000,000 to 4,000,000 / over 4,000,000 to 5,000,000 | 4.40% / 5.45% | https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/ |
| Over 5,000,000 to 10,000,000 / over 10,000,000 to 20,000,000 | 6.5% / 7.55% | https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/ |
| Over 20,000,000 | 8.60% | https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/ |

The current city page has a missing zero in the printed upper endpoint of its lower residential step. The archived consolidated Municipal Code confirms the unchanged lower boundary; it is used only for that corroboration, not to establish the later upper-rate amendment. [Municipal Code, section 760-9.2(A)(4)-(5)](https://www.toronto.ca/legdocs/municode/1184_760.pdf). Toronto also identifies a municipal non-resident speculation tax, separate from both LTT layers. Its complete buyer, transition and exemption rules, the earlier 2026 MLTT schedule and municipal filing procedure remain H13; do not omit the municipal foreign-buyer test or guess the earlier bands. [Official source](https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/)

### CA02: Canada: UHT repeal and unconfirmed annual/local layers

The current federal Act sections 1.1 and 6.1 expressly remove UHT payable and the return requirement for calendar years from 2025 onward. Thus no 2026 UHT or annual UHT return should be imposed under the old matrix. Earlier-year liabilities, returns, exclusions and exemptions are separate; the repeal does not erase those historic obligations. The old trust/corporate/occupancy shorthand is not adequate to resolve an earlier year and remains H13. [Official source](https://laws-lois.justice.gc.ca/eng/acts/U-0.5/FullText.html)

British Columbia property transfer tax/additional foreign-buyer duty, Quebec municipal transfer duties, Alberta and Saskatchewan title fees, Manitoba LTT, Nova Scotia municipal/provincial layers, PEI/New Brunswick/Newfoundland and Labrador, BC speculation/vacancy tax and municipal vacant-home taxes in Toronto/Vancouver/Montreal all remain distinct topics. Their original rates and exemptions are retained as H13, not cleared from Ontario law or assumed unchanged. Annual ownership taxes are a separate scope; a vacancy-tax declaration can matter even where no purchase duty is due.

### IE01: Ireland: Help to Buy is an income-tax refund

This is not a transfer-duty exemption. The current Revenue page distinguishes the earlier enhanced relief from the further enhanced relief for qualifying contracts/first mortgage drawdowns from 7 October 2026 through 31 December 2029. The earlier enhanced branch runs through 6 October 2026 with a maximum of EUR 30,000. The maximum became EUR 35,000 for the later branch; the refund is the lesser of that cap, 10% of the qualifying purchase value/approved self-build valuation and qualifying income tax/DIRT paid for the preceding four years. USC and PRSI do not count; the cap is per property, not per buyer. [Official source](https://www.revenue.ie/en/property/help-to-buy-incentive/how-much-can-you-claim.aspx)

The property must be a qualifying new home/self-build for the buyer's home, not an investment, with the required mortgage and value conditions. The Revenue property page requires at least 70% qualifying loan-to-value and a value not exceeding EUR 500,000, with a specific local-authority shared-equity exception. Full first-time-buyer, occupation, tax-compliance, claim and clawback conditions remain H14. Do not calculate an entitlement from the maximum alone. [Official source](https://www.revenue.ie/en/property/help-to-buy-incentive/what-type-of-property-qualifies.aspx)

## When to refuse or refer

Do not issue a filing-ready amount while a necessary input, actual property classification, date, rate, surcharge definition, relief condition or return process is unresolved. Do not treat a blocked page, a generic authority homepage, the old `[T1]` markers or a historical snapshot as confirmation. The following are **non-usable source holds**, not instructions or safe harbours. Every original claim is retained in the writer's original-line destination record, including errors corrected above.

- **H01, UK relief/filing limits:** the complete England/NI historical first-time ownership test; exact MDR protected-contract/variation tests and historical average-price computation; Schedule 7 group ownership and withdrawal; charity, acquisition and sub-sale conditions; full Scotland first-time relief eligibility and filing process; Wales higher-rate individual/trust and main-residence replacement tests and filing. The old unconditional post-repeal MDR refusal is withdrawn. Do not infer a universal 75%-group rule or complete local filing method from a summary page.
- **H02, German regional and complex branches:** actual current rate sources for Bayern, Niedersachsen, Sachsen-Anhalt, Mecklenburg-Vorpommern, Thüringen, Rheinland-Pfalz, Berlin, Hessen, Baden-Württemberg, Saarland, Schleswig-Holstein, Nordrhein-Westfalen and Brandenburg. The old Hamburg direction claim and Sachsen grouping are corrected; the old Bremen rate is not cleared, and the identified amendment remains held. Detailed partnership/co-ownership relief computations, share-event priority/attribution and all pre-/post-July 2026 transition histories need the applicable event-by-event law; notary and party notifications must not be conflated. The old common-ownership percentage and one-window-for-all-share-deals propositions are rejected.
- **H03, Spain:** current complete ITP bands/reliefs for Madrid, Andalucía, Valencia, Galicia, Aragón, Asturias, Murcia, Castilla-La Mancha, Extremadura, Baleares and Canarias; Catalonia special large-holder/whole-building and reduced-rate entitlement, including July 2026 changes; national first/subsequent-delivery VAT classification and elections, new-build ordinary/protected-housing VAT, each regional AJD amount/base and documented-act conditions. The old Catalonia top band and old securities-law article reference are corrected. No national “typical” AJD rate clears a client amount.
- **H04, France:** current local deliberation for the deed date, combined departmental/communal/collection-charge computation and base; temporary-rate first-acquirer definition and qualification; new-build VAT/reduced DMTO; family SCI, divorce, forest/agricultural relief; notarial return/payment procedure; CGI article 726 property-rich share-transfer scope/base. The June table alone is not a November all-départements opinion.
- **H05, Italy:** current complete prima-casa entitlement including the amended prior-home disposal window and expatriate/residence exceptions; commercial property registration/VAT-election rates/bases; current filing/registration process. The official guide actually read still prints historical conditions. The old universal cadastral-base and commercial either/or propositions are rejected; do not use them. The downloaded Gazette PDF's broken text did not establish the unread amendment.
- **H06, Netherlands:** notarial return/payment steps and any transaction-specific exception beyond the ordinary dwelling/main-home/starter branches read. Do not substitute the old first-ever-home, age-inclusive or old threshold claims for current article 15.
- **H07, Portugal:** complete other-housing and Madeira/Azores table bindings, youth exemption and its continuation/clawbacks; exact commencement and later-amendment application of the new non-resident housing regime; capped-rent limits, reimbursements and blacklist-entity exceptions; special taxable bases. Do not apply the January ordinary-home table universally or reuse the old upper-band, second-home or reversed commercial/rustic values.
- **H08, Singapore:** complete FTA, spouse, developer and identifiable-beneficiary trust remission/refund tests and applications; acquisition/disposal date exceptions, industrial or residential exemption claims, and filing deadlines outside the ordinary domestic residential sale scope read. The old developer “completion means automatic remission” and single SSD-cohort descriptions are rejected. ABSD is not established solely by a passport.
- **H09, Hong Kong:** the schedule for instruments before 26 February 2026; all historical AVD/BSD/SSD transitional acquisitions, full reliefs, non-residential/mixed classification and stamping procedure. The old October 2023 abolition and old ordinary upper-band/first-home claims are rejected. Abolition of one tax does not eliminate the other instrument duties.
- **H10, Australia:** current complete standard-duty bands and eligibility/foreign surcharges for NSW, Victoria, Queensland, WA, SA, Tasmania, ACT and NT; NSW/Victoria/Queensland/WA landholder duty; annual foreign-owner land-tax overlays in NSW, Victoria, Queensland, WA and Tasmania; current phase-out/exemption conditions and Victoria commercial/industrial transition. The interstate snapshot is not full-year 2026 authority. In particular the old NSW foreign-duty, Victoria lower-band, ACT range and Tasmania annual-land-tax descriptions cannot be used as current rates. WA's current foreign-duty rule is separately supported above, but its complete exemptions and ordinary calculation remain held.
- **H11, New Zealand:** actual enactment/current non-application of the old stamp-duty abolition proposition; current and historical bright-line disposal periods, exemptions and other land-sale income rules; full investor-visa and other sensitive-land exceptions beyond the LINZ eligibility scope read. The old acquisition-date-only ten-year statement is not a current disposal instruction. Preserve the purchase-consent question even where a tax is absent.
- **H12, Japan:** actual current prefectural acquisition-tax land/building rates, temporary base reductions and exemptions; complete time-limited and certified-housing registration reductions and prefectural/registration filing steps. NTA registration-tax figures cannot prove the separate acquisition-tax amount.
- **H13, Canada:** BC property transfer tax and additional foreign-buyer regional scope; Quebec municipal Welcome Tax bands, Alberta/Saskatchewan title fees, Manitoba LTT, Nova Scotia municipal and provincial non-resident duty, PEI/NB/NL charges; earlier-2026 Toronto MLTT, full municipal foreign-buyer tax, Ontario NRST exclusions/refunds/first-home refund and filing; BC speculation/vacancy tax and Toronto/Vancouver/Montreal vacant-home tax current rates, exemptions and annual declarations; historic UHT years and their affected/excluded owner, trust/corporate/occupancy rules. Federal purchase prohibitions are separate from provincial tax. Do not infer a purchase exemption from no current UHT.
- **H14, Ireland:** full HTB first-time-buyer, occupation, tax-compliance, application/payment and clawback conditions and the applicable earlier enhanced branch. It is a tax-paid-limited rebate, not an automatic amount off stamp duty.
- **H15, other cross-country topics:** South African transfer-duty rates/conditions; UK “land-rich”/group-abuse charge scope beyond ordinary share duty; France property-rich shares, Singapore ACD and Australian landholder thresholds/rates; all unverified intra-group ownership/holding/clawback generalisations. There is no verified worldwide uniform group-percentage or holding period. UK ATED and other annual property taxes remain separately scoped. Load the relevant country/indirect-transfer Guide and obtain the missing official rule before computing.

## Worked cases

These are hypothetical 2026 inputs, not invented client facts. No original worked cases or numerical example inputs existed in the previous version.

### Case 1: England, decide whether established first-time status changes duty

Assume an ordinary single freehold dwelling at GBP 500,000 on 16 November 2026, one individual purchaser intending it as a main home, no linked transaction, no special corporate rate, no additional-property or non-resident surcharge. Compare confirmed first-time eligibility with a purchaser who fails only that relief. The ordinary table yields GBP 15,000; the qualified first-time table yields GBP 10,000. Thus the relief saves GBP 5,000, but only where the independently established conditions are true. A total price above the relief cap would instead remove the relief entirely. Sources: UK01-UK02.

```oa-check
name: England ordinary versus eligible first-time buyer, 2026
inputs:
  price: 500000
steps:
  ordinary: max(min(price, 250000) - 125000, 0) * 0.02 + max(min(price, 925000) - 250000, 0) * 0.05 + max(min(price, 1500000) - 925000, 0) * 0.10 + max(price - 1500000, 0) * 0.12
  first_time: max(price - 300000, 0) * 0.05
  saving: ordinary - first_time
expected:
  ordinary: 15000
  first_time: 10000
  saving: 5000
```

### Case 2: Singapore foreign individual with no remission

Assume one foreign individual buys a residential interest on 16 November 2026 for SGD 2,000,000, equal to market value, with no FTA preference, spouse or other remission and no linked/mixed-use instrument. BSD is SGD 69,600 and ABSD is SGD 1,200,000, total SGD 1,269,600. The combined amount is derived from two separate charges. Do not label it a single statutory purchase-tax rate; seller duty is not this purchaser's BSD/ABSD. Sources: SG01-SG02.

```oa-check
name: Singapore residential buyer duty plus unrelieved foreign-individual ABSD, 2026
inputs:
  value: 2000000
steps:
  bsd: min(value, 180000) * 0.01 + max(min(value, 360000) - 180000, 0) * 0.02 + max(min(value, 1000000) - 360000, 0) * 0.03 + max(min(value, 1500000) - 1000000, 0) * 0.04 + max(min(value, 3000000) - 1500000, 0) * 0.05 + max(value - 3000000, 0) * 0.06
  absd: value * 0.60
  total: bsd + absd
expected:
  bsd: 69600
  absd: 1200000
  total: 1269600
```

## Output and completion checklist

The reviewer brief must include property classification; purchaser and beneficial-owner profiles; existing portfolio; dated regional ordinary-band calculation; each foreign/additional-home overlay; each granted/refused/held relief; VAT versus transfer-tax classification/election; indirect share/landholder anti-abuse; annual surcharges flagged for separate scope; actual filing/payment schedule and proof requirements; and open questions labelled `[T2]` or `[T3]`. Do not delete an unresolved topic from the brief to make the amount look complete.

- [ ] The property/date and subnational jurisdiction match the schedule.
- [ ] England's current residential thresholds and additional-property rules were used only where applicable; MDR grandfathering was not ignored.
- [ ] Scottish ADS and Wales higher-rate bands were kept separate from England's rules.
- [ ] Each German Land rate and each Spanish CCAA branch is actually supported, or held.
- [ ] Italian relief/base conditions were not reduced to the old four-point test.
- [ ] Singapore buyer profile, dwelling sequence, remission and seller acquisition cohort were tested separately.
- [ ] Hong Kong abolition and rate-change dates match the instrument.
- [ ] Australian foreign-buyer, landholder and annual tax layers were not conflated.
- [ ] Canadian provincial, municipal and foreign-buyer layers were considered without imposing repealed current UHT.
- [ ] Share/landholder anti-abuse and all corporate/trust conditions were considered; no uniform group exemption was invented.
- [ ] Every `[T2]`/`[T3]` question and non-usable hold remains visible to the reviewer.

## Sources

Read dates below mean actual reading of the stated scope. Failed direct fetches are preserved separately; readable web-reader bodies are distinguished from ordinary downloads. A current page does not establish every historical or future period. The original generic evidence markers supplied no actual source links.

| Source | Official URL | Read on | Actual scope and limit |
|---|---|---|---|
| uk-res | https://www.gov.uk/stamp-duty-land-tax/residential-property-rates | 2026-11-16 | Read for: Residential rates and first-time buyers, extracted lines 75-205; Non-UK-resident residential surcharge and ordinary bands, extracted75-205 |
| uk-higher | https://www.gov.uk/guidance/stamp-duty-land-tax-buying-an-additional-residential-property | 2026-11-16 | Read for: Higher-rates conditions, companies, joint ownership, main-residence replacement and filing, extracted 85-265 |
| uk-nonres-correct | https://www.gov.uk/stamp-duty-land-tax/nonresidential-and-mixed-rates | 2026-11-16 | Read for: Classification, freehold/premium table and new lease qualification, extracted75-145 |
| uk-reliefs | https://www.gov.uk/guidance/stamp-duty-land-tax-relief-for-land-or-property-transactions | 2026-11-16 | Read for: MDR section and group/charity relief summaries, extracted112-184 and210-265 |
| scot-general | https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property | 2026-11-16 | Read for: Current residential table and first-time nil band, extracted137-233 |
| scot-ads | https://revenue.scot/taxes/land-buildings-transaction-tax/additional-dwelling-supplement-ads | 2026-11-16 | Read for: Rate transition, charge scope, ownership threshold and replacement/refund conditions, extracted140-244 |
| wales-rates | https://www.gov.wales/land-transaction-tax-rates-and-bands | 2026-11-16 | Read for: Actual readable government web-reader body, main and higher tables plus date/transition notes; direct fetch403 |
| de-sachsen | https://www.steuern.sachsen.de/grunderwerb-und-grundsteuer-4009.html | 2026-11-16 | Read for: Current Grunderwerbsteuer paragraph, extracted lines 125-128 |
| de-hamburg | https://www.hamburg.de/service/info/11311613/n0/ | 2026-11-16 | Read for: Actual web-reader Hamburg service operative body, paragraphs 26-71, rate andnotification/payment sequence |
| de-act | https://www.gesetze-im-internet.de/grestg_1983/BJNR017770982.html | 2026-11-16 | Read for: Sections3,15,18-20 and23 including2026 commencement, extracted108-133,291-293,342-430,460-490; Complete sections1,3,5-7 and6a and current section23 transition provisions, extracted1-173 and460-490 |
| cat-rates | https://atc.gencat.cat/es/tributs/itpajd/tpo/tarifes-tipus/ | 2026-11-16 | Read for: Ordinary total-value tariff, large-holder and whole-building gates with2026 counting changes/exceptions, extracted280-440 |
| es-art338 | https://www.boe.es/buscar/act.php?id=BOE-A-2023-7053#a338 | 2026-11-16 | Read for: Complete article338(1)-(3), extracted5540-5558 |
| fr-dmto | https://www.impots.gouv.fr/sites/default/files/media/1_metier/3_partenaire/notaires/dmto/dmto_2026-06.pdf | 2026-11-16 | Read for: June2026 schedule header, separate rate/first-acquirer columns and departmental entries, extracted1-240 |
| it-house | https://www1.agenziaentrate.gov.it/web_app_entrate/guida_acquisto_casa.html | 2026-11-16 | Read for: Residential resale/VAT tables, price-value conditions, prima-casa categories/residence/ownership and stale one-year text, extracted180-392,440-690 |
| nl-law | https://wetten.overheid.nl/BWBR0002740/2026-01-01#HoofdstukII_Afdeling3_Artikel14 | 2026-11-16 | Read for: Current2026 article14 and15(1)(p), extracted766-800 and1030-1051 |
| nl-government | https://www.rijksoverheid.nl/themas/bouwen-en-wonen/huis-kopen/vraag-en-antwoord/huis-kopen/vrijstelling-overdrachtsbelasting | 2026-11-16 | Read for: Actual complete web-reader government exemption/rates body, lines 6-43; eachjointbuyer,wholevalue,onceonlynotfirsthome |
| pt-buy | https://info.portaldasfinancas.gov.pt/pt/apoio_ao_contribuinte/Cidadaos/Casa_e_propriedades/Compra_da_casa/Paginas/default.aspx | 2026-11-16 | Read for: Base, purchaser purpose/residence, Model1 beforedeed and payment workflow, extracted32-71 |
| pt-2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_40129_2026.pdf | 2026-11-16 | Read for: Complete2026 circular tablesI-VI; candidate usesTableI only, extracted1-205 |
| pt-art17 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cimt/Pages/cimt17.aspx | 2026-11-16 | Read for: Completecurrentarticle17 with amendednonresidentparagraphs10-12, extracted31-280 |
| pt-selo | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/selo/Pages/ccod-selo-tabgiselo.aspx | 2026-11-16 | Read for: TGISitem1.1 andneighboritem1.2, extracted31-39 |
| sg-bsd | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/buyer%27s-stamp-duty-%28bsd%29 | 2026-11-16 | Read for: Actual IRAS web-reader body plus full unchanged-stock extraction: requirement/linkedtransactions/currenttable and nearest-dollar rounding; ordinary urllib fetch 403 |
| sg-absd | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer%27s-stamp-duty-%28absd%29 | 2026-11-16 | Read for: Actual IRAS web-reader body plus full unchanged-stock extraction from Determining ABSD liability through current/prior rate explanation; FTAreadercontext separately; ordinary urllib fetch 403 |
| sg-ssd | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-residential-property | 2026-11-16 | Read for: Actual IRAS web-reader and full unchanged-stock extraction, determining liability through administration: acquisition/salecohorts,basis,exemptions,declaration; ordinary urllib fetch 403 |
| sg-industrial | https://www.iras.gov.sg/taxes/stamp-duty/for-property/selling-or-disposing-property/seller%27s-stamp-duty-%28ssd%29-for-industrial-property | 2026-11-16 | Read for: Actual IRAS web-reader and full unchanged-stock extraction: all liability/date/rate,basis,exemption,administration sections; ordinary urllib fetch 403 |
| hk-avd | https://www.ird.gov.hk/eng/faq/avd.htm | 2026-11-16 | Read for: CurrentFAQ1fullresidential/nonresidentialtables andFAQ2 historicalreferral, extracted145-212 |
| hk-bsd | https://www.ird.gov.hk/eng/faq/bsd.htm | 2026-11-16 | Read for: Introductory abolition notice, extracted125-190 |
| hk-ssd | https://www.ird.gov.hk/eng/faq/ssd.htm | 2026-11-16 | Read for: Introductory abolition notice, extracted125-205 |
| au-overview | https://www.wa.gov.au/system/files/2025-11/ostr-2025-26.pdf | 2026-11-16 | Read for: Dated2025-26 interstate transferduty andforeignsurcharge comparisons, extracted470-675; no2026-27continuityclaimed |
| au-wa-foreign | https://www.wa.gov.au/government/publications/foreign-transfer-duty | 2026-11-16 | Read for: Current23October2026 body: definitions, property andexemptions, extracted281-412 |
| nz-invest | https://www.linz.govt.nz/guidance/overseas-investment/buying-residential-property-live | 2026-11-16 | Read for: Completecurrentbuyereligibility, ordinarilyresident, partner/sensitive-land andconsentconditions, extracted190-320 |
| jp-registration | https://www.nta.go.jp/publication/pamph/koho/kurashi/html/05_1.htm | 2026-11-16 | Read for: NTAregistration-tax table, dates, qualifyinghouseconditions andcertificate timing, extracted253-298 |
| on-rates | https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax | 2026-11-16 | Read for: Completeconsideration/rate/residentialqualifier andhistoricalagreement scope, extracted140-245 |
| on-nrst | https://www.ontario.ca/document/non-resident-speculation-tax | 2026-11-16 | Read for: Currentrate, foreignentitydefinition andagreement/assignmenttransitions, extracted120-200 |
| toronto-rates | https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/ | 2026-11-16 | Read for: CompletecurrentMLTTtableresidential/nonresidentialandMNRSTwarning, extracted1-104 |
| toronto-bylaw | https://www.toronto.ca/legdocs/municode/1184_760.pdf | 2026-11-16 | Read for: Archived September 2023 consolidation, section 760-9.2(A)(1)-(5) and B; only unchanged lower-table/boundary corroboration, not the 2026 upper amendment |
| ca-uht-act | https://laws-lois.justice.gc.ca/eng/acts/U-0.5/FullText.html | 2026-11-16 | Read for: Currentenactedsections1.1and6.1 with2026amendmentnotes, extracted140-160and710-724 |
| ie-htb-amount | https://www.revenue.ie/en/property/help-to-buy-incentive/how-much-can-you-claim.aspx | 2026-11-16 | Read for: Current2026earlier/furtherenhanceddates,caps,lesser-of formula,taxpopulationandpropertycap, extracted61-109 |
| ie-htb-property | https://www.revenue.ie/en/property/help-to-buy-incentive/what-type-of-property-qualifies.aspx | 2026-11-16 | Read for: Property/newbuild,70%mortgage,500kvalueandshared-equityexception, extracted60-103 |

Not yet confirmed: H01 UK relief transitions/eligibility and local filing; H02 remaining German Land rates and complex event/notification/restructure histories; H03 other Spanish regions, full Catalonia special/reduced eligibility and VAT/AJD; H04 France complete current local/combined/relief/new-build/share/filing rules; H05 Italy amended complete prima-casa and commercial/filing rules; H06 Netherlands notarial process/special cases; H07 Portugal islands/other housing/youth/blacklist and full new non-resident dated operation; H08 Singapore full remission/exemption and other filing branches; H09 Hong Kong earlier2026 and other complete instrument branches; H10 Australian complete current state/annual/landholder rules; H11 NZ stamp-duty/bright-line and remaining foreign-investment branches; H12 Japan acquisition tax/full reductions and filing; H13 Canadian other provinces, annual taxes, historical UHT and full local exemptions/processes; H14 Ireland complete HTB eligibility/claim/clawback; H15 South Africa and other indirect-transfer/group/annual regimes. Details and retained conditions are in the non-usable hold section above. These gaps are not comprehensive coverage.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Property transfer tax rules change frequently with budget cycles and have material magnitude in transactions. Every output must be reviewed and signed off by a credentialed local conveyancing solicitor / notary / tax practitioner before completion.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `property-transfer-tax-matrix` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/property-transfer-tax-matrix. If neither is available, confirm every figure against the official source pages cited above before relying on it.
