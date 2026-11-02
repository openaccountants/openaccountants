---
name: es-autonomous-worker
description: Compute the 2026 tax, social contributions and cash position of a Spanish resident sole trader or professional. Covers autónomo registration, actual assessment-method selection, deductible expenses, simplified provisions, professional withholding, cumulative income-tax prepayments, VAT reconciliation and day-based RETA income banding. Distinguishes company controllers, family collaborators, TRADE arrangements and pluriactividad, and identifies the separate conditions for reduced contributions and new-activity relief. Use for cuota de autónomos, alta autónomo, Modelo 130, professional invoices, take-home profit or income-based regularisation questions. Includes an annual Madrid tax-to-cash reconciliation and a part-year contribution example. Common-territory computations are supplied; foral and island/city indirect taxes retain explicit limits.
version: 1.3
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - es-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain self-employment: 2026 tax, contributions and cash reconciliation v1.3

> Based on work by Nambu89 (Impuestify) and Pau March (larenta), licensed under MIT. Adapted for the OpenAccountants format.

## Who this applies to

This Guide computes the ordinary **2026** common-territory position of a Spanish-resident individual operating a business or profession. Select the actual activity, assessment method, tax territory and social-security legislation before calculating. It connects [annual IRPF](es-income-tax.md), [regional credits](es-irpf-deductions.md), [payments on account](es-estimated-tax.md), [VAT](es-vat-return.md) and [contributions](es-social-contributions.md); an autónomo's invoice cash is not their after-tax profit.

IRPF economic activity requires the organisation described in [LIRPF art. 27](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a27). RETA membership follows the distinct habitual, personal, direct, own-account and category tests in [LGSS art. 305](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a305). A low profit alone is not a statutory general exemption from registration. Tax residence, VAT establishment, customer location and social-security coverage are separate facts.

**Company workers.** Effective control under art. 305.2.b is conclusive at an own holding of at least half the capital; the rebuttable presumptions include at least half held by cohabiting family, an own holding of at least one third, or at least one quarter with management functions. The administration can establish control outside those presumptions. Company-paid income is **not automatically salary**: professional services covered by LIRPF art. 27.1 are activity income when its shareholder/RETA or alternative-mutual conditions hold. Director remuneration and other employment income require their own classification under art. 17. Keep corporate tax and the individual's tax/contributions separate.

**TRADE.** At least **75%** of work and activity income from one client is necessary but insufficient. Apply all [Ley 20/2007 arts. 11–12](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a11) conditions: own organisation, relevant independent infrastructure, distinct work from the client's staff, commercial risk and the employee/subcontracting restriction with its specified care/leave exceptions. The contract is written and registered. TRADE status does not itself fix an IRPF deduction, invoice withholding or VAT exemption.

## Rates, bands and thresholds

All amounts are EUR. These are 2026 ordinary common-territory rules unless stated otherwise.

