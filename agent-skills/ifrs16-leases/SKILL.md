---
name: ifrs16-leases
description: "IFRS 16 lease identification, recognition exemptions, measurement, modifications, lessor and sale-and-leaseback working papers, with a 2024 amendment basis and explicit source-access boundaries. Load financial-reporting-workflow-base."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ifrs16-leases"
  jurisdiction: "GLOBAL"
  last_updated: "2026-11-16"
---

# IFRS 16 leases v0.4

**Coverage is partial:** individually identified supporting-source and current US comparison gaps below remain outside usable instructions.

**General reference only.** Produces working papers and a reviewer brief, not an audit, assurance opinion or signed financial statements. Tier 2; not approved by an accountant.

## Scope

**Standard and effective-date basis:** IFRS 16 Leases; effective-date key **2024-01-01** for Lease Liability in a Sale and Leaseback. C1D applies that amendment to annual periods beginning on or after 1 January 2024, with earlier application permitted and disclosed. Its C20E retrospective scope is stated below; this date does not assert initial adoption of the whole Standard or future IFRS 18 amendments. [IFRS 16.C1D/C20E](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html).


**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the recognition, measurement, presentation, and disclosure rules for leases under IFRS. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

- **Scope**  -  IFRS 16 applies to all leases except: leases to explore for or use minerals/oil/gas, leases of biological assets within IAS 41 held by a lessee, service concession arrangements (IFRIC 12), licences of intellectual property granted by a lessor (IFRS 15), and rights held under licensing agreements for items such as films, patents, and copyrights (IAS 38).  _(IFRS 16.3)_


This skill covers:

- Identifying a lease  -  an identified asset the customer controls the use of (`IFRS 16.9`–`.11`, `B9`–`B33`).
- The **lessee single model**: one accounting treatment for every lease (other than exemptions), normally front-loaded for a level-payment cost-model lease.
- The **2 recognition exemptions**: short-term leases and low-value-asset leases (`IFRS 16.5`–`.8`).
- Initial and subsequent measurement of the lease liability and right-of-use (ROU) asset (`IFRS 16.22`–`.38`).
- The discount rate, variable lease payments, reassessment, remeasurement, and modifications.
- Sale-and-leaseback (`IFRS 16.98`–`.103`) and sublease classification (`IFRS 16.B58`).
- The **lessor model** retained from IAS 17: finance vs. operating (`IFRS 16.61`–`.97`).

This skill does NOT cover: lessor revenue subject to `IFRS 15`, impairment of ROU assets (`IAS 36`, cross-referenced). It defers the US GAAP treatment to `us-gaap-asc842-leases`.


**Version basis for 2026 work.** IFRS 16 initially applies to annual periods beginning on or after 1 January 2019; early application requires IFRS 15 at or before initial application and disclosure (C1). It replaced IAS 17, IFRIC 4, SIC-15 and SIC-27 (C21). The sale-and-leaseback amendment applies from annual periods beginning on or after 1 January 2024; IFRS 18 consequential amendments are excluded until adopted. The 2026 issued HTML also contains future-effective text; do not assume its publication year is its effective date. The operative core was personally read in the official copy retrieved on 14 November 2026. Official retrieval succeeded again on 16 November 2026 and the core was reconciled with that body; selected supporting clauses were personally read on 16 November. The source table distinguishes those reads from retrieval alone.

## Ask the client first

- Reporting-period start/end, IFRS 18 early adoption, lessee/lessor/intermediate-lessor role and complete contract.
- Identified asset, substitution rights, decision rights, non-lease services and component election.
- Commencement, enforceable term, options, incentives, guarantees, payment schedule and index/floating-rate clauses.
- Evidenced implicit rate or incremental borrowing rate, direct costs, prepayments, restoration obligation and depreciation basis.
- Short-term/low-value elections, subleasing plans, modifications, sale-and-leaseback terms and opening balances.

## The method, step by step

### Section 2  -  Reference layer (Layer A): identifying a lease and the single model

### Step 0  -  Is there a lease?  -  `IFRS 16.9`–`.11`, `B9`–`B33`

