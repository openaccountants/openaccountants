---
name: nl-zzp-deductions
description: "Compute 2026 Dutch self-employed business-profit deductions: hours test, zelfstandigenaftrek, startersaftrek, unpaid-partner meewerkaftrek, KIA and MKB-winstvrijstelling. Screen restricted costs, private-vehicle mileage, disinvestment, unused relief and existing FOR balances; refer specialist and cross-border applications. Trigger on zzp deductions, urencriterium, ondernemersaftrek, KIA and Dutch freelancer relief. Full personal tax and credits: nl-income-tax."
version: 2.4
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Netherlands: self-employed deductions and business reliefs (2026)

Calculate taxable enterprise profit after business adjustments, ondernemersaftrek and MKB-winstvrijstelling. This working paper does not submit a return or calculate the full personal tax bill. Figures below concern 2026; the expressly labelled historical case retains its original 2025 inputs.

## Who this applies to

The ordinary calculation covers a resident sole trader with established income-tax entrepreneur status. An entrepreneur carries on an enterprise for their own account and is directly bound by its obligations; an independently practised profession also qualifies. Registration, a VAT number or issuing freelance invoices does not settle this status. Employment, other-work income, passive profit participation and lending need their own classification; do not award entrepreneur relief from the business label alone. [Wet IB 2001 arts. 3.2, 3.4–3.5](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

Gather the inputs under **Ask the client first** before awarding relief. Partnership allocation, non-residence, foreign activity, company transitions and specialist relief are held for the explicit referrals below. The full box 1 calculation and credits route to `nl-income-tax`; personal deductions to `nl-deductions`; a bv/director to `nl-corporate-tax` and `nl-box2-substantial-interest`.

## Rates, bands and thresholds

| Item and operative conditions | 2026 amount | Source |
|---|---|---|
| Ordinary urencriterium: eligible actual business work in the calendar year; other-work comparison and exclusions below also apply | At least 1,225 hours, including for a part year | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium |
| Zelfstandigenaftrek: entrepreneur meeting the hours test, below AOW age at the start of the year; profit cap below | EUR 1,200 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml (art. 3.76) |
| Startersaftrek increase: ordinary deduction entitlement plus complete lookback and company-return tests below | EUR 2,123 | same |
| AOW age reached at the start of the year: ordinary deduction including any starter increase | 50% of the otherwise applicable amount; use return rounding | same |
| MKB-winstvrijstelling: aggregate entrepreneur profit after ondernemersaftrek, including negative results; no hours condition | 12.7% | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml (art. 3.79a) |
| Tariefsaanpassing: formula and full deduction pool below | 11.94%; top-band threshold EUR 78,426; computed maximum deduction benefit 37.56% = 49.50% − 11.94% | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml (art. 2.10) |
| KIA: total qualifying annual investment not more than EUR 2,900 | Nil | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml (art. 3.41) |
| KIA: more than EUR 2,900, not more than EUR 71,683 | 28% of investment | same |
| KIA: more than EUR 71,683, not more than EUR 132,746 | EUR 20,072 | same |
| KIA: more than EUR 132,746, not more than EUR 398,236 | EUR 20,072 minus 7.56% of excess above EUR 132,746 | same |
| KIA: more than EUR 398,236 | Nil | same |
| KIA individual-asset exclusion | Investment amount below EUR 450 is excluded; exactly EUR 450 is not excluded by this minimum alone | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml (art. 3.45(2)(b)) |
| Eligible private-owned or privately rented vehicle: business travel; further restricted-cost limitations still apply | EUR 0.25 per km under the approval retroactive to 1 January 2026; approval expires 1 January 2027 | https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html (parts 2.2 and 3) |

## The base

**1. Establish status and hours separately.** The ordinary hours test requires at least 1,225 hours on one or more enterprises in which the individual earns profit as entrepreneur. More working time must go to those enterprises than to employment and other-work activities, unless the person was not an entrepreneur in at least one of the five preceding calendar years. Do not prorate a part year. Actual quotations, administration and business website work count; idle availability does not. Make the hours plausible using calendars, quotations, timesheets and invoices. Pregnancy interruption counts over the period corresponding to employee pregnancy/maternity leave; the authority describes 16 weeks. [Art. 3.6](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml) ; [hours and evidence](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium)

For a partnership with household members, direct-line relatives or their household members, exclude mainly supportive work in an arrangement unusual between unrelated persons; the authority uses 70% or more supportive work. Also exclude work where the arrangement serves a connected person's enterprise from which the taxpayer does not themselves derive entrepreneur profit. The connected-enterprise definition includes the substantial-interest company situation in art. 3.6(4). Uncertain classification or allocation: **Check this point with one of our partner accountants.** Failing the hours test does not by itself reclassify established enterprise income; assess each relief's own conditions. [Art. 3.6(2)–(5)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml) ; [authority explanation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium)

**2. Reconcile fiscal profit.** Use annual profit determined under sound business practice and a consistent accounting policy, rather than bank deposits. Establish depreciation, cost restrictions, private use, investment deductions, disinvestment and reserve movements before ondernemersaftrek. Aggregate the individual's qualifying enterprises for ondernemersaftrek and MKB. [Arts. 3.25, 3.75 and 3.79a](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

For otherwise allowable income-tax limited expenses, the first EUR 5,700 is disallowed, or elect in the return to deduct 80%. The pool includes food/drink/stimulants, representation/receptions/entertainment, congresses/seminars/excursions/study trips and related travel/stay. The turnover-supply exception applies where the business directly produces/trades the relevant goods or provides the relevant services and the items form part of turnover. No private withdrawal for the taxpayer is separately taken for this pool. Apply outright exclusions first. In particular, the taxpayer's own course/congress/study-trip travel and stay above EUR 1,500 is excluded unless the nature of their work necessitates attendance; household equivalence also applies. For private-vehicle travel in this pool, first apply the per-km cap, then the relevant limitation. [Arts. 3.15 and 3.16(2)(f), (8), (11)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml) ; [2026 mileage approval](https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html)

For ordinary business travel using the entrepreneur's privately owned or privately rented vehicle, the approval allows EUR 0.25 per km retroactive to 1 January 2026 despite the EUR 0.23 statutory text. Fuel, insurance, tolls and parking are included: do not deduct them again. This approval expires on 1 January 2027; do not extend it into a later year without checking the replacement authority. [Approval parts 2.2 and 3](https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html) ; [included vehicle costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026)

Use the established tax cost of equipment: exclude deductible VAT; include irrecoverable VAT. VAT recovery itself needs separate assessment. [Tax cost and VAT](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving)

Workspace-at-home tests, ordinary/work clothing and exceptions, non-trade literature, home telephone subscriptions, business-car private use/value/zero-emission and older-car rules, ordinary depreciation/residual life/building floors, and starter free depreciation (eligible years, exclusions, ceilings, payment/use and recapture): **Check this point with one of our partner accountants.** Do not use the former summary as a standalone deduction or immediate-write-off permission.

**3. KIA.** Choose KIA in the return and deduct it from fiscal profit separately from established depreciation. Investment means entering qualifying acquisition/improvement obligations or incurring production costs borne by the taxpayer. If an asset is not in use at year end, the deduction cannot exceed payments; the remainder follows later payments, but no later than the year of first use. Cessation/final-settlement applications require specialist review. [Arts. 3.41, 3.43–3.44](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

The annual table applies only after eligibility is established. Land (including improvement exceptions), dwellings, ordinary/professional-transport cars, pleasure boats, financial assets/claims/goodwill/public permissions, animals, assets made available to others, forestry/foreign use, connected-party and estate acquisitions, and ministerial exceptions need the complete exclusions assessment. Partnership KIA also needs joint and outside-partnership investment allocation, rather than a simple profit-share split. EIA, MIA and Vamil need their own scheme assessment. For these applications: **Check this point with one of our partner accountants.** The worked equipment case stipulates ordinary qualifying sole-trader investment.

**4. Disinvestment.** Where aggregate annual disposal proceeds exceed EUR 2,900 and a disposal is within five years from the start of the investment year, add the original investment-deduction percentage of disposal proceeds back to profit, using a proceeds base no higher than the investment amount that received relief. Private withdrawals and changes to third-party or foreign-business use can be deemed disposals at market value. Reversal of an investment or a reduction/refund/reimbursement also counts. Failure to pay at least 25% within twelve months of commitment, unless already in use, or failure to put the asset in use within three years from the start of the investment year, counts as reversal. Ministerial exceptions or unusual transactions: **Check this point with one of our partner accountants.** [Art. 3.47](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

**5. Zelfstandigenaftrek and startersaftrek.** The ordinary EUR 1,200 requires entrepreneur status and the hours test. Add EUR 2,123 if the taxpayer was not an entrepreneur in at least one of the preceding five years and zelfstandigenaftrek applied no more than twice in those years. Exclude a business continued under Wet Vpb art. 14c where continuation began in the current or any of the preceding five years. Starter entitlement is an increase to the ordinary deduction, not an amount to save by choice. Halve the applicable ordinary amount including the increase if AOW age was reached at the start of the year. [Art. 3.76(1)–(4)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

For a non-starter the current deduction cannot exceed aggregate entrepreneur profit; for a qualifying starter this cap does not apply, so it may create a loss. Profit-cap reductions become unused zelfstandigenaftrek. A nil deduction through this cap still counts as an application for the starter lookback. The inspector establishes unused amounts and utilisation by appealable decisions, separately shown on the assessment. In the following nine years, use the oldest amount first, only up to profit above that year's zelfstandigenaftrek and with current eligibility established. Obtain the decisions; do not assume utilisation is automatic. Death/cessation exceptions: **Check this point with one of our partner accountants.** [Art. 3.76(5)–(10)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

**6. Other ondernemersaftrek.** For the uncomplicated unpaid-partner branch, the entrepreneur must meet the hours test and the fiscal partner must work without remuneration. Qualifying profit is the aggregate profit of enterprises in which that partner works unpaid, excluding expropriation compensation, cessation (including death), foreign-transfer and final-settlement profits. [Art. 3.78](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

| Unpaid partner's evidenced annual hours; all preceding conditions required | Meewerkaftrek | Source |
|---|---|---|
| Below 525 | Nil | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml (art. 3.78) |
| At least 525, below 875 | 1.25% of qualifying profit | same |
| At least 875, below 1,225 | 2% | same |
| At least 1,225, below 1,750 | 3% | same |
| At least 1,750 | 4% | same |

Partner remuneration and its deductibility/taxation (including the authority's below-EUR-5,000 interpretation versus statutory unpaid wording), S&O/RVO relief and starter declaration/company-return conditions, disability starter relief and its reduced-hours/benefit/lookback conditions, and cessation relief including rollovers and prior use: **Check this point with one of our partner accountants.** These specialist amounts are not awarded by this ordinary calculation.

**7. MKB-winstvrijstelling and capped benefit.** Ondernemersaftrek is the aggregate of zelfstandigenaftrek, S&O, meewerkaftrek, disability starter relief and cessation relief. After establishing all applicable deductions, subtract them from aggregate entrepreneur profit and apply 12.7% MKB to the remainder. There is no hours test for MKB. A negative remainder produces a negative exemption, reducing the loss rather than increasing it. The result is taxable enterprise profit for box 1, not the complete box 1 base. [Arts. 3.2, 3.74–3.75 and 3.79a](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

For tariefsaanpassing, let D be **all** deducted items in art. 2.10(3): ondernemersaftrek; MKB where aggregate profit after ondernemersaftrek is positive; TBS exemption where aggregate activity result is positive; deductible own-home costs; and personal deductions. Extra tax is 11.94% × min(D, max(box 1 taxable income + D − EUR 78,426, 0)). The computed maximum benefit rate is 49.50% − 11.94% = 37.56%. Pass the complete pool to `nl-income-tax`; using business deductions alone when other listed items exist understates the adjustment. [Art. 2.10(1)–(3)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

Ordinary assessed box 1 losses have three-year carryback and nine-year carryforward, oldest first, separately from unused zelfstandigenaftrek. Conscientious-objector, partner-death and tax-neutral-company-return cases require separate review: **Check this point with one of our partner accountants.** [Art. 3.150](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

**8. Existing FOR.** No additions since 2023. An existing reserve can remain but release rules continue. Where the reserve exceeds enterprise equity, cessation, AOW age at the start of the year, or failure of the hours test in both this year and last year calls for assessment. An annuity conversion or death/partner continuation also requires assessment. For the exact release, conversion, succession, equity measurement and timing: **Check this point with one of our partner accountants.** Continuation alone does not establish that the balance stays unchanged. [Authority: existing reserve and triggers](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve)

## Deadlines and filing

Report the calculation in the income-tax return's business-profit computation, then pass the taxable result and full adjustment ledger to `nl-income-tax`/`nl-return-assembly`. File when invited and use the actual invitation deadline; AWR art. 9 requires at least one month after invitation. Request any extension before that deadline and use the granted date. Do not extrapolate a personal 1 May 2027 deadline, a paper-only extension channel or an automatic four-month grant. [AWR art. 9](https://wetten.overheid.nl/BWBR0002320/) ; [invitation obligation](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/moet_ik_aangifte_doen) ; [extension request deadline](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/kan-ik-nog-uitstel-aanvragen-belastingaangifte)

No-invitation filing/assessment thresholds and refunds, the return-year filing/extension channel and non-resident paper/online route: **Check this point with one of our partner accountants.** Retain the unused-deduction decisions, election evidence and filed computation.

## Penalties and interest

For a living taxpayer, the authority first sends a reminder and then a formal demand; missing the demand deadline can trigger a EUR 469 default penalty, potentially EUR 6,709 for repeated failures. No penalty applies where all fault is absent. [Authority penalty guidance](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete) ; [reminder and formal demand](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig)

Assessment-payment penalties, failure-to-request-a-return penalties, incorrect-return intent/gross-negligence tests and penalty bases, and interest rates/periods/caps/conformity exceptions: **Check this point with one of our partner accountants.** Do not apply a blanket late-payment percentage or a 2026 interest rate to a later interest period.

## Cross-border points

Non-resident Dutch permanent establishments/representatives, resident foreign permanent establishments and treaty/unilateral relief, foreign-use investment exclusions/deemed disposals/free-depreciation recapture, and emigration/asset transfers/final settlement: **Check this point with one of our partner accountants.** Do not award identical relief solely because profit is connected with the Netherlands. Retain the treaty, establishment, asset-use and residence facts for `nl-cross-border`/`nl-double-tax-relief`.

## Two worked examples that recompute

Keep cents for transparent arithmetic; use the return software's required rounding. Both cases assume residence, income-tax entrepreneur status and complete ordinary eligibility, no unused deductions or specialist relief, and no other art. 2.10(3) deductions.

### Example 1: established freelancer with new equipment (2026)

The designer is below AOW age at the start of 2026, self-employed for eight years, and works 1,600 hours entirely in the enterprise. Profit after established normal depreciation is EUR 52,800. Equipment investment is EUR 10,000, each asset above EUR 450; assume qualifying sole-trader obligations, use and payment in 2026 and no exclusion. KIA is EUR 2,800, leaving EUR 50,000 before ondernemersaftrek. The non-starter deduction is EUR 1,200; MKB is 12.7% × EUR 48,800 = EUR 6,197.60. Taxable enterprise profit is EUR 42,602.40. With no other income or adjustment-pool items, reconstruction to EUR 50,000 is below EUR 78,426, so no tariefsaanpassing. [Arts. 3.41, 3.76, 3.79a and 2.10](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

```oa-check
name: Established freelancer, KIA, zelfstandigenaftrek and MKB (2026)
inputs:
  profit_after_depreciation: 52800
  investment: 10000
  kia_rate: 0.28
  zelfstandigenaftrek: 1200
  mkb_rate: 0.127
  top_band_threshold: 78426
steps:
  - kia: investment * kia_rate
  - profit_before_oa: profit_after_depreciation - kia
  - za: min(zelfstandigenaftrek, profit_before_oa)
  - profit_after_oa: profit_before_oa - za
  - mkb: profit_after_oa * mkb_rate
  - taxable_profit: profit_after_oa - mkb
  - excess_over_top_band: max(taxable_profit + za + mkb - top_band_threshold, 0)
expected:
  kia: 2800.00
  profit_before_oa: 50000.00
  profit_after_oa: 48800.00
  mkb: 6197.60
  taxable_profit: 42602.40
  excess_over_top_band: 0.00
```

### Example 2: high-earning starter hit by the tariefsaanpassing (2026)

The consultant started in 2025 after employment and works 1,500 hours entirely in the enterprise. It is her second deduction year; assume she is below AOW age at the start of 2026, has at most two uses in the five-year lookback and no art. 14c company-return exclusion. Profit before ondernemersaftrek is EUR 120,000, with no other box 1 income. EUR 1,200 + EUR 2,123 = EUR 3,323 deduction leaves EUR 116,677. Exact MKB is EUR 14,817.979; exact taxable profit EUR 101,859.021; exact total deductions EUR 18,140.979. Reconstruction is EUR 120,000 and excess EUR 41,574. The lower amount is the deductions: the rounded adjustment is EUR 2,166.03 and rounded top-rate saving EUR 8,979.78, leaving EUR 6,813.75. Keep the exact deduction base until the stated rounding steps; rounding the MKB/base earlier was the source of the former one-cent overstatement. [Arts. 3.76, 3.79a and 2.10](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)

```oa-check
name: Starter with profit EUR 120,000, capped benefit (2026)
inputs:
  profit_before_oa: 120000
  zelfstandigenaftrek: 1200
  startersaftrek: 2123
  mkb_rate: 0.127
  top_band_threshold: 78426
  adjustment_rate: 0.1194
  top_rate: 0.495
steps:
  - ondernemersaftrek: zelfstandigenaftrek + startersaftrek
  - profit_after_oa: profit_before_oa - ondernemersaftrek
  - mkb: profit_after_oa * mkb_rate
  - taxable_profit: profit_after_oa - mkb
  - deductions: ondernemersaftrek + mkb
  - excess: max(taxable_profit + deductions - top_band_threshold, 0)
  - tariefsaanpassing: round(min(deductions, excess) * adjustment_rate, 2)
  - saving_at_top_rate: round(deductions * top_rate, 2)
  - net_saving: saving_at_top_rate - tariefsaanpassing
expected:
  ondernemersaftrek: 3323.00
  profit_after_oa: 116677.00
  mkb: 14817.98
  taxable_profit: 101859.02
  deductions: 18140.98
  excess: 41574.00
  tariefsaanpassing: 2166.03
  saving_at_top_rate: 8979.78
  net_saving: 6813.75
```

### Earlier original cases retained

These preserve the scenarios from the Guide before its October rewrite; they are independent of the two blocks above.

- **Ordinary profitable entrepreneur, 2026:** eligible non-starter below pension age, EUR 50,000 profit and no other deductions: EUR 50,000 − EUR 1,200 = EUR 48,800; MKB EUR 6,197.60; taxable profit EUR 42,602.40. [Arts. 3.76 and 3.79a](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)
- **Limited-profit non-starter, 2025 then 2026:** established 2025 entitlement EUR 2,470 against EUR 1,500 profit gives EUR 1,500 current deduction, nil remainder and EUR 970 unused relief. With continuing eligibility and EUR 50,000 profit in 2026, EUR 1,200 current relief and the established EUR 970 carryforward leave EUR 47,830 before MKB. This is historical 2025 input, not a 2026 ordinary entitlement. [2025 amount](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025) ; [Art. 3.76(5)–(8)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)
- **Low-profit starter, 2026:** complete ordinary/starter eligibility below AOW age and EUR 2,000 profit: EUR 2,000 − EUR 3,323 = −EUR 1,323; MKB −EUR 168.021; taxable result −EUR 1,154.979 (−EUR 1,154.98 to cents). [Arts. 3.76 and 3.79a](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)
- **Nil deduction in the lookback:** three preceding years of deduction application include one reduced to nil by the profit cap. That remains three applications, so the at-most-two condition fails. [Art. 3.76(3), (5)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)
- **Investment/hours boundary:** an established entrepreneur failing the hours test invests exactly EUR 2,900 in otherwise eligible assets. KIA is nil and ordinary zelfstandigenaftrek is unavailable; MKB remains separately assessable on enterprise profit. [Arts. 3.41, 3.76 and 3.79a](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml)
- **Partner/reserve decisions:** the partner works 875 evidenced unpaid hours but the entrepreneur fails their own hours test: no meewerkaftrek. Separately, the continuing business has FOR exceeding equity and fails the hours test this year and last year. Preserve those facts for the FOR referral above; do not assume no release merely because trading continues. [Art. 3.78](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml) ; [Reserve trigger](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve)

## Ask the client first

Obtain income year, legal form, residence, activity/status evidence; reconciled profit and all cost/depreciation/private-use/investment/reserve adjustments; actual business and other-work hours, pregnancy and connected-person arrangements; AOW position at 1 January; entrepreneur status and deduction uses in each of 2021–2025 and any company return; unused-deduction/loss decisions; investment commitments, tax cost/VAT, sellers, payments/use/disposals; partner hours/pay; and S&O declarations, disability benefits, cessation or FOR records. Preserve unknowns. Resolve dependent facts before producing a usable deduction, while continuing independent calculations.

## Sources

| Official source and passage read | URL | Read on |
|---|---|---|
| Wet IB 2001, exact manifest-discovered 21 February 2026 edition; arts. 3.2/3.4–3.6, 3.15–3.17, 3.25, 3.41/3.43–3.47, 3.74–3.79a, 3.150, 10a.29 and 2.10 read for the retained computation and boundaries | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml | 2026-11-26 |
| Urencriterium, read for annual threshold/part-year, actual work/evidence, pregnancy and connected-person exclusions | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium | 2026-11-26 |
| Staatscourant policy, read for part 2.2 income-tax travel approval and part 3 retroactivity/expiry | https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html | 2026-11-26 |
| Tax depreciation page, read for deductible/irrecoverable VAT cost basis only; completed bookkeeping proof reused | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving | 2026-11-26 |
| Private-vehicle page, read for included fuel/insurance/toll/parking costs only; completed bookkeeping proof reused | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026 | 2026-11-26 |
| FOR page, read for no additions, continuing reserve, equity/hours/cessation/AOW and annuity/death triggers; exact release referred | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve | 2026-11-26 |
| Zelfstandigenaftrek 2025 page, read for ordinary amount/profit cap; historical case only | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025 | 2026-11-26 |
| AWR art. 9 and authority invitation obligation; completed income-tax proof reused | https://wetten.overheid.nl/BWBR0002320/ ; https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/moet_ik_aangifte_doen ; https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/kan-ik-nog-uitstel-aanvragen-belastingaangifte | 2026-11-22; applicability checked 2026-11-26 |
| Penalty guidance, reminder/demand, default amounts, repeated failure and absence of all fault; completed income-tax proof reused | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete ; https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig | 2026-11-22; applicability checked 2026-11-26 |

Not yet confirmed: specialist and rare applications are explicit non-usable referrals above, including paid-partner interpretation, S&O, disability/cessation/rollover relief, investment exclusions/allocation/special schemes, workspace/car/depreciation, FOR release/conversion, special losses, filing/extension channels and no-invitation thresholds, penalty/interest assessment, cross-border and later-year legislative effects. **Check this point with one of our partner accountants.** No proposed future-year rate or stale bill stage is usable guidance here.
