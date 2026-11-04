---
name: es-corporate-tax
description: "Use this Guide to compute Spanish common-territory corporate income tax for a period beginning in 2026. It covers residence, accounting-to-tax adjustments, microcompany and small-company rates, depreciation, finance costs, participation income, capitalisation and levelling reserves, carried-forward losses, credits, the domestic minimum tax, annual Modelo 200 and Modelo 202 instalments. Trigger phrases include Impuesto sobre Sociedades, IS, SL taxes, empresa de reducida dimensión, bases imponibles negativas, reserva de capitalización, reserva de nivelación, pagos fraccionados and corporate exit tax. Obtain the exact period, territory, entity status, aggregated turnover and accounts before computing. The September 2026 Ceuta and Melilla amendments have specific effective-date tests. Foral taxes, consolidation, reorganisations and specialist incentive claims require their own verified analysis."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/es-corporate-tax"
  jurisdiction: "ES"
  tax_year: "2026"
  last_updated: "2026-10-28"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Corporate income tax in Spain v1.3

Compute Spanish corporate tax for a period beginning in 2026 from the accounts, then test the company's rate, reliefs and minimum tax. This revision is sourced from the law; independent whole-pack review is pending and no accountant has signed it off.

> **Based on work by Nambu89 (Impuestify)** and **Pau March (larenta)**, licensed under MIT. Adapted for the OpenAccountants format. The two source links were on a code hosting site, which is not an official source, so the links are not reproduced here.

> **General reference only.** Produce a computation, reconciliation and filing checklist for a qualified reviewer. Obtain missing facts rather than substituting a territory, entity type, accounting treatment or turnover.

## Who this applies to

[Ley 27/2014 (LIS), arts. 7–8](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a7) taxes resident legal persons, apart from civil-law partnerships without a commercial object, and the funds and other vehicles expressly listed in art. 7. A resident is taxed on worldwide income. Residence follows **any** of incorporation under Spanish law, Spanish registered office, or effective management in Spain; effective management means direction and control of the whole activity. Incorporation alone can therefore retain Spanish residence after management moves.

This Guide computes the common-territory regime. The [foral corporate Guide](es-foral-corporate-tax.md) supplies the separate four territorial ordinary methods and law/collection allocation, with its precise unresolved branches identified. Establish whether common or Basque/Navarre foral tax rules apply before using the rates. The fiscal period follows the entity's accounting year, cannot exceed **12 months**, and closes on extinction, transfer of residence abroad and the other transformations in [LIS art. 27](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a27). The period's **start year**, not the year the return is filed, determines the staged 2026 rates.

For a patrimonial entity, test assets under [LIS art. 5.2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a5), including its valuation and excluded-security rules; it is not enough to label a company a holding company. Patrimonial status excludes the ordinary micro, reduced-dimension and newly created rates in art. 29.1. Fully exempt and partially exempt bodies follow art. 9 and the filing exceptions below. Non-residents and Spanish permanent establishments require the IRNR rules as well.

## Rates, bands and thresholds

Unless stated otherwise, these apply to **periods beginning in 2026**. Check the statutory exclusions before selecting a row.

