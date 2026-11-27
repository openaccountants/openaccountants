---
name: ifrs16-leases
description: "IFRS 16 lease identification, exemptions, lessee measurement, remeasurement, modifications, sale-and-leaseback, subleases and lessor working papers. Includes recomputing examples and explicit holds for unproven comparisons. Load financial-reporting-workflow-base."
version: 0.5
jurisdiction: GLOBAL
last_updated: 2026-11-27
depends_on:
  - financial-reporting-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-reporting
type: computation
standard: "IFRS 16 Leases"
effective_date: 2024-01-01
source_checked: 2026-11-27
---

# IFRS 16 leases v0.5

**General reference only.** Produces working papers and a reviewer brief, not an audit, assurance opinion or signed financial statements. Load `financial-reporting-workflow-base` for the output contract and journal format. Obtain professional review before reliance.

## Scope

Use for IFRS lessees, lessors and intermediate lessors. The operative version includes **Lease Liability in a Sale and Leaseback**, effective for annual periods beginning on or after **1 January 2024**; earlier application is permitted and disclosed. Apply that amendment retrospectively under IAS 8 to sale-and-leaseback transactions entered into after initial application of IFRS 16, not just transactions from 2024. IFRS 16 initially applied from annual periods beginning **1 January 2019**; early application required IFRS 15 at or before initial application and disclosure. C21 replaced IAS 17, IFRIC 4, SIC-15 and SIC-27. Local endorsement and entity-specific adoption require confirmation. [IFRS 16.C1, C1D, C20E, C21](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_C1).

Exclude mineral/oil/gas exploration or use leases; IAS 41 biological assets held by a lessee; IFRIC 12 service concessions; IFRS 15 intellectual-property licences granted by a lessor; and lessee IAS 38 licensing rights such as films, manuscripts, patents and copyrights. For other intangible-asset leases, lessee application is optional. [IFRS 16.3–4](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_3).

**Version gate:** the 2026 issued text contains amendments that apply only when IFRS 18 is applied. Do not apply its amended paragraph 49 or amended IAS 7 interest rules merely because the source says 2026. [IFRS 16.C1E](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_C1E); [IAS 7.64](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_64).

## Ask the client first

Obtain the reporting period, applicable endorsed framework and IFRS 18 adoption facts; entity role; complete contracts and amendments; asset/substitution/decision rights; non-lease services; enforceable period and options; commencement date; payment timing, incentives, index/rate clauses and guarantees; evidenced discount rate; prepayments/direct costs; restoration obligations; useful life and depreciation method; exemption elections; sublease plans; opening balances and sale-and-leaseback terms. Missing evidence prevents a final conclusion.

## The method, step by step

### 1. Identify and separate the lease

At contract inception test whether consideration buys control of an identified asset for a period. Throughout that period the customer must obtain substantially all economic benefits from use and direct its use. Explicit or implicit specification can identify the asset. Reassess lease identification only when contract terms change. [IFRS 16.9–11, B9, B13](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_9).

A supplier substitution right defeats identification only when the supplier both can practically substitute and benefits economically from doing so throughout the period of use. A repair/maintenance or technical-upgrade right alone does not defeat identification. If the customer cannot readily assess substantiveness, presume the right is not substantive. A capacity portion must be physically distinct or represent substantially all capacity. [IFRS 16.B14–B20](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_B14).

The customer directs how and for what purpose the asset is used. If those decisions are predetermined, the customer must either control operation throughout use without the supplier changing its instructions, or have designed the asset so as to predetermine its use. Protective rights alone do not remove control. [IFRS 16.B24, B30](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_B24).

