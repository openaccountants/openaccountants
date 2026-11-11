---
name: pe-corporate-income-tax
description: >
  Prepare Peru business income tax for tax year 2026 before completing a
  monthly payment or annual corporate return. Covers domiciled companies,
  Peru permanent establishments, the General Regime, MYPE Tributario entry
  and graduated tax, the Special Income Regime screen, accounting-to-tax
  reconciliation, deductions, loss elections, monthly advances, annual credits
  and SUNAT filing evidence. Identifies the new agrarian-law conditions without
  treating every agricultural company as an ordinary MYPE. Use for Peru
  corporate income tax, renta de tercera categoria, Regimen General, RMT,
  RER, pagos a cuenta, coeficiente, Formulario 710 and Declara Facil 621.
  Produces a sourced computation, regime decision, return checklist and
  proposed payment for human approval; specialist sector returns remain separate.
jurisdiction: PE
category: international
tax_year: 2026
last_updated: 2026-11-11
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: computation
version: 0.1
---

# Peru corporate income tax, tax year 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Built from the law. Not yet approved.** Prepare the computation and proposed filings. Do not submit, pay, change an election or post journals without approval.

**Quick reference.** General Regime annual income tax applies to taxable profit. RMT has a revenue eligibility gate and a separate profit-band computation. RER is a final monthly turnover charge for qualifying businesses. General/RMT monthly payments are advances against annual liability; a coefficient is not the annual rate. Obtain entity, regime history, revenue, adjustments and loss election first. This file covers **1 January to 31 December 2026**. Exact 2027 annual dates and released 2026 annual-form fields were not confirmed.

## Who this applies to

