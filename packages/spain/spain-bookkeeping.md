---
name: spain-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Plan General de Contabilidad (PGC), financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for a Spanish entity. Trigger on phrases like "PGC", "Plan General de Contabilidad", "cuadro de cuentas", "chart of accounts Spain", "balance", "cuenta de pérdidas y ganancias", "PYMES accounting", "microempresa Spain", "capitalise or expense Spain", "amortización", "depreciation Spain", "bank reconciliation Spain", "autónomo bookkeeping", "bookkeeping Spain", or any question about recording transactions, classifying expenses, or preparing accounts under Spanish law. ALWAYS read this skill before touching any bookkeeping work for Spain.
version: 1.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bookkeeping in Spain: the books, the Plan General de Contabilidad and the annual accounts

Which books a Spanish autónomo or company must keep, how they are legalised at the Registro Mercantil, how long they are kept, the account structure of the Plan General de Contabilidad, the simplifications for a small company, how expenses and assets are classified and what an invoice and a payment must carry. Figures are for tax year 2026. All figures come from consolidated Spanish statutes and from Agencia Tributaria pages current at the date of this refresh; the simplified depreciation table comes from the Agencia Tributaria Manual de actividades económicas, the same page the `es-income-tax` Guide uses.

## Spain bookkeeping: Guide version 2.0

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Currency | EUR |
| Financial year | The tax year for personal income tax is the calendar year. A company's financial year is whatever its articles say; where the articles are silent, the Ley de Sociedades de Capital says it ends on the thirty first of December |
| Accounting standards | Plan General de Contabilidad, Real Decreto 1514/2007; Plan General de Contabilidad de Pequeñas y Medianas Empresas, Real Decreto 1515/2007, which also carries the specific criteria for microempresas |
| Governing bodies | Instituto de Contabilidad y Auditoría de Cuentas; Registro Mercantil; Agencia Tributaria |
| Key legislation | Código de Comercio, articles 25 to 49; Ley de Sociedades de Capital; Ley 27/2014 del Impuesto sobre Sociedades; Ley 35/2006 del Impuesto sobre la Renta de las Personas Físicas and its Reglamento, Real Decreto 439/2007; the two accounting plans |
| Compulsory books, any trader | Libro de Inventarios y Cuentas anuales, and a Libro Diario |
| Extra books, a company | A book or books of actas; a libro registro de socios in an SL, or a libro registro de acciones nominativas in an SA |
| Books, autónomo in estimación directa simplificada | Libro registro de ventas e ingresos, libro registro de compras y gastos, libro registro de bienes de inversión. A professional keeps a book of ingresos, one of gastos, one of bienes de inversión and one of provisiones de fondos y suplidos |
| Standard chart of accounts | The cuadro de cuentas in part four of the Plan General de Contabilidad, nine groups. The accounting movements in part five are not binding, and neither is the numbering and naming of the accounts in part four, except where either carries a recognition or measurement criterion |
| Record retention | Six years from the last entry under the Código de Comercio; four years for tax, being the general prescription period |

## Which books each taxpayer must keep

The duty follows two separate laws at once. The Código de Comercio binds anyone who is an empresario, which includes a company and a trading sole trader. The income tax rules bind the individual, and for an individual whose activity is not mercantile they replace full accounting with a short list of registers.

### The autónomo in estimación directa simplificada

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Prior-year turnover under which the simplified direct estimation applies | EUR 600,000 | "no supere los 600.000 euros anuales en el año inmediato anterior" |
| Deductible provisions and hard-to-justify expenses together, as a share of net income before this item | 5% | "se cuantificará aplicando el porcentaje del 5 por ciento sobre el rendimiento neto" |
| Yearly ceiling on that same item | EUR 2,000 | "sin que la cuantía resultante pueda superar 2.000 euros anuales" |

- **A business activity keeps three registers.** Article 68.4 of Real Decreto 439/2007 sends the simplified filer to the list in article 68.3: a libro registro de ventas e ingresos, a libro registro de compras y gastos and a libro registro de bienes de inversión. There is no libro diario and no double entry.
- **A professional activity keeps four.** Article 68.5 applies to a professional in either modality of direct estimation: libro registro de ingresos, libro registro de gastos, libro registro de bienes de inversión and libro registro de provisiones de fondos y suplidos.
- **The turnover limit is a cliff**, tested on the prior year across all the taxpayer's activities together. The reduction in the table is the combined figure for deductible provisions and hard-to-justify expenses, not a separate allowance on top.

### The autónomo in estimación directa normal

- **A mercantile business keeps full accounts.** Article 68.2 of Real Decreto 439/2007 requires accounting adjusted to the Código de Comercio for a business activity in the normal modality. That means the Libro de Inventarios y Cuentas anuales and the Libro Diario, and the legalisation duty below.
- **A non-mercantile activity does not.** Article 68.3 limits the duty to the three registers, whichever modality applies. A professional in the normal modality keeps the four registers of article 68.5, not a libro diario.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820

### The autónomo in estimación objetiva (módulos)

- **Invoices, not books.** Article 68.6 of Real Decreto 439/2007 requires the invoices issued to be kept numbered in date order and grouped by quarter, together with the invoices and other documents received, and the evidence for the signs, indices and modules applied.
- **Two extra registers where they bite.** Anyone in this method who deducts depreciation keeps a libro registro de bienes de inversión, and any activity whose net income depends on the volume of operations keeps a libro registro de ventas o ingresos (article 68.7).
- **Do not place a client in or out of módulos from this Guide.** Two official sources disagree about the income limits that decide who may stay in the method. The `es-estimated-tax` Guide prints both readings side by side. Use it, and treat the entry test as unsettled.

### The company: the books the Código de Comercio demands

| What | Book | Note |
| --- | --- | --- |
| Source | all rules below | https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627 |
| Every empresario | Libro de Inventarios y Cuentas anuales | Opens with a detailed opening balance sheet. At least quarterly a trial balance with sums and balances is transcribed into it. The closing inventory and the annual accounts are transcribed into it too (article 28.1) |
| Every empresario | Libro Diario | Records every operation of the business day by day. A combined entry of the totals is valid for periods of no more than a quarter, provided the detail appears in other matching books or registers (article 28.2) |
| A mercantile company | Libro o libros de actas | Records at least every resolution of the general and special meetings and of the other collegiate bodies, with the convening and constitution data, a summary of what was debated, the interventions for which a record was asked, the resolutions adopted and the voting results (article 26.1) |
| A sociedad de responsabilidad limitada | Libro registro de socios | The company treats as a member only the person entered in it (article 104 of the Ley de Sociedades de Capital) |
| A sociedad anónima or comanditaria por acciones with registered shares | Libro registro de acciones nominativas | The company treats as a shareholder only the person entered in it (article 116 of the Ley de Sociedades de Capital) |

- **Who may keep them.** The accounting is kept by the empresario directly or by other duly authorised persons, without relieving the empresario of responsibility. Authorisation is presumed unless the contrary is proved (article 25.2).
- **How they are written.** Article 29 requires the books to be kept, whatever the procedure used, in date order with no gaps, interpolations, crossings out or erasures. Errors are corrected as soon as they are noticed. Abbreviations or symbols whose meaning is not precise under the law, the regulation or general commercial practice may not be used.
- **The annual accounts are a unit.** Article 34.1 lists the balance sheet, the profit and loss account, a statement of changes in equity, a cash flow statement and the memoria. The statement of changes in equity and the cash flow statement are not compulsory where a legal provision says so.
- The Ley de Sociedades de Capital articles named above are at https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

### The VAT registers

