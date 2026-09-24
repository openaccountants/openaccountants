---
name: spain-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (cuentas anuales) for a Spanish company. Trigger on phrases like "cuentas anuales", "Registro Mercantil", "depósito de cuentas", "Plan General de Contabilidad", "PGC", "PGC PYMES", "balance", "cuenta de pérdidas y ganancias", "memoria", "auditoría España", "ICAC", or any question about preparing and filing statutory accounts under Spanish commercial law. Covers PGC/PGC-PYMES frameworks, size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spanish annual accounts: the cuentas anuales, the models, the audit and the deposit

How a Spanish company draws up its annual accounts, which official model it must use, which size tests decide the abbreviated forms and the audit, and how the accounts are deposited at the Registro Mercantil. Figures are for tax year 2026. Almost every threshold in this area is printed in the Ley de Sociedades de Capital and in the accounting decrees in WORDS, not in digits, so this Guide prints them in words too: writing them as amounts would put a number in the Guide that no official page carries. The deposit models in force are the ones approved by the resolution of 19 May 2026; the accounting and company law texts are consolidated statutes that carry no year of their own.

## Spain financial statements: Guide version 2.0

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Currency | EUR |
| Filing authority | Registro Mercantil of the province where the registered office is located |
| Primary legislation | Texto Refundido de la Ley de Sociedades de Capital, Real Decreto Legislativo 1/2010; Código de Comercio |
| Supporting legislation | Real Decreto 1514/2007, Plan General de Contabilidad; Real Decreto 1515/2007, Plan General de Contabilidad de Pymes; Ley 22/2015 de Auditoría de Cuentas; Real Decreto 2/2021, its regulation; Real Decreto 1784/1996, Reglamento del Registro Mercantil |
| Accounting standards | Plan General de Contabilidad, or the Plan General de Contabilidad de Pymes with the optional microempresa criteria |
| Financial year | Whatever the articles say. Where the articles are silent, article 26 of the Ley de Sociedades de Capital says the financial year ends on the thirty first of December |
| Formulation deadline | Three months from the close of the financial year (article 253.1) |
| Meeting deadline | The ordinary general meeting is held within the first six months of each financial year (article 164.1) |
| Filing deadline | Within the month following approval of the accounts (article 279.1) |
| Latest ordinary filing | End of July for a company whose year ends on the thirty first of December. DERIVED, not published: no official page prints this date. It is six months (article 164.1) plus one month (article 279.1), and it holds only where the year ends on the thirty first of December AND the meeting is held on the last day of the six month window. A company that approves its accounts in April must deposit them in May, and a year ending on another date moves the whole thing |
| Filing fee | Set by the registry tariff. No page on the official hosts this Guide may cite prints it, so no amount is given here |
| Digital filing | Electronic deposit through the registrars' portal (registradores.org), or on paper at the registry |
| Official models | The models approved by the resolution of 19 May 2026 of the Dirección General de Seguridad Jurídica y Fe Pública: Normal, Abreviado and Pyme |

## Section 2: Reporting Framework

| Entity type | Applicable standard |
| --- | --- |
| Large and medium companies | The full Plan General de Contabilidad, Real Decreto 1514/2007 |
| Small companies meeting the article 2 test of Real Decreto 1515/2007 | The Plan General de Contabilidad de Pymes, or the full plan. The choice must be kept for at least three financial years |
| Microempresa criteria | Article 4 of Real Decreto 1515/2007. Not a third plan: an option inside the Pymes plan, open only to a business that has already opted for it, and taken as a block |
| Companies barred from the Pymes plan | A public interest entity within article 3.5 of Ley 22/2015; a company in a group that formulates or should have formulated consolidated accounts; a company whose functional currency is not the euro; deposit taking financial entities and their managers (article 2.2) |
| Listed groups, consolidated accounts | Where any group company has securities admitted to trading on a regulated market of a Member State, the international standards adopted by European Union regulation apply (article 43 bis.a of the Código de Comercio) |
| Non-listed groups, consolidated accounts | A choice between the Código de Comercio rules and the international standards. Once the international standards are chosen the consolidated accounts must be drawn up on them continuously (article 43 bis.b) |

- **The annual accounts are one unit.** Article 34.1 of the Código de Comercio lists the balance sheet, the profit and loss account, a statement of changes in equity, a cash flow statement and the memoria, and says those documents form a unit. The statement of changes in equity and the cash flow statement are not compulsory where a legal provision says so.
- **They are expressed in euros** (article 34.5), and where the legal provisions are not enough to give a true and fair view the memoria must carry the extra information needed (article 34.3).
- Sources: https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627 and https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966

## Section 3: Size Thresholds

The three size tests below are the ones this Guide owns for the filing and audit questions. `spain-bookkeeping` states the same tests for the choice of accounting plan, in the same words. If the two Guides ever differ, the statute wins and both are wrong.

### Abbreviated accounts (cuentas anuales abreviadas): Art. 257 TRLSC

- **Eligibility condition.** A company may draw up an abbreviated balance sheet and an abbreviated statement of changes in equity if, during two consecutive financial years, it meets at the closing date of each of them at least two of the three circumstances below (article 257.1).
- **It is two of three, not all three,** and it is tested at the CLOSE of each of the two years, not on an average.
- **Losing it also takes two years.** The company loses the facility if it fails to meet two of the circumstances for two consecutive financial years (article 257.1, final paragraph).
- **A new company is tested on one year.** In the first financial year from incorporation, transformation or merger, the company may use the abbreviated forms if it meets at least two of the three at the close of that year (article 257.2).

