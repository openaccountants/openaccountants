---
name: us-expatriation-exit-tax
description: "US expatriation tax for citizens renouncing and long-term green-card holders abandoning status: the covered-expatriate tests (IRC §877A/§877), the mark-to-market exit tax, the special rules for deferred compensation, tax-deferred accounts and non-grantor trust interests, the dual-citizen and minor exceptions, Form 8854, and the §2801 tax on US recipients of gifts from covered expatriates. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
version: 0.1
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
depends_on:
  - cross-border-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Expatriation Exit Tax

## What this file is

This is a topic content skill that **loads on top of `cross-border-tax-workflow-base`** and assumes the **`cross-border-tax-router`** has already run its Step 0 residency map and routed the situation here. It carries the substantive US rules for two populations who sever the US tax net:

1. a **US citizen who renounces** citizenship, and
2. a **long-term resident (LTR)** — a lawful permanent resident (green-card holder) for at least **8 of the prior 15 tax years** under **§877(e)(2)** — who **abandons** that status or is treated as a resident of a treaty country.

It produces a working paper and reviewer brief; it never produces a filed return, and no human has signed off on its output until `request_accountant_review` returns a credentialed sign-off.

**Sequencing — fix the exit-tax test and date FIRST.** Per the `cross-border-tax-router` sequencing rule, the **covered-expatriate determination and the expatriation date must be fixed before any post-expatriation disposal is planned**. Expatriation triggers a **deemed sale of all worldwide property** the day before the expatriation date (§877A(a)), which **resets basis** and changes the timing of every later transaction. Planning a disposal before pinning the date produces wrong basis and wrong gain. Do the test and the date, then plan.

**Currency.** The **net-worth $2,000,000 test threshold is fixed by statute** and not indexed. Two figures **are** inflation-indexed and change every year — the **average-annual-net-income-tax threshold** and the **net-gain exclusion amount** for the mark-to-market tax. This file never hardcodes a current figure as authoritative; it instructs the agent to **confirm the current-year value** from the Form 8854 instructions / the relevant Rev. Proc. inflation-adjustment release before computing.

## Layer A — Reference layer (the rules)

### A.1 — Who is an "expatriate" (IRC §877A(g)(2), §877(e))

- **Expatriate** — An expatriate is (a) a US citizen who relinquishes citizenship, or (b) an LTR who ceases to be a lawful permanent resident. The expatriation regime of §877A only bites where the expatriate is also a covered expatriate. Non-LTR green-card holders and ordinary non-resident aliens are out of scope.  _(IRC §877A(g)(2), §877(e))_

### A.2 — Covered-expatriate decision tree (IRC §877A(g)(1), §877(a)(2))

- **Covered-expatriate tests — any one triggers covered status** — An expatriate is a covered expatriate if they meet ANY ONE of the three independent tests below (subject to the limited exceptions in A.4): 1) Net-worth test — §877(a)(2)(B): Worldwide net worth is ≥ $2,000,000 on the expatriation date. This threshold is fixed (not indexed). Net worth is computed on a fair-market-value balance-sheet basis. 2) Net-income-tax test — §877(a)(2)(A): The average annual net US income tax for the 5 tax years ending before the expatriation date exceeds an inflation-indexed threshold. Confirm the current-year figure from the Form 8854 instructions before applying it — it has been in roughly the $190k–$200k range in recent years, but treat any number here as confirm current year, not authoritative. 3) Certification test — §877(a)(2)(C): The expatriate fails to certify, on Form 8854, under penalties of perjury, full compliance with all US federal tax obligations for the 5 tax years preceding expatriation (and to attach evidence of compliance if requested). Failure to certify makes the person a covered expatriate regardless of net worth or income. Meeting any one test ⇒ covered. The three are tested independently; a person under the net-worth and income thresholds is still covered if they cannot certify on Form 8854.  _(IRC §877A(g)(1), §877(a)(2))_
- **Net-worth test threshold** — 2000000 USD (fixed, not indexed)  _(§877(a)(2)(B))_
- **Average annual net US income tax threshold (5-year test)** — inflation-indexed; roughly $190k–$200k in recent years — confirm current-year figure from Form 8854 instructions USD (confirm current year)  _(§877(a)(2)(A))_

