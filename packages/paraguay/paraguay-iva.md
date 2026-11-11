---
name: paraguay-iva
description: "Paraguay value added tax (Impuesto al Valor Agregado, IVA) for 2026 under Ley N° 6380/2019 Libro II Título I (as amended by Ley N° 7067/2023) and its regulation Decreto N° 3107/2019. Covers who pays (businesses, independent professionals, landlords, importers; not RESIMPLE payers), when the tax arises, the 10% general rate and the 5% rate (residential rent, real estate on a 30% base, basic food basket, listed farm and livestock products, registered medicines), exemptions, the monthly Form 120 (obligation 211), IVA credit rules and the six-month proration, the restricted credit list for professionals and the 30% car rule, withholding and perception (State bodies, exporters, card processors, payments abroad, digital services), exporter refunds, the RUC-digit due dates and penalties. Trigger on: Paraguay VAT, IVA Paraguay, Formulario 120, IVA crédito, IVA débito, retención IVA, servicios digitales IVA Paraguay, saldo técnico, devolución IVA exportador. Out of scope: income taxes (paraguay-corporate-income-tax, paraguay-income-tax), excise (ISC), customs."
version: 1.1
jurisdiction: PY
tax_year: 2026
last_updated: 2026-11-11
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
type: computation
tier: 2
domain: vat-gst
---

# Paraguay IVA: 2026 rates, credit, withholding and the monthly return v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The law is Ley N° 6380/2019 "De Modernización y Simplificación del Sistema Tributario Nacional", Libro II, Título I (arts. 80 to 106), read in the text published by the Biblioteca y Archivo Central del Congreso Nacional (BACN). Since 2020 it replaces the IVA of Ley 125/1991. Article 100(3)(h) (passenger transport) was replaced by Ley N° 7067/2023. The regulation is the Anexo to Decreto N° 3107/2019, read in the scanned copy published by the Dirección Nacional de Ingresos Tributarios (DNIT, which replaced the Subsecretaría de Estado de Tributación under Ley N° 7143/2023); its art. 19 was replaced by Decreto N° 8175/2022. For 2026 the budget law, Ley N° 7609/2025, suspends exemptions in other laws but expressly keeps those of Ley 6380 (art. 244(n)), and suspends the progressive cut in IVA withholding percentages (art. 266). Amounts are in guaraníes (G). IVA is computed monthly (art. 86).

## Who this applies to

- **IVA taxpayers** (art. 82): individuals who provide personal or professional services outside employment, or let real estate; individuals running a sole-owner business (empresa unipersonal); companies, associations, cooperatives, foundations and every other private entity; consortia for a public work; branches of foreign entities; public enterprises with commercial activity; habitual and casual importers; transparent legal structures; non-resident (INR) taxpayers; undivided estates.
- **Not taxpayers** (Decreto 3107 art. 3): central-government bodies, and sole-owner businesses in the IRE RESIMPLE, unless they also provide personal or professional services (Ley 6380 art. 27).
- **What is taxed** (arts. 80 and 81): sales of goods, services (except employment) and imports. A sale includes private use of business goods by owners, partners, directors and staff, leasing with a purchase option, the transfer of a business or of shares and quotas, consignment, and the transfer of rights. Services include loans and financing, works contracts, insurance, intermediation, letting of movables, property and intangibles, professions, transport, digital services, obligations not to act, and derivatives where the investor is in Paraguay.
- **Territory** (art. 84): goods located in Paraguay, services performed in Paraguay, and imports. Technical assistance and other services performed abroad are taxed when used in Paraguay. Loans are Paraguayan when the borrower is resident; insurance when the risk or person is in Paraguay; digital services when any one of the IP address or SIM country, billing address, paying bank account, card issuer is Paraguayan; international transport is 25% taxed in Paraguay (Decreto 3107 art. 7: freight to Paraguay and tickets from or to Paraguay).

