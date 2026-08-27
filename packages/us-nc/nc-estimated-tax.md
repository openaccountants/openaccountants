---
name: nc-estimated-tax
description: Use this skill whenever asked about North Carolina individual quarterly estimated income tax. Trigger on phrases like "NC estimated tax", "Form NC-40", "NC quarterly payments", "NC safe harbor", "Form D-422", "NC underpayment penalty", "do I need to make NC estimates".
jurisdiction: US-NC
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NC Estimated Tax

## North Carolina Individual Estimated Income Tax Skill — Form NC-40

> **Scope.** This skill covers North Carolina Form NC-40 (Individual Estimated Income Tax) and Form D-422 (Underpayment of Estimated Tax by Individuals) for full-year NC resident individuals — sole proprietors, freelancers, independent contractors, partners, S-corporation shareholders, and W-2 earners with insufficient withholding. Tax year 2025 (returns and final quarterly payment filed in early 2026) and tax year 2026 prospective planning.
>
> **Out of scope.** Estate and trust estimated tax (Form D-407), pass-through entity estimated tax, corporate estimated tax (Form CD-429), multistate apportionment, part-year and nonresident estimates. See refusal catalogue.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing. Items flagged `[VERIFY:]` require independent confirmation against current NCDOR guidance.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual quarterly estimated income tax |
| Jurisdiction | North Carolina (US-NC) |
| Tax year | 2025 (final installment Jan 15 2026); 2026 prospective |
| Primary form | Form NC-40 (quarterly vouchers) |
| Underpayment form | Form D-422 + Form D-422A (annualized worksheet) |
| Tax structure | Flat rate |
| Rate (TY 2025) | 4.25% |
| Rate (TY 2026) | 3.99% |
| Underpayment interest rate (Jan–Jun 2026) | 7% annual |
| Threshold to require estimates | $1,000 expected liability after withholding & credits |
| Tax authority | North Carolina Department of Revenue (NCDOR) |
| Website | https://www.ncdor.gov |
| Statute | N.C.G.S. § 105-163.15 (individual estimated tax) |
| Interest authority | N.C.G.S. § 105-241.21; rate set under § 105-241.21(a) |

**Sources:**
- NCDOR, Estimated Income Tax page: https://www.ncdor.gov/taxes-forms/individual-income-tax/estimated-income-tax
- NCDOR, 2025 Form NC-40 Individual Estimated Income Tax: https://www.ncdor.gov/2025-nc-40-individual-estimated-income-tax/open
- NCDOR, 2025 Form D-422 Underpayment of Estimated Tax by Individuals: https://www.ncdor.gov/taxes-forms/individual-income-tax/individual-income-tax-forms-instructions/2025-form-d-422-underpayment-estimated-tax-individuals
- NCDOR, Interest Rate January–June 2026 Memorandum: https://www.ncdor.gov/interest-rate-memo-jan-jun-2026pdf/open
- NCDOR, Interest Overview: https://www.ncdor.gov/taxes-forms/policies/penalties-and-interest/interest-overview
- Session Law 2023-134 (rate phase-down schedule)
- N.C. Gen. Stat. § 105-163.15

## Section 2: Quick reference

### The four quarterly due dates (TY 2025 calendar-year filers)

**Quarterly due dates table**

| Installment | Period covered | Due date |
| --- | --- | --- |
| Q1 | Jan 1 – Mar 31, 2025 | April 15, 2025 |
| Q2 | Apr 1 – May 31, 2025 | June 15, 2025 |
| Q3 | Jun 1 – Aug 31, 2025 | September 15, 2025 |
| Q4 | Sep 1 – Dec 31, 2025 | January 15, 2026 |

- **Jan 31 exception** — The January 15 (Q4) payment may be skipped if the full Form D-400 return is filed and the entire balance is paid by January 31, 2026.  _(NCDOR Estimated Income Tax page; G.S. § 105-163.15(d))_

### Threshold to require quarterly estimates

- **Threshold requiring NC estimates** — $1,000 USD (Tax shown due on return, reduced by NC withholding and allowable tax credits, is $1,000 or more; applies regardless of how much income is non-wage.)  _(NCDOR NC-40 Instructions; G.S. § 105-163.15(a))_

`[VERIFY:]` Some commentary suggests NC may treat the threshold as lower in specific transitional years. Current NCDOR guidance for 2025 and 2026 explicitly uses $1,000.

### Safe harbor (no underpayment interest)

- **Safe harbor calculation** — Combined withholding plus timely estimated payments must equal at least the smaller of: 1. 90% of current-year tax, OR 2. 100% of prior-year tax (prior year must cover a full 12 months), OR 3. 110% of prior-year tax if prior-year NC AGI > $150,000 ($75,000 if MFS).  _(NCDOR NC-40 Instructions; G.S. § 105-163.15(c))_

