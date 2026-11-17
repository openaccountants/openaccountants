---
name: ifrs-local-gaap-reconciliation
description: Reconcile IFRS Accounting Standards with an identified local framework at transaction level. Covers IFRS, US GAAP, German HGB, UK and Republic of Ireland FRS 102, Italian OIC, French PCG, Indian Ind AS, Chinese ASBE, Japanese J-GAAP, Brazilian CPC and Canadian ASPE, with individually identified source and adoption limits. Use before booking a cross-GAAP adjustment or preparing comparative recognition, measurement, presentation, disclosure and transition bridges. Load financial-reporting-workflow-base.
version: 0.2
jurisdiction: GLOBAL
last_updated: 2026-11-16
depends_on:
  - financial-reporting-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-reporting
type: cross-country-method
standard: IFRS Accounting Standards and selected national frameworks
effective_date: 2026-11-16
source_checked: 2026-11-16
---

# IFRS and local GAAP reconciliation

## Scope

**Coverage is partial.** This is a Tier 2 source-cited draft; current ASC, Canadian Handbook and individually identified national implementation gaps below remain outside usable accounting instructions.

Prepare a transaction-level reconciliation and reviewer brief between IFRS Accounting Standards and the identified local framework. Load `financial-reporting-workflow-base`; the original `financial-statements-workflow-base` dependency was not an existing parent. This is a source-cited draft, not an accountant attestation or a substitute for the actual applicable national standard.

The revision date **2026-11-16** is an internal Guide revision date, not a common effective date for these frameworks. Identify annual and interim periods, comparatives, transition date, early-adoption elections and the entity's legal reporting obligations before choosing any rule. IFRS as issued by the IASB, EU-endorsed IFRS and a national IFRS-equivalent framework are different bases; check current endorsement and national commencement rather than treating publication as adoption. The 2026-issued IFRS texts include future amendments. Apply each amendment's own gate.

The original framework routes remain: US GAAP/ASC; German HGB and applicable DRS; UK and Republic of Ireland FRS 102, including Section 1A; Italian OIC and the original Civil Code articles 2423–2435 research lead; French PCG/ANC; Indian Ind AS under the Companies (Indian Accounting Standards) Rules 2015 route; Chinese ASBE; Japanese J-GAAP/ASBJ; Brazilian CPC and the separate CPC-PME route; and Canadian ASPE/Handbook Part II. This Guide does not establish that a particular entity is eligible for one of those frameworks. National differences explicitly reserved under Sources cannot be used to book an adjustment.

Exclude local filing portals/XBRL/audit thresholds, tax computations beyond scoped current/deferred-tax accounting, audit opinion construction and jurisdiction-specific first-time-adoption execution. Route those separately. Industry-specific extractives GAAP is excluded. Insurance and banking require their actual sector standards: the original IFRS 17/ASC 944 and IFRS 9/ASC 326 comparison leads do not make this a complete industry manual. Every final reconciliation requires a credentialed practitioner with the relevant dual-GAAP competence.

## Ask the client first

Obtain the entity/group chart, public-accountability and public/private/SEC status, legal reporting basis, reporting and comparative dates, previous statements, accounting policies and adoption elections. Obtain the trial balance, consolidation adjustments, material contracts, valuations, acquisition/lease/development/credit-loss workpapers, functional currencies, cash-flow classifications, tax bases and tax-rate evidence. Identify covenants and materiality. Do not infer a framework or policy from the company's country or size alone.

## The method, step by step

### Identify both frameworks and periods

Record IFRS-as-issued versus IFRS-as-endorsed, the exact local standard edition and applicable entity scope. For US GAAP distinguish current ASC text, amendment evidence and an unadopted or superseded amendment. For FRS 102 distinguish pre-review accounting, the Periodic Review 2024 amendments and the later adapted-format amendments. The original generic Ind AS 2024 and China 2024 supplementary-guidance labels are not a complete current-law source register.

### Walk each transaction and difference

For every material balance or transaction, record both recognition decisions, measurement basis, presentation and disclosure; cite the operative paragraphs and exceptions on both sides. A common project or broadly converged framework does not establish identical outcomes. A difference may be zero, temporary, permanent, presentation-only or disclosure-only. Do not manufacture an adjusting journal where only disclosure changes.

### Prepare and reconcile the entries

Show each debit/credit, income-statement effect, equity effect, balance-sheet movement and cash-flow reclassification. Distinguish current-period expense from opening-equity transition and prior-period restatement. Assess tax effects under the applicable tax-accounting framework with separately sourced tax bases/rates; a book adjustment is not automatically a taxable deduction. Reconcile the net-income, equity, balance-sheet and, where required, operating-cash-flow bridges to the same trial balance.

### Apply first-time adoption separately

IFRS 1 requires an opening IFRS statement of financial position, consistent policies based on standards effective at the first IFRS reporting-period end, and its specific exceptions/exemptions. Ordinary standards' transition provisions do not automatically replace IFRS 1. Opening adjustments normally enter retained earnings or another appropriate equity category. Explain the transition's financial-position, performance and cash-flow effects; prepare the equity and comprehensive-income reconciliations and material cash-flow explanations in .23–.25. Do not describe a generic PAT bridge as the complete statutory IFRS 1 disclosure. The deemed-cost choices in D5–D8 have asset, measurement and timing conditions; they are not an unrestricted election to retain every previous-GAAP balance. [IFRS 1.6–.11, .23–.25, D5–D8](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs1.html).

## Difference catalogue

Each row is a screening instruction. Use the linked topic Guide for its scoped computation, then obtain any missing local rule before booking the bridge. The individually retained US comparisons in Sources are research requests, not cleared current ASC instructions.

### Revenue recognition

IFRS 15 uses contract identification, performance obligations, transaction price, allocation and satisfaction of obligations. Variable consideration uses expected value or most-likely amount according to which better predicts entitlement, consistently for the uncertainty, and must meet the constraint; a licence's use/access conclusion follows the complete B58–B61 conditions, including significant effect on form/function **or** benefits substantially dependent on activities. An eligible right-to-access licence is recognised over time; an eligible right-to-use licence is recognised at the point when the customer can use and benefit from it, subject to the complete commencement conditions. Incremental contract-acquisition costs require expected recovery, amortise the recognised asset systematically consistent with transfer of the related goods/services, with the amortisation-period **1 year or less** expense practical expedient; principal/agent depends on control of the specified good/service. Use `ifrs15-revenue` for all conditions. Do not presume a zero IFRS/ASC 606 bridge merely because the standards were jointly developed. [IFRS 15.9, .22, .31, .47, .53–.59, .73, .91–.94, .99–.100, B34–B38, B58–B61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html).

