---
name: oh-cat
description: Ohio Commercial Activity Tax (CAT) — ORC Chapter 5751
jurisdiction: US-OH
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# OH Cat

## Ohio Commercial Activity Tax (CAT) — ORC Chapter 5751

- **Ohio CAT overview** — Ohio CAT is a gross receipts tax (not an income tax) imposed on the privilege of doing business in Ohio, codified at Ohio Revised Code (ORC) Chapter 5751. Effective for tax periods beginning January 1, 2025, the exclusion threshold is $6,000,000 of taxable Ohio gross receipts, the rate is 0.26% on the excess, and the $150 annual minimum tax (AMT) is eliminated. Sourcing is market-based, bright-line nexus thresholds apply, and reports are now annual (Form CAT 12) due May 10 for the prior calendar year. Tax year 2025.  _(ORC Chapter 5751)_

## 1. Scope of this skill

This skill covers:

- Determination of whether a taxpayer must register and file Ohio CAT for tax year 2025 (calendar-year 2025 receipts, return due May 10, 2026).
- Computation of taxable gross receipts, application of the $6,000,000 exclusion, and computation of the 0.26% tax on the excess.
- Market-based sourcing rules under ORC §5751.033.
- Bright-line nexus tests under ORC §5751.01(I).
- Combined and consolidated election mechanics under ORC §5751.011 and §5751.012.
- Identification of excluded receipts under ORC §5751.01(F)(2).
- Filing logistics on the Ohio Business Gateway (OBG) including Form CAT 12, extensions, and final return mechanics for taxpayers cancelling registration after the HB 33 threshold increase.

This skill does **not** cover:

- Ohio personal income tax (IT 1040) — see `oh-income-tax`.
- Ohio sales and use tax — see `oh-sales-tax`.
- Ohio municipal income tax (RITA, CCA, self-administered cities) — refer out; municipal tax is separate from CAT and applies in parallel.
- Financial institutions subject to the Financial Institutions Tax (FIT) under ORC Chapter 5726 — these entities are statutorily excluded from CAT.
- Insurance companies subject to the insurance premium tax under ORC Chapter 5725/5729 — also excluded.
- Pre-2024 CAT periods (quarterly returns, $150k threshold, AMT). If the engagement requires correcting or amending a CAT 1 quarterly return for a period ending on or before December 31, 2023, escalate to a reviewer; the legacy regime is preserved in §3 below for reference but is not the primary scope.

## 2. Recent reform — HB 33 (signed July 4, 2023)

Ohio House Bill 33 (135th General Assembly, the FY 2024–2025 biennial budget) rewrote the CAT in two phased steps. The reform was the largest contraction of the CAT since its 2005 enactment and removed an estimated 90%+ of registered CAT filers from the system.

### 2.1 What HB 33 changed

- **Exclusion threshold raised** — $3,000,000 for tax periods beginning on or after January 1, 2024; $6,000,000 for tax periods beginning on or after January 1, 2025, and continuing thereafter (no further scheduled step-up)  _(HB 33)_
- **Annual Minimum Tax (AMT) eliminated** — AMT eliminated for tax periods beginning on or after January 1, 2024. Prior law imposed a $150 / $800 / $2,100 / $2,600 / $2,600 tiered AMT depending on the taxpayer's prior-year taxable gross receipts; the AMT is now $0 regardless of receipts.  _(HB 33)_
- **Quarterly filing eliminated** — All CAT taxpayers (subject to the threshold) now file annually on Form CAT 12. The legacy quarterly Form CAT 1 was abolished for periods beginning on or after January 1, 2024.  _(HB 33)_
- **Rate unchanged** — 0.26% percent (on Ohio taxable gross receipts above the exclusion)  _(HB 33)_
- **Sourcing rules unchanged** — Market-based under ORC §5751.033  _(ORC §5751.033)_
- **Bright-line nexus thresholds unchanged** — Bright-line nexus thresholds unchanged in their statutory dollar amounts ($500k/$50k/$50k/25%) but, in practice, a taxpayer that meets bright-line nexus but has Ohio receipts at or below $6,000,000 has no filing obligation for 2025+.  _(ORC §5751.01(I))_

