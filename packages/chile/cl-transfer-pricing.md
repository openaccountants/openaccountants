---
name: cl-transfer-pricing
description: "Chile transfer pricing (precios de transferencia) for tax year 2026 (año comercial 2026, año tributario 2027) under LIR art. 41 E. Covers who is related (art. 41 E No. 1, including any party in a preferential tax regime under art. 41 H and back-to-back deals), the arm's length rule for cross-border operations and business restructurings, the six methods and the most appropriate method, the interquartile range and the median, SII adjustments taxed with the art. 21 sole tax plus a 5% fine, the taxpayer's own upward self-adjustment, corresponding adjustments, advance pricing agreements, and the annual sworn statements: DJ 1907 (medium and large companies, or related operations over CLP 500 million), DJ 1951 local file (over CLP 200 million), DJ 1950 master file and DJ 1937 country-by-country report (groups of EUR 750 million), due 30 June, with the 10 to 50 UTA fine. Trigger on: precios de transferencia Chile, artículo 41 E, DJ 1907, F1907, archivo local, archivo maestro, reporte país por país, partes relacionadas, autoajuste, APA Chile. Out of scope: the IDPC itself (cl-corporate-income-tax), withholding on payments abroad and thin capitalisation (cl-cross-border)."
version: 1.0
jurisdiction: CL
tax_year: 2026
tax_year_notes: "Año comercial 2026, año tributario 2027"
last_updated: 2026-11-11
category: transfer-pricing
type: situation-rules
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: transfer-pricing
---

# Chile: transfer pricing (2026) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers Chile's transfer pricing rule for the 2026 income year: who it reaches, how the arm's length price is tested, what an adjustment costs, and which sworn statements must be filed in 2027 about 2026 operations. Currency: Chilean peso (CLP); fines in UTA.

Linked skills, not repeated here:

- [cl-corporate-income-tax](cl-corporate-income-tax.md): the first category tax (IDPC, 27% for 2026 under art. 14 A), the F22 return and the art. 21 sole tax rate.
- [cl-cross-border](cl-cross-border.md): Impuesto Adicional withholding on payments abroad, thin capitalisation (art. 41 F) and treaty relief.
- [cl-income-tax](cl-income-tax.md): individuals, the UTA of December 2026.

**Which text of the law.** DL 824, Ley sobre Impuesto a la Renta (LIR), LeyChile version of 17 October 2026: art. 41 E (transfer pricing), art. 41 H (preferential regimes), art. 21 (sole tax). Ley 21.850 (17 October 2026) does not amend art. 41 E. DL 830, Código Tributario (CT), art. 64 for domestic operations. The filing obligations come from the SII's 2026 instructions for each sworn statement (año tributario 2026, the latest published), under the power in art. 41 E No. 6.

## Who this applies to

**The rule (art. 41 E, first paragraph).** The SII may challenge, or set where none was set, the prices, values or returns of **cross-border operations** and **business restructurings** that taxpayers domiciled, resident or established in Chile carry out **with related parties abroad**, when they are not at normal market prices. A restructuring is caught when functions, assets, risks, goods or activities able to produce Chilean taxable income move between Chile and abroad, or contracts are ended or substantially changed, and the result is not at arm's length.

**Related parties (art. 41 E No. 1).** Two parties are related when:

- one participates directly or indirectly in the management, control, capital, profits or income of the other; or
- the same person or persons participate directly or indirectly in the management, control, capital, profits or income of both.
- A branch, agency or other permanent establishment is related to its head office, to the other establishments of the same head office, and to the head office's related parties and their establishments.
- Any party resident, domiciled, established or incorporated in a **preferential tax regime** (art. 41 H) is treated as related, whether or not it belongs to the same group. A territory is a preferential regime when it has no effective tax information exchange agreement with Chile and is not rated compliant or largely compliant by the Global Forum; the SII lists them by resolution (art. 41 H).
- **Back-to-back:** a party that deals with a third party, which in turn deals directly or indirectly with a related party of the first in similar or identical operations, is treated as related.

There is **no percentage test** in art. 41 E; participation of any size in management, control, capital, profits or income can make parties related. The DJ 1907 relation codes add individuals: spouse or civil partner, and relatives by blood or marriage to the fourth degree.

