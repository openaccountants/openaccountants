---
name: ar-corporate-income-tax
description: "Use this Guide for Argentine corporate income tax in fiscal years beginning in 2026: Impuesto a las Ganancias sociedades, Ganancias Personas Juridicas, F.713, corporate brackets, ajuste por inflacion, quebrantos and anticipos. It covers resident companies and domestic permanent establishments, the indexed progressive scale, the tax reconciliation, loss restrictions, dividends and branch remittances, ordinary annual filing, the October 2026 web-service transition and advance payments. It prepares a source-cited working paper for a local professional to review. Related-party pricing and foreign-beneficiary category computations are routed to the specialist Argentina Guides. It does not compute promotion regimes, gaming income, reorganisations or provincial turnover tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ar-corporate-income-tax"
  jurisdiction: "AR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Argentina: corporate income tax 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Resident capital companies and other entities in LIG art. 73(a), and Argentine permanent establishments under art. 73(b). This includes SA/SAU, SRL and SAS and the other listed entities where no exemption or separate treatment applies. A partnership/unincorporated business is not automatically a capital company: test its classification and any art. 73(a)(8) election. That election requires commercial accounts, starts on the first day of the fiscal year following the election year, and remains effective for five fiscal periods counted from its first application (art. 73(a)(8)).

**Quick answer:** the 2026 scale depends on the fiscal year's opening date, not the year a return is submitted. Reconcile accounts to taxable income, keep domestic/foreign source and restricted losses separate, apply the indexed scale, then eligible credits and actual advance payments. Get entity form, year opening/closing dates, accounts and tax adjustments, loss history and credits first.

This Tier 2 draft has no professional approval. It produces the tax bridge, computation, filing calendar and unresolved-issues list. Resident companies are taxed on worldwide income; foreign tax credit is limited, not a gross-income exclusion (LIG art. 1). Corporate year attribution follows the commercial fiscal period and accrual rules in art. 24. Do not use the individual's calendar-year deduction tables.

Out of scope: gaming's separate art. 73 rate, promotion/RIGI/knowledge-economy regimes, reorganisations and complex trust/fund classification. Foreign source, PE and withholding categories are in [argentina-cross-border](argentina-cross-border.md); TP in [argentina-transfer-pricing](argentina-transfer-pricing.md). Provincial turnover tax is a separate liability, not a credit assumed here.

## Rates, bands and thresholds

### Fiscal years beginning in 2026

| Net taxable income, ARS | Fixed tax, ARS | Marginal rate | Excess over, ARS | Official source |
|---|---|---|---|---|
| 0 to 133,514,185.74 | 0.00 | 25% | 0.00 | ARCA 2026 art. 73 scale; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/determinacion/documentos/Ganancias-Escala-PJ-2026.pdf |
| Over 133,514,185.74 to 1,335,141,857.38 | 33,378,546.43 | 30% | 133,514,185.74 | same |
| Over 1,335,141,857.38 | 393,866,847.93 | 35% | 1,335,141,857.38 | same |

Apply fixed tax + marginal rate × excess. LIG art. 73 adjusts bands annually by October-on-October IPC for fiscal years beginning after each update. Do not use the unindexed original ARS 5m/50m statute table or the old Guide's 2025 brackets for a year opening in 2026.

| Other rule | Amount or period | Conditions and official source |
|---|---|---|
| Branch profit remittance | Additional 7% | LIG art. 73(b), on remitting PE profits to head office; underlying corporate tax still applies; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Dividends to individuals/foreign beneficiaries | See cross-border Guide's art. 97 computation | Identify recipient and profit period before distributing; corporate resident receipts have separate art. 68 treatment; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Ordinary loss carryforward | Five following years | LIG art. 25, subject to source/type restrictions; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| New loss indexation | Losses from fiscal years beginning from 1 January 2025 | Current art. 25, amended by Ley 27.802 art. 190: IPC between loss-year close and computation-year close; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Tax inflation adjustment trigger | IPC increase above 100% over 36 months before closing | LIG art. 106, transitional first-year rules are separate historic rules; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Corporate advances | Nine payments, each 11.11% of adjusted prior-year base | ARCA current anticipos instructions; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/anticipos.asp |
| Minimum advance amount | ARS 2,500, inclusive | An advance equal to or above this is payable; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/anticipos.asp |