### 2.2 Practical consequence for small businesses

A sole proprietor, single-member LLC, partnership, S-corp, or C-corp with Ohio-sourced gross receipts of $6,000,000 or less for calendar year 2025 has no CAT filing obligation for tax year 2025, regardless of bright-line nexus.

This is a categorical shift from the pre-2024 regime, under which any entity with $150,000+ in Ohio gross receipts had to register, file (initially quarterly), and pay at least the $150 AMT. Most freelancers, contractors, single-owner consultancies, and small partnerships served by openaccountants.com no longer touch the CAT at all.

### 2.3 Cancellation of registration

- **Cancellation procedure** — Taxpayers previously registered for CAT who will not exceed $6,000,000 in tax year 2025 should cancel their CAT account through the Ohio Business Gateway to avoid non-filer notices and proposed assessments. The cancellation is effective the first day of the calendar year in which the taxpayer no longer expects to meet the threshold. The Ohio Department of Taxation (ODT) issued Information Release CAT 2023-04 (and subsequent updates) confirming the cancellation procedure. If a registered taxpayer simply stops filing without cancelling, ODT will issue a non-filer notice and ultimately a jeopardy assessment based on prior-year receipts.  _(ODT Information Release CAT 2023-04)_

## 3. Threshold and AMT history

**Threshold and AMT history**  _(ORC Chapter 5751 / HB 33)_

| Tax period beginning | Registration / exclusion threshold | Tax rate | AMT | Filing frequency |
| --- | --- | --- | --- | --- |
| 2005–2013 | Register at $150k; exclusion $1,000,000 | 0.26% on excess | Tiered $150–$2,600 | Quarterly / annual depending on receipts |
| 2014–2023 | Register at $150k; exclusion $1,000,000 | 0.26% on excess | Tiered $150–$2,600 | Quarterly (most filers); annual <$1M |
| **2024** | **Exclusion $3,000,000; no separate registration threshold below exclusion** | **0.26% on excess** | **$0 (eliminated)** | **Annual only (Form CAT 12)** |
| **2025+** | **Exclusion $6,000,000** | **0.26% on excess** | **$0** | **Annual only (Form CAT 12)** |

The 2026+ row is identical to 2025 unless the General Assembly enacts a further change. As of the last_updated date of this skill (2025-11-15), no further scheduled change is enacted.

### 4.1 Base formula (2025)

- **CAT computation formula** — Taxable Ohio gross receipts (after exclusions in §7) ............ A Less: $6,000,000 statutory exclusion ............................ ($6,000,000) Excess subject to tax ........................................... B = max(0, A − 6,000,000) CAT due ......................................................... B × 0.0026  _(ORC §5751.03)_
- **No AMT/minimum/fee** — There is no AMT, no minimum, no registration fee, and no per-entity adder for tax year 2025.  _(HB 33)_

### 4.2 Combined / consolidated groups

- **Group exclusion** — For a combined group under ORC §5751.011 or a consolidated elected group under §5751.012, a single $6,000,000 exclusion applies to the group as a whole, not per member. Intra-group receipts are eliminated (consolidated election) or included (combined). See §9 for election mechanics.  _(ORC §5751.011, §5751.012)_

### 4.3 Rounding

- **Rounding requirement** — ODT instructions for Form CAT 12 require the taxpayer to round taxable gross receipts to the nearest whole dollar before applying the exclusion and rate. Round the final tax due to the nearest cent.  _(Form CAT 12 instructions)_

## 5. Sourcing — market-based under ORC §5751.033

Ohio sources gross receipts to Ohio under a market-based regime. The sourcing rules are unchanged by HB 33.

### 5.1 Tangible personal property — §5751.033(E)

- **Sourcing of TPP receipts** — Gross receipts from the sale of tangible personal property are sourced to Ohio if the property is received in Ohio by the purchaser (ship-to / delivered-to location). The location of the seller, the contract execution, or the order acceptance is irrelevant. If the property is shipped to an out-of-Ohio location (even from an Ohio warehouse), the receipt is not Ohio-sourced.  _(ORC §5751.033(E))_

