---
name: mi-estimated-tax
description: Use this skill whenever asked about Michigan quarterly estimated income tax for individuals — sole proprietors, single-member LLCs, freelancers, and high-income wage earners with insufficient withholding. Trigger on phrases like "Michigan estimated tax", "MI-1040ES", "MI quarterly payments", "Michigan underpayment penalty", "MI-2210", "MCL 206.301", "Michigan estimated tax safe harbor".
jurisdiction: US-MI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MI Estimated Tax

## Michigan Quarterly Estimated Income Tax — Individuals

> **Scope.** This skill covers Michigan Form MI-1040ES (quarterly estimated income tax vouchers) and Form MI-2210 (underpayment penalty) for full-year Michigan resident individuals who are sole proprietors, single-member LLCs, or W-2 earners with insufficient withholding. It covers the safe-harbor tests under MCL 206.301, the four quarterly installment due dates, the annualized income method for taxpayers with uneven income, and coordination with federal Form 1040-ES.
>
> **Out of scope.** Estate and trust estimated payments (MI-1041ES), S-corp pass-through entity tax (PTET) estimated payments under MCL 206.813 (handled in a separate skill), corporate income tax estimates (Form 4913), multistate apportionment edge cases, and city-level estimated payments (Detroit D-1040ES and similar are filed separately with the city).
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates, thresholds, and interest rates were researched on 2026-05-28 from official Michigan Department of Treasury publications and Revenue Administrative Bulletins. A qualified Michigan professional must review before any payment schedule is acted upon.

## Section 1: Metadata

- **Jurisdiction** — Michigan (US-MI)
- **Tax type** — Individual income tax — estimated payments
- **Primary form** — Form MI-1040ES (quarterly voucher)
- **Penalty form** — Form MI-2210 (Underpayment of Estimated Income Tax)
- **Tax year** — 2026 (vouchers paid April 2026 – January 2027)
- **Authority** — Michigan Department of Treasury
- **Statute** — MCL 206.301 (estimated tax); MCL 205.23 (interest); MCL 205.24 (penalty)
- **Version** — 0.1
- **Last updated** — 2026-05-28
- **Validation** — AI-drafted — Q3 (pending Michigan CPA/EA verification)

### Sources consulted

**Sources consulted**

| # | Source | URL |
| --- | --- | --- |
| 1 | MCL 206.301 — Estimated Tax Installments | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-301 |
| 2 | MCL 205.23 — Interest on underpayments | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-205-23 |
| 3 | 2026 MI-1040ES Vouchers & Instructions | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf |
| 4 | 2025 MI-2210 Underpayment of Estimated Tax | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-2210.pdf |
| 5 | Revenue Administrative Bulletin 2026-1 (H1 2026 interest rate) | https://www.michigan.gov/taxes/rep-legal/rab/2026-revenue-administrative-bulletins/revenue-administrative-bulletin-2026-1 |
| 6 | Revenue Administrative Bulletin 2026-5 (H2 2026 interest rate) | https://www.michigan.gov/taxes/rep-legal/rab/2026-revenue-administrative-bulletins/revenue-administrative-bulletin-2026-5 |
| 7 | Michigan Treasury — Am I Required to Make Estimates? | https://www.michigan.gov/taxes/questions/iit/accordion/estimate/am-i-required-to-make-estimated-tax-payments-1 |
| 8 | Michigan Treasury — Interest Rate Due on Under/Overpayments | https://www.michigan.gov/taxes/interest-rate |
| 9 | Michigan Treasury Online (MTO) portal | https://mto.treasury.michigan.gov/ |

## Section 2: Quick reference

**Quick reference table**

