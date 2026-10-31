---
name: au-dssp
description: >
  Use this skill to classify Australian Dividend Substitution Share Plan
  transactions and maintain share parcel tax records for the 2026-27 income
  year. Covers Australian resident individuals, companies, trusts and complying
  superannuation funds holding shares on capital account, subject to the
  applicable scheme ruling. Trigger phrases include DSSP, dividend substitution
  share plan, bonus share plan, AFIC bonus shares, Argo DSSP, dividend
  reinvestment versus DSSP, inherited acquisition date and bonus share cost
  base. Produces a documented income classification and parcel reconciliation
  for professional review; excludes investment recommendations and complete
  income tax or capital gains tax calculations.
version: 0.2
jurisdiction: AU
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
depends_on:
  - workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Dividend Substitution Share Plans (DSSP) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

**This file is a content skill that loads on top of a workflow base**, [workflow-base](../foundation/workflow-base.md). It determines the treatment of an existing DSSP allotment and updates acquisition records. Pass the reconciled parcels to [au-capital-gains](au-capital-gains.md) when a later disposal needs calculation; verify that companion's coverage for the disposal period.

**Tax year coverage.** This skill is current for tax year 2026-27 as of 18 October 2026. Its numerical example reproduces historical ATO facts to demonstrate allocation, not current share prices or allotment terms. Check the operative law, ruling status and actual scheme for the transaction date before applying a position.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

## Section 2 — Filing requirements

For an allotment satisfying its ruling, exclude the bonus-share value from dividend income. Report actual cash or reinvested dividends separately under the applicable annual return instructions. A DRP dividend remains assessable even when no cash reaches the shareholder. Sources: [CR 2023/61, paragraphs 7–10][argo]; [TD 2000/3, paragraphs 1–4][drp].

Determine the taxpayer's return obligations and lodgment date separately; this skill supplies no general filing deadline. Retain the election confirmation, registry allotment advice, dividend statement, original acquisition records, prior corporate actions and parcel calculations. The ATO specifically requires acquisition and dividend-treatment records for bonus shares: [ATO, Keeping records, “Records relating to bonus shares”][records].

Intake additions: establish the legal and beneficial owner, residency, entity type, income year, issuer, plan name, participation election, participating parcels, allotment quantity, consideration paid, capital/revenue classification and any applicable financial-arrangements election. Obtain the scheme ruling and confirm that its described scheme was carried out.

---

## Section 3 — Rates and thresholds

| Item | Amount or condition | Source |
|------|---------------------|--------|
| Minimally franked dividend | Unfranked, or franked to less than 10%; the listed-company exception requires a dividend outside this definition and no related share-capital-account credit | [ITAA 1936, section 45(3)][streaming]; [section 6BA(6)][bonus-share-law] |
| Original acquisition date boundary | On or after 20 September 1985: reasonably apportion the first element across original and bonus shares; earlier fully paid qualifying shares follow the pre-CGT branch | [ITAA 1997, section 130-20(3), table items 1 and 3][cgt-law] |
| AFIC ruling period | Applies from 1 July 2011, subject to the ruling's class, scheme and settlement qualifications | [CR 2012/10, paragraphs 3–8][afic] |
| Argo and Argo Infrastructure ruling periods | 1 July 2023 to 30 June 2028; verify the applicable issuer and scheme | [CR 2023/61, paragraph 6][argo]; [CR 2023/62, paragraph 6][argo-infrastructure] |

There is no standalone DSSP tax rate in this skill. Do not infer a permanent tax exemption from the absence of dividend income at allotment.

---

## Section 4 — Computation rules

### Step 1 — Identify the transaction and establish ruling coverage

Match the election and registry advice to the issuer's scheme. Check residency, capital-account treatment, exclusion of financial-arrangements treatment, consideration, share-capital-account treatment and the ruling period. Confirm the scheme matches the ruling rather than relying on “DSSP” in a transaction description. Sources: [CR 2012/10, paragraphs 3–6 and 22][afic]; [CR 2023/61, paragraphs 4–10 and 16–26][argo].