Peru-incorporated legal persons generally pay on worldwide taxable income. Specified Peru branches, agencies and PEs of foreign enterprises pay on Peru-source income. Foreign enterprises without a Peru PE need source/withholding analysis, not automatic taxation of worldwide profit at the resident rate. [LIR arts. 6-7](https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf), [arts. 14 and 14-B](https://www.sunat.gob.pe/legislacion/renta/ley/capiii.pdf).

Test the regime in this order:

1. **Special rules first.** Screen agrarian, Amazonian, aquaculture, forestry, financial-sector, exemption and stability-agreement rules. LIR art. 55 identifies separate sector statutes. A business description or SME status alone does not establish eligibility. [LIR art. 55](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf).
2. **RER.** Meet every income, purchases, asset, staffing and activity condition. Construction, specified transport, professional/consulting and other listed activities are excluded; foreign-source income also excludes entry. Apply the complete art. 118 activity list, not turnover alone. [LIR arts. 117-118](https://www.sunat.gob.pe/legislacion/renta/ley/capxv.pdf).
3. **RMT.** Eligible domiciled art. 14 taxpayers must meet the annual net-income limit. Exclusions include capital-linked persons whose combined annual income exceeds the limit, Peru PEs of foreign enterprises, and taxpayers exceeding the preceding-year limit. RMT's capital linkage uses Regulation art. 24(1), (2) and (4), plus the specified spousal ownership in (1)/(2), under DS 403-2016-EF art. 3; do not import every broader TP relationship. Aggregate prior-regime amounts as DL 1269 art. 3(c) requires. The income definition includes the specified foreign-source income. [DL 1269 arts. 1-3](https://www.sunat.gob.pe/legislacion/mypeIR/dl1269.pdf), [DS 403-2016-EF art. 3](https://www.sunat.gob.pe/legislacion/mypeIR/r-dl1269.pdf).
4. **General Regime.** Apply when no valid alternative applies. Exceeding RMT's annual limit or incurring its specified capital-link/foreign-PE exclusion during the year makes General annual taxation apply for the **whole year, excluding months previously in RER or Nuevo RUS**. Previous RMT advances retain their credit character; RER/Nuevo RUS periods are not retrospectively converted into General months. [DL 1269 art. 9](https://www.sunat.gob.pe/legislacion/mypeIR/dl1269.pdf), [DS 403-2016-EF art. 5.1](https://www.sunat.gob.pe/legislacion/mypeIR/r-dl1269.pdf).

New-business RMT entry is through the timely declaration for the RUC activity-start month. General-to-RMT entry is January of the next qualifying year. RER-to-RMT/General can occur during the year; General/RMT-to-RER is January-only and loses loss carryforwards. RER entry requires both declaration **and payment** of the relevant initial-activity or eligible switching month's quota by its due date under art. 119. The lowest example tax does not permit retrospective switching. [DL 1269 arts. 7-9](https://www.sunat.gob.pe/legislacion/mypeIR/dl1269.pdf), [LIR arts. 119-122](https://www.sunat.gob.pe/legislacion/renta/ley/capxv.pdf).

## Rates, bands and thresholds

Figures are for **2026**, except the explicitly identified coefficient years. PEN means soles. Revenue ceilings and taxable-profit bands are different populations.

| Item and conditions | Figure or boundary | Official source and short original-language extract |
|---|---|---|
| 2026 UIT | PEN 5,500 | [SUNAT UIT table, DS 301-2025-EF](https://www.sunat.gob.pe/indicestasas/uit.html): `2026 ... 5,500` |
| General annual net taxable business income | 29.5% | [LIR art. 55](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `veintinueve coma cincuenta por ciento` |
| RMT own annual net-income ceiling, subject to exclusions | Not above 1,700 UIT, or PEN 9,350,000; preceding-year and capital-linked combined-income tests remain | [DL 1269 arts. 1 and 3](https://www.sunat.gob.pe/legislacion/mypeIR/dl1269.pdf): `no superen las 1700 UIT` |
| RMT annual taxable profit | 10% on first 15 UIT, or PEN 82,500; 29.5% on excess | [DL 1269 art. 5](https://www.sunat.gob.pe/legislacion/mypeIR/dl1269.pdf): `Hasta 15 UIT ... 10%`; `Más de 15 UIT ... 29,50%` |
| RMT monthly advance while annual net income has not exceeded 300 UIT | 1% of monthly net income; gate PEN 1,650,000. From the month the gate is exceeded, use art. 85 | [DL 1269 art. 6](https://www.sunat.gob.pe/legislacion/mypeIR/dl1269.pdf): `no superen las 300 UIT`; `uno por ciento (1,0%)` |
| General ordinary monthly advance, unless valid modification/suspension applies | Greater of coefficient times monthly net income and 1.5% of that income; no prior calculated tax means percentage route | [LIR art. 85](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf): `monto que resulte mayor`; `uno coma cinco por ciento (1,5%)` |
| Coefficient year and precision | January-February: 2024 tax/net income; March-December: 2025. Round the coefficient to four decimals | [LIR art. 85(a)](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf), [Regulation art. 54(b)](https://www.sunat.gob.pe/legislacion/renta/regla/cap11.pdf): `cuatro (4) decimales` |
| RER annual income and purchases | Each not above PEN 525,000; purchases exclude fixed assets. Other gates remain | [LIR art. 118(a)(i), (iii)](https://www.sunat.gob.pe/legislacion/renta/ley/capxv.pdf): `525,000.00` |
| RER assets/staff | Activity fixed assets not above PEN 126,000 excluding land/buildings and vehicles; no more than 10 staff per shift | [LIR art. 118(a)(ii), (iv)](https://www.sunat.gob.pe/legislacion/renta/ley/capxv.pdf): `126,000.00`; `mayor a 10` |
| RER final monthly income tax | 1.5% of monthly net third-category income; a year wholly in RER has no General/RMT annual true-up | [LIR art. 120](https://www.sunat.gob.pe/legislacion/renta/ley/capxv.pdf): `1.5%`; `carácter cancelatorio` |
| Ordinary domestic business loss: system A | Four immediately following years, then expiry; the special 2020 five-year window does not extend ordinary 2026 losses | [LIR art. 50(a)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf): `cuatro (4) ejercicios inmediatos posteriores` |
| Ordinary domestic business loss: system B | Offset up to 50% of each later year's qualifying domestic net business income until used | [LIR art. 50(b)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf): `cincuenta por ciento (50%)` |
| Net-interest cap where no statutory exclusion applies | 30% of preceding-year tax EBITDA; excess has four-following-year window | [LIR art. 37(a)(1)-(2)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf): `treinta por ciento (30%) del EBITDA`; `cuatro (4) ejercicios` |
| Income exclusion from that cap | Current-year net income not above 2,500 UIT, or PEN 13,750,000; ordinary causality/other interest conditions still apply | [LIR art. 37(a)(2)(b)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf): `menores o iguales a ... (2500) UIT` |
| Qualifying agrarian enterprises under new Law 32434 | 15% on net income for 2026-2035; General rate from 2036. Apply arts. 3-4 and exclusions | [Law 32434 art. 12.1, official Gazette PDF table](https://busquedas.elperuano.pe/api/archivo/file/7oiMed6E4bc8gpK300ViG3/*/2437329-1.PDF): `2026 - 2035 ... 15%` |
| Table I late determinative declaration, before relief | 1 UIT, using legally applicable UIT rather than automatically the return year's value | [Tax Code art. 176(1), Table I and art. 180(a)](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf): `Numeral 1 ... 1 UIT` |
| Ordinary Table I understatement, before relief | 50% of tax payable omitted; improper refunds have separate 100% basis. Note 21 defines difference; general minimum 5% UIT | [Tax Code art. 178(1), Table I/general notes/note 21](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf): `50% del tributo por pagar omitido` |

## The base

### Accounts-to-tax computation

1. **Close the calendar year.** Third-category income generally accrues under art. 57's goods, services and contingent-consideration rules. Cash, invoice and accounting dates do not invariably establish tax accrual. Identify income outside charge/exempt under its verified provision. [LIR art. 57](https://www.sunat.gob.pe/legislacion/renta/ley/capviii.pdf).
2. **Reconcile sales and cost.** Art. 20 deducts supported tax cost from net disposal income after ordinary returns/discounts. Check supplier status and statutory documentary exceptions. Separate inventory cost from overheads; a capital purchase is not automatically a current expense. [LIR art. 20](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [arts. 37 and 44(e)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf).
3. **Test expenses.** Art. 37 starts with necessity to generate taxable income or maintain its source, subject to specific limits, timing, evidence and art. 44 prohibitions. Add back private/family costs, Peru income tax, public-sector fines/Tax Code late interest, unsupported provisions, non-qualifying donations and disallowed vouchers as applicable. Check each specific exception rather than disallowing every donation/provision. [LIR arts. 37 and 44(a)-(j)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf).
4. **Replace book depreciation with allowable tax depreciation.** Establish asset, tax cost, in-use period, accounting recognition, statutory/regulatory rate and any accelerated regime. Keep a tax asset and temporary-difference schedule; no universal asset rate is supplied. [LIR arts. 38-43](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf).
5. **Check interest and related parties.** Tax EBITDA is net income after loss offset plus net interest, depreciation and amortisation, not necessarily book EBITDA. Test all art. 37(a)(2) exclusions, not only the table's income gate. New businesses have the specified current-year EBITDA rule. Track restricted-interest vintages/expiry; causality and exempt-interest restrictions remain. Related-party pricing/service deductions also need [peru-transfer-pricing](peru-transfer-pricing.md). [LIR art. 37(a)](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [art. 32-A](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf).
6. **Apply losses.** Track eligible domestic losses by origin/year and elected system. Elect in the annual return; omission defaults to A. Changing systems is restricted until accumulated losses are exhausted. Exempt income and non-hedging derivatives have special rules. A 2020 system-A balance does not gain a fresh four-year life in 2026. [LIR art. 50](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf).
7. **Integrate foreign income correctly.** Apply art. 51 netting/excluded-loss rules and art. 51-A evidence. No overall foreign net loss offsets domestic income. Qualifying foreign credits require art. 88's direct/indirect-credit conditions; [peru-cross-border-tax](peru-cross-border-tax.md) owns that method and non-resident withholding conditions. [LIR arts. 51-51-A](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), [art. 88(e)-(f)](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf).
8. **Compute then settle.** Apply the verified annual General/RMT rates to taxable profit, then reconcile allowable credits, advances and prior balances. Distinguish non-refundable foreign credits from credits supporting a refund/balance. Record annual liability separately from residual payment and reconcile to SUNAT/ledger records. [LIR art. 55](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), [art. 88](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf).

**Indirect profit dispositions.** Legal persons separately test art. 24-A(g) and art. 55's additional tax on an indirect disposition not susceptible to subsequent tax control. An expense add-back does not automatically establish that condition. Classify the disposition and timing rather than imposing or ignoring the extra charge on every adjustment. [LIR art. 24-A](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [art. 55](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf).

### Agrarian scope changed for 2026

Law 32434's income-tax provisions start **1 January 2026**. Its qualifying enterprise rate replaces this file's unsupported generic rising Law 31110 schedule. Check enterprise definition, activity, location and excluded products. Principal activity generally requires other activities' net income not above **20%** of total annual net income. Agroindustry has the outside-Lima-Metropolitana/Callao and excluded-product conditions. Beneficiaries cannot also use RMT or the other expressly excluded benefits. Special small-producer taxation, additional purchase deductions, irrigation/hydraulic depreciation, stability agreements and sector-specific advances need a sector working rather than the ordinary examples below. [Law 32434 arts. 3-4, 11-14, first/twelfth final provisions](https://busquedas.elperuano.pe/dispositivo/EX/2437329-1), [DS 015-2026-EF arts. 3-12](https://cdn.www.gob.pe/uploads/document/file/9437490/7730417-decreto-supremo-n-015-2026-ef.pdf?v=1770915573).

Full agrarian and other special-sector computations, ITAN, investment/stability benefits, reorganisations, construction-contract methods, financial-sector calculations and full foreign-credit computations are out of scope for this ordinary corporate method. They need their own law and working, rather than being assumed zero.

## Deadlines and filing

### Monthly declarations and payments

For General advances, compute both amounts in the table unless a valid art. 85/Regulation art. 54 modification or suspension applies. A current loss alone does not permit zero advances. RMT's 1% route ends from the month its cumulative gate is exceeded. RER's monthly income tax is final rather than a credit awaiting an annual profit return. [LIR art. 85](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf), [art. 120](https://www.sunat.gob.pe/legislacion/renta/ley/capxv.pdf), [DL 1269 art. 6](https://www.sunat.gob.pe/legislacion/mypeIR/dl1269.pdf), [Regulation art. 54](https://www.sunat.gob.pe/legislacion/renta/regla/cap11.pdf).

SUNAT identifies **Declara Facil 621 - IGV-Renta mensual** for ordinary monthly business declarations. Use the actual monthly RUC/category schedule and any extension, not a universal due day. [SUNAT monthly guidance](https://orientacion.sunat.gob.pe/declaracion-y-pago-mensual-1).

1. Reconcile period/cumulative revenue, sales/purchases records, regime history, coefficient working and credits.
2. Enter **SUNAT Operaciones en Linea** with authorised SOL credentials, then **Mis declaraciones y pagos**. Select **Declara Facil 621** and period.
3. Verify personalised data/regime, complete net income, coefficient/percentage and credit fields, and reconcile the income-tax result. IGV is a separate calculation handled by [peru-igv](peru-igv.md). Current numbered fields were not confirmed; do not copy an old screenshot's boxes.
4. Obtain approval and submit. RS 335-2017 art. 7 permits enabled affiliated bank-account debit, enabled affiliated payment cards and NPS payment through authorised banks where applicable. Follow current service options. Do not apply imported-service/purchase-liquidation IGV payment restrictions as a new ordinary income-tax method.
5. Save the **constancia de presentacion** and separate payment receipt/NPS reconciliation. Art. 8's specified bank/card/system/NPS rejection means non-filing. Attempted upload is not filing; a declaration is not proof of payment.
6. For replacement/correction, select original period and correct declaration type in the supported service. Preserve receipts and explain changes. Apply Tax Code art. 88 before assuming a tax-reducing correction is immediately effective.

Sequence, payment and receipt source: [RS 335-2017 arts. 6-10](https://www.sunat.gob.pe/legislacion/superin/2017/335-2017.pdf), read with [RS 047-2026's final payment-method amendment](https://www.sunat.gob.pe/legislacion/superin/2026/000047-2026.pdf) for the distinct IGV exclusions.

### Annual return and balance

LIR art. 79 establishes annual declaration and balance payment. SUNAT has a general schedule and qualifying extended MYPE population. The **2025 return campaign filed in 2026 is not the 2026 return schedule**. Exact 2027 dates were not confirmed. Obtain the current annual resolution and correct population before filing; do not carry over the old approximate May-June 2026 window. [LIR art. 79](https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf), [SUNAT annual page, explicitly Renta 2025](https://renta.sunat.gob.pe/empresas/como-realizar-la-declaracion-del-impuesto-la-renta).

The published procedure uses **Formulario Virtual 710**, simplified or complete for the prescribed population. The readable **2025 campaign** page lists complete-form triggers, including higher income, benefits/stability, TP-report duties, trial balance, financial-sector and listed transactions. Treat it as a prior-campaign procedural reference. Confirm the released **2026** form/version, triggers, numbered fields and annexes when available; this file does not claim to have checked an unreleased form. [SUNAT 710 instructions](https://renta.sunat.gob.pe/empresas/como-realizar-la-declaracion-del-impuesto-la-renta).

Prepare financial statements, tax reconciliation, asset/loss schedules and credits/payments first. In SOL select the actual annual 710 version and **2026** exercise; complete identification, financial, reconciliation, tax and credit information against approved workings and the current official field mapping. Check trial-balance/transaction annexes. Obtain sign-off, submit, retain accepted declaration, arrange residual payment through the current authorised route, and reconcile both receipts. Missing year-specific form details are a filing dependency, not permission to use a 2025 form.

## Penalties and interest

Classify late determinative filing under art. 176(1), understatement under art. 178(1) and unremitted retentions under art. 178(4) separately. The table gives ordinary **Table I** starting sanctions before relief. For understatement, note 21 includes prior balances, eligible losses, advances, other credits and offsets in tax payable omitted; it is not automatically omitted revenue times the corporate rate. Art. 180(a) uses UIT at commission, or detection where commission date cannot be established. A 2026 return filed late in 2027 does not automatically use 2026 UIT. [Tax Code arts. 176, 178, 180, Table I and note 21](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf).

Current graduality/discretion, correction, notification and payment stage affect payable fines; no universal discount is asserted. Art. 33 charges daily interest from the day after tax due date through payment inclusive, using monthly TIM divided by **30** and statutory suspension rules. Use actual rate periods. Numeric current TIM and fact-specific relief were not independently confirmed. [Tax Code arts. 33 and 166](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf).

## Cross-border points

Separate the company's own tax, shareholder dividend tax and payer withholding. Ordinary Peru-company dividends to another domiciled legal person fall outside art. 73-A's general withholding; resident-individual/non-resident distributions require the distribution-year/profit-vintage conditions. Non-resident dividend, interest, royalty and technical-assistance rates/conditions are owned by [peru-cross-border-tax](peru-cross-border-tax.md), including qualified external-credit interest, the technical-assistance audit-report gate, treaty eligibility and source. [LIR arts. 54 and 56](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), [art. 73-A](https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf).

The external-credit condition retained from the previous version is a ceiling of the preferential prevailing rate in the originating market **plus three percentage points**. Those three points cover fees, commissions, premiums and every other addition to the agreed interest. This confirms the statutory margin, not the current loan-specific reference rate; the other cash-inflow, connection and statutory conditions still apply. [LIR art. 56(a)(2), (j)](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `más tres (3) puntos`; `cubren los gastos y comisiones, primas`.

Related-party and specified low-tax/preferential-regime dealings need [peru-transfer-pricing](peru-transfer-pricing.md)'s valuation and service-deduction evidence even below reporting thresholds. A pricing adjustment does not alone prove a withholding event or dividend distribution. [LIR art. 32-A](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf).

## Two worked examples that recompute

### 1. General Regime annual reconciliation and remaining payment

An ordinary domiciled General company has **PEN 250,000** accounting profit before tax, including **PEN 10,000** private expenses and **PEN 5,000** public-sector fines, non-deductible under art. 44. Its documented eligible **PEN 40,000** domestic system-A loss remains in time. Assume no other adjustment, foreign income or special regime. Taxable profit is PEN 225,000 and annual tax PEN 66,375. Substantiated creditable advances **PEN 50,000** leave PEN 16,375 payable. Assume the expenses do not separately qualify as indirect profit dispositions; that classification must be investigated rather than automatically applying/ignoring the extra charge.

```oa-check
name: General Regime 2026 reconciliation and balance
inputs:
  accounting_profit: 250000
  private_expenses: 10000
  public_fines: 5000
  eligible_loss: 40000
  rate: 0.295
  advances: 50000
steps:
  - before_loss: accounting_profit + private_expenses + public_fines
  - taxable_profit: before_loss - eligible_loss
  - annual_tax: taxable_profit * rate
  - balance: annual_tax - advances
expected:
  before_loss: 265000
  taxable_profit: 225000
  annual_tax: 66375
  balance: 16375
```

### 2. RMT eligibility changes the annual result

A Peru-incorporated company has **PEN 200,000** final taxable profit and current/prior annual net income of **PEN 2,000,000**, with no disqualifying capital-linked group, foreign PE or special regime, and timely valid RMT entry for the whole year. It has no RER or Nuevo RUS months. The first PEN 82,500 profit at 10% and remaining PEN 117,500 at 29.5% produce **PEN 42,912.50**. General tax on the same profit is **PEN 59,000**, a **PEN 16,087.50** difference before credits. If it instead breaches the own/group income gate or a relevant exclusion, the whole-year General result applies under art. 9, with the preceding RER/Nuevo RUS-month exception where such periods exist. Small profit alone does not establish RMT eligibility.

```oa-check
name: RMT versus General, same profit with eligibility decision
inputs:
  uit: 5500
  profit: 200000
  annual_net_income: 2000000
  gate_uit: 1700
  band_uit: 15
  first_rate: 0.10
  excess_rate: 0.295
steps:
  - income_ceiling: gate_uit * uit
  - income_headroom: income_ceiling - annual_net_income
  - first_band: band_uit * uit
  - first_tax: min(profit, first_band) * first_rate
  - excess_tax: max(0, profit - first_band) * excess_rate
  - rmt_tax: first_tax + excess_tax
  - general_tax: profit * excess_rate
  - difference: general_tax - rmt_tax
expected:
  income_ceiling: 9350000
  income_headroom: 7350000
  first_band: 82500
  first_tax: 8250
  excess_tax: 34662.50
  rmt_tax: 42912.50
  general_tax: 59000
  difference: 16087.50
```

For a separate monthly General illustration without modification/suspension, **PEN 100,000** monthly net income and a correctly rounded **0.0300** coefficient give PEN 3,000 versus PEN 1,500 under the percentage: advance PEN 3,000. A **0.0100** coefficient instead gives PEN 1,500 as the greater amount. These are assumed lawful coefficient inputs; retain the actual prior-year working.

```oa-check
name: Ordinary General monthly advance, both comparison outcomes
inputs:
  monthly_net_income: 100000
  high_coefficient: 0.0300
  low_coefficient: 0.0100
  percentage: 0.015
steps:
  - percentage_amount: monthly_net_income * percentage
  - high_advance: max(monthly_net_income * high_coefficient, percentage_amount)
  - low_advance: max(monthly_net_income * low_coefficient, percentage_amount)
expected:
  percentage_amount: 1500
  high_advance: 3000
  low_advance: 1500
```

## Ask the client first

1. Entity/residence/PE, activity, location, sector/stability benefits and full RUC regime/election history.
2. Current/prior-year revenue by regime, foreign income, capital-linked persons' revenue, RER purchases/assets/staff and activity exclusions.
3. Trial balance, revenue/cost cut-off, expense evidence, tax assets, restricted interest and reconciliation adjustments.
4. Losses by origin/year, elected system and previous use, including any 2020/derivative restrictions.
5. Coefficient-year calculated tax/net income, monthly declarations/payments, balances and foreign-credit evidence.
6. RUC schedule category, accepted receipts, notices/audits, corrections, profit-vintage/dividend and cross-border contracts.

## Sources

| Source and portions read | URL | Read on |
|---|---|---|
| LIR Chapter II; arts. 6-7, worldwide and PE/source-only scope | https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf | 2026-11-11 |
| LIR Chapter III; arts. 14 and 14-B, entities/PE population | https://www.sunat.gob.pe/legislacion/renta/ley/capiii.pdf | 2026-11-11 |
| LIR Chapter V; art. 20 cost/documentary rules and art. 32-A pricing/service provisions | https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf | 2026-11-11 |
| LIR Chapter VI; art. 37 opening/interest, arts. 38-44 assets/prohibitions and arts. 50-51-A losses/foreign income | https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf | 2026-11-11 |
| LIR Chapter VII; current arts. 55-56 corporate rate, disposition charge and non-resident conditions | https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf | 2026-11-11 |
| LIR Chapter VIII; art. 57 calendar/accrual and current amendment notes | https://www.sunat.gob.pe/legislacion/renta/ley/capviii.pdf | 2026-11-11 |
| LIR Chapter X; art. 73-A dividend scope/timing | https://www.sunat.gob.pe/legislacion/renta/ley/capx.pdf | 2026-11-11 |
| LIR Chapter XI; arts. 79, 85 and 88 annual duty, advances and credits | https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf | 2026-11-11 |
| LIR Chapter XV; arts. 117-122 RER gates/exclusions, final charge and regime changes | https://www.sunat.gob.pe/legislacion/renta/ley/capxv.pdf | 2026-11-11 |
| DL 1269; arts. 1-9 RMT definition/exclusions, rates, advances, entry and exit | https://www.sunat.gob.pe/legislacion/mypeIR/dl1269.pdf | 2026-11-11 |
| DS 403-2016-EF; arts. 3-5 capital-linkage, entry and prior-RER/Nuevo RUS-month exception; art. 6 formal deduction requirements and art. 8 suspension screen consulted | https://www.sunat.gob.pe/legislacion/mypeIR/r-dl1269.pdf | 2026-11-11 |
| Regulation Chapter XI; art. 54 advance comparison and four-decimal precision; suspension/modification routes consulted | https://www.sunat.gob.pe/legislacion/renta/regla/cap11.pdf | 2026-11-11 |
| SUNAT UIT table; 2026 row and DS 301-2025-EF reference | https://www.sunat.gob.pe/indicestasas/uit.html | 2026-11-11 |
| Law 32434 Gazette HTML; arts. 3-4, 11-14, commencement/exclusions. Rate table absent from HTML | https://busquedas.elperuano.pe/dispositivo/EX/2437329-1 | 2026-11-11 |
| Law 32434 direct official Gazette PDF; art. 12.1 table visually read on PDF page 4 / Gazette page 5, with arts. 2-4, 11-14 and commencement/exclusion neighbours | https://busquedas.elperuano.pe/api/archivo/file/7oiMed6E4bc8gpK300ViG3/*/2437329-1.PDF | 2026-11-11 |
| DS 015-2026-EF official government PDF; arts. 3-12 activity/sector-payment provisions | https://cdn.www.gob.pe/uploads/document/file/9437490/7730417-decreto-supremo-n-015-2026-ef.pdf?v=1770915573 | 2026-11-11 |
| RS 335-2017; arts. 6-10 submission, payment, rejection and receipts | https://www.sunat.gob.pe/legislacion/superin/2017/335-2017.pdf | 2026-11-11 |
| RS 047-2026; final RS 335 payment amendment, distinguished from ordinary income tax | https://www.sunat.gob.pe/legislacion/superin/2026/000047-2026.pdf | 2026-11-11 |
| SUNAT monthly guidance; 621 and advance comparison; old annual banner not treated as a 2026 return timetable | https://orientacion.sunat.gob.pe/declaracion-y-pago-mensual-1 | 2026-11-11 |
| SUNAT annual 710 page; populations read as explicitly dated 2025 campaign procedure, not released 2026 form | https://renta.sunat.gob.pe/empresas/como-realizar-la-declaracion-del-impuesto-la-renta | 2026-11-11 |
| Tax Code through 26 June 2026; arts. 33, 176, 178, 180 and current Table I/general notes/note 21 | https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf | 2026-11-11 |

Not yet confirmed: exact RUC-specific 2027 annual dates for 2026; released 2026 annual 710 version/numbered fields/annexes; current live 621 numbered fields; current numeric TIM and fact-specific penalty relief. These are omitted rather than copied from the 2025 campaign or memory. Full agrarian/special-sector computations, ITAN, stability/reorganisation cases, detailed asset-rate elections and transaction-specific withholding/foreign-credit computations require separate primary-source workings outside this ordinary corporate method.