- **Lease identification test**  -  A contract is, or contains, a lease if it conveys the right to control the use of an identified asset for a period in exchange for consideration. Control requires both: 1) The right to obtain substantially all of the economic benefits from use of the identified asset (B21–B23); and 2) The right to direct the use of the asset (B24–B30). An asset is identified when explicitly or implicitly specified and the supplier has no substantive substitution right (B13–B19). If the supplier both benefits economically from substituting and has the practical ability to substitute throughout the period of use, there is no identified asset  -  it is a service contract.  _(IFRS 16.9–.11, B9–B33)_

### Step 1  -  Determine the lease term  -  `IFRS 16.18`–`.21`

- **Lease term determination**  -  Lease term = non-cancellable period + periods covered by an extension option the lessee is reasonably certain to exercise + periods covered by a termination option the lessee is reasonably certain not to exercise.  _(IFRS 16.18–.21)_

⚑ AUDIT FLASH POINT  -  reasonably-certain option assessment. Renewal/termination judgement sizes both the ROU asset and the lease liability. "Reasonably certain" is a high threshold based on economic incentive (significant leasehold improvements, below-market rate, criticality of the asset). Document the economic-incentive and enforceable-term analysis; the lessee has no operating-lease classification alternative.

### Step 2  -  The lessee SINGLE model  -  `IFRS 16.22`

- **Lessee single model**  -  At the commencement date, a lessee recognizes a right-of-use asset and a lease liability for every lease, except those to which a recognition exemption is applied (§3). There is no finance-versus-operating classification for lessees  -  IFRS 16 abolished it. The cost-model lessee normally recognises depreciation and interest separately; the expense profile depends on the cash-flow and asset-measurement facts.  _(IFRS 16.22)_

### Step 3  -  The expense is normally front-loaded for a level-payment cost-model lease  -  `IFRS 16.31`, `.36`–`.38`

- **Front-loaded expense mechanics**  -  The ROU asset is depreciated (typically straight-line) over the shorter of the lease term and the asset's useful life  -  over the useful life if ownership transfers or a purchase option is reasonably certain (16.32). The lease liability accretes interest at the discount rate; each payment splits into interest and principal (16.36–.38). With a positive discount rate, level payments in arrears, straight-line depreciation and no remeasurement, interest usually declines, so combined expense is front-loaded. Zero-rate, increasing-payment, fair-value/revaluation and capitalised-cost cases do not support an always-front-loaded claim. Under a conventional EBITDA definition, separately expensed depreciation and interest are excluded; their exact financial-statement line items and any covenant EBITDA definition require separate assessment.  _(IFRS 16.31, .36–.38)_

### Section 3  -  Reference layer: exemptions, measurement, and special topics

### The 2 recognition exemptions  -  `IFRS 16.5`–`.8`

- **Recognition exemptions**  -  A lessee may elect not to apply the single model to: 1) Short-term leases  -  a lease with a term of 12 months or less at commencement, with no purchase option (16.5(a), definition in Appendix A). Elected by class of underlying asset. 2) Leases of low-value assets  -  assets that, when new, are of low value (16.5(b), B3–B8). The operative Standard gives no monetary cap. Assess the value when new and the conditions in B3-B8; tablets, small office furniture and telephones are examples. The legacy monetary BC100 assertion is reserved below because that Basis text was not read. Elected on a lease-by-lease basis. The assessment is on absolute value when new, regardless of materiality to the lessee. For exempt leases, recognize the payments as an expense on a straight-line basis (or another systematic basis) over the term (16.6).  _(IFRS 16.5–.8)_

⚑ AUDIT FLASH POINT  -  low-value exemption uses an absolute, not entity-relative, test. The current ASC exemption comparison is retained below for source recovery. The operative low-value assessment is per underlying asset, not per portfolio  -  bundling many low-value assets into one lease does not itself disqualify the items, but assess each underlying asset's value when new subject to B5's usable-alone/readily-available-resource and dependency conditions stated below. Document the policy and the per-asset basis.

### Initial measurement  -  `IFRS 16.24`–`.28`