German HGB's realisation/prudence principles do not establish a universal delivery-date rule for every licence or an enforceability-only variable-consideration test. The revised FRS 102 Section 23 uses its own 5-step model for periods within the applicable adoption gate; it contains accommodations and scope exclusions and is not a statement of complete IFRS 15 identity. Japanese revenue convergence and the old FY2021/2018 assertions remain individually reserved below. [HGB §252](https://www.gesetze-im-internet.de/hgb/__252.html); [FRS 102.1.37, .23.1–.23.5](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf).

### Leases

IFRS 16 has a lessee recognition model with elected short-term and low-value exemptions. A short-term lease is **12 months or less** at commencement and contains no purchase option; **12 months exactly** is not automatically capitalised. The operative Standard contains no USD 5,000 exemption cap. Assess the underlying asset when new, per asset, including independence and sublease restrictions. Recognition, depreciation, interest, modifications and sale-and-leaseback depend on their separate conditions. Where the asset transfer qualifies as a sale under IFRS 15, the seller-lessee recognises only gain/loss relating to rights transferred and measures the retained ROU proportionately; off-market terms and failed-sale financing follow their separate rules in .101–.103; a front-loaded total expense or EBITDA difference is not universal. Use `ifrs16-leases` and the separately source-limited `us-gaap-asc842-leases` comparison. [IFRS 16.5–.8, .22–.38, .99–.103, B3–B8 and Appendix A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html).

