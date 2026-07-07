---
name: ca-pte-elective-tax
description: Tier 2 California content skill for the Pass-Through Entity Elective Tax (R&TC §§ 17052.10, 19900-19906; AB 150). Applies to S-corps, partnerships, and LLCs taxed as partnerships with at least one consenting individual, fiduciary, estate, or trust owner. Computes the 9.3% tax on qualified net income (each consenting owner's distributive share of CA-sourced income), produces Form 3804 entity election and Form 3804-CR owner-level nonrefundable credit, schedules the mandatory June 15 prepayment (greater of $1,000 or 50% of prior-year PTE tax) and the balance due by the original return due date, and flags the post-2025 sunset and the federal Notice 2020-75 SALT-cap workaround treatment. Tax year 2025.
jurisdiction: US-CA
domain: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ca-pte-elective-tax

## California Pass-Through Entity Elective Tax (PTE Elective Tax / "AB 150 tax")

## Section 1 -- Scope

### 1.1 What this skill does

- **PTE Elective Tax** — This skill prepares the California Pass-Through Entity Elective Tax computation, election, payment schedule, and owner-level credit for tax year 2025. The PTE Elective Tax (sometimes called the "AB 150 tax", the "SALT-cap workaround", or the "PTET") is an annual entity-level election that allows qualifying pass-through entities to pay an entity-level California income tax at 9.3% of each consenting owner's distributive share of California-sourced income. In exchange, each consenting owner receives a nonrefundable California credit equal to their share of the tax paid on Form 3804-CR. The economic purpose of the election is to convert what would otherwise be a state income tax paid at the owner level (subject to the federal $10,000 state and local tax (SALT) deduction cap under IRC § 164(b)(6)) into a state income tax paid at the entity level. Under IRS Notice 2020-75 (issued November 9, 2020), specified income tax payments made by a partnership or S corporation are deductible by the entity in computing its non-separately-stated taxable income and are not treated as separately stated items subject to the SALT cap. The election therefore preserves the federal deduction for what is, in economic substance, the owners' California income tax.  _(IRC § 164(b)(6); IRS Notice 2020-75)_

### 1.2 Statutory authority

- **R&TC § 17052.10** — Owner-level nonrefundable PTE tax credit; ordering, carryforward, and refundability rules.  _(R&TC § 17052.10)_
- **R&TC §§ 19900–19906** — Entity-level election, qualified net income definition, tax rate, payment schedule, election procedure, and irrevocability.  _(R&TC §§ 19900–19906)_
- **AB 150 (2021 Cal. Stat. ch. 82)** — Enacted the regime for tax years beginning on or after January 1, 2021, and before January 1, 2026.  _(AB 150 (2021 Cal. Stat. ch. 82))_
- **SB 113 (2022 Cal. Stat. ch. 3)** — Expanded eligibility (allowed disregarded SMLLC owners and SMLLCs owned by individuals to consent), removed tentative-minimum-tax limitation on the credit, allowed credit to reduce tax below tentative minimum tax, and reordered the credit ahead of the OSTC.  _(SB 113 (2022 Cal. Stat. ch. 3))_
- **SB 851 (2022 Cal. Stat. ch. 705)** — Clarified the interaction of the PTE credit with the Other State Tax Credit (OSTC) by directing taxpayers to add back the PTE credit when computing the OSTC's "net tax" denominator.  _(SB 851 (2022 Cal. Stat. ch. 705))_
- **IRS Notice 2020-75** — Federal blessing of entity-level deduction.  _(IRS Notice 2020-75)_

### 1.3 What this skill does NOT cover

1. Composite returns under R&TC § 18535 (Form 540NR Group Return) — these are a separate regime, mutually exclusive with PTE elective tax for the same income stream.
2. The nonresident withholding regime under R&TC §§ 18662, 18666 (Forms 592, 592-PTE, 592-B) — separate from PTE elective tax, but interacts because PTE prepayments do not satisfy the nonresident withholding obligation.
3. Tiered partnerships where an upper-tier pass-through is itself an owner of the electing entity (these owners are ineligible to consent; the lower tier may still elect for its individual owners).
4. Publicly traded partnerships (statutorily excluded).
5. Disregarded entities other than SMLLCs owned by individuals (the 2022 SB 113 fix narrowly admitted SMLLCs owned by individuals only).
6. Post-2025 elections — the regime sunsets for taxable years beginning on or after January 1, 2026 unless re-extended (see Section 9).

### 1.4 Assumed companion skills

This skill must be loaded alongside `us-tax-workflow-base` v0.2 or later. It typically runs in coordination with:

- `ca-540-individual-return` — owner-level Form 540 / 540NR claiming the PTE credit.
- `ca-smllc-form-568` — for multi-member LLC entity returns electing PTE (note: that skill is SMLLC-only; multi-member 568 is documented here for the PTE flow).
- `us-s-corp-election-decision` — when a freelance developer is considering S-corp status, the PTE election is a downstream consequence to evaluate.
- `us-federal-return-assembly` — for the entity's federal Form 1065 / 1120-S with the Notice 2020-75 deduction.

## Section 2 -- Eligibility

The PTE elective tax has two eligibility tests that must BOTH be satisfied:

1. The **entity** must be a "qualified entity" under R&TC § 19902(a).
2. At least one **owner** must be a "qualified taxpayer" under R&TC § 17052.10(b) and must affirmatively consent to inclusion.

The election covers only the qualified net income attributable to consenting qualified taxpayers. Non-consenting owners and ineligible owners are excluded from the computation; the entity continues to report their distributive shares in the ordinary way on Schedule K-1 (565 / 568 / 100S).

### 2.1 Qualified entities (R&TC § 19902(a))

- **Qualified entity definition** — A qualified entity is an entity that: 1. Is taxed as a partnership or S corporation for the taxable year; AND 2. Has only partners, shareholders, or members that are (a) corporations (as defined in R&TC § 23038, which excludes S corporations from "corporation" for this purpose; an S corporation owner of a partnership is treated as a permitted upper-tier owner only with respect to its own individual shareholders' shares, not as a qualified taxpayer itself), (b) individuals, fiduciaries, estates, or trusts; AND 3. Is NOT a publicly traded partnership (as defined in IRC § 7704); AND 4. Is NOT a partnership, LLC, or other entity that is required to be included in a combined reporting group under R&TC § 25101.5.  _(R&TC § 19902(a))_

**Eligible entity types**  _(R&TC § 19902(a))_

| Federal classification | CA return | PTE-eligible? |
| --- | --- | --- |
| S corporation (Form 1120-S) | Form 100S | YES |
| Partnership / multi-member LLC taxed as partnership (Form 1065) | Form 565 or Form 568 | YES |
| LLC taxed as S corporation | Form 100S | YES |
| Sole proprietorship | Schedule C (federal) / nothing at CA entity level | NO |
| Single-member LLC disregarded for federal tax, owned by individual | Form 568 (CA only) | NO (entity ineligible) — but see Section 2.3 below: the SMLLC's individual owner may consent at the level of an upper-tier electing partnership |
| Single-member LLC disregarded, owned by a partnership / S-corp | Form 568 | NO |
| C corporation (Form 1120) | Form 100 | NO |
| Publicly traded partnership | Form 565 | NO (statutorily excluded) |

- **Critical exclusion — SMLLCs** — A single-member LLC disregarded for federal tax is NOT a qualified entity in its own right, because it is not "taxed as a partnership or S corporation." A freelance developer operating through a CA SMLLC cannot elect PTE on the SMLLC. To access the PTE workaround, the SMLLC would need to (a) elect S-corp treatment via Form 2553 (after which it files Form 1120-S federally and Form 100S in CA — see `us-s-corp-election-decision`), or (b) bring in a second member, become a partnership, and file Form 1065 / 568.  _(R&TC § 19902(a))_
- **Critical exclusion — sole proprietorships** — A bare sole proprietor reporting on Schedule C has no entity that can elect. The SALT-cap workaround is unavailable.  _(R&TC § 19902(a))_

### 2.2 Qualified taxpayers (R&TC § 17052.10(b))

- **Qualified taxpayer definition** — A qualified taxpayer is a partner, shareholder, or member of a qualified entity that is: 1. An individual, fiduciary, estate, or trust subject to California personal income tax under R&TC Part 10; AND 2. NOT a partnership for federal tax purposes; AND 3. Consents to have its distributive share of qualified net income included in the entity's PTE elective tax computation.  _(R&TC § 17052.10(b))_

**Eligibility chart for owners**  _(R&TC § 17052.10(b))_

| Owner type | Qualified taxpayer? |
| --- | --- |
| Individual (CA resident) | YES |
| Individual (CA nonresident with CA-source income) | YES |
| Individual (CA part-year resident) | YES (only for CA-source share) |
| Grantor trust (treated as owned by individual grantor) | YES — consent through grantor |
| Non-grantor trust (irrevocable, separate tax entity) | YES |
| Estate (during administration) | YES |
| Disregarded SMLLC owned by an individual | YES — SB 113 fix; consent runs through the SMLLC's individual owner |
| Disregarded SMLLC owned by a non-individual (e.g., S-corp, partnership, trust other than grantor) | NO (entity is disregarded but the underlying owner is not a qualified taxpayer) |
| C corporation | NO |
| S corporation owner of a partnership | NO (S-corp itself cannot be a qualified taxpayer; however, the lower-tier partnership may still elect for its other qualifying owners) |
| Partnership owner of a partnership / S-corp | NO (tiered partnership exclusion) |
| Other pass-through entity (LLC taxed as partnership) | NO |
| Publicly traded partnership | NO |
| Foreign partner not otherwise subject to CA tax | NO (not subject to CA personal income tax) |

- **Practical consequence of tiered partnership exclusion** — If an upper-tier LLC (taxed as partnership) owns 30% of a lower-tier LLC, the lower tier may still elect PTE — but only the 70% held by individuals / trusts is included in qualified net income. The 30% attributable to the upper-tier partnership is excluded entirely; it gets no PTE tax paid on its behalf and no credit. This significantly weakens the workaround for tiered structures.  _(R&TC § 17052.10(b))_

### 2.3 Consent mechanics

- **Consent mechanics** — Each qualified taxpayer must affirmatively consent on the entity's Form 3804 (Pass-Through Entity Elective Tax Calculation) by signing or being listed as a consenting owner. Consent is owner-by-owner and is annual. A taxpayer may consent in 2024 and not consent in 2025. Consent is irrevocable for the year for which it is given (parallel to the entity-level election irrevocability). A non-consenting owner is not penalized — their distributive share is simply excluded from the PTE computation and they continue to pay California tax through their individual return (Form 540 / 540NR), through composite return inclusion, or through Form 592-PTE nonresident withholding.  _(Form 3804)_

## Section 3 -- Election mechanics

### 3.1 How the election is made

- **Election steps** — The election is made by: 1. Including the election on a timely filed return (including extensions) — Form 100S (S-corps), Form 565 (partnerships), or Form 568 (multi-member LLCs taxed as partnerships) — for the taxable year for which the election applies; AND 2. Filing Form 3804 with that return, listing each consenting qualified taxpayer, their share of qualified net income, and the tax computed; AND 3. Making the required prepayment by June 15 of the taxable year (see Section 5). The election is annual. An entity that elected for 2024 must elect again for 2025 (and pay the required June 15 prepayment) to obtain the benefit for 2025. There is no "evergreen" or "continuing" election.  _(Form 3804)_

### 3.2 Irrevocability and deadlines

- **Irrevocability** — Once made, the election is irrevocable for that taxable year (R&TC § 19902(c)). The entity cannot amend out of the election after the original due date of the return. This is functionally important because: - If the entity later realizes the election was disadvantageous (e.g., owners would have benefited more from the OSTC ordering, or qualified net income was overstated), the entity cannot withdraw. - Conversely, if the entity missed the June 15 prepayment, the election is void for that year and cannot be cured by paying late (see Section 5.2). The entity may still elect for the following year.  _(R&TC § 19902(c))_

### 3.3 Timing of the election decision

- **Timing flexibility and constraint** — Because the election is made on the return (including extensions), an entity has until the extended due date of the entity return to make a final election decision — typically: - S corporations / partnerships: September 15 of the year following the taxable year (calendar-year filers). - LLCs taxed as partnerships (Form 568): September 15 of the year following. However, this flexibility is constrained by the June 15 prepayment rule. The entity must make the June 15 prepayment during the taxable year to preserve the option of electing. Failure to pre-pay by June 15 voids the election even if the entity tries to elect on a September-filed return.

**Practical workflow for tax year 2025**

| Date | Action |
| --- | --- |
| Early 2025 | Estimate qualified net income; identify consenting owners. |
| June 15, 2025 | Mandatory prepayment of greater of $1,000 or 50% of prior-year PTE tax. Use Form 3893 (Pass-Through Entity Elective Tax Payment Voucher). |
| December 31, 2025 | Tax year closes; finalize qualified net income computation. |
| March 15, 2026 | Original due date for Form 100S / 565 / 568 (calendar-year). Final PTE balance due. Election deadline if no extension. |
| September 15, 2026 | Extended due date. Final deadline to make the election. |

### 3.4 Form 3893 vs. Form 3804

- **Distinct FTB forms** — Two distinct FTB forms are involved: - Form 3893 (Pass-Through Entity Elective Tax Payment Voucher) — payment voucher used to remit the June 15 prepayment AND the balance due at filing. There are typically two distinct vouchers per year (one for the current-year prepayment due June 15 of the current taxable year, and one for the balance due / prior-year reconciliation, used with the return). - Form 3804 (Pass-Through Entity Elective Tax Calculation) — calculation schedule attached to the entity's Form 100S / 565 / 568, listing each consenting owner and computing the tax. Form 3804 is the elective mechanism itself. - Form 3804-CR (Pass-Through Entity Elective Tax Credit) — owner-level credit form filed with Form 540 / 540NR / 541 by each consenting owner to claim the credit.  _(Form 3893; Form 3804; Form 3804-CR)_

## Section 4 -- Rate and qualified net income calculation

### 4.1 Rate (R&TC § 19900(a)(2))

- **PTE tax rate** — 9.3%

This rate was chosen because it matches the marginal CA personal income tax rate for the income bracket where many pass-through owners fall (the 9.3% bracket starts at approximately $66,000 of single-filer CA taxable income for 2025). It is below the top marginal CA rate of 12.3% (or 13.3% including the mental health services tax under R&TC § 17043) — meaning owners in the top brackets pay only 9.3% via PTE and reconcile the remaining 3.0–4.0% on their personal return (uncredited). The 9.3% rate is statutory and not indexed.

### 4.2 Qualified net income (R&TC § 19902(b))

- **Qualified net income (QNI)** — Qualified net income (QNI) is the sum, for each consenting qualified taxpayer, of: 1. The taxpayer's distributive share (for partners / members) or pro rata share (for S-corp shareholders) of the entity's income subject to California personal income tax; PLUS 2. Guaranteed payments under IRC § 707(c) made to consenting partners (for 2022 and forward — SB 113 expansion; AB 150 originally excluded guaranteed payments).  _(R&TC § 19902(b))_
- **Apportionment / sourcing** — For a multi-state pass-through entity, QNI is computed by reference to the share of the entity's income that is California-source under R&TC §§ 17951–17955 and the apportionment rules under R&TC §§ 25120 et seq. (as adopted for personal income tax purposes by R&TC § 17743). The CA-source share is the share that flows through to the owner's CA tax base.  _(R&TC §§ 17951–17955; R&TC §§ 25120 et seq.; R&TC § 17743)_
- **Resident vs. nonresident owners** — For a CA-resident consenting owner, QNI includes their entire distributive share regardless of where the entity's income was earned (CA residents are taxed on worldwide income). For a CA-nonresident consenting owner, QNI is limited to the CA-source share of the distributive share.  _(R&TC § 19902(b))_
- **Loss years** — If the entity has a net loss for the year, QNI for each consenting owner is zero (negative QNI is not netted across owners and does not produce a credit). The entity should still file Form 3804 showing zero tax, OR may simply not elect for the loss year.  _(R&TC § 19902(b))_
- **Items excluded from QNI** — Capital gains / losses are included to the extent they enter into the owner's California taxable income (note that California does not have preferential capital gain rates — capital gains are ordinary income for CA purposes). Tax-exempt municipal bond interest is excluded.  _(R&TC § 19902(b))_

### 4.3 Per-owner computation

- **Per-owner PTE tax computation** — For each consenting qualified taxpayer: QNI_i = consenting owner i's distributive share of CA-taxable income (including guaranteed payments to partners); Tax_i = QNI_i × 9.3%. Entity-level PTE tax = sum of Tax_i across all consenting owners.  _(R&TC § 19900(a)(2); R&TC § 19902(b))_
- **Importance of per-owner computation** — This per-owner computation is important because the owner-level credit on Form 3804-CR is each owner's Tax_i, not a pro rata share of the entity total. If owners have unequal CA-source allocations (e.g., a CA-resident 50% partner and a Nevada-resident 50% partner where only 60% of entity income is CA-source), the per-owner credits will differ even though their ownership percentages are equal.

## Section 5 -- Payment schedule

The PTE elective tax has a two-installment payment schedule. Compliance with the first installment is a hard prerequisite for the election; missing it voids the election.

### 5.1 June 15 prepayment (R&TC § 19904)

- **June 15 prepayment amount** — By June 15 of the taxable year (i.e., during the year being taxed, NOT the year after), the entity must pay the greater of: $1,000; OR 50% of the prior taxable year's PTE elective tax.  _(R&TC § 19904)_
- **Calendar-year electing entity specifics** — 2025 prepayment due June 15, 2025, based on greater of $1,000 or 50% of 2024 PTE tax. First-year electors (no prior PTE tax): must still pay $1,000 by June 15 to preserve the option to elect. Re-electors who skipped a year: If the entity elected in 2023 but not in 2024, the "prior taxable year's PTE elective tax" is $0, so the floor is $1,000. The payment is made with Form 3893 (PTE Voucher), mailed or paid electronically via the FTB Web Pay system, or via the entity's tax software with an electronic funds transfer.  _(R&TC § 19904)_

### 5.2 Consequences of missing the June 15 prepayment

- **Voided election if prepayment missed** — Under R&TC § 19904(c), if the entity fails to make the required June 15 prepayment in full, the entity cannot make the PTE election for that taxable year. The election is void. The entity may not cure by paying late. The election is also void if the prepayment is short (e.g., the entity paid $800 thinking the floor was $500). FTB has issued guidance treating any underpayment as voiding the election; do not rely on a "substantial compliance" argument. This is one of the most consequential operational rules in the PTE regime. Reviewer checks at Section 11 emphasize this hard deadline.  _(R&TC § 19904(c))_
- **Mitigation if the deadline is missed** — The entity files its 100S / 565 / 568 without electing PTE. Owners pay tax through their individual returns (Forms 540 / 540NR) and through nonresident withholding (Form 592-PTE) as applicable. The entity may elect for the following taxable year (and must make the June 15 prepayment of the following year — typically a smaller floor of $1,000 since prior-year PTE was $0).  _(R&TC § 19904(c))_

### 5.3 Balance due at original return due date (R&TC § 19904(b))

- **Balance due timing** — The balance of the PTE elective tax (total tax less June 15 prepayment) is due by the original due date of the entity return (without regard to extensions). For calendar-year filers: S corporations (Form 100S): March 15 of the year following the taxable year. Partnerships (Form 565): March 15 of the year following. LLCs taxed as partnerships (Form 568): March 15 (NOTE: the LLC franchise tax of $800 is separately due April 15; the PTE balance is due March 15 for an LLC taxed as a partnership filing Form 568 — verify the entity classification before applying dates). The balance is paid with a second Form 3893 voucher. Late payment of the balance does NOT void the election (only the June 15 prepayment has that consequence), but late payment triggers interest under R&TC § 19101 and may trigger penalties under R&TC § 19132 (late payment penalty) and § 19142 (estimated tax-equivalent underpayment exposure).  _(R&TC § 19904(b); R&TC § 19101; R&TC § 19132; R&TC § 19142)_

### 5.4 Interest and penalties on PTE tax

- **Interest on underpaid PTE tax** — Interest on underpaid PTE tax accrues at the FTB underpayment rate (quarterly adjusted; for 2025, approximately 7–8% — verify at filing time) from the original due date until paid.
- **Late payment penalty** — Late payment penalty under R&TC § 19132 is 5% of the unpaid tax plus 0.5% per month of the unpaid balance, capped at 25%.  _(R&TC § 19132)_
- **No specific PTE estimated-tax penalty** — No specific PTE estimated-tax penalty exists (the June 15 prepayment is not framed as a "safe harbor" calculation; it is a binary election prerequisite).

## Section 6 -- Owner credit (Form 3804-CR)

### 6.1 Mechanics of the credit (R&TC § 17052.10)

- **Credit amount per owner** — Each consenting qualified taxpayer claims a nonrefundable California income tax credit equal to their share of the PTE elective tax paid by the entity. The credit is claimed on the consenting owner's California personal income tax return (Form 540 / 540NR for individuals, Form 541 for trusts and estates) using Form 3804-CR (Pass-Through Entity Elective Tax Credit). Credit amount per owner i = Tax_i = QNI_i × 9.3%.  _(R&TC § 17052.10)_

### 6.2 Nonrefundable + 5-year carryforward

- **Carryforward rule** — The credit is nonrefundable. If the credit exceeds the owner's CA net tax for the year, the excess is carried forward for up to 5 succeeding taxable years (R&TC § 17052.10(b)(2)). Any unused credit after 5 years is lost. The credit cannot be carried back, refunded, transferred, sold, or assigned.  _(R&TC § 17052.10(b)(2))_

This nonrefundability is a meaningful design constraint: if a consenting owner has a CA tax loss year (e.g., large rental losses or NOL absorption) immediately after consenting, the credit may go unused for that year and start its 5-year clock. Practitioners should model whether a consenting owner can absorb the credit before recommending consent.

### 6.3 Ordering rules — PTE credit vs. Other State Tax Credit (OSTC)

- **OSTC interaction overview** — A key technical issue is the interaction between the PTE credit (R&TC § 17052.10) and the Other State Tax Credit (OSTC) under R&TC § 18001 et seq. The OSTC mitigates double taxation when a CA resident pays tax to another state on income also taxed by California.  _(R&TC § 17052.10; R&TC § 18001 et seq.)_
- **SB 113 reordering (2022)** — Effective for tax years beginning on or after January 1, 2022, the PTE credit is applied before other credits with carryover, including the OSTC, in the ordering hierarchy under R&TC § 17039. Specifically: 1. Credits with no carryover and no refund are applied first. 2. The PTE credit is applied before credits with carryover. 3. The OSTC is applied after the PTE credit.  _(R&TC § 17039; SB 113 (2022))_
- **SB 851 OSTC denominator fix (2022)** — To prevent owners from "double-dipping" the PTE credit (claiming the PTE credit against CA tax AND treating the PTE-tax payment as reducing the "net tax" denominator in the OSTC computation), R&TC § 18001 was amended to require taxpayers to add back the PTE credit when computing the "net tax" used in the OSTC formula. This restores the OSTC to the value it would have had absent the PTE election, preventing a windfall.  _(R&TC § 18001; SB 851 (2022))_

The practical effect for a CA-resident owner with income in another PTE-electing state (e.g., NY, NJ, MD): the owner generally gets the PTE credit in CA AND the OSTC for tax paid to the other state, but the OSTC denominator add-back ensures the OSTC is sized as if the CA PTE credit had not been claimed. The owner does not get to claim both the full PTE credit and the full OSTC simultaneously against the same income; the SB 851 mechanism splits them.

### 6.4 No AMT / TMT limitation

- **TMT floor removal** — Originally under AB 150, the PTE credit could only reduce CA tax down to the tentative minimum tax (TMT) under R&TC § 17062, not below. SB 113 removed the TMT limitation effective for 2021 and forward. The PTE credit now reduces CA net tax without a TMT floor, parallel to the treatment of refundable credits even though the PTE credit itself is nonrefundable.  _(R&TC § 17062; SB 113)_

### 6.5 Trust and estate owners

- **Trust/estate credit claim** — A trust or estate that is a consenting qualified taxpayer claims the credit on Form 541 (Fiduciary Income Tax Return), Schedule G. If the trust or estate distributes the underlying PTE income to a beneficiary, the credit generally remains at the trust/estate level (it does NOT pass through to the beneficiary as a separately-stated credit — this contrasts with some other states). Practitioners should review trust DNI mechanics with a fiduciary income tax specialist if the trust is a complex trust with significant distributions.  _(Form 541, Schedule G)_

## Section 7 -- Interactions with other CA taxes

### 7.1 PTE tax is IN ADDITION to LLC franchise tax (Form 568)

- **LLC franchise tax and fee stacking** — For an LLC taxed as a partnership filing Form 568, the PTE elective tax is separate from and in addition to: The $800 annual LLC tax under R&TC § 17941 (Form 3522 or Form 568 Line 2). The LLC fee under R&TC § 17942 (the gross-receipts-based fee on a stepped schedule, capped at $11,790 for total income ≥ $5M).  _(R&TC § 17941; R&TC § 17942)_

A multi-member LLC with $500,000 of CA-source income that elects PTE for two consenting individual owners owes: $800 LLC tax; LLC fee (e.g., $2,500 for income $250k–$499,999; $6,000 for income $500k–$999,999 — verify exact bracket from `ca-smllc-form-568` skill or the FTB schedule); PTE elective tax = $500,000 × 9.3% = $46,500. The $800 LLC tax and LLC fee are entity-level deductions on the federal Form 1065 (reducing flow-through income to owners). The PTE tax is also deductible at the entity level under Notice 2020-75. These are stacking deductions.

### 7.2 PTE tax is IN ADDITION to 1.5% S-corp tax (Form 100S)

- **S-corp tax stacking** — For an S corporation filing Form 100S, the PTE elective tax is separate from and in addition to the 1.5% California S-corp franchise / income tax under R&TC § 23802. (The 1.5% applies to the S-corp's net income; the $800 minimum tax floor also applies.) An S corp with $500,000 of CA net income that elects PTE owes: $7,500 = 1.5% × $500,000 S-corp tax (subject to $800 floor); PTE tax = $500,000 × 9.3% = $46,500. Both are entity-level. Both are deductible federally (the 1.5% under IRC § 164 / Notice 2020-75 treatment for entity-level state income taxes). The owner-level credit on Form 3804-CR is only for the PTE tax (the $46,500), not for the 1.5% S-corp tax (which is a true entity-level franchise tax and does not pass through as an owner credit).  _(R&TC § 23802; IRC § 164)_

### 7.3 Interaction with composite returns and nonresident withholding

- **Composite return exclusivity** — Composite return (Form 540NR Group Return, R&TC § 18535): A nonresident owner included in the entity's composite return is NOT a consenting qualified taxpayer for PTE purposes. The two regimes are mutually exclusive at the owner level for the same income. An owner either consents to PTE OR is included in the composite — not both.  _(R&TC § 18535)_
- **Nonresident withholding interaction** — Nonresident withholding (Form 592-PTE, R&TC § 18662): The entity's PTE prepayment / payment does NOT discharge the entity's nonresident withholding obligation under § 18662. Practically, however, FTB has issued guidance that withholding for a nonresident owner who has consented to PTE may be reduced or waived because the owner's CA tax is being paid through the entity. Practitioners should consult the most current FTB guidance and the Form 592-PTE instructions; this is one of the more operationally confusing intersections.  _(R&TC § 18662)_

### 7.4 Interaction with California estimated tax (Form 540-ES)

- **Estimated tax adjustment** — A consenting owner who expects to receive a PTE credit may reduce their Form 540-ES estimated payments to account for the credit, but should NOT reduce them to zero if the PTE prepayment / balance is not fully made by year-end. The Form 540-ES safe harbor (R&TC § 19136) is computed on the owner's actual CA net tax after credits; if the PTE credit reduces CA net tax appropriately, estimated payments can be sized accordingly. See `ca-540-es-estimated-tax`.  _(R&TC § 19136)_

## Section 8 -- Federal treatment

### 8.1 IRS Notice 2020-75

- **Notice 2020-75 blessing** — On November 9, 2020, the IRS issued Notice 2020-75, blessing entity-level pass-through state income taxes as deductible at the entity level rather than as a separately stated item subject to the $10,000 SALT cap under IRC § 164(b)(6). The Notice provides: "A specified income tax payment made by a partnership or an S corporation during a taxable year does not constitute an item of expense that must be taken into account in computing a partner's or shareholder's separately stated items under section 702(a) of the Code or section 1366(a) of the Code... a specified income tax payment may be deducted by the partnership or S corporation in computing its non-separately stated taxable income or loss for the taxable year of payment." "Specified income tax payment" is defined as a payment by a partnership or S corporation to a state, political subdivision, or DC, in satisfaction of a tax imposed by such jurisdiction on the entity (rather than on the partners/shareholders). The CA PTE elective tax fits this definition.  _(IRS Notice 2020-75; IRC § 164(b)(6))_

### 8.2 Practical federal mechanics

For a 2025 PTE-electing entity: 1. Entity pays PTE tax ($46,500 in the running example). Cash leaves the entity in 2025 (or first half of 2026 for the balance, but only the paid portion is deductible in 2025 — see Section 8.3 on cash vs. accrual timing). 2. Entity deducts PTE tax in computing federal partnership / S-corp ordinary income. The Form 1065 / 1120-S non-separately-stated income decreases by $46,500. 3. Owners' K-1s flow through the reduced ordinary income — each 50/50 owner sees $23,250 less of distributive share / pro rata share on their federal K-1 than they would have absent the election. 4. Owners pay CA PTE elective tax of $0 personally (the entity paid it). They claim the CA Form 3804-CR credit of $23,250 on their CA Form 540 / 540NR. 5. Federal net effect: Each owner's federal AGI decreases by $23,250 × marginal federal rate. For a 37% marginal taxpayer, $23,250 × 37% ≈ $8,602 of federal tax saved — roughly the federal SALT-cap deduction that would otherwise have been lost.

### 8.3 Cash-basis vs. accrual-basis timing

- **Cash-basis entities timing** — Cash-basis entities (most pass-throughs unless they have inventories or gross receipts > the § 448(c) threshold): The PTE tax is deductible federally in the year paid. So the June 15, 2025 prepayment is deductible on the 2025 Form 1065 / 1120-S. The March 15, 2026 balance is deductible on the 2026 Form 1065 / 1120-S — UNLESS paid by December 31, 2025.  _(IRC § 448(c))_

Many CA-PTE-electing entities accelerate the balance payment into December of the taxable year to capture the full federal deduction in the same year. The June 15 prepayment plus a December "true-up" payment effectively front-loads the deduction.

- **Accrual-basis entities** — The PTE tax is deductible in the year to which it relates (assuming the all-events test under Treas. Reg. § 1.461-1 is met). Most pass-throughs are not accrual basis, so this is uncommon.  _(Treas. Reg. § 1.461-1)_

### 8.4 No federal owner credit / pickup

- **No federal pass-through of PTE deduction** — The PTE tax paid by the entity is not a separately stated item on the federal K-1 that owners pick up. Owners do not claim a federal deduction for "state income tax paid by the partnership" — the deduction was already captured at the entity level. Owners also do not include the PTE tax in their personal federal Schedule A SALT deduction (because they did not personally pay it). The owner's CA Form 3804-CR credit is purely a state-level item; it has no federal counterpart.

### 8.5 Section 461(l) excess business loss limitation

- **Excess business loss interaction** — The reduction of flow-through ordinary income by the PTE tax does affect the computation of excess business losses under IRC § 461(l) (which limits net business losses for individual taxpayers to $313,000 / $626,000 MFJ for 2025, indexed). For loss-year electing entities the math reverses, but in practice loss-year entities typically do not elect.  _(IRC § 461(l))_

## Section 9 -- Sunset and legislative outlook

### 9.1 Statutory sunset

- **Sunset date** — AB 150 enacted the PTE elective tax for taxable years beginning on or after January 1, 2021, and before January 1, 2026. R&TC § 19906 provides an explicit operative-period limitation. This means: Tax year 2025 is the LAST scheduled year of the regime under current statute (for calendar-year entities, the year ending December 31, 2025). Tax year 2026 and forward: Absent legislative extension, the regime expires. Entities will not be able to elect for tax year 2026.  _(R&TC § 19906)_

### 9.2 Linkage to federal SALT cap

- **Federal SALT cap linkage** — The PTE regime is economically motivated by the federal $10,000 SALT cap under IRC § 164(b)(6), which itself was originally enacted by the Tax Cuts and Jobs Act (TCJA) for tax years 2018–2025. The TCJA SALT cap was set to expire after 2025. Federal legislation in mid-2025 modified the SALT cap going forward (the One Big Beautiful Bill Act, P.L. 119-21, July 4, 2025 — verify exact post-2025 SALT cap mechanics from the federal `us-tax-workflow-base` skill). Whether California extends AB 150 depends partly on whether the federal SALT cap continues. If the federal cap survives at $10,000 (or some higher level), state pressure to maintain the PTE workaround continues. If the federal cap is repealed entirely, the workaround loses its purpose.  _(IRC § 164(b)(6); P.L. 119-21)_

### 9.3 Legislative status (as of the last_updated date of this skill)

As of November 15, 2025: No California legislation has been enacted to extend AB 150 beyond December 31, 2025. Trailer-bill negotiations in mid-2025 considered extension but did not enact it. Tax practitioners and major firms anticipate either (a) a clean extension in early 2026 with retroactive effect to January 1, 2026, or (b) a re-architected regime if the federal SALT cap materially changes.

**Reviewer guidance for tax year 2025 returns:** Proceed with PTE election as normal — the regime is fully operative for 2025. For 2026 estimated tax planning, do not assume PTE will be available in 2026. Build the owner's 2026 estimated tax baseline assuming no PTE workaround (full individual-level CA tax). If a 2026 extension passes, adjust mid-year.

**Reviewer flag for any 2026-forward planning advice:** This skill explicitly does NOT opine on post-2025 availability. Any taxpayer plan that depends on 2026 PTE availability must include an "if-extended" alternative scenario and a written caveat about legislative uncertainty.

## Section 10 -- Worked examples

### 10.1 Example A: Two-member LLC, both CA residents, equal partners

ABC Software LLC, a CA LLC taxed as a partnership (Form 568). Two members: Alex (CA resident, 50%) and Brooke (CA resident, 50%). Both individuals. 2025 CA-source ordinary income: $500,000. Both members consent to PTE.

**Computation**

| Step | Amount |
| --- | --- |
| Qualified net income — Alex | $250,000 |
| Qualified net income — Brooke | $250,000 |
| Total QNI | $500,000 |
| PTE tax rate | 9.3% |
| **Total PTE tax** | **$46,500** |
| Alex's credit (Form 3804-CR) | $23,250 |
| Brooke's credit (Form 3804-CR) | $23,250 |

**Payment schedule**

| Date | Action | Amount |
| --- | --- | --- |
| June 15, 2025 | First-year election; floor is $1,000 (no prior PTE). Practitioner electing the safe approach pays $1,000. | $1,000 |
| December 31, 2025 | Optional: accelerate balance to maximize federal deduction in 2025. | $45,500 |
| March 15, 2026 | If not paid in December, balance due. | $45,500 |
| March 15, 2026 | LLC tax ($800) and LLC fee due. | $800 + LLC fee |

Form 1065 ordinary income reduced by $46,500 PTE tax + $800 LLC tax + LLC fee. Each K-1 reflects 50% of the reduced ordinary income. Each owner's federal AGI lower by approximately $23,650 (their 50% share of the entity-level state deductions).

Each owner files Form 540 (CA resident return) including Form 3804-CR. Each owner's Form 540 reports their $250,000 distributive share (note: CA does NOT adopt the Notice 2020-75 federal reduction at the owner level — for CA personal income tax purposes, the owner is taxed on the full $250,000 of CA-source income, then claims the $23,250 PTE credit as an offset against CA net tax).

Federal SALT cap workaround captured; California tax economically the same as without the election (paid via PTE rather than via personal income tax).

### 10.2 Example B: S corporation, one CA resident shareholder and one nonresident shareholder

XYZ Consulting Inc., a CA S-corp (Form 100S). Two shareholders: Chris (CA resident, 60%) and Dana (Nevada resident, 40%). Both individuals. 2025 federal S-corp ordinary income: $400,000. CA apportionment factor: 75% (i.e., $300,000 CA-source). Both shareholders consent to PTE.

**Computation**

| Step | Amount |
| --- | --- |
| Chris's pro rata share — federal | $240,000 (60% × $400,000) |
| Chris's pro rata share — CA-source | $180,000 (60% × $300,000) |
| BUT: Chris is a CA resident, so taxed on full $240,000 — wait, this is per-owner-by-residency. |  |
| Chris's QNI (CA resident — full distributive share) | $240,000 |
| Dana's pro rata share — federal | $160,000 |
| Dana's pro rata share — CA-source (nonresident — limited to CA-source) | $120,000 (40% × $300,000) |
| Dana's QNI (nonresident — CA-source only) | $120,000 |
| Total QNI | $360,000 |
| PTE tax rate | 9.3% |
| **Total PTE tax** | **$33,480** |
| Chris's credit | $22,320 ($240,000 × 9.3%) |
| Dana's credit | $11,160 ($120,000 × 9.3%) |

This computation illustrates a frequently-misunderstood point: for a CA-resident consenting owner of a multi-state pass-through, QNI is the FULL distributive share (because CA taxes residents on worldwide income), not just the CA-apportioned share. For a nonresident consenting owner, QNI is limited to the CA-apportioned share. This produces apparently-asymmetric tax-per-percent-ownership outcomes that are correct and intended.

Dana, as a Nevada resident, is taxed by CA only on her CA-source $120,000. She must file Form 540NR to claim the $11,160 PTE credit. If her only CA-source income is the $120,000 from the S-corp, her CA tax on $120,000 at graduated rates is approximately $7,000–$8,000 (varies with deductions / exemptions); the $11,160 credit fully covers her CA tax AND leaves about $3,000–$4,000 of carryforward credit. Because the credit is nonrefundable, Dana cannot get the excess as a refund. The carryforward expires after 5 years if Dana has no further CA-source income. Important practical implication: Nonresident owners can over-pay through PTE if their CA-source share is small relative to the tax computed by the entity. The PTE election may still be net-positive for them (because the federal SALT-cap savings often exceed the trapped credit), but a careful owner-by-owner analysis is required.

### 10.3 Example C: Tiered partnership — upper-tier LLC owns 30%, individuals own 70%

DEF Holdings LLC (the lower tier), a CA LLC taxed as a partnership (Form 568). Members: Upper Tier Capital LLC (a multi-member LLC taxed as partnership, owns 30%) and seven individual members (CA residents, each owning 10%). 2025 CA-source ordinary income: $1,000,000. All seven individuals consent. Upper Tier Capital LLC is ineligible.

**Computation**

| Step | Amount |
| --- | --- |
| Total entity CA-source income | $1,000,000 |
| Share owned by ineligible upper-tier partnership | 30% → $300,000 (EXCLUDED) |
| Share owned by consenting individuals | 70% → $700,000 |
| Qualified net income | $700,000 |
| PTE tax | $700,000 × 9.3% = $65,100 |
| Credit per consenting individual (10% each) | $9,300 |

The $300,000 attributable to Upper Tier Capital LLC pays no PTE tax. Those dollars flow through to Upper Tier as ordinary income on the K-1; Upper Tier in turn distributes to its own members, who pay CA tax through their personal returns and bear the federal SALT-cap pain. The PTE workaround captures only 70% of the lower-tier entity's economic activity. A planning note: if the upper-tier ownership can be restructured (e.g., upper tier converts to S-corp, or upper tier's owners receive their interest directly), more of the lower tier's income becomes PTE-eligible. This is a multi-year, multi-entity planning question.

### 10.4 Example D: Disregarded SMLLC owned by an individual, member of a partnership

GHI Partners, a multi-member CA LLC taxed as a partnership. One of the members is "Erin Single LLC," a CA SMLLC disregarded for federal tax purposes, wholly owned by Erin (a CA-resident individual). Erin Single LLC owns 25% of GHI Partners. GHI 2025 CA-source income: $800,000. Erin Single LLC's distributive share: $200,000.

Can Erin (through her SMLLC) consent to PTE at GHI Partners level?

- **Answer** — YES, by virtue of SB 113. The SB 113 amendment to R&TC § 17052.10 expressly admits as a qualified taxpayer "a disregarded business entity, and its partners or members, that is a partner, shareholder, or member of an electing qualified entity," provided the underlying owner is an individual, fiduciary, estate, or trust. Erin (the individual) is the qualified taxpayer; Erin's SMLLC is the conduit on the K-1.  _(R&TC § 17052.10; SB 113)_

Erin's QNI = $200,000. PTE tax on Erin's share = $200,000 × 9.3% = $18,600. Erin claims the $18,600 credit on her Form 540 (Form 3804-CR), even though her K-1 was issued to "Erin Single LLC."

Form 3804 should list Erin (the individual) as the consenting qualified taxpayer, with the SMLLC noted as the disregarded conduit. Practitioners sometimes incorrectly list the SMLLC as the consenting party; this triggers FTB matching issues because the SMLLC has no CA personal income tax account. Always list the underlying individual.

### 10.5 Example E: Part-year resident consenting owner

JKL Studios LLC, a CA LLC taxed as a partnership. One member: Fei, who was a CA resident for the first 6 months of 2025 and moved to Washington State on July 1, 2025. Fei's 2025 distributive share from JKL: $300,000, of which $180,000 was earned by the partnership while Fei was a CA resident (Jan–June) and $120,000 while Fei was a WA resident (July–Dec). Assume all of JKL's income is CA-source (so apportionment is 100% to CA).

- **Computation** — For part-year residents, R&TC § 17041(b) prorates the CA tax base. For PTE purposes, the question is: what is Fei's QNI? During Jan–June: Fei is a CA resident, taxed on worldwide distributive share. QNI portion = $180,000. During July–Dec: Fei is a WA nonresident; taxed by CA only on CA-source share, which is 100% in this example. QNI portion = $120,000. Total QNI for Fei = $300,000 (because all entity income was CA-source, the residence-period analysis happens to coincide with the apportionment analysis). PTE tax = $300,000 × 9.3% = $27,900. Fei files Form 540NR (part-year resident return) and claims the $27,900 credit.  _(R&TC § 17041(b))_

Suppose JKL's CA apportionment factor were 70% (not 100%), and the entity earned ratably throughout the year. Jan–June (Fei is CA resident): Fei's distributive share = $150,000 of $300,000, but worldwide-taxed → QNI = $150,000. July–Dec (Fei is WA nonresident): Fei's distributive share = $150,000, but only 70% CA-source → QNI = $105,000. Total QNI for Fei = $255,000, PTE tax = $23,715. This calculation is technically nuanced and requires verifying which day-by-day or month-by-month allocation method the entity uses. The standard approach is the "ratable" / "interim closing" method; entities with seasonal income (e.g., a project that closed in March before Fei moved) may use a closing-of-the-books approach.

## Section 11 -- Common errors and reviewer checks

The following checks should be completed for every PTE election engagement. They reflect FTB enforcement patterns and the most common practitioner errors observed in the first four years of the regime.

- **Check 301** — June 15 prepayment timely and full. Verify the prepayment was made by June 15 of the taxable year (not the year after) in the correct amount (greater of $1,000 or 50% of prior-year PTE tax). A short payment voids the election. Confirm Form 3893 voucher reference matches the FTB cashed check / EFT confirmation.  _(R&TC § 19904)_
- **Check 302** — Prior-year PTE tax correctly computed for the 50% floor. If the entity elected in the prior year, the floor is the higher of $1,000 or 50% of that prior-year tax. Verify by pulling the prior-year Form 3804.  _(Form 3804)_
- **Check 303** — All consenting owners are eligible qualified taxpayers. Each consenting owner must be an individual, fiduciary, estate, trust, or disregarded SMLLC owned by an individual. Verify by reviewing each owner's federal classification (Form W-9 or K-1 detail). A C-corporation or partnership owner inadvertently listed on Form 3804 invalidates that line item (not necessarily the whole election, but creates an FTB inquiry).  _(Form 3804)_
- **Check 304** — Form 3804 ties to entity return. The total PTE tax on Form 3804 should match the entity's "PTE tax paid" line on Form 100S, Form 565, or Form 568. The sum of per-owner credits on Form 3804 should equal entity-level PTE tax.  _(Form 3804)_
- **Check 305** — Each consenting owner has a corresponding Form 3804-CR. When preparing the owner-level 540 / 540NR, verify the owner is claiming exactly the credit shown on Form 3804 for that owner (and that the entity's EIN / CA Secretary of State number is correctly cross-referenced on Form 3804-CR).  _(Form 3804-CR)_
- **Check 306** — Nonresident-owner QNI uses CA-source share only. For each nonresident consenting owner, verify QNI was computed using the CA-apportioned share, not the worldwide distributive share. This is the single most common substantive error.
- **Check 307** — Resident-owner QNI uses full distributive share. For each CA-resident consenting owner, verify QNI was computed using the worldwide distributive share, not just CA-apportioned. This is the mirror error of Check 306.
- **Check 308** — Guaranteed payments included in partner QNI (2022 forward). For partnerships, verify that any guaranteed payments under IRC § 707(c) to consenting partners are included in QNI. SB 113 added these for years beginning in 2022 and forward.  _(IRC § 707(c); SB 113)_
- **Check 309** — Tiered partnership exclusion enforced. If any owner is itself a partnership or LLC taxed as partnership (not a disregarded SMLLC owned by an individual), verify that owner is excluded from Form 3804 entirely.  _(Form 3804)_
- **Check 310** — Election made on a timely (with extension) return. Verify the entity return was filed by the extended due date (typically September 15 of the year following the taxable year). A late entity return forfeits the election even if June 15 prepayment was made.
- **Check 311** — PTE balance paid (no late penalty exposure). Verify the balance due was paid by the original due date (typically March 15 of the year following). Late payment triggers interest and penalties but does not void the election.
- **Check 312** — Owner credit carryforward tracked. For each consenting owner, if the PTE credit exceeds CA net tax for the year, verify the carryforward is recorded on the owner's CA tax workpapers with a 5-year expiry calendar.
- **Check 313** — OSTC ordering correct. For CA-resident owners with out-of-state income, verify the PTE credit is applied before the OSTC and that the SB 851 add-back is applied in the OSTC denominator.  _(SB 851)_
- **Check 314** — Federal Notice 2020-75 deduction taken at entity level. Verify the federal Form 1065 / 1120-S deducts the PTE tax paid in 2025 as a Notice 2020-75 specified income tax payment, reducing non-separately-stated taxable income.  _(IRS Notice 2020-75)_
- **Check 315** — Federal deduction timing matches cash basis. Verify only PTE tax paid by December 31, 2025 is deducted on the 2025 federal return. The March 15, 2026 balance, if not pre-paid by 12/31/25, is deducted on the 2026 federal return.
- **Check 316** — Entity is NOT a publicly traded partnership. Confirm by reviewing the entity's federal classification and any PTP listing.
- **Check 317** — Entity is NOT a disregarded SMLLC trying to elect at its own level. A SMLLC disregarded federally cannot itself elect; verify the entity files Form 1065 or Form 1120-S federally.
- **Check 318** — Consenting owners affirmatively consented. Review the consent log / Form 3804 signature mechanics. FTB has, in audit, requested evidence of owner consent (operating agreement amendments, signed consent forms, or written attestations).  _(Form 3804)_
- **Check 319** — Composite return mutual exclusion. Verify that no consenting PTE owner is also included in a Form 540NR Group Return for the same year.
- **Check 320** — Nonresident withholding (Form 592-PTE) reconciled. Verify the entity's nonresident withholding for any consenting nonresident owner is appropriately reduced or waived per current FTB guidance, and that any withholding paid is properly credited on the nonresident's Form 540NR (in addition to the PTE credit).  _(Form 592-PTE)_
- **Check 321** — Sunset disclosure to client. Verify the client has been advised in writing that PTE may not be available for tax year 2026 absent legislative action, and that 2026 estimated tax planning should assume non-availability as the conservative baseline.
- **Check 322** — Trust / estate credit not pushed to beneficiaries. If the consenting owner is a trust or estate, verify the credit is claimed at the trust/estate level on Form 541 and is not separately stated to beneficiaries on Schedule K-1 (541) unless specifically supported.  _(Form 541)_
- **Check 323** — Net loss year handled. If the entity has a net loss, verify that no PTE election was made (or, if made, that QNI is reported as zero for each owner). Confirm no credit is generated from a loss year.
- **Check 324** — SMLLC-owned-by-individual disclosure on Form 3804. When a consenting owner is an SMLLC, verify Form 3804 lists the underlying individual (not the SMLLC) as the consenting party, with the SMLLC noted as the conduit.  _(Form 3804)_
- **Check 325** — Part-year resident QNI correctly bifurcated. For any consenting part-year resident, verify the residency-period-vs-nonresidency-period bifurcation of QNI per Section 10.5.

## Section 12 -- Output specification

For each PTE elective tax engagement, this skill produces:

1. Eligibility memo: Confirmation that the entity is a qualified entity and listing of which owners are qualified taxpayers (with reasons for any exclusion).
2. Consent register: Per-owner consent status, with copies of consent documentation.
3. Form 3804 (entity-level calculation): Per-owner QNI and tax, total entity PTE tax.
4. Form 3893 payment vouchers: June 15 prepayment voucher (year of the taxable year) and balance-due voucher (year after).
5. Form 3804-CR (per consenting owner): Owner's credit amount, attached to the owner's Form 540 / 540NR / 541 workpapers.
6. Federal deduction memo: Notice 2020-75 specified income tax payment deduction on Form 1065 / 1120-S, with cash-basis timing.
7. Cross-skill handoffs:
   - To `ca-540-individual-return` / `ca-540-es-estimated-tax`: PTE credit amount for each owner, OSTC interaction (if applicable), 2025 estimated tax adjustment.
   - To `us-federal-return-assembly`: Entity-level PTE deduction, reduced K-1 flow-throughs.
   - To `us-s-corp-election-decision`: PTE benefit as an input to the S-corp break-even analysis (when applicable).
8. Reviewer brief: Sections 11 checks completed, sunset disclosure included, signed off by reviewer.

## Section 13 -- Cross-skill references

Inputs from:
- `us-sole-prop-bookkeeping` / entity-level bookkeeping — entity's CA-source ordinary income, apportionment factor.
- `us-schedule-c-and-se-computation` — N/A directly (sole props are ineligible); informational only.
- Prior-year Form 3804 — for 50% prior-year floor computation.
- Entity operating agreement / shareholder agreement — for ownership percentages and consent mechanics.

Outputs to:
- `ca-540-individual-return` — PTE credit on Form 3804-CR per consenting owner.
- `ca-540-es-estimated-tax` — adjusted owner estimated tax baseline.
- `ca-smllc-form-568` — for multi-member 568 PTE-electing entities (note that skill is SMLLC-only; this skill provides the multi-member 568 PTE flow).
- `us-federal-return-assembly` — entity-level Notice 2020-75 deduction.
- `us-ca-return-assembly` — final unified package for taxpayer.

## Section 14 -- Known gaps and uncertainty flags

1. Post-2025 availability is uncertain. As of the last_updated date, no legislative extension has been enacted. Practitioners must NOT assume PTE will be available in tax year 2026 or later. Conservative 2026 planning baseline = no PTE.
2. Federal SALT cap post-2025 mechanics. The interaction with the post-2025 federal SALT cap (as modified by P.L. 119-21, the One Big Beautiful Bill Act of July 4, 2025) requires verification at filing time. The economic motivation for the PTE election depends on the surviving federal cap level.
3. FTB underpayment interest rate for 2025 quarters must be verified at filing time for any late-PTE-balance interest computation.
4. Form 592-PTE nonresident withholding waiver mechanics for consenting nonresident owners are based on FTB administrative guidance; verify the most current FTB Notice or Form 592-PTE instructions at filing time.
5. Tiered partnership planning (e.g., restructuring upper-tier ownership to maximize PTE eligibility) is multi-year, multi-entity, and not fully detailed here. Refer to a dedicated entity-restructuring workflow.
6. Trust DNI / credit-passthrough rules for complex trusts are summarized only; complex fiduciary income tax matters require specialist review.
7. California conformity to Notice 2020-75 at the entity level for state-tax-base purposes is not the same question — CA does not allow the entity to deduct PTE tax in computing the entity's own CA tax base (because the PTE tax IS the CA tax). Federal conformity for federal-base purposes is the relevant point.

### Change log

v0.1 (November 2025): Initial content skill covering eligibility, election mechanics, 9.3% rate, June 15 prepayment, owner credit on Form 3804-CR, OSTC ordering, federal Notice 2020-75 treatment, sunset uncertainty, and five worked examples.

## End of skill

## Provenance & attribution

This skill is authored by the Open Accountants project and is intended for use by credentialed tax professionals (Enrolled Agents, CPAs, attorneys admitted to practice under Circular 230) reviewing California pass-through entity tax matters. Statutory and form references are drawn from:

- California Revenue and Taxation Code (R&TC), Division 2, Part 10 (Personal Income Tax) and Part 10.4 (Pass-Through Entity Elective Tax), as amended through 2025.
- California Franchise Tax Board (FTB) forms and instructions: Form 3804 (Pass-Through Entity Elective Tax Calculation), Form 3804-CR (Pass-Through Entity Elective Tax Credit), Form 3893 (Pass-Through Entity Elective Tax Payment Voucher), Form 100S (S Corporation Tax Return), Form 565 (Partnership Return of Income), Form 568 (Limited Liability Company Return of Income), Form 592-PTE, Form 540, Form 540NR, Form 541.
- AB 150 (2021 Cal. Stat. ch. 82), SB 113 (2022 Cal. Stat. ch. 3), SB 851 (2022 Cal. Stat. ch. 705).
- IRS Notice 2020-75 (November 9, 2020).
- IRC §§ 164(b)(6), 461(l), 702, 707(c), 1366, 7704.

The verified, country-signed-off version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Verification model: lead California accountant signs off, with optional contributing reviewers, per the multi-accountant-per-jurisdiction governance model. Pending verification status as of v0.1; awaiting review by a California-licensed CPA or Enrolled Agent with PTE experience.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
