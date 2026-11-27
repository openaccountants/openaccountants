---
name: italy-vat-return
description: "Prepare Italian ordinary-regime periodic IVA settlements, quarterly LIPE and F24 payments for 2026: invoice evidence, VP fields, credits, monthly or elected quarterly deadlines, reverse charge, split payment, deduction limits and late-payment correction."
version: 2.4
jurisdiction: IT
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - vat-workflow-base
  - eu-vat-directive
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Italian VAT return: periodic IVA settlement, LIPE and payment (2026)

## Who this applies to

Italian sole traders, professionals and companies using the ordinary IVA regime. Settle the VAT period, pay any debt and separately communicate the quarterly LIPE. A bank statement is a reconciliation aid: prepare the return from invoices, customs documents and VAT registers, with the tax point, receipt/registration dates and prior credits established. D.P.R. 633/1972 art. 1; D.P.R. 100/1998 art. 1; LIPE instructions.

Use `vat-workflow-base` and `eu-vat-directive` alongside. [Annual IVA return](it-dichiarazione-iva-annuale.md), [e-invoicing](italy-einvoice.md), [forfettario](it-regime-forfettario.md), [bookkeeping](italy-bookkeeping.md), [IRPEF](it-income-tax.md), [employee IRPEF](it-irpef-employees.md), [IRES](it-ires-corporate-tax.md), [payroll](italy-payroll.md) and [cross-border](it-cross-border.md) remain separate jobs.

**Special cases, held rather than calculated here:** forfettario (including entry/exit and reverse-charge payment timing), minimi, agricultural and travel-agent regimes, margin schemes, IVA groups/group settlements, IVA per cassa, pro rata and capital-goods adjustment/refund entitlement, non-resident registration/fiscal representatives, and income-tax depreciation. Check this point with one of our partner accountants. Do not use ordinary-regime calculations for those cases.

This Guide keeps the 2026 tax year. D.Lgs. 10/2026's IVA consolidation applies from January 2027; it does not turn a 2026 transaction into a 2027 transaction. Use the applicable model at transmission and retain the receipt.

## Rates, bands and thresholds

| Item | 2026 rule | Official source |
|---|---|---|
| Standard IVA | 22% | D.P.R. 633/1972 art. 16, https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art16!vig=2026-11-27 |
| Reduced rates | 4%, 5%, 10% only for the exact goods/services and conditions in Tabella A Parts II, II-bis, III; art. 34 agricultural rules are separate | Art. 16, https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art16!vig=2026-11-27 |
| Illustrative tariff entries | Retail-packaged fresh non-concentrated/unsweetened milk meeting Part II n. 3; butter/cheese n. 4; fresh basil/rosemary/sage and specified oregano/plants Part II-bis n. 1-bis; restaurant food/drink service Part III n. 121. Classification follows the entry, not the merchant's name | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633:1~allA!vig=2026-11-27 |
| Quarterly option | Previous calendar year's volume d'affari no more than EUR 500,000 for services/professionals, EUR 800,000 for other activities; an option is required | D.P.R. 542/1999 art. 7 and L. 183/2011 art. 14(11), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2011-11-12;183~art14!vig=2026-11-27 ; limits in D.P.R. 600/1973 art. 18, https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art18!vig=2026-11-27 |
| Quarterly option interest | 1% on the amount to pay, including the annual quarterly balance; monthly settlement has no option interest | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art7!vig=2026-11-27 |
| Small monthly debt | EUR 100 or less moves to the next payment, with payment by 16 December at latest; December's own amount is paid the next January | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-03-23;100~art1!vig=2026-11-27 |
| Small elected-quarterly debt | EUR 100 or less moves to the next quarter, with payment by 16 November at latest | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art7!vig=2026-11-27 |
| Mixed-use road motor vehicle deduction | 40%, subject to the vehicle definition and exceptions below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art19bis.1!vig=2026-11-27 |
| Representation-goods exception | Goods of unit cost no more than EUR 50; this is not a restaurant-entertainment allowance | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art19bis.1!vig=2026-11-27 |

**Other reduced-rate classifications:** retain the product facts for vegetables/fruit/pulses, bread/pasta/crackers/oil, publications, first homes, orthopaedic aids, school/workplace canteens, social/health/education services, water passenger transport, truffles, winter-sport/mountaineering teaching, young horses, art/antiques/collectables, electricity/gas, medicines, hotels, passenger transport, housing and renovation. Their shorthand names do not establish a tariff entry, social-provider qualification, property condition or significant-goods treatment. If those conditions have not been established, the rate is a non-usable hold. Check this point with one of our partner accountants. Do not assume that all reduced-rate items in an industry share a rate.

## The base

