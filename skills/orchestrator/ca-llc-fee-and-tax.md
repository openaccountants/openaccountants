---
name: ca-llc-fee-and-tax
description: Tier 2 California content skill for Form 568 — the $800 annual minimum tax (R&TC § 17941) plus the tiered LLC fee on gross receipts (§ 17942). Covers every LLC classified as a partnership or disregarded entity that is organized, registered, or doing business in California, the four fee brackets at $250k / $500k / $1M / $5M of total income from all sources reportable to California, the Form 3522 ($800 minimum tax voucher) due April 15 and the Form 3536 (estimated LLC fee voucher) due June 15, disregarded SMLLC treatment, multi-member partnership filings, the corporation election carve-out, and economic / doing-business nexus under the § 23101 factor presence test. Tax year 2025.
jurisdiction: US-CA
domain: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ca-llc-fee-and-tax

## California LLC Annual Tax & Fee — Form 568, 3522, 3536

> **Reviewer warning.** This skill is a content reference for an Enrolled Agent, CPA, or California attorney to consume when preparing or reviewing a California LLC filing. It is **not** legal advice and must **not** be delivered to the taxpayer without credentialed review. Every output produced under this skill must be reviewed and signed by a Circular 230 practitioner (federal) and a California-licensed preparer (CTEC-registered or higher). The Franchise Tax Board (FTB) is the controlling authority; nothing in this skill overrides published FTB guidance, the California Revenue and Taxation Code (R&TC), or California Code of Regulations Title 18.

## 1. Scope

### 1.1 In scope

- **Two-pronged entity-level liability** — This skill covers the **two-pronged** California entity-level liability imposed on every LLC that is either organized in California, registered with the California Secretary of State (SOS) as a foreign LLC, or doing business in California within the meaning of R&TC § 23101: 1. The $800 annual minimum franchise tax under R&TC § 17941. 2. The tiered LLC fee on total income from all sources reportable to California under R&TC § 17942.  _(R&TC § 17941; R&TC § 17942; R&TC § 23101)_
- **Reporting forms** — Together these are reported on Form 568, Limited Liability Company Return of Income, with the $800 prepaid on Form 3522 (LLC Tax Voucher) and the LLC fee estimated on Form 3536 (Estimated Fee for LLCs). The skill is written for the 2025 tax year (returns filed in 2026) and presumes the LLC has not elected to be taxed as a corporation.  _(Form 568; Form 3522; Form 3536)_

**Federal classification vs California return**

| Federal classification | California return | $800 tax owed? | LLC fee owed? |
| --- | --- | --- | --- |
| Disregarded single-member LLC | Form 568 (single-member filing) | Yes | Yes |
| Partnership (2+ members) | Form 568 (partnership filing) + Sch K-1 (568) | Yes | Yes |
| C-corporation (Form 8832 election) | Form 100 | Yes ($800 minimum on Form 100) | **No** |
| S-corporation (Form 2553 election) | Form 100S | Yes ($800 minimum on Form 100S; plus the 1.5% S-corp tax) | **No** |

### 1.2 Out of scope (refusal catalogue)

The following situations require the reviewer to draft from primary authority — this skill must decline to produce a numeric output and route the matter:

- **R-CA-LLC-1** — LLPs (limited liability partnerships) — separate $800 regime under § 17948.  _(R&TC § 17948)_
- **R-CA-LLC-2** — Series LLCs — each protected series is treated as a separate LLC owing $800 under FTB Notice 2009-04; this skill covers single-shell LLCs only.  _(FTB Notice 2009-04)_
- **R-CA-LLC-3** — Investment partnerships and qualifying investment securities — the § 17955 carve-out from "doing business" for nonresident members.  _(R&TC § 17955)_
- **R-CA-LLC-4** — LLCs in a unitary combined-reporting group with a corporate parent.
- **R-CA-LLC-5** — LLCs that received a § 23114 first-year exemption under former AB 85 / SB 818 for tax years 2021–2023. Closing-out and short-year arithmetic for those years requires reviewer-drafted computation; this skill states the rule but does not produce a number.  _(R&TC § 23114; AB 85; SB 818)_
- **R-CA-LLC-6** — Cannabis LLCs subject to the cannabis excise tax and CDTFA cannabis tax — sales-side issues live in `ca-sales-use-tax.md`.
- **R-CA-LLC-7** — Real-estate LLCs holding properties subject to Prop 13 base-year reassessment under R&TC § 64(c)/(d).  _(R&TC § 64(c)/(d))_
- **R-CA-LLC-8** — LLCs claiming an § 17942(b)(3) "small business deduction" or the disaster-relief postponements — verify against current FTB notices, do not assume.  _(R&TC § 17942(b)(3))_
- **R-CA-LLC-9** — Pass-Through Entity Elective Tax (AB 150) — the 9.3% PTET election is in scope of the separate `ca-pte-elective-tax.md` skill; this skill notes the interaction only.  _(AB 150)_
- **R-CA-LLC-10** — Final / short-period returns triggered by mid-year dissolution, conversion, or merger — these require reviewer-drafted apportionment of the $800 and the LLC fee bracket.

If the engagement touches any of R-CA-LLC-1 through R-CA-LLC-10, the reviewer drafts the position from primary authority and the skill output is limited to the unaffected portions.

## 2. Who must file Form 568

### 2.1 The trigger — three independent gates

- **Gate A — Organized in California** — The LLC was formed by filing Form LLC-1 (Articles of Organization) with the California Secretary of State. Once organized, the LLC owes $800 every year until it dissolves via Form LLC-3 or LLC-4/7, regardless of activity.
- **Gate B — Registered as a foreign LLC** — The LLC was organized in another state but has registered with the California SOS as a foreign LLC (Form LLC-5). Registration alone is enough to trigger annual $800 liability.
- **Gate C — Doing business under R&TC § 23101** — Even without SOS organization or registration, an LLC is "doing business" if any of the following is true (the factor presence test, § 23101(b)): the LLC is organized or commercially domiciled in California; or California sales exceed the lesser of $735,019 (2025 indexed threshold — confirm current-year figure on FTB.ca.gov; see § 4.4 below) or 25% of total sales; or California real property and tangible personal property exceed the lesser of $73,502 (2025) or 25% of total real and tangible property; or California compensation paid exceeds the lesser of $73,502 (2025) or 25% of total compensation; or the LLC actively engages in any transaction in California "for the purpose of financial or pecuniary gain or profit" (§ 23101(a)) — a low bar.  _(R&TC § 23101(a); R&TC § 23101(b))_
- **2025 thresholds (FTB-indexed under § 23101(b)(4))** — $735,019 (sales), $73,502 (property), $73,502 (payroll)  _(R&TC § 23101(b)(4))_

