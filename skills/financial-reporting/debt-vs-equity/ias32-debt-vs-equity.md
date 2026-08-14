---
name: ias32-debt-vs-equity
description: "IFRS classification of issued financial instruments as financial liabilities, equity, or compound instruments under IAS 32 (Financial Instruments: Presentation), with the related liability-measurement rules in IFRS 9. Covers the substance-over-form principle, the contractual-obligation test, the fixed-for-fixed test for contracts settled in the entity's own equity, contingent settlement provisions, the puttable-instruments exception, split accounting for compound instruments (convertible bonds), treasury shares, classification of interest/dividends/gains/losses, and offsetting. Produces classification conclusions, journal entries (including compound-instrument split accounting), and a reviewer brief. Issued as the IFRS edition of the debt-vs-equity topic; see us-gaap-debt-vs-equity for the US GAAP edition. MUST load alongside financial-reporting-workflow-base."
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

# Ias32 Debt Vs Equity

## IFRS Debt vs. Equity — IAS 32 v0.1

## What this file is

**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the classification, measurement, presentation, and disclosure rules for issued financial instruments — distinguishing financial liabilities from equity, and splitting compound instruments — under IFRS. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

**Standard currency.** IAS 32 as effective, including the puttable-instruments amendments (effective annual periods beginning on or after 1 January 2009) and conforming changes for IFRS 9. Initial and subsequent **measurement** of the liability component is governed by IFRS 9; IAS 32 governs **classification and presentation**.

**Scope.** This skill addresses the **issuer's** classification of instruments it has issued. It does not cover the holder's classification of financial assets (IFRS 9), derivative measurement beyond the own-equity test, hedge accounting, or impairment.

## Section 1 — Scope statement

This skill covers, from the **issuer's** perspective:

- The substance-over-form classification principle (`IAS 32.15`–`16`).
- The contractual-obligation test for financial liabilities and the residual definition of equity.
- The fixed-for-fixed test for contracts settled in the entity's own equity instruments (`IAS 32.16(b)`, `.21`–`.24`).
- Contingent settlement provisions (`IAS 32.25`) and settlement options (`IAS 32.26`–`27`).
- The puttable-instruments and obligations-on-liquidation exceptions (`IAS 32.16A`–`16D`).
- Split accounting for compound financial instruments (`IAS 32.28`–`32`).
- Treasury shares (`IAS 32.33`–`34`), interest/dividends/gains/losses (`IAS 32.35`–`41`), and offsetting (`IAS 32.42`–`50`).
- Preference shares (mandatorily redeemable vs. discretionary-dividend non-redeemable).

This skill does NOT cover: classification of financial assets, derivative pricing/valuation methodology, hedge accounting, or distributions in specie (`IFRIC 17`). It defers the US GAAP treatment to `us-gaap-debt-vs-equity`.

## Section 2 — Reference layer (Layer A): the classification rules

### The core principle — `IAS 32.15`–`16`

- **Substance over form classification** — On initial recognition the issuer classifies the instrument (or its component parts) as a financial liability, a financial asset, or equity, in accordance with the substance of the contractual arrangement and the IAS 32 definitions — not its legal form. The label on the certificate ("share", "bond", "note") does not decide the answer.  _(IAS 32.15)_
- **When a financial liability exists** — A financial liability exists when the instrument contains either: (1) A contractual obligation to deliver cash or another financial asset to another entity, or to exchange financial assets/financial liabilities with another entity under conditions that are potentially unfavourable to the issuer; or (2) A contract that will or may be settled in the entity's own equity instruments and is: a non-derivative for which the entity is or may be obliged to deliver a variable number of its own equity instruments; or a derivative that will or may be settled other than by exchanging a fixed amount of cash (or another financial asset) for a fixed number of the entity's own equity instruments — the "fixed-for-fixed" test.  _(IAS 32.11, .16(a), IAS 32.16(b))_
- **When an instrument is equity** — An instrument is equity if, and only if, both: It includes no contractual obligation to deliver cash or another financial asset, or to exchange under potentially unfavourable conditions; and if it will or may be settled in the entity's own equity, it is either a non-derivative that includes no obligation to deliver a variable number of own shares, or a derivative that will be settled only by exchanging a fixed amount of cash for a fixed number of own shares.  _(IAS 32.16(a)–(b))_

