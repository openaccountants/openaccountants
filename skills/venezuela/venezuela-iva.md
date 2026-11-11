---
name: venezuela-iva
description: >
  Compute and review Venezuelan Impuesto al Valor Agregado for tax year 2026
  for ordinary taxpayers, including sole traders and companies. Covers taxable
  events, domestic supplies, exports, imported services, the taxable base,
  invoice evidence, input-credit eligibility, mixed taxable and exempt activities,
  carryforwards and reconciliation of withholding certificates. Use for Venezuela
  VAT, IVA, SENIAT IVA, Forma 30, débito fiscal, crédito fiscal, contribuyente
  ordinario, contribuyente formal, contribuyente especial, prorrata, or an IVA
  working paper. Includes local bank narration triage and four recomputing
  cases. Produces a reviewable calculation and filing handoff; current special
  taxpayer calendars, withholding administration and live portal field numbers
  remain evidence gates identified in Sources.
version: 2.1
jurisdiction: VE
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: computation
domain: tax
---

# Venezuela IVA v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** determine the taxable event before reading the cash movement. The general statutory rate is 16%; qualifying exports are zero-rated; exemption and non-subjection are different from zero-rating. Only an eligible ordinary taxpayer can deduct qualifying documented input IVA. The relevant authority is the consolidated Ley del IVA in Gaceta Oficial 6.507, arts. 3-16, 27, 29 and 33-38, not a bank-description rule. The official Assembly copy was unavailable live; the dated archive listed in Sources contains the actual gazette text.

**Required inputs before computing:** RIF and taxpayer registration/status notices; exact period and taxpayer calendar; supply descriptions and destinations; invoices and delivery/service dates; purchase and sales books; import declarations and tax-payment receipts; foreign-currency event-date valuation evidence; prior returns and credit balances; withholding certificates and related returns. A bank statement alone is insufficient. Read the supplied records before requesting anything missing.

This Guide loads on `vat-workflow-base` and produces working papers for a Venezuelan Contador Público Colegiado. It covers ordinary IVA computation. Special-taxpayer returns, retention filing and exact portal mapping require the additional primary evidence listed in Sources before a filing can be completed. Specialist matters include hydrocarbon operations, IGTF computation, currency controls, inflation accounting, special fiscal territories and refund applications.

## Who this applies to