**Out of the rule, into another one.** Operations between related parties **inside Chile** are not under art. 41 E; the SII may value them at market under CT art. 64 when a price that sets a tax differs notoriously from normal market values. Interest paid to related lenders abroad on excess debt is also tested by art. 41 F (see cl-cross-border).

## Rates, bands and thresholds

| Item | Rule or amount | Year | Source URL |
|---|---|---|---|
| Tax on an SII transfer pricing adjustment | The difference is taxed only with the sole tax of art. 21, first paragraph (40%, see cl-corporate-income-tax), whether the taxpayer rectifies or the SII assesses | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (LIR art. 41 E No. 4; art. 21) |
| Fine on top of that sole tax | 5% of the difference, unless the taxpayer delivered the information the SII asked for in the audit, duly and on time | 2026 | same, art. 41 E No. 4 |
| Range | One comparable: a single figure. Two or more: the interquartile range (first to third quartile); outside it the price is not at arm's length | 2026 | same, art. 41 E No. 4 |
| Point of adjustment | SII assessment or resolution: the single figure or the **median**. Taxpayer accepts and rectifies: the single figure or any point in the range agreed with the SII | 2026 | same, art. 41 E No. 4 |
| Self-adjustment (autoajuste) before any SII request | To a point in the range; added to the IDPC base; only upward (never to lower taxable income or raise a loss) | 2026 | same, art. 41 E No. 9 |
| Sworn statement fine (DJ not filed, wrong, incomplete or late) | 10 to 50 UTA (CLP 8,736,240 to 43,681,200 at the December 2026 UTA of CLP 873,624), capped at the greater of 15% of capital propio and 5% of capital efectivo | 2026 | same, art. 41 E No. 6; https://www.sii.cl/valores_y_fechas/utm/utm2026.htm |
| Extension of a TP sworn statement deadline | Once, up to 3 months, on request to the Director Regional or Director de Grandes Contribuyentes; extends the CT art. 59 audit term by the same | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (art. 41 E No. 6) |
| DJ 1907 (annual TP sworn statement): who files | (a) companies in the Medium or Large segment at 31 December with any operation with related parties abroad; (b) any other taxpayer whose operations with related parties abroad (including preferential-regime parties) total more than CLP 500,000,000, at the Banco Central rate of 31 December | AT 2026 instructions | https://www.sii.cl/ayudas/ayudas_por_servicios/renta/2026/instrucciones_dj1907.pdf |
| DJ 1951 (local file): who files | All three: Large segment at 31 December; the group's parent filed a country-by-country report in Chile or abroad; operations with related parties abroad over CLP 200,000,000. Only operations over CLP 200,000,000 are reported, but loans and financial operations are reported whatever their amount | AT 2026 instructions | https://www.sii.cl/ayudas/ayudas_por_servicios/renta/2026/instrucciones_dj1951.pdf |
| DJ 1950 (master file) and DJ 1937 (country-by-country report): who files | The Chilean-resident parent of a multinational group with consolidated income of at least EUR 750 million (at the observed rate of 1 January 2015), or the Chilean group member designated as surrogate parent | AT 2026 instructions | https://www.sii.cl/ayudas/ayudas_por_servicios/renta/2026/instrucciones_dj1950.pdf ; https://www.sii.cl/ayudas/ayudas_por_servicios/renta/2026/instrucciones_dj1937.pdf |
| Due date of DJ 1907, 1937, 1950 and 1951 | 30 June (AT 2026 calendar) | AT 2026 | https://www.sii.cl/ayudas/ayudas_por_servicios/2120-formularios_y_plazos_2026-2171.html |
| Advance pricing agreement (APA) | Applies from the year the minute is signed and the 4 following years; may reach back up to 3 earlier years (no art. 21 sole tax, interest or fines for those years); SII decides within 12 months of complete information, silence is rejection; prior consultation answered within 2 months | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6368 (art. 41 E No. 7) |
| Corresponding adjustment after a foreign adjustment | Request within 1 year from when the foreign adjustment is final; needs a treaty that does not forbid it; SII authorisation of nature and amount | 2026 | same, art. 41 E No. 8 |

The segment (Micro, Small, Medium, Large) is shown in "Mi Información Tributaria / Mis Datos" on sii.cl and computed under Resolución Ex. SII N° 76 of 2017 (DJ 1907 instructions).

