---
name: us-gaap-debt-vs-equity
description: US GAAP classification of issued financial instruments as liabilities, equity, mezzanine (temporary) equity, or compound instruments under ASC 480 (Distinguishing Liabilities from Equity), ASC 470-20 (convertible debt, as amended by ASU 2020-06), ASC 815-40 (contracts in an entity's own equity), and ASC 505 (equity). Covers the three classes of freestanding instruments classified as liabilities, the post-ASU 2020-06 single-liability model for most convertible debt, the indexed-to-own-stock and equity-classification conditions, and SEC temporary/mezzanine equity. Produces classification conclusions, journal entries, and a reviewer brief. Issued as the US GAAP edition of the debt-vs-equity topic; see ias32-debt-vs-equity for the IFRS edition. MUST load alongside financial-reporting-workflow-base.
version: 0.1
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
depends_on: - financial-reporting-workflow-base
category: financial-reporting
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US GAAP Debt Vs Equity

## US GAAP Debt vs. Equity — ASC 480 / 470-20 / 815-40 / 505 v0.1

## What this file is

**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the classification, measurement, presentation, and disclosure rules for issued financial instruments under US GAAP — distinguishing liabilities from equity, identifying temporary (mezzanine) equity, and accounting for convertible debt. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

**Standard currency.** ASC 480, ASC 815-40, and ASC 505 as effective, and ASC 470-20 **as amended by ASU 2020-06** (*Debt — Debt with Conversion and Other Options; Derivatives and Hedging — Contracts in Entity's Own Equity*), effective for public business entities for fiscal years beginning after 15 December 2021 and for all other entities after 15 December 2023. ASU 2020-06 **eliminated** the cash-conversion and most beneficial-conversion-feature (BCF) separation models.

**Scope.** This skill addresses the **issuer's** classification of instruments it has issued. It does not cover the holder's classification, embedded-derivative measurement methodology beyond bifurcation triggers, EPS computation, or share-based payment (ASC 718).

## Section 1 — Scope statement

- **Scope covered** — The three classes of freestanding instruments classified as liabilities (or assets) under ASC 480; convertible debt under ASC 470-20 after ASU 2020-06 (single-liability default; the limited remaining separation cases); contracts in the entity's own equity under ASC 815-40 (indexed-to-own-stock assessment and equity-classification conditions); temporary (mezzanine) equity for SEC registrants under ASC 480-10-S99-3A; treasury stock and the classification of dividends/distributions (ASC 505-30, 505-10).  _(ASC 480; ASC 470-20; ASC 815-40; ASC 480-10-S99-3A; ASC 505-30; ASC 505-10)_
- **Scope excluded** — This skill does NOT cover: share-based payment (ASC 718), EPS (ASC 260), embedded-derivative valuation methodology, or the holder's accounting. It defers the IFRS treatment to ias32-debt-vs-equity.  _(ASC 718; ASC 260)_

## Section 2 — Reference layer (Layer A): the classification rules

### The order of analysis

- **Sequence of analysis for freestanding financial instruments** — For a freestanding financial instrument, US GAAP applies a sequence: (1) Is it within the scope of and classified as a liability under ASC 480? If not, (2) for SEC registrants, is it redeemable such that it must sit in temporary equity (ASC 480-10-S99-3A)? (3) For contracts in own equity, does it meet the ASC 815-40 indexation and equity-classification conditions, or is it a derivative/liability? Convertible debt runs through ASC 470-20 (post-ASU 2020-06) with an ASC 815-15 embedded-derivative screen.  _(ASC 480; ASC 480-10-S99-3A; ASC 815-40; ASC 470-20; ASC 815-15)_

### ASC 480 — three classes classified as liabilities — `ASC 480-10-25`

- **Freestanding financial instrument liability classification** — A freestanding financial instrument is classified as a liability (or in some cases an asset) if it falls into any of three classes.  _(ASC 480-10-25)_
- **Class 1 — Mandatorily redeemable financial instruments** — An instrument embodying an unconditional obligation requiring the issuer to redeem it by transferring assets at a specified or determinable date or on an event certain to occur (e.g. mandatorily redeemable preferred stock). Liability classification applies even though the instrument is legally equity.  _(ASC 480-10-25-4)_
- **Class 2 — Obligations to repurchase the issuer's equity shares by transferring assets** — Instruments that embody an obligation (other than only on liquidation/termination) to repurchase the issuer's own shares, or that are indexed to such an obligation, and that may require settlement by transferring assets — e.g. a written put option or a forward purchase contract on the issuer's own shares.  _(ASC 480-10-25-8)_
- **Class 3 — Certain obligations settleable in a variable number of shares** — Instruments embodying an unconditional obligation, or a financial instrument other than an outstanding share that may require settlement by issuing a variable number of shares, where the monetary value of the obligation at inception is based predominantly on any one of: a fixed monetary amount known at inception (e.g. a note settleable in $1m of shares); variations in something other than the issuer's own share price (e.g. a commodity price or an index); or variations inversely related to the issuer's share price (e.g. a written put settled in shares).  _(ASC 480-10-25-14)_
- **AUDIT FLASH POINT — mandatorily redeemable preferred is a liability, dividends are interest** — A preferred share that must be redeemed for cash on a fixed date is an ASC 480-10-25-4 liability; its "dividends" are recognised in interest expense, not as an equity distribution. Misclassifying it as equity overstates equity and understates expense. (Note: ASC 480 defers liability classification for certain mandatorily redeemable instruments of non-SEC-registrant entities and for those redeemable only on liquidation — ASC 480-10-65 / 25-4 scope nuances. Document the scope conclusion.)  _(ASC 480-10-25-4; ASC 480-10-65)_

### ASC 470-20 — convertible debt after ASU 2020-06 — `ASC 470-20-25`

- **Single liability default after ASU 2020-06** — ASU 2020-06 eliminated the cash-conversion model and most of the beneficial-conversion-feature (BCF) model. For most convertible debt instruments the issuer records the entire proceeds as a debt liability with no separation of an equity component. The conversion feature is not bifurcated into equity.  _(ASC 470-20-25 as amended)_
- **Separation required — substantial premium** — If convertible debt is issued at a substantial premium, the premium may be attributable to the conversion feature and recorded in paid-in capital.  _(ASC 470-20-25-13)_
- **Separation required — embedded derivative requiring bifurcation** — If the conversion feature (or another embedded feature) meets the ASC 815-15-25 criteria for separation from the debt host (not clearly-and-closely related, would be a derivative standalone, and does not qualify for the own-equity scope exception in ASC 815-10-15-74(a)/ASC 815-40), bifurcate it as an embedded derivative liability measured at fair value, with changes in P&L.  _(ASC 815-15-25; ASC 815-10-15-74(a); ASC 815-40)_
- **AUDIT FLASH POINT — single-liability default is the headline divergence from IFRS** — Post-ASU 2020-06, a plain convertible bond is one liability at full proceeds with no equity component under US GAAP, whereas IAS 32 always splits it into liability + equity. For an identical bond, reported equity, leverage, and the interest-expense profile differ between frameworks. Confirm no embedded-derivative bifurcation or substantial-premium fact pattern overrides the single-liability default.  _(ASC 470-20-25; IAS 32)_

### ASC 815-40 — contracts in the entity's own equity — `ASC 815-40-15` and `-25`

- **Two gates for equity classification** — A contract on the issuer's own stock (e.g. warrants, written options, forward sale of shares, the conversion feature screened above) avoids derivative/liability treatment — i.e. qualifies for equity classification — only if it passes two gates.  _(ASC 815-40-15; ASC 815-40-25)_
- **Gate 1 — Indexed to the entity's own stock** — A two-step test: (Step 1) evaluate the contract's exercise contingencies (must not be based on an observable market/index other than those referenced to the issuer's own operations or stock); (Step 2) evaluate the settlement provisions — the settlement amount must equal the difference between the fair value of a fixed number of shares and a fixed monetary amount (a "fixed-for-fixed" analogue, but not identical to IAS 32). A notable allowance: a strike price denominated in a currency other than the issuer's functional currency does not by itself preclude indexation under US GAAP — an FX exception that differs from IFRS.  _(ASC 815-40-15-5 to 15-8; ASC 815-40-15-7I)_
- **Gate 2 — Equity classification conditions** — Settlement in unregistered shares is permitted, the entity has sufficient authorised and unissued shares, there is an explicit share cap, no required cash payment if the entity fails to timely file, no cash-settled top-off/make-whole, and the contract ranks no higher than other equity in a bankruptcy — among others. Failing any condition → asset/liability (derivative), remeasured through earnings.  _(ASC 815-40-25-1 to 25-43)_
- **AUDIT FLASH POINT — share-settled vs. cash-settled, and the FX exception** — Whether a warrant is equity or a fair-valued liability hinges on the ASC 815-40-25 conditions; a single failing condition (e.g. a net-cash-settlement provision on a failed registration) makes the whole instrument a liability remeasured through earnings, injecting P&L volatility. The functional-currency-strike conclusion can differ from IFRS's fixed-for-fixed — flag for dual-reporters.  _(ASC 815-40-25)_

### ASC 480-10-S99-3A — temporary (mezzanine) equity — SEC registrants

- **Temporary equity classification conditions** — For SEC registrants, an equity-classified instrument (most commonly redeemable preferred stock or redeemable non-controlling interest) that is redeemable: at a fixed or determinable price on a fixed or determinable date, at the option of the holder, or upon an event not solely within the control of the issuer, and that is not already a liability under ASC 480, must be presented in "temporary equity" — a mezzanine section between liabilities and permanent equity on the balance sheet. Subsequent measurement follows one of two methods (accrete to the redemption amount over the period to the earliest redemption date, or recognise changes immediately).  _(ASC 480-10-S99-3A)_
- **AUDIT FLASH POINT — temporary equity has no IFRS equivalent** — A redeemable preferred whose redemption is outside the issuer's control sits in mezzanine equity under SEC US GAAP, but is generally a financial liability under IAS 32. This is a structural balance-sheet difference, not a measurement nuance. Confirm registrant status and the "outside the issuer's control" assessment.  _(ASC 480-10-S99-3A; IAS 32)_

### Treasury stock and distributions — `ASC 505-30`, `505-10`

- **Treasury stock and dividend classification** — Reacquired own shares (treasury stock) are recorded as a reduction of equity (cost or par-value method); no gain or loss in earnings on reacquisition/reissuance — differences go to paid-in capital / retained earnings. Dividends declared on equity-classified stock reduce retained earnings; "dividends" on liability-classified instruments are interest expense.  _(ASC 505-30; ASC 505-10)_

## Section 3 — Reference layer: high-frequency special topics

- **Freestanding vs. embedded** — ASC 480 applies to freestanding instruments; conversion and similar features inside a host contract are embedded and screened under ASC 815-15 for bifurcation. Getting this scoping wrong is the most common error.  _(ASC 480-10-25 scope; ASC 815-15)_
- **Order of consolidation/sequencing** — When an entity has multiple contracts competing for the same authorised shares, evaluate sequencing to determine whether enough shares remain for equity classification.  _(ASC 815-40-25)_
- **Down-round features** — A down-round feature no longer precludes equity classification of an otherwise-equity instrument; its effect is recognised as a deemed dividend when triggered (interaction with EPS).  _(ASU 2017-11)_
- **Convertible debt issuance costs** — Post-ASU 2020-06, issuance costs are allocated entirely to the single debt liability and amortised as part of the effective interest rate (no allocation to an equity component, because there generally is none).  _(post-ASU 2020-06)_
- **Induced conversions / extinguishments** — Conversions induced by sweetened terms, and repurchases, follow the extinguishment/induced-conversion guidance.  _(ASC 470-20-40)_

## Section 4 — Executable layer (Layer B): the procedure

Run these steps on the instrument's facts. Each cites the Layer A rule it executes.

- **Step 1** — Determine freestanding vs. embedded (ASC 480-10 scope / ASC 815-15). Freestanding → continue with ASC 480; embedded feature → screen under ASC 815-15.  _(ASC 480-10; ASC 815-15)_
- **Step 2** — Run the ASC 480 three-class test (480-10-25-4, -8, -14): mandatorily redeemable? obligation to repurchase own shares by transferring assets? variable-share obligation based predominantly on a fixed amount / non-share variable / inverse to share price? Any → liability.  _(ASC 480-10-25-4; ASC 480-10-25-8; ASC 480-10-25-14)_
- **Step 3** — If convertible debt (ASC 470-20): default to a single liability at full proceeds; check for a substantial premium (25-13) or an embedded derivative needing bifurcation (ASC 815-15-25).  _(ASC 470-20; ASC 470-20-25-13; ASC 815-15-25)_
- **Step 4** — For contracts on own equity (ASC 815-40): apply the indexed-to-own-stock two-step test (15-5 to 15-8, incl. the FX allowance) and the equity-classification conditions (25-1 to 25-43). Pass both → equity; fail → derivative/liability remeasured through earnings.  _(ASC 815-40-15-5 to 15-8; ASC 815-40-25-1 to 25-43)_
- **Step 5** — For SEC registrants, screen equity instruments for temporary equity (480-10-S99-3A); set up accretion to the redemption amount if applicable.  _(ASC 480-10-S99-3A)_
- **Step 6** — Book the journal entries (base §3 format) at initial recognition and over subsequent periods (effective-interest accretion, fair-value remeasurement of any liability-classified contract, mezzanine accretion).  _(base §3)_
- **Step 7** — Classify distributions: interest expense (liability) vs. dividend to retained earnings (equity); deemed dividend for any down-round trigger.
- **Step 8** — Produce the disclosure checklist (§6) and reviewer brief with every flash point.  _(§6)_

### Worked example (illustrative) — convertible bond, US GAAP single liability

Same as the IFRS edition for direct comparison: on 1 Jan 20X1 a non-SEC-or-SEC entity issues a $1,000,000 par, 3-year, 5% annual-coupon convertible bond at par, convertible into a fixed number of the issuer's shares. The market rate for similar non-convertible debt is 8%. Assume the conversion feature does not require bifurcation (it meets the ASC 815-40 own-equity scope exception) and there is no substantial premium.

Under ASU 2020-06 the cash-conversion separation model is eliminated; with no bifurcated derivative and no substantial premium, the entire $1,000,000 proceeds are recorded as a single debt liability with no equity component (ASC 470-20-25). Because the bond was issued at par, there is no discount/premium to amortise and the coupon rate equals the carrying yield — the 8% market rate for "similar non-convertible debt" is not used to split the instrument (contrast IFRS, which uses 8% to carve out an equity component).

1 Jan 20X1 — issue of convertible bond, single liability — driving rule: ASC 470-20-25 (post-ASU 2020-06)
  Dr  Cash                                       1,000,000
      Cr  Convertible debt (liability)                 1,000,000
  (memo: full proceeds to a single liability; NO equity conversion component
   recognised. Debits = credits ✓)

31 Dec 20X1 — coupon paid (issued at par, no discount) — driving rule: ASC 835-30 effective interest
  Dr  Interest expense (P&L)                         50,000
      Cr  Cash                                              50,000
  (memo: 5% coupon = carrying yield because issued at par; no amortisation.
   Repeats end 20X2 and 20X3. Debits = credits ✓)

31 Dec 20X3 — conversion at maturity (assume all converted) — driving rule: ASC 470-20-40 (book-value method)
  Dr  Convertible debt (liability)               1,000,000
      Cr  Common stock / additional paid-in capital     1,000,000
  (memo: carrying amount of the debt reclassified to equity on conversion; no
   gain or loss under the book-value method. Debits = credits ✓)

Contrast with IFRS (see ias32-debt-vs-equity §4). For the identical bond, IAS 32 splits the proceeds into a $922,687 liability (PV at 8%) and a $77,313 equity conversion option, then accretes the liability to par at an 8% effective rate (interest expense $73,815 / $75,720 / $77,778 vs. US GAAP's flat $50,000). Same cash flows, materially different equity, leverage, and interest expense.

The single-liability answer holds only if the conversion (and any other embedded) feature is not a bifurcated derivative and the bond is not issued at a substantial premium. If the conversion feature failed the ASC 815-40 own-equity scope exception (e.g. a net-cash-settlement or insufficient-shares problem), it would be a fair-valued embedded derivative with earnings volatility — a completely different P&L.

## Section 5 — Presentation

- **ASC 480 liabilities presentation** — ASC 480 liabilities are presented within liabilities, even where the instrument is legally equity (e.g. mandatorily redeemable preferred).  _(ASC 480)_
- **Temporary (mezzanine) equity presentation** — Temporary (mezzanine) equity is presented between liabilities and permanent equity on an SEC registrant's balance sheet, captioned separately.  _(ASC 480-10-S99-3A)_
- **Equity-classified contracts presentation** — Equity-classified contracts (qualifying warrants, conversion features where separated as a substantial premium) sit in permanent equity / additional paid-in capital.
- **Treasury stock presentation** — Treasury stock reduces equity; no earnings gain/loss on reacquisition or reissuance.  _(ASC 505-30)_
- **Distributions presentation** — Interest expense for liability-classified instruments; dividends to retained earnings for equity; deemed dividend on a triggered down-round feature.

## Section 6 — Divergence from IFRS (IAS 32 / IFRS 9)

This is the section a dual-reporter scrutinises most. For an identical instrument the two frameworks frequently reach different classifications and amounts.

**US GAAP vs IFRS divergence table**  _(ASC 480/470-20/815-40; IAS 32)_

| Area | US GAAP (ASC 480/470-20/815-40) | IFRS (IAS 32) |
| --- | --- | --- |
| **Convertible bonds** | Post-**ASU 2020-06**, generally **a single liability** at full proceeds — no equity component (BCF/cash-conversion separation **eliminated**); split only for a substantial premium or a bifurcated embedded derivative | **Split** into liability (PV at market rate) + equity (residual) — **always** for a conventional convertible (`IAS 32.28`–`32`) |
| **Mezzanine / temporary equity** | **Temporary equity** between liabilities and permanent equity for SEC registrants (`ASC 480-10-S99-3A`) — redeemable preferred, redeemable NCI | **No such category** — typically a **financial liability** under IAS 32 |
| **Own-equity contracts** | **Indexed-to-own-stock** test (`ASC 815-40-15`) with an explicit **FX exception** (non-functional-currency strike does not preclude indexation, `15-7I`) | **Fixed-for-fixed** test (`IAS 32.16(b)`); a non-functional-currency settlement amount generally **fails** fixed-for-fixed |
| **Puttable instruments** | **No equity exception** — generally a liability or, for SEC filers, temporary equity | **Equity by exception** if `IAS 32.16A`–`16D` conditions met |
| **Mandatorily redeemable instruments** | **Liability** (`ASC 480-10-25-4`), with deferrals/scope nuances for non-SEC entities and liquidation-only redemption | **Liability** (`IAS 32.18(a)`), with its own scope nuances |
| **"Dividends" on liability-classified preferred** | Charged to income (interest); EPS/presentation mechanics differ | **Interest expense** in P&L (`IAS 32.40`) |

Run `ias32-debt-vs-equity` in parallel for dual-reporters and present both answers (base §2).

## Section 7 — Disclosure checklist — `ASC 480-10-50`, `470-20-50`, `815-40-50`, SEC S-X

- **ASC 480 instruments disclosure** — Nature and terms, including redemption requirements, settlement alternatives, and the number of shares potentially issuable.  _(ASC 480-10-50-1 to 50-3)_
- **Mandatorily redeemable instruments disclosure** — Amount that would be paid and number of shares, at the balance-sheet date as if settlement occurred.  _(ASC 480-10-50-2)_
- **Convertible debt disclosure** — Principal, coupon, conversion terms, conversion price, number of shares on conversion, and (post-ASU 2020-06) the if-converted EPS effect.  _(ASC 470-20-50)_
- **Own-equity contracts disclosure** — Terms, classification (equity vs. liability), and fair-value/remeasurement information for liability-classified contracts.  _(ASC 815-40-50)_
- **Temporary (mezzanine) equity disclosure** — Separate balance-sheet caption, redemption terms, accretion method and amounts.  _(ASC 480-10-S99-3A)_
- **Treasury stock disclosure** — Shares held and method (cost/par).
- **Down-round feature triggered disclosure** — Deemed dividend and EPS effect.  _(ASU 2017-11)_
- **Defaults/covenant breaches disclosure** — Defaults/covenant breaches on liability-classified instruments.

## Section 8 — Topic self-checks (in addition to base §7)

- [ ] Freestanding vs. embedded scoping resolved first; each conclusion cites its ASC paragraph
- [ ] ASC 480 three-class test applied (`25-4`, `25-8`, `25-14`); mandatorily-redeemable / repurchase-obligation / variable-share cases identified
- [ ] Convertible debt: **single-liability** default applied unless a substantial premium or a bifurcated embedded derivative is documented (`ASC 470-20`, `815-15-25`)
- [ ] Own-equity contracts: **indexed-to-own-stock** two-step test **and** equity-classification conditions both applied (`ASC 815-40-15`, `-25`); FX allowance noted
- [ ] SEC registrants screened for **temporary (mezzanine) equity**; accretion method stated (`480-10-S99-3A`)
- [ ] Subsequent measurement shown: effective-interest on debt, fair-value remeasurement of any liability-classified contract, mezzanine accretion
- [ ] Distributions classified: interest expense (liability) vs. dividend to retained earnings (equity); deemed dividend on down-round trigger
- [ ] Treasury stock reduces equity, no earnings gain/loss
- [ ] **Divergence from IAS 32** checked for dual-reporters (especially single-liability convertible vs. split, and mezzanine vs. liability)

## Section 9 — Disclaimer

Provides computational and interpretive guidance on ASC 480 / 470-20 / 815-40 / 505 only. Not an audit and not assurance. Classifying instruments as liabilities, equity, or temporary equity turns heavily on the specific contractual terms, registrant status, and significant judgement. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

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