- **Lease liability initial measurement**  -  Lease liability = present value of the lease payments not yet paid, discounted at the interest rate implicit in the lease if readily determinable; otherwise the lessee's incremental borrowing rate.  _(IFRS 16.26–.27)_
- **Lease payments included**  -  Lease payments included (16.27): fixed payments, including in-substance fixed payments under B42 (less incentives receivable), variable payments that depend on an index or rate (measured initially using the index/rate at commencement), amounts expected under residual value guarantees, the exercise price of a reasonably-certain purchase option, and termination penalties if the term reflects termination.  _(IFRS 16.27)_
- **ROU asset initial measurement**  -  ROU asset (16.24) = lease liability + lease payments made at/before commencement (prepaid) + initial direct costs − lease incentives received + an estimate of dismantling/removal/restoration costs the lessee is obligated to incur (recognized as a provision under IAS 37).  _(IFRS 16.24)_

⚑ AUDIT FLASH POINT  -  restoration costs are baked into the ROU asset. IFRS 16.24(d) brings the day-one dismantling/restoration provision into the ROU asset (mirrored by an IAS 37 provision). Omitting it understates both the asset and the provision and distorts depreciation. The ASC 410/842 comparison remains reserved below.

For restoration provisions, IAS 37.14 requires a present legal/constructive obligation from a past event, a probable outflow and a reliable estimate. Future operating expenditure alone is not an obligation (.17-.26). Measure the best estimate at period end; discount when time value is material using a pre-tax rate reflecting liability risks not already included in cash flows, without double-counting (.36-.52). IFRS 16.24-.25 determines whether the cost enters the ROU asset or, for production inventory, IAS 2. This is not an automatic day-1 provision for every lease.

### Subsequent measurement  -  `IFRS 16.29`–`.46`

- **Subsequent measurement rules**  -  ROU asset carried at cost less accumulated depreciation and impairment (cost model), or revaluation/fair-value models where the related IFRS (IAS 16, IAS 40) is applied to that asset class. Lease liability remeasured for reassessments and modifications (below).  _(IFRS 16.29–.46)_

### Variable lease payments  -  `IFRS 16.27(b)`, `.42`

- **Variable lease payments treatment**  -  Payments depending on an index or rate are included in the liability at the index/rate at commencement; when the resulting contractual payment change takes effect, the liability is remeasured using revised payments (16.42(b)), with the adjustment against the ROU asset. Variable payments based on usage or performance (e.g. % of sales) are excluded and expensed as incurred (16.38(b)).  _(IFRS 16.27(b), .42)_

⚑ AUDIT FLASH POINT  -  index-linked payment changes. Under IFRS 16 the resulting change in contractual cash flows triggers remeasurement when the payment adjustment takes effect; the current ASC treatment remains reserved below. Do not assume identical CPI-linked-rent mechanics for a dual-reporter.

### Reassessment and remeasurement  -  `IFRS 16.39`–`.43`

- **Reassessment and remeasurement triggers**  -  Remeasure the liability (adjusting the ROU asset; once the ROU asset is reduced to nil, further reductions go to P&L) when: the lease term or purchase-option assessment changes (use a revised discount rate); the amount expected under a residual value guarantee changes; or future payments change due to an index/rate (use an unchanged discount rate for residual-guarantee and index-only changes; a floating-interest-rate change requires a revised discount rate under .43).  _(IFRS 16.39–.43)_

### Modifications  -  `IFRS 16.44`–`.46`

- **Modification treatment**  -  A modification that increases scope by adding a right of use at a price commensurate with its standalone price → separate lease (16.44). Otherwise, remeasure the liability using a revised discount rate at the effective date. A modification that decreases scope reduces the ROU asset and recognizes a gain or loss on the partial termination in P&L (16.46); other modifications adjust the ROU asset only.  _(IFRS 16.44–.46)_

### Interest-rate benchmark reform modification exception

