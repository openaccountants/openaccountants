---
name: ifrs16-leases
description: "IFRS lease accounting under IFRS 16 (Leases). Covers the lessee single model — every lease (other than the two recognition exemptions) puts a right-of-use asset and a lease liability on the balance sheet, and the expense is ALWAYS front-loaded: depreciation of the ROU asset plus interest on the lease liability, with no operating/finance split for lessees. Covers lease identification, the short-term and low-value-asset exemptions, initial and subsequent measurement, the discount rate, variable lease payments, reassessment and remeasurement triggers, modifications, sale-and-leaseback, the sublease classification rule, and the retained lessor dual model (finance versus operating). Produces recognition conclusions, journal entries, and a reviewer brief. Issued as the IFRS edition of the leases topic; see us-gaap-asc842-leases for the US GAAP edition. MUST load alongside financial-reporting-workflow-base."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - financial-reporting-workflow-base
category: financial-reporting
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ifrs16 Leases

## IFRS Leases — IFRS 16 v0.1

## What this file is

**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the recognition, measurement, presentation, and disclosure rules for leases under IFRS. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

- **Standard currency** — IFRS 16 as effective for annual periods beginning on or after 1 January 2019, superseding IAS 17, IFRIC 4, SIC-15, and SIC-27. Confirm no scope exclusion applies.  _(IFRS 16)_
- **Scope** — IFRS 16 applies to all leases except: leases to explore for or use minerals/oil/gas, leases of biological assets (IAS 41), service concession arrangements (IFRIC 12), licences of intellectual property granted by a lessor (IFRS 15), and rights held under licensing agreements for items such as films, patents, and copyrights (IAS 38).  _(IFRS 16.3)_

## Section 1 — Scope statement

This skill covers:

- Identifying a lease — an identified asset the customer controls the use of (`IFRS 16.9`–`.11`, `B9`–`B33`).
- The **lessee single model**: one accounting treatment for every lease (other than exemptions), always front-loaded.
- The **two recognition exemptions**: short-term leases and low-value-asset leases (`IFRS 16.5`–`.8`).
- Initial and subsequent measurement of the lease liability and right-of-use (ROU) asset (`IFRS 16.22`–`.38`).
- The discount rate, variable lease payments, reassessment, remeasurement, and modifications.
- Sale-and-leaseback (`IFRS 16.98`–`.103`) and sublease classification (`IFRS 16.B58`).
- The **lessor model** retained from IAS 17: finance vs. operating (`IFRS 16.61`–`.97`).

This skill does NOT cover: lessor revenue subject to `IFRS 15`, impairment of ROU assets (`IAS 36`, cross-referenced). It defers the US GAAP treatment to `us-gaap-asc842-leases`.

## Section 2 — Reference layer (Layer A): identifying a lease and the single model

### Step 0 — Is there a lease? — `IFRS 16.9`–`.11`, `B9`–`B33`

- **Lease identification test** — A contract is, or contains, a lease if it conveys the right to control the use of an identified asset for a period in exchange for consideration. Control requires both: 1) The right to obtain substantially all of the economic benefits from use of the identified asset (B21–B23); and 2) The right to direct the use of the asset (B24–B30). An asset is identified when explicitly or implicitly specified and the supplier has no substantive substitution right (B13–B19). If the supplier benefits economically from substituting and is practically able to, there is no identified asset — it is a service contract.  _(IFRS 16.9–.11, B9–B33)_

### Step 1 — Determine the lease term — `IFRS 16.18`–`.21`

- **Lease term determination** — Lease term = non-cancellable period + periods covered by an extension option the lessee is reasonably certain to exercise + periods covered by a termination option the lessee is reasonably certain not to exercise.  _(IFRS 16.18–.21)_

⚑ AUDIT FLASH POINT — reasonably-certain option assessment. Renewal/termination judgement sizes both the ROU asset and the lease liability. "Reasonably certain" is a high threshold based on economic incentive (significant leasehold improvements, below-market rate, criticality of the asset). Document the incentive analysis — this is the most-challenged lessee judgement, and under IFRS it is not softened by any operating-lease alternative.