`[VERIFY:]` Confirm the 110% high-income variant remains in effect for TY 2025 — NCDOR mirrors the federal § 6654 structure, and the LegalClarity summary explicitly confirms the $150,000/$75,000 thresholds, but the statute text should be read alongside any annual NCDOR memo.

### Flat tax rates (use for projecting current-year liability)

**Flat tax rates table**  _(Session Law 2023-134)_

| Tax year | Rate | Source |
| --- | --- | --- |
| 2024 | 4.50% | Session Law 2023-134 |
| 2025 | 4.25% | Session Law 2023-134 |
| 2026 | 3.99% | Session Law 2023-134 |
| 2027 | 3.49% (triggered) | Session Law 2023-134; revenue trigger expected to be met |
| 2028+ | Scheduled to 2.99% then ultimately 2.49% by 2030 | `[VERIFY:]` confirm final-year phase-down legislation |

### Current underpayment interest rate

**Current underpayment interest rate table**  _(NCDOR Interest Rate Memos)_

| Period | Annual rate | Source |
| --- | --- | --- |
| Jul 1 – Dec 31, 2025 | 7% | NCDOR Interest Rate Memo Jul–Dec 2025 |
| Jan 1 – Jun 30, 2026 | 7% | NCDOR Interest Rate Memo Jan–Jun 2026 |

- **Rate-setting rule** — Rate is set by the Secretary of Revenue under G.S. § 105-241.21(a), must fall between 5% and 16%, and is published on or before December 1 (for the following Jan–Jun period) and June 1 (for the following Jul–Dec period).  _(G.S. § 105-241.21(a))_

### Payment methods

**Payment methods table**

| Method | Detail |
| --- | --- |
| NCDOR e-Services (online) | https://eservices.dor.nc.gov — free; bank draft (eCheck) or credit card (convenience fee applies) |
| Paper check + NC-40 voucher | Mail to NCDOR, PO Box 25000, Raleigh, NC 27640-0630 |
| Approved tax software | TurboTax, Drake, ProSeries, etc. — submits via NCDOR API |

## Section 3: Threshold determination — when MUST you make estimates

### The $1,000 test

- **Required-to-make-estimates test** — A NC resident individual is required to make estimated tax payments if all of the following are true: 1. Expected NC tax liability for the year minus expected NC withholding and allowable credits ≥ $1,000, AND 2. The taxpayer did not satisfy the prior-year safe harbor through withholding alone.  _(G.S. § 105-163.15(a))_

### Decision tree

```
Step 1: Project current-year NC tax
        = (Federal AGI ± NC modifications − NC std/itemized − child deduction) × rate

Step 2: Subtract projected NC withholding (W-2 Box 17, 1099-NEC NC withhold)

Step 3: Subtract projected NC credits (D-400TC)

Step 4: Is result ≥ $1,000?
        - NO  → No estimates required. Underpayment penalty cannot apply (G.S. § 105-163.15(e)).
        - YES → Continue to Step 5.

Step 5: Does prior-year withholding alone ≥ prior-year tax (× 110% if AGI > $150k)?
        - YES → No estimates required; safe harbor met by withholding alone.
        - NO  → Estimates required. Compute required annual payment (Section 5).
```

### First-year filers