For lessee modifications changing the basis of future payments because of qualifying interest-rate benchmark reform, .104–.105 require the .42 expedient only if the change is both a direct consequence of reform and economically equivalent to the immediately previous basis. Qualifying reform uses the IFRS 9 definition/references in .104, so obtain that separate assessment rather than assuming every interest change qualifies. If additional modifications occur at the same time, .106 requires applying the applicable IFRS 16 modification requirements to all simultaneous changes, including the reform change. Read the C20C–C20D transition if first applying those amendments; no blanket prospective-only rule follows. _(IFRS 16.104–.106, C20C–C20D)_

### Sale-and-leaseback  -  `IFRS 16.98`–`.103`

- **Sale-and-leaseback treatment**  -  First apply IFRS 15 to determine whether the transfer is a sale (does control pass to the buyer-lessor?). If it is a sale, the seller-lessee measures the ROU asset arising from the leaseback at the proportion of the previous carrying amount of the asset that relates to the right of use it retains, and recognizes a gain or loss only on the rights transferred to the buyer-lessor (16.100). Off-market terms are adjusted (16.101). If the transfer is not a sale, the seller-lessee continues to recognize the asset and accounts for the proceeds as a financial liability under IFRS 9 (16.103).  _(IFRS 16.98–.103)_

⚑ AUDIT FLASH POINT  -  proportional gain, not full gain. IFRS 16 recognizes a gain only on the rights transferred to the buyer-lessor, retaining the rest in the ROU asset. Recover the current ASC sale-and-leaseback text separately before quantifying a dual-reporting reconciliation.

### Sublease classification  -  `IFRS 16.B58`

- **Sublease classification rule**  -  When a lessee subleases an asset (intermediate lessor), the sublease is classified by reference to the ROU asset arising from the head lease  -  not the underlying asset. If the head lease is short-term and expensed under .6, classify the sublease as operating. Otherwise apply the finance/operating risks-and-rewards tests to the ROU asset; a single term/value indicator does not override the full test.  _(IFRS 16.B58)_

The 2024 sale-and-leaseback liability amendment is applied retrospectively, in accordance with IAS 8, to sale-and-leaseback transactions entered into after the date of initial application (C20E). Obtain the IAS 8 transition working paper before executing retrospective presentation; the amendment is not limited to new transactions from 2024. _(IFRS 16.C1D, C20E)_

### Lessor model (retained dual model)  -  `IFRS 16.61`–`.97`

- **Lessor dual model**  -  IFRS 16 kept the IAS 17 lessor model: a lessor classifies each lease as finance or operating (16.61). Finance lease  -  transfers substantially all the risks and rewards incidental to ownership (16.62, indicators in 16.63–.64: ownership transfer, bargain purchase option, term covering major part of economic life, PV of payments ≥ substantially all of fair value, specialized asset). Derecognize the asset; recognize a net investment in the lease (16.67–.68). Operating lease  -  otherwise; keep the asset and recognize lease income on a straight-line basis or another systematic basis if it better represents the pattern in which benefit from use of the underlying asset diminishes (16.81).  _(IFRS 16.61–.97)_

### Section 4  -  Executable layer (Layer B): the procedure

First identify the entity's role. Lessees apply steps 1–8; a lessor routes to the lessor model and IFRS 15 component allocation in .17 instead of booking a lessee ROU/liability. An intermediate lessor applies both relevant roles and B58. Each step cites the rule it executes.

1. **Confirm a lease exists** (Step 0 / §2): identified asset + control. If no lease is identified, account for the service under the applicable Standard and stop the lease computation. _(IFRS 16.9–.11, B9–B33)_
2. **Determine the lease term** (Step 1 / §2): include reasonably-certain renewals/terminations. _(IFRS 16.18–.21, B34–B41)_
3. **Check the exemptions** (§3, `16.5`–`.8`): short-term (≤ 12 mo, no purchase option) or low-value (conditions B3-B8). If elected, expense on a straight-line basis or another systematic basis that better represents the pattern of benefit, and stop the lessee balance-sheet computation (.6).
4. **Determine the discount rate** (§3): implicit rate, else IBR. _(IFRS 16.26)_
5. **Measure the lease liability** = PV of lease payments (`16.26`). Show the PV math in a memo line.
6. **Measure the ROU asset** = liability + prepaid + initial direct costs − incentives + restoration estimate (`16.24`).
7. **Book day-1 recognition**, then **subsequent-period** entries (base §3 format): depreciation of ROU + interest on liability  -  **normally front-loaded on the stated level-payment, positive-rate assumptions**. _(IFRS 16.22–.38)_
8. **Handle variable payments, reassessment, modifications, subleases** as triggered (§3). _(IFRS 16.39–.46, B58)_
9. **If the entity is the lessor**, classify finance vs. operating (`16.61`).
10. **Classify balances and cash flows**, produce the **disclosure checklist** (§6) and **reviewer brief** with every flash point. _(IFRS 16.47–.50, .51–.60)_

