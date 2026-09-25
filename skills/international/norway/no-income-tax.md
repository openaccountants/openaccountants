---
name: no-income-tax
description: Use this skill whenever asked about Norwegian income tax for self-employed individuals (enkeltpersonforetak). Trigger on phrases like "Norwegian tax", "trinnskatt", "alminnelig inntekt", "personfradrag", "skattemelding", "RF-1175", "naeringsoppgave", "enkeltpersonforetak", "self-employed tax Norway", or any question about filing or computing income tax for a Norwegian self-employed client. Covers alminnelig inntekt (22%), trinnskatt (5 brackets), personfradrag, naeringsinntekt computation, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Norwegian income tax work.
version: 2.0
jurisdiction: "NO"
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway income tax: 2026 sole-proprietor calculation and return

Figures are for tax year 2026. For income earned in **2026**, normally reported in **2027**. A return submitted during **2026** for **2025** income needs that earlier year's rates. This Guide covers ordinary Norwegian sole proprietors (*enkeltpersonforetak*, ENK), including owners with wages. Amounts are NOK. Figures and procedures were researched in September 2026; the business shielding rate is established after year-end.

## Ask the client first

- Confirm income year, tax residence and residence dates, tax municipality, National Insurance coverage, age and business activity. Obtain coverage decisions where work crosses borders.
- Obtain the ledger, invoices, platform gross-sales/fees statements, bank reconciliations, VAT records, stock and receivables/payables lists, asset register and disposals. A bank export alone does not establish taxable profit.
- Obtain salary/benefit statements, private interest and other deductions, ordinary tax losses, negative calculated business personal income, spouse participation, advance payments and withholding.
- Check whether the taxpayer was selected for the young-person work-deduction trial. Age alone does not confer entitlement.
- For mixed costs obtain business-purpose evidence, phone bills, office use, vehicle classification, travel logs and meal attendees. Identify any grants, related-party withdrawals or foreign transactions.

## The method, step by step

1. Establish business, residence, municipality and coverage status; choose the correct income year.
2. Reconcile income and expenses to taxable business profit, including VAT, timing, stock, private use and tax depreciation.
3. Calculate business *personinntekt* using the capital/interest/shield/loss bridge below; retain it separately from ordinary income.
4. Combine the owner's ordinary income and deductions; calculate ordinary-income tax, bracket tax and National Insurance separately.
5. Apply eligible deductions and tax credits once, reconcile withholding and advances, submit the whole personal return with business information, and retain the calculation and submission receipt.

## Establish the scope

Business requires profit potential, sufficient duration and extent, and operation for the owner's own account and risk. Registration or payment-platform labels do not settle that question. Occasional independent work can instead be employment-type income; passive investments can be capital income. A low turnover does not make a genuine business tax-exempt. Decide rental classification from the actual activity, rather than classifying every rent receipt alike. [Business criteria](https://www.skatteetaten.no/bedrift-og-organisasjon/starte-og-drive/er-jeg-naringsdrivende/)

