---
name: cn-cross-border
description: "Mainland China 2026 cross-border tax route: individual domicile/day-count/six-year rules, Chinese and foreign source, enterprise residence and establishments, individual and corporate foreign-tax credits, emigration/cessation clearance, non-resident withholding and treaty evidence. Uses the actual applicable treaty; no generic relocation or passport shortcut."
jurisdiction: CN
category: international
tax_year: 2026
version: 1.0
last_updated: 2026-10-29
tier: 2
---

# China cross-border tax: residence, source, foreign credits and departure

## Who this applies to

Mainland China individuals and enterprises with foreign income, incoming/outgoing work, foreign owners or a proposed move. Hong Kong, Macao, Taiwan and foreign countries are separate jurisdictions; their domestic rules are not established by this China Guide. Use `cn-iit` for individual tax computations, `cn-corporate-tax` for enterprise profits, `cn-withholding` for payer duties and `cn-transfer-pricing` for related-party pricing.

**Individual residence is not citizenship or simply where the person sleeps.** A person domiciled in China is resident; a non-domiciled person is resident if present at least 183 days in the calendar year. Domicile means habitually residing in China because of household registration, family or economic interests. A non-domiciled person below 183 days is a non-resident taxable on Chinese-source income. Resident status generally brings worldwide income into scope, subject to the actual non-domiciled concession and treaty ([IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 1; [IIT Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443213.html) art. 2). Do not declare that a Singapore address, foreign residence certificate or hukou fact alone settles every issue.

An enterprise is Chinese resident if established under Chinese law or, for a foreign-established enterprise, if its actual management body is in China. The actual management body exercises substantive, overall management/control over production/business, personnel, accounts and property. Non-residents are taxed on Chinese establishment profits and effectively connected foreign income, or on specified Chinese-source income without that connection ([EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) arts. 2–3; [EIT Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html) art. 4). A treaty permanent-establishment test is separate from the domestic establishment definition.

## Rates, bands and thresholds

| Test / amount | Rule | Official provision |
| --- | --- | --- |
| Individual calendar-year residence, no China domicile |At least 183 days | [IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 1 |
| Non-domiciled foreign-income concession |Fewer than 6 consecutive years reaching 183 days; foreign-source income also must be paid by a foreign unit/individual and required filing conditions apply | [IIT Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443213.html) art. 4 |
| Break resetting that consecutive-year count |A single absence **over 30 days** in the relevant 183 day year, as prescribed | [IIT Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443213.html) art. 4; [2019 No.34](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201904/t444837.html) |
| Non-domiciled short stay |Cumulative stay not over 90 days; foreign-paid Chinese-source work income not borne by a China establishment has the stated domestic exemption | [IIT Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443213.html) art. 5; no universal treaty 90/183 day exemption inferred |
| Individual foreign-tax-credit excess |Up to 5 following tax years, with the appropriate country's remaining limit | [MOF/STA 2020 No.3](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202002/t452398.html) §6 |
| Ordinary EIT rate used in corporate illustration |25%; actual exemption/preference eligibility separately tested | [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) art. 4 |
| Corporate foreign-credit excess |5 consecutive tax years starting after origin year, subject to limit headroom | [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) art. 23; [EIT Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html) art. 79; [Caishui 2009 No.125](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203574/content.html) §9 |
| Corporate credit basket method |Country-by-country or comprehensive; election cannot change within 5 years | [Caishui 2017 No.84](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5202488/content.html) §1 |
| Corporate indirect dividend-credit holding |Specified qualifying 20% holding chain and up to 5 foreign tiers; full direct/indirect conditions apply | [Caishui 2017 No.84](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5202488/content.html) §2; [Caishui 2009 No.125](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203574/content.html) §§5–6 as modified |

## The base

### Individual source, residence and credits

Record domicile facts, full arrival/departure records, all work locations and the actual economic payer/bearer. For a non-domiciled individual's residence-day count,2019 No.34 counts days of actual China presence lasting 24 hours; a day shorter than 24 hours does not count. Its consecutive-year rule counts from 2019, not an invented pre 2019 history. Do not confuse a residence day with an income allocation workday. The 183 day and over 30 day tests must be applied to the actual year/absence records.

Chinese source is determined by the income type, not the receiving bank account. Work/services performed in China, property used or transferred in China, rights used in China and the specified China-paid dividend/interest rules follow IIT Regulations art. 3. The non-domiciled foreign-source/foreign-paid concession does not exempt Chinese-source salary merely because an overseas parent transfers it. Apply the specific income allocation measures in `cn-iit` before tax or treaty relief.

For a Chinese-resident individual's foreign income, classify each amount into comprehensive, business or the relevant separate category. Comprehensive foreign income is combined with domestic comprehensive income for annual computation; do not automatically apply 20% to every offshore receipt. Use the country-specific category limits and their sum under 2020 No.3 §3. For comprehensive income the limit is Chinese tax on combined comprehensive income×that country's comprehensive **income amount**/combined comprehensive income amounts. Income amount is not always gross cash receipts; authors' fees/labour receipts follow their statutory reductions.

Only qualifying foreign income tax due and actually paid is creditable, with the statutory exclusions for erroneous/non-treaty tax, penalties/interest, amounts refunded/compensated and exempt foreign income. Credit the lower of qualifying tax and limit; excess carries subject to the same country's five-year headroom. Obtain tax payment/assessment evidence or the prescribed substitute proof; treaty tax sparing applies only under its actual treaty provision ([IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 7; [MOF/STA 2020 No.3](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202002/t452398.html) §§3–6,9–10). Do not cross-credit Country A's excess against Country B without a legal rule.

### Enterprise residence, establishments and foreign credits

Resident enterprises include foreign branch income whether or not remitted to China. Determine source and allowable costs under EIT Regulations art. 7 and No.125 §3, then calculate taxable income and tax consistently with Chinese rules. A foreign establishment without independent legal tax status is not treated as a dividend-paying subsidiary. Avoid netting foreign losses against domestic profits without the actual rule ([EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) arts. 3,17–18; [Caishui 2009 No.125](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203574/content.html) §3).

For qualifying foreign income tax actually due/paid, use the selected lawful basket method and the ordinary limit: combined Chinese EIT×qualifying basket's foreign taxable income/combined taxable income. The standard statutory rate applies unless the competent provisions specify otherwise. Exclude penalties, incorrectly imposed/non-treaty tax, refunded/compensated amounts and other specified non-creditable tax. For indirect dividend credits, verify each ownership tier, actual underlying tax, allocation and evidence. No.84 expands the specified chain to 5 tiers; do not retain the unmodified old 3 tier rule ([EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) arts. 23–24; [EIT Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html) arts. 77–80; [Caishui 2009 No.125](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203574/content.html) §§4–9; [Caishui 2017 No.84](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5202488/content.html)).

Maintain a separate origin-year register of foreign tax, direct/indirect classification, basket, allowable limit, tax used and expiry. A lawful switch of method after the election period preserves eligible previous excess only for its remaining statutory years. Simplified-credit methods, tax sparing, foreign losses, preferential domestic regimes and special reorganisations require their own eligibility and evidence; no blanket credit at 12.5% or exemption based on a foreign headline rate is asserted here ([Caishui 2009 No.125](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203574/content.html) §§7,10; [Caishui 2017 No.84](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5202488/content.html) §1).

## Deadlines and filing

| Matter | Rule | Official provision |
| --- | --- | --- |
| Resident individual's foreign income |File/pay 1 March–30 June after the income year, through the designated competent Chinese tax authority | [IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 13; [MOF/STA 2020 No.3](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202002/t452398.html) §§7–8 |
| Individual emigration with cancellation of Chinese household registration |Settle tax **before cancellation** | [IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) arts. 10,13 |
| EIT ordinary annual settlement |Within 5 months after tax year end;2026 calendar year therefore 31 May 2027, subject to applicable lawful adjustments | [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) art. 54 |
| Enterprise stops business during year |Within 60 days after actual termination, settle current-period EIT; liquidating enterprise files/pays liquidation-income tax before tax deregistration | [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) art. 55 |
| Non-resident payer withholding |Use the separate EIT 7 day/IIT/VAT clocks in `cn-withholding`; no universal “cross-border deadline” | [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) arts. 37–40; `cn-withholding` |

The individual pre-cancellation duty is not a statement that every flight triggers mark-to-market tax, nor proof that a formal exit certificate exists or is unnecessary in every administrative case. Preserve the exact move, domicile, work, property, hukou and filing facts. The older China–Singapore corridor remains a historical supporting document, not a substitute for this 2026 national route or a fresh Singapore-law opinion.

## Penalties and interest

Foreign income is not exempt from ordinary declaration/payment duties. Tax Collection Administration Law art. 32 applies a daily 0.05% late surcharge in its statutory overdue situations. Failure to file, false returns, tax evasion, withholding failures and nonpayment after an order have distinct triggers and sanctions in arts. 60,62–64,68–69; the relevant primary provisions and amounts are preserved in `cn-iit`, `cn-corporate-tax` and `cn-withholding`. Apply the actual violation date, liability, notice and defence facts; do not infer one automatic percentage penalty from a foreign account or CRS report ([Tax Collection Administration Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html)). TP special interest is separately covered by `cn-transfer-pricing`.

## Cross-border points

**Treaty work starts after domestic classification.** Use the actual treaty and effective protocol/MLI positions for residence tie-breakers, establishment, source allocation, withholding caps and credit relief. A foreign tax-residence certificate is evidence, not a unilateral override of Chinese domestic law. No treaty-country rate table, generic services 183 day test or automatic Singapore residence outcome is verified here. Non-resident treaty claims follow self-assessment/reporting/retained-evidence procedures and subsequent checks ([STA 2019 No.35](https://tianjin.chinatax.gov.cn/11200000000/0300/030004/03000418/20191024101530609.shtml) arts. 2–8).

Keep corporate residence, individual domicile, registered business location and the economic place of work separate. Corporate relocation, an indirect China-asset transfer, an outbound related-party asset movement, a non-resident shareholder payment and individual emigration are different events. Refer indirect-transfer/beneficial-owner issues to `cn-withholding` and related-party pricing to `cn-transfer-pricing`. CRS/CARF reporting, SAFE currency controls, bank remittance documents, foreign immigration and the destination's tax law require their own current primary sources; none establishes a new China tax rate here.

## Two worked examples that recompute

**Example 1: resident individual's comprehensive foreign credit.** Assume a resident with domestic comprehensive income amount 400000 and Country A amount 100000; basic deduction 60000 and allowable social deductions 40000. Combined taxable income 400000; Chinese tax at 25% less 31920=68080. Country A limit=68080×100000/500000=13616. Qualifying Country A income tax paid 20000 gives credit 13616 and excess 6384 for the applicable five-year carry. Chinese liability after this credit, before other relief/prepayments, is 54464. Actual category, income amounts, deductions and proof are assumed verified ([MOF/STA 2020 No.3](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202002/t452398.html) §§3,6; `cn-iit`).

```oa-check
name: China 2026 resident comprehensive country credit
inputs:
  china_income_amount: 400000
  country_a_income_amount: 100000
  basic_deduction: 60000
  social_deduction: 40000
  qualifying_foreign_tax: 20000
steps:
  combined_income: china_income_amount + country_a_income_amount
  taxable_income: combined_income - basic_deduction - social_deduction
  chinese_tax: taxable_income * 0.25 - 31920
  country_a_limit: chinese_tax * country_a_income_amount / combined_income
  credit: min(qualifying_foreign_tax, country_a_limit)
  excess: qualifying_foreign_tax - credit
  chinese_liability_after_credit: chinese_tax - credit
expected:
  taxable_income: 400000
  chinese_tax: 68080
  country_a_limit: 13616
  credit: 13616
  excess: 6384
  chinese_liability_after_credit: 54464
```

**Example 2: resident enterprise, one foreign branch basket.** Assume correctly adjusted domestic taxable income 600000 and Country A foreign branch taxable income 400000, no losses/preferences/indirect credits, and qualifying foreign tax 120000. Combined taxable income 1000000; Chinese EIT at 25%=250000. Country A limit 100000; allowed credit 100000; excess 20000 carries within the statutory period. Chinese EIT after credit 150000, before actual domestic prepayments. This is a direct-credit illustration, not proof of a preferential rate or blanket credit for every foreign levy ([EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) art. 23; [Caishui 2009 No.125](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203574/content.html) §§4,8–9).

```oa-check
name: China 2026 resident enterprise direct foreign branch credit
inputs:
  domestic_taxable_income: 600000
  foreign_taxable_income: 400000
  qualifying_foreign_tax: 120000
steps:
  combined_taxable_income: domestic_taxable_income + foreign_taxable_income
  chinese_eit: combined_taxable_income * 0.25
  foreign_limit: chinese_eit * foreign_taxable_income / combined_taxable_income
  credit: min(qualifying_foreign_tax, foreign_limit)
  excess: qualifying_foreign_tax - credit
  chinese_eit_after_credit: chinese_eit - credit
expected:
  combined_taxable_income: 1000000
  chinese_eit: 250000
  foreign_limit: 100000
  credit: 100000
  excess: 20000
  chinese_eit_after_credit: 150000
```

## Ask the client first

- Individual or company? Which countries, dates, entities, income categories and tax years are involved?
- For an individual: domicile/habitual-residence facts, full day/absence/workday records since 2019, economic payer/bearer, family/business interests and proposed hukou cancellation?
- For an enterprise: incorporation, actual overall management/control, China/foreign establishments, legal status of foreign branches/subsidiaries and any cessation/liquidation/asset move?
- What are gross receipts, statutory income amounts, allowable deductions, foreign taxable income, Chinese adjustments, qualifying foreign tax actually paid and available proof?
- Which treaty, effective protocol/MLI text, certificate, ownership tier and beneficial-owner/establishment evidence supports a claim?
- Which foreign-credit method is elected, when was it last changed, and what origin-year excess/losses remain unexpired?
- Which filings, notices, payments, refunds and prepayments already exist? Keep tax clearance separate from immigration and bank documentation.

## Sources

| Source | Official URL | Read on |
| --- | --- | --- |
| IIT Law | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html | 2026-10-29 |
| IIT Regulations | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443213.html | 2026-10-29 |
| 2019 No.34 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201904/t444837.html | 2026-10-29 |
| MOF/STA 2020 No.3 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202002/t452398.html | 2026-10-29 |
| EIT Law | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html | 2026-10-29 |
| EIT Regulations | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html | 2026-10-29 |
| Caishui 2009 No.125 | https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203574/content.html | 2026-10-29 |
| Caishui 2017 No.84 | https://fgk.chinatax.gov.cn/zcfgk/c102416/c5202488/content.html | 2026-10-29 |
| STA 2019 No.35 | https://tianjin.chinatax.gov.cn/11200000000/0300/030004/03000418/20191024101530609.shtml | 2026-10-29 |
| Tax Collection Administration Law | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html | 2026-10-29 |

| Additional operative source | https://guangdong.chinatax.gov.cn/gdsw/fssw_nsrxt_kjxz/2025-10/09/content_b02be06c906e46bca00673beb9e7783a.shtml | 2026-10-29 |

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. A qualified professional in the relevant jurisdiction must review the work before filing, paying or taking a tax position.

**Not yet confirmed:** individual treaty-by-treaty tie-breaker/PE/withholding outcomes, current destination-country tax rules (including Singapore and Hong Kong foreign-income regimes), immigration/hukou/bank certificates and SAFE procedure; corporate reorganisation/asset-migration liquidation exceptions and preferential foreign-credit interactions; simplified or tax-sparing credit eligibility; foreign losses and indirect-credit chain facts; CRS/CARF operational reporting and Pillar Two. These are separate determinations, not a “move abroad and all Chinese tax stops” default.
