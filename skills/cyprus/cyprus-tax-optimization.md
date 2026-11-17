---
name: cyprus-tax-optimization
description: >-
  Lawful Cyprus tax planning for 2026: residence and domicile, SDC and the fixed-levy election, company versus self-employment, new-resident exemptions, crypto, approved share plans, foreign pensions and IP-box referral. Use before advising on reducing Cyprus tax; establish eligibility and model the person's facts before recommending an option.
version: 0.3
jurisdiction: CY
tax_year: 2026
last_updated: 2026-11-17
category: tax-optimization
type: decision
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Cyprus tax planning: the legal levers after the 2026 reform v0.3

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

**Source-provenance hold:** This draft is not usable for a filing, election, eligibility determination or recommendation. Official retained/current base text for the Income Tax Law, SDC Law and the main accounts provisions and cross-referenced income scope has not been fully recovered. The recovered amendment passages do not clear the complete workflow. Keep the legal material and conditional worked cases below as research until the remaining dependencies under Sources are closed.

Prepare a Cyprus tax-planning working paper for an individual, freelancer or owner-managed company for tax year 2026, in EUR. Compare lawful options only after establishing eligibility. This is not a return or a filing instruction. The Income Tax (Amendment) Law 244(I)/2025 generally commenced on 1 January 2026; apply current consolidated law, including subsequent amendments, rather than pre-reform figures. [Law 244(I)/2025, art. 23, originally numbered 25](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf); [Gazette 5075 correction, paragraph (a)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/203DBFC78C778160C2258DAB0020F89D/%24file/5075%2027%202%202026%20PARARTIMA%201o%20MEROS%20I.pdf).

Use `cyprus-income-tax` for the full personal computation and deductions, `cy-non-dom` for detailed domicile work, `cyprus-payroll` for payroll, and `cyprus-vat-return` for VAT. These are handoffs, not a certification of those Guides' current contents. The authority is the Tax Department, Ministry of Finance. Tax years are calendar years; the rules below distinguish income tax residence from domicile for Special Defence Contribution (SDC).

### Quick reference: options side by side

| Option | What decides it | Source |
| --- | --- | --- |
| Non-domiciled individual | Income tax residence and legal domicile are separate; non-dom removes individual SDC on dividends and interest, not an automatic GHS exemption | SDC Law 117(I)/2002, arts. 2, 3, 3B, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html); GHS Law 89(I)/2001, art. 19, [law](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html) |
| Company versus self-employment | Corporate tax then salary/dividend extraction, compared with personal tax and contributions on business profit; use actual income and costs, no combined-rate promise | Income Tax Law 118(I)/2002, arts. 5, 8, Second Schedule, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| New-resident or returning-worker relief | Start date, residence and work history, remuneration, relief period and non-stacking rules | Income Tax Law, art. 8(21A), (21B), (23A), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Fixed SDC election after deemed domicile | Irrevocable prepaid levy compared with ordinary SDC over the whole commitment | SDC Law, art. 3D, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Crypto, approved employee share plan, foreign pension | Classify the income before applying its separate statutory regime | Income Tax Law, arts. 20, 20D, 20E, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| IP box | Qualifying profit and asset under the regulations, not all IP receipts; refer the nexus computation | Income Tax Law, art. 9(1)(κ), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |

### Personal income tax scale

Apply marginal rates to chargeable income, after applicable exemptions and deductions. These are the bands from tax year 2026, not rates on gross receipts.

| Chargeable income slice | Rate | Source |
| --- | --- | --- |
| Up to EUR 22,000 | 0% | Income Tax Law, Second Schedule 1(γ), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Above EUR 22,000 to EUR 32,000 | 20% | Income Tax Law, Second Schedule 1(γ), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Above EUR 32,000 to EUR 42,000 | 25% | Income Tax Law, Second Schedule 1(γ), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Above EUR 42,000 to EUR 72,000 | 30% | Income Tax Law, Second Schedule 1(γ), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Above EUR 72,000 | 35% | Income Tax Law, Second Schedule 1(γ), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |

## Ask the client first

- How many days were you physically in Cyprus and each other country this year? Do you have a Cyprus business, job or office in a Cyprus tax-resident person and a permanent home owned or rented here? Did any relevant business, job or office end during the year?
- Where were you born and where was your father domiciled then? Obtain the legal domicile history, not birthplace alone, and residence history for the last 20 years and any claimed non-resident period before that.
- Do dividends come from profits of 2025 or earlier, or 2026 onward? Are there undistributed 2024 or 2025 profits, earlier deemed distributions or SDC payments?
- Do you or a connected person use company property, such as a car, house or loan, privately? Obtain ownership, value, use and transfer records; a loan also needs separate income-tax analysis.
- When did you start work or business in Cyprus, what did you earn in the first 12 months and each relevant year, and where did you reside and work in the prior 7 years and, where relevant, the prior 15 years? Obtain prior exemptions and any protected historic entitlement.
- Do you hold crypto-assets, an approved share plan or a pension for foreign services? Obtain transaction records, plan approval and vesting terms, pension documents, and social-insurance/GHS coverage evidence.

