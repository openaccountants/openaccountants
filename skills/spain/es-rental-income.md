---
name: es-rental-income
description: Use this Guide to compute common-territory Spanish individual rental and own-use property income for 2026. It covers ownership and income classification, gross rent, property-specific interest and repair caps, other expenses, bad debts, depreciation and lifetime limits, residential net-income reductions, the October reform and December lease-date transition, relative lettings and imputed income. Trigger phrases include alquiler España, arrendamiento vivienda, rendimiento capital inmobiliario, reducción alquiler, amortización inmueble, gastos reparación, renta imputada and landlord tax Spain. Obtain actual lease and renewal dates, tenant use and age, prior rent and reference-price evidence, large-holder status, cadastral values, acquisition costs, rental days and prior expense ledgers. Resident rental results feed the full state and regional IRPF computation. Non-resident income, property businesses, corporate landlords and indirect-tax treatment have separate companion routes.
version: 1.5
jurisdiction: ES
tax_year: 2026
last_updated: 2026-11-28
drafted_by: OpenAccountants
approved_by: pending
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Spain: rental and own-use property income v1.5

Compute 2026 common-territory rental income property by property, then apply the correct lease-date relief and annual IRPF route. Establish residence, ownership, property use and the actual lease date before computing relief; do not default an unknown residence to IRPF or quote a state-only scale as the total Spanish rate.

## Who this applies to

[LIRPF art. 22](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a22) covers an individual's income from letting/ceding property or real enjoyment rights outside an economic activity. Identify the beneficial right, ownership share, use and lease dates. A sublessor's receipts and letting an operating business are **movable-capital income under art. 25.4.c** unless the activity rules apply; letting bare premises remains property income. The owner's rent from a tenant who sublets remains property income. Distinguish it from the owner's participation in the subletting price: [AEAT classifies that participation as property income but denies the housing reduction on it](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html). Do not grant the property-income housing reduction to the sublessor's movable-capital receipts ([LIRPF art. 25.4.c](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a25)).

Property letting is an economic activity under [art. 27.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a27) when its organisation uses at least one full-time employee under a genuine employment contract. The owner's own management does not satisfy that employment test. Hotel-type services can also change classification under the [AEAT explanation](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html). Do not decide income-tax or VAT classification from a tourist-registration label alone.

This Guide covers common-territory resident property income; `es-income-tax.md` computes its general state-plus-regional IRPF. Non-residents use `es-non-resident-income-tax-irnr-and.md`, including the 2026 revised filing periods and directly linked expense conditions. Foral taxpayers, corporate landlords, property economic activities and specialist indirect-tax territories need their applicable route. Their case-specific outcomes, and treaty or foreign-tax-credit amounts, are non-usable in this Guide. Check this point with one of our partner accountants.

## Rates, bands and thresholds

There is **no single resident rental-income tax percentage**. Reduced net rent joins the general base and is taxed through the state and applicable community scales, with the person's other income and minima. Do not substitute the payroll withholding table or savings scale.

