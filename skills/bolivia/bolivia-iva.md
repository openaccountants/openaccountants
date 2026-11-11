---
name: bolivia-iva
description: "Bolivia IVA (Impuesto al Valor Agregado, 13%) and IT (Impuesto a las Transacciones, 3%) for 2026 under Ley 843 Títulos I and VI and their regulations DS 21530 and DS 21532, as consolidated by the Servicio de Impuestos Nacionales (SIN) to 30 September 2026. Covers who pays, the 13% rate applied to the invoiced price with the tax inside it, debit and credit, the proportional credit, carried-forward balances updated by the UFV, exports and zero rates, imports, invoices and electronic invoicing, the monthly Forms 200 and 400 with their boxes, NIT-digit deadlines, the IT base and exemptions, the IUE credit against IT, IT and IUE withholdings when buying from individuals without an invoice, 2026 changes (DS 5563, Ley 1718) and penalties. Trigger on: Bolivia IVA, Bolivia VAT, Formulario 200, Formulario 400, debito fiscal, credito fiscal, factura Bolivia, Impuesto a las Transacciones, IT 3%, SIN filing, RCV. Out of scope: company profit tax (bolivia-corporate-income-tax), individuals (bolivia-income-tax)."
version: 2.1
jurisdiction: BO
tax_year: 2026
last_updated: 2026-11-11
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
type: computation
tier: 2
domain: vat-gst
---

# Bolivia IVA (13%) and IT (3%): monthly returns for 2026 v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The law is Ley N° 843 (Texto Ordenado): Título I for the IVA (arts. 1 to 18) with its regulation DS 21530, and Título VI for the IT (arts. 72 to 78) with its regulation DS 21532. This skill reads both in the SIN's consolidated edition "Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, Complementado, actualizado al 30/09/2026", which also carries the 2026 changes: DS 5563 of 2 March 2026 (professionals' IVA credit, IUE credit against IT) and Ley 1718 of 10 April 2026 (end of the 70% limit on fuel credit). The SIN edition is published for information; the Gaceta Oficial text governs. Penalties come from the Código Tributario, Ley N° 2492, in the SIN edition to the same date. Both taxes are monthly: each calendar month is a tax period (art. 10, art. 77). Amounts are in bolivianos (Bs).

## Who this applies to

**IVA taxpayers** (Ley 843 art. 3) are those who:

- habitually sell movable goods, or sell them in their own name for others;
- import goods definitively in their own name;
- carry out works, provide services or any other kind of supply;
- rent out movable or immovable property;
- carry out financial leasing of movable goods.

Once someone is a taxpayer, every sale of movables linked to that activity is taxed, whatever the goods. The IVA covers sales of movables in Bolivia, works and services performed in Bolivia, and definitive imports (art. 1).

**Outside the IVA** (art. 2):

- interest on credits granted or deposits received by financial entities. Their other services paid by commission or fee are taxed, so a bank's account fee carries IVA;
- buying and selling shares, debentures and securities;
- transfers in a reorganisation or a capital contribution. The predecessor's credit balances pass to the successor.

**Taking goods for the owner's or partners' private use** counts as a sale, valued at the retail market price (arts. 2 and 5).

**IT taxpayers** (arts. 72 and 73) are anyone, individual or legal person, who carries on trade, industry, a profession, a trade, business, rental of goods, works, services or any other activity in Bolivia, whether for profit or not. Free transfers of goods and rights are also inside. Reorganisations and capital contributions are outside.

**When to refer.** Refer for: the simplified regimes (Régimen Tributario Simplificado, Sistema Tributario Integrado, Régimen Agropecuario Unificado), which have their own forms; hydrocarbons (IEHD, IDH, refinery rules); mining exporters' refunds; ICE on alcohol and tobacco; and export refund (CEDEIM) claims. Company profit tax: [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md). Individuals' RC-IVA: [bolivia-income-tax](bolivia-income-tax.md).

## Rates, bands and thresholds