| Registry transaction | Tax working-paper treatment | Source |
|----------------------|-----------------------------|--------|
| DSSP bonus allotment matching the ruling | Apply the non-dividend classification and parcel allocation below | [CR 2023/61, paragraphs 7–13][argo] |
| Dividend applied under a DRP | Record the assessable dividend and a separate purchase parcel; retain its new acquisition date and cost | [TD 2000/3, paragraphs 1–4][drp] |
| Mixed cash/DRP and DSSP participation | Separate the actual dividend from the bonus allotment and use only participating shares for allocation | [CR 2012/10, paragraphs 14–22][afic] |
| Unidentified bonus or reinvestment entry | Mark Needs Input until the election and plan evidence establish the treatment | [CR 2012/10, paragraphs 3–6][afic] |

### Step 2 — Determine income, franking and LIC treatment

For a qualifying DSSP, record no assessable dividend for the bonus allotment. Do not claim the foregone dividend's franking credit, gross-up or tax offset: the shareholder did not receive that franked dividend. Do not claim an LIC capital gain deduction for the foregone dividend. Keep actual dividends on non-participating shares separate. Sources: [CR 2012/10, paragraphs 14–22][afic]; [ITAA 1997, section 207-20][franking]; [CR 2023/61, paragraphs 10 and 15][argo].

### Step 3 — Allocate bonus shares to participating original parcels

Preserve each original acquisition parcel. For partial participation within a purchase parcel, separate the participating shares and their proportional first element from the non-participating shares. Allocate the actual bonus quantity pro rata across the participating original parcels. Reconcile the allocated total to the registry advice; resolve fractional allocation and scheme rounding from the actual plan rather than inventing additional whole shares. Bonus shares inherit the acquisition date of their corresponding original parcel. Sources: [ITAA 1997, section 130-20][cgt-law]; [CR 2023/61, paragraphs 11, 20 and 42–43][argo].

### Step 4 — Reallocate acquisition cost without increasing it

For each post-CGT parcel of identical shares issued for no consideration, define:

- `N`: participating original shares immediately before the allotment.
- `B`: bonus shares allocated to that parcel.
- `C`: that parcel's first cost-base element immediately before the allotment.

Calculate `new first element per share = C / (N + B)`. The original shares retain `N × C / (N + B)` and the bonus shares receive `B × C / (N + B)`. Their combined first element must still equal `C`. Apply the same allocation separately to the reduced-cost-base first element if its balance differs. Do not add the foregone dividend or market value as new acquisition expenditure. Sources: [ITAA 1936, section 6BA(3)][bonus-share-law]; [ITAA 1997, section 130-20(3)][cgt-law]; [CR 2012/10, paragraphs 44–52][afic].

Keep other cost-base elements separately attributable; these formulas reallocate the first element only. Keep full precision in the parcel ledger and reconcile any display rounding so the total first element remains unchanged. Repeat using the updated quantities and balances for each later qualifying allotment.

### Step 5 — Worked example using published ATO figures

The ATO's historical bonus-share example illustrates the allocation rule used above; it does not establish eligibility for a particular DSSP. Chris bought 100 shares for $1 each on 1 June 1985 and 300 shares for $1 each on 27 May 1986. He received 400 fully paid bonus shares on 15 November 1986 for no payment, with no amount assessed as a dividend. Source: [ATO, Guide to capital gains tax 2025, Example 35][ato-example].

| Worked position | Result | Source |
|-----------------|--------|--------|
| Dividend classification | Exclude the allotment from dividend income under the example's stated facts | [ATO Example 35][ato-example] |
| Parcel allocation | Allocate 100 bonus shares to the earlier parcel and 300 to the later parcel | [ATO Example 35][ato-example] |
| Later parcel's first element | $300 ÷ (300 + 300) = $0.50 for each original and bonus share | [ATO Example 35][ato-example] |
| Cost reconciliation, derived from those inputs | Original shares: 300 × $0.50 = $150; bonus shares: 300 × $0.50 = $150; combined: $300 | [ATO Example 35][ato-example] |
| Acquisition dates and earlier parcel | The bonus parcels inherit 1 June 1985 and 27 May 1986 respectively; the earlier 100 bonus shares retain pre-CGT treatment | [ATO Example 35][ato-example] |