## The base

1. **Map the operations.** List every operation of 2026 with each related party abroad, and every balance still open in 2026: sales of goods, services rendered and received, royalties, interest and loans, leases, insurance, share sales, guarantees, restructurings. The DJ 1907 groups them by operation code (101 sale of goods produced, 102 goods for resale, 103 to 108 services, 109 licences, 111 interest, 116 share sales and so on), one record per type and counterparty.
2. **Test each against the arm's length standard.** Normal market prices are those that independent parties would have agreed in comparable operations and circumstances, looking at the relevant markets, the functions, assets and risks of each party, and the specific features of the goods, services or contracts (art. 41 E, third paragraph).
3. **Choose the most appropriate method** (art. 41 E No. 2), weighing each method's strengths and weaknesses, the type of operation, the information available, the comparables, the tested party, the years of financial data, ranges and comparability adjustments:
   - comparable uncontrolled price;
   - resale price (resale price less the gross margin of comparable resellers: gross profit over sales);
   - cost plus (direct and indirect production costs, without general or operating expenses, plus the comparable margin on cost);
   - profit split;
   - transactional net margin (net margin on assets, costs, sales or another reasonable indicator);
   - residual methods, only where none of the above can be applied, and the taxpayer must justify why.
4. **Compare with the range.** Inside the interquartile range: at arm's length. Outside it: not at arm's length (art. 41 E No. 4).
5. **Document.** A transfer pricing study is optional, but the taxpayer must keep all the information behind the methods, its own or its related parties' abroad, available to the SII (art. 41 E No. 3, citing CT arts. 59 and following).
6. **Self-adjust if needed, before the SII asks.** If the price is outside the range and favours the foreign party, add the adjustment to the 2026 IDPC base in the F22 (art. 41 E No. 9). A self-adjustment can never reduce taxable income. If the SII later adjusts the same operations, the art. 21 sole tax applies under No. 4.
7. **If the SII audits.** It summons the taxpayer under CT art. 63 to prove market prices (art. 41 E No. 2). If not proven, it sets the price itself with the methods and assesses (No. 4). The adjustment affects only taxes of the LIR, not VAT or customs (No. 4, last paragraph). The assessment can be challenged under Book III of the Código Tributario (No. 5).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Self-adjustment for 2026 | In the F22 for AT 2027, filed in April 2027 (see cl-corporate-income-tax) | LIR art. 41 E No. 9 |
| DJ 1907, DJ 1951, DJ 1950, DJ 1937 on 2026 operations | 30 June 2027, if the AT 2027 calendar keeps the AT 2026 date | SII 2026 calendar; LIR art. 41 E No. 6 |
| Extension | Up to 3 months, once, requested before the deadline | art. 41 E No. 6 |
| Corresponding adjustment request | 1 year from the foreign adjustment becoming final | art. 41 E No. 8 |
| APA monitoring report | Annually, as the APA minute sets; 30 days to cure after a request, or the SII may end the APA | art. 41 E No. 7 |

**How to file a sworn statement.** On sii.cl, log in with the company RUT and Clave Tributaria, open Servicios online, Declaraciones juradas, Declaraciones juradas de Renta, and choose form 1907 (or 1950, 1951, 1937). Fill Section A (the declarant) and Section B: for each related party abroad, its name without accents, its foreign tax ID, the country code from the SII's "País de Residencia" list, the relation code (1 to 13), the operation code, the amounts in pesos, the method and profitability indicator and any adjustment. Submit, and keep the certificate of filing.

## Penalties and interest

- **Adjustment by the SII:** the art. 21 sole tax on the difference plus a fine of 5% of the difference, unless the requested information was delivered duly and on time (art. 41 E No. 4). The SII sets by circular the minimum information that avoids the fine.
- **Sworn statement missing, wrong, incomplete or late:** 10 to 50 UTA, capped at the greater of 15% of capital propio and 5% of capital efectivo; imposed under the procedure of CT art. 165 No. 1 (art. 41 E No. 6).
- **Maliciously false sworn statement or APA information:** CT art. 97 No. 4, first paragraph (art. 41 E Nos. 6 and 7).
- **Late payment:** CPI adjustment and penal interest under CT art. 53; the rate for July to December 2026 is in [cl-income-tax](cl-income-tax.md).
- **APA in force:** no penal interest or fines on infringements found while it is in force, unless they carry prison, provided the taxpayer cures them within the term set (art. 41 E No. 7).