> **2025 thresholds (FTB-indexed under § 23101(b)(4)).** The published 2025 amounts are $735,019 (sales), $73,502 (property), and $73,502 (payroll). The reviewer must verify against the FTB's current "Doing Business in California" indexing notice before relying on these figures — the prompt-issuer's draft used the 2024 figure of $711,538, which is now stale.

Once Gate C is met, the LLC is liable for the $800 and the LLC fee even if it never registered with the SOS. The FTB issues a "Notice of Tax Due" via its non-filer enforcement program, and the LLC is also exposed to the SOS-registration penalty under Corporations Code § 17708.07 ($2,000 + back franchise taxes + interest).

### 2.2 Filing duty survives revenue collapse

- **$800 not tied to profitability** — The $800 minimum is not a function of profitability or activity. An LLC organized in California in 2019 that has had zero revenue and zero activity since 2022 still owes $800 every year until it files dissolution paperwork with both the SOS (Form LLC-3 / LLC-4-7 / LLC-4-8) and the FTB. The FTB will not stop billing until the SOS confirms cancellation and the LLC has filed a final Form 568 marked "Final Return."

### 2.3 Filing deadline

- **Form 568 due date and extension** — Form 568 is due the 15th day of the 3rd month after the close of the LLC's tax year. For a calendar-year LLC, that is March 15, 2026 for the 2025 return. The automatic 7-month extension (Form 3537 paper, or automatic e-file extension) moves the filing deadline to October 15, 2026, but does not extend the payment deadline for any of the $800 or the LLC fee — those remain due on their original dates (see § 6).

## 3. The $800 annual minimum franchise tax — mechanics

### 3.1 Statutory basis

- **Annual $800 minimum tax, stacks with fee** — R&TC § 17941 imposes an annual tax of $800 on every LLC subject to California tax for the privilege of doing business in California. It is structured as a minimum tax: the LLC owes $800 even if its computed fee under § 17942 is $0. The two amounts stack; they are not alternatives.  _(R&TC § 17941)_

### 3.2 Due date and form

- **$800 minimum tax due date** — 15th day of the 4th month of tax year N — i.e., April 15, 2025 for a calendar-year LLC's 2025 liability, paid on Form 3522 (LLC Tax Voucher). The taxpayer pays this prospectively, before the tax year ends. The Form 568 filed in 2026 then reconciles the prepayment.  _(Form 3522)_

> **The voucher year is the tax year, not the filing year.** The 2025 Form 3522 paid on April 15, 2025 covers the 2025 tax year. The 2024 Form 3522 was due April 15, 2024 and covered 2024. The 2026 Form 3522 will be due April 15, 2026 and covers 2026. Misalignment between voucher year and tax year is the single most common cause of duplicate FTB billing notices; verify the year written on the voucher against the year being paid.

### 3.3 First-year status — AB 85 / SB 818 (expired)

- **AB 85 / SB 818 waiver expired** — For tax years 2021, 2022, and 2023 only, AB 85 (2020) and SB 818 (2021) waived the $800 first-year minimum tax for LLCs, LPs, and LLPs newly organized or registered in California. The waiver expired for tax years beginning on or after January 1, 2024. As currently enacted, an LLC formed on or after January 1, 2024 owes the full $800 for its first short year, due by the 15th day of the 4th month after formation.  _(AB 85 (2020); SB 818 (2021))_