## The base

Use [LIG arts. 23-25, 53, 55-78, 83-93 and 105-109](https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05). The working paper must distinguish book profit, tax adjustments, source-specific results, restricted losses, taxable net income, determined tax and payment credits.

1. Start with the applicable commercial accounts and reconcile to the statutory tax measurement. Taxable business income generally accrues; accounting recognition and inflation restatement are not by themselves the tax result. Separate exempt/non-taxable income and identify direct/shared costs attributable to it.
2. Reconcile sales, inventory and cost of sales under the statutory valuation rules, fixed-asset tax depreciation and disposals, foreign exchange, receivables and provisions. Accounting impairments/reserves are not automatically deductions. Retain asset cost/date and depreciation schedules, inventory and bad-debt evidence.
3. Deduct expenses necessary to earn, maintain or preserve taxable income under art. 83, with documents and any specific limitations. Test art. 92 disallowances separately: distributions, personal costs, non-deductible taxes, penalties (Decreto 862 art. 227), limited royalties and other restricted expenditure do not become deductible by booking them as business expenses.
4. Prepare the tax inflation adjustment where art. 106's trigger applies. This is a distinct statutory balance-sheet computation with prescribed asset/liability exclusions and movements. Do not apply the annual CPI percentage to accounting profit or equate accounting inflation adjustment with tax adjustment. Historic instalment components and special investments require a separate year-by-year schedule.
5. Apply current-year and brought-forward losses by source/type. Under art. 25, securities/digital-asset and non-hedging derivative losses are specific losses; they cannot freely shelter ordinary trading profit. Foreign-source losses remain against foreign-source income under art. 131. Ordinary unabsorbed loss expires after the statutory five-year window. For fiscal years beginning from 2025, update qualifying losses by IPC between year-end months under the current art. 25; do not extend that rule automatically to older losses.
6. Floor the taxable base at zero and apply the fiscal-opening-year scale. Then deduct eligible foreign tax credit and other admitted payment credits, suffered withholdings/perceptions and paid advances, reconciling each certificate and account. A final withholding cannot automatically be used again as a general credit.

### Common deduction limits

**Related-party financial interest:** under LIG art. 85(a) and [Decreto 862 arts. 192-200](https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06), classify financial debt with related domestic or foreign parties first; debts for ordinary business purchases, leases and services are excluded. Include under-par financial-debt discounts and disguised financial debt. The ordinary annual ceiling is the greater of ARS 1,000,000 and 30% of the statutory measure: taxable income before the relevant interest, updates, exchange differences and opening accumulated losses, adding back art. 86(f) depreciation/amortisation. Updates and exchange differences are included in “interest” to the extent art. 106 does not apply as provided by art. 85(a).

Add unused capacity from the three immediately preceding fiscal periods, only once and oldest first. Interest disallowed by this ceiling carries to the five immediately following periods, remains subject to their ceiling, and is used oldest first. Keep separate year-expiry schedules for capacity and disallowed interest.

Before limiting, test the statutory exceptions: Ley 21.526 financial entities; qualifying financial trusts; businesses mainly carrying on statutory leasing and otherwise exclusively financial activities; interest up to financial-asset interest accrued in the year; the proved independent-creditor group ratio; and proved effective taxation of the recipient. The group exception requires at least 80% common direct/indirect ownership throughout the debt period and an independent Argentine public accountant's special report. For the recipient exception, decree art. 200 requires the domestic recipient's taxable return and sufficient determined tax in the payment year; for foreign recipients, the qualifying paid interest, updates and discounts must be subject to final withholding, including treaty-limited or treaty-eliminated withholding. Unwithheld foreign-currency exchange differences remain subject to the ceiling. Preserve the statutory evidence instead of assuming payment alone proves an exception. Withholding and TP apply independently of deductibility.

**Representation:** LIG art. 91(h) caps documented actual representation expenses at 1.50% of remuneration paid in the fiscal year to employees. Decree art. 221 excludes art. 91(f) extraordinary remuneration/gratuities from that denominator, requires causal connection with taxable non-exempt income, and excludes accompanying travellers' costs. General advertising to potential consumers and qualifying employee travel allowances are not representation merely because they promote the business.