### 5.2 Services — §5751.033(I)

- **Sourcing of services receipts** — Gross receipts from services are sourced to Ohio to the extent the purchaser receives the benefit of the service in Ohio. For services with a benefit received in multiple states, the taxpayer must allocate using a reasonable, consistently applied method that reflects where the purchaser uses or consumes the service. The default proxy for many B2B services is the purchaser's billing address or principal place of business when no better data exists.  _(ORC §5751.033(I))_

### 5.3 Real property — §5751.033(B)–(C)

- **Sourcing of real property receipts** — Receipts from the sale, lease, or rental of real property are sourced to Ohio if the real property is located in Ohio.  _(ORC §5751.033(B)–(C))_

### 5.4 Intangibles — §5751.033(F)

- **Sourcing of intangible property receipts** — Receipts from the use of intangible property (royalties, licenses, franchise fees) are sourced to Ohio in proportion to the use of the intangible in Ohio. For software licensed to be used in Ohio, this is typically the licensee's location.  _(ORC §5751.033(F))_

### 5.5 Rents and royalties on tangible property — §5751.033(D)

- **Sourcing of rents/royalties on TPP** — Sourced to Ohio if the tangible property is located in Ohio during the rental or royalty period.  _(ORC §5751.033(D))_

### 5.6 Throw-out / throw-back

- **No throw-out/throw-back rule** — Ohio CAT has no throw-out and no throw-back rule. If a receipt is not Ohio-sourced under the rules above, it stays out of the Ohio numerator regardless of whether it is taxed elsewhere.  _(ORC §5751.033)_

## 6. Bright-line nexus tests — ORC §5751.01(I)

- **Bright-line nexus tests** — A taxpayer has "substantial nexus" with Ohio for CAT purposes (and would need to register if above the exclusion threshold) if any one of the following is true during the calendar year: 1. $500,000+ of Ohio taxable gross receipts. 2. $50,000+ of Ohio property (owned or rented, at average value during the year). 3. $50,000+ of Ohio payroll (compensation paid to employees performing services in Ohio). 4. 25%+ of the taxpayer's total receipts, total property, or total payroll is in Ohio. 5. Domiciled in Ohio (organized under Ohio law or commercially domiciled in Ohio).  _(ORC §5751.01(I))_

The bright-line standards have been upheld against constitutional challenge in *Crutchfield Corp. v. Testa*, 151 Ohio St.3d 278 (2016), where the Ohio Supreme Court rejected the argument that physical presence is required for a gross receipts tax under the Commerce Clause — anticipating *South Dakota v. Wayfair* (2018) by two years.

- **Interaction with HB 33** — Bright-line nexus alone does not create a 2025 filing obligation. A taxpayer must meet bright-line nexus and have more than $6,000,000 of Ohio taxable gross receipts to file. A remote seller with $1,000,000 of Ohio receipts in 2025 has bright-line nexus but no CAT to file.  _(HB 33)_

## 7. Who must file — entity type

- **Entity types subject to CAT** — CAT applies to all entity types, including: - Sole proprietorships (Schedule C federal filers). - Single-member LLCs disregarded for federal tax. - General and limited partnerships, LLPs, LLLPs. - Multi-member LLCs taxed as partnerships. - S-corporations — even though Ohio has no separate state-level S-corp tax, the S-corp is the CAT taxpayer; the shareholders separately owe Ohio personal income tax on flow-through K-1 income. - C-corporations. - Disregarded entities and grantor trusts (the deemed owner is the CAT taxpayer; the disregarded entity does not separately file unless it is part of a combined / consolidated group election). - Non-Ohio entities that meet bright-line nexus and the threshold.  _(ORC Chapter 5751)_
- **Statutorily excluded entities** — Statutorily excluded under ORC §5751.01(E): - Financial institutions subject to the Financial Institutions Tax (FIT) under ORC Chapter 5726. - Insurance companies subject to ORC Chapters 5725 and 5729. - Certain affiliates of insurance companies. - Public utilities subject to the excise tax under ORC Chapter 5727 (the receipts subject to the public utility excise are excluded; non-utility receipts of a public utility are not). - Dealers in intangibles formerly subject to the (repealed) dealers-in-intangibles tax — limited residual exclusion. - Certain non-profit organizations to the extent receipts are from activities exempt from federal income tax under IRC §501. - 501(c)(3) hospitals and similar. - Certain agricultural cooperatives organized under ORC Chapter 1729 or Subchapter T of the IRC. A taxpayer is also excluded as a non-filer (rather than as an exempt entity) if the taxpayer is below the $6,000,000 receipts threshold.  _(ORC §5751.01(E))_