### Step 6 — Produce the reviewer records

Extend the base working paper with issuer, scheme, ruling and coverage conclusion; participating parcel identifier; original and bonus quantities; original and inherited acquisition dates; first-element balances before and after; separate reduced-cost-base balances; other cost elements; registry reconciliation; dividend, franking and LIC treatment; source links; and unresolved facts. Flag every DSSP classification and parcel adjustment for review, regardless of amount. This is a workflow review rule, not a statutory monetary threshold.

---

## Section 5 — Edge cases and special rules

- **Pre-CGT parcels:** apply the fully paid bonus-share branch separately from post-CGT parcels, using the boundary in Section 3. Do not extend it to partly paid shares. Source: [ITAA 1997, section 130-20(3), table items 2–4][cgt-law].
- **Partial participation and repeated allotments:** use the participating shares and actual allotment for each event. Preserve parcel dates and cumulative allocations. Source: [CR 2023/61, paragraphs 20–24 and 42–45][argo].
- **Anti-avoidance:** a plan label or an election alone does not establish non-dividend treatment. Review streaming or materially different arrangements separately; conclusions about sections 45, 45A and 45B belong to the stated scheme. Source: [CR 2023/61, paragraphs 8–9, 16 and 32–39][argo].

| Missing or ambiguous fact | Permitted treatment |
|---------------------------|---------------------|
| Plan classification, election or ruling coverage | Mark Needs Input; do not assume a DSSP exemption or substitute a DRP treatment |
| Original acquisition cost or date | Mark the affected calculation Needs Input; do not substitute a nil cost or the allotment date |
| Participating parcels, bonus quantity or rounding | Reconcile with registry records before finalising parcel balances |

**R-AU-DSSP-SCOPE:** trigger when the requested treatment falls outside Section 1, or the scheme materially differs from the supporting ruling. Output: “This DSSP skill does not establish the tax treatment of these facts. Obtain the applicable primary authority and professional review before completing the affected position.”

**R-AU-DSSP-EVIDENCE:** trigger when a missing fact in the table prevents classification or allocation. Output: “Needs Input: the DSSP classification or parcel calculation cannot be completed from the available records. Obtain the missing scheme or acquisition evidence identified in the working paper.”

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] All input figures trace to source documents.
- [ ] Rates, statutory boundaries and ruling periods match the transaction date.
- [ ] The issuer, shareholder class and actual scheme satisfy the cited ruling.
- [ ] DSSP, DRP and cash-dividend transactions are classified separately.
- [ ] No foregone dividend or market value has increased acquisition cost.
- [ ] Bonus quantities reconcile and each parcel retains its correct acquisition date.
- [ ] First-element balances reconcile before and after allocation; reduced cost base and other cost elements remain distinct.
- [ ] Edge cases and refusal triggers in Section 5 are checked.
- [ ] Output format matches the base skill spec and includes the reviewer records in Section 4.

**Revision record:** v0.2, 18 October 2026. Source-cited draft with parcel allocation, transaction patterns and reviewer checks; professional sign-off pending.

[afic]: https://www.ato.gov.au/law/view/document?DocID=CLR/CR201210/NAT/ATO/00001
[argo]: https://www.ato.gov.au/law/view/document?DocID=CLR/CR202361/NAT/ATO/00001
[argo-infrastructure]: https://www.ato.gov.au/law/view/document?DocID=CLR/CR202362/NAT/ATO/00001
[drp]: https://www.ato.gov.au/law/view/document?DocID=TXD/TD20003/NAT/ATO/00001
[records]: https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-guide-2022/part-a-about-capital-gains-tax/keeping-records
[streaming]: https://www.ato.gov.au/law/view/document?DocID=PAC/19360027/45
[bonus-share-law]: https://www.ato.gov.au/law/view/document?DocID=PAC/19360027/6BA
[cgt-law]: https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/130-20
[franking]: https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/207-20
[ato-example]: https://www.ato.gov.au/api/public/content/e69fe46564f948f1a935476d86d6b5aa?v=47aa113a

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

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
