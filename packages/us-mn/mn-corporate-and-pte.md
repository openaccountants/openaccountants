---
name: mn-corporate-and-pte
description: "Minnesota M4/M3/M8, 2026 minimum fee, corporate AMT/NOL, unitary and foreign income corrections, PTE election/credits and separate estimate calendars."
jurisdiction: US-MN
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
category: state-tax
version: "0.2"
---

# Minnesota corporate franchise and pass-through entity tax, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

## Who this applies to

Minnesota C corporations filing M4, S corporations filing M8, partnerships/partnership-taxed LLCs filing M3, and qualifying pass-through entities considering Schedule PTE. Existing slug `mn-corporate-and-pte` remains the single owner. Federal computations belong to `us-form-1120-c-corp` and the applicable federal entity skills. CurrencyUSD. Published 2026 law/indexing applies; verified final 2025 M4 and Schedule PTE mechanics are labelled **2025-2026 filing cycle**. Final 2026 annual forms are pending, not replaced by the software-vendor draft forms.

Corporations transacting business or owning property in Minnesota must test M4 filing regardless of incorporation state. PublicLaw 86-272 protection can apply to this income-measured franchise tax and can remove the minimum fee when there is no filing requirement; the old assertion that “franchise” defeats protection was wrong. Exempt-organization unrelated income, insurance, cooperatives, financial institutions, RIC/REIT/REMIC and special industries need their prescribed form/exemption rules. [Final 2025 M4 instructions](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

## Rates, bands and thresholds

| Item | 2026 rate / boundary | Official source |
| --- | --- | --- |
| C-corporation franchise tax | 9.8% of Minnesota taxable net income | [290.06 subd. 1](https://www.revisor.mn.gov/statutes/cite/290.06); [M4](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf) |
| Corporate AMT | 5.8%; compute AMTI/AMTT separately and credit regular tax as prescribed | [290.0921](https://www.revisor.mn.gov/statutes/cite/290.0921) |
| Corporate AMT exemption | 40,000 reduced 25% of AMTI over 150,000; zero at 310,000; statutory exceptions apply | [290.0921 subd. 2](https://www.revisor.mn.gov/statutes/cite/290.0921) |
| Regular corporate NOL limit/carry | 70% of taxable net income;15 succeeding taxable years; no carryback | [290.095 subds. 2-3](https://www.revisor.mn.gov/statutes/cite/290.095) |
| PTE ordinary income rate | 9.85% for qualifying owners' state base; no owner standard deduction/exemption at entity level | [289A.08 subd. 7a](https://www.revisor.mn.gov/statutes/cite/289A.08); [PTE page](https://www.revenue.state.mn.us/pass-through-entity-pte-tax) |
| C-corporation estimate trigger | Estimated tax more than 500 | [289A.26](https://www.revisor.mn.gov/statutes/cite/289A.26); [M4](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf) |
| Ordinary corporate required annual estimate | Lesser 100% current or 100% eligible full prior-year tax; large-corporation restriction | [289A.26 subd. 7](https://www.revisor.mn.gov/statutes/cite/289A.26) |
| PTE estimate additional-charge annual test | Generally lesser 90% current original liability or 100% prior total liability, with equal timely installments; special 2026 first-quarter relief | [PTE page](https://www.revenue.state.mn.us/pass-through-entity-pte-tax) |
| R&D credit | 10% first 2 million excess Minnesota QRE over base;4% excess above 2 million | [290.068 subd. 1](https://www.revisor.mn.gov/statutes/cite/290.068) |
| R&D refundable portion | Elect 25% of otherwise unused current-year credit for 2026-2027 under statutory conditions; remainder carries 15 years | [290.068 subds. 3-3 b](https://www.revisor.mn.gov/statutes/cite/290.068) |

**2026 minimum fee**, using Minnesota property+payroll+sales/receipts after fee-specific adjustments, not the income-apportionment denominator:

| Minnesota PP&S total | FeeUSD | Official source |
| --- | --- | --- |
| Less than 1,280,000 | 0 | [2026 indexing,290.0922](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| 1,280,000 to less than 2,560,000 | 260 | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| 2,560,000 to less than 12,830,000 | 770 | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| 12,830,000 to less than 25,640,000 | 2,560 | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| 25,640,000 to less than 51,280,000 | 5,140 | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |
| 51,280,000 or more | 12,830 | [2026 indexing](https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf) |

## The base

**M4 bridge.** Begin M4I with federal taxable income before federal NOL/special deductions, ordinarily Form 1120 line 28, adjusted to the Minnesota group. Reconcile federal consolidated versus state unitary members on Schedule REC. M4NC is the federal nonconformity schedule, **not** the NOL schedule. State NOL uses Schedule NOL, dividends Schedule DIV, alternative tax AMTI/AMTT and credits their actual schedules. M4I computes income; M4A apportionment and minimum fee; M4T tax; M4 summarizes payments/refund. [M4, pp.4,8-16](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

Add back net-income taxes/minimum fees deducted federally and other required additions. For section 168(k) bonus depreciation, the verified annual method adds 80%, then recovers one-fifth of that added amount in each of the following five years, subject to loss restrictions. That is not an 80% recovery every year. Capital losses have their own state 15-year/no-carryback treatment. Interest limitation may need a state-group recalculation if the Minnesota and federal groups differ; a matching group does not create an automatic adjustment. Track state tax refunds, foreign-tax gross-up, eligible credit-disallowed expenses, delayed interest and other actual subtraction lines. Do not invent a C-corporation QBI adjustment to an already before-special-deductions base. The old section 179 USD25,000 cap is not carried forward as 2026 law. [M4I, pp.8-11](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

The July 2026 revision of the 2025 booklet recognizes federal law through May 1,2026 but preserves state modifications. Current 2026 business FAQs require a C-corporation 80% addition for current domestic R&E expense, recovered one-fourth of that addition in each subsequent four years; converting to S status does not preserve those C-corporation subtractions. Individuals, partnerships and S corporations conform to domestic R&E expensing. Qualified production-property bonus depreciation has no 80% addition; other bonus does. Use current M4NC and actual catch-up guidance. Never assume a federal law change automatically reaches every state entity form. [Updated M4, p.1](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf); [2026 business tax-law FAQs](https://www.revenue.state.mn.us/2026_tax_law_change_faq).

**NOL.** Compute and track Minnesota losses separately by corporation, vintage, loss-year apportionment and acquisition limitation. Deduct no more than 70% of current taxable net income; carry unused qualifying loss into the 15 succeeding taxable years. No federal indefinite/20-year or 80% rule is substituted. A separate Schedule NOL is required for each member claiming a loss; it is not a free group-wide pooled loss. Special individual casualty/disaster provisions are distinct. [290.095](https://www.revisor.mn.gov/statutes/cite/290.095); [M4Tline 6](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

**Combined reporting.** More-than 50% common voting ownership and actual unitary flow-of-value facts matter. Domestic unitary companies and disqualified captive insurers are included under 290.17; foreign entities treated as C corporations are generally excluded from the combined return and file separately if they independently have Minnesota nexus. Included foreign non-C entities and captive exceptions require analysis. Eliminate intercompany transactions among included members and document Schedule AFF. The old list of 40 alleged tax havens,80/20 inclusion test and claimed worldwide-election rule are withdrawn: **290.01 subd. 5b defines “insurance company,” not a tax-haven list**. No country of incorporation automatically forces the old list's inclusion. No claim about courts upholding that fictitious list remains. [290.01 subds. 5-5c](https://www.revisor.mn.gov/statutes/cite/290.01); [290.17 subd. 4](https://www.revisor.mn.gov/statutes/cite/290.17); [M4 pp.4-5](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

**Apportionment and minimum fee.** The general method is single Minnesota-sales/everywhere-sales. Tangible sales follow receipt by the purchaser, services follow receipt with ordering-office/billing-office fallbacks, and intangibles follow purchaser use; indeterminable intangible use can require exclusion from both factor parts. Ordinary out-of-state deliveries are not automatically thrown back merely for lack of destination-state nexus. Exclude prescribed investment/capital/intercompany receipts. A group uses combined denominator and member Minnesota numerators, including otherwise missing in-state group sales as prescribed by M4Aline 7. Special financial/transport/mining formulas and FormALT approval are separate. [M4A, pp.12-14](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

For the fee, average owned inventory/property at cost, capitalize actual rent at 8 times, and use total Minnesota payroll rather than the UI wage-base cap. Apply fee adjustments, including partnership amounts, air-carrier receipts and short-year owned property. Do not merely aggregate every member into one fee or assert that a short year can never change the base: M4A uses member columns and actual adjustments. RICs/REITs/REMICs are exempt; partnership farming/JOBZ and S-corporation JOBZ exemptions require their separate criteria. A disregarded sole-owner LLC reporting only on M1 does not pay a standalone minimum fee. [M4A](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf); [minimum fee page](https://www.revenue.state.mn.us/minimum-fee).

**AMT.** Compute the state preference/adjustment and exemption base on AMTI/AMTT, including state-specific depreciation, adjusted-current-earnings and alternative-NOL/DRD limits and statutory exempt entities. The state 5.8% AMT is separate from federal CAMT. It is not simply 5.8% of ordinary income in every case. Regular tax is credited against the alternative computation; add only the incremental alternative liability, then the minimum fee and other actual form adjustments. AMT carryover credit needs its own calculation. The old “private-activity-bond preference always applies” claim conflicts with the statute's exclusions. [290.0921](https://www.revisor.mn.gov/statutes/cite/290.0921); [M4T](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

**Foreign income.** The old “80% subtraction on post-section 250 GILTI” formula is withdrawn. Current Revenue guidance classifies 2023-2025 GILTI, and 2026-onward NCTI, as dividend income. It requires section 250 special-deduction additions and certain related-CFC look-through adjustments; for 2026 onward it allows the specified 10%-of-QBAI subtraction. Relevant dividend income can receive the state DRD and is excluded from the ordinary sales factor. General state DRD is 50% for 20%-or-more ownership and 40% below 20%, subject to statutory conditions, not 80%/70%. Section 965 deferred foreign income has the prescribed subtraction. Determine the actual foreign base and DIV calculation before computing tax; no old USD10 million/50%-federal/80%-state example survives as current law. [Foreign income, updatedSeptember 21,2026](https://www.revenue.state.mn.us/foreign-income); [290.21 subd. 4](https://www.revisor.mn.gov/statutes/cite/290.21).

**R&D.** Only Minnesota qualified research and the Minnesota receipts/base rules qualify. Compute excess QRE over the supported base before applying 10%/4%; do not assume a federal election or a generic alternative-simplified method establishes state entitlement. Apply unitary allocation, then the timely irrevocable partial-refund election.2025 refundability is 19.2%;2026-2027 is 25%. Nonrefunded eligible excess carries 15 years, with no general carryback. Current-year credit and old carryovers are distinct; prior-year carryover does not create a current refundable amount. Pass-through allocation goes on the appropriate owner schedules. [290.068](https://www.revisor.mn.gov/statutes/cite/290.068); [M4 pp.6,15](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

**PTE election and owner reconciliation.** Qualifying partnerships/S corporations and LLCs taxed as either may elect; a disregarded LLC/C corporation/publicly traded partnership does not become eligible by choosing a label. Qualifying owners include the prescribed individuals/estates, S-corporation shareholder trusts and qualifying disregarded ownership; nonqualifying owners are excluded. Owners controlling more than 50% of qualifying-owner interests must elect; it binds all qualifying owners. File Schedule PTE by the entity's due/extended due date. It cannot be revoked after the original due date under Revenue's administration. The 2026 law extends availability to years beginning beforeJanuary 1,2028; the old 2025 form's sunset statement is superseded. [289A.08 subd. 7a](https://www.revisor.mn.gov/statutes/cite/289A.08); [current PTE page](https://www.revenue.state.mn.us/pass-through-entity-pte-tax).

For partnerships include resident qualifying partners' total distributive income and nonresidents' Minnesota-source shares, using PTE-RP for residents. S-corporations use Minnesota-source income for qualifying shareholders, including residents. Compute 9.85% after state modifications and no personal deduction/exemption. Issue KPI/KS/KPC as applicable. Owner refundable credit on M1REF/M2 requires the entity to have **paid** the tax; payment years and owner tax years can differ. Do not promise a federal saving from the state election: federal deductibility, QBI effects, owners' limits and timing belong in federal skills. Add back the state-tax deduction as required on the state owner/entity bridge so the same income is not both deducted and credited. [Current PTE page](https://www.revenue.state.mn.us/pass-through-entity-pte-tax); [2025-2026 Schedule PTE mechanics](https://www.revenue.state.mn.us/sites/default/files/2026-01/pte-25.pdf).

Residents still file M1/M2 when required. A qualifying nonresident with only the permitted PTE/composite income can elect satisfaction of the ordinary state filing requirement, subject to installment-sale and other exceptions. Net investment income tax remains an **owner** return obligation:1% on Minnesota net investment income exceeding 1 million, reported on M1/M2 and NIIT, cannot be paid through the PTE election according to current Revenue guidance. Do not treat an ordinary PTE election as eliminating all owner filings or default to PTE rather than comparing composite/no election. Owner-credit amendments and entity refunds must be coordinated to prevent duplicate refunds. [Current PTE page, credit/amendment/NIIT sections](https://www.revenue.state.mn.us/pass-through-entity-pte-tax).

## Deadlines and filing

The ordinary M4 due date follows the applicable federal income-return due date, including special cooperative rules; the verified calendar 2025 M4 annual cycle is April 15,2026. Minnesota grants an automatic seven-month filing extension with no application, independent of paying 90%; payment is still due originally. A longer federal extension can control under the booklet. Use the designated filer for combined-group payments. M3/M8 calendar returns ordinarily use the third-month 15 th due date and their entity extension rules. Final 2026 instructions remain pending. [M4 pp.1-4](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf); [PTE page](https://www.revenue.state.mn.us/pass-through-entity-pte-tax).

Corporate estimates are due the 15 th of months**3,6,9,12**, not 4,6,9,12. Required annual payment is generally lesser 100% current or eligible 12-month prior-year tax. A large corporation with at least 1 million Minnesota taxable net income in one of the prior 3 years generally uses current-year tax, with first-installment prior-year relief recaptured in the second. Annualization/seasonal methods require 289A.26; first Minnesota tax year and short years have their stated exceptions. [289A.26](https://www.revisor.mn.gov/statutes/cite/289A.26); [M4 pp.2-3](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf).

PTE estimates use the individual/PTE calendar pattern April 15, June 15, September 15, January 15 following year, subject to closed days. Current Revenue guidance requires four equal timely payments and gives 2026-only relief treating the first installment timely if paid by the second due date. The original-tax annual additional-charge test generally uses 90% current or 100% prior total state liability; do not transfer individual payments to the entity account. Electing is not automatic merely because an estimate was paid. [PTE page](https://www.revenue.state.mn.us/pass-through-entity-pte-tax); [289A.25](https://www.revisor.mn.gov/statutes/cite/289A.25).

Use e-Services/approved electronic return software and the actual tax account/year; retain all accepted returns and payment confirmations. Electronic payment rules include 10,000-or-more estimates in the prescribed June 30 lookback and other-business-tax electronic requirements, continuing thereafter. Amend M4 using M4X; report relevant federal changes within 180 days. M3X/M8X and owner amendments require coordinated schedules. [M4 pp.2-4](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf); [PTE page](https://www.revenue.state.mn.us/pass-through-entity-pte-tax).

## Penalties and interest

Verified 2025-2026 M4 instructions impose 6% late-payment penalty unless the 90%-paid/original-date and balance-by-extended-date conditions apply,5% late-filing after extension, a further 5% balance-not-paid-on-filing charge and 5% wrong-payment-method charge under their conditions.2026 interest is 7% using actual days on relevant tax/penalty; final 2027 rate remains unconfirmed. M15C corporate and EST PTE underpayment charges are separate from final balance penalties. A filing extension does not waive estimate charges. [M4 p.7](https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf); [PTE page](https://www.revenue.state.mn.us/pass-through-entity-pte-tax).

## Cross-border points

Test nexus/protected solicitation, unitary membership, receipts sourcing, foreign entity classification, shareholder residency and state credit separately. A foreign IP affiliate is not included solely because it is in Cayman, Malta, Ireland or any other alleged list. A Wisconsin-resident partner can have Minnesota-source PTE income without wage reciprocity; wage reciprocity does not exempt business distributive income. Specialist financial, mining, insurance and transport computations, disputed constitutional positions and material acquisitions need the actual relevant instructions and advice.

## Two worked examples that recompute

**A: Acme Manufacturing, Inc.** Retain the existing invented 5 million income,100% factor and 43 million Minnesota PP&S. Assume no NOL/credits and no AMT preferences: regular tax 490,000 exceeds the illustrative 290,000 alternative computation;2026 fee is 5,140 because 43 million is below 51.28 million. Total 495,140, not the old 500,460. Four equal current-year corporate estimate installments are 123,785 if no exception. A real AMTI/AMTT calculation is still required.

```oa-check
name: Minnesota Acme corrected 2026 fee
inputs:
  income: 5000000
  pps: 43000000
steps:
  - regular: income * 0.098
  - illustrative_alternative: income * 0.058
  - fee: 5140
  - total: max(regular, illustrative_alternative) + fee
  - quarter: total / 4
expected:
  regular: 490000
  illustrative_alternative: 290000
  total: 495140
  quarter: 123785
```

**B: TechParent/TechOps/TechIP decision.** Preserve the existing 50 million illustrative modified income,30 million Minnesota receipts/200 million eligible everywhere receipts and 80 million PP&S solely as **already-supported combined-group inputs**. Their arithmetic produces 735,000 regular tax plus 12,830 fee=747,830. The old legal premise forcing TechIP Cayman into the group is rejected. If a supported alternate eligible group instead has 40 million modified income, the same assumed 15% factor and the same fee, arithmetic is 600,830. Neither scenario determines actual foreign membership or promises a 100,000-300,000 saving; actual inputs must be rebuilt first.

```oa-check
name: Minnesota group-input decision after rejecting tax-haven premise
inputs:
  supported_income_a: 50000000
  supported_income_b: 40000000
  mn_sales: 30000000
  all_sales: 200000000
  fee: 12830
steps:
  - factor: mn_sales / all_sales
  - tax_a: supported_income_a * factor * 0.098 + fee
  - tax_b: supported_income_b * factor * 0.098 + fee
  - difference: tax_a - tax_b
expected:
  factor: 0.15
  tax_a: 747830
  tax_b: 600830
  difference: 147000
```

**C: Northstar ConsultingLLP, Anna and Ben.** Retain 1 million supported pre-state-tax base, all Minnesota source,60% resident Anna/40% nonresident Ben. Subject to qualifying-owner election and no additional modifications, ordinary PTE tax 98,500 allocates 59,100/39,400. If federal rules allow an entity deduction of 98,500, remaining distributive income 901,500 allocates 540,900/360,600; state additions restore 600,000/400,000 before owner deductions. An assumed independently computed Anna liability 58,000 gives a 1,100 refund when 59,100 credit was paid. No federal 37%/SALT-limit saving is assumed. Four equal full-liability PTE installments are 24,625, with the 2026 first-quarter timing relief above.

```oa-check
name: Minnesota Northstar paid PTE reconciliation
inputs:
  base: 1000000
  anna_share: 0.6
  assumed_anna_tax: 58000
steps:
  - pte: base * 0.0985
  - anna_credit: pte * anna_share
  - ben_credit: pte - anna_credit
  - federal_after_assumed_deduction: base - pte
  - anna_k1: federal_after_assumed_deduction * anna_share
  - anna_restored: anna_k1 + anna_credit
  - anna_refund: anna_credit - assumed_anna_tax
  - quarter: pte / 4
expected:
  pte: 98500
  anna_credit: 59100
  ben_credit: 39400
  anna_k1: 540900
  anna_restored: 600000
  anna_refund: 1100
  quarter: 24625
```

## Ask the client first

1. Tax/entity classification, tax year, Minnesota nexus, protected activities and all related/foreign entities?
2. Federal returns, group reconciliation, actual state modifications, NOL vintages/acquisitions, interest/depreciation/research records?
3. Minnesota/everywhere receipts, market/use locations, member property/payroll/rents and special-industry facts?
4. Owners' classifications/residency and percentages, election authority/date, income sourcing, other Minnesota income and actual PTE payments/credits?
5. Current/prior tax, large-corporation test, dated installments/extensions, certified credits, AMT schedules and notices?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Updated 2025 M4 instructions. Read for entire 16-page 2025-2026 filing cycle, conformity revision, forms, unitary groups, base, apportionment, fee, credits, dates, estimates and penalties. | https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf | 2026-11-13 |
| 2026 inflation amounts. Read for every minimum-fee boundary and fee. | https://www.revenue.state.mn.us/sites/default/files/2025-12/inflation-adjusted-amounts-2026.pdf | 2026-11-13 |
| 290.01. Read for domestic/foreign and insurance definitions, especially 5 b. | https://www.revisor.mn.gov/statutes/cite/290.01 | 2026-11-13 |
| 290.17. Read for all unitary inclusion/exclusion and intercompany rules. | https://www.revisor.mn.gov/statutes/cite/290.17 | 2026-11-13 |
| 290.095. Read for NOL limit,15-year carry, apportionment and acquisition restrictions. | https://www.revisor.mn.gov/statutes/cite/290.095 | 2026-11-13 |
| 290.0921. Read for AMT rate, exemption, preferences, exempt entities and alternative loss/DRD limits. | https://www.revisor.mn.gov/statutes/cite/290.0921 | 2026-11-13 |
| 290.21. Read for 50%/40% DRD and conditions. | https://www.revisor.mn.gov/statutes/cite/290.21 | 2026-11-13 |
| 290.068. Read for QRE/base, rates, allocation, partial refund election and carryover. | https://www.revisor.mn.gov/statutes/cite/290.068 | 2026-11-13 |
| 289A.08. Read for current PTE election, owners, bases and sunset. | https://www.revisor.mn.gov/statutes/cite/289A.08 | 2026-11-13 |
| 289A.26. Read for corporate 100% estimates, months 3/6/9/12, large-corporation and short/annualized rules. | https://www.revisor.mn.gov/statutes/cite/289A.26 | 2026-11-13 |
| 289A.25. Read for individual/PTE calendar and distinction. | https://www.revisor.mn.gov/statutes/cite/289A.25 | 2026-11-13 |
| Current PTE page. Read for 2026 extension/first-quarter relief, paid credits, owner filing and NIIT routing. | https://www.revenue.state.mn.us/pass-through-entity-pte-tax | 2026-11-13 |
| 2025 Schedule PTE. Read for 2025-2026 annual form workflow only; obsolete sunset superseded by 2026 law. | https://www.revenue.state.mn.us/sites/default/files/2026-01/pte-25.pdf | 2026-11-13 |
| Foreign income. Read for 2026 NCTI/QBAI, section 250/look-through additions, DRD and factor exclusion. | https://www.revenue.state.mn.us/foreign-income | 2026-11-13 |
| 2026 business law FAQs. Read for C-corporation domestic R&E/catch-up decoupling distinction. | https://www.revenue.state.mn.us/2026_tax_law_change_faq | 2026-11-13 |
| Minimum fee page. Read for exempt entities, partnership/S-corporation exceptions and disregarded LLC. | https://www.revenue.state.mn.us/minimum-fee | 2026-11-13 |

Not yet confirmed: final 2026 M4/M3/M8/PTE/PTE-RP/DIV/AMTI/AMTT/M4NC/RD forms and line mappings; full 2026 R&E/catch-up/production-property modifications, foreign NCTI/QBAI/DIV and special-industry computations, complex unitary/acquisition restrictions, owner NIIT/credit limitations and final 2027 interest. The withdrawn tax-haven list,80/20/worldwide-election assertions and old federal-rate/SALT examples are not current defaults.