## 8. Excluded receipts — ORC §5751.01(F)(2)

- **Excluded receipt categories** — 1. Interest income — excluded except interest on credit card and banking transactions earned by a person in the business of making such loans. Ordinary operating interest on bank deposits held by a non-financial business is excluded. 2. Dividends received from any corporation. 3. Receipts from the sale, exchange, or disposition of capital assets and §1221/§1231 assets. A practice firm or contractor selling a vehicle, computer, or office building does not include the proceeds in the CAT base. (Inventory sales are not §1221/§1231 — those are taxable gross receipts.) 4. Receipts from the issuance or sale of one's own stock, debt, or other equity / debt instruments (e.g., a capital raise, a bond issuance). 5. Contributions to capital. 6. Damages received for personal injury or property loss, to the extent the damages do not represent recovery of lost profits. 7. Federal, state, and local excise taxes collected from the purchaser when the seller is acting as a collection agent (e.g., Ohio sales tax collected at point of sale is excluded from the CAT base; the seller's own commission or markup is not excluded). 8. Tips and gratuities paid over to employees. 9. Receipts of an agent on behalf of a principal, to the extent the agent is required to remit the gross to the principal (commissions retained by the agent are taxable gross receipts to the agent). 10. Loan proceeds received by the borrower. 11. Pass-through receipts of qualified motor fuel dealers, qualified distribution centers, and certain other narrow categories under §5751.01(F)(2)(z) and following — escalate to reviewer if the engagement involves these. 12. Receipts from agricultural commodity sales by producers in certain circumstances.  _(ORC §5751.01(F)(2))_

The list above is non-exhaustive. The full statutory list of exclusions runs to roughly 50 subparagraphs at ORC §5751.01(F)(2)(a) through §5751.01(F)(2)(zz). For freelance software developers, consulting firms, and standard small-business engagements, the most commonly relevant exclusions are #1, #2, #3, #4, and #7.

### 9.1 Combined taxpayer — §5751.011 (mandatory)

- **Combined taxpayer rules** — Two or more persons are required to file as a combined taxpayer if they have more than 50% common ownership (direct or indirect) and they elect or are deemed to be combined. Inter-member receipts are included in the combined group's taxable gross receipts (i.e., not eliminated). One $6,000,000 exclusion applies to the group.  _(ORC §5751.011)_

### 9.2 Consolidated elected taxpayer — §5751.012 (elective)

- **Consolidated election rules** — Two or more persons may elect to file as a consolidated elected taxpayer if they have either: - 80% or more common ownership (the "80% consolidated election"), or - 50% or more common ownership (the "50% consolidated election"). Under a consolidated election, intra-group receipts are eliminated in computing the group's taxable gross receipts. The trade-off is that all commonly owned entities meeting the chosen threshold must be included, including entities with no Ohio nexus — bringing their out-of-Ohio receipts in as part of the denominator for sourcing computations is generally irrelevant (since CAT is market-based and the numerator is Ohio receipts, not an apportionment factor), but bringing them in does mean their Ohio receipts are pulled in. The consolidated election is binding for at least 8 calendar quarters (now effectively 2 annual periods under the post-2024 annual regime). The election is made on Form CAT-CS.  _(ORC §5751.012)_

### 9.3 Decision framework