**Settle from the documents.** VAT due is the chargeable output tax less input tax whose deduction is exercised for that period. Purchase documents received and recorded by the following month's fifteenth can support deduction for the operation month, except operations in the previous year. Elected quarterly filers may record sales invoices by the end of the following month with reference to the operation month. D.P.R. 100/1998 art. 1; D.P.R. 542/1999 art. 7(3-bis).

Determine the tax point before using the bank date: domestic services generally follow payment or an earlier invoice; general cross-border B2B services follow completion, periodic accrual or earlier payment (art. 6). Foreign currency follows the operation-date exchange rate, or invoice date if the first date is not indicated, then the nearest preceding quotation if unavailable; the ECB rate may be used for all operations in the calendar year (art. 13(4)). A bank-converted euro figure alone does not establish the VAT conversion.

**LIPE working paper:** one module per month for monthly settlements, one per quarter for quarterly settlements; one quarterly communication. Use euro cents, rounding the third decimal up from five. The following is the ordinary-regime VP mapping from the [official instructions](https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f), pp. 5–8.

| Field | Entry and control |
|---|---|
| VP1 | Reference month/quarter; an art. 7 elected quarterly filer uses code 5 for Q4 |
| VP2 | Net registered/registrable active transactions, including taxable, non-imponibile, exempt, territorial-out-of-scope transactions requiring an invoice, and supplies on which the buyer owes VAT; respect the art. 36-bis dispensation exception |
| VP3 | Net purchases and imports from invoices/customs documents registered in the period, including non-deductible/deferred-tax purchases; not just EU acquisitions |
| VP4 | Tax that became chargeable in the period, including tax the business owes as reverse-charge buyer |
| VP5 | Registered input tax whose deduction is exercised for the period; reverse charge only to the deductible extent |
| VP6 | VP4 minus VP5: positive debt in column 1, otherwise absolute credit in column 2 |
| VP7 | Previous period's debt carried because it did not exceed the small-debt limit; never previous credit |
| VP8 | Previous settlement's credit in the same calendar year, excluding credit requested as refund or offset through IVA TR |
| VP9 | Prior annual return's compensable credit brought into this settlement, net of amounts already brought into earlier settlements; do not double-count VP8 or F24 use |
| VP10 | Specific F24 elementi identificativi payments for first domestic vehicle sales in this period, even if paid earlier; never general EU purchases |
| VP11 | Special tax credits used to reduce this payment, excluding credits offset directly in F24; elected Q4 filers leave blank |
| VP12 | Elected quarterly interest on the amount to pay after applicable credits; elected Q4 filers leave blank here and settle through the annual balance |
| VP13 | Acconto due, even if unpaid, in amount column 2 and method in column 1; omit where below EUR 103.29; methods: historical, forecast, actual, special-sector |
| VP14 | Debt column 1 = positive result of (VP6 column 1 + VP7 + VP12) minus (VP6 column 2 + VP8 + VP9 + VP10 + VP11 + VP13 column 2); negative result's absolute value goes in credit column 2. It is tax due/credit, not tax actually paid. Elected Q4 filers leave blank |

Keep the invoice/register reference, tax point, net base, output tax, deductible input tax, VAT treatment, VP fields, evidence and unresolved facts on each working-paper line. Reconcile VP totals, prior returns, credits, actual F24 payments and the annual return; recalculate the workbook. No invented statutory materiality limits or ABI transaction-code rules.

**Deduction conditions (arts. 19 and 19-bis.1).** Costs must belong to the business and confer deduction entitlement; private-use shares do not. Exempt activities can require pro rata: use the special-case hold. Phones and internet have no universal fixed half deduction: establish business/private use objectively.

| Cost | Treatment |
|---|---|
| Road motor vehicle | The EU authorization remains effective for 2026 under Decision 2007/441/EC as extended by Decision (EU) 2025/2529. The limited class is motor vehicles other than Tabella B(f), excluding agricultural/forestry tractors, normally transporting persons/goods, authorised mass no more than 3,500 kg and no more than eight passenger seats besides the driver. If not exclusively business, deduction is 40%. The limit does not apply where the vehicle is the business's own trading activity or for commercial agents/representatives. Outside that limit, ordinary deduction conditions still apply; a van name or an IT-consultant occupation proves neither use nor entitlement |
| Lease/hire, custody, repairs, tolls and vehicle fuel | Follow the vehicle's deductible share. Retain the required card or other approved traceable-payment proof for fuel; a bank description alone is insufficient |
| Passenger transport | Blocked unless it forms the business's own activity |
| Purchased food/drink | Blocked except own business activity or the specified school/business canteen and workplace-vending cases. Restaurant/accommodation services are distinct; business purpose, an invoice naming the deduction claimant and the representation restriction still matter. For employee beneficiaries, retain their details in the invoice or attached note (AdE circulars 53/E of 2008 and 6/E of 2009) |
| Representation | Blocked, except the unit-cost goods exception above; documenting a client dinner does not create a percentage recovery |
| Residential-property VAT, luxury/aircraft/boat exceptions | Do not apply a generic builders/full-recovery shortcut. Non-usable hold: Check this point with one of our partner accountants |

