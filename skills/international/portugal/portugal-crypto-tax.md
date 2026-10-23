---
name: portugal-crypto-tax
description: "Portuguese IRS on crypto assets for resident individuals, tax year 2026. Covers gains on crypto that is not a security (CIRS art. 10(1)(k)): the 28% autonomous rate or aggregation at the 2026 bands (12.5% to 48% plus the solidarity surcharge), the exclusion for crypto held 365 days or more (art. 10(22)), tax-free crypto-for-crypto swaps (art. 10(23)), the carve-out for non-cooperative counterparties (art. 10(24)), the exit charge on loss of residence (art. 10(25), art. 43(12)), FIFO per custodian, rewards paid in crypto or fiat, mining and trading as Category B (coefficients 0.15 and 0.95), losses, filing and fines. Article numbers follow Decreto-Lei 97/2026, which renumbered art. 10. Trigger on: 'crypto tax Portugal', 'Bitcoin Portugal 365 dias', 'criptoativos IRS', 'staking Portugal', 'exit tax crypto Portugal', 'Anexo G crypto'. Out of scope: self-employed rules in general (pt-income-tax), residence and other exit rules (pt-cross-border), NHR and IFICI (pt-nhr-ifici), companies (pt-corporate-tax)."
version: 1.1
jurisdiction: PT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
verified_by: pending
depends_on:
  - pt-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal: IRS on crypto assets (tax year 2026)

> Source-cited draft: not reviewed by an accountant.

This skill computes the IRS of a Portuguese resident individual on crypto: gains on sale, rewards, mining and trading as a business, and the charge on leaving Portugal. Crypto gains have been taxable since 1 January 2023 (Lei 24-D/2022). Decreto-Lei 97/2026, de 20 de maio, renumbered CIRS art. 10. The crypto rules did not change in substance: the 365-day exclusion moved from n.º 19 to n.º 22, swaps from n.º 20 to n.º 23, the carve-out from n.º 21 to n.º 24, and the exit charge from n.º 22 to n.º 25. Older material citing art. 10(17), (19) or (22) uses the old numbers.

Sibling skills, which this one links to and does not repeat:

- `pt-income-tax`: Category B (self-employed) rules, the simplified regime, payments on account.
- `pt-irs-employees-investment`: the 2026 bands in full, deductions from the tax, the household, interest rates.
- `pt-cross-border`: residence, split years, non-residents, exit rules for other assets.
- `pt-nhr-ifici`: NHR and IFICI holders.
- `pt-social-contributions`: social security on Category B crypto income.