- **Combined vs consolidated decision framework** — For a small group of commonly owned entities: - If intra-group receipts are large (e.g., a holding company that licenses IP to operating subsidiaries), a consolidated election is usually beneficial because eliminating intra-group receipts can drop the group below the $6,000,000 threshold or shrink the taxable base. - If intra-group receipts are small and Ohio operations are concentrated in one entity, filing separately is usually simpler. - A combined filing (mandatory above 50% common ownership absent a consolidated election) does not eliminate intra-group receipts and is therefore rarely preferred over a consolidated election when both are available. Escalate to a reviewer before recommending a consolidated election: the 8-quarter binding period and the inclusion of all qualifying affiliates make this a non-trivial decision.

### 10.1 Form

- **Form CAT 12** — Form CAT 12 — Annual Commercial Activity Tax Return. Filed through the Ohio Business Gateway (OBG) at gateway.ohio.gov. Paper filing is permitted only in narrow circumstances (e.g., the taxpayer has obtained a hardship waiver). Most filers file and pay electronically. Form CAT 1 (the legacy quarterly return) is abolished for periods beginning on or after January 1, 2024.  _(Ohio Business Gateway)_

### 10.2 Due date

- **Filing due date** — May 10 following the close of the calendar year. For tax year 2025, the return is due Monday, May 11, 2026 (May 10, 2026 is a Sunday; ORC §5703.063 shifts the due date to the next business day).  _(ORC §5703.063)_

### 10.3 Extensions

- **No routine extensions; penalties** — Ohio does not grant routine extensions of time to file the CAT return. Late filing triggers: - Late filing penalty: the greater of $50 or 5% of the tax due per month (or fraction thereof), up to 50% of the tax due, under ORC §5751.06. - Late payment penalty: 10% of the tax due (or $50, whichever is greater), under ORC §5751.06(B). - Interest at the statutory rate set annually under ORC §5703.47.  _(ORC §5751.06, §5751.06(B), §5703.47)_

### 10.4 Registration

- **Registration requirement** — Taxpayers who reasonably expect to exceed $6,000,000 in taxable Ohio gross receipts in the current calendar year must register within 30 days of meeting the threshold, using Form CAT 1 (the registration form — note: different from the abolished quarterly return form which shared the same number under the legacy regime; in current ODT usage "CAT 1" refers only to registration). There is no longer a registration fee.  _(ORC Chapter 5751)_

### 10.5 Final return / cancellation

- **Final return and cancellation procedure** — A taxpayer who no longer expects to meet the threshold files a final CAT 12 covering the partial year of activity up to the cancellation date and submits a CAT account cancellation through OBG. See §2.3 above.  _(ODT Information Release CAT 2023-04)_

### Example 1 — Small Ohio LLC under the threshold

Facts: ABC Consulting LLC is an Ohio-domiciled single-member LLC owned by an Ohio resident. Calendar year 2025 gross receipts are $4,000,000, all sourced to Ohio (services delivered to Ohio clients). The LLC has $80,000 of Ohio payroll.

Analysis:
- Bright-line nexus: yes — Ohio domicile and >$500k Ohio receipts and >$50k Ohio payroll. Three independent bright-line tests are met.
- Threshold: $4,000,000 < $6,000,000 exclusion.
- CAT due: $0.
- Filing required: No. The LLC has no CAT obligation for 2025.
- If the LLC was previously registered for CAT (e.g., it registered in 2022 when the threshold was $150k), it should cancel its CAT account through OBG to avoid non-filer notices.
- The owner separately owes Ohio personal income tax on the $4M of net profit flowing through Schedule C → IT 1040, and Ohio municipal income tax to the applicable RITA / CCA / self-administered city. Those are independent of CAT.

### Example 2 — Ohio C-corp above the threshold

Facts: XYZ Manufacturing, Inc. is a Delaware C-corp with its principal place of business and manufacturing plant in Cleveland, Ohio. Calendar year 2025 gross sales are $25,000,000. Of those, $10,000,000 ship to Ohio purchasers and $15,000,000 ship out of state. XYZ also receives $500,000 of dividends from a subsidiary, $200,000 of interest on operating bank deposits, and $400,000 from the sale of a fully-depreciated press (book gain $400,000, treated as §1231 property for federal purposes).