| Item | Amount/test | Official source |
|---|---|---|
| Simplified direct assessment | Prior-year combined activity turnover no more than 600,000, annualised when required; no incompatible method or valid renunciation | [RIRPF arts. 28–29](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a28) |
| Simplified provisions and hard-to-justify expenses | 5% of positive qualifying net income before this item, combined annual cap 2,000; incompatible with elected art. 32.2.1 relief | [RIRPF art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a30) |
| Qualifying Ceuta simplified activity | 10% instead of 5%, same 2,000 cap; separate instalment commencement rule | [LIRPF DA 64](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-18) |
| Professional invoice withholding | 15%; eligible start tax period and next two 7%, with no professional activity in the preceding year and written notice | [RIRPF art. 95.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95) |
| Direct-assessment prepayment | 20% of cumulative net income, then statutory deductions/adjustments | [RIRPF art. 110](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| Professional exemption from prepayments | At least 70% of prior-year relevant income withheld; start-year covered-period test | [RIRPF art. 109.2/5](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a109) |
| Standard VAT | 21%; 10% and 4% only for specifically listed supplies, with dated exceptions | [LIVA arts. 90–91](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a90) |
| Ordinary RETA components | CC 28.30%, occupational 1.30%, cessation 0.90%, training 0.10%, MEI 0.90%; derived full-cover total 31.50% before exceptions/bonuses | [2026 order arts. 18 and 37](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10), [art. 37](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-9) |
| RETA generic deduction for band income | 7%; 3% for art. 305.2.b/e after 90 days in those categories | [LGSS art. 308.1.c](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308) |
| Company/family final-base floor | Group 7 minimum 1,424.40 once the 90-day test applies; separate 2025 provisional-base continuation | [LGSS art. 308.1.a.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308), [order art. 18.4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Pluriactividad | Refund 50% of combined CC above 17,323.68, capped at 50% of RETA CC paid | [Order art. 18.8](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| New-activity IRPF reduction | 20% of eligible positive net income, base capped at 100,000, first positive year and following year; statutory prior-activity/former-employer exclusions | [LIRPF art. 32.3](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a32) |

There is no single ordinary final “autónomo tax rate”. Apply the state and actual community scales and minima in [es-income-tax](es-income-tax.md), then credits and prepayments. The RETA bands, including all minimum/maximum bases, are reproduced in [es-social-contributions](es-social-contributions.md#rates-bands-and-thresholds).

## The base

### 1. Establish the tax method and keep records

Determine normal direct, simplified direct or objective assessment from the census/elections and prior-year data. Never default an unknown activity to professional withholding, VAT territory or simplified assessment. Keep the [RIRPF art. 68](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a68) income, expense, capital-asset and, for professions, provisions/advances books, or required mercantile accounts. Obtain invoices, payment evidence, business purpose and depreciation schedules.

For módulos, [LIRPF art. 31 and DT 32](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a31) must be read with the [2026 annual order](https://www.boe.es/buscar/act.php?id=BOE-A-2025-25272). The ordinary statutory non-farming receipts/business-invoicing/purchases baseline is **150,000/75,000/150,000**; farming/livestock/forestry receipts have their separate **250,000** ceiling. Current DT 32 ends its express extension at 2024 after the later extensions were left without effect. That textual baseline is distinct from AEAT's published 2026 administrative route: its [1 April post-repeal note](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html) expressly maintains the 2016–2024 limits for 2026, and the [current entry page](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html) specifies **250,000/125,000/250,000**. Apply that published route with the actual annual-order activity, specific magnitudes, aggregation, annualisation, territorial, compatibility and election conditions; do not exclude a trader solely by substituting the lower baseline for those published 2026 limits. An otherwise eligible trader with prior-year ordinary receipts 200,000, required-invoice B2B receipts 100,000 and relevant purchases 220,000 passes the three administrative numerical tests. This does not resolve the separate legal reconciliation of the statutory/repeal texts or a particular return correction. AEAT also confirms validity of renunciations/revocations made while the two decrees operated; preserve the filing and date and use the complete published election route in [es-estimated-tax](es-estimated-tax.md), including its limits on implicit renunciation and exceptional windows. The linked Guide supplies the payment worksheets; an actual module activity needs its annual-order units/indices, not accounting profit times 5%.

### 2. Compute direct-assessment activity income

Under [LIRPF arts. 28–30](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a30), start with the full activity receipts on the actual tax accounting basis. Deduct substantiated business expenses and tax depreciation, including the proprietor's eligible own RETA/alternative-mutual contribution. Keep recoverable input VAT outside both income and expenses; retain irrecoverable VAT where it forms part of the deductible cost or asset basis. Owner drawings, loan principal, income-tax withholding and Modelo 130 are not activity expenses.

| Cost requiring a special computation | 2026 method | Official source |
|---|---|---|
| Home supplies | 30% × separately evidenced business floor-area share × qualifying supplies, unless another higher/lower share is proved | [LIRPF art. 30.2.5.b](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a30) |
| Eligible health insurance | Up to 500 per covered proprietor/spouse/cohabiting child under 25; 1,500 per qualifying disabled person | [Art. 30.2.5.a](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a30) |
| Own business meals | Restaurant/hospitality and electronic payment; actual eligible cost within Spain 26.67 without /53.34 with qualifying overnight; abroad 48.08/91.35 | [Art. 30.2.5.c](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a30), [RIRPF art. 9](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a9) |
| Business assets | Actual allocation and depreciation. Indivisible mixed-use assets are not automatically deductible by an invented percentage | [RIRPF arts. 22 and 30](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a22) |
| Ordinary passenger vehicle | IRPF exclusive-use restriction with the article's specific transport/agent/hire exceptions; VAT's rebuttable 50% presumption is a different tax rule | [RIRPF art. 22.4](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a22), [LIVA art. 95.Tres](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a95) |

Apply the simplified 5%/2,000 combined item only after the qualifying expenses and before subsequent income reductions. Test [LIRPF art. 32](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a32) low-income, qualifying unrelated single-client/TRADE, disability, irregular and new-activity relief using the complete conditions and formulas in [the annual IRPF computation](es-income-tax.md#the-base). The single-client reduction and simplified provisions item are incompatible; first registration alone does not establish new-activity relief. A business fixed-asset disposal is separately a capital gain under art. 28.2, rather than another turnover receipt.

### 3. Independently band and regularise RETA

For direct assessment, build annual computable activity income by adding deducted own social/alternative-mutual contributions back to IRPF net activity income, then include the other statutory company/partner/attributed income in [LGSS art. 308.1.c](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308). Apply the appropriate 7%/3% generic deduction. A shareholder's relevant company work and equity income is not omitted merely because it is outside the sole trade.

Let D be **regularisable calendar days** after statutory benefit/reduced-fee exclusions. `monthly_band_income = annual_computable_income_after_generic_deduction / D × 30`. Do not substitute annual/12 or a count of monthly bank debits. Compare against the actual year's bands, choose a permissible base, and apply all covered components and eligible bonuses. Annual regularisation compares the day-weighted provisional base against the final band, retaining signed monthly differences, partial-month proportions and historical-base elections ([RD 2064/1995 arts. 44–46](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a44)). Use [the contribution Guide](es-social-contributions.md#the-base) for exclusions, final-base floors, notices and refunds.

**Starting reduction.** [Ley 20/2007 art. 38 ter](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a3-5) covers qualifying first registration or no registration in the preceding two years, three when previously enjoyed. Request it at registration. Its first period runs from effective registration through the following twelve complete calendar months; a requested further twelve needs annual computable income below annual SMI, with the stated annual tests. Qualifying disability of at least 33%, gender violence and terrorism cases have 24/36 complete months. It expressly extends to qualifying company/cooperative members and excludes the listed joining relatives/religious members. A baja ends the benefit. The general **new-2026 monetary amount is unconfirmed**: [RDL 13/2022 DT 5](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482) fixes amounts only through 2025, while the TGSS display does not reconcile its components. Record an individual's actual award/assessment without turning it into a general statutory amount.

**Other relief.** Qualifying family collaborators under [art. 35](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a35) receive 50% for eighteen months then 25% for six on CC at general-band-1 minimum, subject to prior-registration/relationship conditions. Company/family final floors still require testing. [Art. 36](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a36) changes qualifying Ceuta/Melilla CC relief from 50% to 75% for quotas accrued from **1 October 2026**; use each period's sector list and do not reduce MEI or every contingency. Pluriactividad includes employer and employee CC plus RETA CC before applying the excess/refund cap.

### 4. Reconcile invoice cash, VAT, annual IRPF and spendable income

For a taxable professional fee, `invoice cash = fee + output VAT − applicable withholding`. The withholding is credited on annual IRPF, not deducted as a cost. Private/non-obliged customers and foreign payers require their actual withholding analysis; a Spanish professional invoice does not automatically suffer 15% from every customer ([RIRPF arts. 75–76 and 95](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a76)).

Compute VAT separately: output VAT less **eligible**, evidenced input VAT, then period adjustments, prior credits and payment/refund treatment. Mixed business/private use and exempt activities can limit input recovery. A foreign client does not automatically make a service VAT-free; use LIVA place-of-supply and reverse-charge rules in [es-vat-return](es-vat-return.md).

Annual IRPF combines the correctly classified net activity amount with all other income, base reductions, state/community scales and distinct minima, credits and actual prepayments. Reconcile spendable annual cash as collected fees less actual business outflows, final net indirect tax, final personal tax and any contribution regularisation. Outstanding invoices, capital purchases, loan principal and timing differences prevent equating taxable profit with bank cash without a reconciliation.

## Deadlines and filing

| Obligation | Timing/route | Official source |
|---|---|---|
| Census registration | Modelo 036 before activity starts; actual activity/regime/withholding registrations. Modelo 037 was abolished from 3 February 2025 | [RGAT art. 9](https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984), [Orden HAC/1526/2024](https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410) |
| RETA | Registration/cessation and changes through TGSS with actual start/end/coverage information; use the statutory effective date and exclusions | [LGSS arts. 305/308](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308), [TGSS guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) |
| Modelo 130/131 if obliged | Q1–3 days 1–20 April/July/October; Q4 days 1–30 following January; applicable non-working-day extension. File the prescribed negative return when obliged but no payment | [RIRPF art. 111](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a111) |
| Ordinary quarterly Modelo 303 | First three quarters days 1–20 April/July/October; Q4 first 30 days following January; monthly/SII/REDEME routes differ | [RIVA art. 71](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a71) |
| Modelo 390 | Applicable January annual summary; exemptions depend on actual regime and final-period information | [Orden EHA/3111/2009](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472) |
| Annual Modelo 100 | Anyone registered in RETA at any time in the tax year files; 2026 income is filed in the prescribed 2027 campaign | [LIRPF arts. 96–97](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a96) |
| Payer withholding | If paying employees/professionals, apply the distinct 111/190 obligations in [es-modelo-111](es-modelo-111.md); business-rent 115/180 is a separate route | [RIRPF arts. 95/100/108](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108), [AEAT rent withholding](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/7-otras-obligaciones-fiscales-retenciones/7_3-retenciones-arrendamiento-bienes-inmuebles-180.html) |
| RETA base change | Requests Jan–Feb/Mar–Apr/May–Jun/Jul–Aug/Sep–Oct/Nov–Dec take effect March/May/July/September/November/following January | [RD 2064 art. 45](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a45) |

Apply actual direct-debit cutoffs separately. Determine Modelo 349, 347 and foreign-asset reports from the underlying transactions and exemptions, not simply from the existence of an autónomo registration. Preserve filing, payment and award evidence.

**Modelo 347.** Under [RGAT arts. 31–33](https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984#a33), an obliged operator normally reports a third party where the relevant calendar-year transactions **exceed 3,005.06**, counting deliveries and purchases separately and including the tax in the prescribed transaction amount. Check SII/reporting exclusions, operations already covered by a coincident specific return, invoice and other statutory exclusions before requiring the form. Exactly 3,005.06 does not exceed the threshold. Cash-scheme operations require the two statutory accrual views and annual information; do not omit one merely because the invoice was unpaid. File 347 **during February following the calendar year reported**, subject to the applicable non-working-day calendar and incorporated technical-presentation provision ([Orden EHA/3012/2008 art. 10](https://www.boe.es/buscar/act.php?id=BOE-A-2008-16973#a10), read 2026-10-27).

**Modelo 720.** The foreign-account, securities/rights/insurance/rents and foreign-property blocks have **separate 50,000 aggregate thresholds**, not 50,000 per asset or one combined allowance. For accounts test both year-end and last-quarter average balances; exceeding either aggregate triggers all reportable accounts. Apply actual ownership/authority/beneficial-owner status, each block's valuation rules and its exemptions, including the specifically conditioned commercial-accounting exemptions. Following a prior report, a block generally requires reporting on an **increase exceeding 20,000** against its last reported reference, with separate cessation/disposal reporting duties even without that increase. The statutory window is **1 January–31 March following the report year**, subject to the applicable calendar. These are information returns, not a wealth-tax allowance or authority to apply retired punitive rules ([RGAT arts. 42 bis/42 ter/54 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984#a42bis)). Foreign crypto custody uses the distinct 721 route in the crypto sibling, not automatic insertion into 720.

## Penalties and interest

Tax and Social Security collection have separate rules. For tax, [LGT art. 27](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) voluntary late payable returns without prior request carry **1% plus 1% per complete month** within twelve months; thereafter **15% plus interest after those twelve months**, with the conditional 25% surcharge reduction. [Art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a28) executive surcharges are 5%/10%/20% by payment stage. [Arts. 191 and 198](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a191) distinguish classified underpayment sanctions of 50–150% from ordinary non-economic late returns, generally 200 with the statutory no-request reduction. Default interest follows the applicable period rate under art. 26; [AEAT records 4.0625% under the continued 2026 budget](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html).

For contributions, [LGSS art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) applies 10% in the first late calendar month and 20% subsequently when the art. 29 duties were met; otherwise 20% before the demand/assessment period ends and 35% afterwards. [Art. 31](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a31) supplies interest exigibility and legal rate plus 25% relative uplift unless otherwise budgeted. A regularisation paid by its special notice deadline is not an ordinary late quota.

## Cross-border points

Common-territory residence does not eliminate foreign income: classify it and apply the actual treaty, source and foreign-credit rules in [es-income-tax](es-income-tax.md) and [IRNR/cross-border Guide](es-non-resident-income-tax-irnr-and.md). Foreign payers, digital-nomad status and an overseas account do not establish the incoming-worker election; [es-beckham](es-beckham.md) has its own eligibility and deemed-source computation.

Social-security legislation is selected independently. [Regulation 883/2004 arts. 11–13](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02004R0883-20190731) determines one applicable Member State, posting/multi-state exceptions and the employment-state rule for employment in one state plus self-employment in another. Obtain the actual determination/A1 evidence instead of assuming Spanish RETA from tax residence alone.

[VAT territory, LIVA art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a3), excludes Canarias, Ceuta and Melilla. This does not mean every invoice by a Canary-established trader bears IGIC: test place of supply, exemptions and reverse charge. Use [the ordinary2026 IGIC computation](es-canary-islands-igic.md), which reads Ley20/1991 alongside the current DL1/2025 regional consolidation and dated2026 amendments. Ceuta/Melilla use [the two city IPSI methods](es-ceuta-melilla-ipsi.md) and current ordinances. Foral residents use [the separate IRPF method](es-foral-income-tax.md); national social-security rules still require their own test. Each territorial Guide names any unresolved ordinary branch precisely.

## Two worked examples that recompute

### 1. Madrid professional: final tax versus invoice cash

Assume an established 40-year-old Madrid resident, individual return, unrelated multiple clients, no relatives/minimum additions, base reductions or tax credits. Annual collected fees are 60,000; wholly deductible paid costs excluding recoverable VAT are 20,000, including actual own contributions. Of the costs, 10,000 carries fully deductible 21% input VAT; remaining costs have no deductible VAT. All fees carry 21% VAT and 15% professional withholding. Prior-year 70% withholding exemption releases Modelo 130. The simplified allowance is 2,000, leaving general base 38,000. State/Madrid scales and personal minima produce 4,353.50 and 3,783.04 tax, as [LIRPF arts. 63/74](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a63) and [Madrid arts. 1–2](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068#a1) prescribe. Total 8,136.54 is settled against 9,000 withholding: refund 863.46. Cash after costs and net VAT before that refund is 31,000; final spendable cash is **31,863.46**, with no outstanding invoices, investment/financing movements or contribution adjustment. Actual contributions are an expense input, not proof a TGSS regularisation is nil.

```oa-check
name: Madrid professional annual tax and collected cash reconciliation
inputs:
  fees: 60000
  expenses: 20000
  vat_cost_base: 10000
steps:
  simplified: min(2000, max(0, fees - expenses) * 0.05)
  base: fees - expenses - simplified
  state_tax: round(4362.75 + (base - 35200) * 0.185 - 5550 * 0.095, 2)
  madrid_tax: round(3841.42 + (base - 35425.68) * 0.174 - 5956.65 * 0.085, 2)
  tax: state_tax + madrid_tax
  withholding: fees * 0.15
  output_vat: fees * 0.21
  input_vat: vat_cost_base * 0.21
  net_vat: output_vat - input_vat
  received: fees + output_vat - withholding
  cash_before_settlement: received - expenses - input_vat - net_vat
  refund: withholding - tax
  spendable: cash_before_settlement + refund
expected:
  simplified: 2000
  base: 38000
  state_tax: 4353.50
  madrid_tax: 3783.04
  tax: 8136.54
  net_vat: 10500
  cash_before_settlement: 31000
  refund: 863.46
  spendable: 31863.46
```

### 2. Part-year RETA and an invoice with withholding

Assume a non-company ordinary fully covered worker with 180 documented regularisable days, IRPF net activity income 10,000 and deducted own contributions 1,200. These are final tax-record inputs; no reduced-fee days, benefits or other computable activity income. Band income is `(10,000 + 1,200) × 93% /180 ×30 = 1,736`, general band 4, whose permitted base is 1,143.79–1,850. A chosen 1,200 base gives **378** for a full ordinary contribution month, before separate component rounding. It is not an asserted full-year quota. Separately a professional fee of 1,000 with 21% VAT and 15% withholding produces **1,060** collected, not 1,210 income or 850 profit. Actual expense documents, annual tax and the period's VAT worksheet are still needed to calculate final spendable cash.

```oa-check
name: Part-year day-based RETA plus professional invoice reconciliation
inputs:
  irpf_net: 10000
  own_contributions: 1200
  regularisable_days: 180
  chosen_base: 1200
  fee: 1000
steps:
  monthly_band_income: (irpf_net + own_contributions) * 0.93 / regularisable_days * 30
  cc: chosen_base * 0.283
  occupational: chosen_base * 0.013
  cessation: chosen_base * 0.009
  training: chosen_base * 0.001
  mei: chosen_base * 0.009
  full_month_quota: cc + occupational + cessation + training + mei
  invoice_vat: fee * 0.21
  invoice_withholding: fee * 0.15
  collected: fee + invoice_vat - invoice_withholding
expected:
  monthly_band_income: 1736
  full_month_quota: 378
  invoice_vat: 210
  invoice_withholding: 150
  collected: 1060
```

## Ask the client first

- What are your tax residence, community, establishment and actual work locations, and what applicable social-security determination exists?
- What activities/IAE categories, assessment methods and elections are registered, and what were prior-year turnover and withheld-income proportions?
- What complete receipts, expenses, VAT invoices, asset-use/depreciation records and withheld/prepaid-tax certificates support the year?
- What registration/cessation days, provisional bases, contribution payments, benefit periods and reduced-fee awards appear in TGSS records?
- Are you a company controller, director, partner, family collaborator or dependent contractor, and what company/other work income exists?
- What family, disability, start-up, regional-credit and foreign-income facts alter final IRPF or the contribution relief?

## Sources

[RGAT arts. 31–33/42 bis/42 ter/54 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984) reread **2026-10-27** for conditional reporting thresholds, exemptions, later-year triggers and windows.

| Official source | Purpose | Read on |
|---|---|---|
| [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764), arts. 17/27–32/63/74/96, DA 64 | Income classification, net activity, relief, annual tax and filing | 2026-10-26 |
| [RD 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820), arts. 9/22/26/28–30/68/95/109–111 | Expenses, method, records, withholding and instalments | 2026-10-26 |
| [Ley 20/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409), arts. 11–12/35–38 ter | TRADE and contribution relief | 2026-10-26 |
| [LGSS](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724), arts. 30–31/305/308/313; [2026 order](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296); [RD 2064/1995](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579) | Registration category, band income, day method, rates, regularisation, collection | 2026-10-26 |
| [RDL 13/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482) DT 5; [TGSS guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) | Starting-fee authority/display discrepancy | 2026-10-26 |
| [RGAT](https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984), art. 9; [HAC/1526/2024](https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410) | Census and abolished 037 | 2026-10-26 |
| [LIVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740); [RIVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925); [390 order](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472) | VAT territory, rates, allocation and filing | 2026-10-26 |
| [AEAT 115/180](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/7-otras-obligaciones-fiscales-retenciones/7_3-retenciones-arrendamiento-bienes-inmuebles-180.html) | Business-rent withholding form route | 2026-10-26 |
| [2026 module order](https://www.boe.es/buscar/act.php?id=BOE-A-2025-25272); [AEAT module-entry page](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html) | Earlier read of annual-order gateway and statutory/entry-page discrepancy; current administrative route supplied below | 2026-10-26 |
| [AEAT 1 April post-repeal note](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html), [current IRPF eligibility](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html) | Express 2026 administrative limits and valid renunciations; complete election method linked without treating repealed decrees as current law | 2026-10-28 |
| [Madrid D.Leg. 1/2010](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068), arts. 1–2 | Example's regional scale and personal minimum | 2026-10-26 |
| [LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186), arts. 26–28/191/198; [AEAT interest](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html) | Tax collection and sanctions | 2026-10-26 |
| [Regulation 883/2004](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02004R0883-20190731), arts. 11–13 | Applicable social-security legislation | 2026-10-26 |
| [Ley 4/2012](https://www.boe.es/buscar/act.php?id=BOE-A-2012-9282), arts. 51–57 | Canary rate framework; BOE consolidation marked updating, not a complete 2026 IGIC reconciliation | 2026-10-26 |

**Not yet confirmed:** general statutory amount for new 2026 reduced-fee awards and precise extension-boundary issues; legal reconciliation of the statutory/repeal texts with AEAT's published 2026 entry route, case-specific return corrections beyond its supplied election routes, and activity-specific module indices; the precisely outstanding branches in the linked foral IRPF/IGIC/IPSI Guides; specific foreign/treaty and special-system cases outside the ordinary routes. The final 2026 Modelo 100 campaign/schema for 2027 is not presumed from prior years. Independent whole-pack review remains pending.

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