Every figure below was read on the Portal das Finanças (AT's consolidated CIRS and RGIT) on 2026-10-23.

## Who this applies to

**Resident individuals.** Residence follows CIRS art. 16: more than 183 days in Portugal in any 12-month period starting or ending in the year, or a home kept as a habitual residence. Residents are taxed on worldwide gains. Non-residents are in `pt-cross-border`.

**What counts as a crypto asset.** Any digital representation of value or rights that can be transferred or stored electronically using distributed ledger or similar technology (art. 10(20)). Unique crypto assets not fungible with other crypto assets (NFTs) are excluded from that definition (art. 10(21)). Crypto assets that are securities follow the securities rules, not this skill (art. 10(1)(k)).

**Which category.**

| Activity | Category and rule |
|---|---|
| Occasional sale of crypto for fiat, goods or services | Category G capital gain (art. 10(1)(k)) |
| Rewards from crypto operations (staking, lending) paid in fiat | Category E capital income (art. 5(2)(u)) |
| Rewards paid in crypto | Not taxed on receipt; taxed as a capital gain when the crypto received is sold (art. 5(11)) |
| Crypto trading or mining carried on as a business | Category B (`pt-income-tax`); coefficient 0.15 for crypto operations, 0.95 for mining (art. 31(1)(a) and (d)) |
| Crypto received as pay for work | Category A or B, as pay; not a capital gain |

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Net crypto gains (Category G), held under 365 days | 28% autonomous rate | 2026 | CIRS art. 72(1)(c): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx |
| Option to aggregate instead | 2026 IRS bands, 12.50% to 48.00%; solidarity surcharge 2.5% over EUR 80,000 and 5% over EUR 250,000 | 2026 | CIRS art. 72(13), art. 68 (Lei 73-A/2025), art. 68-A: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx |
| Crypto held 365 days or more | Gains and losses excluded | 2026 | CIRS art. 10(22), wording of DL 97/2026: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx |
| Crypto-for-crypto swap (held under 365 days) | No tax; the crypto received takes the acquisition value of the crypto given | 2026 | CIRS art. 10(23) |
| Carve-out | Exclusion and swap deferral do not apply when the taxpayer or the payer is not resident in the EU/EEA or in a state with a tax treaty or exchange-of-information agreement with Portugal | 2026 | CIRS art. 10(24) |
| Loss of residence | Treated as a sale; gain = market value on the date residence ends less acquisition value and acquisition costs | 2026 | CIRS art. 10(25), art. 43(12): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs43.aspx |
| Rewards paid in fiat (Category E) | 28% autonomous rate; no withholding | 2026 | CIRS art. 5(2)(u), art. 72(1)(d), art. 101-B(5) |
| Order of disposal | FIFO, separately at each custodian or crypto service provider | 2026 | CIRS art. 43(8)(g) and (9) |
| Losses with a counterparty in a listed low-tax regime | Do not count | 2026 | CIRS art. 43(7) |
| Loss carry-forward, Category G crypto | 5 years, only if the person aggregates | 2026 | CIRS art. 55(1)(d): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs55.aspx |
| Simplified regime coefficients (Category B) | 0.15 crypto operations; 0.95 mining | 2026 | CIRS art. 31(1)(a) and (d): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Category B loss carry-forward | 12 years | 2026 | CIRS art. 55(1)(a) |

There is no 35% rate on crypto gains. The 35% list in art. 72(18) covers capital income from listed low-tax jurisdictions and gains on certain securities and trusts, not art. 10(1)(k). The 2026 bands are lower than 2025: use the Lei 73-A/2025 table, not the 2025 table.

## The taxable base

**Gain on each sale (Category G).** Sale value less acquisition value, each with the costs needed to buy and sell (art. 10(4)(a), art. 43(12) for the exit). Convert to euros at the date of each operation. Which units were sold: the oldest first, counted at each custodian separately (art. 43(8)(g) and (9)). A wallet at one exchange and another at a second exchange are two FIFO queues.

**365-day test.** Each unit sold is checked against its own acquisition date. Units held 365 days or more are out, gains and losses both (art. 10(22)). Units held less are in.

**Swaps.** When crypto held under 365 days is exchanged for other crypto, there is no tax. The new crypto takes the old acquisition value (art. 10(23)). The swap rule also covers crypto received as a reward under art. 5(11). Tax arises when crypto is exchanged for fiat, goods or services.

**Net and choose.** Net all Category G crypto gains and losses of the year (art. 43(1)). A net gain pays 28% (art. 72(1)(c)), or the person opts to aggregate it with other income at the band rates (art. 72(13)). Aggregation pays when the marginal rate on the gain is below 28%: in 2026 that means total taxable income stays within band 4 (EUR 23,089, marginal 24.10%), or reaches band 5 only for a small part. If the person aggregates crypto gains, they must aggregate all income of that category (art. 22(5)). Worked example 1 shows the test.

**Losses.** A net loss on crypto can be carried forward 5 years only if the person aggregates in the loss year (art. 55(1)(d)). Losses with a counterparty in a listed low-tax regime do not count (art. 43(7)).

**Rewards.** Rewards in fiat are Category E income in the year received, 28% or aggregated (art. 5(2)(u), art. 72(1)(d)). Rewards in crypto are not taxed on receipt; the gain arises when they are sold (art. 5(11)). This skill takes their acquisition value as EUR 0.

**Business crypto (Category B).** If trading or mining is a business, use `pt-income-tax`. In the simplified regime, crypto operations use coefficient 0.15 and mining 0.95 (art. 31(1)(a) and (d)). The income counts when the crypto is sold (art. 31(17)). Stopping the activity or losing residence counts as a sale (art. 31(18)). The 365-day exclusion is a Category G rule and does not apply to Category B income.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Modelo 3 for 2026, with Anexo G for taxable crypto gains | 1 April to 30 June 2027, online | CIRS art. 60(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx |
| Payment of the balance | By 31 August 2027 when AT assesses within the normal period | CIRS art. 97(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx |
| Exit charge | Declared in the return for the year residence ends, with the year's other income | CIRS art. 10(25), art. 43(12) |

Excluded gains on crypto held 365 days or more are reported in the return's annex for excluded gains (Anexo G1). Rewards in fiat go in Anexo E, business crypto in Anexo B. Box numbers change between return versions; check the 2026 form.

Keep, for each unit: acquisition date and price, custodian, sale date and price, and fees. The 365-day exclusion depends on proving the acquisition date.

## Penalties and interest

- **Late or missing return:** fine of EUR 150 to EUR 3,750 (RGIT art. 116(1)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx
- **Omissions or errors in the return** (for example an undeclared crypto gain) that are not fraud: fine of EUR 375 to EUR 22,500, cut to a quarter when no tax is due (RGIT art. 119(1) and (2)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit119.aspx
- **Compensatory interest** when the taxpayer's fault delays the assessment (LGT art. 35), and **late payment interest** from the due date (LGT art. 44). Rates: see `pt-irs-employees-investment`. Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx

## Cross-border points

- **Exit charge.** Losing Portuguese residence is treated as a sale of crypto held as a capital asset (art. 10(25)). The gain is market value on the date residence ends less acquisition value and costs (art. 43(12)). Units held 365 days or more on that date stay excluded (art. 10(22)). The rule was added by Lei 24-D/2022 as art. 10(22); Decreto-Lei 97/2026 renumbered it n.º 25 and did not change it. Residence ends on the last day of presence (art. 16(4)), and a person who becomes resident again in the following year is resident for the whole year (art. 16(16)). See `pt-cross-border` for the residence rules. Worked example 2 shows the charge.
- **Business crypto on exit.** For Category B crypto, losing residence counts as a sale (art. 31(18)(b)).
- **Non-cooperative counterparties.** No 365-day exclusion and no swap deferral where the taxpayer or the payer is outside the EU/EEA and outside any treaty or exchange-of-information agreement (art. 10(24)). Art. 10(24) still refers to "n.os 19 e 20"; this skill reads that as the rules now in n.º 22 and 23.
- **Foreign exchanges.** A foreign exchange withholds no Portuguese tax. The gain is taxed in Portugal; foreign tax credit, if any, is in `pt-foreign-source-treaties`.
- **NHR and IFICI.** See `pt-nhr-ifici`.

## Worked examples

### Example 1: gain on BTC held under 365 days, 28% or aggregation

A resident bought 2 BTC at EUR 30,000 each on 1 February 2026, with EUR 200 of fees. She sold both on 1 October 2026 at EUR 50,000 each, with EUR 300 of fees. Held 8 months, so taxable. Her only other income is a salary of EUR 40,000, with 11% employee social security (EUR 4,400). Deductions from the tax are left out because they are the same either way.

1. Gain: (100,000 - 300) - (60,000 + 200) = EUR 39,500.
2. Option A, 28%: 39,500 x 28% = EUR 11,060.
3. Option B, aggregate: salary less the specific deduction of EUR 4,587.09 (higher than her EUR 4,400 social security) gives EUR 35,412.91. Tax on salary alone: 29,397 x 20.579% + (35,412.91 - 29,397) x 34.90% = EUR 8,149.16. With the gain, taxable income is EUR 74,912.91 (band 8). Tax: 46,566 x 26.472% + (74,912.91 - 46,566) x 44.60% = EUR 24,969.67. Extra tax from the gain: EUR 16,820.51. No solidarity surcharge (under EUR 80,000).
4. The 28% rate is cheaper by EUR 5,760.51. She declares the gain in Anexo G at 28%.

```oa-check
name: PT crypto gain held under 365 days, 28% vs aggregation (2026)
inputs:
  proceeds: 100000
  sale_fees: 300
  cost: 60000
  buy_fees: 200
  salary: 40000
  ias: 537.13
steps:
  - gain: proceeds - sale_fees - (cost + buy_fees)
  - autonomous_tax: gain * 0.28
  - specific_deduction: round(max(8.54 * ias, salary * 0.11), 2)
  - cat_a: salary - specific_deduction
  - tax_salary_only: round(29397 * 0.20579 + (cat_a - 29397) * 0.349, 2)
  - aggregated: cat_a + gain
  - tax_aggregated: round(46566 * 0.26472 + (aggregated - 46566) * 0.446, 2)
  - extra_if_aggregated: tax_aggregated - tax_salary_only
  - saving_at_28: extra_if_aggregated - autonomous_tax
expected:
  gain: 39500
  autonomous_tax: 11060
  cat_a: 35412.91
  tax_salary_only: 8149.16
  tax_aggregated: 24969.67
  extra_if_aggregated: 16820.51
  saving_at_28: 5760.51
```

### Example 2: leaving Portugal with crypto, the exit charge

A resident stops being resident on 30 September 2026. On that date he holds, at one EU exchange:

- 1 BTC bought on 1 June 2026 for EUR 60,000 plus EUR 100 of fees (121 days), market value EUR 70,000;
- 10 ETH bought on 1 March 2024 for EUR 20,000 (over 365 days), market value EUR 30,000.

He sells nothing. He has no other Category G income in 2026.

1. Loss of residence is treated as a sale (art. 10(25)).
2. BTC: 70,000 - 60,000 - 100 = EUR 9,900, held under 365 days, so taxable (art. 43(12)).
3. ETH: gain of EUR 10,000, held over 365 days, so excluded (art. 10(22)).
4. Tax at 28%: 9,900 x 28% = EUR 2,772, declared in his 2026 return (Anexo G). He may opt to aggregate instead; with no other income in 2026 that test is the one in example 1.
5. If he becomes resident again in 2027, he is treated as resident for the whole of 2026 (art. 16(16)). Ask about plans to return before filing.

```oa-check
name: PT crypto exit charge on loss of residence, BTC under 365 days, ETH excluded (2026)
inputs:
  btc_market_value: 70000
  btc_cost: 60000
  btc_fees: 100
  eth_market_value: 30000
  eth_cost: 20000
  eth_excluded: 1
steps:
  - btc_gain: btc_market_value - btc_cost - btc_fees
  - eth_gain: eth_market_value - eth_cost
  - taxable_gain: btc_gain + eth_gain * (1 - eth_excluded)
  - exit_tax: taxable_gain * 0.28
expected:
  btc_gain: 9900
  eth_gain: 10000
  taxable_gain: 9900
  exit_tax: 2772
```

## Ask the client first

1. Were you resident in Portugal for all of 2026, and do you plan to leave or have you left? (Worldwide tax, exit charge, split year.)
2. For every sale, swap or payment with crypto: dates bought and sold, prices in euros, fees, and the exchange or wallet. (FIFO per custodian and the 365-day test.)
3. Did you receive staking, lending or other rewards, in fiat or in crypto? (Category E in the year, or a gain on later sale.)
4. Do you trade or mine regularly, with dedicated equipment or as your living? (Category B and `pt-income-tax`.)
5. Are any exchanges or counterparties outside the EU/EEA, in a country with no tax treaty with Portugal, or in a listed low-tax jurisdiction? (Art. 10(24) and art. 43(7).)
6. What is your other income in 2026? (Whether aggregation beats 28%.)

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 10, crypto gains, n.º 20 to 25 (wording of DL 97/2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx | 2026-10-23 |
| CIRS art. 10, wording in force until May 2026 (exit rule as n.º 22, from Lei 24-D/2022) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs10ra_202605.aspx | 2026-10-23 |
| CIRS art. 5, crypto remuneration (n.º 2 u) and n.º 11) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs5.aspx | 2026-10-23 |
| CIRS art. 16, residence | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx | 2026-10-23 |
| CIRS art. 22, aggregation | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs22.aspx | 2026-10-23 |
| CIRS art. 31, coefficients 0.15 and 0.95, n.º 17 and 18 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-10-23 |
| CIRS art. 43, FIFO, low-tax losses, exit value | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs43.aspx | 2026-10-23 |
| CIRS art. 55, losses | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs55.aspx | 2026-10-23 |
| CIRS art. 60 and 97, filing and payment | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx | 2026-10-23 |
| CIRS art. 68, IRS bands 2026 (wording of Lei 73-A/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx | 2026-10-23 |
| CIRS art. 68-A, solidarity surcharge | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx | 2026-10-23 |
| CIRS art. 72, 28% rate, aggregation option, 35% list | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx | 2026-10-23 |
| CIRS art. 101-B(5), no withholding on crypto remuneration | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101b.aspx | 2026-10-23 |
| CIRS art. 25, specific deduction (example 1) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx | 2026-10-23 |
| RGIT art. 116 and 119, fines | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit119.aspx | 2026-10-23 |
| LGT art. 35 and 44, interest | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx | 2026-10-23 |
| Segurança Social guide, IAS 2026 EUR 537.13 (example 1) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-10-23 |

Not yet confirmed: the text of Decreto-Lei 97/2026 itself (the Diário da República page did not load; the renumbering is taken from AT's consolidated CIRS, which marks each paragraph "anterior n.º"); the acquisition value of crypto received as a reward (this skill assumes EUR 0); whether a swap restarts the 365-day period (no AT guidance read); how occasional mining outside a business is taxed; how NFT sales are taxed once excluded from the crypto definition; the Anexo G, G1, E and B box numbers for 2026; that art. 10(24), which still cites "n.os 19 e 20", is read as n.º 22 and 23; DAC8 and Portuguese exchange reporting dates.

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