| Item | Value | Source |
| --- | --- | --- |
| Estimated tax threshold | Expected tax > $500 after withholding and credits | MCL 206.301(1) |
| Safe harbor — current year | 90% of current-year tax | MI-1040ES Instr. |
| Safe harbor — prior year (standard) | 100% of prior-year tax (12-month return) | MI-1040ES Instr. |
| Safe harbor — high-income (AGI > $150k) | 110% of prior-year tax | MI-1040ES Instr. `[VERIFY:]` see §5 |
| Safe harbor — farmers/fishermen | 66⅔% of current-year tax | MCL 206.301(4) |
| Q1 due date (TY 2026) | April 15, 2026 | MCL 206.301(1) |
| Q2 due date | June 15, 2026 | MCL 206.301(1) |
| Q3 due date | September 15, 2026 | MCL 206.301(1) |
| Q4 due date | January 15, 2027 | MCL 206.301(1) |
| Michigan flat tax rate (TY 2026) | 4.25% | MCL 206.51 |
| Interest rate — H1 2026 | 8.48% annual / 0.0002324 daily | RAB 2026-1 |
| Interest rate — H2 2026 | 7.85% annual / 0.0002150 daily | RAB 2026-5 |
| Late-payment penalty | 10% of underpayment ($10 min/quarter) | MCL 205.24 |
| Failure-to-file penalty | 25% of tax due ($25 min/quarter) | MCL 205.24 |
| Payment methods | MTO eCheck (free); debit card ($3.95); credit card (2.3%); mail + voucher | Treasury |
| Mail-in address | Michigan Department of Treasury, P.O. Box 30774, Lansing, MI 48909 | MI-1040ES |

## Section 3: Threshold determination — when MUST you make estimates

- **Estimated payment requirement threshold** — An individual must make quarterly estimated payments if the expected annual Michigan tax liability, after subtracting (1) Michigan income tax withholding under MCL 206.351 and (2) all allowable Michigan credits, exceeds $500.  _(MCL 206.301(1))_

### Decision flow

```
Step 1: Compute expected Michigan AGI for TY 2026.
Step 2: Compute Michigan tax at 4.25% (after personal exemptions of $5,800/each).
Step 3: Subtract anticipated Michigan withholding (from W-2 Box 17, 1099 boxes, pension W-4P).
Step 4: Subtract anticipated credits (Homestead Property Tax Credit, Home Heating Credit, etc.).
Step 5: If remainder > $500 → MUST make estimates.
        If remainder ≤ $500 → no estimates required (but voluntary payments allowed).
```

### Common triggers

**Common triggers**

| Situation | Trigger? |
| --- | --- |
| Sole prop / SMLLC with no withholding | Almost always YES once net SE income > ~$13,000 |
| W-2 earner with W-4 set correctly | Usually NO |
| W-2 earner with side gig (Schedule C) | Depends — compute step 5 |
| Retiree with no MI withholding on 1099-R | Yes if subtraction does not zero out tax |
| Capital gains windfall in current year | Yes — may also need annualized method (§7) |
| Both spouses earn — MFJ | Compute on combined liability |

## Section 3: Threshold determination — when MUST you make estimates

`[VERIFY:]` MCL 206.301 uses the singular "person" — joint filers compute the threshold on the combined liability shown on the joint MI-1040. Confirm with 2026 MI-1040ES instructions.

## Section 4: Safe-harbor calculation

- **Safe harbor avoidance of penalty** — A taxpayer who meets any one of the safe harbors avoids the underpayment penalty under MCL 205.24, regardless of the final balance due on the MI-1040.  _(MCL 205.24)_

### Safe harbor 1 — Current-year 90%

- **Current-year safe harbor** — 90% percent (of actual TY 2026 Michigan tax liability, paid through withholding + estimates)  _(MI-1040ES Instr.)_

### Safe harbor 2 — Prior-year 100%

- **Prior-year safe harbor** — Pay at least 100% of the TY 2025 Michigan tax shown on the MI-1040, line 20 (total tax), provided the TY 2025 return covered 12 full months, AND a TY 2025 MI-1040 was actually filed.  _(MI-1040ES Instr.)_

### Safe harbor 3 — High-income prior-year 110%