**Abbreviated balance sheet and abbreviated profit and loss thresholds**  _(Art. 257, Art. 258 TRLSC)_

| Criterion | Abbreviated balance sheet, article 257 | Abbreviated profit and loss account, article 258 |
| --- | --- | --- |
| Total activo (total assets) | Not above four million euros | Not above eleven million four hundred thousand euros |
| Cifra de negocios (net annual turnover) | Not above eight million euros | Not above twenty two million eight hundred thousand euros |
| Empleados (average employees in the year) | Not more than fifty | Not more than two hundred and fifty |

- Every one of the six amounts above is printed in the Ley de Sociedades de Capital in words. The law does not print them as digits anywhere, so neither does this Guide.
- **The two tests are independent.** A company can qualify for the abbreviated profit and loss account and still be barred from the abbreviated balance sheet, and that combination changes what it must file.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

### PGC-PYMES eligibility

- **The same three amounts, a different rule.** Article 2.1 of Real Decreto 1515/2007 opens the Pymes plan to any business, whatever its legal form and whether individual or a company, that during two consecutive financial years meets at the close of each of them at least two of: total assets not above four million euros, net annual turnover not above eight million euros, average employees not more than fifty. The amounts are the same as in article 257 of the Ley de Sociedades de Capital, but the consequence is the accounting plan, not the filing model.
- **A group is tested on group figures.** Where the business is part of a group, the assets, the turnover and the headcount of all the entities in the group are added, with the eliminations and incorporations of the consolidation rules (article 2.1).
- **The choice sticks.** A business inside the scope that opts for one plan or the other must keep the choice for at least three financial years, unless it loses the facility first (article 2.3).
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966

### Micro-entity criteria (within PGC-PYMES)

**Microempresa criteria, article 4 of Real Decreto 1515/2007**

| Criterion | Threshold |
| --- | --- |
| Total activo | Not above one million euros |
| Cifra de negocios | Not above two million euros |
| Empleados | Not more than ten |

- These are printed in the decree in words as well ("el millón de euros", "los dos millones de euros", "diez").
- **The criteria live in article 4, not article 2.** The earlier version of this Guide cited article 2 for them. Article 2 is the scope of the Pymes plan; article 4 is the microempresa option inside it.
- **They are an option and they are taken together.** A business that opts for them must follow all of them jointly, and must keep the choice for at least three financial years.
- **The test itself is the same shape:** two of the three, at the close of each of two consecutive financial years, group figures where there is a group, one year only in the year of incorporation or transformation.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966

## Section 4: Required Financial Statements

| Document | Micro and small (abbreviated) | Medium and large (normal) |
| --- | --- | --- |
| Balance (balance sheet) | Required, abbreviated model where article 257 is met | Required, normal model |
| Cuenta de pérdidas y ganancias (profit and loss) | Required, abbreviated model where article 258 is met | Required, normal model |
| Estado de cambios en el patrimonio neto | Not compulsory where the abbreviated balance sheet may be drawn up (article 257.3) | Required |
| Estado de flujos de efectivo | Not compulsory where the abbreviated balance sheet may be drawn up (article 257.3) | Required |
| Memoria (notes) | Required, abbreviated memoria, ten notes | Required, normal memoria, twenty five notes |
| Informe de gestión (management report) | Not required where the abbreviated balance sheet and abbreviated statement of changes in equity are drawn up (article 262.3) | Required |
| Informe de auditoría (audit report) | Where the company is obliged to audit by a legal provision, or an auditor was appointed on the minority's request or voluntarily and the appointment was registered (article 279.1). Being inside the article 263.2 size exception is NOT enough on its own: check the triggers outside the size test in Section 10 first | Required |

- **The exemption from the estado de cambios and the estado de flujos hangs on the BALANCE SHEET test, not on the profit and loss test.** A company that qualifies for the abbreviated profit and loss account but not for the abbreviated balance sheet must still file both statements.
- **A company drawing up abbreviated accounts that has acquired its own shares or its parent's shares** must still give the information required by article 148.d in the memoria, even though it files no management report (article 262.3).
- **Where the abbreviated profit and loss account may NOT be drawn up**, the management report must state the average payment period to suppliers, and where that period is above the maximum in the late payment rules, the measures planned to bring it down (article 262.1).
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

## Section 5: Year-End Adjustments Checklist

The valuation rules cited are the normas de registro y valoración in part two of the Plan General de Contabilidad, Real Decreto 1514/2007. They are numbered the same way in the Pymes plan for the items the Pymes plan keeps.

