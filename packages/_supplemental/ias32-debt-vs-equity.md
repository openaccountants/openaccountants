---
name: ias32-debt-vs-equity
description: "IFRS classification of issued financial instruments as financial liabilities, equity, or compound instruments under IAS 32 (Financial Instruments: Presentation), with the related liability-measurement rules in IFRS 9. Covers the substance-over-form principle, the contractual-obligation test, the fixed-for-fixed test for contracts settled in the entity's own equity, contingent settlement provisions, the puttable-instruments exception, split accounting for compound instruments (convertible bonds), treasury shares, classification of interest/dividends/gains/losses, and offsetting. Produces classification conclusions, journal entries (including compound-instrument split accounting), and a reviewer brief. Issued as the IFRS edition of the debt-vs-equity topic; see us-gaap-debt-vs-equity for the US GAAP edition. MUST load alongside financial-reporting-workflow-base."
version: 0.4
jurisdiction: GLOBAL
last_updated: 2026-11-16
depends_on:
  - financial-reporting-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-reporting
type: computation
standard: "IAS 32 Financial Instruments: Presentation"
effective_date: 2014-01-01
source_checked: 2026-11-16
---

# IAS 32 debt versus equity v0.4

**Coverage is partial:** the individually identified supporting-standard and current US comparison gaps below remain outside usable instructions.

**General reference only.** Produces working papers and a reviewer brief, not an audit, assurance opinion or signed financial statements. Tier 2; not approved by an accountant.

## Scope

**Standard and effective-date basis:** IAS 32 Financial Instruments: Presentation; effective-date key **2014-01-01** for the offsetting amendments. Paragraph .97L applies them retrospectively for annual periods beginning on or after 1 January 2014. Earlier application requires disclosure and the associated IFRS 7 offsetting disclosures; obtain that separately sourced disclosure analysis. This date does not establish IFRS 9/17/18 adoption. [IAS 32.97L](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html).


**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the classification, measurement, presentation, and disclosure rules for issued financial instruments  -  distinguishing financial liabilities from equity, and splitting compound instruments  -  under IFRS. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.


**Scope.** This skill addresses the **issuer's** classification of instruments it has issued. It does not cover the holder's classification of financial assets (IFRS 9), derivative measurement beyond the own-equity test, hedge accounting, or impairment.


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


**Version basis for 2026 work.** The effective-date field identifies the directly read core amendment basis (offsetting amendments, IAS 32.97L). The puttable/liquidation exception amendment applies to annual periods beginning on or after 1 January 2009; early application requires disclosure and the related IAS 1/IAS 39/IFRS 7/IFRIC 2 amendments together (.96A). It is a limited exception, not applicable by analogy or automatically under other Standards (.96B-.96C). IFRS 9 initially applies to annual periods beginning on or after 1 January 2018; early application generally requires disclosure, all requirements and Appendix C amendments together, subject to the stated transition exceptions including the historical own-credit-only election (.7.1.1-.2). Apply IFRS 17 consequential provisions only when that Standard applies; its separate transition date was not recovered here. IFRS 18/IFRS 19 consequential presentation/disclosure changes are excluded until adopted. The 2026 issued HTML also contains future-effective text; do not assume its publication year is its effective date. The operative core was personally read in the official copy retrieved on 14 November 2026. Official source retrieval succeeded again on 16 November 2026; the core was reconciled with that body and the selected supporting clauses below were personally read. Source dates distinguish those reads from mere retrieval.

## Ask the client first

- Issuer reporting framework, reporting period, group versus separate accounts and early-adopted standards.
- Complete instrument terms, side agreements, redemption/dividend obligations and who controls settlement alternatives.
- Number/class of own shares, settlement currency, contingencies, puts, liquidation and subordination rights.
- Proceeds, costs, coupon/maturity cash flows, comparable non-convertible market yield and relevant IFRS 9 measurement election.
- All other instruments/contracts affecting puttable residual returns, treasury shares and legally enforceable set-off rights.

## The method, step by step

### Section 2  -  Reference layer (Layer A): the classification rules

### The core principle  -  `IAS 32.15`–`16`

