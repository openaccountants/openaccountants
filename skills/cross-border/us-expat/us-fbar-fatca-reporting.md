---
name: us-fbar-fatca-reporting
description: "US foreign-account and foreign-asset reporting for US persons: the FBAR (FinCEN Form 114) and FATCA (Form 8938, IRC §6038D). Covers the $10,000 FBAR aggregate threshold, the higher Form 8938 thresholds, who must file, what each regime counts, deadlines, the willful/non-willful penalty regime, and the streamlined and delinquent-FBAR remediation paths. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
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

# US Fbar FATCA Reporting

## US Foreign-Account Reporting — FBAR & FATCA v0.1

## What this file is

This is a **topic content skill**. It loads on top of `cross-border-tax-workflow-base` and assumes the cross-border router has already run, identified the taxpayer as a **US person**, and confirmed the presence of foreign financial accounts and/or foreign assets. It does not re-derive residency or US-person status; consume those from the router's working paper.

It produces a **working paper** and a **reviewer brief** describing which reporting regimes are triggered and why. It is **not** advice, **not** a filed FBAR, and **not** a filed return. A licensed accountant signs off before anything is filed.

Two distinct regimes are in scope, governed by different bodies of law and filed in different places. They overlap but **neither satisfies the other**:

- **FBAR** — FinCEN Form 114, filed electronically with **FinCEN** (the Financial Crimes Enforcement Network) through the BSA E-Filing System, **not** the IRS and **not** attached to the Form 1040. Statutory basis: Bank Secrecy Act, **31 USC §5314**; regulation **31 CFR 1010.350**.
- **FATCA** — **Form 8938**, *Statement of Specified Foreign Financial Assets*, filed **with the Form 1040** under **IRC §6038D**.

## Layer A — Reference layer (decision trees)

Each rule cites the form or statute that controls it. When a threshold figure is involved, **confirm the current-year figure against the live IRS/FinCEN instructions before relying on it** — do not treat any number below as authoritative for the filing year.

### A1. Is the taxpayer a "US person"? (gate for both regimes)

- **US person definition / gate condition** — A US person includes US citizens, US resident aliens (green-card or substantial-presence), and certain US entities/trusts/estates. If the router has not confirmed US-person status, stop and resolve that first — neither regime applies to a non-US person.  _(31 CFR 1010.350(b) for FBAR; IRC §6038D and 8938 instructions for FATCA)_

### A2. FBAR decision tree (31 USC §5314 / 31 CFR 1010.350)

- **FBAR trigger — financial interest or signature authority** — Does the US person have a financial interest in OR signature authority over one or more foreign financial accounts? (Bank, securities, brokerage, certain foreign-issued insurance/annuity with cash value, certain foreign mutual funds.) No → FBAR not required on those facts. Yes → continue.  _(31 USC §5314 / 31 CFR 1010.350)_
- **FBAR aggregate threshold** — US$10,000 USD (Aggregate maximum value of all foreign financial accounts exceeding this at any point during the calendar year triggers FBAR. This is an aggregate-across-all-accounts test, evaluated at the highest balance each account reached during the year — NOT a per-account test. Five accounts of $3,000 each trip the threshold even though no single account exceeds $10,000. No → FBAR not required. Yes → FBAR required (FinCEN Form 114), reporting every qualifying account, including signature-authority-only accounts.)  _(31 USC §5314 / 31 CFR 1010.350)_
- **FBAR deadline** — April 15, with an automatic extension to October 15 (no separate extension request needed for the FBAR).  _(31 USC §5314 / 31 CFR 1010.350)_

### A3. FATCA / Form 8938 decision tree (IRC §6038D)