| Item | Amount or test | Tax year | Official source |
|---|---|---|---|
| Ordinary corporate rate | 25% | 2026 | [LIS art. 29.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a29) |
| Microcompany turnover test | Immediately preceding period's net turnover below EUR 1 million; annualisation and aggregation apply | 2026 | [LIS DT 44.2.a; arts. 101.2–101.3](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#dt-6) |
| Microcompany rate | 19% on the first EUR 50,000 of taxable base; 21% on the excess | 2026 | [LIS DT 44.2.a](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#dt-6) |
| Short-period microcompany first band | EUR 50,000 × period days / 365, capped at the base | 2026 | [LIS DT 44.2.a](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#dt-6) |
| Reduced-dimension entity (ERD) | 23%, subject to another applicable special rate; art. 101 ordinarily requires prior-period net turnover below EUR 10 million | 2026 | [LIS DT 44.2.b; art. 101](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#dt-6) |
| Qualifying newly created economic activity | 15% in the first positive-base period and the next, unless a lower rate applies | 2026 | [LIS art. 29.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a29) |
| Credit institutions and specified hydrocarbon activity | 30%; the article distinguishes activities outside that special rate | 2026 | [LIS art. 29.6](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a29) |
| Qualifying Ley 49/2002 bodies / qualifying investment vehicles / pension funds | Respectively 10% / 1% / 0%; each has its own eligibility conditions | 2026 | [LIS arts. 29.3–29.5](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a29) |
| Protected cooperatives' cooperative results | Applicable art. 29.1 rates less 3 percentage points, capped at 20%; separate rules govern credit cooperatives and extra-cooperative results | 2026 | [LIS art. 29.2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a29) |
| Credit cooperatives and rural savings banks | Applicable art. 29.1 rates for cooperative results; **30% for extra-cooperative results** | 2026 | [LIS art. 29.2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a29) |
| General loss-offset percentage | 70% of the positive base before capitalisation reserve and loss relief | 2026 | [LIS art. 26.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a26) |
| Large-company loss-offset percentages | 50% for preceding-12-month turnover at least EUR 20m but below EUR 60m; 25% from EUR 60m | 2026 | [LIS DA 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#dadecimoquinta) |
| Minimum ordinary loss capacity | EUR 1m, proportionately reduced for a short period, subject to available positive base and eligible losses | 2026 | [LIS arts. 26.1–26.2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a26) |
| Net finance-cost limit | 30% of statutory operating profit; at least EUR 1m current-period net costs deductible, prorated for a short period | 2026 | [LIS arts. 16.1, 16.4](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a16) |
| Capitalisation reserve | Generally 20% of qualifying own-funds increase; enhanced headcount bands and base caps below | 2026 | [LIS art. 25](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a25) |
| Levelling reserve | Up to 10% of positive base, maximum EUR 1m, prorated for a short period | 2026 | [LIS art. 105.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a105) |
| Domestic minimum tax trigger | Preceding-12-month turnover at least EUR 20m, or tax consolidation regardless of turnover | 2026 | [LIS art. 30 bis.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a3-3) |
| Domestic minimum percentages | Generally 15%; qualifying new companies 10%; specified art. 29.6 entities 18%; cooperatives 60% of their gross tax | 2026 | [LIS art. 30 bis.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a3-3) |
| Reduced-rate domestic minimum formula | Multiply the applicable micro scale or ERD rate by 15/25 and round upward; this is a minimum-tax test, not the ordinary tax rate | 2026 | [LIS art. 30 bis.1 and DT 44.2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a3-3) |
| General corporate withholding | 19%; image-right income 24%; taxable special lottery prizes 20% | 2026 | [LIS art. 128.6](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a128) |

For the ordinary ERD/micro tests, aggregate group turnover under art. 101.3 and annualise a short prior period or activity under art. 101.2. Exactly EUR 1m is outside the micro threshold. Art. 101.4 can preserve ERD incentives for **three following periods** after the EUR 10m threshold is reached where its historical conditions hold. A new entity is not automatically a qualifying new business: transferred related-party activity, the specified activity previously conducted by a majority individual owner, group membership and patrimonial status can disqualify it (art. 29.1).

**Other start years.** Do not apply 2026 rates to a period beginning in 2025 and ending in 2026. DT 44 gives micro rates **21%/22% in 2025**, then **19%/21% in 2026**, before the art. 29.1 **17%/20%** scale from 2027. The ERD transition is **24%, 23%, 22%, 21%** for starts in **2025, 2026, 2027, 2028**, then **20%**. The EUR 50,000 band is prorated for a short period. These are the statute's dated transitions, not predictions ([DT 44](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#dt-6)).

## The base

### 1. Reconcile the accounts to tax

Start from accounting profit determined under the Commercial Code and applicable accounting rules, then make the adjustments required by tax law ([LIS art. 10.3](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a10)). Keep a schedule by item, accounting amount, tax amount, difference, timing reversal and article. Account for the accrual and booking requirements in [art. 11](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a11); an unpaid invoice is not automatically outside the period.

Add back own-funds remuneration, including the specified group participating-loan interest; corporate and complementary tax expenses; criminal/administrative penalties and the statutory late/enforcement surcharges; gambling losses; and other disallowances in [art. 15](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a15). Add back equity-interest impairment within the categories in art. 15.k, testing its incorporated art. 21 holding/foreign-tax conditions. Donations are not an ordinary expense deduction, although a separate tax credit is available when its own conditions hold. Client/supplier entertainment is capped at **1% of period net turnover**; customary staff, promotion and income-correlated expenses are not automatically donations. Do not equate every director payment with a prohibited distribution; art. 15.e expressly addresses employment/senior-management remuneration. Test related-party pricing under art. 18 and special group-acquisition finance restrictions under art. 15.h.

Bad-debt impairment follows [art. 13.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a13): for example, **six months** overdue, insolvency proceedings or the specified judicial/arbitration circumstances. Public-authority, related-party and general portfolio provisions have exclusions. Qualifying ERDs have the separate **1%** collective debtor allowance with exclusions and roll-forward mechanics in [art. 104](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a104). Do not deduct both an individual impairment and a collective allowance on the same included debt.

For finance costs, calculate the statutory net costs and operating-profit measure, not an unadjusted accounts EBITDA. Art. 16 excludes specified non-deductible/hybrid items and income outside the tax base from its measure. Carry disallowed net costs forward without a fixed expiry; unused percentage capacity can augment limits in the following **five years**. Apply acquisition-debt limits and the credit/insurance and qualifying extinction exceptions separately (art. 16).

### 2. Compute depreciation and investment differences

[LIS art. 12](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) accepts effective depreciation using its linear table, permitted declining-balance or sum-of-digits methods, an approved plan, or justified actual depreciation. Building/furniture restrictions apply to the alternative methods. Retain the asset's cost, start-of-use date, useful life, method, accounting charge, tax charge and closing tax basis.

| Selected linear asset class | Maximum annual coefficient / maximum years | Tax year | Source |
|---|---|---|---|
| General civil works / commercial, administrative, service and residential buildings | 2% / 100 years | 2026 | [LIS art. 12.1.a](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) |
| Industrial buildings | 3% / 68 years | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) |
| Other installations / furniture / other assets | 10% / 20 years | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) |
| Machinery | 12% / 18 years | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) |
| External transport equipment | 16% / 14 years | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) |
| Lorries | 20% / 10 years | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) |
| Data-processing equipment | 25% / 8 years | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) |
| Computer systems and software | 33% / 6 years | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a12) |

