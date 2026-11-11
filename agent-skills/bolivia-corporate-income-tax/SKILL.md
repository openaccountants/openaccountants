---
name: bolivia-corporate-income-tax
description: "Bolivia corporate income tax (Impuesto sobre las Utilidades de las Empresas, IUE) for 2026 under Ley 843 Título III and its regulation DS 24051, as consolidated by the Servicio de Impuestos Nacionales (SIN) to 30 September 2026. Covers who pays (companies, branches, sole-owner businesses), the 25% rate, the 25% additional rate for ASFI and APS regulated financial entities with return on equity above 6%, the base from financial statements in UFV-restated constant currency, non-deductible items, depreciation rates and the 2026 accelerated depreciation option (DS 5563), the 3-year loss carry-forward, the year-end dates by sector and the 120-day deadline, Forms 500, 520, 605 and 570, the IUE credit against the 3% transactions tax (IT), IUE-BE withholding at 12.5% on payments abroad and the reinvestment rates, and penalties under Ley 2492. Trigger on: Bolivia corporate tax, IUE Bolivia, Formulario 500, impuesto sobre las utilidades, IUE-BE, AA-IUE, SRL tax Bolivia. Out of scope: individuals"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bolivia-corporate-income-tax"
  jurisdiction: "BO"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Bolivia corporate income tax (IUE): 2026 rate, base, losses, IT credit and filing v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The law is Ley N° 843 (Texto Ordenado), Título III "Impuesto sobre las Utilidades de las Empresas" (arts. 36 to 51 ter), and its regulation, Decreto Supremo N° 24051 of 29 June 1995. This skill reads both in the SIN's consolidated edition "Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, Complementado, actualizado al 30/09/2026", which also reproduces the 2026 changes: DS 5563 of 2 March 2026 (accelerated depreciation, bad-debt provisions, deductible IVA, IT credit), Ley 1705 (Presupuesto General del Estado 2026, keeping the IUE-BE reinvestment incentive) and Ley 1717 of 10 April 2026 (repeal of the financial transactions tax, ITF). The SIN edition says it is published for information and that the Gaceta Oficial text governs. Penalties and interest come from the Código Tributario, Ley N° 2492, in the SIN consolidated edition to the same date, which includes Ley 1733 of 27 May 2026. All amounts are in bolivianos (Bs). The tax year (gestión fiscal) is the year ending on the sector closing date in 2026 (see "Deadlines and filing").

## Who this applies to

- **Every company, public or private** (Ley 843 art. 37): sociedades anónimas, sociedades anónimas mixtas, sociedades en comandita, cooperatives, SRLs, sociedades colectivas, de hecho or irregular companies, sole-owner businesses (empresas unipersonales), and branches, agencies or permanent establishments of foreign companies. The list is illustrative, not closed.
- **Mining, hydrocarbons and electricity companies** are inside the general IUE (art. 38), with sector surtaxes on top (see "When to refer" below).
- **A business is any economic unit**, including a one-person one, that combines factors of production in industry, trade, services, rental of movables or works (art. 39). Since Ley 1448 of 25 July 2022 the words "the exercise of liberal professions and trades" are deleted from art. 39: independent professionals are no longer IUE payers and go to [bolivia-income-tax](bolivia-income-tax.md).
- **Source rule** (art. 42; DS 24051 art. 4): only Bolivian-source profit is taxed, whatever the nationality, domicile or residence of the owner and wherever the contract is signed. Bolivian-source includes advisory, technical assistance and professional services performed from abroad when linked to Bolivian-source profit (art. 44 b; DS 24051 art. 4 e). Foreign-source income and dividends received from another IUE-paying company are left out of the base (DS 24051 art. 31).
- **Exempt** (art. 49): activities of the State, departments, municipalities and public universities (except activities under the Code of Commerce); non-profit associations and foundations with the activities listed in art. 49 b) that meet the statutory and economic-reality conditions and have the exemption formally recognised by the SIN (DS 24051 art. 5); interest to international credit bodies and foreign official institutions under ratified agreements. Free-zone users are not exempt (Ley of 28 December 2008, art. 55, reproduced under art. 37).