| Expense/base rule | 2026 amount/condition | Official source |
|---|---|---|
| Interest/other finance costs **plus repairs/conservation**, per property | Combined deduction capped at that property's gross income; excess carries four following years under same cap | [LIRPF art. 23.1.a.1/RIRPF art. 13.a](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| Building depreciation, annual ordinary maximum | 3% of greater eligible acquisition cost or cadastral value, **land excluded** | [LIRPF art. 23.1.b/RIRPF art. 14](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a14) |
| Furniture/fittings | Applicable simplified-table coefficient, normally 10% for listed furniture/installations, subject to actual asset/category | [RIRPF art. 14.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a14), [AEAT depreciation guidance](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html) |
| Doubtful debt | Debtor in **concurso** proceedings, or **more than six months** since first collection attempt at year-end without credit renewal | [RIRPF art. 13.e](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a13) |
| Qualifying irregular income | 30% reduction, single-period inclusion, eligible net-income ceiling 300,000 | [LIRPF art. 23.3](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23), [RIRPF art. 15](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a15) |
| Own-use imputation | Generally 2%; qualifying 2026 revaluations effective from 1 January 2012 use 1.1% | [Operative art. 85](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764&p=20261002&tn=1#a85), [DA 55](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-10) |

### Choose the lease-date regime first

[Current DT 38](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) preserves different versions of art. 23.2. The October 2026 reform does not put every existing lease onto its newest ladder.

| Contract population | Applicable housing reduction | Source |
|---|---|---|
| Before 26 May 2023 | Preserved 60% rule under art. 23.2's 31 December 2021 wording | [DT 38.1, RDL 29/2026 art. 6.Segundo.Catorce](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823) |
| From 26 May 2023 through 30 November 2026; exact 1 December boundary held | Preserved 31 December 2025 ladder: 90/70/60/50% according to actual conditions | [DT 38.2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823) |
| New leases outside those preserved populations | Current art. 23.2 ladder below; document all price/landlord/tenant conditions | [Current art. 23.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |

For the preserved 2025 ladder, 90% requires the same landlord's new lease in a declared stressed area and **more than 5%** initial rent reduction against the appropriately uprated previous rent. Failing that, 70% applies to the specified first letting in a stressed area to an 18–35-year-old (proportionate to qualifying tenants), or the statutory public/nonprofit social/vulnerable-housing route. Failing those, qualifying rehabilitation completed in the prior two years gives 60%; otherwise 50% ([art. 23.2 operative older wording](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764&p=20261002&tn=1#a23)).

### Current ladder for a new post-transition lease

The following percentages reduce **positive net income**, not gross rent. For routes (a) and (b), the landlord must **not** be a gran tenedor when the contract is signed. Use the current [housing-law art. 3.k](https://www.boe.es/buscar/act.php?id=BOE-A-2023-12203) definition and any permitted stressed-area specification, not a guessed property count. Its general test is more than ten residential urban properties or more than 1,500 m² residential built area, excluding garages/storage. A motivated stressed-area declaration can particularise the test to five or more residential properties there. Separate residential units in one registered building count independently even without registered horizontal division; status is evidenced by the Property Registry certification. Check the actual declaration and holdings at signing.

| New-contract condition | Reduction | Source |
|---|---:|---|
| (a) Same landlord, initial rent cut **more than 5%** versus uprated prior rent: qualifying same-tenant renewal after statutory minimum/prorogations, or new tenant with rent below applicable reference-index limit | 100% | [Art. 23.2.a.1.a′](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| Same >5% cut; failing 100%: stressed area **and** tenant 18–35 | 95% | [Art. 23.2.a.1.b′](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| Same cut; failing preceding rows: stressed area | 90% | [Art. 23.2.a.1.c′](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| Same cut; failing preceding rows: tenant 18–35 | 85% | [Art. 23.2.a.1.d′](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| Same cut; remaining case | 70% | [Art. 23.2.a.1.e′](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| (a) Initial rent not above uprated prior rent, outside preceding branch | 50% | [Art. 23.2.a.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| (a) Rent increase: ≤5% / >5–10% / >10–15% / >15–20% / >20% | 40% /30% /25% /20% /15% | [Art. 23.2.a.3](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| (b) Landlord's first letting: rent below reference-index limit | 100% | [Art. 23.2.b.1](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| First letting; failing above: stressed area and tenant 18–35 / stressed area only / tenant 18–35 only | 95% /90% /85% | [Art. 23.2.b.2–4](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| First letting; other case, rent ≥reference-index limit | 50% | [Art. 23.2.b.5](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| (c) Statutory public/nonprofit social/vulnerable-housing or capped public-programme route | 70% | [Art. 23.2.c](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| (d) Qualifying rehabilitation finished in two years before lease | 60% | [Art. 23.2.d](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) |
| Qualifying tacit extension, non-large landlord and reference-price conditions, with five-year minimum expiring after 1 December 2026 | 80% for qualifying extension income, including otherwise preserved leases | [Art. 23.2/DT 38 final paragraph](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823) |

Choose the highest **actually applicable** current reduction if several qualify, maintaining the conditions. Do not grant routes (a)/(b) to a large holder or invent a residual 50% where no statutory route is met. Age-conditioned reductions are proportionate where only some tenants qualify. Keep the housing-authority price/reference and stressed-zone evidence current for the actual contract. Exact boundary cases at 1 December remain separately flagged below; the example uses 15 December.

## The base

### Property income, expenses and depreciation

Start from everything payable for the letting, including goods let with it and tenant payments of the landlord's obligations, excluding separately charged VAT/IGIC under [LIRPF art. 22.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a22). Identify refundable deposits separately until their actual retention/application; do not automatically classify a retained deposit or damages payment without the contract and purpose. A disputed deposit classification is non-usable here. Check this point with one of our partner accountants. Use [art. 14](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a14) accrual rules; a missing bank receipt does not automatically eliminate rent due.

Under [RIRPF art. 13](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a13), deduct necessary supported interest/finance, repairs, non-penalty property taxes, community/management/caretaking, insurance, utilities, legal/formalisation costs and qualifying bad debts. Keep improvements/enlargement as capital, not repairs, and mortgage principal as capital repayment. The owner's payment to end a lease early is treated as an improvement, while compensation received by the owner when the tenant terminates is property income under the cited [AEAT classification](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html); classify who pays whom and why. A previously deducted bad debt later collected returns to income in collection year.

For the first ordinary doubtful-debt route, **concurso** under RIRPF13.e.1 is the specified insolvency-proceeding status; an unpaid balance or a debtor's financial difficulty alone is not proof of that status. Alternatively, under13.e.2, retain evidence of the landlord's **first collection action**, require **strictly more than six months** between it and the tax-period end, and verify no credit renewal. For a normal31December2026 year-end and no concurso, a first collection action on1July2026 does not satisfy that timing route; one on30June2026 does. With otherwise qualifying unpaid rent EUR1,000 already included in gross income, the latter facts support a EUR1,000 doubtful-debt expense; the1July facts alone support none under that route. The finance/repair gross-income cap does not extend to this separate expense. Later recovery of an amount actually deducted is income in the recovery year. The exceptional three-month rule for2020/2021 is not the2026 threshold ([RIRPF13.e](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a13)).

For each property, let G be gross income, F current qualifying finance-plus-repair costs and C eligible earlier capped costs. Apply `capped_deduction = min(G, F +eligible_C)` in the statutory expiry/order schedule and preserve unused amounts by origin year. **Only this class is capped at gross income**. Other expenses and depreciation can create a negative net property result. Do not offset one property's unused repair limit against another property's rent.

For the building, remove land from eligible acquisition value and cadastral value. If needed, allocate acquisition cost using the year's cadastral construction/land ratio. Annual maximum is `0.03 ×max(eligible_acquisition_building_value, cadastral_building_value)`, prorated for entitled rental days and ownership, and capped by **remaining depreciable acquisition value**. A higher cadastral basis does not create an unlimited lifetime deduction. For inherited/gift property use the supported art. 36/ISD acquisition value and costs, not only cash inheritance expenses. These annual/lifetime and inherited-value principles are explained in the [AEAT depreciation page](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html), including the identified Supreme Court/TEAC criteria. Retain the actual lawful depreciation schedule for later gain basis; do not double deduct an asset purchase. A later-sale dispute about minimum depreciation or previously undeducted amounts is non-usable here. Check this point with one of our partner accountants.

For a purchased real use/enjoyment right, depreciate its acquisition cost over its fixed duration, or at 3% if for life, in either case capped at gross income from that right. Furniture used for more than one year follows its actual simplified-table category (10% maximum for listed installations, furniture and fittings), rather than an immediate deduction. [RIRPF art. 14](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a14).

### Apply relief to each positive property result

`net_rent = gross_rent −capped_finance_repairs −other_allowed_expenses −allowed_depreciation`.

If qualifying positive net rent, select the lease-date branch and reduction r: `housing_reduction = max(net_rent,0) ×r`; `taxable_net_rent = net_rent −housing_reduction`. A negative result is **not** multiplied by 40% or 50%. Apply reductions before aggregating different properties, so a positive property's relief does not shrink another property's loss.

Housing relief applies only to the statutory permanent-home use and properly declared positive net income before a verification/review/inspection procedure begins. It does not cover omitted income/incorrect expenses regularised in that procedure, or contracts violating the specified LAU rent limitation ([art. 23.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23)). Seasonal/tourist use does not become permanent housing merely because the building is residential. The identified corporate-tenant residential-use method is supplied below. Rehabilitation uses [RIRPF art. 41.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a41), either the specified subsidised rehabilitation route or the reconstruction/structural route with cost strictly exceeding 25% of the relevant acquisition value (if acquired within the preceding two years) or otherwise market value, excluding land. Ordinary repainting alone is not rehabilitation.

**Company tenant under preserved housing wording.** Where DT38 preserves the earlier art.23.2 wording, a company paying the rent does not by itself disqualify an individual landlord from housing relief. [TEAC00/05138/2013,8September2016](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00%2F05138%2F2013%2F00%2F0%2F1) establishes the route when the dwelling is proved to be the permanent home of identified natural persons. The [exact AEAT2025 housing explanation](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda.html) requires the exclusive residential use of a particular natural person to be established from the outset; a generic contractual destination for the company's employees does not qualify under that explanation. Retain the lease, identification of the actual occupant and family where applicable, the residential-use terms and evidence of actual permanent occupation.

Within that preserved population, choose the independently applicable preserved art.23.2/DT38 lease-date percentage above and apply it to eligible declared positive net income. Do not import the old50% percentage quoted in the2009 dispute into2026. Nor does an employee's age alone prove a higher-rate route whose actual statutory conditions concern the tenant. For a continuing lease signed1January2020, identified permanent-home use from the outset, all preserved60% conditions met, and12,000 net income after allowed expenses, housing relief is7,200 and reduced net4,800. An otherwise identical lease merely giving the company a generic right to house unspecified employees does not establish this relief; absent another applicable relief, reduced net remains12,000. A genuine seasonal stay also fails the permanent-home test. The new post-transition2026 art.23.2 expressly refers to LAUart.2.1, whereas TEAC's reasoning concerned earlier wording without that express incorporation. The supplied company-tenant conclusion therefore covers the preserved wording; the effect of the new reference on a post-transition company lease, including any company-tenant claim to the new-text80% tacit-extension route even where the original lease is older, is non-usable here. Check this point with one of our partner accountants. No automatic entitlement or universal denial is asserted for that new population. These are the individual's IRPF housing rules; VAT exemption and the employer's benefit-in-kind treatment follow their separate companion methods ([currentLIRPF23/DT38](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23); [AEAT housing-use boundary](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda.html)).

**Housing relief before irregular-income relief.** Test each entitlement independently. Under [LIRPF art.23.3](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23), the 30% route requires generation over more than two years or the specific regulatory irregular-income category, with inclusion in one tax period. Ordinary monthly rent does not acquire that status because the lease lasts several years. [RIRPF art.15](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a15) lists the owner's business-lease transfer receipts, tenant/subtenant/assignee compensation for property damage, and lifetime use/enjoyment rights. A tenant's own lease-transfer proceeds instead follow the capital-gain route. Keep the specific pre-2015 instalment transition in LIRPF DT25.3 separate from a new receipt's single-period condition ([AEAT ordering and categories](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/rendimientos-periodo-generacion-superior-dos-anos.html)).

For an amount independently qualifying for both routes, first calculate the applicable housing reduction on its eligible positive net income. Apply 30% only to the resulting qualifying irregular net amount, subject to the **300,000 annual irregular-income base ceiling**. The ceiling is tested after housing relief, not against the original rent. For one positive qualifying component and no competing irregular income, let `N` be its net income after expenses, `h` its independently established housing-reduction rate and `R=N×(1−h)`; the further reduction is `30%×min(R,300,000)`, and reduced income is `R` minus that amount. These conditions do not grant housing treatment to a commercial lease or make an otherwise regular receipt irregular. AEAT expressly applies this order; the current2026 law retains art.23.3 while the applicable housing percentage is selected under the actual art.23.2/DT38 lease route ([AEAT method](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/rendimientos-periodo-generacion-superior-dos-anos.html); [current law](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23)).

Hypothetical controls assume both entitlements have already been established and there are no other irregular amounts. With net10,000 and preserved housing relief60%, housing relief is6,000, leaving4,000; irregular relief is1,200 and taxable net2,800. The percentages are successive: adding60%+30% against the original10,000 would be wrong. If a separately qualifying current route gives90% housing relief, the same10,000 leaves1,000, then300 irregular relief and700 taxable net;100% housing relief leaves no further irregular base. Net800,000 with independently established50% housing relief leaves400,000: only300,000 receives30%, so irregular relief is90,000 and taxable net310,000.

For several irregular amounts, retain their post-housing values and apply the annual ceiling across the taxpayer's claim. AEAT requires the algebraic sum of positive and negative irregular amounts; do not discard a negative amount before testing that ceiling. Where all the irregular amounts concerned are positive and their same-nature total exceeds the ceiling, distribute the maximum reduction proportionately. For post-housing amounts200,000 and400,000 with no other irregular amounts, the300,000 base splits100,000/200,000; relief is30,000/60,000, leaving170,000/340,000. These positive controls do not replace the signed treatment required for a negative irregular amount ([AEAT annual cap and apportionment](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/rendimientos-periodo-generacion-superior-dos-anos.html)). Keep a relative letting's [2026 art. 24](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764&p=20261002&tn=1#a24) minimum-result test, covering spouse/relatives through the third degree including affinity, against the relevant property imputation. The amended 2027 relative/imputation formula is not the 2026 rule.

### Partial use, indirect tax and annual handoff

Allocate ownership, rental days and non-rental use consistently across income, time-related expenses and depreciation. Ordinary vacancy while awaiting a tenant does not itself remove imputation or make vacancy-period running costs deductible. A disputed pre-letting repair or mixed-use cost allocation is non-usable here. Check this point with one of our partner accountants.

For 2026, ordinary nonbusiness/non-rented urban property and qualifying nonessential rural construction, excluding the main home and undeveloped land, generally produces imputed income of cadastral value ×2%, apportioned to relevant ownership/available days. DA55 applies 1.1% where municipal values were revised/modified/determined by a general collective valuation effective from 1 January 2012. If cadastral value is absent or unnotified at accrual, use 1.1% of 50% of the greater administratively checked value or acquisition price/value. No imputation for construction or urban-planning inability to use; a bare assertion of vacancy or damage does not prove that exception. Real enjoyment rights determine who reports it. [2026 art.85](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764&p=20261002&tn=1#a85), [DA55](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-10). For a resident, include eligible imputation in the general base; a vacant investment property is not automatically the taxpayer's exempt main home. The future aggregate progressive imputation scale starts **2027**, not 2026.

For VAT, use `es-vat-return.md`. The 2026 December amendment can remove exemption from the specified furnished stays of no more than thirty nights outside the landlord's main home, in addition to the hotel-service route. It does not by itself turn every tourist let into an IRPF economic activity or permanent-home relief case ([RDL 29/2026 art. 7](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823)). Keep income-tax category, VAT and tourist licensing as separate tests.

Aggregate the computed property results and imputation with other **general** income, then run the state/community/minimum/credit procedure in `es-income-tax.md`. A tenant's withholding is a tax prepayment, not a rental expense. The resident urban-rent rate is ordinarily 19% on subject payments excluding VAT, with statutory payer/exemption conditions ([RIRPF arts. 75/76/100](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a100)); do not apply professional Modelo 111 to it. A non-resident uses the distinct IRNR rate/base/withholding and 210 route.

### Urban-rent withholding exceptions

After establishing that the payer must withhold under RIRPF art. 76, apply the art. 75.3.g exclusions: a company renting housing for its employees; annual rent paid by the same tenant to the same landlord **not exceeding 900, excluding VAT**; or a landlord in IAE group 861 (or another authorising letting/subletting heading) for whom applying group 861's rules to the rented properties' cadastral values produces a **nonzero quota**, evidenced to the tenant through the required certification. An IAE exemption or registration alone is not that certificate. A private tenant paying outside an economic activity does not acquire a withholding duty merely by paying more than 900. Where the urban property is in Ceuta/Melilla and meets LIRPF art. 68.4, art. 100 cuts the **19% rate by 60%**, giving a derived **7.6%**; it is not a 60-point cut ([RIRPF arts. 75.3.g/76/100](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a75)).

## Deadlines and filing

Residents use Modelo 100 for the accrual year under the approved campaign. Exact 2026-return campaign dates, boxes and payment-option deadlines for filing in 2027 are non-usable here until their own approved form/calendar is established. Check this point with one of our partner accountants. Preserve each property's lease, price history/index/zone evidence, beneficial ownership, IBI values, finance/repairs carry ledger, depreciation schedule and withholding certificate.

For non-residents, 2026 own-use 210 has the new **1 April–31 December 2027** window, and payable annual rental grouping has **1–20 April 2027**. Ungrouped rental accruals through September 2026 retain the relevant quarterly route; from October the new following-April route applies. Nil 210 returns are due 1–20 January following accrual; refund returns can start 1 February following accrual and have the four-year period counted from the end of the withholding declaration/payment period, not automatically four years from the rental receipt. Filing and direct-debit deadlines are distinct; for the new rental route direct debit is 1–15 April, and for imputation 1 April–23 December of the following year. Grouping requires the same taxpayer, income-type code, rate and property/right, normally also the same payer; nonwithheld rent may combine payers for that same property using code35. Grouped rents cannot offset one another. Do not group different properties or co-owners into one income merely because they share an agent. These rules and the commencement provisions govern ([210 order art. 5](https://www.boe.es/buscar/act.php?id=BOE-A-2010-19707#a5); [2026 amendment/commencement](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13573)). Refer to the complete `es-non-resident-income-tax-irnr-and.md#deadlines-and-filing` before selecting a period. Resident business-rent withholding is paid through Modelo 115 and reported annually on Modelo 180; use the [AEAT rent-withholding procedure](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/7-otras-obligaciones-fiscales-retenciones/7_3-retenciones-arrendamiento-bienes-inmuebles-180.html).

The old tourist-intermediary **Modelo 179 ceased for 2024 and later years**. RD 117/2024's platform reporting replaces that real-estate information: **040** manages registration/change/deregistration in the platform-operator register, and **238** communicates reportable platform information under its operator/seller/property tests. These are operator obligations, not automatic landlord returns; a landlord still reconciles their own taxable income to platform statements ([AEAT 179 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-179-decla_____la-cesion-uso-turisticos/preguntas-frecuentes.html); [Orden HAC/72/2024](https://www.boe.es/buscar/doc.php?id=BOE-A-2024-2092)).

## Penalties and interest

Use [LGT arts. 26–28/191/198](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27): unprompted late tax-due filing generally has 1% plus 1% per complete month until the statutory twelve-month switch; once twelve months have elapsed, 15% plus interest from the day after twelve months until filing. The 25% surcharge reduction requires the statutory payment conditions; it is not automatic. Under-declaration, information failures, enforcement, interest rates and assessment/remedy outcomes need their own conditions. No actual penalty, interest or remedy amount is supplied here. Check this point with one of our partner accountants. A housing reduction can be unavailable on income/expense amounts found in an initiated check under art. 23.2; late payment interest is not a substitute for meeting the substantive relief conditions. Do not put an assumed universal landlord fine into the deductible expense schedule.

## Cross-border points

For a nonresident individual without a permanent establishment, ordinary statutory Spanish-property rent is taxed at 24% on gross income. Residence in another EU state or a qualifying EEA state with effective exchange of tax information gives the 19% rate and permits the IRPF expenses proved directly and inseparably linked to the Spanish income; residence and expense evidence are essential. Resident housing reductions do not automatically transfer to IRNR. Third-country expense/refund claims or EU-law disputes are non-usable here: neither a universal entitlement nor an outcome on a challenge is asserted. Check this point with one of our partner accountants. A resident's foreign-property rent enters worldwide IRPF with the actual treaty/source/foreign-tax-credit analysis. A foreign account or agent does not establish tax residence or source. Preserve applicable treaty and foral allocation evidence; do not reduce Spanish tax by an unverified treaty assumption ([TRLIRNR arts. 13/24/25](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a24); [LIRPF arts. 2/80](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a80)).

## Two worked examples that recompute

### 1. Full-year preserved lease, depreciation and 50% reduction

A hypothetical resident's permanent-home lease was signed in 2024 and remains within the preserved 2025 ladder, with no enhanced conditions. Gross 2026 rent is **12,000**. Qualifying interest/repairs are 2,000, other supported expenses 1,000. Total eligible acquisition value is 150,000, of which 80% is building; total cadastral value is 100,000 with the same construction share. It is rented all year, no accumulated cap is exhausted. Building depreciation at the chosen lawful 3% is `max(120,000,80,000) ×3%=3,600`. Net is **5,400**, 50% relief **2,700**, taxable general-base rental income **2,700**. Annual IRPF then depends on the person's full state/regional computation ([art. 23/DT 38](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823); [RIRPF art. 14](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a14)).

```oa-check
name: Spain 2026 preserved residential lease and depreciation
inputs:
  gross_rent: 12000
  finance_repairs: 2000
  other_expenses: 1000
  acquisition_total: 150000
  cadastral_total: 100000
  building_share: 0.80
steps:
  capped_expenses: min(gross_rent, finance_repairs)
  depreciation_base: max(acquisition_total * building_share, cadastral_total * building_share)
  depreciation: depreciation_base * 0.03
  net_rent: gross_rent - capped_expenses - other_expenses - depreciation
  housing_reduction: max(net_rent, 0) * 0.50
  taxable_net: net_rent - housing_reduction
expected:
  depreciation_base: 120000
  depreciation: 3600
  net_rent: 5400
  housing_reduction: 2700
  taxable_net: 2700
```

### 2. Capped repair carryforward, unreduced loss and qualifying December first lease

A hypothetical resident's property A earns **4,000**, with qualifying finance/repairs **6,000**, other expenses 800 and valid depreciation 1,200. Deduct only 4,000 finance/repairs; carry **2,000** in that property's four-year capped-cost ledger. Other expenses/depreciation give **−2,000 net**, with no housing reduction.

The same owner acquires property B on **15 December 2026** and immediately makes its first permanent-home lease. Documentary facts establish that the landlord is not a large holder and the initial rent is **below** the legally applicable reference-price limit; all current art. 23.2.b.1 conditions hold. December gross rent is 1,200, with 200 properly computed allowable expenses/depreciation. Net **1,000** receives **100% reduction**, leaving zero taxable rental net. B has no own-use days during this ownership. Combined taxable rental result is **−2,000**, not a loss reduced by 50% or 100%. Other general income and annual loss/minimum rules are still required for final IRPF ([LIRPF art. 23](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23); [RDL 29/2026 art. 6/DT 38](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823)).

```oa-check
name: Spain 2026 property-specific cap and December housing relief
inputs:
  a_rent: 4000
  a_finance_repairs: 6000
  a_other: 800
  a_depreciation: 1200
  b_rent: 1200
  b_allowed_expenses: 200
steps:
  a_capped_deduction: min(a_rent, a_finance_repairs)
  a_carryforward: a_finance_repairs - a_capped_deduction
  a_net: a_rent - a_capped_deduction - a_other - a_depreciation
  a_reduction: max(a_net, 0) * 0.50
  b_net: b_rent - b_allowed_expenses
  b_reduction: max(b_net, 0) * 1.00
  total_taxable_rental: a_net - a_reduction + b_net - b_reduction
expected:
  a_carryforward: 2000
  a_net: -2000
  a_reduction: 0
  b_net: 1000
  b_reduction: 1000
  total_taxable_rental: -2000
```


### Historical numerical controls retained

The earlier purchase illustration keeps its **2025** setting: purchase price 200,000, land40%/building60%, hence acquisition building value120,000 and maximum annual depreciation3,600 at3%, assuming cadastral construction value is no higher, full-year letting and available lifetime basis. If the cadastral building value is higher or the remaining lifetime basis lower, those original inputs alone do not determine the deduction; do not silently change them. An actual 2025 filing amount is non-usable without those missing facts. Check this point with one of our partner accountants.

The earlier AEAT inherited-property illustration keeps ISD value100,000, acquisition costs/taxes2,000, cadastral value80,000 and land20%/building80%: eligible acquisition building value81,600 exceeds cadastral building value64,000; maximum annual depreciation2,448 and lifetime acquisition-value cap81,600. This is the original illustration from the 2025 manual, not a newly invented acquisition year. [AEAT depreciation example](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html).

The original 2025 net10,000 →4,000 example remains valid where the **preserved60%** housing route is independently established; it is not a universal reduction for every residential contract. No original year or numerical input is substituted.

```oa-check
name: Historical 2025 purchase and inherited-property depreciation controls
inputs:
  purchase_price: 200000
  purchase_building_share: 0.60
  inherited_isd_value: 100000
  inherited_costs: 2000
  inherited_cadastral: 80000
  inherited_building_share: 0.80
steps:
  - purchase_building: purchase_price * purchase_building_share
  - purchase_annual_maximum: purchase_building * 0.03
  - inherited_building: (inherited_isd_value + inherited_costs) * inherited_building_share
  - inherited_cadastral_building: inherited_cadastral * inherited_building_share
  - inherited_annual_maximum: max(inherited_building, inherited_cadastral_building) * 0.03
expected:
  purchase_building: 120000
  purchase_annual_maximum: 3600
  inherited_building: 81600
  inherited_cadastral_building: 64000
  inherited_annual_maximum: 2448
```

## Ask the client first

1. What residence/territory, beneficial ownership and actual rental/business use applies to each property?
2. What lease/renewal dates, earlier uprated rent, tenant ages/use, large-holder status and official price/zone evidence establish the correct relief?
3. What gross payable rent, refunds/deposits and withholding reconcile to the lease, payment and accrual records?
4. Which finance/repairs, other expenses, bad debts, prior capped costs and depreciation schedules are evidenced property by property?
5. What construction/land values, acquisition/improvement dates and rental/own-use days support annual and lifetime depreciation and imputation?
6. What other annual income, regional minima/credits, foreign tax and prior filings affect final tax and correction?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [LIRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764), [operative older art. 23/24/85](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764&p=20261002&tn=1) | Property classification, capped expenses, reductions, relative minimum and imputation, with separate effective periods | 2026-11-28 |
| [RDL 29/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823) | Art. 6 new reduction ladder and DT 38 lease-date preservation, DA 55 for 2026, future 2027 imputation; art. 7 December VAT change | 2026-11-28 |
| [RIRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820), [housing law art. 3.k](https://www.boe.es/buscar/act.php?id=BOE-A-2023-12203) | Expenses, bad debts, depreciation/rehabilitation and landlord classification; housing law read through official web tool | 2026-11-28 |
| [AEAT depreciation guidance](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html), [classification guidance](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html) | Existing inherited-cost/lifetime-cap research and use/activity distinctions; manual is labelled 2025 and not substituted for the 2026 statutory transition | 2026-11-28 |
| [IRNR law](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527), [210 order](https://www.boe.es/buscar/act.php?id=BOE-A-2010-19707), [2026 amendment](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13573) | Non-resident rate/base and revised rental/own-use filing periods | 2026-11-28 |
| [LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Conduct-based correction, interest and penalty rules | 2026-11-28 |

| AEAT business-rent withholding, Modelos 115/180 | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/7-otras-obligaciones-fiscales-retenciones/7_3-retenciones-arrendamiento-bienes-inmuebles-180.html | 2026-11-28 |
| [RIRPF arts. 75.3.g/76/100](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a75), [LIRPF art. 25.4.c](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a25), [AEAT 179 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-179-decla_____la-cesion-uso-turisticos/preguntas-frecuentes.html), [HAC/72/2024](https://www.boe.es/buscar/doc.php?id=BOE-A-2024-2092) | Subletting/business classification, conditional rent withholding exceptions and territorial reduction, operator 040/238 replacing 179 | 2026-11-28 |
| [AEAT irregular property-income reductions](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/rendimientos-periodo-generacion-superior-dos-anos.html), [LIRPF23.3](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a23) and [RIRPF15](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a15) | Housing-first computation, post-housing annual irregular base, separate entitlement and proportional same-nature cap allocation; 2025 administrative explanation of unchanged23.3 method | 2026-11-28 |
| [TEAC00/05138/2013,8September2016](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00%2F05138%2F2013%2F00%2F0%2F1), [AEAT housing-use/company-tenant explanation](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda.html) | Preserved-wording exclusive identified permanent-home use from outset; generic employee use excluded; actual preserved rate selected separately from historical dispute rate; new express-LAU-reference population unconfirmed | 2026-11-28 |

**Not yet confirmed / non-usable outcomes:** exact treatment of a lease signed on the 1 December transition boundary; a replacement contract versus a continuing/novated lease where facts are disputed; case-specific reference-index/zone eligibility, the effect of the new express LAUart.2.1 reference on post-transition company leases or a company-tenant claim to the new80% tacit-extension route, and foral allocation. The ordinary expense, depreciation, lease-date and own-use routes above are supplied. Check this point with one of our partner accountants.

> Contributed by OpenAccountants.
