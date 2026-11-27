---
name: de-trade-tax
description: "German trade tax for collection period 2026: liability, financing add-backs, property reduction, losses, allowances, municipal multipliers, income-tax credit, apportionment, returns and payments. Specialist cases are explicitly referred. Trigger on Gewerbesteuer, Gewerbeertrag, Hebesatz, Steuermessbetrag, Hinzurechnung, Kürzung, § 35 EStG or Zerlegung."
version: 1.6
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Trade tax in Germany (Gewerbesteuer): collection period 2026

## Who this applies to

First obtain the activity, legal form, period, profit reconciliation, financing costs, business-owned property, determined losses, establishment municipalities, year-specific tax notices, general partnership profit shares and the owner's income-tax credit ceiling. Do not use a national multiplier for a particular business.

A standing commercial business is liable to the extent it operates through a German permanent establishment ([GewStG § 2(1)](https://www.gesetze-im-internet.de/gewstg/__2.html)). Under [EStG § 15(2)](https://www.gesetze-im-internet.de/estg/__15.html), commercial activity is independent, sustained, profit-seeking participation in the general market, excluding agriculture/forestry, a free profession and other self-employed work. A natural person's qualifying scientific, artistic, writing, teaching, educational, named or similar professional activity belongs under [§ 18](https://www.gesetze-im-internet.de/estg/__18.html). The named professions include doctors, dentists, vets, lawyers, notaries, patent attorneys, surveyors, engineers, architects, commercial chemists, auditors, tax advisers, consulting economists, sworn accountants, tax agents, Heilpraktiker, Dentisten, physiotherapists, journalists, photo reporters, interpreters, translators and maritime pilots (Lotsen); other self-employed categories include executors, asset managers and supervisory-board members. A job title, registration or earlier classification does not settle borderline IT/software work: **Check this point with one of our partner accountants.**

Capital companies (including GmbH, UG, AG, KGaA and SE), cooperatives and mutual insurance/pension-fund associations are commercial by legal form; an election under § 1a KStG treats the electing partnership as a company for trade tax ([GewStG § 2(2), (8)](https://www.gesetze-im-internet.de/gewstg/__2.html)). Other private-law legal persons and associations without legal personality are covered insofar as they run an economic business, excluding agriculture/forestry (§ 2(3)). Specific exemptions, solar businesses, travelling trade and home-worker relief: **Check this point with one of our partner accountants.**

The entrepreneur for whose account the business runs owes the tax; an ordinary commercial partnership is itself the debtor. EWIV members are instead joint debtors. On transfer of the whole business, the old entrepreneur owes it until transfer and the new one thereafter ([§ 5](https://www.gesetze-im-internet.de/gewstg/__5.html)). Activity-related temporary interruptions do not end liability ([§ 2(4)](https://www.gesetze-im-internet.de/gewstg/__2.html)).

Opening a commercial business is notified to the municipality, which informs the tax office; where real-tax assessment has not been delegated to municipalities, the tax office replaces the municipality; a free profession is notified to the tax office. Supply the further tax-registration information electronically within one month of the event; a hardship waiver on application permits the official paper format. Any statutory/ministerial small-activity notification exception needs checking ([AO § 138(1), (1b), (4)](https://www.gesetze-im-internet.de/ao_1977/__138.html)). Liability follows the statutory activity test, rather than the mere registration.

For mixed professional/commercial work, distinguish a sole trader from a partnership, separable from inseparable activities, own commercial receipts from commercial partnership income, and commercially structured partnerships. The partnership taint/de minimis rules and the 5 November 2025 decree are specialist questions: **Check this point with one of our partner accountants.** Do not infer an outcome from a small profit or a commercial loss. Tax groups, banks, insurers, shipping, audit reclassification and business disposal/closure: **Check this point with one of our partner accountants.**

## Rates, bands and thresholds

| Item | Rule for 2026 | Official source |
|---|---|---|
| Ordinary base calculation | Round trade income down to full EUR 100; natural persons and partnerships deduct EUR 24,500, limited to rounded income; capital companies have no such allowance | [GewStG § 11(1)](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Other specified bodies | EUR 5,000, limited to rounded trade income, only for the exact § 11(1) no. 2 categories | [GewStG § 11(1)](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Ordinary base rate | 3.5% after rounding and allowance | [GewStG § 11(2)](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Municipal multiplier floor | 200% for 2026; 280% first applies for 2027 | [BMF](https://www.bundesfinanzministerium.de/Content/DE/Glossareintraege/G/gewerbesteuer.html?view=renderHelp), [GewStG § 36(5b)](https://www.gesetze-im-internet.de/gewstg/__36.html) |
| Munich multiplier | 490% for the 2026 illustration; city series says “seit 1997: 490 Prozent”. Check the notice for the particular period | [City of Munich](https://stadt.muenchen.de/infos/hebesaetze-gewerbesteuer-grundsteuer.html) |

The municipality sets its own multiplier. The same multiplier applies to all its businesses, subject to the statutory boundary-change exception. A decision effective from the beginning of a year must be made by 30 June; a later decision cannot exceed the last level ([§ 16(1)–(4)](https://www.gesetze-im-internet.de/gewstg/__16.html)). Multiply each municipality's base share by its multiplier divided by 100. There is no unconditional net effective rate: the owner's credit also depends on both ceilings below.

## The taxable base

The collection period is the calendar year, shortened to the period of liability where necessary ([§ 14](https://www.gesetze-im-internet.de/gewstg/__14.html)). Start with the profit under income/corporation-tax rules, add § 8 amounts and subtract § 9 amounts ([§ 7](https://www.gesetze-im-internet.de/gewstg/__7.html)). Trade tax and its ancillary charges are not business expenses ([EStG § 4(5b)](https://www.gesetze-im-internet.de/estg/__4.html)). The profit computation belongs in `de-einkommensteuer-freelancer`, `germany-income-tax`, `de-partners-and-part-year` or `de-corporate-tax`; classification intake is in `de-freelance-intake`. Obtain the complete partnership profit reconciliation, including partners' remuneration; different financial years and disposals require a partner accountant before assigning the period or base.

**Financing add-back ([§ 8 no. 1](https://www.gesetze-im-internet.de/gewstg/__8.html)).** Only include items insofar as deducted in arriving at profit. Weight each item, sum the weighted amounts, subtract EUR 200,000 and add one quarter of the positive excess. At or below the allowance, the financing add-back is zero; other § 8 items still require checking.

- Debt remuneration: in full, including the specified non-ordinary early-payment discounts and receivable-discount amounts. Special receivable-sale arrangements: **Check this point with one of our partner accountants.**
- Annuities/permanent burdens: in full, excluding pensions from a direct employer pension promise; silent-partner profit shares: in full.
- Movable fixed assets owned by someone else: one fifth of rent/lease payments. Electric vehicles, qualifying externally chargeable hybrids and non-motor bicycles use half that share. For hybrids the conformity certificate must show at most 50 g CO2/km OR at least 80 km electric range. The halving applies only to contracts after 31 December 2019; for contracts before 1 January 2025, 60 km replaces 80 km, and the relief applies last in 2030 ([§ 36(4)](https://www.gesetze-im-internet.de/gewstg/__36.html)).
- Immovable fixed assets owned by someone else: one half of rent/lease payments.
- Time-limited rights: one quarter, excluding licences solely permitting derived rights to be passed to third parties and expenses forming the artists' social-levy base.

Other add-backs (KGaA partner shares, exempt dividends, partnership losses, corporate donations, dividend-related share write-downs and foreign taxes): **Check this point with one of our partner accountants.**

**Property reduction.** Deduct the Grundsteuer recorded as a business expense in the period for property in the entrepreneur's business assets ([§ 9 no. 1 sentence 1](https://www.gesetze-im-internet.de/gewstg/__9.html)). This rule first applies in 2025 ([§ 36(4b)](https://www.gesetze-im-internet.de/gewstg/__36.html)); do not use the old Einheitswert percentage for 2025/2026. Rented premises do not qualify under this rule. Extended property relief, including an election and limits on ancillary activities: **Check this point with one of our partner accountants.** Partnership-profit reductions, domestic/foreign dividends, participation thresholds/treaties and related costs: **Check this point with one of our partner accountants.** Donations, eligible recipients, excluded subscriptions and carry-forward: **Check this point with one of our partner accountants.**

**Trade losses ([§ 10a](https://www.gesetze-im-internet.de/gewstg/__10a.html)).** Previously unused determined trade losses reduce trade income up to EUR 1 million in full, then up to 60% of the excess. Only preceding-period losses enter this rule; do not import income-tax loss carry-back. The remaining loss is separately determined. For partnerships, both the loss and the EUR 1 million limit are allocated under the general profit-sharing keys, excluding advance profit shares; the deduction-year key applies to income and limit. Verify continuing partner/business identity before applying the examples. Whole-business transfers and changes of partners/shareholders, including §§ 8c/8d KStG: **Check this point with one of our partner accountants.**

**Apportionment ([§ 28](https://www.gesetze-im-internet.de/gewstg/__28.html)).** Several municipalities, an establishment spanning municipal boundaries, or an intra-year move require apportionment. The ordinary key uses establishment qualifying wages, rounded down to full EUR 1,000 ([§ 29](https://www.gesetze-im-internet.de/gewstg/__29.html)). Under [§ 31](https://www.gesetze-im-internet.de/gewstg/__31.html), start with employment remuneration, excluding other-law income-tax exemptions but including overtime/Sunday/holiday/night supplements regardless of their tax treatment. Exclude trainees' pay and profit-based one-off remuneration; cap each employee's other remuneration at EUR 50,000. In a partly exempt business exclude employees not exclusively or predominantly in the taxable business/part. A non-legal-person business adds EUR 25,000 annually in total for working entrepreneurs/partners. Energy/storage special keys, infrastructure exceptions, multi-municipality establishments and exceptional allocation: **Check this point with one of our partner accountants.**

**Income-tax credit ([EStG § 35](https://www.gesetze-im-internet.de/estg/__35.html)).** Eligible sole traders, individual commercial partners and KGaA general partners have a credit limited to the lowest of four times the matching base amount/share, trade tax actually payable attributable to that business/share, and the Ermäßigungshöchstbetrag. Compute that last ceiling from positive eligible commercial income divided by all positive income, multiplied by the reduced tariff tax. Eligible commercial income must be subject to trade tax and not excluded from § 35 elsewhere; reduced tariff tax reflects treaty reductions and the specified foreign-tax credits. Apply business-specific limits; never assume spare credit transfers between businesses or is refunded/carried forward.

For partners, use the general profit-sharing key excluding advance shares, with the share percentage rounded to two decimal places; base, tax and shares are separately/uniformly determined. Treaty allocation and multi-tier partnerships: **Check this point with one of our partner accountants.** The base/share and trade-tax notices are binding basis notices for the credit. Companies do not receive this income-tax credit.

The credit is disregarded for church-tax base purposes ([EStG § 51a(2)](https://www.gesetze-im-internet.de/estg/__51a.html)); obtain the applicable church/state rules rather than assuming a rate. For assessed solidarity surcharge, [SolzG § 3(1), (2)](https://www.gesetze-im-internet.de/solzg_1995/__3.html) uses assessed income tax with its child-allowance adjustment; [EStG § 2(6)](https://www.gesetze-im-internet.de/estg/__2.html) includes tax reductions. Thus § 35 can lower that base. Do not treat it as a separate direct surcharge credit or promise a cash reduction where no surcharge is due.

## Deadlines and filing

A liable business files when unrounded trade income exceeds EUR 24,500. Non-exempt capital companies, cooperatives and mutual insurance associations file irrespective of amount; any business with a preceding-period determined loss or a specific tax-office demand must file ([GewStDV § 25](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html)). For other private-law bodies/associations, public-law businesses and partly exempt bodies, the exact EUR 5,000/category tests in § 25(1) nos. 3–5 require separate review: **Check this point with one of our partner accountants.** A sole trader at/below EUR 24,500 has no ordinary return duty absent the loss/demand overrides. EUR 24,580 rounds to EUR 24,500 and gives no tax, but still triggers filing.

File the base-amount declaration electronically, plus an apportionment declaration when required. On application the authority may waive electronic transmission for undue hardship; the official paper form must then be signed by the debtor or AO § 34 representative ([§ 14a](https://www.gesetze-im-internet.de/gewstg/__14a.html)). Current-year ELSTER form identifiers, including historical GewSt 1 A/1 D and Anlage EMU claims: **Check this point with one of our partner accountants.** Do not infer an annex from financing costs alone.

The ordinary required 2026 return without an adviser is due seven months after year-end: 31 July 2027 is Saturday, so 2 August 2027. With a qualifying adviser, § 149(3) no. 3 sets 29 February 2028, subject to an earlier lawful demand or individual extension ([AO § 149](https://www.gesetze-im-internet.de/ao_1977/__149.html), [§ 108(3)](https://www.gesetze-im-internet.de/ao_1977/__108.html)). For 2025 the corresponding ordinary dates are 31 July 2026 and 1 March 2027. Check individual extensions before calling a return late; pandemic extensions concerned 2020–2024.

Prepayments fall on 15 February, 15 May, 15 August and 15 November; apply weekend/local statutory-holiday rollover. Ordinarily each is one quarter of the last assessed tax, rounded down to whole euros and set only if that single payment is at least EUR 50 ([§ 19(1), (2), (5)](https://www.gesetze-im-internet.de/gewstg/__19.html)). Different financial years follow § 19(1) sentences 2–3, not an assumed calendar-year cash schedule. The municipality can adjust expected tax through the fifteenth month after the period; an increase is due within one month of notification. An expected base fixed by the tax office binds the municipality; new businesses follow the same expected-tax method (§ 19(3)–(4)).

Credit prepayments at settlement. The balance is due one month after notification, except the portion matching already-due unpaid prepayments is due immediately. An excess is set off/refunded after notification ([§ 20](https://www.gesetze-im-internet.de/gewstg/__20.html)). Liability/base objections concern the tax-office base notice ([AO § 184](https://www.gesetze-im-internet.de/ao_1977/__184.html)); municipal multiplier/collection questions concern its own notice.

## Penalties and interest

For base/apportionment declarations, [AO § 152(6)](https://www.gesetze-im-internet.de/ao_1977/__152.html) provides EUR 25 per started month, maximum EUR 25,000 (§ 152(10)). Before mandatory assessment, § 152(1) is discretionary and excuses credible excusable delay. Under § 152(2), mandatory assessment normally follows failure to file within 14 months after year-end or by the earlier-demand date, subject to extended-deadline § 152(3) no. 1. The nil-tax/prepayment-covered exceptions are not imported by § 152(6). If applicable, three months and five days late gives four started months × EUR 25 = EUR 100. Initial unexpected demands, nonfiling, changes and special periods require individual review: **Check this point with one of our partner accountants.**

Late payment is 1% per started month of overdue assessed/declared tax rounded down to a multiple of EUR 50; no late-payment surcharge on ancillary charges. The three-day grace excludes AO § 224(2) no. 1 payment methods (including cash/cheques handed or sent to the authority); a bank transfer counts when credited ([AO § 240](https://www.gesetze-im-internet.de/ao_1977/__240.html), [§ 224](https://www.gesetze-im-internet.de/ao_1977/__224.html)). If a surcharge applies, EUR 1,234.56 rounds to EUR 1,200, giving EUR 12 per started month.

Assessment-difference interest, its 0.15% monthly rule, commencement, full-month/rounding rules, refunds, amendments and payments made before assessment: **Check this point with one of our partner accountants.** Do not use the old bare rate/start date as a complete calculation.

## Cross-border points

Foreign management/German establishments, no-treaty reciprocity exemptions, foreign permanent-establishment reductions, CFC/passive-establishment inclusions, foreign dividends and foreign taxes: **Check this point with one of our partner accountants.** Obtain the treaty, establishment and ownership facts; no automatic exemption or 15% safe harbour is given here. Owner emigration routes to `leaving-germany-exit-tax`/`de-non-resident-tax`; company income tax to `de-corporate-tax`.

## Worked examples

These are conditional 2026 computations, not actual assessments. Assume no unlisted adjustments, ordinary eligibility and continuous business/partner loss identity. Credits additionally require the stated positive-income ceiling; prepayments remain subject to notices/adjustments.

**Example 1: sole trader in Munich, ordinary costs.** Keep profit EUR 80,000, interest EUR 12,000, shop rent EUR 36,000 and petrol-car lease EUR 10,000. Financing sum = 12,000 + 18,000 + 2,000 = EUR 32,000, so add-back zero. After EUR 24,500 allowance: EUR 55,500; base EUR 1,942.50; Munich 490% gives EUR 9,518.25. Assuming Ermäßigungshöchstbetrag at least EUR 7,770, credit EUR 7,770 and unoffset tax EUR 1,748.25; this is not a deductible trade-tax expense. Ordinary next prepayment EUR 2,379. Sources: [§ 8](https://www.gesetze-im-internet.de/gewstg/__8.html), [§ 11](https://www.gesetze-im-internet.de/gewstg/__11.html), [§ 19](https://www.gesetze-im-internet.de/gewstg/__19.html), [EStG § 35](https://www.gesetze-im-internet.de/estg/__35.html), [Munich](https://stadt.muenchen.de/infos/hebesaetze-gewerbesteuer-grundsteuer.html).

```oa-check
name: Sole trader in Munich, profit EUR 80,000 (2026)
inputs:
  profit: 80000
  interest: 12000
  shop_rent: 36000
  car_lease: 10000
  allowance: 24500
  multiplier: 490
  income_tax_ceiling: 7770
steps:
  - financing_sum: interest + shop_rent / 2 + car_lease / 5
  - add_back: max(financing_sum - 200000, 0) / 4
  - trade_income: profit + add_back
  - rounded: floor(trade_income / 100) * 100
  - taxable: max(rounded - allowance, 0)
  - base_amount: taxable * 0.035
  - trade_tax: base_amount * multiplier / 100
  - credit: min(4 * base_amount, trade_tax, income_tax_ceiling)
  - not_offset: trade_tax - credit
  - prepayment: floor(trade_tax / 4)
expected:
  financing_sum: 32000
  add_back: 0
  base_amount: 1942.50
  trade_tax: 9518.25
  credit: 7770.00
  not_offset: 1748.25
  prepayment: 2379
```

**Example 2: KG, two equal partners.** Keep profit EUR 1,400,000, interest EUR 180,000, warehouse rent EUR 120,000, eligible expensed Grundsteuer EUR 6,000 and determined losses EUR 2,000,000. Assume both partners are eligible individuals with equal general shares, unchanged loss entitlements and no special remuneration/other adjustments. Financing sum EUR 240,000 gives add-back EUR 10,000; pre-loss income EUR 1,404,000. Loss use EUR 1,242,400 leaves income EUR 161,600 and loss EUR 757,600. After allowance: EUR 137,100; base EUR 4,798.50. The original 410% is retained as a hypothetical municipal multiplier, not a national average or a verified town rate: tax EUR 19,673.85. Each partner's base share EUR 2,399.25 gives fourfold limit EUR 9,597, still subject to that partner's payable-tax share and positive-income ceiling. Sources: [§ 8](https://www.gesetze-im-internet.de/gewstg/__8.html), [§ 9 no. 1](https://www.gesetze-im-internet.de/gewstg/__9.html), [§ 10a](https://www.gesetze-im-internet.de/gewstg/__10a.html), [§ 11](https://www.gesetze-im-internet.de/gewstg/__11.html), [EStG § 35](https://www.gesetze-im-internet.de/estg/__35.html).

```oa-check
name: KG with add-back, Grundsteuer and loss carry-forward (2026)
inputs:
  profit: 1400000
  interest: 180000
  warehouse_rent: 120000
  grundsteuer: 6000
  losses_bf: 2000000
  allowance: 24500
  multiplier: 410
  partner_share: 0.5
steps:
  - financing_sum: interest + warehouse_rent / 2
  - add_back: max(financing_sum - 200000, 0) / 4
  - before_losses: profit + add_back - grundsteuer
  - loss_limit: min(before_losses, 1000000) + max(before_losses - 1000000, 0) * 0.6
  - loss_used: min(losses_bf, loss_limit)
  - trade_income: before_losses - loss_used
  - loss_cf: losses_bf - loss_used
  - rounded: floor(trade_income / 100) * 100
  - base_amount: max(rounded - allowance, 0) * 0.035
  - trade_tax: base_amount * multiplier / 100
  - partner_credit_cap: 4 * base_amount * partner_share
expected:
  add_back: 10000
  before_losses: 1404000
  loss_used: 1242400
  loss_cf: 757600
  base_amount: 4798.50
  trade_tax: 19673.85
  partner_credit_cap: 9597.00
```

**Preserved historical cases.** Original years/inputs below are retained as historical scenario data, not current municipal rate statements. The seven original tests appeared in the 2025 Guide and were repeated in later 2026 versions; retain that distinction when using them. Where no case year was specified, none is invented. Apply the rules above only after proving eligibility and the actual period's notice.

- Original 2025 city list: Berlin 410%, Munich 490%, Hamburg 470%, Frankfurt 460%, Cologne 475%, Düsseldorf 440%, Stuttgart 420%, Leipzig 460%, Dresden 450%, Monheim am Rhein 250%. These historic supplied figures are not a usable rate card; the “lowest major rate” claim is withdrawn. **Check this point with one of our partner accountants.**
- Berlin profit EUR 80,000 with no adjustments and supplied 410%: base EUR 1,942.50, model tax EUR 7,964.25, credit at most EUR 7,770, residual at least EUR 194.25. The former 0.24% description does not measure income above the allowance; 194.25 / 55,500 = 0.35%, still only a conditional model.
- Hamburg profit EUR 20,000/supplied 470%: ordinary natural-person base zero. Monheim profit EUR 60,000/supplied 250% and sufficient ceiling: base EUR 1,242.50, model tax EUR 3,106.25; fourfold amount EUR 4,970 is capped to EUR 3,106.25, not an actual EUR 4,970 credit. Munich profit EUR 100,000/supplied 490%: base EUR 2,642.50, tax EUR 12,948.25, credit at most EUR 10,570, residual at least EUR 2,378.25.
- Berlin taxable trade income after allowance EUR 10,000/supplied 410% and stipulated § 35 ceiling EUR 1,200: base EUR 350, model tax EUR 1,435, credit min(1,400, 1,435, 1,200) = EUR 1,200; residual EUR 235.
- Ordinary sole trader profit EUR 18,000, no adjustments: base zero; a prior loss determination or demand can still require filing. Architect working alone, profit EUR 90,000: professional status must be established; earlier registration alone is not proof. Adding building-material sales EUR 5,000 out of EUR 100,000 gives 5% receipts, not an automatic partnership-taint test for a sole trader. **Check this point with one of our partner accountants.**
- Low-multiplier income EUR 30,000, supplied 200%, stated “marginal ESt” EUR 3,000: base EUR 192.50; model tax EUR 385; fourfold EUR 770; credit at most EUR 385. Marginal tax is not proof of the statutory ceiling. Earlier same-business floor case: base EUR 1,942.50 × 200% = EUR 3,885; credit at most EUR 3,885; ordinary quarterly amount EUR 971. Both are 2026 floor scenarios, not the 2027 floor.
- Partnership pre-loss income EUR 1,500,000 and losses EUR 2,000,000: conditional loss use EUR 1,300,000, income left EUR 200,000, loss left EUR 700,000, base EUR 6,142.50. Earlier interest EUR 180,000/rent EUR 120,000 example gives weighted EUR 240,000 and add-back EUR 10,000. Interest-only EUR 50,000 gives zero financing add-back if there are no other items; old EUR 50,000/EUR 150,000 review triggers were workflow heuristics, not statutory thresholds.
- Prior assessed tax EUR 6,000 gives ordinary EUR 1,500 quarterly prepayments. Paid EUR 8,000 versus actual tax EUR 3,000 gives EUR 5,000 available for set-off/refund after notification; finality is not a condition in § 20(3).
- Ordinary corporation with A employee EUR 100,000 and B employee EUR 50,000, no exclusions/other adjustments: qualifying wages EUR 50,000 each; base EUR 1,000 splits EUR 500 each. June move Munich/supplied 490% to Leipzig/supplied 460%, including a sole trader without employees: no year-end municipality shortcut. **Check this point with one of our partner accountants.**
- Original three-year IT-consultant reclassification, forgotten tax registration and church-member questions remain specialist inputs; no retrospective amendment or surcharge result is assumed. Original separable-partnership receipt checkpoints EUR 500,000/EUR 15,000/EUR 15,000.01 and EUR 1,000,000/EUR 24,500/EUR 24,500.01, including loss-making branches, remain non-usable classification cases. Arithmetic: 3% × 500,000 = 15,000 and 3% × 1,000,000 = 30,000. **Check this point with one of our partner accountants.**

## Ask the client first

Collect the inputs listed at the start from existing records before asking for gaps. Obtain complete financing contracts, municipal notices with year and establishment history, property-expense proof, loss determinations and partnership allocations, and income-tax ceiling calculations. For wages obtain employee-by-employee pay, exemptions, supplements, training status and profit bonuses. Reconcile prepayments and tax notices; refer held cases before using their outcome.

## Sources

Completed exact operative reads are reused only where the same rule and period apply. New reads below cover the identified provisions, not every provision in the full code. Historical scenario figures and arithmetic are not source verification of municipal rates.

| Source and read scope | Official URL | Read on |
|---|---|---|
| GewStG §§ 2, 5, 7, 8, 10a, 11, 14, 14a, 16, 19, 20, 28, 29, 31, 36: full displayed sections read; § 9 no. 1 and its alternatives/conditions read | https://www.gesetze-im-internet.de/gewstg/ | 2026-11-27 |
| GewStDV § 25: all filing categories and overrides | https://www.gesetze-im-internet.de/gewstdv_1955/__25.html | 2026-11-27 |
| EStG § 35: full credit, ceilings, allocation and basis notices | https://www.gesetze-im-internet.de/estg/__35.html | 2026-11-27 |
| EStG § 15(2), § 18(1) and AO § 138(1), (1b), (4): reused completed freelance-intake operative reads | https://www.gesetze-im-internet.de/estg/__15.html | 2026-11-26 |
| EStG § 4(5b): reused completed exact prohibition | https://www.gesetze-im-internet.de/estg/__4.html | 2026-10-29 |
| AO §§ 149(2)–(4), 108(3) and EGAO Art. 97 § 36 opening: reused freelance-intake deadlines/rollover/pandemic-scope reads | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-11-26 |
| AO §§ 152, 240, 224, 184: displayed surcharge/payment/basis-notice conditions | https://www.gesetze-im-internet.de/ao_1977/ | 2026-11-27 |
| EStG § 51a(2), § 2(6); SolzG § 3(1)–(2): church and assessed-surcharge base clauses | https://www.gesetze-im-internet.de/estg/__51a.html | 2026-11-27 |
| BMF Gewerbesteuer: complete short entry, dated floor transition | https://www.bundesfinanzministerium.de/Content/DE/Glossareintraege/G/gewerbesteuer.html?view=renderHelp | 2026-11-27 |
| Munich: Gewerbesteuer series “seit 1997: 490 Prozent”, separate from Grundsteuer | https://stadt.muenchen.de/infos/hebesaetze-gewerbesteuer-grundsteuer.html | 2026-11-27 |

Not yet confirmed: specialist topics expressly held above; historical municipal figures other than the retained Munich series are supplied case inputs only. Current 2026 ELSTER form identifiers/annex routing are not established here. Check this point with one of our partner accountants.