**Supplier discovery, not supplier tax rules.** Keep the bank-pattern matrix as evidence prompts. No brand, IBAN, personal email, payment code or company suffix decides country, business use, supply type, exemption, tax rate or invoice validity. Until missing evidence is obtained, park the line as unresolved; never invent output VAT, a domestic country or a reverse-charge billing entity. Do not deduct unsupported input tax.

| Patterns retained from the bank library | Evidence to obtain before posting |
|---|---|
| UniCredit, Intesa, BPM, MPS, BPER, BancoPosta, Credem, Revolut, Wise, N26; interest/loan lines | Separate actual financial services, taxable subscriptions and principal; examine documents |
| Agenzia/F24/Riscossione, INPS/INAIL, CCIAA, Comune/Regione | Identify the tax, contribution or fee and whether any separate supply/invoice exists; do not invent recoverable VAT |
| Dogana/customs | Use the import document for VP3/VP5; do not duplicate the bank payment |
| Enel, Eni Plenitude, Edison, A2A, Iren, Hera, Acea; TIM, Vodafone, WindTre, Fastweb, Iliad | Invoice rate, customer use and business share |
| Generali, Allianz, UnipolSai, AXA, Zurich; Poste standard mail, Poste Delivery, SDA, BRT, DHL, GLS, TNT | Exact insured/postal/courier service and invoice treatment; no brand-wide exemption |
| Trenitalia, Italo, ATAC, ATM, GTT, ANM, taxi/Uber, ITA/Ryanair/EasyJet, Autostrade/Telepass | Route, invoice and passenger/vehicle rule; international travel is not automatically absent from VP3 |
| Supermarkets (Esselunga, Conad, Coop, Eurospin, Lidl, Carrefour, Penny, MD, PAM, Despar, Iper), restaurants/bars, hotels, ENI/Q8/IP/Esso/Shell | Invoice, business purpose, representation/food/service distinction, vehicle type and fuel payment proof |
| Google, Microsoft, Adobe, Meta, LinkedIn, Dropbox, Slack, Zoom, Spotify, Atlassian, AWS, Stripe; Notion, Anthropic, OpenAI, Figma, Twilio, Canva, GitHub, HubSpot; Apple/Amazon | Actual legal supplier and establishment involved, business/private purchase and invoice tax; an Italian VAT number alone does not establish an Italian branch supply |
| Stripe/PayPal transaction fees, SumUp/Nexi/Satispay, Italian professional firms | Identify service, supplier's regime and actual invoice; neither automatic exemption nor automatic standard tax |
| Wages/TFR/pension funds, rent/IMU, Airbnb, platform sales/fees, drawings, dividends, owner injections, loan repayments, individual/foreign transfers, cash withdrawals | Identify underlying event, invoice and parties. Cash withdrawal/internal transfer alone creates no VAT purchase; trace later expenditure separately. For property/platform special regimes use the special-case hold |

Bank CSV column names (Data, Descrizione/Causale, Dare, Avere, Saldo) and words such as bonifico, affitto, stipendio, rimborso, versamento, prelievo and giroconto are reading aids. Establish the export's date/decimal/sign conventions; a foreign IBAN is not proof of tax establishment. No bank statement means the reconciliation is incomplete; invoices/registers remain necessary even when a statement exists.

## Deadlines and filing

| Obligation | Ordinary deadline and 2026 calendar application | Official source |
|---|---|---|
| Monthly settlement/payment | Sixteenth of next month; December payable next January. Submit F24 through the applicable telematic channel | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-03-23;100~art1!vig=2026-11-27 ; https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva |
| Elected quarterly payment | First three quarters: sixteenth of second following month, subject to weekend/August shifts. For 2026: 18 May, 20 August, 16 November. Q4: annual balance by 16 March 2027, or the income-tax balance deadline with 0.40% for each month/fraction after that March date, in addition to option interest | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art7!vig=2026-11-27 |
| August and non-working days | Covered fiscal obligations/F24 sums falling on 1–20 August can be completed by 20 August without surcharge; tax payments/filings due Saturday/holiday move to the next working day | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=2026-11-27 ; https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-05-13;70~art7!vig=2026-11-27 |
| LIPE | Q1: 1 June 2026; Q2: 30 September; Q3: 30 November; Q4: 1 March 2027. General rule: last day of second following month, except Q2 at end September. Q4 may instead be in the annual return filed by its February deadline (shifted for the weekend) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig=2026-11-27 ; https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-05;141:1~art51!vig=2027-01-01 ; official LIPE instructions |
| Annual IVA return for 2026 | 1 February–30 April 2027; separate from paying periodic IVA | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art8!vig=2026-11-27 |
| Acconto | Ordinary deadline 27 December, shifted to 28 December 2026; check obligation and method in the annual-return Guide | https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva ; official LIPE instructions |