The VAT registers are a separate set, kept under the Reglamento del IVA, and they are the `es-vat-return` Guide's subject. Article 62.1 of Real Decreto 1624/1992 lists four: a libro registro de facturas expedidas, a libro registro de facturas recibidas, a libro registro de bienes de inversión and a libro registro de determinadas operaciones intracomunitarias. The simplified regime, the farming regime and the equivalence surcharge regime are outside that general duty, subject to what their own rules say. Do not answer a question about the content, the deadlines or the electronic supply of these registers from this Guide; read `es-vat-return`.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925 |
| Previous calendar year turnover above which the VAT period is the month, which is also what pulls a business into supplying the registers electronically | EUR 6,010,121.04 | "hubiese excedido durante el año natural inmediato anterior de 6.010.121,04 euros" |

## Legalisation at the Registro Mercantil

- **The deadline is four months from the close of the financial year.** Article 27.2 of the Código de Comercio allows entries to be made by any suitable procedure on sheets that are later bound in order to form the compulsory books, and those books are legalised "antes de que transcurran los cuatro meses siguientes a la fecha de cierre del ejercicio".
- **It is electronic, and it covers the actas and the members' register too.** Article 18.1 of Ley 14/2013 says every book a trader must keep, including the books of minutes of meetings and other collegiate bodies and the registers of members and of registered shares, is legalised telematically at the Registro Mercantil after being completed in electronic form, and before those same four months run out.
- **Which registry.** The one of the place where the trader has its domicilio. A legalisation done by the registry of origin keeps its full value after a change of domicile (article 27.1).
- **What the registrar does.** The registrar checks the formal requirements and the regular successive formation of the books within each class, and certifies the intervention electronically with a validation code (article 18.3 of Ley 14/2013).
- **Minute books may be legalised more often.** A trader may voluntarily legalise books of detail of minutes, or groups of minutes, formed over a period shorter than the year, where it matters to prove the fact and the date reliably (article 18.2 of Ley 14/2013).
- Sources: https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627 and https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074

## The annual accounts: formulate, approve, deposit

Three deadlines run one after the other, and only the last one carries a fine.

| Step | Deadline | Note |
| --- | --- | --- |
| Source | all rules below | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| The directors formulate the annual accounts, the management report and the proposed appropriation of the result | Within three months of the close of the financial year | "en el plazo máximo de tres meses contados a partir del cierre del ejercicio social" (article 253.1) |
| The ordinary general meeting approves them | Within the first six months of each financial year | The meeting is valid even if convened or held out of time (article 164) |
| The directors file them at the Registro Mercantil of the registered office | Within the month following approval | Certification of the resolutions approving the accounts and appropriating the result, with a copy of each of them, plus the management report and the auditor's report where the company must be audited (article 279.1) |

**The fine for filing late (article 283 of the Ley de Sociedades de Capital)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| Fine on the company, lower end of the range | EUR 1,200 | "una multa por importe de 1.200 a 60.000 euros por el Instituto de Contabilidad y Auditoría de Cuentas" |
| Fine on the company, upper end of the range | EUR 60,000 | "una multa por importe de 1.200 a 60.000 euros por el Instituto de Contabilidad y Auditoría de Cuentas" |
| Annual turnover of the company or group above which the ceiling rises | EUR 6,000,000 | "Cuando la sociedad o, en su caso, el grupo de sociedades tenga un volumen de facturación anual superior a 6.000.000 euros" |
| The raised ceiling, for each year of delay | EUR 300,000 | "el límite de la multa para cada año de retraso se elevará a 300.000 euros" |

- The fine is set by the Instituto de Contabilidad y Auditoría de Cuentas, sized by the company's total assets and sales figure for the last year declared to the tax administration. Where the accounts were filed before the penalty procedure started, the fine is imposed at its minimum grade and cut by fifty per cent. These infringements prescribe in three years.

## How long to keep the books

| What | Period | Note |
| --- | --- | --- |
| Source, the commercial rule | all rules below | https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627 |
| Books, correspondence, documentation and supporting papers concerning the business | Six years from the last entry made in the books | "durante seis años, a partir del último asiento realizado en los libros" (article 30.1). Ceasing to trade does not end the duty; it passes to the heirs, or to the liquidators of a dissolved company |

| What | Period | Note |
| --- | --- | --- |
| Source, the tax rule | all rules below | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 |
| The administration's right to assess the tax debt, and to demand payment of debts already assessed | Four years | Article 66. The taxpayer's rights to claim and to obtain refunds prescribe on the same four years |
| The administration's right to start a check of offset or pending losses, deductions and bases | Ten years | Article 66 bis.2, counted from the day after the filing deadline of the return for the period in which the right arose |

- The income tax rule adds its own line: article 68.1 of Real Decreto 439/2007 makes the taxpayer keep the vouchers and documents evidencing the operations, income, expenses, reductions and deductions that must appear in the returns "durante el plazo máximo de prescripción".
- A payment that could not lawfully be made in cash has its own retention rule: the parties keep the evidence of the payment for five years from its date, to prove it went through a means of payment other than cash (article 7 of Ley 7/2012).
- **Take the longest period that applies.** Six years from the last entry will normally outlast the four year tax period, but a loss carried forward keeps the ten year window open on the year that created it.

## Section 2: Standard Chart of Accounts (PGC / PGC-PYMES, Cuadro de Cuentas)

The cuadro de cuentas in part four of the Plan General de Contabilidad, Real Decreto 1514/2007, has **nine** groups, not seven. Groups 1 to 5 are balance sheet accounts, groups 6 and 7 are profit and loss accounts, and groups 8 and 9 hold the expenses and the income charged directly to equity. The Plan General de Contabilidad de Pequeñas y Medianas Empresas has no group 8 and no group 9, because a business on that plan does not use the equity-charged categories those groups exist for.

| Group | Name in the plan | What it holds |
| --- | --- | --- |
| Source | the group names below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884 |
| Grupo 1 | Financiación básica | Equity and long term financing |
| Grupo 2 | Activo no corriente | Non-current assets |
| Grupo 3 | Existencias | Inventories |
| Grupo 4 | Acreedores y deudores por operaciones comerciales | Trade payables and receivables |
| Grupo 5 | Cuentas financieras | Financial accounts |
| Grupo 6 | Compras y gastos | Purchases and expenses |
| Grupo 7 | Ventas e ingresos | Sales and revenue |
| Grupo 8 | Gastos imputados al patrimonio neto | Expenses charged to equity |
| Grupo 9 | Ingresos imputados al patrimonio neto | Income charged to equity |

**Using the codes is not compulsory, and both plans say so in the same words.** Article 2 of Real Decreto 1514/2007 for the full plan, and article 3.1 of Real Decreto 1515/2007 for the small and medium plan, each say that the accounting movements in part five and the aspects relating to the numbering and naming of accounts in part four are not binding, except where they contain recognition or measurement criteria. The recognition and measurement rules themselves are binding. In practice every Spanish accounting package ships the standard codes, so departing from them costs more than it saves.

The group structure and the account names below are the plan's own, taken from its cuadro de cuentas. **The selection of accounts, and the English labels, are OpenAccountants' own**: this is the short list a small Spanish business actually uses, not a reproduction of the whole cuadro, which runs to several hundred accounts.

### Grupo 1: Financiación Básica (Basic Financing, Equity & Long-Term Liabilities)

