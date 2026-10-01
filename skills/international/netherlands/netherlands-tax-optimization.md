---
name: netherlands-tax-optimization
description: Use this skill whenever asked about reducing tax in the Netherlands, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals (ZZP'ers/ondernemers) in the Netherlands. Trigger on phrases like "reduce tax", "tax planning", "save tax", "optimize", "allowances", "deductions I'm missing", "belasting besparen", "belastingoptimalisatie", "minder belasting betalen", "aftrekposten", "zelfstandigenaftrek". ALWAYS read this skill before advising on any Dutch tax optimization strategy.
version: 1.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-01
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands tax planning: sole traders, households and business structure

Use this method for tax year 2026 planning and separately labelled 2025 return work. It produces a documented comparison of lawful choices, a cash forecast and actions for review. It does not turn an estimate into a filed return or make an investment, incorporation, pension contribution or insurance purchase for the client. Refresh the official sources before a later-year decision; proposed future measures are not current rules.

## Ask the client first

- Which tax year and decision date apply? Is this a resident individual, an IB entrepreneur, other-work earner, partnership member or shareholder/director? Obtain residence, cross-border work and insurance periods, age/AOW status, contracts and the actual working relationship.
- Obtain reconciled accounts, the asset register, profit before and after tax adjustments, other income, prior assessments and loss decisions, withheld taxes, provisional assessments, payment records and VAT status. Ask for cash needed personally and cash that can remain invested in the business.
- Obtain actual business hours, other-work hours and entrepreneurial/deduction history; partner work, remuneration, ownership, agreed profit shares and household partnership periods. Registration and a desired deduction do not establish eligibility.
- Obtain investment quotes and binding-order dates, asset specifications, new/used status, grants, VAT recovery, payment and first-use dates, planned disposals, and any RVO applications/decisions. Do not assume a supplier's “green” label establishes relief.
- For pension planning obtain prior-year income, pension accrual statements and factor A or the applicable pension-transition information, unused annual room and prior contributions. Obtain existing FOR, cessation plans, product terms and payment dates. For AOV obtain the policy, insured person, payer and benefit form.
- Obtain mortgage/home-office facts, gift agreements and receipts, relevant care expenses, assets and debts at the reference date, annual actual returns and partner allocation choices. Record missing inputs as holds, not zeros.

## The method, step by step

1. **Fix the baseline and the status of every assumption**

Classify income and each working relationship first. Income-tax entrepreneur status is separate from VAT status and employment status. Refer unresolved disguised-employment or international cases before counting entrepreneur relief. Use [freelance intake](/skills/nl-freelance-intake) to establish the facts. [Official entrepreneur criteria](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/).

Reconcile a no-change baseline using [income tax](/skills/nl-income-tax), [entrepreneur deductions](/skills/nl-zzp-deductions), [personal deductions](/skills/nl-deductions) and [return assembly](/skills/nl-return-assembly). Record the retrieved version and tax year of each dependency. If a dependency has not been checked against current official sources, hold its affected calculation. Each scenario must use the same accounting period and separately show accounting profit, taxable profit, taxable income in each box, credits, Zvw, assessment offsets and cash payments.

These are ordinary full-year rates before AOW-age adjustments; do not apply the ordinary table to an AOW or partial-insurance case. Annual credits depend on their statutory income bases and personal circumstances, so there is no universal tax-free business-profit threshold. [Box 1 and AOW tables](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/); [annual tax calculation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening).

| Item | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Ordinary Box 1 | 35.82% through €38,441; 37.48% above that through €76,817; 49.50% above | 35.75% through €38,883; 37.56% above that through €78,426; 49.50% above | [Annual bands](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/) |
| Ordinary self-employment deduction before age/profit limits | €2,470 | €1,200 | [2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025), [2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026) |
| Starter supplement, only when conditions met | €2,123 | €2,123 | [Starter conditions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek) |
| MKB exemption after entrepreneur deductions | 12.7% | 12.7% | [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling) |
| Maximum rate of relief for specified entrepreneur deductions/MKB | 37.48% | 37.56% | [MKB rate restriction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling) |
| Self-paid Zvw rate and annual contribution-income ceiling | 5.26%; €75,864 | 4.85%; €79,409 | [2025](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/inkomensafhankelijke_bijdrage_zorgverzekeringswet), [2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/inkomensafhankelijke_bijdrage_zorgverzekeringswet) |

2. **Establish relief before attempting to optimize it**

For the ordinary hours criterion, substantiate at least 1,225 business hours in the calendar year; do not prorate this for a late start. Apply the majority-of-working-time condition and its starter exception, the pregnancy rule and the connected-person partnership exclusions. There is no statutory half-year hours target. Apply starter lookback and prior deduction history from the evidence, including years where profit limitation reduced a deduction to nil. [Hours](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium); [starter](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek); [Wet IB, article 3.76](https://wetten.overheid.nl/BWBR0011353).

Ordinary unused self-employment deduction has its own nine-year carryforward and profit limits; use requires entitlement to the ordinary self-employment deduction in the utilization year. Apply those limits and use assessments and oldest amounts first. It is different from a Box 1 loss. When the starter exception applies, the combined current deduction can exceed profit; the MKB exemption also reduces the deductible amount of a loss. Do not add percentage “savings” from each relief independently. [Unused deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/zelfstandigenaftrek1/verrekenen_niet_gerealiseerde_zelfstandigenaftrek); [self-employment deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/zelfstandigenaftrek1/); [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling).

For partner work, compare a genuine partnership, qualifying cooperation deduction and actual remuneration using the facts. Cooperation deduction requires the entrepreneur's own hours criterion and at least 525 partner hours with no remuneration or remuneration below €5,000; the deduction percentage depends on hours. Remuneration below that boundary is not a deductible business wage. At or above it, consider the documented remuneration route and the partner's corresponding income. Do not presume an employment relationship. A VOF does not automatically qualify every partner or multiply the KIA table. [Partner remuneration](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/arbeidsbeloning_aan_fiscale_partner); [cooperation deduction, article 3.78](https://wetten.overheid.nl/BWBR0011353); [investment relief and partnerships](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/voorwaarden_investeringsregelingen).

3. **Separate business expenses, personal deductions and capital expenditure**

Keep only substantiated business costs, remove private portions and distinguish current costs from assets. Prepayment or delayed invoicing does not automatically move income-tax profit: follow the consistent, legally acceptable profit-recognition method, accruals and work in progress. VAT invoice/cash rules are a separate question. [Good business practice](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/goed_koopmansgebruik); [business costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten/overzicht-mogelijk-aftrekbare-zakelijke-kosten).

- **Private vehicle:** business journeys in a vehicle privately owned or privately rented use €0.23/km for 2025 and €0.25/km for 2026. Fuel, insurance, tolls and parking are included; do not deduct them again. This is not the company-car method. [Year-specific rule](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026).
- **Meals, representation and similar limited costs:** for an IB entrepreneur compare the annual €5,700 disallowance with the permitted 80% deduction alternative in both years, using the correct cost pool. Personal consumption remains private; special travel/stay limits and necessary-attendance exceptions may apply. Do not use this IB percentage for a BV. [Cost categories](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten/overzicht-mogelijk-aftrekbare-zakelijke-kosten).
- **Training:** document the business purpose and maintenance of existing professional knowledge; do not assume a new qualification is deductible. **Home office:** use the official tool and establish independence of the space and the applicable income tests; a desk or a separate room alone is insufficient. [Training/costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten/overzicht-mogelijk-aftrekbare-zakelijke-kosten); [workspace](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/werkruimte_in_de_woning).
- **AOV:** qualifying periodically paying disability insurance is a personal income-provision deduction, not a reduction of business profit. Lump-sum policies do not receive that deduction. Check the policy and applicable payer/insured conditions, and do not deduct premiums already accounted for in payroll. [AOV](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/arbeidsongeschiktheidsverzekering-voor-ondernemers); [income provisions](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/uitgaven_voor_inkomensvoorzieningen).
- **Mortgage, gifts and care:** run the individual conditions and partner rules in [personal deductions](/skills/nl-deductions), including rate limits, gift caps and reimbursement exclusions. A charitable or housing payment does not automatically create an equal cash tax saving. [Annual deduction framework](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening).

4. **Compare investments on commercial need and after-tax cash**

Establish the real asset, qualifying cost including irrecoverable VAT, annual aggregate and exclusions. KIA is an extra profit deduction, not a reimbursement of expenditure. An ordinary asset below €450 does not qualify; connected assets and partnership investment require the proper grouping. Qualifying BVs may also obtain KIA. Confirm obligation, payment and first-use timing before assigning the deduction to a year. [KIA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/kleinschaligheidsinvesteringsaftrek_kia); [general investment conditions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/voorwaarden_investeringsregelingen); [2026 company relief](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026).

| 2026 total qualifying investment | KIA | Source |
| --- | --- | --- |
| At most €2,900 | None | [2026 table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) |
| €2,901–€71,683 | 28% | [2026 table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) |
| €71,684–€132,746 | €20,072 | [2026 table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) |
| €132,747–€398,236 | €20,072 less 7.56% of the excess above €132,746 | [2026 table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) |
| Above €398,236 | None | [2026 table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) |

Use the separate [2025 KIA table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/investeringsaftrek-2025/kleinschaligheidsinvesteringsaftrek-2025) for 2025 obligations. Model a commercially feasible purchase now versus later with each year's complete investment total, payment constraints, deductions, loss use and liquidity. Do not split an economic asset artificially or spend merely to obtain relief. Review disposals and deemed disposals for recapture within the statutory five-year window, its annual threshold and the cap at relief previously obtained. [Disinvestment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/desinvesteringsbijtelling).

For ordinary depreciation substantiate acquisition cost, residual value and useful life; cap annual ordinary depreciation at 20% of acquisition cost, or 10% for goodwill, and prorate actual use. Do not invent a zero residual value or standard asset life. Building land is not depreciable. The building floor is the WOZ value; the limited transition for qualifying own-use buildings first used before 2024 must be checked from original use and depreciation history. Starter arbitrary depreciation requires its own eligibility and residual/building constraints. [Depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving); [buildings](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/afschrijving_bedrijfspand); [starter arbitrary depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/willekeurige_afschrijving/startende_ondernemer).

5. **Validate green relief before counting it**

Check the binding-order year's exact RVO list, code description, eligible new asset, minimum eligible amount, permitted costs, certificates, grants, state-aid limits and application deadline. EIA and MIA/Vamil normally require at least €2,500 of eligible investment per the applicable asset/application rules; read the relevant conditions rather than grouping unrelated small items to reach it. [EIA conditions](https://www.rvo.nl/subsidies-financiering/eia/ondernemers/voorwaarden); [MIA/Vamil conditions](https://www.rvo.nl/subsidies-financiering/mia-vamil/ondernemers/voorwaarden).

- EIA gives a 40% deduction on the eligible cost, subject to the code and scheme limits. [EIA](https://www.rvo.nl/subsidies-financiering/eia/ondernemers).
- MIA is code-dependent: 27%, 36% or 45%. Vamil permits arbitrary depreciation of 75%, with the remainder depreciated normally and the residual-value floor retained. A code may offer only one relief. [Code letters](https://www.rvo.nl/subsidies-financiering/mia-vamil/milieulijst); [Vamil application and depreciation](https://www.rvo.nl/subsidies-financiering/mia-vamil/ondernemers/aanvragen).
- EIA and MIA cannot both apply to the same investment costs; eligible Vamil may coexist with EIA. Check KIA separately. Grants can reduce eligible cost or prohibit combination entirely. [Combination restrictions](https://www.rvo.nl/subsidies-financiering/mia-vamil/ondernemers/voorwaarden); [company investment rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026).

For purchase costs apply within three months after the binding order/agreement, not the invoice, payment or installation. Self-construction costs normally have a quarter-end-based period; first use in that quarter changes the trigger. Save the exact deadline, submission authority, reference and decision. Check income-tax application timing independently of RVO notification. Missing the deadline is a hold/referral, not permission to backdate an order. [EIA procedure](https://www.rvo.nl/subsidies-financiering/eia/ondernemers/aanvragen); [MIA/Vamil procedure](https://www.rvo.nl/subsidies-financiering/mia-vamil/ondernemers/aanvragen).

6. **Calculate pension room and loss relief correctly**

For ordinary lijfrente planning, use the official calculator with the correct prior-year income and pension accrual, franchise/cap, transition information and historical unused room. The expanded percentage is 30% of the applicable pension base, not 30% of current profit. Unused annual room may enter the following ten years' reserve; use older room before it expires. Keep the calculator result and underlying documents. Do not reuse the former annual-room formula. [Expanded rules](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/nieuwe-regels-voor-pensioenen-wat-betekent-dat-voor-mij); [room and payment rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/lijfrente/aftrekken-lijfrentepremies/).

The 2026 annual room uses 2025 circumstances, while a 2025 calculation uses 2024 circumstances. A qualifying ordinary contribution is deducted in the payment year, within combined room across products. The 2026 reserve maximum is €42,753; it does not create room without unused entitlements. Excess paid contributions do not become a later-year deduction merely because future room appears. Record nondeducted premiums for eventual benefit taxation. Check age and product eligibility, future taxable benefits, liquidity, charges and early-release/revision-interest consequences. [2025 income provisions](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/uitgaven_voor_inkomensvoorzieningen); [2026 income provisions](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/uitgaven_voor_inkomensvoorzieningen); [ordinary contributions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/lijfrente/aftrekken-lijfrentepremies/).

On cessation, check the separate cessation deduction and prior usage before calculating the residual gain: the lifetime maximum is €3,630 and the deduction cannot exceed qualifying cessation profit. [Cessation deduction](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek).

No new FOR additions are available from 2023. Existing FOR requires its own release calculation; an excess over business equity interacts with the specified cessation/AOW/hours triggers. Do not equate every trigger with release of the entire reserve. Converting a qualifying FOR or cessation amount into lijfrente is a separate conditional route: for a 2026 deduction the qualifying payment must be made before 1 July 2027, with the profit inclusion and applicable limits accounted for. That exception is not the ordinary pension-payment deadline. [FOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve); [conversion conditions](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/uitgaven_voor_inkomensvoorzieningen).

An enterprise loss first offsets other positive Box 1 income in the same year. A remaining Box 1 loss is carried back three years, starting with the earliest, then forward nine years. It cannot offset Box 2 or Box 3. Use the official loss decisions and distinguish this from unused self-employment deduction and corporate loss rules. A written provisional carryback request can accompany the loss-year return when its conditions are met; the provisional amount is limited to 80% and the earlier assessment must be final. [Losses](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/verlies_uit_onderneming).

7. **Compare a BV and a genuine partnership on like-for-like facts**

There is no universal incorporation profit threshold. For an actual BV comparison model justified director salary, employer costs and insurance status, company taxable profit, corporation tax, retained cash, eventual distributions, personal Box 1/Box 2 tax and credits, compliance costs, conversion/cessation consequences and the client's cash needs. Deferred shareholder tax is not permanent elimination. Obtain professional structuring review before execution. Use [corporate tax](/skills/nl-corporate-tax) for the company calculation.

| Input | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Corporation tax | 19% through €200,000; 25.8% above | Same | [Company rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting) |
| Box 2 | 24.5% through €67,804; 31% above | 24.5% through €68,843; 31% above | [Box 2](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_2/) |
| Usual-salary statutory reference | €56,000 | €58,000 | [Salary rule](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/) |

The salary reference is not a safe-harbour chosen salary: the main rule takes the highest of the comparable-job salary, the relevant highest employee salary and the annual reference, with evidenced exceptions. Personal entrepreneur deductions do not transfer to BV salary, while qualifying corporate investment relief can remain available. A spouse/partner salary, profit share or asset transaction must reflect the actual work and legal arrangement. [Salary](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/); [company investment relief](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026).

For fiscal partners compare only legally allocable common items and keep the combined total unchanged. Business profit and wages cannot simply be moved to the lower-rate partner. Recalculate both returns, income-dependent credits and relevant benefits instead of selecting the highest marginal rate in isolation. [Partner allocation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/fiscaal_partnerschap).

8. **Keep VAT, social insurance and wealth planning distinct**

Use the current [Netherlands VAT return method](/skills/nl-vat-return) for invoice/cash timing, input deduction, private use, mixed activities, corrections and capital-goods revision. For second-hand goods, establish margin-scheme eligibility and the required purchase/sales records separately; refer to the current VAT method and official scheme conditions before using a margin calculation. [Margin-scheme conditions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/bijzondere_regelingen/margeregeling/). KOR eligibility and economic advantage are separate: compare customer pricing and lost input deduction, not only output VAT saved. It is not a universal three-year lock-in. Confirm official registration/withdrawal dates and cross-border obligations before changing invoices. [KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden); [KOR consequences](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling).

Compute Zvw on its own contribution-income base and remaining annual cap after other covered income. A private pension/AOV deduction from Box 1 is not automatically a Zvw reduction. The income-tax bill, Zvw assessment and health-insurer premium are different amounts. For partial-year or foreign coverage refer the insurance determination. AOW age does not mean all national-insurance premiums vanish. [2026 Zvw](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/inkomensafhankelijke_bijdrage_zorgverzekeringswet); [AOW rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/).

Do not describe a savings circle as WW insurance or assume all former employee rights disappear. UWV voluntary sickness/disability cover has application and prior-insurance conditions; the ordinary transition application period is thirteen weeks, with distinct part-time-employment rules. Voluntary WW is limited to specified situations, not generally available to every sole trader. Refer policy selection and coverage gaps to a qualified adviser. [UWV for self-employed people](https://www.uwv.nl/nl/verzekeren/vrijwillige-verzekering/zzp-verzekering); [insurance types](https://www.uwv.nl/nl/verzekeren/vrijwillige-verzekering/verzekering-zw-wia-wao-ww).

For Box 3 distinguish the reference-date deemed method from the annual actual-return comparison. The ordinary exemption is €57,684 per person for 2025 and €59,357 for 2026; eligible whole-year partners have double those amounts. The Box 3 tax rate is 36%. Actual-return relief has no ordinary tax-free allowance and is not a selective deduction of only losing assets. Check the year-specific method and retain the complete asset/debt and return evidence. Moving assets to a qualifying home or pension product also changes liquidity, costs and legal conditions. Do not promise savings from a future system that has not taken effect. [2025 calculation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/bezittingen_en_schulden_box_3_); [2026 calculation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/bezittingen_en_schulden_box_3_); [actual-return framework](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening).

Temporary tax-motivated changes around the reference date can be disregarded. For the 2025 return, the official guidance identifies investment-to-cash transactions crossing the reference date and reversed within three months, and analogous temporary debt; evidence of a non-tax reason matters. Apply the current statutory rule for a later reference date and refer uncertain arrangements. Do not recommend year-end round trips as a saving. [Reference-date arbitrage](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/regels_voor_het_tijdelijk_verplaatsen_van_bezittingen_en_schulden); [Wet IB, article 5.24](https://wetten.overheid.nl/BWBR0011353).

9. **Deliver decisions, dates and a cash forecast**

For each option show: baseline facts, changed facts, qualification evidence, source/year, income-tax effect, Zvw effect, VAT effect, cash outlay, timing of recovery, future tax/recapture, non-tax cost and unresolved holds. A deduction is not a cash refund. Recalculate credits and exemptions after every change; do not use “deduction × top rate” as the whole-client answer.

Use an event-based calendar: monitor actual hours and profit during the year; diary RVO dates from binding commitments; review pension room and payment before year end; retain reference-date wealth evidence; prepare accounts and assessments for the correct return year. Take filing/payment dates from the actual invitation, granted extension, return period and current official calendar. A requested extension is not proof of a granted date. Keep income-tax and VAT deadlines separate and never repeat the old March date for a normal prior-year final-quarter VAT return.

## Worked boundary cases

### Case 1 — KIA is not a cash saving

Assume a qualifying 2026 investment of €15,000 is the complete annual KIA total, fully paid and in use, with all other eligibility satisfied. KIA is €4,200. This is the additional profit deduction before the MKB interaction and tax/credit calculation, not the refund. Hold the cash-tax answer until the client's complete scenario is calculated. [KIA table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026).

### Case 2 — A missed investment deadline

A business accepted a binding equipment order months ago, but the supplier invoiced today. Use the order date for RVO purchase-cost notification. If its application period has expired, exclude unapproved relief from the committed cash forecast and refer; changing the invoice date cannot cure the missed deadline. [EIA application](https://www.rvo.nl/subsidies-financiering/eia/ondernemers/aanvragen).

### Case 3 — Pension payment across years

The client pays an ordinary lijfrente contribution in the following year and wants it deducted from the preceding return because that return is still open. Reject that timing assumption. Calculate eligibility in the payment year. Separately examine the statutory FOR/cessation conversion exception only if those facts actually exist. [Payment rule](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/lijfrente/aftrekken-lijfrentepremies/).

### Case 4 — Business loss with wages

Assume a final taxable enterprise loss of €15,000 after applicable profit adjustments and wage income of €10,000, with no other Box 1 items. The remaining Box 1 loss is €5,000. Apply the three-year carryback and then nine-year carryforward sequence using available assessments, not the BV loss regime. [Official loss example](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/verlies_uit_onderneming).

### Case 5 — The Zvw cap is already partly used

Assume 2026 covered wages of €40,000 and qualifying freelance contribution income of €50,000 with no other adjustments. The remaining cap is €39,409. The self-paid contribution is 4.85% of that amount, €1,911.34 before the assessment's rounding. Do not charge the percentage on the whole freelance amount. [Official cap example](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/inkomensafhankelijke_bijdrage_zorgverzekeringswet).

### Case 6 — An attractive BV percentage is incomplete

The client supplies only business profit and asks whether to incorporate. Hold the recommendation until comparable salary, retained/distributed cash, insurance, costs and personal circumstances are supplied. Do not insert an arbitrary salary or compare corporate tax alone with total sole-trader tax. [Salary rule](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/); [company rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting); [Box 2](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_2/).

### Case 7 — Mileage without duplicate costs

Assume 1,000 substantiated business kilometres in a privately owned vehicle in 2026. The profit deduction is €250; separately submitted fuel and parking for those journeys add no further profit deduction. The same distance in 2025 would use €0.23/km, not the 2026 rate. [Private vehicle](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026).

### Case 8 — AOV has the wrong ledger location

A qualifying policy pays periodic disability benefits. Remove its premium from business costs and consider the personal income-provision deduction on the documented conditions. If it instead pays a lump sum, do not grant that premium deduction. Recalculate the business-profit-based items after the reclassification. [AOV classification](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/arbeidsongeschiktheidsverzekering-voor-ondernemers).

## When to refuse or refer

- Refuse fabricated hours, backdated commitments, concealed income, invented expenses or a filing based on unverified eligibility. Preserve the true records and explain the missing evidence.
- Hold employment, residence, foreign insurance, AOW/partial-year, partnership allocation, company conversion and disputed legal-character questions for appropriate review.
- Refer specialist asset/list eligibility, state-aid combinations, uncertain RVO deadlines, pensions with transition or old-product rights, cessation and FOR calculations when the necessary determination is unavailable.
- Hold a numerical “saving” if the baseline, dependency, credit base, future tax effect or cash consequence is incomplete. Label estimates and conditional alternatives explicitly.
- Require the client’s reviewed facts and explicit filing/payment authority before an adviser or authorized system submits anything. A planning comparison supplies neither authority nor professional attestation.

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
