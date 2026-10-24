---
name: iceland-payroll
description: Use this skill whenever asked about Iceland payroll processing for employed persons. Trigger on phrases like "Iceland payroll", "Icelandic payroll", "staðgreiðsla", "PAYE Iceland", "withholding Iceland", "tryggingagjald", "social security contribution Iceland", "persónuafsláttur", "personal tax credit Iceland", "lífeyrissjóður", "mandatory pension Iceland", "séreignarsparnaður", "supplementary pension", "launagreiðendaskrá", "employer registry Iceland", "RSK 5.02", "launamiði", "skilagreining", "net salary Iceland", "tax withholding Iceland", "employer social cost Iceland", "kjarasamningur", "minimum wage Iceland", "municipal income tax Iceland", "gross to net Iceland", "salary calculation Iceland", or any question about computing employee pay, withholding income tax (state + municipal), or social contributions for Iceland-based employees. This skill covers PAYE (staðgreiðsla) income tax withholding, the personal tax credit, employer social security contribution (tryggingagjald), mandatory occupational pension (employee 4% + employer 11.5%), supplementary private pension, no statutory minimum wage (collective-agreement minimums), 2026 benefit valuation for vehicles, meals, housing, commuting, fitness and employee loans, and filing obligations to Skatturinn. ALWAYS read this skill before processing any Iceland payroll.
version: 0.7
jurisdiction: IS
tax_year: 2026
last_updated: 2026-10-23
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland payroll: employer method for 2026

Figures are for tax year 2026. [Dated official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/)

## Who this applies to

Use this method for ordinary Icelandic employed-person payroll in 2026. Establish employer and employee identity, residence and work location, pay date and period, contract and collective agreement, cash wages, benefits, pension arrangements, other deductions, and the employee's tax-credit and bracket instruction. Keep source documents and pay-run approval. Unknown tax residence, posted-worker coverage, contractor status, director fees, equity, benefit valuation or sector-specific charges require the applicable separate rule before calculation. Pay rates, including minimum pay, come from the applicable collective agreement and employment contract; this skill does not set them.