### Section 6  -  Disclosure checklist  -  `IFRS 16.51`–`.60`

**Disclosure checklist**  _(IFRS 16.51–.60)_

- [ ] Depreciation charge for ROU assets by class of underlying asset (`53(a)`)
- [ ] Interest expense on lease liabilities (`53(b)`)
- [ ] Expense relating to short-term leases and to low-value-asset leases (the exemptions) (`53(c)`, `53(d)`)
- [ ] Expense relating to variable lease payments not in the liability (`53(e)`)
- [ ] Income from subleasing ROU assets; gains/losses on sale-and-leaseback (`53(f)`, `53(i)`)
- [ ] Total cash outflow for leases (`53(g)`)
- [ ] Additions to ROU assets; carrying amount of ROU assets by class (`53(h)`, `53(j)`)
- [ ] **Maturity analysis** of lease liabilities (`58`, applying `IFRS 7` liquidity-risk requirements)
- [ ] Significant judgements and the nature of leasing activities (`51`, `59`)
- [ ] Lessor disclosures: finance-lease net investment and selling profit; operating-lease income; risk management (`89`–`97`)

### Section 7  -  Topic self-checks (in addition to base §7)

- [ ] Lease vs. service determined (identified asset + control of use); cited `16.9`–`.11`, `B9`–`B33`
- [ ] Lease term includes only reasonably-certain renewals/terminations _(IFRS 16.18–.21, B34–B41)_
- [ ] Exemptions considered: short-term (≤ 12 mo, no purchase option) **and** low-value (absolute value when new, per asset) _(IFRS 16.5–.8, B3–B8, Appendix A)_
- [ ] **Single model** applied  -  no finance/operating split attempted for the lessee _(IFRS 16.22)_
- [ ] Discount rate: implicit, else IBR  -  stated _(IFRS 16.26)_
- [ ] Lease liability = PV of payments; PV math shown in a memo line _(IFRS 16.26–.28)_
- [ ] ROU = liability + prepaid + IDC − incentives + restoration estimate (IAS 37 recognition and measurement separately assessed)
- [ ] Subsequent: depreciation of ROU + interest on liability  -  normally front-loaded on the stated level-payment, positive-rate assumptions _(IFRS 16.29–.38)_
- [ ] Index/rate payments **remeasured** on change (contrast ASC 842); usage-based excluded
- [ ] Reassessment/modification triggers checked (revised vs. unchanged discount rate applied correctly) _(IFRS 16.39–.46)_
- [ ] Sale-leaseback uses proportional-gain mechanic; sublease classified by reference to the ROU asset _(IFRS 16.98–.103, B58)_
- [ ] Lessor classification (finance / operating) where the entity is the lessor _(IFRS 16.61–.66)_
- [ ] Divergence from ASC 842 checked for dual-reporters (especially the single vs. dual model)


### Additional conditions read in the primary text

If substitution cannot readily be assessed, presume it is not substantive (B19); a repair/maintenance substitution right alone does not defeat an identified asset (B18). A non-physically-distinct capacity portion qualifies only if it is substantially all of the asset capacity (B20). Where relevant use decisions are predetermined, apply the customer-operation or customer-design alternatives (B24(b)); protective supplier rights alone do not remove control (B30). Determine enforceability before options: the lease ceases to be enforceable when both parties can terminate without permission with no more than an insignificant penalty (B34-B35). Reassess reasonably-certain options for a significant event/change within the lessee's control affecting that conclusion (.20-.21). For intangible leases outside the specified .3(e) licensing exclusion, .4 permits but does not require lessee application.

