---
name: venezuela-transfer-pricing
description: "Apply Venezuela's transfer pricing rules to a Venezuelan taxpayer's 2026 transactions with foreign related enterprises. Covers related-party and low-tax-jurisdiction screening, comparability, the compulsory first consideration of comparable uncontrolled price, resale price, cost plus, profit split and transactional net margin, income adjustments, related-party debt and interest, Spanish-language documentation, the statutory information-return obligation, corresponding adjustments, advance pricing agreements and tax-audit safeguards. Use for precios de transferencia, partes vinculadas, libre concurrencia, subcapitalización, related-party imports, management charges, royalties, intragroup loans, SENIAT transfer pricing and acuerdos anticipados. Produces a documented pricing calculation and unresolved-items list. Current return forms, portal fields, administrative range calculations and special-taxpayer filing dates remain unconfirmed; this is not an executable filing guide."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/venezuela-transfer-pricing"
  jurisdiction: "VE"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Venezuela: transfer pricing (2026) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Answer layer.** Price the controlled transaction as independent parties would price a comparable transaction; consider comparable uncontrolled price (CUP) first and document why the method used fits the transaction. Calculate any income, cost or deduction adjustment for the transaction's fiscal year. Related-party interest has an additional debt/equity restriction. Keep the supporting calculation and documents in Spanish. The statutory information-return month does not establish the applicable administrative form, day or submission route. [LISLR arts. 109-111, 116, 140, 166-167](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

The law read is the consolidated **Decreto con Rango, Valor y Fuerza de Ley de Impuesto sobre la Renta** (LISLR), Gaceta Oficial 6.210 Extraordinario of 30 December 2015, and the **Código Orgánico Tributario** (COT), Gaceta Oficial 6.507 Extraordinario of 29 January 2020. These are facsimiles of the official gazettes on Venezuelan government hosts. This is a new skill, built from those texts, with no accountant approval. The sources were read on 11 November 2026; the unresolved administrative details are listed at the end.

## Who this applies to

