---
name: us-gaap-asc842-leases
description: US GAAP lease accounting under ASC 842 (Leases). Covers the lessee dual model — every lease (other than short-term) puts a right-of-use asset and a lease liability on the balance sheet, then splits into finance leases (front-loaded interest + straight-line ROU amortization) versus operating leases (a single straight-line total lease cost). Covers lease identification and the finance-versus-operating classification criteria, initial and subsequent measurement, the discount rate, short-term and component elections, variable lease payments, remeasurement and reassessment triggers, modifications, the lessor model (sales-type, direct financing, operating), and sale-leaseback. Produces classification conclusions, journal entries, and a reviewer brief. Issued as the US GAAP edition of the leases topic; see ifrs16-leases for the IFRS edition. MUST load alongside financial-reporting-workflow-base.
version: 0.1
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
depends_on:
  - financial-reporting-workflow-base
category: financial-reporting
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US GAAP Asc842 Leases

## US GAAP Leases — ASC 842 v0.1

## What this file is

**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the recognition, measurement, presentation, and disclosure rules for leases under US GAAP. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

- **Standard currency** — ASC 842 as effective for all entities (public business entities since annual periods beginning after 15 Dec 2018; all other entities after 15 Dec 2021). ASC 842 superseded ASC 840. Confirm no entity-specific scope exclusion applies.  _(ASC 842)_
- **Scope** — ASC 842 applies to leases of property, plant, and equipment except: leases of intangible assets (ASC 350), leases to explore for or use minerals/oil/gas (ASC 930), leases of biological assets, leases of inventory, and leases of assets under construction.  _(ASC 842-10-15-1)_

## Section 1 — Scope statement

This skill covers:

- Identifying a lease — an identified asset the customer controls the use of (`ASC 842-10-15-3` to `15-16`).
- The **lessee dual model**: classification as finance or operating, and the differing P&L pattern of each.
- Initial and subsequent measurement of the lease liability and right-of-use (ROU) asset (`ASC 842-20-30`, `-35`).
- The discount rate, short-term lease exemption, and the practical expedient not to separate lease/non-lease components.
- Variable lease payments, remeasurement, reassessment, and modifications.
- The **lessor model**: sales-type, direct financing, and operating leases (`ASC 842-30`).
- Sale-and-leaseback (`ASC 842-40`, tied to the `ASC 606` control-transfer test).

This skill does NOT cover: leveraged leases grandfathered under ASC 840 transition, lease revenue subject to `ASC 606`, or impairment of ROU assets (handled by `ASC 360`, cross-referenced). It defers the IFRS treatment to `ifrs16-leases`.

### Step 0 — Is there a lease? — `ASC 842-10-15-3` to `15-16`

- **Lease definition and control test** — A contract is or contains a lease if it conveys the right to control the use of an identified asset for a period in exchange for consideration. Control requires both: (1) the right to obtain substantially all of the economic benefits from use of the identified asset (15-17); and (2) the right to direct the use of the asset (15-20) — i.e. the customer decides how and for what purpose the asset is used. An asset is identified when explicitly or implicitly specified, and the supplier has no substantive substitution right (15-9 to 15-14). If the supplier can substitute the asset for its own economic benefit, there is no identified asset and no lease — it is a service contract.  _(ASC 842-10-15-3 to 15-16)_

### Step 1 — Determine the lease term — `ASC 842-10-30-1`

- **Lease term definition** — Lease term = non-cancellable period + periods covered by an option to extend that the lessee is reasonably certain to exercise + periods covered by an option to terminate that the lessee is reasonably certain not to exercise.  _(ASC 842-10-30-1)_

⚑ AUDIT FLASH POINT — reasonably-certain option assessment. Renewal/termination judgement directly sizes both the ROU asset and the lease liability, and it gates classification. "Reasonably certain" is a high threshold based on economic incentive (significant leasehold improvements, below-market rate, importance of the location). Document the incentive analysis; this is the most-challenged lessee judgement.

### Step 2 — Classify the lease (lessee) — `ASC 842-10-25-2` to `25-3`