Intangibles follow reliable useful life; where it cannot be reliably estimated, and for goodwill, the annual tax ceiling is **one twentieth**, equivalent to **5%**. New tangible assets costing no more than **EUR 300 each** can be freely depreciated within a **EUR 25,000** period cap, prorated for a short period (arts. 12.2–12.3.e). Qualifying ERDs can use accelerated depreciation for the new assets in [art. 103](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a103). The separate employment-linked free-depreciation limit is **EUR 120,000 per qualifying average-headcount increase**, with the acquisition, **24-month increase and further 24-month maintenance** tests in [art. 102](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a102). Keep the eligibility schedule; do not claim it merely because one employee joined.

### 3. Apply participation and foreign-income treatment

[LIS art. 21](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a21) requires at least a **5%** direct/indirect holding and the relevant **one-year** holding test. A dividend can complete that year through subsequent holding; a disposal must satisfy the relevant condition on the disposal date. Foreign subsidiaries also require the statutory analogous tax test, generally a nominal **10%**, with the applicable treaty/information-exchange rule. Check indirect holdings, deductible payer distributions, patrimonial entities, reorganisations and loss restrictions before concluding an exemption.

Art. 21.10 reduces qualifying exempt dividends and gains by **5% for management costs**, giving a derived **95% exempt amount** in the ordinary case. This arithmetic is allowed; the statute need not print the derived result. The art. 21.11 exception concerns dividends, not a universal full exemption for all small companies: it requires prior turnover below **EUR 40m**, the non-patrimonial and prior group/holding restrictions, a wholly owned subsidiary incorporated after **1 January 2021**, and receipt within the specified **three following years**. Record each condition separately.

Qualifying foreign permanent-establishment positive income follows [art. 22](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a22); ordinary foreign PE losses are not imported into the Spanish base, while cessation has its own netting rules. For taxable foreign income, test the credit for actual foreign tax against the corresponding Spanish tax under [arts. 31–32](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a31). Large companies within DA 15 have a separate **50% gross-tax cap** on the listed international double-tax credits. Do not combine an exemption and credit on the same income without a statutory basis.

### 4. Apply reserves and eligible losses in order