⚑ AUDIT FLASH POINT — substance over form on preference shares. A "preference share" is the textbook trap. If dividends are mandatory or the share is mandatorily redeemable for cash, it is a financial liability (`IAS 32.18(a)`) even though it is legally share capital — and its "dividends" are interest expense in P&L (`IAS 32.40`). This moves amounts off equity and into profit or loss and changes leverage and EPS. Evidence the obligation analysis.

### The fixed-for-fixed test — `IAS 32.16(b)`, `.21`–`.24`

- **Fixed-for-fixed condition** — A contract settled in the entity's own equity is equity only if it exchanges a fixed amount of cash for a fixed number of the entity's own shares. The "fixed-for-fixed" condition fails — and the contract is a liability/derivative — where, for example: The number of shares to be delivered varies with the instrument's fair value or some other variable; the amount of cash to be received varies; Settlement is in a variable number of shares whose total value equals a fixed monetary amount (this is "shares as currency" → a liability); An issued put or forward obliges the entity to repurchase its own shares for cash → recognise a financial liability for the present value of the redemption amount, reclassified from equity.  _(IAS 32.16(b), .21–.24, IAS 32.21, IAS 32.20(b), IAS 32.23)_

⚑ AUDIT FLASH POINT — written put / forward on own shares. A contract obliging the entity to buy back its own shares for cash creates a liability for the present value of the redemption amount (`IAS 32.23`), even if the obligation is conditional and even though the underlying is the entity's own equity. The offsetting debit reduces equity. Reviewers must confirm the gross-settlement liability was recognised, not netted.

### Contingent settlement provisions — `IAS 32.25`

- **Contingent settlement provisions** — An instrument is a financial liability if settlement in cash (or another financial asset, or in a way that would otherwise be a liability) is contingent on uncertain future events outside the control of both the issuer and the holder — e.g. a change in a stock index, a consumer price index, interest rates, or the issuer's revenue/net income. Exceptions (still equity): the contingency is not genuine (only a remote, non-substantive possibility triggers cash settlement), or settlement in cash is required only on liquidation of the issuer.  _(IAS 32.25)_

### Settlement options — `IAS 32.26`–`27`

- **Settlement options with choice of method** — Where a derivative gives either party a choice of settlement method (cash vs. shares), it is a financial asset or financial liability unless all settlement alternatives would result in equity classification.  _(IAS 32.26–27)_

### The puttable-instruments exception — `IAS 32.16A`–`16D`

- **Puttable instrument equity exception conditions** — Some instruments meet the definition of a financial liability (because the holder can put them back for cash) yet are classified as equity by exception if all the conditions are met. A puttable instrument (16A–16B) is equity only if it: Entitles the holder to a pro rata share of net assets on liquidation; Is in the most subordinated class and all instruments in that class have identical features; Has no other contractual obligation to deliver cash/financial assets except the put; Has total expected cash flows based substantially on profit or loss, change in net assets, or change in fair value of the entity; and The issuer has no other instrument with terms that substantially fix or restrict the residual return to the puttable holders. A parallel exception (16C–16D) applies to instruments imposing an obligation only on liquidation that deliver a pro rata net-asset share. If the conditions later cease to be met, reclassify (16E–16F).  _(IAS 32.16A–16B, IAS 32.16C–16D, IAS 32.16E–16F)_

⚑ AUDIT FLASH POINT — puttable equity exception is narrow. The `16A`–`16D` exception is met by, e.g., open-ended fund units and some partnership/co-operative capital — but only if every condition holds. Failing one (e.g. a second class with a fixed return) tips the whole class into liability, which can wipe out reported equity. This is also a divergence point: US GAAP has no equivalent equity exception.

## Section 3 — Reference layer: compound instruments and special topics

### Compound (hybrid) instruments — split accounting — `IAS 32.28`–`32`

- **Split accounting method** — A non-derivative instrument that contains both a liability component and an equity component (the classic case: a convertible bond — debt plus a holder option to convert into a fixed number of shares) must be split on initial recognition. The method is prescribed: 1. Measure the liability component first, at the fair value of a similar liability without the conversion feature — i.e. the present value of the contractual cash flows (principal + coupons) discounted at the market rate for an equivalent non-convertible instrument. 2. Assign the residual (total issue proceeds minus the liability component) to the equity component (the conversion option). 3. The equity component is not remeasured subsequently. The liability component is measured at amortised cost under IFRS 9, unwinding the discount to the market rate as interest expense. 4. Transaction costs are allocated pro rata to the two components.  _(IAS 32.28–29, IAS 32.31–32, IAS 32.38)_

