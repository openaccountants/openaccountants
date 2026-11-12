---
name: bolivia-income-tax
description: "Bolivia personal income tax for 2026: the RC-IVA (Régimen Complementario al Impuesto al Valor Agregado, 13%) for employees, independent professionals, landlords and investors, under Ley 843 Título II and DS 21531 as consolidated by the Servicio de Impuestos Nacionales (SIN) to 30 September 2026, with the 2026 minimum wage of Bs 3,300 (DS 5516). Covers who pays and what income is taxed, the exclusions (aguinaldo, dividends, severance, pensions), the two-minimum-wage non-taxable amount for employees, the credit for invoices on Form 110, the presumed credits, quarterly Form 610 for independents, employer Form 608, withholding on Form 604, non-domiciled individuals, why independent professionals no longer pay IUE (Ley 1448), the Re-IVA refund, the IGF wealth tax and penalties. Trigger on: RC-IVA, Formulario 610, Formulario 110, Formulario 608, retencion RC-IVA, impuesto a la renta Bolivia, salario minimo 2026, profesional independiente Bolivia, impuesto a las grandes fortunas, IGF, Re-IVA."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bolivia-income-tax"
  jurisdiction: "BO"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Bolivia personal income tax (RC-IVA) for 2026: employees, professionals, landlords v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The law is Ley N° 843 (Texto Ordenado), Título II "Régimen Complementario al Impuesto al Valor Agregado" (arts. 19 to 35), and its regulation DS 21531. This skill reads both in the SIN's consolidated edition "Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, Complementado, actualizado al 30/09/2026", which includes Ley 1448 of 25 July 2022 and DS 4850 (independent professionals moved into the RC-IVA from 2023), DS 5383 (employees' presumed credit cut to one minimum wage) and DS 5563 of 2 March 2026. The SIN edition is for information; the Gaceta Oficial governs. The 2026 national minimum wage (Salario Mínimo Nacional, SMN) is from DS 5516 of 13 January 2026, read in the Gaceta Oficial. Penalties come from the Código Tributario, Ley N° 2492. The RC-IVA period is the month (art. 28); independents file by quarter. Amounts are in bolivianos (Bs).

## Who this applies to

- **Individuals and undivided estates** (art. 22) with Bolivian-source income, whatever their nationality, domicile or residence (arts. 20 and 21). Bolivia taxes by source: income from goods located or used in Bolivia, or from acts done in Bolivia. Diplomats of foreign missions and foreign officials of international bodies are outside, on reciprocity (art. 20).
- **Income taxed** (art. 19): rent of real estate and of movables, rights and concessions (unless the owner is an IUE payer); interest and other returns on capital not subject to IUE; salaries, wages, overtime, bonuses, commissions, allowances, per diems, representation expenses and every other pay in cash or kind; directors' and auditors' fees and the salaries of partners and of a sole owner; any other habitual income not subject to IUE; income from a profession or trade exercised independently (inciso g, added by Ley 1448); and fees of non-domiciled persons for work done in Bolivia (inciso h, also from Ley 1448).
- **Independent professionals are in the RC-IVA, not the IUE.** Ley 1448 added art. 19 g) and struck "the exercise of liberal professions and trades" from the IUE definition of a business (art. 39). DS 4850 removed them from the IUE filing rules. A sole-owner business (empresa unipersonal) remains an IUE payer: see [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md).
- **Not taxed** (art. 19 c; DS 21531 art. 1):
  - dividends and profit distributions from companies and sole-owner businesses that pay IUE, and bonus shares from reinvested profits;
  - interest on fixed-term deposits in bolivianos or UFV for more than 30 days, or in foreign currency or dollar-indexed bolivianos for 3 years or more, and returns on debt securities issued for 3 years or more. Early redemption makes the interest taxable;
  - the Christmas bonus (aguinaldo de navidad);
  - severance and voluntary-retirement benefits paid under labour law. Extra gratuities on leaving are taxed;
  - family, marriage, birth, nursing and funeral subsidies, and social-security pensions and annuities;
  - per diems and representation expenses accounted for with invoices, with any surplus returned;
  - social-security contributions and benefits of the pension system (Ley 065 art. 66, reproduced under art. 19).