**Read this first.** The 13% is applied to the invoiced price, and that price already contains the IVA. The invoice does not show the tax separately (Ley 843 art. 5, art. 15). So the debit is 13% of the invoice total, not 13/113 of it. On Bs 11,300 invoiced the debit is Bs 1,469. Measured on the price without tax, the effective rate is 13 / 87 = about 14.94%. Form 200 computes it the same way: box 39 = (boxes 13 + 16 + 17 + 18) x 13%.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| IVA general rate (Ley 843 art. 15), on the invoiced net price with the tax included (art. 5) | 13% | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| IVA credit (art. 8 a; DS 21530 art. 8): rate applied to the invoiced amount of purchases linked to taxed activity | 13% | 2026 | same |
| Exports (art. 11): no debit; the credit on inputs offsets domestic IVA, and any excess is refunded in negotiable credit notes | 0% | 2026 | same |
| Export refund cap (DS 25465 art. 3, reproduced under DS 21530 art. 8) | Up to 13% of the FOB export value | 2026 | same |
| Zero rate: sale of printed books, Bolivian or imported, and official State publications (Ley 366 art. 8 II) | 0%, no credit on inputs used only for these sales | 2026 | same |
| Zero rate: international road freight by Bolivian carriers (Ley 3249), not an export, so no refund of credit | 0% | 2026 | same |
| Zero rate: domestic gold sales to raise international reserves (Ley 1503 art. 8); soy and similar products for YPFB biodiesel plants (Ley 1613 art. 21) | 0% | 2026 | same |
| Exempt imports (art. 14; Ley 366 art. 8 I; Ley 1613 art. 9; DS 5533 of 30 January 2026): diplomatic imports, travellers' bona fide goods, printed books, newspapers and magazines, crude oil, gasoline and diesel | Exempt | 2026 | same |
| Sale below which no invoice is needed (art. 16), with a daily summary invoice at the end of the day | Bs 5.00 | 2026 | same |
| Fuel purchases: limit of credit to 70% (Ley 1356 art. 18) repealed by Ley 1718 of 10 April 2026 | Full 13% credit | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281149 |
| IT rate (art. 75), on gross income accrued in the month (art. 74), IVA included | 3% | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| IT withheld when paying individuals for taxed items without an invoice (DS 21532 art. 10) | 3% of the full amount | 2026 | same |
| IUE withheld when paying individuals for movable goods without an invoice (DS 24051 art. 3) | 5% of the amount (25% of a presumed 20% profit) | 2026 | same |
| Payments that must be backed by a bank or other ASFI-regulated document (DS 27310 art. 37 as replaced by DS 772) | Bs 50,000 and above per transaction | 2026 | same |
| Monthly IVA and IT returns and payment, by last digit of the NIT (DS 21530 art. 10; DS 21532 art. 7) | Digit 0 by day 13, rising one day per digit, to digit 9 by day 22 of the next month | 2026 | same |
| IT on transfers of registered goods (real estate, vehicles, aircraft, boats, capital quotas) outside the habitual activity (DS 21532 art. 7) | Return and payment within 10 working days of the transfer, one return per asset | 2026 | same |
| Omission of payment penalty (Ley 2492 art. 165, text of Ley 1448) | 60% of the updated omitted tax | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/168844 |
| Late interest on tax omitted, in UFV at the due date (Ley 2492 art. 47) | 4% a year for years 1 to 4; 6% for years 5 to 7; 10% from year 8 | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf |
| Breach of formal duties, such as a late return or an unissued invoice (Ley 2492 art. 162) | 50 UFV to 5,000 UFV per breach | 2026 | same |

## The base

### IVA debit

1. **Base.** The net price in the invoice for goods, works, services and every other supply (art. 5), after customary discounts and returnable packaging at market value. Services supplied with the sale (transport, cleaning, packing, insurance, guarantee, installation, maintenance) and financing charges for deferred payment are part of the price even if invoiced apart. ICE and IEHD shown separately on the invoice are not part of the base (DS 21530 art. 5).
2. **Debit.** 13% of that base for the invoices issued in the month (art. 7; DS 21530 art. 7). Add 13% of returns, cancellations, discounts and rebates obtained on purchases that had earned a credit.
3. **When the debit arises** (art. 4; DS 21530 art. 4):
   - sales: on delivery or an equivalent act, backed by the invoice;
   - services and works: when finished or when all or part of the price is received, whichever is first;
   - construction: at each progress certificate received;
   - continuous services at fixed prices: at payment or at the end of each month, whichever is first, with the invoice by the fifth working day of the next month;
   - imports: at customs clearance;
   - financial leasing: at each instalment due.