- **High-income prior-year safe harbor** — If TY 2025 federal AGI exceeded $150,000 ($75,000 if MFS), the prior-year safe harbor is 110% of TY 2025 Michigan tax — not 100%.  _(MI-1040ES Instr.)_

### Safe harbor 3 — High-income prior-year 110%

`[VERIFY:]` Michigan's MI-1040ES 2026 instructions reference the federal §6654(d)(1)(C) higher-income test. The MI safe harbor is presented as "100% (or 110% if AGI > $150k)" by Michigan Treasury and by the official MI-1040ES instructions. Confirm that the AGI threshold language continues to apply at $150,000 for TY 2026 — the figure has not been indexed and mirrors the federal threshold under §6654(d)(1)(C).

### Safe harbor 4 — Farmers, fishermen, seafarers (MCL 206.301(4))

- **Farmer/fisherman/seafarer safe harbor** — If at least two-thirds of expected AGI is from farming, fishing, or seafaring, taxpayer may pay 66⅔% of current-year tax in a single installment by January 15, OR file and pay full balance by March 1 of the following year.  _(MCL 206.301(4))_

### Lower-of test

- **Lower-of test** — The taxpayer pays the lower of (a) the prior-year safe harbor and (b) 90% of current-year. Most software defaults to the prior-year amount because it is fixed and certain. Use current-year 90% only if current-year income has dropped materially.

## Section 5: Regular installment method — four equal payments

- **Regular installment formula** — ``` Required annual payment (RAP) = lower of: (a) 90% × TY 2026 expected Michigan tax (b) 100% (or 110% if high-income) × TY 2025 Michigan tax (c) — for farmers/fishermen — 66⅔% × TY 2026 expected tax Quarterly installment = (RAP − expected TY 2026 withholding) ÷ 4 ```  _(MCL 206.301(2))_

### Timing table — TY 2026

**Timing table — TY 2026**

| Installment | Period covered | Due date | Cumulative % required |
| --- | --- | --- | --- |
| Q1 | Jan 1 – Mar 31, 2026 | April 15, 2026 | 25% |
| Q2 | Apr 1 – May 31, 2026 | June 15, 2026 | 50% |
| Q3 | Jun 1 – Aug 31, 2026 | September 15, 2026 | 75% |
| Q4 | Sep 1 – Dec 31, 2026 | January 15, 2027 | 100% |

### Timing table — TY 2026

- **Deadline shift for weekends/holidays** — If a due date falls on a Saturday, Sunday, or Michigan legal holiday, the deadline shifts to the next business day.  _(MCL 205.27a)_

### Withholding rule

- **Withholding treated as paid evenly** — Michigan, like federal, treats withholding as paid evenly across the four quarters unless the taxpayer elects to treat it as paid when actually withheld. This is favorable to taxpayers whose withholding is back-loaded (e.g., a December bonus with full MI withholding can cover earlier underpayments).

## Section 6: Annualized income method (uneven income)

- **Annualized income method** — For taxpayers whose income arrives unevenly across the year — typical patterns include consulting engagements that close in Q3, capital gains realized in Q4, or seasonal businesses — Michigan permits an annualized income installment method analogous to federal Form 2210 Schedule AI. The method is implemented on Form MI-2210, Part 3 (Annualized Income Worksheet).  _(Form MI-2210, Part 3)_

### Annualization periods

**Annualization periods**

| Period | Months covered | Annualization factor |
| --- | --- | --- |
| Period 1 | Jan 1 – Mar 31 | × 4 |
| Period 2 | Jan 1 – May 31 | × 2.4 |
| Period 3 | Jan 1 – Aug 31 | × 1.5 |
| Period 4 | Jan 1 – Dec 31 | × 1 |

### Mechanics

