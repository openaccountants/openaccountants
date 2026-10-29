---
name: de-income-tax
description: "Use this skill to turn a German self-employed person's year of bank transactions into profit (Anlage EÜR) and the 2026 income tax, for a Freiberufler (Anlage S) or a sole trader (Anlage G) resident in Germany. Tax year 2026, filed in 2027. Covers sorting receipts and costs, the § 4(5) EStG limits (entertainment 70%, gifts EUR 50, home office EUR 6 a day up to EUR 1,260), cars, low-value assets (EUR 800), depreciation, § 7g, the § 19 UStG small-business limits (EUR 25,000 / 100,000), the 2026 tariff, solidarity surcharge, church tax, the § 35 trade tax credit, prepayments, deadlines and penalties. Trigger on: Einkommensteuer Selbständige, Anlage EÜR, Betriebsausgaben, Bewirtung, Arbeitszimmer, GWG, Vorauszahlungen, Gewerbesteuer Anrechnung, Freiberufler tax. Out of scope: employees (de-employee-income-tax), non-residents (de-non-resident-tax), trade tax computation (de-trade-tax), companies (de-corporate-tax), partnerships."
version: 2.5
jurisdiction: DE
tax_year: 2026
tier: 2
last_updated: 2026-10-29
category: international
depends_on:
  - income-tax-workflow-base
verified_by: pending
---

# Germany: income tax for the self-employed, from bank statement to tax, tax year 2026

This skill takes one self-employed person's business transactions for 2026, sorts them into the cash-basis profit statement (Einnahmen-Überschuss-Rechnung, EÜR), and works out the income tax, solidarity surcharge and church tax. It is for the 2026 return, filed in 2027.

See also, and do not repeat here:

- **de-einkommensteuer-freelancer**: the full method for Freiberufler and traders (EÜR or books, losses, the 30% and 25% flat expense rates for writers and teachers, 2025 figures for returns filed now).
- **de-trade-tax**: trade tax (Gewerbesteuer), add-backs, the municipal multiplier.
- **de-estimated-tax**: planning prepayments.
- **de-employee-income-tax**: wages, Werbungskosten, child allowances against Kindergeld, extraordinary burdens.
- **de-non-resident-tax**: a person who does not live in Germany but has German business income.
- **de-social-contributions**: contribution rates for the self-employed.
- **germany-bookkeeping** and **germany-vat-return**: records, asset pools and VAT returns.

## Who this applies to