4. **Imports** (art. 6). The base is the customs CIF value plus duties, customs charges and every other cost needed for clearance. The IVA paid at customs is a credit like a purchase.

### IVA credit

1. **Rate.** 13% of the invoiced amount of purchases, definitive imports, works and services charged to the taxpayer in the month (art. 8 a; DS 21530 art. 8).
2. **Link to the taxed activity.** The credit counts only to the extent the purchase is linked to taxed operations. The SIN lists by resolution the credits not considered linked.
3. **Professionals (DS 5563, from 2 March 2026).** For individuals exercising a profession or trade independently, linked purchases now expressly include: food and clothing for personal use; personal training, transport and health; health and life insurance premiums for the taxpayer, spouse and first-degree relatives; fuel for a personal vehicle; and basic utilities. The invoices must be in the taxpayer's name.
4. **No invoice, no credit.** Without an invoice, nota fiscal or equivalent document there is no credit (art. 12). A sale without an invoice is presumed unpaid and is tax fraud. A digital invoice has the same value as a paper original if it is registered in the SIN database (DS 4541).
5. **Bank document for large payments.** A payment of Bs 50,000 or more needs a bank or other ASFI-regulated document for the full value, or the credit can be rejected.
6. **Mixed use** (DS 21530 art. 8). Credit on purchases used for both taxed and non-taxed operations is first allocated directly where possible. The rest is allocated by the month's net sales, with exports counted as taxed. Form 200 box 1003 = box 31 x (box 13 + box 14) / (box 13 + box 14 + box 15 + box 505) x 13%. The monthly proportions are provisional. They are trued up in an extra IVA return filed with the year's IUE return, which cannot be amended later.
7. **Zero-rated only.** Purchases used only for zero-rated sales give no credit. With mixed zero-rated and other sales, the credit is in proportion to the non-zero-rated activity.
8. **Free supplies.** Goods or services given away produce no debit, so the credit taken on their inputs is paid back in the month of the gift. It is updated by the UFV from the last working day of the month before it was taken to the last working day of the month before it is paid back (Form 200 box 55).
9. **Timing.** One month's credits cannot be set against earlier months' debits.

### Balance

1. **Payable** (art. 9; Form 200 box 909). Debit above credit is payable.
2. **Credit balance** (DS 21530 art. 9). Credit above debit carries forward against future IVA only, updated each month by the UFV from the last working day of the month it arose to the last working day of the next month. It is not refunded in cash, except for exporters.

### IT base (arts. 74 and 77; DS 21532 art. 4)

1. **Base.** Gross income accrued in the month from the taxed activity: sales, total fees for services, interest on loans, and in general all operations. Taxpayers not required to keep books use income received. The IVA inside the price is not excluded, so the IT is 3% of the invoice total.
2. **Excluded from the base:** ICE and IEHD; reimbursed expenses incurred for others with a statement of account; tax refunds to exporters; and customary discounts actually given.
3. **Exempt** (art. 76):
   - employment work;
   - public office;
   - exports of goods (but not related transport, handling or storage);
   - services of the State and municipalities (not public companies);
   - interest on savings, current and fixed-term deposits, and income from securities investments;
   - private schools in the official curriculum;
   - diplomatic missions and international bodies;
   - sales of printed books, newspapers and magazines;
   - sales of securities and SRL capital quotas;
   - domestic sales of minerals, metals, oil and gas bound for export.
4. **IUE credit.** The IUE actually paid for the year counts as a payment on account of each later month's IT until used up (Form 400 box 664). Since DS 5563 the IUE need not have been paid by its due date. Any amount unused when the next IUE return falls due is lost, and it is never refunded. The IUE cannot be set against IT on transfers of goods and rights. The detail is in [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md).

## Deadlines and filing

Steps each month, in the order the filer meets them (SIN, SIAT form pages):