**When to refer.** Refer to a specialist for: maquila (Ley N° 7547/2025, which repealed the maquila law Ley 1064/1997); investment-incentive projects under Ley N° 7548/2025 or the old Ley 60/1990 regime; free zones; the Régimen de Turismo and the shopping-tourism regime (Decreto 2063/2024); reorganisations; exporter refund claims and the accelerated-refund guarantee; excise (ISC). Income tax: [paraguay-corporate-income-tax](paraguay-corporate-income-tax.md) and [paraguay-income-tax](paraguay-income-tax.md).

## Rates, bands and thresholds

Quick answer: **10% unless the item is on the 5% list or exempt.** The tax is added to a base that includes other taxes (such as ISC) but not IVA itself (art. 85).

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| General rate, all other cases (art. 90(g)) | 10% | 2026 | https://www.bacn.gov.py/leyes-paraguayas/9332/ley-n-6380-de-modernizacion-y-simplificacion-del-sistema-tributario-nacional |
| Letting of property used **exclusively** as a home, including use and usufruct (art. 90(a)) | 5%; commercial lettings at 10% | 2026 | same |
| Sale of real estate (art. 90(b)) on a base of 30% of the price or of each monthly instalment (art. 85(3)) | 5% of 30%: 1.5% of the price | 2026 | same |
| Basic basket: rice, pasta, vegetable oil, yerba mate, milk, eggs, flour, iodised salt (art. 90(c); detail in Decreto 3107 art. 23) | 5% on sale and import | 2026 | same |
| Listed agricultural, horticultural and fruit products, including soya, maize, wheat, cotton and their primary derivatives (flours, crude oils, expellers, pellets) (art. 90(d)) | 5% on sale and import | 2026 | same |
| Live cattle, horses, goats, buffalo, sheep, fish, poultry, pigs, rabbits and primary derivatives (meat, offal, wool, hides, horns, bones) unaltered except to preserve them (art. 90(e)); seafood at 10% (Decreto 3107 art. 24) | 5% | 2026 | same |
| Medicines for human use registered with the Ministry of Health, and prescribed magistral formulations (art. 90(f); Decreto 3107 art. 25) | 5% | 2026 | same |
| Casual importer (art. 85(7)) | Customs base increased by 30%; IVA paid is final | 2026 | same |
| Movables used in a professional's personal services, when sold (art. 85(9)) | Base of 30% of the sale value | 2026 | same |
| IVA credit for a professional on buying a car (art. 88) | Up to 30% of the IVA on the car | 2026 | same |
| Exporter refund ceiling (art. 101) | Not above 10% of the export customs value; any excess goes to later claims | 2026 | same |
| Public passenger transport: national urban, metropolitan, short, medium and long distance (art. 100(3)(h) as replaced by Ley 7067/2023) | Exempt | 2026 | https://www.dnit.gov.py/documents/20123/277628/LEY+N%C2%B0+7067+-+35322+-+2023+-+REF.+QUE+MODIFICA+ART+100+DE+LEY+6380-2019.pdf/7015a0a7-8481-091d-3bd2-4e063894f283 |
| Withholding on IVA, ceiling from the fourth year of the law (Ley 6380 art. 136) | Not above 10% of the IVA on the invoice; the progressive cut is suspended for 2026 (Ley 7609/2025 art. 266) | 2026 | https://www.mef.gov.py/sites/default/files/2026-01/LEY_7609_PGN_2026_OCR.pdf |
| Withholding by public bodies on suppliers (Decreto 3107 art. 36) | 30% of the IVA; 100% on court-set fees and, as a final payment, on unregistered non-professional individuals who opt for it | 2026 | https://www.dnit.gov.py/documents/47797/47809/Decreto+N%C2%B0+3107-19.pdf/d723b322-e502-e34b-18bc-3df7bfd0f785 |
| Withholding by registered exporters on local suppliers (Decreto 3107 art. 37) | 70% of the IVA at 10%; 30% on goods at 5%; 10% on art. 90(d)(1) farm products | 2026 | same |
| Withholding by designated agents (Decreto 3107 art. 38) | 30% of the IVA; 10% on art. 90(d)(1) farm products | 2026 | same |
| Withholding by card processors (Decreto 3107 art. 39) | 0.90909% of total transactions | 2026 | same |
| Withholding on payments to non-residents without a branch, by IRE General payers and public bodies (Decreto 3107 art. 41) | 100% of the IVA, final for the non-resident; if the price includes IVA, divide by 11 (10%) or 21 (5%) | 2026 | same |
| Perception on digital services from abroad paid by card or transfer (Decreto 3107 art. 31) | 100% of 10% of the price, added on top; final for the foreign provider | 2026 | same |
| Withholding by property managers on rent for unregistered individual owners (Decreto 3107 art. 42) | 100% of the IVA, final | 2026 | same |
| No withholding below (Decreto 3107 art. 44) | Purchases in the month under 10 daily minimum wages, before IVA | 2026 | same |
| Proration period for common input IVA (Decreto 3107 art. 18) | Taxed income over total income of the last 6 months, including the current month | 2026 | same |
| Bad debts (Decreto 3107 art. 17) | Output IVA recoverable after 36 months unpaid, or on bankruptcy, a general inhibition or a court-approved composition | 2026 | same |