**When to refer.** Refer for: transport cooperatives' members (DS 5196), mining-sector withholding, Bolivian diplomatic staff abroad (extra 50% deduction, art. 26 II), heirs and undivided estates in partition, and any IGF case. VAT and the transactions tax that independents also pay on their fees: [bolivia-iva](bolivia-iva.md). Contribution rates to the Gestora and the health funds: [bolivia-social-contributions](bolivia-social-contributions.md) and [bolivia-payroll](bolivia-payroll.md).

## Rates, bands and thresholds

Quick answer: **one rate, 13%**, on monthly taxable income, less credits for the IVA in the person's purchase invoices (Form 110) and a presumed credit. There are no brackets. The figures in bolivianos use the 2026 SMN of Bs 3,300, in force from 1 January 2026.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| RC-IVA rate on taxable income (Ley 843 art. 30) | 13% | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| National minimum wage, public and private sectors, retroactive to 1 January 2026 (DS 5516 art. 23) | Bs 3,300 a month | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281033 |
| Employees: non-taxable minimum, two SMN a month (art. 26 I; DS 21531 art. 8 a), only for employment income (DS 21531 art. 6) | Bs 6,600 a month | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Employees: presumed credit, 13% of one SMN (DS 21531 art. 8 c 2, text of DS 5383) | Bs 429 a month | 2026 | same |
| Independents and landlords: presumed credit, 13% of two SMN for each month (DS 21531 art. 9 c 2) | Bs 858 a month; Bs 2,574 a quarter | 2026 | same |
| Credit for purchase invoices (DS 21531 arts. 8 and 9): 13% of invoices in the person's name, no more than 120 days old (before delivery to the employer, or before the quarter's end for independents) | 13% of the invoice amount | 2026 | same |
| Independents: income from IVA-taxed operations is the month's total sales less the 13% IVA in them (DS 21531 art. 9 a) | Sales less 13% | 2026 | same |
| Anticresis (antichretic) contracts: presumed income (art. 27; DS 21531 art. 7) | 10% a year of the contract amount, one twelfth a month | 2026 | same |
| Withholding on payments by legal persons to individuals without an invoice, for rent, directors' fees, habitual income, independent work or non-domiciled work (DS 21531 art. 11) | 13% of the full amount, final | 2026 | same |
| Withholding on interest paid to individuals who do not show a NIT (DS 21531 art. 12) | 13% of the full amount | 2026 | same |
| Re-IVA cash refund for individuals with average monthly income up to Bs 9,000, on electronically issued purchase invoices (Ley 1355 arts. 2 and 3) | Up to 5% of the price | 2026 | same |
| IGF wealth tax threshold: net fortune at 31 December (Ley 1357 art. 5) | Above Bs 30,000,000 | 2026 | same |
| IGF rates on the whole base, less a fixed discount (Ley 1357 art. 9) | Bs 30,000,001 to 40,000,000: 1.4% less Bs 150,000; Bs 40,000,001 to 50,000,000: 1.9% less Bs 350,000; above Bs 50,000,000: 2.4% less Bs 600,000 | 2026 | same |
| Omission of payment penalty (Ley 2492 art. 165, text of Ley 1448) | 60% of the updated omitted tax | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/168844 |
| IGF omission of payment (Ley 1357 art. 15) | 200% of the omitted tax | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Late interest, in UFV at the due date (Ley 2492 art. 47) | 4% a year for years 1 to 4; 6% for years 5 to 7; 10% from year 8 | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf |

## The base

**Employees** (art. 25; DS 21531 arts. 5 and 8). The employer computes the tax for each employee every month:

1. Start from all pay of the month (art. 19 d), excluding the items listed as not taxed (aguinaldo, severance, subsidies).
2. Deduct the employee's social-security contributions and other contributions required by social laws (art. 25; DS 21531 art. 5). The rates are in [bolivia-social-contributions](bolivia-social-contributions.md); take the amount from the payslip.
3. Deduct the non-taxable minimum of two SMN, Bs 6,600 in 2026. If the deductions exceed the pay, the base is zero.
4. Apply 13%.
5. Credit, in this order: 13% of the invoices the employee hands to the employer on Form 110 by the 20th of the month (in the employee's name, signed, at most 120 days old, ICE excluded); the presumed credit of 13% of one SMN, Bs 429; then the employee's updated balance from earlier months.
6. Anything left is withheld by the employer. A balance in the employee's favour carries forward with UFV maintenance of value (DS 21531 art. 19) and moves with the employee to a new job (DS 21531 art. 8). One employee's balance cannot be set against another's.

**AUDIT FLASH POINT: Form 608 label.** The SIAT page for employer Form 608 still names box 215 "13% de dos (2) Salarios Mínimos Nacionales". The regulation, DS 21531 art. 8 c) 2 as amended by DS 5383, gives employees one SMN. Follow the decree, check what the Planillas Tributarias application actually fills in, and refer if it differs.

**Independent professionals, trades, landlords and other direct contributors** (DS 21531 art. 9, text of DS 4850). They declare by quarter, month by month:

1. Income of each month (Form 610 box 13), plus income in kind (box 26). Where the income is from IVA-taxed operations, deduct the 13% IVA contained in the invoices issued (box 707). Add presumed antichretic income (box 42).
2. Deduct social-security contributions actually paid on time for that month (box 23).
3. Apply 13% (box 909). There is **no** two-SMN deduction: that is only for employment income (DS 21531 art. 6).
4. Credit: 13% of the invoices listed on Form 110 (box 781); the presumed credit of 13% of two SMN for each month (box 794, Bs 2,574 a quarter in 2026); and the updated balance from the previous quarter (box 635).
5. The balance due is box 1002, less payments on account (boxes 622 and 640). A balance in favour carries forward with maintenance of value.

**Invoices used for IVA.** A person who is also an IVA taxpayer may use an invoice against the RC-IVA only if it is not taken as an IVA credit (art. 31). Since DS 5563 (2 March 2026), an independent professional's IVA credit expressly includes personal food, clothing, training, transport, health, insurance, personal-vehicle fuel and utilities. Decide for each invoice which return it goes to; it cannot go to both. See [bolivia-iva](bolivia-iva.md).

**Investment and other income.** Taxable interest and rent are declared by the individual as a direct contributor (art. 9). The payer withholds 13% on interest if the recipient shows no NIT (DS 21531 art. 12), and on rent and the other art. 11 items if no invoice backs the payment. Those withholdings are final (DS 21531 art. 13). A person with both employment and independent income files each way separately and splits the invoices between the employer and Form 610 (DS 21531 art. 16).

**Non-domiciled individuals** (art. 19 h; DS 21531 art. 9 bis). An individual not domiciled in Bolivia who earns income for work done in Bolivia under a contract with a foreign entity declares and pays 13% of the total, with no deductions. The deadline is 3 days after the end of each month, or before leaving the country if sooner (Forms 613 and 614). They may pay in US dollars into the SIN account (DS 21531 art. 20). An individual who pays a non-domiciled person for services in Bolivia withholds 13% of the total within 5 days of payment or of the end of the service (DS 21531 art. 11). Payments abroad for services from abroad are IUE-BE at 12.5%, in [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md).

**Re-IVA** (Ley 1355). An individual with average monthly income up to Bs 9,000 who registers with the SIN as a beneficiary can get back in cash up to 5% of the price in purchase invoices issued electronically in their name and ID number. IVA already used against the RC-IVA, and purchases of State-subsidised goods, are excluded (art. 7).

**IGF, the wealth tax** (Ley 1357). The SIN consolidated text to 30 September 2026 carries Ley 1357 with no note of repeal, and the SIAT still lists Forms 22 (residents) and 23 (non-residents).
- **Who:** residents (more than 183 days in Bolivia in any 12 months) on their worldwide fortune, and non-residents on fortune in Bolivia, when net fortune at 31 December exceeds Bs 30,000,000.
- **Base:** fortune less outstanding capital of loans from ASFI-regulated lenders, excluding household goods. Spouses under community property each count their own fortune plus 50% of the fortune built up during the marriage.
- **Tax:** the rate applies to the whole base, less a fixed discount (art. 9). Property tax and IUE paid as a professional count as payments on account (art. 10).