| Code | Account | Notes |
| --- | --- | --- |
| 100 | Capital social | Share capital |
| 102 | Capital | Owner's capital, sole trader |
| 112 | Reserva legal | Legal reserve. A company must put a figure equal to ten per cent of the year's profit into it until it reaches at least twenty per cent of the share capital (article 274 of the Ley de Sociedades de Capital). A sociedad de responsabilidad limitada whose capital has not yet reached three thousand euros follows a stricter rule instead: article 4.1 of the same law makes it put at least twenty per cent of the profit into the legal reserve until the reserve and the share capital together reach three thousand euros |
| 113 | Reservas voluntarias | Voluntary reserves |
| 120 | Remanente | Retained earnings |
| 121 | Resultados negativos de ejercicios anteriores | Accumulated losses |
| 129 | Resultado del ejercicio | Current year profit or loss |
| 130 | Subvenciones oficiales de capital | Government capital grants |
| 141 | Provisión para impuestos | Tax provisions |
| 142 | Provisión para otras responsabilidades | Other provisions |
| 170 | Deudas a largo plazo con entidades de crédito | Long term bank loans |
| 171 | Deudas a largo plazo | Other long term debts |
| 174 | Acreedores por arrendamiento financiero a largo plazo | Finance lease liabilities, long term |

### Grupo 2: Activo No Corriente (non-current assets)

| Code | Account | Notes |
| --- | --- | --- |
| 200 | Investigación | Research costs |
| 201 | Desarrollo | Development costs |
| 203 | Propiedad industrial | Patents and trademarks |
| 206 | Aplicaciones informáticas | Software |
| 210 | Terrenos y bienes naturales | Land. Land is not depreciated |
| 211 | Construcciones | Buildings |
| 212 | Instalaciones técnicas | Technical installations |
| 213 | Maquinaria | Machinery |
| 214 | Utillaje | Tools |
| 215 | Otras instalaciones | Other installations |
| 216 | Mobiliario | Furniture |
| 217 | Equipos para procesos de información | Computer equipment |
| 218 | Elementos de transporte | Vehicles |
| 219 | Otro inmovilizado material | Other tangible assets |
| 280 | Amortización acumulada del inmovilizado intangible | Accumulated amortisation, intangible |
| 281 | Amortización acumulada del inmovilizado material | Accumulated depreciation, tangible |
| 290 | Deterioro de valor del inmovilizado intangible | Impairment, intangible |
| 291 | Deterioro de valor del inmovilizado material | Impairment, tangible |

### Grupo 3: Existencias (inventories)

| Code | Account | Notes |
| --- | --- | --- |
| 300 | Mercaderías | Merchandise |
| 310 | Materias primas | Raw materials |
| 350 | Productos terminados | Finished goods |
| 390 | Deterioro de valor de las mercaderías | Write-down of merchandise |

### Grupo 4: Acreedores y Deudores por Operaciones Comerciales (Trade Payables & Receivables)

| Code | Account | Notes |
| --- | --- | --- |
| 400 | Proveedores | Trade payables |
| 410 | Acreedores por prestaciones de servicios | Creditors for services |
| 430 | Clientes | Trade receivables |
| 438 | Anticipos de clientes | Customer advances on account of future supplies |
| 440 | Deudores | Sundry debtors |
| 465 | Remuneraciones pendientes de pago | Salaries payable |
| 470 | Hacienda Pública, deudora por diversos conceptos | Amounts recoverable from the tax authority |
| 4700 | Hacienda Pública, deudora por IVA | VAT recoverable, input above output |
| 472 | Hacienda Pública, IVA soportado | Input VAT |
| 473 | Hacienda Pública, retenciones y pagos a cuenta | Withholding tax and payments on account suffered |
| 475 | Hacienda Pública, acreedora por conceptos fiscales | Amounts payable to the tax authority |
| 4750 | Hacienda Pública, acreedora por IVA | VAT payable |
| 476 | Organismos de la Seguridad Social, acreedores | Social security payable |
| 477 | Hacienda Pública, IVA repercutido | Output VAT |
| 480 | Gastos anticipados | Prepaid expenses |
| 485 | Ingresos anticipados | Deferred income |

### Grupo 5: Cuentas Financieras (financial accounts)

| Code | Account | Notes |
| --- | --- | --- |
| 520 | Deudas a corto plazo con entidades de crédito | Short term bank loans |
| 523 | Proveedores de inmovilizado a corto plazo | Short term creditors for fixed assets |
| 524 | Acreedores por arrendamiento financiero a corto plazo | Finance lease liabilities, short term |
| 551 | Cuenta corriente con socios y administradores | Directors' and members' current account |
| 570 | Caja, euros | Cash in hand, euro |
| 572 | Bancos e instituciones de crédito c/c vista, euros | Bank current accounts, euro |
| 573 | Bancos e instituciones de crédito c/c vista, moneda extranjera | Bank current accounts, foreign currency |
| 574 | Bancos e instituciones de crédito, cuentas de ahorro, euros | Bank savings accounts, euro |
| 575 | Bancos e instituciones de crédito, cuentas de ahorro, moneda extranjera | Bank savings accounts, foreign currency |

### Grupo 6: Compras y Gastos (Purchases & Expenses)

| Code | Account | Notes |
| --- | --- | --- |
| 600 | Compras de mercaderías | Merchandise purchases |
| 601 | Compras de materias primas | Raw material purchases |
| 602 | Compras de otros aprovisionamientos | Other supplies |
| 606 | Descuentos sobre compras por pronto pago | Purchase discounts for prompt payment |
| 607 | Trabajos realizados por otras empresas | Subcontracting |
| 621 | Arrendamientos y cánones | Rent and royalties |
| 622 | Reparaciones y conservación | Repairs and maintenance |
| 623 | Servicios de profesionales independientes | Professional fees |
| 624 | Transportes | Transport costs |
| 625 | Primas de seguros | Insurance premiums |
| 626 | Servicios bancarios y similares | Bank charges |
| 627 | Publicidad, propaganda y relaciones públicas | Advertising and public relations |
| 628 | Suministros | Utilities: electricity, water, gas |
| 629 | Otros servicios | Telecoms, postage, other services |
| 631 | Otros tributos | Taxes other than income tax |
| 640 | Sueldos y salarios | Salaries |
| 642 | Seguridad Social a cargo de la empresa | Employer social security |
| 649 | Otros gastos sociales | Other social costs |
| 650 | Pérdidas de créditos comerciales incobrables | Bad debts written off |
| 662 | Intereses de deudas | Interest on borrowings |
| 669 | Otros gastos financieros | Other financial expenses |
| 678 | Gastos excepcionales | Exceptional charges |
| 680 | Amortización del inmovilizado intangible | Amortisation, intangible |
| 681 | Amortización del inmovilizado material | Depreciation, tangible |
| 694 | Pérdidas por deterioro de créditos por operaciones comerciales | Impairment of trade receivables |

### Grupo 7: Ventas e Ingresos (Sales & Revenue)

| Code | Account | Notes |
| --- | --- | --- |
| 700 | Ventas de mercaderías | Merchandise sales |
| 701 | Ventas de productos terminados | Sales of finished goods |
| 705 | Prestaciones de servicios | Service revenue |
| 706 | Descuentos sobre ventas por pronto pago | Sales discounts for prompt payment |
| 708 | Devoluciones de ventas y operaciones similares | Sales returns |
| 740 | Subvenciones, donaciones y legados a la explotación | Operating grants |
| 746 | Subvenciones, donaciones y legados de capital transferidos al resultado del ejercicio | Capital grants released to the result |
| 762 | Ingresos de créditos | Interest income |
| 769 | Otros ingresos financieros | Other financial income |
| 771 | Beneficios procedentes del inmovilizado material | Gains on disposal of fixed assets |
| 778 | Ingresos excepcionales | Exceptional income |

Source for every account code and Spanish name above: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884