Low-value relief requires the asset to be usable alone or with readily available resources and not highly dependent on/interrelated with other assets. A head lease that is subleased or expected to be subleased fails low-value relief (B5-B7). A short-term lease containing any purchase option fails the IFRS definition; that differs from the US reasonably-certain-purchase test. For a lessee, separate components and allocate relative standalone prices unless the asset-class non-separation election is taken (.12–.16); that election excludes embedded derivatives meeting IFRS 9.4.3.3: separation requires all 3 conditions (risks not closely related, a stand-alone derivative definition met, and no whole-hybrid fair-value-through-profit-or-loss measurement). Document that assessment where relevant. For a lessor, allocate consideration under IFRS 15.73–.90 as .17 requires, with that separate source analysis. Restoration costs enter the ROU asset when the obligation arises; costs incurred producing inventories follow IAS 2 rather than being added automatically to the ROU asset (.24-.25). Costs otherwise capitalised into another asset do not necessarily appear immediately in profit or loss (.38). B42 includes in-substance fixed payments that are unavoidable despite variable form, including resolved variability, the only realistic payment set, or the discounted lowest amount where at least one of several realistic sets must be paid; assess these before excluding variable payments.

For a qualifying sale and leaseback, apply .102A after commencement: determine payments/revised payments so that subsequent accounting does not recognise gain on the retained right of use; partial/full-termination gains under .46(a) remain possible. This September 2022 amendment applies from annual periods beginning 1 January 2024 (C1D). The .49 change linked to IFRS 18 is excluded until that Standard is applied (C1E).

## Worked cases

All monetary amounts, rates and transaction dates below are illustrative supplied facts, not legal thresholds or prescribed yields. Keep the original whole-dollar journal displays separate from the cent-precision check.

### Worked example (illustrative)

Same facts as the US GAAP edition: a lessee leases equipment for 5 years, paying $50,000 annually in arrears, implicit rate not determinable, incremental borrowing rate 6%. No initial direct costs, prepayments, incentives, or restoration obligation. Assume the cost model with straight-line depreciation, no ownership transfer, no purchase option reasonably certain to be exercised, and an asset useful life of at least 5 years; these facts support depreciation over the 5-year lease term. PV of an ordinary annuity, 5 periods @ 6% = 4.2124.

> Lease liability = 50,000 × 4.2123637856 = $210,618.19, displayed as $210,618 (rounded). ROU asset = $210,618.

For this recognised IFRS 16 lessee case the single-model interest and amortisation pattern applies. The comparison with the stated US finance-lease illustration is conditional on its separate classification, amortisation and version assumptions; it is not a universal cross-framework equivalence.

#### Day 1  -  recognition  -  `IFRS 16.22`, `.24`, `.26`

```
Day 1  -  recognize ROU asset and lease liability  -  driving rule: IFRS 16.22 / .24 / .26
  Dr  Right-of-use asset                     210,618
      Cr  Lease liability                         210,618
  (memo: PV = 50,000 × unrounded annuity factor 4.2123637856 @ 6%, 5 yrs; no IDC/prepaid/incentive/restoration; debits = credits ✓)
```

#### Year 1  -  single model (front-loaded)  -  `IFRS 16.31`, `.36`–`.38`

Interest = 6% × 210,618 = 12,637. Payment 50,000 → principal reduction = 50,000 − 12,637 = 37,363. Depreciation (straight-line) = 210,618 ÷ 5 = 42,124.

```
End of Yr 1  -  accrue interest and pay  -  driving rule: IFRS 16.36-38 (effective interest)
  Dr  Interest expense (finance cost)         12,637
  Dr  Lease liability                         37,363
      Cr  Cash                                     50,000
  (memo: interest 6% × 210,618 = 12,637; principal plug 37,363; liability → 173,255; debits 50,000 = credits 50,000 ✓)

End of Yr 1  -  depreciate ROU asset  -  driving rule: IFRS 16.31 (straight-line)
  Dr  Depreciation expense                    42,124
      Cr  Right-of-use asset (accum. depn.)       42,124
  (memo: 210,618 / 5 = 42,124; ROU → 168,494; debits = credits ✓)
```

