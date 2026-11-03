---
name: gn-property-tax
description: "Guinea CFU property and rental-income working method using the enacted March 2026 rate replacement, the enacted CGI base and DGI guidance updated in April 2026. Use it to test ownership and property scope, identify exemptions, build the ordinary occupied-property rental-value base, calculate CFU, and distinguish owner payment from rental withholding and its remittance. The governing version for the actual period must still be established, including any October rectification effect; otherwise outputs remain hypothetical analysis only. It preserves the previously reviewed four rate/base pairs and examples while adding substantive liability, valuation and collection steps. Vacant-property estimates, mixed use, part-year allocation, treaty relief, sanctions and detailed filing screens remain unresolved."
jurisdiction: GN
category: international
tax_year: 2026
tax_year_notes: "Enacted 31 March 2026 replacement text; earlier periods and October rectification status unconfirmed."
tier: 2
last_updated: 2026-11-01
version: 1.2
---

# Guinea CFU: property classification and rate workpaper v1.2

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Guinea.

## Who this applies to

**Governing-version prerequisite.** Before using this workflow for an actual period, establish the governing versions of the March CGI 265 rate replacement and the newly used CGI 257-264 and 266-272 liability, valuation, declaration and withholding provisions, including promulgation/effect and any October rectification. Establish that the April DGI interpretation remains applicable where used. If any governing version is unresolved, label every result **hypothetical source-version analysis only** and stop before a live liability, valuation, withholding, filing or payment conclusion. Neither the March rate replacement nor the April guidance proves the whole imported provision set remains operative unchanged.

Use to prepare the ordinary CFU liability, rental-value, rate and collection workpaper under the source versions below. Apply the governing-version prerequisite first. The expanded scope tests ownership/property liability and exemptions, assembles the ordinary occupied-property base, and distinguishes annual CFU from rental withholding. The rate comes from CGI article 265 as replaced by article 14 of Law L/2026/010/CNT of 31 March 2026. It remains a partial compliance workpaper, not a final assessment. The same official bundle contains promulgation decree D/2026/0103/PRG/SGG, signed 31 March 2026. Use this replacement text where applicable; allocation to periods before the replacement and the status/effect of the October rectifying bill remain unconfirmed. [Law art. 14 and decree arts. 1–2, PDF pp. 21,27](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf).

### Establish liability and exemptions before selecting a rate