1. Compute Michigan AGI for each cumulative period (YTD through Mar 31, May 31, Aug 31, Dec 31).
2. Multiply by the annualization factor for that period to get annualized AGI.
3. Subtract pro-rated exemptions and apply 4.25%.
4. Multiply the annualized tax by the cumulative safe-harbor percentage (22.5%, 45%, 67.5%, 90% for the four periods — these are 90% × 25%/50%/75%/100%).
5. Subtract withholding allocated to that period and prior installments paid.
6. Result = required installment for that quarter.

### Worked snippet

**Worked snippet table**

| Period | YTD MI AGI | Annualized AGI | Annualized tax (4.25%) | Cum. required (× factor) | Prior installments | This installment |
| --- | --- | --- | --- | --- | --- | --- |
| 1 (Mar 31) | $8,000 | $32,000 | $1,360 | $306 (22.5%) | 0 | $306 |
| 2 (May 31) | $15,000 | $36,000 | $1,530 | $689 (45%) | $306 | $383 |
| 3 (Aug 31) | $90,000 | $135,000 | $5,738 | $3,873 (67.5%) | $689 | $3,184 |
| 4 (Dec 31) | $140,000 | $140,000 | $5,950 | $5,355 (90%) | $3,873 | $1,482 |

### Worked snippet

Without annualization the consultant would owe $1,488 per quarter (roughly $5,950 ÷ 4). With annualization the Q1 and Q2 payments are tiny because little income had been earned. Total paid across all four quarters is identical, but no underpayment penalty accrues for Q1 and Q2.

## Section 7: Form MI-1040ES voucher — line by line

**Voucher line by line table**

| Voucher line | Field | What to enter |
| --- | --- | --- |
| 1 | Taxpayer's SSN | Primary filer SSN |
| 2 | Spouse SSN (if joint) | Spouse SSN |
| 3 | Filer's name and address | Primary + spouse names; mailing address |
| 4 | Voucher number (1, 2, 3, 4) | Pre-printed; matches quarter |
| 5 | Amount of estimated tax payment | $ amount in whole dollars |
| 6 | Make check payable to | "State of Michigan" — write filer SSN and "2026 MI-1040ES" on memo line |

## Section 7: Form MI-1040ES voucher — line by line

The 2026 MI-1040ES is a four-voucher set. Each voucher is identical except for the period and due date.

### Mail-in destination

- **Mail-in address** — Michigan Department of Treasury P.O. Box 30774 Lansing, MI 48909

### Joint vs separate filers (MCL 206.311)