First establish the positive base and statutory reference amounts before the relevant reductions. Apply capitalisation reserve, then eligible loss offset, then any qualifying levelling-reserve movement. Keep the actual before-reserve reference base for the loss cap; it is not the reduced base after capitalisation (arts. 25–26, 30 and 105).

**Capitalisation reserve, art. 25.** For taxpayers at art. 29.1 or 29.6 rates, compute the qualifying increase in own funds from closing funds excluding the current result minus opening funds excluding the preceding result, then remove the statutory non-qualifying movements, including member contributions, debt capitalisations, specified restructuring/own-share movements, legal reserves, levelling/Canary reserves and the other art. 25.2 exclusions. Generally reduce by **20%** of that increase. The enhanced rates are **23%** where average headcount rises at least **2% without exceeding 5%**, **26.5%** where it is between **5% and 10%**, and **30%** above **10%**. The literal article overlaps at exactly **5%**. AEAT’s [2025 corporate manual, for periods beginning from 2025](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2025/principales-novedades-impuesto-sobre-sociedades-2025/reserva-capitalizacion.html), resolves its administrative table as **23% for ≥2% and <5%, 26.5% for ≥5% and ≤10%, and 30% above 10%**. Retain both the statutory wording and that published administrative interpretation; the manual is not a legislative correction. At an exact 5% claim, record this interpretation and the underlying headcount evidence rather than describing the statute as unambiguous.

Cap the reduction at **20%** of the positive statutory reference base, or **25%** where preceding-12-month net turnover is below **EUR 1m**. Hold the own-funds increase and separately identified unavailable reserve for **three years**, subject to statutory exceptions; hold enhanced headcount for the same period. Unused qualifying reduction carries into periods ending in the following **two years** subject to the cap. A breach triggers tax and interest under arts. 25.4 and 125.3. Source: [LIS art. 25](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a25).

**Losses, art. 26 and DA 15.** Carry eligible assessed/self-assessed losses forward without a fixed expiry. For an ordinary full-year period, offset the lower of available eligible losses, the remaining positive base and the greater of **EUR 1m** or the relevant **70%/50%/25%** reference-base amount. Prorate the EUR 1m amount for a short period. New-activity first-positive-period rules, qualifying creditor write-offs and extinction alter the percentage restriction; read the exact art. 26 exception, including restructuring exclusions. Acquisition anti-trafficking restrictions in art. 26.4 can deny losses entirely. The **ten-year** loss-checking period does not remove the taxpayer's later duty to substantiate a claimed loss with the specified return/accounts and deposit evidence (art. 26.5).

**Levelling reserve, art. 105.** For qualifying art. 101 entities applying the required art. 29.1 rate, reduce a positive base by up to **10%**, within the **EUR 1m** short-period-adjusted ceiling. The [AEAT instructions for 2025 and following periods](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html) expressly retain this computation for qualifying reduced-dimension entities. Book the unavailable reserve from profits as art. 105.3 requires. Add the reduction back against negative bases in periods ending within the following **five years**, and add any remainder in the period at that deadline. The same funds cannot support the levelling, capitalisation and Canary investment reserves simultaneously. Include the movement in art. 40.3 instalments. Breach requires the attributable gross tax increased by **5%**, plus interest (art. 105.6).

### 5. Compute gross tax, credits and the minimum

Apply the selected rate or micro bands to the resulting base. Negative tax is not generated by applying the ordinary rate to a loss. Art. 30 defines gross and net tax; apply the Chapter II/III double-tax credits and bonificaciones before Chapter IV credits, subject to their distinct caps.