### Step 2 — The lessee SINGLE model — `IFRS 16.22`

- **Lessee single model** — At the commencement date, a lessee recognizes a right-of-use asset and a lease liability for every lease, except those to which a recognition exemption is applied (§3). There is no finance-versus-operating classification for lessees — IFRS 16 abolished it. Every recognized lease is measured and expensed on the same (front-loaded) basis.  _(IFRS 16.22)_

### Step 3 — The expense is ALWAYS front-loaded — `IFRS 16.31`, `.36`–`.38`

- **Front-loaded expense mechanics** — The ROU asset is depreciated (typically straight-line) over the shorter of the lease term and the asset's useful life — over the useful life if ownership transfers or a purchase option is reasonably certain (16.32). The lease liability accretes interest at the discount rate; each payment splits into interest and principal (16.36–.38). Because interest is higher in early periods (larger liability) while depreciation is level, the total periodic expense is front-loaded for every lease. This is the IFRS 16 signature: it raises EBITDA (depreciation and interest sit below it) but increases finance costs and front-loads total profit-or-loss impact.  _(IFRS 16.31, .36–.38)_

## Section 3 — Reference layer: exemptions, measurement, and special topics

### The two recognition exemptions — `IFRS 16.5`–`.8`

- **Recognition exemptions** — A lessee may elect not to apply the single model to: 1) Short-term leases — a lease with a term of 12 months or less at commencement, with no purchase option (16.5(a), definition in Appendix A). Elected by class of underlying asset. 2) Leases of low-value assets — assets that, when new, are of low value (16.5(b), B3–B8). The Basis for Conclusions (BC100) indicates the IASB had in mind assets of around USD 5,000 or less when new (e.g. tablets, small office furniture, telephones). Elected on a lease-by-lease basis. The assessment is on absolute value when new, regardless of materiality to the lessee. For exempt leases, recognize the payments as an expense on a straight-line basis (or another systematic basis) over the term (16.6).  _(IFRS 16.5–.8)_

⚑ AUDIT FLASH POINT — low-value exemption is unique to IFRS and is an absolute, not relative, test. There is no US GAAP equivalent (ASC 842 has only the short-term exemption). The ~USD 5,000-when-new guide is not a hard cap and is judged per asset, not per portfolio — bundling many low-value assets into one lease does not disqualify the items, but the assessment must be on each underlying asset's value when new. Document the policy and the per-asset basis.

### Initial measurement — `IFRS 16.24`–`.28`

- **Lease liability initial measurement** — Lease liability = present value of the lease payments not yet paid, discounted at the interest rate implicit in the lease if readily determinable; otherwise the lessee's incremental borrowing rate.  _(IFRS 16.26–.27)_
- **Lease payments included** — Lease payments included (16.27): fixed payments (less incentives receivable), variable payments that depend on an index or rate (measured initially using the index/rate at commencement), amounts expected under residual value guarantees, the exercise price of a reasonably-certain purchase option, and termination penalties if the term reflects termination.  _(IFRS 16.27)_
- **ROU asset initial measurement** — ROU asset (16.24) = lease liability + lease payments made at/before commencement (prepaid) + initial direct costs − lease incentives received + an estimate of dismantling/removal/restoration costs the lessee is obligated to incur (recognized as a provision under IAS 37).  _(IFRS 16.24)_

⚑ AUDIT FLASH POINT — restoration costs are baked into the ROU asset. IFRS 16.24(d) brings the day-one dismantling/restoration provision into the ROU asset (mirrored by an IAS 37 provision). Omitting it understates both the asset and the provision and distorts depreciation. ASC 842 handles asset retirement obligations under separate guidance (ASC 410), so the day-one ROU figure can differ between frameworks.

### Subsequent measurement — `IFRS 16.29`–`.46`

