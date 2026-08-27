---
name: us-foreign-trust-reporting
description: "US taxation and reporting of foreign trusts for US persons: the court/control tests (IRC §7701), grantor-trust ownership under §671–679 (especially §679), the throwback / accumulation-distribution regime (§665–668) and its interest charge, and Forms 3520 and 3520-A with their penalties. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
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

# US Foreign Trust Reporting

## What this file is

This is a **topic content skill**. It loads on top of `cross-border-tax-workflow-base` and assumes the **cross-border-tax-router has already run** and sequenced the engagement. It carries the US foreign-trust rules only; the workflow architecture, intake map, sequenced-plan contract, and mandatory human hand-off live in the base.

**Characterize the trust FIRST.** Before any distribution is taxed, any gain on a sale is computed, or any form is selected, this skill determines (1) whether the trust is *foreign*, and (2) whether it is a *grantor* (owned) or *non-grantor* trust as to the US person. Every downstream number depends on that answer. A distribution from a grantor trust the US person already owns is not a taxable distribution at all; the same cash from a non-grantor trust can carry throwback tax plus an interest charge. Do not compute the consequence before you have fixed the character.

**Currency.** Provisions cited are current US federal law (IRC + Forms 3520 / 3520-A). Penalty *amounts* below are the long-standing statutory figures; confirm current indexing and any active penalty-relief procedure for the filing year.

This output is a **working paper**, never a filed return. Foreign-trust positions carry some of the highest penalty exposure in the Code (§6677, §6048). The foreign-country (e.g. Australian) treatment is **out of scope** and is deferred to a local accountant — see the flash points.

## Layer A — Reference layer

### A1. Is the trust FOREIGN? (the two "courts" tests)

- **Foreign vs domestic trust determination** — A trust is a **US (domestic) trust only if it passes BOTH** of the following. Fail either one and it is a **foreign trust**. COURT TEST: A court within the US is able to exercise primary supervision over the administration of the trust? NO → FOREIGN TRUST. YES → proceed to control test. CONTROL TEST: One or more US persons have authority to control all substantial decisions of the trust? NO → FOREIGN TRUST. YES → DOMESTIC TRUST. "All substantial decisions" is read strictly (distributions, who can benefit, investment, removal/replacement of trustee, termination, litigation). A single substantial decision controlled by a non-US person taints the control test. A foreign trustee, foreign situs, or foreign-law governing instrument typically fails the court test. **Conservative default:** if either test is not clearly met on the documents, treat the trust as **FOREIGN** and proceed under this skill.  _(IRC §7701(a)(30)(E), §7701(a)(31)(B); §7701(a)(30)(E)(i) court test; §7701(a)(30)(E)(ii) control test)_

### A2. GRANTOR vs NON-GRANTOR (is a US person the OWNER?) — §671–679

- **Grantor vs non-grantor determination** — If a US person is treated as the **owner** of all or part of the trust under the grantor-trust rules, that person is taxed **currently** on the trust's income (income, deductions, credits flow through — §671), regardless of whether anything is distributed. Run these in order: §673–678 ordinary grantor-trust triggers: Retained reversion, power to control beneficial enjoyment, certain administrative powers, revocability, retained income interest, or a power held by a person to vest corpus/income in himself? YES → US person is OWNER of that portion (GRANTOR TRUST). NO → proceed to §679. §679 — the foreign-trust-specific owner rule (the decisive one offshore): A US person (directly or indirectly) TRANSFERRED property to a FOREIGN trust that has (or may have) a US BENEFICIARY? YES → US transferor is treated as OWNER of the transferred portion → GRANTOR TRUST as to that US person. NO → NON-GRANTOR FOREIGN TRUST (throwback regime applies to US-beneficiary distributions — see A3). §679 notes: - The "US beneficiary" condition is read broadly: if **any** trust terms could permit a US person to benefit, or amounts could be accumulated for a future US beneficiary, the condition is generally treated as met. - §679 can apply to transfers made *before* the transferor became a US person but within the look-back window tied to US residency (the 5-year pre-residency rule) — flag any transfer near an immigration date. - A transfer for full fair-market-value consideration is generally outside §679; a gratuitous or below-value transfer is in.  _(IRC §671; §673–678; §679)_

### A3. NON-GRANTOR foreign trust → US-beneficiary DISTRIBUTIONS: throwback (§665–668)