- **Joint vs separate filer rules** — Joint filers may file a single MI-1040ES voucher set covering both spouses, OR each spouse may file separately. If a joint MI-1040 will be filed, joint estimates are easiest — credits apply to the combined liability. If one spouse later files MFS, the estimates can be allocated by mutual agreement (default allocation per MCL 206.311(2) is by proportion of each spouse's separate tax to the combined tax).  _(MCL 206.311)_

## Section 8: Underpayment penalty — Form MI-2210

When required estimates are not paid (or are paid late or short), MI-2210 calculates: 1. Underpayment penalty — a fixed percentage charge, AND 2. Interest — at the quarterly Treasury rate.

### Penalty component (MCL 205.24)

**Penalty component table**  _(MCL 205.24)_

| Failure | Rate | Minimum |
| --- | --- | --- |
| Failure to pay enough estimate / paid late | 10% of the underpayment | $10 per quarter |
| Failure to file an estimate at all | 25% of the underpayment | $25 per quarter |

### Interest component (MCL 205.23(2))

- **Interest accrual period** — Interest accrues on each quarterly underpayment from the due date of that installment to the earlier of (a) the date the underpayment was paid, or (b) April 15 of the following year (the MI-1040 filing deadline). The annual rate is set twice a year by Treasury under MCL 205.23(2) at 1 percentage point above the adjusted prime rate charged by three large Michigan commercial banks.  _(MCL 205.23(2))_

### Interest component (MCL 205.23(2))

**Interest rate table**

| Period | Annual rate | Daily rate | Authority |
| --- | --- | --- | --- |
| Jan 1 – Jun 30, 2026 | 8.48% | 0.0002324 | RAB 2026-1 |
| Jul 1 – Dec 31, 2026 | 7.85% | 0.0002150 | RAB 2026-5 |

### Interest component (MCL 205.23(2))

`[VERIFY:]` Rates for 2027 will be issued in RAB 2026-13 (December 2026) and RAB 2027-5 (June 2027). Check michigan.gov/taxes/interest-rate before finalizing any MI-2210.

### MI-2210 form structure

**MI-2210 form structure table**

| Part | Function |
| --- | --- |
| Part 1 | Required Annual Payment (lower of 90% current / 100% (or 110%) prior) |
| Part 2 | Short Method (regular installments — equal quarterly amounts) |
| Part 3 | Annualized Income Worksheet (for uneven income; see §6) |
| Part 4 | Penalty and Interest Computation (per quarter) |

### Penalty waiver / reasonable cause

- **Reasonable cause waiver grounds** — Under MCL 205.24(4) the Treasury may waive the underpayment penalty (but not interest) for: Casualty, disaster, or other unusual circumstance where imposition would be inequitable; Reasonable cause shown — e.g., reliance on incorrect written advice from Treasury, retirement after age 62, or first-year self-employment; Death of the taxpayer during the year. Submit a written reasonable-cause statement with MI-2210. Interest is not waivable.  _(MCL 205.24(4))_

### MTO (Michigan Treasury Online) — preferred

1. Navigate to https://mto.treasury.michigan.gov/.
2. Sign in (or create an Individual account using SSN + prior-year AGI).
3. Select "Make a Payment" → "Estimated Tax (MI-1040ES)".
4. Choose tax year 2026 and the installment quarter (1–4).
5. Enter bank routing + account number for ACH eCheck (no fee), OR enter debit/credit card details.
6. Confirm — keep the MTO confirmation number for the file.

### Mail with voucher

Detach the appropriate quarterly voucher from MI-1040ES, attach check payable to "State of Michigan", write SSN and "2026 MI-1040ES Q[n]" on memo line, mail to P.O. Box 30774, Lansing, MI 48909. Use certified mail for evidence of timely filing.

### Bank ACH debit (recurring)

Through MTO a taxpayer can schedule all four quarterly debits in advance on the four statutory due dates. This is the recommended method for sole-prop clients who want to "set and forget".

### Card fees

- **Debit card fee** — $3.95 flat fee per transaction USD (debit card payment)  _(MTO payment processor disclosures)_
- **Credit card fee** — 2.3% percent (of payment, paid to processor not Treasury)  _(MTO payment processor disclosures)_

## Section 10: Coordination with federal Form 1040-ES

**Michigan due dates match federal due dates**

| Quarter | Federal 1040-ES | Michigan MI-1040ES |
| --- | --- | --- |
| Q1 | April 15, 2026 | April 15, 2026 |
| Q2 | June 15, 2026 | June 15, 2026 |
| Q3 | September 15, 2026 | September 15, 2026 |
| Q4 | January 15, 2027 | January 15, 2027 |

### Practical workflow

1. Compute federal Schedule C net profit + SE tax under the `us-schedule-c-and-se-computation` skill.
2. Run federal estimated tax via `us-quarterly-estimated-tax` skill (1040-ES).
3. Apply the federal AGI figure as the input to the Michigan threshold test (§3) and the MI 4.25% computation (Michigan AGI starts from federal AGI — see `mi-income-tax` skill).
4. Compute MI required annual payment and divide by 4.
5. Schedule both federal and Michigan payments on MTO + EFTPS in the same session each quarter.

### Differences to watch

**Differences to watch table**

| Federal | Michigan |
| --- | --- |
| 25/25/25/25 installments | 25/25/25/25 installments (identical) |
| §6654 safe harbor 100%/110% | MCL 206.301 safe harbor 100%/110% (parallel) |
| §6654 interest rate (federal short-term + 3) | MCL 205.23 (prime + 1, set semi-annually) |
| Form 2210 | Form MI-2210 |
| EFTPS / IRS Direct Pay | Michigan Treasury Online (MTO) |
| Form 1040-ES voucher | Form MI-1040ES voucher |

### Tier 1 — deterministic (do not require judgment)

**Tier 1 rules table**

| ID | Rule |
| --- | --- |
| T1-01 | Threshold = $500 expected liability after withholding and credits (MCL 206.301(1)) |
| T1-02 | Four installments due April 15, June 15, September 15, January 15 |
| T1-03 | Each installment = ¼ of required annual payment (RAP) less expected withholding ÷ 4 |
| T1-04 | RAP = lower of (a) 90% current year or (b) 100% (110% if AGI > $150k) prior year |
| T1-05 | Farmer/fisherman alternative = 66⅔% by Jan 15 OR full payment by Mar 1 (MCL 206.301(4)) |
| T1-06 | Late/under penalty = 10% of shortfall, $10 min per quarter |
| T1-07 | Failure to file estimate = 25% penalty, $25 min per quarter |
| T1-08 | Interest rate = Treasury-set semi-annual rate under MCL 205.23 |
| T1-09 | Joint filers may file one voucher set (MCL 206.311) |
| T1-10 | Make check payable to "State of Michigan" with SSN + "2026 MI-1040ES Q[n]" on memo |

### Tier 2 — judgment-required (flag for reviewer)

**Tier 2 rules table**

| ID | Situation | Judgment call |
| --- | --- | --- |
| T2-01 | High-income 110% trigger | Use TY 2025 federal AGI; if > $150k, default to 110% |
| T2-02 | Uneven income — use annualized method? | Use if Q1/Q2 income < 25% of annual; document |
| T2-03 | First-year self-employed (no prior-year liability) | Only current-year 90% safe harbor available; consider reasonable-cause waiver |
| T2-04 | Mid-year change in withholding | Recompute Q3/Q4; do not amend Q1/Q2 |
| T2-05 | Capital gains windfall Q4 | Annualized method usually beats regular installment |
| T2-06 | Spouse files MFS after joint estimates paid | Allocate per MCL 206.311(2) proportional rule |
| T2-07 | Detroit / Grand Rapids resident with city tax | City has separate estimated tax — do not combine |
| T2-08 | Reasonable-cause waiver request | Draft written statement; cite specific MCL 205.24(4) ground |

## Section 12: Worked examples

### Example 1 — Steady-income sole proprietor ($120k expected)

**Facts.** Single filer; full-year Michigan resident; sole proprietor with expected TY 2026 Schedule C net profit of $120,000; no W-2 withholding; TY 2025 MI-1040 total tax was $4,750 (federal AGI $115k); no city income tax.

**Step 1 — Determine if estimates required.**
- Expected MI AGI ≈ $120,000 − ½ SE tax adjustment ($8,478) = $111,522.
- Less personal exemption $5,800 → MI taxable $105,722.
- MI tax @ 4.25% = $4,493.
- No withholding, no credits → expected liability $4,493 > $500. **Estimates required.**

**Step 2 — Required annual payment (RAP).**
- Current-year 90%: $4,493 × 90% = $4,044.
- Prior-year 100%: $4,750. (Federal AGI was $115k, under $150k, so 100% applies.)
- RAP = lower = **$4,044**.

**Step 3 — Quarterly installment.**
- $4,044 ÷ 4 = **$1,011 per quarter**.

**Step 4 — Voucher schedule.**

**Voucher schedule table**

| Quarter | Due date | Amount |
| --- | --- | --- |
| Q1 | April 15, 2026 | $1,011 |
| Q2 | June 15, 2026 | $1,011 |
| Q3 | September 15, 2026 | $1,011 |
| Q4 | January 15, 2027 | $1,011 |
| **Total** |  | **$4,044** |

### Example 1 — Steady-income sole proprietor ($120k expected)

Schedule four ACH debits via MTO at sign-up; no further action required.

### Example 2 — Sole prop with Q3 income spike (annualized method)

**Facts.** Single filer; consultant; total 2026 net profit $140,000 but landed in this distribution: $8,000 by Mar 31; $15,000 by May 31; $90,000 by Aug 31; $140,000 by Dec 31. TY 2025 prior tax was $3,200.

**Regular installment method would require** $140,000 × ~4% MI = ~$5,950 annual tax × 90% ÷ 4 = **$1,339/quarter** — but the taxpayer earned only $8,000 by Mar 31, so $1,339 due April 15 is roughly 67% of all income earned to that date. Painful.

**Annualized method (MI-2210 Part 3):**

**Annualized method table**

| Period | YTD MI AGI | × Factor | Annualized | × 4.25% | Cum. 22.5/45/67.5/90% | Less prior pmts | This pmt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 (3/31) | $8,000 | 4.00 | $32,000 | $1,360 | $306 | 0 | $306 |
| 2 (5/31) | $15,000 | 2.40 | $36,000 | $1,530 | $689 | $306 | $383 |
| 3 (8/31) | $90,000 | 1.50 | $135,000 | $5,738 | $3,873 | $689 | $3,184 |
| 4 (12/31) | $140,000 | 1.00 | $140,000 | $5,950 | $5,355 | $3,873 | $1,482 |
| **Total** |  |  |  |  |  |  | **$5,355** |

### Example 2 — Sole prop with Q3 income spike (annualized method)

The annualized method front-loads cash to Q3 when the income actually arrived. No MI-2210 penalty accrues because each cumulative payment meets the cumulative safe-harbor percentage.

`[VERIFY:]` Annualization factors mirror federal Schedule AI; confirm the MI-2210 (2026 revision) replicates the federal 4 / 2.4 / 1.5 / 1 sequence.

### Example 3 — High-income W-2 earner with withholding shortfall

**Facts.** MFJ; both spouses W-2; combined wages $300,000; combined federal AGI 2025 was $285,000 (i.e., > $150k threshold); MI withholding for 2026 projected at $9,500 against expected MI tax of $12,400; TY 2025 MI total tax was $11,800. No self-employment income.

**Step 1 — Estimates required?**
- Expected MI tax $12,400 − withholding $9,500 = $2,900 shortfall.
- $2,900 > $500 → **Estimates required.**

**Step 2 — RAP under high-income rule.**
- Current-year 90%: $12,400 × 90% = $11,160.
- Prior-year 110% (because 2025 AGI > $150,000): $11,800 × 110% = $12,980.
- RAP = lower = **$11,160**.

**Step 3 — Subtract withholding spread evenly.**
- Required payments net of withholding: $11,160 − $9,500 = $1,660.
- Quarterly installment: $1,660 ÷ 4 = **$415 per quarter**.

**Step 4 — Voucher schedule.**

**Voucher schedule table**

| Quarter | Due date | Amount |
| --- | --- | --- |
| Q1 | April 15, 2026 | $415 |
| Q2 | June 15, 2026 | $415 |
| Q3 | September 15, 2026 | $415 |
| Q4 | January 15, 2027 | $415 |
| **Total estimates** |  | **$1,660** |
| **+ Withholding** |  | **$9,500** |
| **= RAP** |  | **$11,160** |

### Example 3 — High-income W-2 earner with withholding shortfall

For W-2 couples, increasing Michigan withholding via MI-W4 line 6 ("additional amount per pay") is usually administratively easier than quarterly vouchers — and withholding is treated as paid evenly across all four quarters even if added in November, which can fully cure an underpayment for Q1–Q3.

## Section 13: Refusal catalogue

**Refusal catalogue table**

| ID | Situation | Action |
| --- | --- | --- |
| MI-EST-R-01 | Estate or trust estimated payments (MI-1041ES) | Refuse — separate fiduciary skill required |
| MI-EST-R-02 | S-corp / partnership PTET estimated payments (MCL 206.813) | Refuse — load `mi-ptet-estimated-tax` (separate skill, pending) |
| MI-EST-R-03 | Corporate Income Tax estimates (Form 4913) | Refuse — load `mi-corporate-income-tax` |
| MI-EST-R-04 | Multistate apportionment with Michigan as one of several states | Refuse — flag for professional review |
| MI-EST-R-05 | Part-year or non-resident estimates (Schedule NR) | Refuse — out of scope |
| MI-EST-R-06 | Detroit / Grand Rapids / other city estimates (D-1040ES, etc.) | Refuse — separate city return |
| MI-EST-R-07 | Tax year other than current (TY 2024 or earlier) | Refuse — rates and rules may differ |
| MI-EST-R-08 | Michigan Business Tax (MBT) carryover entities | Refuse — different tax regime |
| MI-EST-R-09 | Composite return estimated payments for non-resident members | Refuse — separate skill required |

## Section 14: Form mapping

**Form mapping table**

| Michigan form | Purpose | Federal counterpart |
| --- | --- | --- |
| MI-1040ES (voucher 1–4) | Quarterly estimated payment | Form 1040-ES (voucher 1–4) |
| MI-1040ES instructions + worksheet | Computation worksheet | Form 1040-ES worksheet |
| MI-2210 Part 1 | Required Annual Payment | Form 2210 Part I |
| MI-2210 Part 2 | Short method (equal installments) | Form 2210 Part III, Short Method |
| MI-2210 Part 3 | Annualized Income Worksheet | Form 2210 Schedule AI |
| MI-2210 Part 4 | Penalty and Interest computation | Form 2210 Part III, Regular Method |
| MI-W4 | Employee withholding certificate | Form W-4 |
| MI-1040 line 28 | Estimated payments applied | Form 1040 line 26 |
| MI-1040 line 36 | Refund overpayment applied to next year | Form 1040 line 36 |

### MI-1040ES voucher line numbers (2026)

**Voucher line numbers table**

| Line | Field |
| --- | --- |
| 1 | Filer SSN |
| 2 | Spouse SSN (if joint) |
| 3 | Filer name and address |
| 4 | Voucher number (1, 2, 3, or 4) |
| 5 | Amount of estimated payment |
| 6 | Check payable to "State of Michigan"; write SSN + "2026 MI-1040ES Q[n]" |

## Section 15: Provenance

**Provenance table**

| Element | Source | Confidence |
| --- | --- | --- |
| $500 threshold | MCL 206.301(1) | High |
| Due dates Apr 15 / Jun 15 / Sep 15 / Jan 15 | MCL 206.301(1) | High |
| 90% / 100% / 110% safe harbor | MI-1040ES 2026 instructions | High (`[VERIFY:]` 110% AGI threshold) |
| Farmer/fisherman 66⅔% | MCL 206.301(4) | High |
| 4.25% flat rate | MCL 206.51 | High |
| Personal exemption $5,800 | MCL 206.30; 2026 RAB | High |
| 10% / 25% penalty | MCL 205.24 | High |
| Interest rate 8.48% (H1 2026) | RAB 2026-1 | High |
| Interest rate 7.85% (H2 2026) | RAB 2026-5 | High |
| Annualization factors 4 / 2.4 / 1.5 / 1 | MI-2210 Part 3 (2025 form) | Medium — `[VERIFY:]` 2026 form |
| Joint filer single voucher allowance | MCL 206.311 | High |
| Reasonable cause waiver grounds | MCL 205.24(4) | High |
| MTO payment portal mechanics | mto.treasury.michigan.gov walkthrough | Medium |
| Card / debit fees ($3.95 / 2.3%) | MTO payment processor disclosures | Medium — rates may change |

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