Refer every IGF case.

## Deadlines and filing

| Who | Form | Deadline | Source |
|---|---|---|---|
| Employee | Form 110 with the invoices, to the employer | By the 20th of the month (DS 21531 art. 8 c 1) | SIN consolidated Ley 843 |
| Employer (withholding agent) | Form 608, monthly, from the Planillas Tributarias application | NIT-digit day 13 to 22 of the next month (digit 0 by the 13th, up to digit 9 by the 22nd) (DS 21531 art. 8) | same |
| Independent, landlord, other direct contributor | Form 610 with Form 110, quarterly | Within 20 days after the quarter: 20 April, 20 July, 20 October, 20 January (DS 21531 art. 9) | same |
| Payer withholding 13% on payments without invoice | Form 604 (box 415 national services, 416 foreign individuals, 434 rent, financial interest and others; box 909 tax) | NIT-digit day of the next month (DS 21531 art. 11) | SIAT Form 604 page |
| Non-domiciled individual | Forms 613 and 614 | 3 days after each month, or before leaving (DS 21531 art. 9 bis) | SIN consolidated Ley 843 |

A quarterly return is due even with no income or with a balance in the taxpayer's favour (DS 21531 art. 9).

## Penalties and interest

- **Late payment** (Ley 2492 art. 47): the omitted tax in UFV at the due date, plus interest of 4% a year for years 1 to 4, 6% for years 5 to 7 and 10% from year 8.
- **Omission of payment** (art. 165): 60% of the updated omitted tax. The same applies to an employer or payer who fails to withhold. A withholding agent who does not withhold or pay over in time is liable for the tax (DS 21531 art. 13). The fine is extinguished if the debt is paid by the twentieth day after notification of the Vista de Cargo (art. 157). It is reduced by 80%, 60% or 40% at the later stages in art. 156.
- **Formal duties** (art. 162): 50 to 5,000 UFV per breach; a late return is fined directly.
- **IGF omission**: 200% of the omitted tax, and the taxpayer loses confidentiality in enforcement (Ley 1357 art. 15).
- **Limitation** (art. 59, text of Ley 1733 of 27 May 2026): 4 years from 1 January after the due date; 6 years if the person never registered or chose the wrong regime.

## Cross-border points

- **Source only.** The RC-IVA reaches Bolivian-source income only (arts. 20 and 21). Pay for work done abroad for a foreign employer is not Bolivian-source. Directors' fees for work abroad for a Bolivian company are Bolivian-source under the IUE source rule (art. 44 a); treat them the same and refer if in doubt.
- **Non-domiciled workers** pay on the gross with no deductions, within 3 days after each month (above).
- **Paying a non-resident.** Individuals withhold 13% for services performed in Bolivia. Companies withhold IUE-BE at 12.5% on Bolivian-source amounts sent abroad ([bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)).
- **IGF** reaches residents' worldwide fortune.

## Two worked examples that recompute

### Example 1: employee, March 2026, with and without invoices

Ana earns Bs 12,000 gross in March 2026. Her payslip shows Bs 1,525.20 of employee social-security contributions. She has no earlier balance.

- Pay less contributions: 12,000 - 1,525.20 = Bs 10,474.80.
- Less two SMN (2 x 3,300 = 6,600): base Bs 3,874.80.
- 13%: Bs 503.72.
- No invoices: less the presumed credit Bs 429 (13% of one SMN). The employer withholds Bs 74.72 and declares it on Form 608.
- With Bs 1,000 of valid invoices on Form 110 by 20 March: credit 130 + 429 = Bs 559. Nothing is withheld. Her balance of Bs 55.28 carries to April, updated by the UFV.
- The edge: at Bs 7,000 gross with Bs 889.70 of contributions, pay less contributions is Bs 6,110.30, below Bs 6,600. The base is zero and no RC-IVA is due.