LIPE is filed electronically, directly or through an authorised intermediary, including credit periods. Exemption applies if there is no annual-return or periodic-settlement duty and that exemption persists. No communication is needed for an entirely empty VP quarter, but carrying a credit from the preceding quarter is data and triggers filing. Correct a LIPE by replacement before the annual return; afterwards correct through the annual return. Retain the transmission receipt, any rejection and successful resubmission. Instructions pp. 1–2.

Invoices for ordinary domestic supplies use SdI under D.Lgs. 127/2015 art. 1(3); check sector-specific exceptions in the invoicing Guide. Art. 21(4) generally allows twelve days from the tax point, or the next month's fifteenth for documented deferred deliveries/services meeting its conditions; general EU B2B services use the next month's fifteenth. Establish VAT registration obligations and sales/purchase/retail registers with the bookkeeping/invoicing Guides; absence of SdI access does not justify ignoring transactions already made.

**Esterometro:** for cross-border transactions in 2026 transmit XML through SdI: outbound by the invoice/document deadline, inbound by the next month's fifteenth after document receipt or performance. Exceptions: customs document, an invoice already transmitted through SdI, or territorially non-Italian purchases no more than EUR 5,000 per operation. This is not a universal small-purchase exemption. D.Lgs. 127/2015 art. 1(3-bis).

## Penalties and interest

| Violation/relief | Rule for the 2026 cases here | Official source |
|---|---|---|
| Late/short payment | 25% of unpaid tax; halved for payment within 90 days; within 15 days the halved amount is reduced to one fifteenth per day | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-11-27 |
| Ravvedimento for uncomplicated voluntary payment correction | Pay tax, reduced penalty and legal interest. For missed payment within 30 days: one tenth of minimum; correction within 90 days: one ninth; by the violation-year return deadline: one eighth; later: one seventh, before the special audit/draft-assessment stages. Notices of liquidation/assessment and statutory automated-control payment notices bar this ordinary route | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-11-27 |
| Legal interest | 1.60% yearly from 1 January 2026, accruing day by day; split a correction spanning rate years | https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=25A06705&atto.dataPubblicazioneGazzetta=2025-12-13&atto.tipoProvvedimento=DECRETO |
| LIPE omitted/incomplete/wrong | EUR 500–2,000, halved for filing/correction within 15 days | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-11-27 |
| Esterometro omitted/wrong | EUR 2 per invoice, monthly maximum EUR 400; halved with monthly maximum EUR 200 if sent/corrected within 15 days; applies to operations from July 2022 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-11-27 |

The post-reform payment penalty applies to violations from September 2024 (D.Lgs. 87/2024 art. 5). Quarterly option interest is additional to late-payment interest/penalty. Do not apply the old bare penalties for non-spettante/inesistente offsets, uninvoiced taxable/exempt transactions, undue deduction, missing/irregular supplier invoices, or reverse-charge omissions/errors without testing the operative minimum, exception and procedural stage. Those outcomes and post-audit one-sixth/one-fifth/one-quarter reductions are non-usable holds. Check this point with one of our partner accountants.

## Cross-border points

- General B2B services follow the customer's establishment (art. 7-ter); property, passenger transport, restaurant and other special place-of-supply rules can override it (arts. 7-quater onwards). Check taxable-person capacity and the establishment receiving the service. An invalid/missing VIES lookup alone does not automatically create Italian standard-rate service VAT.
- First test any exemption, non-imponibile treatment or cross-border small-business franchise: a TD17 does not itself require tax where the supply is exempt/franchised. When the Italian business owes tax on a non-resident's Italian-situs supply, art. 17(2) places the obligation on the buyer: EU supplier invoices are integrated under D.L. 331/1993 arts. 46–47; non-EU services use self-invoicing. General foreign services use TD17 and EU goods acquisitions TD18 under the invoicing specification. Net purchases enter VP3, VAT VP4 and deductible VAT VP5, never VP10–VP12 as purchase bases. If an Italian establishment actually made the supply, art. 17(4) displaces the non-resident rule; wrongly charged Italian VAT is not automatically deductible.
- Domestic construction subcontracting under art. 17(6)(a) excludes services to a general contractor entrusted with all works and is distinct from building cleaning/demolition/plant installation/completion under (a-ter). Taxed-by-option building transfers, qualifying gold, scrap, electronics and energy-sector transactions have their own conditions. Classification/authorization/supply-chain boundaries, including logistics and its interim option, are held if not established. Check this point with one of our partner accountants. Once reverse charge is established, use the VP3/VP4/VP5 mapping above.
- Split-payment sales require an eligible customer and are excluded where the buyer already owes reverse-charge VAT. Public-body status alone is insufficient; check art. 17-ter's listed scope, customer attestation and exclusions (including services subject to income-tax withholding and specified collective-domain management). The listed-company limb was removed for invoices from July 2025. EU Decision 2026/1728 extends the authorization to June 2029. The supplier reports the net in VP2 but excludes that VAT from VP4; a business buyer including split tax in its settlement reports VP4 and deductible VP5. Other buyer payment modes/refund claims: Check this point with one of our partner accountants.
- Export non-imponibile treatment requires art. 8's transport/export evidence. For ordinary intra-EU B2B goods under art. 41(1)(a), establish consideration, movement to another member state, the customer's communicated member-state VAT identification and the recapitulative list or due justification for omission. Do not treat services as art. 41 goods. Imports normally use customs assessment/documents, not blanket postponed accounting (art. 70); special gold/scrap arrangements require their own checks.
- The EU distance-sales/e-services EUR 10,000 test covers the combined qualifying total in both prior and current calendar years; domestic treatment requires establishment only in Italy, qualifying dispatch/recipient facts and no destination-tax election. Other goods/consumers, platform deemed-supplier rules and OSS/IOSS filings are held here. Check this point with one of our partner accountants. Intrastat service thresholds, exclusions and deadlines remain separate unresolved classification inputs: do not infer them from LIPE.