**When to refer.** Refer to a specialist for: the 25% surtax on extraordinary profits from extractive activities (art. 51 bis), the mining additional rate of 12.5% (Ley 535 art. 102), hydrocarbons (IDH and royalties), insurers' technical reserves, reorganisations and mergers (DS 24051 art. 28), liquidation, and anything under a special regime (RTS, STI, RAU). Individuals and independent professionals: [bolivia-income-tax](bolivia-income-tax.md). IVA and IT monthly returns: [bolivia-iva](bolivia-iva.md). Employer contributions: [bolivia-payroll](bolivia-payroll.md).

## Rates, bands and thresholds

Quick answer: **25% of net taxable profit**, one rate, no bands. The IUE paid then counts as a payment on account of the next year's 3% IT. Ley 843 below is the SIN edition consolidated to 30 September 2026.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| IUE rate on net taxable profit (Ley 843 art. 50) | 25% | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Additional rate (AA-IUE) for ASFI-regulated financial intermediaries, leasing companies, general warehouses, SAFIs, brokers and securitisation companies, and APS-regulated insurers and reinsurers, only when return on equity exceeds 6% (art. 51 ter; Ley 921 applies it to profits from gestión 2017) | 25% on top of the 25% rate; not creditable against IT | 2026 | same |
| Surtax on profit from extractive activities in non-renewable natural resources, after the art. 51 bis deductions (out of scope here) | 25% | 2026 | same |
| Mining additional rate when prices are at or above the Ley 535 art. 101 table (out of scope here) | 12.5% | 2026 | same |
| IUE-BE: presumed net profit on Bolivian-source amounts paid, credited or remitted abroad (art. 51) | 50% of the gross, taxed at 25%: 12.5% of the gross, final | 2026 | same |
| IUE-BE on dividends or branch profits not capitalised, when at least 75% is reinvested (Ley 1613 art. 10 kept by Ley 1705; DS 5563 art. 3 III a) | 3.125% of the amount not capitalised | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281098 |
| Same, reinvestment 50% to 74.99% (DS 5563 art. 3 III b) | 6.25% of the amount not capitalised | 2026 | same |
| Same, reinvestment 25% to 49.99% (DS 5563 art. 3 III c) | 11.25% of the amount not capitalised | 2026 | same |
| Agencies of foreign companies with activities partly carried out in Bolivia (transport, communications, news, partly-local services), presumed net profit (DS 24051 art. 42) | 16% of Bolivian gross income, taxed at 25% | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Withholding on payments to individuals for movable goods without an invoice (DS 24051 art. 3, as amended by DS 4850) | 25% of a presumed 20% profit: 5% of the amount paid | 2026 | same |
| Transactions tax that the IUE is credited against (art. 75, art. 77) | 3% of gross income, monthly | 2026 | same |
| Loss carry-forward, general (art. 48, text of Ley 169) | Up to the 3 following years; not indexed | 2026 | same |
| Loss carry-forward, new productive ventures with at least Bs 1,000,000 invested, and the hydrocarbon and mining productive sector (art. 48) | Up to the 5 years after the start of operations; not indexed | 2026 | same |
| Donations deduction, to SIN-recognised exempt non-profits only (art. 47; DS 24051 art. 18 f) | Up to 10% of the taxable profit of the year | 2026 | same |
| Staff welfare spending beyond what labour law or collective agreements require (DS 24051 art. 11) | Up to 8.33% of gross salaries on the year's payroll | 2026 | same |
| Ordinary repairs deductible in the year (DS 24051 art. 22) | Up to 20% of the asset's value; above that, capitalised | 2026 | same |
| Interest to owners or partners on their loans (DS 24051 art. 18 k) | Deductible only up to LIBOR + 3% (foreign) or the BCB lending rate (local), and in total up to 30% of the interest the company pays to third parties | 2026 | same |
| Payments that must be supported by a bank or other ASFI-regulated document (DS 27310 art. 37 as replaced by DS 772, reproduced under DS 24051 art. 8) | Bs 50,000 and above per transaction | 2026 | same |
| Accelerated depreciation option for fixed assets acquired 1 January to 31 December 2026, not for mining and hydrocarbon extractors (DS 5563 Disposición Adicional Primera a) | Half the useful life in the DS 24051 art. 22 annex | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281098 |
| Annual return and payment deadline (DS 24051 art. 39) | 120 days after the year-end, with or without an external audit opinion | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| IUE-BE and art. 3 withholdings, payment day by last digit of the NIT (DS 24051 arts. 3 and 34) | Day 13 (digit 0) to day 22 (digit 9) of the month after the payment | 2026 | same |
| Omission of payment penalty (Ley 2492 art. 165, text of Ley 1448) | 60% of the updated omitted tax | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/168844 |
| Late interest on tax omitted, expressed in UFV at the due date (Ley 2492 art. 47) | 4% a year for years 1 to 4; 6% for years 5 to 7; 10% from year 8 | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf |
| Breach of formal duties, such as a late return (Ley 2492 art. 162 I) | 50 UFV to 5,000 UFV, the amount for each breach set by SIN regulation | 2026 | same |
| Limitation period for SIN to audit, assess, sanction and enforce (Ley 2492 art. 59 I, text of Ley 1733 of 27 May 2026) | 4 years, plus 2 more if the taxpayer did not register or registered in the wrong regime | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281228 |

