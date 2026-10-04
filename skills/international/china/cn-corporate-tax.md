---
name: cn-corporate-tax
description: "当被问及中国企业所得税（CIT）相关事宜时使用本技能。触发关键词包括：\"中国企业所得税\"、\"CIT 25%\"、\"小型微利企业\"、\"高新技术企业 15%\"、\"研发费用加计扣除 200%\"、\"年度汇算清缴企业所得税\"、\"季度预缴企业所得税\"、\"海南自贸港 15%\"、\"横琴粤澳 15%\"、\"非居民企业预提所得税\"、\"支柱二 全球最低税\"。覆盖《中华人民共和国企业所得税法》25%标准税率、小型微利企业优惠（应纳税所得额≤300万元部分实际税负5%）、高新技术企业15%税率、技术先进型服务企业15%、研发费用加计扣除（一般及制造业100%加计、集成电路与工业母机120%加计）、区域性税率优惠（海南、横琴、前海、上海临港、西部大开发）、非居民企业预提所得税、反避税与转让定价、季度预缴与5月31日前年度汇算清缴。Trigger also on: \"China CIT\", \"China corporate income tax\", \"small low-profit enterprise China\", \"HNTE 15%\", \"R&D super deduction\", \"advanced technology service enterprise\", \"Hainan Free Trade Port 15%\", \"Hengqin 15%\", \"China withholding tax\", \"China Pillar Two GloBE\". 不在范围：个人所得税（见 china-pit）、增值税（见 china-vat）、消费税、关税、契税、印花税、土地增值税、银行/保险/石油/采矿特殊行业、合并纳税、信托与合伙企业穿透、税收居民身份认定争议。在处理任何中国企业所得税事项前，必须先阅读本技能。"
jurisdiction: CN
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# China Enterprise Income Tax (企业所得税): rates, small low-profit enterprises, HNTE and regional 15%, R&D super-deduction, withholding, losses and filing for 2026

## Scope and who this is for ([CIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html))

This Guide covers mainland China Enterprise Income Tax (CIT, 企业所得税) for tax year 2026, which is the calendar year 1 January to 31 December 2026. It is for companies and other enterprises, and for their advisers, who prepare or review quarterly prepayments, the annual settlement (汇算清缴) or withholding on payments to non-residents.

The legal base is the **Enterprise Income Tax Law (中华人民共和国企业所得税法)**, as last amended on 29 December 2018, and its **Implementation Regulations (企业所得税法实施条例, State Council Decree No. 512)**. Most of the reliefs that matter in practice sit in announcements from the Ministry of Finance (MOF) and the State Taxation Administration (STA). Several of them expire on 31 December 2027, so check the end date of every relief you apply.

Who pays:
- **Resident enterprises** are enterprises set up under Chinese law, or foreign-law enterprises whose place of effective management is in China. They pay tax on their worldwide income (Law Art. 2-3).
- **Non-resident enterprises with an establishment in China** pay tax on income connected with that establishment (Law Art. 3).
- **Non-resident enterprises without an establishment**, or whose income is not connected with one, pay on China-source income by withholding at source (Law Art. 3, 37).
- Sole proprietorships and partnerships are **not** CIT taxpayers (Law Art. 1). Their owners fall under individual income tax.

Currency: tax is computed in renminbi. Income in foreign currency is converted to renminbi (Law Art. 56).

Out of scope: Hong Kong, Macao and Taiwan; individual income tax; VAT and surcharges; banks, insurers, securities firms, oil, gas and mining; cross-region consolidated filing by head offices and branches; special tax treatment of reorganisations; tax audits and disputes; and Pillar Two. See "When to refuse or refer".

## What is new or confirmed for 2026 ([MOF/STA announcement 2023 No. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html); [MOF/STA announcement 2025 No. 16](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202601/t478898.html); [STA announcement 2025 No. 17](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202507/t477034.html); [Hainan Tax Bureau 2025 No. 2](https://hainan.chinatax.gov.cn/xxgk_6_1/14160619.html))