- **First-year filer carve-out** — A taxpayer with no NC return for the immediately preceding tax year (e.g., new NC resident, recent graduate) cannot use the prior-year safe harbor — only the 90% current-year safe harbor is available.  _(`[VERIFY:]` Confirm NC's first-year carve-out language tracks federal § 6654(d)(1)(B); the LegalClarity summary characterizes this as a "one-year grace period" but the statutory effect is that no penalty can compute without a prior-year benchmark.)_

### Income types that commonly trigger the threshold

- Schedule C net profit (sole prop / SMLLC disregarded)
- Schedule E partnership K-1 income (NC source)
- S-corp K-1 distributive share
- Rental income net of expenses
- Capital gains (NC taxes at the flat rate, no preferential rate)
- IRA / 401(k) distributions without withholding
- Social Security — **NOT** taxed by NC, so does not increase NC liability
- Marketplace facilitator earnings (1099-K)

## Section 4: The safe-harbor calculation

NC's safe harbor mirrors federal § 6654 in structure but uses NC tax figures throughout.

### The three-prong test (taxpayer satisfies ANY one)

**Three-prong test table**

| Prong | Calculation | Applies to |
| --- | --- | --- |
| **A** | Withholding + estimates ≥ 90% × current-year NC tax | All taxpayers |
| **B** | Withholding + estimates ≥ 100% × prior-year NC tax | Prior-year NC AGI ≤ $150,000 (or ≤ $75,000 MFS) |
| **C** | Withholding + estimates ≥ 110% × prior-year NC tax | Prior-year NC AGI > $150,000 (or > $75,000 MFS) |

### Required annual payment (RAP)

- **RAP formula** — RAP = smaller of: (a) 90% × current-year NC tax (Form D-400, Line 17 after credits, before payments); (b) 100% × prior-year NC tax [or 110% if AGI threshold exceeded]. This RAP figure feeds Form D-422 Part I, Line 8 as the "required annual payment."  _(Form D-422 Part I, Line 8)_

### Worked safe-harbor calc — moderate income

> Taxpayer: NC resident, single, freelance developer.
> Prior-year (2024) NC tax (D-400 Line 17): $7,200. Prior-year NC AGI: $108,000.
> Current-year (2025) projected NC tax: $9,000.

**Moderate-income prong table**

| Prong | Calculation | Amount |
| --- | --- | --- |
| A — 90% current year | $9,000 × 0.90 | $8,100 |
| B — 100% prior year | $7,200 × 1.00 | $7,200 |

110% high-income variant does not apply ($108k ≤ $150k threshold). RAP = lower of $8,100 or $7,200 = $7,200. Each quarterly installment under the regular method = $7,200 / 4 = $1,800.

### Worked safe-harbor calc — high-income

> Taxpayer: NC resident, MFJ. Prior-year (2024) NC tax: $18,400.
> Prior-year NC AGI: $312,000 (> $150,000 threshold → 110% applies).
> Current-year (2025) projected NC tax: $22,000.

**High-income prong table**

| Prong | Calculation | Amount |
| --- | --- | --- |
| A — 90% current year | $22,000 × 0.90 | $19,800 |
| C — 110% prior year | $18,400 × 1.10 | $20,240 |

RAP = lower of $19,800 or $20,240 = $19,800. Each quarterly installment = $19,800 / 4 = $4,950.

> **Practical tip.** When the 110% rule applies and current-year income is projected to drop, choosing the 90% current-year prong avoids over-payment. When current-year income is projected to spike, locking in the 110% prior-year prong avoids penalty exposure on growth.

## Section 5: Quarterly installment amounts — regular method

### The simple split

- **Installment formula** — Installment = Required Annual Payment ÷ 4. Each installment is then reduced by NC withholding for that period to arrive at the cash payment needed by the due date.

### Withholding crediting

- **Withholding crediting rule** — NC withholding (from W-2s, NC 1099 withholding, pension withholding) is treated as paid evenly across the four installment periods unless the taxpayer elects otherwise on Form D-422 (e.g., to assign actual period-by-period withholding for a year-end bonus).  _(NCDOR D-422 instructions; mirrors federal § 6654(g))_

### Worked installment schedule

> Same facts as moderate-income example above. RAP = $7,200. Projected NC withholding from a small W-2 = $1,200 (treated as $300/quarter).

**Worked installment schedule table**

| Quarter | Due date | Required installment | Withholding credit | Net NC-40 payment |
| --- | --- | --- | --- | --- |
| Q1 | Apr 15, 2025 | $1,800 | $300 | **$1,500** |
| Q2 | Jun 15, 2025 | $1,800 | $300 | **$1,500** |
| Q3 | Sep 15, 2025 | $1,800 | $300 | **$1,500** |
| Q4 | Jan 15, 2026 | $1,800 | $300 | **$1,500** |
| **Total** |  | **$7,200** | **$1,200** | **$6,000** |

## Section 6: Annualized income installment method (Form D-422A)

Used when income is lumpy or seasonal — large Q3 or Q4 capital gain, freelance project completion bonus, partnership distribution late in the year. The annualized method allows the taxpayer to "back-load" payments into the period when income is actually earned, avoiding penalty on earlier installments.

### How it works (conceptual)

- **Annualized method steps** — For each cumulative period (3 months, 5 months, 8 months, 12 months), compute: 1. Cumulative NC AGI through that period; 2. Annualize: multiply by annualization factor (4, 2.4, 1.5, 1.0); 3. Compute NC tax on annualized amount; 4. Multiply by applicable percentage (22.5%, 45%, 67.5%, 90%); 5. Subtract prior cumulative installments. Result: the annualized installment for that quarter, compared against the regular installment — the smaller of the two is the required installment for that period (the difference rolls forward to later quarters).

### Annualization factors and percentages

**Annualization factors table**  _(Form D-422A Annualized Income Installment Worksheet; mirrors federal Schedule AI of Form 2210)_

| Installment | Months in period | Annualization factor | Cumulative % required |
| --- | --- | --- | --- |
| 1 (Apr 15) | 3 (Jan–Mar) | 4.0 | 22.5% |
| 2 (Jun 15) | 5 (Jan–May) | 2.4 | 45.0% |
| 3 (Sep 15) | 8 (Jan–Aug) | 1.5 | 67.5% |
| 4 (Jan 15) | 12 (Jan–Dec) | 1.0 | 90.0% |

### All-or-nothing election

- **All-or-nothing election rule** — If the annualized method is used for any one installment, it MUST be used for ALL four installments.  _(D-422A instructions)_

### Worked example — Q3 income spike

> Taxpayer: NC freelance developer. Steady income Jan–Aug ~ $4,000/month. Closes a large project September with $80,000 lump sum. NC tax projection for full year: $6,500 (steady) + $3,400 (Q3 spike) = $9,900. Prior-year NC tax: $7,800. RAP = lower of (90% × $9,900 = $8,910) or ($7,800) = **$7,800**.

**Regular method** would require $1,950 per quarter — but the taxpayer doesn't have the cash in Q1/Q2 because the big income hasn't arrived.

**Annualized method:**

**Annualized worked example table**

| Period | Cumulative NC AGI | Annualized AGI | Annualized NC tax (4.25%) | × cumulative % | Less prior installments | **This quarter** |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 (3 mo) | $12,000 | $48,000 | ~$1,500 (after deductions) | × 22.5% = $338 | — | **$338** |
| Q2 (5 mo) | $20,000 | $48,000 | ~$1,500 | × 45.0% = $675 | − $338 | **$337** |
| Q3 (8 mo) | $112,000 | $168,000 | ~$6,650 | × 67.5% = $4,489 | − $675 | **$3,814** |
| Q4 (12 mo) | $128,000 | $128,000 | ~$4,930 | × 90.0% = $4,437 | − $4,489 | **$0** (or wait — see note) |

> **Note.** The Q4 cumulative requirement ($4,437) can be less than already paid ($4,489) when income decelerates after Q3. In that case the Q4 installment falls to zero. Form D-422 then carries the "excess Q3" forward as a credit toward any remaining shortfall — interest on any earlier underpayment is still computed period by period.

`[VERIFY:]` These illustrative numbers approximate the mechanics; an actual return uses D-422A line by line with the precise NC AGI, NC standard deduction (annualized), and child deduction (annualized). Run the worksheet against the live taxpayer facts before relying on figures.

## Section 7: Form NC-40 vouchers — line by line

### Voucher anatomy

Form NC-40 is a single page producing four detachable vouchers (each labeled with the installment number and due date). When generated through NCDOR e-Services, the form is personalized with the taxpayer's SSN, name, and address.

### Voucher fields

**Voucher fields table**

| Field | Description | How to populate |
| --- | --- | --- |
| SSN (primary) | Primary taxpayer Social Security Number | 9 digits, no dashes on voucher |
| SSN (spouse) | If MFJ, second SSN | Required if filing jointly and joint estimate |
| Name(s) | Last name first, then first name(s) | Match D-400 filing |
| Address | NC mailing address | Update on file if moved |
| Installment number | 1, 2, 3, or 4 | One voucher per quarter |
| Amount of payment | Dollars only (round) | Match check / e-payment |
| Tax year | "2025" for TY 2025 vouchers |  |

### Generating NC-40

1. Visit https://eservices.dor.nc.gov/vouchers/nc40.jsp
2. Enter name, SSN, and (if joint) spouse SSN
3. Enter amounts and select installment(s)
4. Print PDF — separate vouchers per quarter
5. Mail with check made payable to **N.C. Department of Revenue**
6. Write SSN and "2025 NC-40" on the memo line of the check

### Joint vs. separate filing

- **Joint vs separate filing rules** — If both spouses anticipate filing MFJ, file a joint NC-40 with both SSNs and one combined payment per quarter. If spouses anticipate filing MFS, each must file his/her own NC-40 with individual payments. If estimated payments were made jointly but the couple ultimately files MFS, the joint payments may be allocated between the spouses in any proportion they agree on each D-400; allocations must reconcile to the total paid.  _(NCDOR D-400 Instructions, "Estimated Tax Paid" section)_

### Extension to file is NOT extension to pay

- **Extension does not extend payment deadline** — A federal Form 4868 or NC application for extension extends the filing deadline (D-400 to October 15) but does NOT extend the payment deadline. The Q4 installment due January 15 and any balance due April 15 still accrues interest from the original due date.  _(NCDOR "Extensions" page; G.S. § 105-263)_

## Section 8: Form D-422 — underpayment penalty mechanics

Form D-422 computes interest on underpayments installment by installment. It is filed with Form D-400 when an underpayment exists, OR NCDOR computes it automatically and bills the taxpayer (in which case D-422 is not required — but preparing it yourself avoids surprises and is the default for any return with shortfall).

### Part I — Required Annual Payment (Lines 1–8)

**Part I lines table**

| Line | Description |
| --- | --- |
| 1 | Current-year NC tax (D-400 Line 17 after credits) |
| 2 | 90% × Line 1 |
| 3 | Prior-year NC tax (full 12 months) |
| 4 | 100% (or 110% if AGI > $150k / $75k MFS) × Line 3 |
| 5 | Smaller of Line 2 or Line 4 |
| 6 | NC withholding (W-2 + 1099 + pension) |
| 7 | Line 5 − Line 6 |
| 8 | **Required annual payment** = Line 7 (if ≥ $1,000) |

- **Line 8 stop rule** — If Line 8 < $1,000, no penalty applies and D-422 stops here.

### Part II — Short Method (Lines 9–14)

- **Short method eligibility** — Available only if: No estimated payments were made, OR All four installments were equal and paid on the regular due dates. If either condition is true, the taxpayer can compute interest in aggregate rather than period by period.

### Part III (regular method) — Interest Per Installment

**Part III lines table**

| Line | Description |
| --- | --- |
| 15 | Required installment (Line 8 ÷ 4, OR D-422A annualized amount) |
| 16 | Estimated tax + withholding applied to this period |
| 17 | Underpayment (Line 15 − Line 16) |
| 18 | Number of days underpayment outstanding |
| 19 | Interest = Line 17 × annual rate × (Line 18 / 365) |

- **Total interest carryover** — Total interest = sum of Line 19 across all four columns → carry to D-400 Line 27 (or equivalent line on current-year return) as "Interest on the underpayment of estimated income tax."

### The "7-day rule" — period-by-period netting

- **No netting across quarters** — Interest does NOT net across quarters the way most taxpayers expect. An overpayment in Q3 does NOT retroactively cure an underpayment in Q1 — it only stops Q3's clock prospectively. The taxpayer can owe interest on a Q1 shortfall even if the year-end total paid in equals or exceeds the RAP.

> `[VERIFY:]` Some practitioner guides describe a 7-day "grace" rule derived from the date-counting convention in the D-422 instructions (i.e., a payment received within ~7 days of the next installment due date is sometimes treated as paid on the next due date for interest-tolling purposes). Confirm against the current-year D-422 instructions before claiming any such grace in a return.

### Penalty waiver / reasonable cause

- **Waiver conditions** — NCDOR may waive interest on underpayment of estimated tax in cases of: Casualty, disaster, or other unusual circumstances making penalty inequitable, OR Retirement after age 62 or disability during the tax year, OR First-year filer with no prior return. Submit a written waiver request with the return attaching documentation.  _(G.S. § 105-163.15(e); NCDOR D-422 instructions waiver section)_

> NCDOR has no statutory authority to abate the underpayment interest itself purely on hardship grounds — the waiver is narrow and codified.

## Section 9: Payment methods — operational detail

### NCDOR e-Services (recommended)

1. Go to https://eservices.dor.nc.gov
2. Select "File and Pay" → "Pay Individual Income Tax" → "Estimated Income Tax (NC-40)"
3. Enter SSN, name, payment amount, tax year, installment number
4. Choose bank draft (no fee) or credit/debit card (convenience fee ~2%)
5. Receive confirmation number — save this as proof of timely payment

### Paper check + voucher

- **Paper check steps and postmark rule** — 1. Generate NC-40 PDF (Section 7) 2. Write check payable to N.C. Department of Revenue 3. Write SSN, "2025 NC-40," and installment number (1 of 4, etc.) on memo line 4. Mail to: ``` North Carolina Department of Revenue PO Box 25000 Raleigh, NC 27640-0630 ``` 5. Postmark counts as paid date for timeliness — use certified mail for installments mailed close to the deadline.

### Through tax software

Most major software (TurboTax, Drake, ProSeries, UltraTax, Lacerte) can submit NC estimated payments via NCDOR's API, generating a confirmation number. Confirm the payment reflects on the e-Services account after 3–5 business days.

## Section 10: Coordination with federal Form 1040-ES

NC quarterly due dates mirror federal Form 1040-ES exactly — April 15, June 15, September 15, January 15. This permits a single quarterly workflow:

**Federal/NC coordination table**

| Step | Federal | North Carolina |
| --- | --- | --- |
| Project current-year tax | Federal 1040 + Schedule SE | NC D-400 (using federal AGI as start) |
| Compute safe harbor | 90% / 100% (110% > $150k) | 90% / 100% (110% > $150k) |
| Divide RAP | ÷ 4 (regular method) | ÷ 4 (regular method) |
| File voucher | Form 1040-ES voucher | Form NC-40 voucher |
| Pay | IRS Direct Pay / EFTPS | NCDOR e-Services |

### Key differences

**Key differences table**

| Item | Federal | NC |
| --- | --- | --- |
| Tax structure | Progressive + SE tax | Flat 4.25% (2025) / 3.99% (2026) |
| SE tax | 15.3% via Schedule SE | NC has **no separate SE tax** |
| Capital gains | Preferential 0/15/20% | Taxed at flat rate (no preference) |
| Underpayment form | Form 2210 | Form D-422 |
| Annualized worksheet | Schedule AI of Form 2210 | Form D-422A |
| Interest rate (Jan–Jun 2026) | Federal short-term + 3% (≈ 8% currently) | 7% NC |
| Jan 31 file-and-pay exception | Available | Available |

### Practical tip

When a taxpayer files MFJ federally and MFJ NC, send one combined quarterly worksheet to the client. Show federal estimate, NC estimate, both due dates, both payment links, and store federal and NC confirmation numbers side by side.

## Section 11: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| NC-EST-T1-01 | Estimated tax required if expected NC tax less withholding & credits ≥ $1,000 | G.S. § 105-163.15(a) |
| NC-EST-T1-02 | Four installments due 4/15, 6/15, 9/15, 1/15 (following year) | G.S. § 105-163.15(b) |
| NC-EST-T1-03 | Jan 15 installment may be skipped if return filed and balance paid by Jan 31 | G.S. § 105-163.15(d) |
| NC-EST-T1-04 | Safe harbor = lower of 90% current-year or 100% prior-year NC tax | G.S. § 105-163.15(c) |
| NC-EST-T1-05 | Prior-year safe harbor = 110% if prior-year NC AGI > $150,000 ($75,000 MFS) | G.S. § 105-163.15(c); `[VERIFY:]` annual NCDOR memo |
| NC-EST-T1-06 | Underpayment interest rate set by Secretary, between 5% and 16% | G.S. § 105-241.21(a) |
| NC-EST-T1-07 | Current rate (Jul 2025 – Jun 2026) = 7% annual | NCDOR Interest Rate Memos |
| NC-EST-T1-08 | If annualized method used for any installment, must use for all four | Form D-422A instructions |
| NC-EST-T1-09 | If RAP < $1,000, no underpayment interest can apply | G.S. § 105-163.15(e) |
| NC-EST-T1-10 | Extension to file does NOT extend time to pay | G.S. § 105-263 |
| NC-EST-T1-11 | Farmers / commercial fishermen (≥ ⅔ gross income from farming/fishing) may pay one installment by Jan 15 OR file and pay by Mar 1 | G.S. § 105-163.15(g) |

## Section 12: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule ID | Situation | Guidance |
| --- | --- | --- |
| NC-EST-T2-01 | **Income spike in mid-year (Q3/Q4)** | Run both regular and annualized methods on D-422A. Annualized often produces lower or zero installments in Q1/Q2 with most payment owed in Q3/Q4. |
| NC-EST-T2-02 | **Change in filing status mid-year (divorce, marriage)** | Prior-year safe harbor uses the prior-year return as filed. Spouses who divorced mid-year should allocate prior-year tax in proportion to separate tax liabilities had they filed separately — judgment required. |
| NC-EST-T2-03 | **Large one-time gain (sale of business, real estate)** | Consider annualized method for the quarter of sale. Project full-year liability including the gain to test whether the 90% current-year safe harbor still beats prior-year. |
| NC-EST-T2-04 | **Move to NC mid-year** | Cannot use NC prior-year safe harbor (no NC return last year). Only the 90% current-year prong is available. Build cumulative income from NC residency start date. |
| NC-EST-T2-05 | **Federal return amended after Q1 NC-40 paid** | If federal AGI changes, NC AGI changes too. Adjust later quarterly NC-40 payments to track new full-year projection; an over-paid Q1 cannot be refunded mid-year but applies to year-end. |
| NC-EST-T2-06 | **PTET election by partnership / S-corp** | If the entity elected NC PTET, the owner's share of NC tax paid by the entity reduces the owner's NC liability — may eliminate the owner's need for personal estimates. Confirm entity actually paid PTET timely. |
| NC-EST-T2-07 | **Retirement during year (age 62+)** | Penalty waiver may apply under G.S. § 105-163.15(e) for the year of retirement and the following year. File written waiver request. |
| NC-EST-T2-08 | **Bonus / withholding adjustment via W-4** | Increasing withholding late in the year is treated as paid **evenly across all four periods** by default — this can retroactively cure earlier underpayments. Useful tool when an underpayment is identified late. |

## Section 13: Worked examples

### Example 1 — Steady-income NC freelancer ($150k expected)

> **Taxpayer:** Single, full-year NC resident, freelance graphic designer.
> Projected 2025 NC AGI: $150,000. No W-2 withholding. No NC credits.
> Prior-year (2024) NC tax: $5,800. Prior-year NC AGI: $138,000.

**Step 1 — Project 2025 NC tax:**
- Federal AGI proxy ≈ NC AGI = $150,000
- NC standard deduction (single) = $12,750
- NC taxable income = $137,250
- NC tax = $137,250 × 4.25% = **$5,833**

**Step 2 — Safe harbor:**
- 90% current year = $5,833 × 0.90 = $5,250
- 100% prior year = $5,800 (110% rule does not apply — prior AGI $138k ≤ $150k)
- **RAP = lower = $5,250**

**Step 3 — Test threshold:** $5,833 expected tax, zero withholding, shortfall $5,833 ≥ $1,000 → estimates required.

**Step 4 — Installments:**

**Example 1 installments table**

| Q | Due | Amount |
| --- | --- | --- |
| 1 | Apr 15, 2025 | $1,313 |
| 2 | Jun 15, 2025 | $1,313 |
| 3 | Sep 15, 2025 | $1,313 |
| 4 | Jan 15, 2026 | $1,311 |
| **Total** |  | **$5,250** |

**Step 5 — Year-end:** If actual 2025 NC tax is $5,833 and $5,250 was paid in estimates, balance due with D-400 = $583 by April 15, 2026. Safe harbor met → no D-422 interest.

### Example 2 — Self-employed with Q3 income spike (annualized method)

> **Taxpayer:** Single, NC resident, software consultant. Steady income $5,000/month Jan–Aug. Closes a $90,000 platform deal in September. Final 2025 NC AGI = $130,000. Prior-year NC tax: $4,400.

**Projected NC tax:**
- NC AGI $130,000 − $12,750 std ded = $117,250 taxable
- Tax = $117,250 × 4.25% = **$4,983**

**Safe harbor:** lower of (90% × $4,983 = $4,485) or ($4,400) = **$4,400**.

**Regular method** = $1,100 per quarter — but the taxpayer doesn't have cash to pay $1,100 in Q1 and Q2 against ~$10,000 of cumulative income.

**Annualized method (D-422A) by period:**

**Example 2 annualized table**

| Period | Cum NC AGI | Annualized | Annual NC tax (after std ded) | × cum % | Less prior | **This Q** |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 (3 mo) | $15,000 | $60,000 | $2,009 | × 22.5% = $452 | — | **$452** |
| Q2 (5 mo) | $25,000 | $60,000 | $2,009 | × 45.0% = $904 | − $452 | **$452** |
| Q3 (8 mo) | $130,000 | $195,000 | $7,744 | × 67.5% = $5,227 | − $904 | **$4,323** (capped at RAP balance) |
| Q4 (12 mo) | $130,000 | $130,000 | $4,983 | × 90.0% = $4,485 | − $4,485 already paid | **$0** |

`[VERIFY:]` Approximate; rerun on D-422A with precise NC standard deduction annualized per IRS-aligned convention. The pattern shows: tiny Q1 and Q2, large Q3 catch-up, zero Q4. No penalty results because each installment met its annualized cumulative threshold.

### Example 3 — High-income MFJ with W-2 withholding shortfall

> **Taxpayer:** MFJ, both spouses NC residents. Spouse A: W-2 salary $180,000, NC withholding $7,200. Spouse B: freelance income $130,000, no withholding. Prior-year (2024) NC AGI: $295,000 (>$150,000 → 110% rule applies). Prior-year NC tax: $13,800.

**Projected 2025 NC tax:**
- NC AGI ≈ $310,000 − $25,500 MFJ std ded = $284,500
- Tax = $284,500 × 4.25% = **$12,091**

**Safe harbor:**
- 90% current year = $12,091 × 0.90 = $10,882
- 110% prior year = $13,800 × 1.10 = $15,180
- **RAP = lower = $10,882**

**Test threshold:**
- Expected tax $12,091 − withholding $7,200 = $4,891 ≥ $1,000 → estimates required

**Required quarterly cash payment (after withholding):**
- Withholding credit per quarter = $7,200 ÷ 4 = $1,800
- Required installment per quarter = $10,882 ÷ 4 = $2,721
- Net NC-40 payment per quarter = $2,721 − $1,800 = **$921**

**Example 3 payments table**

| Q | Due | NC-40 Payment |
| --- | --- | --- |
| 1 | Apr 15, 2025 | $921 |
| 2 | Jun 15, 2025 | $921 |
| 3 | Sep 15, 2025 | $921 |
| 4 | Jan 15, 2026 | $920 |
| **Total** |  | **$3,683** |

**Alternative — increase Spouse A's W-2 withholding:** If Spouse A files a new NC-4 to add ~$300/month extra NC withholding ($3,600 annual), total withholding rises to $10,800 → covers 90% safe harbor without any NC-40 payments. Withholding is deemed paid evenly across the year, so this also retroactively cures any Q1/Q2 shortfall. This is the cleanest fix for W-2 dominated households.

## Section 14: Refusal catalogue

- **R-NC-EST-01** — Estate or trust estimated tax  _("NC fiduciary estimated tax (Form NC-EST or D-407 quarterly) is outside this skill's scope. Refer to NCDOR D-407 instructions.")_
- **R-NC-EST-02** — Pass-through entity estimated tax  _("NC PTET estimated payments (Form NC-429 PTE) are covered by a separate pass-through entity skill, not this individual estimated tax skill.")_
- **R-NC-EST-03** — Corporate estimated tax  _("NC corporate estimated tax (Form CD-429) is not covered. See NCDOR corporate estimated tax guidance.")_
- **R-NC-EST-04** — Part-year or nonresident estimates  _("NC part-year and nonresident allocation requires Schedule PN and apportionment logic outside this skill. Refer to a multistate specialist.")_
- **R-NC-EST-05** — Multistate apportionment of self-employment income  _("Apportionment of business income across NC and other states is outside scope. NC taxes residents on all income with credit for taxes paid to other states on D-400TC.")_
- **R-NC-EST-06** — Federal-only quarterly estimates question  _("Federal Form 1040-ES is covered by the us-quarterly-estimated-tax skill, not this NC skill. Use that skill for the federal computation.")_
- **R-NC-EST-07** — Farmers / commercial fishermen with complex special-rule scenarios  _("The farmer/fisherman one-installment rule under G.S. § 105-163.15(g) is mentioned briefly here; complex agricultural / fishing facts require dedicated review.")_

## Section 15: Form mapping

### Form NC-40 (Estimated Income Tax)

**Form NC-40 fields table**

| Voucher field | Description |
| --- | --- |
| Tax year | Year of the underlying return (e.g., 2025) |
| Installment number | 1, 2, 3, or 4 |
| Primary SSN | 9-digit |
| Spouse SSN | If joint estimate |
| Name(s) | Match D-400 |
| Address | NC mailing address |
| Amount enclosed | Cash payment for this installment |

### Form D-422 (Underpayment of Estimated Tax by Individuals)

**Form D-422 parts table**

| Part | Lines | Purpose |
| --- | --- | --- |
| Part I | 1–8 | Required annual payment determination |
| Part II | 9–14 | Short method (only if no estimates made or all four equal & timely) |
| Part III | 15–19 (× 4 columns) | Regular method — interest per installment |

### Form D-422A (Annualized Income Installment Worksheet)

**Form D-422A line groups table**

| Line group | Purpose |
| --- | --- |
| Top | Cumulative NC AGI by period (3, 5, 8, 12 months) |
| Middle | Annualization factor & annualized NC tax |
| Bottom | Applicable percentage × annualized tax → annualized installment |

## Section 16: Provenance + sources

### Primary statutory sources

- **N.C. Gen. Stat. § 105-163.15** — Failure by individual to pay estimated income tax; interest
- **N.C. Gen. Stat. § 105-241.21** — Interest on taxes
- **N.C. Gen. Stat. § 105-263** — Timely filing of mail and extension
- **Session Law 2023-134** (2023 Appropriations Act, Part XLII) — flat rate phase-down schedule

### Primary administrative sources

- NCDOR, Estimated Income Tax page (https://www.ncdor.gov/taxes-forms/individual-income-tax/estimated-income-tax)
- NCDOR, 2025 Form NC-40 + instructions (https://www.ncdor.gov/2025-nc-40-individual-estimated-income-tax/open)
- NCDOR, 2025 Form D-422 + instructions (https://www.ncdor.gov/taxes-forms/individual-income-tax/individual-income-tax-forms-instructions/2025-form-d-422-underpayment-estimated-tax-individuals)
- NCDOR, Form D-422A Annualized Income Installment Worksheet
- NCDOR, Interest Rate Memorandum Jan–Jun 2026 (https://www.ncdor.gov/interest-rate-memo-jan-jun-2026pdf/open)
- NCDOR, Interest Overview (https://www.ncdor.gov/taxes-forms/policies/penalties-and-interest/interest-overview)
- NCDOR, e-Services portal (https://eservices.dor.nc.gov)

### Items flagged for verification

**Items flagged for verification table**

| `[VERIFY:]` item | Reason |
| --- | --- |
| 110% prior-year safe harbor for AGI > $150,000 (MFS > $75,000) | Mirrors federal § 6654(d); confirmed by practitioner summaries but read NCDOR's annual NC-40 instructions for explicit codification |
| 2028+ rate schedule (final phase-down to 2.49% by 2030) | Subject to legislative change; revenue triggers may delay |
| 7-day grace rule on installment payments | Practitioner convention; confirm against current D-422 instructions |
| Specific D-422 line numbers and exact column placement | Confirmed by structure (Part I 1–8, Part II 9–14, Part III installment columns) but verify against current-year PDF before populating |
| First-year filer carve-out | Mirrors federal § 6654(d)(1)(B); confirm NCDOR statutory text |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