**Advice from abroad and board members acting abroad:** independently of withholding and TP, LIG art. 92(e) and [Decreto 862 art. 228](https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06) limit foreign-performed technical, financial or other advice deductions to the applicable alternative: 3% of the sales/revenue used as the contractual remuneration base, or 5% of the investment actually made because of the advice. Separate mixed art. 104(a) consideration into its relevant components. Remuneration to directors, council members or comparable bodies of domestic entities acting abroad has a separate ceiling: 12.5% of the commercial profit if fully distributed as dividends, or 2.5% if none is distributed, increasing proportionally with distribution. Use the commercial profit of the year for which the remuneration is paid. ARCA may set other limiting indices where the operations do not fit those cases; do not select the larger percentage without establishing the applicable facts.

**Directors and managing partners:** under art. 91(i) and decree art. 222, deductible role fees cannot exceed the greater of 25% of accounting profit after the year's income tax and the sum of each recipient's actual allocation capped at ARS 12,500. The statutory fixed amount rises 40% for a woman recipient and 60% for a travesti, transsexual or transgender recipient; where a mandatory board quota applies, the increase applies only for members exceeding it. These are alternatives to the profit cap, not additional deductions. Individual allocation by the competent body must occur by the annual return deadline to deduct for the service year; later allocation is deducted in that allocation year. Syndics' fees follow the allocation timing rule but are not silently put under the director-role cap. Separately paid wages or other genuine services follow their own income category, supported by actual work, reasonable amount and relevant social-security compliance.

Decree art. 227 disallows fiscal fines, punitive interest and specified accessories, but expressly excepts Ley 11.683 art. 37 compensatory interest and statutory updates. Do not disallow all tax interest. Foreign trademark/patent royalties are limited to 80% under decree art. 229, with arm's-length pricing and art. 24 timing checked separately.

### Tax inflation adjustment working paper

Use LIG arts. 105-108, not the accounting restatement. First test the above-100% 36-month trigger. Art. 107 uses values at the preceding fiscal close under tax rules; excluded assets/liabilities use their commercial or tax balance values as prescribed. Foreign currency deposits, credits and debts use the applicable Banco Nación closing buying/selling rate including accrued interest; peso items include accrued interest/updates. Quoted non-equity securities use closing quotation; unquoted instruments use cost plus accrued interest/updates/FX. Digital assets use the statutory closing-quotation rule, with the prescribed regulation checked for the particular asset. Customer advances freezing prices include the monthly IPC update under art. 107(e).