- **Throwback / accumulation-distribution regime** — A US person who is a beneficiary (not owner) of a foreign non-grantor trust is taxed on distributions under the **throwback / accumulation-distribution regime**: - **DNI first.** A current-year distribution carries out distributable net income (DNI) and is taxed to the beneficiary at ordinary rates (character preserved). - **UNI / accumulation distribution (§665).** Income a foreign trust **earned in a prior year but did not distribute** becomes **undistributed net income (UNI)**. A distribution exceeding current DNI is an **accumulation distribution** that pulls UNI out of prior years ("throwback"). - **Throwback tax (§666–667).** The thrown-back UNI is taxed as if received in the earlier years (averaging mechanics), and — critically — **long-term capital gains accumulated in a foreign trust lose their preferential character** and come out as ordinary income. - **§668 interest charge.** A non-deductible **interest charge** is imposed on the deferred tax, compounding for **every year the income sat undistributed**. For a trust that accumulated for decades, the interest charge alone can approach or exceed the distribution — this is why long-accumulating foreign trusts are punitive to US beneficiaries.  _(IRC §665; §666–667; §668)_
- **Default method vs actual method** — **Actual (exact) method** — requires the trust's complete year-by-year DNI/UNI records to allocate UNI to specific accumulation years; usually the lower number, but needs reliable historical accounting. **Default method (Form 3520 instructions)** — used when the year-by-year history is unavailable. It synthesizes an average accumulation period and applies the highest rate, generally producing a **higher** tax and interest charge. **Conservative default:** if the trust cannot produce reliable year-by-year UNI records, assume the **default method** applies and flag the UNI exposure as material and probably understated by any back-of-envelope estimate.  _(Form 3520 instructions)_

### A4. Reporting forms

**Reporting forms table**  _(§6048(a)/(c); §6048(b))_

| Form | Who / when | Covers |
| --- | --- | --- |
| **Form 3520** (§6048(a)/(c)) | The US person | Transfers TO a foreign trust; distributions FROM a foreign trust; ownership of a foreign trust; AND large gifts/bequests from foreign persons/estates. |
| **Form 3520-A** (§6048(b)) | The foreign trust (the **US owner** is responsible for ensuring it is filed; owner files a substitute if the trust will not) | Annual information return of a foreign trust **with a US owner** — income statement, balance sheet, and Foreign Grantor Trust Owner/Beneficiary statements to the US persons. |