For FRS 102 periods applying the Periodic Review 2024 amendments, Section 20 requires a lessee ROU asset and lease liability subject to its own scope/exemptions. The old blanket operating-lease-off-balance-sheet comparison is not a calendar-2026 default. HGB economic attribution requires the actual contract and §246; that paragraph alone does not establish that most operating leases remain off balance sheet. Japanese lease adoption is addressed below. [FRS 102.1.37, .20.1–.20.12, .20.45](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf); [HGB §246(1)](https://www.gesetze-im-internet.de/hgb/__246.html).

### Financial instruments: impairment

IFRS 9's loss-allowance scope includes specified amortised-cost/FVOCI assets, lease receivables, contract assets, loan commitments and financial guarantees. In the general model, significant credit-risk increase leads to lifetime ECL and otherwise 12-month ECL, subject to the specific exceptions. Purchased/originated credit-impaired assets use cumulative changes in lifetime ECL; specified trade receivables/contract assets require lifetime ECL, while other specified receivable categories have policy choices. It is false to treat every IFRS day-one allowance as 12-month ECL or to assume a universally smaller allowance than US GAAP. Recover ASC 326's actual amortised-cost and available-for-sale scope and model separately; held-to-maturity debt is not a US-only addition to an otherwise identical scope. [IFRS 9.5.5.1–.5.5.16](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html).

### Financial instruments: classification and measurement

IFRS 9 financial-asset classification depends on the business model and contractual cash-flow characteristics, with amortised-cost and FVOCI conditions, a residual FVPL category and separate designation/election provisions. The equity FVOCI election is irrevocable at initial recognition for eligible instruments neither held for trading nor acquisition contingent consideration; OCI amounts do not subsequently recycle to profit or loss, though transfers within equity are permitted. Apply the actual current contract terms and amendments before an SPPI conclusion. The old US cost/observable-price-change wording and debt/equity category equivalence are individually reserved below. [IFRS 9.4.1.1–.4.1.5, .5.7.5–.5.7.6, B5.7.1](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html).

### Goodwill

IFRS 3's subsequent goodwill basis is cost less accumulated impairment; apply IAS 36's CGU allocation, annual/indicator tests, higher-of recoverable amount, allocation floors and prohibition on reversing goodwill impairment. The asset is not an IAS 38 development asset. Use `ifrs3-business-combinations` for the complete conditions, including partial-goodwill testing. HGB and FRS 102 require useful-life amortisation with their distinct exceptional **10-year** rules; Japan's rule allows no more than **20 years**, with method and immateriality qualifications below. Do not use the old HGB **5-year** fallback or ASPE **40-year** assertion. US private-company **10-year** alternatives and public-entity impairment mechanics still require current ASC scope and elections. [IFRS 3.B63(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html); [IAS 36.80, .90, .104–.105, .124](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias36.html).

### Inventory

IAS 2 uses specific identification for its .23 items and FIFO/weighted-average for the others; it does not permit LIFO. A subsequent NRV recovery reverses a prior write-down only to the original write-down limit, leaving the lower of cost and revised NRV. Document quantity, cost layers, previous write-down and revised NRV before any LIFO-reserve or reversal bridge. The original US LIFO/conformity and no-reversal comparison remains a specific current-source request, not a cleared tax or accounting conclusion. [IAS 2.23–.33](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html).

### Property, plant and equipment

IAS 16 permits the cost or revaluation model by class and requires separate depreciation of significant parts. IAS 36 reversal requires a changed estimate of recoverable amount and is capped by the carrying amount that would exist without the earlier impairment; a revalued asset also has the applicable revaluation treatment. A changed indicator alone does not determine the reversal amount. HGB has the cost ceiling, impairment and reversal rules in §253, including the separate goodwill no-reversal exception. US revaluation/component-depreciation/ASC 360 reversal and the old HGB no-component assertion remain individually reserved. [IAS 16.29–.31, .36, .43](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html); [IAS 36.110–.121](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias36.html); [HGB §253](https://www.gesetze-im-internet.de/hgb/__253.html).

### Intangibles, research and development

IAS 38 expenses research. Development capitalisation starts only when all **6** criteria are demonstrated: technical feasibility, intention, ability to use/sell, probable economic benefits, resources and reliable attributable-cost measurement. Earlier expense is not reinstated as an asset. Amortisation begins when an eligible finite-life asset is available for use; indefinite-life assets have different subsequent requirements. It is false that all IFRS R&D is expensed or that every software project must be capitalised. The original US R&D/software exceptions require current ASC 730/985-20/350-40 text. [IAS 38.54–.57, .65, .71, .97, .107–.108](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias38.html).

### Borrowing costs

IAS 23 requires capitalisation of directly attributable borrowing costs for a qualifying asset and expenses other borrowing costs, subject to its stated exceptions. A qualifying asset necessarily takes a substantial time to prepare. Fair-value qualifying assets and large-quantity repetitive inventories have scope relief; capitalisation starts only when expenditure, borrowing costs and preparation activities coexist, is suspended during qualifying extended interruptions and ceases when substantially all preparation is complete. It is not a rule to capitalise every fixed asset or every long-cycle inventory. FRS 102's class-consistent policy choice is below. The original general US equivalence and construction-inventory distinction remain reserved. [IAS 23.1, .4–.10, .17–.22](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias23.html).

### Provisions

IAS 37 recognition requires a present legal/constructive obligation from a past event, probable outflow and reliable estimate; probable means more likely than not in this context. Measure the best estimate using the relevant population/individual-obligation analysis; discount when time value is material, applying its rate and risk conditions. The original US **70%–80%** shorthand is not an authoritative universal probability threshold, and no conclusion that IFRS always recognises more provisions at smaller amounts follows. Preserve the actual recognition and amount questions separately. [IAS 37.14–.26, .36–.47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias37.html).

### Employee benefits

The relevant Standard is **IAS 19**, not IFRS 19. For defined-benefit plans use the projected-unit-credit method, asset-ceiling conditions, the applicable high-quality-corporate-bond market yield with government-bond fallback where there is no deep market in that currency, and matching currency/term. Service cost/net interest normally enter profit or loss unless another Standard requires/permits asset inclusion; remeasurements enter OCI without later profit-or-loss recycling. Net interest uses the applicable discount rate on the net defined-benefit liability/asset, taking account of the required contribution/benefit-payment and other specified adjustments. The original universal “AA bonds” and US corridor-abolished assertion are not cleared rules. [IAS 19.57, .67, .83–.86, .120–.130](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias19.html).

### Income taxes

Identify the accounting carrying amount and tax base under IAS 12 before measuring temporary differences and applying recognition exceptions. IFRIC 23 requires a separate/combined uncertainty assessment that better predicts resolution and assumes examination with full information. If acceptance is probable, follow the tax filing treatment; otherwise use the most-likely amount or expected value, whichever better predicts resolution, and reassess changed facts. This is not a universal choice to minimise a tax provision. US ASC 740 recognition/measurement, intra-entity inventory versus other assets and the original exact cumulative-probability boundary remain individually reserved. [IAS 12.7–.11, .15, .24](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias12.html); [IFRIC 23.4–.14](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric23.html).

### Foreign exchange and hyperinflation

IAS 21 gives priority to the primary functional-currency indicators, supported by the additional indicators; management cannot simply choose the parent's currency. Initial foreign-currency transactions use transaction-date spot rates; closing monetary items use the closing rate, while historical-cost and fair-value non-monetary items follow their separate dates. Apply the specific profit-or-loss/OCI exceptions. IAS 29 applies where the functional currency is hyperinflationary; **3-year** cumulative inflation approaching or exceeding **100%** is an indicator, not an absolute trigger. Lack-of-exchangeability amendments apply to annual periods beginning on or after **2025-01-01**, with their estimation/disclosure/transition requirements. Do not borrow the original US “same threshold” or remeasurement conclusion without current ASC 830. [IAS 21.9–.14, .21–.23, .28, .19A, .57A–.57B, .60L–.60M](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias21.html); [IAS 29.1–.4](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias29.html).

### Consolidation

IFRS 10 control requires power, exposure/rights to variable returns and the ability to use power to affect returns, with reassessment for changed facts. Its investment-entity exception and the subsidiary service-provider qualification require separate analysis; do not convert it into an exemption for every investment subsidiary. Common-control combinations are outside IFRS 3's scope; that exclusion does not itself prescribe pooling. The original US voting/VIE, primary-beneficiary and investment-company outcomes, and national consolidation alternatives, require their own actual current text. [IFRS 10.5–.9, .31–.33](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs10.html); [IFRS 3.2(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html).

### Business combinations

IFRS 3 permits acquisition-by-acquisition fair-value or proportionate-net-asset measurement only for NCI components that are present ownership interests entitling holders to a proportionate share of net assets on liquidation. Other NCI components use fair value unless another IFRS requires a different basis. Contingent consideration's equity/liability conclusion requires the actual instrument and IAS 32/other applicable conditions; do not classify from a variable-amount label alone. Acquisition-related costs are expensed as incurred and services are received, except debt/equity issue costs follow their applicable standards. Use `ifrs3-business-combinations` and `ias32-debt-vs-equity`; the original US always-fair-value NCI, same earn-out classification and expense assertions remain current-source requests. [IFRS 3.19, .40, .53, .58](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html).

### Cash flows

Preserve separate classification questions for interest paid/received, dividends paid/received and income taxes. The original pre-IFRS 18 policy alternatives, operating/financing for interest paid and dividends paid, operating/investing for interest/dividends received, and operating income taxes unless specifically identifiable with investing/financing, are retained as **Not yet confirmed for an entity not applying IFRS 18** because the relevant required-edition IAS 7 text was not recovered here. The 2026-issued IAS 7 includes IFRS 18-linked amendments; do not apply those to every 2026 preparer. For an actual IFRS 18 adopter, analyse .33A/.34A–.34D and .64 with the main-business-activity qualifications. The original US operating-only versus financing classifications need current ASC 230 and exceptions. [IAS 7.33A–.34D, .64](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html).

### Presentation: IFRS 18

IFRS 18 applies to annual reporting periods beginning on or after **2027-01-01**; earlier application is permitted with disclosure. It classifies profit-or-loss income/expenses into **5** categories: operating, investing, financing, income taxes and discontinued operations. Required subtotals include operating profit/loss and profit/loss before financing and income taxes, with the .73 specified financing-business exception. Its management-defined-performance-measure definition and exclusions must be tested before the disclosure requirements apply. For an in-scope MPM, .123 requires a reconciliation to the most directly comparable specified or IFRS-required subtotal/total and income-tax/NCI effects for each reconciling item, with its specified calculation and explanation requirements. Do not call every adjusted measure an MPM or assert that a particular US presentation has no equivalent without reading current US requirements. [IFRS 18.47–.49, .69–.73, .117–.119, .123–.125, C1](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).

### Reduced disclosures: IFRS 19

IFRS 19 may be elected for periods beginning on or after **2027-01-01**, with earlier application and disclosure permitted. At period end the entity must be a subsidiary, lack public accountability and have an ultimate/intermediate parent producing publicly available IFRS-compliant consolidated statements. It changes disclosures, not the other Standards' recognition/measurement requirements; specified disclosures remain applicable, including all disclosures of IFRS 8/17/IAS 33 if applied. Intermediate-parent separate-statement eligibility and incidental fiduciary activities have their own conditions. Do not describe every subsidiary or every private company as eligible, or assume a US private-company alternative is the same. [IFRS 19.1–.4, .7–.12, A1](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs19.html).

## National framework overlays

### German HGB

| Original topic | Current bounded comparison |
| --- | --- |
| Prudence/realisation | Apply §252's prudence, realisation, accrual and consistency principles, including its justified-exception clause; this is not proof that every IFRS outcome is less prudent. The IFRS Conceptual Framework describes faithful representation as complete, neutral and free from error, with prudence supporting neutrality, not deliberate overstatement of liabilities. [Conceptual Framework 2.13–2.16](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/cf.html). [HGB §252](https://www.gesetze-im-internet.de/hgb/__252.html). |
| Internally generated intangibles | §248(2) permits capitalisation of eligible internally generated fixed intangible assets but excludes internally generated brands, publishing titles/rights, customer lists and comparable items. The old “rare in practice” claim is unconfirmed. [HGB §248](https://www.gesetze-im-internet.de/hgb/__248.html). |
| Goodwill | §246 treats acquired goodwill as finite-lived; §253(3) amortises over expected useful life. Only exceptionally, if useful life cannot be reliably estimated, its cross-referenced rule uses **10 years**. The original **5 years** is wrong for this rule. [HGB §253(3)](https://www.gesetze-im-internet.de/hgb/__253.html). |
| Pension discounting | §253(2) uses the relevant average market-rate periods, with the statutory discount rates determined and published monthly by the Bundesbank: **10 prior financial years** for retirement provisions, **7** for other provisions; its pension simplification assumes **15-year** remaining maturity. Compare the actual IAS 19 currency/term/bond conditions, not a universal AA shortcut. [HGB §253(2)](https://www.gesetze-im-internet.de/hgb/__253.html). |
| Construction revenue | The old completed-contract/§275(2)1 claim remains unconfirmed; that presentation citation does not establish a universal recognition rule. Apply §252 and recover the actual contract-specific national interpretation before comparing IFRS 15's over-time criteria. [HGB §252](https://www.gesetze-im-internet.de/hgb/__252.html). |
| Provisions | §249 covers uncertain liabilities, onerous pending contracts, specified omitted maintenance made up within **3 months** of the next year, next-year overburden removal and non-legally-obliged warranties. It prohibits provisions for other purposes; the original blanket “omissions of own labour” is not the rule. [HGB §249](https://www.gesetze-im-internet.de/hgb/__249.html). |
| Short-maturity FX | §256a requires the closing spot middle rate. With remaining maturity **1 year or less**, the stated cost-ceiling/unrealised-profit restrictions do not apply; the old lower-of-historical-or-closing rule is not correct. [HGB §256a](https://www.gesetze-im-internet.de/hgb/__256a.html). |
| Derivatives/hedge units | §254 disapplies specified provisions only to the extent and period that qualifying opposing value/cash-flow changes offset within a valuation unit. It does not say that every designated hedge is at fair value or establish every unhedged derivative's measurement. Under IFRS 9, derivatives within its scope are generally measured at fair value, with the specific hedge-accounting/presentation rules separately applied; no universal national equivalence follows. [IFRS 9.4.1.4, .4.2.1, .5.7.1](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html). [HGB §254](https://www.gesetze-im-internet.de/hgb/__254.html). |

[HGB §§246, 248–249, 252–254, 256a](https://www.gesetze-im-internet.de/hgb/__253.html). Recover any additional DRS or sector rule before applying these statutory screens to a material transaction.

### UK and Republic of Ireland FRS 102

The main March 2024 Periodic Review amendments apply to periods beginning on or after **2026-01-01**, with early application only if the relevant package is applied together. Supplier-finance disclosure paragraphs .7.20B–.7.20C have the separate **2025-01-01** gate. The September 2024 edition plus subsequent amendments constitutes the current edition. February 2026 adapted-format amendments have separate **2027-01-01** gates and early-adoption package conditions under .1.72–.1.73; do not assume every later amendment has the 2026 date. [FRS 102.1.36–.1.40](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf); [FRC current edition/amendment register](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/).

| Original topic | Comparison for the applicable revised edition |
| --- | --- |
| Goodwill | Finite useful life and systematic amortisation; exceptionally, if a reliable estimate cannot be made, life must not exceed **10 years**. This is not a default maximum for every reliably estimated life (.19.23). [FRS 102.19.23](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf). |
| Investment property | Revised .16.7 requires fair value at each reporting date through profit or loss; consider the actual definition and specific intragroup property policy. The old blanket undue-cost-or-effort limitation and “same option as IAS 40” are not the revised .16.7 rule. IAS 40 has its own policy choice and exceptional measurement conditions. [FRS 102.16.4A–.16.7](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf). |
| Borrowing costs | .25.2 permits a policy to capitalise qualifying directly attributable costs, consistently by class; otherwise expense borrowing costs. This differs from IAS 23's applicable capitalisation requirement, but neither permits every cost to be capitalised. [FRS 102.25.2–.25.2C](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf). |
| Development | .18.8H permits development recognition only on demonstrating all **6** criteria; a capitalisation policy must be applied consistently to qualifying development expenditure (.18.8K). Research is expensed. Compare the entity's actual policy with IAS 38. [FRS 102.18.8E–.18.8K](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf). |
| Defined benefit plans | .28.23–.28.24 recognises specified service costs/net interest in profit or loss and remeasurements in OCI, subject to other-asset inclusion; do not infer every IAS 19 measurement is identical. [FRS 102.28.23–.28.24B](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf). |
| Leases/revenue | Revised Section 20 has ROU/liability recognition subject to its exemptions and revised Section 23 has its own 5-step revenue model. Lessee transition does not restate comparatives and adjusts opening equity, with specified expedients/measurement conditions (.1.44–.1.54). Revenue transition choices must be sourced separately before use. [FRS 102.20.45/.23.1–.23.5/.1.44–.1.54](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf). |

[FRS 102 Sections 16, 18–20, 23, 25, 28 and transition](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf). Retain the old pre-review operating/finance and off-balance-sheet operating-lease comparison only for an actual earlier-period framework after recovering that edition; it is not the default revised model.

### Indian Ind AS

The ICAI **2025–2026** compendium includes MCA's **2025** amendments. It is a published national-standard reproduction; individual company applicability and any later notification still require their own legal check. MCA's direct PDF URLs returned access errors in this source session; the actual compendium PDFs, not search snippets, support the limited comparisons below. The actual **2026-08-12** Gazette G.S.R. **725(E)** subsequently amends Ind AS **101, 107, 109, 110 and 7**, with the identified amendment application gates at annual periods beginning on or after **2026-04-01**; publication commencement and reporting-period application are different tests. Its Ind AS 101 changes concern B5–B6 and related application wording, rather than the D7AA/D13AA comparisons below. The instrument also expressly describes the IFRS 18-corresponding Ind AS as under formulation at its issue date. NFRA's recommendation of Ind AS 118 is not an MCA notification; its final notification/current applicability remains individually unconfirmed here. Do not apply IFRS 18 automatically to an Ind AS preparer. [G.S.R. 725(E), rules 1–2(A)–(E)](https://egazette.gov.in/WriteReadData/2026/275402.pdf).

| Original topic | Corrected limited comparison |
| --- | --- |
| Long-term monetary FX | Ind AS **101.D13AA** permits a first-time adopter to continue its previous-GAAP policy for qualifying long-term monetary items recognised immediately before its first Ind AS reporting period. The old generic “Ind AS para 46A” is not the current operative locator or an unrestricted policy for new items. [Ind AS 101.D13AA](https://resource.cdn.icai.org/94028indas2025-26-101.pdf). |
| Bargain purchase | Ind AS 103.34/.36/.36A requires the reassessment and underlying-reason evidence analysis: qualifying gain is in OCI accumulated as capital reserve; without clear underlying-reason evidence, the reassessed excess is directly in equity as capital reserve. It is not always routed through OCI. IFRS 3's separate reassessed gain rule uses profit or loss. [Ind AS 103.34–.36A](https://resource.cdn.icai.org/94030indas2025-26-103.pdf). |
| PPE deemed cost | Ind AS 101.D7AA's previous-GAAP carrying-value option has the no-functional-currency-change, all-relevant-asset, prior-GAAP/consolidation and specified adjustment conditions; it also extends as stated to eligible intangible assets and investment property. Do not replace those conditions with “IFRS is stricter”. IFRS 1 D5–D8 has its own elections. [Ind AS 101.D7AA](https://resource.cdn.icai.org/94028indas2025-26-101.pdf). |
| Service concessions | Ind AS **115 Appendix D** is integral operator guidance, with grantor regulation/control and residual-interest conditions and the whole-life qualification; it does not specify grantor accounting. Ind AS 115.C10 supersedes Ind AS 11/18. The original deferred Ind AS 11 Appendix C assertion must not be used to conclude service-concession guidance was not adopted. The original IFRIC 12 comparison lead remains a required counterpart source for a complete operator reconciliation, rather than a universal equivalence conclusion. [Ind AS 115 Appendix D/C10](https://resource.cdn.icai.org/94042indas2025-26-115.pdf). |

[Ind AS 101](https://resource.cdn.icai.org/94028indas2025-26-101.pdf); [Ind AS 103](https://resource.cdn.icai.org/94030indas2025-26-103.pdf); [Ind AS 115](https://resource.cdn.icai.org/94042indas2025-26-115.pdf); [ICAI edition register](https://www.icai.org/post/compendium-of-indian-accounting-standards).

### Chinese ASBE

MOF's retrieved ASBE 36 articles 3–6 distinguish related parties and explicitly state that enterprises merely under common state control, without other related-party relationships, are not related parties. Do not repeat the original blanket claim that all such state-owned entities require broader related-party disclosure than IFRS. The text read is an identified MOF standard publication; it is not proof that the entire ASBE corpus or every 2024/2026 amendment has been reviewed. [ASBE 36 articles 2–12](https://kjs.mof.gov.cn/zt/kjzzss/kuaijizhunzeshishi/200806/t20080618_46245.htm).

The identified MOF texts support these bounded national comparisons; do not extend an asset-specific rule to assets excluded from that standard or treat this as a complete ASBE amendment review.

| Topic | Operative national rule and comparison limit |
| --- | --- |
| Impairment | ASBE 8 article 17 prohibits reversal of impairment recognised under that standard; articles 3–4 distinguish its excluded asset categories and annual goodwill/indefinite-life testing. This is not a prohibition on reversing every inventory or financial-asset write-down. IAS 36 separately prohibits goodwill reversal but requires qualifying other-asset reversals subject to its measurement cap. [ASBE 8 articles 3–4, 15–17, 23–25](https://kjs.mof.gov.cn/zt/kjzzss/kuaijizhunzeshishi/200806/t20080618_46240.htm). |
| Government grants | Revised ASBE 16 articles 6–11 require the recognition conditions and distinguish asset/income grants. Asset-related grants reduce the asset or are deferred and released systematically over its useful life; nominal-measurement grants enter current income. Income grants follow the compensated-cost/loss timing; mixed grants are split or, if inseparable, classified as income-related. IAS 20.7/.12 separately impose reasonable-assurance and systematic cost-matching requirements, and .24–.27 permit asset-grant presentation as deferred income or deduction from the asset. Do not turn either national or IFRS presentation choice into an unconstrained recognition election. [IAS 20.7–.12, .24–.27](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias20.html). [ASBE 16 articles 6–11](https://kjs.mof.gov.cn/zt/kjzzss/kuaijizhunzeshishi/200806/t20080618_46232.htm). |
| Common control | ASBE 20 articles 5–7 define non-temporary common ultimate control, measure acquired assets/liabilities at the acquiree's combination-date carrying values, align accounting policies and put the net-assets/consideration difference against capital reserve then retained earnings if insufficient. IFRS 3 excludes such combinations; that exclusion does not itself mandate pooling under IFRS. [ASBE 20 articles 4–7](https://kjs.mof.gov.cn/zt/kjzzss/kuaijizhunzeshishi/200806/t20080618_46228.htm); [IFRS 3.2(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html). |
| Borrowing costs | ASBE 17 article 4 capitalises directly attributable costs only for an asset requiring a substantial preparation period, including specified fixed assets, investment property and inventory; other costs are expensed. Article 5 imposes the **3** commencement conditions. Articles 11–14 govern interruption/completion, including abnormal continuous interruption of **more than 3 months** with a necessary-process exception. Do not capitalise all fixed-asset borrowing costs or presume every IAS 23 amount is identical. [ASBE 17 articles 4–5, 11–14](https://kjs.mof.gov.cn/zt/kjzzss/kuaijizhunzeshishi/200806/t20080618_46231.htm). |

ASBE 16's revised text commenced **2017-06-12** and replaced its identified 2006 version; its transition is in articles 18–20. The other linked MOF publications identify the actual text read, not an assurance that every later interpretation or entity-specific implementation has been cleared. Obtain any applicable later overlay before finalising a national entry.

### Japanese J-GAAP

ASBJ Statement 21.32 requires systematic goodwill amortisation over its expected benefit period, no more than **20 years**, using straight-line **or another reasonable method**; immaterial goodwill may be expensed in the year it arises. The old “always straight-line” shorthand is incomplete. The actual standard and its impairment guidance must be applied together; a project considering goodwill changes does not itself amend this rule. [ASBJ Statement 21.28–.33](https://www.asb-j.jp/jp/wp-content/uploads/sites/4/kichu_20251016_17.pdf).

Statement **34.58** applies the new lease standard to fiscal years beginning on or after **2027-04-01**, with early application from fiscal years beginning on or after **2025-04-01**. Its lessee model recognises ROU/liability, subject to the actual implementation conditions; the old off-balance-sheet comparison cannot be applied without identifying adoption status. Statement **29.16–.18** contains its own revenue principle and **5** steps, scope exclusions and permitted alternatives. The original **2018** standard is distinguished from its **2020** revision, which .81 applies from consolidated and separate fiscal years beginning on or after **2021-04-01**, with the specific early/transition routes in .82–.89-4; .83-3 ties the 2024 lease-related revision to that lease standard's application. Convergence is not proof of identical outcomes. [ASBJ Statement 29.3–.4, .16–.18, .81–.89-4](https://www.asb-j.jp/jp/accounting_standards_system/details.html?topics_id=13).

The Business Accounting Council R&D standard, section III, expenses all costs within its R&D definition, including the R&D portion of software, subject to section VI: the standard excludes work performed for another enterprise, mining-specific resource-development activities, and business-combination acquired assets other than the specified commissioned, market-sale and internal-use software. Section IV separately requires capitalisation of qualifying non-R&D product-master costs, excluding maintenance, and qualifying internal-use software when future revenue or cost savings are sufficiently certain. A generic “technological feasibility” label does not replace these purpose-specific conditions; IFRS IAS 38 separately capitalises development when its **6** criteria are met. [Official ASBJ publication, R&D standard sections I–VI and notes 1–3](https://www.asb-j.jp/jp/accounting_standards_system/details.html?topics_id=82).

Statement **26.15, .24–.25** puts the specified unrecognised actuarial/past-service amounts through OCI with later reclassification when expensed; .39 excludes those OCI provisions in the specified separate-financial-statement treatment. This is not IAS 19's no-recycling model. The revision's general gate in .34 is fiscal-year ends for years beginning on or after **2013-04-01**, while .35 has the distinct **2014-04-01** commencement for the stated obligation/service-cost and presentation provisions, with its expressly conditioned later/earlier routes. The original “post-2014” blanket and historical corridor assertion must not replace those distinctions. Pension comparisons concern **IAS 19**, not IFRS 19. [ASBJ Statement 26.15, .24–.25, .34–.39](https://www.asb-j.jp/jp/accounting_standards_system/details.html?topics_id=113). [ASBJ Statement 34.25–.34, .58–.59](https://www.asb-j.jp/jp/wp-content/uploads/sites/4/lease_20240913_02.pdf).

### Brazilian CPC

Identify the exact CPC and regulator-adopted basis, entity type and period; do not assume a listed-company framework or CPC-PME election from the country alone. CVM Resolution **237**, articles 1–3, makes CPC **51** mandatory for the specified public companies from fiscal years beginning on or after **2027-01-01**. That is an adopted national instrument, not proof that all current CPC is identical to IFRS or that every smaller entity uses IFRS for SMEs. The original **2010** full-IFRS/listed-company claim, PME eligibility, ICPC/OCPC timing, RTT/MEP repeal interaction and Law **11638/2007** opening-balance indexation remain individually reserved below. [CVM Resolution 237, articles 1–3](https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/resolucoes/anexos/200/resol237.pdf).

### Canadian ASPE

Do not use the original amortise-goodwill-over-up-to-**40-years** assertion. AcSB's identified exposure draft proposes a new amortisation choice; a proposal is not a current accounting election. The actual current Handbook Part II recognition/measurement paragraphs were not recovered here: the official publisher platform opened to its login page, which supplies no operative standard text. Goodwill, intangible useful lives, leases, taxes-payable versus future-income-tax methods, subsidiary/associate investment choices and defined-benefit valuation options are individually retained as source requests below. Do not infer that ASPE necessarily has less deferred tax. [AcSB identified proposal and status](https://www.frascanada.ca/en/aspe/documents/ed-relief-from-recognition-acquired-intangible-assets-amortization-goodwill).

## Worked cases

### IFRS to HGB: exceptional goodwill useful-life fallback

Assume acquired goodwill **EUR 100,000** was recognised at the year's start under both applicable frameworks. There is no impairment, disposal, currency movement or tax effect in this illustration. In the exceptional HGB case, the expected useful life cannot be reliably estimated, so the applicable §253(3) fallback is **10 years**; assume straight-line amortisation is the supported systematic method for this fact pattern. HGB annual amortisation is **EUR 10,000**, closing goodwill **EUR 90,000**. IFRS goodwill remains **EUR 100,000** on these no-impairment facts. The IFRS-to-HGB entry is Dr amortisation expense / Cr accumulated goodwill amortisation **EUR 10,000**; HGB profit and equity are each **EUR 10,000 lower**. This does not set a 10-year life for reliably estimable HGB goodwill or clear recognition of the acquisition itself. [HGB §253(3)](https://www.gesetze-im-internet.de/hgb/__253.html); [IFRS 3.B63(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html).

```oa-check
name: IFRS to HGB goodwill amortisation bridge under exceptional useful-life fallback
inputs:
  goodwill: 100000
  fallback_years: 10
steps:
  hgb_amortisation: goodwill / fallback_years
  hgb_closing_goodwill: goodwill - hgb_amortisation
  ifrs_closing_goodwill: goodwill
  profit_delta_hgb_minus_ifrs: 0 - hgb_amortisation
  equity_delta_hgb_minus_ifrs: 0 - hgb_amortisation
expected:
  hgb_amortisation: 10000
  hgb_closing_goodwill: 90000
  ifrs_closing_goodwill: 100000
  profit_delta_hgb_minus_ifrs: -10000
  equity_delta_hgb_minus_ifrs: -10000
```

### IFRS to FRS 102: documented development-expensing policy

Assume research costs **EUR 40,000**, followed by development costs **EUR 60,000** incurred only after all **6** IAS 38 recognition criteria have been demonstrated. The development asset is not yet available for use, there is no impairment and this illustration assumes no tax effect. Under IAS 38, research expense is **EUR 40,000** and the development asset **EUR 60,000**. For a revised FRS 102 preparer with a valid consistently applied development-expensing policy, total expense is **EUR 100,000** and no development asset is recognised. The IFRS-to-FRS 102 entry is Dr development expense / Cr intangible asset **EUR 60,000**; profit and equity fall by **EUR 60,000**. A FRS 102 capitalisation policy meeting all its conditions would change the comparison. This example supplies the criteria evidence; arithmetic does not prove technical feasibility or policy eligibility. [IAS 38.54–.57, .97](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias38.html); [FRS 102.18.8E–.18.8K](https://media.frc.org.uk/documents/FRS_102_September_2024_Redacted_edition_UkckFQ0.pdf).

```oa-check
name: IFRS to FRS 102 development-expensing policy bridge
inputs:
  research_cost: 40000
  qualifying_development_cost: 60000
steps:
  total_cost: research_cost + qualifying_development_cost
  ifrs_expense: research_cost
  ifrs_asset: qualifying_development_cost
  frs102_expense: total_cost
  frs102_asset: 0
  profit_delta_frs102_minus_ifrs: ifrs_expense - frs102_expense
  equity_delta_frs102_minus_ifrs: frs102_asset - ifrs_asset
expected:
  total_cost: 100000
  ifrs_expense: 40000
  ifrs_asset: 60000
  frs102_expense: 100000
  frs102_asset: 0
  profit_delta_frs102_minus_ifrs: -60000
  equity_delta_frs102_minus_ifrs: -60000
```

## Outputs and completion checklist

Produce the exact framework/period/adoption statement; materiality-ranked transaction catalogue with both operative citations; net-income and equity bridges; balance-sheet bridge; cash-flow bridge if in scope; disclosure differences; transition/restatement schedules; future-effective standards log; journals with balanced debits/credits; and a reviewer brief listing each missing source, judgement and owner. Use [T2]/[T3] as unresolved-review labels, not approval labels.

Check goodwill for HGB, FRS 102, Japan and the specifically unresolved ASPE comparison; leases across IFRS/ASC/FRS/HGB including period gates; ECL versus the actual ASC model; inventory/LIFO/write-down reversals; uncertain taxes and deferred-tax effects; cash-flow presentation; and IFRS 18/19, FRS 102 and ASBJ adoption status. Reconcile every figure to the trial balance and every journal to both bridges. Do not quantify a source-limited item merely to complete a checklist.

## When to refuse or refer

Stop the affected adjustment if either operative framework, period, eligibility, measurement input or source is unresolved. Do not equate EU-endorsed and IASB-issued IFRS without checking endorsement. Do not apply Ind AS/ASBE/CPC rules from training memory or assume all national convergence differences are minor. For US impairment reversals, development/software capitalisation, private-company goodwill, tax methods and consolidation, obtain the specifically identified current ASC text before accepting or reversing an entry. Do not state that ASPE/FRS necessarily has less deferred tax; do not turn their policy choices into automatic elections. Refer material valuation, financial-instrument, tax-uncertainty, sector, covenant or transition disputes with the actual contracts and workpapers.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute accounting, audit, or financial advice. GAAP differences carry direct consequences for reported earnings, debt covenants, and tax provisions. Every output must be reviewed and signed off by a credentialed CPA / CA with dual-GAAP experience before any reconciliation is finalised.

## Sources

Actual operative read scopes and native extracts are retained in the separate rule ledger. The IFRS 2026-issued books, German statutes, FRC edition/amendment texts and identified national publications were personally read in the specific scopes cited on **2026-11-16**; earlier source captures retain their original retrieval provenance. A successful download is not a whole-standard read. Current ASC and subscription Handbook content were not recovered as complete operative bodies; prior actual access records are preserved and do not constitute source approval.

### Not yet confirmed: individual original US comparison assertions

Each item below is outside usable current-ASC instructions. Ordinary official ASC recovery produced no readable operative text; the read ASU amendments support only their stated paragraphs and transition terms. Do not use a historical ASU as proof of the complete 2026 Codification.

| Original topic | Specific retained source request |
| --- | --- |
| Revenue | ASC 606/340-40 variable consideration, licence use/access, recoverable commissions/amortisation expedient and principal/agent; the original blanket “same”/no-adjustment except transition proposal, including the original full-retrospective versus modified-retrospective transition alternatives, is not established. |
| Leases | ASC 842 operating versus finance cost/ROU models, lessor equivalence with ASC 840/842, off-market sale-leaseback gain and EBITDA/front-loading comparison; apply all classification, impairment and other-asset exceptions. The old IFRS ≥12 months/>USD 5,000 formula is not current IFRS law. |
| Credit loss | ASC 326 CECL amortised-cost scope and available-for-sale allowance; original all-lifetime/no-staging, “same plus HTM”, OTTI replacement and higher-day-one-allowance proposals need the actual scope and current amendments. |
| Financial assets | ASC 320/321/825 trading/AFS/HTM debt and equity FV-through-earnings categories, non-marketable measurement alternative, impairment and observable-price-change adjustment directions; do not use the old “cost less observable changes” formula. |
| Goodwill | ASC 350 public-entity non-amortisation/annual-indicator test/reporting-unit comparison, ASU 2014-02 eligible-private-company 10-year alternative and ASU 2017-04 single-step model; no automatic reporting-unit-broader conclusion. |
| Inventory | ASC 330 LIFO permission, US tax LIFO-conformity interaction and no write-down reversal; the tax-conformity claim requires separate actual tax law as well as accounting scope. |
| PPE | ASC 360 no-revaluation/component-depreciation permission and impairment no-reversal conditions; no current US execution conclusion is authorised by the old table. |
| R&D/software | ASC 730 general expense, ASC 985-20 technological-feasibility and ASC 350-40 internal-use/web exceptions; recover current versions, scope, cost and adoption conditions before capitalising or reversing costs. The original directional proposal that IFRS technology companies often capitalise more development cost and that reconciliation therefore requires reversal remains individually unconfirmed; neither direction nor an automatic reversal follows from a generic framework label. |
| Borrowing | ASC 835-20 qualifying-asset and routine-versus-major-construction-inventory treatment; no universal identity with IAS 23. |
| Provisions | ASC 450 probable definition, range/low-end measurement and discounting exceptions; the original 70%–80% likelihood and smaller/larger-liability generalisations must not drive a numerical conclusion. |
| Employee benefits | ASC 715 OCI/amortisation/service-period, corridor and expected-return/PBO-interest rules; the original corridor-abolished claim and universal difference require current operative proof. |
| Tax | ASC 740 more-likely-than-not recognition and exact cumulative-probability measurement boundary, the original proposed post-2017 immediate non-inventory-transfer recognition versus inventory deferral until external sale, and tax-base comparison; the old ≥50% shorthand is not cleared. |
| FX | ASC 830 functional-currency indicators, hyperinflation threshold/period and reporting-currency remeasurement; do not apply a universal common 100% trigger. |
| Consolidation | ASC 810 voting/VIE and primary-beneficiary conditions, potential voting rights and ASC 946 investment-company exception/subsidiary scope; no blanket equivalence to IFRS 10. |
| Business combinations | ASC 805 always-fair-value NCI/full goodwill, contingent consideration liability/equity classification and later measurement, and acquisition-cost expense versus issue-cost exceptions; the original blanket “same” statements need actual current scope/conditions. |
| Cash flows | ASC 230 interest paid/received and dividends received operating-only, dividends paid financing and income taxes operating-only proposals, including all exceptions; do not reclassify from labels alone. |
| Presentation/disclosures | Claimed absence of a direct IFRS 18/19 equivalent versus US presentation/private-company alternatives; obtain actual applicable US requirements before a complete-equivalence or no-equivalent conclusion. |

The original named US adoption leads have actual amendment-date evidence: ASU **2023-09**, .740-10-65-9, applies for PBE annual periods beginning after **2024-12-15** and other-entity annual periods after **2025-12-15**, permits early adoption for unissued/available-for-issuance annual statements, and uses prospective application with retrospective application permitted. ASU **2023-07**, .280-10-65-1, applies to the specified public entities and has fiscal years after **2023-12-15** and interim periods within fiscal years after **2024-12-15**, early adoption and retrospective application with the impracticability/disclosure qualification. These are adoption gates, not a clearance of every underlying disclosure requirement. [Actual ASU 2023-09](https://storage.fasb.org/ASU%202023-09.pdf); [actual ASU 2023-07](https://storage.fasb.org/ASU%202023-07.pdf).

### Not yet confirmed: remaining national and historical assertions

| Original item | Precise limit and required recovery |
| --- | --- |
| Italy OIC / France PCG | The official OIC in-force index and ANC 2026 PCG publication index were opened, and the original Civil Code articles 2423–2435/ANC 2014-03 research references are retained. These index reads do not establish transaction-specific local rules; no local adjustment is supplied. [OIC index](https://www.fondazioneoic.eu/principi-contabili-category/2026/); [ANC current PCG index](https://www.anc.gouv.fr/plan-comptable-general-0). Read 2026-11-16, index scope only. |
| German intangibles/construction/PPE/derivatives | The original §§238–342e broad research range is not an operative citation. The named historical BilMoG-era HGB framework, economic-ownership and intangible-applicability research context needs its own period-specific proof; it is not current scope clearance. “Rarely capitalised”, enforceable-claim-only variable consideration, delivery-date licences, commissions expensed as incurred, generally consistent principal/agent outcomes, construction completed-contract under §275(2)1, universal off-balance-sheet operating leases, no component depreciation and all designated derivatives at FV remain individually unconfirmed beyond the actual statutory screens read above. |
| Earlier FRS 102 | The old off-balance-sheet operating-lease model and investment-property undue-cost-or-effort statement need the actual earlier edition and period; do not apply them to the revised .20/.16.7 model. Revenue full/modified-retrospective transition choices need their specific current transition paragraphs before election. The original historical ranking that leases were the largest pre-review FRS 102/IFRS difference for UK private companies remains individually unconfirmed and cannot select or quantify an adjustment. |
| Ind AS period corpus | The original blanket 2024-amendments/current-for-all-2025-periods statement is not a complete national applicability check. The identified 2025–2026 compendium supports only the specific paragraphs read, not every later notification. The old proposed previous-GAAP policy of amortising long-term monetary FX differences over the remaining asset/liability life remains individually unconfirmed; D13AA is a qualified continuation election, not proof of that underlying policy outcome. |
| ASBE impairment | The identified ASBE 8 rule is now addressed above with article-specific scope exclusions; later amendments/interpretations and the entity's applicable corpus still require confirmation before execution. |
| ASBE grants | The actual revised ASBE 16 articles 6–11 and 18–20 were recovered/read; the original universal IFRS-equivalence proposal remains unsupported beyond those precise recognition, presentation and timing rules. |
| ASBE common control | The actual ASBE 20 articles 4–7 were recovered/read. Its national carrying-value rule does not establish that every corresponding IFRS common-control transaction uses pooling. |
| ASBE borrowing | The actual ASBE 17 articles 4–5 and 11–14 were recovered/read. The original all-fixed-assets and universal “same as IFRS” proposals are superseded by the stated qualifying-asset and timing conditions. |
| ASBE dates | The 2006/2014 label and unspecified 2024 supplementary guidance do not establish the complete 2026 corpus. The identified ASBE 36 related-party text does not cure those separate missing sources. |
| Japan revenue | Statement 29's actual scope, 5-step principle, revision/commencement and transition clauses are now addressed above; a blanket zero-difference conclusion remains unconfirmed for a specific contract. |
| Japan development/R&D | The actual R&D standard sections III–IV supersede the generic feasibility-only proposal. Transaction-specific software implementation guidance and cost allocations still require their applicable clauses. |
| Japan pensions | The actual Statement 26 OCI/reclassification, separate-statement exception and distinct commencement provisions are addressed above. The original historical “corridor previously allowed” assertion remains unconfirmed and cannot drive an entry. |
| Brazil scope/history | Original listed-company full IFRS from 2010, CPC-PME eligibility/IFRS-for-SMEs identity, ICPC/OCPC lag, RTT/MEP repeal and Law 11638/2007 opening-indexation assertions each need their own operative national period source. The actual CVM 237/CPC 51 adoption above is a narrower finding. |
| ASPE goodwill | Original amortise with no stated maximum/typically ≤40 years is unsupported and must not be used. The identified AcSB proposal does not create a current amortisation election; obtain current .3064 and final amendments/adoption status. |
| ASPE intangibles | Original all-intangibles-useful-life-amortisation comparison needs current .3064 finite/indefinite-life recognition and impairment conditions. |
| ASPE leases | Original operating/finance distinction versus IFRS 16 requires current .3065 scope, classification and measurement. |
| ASPE tax | Original taxes-payable versus future-income-tax policy choice requires current .3465 eligibility/application; no conclusion of necessarily lower deferred tax. |
| ASPE investments | Original cost/equity/consolidation choices for subsidiaries/associates require current .1591/.3051 scope, presentation and control/influence conditions; do not equate those different investments or IFRS statements. |
| ASPE pensions | Original accrued-benefit-obligation valuation choice versus prescribed IFRS projected-unit-credit requires current .3462 and plan scope. |
| Historical corpus cutoff | The original “IASB through 31 December 2024/current from 1 January 2025” umbrella is superseded by paragraph-specific period/adoption gates; it is not retained as a current guarantee. |

Recover the specific missing operative text or obtain a qualified practitioner's documented resolution before turning any reserved item into an entry. Keep the exact unresolved item in the practitioner review file.
