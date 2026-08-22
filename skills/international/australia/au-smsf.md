---
name: au-smsf
description: >
  Use this skill whenever asked about Australian self-managed superannuation funds -- SMSF accounting, the SMSF annual return (SAR), supervisory levy, fund tax at 15%, exempt current pension income (ECPI), actuarial certificates, non-arm's length income or expenses (NALI/NALE), contribution caps and acceptance rules, minimum pension drawdowns, transfer balance cap and TBAR reporting, SMSF audits, in-house assets, LRBA safe harbour rates, or Division 296. Trigger on phrases like "SMSF", "self-managed super", "SAR", "supervisory levy", "actuarial certificate", "ECPI", "NALI", "TBAR", "minimum pension", "bare trust", or "SMSF audit". ALWAYS read this skill before touching any SMSF work.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Self-Managed Super Funds (SMSF) -- Accounting, Tax & Compliance Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context (2026-27).** Three regime changes hit SMSF files this year. (1) **Division 296** is law (Building a Stronger and Fairer Super System Act 2026): from 2026-27 an EXTRA 15% applies to the earnings proportion attributable to total super balance (TSB) between $3m and $10m, and an extra 25% above $10m -- realised-earnings basis, thresholds indexed, levied on the MEMBER personally, not the fund. (2) **Payday super**: employer contributions now arrive within 7 business days of each payday -- frequent small receipts are the new normal and the fund's ESA/bank details must work. (3) The **NALE rules** as amended by the Treasury Laws Amendment (Support for Small Business and Charities and Other Measures) Act 2024 cap general-expense NALI at TWICE the expense shortfall (applied from 2018-19). This skill covers SMSF accounting, tax and compliance only -- it is NOT financial product advice (see R-AU-SF-1).

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary legislation | Superannuation Industry (Supervision) Act 1993 (SIS Act) + SIS Regulations 1994; ITAA 1997 Div 295 |
| Regulator | ATO (SMSFs); ASIC (approved SMSF auditors, trustee companies) |
| Income year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Fund tax rate (complying) | 15% on low-tax component (earnings + assessable contributions, s 295-160) |
| Discounted capital gains | 1/3 discount if held 12+ months -> 10% effective |
| ECPI (retirement-phase earnings) | 0% -- segregated or proportionate (actuarial certificate) method |
| NALI / non-complying fund | 45% |
| No-TFN contributions | Extra 32% on mandated employer contributions (complying fund) |
| Supervisory levy | $259/year (unchanged since 2014-15), paid a year IN ADVANCE with the SAR; new fund's first SAR: $518 |
| SAR due dates | Self-lodgers: new/overdue 31 Oct (pay 1 Dec), others 28 Feb. Tax agent: first year 28 Feb (31 Oct if ATO-reviewed at registration); ongoing per agent program (generally 15 May) |
| Audit | ASIC-registered approved SMSF auditor, appointed >= 45 days before SAR due; audit finalised BEFORE lodgment |
| Max members | 6 (since 1 July 2021) |
| Concessional cap (2026-27) | $32,500 (carry-forward if TSB < $500,000 at prior 30 June) |
| Non-concessional cap (2026-27) | $130,000; bring-forward by TSB at 30 June 2026 (Rule 8) |
| General transfer balance cap | $2,100,000 (2025-26: $2.0m); personal caps vary (proportional indexing) |
| Minimum pension drawdowns | 4% (under 65) to 14% (95+) -- no reduction currently in force |
| TBAR | Quarterly for ALL SMSFs since 1 July 2023; due 28 days after quarter end |
| LRBA safe harbour rate (PCG 2016/5) | 2026-27: 9.35% real property (2025-26: 8.95%); 11.35% listed securities (property rate + 2%) |
| Division 296 | First year 2026-27; extra 15% ($3m-$10m proportion) / 25% (>$10m); member-levied; FLAG, never compute |
| ASIC special purpose trustee company review fee | $70/year from 1 July 2026 |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults**