- **Finance lease classification criteria** — A lease is a finance lease if it meets any one of the following five criteria at commencement; otherwise it is an operating lease: (a) The lease transfers ownership of the underlying asset to the lessee by the end of the term. (b) The lease grants a purchase option the lessee is reasonably certain to exercise. (c) The lease term is for the major part of the remaining economic life of the asset (unless commencement is at or near the end of the asset's economic life — 25-3(b)). (d) The present value of the lease payments plus any lessee-guaranteed residual value equals or exceeds substantially all of the fair value of the underlying asset. (e) The asset is so specialized that it is expected to have no alternative use to the lessor at the end of the term.  _(ASC 842-10-25-2 to 25-3)_

⚑ AUDIT FLASH POINT — "major part" and "substantially all" are no longer bright lines. ASC 842 deliberately removed ASC 840's 75% / 90% bright lines, but `ASC 842-10-55-2` permits an entity to use those thresholds as one reasonable approach. Many preparers retain ≈75% (major part) and ≈90% (substantially all) as a policy. The threshold chosen is a judgement that can flip classification — and classification changes the P&L pattern and EBITDA. Document the policy and the inputs.

### Step 3 — Both classifications: recognize ROU asset + lease liability — `ASC 842-20-25-1`

- **Dual recognition** — Critically, both finance and operating leases recognize a right-of-use asset and a lease liability on the balance sheet (842-20-30-1, -30-5). The dual model lives in the P&L pattern and subsequent measurement, not in whether the lease is on the balance sheet.  _(ASC 842-20-25-1)_

### Initial measurement — `ASC 842-20-30`

- **Lease liability discount rate** — Lease liability = present value of the lease payments not yet paid, discounted at the rate implicit in the lease if readily determinable; otherwise the lessee's incremental borrowing rate (IBR). A lessee that is not a public business entity may elect, as an accounting policy by asset class, to use a risk-free rate.  _(842-20-30-1, -30-2, -30-3)_
- **Lease payments included** — Lease payments included: fixed payments (less incentives receivable), in-substance fixed payments, variable payments that depend on an index or rate (measured using the index/rate at commencement), the exercise price of a reasonably-certain purchase option, termination penalties if the term reflects termination, and amounts probable of being owed under a residual value guarantee.  _(842-10-30-5)_
- **ROU asset formula** — ROU asset = lease liability + lease payments made at/before commencement (prepaid) + initial direct costs − lease incentives received  _(842-20-30-5)_

### Subsequent measurement — the dual model — `ASC 842-20-35`

- **Finance lease subsequent measurement** — The lease liability accretes at the discount rate; each payment is split into interest expense and principal reduction (effective-interest method). The ROU asset is amortized, generally straight-line, over the shorter of the lease term or the asset's useful life (over useful life if ownership transfers or a purchase option is reasonably certain). P&L shows two separate line items — interest + amortization — which are front-loaded (interest is higher early when the liability is larger).  _(842-20-35-1 to -35-7)_
- **Operating lease subsequent measurement** — A single total lease cost is recognized on a straight-line basis over the lease term (total payments ÷ term). The lease liability still accretes at the discount rate (interest on the liability), and the ROU asset is reduced by the difference between the straight-line cost and the periodic interest on the liability (the ROU amortization is the plug). This keeps total cost level even as the interest/principal split changes. P&L shows one line — operating lease cost — typically in operating expenses, not split into interest and amortization. This preserves EBITDA relative to a finance lease.  _(842-20-35-3 to -35-6)_

### Short-term lease exemption — `ASC 842-20-25-2`

- **Short-term lease exemption** — A lessee may elect, by class of underlying asset, not to recognize an ROU asset or lease liability for a short-term lease — a lease with a term of 12 months or less that does not include a purchase option the lessee is reasonably certain to exercise. Recognize the lease cost straight-line over the term.  _(ASC 842-20-25-2)_
- **Short-term lease term threshold** — 12 months or less months  _(ASC 842-20-25-2)_

### Separating components — `ASC 842-10-15-28` to `15-42`

- **Separating lease and non-lease components** — Consideration is allocated between lease and non-lease components (e.g. maintenance) on a relative standalone-price basis. A lessee may elect, by asset class, the practical expedient not to separate non-lease components — accounting for the whole as a single lease component (842-10-15-37), which grosses up the ROU asset and liability.  _(ASC 842-10-15-28 to 15-42)_

### Variable lease payments — `ASC 842-20-55-1`

- **Variable lease payment treatment** — Variable payments that depend on an index or rate are included in the liability at the index/rate in effect at commencement; subsequent changes in that index/rate are expensed as incurred (they do not trigger remeasurement on their own). Variable payments based on usage or performance (e.g. % of sales) are excluded from the liability and expensed as incurred.  _(ASC 842-20-55-1)_

⚑ AUDIT FLASH POINT — index-based payments are frozen at day one. A common error is remeasuring the liability every time CPI moves. Under US GAAP, a change in an index/rate alone is a period expense, not a remeasurement (`842-20-35-5`). Remeasurement is triggered only by the events below — and this differs in mechanics from IFRS 16.

### Remeasurement and reassessment triggers — `ASC 842-20-35-4` to `-35-5`

- **Remeasurement triggers** — Remeasure the lease liability (and adjust the ROU asset) when: the lease term or a purchase-option assessment changes (35-4); the amount probable of being owed under a residual value guarantee changes; a contingency resolves such that some variable payments become fixed (in-substance fixed). Reassess classification only on a modification not accounted for as a separate contract, or on a change in lease term / purchase-option assessment (842-10-25-1).  _(ASC 842-20-35-4 to -35-5)_

### Modifications — `ASC 842-10-25-8` to `25-18`

- **Modification treatment** — A modification that grants an additional right of use at a price commensurate with its standalone price → separate new lease. Otherwise, remeasure the existing lease at the modification date using a revised discount rate, and reclassify if the criteria warrant. A modification that fully or partially terminates a lease reduces the ROU asset/liability with any difference to P&L.  _(ASC 842-10-25-8 to 25-18)_

### Lessor model — `ASC 842-30`

- **Lessor classification tests** — Lessor classification mirrors the lessee finance criteria (a)–(e) plus collectibility and residual tests: Sales-type lease — meets any of criteria (a)–(e) (842-10-25-2). Derecognize the asset, recognize a net investment in the lease and selling profit/loss at commencement (842-30-25-1). Direct financing lease — fails (a)–(e) but the PV of payments + any third-party residual guarantee ≥ substantially all of fair value, and collection is probable (842-10-25-3). Selling profit is deferred into the net investment. Operating lease — neither of the above. The lessor keeps the asset on its books and recognizes lease income straight-line (842-30-25-11).  _(ASC 842-30)_

### Sale-and-leaseback — `ASC 842-40`

- **Sale-leaseback treatment** — First test whether the transfer is a sale under ASC 606 (does control pass to the buyer-lessor?). If a leaseback would be a finance lease for the seller-lessee, the transfer is not a sale — account for it as a financing (the asset stays on the seller's books; proceeds are a borrowing) (842-40-25-2). If control transfers and the leaseback is operating, it is a sale — recognize the full gain/loss on the sale, adjusted for any off-market terms (842-40-30-1 to -30-3). US GAAP recognizes the full gain on the rights sold (subject to off-market adjustment), unlike IFRS 16's proportional-gain mechanic.  _(ASC 842-40-25-2, 842-40-30-1 to -30-3)_

## Section 4 — Executable layer (Layer B): the procedure

Run these steps on the transaction's facts. Each cites the Layer A rule it executes.

1. **Confirm a lease exists** (Step 0 / §2): identified asset + control. If it is a service contract, stop — not in ASC 842.
2. **Determine the lease term** (Step 1 / §2): include reasonably-certain renewals/terminations.
3. **Check the short-term exemption** (§3, `842-20-25-2`): if ≤ 12 months and no reasonably-certain purchase option, expense straight-line and stop.
4. **Classify** finance vs. operating (Step 2 / §2): test criteria (a)–(e); state the policy thresholds used.
5. **Determine the discount rate** (§3): implicit rate, else IBR, else (non-PBE election) risk-free rate.
6. **Measure the lease liability** = PV of lease payments (§3). Show the PV math in a memo line.
7. **Measure the ROU asset** = liability + prepaid + initial direct costs − incentives (§3).
8. **Book day-1 recognition** and **subsequent-period** entries (base §3 format) per the classification's P&L pattern.
9. **Handle variable payments, remeasurement, modifications** as triggered (§3).
10. **Classify balances and cash flows**, produce the **disclosure checklist** (§6) and **reviewer brief** with every flash point.

### Worked example (illustrative)

A lessee leases equipment for 5 years, paying $50,000 annually in arrears. The rate implicit in the lease is not readily determinable, so the lessee uses its incremental borrowing rate of 6%. There are no initial direct costs, prepayments, or incentives. PV of an ordinary annuity, 5 periods @ 6% = annuity factor 4.2124.

> Lease liability = 50,000 × 4.2124 = $210,618 (rounded). ROU asset = $210,618.

#### Day 1 — recognition (identical for finance and operating) — `ASC 842-20-30-1`, `-30-5`

```
Day 1 — recognize ROU asset and lease liability — driving rule: ASC 842-20-30-1 / -30-5
  Dr  Right-of-use asset                     210,618
      Cr  Lease liability                         210,618
  (memo: PV = 50,000 × annuity factor 4.2124 @ 6%, 5 yrs; no IDC/prepaid/incentive; debits = credits ✓)
```

#### Year 1 — FINANCE LEASE — `ASC 842-20-35-1` to `-35-7`

Interest = 6% × 210,618 = 12,637. Payment 50,000 → principal reduction = 50,000 − 12,637 = 37,363. ROU amortization (straight-line) = 210,618 ÷ 5 = 42,124.

```
End of Yr 1 — accrue interest and pay — driving rule: ASC 842-20-35-1 (effective interest)
  Dr  Interest expense                        12,637
  Dr  Lease liability                         37,363
      Cr  Cash                                     50,000
  (memo: interest 6% × 210,618 = 12,637; principal plug 37,363; liability → 173,255; debits 50,000 = credits 50,000 ✓)

End of Yr 1 — amortize ROU asset — driving rule: ASC 842-20-35-7 (straight-line)
  Dr  Amortization expense                    42,124
      Cr  Right-of-use asset (accum. amort.)      42,124
  (memo: 210,618 / 5 = 42,124; ROU → 168,494; debits = credits ✓)
```

Year-1 total P&L (finance) = 12,637 + 42,124 = 54,761 — front-loaded (> the 50,000 cash payment early on). Interest hits below the EBITDA line; amortization is a non-cash add-back.

#### Year 1 — OPERATING LEASE — `ASC 842-20-35-3` to `-35-6`

Single straight-line lease cost = 250,000 ÷ 5 = 50,000 per year. The liability still accretes interest of 12,637; the ROU asset is reduced by the plug = 50,000 − 12,637 = 37,363 so that total cost stays level at 50,000.

```
End of Yr 1 — single straight-line operating lease cost — driving rule: ASC 842-20-25-6
  Dr  Operating lease cost (operating expense) 50,000
      Cr  Lease liability (interest accretion)      12,637
      Cr  Right-of-use asset (amortization plug)    37,363
  (memo: SL cost 250,000/5 = 50,000; interest 6% × 210,618 = 12,637; ROU plug = 50,000 − 12,637 = 37,363; debits 50,000 = credits 50,000 ✓)

End of Yr 1 — pay the lessor — driving rule: ASC 842-20-35-3
  Dr  Lease liability                         50,000
      Cr  Cash                                     50,000
  (memo: liability after accretion 223,255 then payment 50,000 → 173,255; matches finance-lease liability balance; debits = credits ✓)
```

Year-1 total P&L (operating) = 50,000, a single line above EBITDA — flat across all five years. Note the lease liability follows the identical amortization schedule under both models (173,255 after Year 1); only the ROU asset and the P&L geography/pattern differ.

> ⚑ AUDIT FLASH POINT — classification swings EBITDA and the expense pattern, not the liability. Finance vs. operating produces the same balance-sheet liability schedule but a higher, front-loaded total cost and an EBITDA-favourable geography (interest + amortization vs. a single operating expense) under finance. A wrong classification misstates EBITDA, leverage covenants, and the expense trajectory. Evidence the criteria (a)–(e) conclusion and the threshold policy.

## Section 5 — Divergence from IFRS 16

The headline divergence in leases is the lessee model itself, and it is one of the largest US-GAAP/IFRS differences in practice.

**US GAAP vs IFRS 16 comparison table**  _(IFRS 16.31, .36, .5-.8, .42, .100, .61)_

| Area | US GAAP (ASC 842) | IFRS (IFRS 16) |
| --- | --- | --- |
| **Lessee model** | **Dual model** — finance *or* operating. Operating leases keep a **single straight-line operating expense** (EBITDA-neutral) | **Single model** — **all** leases front-loaded: depreciation of ROU + interest on liability. **Boosts EBITDA, raises finance costs** (`IFRS 16.31`, `.36`) |
| Operating-lease P&L pattern | One straight-line line; no interest/amortization split | No operating leases for lessees; every lease is front-loaded |
| **Low-value asset exemption** | **None** | **Yes** — leases of low-value assets (~USD 5,000 new) may be expensed (`IFRS 16.5`–`.8`); unique to IFRS |
| Short-term exemption | ≤ 12 months, by asset class (`842-20-25-2`) | ≤ 12 months, by asset class (`IFRS 16.5`) — same |
| Index-linked payment remeasurement | Change in index/rate alone is **expensed**, no remeasurement (`842-20-35-5`) | Change in index/rate **triggers remeasurement** of the liability (`IFRS 16.42`) |
| Discount-rate fallback | Risk-free-rate election available to non-PBEs | No risk-free election |
| Sale-leaseback gain | **Full gain** on rights sold (off-market adjusted) | **Proportional gain** — only on rights transferred to the buyer (`IFRS 16.100`) |
| Lessor model | Sales-type / direct financing / operating (`842-30`) | Finance / operating (`IFRS 16.61`) — substantially aligned |
| Cash-flow presentation | Operating-lease payments → **operating**; finance-lease principal → **financing**, interest per policy | All lease principal → **financing**; interest per policy. IFRS pushes more cash to financing |

Always run `ifrs16-leases` in parallel for dual-reporters and present both answers (base §2). The same lease can be a flat $50,000 operating expense under ASC 842 and a front-loaded $54,761 (depreciation + interest) under IFRS 16.

## Section 6 — Disclosure checklist — `ASC 842-20-50`

Trigger and produce as relevant:

- [ ] Nature of leases, terms, options, and significant judgements (`50-3`)
- [ ] Total lease cost disaggregated: finance (amortization + interest), operating lease cost, short-term, variable, and sublease income (`50-4`)
- [ ] Weighted-average remaining lease term and weighted-average discount rate, by finance and operating (`50-4`)
- [ ] Cash paid for amounts in lease liabilities, split by operating/financing (`50-4`)
- [ ] ROU assets obtained in exchange for new lease liabilities (`50-4`)
- [ ] **Maturity analysis** of lease liabilities (undiscounted) for each of the next five years and thereafter, reconciled to the discounted liability (`50-6`)
- [ ] Practical expedients and accounting policy elections taken — short-term, non-separation of components, risk-free rate (`50-9`)
- [ ] Lessor disclosures: lease income, net investment components, residual-value risk management (`842-30-50`)

## Section 7 — Topic self-checks (in addition to base §7)

- [ ] Lease vs. service determined (identified asset + control of use); cited `842-10-15`
- [ ] Lease term includes only reasonably-certain renewals/terminations
- [ ] Short-term exemption considered (≤ 12 mo, no reasonably-certain purchase option)
- [ ] Classification tested against all five criteria (a)–(e); threshold policy (≈75% / ≈90%) stated as judgement
- [ ] **Both** ROU asset and lease liability recognized (dual model is P&L pattern, not on/off balance sheet)
- [ ] Discount rate: implicit, else IBR, else risk-free (non-PBE) — stated
- [ ] Lease liability = PV of payments; PV math shown in a memo line
- [ ] ROU = liability + prepaid + IDC − incentives
- [ ] Finance: interest (effective rate) + straight-line ROU amortization, front-loaded
- [ ] Operating: single straight-line cost; ROU reduced by the plug; liability accretes
- [ ] Index/rate payments frozen at commencement; usage-based excluded
- [ ] Remeasurement/modification triggers checked
- [ ] Lessor classification (sales-type / direct financing / operating) where the entity is the lessor
- [ ] Divergence from IFRS 16 checked for dual-reporters (especially the single vs. dual model)

## Section 8 — Disclaimer

Provides computational and interpretive guidance on ASC 842 only. Not an audit and not assurance. Lease classification and measurement turn heavily on entity-specific facts and significant judgement (lease term, discount rate, classification thresholds). Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

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