- **SFFA trigger** — Does the US person hold specified foreign financial assets (SFFAs)? SFFAs are broader than FBAR-reportable accounts — they include foreign financial accounts plus foreign stock or securities held outside an account, interests in foreign entities, and foreign financial instruments held for investment. No → Form 8938 not required. Yes → continue.  _(IRC §6038D)_
- **Form 8938 threshold — living abroad, single/MFS** — > $200,000 on the last day of the year or > $300,000 at any time during the year USD (Illustrative (living abroad) — confirm exact current-year figures)  _(IRC §6038D)_
- **Form 8938 threshold — living abroad, married-filing-jointly** — > $400,000 last day or > $600,000 any time USD (Illustrative (living abroad) — confirm exact current-year figures)  _(IRC §6038D)_
- **US-resident thresholds lower than abroad thresholds** — US-resident thresholds are lower than the abroad thresholds. Do not hardcode — pull the exact figures from the current Form 8938 instructions. Below threshold → Form 8938 not required. At/above threshold → Form 8938 required, filed with the 1040.  _(IRC §6038D)_
- **Form 8938 deadline** — With the income tax return, including extensions (Form 8938 follows the 1040 due date, unlike the standalone FBAR deadline).  _(IRC §6038D)_

### A4. Overlap rule

- **Overlap between FBAR and Form 8938** — Many assets — e.g. a foreign brokerage account — are reportable on both FBAR and Form 8938. Filing one does not discharge the obligation to file the other. Map each asset to both regimes independently.  _(31 USC §5314 / 31 CFR 1010.350; IRC §6038D)_

## Layer B — Executable layer

**Input:** a list of foreign accounts/assets, each with: type, institution, country, financial-interest vs signature-authority, max balance during year (in account currency), year-end balance, and the USD-converted equivalents.

0. **Step 1: Normalize to USD** — Convert each account's maximum balance and year-end balance to USD using the Treasury year-end exchange rate (or a documented published rate). Record the rate and source in the working paper.
0. **Step 2: FBAR test** — Sum the maximum USD balances across all foreign financial accounts (financial interest + signature authority). If aggregate > $10,000 → flag FBAR required; list every qualifying account, marking signature-authority-only ones.
0. **Step 3: FATCA test** — Identify which holdings are SFFAs (superset of FBAR accounts — add foreign stock/securities held outside an account, foreign-entity interests). Determine the taxpayer's filing status and abroad vs US residency from the router output. Look up the current-year Form 8938 threshold pair (last-day / any-time) for that status+residency. Do not rely on the illustrative numbers in A3 — confirm them. Apply both the last-day test (year-end aggregate) and the any-time test (peak aggregate). Tripping either triggers Form 8938.
0. **Step 4: Deadlines** — Set FBAR to Oct 15 (auto-extended) and Form 8938 to the 1040 due date including extensions.
0. **Step 5: Output the reviewer brief** — Output the reviewer brief: which forms are required, which thresholds were tripped and by how much, the list of accounts/assets mapped to each regime (noting the overlap), FX rates used, and any open items requiring counsel (willfulness, pension treatment, signature-authority edge cases).

- **Below-threshold documentation and conservative posture** — If the taxpayer is below all thresholds, still document the test and the margin — near-threshold cases should be re-checked, and conservative posture is: when genuinely unsure whether an item counts or whether a threshold is tripped, file.  _(31 USC §5314 / 31 CFR 1010.350; IRC §6038D)_

## Comparison table — FBAR vs Form 8938

**Comparison table — FBAR vs Form 8938**  _(31 USC §5314 / 31 CFR 1010.350; IRC §6038D)_

| Dimension | FBAR (FinCEN Form 114) | FATCA (Form 8938) |
| --- | --- | --- |
| Legal basis | Bank Secrecy Act, 31 USC §5314 / 31 CFR 1010.350 | IRC §6038D |
| Where filed | FinCEN, via BSA E-Filing (separate from the return) | Attached **to the Form 1040** |
| Who files | US persons with financial interest **or signature authority** | US persons holding specified foreign financial assets |
| Threshold | Aggregate **> $10,000** at **any time** (all accounts) | Higher, varies by **filing status** and **abroad vs US** (confirm current-year figures) |
| What counts | Foreign **financial accounts** | **SFFAs** — broader: accounts **plus** foreign stock/securities held outside an account, foreign-entity interests |
| Test type | **Aggregate**, not per-account; peak balance | Last-day **and** any-time aggregate of SFFAs |
| Deadline | **Apr 15**, auto-extended to **Oct 15** | With the 1040, **including extensions** |
| Penalty regime | Non-willful vs willful (see below); civil + potential criminal | §6038D penalties (e.g., failure-to-file + continuation; understatement penalties) |