Depreciation rates (DS 24051 art. 22 annex), straight line on cost; a selection of the annex, all from the same consolidated Ley 843 edition:

| Asset | Useful life | Annual rate | Year | Source |
|---|---|---|---|---|
| Buildings (edificaciones) | 40 years | 2.5% | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Office furniture and fittings | 10 years | 10% | 2026 | same |
| Machinery in general; equipment and installations | 8 years | 12.5% | 2026 | same |
| Motor vehicles; aircraft; construction machinery | 5 years | 20% | 2026 | same |
| Computer equipment; tools in general; agricultural machinery | 4 years | 25% | 2026 | same |
| Silos, warehouses and sheds; staff housing; irrigation channels and wells | 20 years | 5% | 2026 | same |

## The base

**Start from the financial statements.** For a company that must keep accounts (DS 24051 art. 2 a: everyone under the Code of Commerce, plus sole-owner businesses, de hecho companies, cooperatives and housing mutuals), the base is the profit in the annual financial statements prepared under generally accepted accounting principles, with the adjustments below (Ley 843 art. 47; DS 24051 arts. 6 and 7). Income and expenses are on an accruals basis; profit on instalment sales may be taken when each instalment falls due (art. 46).

**Constant currency.** The financial statements used for the IUE are restated in constant currency only by the change in the UFV (Unidad de Fomento de Vivienda) published officially, applying Norma Contable N° 3 as revised in September 2007 (DS 24051 art. 38, text of DS 29387). The SIN has answered that this rule still applies for the IUE despite the MEFP communiqué suspending full inflation adjustment for accounting (SIN consultation on the IUE page, see Sources). Use the UFV of the opening and closing dates of the company's own year.

**What is deductible.** Every expense needed to earn taxable profit and keep the source, in Bolivia or abroad, backed by original documents (art. 47; DS 24051 art. 8). In particular:

- **Staff costs**, including payments to owners and their relatives, if services are really rendered and the person is on the payroll with social security paid; the employer must show RC-IVA was applied, except on aguinaldos (DS 24051 art. 11). Aguinaldos and bonuses count for the year if paid before that year's return is due (art. 47).
- **Taxes actually paid as taxpayer** (DS 24051 art. 14 I): IT actually paid (not the IT covered by the IUE credit), property tax on real estate and vehicles, transfer taxes, IDH, municipal licences and fees. From DS 5563 (2 March 2026) the IVA in purchases is also deductible where it cannot be credited because it relates to exempt or zero-rated operations, and so is ICE shown separately and not recoverable. Fines and penalties are never deductible. Since Ley 1717 abrogated the ITF from 10 April 2026, the old rule barring ITF deductions has no effect from that date.
- **Provisions** only where a law requires them or DS 24051 allows them (art. 18 g), notably the severance provision under DS 24051 art. 17 b) and the bad-debt provision under art. 17 c). For gestión 2026 only, DS 5563 lets the bad-debt provision use, for the second year of the calculation, the greater of the actual 2025 bad debts and 60% of the actual 2026 bad debts.
- **Depreciation** at the annex rates from the month the asset is first used, the first month counted as a full month (DS 24051 art. 22). Accumulated depreciation may not exceed cost.

**What is not deductible** (art. 47; DS 24051 art. 18): personal withdrawals and personal expenses of the owner, partners or family; personal-service costs where RC-IVA compliance is not shown; the IUE itself; goodwill, trademarks and similar intangibles unless a price was paid; donations above the 10% limit or to non-recognised entities; provisions and reserves not authorised by law or the regulation; depreciation on technical revaluations; taxes on capital goods (they go into the asset's cost); losses from illegal operations; owner-loan interest above the art. 18 k) limits; and sums owners take as salary outside art. 11.

**AUDIT FLASH POINT: owner-loan interest.** DS 24051 art. 18 k) still caps cross-border owner-loan interest at "LIBOR + 3%". LIBOR is no longer published. The consolidated text read on 2026-11-11 carries no replacement benchmark. Treat any such deduction as at risk and refer.