- **Substance over form classification**  -  On initial recognition the issuer classifies the instrument (or its component parts) as a financial liability, a financial asset, or equity, in accordance with the substance of the contractual arrangement and the IAS 32 definitions  -  not its legal form. The label on the certificate ("share", "bond", "note") does not decide the answer.  _(IAS 32.15)_
- **When a financial liability exists**  -  A financial liability exists when the instrument contains either: (1) A contractual obligation to deliver cash or another financial asset to another entity, or to exchange financial assets/financial liabilities with another entity under conditions that are potentially unfavourable to the issuer; or (2) A contract that will or may be settled in the entity's own equity instruments and is: a non-derivative for which the entity is or may be obliged to deliver a variable number of its own equity instruments; or a derivative that will or may be settled other than by exchanging a fixed amount of cash (or another financial asset) for a fixed number of the entity's own equity instruments  -  the "fixed-for-fixed" test.  _(IAS 32.11, .16(a), IAS 32.16(b))_
- **When an instrument is equity**  -  An instrument is equity if, and only if, both: It includes no contractual obligation to deliver cash or another financial asset, or to exchange under potentially unfavourable conditions; and if it will or may be settled in the entity's own equity, it is either a non-derivative that includes no obligation to deliver a variable number of own shares, or a derivative that will be settled only by exchanging a fixed amount of cash for a fixed number of own shares.  _(IAS 32.16(a)–(b))_

⚑ AUDIT FLASH POINT  -  substance over form on preference shares. A "preference share" is the textbook trap. Mandatory cash dividends create a liability component; a share with both liability and equity components requires separate classification (`IAS 32.28`, AG26). A cash-redemption obligation is assessed under .18(a), subject to the narrowly qualifying .16A-.16D exceptions. Returns on the liability component are recognised in profit or loss under .35-.40, even though the instrument is legally share capital. This moves amounts off equity and into profit or loss and changes leverage and EPS. Evidence the obligation analysis.

### The fixed-for-fixed test  -  `IAS 32.16(b)`, `.21`–`.24`

- **Fixed-for-fixed condition**  -  A contract settled in the entity's own equity is equity only if it exchanges a fixed amount of cash for a fixed number of the entity's own shares. The "fixed-for-fixed" condition fails  -  and the contract is a liability/derivative  -  where, for example: The number of shares to be delivered varies with the instrument's fair value or some other variable; the amount of cash to be received varies; Settlement is in a variable number of shares whose total value equals a fixed monetary amount (this is "shares as currency" → a liability); An issued put or forward obliges the entity to repurchase its own shares for cash → recognise a financial liability for the present value of the redemption amount, reclassified from equity.  _(IAS 32.16(b), .21–.24, IAS 32.21, IAS 32.20(b), IAS 32.23)_

⚑ AUDIT FLASH POINT  -  written put / forward on own shares. A contract obliging the entity to buy back its own shares for cash creates a liability for the present value of the redemption amount (`IAS 32.23`), even if the obligation is conditional and even though the underlying is the entity's own equity. The offsetting debit reduces equity. Reviewers must confirm the gross-settlement liability was recognised, not netted.

### Contingent settlement provisions  -  `IAS 32.25`

- **Contingent settlement provisions**  -  An instrument is a financial liability if settlement in cash (or another financial asset, or in a way that would otherwise be a liability) is contingent on uncertain future events outside the control of both the issuer and the holder  -  e.g. a change in a stock index, a consumer price index, interest rates, or the issuer's revenue/net income. Exceptions require .25(a)-(c): the cash-settlement contingency is not genuine (AG28: extremely rare, highly abnormal and very unlikely), settlement is required only on liquidation, or all .16A-.16B puttable-exception conditions are met.  _(IAS 32.25)_

### Settlement options  -  `IAS 32.26`–`27`

- **Settlement options with choice of method**  -  Where a derivative gives either party a choice of settlement method (cash vs. shares), it is a financial asset or financial liability unless all settlement alternatives would result in equity classification.  _(IAS 32.26–27)_

### The puttable-instruments exception  -  `IAS 32.16A`–`16D`