### A.3 — Mark-to-market "exit tax" mechanics (IRC §877A(a), (b))

- **Deemed sale on expatriation** — A covered expatriate is treated as having sold all property they own (with limited exceptions for the special-regime assets in A.5) at fair market value on the day before the expatriation date (§877A(a)(1)).  _(IRC §877A(a)(1))_
- **Net gain recognition and exclusion** — Net gain from the deemed sale is recognized; net gain above an inflation-indexed exclusion amount is taxed (§877A(a)(3)). Confirm the current-year exclusion from the Form 8854 instructions / Rev. Proc. — it has been above ~$800k in recent years; treat as confirm current year. The exclusion amount is allocated pro rata across the assets with built-in gain.  _(IRC §877A(a)(3))_
- **Net-gain exclusion amount** — inflation-indexed; above ~$800k in recent years — confirm current year USD (confirm current year)  _(§877A(a)(3))_
- **Losses and wash-sale rules** — Losses are taken into account (and wash-sale rules under §1091 apply), but the exclusion only shelters net gain, not loss.  _(IRC §1091)_
- **Deferral election** — An irrevocable election to defer the mark-to-market tax on a per-asset basis is available under §877A(b) — but it requires adequate security (e.g. a bond), a waiver of treaty rights to the assessment, and interest accrues until paid. Note it; do not assume it.  _(IRC §877A(b))_

### A.4 — Exceptions to covered status (IRC §877A(g)(1)(B))

- **Two exceptions to covered status** — Two exceptions can keep an expatriate out of covered status even if they breach the net-worth or income test — but BOTH still require filing Form 8854 and certifying 5 years of compliance (the certification test is never waived): 1) Dual-citizen-at-birth exception — §877A(g)(1)(B)(i): The person (a) became a US citizen and a citizen of another country at birth and, as of the expatriation date, continues to be a citizen of, and taxed as a resident of, that other country, AND (b) was a US resident for not more than 10 of the 15 tax years ending with the expatriation year. 2) Minor-expatriate exception — §877A(g)(1)(B)(ii): The person relinquished US citizenship before age 18½ and was a US resident for not more than 10 tax years before relinquishment. If an exception applies, the person can still certify on Form 8854 and avoid covered status; if they cannot certify, the certification test makes them covered regardless of the exception.  _(IRC §877A(g)(1)(B))_

### A.5 — Special asset regimes (IRC §877A(c)–(f))

- **Eligible deferred compensation** — If the payer is a US person (or a non-US payer that elects to be treated as one) and the covered expatriate irrevocably waives treaty withholding-reduction rights, the item is "eligible": it is not marked to market; instead 30% withholding applies to future taxable payments.  _(IRC §877A(d)(1))_
- **Ineligible deferred compensation** — Where the eligibility conditions are not met, the covered expatriate is treated as receiving a deemed lump-sum distribution of the present value of the accrued benefit on the day before expatriation — taxed up front.  _(IRC §877A(d)(2))_
- **Specified tax-deferred accounts** — IRAs, §529 plans, Coverdell ESAs, health/medical savings accounts, etc. are treated as receiving a deemed full distribution of the entire account on the day before expatriation (income tax applies; the 10% early-distribution additional tax does not).  _(IRC §877A(e))_
- **Interests in non-grantor trusts** — A covered expatriate's beneficial interest in a non-grantor trust is not marked to market. Instead, the trustee withholds 30% of the taxable portion of each direct or indirect distribution to the covered expatriate. Cross-reference `us-foreign-trust-reporting` for the trust classification (grantor vs non-grantor) and the reporting that surrounds it.  _(IRC §877A(f))_
- **Withholding rate on eligible deferred comp / non-grantor trust distributions** — 30 %  _(IRC §877A(d)(1), §877A(f))_