Separate lease components from non-lease components and allocate lessee consideration using relative standalone prices; estimate unavailable standalone prices using observable information as far as possible. Separate lease components require benefit alone/with readily available resources and no high dependency/interrelation with other leased assets. Charges transferring no good/service are not separate components. A lessee may instead elect, by underlying-asset class, to combine each lease component with associated non-lease components. That election excludes embedded derivatives meeting IFRS 9.4.3.3. For a non-financial-asset host, that paragraph requires all three: risks not closely related, standalone derivative definition satisfied, and no whole-hybrid fair-value-through-profit-or-loss measurement. Detailed derivative valuation is held below. Lessors allocate under IFRS 15.73–90, not the lessee election. [IFRS 16.12–17, B32–B33](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_12); [IFRS 9.4.3.3](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html#IFRS09_4.3.3).

### 2. Determine term and exemptions

Determine the enforceable period first: enforceability ends when both parties can terminate without the other's permission with no more than an insignificant penalty; consider broader economics, not just termination payments. A lessee-only termination right is an option for the lessee to assess; a lessor-only right does not shorten the non-cancellable period. Lease term includes the non-cancellable period, reasonably-certain extension options and periods under termination options reasonably certain not to be exercised. Consider all economic incentives, including significant improvements, replacement costs and contractual pricing. If an option combined with other features guarantees substantially the same minimum/fixed cash return regardless of exercise, assume reasonably-certain extension/non-termination (B38). Reassess options on a significant event/change within the lessee's control affecting reasonable certainty; revise term when the non-cancellable period changes. [IFRS 16.18–21, B34–B41](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_18).

**AUDIT FLASH POINT** — document enforceability and option judgements before computing present value.

- **Short-term election:** term **12 months or less at commencement**, with **no purchase option**; elect by underlying-asset class. A modification or term change makes an exempt short-term lease a new lease for this assessment. [IFRS 16.5–8, Appendix A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_5).
- **Low-value election:** elect lease by lease; assess absolute value **when new**, irrespective of lessee size or materiality. The asset must be usable alone/with readily available resources and not highly dependent on/interrelated with other assets. Cars typically fail; tablets, small office furniture and telephones can qualify. A head lease subleased or expected to be subleased cannot qualify. Bundling does not replace the per-asset conditions. The operative paragraphs supply no monetary threshold; the historical monetary suggestion is held below. [IFRS 16.8, B3–B8](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_B3).
- If elected, expense payments straight-line over the term, or on another systematic basis when more representative of the benefit pattern; stop the lessee ROU/liability computation. [IFRS 16.6](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_6).

### 3. Measure the lessee liability and ROU asset

At commencement recognise a right-of-use (ROU) asset and lease liability for a recognised lease; there is no lessee finance/operating classification. Liability equals present value of payments unpaid at commencement. Use the implicit rate if readily determinable, otherwise the lessee's incremental borrowing rate: similar term/security, funds for an asset of similar value to the ROU asset, and similar economic environment. [IFRS 16.22, .26, Appendix A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_26).

Include fixed and in-substance fixed payments less incentives receivable; index/rate-linked payments using the commencement index/rate; expected residual-guarantee payments; purchase price if exercise is reasonably certain; and termination penalties when the term reflects termination. Assess B42 before excluding variable payments: unavoidable payments include variability that resolves, the only realistic payment set, or the discounted lowest realistic set when at least one must be paid. [IFRS 16.27–28, B42](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_27).

ROU cost = initial liability + payments at/before commencement minus incentives received + initial direct costs + qualifying restoration/dismantling estimate. Initial direct costs are incremental costs that would not have arisen without obtaining the lease. Avoid counting the same incentive twice. Recognise restoration cost when the obligation arises, which can be later than commencement; production-inventory costs follow IAS 2. [IFRS 16.23–25, Appendix A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_24).

Restoration obligations are recognised/measured under IAS 37. A provision needs a present legal/constructive obligation from a past event, probable outflow and reliable estimate; future operating expenditure alone is insufficient. Use the period-end best estimate, discounting when time value is material at a pre-tax rate reflecting time value and liability-specific risks not already included in cash flows. Future events enter only with sufficient objective evidence. [IAS 37.14, .17–19, .36, .45–48](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias37.html#IAS37_14).

**AUDIT FLASH POINT** — a restoration clause does not automatically create a day-one provision for every lease.

### 4. Subsequent measurement and modifications

Under the cost model carry the ROU asset at cost less accumulated depreciation/impairment, adjusted for liability remeasurement. Apply IAS 16 depreciation: useful life of the underlying asset if ownership transfers or ROU cost reflects exercise of a purchase option; otherwise the earlier of ROU useful life and lease-term end. Straight-line is an example assumption, not compulsory for every lease. IAS 36 determines impairment. [IFRS 16.29–33](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_29); [IAS 16.60–62](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html#IAS16_60).

If the lessee applies IAS 40's fair-value model to investment property, apply it to ROU assets meeting the investment-property definition. If IAS 16 revaluation is used for a PPE class, the lessee may elect that model for all ROU assets relating to that class. Detailed eligibility/valuation is held below. [IFRS 16.34–35](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_34).

Increase liability for interest at a constant periodic rate, reduce it for payments, and remeasure as required. Interest and variable payments excluded from liability enter profit or loss when triggered, unless included in another asset under another Standard. Positive-rate, level-payment, straight-line cost-model leases without remeasurement normally produce declining combined depreciation/interest expense; **not every lease is front-loaded**. Do not promise an EBITDA result without the applicable reporting/covenant definition. [IFRS 16.36–38](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_36).

Remeasure for:
- term or purchase-option reassessment: revised payments and revised implicit rate if determinable, otherwise current incremental borrowing rate (.40–41);
- changed expected residual guarantee or index/rate-linked contractual payments: revised payments and unchanged discount rate, except floating-interest-rate changes use a revised rate (.42–43). Remeasure an index reset **when the contractual cash-flow adjustment takes effect**, not every index publication.

Ordinary remeasurement adjusts the ROU asset; if it reaches zero, a further liability reduction goes to profit or loss. [IFRS 16.39–43](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_39).

A modification is a separate lease only if it adds rights to one or more underlying assets and consideration is commensurate with the standalone price of the added scope, appropriately adjusted for contract circumstances. Otherwise, at its effective date reallocate consideration, redetermine term and discount revised payments using revised implicit rate/IBR. Scope decreases reduce the ROU asset for partial/full termination and recognise the related gain/loss; other modifications adjust the ROU asset. [IFRS 16.44–46](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_44).

For qualifying benchmark-reform modifications, apply the .42 expedient only where the change is a direct consequence of reform and economically equivalent to the preceding basis. Additional simultaneous modifications bring all changes into the applicable modification requirements. C20C–D require retrospective application subject to their no-hindsight/prior-period-restatement relief and opening-equity adjustment. IFRS 9 reform qualification and detailed transition execution are held below. [IFRS 16.104–106, C20C–D](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_104).

### 5. Sale and leaseback, subleases and lessors

Apply IFRS 15's performance-obligation satisfaction requirements to decide whether the transfer is a sale; obtain the separate control/repurchase assessment. If a sale, seller-lessee ROU equals the proportion of previous carrying amount relating to retained use; recognise gain/loss only for rights transferred. Buyer-lessor accounts for the purchase under applicable Standards and the lease under lessor requirements. Below-market terms are prepaid lease payments; above-market terms are additional financing. Measure that adjustment using the more readily determinable of consideration-versus-asset fair-value difference and contractual-versus-market lease-payment PV difference. [IFRS 16.98–102](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_99).

After commencement apply .29–35 to the leaseback ROU and .36–46 to its liability, determining payments/revised payments so no gain/loss on retained use is recognised; partial/full-termination gains/losses remain possible. This includes variable-payment leasebacks; do not mechanically apply the ordinary usage-payment exclusion to eliminate their liability. If transfer is not a sale, seller retains the asset and records an IFRS 9 liability equal to proceeds; buyer records an IFRS 9 financial asset and no transferred asset. Detailed IFRS 9 execution is held below. [IFRS 16.100, .102A–103](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_102A).

An intermediate lessor classifies a sublease by reference to the head-lease ROU asset, not the underlying asset, except that a short-term head lease expensed under .6 makes the sublease operating. Otherwise apply the full risks-and-rewards assessment; a single term/value indicator is not conclusive. [IFRS 16.B58, .62–65](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_B58).

A lessor classifies at inception as finance if substantially all ownership risks/rewards transfer, otherwise operating. Ownership/purchase options, major-part term, substantially-all PV, specialised nature and other .63–64 indicators are assessed together; no universal numeric bright line is supplied. Reassess classification only for modification, not changes in estimates/circumstances. A finance lessor presents a receivable at net investment, using the implicit rate; an intermediate lessor unable to determine the sublease implicit rate may use the head rate adjusted for sublease direct costs. A lessor's operating-lease asset remains presented by its nature; recognise income straight-line or another more representative systematic benefit-diminution basis. [IFRS 16.61–69, .81–88](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_61).

### 6. Presentation, disclosures and reviewer brief

Present ROU assets/liabilities separately or identify their balance-sheet lines in the notes; non-separate ROU presentation uses the line for corresponding owned assets. ROU investment property is presented as investment property. Present lease interest separately from ROU depreciation. Principal cash payments are financing; exempt short-term/low-value and excluded variable cash payments are operating. Interest follows the applicable version of IAS 7; pre-IFRS-18 classification remains held below. [IFRS 16.47–50](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_47).

For entities applying IFRS 18, IAS 7.34A generally makes interest paid financing. Entities investing in assets or financing customers as a main business use .34B–D's P&L-linked classification and single-category requirements; if P&L interest spans categories, apply the specified policy choice among associated activities. Do not use this for a non-adopter. [IAS 7.31–34D, .64](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_34A).

The lessee disclosure checklist includes depreciation by asset class, interest, exempt short-term/low-value expense, excluded variable expense, sublease income, cash outflow, additions, sale-and-leaseback gains/losses and closing ROU by class. Short-term expense may omit leases of one month or less; do not double-count short-term low-value expense in both exemption lines. Include capitalised costs within the .53 amounts and use a table unless another format is more appropriate. Add short-term commitments if .55's portfolio condition applies, exemption-election disclosure, nature, relevant unrecognised cash-flow exposure, restrictions/covenants and sale-and-leaseback information. Provide lease-liability maturities separately from other financial liabilities, applying IFRS 7.39/B11. For investment-property ROU assets apply IAS 40 disclosures instead of .53(a), (f), (h), (j); revalued ROU assets require IAS 16.77 disclosures (.56–57); detailed execution is held below. [IFRS 16.51–60](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_53).

For lessors include finance-lease selling profit/loss, finance income and excluded variable income; operating income with non-index/rate variable income separately; nature and retained-risk management; significant net-investment movements; and receivable maturities annually for the first five years plus remaining total. Reconcile finance-lease undiscounted receipts to net investment, identifying unearned finance income and discounted unguaranteed residual. Operating-asset disclosures also follow .95–96's applicable Standards. [IFRS 16.89–97](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_89).

Return source-document inputs, role/term/election conclusions, PV schedule, balanced journals, movement reconciliation, disclosures and explicit holds to the reviewer. Check components and restoration before booking; check index/floating-rate distinction, modifications, leaseback and sublease rules before subsequent entries.

## Worked cases

All case values are hypothetical supplied inputs, not prescribed yields or thresholds. No case year has been substituted.

### Original equipment case

Equipment lease: **5 years**, **USD 50,000 annually in arrears**, implicit rate not determinable, **6% IBR**, no direct costs, prepaid payments, incentives or restoration. Assume straight-line cost-model depreciation, no ownership transfer/purchase-option exercise, and ROU useful life at least the term. [IFRS 16.22–32, .36–38](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_26).

PV factor = 4.2123637856; liability/ROU = USD 210,618.19. Year-one interest = 12,637.09; principal = 37,362.91; closing liability = 173,255.28; depreciation = 42,123.64; closing ROU = 168,494.55; expense = 54,760.73. Use cents consistently:

```
Commencement: Dr ROU 210,618.19 / Cr lease liability 210,618.19
Year 1 payment: Dr interest 12,637.09 + Dr liability 37,362.91 / Cr cash 50,000.00
Year 1 depreciation: Dr depreciation 42,123.64 / Cr accumulated depreciation 42,123.64
```

The historical whole-dollar illustration used 210,618; 12,637; 37,363; 173,255; depreciation 42,124; closing ROU 168,494; expense 54,761. Its closing ROU subtracts rounded depreciation from rounded opening cost; the cent schedule rounds closing ROU to 168,495. Do not mix those rounding conventions. Principal cash is financing; interest classification follows the adoption gate/hold above.

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

### Existing index-reset case

After the first payment, **4 annual payments of USD 50,000** remain. A contractual index adjustment now takes effect, increasing each to **USD 52,000**. Retain **6%** because this is an index reset, not a floating-interest-rate reset. Remaining liability changes from **173,255.28** to **180,185.49**, increasing ROU by **6,930.21**, assuming the ROU remains recognised. [IFRS 16.39, .42–43](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html#IFRS16_42).

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

The following holds are **non-usable conclusions**, not alternative rules. Preserve supplied facts; do not compute a final outcome from an unproven premise.

- Historical approximately **USD 5,000 when new** suggestion attributed to BC100: no usable monetary threshold. The cited Basis page remains subscription-limited. Check this point with one of our partner accountants.
- Pre-IFRS-18 interest-paid cash-flow classification: earlier official IAS 7 text was not recovered; do not infer the old policy from the 2026 issued amendments. Check this point with one of our partner accountants.
- Detailed IAS 36 impairment/CGU valuation, IAS 16 revaluation/IAS 40 eligibility and valuation, and their additional disclosures; IFRS 7 maturity-analysis execution beyond the IFRS 16 routing instruction: no final valuation/disclosure-completeness conclusion here. Check this point with one of our partner accountants.
- IFRS 15 sale/control/repurchase qualification and lessor allocation; IFRS 9 derivative valuation, reform qualification and financial-asset/liability execution; IAS 8 transition working papers and local endorsement/adoption: separate operative analyses required before executing these outcomes. Check this point with one of our partner accountants.
- EBITDA/covenant metrics depend on the actual definition; no universal increase is asserted. Check this point with one of our partner accountants.

### Original US GAAP comparison topics retained as individual holds

The current authoritative ASC text has not been read for these comparisons; `us-gaap-asc842-leases` is the separate US edition, not proof of them. Each original comparison remains unavailable until independently established.

| Original comparison topic | Non-usable conclusion and referral |
|---|---|
| Lessee model and original example | No current US finance/operating classification, expense or EBITDA conclusion; original USD 50,000 operating expense versus IFRS USD 54,761 rounded illustration is not a usable US result. Check this point with one of our partner accountants. |
| Low-value exemption | No universal current-US no-equivalent assertion. Check this point with one of our partner accountants. |
| Short-term exemption | No claim that election, term or purchase-option tests are identical. Check this point with one of our partner accountants. |
| Indexed rents | No blanket US no-remeasurement conclusion. Check this point with one of our partner accountants. |
| Restoration costs | No current ASC 410/842 measurement or cost-location conclusion. Check this point with one of our partner accountants. |
| Sale and leaseback | No current-US full-gain, sale-qualification or off-market adjustment conclusion. Check this point with one of our partner accountants. |
| Subleases | No current-US underlying-asset classification conclusion. Check this point with one of our partner accountants. |
| Discount rate | No current-US risk-free-election eligibility or priority conclusion. Check this point with one of our partner accountants. |
| Lessor model | No current-US sales-type/direct-financing/operating alignment conclusion. Check this point with one of our partner accountants. |
| Cash flows | No current-US operating/finance payment-classification conclusion. Check this point with one of our partner accountants. |

Provides computational and interpretive guidance on IFRS 16 only. Not an audit and not assurance. Lease measurement turns heavily on entity-specific facts and significant judgement. Have outputs reviewed and signed by a qualified accountant before they enter financial statements relied upon by third parties.

## Sources

| Official source | Actual operative read scope | Date read |
|---|---|---|
| [IFRS 16 Leases](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html) | .3–46, .47–69, .81–106; Appendix A relevant definitions; B3–B42, B58; C1/C1D–E, C20C–E/C21; read clauses and neighbouring conditions, not just retrieval | 2026-11-27 |
| [IAS 37](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias37.html) | .14–26, .36–48: obligation, probability, estimate, discounting and future events | 2026-11-27 |
| [IFRS 9](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html) | .4.3.1–7: embedded-derivative gate only; no full valuation | 2026-11-27 |
| [IAS 16](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html) | .60–62: depreciation method; no complete revaluation module | 2026-11-27 |
| [IAS 7](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html) | .31–34D and .64: IFRS 18 adoption-dependent interest cash flows | 2026-11-27 |

Not yet confirmed: no unproven conclusion is usable. The specific monetary, earlier-IAS-7, current-US, valuation, supporting-standard execution, local-adoption and EBITDA points are closed by the explicit non-usable referrals above. [Basis access attempt](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16-bc.html) and [earlier IAS 7 attempt](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2024/issued/ias7.html) reached the subscription landing page on 2026-11-27; neither is a completed paragraph read. The [ASC source](https://asc.fasb.org/) remains the previously documented unread source, not a new successful read.