## Section 3: Revenue Recognition

| Scenario | Treatment |
| --- | --- |
| **Default under the accounting plans** | Accruals (devengo). Revenue is recognised when the goods or services are delivered, not when the money arrives |
| **Estimación directa normal** | Full accruals with double entry where the activity is mercantile; otherwise the three registers, still on accruals |
| **Estimación directa simplificada** | Simplified registers but still accruals. The turnover limit is in the table in "Which books each taxpayer must keep" |
| **Estimación objetiva (módulos)** | Net income is computed from objective parameters, not from the recorded revenue. Invoices are kept; see the section above |
| **Autónomo, general** | Income and expenses go in the libros registro named above, with the date, the invoice number, the counterparty and the amount |
| **VAT on sales** | Revenue is recorded net of VAT. The VAT goes to account 477, IVA repercutido |
| **Advance payments** | A payment received on account of a future supply is credited to account 438, Anticipos de clientes, and cleared when the supply is invoiced. Account 485, Ingresos anticipados, is a different thing: it is the year-end cut-off entry for income already recorded in the closing year that belongs to the next one |

There is one Spanish election that changes all of this for VAT only: the cash criterion regime (régimen especial del criterio de caja). It moves the VAT tax point to collection, and it does **not** move the accounting or income tax tax point. It is the `es-vat-return` Guide's subject.

### IVA Rates (2026)

| Rate | Application | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| 21% | The general rate. The default for any taxable supply where nothing else applies | "El Impuesto se exigirá al tipo del 21 por ciento" |
| 10% | The reduced rate. Article 91.Uno lists it: food and drink outside the super-reduced list, water, passenger transport, hotels, restaurants and catering, the first transfer of new housing, qualifying home renovation | "Se aplicará el tipo del 10 por ciento a las operaciones siguientes" |
| 4% | The super-reduced rate. Article 91.Dos lists it: plain bread, milk, cheese, eggs, fruit, vegetables, pulses, tubers and cereals, olive oil, books, newspapers, medicines for human use, social housing | "Se aplicará el tipo del 4 por ciento a las operaciones siguientes" |

**Exempt is not a rate.** A supply exempt under article 20 of Ley 37/1992, such as medical care, education, insurance, most financial services or residential letting, carries no output VAT and gives no right to deduct the input VAT behind it. Recording it as a zero rate will produce the wrong deductible proportion. Exports and intra-Community supplies are a different case again: exempt, but with the right to deduct. Which box each of these goes in is in `es-vat-return`.

## Section 4: Expense Classification

### What the corporate tax law refuses, and the one thing it caps

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Client and supplier entertainment (atenciones a clientes o proveedores), deductible up to this share of the net turnover of the tax period | 1% | "los gastos por atenciones a clientes o proveedores serán deducibles con el límite del 1 por ciento del importe neto de la cifra de negocios del período impositivo" |

Article 15 of Ley 27/2014 lists what is never a deductible expense: anything that is a return on own funds; the corporate tax charge and the Impuesto Complementario; criminal and administrative fines and penalties, the surcharges of the enforcement period and the surcharge for a late return filed without a prior demand; gambling losses; gifts and liberalities; expenses of conduct contrary to the law; and services corresponding to operations with persons or entities in a territory classed as a tax haven, unless the taxpayer proves the operation really happened. The same article says that client and supplier entertainment, customary staff expenses, promotion of sales, and anything correlated with income are **not** gifts or liberalities, so they are deductible; entertainment is then capped by the figure in the table.

A self-employed person is inside these rules too. Article 28.1 of Ley 35/2006 determines net income from an economic activity by the corporate tax rules, with the special rules below on top.

### Special self-employed expense rules

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Share of the home supplies bill that is deductible, applied to the area proportion, unless another share is proved | 30% | "en el porcentaje resultante de aplicar el 30 por ciento a la proporción existente entre los metros cuadrados" |
| Health insurance premium ceiling, per person covered | EUR 500 | "El límite máximo de deducción será de 500 euros por cada una de las personas" |
| The same ceiling where that person has a disability | EUR 1,500 | "o de 1.500 euros por cada una de ellas con discapacidad" |

- The home supplies share is applied to the proportion the area used for the activity bears to the total area of the home. It is a default, not a cap: a higher or a lower percentage is allowed where it is proved.
- The health cover may include the taxpayer, their spouse and children under twenty five living with them. The ceiling is per person, per year.

### Own meal costs while working

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Per day in Spain, with an overnight stay | EUR 53.34 | "Por gastos de manutención, 53,34 euros diarios, si corresponden a desplazamiento dentro del territorio español" |
| Per day abroad, with an overnight stay | EUR 91.35 | "o 91,35 euros diarios, si corresponden a desplazamientos a territorio extranjero" |
| Per day in Spain, no overnight stay | EUR 26.67 | "las asignaciones para gastos de manutención que no excedan de 26,67" |
| Per day abroad, no overnight stay | EUR 48.08 | "26,67 ó 48,08 euros diarios" |

**Both conditions must hold, not either.** The meal must be taken in a restaurant or hospitality establishment AND paid by electronic means. A cash receipt fails the test even if the amount is inside the limit.

### The payment has to be traceable, and above a limit it may not be cash

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2012-13416 |
| Amount at or above which an operation with a business or professional on either side may not be paid in cash | EUR 1,000 | "No podrán pagarse en efectivo las operaciones, en las que alguna de las partes intervinientes actúe en calidad de empresario o profesional, con un importe igual o superior a 1.000 euros" |
| The same limit where the payer is an individual who proves they are not tax resident in Spain and is not acting as a business or professional | EUR 10,000 | "el citado importe será de 10.000 euros o su contravalor en moneda extranjera cuando el pagador sea una persona física" |
| Fine, as a share of the amount paid in cash | 25% | "La sanción consistirá en multa pecuniaria proporcional del 25 por ciento de la base de la sanción" |

- **Splitting does not help.** The amounts of all the operations or payments into which the delivery of goods or the supply of services has been broken up are added together.
- **Both sides are liable.** Payer and receiver answer jointly and severally, and the Agencia Tributaria may proceed against either or both.
- **Keep the proof for five years** from the date of payment, and produce it on request.

### Invoices

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696 |
| Amount, VAT included, up to which a simplified invoice may be issued for any operation | EUR 400 | "Cuando su importe no exceda de 400 euros, Impuesto sobre el Valor Añadido incluido" |
| Amount, VAT included, up to which a simplified invoice may be issued in the listed cases, retail sales among them | EUR 3,000 | "cuando su importe no exceda de 3.000 euros, Impuesto sobre el Valor Añadido incluido" |

A full invoice under article 6 of Real Decreto 1619/2012 carries the number and, where used, the series, with correlative numbering inside each series; the date of issue; the full name or company name of both the issuer and the customer; the tax identification number of the issuer, and of the customer in the cases the article lists, which include an exempt intra-Community supply of goods and any operation where the customer is the taxable person; the address of both; the description of the operation with the data needed to determine the taxable amount and its unit price; the rate applied; the VAT charged, shown separately; the date of the operation where it differs from the date of issue; and the wording the article requires where the operation is exempt, reverse charged, under a margin scheme or on the cash criterion.

**Timing.** The invoice is issued when the operation is carried out. Where the customer is a business or professional acting as such, it must be issued before the sixteenth day of the month following the one in which the VAT on that operation became chargeable (article 11.1).

**The software is a separate duty.** Real Decreto 1619/2012 says what an invoice must carry. What the program that issues it must do is a different regime with its own timetable, and it is in `spain-einvoice`, not here.

### The classification table