| # | Adjustment | Spain-specific notes |
| --- | --- | --- |
| 1 | Amortización (depreciation) | Valuation rule 2.ª, inmovilizado material. Systematic over the useful life. A small company often aligns the accounting rate with the tax table, which is a choice, not a rule |
| 2 | Provisiones (provisions) | Valuation rule 15.ª, provisiones y contingencias. Present obligation, probable outflow, reliable estimate |
| 3 | Periodificación (accruals and prepayments) | Accrual basis. The balance sheet carries periodificaciones at both short and long term on both sides |
| 4 | Deterioro de créditos comerciales (bad debts) | Valuation rule 9.ª, instrumentos financieros, decides the accounting impairment on the evidence available. The six month rule is the TAX test in article 13.1.a of Ley 27/2014 for deductibility, not the accounting trigger. Do not use one for the other |
| 5 | Existencias (inventory) | Valuation rule 10.ª. Lower of cost and net realisable value, with weighted average cost or first in first out |
| 6 | Impuesto diferido (deferred tax) | Valuation rule 13.ª, impuestos sobre beneficios. Temporary differences. The rate to apply is the corporate tax rate the company expects: take it from `es-corporate-tax`, which carries the rate table and the transitional step down, not from this Guide |
| 7 | Diferencias de cambio (foreign currency) | Valuation rule 11.ª, moneda extranjera. Monetary items retranslated at the closing rate |
| 8 | Indemnizaciones por despido (severance) | Provision where there is a present obligation, for example a communicated restructuring plan |
| 9 | Vacaciones devengadas (holiday accrual) | Provision for untaken leave and the social security on it |
| 10 | Subvenciones de capital (capital grants) | Valuation rule 18.ª. A non-refundable grant is recognised directly in equity and taken to profit and loss over the life of the asset |
| 11 | Arrendamientos financieros (finance leases) | Valuation rule 8.ª, arrendamientos. Capitalised, substance over form. A business using the microempresa criteria does NOT capitalise: it charges the instalments of the year to profit and loss and recognises the asset when the purchase option is exercised, and explains the lease in the memoria (article 4.3, rule 1.ª of Real Decreto 1515/2007) |
| 12 | Impuesto sobre Sociedades (corporate tax charge) | Current tax plus the movement on deferred tax. The accounting result is the starting point for the tax base; the adjustments belong to `es-corporate-tax` |
| 13 | Hechos posteriores al cierre (events after the reporting date) | Valuation rule 23.ª. An event that shows a condition already existing at the close changes the accounts; one that does not is disclosed in the memoria |

- Sources: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884 and https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966

## Section 6: Cuenta de Pérdidas y Ganancias Format (P&L)

This is the NORMAL model in part three of the Plan General de Contabilidad, by nature, with the prior year alongside and the feeding account numbers in the plan's own left column. The abbreviated model is NOT this block with the sub-letters removed. It carries lines one to seventeen with no sub-letters at all, but it has no line eighteen, no OPERACIONES CONTINUADAS block and no OPERACIONES INTERRUMPIDAS block, and its four subtotals are lettered differently: A) RESULTADO DE EXPLOTACION, B) RESULTADO FINANCIERO, C) RESULTADO ANTES DE IMPUESTOS (A mas B) and D) RESULTADO DEL EJERCICIO (C mas 17). Heading an abbreviated account "A.1)" is a wrong line on an official model. The Pymes model is different again and is set out in `spain-bookkeeping`.

~~~
A) OPERACIONES CONTINUADAS.

 1. Importe neto de la cifra de negocios.
    a) Ventas.
    b) Prestaciones de servicios.
 2. Variacion de existencias de productos terminados y en curso de fabricacion.
 3. Trabajos realizados por la empresa para su activo.
 4. Aprovisionamientos.
    a) Consumo de mercaderias.
    b) Consumo de materias primas y otras materias consumibles.
    c) Trabajos realizados por otras empresas.
    d) Deterioro de mercaderias, materias primas y otros aprovisionamientos.
 5. Otros ingresos de explotacion.
    a) Ingresos accesorios y otros de gestion corriente.
    b) Subvenciones de explotacion incorporadas al resultado del ejercicio.
 6. Gastos de personal.
    a) Sueldos, salarios y asimilados.
    b) Cargas sociales.
    c) Provisiones.
 7. Otros gastos de explotacion.
    a) Servicios exteriores.
    b) Tributos.
    c) Perdidas, deterioro y variacion de provisiones por operaciones comerciales.
    d) Otros gastos de gestion corriente.
 8. Amortizacion del inmovilizado.
 9. Imputacion de subvenciones de inmovilizado no financiero y otras.
10. Excesos de provisiones.
11. Deterioro y resultado por enajenaciones del inmovilizado.
    a) Deterioros y perdidas.
    b) Resultados por enajenaciones y otras.
A.1) RESULTADO DE EXPLOTACION (uno a once).

12. Ingresos financieros.
    a) De participaciones en instrumentos de patrimonio.
       a 1) En empresas del grupo y asociadas.
       a 2) En terceros.
    b) De valores negociables y otros instrumentos financieros.
       b 1) De empresas del grupo y asociadas.
       b 2) De terceros.
13. Gastos financieros.
    a) Por deudas con empresas del grupo y asociadas.
    b) Por deudas con terceros.
    c) Por actualizacion de provisiones.
14. Variacion de valor razonable en instrumentos financieros.
    a) Valor razonable con cambios en perdidas y ganancias.
    b) Transferencia de ajustes de valor razonable con cambios en el patrimonio neto.
15. Diferencias de cambio.
16. Deterioro y resultado por enajenaciones de instrumentos financieros.
    a) Deterioros y perdidas.
    b) Resultados por enajenaciones y otras.
A.2) RESULTADO FINANCIERO (doce a dieciseis).