The rates in Decreto 3107 arts. 36 to 41 are those of the 2019 text; later decrees on the DNIT list that amend Decreto 3107 (3322, 3477, 3529, 3667, 3739, 3881 and 3967 of 2020) were not read, and art. 136 caps withholding at 10% of the IVA "from the fourth year". Confirm the percentage in force with the withholding agent's certificate.

## The base

**When the tax arises** (art. 83): the first of delivery, payment (full or partial) or the due date for a service. Utilities and telecoms: the payment due date. Imports: when the customs declaration is numbered. Services from abroad: payment or the due date, whichever is first. Loans: payment or the instalment due date of the interest and charges. Private use: when the goods are taken. Continuing services are monthly; building works at each payment or progress certificate; leasing at each instalment (Decreto 3107 art. 4). The invoice must be issued at the same time.

**The base** (art. 85): the accrued price with everything charged to the buyer, including interest and surcharges and other taxes, less returns and market discounts shown on the invoice. Special bases: interest and charges (not capital) on loans; the monthly rent; 30% of the price for real estate; cost for private use and free supplies; customs value plus duties and taxes before release for imports (plus 30% for a casual importer). Foreign-currency prices convert at the BCP buying or selling rate at the close of the previous day (Decreto 3107 art. 13). A barter is two sales (Decreto 3107 art. 9).

**Exempt** (art. 100, kept in force for 2026 by Ley 7609 art. 244(n)): sales of foreign currency, securities, shares and quotas; assignment of receivables; books, newspapers and educational magazines; laptops for free school programmes; goods donated to recognised education and sports bodies; games of chance; petroleum fuels and biofuels; business reorganisations; contributions in kind to capital; **exports of goods** (keep the documents, or the sale is deemed domestic); interest on securities; derivatives; international freight for exports; bank, finance and cooperative deposits; education by recognised institutions and teaching for them; public passenger transport (Ley 7067/2023); travellers' baggage and diplomatic imports; non-profit and religious bodies on their non-business activities (the exemption does not cover the listed business activities, such as restaurants, transport, lending and letting); supplies to recognised education bodies of lab, classroom, library and IT equipment (with a Ministry release); and transactions of cooperatives with each other and their members.

**IVA credit** (arts. 88 and 89): IVA on local purchases in the month, IVA paid at customs, and IVA withheld or perceived on payments to non-residents. To deduct it the purchase must serve taxed operations directly or in part, be a real outlay, and be supported by a document naming the buyer and its RUC with a precise description; the buyer must check that the supplier's timbrado is valid (Decreto 3107 art. 22). Common inputs that serve taxed, untaxed and exempt operations are prorated by taxed income over total income of the last six months (art. 88; Decreto 3107 art. 18); the non-creditable part becomes a cost for the IRE or IRP (art. 91). Goods destroyed or stolen: the credit is reversed. In a reorganisation, the credit passes to the successor in proportion to net worth transferred.