The legislature has periodically considered extending the waiver (AB 1432 in 2023 died in committee; subsequent proposals have not advanced as of this skill's last update). The reviewer must check the FTB's "Annual Tax — Limited Liability Companies" page for any extension before relying on the expiration.

### 3.4 The "15-day rule" — § 17946 / § 17941(f)

- **15-day rule for $0 short year** — An LLC that (a) files its Articles of Organization or Application to Register in the last 15 days of its tax year and (b) conducts no business during those 15 days owes $0 for that short year. The next full tax year is its "first" year for AB 85 / SB 818 purposes.  _(R&TC § 17946; R&TC § 17941(f))_
- **Calendar-year example** — For a calendar-year LLC, "last 15 days" means December 17 through December 31. An LLC organized on December 18, 2025 with no activity by December 31, 2025 owes no 2025 $800. Its first $800 voucher is due April 15, 2026 for the 2026 tax year.
- **Fiscal-year application** — The 15-day rule applies to non-calendar fiscal years by reference to the LLC's tax-year end. A fiscal-year LLC with a June 30 year-end that is organized June 17 owes nothing for the 14-day short year ending June 30, but owes $800 for the next full year starting July 1.

### 3.5 No proration for partial years

- **No proration outside 15-day window** — The $800 is not prorated for short years that fall outside the 15-day rule. An LLC organized on December 16, 2025 — one day outside the 15-day window — owes the full $800 for the 16-day stub year, due April 15, 2026 (because the first $800 falls due in the 4th month after the start of the tax year, and the stub year ends December 31, 2025).

## 4. The LLC fee — tiered schedule on total income (§ 17942)

### 4.1 The fee schedule (R&TC § 17942(a))

**Total income from all sources reportable to California — Fee**  _(R&TC § 17942(a))_

| Total income from all sources reportable to California | Fee |
| --- | --- |
| Less than $250,000 | $0 |
| $250,000 — $499,999 | **$900** |
| $500,000 — $999,999 | **$2,500** |
| $1,000,000 — $4,999,999 | **$6,000** |
| $5,000,000 or more | **$11,790** |

- **Flat fee per bracket, not indexed** — The fee is a flat amount per bracket, not a percentage. An LLC with $250,001 of total income owes the same $900 as one with $499,999. The schedule has been at these dollar amounts since 2008 and is not indexed for inflation.  _(R&TC § 17942(a))_

### 4.2 "Total income from all sources reportable to California" — the definition trap

- **Total income definition** — The fee base is not federal gross receipts, not federal gross income, and not Schedule C line 1. § 17942(b)(1)(A) defines "total income" as gross income under IRC § 61 plus the cost of goods sold, without netting for any deductions, but excluding the following: Allocations, distributions, or gains from another LLC that already paid a California LLC fee on that income (the § 17942(b)(1)(B) anti-stacking rule); Income that is not derived from or attributable to California sources, except as determined under the apportionment rule in § 4.3.  _(R&TC § 17942(b)(1)(A); R&TC § 17942(b)(1)(B))_

Worked components:

- **Gross receipts** (e.g., consulting fees, software-licensing revenue, product sales) — included gross, before any cost of goods sold or deductions.
- **Cost of goods sold** — for a retailer or manufacturer, COGS is added back to determine "total income." A reseller with $1.2M of gross sales and $900k of COGS has $1.2M of total income for § 17942 purposes (not $300k of gross profit). This is the single largest divergence from how the LLC's K-1 looks.
- **Interest, dividends, royalties** — included.
- **Capital gains and § 1231 gains** — included at gross.
- **Rental income** — included gross.
- **Guaranteed payments to members** — included (because they are deductible by the LLC at the federal level, they are part of the LLC's gross income before that deduction).
- **Tax-exempt municipal-bond interest** — excluded (not part of IRC § 61 gross income).
- **§ 1031 like-kind exchange deferred gain** — excluded to the extent deferred federally.

The fee base routinely exceeds the LLC's federal ordinary business income on Schedule K Line 1 by a multiple — especially for high-COGS businesses. Reviewers must build the "total income" figure from the LLC's gross revenue line, not from net income.

### 4.3 The apportionment rule — single sales factor

- **Single-sales-factor apportionment** — For multistate LLCs, "total income from all sources reportable to California" is computed by apportioning total worldwide income using the same single-sales-factor apportionment that applies to corporations under R&TC § 25128.7. The numerator is California sales; the denominator is total sales everywhere.  _(R&TC § 25128.7)_
- **Sourcing rules for sales, services, intangibles** — Sales of tangible personal property — sourced to California if shipped or delivered to a buyer in California (§ 25135), with throwback not applicable for the § 17942 fee (CA does not have throwback as of 2025 for corporations either after 2013). Sales of services — sourced to California where the benefit of the service is received by the customer (market-based sourcing under § 25136 and Reg. § 25136-2). A software developer LLC with all California-resident clients has a 100% California sales factor; an LLC selling SaaS to enterprise customers nationwide apportions based on customer location. Sales of intangibles / licensing — generally sourced where the intangible is used (§ 25136(a)(2)).  _(R&TC § 25135; R&TC § 25136; Reg. § 25136-2; R&TC § 25136(a)(2))_
- **When apportionment is moot** — For an in-state, single-state California LLC with all customers in California, apportionment is moot: total income from all sources reportable to California = worldwide total income. The factor only matters when the LLC has out-of-state customers and is itself either organized in California or doing business in California under § 23101.  _(R&TC § 23101)_

### 4.4 The fee is a tax, not a fee — *Northwest Energetic Services* fallout

- **Commerce Clause holding and apportionment fix** — In Northwest Energetic Services LLC v. FTB (2008) and Ventas Finance I LLC v. FTB (2008), the Court of Appeal held that pre-2007 § 17942 violated the Commerce Clause by taxing all of an LLC's income regardless of California connection. The legislature responded with the current language requiring apportionment to California-sourced income. Foreign LLCs registered in California but doing no California business owe the $800 minimum but $0 of the § 17942 fee because their California-apportioned total income is $0. The $800 itself survived constitutional challenge as a franchise tax for the privilege of registration.  _(Northwest Energetic Services LLC v. FTB (2008); Ventas Finance I LLC v. FTB (2008))_

### 4.5 Interaction with the PTE Elective Tax

- **PTET separate from $800 and LLC fee** — Under AB 150 (2021), as extended through 2025 by SB 113, an LLC taxed as a partnership may elect to pay a 9.3% Pass-Through Entity Elective Tax on the qualified net income of consenting members. The PTET is separate from and additional to the $800 minimum and the § 17942 fee. The PTET is not a substitute for either, and the § 17942 fee is not reduced by PTET payments. See `ca-pte-elective-tax.md` for the election mechanics, the 6/15 prepayment, and the credit flow to the members' Form 540.  _(AB 150 (2021); SB 113)_

## 5. Estimated payments

The $800 minimum and the LLC fee each have their own prepayment regime. Missing either generates an automatic FTB notice with penalty and interest.

### 5.1 Form 3522 — $800 LLC Tax Voucher

- **Form 3522 mechanics** — Form name: FTB 3522, Limited Liability Company Tax Voucher. Liability covered: The $800 § 17941 minimum tax for the current tax year. Due date: 15th day of the 4th month of the LLC's tax year. For a calendar-year LLC, April 15 of the tax year. Mechanism: Single voucher with a single payment. The LLC writes the tax year on the voucher and submits with payment. First-year deadline: For an LLC newly organized in 2025, the first Form 3522 is due April 15, 2025 — or, if the LLC was organized after April 15, by the 15th day of the 4th month after formation. An LLC organized June 5, 2025 owes its first $800 by October 15, 2025 (the 15th day of the 4th month after June).  _(R&TC § 17941; Form 3522)_
- **Underpayment penalties and interest** — Late or unpaid $800 is subject to: 5% late-payment penalty under § 19132 on the unpaid amount, plus 0.5% per month failure-to-pay penalty up to a 25% cap, plus Interest at the FTB's underpayment rate (the rate is reset semi-annually; consult FTB Notice for the current period).  _(R&TC § 19132)_

### 5.2 Form 3536 — Estimated Fee for LLCs

- **Form 3536 mechanics** — Form name: FTB 3536, Estimated Fee for LLCs. Liability covered: The § 17942 tiered LLC fee for the current tax year, prepaid based on the LLC's expected total income. Due date: 15th day of the 6th month of the LLC's tax year. For a calendar-year LLC, June 15 of the tax year. How much to pay: The LLC must pay the estimated fee for the bracket it expects to land in. There is no safe-harbor based on prior year; the safe-harbor is the lower of prior-year fee or current-year fee.  _(Form 3536)_
- **10% underpayment penalty — § 17942(d)(2)** — If the estimated fee paid by June 15 is less than the amount of the fee owed for the year, the FTB imposes a 10% penalty on the underpaid portion. There is no penalty if the amount paid is at least equal to the prior year's § 17942 fee (the standard safe-harbor).  _(R&TC § 17942(d)(2))_
- **First-year LLCs** — A first-year LLC owes the § 17942 fee for its first year (if its first-year income hits the bracket) and must pay Form 3536 by the 15th day of the 6th month of that first year. There is no prior-year safe-harbor because there is no prior year — the LLC must estimate carefully or accept the 10% penalty.

> **Worked safe-harbor example.** A calendar-year LLC's 2024 § 17942 fee was $2,500 (bracket $500k–$999,999). In 2025, the LLC expects total income of $1,300,000 (bracket $1M–$4,999,999, fee $6,000). To avoid the 10% penalty, the LLC must pay at least $2,500 by June 15, 2025 (the prior-year safe-harbor). It will then owe the remaining $3,500 with the Form 568 filed by March 15, 2026. If the LLC instead pays $0 on June 15 and $6,000 in March, the penalty is 10% × $6,000 = $600.

### 5.3 No estimated payments for the personal income tax of the members

- **Entity-level prepayments do not cover member tax** — The LLC's prepayments under 3522 and 3536 are entity-level and discharge only the entity's $800 and LLC fee. They do not discharge any member's personal income tax on their distributive share of the LLC's income. Members owing California personal income tax on K-1 income use Form 540-ES (see `ca-540-es-estimated-tax.md`); members who are nonresidents may have additional withholding under § 18662 (Form 592 / 592-B).  _(R&TC § 18662)_

## 6. Disregarded single-member LLC (SMLLC)

### 6.1 Federal vs. California treatment

- **Federal disregarded treatment** — A single-member LLC that has not elected to be taxed as a corporation is disregarded for federal income tax purposes under Reg. § 301.7701-3(b)(1)(ii) — its income is reported on the member's federal return (Schedule C if the member is an individual, Form 1120 Schedule C-equivalent if the member is a corporation, etc.).  _(Reg. § 301.7701-3(b)(1)(ii))_
- **California does not disregard for entity-level tax** — California does not disregard the LLC for the entity-level tax and fee. Even though the federal income flows to the member's Form 540 Schedule CA, the LLC itself is liable for: 1. The $800 minimum tax (Form 3522). 2. The § 17942 fee if its total income reaches the brackets (Form 3536 + Form 568). 3. Filing Form 568 annually.

This is the most-misunderstood feature of California LLC taxation. A solo software developer who forms a California SMLLC and reports the consulting revenue on federal Schedule C still has a Form 568 obligation and still owes $800 per year and still owes the § 17942 fee if California-sourced total income reaches $250k.

### 6.2 Form 568 mechanics for a disregarded SMLLC

- **Form 568 side requirements for SMLLC** — A disregarded SMLLC files Form 568 with: Side 1 completed identifying the SMLLC and the single member. Side 2 completed for the $800 and the § 17942 fee. Side 3 (Schedule IW, Limited Liability Company Income Worksheet) completed to derive total income. Sides 4–7 (Schedule B, Schedule K, etc.) not required — the SMLLC does not issue a K-1 to itself. Schedule EO (Pass-Through Entity Ownership) if the SMLLC owns interests in other PTEs. Schedule T (Nonconsenting Nonresident Members' Tax Liability) — N/A for an SMLLC.  _(Form 568; Schedule IW)_
- **Member reporting and no credit for $800** — The member then reports the LLC's federally-disregarded income on Schedule CA (540), Part I, Line 3 (business income), where the LLC's net profit ties to the federal Schedule C. No separate California addition is made for the SMLLC profit — the federal Schedule C profit is the starting point and Schedule CA adjusts only for non-conformity items (e.g., bonus depreciation, § 179 differences). The $800 paid on Form 3522 is not deductible by the SMLLC on Schedule C as a federal expense and is not a credit against the member's personal income tax.  _(Schedule CA (540))_

### 6.3 Where the $800 is deductible (and where it is not)

- **$800 deductibility federal vs California** — The $800 paid by the LLC is deductible as a state tax on the federal Schedule C for the SMLLC member, subject to the federal $10,000 SALT cap under § 164(b)(6) as it applies to the individual. But because the OBBBA (One Big Beautiful Bill Act, P.L. 119-21, July 4, 2025) makes the SALT cap permanent and raises the cap to $40,000 for 2025 (subject to AGI phase-down), the practical SALT room may be tight. The $800 is not deductible on the California Schedule CA — it is added back as a state-income-tax-equivalent and is never deductible against California income.  _(IRC § 164(b)(6); OBBBA P.L. 119-21)_
- **LLC fee deductibility follows same rule** — The § 17942 fee follows the same rule: deductible federally on Schedule C (subject to SALT cap), added back on Schedule CA.

## 7. Multi-member LLC taxed as a partnership

### 7.1 Filing requirements

- **Multi-member partnership filing requirements** — A multi-member LLC defaults to federal partnership treatment under Reg. § 301.7701-3(b)(1)(i). It files Form 1065 federally and Form 568 in California as a partnership filing. Form 568 — completed in full, all sides, all schedules. Schedule K (568) — California-equivalent of federal Schedule K, allocating income, deductions, credits among the members. Schedule K-1 (568) — issued to each member; required for resident, part-year-resident, and nonresident members. Schedule T — computes nonconsenting nonresident members' California tax that the LLC must withhold and remit. Schedule R — for multistate LLCs, apportions income to California using single-sales-factor.  _(Reg. § 301.7701-3(b)(1)(i); Form 1065; Form 568)_

### 7.2 Withholding on nonresident members — § 18662

- **Withholding rates and forms** — A California LLC with nonresident members must withhold 7% of distributions to nonresident individuals (and 8.84% for nonresident C-corp members) under R&TC § 18662 unless the member completes Form 590 (Withholding Exemption Certificate) or the LLC files a group return. Withholding is remitted on Form 592, with annual reconciliation on Form 592-B.  _(R&TC § 18662)_
- **Nonconsenting nonresident member Schedule T tax rate** — A nonconsenting nonresident member alternatively has their share of California source income reported on Schedule T of Form 568, and the LLC pays the California tax at the highest individual rate (12.3% for 2025, plus the 1% MHST for income over $1M) on that share.

### 7.3 Members' Form 540 / 540-NR

- **Member reporting by residency** — Each member's distributive share, as shown on the K-1 (568), is reported on: Resident member — Form 540, Schedule CA Part I, Line 5 (partnership income). Part-year resident member — Form 540-NR, with California-source portion only. Nonresident member — Form 540-NR, California-source K-1 only.
- **Entity taxes not allocated to members** — The $800 and the § 17942 fee are paid by the LLC; they are not allocated to members on the K-1. Members do not get a credit for them on Form 540 — these are entity-level taxes, period. (Contrast with the PTE Elective Tax, which does flow to members as a credit on Form 540 Line 43 — see `ca-pte-elective-tax.md`.)

## 8. LLC electing to be taxed as a corporation

### 8.1 The election mechanics

- **Corporate/S-corp election mechanics** — An LLC may elect federal corporate tax treatment by filing Form 8832 (entity classification election). An LLC that has elected corporate treatment may further elect S-corp treatment by filing Form 2553. These are federal elections, but California automatically follows the federal corporate-status election under R&TC § 23038.  _(R&TC § 23038)_

### 8.2 California filing track for a C-corp-elected LLC

- **C-corp filing, rate, and LLC fee exclusion** — Files Form 100 (California Corporation Franchise or Income Tax Return). Pays the greater of: (a) the 8.84% corporate franchise tax on apportioned California net income or (b) the $800 minimum franchise tax under § 23153. Does NOT file Form 568. Does NOT pay the § 17942 LLC fee. This is the key planning point: an LLC that crosses the $5M total income threshold owes $11,790 of LLC fee as a partnership/disregarded entity, but $0 of LLC fee as a corporation (though it now pays 8.84% on net income, which usually exceeds $11,790 for any profitable business of that size).  _(R&TC § 23153; Form 100)_
- **First-year $800 for C-corp elections** — Under AB 85's now-expired waiver, first-year corporations (including LLCs electing C-corp status) were exempt from the $800 minimum for tax years 2021–2023. The waiver has expired for tax years beginning on or after January 1, 2024. First-year corporations now owe the $800 minimum from year one.  _(AB 85)_

### 8.3 California filing track for an S-corp-elected LLC

- **S-corp filing, rate, and LLC fee exclusion** — Files Form 100S (California S Corporation Franchise or Income Tax Return). Pays the greater of: (a) 1.5% of California net income or (b) the $800 minimum under § 23802. Does NOT file Form 568. Does NOT pay the § 17942 LLC fee.  _(R&TC § 23802; Form 100S)_

S-corp election in California is rarely break-even for a freelancer because the 1.5% state-level S-corp tax is layered on top of any federal SE-tax savings. See `us-s-corp-election-decision.md` for the full break-even analysis with California complications.

### 8.4 Revoking the corporate election

- **Revocation reverts to Form 568** — An LLC that revokes its corporate election reverts to disregarded or partnership treatment and resumes Form 568 filing, including the § 17942 fee. The federal revocation is via a new Form 8832 (after the 60-month limit), and California automatically follows.

## 9. Doing business in California — factor presence and economic nexus

### 9.1 The § 23101(a) "actively engaging" prong

- **Actively engaging in transaction definition** — R&TC § 23101(a) defines "doing business" as actively engaging in any transaction for the purpose of financial or pecuniary gain or profit. A single transaction can qualify. This historical definition was supplemented (not replaced) by the factor presence test in § 23101(b).  _(R&TC § 23101(a))_

### 9.2 The § 23101(b) factor presence test (2025 thresholds)

- **Factor presence test triggers doing business** — An out-of-state LLC is doing business in California — and therefore liable for $800 + LLC fee + Form 568 — if any one of the three factors (sales, property, compensation) exceeds its threshold.  _(R&TC § 23101(b))_

**2025 California thresholds by factor**

| Factor | 2025 California threshold |
| --- | --- |
| California sales | Greater of **$735,019** or **25%** of total sales |
| California real or tangible property | Greater of **$73,502** or **25%** of total property |
| California compensation paid | Greater of **$73,502** or **25%** of total compensation |

The thresholds are indexed annually. The reviewer must confirm the current-year published thresholds from FTB Notice or FTB.ca.gov before issuing any nexus opinion. (For tax year 2024, the thresholds were $711,538 / $71,154 / $71,154.)

### 9.3 Pass-through nexus — *Swart Enterprises*

- **Swart Enterprises holding and FTB narrow interpretation** — In Swart Enterprises, Inc. v. FTB (2017), the Court of Appeal held that a 0.2% passive interest in a California-doing-business LLC was not enough to subject an out-of-state corporation to California's $800 franchise tax. The FTB has narrowly interpreted Swart in FTB Legal Ruling 2018-01: it applies only to very small, passive, non-managing interests in manager-managed LLCs. Any member-managed interest, any interest of 0.5% or more, or any interest carrying management rights triggers California "doing business" and the LLC fee/tax obligation on the upper-tier entity.  _(Swart Enterprises, Inc. v. FTB (2017); FTB Legal Ruling 2018-01)_

### 9.4 P.L. 86-272 — does NOT shield the LLC fee

- **P.L. 86-272 scope and exclusions** — Public Law 86-272 protects out-of-state businesses from state income tax if their only California activity is solicitation of orders for tangible personal property shipped from outside the state. P.L. 86-272 does not apply to: The $800 franchise tax (which is a tax for the privilege of doing business, not on income). The § 17942 LLC fee (which is a fee on total income, not a net income tax). Sales of services or intangibles (P.L. 86-272 covers TPP only). Sales facilitated by activities other than solicitation (e.g., post-sale customer support in California, which the FTB has aggressively argued post-COVID and codified in FTB Technical Advice Memorandum 2022-01).  _(Public Law 86-272; FTB Technical Advice Memorandum 2022-01)_
- **TPP seller still owes $800 + fee** — A foreign LLC selling tangible goods into California that is otherwise P.L. 86-272-protected from California income tax may still owe the $800 + LLC fee + Form 568.

### 9.5 Consequences of non-filing

- **FTB non-filer enforcement data sources** — The FTB's non-filer enforcement program identifies LLCs through: IRS data sharing (federal partnership returns showing California-source income). SOS registration data. 1099 / W-2 / Form 592 data showing California-source payments. Sales-tax records from CDTFA.
- **Demand letter and penalty exposure** — Once identified, the FTB issues a demand letter for back $800 minimums plus § 17942 fees plus penalties plus interest, often going back four open years. The taxpayer also exposes itself to the SOS $2,000 penalty for unregistered foreign LLCs under Corporations Code § 17708.07, and individual members may face California personal income tax assessments on their distributive shares of California-source income.  _(Corporations Code § 17708.07)_

## 10. Penalties and interest

### 10.1 Late filing of Form 568

- **§ 19131 late-filing penalty** — 5% of the unpaid tax per month, up to 25%, with a minimum of $18 for non-filing LLCs.  _(R&TC § 19131)_
- **Per-member late-filing penalty (§ 19172)** — For partnerships and LLCs taxed as partnerships, $18 per member per month for up to 12 months — capped at $216 per member. An LLC with 10 members that files Form 568 12 months late owes $2,160 in per-member penalties before any tax-based penalties.  _(R&TC § 19172)_

### 10.2 Late payment

- **§ 19132 late-payment penalty** — 5% of the unpaid amount, plus 0.5% per month up to a 25% cap.  _(R&TC § 19132)_
- **Combined cap § 19132.5** — § 19132.5 generally caps the combined late-filing + late-payment penalty at 25% of the underpaid amount.  _(R&TC § 19132.5)_

### 10.3 § 17942(d) — LLC fee underpayment penalty

- **10% underpayment penalty** — 10% of the underpayment of the § 17942 estimated fee due June 15, with no safe-harbor below prior-year fee.  _(R&TC § 17942(d))_

### 10.4 Estimated-tax / minimum-tax late payment

- **$800 minimum subject to § 19132 penalty** — The $800 minimum is itself subject to the § 19132 5% late-payment penalty plus 0.5%/month if Form 3522 is not paid by the 15th day of the 4th month.  _(R&TC § 19132)_

### 10.5 Interest

- **FTB underpayment rate H1 2025** — The FTB underpayment rate is reset semi-annually by FTB Notice. For the period January 1, 2025 — June 30, 2025, the rate is 8% per annum, compounded daily; verify the second-half-2025 rate before issuing any output.  _(FTB Notice)_

### 10.6 Penalty abatement

- **First-time abatement § 19132.5(b)** — California allows a one-time abatement of timeliness penalties for an individual taxpayer with a clean 4-year compliance history. The abatement applies to the $800 minimum tax late-payment penalty for an SMLLC (because the SMLLC owner is an individual). It does not apply to multi-member LLCs.  _(R&TC § 19132.5(b))_
- **Reasonable cause abatement § 19133** — § 19133 abatement is available on a showing of reasonable cause and not willful neglect; the taxpayer files FTB 2917 (Reasonable Cause — Individual and Fiduciary Claim for Refund) or FTB 2924 (Reasonable Cause — Business Entity Claim for Refund).  _(R&TC § 19133)_

## 11. Worked examples

### 11.1 Example A — California-resident solo developer SMLLC, $310k of consulting revenue

Maria Reyes, California resident, forms Bay Code Studio LLC (an SMLLC) on January 5, 2024.
2025 tax year: she earns $310,000 of consulting revenue (gross), with $40,000 of business expenses, for federal Schedule C net profit of $270,000.
All clients are California-based; no out-of-state revenue.

- **$800 minimum tax due date and payment** — $800 minimum tax (§ 17941). Due April 15, 2025 on Form 3522. Paid: $800.  _(§ 17941)_
- **§ 17942 total income for Example A** — "Total income from all sources reportable to California" = gross receipts of $310,000 (no COGS; consulting). All California-sourced (California-resident clients receive the benefit in California).  _(§ 17942)_
- **§ 17942 fee bracket for Example A** — $250,000 ≤ $310,000 < $500,000 → $900 fee.  _(§ 17942)_
- **Form 3536 estimated fee for Example A** — Due June 15, 2025. Prior-year (2024) fee: assume Maria's 2024 revenue was $230k, so 2024 fee = $0. Safe-harbor: lower of (prior-year $0) or (current-year $900) = $0 — Maria pays $0 on Form 3536 without penalty. Maria pays the $900 with Form 568 in March 2026.
- **Form 568 for Example A** — Filed March 15, 2026, for tax year 2025. Side 2 reconciles the $800 (paid April 2025 via 3522) and the $900 fee (paid March 2026 with return). Side 3 Schedule IW reports the $310,000 of total income. No K-1 issued (SMLLC).
- **Federal Schedule C / Maria's Form 540 for Example A** — Federal Schedule C: $270,000 net profit (after $40k expenses; the $800 and the $900 are deductible state taxes on Schedule C subject to SALT cap of $40,000 under OBBBA — see § 6.3). California Schedule CA: starts with federal Schedule C profit; adds back the $800 and the $900 (state-income-tax-equivalent under § 17072).  _(§ 17072)_

Total California cash outlay at the entity level: $1,700. Plus Maria's personal income tax on the $270k Schedule C income at the 2025 California rates, covered in `ca-income-tax.md`.

### 11.2 Example B — Multi-member LLC, $1.4M of total income, multistate sales

Salish Robotics LLC is a Delaware-organized LLC with three members: a California resident (40%), an Oregon resident (30%), and a Washington corporation (30%).
Registered as a foreign LLC in California with SOS.
2025 gross receipts: $1,400,000 ($800,000 California, $400,000 Oregon, $200,000 Washington). COGS: $300,000.
All sales are services (robotics consulting); market-based sourcing applies.

- **Filing trigger for Example B** — Registered foreign LLC (Gate B) — California-resident member is sufficient. § 23101(b) sales test: California sales $800,000 > $735,019 threshold → doing business confirmed.  _(§ 23101(b))_
- **$800 minimum tax for Example B** — Due April 15, 2025. Paid: $800.
- **§ 17942 total income for Example B** — Gross receipts plus COGS (because § 17942(b)(1)(A) is computed without netting COGS) = $1,400,000 + $0 (consulting, no inventory COGS in the technical sense — but if the $300k were classified as COGS in inventory accounting, it would be added back; for a services LLC, $300k of direct labor is not COGS for § 17942 purposes and the total income is just $1,400,000 of gross receipts).  _(§ 17942(b)(1)(A))_
- **California apportionment for Example B** — Single sales factor: $800,000 / $1,400,000 = 57.143%. California-apportioned total income: $1,400,000 × 57.143% = $800,000.
- **§ 17942 fee bracket for Example B** — $500,000 ≤ $800,000 < $1,000,000 → $2,500 fee.  _(§ 17942)_
- **Form 3536 estimated fee for Example B** — Due June 15, 2025. Safe-harbor = prior-year fee. Assume 2024 fee = $2,500 (same bracket). Salish pays $2,500 on June 15, 2025; no underpayment.
- **Schedule T / nonresident withholding for Example B** — The Oregon individual member's California-source distributive share triggers § 18662 7% withholding unless Form 590 is filed. The Washington C-corp member's share triggers 8.84% withholding unless Form 590 is filed. The LLC files Form 592 quarterly to remit.  _(§ 18662)_
- **K-1 (568) to each member for Example B** — Allocates California-source income (the apportioned $800k of total income, less apportioned deductions, to net income figure). The California-resident member reports the K-1 on Form 540 Schedule CA Line 5. The Oregon and Washington members file Form 540-NR.

Total California entity-level outlay: $3,300 ($800 + $2,500), plus member-level withholding via Form 592.

### 11.3 Example C — Out-of-state LLC, no SOS registration, hits factor presence

Aspen Analytics LLC is organized in Colorado, never registered with California SOS, has no California office or employees.
2025 sales: $4,200,000 total worldwide, of which $1,100,000 is to California-based customers (SaaS subscription benefit received in California).
All members are Colorado residents.

- **§ 23101(b) trigger for Example C** — California sales $1,100,000 > $735,019 (2025 threshold) → doing business in California even without SOS registration.  _(§ 23101(b))_
- **Penalty exposure for Example C** — Aspen owes (a) $800 minimum, (b) § 17942 fee, (c) Form 568, (d) potentially the $2,000 Corporations Code § 17708.07 penalty for unregistered foreign LLC, plus (e) back-year liabilities if it has been over-threshold in prior years.  _(Corporations Code § 17708.07)_
- **§ 17942 total income for Example C** — $4,200,000 worldwide.  _(§ 17942)_
- **California apportionment for Example C** — $1,100,000 / $4,200,000 = 26.19%. California total income: $4,200,000 × 26.19% = $1,100,000.
- **§ 17942 fee bracket for Example C** — $1,000,000 ≤ $1,100,000 < $5,000,000 → $6,000 fee.  _(§ 17942)_
- **Total minimum plus fee and penalties for Example C** — $800 minimum + $6,000 fee = $6,800. Plus penalties for non-filing (5% per month, up to 25%, plus $18/month per member under § 19172 — but Aspen is a partnership, so per-member penalty applies if it has multiple members).  _(§ 19172)_

Register with California SOS retroactively (Form LLC-5), file Form 568 for 2025 and any open prior years, request first-time abatement where eligible, and consider voluntary disclosure under the FTB Voluntary Disclosure Program (Form 4925) to limit look-back to 6 years and waive some penalties.

### 11.4 Example D — 15-day rule, year-end formation

Pacific Yields LLC files Articles of Organization with California SOS on December 22, 2025.
It opens a business bank account on January 4, 2026 and earns no revenue and incurs no expenses between December 22, 2025 and December 31, 2025.

- **15-day rule application for Example D** — 15-day rule (§ 17946 / § 17941(f)) — formation date Dec 22 is within the last 15 days of the calendar tax year (Dec 17 — Dec 31) AND no business was conducted → $0 for 2025.  _(§ 17946 / § 17941(f))_
- **2026 first-year treatment for Example D** — 2026 is the LLC's "first year" for AB 85 purposes — but AB 85's first-year waiver expired for tax years beginning on or after January 1, 2024. So the LLC owes the full $800 for 2026, due April 15, 2026 on Form 3522.  _(AB 85)_
- **Form 568 filing requirement for Example D** — No Form 568 filing is required for 2025 (because the 15-day rule effectively means no 2025 tax year). Filing begins with the 2026 return due March 15, 2027.

### 11.5 Example E — LLC that elected S-corp treatment

Saguaro Software LLC, formed in California in 2022, filed Form 2553 effective January 1, 2025 to elect federal S-corp treatment.
2025 gross receipts: $1,200,000. Owner pays herself $90,000 W-2 salary; net pass-through income $400,000.

- **California follows S-corp election for Example E** — California auto-follows the S-corp election. Saguaro files Form 100S, not Form 568.
- **Form 568 not required for Example E** — Form 568 not required for 2025. (2024 Form 568 — covering the pre-election year — was due March 17, 2025 because March 15, 2025 was a Saturday).
- **California S-corp tax under § 23802 for Example E** — 1.5% × California net income, or $800 minimum, whichever is greater. 1.5% × $490,000 (net income before salary deduction at the entity is more nuanced — but assume California net income ≈ $400,000 of pass-through plus add-backs as relevant) = $6,000. Greater of $6,000 or $800 = $6,000.  _(§ 23802)_
- **§ 17942 fee not owed for Example E** — § 17942 fee NOT owed. S-corp track exempts Saguaro from the LLC fee.  _(§ 17942)_
- **Federal vs. California reasonable salary for Example E** — $90,000 W-2 reasonable-salary determination is a federal issue (see `us-s-corp-election-decision.md`). California follows federal salary characterization but does not impose its own reasonable-compensation test.

Compared to remaining a partnership-LLC: as a partnership, Saguaro would owe $800 + $6,000 (§ 17942 bracket $1M–$4,999,999) = $6,800. As an S-corp, $6,000. Net California savings from S-election: $800/year. Federal SE-tax savings are the dominant driver — California's S-corp tax cost largely offsets the LLC fee savings. Run the full break-even from `us-s-corp-election-decision.md` before recommending.

## 12. Output specification — what this skill produces

When invoked in a workflow, this skill produces four reviewer-ready artifacts:

### 12.1 The California LLC liability summary

**California LLC Liability Summary template**

```
California LLC Liability — [LLC name], Tax Year 2025
─────────────────────────────────────────────────────
Federal classification:        [disregarded / partnership / C / S]
California return:             [Form 568 / Form 100 / Form 100S]
SOS status:                    [Domestic / Foreign registered / Unregistered, doing business]
Tax year:                      [calendar / fiscal MM-DD]

$800 minimum tax (§ 17941):    $800
  Form 3522 due:               [date]
  Form 3522 paid:              [date / status]
  AB 85 first-year applicable? [N/A — expired for 2024+]
  15-day rule applicable?      [Yes/No, with explanation]

§ 17942 LLC fee:
  Total income (gross + COGS): $[amount]
  CA sales factor:             [%]
  CA total income:             $[amount]
  Bracket:                     [< $250k / $250k-$499,999 / $500k-$999,999 / $1M-$4,999,999 / $5M+]
  Fee:                         $[0 / 900 / 2,500 / 6,000 / 11,790]
  Form 3536 due:               [date]
  Form 3536 paid:              $[amount paid by due date]
  Safe-harbor (prior-year):    $[prior-year fee]
  Underpayment penalty (10%):  $[amount, if applicable]

PTE Elective Tax (separate):   [See ca-pte-elective-tax.md]
Member withholding (§ 18662):  [See § 7.2 of this skill / Form 592]

Total entity-level CA tax:     $[$800 + § 17942 fee]
Total penalties + interest:    $[amount]
```

### 12.2 The Form 568 walkthrough

A side-by-side mapping of source data (QuickBooks / Xero / bank-feed) to Form 568 line numbers, with a flag for each line that requires reviewer judgment (apportionment, total income definition, nexus determination).

### 12.3 The Form 3522 / Form 3536 voucher pack

Two pre-filled vouchers with the entity name, CA SOS file number, year, and amount — ready for the reviewer to sign and the taxpayer to mail or e-pay via FTB Web Pay.

### 12.4 The reviewer brief

A 1-page narrative for the credentialed reviewer covering:
- The classification basis (disregarded vs. partnership) and citation.
- The nexus basis (Gate A / B / C) and citation.
- The total-income build-up, with COGS and apportionment shown.
- Penalty exposure if any payment was late.
- Cross-references to the federal return (`us-sole-prop-bookkeeping.md` / `us-schedule-c-and-se-computation.md`), to `ca-income-tax.md` for the member's Form 540, and to `ca-pte-elective-tax.md` if PTET is elected.

## 13. Self-checks before issuing output

Before the skill releases any number, the reviewer (and the skill, where automated) verifies:

- [ ] The $800 line is exactly $800. No proration, no partial-year math. If the LLC was formed in the last 15 days with no activity, the $800 is $0 — verify both prongs.
- [ ] The § 17942 fee matches a bracket exactly. $900 / $2,500 / $6,000 / $11,790 / $0 — no interpolation.
- [ ] The total income figure adds back COGS. The base is gross receipts + COGS, not net income.
- [ ] Apportionment is single sales factor, market sourcing. For multistate LLCs only.
- [ ] The voucher year on Form 3522 matches the tax year. Most common error.
- [ ] The Form 3536 amount equals at least prior-year fee to avoid the 10% penalty.
- [ ] The first-year waiver is NOT applied for 2024+ formations. AB 85 expired.
- [ ] The 2025 § 23101(b) thresholds are confirmed against current FTB indexing notice ($735,019 / $73,502 / $73,502 used here; verify before issuing).
- [ ] For SMLLCs, the federal Schedule C tie-out matches the SMLLC Side 3 IW total income.
- [ ] For partnerships, the K-1 California-source amounts tie to Schedule T withholding.
- [ ] PTET interaction documented. $800 + LLC fee are unaffected by PTET; PTET is a separate liability if elected.
- [ ] Federal SALT deductibility noted, but not over-claimed (SALT cap as enacted by OBBBA for 2025).

## 14. Cross-references to other OpenAccountants skills

- `us-tax-workflow-base.md` — must be loaded first (workflow scaffolding).
- `us-sole-prop-bookkeeping.md` — federal Schedule C side for SMLLCs.
- `us-schedule-c-and-se-computation.md` — federal SE tax on member's distributive share.
- `ca-income-tax.md` — California Form 540 for the LLC's individual member(s).
- `ca-540-es-estimated-tax.md` — member-level California estimated tax.
- `ca-smllc-form-568.md` — the predecessor SMLLC-only skill; this skill supersedes and generalizes it.
- `ca-pte-elective-tax.md` — PTE Elective Tax under AB 150 / SB 113 (separate liability).
- `us-s-corp-election-decision.md` — break-even analysis for the corporate election.
- `us-ca-return-assembly.md` — final assembly of the federal + California package.

## 15. Provenance and primary authority

This skill is built from the following primary sources. Citations are to the source as in effect on the skill's last-updated date.

### 15.1 California Revenue and Taxation Code

- **§ 17941** — Annual tax on LLCs; the $800 minimum.  _(§ 17941)_
- **§ 17942** — Fee on LLCs; the tiered total-income schedule, with sub-sections (a) (rate schedule), (b)(1)(A) (total income definition), (b)(1)(B) (anti-stacking), (d)(1) (estimated payment), (d)(2) (10% underpayment penalty).  _(§ 17942)_
- **§ 17946** — Short-year first-year rule (the 15-day rule).  _(§ 17946)_
- **§ 17948** — LLP annual tax (cross-reference; LLPs are out of scope here).  _(§ 17948)_
- **§ 17955** — Investment partnership exception for nonresident members.  _(§ 17955)_
- **§ 18662** — Withholding on nonresident members.  _(§ 18662)_
- **§ 19131** — Late-filing penalty.  _(§ 19131)_
- **§ 19132** — Late-payment penalty.  _(§ 19132)_
- **§ 19132.5** — Combined penalty cap and first-time abatement.  _(§ 19132.5)_
- **§ 19133** — Reasonable-cause abatement.  _(§ 19133)_
- **§ 19172** — Per-member late-filing penalty for partnerships.  _(§ 19172)_
- **§ 23038** — Federal classification follows for California.  _(§ 23038)_
- **§ 23101** — Doing-business definition: § 23101(a) actively engaging, § 23101(b) factor presence test, § 23101(b)(4) annual indexing.  _(§ 23101)_
- **§ 23153** — Corporate $800 minimum franchise tax.  _(§ 23153)_
- **§ 23802** — S-corporation 1.5% tax / $800 minimum.  _(§ 23802)_
- **§ 25128.7** — Single sales factor apportionment.  _(§ 25128.7)_
- **§ 25135** — Sales of TPP sourcing.  _(§ 25135)_
- **§ 25136** — Sales other than TPP — market sourcing.  _(§ 25136)_

### 15.2 California legislation

- **AB 85 (2020), Chapter 8, Statutes of 2020** — First-year $800 waiver for LLCs/LPs/LLPs, tax years 2021–2023.  _(AB 85 (2020), Chapter 8, Statutes of 2020)_
- **SB 818 (2021)** — Extended AB 85 waiver to 2023.  _(SB 818 (2021))_
- **AB 150 (2021)** — Pass-Through Entity Elective Tax (Subchapter 10.4, R&TC §§ 17052.10, 19900–19906).  _(AB 150 (2021))_
- **SB 113 (2022)** — Extended PTET refinements through 2025.  _(SB 113 (2022))_

### 15.3 California regulations

- **18 CCR § 17951-4** — Apportionment for pass-through entities.  _(18 CCR § 17951-4)_
- **18 CCR § 25136-2** — Market-based sourcing for services and intangibles.  _(18 CCR § 25136-2)_

### 15.4 California case law

- **Northwest Energetic Services LLC v. FTB** — 159 Cal.App.4th 841 (2008) — Pre-2007 § 17942 unconstitutional Commerce Clause violation.  _(Northwest Energetic Services LLC v. FTB, 159 Cal.App.4th 841 (2008))_
- **Ventas Finance I LLC v. FTB** — 165 Cal.App.4th 1207 (2008) — Same issue, partial refund granted.  _(Ventas Finance I LLC v. FTB, 165 Cal.App.4th 1207 (2008))_
- **Swart Enterprises, Inc. v. FTB** — 7 Cal.App.5th 497 (2017) — Small passive interest in CA LLC insufficient to subject upper-tier corporation to $800.  _(Swart Enterprises, Inc. v. FTB, 7 Cal.App.5th 497 (2017))_

### 15.5 California Franchise Tax Board guidance

- **FTB Publication 3556** — Limited Liability Company Filing Information.  _(FTB Publication 3556)_
- **FTB Form 568 Instructions** — 2024 booklet; 2025 booklet pending release Q4 2025.  _(FTB Form 568 Instructions)_
- **FTB Form 3522 Instructions** — FTB Form 3522 Instructions.  _(FTB Form 3522 Instructions)_
- **FTB Form 3536 Instructions** — FTB Form 3536 Instructions.  _(FTB Form 3536 Instructions)_
- **FTB Legal Ruling 2018-01** — Application of Swart to non-managing-member LLC interests.  _(FTB Legal Ruling 2018-01)_
- **FTB Notice — annual § 23101(b) thresholds** — Current and prior-year indexing.  _(FTB Notice — annual § 23101(b) thresholds)_
- **FTB Technical Advice Memorandum 2022-01** — Post-COVID P.L. 86-272 activities; FTB position that interactive website features are unprotected non-solicitation activity.  _(FTB Technical Advice Memorandum 2022-01)_

### 15.6 Federal cross-references

- **IRC § 61** — Gross income (referenced for the § 17942 "total income" definition base).  _(IRC § 61)_
- **Reg. § 301.7701-3** — Federal entity classification (check-the-box).  _(Reg. § 301.7701-3)_
- **P.L. 86-272** — Federal solicitation immunity (15 U.S.C. §§ 381–384) — does not shield § 17941 or § 17942.  _(P.L. 86-272)_
- **P.L. 119-21 (OBBBA, July 4, 2025)** — Federal SALT cap modifications for 2025.  _(P.L. 119-21 (OBBBA, July 4, 2025))_

## 16. Disclaimer

This skill is internal OpenAccountants reference content. It is not tax advice. The Franchise Tax Board's published forms, instructions, regulations, and notices are the controlling authority. California law changes annually — and § 23101(b) thresholds change annually with indexing — so the reviewer must confirm every dollar amount against current-year FTB guidance before issuing any output to a taxpayer.

No skill output may be released to a client without sign-off by a Circular 230 federal practitioner and a California-licensed preparer (CTEC-registered, EA, CPA, or California attorney). Disregarded SMLLC outputs additionally require the member's signature on the Form 540 incorporating the SMLLC's federal Schedule C profit.

Where this skill conflicts with an FTB Notice issued after 2025-11-15, the FTB Notice controls. Where this skill conflicts with a published court decision issued after 2025-11-15, the court decision controls. The reviewer is the final authority on the engagement.

— End of skill —

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