No figure appears in this table. Where a limit or a rate matters, it is in one of the sourced tables above.

| Expense type | PGC code | Tax treatment | Notes |
| --- | --- | --- | --- |
| Rent of commercial premises | 621 | Deductible | Rent to a landlord is generally subject to withholding; see `es-income-tax` |
| Utilities | 628 | Deductible for business premises | Apportion if a home office; see the share in the self-employed table above |
| Home office, autónomo | 628 and 621 | Deductible on the area proportion, and for supplies on the share of that proportion in the table above | Article 30.2 rule 5 of Ley 35/2006 |
| Professional fees, asesor fiscal or abogado | 623 | Deductible | The invoice is normally subject to withholding on account of income tax; the rate is in `es-income-tax` |
| Insurance | 625 | Deductible for the business | Health cover for the autónomo has its own ceiling, in the table above |
| Advertising and public relations | 627 | Deductible |  |
| Travel and subsistence | 629 | Deductible. The taxpayer's own meals are capped per day, in the table above | Both the restaurant condition and the electronic payment condition must hold |
| Client and supplier entertainment | 627 | Deductible up to the share of net turnover in the table above | Not a gift under article 15.e of Ley 27/2014, so not blocked outright |
| Office supplies | 602 | Deductible |  |
| Telecoms | 629 | Deductible for a business line | Apportion a mixed-use line |
| Bank charges | 626 | Deductible |  |
| Vehicle, autónomo | various | Income tax: only where the vehicle is an asset of the activity. Article 22.4 of Real Decreto 439/2007 refuses to treat incidental private use as irrelevant for cars, mopeds, motorcycles, aircraft and pleasure craft, except for mixed goods vehicles, passenger transport for consideration, driving or flying instruction for consideration, and the travel of commercial representatives and agents, and a vehicle habitually hired out for consideration | The VAT side is a separate presumption; see `es-vat-return` |
| Vehicle fuel and running costs | 602 and 628 | Follows the vehicle above | The VAT side is in `es-vat-return` |
| Fines, penalties and tax surcharges | 678 | Not deductible | Article 15.c of Ley 27/2014 covers criminal and administrative fines, enforcement-period surcharges and the surcharge for a late return filed without a prior demand |
| Depreciation and amortisation | 680 and 681 | Deductible on the tables in Section 5 |  |
| Gifts and donations | 678 | Not deductible as an expense | Article 15.e of Ley 27/2014. Relief for a gift to a qualifying non-profit is a tax credit under its own law, not an expense, and it is outside this Guide |

## Section 5: Asset vs Expense Thresholds

### Capitalisation Rules

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Unit value at or below which a new tangible fixed asset may be depreciated freely | EUR 300 | "Los elementos del inmovilizado material nuevos, cuyo valor unitario no exceda de 300 euros" |
| Ceiling on that free depreciation for the tax period | EUR 25,000 | "hasta el límite de 25.000 euros referido al período impositivo" |

- **It is article 12.3.e of Ley 27/2014, not a small-company rule.** The provision sits in the general depreciation article and is open to any corporate taxpayer. The live version of this Guide attributed it to article 102 and restricted it to empresas de reducida dimensión. Article 102 is a different relief, tied to an increase in the average headcount.
- **The asset must be NEW and tangible.** Second-hand equipment and intangibles are outside this letter.
- **Both limits bite together.** The unit value must not exceed the first amount, and the total taken under this letter in the period must not exceed the second. Where the tax period is shorter than a year, the ceiling is the second amount multiplied by the proportion the period bears to the year.
- **It reduces the tax value of the asset.** Amounts taken as free depreciation reduce, for tax purposes, the value of the assets depreciated.
- Above those limits, capitalise and depreciate on the table below.

### Depreciation Rates (LIS Art. 12.1.a, Tabla de Amortización Lineal)

This is the whole official table in article 12.1.a of Ley 27/2014. It applies to a company, and to an autónomo in the normal modality of direct estimation.

| Asset type | Maximum linear coefficient | Maximum period, years |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Obra civil general | 2% | 100 |
| Pavimentos | 6% | 34 |
| Infraestructuras y obras mineras | 7% | 30 |
| Centrales hidráulicas | 2% | 100 |
| Centrales nucleares | 3% | 60 |
| Centrales de carbón | 4% | 50 |
| Centrales renovables | 7% | 30 |
| Otras centrales | 5% | 40 |
| Edificios industriales | 3% | 68 |
| Terrenos dedicados exclusivamente a escombreras | 4% | 50 |
| Almacenes y depósitos, gaseosos, líquidos y sólidos | 7% | 30 |
| Edificios comerciales, administrativos, de servicios y viviendas | 2% | 100 |
| Subestaciones, redes de transporte y distribución de energía | 5% | 40 |
| Cables | 7% | 30 |
| Resto instalaciones | 10% | 20 |
| Maquinaria | 12% | 18 |
| Equipos médicos y asimilados | 15% | 14 |
| Locomotoras, vagones y equipos de tracción | 8% | 25 |
| Buques, aeronaves | 10% | 20 |
| Elementos de transporte interno | 10% | 20 |
| Elementos de transporte externo | 16% | 14 |
| Autocamiones | 20% | 10 |
| Mobiliario | 10% | 20 |
| Lencería | 25% | 8 |
| Cristalería | 50% | 4 |
| Útiles y herramientas | 25% | 8 |
| Moldes, matrices y modelos | 33% | 6 |
| Otros enseres | 15% | 14 |
| Equipos electrónicos | 20% | 10 |
| Equipos para procesos de información | 25% | 8 |
| Sistemas y programas informáticos | 33% | 6 |
| Producciones cinematográficas, fonográficas, vídeos y series audiovisuales | 33% | 6 |
| Otros elementos | 10% | 20 |

- **Land is not in the table and is not depreciated.** Split the land out of the purchase price of a building before applying the building coefficient.
- **The coefficient is a maximum and the period is a maximum.** Any figure between the two is accepted as effective depreciation.
- **There are four other accepted methods** in article 12.1: a constant percentage on the written down value, the sum of the digits, a plan agreed with the tax administration, and any amount the taxpayer justifies. Buildings, furniture and fittings may not use the constant percentage or the digits method.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Floor under the constant percentage method | 11% | "El porcentaje constante no podrá ser inferior al 11 por ciento" |

- An intangible asset is amortised over its useful life. Where that cannot be estimated reliably, and for goodwill, the deduction is capped each year at one twentieth of the amount (article 12.2).

### Accelerated Depreciation for Small Businesses (Empresas de Reducida Dimensión)

The regime is open where the net turnover of the immediately preceding tax period was below the amount in the table below. The incentives do not apply to an entity that is an entidad patrimonial.

- **New tangible assets, property investments and intangible assets** put at the taxpayer's disposal in a period that meets the test may be depreciated at the coefficient that results from multiplying by two the maximum linear coefficient in the official tables (article 103.1). The "new" condition is written for the tangible assets and the property investments; the article does not repeat it for the intangibles.
- **The relief runs on after the company outgrows it.** Article 101.4 keeps the incentives for the three immediately following tax periods after the one in which the turnover reaches that figure, provided the conditions were met in that period and in the two before it.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Net turnover of the immediately preceding tax period below which the reduced-dimension incentives apply | EUR 10 million | "sea inferior a 10 millones de euros" |
| Intangibles within article 13.3, deductible at this share of the amount that article gives | 150% | "podrán deducirse en un 150 por ciento del importe que resulte de aplicar dicho apartado" |