A.3) RESULTADO ANTES DE IMPUESTOS (A.1 mas A.2).

17. Impuestos sobre beneficios.
A.4) RESULTADO DEL EJERCICIO PROCEDENTE DE OPERACIONES CONTINUADAS (A.3 mas 17).

B) OPERACIONES INTERRUMPIDAS.

18. Resultado del ejercicio procedente de operaciones interrumpidas neto de impuestos.
A.5) RESULTADO DEL EJERCICIO (A.4 mas 18).
~~~

- **Line eighteen is part of the model.** The earlier version of this Guide showed block B with no line in it, so the reader could not see where the discontinued result is posted.
- **Line four has four sub-letters, not three,** and line six has three, not two. The earlier version left out the impairment of goods and raw materials and the personnel provisions line.
- **Line twelve is the only line with a second level.** Both a) and b) split again into group and associated undertakings on one side and third parties on the other. No other line in the normal model goes below a letter.
- Line seventeen may be positive or negative; the plan marks it so.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884

## Section 7: Balance Format (Balance Sheet)

This is the NORMAL model in part three of the Plan General de Contabilidad, as amended by Real Decreto 1/2021 for the A-2 subgroup. It is one vertical statement in two blocks, not two facing columns, and the two totals must agree. The abbreviated model keeps the same letters and roman numerals, except that the A-2 subgroup is shown as a single line, and drops most of the arabic sub-items.

~~~
ACTIVO.

A) ACTIVO NO CORRIENTE.
     I. Inmovilizado intangible.
    II. Inmovilizado material.
   III. Inversiones inmobiliarias.
    IV. Inversiones en empresas del grupo y asociadas a largo plazo.
     V. Inversiones financieras a largo plazo.
    VI. Activos por impuesto diferido.
B) ACTIVO CORRIENTE.
     I. Activos no corrientes mantenidos para la venta.
    II. Existencias.
   III. Deudores comerciales y otras cuentas a cobrar.
    IV. Inversiones en empresas del grupo y asociadas a corto plazo.
     V. Inversiones financieras a corto plazo.
    VI. Periodificaciones a corto plazo.
   VII. Efectivo y otros activos liquidos equivalentes.
TOTAL ACTIVO (A mas B).

PATRIMONIO NETO Y PASIVO.

A) PATRIMONIO NETO.
   A-1) Fondos propios.
          I. Capital. Capital escriturado; (capital no exigido).
         II. Prima de emision.
        III. Reservas. Legal y estatutarias; otras reservas.
         IV. (Acciones y participaciones en patrimonio propias).
          V. Resultados de ejercicios anteriores. Remanente;
             (resultados negativos de ejercicios anteriores).
         VI. Otras aportaciones de socios.
        VII. Resultado del ejercicio.
       VIII. (Dividendo a cuenta).
         IX. Otros instrumentos de patrimonio neto.
   A-2) Ajustes por cambios de valor.
          I. Activos financieros a valor razonable con cambios en el
             patrimonio neto.
         II. Operaciones de cobertura.
        III. Otros.
   A-3) Subvenciones, donaciones y legados recibidos.
B) PASIVO NO CORRIENTE.
     I. Provisiones a largo plazo.
    II. Deudas a largo plazo.
   III. Deudas con empresas del grupo y asociadas a largo plazo.
    IV. Pasivos por impuesto diferido.
     V. Periodificaciones a largo plazo.
C) PASIVO CORRIENTE.
     I. Pasivos vinculados con activos no corrientes mantenidos para la venta.
    II. Provisiones a corto plazo.
   III. Deudas a corto plazo.
    IV. Deudas con empresas del grupo y asociadas a corto plazo.
     V. Acreedores comerciales y otras cuentas a pagar.
    VI. Periodificaciones a corto plazo.
TOTAL PATRIMONIO NETO Y PASIVO (A mas B mas C).
~~~

- **Five headings the earlier version of this Guide left out**, which is why its roman numerals ran wrong: activos no corrientes mantenidos para la venta in current assets, pasivos vinculados con those assets in current liabilities, periodificaciones a largo plazo in non-current liabilities, and the dividendo a cuenta and otros instrumentos de patrimonio neto lines in fondos propios. The A-2 subgroup was also shown flat, with none of its three roman numerals.
- **Assets are split by their function,** not by their label. Article 35.1 of the Código de Comercio puts in current assets what the business expects to sell, consume or realise within its normal operating cycle, and generally anything falling due or expected to be realised within one year of the closing date. Everything else is non-current.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884

## Section 8: Memoria (Notes to Accounts)

The memoria completes, expands and comments on the other documents (article 259 of the Ley de Sociedades de Capital). There are two content lists in the Plan General de Contabilidad, and they are lists of NOTES, not of topics chosen by the preparer.

