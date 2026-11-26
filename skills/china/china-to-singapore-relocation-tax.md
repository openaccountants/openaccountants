---
name: china-to-singapore-relocation-tax
description: "Use this skill for a Chinese citizen or long-term China resident moving to Singapore in 2026. Covers domestic and treaty residence, CRS reporting, Chinese dividends (20% domestic, 10% treaty cap for eligible individuals), China-source property and equity gains, the USD 50,000 annual simplified currency-conversion allowance, and Singapore income tax and property stamp duty. Built from the law, not reviewed by an accountant."
version: "2.1"
jurisdiction: CN
tax_year: 2026
tax_year_notes: "China calendar tax year 2026; Singapore Year of Assessment 2027 (income of calendar 2026). Singapore rates are those IRAS shows as current."
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: cross-border
type: situation-rules
---

# China to Singapore: tax residence, investments and reporting

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by qualified professionals in China and Singapore.

## Who this applies to

**Who it's for.** Chinese-tax-connected individuals (citizens and long-term residents) moving to Singapore in 2026, and their advisers. A move can change domestic and treaty residence on different dates. Keep records of the facts that determine each and check the rules for each source of income.

Not covered here: inbound foreigners moving to China (`cn-iit`, `cn-cross-border`), Hong Kong (`hong-kong` pack), the full Chinese computation (`cn-iit`) and company-level withholding (`cn-withholding`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| China residence by days | 183 days | A person without domicile in China is resident if present 183 days or more in the tax year (IIT Law art. 1) | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html |
| China IIT on dividends, interest, property transfer gains, rental | 20% | Ordinary statutory rate under IIT Law art. 3(3). Reduced rates, exemptions and treaties can apply. Qualifying individual housing rent has a 10% rate | same |
| China foreign tax credit | Up to the PRC tax on the foreign income | Resident individuals (IIT Law art. 7) | same |
| Six-year rule for individuals without Chinese domicile | 183 days in the current year and in each of the previous six years, with no single absence over 30 days during those six years | Count years from 2019. If a previous year falls short or has an absence over 30 days, qualifying foreign-source income paid abroad can be exempt, subject to filing | https://fgk.chinatax.gov.cn/zcfgk/c102416/c5202334/content.html |
| China-Singapore treaty, dividends to a company holding 25% or more | 5% cap | Eligible beneficial owner is a company (excluding partnerships) directly holding at least 25% of the capital (art. 10(2)(a)) | https://guangdong.chinatax.gov.cn/gdsw/gzsw_zcq_zczy_tysc/2021-09/16/2421a19f85e74408a85aa43f2bb50609/files/ca9c3ec21241453290b3ab48b235b4a4.pdf |
| China-Singapore treaty, dividends in other cases (individuals) | 10% cap | Eligible beneficial owner is a Singapore treaty resident (art. 10(2)(b)) | same |
| China-Singapore treaty, interest | 10% cap | Residual category for qualifying beneficial owners, subject to art. 11 exceptions | same |
| Simplified foreign exchange allowance | USD 50,000 equivalent per person per year | Separate allowances for individual FX settlement and domestic individuals' FX purchases. Documented current-account transactions can proceed outside the allowance. Capital transfers follow separate rules | https://www.safe.gov.cn/tianjin/2026/0706/3085.html |
| Singapore tax residence | 183 days | Foreigner who stayed or worked in Singapore at least 183 days in the previous calendar year, or stayed or worked continuously for 3 consecutive years. A separate concession covers continuous employment straddling 2 calendar years with at least 183 days of qualifying stay. Directors, public entertainers and professionals are excluded from the 2-year concession | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates |
| Singapore resident rate on the first S$1,000,000 | S$199,150 | Gross tax on the first S$1,000,000 of chargeable income | same |
| Singapore resident top rate | 24% | Chargeable income above S$1,000,000 | same |
| Singapore non-resident employment income | 15% flat or resident rates, whichever is higher | Taxable employment income. Non-resident short-term employment of 60 days or less can be exempt, subject to exceptions | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency |
| Singapore overseas income of individuals | Generally not taxable | Overseas income received by an individual, subject to exceptions such as income through a Singapore partnership or overseas duties incidental to Singapore employment | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/income-received-from-overseas |
| Singapore ABSD, foreigner buying any residential property | 60% | Of the price or market value, whichever is higher, subject to applicable remissions | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer's-stamp-duty-(absd) |

## The base

### Part 1: Chinese domestic residence, treaty residence and CRS

China's IIT Law art. 1 generally taxes residents on worldwide income. A person is resident if domiciled in China or, without domicile, present for at least **183 days** in the tax year. The six-year exemption for eligible foreign-source income applies to people without Chinese domicile who meet its conditions.

**Domicile.** IIT Implementing Regulations art. 2 asks whether the individual habitually resides in China by reason of household registration (hukou), family or economic interests. Those facts inform the test on departure and return. If the individual cancels their Chinese hukou on emigrating, settle Chinese tax before cancelling it (IIT Law art. 13).

**Treaty residence.** For a dual resident, art. 4 first looks for a permanent home. With a home in both countries, it considers the centre of vital interests. If that test is inconclusive or there is no permanent home in either country, the next tests are habitual abode, nationality and finally agreement between the authorities. Treaty residence can limit China's taxing rights even if the person remains resident under China's domestic rules.

**CRS.** Singapore financial institutions report eligible accounts to IRAS for exchange with reportable jurisdictions, including China. Give each institution every jurisdiction where you are currently tax resident and update the information when it changes. Determine whether any offshore income needs to be reported in China under the rules for that income.

### Part 2: Chinese-source income after the move

- **Chinese company dividends** use the ordinary domestic rate of 20%. The treaty caps China's tax at **10%** of gross dividends for an eligible individual beneficial owner resident in Singapore. A separate 5% cap applies to qualifying corporate holders with at least 25% direct ownership. Check effective connection and treaty entitlement before claiming either cap.
- **Chinese real estate** can be taxed in China under treaty art. 13(1). The ordinary 20% rate is on the taxable gain after basis and reasonable expenses. Check the relief for long-held sole family homes. Qualifying individual housing rent is taxed at 10%.
- **Equity disposals** can attract the domestic 20% individual rate on the taxable gain. For a Singapore treaty resident, art. 13(4) permits taxation in China on shares deriving more than 50% of their value from Chinese immovable property. Subject to that rule, art. 13(5) permits China to tax gains on shares or other equity in a Chinese resident entity if the seller held at least 25%, directly or indirectly, at any time in the preceding 12 months. Art. 13(6) reserves other gains covered by that paragraph to the seller's treaty residence.
- **Indirect disposals** by non-resident enterprises can be recharacterised under STA Bulletin 2015 No. 7 when the statutory conditions are met. Analyse an individual's offshore company sale under the IIT Law, including the anti-avoidance rule in art. 8 where relevant, and the treaty.
- **Employment exercised in China** is generally China-source regardless of where paid. Art. 15(2) can reserve taxation to Singapore if presence in China does not exceed 183 days in any 12 months, the employer is non-resident in China and no Chinese permanent establishment or fixed base bears the pay.

**Currency transfers.** The USD 50,000 annual simplified conversion allowance is available for individual FX settlement and separately for domestic individuals' purchases. Banks may process bona fide current-account purchases with supporting documents outside the allowance. Capital transactions have their own rules. A qualifying emigrant transferring personal property applies to the SAFE office for their former hukou location. Use licensed channels. Illegal currency trading and unlicensed remittance can carry penalties depending on the conduct and jurisdiction.

### Part 3: Singapore tax and residency

- The Singapore resident rate reaches **24%** on chargeable income above S$1,000,000. Apply the tax-residency rules for the year in the rates table.
- Gains on personal investment disposals are generally outside income tax. Trading or other income-generating disposals can be taxable. Check the facts of securities, crypto and founder exits.
- Overseas income received by individuals is generally exempt, subject to the exceptions in the rates table. The s10L rules for foreign asset gains apply to entities in relevant groups.
- Estate duty was removed for deaths on and after 15 February 2008. The general foreign-buyer ABSD rate on Singapore residential property is **60%**, subject to applicable remissions. Citizen and permanent resident rates depend on the number of properties and the purchaser's status.
- The Employment Pass, ONE Pass and permanent residence are possible immigration routes. Family-office incentives under sections 13O and 13U have separate eligibility conditions.
- Ordinary mandatory CPF contributions apply to employed Singapore citizens and permanent residents.

## Deadlines and filing

**Before the move**

1. Map the domicile facts, including hukou, family location, business and habitual residence.
2. Plan the currency transfer against the transaction type, required documents and any approval.
3. Check who will sell any shares, the treaty capital gains rules and when dividend relief can apply.

**During the move**

4. Keep evidence of homes, family location and days. Assess domestic and treaty residence separately.
5. Update financial institutions' CRS self-certifications with all applicable jurisdictions.
6. File Chinese returns for the applicable Chinese and foreign income. Under IIT Law art. 13, residents file qualifying foreign income from 1 March to 30 June of the following year. For 2026, the deadline is **30 June 2027**. If cancelling hukou on emigrating, settle Chinese tax before cancellation.

**After the move**

7. Record Chinese work days, the employer's residence and who bears the cost for treaty purposes.
8. Before a disposal or return, reassess the treaty, Chinese tax residence and any applicable corporate or individual anti-avoidance provisions.

## Penalties and interest

China charges a late payment surcharge of **0.05% per day** from the day after the payment deadline through the day of payment (Tax Collection Administration Law art. 32 and Implementing Regulations art. 75). Tax evasion under art. 63 can attract a fine of **50% to five times** the unpaid or underpaid tax. Art. 77 requires referral if a crime is suspected.

## Cross-border points

| Check | Why it matters |
| --- | --- |
| Chinese residence after a move | The answer depends on habitual residence and, where the person has no Chinese domicile, the statutory day count. |
| Reporting offshore accounts and income | Financial institutions and individual taxpayers have separate reporting obligations. Correct inaccurate declarations and apply the tax rules for each income category. |
| Sale of a holding company | Identify the seller and apply the relevant domestic law and treaty provisions. |
| Buying a Singapore home | The ordinary foreign-buyer ABSD rate is 60%. Check all purchasers' status and any applicable remissions. |

## Two worked examples that recompute

**Example 1: Singapore tax on a mover's first full year.** A mover becomes Singapore resident and has chargeable income of S$1,200,000 (salary from a Singapore employer). Tax: S$199,150 on the first S$1,000,000, plus 24% of S$200,000 = S$48,000; gross YA 2027 tax S$247,150 before any applicable rebate.

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

**Example 2: dividend before or after qualifying for treaty relief.** A founder directly holds ordinary shares in a Chinese operating company, which pays a CNY 2,000,000 dividend. Before qualifying for Singapore treaty relief, ordinary Chinese IIT at 20% is CNY 400,000. Once the founder qualifies as a Singapore treaty resident and an eligible beneficial owner and claims relief, the 10% treaty cap limits Chinese tax to CNY 200,000. Assume the qualifying overseas dividend is received directly as an individual and exempt in Singapore. At the treaty cap, the difference is CNY 200,000. Treaty eligibility and the actual receipt determine the result.

```oa-check
name: CN dividend at the 20% domestic rate or 10% treaty cap
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
| China IIT Law, arts. 1, 3, 6, 7, 8 and 13 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html | 2026-11-27 |
| China IIT Implementing Regulations, arts. 2–4 and 20–22 | https://www.chinatax.gov.cn/chinatax/n810219/n810744/n3752930/n3752974/c3963364/content.html | 2026-11-27 |
| STA explanation of domicile and habitual residence | https://www.chinatax.gov.cn/n810356/n3255681/c4251584/content.html | 2026-11-27 |
| MOF and STA Announcement 2019 No. 34, six-year rule | https://fgk.chinatax.gov.cn/zcfgk/c102416/c5202334/content.html | 2026-11-27 |
| China-Singapore tax treaty as modified by the MLI, arts. 4, 10, 11, 13 and 15 | https://www.iras.gov.sg/media/docs/default-source/dtas/singapore-china-dta-%28ratified%29%28mli%29%281-sep-2022%29.pdf | 2026-11-27 |
| STA treaty relief procedure | https://www.chinatax.gov.cn/n810356/n3255681/c5220459/content.html | 2026-11-27 |
| STA Bulletin 2015 No. 7, indirect disposals by non-resident enterprises | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/ssxd/201502/t412657.html | 2026-11-27 |
| China Tax Collection Administration Law, arts. 32, 63 and 77 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html | 2026-11-27 |
| Implementing Regulations, art. 75, surcharge period | https://fgk.chinatax.gov.cn/zcfgk/c100010/c5195082/content.html | 2026-11-27 |
| Cai Shui 2008 No. 24, individual housing rental | https://fgk.chinatax.gov.cn/zcfgk/c102416/c5203346/content.html | 2026-11-27 |
| SAFE 2020 current-account rules, arts. 55–56, FX conversion allowance | https://www.safe.gov.cn/tianjin/2026/0706/3085.html | 2026-11-27 |
| SAFE emigrant property transfer | https://www.safe.gov.cn/tianjin/2026/0319/3018.html | 2026-11-27 |
| IRAS individual income tax rates | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates | 2026-11-27 |
| IRAS tax residence and short-term employment exemption | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency | 2026-11-27 |
| IRAS income received from overseas | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/income-received-from-overseas | 2026-11-27 |
| IRAS gains on disposals | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/gains-from-sale-of-property-shares-and-financial-instruments | 2026-11-27 |
| IRAS s10L guidance, foreign asset gains | https://www.iras.gov.sg/docs/default-source/e-tax/tax-treatment-of-gains-or-losses-from-the-sale-of-foreign-assets.pdf | 2026-11-27 |
| IRAS estate duty | https://www.iras.gov.sg/taxes/other-taxes/estate-duty/estate-duty/ | 2026-11-27 |
| IRAS additional buyer's stamp duty | https://www.iras.gov.sg/taxes/stamp-duty/for-property/buying-or-acquiring-property/additional-buyer's-stamp-duty-(absd) | 2026-11-27 |
| IRAS CRS self-certification | https://www.iras.gov.sg/taxes/international-tax/common-reporting-standard-%28crs%29/basic-information-for-account-holders-of-financial-institutions | 2026-11-27 |
| IRAS CRS list of reportable jurisdictions | https://www.iras.gov.sg/docs/default-source/uploadedfiles/pdf/list-of-reportable-jurisidictions.pdf | 2026-11-27 |
| MAS family-office fund tax incentives | https://www.mas.gov.sg/schemes-and-initiatives/fund-tax-incentive-scheme-for-family-offices | 2026-11-27 |