⚑ AUDIT FLASH POINT — the discount rate drives the split. The market rate for "similar non-convertible debt" is a significant estimate. A higher rate → a smaller liability and larger equity component → lower reported leverage but higher future interest expense. The rate must be evidenced (comparable issuances, credit spread, tenor). This is the single biggest divergence from US GAAP, which after ASU 2020-06 generally books one liability with no equity split (see §7).

### Conversion, redemption, and amendment — `IAS 32.AG32`

- **Conversion and redemption treatment** — On conversion at maturity, derecognise the liability component and reclassify it to equity; no gain or loss arises. On redemption/repurchase, allocate the consideration paid between liability and equity components using the same method applied at issuance; the liability-component difference goes to P&L, the equity-component difference to equity.  _(IAS 32.AG32, IAS 32.AG33–AG35)_

### Treasury shares — `IAS 32.33`–`34`

- **Treasury shares treatment** — An entity's reacquired own equity instruments ("treasury shares") are deducted from equity. No gain or loss is recognised in P&L on the purchase, sale, issue, or cancellation of own equity instruments; consideration paid or received is recognised directly in equity.  _(IAS 32.33)_

### Interest, dividends, gains, and losses — `IAS 32.35`–`36`

- **Distributions follow instrument classification** — Distributions and gains/losses follow the classification of the related instrument: Interest, dividends, losses and gains relating to a financial liability → profit or loss (e.g. "dividends" on redeemable preference shares are interest expense). Distributions to holders of an equity instrument → debited directly to equity, net of any related income tax benefit. Transaction costs of an equity transaction → deducted from equity.  _(IAS 32.35, IAS 32.37)_

### Offsetting — `IAS 32.42`

- **Offsetting conditions** — A financial asset and financial liability are offset (presented net) only when the entity (a) has a legally enforceable right to set off the recognised amounts and (b) intends either to settle net or to realise the asset and settle the liability simultaneously. Both conditions are mandatory.  _(IAS 32.42)_

### Preference shares — summary

**Preference shares — summary**

| Feature | Classification |
| --- | --- |
| **Mandatorily redeemable** for cash (fixed date/amount) | **Financial liability** (`IAS 32.18(a)`) |
| Redeemable **at the holder's option** | **Financial liability** (issuer cannot avoid cash outflow) |
| **Mandatory** (non-discretionary) dividends, non-redeemable | **Liability** for the dividend obligation (or compound) |
| **Discretionary** dividends, **non-redeemable** (issuer controls redemption) | **Equity** (`IAS 32.AG25`–`AG26`) |
| Redeemable **only at issuer's option** | **Equity** (no contractual obligation) |

## Section 4 — Executable layer (Layer B): the procedure

Run these steps on the instrument's facts. Each cites the Layer A rule it executes.

- **Step 1** — Read the contract for substance, not the label. List every settlement term, option, contingency, and redemption feature.  _(IAS 32.15)_
- **Step 2** — Apply the contractual-obligation test: is there any obligation to deliver cash/another financial asset, or to exchange under potentially unfavourable conditions, that the issuer cannot avoid? If yes → financial liability (in whole or part).  _(IAS 32.16(a))_
- **Step 3** — For own-equity settlement, apply the fixed-for-fixed test: fixed cash for fixed shares → equity; variable on either leg → liability/derivative.  _(IAS 32.16(b), .21–24)_
- **Step 4** — Check contingent settlement provisions: cash settlement contingent on an event outside both parties' control → liability, unless not genuine or only on liquidation.  _(IAS 32.25)_
- **Step 5** — Check the puttable / liquidation-only exceptions: if every condition is met, classify as equity by exception.  _(IAS 32.16A–16D)_
- **Step 6** — If the instrument is compound: measure the liability component at PV of cash flows at the market rate for similar non-convertible debt; assign the residual to equity; allocate transaction costs pro rata.  _(IAS 32.28–32)_
- **Step 7** — Book the journal entries (base §3 format) at initial recognition and over subsequent periods (discount unwind to interest expense; conversion/redemption).
- **Step 8** — Classify distributions: liability → P&L; equity → directly in equity.  _(IAS 32.35)_
- **Step 9** — Assess offsetting only if both conditions are met.  _(IAS 32.42)_
- **Step 10** — Produce the disclosure checklist (§6, plus IFRS 7) and reviewer brief with every flash point.

### Worked example (illustrative) — convertible bond, IFRS split accounting