1. Take opening assets, then remove every art. 106(a) exclusion: non-trading land/buildings and works; materials for those works; depreciable movable assets; movable fixed assets being made; intangibles; standing/cut timber in forestry; shares/equity/fund units; foreign investments not producing or used to produce Argentine-source income; non-depreciable movables other than securities/trading stock; price-freezing purchase advances for items 1-9; documented committed/irrevocable future-capital contributions except market-like interest/indexed ones; unpaid shareholder subscriptions; owner/partner debit balances from unpaid capital or non-market dealings; non-market debit balances of foreign persons/groups participating directly or indirectly in the local foreign-capital company's capital, control or management; already tax-deducted formation/organisation/reorganisation/development/research expenses; and capitalised non-deductible tax/expense advances, retentions and payments on account. If an opening item in exclusions 1-7 was sold or distributed in the year as described in art. 106(a), do not remove its opening value. For those art. 106(a) penultimate-paragraph disposals, art. 107(d) overrides the opening value with the tax cost used on disposal. Opening stock transferred to fixed assets is removed at its opening tax value.
2. Subtract admitted opening liabilities: debts with only tax-admitted provisions at admitted amounts; income received in advance/future benefits; and art. 91 fees/gratuities deducted for the year for which paid. Exclude documented committed/irrevocable future capital receipts that never bear interest/updates, non-market owner/partner credit balances, and non-market credit balances of foreign persons/groups participating directly or indirectly in the local foreign-capital company's capital, control or management. Do not use equity as a debt.
3. Multiply that qualifying opening asset-minus-liability balance by `IPC closing month / IPC preceding closing month - 1`. The signed static formula is `-(qualifying opening assets - admitted opening liabilities) × (IPC close / IPC preceding close - 1)`. Asset surplus produces a **negative** adjustment; liability surplus a **positive** adjustment. This is the static amount.
4. Add **positive** monthly IPC changes, from the event month to the closing month, on: owner/partner withdrawals and third-party funds/assets disposed of without market-like interest/update or dealings; distributed dividends other than bonus shares; effective capital reductions; paid fees above art. 91 limits; acquisitions/incorporations of excluded assets 1-10 still held at close, including own-share acquisitions; and funds/assets converted into the foreign investments of exclusion 8, subject to art. 106(d)(I)(6)'s exclusions 1-7, 9 and 10. For each movement use amount × `(IPC close / IPC event month - 1)`.
5. Subtract **negative** monthly changes on contributions/capital increases; foreign investments of exclusion 8 newly used to produce Argentine income, except assets of exclusions 1-7, 9 and 10; and the tax cost of exclusion-9 non-depreciable movables sold or delivered for art. 106(d)(I)(1)-(5) purposes. Use the same event-to-closing monthly formula.
6. Net static and dynamic amounts once. Positive increases profit/reduces loss; negative reduces profit/increases loss. Reconcile art. 108's accrued updates/FX and price-freezing advance adjustments in the tax bridge so they are neither omitted nor counted twice. Historical deferred instalments remain a separate vintage schedule; this does not validate their transitional conditions.

Retain the opening classification, excluded-item list, IPC series/months, each dated movement, sign and reconciliation. An unclassified balance or unsupported index prevents finalising that component.

**Exception and transition table**

| Fact | Treatment and source |
|---|---|
| Year begins in 2025 but closes in 2026 | Use the opening-year scale, not this 2026 table, under LIG art. 73 |
| Loss year opened in 2024 | Current art. 25's new 2025-onward indexation does not automatically cover it; keep old loss unconfirmed pending its applicable rules |
| Recipient of dividend is another Argentine capital company | Test LIG art. 68; do not assume the individual/foreign dividend treatment |
| Distribution relates to pre-2018 accumulated profits | Reconcile art. 74 equalisation-tax and transitional provisions before payment; no automatic current-dividend shortcut |
| Gaming, promotion, reorganisation or hybrid entity | Refer the special regime; this ordinary computation does not establish its rate or exemption |

## Deadlines and filing

