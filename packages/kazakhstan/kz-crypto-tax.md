---
name: kz-crypto-tax
description: "Kazakhstan 2026 digital assets and mining: licensing boundaries, recognised income, acquisition cost, electricity charges and quarterly obligations."
version: 1.1
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: tax

type: situation-rules
---

# Kazakhstan digital assets and mining tax v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Kazakhstan individuals disposing of digital assets and lawful mining businesses assessing income tax plus the separate electricity-based mining charge. Determine resident/non-resident, individual/ИП/legal-entity status, activity and period first. The regulatory perimeter changed during 2026; a trading licence or a tax computation does not itself authorise mining or an unregulated venue.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Individual disposal gain | Positive sale/capital-contribution value less statutory original cost (art. 389); ordinary personal annual rate schedule is in kz-income-tax | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Mining income | Pool-distributed asset quantity × prescribed value, excluding value retained as pool commission (art. 325); not simply cash sales less every expense | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Ordinary mining electricity fee | KZT 2 per 1 kWh consumed in the reporting period (art. 659) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Qualifying own renewable/off-grid generation | KZT 1 per 1 kWh under the precise generation conditions in art. 659 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| No mining licence or absent/faulty control meters | KZT 25 per 1 kWh; missing/faulty meters use continuous maximum-capacity consumption computation (art. 659) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Mining fee period/deadlines | Quarterly; declaration by the 15th and payment by the 25th of the second month after the quarter (arts. 660–661) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Digital Assets Law art. 9 requires a mining licence and distinguishes the licensed data-centre-owning/other-lawful-possession route from the hardware-at-a-data-centre route. Do not assume a home setup is legal or licence-exempt. Check the actual licence/subtype, location, electricity supply, pool and meter evidence. The electricity fee is separate from business income tax; the old price-banded charge description is superseded by the current art. 659 rates/conditions.

From 1 May 2026, the national regulated perimeter extends beyond AIFC. Digital Assets Law art. 12-1 permits specified licensed/registered National Bank providers, AIFC licensed participants, regulatory-sandbox and other listed cases. The National Bank’s official 30 April release explains the licensing/registration outside AIFC and its separate relationship with AIFC regulation. The old AIFC-only rule and old secured/unsecured shorthand are incomplete: distinguish unsecured crypto from the current digital-financial-asset categories. Do not assume P2P/offshore activity is unrestricted; establish the actual provider’s permission and applicable rule.

Individual art. 389 cost ordinarily uses documented acquisition value, with specific values for distributions, income already recognised, receivable settlement, previously taxed gifts, inheritance/charity and prescribed valuation evidence. Preferential-tax-state-source assets and cases where the statutory cost provisions cannot determine a cost can have zero original cost. Do not invent a cost, treat every missing statement as legal proof of zero, or apply an unverified loss offset. Corporate/business asset disposal uses art. 326, with different loss and reorganisation provisions; mining-income recognition under art. 325 is not replaced by that disposal formula. Art. 327 denies a second deduction for mining-pool service costs.

Apply `kz-income-tax` for the relevant individual/ИП annual schedule and `kz-corporate-income-tax` for companies; neither an unconditional individual flat rate nor one corporate headline decides every fact pattern. General ИП rules require eligible deductions and the appropriate income category. VAT treatment, crypto-to-crypto characterisation, staking/airdrops and special valuation implementation need their own check; no guessed disposal date or rate is substituted.

## Deadlines and filing

Mining fee: identify actual quarterly kWh and conditions, compute the correct art. 659 branch, use the current mining-fee declaration in the taxpayer cabinet, validate, retain acceptance and pay/verify allocation by arts. 660–661 deadlines. No current electronic line map is invented. Individual gains/assets can trigger income/property and asset disclosure obligations; use `kz-income-tax` and current arts. 417–424 for the applicable job rather than assuming cash-out is the only taxable/reportable event. Keep wallet/exchange statements, acquisition/disposal documents, valuation and fund movements linked to the return.

## Penalties and interest

The KZT 25 mining-fee branch is a statutory fee calculation, not a licence to operate or an exhaustive penalty. Licensing, unregulated activity, tax understatement and late payment can have separate consequences requiring the current applicable provision.

## Cross-border points

Confirm residence, foreign providers and source of assets. AIFC versus national-provider regulation and tax treatment are separate questions. Do not present offshore/P2P trading as automatically lawful, apply treaty relief without entitlement, or assume assets held abroad escape declaration.

## Two worked examples that recompute

Case 1: preserved individual BTC disposal, documented purchase KZT 4,000,000 and sale KZT 6,000,000, no other adjustments and ordinary annual income still below its higher-rate threshold. Gain KZT 2,000,000 gives KZT 200,000 under the owning lower-band schedule. This does not establish regulatory permission.

```oa-check
name: Documented individual digital-asset disposal
inputs:
  sale: 6000000
  documented_cost: 4000000
steps:
  - gain: max(sale - documented_cost, 0)
  - lower_band_tax: gain * 0.10
expected:
  gain: 2000000
  lower_band_tax: 200000
```

Case 2: hypothetical licensed miner consumes 10,000 kWh. Ordinary fee is KZT 20,000; if the precise own-generation conditions apply it is KZT 10,000; missing licence/meter conditions produce KZT 250,000 on the determined consumption base. Do not choose the low branch solely from an electricity invoice label.

```oa-check
name: Mining electricity condition comparison
inputs:
  kwh: 10000
steps:
  - ordinary_fee: kwh * 2
  - qualifying_generation_fee: kwh * 1
  - noncompliant_fee: kwh * 25
expected:
  ordinary_fee: 20000
  qualifying_generation_fee: 10000
  noncompliant_fee: 250000
```

Preserved former “home miner” case: KZT 3,000,000 sale receipts less KZT 1,200,000 claimed costs arithmetically leaves KZT 1,800,000, and a hypothetical applicable lower-band ИП tax would be KZT 180,000 before the separate mining fee. This is not a valid automatic tax result: first establish lawful licensed status, art. 325 recognised mining value, allowable costs (without double-deducting pool costs), income category and the separate measured fee. If those are absent, refuse the old shortcut.

## Ask the client first

- Residence and individual/ИП/company status; trading versus mining activity and dates?
- Provider permission/AIFC or national perimeter and actual mining licence/subtype?
- Complete acquisition/disposal, wallet/pool and valuation evidence?
- Electricity generation/source, kWh, control meter and licence condition?
- Other annual taxable income, costs, already recognised income and declaration history?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 325–327, 363, 389, 417–424 and 657–661 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for current Digital Assets Law arts. 9–10 and 12-1, ordinary browser | https://adilet.zan.kz/rus/docs/Z2300000193 | 2026-11-14 |
| Read for National Bank 30 April release: categories and regulatory perimeter from 1 May 2026 | https://nationalbank.kz/ru/news/informacionnye-soobshcheniya/19193 | 2026-11-14 |

Not yet confirmed: Crypto-to-crypto and staking/airdrop classification, specific valuation implementation, individual loss offsets, asset-specific VAT and current electronic form boxes. Do not reuse the old AIFC-only restriction, price-banded electricity charge or unqualified home-miner net-profit shortcut.