| Note | Abbreviated memoria (ten notes) | Normal memoria (twenty five notes) |
| --- | --- | --- |
| 1 | Actividad de la empresa | Actividad de la empresa |
| 2 | Bases de presentación de las cuentas anuales | Bases de presentación de las cuentas anuales |
| 3 | Normas de registro y valoración | Aplicación de resultados |
| 4 | Inmovilizado material, intangible e inversiones inmobiliarias | Normas de registro y valoración |
| 5 | Activos financieros | Inmovilizado material |
| 6 | Pasivos financieros | Inversiones inmobiliarias |
| 7 | Fondos propios | Inmovilizado intangible |
| 8 | Situación fiscal | Arrendamientos y otras operaciones de naturaleza similar |
| 9 | Operaciones con partes vinculadas | Instrumentos financieros |
| 10 | Otra información, which carries the average headcount, off balance sheet arrangements, exceptional items, financial commitments and guarantees, and events after the close | Existencias |
| 11 | Not in the abbreviated memoria | Moneda extranjera |
| 12 | Not in the abbreviated memoria | Situación fiscal |
| 13 | Not in the abbreviated memoria | Ingresos y gastos |
| 14 | Not in the abbreviated memoria | Provisiones y contingencias |
| 15 | Not in the abbreviated memoria | Información sobre medio ambiente |
| 16 | Not in the abbreviated memoria | Retribuciones a largo plazo al personal |
| 17 | Not in the abbreviated memoria | Transacciones con pagos basados en instrumentos de patrimonio |
| 18 | Not in the abbreviated memoria | Subvenciones, donaciones y legados |
| 19 | Not in the abbreviated memoria | Combinaciones de negocios |
| 20 | Not in the abbreviated memoria | Negocios conjuntos |
| 21 | Not in the abbreviated memoria | Activos no corrientes mantenidos para la venta y operaciones interrumpidas |
| 22 | Not in the abbreviated memoria | Hechos posteriores al cierre |
| 23 | Not in the abbreviated memoria | Operaciones con partes vinculadas |
| 24 | Not in the abbreviated memoria | Otra información |
| 25 | Not in the abbreviated memoria | Información segmentada |

- **The abbreviated memoria is not a shortened version of the normal one; it is a different list with different note numbers.** In the abbreviated memoria the tax note is note eight; in the normal memoria it is note twelve. Cross-references in a set of accounts must use the right list.
- **What may not be omitted.** Article 261 of the Ley de Sociedades de Capital lets a company that may draw up an abbreviated balance sheet omit the indications set by regulation, but the first, fifth, sixth, tenth (as to the average number of people employed), fourteenth, fifteenth, nineteenth and twenty first indications of article 260 must always be supplied, and the seventh and twelfth must be given in global terms, together with the name and registered office of the company that draws up the consolidated accounts of the smallest group the company belongs to.
- **The tax note has changed for 2026.** Note twelve of the individual memoria was amended to carry the temporary exemption from recognising deferred tax assets and liabilities arising from the global minimum taxation rules, following the tenth final provision of Ley 7/2024.
- Sources: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884 and https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

## Section 9: Filing Requirements

| Item | Detail |
| --- | --- |
| Filing authority | Registro Mercantil of the registered office (article 279.1 of the Ley de Sociedades de Capital; article 365.1 of the Reglamento del Registro Mercantil) |
| Who must file | Directors of a sociedad anónima, a sociedad de responsabilidad limitada, a comanditaria por acciones and a sociedad de garantía recíproca, pension funds, and generally any trader required to publish accounts. Liquidators file the annual liquidation statement. Any other registered trader may file voluntarily (article 365) |
| Filing method | Electronic deposit through the registrars' portal, or on paper at the registry |
| Formulation deadline | Directors formulate the accounts, the management report and the proposed appropriation of the result within three months of the close (article 253.1), and all directors sign them |
| Meeting approval deadline | The ordinary general meeting is held within the first six months of each financial year. The meeting is valid even if convened or held out of time (article 164) |
| Filing deadline | Within the month following approval (article 279.1) |
| Latest ordinary filing | End of July for a company whose year ends on the thirty first of December. DERIVED, not published: six months to the meeting plus one month to the deposit. The statutory deadline is one month from APPROVAL, so an earlier meeting brings the deposit forward, and a year ending on another date moves it entirely |
| Documents to file | Signed application; notarially attested certificate of the approval and appropriation resolutions, stating whether any document was drawn up in abbreviated form and why, and that all directors signed; one copy of the accounts; one copy of the management report; one copy of the audit report where the company is audited or an auditor was appointed by the minority; the own shares document where required; a certificate that the deposited accounts are the audited ones (article 366.1) |
| Extra declarations in the model | The identification of the beneficial owner (titularidad real), and, in the normal model, the new IP sheet for the public country by country corporate tax report |
| Certification wording for 2026 | The directors must state in the approval certificate whether they used the option to re-formulate the accounts in the first additional provision of Real Decreto-ley 4/2025 |
| Registrar's review | Within fifteen days of the presentation entry (article 280.1) the registrar checks only that the documents are the ones the law requires, that they were properly approved and that the required signatures are there (article 280.1; scope of the review under article 368.1) |
| Presentation entry | Valid for five months (article 367) |
| Format | The models approved by the resolution of 19 May 2026, mandatory for accounts presented for deposit after its publication in the Boletín Oficial del Estado |
| Activity code | The CNAE-2025 classification only. Every reference to the previous 2009 classification was removed from the models and from the error tests |
| Language | Spanish, or a co-official language of the autonomous community |
| Retention by the registry | Six years (article 280.2) |
| Publicity | Anyone may obtain information on all deposited documents (article 281), by registrar's certificate or by copy (article 369) |
| XBRL | The resolution does not impose XBRL on the individual accounts themselves; the digital deposit format is set in its Anexo II. The public country by country report has its own common template and electronic format set by European Union regulation |