**AUDIT FLASH POINT: payments of Bs 50,000 or more** must be backed by a document issued by an ASFI-regulated financial entity for the full value of each transaction, whether cash, credit or instalments (DS 27310 art. 37). Without it the SIN can reject the expense and the IVA credit.

**2026 accelerated depreciation (DS 5563, Disposición Adicional Primera a).** For fixed assets acquired between 1 January and 31 December 2026, a company may, voluntarily and instead of the normal annex, depreciate over half the annex useful life (a 4-year computer over 2 years). Mining and hydrocarbon extractors are excluded. The election must be notified to the SIN in a sworn statement and disclosed in the notes to the financial statements of that year.

**Losses** (art. 48). A Bolivian-source loss can be set against taxable profit of at most the 3 following years; it is not indexed. New productive ventures with minimum invested capital of Bs 1,000,000, and the hydrocarbon and mining productive sector, get 5 years from the start of operations. Losses of banks and financial intermediaries up to gestión 2010 cannot be used. DS 24051 art. 32 still reads "until used up" and "updated"; the later law (Ley 169) governs. Form 500 box 619 carries the losses still within their period.

**Companies not required to keep accounts** file an annual sworn statement to 31 December: gross taxable income (from the IVA sales and purchases records, interest and rentals), less invoiced expenses, IT actually paid and other taxes (DS 24051 art. 3 b). This is Form 520.

**Tax and the IT credit** (art. 77; DS 21532 art. 7). The IUE determined and actually paid for the year counts as a payment on account of the 3% IT in each later monthly IT return, until used up. Since DS 5563 the IUE need not have been paid by its due date to qualify. Any part still unused when the next year's IUE return falls due (including any extension) is lost to the State and is never refunded. The art. 51 bis surtax and the art. 51 ter AA-IUE are not creditable. The IUE is not creditable against IT on transfers of goods and rights. In practice the yearly cash cost of the two taxes together is the higher of the IUE and that year's IT, when the IT is large enough to absorb the IUE before the next IUE return is due.

## Deadlines and filing

**Year-end by sector** (DS 24051 art. 39). The company's tax year closes on:

| Closing date | Sector |
|---|---|
| 31 March | Industrial and oil companies |
| 30 June | Rubber, chestnut, agricultural, livestock and agro-industrial companies |
| 30 September | Mining companies |
| 31 December | Banks, insurers, commercial, service and all other companies, and those not required to keep accounts |

**Deadline.** The return and payment are due 120 days after the year-end, with or without an audit opinion (art. 39). For a 31 December 2026 year-end that is 30 April 2027; for 31 March 2026, 29 July 2026. A return must be filed even when all income is exempt or there is a loss (art. 40). In liquidation, the liquidation balance sheet is due 120 days after liquidation (art. 41).

**Steps, in the order the filer meets them** (SIN, SIAT forms pages):

1. Close the books, restate in UFV (art. 38), and prepare the financial statements: balance sheet, income statement, statement of changes in equity, cash flow statement and notes (DS 24051 art. 36).
2. In the SIAT, fill in **Form 500** (IUE, contributors required to keep accounts). Box 42 accounting profit or box 68 accounting loss; box 71 total non-deductible expenses (DS 24051 art. 18); box 480 regularisations for expenses that fail DS 24051 art. 8; box 495 non-taxed income (foreign-source or outside the tax); box 563 and 589 deferral of instalment-sale profit; box 592 net profit; box 606 net loss; box 619 unused loss from last year still within its period; box 1013 loss carried to next year; box 26 net taxable profit; box 909 tax determined at 25% of box 26.
3. In the liquidation section, box 622 takes payments on account already made and box 640 any balance carried; box 996 is the final balance due to the State.
4. Send the financial statements digitally with **Form 605** (balance sheet, income statement, statement of changes in equity, cash flows, notes, valued physical inventory, loss-compensation schedule where used, and supplementary tax information where required). The SIAT returns a certification code, a security code and a QR code on the received Form 605.
5. Pay by the same day-120 deadline. Then claim the IUE paid as a credit in each later monthly IT return (Form 400) until used up or until the next IUE return falls due.
6. Companies not required to keep accounts use **Form 520** instead (box 648 income, box 707 IVA declared, box 781 invoiced expenses, box 794 IT actually paid, box 882 other taxes, box 912 other deductible expenses, box 967 and 1024 losses).
7. Withholdings during the year: IUE-BE on payments abroad on **Form 530**; IUE withheld on purchases from individuals without an invoice on **Form 570**; the AA-IUE for financial entities on **Form 515**. Remittances under a tax treaty have their own **Form 591**. Pay withholdings by the NIT-digit day (13 to 22) of the month after the payment.