### A.6 — §2801 transfer tax on US recipients (high level)

- **§2801 transfer tax on US recipients** — Separate from the exit tax, IRC §2801 imposes a transfer tax on the US citizen or resident recipient of a "covered gift or bequest" received from a covered expatriate — at the highest gift/estate-tax rate, on amounts above the annual exclusion. This is a distinct transfer-tax regime that follows the covered expatriate indefinitely and burdens the recipient, not the expatriate. Flag it at a high level when a covered-expatriate determination is positive; do not compute it in this file.  _(IRC §2801)_

## Layer B — Executable layer (the procedure)

Work the steps in order. Do not plan disposals before Step 4 is fixed.

## B.1 — Confirm status and dates.

- **B.1 — Confirm status and dates** — Determine whether the person is a renouncing citizen or an LTR (8-of-15-years test, §877(e)(2)). Fix the expatriation date (date of the consular renunciation / CLN, or the date LPR status was abandoned or treaty-residence began). Record it; everything keys off the day before this date.  _(§877(e)(2))_

## B.2 — Build the FMV net-worth balance sheet.

- **B.2 — Build the FMV net-worth balance sheet** — Schedule all worldwide assets at fair market value less liabilities: real property, business interests, publicly traded and private securities, pension and deferred-comp present values, vested and unvested options/RSUs, IRAs and other tax-deferred accounts, and beneficial interests in trusts. Compare to the $2,000,000 fixed threshold.  _(§877(a)(2)(B))_

## B.3 — Compute the 5-year average net income tax.

- **B.3 — Compute the 5-year average net income tax** — Pull the net US income tax from the 5 returns ending before the expatriation year, average them, and compare to the current-year indexed threshold (confirm current year).  _(§877(a)(2)(A))_

## B.4 — Determine covered status.

- **B.4 — Determine covered status** — Apply the A.2 tree: net-worth OR income OR certification-failure ⇒ covered. Apply the A.4 exceptions (dual-citizen / minor) only to the net-worth and income tests, never to certification. Record which test(s) are met and why.  _(§877A(g)(1), §877(a)(2))_

## B.5 — If covered, compute the exit tax.

- **B.5 — If covered, compute the exit tax** — Mark all non-special-regime property to market (FMV day-before less basis), net the gains and losses, subtract the indexed net-gain exclusion (confirm current year), and apply the relevant capital-gain / ordinary rates. Apply the §877A(b) deferral election only if security and a treaty waiver are in place. Separately run the special regimes (A.5): ineligible deferred comp and tax-deferred accounts as deemed distributions; eligible deferred comp and non-grantor-trust interests as 30% future-payment withholding.  _(§877A(a), (b), (d), (e), (f))_

## B.6 — Prepare Form 8854.

- **B.6 — Prepare Form 8854** — Complete Form 8854 (Initial and Annual Expatriation Statement) to establish the expatriation date and certify 5 years of compliance. Remember: non-filing or non-certification of Form 8854 is itself the certification test failing, which makes the person covered regardless of B.2/B.3. Note any annual Form 8854 obligations (e.g. while a deferral election is outstanding).  _(Form 8854; §877(a)(2)(C))_

## B.7 — Flag §2801 exposure.

- **B.7 — Flag §2801 exposure** — If covered, note in the reviewer brief that future gifts/bequests from this person to US persons fall under the §2801 recipient transfer-tax regime.  _(IRC §2801)_

## B.8 — Assemble working paper + reviewer brief

- **B.8 — Assemble working paper + reviewer brief** — Assemble working paper + reviewer brief and route to request_accountant_review. Mark every indexed figure as confirm current year.

## ⚑ AUDIT FLASH POINT — net-worth valuation is broader than people expect.