## Cross-border points

- **Treaties and double taxation.** When another state adjusts the foreign party's price, the Chilean taxpayer may ask for a corresponding adjustment under art. 41 E No. 8 if the treaty does not forbid it. The SII lists treaties in force and its circulars on mutual agreement procedures (Circular 13 of 2022, amended by Circular 19 of 2023) on its treaties page.
- **Payments abroad.** The same operation usually carries Impuesto Adicional withholding (services, royalties, interest). An adjusted price does not change the withholding already made; see [cl-cross-border](cl-cross-border.md).
- **Imports.** An APA covering imports of goods is signed jointly with the Servicio Nacional de Aduanas (art. 41 E No. 7).

## Two worked examples that recompute

UTA December 2026 = CLP 873,624. The art. 21 sole tax rate (40%) and the IDPC rate for 2026 (27%, art. 14 A) are those set out in cl-corporate-income-tax.

### Example 1: management fee to the foreign parent, SII adjusts to the median

Andina Servicios SpA (Large segment) paid its Spanish parent a management fee of CLP 900,000,000 for 2026. A benchmark of comparable service fees gives a first quartile of CLP 520,000,000, a median of CLP 600,000,000 and a third quartile of CLP 700,000,000.

- The fee is above the third quartile, so it is not at arm's length (art. 41 E No. 4).
- The SII assesses to the median: difference CLP 300,000,000.
- Sole tax of art. 21 at 40%: CLP 120,000,000.
- Andina did not hand over the information requested in the audit, so the 5% fine applies: CLP 15,000,000. Total CLP 135,000,000, before CPI adjustment and interest.
- Andina is in the Large segment with operations abroad, so it also had to file DJ 1907; a missed DJ 1907 adds a fine of 10 to 50 UTA (CLP 8,736,240 to 43,681,200).

```oa-check
name: CL transfer pricing 2026, management fee adjusted to the median
inputs:
  fee_paid: 900000000
  median: 600000000
  sole_tax_rate: 0.40
  uta: 873624
steps:
  - sii_difference: fee_paid - median
  - sole_tax: sii_difference * sole_tax_rate
  - fine_5pct: sii_difference * 0.05
  - total_assessed: sole_tax + fine_5pct
  - dj_fine_min: 10 * uta
  - dj_fine_max: 50 * uta
expected:
  sii_difference: 300000000
  sole_tax: 120000000
  fine_5pct: 15000000
  total_assessed: 135000000
  dj_fine_min: 8736240
  dj_fine_max: 43681200
```

### Example 2: self-adjust now, or wait? And must a small company file DJ 1907?

Same facts, but Andina's adviser spots the problem in March 2027, before the F22 for AT 2027 is filed and before any SII request.

- **Self-adjust (No. 9):** it may adjust to any point in the range. Adjusting to the third quartile adds CLP 200,000,000 to the IDPC base, which at 27% costs CLP 54,000,000.
- **Wait and be assessed (No. 4):** CLP 135,000,000 as in example 1 (CLP 120,000,000 if the information is delivered and the fine falls away).

The figure that decides is 27% of the gap to the chosen point in the range against 40% of the gap to the median plus the 5% fine: here CLP 54,000,000 against CLP 135,000,000, a saving of CLP 81,000,000. Self-adjustment wins whenever the price is outside the range and can be fixed before the SII asks. It cannot be used the other way: a price below the first quartile that favours Chile cannot be self-adjusted downward.

**Filing test for a small company.** A Small-segment SpA buying CLP 450,000,000 of goods from its related Peruvian distributor in 2026 does not file DJ 1907 (under CLP 500,000,000 and not Medium or Large). At CLP 520,000,000 it must. It must still price at arm's length either way.