CGI 257 imposes CFU on built/unbuilt property in Guinea and rental income. Article 259 makes the person owning the property on 1 January of the assessment year, or receiving rental income, liable. If the owner cannot be reached, the possessor, agent, tenant, legatee or other entitled person pays in the owner's name and for their account. Article 260 makes the lessee liable for a building constructed at its expense on leased land/property where it will revert to the lessor without compensation and free of charges. Obtain the title, use/lease rights, 1 January ownership and rental-income records before attributing liability. A private sale-contract apportionment does not itself replace the legal owner's liability. [CGI 257-260](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI 2026 précis §4.1.1.1](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

Built property includes permanent usable constructions, inseparable attached equipment/machines or machinery on special foundations forming part of the construction, and fixed advertising structures. Unbuilt property under article 262 includes bare commercial/industrial sites, quarries, ponds/saltworks, and built properties temporarily or permanently unfit for use, including reconstruction, demolition or ruin. Do not equate “unbuilt”, “unfinished” and “completed but unoccupied”: they are different classification questions. [CGI 261-262](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

Article 263 exempts state/local-authority property only when allocated to public/general-interest service and unproductive of income; places of worship; public preschool/school/university buildings; private preschool/school/university buildings erected by the institution's founders; agricultural buildings housing animals or storing crops; and diplomatic/consular-owned property subject to reciprocity, excluding private staff/collaborator use. Keep evidence for the precise condition. An exemption is not established just because the tenant is a school, farm or diplomat. [CGI 263](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Rates, bands and thresholds

| Confirmed property classification | CFU rate and base under replaced CGI 265 | Official source |
|---|---|---|
| Residential property occupied by its owner | 2% of actual annual rental value | [Law art. 14 / CGI 265, first bullet](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |
| Professional-use property occupied by its owner | 10% of actual annual rental value | [Law art. 14 / CGI 265, second bullet](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |
| Rented property | 15% of actual annual rental value | [Law art. 14 / CGI 265, third bullet](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |
| Completed property that is unoccupied | 5% of estimated annual rental value | [Law art. 14 / CGI 265, fourth bullet](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |

The base is rental value, not the property's purchase price. Keep actual annual rental value and estimated annual rental value in separate workpaper fields; the law uses different bases for occupied/rented and completed-unoccupied property. These rates do not establish that a particular taxpayer or property is taxable. [CGI 265 as replaced](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21).

## The base

0. Establish the governing-version prerequisite above and record the evidence for the actual period, including any October effect. If unresolved, stop live use; the following steps only illustrate the opened source versions hypothetically.
1. Establish the liable person, taxable property and any exemption using the scope rules above. Preserve title, lease, occupation/completion and exemption evidence. Keep each property and its use separately identified.
2. For the ordinary annual assessment, article 264 fixes the rental-value reference at 1 January of the assessment year. For owner-occupied residential property, use annual rent generated by comparable property of the same nature/category in the same neighbourhood and commune; absent a comparator, obtain a supported direct appraisal. Do not substitute purchase cost for a residential comparison. [CGI 264 I-II](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
3. For commercial-use property, article 264 III sets real rental value at 10% of market value, and market value at 70% of cost: the resulting ordinary base is 7% of supported property cost. Include fixtures falling within article 261; separate movable assets. The DGI applies this method to non-let commercial/industrial property. Obtain the cost support and resolve classification before using it. [CGI 261,264 III](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [précis §4.1.2](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).
4. For rented property, the DGI's current guidance uses annual rent, increased by owner expenses contractually borne by the tenant and decreased by tenant expenses borne by the owner. Reconcile the lease, gross annual rent and supported transfers of expenses; do not deduct every ownership expense as if this were a net-profit tax. This adjustment method is expressly attributed to administrative guidance, rather than quoted as the text of article 264. [DGI précis §4.1.2, propriétés louées](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).
5. Classify the rate category and multiply the established annual base by its rate. Keep actual annual rental value separate from the estimated annual rental value for completed unoccupied property. The March replacement uses an estimated base for the latter but does not supply its full estimation machinery. Do not automatically apply the commercial-cost formula to a vacant property without that conclusion. [CGI 265 as replaced](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21).
6. Test rental withholding separately below. Reconcile owner assessment, withholding evidence and any discharge before requesting another payment for the same property. Article 268 makes its specified rental withholding final for the CFU on rented property; it is not automatically another tax added to the annual amount. [CGI 268](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
7. Stop for mixed use, change of use, a disputed 1 January condition, partial ownership, an estimated vacancy base, special investment relief or a period before the rate replacement. Obtain the governing allocation/valuation/relief rules rather than assume a full-year rate decides the case. The workpaper records evidence, taxable/exempt status, category, base, rate, amount, collection route and unresolved questions.

## Deadlines and filing

### Owner declaration and annual payment

Owners of built/unbuilt properties must declare rental income with copies of authentic leases and rental contracts. CFU is collected by the tax receiver where the property is located; article 267 sets payment no later than 30 June each year, in one payment or instalments. The source does not give a separate instalment timetable to invent here. Record the assessment, declared base, due date and receipts. Article 272 requires property-transfer/use acts to mention that the owner is current with CFU; obtain that evidence for a sale or transfer. [CGI 266-267,272](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

### Rental withholding decision and remittance

Article 268 I requires withholding where an IS-liable legal person, state/local authority, public industrial/commercial establishment, NGO, international institution or diplomatic/consular mission pays rent to a person acting privately. It also covers property intermediaries passing rent to a private owner, and tenants paying rent on state/local-authority property. A landlord acts privately under article 268 II when the rented property is not entered among its business assets. Verify both payer category and landlord asset status; this is not a blanket withholding rule for every tenant. [CGI 268](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

The specified withholding is 15% of gross rent, deducted from the rent paid, and is final for CFU on the rented property. Remit to the tax receiver for the property's location within the first fifteen days of the month after paying rent. Article 270's form must identify payer, property address, owner, rental period, gross rent and withheld amount. Keep the payee's gross rent and cash received separate from the tax withheld; do not apply the annual valuation adjustments automatically to the statutory gross-rent withholding base. [CGI 268,270](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

By 15 February each year, the withholder supplies the annual statement of prior-year rents for all rented buildings and sums remitted. Reconcile that statement to each rent payment, withholding declaration and receipt. The current printable form identifier, portal boxes and authenticated payment/receipt screens remain unconfirmed; no live submission is performed by this Guide. [CGI 268 IV,270 III](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Penalties and interest

Article 267 III permits a third-party debt notice against rent when CFU is not paid on time. This does not establish a separate penalty percentage or interest rate. No complete current CFU sanction/appeal method has been verified in this expansion; obtain the notice and governing procedure before calculating a sanction or advising on a disputed assessment. [CGI 267 III](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Cross-border points

The DGI's April 2026 guidance expressly covers owners of Guinea property regardless of nationality or residence and distinguishes property ownership from rental-income liability. The enacted base and current guidance do not supply a complete treaty/foreign-credit answer here. A non-resident owner is not exempt merely because of residence, but treaty relief, foreign rental income received by a Guinea resident, fiscal representation and any double-tax relief require their separate governing rules and facts. The governing-version prerequisite remains in force. [CGI 257-260](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §4.1.1.1](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

## Two worked examples that recompute

First, an owner-occupied home has an independently confirmed actual annual rental-value base of GNF 60,000,000. The property is assumed taxable without exemption and the replaced article applies. CFU is GNF 1,200,000. The example establishes no valuation method.

```oa-check
name: Owner-occupied residential rate workpaper
inputs:
  confirmed_annual_rental_value: 60000000
  rate: 0.02
steps:
  - cfu: confirmed_annual_rental_value * rate
expected:
  cfu: 1200000
```

Second, compare a completed property remaining wholly unoccupied with a hypothetical letting for a full annual period. Each scenario has an independently confirmed GNF 120,000,000 annual base, estimated in the vacancy scenario and actual in the rental scenario. The results are GNF 6,000,000 and GNF 18,000,000. The GNF 12,000,000 difference is only the CFU component of a letting decision; rent, costs, other taxes and transition allocation are not modeled.

```oa-check
name: Vacancy versus full-period rental CFU component
inputs:
  confirmed_estimated_vacant_base: 120000000
  confirmed_actual_rented_base: 120000000
  vacant_rate: 0.05
  rented_rate: 0.15
steps:
  - vacant_cfu: confirmed_estimated_vacant_base * vacant_rate
  - rented_cfu: confirmed_actual_rented_base * rented_rate
  - additional_cfu_if_rented: rented_cfu - vacant_cfu
expected:
  vacant_cfu: 6000000
  rented_cfu: 18000000
  additional_cfu_if_rented: 12000000
```

### Additional base and withholding checks

For an owner-occupied professional property with supported cost of GNF 1,000,000,000, the assumed ordinary commercial valuation produces market value GNF 700,000,000 and actual annual rental value GNF 70,000,000. At the retained March professional-use rate, CFU is GNF 7,000,000. This example is conditional on the governing source versions and classification; it is not the vacant-property estimation method.

```oa-check
name: Owner-occupied commercial property cost to annual CFU
inputs:
  supported_property_cost: 1000000000
steps:
  - statutory_market_value: supported_property_cost * 0.70
  - actual_annual_rental_value: statutory_market_value * 0.10
  - cfu: actual_annual_rental_value * 0.10
expected:
  statutory_market_value: 700000000
  actual_annual_rental_value: 70000000
  cfu: 7000000
```

An IS-liable company pays gross monthly rent GNF 10,000,000 to an owner whose rented property is held privately. Assume the governing law and all withholding conditions are established. It withholds GNF 1,500,000 and pays the owner GNF 8,500,000, reconciling to the GNF 10,000,000 gross amount. Compare this with a payer/owner relationship outside article 268: its withholding cannot be assumed from the rent alone and must be reviewed separately, rather than mechanically deducting 15% from every tenant payment.

```oa-check
name: Qualifying rent payer deducts CFU withholding from gross rent
inputs:
  gross_rent: 10000000
steps:
  - cfu_withheld: gross_rent * 0.15
  - owner_cash: gross_rent - cfu_withheld
  - gross_reconciliation: owner_cash + cfu_withheld
expected:
  cfu_withheld: 1500000
  owner_cash: 8500000
  gross_reconciliation: 10000000
```

## Ask the client first

- What proves the governing source version for the actual period, including any October rectification effect?
- Who owned the property on 1 January, who receives rent, and are ownership, use or lease-to-build rights disputed?
- What are the property's location, condition, use, occupation and any change-of-use facts?
- Which precise exemption or approved investment relief is claimed, and what proves its conditions?
- What lease, comparable rent/appraisal, supported commercial-property cost and contractual expense transfers establish the base?
- What are payer category, landlord business-asset status, gross rent payments, withholding declarations, assessments and receipts; is either party non-resident?

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [DGB official enacted 2026 law bundle](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf), scanned law pp. 19–24, especially art. 14 fully replacing CGI 265 on p. 21; promulgation decree arts. 1–2 on p. 27 and corroborating reference on p. 28. Operative page and signed decree also visually inspected. | 2026-11-01 |

| [DGI enacted CGI base, L/2021/032/AN](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf), cover and full CFU division arts. 257-274 with neighbouring provisions. Hosted by ITIE Guinea; cover states promulgation and application from 1 January 2022. Read as the enacted base, not a complete current consolidation. | 2026-11-01 |
| [DGI Précis fiscal 2026, version 10 April 2026](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx), cover/introduction and full §4.1: liability, property scope, exemptions, bases, updated rates and collection. It expressly describes DGI's operational position and updates for LFI 2026; it is administrative guidance. | 2026-11-01 |

**Not yet confirmed:** effect before the 31 March rate replacement and final promulgated status/effect of the October 2026 rectifying bill; complete amendment chain for every CGI provision; completed-unoccupied estimation machinery; mixed use/change of use/part-year allocation, split rights and contested valuations; special investment reductions; treaty relief, foreign rental-income and foreign-credit method; current forms/portal/boxes/receipts and complete sanctions/appeals. The newly read enacted base and April guidance close substantive ordinary liability, valuation and collection gaps within the stated source versions, not the operative-version prerequisite or full country coverage.