## The method, step by step

1. Fix the tax year and classify every income stream. Use the personal scale above and corporate rate below for 2026. Separate profit years behind dividends. [Income Tax Law, Second Schedule](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html); [SDC Law, art. 3](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).
2. Establish income tax residence from actual days and ties, then determine legal domicile separately. Record evidence and treaty issues before applying an exemption. [Income Tax Law, art. 2](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html); [SDC Law, art. 2](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).
3. Apply the domicile exceptions and deemed-domicile test below. Where eligible after deemed domicile, compare ordinary SDC with the full fixed levy before an irrevocable election. Keep unverified form instructions out of the filing brief. [SDC Law, arts. 2, 3D](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).
4. For each dividend identify its source company, profit year, recipient's SDC status, prior taxed/deemed distribution and any disguised distribution. [SDC Law, arts. 3, 3A, 3Γ](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).
5. Determine GHS coverage independently of non-dom status; aggregate the statutory income categories against the common cap, rather than granting a fresh cap per payer. [GHS Law, arts. 16, 19](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html).
6. Test each employment or returning-worker exemption against its complete conditions. Compare permitted alternatives; do not stack incompatible exemptions. [Income Tax Law, art. 8(21A), (21B), (23A)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).
7. Test crypto, approved share-plan and foreign-pension treatment separately; ordinary rules apply where a special regime excludes the income. [Income Tax Law, arts. 20, 20D, 20E](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).
8. Compare company and self-employment using the client's actual taxable profit, salary, extraction needs, social-insurance bases, GHS, reliefs and compliance costs. Do not quote a combined or effective tax rate. Route the full computation to `cyprus-income-tax` and `cyprus-payroll`.
9. Screen for substance, treaty residence, the general anti-abuse rule and private company benefits. Refer unresolved IP-box/nexus work before proposing a result. [Income Tax Law, arts. 9(1)(κ), 33A](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html); [SDC Law, art. 3A](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

### Residence and domicile

An individual is income tax resident if present in Cyprus for more than 183 days in the tax year, or under the alternative 60-day test if ALL conditions hold: at least 60 days in Cyprus; no stay exceeding 183 days in any one other state; a Cyprus business and/or employment and/or an office in a Cyprus tax-resident person during the year; and an owned or rented permanent Cyprus home. Termination of the relevant business, employment or office during the year defeats that limb. From 2026 the test no longer excludes someone merely because they are also tax resident elsewhere; a treaty conflict still needs advice. [Income Tax Law, art. 2](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

Arrival counts as Cyprus and departure as outside. Same-day arrival and departure counts as Cyprus; same-day departure and return counts as outside. Do not substitute residence certificates for actual day counts. [Income Tax Law, art. 2](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

For individual SDC, residence means income tax residence AND Cyprus domicile. An individual who is non-resident or non-domiciled is outside individual SDC on dividends and interest. Rental SDC was abolished from 2026, so non-dom no longer creates a rental-SDC advantage; ordinary income tax and any GHS remain separate questions. [SDC Law, arts. 2, 3, 3B, as amended by Law 245(I)/2025](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

Domicile of origin follows the Wills and Succession Law framework. For someone with a Cyprus domicile of origin, the SDC exceptions are: acquired and maintained foreign domicile of choice AND Cyprus tax non-residence for any period of at least 20 consecutive years before the tax year; OR Cyprus tax non-residence for at least 20 consecutive years immediately before the commencement of the domicile provisions on 16 July 2015. The first exception does not require that whole period to immediately precede the current tax year. Birthplace alone does not decide domicile. [SDC Law, art. 2(3)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

Whatever domicile of origin, Cyprus tax residence for at least 17 of the 20 tax years immediately preceding the tax year creates deemed domicile. It continues until 20 years of non-residence have elapsed under the statutory rule. **Audit flash point:** establish genuine residence and the complete domicile history before using the exemption. [SDC Law, art. 2(3)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

### Fixed SDC after the deemed-domicile point

Article 3D is an alternative imposition of SDC, not a renewal of legal non-dom status. It is available only to an individual without Cyprus domicile of origin who has become deemed domiciled under article 2(3). Compare all SDC income over the commitment, cash timing and foreign tax credits before electing.

| Rule | Amount or condition | Source |
| --- | --- | --- |
| Fixed annual SDC, irrespective of income | EUR 50,000 | SDC Law, art. 3D(1), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Irrevocable and binding period | 5 consecutive tax years; up to 2 such periods, with accepted application | SDC Law, art. 3D(2), (3), (9), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Prepayment | EUR 250,000 in one instalment for the whole period | SDC Law, art. 3D(4), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Application deadline | 30 June of the first year of the period, prescribed form accepted by Commissioner | SDC Law, art. 3D(3), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Payment deadline | End of the month following the month of approval | SDC Law, art. 3D(4), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |

Late payment invalidates the alternative treatment for every year of the period and ordinary SDC applies. The payment exhausts SDC for the covered years, cannot be set against other tax liabilities or credits, is non-refundable for any reason, and permits no foreign-tax credit against that levy. A person with Cyprus domicile of origin cannot elect. Current form, portal, advance-application and attachment details remain held under Sources. [SDC Law, art. 3D(4)-(9)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

### SDC on dividends, interest and company benefits

The following individual rates require residence AND domicile for SDC purposes. They do not apply to exempt non-dom individuals merely because a company pays a dividend.

| Item | Treatment | Source |
| --- | --- | --- |
| Ordinary individual dividend, including profits of 2026 onward | 5%, subject to prior-tax/deemed-dividend relief | SDC Law, art. 3(1)(a), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Dividend from a Cyprus-resident company from profits up to and including 2025, received in the six-year transition from 2026, through 31 December 2031 | 17%; article 3 does not impose the former draft's eight-profit-year restriction | SDC Law, art. 3(1)(a)(ii), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Interest received or credited: general individual rate | 17%; exceptions below | SDC Law, art. 3B(a), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Specified government savings/development securities and qualifying listed corporate/local-authority/public-body bonds | 3% on interest; classify the instrument under the statutory list | SDC Law, art. 3B(b)(i), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Individual total annual income including interest not exceeding EUR 12,000 | Refund of interest SDC above 3%; not an automatic blanket exemption | SDC Law, art. 3B(a)(i), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Deemed distribution of a resident company's 2024 and 2025 profits only | 70% after corporate tax at the end of 2 years following the profit year; SDC 17%, reduced by actual distributions | SDC Law, art. 3Γ(1), (4), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| Disguised distribution to a shareholder resident for SDC | 10% on the statutory benefit amount, including indirect shareholders | SDC Law, art. 3A, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |

A 2027 dividend from 2025 profits falls within the transitional rate; a dividend from 2026 profits falls within the ordinary rate. This is a profit-vintage distinction, not a rate determined solely by payment year. Track actual dividends already subjected to SDC or deemed distributed, and the statutory reduction. Deemed distributions apply only to profits attributable directly or indirectly to an individual resident for SDC at the deemed-distribution date. The ordinary two-year deemed-distribution rule no longer covers 2026 profits. Dissolution and pre-reform profit pools require separate article 3Γ review; do not infer that retaining old profits always avoids SDC. [SDC Law, arts. 3(1)(a), 3Γ](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

Interest on compensation for disability, serious bodily injury or death is exempt from SDC. The interest rate above is not a statement about all companies or non-resident corporate recipients: their statutory exceptions/withholding rules need separate work. [SDC Law, art. 3B](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

For private use of company assets, article 3A uses market value when use starts, multiplied by personal-use proportion; an asset unrelated to the business is wholly private. An increase in private use creates an additional amount at the then market value; a reduction does not refund earlier SDC. For a transfer below market value, the benefit is the market-value/consideration difference, reduced by the already charged use benefit for the same asset. The specific donor-shareholder/connected-donor exceptions, income-tax employment-benefit exclusion, and capital-reduction/dissolution/liquidation exclusion must be tested before applying the charge. Later dividends, contributions or cessation of use do not generally refund SDC already paid. Do not treat a shareholder's company house or car as automatically tax-free, or charge the whole asset value without checking these conditions. [SDC Law, art. 3A(2)-(6)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

### GHS is separate from SDC

Dividends received by an individual are income-tax exempt under article 8(20), but SDC and GHS require their own analysis. Non-dom does not itself exempt GHS. Determine statutory coverage and any EU/international coordination exemption first; do not promise exemption solely from an overseas insurance card. [Income Tax Law, art. 8(20)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html); [GHS Law, arts. 16, 19](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html).

| Category | GHS contribution | Source |
| --- | --- | --- |
| Employee earnings, pensions, covered office remuneration and income-earner income including dividends | 2.65% under the applicable category | GHS Law, art. 19(1)(a), (d), (e), (g), [law](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html) |
| Self-employed earnings | 4% | GHS Law, art. 19(1)(c), [law](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html) |
| Employer on employee earnings; payer of covered office remuneration | 2.90%, separate from the person's contribution | GHS Law, art. 19(1)(b), (f), [law](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html) |
| Aggregate annual personal contribution base | EUR 180,000 across earnings, pensions and income, not per payer | GHS Law, art. 19(3)-(4), [law](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html) |

Article 19(4) sets the category order and excess-contribution refund mechanism; do not simply stop every withholding stream independently. For contribution years beginning on or after 1 January 2025, contributions on amounts above the cap are refunded by the Tax Commissioner under the Assessment and Collection of Taxes Law. [Law 118(I)/2025, art. 2](https://www.mof.gov.cy/mof/gpo/gazette.nsf/CA8047D664C8E228C2258CC40036F9A3/$file/5047%2011%207%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf). The former Guide's exclusive exemption statement and exact S1/A1/Ministry certificate instructions are held below, not usable filing instructions.

### Company route compared with self-employment

A company is Cyprus resident if managed and controlled in Cyprus OR incorporated under Cyprus law, unless a double-tax treaty provides otherwise for the incorporation limb. Transfer of the registered office or seat to Cyprus counts as incorporation. The former incorporation test's requirement not to be resident elsewhere has been removed. Management, substance and competing treaty claims still need analysis. [Income Tax Law, art. 2](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

| Item | Treatment | Source |
| --- | --- | --- |
| Corporate tax from 2026 | 15% on taxable profit | Income Tax Law, Second Schedule 2, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Tax loss carry-forward | 7 years after the end of the loss year, for a company within the statutory books/accounts/return scope; ownership and business-change restrictions apply | Income Tax Law, art. 13, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Scientific research spending, and R&D spending recognized under international accounting standards, in 2025 through 2030 by a person conducting a business who economically owns the intangible asset resulting, or potentially resulting, from the spending | Additional 20% deduction; exclude machinery, plant and building costs (including staff accommodation) eligible under article 10; capital-spending timing follows the underlying allowance | Income Tax Law, art. 9(1)(δ), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Self-employed social insurance on insurable income | 16.6% paid by the person; state's 5.2% is separate, not another personal charge | Government one-stop shop, contributions and self-employed sections, [page](https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/) |
| Natural-person business accounts exemption | Turnover plus other gross income specified in article 30 up to EUR 120,000 is exempt from the audited/reviewed accounts requirement, not basic record keeping | Assessment and Collection of Taxes Law 4/1978, art. 30(1), [law](https://www.cylaw.org/nomoi/enop/non-ind/1978_1_4/full.html) |
| Review instead of audit | Above EUR 120,000 and up to EUR 200,000 specified turnover/gross income AND total balance-sheet assets up to EUR 500,000 for at least 2 consecutive years; otherwise test audit requirement | Assessment and Collection of Taxes Law, art. 30(1), [law](https://www.cylaw.org/nomoi/enop/non-ind/1978_1_4/full.html) |

A company pays corporate tax first. A dividend then falls under the shareholder's income-tax exemption and the relevant SDC/GHS treatment. Salary is personal employment income and brings payroll/social-insurance/GHS obligations; route to `cyprus-payroll`. Self-employment is personal business profit subject to the marginal scale, applicable reliefs and contributions. Social insurance uses the statutory insurable/estimated earnings classification, not automatically accounting profit; obtain the actual applicable base and cap before comparing. The government one-stop page still prints an old accounts threshold; current article 30 prevails. Do not repeat that stale EUR 70,000 figure as a 2026 audit rule.

Do not quote a combined or effective rate. Compare actual cash retained and extracted, contribution bases, profit vintage, existing deemed distributions, compliance costs and available reliefs. Screen private assets under article 3A and the overall arrangement under article 33A. Incorporation alone does not settle treaty residence or demonstrate real business substance.

### Special income regimes

| Income | Rate and limits | Source |
| --- | --- | --- |
| Crypto disposal gains under article 20E | 8%, separately; sale, gift, swap and payment are disposals; mining-acquired crypto excluded and taxed under ordinary rules | Income Tax Law, art. 20E, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Crypto losses | Offset only same-year crypto gains; no carry-forward or group relief under this regime | Income Tax Law, art. 20E(2), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Approved share-option/share-award benefit for a Cyprus-resident employee/director who is not connected under article 33 | 8% separately, within twice employer income in the vesting-end year (excluding the benefit) and EUR 1,000,000 per rolling 10 years | Income Tax Law, art. 20D, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Share-plan conditions | At least 3-year vesting beginning no earlier than approval, no transfer before vesting, ordinary employer/parent share rights except voting, exercise/acquisition price at least 50% of value at approval | Income Tax Law, art. 20D(1), proviso (i)-(iv), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Resident individual's pension for services outside Cyprus | Optional 5% on the annual amount above EUR 5,000, assessed separately; may elect ordinary rules for each year | Income Tax Law, art. 20, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |

A connected shareholder-director cannot use the employee share-plan rate. The share-plan transitional approval rule for vesting begun before the amendment required submission by 30 June 2026, with the minimum three-year vesting period not having ended by that date; do not use that expired transition for a new plan. Obtain per-person approval and test every condition. Crypto outside article 20E and benefits exceeding the special-rate limits need ordinary-law analysis. [Income Tax Law, arts. 20D, 20E](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

### IP box and R&D interaction

Article 9(1)(κ) expressly deducts 80% of qualifying profits from qualifying intangible assets, allows annual waiver in whole or part, and limits eligible losses to 20% for offset/carry-forward. It gives priority to paragraph (ε) where both regimes could apply. This is not an 80% deduction from all IP revenue. The regulations determine qualifying assets and the qualifying-profit/nexus computation; those operative regulations have not been read for this Guide, so asset eligibility and an actual IP-box computation remain non-usable holds. State no effective IP tax rate. [Income Tax Law, art. 9(1)(κ)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

R&D spending must be recognized under international accounting standards. The deduction requires a person conducting a business with economic ownership of the intangible asset that results, or may result, from the spending. Paragraph (δ) excludes machinery, plant and building costs, including staff accommodation, for which article 10 allowances may be granted. The additional R&D deduction is also unavailable for spending on a qualifying intangible asset if article 9(1)(κ) applied to it in any year, including the current year. For capital spending, the additional deduction follows the years of the underlying paragraph (λ) allowance. Refer every substantive IP-box question to a Cyprus tax adviser with asset ownership, development-cost and related-party records. [Income Tax Law, art. 9(1)(δ), including its provisos](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

### Personal reliefs and new-resident exemptions

| Route | Figure and period | Source |
| --- | --- | --- |
| Article 8(21B), returning worker/business starter | 25% of employment remuneration or business profits, maximum EUR 25,000 per year; earnings/profits must strictly exceed EUR 30,000 in the first 12 months and in each claim year | Income Tax Law, art. 8(21B), [law](https://www.mof.gov.cy/mof/gpo/gazette.nsf/25F3A7FDDE03FF1CC2258DB2003B08C1/$file/5076%206%203%202026%20PARARTIMA%201o%20MEROS%20I.pdf) |
| Article 8(21B), entry and duration | Start during 2025 through 2030; 7 consecutive tax years including the start year, subject to annual conditions | Income Tax Law, art. 8(21B), [law](https://www.mof.gov.cy/mof/gpo/gazette.nsf/25F3A7FDDE03FF1CC2258DB2003B08C1/$file/5076%206%203%202026%20PARARTIMA%201o%20MEROS%20I.pdf) |
| Article 8(23A), qualifying first employment | 50% of remuneration; generally strictly above EUR 55,000 per claim year; up to 17 tax years from the start year or repeal if earlier | Income Tax Law, art. 8(23A), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Article 8(21A), eligible first employment starting 26 July 2022 through 2027 | 20% of remuneration, capped at EUR 8,550 per year; 7 years starting in the year after first employment; no remuneration minimum in this paragraph | Income Tax Law, art. 8(21A), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |

For article 8(21B), ALL apply: non-resident in the preceding 7 tax years; resident in some year before that period; the entry window above; and either a recognised university degree plus at least 36 months' full-time foreign-employer work abroad during the 84 months preceding the month of commencement, OR full-time foreign-employer work abroad for the 84 months preceding that month. For a 2026 start, the non-resident years are 2019-2025. Except for the start year, the claimant must be Cyprus tax resident. The exemption is once in a lifetime and cannot be used with article 8(21A). The earnings threshold is strict, not inclusive. [Income Tax Law, art. 8(21B)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/25F3A7FDDE03FF1CC2258DB2003B08C1/$file/5076%206%203%202026%20PARARTIMA%201o%20MEROS%20I.pdf).

For article 8(23A), the current main rule requires at least 15 consecutive years of non-residence immediately before first employment from 1 January 2022 onward. First employment means starting paid services in Cyprus after 15 consecutive tax years without paid services here, for a resident or non-resident employer. Becoming Cyprus tax resident after commencement is not a stated requirement of this paragraph. The start year can qualify where first-12-month remuneration exceeds the threshold. The statute's annual-threshold/first-or-second-year rule and the Commissioner's anti-arrangement condition must be considered where pay fluctuates; do not promise relief in a below-threshold year. It is once in a lifetime and cannot stack with articles 8(21), (21A), (21B) or (23). [Income Tax Law, art. 8(23A)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

Historic cases are separate: pre-amendment 2023 beneficiaries retain protection under the earlier conditions; specified continuous pre-2022 employment can qualify under the transitional branches. Do not replace that analysis with a universal former 10-year test, or a claim that every change of employer ends relief. Older article 8(23) for 2012-2021 starts and legacy article 8(21) are outside the current-entry comparison and require their own history review. The legacy article 8(21) exemption is also 20% capped at EUR 8,550, subject to its own limited eligibility and duration. [Income Tax Law, art. 8(21), (23), (23A)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

Article 8(21A) additionally requires employment abroad with a non-resident employer for the 3 consecutive years before the Cyprus start, and uses the statutory first-employment definition. Check current entitlement and earlier claims before choosing it; do not impose the former Guide's unsupported automatic end-of-first-job cliff. The alternatives are not cumulative. Personal deductions for children, rent/housing-loan interest, green expenditure, insurance and contributions belong in the full `cyprus-income-tax` computation; this Guide does not determine those entitlements. [Income Tax Law, art. 8(21A), (23A)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

## Boundary and exception table

| Boundary | Action | Source |
| --- | --- | --- |
| Actual residence versus certificates | Reconstruct days, Cyprus ties and termination events; refer dual residence/treaty questions | Income Tax Law, art. 2, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Domicile origin/choice dispute or protected historic employment exemption | Obtain history and professional determination before using an exemption | SDC Law, art. 2, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html); Income Tax Law, art. 8, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Domestic old profits, previously deemed/taxed dividends, liquidation, interposed company, foreign corporate recipient | Trace profit pools and recipient; refer beyond the individual ordinary-dividend comparison | SDC Law, arts. 3, 3B, 3Γ, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |
| IP asset/nexus facts or overseas social-health coverage | Hold the unverified computation/procedure; obtain the missing operative confirmation | Income Tax Law, art. 9(1)(κ), [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html); GHS Law, art. 16, [law](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html) |
| Artificial arrangement without genuine commercial reasons | Refuse artificial residence/substance; article 33A disregards non-genuine arrangements whose main purpose or one main purpose is a tax advantage defeating the law's object | Income Tax Law, art. 33A, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) |
| Private company benefit | Test statutory valuation, exceptions, employment-benefit overlap and prior charges | SDC Law, art. 3A, [law](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) |

## Worked cases

### Case 1: choose between two employment exemptions

Illustrative 2026 decision, not an eligibility determination: first employment began in 2025 after 15 consecutive years of non-residence and no paid Cyprus services, including the required prior foreign-employer employment. The adviser confirms that either article 8(21A) or article 8(23A) is available in 2026, all approval/history conditions are satisfied and there is no protected earlier claim. Remuneration is EUR 60,000; there is no other taxable income. Isolate income tax before contributions and other deductions to compare the exemption itself. Do not stack them. [Income Tax Law, art. 8(21A), (23A), Second Schedule](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html).

Article 8(21A): the percentage deduction would be EUR 12,000 but the cap reduces it to EUR 8,550. Chargeable income is EUR 51,450. Tax is EUR 2,000 + EUR 2,500 + EUR 2,835 = EUR 7,335. Article 8(23A): exempt EUR 30,000, leaving EUR 30,000; tax is EUR 1,600. The latter reduces the isolated income tax by EUR 5,735, provided eligibility holds. A person meeting only the former route cannot choose the latter merely for that saving. Both options still require contribution and full personal-return work.

```oa-check
name: 2026 employment exemption decision
inputs:
  remuneration: 60000
  cap_21a: 8550
steps:
  - exemption_21a: min(remuneration * 0.20, cap_21a)
  - base_21a: remuneration - exemption_21a
  - tax_21a: clamp(base_21a - 22000, 0, 10000) * 0.20 + clamp(base_21a - 32000, 0, 10000) * 0.25 + clamp(base_21a - 42000, 0, 30000) * 0.30 + max(base_21a - 72000, 0) * 0.35
  - base_23a: remuneration * 0.50
  - tax_23a: clamp(base_23a - 22000, 0, 10000) * 0.20 + clamp(base_23a - 32000, 0, 10000) * 0.25 + clamp(base_23a - 42000, 0, 30000) * 0.30 + max(base_23a - 72000, 0) * 0.35
  - tax_difference: tax_21a - tax_23a
expected:
  exemption_21a: 8550
  base_21a: 51450
  tax_21a: 7335
  base_23a: 30000
  tax_23a: 1600
  tax_difference: 5735
```

### Case 2: the fixed SDC election can cost more

Assume an individual without Cyprus domicile of origin is deemed domiciled and eligible for an approved article 3D election for a five-year period beginning in 2026. Assume EUR 500,000 dividends each year, all from 2026-onward profits within ordinary individual dividend treatment, and no other SDC income, prior-tax relief or foreign tax credit. Hold rates constant for this illustration; later years require a law update. [SDC Law, arts. 3, 3D](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html).

Ordinary SDC would be EUR 25,000 annually, EUR 125,000 over the period. The election requires EUR 250,000 upfront even on these lower incomes. It costs EUR 125,000 more before the time value of money, so ordinary treatment is preferable on these facts. Different interest/dividend amounts or foreign-tax credits can reverse the choice. GHS and company tax are outside both sides of this comparison; it is not a combined-rate illustration. Approval, payment and irreversibility still matter.

```oa-check
name: Fixed SDC versus ordinary dividends
inputs:
  annual_dividends: 500000
  years: 5
  fixed_payment: 250000
steps:
  - annual_sdc: annual_dividends * 0.05
  - ordinary_sdc: annual_sdc * years
  - extra_cost_fixed: fixed_payment - ordinary_sdc
expected:
  annual_sdc: 25000
  ordinary_sdc: 125000
  extra_cost_fixed: 125000
```

## When to refuse or refer

- Refuse paper residence, fabricated domicile or an arrangement without genuine commercial reasons to obtain a tax advantage. Preserve evidence of real management, activity and residence.
- Refer every substantive IP-box asset/nexus/computation question; the statutory percentage alone does not establish eligibility.
- Refer domicile-of-choice disputes, the long non-residence exceptions and any exemption/election application, including the held Form T.D.38 and TD 631 instructions.
- Refer treaty residence of an individual/company and competing country claims; incorporation does not resolve a treaty tie.
- Refer pre-2018 profit pools, old deemed distributions, liquidation, or dividends after 31 December 2031 from pre-2026 profits for a complete transition analysis. The old eight-year cutoff is not a current general individual-dividend rule.
- Refer any plan requiring a combined/effective rate or an unverified relief. This Guide compares separate charges and does not determine a universal extraction structure.

## Filing and payment

This Guide produces a decision working paper, not a completed election or return. The fixed-SDC application and payment deadlines are above; have the adviser establish the current prescribed form and portal before filing. Ordinary tax-return, SDC withholding/payment, payroll and contribution submissions require the appropriate filing Guide and current authority instructions. Do not use blocked legacy PDF links as a form-filing authority or submit a live form from this workflow.

## Completion checklist

- Trace income, days, domicile, employment history, plan approvals, dividend vintage and contribution coverage to the person's documents.
- Record each option's eligibility, annual thresholds, cap, non-stacking condition, cash cost, deadline and unresolved condition.
- Reconcile old profit/deemed-distribution balances and all GHS income streams before comparing net cash.
- Keep IP nexus, historic protected reliefs and inaccessible procedures out of usable conclusions until resolved.
- Recompute the comparison using actual facts; obtain qualified professional review before action.

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Cyprus) before acting upon.

## Sources

Read date means substantive paragraphs read, not a successful retrieval. CyLaw is the nonprofit Bar/CyLII service, not a government-hosted database: its HTML is a private maintained consolidation and the historical reads below do not establish official current-law provenance. [EU N-Lex](https://n-lex.europa.eu/n-lex/legis_cy/cy_gov_cyprus_form?lang=en) refers readers to CyLaw; the [EU Publications Office Gazette profile](https://op.europa.eu/en/web/forum_official_gazettes/cyprus-oj) distinguishes the binding Gazette from consolidations (both provenance pages read 2026-11-16). The completed official Gazette 5070 recovery established exact operative-body identity for Laws 244/245 after whitespace and printed-page-number normalization; whole-file byte equality is not claimed. Reuse that evidence and the completed substantive review. The later official reads below supply only their specified replacement provisions, amendment targets and commencement. No accountant approval or clearance of the remaining base-law dependencies is claimed.

| Source | Actual scope read | Read date |
| --- | --- | --- |
| [Income Tax Law 118(I)/2002, consolidated](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) | Art. 2 residence/day counting; art. 8(19)-(23A) exemptions and transitional/non-stacking conditions; art. 9(1)(d), (κ) R&D/IP; art. 13 loss conditions; arts. 20, 20D, 20E; art. 33A; Second Schedule; relevant commencement notes | 2026-11-16 |
| [Official Gazette 5070: Law 244(I)/2025](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) | Title, reform text and amended rates; commencement originally numbered art. 25, corrected to art. 23 by Gazette 5075; completed operative-body identity match reused | 2026-11-16 |
| [SDC Law 117(I)/2002, consolidated](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) | Art. 2 residence/domicile; art. 3 individual dividends/transition/relief; arts. 3A-3D disguised distribution, interest exceptions, deemed distribution and fixed levy; 2025 amendment commencement note | 2026-11-16 |
| [Official Gazette 5070: Law 245(I)/2025](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) | Title, replacement of art. 3/rental provisions and art. 10 commencement; completed operative-body identity match reused | 2026-11-16 |
| [GHS Law 89(I)/2001, consolidated](https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html) | Arts. 16 and 19: beneficiary/coordination reference, contribution categories, aggregate cap, order and refund; no claim to have verified foreign-coverage filing documents | 2026-11-16 |
| [Assessment and Collection of Taxes Law 4/1978](https://www.cylaw.org/nomoi/enop/non-ind/1978_1_4/full.html) | Art. 30 natural-person records/accounts/audit-review thresholds and Law 243(I)/2025 commencement note | 2026-11-16 |
| [Government one-stop shop: social insurance](https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/) | Contribution split and self-employed estimated-earnings paragraphs only; its accounts threshold is stale and is superseded here by art. 30, not relied on | 2026-11-16 |
| [Official Gazette 5075: correction to Law 244(I)/2025](https://www.mof.gov.cy/mof/gpo/gazette.nsf/203DBFC78C778160C2258DAB0020F89D/%24file/5075%2027%202%202026%20PARARTIMA%201o%20MEROS%20I.pdf) | PDF 1: renumbering of arts. 16-25 as 14-23 and the separate art. 14B textual correction | 2026-11-17 |
| [Official Gazette 5076: Law 17(I)/2026](https://www.mof.gov.cy/mof/gpo/gazette.nsf/25F3A7FDDE03FF1CC2258DB2003B08C1/$file/5076%206%203%202026%20PARARTIMA%201o%20MEROS%20I.pdf) | PDF 39-41: art. 8(21B) full replacement, month-based work-history windows, non-stacking additions and 1 January 2025 commencement | 2026-11-17 |
| [Official Gazette 5086: Laws 66/67(I)/2026](https://www.mof.gov.cy/mof/gpo/gazette.nsf/21F7154E05045B76C2258DD900389972/%24file/5086%2014%204%202026%20PARARTIMA%201o%20MEROS%20I.pdf) | PDF 4-9: amendment targets and operative text; Law 66 adds art. 39A; Law 67 arts. 2-4 amend art. 8(11), share-plan transitional approval and commencement | 2026-11-17 |
| [Official Gazette 4523: Law 119(I)/2015](https://www.mof.gov.cy/mof/gpo/gazette.nsf/F674ED42A2E1D563C225872C00406415/$file/4523%2016%207%202015%20PARARTIMA%201o%20MEROS%20I.pdf) | PDF 15-16: resident/domicile definitions, domicile-of-origin exceptions, 17-of-20 test and 16 July 2015 commencement; subsequent/current base applicability remains held | 2026-11-17 |
| [Official Gazette 4897: Law 90(I)/2022](https://www.mof.gov.cy/mof/gpo/gazette.nsf/692DC834CD302112C225886B003E85BB/$file/4897%2024%206%202022%20PARARTHMA%201o%20MEROS%20I.pdf) | PDF 17, art. 4: natural-person accounts proviso, specified income scope, EUR 200,000/EUR 500,000 and two-year review gate; later EUR 120,000 substitution read in Law 243/2025 art. 17 in Gazette 5070; retained main accounts text and referenced income scope remain held | 2026-11-17 |
| [HIO official Law 74(I)/2017](https://www.gesy.org.cy/el-gr/pressrelease/2017-1-074-peri-genikou-systimatos-ygeias-nomos-20017.pdf) | Relevant replacement definitions, arts. 16/19 and commencement, PDF 1-4, 15-18 and 49; beneficiary/coordination reference, rates, aggregate cap, category order and refund; no foreign-coverage procedure clearance | 2026-11-17 |
| [Official Gazette 5047: Law 118(I)/2025](https://www.mof.gov.cy/mof/gpo/gazette.nsf/CA8047D664C8E228C2258CC40036F9A3/$file/5047%2011%207%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) | PDF 1-2, art. 2: excess-cap refund by Tax Commissioner for contribution years beginning on or after 1 January 2025 | 2026-11-17 |
| [29(I)/2025 official Gazette](https://www.mof.gov.cy/mof/gpo/gazette.nsf/96B722F6AA0C4264C2258C5E002DFBC7/$file/5031%2031%203%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) | PDF [1]: Amends article 22 only: prescriptions and referrals. | 2026-11-17 |
| [53(I)/2025 official Gazette](https://www.mof.gov.cy/mof/gpo/gazette.nsf/722F5AE57F178F54C2258C770030E2EA/$file/5036%2025%204%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) | PDF [7, 8, 9, 10, 11, 12, 13]: Changes competent-authority and Commissioner definitions, Part VIII oversight and transitions. No change to articles 16/19 or contribution definitions. | 2026-11-17 |
| [139(I)/2025 official Gazette](https://www.mof.gov.cy/mof/gpo/gazette.nsf/F0CF43ACA530EFBAC2258CD2003C75E2/$file/5050%2025%207%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) | PDF [1, 2, 3, 4]: Changes General Director and cross-border healthcare definitions, articles 33/33A/33B/59. This concerns healthcare abroad, not a foreign-insurance contribution exemption. | 2026-11-17 |
| [60(I)/2026 official Gazette](https://www.mof.gov.cy/mof/gpo/gazette.nsf/BD672DDC455EA08AC2258DD300413FBE/$file/5084%208%204%202026%20PARART%CE%97MA%201o%20MEROS%20I.pdf) | PDF [55, 56, 57, 58, 59, 60]: Adds clinical centre/board definitions and changes articles 14/22/33C/34/35/35A/35B/35C/60A; commencement by notice. No change to articles 16/19 or contribution definitions. | 2026-11-17 |
| [61(I)/2026 official Gazette](https://www.mof.gov.cy/mof/gpo/gazette.nsf/C63D7188DE8B643DC2258DD40036A7EA/$file/5085%209%204%202026%20PARART%CE%97MA%201o%20MEROS%20I.pdf) | PDF [1]: Adds counselling psychologists to the other-health-professionals definition only. | 2026-11-17 |

**Not yet confirmed:** the official retained/current Income Tax Law 118(I)/2002 base, SDC Law 117(I)/2002 base and their unresolved applicability dependencies; the retained main Assessment Law 4/1978 art. 30 text and referenced Income Tax Law art. 5 scope. These source gaps prevent use of this draft for a filing, election, eligibility determination or recommendation. Separate non-usable holds: current T.D.38 exemption procedure; TD 631/TFA submission route, availability up to two years in advance, clean-criminal-record and non-dom certificate attachment requirements; exact overseas GHS exemption scope, S1/A1/Ministry certificate route and whether any exemption is exclusive; operative IP-box regulations defining qualifying assets and nexus computation. The former Guide's government PDFs/pages (2026 reform FAQs/presentations, residency page, extension application, T.D.59A, 2025 return guide and employment-relief tables) could not be read in this pass: direct access failed or recovered captures were WAF error pages; browser fallback was unavailable. The recovered official amendment passages support only the stated provisions; the still-unrecovered base-law dependencies and procedural details are not validated by those citations. These holds prevent filing or using the affected procedural/asset conclusions; they do not turn an unverified form into an approved instruction.
