---
name: international-incorporation
description: "International company formation and jurisdiction selection guide for solo founders, freelancers, and digital nomads. Use when the user asks about: where to register a company, business jurisdiction selection, Wyoming LLC setup, Delaware LLC, Hong Kong company formation, Singapore Pte Ltd, Estonia e-Residency OÜ, UK Ltd incorporation, Dubai freezone company, offshore company structure, one-person company (一人公司), solo founder incorporation, entity type selection, pass-through vs corporation, company formation costs, annual compliance by jurisdiction, 注册公司, 海外公司, 开公司, 离岸公司, 会社設立, 法人化, incorporating abroad, best country to register a business, cheapest jurisdiction, Stripe Atlas, company for non-US founders, company closure, operating agreement, or any question about choosing where to incorporate an international business."
version: 1.1
jurisdiction: INTL
tax_year: 2026
last_updated: 2026-11-16
source_checked: 2026-11-16
type: cross-country-method
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
---

# International Incorporation

Choose an entity after comparing the founder's actual residence, business operations, funding and continuing obligations. Incorporation abroad does not itself create a tax exemption, permission to remit money, immigration status or access to a bank account.

> **Based on work by [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill provides general guidance on international company formation. It does not constitute legal or tax advice. All structures and tax treatments must be verified with qualified local advisors (CPAs, tax attorneys, chartered accountants) in the relevant jurisdictions before implementation. Tax rules, costs, and compliance requirements change frequently.

## Scope and period

This is a **2026 comparison and formation workflow**, checked **16 November 2026**. The statutory screens below are bounded by their named official sources and entity types. Individually unresolved costs, timelines, national tax proposals and commercial services remain unusable under **Not yet confirmed**. Not yet approved.

The original United States, Singapore, Estonia and Dubai short list, plus United Kingdom and Hong Kong alternatives, remains a comparison list. The former “Tier 1”/“Tier 2” country ranking is not a trust rating or a recommendation that a country fits most founders. For a specific decision, prepare a documented comparison of domestic operation against each feasible foreign entity, including both company and owner taxation.

## The method, step by step

1. Record nationality, primary objective, each tax residence, business activity, revenue, customer and supplier locations, places where work and management occur, employees, funding and intended profit distributions. Distinguish the founder's tax residence from the company's residence.
2. Check lawful funding and foreign-exchange constraints before selecting a country; use the separate `forex-controls.md` route for the relevant home-country research. Do not assume a Hong Kong account removes mainland-China controls or that an Indian LRS allowance clears every overseas investment.
3. Compare entity classification, owner-level tax, source and permanent-establishment exposure, local licences, actual management/substance and required registrations. Record each unresolved home-country CFC, reporting, treaty and social-tax issue before recommending implementation.
4. Obtain current official filing fees and separate written commercial quotes for agents, resident directors, secretaries, office, accounting, visas, banking and payment services. State currency, quote date and inclusions; do not present a state fee as a complete annual cost.
5. Give the founder a formation and continuing-obligations calendar, permitted payment route, ownership/management documents and funded closure plan. Confirm actual bank/payment eligibility separately from registration. The workflow does not authorise an application, payment or filing.

## United States: Wyoming LLC and Delaware LLC / C-Corp

### Classification and tax screen

A domestic single-member LLC is normally disregarded for **federal income tax** unless it elects corporate treatment on Form **8832**. A domestic LLC with at least **2 members** is normally a partnership unless it elects corporate treatment. A disregarded LLC remains a separate entity for employment and certain excise taxes. The owner reports the relevant activities; “disregarded” does not mean tax-free. [IRS classification and EIN rules](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies).

For a foreign owner, determine US trade/business and effectively connected income, US-source income, applicable treaty relief and relevant state obligations. The IRS expressly treats connected income as taxable; US-source FDAP that is not effectively connected is generally taxed on its gross amount at **30% or a lower treaty rate**, subject to its actual scope. Merely having foreign owners or serving global SaaS/digital-service customers does not establish **0% US tax**. Home-country taxation is a separate question. [ECI scope and exceptions](https://www.irs.gov/individuals/international-taxpayers/effectively-connected-income-eci); [FDAP scope](https://www.irs.gov/individuals/international-taxpayers/fixed-determinable-annual-periodical-fdap-income).

An ordinary C-corporation's Form **1120** tax computation applies **21%** to taxable income; that is not the combined company-and-shareholder rate or a waiver of other corporate taxes. A distribution needs its own shareholder/withholding analysis. For an individual carrying on a business through a disregarded LLC, the IRS describes self-employment taxation; the standard **15.3%** combines **12.4%** Social Security and **2.9%** Medicare, with a Social Security earnings cap and potential additional Medicare tax. It is not a flat charge on every US citizen's LLC revenue and is not a nationality-only test. [Form 1120, Schedule J line 1a](https://www.irs.gov/instructions/i1120); [self-employment scope, cap and additional-tax conditions](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes).

### Form 5472 and EIN

A wholly foreign-owned **domestic disregarded entity** is treated separately as a corporation for the limited section **6038A** information-reporting rules. A reporting corporation generally files **Form 5472** when it has a reportable related-party transaction; the no-reportable-transaction exception must be checked. Contributions, distributions and amounts connected with formation, dissolution, acquisition or disposition can be reportable under Part V. This is broader than a sale to a foreign related party, but not a universal filing rule for every foreign-owned LLC regardless of classification or transactions. [Actual Form 5472 instructions, definitions, who must file and Part V](https://www.irs.gov/instructions/i5472).

A foreign-owned US DE attaches Form **5472** to a **pro forma Form 1120** by that return's due date, including a valid extension; use the owner's US tax year, or the calendar year if there is none. The ordinary Form 1120 rule is the **15th day of the 4th month** after year-end, with its specified June-year-end and weekend/holiday exceptions. Thus **15 April** is a calendar-year illustration, not a universal deadline. Form **7004** must be requested by the regular due date; the DE uses the special fax/mail route and cannot e-file Form 5472. [5472 filing/extension instructions](https://www.irs.gov/instructions/i5472); [1120 due dates](https://www.irs.gov/instructions/i1120).

The initial failure-to-file-or-maintain-records penalty is **USD 25,000**; substantially incomplete filing counts as failure. Continued failure beyond **90 days after IRS notification** can trigger another **USD 25,000 for each related party for each 30-day period or part** after that point. Do not describe the initial penalty as a universal annual charge “per form per year”. The IRS EIN rules distinguish income-tax identification from employment/excise obligations; a bank may require an EIN even where the default income-tax rule alone does not. [Penalties and DE filing rules](https://www.irs.gov/instructions/i5472); [LLC EIN distinctions](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies).

### State formation and continuing costs

| Entity / task | Current source-bounded finding |
| --- | --- |
| Wyoming LLC formation | Official articles filing fee **USD 100**. The older paper instructions state processing up to **15 business days** after receipt and no expedited filing. The later **2026** official fee schedule separately lists expedited services at **USD 1,400 same business day / USD 700 next business day**; confirm availability for the selected submission. Neither source guarantees the old **1–3 days** total formation timeline. [Official form instructions](https://sos.wyo.gov/Forms/Business/LLC/LLC-ArticlesOrganization.pdf); [later fee schedule](https://sos.wyo.gov/Business/Docs/BusinessFees.pdf). |
| Wyoming annual report | Due on the **1st day of the anniversary month**. Annual report licence tax is the greater of **USD 60** or **0.0002 × assets located and employed in Wyoming**; service-provider fees and online payment charges are separate. The form warns of dissolution if unpaid within **60 days** of the due date. [Annual report instructions](https://wyobiz.wyo.gov/Business/AnnualReport.aspx); [June 2026 fee schedule](https://sos.wyo.gov/Business/Docs/BusinessFees.pdf). |
| Delaware domestic LLC formation | The **1 August 2026** fee schedule lists **USD 110** state filing fee for ordinary domestic formation; optional certified copies and expedited fees are separate. This supersedes the old **USD 90** figure. [Current official schedule, LLC table](https://corpfiles.delaware.gov/Fee_Schedule/AugustFee2026.pdf). |
| Delaware LLC / LP / GP annual tax | The current official instructions say **USD 400**, due **1 June** for the prior year, with **no annual report** for these entities. Late payment carries **USD 200 plus 1.5% monthly interest on tax and penalty**; no proration, and any activity in the state's records during the year can trigger that year's tax. This supersedes the original **USD 300** annual LLC figure and must not be applied to a C-corporation's separate franchise-tax regime. [Delaware instructions](https://corp.delaware.gov/alt-entitytaxinstructions/). |

Wyoming LLC/global SaaS and Delaware C-Corp/US venture-capital funding are retained **use cases to evaluate**, not guaranteed best choices. SAFE notes, convertible instruments and investor preferences require transaction-specific legal work. The original “no substance required” statement cannot waive registered-agent, actual-management, nexus, home-country or beneficial-owner requirements. Banking and Atlas proposals remain individually bounded below.

## Singapore Pte. Ltd.

The corporate headline rate is **17% of chargeable income**. Under the qualifying new-start-up scheme, the first **3 consecutive YAs** from YA **2020** onward exempt **75% of the first SGD 100,000** normal chargeable income and **50% of the next SGD 100,000**. The company must be incorporated and tax-resident in Singapore for that YA; throughout the basis period, no more than **20** shareholders must beneficially hold all share capital directly, with all shareholders individuals or at least **1 individual holding at least 10% of issued ordinary shares**. Investment-holding and property-development companies are excluded. Loss/no-income years still consume the consecutive-YA window. The old **8.5% on the first SGD 200,000** is not the start-up formula. [IRAS rate, exemption, exclusions and first-YA conditions](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes).

For **YA 2026**, the enhanced rebate is **50% of corporate tax payable**, with combined rebate/cash-grant benefits capped at **SGD 40,000**. The separate **SGD 2,000** cash grant requires an active company and the specified **2025 local-employee CPF condition**, excluding shareholder-directors; it is not another unrestricted credit on top of the full rebate. Apply IRAS's interaction rules. This temporary YA-specific relief does not change the **17%** headline rate. [Actual current IRAS rebate and grant rules](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes).

Singapore currently does not withhold tax on dividends. The capital/revenue nature of a gain must be determined before using the capital-gains non-taxation statement; calling a receipt a “capital gain” does not establish its nature or clear other foreign-income provisions. [IRAS dividend withholding](https://www.iras.gov.sg/taxes/withholding-tax/payments-to-non-resident-company/payments-that-are-not-subject-to-withholding-tax); [IRAS taxable/non-taxable income](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/taxable-non-taxable-income).

Reserve the name before registration: ACRA lists **SGD 15** for the name and **SGD 300** for registration, a combined **SGD 315** statutory charge before providers or other services. At least **1 locally resident director** is needed at registration; appoint a secretary within **6 months**, and a sole director cannot also be that secretary. The registered office must be a Singapore address meeting the stated accessibility requirements; it need not be the operational premises. [ACRA fees](https://www.acra.gov.sg/manage/companies/service-transaction-fees/); [registration requirements](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/registering-via-bizfile/); [officers](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/appointing-company-directors-other-key-officers/).

An Asia-Pacific business and the original **USD 50,000 revenue** planning breakpoint remain comparison inputs, not exemption or formation eligibility. Current nominee-director prices, service totals and processing-time promises remain unconfirmed below.

## Estonia e-Residency OÜ

The standard company distribution tax is **22/78 of the net distribution from 2025**, not the old **20%** figure. Retaining and reinvesting profit does not itself trigger distribution tax, but fringe benefits, gifts, donations, entertainment, equity payments and non-business expenses can be taxable; do not call every payment out a tax-free reinvestment. This does not clear special regimes or home-country taxation. [EMTA current rate and distribution scope](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes); [government non-business-payment scope](https://learn.e-resident.gov.ee/hc/en-gb/articles/360002559718-Taxable-payments).

E-Residency is not personal or company tax residency. Consider actual management, permanent establishment and dual residence where the founder lives and works. An EU-facing business reinvesting profits, including the original non-EU-founder/EU-market-access case, is a use case, not a guarantee that only Estonia may tax it. The current official state-fee page lists **EUR 150** for an e-Residency application and **EUR 265** for OÜ registration, hence **EUR 415** before providers or travel/pickup costs; it identifies the application fee as **EUR 165 from 2027**. Do not use the original **EUR 385** package estimate as a current quote. [Official tax-residency caution](https://www.e-resident.gov.ee/taxes-in-estonia/); [current state fees](https://learn.e-resident.gov.ee/hc/en-gb/articles/11432057891473-Estonian-state-fees).

## Dubai free-zone company

Free-zone incorporation does not by itself create a tax holiday. The cited January2026 Ministry-hosted consolidation is expressly an **unofficial English translation**; the Arabic original was not read here. Under its corporate-tax article **3(1)** and Cabinet Decision **116/2022**, ordinary taxable persons have **0% on taxable income up to AED 375,000** and **9% on the excess**; this is taxable income, not turnover. A **Qualifying Free Zone Person** instead has **0% on qualifying income and 9% on non-qualifying taxable income** under article **3(2)**, with no automatic ordinary **AED 375,000** allowance for that non-qualifying portion. Establish qualifying status, actual income and all current conditions before calculating. The amended article **3(3)** separately provides for MNE top-up-tax legislation; the ordinary/free-zone rates are not a clearance of that group-level regime. [Corporate-tax law articles 3, 18–19](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [Cabinet Decision 116 article 2](https://mof.gov.ae/wp-content/uploads/2023/02/Cabinet-Decision-No-116-of-2022-on-CT-Article-3-Threshold-1.pdf).

Article **18** requires adequate substance, qualifying income, no article **19** ordinary-rate election, compliance with transfer-pricing/documentation articles **34/55**, and other prescribed conditions. This Guide does not supply a complete current qualifying/excluded-activities calculation: recover the applicable decisions and use `free-zones-sez-matrix.md` for that separate work. An election can begin in the election period or following period. Do not infer qualifying status from a **DMCC, IFZA or Meydan** licence alone. [Ministry-hosted English articles18–19 and adjacent provisions, subject to the translation limit above](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf).

The original **5% personal income tax from January 2026** assertion is unsupported and must not be used. **Not yet confirmed:** the separate historical claim that personal income tax **was 0% until December 2025** is also unverified and must not be used; the cited natural-person corporate-tax screen does not establish that historical claim. For natural persons, the FTA says UAE business/business-activity turnover must exceed **AED 1 million in a calendar year** before the stated corporate-tax screen applies; wages, personal investment and real-estate investment income are excluded income streams for that screen. This is not a universal zero-tax promise for every founder or business receipt. A licence, visa or relocation alone is not a complete personal or treaty-residence determination; the earlier “must live there” shorthand cannot replace the actual residence tests. [FTA natural-person scope](https://tax.gov.ae/en/taxes/corporate.tax/corporate.tax.topics/basis.of.taxation.natural.person.aspx).

## United Kingdom Ltd

For ordinary non-ring-fence profits, the headline rates are **19%** at the small-profits end and **25%** at the main-rate end. The usual **GBP 50,000 / GBP 250,000** limits are reduced for short accounting periods and associated companies, with marginal relief between the adjusted limits. The relief is unavailable to non-UK-resident companies and close investment-holding companies, and augmented profits matter. Do not treat the original two brackets as an all-entity calculation. [2026 rates](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax); [relief scope and adjusted limits](https://www.gov.uk/guidance/corporation-tax-marginal-relief).

Current Companies House formation is **GBP 100 online**, usually within **24 hours**; the postal route is **GBP 124** and ordinarily **8–10 days**. An agent's service bill is separate. The service identifies director identity-verification/personal-code and PSC information requirements; incorporation is not a promise of banking or permission to work in the UK. The original **GBP 12** and “cheapest/fastest globally” are superseded or unsubstantiated. UK/EU B2B consulting clients remain a commercial comparison input. [Current formation service](https://www.gov.uk/limited-company-formation/register-your-company); [official fee schedule](https://www.gov.uk/government/publications/companies-house-fees/companies-house-fees).

## Hong Kong Limited Company (有限公司)

Corporations normally pay **16.5%** profits tax. Under the qualifying two-tier regime, the first **HKD 2 million** assessable profits is taxed at **8.25%**, with **16.5%** above it. Only **1 nominated connected entity** can use the two-tier regime for a year; the specified concessionary-regime elections also exclude eligibility. Do not assume every company in a group receives the lower band. [IRD ordinary rates](https://www.ird.gov.hk/eng/tax/bus_pft.htm); [two-tier FAQ Q1–Q13](https://www.ird.gov.hk/eng/faq/2tr.htm).

The territorial source test turns on the actual operations producing the profits; absence of a Hong Kong office/employees and signing contracts abroad is not a mechanical exemption checklist. The **FSIE** overlay concerns specified foreign-source income received in Hong Kong by an **MNE entity carrying on a trade, profession or business there**, irrespective of revenue or asset size: interest, dividends, IP income and equity disposal gains from **1 January 2023**, extended to other disposal gains from **1 January 2024**. Test exclusions and the applicable economic-substance, nexus, participation or intra-group-transfer exceptions before an exemption; do not apply one substance test to every income type. Source and economic substance are separate contexts. [Territorial charge](https://www.ird.gov.hk/eng/tax/bus_pft.htm); [actual FSIE scope, exclusions, receipt and exception architecture](https://www.ird.gov.hk/eng/tax/bus_fsie.htm).

The China/Asia-trade and mainland-founder use case is retained for comparison, subject to both jurisdictions' obligations. Hong Kong incorporation does not erase mainland forex, personal-tax, management or transfer-pricing issues. The Treasury Bureau confirms **no Hong Kong withholding tax on dividends**; that does not exempt the recipient in another jurisdiction. The detailed transaction-specific offshore exemption conclusion remains unresolved by incorporation alone. [Official dividend-withholding policy](https://www.fstb.gov.hk/en/treasury/general/prevailing-tax-policy.htm).

## Decision tree and revenue planning

Start with legal residence, operations and permitted funding, then compare the same original branches:

| Original founder / business branch | Corrected decision task |
| --- | --- |
| Mainland China, global revenue / no global revenue | Compare Hong Kong Ltd with lawful domestic 个体户 or 小规模纳税人 routes. Recover mainland eligibility, foreign-investment/forex and tax rules; do not select Hong Kong to “escape” controls. |
| Taiwan, significant international revenue / domestic revenue | Compare Taiwan domestic company with Hong Kong Ltd / Singapore Pte. Ltd.; determine actual home-country residence, reporting and funding rules before selecting. |
| India | Compare US LLC and Singapore Pte. Ltd. only after the resident-individual LRS/overseas-investment screen; no general “strong DTAA” or automatic tax saving conclusion. |
| US citizen | Compare domestic LLC and C-corporation with foreign alternatives; separately resolve owner reporting/CFC and other home-country issues. A Wyoming entity is not a general cure for foreign-company rules. |
| Other nationality: US/global customers without VC / with VC | Evaluate Wyoming LLC / Delaware C-Corp respectively, subject to the federal and state screens above and actual investor requirements. |
| EU customers, retain profits / distribute profits | Evaluate Estonia OÜ / UK Ltd respectively; compare combined owner/company taxes and operating residence, not only retained-profit deferral or old setup price. |
| Asia customers, above / below USD 50,000 revenue | Evaluate Singapore / Hong Kong and the original Wyoming LLC + Wise option as commercial alternatives; the number is not a legal threshold. |
| Founder willing to relocate for lower personal tax | Evaluate a UAE free-zone entity only after residence, business, qualifying-income and home-country exit/continuing-tax analysis. |

RBI's actual LRS direction permits **resident individuals**, not corporates/partnerships/HUFs/trusts, to remit up to **USD 250,000 per April–March financial year** for permitted current/capital transactions. ODI/OPI must comply with the **2022 overseas-investment rules, regulations and directions**; prohibited FEMA/margin transactions remain outside the scheme. The allowance does not itself approve funding any LLC. [RBI LRS A1–A6 and adjacent conditions](https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10192).

The original revenue bands are **planning heuristics**, not incorporation/tax-law exemptions: **below USD 5,000/year**, compare invoicing personally/sole proprietorship with liability/licensing needs; **USD 5,000–25,000**, compare one simple entity, including the original Wyoming LLC / UK Ltd alternatives, and the old **USD 50–100 monthly** budget; **USD 25,000–100,000**, add proper accounting and accounting software and compare the old **USD 100–250 monthly** budget; **USD 100,000–500,000**, compare Singapore/Estonia and the old **USD 300–700 monthly** budget; **above USD 500,000**, consider whether additional jurisdictions and legal/accounting support justify the old **USD 1,000+ monthly** budget. None of those service budgets is a current quote, and low revenue does not universally permit trading without registration.

## Continuing-obligations calendar

| Jurisdiction / filing | Current finding and boundary |
| --- | --- |
| Wyoming annual report | Anniversary-month **1st day**; annual licence-tax formula and **60-day** dissolution warning as stated above. The old **USD 50 + USD 2/month** late-fee formula is not established by these official sources. [Official report](https://wyobiz.wyo.gov/Business/AnnualReport.aspx); [form](https://sos.wyo.gov/Forms/Business/LLC/LLC-ArticlesOrganization.pdf). |
| Delaware LLC | **1 June**, **USD 400**, **USD 200 + 1.5% monthly** tax/penalty interest as above; do not transfer this LLC rule to a C-corporation. [Actual Delaware instructions](https://corp.delaware.gov/alt-entitytaxinstructions/). |
| Foreign-owned US DE | Form **5472 + pro forma 1120**, reportable-transaction and classification gates, year-specific deadline/extension and penalty rules above; **15 April** only for the relevant calendar-year example. [Actual IRS instructions](https://www.irs.gov/instructions/i5472). |
| Singapore ACRA | Non-listed companies normally file within **7 months after FYE**; **8 months** where a share-capital company keeps an overseas branch register. Listed-company routes are **5 / 6 months** respectively. “Within 30 days of AGM” is not the current general rule. All live companies remain subject, including dormant/tax-waived companies; the current page warns of penalties up to **SGD 600**, not an automatic flat **SGD 300**. [ACRA current requirements](https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/filing-annual-returns-companies/deadline-requirements/). |
| Singapore income-tax return | Where a YA 2026 return is required, file by **30 November 2026**, subject to the relevant IRAS waiver. For a company newly incorporated in **2025**, filing is required if its first financial statements closed in 2025 and it derived income or started business that year. IRAS says no YA 2026 filing is required under this new-company branch if its first accounts did not close in 2025, or if they closed but it neither commenced business nor received income that year. The separate dormant-company branch depends on its IRAS status and waiver. Form C-S / C-S (Lite) eligibility and supporting documents are separate. An ACRA filing is not an IRAS filing. **Not yet confirmed:** Singapore-specific penalties and estimated-assessment consequences for failure to file; the Hong Kong reservation does not establish them. [IRAS 2026 season](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-filing-season-2026). |
| Estonia annual report | The annual report is due within **6 months after FY-end**, including a year with no economic activity; use the actual reporting period. The original **EUR 100–3,200** fine range remains unconfirmed. [RIK deadline/inactivity scope](https://www.rik.ee/en/e-business-register/annual-report); [government annual-report guidance](https://www.eesti.ee/en/artikkel/doing-business/accounting-and-reporting/annual-report). |
| UK confirmation statement | Review and file at least every **12 months**, within **14 days** after the review period ends; **GBP 50 online / GBP 110 post** for the applicable fee period. Failure can lead to a fine up to **GBP 5,000** and strike-off, not a universal **GBP 250** charge. [Official statement guidance](https://www.gov.uk/running-a-limited-company/confirmation-statement). |
| UK accounts | Ordinary private-company accounts: **9 months after FY-end**, first accounts normally **21 months after registration**. Private-company late-account bands are **GBP 150 / 375 / 750 / 1,500** for up to **1 month / 1–3 months / 3–6 months / over 6 months**, doubled for **2 consecutive late years**. Filing and tax-return deadlines differ; recover special-period/extension rules before execution. [Official deadlines](https://www.gov.uk/prepare-file-annual-accounts-for-limited-company); [penalty bands and appeal conditions](https://www.gov.uk/annual-accounts/penalties-for-late-filing). |
| Hong Kong NAR1 | Private company generally files within **42 days after incorporation/re-domiciliation anniversary**, except that initial year and the actual declared-dormancy rules. Timely fee **HKD 105**. The FAQ expressly states that its graduated scale is also the private-company scale: **HKD 870** after **42 days** but within **3 months**, **HKD 1,740** after **3** but within **6 months**, **HKD 2,610** after **6** but within **9 months**, and **HKD 3,480** after **9 months**, measured from the applicable anniversary for a private company. Prosecution is separate from the registration fee. [Registry FAQ private-company questions and Q33 scale](https://www.cr.gov.hk/en/faq/local-company/annual-return.htm). |
| Hong Kong profits-tax return | The actual **1 April 2026** IRD notice gives a general **1 month after issue** rule, subject to the actual return and extensions. The **2025/26 Block Extension Letter paragraph 15** allows first profits-tax returns during the year **3 months after issue** without an extension application; its electronic Notice definition specifies **2 months** for that notice route, and represented/e-filed cases have their separate extension conditions. Do not substitute the general **1-month** rule for those routes. Penalty/estimated-assessment conditions remain separately unconfirmed. [Current IRD notice](https://www.ird.gov.hk/eng/ppr/archives/26040102.htm); [actual 2025/26 letter paragraphs 6–21 and footnote 2](https://www.ird.gov.hk/eng/pdf/bel26e.pdf). |
| Dubai free-zone licence | Track the issuing authority's actual renewal date and conditions; the old generic annual-renewal/cancellation assertion does not establish a current licence deadline or the separate corporate-tax filing duty. |

## Mainland-founder structure and remittances

The original proposed structure was **Hong Kong Ltd receiving global payments via Stripe HK / PayPal / Airwallex**, paying service fees under contract to a mainland **个体户**, which issues **增值税普票** for actual services. Retain those as candidate business/payment flows for documented legal/tax and provider eligibility analysis, not a pre-approved offshore arrangement. Keep the real agreement, actual deliverables, invoice and pricing support, including the original proposed market-rate pricing check; those documents alone do not establish deductibility or a special assessed-tax rate.

SAFE's official personal-FX rules distinguish trade/current-account flows from capital-account investment and require the relevant approvals/registration or permitted financial institution channels. The foreign company does not remove the domestic person's applicable controls. The original **USD 50,000 annual personal-remittance limit** is not a universal limit for legitimate business receipts or payments; its exact current facilitation scope and exceptions require their own source. [SAFE articles 10–17 and 27–32](https://www.safe.gov.cn/safe/2022/0818/21330.html).

For a **China resident individual**, the individual-income-tax law includes domestic and foreign income and applies a standard **20%** proportional rate to interest/dividend income, with the stated per-receipt income base. Test actual residence, non-domiciled exemptions, treaties, other relief and the foreign-tax-credit limit before computing tax: the implementation rules have specific foreign-income exemptions and credit-evidence/carryforward terms. This confirms the standard dividend rate, not a universal **20%** charge for every mainland founder or every receipt. The Act separately permits arm’s-length, controlled-low-tax-company and non-commercial-arrangement adjustments. [IIT law articles 1–8](https://www.chinatax.gov.cn/chinatax/n810219/n810744/n3752930/n3752974/c3970366/content.html); [implementation articles 2–6 and 20–22](https://www.chinatax.gov.cn/chinatax/n810219/n810744/n3752930/n3752974/c3963364/content.html).

### Not yet confirmed: mainland flow figures and tax conclusions

| Original proposal | Specific unresolved item |
| --- | --- |
| 个体户 assessed taxation | **0.5%–2%** effective tax is not a generally established national rate; determine current locality, taxpayer, assessment eligibility and actual taxes. |
| Service fee size | A **50% of Hong Kong revenue** ceiling/transfer-pricing scrutiny threshold is unproved; do not use it as a safe harbour or cap. |
| Salary from Hong Kong company | “Hong Kong salaries tax if work performed there” is incomplete; source, residence, employment and relevant treaty/national conditions remain unresolved. |
| Dividends to mainland individual | The **0% Hong Kong dividend withholding / 20% standard China resident-dividend rate** are sourced above. The actual recipient’s residence, exemptions, treaty/credit and reporting conditions remain to be resolved; no gross/net cross-border distribution is computed from the two numbers alone. |
| Service-fee repatriation | Contract + 发票 do not by themselves establish deductibility, lawful forex settlement or the unconfirmed **0.5%–2%** outcome. |
| Personal remittance | Old **USD 50,000/year** must not be used to split business remittances, bypass capital controls or substitute for the actual current-account/capital-account route. |

## Operating agreement and succession

Prepare an LLC operating-agreement analysis covering **membership percentages**, **member-managed versus manager-managed control**, **distribution policy**, **succession/death/incapacity**, and **buy-sell/dissolution/transfer mechanisms**. These are **5 planning subjects**, not a claim that every US state mandates the same written agreement for every single-member LLC. Recover the chosen state's applicable law and coordinate the documents with actual tax classification and estate planning.

For a decedent who was neither a US citizen nor US resident, the IRS says Form **706-NA** is required when US-situated assets at death exceed **USD 60,000**, with applicable estate-treaty conditions and situs exclusions. That is a filing screen, not a universal estate-tax exemption, LLC-interest situs conclusion or amount of tax. The original **up-to-40%** assertion needs the actual rate/estate/credit calculation; the original “foreign holding company such as HK Ltd removes exposure” is not established and must not be implemented as an automatic cure. [IRS situs, exclusions, treaties and filing threshold](https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns).

## Worked comparisons

### Singapore: qualifying start-up and YA 2026 relief

Assume a company meets **every** new-start-up condition above in **YA 2026**, which is within its first **3 consecutive YAs**, and has **SGD 200,000 normal chargeable income** at the **17%** rate. It has no other credits/reliefs, no qualifying **2025 local employee** and no cash-grant entitlement. Exempt income is **SGD 125,000**, leaving **SGD 75,000**, with base tax **SGD 12,750** before the **50% YA 2026 rebate**. The rebate is **SGD 6,375**, below the applicable **SGD 40,000** cap; net tax is **SGD 6,375**. Base effective tax is **6.375%**, and net effective tax **3.1875%** for these supplied facts, not a permanent rate or a consequence of incorporation alone. [IRAS actual scheme and rebate conditions](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes).

```oa-check
name: Singapore qualifying start-up YA2026 base tax and rebate
inputs:
  normal_chargeable_income: 200000
  first_band: 100000
  second_band: 100000
  first_exemption_rate: 0.75
  second_exemption_rate: 0.5
  corporate_rate: 0.17
  rebate_rate: 0.5
steps:
  exempt_income: first_band * first_exemption_rate + second_band * second_exemption_rate
  taxable_after_exemption: normal_chargeable_income - exempt_income
  base_tax: taxable_after_exemption * corporate_rate
  rebate: base_tax * rebate_rate
  net_tax: base_tax - rebate
  base_effective_percent: base_tax / normal_chargeable_income * 100
  net_effective_percent: net_tax / normal_chargeable_income * 100
expected:
  exempt_income: 125000
  taxable_after_exemption: 75000
  base_tax: 12750
  rebate: 6375
  net_tax: 6375
  base_effective_percent: 6.375
  net_effective_percent: 3.1875
```

### Estonia: gross profit versus net distribution

Assume **EUR 100,000** ordinary profit is available for distribution and no exemption, special regime, prior-tax credit, owner-level tax or other taxable payment applies. At the standard **22/78** net-distribution rate, distribute **EUR 78,000** and pay **EUR 22,000** corporate tax. The tax is **22% of the gross EUR 100,000**, or **22/78 of EUR 78,000**; it is not **22% of the net dividend**. A foreign owner's tax remains a separate calculation. [EMTA actual standard distribution tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes).

```oa-check
name: Estonia gross available profit and net distribution
inputs:
  profit_available: 100000
  net_share: 0.78
  distribution_tax_numerator: 22
  distribution_tax_denominator: 78
steps:
  net_dividend: profit_available * net_share
  corporate_tax: net_dividend * distribution_tax_numerator / distribution_tax_denominator
  gross_use: net_dividend + corporate_tax
expected:
  net_dividend: 78000
  corporate_tax: 22000
  gross_use: 100000
```

## Not yet confirmed: commercial prices, times and implementation

These individually retained old amounts and process claims are **not current quotes or authorised instructions**. Official registry/tax recovery above establishes only its stated narrower findings. The named providers' products, supported countries, KYC, licences, account opening and processing promises require their own current first-party terms. A successful company registration never guarantees their approval.

| Original country / commercial item | Precise legacy proposal requiring current proof |
| --- | --- |
| Wyoming package | **USD 100–500 setup, 1–3 days, USD 60–600 annual**; actual official state fees/timing above supersede the corresponding component. **Mercury remote opening / Wise Business** and no-substance/no-US-liability outcomes are not established. |
| Delaware package | **USD 90 filing, 1–2 days, USD 300+ annual**, **Stripe Atlas USD 500**, **Mercury / Atlas pipeline**: current domestic LLC formation filing is **USD 110** and annual LLC tax **USD 400** above; recover any other entity-specific charges and actual commercial quote. |
| Stripe Atlas sequence | Original **USD 500 → Delaware C-Corp → EIN → Mercury → Stripe activation in 1–2 weeks** is not an assured sequence. The Atlas commercial discovery result does not establish this universal pipeline, current contractual terms or bank approval; its captured tool response was a rewritten summary, not a primary fee/contract read. |
| Singapore package | Original **SGD 300–800 setup / 1–2 days / SGD 3,000–5,000 annual**, nominee **SGD 2,000/year**, **DBS / OCBC** in-person possibilities. State name/registration fees are **SGD 315** above; the remaining prices/timing/KYC need quotes and actual eligibility. |
| Estonia package | Original **2–4 weeks / EUR 500–1,500 annual**, **Wise Business / LHV**; current application/registration fees total **EUR 415** above, while commercial annual costs, timings and the original fully remote administration promise remain unconfirmed. |
| Dubai package | Original **AED 5,000–15,000 setup / 3–10 days / AED 10,000–20,000 annual**, licence+visa+office+insurance and **Emirates NBD / Mashreq / Wise**. Recover the particular DMCC/IFZA/Meydan licence/package and actual banking terms. |
| UK package | Original same-day completion, **GBP 200–500 annual** and **Wise Business / Revolut Business**; current official formation service says usually **24 hours** and does not establish all-in costs or account approval. |
| Hong Kong package | Original **HKD 3,000–5,000 (USD 400–650) setup / 1–2 weeks / HKD 5,000–10,000 annual**, **HSBC / ZA Bank / Airwallex HK / Stripe HK** and no-forex-control shortcut; none is a current all-in quote or lawful-remittance conclusion. |

### Original annual-cost comparison: budget recovery only

Every row is an **unconfirmed historical USD budget**, not a current “year 1” recommendation. The original total is retained to identify the precise quote to replace; fees, exchange rates, tax and service inclusions may have changed. Confirm which annual costs fall in year 1 to avoid double counting.

| Original structure | Setup / maintenance / accounting | Original total to replace |
| --- | --- | --- |
| Wyoming LLC | **160 / 60 / 500–1,500** | **720–1,720**; replace state components from the current fee schedule and obtain provider quotes. |
| Delaware LLC | **390 / 300 / 500–1,500** | **1,190–2,190**; maintenance assumption is superseded by the current **400** annual state tax, before other costs. [Current Delaware component](https://corp.delaware.gov/alt-entitytaxinstructions/). |
| Stripe Atlas DE C-Corp | **500 / 300 / 1,000–3,000** | **1,800–3,800**; the LLC annual tax is not the C-corporation franchise-tax calculation. |
| Hong Kong Ltd | **500 / 800–1,500 / 800–1,500** | **2,100–3,500**; replace with current HKD state charges and commercial quotes, with dated currency conversion. |
| Estonia OÜ | **600 / 300–500 / 600–1,200** | **1,500–2,300**; replace the assumed application/registration and accounting/agent costs separately. |
| UK Ltd | **60 / 200 / 500–1,500** | **760–1,760**; original USD setup figure is not the current GBP statutory fee. |
| Singapore Pte. Ltd. | **800 / 3,000–5,000 / 1,000–2,000** | **4,800–7,800**; current statutory fees do not establish nominee/accounting quotations. |
| Dubai Freezone | **3,000 / 3,000–5,000 / 1,000–2,000** | **7,000–10,000**; recover actual authority, activity, visa/office and renewal package. |

### Not yet confirmed: remaining national obligations

| Original item | Specific recovery required |
| --- | --- |
| Estonia annual report / late fine | The **6-month** deadline/inactivity obligation is now supported above. The **EUR 100–3,200** fine range and current enforcement grounds/procedure remain unrecovered; the registry guidance is not a complete current penalty computation. Do not treat all non-filing as an automatic fixed fine. |
| Hong Kong NAR1 late scale | The original **HKD 870–3,480** range is now resolved into the sourced graduated registration-fee bands above. Any separate prosecution fine, relief and company-specific filing/dormancy eligibility still need their actual conditions; the registration fee is not a universal all-penalties amount. |
| Hong Kong profits-tax return | The general **1-month** deadline is now addressed above using the current IRD notice. Obtain the actual return, assessment year and applicable extension; penalty and estimated-assessment conditions remain separately unconfirmed. |
| Hong Kong dividend recipient | The actual **0% Hong Kong dividend-withholding** finding is now sourced above; no worldwide recipient exemption, mainland-credit result or transaction-specific net distribution follows. |
| Dubai licence renewal | Original annual renewal and licence cancellation: obtain the actual authority's licence and conditions; this is separate from tax registration/return/visa/immigration work. |
| Home-country overlays | The sourced standard China resident-dividend **20%** rate above does not settle actual exemptions/credits. Taiwan domestic/foreign-company choice, complete US CFC reporting and Indian treaty advantage remain unresolved by foreign-company registration; recover the actual supplied-fact rules. |

## Company closure and winding down

Plan dissolution, creditor settlement, final accounts/returns and the actual company's registrations before stopping operations. Dormancy or a strike-off application does not itself close every tax, employee, bank, visa or contractual obligation. The current Hong Kong Registry expressly requires continuing annual-return and statutory compliance until dissolution. The original universal claim that penalties, late fees and government liens continue to accrue on every dormant entity requires jurisdiction-specific grounds; no automatic lien or fixed charge is established here. [Registry closure FAQ](https://www.cr.gov.hk/en/faq/local-company/dereg-striking-off-winding-up.htm).

| Original jurisdiction / process | Current finding or individual unresolved boundary |
| --- | --- |
| Wyoming: Articles of Dissolution + settle debts + final tax return | June **2026** official LLC fee schedule lists **USD 60** for amendment/dissolution/other filing, superseding the old **USD 0** state-fee claim. The original **1–3 months** and complete final-tax procedure need separate recovery. [Official fee schedule](https://sos.wyo.gov/Business/Docs/BusinessFees.pdf). |
| Delaware: Certificate of Cancellation + final franchise tax | Current domestic LLC cancellation filing is **USD 220**, with all state taxes through the effective cancellation date paid before filing; the official form requires an authorised signatory and the exact name/formation date. Copies/expedited service cost extra. The original **USD 200+ / 1–3 months** is not a total current quote or guaranteed completion time. [Actual cancellation instructions](https://corpfiles.delaware.gov/LLC_Forms/Cancellation%20-%20LLC%20-%20domestic.pdf); [August 2026 fee schedule](https://corpfiles.delaware.gov/Fee_Schedule/AugustFee2026.pdf). |
| Singapore: ACRA strike-off or voluntary winding-up | The current **strike-off application is free**; service-provider fees and voluntary winding-up costs differ. The company must have stopped/never started business, no unpaid government debts/issues, registered charges, litigation, regulatory/disciplinary proceedings, property/debts/potential claims, and all or a majority of directors agree. Clear tax credits and court summons and update information. In Bizfile select **Deregister → Local company → Apply to strike off business entity**, verify the company, confirm criteria and cessation/reason; required director endorsement must occur within **14 days** or the application lapses, with the stated CSP exception. The company remains live after approval. Applications from **20 October 2026** take at least **2 months** after approval, with a **60-day** First Gazette objection period and Final Gazette dissolution if unobstructed; earlier applications use the separate at-least-**3-month** process. Unresolved objections can lapse the process. The old **SGD 30–3,000+ / 3–6 months** is not a current all-route quote. [Actual current ACRA procedure, criteria and period split](https://www.acra.gov.sg/manage/companies/closing-a-local-company/striking-off/). |
| Estonia: liquidation through e-Business Register | Original **EUR 200–500 / 3–12 months** remains unconfirmed; recover actual liquidation/creditor/filing and tax requirements. |
| UK: DS01 strike-off or voluntary liquidation | Current fees table lists **GBP 13 online / GBP 18 paper**; the general apply page states **GBP 18** without that channel split. Use the authority's current route-specific fee confirmation before payment, not the old **GBP 10**. DS01 needs a majority of directors; deal with assets first, as remaining assets pass to the Crown. The notice period is **2 months** if nobody objects, not a guaranteed **3–6-month** total. Actual eligibility and creditor notifications still need the full chosen-route procedure. [Fee schedule](https://www.gov.uk/government/publications/companies-house-fees/companies-house-fees); [apply page](https://www.gov.uk/strike-off-your-company-from-companies-register/apply-to-strike-off). |
| Hong Kong: deregistration or voluntary winding-up | Deregistration is for eligible defunct solvent local private/guarantee companies: all members agree; no business during the preceding **3 months** or never commenced; no outstanding liabilities or proceedings; no HK immovable property in company/subsidiary assets; IRD no-objection notice. Submit NDR1 within **3 months** of that notice with fee. Registry strike-off is a Registrar power, not a company application. The original **HKD 690 / 5–7 months** is not a verified total fee/time; recover the route-specific charges and tax clearance. [Registry FAQ Q1–Q3/Q13](https://www.cr.gov.hk/en/faq/local-company/dereg-striking-off-winding-up.htm). |
| Dubai: cancel licence, deregister and cancel visa | Original **AED 2,000–5,000 / 2–4 months** remains unconfirmed. Obtain the actual licensing, tax, immigration, employment and bank closure sequence and clear liabilities. |

## Output and checks

Provide a comparison of the same feasible entity options showing sourced tax assumptions, lawful funding, official fees versus dated service quotes, banking eligibility, owner/company residence and continuing duties. Attach the calendar, unresolved-source list, proposed ownership/operating agreement and exit steps. Stop before implementation where an item needed for the choice remains unresolved.

Do not promise tax-free foreign LLC profits, a guaranteed offshore exemption, escape from exchange controls, a nationality-only entity choice, assured bank/payment approval, a universal written-LLC-agreement mandate, or an automatic foreign-holding-company estate-tax cure. Do not treat the old **USD 100,000** referral breakpoint as permission to skip professional review for lower-value or life-changing decisions.

## Footer notes

*Data reflects 2024–2026 rules. For amounts >$100,000 USD or life-changing decisions, verify current rules with a qualified advisor in each relevant jurisdiction.*
*Original content: [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise) — MIT License.*
*OpenAccountants — open-source accounting skills for AI — info@openaaccountants.com*

The original footer is preserved verbatim as attribution/contact text; its historical date umbrella is superseded by the specific checked sources and explicit reservations above.

## Sources

Official sources were actually opened and read in the stated operative scopes on **2026-11-16**; these are research findings. Not yet approved. IRS LLC, ECI, FDAP, Forms 5472/1120, self-employment and estate scopes; Wyoming official form, annual report and June 2026 fee schedule; Delaware LLC instructions; IRAS rate/exemption/current YA 2026 rebate/dividend/non-taxable-income/filing scopes; ACRA registration/officers/fees/annual-return scopes; EMTA distribution-tax and e-Residency residence/fee scopes; UAE Ministry-hosted unofficial English consolidation articles3,11–12,18–19 (Arabic original not read), plus Decision116 article 2 and natural-person scope; UK formation/fees/relief/confirmation/accounts/penalties/closure scopes; Hong Kong territorial/FSIE/two-tier/annual-return/closure scopes; RBI LRS A1–A6 and SAFE10–17,27–32. Each operative section links its actual source. Unread full-corpus details and unresolved national/provider figures are explicitly limited above.

| Source / actual read scope | Official URL | Read date |
| --- | --- | --- |
| Read for: IRS: classification/EIN/employment-excise distinctions; ECI/FDAP scope and exceptions | [LLC](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies); [ECI](https://www.irs.gov/individuals/international-taxpayers/effectively-connected-income-eci); [FDAP](https://www.irs.gov/individuals/international-taxpayers/fixed-determinable-annual-periodical-fdap-income) | 2026-11-16 |
| Read for: IRS: 5472 definitions/exceptions/DE filing/extension/penalties/Part V; 1120 due date and Schedule J line1a; SE rate/cap; estate situs/treaty/filing scope | [5472](https://www.irs.gov/instructions/i5472); [1120](https://www.irs.gov/instructions/i1120); [SE](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes); [estate](https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns) | 2026-11-16 |
| Read for: Wyoming: actual LLC form instructions; annual-report substantive instructions; June 2026 LLC fee schedule with neighboring categories | [Form](https://sos.wyo.gov/Forms/Business/LLC/LLC-ArticlesOrganization.pdf); [report](https://wyobiz.wyo.gov/Business/AnnualReport.aspx); [fees](https://sos.wyo.gov/Business/Docs/BusinessFees.pdf) | 2026-11-16 |
| Read for: Delaware: complete operative LLC/LP/GP tax instructions, not C-corporation law | [Instructions](https://corp.delaware.gov/alt-entitytaxinstructions/) | 2026-11-16 |
| Read for: IRAS: rate/current YA 2026 rebate+grant interaction/start-up exemption and qualifying conditions+neighbors; dividend paragraph; capital/revenue distinction; YA 2026 Step 3 new-company eligibility exceptions, dormant-company status and filing/waiver | [Rate/relief](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes); [dividends](https://www.iras.gov.sg/taxes/withholding-tax/payments-to-non-resident-company/payments-that-are-not-subject-to-withholding-tax); [income](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/taxable-non-taxable-income); [filing](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-filing-season-2026) | 2026-11-16 |
| Read for: ACRA: fees table; officers lines 37–55 / 101–117; registration lines 46–114; annual-return requirements lines 36–88 | [Fees](https://www.acra.gov.sg/manage/companies/service-transaction-fees/); [officers](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/appointing-company-directors-other-key-officers/); [register](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/registering-via-bizfile/); [annual](https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/filing-annual-returns-companies/deadline-requirements/) | 2026-11-16 |
| Read for: Estonia: EMTA lines307–353 distribution-tax/rate/transition and government taxable-payments paragraphs18–31 non-business scope; e-Residency residence caution; state-fee table updated 13 November | [Tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes); [non-business payments](https://learn.e-resident.gov.ee/hc/en-gb/articles/360002559718-Taxable-payments); [residence](https://www.e-resident.gov.ee/taxes-in-estonia/); [fees](https://learn.e-resident.gov.ee/hc/en-gb/articles/11432057891473-Estonian-state-fees) | 2026-11-16 |
| Read for: UAE: Ministry-hosted unofficial English consolidation3,11–12,18–19 with neighbors, Arabic original not read; complete Decision116; complete natural-person operative scope | [Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [Decision116](https://mof.gov.ae/wp-content/uploads/2023/02/Cabinet-Decision-No-116-of-2022-on-CT-Article-3-Threshold-1.pdf); [natural person](https://tax.gov.ae/en/taxes/corporate.tax/corporate.tax.topics/basis.of.taxation.natural.person.aspx) | 2026-11-16 |
| Read for: UK: formation and fee-table first section; complete relief scope; statement lines 63–117; account deadlines lines 60–86; penalties lines 61–110; apply-to-strike-off operative page | [Formation](https://www.gov.uk/limited-company-formation/register-your-company); [fees](https://www.gov.uk/government/publications/companies-house-fees/companies-house-fees); [tax rates](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax); [relief](https://www.gov.uk/guidance/corporation-tax-marginal-relief); [statement](https://www.gov.uk/running-a-limited-company/confirmation-statement); [accounts](https://www.gov.uk/prepare-file-annual-accounts-for-limited-company); [penalties](https://www.gov.uk/annual-accounts/penalties-for-late-filing); [closure](https://www.gov.uk/strike-off-your-company-from-companies-register/apply-to-strike-off) | 2026-11-16 |
| Read for: Hong Kong: territorial scope/rate; FSIE covered income/exclusions/MNE/receipt/exception architecture; two-tier Q1–Q13; annual-return private-company questions and Q33 scale; closure Q1–Q3 / Q13 with neighbors | [Profits](https://www.ird.gov.hk/eng/tax/bus_pft.htm); [FSIE](https://www.ird.gov.hk/eng/tax/bus_fsie.htm); [two-tier](https://www.ird.gov.hk/eng/faq/2tr.htm); [annual](https://www.cr.gov.hk/en/faq/local-company/annual-return.htm); [closure](https://www.cr.gov.hk/en/faq/local-company/dereg-striking-off-winding-up.htm) | 2026-11-16 |
| Read for: further recovered national scopes: RIK annual report lines 62–70 and government line 161; ACRA strike-off lines 46–101 / 120–185 plus exceptions; Delaware cancellation whole 3-page form and August 2026 LLC formation/cancellation table; IRD April2026 notice lines 160–176 and actual 2025/26 letter paragraphs1–21 with footnotes 1–2 (remaining pages retrieved only) | [RIK](https://www.rik.ee/en/e-business-register/annual-report); [Estonia](https://www.eesti.ee/en/artikkel/doing-business/accounting-and-reporting/annual-report); [ACRA closure](https://www.acra.gov.sg/manage/companies/closing-a-local-company/striking-off/); [Delaware cancellation](https://corpfiles.delaware.gov/LLC_Forms/Cancellation%20-%20LLC%20-%20domestic.pdf); [Delaware fees](https://corpfiles.delaware.gov/Fee_Schedule/AugustFee2026.pdf); [IRD notice](https://www.ird.gov.hk/eng/ppr/archives/26040102.htm); [extension letter](https://www.ird.gov.hk/eng/pdf/bel26e.pdf) | 2026-11-16 |
| Read for: further original mainland/dividend scopes: IIT law articles 1–8 and implementation articles 2–6 / 20–22 with neighbors; complete FSTB policy page, dividend-withholding statement only (other broad tax summaries not adopted) | [IIT law](https://www.chinatax.gov.cn/chinatax/n810219/n810744/n3752930/n3752974/c3970366/content.html); [implementation](https://www.chinatax.gov.cn/chinatax/n810219/n810744/n3752930/n3752974/c3963364/content.html); [HK withholding](https://www.fstb.gov.hk/en/treasury/general/prevailing-tax-policy.htm) | 2026-11-16 |
| Read for: funding: RBI LRS A1–A6 plus adjacent conditions; SAFE personal-FX articles 10–17 / 27–32 with immediate neighbors | [RBI](https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10192); [SAFE](https://www.safe.gov.cn/safe/2022/0818/21330.html) | 2026-11-16 |

**Not yet confirmed:** Each specific unresolved amount, condition, provider outcome, home-country overlay, old annual-cost budget and remaining closure procedure is individually retained in the explicitly unusable tables above. The original annual-report/late-fee, personal-tax, estate-rate and foreign-holding-company assertions are not filing-ready. The Atlas rewritten commercial-discovery response is not a primary contract/fee read, government-source endorsement or validated current quote.
