---
name: oil-gas-extractives
description: "For 2026 petroleum, mining and related businesses: map licences and production-sharing, separate royalty/resource/levy bases, reconcile accounting and restoration, and route country reporting. Corrects UK levy investment relief and Norway technical-rate mechanics; includes a recomputing UK case and explicit unresolved-country items."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/oil-gas-extractives"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Oil, gas and extractives v1.0

## Scope and quick reference

A 2026 cross-country method for petroleum producers, refiners, miners, oilfield services, midstream and LNG businesses. Identify the licence/contract and country before calculating tax. Load `corporate-income-tax-workflow-base` and the country's corporate, royalty, withholding and cross-border jobs. A contractor, producer and mineral-rights owner can have different tax bases.

This does not estimate reserves, design a production-sharing contract, provide engineering/environmental remediation instructions or perform safety regulation. Production, reserve and restoration estimates require the responsible specialists. Financial reporting, petroleum taxes, royalties, emissions charges and government-payment reporting are separate workpapers.

| Critical distinction | Instruction | Source |
| --- | --- | --- |
| UK levy versus ordinary ring-fence tax | Compute the levy on its own adjusted base; do not assume the same allowance/loss/finance rules | [Energy Profits Levy Act, section 1](https://www.legislation.gov.uk/ukpga/2022/40/section/1) |
| Investment allowance | Do not use the former broad levy allowance for current spending; the amended law identifies qualifying decarbonisation expenditure | [Finance Act 2025, section 16](https://www.legislation.gov.uk/ukpga/2025/8/section/16) |
| Norwegian special tax | Distinguish the technical special-tax rate and calculated ordinary-tax deduction from the quoted overall marginal burden | [Norwegian Tax Administration, petroleum system](https://www.skatteetaten.no/bedrift-og-organisasjon/rapportering-og-bransjer/bransjer-med-egne-regler/oljeskatt/om-oljeskattekontoret/petroleumsskattesystemet/) |
| Decommissioning | Assess the present legal/constructive obligation and recognition conditions; first production is not a universal recognition date | [AASB 137, paragraphs 14-19](https://standards.aasb.gov.au/aasb-137-jan-2026) |

## Ask the client first

- Which entity, residence, licensed field/mine, country and reporting/tax period are involved?
- Is the arrangement a concession/royalty, production-sharing contract, risk/service contract or a combination, and who owns each output stream?
- What are the production/sales volumes, prices or mandated norm prices, cost recovery, royalty bases and government entitlements?
- Which exploration, development, production, finance, restoration and disposal costs belong to which asset, field, ring fence and period?
- What are the elections, approvals, cost-recovery limits, losses, investment dates and binding contract terms?
- What evidence supports reserves, useful lives, decommissioning obligations, transfer pricing and any top-up-tax or payment-disclosure position?

## The method, step by step

1. Map the legal and fiscal arrangement, relevant tax/royalty authority, licence, ownership and revenue entitlement. Do not select a fiscal model from a country name alone: separate projects can have different contracts.
2. Reconcile output to sales, inventory, internal transfers and the government's in-kind/cash share. Apply statutory norm prices or related-party pricing where required; actual invoice proceeds are not always the tax base.
3. Build separate bases for ordinary corporate tax, special petroleum/resource taxes, royalties, levies, severance and emissions charges. Document field/entity ring fences and the precise income/cost/recovery rules.
4. Analyse investment costs by the actual tax regime, date, asset and approval, including any remaining temporary/transition provision. Current expensing in one base does not eliminate depreciation in another.
5. Reconcile exploration/development accounting, reserves-based depletion, impairment, restoration obligations and current/deferred tax. Keep the financial-reporting model distinct from tax deductions and production-sharing cost recovery.
6. Evaluate cross-border withholding/transfer pricing, government-payment reports and any top-up-tax covered-tax/substance/timing questions separately. A production royalty is not automatically an income-based covered tax.
7. Produce a field/mine and entity reconciliation, calculation, source/election evidence, filing handoff and explicit open-item schedule before professional sign-off.

## Fiscal models and country workpapers

| Model | Question to resolve in the actual licence/contract |
| --- | --- |
| Concession or royalty plus tax | Who owns production, what is the royalty basis and how does it interact with corporate/resource tax and ring fences? |
| Production sharing | What is recoverable cost, what limits/carryforwards apply, how is profit output split and is any tax paid by the state on behalf of the contractor? |
| Risk/service arrangement | Is the contractor entitled to output or a service fee, who bears risk/cost, and which withholding/PE/indirect-tax rules apply? |

Retain the original production-sharing country questions for Indonesia, Nigeria, Angola, Egypt, Algeria, Brazil pre-salt and Kazakhstan and the historic Mexico service/reform question. No current contract is classified merely from those examples. Jurisdictions excluded by the repository's coverage policy are not added as new country guidance.

## United Kingdom: separate each charge

UK upstream ring fencing prevents certain outside losses and finance costs reducing the relevant petroleum base; it does not mean that every profit and loss movement stays in an identical base for every charge. [HMRC OT00020](https://www.gov.uk/hmrc-internal-manuals/oil-taxation-manual/ot00020) distinguishes field-based PRT, ring-fence corporation tax and supplementary charge. The later levy is a further charge under its own Act.

| Charge or allowance | Confirmed rule for the applicable period | Source |
| --- | --- | --- |
| Ring-fence corporation tax | Main rate 30%; establish the actual ring-fence base and any small-profit/marginal-relief rules separately | [HMRC OT00020](https://www.gov.uk/hmrc-internal-manuals/oil-taxation-manual/ot00020) |
| Supplementary charge | 10% for the current regime; finance costs are excluded from its relevant base | [HMRC OT00020](https://www.gov.uk/hmrc-internal-manuals/oil-taxation-manual/ot00020) |
| Energy Profits Levy | 38% of levy profits; change applies from November 2024 with straddling-period provisions | [EPL Act section 1](https://www.legislation.gov.uk/ukpga/2022/40/section/1), [Finance Act 2025 section 15](https://www.legislation.gov.uk/ukpga/2025/8/section/15) |
| Statutory levy end boundary | Qualifying accounting-period boundary is 31 March 2030 under the amended provision; establish any separate early-termination mechanism and straddling rules | [EPL Act section 1](https://www.legislation.gov.uk/ukpga/2022/40/section/1), [Finance Act 2025 section 17](https://www.legislation.gov.uk/ukpga/2025/8/section/17) |
| Current additional levy investment expenditure | 66% additional expenditure for qualifying capital decarbonisation spending meeting the amended conditions; not a broad allowance for all investment | [Finance Act 2025 section 16, replacing EPL Act section 2](https://www.legislation.gov.uk/ukpga/2025/8/section/16) |
| Petroleum Revenue Tax | 0% from January 2016 for taxable pre-cut-off fields; not abolished solely by the zero rate | [HMRC PRT guide](https://www.gov.uk/guidance/oil-gas-and-mining-petroleum-revenue-tax) |

Finance Act 2025 section 16 restricts the additional levy expenditure to capital decarbonisation of upstream production, oil-related activity, non-disqualifying purposes and the stated exclusions, with just-and-reasonable allocation where mixed. It applies to expenditure from November 2024. The old broad investment-allowance claim is not a current relief. Check anti-recycling and timing provisions before claiming an amount.

The amended levy base leaves financing/decommissioning items and specified ordinary loss/group relief provisions out of account, with its own levy-loss rules and particular decommissioning-fund provisions. Do not apply an ordinary-tax loss carryback or restoration deduction automatically to the levy. [EPL Act section 1](https://www.legislation.gov.uk/ukpga/2022/40/section/1).

PRT applies to taxable fields approved before the statutory cut-off; the zero rate is not a benefit for a newly approved field. HMRC explains continuing access to historic tax for loss/decommissioning carryback and a separate field opt-out election requiring participator agreement. Obtain the actual field history, election, computation and filing obligations. The [PRT guide](https://www.gov.uk/guidance/oil-gas-and-mining-petroleum-revenue-tax) must not be read as automatic exemption from records/returns.

### Worked case: headline sum with expressly equal bases

Fabricated illustration only: assume a UK company has separately established GBP 1,000,000 taxable profits in each of the three current main-rate bases, with no allowance, small-profit relief, levy investment expenditure, loss relief, financing/decommissioning adjustment or period split. The amounts are GBP 300,000 RFCT, GBP 100,000 SC and GBP 380,000 levy, total GBP 780,000. Actual effective tax can differ because those assumptions often do not hold. Never use the sum of headline rates as a substitute for computing each base.

```oa-check
name: UK upstream separate equal-base illustration
inputs:
  rfct_base: 1000000
  sc_base: 1000000
  levy_base: 1000000
  rfct_rate: 0.30
  sc_rate: 0.10
  levy_rate: 0.38
steps:
  rfct: rfct_base * rfct_rate
  supplementary: sc_base * sc_rate
  levy: levy_base * levy_rate
  total: rfct + supplementary + levy
expected:
  rfct: 300000
  supplementary: 100000
  levy: 380000
  total: 780000
```

## Norway: do not use the effective special rate as the statutory multiplier

The [Norwegian Tax Administration's petroleum-system page](https://www.skatteetaten.no/bedrift-og-organisasjon/rapportering-og-bransjer/bransjer-med-egne-regler/oljeskatt/om-oljeskattekontoret/petroleumsskattesystemet/) explains the cash-flow special tax, ordinary-tax calculation and petroleum-law asset categories. The technical special-tax rate is applied after the calculated-company-tax deduction; the quoted combined marginal rate is not obtained by simply adding it to ordinary tax on the same unadjusted profit.

| Item | Value and condition | Source |
| --- | --- | --- |
| Ordinary-income rate used in the petroleum calculation | 22%; compute the correct ordinary offshore base and calculated-tax deduction | [Tax Administration, cash-flow section](https://www.skatteetaten.no/bedrift-og-organisasjon/rapportering-og-bransjer/bransjer-med-egne-regler/oljeskatt/om-oljeskattekontoret/petroleumsskattesystemet/) |
| Technical special-tax rate | 71.8% on the distinct special-tax base, including the calculated-company-tax deduction | [Tax Administration, cash-flow section](https://www.skatteetaten.no/bedrift-og-organisasjon/rapportering-og-bransjer/bransjer-med-egne-regler/oljeskatt/om-oljeskattekontoret/petroleumsskattesystemet/) |
| Quoted combined marginal burden | 78%, as described by the authority; not a substitute for statutory base/timing/rounding computations | [Tax Administration](https://www.skatteetaten.no/bedrift-og-organisasjon/rapportering-og-bransjer/bransjer-med-egne-regler/oljeskatt/om-oljeskattekontoret/petroleumsskattesystemet/) |

Immediate investment deduction concerns qualifying petroleum-law assets in the special-tax base, not every asset in every base. Maintain the ordinary depreciation base, special basis, historic/temporary project approvals and separate uplift conditions. Establish norm prices where applicable, financial-item allocation, transfers requiring the relevant tax consent and loss/refund treatment. Do not apply a newly announced budget proposal instead of the enacted current-period rule. This is a method boundary, not a complete Norwegian return.

## EU solidarity and windfall taxes

Keep Council Regulation 2022/1854, its covered sectors, surplus-profit measure and temporary periods as a dated legislative question. A past EU contribution does not prove a current national extension, rate or base. Obtain the national law and tax period for any 2026 charge before calculating it; the former global surcharge/base percentages and claim that most countries extended it are held in Sources. UK EPL is a separate domestic regime, not an EU implementation.

## United States and mining-country handoffs

Preserve US federal/company/state tax, severance, offshore/onshore/private royalties, intangible drilling costs, cost versus percentage depletion and successful-efforts/full-cost accounting as separate questions for existing country/state jobs. The former state percentage list, federal lease-rate history and automatic expenditure election are not current figures supplied here. Obtain the actual lease, owner, producer status, election and law.

For mining in Australia, Canada, Chile, Peru, South Africa and Indonesia, retain royalty, corporate/resource tax, provincial/state, refined/unrefined, mineral, margin and transition distinctions. Australia's repealed MRRT is a historical topic, not an existing universal royalty; a single Canadian combined corporate rate is not country-wide. The former national rate ranges, Chilean corporate-tax statement, South African change date and blanket capital-expensing claims are held until the actual relevant sources are read.

## Accounting, reserves and restoration

- **Exploration and evaluation:** identify the applicable IFRS 6 or local/US accounting policy, project stage, rights and impairment indicators. Do not infer that every full-cost/successful-efforts method is permitted identically across frameworks or that development costs remain in an exploration policy indefinitely. The detailed IFRS/ASC 932 rules remain held.
- **Depletion:** reconcile the approved reserve categories and production data to the selected depletion method. The original PRMS proved/probable/possible distinctions remain a specialist input question, not a reserve estimate made by this guide.
- **Restoration/decommissioning:** under the cited IAS 37-aligned recognition principle, establish a present legal/constructive obligation from a past event, probable outflow and reliable estimate. Do not defer recognition automatically until first production or recognise every planned future operating cost. [AASB 137, paragraphs 8 and 14-19](https://standards.aasb.gov.au/aasb-137-jan-2026).
- **Measurement and entry:** obtain the supported cash-flow/timing and discount assessment. Whether the debit is an asset or expense is determined by the applicable other accounting standard, not IAS 37 alone. Keep unwinding, estimate changes, recoveries, asset depreciation and impairment separate.
- **Tax bridge:** deductible timing, security funds, carryback, loss limitation and deferred tax are country-specific. An accounting provision is not automatically an immediate tax deduction, and a statement that deduction is always only on payment is not a global rule.

## Government-payment reporting and top-up tax

Preserve EITI and country-by-country resource-payment disclosure questions, including EU Accounting/Transparency requirements and listed/entity/materiality scope. These are not the same report as transfer-pricing country-by-country reporting. Obtain the applicable report, authority, payment categories, consolidation basis and deadline. The former count of participating countries is not a verified compliance condition.

For top-up tax, identify group scope, covered taxes, royalties versus income-based resource taxes, severance, current/deferred tax and substance-based exclusions under the actual implementing law. The [UK deferred-tax recapture guidance](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt27400) identifies excluded-liability categories including specified natural-resource licences and decommissioning/remediation costs; do not treat every timing item as recaptured. There is no automatic extractives exclusion established here. Any shipping exclusion or other country's treatment needs its own activity and law analysis.

## When to refuse or refer

- Missing licence/PSC, royalty base, production allocation, required norm price or local law: do not compute a final fiscal charge from a generic country example.
- Unsupported reserves, cost-to-complete, restoration cash flows or accounting policy: obtain the responsible specialist's evidence before completing entries.
- Unconfirmed allowance, temporary regime, loss relief, top-up-tax covered tax or election: retain a named open item and the actual project/period.
- Resource transfers, project ring fences, production-sharing, decommissioning security and disputed government entitlements require specialist tax/legal review.

## Completion checklist

- Contract model, ownership, output, price, cost and government shares reconcile by field/mine/entity.
- Each corporate/resource/royalty/levy base and ring fence is computed separately.
- Investment date, asset class, election, approval, transition, loss and finance rules have current support.
- Accounting policy, reserves, depletion, restoration and tax timing are distinct workpapers.
- Resource-payment reports and top-up-tax treatment are not confused with each other or ordinary corporation tax.
- Held country figures and unsupported historic extensions are excluded from the final calculation.

## Sources

| Source | URL | Read on | Read for |
| --- | --- | --- | --- |
| EPL Act 2022, section 1, current revised text | https://www.legislation.gov.uk/ukpga/2022/40/section/1 | 2026-11-14 | Read for charge, current rate/end boundary, separate levy base, exclusions and levy-loss handoff; direct HTML cached where web parser rejected XHTML |
| Finance Act 2025 section 15 | https://www.legislation.gov.uk/ukpga/2025/8/section/15 | 2026-11-14 | Read for enacted rate change, commencement and straddling-period rules |
| Finance Act 2025 section 16 | https://www.legislation.gov.uk/ukpga/2025/8/section/16 | 2026-11-14 | Read for amended decarbonisation expenditure, additional amount, exclusions, apportionment and expenditure-date commencement |
| Finance Act 2025 section 17 | https://www.legislation.gov.uk/ukpga/2025/8/section/17 | 2026-11-14 | Read for enacted levy end extension and corresponding transition changes |
| HMRC OT00020 | https://www.gov.uk/hmrc-internal-manuals/oil-taxation-manual/ot00020 | 2026-11-14 | Read for RFCT/SC current rates, ring-fence boundaries and historical PRT context; its three-element overview is not used to deny the later levy |
| HMRC PRT guide | https://www.gov.uk/guidance/oil-gas-and-mining-petroleum-revenue-tax | 2026-11-14 | Read for taxable-field cut-off, zero rate, continued tax history and field opt-out requirements |
| Norwegian Tax Administration, petroleum tax | https://www.skatteetaten.no/bedrift-og-organisasjon/rapportering-og-bransjer/bransjer-med-egne-regler/oljeskatt/om-oljeskattekontoret/petroleumsskattesystemet/ | 2026-11-14 | Read for cash-flow special-tax calculation, technical/ordinary rates, calculated-tax deduction, asset categories, norm-price, transition, finance, transfer and loss sections |
| AASB 137, January 2026 compilation | https://standards.aasb.gov.au/aasb-137-jan-2026 | 2026-11-14 | Read for paragraphs 8 and 14-19: recognition conditions and separation of provision recognition from asset/expense classification |
| HMRC MTT27400 | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt27400 | 2026-11-14 | Read for excluded deferred-tax liability categories relevant to natural resources and decommissioning |

Not yet confirmed: full UK small-profit/capital allowance/loss/carryback/finance and levy early-termination/fund/payment rules beyond the linked provisions; full Norwegian current law/election/temporary-project and return computation beyond the authority overview; current PSC/service terms for named countries; EU solidarity contribution and national extensions/rates/periods; US state severance, lease royalties, drilling/depletion and accounting provisions; Australia/Canada/Chile/Peru/South Africa/Indonesia royalty/corporate/resource-tax and expensing details; full IFRS 6/ASC 932/ASC 410 and PRMS methodology; supported decommissioning measurement and asset-debit treatment for an actual project; EITI country count and country payment-reporting scope/deadlines; top-up-tax covered-tax/substance and non-UK implementation. No unsupported old rate matrix is used.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `oil-gas-extractives` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/oil-gas-extractives. If neither is available, confirm every figure against the official source pages cited above before relying on it.