| Ambiguity | Default |
|---|---|
| Unknown ECPI method | Assume proportionate -- actuarial certificate REQUIRED before claiming |
| Unknown whether minimum pension paid | Do NOT claim ECPI until payments verified against SIS Reg Sch 7 minimum |
| Unknown member TSB | Assume caps/bring-forward/carry-forward unavailable; ask for TSB at 30 June 2026 |
| Related-party transaction in the file | Escalate -- s 65 / s 66 / Part 8 / NALI screen before classifying |
| Unknown asset valuation support | Flag audit risk -- market value at 30 June required (SIS Reg 8.02B) |
| Contribution credited near 30 June | Date RECEIVED by the fund governs the year and the cap |
| Unknown auditor appointment date | Check the 45-day rule now -- late appointment jeopardises lodgment |
| Unknown member age | Ask -- age drives acceptance rules AND pension minimums |
| Payment to a member with no documented condition of release | Treat as potential illegal early access; escalate (never classify as a benefit) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- trust deed and member list, trustee type (individual vs corporate), member ages and account phases (accumulation / retirement), trial balance or bank statements, prior-year SAR, and each member's TSB at 30 June 2026.

**Recommended** -- actuarial certificate (if proportionate), 30 June market valuations with evidence, contribution and pension payment schedules per member, TBAR lodgment history, LRBA loan agreement and amortisation schedule, investment strategy with last review date.

**Ideal** -- signed trustee declarations (NAT 71089), audit workpapers and prior auditor management letters, deed history including pension documentation, lease agreements for any related-party tenancy, insurance policy schedule.

### Refusal catalogue

**R-AU-SF-1 -- Financial product / investment advice (AFSL boundary).** *Trigger:* asked to recommend investments, whether to start/commute a pension, how much to contribute, or whether an SMSF suits the client. *Message:* "That is personal financial product advice requiring an Australian Financial Services Licence (the accountants' exemption ended 1 July 2016). I can handle SMSF accounting, tax and compliance only. Refer to a licensed financial adviser." HARD refusal -- no exceptions.

**R-AU-SF-2 -- In-specie contribution / off-market transfer valuations.** *Trigger:* asked to set the value of an asset contributed or transferred in-specie. *Message:* "Contribution value must be market value with qualified valuation evidence; s 66 acquisition rules also apply. Obtain an independent valuation and escalate."

**R-AU-SF-3 -- LRBA structuring.** *Trigger:* asked to establish a bare/holding trust, draft loan terms, or design a related-party LRBA. *Message:* "LRBA establishment is legal and financial advice. I can classify payments on an EXISTING documented LRBA and check the PCG 2016/5 safe harbour only. Escalate."

**R-AU-SF-4 -- Related-party acquisitions.** *Trigger:* proposed purchase from / lease to a member or related party. *Message:* "s 66 prohibits most related-party acquisitions (exceptions: listed securities and business real property at market value, within in-house limits). Transaction design must be escalated before any step is taken."

**R-AU-SF-5 -- Early-access schemes.** *Trigger:* any request to pay benefits without a documented condition of release, or to 'temporarily borrow' fund money. *Message:* "Illegal early access -- taxed at marginal rates plus penalties, trustee disqualification, potential fund non-compliance (45% on assets), and promoter penalties. Refuse and warn; compassionate release runs through the ATO only."

**R-AU-SF-6 -- Wind-ups.** *Trigger:* asked to wind up a fund. *Message:* "Wind-up sequencing (benefit payments/rollovers, final audit, final SAR with levy adjustment, deregistration) is judgment work with irreversible steps. Escalate to a qualified practitioner."

**R-AU-SF-7 -- Death benefit disputes / BDBNs.** *Trigger:* death benefit payment directions, binding death benefit nomination validity, or competing claims. *Message:* "Legal advice. Escalate to an estate/superannuation lawyer."

## Section 3 -- Fund structure and registration

### 3.1 Definition of an SMSF (SIS Act s 17A)