- **Puttable instrument equity exception conditions**  -  Some instruments meet the definition of a financial liability (because the holder can put them back for cash) yet are classified as equity by exception if all the conditions are met. A puttable instrument (16A–16B) is equity only if it: Entitles the holder to a pro rata share of net assets on liquidation; Is in the most subordinated class and all instruments in that class have identical features; Has no other contractual obligation to deliver cash/financial assets except the put; Has total expected cash flows based substantially on profit or loss, change in net assets, or change in fair value of the entity; and The issuer has no other instrument with terms that substantially fix or restrict the residual return to the puttable holders. A parallel exception (16C–16D) applies to instruments imposing an obligation only on liquidation that deliver a pro rata net-asset share. If the conditions later cease to be met, reclassify (16E–16F).  _(IAS 32.16A–16B, IAS 32.16C–16D, IAS 32.16E–16F)_

⚑ AUDIT FLASH POINT  -  puttable equity exception is narrow. The `16A`–`16D` exception is met by, e.g., open-ended fund units and some partnership/co-operative capital  -  but only if every condition holds. Failing one (e.g. a second class with a fixed return) tips the whole class into liability, which can wipe out reported equity. The US comparison remains a separate current-source request below.

### Section 3  -  Reference layer: compound instruments and special topics

### Compound (hybrid) instruments  -  split accounting  -  `IAS 32.28`–`32`

- **Split accounting method**  -  A non-derivative instrument that contains both a liability component and an equity component (the classic case: a convertible bond  -  debt plus a holder option to convert into a fixed number of shares) must be split on initial recognition. The method is prescribed: 1. Measure the liability component first, at the fair value of a similar liability without the conversion feature  -  i.e. the present value of the contractual cash flows (principal + coupons) discounted at the market rate for an equivalent non-convertible instrument. 2. Assign the residual (total issue proceeds minus the liability component) to the equity component (the conversion option). 3. The equity component is not remeasured subsequently. Subsequent liability measurement requires a separate IFRS 9 conclusion. The illustration assumes amortised cost with an effective-interest unwind; that assumption is not an IFRS 9 eligibility determination. 4. Transaction costs are allocated pro rata to the two components.  _(IAS 32.28–29, IAS 32.31–32, IAS 32.38)_

⚑ AUDIT FLASH POINT  -  the discount rate drives the split. The market rate for "similar non-convertible debt" is a significant estimate. A higher rate → a smaller liability and larger equity component → lower reported leverage but higher future interest expense. The rate must be evidenced (comparable issuances, credit spread, tenor). The current US comparison is reserved below rather than decided by this IAS 32 computation.

### Conversion, redemption, and amendment  -  `IAS 32.AG32`

- **Conversion and redemption treatment**  -  On conversion at maturity, derecognise the liability component and reclassify it to equity; no gain or loss arises. For early redemption/repurchase before maturity with the original conversion privileges unchanged, allocate consideration and transaction costs between liability and equity at the transaction date using the issuance-allocation method; the liability-component gain/loss goes to P&L and equity consideration to equity (AG33–AG34). For amended terms inducing early conversion, recognise the difference between the fair values of revised and original conversion consideration at the amendment date as a P&L loss (AG35). Other changed-term cases require separate analysis.  _(IAS 32.AG32, IAS 32.AG33–AG35)_

### Treasury shares  -  `IAS 32.33`–`34`

- **Treasury shares treatment**  -  An entity's reacquired own equity instruments ("treasury shares") are deducted from equity. No gain or loss is recognised in P&L on the purchase, sale, issue, or cancellation of own equity instruments; consideration paid or received is recognised directly in equity.  _(IAS 32.33)_

### Interest, dividends, gains, and losses  -  `IAS 32.35`–`36`

- **Distributions follow instrument classification**  -  Distributions and gains/losses follow the classification of the related instrument: Interest, dividends, losses and gains relating to a financial liability → profit or loss (e.g. "dividends" on redeemable preference shares are interest expense). Distributions to holders of an equity instrument → debited directly to equity. Related income tax follows IAS 12 under .35A; obtain that source before concluding the tax recognition or presentation. Transaction costs of an equity transaction → deducted from equity.  _(IAS 32.35, IAS 32.37)_

### Offsetting  -  `IAS 32.42`