- Sources: https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 , https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533 and https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-11581

### Consequences of non-filing

- **Registry closure, and the clock is one year from the YEAR END, not from the filing deadline.** Article 378.1 of the Reglamento del Registro Mercantil closes the company's sheet once a year has passed from the close of the financial year without the duly approved accounts being deposited: the registrar then registers nothing presented after that date until the deposit is made. Article 282 of the Ley de Sociedades de Capital states the closure itself.
- **What still gets through the closure.** Removal or resignation of directors, managers, general managers or liquidators; revocation or renunciation of powers; dissolution of the company and appointment of liquidators; and entries ordered by a judicial or administrative authority (article 282.2; article 378.1).
- **Three ways the closure is held off, and a fourth in the next bullet is the one that matters most.** If only the presentation entry has been made, the provisional closure happens only when that entry lapses (article 378.2). If an appeal is lodged against the suspension or refusal of the deposit, the presentation entry is suspended until the final decision (article 378.3). If an appeal is lodged against the registrar's decision on a minority request for an auditor, no closure follows for want of that year's accounts until three months have run from the final decision, even if the one year period has already passed (article 378.4).
- **If the meeting did not approve the accounts, there is no closure, but only if you prove it in time.** Where the accounts were not deposited because the general meeting did not approve them, the closure does not follow if that is evidenced by a certificate of the administrative body with notarially legitimated signatures stating the cause, or by an authorised copy of the notarial minutes of the meeting recording the non-approval. To stop the closure the certificate or the copy must reach the Registro Mercantil BEFORE the one year period in article 378.1 expires, and the situation must be shown to persist every six months by one of those means. Those certificates and minutes are themselves registered and published in the Boletín Oficial del Registro Mercantil (article 378.5).
- **None of that excuses the later years.** Where article 378.3, 378.4 or 378.5 applies, the duty to deposit the accounts of later financial years still stands (article 378.6).
- **The closure lasts until it is cured.** It persists until the outstanding accounts are deposited, or until the failure to approve them is proved at any time in the form article 378.5 requires (article 378.7).
- **How the fine starts.** In the first month of each year the registrars send the list of companies that did not file to the Dirección General, which passes it to the Instituto de Contabilidad y Auditoría de Cuentas in the second month of the year for the penalty file to be opened (article 371).

**The fine for filing late (article 283 of the Ley de Sociedades de Capital)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| Fine on the company, lower end of the range | EUR 1,200 | "una multa por importe de 1.200 a 60.000 euros por el Instituto de Contabilidad y Auditoría de Cuentas" |
| Fine on the company, upper end of the range | EUR 60,000 | "una multa por importe de 1.200 a 60.000 euros por el Instituto de Contabilidad y Auditoría de Cuentas" |
| Annual turnover of the company or group above which the ceiling rises | EUR 6,000,000 | "Cuando la sociedad o, en su caso, el grupo de sociedades tenga un volumen de facturación anual superior a 6.000.000 euros" |
| The raised ceiling, for each year of delay | EUR 300,000 | "el límite de la multa para cada año de retraso se elevará a 300.000 euros" |

- **Who is fined.** The company, not the directors, and the fine is imposed by the Instituto de Contabilidad y Auditoría de Cuentas.
- **How it is sized.** By the company's total assets and its sales figure, both taken from the last year declared to the tax administration. The company must supply those figures; not supplying them counts against it. Where they are not available the fine is set from the share capital, which the registry supplies (article 283.2).
- **Filing before the penalty file is opened cuts it.** The fine is then imposed at its minimum grade and reduced by fifty per cent (article 283.3). The statute writes that reduction in words, so this Guide does too.
- **These infringements prescribe in three years** (article 283.4).
- This is the only one of the three deadlines that carries a fine. Missing the three month formulation deadline or the six month meeting deadline has consequences for the directors, but no fine under this article.

## Section 10: Audit Requirements

### Mandatory audit (Art. 263 TRLSC)

- **The starting point is that everyone is audited.** Article 263.1 says the annual accounts and, where there is one, the management report must be reviewed by an auditor. Article 263.2 is an EXCEPTION to that rule, not a concession granted to small companies.
- **The exemption condition.** A company is excepted if, during two consecutive financial years, it meets at the closing date of each of them at least two of the three circumstances below. It loses the facility if it fails to meet two of them for two consecutive years (article 263.2).
- **A new company is tested on one year.** In the first financial year from incorporation, transformation or merger, the company is excepted if it meets at least two of the three at the close of that year (article 263.3).

**Audit exemption thresholds**  _(Art. 263 TRLSC)_

| Criterion | Threshold for the exemption |
| --- | --- |
| Total activo (total assets) | Not above two million eight hundred and fifty thousand euros |
| Cifra neta de negocios (net annual turnover) | Not above five million seven hundred thousand euros |
| Número medio de empleados (average employees in the year) | Not more than fifty |

- All three are printed in the Ley de Sociedades de Capital in words. The earlier version of this Guide printed them as amounts and stated them the wrong way round, as thresholds a company must EXCEED to be audited, with a total row that did not add up. The statute frames them as ceilings a company must stay at or below, two out of three, for two years running, in order to escape the audit.
- **Cessation of the audit obligation, and this sentence is a reading, not the statute's words.** Article 263.2 states the exception and states how the facility is lost; it does not spell out the return journey. This Guide takes it that a company that was audited and then meets two of the three at the close of two consecutive years falls back inside the exception from then on, which is the natural reading of the same sentence. An accountant should confirm that before relying on it, because nothing in article 263 says it in those terms.
- Source: https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