- **Form 3520 penalty** — Greater of $10,000 or 35% USD or percent of gross value (of the gross value of the property transferred / distribution received (5% for failure to report ownership), per failure)  _(§6677)_
- **Form 3520-A penalty** — Greater of $10,000 or 5% USD or percent of gross value (of the gross value of the trust's assets treated as owned by the US person, per month of non-compliance)  _(§6677)_
- **Large foreign gift/bequest under-reporting penalty** — 5% per month (capped) percent per month (separate penalty for under-reporting large foreign gifts/bequests)  _(§6677)_
- **Reasonable cause defense** — **Reasonable cause** is a defense (§6677(d)); recent IRS practice has moved toward **first-time-abatement-style relief** and away from automatic systemic assessment on late-filed 3520/3520-A — confirm the current procedure and assert reasonable cause affirmatively where the facts support it.  _(§6677(d))_

## Layer B — Executable layer (trust facts → owner → treatment → forms)

Run top to bottom. Stop and flag at any unknown — do not assume favorably.

1. **Gather trust facts.** Instrument, governing law, situs, trustee nationality/residence, who controls each substantial decision, settlor, beneficiary class, funding history (who transferred what, when, for what consideration), and year-by-year income/distribution records if any.
2. **FOREIGN test (A1).** Apply court + control. If either fails → foreign. If either is unclear → treat as foreign.
3. **OWNER test (A2).** Apply §673–678, then **§679**. Decide grantor vs non-grantor **as to each relevant US person**. A trust can be a grantor trust as to one US person and not another.
4. **Branch:**
   - **Grantor (US owner):** trust income is reported on the **owner's** US return currently (Schedule B / relevant schedules). File **Form 3520-A** (or substitute) and **Form 3520**. Distributions to the owner are generally **non-taxable returns of owned assets** — characterize the trust before calling any cash a "distribution."
   - **Non-grantor + US-beneficiary distribution:** compute DNI; identify any accumulation distribution; run throwback (A3) under actual method if records allow, else default method; add the **§668 interest charge**. Report on **Form 3520**.
   - **No US owner, no distribution this year:** report transfers/ownership as applicable on **Form 3520**; UNI continues to accrue silently — note future exposure.
5. **SALE overlay (see flash point).** Determine the **tax owner at the moment of sale** from step 3, *before* computing gain. Grantor analysis first: if a US person owns the trust under §679, gain on the trust selling an asset is **that US person's gain currently**. If non-grantor, gain stays in the trust, swells DNI/UNI, and is taxed to a US beneficiary only on distribution (with throwback on any accumulated portion).
6. **Residency overlay.** If the US person's status is changing (expatriation, becoming/ceasing to be a US person), the **router's sequencing rule** governs order of operations and you must **cross-reference `us-expatriation-exit-tax`** — a §877A mark-to-market and the §679 ownership question can collide.
7. **Assemble working paper + reviewer brief** per the base contract.

## Audit flash points

⚑ AUDIT FLASH POINT — §679 deemed ownership. A US person who transferred property to a foreign trust that *could* benefit any US person is treated as the **owner** even with no distribution and no retained control. Check funding history and any transfer within the pre-residency window. Missing this turns a "non-grantor" analysis into a current-tax-and-3520-A filing obligation.

⚑ AUDIT FLASH POINT — throwback interest on long-accumulated UNI. For a foreign non-grantor trust that accumulated income for many years, the **§668 interest charge** compounds across every accumulation year and capital gains lose their character. The interest can rival the distribution itself. If year-by-year records are missing, assume the **default method** and treat the exposure as large and under-estimated.

⚑ AUDIT FLASH POINT — 3520 / 3520-A penalties and reasonable cause. Penalties run to **35%** (3520) and **5%/month** (3520-A) of trust value. File on time; if late, assert **reasonable cause (§6677(d))** affirmatively and check the current IRS penalty-relief / first-time-abatement posture before assuming an automatic penalty.

⚑ AUDIT FLASH POINT — US vs foreign characterization mismatch. A trust the US treats as a foreign **non-grantor** trust may be treated entirely differently abroad. **Australian discretionary and unit trusts** are common and are **typically foreign non-grantor trusts to the US unless §679 applies** — but their Australian treatment (e.g. trust distributions, CGT, present entitlement) does **not** track the US analysis. The two systems can each tax the same economics differently and double-tax relief is not automatic. The Australian side **requires a local accountant** — do not opine on it.

⚑ AUDIT FLASH POINT — selling trust assets vs distributing then selling: order matters. Whether the trust sells the asset (gain lands in the trust → DNI/UNI → throwback to a US beneficiary later) or distributes the asset first and the US person sells (gain on the beneficiary's own return, possibly with stepped basis questions) produces **materially different US tax**. Fix the **tax owner at the instant of sale** under the §679/grantor analysis **before** modelling the sale, and sequence per the router.

## Topic self-checks

- [ ] Court test AND control test both applied; foreign/domestic conclusion stated (defaulted to FOREIGN where unclear).
- [ ] §673–678 screened, then **§679** screened against full funding history and any pre-residency transfers; grantor vs non-grantor fixed **per US person**.
- [ ] If grantor: owner's current income inclusion handled; **3520-A** (or substitute) and **3520** identified.
- [ ] If non-grantor distribution: DNI vs accumulation distribution computed; throwback run; **§668 interest charge** included; actual vs **default** method chosen and justified.
- [ ] UNI / records availability assessed; default method assumed where history missing.
- [ ] **Form 3520** transfer/distribution/gift items captured; penalties and reasonable-cause posture noted.
- [ ] **Sale overlay:** tax owner at moment of sale fixed before any gain computed.
- [ ] **Residency overlay:** `us-expatriation-exit-tax` cross-referenced and router sequencing applied where status is changing.
- [ ] Australian (or other foreign-country) treatment **explicitly deferred** to a local accountant.
- [ ] Output labelled a working paper; no human sign-off claimed.

## Disclaimer

Provides computational and interpretive guidance on US foreign-trust taxation and Forms 3520/3520-A only. Not tax or legal advice and not a filed return. Trust characterization and throwback turn on the trust instrument and history and require professional judgement; the foreign-country treatment requires a local accountant. Have outputs reviewed and signed by a qualified, licensed accountant before acting. Research-verified (tier 2) pending credentialed sign-off.

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