The ordinary case is a Venezuelan taxpayer importing or exporting goods, services or rights with a foreign related enterprise. LISLR art. 109 requires arm's length income, costs and deductions; art. 110 expressly addresses related-party imports and exports. Article 114 defines a related enterprise through direct or indirect participation in another's management, control or capital, or participation by the same persons in both. It does not supply a numerical ownership percentage. Map the actual management and control links, rather than inventing a shareholding threshold. [LISLR arts. 109-110, 114](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

Include an independent intermediary when a Venezuelan resident uses that intermediary to transact with a foreign related party (art. 115). Transactions by Venezuelan resident or domiciled natural or legal persons with persons or entities located or domiciled in low-tax jurisdictions are presumed related unless proved otherwise (art. 117). The current administrative jurisdiction list must be obtained before deciding that a named destination qualifies. [LISLR arts. 115-117](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

**Boundary.** A wholly domestic arrangement is not treated here as either exempt or automatically subject to the foreign-related-party information return: art. 109 is broad while art. 110 expressly addresses imports/exports. Refer a domestic-only scope determination for a sourced legal analysis. Do not extend the foreign-transactions filing mechanics to it by analogy. This skill also does not set corporate income tax rates, withholding, VAT, customs values or exchange rates; those are distinct computations.

## Rates, bands and thresholds

| Item | Rule and conditions | Source URL and provision |
|---|---|---|
| Related-party ownership percentage | No percentage is stated in the definition; direct/indirect management, control or capital participation, including common participation, is the test | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20 (LISLR art. 114) |
| Pricing method | Consider CUP first; SENIAT evaluates whether the chosen method is the most appropriate for the transaction and economic activity | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22 (LISLR art. 140) |
| Related-party interest limitation | Deductible proportion is capped at 1; use the positive excess of annual average equity over annual average independent-party debt divided by related-party debt under art. 116, subject also to market conditions | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20 (LISLR art. 116) |
| Statutory information return | June following fiscal-year close, subject to the terms of the implementing providencia; for a 31 December 2026 close, the statutory month is June 2027, not a confirmed administrative filing day | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=24 (LISLR art. 166) |
| APA preliminary procedure | SENIAT has 30 working days to examine preliminary documentation and explain the procedure; silence permits submission of the proposal, not approval | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22 (LISLR art. 143) |
| APA decision | 12 months from submission; silence means rejection | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=23 (LISLR art. 151) |
| Ordinary APA period | Fiscal year of signature and 3 following fiscal years; a treaty mutual-agreement procedure may support a longer period | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=24 (LISLR art. 162) |
| TP documentation not maintained/conserved | 1,000 times the BCV official exchange rate of the highest-value currency; closure for 10 continuous days if there is an office, premises or establishment | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=14 (COT art. 104(12) and sanction paragraph) |
| Declaration not filed or more than 1 year late | General declaration sanction: 150 times that exchange-rate unit and closure for 10 continuous days if there is an establishment; classify the obligation correctly before applying | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=13 (COT art. 103(1)) |
| Declaration incomplete or no more than 1 year late | General declaration sanction: 100 times that exchange-rate unit | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=13 (COT art. 103(3)) |
| Declaration in an unauthorized form, medium, format or place | General declaration sanction: 50 times that exchange-rate unit | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=13 (COT art. 103(6)) |
| Special taxpayers: formal monetary penalties | Increase by 200%, meaning base penalty multiplied by 3; applies to formal offences in that chapter, not automatically to every tax penalty | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=14 (COT art. 108, final paragraph) |
| Tax omitted through unlawful diminution of tax revenue | 100%-300% of omitted tax, without prejudice to art. 119; art. 112's valuation exception and art. 196 acceptance/payment procedure must be tested | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=15 (COT art. 112) |
| Acceptance/payment in the art. 196 procedure | 30% of omitted tax for the accepted and paid amount, plus interest and other applicable fines; this is not a general voluntary-disclosure rate | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=24 (COT arts. 112, second paragraph, 195-196) |
| Late-payment interest | 1.2 times the applicable BCV-calculated active lending rate for each relevant period; the last SENIAT-published rate applies if the next rate is not published on time | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=9 (COT art. 66) |
| TP audit defence | 5 months for submissions/evidence after the art. 195 period expires, subject to the special art. 120 indicia rule | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=24 (COT art. 198) |
| TP audit final decision | 2 years from expiry of the defence-submission period; apply the statutory procedural exceptions | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=25 (COT art. 202, third paragraph) |

No table amount is a fixed bolívar fine. COT art. 91 uses the exchange rate prevailing **when paid** for fixed multiples. For percentage fines, art. 92 converts the amount using the highest-value currency's official exchange rate at the offence date and uses that currency's rate at payment. Do not replace the highest-value currency test with an assumed US-dollar unit. [COT arts. 91-92](https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=11).

## The base

### The method, step by step

1. **Build the transaction population.** Reconcile related-party sales, purchases, services, licences, financing and other controlled dealings to contracts and the books. Record date, counterparty, relationship, amount and currency. Screen intermediaries and low-tax-jurisdiction dealings. Work transaction by transaction; group closely linked/continuous transactions only when they cannot adequately be valued separately. A package must also be broken into its elements to test the total. [LISLR arts. 114-117, 129, 167(d)-(h)](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).
2. **Describe what each party does.** Compare property/service characteristics, functions, assets, risks, contractual terms, economic circumstances and business strategies. A comparable is acceptable if differences do not materially affect price/margin, or if reasonably accurate adjustments eliminate the effects. For services assess nature/duration; for goods, physical characteristics, quality, availability and volume; for intangibles, licence/sale, right, duration, protection and expected benefits. Check actual conduct alongside the contract. [LISLR arts. 120-128](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=21).
3. **Test the method.** First consider a reliable CUP, including the taxpayer's own uncontrolled dealings. Record each material difference and its adjustment; if a price comparison cannot be made reliably, document that failure before selecting another listed method. SENIAT may evaluate the appropriateness of the choice. [LISLR arts. 120, 134-140](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=21).
4. **Run the selected computation.** Use the methods table below. Reconcile the comparable and tested-party accounting measures before comparing gross or operating margins. Price controls, interest/exchange controls, royalty-payment controls and other State intervention are differences to analyze, not a reason to accept the controlled price without testing. Prior-year data may explain losses or economic/product cycles; it is not an automatic substitute for the transaction's circumstances. [LISLR arts. 132-139, 167(k)-(l)](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22).
5. **Bridge to taxable income.** If the controlled conditions deprived the Venezuelan enterprise of profits it would have earned independently, include that difference in the fiscal year in which the controlled transaction occurred. Show separately the booked amount, arm's length amount and adjustment to income, costs or deductions. Do not assume that a foreign downward adjustment authorizes a Venezuelan deduction: the treaty and acceptance conditions below matter. [LISLR arts. 109-112](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).
6. **Apply the separate debt test.** For related-party interest, use art. 116 after testing market terms, as described below. A market interest rate alone does not establish deductibility. [LISLR art. 116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).
7. **Close the evidence and filing workpapers.** Retain the document set below, price computation, reconciliation and unresolved items. Carry the supported adjustment into the income-tax working papers. Establish the current implementing return requirements before preparing a submission; the statutory obligation is described in the next section. [LISLR arts. 166-168](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=24).

### Methods and denominators

| Method | Computation and condition | Official source |
|---|---|---|
| CUP, precio comparable no controlado | Compare the controlled price with a comparable uncontrolled price under comparable circumstances; make reliable material-difference adjustments | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22 (LISLR arts. 120, 135, 140) |
| Resale price, precio de reventa | Start with the resale price to an independent customer and subtract the comparable gross profit margin calculated on that resale price; account for functions, assets and risks | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22 (LISLR art. 136) |
| Cost plus, costo adicionado | Add the comparable profit markup calculated on the supplier's relevant costs; maintain a consistent cost base and functional comparison | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22 (LISLR art. 137) |
| Profit split, división de beneficios | Add the operating profits of the related parties in the transaction and allocate the global operating profit using relevant assets, costs and expenses; allocate residual profit considering significant intangibles and the independent-party result | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22 (LISLR art. 138) |
| Transactional net margin | Determine the operating profit independent parties would earn in comparable transactions using an appropriate profitability indicator such as assets, sales, costs, expenses or cash flow | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22 (LISLR art. 139) |

LISLR arts. 130-131 permit unique prices/margins and, where precision cannot be obtained, ranges from comparable transactions or methods. They do not themselves give the administrative percentile formula or adjustment point. Do not supply a median or interquartile algorithm from another jurisdiction. Range-based cases remain referred pending confirmation of the implementing rule. [LISLR arts. 130-131](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22).

### Related-party debt and interest

LISLR art. 116 limits interest paid directly or indirectly to related parties when total related and independent debt exceeds equity. Prepare:

- Annual average equity = (opening equity + closing equity) / 2, before the fiscal inflation adjustment and excluding the year's profit/loss.
- Annual average debt = sum of each month-end debt balance / number of months in the fiscal year; exclude interest accrued in that month from that month's balance.
- Available equity = annual average equity minus annual average independent-party debt.
- If available equity is positive, divide it by the related-party debt measure specified in art. 116. A quotient at least 1 permits all the related-party interest; a quotient below 1 permits only that proportion. Do not produce a negative deduction when available equity is non-positive; refer that fact pattern for legal treatment.

The text uses `saldo anual` for related-party debt in the quotient and defines `saldo promedio anual` for debt in the surrounding paragraph. Where fluctuating related debt makes that wording change the outcome, record both measures and obtain a sourced interpretation; the worked case deliberately uses constant related debt. [LISLR art. 116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

Excess related debt over annual average equity is treated as equity under art. 116. Even when total debt does not exceed equity, a related loan lacking market terms is treated as equity. Analyze borrowing capacity without related-party intervention, the amount an independent lender would lend, interest and other terms as well as overall indebtedness. Do not confuse the denominator for interest deductibility (after subtracting independent debt) with the provision's separate equity-treatment sentence. [LISLR art. 116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

### The documentary file

Keep the information supporting the calculation in Spanish, translated where necessary, and preserve electronically held data securely and accessibly. LISLR art. 167 requires, among other material:

- Fixed assets, acquisition support, depreciation and disposals; activity risks; organization, functional departments, strategic alliances and distribution channels.
- Venezuelan taxpayer and related-party identities, RIF/tax identifiers, fiscal domicile, residence, proof of relationship, business/customer/ownership information; transaction dates, amounts and currencies.
- Multinational group activities, locations, intercompany operations and ownership changes; financial statements and production/cost-of-sales statements.
- Contracts, financing, guarantees, licences, royalties, research/cost allocations, securities and intangible-rights details; business strategy, volumes, credit/payment terms, quality certifications and exclusivity.
- Method selection and objective reasons, comparable operations and adjustments, functional/pricing analysis, monthly inventory controls/valuation, and details and decisions from foreign related-party TP audits or litigation.

[LISLR art. 167(a)-(o), including ñ and sole paragraph](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=24).

Retention is not simply “ten years from the invoice.” LISLR art. 167 refers to the legal retention period; COT arts. 55-56 set a general six-year prescription and a ten-year term in specified cases, including taxable events connected with acts or assets abroad. Article 59 sets different starting points for assessment, penalties and collection, and arts. 60-62 provide interruption/restart and suspension. Keep a documented retention calendar covering the applicable periods and any continuing proceedings; do not destroy a file merely because its initial calendar interval expired. [COT arts. 55-62](https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=8).

For international primary/secondary/open-market securities operations, keep the additional chronological book: buyer/seller, operation amount, unit price, units, interest, agreed currency and transaction-date exchange rate, date, intermediaries, negotiation location and custodians. [LISLR art. 168](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=25).

## Deadlines and filing

**Statute and administrative steps must be separated.** LISLR art. 166 says the information return for controlled transactions is presented in June following fiscal-year close, under an implementing providencia. The calendar-year 2026 case therefore points to statutory June 2027. A non-calendar year, special-taxpayer status or a RIF-based calendar requires the applicable providencia and calendar before a day can be given. No 2026 filing calendar is used here to promise a 2027 deadline. [LISLR art. 166](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=24).

Prepare a transaction schedule and reconcile it to the income-tax working papers and art. 167 file. The current return form, annex allocation, field identifiers, authorized receiving office or online path, submission acknowledgement and any amendment mechanics have not been confirmed from an accessible primary administrative source. Stop at the reviewed working papers until those are obtained. A successful login, a generic income-tax return or an old paper template is not evidence of the applicable TP submission procedure.

### Advance pricing agreements

A taxpayer may propose a valuation **before** the transactions. Non-residents planning Venezuelan activity through a permanent establishment or related entity may also apply. All related parties to the transactions must subscribe; withdrawal by any ends the procedure. Preliminary information identifies the parties/RIF/residence, transactions and proposed content; SENIAT has the 30-working-day preliminary period described above. [LISLR arts. 141-143](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=22).

The full proposal includes the technical/legal/economic/financial description, functions/risks, method, essential assumptions, currency, justification, value/range, comparables/adjustments, other pending valuation proposals and unaffected related dealings. SENIAT may investigate and approve the proposed or an alternative method, or reject it. An approved internationally accepted alternative method may be agreed; this does not license an unagreed method in an ordinary return. Silence after 12 months is rejection. [LISLR arts. 144-151](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=23).

An approved agreement is applied only as its terms require. Fraud/false information may invalidate it from signature; non-compliance may invalidate it from the breach. With the definitive income-tax return, submit a report of covered transactions, results/method implementation and significant changes in economic assumptions. A significant change may require modification subscribed by all affected parties. The ordinary term is signature year plus three following years, potentially longer under a treaty mutual agreement. Audit powers continue. [LISLR arts. 152-164](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=24). Modification proceedings and challenges to determinations require specialist handling under arts. 156-165; this skill does not provide the procedural application package.

## Penalties and interest

Use the figures in the table with their legal triggers. The low-tax-investment declaration is a different offence in COT art. 103(7); do not apply its higher fine merely because an ordinary TP information return concerns a foreign related party. The TP documentation offence is expressly art. 104(12). Special-taxpayer formal monetary penalties increase by 200% under art. 108. [COT arts. 103-104, 108](https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=13).

For an underassessment, COT art. 112's ordinary penalty is 100%-300% of omitted tax; its first paragraph excludes the specified case where a legally required property valuation is increased administratively by no more than one quarter. That is not a universal TP safe harbour. Its second paragraph links the 30% fine to acceptance/payment under art. 196. Article 195 gives 15 working days after notification of the assessment record for the omitted/corrected declaration and payment; partial acceptance obtains that treatment only for the accepted and paid amount. [COT arts. 112, 195-196](https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=15).

Interest accrues from the tax's payment deadline until discharge, even if the act's effects are suspended administratively or judicially. Article 66 uses each period's applicable rate and specifies BCV's active rate for the six largest commercial/universal banks by deposits, excluding preferential portfolios, for the immediately preceding month; SENIAT should publish it in the first ten continuous days of the month, otherwise its last published rate applies. Obtain those rates before computing a monetary total. [COT art. 66](https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=9).

**AUDIT FLASH POINT.** Send an actual assessment to Venezuelan tax counsel promptly. COT art. 198 gives the TP defence period of five months after art. 195's period expires, with a different fifteen-working-day rule where the record contains art. 120 indicia. For access to independent-party comparable information, a taxpayer may designate at most two representatives in writing within fifteen working days after that same art. 195 period; individuals may access it directly. Access runs to twenty working days after the final decision's notification; one substitution is allowed. Notes are permitted, removal or photocopying is not. Confidentiality responsibilities last five years from access or designation as the statute provides. The TP final-decision period is two years from the expiry of the defence-submission period; the art. 120 exception in art. 202 must also be examined. [COT arts. 198, 202](https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf#page=25).

## Cross-border points

LISLR art. 112 permits a Venezuelan related resident to submit a substitute return reflecting a foreign corresponding adjustment only where a fiscal treaty permits the foreign authority's adjustment and the Venezuelan administration accepts it. It is not an automatic bilateral deduction. Verify the actual treaty, covered taxes, parties, year and competent-authority acceptance before recommending relief. [LISLR art. 112](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

For matters the LISLR does not address, art. 113 refers to the OECD's 1995 transfer pricing guidelines or replacements **only to the extent consistent with the LISLR and Venezuela's treaties**. It does not itself enact a master-file, local-file or country-by-country reporting threshold. No such numerical threshold or no-filing conclusion is inferred here. [LISLR art. 113](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

Treaty rate tables, customs adjustments, indirect tax consequences, specialist APA procedure and the current low-tax-jurisdiction list are outside this ordinary pricing computation. They require their own primary-source checks.

## Two worked examples that recompute

All monetary values below are **hypothetical VES inputs in one consistent measurement basis**. Markups, margins, prices and balances are evidence assumptions, not Venezuelan legal rates. Tax rates, current exchange rates and monetary tax penalties are deliberately not supplied by these examples.

### Example 1: comparable sale and a method decision

A Venezuelan company sells 1,000 identical units to its foreign subsidiary for VES 90 each. It also sells the same quantity on the same date, terms, market and functions to an independent customer for VES 100 each. There are no material differences. The reliable internal CUP is VES 100, giving arm's length sales of VES 100,000 and an upward income adjustment of VES 10,000, allocated to the transaction's fiscal year. [LISLR arts. 109-111, 120, 135, 140](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

For the method decision, suppose a proposed cost-plus comparison instead gives a cost of VES 80 and an evidenced markup of 20%, producing VES 96 and an adjustment of VES 6,000. It is VES 4,000 lower than the CUP result. Select the reliable CUP in the stated facts: CUP is the statutory first option and directly matches the transaction. If the independent sale had material unadjustable differences, this conclusion would fail; document why a cost-plus or another method then supplies the most appropriate comparison. This is not an election to pay tax on whichever method gives the lower result.

```oa-check
name: Reliable internal CUP versus proposed cost plus
inputs:
  units: 1000
  controlled_price: 90
  comparable_price: 100
  unit_cost: 80
  hypothetical_markup: 0.20
steps:
  booked_sales: units * controlled_price
  cup_sales: units * comparable_price
  cup_adjustment: cup_sales - booked_sales
  cost_plus_price: unit_cost * (1 + hypothetical_markup)
  cost_plus_sales: units * cost_plus_price
  cost_plus_adjustment: cost_plus_sales - booked_sales
  difference_between_methods: cup_adjustment - cost_plus_adjustment
expected:
  booked_sales: 90000
  cup_sales: 100000
  cup_adjustment: 10000
  cost_plus_price: 96
  cost_plus_adjustment: 6000
  difference_between_methods: 4000
```

### Example 2: arm's length loan with a separate interest restriction

A company has opening qualifying equity of VES 900,000 and closing qualifying equity of VES 1,100,000, already excluding the year's profit/loss and before fiscal inflation adjustment. Independent debt is VES 200,000 at each month-end. Related debt is a constant VES 1,600,000 throughout the year and at each month-end, excluding accrued interest. Related interest paid is VES 160,000. Assume the borrowing itself and all its terms are established to be market terms and other ordinary deduction requirements are met. [LISLR art. 116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

Average equity is VES 1,000,000. Available equity is VES 800,000 after independent debt. The quotient is 800,000 / 1,600,000 = 0.5; deductible related interest is VES 80,000 and the remaining VES 80,000 is added back. The separate debt-as-equity sentence applies to the VES 600,000 of related debt above average equity; that is different from the VES 800,000 financing headroom after independent debt. Even a fully market-priced loan can face this restriction. A non-market loan requires the separate equity treatment, not merely this percentage limitation.

```oa-check
name: Constant related debt with positive equity headroom
inputs:
  opening_equity: 900000
  closing_equity: 1100000
  monthly_independent_debt: 200000
  monthly_related_debt: 1600000
  months: 12
  interest_paid: 160000
steps:
  average_equity: (opening_equity + closing_equity) / 2
  average_independent_debt: monthly_independent_debt * months / months
  average_related_debt: monthly_related_debt * months / months
  available_equity: average_equity - average_independent_debt
  deductible_fraction: min(1, available_equity / average_related_debt)
  deductible_interest: interest_paid * deductible_fraction
  interest_addback: interest_paid - deductible_interest
  related_debt_above_equity: max(0, average_related_debt - average_equity)
expected:
  average_equity: 1000000
  available_equity: 800000
  deductible_fraction: 0.5
  deductible_interest: 80000
  interest_addback: 80000
  related_debt_above_equity: 600000
```

## Ask the client first

1. What is the taxpayer's residence, entity type, actual fiscal-year start/close and SENIAT special-taxpayer status?
2. Who directly or indirectly manages, controls or owns each counterparty, where are they located/domiciled, and are intermediaries or low-tax jurisdictions involved?
3. What transactions, amounts, dates, currencies, contracts and book entries are in scope, including financing, licences, guarantees and services?
4. What functions, assets and risks does each party actually have; what independent transactions and reliable adjustments support the comparison?
5. For interest, what are qualifying opening/closing equity, every month-end related/independent debt balance, interest paid and evidence of independent borrowing terms?
6. Is there an APA, foreign adjustment, treaty claim, prior ruling or audit notice, and what primary administrative return/calendar instructions and Spanish-language records are available?

**When to refuse or refer.** Do not invent a comparable, profit markup, exchange rate, percentage ownership test, range adjustment point, treaty entitlement or filing field. Refer missing comparable data, a range computation without its administrative rule, fluctuating-debt ambiguity, non-positive equity headroom, domestic-only scope, an actual audit or an APA procedural application. Output the supported pricing calculation and precise missing evidence, not a filing-ready assurance.

## Sources

| Source | URL | Read on | Exact native-language wording and extent read |
|---|---|---|---|
| LISLR, Gaceta Oficial 6.210 Extraordinario, 30 December 2015; consolidated arts. 109-168, printed pp. 20-25 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf | 2026-11-11 | Read the complete TP chapter and neighbouring consolidated provisions. Art. 109: “los precios y montos de contraprestaciones que hubieran utilizado con o entre partes independientes en operaciones comparables”; art. 140: “deberá considerar el método del precio comparable no controlado como primera opción”; art. 166: “en el mes de junio siguiente a la fecha de cierre del ejercicio fiscal”. |
| COT, Gaceta Oficial 6.507 Extraordinario, 29 January 2020; official National Assembly PDF archived 2026-01-11, capture 20260111171201; arts. 55-66, 90-108, 112 and 193-203 | https://web.archive.org/web/20260111171201id_/https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-mediante-el-cual-se-dicta-el-codigo-organico-tributario-20211019155621.pdf | 2026-11-11 | Read the cited prescription, interest, sanctions and TP-audit sections with their adjacent exceptions. Live Assembly original returned 404 directly and in an ordinary browser; dated archive used. Its PDF is byte-identical to the previously reviewed public-authority copy (SHA256 ad9508084b172b77b9e1f98eaa86c46759418a4032177de6bf4cbbf176cac262). Art. 108: “las sanciones pecuniarias aplicables serán aumentadas en un doscientos por ciento (200%)”; art. 104(12): “No mantener o conservar la documentación e información que soporta el cálculo de los precios de transferencia”. |

Not yet confirmed: current implementing TP information-return form, annexes, portal/authorized receiving route, box identifiers, acknowledgement and amendment steps; the administrative range/median calculation and adjustment rule; current low-tax-jurisdiction list; any special-taxpayer or non-calendar-year administrative filing dates, including the 2027 calendar for a 2026 close; monetary penalty totals without the required BCV exchange rates and period interest rates; master-file/local-file/CbCR obligations or thresholds beyond the statute read; authoritative interpretation of `saldo anual` for fluctuating related debt and of non-positive equity headroom; domestic-only scope and subsequent administrative changes not established from the inaccessible SENIAT material. Direct SENIAT retrieval and an ordinary browser visit timed out on 2026-11-11; the archive route did not yield an accessible dated copy. These omissions keep the pack's TP domain partial.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `venezuela-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/venezuela-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