### Always subject to audit (regardless of size)

The first additional provision of Ley 22/2015 says these entities must be audited in any case, whatever their legal form:

- Entities that issue securities admitted to trading on official secondary securities markets or on multilateral trading facilities.
- Entities that issue bonds in a public offering.
- Entities habitually engaged in financial intermediation, and in any case credit institutions, investment firms, market operators, the central securities depository, central counterparties, the stock exchange company, investment guarantee fund managers and other financial entities, including collective investment schemes and securitisation funds and their managers, registered with the Banco de España or the Comisión Nacional del Mercado de Valores.
- Entities whose objects are activities under the private insurance supervision law, within the limits set by regulation, and pension funds and their managing entities.
- Entities that receive subsidies or aid, or that carry out works, supply goods or provide services to the State and other public bodies, within the limits set by the Government by royal decree.
- Any other entity that exceeds the limits set by the Government by royal decree, being limits on turnover, total assets and average headcount.

**The two limits the Government set by royal decree**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2021-1351 |
| Subsidies or aid from public budgets or European Union funds received in one financial year, accumulated, above which the accounts must be audited | EUR 600,000 | "por un importe total acumulado superior a 600.000 euros, estarán obligadas a someter a auditoría las cuentas anuales correspondientes a dicho ejercicio" |
| Public sector contracts entered into in one financial year, accumulated, above which the accounts must be audited | EUR 600,000 | "de 26 de febrero de 2014, por un importe total acumulado superior a 600.000 euros, y este represente más del 50" |
| Share of net annual turnover those contracts must ALSO exceed | 50% | "superior a 600.000 euros, y este represente más del 50 % del importe neto de su cifra anual de negocios" |

- **The two contract conditions are cumulative**, the accumulated amount AND the share of turnover. The subsidies condition stands on the amount alone.
- **The years caught are not the same.** Subsidies pull in the accounts of the year of receipt AND the years in which the assisted operations or investments are carried out. Public contracts pull in the accounts of that financial year AND the following one.
- **When it counts as received.** A subsidy counts when it must be recorded in the books; a contract counts when the corresponding right to collect must be recorded.
- **The size limit itself.** The first additional provision of Real Decreto 2/2021 sets the size trigger by reference back to article 263.2 of the Ley de Sociedades de Capital, and extends it to entities of any legal form that must draw up annual accounts. So a non-company entity is tested on the same three amounts.
- **A group that must consolidate** is dealt with by the consolidation rules in the Código de Comercio, which are outside this Guide.

### Auditor qualification

- **Auditor qualification requirement.** Only a natural or legal person entered in the Registro Oficial de Auditores de Cuentas of the Instituto de Contabilidad y Auditoría de Cuentas, meeting the conditions in articles 9 to 11 and providing the financial guarantee in article 27, may carry out a statutory audit (article 8.1 of Ley 22/2015). The register is public and accessible electronically (article 8.2).
- **Who appoints, and for how long.** The general meeting appoints the auditor before the end of the financial year to be audited, for an initial period of not less than three and not more than nine years (article 264.1 of the Ley de Sociedades de Capital). The meeting may not revoke the auditor before the initial period ends without just cause (article 264.3).
- **If the meeting does not appoint in time.** The directors or any shareholder may ask the commercial registrar of the registered office to appoint the auditor (article 265.1).
- **The minority's right in a company that is NOT obliged to audit.** Shareholders holding at least five per cent of the share capital may ask the registrar to appoint an auditor at the company's cost, provided three months have not passed since the close of the financial year concerned (article 265.2).
- Sources: https://www.boe.es/buscar/act.php?id=BOE-A-2015-8147 and https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544

## Section 11: How this Guide fits with `spain-bookkeeping`

Both Guides touch the annual accounts. They are written to agree; if they ever differ, the statute decides and this Guide should be corrected.

| Topic | Which Guide to read |
| --- | --- |
| The books of the Código de Comercio, who must keep them, and how they are written | `spain-bookkeeping` |
| Legalisation of the books at the Registro Mercantil, and the four month deadline | `spain-bookkeeping` |
| The chart of accounts, posting, expense classification, asset versus expense | `spain-bookkeeping` |
| The Pymes models of the balance sheet and the profit and loss account | `spain-bookkeeping` |
| The NORMAL models of the balance sheet and the profit and loss account, and the abbreviated models | This Guide |
| The size tests, stated in the same words in both | `spain-bookkeeping` for choosing the accounting plan; this Guide for the filing model and the audit |
| The memoria, note by note | This Guide |
| The audit: the exemption test, the triggers outside it, the auditor | This Guide |
| Formulate, approve, deposit, the models, the registry closure and the fine | This Guide |
| How long the books and papers are kept | `spain-bookkeeping` |
| The corporate tax adjustments to the accounting result, and the tax rates | `es-corporate-tax` |
| The VAT registers and the return | `es-vat-return` |
| What the invoicing software must do, and the business to business mandate | `spain-einvoice` |

## The method, step by step

