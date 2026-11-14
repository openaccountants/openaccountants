---
name: insurance-sector
description: "A 2026 cross-country insurance method: reconcile IFRS insurance and reinsurance balances, national tax reserves, premium taxes, captive licensing, prudential and multinational tax work. Includes sourced UK IPT arithmetic and correct Singapore licensing reference; holds unconfirmed country rates and specialist US GAAP/tax details."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/insurance-sector"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Insurance sector v1.0

## Scope and quick reference

For 2026 insurers, reinsurers, insurance groups and captives: reconcile insurance-contract accounts to national tax, premium taxes, solvency and top-up-tax work. Load `corporate-income-tax-workflow-base` and the country's actual insurance/corporate-tax and VAT jobs. IFRS accounting, US GAAP, prudential returns and tax reserves are separate bases.

This file does not price products, estimate actuarial reserves independently, perform a solvency return, obtain an insurance authorisation or resolve Lloyd's specialist tax. A qualified actuary's output is an input to review, not proof that every tax reserve is deductible.

| First question | Instruction | Source |
| --- | --- | --- |
| What contract and framework? | Identify insurance risk, contract scope/group and the applicable adopted framework before choosing a measurement model | [AASB 17, scope and grouping](https://standards.aasb.gov.au/aasb-17-dec-2022) |
| Are reinsurance and issued contracts separate? | Apply the separate reinsurance-held requirements, including non-performance and loss recovery | [AASB 17, paragraphs 60-70A](https://standards.aasb.gov.au/aasb-17-dec-2022) |
| Is premium tax due? | Establish risk location, contract class, liable person and exemption before selecting a rate | [HMRC insurer guide](https://www.gov.uk/guidance/insurance-premium-tax) |
| Is a captive exempt from tax? | A captive licence is not an income-tax exemption or proof that related premiums are deductible | [MAS official application, explanatory notes](https://www.mas.gov.sg/-/media/mas-media-library/regulation/insurance/captive-insurers-licence/applicationform--captiveinsurers-march-2022.pdf) |

## Ask the client first

- Which insurer/reinsurer/captive entities, licences, tax residences, branches and group relationships exist?
- What are the actual contract classes, policy/risk locations, coverage periods, currencies and reporting/tax dates?
- Which framework, reporting edition, measurement approach, grouping and transition method apply?
- What are the actuarial cash flows, discount assumptions, risk adjustments, contractual service margins, acquisition costs and reinsurance terms?
- What evidence supports tax reserves, premium-tax exemptions/allocations, intermediary fees and payments to related parties?
- Which national solvency, foreign ownership/CFC/PFIC and top-up-tax rules/elections must be established separately?

## The method, step by step

1. Establish legal, licensed and tax status separately. Classify issued contracts, reinsurance held, investment components and any separate customer-service promises under the actual framework.
2. Establish the applicable contract grouping, coverage and recognition dates. Obtain actuarial model outputs and reconcile assumptions to the approved valuation and ledger, rather than estimating missing liabilities as zero.
3. Record fulfilment cash flows, the risk adjustment and any contractual service margin under the selected approach. Explain onerous groups, finance movements, acquisition costs, foreign exchange and service release separately.
4. Compute reinsurance-held balances using their own recognition, risk-transfer and non-performance requirements. Reconcile recoveries and loss-recovery components without netting away the underlying loss.
5. Bridge the accounts to the country's insurance tax base and tax reserve/DAC rules. Identify current/deferred tax and transition items; do not infer a tax asset from the mere existence of a CSM.
6. Classify each premium by risk location, cover, dates, liable person and national exemption. Split mixed taxable/exempt cover on supported facts. Reconcile returns, intermediary fees, remittances and policy records.
7. Separately reconcile solvency capital, prudential technical provisions and top-up-tax outcomes. Licensing, accounting profit and a nominal country rate do not decide these results.

Steps 1-4 use the IFRS-aligned for-profit principles in [AASB 17, paragraphs 3-28F, 32-59 and 60-70A](https://standards.aasb.gov.au/aasb-17-dec-2022). The [AASB index](https://standards.aasb.gov.au/accounting-standards) identifies the public-sector insurance amendment applicable from July 2026; the older compilation must not be used as proof that public-sector scope is unchanged. Another accounting framework needs its own actual standard.

## Insurance accounting decisions

| Issue | Work required | Source |
| --- | --- | --- |
| General measurement | Current, probability-weighted future cash flows within the boundary, discounting/financial risk, non-financial risk adjustment and CSM | [AASB 17, paragraphs 32-39](https://standards.aasb.gov.au/aasb-17-dec-2022) |
| Premium allocation approach | Optional only if its actual eligibility test is met. Short coverage is one route; qualifying similarity to general measurement is another | [AASB 17, paragraphs 53-59](https://standards.aasb.gov.au/aasb-17-dec-2022) |
| Direct participation features | Assess the applicable modified requirements rather than applying a label to all participating products | [AASB 17, paragraphs 29 and 45](https://standards.aasb.gov.au/aasb-17-dec-2022) |
| Contractual service margin | Unearned profit for relevant issued-contract groups; release follows insurance-contract service, not premium receipt alone | [AASB 17, paragraphs 38-46](https://standards.aasb.gov.au/aasb-17-dec-2022) |
| Onerous issued contracts | Recognise the required loss/loss component when the conditions are met; do not hide it by assuming a positive CSM | [AASB 17, paragraphs 47-52 and 57-58](https://standards.aasb.gov.au/aasb-17-dec-2022) |
| Acquisition cash flows | Allocate rationally, recognise/assess recoverability as required, and distinguish any permitted expense election | [AASB 17, paragraphs 28A-28F and 59](https://standards.aasb.gov.au/aasb-17-dec-2022) |
| Reinsurance held | Apply its own net-cost/net-gain CSM, counterparty non-performance, risk transfer and loss-recovery mechanics | [AASB 17, paragraphs 60-70A](https://standards.aasb.gov.au/aasb-17-dec-2022) |

Do not treat IFRS risk adjustment as a US GAAP margin, import a US discount rate into IFRS measurement or assume an ASC 944 LDTI loss test equals an IFRS onerous-group test. Preserve the original comparison topics for general/PAA/variable-fee measurement, discount curves, CSM, risk adjustment, premium deficiency/onerous losses, acquisition costs and reinsurance presentation, but do not use the old comparison table as a confirmed US GAAP rule set. Detailed ASC 944/LDTI commencement, scope and amendments are held in Sources.

An IFRS transition balance, tax basis, enacted tax treatment and recoverability assessment are all needed for deferred tax. A CSM does not automatically create a deferred tax asset, and a transition amount is not necessarily recognised or released through the same component in every case. Keep the gross/tax basis and recognition evidence rather than a universal equity-to-profit rule.

## United Kingdom: premium tax, not corporation tax

The following rates apply to the correctly classified UK taxable premium, not to insurance-company profit. Reinsurance and most long-term insurance are **exempt**, rather than a universal zero-rated supply. Overseas risks may face tax in their actual location.

| Premium class | Rate and condition | Source |
| --- | --- | --- |
| Standard-rated taxable general-insurance premiums | 12%; establish UK risk and no relevant exemption | [HMRC rate table](https://www.gov.uk/government/publications/rates-and-allowances-insurance-premium-tax/insurance-premium-tax-rates), [insurer guide](https://www.gov.uk/guidance/insurance-premium-tax) |
| Higher-rated contracts | 20% for travel and the specified appliance/vehicle insurance arrangements; the selling arrangement matters | [HMRC insurer guide](https://www.gov.uk/guidance/insurance-premium-tax), [rate table](https://www.gov.uk/government/publications/rates-and-allowances-insurance-premium-tax/insurance-premium-tax-rates) |

An insurer intending to receive taxable premiums, or a taxable intermediary charging a higher-rate related fee, must establish its registration obligation. Mixed taxable/exempt premiums can require registration even if some cover is exempt. Use the actual policy allocation and [HMRC registration/return instructions](https://www.gov.uk/guidance/insurance-premium-tax), retain policy documents, endorsements, premium adjustments and notices to file, and confirm the actual return/payment period. This guide does not replace full Notice IPT1 risk-location, apportionment and contract-class tests.

For income tax keep UK general insurance, life business and Lloyd's distinct. Do not cite the life-business Finance Act provisions as the universal general-insurer rule. I minus E, trading/non-trading business, reserves, transition and Lloyd's requirements are separate held country questions; a premium-tax rate does not answer them.

### Worked case: tax-exclusive premiums in different classes

Fabricated UK illustration after the full location/classification work has established a standard-rated premium of GBP 1,000 and a higher-rated travel premium of GBP 500. Both are tax-exclusive and have no mixed cover, adjustment or exemption. IPT is GBP 120 plus GBP 100, total GBP 220; combined premium plus tax is GBP 1,720. An inclusive premium would require the appropriate tax fraction instead of adding the rate again. An exempt reinsurance premium must not be included in either taxable base.

```oa-check
name: UK separate premium tax classes
inputs:
  standard_premium: 1000
  higher_premium: 500
  standard_rate: 0.12
  higher_rate: 0.20
steps:
  standard_tax: standard_premium * standard_rate
  higher_tax: higher_premium * higher_rate
  total_tax: standard_tax + higher_tax
  total_due: standard_premium + higher_premium + total_tax
expected:
  standard_tax: 120
  higher_tax: 100
  total_tax: 220
  total_due: 1720
```

## European insurance and solvency

Maintain separate premium-tax workpapers for Germany, France, Italy, Spain, the Netherlands, Belgium, Sweden and Ireland. Each must establish the insured risk, location, insurance class, taxable person, applicable premium date, national levies and exemptions. The former national percentage table, including fire/health/motor/life categories and additional parafiscal charges, was not supported by current official sources and is held below. A single standard percentage cannot describe every country's contract mix.

For Solvency II/technical provisions, prudential risk margins, transitional measures, deferred taxes and loss-absorbing capacity, obtain the current adopted regulatory text and valuation. Accounting liabilities, prudential technical provisions and tax-deductible reserves need not match. No current solvency capital percentage, transition allowance or DTA recognition conclusion is supplied by this global method.

## Singapore and captive-location workpapers

The [MAS application form, explanatory notes](https://www.mas.gov.sg/-/media/mas-media-library/regulation/insurance/captive-insurers-licence/applicationform--captiveinsurers-march-2022.pdf) identifies a captive insurer's licensing application under section 11 of the **Insurance Act 1966**. It does not support the former reference to a separate "Captive Insurance Act 2015". The form is dated March 2022 and is used here only to identify that legal basis; it does not confirm current admission requirements, fees, capital or tax incentives.

Preserve separate captive workpapers for Bermuda, Cayman Islands, Guernsey, Isle of Man, Singapore and the originally named US states Vermont, Hawaii and South Carolina. For each establish current licence class, insured related risks, risk transfer/distribution, substance, capital, premium deductibility, related-party pricing, domicile and foreign-owner taxation. The old captive population counts are not statutory eligibility tests or current market facts and are held rather than repeated as researched statistics.

For Bermuda, assess current corporate income tax scope, transition and in-scope group status from the actual law; do not retain a blanket assumption of no tax. For Cayman do not assume the original claimed domestic top-up-tax commencement. Captive incorporation alone neither makes premiums deductible to the parent nor guarantees relief from controlled-foreign-company or other anti-avoidance rules.

## United States and multinational groups

Keep the original US questions for life/non-life classification under the relevant Internal Revenue Code, life reserves, non-life reserve discounting, tax deferred acquisition costs, related-person insurance income, elections under section 953(d), PFIC active-insurance eligibility and foreign shareholder consequences. PFIC, CFC and an insurer's own tax computation are different tests. The former numerical liability/asset tests and blanket deductions remain held until the current US country source is read; do not perform them from this guide.

Likewise preserve BEAT, interest/cross-border deductions, GILTI/foreign-income regime changes, FDII and related reinsurance as current-year country questions. Neither a reinsurance payment nor a captive label proves an anti-abuse charge applies or is avoided. A tax election is a specific client decision with conditions and filing dates, not a default instruction.

For top-up tax reconcile group scope, financial-accounting insurance balances, actual covered taxes, timing, deferred tax, elections and country implementation. An insurance CSM is not automatically the same tax timing difference everywhere. Do not assert that a low-tax captive is "neutralised" without the computation and applicable exemptions. The [UK deferred-tax recapture source](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt27400) expressly distinguishes excluded liabilities, including specified insurance reserve/acquisition-cost categories, from liabilities subject to recapture. Other countries' implementations must be established separately.

## When to refuse or refer

- Missing policy classification, actuarial evidence, model scope or framework: do not manufacture a reserve/CSM or an automatic tax adjustment.
- Unconfirmed premium location/class, licence, national tax reserve rule or election: retain a named open item before filing or claiming relief.
- Captive structuring, disputed risk transfer, solvency, Lloyd's, complex reinsurance, foreign-owner insurance rules or top-up-tax elections: obtain the responsible specialist's conclusion.

## Completion checklist

- Contract groups, recognition, measurement, acquisition cash flows, CSM and onerous losses reconcile to the ledger.
- Reinsurance held, counterparty risk and loss recovery are separate from issued-contract balances.
- Tax reserves/DAC, current/deferred tax and transition have country-law support.
- Premium location, taxable/exempt classes, intermediary fees and return records are reconciled.
- Solvency, captive licensing/substance, foreign-owner anti-avoidance and top-up-tax work is separately documented.
- Every unresolved figure or legal condition below remains out of usable guidance.

## Sources

| Source | URL | Read on | Read for |
| --- | --- | --- | --- |
| AASB 17, December 2022 compilation | https://standards.aasb.gov.au/aasb-17-dec-2022 | 2026-11-14 | Read for recognition/measurement sections, general approach, PAA, onerous groups, acquisition cash flows and separate reinsurance-held requirements; not a full actuarial model or US GAAP comparison |
| AASB current standards index | https://standards.aasb.gov.au/accounting-standards | 2026-11-14 | Read for calendar-year 2026 and public-sector insurance amendment boundary |
| HMRC IPT rates | https://www.gov.uk/government/publications/rates-and-allowances-insurance-premium-tax/insurance-premium-tax-rates | 2026-11-14 | Read for current standard/higher rate rows versus historic rates |
| HMRC insurer guide | https://www.gov.uk/guidance/insurance-premium-tax | 2026-11-14 | Read for taxable classes, exemptions, insurer/intermediary registration and policy/return records |
| MAS captive application, March 2022 | https://www.mas.gov.sg/-/media/mas-media-library/regulation/insurance/captive-insurers-licence/applicationform--captiveinsurers-march-2022.pdf | 2026-11-14 | Read for explanatory notes identifying Insurance Act 1966 section 11 only; current full Act fetch returned 403 |
| HMRC MTT27400 | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt27400 | 2026-11-14 | Read for deferred-tax liability recapture and excluded insurance-reserve/acquisition-cost categories |

Not yet confirmed: detailed ASC 944/LDTI rules and effective dates; IFRS transition/deferred-tax conclusions for an actual contract/tax basis; full UK IPT Notice IPT1 risk-location/apportionment/exemption details and national income-tax/life/I minus E/Lloyd's rules; German/French/Italian/Spanish/Dutch/Belgian/Swedish/Irish premium taxes and parafiscal charges; Solvency II prudential rules and transitions; current Singapore licensing/tax details beyond the dated MAS form; all former captive counts; Bermuda corporate-tax group/transition conditions (official Act download timed out); Cayman's claimed domestic top-up-tax commencement; Guernsey/Isle of Man/US-state captive conditions; current US life/non-life/reserve/DAC/PFIC/CFC/election/BEAT/foreign-income provisions; non-UK top-up-tax implementation. No former global rate or captive-count table is carried into a usable calculation.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `insurance-sector` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/insurance-sector. If neither is available, confirm every figure against the official source pages cited above before relying on it.