- **Ordinary taxpayers:** habitual importers, industrial businesses, traders and habitual service providers, and persons or entities carrying on the taxable activities in the ordinary course of their business. This includes qualifying individuals and companies. Do not invent a turnover threshold: art. 5 defines the ordinary category by activity. Public bodies conducting taxable activities are addressed by art. 7. [Ley del IVA arts. 1, 3, 5 and 7](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
- **Occasional taxpayers:** non-habitual importers of tangible movable property pay import IVA for each import, without an input-credit entitlement under this category; art. 6 distinguishes them from ordinary taxpayers. [Art. 6](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
- **Formal taxpayers:** persons performing exclusively exempt or exonerated activities. This is not a synonym for a small business. Article 8 retains formal duties and allows administrative simplification; it excludes IVA payment and ordinary tax-determination rules for that category. Someone conducting both taxable and exempt activities needs the ordinary/mixed-use analysis. [Arts. 5 and 8](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
- **Non-domiciled supplier:** the purchaser of movable goods or recipient of services is responsible for payment where the supplier is not domiciled in Venezuela. Test actual territorial use before applying this rule. [Arts. 9(1), 14 and 15](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
- **Special taxpayers and withholding agents:** obtain the designation/notification and its effective date. Article 11 authorises appointment of retention and perception agents and recovery of excess retention subject to the applicable providencia. It does not establish a universal withholding percentage, return deadline or automatic right to deduct any certificate. The current administrative details are not established by the sources read for this rewrite. [Art. 11](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
- **Intermediaries:** a commission agent is taxed on its remuneration; the represented party accounts for the underlying supply excluding that commission, with the joint-payment responsibility described in art. 10. Match the settlement to that legal relationship before treating the bank receipt as turnover. [Art. 10](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

### What is taxed and where

Taxable events include sales of tangible movable property, specified inventory/fixed-asset withdrawals, definitive imports, paid independent services executed or used in Venezuela, and exports. A withdrawal for personal use, gifts or an unexplained stock shortfall can have output-IVA consequences; transfer into the business's own fixed assets or qualifying use in its business is treated differently by art. 4(3). [Arts. 3-4](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

Goods must be situated in Venezuela for the domestic sale/withdrawal rule. Services executed or used in Venezuela can be taxable despite foreign contracting, payment or supplier domicile. For international transport, art. 15 treats the service as partly domestic and applies tax to half the passage/freight value sold or issued in Venezuela for a journey departing Venezuela. Confirm whether an exemption or a more specific treatment applies before computing that base. [Arts. 14-15](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

An export of goods requires definitive departure from the customs territory for use or consumption abroad. A service export requires a beneficiary/recipient without Venezuelan domicile or residence **and exclusive use or enjoyment abroad**. A foreign invoice address or foreign payment alone is insufficient. [Art. 4(6)-(7)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

## Rates, bands and thresholds

These are the continuing statutory rules in the consolidated text read, subject to a later applicable Executive decree. Check the transaction's date and any product-specific decree. The percentage authorisations are not a licence to select a rate.

| Item | Rate or limit and neighbouring conditions | Official text actually read |
|---|---|---|
| General IVA | 16%, until the Executive establishes a different rate; exclude operations within a specific statutory treatment | [Ley del IVA art. 63, gazette p. 73; archived official copy](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Qualifying exports | 0% on goods and services satisfying the export definitions; eligible inputs can remain deductible | [Arts. 4(6)-(7), 27 and 33](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Specified reduced operations | 8% until changed by the Executive; only the operations listed in art. 64, reproduced below | [Art. 64, gazette p. 73](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Luxury consumption | 15% additional to the general rate until changed; applies only to the goods/services and qualifying values in art. 61 | [Art. 61, gazette pp. 72-73](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| General rate-setting limits | 8% to 16.5%; these bound the Executive's power, rather than replace art. 63's applicable rate | [Art. 27](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Luxury rate-setting limits | 15% to 20% additional; art. 61 supplies the statutory continuing rate and product list | [Arts. 27 and 61](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Foreign-currency additional IVA | unverified as an operative charge: art. 27 authorises 5% to 25% and arts. 62/71 require an Executive decree; no implementing rate decree was confirmed in this review | [Arts. 27, 62 and 71](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Input-credit exercise limit | 12 tax periods from invoice/debit-note issue, customs declaration, or imported-service tax-payment receipt, as applicable; all other eligibility requirements remain | [Art. 33](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Ordinary statutory assessment period | One calendar month; a special administrative regime must be checked separately | [Art. 32](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |

**Reduced operations, not a general essentials category.** Article 64 lists imports/sales of goats, sheep and minor species for slaughter or breeding; meat in natural, chilled, frozen, salted or brined form except the chicken, bovine and porcine meats exempt under art. 18(1)(o); lard; qualifying animal feed/minerals and exclusive inputs for those species; non-commercial predominantly intellectual professional services to public authorities; and domestic passenger air transport. Do not replace this list with “certain food.” [Art. 64](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

**Luxury conditions.** Article 61 includes automobiles with customs value or domestic factory price at least USD 40,000; motorcycles on the same valuation basis at least USD 20,000; listed civil aircraft/accessories and recreational/private vessels; coin/token or similar gambling machines and gaming tables; jewellery/watches priced at least USD 300; weapons/accessories/projectiles; separately fitted vehicle accessories priced at least USD 100; art/antiques priced at least USD 40,000; natural-fur/skin clothing/accessories priced at least USD 10,000; recreational/sport animals; caviar/substitutes. Its service list covers restricted-access restaurant/nightclub/bar memberships and maintenance fees, listed vessel/aircraft hire or use, and third-party services through text messaging or other technology. Examine the full item and valuation basis, not just the seller's industry. Where the general 16% and statutory additional 15% both apply, their sum is 31% of the same base; that is not a universal maximum rate. [Arts. 27, 61 and 63](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

## The base

### 1. Establish the event and period

Create a supply register independent of cash movements. Domestic goods generally trigger at the earliest of invoice, payment or actual delivery; sales to public bodies use the payment-order rule. Definitive imports trigger at registration of the customs declaration. Listed utilities use invoice issue; successive services use the earliest of invoice, payment or due consideration; public-body services use the payment-order rule; specified foreign services use receipt by the beneficiary; other services use the earliest event listed in art. 13(3)(e). Goods exports trigger on definitive departure. Apply the rate applicable to that event, rather than the rate when a later bank settlement arrives. [Art. 13](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

### 2. Build the price excluding IVA

For movable goods, start with invoiced price, subject to the market-price floor and the statutory definition of comparable open-market price between unrelated parties. Services, domestic or foreign, use total invoiced consideration and include goods supplied/attached as part of the service. Non-money consideration uses the assigned value subject to the statutory market-price floor. [Arts. 20 and 22](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

Add the accessories required by art. 23: price revisions, commissions, relevant interest and ancillary consideration; qualifying transport, packaging, insurance, installation and maintenance; specified container deposits; and other taxes except the exclusions expressly named there. Proper agency reimbursements and independently taxable ancillary services require separate treatment. Deduct ordinary trade discounts/bonuses supported on the invoice under art. 24. [Arts. 20-24](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

Definitive import base = customs value + the applicable import taxes, surcharges, compensatory/antidumping duties, late interest and other import expenses, excluding IVA and the national-tax exceptions in arts. 20-21. Reconcile later customs adjustments. Do not use only the supplier's foreign-currency invoice. [Art. 21](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

For foreign-currency domestic sales/services, art. 25 requires national-currency equivalence at the market exchange rate on the taxable-event day; if that day is not a financial-sector business day, it specifies the rate on the next business day. Import conversion follows customs law/regulations. Capture the actual applicable valuation evidence and denomination. A BCV rate may be relevant evidence, but this text does not establish the old unconditional “BCV transaction-date rate” shortcut or a current numerical exchange rate. [Arts. 25 and 69](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

### 3. Separate exemption, non-subjection and zero-rating

| Category | Treatment and conditions | Source |
|---|---|---|
| Listed basic food/agricultural items | Domestic sales of the exact art. 18 products are exempt. Product, preparation and end-use restrictions matter; the list is below. | [Ley del IVA art. 18](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Medicines/agrochemicals | Listed medicinal/agrochemical products and exclusively used active ingredients, including specified vaccines/sera/plasma and therapeutic/prophylactic substances for human, animal or plant use. A pharmacy description does not exempt every item sold there. | [Art. 18(3)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Disability/medical equipment and publishing | Listed adapted vehicles, wheelchairs and named medical devices/prostheses; newspapers/publishing paper, books, magazines, pamphlets and publishing inputs. Match the statutory product and applicable requirements. | [Art. 18(4)-(6)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Passenger and goods transport | National land/water passenger transport and goods transport are listed services; distinguish domestic passenger air transport under art. 64 and international transport under art. 15. | [Arts. 15, 19(1)-(2) and 64](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Education and institutional services | Education from institutions registered with the specified ministries; qualifying institution-only lodging/food and accessories for listed users; park/zoo/museum/cultural admissions operated by non-profit entities exempt from Impuesto sobre la Renta; in-premises student/worker canteen services. | [Art. 19(3)-(5), (8)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Health | Medical assistance, dentistry, surgery and hospitalisation services; the exact service is relevant, not merely a payee's name. | [Art. 19(6)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Residential utilities | Residential electricity, water, urban cleaning and gas, and national telephone service through public telephones; these do not exempt all commercial utilities/telecoms. | [Art. 19(9)-(13)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Fuel transport and animal rearing | Transport of hydrocarbon-derived fuels; listed livestock/poultry/minor-species rearing, reproduction and production. This does not establish a blanket exemption for gasoline/diesel sales. | [Art. 19(14)-(15)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Loans and banking | Money loans and the listed regulated financial operations are non-subject, rather than zero-rated exports. Review the art. 5 leasing/storage exceptions. | [Arts. 5 and 16(3)-(4)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Employment and insurance | Listed dependent employment and insurance/reinsurance operations are non-subject; independent services need their own analysis. | [Art. 16(5)-(6)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Residential rent | The service definition brings non-residential immovable-property rentals into IVA; distinguish the residential letting from a commercial rental or independent taxable service. | [Art. 4(4)](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |
| Exports | Qualifying exports are taxable at zero, with the input-credit distinction maintained. | [Arts. 4, 27 and 33](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) |

The art. 18 food list includes natural vegetable foods/certified seeds and named biological reproduction/agricultural inputs; specified poultry and eggs; rice; vegetable flour/semolina; bread/pasta; salt; non-industrial sugar/papelón; roasted/ground/bean coffee; mortadella; natural-presentation canned tuna; cylindrical canned sardines up to 170 g; specified milk/infant formula including soy; white cheese; margarine/butter; chicken/bovine/porcine meat in the stated conditions; mayonnaise; oats; bovine/porcine slaughter and breeding animals; edible oils other than olive oil. Further rows cover fertilisers and natural gas used to make them, human-food maize, animal-feed yellow maize, exclusive vegetable-oil inputs, specified feed/minerals and their exclusive inputs, sorghum and soy. Preserve the precise description; do not exempt a whole shop or invoice by keyword. [Art. 18](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

The statute also contains limited cultural/sport admissions, import-specific benefits and special-territory/transitional relief. Current numerical admission thresholds, import suspension/exoneration decrees and special-territory entitlement are outside the confirmed calculation here; see Sources. Never transfer the domestic art. 18 exemption mechanically to an import.

### 4. Compute output IVA and adjustments

Group taxable bases by event date and legally applicable rate, multiply each base by its rate, and sum the debits. Keep zero-rated, exempt and non-subject totals separately. If an invoice wrongly overstates IVA, art. 30 generally requires the invoiced debit to be included unless corrected within the same period. Record returns/cancellations and pricing/debit changes with the corrective documentation in arts. 36-37 and 58; retain the originals. Do not remove a debit just because its invoice is unpaid. [Arts. 28-30, 36-37 and 58](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

### 5. Test each input before allocating it

Apply these gates in order, recording the reason for any disallowance:

1. The claimant is a registered ordinary taxpayer, the charged IVA is legally due, and it relates to the claimant's habitual activity generating taxable or zero-rated operations. Exempt/formal or occasional status does not carry the same credit right. [Arts. 6, 8, 29 and 33](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
2. The invoice/customs/payment evidence is genuine, reliable and meets the statutory minimum requirements; the supplier is an ordinary taxpayer. Excess tax, false documents and non-ordinary suppliers do not create a valid deduction. [Arts. 33, 35 and 57](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
3. The expense is directly and exclusively linked to the business/profession. Goods used alternately or simultaneously for private purposes, items absent from the business accounting and personal/family/employee consumption fall within the exclusions. Do not substitute a casual business-use percentage for art. 33's private-use exclusions. [Art. 33, paragraphs one and two](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
4. Food/beverage services, alcoholic beverages and public spectacles are expressly excluded. A generic “entertainment” label should be resolved to the actual statutory category. Article 33 does **not** name all passenger vehicles as a prohibited class: determine the vehicle's activity, private use, accounting and documentation. [Art. 33](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).
5. Exercise the credit within the statutory period measured from the correct document; imported-service evidence is the tax-payment receipt. Keep the document date and claim period in the paper. [Arts. 33 and 48](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

For domestic purchases, invoice IVA can support the credit subject to those gates. For imported goods, document the tax actually paid on nationalisation. For a taxable non-domiciled service, the recipient determines and pays the IVA when the event occurs; **the payment receipt supports the ordinary taxpayer's credit**. Do not post a self-assessed debit and immediate matching credit without payment and the remaining eligibility tests. [Arts. 9, 29, 33, 35 and 48](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

### 6. Attribute inputs and perform prorrata

Deduct eligible inputs used exclusively in taxable operations in full. Exclude inputs used only for exempt/non-taxable activity. For eligible common inputs used partly in taxable operations where separate accounts are not maintained, art. 34 uses taxable sales / total sales for that same month, applied to the common input pool. Keep the attribution separate from private-use exclusions. Zero-rated activities retain the credit entitlement in art. 33. A month with no denominator or unusual non-sale items requires review, not an invented ratio. [Arts. 33-34](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

Nondeductible tax under this allocation becomes cost; it is not a future credit carryforward. Adjust credits for cancelled purchases/excess charges and properly received debit notes. [Arts. 35 and 37](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

### 7. Liquidate, keep distinct balances and reconcile cash

Ordinary period liability = adjusted output debits less eligible credits. An excess eligible credit carries to the following/successive periods until absorbed under art. 38. Reconcile opening excess to the prior filed return, then show the remaining balance. Distinguish that balance from excess withholding governed by art. 11 and exporter recovery governed by arts. 43-44; none is a generic cash refund or transferable tax asset. Cessation, merger/absorption and credit transfers have specific restrictions in arts. 40-41. [Arts. 31-32, 35, 38 and 40-44](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

Match every withholding certificate to supplier RIF, buyer/agent, invoice, period, actual withheld amount and any proof needed by the operative providencia. Maintain supplier receipts, agent remittances and recoverable withholding separately from purchase IVA. Do not reduce the return merely because the buyer paid less than the invoice. Current withholding percentage, exceptions, timing and excess-recovery procedure are unconfirmed here; this is a filing gate rather than a substitute rule. [Art. 11](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

### Local bank narration triage

These are document-search cues retained from the prior workflow, not official bank-export specifications or tax rules. Apply the cited supply/credit tests to the underlying documents.

| Narration or payee | Search and reconciliation action |
|---|---|
| TRANSFERENCIA [client], TRF DESDE, DEPOSITO EFECTIVO, CASH DEPOSIT | Find the invoice, own-account transfer, advance, loan, capital contribution or refund. A credit is not automatically a sale. |
| PAGO MOVIL, BIOPAGO, PUNTO DE VENTA, POS, MERCADOPAGO VE | Reconcile gross customer supplies, settlement fees, reversals and timing; do not use net settlement as the taxable base. |
| ZELLE, PAYPAL VE | Trace the actual supply and currency; distinguish payment processing from territoriality and keep IGTF assessment separate. |
| INTERESES, INT GANADOS; PRESTAMO, CREDITO | Identify regulated banking interest or loan principal under art. 16; do not classify all receipts described as interest without examining the source. |
| ALQUILER, ARRENDAMIENTO | Obtain the lease and invoice; distinguish commercial premises from residential letting. |
| CORPOELEC, ELECTRICIDAD | Determine commercial or residential supply and check invoice evidence. |
| CANTV, MOVILNET, MOVISTAR, DIGITEL | Obtain the service invoice; test exclusive business linkage and the actual service, including any special-rate item. |
| AUTOMOVIL, VEHICULO | Obtain purchase/customs documents and use records; apply the credit gates and any luxury output-rate conditions, not an automatic car block. |
| RESTAURANT, CENA, BANQUETE | Resolve whether the charge is a food/beverage service or another supply; apply art. 33's exclusions. |
| ARROZ, HARINA, PAN, CARNE, LECHE; FARMACIA, MEDICINA | Match exact goods and preparation/end-use to art. 18; a store's name does not prove exemption. |
| COLEGIO, UNIVERSIDAD; CONSULTA MEDICA, HOSPITAL | Match the service and registration/institution conditions in art. 19. |
| GASOLINA, DIESEL | Obtain the current fuel-sale decree and facts; do not inherit the old blanket fuel exemption. |
| SENIAT PAGO, IMPUESTO; IGTF PAGO | Tax settlement is not a purchase-credit invoice. Keep tax payments and distinct IGTF amounts separate. |
| IVSS, SEGURO SOCIAL, FAOV, BANAVIH; RETIRO PERSONAL | Separate contribution remittances/drawings from purchases. If goods were withdrawn from business inventory, examine output IVA under art. 4(3). |

The old bank-format hints are preserved as intake candidates: Banco de Venezuela (Fecha, Descripción, Débito, Crédito, Saldo); Banesco (Fecha, Referencia, Descripción, Monto, Saldo); Mercantil (Fecha, Descripción, Cargo, Abono, Saldo); Provincial/BBVA (Fecha, Concepto, Débito, Crédito, Saldo); Banco Nacional de Crédito (Fecha, Detalle, Débito, Crédito, Disponible); Banco del Tesoro (Fecha, Descripción, Debe, Haber, Saldo). Inspect the actual PDF/CSV header and opening/closing balance, date format, sign and denomination before mapping. Current export-format availability has not been confirmed from an official source. No narration alone establishes liability or deduction. The applicable legal tests remain [arts. 3-4, 13, 16, 18-19 and 33](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

## Deadlines and filing

Article 32 supplies the ordinary monthly period; art. 47 delegates return/payment place, date, form and conditions to implementing rules. Do not infer the ordinary due date from a special-taxpayer RIF calendar. The current 2026 calendar, applicable special/advance regimes, current retention filing and live IVA form were not obtained from primary text. Exact due dates and form numbers therefore remain unconfirmed in Sources.

Prepare the handoff in this order:

1. Match the RIF and registration to the legal person, establishments and notification effective dates; registration and changes are governed by arts. 51-53. Resolve ordinary/formal/occasional status and any special regime before choosing a period.
2. Close the supply and purchase books. Article 56 requires all operations, including non-taxable operations and corrective documents, to be recorded, and records/source media to be retained while the obligation is unprescribed. Record transactions in the month perfected; debit/credit notes in the month issued/received. Keep output, deductible-input and import accounts separately.
3. Check invoice particulars against arts. 54-57: consecutive invoice number; separate control number where applicable; issuer name, fiscal domicile and RIF; recipient identity/RIF and NIT if held; rate and IVA separate from price. Article 57 explains which missing minimums defeat credit and that other omissions may instead be formal infringements. Do not declare every typo automatically fatal. Obtain the operative invoicing providencia for the taxpayer and date before approving issuance media or additional fields.
4. Assemble taxable/zero/exempt/non-subject sales and import bases, output debits, eligible domestic/import/service credits, prorrata adjustments, opening excess and separately controlled withholding. Reconcile these to ledger and document totals, then to the bank via receivables/payables, fees, transfers and timing.
5. Use the actual [SENIAT fiscal portal](https://declaraciones.seniat.gob.ve/) for the matching natural/legal-person account once available. Obtain and retain the current official IVA manual/form and calendar. Map the working-paper descriptions to the **displayed field labels and codes**, choosing the proper period and original/substitute status. This review did not establish current menu names, numeric boxes, submission buttons or payment options; stop before submission while that mapping is missing.
6. Preview the mapped return and recompute liability/carryforward. Once the authorised reviewer approves the complete evidence, submit using the verified portal instructions; retain the accepted declaration/reference, payment instruction/reference and completed payment receipt, and reconcile the charged bank payment. An accepted declaration and actual payment must each be evidenced. Do not treat the offline working paper as a filed return.
7. For corrections, art. 50 distinguishes adjustments not producing tax payable, recorded in the detection period, from adjustments producing a payment difference, requiring a substitute return for the affected period. Check interest and penalties and the actual portal correction procedure. [Arts. 47-58](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

### Legacy Forma 30 mapping retained for reconciliation only

**Not approved for portal entry.** No current primary form was read to substantiate the former numeric map. Preserve these as legacy identifiers so old working papers can be reconciled; obtain the actual current code for every description before filing.

| Legacy identifier | Old description to reconcile | Current status |
|---|---|---|
| L1 | Ventas internas gravadas | Current field code unconfirmed |
| L2 | Débito fiscal en ventas internas | Current field code unconfirmed |
| L3 | Ventas de exportación | Current field code unconfirmed |
| L4 | Ventas internas no gravadas / exentas | Current field code and required separation unconfirmed |
| L5 | Total ventas | Current field code unconfirmed |
| L6 | Total débito fiscal | Current field code unconfirmed |
| L7 | Compras internas gravadas | Current field code unconfirmed |
| L8 | Crédito fiscal en compras internas | Current field code unconfirmed |
| L9 | Importaciones gravadas | Current field code unconfirmed |
| L10 | Crédito fiscal en importaciones | Current field code unconfirmed |
| L11 | Total crédito fiscal | Current field code unconfirmed |
| L12 | Ajustes / prorrata | Current field code unconfirmed |
| L13 | Crédito fiscal neto | Current field code unconfirmed |
| L14 | Diferencia | Current field code unconfirmed |
| L15 | Excedente crédito fiscal anterior | Current field code unconfirmed |
| L16 | Retenciones de IVA | Current field code and allowable timing unconfirmed |
| L17 | Total a pagar / excedente | Current field code unconfirmed |

### Working paper and completion checklist

```text
VENEZUELA IVA WORKING PAPER: tax year 2026
Taxpayer / RIF / establishment / status notices:
Period / regime / official due-date evidence:
Currency denomination / FX event and valuation evidence:
A. Supplies: event date, base, rate, debit; zero/exempt/non-subject separately
B. Inputs: document, date, legal IVA, activity link, payment evidence if required
C. Disallowances and eligible common-input pool / monthly prorrata
D. Adjusted debits minus eligible credits; opening excess; closing excess/payable
E. Withholding certificates: separately reconciled; operative deduction rule attached
F. Bank reconciliation: gross invoices, fees, settlements, transfers, contributions
G. Current form: actual field label/code -> working-paper row
H. Reviewer exceptions resolved / authorised return / acceptance / payment receipt
```

Finish only when taxpayer category, event dates, denomination/rates, exemptions, invoice minimums, imported-service payment evidence, credit age, monthly prorrata, prior excess, withholding and current form/calendar all reconcile. Keep IGTF separate. Missing items remain explicit open items; do not label the paper “filed” or claim this text supplies an end-to-end current portal procedure.

## Penalties and interest

Use the **Código Orgánico Tributario (https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf)** in Gaceta Oficial 6.507, not the former IVA-specific UT table. The government-hosted PDF below is labelled IVA in its filename but actually contains the COT extract; only its actual COT text is used here. Fixed monetary penalties use multiples of the official exchange rate of the highest-value currency published by BCV, valued at payment under art. 91. Do not substitute the Unidad Tributaria or a guessed present currency/rate. Percentage fines have the conversion/payment rule in art. 92.

| Breach | Statutory consequence and limits | Official source |
|---|---|---|
| Declaration incomplete or delayed no more than one year | Fine of 100 currency-rate multiples, COT art. 103(3); special-taxpayer pecuniary increase below | [COT arts. 91 and 103](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| No declaration, or delay exceeding one year | 150 currency-rate multiples and ten continuous days' closure if there is an establishment; art. 103(1) and its closure provisions | [COT art. 103](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Voluntary late payment, without extension and without verification/audit/determination concerning that tax | Within one year: 0.28% of the debt per day, capped at 100%; after one year additional 50%, after two years additional 150%, per the statutory time branches; audit payment instead engages art. 112 as appropriate | [COT art. 110](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Default interest | 1.2 times the applicable active bank rate, by each period of rate validity, from due date until discharge. Art. 66 defines BCV's preceding-month average and publication/fallback rules; no fixed monthly rate is supplied here. | [COT art. 66](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Failure to retain/collect; insufficient retention | Non-retention: 500% of tax not retained/collected. Under-retention: 100% of the shortfall. | [COT art. 115(1)-(2)](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Late remittance of retained tax | 5% per day for up to 100 days; later remittance and remittance during verification/audit engage the non-remittance rule and art. 121 as specified. Non-remittance fine: 1,000%; Republic/governorate/municipality and responsible-official rules differ in the same article. | [COT arts. 115(3)-(4) and 121](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Books not kept / fiscal memory destroyed, altered or not conserved | Art. 102(1)/(3): 150 currency-rate multiples and ten continuous days' closure; other listed books/record defects: 100 multiples and five continuous days. Article includes branch and continued-closure rules. | [COT art. 102](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| No invoice / unauthorised medium; specified false/illegible data or retention defects | Art. 101(1)-(4): 150 currency-rate multiples and ten continuous days' closure. Specified other invoice breaches under (5)-(8)/(11): 100 multiples and five days. Continued-closure and location rules must be read for the actual breach. | [COT art. 101](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Illegitimate diminution of tax | 100% to 300% of omitted tax, subject to art. 112's own exceptions/reduction and fraud provisions | [COT art. 112](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Fraud | Simulation, concealment, deception or other fraudulent manoeuvre reducing tax: six months to seven years' imprisonment; art. 119 also increases the art. 112 fine by 200%, with its separate improper-refund rule | [COT arts. 118-119](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Special-taxpayer formal infringements | Pecuniary sanctions in the formal-infringement chapter increase by 200%; this is not a blanket multiplier for every material fine | [COT art. 108](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |

These are statutory consequences, not a stackable quotation of a taxpayer's total exposure. COT arts. 82 and 94-97 govern concurrence, the range and aggravation/mitigation; art. 85 includes force majeure among exclusions from responsibility. Preserve evidence of SENIAT downtime and attempt/response dates, seek the applicable official extension or relief decision, and obtain specialist assessment. Downtime does not itself establish an automatic extension or cancellation of tax/interest. [COT arts. 66, 82, 85 and 94-97](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf).

## Cross-border points

Foreign payment is not the export test. Apply territorial execution/use and export-beneficiary/exclusive-use facts separately. Imported goods use customs event/base/payment evidence; imported services use the recipient-payment and credit-receipt sequence. [Ley del IVA arts. 4, 9, 13-15, 21, 25 and 48](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

Exporter credit recovery is a distinct process. Article 43 requires an application, supporting exports and eligible credits, with a monthly calculation. If domestic sales also exist, calculate deductible credit plus opening excess, subtract output debits to obtain undeducted credit, and compare that with total deductible credit multiplied by export sales / total sales; recover the lower figure, subject also to the statutory export-value cap. Article 44 requires verification of the actual exports, periods, domestic sales, input operations and supplier debit records. Do not recognise a cash refund from zero-rating alone. The current application procedure is outside scope pending implementing evidence. [Arts. 43-44](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

The foreign-currency additional IVA authority in arts. 27/62 is distinct from IGTF and requires the applicable decree before a percentage can be charged. Do not apply the legal authorisation range as if it were an enacted rate, or infer that there is universally no additional charge merely because the implementing text was not reached. Hydrocarbon zero-rating and specialised recovery, special territories, industrial pre-operating credits, diplomatic reciprocity and currency-control requirements need a separate specialist review. [Arts. 17, 27, 43-46 and 62-66](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

## Two worked examples that recompute

Four cases retain the old purchase, withholding, imported-service and vehicle scenarios with corrected evidential conditions. All amounts and the exchange conversion below are hypothetical facts, not published currency quotes or thresholds.

### Case 1: domestic purchase and ordinary settlement

A registered ordinary taxpayer makes standard-rated taxable sales of Bs. 30,000 excluding IVA and buys exclusively business office supplies for Bs. 10,000 plus IVA, gross Bs. 11,600. The invoice satisfies the statutory minimums, supplier is ordinary, credit is timely and no other disallowance applies. There is no opening excess or withholding. At the statutory 16% rate, output is Bs. 4,800, input Bs. 1,600 and the ordinary period calculation is Bs. 3,200 payable. Map the credit to the current labelled domestic-purchase field, not an unconfirmed “line 8.” [Arts. 28-29, 32-35 and 63](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

```oa-check
name: Domestic office supplies and period IVA
inputs:
  sales_base: 30000
  purchases_base: 10000
  rate: 0.16
steps:
  output: sales_base * rate
  input: purchases_base * rate
  purchase_gross: purchases_base + input
  payable: output - input
expected:
  output: 4800
  input: 1600
  purchase_gross: 11600
  payable: 3200
```

### Case 2: withholding certificate and cash reconciliation

The supplier's invoice is Bs. 10,000 plus Bs. 1,600 IVA. A certificate supplied as a case fact shows Bs. 1,200 withheld; cash received is Bs. 10,400. The arithmetic reconciles: receipt plus certificate equals gross invoice. This **does not validate a 75% legal rule**, current filing frequency or a “line 16” deduction. The provider's output debit remains Bs. 1,600; the certificate remains separately controlled until the operative retention providencia and its deduction period are confirmed. The legacy withholding scenario is retained without inventing the current rule. [Arts. 11 and 29](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

```oa-check
name: Supplied certificate reconciles supplier cash without assuming deductibility
inputs:
  base: 10000
  rate: 0.16
  certified_withheld: 1200
steps:
  output_debit: base * rate
  gross_invoice: base + output_debit
  supplier_cash: gross_invoice - certified_withheld
  reconciled: supplier_cash + certified_withheld
expected:
  output_debit: 1600
  gross_invoice: 11600
  supplier_cash: 10400
  reconciled: 11600
```

### Case 3: imported service, payment and common-input prorrata

A non-domiciled consultant provides a service used in Venezuela. The hypothetical fee is USD 1,000 and the supported art. 25 conversion for its event yields Bs. 36.60 per dollar: base Bs. 36,600, recipient IVA Bs. 5,856 at 16%. The recipient pays the tax and obtains the payment receipt. Assume it is a registered ordinary taxpayer, all documentary/age/business gates pass, the service is common to taxable and exempt activity, separate attribution is unavailable, and the month's taxable sales are Bs. 60,000 out of total Bs. 100,000. Only Bs. 3,513.60 of this common input is deductible under the monthly ratio; Bs. 2,342.40 is nondeductible cost. Without the payment receipt no credit is admitted by this case; with wholly qualifying taxable use, the full credit could instead be tested. There is no automatic immediate net-zero reverse charge. [Arts. 9, 15, 25, 33-35 and 48](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

```oa-check
name: Imported consulting paid and allocated to mixed operations
inputs:
  usd_fee: 1000
  hypothetical_event_fx: 36.60
  rate: 0.16
  taxable_sales: 60000
  total_sales: 100000
steps:
  service_base: usd_fee * hypothetical_event_fx
  recipient_tax_paid: service_base * rate
  ratio: taxable_sales / total_sales
  eligible_credit: recipient_tax_paid * ratio
  nondeductible_cost: recipient_tax_paid - eligible_credit
expected:
  service_base: 36600
  recipient_tax_paid: 5856
  eligible_credit: 3513.60
  nondeductible_cost: 2342.40
```

### Case 4: passenger car, personal use and the actual exclusion

A taxpayer buys a sedan for Bs. 200,000 plus Bs. 32,000 IVA, total Bs. 232,000. Assume evidence establishes personal/family use. Credit is zero under art. 33's private-use rule, and the IVA is included in cost under art. 42. The denial follows those facts, rather than a statutory ban on all passenger vehicles. A genuinely exclusively qualifying business vehicle needs its own eligibility and documentation assessment; the stated bolívar price alone cannot establish the USD customs/factory luxury threshold. [Arts. 33, 42 and 61](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf).

```oa-check
name: Sedan with documented personal use
inputs:
  base: 200000
  rate: 0.16
  eligible_credit: 0
steps:
  invoiced_tax: base * rate
  cash_price: base + invoiced_tax
  nondeductible_tax: invoiced_tax - eligible_credit
expected:
  invoiced_tax: 32000
  cash_price: 232000
  nondeductible_tax: 32000
```

## Ask the client first

After reading the records, request only missing facts:

1. RIF, registered activity, ordinary/formal/occasional classification, special designation notices and establishment details. Never default an unknown taxpayer to ordinary status.
2. Goods/services actually sold, product composition/preparation, customer locations and use, public-body customers, exempt/exonerated activity and any qualifying special-territory/decree claim.
3. Invoice/delivery/service/payment/due dates and currency denomination, with the actual event-date conversion evidence and customs documents where relevant.
4. Sales/purchase books, fiscal invoices, corrective documents, separate accounts for mixed activities and evidence of exclusive business use. A bank statement is a reconciliation input, not a minimum viable return.
5. Foreign supplier domicile, where a service is used, recipient tax payment/receipt, and export beneficiary/exclusive foreign-use evidence.
6. Prior return, opening excess eligible credit, withholding certificates, prior withholding balances and any refund/transfer application.
7. Current official calendar/form, taxpayer-specific notices and portal status. The preparer obtains the legal rates and procedures; do not ask the client to research tax law.

**Bank-only onboarding fallback:** preserve original statements, parse only the actual header/denomination, reconcile opening plus movements to closing balance, and tag transactions for documents using the narration table. Hold liability/credit and filing when status, event, rate, invoices or procedure is unresolved. Separate IGTF, contribution remittances, loans and own transfers; flag currency, luxury, mixed/exempt, imported-service and retention cases. Do not claim all credits are sales or block every vehicle automatically.

**When to refuse or refer:** hold an unsupported rate/current calendar/field mapping; refer hydrocarbon transactions, inflation-adjustment interactions, currency controls, IGTF computation, special fiscal territories, credit recovery, enforcement/fraud and contested downtime relief to the relevant specialist. Ordinary record reconstruction can continue while those issues are resolved. Do not produce a definitive filing figure by filling an evidence gap from memory.

**Version record:** v2.1 replaces the v2.0 bank-first draft with the sourced event/base/credit method, corrects status and penalty rules, and retains the old operational topics as evidence gates where not confirmed. The earlier v2.0/v1.1/v1.0 change labels are historical release descriptions, not evidence that the former rates or bank-format claims were reviewed.

## Sources

Read dates below mean the identified text was opened and read. The National Assembly's live PDF returned an unavailable-page response, independently checked in an ordinary browser; the dated archive is expressly identified. A government file's name or gazette summary was not treated as evidence of provisions absent from its contents.

| Text and provisions read | Official URL / dated archive | Read date and actual scope |
|---|---|---|
| Ley del IVA, Gaceta Oficial 6.507 of 29 January 2020, amendment and consolidated text | [Official Assembly original](https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf); [archived official capture 20261103211016](https://web.archive.org/web/20261103211016id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf) | 2026-11-11: read actual gazette pp. 62-74, amendment arts. 1-9 and consolidated arts. 1-72, particularly taxable events/status, exemptions, base, credits, payment, invoice/record duties and continuing rates. Statutory art. 63 expressly continues the general rate until changed. |
| Código Orgánico Tributario, same Gaceta Oficial, government-hosted extract | [Actual COT extract, despite IVA filename](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) | 2026-11-11: read arts. 66, 82, 85, 89-97, 101-103, 108-115, 118-121 for interest, fine units, conditions, special-taxpayer increase and enforcement. This extract does not contain the IVA law. |

Short exact source wording anchors the core distinctions: IVA art. 8, “exclusivamente actividades u operaciones exentas o exoneradas”; art. 33, “doce (12) períodos impositivos”; art. 34, “considerando únicamente las operaciones del mes en que se realiza”; art. 48, “La constancia de pago del impuesto constituirá el comprobante del crédito fiscal”; art. 63, “hasta tanto el Ejecutivo Nacional establezca una alícuota distinta”. COT art. 66 specifies “equivalentes a 1.2 veces la tasa activa bancaria”; art. 115(1) says “quinientos por ciento (500%)”. These are quotations of the law, not paraphrases of a search result.

Not yet confirmed: a complete later-decree/current-2026 administrative sweep; the live SENIAT IVA manual/form, the “Forma 30” identifier and former numeric lines L1-L17; ordinary filing/payment due dates and 2026 special-taxpayer/advance/retention calendars; the operative special designation and withholding providencias, including the 2025 replacement located but not read from primary text; legal withholding percentages, 100% cases, government-entity rules, certificate/deduction and excess-recovery timing. The former 2005 providencia citation, 75%/100% shortcut, lack-of-domicile trigger, half-month periods and old 20th/5th deadlines are not carried forward as law. Also unconfirmed: implementing decree/rate for foreign-currency additional IVA; BCV-only conversion as a universal rule; current UT value and numerical cultural-admission relief; current import suspensions/exonerations and fuel-sale exemptions; special-territory and transitional relief eligibility; detailed invoice-media/fiscal-machine/electronic rules and implementation dates; current bank export formats; currency-reform naming/date and actual exchange quotations; portal downtime extensions; current refund application steps. The old 5-50 UT filing, 1% monthly payment, 50-200 UT books and 1-5 day no-invoice figures are superseded by the COT rules above, not current alternatives. Resolve the relevant open point from official text before taking that position or filing.