1. **Fix the financial year and the two prior years' figures first.** Article 26 of the [Ley de Sociedades de Capital](https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544) ends the year on the thirty first of December where the articles are silent. Write down the total assets, the net turnover and the average headcount at the CLOSE of each of the last two financial years. Every question below turns on those six numbers, and on a group they are the group's, not the company's.
2. **Decide the plan, then the models.** Test article 2 of [Real Decreto 1515/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966) for the Pymes plan and article 4 for the microempresa criteria, then test article 257 of the Ley de Sociedades de Capital for the abbreviated balance sheet and article 258 for the abbreviated profit and loss account. The balance sheet test, not the profit and loss test, is what removes the estado de cambios en el patrimonio neto, the estado de flujos de efectivo and the informe de gestión.
3. **Draw up the statements on the official model.** The normal and abbreviated balance sheet and profit and loss layouts are in part three of [Real Decreto 1514/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884). Article 255 of the Ley de Sociedades de Capital requires the items to appear separately and in the model's order; you may subdivide an item or add a new one whose content is not already covered, and you may group items that are individually irrelevant provided they are shown separately in the memoria (article 256).
4. **Write the memoria against the right list**, ten notes for the abbreviated memoria and twenty five for the normal one, and check what article 261 of the [Ley de Sociedades de Capital](https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544) says may never be omitted.
5. **Settle the audit before the meeting is called.** Apply article 263.2, then check the triggers outside the size test in the additional provisions of [Real Decreto 2/2021](https://www.boe.es/buscar/act.php?id=BOE-A-2021-1351) and the first additional provision of [Ley 22/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-8147). If the company is audited, the auditor must already have been appointed before the end of the year being audited (article 264.1).
6. **Formulate within three months, sign, and let the meeting approve within six months.** Both deadlines are in the Ley de Sociedades de Capital, articles 253.1 and 164.1.
7. **Deposit within the month after approval**, on the models approved by the [resolution of 19 May 2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-11581), with the documents listed in article 366.1 of the [Reglamento del Registro Mercantil](https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533), the beneficial owner declaration, and the statement about the re-formulation option in the approval certificate.
8. **Diary the closure date, not the filing date.** Article 378.1 of the Reglamento del Registro Mercantil closes the sheet one year after the YEAR END, which for a calendar year company is five months after the ordinary filing deadline has already passed.

## Ask the client first

- **What are the total assets, the net turnover and the average headcount at the close of each of the last two financial years?** Three tests hang on them, they are tested at the close and not on an average, and two of three is enough.
- **Is the company part of a group?** Group figures replace the company's own in the accounting plan test, and a company in a group that consolidates cannot use the Pymes plan at all.
- **Did the company receive public subsidies, or contract with the public sector, during the year?** Either can force an audit on a company that sits inside the article 263.2 exception and would otherwise not be audited at all, and the contract trigger also catches the following year.
- **Which financial year do the articles set, and has it ever been changed?** Every deadline in this Guide runs from the close, and a short or changed year moves all of them.
- **Has an auditor been appointed, and when?** The appointment must be made before the end of the year to be audited. An appointment made afterwards does not cure the gap; the registrar appoints instead.
- **Were last year's accounts deposited, and is the registry sheet open?** Ask for the deposit receipt. A closed sheet blocks every other filing the client may be waiting on.

## When to refuse or refer

- **Consolidated accounts.** Article 42 and following of the Código de Comercio, the exemptions from consolidating, and article 43 bis on which framework applies, are outside this Guide.
- **The foral territories.** Bizkaia, Gipuzkoa, Araba and Navarra have their own rules and their own official sites. This Guide is written from state law.
- **Whether a specific company must be audited.** The size test is only one of several routes into an audit, other laws add more, and the consequence of getting it wrong falls on the directors. Refer it to an auditor.
- **Sector adaptations of the accounting plan.** Construction, insurance, non-profit entities, health service entities and others have adapted plans that override parts of the general one.
- **Public interest entities.** The rules on their audit, their audit committee and their reporting are in Ley 22/2015 and are not covered here.
- **The corporate tax return.** The accounting result is the starting point, not the answer. Read `es-corporate-tax`.
- **Any amount printed in the law in words.** Where this Guide writes a threshold in words it is because no official page prints the digits. Do not turn it into a number to feed a calculation without an accountant confirming it.
- **The registry fee, and any quoted cost of filing.** No page on the hosts this Guide may cite prints a tariff.

## Sources

- Código de Comercio: https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627
- Ley de Sociedades de Capital, Real Decreto Legislativo 1/2010: https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544
- Plan General de Contabilidad, Real Decreto 1514/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19884
- Plan General de Contabilidad de Pymes, Real Decreto 1515/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-19966
- Reglamento del Registro Mercantil, Real Decreto 1784/1996: https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533
- Ley 22/2015 de Auditoría de Cuentas: https://www.boe.es/buscar/act.php?id=BOE-A-2015-8147
- Reglamento de la Ley de Auditoría de Cuentas, Real Decreto 2/2021: https://www.boe.es/buscar/act.php?id=BOE-A-2021-1351
- Resolución de 19 de mayo de 2026, models for deposit at the Registro Mercantil: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-11581
- Ley 27/2014 del Impuesto sobre Sociedades: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an auditor de cuentas or asesor fiscal) before filing or acting upon.

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