| Credit | Basic amount and limits | Tax year | Official source |
|---|---|---|---|
| Research and development | 25% of qualifying spend up to the preceding-two-year average and 42% of the excess; additional 17% for qualifying exclusive researchers; 8% for qualifying exclusive investment excluding land/buildings | 2026 | [LIS art. 35.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a35) |
| Technological innovation | 12% of qualifying spend | 2026 | [LIS art. 35.2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a35) |
| Additional average disabled-worker employment | EUR 9,000 per person-year for disability at least 33% but below 65%; EUR 12,000 from 65% | 2026 | [LIS art. 38](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a38) |
| Spanish film/series production, specialist qualification required | 30% on the first EUR 1m credit base and 25% above; EUR 20m credit ceiling, EUR 10m per series episode; territory, certification, aid-intensity and other conditions apply | 2026 | [LIS art. 36.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a36) |
| Ordinary Chapter IV credit cap | 25% of gross tax after international double-tax credits and bonificaciones; 50% when current art. 35/36 credits exceed 10% of that reference amount | 2026 | [LIS art. 39.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a39) |
| Qualifying donations | 40%, or 50% for the qualifying repeated-donation history; credit base capped at 15% of period taxable base | 2026 | [Ley 49/2002 art. 20](https://www.boe.es/buscar/act.php?id=BOE-A-2002-25039#a20) |

R&D/innovation bases exclude the relevant grants and require project-level qualifying costs and the territorial/activity conditions in art. 35. A software maintenance expense is not automatically R&D. Ordinary Chapter IV unused credits carry **15 years**, art. 35 credits **18 years** (art. 39.1). The optional art. 39.2 R&D/innovation route discounts the credit by **20%** and requires its waiting period, staffing, reinvestment, evidence and monetary caps; do not claim an uncapped cash refund from the headline percentage. Donations' unused credit and excess credit base have **ten-year** carryforwards under Ley 49/2002 art. 20. Obtain the qualifying beneficiary and donation evidence before claiming.

Apply the domestic minimum only after testing its trigger and exclusions. It does not apply to art. 29.3–29.5 entities or the specified SOCIMI regime. The minimum base has its own levelling and Canary adjustments, and excludes the eligible ZEC part. Under [art. 30 bis.2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a3-3), apply the permitted bonificaciones, art. 38 bis and international double-tax credits first. If they take the amount below the nominal floor, that lower amount becomes the statutory minimum. Otherwise remaining credits cannot reduce tax below the minimum, subject to the express Canary exceptions. Carry unused credits under their own rules. **Do not simply take the greater of 15% of base and tax after every credit**: the statutory ordering and exceptions matter.

Finally deduct actual eligible withholding, payments on account and instalments under [LIS art. 41](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a41). An excess is refundable; the liability floor does not prevent repayment of overpaid instalments.

### 6. Preserve the territorial incentive tests

**Ceuta and Melilla.** For periods beginning from **1 January 2026** that **had not ended by 3 September 2026**, [RDL 22/2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-18429#a3) raises the qualifying art. 33 bonificación to **60%**. An earlier-ended 2026 short period retains the prior **50%** rule. The qualifying activity normally closes a commercial cycle in the territory; isolated movements do not suffice, and the article has express real-estate, wholesale, shipping/fishing and extended-operation rules.

Under the new art. 33.3 presumption, a fixed place of business supports **EUR 60,000 per full-time employee**, capped at **EUR 1.2m** at group level; the first **two periods beginning after its establishment** use **EUR 120,000** and **EUR 2.4m**. Prove the completed commercial cycle for relief on the excess. Before the amendment applies, the corresponding presumption is **EUR 50,000 per employee**, capped at **EUR 400,000**; do not backdate the new ceilings ([prior art. 33](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328&p=20260321&tn=1#a33)).

**ZEC and Canary incentives.** Keep them separate from ordinary micro/ERD computations. [Ley 19/1994 arts. 31, 43–44](https://www.boe.es/buscar/act.php?id=BOE-A-1994-15794#a31) requires registration and qualifying activity/residence/substance; its special rate is **4%** only on the eligible base. Investment in the first **two years** is ordinarily at least **EUR 100,000** in Gran Canaria/Tenerife or **EUR 50,000** in the listed other islands; qualifying employment is normally at least **five/three jobs**, created within **six months**, with maintenance conditions and statutory exceptions. The eligible base is the smaller of the territorial coefficient result and the employment cap: **EUR 1.8m**, plus **EUR 500,000** for each qualifying extra job within the stated **50-job** band, subject to the **30% net-turnover ceiling on the tax reduction**. Excess base is not automatically taxed at 4%, and listed-jurisdiction operations do not qualify. A specific ZEC computation requires the full coefficient, investment and staffing schedules. The distinct Canary investment reserve under art. 27 and specialised sector incentives are outside the ordinary examples.

## Deadlines and filing

| Obligation | Rule | Official source |
|---|---|---|
| Annual corporate return and payment | Modelo 200 for ordinary taxpayers; 25 calendar days following the six months after period end. A calendar-year 2026 period is returned in 2027 under this rule | [LIS arts. 124–125](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a124) |
| Form not yet approved when the statutory window opens | Art. 124.1 provides a 25-day window after the form rule enters into force, with an option to use the ordinary window under the preceding period's formal rules | [LIS art. 124.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a124) |
| Modelo 202 instalments | First 20 calendar days of April, October and December; non-working-day extensions apply | [LIS art. 40.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a40); [AEAT instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html) |
| Corporate withholding obligations | Pay over required withholding, submit prescribed returns/annual summary and give the payee a certificate | [LIS art. 128](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a128) |
| Related-party disclosures | Test Modelo 232 separately from documentation and corporate tax; use the [transfer-pricing Guide](spain-transfer-pricing.md) | [Orden HFP/816/2017 arts. 2–5](https://www.boe.es/buscar/doc.php?id=BOE-A-2017-10042) |

A dormant, loss-making or nil-tax company is not exempt from the annual return merely for that reason. Fully exempt art. 9.1 bodies do not file. An art. 9.3 partially exempt entity avoids filing only if **all** conditions hold: total annual income no more than **EUR 75,000**, non-exempt income no more than **EUR 2,000**, and all non-exempt income subject to withholding. Other art. 9.2–9.4 bodies declare exempt and non-exempt income as art. 124.3 requires. Consolidation requires its group return and separate regime; this Guide does not assemble Modelo 220.

**Modelo 202 method.** Under art. 40.2, take **18%** of the last period's gross tax whose declaration deadline had ended when the instalment window opened, less that period's applicable credits, bonificaciones and withholding. Apply the short-prior-period aggregation rule where needed. This is not 18% of current turnover or of the last return's balance payable after instalments.

Under art. 40.3, compute the current cumulative base for **3, 9 or 11 months** for a calendar-year taxpayer, then apply **floor(5/7 × annual rate expressed as a percentage)** below **EUR 10m** preceding-12-month turnover. From **EUR 10m**, DA 14 instead uses **ceil(19/20 × that rate)**. Apply separate relevant bands/rates for a multi-rate taxpayer, then eligible bonificaciones, withholding and prior current-period instalments according to the form. The method is compulsory where the relevant turnover **exceeds EUR 6m**; other taxpayers can elect through the census return in February for a calendar period, with the separate short/non-calendar-period election rules in art. 40.3. Exactly EUR 6m does not itself trigger that compulsory-method limb. Source: [LIS art. 40, DA 14](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a40); [AEAT instructions, sections B1/B2](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html).

For taxpayers within DA 14, also test the minimum instalment: generally **23%** of adjusted positive accounting profit for the cumulative period, **25%** for the specified art. 29.6 entities, less previous instalments only as that minimum calculation allows. Statutory exceptions and adjustments include qualifying debt write-offs/capitalisations, exempt or bonified income and Canary/ZEC items. For qualifying Ceuta/Melilla income, the normal DA 5.4 exclusion is **50%**, increased to **60%** for 2026-start periods' payment windows beginning from **3 September 2026**, under the new **DA 20** inserted by RDL 22/2026 art. 3. This instalment timing test is distinct from the annual art. 33 test above.

Modelo 202 is electronically filed even if nil when turnover exceeds **EUR 6m**. Other taxpayers generally do not file a nil instalment where the instructions' conditions hold; art. 29.4–29.5 entities and the specified all-resident-member AIE/UTE cases have exemptions. Do not assume that every incorporated entity must submit a nil Modelo 202. Annual 2026 return schemas, boxes and the 2027 filing calendar must be confirmed from their own publication; 2025-return forms are not relabelled as 2026 forms.

## Penalties and interest

| Event | Statutory amount or consequence | Tax year | Official source |
|---|---|---|---|
| Voluntary late tax return with amount due and no prior request, within the first 12 months | 1% plus 1% for each complete month late; no art. 27 penalty or pre-filing interest for that period | 2026 | [LGT art. 27.2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| That return after 12 months | 15% surcharge plus interest from the day after the 12-month period until filing | 2026 | [LGT art. 27.2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| Timely payment conditions satisfied | 25% reduction of the art. 27 surcharge, subject to all art. 27.5 requirements | 2026 | [LGT art. 27.5](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| Executive collection | 5% before enforcement-order notification; 10% when debt and reduced surcharge are paid within the specified enforcement window; otherwise 20% and applicable interest | 2026 | [LGT art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a28) |
| Culpable underpayment, after classification | Minor 50%; serious 50–100%; very serious 100–150% of the statutory unpaid-tax base | 2026 | [LGT art. 191](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a191) |
| Late ordinary return without economic loss | EUR 200; halved without a prior request, subject to the article's rules | 2026 | [LGT arts. 198.1–198.2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198) |
| Default interest | Apply the rate in force for each delay segment. AEAT records 4.0625% for 2026 under the continued budget until a replacement budget rate takes effect | 2026 | [LGT art. 26](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a26); [AEAT interest rule](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html) |

Determine whether there was a prior request, unpaid tax, a self-correction or an information-return offence before choosing a row. Late disclosure and TP documentation offences have their own regimes. Art. 191 classifications turn on concealment, false documents, accounting incidence, withheld amounts and fraudulent means; the maximum is not an automatic sanction for every mistake. Apply any eligible conformity/payment reductions under [LGT art. 188](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a188). A reserve or credit clawback also follows its specific tax-and-interest provision. Do not deduct non-deductible sanctions in the next corporate computation.

## Cross-border points

Resident-company worldwide income remains in scope even if the payer or bank is overseas (LIS art. 7.2). Apply the participation, foreign PE and foreign-tax-credit tests above to the actual income and country. Market-value pricing applies under art. 18 to both domestic and international related parties. Resident corporate withholding under art. 128 is not a universal rate for payments to foreign recipients; identify the non-resident domestic rule, treaty and exemption separately. Certain qualifying dividends and intra-tax-consolidation payments are exempt from withholding under art. 128.4; eligible Ceuta/Melilla urban rents halve the general 19% rate under art. 128.6.a.

[LIS art. 19.1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a19) includes market value less tax value of assets when a resident entity transfers residence abroad, except assets remaining attached to its Spanish permanent establishment. A qualifying EU/EEA destination with the required recovery-assistance arrangement permits an election for **five equal annual payments** in the final-period tax return; the first falls in its voluntary payment window and the remaining four carry interest. Test guarantees and the acceleration events in the article, including qualifying onward transfers, disposals, insolvency/liquidation and non-payment. Temporary transfers for the specified financing, security, prudential-capital or liquidity purposes have a return-within-**one-year** exception. A management move does not by itself prove cessation of Spanish residence under art. 8. Obtain the legal and treaty residence analysis before treating any move as triggering or avoiding the charge.

Foral allocation, permanent-establishment attribution, treaty limitation/anti-abuse, fiscal consolidation, hybrid mismatches, controlled foreign companies, reorganisations and the separate complementary minimum tax require their own fact-specific analysis. They are not resolved by inserting an assumed treaty rate in this ordinary computation.

## Two worked examples that recompute

### Example 1: ordinary reduced-dimension company

Assume a common-territory trading SL has a full calendar-year 2026 period, prior-year aggregated turnover EUR 2m, is not newly created or patrimonial, and is outside tax consolidation and the minimum-tax trigger. Its agreed taxable base is EUR 100,000 after all account adjustments; it claims no reserves, losses or credits. Under DT 44.2.b its tax is **EUR 23,000**. With EUR 1,000 eligible withholding and EUR 7,000 instalments, art. 41 leaves **EUR 15,000 payable**. These are hypothetical client facts, not figures claimed to be printed in the statute.

```oa-check
name: Ordinary Spanish ERD company for a 2026-start period
inputs:
  taxable_base: 100000
  applicable_rate: 0.23
  eligible_withholding: 1000
  instalments_paid: 7000
steps:
  gross_tax: taxable_base * applicable_rate
  balance_payable: gross_tax - eligible_withholding - instalments_paid
expected:
  gross_tax: 23000
  balance_payable: 15000
```

### Example 2: short-period microcompany band

Assume an established, eligible common-territory microcompany has a **181-day period beginning in 2026**, preceding-period aggregated turnover below EUR 1m, and EUR 120,000 taxable base after all adjustments. It is not newly created, patrimonial or in a special/group regime, and has no credits, reserves or prepayments. DT 44.2.a prorates the lower band: EUR 50,000 × 181/365 = **EUR 24,794.520547…**. Tax that part at 19% and the remaining **EUR 95,205.479452…** at 21%, giving **EUR 24,704.11** rounded to cents. Keeping a full EUR 50,000 lower band would understate tax. Retain calculation precision until the final monetary rounding.

```oa-check
name: Spanish microcompany with a 181 day 2026-start period
inputs:
  taxable_base: 120000
  full_year_band: 50000
  period_days: 181
  statutory_denominator: 365
  lower_rate: 0.19
  upper_rate: 0.21
steps:
  short_period_band: min(taxable_base, full_year_band * period_days / statutory_denominator)
  upper_band_base: max(0, taxable_base - short_period_band)
  tax: round(short_period_band * lower_rate + upper_band_base * upper_rate, 2)
expected:
  short_period_band: 24794.5205479452
  upper_band_base: 95205.4794520548
  tax: 24704.11
```

## Ask the client first

1. What are the exact accounting-period dates, incorporation/residence facts and common/foral territory, and did any move, cessation or transformation occur?
2. What are prior-period and preceding-12-month turnovers, the full control/ownership group, business activity, patrimonial tests and any newly created or special-regime status?
3. What accounts, tax reconciliations, asset schedules, finance costs, participation income, foreign taxes and related-party dealings support the base?
4. What losses, tax credits and reserve balances exist, with their source years, prior checks, ownership changes, eligible equity movements and headcount evidence?
5. Which instalment method/elections apply, what withholding and instalments were actually paid, and has AEAT issued any request or assessment?
6. Are there Ceuta/Melilla or Canary/ZEC activities, group returns or specialist reliefs, and what dates, substance, employment and investment evidence support them?

## Sources

[LIS art. 29.2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a29) and the [AEAT capitalisation-reserve table](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2025/principales-novedades-impuesto-sobre-sociedades-2025/reserva-capitalizacion.html) reread **2026-10-27** for the credit-cooperative rate and the exact 5% administrative interpretation.

| Official source | Provisions and use | Read on |
|---|---|---|
| [Ley 27/2014, current consolidated text](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328) | Arts. 5, 7–16, 18–22, 25–33, 35–41, 101–105, 124–128; DA 14–15; DT 44: scope, base, reliefs, rates, filings and exit charge | 2026-10-25 |
| [Ley 27/2014, BOE revision published 21 March 2026](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328&p=20260321&tn=1) | Prior art. 33 for periods outside the September amendment's temporal scope | 2026-10-25 |
| [RDL 22/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-18429) | Art. 3 and final entry-into-force rule: 2026 Ceuta/Melilla annual and instalment transitions, including new DA 20 | 2026-10-25 |
| [AEAT Modelo 202 instructions for 2025 and following periods](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html) | Current instalment methods, levelling reserve, nil filing and September 2026 update; the title expressly includes following periods | 2026-10-25 |
| [Ley 49/2002](https://www.boe.es/buscar/act.php?id=BOE-A-2002-25039) | Art. 20: corporate donation credit, repetition test, base cap and carryforward | 2026-10-25 |
| [Ley 19/1994](https://www.boe.es/buscar/act.php?id=BOE-A-1994-15794) | Arts. 31, 43–44: ZEC eligibility and rate/base limits; art. 27 routes the separate Canary reserve | 2026-10-25 |
| [Orden HFP/816/2017](https://www.boe.es/buscar/doc.php?id=BOE-A-2017-10042) | Arts. 2–5: Modelo 232 obligations, separate from the annual tax return | 2026-10-25 |
| [Ley 58/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Arts. 26–28, 188, 191, 198: interest, late/enforcement surcharges and penalties | 2026-10-25 |
| [AEAT interest calculation](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html) | Explicit 2026 continued-budget interest rate; the underlying annual return is for 2025 | 2026-10-25 |

Not yet confirmed: the specific foral surcharge/minimum and procedure questions recorded in [foral corporate Sources](es-foral-corporate-tax.md#sources); a legislative or binding resolution settling the art. 25 literal 5% overlap beyond AEAT’s now-cited administrative table; the final 2026 annual-return schema/calendar to be published for filing in 2027; full specialist-regime claims outside the ordinary computation. The reduced-rate minimum-tax rounding must be checked against the filing instructions applicable to the actual return. Independent whole-pack review is pending.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-28. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `es-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/es-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