On 1 Jan 20X1 an entity issues a $1,000,000 par, 3-year, 5% annual-coupon convertible bond at par. Each bond is convertible at the holder's option into a fixed number of the entity's ordinary shares at maturity (fixed-for-fixed → conversion option is equity). The market rate for a similar non-convertible 3-year bond of this issuer is 8%. Coupons of $50,000 are paid annually in arrears; principal $1,000,000 repaid (or converted) at the end of 20X3.

**Step 1 — Liability component = PV of cash flows at 8% (`IAS 32.31`)**  _(IAS 32.31)_

| Cash flow | Amount | PV factor @ 8% | Present value |
| --- | --- | --- | --- |
| Coupon, end 20X1 | 50,000 | 0.92593 | 46,296 |
| Coupon, end 20X2 | 50,000 | 0.85734 | 42,867 |
| Coupon, end 20X3 | 50,000 | 0.79383 | 39,692 |
| Principal, end 20X3 | 1,000,000 | 0.79383 | 793,832 |
| **Liability component** |  |  | **922,687** |

- **Step 2 — Equity component = residual** — $1,000,000 − $922,687 = $77,313  _(IAS 32.32)_

```
1 Jan 20X1 — issue of convertible bond, split accounting — driving rule: IAS 32.28–32
  Dr  Cash                                       1,000,000
      Cr  Convertible bond — liability component        922,687
      Cr  Equity — conversion option (other equity)      77,313
  (memo: liability = PV of coupons+principal at the 8% market rate for similar
   non-convertible debt; equity = residual proceeds. Debits = credits ✓)
```

Subsequent measurement — liability at amortised cost, effective rate 8% (IFRS 9). Coupon paid is 5% of par = $50,000; interest expense is 8% of the opening carrying amount; the difference accretes the liability toward par.

**Subsequent measurement — liability at amortised cost, effective rate 8%**

| Year | Opening | Interest @ 8% | Coupon paid | Closing |
| --- | --- | --- | --- | --- |
| 20X1 | 922,687 | 73,815 | 50,000 | 946,502 |
| 20X2 | 946,502 | 75,720 | 50,000 | 972,222 |
| 20X3 | 972,222 | 77,778 | 50,000 | 1,000,000 |

```
31 Dec 20X1 — accrue interest at effective rate, pay coupon — driving rule: IFRS 9 (amortised cost); IAS 32.35
  Dr  Interest expense (P&L)                         73,815
      Cr  Cash                                              50,000
      Cr  Convertible bond — liability component            23,815
  (memo: 8% × 922,687 = 73,815; coupon 5% × 1,000,000 = 50,000; accretion 23,815.
   Debits = credits ✓. Repeat each year on the table above.)
```

```
31 Dec 20X3 — conversion at maturity (assume all converted) — driving rule: IAS 32.AG32
  Dr  Convertible bond — liability component       1,000,000
  Dr  Equity — conversion option                       77,313
      Cr  Share capital / share premium                  1,077,313
  (memo: liability at par on conversion + equity option reclassified to issued
   capital; NO gain or loss on conversion per AG32. Debits = credits ✓)
```

If the bonds were redeemed for cash at maturity instead, the liability component is settled at $1,000,000 and the $77,313 equity component remains in equity (may be transferred within equity); no P&L gain/loss arises if redeemed at par.

⚑ AUDIT FLASH POINT — contrast with US GAAP single-liability. Under US GAAP post-ASU 2020-06, the same bond is generally one liability of $1,000,000 with no equity component (see `us-gaap-debt-vs-equity` §7) — so reported equity, leverage, and the interest-expense profile differ materially between the two frameworks for an identical instrument. A dual-reporter must run both editions and reconcile.

## Section 5 — Presentation

- **Presentation rules** — Liability components of issued instruments are presented within financial liabilities; current vs. non-current split per IAS 1. Equity components (e.g. the conversion option, the puttable-exception class) are presented within equity. Treasury shares are a deduction from equity, shown separately or in retained earnings/a treasury-share reserve. Distributions on liability-classified instruments are interest expense in P&L; distributions on equity instruments are movements within equity. Offset a financial asset and liability only where both IAS 32.42 conditions are met.  _(IAS 32.33, IAS 32.35–40, IAS 32.42, IAS 1)_

## Section 6 — Divergence from US GAAP (ASC 480 / 470-20 / 815-40 / 505)

This is the section a dual-reporter scrutinises most. For an identical instrument the two frameworks frequently reach different classifications and amounts.