The right must be currently enforceable in the normal course and on default/insolvency, not merely activated by a future event. A master netting agreement effective only on default is not enough; also document the net/simultaneous-settlement intention (.42-.50, AG38A-AG38F).

- **Offsetting conditions**  -  A financial asset and financial liability are offset (presented net) only when the entity (a) has a legally enforceable right to set off the recognised amounts and (b) intends either to settle net or to realise the asset and settle the liability simultaneously. Both conditions are mandatory.  _(IAS 32.42)_

### Preference shares  -  summary

**Preference shares  -  summary**

| Feature | Classification |
| --- | --- |
| **Mandatorily redeemable** for cash (fixed date/amount) | **Financial liability** (`IAS 32.18(a)`)  [Primary text](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| Redeemable **at the holder's option** | **Financial liability** (issuer cannot avoid cash outflow)  [Primary text](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) (IAS 32.18(a), .16A–.16D) |
| **Mandatory** (non-discretionary) dividends, non-redeemable | **Liability** for the dividend obligation (or compound)  [Primary text](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) (IAS 32.AG26) |
| **Discretionary** dividends, **non-redeemable** (issuer controls redemption) | **Equity** (`IAS 32.AG25`–`AG26`)  [Primary text](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| Redeemable **only at issuer's option** | **Equity only if** distributions are discretionary and all other terms avoid a liability obligation; exercising redemption can create an obligation (AG25–AG26)  [Primary text](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |

### Section 4  -  Executable layer (Layer B): the procedure

Run these steps on the instrument's facts. Each cites the Layer A rule it executes.

- **Step 1**  -  Read the contract for substance, not the label. List every settlement term, option, contingency, and redemption feature.  _(IAS 32.15)_
- **Step 2**  -  Apply the contractual-obligation test: is there any obligation to deliver cash/another financial asset, or to exchange under potentially unfavourable conditions, that the issuer cannot avoid? If yes → financial liability (in whole or part).  _(IAS 32.16(a))_
- **Step 3**  -  For own-equity settlement, apply the fixed-for-fixed test: fixed cash for fixed shares → equity; variable on either leg → liability/derivative.  _(IAS 32.16(b), .21–24)_
- **Step 4**  -  Check contingent settlement provisions: cash settlement contingent on an event outside both parties' control → liability, unless the .25(a)-(c) exceptions, including the fully qualifying puttable exception, apply.  _(IAS 32.25)_
- **Step 5**  -  Check the puttable / liquidation-only exceptions: if every condition is met, classify as equity by exception.  _(IAS 32.16A–16D)_
- **Step 6**  -  If the instrument is compound: measure the liability component at PV of cash flows at the market rate for similar non-convertible debt; assign the residual to equity; allocate transaction costs pro rata.  _(IAS 32.28–32)_
- **Step 7**  -  Book the journal entries (base §3 format) at initial recognition and over subsequent periods only after obtaining the applicable IFRS 9 measurement conclusion; the discount-unwind illustration assumes amortised cost. Apply the separate AG32–AG35 conversion/redemption/inducement conditions.
- **Step 8**  -  Classify distributions: liability → P&L; equity → directly in equity.  _(IAS 32.35)_
- **Step 9**  -  Assess offsetting only if both conditions are met.  _(IAS 32.42)_
- **Step 10**  -  Produce the disclosure checklist (§6, plus IFRS 7) and reviewer brief with every flash point.

### Section 5  -  Presentation

- **Presentation rules**  -  Liability components of issued instruments are presented within financial liabilities; current/non-current presentation requires the IAS 1 or early-adopted IFRS 18 handoff, reserved below. Equity components (e.g. the conversion option, the puttable-exception class) are presented within equity. Treasury shares are a deduction from equity, shown separately or in retained earnings/a treasury-share reserve. Distributions on liability-classified instruments are interest expense in P&L; distributions on equity instruments are movements within equity. Offset a financial asset and liability only where both IAS 32.42 conditions are met.  _(IAS 32.33, IAS 32.35–40, IAS 32.42, IAS 1)_

### Disclosure handoff

IAS 32.3 directs financial-instrument disclosures to IFRS 7. Apply the following scoped checklist to material information; it does not replace every applicable disclosure:

- Explain material instrument terms and their significance for financial position/performance, together with relevant risk exposures and management (.7, .31-.34). Coupon/dividend, maturity, conversion and put/call terms are transaction-specific inputs to that assessment.
- For an issued compound instrument with multiple embedded derivatives whose values are interdependent, disclose the existence of those features (.17). That paragraph does not independently require the full conversion-option/split/terms checklist for every compound instrument.
- For loans payable recognised at period end, disclose defaults during the period, the closing carrying amount in default and whether remedied or renegotiated before authorisation (.18). Other breaches permitting accelerated repayment require the same information unless remedied or renegotiated on or before period end (.19).
- The offsetting note covers both recognised instruments actually offset and instruments under enforceable master netting or similar arrangements even when not offset (.13A). Present gross assets/liabilities, amounts offset, net balance-sheet amounts, relevant other arrangement/collateral amounts and the residual net amount, separately by assets and liabilities; cap .13C(d) by .13C(c), explain rights and cross-refer split notes (.13B-.13F).
- Include the applicable effective-interest expense information for financial liabilities outside fair value through profit or loss (.20(b)); do not import the IFRS 18 presentation consequences into a period before that Standard applies (.44KK).
- When IFRS 18 is actually adopted, IFRS 7.19A requires the qualifying puttable-equity amount, repurchase-management objectives/policies/processes, expected redemption cash outflow and its determination; .19B requires amounts, timing and reasons for the specified liability/equity reclassifications. The .44KK adoption gate applies. The original `IAS 32.136A` citation was wrong; the pre-IFRS-18 IAS 1 disclosure route is individually reserved below.

### Section 8  -  Topic self-checks (in addition to base §7)

- [ ] Classification driven by **substance**, not legal form; each conclusion cites its `IAS 32` paragraph
- [ ] Contractual-obligation test applied (can the issuer avoid delivering cash/financial assets?) _(IAS 32.11, .16–.20)_
- [ ] Fixed-for-fixed test applied to any own-equity-settled contract; variability on either leg flagged _(IAS 32.16(b), .21–.24)_
- [ ] Contingent settlement provisions assessed (`IAS 32.25`); "not genuine" / "only on liquidation" exceptions documented
- [ ] Puttable / liquidation-only exception conditions tested **in full** (all conditions met, or not equity) _(IAS 32.16A–.16F, AG29A)_
- [ ] Compound instruments **split**: liability = PV at market rate for similar non-convertible debt; equity = residual; transaction costs allocated pro rata _(IAS 32.28–.32, .38)_
- [ ] Subsequent IFRS 9 measurement basis separately evidenced; amortised-cost unwind only when appropriate; maturity conversion/unchanged-privilege early redemption/inducement distinguished (AG32–AG35)
- [ ] Distributions classified per `IAS 32.35` (liability → P&L; equity → equity)
- [ ] Treasury shares deducted from equity, no P&L gain/loss _(IAS 32.33–.34, .33A)_
- [ ] Offsetting applied only where both `IAS 32.42` conditions met
- [ ] **Divergence from US GAAP** checked for dual-reporters (especially convertible split vs. single liability, and mezzanine equity)


### Conditions to retain beside a classification

Apply the puttable exception in full, not by analogy (.96B). AG29A excludes extending .16A–.16D equity-exception classification to NCI in consolidated financial statements: instruments qualifying in separate/individual accounts are liabilities when they are NCI in the consolidated group. The most-subordinated class must have no liquidation priority and need no conversion into another instrument to become that class; identical features include the put/redemption formula. Apart from the put, .16A(d) also excludes own-equity settlement that otherwise meets the liability definition. The .16B/.16D exclusion concerns another instrument or contract with both profit/net-asset-linked cash flows and a substantially fixed/restricted residual return; disregard the specified arm's-length-like non-financial holder contracts, and deny the exception if compliance cannot be determined. The instrument's own effects are excluded from the specified return tests. Do not import the .16A expected-return test into the separate .16C liquidation-only exception.

Fixed-for-fixed is subject to the pro-rata rights/options/warrants exception for a fixed amount of any currency offered to all existing holders of the same class (.11, .16(b)); own-equity for this purpose excludes .16A-.16D exception instruments and future-receipt/delivery contracts (.16, .22A). An issuer-only redemption option does not itself create a present obligation, but exercise can create one; discretionary dividends and all other terms still need assessment (AG25-AG26). Treasury-share deduction has the narrow instrument-by-instrument irrevocable exception for qualifying investment-fund/insurance underlying-item holdings (.33A); refer these facts rather than automatically deducting. Puttable reclassification is dated when conditions change: equity-to-liability uses fair value and an equity difference; liability-to-equity uses carrying amount (.16E-.16F). Gross written-put recognition is subject to the .16A-.16D exceptions (.23).

## Worked cases

All monetary amounts, rates and transaction dates below are illustrative supplied facts, not legal thresholds or prescribed yields. Keep the original whole-dollar journal displays separate from the cent-precision check.

### Worked example (illustrative)  -  convertible bond, IFRS split accounting

On 1 Jan 20X1 an entity issues a $1,000,000 par, 3-year, 5% annual-coupon convertible bond at par. Each bond is convertible at the holder's option into a fixed number of the entity's ordinary shares at maturity (fixed-for-fixed → conversion option is equity). The market rate for a similar non-convertible 3-year bond of this issuer is 8%. Coupons of $50,000 are paid annually in arrears; principal $1,000,000 repaid (or converted) at the end of 20X3.

**Step 1  -  Liability component = PV of cash flows at 8% (`IAS 32.31`)**  _(IAS 32.31)_

| Cash flow | Amount | PV factor @ 8% | Present value | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| --- | --- | --- | --- | --- |
| Coupon, end 20X1 | 50,000 | 0.92593 | 46,296 | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| Coupon, end 20X2 | 50,000 | 0.85734 | 42,867 | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| Coupon, end 20X3 | 50,000 | 0.79383 | 39,692 | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| Principal, end 20X3 | 1,000,000 | 0.79383 | 793,832 | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| **Liability component** |  |  | **922,687** | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |

- **Step 2  -  Equity component = residual**  -  $1,000,000 − $922,687 = $77,313  _(IAS 32.32)_

```
1 Jan 20X1  -  issue of convertible bond, split accounting  -  driving rule: IAS 32.28–32
  Dr  Cash                                       1,000,000
      Cr  Convertible bond  -  liability component        922,687
      Cr  Equity  -  conversion option (other equity)      77,313
  (memo: liability = PV of coupons+principal at the 8% market rate for similar
   non-convertible debt; equity = residual proceeds. Debits = credits ✓)
```

Illustration conditional on a separately established IFRS 9 amortised-cost measurement basis and no transaction costs: effective rate 8%. Coupon paid is 5% of par = $50,000; interest expense is 8% of the opening carrying amount; the difference accretes the liability toward par.

**Subsequent measurement  -  liability at amortised cost, effective rate 8%**

| Year | Opening | Interest @ 8% | Coupon paid | Closing | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| --- | --- | --- | --- | --- | --- |
| 20X1 | 922,687 | 73,815 | 50,000 | 946,502 | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| 20X2 | 946,502 | 75,720 | 50,000 | 972,222 | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |
| 20X3 | 972,222 | 77,778 | 50,000 | 1,000,000 | Derived from illustrative case inputs; [IAS 32.31-.32, AG31](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) |

```
31 Dec 20X1  -  accrue interest at effective rate, pay coupon  -  driving rule: IFRS 9 (amortised cost); IAS 32.35
  Dr  Interest expense (P&L)                         73,815
      Cr  Cash                                              50,000
      Cr  Convertible bond  -  liability component            23,815
  (memo: 8% × 922,687 = 73,815; coupon 5% × 1,000,000 = 50,000; accretion 23,815.
   Debits = credits ✓. Repeat each year on the table above.)
```

```
31 Dec 20X3  -  conversion at maturity (assume all converted)  -  driving rule: IAS 32.AG32
  Dr  Convertible bond  -  liability component       1,000,000
  Dr  Equity  -  conversion option                       77,313
      Cr  Share capital / share premium                  1,077,313
  (memo: liability at par on conversion + equity option reclassified to issued
   capital; NO gain or loss on conversion per AG32. Debits = credits ✓)
```

If the bonds were redeemed for cash at maturity instead, the liability component is settled at $1,000,000 and the $77,313 equity component remains in equity (may be transferred within equity); no P&L gain/loss arises if redeemed at par.

⚑ AUDIT FLASH POINT  -  dual-reporting handoff. The original US comparison remains an explicitly source-limited hypothesis: for the same $1,000,000 bond issued at par, assume the applicable US rule permits a single $1,000,000 liability with no equity component and $50,000 interest each year, with no bifurcated derivative, substantial premium, other separate right, issue costs or fair-value designation. Compare that proposed outcome with this IFRS case's $922,687 initial liability, $77,313 equity and 8% effective-interest profile. The US figures are not a cleared current-ASC conclusion; run the relevant edition and reconcile only after its authoritative-source gate is met.

```oa-check
name: Existing compound bond, liability first and equity residual
inputs:
  principal: 1000000
  coupon_rate: 0.05
  market_rate: 0.08
  proceeds: 1000000
steps:
  - coupon: principal * coupon_rate
  - pv_1: coupon / (1 + market_rate)
  - pv_2: coupon / ((1 + market_rate) * (1 + market_rate))
  - pv_3: (principal + coupon) / ((1 + market_rate) * (1 + market_rate) * (1 + market_rate))
  - liability: round(pv_1 + pv_2 + pv_3, 2)
  - equity: proceeds - liability
  - first_interest: round(liability * market_rate, 2)
  - first_closing: liability + first_interest - coupon
expected:
  liability: 922687.09
  equity: 77312.91
  first_interest: 73814.97
  first_closing: 946502.06
```

A second case uses the same qualifying compound instrument and $20,000 of incremental directly attributable issue costs. Allocate costs in proportion to proceeds: $18,453.74 to the liability and $1,546.26 to equity (IAS 32.38). Initial net liability is $904,233.35 and net equity $75,766.65. The original 8% yield must not simply be reused after netting liability costs; the subsequent effective yield requires a separate IFRS 9 computation, reserved below.

```oa-check
name: Compound issue costs allocated to both components
inputs:
  gross_liability: 922687.09
  gross_equity: 77312.91
  proceeds: 1000000
  costs: 20000
steps:
  - liability_costs: round(costs * gross_liability / proceeds, 2)
  - equity_costs: costs - liability_costs
  - net_liability: gross_liability - liability_costs
  - net_equity: gross_equity - equity_costs
expected:
  liability_costs: 18453.74
  equity_costs: 1546.26
  net_liability: 904233.35
  net_equity: 75766.65
```

## When to refuse or refer

Refuse a final recognition, classification, valuation or disclosure conclusion when required contracts, applicable reporting period, adoption facts or supporting standards are missing. Refer significant valuations, enforceability, control, impairment and complex settlement terms to a qualified reporting specialist. Return the facts, paragraph-by-paragraph reasoning, balanced journals, reconciliation and open items to the reviewer. Do not issue audit or assurance language. Any topic reserved below remains outside usable instructions until its operative primary source is recovered.


### Original professional disclaimer

Provides computational and interpretive guidance on IAS 32 (with IFRS 9 for liability measurement) only. Not an audit and not assurance. Classifying instruments as liabilities or equity turns heavily on the specific contractual terms and significant judgement. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

## Sources

| Source | Official URL | Actual read scope and date |
|---|---|---|
| IAS 32 Financial Instruments: Presentation | [IAS 32 Financial Instruments: Presentation](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html) | Read for .2-.50, .96-.97U, AG25-AG35 and AG38A-AG38F in the official 2026-issued copy retrieved 2026-11-14, personally read 2026-11-15; official body retrieved again and reconciled 2026-11-16; existing read scope retained |
| IFRS 7 disclosure clauses | [IFRS 7](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs7.html) | Read 2026-11-16: .3-.8, .13A-.13F, .17-.21, .31-.34, .44KK, B40-B41 and neighbors; issued-copy IFRS 18 consequences gated. |
| IFRS 9 liability measurement | [IFRS 9](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html) | Read 2026-11-16: .4.2.1-.2, .4.3.1-.7, .5.1.1-.3, .5.3.1-.2, Appendix A effective-interest definitions, B5.4.1-.6 and .7.1.1-.2; selected liability scope, not full financial-instrument clearance. |
| Supporting IAS 1 | [IAS 1 attempted official path](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias1.html) | Attempted 2026-11-16: 2026/2025 paths returned 404; 2024 path redirected to premium landing, not the Standard. Not read; individual limits below. |
| Current US comparison | [Authoritative ASC](https://asc.fasb.org/) | Attempted again 2026-11-16; official ASC web pages returned 0 readable lines. Current operative Codification not read; historical recovery limits are preserved in external evidence. |

Not yet confirmed: IAS 12 income-tax effects under .35A require primary-source recovery; no automatic tax benefit or equity treatment is established here.  jurisdiction-specific endorsement and entity-specific early adoption; all individually retained source-limited items below. These boundaries are not accountant approval.

#### Not yet confirmed: individual pre-IFRS-18 presentation and disclosure routes

The 2026 and 2025 official IAS 1 HTML paths returned 404; the 2024 path redirected to the IFRS premium landing page on 16 November 2026, not operative IAS 1. These specific current-period requirements therefore remain source-limited, rather than being treated as verified by the IFRS 18 relocation:

| Original topic | Unresolved source-dependent requirement |
| --- | --- |
| Accounting policy | Current-period material policy wording and the applicable IAS 1 paragraph; IFRS 7.21 in the issued copy has an IFRS 18-dependent IAS 8 reference (.44KK). |
| Puttable-equity amount | Pre-IFRS-18 IAS 1.136A summary quantitative disclosure; not `IAS 32.136A`. |
| Puttable repurchase management | Pre-IFRS-18 objectives/policies/processes and changes, including management of the obligation. |
| Puttable expected cash flow | Pre-IFRS-18 expected redemption/repurchase cash outflow and how it is determined. |
| Puttable/liquidation-only reclassification | Pre-IFRS-18 IAS 1.80A amount, timing and reason route; do not use future IFRS 7.19B without adoption. |
| Treasury-share amount | Current-period presentation/disclosure of the amount and retained-earnings/reserve caption under the applicable presentation basis. The IAS 32.33 deduction rule is separately supported above. |
| Current/non-current presentation | Apply the entity's actual IAS 1 or adopted IFRS 18 framework; this file does not clear the detailed maturity/covenant classification. |

#### Not yet confirmed: individual current US comparisons

Official ASC web recovery on 16 November 2026 returned no readable operative paragraphs. Each comparison below needs current authoritative ASC support before use; the IFRS analysis above remains independently bounded.

| Original comparison topic | Reserved US-dependent conclusion |
| --- | --- |
| Convertible bonds | Current single-liability versus component-split outcome, including the ASU 2020-06 substantial-premium and embedded-derivative exceptions. |
| Temporary equity | SEC-specific redeemable preferred/NCI presentation under ASC 480-10-S99-3A; do not infer a universal intermediate category. |
| Own-equity settlement | Current ASC 815-40 indexation and foreign-currency exceptions versus IAS 32 fixed-for-fixed and its own exceptions. |
| Puttable instruments | Current liability, temporary-equity or equity outcome under the applicable ASC scope; no categorical US no-exception conclusion. |
| Mandatorily redeemable instruments | ASC 480 scope, freestanding/embedded and timing/condition differences. |
| Liability-classified dividends | US income-statement and EPS mechanics; IFRS treatment is stated above. |

#### IFRS 9 measurement boundary

The recovered IFRS 9.4.2.1-.2, .4.3.3-.5, .5.1.1-.1A, .5.3.1-.2 and Appendix A/B5.4.1-.6 support a separate liability-measurement assessment, not a blanket amortised-cost result. Consider fair-value-through-profit-or-loss categories/designations, embedded derivatives and the other .4.2.1 exceptions. Directly attributable liability issue costs affect initial measurement outside fair value through profit or loss; effective-interest calculations include relevant fees, transaction costs, premiums and discounts. The bond examples remain conditional on the documented amortised-cost basis, unmodified contractual cash flows and their stated costs. A separately sourced IFRS 9 conclusion is still needed for an actual instrument with additional features.