Year-1 total P&L = 12,637 + 42,124 = 54,761  -  front-loaded and declining thereafter as interest falls. Under a conventional EBITDA definition, depreciation and interest are excluded; confirm the reporting/covenant definition. The current ASC operating-lease comparison is reserved below. For the cash-flow statement, .50(a) places the $37,363 rounded principal within financing. The interest portion requires IAS 7 under .50(b). The recovered 2026-issued IAS 7.34A-.34D changes are conditional on IFRS 18 adoption (.64): .34A generally classifies interest paid as financing, with the specified main-business exceptions and single-category requirements in .34B-.34D. The pre-IFRS-18 IAS 7 policy route remains individually source-limited below; do not apply future wording automatically. Exempt-lease and excluded variable payments follow .50(c) operating classification.

⚑ AUDIT FLASH POINT  -  dual-reporting handoff. Reconcile the same contractual cash flows after recovering the current ASC classification and expense rules. The archived operating-versus-finance comparison is not a current-ASC conclusion.

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

For an index-linked lease, suppose after the first payment 4 annual payments of $50,000 remain. A contractual index reset now takes effect and raises each to $52,000. The unchanged discount rate is the documented 6%; this is an index reset, not a floating-interest-rate reset. Remeasure the remaining liability from $173,255.28 to $180,185.49 and increase the ROU asset by $6,930.21, assuming it remains recognised (IFRS 16.39, .42(b)-43). The inputs are illustrative, not a prescribed interest or inflation rate.

```oa-check
name: Index reset takes effect, unchanged discount rate
inputs:
  old_payment: 50000
  new_payment: 52000
  rate: 0.06
steps:
  - factor: 1 / (1 + rate) + 1 / ((1 + rate) * (1 + rate)) + 1 / ((1 + rate) * (1 + rate) * (1 + rate)) + 1 / ((1 + rate) * (1 + rate) * (1 + rate) * (1 + rate))
  - old_liability: round(old_payment * factor, 2)
  - new_liability: round(new_payment * factor, 2)
  - rou_adjustment: new_liability - old_liability
expected:
  old_liability: 173255.28
  new_liability: 180185.49
  rou_adjustment: 6930.21
```

## When to refuse or refer

Refuse a final recognition, classification, valuation or disclosure conclusion when required contracts, applicable reporting period, adoption facts or supporting standards are missing. Refer significant valuations, enforceability, control, impairment and complex settlement terms to a qualified reporting specialist. Return the facts, paragraph-by-paragraph reasoning, balanced journals, reconciliation and open items to the reviewer. Do not issue audit or assurance language. Any topic reserved below remains outside usable instructions until its operative primary source is recovered.


### Original professional disclaimer

Provides computational and interpretive guidance on IFRS 16 only. Not an audit and not assurance. Lease measurement turns heavily on entity-specific facts and significant judgement (lease term, discount rate, low-value and exemption elections, restoration estimates). Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

## Sources

