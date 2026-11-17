---
name: us-gaap-asc842-leases
description: "Lessee lease working-paper computations based on official ASU 2016-02 and ASU 2021-09 text, with original identification, lessor, modification, sale-and-leaseback and disclosure topics retained individually for current authoritative ASC source recovery. Load financial-reporting-workflow-base."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-gaap-asc842-leases"
  jurisdiction: "US"
  last_updated: "2026-11-16"
---

# US GAAP ASC 842 leases v0.3

**General reference only.** Working papers and reviewer brief only; not an audit or assurance opinion. Tier 2; not approved by an accountant.

## Scope

**Standard and effective-date basis:** ASC 842 Leases (ASU 2016-02 and ASU 2021-09 amendment basis); effective-date key **2021-12-16**. This is a version-index date for the first possible fiscal-year start after 15 December 2021, not universal ASC 842 adoption. For an entity that had adopted Topic 842 by 11 November 2021, ASU 2021-09 is effective for fiscal years beginning after 15 December 2021 and interim periods within fiscal years beginning after 15 December 2022; early application is permitted and specified modified-retrospective transition applies. An entity that had not adopted Topic 842 by 11 November 2021 adopts the amendment with Topic 842 using 842-10-65-1 transition. Determine the entity-specific original adoption date separately; the read original ASU 2016-02 alone is not current adoption authority. [ASU 2021-09 effective-date and transition summary](https://storage.fasb.org/ASU%202021-09.pdf).

Load `financial-reporting-workflow-base`. This issuer/transaction worksheet retains the complete original topic coverage, but separates the actually read amendment-basis computations from unrecovered current authoritative guidance. It does not cover the holder's accounting, control or valuation methodologies beyond the explicit steps.

**Source boundary for 2026 work.** This is a source-bounded research and computation worksheet. Current authoritative ASC text was attempted through the official site and an ordinary browser on 15 November 2026 but did not render. The FASB amendments below were opened and their stated operative paragraphs read. Each Update expressly distinguishes itself from the authoritative Codification; reading an ASU does not establish that every intervening amendment is incorporated. Consequently, the method explains only the stated amendment-basis checks. Do not use it to sign a current-ASC conclusion until the authoritative, entity-applicable text is recovered. A further official ASC web attempt on 16 November 2026 returned no operative text. Broader unresolved rules are individually reserved under Sources.

## Ask the client first

- Reporting period, PBE/non-PBE status, all adopted lease Updates and lessee/lessor/intermediate-lessor role.
- Complete asset/control/substitution/term/options analysis, commencement and documented finance/operating classification.
- Each payment, index/rate, guarantee, incentive, prepayment, direct cost and non-lease component with standalone prices.
- Readily determinable implicit rate, evidenced incremental borrowing rate, any non-PBE risk-free election and asset class.
- Impairments, modifications, termination/sublease/sale-and-leaseback facts and required disclosure balances.

## The method, step by step

1. **Version and contract gate.** Obtain a current authoritative ASC 842 scope/identification/classification conclusion. The original exclusions, all 5 finance criteria, 75%/90% reasonable-approach indicators, term/options and complete special-topic instructions are individually retained below; they are not asserted fully current by this worksheet.
2. **Read amendment-basis recognition and measurement.** ASU 2016-02 Section A sets out ASC 842-20-25-1/-25-2: both recognised classifications have a ROU asset and liability, subject to the elected short-term exception by asset class. Under -30-1/-30-5 the liability is PV of unpaid lease payments; ROU cost adds prepayments and eligible initial direct costs and subtracts incentives received. Do not double-count a lessee guarantee already included in payments when applying a classification test (842-10-25-2(d)). [Official original amendment](https://storage.fasb.org/ASU%202016-02_Section%20A.pdf).
3. **Apply the read discount-rate amendment.** ASC 842-20-30-3 as amended by ASU 2021-09 uses readily determinable implicit rate first. Otherwise use IBR, or for a non-PBE an elected risk-free rate with a term comparable to the lease, by underlying asset class. The election does not override an available implicit rate; disclose election and relevant asset classes under -50-10. [Official amendment](https://storage.fasb.org/ASU%202021-09.pdf).
4. **Compute the stated expense pattern.** In ASU 2016-02, ASC 842-20-25-5/-25-8 and -35-1/-35-8 give finance interest plus ROU amortisation, and an operating single lease cost normally on a straight-line basis. A different representative systematic basis and costs capitalised into another asset are explicit exceptions. Impairment changes subsequent operating cost mechanics; do not retain a flat-cost plug after impairment. The original text's claim that an operating lease preserves EBITDA relative to finance is backwards under a conventional EBITDA definition: operating lease cost usually reduces EBITDA; finance interest/amortisation are generally excluded. EBITDA/covenant definitions are contractual and must be checked. [Official original amendment](https://storage.fasb.org/ASU%202016-02_Section%20A.pdf).
5. **Components and elections.** ASC 842-10-15-33/-15-37 in that Update allocates relative standalone consideration unless the lessee elects, by asset class, to combine each lease component with its associated non-lease components. The election can increase the measured lease balance. This lessee expedient is not a general lessor allocation rule. [Official original amendment](https://storage.fasb.org/ASU%202016-02_Section%20A.pdf).
6. **Do not extrapolate to unrecovered current rules.** Remeasurement, modification, lessor variable-payment classification, common-control arrangements, sale-and-leaseback and Topic 230 interest presentation require current authoritative source recovery. Individual source requests below preserve the original conditions, special topics and completion checks. The read 2016 amendment itself gives investing exceptions for operating cash flows capitalised into another asset; a bare always-operating cash-flow statement is too broad (842-20-45-5). [Official original amendment](https://storage.fasb.org/ASU%202016-02_Section%20A.pdf).

### Verified corrections and remaining boundary

The original annuity-factor display used 4.2124 as though it exactly produced $210,618; the full factor is 4.2123637856 and the cent result $210,618.19. The old operating-lease EBITDA wording was reversed; capitalisation/impairment and cash-flow exceptions were missing. Its lessor/sale/remeasurement rules and claimed comparison with IFRS require current-ASC access and are individually reserved. The original short-term wording also needs the actual glossary definition checked; no IFRS low-value monetary threshold is adopted from it.

## Worked cases

All case values and rates are illustrative input facts. Classification/application gates are stated in each case; arithmetic does not verify those gates.

The original illustrative facts are a 5-year equipment lease with $50,000 annual payments in arrears and an implicit rate that is not readily determinable, with a supplied incremental borrowing rate of 6%. There are no incentives, prepayments, direct costs, impairment or other asset-capitalisation effects. Conditional on the supplied lease/classification conclusions, liability and initial ROU are $210,618.19; first-year interest is $12,637.09 and closing liability $173,255.28. The 5-year straight-line finance-ROU amortisation period is a supplied case assumption requiring a separately supported applicable amortisation conclusion, rather than a period derived solely from the lease term. Under that assumption, ROU expense is $42,123.64 and combined expense $54,760.73. Conditional on operating classification with the stated assumptions, single lease expense is $50,000 and the ROU reduction is $37,362.91. Both classifications have the same liability cash-flow schedule on these facts. The original whole-dollar proposed journals, rounded independently from full precision, are retained below.

```oa-check
name: Existing 5-year equipment lease, full-precision discounting
inputs:
  payment: 50000
  rate: 0.06
  years: 5
steps:
  - factor: 1 / (1 + rate) + 1 / ((1 + rate) * (1 + rate)) + 1 / ((1 + rate) * (1 + rate) * (1 + rate)) + 1 / ((1 + rate) * (1 + rate) * (1 + rate) * (1 + rate)) + 1 / ((1 + rate) * (1 + rate) * (1 + rate) * (1 + rate) * (1 + rate))
  - liability: round(payment * factor, 2)
  - interest: round(liability * rate, 2)
  - closing_liability: liability + interest - payment
  - depreciation: round(liability / years, 2)
  - total_finance_cost: interest + depreciation
expected:
  liability: 210618.19
  interest: 12637.09
  closing_liability: 173255.28
  depreciation: 42123.64
  total_finance_cost: 54760.73
```

The component-election case has a 2-year contract with $60,000 annual combined payments in arrears. Standalone annual lease price is $50,000 and maintenance is $10,000; the supplied evidenced discount rate is 6%. Without the non-separation election the allocated lease PV is $91,669.63; with a valid election the combined lease PV is $110,003.56, an increase of $18,333.93. These are illustrative prices/rates, not prescribed thresholds.

```oa-check
name: Component separation versus valid asset-class election
inputs:
  combined_payment: 60000
  lease_ssp: 50000
  service_ssp: 10000
  rate: 0.06
steps:
  - lease_payment: combined_payment * lease_ssp / (lease_ssp + service_ssp)
  - factor: 1 / (1 + rate) + 1 / ((1 + rate) * (1 + rate))
  - separated_liability: round(lease_payment * factor, 2)
  - combined_liability: round(combined_payment * factor, 2)
  - increase: combined_liability - separated_liability
expected:
  separated_liability: 91669.63
  combined_liability: 110003.56
  increase: 18333.93
```


### Preserved original whole-dollar journal proposals

Subject to the case assumptions and separately sourced current classification and amortisation conclusions: commencement Dr ROU asset / Cr lease liability $210,618. For the finance case, first-year Dr interest / Cr liability $12,637, Dr liability / Cr cash $50,000, then Dr ROU amortisation / Cr accumulated ROU amortisation $42,124. The liability closes at $173,255; net ROU is $168,494 and total finance expense is $54,761. Each journal balances; independent whole-dollar rounding can differ from cent-level displayed balances.

For the operating case, total fixed payments $250,000 / 5 years give $50,000 annual lease cost. The liability first accretes to $223,255 and payment reduces it to $173,255. A combined proposed journal is Dr lease cost $50,000 / Cr lease liability $12,637 / Cr ROU asset $37,363, followed by Dr lease liability / Cr cash $50,000. The $37,363 ROU reduction is the expense less liability accretion, not a separate extra expense. These ordinary mechanics do not apply unchanged after impairment, a modification, a representative alternative systematic pattern or capitalisation into another asset.

## When to refuse or refer

Refuse a final current-US-GAAP accounting conclusion while authoritative ASC text or required contracts/adoption facts are unavailable. Do not treat a readable ASU as full current Codification access. Refer scope, complex own-equity/lease/acquisition classifications, valuation, enforceability, impairment, SEC presentation and tax effects to the appropriate specialist. Return the source gap and proposed arithmetic working paper, not a signed financial statement or assurance conclusion. Exclude grandfathered leveraged leases under ASC 840 transition, revenue outside the lease model under ASC 606 and execution of ASC 360 impairment. Refer their scope/interaction questions separately. For dual reporters prepare a separate `ifrs16-leases` assessment.

## Disclaimer

Provides computational and interpretive guidance on ASC 842 only. Not an audit and not assurance. Lease classification and measurement turn heavily on entity-specific facts and significant judgement (lease term, discount rate, classification thresholds). Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

## Sources

| Source | Official URL | Actual read scope and date |
|---|---|---|
| ASU 2016-02 Section A | [ASU 2016-02 Section A](https://storage.fasb.org/ASU%202016-02_Section%20A.pdf) | Read for ASC 842-10-15-33 through -15-37, -25-1 through -25-7, -55-2/-55-3; 842-20-25-1 through -25-8, -30-1 through -30-6, -35-1 through -35-9, -45-5 and neighbouring exceptions; actual official PDF; 2026-11-15 |
| ASU 2021-09 | [ASU 2021-09](https://storage.fasb.org/ASU%202021-09.pdf) | Read for ASC 842-20-30-3, -50-10, transition/effective-date summary and adjacent disclosure changes; actual official PDF; 2026-11-15 |
| Current authoritative Codification | [ASC](https://asc.fasb.org/) | Attempted 2026-11-15; web root returned no readable lines; ordinary Brave visit reached /Login but rendered only a stalled loader. Not read; no current-authority claim. |


### Not yet confirmed: individual current-ASC source requests

The official Codification recovery did not yield operative text. Each following item is a specific retained current-source request, not executable current-ASC guidance; read ASU calculations and corrections above have only their stated version scope.

| Original topic retained | Exact question or condition to resolve |
|---|---|
| Initial adoption and scope | Original PBE periods after 15 December 2018 and other-entity periods after 15 December 2021, all subsequent deferrals and transition choices, and replacement of ASC 840; do not use an original adoption date without entity-specific amendments. |
| Excluded assets and arrangements | Intangibles under ASC 350, mineral/oil/gas exploration/use under ASC 930, biological assets, inventory and assets under construction; grandfathered leveraged leases, non-lease revenue and ASC 360 impairment need separate applicable guidance. |
| Identified asset and substitution | Explicit/implicit identification and supplier substantive substitution: practical ability throughout use plus economic benefit, not benefit alone. Recover current exceptions and assessment evidence. |
| Control of use | Both substantially all economic benefits and direction of how/for-what-purpose use; predetermined-use and protective-right conditions must be read before concluding lease versus service. |
| Lease term | Non-cancellable period, reasonably certain extension/purchase and termination options, lessor-controlled periods and reassessment conditions. The original economic-incentive assessment inputs, including significant leasehold improvements, below-market rates and importance of the location, remain individually unconfirmed under current ASC; retain and document those facts without treating the old high-threshold description as cleared. |
| Finance criterion 1 | Ownership transfers by end of term. |
| Finance criterion 2 | Purchase option reasonably certain to be exercised. |
| Finance criterion 3 | Major part of remaining economic life, including the near-end-of-economic-life qualification. |
| Finance criterion 4 | PV of lease payments plus applicable residual guarantee not already in payments is substantially all fair value. Do not double-count the same guarantee. |
| Finance criterion 5 | Specialised nature leaving no expected alternative lessor use at term end. |
| 75% and 90% indicators | Verify the current reasonable-approach status and conditions of the original 75% major-part and 90% substantially-all illustrations; they are not automatic bright-line classification rules. |
| Payment perimeter | Fixed/in-substance fixed payments less incentives; index/rate at commencement; reasonably certain purchase price; term-consistent termination penalties and probable residual-guarantee payments. Check current inclusions and avoid double counting. |
| Short-term election | The original no-more-than-12-month term and no reasonably certain purchase-option wording require the actual ASC glossary and election conditions; do not import IFRS's different purchase-option definition or an IFRS low-value exemption. |
| Finance ROU amortisation | Useful life versus lease term when ownership transfers or a purchase option is reasonably certain; case amortisation period above is supplied, not a universal 5-year rule. |
| Operating subsequent cost | Current impairment consequences, alternative representative systematic basis and other-asset capitalisation; the read original ASU ordinary single-cost mechanics are not a universal flat plug. |
| Variable payments | Index/rate changes versus usage/performance amounts, initial exclusion and later expense/capitalisation, and events requiring liability remeasurement. Do not apply an unconditional no-index-reset statement. |
| Reassessment and remeasurement | Option/term changes, residual-guarantee expectation changes, resolution of variable payments into fixed payments and the applicable revised/unchanged discount rate and reclassification triggers. |
| Modification | Added right at commensurate standalone price as separate contract versus remeasurement with revised rate; scope reductions and partial-termination gain/loss versus ROU adjustment, with all current conditions. |
| Lessor sales-type classification | Applicable finance-type criteria, control, collectibility and variable-payment exceptions; recover intervening amendments. The original proposed commencement outcome, derecognise the underlying asset and recognise a net investment and selling profit or loss, remains individually unconfirmed for execution until current recognition conditions and exceptions are recovered. |
| Lessor direct financing | PV of payments plus relevant third-party guarantees, substantially-all fair value, probable collectibility and no sales-type condition; deferred selling profit and later income require current text. |
| Lessor operating | Asset retention, depreciation, lease-income pattern and any representative alternative; current variable-payment and common-control guidance cannot be inferred from the original 2016 text. |
| Sale and leaseback | ASC 606 control transfer, finance/sales-type leaseback bars, repurchase rights and their exceptions require current text. Preserve the original proposed failed-sale financing outcome, seller retains the asset and records proceeds as borrowing, and the contrasting control-passing operating-leaseback proposal, full sale gain or loss adjusted for off-market terms. Both outcomes and the seller/buyer entries remain individually unconfirmed for execution until all current sale, recognition and measurement conditions are recovered; operating classification alone does not establish a sale. |
| Components | Current lessor allocation and any lessor election are separate from the actually read lessee relative-standalone-price and asset-class combination election. |
| Presentation | Finance interest/ROU amortisation versus operating single-cost presentation; separate balance-sheet presentation/disclosure and all impairment/capitalisation exceptions. |
| Cash flows | Principal financing and interest under Topic 230 for finance leases; operating classification and amounts capitalised into another asset, including investing exceptions. Do not import IFRS's policy choice or say all operating-lease payments are always operating cash flows. |
| Disclosures: narrative and judgments | Nature, options, restrictions/guarantees, significant classification/term/rate judgments and policy/election choices. |
| Disclosures: amounts | Disaggregated finance/operating/short-term/variable costs, sublease income, weighted-average remaining term and discount rate by type, cash paid and non-cash ROU additions. |
| Disclosures: maturity and lessor | Payments for each of the next 5 years and thereafter with liability reconciliation; lessor income, net investment and residual-value risk information. Verify current scope and detail. |
| IFRS comparison: recognition and cost | Compare conditional finance/single-model and operating expense profiles, not an assertion that operating leases preserve conventional EBITDA. Both frameworks have their own exemptions and capitalisation/impairment conditions. |
| IFRS comparison: low value and short term | The old approximately $5,000 IFRS low-value illustration is not a US threshold or a mandatory IFRS rule; actual IFRS Basis for Conclusions recovery remains needed. Short-term purchase-option conditions are not identical. |
| IFRS comparison: measurement and specials | Separately source each framework's index/rate remeasurement, discount-rate/risk-free election, sale-and-leaseback gains and continuing rights, lessor model and cash-flow classification. Run both Guides, not a generic identical-treatment assertion. |

### Retained execution and self-checks

The original work programme remains: establish a lease and applicable scope; determine term/options; record classification and every relevant criterion; identify payment components and rate/elections; compute PV and ROU; book initial and subsequent journals; track variable payments and reassessment; separately analyse modifications, lessor and sale-and-leaseback facts; prepare cash flows and disclosure reconciliations; submit source gaps and the reviewer brief.

The retained checks cover identified-asset/control/substitution evidence; term and options; all 5 classification criteria without treating 75%/90% as mandatory bright lines; complete payment perimeter; implicit-rate/IBR/election order; ROU reconciliation and journals; expense pattern and impairment; variables/remeasurement/modifications; lessor and sale-and-leaseback conditions; presentation/cash flows; disclosures; and a separate IFRS comparison. Resolve each applicable source row before a final accounting conclusion.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-gaap-asc842-leases` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-gaap-asc842-leases. If neither is available, confirm every figure against the official source pages cited above before relying on it.