**Professionals' restricted credit** (Decreto 3107 art. 19 as replaced by Decreto 8175/2022, as summarised in the [DNIT IVA guide](https://www.dnit.gov.py/documents/20123/224724/IVA+Cartilla+6.08.24.pdf/c23f9d9f-8747-815f-28c2-4d0c1fa9e6d6)): an individual providing personal or professional services deducts IVA credit only on personal health (including medicines and prepaid medicine for their share); food and non-alcoholic drinks (up to 30% of that IVA); training related to the service; utilities and telecoms used only for the service; office rent and upkeep; office supplies, furniture, professional equipment and tools; work clothing; spare parts, lubricants, maintenance, repairs and insurance of a car used only for the service; and subcontracted professional services for the service. A car purchase gives up to 30% of its IVA (law art. 88).

**Excess credit** (art. 88; Decreto 3107 art. 20): an excess of credit over debit carries forward as the "saldo técnico" with no refund, except for exporters. A taxpayer may waive the balance to the DNIT (it then becomes a non-deductible cost for income tax, art. 91). No refund on ceasing activity.

**Exporters** (arts. 101 to 103): IVA credit on goods and services linked to exports is set first against domestic IVA debit, then refunded or carried forward. Exports of farm products in their natural state and first-processing derivatives get no refund of the IVA on buying those goods, but do for other inputs. Claims run month by month in order, from the month after the return's due date, within the limitation period, with the exporter's authorisation to its banks to report to the DNIT. The DNIT refunds within 90 working days of accepting the claim and credits the RUC current account; an accelerated refund against a bank guarantee is available (art. 102). An export is declared in the month of the "cumplido de embarque" (Decreto 3107 arts. 27 and 30).

**Digital services and services from abroad.** A Paraguayan bank, card processor, exchange house, cooperative, payment processor or phone company that pays a foreign digital provider (streaming, apps, platforms) on the customer's card or transfer perceives 10% on top; for an IVA-taxpayer customer using it for taxed activity, the perception shown on the card statement is IVA credit in that month (Decreto 3107 arts. 31 and 33; [Resolución General 76/2020](https://www.dnit.gov.py/documents/20123/221869/RESOLUCION+GENERAL+N%C2%B0+76_2020_SERVICIOS+DIGITALES.pdf/8025edb7-e1cd-0f8e-7267-5ade0fa98e0e) arts. 3 and 4). Other services from a non-resident without a branch are subject to 100% withholding by an IRE General payer or public body (Decreto 3107 art. 41); the withheld IVA is the payer's credit (art. 88(3)). A resident that buys digital services abroad to resell them withholds IVA and INR itself (RG 76/2020 art. 6).

## Deadlines and filing