- **In scope.** An individual with a residence or habitual abode in Germany, taxed on worldwide income (§ 1(1) EStG), who earns profit from self-employed work (§ 18 EStG, Anlage S) or a trade (§ 15 EStG, Anlage G), and works out profit by the cash method (§ 4(3) EStG). Single or jointly assessed with a spouse.
- **Freiberufler or trade.** Only a trade pays trade tax and gets the § 35 credit. The named professions in § 18(1) no. 1 EStG (doctors, lawyers, engineers, architects, tax advisers, journalists, translators and similar) and scientific, artistic, writing and teaching work are Freiberufler. Everything else run for profit is a trade (§ 15(2) EStG). Unclear cases: refer (see de-einkommensteuer-freelancer).
- **Cash method or books.** A trader must keep books once the tax office gives notice after turnover over EUR 800,000 or trade profit over EUR 80,000 in a year (§ 141 AO). A Freiberufler can always use the cash method. Books are out of scope here.
- **Who must file.** Without wages, anyone whose total income is above the basic allowance (twice it for spouses) (§ 56 EStDV). With business income the return and the EÜR must be sent electronically (§ 25(4) EStG, § 60(4) EStDV).
- **Out of scope.** Companies (GmbH, UG): de-corporate-tax. Partnerships (GbR, OHG, KG, PartG), whose profit is fixed at partnership level. Non-residents with German business income: de-non-resident-tax. Selling or closing the business, extraordinary income (§ 34 EStG), retained profits (§ 34a EStG), foreign income and treaties.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tariff zone 1, basic allowance (Grundfreibetrag) | Taxable income EUR 0 to 12,348: no tax | 2026 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Tariff zone 2 | EUR 12,349 to 17,799: (914.51 × y + 1,400) × y, y = (x − 12,348) / 10,000 | 2026 | Same |
| Tariff zone 3 | EUR 17,800 to 69,878: (173.10 × z + 2,397) × z + 1,034.87, z = (x − 17,799) / 10,000 | 2026 | Same |
| Tariff zone 4 (42%) | EUR 69,879 to 277,825: 0.42 × x − 11,135.63 | 2026 | Same |
| Tariff zone 5 (45%) | From EUR 277,826: 0.45 × x − 19,470.38 | 2026 | Same |
| Rounding | Taxable income x and the tax are both rounded down to whole euros | 2026 | Same, § 32a(1) sentences 1 and 6 |
| Splitting (joint assessment) | Twice the tax on half the joint taxable income | 2026 | Same, § 32a(5) |
| Solidarity surcharge | 5.5% of income tax; nothing while the tax is at most EUR 20,350 (EUR 40,700 under splitting); above that, at most 11.9% of the excess | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__3.html and https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Church tax (members only) | 8% or 9% of income tax, by state; base ignores the § 35 credit | 2026 | https://www.gesetze-im-internet.de/estg/__51a.html; BMF booklet "Steuern von A bis Z" (Stand January 2025): "je nach Bundesland 8 oder 9 Prozent" |
| Trade tax credit (§ 35) | 4.0 × trade tax base amount (Messbetrag), capped at the tax on trade income and at the trade tax actually payable | 2026 | https://www.gesetze-im-internet.de/estg/__35.html |
| Trade tax allowance, base rate | EUR 24,500 off trade income (rounded down to EUR 100); base rate 3.5% | 2026 | https://www.gesetze-im-internet.de/gewstg/__11.html |
| Trade tax multiplier floor | 200% for 2026; 280% from 2027 | 2026 | Law of 29 June 2026 (BGBl. 2026 I Nr. 197), Art. 8: in § 16(4) sentence 2 GewStG "wird die Angabe „200“ durch die Angabe „280“ ersetzt", first applied for 2027 (https://www.gesetze-im-internet.de/gewstg/__36.html, § 36(5b)). The § 16 page already shows only the 2027 wording |
| Trade tax itself | Not a business expense | 2026 | https://www.gesetze-im-internet.de/estg/__4.html (§ 4(5b)) |
| Small business (Kleinunternehmer) | Prior-year turnover not over EUR 25,000 and current-year turnover not over EUR 100,000 | 2026 | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Business entertainment (Bewirtung) | 70% deductible, with a proper receipt | 2026 | https://www.gesetze-im-internet.de/estg/__4.html (§ 4(5) no. 2) |
| Gifts to non-employees | Deductible only if the year's gifts to one person cost at most EUR 50 | 2026 | Same, § 4(5) no. 1 |
| Home office day rate (Tagespauschale) | EUR 6 per day worked mainly at home without going to an outside place of work, max EUR 1,260 a year | 2026 | Same, § 4(5) no. 6c |
| Home office room that is the centre of all work | Actual cost, or EUR 1,260 a year flat (one twelfth less per month not met) | 2026 | Same, § 4(5) no. 6b |
| Home to own premises | EUR 0.38 per full km one way, per day; cap EUR 4,500 unless a car is used | 2026 | https://www.gesetze-im-internet.de/estg/__9.html (§ 9(1) sentence 3 no. 4), applied by § 4(5) no. 6 EStG |
| Meals on business trips | EUR 28 for a full day away; EUR 14 for arrival, departure, or more than 8 hours away | 2026 | Same, § 9(4a), applied by § 4(5) no. 5 EStG |
| Business trips in a private car | EUR 0.30 per km, or the actual cost share | 2026 | BMF, 2026 Anlage EÜR instructions, line 72 (URL in Sources) |
| Business car, private use | 1% of list price per month, only if business use is over 50% | 2026 | https://www.gesetze-im-internet.de/estg/__6.html (§ 6(1) no. 4) |
| Low-value asset (GWG) | Expensed at once if cost reduced by contained input VAT for the eligibility test is at most EUR 800; the expense includes irrecoverable VAT; register if over EUR 250 | 2026 | Same, § 6(2) |
| Pool (Sammelposten), instead | Assets over EUR 250 up to EUR 1,000, one fifth a year over five years | 2026 | Same, § 6(2a) |
| Computer hardware and software | Useful life of one year may be taken: full cost in the year bought, still listed on Anlage AVEÜR | 2026 | BMF, 2026 Anlage EÜR instructions, line 34, citing the BMF letter of 22 February 2022 |
| Declining balance | Movable assets bought 1 July 2025 to 31 December 2027: up to 3 × straight-line rate, max 30% | 2026 | https://www.gesetze-im-internet.de/estg/__7.html (§ 7(2)) |
| Electric vehicles bought 1 July 2025 to 31 December 2027 | 75% in the year bought, then 10%, 5%, 5%, 3%, 2% | 2026 | Same, § 7(2a) |
| Investment deduction (§ 7g) | Up to 50% of expected cost; profit calculated without investment deductions or § 7g(2) add-backs not over EUR 200,000; open deductions per business not over EUR 200,000 | 2026 | https://www.gesetze-im-internet.de/estg/__7g.html |
| § 7g special depreciation | Up to 40% in total over the year bought and the four after | 2026 | Same, § 7g(5) |
| Pension contributions | 100% within a cap of EUR 30,826 (EUR 61,652 joint) | 2026 | https://www.gesetze-im-internet.de/estg/__10.html (§ 10(3)); ceiling https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html |
| Health, care and other insurance | Cap EUR 2,800 (EUR 1,900 with tax-free help towards cover, such as the Künstlersozialkasse); basic health and care cover always in full; statutory health with sick pay cut by 4% | 2026 | Same, § 10(1) no. 3 and § 10(4) |
| Special expenses lump sum | EUR 36 (EUR 72 joint) | 2026 | https://www.gesetze-im-internet.de/estg/__10c.html |
| Prepayments | 10 March, 10 June, 10 September, 10 December; set only if at least EUR 400 a year and EUR 100 a date | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |

## The taxable base

**Step 1: profit (Anlage EÜR).** Receipts when received, costs when paid (§ 11 EStG). Regular payments made shortly before or after the year end count in the year they belong to.

| On the bank statement | Treatment |
|---|---|
| Client payments, fees (Honorar), platform payouts (Stripe, PayPal) | Receipts. Normal VAT scheme: the VAT collected is also a receipt and VAT paid to the tax office an expense. Kleinunternehmer: the gross amount |
| Rent for business premises, office supplies, software, advertising, bank fees, adviser fees, chamber dues, business liability insurance | Expense in full |
| Restaurant with a client (Bewirtung) | 70% of the reasonable cost. Needs a receipt naming place, date, guests and reason, with the till receipt. Input VAT is still fully deductible |
| Gifts to clients | In full if the year's gifts to that person cost EUR 50 or less; above that, nothing at all. Record each recipient |
| Rent of the home, home office | Day rate EUR 6 per day worked mainly at home, max EUR 1,260. Room costs only if the room is the centre of all work |
| Fuel, car costs | Depends on the car method; see below. No method confirmed: deduct nothing yet |
| Laptop, phone, furniture | Over EUR 800 net: depreciate (computers and software: one year allowed). EUR 800 or less: expense now or pool |
| Health, care, pension insurance (Krankenkasse, DRV, KSK) | Not a business expense. Special expense in Step 2 |
| Income tax, surcharge, church tax, prepayments | Never a business expense (§ 12 no. 3 EStG). Church tax paid is a special expense in Step 2 (§ 10(1) no. 4 EStG) |
| Trade tax (Gewerbesteuer) | Never deductible (§ 4(5b) EStG). Records that call it an expense are wrong for any year since 2008 |
| Fines from a court or authority | Not deductible (§ 4(5) no. 8 EStG) |
| Transfers between own accounts, loan principal, private withdrawals | Leave out of ordinary cash receipts/expenses, but record withdrawals and deposits separately. Business-loan interest is subject to § 4(4a) EStG, also under EÜR: overwithdrawals are withdrawals exceeding profit plus deposits. The statutory add-back is 6% of current plus prior overwithdrawals less prior underwithdrawals, capped at the year's interest less EUR 2,050. Profit for this test excludes the add-back itself. Interest on fixed-asset acquisition/production loans is unaffected. The complete multi-year balance and mixed-debt allocation method is not set out here |
| Wages, rent received, interest, dividends | Not business income. Other forms (Anlage N, V, KAP) |
| Cash withdrawals | Ask what the cash paid for. Default: leave out |

**Cars.** A car used more than 50% for business can be a business asset: all costs are expenses and private use is added back at 1% of the gross list price per month (§ 6(1) no. 4 EStG), or by logbook. A private car used for business trips: EUR 0.30 per km or the actual cost share. Trips from home to the own office count only at EUR 0.38 per km one way. Electric and hybrid cars have special rules: refer.

**Phone and internet.** Deduct the business share shown by records. The employee flat rate from the wage tax guidelines is not a rule for the self-employed.

**Mixed and unknown items.** Default to no deduction until the client confirms the business share.

**Step 2: from profit to taxable income** (§ 2 EStG). Profit plus any other income = total income. Less special expenses: pension contributions within the cap; basic health and care cover in full; other insurance only if the cap has room; church tax paid, donations, or the EUR 36 lump sum. Less extraordinary burdens and child allowances (see de-employee-income-tax). Round down to whole euros.

**Step 3: tax.** Apply the tariff (or splitting). For a trader, subtract the § 35 credit: the lowest of 4.0 × Messbetrag, the tax that falls on trade income (positive trade income / all positive income × tariff tax), and the trade tax actually payable. Unused credit is lost. Then the surcharge on the tax after the credit, and church tax on the tax before the credit (§ 51a(2) EStG). Subtract prepayments paid.

**Losses.** A loss offsets other income of the same year, then can be carried back, subject to the statutory cap, to the immediately preceding year and any remainder to the second preceding year, or forward without time limit (§ 10d EStG; see de-einkommensteuer-freelancer).

## Deadlines and filing

| Step | Rule |
|---|---|
| Register the business | Within one month of starting (§ 138 AO): a trade with the municipality, a Freiberufler with the tax office online |
| Forms | Main form, Anlage S or G, Anlage EÜR with Anlage AVEÜR (one set per business), Anlage Vorsorgeaufwand, Anlage Sonderausgaben. Electronic, through ELSTER (§ 25(4) EStG, § 60(4) EStDV) |
| Own return | Seven months after year end (§ 149(2) AO): 31 July 2027 is a Saturday, so Monday 2 August 2027 (§ 108(3) AO) |
| Prepared by a tax adviser | Last day of February of the second year after (§ 149(3) AO): Tuesday 29 February 2028. The office can call for an earlier return with four months' notice (§ 149(4) AO) |
| Balance due | One month after the notice (§ 36(4) EStG) |
| Prepayments | 10 March, 10 June, 10 September, 10 December, set by notice from the last assessed tax. The office can adjust them until 15 months after year end; a rise after year end is due one month after the notice and only if at least EUR 5,000 (§ 37(3) to (5) EStG) |

## Penalties and interest

- **Late-filing surcharge (§ 152 AO).** May be set for any late return. Must be set if the return is not in within 14 months after year end (for 2026: after 29 February 2028), unless the deadline was extended, the tax is nil, or the tax is not more than prepayments and tax withheld. Amount: 0.25% per started month of the tax less prepayments and tax withheld, at least EUR 25 per started month, at most EUR 25,000, rounded down to euros (§ 152(5) and (10) AO).
- **Interest (§ 233a AO).** From 15 months after year end (1 April 2028 for 2026) until the notice: 0.15% per full month, 1.8% a year (§ 238(1a) AO), on the balance rounded down to EUR 50. Refunds earn the same.
- **Late payment (§ 240 AO).** 1% per started month on the overdue amount rounded down to EUR 50. Applies to late prepayments too.
- **Wrong returns.** Tax evasion is a crime (§ 370 AO). Reckless understatement is an administrative offence with a fine of up to EUR 50,000 (§ 378 AO). Either case: refer.

## Cross-border points

- **Non-residents.** A person without a German home or habitual abode is taxed only on German income, including profit from a German permanent establishment or self-employed work done in Germany (§ 49 EStG). Use de-non-resident-tax.
- **Foreign clients.** Fees from foreign clients for work done in Germany by a resident are German income in full. VAT on cross-border services: germany-vat-return.
- **Foreign tax, foreign establishment, moving in or out.** Foreign tax credits are in de-non-resident-tax (§ 34c EStG). If a treaty exempts profit of a foreign establishment, test progression separately under § 32b EStG, including its statutory exceptions; exemption does not itself establish progression. Refer for that treaty and progression assessment. Departure with shares: leaving-germany-exit-tax.
- **§ 7g abroad.** The investment deduction needs the asset used in a German establishment (§ 7g(1) EStG).

## Worked examples

### Example 1: Freiberufler designer, single, normal VAT scheme

Anna is a self-employed designer in Hamburg, single, no church, normal VAT scheme. 2026 fees net of VAT: EUR 72,000. Ordinary costs (software, studio share, insurance, adviser): EUR 9,000. A client dinner: EUR 400 net. A gift to one client: EUR 80. 140 days worked mainly at home without going to the studio, no separate room. All VAT she collected in 2026 she also paid over in 2026, so VAT nets to nil in the EÜR. A laptop for EUR 1,800 net. Basic health and care cover per the insurer's certificate (already net of the 4% cut): EUR 7,200. Private pension (Rürup) EUR 3,000. Prepayments paid: EUR 10,000. (Invented case.)

- Dinner: 70% of 400 = EUR 280. Gift: over EUR 50, so EUR 0. Home office: 140 × 6 = EUR 840. Laptop: one-year life, EUR 1,800.
- Profit: 72,000 − 9,000 − 280 − 0 − 840 − 1,800 = EUR 60,080.
- Taxable income: 60,080 − 7,200 − 3,000 − 36 = EUR 49,844. Zone 3.
- Tax: z = 3.2045; (173.10 × 3.2045 + 2,397) × 3.2045 + 1,034.87 = 10,493.59, rounded down EUR 10,493. Below EUR 20,350: no surcharge.
- Balance: 10,493 − 10,000 = EUR 493 to pay one month after the notice.

```oa-check
name: DE Freiberufler 2026, single, profit from EÜR items, zone 3
inputs:
  fees: 72000
  ordinary_costs: 9000
  dinner: 400
  gift: 80
  home_days: 140
  laptop: 1800
  basic_cover: 7200
  pension: 3000
  prepaid: 10000
steps:
  - dinner_deductible: dinner * 0.70
  - gift_deductible: 0
  - home_office: min(home_days * 6, 1260)
  - profit: fees - ordinary_costs - dinner_deductible - gift_deductible - home_office - laptop
  - taxable: floor(profit - basic_cover - pension - 36)
  - z: (taxable - 17799) / 10000
  - tax: floor((173.10 * z + 2397) * z + 1034.87)
  - balance: tax - prepaid
expected:
  profit: 60080
  taxable: 49844
  tax: 10493
  balance: 493
```

`gift_deductible` is 0 because the EUR 80 gift is over the EUR 50 limit, so none of it counts.

### Example 2: sole trader with the trade tax credit capped, church member

Bernd runs an online shop in a town with a trade tax multiplier of 360%. 2026 profit EUR 95,000, his only income; no trade tax add-backs. Single, church member at 9%. Special expenses: basic health and care cover EUR 9,000, pension EUR 6,000. 2026 is his first year of trading, so no church tax or prepayments were paid in it and the EUR 36 lump sum applies. (Invented case; the multiplier is an input, each town sets its own.)

- Trade tax: 95,000 − 24,500 = 70,500 × 3.5% = Messbetrag EUR 2,467.50; × 360% = EUR 8,883. Not deductible, so profit stays EUR 95,000.
- Taxable income: 95,000 − 9,000 − 6,000 − 36 = EUR 79,964. Zone 4: 0.42 × 79,964 − 11,135.63 = 22,449.25, so EUR 22,449.
- Credit: 4 × 2,467.50 = 9,870. Cap on trade share: all income is trade, so EUR 22,449. Cap on trade tax payable: EUR 8,883. The lowest is EUR 8,883; the other EUR 987 is lost.
- Income tax: 22,449 − 8,883 = EUR 13,566. Below EUR 20,350: no surcharge.
- Church tax at 9% on the tax before the credit: 9% × 22,449 = EUR 2,020.41 (state rounding rules may differ).

```oa-check
name: DE sole trader 2026, § 35 credit capped by trade tax payable, church tax base
inputs:
  profit: 95000
  hebesatz: 3.60
  basic_cover: 9000
  pension: 6000
steps:
  - trade_income: floor(profit / 100) * 100
  - messbetrag: (trade_income - 24500) * 0.035
  - trade_tax: messbetrag * hebesatz
  - taxable: floor(profit - basic_cover - pension - 36)
  - tariff_tax: floor(0.42 * taxable - 11135.63)
  - credit: min(4 * messbetrag, tariff_tax, trade_tax)
  - income_tax: tariff_tax - credit
  - church_tax: tariff_tax * 0.09
expected:
  messbetrag: 2467.50
  trade_tax: 8883
  taxable: 79964
  tariff_tax: 22449
  credit: 8883
  income_tax: 13566
  church_tax: 2020.41
```

In `credit`, the second term is the tax on trade income: here trade income is all the income, so the share is the whole tariff tax.

## Ask the client first

1. What exactly is the work, and is a trade registered? This decides Anlage S or G, trade tax and the § 35 credit.
2. VAT status: turnover in 2025 and expected in 2026, and whether the small-business rule is used. This decides gross or net figures.
3. Home office: days worked mainly at home, and whether a separate room is the centre of all work.
4. Car: business asset or private, business-use share, and logbook or 1% method.
5. Health and pension cover: statutory, private or Künstlersozialkasse, and the insurer's annual certificates.
6. Married and assessed jointly? Church member, and in which state?

## Sources

| Source | URL | Read on |
|---|---|---|
| EStG § 2 (order from income to taxable income) | https://www.gesetze-im-internet.de/estg/__2.html | 2026-10-23 |
| EStG § 4 (§ 4(5) limits, home office, trade tax not deductible) | https://www.gesetze-im-internet.de/estg/__4.html | 2026-10-23 |
| EStG § 6 (EUR 800, pool, 1% car rule) | https://www.gesetze-im-internet.de/estg/__6.html | 2026-10-23 |
| EStG § 7 (declining balance 30%, electric vehicles) | https://www.gesetze-im-internet.de/estg/__7.html | 2026-10-23 |
| EStG § 7g (investment deduction) | https://www.gesetze-im-internet.de/estg/__7g.html | 2026-10-23 |
| EStG § 9 (EUR 0.38 per km, meal rates) | https://www.gesetze-im-internet.de/estg/__9.html | 2026-10-23 |
| EStG § 10 (special expenses, caps) | https://www.gesetze-im-internet.de/estg/__10.html | 2026-10-23 |
| EStG § 10c (lump sum EUR 36) | https://www.gesetze-im-internet.de/estg/__10c.html | 2026-10-23 |
| EStG § 10d (losses) | https://www.gesetze-im-internet.de/estg/__10d.html | 2026-10-23 |
| EStG § 11 (cash basis, ten-day rule) | https://www.gesetze-im-internet.de/estg/__11.html | 2026-10-23 |
| EStG § 12 (personal taxes not deductible) | https://www.gesetze-im-internet.de/estg/__12.html | 2026-10-23 |
| EStG §§ 15, 18 (trade, self-employed work) | https://www.gesetze-im-internet.de/estg/__18.html | 2026-10-23 |
| EStG § 25 (electronic filing) | https://www.gesetze-im-internet.de/estg/__25.html | 2026-10-23 |
| EStG § 32a (2026 tariff) | https://www.gesetze-im-internet.de/estg/__32a.html | 2026-10-23 |
| EStG § 35 (trade tax credit) | https://www.gesetze-im-internet.de/estg/__35.html | 2026-10-23 |
| EStG § 36 (payment of balance) | https://www.gesetze-im-internet.de/estg/__36.html | 2026-10-23 |
| EStG § 37 (prepayments) | https://www.gesetze-im-internet.de/estg/__37.html | 2026-10-23 |
| EStG § 51a (church tax base) | https://www.gesetze-im-internet.de/estg/__51a.html | 2026-10-23 |
| EStDV §§ 56, 60 (duty to file, EÜR electronically) | https://www.gesetze-im-internet.de/estdv_1955/__56.html | 2026-10-23 |
| GewStG § 11 (EUR 24,500, 3.5%) | https://www.gesetze-im-internet.de/gewstg/__11.html | 2026-10-23 |
| GewStG §§ 16, 36 (multiplier floor 280% only from 2027) | https://www.gesetze-im-internet.de/gewstg/__36.html | 2026-10-23 |
| BGBl. 2026 I Nr. 197, law of 29 June 2026, Art. 8 (floor 200 to 280) | https://www.recht.bund.de/bgbl/1/2026/197/VO.html | 2026-10-23 |
| UStG § 19 (EUR 25,000 / 100,000) | https://www.gesetze-im-internet.de/ustg_1980/__19.html | 2026-10-23 |
| SolzG §§ 3, 4 (EUR 20,350 / 40,700, 5.5%, 11.9%) | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-10-23 |
| AO §§ 108, 138, 141, 149 (deadlines, registration, books) | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-10-23 |
| AO § 152 (late-filing surcharge) | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-10-23 |
| AO §§ 233a, 238 (interest 0.15% a month) | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-10-23 |
| AO § 240 (late payment 1%) | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-10-23 |
| AO §§ 370, 378 (evasion, reckless understatement, fine up to EUR 50,000) | https://www.gesetze-im-internet.de/ao_1977/__378.html | 2026-10-23 |
| EStG § 49 (German income of non-residents) | https://www.gesetze-im-internet.de/estg/__49.html | 2026-10-23 |
| SVBezGrV 2026 § 4 (miners' pension ceiling EUR 124,800) | https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html | 2026-10-23 |
| BMF, Anlage EÜR 2026 form and instructions (letter of 1 September 2026) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 | 2026-10-23 |
| BMF booklet "Steuern von A bis Z" (Stand January 2025; church tax 8 or 9%) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 | 2026-10-23 |

Not yet confirmed: which states charge 8% and which 9% church tax, and their rounding (state church tax rules, not on a federal page); the one-year life for computers rests on a BMF letter of 22 February 2022 as cited in the 2026 EÜR instructions, not on the statute; the EUR 0.30 per km rate for business trips rests on the same instructions; the 2026 main form and Anlage S and G line numbers (ELSTER's 2026 guide is not yet published).