## Penalties and interest

- **Late payment** (Ley 2492 art. 47): the debt is the omitted tax expressed in UFV at the due date, plus interest of 4% a year for the first 4 years, 6% for years 5 to 7 and 10% from year 8, without any demand from the SIN.
- **Omission of payment** (art. 165, text of Ley 1448): 60% of the updated omitted tax, also for failing to withhold. The fine is extinguished if the debt is paid by the twentieth day after notification of the Vista de Cargo or Auto Inicial (art. 157). It is reduced by 80% if paid after that and before the Resolución Determinativa; 60% if paid before an appeal to the regional authority (alzada); 40% if paid after the alzada and before the hierarchical appeal (art. 156).
- **Formal duties** (art. 162): 50 UFV to 5,000 UFV per breach; a late return or missing invoice is fined directly, without the sanction procedure. The amount in bolivianos is the UFV value on the payment date.
- **Limitation** (art. 59, text of Ley 1733): 4 years for SIN to audit, assess, sanction and enforce, counted from 1 January after the payment due date (art. 60); 6 years if the taxpayer did not register or chose the wrong regime; sanctions imposed must be enforced within 2 years.

## Cross-border points

- **Payments abroad (IUE-BE).** On Bolivian-source amounts paid, credited or remitted to a beneficiary abroad (rents under DS 24051 art. 4, and Ley 843 arts. 19 and 44), the payer withholds 25% of a presumed net profit of 50%, so 12.5% of the gross, as a final tax (art. 51; DS 24051 art. 34). Fees for services from abroad linked to Bolivian-source profit are Bolivian-source (art. 44 b).
- **Branches.** A branch of a foreign company is presumed to distribute its profits, net of earlier losses, on the due date for filing its financial statements, whatever the date funds are sent (DS 24051 art. 34). IUE-BE is due then.
- **Reinvestment.** For dividends of Bolivian companies to foreign shareholders and for branch profits, capitalised reinvestment lowers the IUE-BE to 3.125%, 6.25% or 11.25% of the part not capitalised, depending on the reinvestment share. The reinvested amount must go to an equity reserve for fixed assets, inventories or investment in the same line of business by the close of the next IUE year (DS 5563 arts. 2 and 3). If the reserve is distributed or not reinvested, the tax is due as omitted tax under Ley 2492 art. 47.
- **Transfer pricing.** Related-party transactions must be priced at arm's length (art. 45, text of Ley 549); the SIN can adjust them (art. 45 bis) using one of six methods (art. 45 ter). Low- or no-tax countries are those on the OECD non-cooperative list and those listed by four or more South American laws (DS 2993). Documentation and the related-party return are for a transfer pricing skill; refer.
- **Treaties.** A treaty may reduce IUE-BE; remittances under a treaty use Form 591. The treaty texts were not read for this skill.

## Two worked examples that recompute

### Example 1: commercial SRL, 31 December 2026 year-end, a 2023 loss, IT credit

Comercial Andina SRL sells goods, so its year closes on 31 December. For gestión 2026 its UFV-restated accounting profit is Bs 800,000. It booked Bs 20,000 of tax fines and Bs 15,000 of the owner's family travel. It has a 2023 tax loss of Bs 100,000 not yet used. Its monthly gross income is Bs 2,000,000.

- Net profit (box 592): 800,000 + 20,000 + 15,000 = Bs 835,000.
- The 2023 loss is in its third and last following year (2024, 2025, 2026), so all of it can be used (box 619): net taxable profit (box 26) Bs 735,000.
- IUE at 25% (box 909): Bs 183,750, due by 30 April 2027 with Forms 500 and 605.
- Monthly IT is 3% of Bs 2,000,000 = Bs 60,000. Once paid, the IUE covers the IT of three full later months (Bs 180,000) and Bs 3,750 of the fourth, where the company then pays Bs 56,250 in cash. The credit is fully used well before the next IUE due date, so nothing is lost.
- The edge: had the loss been from 2022, its 3 years (2023 to 2025) would have run out. Base Bs 835,000, IUE Bs 208,750.