## Two worked examples that recompute

All amounts below are hypothetical case inputs or calculations, not statutory thresholds.

**1. Quarterly software consultancy, Q2 2026 (original case).** Prior-year service volume EUR 300,000 and quarterly option. Italian sales EUR 60,000, German general B2B consulting EUR 20,000, US software EUR 2,000, Italian services EUR 10,000, mixed-use car lease EUR 3,000 plus EUR 660 VAT. Assume all invoices/period conditions and ordinary full deduction except the car are established. VP2 EUR 80,000; VP3 EUR 15,000; VP4 EUR 13,640; VP5 EUR 2,904; debt EUR 10,736, interest EUR 107.36, total EUR 10,843.36. Pay by 20 August and file LIPE by 30 September 2026.

```oa-check
name: Italy quarterly settlement Q2 2026 with reverse charge and car limit
inputs:
  sales_it_22: 60000
  services_to_eu_b2b: 20000
  software_us: 2000
  purchases_it_22: 10000
  car_lease: 3000
steps:
  - vp2: sales_it_22 + services_to_eu_b2b
  - vp3: software_us + purchases_it_22 + car_lease
  - reverse_charge_vat: software_us * 0.22
  - vp4: sales_it_22 * 0.22 + reverse_charge_vat
  - car_vat_deductible: car_lease * 0.22 * 0.40
  - vp5: reverse_charge_vat + purchases_it_22 * 0.22 + car_vat_deductible
  - vp6: vp4 - vp5
  - vp12_interest: vp6 * 0.01
  - vp14: vp6 + vp12_interest
expected:
  vp2: 80000
  vp3: 15000
  vp4: 13640
  car_vat_deductible: 264
  vp5: 2904
  vp6: 10736
  vp12_interest: 107.36
  vp14: 10843.36
```

**2. September 2026 VAT paid late (original case).** A monthly retailer owes EUR 8,000 on 16 October and pays on 26 October: ten days late, before any audit or blocking notice. The within-fifteen-day penalty and within-thirty-day ravvedimento produce EUR 66.67 penalty; ten days' legal interest EUR 3.51. Total EUR 8,070.18, allocated to the appropriate tax, penalty and interest codes after checking the actual F24 instructions.

```oa-check
name: Italy monthly VAT paid 10 days late with ravvedimento (2026)
inputs:
  vat_due: 8000
  days_late: 10
  legal_rate: 0.016
steps:
  - base_penalty: vat_due * 0.25
  - within_90_days: base_penalty / 2
  - within_15_days: within_90_days * days_late / 15
  - ravvedimento_penalty: round(within_15_days / 10, 2)
  - interest: round(vat_due * legal_rate * days_late / 365, 2)
  - total_f24: vat_due + ravvedimento_penalty + interest
expected:
  base_penalty: 2000
  within_90_days: 1000
  ravvedimento_penalty: 66.67
  interest: 3.51
  total_f24: 8070.18
```

**Historical cases retained with corrected outcomes.** Dates and amounts are original hypothetical inputs. They do not establish actual supplier entities, invoices, business use or entitlement.