The employer must be on the withholding register (launagreiðendaskrá) and have the required electronic identity or withholding web key. Notify the register at least 8 days before the activity starts; an employer that stops paying wages during the year must notify Skatturinn within eight days. [Employer register](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/) [Act 45/1987, art. 19](https://www.althingi.is/lagas/nuna/1987045.html) The electronic service supports returns, detailed wage information, bank payment claims, corrections and statements. [Skatturinn electronic filing](https://www.skatturinn.is/atvinnurekstur/rafraen-skil/stadgreidsla/)

## Rates, bands and thresholds

For monthly taxable income in 2026, apply each rate only to its band:

| Monthly taxable income, ISK | Rate |
| --- | ---: |
| Up to 498,122 | 31.49% |
| Above 498,122 through 1,398,450 | 37.99% |
| Above 1,398,450 | 46.29% |
| Evidence | [Official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) |

Each withholding rate is state income tax plus the national average municipal tax of 14.94% (state share 16.55%, 23.05% and 31.35% in the three bands). Withholding uses the same municipal rate everywhere, but each municipality sets its own final rate, so the annual assessment collects or refunds the difference. Do not adjust withholding for the employee's municipality. [Rate make-up](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

For weekly pay, the January 2026 employer notice gives weekly bands: 31.49% on the first 114,636, 37.99% from 114,637 to 321,835 and 46.29% above 321,835. Where weekly wages vary, they may be evened out between weeks within the month so that the month's withholding is right. [Employer notice 1/2026](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

The monthly personal tax credit is ISK 72,492 (ISK 869,898 for the year). The ordinary resident credit applies from the year a person turns 16. Eligible temporary employees taxed under Income Tax Act Article 3(1) also receive credit for their qualifying days in Iceland, starting on arrival rather than the first working day. Turning 16 satisfies the age condition for the whole year; it does not remove residence or stay-based limits. Establish the applicable income category, status and days under the [cross-border Guide](is-cross-border.md) before using a full annual credit. [Posted-worker credit](https://www.skatturinn.is/english/individuals/posted-workers/) [Limited-liability employment credit](https://www.skatturinn.is/english/individuals/limited-tax-liability/) These are withholding figures, not a promise of the employee's final annual tax. [Official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) [Personal tax credit](https://www.skatturinn.is/english/individuals/personal-tax-credit/)

For pay periods shorter than a month, the credit per period is: half a month 36,246; for 14 days and one week, the dated 2026 page shows 33,365 and 16,682 while the January 2026 notice shows 33,366 and 16,683 (the same formula rounded differently). For any other period use 869,898 × days in the period ÷ 365. [Period credits](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) No pay period may be longer than one month. [Employer register](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/)

Obtain instructions on the bracket, whether credit is used, starting month and supported accumulated credit. Multiple employers must use the employee's allocation; they cannot see each other's credit use. Unused credit can accumulate within the year, but cannot cross into another year. People moving to/from Iceland or temporarily working there need the day-limited entitlement checked; a displayed cumulative balance can overstate their entitlement. Obtain the employee's statement when changing employers. Never turn a credit into extra cash after withholding reaches zero. [Personal tax credit](https://www.skatturinn.is/english/individuals/personal-tax-credit/)

**Spouse's credit.** In 2026 an employee may use up to 100% of a spouse's unused credit, but only for spouses living together, or cohabitants who meet the conditions for joint taxation and file a joint return. The employer may apply it only against the Skatturinn statement of the spouse's used credit on which the spouse's name appears. [Spouse credit, 2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Conditions](https://www.skatturinn.is/einstaklingar/stadgreidsla/personuafslattur/)

If credit is over-used or pay is taxed in too low a band, too little is withheld and the shortfall becomes the employee's debt at assessment. Skatturinn states that over-used credit not corrected during the year is collected with a 2.5% surcharge. When notified, stop or reduce the credit use until it evens out, or move pay into the correct band. [Over-used credit](https://www.skatturinn.is/einstaklingar/stadgreidsla/ofnyttur-personuafslattur/)

The default calculation uses each month's wages separately, including bonuses and overtime. Averaging across months is allowed only where monthly wages normally vary by at least 50%; the employer may then withhold proportionally on total wages from the start of the income year (or of employment) to the end of the current pay period. Do not give every employer the lowest band. For minor payments from someone other than the main employer (for example union payments or board fees), the payer may withhold at the middle band rate, but only if the payment is no more than 650,000 per month. [Withholding method](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

### Children's wages

Children born in 2011 or later (who do not reach 16 in 2026) pay 6% (4% state, 2% municipal) with no personal credit, only on income above the child allowance of 300,000 for the year. On the return, enter their total wages without deductions. Children aged 15 and younger do not pay into a pension fund. The English key-rates page still says "born 2010 or later"; the dated Icelandic 2026 pages say 2011, which matches the full-year credit for those turning 16 in 2026. [Child rate 2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

## The base

1. Establish wage components, pension arrangements and the employee instruction.
2. Separate withholding-exempt payments from taxable pay, then calculate taxable income, withholding and cash net separately.
3. Add employer pension and payroll tax, then file, pay and reconcile.

### Taxable pay

Withholding applies to all pay for work plus vehicle allowances, benefits, relocation and travel money, per diems and other work-related payments, except payments that Regulation 591/1987 lists as outside withholding. Two common exemptions have conditions:

- **Vehicle allowance** is outside withholding only if it reimburses specific driving done for the employer, the payment is within the current Travel Costs Committee maximum used by the withholding rule, and the employee keeps a regular log of each trip (date, distance, purpose, rate paid, employee name and ID, vehicle registration). Driving between home and the usual workplace always counts as the employee's own. Apply Regulation 591/1987 Article 3 and the current dated maximum; the annual income-return kilometre deduction scale is a different calculation. If the conditions for excluding an amount fail, include the affected amount in withholding.
- **Per diems and travel money** are outside withholding only for travel for the employer, within the amounts Skatturinn's valuation allows, with records of the trip purpose, days, amounts and employee. Any excess above those limits is taxable pay.

Uniforms the employee is expected to wear at work are not withholding pay. Even when a vehicle allowance is outside withholding, it still enters the payroll-tax base (see below). [Withholding base and exemptions](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Payroll-tax base](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/)

### Benefit valuation and separate payroll bases

Use **income-year 2026** rules, not a return labelled 2026 for 2025 wages. Record the recipient, relationship to the employer, benefit/cash form, actual availability/use dates, employer cost, applicable tax value and employee payment. General private benefits use market/current value unless a specific valuation applies; where the employee pays less than that value, the difference is taxable. Cash gifts and cards exchangeable for money are taxable even when a staff-event/treat exclusion would otherwise exist. [2026 valuation rules, sections 1–2.1][benefit-notice]

Keep **three bases**: PAYE includes the taxable benefit; the statutory minimum pension base excludes benefits in kind and the specified expense reimbursements; the employer levy includes taxable benefits at tax valuation plus the relevant employer pension. Confirm any contractual pension treatment separately. A noncash benefit does not increase bank wages, and its tax value is not necessarily the employer's actual cost. Do not deduct a benefit valuation from cash pay a second time after including it in taxable income. [Withholding Act, Article 5](https://www.althingi.is/lagas/nuna/1987045.html); [Pension Act, Article 3](https://www.althingi.is/lagas/nuna/1997129.html); [Levy Act, Articles 6–8](https://www.althingi.is/lagas/nuna/1990113.html)

#### Cars: decide availability before valuing it

Full private availability is valued **regardless of actual kilometres**. Multiple cars made available to the employee/family are valued separately. Owners, managers, comparable executives and directors with private use are treated as having full/unlimited availability; a low-mileage log alone does not give them the limited-use method. Leased or borrowed cars are also within the rules. Keep the asset/lease record, original VAT-inclusive price or required dealer/lessor reference, acquisition/availability year, power type, use agreement, restrictions, running-cost invoices and employee payments. [Section 2.3][benefit-notice]; [Authority car guidance][benefit-guidance]

| Full-use car category | Annual valuation method for 2026 | Source |
|---|---|---|
| Employer-owned car acquired in 2014 or later | 28% of the supported value for fossil-fuel cars; 20% for the stated electricity/hydrogen/methane clean-energy cars. A hybrid label alone does not establish that latter class. | [Section 2.3][benefit-notice] |
| Permitted value reduction for that category | 10% of the previous year's value each year, starting **after** the employer's acquisition year; never below 50% of original acquisition price. This is reducing balance, not ten percentage points of original price each year. | [Section 2.3][benefit-notice]; [Authority explanation][benefit-guidance] |
| Employer-owned car acquired in 2013 or earlier | Current annual rule: 30% of original acquisition price. The operational page instead refers to the first-use-year vehicle register; retain this source conflict and resolve a specific old-car base before filing. Do not automatically extend the later-acquisition reduction method. | [Section 2.3][benefit-notice]; [conflicting operational base][benefit-guidance] |
| Car not owned by the employer | The stated dealer-list price when employer availability begins or lessor reference value when yearly/monthly rent is set; 28%/20% power-type rule. Apply the supported 10% annual reduction/floor from its own start year. Lease instalments are not automatically the valuation base. | [Section 2.3][benefit-notice] |
| Employee pays the defined running costs | Reduce the fossil percentage by **six points**, or the stated clean-energy percentage by **three points**, of the supported car value. These are not 6%/3% discounts on the already calculated benefit. | [Section 2.3][benefit-notice] |
| Pure electric, employee pays charging alone while employer pays other running costs | The stated **19%** annual rate; do not claim 17% solely because the employee charges at home. | [Section 2.3][benefit-notice] |

Defined running costs concern fuel/electricity, lubrication, cleaning and comparable running items; repairs, parts, tyres, insurance, vehicle taxes and kilometre taxes do **not** qualify for the running-cost reduction merely because the employee pays them. Supported payments to the employer for use reduce the benefit value; distinguish them from the separate running-cost adjustment and reconcile actual settlement without deducting the same payment twice. [Section 2.3][benefit-notice]

Partial-year full use takes **one twelfth of the annual benefit per commenced monthly period of availability**. Do not apply the housing day fraction to a car. The authority's example counts **five months** for 15 January–10 June; counting six named calendar months instead does not reproduce it. Retain the actual period determination where a boundary is disputed. For employee/employer co-ownership, value the employer's share. [Section 2.3][benefit-notice]

The **limited-use** car method is **ISK 144 per private kilometre**, only where permission outside working hours is confined to commuting/occasional use and the vehicle otherwise serves the employer's daily business, with clear records. More extensive use invokes full availability. The separate collective-agreement transport exception requires the stated absence of public transport and staff collection/delivery arrangements; ordinary commuting alone is not that exception. A car with the specified security/location systems and a regular dedicated driver also has its own exclusion. Document the actual exception before excluding value. [Section 2.3][benefit-notice]

Other motor vehicles/trailers under **section 2.4**, including the stated motorcycles, snowmobiles and caravans, have their own full/unlimited **28%** method, value reduction/floor and defined six-point running-cost adjustment. Do not give every electric item the clean-car 20% rate. Private aircraft use under **section 2.5** is valued at **317,000 per commenced flight hour**, or **32,000** for the stated small single-engine aircraft; the time definition includes the relevant parking-to-parking, waiting and empty-return time. These require category and journey evidence, not a private-mileage car substitution. [Sections 2.4–2.5][benefit-notice]

#### Food, housing and supported exclusions

| Benefit | 2026 valuation / exclusion | Evidence and source |
|---|---|---|
| Food supplied free to employee/family | Breakfast 501; lunch or dinner 751; full food day 2,003. A quarter reduction is permitted for children **under 12**. Offset supported employee payment against the relevant value, without creating a negative benefit. | Meal type, count, recipient age and employee payments; [sections 1 and 2.7][benefit-notice]. |
| Ordinary employee housing | Annual 5% of the supported property/land assessment, including the stated separately assessed structures, multiplied by the **actual location factor**: 1.0 for Reykjavík, Seltjarnarnes, Mosfellsbær, Kópavogur, Garðabær and Hafnarfjörður; 0.8 for Suðurnesjabær, Reykjanesbær, Vogar, Akranes, Akureyri, Árborg, Hveragerði and Ölfus; 0.7 elsewhere. Part-year use is by days. Free heat/electricity is added at cost. | Property assessment, exact municipality, occupancy/days, employee rent and energy costs; [section 2.8][benefit-notice]. |
| Required residence / temporary work camp | Required-residence relief for incomplete use needs the authority's assessment decision. The rule treats up to 150 m² plus 5 m² per resident above six as fully used. The separately stated temporary service stay in work/fishing camps is excluded. | Actual work obligation, occupants/use and decision; do not automatically reduce payroll housing value by spare floor area. [Section 2.8][benefit-notice]. |
| Occasional ordinary employee holiday accommodation | 5,000 per day **above ten days per year**; up to ten days excluded under that branch. Supported employer/union holiday-cost reimbursement is a separate exclusion up to 79,000 annually with valid invoices. | Cumulative employee/family days and actual invoices; distinguish the two branches. [Section 2.8][benefit-notice]. |
| Fitness reimbursement | Up to 85,000 annually for supported qualifying regular exercise, with valid invoices. Equipment/clothing, general online-content subscriptions and ordinary spa/leisure visits do not qualify merely through a wellness label. | Activity, invoice and cumulative reimbursements; [section 2.9][benefit-notice]. |
| Qualifying staff events/treats | The stated events/treats generally available to all employees, including relevant staff-association funding, have a 192,000 annual per-employee employer-cost limit; excess is taxable. This does not exempt cash gifts or cash-redeemable cards. | Offer to staff, actual type/cost and annual allocation; [sections 1–2.1][benefit-notice]. |
| Workplace facilities / work clothing | The stated workplace coffee, on-site fitness, preventive health care and directly job-related courses are excluded. Clothing is at cost unless the uniform/marked-work-clothing/necessary-protection conditions apply. | Actual supply/use and work connection; an ordinary private wardrobe does not become exempt by reimbursement. [Sections 2.1–2.2][benefit-notice]. |

**Owner/manager/director property is a separate branch.** Private availability beyond ten days invokes the section 2.8 full/unlimited rule **from day one**. Do not substitute the ordinary occasional-holiday ten-day exclusion. For Icelandic property, establish the book acquisition cost plus capital improvements and the stated higher-assessment comparison, with the permitted 3% annual reduction subject to its assessment floor. For foreign property, the separate 5%-of-book-cost-plus-improvements rule applies. Supported rent and unrelated letting periods affect the calculation, and one property is not simultaneously attributed to several people under this rule. Resolve the actual value, period and permitted reduction before calculating; the ordinary employee example below does not settle those cases. [Section 2.8][benefit-notice]

**Commuting payment is conditional.** Section 2.6 permits up to **11,500 per month / 138,000 for full-year work** where the signed employer/employee agreement and qualifying public/green transport at least **80% of trips** are proved. At least **40% but below 80%** permits half the monthly limit, **5,750**. Below 40% or failure of the required conditions leaves the commuting payment taxable. Keep trip records and period/payment totals. Cars of any propulsion do not qualify as the green mode for this rule; a pure-electric company car does not itself establish exempt commuting cash. Taxable excess belongs in the payroll computation. [Section 2.6][benefit-notice]

**Employee loans and deferred purchase payments.** Section 2.10 requires a monthly comparison using the **opening loan balance** and the applicable Central Bank general indexed or unindexed rate for that month, against actual interest. Include the supported positive benefit in monthly withholding. Keep the loan/instalment contract, indexed status, opening principal, dated benchmark, monthly interest calculation, actual charge and benefit. Deferred share/property purchase payments are also within the stated rule; a nil cash advance is not proof of no financing benefit. Select the **general loan benchmark**, not the policy, IKON or late-interest headline. No permanent benchmark rate or unsupported day-count method is supplied here. Loan forgiveness, equity-plan entitlement and disputed financing terms need their own statutory determination. [Section 2.10][benefit-notice]; [Central Bank rate portal][loan-benchmarks]

#### Reporting and benefit reconciliation

Roll forward each benefit schedule by employee and period; reconcile employee charges, annual exclusions, PAYE value, pension base, levy base and bank pay. Do not assume a category is outside monthly reporting merely because it is noncash. The published wage-statement **2026 layout concerns 2025 wages** and separately identifies car, clothing, housing and food benefits; it is evidence of the category layout, not an accepted 2027 return for 2026 wages. Match the actual wage year's live fields before submission, preserve acceptance, and correct the original affected periods under the existing procedure. An insufficient-cash or benefit-only pay run requires a documented withholding/settlement decision before release; do not turn a negative calculated bank balance into a fictitious payment or simply omit the benefit. [Withholding Act, Articles 5 and 20](https://www.althingi.is/lagas/nuna/1987045.html); [Annual reporting guidance](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/); [Published 2026 statement][benefit-wage-form]

### Share options: classification, valuation and separate tax dates

Obtain the instrument and amendments, employment/director/service relationship, company/group details, grant and exercise dates, strike/payment, market-value evidence, share register and every subsequent ownership change. Separate actual share options from cash bonuses, phantom shares, restricted-share awards and direct discounted purchases; the option provisions alone do not establish those other instruments' treatment. Cross-border work, residence and treaty allocation need the [cross-border method](is-cross-border.md) before applying these domestic examples.

**Ordinary Article 9 option.** Record employment income as **market value at exercise less the contract purchase price**. Use the quoted exchange/organised-market price, otherwise actual unlisted dealings, otherwise book equity from the last audited annual or interim accounts. Income taxation is deferred until **ownership changes**, not remeasured using the later sale price. The Article 9 director extension expressly concerns qualifying innovation companies; do not assume every director or contractor fits the ordinary employee example. [Income Tax Act, Article 9][option-act]

Keep the two taxes and reporting events separate. Skatturinn expressly says the employer pays the **levy at exercise**, does **not deduct PAYE from the option wage then**, and reports the exercise particulars and option income in the following year's information submission. If the shares remain held, the individual reports the asset and carries the deferred tax position forward until ownership changes. Article 18 then gives ordinary Article 9 shares an **exercise-market-value capital basis**, subject to its same-class average-cost rule. A later capital loss is not automatically a reduction of the fixed option wage. Non-sale transfers, losses, mobility and the actual later collection/reporting procedure need their specific determination. [Employee guidance, option section][benefit-guidance]; [levy timing](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald/); [Articles 9, 18 and 24][option-act]

**Article 10 employee plan.** Apply capital treatment only after documenting every condition: offered to all staff with equal share rights; permanent employment in the company/group; at least 12 months before exercise; grant price at least the preceding ten whole trading days' weighted quotation, otherwise the Article 9 market measure; at least two years' share ownership after exercise; nontransferable option, with the contract expressly prohibiting **pledging or other transfer** under the authority's instructions; annual contract **purchase-price** total no more than **1,500,000**; and advance authority plan confirmation. The cap is not a gain allowance. Contractors and directors are not employees for this route. The authority says premature disposal loses this capital treatment. At sale, qualifying income is **sale proceeds less original contract purchase price**. Do not apply the ordinary Article 9 basis uplift to that capital amount. Maintain the year-end employee/exercise/purchase-price report. [Article 10][option-act]; [authority plan conditions][benefit-guidance]; [published plan/report instructions][option-form]

**Article 10a startup alternative.** Establish the Article 18 startup definition separately: qualifying innovation company under Act 152/2009 Article 3(3), formed for recognised R&D and spending **more than 10% of turnover** on it, within Article 30B's specifically referenced size test: **no more than 25 employees**, turnover **under 650 million and/or balance sheet under 650 million**, using the consolidated group where applicable. This is not the R&D-credit SME test. Obtain Rannís project confirmation **before the option contract** and prove the recipient's work exclusively concerns that project. Require at least **18 months** to exercise, grant-market-value strike (last approved annual book equity if no market value), nontransferability and term no longer than **eight years**. The individual service-provider extension caps total services at **2 million per twelve months**, with clear contractual pricing. Preserve the statutory restriction on obligatory cash settlement/company or related-party buyback, including its narrow normal/customary-transaction exception; a buyback promise is not automatically eligible. Report issued contracts and exercises annually. Qualifying capital income at sale is sale less contract purchase price. Article 10a is currently scheduled to lapse on **1 January 2034**; recheck future transactions. [Articles 10a, 18 and 30B][option-act]; [Innovation Act, Articles 3 and 5](https://www.althingi.is/lagas/nuna/2009152.html)

For Articles 10 and 10a, the stated gain is expressly **not Article 31 operating expenditure**, and the share purchase gives no Article 30B share-subscription deduction. Preserve the employer's book-to-tax bridge rather than assuming an accounting share-payment charge is tax deductible. Proved capital-plan classification is a separate branch from the ordinary wage-option levy/PAYE sequence above; obtain the applicable contribution/reporting treatment rather than applying an undifferentiated option flag. [Articles 10 and 10a][option-act]

**Form conflict.** Published RSK 2.085, dated 5 November 2024, identifies the Article 9/10/10a route and acquisition details, but its reverse describes Article 9 income as original price to later sale. That conflicts with current Article 9's exercise spread and Article 18's exercise-value basis. Use the Act for the computation and retain this discrepancy for the actual reporting decision. This published layout does not establish accepted 2027 fields or a completed filing. [Current Act][option-act]; [RSK 2.085][option-form]

### Pension and gross-to-net calculation

By law the minimum pension contribution is at least 15.5% of the contribution base, and workers are covered from age 16 to 70. The split between employee and employer follows the collective agreement for the trade (or special law), and fund membership must be stated in the written employment contract. A transitional rule lets 12% be used instead of 15.5% where the current collective agreement still uses 12%, until a new agreement takes effect. [Act 129/1997, art. 1-2](https://www.althingi.is/lagas/nuna/1997129.html)

The current employer instructions use 4% employee pension and an adjustable 11.5% employer default (together 15.5%). They exclude ages 15 and younger and 70 or older. Confirm actual contributions, fund, collective agreement, base, remittance schedule and supplementary arrangements. [Employer instructions](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) The contribution base is all taxable pay for work, but not benefits in kind (such as clothing, food and housing) or reimbursements of expenses (such as vehicle allowances, per diems and meal money). [Act 129/1997, art. 3](https://www.althingi.is/lagas/nuna/1997129.html)

Employee mandatory contributions can be deducted from income up to 4% of the contribution base. Qualifying additional pension contributions have a separate deduction up to 4%; regular payment and an eligible recipient are conditions. A tax deduction limit does not itself establish a worker's contractual pension entitlement. [Pension deduction conditions](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/)

Employer pension contributions are not taxable to the employee, except that they become taxable income if the employer's contributions exceed 12% of the contribution base plus 2,000,000 a year. Contributions agreed in a collective agreement or fixed by law are never taxable. [Act 90/2003, art. 28, item 5](https://www.althingi.is/lagas/nuna/2003090.html)

Keep cash and noncash components distinct:

```text
withholding base = taxable cash remuneration + taxable noncash benefits
                   − eligible employee pension deduction − other supported deductions
income tax withheld = maximum of zero and
                      (progressive band tax − authorised available credit)
bank net pay = cash remuneration + supported cash reimbursements
               − employee pension withheld − income tax withheld
               − other authorised cash deductions
```

A noncash benefit can increase taxable income without adding money to the bank payment. Confirm valuation and pension treatment separately. Do not deduct employer pension or employer payroll tax from employee pay. These formulas are accounting controls; a benefit or reimbursement must have its own legal classification before use.

### Employer pension and payroll tax

Calculate employer pension separately from the employee deduction. General 2026 payroll tax (`tryggingagjald`) is 6.35%, made up of 4.90% general levy, 1.35% employment-insurance levy, 0.05% wage-guarantee fund fee and 0.05% market fee. For wages of seamen on fishing vessels add 0.65%, giving 7.00%. Its base includes taxable benefits (food, housing, clothing, car use) at their tax valuation, all vehicle allowances, taxable per diems and ordinary wage-option gains in the year of exercise, as well as wages. Apply the option classification and separate tax dates above; this levy timing is not immediate option PAYE or a rule for every capital plan. Do not reduce this employer base by the employee's pension deduction. Payments that are not taxable to the employee, such as qualifying commuting payments, are outside the base. [Payroll tax](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) [Seamen rate](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

Special cases, each needing evidence before use:

- **Posted EEA workers with an A1 certificate:** for citizens of an EEA state hired to work in Iceland for one year or less, the employer does not pay the full rate if it holds the worker's A1 certificate showing cover under the home country's social security. Skatturinn lists 0.293% for 2024 and 2025 and has not published a 2026 figure on that page; confirm the 2026 rate with Skatturinn before use. These wages are reported separately and excluded from the general base. [A1 rule](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)
- **Financial activities:** screen the employer under Act 165/2011 Articles 2–3, then use the [corporate Guide’s separate financial-sector method](is-corporate-income-tax.md). The 5.5% remuneration tax includes employer pension contributions and has Article 5 exclusions; it is not a blanket percentage of cash wages. Reconcile its own base, monthly return/payment and annual assessment separately from PAYE and the employer levy. [Act 165/2011, Articles 2–10](https://www.althingi.is/lagas/nuna/2011165.html)

Employer pension contributions also enter the payroll-tax base. The wage-return guidance expressly includes the general employer pension contribution among reportable payroll-tax amounts. Use that base rule with the dated current-year rate; the annual-return page's assessment-year label is not a new wage-year rate. [Payroll-tax base reporting](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/)

```text
employer payroll tax = confirmed total payroll-tax base × applicable employer rate
ordinary cash-wage employer cost = cash wages + employer pension + payroll tax
                                  + other applicable employer obligations
```

For benefits, separately reconcile actual employer benefit cost and the tax valuation; they need not be equal. The ordinary cost formula above assumes no benefits or additional employer charges.

## Deadlines and filing

Pension contributions have a separate payment cycle: due on the tenth of the following month, final due date the last day of that month, subject to the applicable fund rules and agreement. Remit to the fund/provider rather than treating them as part of the tax-authority payment. [Act 129/1997, art. 7](https://www.althingi.is/lagas/nuna/1997129.html)

Use the employer service: `Vefskil → Staðgreiðsla → Skila skýrslu`, or supported payroll software. Withholding and payroll tax fall due on the 1st of the month after the wage month, and the return and payment must reach Skatturinn by the 15th (the final due date). Example: January wages are due by 15 February. If the 15th falls on a weekend or public holiday, it moves to the next working day. Confirm the tax calendar and the generated payment claim. Registered legal entities submit a nil return even when no wages were paid; if payroll pauses, still file, or Skatturinn estimates the amount due. [Filing and corrections](https://www.skatturinn.is/einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum/) [Dated reporting rule](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Due dates](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/)

**Small-payroll exception.** If wages (and any calculated remuneration) average less than 42,000 a month, the employer may file and pay for the first time on the due date of the month in which the year's total reaches 504,000, and on every due date after that. If the year's total does not reach 504,000, it may file and pay once for the year, as if it were the December return. [Payment periods](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)

For levy outside withholding, current Act 113/1990 Article 12 sets 1 June for individuals and 1 November for legal entities, with final due dates one month later. Published guidance conflicts: the general levy page says 1 July, while the collections page says 1 June for individuals and 1 October for companies. Use the statute as the legal reference, retain the conflict and resolve the actual assessment/payment claim with Skatturinn before payment. Ordinary taxable benefits remain in monthly reporting. [Act 113/1990, arts. 12 and 16](https://www.althingi.is/lagas/nuna/1990113.html), [general guidance](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald), [collections guidance](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/)

### Map the calculation to the return

The official employer instructions map the monthly return as follows:

| Field | Enter or check |
| --- | --- |
| Kennitala | Employee identifier. |
| Laun og hlunnindi | Wages, car benefits, taxable vehicle allowance and taxable daily allowances. |
| Lífeyrissjóður | Paid deductible employee pension, including eligible supplementary savings. |
| Persónuafsláttur / Persónuafsláttur maka | Authorised credit; spouse credit entered separately. |
| Þrepaskipti / Þar af í þrepi 2 | Allocate taxable income between applicable bands. |
| Mótframlag | Actual employer pension; correct the default when needed. |
| Tryggingagjald / Reikna | Calculate employer payroll tax and reconcile the displayed amount. |
| Source | [Official return instructions](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |

Do not submit the prose calculation as a return. Match each employee row, totals and the payment claim; save the accepted submission and payment evidence.

For an incorrect submitted return, Skatturinn instructs employers to submit the correct return first and then reverse the wrong return using `Vefskil → Staðgreiðsla → Bakfæra skýrslu`; correction login requires the withholding web key. Preserve both references and acknowledgements. Reconcile the resulting liability and actual payments; a return correction is not proof of a cash refund or offset. [Correction sequence](https://www.skatturinn.is/einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum/)

For every run, reconcile wages and benefits, employee deductions, employer pension, tax bases, withholding, payroll tax, the pension-fund payment, bank net pay and ledger. Give the employee the itemised result. At year end reconcile the payroll records to wage statements and employer annual reporting for the actual wage year; use the relevant year's filing instructions before submission. Payroll-tax annual assessment follows the employer wage return. [Annual payroll-tax reporting](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)

## Penalties and interest

**Late payment and missing returns.** If withholding is not paid on time, a surcharge of 1% of the unpaid amount is added for each day after the final due date, up to a maximum of 10%. If it is not paid within a month from the first due date, penalty interest (dráttarvextir) also runs from that first due date. If no return is filed or it is deficient, Skatturinn estimates the amount due and the same surcharge applies, unless the estimated amount was paid before the final due date. The surcharge can be waived only if Skatturinn accepts valid reasons. **Keep payroll levy separate:** Act 113/1990 Article 10 expressly excludes that daily PAYE surcharge from tryggingagjald. If the levy remains unpaid at its final due date, default interest runs from the first due date. Do not apply the withholding surcharge or its interest trigger to the employer levy. [Act 45/1987, art. 28](https://www.althingi.is/lagas/nuna/1987045.html), [Act 113/1990, arts. 10–11](https://www.althingi.is/lagas/nuna/1990113.html), [collection rules](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/)

## Cross-border points

Obtain separate residence and social-security determinations for cross-border workers; the A1 decision does not establish income-tax residence. The A1 limits and unresolved 2026 reduced rate are stated in the base section. Use the [cross-border Guide](is-cross-border.md) for source-payment and residence screening and the [social-contribution Guide](iceland-social-contributions.md) for contribution coverage. Foreign staffing arrangements, nonresidents and treaty relief require the applicable facts and rules before final withholding. [2026 employer guidance](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

## Worked examples that recompute

These hypothetical monthly cases assume an ordinary adult employee, full authorised monthly credit, eligible employee pension at 4%, employer pension at 11.5%, no additional savings, no benefits and no other charges unless expressly stated. Figures use exact arithmetic and show two decimal places with final rounding; actual reporting must follow the service's currency/rounding requirements. They are not authority-approved payroll outputs. [Rates and pension inputs](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) The official case below is the filing reference for identical inputs; the decimal table is secondary arithmetic validation. Do not infer a universal rounding rule from one official example.

### Official monthly example and reconciled payment

For cash wages 600,000, employee pension 24,000, taxable income 576,000, credit 72,492 and employer pension 69,000, the authority displays withholding **113,953** and payroll tax **42,482**. The taxable allocation is 498,122 in the first band and 77,878 in the second. [Official example](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

Using those displayed results, bank pay is **462,047** and employer cost is **711,482**. Reconcile bank pay plus employee pension plus withholding to cash wages; reconcile wages plus employer pension plus payroll tax to cost. These are derived controls for the official example. Actual employer/employee facts and the accepted service output still control filing. [Source illustration](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

### Decimal validation examples

Displayed band subtotals are individually rounded for readability; total tax is calculated from unrounded components, so the displayed subtotals can differ from the rounded total.

| Case | Employee result | Employer result |
| --- | --- | --- |
| A: cash wages 400,000 | Employee pension 16,000; taxable base 384,000; band tax 120,921.60; withholding 48,429.60; bank net 335,570.40. | Employer pension 46,000; payroll-tax base 446,000; payroll tax 28,321; combined cost 474,321. |
| B: cash wages 600,000 | Employee pension 24,000; base 576,000. First-band tax 156,858.62; remaining base 77,878 gives second-band tax 29,585.85. Total band tax 186,444.47; withholding 113,952.47; bank net 462,047.53. | Employer pension 69,000; payroll-tax base 669,000; payroll tax 42,481.50; combined cost 711,481.50. |
| C: cash wages 200,000 | Employee pension 8,000; base 192,000; band tax 60,460.80; withholding zero; bank net 192,000. Unused monthly credit 12,031.20 needs supporting same-year records before later use. | Employer pension 23,000; payroll-tax base 223,000; payroll tax 14,160.50; combined cost 237,160.50. |
| K: cash wages 1,800,000 | Employee pension 72,000; taxable base 1,728,000. First-band tax 156,858.62; second-band tax 342,034.61; third-band excess 329,550 gives tax 152,548.70. Total band tax 651,441.92; withholding 578,949.92; bank net 1,149,050.08. | Employer pension 207,000; payroll-tax base 2,007,000; payroll tax 127,444.50; combined cost 2,134,444.50. |
| Evidence | [Rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) and [pension](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) | [Payroll tax](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) |
| D: illustrative noncash control only | Cash 400,000, already-established taxable noncash benefit 20,000, documented deductible pension 16,000: base 404,000; band tax 127,219.60; withholding 54,727.60; bank net 329,272.40. | Confirm benefit valuation, pensionability, employer contributions and employer tax base separately; no total-cost conclusion. |

### Rule checks

| Case | Result |
| --- | --- |
| L: child born 2012, total 2026 wages 450,000 from one employer | Taxed only above the 300,000 child allowance: 150,000 × 6% = 9,000; no personal credit; no pension contributions. |
| M: withholding of 1,000,000 paid 4 days after the final due date | Surcharge 1% per day = 40,000; penalty interest applies only if unpaid a month from the first due date. |
| N: same amount paid 12 days late | Surcharge capped at 10% = 100,000; penalty interest from the first due date also applies if unpaid a month from that date. |
| Evidence | [Child rate](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) and [Act 45/1987, art. 28](https://www.althingi.is/lagas/nuna/1987045.html) |

Additional decision checks: exactly at the first band ceiling, no amount enters the next band; above the upper ceiling, only the excess enters the highest band. A second employer without current bracket/credit instructions must obtain them before a final calculation. A prior-year unused credit cannot reduce this year's tax. A spouse's credit is used only for spouses living together or qualifying cohabitants, against the Skatturinn statement. A vehicle allowance without a driving log is taxable pay. An erroneous filed return follows the correct-then-reverse sequence. A registered legal entity with no wages still files the nil return.

### Recomputable arithmetic controls

These blocks implement cases A, C and K, the stated noncash case and the displayed official reference. They check arithmetic only. They do not infer a statutory currency-rounding rule from a decimal illustration.

```oa-check
name: Iceland payroll A, ordinary monthly cash wages 2026
inputs:
  wages: 400000
  credit: 72492
steps:
  - employee_pension: wages * 0.04
  - tax_base: wages - employee_pension
  - withholding: max(0, tax_base * 0.3149 - credit)
  - net_cash: wages - employee_pension - withholding
  - employer_pension: wages * 0.115
  - levy_base: wages + employer_pension
  - payroll_levy: levy_base * 0.0635
  - employer_cost: wages + employer_pension + payroll_levy
expected:
  tax_base: 384000
  withholding: 48429.60
  net_cash: 335570.40
  levy_base: 446000
  payroll_levy: 28321
  employer_cost: 474321
```

```oa-check
name: Iceland payroll C, unused credit cannot make withholding negative
inputs:
  wages: 200000
  credit: 72492
steps:
  - employee_pension: wages * 0.04
  - tax_base: wages - employee_pension
  - band_tax: tax_base * 0.3149
  - withholding: max(0, band_tax - credit)
  - unused_credit: max(0, credit - band_tax)
  - net_cash: wages - employee_pension - withholding
expected:
  tax_base: 192000
  band_tax: 60460.80
  withholding: 0
  unused_credit: 12031.20
  net_cash: 192000
```

```oa-check
name: Iceland payroll K, upper band only on the excess
inputs:
  wages: 1800000
  first_ceiling: 498122
  second_ceiling: 1398450
  credit: 72492
steps:
  - employee_pension: wages * 0.04
  - tax_base: wages - employee_pension
  - band_one: min(tax_base, first_ceiling) * 0.3149
  - band_two: max(0, min(tax_base, second_ceiling) - first_ceiling) * 0.3799
  - band_three: max(0, tax_base - second_ceiling) * 0.4629
  - band_tax: band_one + band_two + band_three
  - withholding: max(0, band_tax - credit)
  - net_cash: wages - employee_pension - withholding
  - employer_pension: wages * 0.115
  - payroll_levy: (wages + employer_pension) * 0.0635
  - employer_cost: wages + employer_pension + payroll_levy
expected:
  tax_base: 1728000
  band_tax: 651441.92
  withholding: 578949.92
  net_cash: 1149050.08
  payroll_levy: 127444.50
  employer_cost: 2134444.50
```

```oa-check
name: Iceland payroll D, a taxable noncash benefit does not add bank cash
inputs:
  cash_wages: 400000
  taxable_benefit: 20000
  documented_pension: 16000
  credit: 72492
steps:
  - tax_base: cash_wages + taxable_benefit - documented_pension
  - withholding: max(0, tax_base * 0.3149 - credit)
  - bank_net: cash_wages - documented_pension - withholding
expected:
  tax_base: 404000
  withholding: 54727.60
  bank_net: 329272.40
```

```oa-check
name: Iceland displayed official monthly example, reconciliation only
inputs:
  wages: 600000
  employee_pension: 24000
  displayed_withholding: 113953
  employer_pension: 69000
  displayed_levy: 42482
steps:
  - bank_net: wages - employee_pension - displayed_withholding
  - cash_reconciliation: bank_net + employee_pension + displayed_withholding
  - employer_cost: wages + employer_pension + displayed_levy
expected:
  bank_net: 462047
  cash_reconciliation: 600000
  employer_cost: 711482
```

For cases M and N the principal below is **PAYE withholding**, not the employer levy, and the block computes only the capped surcharge, excluding any separately due interest:

```oa-check
name: Iceland PAYE late-payment surcharge cap, not tryggingagjald
inputs:
  unpaid_withholding: 1000000
steps:
  - four_days: unpaid_withholding * min(4 * 0.01, 0.10)
  - twelve_days: unpaid_withholding * min(12 * 0.01, 0.10)
expected:
  four_days: 40000
  twelve_days: 100000
```

### Benefit control 1: leased-car compound reduction and charging-only rate

Use the authority's 2021 lease example: supported original reference value **10 million** and five permitted 10% annual reductions through 2026 give **5,904,900**, not 5 million from a straight 50% subtraction. At 28%, the annual benefit is **1,653,372**, or **137,781 monthly**. For the same established reference value, a qualifying pure-electric car with only employee-paid charging and employer-paid other running costs uses **19%**, giving **93,494.25 monthly**; 17% requires the different full-running-cost conditions. Assume full-year private availability, no employee-use payment and no other exception. [Section 2.3][benefit-notice]

```oa-check
name: Iceland leased car compound reduction and pure electric charging only
inputs:
  supported_reference_value: 10000000
  annual_retention: 0.90
steps:
  - reduced_value: max(supported_reference_value * 0.50, supported_reference_value * annual_retention * annual_retention * annual_retention * annual_retention * annual_retention)
  - fossil_annual_benefit: reduced_value * 0.28
  - fossil_monthly_benefit: fossil_annual_benefit / 12
  - electric_charging_only_monthly: reduced_value * 0.19 / 12
expected:
  reduced_value: 5904900
  fossil_annual_benefit: 1653372
  fossil_monthly_benefit: 137781
  electric_charging_only_monthly: 93494.25
```

### Benefit control 2: car value floor, partial availability and paid use

Assume a fossil car bought after 2013 has an original supported price of **10 million**, seven permitted reductions and no qualifying employee-paid running costs. The 50% floor gives **5 million** instead of the lower reducing-balance result. Assume the authority's 15 January–10 June availability pattern, hence **five commenced monthly periods**, and **50,000** separately paid by the employee for use. Gross period value is **583,333.33**, net taxable benefit **533,333.33**, before filing rounding. Do not use a daily housing fraction or count six calendar-month names. Eligibility, actual availability and paid-use evidence are assumptions. [Section 2.3][benefit-notice]

```oa-check
name: Iceland full use car floor and five commenced monthly periods
inputs:
  original_supported_price: 10000000
  retention: 0.90
  proved_commenced_months: 5
  employee_paid_use: 50000
steps:
  - value_before_floor: original_supported_price * retention * retention * retention * retention * retention * retention * retention
  - supported_value: max(original_supported_price * 0.50, value_before_floor)
  - full_year_value: supported_value * 0.28
  - gross_period_value: full_year_value * proved_commenced_months / 12
  - taxable_period_value: max(0, gross_period_value - employee_paid_use)
expected:
  value_before_floor: 4782969
  supported_value: 5000000
  full_year_value: 1400000
  gross_period_value: 583333.33
  taxable_period_value: 533333.33
```

### Benefit control 3: car value enters PAYE and levy, with separate cash/pension

Assume an ordinary adult with **600,000 cash wages**, a fully supported **210,000 noncash car value** for the month (the authority's 2025 purchase/2026 fossil-car example), full authorised monthly credit and no other item. Under the assumed documented arrangement, pension contributions are 4%/11.5% on **cash wages only**; no contractual broader benefit base applies. Employee pension is **24,000**, PAYE base **786,000**, decimal withholding **193,731.47** and bank pay **382,268.53**. Employer pension is **69,000**; the employer-levy base is **879,000**, giving **55,816.50** at 6.35%. Do not add the car value to bank pay or subtract employee pension from the levy base. Actual car cost and any other employer charges still need their own cost schedule, so this is not total employment cost. Final service rounding remains a separate check. [2026 employer notice 1](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf); [Benefit section 2.3][benefit-notice]; [Pension Act, Article 3](https://www.althingi.is/lagas/nuna/1997129.html); [Levy Act, Articles 7–8](https://www.althingi.is/lagas/nuna/1990113.html)

```oa-check
name: Iceland car benefit separate cash pension PAYE and employer levy bases
inputs:
  cash_wages: 600000
  proved_car_value: 210000
  employee_pension_rate: 0.04
  employer_pension_rate: 0.115
  first_ceiling: 498122
  second_ceiling: 1398450
  authorised_credit: 72492
steps:
  - employee_pension: cash_wages * employee_pension_rate
  - employer_pension: cash_wages * employer_pension_rate
  - paye_base: cash_wages + proved_car_value - employee_pension
  - band_one: min(paye_base, first_ceiling) * 0.3149
  - band_two: max(0, min(paye_base, second_ceiling) - first_ceiling) * 0.3799
  - band_three: max(0, paye_base - second_ceiling) * 0.4629
  - withholding: max(0, band_one + band_two + band_three - authorised_credit)
  - bank_pay: cash_wages - employee_pension - withholding
  - employer_levy_base: cash_wages + proved_car_value + employer_pension
  - employer_levy: employer_levy_base * 0.0635
expected:
  employee_pension: 24000
  employer_pension: 69000
  paye_base: 786000
  withholding: 193731.47
  bank_pay: 382268.53
  employer_levy_base: 879000
  employer_levy: 55816.50
```

### Benefit control 4: ordinary housing is by days, with separate energy

Assume ordinary employee housing within the section 2.8 general branch, applicable property/land assessment **60 million**, an established **0.8 municipality factor**, **30 days** of 2026 occupancy, **20,000** employee rent for that period and **10,000** free energy at supported cost. No owner/director, mandatory-residence relief, work-camp or holiday rule applies. Annual housing value is **2.4 million**; period housing before rent is **197,260.27**. After paid rent and adding energy, taxable value is **187,260.27** before filing rounding. The assumed assessment and use facts must be proved; this is not a director-property example. [Sections 1 and 2.8][benefit-notice]

```oa-check
name: Iceland ordinary employee housing day fraction and paid rent energy
inputs:
  applicable_assessment: 60000000
  supported_location_factor: 0.8
  proved_occupancy_days: 30
  year_days: 365
  employee_rent: 20000
  free_energy_cost: 10000
steps:
  - annual_housing_value: applicable_assessment * 0.05 * supported_location_factor
  - period_housing_before_rent: annual_housing_value * proved_occupancy_days / year_days
  - taxable_housing_and_energy: max(0, period_housing_before_rent - employee_rent) + free_energy_cost
expected:
  annual_housing_value: 2400000
  period_housing_before_rent: 197260.27
  taxable_housing_and_energy: 187260.27
```

### Benefit control 5: commuting trip thresholds and payment excess

Assume the required signed agreement, qualifying mode, monthly work period and trip evidence are established, and each alternative employee receives **11,500**. At **80 qualifying trips out of 100**, the full 11,500 can be excluded. At **79/100** or **40/100**, only **5,750** can be excluded and 5,750 is taxable. At **39/100**, none is excluded. Without the required agreement the payment is not made exempt by the trip percentage alone. The control uses the legally established cap for each alternative; arithmetic does not verify mode or agreement. [Section 2.6][benefit-notice]

```oa-check
name: Iceland commuting full half and zero supported caps
inputs:
  monthly_payment: 11500
  established_80_percent_case_cap: 11500
  established_79_percent_case_cap: 5750
  established_40_percent_case_cap: 5750
  established_39_percent_case_cap: 0
steps:
  - taxable_at_80: max(0, monthly_payment - established_80_percent_case_cap)
  - taxable_at_79: max(0, monthly_payment - established_79_percent_case_cap)
  - taxable_at_40: max(0, monthly_payment - established_40_percent_case_cap)
  - taxable_at_39: max(0, monthly_payment - established_39_percent_case_cap)
expected:
  taxable_at_80: 0
  taxable_at_79: 5750
  taxable_at_40: 5750
  taxable_at_39: 11500
```

### Benefit control 6: separate meal, staff-event and fitness schedules

These are separate hypothetical schedule checks, not items assumed to arise in one payroll month. Twenty lunches at **751** each with **500** paid by the employee per lunch leave **5,020** taxable food value. A supported all-staff event/treat allocation of **220,000** for the year leaves **28,000** above the 192,000 limit; a separate **5,000 cash gift** remains fully taxable. Assume a **100,000** fitness reimbursement consists of 90,000 proved qualifying exercise and 10,000 equipment: at most **85,000** is excluded, leaving **15,000** taxable. The equipment does not qualify simply because the annual exercise ceiling has unused room. These calculations assume the stated classification/evidence and do not determine the pension base of every reimbursement. [Sections 1, 2.1, 2.7 and 2.9][benefit-notice]

```oa-check
name: Iceland food employee payment and annual event fitness exclusions
inputs:
  lunch_count: 20
  lunch_value: 751
  employee_payment_per_lunch: 500
  qualified_event_annual_cost: 220000
  event_limit: 192000
  cash_gift: 5000
  total_fitness_reimbursement: 100000
  proved_qualifying_exercise_cost: 90000
  fitness_limit: 85000
steps:
  - taxable_food: lunch_count * max(0, lunch_value - employee_payment_per_lunch)
  - taxable_event_excess: max(0, qualified_event_annual_cost - event_limit)
  - taxable_cash_gift: cash_gift
  - exempt_fitness: min(total_fitness_reimbursement, proved_qualifying_exercise_cost, fitness_limit)
  - taxable_fitness: total_fitness_reimbursement - exempt_fitness
expected:
  taxable_food: 5020
  taxable_event_excess: 28000
  taxable_cash_gift: 5000
  exempt_fitness: 85000
  taxable_fitness: 15000
```

### Option examples: ordinary wage component versus qualifying capital plan

These domestic resident examples assume one unlisted share holding, no other shares of the same class, no sale costs or capital losses, no applicable capital exemption and supported values. They distinguish computation from eligibility and collection. The 22% capital rate follows the [individual Guide's capital method](iceland-income-tax.md); the deferred wage component still needs the person's applicable earned-income computation.

For an ordinary Article 9 option, assume exercise in 2025 at a total strike of 600,000 and market value of 1,000,000. The wage component is 400,000, fixed at exercise. If the first ownership change is a 2026 sale for 1,300,000, the wage tax charge arises then, while the separate capital gain is 300,000 and capital tax is 66,000. The exercise-year levy and exercise reporting remain separate; this illustration does not calculate wage tax or assert a 2025 levy payment was made. [Articles 9 and 18][option-act]; [exercise reporting and levy guidance][benefit-guidance]

```oa-check
name: Iceland ordinary option fixed exercise wage and later capital gain
inputs:
  contract_purchase_price: 600000
  exercise_market_value: 1000000
  later_sale_proceeds: 1300000
  capital_rate: 0.22
steps:
  - deferred_wage: exercise_market_value - contract_purchase_price
  - capital_basis: exercise_market_value
  - capital_gain: later_sale_proceeds - capital_basis
  - capital_tax: capital_gain * capital_rate
  - economic_gain: later_sale_proceeds - contract_purchase_price
  - separated_gain: deferred_wage + capital_gain
expected:
  deferred_wage: 400000
  capital_basis: 1000000
  capital_gain: 300000
  capital_tax: 66000
  economic_gain: 700000
  separated_gain: 700000
```

If instead **all Article 10 conditions are proved**, assume the same 600,000 contract price and 1,300,000 sale proceeds, with exercise in 2024 and sale after the full two-year holding period in 2026. The capital amount is 700,000 and tax 154,000. The intermediate 1,000,000 exercise value does not become the basis for this qualifying sale. This is not a claim that the two regimes have the same eligibility, dates, employer charges or total tax. [Article 10][option-act]; [published conditions][option-form]

```oa-check
name: Iceland qualifying employee option capital gain uses original purchase price
inputs:
  contract_purchase_price: 600000
  sale_proceeds: 1300000
  capital_rate: 0.22
steps:
  - qualifying_capital_gain: sale_proceeds - contract_purchase_price
  - capital_tax: qualifying_capital_gain * capital_rate
expected:
  qualifying_capital_gain: 700000
  capital_tax: 154000
```

## Ask the client first

- What are the employee identity, age, residence, work location, wage period and pay date?
- What contract, collective agreement, pension fund and contribution arrangement apply?
- Which cash wages, benefits, reimbursements and other deductions are supported?
- For benefits, which availability/use agreements, vehicle values and running costs, housing assessments/days, meal/employee-payment records, signed commuting evidence, annual reimbursement totals and loan benchmarks establish the classification and valuation?
- For equity, which actual instrument, grant/exercise/ownership-change records, market and cost basis, prior plan/project confirmations, eligibility and reporting records prove the Article 9, 10 or 10a branch?
- What current bracket, own-credit and spouse-credit instructions and prior usage apply?
- Which prior returns, payment claims, bank payments and pension statements require reconciliation or correction?

## When to refuse or refer

- Return the period, employee scope, evidence gaps, each cash/noncash component, pension fund and bases, employee and employer contributions, band calculation and credit usage, withholding, bank net, employer costs, filing deadline and references, and reconciliation result. Do not label an unresolved input as confirmed. Recheck before the next wage year, when an official rate/rule changes, or when worker status, pension terms, residence or benefit arrangements change.
- Refer for a specific supported method; do not substitute this ordinary calculation: cross-border workers (determine domicile, rolling-period presence and any treaty entitlement under the [cross-border residence method](is-cross-border.md); a short stay alone does not establish limited tax liability), posted workers and A1 cases, workers hired through a foreign staffing agency (the user undertaking can become liable for withholding), seamen, financial undertakings, board fees, disputed worker classification, and self-employed calculated remuneration. [Limited tax liability and staffing agencies](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

<!-- openaccountants-cta-block -->

## Talk to an accountant

For advice on your facts, [contact OpenAccountants](https://www.openaccountants.com/contact).

## Sources

The following primary sources were accessed on 23 October 2026. This pass checked the contribution-base and penalty corrections, the stated 2026 benefit and option methods and example inputs; it does not attest to all remaining scope or operational questions.

| Official source | Read on |
| --- | --- |
| [Withholding Act 45/1987](https://www.althingi.is/lagas/nuna/1987045.html) | 2026-10-23 |
| [Levy Act 113/1990](https://www.althingi.is/lagas/nuna/1990113.html) | 2026-10-23 |
| [Pension Act 129/1997](https://www.althingi.is/lagas/nuna/1997129.html) | 2026-10-23 |
| [Income Tax Act 90/2003](https://www.althingi.is/lagas/nuna/2003090.html) | 2026-10-23 |
| [atvinnurekstur/ad-hefja-rekstur/launagreidendaskra](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/) | 2026-10-23 |
| [atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/) | 2026-10-23 |
| [atvinnurekstur/rafraen-skil/stadgreidsla](https://www.skatturinn.is/atvinnurekstur/rafraen-skil/stadgreidsla/) | 2026-10-23 |
| [atvinnurekstur/skattar-og-gjold/tryggingagjald](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) | 2026-10-23 |
| [atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) | 2026-10-23 |
| [einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum](https://www.skatturinn.is/einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum/) | 2026-10-23 |
| [einstaklingar/stadgreidsla/ofnyttur-personuafslattur](https://www.skatturinn.is/einstaklingar/stadgreidsla/ofnyttur-personuafslattur/) | 2026-10-23 |
| [einstaklingar/stadgreidsla/personuafslattur](https://www.skatturinn.is/einstaklingar/stadgreidsla/personuafslattur/) | 2026-10-23 |
| [einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/) | 2026-10-23 |
| [english/individuals/key-rates-and-amounts/2026](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) | 2026-10-23 |
| [english/individuals/personal-tax-credit](https://www.skatturinn.is/english/individuals/personal-tax-credit/) | 2026-10-23 |
| [innheimta/skattar-og-gjold/allir-skattar-og-gjold](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/) | 2026-10-23 |
| [media/2026/rsk_0601_1_2026.is.pdf](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) | 2026-10-23 |
| [Posted-worker personal credit](https://www.skatturinn.is/english/individuals/posted-workers/) | 2026-10-23 |
| [Limited-liability employment credit](https://www.skatturinn.is/english/individuals/limited-tax-liability/) | 2026-10-23 |
| [Financial activities tax, Act 165/2011](https://www.althingi.is/lagas/nuna/2011165.html) | 2026-10-23 |
| [2026 valuation rules, official January employer notice 2, sections 1–2.10 and 3.1][benefit-notice] | 2026-10-23 |
| [Current income-year 2026 valuation page](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/skattmat/) | 2026-10-23 |
| [Authority benefit/car operational explanation][benefit-guidance] | 2026-10-23 |
| [Regulation 591/1987, withholding exclusions and travel evidence](https://files.reglugerd.is/pdf/0591-1987/current) | 2026-10-23 |
| [Central Bank, monthly bank/general-rate portal; no permanent rate asserted][loan-benchmarks] | 2026-10-23 |
| [2026 wage statement, expressly for 2025 wages; layout only][benefit-wage-form] | 2026-10-23 |
| [Current Income Tax Act, option classification, basis and startup definition][option-act] | 2026-10-23 |
| [Innovation Act 152/2009, Articles 3 and 5](https://www.althingi.is/lagas/nuna/2009152.html) | 2026-10-23 |
| [RSK 2.085, 5 November 2024; statutory computation discrepancy retained][option-form] | 2026-10-23 |

The authority's linked [2026 Gazette entry](https://island.is/stjornartidindi/nr/2771f46a-7402-4e33-87de-16a856e3f81f) returned HTTP 403 in the web reader. The six-page official employer-notice reproduction and current authority text were read; no successful Gazette retrieval is claimed. This addition is outside the earlier country-review snapshots and needs independent source review. Actual benefit classification, values, contractual pension terms, changing monthly loan/travel benchmarks, insufficient-cash settlement and accepted reporting remain case/operational evidence requirements. Weekly rounding, A1 and other specialist gaps remain open.

[benefit-notice]: https://www.skatturinn.is/media/2026/rsk_0601_2_2026.is.pdf
[benefit-guidance]: https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/launatekjur-og-hlunnindi/
[loan-benchmarks]: https://sedlabanki.is/gagnatorg/vextir
[benefit-wage-form]: https://www.skatturinn.is/media/rsk02/rsk_0201_2026.is.pdf
[option-act]: https://www.althingi.is/lagas/nuna/2003090.html
[option-form]: https://www.skatturinn.is/media/rsk02/rsk_02085.is.pdf