```oa-check
name: Comercial Andina SRL, profit Bs 800,000, add-backs, 2023 loss, IT credit (2026)
inputs:
  profit: 800000
  fines: 20000
  personal: 15000
  loss_2023: 100000
  monthly_income: 2000000
steps:
  - net_profit: profit + fines + personal
  - taxable: net_profit - loss_2023
  - iue: taxable * 0.25
  - monthly_it: monthly_income * 0.03
  - full_months_covered: floor(iue / monthly_it)
  - fourth_month_credit: iue - full_months_covered * monthly_it
  - fourth_month_cash: monthly_it - fourth_month_credit
  - iue_if_loss_expired: net_profit * 0.25
expected:
  net_profit: 835000
  taxable: 735000
  iue: 183750
  monthly_it: 60000
  full_months_covered: 3
  fourth_month_credit: 3750
  fourth_month_cash: 56250
  iue_if_loss_expired: 208750
```

### Example 2: should a service company take the 2026 accelerated depreciation? Worked both ways

Servicios Digitales SA (31 December year-end) puts Bs 400,000 of computer equipment into use in March 2026. Its taxable profit before depreciating this equipment is Bs 500,000. Computers have a 4-year life (25%). March to December is 10 months, the first month counted as full.

- Normal annex: 400,000 x 25% x 10 / 12 = Bs 83,333.33. Base Bs 416,666.67, IUE Bs 104,166.67.
- DS 5563 option, half the life (2 years, 50%): 400,000 x 50% x 10 / 12 = Bs 166,666.67. Base Bs 333,333.33, IUE Bs 83,333.33. The 2026 IUE falls by Bs 20,833.33.
- **What decides it is the IT.** Every boliviano of IUE paid is credited against the IT due before the next IUE return.
  - **Case A, gross income Bs 6,000,000 a year.** IT is Bs 180,000, more than either IUE figure. Each IUE is fully used against IT, so the cash paid for the two taxes is Bs 180,000 either way. The election saves nothing and only reduces depreciation left for later years.
  - **Case B, gross income Bs 2,000,000 a year.** IT is Bs 60,000. With normal depreciation the company pays IUE Bs 104,166.67 and uses only Bs 60,000 of it against IT: cash Bs 104,166.67. With the election: cash Bs 83,333.33. The election saves Bs 20,833.33 now. That is a timing benefit, which reverses as the asset is used up two years earlier.
- If it elects, it must notify the SIN by sworn statement and disclose the method in the 2026 notes.

```oa-check
name: Servicios Digitales SA, Bs 400,000 computers, normal vs DS 5563 accelerated (2026)
inputs:
  asset: 400000
  months: 10
  profit_before: 500000
  income_a: 6000000
  income_b: 2000000
steps:
  - dep_normal: asset * 0.25 * months / 12
  - dep_fast: asset * 0.50 * months / 12
  - iue_normal: (profit_before - dep_normal) * 0.25
  - iue_fast: (profit_before - dep_fast) * 0.25
  - iue_saving: iue_normal - iue_fast
  - it_a: income_a * 0.03
  - cash_a_normal: max(iue_normal, it_a)
  - cash_a_fast: max(iue_fast, it_a)
  - it_b: income_b * 0.03
  - cash_b_normal: max(iue_normal, it_b)
  - cash_b_fast: max(iue_fast, it_b)
  - saving_b: cash_b_normal - cash_b_fast
expected:
  dep_normal: 83333.33
  dep_fast: 166666.67
  iue_normal: 104166.67
  iue_fast: 83333.33
  iue_saving: 20833.33
  it_a: 180000
  cash_a_normal: 180000
  cash_a_fast: 180000
  it_b: 60000
  cash_b_normal: 104166.67
  cash_b_fast: 83333.33
  saving_b: 20833.33
```

The max() shortcut in this block assumes the IT of the 12 months after payment is at least the IT used in the example, and that income is even across the year.

## Ask the client first