```oa-check
name: Employee Ana, March 2026, SMN Bs 3,300
inputs:
  gross: 12000
  contributions: 1525.20
  smn: 3300
  invoices: 1000
  gross_low: 7000
  contributions_low: 889.70
steps:
  - net: gross - contributions
  - base: max(net - 2 * smn, 0)
  - tax: base * 0.13
  - presumed: smn * 0.13
  - withheld_no_invoices: max(tax - presumed, 0)
  - credit_with_invoices: invoices * 0.13 + presumed
  - withheld_with_invoices: max(tax - credit_with_invoices, 0)
  - balance_carried: credit_with_invoices - tax
  - base_low: max(gross_low - contributions_low - 2 * smn, 0)
expected:
  net: 10474.80
  base: 3874.80
  tax: 503.72
  presumed: 429
  withheld_no_invoices: 74.72
  credit_with_invoices: 559
  withheld_with_invoices: 0
  balance_carried: 55.28
  base_low: 0
```

### Example 2: independent consultant, second quarter 2026, Form 610

Carlos is an independent engineer registered in the general regime. From April to June 2026 he invoiced Bs 60,000 in fees, all IVA-taxed. He paid Bs 3,000 of social-security contributions on time for those months. He lists Bs 20,000 of purchase invoices on Form 110 that he has not used as IVA credit, all dated within 120 days before 30 June. There is no balance from the first quarter.

- Box 13: Bs 60,000. Box 707, the 13% IVA in the invoices issued: Bs 7,800. Box 23: Bs 3,000.
- Box 909: (60,000 - 7,800 - 3,000) x 13% = 49,200 x 13% = Bs 6,396. No two-SMN deduction: Carlos is not an employee.
- Box 781: 20,000 x 13% = Bs 2,600. Box 794: 13% x 2 x 3,300 x 3 months = Bs 2,574.
- Due (box 1002): 6,396 - 2,600 - 2,574 = Bs 1,222, filed and paid with Form 610 by 20 July 2026.
- The edge: with fees of only Bs 15,000 in the quarter, box 909 is (15,000 - 1,950 - 3,000) x 13% = Bs 1,306.50. That is below the presumed credit alone (Bs 2,574). Nothing is due, and a balance of Bs 1,267.50 carries forward before counting any invoices. Extra invoices on Form 110 would only grow the balance. They may be worth more in his IVA return, where DS 5563 now lets a professional credit personal purchases.
- Carlos also owes IVA and IT on his fees every month: see [bolivia-iva](bolivia-iva.md).

```oa-check
name: Independent engineer Carlos, Q2 2026, Form 610
inputs:
  fees: 60000
  contributions: 3000
  invoices_110: 20000
  smn: 3300
  months: 3
  fees_low: 15000
steps:
  - iva_in_fees: fees * 0.13
  - determined: (fees - iva_in_fees - contributions) * 0.13
  - invoice_credit: invoices_110 * 0.13
  - presumed: smn * 2 * 0.13 * months
  - due: max(determined - invoice_credit - presumed, 0)
  - determined_low: (fees_low - fees_low * 0.13 - contributions) * 0.13
  - balance_low: presumed - determined_low
expected:
  iva_in_fees: 7800
  determined: 6396
  invoice_credit: 2600
  presumed: 2574
  due: 1222
  determined_low: 1306.50
  balance_low: 1267.50
```

## Ask the client first

1. Employee, independent (profession or trade), landlord or investor, or several at once; and whether domiciled in Bolivia.
2. For an employee: gross monthly pay, the contributions on the payslip, any aguinaldo or severance (not taxed), and the invoices they can hand in on Form 110.
3. For an independent: monthly fees invoiced, contributions paid on time, invoices not used as IVA credit, the balance from last quarter, and the NIT. They also file IVA and IT.
4. Rent (including anticresis contracts), interest by type and term of deposit, and dividends (not taxed).
5. Payments they make to individuals without invoices, or to non-domiciled persons (withholding).
6. Average monthly income (Re-IVA up to Bs 9,000) and, for wealthy clients, net fortune at 31 December (IGF above Bs 30,000,000).

Bank statement pointers:

| Pattern | Treatment |
|---|---|
| SUELDO, SALARIO, HABER, PLANILLA | Employment pay: employer withholds, nothing to file personally |
| AGUINALDO | Not taxed (DS 21531 art. 1) |
| HONORARIOS, PAGO SERVICIOS, CONSULTORIA | Independent income: Form 610 base, and IVA and IT |
| ALQUILER COBRADO, ANTICRETICO | Rent or anticresis: Form 610 base |
| DIVIDENDOS, REPARTO UTILIDADES from a Bolivian IUE payer | Not taxed (art. 19 c) |
| INTERESES DPF over the term limits | Not taxed; early redemption makes them taxable |
| GESTORA, APORTES | Contributions: deductible (employees via payslip, independents box 23) |
| RE-IVA, DEVOLUCION SIN | Refund, not income |
| Own-account transfers, loans, ATM | Not income; ask |

## Sources

| Source | URL | Read on |
|---|---|---|
| SIN, Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, Complementado, actualizado al 30/09/2026: read Título II arts. 19 to 35 with notes (Leyes 1448, 1606, 2382, 1718), DS 21531 arts. 1 to 24 (with DS 3890, 4850, 5383 notes), DS 21530 art. 8 last paragraph (DS 5563), Ley 1355 (Re-IVA) arts. 1 to 7, and Ley 1357 (IGF) arts. 1 to 15 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 5516 of 13 January 2026: art. 23, national minimum wage Bs 3,300 from 1 January 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281033 | 2026-11-11 |
| SIN, Ley N° 2492 Código Tributario Boliviano, Texto Ordenado, Complementado, actualizado al 30/09/2026: read arts. 47, 59, 156, 157, 162 and 165 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf | 2026-11-11 |
| SIN SIAT, Form 610: box codes 13, 26, 707, 42, 23, 909, 781, 794, 693, 1001, 635, 1002, 622, 640 | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/regimen-complementario-al-iva/610-regimen-complementario-del-iva-contribuyente-directo | 2026-11-11 |
| SIN SIAT, Form 608: box codes 13 to 450, including the box 215 label | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/regimen-complementario-al-iva/608-regimen-complementario-del-iva-agentes-de-retencion | 2026-11-11 |
| SIN SIAT, Form 604: box codes 415, 416, 434, 404 to 406, 909 and the annex categories | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/regimen-complementario-al-iva/604-regimen-complementario-del-iva-retenciones | 2026-11-11 |
| SIN SIAT, list of electronic forms: names of Forms 613, 614, 22 and 23 | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico | 2026-11-11 |
| Ministerio de Trabajo, Comunicado DGTHSO-014/2026 of 2 April 2026: applies DS 5516 and the Bs 3,300 SMN | https://mintrabajo.gob.bo/wp-content/uploads/2026/04/COMUNICADO-DGTHSO-0014-26.pdf | 2026-11-11 |
| Gaceta Oficial, Ley N° 1448 of 25 July 2022 (HTML text): new incisos g) and h) of Ley 843 art. 19 and new art. 165 of Ley 2492 (60%) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/168844 | 2026-11-11 |
| Gaceta Oficial, Ley N° 1733 of 27 May 2026 (HTML text): new art. 59 of Ley 2492, 4-year limitation | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281228 | 2026-11-11 |

Not yet confirmed: the employee social-security contribution rates (left to [bolivia-social-contributions](bolivia-social-contributions.md), not re-read here); which presumed-credit figure the Planillas Tributarias application uses for employees (Form 608 box 215 still says two SMN); the IGF filing deadline and valuation rules in DS 4436, and whether any 2026 law repealed Ley 1357 after the SIN consolidation date; the Re-IVA procedure and payment dates (its regulating decree, not read); how individuals' capital gains are taxed outside the stock exchange (DS 5301 art. 49, reproduced in the consolidated text, makes brokers withhold RC-IVA on gains from securities sold on an exchange; the wider rule was not read); treaty relief for non-domiciled individuals; the UFV values in bolivianos for updating balances (Banco Central de Bolivia, not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bolivia-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bolivia-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