1. **Invoice every sale** through the SIN invoicing system. Paper or digital are both valid if registered with the SIN (DS 21530 art. 4; DS 4541). Below Bs 5 a daily summary invoice is enough.
2. **Record purchases and sales in the RCV** (Registro de Compras y Ventas) in SIAT en línea before filing. Form 200 takes its suggested figures from the RCV consolidated for the period.
3. **File Form 200 (IVA)** in SIAT en línea, Declaraciones Juradas module. The return is due even with no activity or a credit balance (DS 21530 art. 10).
   - **Debit side:** box 13 taxed domestic sales (not zero-rated); box 14 exports and exempt operations; box 15 zero-rated sales; box 505 sales outside the IVA; box 16 goods taken for private use; box 17 returns and cancellations made; box 18 discounts obtained; box 39 debit = (13 + 16 + 17 + 18) x 13%; box 55 credit paid back for gifts; box 1002 total debit.
   - **Credit side:** box 11 all purchases; box 26 purchases directly linked to taxed activity (including exports and exempt, excluding zero-rated); box 31 purchases that cannot be allocated; box 27 returns received; box 28 discounts given; box 114 credit = (26 + 27 + 28) x 13%; box 1003 proportional credit; box 1004 total credit.
   - **Result:** box 693 balance in the taxpayer's favour; box 909 tax determined; box 635 updated credit brought forward; box 1001 balance payable; boxes 622 and 640 payments on account; box 468 final amount due.
4. **File Form 400 (IT).** Box 13 gross income (including exempt); box 32 exempt income; box 24 base; box 909 IT at 3%; box 664 IUE paid to offset; box 1001 balance; boxes 622 and 640 payments on account; box 996 amount due.
5. **Withholdings, if any.** IT withheld on payments to individuals without an invoice goes on Form 410. The matching IUE withholding goes on Form 570. Transfers of registered goods go on Form 430 within 10 working days.
6. **Pay** by the NIT-digit day of the month after the period: digit 0 by the 13th, 1 by the 14th, 2 by the 15th, 3 by the 16th, 4 by the 17th, 5 by the 18th, 6 by the 19th, 7 by the 20th, 8 by the 21st, 9 by the 22nd.
7. **Exporters** use Form 210 and claim refunds under DS 25465 (refer).

## Penalties and interest

- **Late payment** (Ley 2492 art. 47): omitted tax in UFV at the due date, plus interest of 4% a year for years 1 to 4, 6% for years 5 to 7 and 10% from year 8.
- **Omission of payment** (art. 165): 60% of the updated omitted tax, also for failing to withhold. The fine is extinguished if the debt is paid by the twentieth day after notification of the Vista de Cargo (art. 157). It is cut by 80%, 60% or 40% at the later stages in art. 156.
- **Formal duties** (art. 162): 50 to 5,000 UFV per breach. A late return, an unissued invoice or a failure to register found in an inspection is fined directly, without the sanction procedure.
- **No invoice** (Ley 843 art. 12): the sale is taxed with no credit at all and is tax fraud.
- **Limitation** (art. 59, text of Ley 1733 of 27 May 2026): 4 years from 1 January after the due date; 6 years if the taxpayer did not register or chose the wrong regime.

## Cross-border points

- **Exports** carry no debit. Their input credit is set against domestic IVA, and the excess is refunded in negotiable credit notes up to 13% of FOB (art. 11; DS 21530 art. 11; DS 25465 art. 3). An export is made when the goods leave the customs territory with the refund documents. Receptive tourism by national operators and hotel stays of foreign non-resident tourists are treated as service exports (Ley 292 art. 30).
- **Imports** are taxed at customs on CIF plus duties and charges (art. 6). The IVA paid is a credit (DS 21530 art. 11 point 2).
- **Services bought from abroad.** No reverse-charge IVA on services from non-residents was found in Título I or DS 21530. Payments abroad carry IUE-BE withholding of 12.5% (see [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)). The earlier version of this skill said "self-assess 13% IVA" on Google, Microsoft, Meta, AWS, Zoom, Slack and Canva. That has no source in the law read and is withdrawn.

## Two worked examples that recompute

### Example 1: distributor, October 2026, IVA and IT, NIT ending in 4

Distribuidora Illimani SRL invoiced Bs 113,000 of taxed sales in October 2026. Its purchases with invoices, all for its taxed activity, total Bs 56,500. It carries an updated IVA credit of Bs 1,000 from September, and Bs 2,000 of IUE paid is still unused for the IT credit.