| Original input | Corrected result or explicit hold |
|---|---|
| AWS EMEA SARL IT BRANCH, EUR 640, “AWS compute charges Q1”, IT IBAN | If an Italian establishment actually supplied and a valid invoice shows ordinary VAT: net EUR 524.59 and VAT EUR 115.41. Otherwise establish reverse charge. Branch text/IBAN alone does not decide |
| APPLE DISTRIBUTION INTL, EUR 14.99, “APPLE ONE PREMIER m.bianchi@gmail.com” | Personal use: no deduction. A personal email does not prove personal use; business evidence and the actual supplier/invoice are needed. The old automatic reverse-charge recovery EUR 2.70 is rejected, not recomputed as an entitlement |
| RISTORANTE DA GIOVANNI MILANO, EUR 187.50, “cena cliente”, Milan architect | If a restaurant invoice shows reduced-rate service: net EUR 170.45, VAT EUR 17.05. Representation: deductible VAT zero; the old 75% recovery EUR 12.79 is wrong. Facts distinguishing representation from ordinary business subsistence are required |
| ARCHITECTES ASSOCIES PARIS, EUR 4,500, “Consulting architettonico progetto Lyon”, FR IBAN | Do not automatically use general B2B treatment: a sufficiently direct link to a Lyon property triggers the property rule. Exact service/location/recipient and French obligations are a non-usable hold. The old EUR 990 Italian-VAT fallback for no VIES check is rejected. Check this point with one of our partner accountants |
| ENI STATION VIA MILANO 12, EUR 85 | With invoice, qualifying mixed-use vehicle and traceable fuel payment: net EUR 69.67, VAT EUR 15.33, deduction EUR 6.13, blocked EUR 9.20. “Van” does not itself prove full deduction |
| CCIAA MILANO, EUR 120, “diritto annuale 2026” | If established as the statutory contribution, no VAT invoice/recovery; never invent EUR 21.64 of VAT from the bank debit. A different invoiced service must be assessed separately |
| 03.04.2026 NOTION LABS INC, USD 16 / EUR 14.68, monthly subscription | Assume EUR 14.68 is the correct statutory converted base and a general business service from a US entity: VP3 EUR 14.68, VP4 EUR 3.23 and deductible VP5 EUR 3.23 |
| 10.04.2026 GOOGLE IRELAND LIMITED, EUR 850, Google Ads April 2026 | With the stated EU general-service invoice and full entitlement: VP3 EUR 850; VP4/VP5 EUR 187 each |
| 15.04.2026 RISTORANTE DA MARIO ROMA, EUR 220, business dinner | If invoice gives ordinary restaurant service rate: net EUR 200, VAT EUR 20. Representation blocks VAT; qualifying ordinary business meal may permit it. Receipt/bank line alone does not establish deduction |
| 18.04.2026 DELL ITALIA SRL, EUR 1,595, invoice DEL2026-0041, Laptop XPS 15 | Valid ordinary taxed business purchase: net EUR 1,307.38, deductible VAT EUR 287.62 in VP5; net VP3. The historical EUR 516.46/516.40 income-tax tests are not LIPE thresholds; depreciation treatment is held |
| 22.04.2026 STUDIO KREBS GMBH, EUR 3,500, IT-2026-018 “IT consultancy March” | General German B2B service: non-soggetta, VP2 and no Italian output VAT. If completed in March, report Q1; April receipt alone does not move it to Q2. Confirm completion/earlier payment and invoice |
| 28.04.2026 LEASYS SPA, EUR 450, Fiat 500X lease | On the stated mixed-use vehicle facts: net EUR 368.85, VAT EUR 81.15, deductible EUR 32.46; VP3/VP5 |
| 05.05.2026 RADIOTAXI ROMA, EUR 18, “Corsa” | Establish route/exemption and invoice; passenger-transport deduction blocked unless own business activity. Do not invent input VAT |
| 12.05.2026 Q8, EUR 122, “Carburante” | With ordinary taxed invoice/card payment and qualifying mixed-use car: net EUR 100, VAT EUR 22, deductible EUR 8.80 |

**Historical consolidated Q2 2026 case.** Italian sales EUR 12,000; German general B2B service EUR 3,500 completed in Q2; laptop net EUR 1,307.38/VAT EUR 287.62; Google EUR 850; Notion EUR 14.68; mixed-use lease EUR 450 gross; prior Q1 credit EUR 300. Assume correct invoices/exchange rate and full deduction except the car. VP6 debt EUR 2,319.92 less prior credit leaves EUR 2,019.92; option interest EUR 20.20; VP14 EUR 2,040.12. No earlier-period credit is taxed again through the interest base. Other Intrastat/foreign-document duties must be settled separately.