The calculation below assumes a full-year resident with ordinary taxable activity and confirmed Norwegian coverage. Non-residence, part-year residence, treaty allocation, foreign tax credit, Svalbard, agriculture/fishing special deductions and pension-credit computations need their specific additional rules. Do the ordinary domestic portions below while resolving those identified branches. Membership is a separate decision from tax residence or citizenship. [National Insurance membership](https://www.nav.no/en/home/rules-and-regulations/membership-of-the-national-insurance-scheme)

## Reconstruct business profit

Taxable operating revenue includes earned sales and relevant fees, commissions, royalties, grants and benefits in kind. Recognise earned credit sales in the earning year even if paid later. Record sales excluding output VAT where charged. Reconcile gross customer sales, refunds, fees and net platform payouts; never treat the bank payout as automatically equal to turnover. Separate loans, transfers and owner cash drawings from sales. Owner withdrawals of goods/assets/services can require income at market value, unlike a transfer of already-earned cash. Check grant exemptions individually. [Business income and timing](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/inntekt-i-enkeltpersonforetak/)

For each expense record invoice, supplier, date, purpose, business/private split, VAT recovery and whether capital or current expenditure. Deduct business operating costs; exclude personal consumption and income-tax payments. Fines and penalty-type charges imposed under law, such as traffic fines and additional tax, are not deductible even when incurred in the business. A cost of **NOK 10,000** or more is deductible only if it was paid through a bank or another licensed payment provider (settlement by set-off is the exception); several payments in the same calendar year for the same delivery, contract or recurring service count as one payment, and if part is paid another way only the bank-paid part is deductible. Recovered input VAT is not another income-tax cost; unrecovered VAT follows the underlying expense or asset. Reconcile opening/closing stock and receivables, bad debts and accruals rather than assuming every payment is an immediate deduction. Use the tax adjustment schedule where accounting and tax treatments differ. The return needs both business income and expenses, not an unexplained net bank total. [Cost connection/private exclusion](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/k-4-kostnader--allment-om-fradrag/K-4.010/K-4.011/); [Bank-payment condition](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/k-4-kostnader--allment-om-fradrag/K-4.021/K-4.025/); [Fines](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/b-21-bot-gebyr-mv/B-21.001/B-21.002/); [VAT and acquisition cost](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/i-3-inngangsverdi/I-3.018/I-3.019/) [Business information and preparation](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/sole-proprietorships/)

### Common expenses and private use

| Item | Treatment and evidence |
|---|---|
| Software, supplies, accountancy, advertising, insurance and premises | Ordinary business-purpose operating expenses; separate capital acquisitions and private portions. A merchant name is only a categorisation clue, not proof of deductibility. |
| Home office | The room must be used exclusively for business. A bedroom or living room also used privately does not qualify. An owner can use eligible actual costs with a supported allocation; there is no deduction for invented rent paid to oneself. The standard deduction is an alternative, not an addition, if you occupy at least **50%** of the dwelling measured by rental value, or rent out a larger share but total annual rent does not exceed **NOK 20,000**. For income year **2026** the standard deduction is **NOK 2,240** (2025: NOK 2,192) for a home office in an owner-occupied (tax-exempt) dwelling, including a housing-cooperative unit, not reduced for part-year use. Rented premises use actual attributable rent/costs. [Home-office conditions](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/office-car-transport-and-equipment/home-offices/); [2026 standard amount](https://www.skatteetaten.no/en/rates/home-office-standard-deduction/?year=2026); [2025 amount and conditions](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/b-14-bolig--hjemmekontor-mv/B-14.002/B-14.004/) |
| Phone and internet | Enter the business EK costs, then add back private use, capped at **NOK 4,392** annually and at the total costs. If costs are below that cap, the addition can consume the whole cost. Claim no private addition only with support for no private use; do not assign an arbitrary percentage or import employee exceptions. [ENK electronic communications](https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/eiendeler-utstyr-eiendom/telefon-og-internett/) |
| Client meals | Qualifying modest hospitality must relate to business and occur during business hours or immediately in connection with negotiations or product demonstrations, with no spirits. It must take place at the workplace, or at a nearby restaurant if the workplace has no canteen or other reasonable catering facility. For catering at a restaurant outside the workplace, the **2026** ceiling is **NOK 592** per person. Exceeding that restaurant ceiling loses the whole meal deduction, rather than allowing a deduction up to the ceiling. If spirits are served, no part of the meal is deductible; tobacco is never deductible. Keep attendee and purpose records. Other entertainment is not deductible at all, for example trips to sporting events, hunting or fishing trips, gifts to business contacts, or running a building, boat or car for entertainment. Borderline costs can instead be advertising or staff welfare; classify them from the facts, not the label. [Hospitality conditions](https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/representasjon-velferdstiltak-reklame-og-gaver/representasjon/); [2026 ceiling, spirits and tobacco](https://www.skatteetaten.no/en/rettskilder/type/handboker/skatte-abc/gjeldende/r-13-representasjon/R-13.008/R-13.009/) |
| Training, professional subscriptions and travel | Verify the applicable deduction conditions and business connection from the supporting documents. Costs of maintaining or updating a qualification the owner already uses to earn income can be deductible; costs of obtaining a new qualification or degree (basic education, further education or specialisation) are normally not. Private gifts and commuting must not be relabelled as ordinary operating costs. Use the relevant specific category where facts require it. [Training conditions](https://www.skatteetaten.no/nn/person/skatt/hjelp-til-rett-skatt/arbeid-trygd-og-pensjon/utdanning/fradrag-for-kostnader-til-utdanning/) |

### Vehicles

Assess each vehicle separately. The business-vehicle branch normally applies at **6,000** business kilometres or more, or if business use is more than half of total use; consider the usage pattern across years. Keep a trip log identifying date, destination, business purpose and distance. [Vehicle classification](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/b-5-bil--fradrag-for-bilkostnader/B-5.007/B-5.010/)

For a car that does not qualify as a business vehicle (under **6,000** business kilometres and not mainly used in the business), the current official business guidance permits **NOK 3.50** per business kilometre, and then no other costs of keeping that car are deductible; running costs and depreciation are covered by the kilometre rate. Confirm the filing-year valuation rules before final submission. A business vehicle gets no kilometre rate. For a business vehicle, claim the relevant actual costs and tax depreciation and add back private use. [Business vehicle method](https://info.altinn.no/starte-og-drive/skatt-og-avgift/skatt/yrkesbil/)

For an ordinary car under the standard private-use method in **2026**, the annual benefit is **30%** of the adjusted list-price base up to **NOK 370,300**, plus **20%** of the excess. The base is normally the original list price including extras; use **75%** of that list price if the car is older than **three years** at **1 January**, or documented business driving exceeds **40,000 km** in the year; use **56.25%** when both conditions apply. The high-mileage reduction needs an electronic logbook showing more than **40,000** business kilometres in the year, and it is not available for class-two vans. This standard method covers owners who account for a car in their own business, not only employees. Compare that benefit with **75%** of calculated total vehicle costs and use the lower add-back. The cost cap uses the special **17%** declining depreciation calculation, not the ordinary tax depreciation deduction; leased cars use lease costs in that cap instead. For a class-two van with documented business need, reduce list price by **50%**, capped at **NOK 150,000**. If older than three years at 1 January, first reduce original list price to **75%**, then apply that van deduction. Alternatively, include **NOK 3.40** per private kilometre supported by an electronic trip log. Record which method is used. [ENK cap and van rules](https://info.altinn.no/starte-og-drive/skatt-og-avgift/skatt/yrkesbil/); [Standard benefit and reduced bases](https://www.skatteetaten.no/satser/bilsatser---firmabil/); [Owners covered by the standard rule](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/b-7-bil--privat-bruk/B-7.012/B-7.013/); [Reduced bases](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/b-7-bil--privat-bruk/B-7.020/B-7.022/)

### Capital assets and [depreciation rates](https://www.skatteetaten.no/satser/avskrivningssatser/)

For a depreciating physical business asset, direct deduction is available where cost is **below NOK 30,000** or useful life is **under three years**. At exactly the threshold with a life of at least three years, capitalise. Two elections exist: a durable asset below NOK 30,000 may instead be capitalised in its pool, and an asset costing NOK 30,000 or more with a life under three years may have its cost spread over its expected useful life instead of being expensed at once. Do not expense non-depreciating land/art merely because its cost is low. Determine cost after recoverable VAT and directly attributable acquisition costs; record delivery and in-service facts. The Norwegian detailed rule resolves the ambiguous threshold wording on the English summary. [Exact direct-deduction boundary](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/d-3-driftsmiddel--direkte-fradragsforing/D-3.001/D-3.002/); [Asset acquisition and grouping](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/office-car-transport-and-equipment/bedriftens-eiendeler-driftsmidler/kjope-eiendeler-til-bedriften/)

Use the correct declining-balance pool, not book depreciation:

| Group | Ordinary maximum annual rate |
|---|---:|
| a: office machines | 30% |
| b: acquired goodwill | 20% |
| c: specified trucks, buses and vans | 24% |
| d: passenger cars, machinery, furniture | 20% |
| e: ships and rigs | 14% |
| f: aircraft | 12% |
| g: installations for transmitting/distributing electric power and electrotechnical equipment in power companies | 5% |
| h: buildings/structures, hotels | 4% (special qualifying categories differ) |
| i: commercial buildings | 2% |
| j: technical installations in business buildings | 10% |

[Depreciation rates and exceptions](https://www.skatteetaten.no/satser/avskrivningssatser/)

Pools a–d are collective; e–i are individual assets; j is per building. Roll forward opening tax balance, additions, disposals and elected depreciation. For sold a/c/d/j assets, unrecognised proceeds reduce the balance; a negative balance triggers income at least at the pool's rate, subject to small-balance rules. Other disposal groups can feed a gain/loss account: recognise at least **20%** of positive gain balance, or deduct up to **20%** of negative balance, subject to closure/small-balance rules. Preserve residual pools after disposal; do not expense the whole purchase and then depreciate it again. [Pools](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/office-car-transport-and-equipment/bedriftens-eiendeler-driftsmidler/kjope-eiendeler-til-bedriften/); [Disposals and gain/loss account](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/inntekt-i-enkeltpersonforetak/)

## Calculate business personal income separately

Start with taxable net business income before ordinary loss carryforward. Remove included capital returns/gains that are outside the personal-income base and add back capital costs/losses that the model excludes. Then deduct qualifying business-debt interest under its specific rule, avoiding a duplicate deduction after the add-back. Retain customer-receivable interest/FX and relevant business fixed-asset gains in the personal-income calculation; a generic “subtract all capital income” rule is wrong. Adjust any gain/loss-account amounts that do not belong in personal income. Show each bridge line, amount and source ledger. Financial-institution/bond-debt interest remains deductible only to the extent the relevant debt does not exceed the shielding base before that debt deduction; add back the excess interest. Private debt interest included in business profit must be added back. [Detailed bridge and debt limitation](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.016/E-5.017/) [Personal-income bridge](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/)

Calculate the optional shield from the average opening/closing qualifying business asset base after prescribed debt deductions. Include qualifying assets used in the business whose return remains within the personal-income model; exclude private assets and financial assets whose actual return was removed. Deduct supplier credit/customer advances and relevant financial-institution/bond debt in the prescribed base. Maintain opening and closing schedules; bank deposits are not automatically qualifying capital. [Shield asset/debt principles](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.054/E-5.055/) Deduct the eligible shield from calculated personal income, not again from ordinary profit. The **2026** maximum business shielding rate is published in January **2027**; retain the rate as an unresolved parameter until publication if a positive shield base exists. A documented zero base, or a clear election of a lower rate (whole percentage points, made no later than filing the return by the deadline), enables a calculation now; without a clear election the maximum published rate applies. Do not substitute the share shielding rate. [Risk-free return calculation](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/); [Publication and election rules](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.054/E-5.091/)

Carry negative calculated personal income separately from ordinary tax losses. Apply available prior negative personal income against positive personal income from the same business under the coordination rules; unused amounts can carry forward. Electing not to use an available offset can forfeit the amount that could have been used. It does not offset wage personal income. Where spouses run a joint business and both worked in it during the income year, positive personal income can be split in the same shares as net business income, but one spouse's negative personal income cannot be deducted from the other spouse's positive personal income; floor each spouse's final business entry at zero for contribution/bracket calculations. [Negative personal income](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.096/E-5.097/); [Carryforward election and spouse allocation](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/)

## Ordinary-income tax and deductions

For the ordinary full-year case:

```text
ordinary income before personal allowance = taxable business profit
  + wages and other ordinary taxable income
  - salary minimum deduction or eligible actual salary costs
  - eligible private interest/other deductions
  - usable ordinary loss carryforward
ordinary-income tax base = max(0, ordinary income
  - applicable work deduction - personal allowance - eligible zone deduction)
ordinary-income tax = applicable ordinary rate × that base
```

There is **no salary minimum deduction on ENK business profit**. Wages alongside the business can qualify separately: **46%** of eligible wages, capped at **NOK 95,700** for the ordinary full-year **2026** case. Do not deduct both the wage standard and the same actual wage costs. The full-year personal allowance is **NOK 114,540** once for the individual. It reduces ordinary income, not bracket tax or National Insurance. Partial-year liability can reduce allowances; confirm the exact month and residence rules before applying full-year inputs. [Final 2026 rates and allowances](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/); [Part-year reduction](https://www.skatteetaten.no/en/rates/personal-allowance/) (that page's year selector can still display an earlier year's amount; use the 2026 circular for the figure)

The ordinary combined rate is **22%**. Qualifying Finnmark/North Troms tax locations use **18.5%** on the relevant ordinary income and up to **NOK 45,000** zone deduction. The zone covers Finnmark and Troms except Balsfjord, Bardu, Dyrøy, Gratangen, Harstad, Ibestad, Kvæfjord, Lavangen, Målselv, Salangen, Senja, Sørreisa, Tjeldsund and Tromsø; eligibility follows tax location at the end of **1 January** of the income year. The ordinary bracket schedule below applies in 2026; do not carry forward the former lower third bracket. If business operates in another municipality, allocate business income/deductions/wealth in the return as instructed, rather than choosing the office municipality for the owner's whole calculation. [Ordinary rates](https://www.skatteetaten.no/satser/alminnelig-inntekt/); [Tax location and zone deduction](https://www.skatteetaten.no/nn/person/skatt/hjelp-til-rett-skatt/arbeid-trygd-og-pensjon/finnmarksfradrag/); [Business in another municipality](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/inntekt-i-enkeltpersonforetak/)

An ordinary business loss first reduces other ordinary income under the applicable rules; unused ordinary loss carries forward with no time limit. It is not automatically the same amount as negative calculated personal income. Keep both schedules and reconcile them separately. [Business deficit](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/inntekt-i-enkeltpersonforetak/); [No time limit](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/u-2-underskudd/U-2.025/U-2.026/)

### Selected young-person [work deduction](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/a-13-arbeidsfradrag-for-unge/A-13.004/)

The trial starts with **2026** income. The target group is people born 1991–2006 who were registered as resident in Norway on 31 October 2025; about **8%** (roughly **100,000**) were randomly drawn for a planned five-year trial, and nobody else will be drawn later. Confirm the taxpayer was drawn; being in the cohort alone is insufficient. The deduction has no effect under the PAYE source-tax scheme (*kildeskatt på lønn*). Do not apply the public page's illustrative salary-income starting point as a universal business-income threshold. [Selection and operation](https://www.skatteetaten.no/person/skatt/arbeidsfradrag/); [Cohort](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/)

For the full-year case let W equal eligible wage/replacement income plus ENK calculated personal income after usable negative-personal-income carryforward. Exclude nonqualifying benefits and pensions. The tentative ordinary-income deduction is:

```text
max(0, 125,000 - 40% × max(0, W - 345,000))
```

It phases out at **NOK 657,500**. Then cap it by eligible income and available ordinary income after other deductions, including ordinary loss carryforward: it cannot create/enlarge a loss or transfer a new loss to a spouse. It reduces ordinary-income tax only. Partial-year rules proportionately reduce both the deduction and phase-out threshold; do not apply this full-year formula unchanged. Reconcile the automatically calculated result with the return. [Eligible base](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/a-13-arbeidsfradrag-for-unge/A-13.003/); [Amount and phase-out](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/a-13-arbeidsfradrag-for-unge/A-13.004/); [Ordering, caps and part-year rules](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/a-13-arbeidsfradrag-for-unge/A-13.005/)

## [Bracket tax](https://www.skatteetaten.no/en/Rates/bracket-tax/) and National Insurance

Let P be total taxable personal income, including wage personal income and the final coordinated nonnegative business amount. Personal allowance, ordinary interest deductions and ordinary loss carryforward do not simply reduce P. Compute each marginal band once on combined P:

| Portion of P above lower bound, up to upper bound | 2026 marginal rate |
|---|---:|
| NOK 226,100 to NOK 318,300 | 1.7% |
| NOK 318,300 to NOK 725,050 | 4.0% |
| NOK 725,050 to NOK 980,100 | 13.7% |
| NOK 980,100 to NOK 1,467,200 | 16.8% |
| Above NOK 1,467,200 | 17.8% |

For each band use `rate × max(0, min(P, upper) - lower)`; the final band has no upper limit. [2026 bracket tax](https://www.skatteetaten.no/en/Rates/bracket-tax/)

For a confirmed ordinary covered adult aged 17–69, business personal income bears **10.8%**, ordinary wages **7.6%**. Pension and income for people under 17 or over 69 use **5.1%**; primary business income from fishing/hunting, or from childminding in the owner's home (children under 12 or with special care needs), bears **7.6%** instead of **10.8%**. Confirm the category and age conditions rather than assigning every ENK owner the high rate. The lower threshold is **NOK 99,650** of total personal income. Compute category-rate amounts, sum them, then limit total National Insurance to **25%** of `max(0, P - 99,650)`. Apply the threshold once across categories; do not use a second allowance for the business. A negative business personal-income remainder does not reduce wage contribution income. [2026 categories and phase-in](https://www.skatteetaten.no/en/rates/national-insurance-contributions/); [Aggregate limit](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/p-15-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-15.027/P-15.035/); [Negative income coordination](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.096/E-5.097/)

## Worked checks

Illustrative calculations below assume full-year ordinary residence outside the zone, confirmed ordinary adult coverage, no pension/special-sector income, and no youth-trial deduction unless stated. Monetary results are mathematical working-paper amounts; reconcile filing rounding with the official calculation.

- **Ordinary business:** profit and final personal income both **NOK 600,000**, no other income/deductions and a documented zero shield. Ordinary tax is **NOK 106,801.20**. Bracket tax is **NOK 12,835.40**. NI is **NOK 64,800**. Total before advances/credits is **NOK 184,436.60**. [Ordinary rate/allowance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/); [Bands](https://www.skatteetaten.no/en/Rates/bracket-tax/); [NI](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)
- **Combined low income:** wage and final business personal income each **NOK 60,000**. The ordinary category-rate NI total is **NOK 11,040**, but the single aggregate ceiling gives **NOK 5,087.50**, which is payable NI. Wage minimum deduction is **NOK 27,600** and the personal allowance eliminates the remaining ordinary-income base; no bracket tax arises. [Salary deduction](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/); [NI phase-in](https://www.skatteetaten.no/en/rates/national-insurance-contributions/); [Combined limit](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/p-15-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-15.027/P-15.035/)
- **Asset boundary:** an eligible machine costing exactly **NOK 30,000** with a three-year life belongs in group d; elected maximum first-year depreciation is **NOK 6,000**, not an immediate full deduction. [Boundary](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/d-3-driftsmiddel--direkte-fradragsforing/D-3.001/D-3.002/); [Group d](https://www.skatteetaten.no/satser/avskrivningssatser/)
- **Selected trial participant:** business profit and personal income **NOK 400,000**, no other deductions and zero shield. The tentative work deduction is **NOK 103,000**, within the stated caps. Ordinary-income tax after it and the personal allowance is **NOK 40,141.20**; the work deduction does not change the bracket or NI bases. [Phase-out](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/a-13-arbeidsfradrag-for-unge/A-13.004/); [Caps](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/a-13-arbeidsfradrag-for-unge/A-13.005/); [Ordinary inputs](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/)
- **Phone:** business EK costs **NOK 3,000** with private use produce an equal private addition, hence zero net cost deduction. Costs above the cap would instead leave costs less **NOK 4,392**. [Private addition](https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/eiendeler-utstyr-eiendom/telefon-og-internett/)
- **Meals:** an otherwise qualifying nearby-restaurant client meal outside the workplace costing **NOK 600** per person exceeds **NOK 592**; deduction is zero even if the other conditions are satisfied. [Whole-cost exclusion](https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/representasjon-velferdstiltak-reklame-og-gaver/representasjon/); [2026 ceiling](https://www.skatteetaten.no/en/rettskilder/type/handboker/skatte-abc/gjeldende/r-13-representasjon/R-13.008/R-13.009/)

- **Older van:** a class-two van with business need, list price NOK 400,000 and age over three years at 1 January has adjusted price `400,000 × 75% − min(400,000 × 75% × 50%, 150,000) = 150,000`; standard annual benefit is NOK 45,000 before the 75% cost cap. Alternatively, 2,000 electronically recorded private kilometres give NOK 6,800 under the kilometre method. [Van calculation](https://info.altinn.no/starte-og-drive/skatt-og-avgift/skatt/yrkesbil/)

## Submit, reconcile and correct

The ENK return deadline is normally **31 May** in the following year, moved to the next working day if necessary. Accordingly, this 2026 calculation belongs to the return in 2027, not the 2025 return being filed in 2026. Submit even for a newly registered, inactive or closed ENK. Revenue of **NOK 50,000** or less can permit simplified business information; it is not a filing exemption. The current route is personal tax return plus business information, rather than automatically prescribing the old RF-1175 form. [Deadline and simplified reporting](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/sole-proprietorships/)

In the return search for “Business”, then “Income, expenses, wealth and debt from business activity”. Complete/reconcile business information, assets, tax adjustments, calculated personal income and losses. Check transferred figures against the working paper, and keep personal debt separate from business debt already reported there. Use accounting software where required by accounting/audit obligations; otherwise use a supported software or website route. Request any extension before the deadline. Save the submitted return, receipt and supporting schedules. [Submission workflow](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/sole-proprietorships/)

Update expected annual profit and other inputs in the tax deduction card as estimates change. Advance instalments normally fall on **15 March, 15 June, 15 September and 15 December**, adjusted for weekends/holidays. A changed estimate is not itself an approved cancellation of an invoice. Wage withholding and advance tax are prepayments, not deductible business expenses. Subtract actual credited withholding/advances from assessed tax to reconcile refund or balance; apply any separately established tax credits only once. Additional advance tax paid by **31 May** of the following year avoids the corresponding underpayment interest. [Advance payments](https://www.skatteetaten.no/en/person/taxes/tax-deduction-card-and-advance-tax/advance-tax/)

Check the assessment notice against all three tax components and credited payments. Pay by the notice's deadlines even if correcting or appealing; do not copy a historical example's interest rate into a 2026 forecast. Correct a submitted return by reopening the relevant year, correcting business and personal transfers together and submitting again. The ordinary self-correction route covers the last **three income years**; for an older year or an authority decision use the appropriate change/appeal process and its notice deadline. Missing filing or inaccurate information can lead to assessment and sanctions; do not predict an automatic penalty without the applicable notice and conditions. [Corrections and filing obligation](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/sole-proprietorships/); [Settlement and payment despite correction](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-assessment/underpaid-tax/)

Keep primary accounting records, vouchers and mandatory reports for **five years** after the accounting year ends. Secondary material such as material agreements/correspondence is generally retained for **three years and six months**; electronically booked entries must also stay electronically available for three years and six months, unless turnover excluding VAT is under NOK 5 million. Apply any longer industry-specific period or retention order. [Retention rules](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/r-3-regnskap--foretak-med-bokforingsplikt/R-3.002/R-3.009/)

A missed filing obligation can lead to a conditional enforcement-fine notice with a new deadline; submit by that deadline to avoid daily accrual. For the tax return the **2026** fine is half a court fee per day (court fee NOK 1,345), up to 50 court fees, a maximum of **NOK 67,250**. Inaccurate or incomplete information that could produce a tax advantage can separately attract additional tax: **20%** of the tax advantage, **40%** in serious cases and up to **60%** in especially serious cases. Exceptions include excusable circumstances, correct pre-filled information, obvious typing/calculation errors and voluntary correction. An enforcement fine paid for the same failure is deducted from the additional tax; appeal additional tax within six weeks. Record the notice, deadline, grounds, correction and any appeal route; do not treat a daily fine and additional tax as the same sanction. [Enforcement fines](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/deadlines-certificates-and-accounting/enforcement-fines/); [Additional tax](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/deadlines-certificates-and-accounting/additional-tax/)

## When to refuse or refer

- Do not present a final liability where income year, business status, actual taxable income or coverage remains unknown. Identify the missing input and calculate unaffected portions.
- Resolve treaty/foreign tax, part-year allowance, Svalbard, special industry, pension-credit or disputed membership branches before claiming this ordinary domestic method is the complete return.
- Do not invent an unpublished shielding rate or certify undocumented expenses. A positive shield-base case remains provisional until its elected/published input is established.
- Require specialist review for disputed business classification, complex spouse/business coordination, reorganisations, contentious valuations, or an authority assessment/penalty. Preserve the facts and calculations already established.

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
