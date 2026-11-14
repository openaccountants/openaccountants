---
name: china-to-singapore-relocation-tax
description: "Use this skill for a Chinese citizen or long-term China resident moving to Singapore in tax year 2026. China taxes by domicile (household registration, family, economic interests), not by days abroad, so a mover who keeps hukou, family and business in China stays worldwide-taxable; CRS data now reaches Chinese bureaus. It covers the domicile test, what China keeps taxing after a real exit (dividends 20% domestic, 10% under the China-Singapore treaty for individuals; property and equity gains; indirect transfers under Bulletin 7), the USD 50,000 a year foreign exchange quota, and the Singapore side (resident rates to 24%, overseas income generally not taxed, 60% ABSD for foreigners). Built from the law, not reviewed by an accountant."
version: "2.0"
jurisdiction: CN
tax_year: 2026
tax_year_notes: "China calendar tax year 2026; Singapore Year of Assessment 2027 (income of calendar 2026). Singapore rates are those IRAS shows as current."
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: cross-border
type: situation-rules
---

# China to Singapore: domicile, the CRS reckoning, and a clean landing

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by qualified professionals in China and Singapore.

## Who this applies to

**Why this corridor needs a guide.** China is a leading origin country for relocating wealthy individuals, and Singapore is a common destination for founders and families who want proximity, schooling and a hard-currency financial system. The corridor's tax content is asymmetric: **Singapore's side is simple; China's side is the opposite of what most movers assume.** The popular belief ("I live in Singapore now, so China can't tax me") confuses *residence* with **domicile**, and the gap between what Chinese law says and what was historically enforced is closing: tax bureaus can now use **CRS data** on offshore accounts. This guide is about leaving properly, not just leaving.

**Who it's for.** Chinese-tax-connected individuals (citizens and long-term residents) moving to Singapore in 2026, and their advisers on both ends. Enforcement practice in China varies by bureau and is evolving: the legal architecture below is stable, but treat enforcement descriptions as a direction of travel, not a guarantee either way.