- Article 102 is a different relief and is often confused with this one: free depreciation of new tangible assets and property investments, conditional on the total average headcount over the twenty four months from the start of the tax period in which the assets come into operation rising against the average of the twelve months before, and the rise being held for another twenty four months, with the qualifying investment limited by a per-head amount in the article. Failing the headcount test means paying back the tax on the excess with interest.

### Estimación Directa Simplificada Table

An autónomo in the simplified modality does not use the corporate table. Article 30 rule 1 of Real Decreto 439/2007 sends them to a simplified table approved by the Ministry, and adds that the reduced-dimension rules of the corporate tax law that affect depreciation apply on top of the amounts the simplified table produces.

**Tabla de amortización simplificada (Agencia Tributaria, Manual de actividades económicas)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html |
| Grupo 1, buildings and other constructions, maximum 68 years | 3% | "Edificios y otras construcciones 3 % 68" |
| Grupo 2, installations, furniture, fittings and the rest of tangible fixed assets, maximum 20 years | 10% | "Instalaciones, mobiliario, enseres y resto del inmovilizado material 10 % 20" |
| Grupo 3, machinery, maximum 18 years | 12% | "Maquinaria 12 % 18" |
| Grupo 4, transport elements, maximum 14 years | 16% | "Elementos de Transporte 16 % 14" |
| Grupo 5, data processing equipment and computer systems and programs, maximum 10 years | 26% | "sistemas y programas informáticos 26 % 10" |
| Grupo 6, tools and implements, maximum 8 years | 30% | "y herramientas 30 % 8" |
| Grupo 7, cattle, pigs, sheep and goats, maximum 14 years | 16% | "Ganado vacuno, porcino, ovino y caprino 16 % 14" |
| Grupo 8, horses and non-citrus fruit trees, maximum 25 years | 8% | "Ganado equino y frutales no cítricos 8 % 25" |
| Grupo 9, citrus trees and vines, maximum 50 years | 4% | "Frutales cítricos y viñedos 4 % 50" |
| Grupo 10, olive groves, maximum 100 years | 2% | "Olivar 2 % 100" |

- **There is no separate software line.** Computer programs sit in grupo 5 with the hardware, at the grupo 5 rate. This agrees with the `es-income-tax` Guide, which uses the same page.
- The simplified table has ten groups and is shorter than the corporate table. Do not mix a coefficient from one into the other.

## Section 6: P&L Format (Cuenta de Pérdidas y Ganancias)

The model below is the one in part three of the Plan General de Contabilidad de Pequeñas y Medianas Empresas. It is a vertical statement classifying expenses by nature, with the prior year alongside. The plan sets out the accounts that feed each line; they are not reproduced here, and the line captions below are the plan's own.

~~~
CUENTA DE PERDIDAS Y GANANCIAS DE PYMES
Correspondiente al ejercicio terminado el ...

  1. Importe neto de la cifra de negocios.
  2. Variacion de existencias de productos terminados y en curso de fabricacion.
  3. Trabajos realizados por la empresa para su activo.
  4. Aprovisionamientos.
  5. Otros ingresos de explotacion.
  6. Gastos de personal.
  7. Otros gastos de explotacion.
  8. Amortizacion del inmovilizado.
  9. Imputacion de subvenciones de inmovilizado no financiero y otras.
 10. Excesos de provisiones.
 11. Deterioro y resultado por enajenaciones del inmovilizado.
A) RESULTADO DE EXPLOTACION (uno a once)

 12. Ingresos financieros.
 13. Gastos financieros.
 14. Variacion de valor razonable en instrumentos financieros.
 15. Diferencias de cambio.
 16. Deterioro y resultado por enajenaciones de instrumentos financieros.
B) RESULTADO FINANCIERO (doce a dieciseis)

C) RESULTADO ANTES DE IMPUESTOS (A mas B)

 17. Impuestos sobre beneficios.
D) RESULTADO DEL EJERCICIO (C mas diecisiete)
~~~

- **There are no sub-letters in this model.** Line one is a single figure, and so are lines four, six and seven. The earlier version of this Guide broke lines one, four, six and seven into a), b), c) and d) items. Those breakdowns are not in the small and medium plan; the detail belongs in the memoria.
- Line seventeen may be positive or negative.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966

## Section 7: Balance Sheet Format (Balance de Situación)

The model in the Plan General de Contabilidad de Pequeñas y Medianas Empresas is **one vertical statement in two blocks**, not two facing columns. The asset block is totalled, then the equity and liabilities block is totalled, and the two totals must agree.

~~~
BALANCE DE PYMES
Al cierre del ejercicio

ACTIVO
A) ACTIVO NO CORRIENTE
     I. Inmovilizado intangible.
    II. Inmovilizado material.
   III. Inversiones inmobiliarias.
    IV. Inversiones en empresas del grupo y asociadas a largo plazo.
     V. Inversiones financieras a largo plazo.
    VI. Activos por impuesto diferido.
B) ACTIVO CORRIENTE
     I. Existencias.
    II. Deudores comerciales y otras cuentas a cobrar.
          Clientes por ventas y prestaciones de servicios.
          Accionistas (socios) por desembolsos exigidos.
          Otros deudores.
   III. Inversiones en empresas del grupo y asociadas a corto plazo.
    IV. Inversiones financieras a corto plazo.
     V. Periodificaciones a corto plazo.
    VI. Efectivo y otros activos liquidos equivalentes.
TOTAL ACTIVO (A mas B).

PATRIMONIO NETO Y PASIVO
A) PATRIMONIO NETO
   A-1) Fondos propios.
          I. Capital. Capital escriturado; (capital no exigido).
         II. Prima de emision.
        III. Reservas.
         IV. (Acciones y participaciones en patrimonio propias).
          V. Resultados de ejercicios anteriores.
         VI. Otras aportaciones de socios.
        VII. Resultado del ejercicio.
       VIII. (Dividendo a cuenta).
   A-2) Subvenciones, donaciones y legados recibidos.
B) PASIVO NO CORRIENTE
     I. Provisiones a largo plazo.
    II. Deudas a largo plazo. Con entidades de credito; acreedores por
        arrendamiento financiero; otras deudas a largo plazo.
   III. Deudas con empresas del grupo y asociadas a largo plazo.
    IV. Pasivos por impuesto diferido.
     V. Periodificaciones a largo plazo.
C) PASIVO CORRIENTE
     I. Provisiones a corto plazo.
    II. Deudas a corto plazo. Con entidades de credito; acreedores por
        arrendamiento financiero; otras deudas a corto plazo.
   III. Deudas con empresas del grupo y asociadas a corto plazo.
    IV. Acreedores comerciales y otras cuentas a pagar. Proveedores;
        otros acreedores.
     V. Periodificaciones a corto plazo.
TOTAL PATRIMONIO NETO Y PASIVO (A mas B mas C).
~~~

- The earlier version of this Guide showed a two-sided horizontal layout, gave the non-current block four headings instead of six, and left out the deferred tax lines and the periodificaciones on both sides. The model above is the one in the plan.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966

## Section 8: Bank Reconciliation Patterns

### Spanish Bank Statement Formats

This table is OpenAccountants' own working note on what Spanish banks export. No official page carries it, and the file layouts change without notice. Treat it as a starting point and confirm the columns against the actual file.

| Bank | Format | Key fields |
| --- | --- | --- |
| CaixaBank | Norma 43, also CSV | Fecha operación, Fecha valor, Concepto, Importe, Saldo |
| Banco Santander | Norma 43, CSV, OFX | Fecha, Concepto, Importe, Saldo disponible |
| BBVA | Norma 43, CSV | Fecha, Descripción, Cargo, Abono, Saldo |
| Banco Sabadell | Norma 43, CSV | Fecha movimiento, Concepto, Importe |
| Bankinter | Norma 43, CSV | Fecha, Descripción, Importe |
| Revolut, N26 | CSV | Date, Description, Amount, Currency |