- **Subsequent measurement rules** — ROU asset carried at cost less accumulated depreciation and impairment (cost model), or revaluation/fair-value models where the related IFRS (IAS 16, IAS 40) is applied to that asset class. Lease liability remeasured for reassessments and modifications (below).  _(IFRS 16.29–.46)_

### Variable lease payments — `IFRS 16.27(b)`, `.42`

- **Variable lease payments treatment** — Payments depending on an index or rate are included in the liability at the index/rate at commencement; when the index or rate changes, the liability is remeasured using revised payments (16.42(b)), with the adjustment against the ROU asset. Variable payments based on usage or performance (e.g. % of sales) are excluded and expensed as incurred (16.38(b)).  _(IFRS 16.27(b), .42)_

⚑ AUDIT FLASH POINT — index-linked remeasurement differs from US GAAP. Under IFRS 16 a change in the index/rate triggers remeasurement of the liability; under ASC 842 the same change is simply expensed with no remeasurement. This is a genuine mechanical divergence for CPI-linked rents — flag for dual-reporters.

### Reassessment and remeasurement — `IFRS 16.39`–`.43`

- **Reassessment and remeasurement triggers** — Remeasure the liability (adjusting the ROU asset; once the ROU asset is reduced to nil, further reductions go to P&L) when: the lease term or purchase-option assessment changes (use a revised discount rate); the amount expected under a residual value guarantee changes; or future payments change due to an index/rate (use an unchanged discount rate for index/rate-only changes).  _(IFRS 16.39–.43)_

### Modifications — `IFRS 16.44`–`.46`

- **Modification treatment** — A modification that increases scope by adding a right of use at a price commensurate with its standalone price → separate lease (16.44). Otherwise, remeasure the liability using a revised discount rate at the effective date. A modification that decreases scope reduces the ROU asset and recognizes a gain or loss on the partial termination in P&L (16.46); other modifications adjust the ROU asset only.  _(IFRS 16.44–.46)_

### Sale-and-leaseback — `IFRS 16.98`–`.103`

- **Sale-and-leaseback treatment** — First apply IFRS 15 to determine whether the transfer is a sale (does control pass to the buyer-lessor?). If it is a sale, the seller-lessee measures the ROU asset arising from the leaseback at the proportion of the previous carrying amount of the asset that relates to the right of use it retains, and recognizes a gain or loss only on the rights transferred to the buyer-lessor (16.100). Off-market terms are adjusted (16.101). If the transfer is not a sale, the seller-lessee continues to recognize the asset and accounts for the proceeds as a financial liability under IFRS 9 (16.103).  _(IFRS 16.98–.103)_

⚑ AUDIT FLASH POINT — proportional gain, not full gain. IFRS 16 recognizes a gain only on the rights transferred to the buyer-lessor, retaining the rest in the ROU asset. ASC 842 generally recognizes the full gain on a qualifying sale. The recognized gain on the same transaction can differ materially — a recurring dual-reporter reconciling item.

### Sublease classification — `IFRS 16.B58`

- **Sublease classification rule** — When a lessee subleases an asset (intermediate lessor), the sublease is classified by reference to the ROU asset arising from the head lease — not the underlying asset. If the sublease covers a major part of the ROU asset's term/value, the intermediate lessor classifies the sublease as a finance lease and derecognizes the relevant ROU asset; otherwise it is operating.  _(IFRS 16.B58)_

### Lessor model (retained dual model) — `IFRS 16.61`–`.97`

- **Lessor dual model** — IFRS 16 kept the IAS 17 lessor model: a lessor classifies each lease as finance or operating (16.61). Finance lease — transfers substantially all the risks and rewards incidental to ownership (16.62, indicators in 16.63–.64: ownership transfer, bargain purchase option, term covering major part of economic life, PV of payments ≥ substantially all of fair value, specialized asset). Derecognize the asset; recognize a net investment in the lease (16.67–.68). Operating lease — otherwise; keep the asset and recognize lease income straight-line (16.81).  _(IFRS 16.61–.97)_