## Penalties (FBAR)

- **Non-willful FBAR penalty — per-report basis** — A civil penalty applies per failure. Per Bittner v. United States, 598 U.S. 250 (2023), the non-willful penalty is assessed per-report (per annual FBAR form), not per-account — a single late FBAR listing many accounts is one non-willful violation, not one per account.  _(Bittner v. United States, 598 U.S. 250 (2023))_
- **Willful FBAR penalty** — Materially higher — up to the greater of $100,000 or 50% of the account balance, assessed per violation, plus potential criminal exposure.  _(31 USC §5314 / 31 CFR 1010.350)_
- **Willfulness determination requires counsel** — Whether conduct is willful or non-willful is a legal determination requiring counsel; do not characterize it in the working paper beyond flagging it as an open item.  _(31 USC §5314 / 31 CFR 1010.350)_

## Remediation paths (non-willful past non-compliance)

For a US person who failed to file in prior years, the standard paths for non-willful conduct are:

- **Streamlined Filing Compliance Procedures** — **Streamlined Foreign Offshore** (taxpayer meets a non-residency / abroad test) or **Streamlined Domestic Offshore** (US-resident). Requires amended/delinquent returns, delinquent FBARs, and a non-willful certification.
- **Delinquent FBAR Submission Procedures** — where the income was reported and tax paid but FBARs were simply not filed; file the delinquent FBARs with a reasonable-cause statement.

Describe these at a high level only. Path selection turns on a willfulness analysis, which requires professional/legal judgement and frequently counsel. Do not certify non-willfulness or recommend a streamlined submission without that review.

## ⚑ AUDIT FLASH POINT — Willfulness

Never label conduct willful or non-willful in the working paper. It drives both penalty exposure and remediation-path eligibility and is a legal call for counsel. Flag it as an open item; do not resolve it.

## ⚑ AUDIT FLASH POINT — Signature-authority-only accounts

Accounts the taxpayer can direct but does not own (employer accounts, accounts they manage for others) are FBAR-reportable even with no financial interest. Easy to miss; capture them.

## ⚑ AUDIT FLASH POINT — Foreign pensions

Whether a foreign pension or retirement plan is FBAR- and/or 8938-reportable depends on the plan's structure (account-style vs entity interest) and any treaty position. Do not assume it is exempt; flag for review.

## ⚑ AUDIT FLASH POINT — Aggregate-not-per-account trap

The $10,000 FBAR threshold is tested on the sum of peak balances across all accounts. Multiple small accounts can trip it even when none individually exceeds $10,000. Never test accounts in isolation.

## ⚑ AUDIT FLASH POINT — Assets reportable on both forms

Reporting a foreign account on the FBAR does not satisfy Form 8938, and vice versa. Map every asset to both regimes independently; the overlap is intentional, not redundant.

## Topic self-checks

- [ ] US-person status confirmed from the router output before applying either regime.
- [ ] All foreign accounts normalized to USD with documented FX rate and source.
- [ ] FBAR tested on **aggregate peak** balances, not per-account.
- [ ] Signature-authority-only accounts identified and included in the FBAR set.
- [ ] SFFA list built as a **superset** of FBAR accounts (added stock/securities held outside an account and foreign-entity interests).
- [ ] Form 8938 thresholds pulled from **current-year** instructions for the correct filing status and abroad/US residency — not the illustrative figures here.
- [ ] Both the last-day and any-time Form 8938 tests applied.
- [ ] Overlap noted: assets on both forms mapped independently; one does not satisfy the other.
- [ ] Deadlines set: FBAR Oct 15 (auto-extended); Form 8938 with the 1040 incl. extensions.
- [ ] Willfulness and remediation-path selection flagged as open items for counsel — not resolved.
- [ ] Conservative posture applied: where genuinely unsure, the item is flagged to file.
- [ ] Output is a working paper + reviewer brief; no claim of human sign-off.

## Disclaimer

Provides computational and interpretive guidance on FBAR and FATCA reporting only. Not tax or legal advice and not a filed return. Willfulness and remediation-path selection require professional/legal judgement. Have outputs reviewed and signed by a qualified, licensed accountant before acting. Research-verified (tier 2) pending credentialed sign-off.

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