1. Sector and year-end: industrial or oil (31 March), agricultural (30 June), mining (30 September) or other (31 December). This sets the 120-day deadline and the closing date.
2. Whether the business must keep accounts (Form 500 and 605) or not (Form 520), and whether it is a regulated financial entity or insurer (AA-IUE) or an extractive company (surtaxes, refer).
3. Unused tax losses by year, and whether the company qualifies for the 5-year period (new venture with at least Bs 1,000,000 invested, or hydrocarbon or mining production).
4. Fixed assets acquired in 2026 and whether the company wants the DS 5563 accelerated depreciation; its expected monthly IT, which decides whether the lower IUE saves cash.
5. Payments abroad (services, royalties, interest, dividends, branch profits), any reinvestment of dividends or branch profits, any treaty claim, and related-party transactions.
6. Expenses without invoices, payments of Bs 50,000 or more without a bank document, owner loans and staff welfare spending above the 8.33% limit.

## Sources

| Source | URL | Read on |
|---|---|---|
| SIN, Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, Complementado, actualizado al 30/09/2026: read Título III arts. 36 to 51 ter with the related notes (Leyes 169, 549, 921, 1448, 1613, 1705, 1717), DS 24051 arts. 2 to 42 and the art. 22 annex, DS 5303 art. 3, DS 5563 arts. 1 to 3 and Disposiciones Adicionales Primera to Cuarta, Título VI arts. 72 to 77 and DS 21532 arts. 7 and 10 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf | 2026-11-11 |
| SIN, Ley N° 2492 Código Tributario Boliviano, Texto Ordenado, Complementado, actualizado al 30/09/2026: read arts. 47, 59, 60, 156, 157, 162 and 165 with their notes (Leyes 812, 1448, 1733) | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf | 2026-11-11 |
| SIN, Compendio Tributario Actualizado: page that lists the two consolidated texts above as the September 2026 editions | https://www.impuestos.gob.bo/index.php/compendio-tributario-actualizado/ | 2026-11-11 |
| SIN SIAT, Form 500 IUE: box names, codes and formulas (42, 68, 71, 480, 495, 563, 589, 592, 606, 619, 1013, 26, 909) | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-a-las-utilidades-de-las-empresas/500-iue-contribuyentes-obligados-a-llevar-registros-contables/f-500 | 2026-11-11 |
| SIN SIAT, Form 500 liquidation section: boxes 622, 640 and 996 | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-a-las-utilidades-de-las-empresas/500-iue-contribuyentes-obligados-a-llevar-registros-contables/liquidacion | 2026-11-11 |
| SIN SIAT, Form 520 IUE for contributors without accounts: boxes 648 to 1024 | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-a-las-utilidades-de-las-empresas/500-iue-contribuyentes-obligados-a-llevar-registros-contables/f-520 | 2026-11-11 |
| SIN SIAT, list of electronic forms: names of Forms 400, 515, 530, 570 and 591 | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico | 2026-11-11 |
| SIN SIAT, IUE consultations: Form 605 contents and codes, UFV restatement still applies under DS 24051 art. 38 | https://siatinfo.impuestos.gob.bo/index.php/impuesto-asunto/iue | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 5563 of 2 March 2026 (HTML text): art. 3 III reinvestment rates and Disposiciones Adicionales Primera to Cuarta | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281098 | 2026-11-11 |
| Gaceta Oficial, Ley N° 1448 of 25 July 2022 (HTML text): new art. 165 of Ley 2492 (60%) and RC-IVA art. 19 g) and h) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/168844 | 2026-11-11 |
| Gaceta Oficial, Ley N° 1733 of 27 May 2026 (HTML text): Disposición Adicional Primera, new art. 59 of Ley 2492 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281228 | 2026-11-11 |
| Gaceta Oficial, Ley N° 1717 of 10 April 2026, published 11 April 2026 (HTML text): abrogation of the ITF, Ley 3446 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281148 | 2026-11-11 |

Not yet confirmed: the replacement, if any, for LIBOR in DS 24051 art. 18 k); the SIN regulation (RND) that sets each formal-duty fine within the 50 to 5,000 UFV range, and the UFV value in bolivianos on any given date (published daily by the Banco Central de Bolivia, not read here); the SIN form and deadline for the sworn statement notifying the DS 5563 accelerated depreciation election; the exact first IT period against which the IUE credit may be taken; the treaty rates on IUE-BE; the Gaceta Oficial original of Ley 1705 (PGE 2026), read here only as cited in DS 5563.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bolivia-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bolivia-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