## Section 4 — Executable layer (Layer B): the procedure

Run these steps on the transaction's facts. Each cites the Layer A rule it executes.

1. **Confirm a lease exists** (Step 0 / §2): identified asset + control. If a service contract, stop.
2. **Determine the lease term** (Step 1 / §2): include reasonably-certain renewals/terminations.
3. **Check the exemptions** (§3, `16.5`–`.8`): short-term (≤ 12 mo, no purchase option) or low-value (~USD 5,000 when new). If elected, expense straight-line and stop.
4. **Determine the discount rate** (§3): implicit rate, else IBR.
5. **Measure the lease liability** = PV of lease payments (`16.26`). Show the PV math in a memo line.
6. **Measure the ROU asset** = liability + prepaid + initial direct costs − incentives + restoration estimate (`16.24`).
7. **Book day-1 recognition**, then **subsequent-period** entries (base §3 format): depreciation of ROU + interest on liability — **front-loaded for every lease**.
8. **Handle variable payments, reassessment, modifications, subleases** as triggered (§3).
9. **If the entity is the lessor**, classify finance vs. operating (`16.61`).
10. **Classify balances and cash flows**, produce the **disclosure checklist** (§6) and **reviewer brief** with every flash point.

### Worked example (illustrative)

Same facts as the US GAAP edition: a lessee leases equipment for 5 years, paying $50,000 annually in arrears, implicit rate not determinable, incremental borrowing rate 6%. No initial direct costs, prepayments, incentives, or restoration obligation. PV of an ordinary annuity, 5 periods @ 6% = 4.2124.

> Lease liability = 50,000 × 4.2124 = $210,618 (rounded). ROU asset = $210,618.

Under IFRS 16 there is no operating-lease alternative — the single model is applied, and the pattern is identical to the US GAAP finance-lease pattern.

#### Day 1 — recognition — `IFRS 16.22`, `.24`, `.26`

```
Day 1 — recognize ROU asset and lease liability — driving rule: IFRS 16.22 / .24 / .26
  Dr  Right-of-use asset                     210,618
      Cr  Lease liability                         210,618
  (memo: PV = 50,000 × annuity factor 4.2124 @ 6%, 5 yrs; no IDC/prepaid/incentive/restoration; debits = credits ✓)
```

#### Year 1 — single model (front-loaded) — `IFRS 16.31`, `.36`–`.38`

Interest = 6% × 210,618 = 12,637. Payment 50,000 → principal reduction = 50,000 − 12,637 = 37,363. Depreciation (straight-line) = 210,618 ÷ 5 = 42,124.

```
End of Yr 1 — accrue interest and pay — driving rule: IFRS 16.36-38 (effective interest)
  Dr  Interest expense (finance cost)         12,637
  Dr  Lease liability                         37,363
      Cr  Cash                                     50,000
  (memo: interest 6% × 210,618 = 12,637; principal plug 37,363; liability → 173,255; debits 50,000 = credits 50,000 ✓)

End of Yr 1 — depreciate ROU asset — driving rule: IFRS 16.31 (straight-line)
  Dr  Depreciation expense                    42,124
      Cr  Right-of-use asset (accum. depn.)       42,124
  (memo: 210,618 / 5 = 42,124; ROU → 168,494; debits = credits ✓)
```

Year-1 total P&L = 12,637 + 42,124 = 54,761 — front-loaded and declining thereafter as interest falls. Both lines sit below EBITDA (depreciation in operating, interest in finance costs), so EBITDA is higher than it would be under an ASC 842 operating lease (where the full $50,000 is an operating expense). On the cash-flow statement, the entire $50,000 is split between financing (principal $37,363) and the interest portion per policy — IFRS pushes lease cash into financing.

⚑ AUDIT FLASH POINT — same transaction, different P&L from US GAAP. This identical lease is a flat $50,000 operating expense under ASC 842 (operating classification) but a front-loaded $54,761 (depreciation + interest) under IFRS 16, lifting EBITDA and finance costs. For a US subsidiary of an IFRS parent, the group and statutory numbers diverge every period — surface the reconciliation.