| Topic | Position for 2026 | Source |
|---|---|---|
| Standard rate | 25%, unchanged | Law Art. 4 |
| Small low-profit enterprise | Taxable income reduced to 25% and taxed at 20%. The announcement extends this to 2027-12-31 | MOF/STA announcement 2023 No. 12 Art. 3 |
| R&D super-deduction | Extra 100% of actual R&D cost, or 200% amortisation where an intangible asset is created, from 2023-01-01 with no end date | MOF/STA announcement 2023 No. 7 |
| IC and machine-tool enterprises | Extra 120%, or 220% amortisation, from 2023-01-01 to 2027-12-31 | MOF/STA announcement 2023 No. 44 |
| Western region | 15% for encouraged-industry enterprises from 2021-01-01 to 2030-12-31 | MOF/STA/NDRC 2020 No. 23 |
| Hainan Free Trade Port | 15% for encouraged-industry enterprises with substantive operations. The current extension runs from 2025-01-01 to 2027-12-31 | Hainan Tax Bureau 2025 No. 2 |
| Advertising cap | New announcement from 2026-01-01 to 2027-12-31: 30% cap for cosmetics manufacturing or sales, pharmaceutical manufacturing and beverage manufacturing (excluding alcohol); related enterprises with a cost-sharing agreement may shift deductible amounts between them; tobacco advertising is never deductible | MOF/STA announcement 2025 No. 16 |
| Prepayment return | Revised A-type monthly or quarterly prepayment return, used from 2025-10-01 | STA announcement 2025 No. 17; Shanghai Tax Bureau Q&A |

## Ask the client first

- **Residence and structure.** Is the entity a resident enterprise? Is it a legal person, or a branch? Branches without legal personality are combined with head office for every test in this Guide ([STA announcement 2023 No. 6 Art. 1](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202303/t466615.html)).
- **Industry.** Is the business in a restricted or prohibited industry (small low-profit test)? Is it in an R&D negative-list industry, such as tobacco, hotels and catering, wholesale and retail, real estate, leasing and business services, or entertainment ([Caishui 2015 No. 119](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201511/t419949.html))?
- **Size, measured as quarterly averages for the year.** What are the headcount (employees plus labour-dispatch workers) and total assets? What is the expected taxable income for 2026?
- **Certificates and lists.** Does it hold an HNTE certificate, and what is the issue date on it? Is it a registered technology-based SME? Is it on the IC or machine-tool enterprise list?
- **Location.** Is it registered and substantively operating in a western-region province or in the Hainan Free Trade Port? What share of revenue does its encouraged-industry main business provide?
- **R&D records.** Are R&D costs kept in a separate ledger for each project? Were any R&D projects commissioned from overseas?
- **Losses.** What losses from each of 2021 to 2025 remain unused, and was the company an HNTE or technology-based SME in any of those years?
- **Cross-border payments.** Does it pay dividends, interest, royalties, rent or other China-source income to non-residents? Does the recipient claim a tax treaty?
- **Prepayments.** Is it on monthly or quarterly prepayment, how much has been prepaid for 2026, and which method does it use (actual profit or another approved method)?
- **Open matters.** Is there any audit, notice from the tax bureau, reorganisation, group consolidation or Pillar Two exposure? If yes, see "When to refuse or refer".

## The method, step by step