- Debit (box 39): 113,000 x 13% = Bs 14,690. Not 113,000 x 13/113 = Bs 13,000: the 13% is applied to the invoice total.
- Credit (box 114): 56,500 x 13% = Bs 7,345.
- IVA determined (box 909): Bs 7,345. Less the carried credit (box 635) Bs 1,000: payable (box 1001) Bs 6,345.
- IT (box 909 of Form 400): 113,000 x 3% = Bs 3,390. Less IUE (box 664) Bs 2,000: payable Bs 1,390.
- NIT ending in 4: both returns and payments are due by 17 November 2026.
- Effective IVA on the price without tax: 14,690 / (113,000 - 14,690) = 14.94%.

```oa-check
name: Distribuidora Illimani SRL, October 2026 IVA and IT
inputs:
  sales: 113000
  purchases: 56500
  credit_bf: 1000
  iue_left: 2000
steps:
  - debit: sales * 0.13
  - credit: purchases * 0.13
  - iva_determined: debit - credit
  - iva_payable: iva_determined - credit_bf
  - wrong_debit_13_113: sales * 13 / 113
  - it: sales * 0.03
  - it_payable: max(it - iue_left, 0)
  - effective_rate: round(debit / (sales - debit) * 100, 2)
expected:
  debit: 14690
  credit: 7345
  iva_determined: 7345
  iva_payable: 6345
  wrong_debit_13_113: 13000
  it: 3390
  it_payable: 1390
  effective_rate: 14.94
```

### Example 2: mixed activity, proportional credit and a credit balance

Librería y Servicios Andes SA in November 2026 has:

- taxed domestic sales Bs 300,000 (box 13);
- exports Bs 100,000 (box 14);
- zero-rated book sales Bs 50,000 (box 15);
- operations outside the IVA Bs 50,000 (box 505);
- purchases directly linked to taxed sales and exports Bs 150,000 (box 26);
- shop rent and utilities that cannot be allocated, Bs 40,000 (box 31).

The edge: what if taxed sales were only Bs 120,000?

- Debit: 300,000 x 13% = Bs 39,000.
- Direct credit (box 114): 150,000 x 13% = Bs 19,500.
- Proportional credit (box 1003): 40,000 x (300,000 + 100,000) / 500,000 x 13% = Bs 4,160. The zero-rated and non-IVA sales take their share of the rent credit out.
- Total credit Bs 23,660. IVA payable Bs 15,340.
- IT: the book sales are exempt from IT (art. 76 h), and the exports too (art. 76 c). Assume the Bs 50,000 outside the IVA is taxed for IT. The IT base is 300,000 + 50,000 = Bs 350,000, so IT is Bs 10,500.
- Edge: with taxed sales of Bs 120,000 instead, the debit is Bs 15,600. The proportion becomes (120,000 + 100,000) / 320,000, so the proportional credit is Bs 3,575 and the total credit Bs 23,075. The balance is Bs 7,475 in the company's favour (box 693). It carries to December updated by the UFV and is not refunded. Only the export part can be claimed back, through the export refund route.

```oa-check
name: Librería y Servicios Andes SA, November 2026, proportional credit
inputs:
  taxed: 300000
  exports: 100000
  zero: 50000
  non_object: 50000
  direct: 150000
  shared: 40000
  taxed_low: 120000
steps:
  - debit: taxed * 0.13
  - credit_direct: direct * 0.13
  - credit_prop: shared * (taxed + exports) / (taxed + exports + zero + non_object) * 0.13
  - credit_total: credit_direct + credit_prop
  - iva_payable: debit - credit_total
  - it: (taxed + non_object) * 0.03
  - debit_low: taxed_low * 0.13
  - credit_prop_low: shared * (taxed_low + exports) / (taxed_low + exports + zero + non_object) * 0.13
  - balance_low: credit_direct + credit_prop_low - debit_low
expected:
  debit: 39000
  credit_direct: 19500
  credit_prop: 4160
  credit_total: 23660
  iva_payable: 15340
  it: 10500
  debit_low: 15600
  credit_prop_low: 3575
  balance_low: 7475
```

## Ask the client first