```oa-check
name: Italy Q2 2026 LIPE with reverse charge, 40% vehicle and credit
inputs:
  sales_22: 12000
  eu_service_sale: 3500
  laptop_net: 1307.38
  laptop_iva: 287.62
  google_net: 850
  notion_net: 14.68
  lease_gross: 450
  vehicle_share: 40
  vp8: 300
  rate: 22
steps:
  - lease_net: round(lease_gross * 100 / (100 + rate), 2)
  - lease_iva: lease_gross - lease_net
  - lease_deductible: round(pct(lease_iva, vehicle_share), 2)
  - output_sales: pct(sales_22, rate)
  - rc_google: round(pct(google_net, rate), 2)
  - rc_notion: round(pct(notion_net, rate), 2)
  - vp2: sales_22 + eu_service_sale
  - vp3: laptop_net + google_net + notion_net + lease_net
  - vp4: output_sales + rc_google + rc_notion
  - vp5: laptop_iva + rc_google + rc_notion + lease_deductible
  - vp6_col1: max(vp4 - vp5, 0)
  - vp6_col2: max(vp5 - vp4, 0)
  - to_pay_before_interest: max(vp6_col1 - vp6_col2 - vp8, 0)
  - vp12: round(pct(to_pay_before_interest, 1), 2)
  - vp14_col1: max((vp6_col1 + vp12) - (vp6_col2 + vp8), 0)
  - vp14_col2: max((vp6_col2 + vp8) - (vp6_col1 + vp12), 0)
expected:
  lease_net: 368.85
  lease_iva: 81.15
  lease_deductible: 32.46
  vp2: 15500
  vp3: 2540.91
  vp4: 2830.23
  vp5: 510.31
  vp6_col1: 2319.92
  vp6_col2: 0
  to_pay_before_interest: 2019.92
  vp12: 20.20
  vp14_col1: 2040.12
  vp14_col2: 0
```

**Historical frequency decision.** EUR 300,000 service volume, quarterly pre-interest debts EUR 6,000/5,000/7,000 and annual Q4 balance EUR 4,000: quarterly option interest EUR 180 plus EUR 40, total EUR 220 versus no option interest monthly. The old approximate funding comparison used three/two/one months and a two-month average, producing a simple annual break-even of 6%. That is an illustrative Q1–Q3 timing assumption, excluding August/day-count/acconto effects; compare actual cash dates before choosing frequency. Election communication/revocation and mixed-activity eligibility: Check this point with one of our partner accountants.

```oa-check
name: Italy monthly or quarterly settlement, cost of the option
inputs:
  q1: 6000
  q2: 5000
  q3: 7000
  q4: 4000
  volume: 300000
  services_limit: 500000
steps:
  - headroom: services_limit - volume
  - int_q1: pct(q1, 1)
  - int_q2: pct(q2, 1)
  - int_q3: pct(q3, 1)
  - int_q4: pct(q4, 1)
  - cost_q1_to_q3: int_q1 + int_q2 + int_q3
  - quarterly_cost: cost_q1_to_q3 + int_q4
  - monthly_cost: 0
  - extra_cost_of_quarterly: quarterly_cost - monthly_cost
  - average_months_deferred: (3 + 2 + 1) / 3
  - break_even_percent_a_year: 1 * 12 / average_months_deferred
expected:
  headroom: 200000
  cost_q1_to_q3: 180
  int_q4: 40
  quarterly_cost: 220
  extra_cost_of_quarterly: 220
  average_months_deferred: 2
  break_even_percent_a_year: 6
```

**Historical carry boundary.** January 2026 debt EUR 85 and February debt EUR 1,000, no credits: carry EUR 85 into February VP7 and pay EUR 1,085 by 16 March. At EUR 100.01 the monthly carry limit is exceeded. Observe the December backstop.

```oa-check
name: Italy EUR 100 carry in a monthly settlement
inputs:
  january_vp14: 85
  february_vp6: 1000
  limit: 100
steps:
  - over_limit: min(ceil(max(january_vp14 - limit, 0)), 1)
  - january_paid: january_vp14 * over_limit
  - february_vp7: january_vp14 - january_paid
  - february_vp14: february_vp6 + february_vp7
expected:
  over_limit: 0
  january_paid: 0
  february_vp7: 85
  february_vp14: 1085
```

**Historical vehicle alternatives.** Lease VAT EUR 81.15 and card-paid fuel VAT EUR 22: mixed-use deduction EUR 41.26; ordinary fully eligible business/agent case EUR 103.15, difference EUR 61.89. Cash fuel blocks fuel deduction, leaving EUR 32.46 lease deduction on these facts.

```oa-check
name: Italy art 19-bis.1 vehicle and fuel deduction cases
inputs:
  lease_iva: 81.15
  fuel_iva: 22
  share_mixed: 40
  share_full: 100
steps:
  - mixed_lease: round(pct(lease_iva, share_mixed), 2)
  - mixed_fuel: round(pct(fuel_iva, share_mixed), 2)
  - mixed_total: mixed_lease + mixed_fuel
  - full_total: pct(lease_iva, share_full) + pct(fuel_iva, share_full)
  - difference: full_total - mixed_total
  - cash_fuel_case: mixed_lease + 0
expected:
  mixed_lease: 32.46
  mixed_fuel: 8.80
  mixed_total: 41.26
  full_total: 103.15
  difference: 61.89
  cash_fuel_case: 32.46
```

## Ask the client first