**IFRS vs US GAAP divergence table**

| Area | IFRS (IAS 32) | US GAAP (ASC 480/470-20/815-40) |
| --- | --- | --- |
| **Convertible bonds** | **Split** into liability + equity components; liability = PV at market rate, equity = residual (`IAS 32.28`–`32`) | Post-**ASU 2020-06**, generally **a single liability** — no equity (BCF/cash-conversion separation **eliminated**); split only for a substantial premium or an embedded derivative bifurcated under ASC 815 |
| **Mezzanine / temporary equity** | **No such category.** Redeemable instruments outside the issuer's control are generally **financial liabilities** | **Temporary equity** between liabilities and permanent equity for SEC registrants (`ASC 480-10-S99-3A`) — redeemable preferred, redeemable NCI |
| **Own-equity contracts** | **Fixed-for-fixed** test (`IAS 32.16(b)`); a non-functional-currency settlement amount generally **fails** fixed-for-fixed | **Indexed-to-own-stock** assessment (`ASC 815-40-15`); has an explicit **FX exception** for fixed-monetary-amount-in-a-different-currency cases — assessment and outcome differ |
| **Puttable instruments** | **Equity by exception** if `IAS 32.16A`–`16D` conditions met | **No equity exception** — typically a liability or, for SEC filers, temporary equity |
| **Mandatorily redeemable instruments** | **Liability** (`IAS 32.18(a)`) | **Liability** (`ASC 480-10-25-4`), but scope (freestanding vs. embedded) and the timing/condition nuances differ |
| **"Dividends" on liability-classified preferred** | **Interest expense** in P&L (`IAS 32.40`) | Generally also a charge to income, but presentation/EPS mechanics differ |

Run `us-gaap-debt-vs-equity` in parallel for dual-reporters and present both answers (base §2).

## Section 7 — Disclosure checklist — `IAS 32` + `IFRS 7`

Trigger and produce as relevant:

- [ ] Accounting policy for classifying instruments as liabilities or equity
- [ ] For **compound instruments**: existence of the equity conversion option, the split between components, and the terms of conversion (`IFRS 7.17`)
- [ ] For instruments classified as equity under the **puttable exception**: the `IAS 32.136A` disclosures (summary quantitative data, objectives/policies for managing the obligation, expected cash outflow on redemption, how it was determined)
- [ ] Terms and conditions of each material instrument: coupon/dividend, maturity, conversion ratio, redemption and put/call features (`IFRS 7.7`, `.31`)
- [ ] **Reclassifications** between liability and equity and their effect (e.g. puttable exception ceasing to be met)
- [ ] Treasury shares: amount held and deducted from equity
- [ ] Defaults and breaches of loan terms on liability-classified instruments (`IFRS 7.18`–`19`)
- [ ] Interest expense on liability-classified instruments (incl. redeemable preference "dividends")
- [ ] Offsetting disclosures where financial assets/liabilities are set off (`IFRS 7.13A`–`13F`)

## Section 8 — Topic self-checks (in addition to base §7)

- [ ] Classification driven by **substance**, not legal form; each conclusion cites its `IAS 32` paragraph
- [ ] Contractual-obligation test applied (can the issuer avoid delivering cash/financial assets?)
- [ ] Fixed-for-fixed test applied to any own-equity-settled contract; variability on either leg flagged
- [ ] Contingent settlement provisions assessed (`IAS 32.25`); "not genuine" / "only on liquidation" exceptions documented
- [ ] Puttable / liquidation-only exception conditions tested **in full** (all conditions met, or not equity)
- [ ] Compound instruments **split**: liability = PV at market rate for similar non-convertible debt; equity = residual; transaction costs allocated pro rata
- [ ] Subsequent measurement shown: discount unwind to interest expense; conversion (no gain/loss) or redemption split
- [ ] Distributions classified per `IAS 32.35` (liability → P&L; equity → equity)
- [ ] Treasury shares deducted from equity, no P&L gain/loss
- [ ] Offsetting applied only where both `IAS 32.42` conditions met
- [ ] **Divergence from US GAAP** checked for dual-reporters (especially convertible split vs. single liability, and mezzanine equity)

## Section 9 — Disclaimer

Provides computational and interpretive guidance on IAS 32 (with IFRS 9 for liability measurement) only. Not an audit and not assurance. Classifying instruments as liabilities or equity turns heavily on the specific contractual terms and significant judgement. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

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