Not covered here: inbound foreigners moving to China (`cn-iit`, `cn-cross-border`), Hong Kong (`hong-kong` pack), the full Chinese computation (`cn-iit`) and company-level withholding (`cn-withholding`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| China residence by days | 183 days | A person without domicile in China is resident if present 183 days or more in the tax year (IIT Law art. 1) | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html |
| China IIT on dividends, interest, property transfer gains, rental | 20% | Flat rate (IIT Law art. 3(3)); applies to residents and, on China-source income, non-residents | same |
| China foreign tax credit | Up to the PRC tax on the foreign income | Resident individuals (IIT Law art. 7) | same |
| Six-year rule (inbound only) | Six consecutive years of 183 days with no single absence over 30 days | Only for individuals without domicile; the count starts from 2019 (MOF and STA announcement 2019 No. 34) | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201904/t444837.html |
| China-Singapore treaty, dividends to a company holding 25% or more | 5% cap | Beneficial owner is a company (not a partnership) directly holding at least 25% of the capital (art. 10(2)(1)) | https://guangdong.chinatax.gov.cn/gdsw/gzsw_zcq_zczy_tysc/2021-09/16/2421a19f85e74408a85aa43f2bb50609/files/ca9c3ec21241453290b3ab48b235b4a4.pdf |
| China-Singapore treaty, dividends in other cases (individuals) | 10% cap | Beneficial owner resident in Singapore (art. 10(2)(2)) | same |
| China-Singapore treaty, interest | 10% cap | Other cases (art. 11) | same |
| Individual foreign exchange quota | 等值 5 万美元 (fifty thousand US dollars) a person a year | Annual total for individual sale and purchase of foreign exchange; above it, documented current-account or approved capital routes (SAFE implementing rules art. 2) | https://www.safe.gov.cn/neimenggu/file/file/20170728/b94fb1d6db30472584863040ecb838f3.pdf |
| Singapore tax residence | 183 days | Foreigner who stayed or worked in Singapore at least 183 days in the previous calendar year, or 3 consecutive years, or employment straddling 2 years totalling 183 days | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates |
| Singapore resident rate on the first S$1,000,000 | S$199,150 | Gross tax on the first S$1,000,000 of chargeable income | same |
| Singapore resident top rate | 24% | Chargeable income above S$1,000,000 | same |
| Singapore non-resident employment income | 15% flat or resident rates, whichever is higher | Non-resident individual | same |
| Singapore overseas income of individuals | Generally not taxable | Overseas income received in Singapore by an individual, including deposits into a Singapore account | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/income-received-from-overseas |
| Singapore ABSD, foreigner buying any residential property | 60% | Of the price or market value, whichever is higher | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer's-stamp-duty-(absd) |

## The base

### Part 1: the Chinese side, domicile is the whole question

China's IIT law taxes two classes of people on **worldwide income** (IIT Law art. 1):
1. individuals **domiciled** in China, and
2. non-domiciled individuals who reside in China **183 days or more** in a year (with the six-year concession for foreigners, an *inbound* rule irrelevant here).

**Domicile is not an address.** Under the Implementing Regulations art. 2, a person is domiciled if they **habitually reside** in China by reason of **household registration (hukou), family, or economic interests**. For a Chinese citizen this means: keeping your hukou, a spouse or dependants in China, the operating business in Shenzhen, the apartments in Shanghai; any dense combination keeps you *domiciled*, and therefore **worldwide-taxable, regardless of how many days you spend in Singapore**.

Consequences worth stating plainly:
- Moving your body is not an exit. A founder who relocates to Singapore while the family, the hukou and the main company stay in China has, on the letter of the law, changed nothing about their Chinese tax position.
- **There is no formal "tax de-registration certificate" for citizens leaving**, and hukou cancellation is generally tied to acquiring foreign citizenship or permanent residence abroad and is administratively serious. A genuine exit is a *pattern of severed facts* (family relocated, habitual residence abroad, economic centre shifted) built and documented over time.
- **The treaty helps at the margin, not at the core.** The China-Singapore treaty tie-breaker (art. 4: permanent home, then centre of vital interests, then habitual abode, then nationality) can allocate residence to Singapore for a dual resident; but a Chinese national whose vital interests genuinely moved is exactly the person who has done the severing work anyway; the treaty does not rescue a paper move.

**The CRS reckoning.** Singapore banks and brokers report accounts of Chinese tax residents to China under CRS. Chinese bureaus have used this data to assess residents' **offshore investment income and gains (20%)**, with late payment surcharges for back years. Two corridor implications: (a) offshore accounts opened while still Chinese-resident are visible history, not a hiding place; (b) the account's self-certified tax residency must be *changed* to Singapore once the move is real, and must be *true* when changed, because a false self-certification compounds the problem in both countries.

### Part 2: what China keeps taxing after a real exit

Even for a genuinely non-domiciled, non-resident former mover, Chinese-source items stay Chinese:

- **Chinese company dividends**: 20% IIT domestically, capped at **10%** under the Singapore treaty for an individual beneficial owner resident in Singapore. The 5% cap is for a Singapore company holding at least 25%. Correction: the old file said the domestic withholding on individuals was 10%; the domestic rate is 20% and the 10% is the treaty cap.
- **Selling the Chinese apartments**: 20% on the gain (with local practice on deductions and the exemptions for long-held family homes; detail in `cn-iit`); rental income taxed at source.
- **Selling the Chinese company**: equity transfers of PRC companies are PRC-taxable for non-residents (individuals 20% on the gain; enterprise withholding in `cn-withholding`), and **indirect** transfers (selling the offshore holding company that owns the PRC company) are reachable under **STA Bulletin 2015 No. 7** if the arrangement lacks a reasonable business purpose. Restructure with advice, not with a diagram from the internet.
- **Employment income for China work-days**: sourced to China regardless of where paid.

**Getting the money out is its own project.** The individual foreign exchange quota (**USD 50,000 per person per year**) and SAFE rules make large transfers a multi-year, documentation-heavy exercise through lawful channels (property-sale repatriation with tax clearance, dividend routes, ODI structures for businesses). Plan liquidity **years** ahead of the move; never touch informal exchange channels: they convert a tax problem into a criminal one in both jurisdictions at once.

### Part 3: the Singapore side (short)

- **Residence**: 183 days in the previous calendar year (or the other IRAS tests in the rates table) makes a foreigner resident; progressive rates to **24%** above S$1,000,000 of chargeable income.
- **Capital gains**: Singapore does not tax capital gains as such; portfolio gains, crypto disposals and the exit from a startup are generally outside tax unless you are trading as a business (not confirmed on an IRAS page in this pass; see Sources).
- **Overseas income for individuals**: overseas income received in Singapore by an individual is generally not taxable (IRAS). Corporate rules differ: the s10L foreign-gains rules target entities, not individuals.
- **No estate duty and no wealth tax** in Singapore (abolition date not confirmed in this pass); property taxes and ABSD on residential purchases do that work instead. Budget **ABSD for foreigners at 60%** on residential property; permanent residents and citizens pay far less; many movers rent first for this reason alone.
- **Employment Pass, ONE Pass, PR** are the immigration gates; the family-office regimes (13O/13U) still work but with tightened minimums and hiring conditions: a structure decision, not a default. Their current figures are not restated here.
- CPF applies to citizens and PRs only; there is no Singapore tax trap waiting in the corridor. The whole game is the Chinese side.

## Deadlines and filing

**Sequenced checklist**

**Two-plus years before**
1. Map the domicile facts: hukou, family location, main business, property. Decide what genuinely moves and when: this list *is* the exit plan.
2. Start lawful liquidity planning against the USD 50,000 a person a year quota and SAFE routes; sequence any property sales with tax clearance and repatriation paperwork.
3. Structure review of the operating business: direct versus offshore holding, Bulletin 7 exposure, dividend policy while still resident (dividends now are 20%; after a real exit, 20% capped at 10% by the treaty).

**The move years**
4. Relocate the family and habitual residence; document leases, schools, days.
5. Establish Singapore residence (183 days), get the IRAS tax residence status, and update **every** financial institution's CRS self-certification to Singapore, truthfully.
6. File Chinese returns correctly during the transition years (China-source items; worldwide while still domiciled or resident). For a resident, foreign income is declared 1 March to 30 June of the next year (IIT Law art. 13); for 2026 income, by 30 June 2027. Respond to any CRS-driven bureau letters with advisers, never with silence.

**After**
7. Keep China work-days low and logged; treaty-source employment income properly.
8. Before any liquidity event in the PRC company, re-check Bulletin 7 and the withholding position. Before returning (some do), remember the six-year clock is for foreigners: a returning citizen is simply domiciled again.

## Penalties and interest

China: unpaid tax carries a late payment surcharge of 0.05% a day from the due date (Tax Collection Law art. 32), so back-year offshore income assessed through CRS carries years of surcharge; concealment and false filing carry fines of 50% to 5 times the tax under art. 63, and possible criminal referral (art. 77). Singapore penalties are not covered here.

## Cross-border points

### The trap list

| Trap | Why it bites |
| --- | --- |
| "I'm in Singapore 300 days a year, so I'm out" | Domicile, not day-count, drives worldwide liability for Chinese citizens; hukou, family and business in China keep you fully taxable. |
| Offshore account opened while Chinese-resident, never declared | CRS has delivered it to your bureau already; assessments charge the 20% with surcharge. Regularise with advice, don't wait. |
| Changing the bank's tax-residency box before the move is real | A false self-certification is its own offence and unravels treaty claims later. |
| Selling the offshore HoldCo that owns the PRC OpCo "tax-free" | Bulletin 7 taxes indirect transfers without a reasonable business purpose; buyers withhold or the seller wears the assessment. |
| Underground money changers to beat the USD 50,000 quota | Converts a planning problem into criminal exposure in both countries simultaneously. |
| Buying the Singapore condo on arrival | 60% ABSD for foreigners; rent until PR (or restructure the housing plan entirely). |
| Assuming Singapore taxes nothing ever | Singapore employment and local business income is taxed up to 24%; territorial is not a tax-free life. |
| Treating the treaty tie-breaker as an escape hatch | It only helps a dual resident whose vital interests genuinely moved, that is someone who already did the hard part. |

## Two worked examples that recompute

**Example 1: Singapore tax on a mover's first full year.** A mover becomes Singapore resident and has chargeable income of S$1,200,000 (salary from a Singapore employer). Tax: S$199,150 on the first S$1,000,000, plus 24% of S$200,000 = S$48,000; total S$247,150.

```oa-check
name: SG resident tax on S$1.2m chargeable income
inputs:
  chargeable: 1200000
steps:
  - first_million: 199150
  - excess: (chargeable - 1000000) * 0.24
  - tax: first_million + excess
expected:
  excess: 48000
  tax: 247150
```

**Example 2: decision, take the dividend before or after a real exit.** A founder's Chinese operating company will pay a 2,000,000 yuan dividend. Option A, paid while the founder is still domiciled in China: 20% IIT = 400,000 yuan (and the founder may still owe Chinese tax on Singapore income too). Option B, paid after a genuine exit, with treaty residence in Singapore and a treaty claim filed: China withholds at most 10% = 200,000 yuan; Singapore does not tax the overseas dividend received by an individual. Waiting for a real exit saves 200,000 yuan. The deciding facts are whether the exit is real (domicile facts) and whether the treaty claim is filed; a paper move gets Option A's result plus penalties.

```oa-check
name: CN dividend before or after exit, 20% domestic vs 10% treaty cap
inputs:
  dividend: 2000000
steps:
  - before_exit: dividend * 0.20
  - after_exit: dividend * 0.10
  - saving: before_exit - after_exit
expected:
  before_exit: 400000
  after_exit: 200000
  saving: 200000
```

## Ask the client first

1. Hukou: kept or cancelled; any foreign citizenship or permanent residence obtained.
2. Where the spouse and dependants live, and from when.
3. The operating business: where it is, who owns it, direct or through an offshore holding company.
4. Chinese property kept or sold, and plans for the proceeds.
5. Offshore accounts: when opened, whether income on them was declared in China.
6. Days in China and in Singapore in 2025 and 2026, and the Singapore immigration route.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| PRC IIT Law, STA Shanghai policy library. Read for arts. 1, 3, 7 and 13 (residence, 20% rate, foreign credit, foreign income filing) | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html | 2026-11-14 |
| IIT Implementing Regulations, STA Shanghai. Read for art. 2, domicile as habitual residence by reason of hukou, family or economic interests | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443213.html | 2026-11-14 |
| MOF and STA announcement 2019 No. 34, STA Shanghai. Read for the six-year rule and its 2019 start | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201904/t444837.html | 2026-11-14 |
| China-Singapore tax treaty (2007), STA Guangdong PDF. Read for art. 4 tie-breaker, art. 10 dividend caps 5% and 10%, art. 11 interest 10% | https://guangdong.chinatax.gov.cn/gdsw/gzsw_zcq_zczy_tysc/2021-09/16/2421a19f85e74408a85aa43f2bb50609/files/ca9c3ec21241453290b3ab48b235b4a4.pdf | 2026-11-14 |
| STA Bulletin 2015 No. 7 on indirect transfers, STA Shanghai. Read for the reasonable business purpose test | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/ssxd/201502/t412657.html | 2026-11-14 |
| Tax Collection Administration Law, STA Shanghai. Read for arts. 32, 63 and 77 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html | 2026-11-14 |
| SAFE implementing rules for individual foreign exchange (PDF on safe.gov.cn). Read for art. 2, the annual total of 等值 5 万美元 a person | https://www.safe.gov.cn/neimenggu/file/file/20170728/b94fb1d6db30472584863040ecb838f3.pdf | 2026-11-14 |
| IRAS, individual income tax rates. Read for the residence tests, the S$199,150 on the first S$1,000,000, the 24% top rate and the non-resident 15% rule | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates | 2026-11-14 |
| IRAS, income received from overseas. Read for overseas income of individuals generally not taxable | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/income-received-from-overseas | 2026-11-14 |
| IRAS, ABSD. Read for the 60% rate for foreigners | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer's-stamp-duty-(absd) | 2026-11-14 |

Not yet confirmed: Singapore's treatment of capital gains and the estate duty abolition date (the IRAS pages tried returned only the site shell); the 13O/13U family office minimums; any official STA statement of the size or dates of CRS-based assessment campaigns (the old file said "2024 to 2025"; no official page read).

*Built for the OpenAccountants migration desk. The origin country's claim doesn't end at the border, it ends where your facts end: household registration, family, the operating business. Move the facts, paper the timeline, respect the currency rules, and Singapore's side is the easiest landing in this collection.*