```oa-check
name: CL transfer pricing 2026, self-adjust to the third quartile or wait, and the DJ 1907 test
inputs:
  fee_paid: 900000000
  median: 600000000
  q3: 700000000
  idpc_rate: 0.27
  threshold: 500000000
  ops_a: 450000000
  ops_b: 520000000
steps:
  - assessed: (fee_paid - median) * (0.40 + 0.05)
  - self_adjustment: fee_paid - q3
  - self_adjust_cost: self_adjustment * idpc_rate
  - saving: assessed - self_adjust_cost
  - over_threshold_a: ops_a - threshold
  - over_threshold_b: ops_b - threshold
expected:
  assessed: 135000000
  self_adjustment: 200000000
  self_adjust_cost: 54000000
  saving: 81000000
  over_threshold_a: -50000000
  over_threshold_b: 20000000
```

## Ask the client first

1. Who are the related parties abroad, and how is each related (shareholding, common control, branch, family, a party in a preferential regime, a back-to-back intermediary)?
2. What operations were done with each in 2026, for how much, and what balances were open at year end?
3. Which SII segment is the company in at 31 December 2026, and is it part of a group whose parent files a country-by-country report (consolidated income of EUR 750 million or more)?
4. Is there a transfer pricing study or benchmark, with the method and the interquartile range?
5. Has the SII sent a request or summons (CT art. 63), or has another country adjusted the same operation?
6. Were there restructurings in 2026: functions, assets, risks or contracts moved or ended?

## Sources

| Source | URL | Read on |
|---|---|---|
| DL 824, LIR, LeyChile version of 17 Oct 2026 (read in the LeyChile XML export and JSON text service): art. 21, art. 41 E Nos. 1 to 9, art. 41 H | https://www.bcn.cl/leychile/navegar?idNorma=6368 | 2026-11-11 |
| Ley 21.850 (DO 17 Oct 2026): arts. 8 and 9, read to confirm they do not amend art. 41 E | https://www.bcn.cl/leychile/navegar?idNorma=1229250 | 2026-11-11 |
| DL 830, Código Tributario: art. 64 | https://www.bcn.cl/leychile/navegar?idNorma=6374 | 2026-11-11 |
| Read for the figures named: SII, instructions for DJ 1907, AT 2026 (who files; CLP 500,000,000; relation and operation codes) | https://www.sii.cl/ayudas/ayudas_por_servicios/renta/2026/instrucciones_dj1907.pdf | 2026-11-11 |
| Read for the figures named: SII, instructions for DJ 1951 local file, AT 2026 (three conditions; CLP 200,000,000) | https://www.sii.cl/ayudas/ayudas_por_servicios/renta/2026/instrucciones_dj1951.pdf | 2026-11-11 |
| Read for the figures named: SII, instructions for DJ 1950 master file, AT 2026 (EUR 750 million) | https://www.sii.cl/ayudas/ayudas_por_servicios/renta/2026/instrucciones_dj1950.pdf | 2026-11-11 |
| Read for the figures named: SII, instructions for DJ 1937 country-by-country report, AT 2026 (EUR 750 million) | https://www.sii.cl/ayudas/ayudas_por_servicios/renta/2026/instrucciones_dj1937.pdf | 2026-11-11 |
| Read for the figures named: SII, declaraciones juradas 2026 forms and deadlines (F1907, F1937, F1950, F1951: 30 June) | https://www.sii.cl/ayudas/ayudas_por_servicios/2120-formularios_y_plazos_2026-2171.html | 2026-11-11 |
| Read for the figures named: SII, UTM/UTA 2026 (UTA December 2026 CLP 873,624) | https://www.sii.cl/valores_y_fechas/utm/utm2026.htm | 2026-11-11 |
| Read for the figures named: SII, international tax conventions page (treaties in force; MAP Circulars 13 of 2022 and 19 of 2023) | https://www.sii.cl/normativa_legislacion/convenios_internacionales.html | 2026-11-11 |

Not yet confirmed: the AT 2027 sworn statement calendar and any change to the DJ 1907, 1950, 1951 or 1937 instructions for 2026 operations; the text of Resolución Ex. SII N° 76 of 2017 (segments); the SII circular naming the minimum information that avoids the 5% fine; the current SII resolution listing preferential regimes under art. 41 H; how the self-adjustment is reported in the AT 2027 F22 (code); whether the art. 21 sole tax on a transfer pricing adjustment reaches Pro Pyme companies on simplified accounts; treaty-specific rules on corresponding adjustments and the MAP circulars themselves (not read).