## Section 5 — Divergence from US GAAP (ASC 842)

The headline divergence in leases is the lessee model itself — IFRS's single model vs. US GAAP's dual model.

**Divergence from US GAAP comparison table**  _(Section 5 — Divergence from US GAAP (ASC 842))_

| Area | IFRS (IFRS 16) | US GAAP (ASC 842) |
| --- | --- | --- |
| **Lessee model** | **Single model** — every lease front-loaded: depreciation of ROU + interest on liability. **Boosts EBITDA, raises finance costs** (`16.31`, `.36`) | **Dual model** — finance *or* operating. Operating leases keep a **single straight-line operating expense** (EBITDA-neutral) |
| **Low-value asset exemption** | **Yes** — ~USD 5,000-when-new guide, per asset (`16.5`–`.8`); **unique to IFRS** | **None** |
| Short-term exemption | ≤ 12 months, by asset class (`16.5`) | ≤ 12 months, by asset class (`842-20-25-2`) — same |
| Index-linked payment remeasurement | Change in index/rate **triggers remeasurement** of the liability (`16.42`) | Change in index/rate alone is **expensed**, no remeasurement (`842-20-35-5`) |
| Restoration/dismantling costs | Included in the day-one ROU asset (`16.24(d)`) with an IAS 37 provision | Handled under separate ARO guidance (`ASC 410`); not folded into ROU the same way |
| Sale-leaseback gain | **Proportional gain** — only on rights transferred to the buyer (`16.100`) | **Full gain** on rights sold (off-market adjusted) |
| Sublease classification | By reference to the **ROU asset** of the head lease (`16.B58`) | By reference to the **underlying asset** |
| Discount-rate fallback | Implicit, else IBR (no risk-free election) | Implicit, else IBR; **risk-free-rate election** for non-PBEs |
| Lessor model | Finance / operating (`16.61`) — retained from IAS 17 | Sales-type / direct financing / operating (`842-30`) — substantially aligned |
| Cash-flow presentation | **All** lease principal → **financing**; interest per policy. Pushes more cash to financing | Operating-lease payments → **operating**; finance-lease principal → financing |

Always run `us-gaap-asc842-leases` in parallel for dual-reporters and present both answers (base §2).

## Section 6 — Disclosure checklist — `IFRS 16.51`–`.60`

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

## Section 7 — Topic self-checks (in addition to base §7)

- [ ] Lease vs. service determined (identified asset + control of use); cited `16.9`–`.11`, `B9`–`B33`
- [ ] Lease term includes only reasonably-certain renewals/terminations
- [ ] Exemptions considered: short-term (≤ 12 mo, no purchase option) **and** low-value (~USD 5,000 new, per asset)
- [ ] **Single model** applied — no finance/operating split attempted for the lessee
- [ ] Discount rate: implicit, else IBR — stated
- [ ] Lease liability = PV of payments; PV math shown in a memo line
- [ ] ROU = liability + prepaid + IDC − incentives + restoration estimate (IAS 37 provision booked)
- [ ] Subsequent: depreciation of ROU + interest on liability — front-loaded for every lease
- [ ] Index/rate payments **remeasured** on change (contrast ASC 842); usage-based excluded
- [ ] Reassessment/modification triggers checked (revised vs. unchanged discount rate applied correctly)
- [ ] Sale-leaseback uses proportional-gain mechanic; sublease classified by reference to the ROU asset
- [ ] Lessor classification (finance / operating) where the entity is the lessor
- [ ] Divergence from ASC 842 checked for dual-reporters (especially the single vs. dual model)

## Section 8 — Disclaimer

Provides computational and interpretive guidance on IFRS 16 only. Not an audit and not assurance. Lease measurement turns heavily on entity-specific facts and significant judgement (lease term, discount rate, low-value and exemption elections, restoration estimates). Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

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