1. **Register** in the RUC with the IVA obligation (obligation 211, IVA General) before invoicing ([DNIT, IVA page](https://www.dnit.gov.py/web/portal-institucional/iva)).
2. **Issue and demand documents.** Every sale, exempt or not, needs a sales document with the buyer's name and RUC or ID (art. 92). Documents are pre-printed with a timbrado, virtual or electronic (e-Kuatia). Goods in transit travel with a remission note or invoice (art. 94). Prices are advertised IVA included (art. 93).
3. **Register purchases and sales in Marangatu** ("Registro de Comprobantes", RG 90/2021) through the month, by hand or by import ([DNIT IVA guide](https://www.dnit.gov.py/documents/20123/224724/IVA+Cartilla+6.08.24.pdf/c23f9d9f-8747-815f-28c2-4d0c1fa9e6d6)).
4. **File Form 120 "IVA, Versión 4" every month**, even with no operations (Decreto 3107 art. 30), including exempt operations and exports, with the Exporter Annex where relevant. Shares sold above par, foreign-currency trading margins and derivatives are reported even though exempt (art. 96).
5. **Due day**: the month after the period, on the day set by the last digit of the RUC, ignoring the check digit: 0 = 7th, 1 = 9th, 2 = 11th, 3 = 13th, 4 = 15th, 5 = 17th, 6 = 19th, 7 = 21st, 8 = 23rd, 9 = 25th; a non-working day moves it to the next working day. The purchases and sales book informative return follows the informative calendar (0 = 8th through 9 = 26th) ([DNIT, deadlines under Ley 6380](https://www.dnit.gov.py/web/portal-institucional/w/vencimiento-ley-n-6380/19)).
6. **Compute**: IVA debit (output on the month's taxed operations, less IVA on returns, discounts and bad debts) less IVA credit (art. 86), less the saldo técnico brought forward, less IVA withheld from the taxpayer in the month (withholdings above the tax due carry forward until used, Decreto 3107 art. 47). Pay the result through the DNIT channels.
7. **Withholding agents** issue withholding certificates through Tesakã, confirm the DNIT's pro-forma settlement on Form 122 within the first six calendar days of the month, and pay by the 7th; if they do not confirm, the DNIT treats it as accepted (DNIT IVA guide).
8. **Imports**: IVA is paid at customs before release (art. 98). Customs also perceives 30% (imports) or 100% (exports) of the IVA on customs brokers' fees (Decreto 3107 art. 32).

## Penalties and interest

From Ley N° 125/1991, Libro V, in the DNIT copy of the 1991 text ([Ley 125/91, arts. 170 to 179](https://www.dnit.gov.py/documents/47797/47809/P+-+Ley+N%C2%BA+125-91.pdf/63cf3ff2-2b45-5920-cfc0-e562ff41ced9)):

- **Late payment (mora, art. 171).** 4% of the unpaid tax if up to one month late, rising by 2 points a month to 14% at five months or more, plus a monthly surcharge or interest day by day at the rate the Executive fixes every four months. A return filed on time but paid late carries only the mora charges (DNIT deadlines page).
- **Late return (contravención, art. 176).** **G 50,000** for a determinative return filed late, and **G 100,000** for a late informative return such as the purchases and sales book (Resolución General 13/2019, Anexo, items 4.a and 4.b, [DNIT page](https://www.dnit.gov.py/web/portal-institucional/w/resolucion-general-n-13-19-anexo)).
- **Underpayment (omisión de pago, art. 177).** Up to 50% of the tax omitted.
- **Fraud (defraudación, arts. 172 to 175).** One to three times the tax evaded. Not issuing invoices, and a withholding agent paying over withheld IVA more than 30 days late, are presumed fraud (art. 174). Goods moving without a remission note can be seized (Ley 6380 art. 94).
- **Refund delays** by the DNIT carry interest at the late-payment rate (art. 103).

## Cross-border points

- **Exports** of goods are exempt with refund of linked input IVA (arts. 100(2) and 101); services are not "exports" in the law, so a service used in Paraguay is taxed even if the provider is abroad (art. 84(1)), and a service performed in Paraguay is taxed even for a foreign client.
- **Imports** are taxed at customs; casual importers pay on a base increased by 30%, as a final payment (art. 85(7)).
- **Non-resident providers**: withholding of 100% of the IVA by the Paraguayan payer, and INR on top (see [paraguay-corporate-income-tax](paraguay-corporate-income-tax.md)); digital services by perception through the payment channel.
- **Real estate and registrable goods of non-residents**: the notary withholds 100% of the IVA on the sale (Decreto 3107 art. 41).

## Worked examples

### Example 1: monthly Form 120 for a trading company

Ferretería Sur S.R.L. (an IRE General payer) has these figures for March 2026, all supported by valid documents:

- Sales of hardware at 10%: G 110,000,000 including IVA (base 100,000,000, IVA 10,000,000).
- Sales of rice at 5%: G 21,000,000 including IVA (base 20,000,000, IVA 1,000,000).
- Purchases for the business: IVA at 10% of G 6,000,000 and at 5% of G 500,000; IVA paid at customs G 1,200,000; IVA perceived on a cloud subscription G 100,000.
- Saldo técnico from February: G 400,000. IVA withheld by a customer that is a designated agent: G 900,000.

IVA debit is 10,000,000 plus 1,000,000 = G 11,000,000. IVA credit is 6,000,000 plus 500,000 plus 1,200,000 plus 100,000 = G 7,800,000. Net G 3,200,000, less the G 400,000 saldo técnico, G 2,800,000, less the G 900,000 withheld: **G 1,900,000** to pay by the RUC-digit day in April 2026.

```oa-check
name: Trading company, Form 120, March 2026
inputs:
  sales_10_gross: 110000000
  sales_5_gross: 21000000
  credit_10: 6000000
  credit_5: 500000
  credit_customs: 1200000
  credit_digital: 100000
  saldo_tecnico: 400000
  withheld: 900000
steps:
  - base_10: sales_10_gross / 1.10
  - base_5: sales_5_gross / 1.05
  - debit: base_10 * 0.10 + base_5 * 0.05
  - credit: credit_10 + credit_5 + credit_customs + credit_digital
  - net: debit - credit
  - after_saldo: net - saldo_tecnico
  - payable: max(0, after_saldo - withheld)
expected:
  base_10: 100000000
  base_5: 20000000
  debit: 11000000
  credit: 7800000
  net: 3200000
  after_saldo: 2800000
  payable: 1900000
```

### Example 2: mixed activities, a foreign consultant and a property sale (includes a decision)

Instituto Delta S.A. runs recognised courses (exempt) and a taxed consultancy. Over October 2025 to March 2026 its taxed income was G 600,000,000 and its total income G 1,000,000,000. In March 2026:

- **Proration.** Common inputs (rent, power, IT) carry IVA of G 10,000,000. Creditable: 60% = G 6,000,000; the other G 4,000,000 is an IRE cost (art. 91).
- **Foreign consultant, the pricing decision.** It hires a consultant abroad, with no branch in Paraguay, for G 55,000,000. If the contract is silent, IVA is not in the price: Delta withholds and pays 10% on top, G 5,500,000, so the deal costs G 60,500,000 and the consultant gets G 55,000,000. If the contract says the price includes IVA, IVA is 55,000,000 / 11 = G 5,000,000 and the consultant gets G 50,000,000. The withheld IVA is Delta's credit (art. 88(3)), but here only in the 60% proportion if the service serves both activities: G 3,300,000 or G 3,000,000. The figure that decides it is who bears the IVA; write it into the contract.
- **Property sale.** It sells an office for G 1,000,000,000. IVA at 5% on a base of 30%: G 15,000,000, an effective 1.5%.

```oa-check
name: Mixed activities, proration, foreign consultant both ways, property sale, 2026
inputs:
  taxed_income_6m: 600000000
  total_income_6m: 1000000000
  common_iva: 10000000
  consultant_price: 55000000
  property_price: 1000000000
steps:
  - proration: taxed_income_6m / total_income_6m
  - common_credit: common_iva * proration
  - common_cost: common_iva - common_credit
  - iva_on_top: consultant_price * 0.10
  - cost_on_top: consultant_price + iva_on_top
  - iva_inside: consultant_price / 11
  - consultant_net_inside: consultant_price - iva_inside
  - credit_on_top: iva_on_top * proration
  - credit_inside: iva_inside * proration
  - property_iva: property_price * 0.30 * 0.05
expected:
  proration: 0.60
  common_credit: 6000000
  common_cost: 4000000
  iva_on_top: 5500000
  cost_on_top: 60500000
  iva_inside: 5000000
  consultant_net_inside: 50000000
  credit_on_top: 3300000
  credit_inside: 3000000
  property_iva: 15000000
```

## Ask the client first

1. Who is the taxpayer: company, sole-owner business (which IRE regime; RESIMPLE is outside IVA), or an individual professional or landlord (restricted credit list)?
2. What does it sell, and is each line at 10%, 5% or exempt (the 5% lists are closed lists)? Any residential versus commercial lettings, real estate sales, exports?
3. Does it have exempt or untaxed income? Then the six-month proration applies.
4. Is it a withholding agent (public body, exporter, designated agent, card processor), and what was withheld from it in the month?
5. Any payments to non-residents or digital services from abroad, and does the contract say whether IVA is included?
6. The last digit of the RUC, the saldo técnico brought forward, and whether it is in the Exporters Register.

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley N° 6380/2019, BACN text: Libro II Título I arts. 80 to 106 (IVA), arts. 27, 136 | https://www.bacn.gov.py/leyes-paraguayas/9332/ley-n-6380-de-modernizacion-y-simplificacion-del-sistema-tributario-nacional | 2026-11-11 |
| Ley N° 7067/2023 (DNIT copy, scanned, read by OCR): new art. 100 numeral 3(h), national public passenger transport | https://www.dnit.gov.py/documents/20123/277628/LEY+N%C2%B0+7067+-+35322+-+2023+-+REF.+QUE+MODIFICA+ART+100+DE+LEY+6380-2019.pdf/7015a0a7-8481-091d-3bd2-4e063894f283 | 2026-11-11 |
| Ley N° 7609/2025, Presupuesto General de la Nación 2026 (MEF copy): arts. 244 (exemptions suspended, Ley 6380 excepted) and 266 (IVA withholding cut suspended) | https://www.mef.gov.py/sites/default/files/2026-01/LEY_7609_PGN_2026_OCR.pdf | 2026-11-11 |
| Decreto N° 3107/2019 (IVA regulation), DNIT copy, scanned, read by OCR: Anexo arts. 3, 4, 7 to 25, 27, 30 to 47 | https://www.dnit.gov.py/documents/47797/47809/Decreto+N%C2%B0+3107-19.pdf/d723b322-e502-e34b-18bc-3df7bfd0f785 | 2026-11-11 |
| DNIT, IVA guide (V 08/24), read for the Decreto 8175/2022 credit list for professionals, Form 120 v4 and obligation 211, Form 122, withholding exceptions | https://www.dnit.gov.py/documents/20123/224724/IVA+Cartilla+6.08.24.pdf/c23f9d9f-8747-815f-28c2-4d0c1fa9e6d6 | 2026-11-11 |
| DNIT, IVA page, read for the obligation and regimes | https://www.dnit.gov.py/web/portal-institucional/iva | 2026-11-11 |
| Resolución General 76/2020 (digital services), DNIT copy: arts. 2 to 6 | https://www.dnit.gov.py/documents/20123/221869/RESOLUCION+GENERAL+N%C2%B0+76_2020_SERVICIOS+DIGITALES.pdf/8025edb7-e1cd-0f8e-7267-5ade0fa98e0e | 2026-11-11 |
| DNIT, deadlines under Ley 6380 (RG 38/2020), read for the RUC-digit calendar and informative returns | https://www.dnit.gov.py/web/portal-institucional/w/vencimiento-ley-n-6380/19 | 2026-11-11 |
| Ley N° 125/1991, DNIT copy of the 1991 text (scanned; arts. 170 to 179 read by OCR) | https://www.dnit.gov.py/documents/47797/47809/P+-+Ley+N%C2%BA+125-91.pdf/63cf3ff2-2b45-5920-cfc0-e562ff41ced9 | 2026-11-11 |
| Resolución General 13/2019, Anexo, DNIT page: items 4.a and 4.b | https://www.dnit.gov.py/web/portal-institucional/w/resolucion-general-n-13-19-anexo | 2026-11-11 |
| DNIT, list of tax laws, read for amendments to Ley 6380 (Ley 7067/2023; Leyes 7547 and 7548 of 2025) | https://www.dnit.gov.py/web/portal-institucional/leyes | 2026-11-11 |

Not yet confirmed: the IVA withholding percentages in force in 2026 (Decreto 3107 arts. 36 to 41 are the 2019 text; the 2020 amending decrees 3322, 3477, 3529, 3667, 3739, 3881 and 3967 were not read; art. 136 caps withholding at 10% of the IVA from the fourth year); the full text of Decreto 8175/2022 (read through the DNIT guide; the scanned decree is only partly legible); the Form 120 v4 box numbers (the earlier skill's line numbers 1 to 18 are not from a DNIT source); the SIFEN/e-Kuatia document types and the rollout schedule; whether a purchase from a non-taxpayer documented by autofactura gives any IVA credit (the earlier skill said yes at 5%; the law gives credit only for IVA included in the document); the current mora surcharge rate; whether later laws changed Ley 125 arts. 171 to 177; the value of the daily minimum wage used for the withholding floor.