CAT computation:
```
Ohio-sourced gross sales (ship-to Ohio) ............. $10,000,000
Out-of-state sales (ship-to other states) ...........          0   (not in Ohio numerator)
Dividends ...........................................          0   (excluded §5751.01(F)(2))
Bank interest .......................................          0   (excluded; not credit-card / banking biz)
§1231 press sale ....................................          0   (excluded — capital / §1231 asset)
-----------------------------------------------------
Taxable Ohio gross receipts ......................... $10,000,000
Less: 2025 exclusion ................................  (6,000,000)
Excess ..............................................  $4,000,000
CAT @ 0.26% .........................................     $10,400
```

XYZ files Form CAT 12 for tax year 2025 by May 11, 2026, reporting taxable Ohio gross receipts of $10,000,000 and tax of $10,400. The out-of-state sales, dividends, bank interest, and press sale are correctly excluded.

### Example 3 — Multi-entity combined / consolidated group

Facts: A privately held group consists of:
- HoldCo, Inc. — Ohio C-corp holding company, no operations, 100% owner of OpCo and IPCo.
- OpCo, LLC — Ohio multi-member LLC (taxed as partnership, 100% owned by HoldCo via merger fiction for state purposes; treated as a separate CAT person), $9,000,000 of Ohio sales to third-party customers.
- IPCo, LLC — Delaware LLC, 100% owned by HoldCo, licenses trademarks to OpCo for an annual royalty of $2,000,000 (paid by OpCo to IPCo) — the IP is used by OpCo in Ohio, so the royalty is Ohio-sourced to IPCo under §5751.033(F).

