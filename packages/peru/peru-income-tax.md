---
name: peru-income-tax
description: >
  Compute Peru individual work income tax for tax year 2026 before preparing
  a return, payroll reconciliation or payment. Covers domiciled individuals'
  fourth-category professional and director income, fifth-category employment,
  the 20% and 24-UIT limit, one combined 7-UIT deduction, evidenced additional
  expenses up to 3 UIT, progressive bands, fourth-category withholding and
  suspension, the actual monthly employment-withholding sequence, foreign
  income ordering and annual credits. Use for Impuesto a la Renta, rentas de
  trabajo, cuarta categoria, quinta categoria, recibos por honorarios, FV 616,
  FV 1609 and annual FV 709 preparation. Produces a sourced working paper
  and proposed filing for human approval. Capital/business computations and
  non-domiciled taxation require the separate category/source method.
version: 0.2
jurisdiction: PE
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: computation
---

# Peru individual work income tax, tax year 2026 v0.2

**Built from the law. Not yet approved.** Prepare the working and proposed filing. Do not submit, pay, amend or post journals without approval.

**Quick reference.** This is Peru, authority **SUNAT**, currency **sol / PEN / S/**, calendar year **1 January to 31 December 2026**. It is not Panama. Use 2026 UIT **PEN 5,500** for 2026 income, even though the annual return is filed later. The 7-UIT deduction is not a tax-band boundary. First establish domicile, tax year, income category and gross receipts; then deduct qualifying work deductions, add the relevant net foreign income and apply the scale. Annual liability is distinct from monthly withholding and the remaining balance.

## Who this applies to

This method covers domiciled individuals' **rentas de trabajo**, including independent fourth-category work under LIR art. 33(a), director and similar income under art. 33(b), employment fifth-category income under art. 34 and the net foreign-source income that art. 51 adds to work income. It also identifies the correct treatment when documents reveal another category. [LIR arts. 33-34](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [arts. 49 and 51](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf).

Confirm domicile under LIR arts. 6-8 and Regulation art. 4, including the effective date of gaining/losing status, before applying deductions. A passport, RUC, foreign employer or foreign bank deposit does not alone decide domicile or source. [LIR Chapter II](https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf), [Regulation art. 4](https://www.sunat.gob.pe/legislacion/renta/regla/cap2.pdf). Where travel or treaty facts matter, obtain the separate current primary-source domicile/source working and qualified Peru advice before finalising this computation.

### Category boundaries and referral

| Finding | Treatment and next action | Official source |
|---|---|---|
| Professional, artistic, scientific or trade activity performed individually | Test art. 33(a). Separate from business operations and the fifth-category exceptions below | [LIR arts. 28, 33-34](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf) |
| Director, sindico, mandatario, gestor de negocios, albacea or similar; municipal/regional council fees | Art. 33(b); no 20% deduction. Actual duties decide, not the bank description | [LIR art. 33(b)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [art. 45](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf) |
| Employment, including taxable cash/in-kind pay, bonuses and profit shares | Art. 34, subject to statutory exclusions. A separate civil-services contract can still fall within art. 34(e); services for a simultaneous employer can fall within (f) | [LIR art. 34](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf) |
| Genuine statutory CTS, qualifying labour indemnities, work-origin pensions or specified subsidies | Screen the exact art. 18 exclusions before treating a payroll-labelled credit as taxable salary | [LIR art. 18](https://www.sunat.gob.pe/legislacion/renta/ley/capiv.pdf) |
| Rental, dividends, interest, royalties, securities or property gains | Separate first/second-category computation. Do not aggregate domestic capital with work or apply a blanket 5% to every receipt | [LIR arts. 35-36 and 49](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [art. 52-A](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf) |
| Business, Nuevo RUS, RER or RMT activity | Separate business/regime work; [pe-corporate-income-tax](pe-corporate-income-tax.md) is the ordinary third-category route, not this personal-work scale | [LIR art. 28](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [Chapter VI art. 49](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf) |
| Non-domiciled individual | Do not apply the resident scale or resident work deductions. Peru-source employment has a 30% rate under art. 54(g), but other non-resident categories have their own rates/bases. Route to cross-border analysis | [LIR art. 54](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), [art. 76](https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf) |

For capital routing, art. 52-A uses **6.25% of qualifying net capital income**, with a separate **5% dividend** rule and profit-vintage/stability conditions. That does not mean 5% of gross sale proceeds or all interest: cost, deductions, exemptions, source and category matter. This file does not prepare rental, securities, property-sale or business returns. [LIR arts. 35-36](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [art. 52-A](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf).

## Rates, bands and thresholds

The table is for **2026** unless a row explicitly says historical comparison. Rate bands apply to the final taxable work/qualifying foreign base, not gross salary. Monetary limits calculated in UIT are recomputed from the official 2026 unit.

| Item and conditions | 2026 figure or boundary | Official source and short Spanish extract |
|---|---|---|
| UIT for 2026 computations | PEN 5,500; 2025 historical UIT was PEN 5,350 and belongs only to 2025 work | [SUNAT UIT table, DS 301-2025-EF](https://www.sunat.gob.pe/indicestasas/uit.html): `2026 ... 5,500` |
| Calendar exercise | 1 January to 31 December | [LIR art. 57](https://www.sunat.gob.pe/legislacion/renta/ley/capviii.pdf): `1 de enero`; `31 de diciembre` |
| Art. 33(a) gross fourth-category deduction | 20%, deduction capped at 24 UIT = PEN 132,000; no deduction for art. 33(b) income | [LIR art. 45](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf): `veinte por ciento (20%)`; `24 Unidades` |
| Fixed combined fourth/fifth-category deduction | 7 UIT = PEN 38,500, once in total and limited to those net domestic work categories | [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation art. 26](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf): `hasta el límite` |
| Evidenced additional work-expense deduction | Combined maximum 3 UIT = PEN 16,500, only amounts actually qualifying and paid; not automatic | [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [SUNAT 2026 guidance](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026): `S/ 16,500 para el 2026` |
| Taxable base up to 5 UIT | Up to PEN 27,500 at 8%; cumulative tax PEN 2,200 | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Hasta 5 UIT ... 8%` |
| Taxable base above 5 through 20 UIT | Above PEN 27,500 through PEN 110,000 at 14%; cumulative PEN 13,750 | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Más de 5 UIT hasta 20 UIT ... 14%` |
| Taxable base above 20 through 35 UIT | Above PEN 110,000 through PEN 192,500 at 17%; cumulative PEN 27,775 | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Más de 20 UIT hasta 35 UIT ... 17%` |
| Taxable base above 35 through 45 UIT | Above PEN 192,500 through PEN 247,500 at 20%; cumulative PEN 38,775 | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Más de 35 UIT hasta 45 UIT ... 20%` |
| Taxable base above 45 UIT | Excess above PEN 247,500 at 30% | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Más de 45 UIT ... 30%` |
| Fourth-category withholding, where payer is a statutory agent | 8% of gross paid/credited. Receipt not above PEN 1,500 or valid effective suspension can remove retention | [LIR art. 74](https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf), [RS 013-2007 arts. 8-9](https://www.sunat.gob.pe/legislacion/superin/2007/013.htm): `no supere los S/. 1500` |
| Fourth-category monthly payment, unless exception/suspension | 8% of gross fourth-category monthly receipts less that month's fourth-category withholding; fifth-category income screens the threshold but is not charged 8% here | [LIR art. 86](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf), [SUNAT monthly method](https://personas.sunat.gob.pe/trabajador-independiente/declaracion-pago): `resta las retenciones de cuarta categoría` |
| General monthly exception: fourth, or fourth plus fifth, income | Not above PEN 4,010; if threshold exceeded, test ordinary monthly tax on all fourth-category receipts, not just the excess | [RS 390-2025 art. 3(a)](https://www.sunat.gob.pe/legislacion/superin/2025/000390-2025.pdf), [RS 013-2007 art. 2](https://www.sunat.gob.pe/legislacion/superin/2007/013.htm): `4 010,00` |
| Monthly exception where art. 33(b) income exists, including combined other fourth/fifth | Not above PEN 3,208 | [RS 390-2025 art. 3(b)](https://www.sunat.gob.pe/legislacion/superin/2025/000390-2025.pdf): `3 208,00` |
| Ordinary projected-income suspension route, general | Not above PEN 48,125 annually; formal authorisation required and changed circumstances can restart tax | [RS 390-2025 art. 3(c)](https://www.sunat.gob.pe/legislacion/superin/2025/000390-2025.pdf), [RS 013-2007 art. 3](https://www.sunat.gob.pe/legislacion/superin/2007/013.htm): `48 125,00` |
| Suspension route where art. 33(b) income exists, including other fourth/fifth | Not above PEN 38,500 projected annual income | [RS 390-2025 art. 3(d)](https://www.sunat.gob.pe/legislacion/superin/2025/000390-2025.pdf): `38 500,00` |
| Current payment-method threshold for ordinary additional-expense claims | SUNAT requires qualifying means for agreed consideration at least PEN 2,000 or USD 500. Test the obligation, not artificial instalments; statutory exceptions require evidence | [Law 28194 arts. 3-6 and 8](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf), [SUNAT 2026 expense guidance](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026): `a partir de S/ 2000 soles o US$ 500` |

Cumulative figures follow the widths: 5 UIT at 8%; the next 15 UIT at 14%; next 15 UIT at 17%; next 10 UIT at 20%. Do not create one-sol gaps with ranges starting at a rounded whole sol, or apply the top marginal rate to the entire base.

## The base

### Required computation order

1. **Establish year, domicile, source, category and perception.** Fourth/fifth-category income generally belongs to the year perceived under art. 57. Reconcile gross receipts to actual availability; an issued but unpaid RHE and an income-tax retention are not respectively automatic receipt and an expense. Employment paid into a foreign account is not automatically foreign-source. [LIR art. 57](https://www.sunat.gob.pe/legislacion/renta/ley/capviii.pdf), [arts. 6-9](https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf).
2. **Split fourth-category gross.** Let A be art. 33(a) professional gross and B art. 33(b) director/similar gross. Deduct `min(20% x A, 24 x UIT)` from A only. Net fourth-category income is A minus that deduction plus B. Do not replace this statutory deduction with actual business costs, or assume an unclear receipt is director income merely to be conservative. Obtain the contract/duties. [LIR arts. 33](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [45](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf).
3. **Add taxable fifth-category gross.** Include all employers and taxable bonuses, gratificaciones, profit shares and in-kind pay. Remove only an established statutory exclusion, such as qualifying CTS under art. 18, not an arbitrary bank-label exclusion. Do not apply the 20% deduction to fifth-category pay. [LIR arts. 18](https://www.sunat.gob.pe/legislacion/renta/ley/capiv.pdf), [34](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf).
4. **Deduct work allowances once.** Deduct the fixed 7 UIT and evidenced additional expenses, the latter capped at 3 UIT. Their combined use is limited to net fourth/fifth-category income: floor the remaining domestic work base at zero. Unused work deductions do not reduce foreign-source income. The 3-UIT allowance is not a refund, tax credit or automatic 10-UIT exemption. [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation art. 26](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf).
5. **Check separate art. 49 deductions.** Supported ITF is limited to the residual net fourth-category income, using Regulation art. 28-B's fifth-first allocation of the 7/additional-UIT deductions; exclude ITF interest/fines. Qualified donations have their own recipient, evidence and 10% limit, not the additional-3-UIT expense bucket. Apply the complete art. 21(s)/28-B rules where present. Unabsorbed work deductions do not carry forward. [LIR art. 49](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation arts. 21(s), 28-B](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf).
6. **Only then add relevant net foreign-source income.** Use art. 51 netting/evidence and the separate qualifying foreign-securities branch. No overall foreign net loss offsets domestic work. Do not subtract another 20%, 7 UIT or 3 UIT from the foreign addition. [LIR arts. 51-51-A](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf). See the cross-border section below.
7. **Apply each marginal band.** With final non-negative base T and unit U, tax is `0.08 x min(T,5U) + 0.14 x min(max(T-5U,0),15U) + 0.17 x min(max(T-20U,0),15U) + 0.20 x min(max(T-35U,0),10U) + 0.30 x max(T-45U,0)`. Use decimal arithmetic and retain the unrounded band working; follow the actual form's rounding when transferring. [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf).
8. **Reconcile credits and settlement.** Apply only allowable documented fourth/fifth retentions, payments on account, prior eligible balances and foreign-tax credits. Do not deduct a retention twice because both the receipt and bank net show it. Separate annual liability, credits, residual payment and potential refund. [LIR arts. 87-88](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf).

For the ordinary no-ITF/no-donation case, the critical order is `max(0, net fourth + taxable fifth - 7UIT - qualifying additional deduction) + relevant positive net foreign income`. Foreign income is not placed inside that `max()` before the work deductions.

### Additional expenses: amount, documents and conditions

These are personal work deductions, not an unrestricted business-expense claim. Use amounts actually paid during 2026 and the proper eligible person, supplier, document and payment route. [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation art. 26-A](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf), [SUNAT's explicitly 2026 expense page](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026).

| Expense and conditions | Deductible part before combined cap | Official source |
|---|---|---|
| Peru immovable rent/subrent, not used exclusively for third-category business | 30% of qualifying agreed rent paid, including relevant accessories/services/landlord taxes and applicable IGV/IPM | [LIR art. 46(a)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf) |
| Peru medical/dental services qualifying as provider's fourth-category income | 30% of unreimbursed amount for self, spouse/recognised union, minor child, or adult child with qualifying CONADIS registration | [LIR art. 46(c)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation art. 26-A(a)](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf) |
| Other personal Peru services qualifying as provider's fourth-category income | 30%, excluding art. 33(b) director/similar services; third-category business services do not qualify through this route | [LIR art. 46(d)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation art. 26-A(b)](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf) |
| Qualifying hotel, restaurant and bar services | 15% of qualifying paid consideration including applicable IGV/IPM; supplier must meet the specified CIIU activity condition | [Regulation art. 26-A(d)](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf), [SUNAT 2026 page](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026) |
| EsSalud contributions for domestic workers | Actual qualifying contributions, 100%; taxpayer must be registered employer, supported by Form 1676/virtual 1676 | [LIR art. 46(e)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation art. 26-A(c)](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf) |

Sum the eligible fractions, then cap at **PEN 16,500** and at the remaining domestic work-income capacity. A PEN 10,000 medical payment produces at most PEN 3,000 deduction before these limits, not PEN 3,000 tax relief. Temporary tourism percentages labelled **2021-2022** in amendment notes are not 2026 rates. [LIR art. 46 and its dated notes](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation art. 26-A](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf).

Keep this evidence per item:

- **Rent:** if landlord is an individual without a business, physical/virtual **1683** identifying the tenant; for business landlord, qualifying electronic invoice. A cash bank deposit is not itself the rental tax document. Confirm the Peru property and non-exclusive-business condition. Rent paid by a married/recognised-union couple can be attributed equally only under SUNAT's communication rules; do not duplicate the full deduction for both. [SUNAT 2026 rent guidance](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026), [Regulation art. 26-A](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf).
- **Medical and other fourth-category services:** qualifying electronic RHE with correct DNI/RUC, registered payment and appropriate profession/service. For a foreign domiciled claimant, SUNAT requires RUC identification. A clinic invoice generating third-category income is not automatically a doctor's fourth-category receipt. For family treatment, document relationship, union registration, insurance reimbursement and required disability registration. [SUNAT 2026 page](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026).
- **Hotels/restaurants:** valid electronic document identifying claimant in the actual **DNI or RUC field**, not merely observations. Supplier active; no-habido status must be cured by year-end where the law permits; CIIU principal and any secondary activity must meet the exclusive qualifying 55/56 condition. Use SUNAT's restaurant/hotel consultation and preserve evidence. [SUNAT 2026 page](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026), [Regulation art. 26-A(d)](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf).
- **Supplier exclusions:** LIR art. 46 excludes a document issued while supplier is no-habido unless cured by 31 December, SUNAT-notified RUC deregistration, and published sujeto sin capacidad operativa status. A platform entry alone does not establish deductibility. [LIR art. 46(i)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf).
- **Payment evidence:** bancarizacion means qualifying financial-system means, not only an electronic transfer. Deposits, enabled cards and other statutory means can qualify. SUNAT's 2026 page uses **PEN 2,000 / USD 500 or more**. Do not split an agreed obligation into smaller cash instalments to avoid the rule. [Law 28194 arts. 3-5, 8](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf), [SUNAT 2026 page](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026).

**Reconcile the payment texts.** LIR art. 46 starts with qualifying means regardless of amount, but permits regulatory exceptions. Regulation art. 26-A expressly excepts smaller expenses and the specified Law 28194 art. 6 cases; its old fixed **PEN 3,500 / USD 1,000** wording is not a reason to ignore Law 28194's independently applicable amended **PEN 2,000 / USD 500** threshold. Apply the current law and 2026 SUNAT instruction together. Equally, do not reject every smaller cash-paid expense if its applicable exception, document and other conditions are satisfied. Special art. 6 cases need the actual facts, not a general cash exemption. [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [Regulation art. 26-A](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf), [Law 28194 arts. 3-8, amended by DL 1529](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf).

Only-fifth-category earners can consult deductions with **DNI and Clave SOL** if not required to hold RUC; others use RUC/SOL or App Personas. Review missing items against evidence rather than assuming the platform is exhaustive. The 2026 page contains a leftover reference to adding expenses in a **2025** return; that is not permission to claim 2026 costs in 2025. [SUNAT 2026 expense page](https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026).

### Document and bank-line reading

Descriptions are screening hints, not deterministic tax classification. Read contract, actual services, payment date, RHE/payroll, gross/net and any exemption before applying treatment. [LIR arts. 18](https://www.sunat.gob.pe/legislacion/renta/ley/capiv.pdf), [33-34](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [57](https://www.sunat.gob.pe/legislacion/renta/ley/capviii.pdf).

| Document/pattern | Record and verify |
|---|---|
| RHE, RXH, honorarios, consultoria, asesoria | Gross paid/credited fourth-category amount, receipt/payment status, art. 33(a)/(b) and any art. 34 employment override; gross is not the net bank receipt |
| Dieta directorio, mandatario, albacea, sindico, gestor | Actual art. 33(b) duties and gross amount; no 20% deduction if confirmed |
| Planilla, sueldo, salario, boleta de pago | Taxable gross employment, excluded amounts, pension/other deductions and tax withholding separately |
| Gratificacion, bono, participacion | Taxable employment screen and ordinary/extraordinary withholding treatment; a CTS deposit is a different statutory item |
| Foreign employer/bank payment | Physical service/source, domicile, foreign tax and currency evidence; do not classify from payer location alone |
| Alquiler cobrado, dividendos, intereses, regalias, venta de acciones | Capital/category/source referral, not automatic work income or blanket tax on the bank credit |
| Retencion 4ta, retencion 5ta, pago a cuenta | Reconcile authorised agent reports, receipt and SUNAT account as credits; do not treat as income deductions |
| FV 1609 / suspension | Actual authorisation, exercise, effective date, expiry and restart conditions; an application alone does not suspend |
| Transferencia propia / prestamo principal | Reconcile both accounts and loan contract; genuine own transfers/loan principal are not service earnings, but a description alone proves nothing |
| Devolucion SUNAT / saldo a favor | Reconcile to the tax refund/credit decision rather than automatically counting a new service receipt |
| Pago IGV | Keep separate from personal income-tax liability; use [peru-igv](peru-igv.md) |

For RHE sum **gross** receipts actually taxable in the year, keep retentions separately and reconcile credit notes. A certificado/reporte de rentas y retenciones corroborates payroll and credit totals; reconcile its period and omissions to boletas and payments. FV 1609's authorisation confirms suspension, not absence of annual tax. [SUNAT independent declaration guidance](https://personas.sunat.gob.pe/trabajador-independiente/declaracion-pago), [dependent guidance](https://personas.sunat.gob.pe/trabajador-dependiente/declaracion-pago).

### Working paper to retain

Record: year and UIT; RUC/DNI and due-date population; domicile/source facts; gross 33(a), 20% deduction/cap, net 33(a), gross 33(b), net fourth total; taxable fifth total; single 7 UIT; each eligible expense fraction and combined cap; residual domestic work base; supported ITF/donations; positive net foreign addition and excluded-loss schedule; final progressive base; each band and total annual tax; allowed foreign credit; separate fourth/fifth retentions, monthly payments and prior credits; balance payable or potential refund; return/payment identifiers; unresolved facts and approval. This retains the full calculation chain rather than just the final number.

Key terms: **renta bruta** gross income; **renta neta** income after applicable deductions; **retencion** withholding; **pago a cuenta** advance credit; **RHE/recibo por honorarios** independent-service receipt; **planilla/remuneracion** payroll/pay; **domiciliado** statutory tax domicile, with effective-date rules; **UIT** tax unit; **bancarizacion** qualifying financial-system payment; **comprobante de pago** qualifying tax document. None of those words alone establishes classification or deductibility.

## Deadlines and filing

### Fourth-category monthly computation and FV 616

Distinguish three tests: **receipt-level retention**, **monthly declaration/payment** and **annual tax/suspension projection**. A receipt at or below PEN 1,500 can have no retention while contributing to taxable monthly/annual income. A payer who is not a statutory retention agent does not automatically withhold. Do not apply 8% only to the excess over a threshold. [LIR arts. 71 and 74](https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf), [86](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf), [RS 013-2007 arts. 2, 8-9](https://www.sunat.gob.pe/legislacion/superin/2007/013.htm).

Where no monthly exception or valid suspension applies, multiply all gross fourth-category receipts for the month by 8%, then subtract that month's fourth-category retentions. Fifth-category income can affect the monthly exception population but is not itself part of this 8% base. If retentions fully cover the monthly payment, art. 86 does not require that payment declaration. The annual reconciliation still remains. [LIR art. 86](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf), [RS 013-2007 final provision 2](https://www.sunat.gob.pe/legislacion/superin/2007/013.htm).

SUNAT's current procedure is [Formulario Virtual 616](https://personas.sunat.gob.pe/trabajador-independiente/declaracion-pago):

1. Reconcile all paid/credited gross fourth-category receipts, credit notes, director income without a receipt where exempt from issuing, retentions and effective suspension.
2. Log into **SOL / Mis declaraciones y pagos / Presentacion y pago / Pago y presentacion de otras declaraciones / Trabajadores Independientes - 616**. Select the actual monthly period and declaration type.
3. Review **Detalle de comprobantes de pago**, including automatically incorporated electronic information. Add applicable printed/imported receipts for historic omitted/corrected periods and art. 33(b) income where no receipt was required. Reconcile gross, retention and resulting payment fields to the working. Current numbered fields were not independently confirmed.
4. Obtain approval, submit and use the supported online payment or generate **NPS** for an authorised banking channel. Save both accepted filing and payment receipts, period, tax code and operation number. A saved draft or unpaid NPS is not proof of payment.
5. SUNAT identifies **1662 / tax code 3041** for a separate fourth-category monthly payment when a declaration was made without payment. Verify period and debt before using it. Do not use that monthly code automatically for annual work-tax settlement.

Use the applicable monthly RUC schedule and actual extensions. The page's old November/December 2025 navigation banner is not a 2026 monthly timetable. Source for the sequence, named fields, NPS and 3041: [SUNAT independent declaration/payment](https://personas.sunat.gob.pe/trabajador-independiente/declaracion-pago).

### Fourth-category suspension: FV 1609 and restart

RS 390-2025 supplies **2026** amounts; RS 013-2007 supplies the application, projection, authorisation and restart framework. The general annual ceiling is not a universal zero-tax guarantee: director income, foreign income and other facts can change the annual result. [RS 390-2025 arts. 1-4/final provision](https://www.sunat.gob.pe/legislacion/superin/2025/000390-2025.pdf), [RS 013-2007 arts. 3-11](https://www.sunat.gob.pe/legislacion/superin/2007/013.htm).

1. Identify when fourth-category activity began, whether art. 33(b) income exists, actual fourth/fifth income, RS 013's applicable reference period and the current annual projection. For shorter activity in the reference period, apply its prescribed fourth-category average/annualisation plus fifth income. Do not simply compare one month's receipt to the annual ceiling.
2. Check the ordinary projected-income route against PEN 48,125, or PEN 38,500 where director/similar income exists. For earners who began before November of the previous exercise, the amended first-half route permits January-June suspension when projected annual tax is not above **8% x projected fourth-category monthly average x elapsed months including the application month**. The average is projected fourth-category income divided by 12. From July, compare projected tax with fourth/fifth retentions and fourth payments made through the preceding month plus the prior-year credit not refunded. A failed ordinary income ceiling does not alone reject these alternative coverage routes. The RS 013 HTML still shows historic 10%; [DS 377-2014-EF art. 1](https://cdn.www.gob.pe/uploads/document/file/252637/227659_file20181218-16260-1we2y1a.pdf) and [RS 002-2015 sole modifying provision, scanned page 3](https://www.sunat.gob.pe/legislacion/superin/2015/002-2015.pdf) replace it with 8%. [SUNAT Informe 090-2015 pp. 2-3](https://www.sunat.gob.pe/legislacion/oficios/2015/informe-oficios/i090-2015.pdf) confirms the average, reference period and both coverage routes.
3. In **SOL / Mis tramites y consultas / Suspension de retenciones de cuarta categoria**, open **FV 1609**. Enter every required fact honestly and obtain **Constancia de Autorizacion** with result, operation number, taxpayer, presentation date and exercise. Save it and give it to the retention agent.
4. For retention, approval takes effect for income made available **from the next calendar day**; for monthly payments, from the **period in which authorisation is issued**. Ordinary validity ends at exercise end, subject to restart. Submission alone is not authorisation.
5. If revised income means retentions/payments/prior credit will not cover the annual tax, restart payments for the **period of the change** and retentions from the **following day**, showing retention on subsequent receipts. Recompute the projection and retain the reason.
6. The exceptional in-person route is for the stated online rejection/omitted-information or service-unavailability cases, not a way around the eligibility test. RS 013 art. 6 gives the 30-day rejection window, temporary authorisation through the second following month's end bounded by year-end, and online regularisation before expiry. RS 390 art. 4 identifies the applicable exceptional-request format.

Procedure and dates: [RS 013-2007 arts. 3-11/reference-period final provision](https://www.sunat.gob.pe/legislacion/superin/2007/013.htm), [SUNAT 2026 suspension guidance](https://personas.sunat.gob.pe/trabajador-independiente/suspension-retenciones), [RS 390-2025](https://www.sunat.gob.pe/legislacion/superin/2025/000390-2025.pdf). The historical form-version/disquette paragraphs in the 2007 resolution are not current FV 616 software instructions.

### Employment withholding: actual monthly sequence

The employer's retention is not annual tax divided by twelve in every month. Project ordinary pay for the remaining months **including the current month**, add ordinary gratificaciones for the exercise and amounts already paid earlier in the year. Deduct the fixed **7 UIT**, apply the progressive scale and relevant statutory credits. Do **not** deduct the additional 3-UIT expenses in monthly payroll. Sole-fifth donations have the specified December-only final-adjustment route with evidence. [LIR art. 75](https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf), [Regulation art. 40(a)-(c)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf).

| Payroll month | From the recomputed annual projected tax subtract | Ordinary division | Official source |
|---|---|---|---|
| January-March | Relevant statutory credits already included in the annual calculation; not a new deduction of current-year prior payroll retentions in this step | 12 | [Regulation art. 40(d)(1)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| April | January-March retentions | 9 | [Regulation art. 40(d)(2)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| May-July | January-April retentions | 8 | [Regulation art. 40(d)(3)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| August | January-July retentions | 5 | [Regulation art. 40(d)(4)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| September-November | January-August retentions | 4 | [Regulation art. 40(d)(5)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| December | January-November retentions | Remaining final adjustment | [Regulation art. 40(d)(6)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |

An extraordinary bonus/profit payment triggers art. 40(e)'s additional incremental tax in that month, separately from ordinary retention. Include taxable in-kind pay at the required value. Variable pay, a new employer, mid-year entry and termination need art. 41; do not blindly multiply a short employment contract's months or retain a fixed twelve-month shortcut. Termination final adjustment and excess refund follow arts. 41-42. For simultaneous employers, the employer paying the highest remuneration consolidates under the employee declarations; retain earlier-employer income/retention evidence. [Regulation arts. 40(e)-(f), 41-44](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf), [SUNAT dependent procedure](https://personas.sunat.gob.pe/trabajador-dependiente/declaracion-pago). The employer reports/pays through PLAME; [peru-payroll](peru-payroll.md) owns the complete employer return.

### Annual return: year-specific filing dependency

LIR art. 79 normally excepts an exclusively fifth-category recipient, **but expressly includes exceptions for the additional-expense deduction and excess-retention refund**. A fifth-only under-retention can instead need the separate regularising payment route; do not infer that every shortfall automatically requires FV 709. Verify all categories, annual resolution and refund position. [LIR art. 79](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf), [SUNAT fifth-category guidance](https://personas.sunat.gob.pe/trabajador-dependiente/declaracion-pago).

The published **Renta 2025** procedure uses **FV 709 - Renta Anual - Persona Natural** through SOL or **App Personas**. Its information is referential and must be verified/modified before submission. That page is not evidence that the **2026** return form/version, boxes or 2027 due dates have been released. [SUNAT annual procedure, explicitly 2025](https://renta.sunat.gob.pe/personas/como-realizar-la-declaracion-del-impuesto-la-renta).

For 2026 annual preparation:

1. Complete the working paper and reconcile receipts, retentions, monthly payments, prior credit and deductions. Determine whether required/eligible to file under the actual 2026 resolution.
2. Once released, enter **SOL / Mis declaraciones y pagos / Presentacion y pago / Renta Anual / 709 Renta Anual Personas** or the supported App Personas route. Select **2026** and correct original/substitute/correction type. Confirm the released year before uploading.
3. Review identification and informative data, separate income categories, gross fourth/fifth, additional-expense details, foreign income and tax credits. Reconcile the personalised information to evidence. Transfer the progressive working, retentions/payments and balance; do not inherit an old numbered box without confirming the current form help.
4. Obtain approval and submit. Retain **Constancia de Presentacion y Pago** and any separate payment receipt. Arrange residual payment through the current supported channel and verify period/code. SUNAT identifies annual work tax code **3073**, distinct from monthly fourth-category 3041; confirm the actual year's payment reference.
5. If refund is appropriate, follow the supported refund application rather than assuming the annual credit is automatically cash. SUNAT's independent-worker page describes the linked **FV 1649** request after declaration and a separate instalment-request **FV 687** route for debt. Confirm the applicable live process, retain the request receipt and monitor SOL notifications. Do not make or apply for these actions without approval.

Portal route is shown in [SUNAT's 2025 FV 709 illustrated procedure](https://renta.sunat.gob.pe/sites/default/files/inline-files/Pasos%20devolucion%20FV%20709.pdf); general payment/refund routes and 3073 are described in [dependent guidance](https://personas.sunat.gob.pe/trabajador-dependiente/declaracion-pago) and [independent guidance](https://personas.sunat.gob.pe/trabajador-independiente/declaracion-pago). These are procedural references, not a claim to have inspected an unreleased 2026 form. Exact numbered 2026 fields, required annexes and current refund eligibility remain a filing check.

**Do not recycle the old dates.** The former table listing 27 May through 10 June **2026** is for **tax year 2025** under RS 386-2025, not for this tax year. The official [2025 schedule](https://renta.sunat.gob.pe/personas/cronograma-de-declaracion-renta-anual-2025-formulario-ndeg-709) is retained only as the historical destination for that old topic. Exact 2027 RUC-specific deadlines and extensions for 2026 were not confirmed.

## Penalties and interest

Late determinative filing, understatement, failure to withhold and failure to pay retained tax are different offences under Tax Code arts. 176-178. Identify the taxpayer's applicable table and facts; do not import a company's Table I amount into a personal-worker case. Art. 180 controls the applicable UIT/other basis. Relief depends on current graduality/discretion, correction, notice and payment stage; no universal fine or discount is asserted here. [Tax Code arts. 166, 176-180 and applicable tables](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf).

Art. 33 charges daily interest from the day after the due date through payment inclusive using monthly TIM divided by **30**, subject to statutory suspension rules. Numeric TIM, period changes and case-specific relief were not confirmed. For debt, instalments, notices, objections or coercive collection, obtain the actual SOL record and a qualified Peru adviser before changing a position. Do not present an estimated computation as a settlement figure or assume a pending instalment request stops collection. [Tax Code arts. 33 and 36](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf).

## Cross-border points

The relevant foreign addition is **net foreign-source income**, after art. 51/51-A conditions and evidence, added **after domestic work deductions**. Foreign securities meeting art. 51's special market conditions follow the capital-income branch instead; foreign income is not invariably work income. Excluded low/no-tax or preferential-regime losses do not enter ordinary netting, and an overall foreign loss cannot offset Peru work income. [LIR arts. 51-51-A](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf).

Foreign tax is not automatically a full refund or deduction. Art. 88(e) limits qualifying foreign income-tax credit to the statutory average-rate ceiling and actually paid eligible foreign tax; unused excess cannot carry forward or be refunded. Verify currency translation, finality, documentary evidence and any treaty. Complete a separate current primary-source foreign-credit and domicile/travel working, with qualified Peru advice where needed, preserving this file's work-income ordering. [LIR art. 88](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf), [Regulation art. 58](https://www.sunat.gob.pe/legislacion/renta/regla/cap11.pdf).

Peru-source employment of a non-domiciled person is a different art. 54(g)/76 computation, not this resident deduction method. Do not generalise its 30% employment rate to all non-resident capital receipts. A tax treaty, Andean rule or change of domicile can alter the analysis; obtain facts before selecting a rate. [LIR arts. 6-10](https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf), [54](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), [76](https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf).

## Two worked examples that recompute

The following cases preserve all six old example families, recomputed with **2026** UIT and expanded with the foreign-ordering and monthly-payment boundaries. They assume confirmed domicile, category/source, ordinary rules, no separate ITF/donation or foreign-credit item unless stated, and documented amounts. All tax results precede unspecified annual credits; a receipt-level retention is not the final annual rate.

### 1. Independent professional only

Gross professional receipts PEN 60,000 yield a PEN 12,000 statutory deduction and PEN 48,000 net fourth-category income. After PEN 38,500 fixed deduction, the PEN 9,500 base produces PEN 760 tax. The annual liability is not the 8% receipts retention.

```oa-check
name: Independent professional only, 2026
inputs:
  professional_gross: 60000
  director_gross: 0
  employment_gross: 0
  eligible_expense_fraction: 0
  net_foreign_addition: 0
  uit: 5500
steps:
  - professional_deduction: min(professional_gross * 0.20, 24 * uit)
  - net_fourth: professional_gross - professional_deduction + director_gross
  - additional: min(eligible_expense_fraction, 3 * uit, max(0, net_fourth + employment_gross - 7 * uit))
  - domestic_base: max(0, net_fourth + employment_gross - 7 * uit - additional)
  - taxable_base: domestic_base + net_foreign_addition
  - band1: min(taxable_base, 5 * uit) * 0.08
  - band2: min(max(taxable_base - 5 * uit, 0), 15 * uit) * 0.14
  - band3: min(max(taxable_base - 20 * uit, 0), 15 * uit) * 0.17
  - band4: min(max(taxable_base - 35 * uit, 0), 10 * uit) * 0.20
  - band5: max(taxable_base - 45 * uit, 0) * 0.30
  - annual_tax: band1 + band2 + band3 + band4 + band5
expected:
  professional_deduction: 12000.0
  net_fourth: 48000.0
  additional: 0
  domestic_base: 9500.0
  taxable_base: 9500.0
  band1: 760.000
  band2: 0.00
  band3: 0.00
  band4: 0.00
  band5: 0.00
  annual_tax: 760
```

### 2. Employment only, before additional deductions

Taxable gross fifth-category income PEN 90,000 is an annual total already including all taxable employment items. After PEN 38,500, base PEN 51,500 produces PEN 2,200 plus PEN 3,360, total PEN 5,560. Do not add another two gratificaciones to an annual total which already includes them. The annual-return exception still needs its statutory refund/additional-expense checks.

```oa-check
name: Employment only, before additional deductions, 2026
inputs:
  professional_gross: 0
  director_gross: 0
  employment_gross: 90000
  eligible_expense_fraction: 0
  net_foreign_addition: 0
  uit: 5500
steps:
  - professional_deduction: min(professional_gross * 0.20, 24 * uit)
  - net_fourth: professional_gross - professional_deduction + director_gross
  - additional: min(eligible_expense_fraction, 3 * uit, max(0, net_fourth + employment_gross - 7 * uit))
  - domestic_base: max(0, net_fourth + employment_gross - 7 * uit - additional)
  - taxable_base: domestic_base + net_foreign_addition
  - band1: min(taxable_base, 5 * uit) * 0.08
  - band2: min(max(taxable_base - 5 * uit, 0), 15 * uit) * 0.14
  - band3: min(max(taxable_base - 20 * uit, 0), 15 * uit) * 0.17
  - band4: min(max(taxable_base - 35 * uit, 0), 10 * uit) * 0.20
  - band5: max(taxable_base - 45 * uit, 0) * 0.30
  - annual_tax: band1 + band2 + band3 + band4 + band5
expected:
  professional_deduction: 0.0
  net_fourth: 0.0
  additional: 0
  domestic_base: 51500.0
  taxable_base: 51500.0
  band1: 2200.00
  band2: 3360.000
  band3: 0.00
  band4: 0.00
  band5: 0.00
  annual_tax: 5560
```

### 3. Professional work and employment combined

Professional gross PEN 50,000 less PEN 10,000 gives PEN 40,000; adding taxable fifth income PEN 120,000 gives PEN 160,000. One PEN 38,500 deduction leaves PEN 121,500. Band tax is PEN 2,200 + PEN 11,550 + PEN 1,955 = PEN 15,705. The allowance is not given separately to each category.

```oa-check
name: Professional work and employment combined, 2026
inputs:
  professional_gross: 50000
  director_gross: 0
  employment_gross: 120000
  eligible_expense_fraction: 0
  net_foreign_addition: 0
  uit: 5500
steps:
  - professional_deduction: min(professional_gross * 0.20, 24 * uit)
  - net_fourth: professional_gross - professional_deduction + director_gross
  - additional: min(eligible_expense_fraction, 3 * uit, max(0, net_fourth + employment_gross - 7 * uit))
  - domestic_base: max(0, net_fourth + employment_gross - 7 * uit - additional)
  - taxable_base: domestic_base + net_foreign_addition
  - band1: min(taxable_base, 5 * uit) * 0.08
  - band2: min(max(taxable_base - 5 * uit, 0), 15 * uit) * 0.14
  - band3: min(max(taxable_base - 20 * uit, 0), 15 * uit) * 0.17
  - band4: min(max(taxable_base - 35 * uit, 0), 10 * uit) * 0.20
  - band5: max(taxable_base - 45 * uit, 0) * 0.30
  - annual_tax: band1 + band2 + band3 + band4 + band5
expected:
  professional_deduction: 10000.0
  net_fourth: 40000.0
  additional: 0
  domestic_base: 121500.0
  taxable_base: 121500.0
  band1: 2200.00
  band2: 11550.00
  band3: 1955.000
  band4: 0.00
  band5: 0.00
  annual_tax: 15705
```

### 4. High employment income crosses every band

Taxable fifth total PEN 300,000 less PEN 38,500 gives PEN 261,500. Cumulative tax at PEN 247,500 is PEN 38,775 and the PEN 14,000 excess contributes PEN 4,200: total PEN 42,975. Applying 30% to the full base would be wrong.

```oa-check
name: High employment income crosses every band, 2026
inputs:
  professional_gross: 0
  director_gross: 0
  employment_gross: 300000
  eligible_expense_fraction: 0
  net_foreign_addition: 0
  uit: 5500
steps:
  - professional_deduction: min(professional_gross * 0.20, 24 * uit)
  - net_fourth: professional_gross - professional_deduction + director_gross
  - additional: min(eligible_expense_fraction, 3 * uit, max(0, net_fourth + employment_gross - 7 * uit))
  - domestic_base: max(0, net_fourth + employment_gross - 7 * uit - additional)
  - taxable_base: domestic_base + net_foreign_addition
  - band1: min(taxable_base, 5 * uit) * 0.08
  - band2: min(max(taxable_base - 5 * uit, 0), 15 * uit) * 0.14
  - band3: min(max(taxable_base - 20 * uit, 0), 15 * uit) * 0.17
  - band4: min(max(taxable_base - 35 * uit, 0), 10 * uit) * 0.20
  - band5: max(taxable_base - 45 * uit, 0) * 0.30
  - annual_tax: band1 + band2 + band3 + band4 + band5
expected:
  professional_deduction: 0.0
  net_fourth: 0.0
  additional: 0
  domestic_base: 261500.0
  taxable_base: 261500.0
  band1: 2200.00
  band2: 11550.00
  band3: 14025.00
  band4: 11000.00
  band5: 4200.000
  annual_tax: 42975
```

### 5. Evidenced personal rent reduces annual work tax

The worker pays PEN 30,000 qualifying Peru rent, documented with the proper rental receipt/invoice and required payment means, with no duplicate spouse claim. The 30% expense fraction is PEN 9,000, below the PEN 16,500 cap. Final base PEN 42,500 gives PEN 4,300 tax, saving PEN 1,260 against case 2. This is an annual deduction; the employer does not reduce monthly withholding by it.

```oa-check
name: Evidenced personal rent reduces annual work tax, 2026
inputs:
  professional_gross: 0
  director_gross: 0
  employment_gross: 90000
  eligible_expense_fraction: 9000
  net_foreign_addition: 0
  uit: 5500
steps:
  - professional_deduction: min(professional_gross * 0.20, 24 * uit)
  - net_fourth: professional_gross - professional_deduction + director_gross
  - additional: min(eligible_expense_fraction, 3 * uit, max(0, net_fourth + employment_gross - 7 * uit))
  - domestic_base: max(0, net_fourth + employment_gross - 7 * uit - additional)
  - taxable_base: domestic_base + net_foreign_addition
  - band1: min(taxable_base, 5 * uit) * 0.08
  - band2: min(max(taxable_base - 5 * uit, 0), 15 * uit) * 0.14
  - band3: min(max(taxable_base - 20 * uit, 0), 15 * uit) * 0.17
  - band4: min(max(taxable_base - 35 * uit, 0), 10 * uit) * 0.20
  - band5: max(taxable_base - 45 * uit, 0) * 0.30
  - annual_tax: band1 + band2 + band3 + band4 + band5
expected:
  professional_deduction: 0.0
  net_fourth: 0.0
  additional: 9000
  domestic_base: 42500.0
  taxable_base: 42500.0
  band1: 2200.00
  band2: 2100.000
  band3: 0.00
  band4: 0.00
  band5: 0.00
  annual_tax: 4300
```

### 6. Professional income plus director fees

Only professional PEN 40,000 receives the PEN 8,000 deduction. Director fees PEN 20,000 remain gross, making net fourth PEN 52,000. After PEN 38,500, base PEN 13,500 at 8% gives PEN 1,080. Director income also changes which monthly/suspension threshold applies.

```oa-check
name: Professional income plus director fees, 2026
inputs:
  professional_gross: 40000
  director_gross: 20000
  employment_gross: 0
  eligible_expense_fraction: 0
  net_foreign_addition: 0
  uit: 5500
steps:
  - professional_deduction: min(professional_gross * 0.20, 24 * uit)
  - net_fourth: professional_gross - professional_deduction + director_gross
  - additional: min(eligible_expense_fraction, 3 * uit, max(0, net_fourth + employment_gross - 7 * uit))
  - domestic_base: max(0, net_fourth + employment_gross - 7 * uit - additional)
  - taxable_base: domestic_base + net_foreign_addition
  - band1: min(taxable_base, 5 * uit) * 0.08
  - band2: min(max(taxable_base - 5 * uit, 0), 15 * uit) * 0.14
  - band3: min(max(taxable_base - 20 * uit, 0), 15 * uit) * 0.17
  - band4: min(max(taxable_base - 35 * uit, 0), 10 * uit) * 0.20
  - band5: max(taxable_base - 45 * uit, 0) * 0.30
  - annual_tax: band1 + band2 + band3 + band4 + band5
expected:
  professional_deduction: 8000.0
  net_fourth: 52000.0
  additional: 0
  domestic_base: 13500.0
  taxable_base: 13500.0
  band1: 1080.000
  band2: 0.00
  band3: 0.00
  band4: 0.00
  band5: 0.00
  annual_tax: 1080
```

### 7. Foreign addition cannot absorb unused work allowances

Professional PEN 20,000 less PEN 4,000 leaves domestic net fourth PEN 16,000. The work allowance reduces that domestic base to zero, not below. Verified relevant net foreign income PEN 30,000 is then added: tax PEN 2,200 + PEN 350 = PEN 2,550 before a separately established foreign credit. Adding foreign income before the 7-UIT deduction would wrongly shelter it.

```oa-check
name: Foreign addition cannot absorb unused work allowances, 2026
inputs:
  professional_gross: 20000
  director_gross: 0
  employment_gross: 0
  eligible_expense_fraction: 0
  net_foreign_addition: 30000
  uit: 5500
steps:
  - professional_deduction: min(professional_gross * 0.20, 24 * uit)
  - net_fourth: professional_gross - professional_deduction + director_gross
  - additional: min(eligible_expense_fraction, 3 * uit, max(0, net_fourth + employment_gross - 7 * uit))
  - domestic_base: max(0, net_fourth + employment_gross - 7 * uit - additional)
  - taxable_base: domestic_base + net_foreign_addition
  - band1: min(taxable_base, 5 * uit) * 0.08
  - band2: min(max(taxable_base - 5 * uit, 0), 15 * uit) * 0.14
  - band3: min(max(taxable_base - 20 * uit, 0), 15 * uit) * 0.17
  - band4: min(max(taxable_base - 35 * uit, 0), 10 * uit) * 0.20
  - band5: max(taxable_base - 45 * uit, 0) * 0.30
  - annual_tax: band1 + band2 + band3 + band4 + band5
expected:
  professional_deduction: 4000.0
  net_fourth: 16000.0
  additional: 0
  domestic_base: 0
  taxable_base: 30000
  band1: 2200.00
  band2: 350.00
  band3: 0.00
  band4: 0.00
  band5: 0.00
  annual_tax: 2550
```

### 8. Professional deduction reaches its 24-UIT ceiling

At professional gross PEN 1,000,000, 20% would be PEN 200,000 but the deduction is capped at PEN 132,000. Net fourth is PEN 868,000 and, after PEN 38,500, taxable base PEN 829,500. Tax is PEN 38,775 plus 30% of PEN 582,000 = PEN 213,375 before credits. Do not cap gross receipts at 24 UIT or deduct a flat 24 UIT from every small professional.

```oa-check
name: Professional deduction reaches its 24-UIT ceiling, 2026
inputs:
  professional_gross: 1000000
  director_gross: 0
  employment_gross: 0
  eligible_expense_fraction: 0
  net_foreign_addition: 0
  uit: 5500
steps:
  - professional_deduction: min(professional_gross * 0.20, 24 * uit)
  - net_fourth: professional_gross - professional_deduction + director_gross
  - additional: min(eligible_expense_fraction, 3 * uit, max(0, net_fourth + employment_gross - 7 * uit))
  - domestic_base: max(0, net_fourth + employment_gross - 7 * uit - additional)
  - taxable_base: domestic_base + net_foreign_addition
  - band1: min(taxable_base, 5 * uit) * 0.08
  - band2: min(max(taxable_base - 5 * uit, 0), 15 * uit) * 0.14
  - band3: min(max(taxable_base - 20 * uit, 0), 15 * uit) * 0.17
  - band4: min(max(taxable_base - 35 * uit, 0), 10 * uit) * 0.20
  - band5: max(taxable_base - 45 * uit, 0) * 0.30
  - annual_tax: band1 + band2 + band3 + band4 + band5
expected:
  professional_deduction: 132000
  net_fourth: 868000
  additional: 0
  domestic_base: 829500
  taxable_base: 829500
  band1: 2200.00
  band2: 11550.00
  band3: 14025.00
  band4: 11000.00
  band5: 174600.00
  annual_tax: 213375
```

### 9. Monthly fourth-category payment despite a small unretained receipt

No suspension applies. Professional receipts paid in a month total PEN 7,000: PEN 6,000 paid by an agent with PEN 480 retention, plus PEN 1,000 with no retention. The ordinary monthly threshold is exceeded. Eight percent of the whole PEN 7,000 is PEN 560; less PEN 480 retention leaves PEN 80 monthly payment. Do not exempt the smaller receipt from the monthly base or tax only the threshold excess. The annual liability is computed separately.

```oa-check
name: Monthly fourth-category payment after retentions
inputs:
  retained_receipt_gross: 6000
  small_receipt_gross: 1000
  rate: 0.08
steps:
  - total_gross: retained_receipt_gross + small_receipt_gross
  - retention: retained_receipt_gross * rate
  - gross_advance: total_gross * rate
  - remaining_advance: max(0, gross_advance - retention)
expected:
  total_gross: 7000
  retention: 480
  gross_advance: 560
  remaining_advance: 80
```

### 10. Non-domiciled employment is a routing decision

Confirmed non-domiciled taxpayer with Peru-source employment: stop the resident computation and use LIR art. 54(g)/76, source and any applicable treaty analysis. Do not grant the resident 20%, 7-UIT or additional-work deductions. This routing result is not a blanket 30% rule for every kind of income.


## Ask the client first

1. **Year and domicile:** 2026 income or a 2025 return filed in 2026? Travel, residence evidence and effective status dates? Stop resident-tax computation if these are unresolved.
2. **Income categories and actual duties:** fourth professional versus director/similar; fifth employment from all employers; business, capital, pensions/CTS or foreign items? Contracts and source facts decide. Do not choose a supposedly conservative category without evidence.
3. **Gross and timing:** RHE and payment dates, credit notes, boletas, ordinary/extraordinary gratificaciones, profit shares, benefits in kind and statutory exclusions? Reconcile gross to net bank and retention separately.
4. **Deductions:** each paid qualifying expense, document with correct claimant identification, supplier status, payment means, relationship/insurance/CONADIS and any spouse attribution? Calculate fractions before the 3-UIT cap. Unknown deductions stay unclaimed pending evidence, not falsely certified as ineligible.
5. **Monthly tax:** fourth/fifth retentions and payments, accepted FV 616s, FV 1609 constancia and effective/restart dates, all employer certificates/reports and prior credits? A suspension does not erase annual liability.
6. **Foreign and other claims:** source, currency conversion, foreign tax and credit ceiling; ITF/donations with full evidence; any capital/business income needing a separate computation?
7. **Filing and settlement:** RUC last digit/population, correct year resolution and extensions, prior return, notices/debt/instalments, payment/refund preference and authorised reviewer?

If documents arrive before answers, build a **provisional** evidence schedule and list missing facts. Compute only the branches supported by facts, clearly distinguishing assumptions from confirmed information. Present the unresolved questions and working for approval. Do not file, pay, post, change an election, submit a refund or contact an authority merely because the working balances. Recompute each band with decimal arithmetic or a tested supported engine; do not claim that an unavailable calculation engine has validated it.

The skill and its outputs are informational and computational material and do not constitute tax, legal or financial advice. Open Accountants and its contributors accept no liability for errors, omissions or outcomes arising from use. Outputs require qualified professional review before filing or acting.

## Sources

| Source and portions actually read | URL | Read on |
|---|---|---|
| LIR Chapter II; arts. 6-10 domicile, effective dates and source | https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf | 2026-11-11 |
| LIR Chapter IV; art. 18 labour indemnities, CTS, pensions and specified subsidies; not every capital exemption reviewed | https://www.sunat.gob.pe/legislacion/renta/ley/capiv.pdf | 2026-11-11 |
| LIR Chapter V; arts. 28, 33-34 business/work classification and employment overrides | https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf | 2026-11-11 |
| LIR Chapter VI; arts. 35-36 capital separation, 45-46 work deductions, 49 ITF/donations and 51-51-A foreign netting | https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf | 2026-11-11 |
| LIR Chapter VII; arts. 52-A, 53 and 54(g), capital versus resident-work scale and non-resident employment | https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf | 2026-11-11 |
| LIR Chapter VIII; art. 57 current calendar/perception provisions and dated amendment notes | https://www.sunat.gob.pe/legislacion/renta/ley/capviii.pdf | 2026-11-11 |
| LIR Chapter X; arts. 71, 74-76, retention agents and fourth/fifth/non-resident tax | https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf | 2026-11-11 |
| LIR Chapter XI; arts. 79 and 86-88, fifth-only exceptions, monthly payment and credits | https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf | 2026-11-11 |
| Regulation Chapter II; art. 4 domicile timing and evidence | https://www.sunat.gob.pe/legislacion/renta/regla/cap2.pdf | 2026-11-11 |
| Regulation Chapter VI; arts. 26, 26-A and 28-B, domestic deduction capacity, expense/payment exceptions and ITF allocation; art. 21(s) donation cross-reference consulted, full special donation computation not reproduced | https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf | 2026-11-11 |
| Regulation Chapter X; arts. 40-44, ordinary/extraordinary monthly retention, employer changes and final adjustment | https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf | 2026-11-11 |
| Regulation Chapter XI; art. 58 foreign-credit conditions consulted with art. 88 | https://www.sunat.gob.pe/legislacion/renta/regla/cap11.pdf | 2026-11-11 |
| SUNAT UIT table; 2026 and historical 2025 rows | https://www.sunat.gob.pe/indicestasas/uit.html | 2026-11-11 |
| RS 390-2025; all operative arts. 1-4 and commencement for 2026 exception/suspension amounts | https://www.sunat.gob.pe/legislacion/superin/2025/000390-2025.pdf | 2026-11-11 |
| RS 013-2007 consolidated HTML; arts. 2-11/reference-period provisions; historical monetary/form-version text distinguished from 2026 amounts | https://www.sunat.gob.pe/legislacion/superin/2007/013.htm | 2026-11-11 |
| DS 377-2014-EF; preamble, art. 1 replacing DS 215-2006 art. 5.1(b.2.1) with 8% and commencement, official PDF read from direct-download text after web fetch returned 403 | https://cdn.www.gob.pe/uploads/document/file/252637/227659_file20181218-16260-1we2y1a.pdf | 2026-11-11 |
| RS 002-2015; scanned page 3 sole modifying provision visually read, replacing RS 013 art. 3.2(c) with 8%; historic annual amounts not used | https://www.sunat.gob.pe/legislacion/superin/2015/002-2015.pdf | 2026-11-11 |
| SUNAT Informe 090-2015; pp. 1-5, especially pp. 2-3 first/second-half coverage and average/reference-period definition; 2015 amounts not used | https://www.sunat.gob.pe/legislacion/oficios/2015/informe-oficios/i090-2015.pdf | 2026-11-11 |
| Law 28194 consolidated text with DL 1529; arts. 3-8 payment thresholds, means and tax effects | https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf | 2026-11-11 |
| SUNAT 2026 deductible expenses; percentages, personal/supplier/document conditions, means of payment and access | https://personas.sunat.gob.pe/devoluciones/gastos-deducibles-para-ano-2026 | 2026-11-11 |
| SUNAT independent declaration/payment; current 2026 thresholds, FV 616 path/fields, NPS and monthly/annual/refund distinctions | https://personas.sunat.gob.pe/trabajador-independiente/declaracion-pago | 2026-11-11 |
| SUNAT suspension guidance; current 2026 limits, FV 1609 and approval timing | https://personas.sunat.gob.pe/trabajador-independiente/suspension-retenciones | 2026-11-11 |
| SUNAT dependent declaration/payment; employer aggregation, withholding table, no monthly 3-UIT deduction and payment route. Embedded 2024 UIT examples not reused | https://personas.sunat.gob.pe/trabajador-dependiente/declaracion-pago | 2026-11-11 |
| SUNAT annual FV 709 procedure; explicitly 2025 campaign, personalised-data review and App Personas. Not proof of released 2026 form | https://renta.sunat.gob.pe/personas/como-realizar-la-declaracion-del-impuesto-la-renta | 2026-11-11 |
| SUNAT illustrated FV 709 refund procedure; first SOL/menu/exercise steps read as 2025 procedural reference | https://renta.sunat.gob.pe/sites/default/files/inline-files/Pasos%20devolucion%20FV%20709.pdf | 2026-11-11 |
| SUNAT 2025 annual schedule; historical destination only for retired May-June 2026 table, not 2026 tax-year dates | https://renta.sunat.gob.pe/personas/cronograma-de-declaracion-renta-anual-2025-formulario-ndeg-709 | 2026-11-11 |
| Tax Code through 26 June 2026; arts. 33, 36, 166 and 176-180, table/population distinction | https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf | 2026-11-11 |

Not yet confirmed: exact RUC-specific 2027 annual dates/extensions for 2026; released 2026 FV 709 numbered fields, annexes, live submission/payment/refund screens and all year-specific filing populations; current FV 616 numbered fields; numeric TIM, personal-table fine amounts and case-specific relief; transaction-specific currency conversion and treaty/foreign-credit entitlement. Figures are omitted pending those checks. Rental/capital/business returns, full donation/ITF exception cases and non-resident computations require separate primary-source workings outside this work-income method.