1. NIT and its last digit (sets the due day, 13th to 22nd), and the regime: general, or a simplified regime (RTS, STI, RAU), which is out of scope.
2. What it sells: taxed, exported, zero-rated (books, international road freight, gold for reserves), exempt imports, or outside the IVA (financial interest, securities). This sets boxes 13, 14, 15 and 505 and the proportional credit.
3. Whether every purchase has an invoice in the company's name registered in the RCV, and whether any payment of Bs 50,000 or more lacks a bank document.
4. The updated IVA credit brought forward, and the unused IUE paid available against IT.
5. Whether it is an independent professional (the DS 5563 personal-expense credit applies) or a company.
6. Payments to individuals without invoices (IT and IUE withholding), transfers of vehicles or real estate (Form 430), and payments abroad (IUE-BE).

Transaction pointers, for classifying a bank statement:

| Pattern | Treatment |
|---|---|
| Bank account fees and commissions (BNB, Mercantil Santa Cruz, Unión, BancoSol, BISA, FIE) | Taxed service: credit if there is an invoice (art. 2) |
| Interest paid or received on loans and deposits from financial entities | Outside the IVA (art. 2); deposit interest exempt from IT (art. 76 e) |
| Payments to SIN, Aduana, Gestora, Caja Nacional de Salud | Tax and social security: not a purchase, no credit |
| Electricity, water, telecoms (ENDE, CRE, ELFEC, EPSAS, SAGUAPAC, ENTEL, Tigo, Viva) | Credit at 13% of the invoice if linked to the activity; mixed use goes to box 31 |
| Foreign SaaS and advertising (Google, Microsoft, Meta, AWS, Zoom) | No Bolivian invoice, so no IVA credit; IUE-BE withholding on the payment |
| Salaries | Outside IVA and IT (art. 76 a) |
| Own-account transfers, loan principal, cash withdrawals | Not a sale or purchase; ask what a withdrawal paid for |

## Sources

| Source | URL | Read on |
|---|---|---|
| SIN, Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, Complementado, actualizado al 30/09/2026: read Título I arts. 1 to 18 with related provisions (Leyes 366, 1503, 1613, 1718, 3249, 292; DS 5533), DS 21530 arts. 3 to 11 with DS 4541, DS 5563 and DS 25465 notes, Título VI arts. 72 to 78, DS 21532 arts. 4, 7 and 10, and DS 24051 art. 3 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf | 2026-11-11 |
| SIN, Ley N° 2492 Código Tributario Boliviano, Texto Ordenado, Complementado, actualizado al 30/09/2026: read arts. 47, 59, 156, 157, 162 and 165 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf | 2026-11-11 |
| SIN, Compendio Tributario Actualizado: page listing the September 2026 consolidated texts | https://www.impuestos.gob.bo/index.php/compendio-tributario-actualizado/ | 2026-11-11 |
| SIN SIAT, Form 200 IVA: RCV prerequisite, filing module, every box code and formula (13 to 468) | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-al-valor-agregado/200-impuesto-al-valor-agregado | 2026-11-11 |
| SIN SIAT, Form 400 IT: box codes 13, 32, 24, 909, 664, 1001, 622, 640, 996 | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-a-las-transacciones/400-impuesto-a-las-transacciones | 2026-11-11 |
| SIN SIAT, list of electronic forms: names of Forms 210, 410, 430 and 570 | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico | 2026-11-11 |
| Gaceta Oficial, Ley N° 1718 of 10 April 2026, published 11 April 2026 (HTML text): sole article repealing Ley 1356 art. 18, no separate commencement date | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281149 | 2026-11-11 |
| Gaceta Oficial, Ley N° 1448 of 25 July 2022 (HTML text): new art. 165 of Ley 2492 (60%) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/168844 | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 5563 of 2 March 2026 (HTML text): Disposiciones Adicionales Segunda (professionals IVA credit) and Tercera (IUE credit against IT) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281098 | 2026-11-11 |
| Gaceta Oficial, Ley N° 1733 of 27 May 2026 (HTML text): new art. 59 of Ley 2492, 4-year limitation | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281228 | 2026-11-11 |

Not yet confirmed: whether fuel purchases in April 2026 before Ley 1718 was published (11 April 2026) keep the 70% limit, since the law states no commencement date; any IVA or IT obligation on services bought from non-residents; the SIN resolution listing credits not linked to the activity; the RND amounts for each formal-duty fine; the UFV values in bolivianos for updating balances (published by the Banco Central de Bolivia, not read here); the current SIN invoicing-system rules (modalities and RND numbers); SIN guidance, if any, on the commencement of Ley 1718.