- **Norma 43, also called Cuaderno 43**, is the Spanish inter-bank standard for an electronic statement. It is published by the banking sector, not by a public authority, and no page on an official host sets it out. Most Spanish accounting software imports it.

### Common Spanish Transaction Descriptions

Also OpenAccountants' own pattern library, not an official classification. Every line is a first guess that the supporting document then confirms or overturns.

| Pattern in the concepto | Likely classification |
| --- | --- |
| TRANSFERENCIA, TRANSF | A transfer. Check the direction and the counterparty before deciding |
| RECIBO, ADEUDO | Direct debit: a utility, an insurance premium, social security |
| TARJETA, TPV | Card payment. Check the merchant |
| NOMINA | Payroll payment, account 640 |
| AEAT, AGENCIA TRIBUTARIA | A tax payment. Not a profit and loss item; it clears account 475 |
| SEG. SOCIAL, TGSS | Social security. Employer contributions are account 642; the autónomo's own contribution is a deductible expense of the activity |
| ALQUILER | Rent, account 621. Check whether withholding was applied |
| CUOTA PRESTAMO | Loan instalment. Split the capital, accounts 170 and 520, from the interest, account 662 |
| COMISION, GASTOS | Bank charges, account 626 |
| TRASPASO | Transfer between the client's own accounts. Exclude |
| INGRESO EFECTIVO | Cash deposit. Trace it to the sale it came from |
| RETA | The autónomo's own social security contribution |

## Section 9: Micro-Entity / Small Business Simplifications

### PGC-PYMES Eligibility (must meet 2 of 3 for two consecutive years)

**Every one of these thresholds is printed in the law in words, not in digits, so this Guide prints them in words.** Writing them as amounts would put a figure in the Guide that no official page carries.

| Criterion | Small and medium plan, article 2 of Real Decreto 1515/2007 | Microempresa criteria, article 4 of the same decree |
| --- | --- | --- |
| Total assets | Not above four million euros | Not above one million euros |
| Net turnover | Not above eight million euros | Not above two million euros |
| Average employees in the year | Not more than fifty | Not more than ten |

- **The test is two of the three, at the close of each of two consecutive financial years.** The business loses the option if it fails to meet two of the three for two consecutive years. In the year it is set up, meeting two of the three at that year's close is enough.
- **The microempresa criteria are an option inside the small and medium plan, not a third plan.** Article 4 opens them only to a business that has already opted for that plan.
- **A group changes the answer.** Where the business forms part of a group, the test is applied to the group figures, on the terms of the rule on group, multi-group and associated undertakings in the plan.
- **The same amounts appear again in company law, for a different purpose.** Article 257 of the Ley de Sociedades de Capital uses the same three to decide who may draw up an abbreviated balance sheet and abbreviated statement of changes in equity, and adds that where the abbreviated balance sheet may be drawn up, neither the statement of changes in equity nor the cash flow statement is compulsory.
- Sources: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966 and https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

**The other two company law thresholds, also in words**

| Test | Total assets | Net turnover | Average employees |
| --- | --- | --- | --- |
| Abbreviated profit and loss account, article 258 of the Ley de Sociedades de Capital | Not above eleven million four hundred thousand euros | Not above twenty two million eight hundred thousand euros | Not more than two hundred and fifty |
| Exemption from the audit, article 263 of the Ley de Sociedades de Capital | Not above two million eight hundred and fifty thousand euros | Not above five million seven hundred thousand euros | Not more than fifty |

- Both are the same two-of-three test over two consecutive financial years, and both are lost the same way.
- **The audit exemption is an exemption from the general rule, not a concession.** Article 263.1 starts from the position that the annual accounts and, where there is one, the management report, must be reviewed by an auditor.
- **Being small does not always save you.** Two independent triggers put a small company back into audit.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2021-1351 |
| Public subsidies or grants received in a financial year, accumulated, above which the accounts of that year and of the years in which the assisted operations are carried out must be audited | EUR 600,000 | "por un importe total acumulado superior a 600.000 euros, estarán obligadas a someter a auditoría las cuentas anuales correspondientes a dicho ejercicio" |
| Contracts with the public sector in a financial year, accumulated, above which the accounts of that year AND of the following year must be audited | EUR 600,000 | "de 26 de febrero de 2014, por un importe total acumulado superior a 600.000 euros, y este represente más del 50" |
| Share of the company's net annual turnover those contracts must also exceed | 50% | "superior a 600.000 euros, y este represente más del 50 % del importe neto de su cifra anual de negocios" |

- The two contract conditions are cumulative: the accumulated amount AND the share of turnover. The subsidies condition stands on the amount alone.
- The two triggers cover different periods, and the difference is in the decree's own words. Public contracts catch "las cuentas anuales correspondientes a dicho ejercicio social y las del siguiente a este", that year and the one after it. Subsidies catch that year and the years in which the assisted operations are carried out. Do not read one period across both.
- The size test is not limited to companies. Disposicion adicional primera of the same decree applies it to "las entidades, cualquiera que sea su naturaleza juridica", provided they must draw up annual accounts under the financial reporting framework that applies to them, so an association or a foundation is tested on the same amounts.

### Simplifications

| Requirement | Microempresa criteria | Small and medium plan | Full plan |
| --- | --- | --- | --- |
| Chart of accounts | The cuadro of the small and medium plan | The cuadro of the small and medium plan, seven groups | The full cuadro, nine groups |
| Balance sheet | Abbreviated where article 257 of the Ley de Sociedades de Capital is met | Abbreviated where article 257 is met | Full |
| Profit and loss account | Abbreviated where article 258 is met | Abbreviated where article 258 is met | Full |
| Estado de cambios en el patrimonio neto | Not compulsory where the abbreviated balance sheet may be drawn up | Part of the plan's models | Required |
| Estado de flujos de efectivo | Not compulsory where the abbreviated balance sheet may be drawn up | Not in the plan's models | Required unless the abbreviated balance sheet may be drawn up |
| Memoria | Simplified | Simplified | Full |
| Leases | A microempresa charges the instalment on a finance lease to profit and loss, and recognises the asset at the amount paid when the purchase option is exercised, with the lease information given in the memoria | Finance and operating distinction | Finance and operating distinction |
| Audit | Exempt only on the article 263 test, and only if neither audit trigger above applies | Same test | Same test |
| Filing at the Registro Mercantil | Required, on the abbreviated models where they apply | Required | Required |

- Sources: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966 and https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

### Autónomo (Self-Employed) Bookkeeping

| Obligation | Detail |
| --- | --- |
| Libro registro de ventas e ingresos, or de ingresos for a professional | Every item of income, with the date, the invoice number, the customer and the amount |
| Libro registro de compras y gastos, or de gastos for a professional | Every expense, with the date, the invoice number, the supplier and the amount |
| Libro registro de bienes de inversión | The fixed asset register. Required in every case listed in article 68 of Real Decreto 439/2007, and also for a módulos taxpayer who deducts depreciation |
| Libro registro de provisiones de fondos y suplidos | A professional only |
| The VAT registers | A separate set under article 62 of Real Decreto 1624/1992; see `es-vat-return` |
| Retention | The commercial period and the tax period both apply; see "How long to keep the books" |
| Electronic supply of the VAT registers | Compulsory for a monthly VAT filer. The turnover that forces a monthly period is in the table in "The VAT registers" |
| Full accounting instead | An autónomo whose business activity is mercantile and who is in the normal modality of direct estimation keeps Código de Comercio accounting, not registers (article 68.2) |

- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820

## Section 10: Interaction with the other Spain Guides

| Guide | How the bookkeeping connects |
| --- | --- |
| `es-income-tax` | The rendimiento neto of the activity starts from the recorded income and expenses. The withholding rates on professional invoices, the per-day meal limits and the simplified depreciation table are all there, and this Guide agrees with it |
| `es-corporate-tax` | The resultado contable from the cuenta de pérdidas y ganancias is the starting point for the corporate tax base. The non-deductible items in Section 4 are the adjustments |
| `es-vat-return` | The VAT accounts, 472 soportado, 477 repercutido, 4700 and 4750, feed the periodic return. The VAT registers, the boxes and the electronic supply deadlines are there, not here |
| `es-modelo-111` | Withholdings on professional fees and on salaries: account 4751 in the payer's books, account 473 for the recipient. Declared periodically and summarised for the year |
| `es-rental-income` | Rental income and expenses are a different income category, not business income, unless the letting is itself the activity. Depreciation on a let building is at the rate in the table below |
| `es-social-contributions` | The employer's cuotas, account 642, and the autónomo's own contribution. Both are deductible for income tax |
| `es-estimated-tax` | The quarterly payments on account, and the contested módulos entry limits |
| `es-autonomous-worker` | Registration, the alta, and the obligations calendar |
| `spain-financial-statements` | The same annual accounts seen from the filing side: the models, the memoria, the abbreviated forms and the audit. Where that Guide and this one both answer, prefer it for anything after the trial balance and this one for anything before it |
| `spain-einvoice` | What the invoicing software itself must do: the SIF rules, VERI*FACTU and the business to business mandate. This Guide gives only what an invoice must carry under Real Decreto 1619/2012 |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Yearly depreciation on a let building, on the greater of the two values the article names, excluding the land | 3% | "si no excede del resultado de aplicar el 3 por ciento sobre el mayor de los siguientes valores" |

## The method, step by step

1. **Settle which law binds the client before opening a ledger.** A company is an empresario and keeps the Libro de Inventarios y Cuentas anuales and the Libro Diario under articles 25 and 28 of the [Código de Comercio](https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627). An individual is tested instead under article 68 of [Real Decreto 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820): mercantile business plus normal modality means full accounting, everything else means the registers listed in Section 1.
2. **Pick the plan and the models.** Check the two-of-three test in article 2 of [Real Decreto 1515/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966) over the two preceding financial years, then check article 4 for the microempresa criteria. Record which years you tested and what the figures were, because losing the option also takes two years.
3. **Set the chart of accounts from the cuadro de cuentas** in part four of [Real Decreto 1514/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884), and keep the standard codes even though article 2 of that decree and article 3.1 of the small and medium decree both say the numbering is not binding.
4. **Post on accruals, net of VAT**, with the VAT to accounts 472 and 477. Check every expense against the two gates in Section 4: is it refused outright by article 15 of [Ley 27/2014](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328), and is there a full invoice under article 6 of [Real Decreto 1619/2012](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696)?
5. **Check the payment route, not only the invoice.** No operation with a business or professional on either side may be settled in cash at or above the limit in the table in Section 4 (article 7 of [Ley 7/2012](https://www.boe.es/buscar/act.php?id=BOE-A-2012-13416)), and the taxpayer's own meal costs are deductible only if paid electronically.
6. **Depreciate on the right table.** Company or normal modality: the table in article 12.1.a of [Ley 27/2014](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328). Simplified modality: the simplified table on the [Agencia Tributaria page](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html). Never take a coefficient from one table into the other.
7. **Close the year on the statutory clock.** Formulate within three months, approve at the ordinary general meeting inside the first six months, file at the Registro Mercantil within the month after approval, and legalise the books telematically within four months of the close under article 18 of [Ley 14/2013](https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074). The filing deadline is the one with a fine on it; the amounts are in Section "The annual accounts".
8. **Archive for the longest period that applies**: six years from the last entry under article 30 of the [Código de Comercio](https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627), four years for tax under article 66 of [Ley 58/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186), ten years where a loss is still being carried forward.

## Ask the client first

- **Is the client a company, or an individual?** And if an individual, is the activity a business or a profession, and is it mercantile? Those three answers pick between full double entry, three registers and four registers.
- **Which modality of direct estimation, and what was last year's turnover?** The simplified modality has a turnover cliff and a different depreciation table. Ask for the figure across all the client's activities together, not just this one.
- **What are the total assets, the net turnover and the average headcount for each of the last two financial years?** Every plan, model and audit question turns on those three, tested at the close of each of two consecutive years.
- **Did the company receive public subsidies or public sector contracts in the year?** Either can force an audit on a company that is otherwise under the size test.
- **Is the client inside a group?** Group figures replace the company's own in every size test.
- **Have the books been legalised, and were the last accounts filed?** Ask for the registry validation code and the filing receipt. A missed filing accrues a fine for each year of delay and closes the registry sheet.
- **What is the SL's share capital?** An SL incorporated with capital below three thousand euros has a different and stricter legal reserve rule, and on liquidation its members answer for the shortfall up to that same amount.

## When to refuse or refer

- **Anything in the foral territories.** The Basque provinces and Navarre have their own accounting and tax rules with their own official sites. This Guide is written from state law and does not cover Bizkaia, Gipuzkoa, Araba or Navarra.
- **Consolidated accounts, and the audit of them.** Article 42 of the Código de Comercio and the consolidation rules are outside this Guide.
- **Whether a specific company must be audited.** Two of the triggers are outside the size test, other laws add more, and the consequence of getting it wrong falls on the directors. Refer it to the auditor or to the client's lawyer.
- **The content, the format and the electronic supply of the VAT registers.** That is `es-vat-return`. Answering it from here will produce the wrong boxes.
- **Whether a client may stay in módulos.** Two official sources disagree on the income limits. See `es-estimated-tax`, and do not decide it on one source.
- **A sector plan.** Construction, insurance, non-profits, health service entities and others have adapted plans that override parts of the general one.
- **Any figure printed in the law in words.** Where this Guide writes an amount in words it is because no official page prints the digits. Do not convert it into a number to feed a calculation without an accountant confirming it.
- **Bank file layouts and transaction patterns.** Section 8 is our own working note, not an official standard, and it changes.

## Sources

- Código de Comercio: https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627
- Ley de Sociedades de Capital, Real Decreto Legislativo 1/2010: https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544
- Plan General de Contabilidad, Real Decreto 1514/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884
- Plan General de Contabilidad de Pequeñas y Medianas Empresas, Real Decreto 1515/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966
- Ley 27/2014 del Impuesto sobre Sociedades: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
- Ley 35/2006 del Impuesto sobre la Renta de las Personas Físicas: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
- Reglamento del IRPF, Real Decreto 439/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- Ley 37/1992 del Impuesto sobre el Valor Añadido: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- Reglamento del IVA, Real Decreto 1624/1992: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925
- Reglamento de facturación, Real Decreto 1619/2012: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
- Ley 58/2003 General Tributaria: https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186
- Ley 7/2012, limitation on cash payments: https://www.boe.es/buscar/act.php?id=BOE-A-2012-13416
- Ley 14/2013, telematic legalisation of the books: https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074
- Reglamento de la Ley de Auditoría de Cuentas, Real Decreto 2/2021: https://www.boe.es/buscar/act.php?id=BOE-A-2021-1351
- Agencia Tributaria, tabla de amortización simplificada: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or auditor de cuentas) before filing or acting upon.

> Contributed by OpenAccountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