- **Maximum 6 members** (up from 4 on 1 July 2021).
- **Individual trustees:** every member is a trustee and every trustee is a member. Single-member fund: 2 individual trustees (the member + 1 other).
- **Corporate trustee:** every member is a director and every director is a member. Single-member fund: sole director, or member + 1 other director.
- No member may be the **employee of another member** unless they are relatives.
- Trustees/directors must not be **remunerated** for trustee duties (arm's-length professional services in another capacity are permitted, s 17B).
- **Disqualified persons** (s 120: undischarged bankrupts, dishonesty convictions, civil penalty orders) can never act -- check the ATO disqualified trustees register at onboarding.
- Minors and members lacking capacity act through a legal personal representative or parent/guardian (s 17A(3)); an enduring power of attorney can stand in for a member.

### 3.2 Individual vs corporate trustee

| Factor | Individual trustees | Corporate trustee |
|---|---|---|
| Ongoing cost | Nil | ASIC annual review fee $70 (special purpose company, from 1 July 2026) |
| Membership change | Retitle EVERY asset | Company remains owner; update directors |
| s 166 administrative penalties | Levied on EACH trustee personally | Levied ONCE on the company |
| Single-member fund | Needs a second person | Sole director permitted |
| Succession on death/incapacity | Fund structure breaks; 6-month fix window (s 17A(4)) | Continuity via directorship |

At the 2026-27 penalty unit of $364, a 60-penalty-unit breach (lending, borrowing, in-house assets) costs $21,840 -- **per individual trustee** ($43,680 for a couple) but once for a corporate trustee. Flag this when a new fund file shows individual trustees.

### 3.3 Registration checklist (new fund)

1. Execute trust deed, appoint trustees, hold initial assets (fund is not legally established until it holds assets).
2. Each trustee/director signs the **ATO trustee declaration (NAT 71089)** within 21 days of appointment; retain 10 years.
3. Register with the ATO within 60 days: **TFN + ABN**, electing regulation under SIS s 19 (irrevocable).
4. Open a fund bank account in the fund/trustee name (asset separation, SIS Reg 4.09A).
5. Obtain an **ESA (electronic service address)** -- required for SuperStream employer contributions (critical under payday super) and for ALL rollovers in/out (SuperStream v3).
6. Prepare the investment strategy (SIS Reg 4.09) BEFORE investing.
7. First-year fund with no assets: request cancellation or 'return not necessary' -- otherwise the SAR is due.

## Section 4 -- Fund taxation (ITAA 1997 Div 295)

### 4.1 Rate structure

| Income class | Rate | Notes |
|---|---|---|
| Assessable contributions (s 295-160) | 15% | Employer + salary-sacrifice + personal deductible (s 290-150 notice) |
| Ordinary earnings on accumulation assets | 15% | Interest, rent, dividends, trust distributions |
| Discounted capital gains | 10% effective | 1/3 discount, asset held 12+ months (NEVER the individuals' 50%) |
| ECPI (retirement-phase earnings) | 0% | Section 4.2 -- method and minimum-payment conditions apply |
| NALI / NALC | 45% | Section 4.3 |
| Non-complying fund | 45% | On income AND (in the first non-complying year) an amount reflecting fund assets |
| No-TFN contributions | +32% | Refundable via offset if TFN quoted within 3 years |

Franking credits offset fund tax and are refundable. Capital losses offset only capital gains (carry forward; losses on segregated pension assets are disregarded entirely).

### 4.2 ECPI -- exempt current pension income

**Segregated method** (ss 295-385): specific assets documented as solely supporting retirement-phase pensions; ALL income (and gains/losses -- disregarded) from those assets is exempt. No actuarial certificate needed for periods of full segregation. A fund 100% in retirement phase at ALL times in the year is deemed segregated for the whole year -- no certificate.

**Proportionate method** (s 295-390): an actuary certifies the exempt proportion of unsegregated income based on average retirement-phase liabilities. **Actuarial certificate required every year the method is used -- obtain it BEFORE lodging the SAR.** Assessable contributions and NALI are never ECPI. Deductions must be apportioned; expenses of gaining ECPI are non-deductible.

**Disregarded small fund assets (s 295-387):** the fund CANNOT use the segregated method (must use proportionate + certificate) when, just before the start of the income year, any member receiving a retirement-phase income stream (from any provider) had a **TSB over $1.6 million**. The $1.6m trigger is a fixed statutory figure -- it has NOT indexed with the transfer balance cap. Exception: a fund 100% in retirement phase at all times in the year escapes the rule (from 2021-22).

**Minimum-payment condition:** ECPI for an account-based pension is only available if the SIS minimum was actually paid for the year (Section 6.1; Example 4).

### 4.3 NALI and NALE -- **AUDIT FLASH POINT**

Income is NALI (s 295-550, taxed at 45%) where it exceeds an arm's-length amount from a non-arm's-length scheme, where a private company dividend or non-fixed trust distribution is involved, or -- since 1 July 2018 -- where the fund incurred **non-arm's-length expenditure** (NALE: expenses lower than arm's length, including nil).

Post the 2024 Act (Treasury Laws Amendment (Support for Small Business and Charities and Other Measures) Act 2024, applied from 2018-19):

- **Specific expense** (tied to a particular asset, e.g. cut-price property maintenance by a related builder): ALL income from that asset is NALI -- including the eventual capital gain.
- **General expense** (e.g. accounting or admin fees): NALI is capped at **2 x (arm's-length expense − actual expense)** -- the "twice the shortfall" rule for SMSFs and small APRA funds.
- Large APRA-regulated funds are carved out of NALE entirely.
- The overall non-arm's-length component cannot exceed the fund's assessable income less deductions, excluding assessable contributions and their deductions.
- Trustee-capacity services (unpaid, own equipment, not through a business) are NOT NALE; discounted services through the trustee's firm ARE (LCR 2021/2). PCG 2020/5's transitional relief for general expenses ended 30 June 2023.

## Section 5 -- Contributions

### 5.1 Acceptance (SIS Reg 7.04)

| Member age | Fund may accept |
|---|---|
| Under 75 | All contribution types -- no work test for acceptance |
| 75+ (from 28 days after the end of the month of the 75th birthday) | Mandated employer (SG) and downsizer ONLY |
| Any age, no TFN quoted | Member contributions must NOT be accepted; employer contributions cop +32% |

**Work test (67-74):** 40 hours in 30 consecutive days -- required only to CLAIM A DEDUCTION for personal contributions (s 290-165), not for acceptance. One-off exemption for recent retirees with TSB < $300,000.

**Downsizer (s 292-102):** age 55+, up to **$300,000 per person** from sale of a home owned 10+ years, contributed within 90 days of settlement with the ATO form; excluded from both caps and acceptance limits; once only; counts to TSB.

**CGT cap:** small business 15-year/retirement exemption proceeds excluded from the NCC cap by election, lifetime limit $1,935,000 (2026-27).

### 5.2 Caps (2026-27)

**Rule 8 -- caps and bring-forward.** Concessional $32,500 (2025-26: $30,000); carry-forward of up to 5 prior years' unused cap only if TSB < $500,000 at 30 June 2026. Non-concessional $130,000 (4 x concessional). Bring-forward by TSB at 30 June 2026: < $1.84m -> $390,000 over 3 years; $1.84m to < $1.97m -> $260,000 over 2 years; $1.97m to < $2.1m -> $130,000 only; >= $2.1m -> nil.

**Excess flows:** excess concessional -> included in the member's assessable income at marginal rates less a 15% offset; may elect to release up to 85%; unreleased excess counts to the NCC cap (no excess concessional charge since 2021-22). Excess non-concessional -> release + associated earnings taxed at marginal rates, or (if retained) 47% on the excess. The FUND's accounting never changes -- assessable contributions stay taxed at 15% in the fund; the excess consequences land on the member.

### 5.3 Member surcharges -- flag, never compute

- **Division 293:** extra 15% on concessional contributions where income + contributions > $250,000 (frozen). ATO-assessed on the member.
- **Division 296 (NEW, first year 2026-27):** extra 15% on the earnings proportion for TSB between $3m and $10m, extra 25% above $10m (thresholds indexed; realised-earnings basis; ATO-assessed on the MEMBER, payable personally or released from super). The SMSF's job is accurate 30 June member balances and market valuations -- the ATO computes from reported data. **Do not attempt the computation in bookkeeping workflows; flag any member with TSB near $3m.**

## Section 6 -- Pensions

### 6.1 Account-based pension minimums (SIS Reg 1.06(9A), Sch 7)

| Age at 1 July (or commencement) | Minimum % of account balance |
|---|---|
| Under 65 | 4% |
| 65-74 | 5% |
| 75-79 | 6% |
| 80-84 | 7% |
| 85-89 | 9% |
| 90-94 | 11% |
| 95+ | 14% |

No reduced ("COVID-halved") rates are in force in 2026-27. Round to the nearest $10; pro-rate by days remaining for pensions commenced mid-year (no minimum if commenced 1-30 June). Payment must LEAVE the fund by 30 June -- journal entries are not payments. Transition-to-retirement income streams (not in retirement phase): 10% maximum applies and the fund earns NO ECPI on them.

**Shortfall consequence:** if the minimum is not met, the pension is taken to have ceased at the start of the income year -- the fund loses ECPI for that pension for the WHOLE year, payments made are treated as lump sums, and a new pension (new documents, new TBC credit, TBAR events) must be commenced to resume. **Catch-up exception** (once only, self-assessed): honest mistake or matters outside trustee control, shortfall <= 1/12 of the annual minimum, caught up as soon as practicable (generally within 28 days of becoming aware) -- then ECPI continues as if paid. Larger or repeat shortfalls need the Commissioner's discretion.

### 6.2 Transfer balance cap and TBAR

- General TBC 2026-27: **$2.1m**. Personal caps differ per member (proportional indexing of unused cap space) -- read the member's ATO TB account, never assume the general cap.
- **TBAR: quarterly for ALL SMSFs since 1 July 2023** (no TSB carve-out), due **28 days after quarter end**: 28 Oct / 28 Jan / 28 Apr / 28 Jul. No nil lodgments required.
- Report: retirement-phase pension commencements and their value, commutations (including commutations to fix excess TB), certain LRBA repayment value-shifts, structured settlement contributions. Pension payments themselves and investment earnings are NOT TB events.
- Excess TB: commute promptly per the determination; respond to a commutation authority within 60 days. Late TBARs make the ATO compute excess determinations off stale data -- a common, avoidable mess.

## Section 7 -- Investment and prohibited-transaction rules

- **Sole purpose test (s 62):** fund maintained solely for retirement/death benefits -- any current-day member benefit (use of the holiday house, art on the wall, wine in the cellar) breaches it.
- **s 65 -- no loans or financial assistance to members/relatives.** Ever, in any amount. 60 penalty units per trustee.
- **In-house assets (Part 8, s 71):** loans to, investments in, or leases to related parties capped at **5% of fund market value** (measured at acquisition and each 30 June). Exceeding at 30 June -> written disposal plan executed before the end of the NEXT year (s 82). Business real property leased at market rent is excluded.
- **s 66 -- acquisitions from related parties prohibited**, except listed securities at market value, business real property at market value, and in-house assets within the 5% limit.
- **Borrowing (s 67):** prohibited except short-term exceptions and a compliant **LRBA (ss 67A-67B)**: single acquirable asset in a separate holding trust, lender recourse limited to that asset. Related-party LRBA terms must satisfy **PCG 2016/5 safe harbour** or evidence arm's-length terms, else the income is NALI: 2026-27 interest **9.35%** real property / **11.35%** listed securities (property rate + 2%); max LVR 70% property / 50% securities; max term 15 years property / 7 years securities; monthly principal-and-interest; registered mortgage/charge; written agreement. (2025-26 rate was 8.95%. Derivation note: the 2026-27 property rate is the RBA indicator rate for investor standard variable housing loans for May 2026 per the PCG 2016/5 methodology; at 20 August 2026 the ATO's QC 18123 table published rows only to 2025-26 -- confirm the ATO row when it appears before relying on it in an audit dispute.)
- **Valuations (SIS Reg 8.02B):** all assets at market value each 30 June, on objective supportable evidence -- unlisted trusts, private companies and property are the perennial audit qualification triggers.
- **Investment strategy (SIS Reg 4.09):** must address risk, return, liquidity, diversification and insurance for members; review REGULARLY -- document a review at least annually and on any significant event (new member, pension commencement, LRBA, market dislocation).

## Section 8 -- Compliance calendar (2025-26 SAR season, 2026-27 year)

| Date | Obligation |
|---|---|
| 28 July / 28 Oct / 28 Jan / 28 Apr | TBAR for the preceding quarter (all SMSFs with TB events) |
| >= 45 days before SAR due | Appoint the ASIC-registered approved SMSF auditor (s 35C) |
| Before lodgment | Audit FINALISED; auditor report (IAR) issued within 28 days of receiving complete documents; actuarial certificate obtained if proportionate ECPI claimed |
| 31 Oct 2026 | 2025-26 SAR: self-lodgers that are newly registered or have overdue prior SARs (pay 1 Dec); tax-agent-lodged new registrants ATO-reviewed at registration |
| 28 Feb 2027 | 2025-26 SAR: other self-lodgers; NEW registrant SMSFs lodging via tax agent (payment due same day) |
| 15 May 2027 | 2025-26 SAR: most continuing tax-agent-lodged SMSFs (agent lodgment program) |
| With every SAR | Supervisory levy $259 paid a year in advance (label L; new funds add $259 at label N = $518 first SAR; wind-ups deduct at label M -- final-year levy usually nil if paid previously) |
| 30 June 2027 | Minimum pensions PAID OUT of the bank; market valuations; in-house asset 5% test; TSB snapshots for caps, DSFA and Div 296 |

SAR more than 2 weeks overdue -> Super Fund Lookup status changes to "Regulation details removed": employers and APRA funds will refuse contributions and rollovers until lodgment catches up.

## Section 9 -- Common breach patterns

| Pattern in the file | Provision | Consequence | Action |
|---|---|---|---|
| EFT to member tagged "loan"/"temporary" | s 65 | 60 PU/trustee ($21,840 at $364/PU); ACR by auditor | Repay + interest; escalate; never reclassify as benefit without condition of release |
| Related-party investments/lease > 5% at 30 June | s 71/s 84 | 60 PU; ATO enforceable undertaking | Written disposal plan before next 30 June end |
| Borrowing outside LRBA (overdraft, margin loan) | s 67 | 60 PU | Clear immediately; document |
| TBAR lodged late/never | TBC reporting | Excess TB determinations off stale data; FTL penalties | Lodge all missed events now; reconcile TB account |
| Proportionate ECPI claimed, no actuarial certificate | s 295-390 | ECPI claim invalid -- amend SAR, tax at 15% | Obtain certificate BEFORE lodgment, always |
| Contributions over caps | Div 291/292 | Member-level ECC/ENCC assessments, release authorities | Check carry-forward/bring-forward eligibility; action release elections in 60 days |
| Benefit paid, no condition of release | s 62 / SIS Reg 6.17 | Illegal early access: marginal tax + penalties, disqualification, possible fund non-compliance (45%) | Refuse to classify as benefit; escalate (R-AU-SF-5) |
| Fund asset used personally (holiday house week) | s 62 sole purpose | Compliance action; NALI risk on related income | Escalate; document cessation |

## Section 10 -- Worked examples

### Example 1 -- Fund tax on mixed income with ECPI and a discounted gain (2026-27)

Two-member fund, one accumulation, one account-based pension; unsegregated; actuary certifies **60% exempt proportion**. Income: rent $32,000, interest $8,000, unfranked dividends $10,000 (= $50,000 ordinary); gross capital gain $30,000 on shares held 3 years; employer + salary-sacrifice contributions $30,000; general admin expenses $4,000.

```
Net capital gain      = $30,000 x (1 - 1/3)           = $20,000
Non-contribution base = $50,000 + $20,000             = $70,000
ECPI                  = 60% x $70,000                 = $42,000
Deductible expenses   = 40% x $4,000                  = $1,600   (ECPI share non-deductible)
Taxable income        = $30,000 + $70,000 - $42,000 - $1,600 = $56,400
Gross tax             = 15% x $56,400                 = $8,460
Payable with SAR      = $8,460 + $259 levy            = $8,719
```

The gain's effective rate here: net gain $20,000, taxed share 40% = $8,000, tax $1,200 = 4.0% of the gross $30,000 (10% without ECPI). Contributions are NEVER sheltered by ECPI.

### Example 2 -- NALE on a general expense (2x rule)

The trustee's accounting firm charges the fund $1,000 for 2026-27 administration; the arm's-length fee is $3,500. This is a non-arm's-length GENERAL expense.

```
Shortfall = $3,500 - $1,000 = $2,500
NALI      = 2 x $2,500      = $5,000
Tax       = 45% x $5,000    = $2,250  (vs $750 at 15% -- a $1,500 penalty effect)
```

Cap check: NALC cannot exceed assessable income less deductions excluding contributions -- here $60,000, so not binding. Contrast: if the discount had been a SPECIFIC expense on a rental property, ALL of that property's income AND its eventual capital gain would be NALI at 45%. Unpaid trustee-capacity work with the trustee's own equipment is not NALE (LCR 2021/2).

### Example 3 -- Excess concessional contributions flow

Member (TSB $600,000 -- no carry-forward) receives SG + salary sacrifice totalling $40,000 in 2026-27 against the $32,500 cap.

```
Fund:   taxes all $40,000 at 15%                        = $6,000  (unchanged)
Excess  = $40,000 - $32,500                             = $7,500
Member: assessable at marginal 39% (37% + 2% Medicare)  = $2,925
        less 15% offset ($7,500 x 15%)                  = -$1,125
        net extra personal tax                          = $1,800
```

Member may elect to release up to 85% of the excess ($6,375) from the fund; unreleased excess also counts toward the $130,000 NCC cap. Nothing is amended in the fund's SAR.

### Example 4 -- Minimum pension shortfall kills ECPI

Member aged 76 at 1 July 2026; pension balance $480,000. Minimum = 6% x $480,000 = **$28,800**. The fund pays only $22,000 by 30 June 2027 -- shortfall $6,800.

The self-assessed catch-up exception is unavailable: $6,800 exceeds 1/12 of the minimum ($2,400). Result: the pension is taken to have ceased 1 July 2026; the fund claims NO ECPI for that interest all year; the $22,000 paid is treated as lump sums; restarting requires fresh pension documents, a new TBC credit and TBAR events (cessation/commencement). Had the shortfall been <= $2,400 from an honest mistake and topped up within about 28 days of discovery, the trustee could self-assess the exception -- once ever; anything else needs the Commissioner's discretion.

## Section 11 -- Provenance

| Topic | Source |
|---|---|
| Fund definition, trustee rules | SIS Act s 17A, s 17B, s 120 (disqualified persons), s 104A (trustee declaration) |
| Sole purpose; lending; acquisitions; borrowing; in-house assets | SIS Act ss 62, 65, 66, 67, 67A-67B, Part 8 (ss 71, 82-85); penalties s 166 ($364/penalty unit from 1 July 2026, Crimes Act s 4AA) |
| Audit and SAR | SIS Act ss 35C, 35D; ato.gov.au "Your SMSF auditor" (45-day appointment); "Lodge SMSF annual returns" (QC 23331) |
| Supervisory levy amount and advance mechanics | ato.gov.au "SMSF supervisory levy" (QC 35359); SAR 2026 instructions label L ($259) |
| Fund tax, contributions, no-TFN, CGT discount | ITAA 1997 Div 295 (s 295-160 assessable contributions); ato.gov.au "How SMSFs are taxed" (QC 23341) |
| ECPI methods, DSFA $1.6m trigger | ITAA 1997 ss 295-385, 295-387, 295-390; ato.gov.au "Exempt current pension income" (QC 21546); TD 2014/7 |
| NALI/NALE 2x general-expense design | ITAA 1997 s 295-550 as amended by Treasury Laws Amendment (Support for Small Business and Charities and Other Measures) Act 2024; LCR 2021/2; PCG 2020/5 (transition ended 30 June 2023) |
| Contribution acceptance, caps, downsizer | SIS Reg 7.04; ITAA 1997 Divs 290-293 (ss 290-150, 290-165), Subdivs 291/292, s 292-102; ato.gov.au contribution caps pages |
| Division 296 | Building a Stronger and Fairer Super System Act 2026 (first year 2026-27) |
| Pension minimums and shortfall exception | SIS Reg 1.06(9A), Sch 7; ato.gov.au "Income stream (pension) rules and payments" + "Exception to minimum pension payment requirements" |
| TBC / TBAR | ITAA 1997 Div 294; ato.gov.au "When to lodge a transfer balance account report for SMSFs" (quarterly, 28 days) |
| LRBA safe harbour | PCG 2016/5 (2026-27: 9.35% property / 11.35% listed securities) |
| Valuations; investment strategy; separation | SIS Regs 8.02B, 4.09, 4.09A; ato.gov.au "Guide to valuing SMSF assets" |
| Deductions (audit, actuarial, levy) | TR 93/17 |

All ATO figures verified against ato.gov.au on 20 August 2026.

### Prohibitions

- NEVER give investment, product or contribution-strategy advice (R-AU-SF-1 -- AFSL boundary)
- NEVER compute Division 296 or Division 293 liabilities -- flag and escalate
- NEVER claim ECPI without checking method eligibility, minimum payments, and (proportionate) the actuarial certificate
- NEVER apply the individuals' 50% CGT discount to a fund (1/3 only)
- NEVER treat NALI as 15% income, or net capital losses against segregated-asset gains
- NEVER accept a related-party transaction value without qualified market evidence
- NEVER classify a payment to a member as a benefit without a documented condition of release
- NEVER assume the general $2.1m TBC applies to a member -- personal caps differ
- NEVER lodge (or treat as lodgeable) a SAR before the audit is finalised
- NEVER present figures as definitive

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