Confirm regime, Partita IVA and entity, sector, period and tax points; prior-year volume by activity and quarterly election; invoices/SdI/customs records and register dates; prior LIPE/annual-return/F24 credits; business/private use and vehicle classification/payment evidence; taxable/exempt activities; public-body customers and attestations; actual foreign supplier/customer establishments, status, goods/services and property links; December acconto, payments and notices. Search the records first. Missing facts stay unresolved: do not substitute a country, rate, regime, credit or supplier.

Before filing: reconcile the bank to documentary records, exclude duplicates, recompute all VP fields, document any held lines and their effect, verify period/deadline/channel/model and F24 codes, obtain the responsible review and retain submission/payment receipts. Do not describe a prepared draft as filed or paid.

## Sources

Official sources below were read on 27 November 2026; article references concern the operative paragraphs, not every unrelated part of an act. The LIPE instructions are the authority's 2024-edition file. A future model or law change needs a fresh applicability check. The Q4 LIPE deadline crossing into 2027 is also preserved by the attached D.Lgs. 141/2026 art. 51, applying from 2027 under art. 368.

| Source | Official URL | Read on |
|---|---|---|
| VAT scope, tax point, place of supply, base and rates: D.P.R. 633/1972 arts. 1, 6, 7-ter, 7-quater, 8, 13, 16, Tabella A | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633!vig=2026-11-27 | 2026-11-27 |
| Reverse charge/split payment and input limits: same act arts. 17, 17-ter, 19, 19-bis.1; invoices art. 21; imports art. 70 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art17!vig=2026-11-27 | 2026-11-27 |
| Periodic settlement and carry: D.P.R. 100/1998 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-03-23;100~art1!vig=2026-11-27 | 2026-11-27 |
| Quarterly option: D.P.R. 542/1999 art. 7; L. 183/2011 art. 14(11); D.P.R. 600/1973 art. 18 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art7!vig=2026-11-27 | 2026-11-27 |
| LIPE law and instructions | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig=2026-11-27 ; https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f | 2026-11-27 |
| Payment guidance and annual-return window | https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva ; https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art8!vig=2026-11-27 | 2026-11-27 |
| August/weekend: D.L. 223/2006 art. 37(11-bis); D.L. 70/2011 art. 7(2)(l) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-05-13;70~art7!vig=2026-11-27 | 2026-11-27 |
| Electronic invoicing/cross-border data: D.Lgs. 127/2015 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig=2026-11-27 | 2026-11-27 |
| Intra-EU goods/distance sales: D.L. 331/1993 art. 41 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig=2026-11-27 | 2026-11-27 |
| Payment/communication penalties: D.Lgs. 471/1997 arts. 11, 13; reform application D.Lgs. 87/2024 art. 5 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-11-27 | 2026-11-27 |
| Ravvedimento: D.Lgs. 472/1997 art. 13 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-11-27 | 2026-11-27 |
| Legal interest: D.M. 10 December 2025, operative article | https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=25A06705&atto.dataPubblicazioneGazzetta=2025-12-13&atto.tipoProvvedimento=DECRETO | 2026-11-27 |
| TD17/TD18 and foreign supplier exceptions: AdE compilation guide v1.10 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/guida_compilazione-fe-esterometro-v1-10_aprile_2025 | 2026-11-27 |
| 2027 LIPE continuity: attached D.Lgs. 141/2026 arts. 51 and 368 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-05;141:1~art51!vig=2027-01-01 | 2026-11-27 |
| Motor-vehicle derogation through 2028: Decision (EU) 2025/2529 amending 2007/441/EC | https://eur-lex.europa.eu/eli/dec_impl/2025/2529/oj/ita/pdf | 2026-11-27 |
| Restaurant/accommodation deduction: AdE circular 53/E of 2008 | https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7BD1D18AAB-C63D-4548-A23D-819C63A46F58%7D | 2026-11-27 |
| Employee-beneficiary invoice identification: AdE circular 6/E of 2009 | https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B0E99AE4F-3000-4A93-8BBB-49B6D428B5AB%7D | 2026-11-27 |
| Split-payment EU extension: Decision 2026/1728 art. 1 | https://eur-lex.europa.eu/eli/dec_impl/2026/1728 | 2026-11-27 |
| Split supplier settlement: D.M. 23 January 2015 art. 2 | https://www.gazzettaufficiale.it/eli/id/2015/02/03/15A00690/sg | 2026-11-27 |
| IVA consolidation from 2027: D.Lgs. 10/2026, attached text art. 171 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art171!vig=2027-01-01 | 2026-11-27 |

Not yet confirmed: the special-case rate classifications, logistics authorization/interim-option conditions, Intrastat service filing and other expressly held outcomes above. Those are non-usable holds: Check this point with one of our partner accountants. No ordinary IVA settlement or LIPE field is delegated to these holds.