[RG 4626 art. 6](https://biblioteca.arca.gob.ar/dcp/REAG01004626_2019_11_05) ordinarily places return and balance payment in the fifth month after commercial closing, subject to the official CUIT calendar. Financial statements and the required accompanying documents are due by the last day of the sixth month. Do not repeat the old Guide's unsourced general June extension: an extension needs its own applicable resolution.

### 2026 transition for F.713

[RG 5908 arts. 1-4](https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5908%7Co%3A9%7Ca%3A2026%7Cf%3A01%2F10%2F2026) introduces **GANANCIAS PERSONAS JURÍDICAS**, Clave Fiscal level 2 or above, for commercial closings from June 2026 inclusive. From 19 October 2026 to 28 February 2027, choose the web service or the existing application; from 1 March 2027 the web service is mandatory. Earlier closings, original or amended, remain in the application. An amendment follows the medium used for its original return.

ARCA's [presentation page](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/presentacion.asp) identifies the return as **F.713**. Reconcile its determination to the working paper: domestic/foreign-source result, admissible losses, determined tax and payment credits/saldo. Exact current web field/box numbering has not been confirmed; do not invent it from older SIAP screenshots. Validate and submit, retain the return and acknowledgement, and separately reconcile payment in Sistema Cuentas Tributarias.

Under RG 4626 art. 4, submit **Memoria, Estados Contables e Informe del Auditor**, professionally certified and signature authenticated, through **Presentación Única de Balances (PUB)**, Clave Fiscal level 2 or above. NIIF reporters have the prescribed local-accounting reconciliation/documents; qualifying MiPyME reporters may use the specified note alternative and retain its working papers. Use individual accounts where consolidated accounts exist. Save PUB's acknowledgement; F.713 does not replace PUB.

### Advances and reduction

The [ARCA anticipos page](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/anticipos.asp) requires nine advances, starting the month after the ordinary annual return/balance deadline. Prior-year determined tax is reduced by the specified promotion relief, non-final withholding/perception credits, substitute-withholding payments, qualifying diesel fuel-tax credits and analogous foreign-tax credit. Current-period amounts are not subtracted from the prior-year base. Apply 11.11% to that adjusted base for each advance, reconcile ARCA's **Sistema Cuentas Tributarias** figures and pay when the minimum is met. VEP advance codes: tax **010**, concept **191**, subconcept **191**. The published [2026 advance calendar](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/documentos/Anticipos-Vencimientos-PJ.pdf) is period/CUIT-specific; calendar-year 2026 profit can create 2027 payment dates, so obtain that year's schedule when published.

Do not reduce advances informally. Ordinary reduction is from the fifth advance; from the third if total exceeds estimated tax by more than 25%, or first if more than 40%. Requirements include active unrestricted CUIT, electronic fiscal domicile, no same-tax/year reduction request in the prior 90 days, and no missing relevant income-tax returns from January of the previous year. Request in **Sistema Cuentas Tributarias**, **Reducción de Anticipos**, with tax/year/projected base; retain **F.2254** and check the fiscal-domicile decision. Pay the resulting estimate on time. Underpayment carries interest under the stated comparison of real tax and original advances.

The special procedure applies if the determined advance-base parameter exceeds ARS 250m for segment 11 or ARS 200m for others **and** the estimated base is more than 10% lower. Use **Presentaciones Digitales**, **Solicitud de Reducción de Anticipos Impuesto a las Ganancias - Trámite Especial**, with supporting projection, at least 60 calendar days before the last advance. ARCA's decision period is 60 calendar days. Do not mistake the request acknowledgement for approval. Source: same current ARCA advance page; its 2027 IPC update applies from March, not a retroactive 2026 threshold change.

## Penalties and interest

Annual return, balance payment, advances and PUB are separate obligations. A filing acknowledgement does not prove payment, and a reduction request does not excuse an unapproved shortfall. Current 2026 penalty amounts and interest rates have not been confirmed here; compute neither from historic nominal figures. The advance-reduction source above expressly warns of interest where reduced amounts fall short, rejection and appeal procedures. Refer a disputed loss indexation, historic inflation component, deduction cap or late-payment assessment before finalising the liability.

## Cross-border points

Residents include foreign income with the limited foreign-tax credit. PE profits use the ordinary scale and the separate remittance charge; dividends and pre-2018 equalisation require recipient/profit-period analysis. The prior Guide's interest/royalty/treaty topics are retained through [argentina-cross-border](argentina-cross-border.md), which owns the category-specific gross withholding and treaty documentation. There is no general software-royalty rate inferred from an invoice label, and no unverified count of treaties. TP, service benefit evidence and financial-interest deduction limits must be checked independently.

## Two worked examples that recompute

### 1. Ordinary 2026 company in the second band

Assume an ordinary resident company's reconciled net taxable income is ARS 200,000,000 for a year opening in 2026, with no special regime, loss or foreign credit. Tax is 33,378,546.43 + (200,000,000 - 133,514,185.74) × 30% = 53,324,290.71. With paid advances of 40,000,000 and valid non-final withholding credits of 5,000,000, balance is 8,324,290.71. The inputs are assumed; scale is ARCA's original 2026 PDF.

```oa-check
name: Corporate second-band tax and balance
inputs:
  taxable_income: 200000000
  first_limit: 133514185.74
  fixed_tax: 33378546.43
  paid_advances: 40000000
  withholding_credit: 5000000
steps:
  - determined_tax: round(fixed_tax + (taxable_income - first_limit) * 0.30, 2)
  - balance: determined_tax - paid_advances - withholding_credit
expected:
  determined_tax: 53324290.71
  balance: 8324290.71
```

### 2. Ordinary loss or restricted securities loss?

Assume ARS 120,000,000 ordinary trading income and a documented ARS 20,000,000 loss, with no indexation difference, previous credits or special regime. If the loss is an eligible ordinary trading loss within its window, taxable income is 100,000,000 and tax 25,000,000. If it is instead a restricted securities loss with no same-source/type gain, it cannot shelter the ordinary income: taxable income remains 120,000,000 and tax 30,000,000. Classification changes current tax by 5,000,000. Both bases remain within the first 2026 band; source LIG art. 25. Do not elect a convenient loss classification.

```oa-check
name: Loss classification decision
inputs:
  ordinary_income: 120000000
  loss: 20000000
steps:
  - ordinary_loss_base: max(0, ordinary_income - loss)
  - ordinary_loss_tax: ordinary_loss_base * 0.25
  - restricted_loss_base: ordinary_income
  - restricted_loss_tax: restricted_loss_base * 0.25
  - tax_difference: restricted_loss_tax - ordinary_loss_tax
expected:
  ordinary_loss_base: 100000000
  ordinary_loss_tax: 25000000
  restricted_loss_base: 120000000
  restricted_loss_tax: 30000000
  tax_difference: 5000000
```

## Ask the client first

1. Legal form, tax classification/elections, fiscal-year opening/closing dates, CUIT and special-regime certificates.
2. Individual accounts, tax bridge, inventories, asset/depreciation and inflation-adjustment schedules, supporting invoices.
3. Loss origin/type/source/year, utilisation and IPC schedules; prior returns and disputed positions.
4. Foreign income/taxes, related-party dealings, financing terms and restrictions.
5. Withholding/perception certificates, actual advances paid and tax-account reconciliations.
6. Distribution/profit-year history, original filing medium, F.713/PUB acknowledgements and any advance-reduction decision.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for corporate scope, accrual, losses/rates and deductions: LIG arts. 1, 23-25, 53, 68, 73-74, 83, 85-88, 91-93, 105-109; quotations: "se inicien a partir del 1° de enero de 2025", "TREINTA Y SEIS (36) meses" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for financial-interest floor, measure, exceptions and oldest-first ordering; representation/director caps and fiscal fines: Decreto 862 arts. 192-200, 221-222, 227-229; quotations: "PESOS UN MILLÓN", "ejercicios fiscales de mayor antigüedad", "el TRES POR CIENTO (3 %) de las ventas o ingresos que se tomen como base contractual" | https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 | 2026-11-11 |
| Read for every indexed band/rate/fixed amount: ARCA corporate scale 2026, whole one-page table; quotation: "133.514.185,74" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/determinacion/documentos/Ganancias-Escala-PJ-2026.pdf | 2026-11-11 |
| Read for F.713/PUB and deadlines: RG 4626 current arts. 1-7; quotation: "quinto mes siguiente al de cierre" | https://biblioteca.arca.gob.ar/dcp/REAG01004626_2019_11_05 | 2026-11-11 |
| Read for new filing service and stages: RG 5908 arts. 1-4; quotation: "desde el 19 de octubre de 2026 hasta el 28 de febrero de 2027" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5908%7Co%3A9%7Ca%3A2026%7Cf%3A01%2F10%2F2026 | 2026-11-11 |
| Read for current form and amendment route: ARCA Presentación page; quotation: "El formulario de declaración jurada es el F. 713" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/presentacion.asp | 2026-11-11 |
| Read for advance base/payment/reduction conditions and codes: ARCA Anticipos page, general and special procedures; quotations: "9 anticipos", "11,11%", "F.2254" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/anticipos.asp | 2026-11-11 |
| Read for advance-calendar identification: ARCA 2026 PDF, title and CUIT/month tables; quotation: "Vencimientos 2026" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/documentos/Anticipos-Vencimientos-PJ.pdf | 2026-11-11 |

Not yet confirmed: precise 2027 CUIT return/payment dates and live F.713 web box numbering; current penalty amounts and interest; detailed historic inflation instalments and special investments; pre-2018 equalisation/transitional profit computation. Old approximate royalty rates, treaty count and general June extension are replaced by verified specialist routing or this explicit unresolved list, not repeated as facts.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ar-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ar-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