Step 1 — separate filing (no election):
- HoldCo: $0 Ohio receipts → no CAT.
- OpCo: $9,000,000 Ohio receipts − $6,000,000 = $3,000,000 × 0.26% = $7,800.
- IPCo: $2,000,000 Ohio receipts (royalty from OpCo). Below threshold → $0. (Bright-line nexus is met via 25%+ rule if IPCo's worldwide receipts are <$8M, but threshold is not met.)
- Group total: $7,800.

Step 2 — consolidated election under §5751.012 (80% common ownership, met via HoldCo):
- Intra-group royalty of $2,000,000 from OpCo to IPCo is eliminated.
- Combined Ohio receipts: $9,000,000 (OpCo's third-party sales) + $0 (HoldCo) + $0 (IPCo, after elimination) = $9,000,000.
- Exclusion: $6,000,000 (one exclusion for the group).
- Taxable: $3,000,000 × 0.26% = $7,800.

In this stylized case the answer is the same. But if IPCo also had $5,000,000 of third-party royalty receipts from Ohio licensees, the separate-filing answer would be:
- OpCo: $3,000,000 × 0.26% = $7,800.
- IPCo: ($5,000,000 + $2,000,000 − $6,000,000) × 0.26% = $1,000,000 × 0.26% = $2,600.
- Group total separate: $10,400.

Under the consolidated election (intra-group $2M eliminated):
- Combined: $9,000,000 (OpCo) + $5,000,000 (IPCo third-party) = $14,000,000.
- Exclusion: $6,000,000.
- Tax: $8,000,000 × 0.26% = $20,800.

In that variant the consolidated election is worse because the single $6,000,000 exclusion replaces what would have been effectively two partial exclusions across the separate filers. The intra-group elimination of $2M does not offset the loss of the second exclusion. The combined / consolidated election decision must be modelled both ways before filing, and the election is binding for 2 annual periods once made.

### Example 4 — Remote seller with Ohio receipts below threshold

Facts: A California S-corp sells custom analytics dashboards to clients nationwide. In 2025 it has $1,500,000 of receipts sourced to Ohio (services consumed by Ohio purchasers under §5751.033(I)) and $20,000,000 of total receipts.

Analysis:
- Bright-line nexus: yes — $1.5M Ohio receipts exceeds the $500,000 receipts threshold.
- Threshold: $1,500,000 < $6,000,000.
- CAT due: $0. No registration required, no filing required.

This is the typical post-HB 33 outcome for SaaS and consulting businesses doing business in Ohio at small to medium scale.

## 12. Interaction with other Ohio taxes

- **Interaction with IT 1040, sales tax, municipal tax, FIT/insurance** — - Ohio personal income tax (IT 1040): Independent of CAT. CAT is paid by the entity (or the sole proprietor as the CAT taxpayer); pass-through owners separately owe IT 1040 on flow-through income. There is no CAT deduction or credit against IT 1040, but the CAT itself is a federally deductible state and local tax under IRC §164 for the entity, subject to the SALT cap rules on the owner's federal return if it flows through (or fully deductible at the entity level for a C-corp). - Ohio sales tax: Independent. Sales tax is a transaction tax collected from customers; the seller acts as a collection agent and the collected sales tax is excluded from CAT receipts under §5751.01(F)(2)(g). Out-of-scope here — see `oh-sales-tax`. - Ohio municipal income tax (RITA / CCA / self-administered): Independent. Municipalities tax net business income (not gross receipts) at rates typically between 1% and 3%. A business that owes CAT also typically owes municipal income tax to each city in which it does business, with apportionment under ORC Chapter 718. Out-of-scope here — refer to municipal tax skill or to the RITA / CCA portals directly. - Ohio Financial Institutions Tax (FIT) / Insurance premium tax: Mutually exclusive with CAT (the taxpayer is in one regime or the other). Out of scope for this skill.  _(ORC §5751.01(F)(2)(g); ORC Chapter 718; IRC §164)_

## 13. Open questions / escalation triggers

Escalate to a reviewer (do not auto-resolve) if any of the following are present:
- Receipts approaching but not clearly above $6,000,000 (close-to-threshold cases require careful sourcing review and timing).
- A consolidated election is being considered, or an existing election is in its binding period.
- Receipts from agricultural commodities, motor fuel, qualified distribution centers, integrated supply chain businesses, or other narrow statutory carve-outs.
- A change in entity structure (merger, reorganization, division) during the year.
- An Ohio-domiciled entity with substantial out-of-state receipts where the 25% bright-line factor is in play but the dollar thresholds are not.
- Any pre-2024 period (legacy quarterly regime, AMT, $150k threshold).
- Disputes with ODT, jeopardy assessments, or non-filer notices on a previously registered account.

## 14. Provenance

- ORC Chapter 5751 — statutory authority for CAT, including:
  - §5751.01 — definitions, exclusions (entity-level and receipts-level).
  - §5751.011 — combined taxpayers.
  - §5751.012 — consolidated elected taxpayers.
  - §5751.02 — imposition of tax.
  - §5751.03 — rate.
  - §5751.033 — sourcing.
  - §5751.05 — return filing.
  - §5751.06 — penalties and interest.
- Ohio House Bill 33 (135th General Assembly, 2023–2024 biennial budget, signed July 4, 2023) — threshold increase to $3M / $6M, AMT elimination, transition to annual filing.
- Ohio Administrative Code (OAC) 5703-29 — CAT regulations.
- Ohio Department of Taxation Information Releases:
  - CAT 2023-04 — HB 33 transition guidance and registration cancellation procedures.
  - CAT 2005-17 — sourcing of services (still relied on post-HB 33; the sourcing rules are unchanged).
  - CAT 2014-01 — bright-line nexus standards (post-Crutchfield guidance).
- Case law:
  - Crutchfield Corp. v. Testa, 151 Ohio St.3d 278, 2016-Ohio-7760 — upheld bright-line nexus under Commerce Clause.
  - Newegg, Inc. v. Testa, 151 Ohio St.3d 271, 2016-Ohio-7762 — companion case.
- Forms:
  - Form CAT 12 — Annual Commercial Activity Tax Return (current).
  - Form CAT 1 — Registration (current usage); legacy quarterly Form CAT 1 abolished.
  - Form CAT-CS — Consolidated election.
- Ohio Business Gateway: gateway.ohio.gov — electronic filing portal.
- ODT CAT homepage: tax.ohio.gov/business/ohio-business-taxes/commercial-activity-tax.

This skill is current as of the last_updated date in the frontmatter. It does not track changes enacted after that date. Before relying on this skill for a tax year other than 2025 or for a fact pattern that touches the open questions in §13, the reviewer should confirm that no superseding legislation or ODT release has been issued.

## End of skill.

*End of skill.*

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