1. **Confirm the taxpayer type.** A resident enterprise is taxed on worldwide income at 25%. A non-resident without an establishment is taxed by withholding (step 9) ([CIT Law Art. 3-4](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html)).
2. **Start from accounting profit and build taxable income.** Taxable income = total income − non-taxable income − exempt income − deductions − losses allowed to be carried forward ([CIT Law Art. 5](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html)). Income is recognised on an accrual basis ([Implementation Regulations Art. 9](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html)).
3. **Remove non-taxable and exempt income.** Non-taxable income is fiscal appropriations, administrative fees and government funds, and other income the State Council designates (Law Art. 7). Exempt income includes treasury bond interest and qualifying dividends between resident enterprises (Law Art. 26). The dividend exemption does not cover shares of a listed resident company held continuously for less than 12 months, and it does not apply to distributions from partnerships or foreign enterprises ([Shanghai Tax Bureau Q&A, 2026](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202604/t479958.html)).
4. **Apply the capped deductions.** See "Capped deductions and other income rules": business entertainment, advertising, donations and staff education.
5. **Add the R&D super-deduction** if the conditions are met (see "R&D super-deduction").
6. **Offset losses** from the previous 5 years (10 for HNTEs and technology-based SMEs, under the conditions below).
7. **Choose the rate.** Use 25% unless the entity has documented eligibility for one preference: small low-profit enterprise, HNTE 15%, western region 15% or Hainan 15%. Apply the preference that gives the lowest tax, and do not stack them on the same income.
8. **Deduct credits and reliefs**, such as foreign tax credits and equipment credits, then compare with the prepayments.
9. **Withholding on non-residents.** On each payment of China-source income to a non-resident without an establishment, the payer withholds at 10% unless a treaty gives a lower rate. The payer pays the tax over within seven days of withholding ([CIT Law Art. 37, 40](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [Implementation Regulations Art. 91](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html)).
10. **File and pay.** Prepay within fifteen days of each quarter end. Settle the year by 31 May 2027 for tax year 2026 (see "Filing and payment").

## Rates for tax year 2026 ([CIT Law Art. 4, 28](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [Implementation Regulations Art. 91](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html))

| Who | Rate | Condition | Source |
|---|---|---|---|
| Resident enterprise (standard) | 25% | Default rate | Law Art. 4 ("企业所得税的税率为25％") |
| Non-resident establishment, connected income | 25% | Income effectively connected with the establishment | Law Art. 3-4 |
| Non-resident without an establishment, China-source passive income | Statutory 20%, **reduced to 10%** | Dividends, interest, rent, royalties, property gains and similar income. A treaty may lower it further | Law Art. 4, 27(5); Regulations Art. 91 ("减按10%的税率征收企业所得税") |
| Small low-profit enterprise | Effectively 5% on all its taxable income | All three size tests met, and not in a restricted or prohibited industry | MOF/STA announcement 2023 No. 12 |
| High and new technology enterprise (HNTE) | 15% | Valid certificate for the year | Law Art. 28 ("减按15％的税率征收企业所得税") |
| Western region encouraged industry | 15% | 2021-2030; main business on the catalogue provides 60% or more of revenue | MOF/STA/NDRC 2020 No. 23 |
| Hainan Free Trade Port encouraged industry | 15% | 2025-2027 extension; substantive operation in Hainan | Hainan Tax Bureau 2025 No. 2 |

Rate formula: tax payable = taxable income × applicable rate − reliefs − credits (Law Art. 22).

## Small low-profit enterprises (小型微利企业) ([MOF/STA announcement 2023 No. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html); [STA announcement 2023 No. 6](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202303/t466615.html))

**The relief.** Taxable income is reduced to 25% of its amount and taxed at 20%. The effective rate is 25% × 20% = 5%. Announcement 2023 No. 12 Art. 3 continues this to 31 December 2027, so it covers tax years 2026 and 2027.

**Who qualifies.** The company must be in an industry that is not restricted or prohibited, **and** meet all three tests at the same time (Art. 5):
- annual taxable income **not over** 300万元 (three million yuan);
- headcount **not over** 300 people;
- total assets **not over** 5000万元 (fifty million yuan).

**It is all-or-nothing.** If taxable income is more than three million yuan, or either size test fails, the company is not a small low-profit enterprise. It then pays the normal rate on its **whole** income. There is no 5% band on the first three million yuan for a larger company.

**How the tests are measured.**
- Headcount includes employees under a labour contract **and** labour-dispatch workers the company uses.
- Headcount and total assets are the average of the four quarters. Each quarter's value = (value at the start of the quarter + value at the end) ÷ 2. The year's value = sum of the quarterly values ÷ 4.
- A company that starts or stops business during the year uses its actual period of operation as the year.
- The final test is the annual settlement. A new company registered as a VAT general taxpayer may claim the relief before its first annual settlement if headcount is 300 or fewer and total assets are 5000万元 or less at the end of the month before filing (Art. 5).
- A company without legal-person branches adds up the head office and all branches for all three tests. A branch cannot claim the relief on its own ([STA announcement 2023 No. 6 Art. 1](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202303/t466615.html); [Shanghai Tax Bureau Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202601/t478977.html)).

**How it is claimed.** The company claims by completing the prepayment and annual returns. No prior application is needed. This relief applies whether tax is assessed on the books or on a deemed basis (STA announcement 2023 No. 6 Art. 2-3). The R&D super-deduction is different: it is only for companies assessed on actual profit (see "R&D super-deduction").

**At prepayment.** Test the figures cumulatively to the end of the period. If a company qualifies part way through the year, it computes the relief cumulatively and sets any earlier overpayment against later prepayments. If it claimed the relief at prepayment but fails at the annual settlement, it pays the difference (Art. 4-6). Small low-profit enterprises prepay **quarterly**. A monthly filer that qualifies at the April, July or October filing moves to quarterly from the next period and stays quarterly for the rest of the year (Art. 7).

## High and new technology enterprises (HNTE, 高新技术企业) at 15% ([CIT Law Art. 28](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [HNTE Administrative Measures, Guokefahuo 2016 No. 32](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201603/t422248.html); [Shanghai Tax Bureau HNTE Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202505/t476449.html))

An HNTE pays 15% instead of 25%. The status comes from a certificate that the provincial science, finance and tax authorities issue jointly. It is not self-assessed.

**Conditions for recognition (Measures Art. 11). All must be met:**
- registered for **at least one year** when it applies;
- owns intellectual property that gives core technical support to its main products or services;
- that technology falls within the State's key supported high-tech fields;
- science and technology staff are **not less than 10%** of total staff for the year;
- R&D spending over the last three accounting years, as a share of sales revenue, is not less than:
  - 5% where sales in the latest year are 5,000万元 (fifty million yuan) or less;
  - 4% where sales are over 5,000万元 and up to 2亿元 (two hundred million yuan);
  - 3% where sales are over 2亿元;
  - and R&D spent in China is not less than 60% of total R&D;
- revenue from high-tech products and services in the latest year is not less than 60% of total revenue;
- the innovation capability assessment meets the required standard;
- no major safety or quality incident and no serious environmental violation in the year before applying.

**Timing.** The certificate is valid for three years from its issue date, and the company then has to be recognised again. The 15% rate applies from the year in which the certificate is issued (Measures Art. 9-10).

**Every year.** The company must still meet the conditions in each year it claims the rate. If it stops meeting them, it cannot use 15% for that year. Keep the evidence (staff ratios, R&D ratios and high-tech revenue) on file.

**HNTE and the small low-profit relief.** Both reduce the rate on the same income, so apply whichever gives the lower tax. For a company that meets the small low-profit tests, the effective 5% beats 15%.

## Regional 15% rates ([MOF/STA/NDRC 2020 No. 23](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202005/t453507.html); [Hainan Tax Bureau 2025 No. 2](https://hainan.chinatax.gov.cn/xxgk_6_1/14160619.html); [Caishui 2020 No. 31](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202009/t455145.html))

**Western region (西部大开发).** From 1 January 2021 to 31 December 2030, an encouraged-industry enterprise located in the western region pays 15%. An encouraged-industry enterprise is one whose main business is a project in the *Catalogue of Encouraged Industries in the Western Region*, and whose main-business revenue is **60% or more** of total revenue. The western region is Inner Mongolia, Guangxi, Chongqing, Sichuan, Guizhou, Yunnan, Tibet, Shaanxi, Gansu, Qinghai, Ningxia, Xinjiang and the Xinjiang Production and Construction Corps. Xiangxi (Hunan), Enshi (Hubei), Yanbian (Jilin) and Ganzhou (Jiangxi) apply the same policy. When the catalogue is revised, the new version applies from its effective date.

**Hainan Free Trade Port (海南自由贸易港).** An encouraged-industry enterprise that is registered in the Hainan Free Trade Port and has substantive operations there pays 15%. The current extension runs from 1 January 2025 to 31 December 2027. The original notice (Caishui 2020 No. 31) set these conditions:
- main-business revenue from the Hainan encouraged-industry catalogue is 60% or more of total revenue;
- the place of effective management is in Hainan, with substantive, comprehensive control of production, staff, accounts and assets there.

If the head office is in Hainan, only the income of the Hainan head office and Hainan branches gets 15%. If the head office is outside Hainan, only a qualifying Hainan branch's income gets 15%. New outbound direct investment made from 2020-01-01 to 2027-12-31 by Hainan tourism, modern services and high-tech enterprises can be exempt, subject to conditions that include a holding of **20% or more** in a foreign subsidiary. Refer these cases.

**Other zones.** Hengqin (Guangdong-Macao), Qianhai (Shenzhen-Hong Kong) and the Lingang New Area (Shanghai) have their own 15% regimes, each with its own catalogue and end date. This Guide does not apply them: refer.

**Conservative default.** Until location, substantive operations and the 60% revenue test are documented, use 25%.

## R&D super-deduction (研发费用加计扣除) ([MOF/STA announcement 2023 No. 7](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202304/t466643.html); [MOF/STA announcement 2023 No. 44](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202309/t468737.html); [Caishui 2015 No. 119](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201511/t419949.html); [Caishui 2018 No. 64](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201807/t440577.html); [Shanghai Tax Bureau R&D Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202111/t461170.html))

| Enterprise | R&D expensed in the year | R&D that creates an intangible asset | Period |
|---|---|---|---|
| All eligible enterprises | Actual cost deducted, **plus** an extra 100% of the actual cost | Amortised on 200% of the asset's cost | From 2023-01-01, no end date |
| Listed IC and machine-tool enterprises | Actual cost deducted, plus an extra 120% | Amortised on 220% of cost | 2023-01-01 to 2027-12-31 |

**Who may claim.** Only resident enterprises that keep sound accounts, are assessed on actual profit (查账征收, not on a deemed basis) and can collect R&D costs accurately may claim. Caishui 2015 No. 119 Part 5(1) says: "本通知适用于会计核算健全、实行查账征收并能够准确归集研发费用的居民企业". A company on deemed (核定) assessment cannot claim.

**Who cannot claim.** Industries on the negative list cannot claim: tobacco manufacturing; accommodation and catering; wholesale and retail; real estate; leasing and business services; entertainment; and any others MOF and STA designate (Caishui 2015 No. 119 Part 4).

**What is not R&D.** Routine upgrades of products or services, direct application of published research results, after-sales technical support, and similar routine work do not qualify (No. 119 Part 1(2)).

**Record-keeping.** Costs must be recorded separately for each project. Costs that cannot be separated from production costs do not qualify for the super-deduction (No. 119 Part 3).

**"Other related costs" cap.** Other related costs (literature, IP fees, travel, meetings and similar) may not exceed 10% of the total eligible R&D cost. Since 2021 the cap has been computed across all projects together: cap = (sum of the five main cost categories) × 10% ÷ (1 − 10%) ([Shanghai Tax Bureau Q&A on STA announcement 2021 No. 28](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202111/t461170.html)).

**R&D commissioned overseas.** 80% of the actual cost counts as the commissioning company's overseas R&D cost. That amount qualifies only up to two-thirds of the company's eligible domestic R&D cost (Caishui 2018 No. 64).

**IC and machine-tool enterprises.** The 120% rate applies only to enterprises on the lists that NDRC, MIIT, MOF and STA compile (2023 No. 44 Art. 2-3). Check the list for the year.

**Conservative default.** If costs are not tracked by project, the industry is on the negative list, or tax is assessed on a deemed basis, do not claim.

## Losses carried forward ([CIT Law Art. 18](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [Caishui 2018 No. 76](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201807/t440878.html))

- **General rule.** A tax loss can be carried forward and set against later profits for up to 5 years. The Law says the carry-forward period "may not exceed five years" (Art. 18). A loss is taxable income below zero, computed under the Law (Regulations Art. 10). There is no carry-back.
- **HNTEs and technology-based SMEs.** From 2018, a company that holds HNTE or technology-based SME status **in a given year** may carry forward unused losses from the 5 years before that year for up to 10 years instead of 5. A technology-based SME must hold a registration number under the technology-based SME evaluation rules (Caishui 2018 No. 76).
- Use losses oldest first, and keep a schedule of each year's loss and use.

## Capped deductions and other income rules ([Implementation Regulations Art. 43-44](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html); [MOF/STA announcement 2025 No. 16](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202601/t478898.html); [Caishui 2018 No. 15](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201803/t436949.html); [Caishui 2018 No. 51](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201805/t439366.html); [MOF/STA announcement 2023 No. 37](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202309/t468599.html))

| Item | Rule | Source |
|---|---|---|
| Business entertainment | 60% of the amount spent, capped at 5‰ of sales (operating) revenue. No carry-forward | Regulations Art. 43 |
| Advertising and promotion (general) | Up to 15% of sales (operating) revenue. The excess carries forward to later years | Regulations Art. 44 |
| Advertising: cosmetics manufacturing or sales, pharmaceutical manufacturing, beverages (not alcohol) | Up to 30% of sales revenue, excess carried forward, for 2026-01-01 to 2027-12-31 | MOF/STA announcement 2025 No. 16 |
| Tobacco advertising | Never deductible | MOF/STA announcement 2025 No. 16 |
| Advertising: related enterprises with a cost-sharing agreement | One party may deduct its own advertising within its cap, or move part or all of it to the other party under the agreement. The other party leaves the amount received out of its own cap calculation | MOF/STA announcement 2025 No. 16 Art. 2 |
| Wages paid to disabled employees | Actual wages deducted, plus an extra 100% of those wages | Regulations Art. 96 |
| Venture capital enterprise investing in an unlisted small or medium HNTE for 2 years or more | 70% of the investment may be set against the venture capital enterprise's taxable income in the year the holding reaches 2 years. Any unused amount carries forward | Regulations Art. 97 |
| Environmental protection, energy and water saving, or work safety equipment on the official catalogues | 10% of the investment is credited against tax payable. Any unused credit carries forward for 5 years. The credit is clawed back if the equipment is transferred or leased out within 5 years | Regulations Art. 100 |
| Charitable donations through qualifying bodies | Up to 12% of annual accounting profit. The excess carries forward three years | Law Art. 9; Caishui 2018 No. 15 |
| Staff education | Up to 8% of total wages. The excess carries forward | Caishui 2018 No. 51 |
| Equipment bought 2024-01-01 to 2027-12-31 | Unit value up to 500万元 (five million yuan) may be deducted in full in the year instead of depreciated | MOF/STA announcement 2023 No. 37 |
| Fines, penalties and late-payment surcharges | Not deductible | Law Art. 10 |
| Supporting documents | If an invoice is missing, it must be obtained before the end of the annual settlement period. An expense of an earlier year that was never deducted can be carried back to the year it arose, for up to five years back, once proper documents are obtained | [Shanghai Tax Bureau Q&A, April 2026](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202604/t480124.html) |

## Withholding on non-residents (源泉扣缴) ([CIT Law Art. 3, 19, 27, 37-40](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [Implementation Regulations Art. 91](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html))

- **Who.** A non-resident enterprise without an establishment in China, or whose China-source income is not effectively connected with its establishment.
- **Rate.** The statutory rate is 20% (Law Art. 4), and Regulations Art. 91 reduces it to **10%**. A tax treaty may reduce it further. Confirm the treaty, the beneficial owner and the documents before applying a lower rate, and refer treaty claims.
- **Base.** For dividends, interest, rent and royalties the base is the gross amount. For property transfers it is the proceeds less the net value of the property (Law Art. 19).
- **Exempt.** Interest on loans from foreign governments to the Chinese government, interest on concessional loans from international financial organisations to the Chinese government and resident enterprises, and other income the State Council approves (Regulations Art. 91).
- **Mechanics.** The payer is the withholding agent. It withholds on each payment, or on the date payment falls due, and pays the tax to the treasury within seven days, filing a withholding report (Law Art. 37, 40). If the payer does not withhold, the non-resident must pay where the income arises (Law Art. 39).
- **Conservative default.** If a cross-border payment's nature is unclear, withhold at 10% and refer.

## Anti-avoidance in brief ([CIT Law Ch. 6](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [Implementation Regulations Art. 118](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html))

- **Transfer pricing.** Related-party transactions must be at arm's length, or the tax bureau may adjust them (Art. 41). An annual related-party transaction report is filed with the annual return (Art. 43). Contemporaneous documentation duties depend on transaction thresholds: refer.
- **Controlled foreign companies.** Profits that a company controlled by resident enterprises (or by them together with Chinese residents) keeps in a country whose effective tax is clearly below the 25% rate, without a genuine business reason, can be taxed on the resident. "Clearly below" means below 50% of the 25% rate (Law Art. 45; Regulations Art. 118).
- **Thin capitalisation.** Interest on related-party debt above the prescribed debt-to-equity ratio is not deductible (Art. 46).
- **General anti-avoidance.** Arrangements without a reasonable commercial purpose can be adjusted (Art. 47). An adjustment carries interest (Art. 48).

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Taxable income exactly 300万元, 300 staff, assets 5000万元 | Qualifies: each test is "not over" | [MOF/STA announcement 2023 No. 12 Art. 5](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html) |
| Taxable income above 300万元 | Not a small low-profit enterprise. Whole income at 25% (or another preference) | MOF/STA announcement 2023 No. 12 Art. 5 |
| Company in a restricted or prohibited industry | No small low-profit relief, whatever its size | MOF/STA announcement 2023 No. 12 Art. 5 |
| Branch without legal personality | Cannot claim the small low-profit relief alone. Combine with head office | [STA announcement 2023 No. 6 Art. 1](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202303/t466615.html) |
| Claimed small low-profit at prepayment, fails at year end | Pay the difference at the annual settlement | STA announcement 2023 No. 6 Art. 6 |
| HNTE certificate issued part way through 2026 | 15% from tax year 2026, the year of issue | [HNTE Measures Art. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201603/t422248.html) |
| HNTE certificate expired and not renewed | 25% from the year it lapses, unless another preference applies | HNTE Measures Art. 9 |
| Western-region company, encouraged business below 60% of revenue | No 15%. Use 25% | [MOF/STA/NDRC 2020 No. 23](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202005/t453507.html) |
| Retailer runs an R&D project | No super-deduction (negative-list industry). The actual cost is still deductible | [Caishui 2015 No. 119](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201511/t419949.html) |
| Overseas R&D above two-thirds of domestic R&D | The excess gets no super-deduction | [Caishui 2018 No. 64](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201807/t440577.html) |
| Loss from 2020 still unused in 2026, ordinary company | Expired after 2025 (5 years) | [CIT Law Art. 18](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) |
| Company is an HNTE in 2026, with an unused 2021 loss | May use it for up to 10 years from 2021 | [Caishui 2018 No. 76](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/201807/t440878.html) |
| Dividend from a listed resident company held less than 12 months | Taxable, not exempt | [Shanghai Tax Bureau Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202604/t479958.html) |
| Dividend from a partnership or foreign company | Not exempt resident-to-resident dividend income | Shanghai Tax Bureau Q&A |
| Royalty paid to a non-resident with no treaty claim | Withhold 10% on the gross amount | [Implementation Regulations Art. 91](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html) |

## Worked cases ([MOF/STA announcement 2023 No. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html); [CIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [MOF/STA announcement 2023 No. 7](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202304/t466643.html); [Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html))

All amounts are in yuan and relate to tax year 2026.

**Case 1: small low-profit enterprise.** A resident technology services company that is not in a restricted industry. Its quarterly-average headcount is 48 and its quarterly-average total assets are 12,000,000 yuan. Accounting profit is 2,600,000. Adjustments: entertainment over the cap +50,000; a non-qualifying donation +30,000; treasury bond interest (exempt) −20,000. Taxable income = 2,600,000 + 50,000 + 30,000 − 20,000 = 2,660,000. All three tests are met (not over three million yuan, 300 staff and fifty million yuan). Tax = 2,660,000 × 25% × 20% = 133,000, an effective 5%. Prepaid 60,000, so 73,000 is due with the annual settlement by 31 May 2027.

**Case 2: just over the income test.** Same company, but taxable income is 3,100,000. It is **not** a small low-profit enterprise. Tax = 3,100,000 × 25% = 775,000. No part of its income is taxed at 5%. If it has an HNTE certificate for 2026, tax = 3,100,000 × 15% = 465,000.

**Case 3: HNTE.** A company whose HNTE certificate was issued in October 2024 (valid until October 2027) has adjusted taxable income of 48,000,000. It still meets the staff, R&D and high-tech revenue ratios for 2026. Tax = 48,000,000 × 15% = 7,200,000. Prepaid 5,000,000, so 2,200,000 is due by 31 May 2027. The certificate is valid for three years from issue, so it lapses in October 2027. The company keeps 15% for tax year 2027 only if it is recognised again, so plan for that during 2027.

**Case 4: R&D super-deduction.** A manufacturing company (not on the negative list, not an HNTE) has accounting profit of 15,000,000, after expensing R&D of 8,000,000 tracked by project. No intangible asset was created. Extra deduction = 8,000,000 × 100% = 8,000,000. Taxable income = 15,000,000 − 8,000,000 = 7,000,000. Tax = 7,000,000 × 25% = 1,750,000. Without the super-deduction, tax would be 15,000,000 × 25% = 3,750,000, so the saving is 2,000,000.

**Case 5: royalty to a non-resident.** A Shanghai company pays a royalty of 1,000,000 to a foreign company that has no establishment in China and makes no treaty claim. Withholding = 1,000,000 × 10% = 100,000. The company pays it to the treasury within seven days of withholding and files the withholding report.

**Case 6: losses.** An ordinary company (never an HNTE or technology-based SME) has 2026 profit of 1,000,000 before losses. It has an unused 2020 loss of 300,000 and an unused 2022 loss of 400,000. The 2020 loss expired after 2025. The 2022 loss is used: taxable income = 1,000,000 − 400,000 = 600,000. If it meets the small low-profit tests, tax = 600,000 × 25% × 20% = 30,000.

## When to refuse or refer

Refer to a Chinese certified tax agent or CPA, and do not finalise, when:
- the entity is a bank, insurer, securities firm, trust, oil or gas producer, or mining company, or is otherwise subject to industry-specific rules;
- head office and branches are in different provinces (cross-region consolidated filing), or the matter is group consolidation;
- the matter is a merger, division, share or asset acquisition claiming special tax treatment, or a reorganisation under [STA announcement 2026 No. 13](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202607/t480970.html);
- there is a tax audit, assessment, notice from the tax bureau, reconsideration or litigation;
- the matter is a permanent establishment, profit attribution, treaty relief or indirect transfer of Chinese property by a non-resident;
- the matter is transfer pricing documentation, an advance pricing arrangement, a CFC, thin capitalisation or a general anti-avoidance adjustment;
- a Hengqin, Qianhai, Lingang, TASE, software or IC tax holiday, or Hainan outbound-investment exemption is claimed;
- **Pillar Two / global minimum tax.** No MOF or STA rule implementing the income inclusion rule, the undertaxed profits rule or a domestic minimum top-up tax could be found on the official hosts at retrieval. If a multinational group within the OECD rules asks, say so and refer. Check the STA policy library for any later announcement;
- the company cannot show its financial statements, prior-year return or loss schedule;
- eligibility for a preference cannot be documented. In that case compute at 25% and flag the preference as pending.

## Filing and payment ([CIT Law Art. 54-55](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [Implementation Regulations Art. 128-129](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html); [STA announcement 2025 No. 17](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202507/t477034.html); [Shanghai Tax Bureau settlement Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202405/t471967.html); [Tax Collection Administration Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html))

**Prepayment (预缴).**
- CIT is prepaid monthly or quarterly, as the tax bureau decides. Small low-profit enterprises always prepay quarterly ([STA announcement 2023 No. 6 Art. 7](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202303/t466615.html)).
- The prepayment return is filed, and the tax paid, **within fifteen days** after the end of each month or quarter (Law Art. 54). For quarterly filers in 2026 that means by mid-April, mid-July and mid-October 2026, and mid-January 2027, subject to the published calendar, which may extend a deadline for public holidays.
- Prepay on actual profit to date. If that is difficult, the company may use one-twelfth or one-quarter of the previous year's taxable income, or another method the tax bureau approves. Once chosen, the method may not be changed at will within the year (Regulations Art. 128).
- Resident enterprises taxed on their books use the revised A-type monthly (quarterly) prepayment return, in use from 1 October 2025 (STA announcement 2025 No. 17; [Shanghai Tax Bureau Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202511/t478219.html)).
- The R&D super-deduction and the small low-profit relief can both be claimed at prepayment, and are confirmed at the annual settlement.

**Annual settlement (年度汇算清缴).**
- Within five months after the year end, file the annual return and settle the balance, whether the company made a profit or a loss and whether or not it is in a tax holiday (Law Art. 54; Regulations Art. 129). For tax year 2026 the deadline is **31 May 2027**. The Shanghai bureau's Q&A shows the same pattern for an earlier year: settlement "在2024年5月31日前" for tax year 2023.
- File the financial statements with the return. File the related-party transaction report where required (Law Art. 43).
- Preferences are self-assessed and claimed on the return. Supporting documents are kept for inspection, not filed in advance ([Shanghai Tax Bureau Q&A, April 2026](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202604/t480124.html)).
- An overpayment can be refunded or set against later tax.
- A company that stops business during the year settles within 60 days of stopping (Law Art. 55; Shanghai settlement Q&A).

**Late payment and penalties** ([Tax Collection Administration Law Art. 32, 62, 63](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html)).
- Late payment: a surcharge of five ten-thousandths (万分之五) of the unpaid tax for each day, from the day the tax became overdue.
- Late filing: the bureau orders correction and may fine up to two thousand yuan. In serious cases the fine is two thousand to ten thousand yuan.
- Tax evasion (false returns, hidden income and the like): the tax and surcharge are recovered, plus a fine of half to five times the unpaid tax. Criminal liability applies where the conduct is a crime.
- Records: keep books, vouchers, returns and other tax records for ten years unless a law says otherwise ([Detailed Rules for the Tax Collection Administration Law, Art. 29](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200402/t284445.html)).

## Returns for tax year 2025 being filed or corrected now ([Shanghai Tax Bureau 2025 settlement Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202604/t479958.html); [CIT Law Art. 54](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html))

The annual settlement for tax year 2025 was due by 31 May 2026. Every resident enterprise that operated in 2025 had to settle, including those that made a loss or were in a tax holiday. On 25 September 2026 that deadline has passed, so any 2025 work is either a correction of a filed return or a late filing:
- a missing 2025 settlement is late, so file at once and expect the daily surcharge and a possible penalty;
- if a 2025 return is wrong, file a correction. Underpaid tax carries the daily surcharge;
- the 2025 rules are the same as those in this Guide for the small low-profit relief, the R&D super-deduction, the western and Hainan 15% rates, HNTE and losses. The advertising rule is different: for 2025 the earlier announcement (MOF/STA announcement 2020 No. 43) applied, and MOF/STA announcement 2025 No. 16 replaced it only from 1 January 2026.

## Completion checklist ([CIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html); [MOF/STA announcement 2023 No. 12](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468162.html); [MOF/STA announcement 2023 No. 7](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/202304/t466643.html); [Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html))

- [ ] Resident or non-resident status confirmed. Legal person or branch identified.
- [ ] Taxable income reconciled from accounting profit, with non-taxable and exempt income removed and caps applied.
- [ ] Small low-profit tests run on quarterly averages (headcount including dispatched workers), with the industry test and the all-or-nothing rule applied.
- [ ] HNTE certificate issue date and validity checked, and the 2026 ratios evidenced.
- [ ] Regional 15%: location, substantive operation and the 60% main-business test documented, with the period (western region to 2030, Hainan to 2027) checked.
- [ ] R&D: not a negative-list industry, costs tracked by project, other-costs cap and overseas limits applied, 100% (or 120% if listed) used.
- [ ] Loss schedule by year. Expired losses removed. HNTE or technology-based SME ten-year rule checked year by year.
- [ ] Only one rate preference applied to the same income.
- [ ] Non-resident payments: 10% withheld (or treaty rate documented and referred) and paid within seven days.
- [ ] Prepayments reconciled: fifteen-day deadlines met; small low-profit enterprises on quarterly filing.
- [ ] Annual settlement for 2026 diarised for 31 May 2027. Any 2025 corrections filed.
- [ ] Referral items (Pillar Two, reorganisations, transfer pricing, special zones, audits) flagged and not finalised.

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