| Source | Official URL | Actual read scope and date |
|---|---|---|
| IFRS 16 Leases | [IFRS 16 Leases](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html) | Read for .1-.46B, .47-.106 (including .102A and the benchmark-reform exception .104-.106), B3-B42, B58, Appendix A short-term definition, C1-C1E, C20C-C20E in the official 2026-issued copy retrieved 2026-11-14, personally read 2026-11-15; official body retrieved again and reconciled 2026-11-16; existing read scope retained |
| IAS 36 impairment handoff | [IAS 36](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias36.html) | Retrieved 2026-11-16 and read for .9-.10, .18-.22, .30-.57, .74-.105, .110-.125, .130/.133-.135 and Appendix C; no complete ROU valuation executed here. |
| IAS 7 issued-copy cash flows | [IAS 7](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html) | Read for .31-.34D on 2026-11-16 and .64; IFRS 18 adoption gate. Earlier required/2024 paths redirected to premium, so pre-adoption route remains reserved. |
| IAS 37 restoration provisions | [IAS 37](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias37.html) | Personally read for .14-.26 on 2026-11-16 and .36-.52, recognition, measurement, discounting and qualifications. |
| IFRS 9 embedded-derivative gate | [IFRS 9](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html) | Personally read for .4.3.1-.7 on 2026-11-16 and neighboring liability classification .4.2.1-.2; no full derivative pricing or hedge module. |
| Low-value Basis attempt | [IFRS 16 Basis](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16-bc.html) | Attempted 2026-11-16: redirected to premium landing, not BC100; not read. |
| Current US comparison | [Authoritative ASC](https://asc.fasb.org/) | Attempted again 2026-11-16; official ASC web pages returned 0 readable lines. Current operative Codification not read; historical recovery limits remain in external evidence. |

Not yet confirmed: the pre-IFRS-18 IAS 7 interest-paid route, low-value BC100 figure and individual current US comparisons below; jurisdiction-specific endorsement and entity-specific early adoption; all individually retained source-limited items below. These boundaries are not accountant approval.

#### Not yet confirmed: low-value monetary suggestion

The old approximately **USD 5,000 when new** assertion attributed to BC100 remains unconfirmed. The official 2026 Basis URL redirected to the premium landing page on 16 November 2026; that is not the paragraph. The amount is not a statutory cap or an operative exemption threshold. Apply the actually read .5-.8/B3-B8 conditions, not this old figure.

#### Not yet confirmed: individual current ASC 842 comparisons

Current ASC web recovery returned 0 readable operative lines on 16 November. Each comparison below requires the actual current ASC rule and its conditions before use:

| Original topic | Specific reserved US-dependent comparison |
| --- | --- |
| Lessee model and example | Current operating/finance classification, single operating lease expense, EBITDA effects and the old conditional USD 50,000 operating expense versus IFRS USD 54,761 illustration; no US classification is assumed from identical cash flows. |
| Low-value assets | Whether a US exemption applies; do not infer a universal no-equivalent conclusion. |
| Short-term leases | Current ASC 12-month election, asset-class basis and purchase-option test; do not assume the IFRS definition is identical. |
| Indexed rents | Current ASC remeasurement triggers and excluded variable-payment treatment versus IFRS .42-.43. |
| Restoration | ASC 410/842 asset-retirement-obligation recognition and where the cost is recorded. |
| Sale and leaseback | Current sale qualification, gain recognition and off-market adjustments versus IFRS proportional retained-right mechanics. |
| Subleases | Current ASC classification reference asset and applicable exceptions versus IFRS B58. |
| Discount rate | Current eligibility/conditions for the US risk-free-rate election and implicit-rate priority. |
| Lessor model | Current sales-type/direct-financing/operating classification and degree of alignment. |
| Cash flows | Current US operating/finance lease-payment classification. |

#### Not yet confirmed: pre-IFRS-18 interest cash flows and detailed impairment execution

IAS 7 issued-copy .31-.34D/64 was read on 16 November: its IFRS 18-dependent wording does not prove the earlier policy choice. The required-edition and 2024 official paths redirected to the premium landing page, not operative earlier text. The earlier interest-paid policy alternatives of operating or financing classification are individually unconfirmed here. Recover the actual pre-IFRS-18 interest-paid route before classifying that portion for an entity that has not adopted IFRS 18. The principal and exempt/excluded-variable classifications in IFRS 16.50 remain separately supported.

IAS 36 has now been recovered and its general impairment/CGU/goodwill clauses read for the combination Guide. This lease Guide still refers the detailed ROU-specific recoverable-amount, CGU allocation and presentation working paper; it does not execute a complete impairment valuation. IFRS 9 full derivative/hedging execution and IAS 40/IAS 16 alternative-measurement eligibility likewise require their separate analyses.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ifrs16-leases` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ifrs16-leases. If neither is available, confirm every figure against the official source pages cited above before relying on it.