The $2M net-worth test is computed at fair market value and includes pension and deferred-compensation present values, vested and unvested equity (options/RSUs), IRAs and other tax-deferred accounts, and beneficial interests in trusts (including hard-to-value non-grantor-trust interests). Omitting illiquid or "not really mine yet" assets is the classic understatement that flips a determination. Value conservatively and document the method.

## ⚑ AUDIT FLASH POINT — the certification trap (§877(a)(2)(C)).

Non-filing or non-certification of Form 8854 makes the person a covered expatriate regardless of net worth or income tax. A person well under the $2M and income thresholds is still covered if they cannot certify 5 clean years. The dual-citizen and minor exceptions do not waive certification. Never conclude "not covered" without confirming a valid Form 8854 certification.

## ⚑ AUDIT FLASH POINT — deferred comp and IRA deemed distribution (§877A(d), (e)).

Ineligible deferred compensation is a deemed lump-sum distribution of present value, and specified tax-deferred accounts (IRAs, §529, Coverdell, HSA/MSA) are a deemed full distribution — both taxed up front, not marked to market. The 10% early-distribution additional tax does not apply to the §877A(e) deemed distribution. Do not fold these into the mark-to-market gain pool.

## ⚑ AUDIT FLASH POINT — non-grantor-trust 30% withholding (§877A(f)).

A covered expatriate's interest in a non-grantor trust is not marked to market; instead the trustee withholds 30% of the taxable portion of each distribution to the covered expatriate, indefinitely. Confirm the trust's grantor/non-grantor classification with us-foreign-trust-reporting before applying either treatment — getting the classification wrong changes the entire mechanism.

## ⚑ AUDIT FLASH POINT — dual-citizen exception conditions (§877A(g)(1)(B)(i)).

The exception applies only if the person became a US and foreign citizen at birth, remains a citizen of and taxed as a resident of that other country on the expatriation date, AND was a US resident for no more than 10 of the 15 tax years ending with the expatriation year. All conditions must hold, and Form 8854 certification is still required. Naturalized citizens and acquired-later dual citizens do not qualify.

## Topic self-checks

- [ ] Is the person a renouncing **citizen** or an **LTR** (8-of-15-years, §877(e)(2))? Expatriation date fixed and recorded?
- [ ] Was the **exit-tax test and date fixed BEFORE** any post-expatriation disposal was planned (router sequencing rule)?
- [ ] FMV net-worth balance sheet built, **including** pensions, options, IRAs and **trust interests**? Compared to the **fixed $2,000,000** threshold?
- [ ] 5-year average net income tax computed and compared to the **indexed threshold** — figure marked *confirm current year*?
- [ ] **Form 8854 certification** confirmed? (Non-certification = covered, regardless of net worth/income.)
- [ ] Covered status concluded under the A.2 tree, with the dual-citizen / minor exceptions applied **only** to net-worth/income, never to certification?
- [ ] Mark-to-market gain computed with the **indexed net-gain exclusion** marked *confirm current year*? Loss and §1091 wash-sale rules considered?
- [ ] Special regimes run separately — ineligible deferred comp and tax-deferred accounts as **deemed distributions**; eligible deferred comp and non-grantor-trust interests as **30% withholding** (§877A(d)–(f))?
- [ ] **§877A(b)** deferral election only assumed where security + treaty waiver exist?
- [ ] **§2801** recipient transfer-tax exposure flagged in the reviewer brief?
- [ ] `us-foreign-trust-reporting` cross-referenced for any trust interest?
- [ ] All indexed figures marked *confirm current year*; no invented citations; no claim that a human has signed off?

## Disclaimer

Provides computational and interpretive guidance on IRC §877A/§877 expatriation and Form 8854 only. Not tax or legal advice and not a filed return. Covered-expatriate status, asset valuation, and the exit-tax computation turn on entity-specific facts and significant judgement. Have outputs reviewed and signed by a qualified, licensed accountant before acting. Research-verified (tier 2) pending credentialed sign-off.

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
