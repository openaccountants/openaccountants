---
name: us-schedule-c-and-se-computation
description: >
  Tier 2 content skill for computing Schedule C bottom line, Form 8829 home office (actual method), and Schedule SE self-employment tax for US sole proprietors and single-member LLCs disregarded for federal tax. Covers tax year 2025 with the 2025 Social Security wage base of $176,100, the 92.35% net SE earnings adjustment under IRC 1402(a)(12), the 12.4% OASDI rate, the 2.9% Medicare rate, and the 0.9% Additional Medicare Tax thresholds. Handles Schedule C Lines 1-32, the 280A home office gross income limitation and carryover, Form 8829 indirect expense allocation, the 1402 net SE earnings computation, the optional methods under 1402(a)(15) and 1402(l), the deductible half of SE tax under 164(f), and the at-risk indicators on Line 32. Consumes classified transactions from us-sole-prop-bookkeeping. Defers QBI, retirement, SE health insurance, and quarterly estimated tax to companion skills. MUST be loaded alongside us-tax-workflow-base v0.1+. Federal only. ALWAYS read this skill before computing Schedule C, SE tax, or home office deductions.
version: 2.0
---

# US Schedule C and SE Computation Skill v2.0

## Section 1 — Quick Reference

### Pipeline Position

```
Bank statement / source data
        |
us-sole-prop-bookkeeping (classifies every transaction into a Schedule C line)
        |
us-schedule-c-and-se-computation (THIS SKILL — aggregates, runs Form 8829, computes net profit, computes SE tax)
        |
us-form-1040-self-employed-positions (QBI, SE health insurance, retirement, OBBBA personal deductions)
        |
us-quarterly-estimated-tax (safe harbor for following year)
```

Tax year: 2025. Currency date: April 2026.

### Self-Employment Tax Core Figures (TY2025)

| Figure | Value | Source |
|---|---|---|
| Net SE earnings adjustment factor | 92.35% | IRC 1402(a)(12) |
| OASDI (Social Security) rate | 12.4% | IRC 1401(a) |
| Medicare rate | 2.9% | IRC 1401(b)(1) |
| Combined SE tax rate | 15.3% | IRC 1401(a) + 1401(b)(1) |
| Social Security wage base | $176,100 | SSA October 2024 announcement |
| Additional Medicare Tax rate | 0.9% | IRC 1401(b)(2) |
| Additional Medicare Tax threshold (single, HoH, QSS) | $200,000 | IRC 3101(b)(2)(C); NOT indexed |
| Additional Medicare Tax threshold (MFJ) | $250,000 | IRC 3101(b)(2)(A); NOT indexed |
| Additional Medicare Tax threshold (MFS) | $125,000 | IRC 3101(b)(2)(B); NOT indexed |
| Minimum net SE earnings to trigger SE tax | $400 | IRC 1402(b)(2); NOT indexed |
| Deductible portion of SE tax | 50% | IRC 164(f) |

### Schedule SE Optional Methods (TY2025)

| Figure | Value |
|---|---|
| Nonfarm optional method max SE earnings | $7,320 |
| Nonfarm gross income threshold | $10,380 minimum gross |
| Nonfarm profit threshold | < $7,320 net AND < 72.189% of gross |
| 5-year lifetime limit | Yes |

### Home Office Methods

| Method | Deduction | Carryover | Depreciation | 1250 Recapture |
|---|---|---|---|---|
| Simplified | $5/sq ft x min(sq ft, 300) = max $1,500 | NO | NO | NO |
| Actual (Form 8829) | Actual expenses x business % | YES (indefinite) | YES (39-year SL) | YES |

Both subject to 280A(c)(5) gross income limitation (deduction cannot exceed Schedule C Line 29 tentative profit).

### Schedule C Computation Structure

| Line | Description |
|---|---|
| 1 | Gross receipts or sales |
| 2 | Returns and allowances |
| 3 | Line 1 minus Line 2 |
| 4 | Cost of goods sold (Part III) |
| 5 | Gross profit (Line 3 minus Line 4) |
| 6 | Other income |
| 7 | Gross income (Line 5 plus Line 6) |
| 8-27b | Expense lines (from bookkeeping skill) |
| 28 | Total expenses (sum of 8-27b) |
| 29 | Tentative profit (Line 7 minus Line 28) |
| 30 | Home office deduction (Form 8829 or simplified) |
| 31 | Net profit or loss (Line 29 minus Line 30) |
| 32 | At-risk indicator (32a all at risk / 32b Form 6198) |

### Schedule SE Part I Structure

| Line | Description |
|---|---|
| 2 | Net profit from Schedule C Line 31 |
| 4a | Line 3 x 92.35% |
| 6 | Net SE earnings subject to tax |
| 7 | $176,100 (2025 SS wage base) |
| 8d | W-2 SS wages (if any) |
| 9 | Line 7 minus Line 8d (remaining SS base) |
| 10 | Smaller of Line 6 or Line 9 x 12.4% (SS portion) |
| 11 | Line 6 x 2.9% (Medicare portion) |
| 12 | SE tax (Line 10 + Line 11) |
| 13 | Deductible half (Line 12 x 50%) flows to Schedule 1 line 15 |

### Conservative Defaults

| Ambiguity | Conservative Default |
|---|---|
| 92.35% adjustment forgotten | Apply it; defensive check |
| 2025 SS wage base unknown | Use $176,100 (verified) |
| W-2 wage coordination unknown | Assume no W-2 (full SS base available); flag |
| Filing status unknown | Single (highest Additional Medicare Tax threshold risk) |
| Form 8829 prior-year carryover unknown | Assume zero; flag |
| Home depreciation basis undocumented | $0 depreciation; flag 1250 recapture risk |
| Actual vs simplified home office method unclear | Ask; do not assume |
| At-risk status | Yes (Line 32a) unless evidence to contrary |
| Net loss large enough for NOL | Refuse (R-COMP-NOL) |
| Gross receipts < 1099 totals | Flag — IRS computer match risk |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Schedule C Line 31 >= $200,000 | Approaches Additional Medicare Tax threshold (single) |
| Schedule C Line 31 <= -$5,000 | Loss territory; check at-risk and hobby loss |
| Form 8829 deduction >= $5,000 | Material; substantiation review |
| Home depreciation taken (actual method) | 1250 recapture risk on future home sale |
| Home office limited by 280A(c)(5) | Carryover treatment verification |
| Net SE earnings near $176,100 wage base | Verify W-2 coordination |
| Combined SE + W-2 >= Additional Medicare Tax threshold | Form 8959 required |
| Gross receipts < 1099 totals | IRS computer match risk |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

**Upstream prerequisite:** This skill requires the `us-sole-prop-bookkeeping` working paper with classified Schedule C line totals. If no working paper exists, run bookkeeping first or accept user-provided totals (flagged as unvalidated).

1. **Schedule C line totals** — from bookkeeping working paper (Lines 1 through 27b)
2. **Home office method** — simplified or actual (Form 8829)
3. **Home office square footage** — office area and total home area
4. **Home expenses (if actual method)** — mortgage interest, taxes, insurance, utilities, repairs
5. **Home depreciation data (if actual)** — adjusted basis, FMV at conversion, land value, date placed in service
6. **Prior-year Form 8829 carryovers** — lines 43 and 44
7. **W-2 wages (if any)** — Box 3 SS wages for SE tax coordination
8. **Filing status** — for Additional Medicare Tax threshold
9. **1099-K, 1099-NEC, 1099-MISC received** — for gross receipts cross-check
10. **At-risk status** — all at risk or Form 6198 needed

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-COMP-NOL | Net operating loss generated | Stop — 172 analysis required; outside scope |
| R-COMP-ATRISK | At-risk limitation may apply (Form 6198) | Stop — 465 analysis required |
| R-COMP-FORM8959-COMPLEX | Additional Medicare Tax with complex W-2 coordination | Flag — compute basic liability; reviewer verifies withholding |
| R-COMP-FARM | Farm income present | Stop — Schedule F, not Schedule C |
| R-COMP-CHURCH | Church employee income | Stop — 1402(j) special rules; specialist needed |
| R-COMP-PRIORYEAR | No prior-year return for carryover verification | Soft stop — proceed with zero carryover assumption; flag |

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns (US Banks)

| # | Narration Pattern | Schedule C Line | Notes |
|---|---|---|---|
| I-01 | `ACH CREDIT [client name]` / `DIRECT DEP [client]` | Line 1 — Gross receipts | Standard ACH deposit from client |
| I-02 | `WIRE TRANSFER FROM [client]` / `INCOMING WIRE` | Line 1 — Gross receipts | Wire transfer from client |
| I-03 | `ZELLE FROM [client]` / `ZELLE PAYMENT` | Line 1 — Gross receipts | Zelle instant payment |
| I-04 | `STRIPE TRANSFER` / `STRIPE PAYOUT` | Line 1 — Gross receipts (gross up) | Stripe payout; gross up for processing fees (Line 27b) |
| I-05 | `SQUARE INC` / `SQ *[business]` / `SQUARE PAYOUT` | Line 1 — Gross receipts (gross up) | Square payout; gross up for fees |
| I-06 | `PAYPAL TRANSFER` / `PAYPAL INST XFER` | Line 1 — Gross receipts (gross up) | PayPal payout; gross up |
| I-07 | `VENMO CASHOUT` / `VENMO PAYMENT` | Line 1 — Gross receipts | Venmo business payment |
| I-08 | `GUSTO PAYMENT` / `BILL.COM PAYMENT` | Line 1 — Gross receipts | Payment platform deposit |
| I-09 | `CHECK DEPOSIT` / `MOBILE CHECK DEP` | Line 1 — Gross receipts | Client check deposited |
| I-10 | `IRS TREAS 310 TAX REF` / `IRS REFUND` | NOT income — tax refund | IRS refund; exclude from Line 1 |
| I-11 | `INTEREST PAYMENT` / `INTEREST EARNED` | Line 6 — Other income (if business acct) | Business account interest |
| I-12 | `TRANSFER FROM [own account]` / `ONLINE TRANSFER` | EXCLUDE — owner contribution | Not income; capital contribution |

### 3.2 Expense Patterns (US Banks)

| # | Narration Pattern | Schedule C Line | Notes |
|---|---|---|---|
| E-01 | `GOOGLE ADS` / `FACEBOOK ADS` / `META ADS` | Line 8 — Advertising | Marketing spend |
| E-02 | `GEICO` / `STATE FARM` / `PROGRESSIVE` (vehicle) | Line 9 — Car/truck expenses | If standard mileage: not deductible separately |
| E-03 | `[Subcontractor name] ACH` / `1099 CONTRACTOR` | Line 11 — Contract labor | 1099-NEC issuance may be required |
| E-04 | `APPLE` / `DELL` / `BEST BUY` (equipment) | Line 13 — Depreciation/179 | Capital asset; classify via 179 or bonus |
| E-05 | `HISCOX` / `NEXT INSURANCE` / `THE HARTFORD` | Line 15 — Insurance | Business liability/E&O insurance |
| E-06 | `LEGALZOOM` / `[CPA name]` / `[attorney name]` | Line 17 — Legal and professional | Tax prep, legal services |
| E-07 | `STAPLES` / `OFFICE DEPOT` / `AMAZON OFFICE` | Line 18 — Office expense | Office supplies and equipment |
| E-08 | `WEWORK` / `REGUS` / `INDUSTRIOUS` | Line 20b — Other business property | Coworking space |
| E-09 | `AMAZON` / `AMAZON.COM` (supplies) | Line 22 — Supplies | Non-office supplies for business |
| E-10 | `UNITED AIRLINES` / `DELTA` / `AMERICAN AIRLINES` / `SOUTHWEST` | Line 24a — Travel | Business flights; document purpose |
| E-11 | `MARRIOTT` / `HILTON` / `HYATT` / `AIRBNB` | Line 24a — Travel | Business accommodation |
| E-12 | `UBER` / `LYFT` / `TAXI` | Line 24a — Travel (ground) | Business ground transport |
| E-13 | `RESTAURANT` / `DOORDASH` / `GRUBHUB` (business meal) | Line 24b — Meals (50%) | Business meals; 50% deductible |
| E-14 | `ADOBE` / `MICROSOFT` / `GITHUB` / `AWS` | Line 27b — Other expenses | Software subscriptions |
| E-15 | `STRIPE FEE` / `PAYPAL FEE` / `SQUARE FEE` | Line 27b — Other expenses | Payment processing fees |
| E-16 | `CHASE MONTHLY FEE` / `WELLS FARGO FEE` / `BOA FEE` | Line 27b — Other expenses | Bank account fees (business) |
| E-17 | `EFTPS TAX PMT` / `IRS USATAXPYMT` | NOT deductible — tax payment | Estimated tax payment; credit not expense |
| E-18 | `TRANSFER TO [personal]` / `OWNER DRAW` | NOT deductible — personal | Owner withdrawal |
| E-19 | `EXXON` / `SHELL` / `CHEVRON` / `BP` (fuel) | Line 9 or Line 27b | If using actual vehicle method; not if standard mileage |
| E-20 | `AT&T` / `VERIZON` / `T-MOBILE` / `XFINITY` / `SPECTRUM` | Line 25 — Utilities (or 8829) | If home office: flows through Form 8829; otherwise Line 25 |

### 3.3 US Bank Fees (Deductible as Line 27b)

| Pattern | Treatment | Notes |
|---|---|---|
| CHASE, JPMORGAN CHASE | Deductible (Line 27b) for business account fees | Largest US bank |
| WELLS FARGO | Deductible (Line 27b) for business account fees | |
| BANK OF AMERICA, BOFA | Deductible (Line 27b) for business account fees | |
| CITIBANK | Deductible (Line 27b) for business account fees | |
| US BANK | Deductible (Line 27b) for business account fees | |
| PNC | Deductible (Line 27b) for business account fees | |
| CAPITAL ONE | Deductible (Line 27b) for business account fees | |
| SVB, SILICON VALLEY | Deductible (Line 27b) for business account fees | Tech banking |
| MERCURY | Deductible (Line 27b) for business account fees | Startup banking |
| RELAY, NOVO, BLUEVINE | Deductible (Line 27b) for business account fees | SMB digital banks |
| MONTHLY SERVICE FEE, MAINT FEE | Deductible (Line 27b) | Account maintenance |
| WIRE FEE, ACH FEE | Deductible (Line 27b) | Transaction fees |

### 3.4 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFER FROM SAVINGS, TRANSFER FROM CHECKING | EXCLUDE | Internal movement |
| OWNER CONTRIBUTION, PERSONAL DEPOSIT | EXCLUDE | Capital contribution, not income |
| LOAN PROCEEDS, SBA LOAN | EXCLUDE | Debt, not income |
| LOAN PAYMENT, PRINCIPAL PAYMENT | EXCLUDE (interest portion may be deductible) | Separate interest vs principal |
| IRS TREAS 310, STATE TAX REFUND | EXCLUDE | Tax refunds |
| CREDIT CARD PAYMENT | EXCLUDE | Paying off CC; expenses on the CC are already classified |

---

## Section 4 — Worked Examples

### Example 1 — Chase (Austin TX, UX Designer — Actual Home Office)

**Bank:** Chase Business Checking
**Client:** Maria Hernandez, freelance UX designer, single, Austin TX, sole prop

```
Date;Description;Debit;Credit;Balance
01/15/2025;ACH CREDIT TECH STARTUP INC;;12,500.00;
01/20/2025;CHASE MONTHLY FEE;15.00;;
02/05/2025;STRIPE TRANSFER;;8,750.00;
02/15/2025;ADOBE CREATIVE CLOUD;54.99;;
03/01/2025;ZELLE FROM DESIGN CLIENT;;3,200.00;
03/15/2025;EFTPS TAX PMT;3,500.00;;
04/01/2025;WEWORK AUSTIN;299.00;;
05/10/2025;UNITED AIRLINES;487.00;;
06/01/2025;MARRIOTT HOTEL;342.00;;
07/15/2025;HISCOX INSURANCE;60.00;;
```

**Schedule C (from bookkeeping totals, annualised):**
- Line 1 (Gross receipts): $87,500
- Line 8 (Advertising): $480
- Line 9 (Car — 4,200 miles x $0.70): $2,940
- Line 11 (Contract labor): $5,200
- Line 13 (Depreciation/179 — MacBook): $3,499
- Line 15 (Insurance): $720
- Line 17 (Legal/professional): $1,150
- Line 18 (Office expense): $2,134
- Line 20b (Coworking): $3,588
- Line 22 (Supplies): $246
- Line 24a (Travel): $4,287
- Line 24b (Meals at 50%): $920
- Line 27b (Other — software, fees, bank): $4,892
- **Line 28 (Total expenses): $30,056**
- **Line 29 (Tentative profit): $57,444**

**Form 8829 (actual method):**
150 sq ft office / 1,200 sq ft home = 12.5%
Indirect expenses: mortgage $14,200 + taxes $7,800 + insurance $1,440 + utilities $3,600 = $27,040
Business portion: $27,040 x 12.5% = $3,380
Depreciation: ($385,000 - $80,000 land) x 12.5% x 2.564% = $977
Total home office: $3,380 + $977 = **$4,357**

280A(c)(5) check: $4,357 < $57,444 — no limitation.

- **Line 30: $4,357**
- **Line 31 (Net profit): $53,087**
- Line 32: 32a (all at risk)

**Schedule SE:**
- Line 4a: $53,087 x 92.35% = $49,026
- Line 10: $49,026 x 12.4% = $6,079 (SS)
- Line 11: $49,026 x 2.9% = $1,422 (Medicare)
- Line 12: **$7,501** (SE tax)
- Line 13: **$3,750** (deductible half)
- Additional Medicare Tax: $49,026 < $200,000 — not applicable

### Example 2 — Wells Fargo (Denver CO, Consultant — Simplified Home Office)

**Bank:** Wells Fargo Business
**Client:** James Park, management consultant, Denver, single

Gross receipts: $142,000. Total expenses (Lines 8-27b): $38,500.
Tentative profit (Line 29): $103,500.

Simplified home office: 200 sq ft x $5 = $1,000. Under $1,500 max.
280A(c)(5) check: $1,000 < $103,500 — no limitation.

- Line 30: $1,000
- Line 31: $102,500

SE tax: $102,500 x 92.35% = $94,659 x 15.3% = $14,483
Deductible half: $7,241
Additional Medicare Tax: $94,659 < $200,000 — not applicable.

### Example 3 — Bank of America (San Francisco, Developer — W-2 + SE)

**Bank:** BOA Business Checking
**Client:** Priya Patel, software developer, SF, also W-2 from part-time job

Schedule C net profit: $85,000. W-2 SS wages (Box 3): $120,000.

SE computation:
- Line 4a: $85,000 x 92.35% = $78,498
- Line 8d: $120,000 (W-2 SS wages)
- Line 9: $176,100 - $120,000 = $56,100 (remaining SS base)
- Line 10: smaller of $78,498 or $56,100 = $56,100 x 12.4% = $6,956 (SS)
- Line 11: $78,498 x 2.9% = $2,276 (Medicare — no cap)
- Line 12: $9,232

Additional Medicare Tax check: $120,000 + $78,498 = $198,498. Under $200,000 (single). Not applicable.

Flag: Close to Additional Medicare Tax threshold — monitor if income increases.

### Example 4 — Mercury (Remote, Net Loss Scenario)

**Bank:** Mercury Business
**Client:** Alex Chen, first-year startup founder

Schedule C net profit: ($12,000) — net loss.
SE tax: $0 (no SE tax on a loss).
Loss flows to Schedule 1 line 3 as ($12,000). Reduces AGI.

Flag: Check hobby loss (3+ year loss streak). Check at-risk (Line 32a confirmed). If loss creates NOL: R-COMP-NOL fires.

### Example 5 — Chase (NYC, High Earner — Additional Medicare Tax)

**Bank:** Chase Business
**Client:** Sarah Kim, consulting, NYC, single

Schedule C net profit: $280,000.
SE: $280,000 x 92.35% = $258,580.
SS portion: min($258,580, $176,100) x 12.4% = $21,836
Medicare: $258,580 x 2.9% = $7,499
SE tax: $29,335. Deductible half: $14,668.

Additional Medicare Tax: $258,580 > $200,000.
Excess: $58,580 x 0.9% = $527 (Form 8959).

### Example 6 — Relay (Austin, 280A Gross Income Limitation)

**Bank:** Relay Business Banking
**Client:** Tom Rivera, photographer, Austin

Gross income (Line 7): $18,000. Expenses (Line 28): $16,500.
Tentative profit (Line 29): $1,500.
Form 8829 actual method tentative deduction: $4,200.

280A(c)(5) limitation: $4,200 > $1,500. Cap deduction at $1,500.
Carryover: $4,200 - $1,500 = $2,700 carried to next year (Form 8829 lines 43-44).

Line 30: $1,500. Line 31: $0. SE tax: $0 ($0 < $400 minimum).

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-US-SE-1 — Always apply the 92.35% adjustment**
Net SE earnings = Schedule C net profit x 92.35%. This is the 1402(a)(12) adjustment. Never compute SE tax on the full Schedule C net profit.

**T1-US-SE-2 — SS wage base coordination with W-2**
If the taxpayer has W-2 wages, subtract W-2 Box 3 SS wages from $176,100 to get the remaining SS base for SE. If W-2 wages already exceed $176,100, the SS portion of SE tax is $0 — only Medicare applies.

**T1-US-SE-3 — Additional Medicare Tax is on Form 8959, NOT Schedule SE**
The 0.9% Additional Medicare Tax is computed on Form 8959, not blended into Schedule SE. Schedule SE Line 11 uses 2.9% only. Never include 0.9% in Schedule SE.

**T1-US-SE-4 — Minimum $400 threshold**
If net SE earnings (after 92.35% adjustment) are less than $400, no SE tax is due. Do not compute SE tax on sub-$400 amounts.

**T1-US-SE-5 — Home office deduction cannot exceed Line 29**
The 280A(c)(5) gross income limitation caps the home office deduction at the tentative profit. Excess carries over under actual method; is lost under simplified method.

**T1-US-SE-6 — Deductible half of SE tax is NOT a Schedule C expense**
The deductible half (Schedule SE Line 13) flows to Schedule 1 line 15 as an above-the-line deduction. It does NOT reduce Schedule C net profit and does NOT reduce QBI.

**T1-US-SE-7 — EFTPS / estimated tax payments are credits, not expenses**
Quarterly estimated tax payments made via EFTPS are credits against the annual tax liability. Never include them as Schedule C expenses.

**T1-US-SE-8 — 1250 recapture warning for actual home office depreciation**
Taking home depreciation creates 1250 recapture on future home sale. The 121 home sale exclusion does NOT shelter this. Flag prominently. Note: depreciation is "allowed or allowable" — skipping the deduction does not avoid recapture.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-US-SE-1 | Simplified vs actual home office comparison | Both methods available each year; no lock-in | Present both calculations; reviewer confirms taxpayer preference |
| T2-US-SE-2 | Vehicle actual vs standard mileage | Cannot switch from actual to standard on same vehicle | Flag — verify prior-year method for the vehicle |
| T2-US-SE-3 | Hobby loss exposure (3+ year loss streak) | 183 rebuttable presumption | Flag — do not refuse; reviewer assesses profit motive |
| T2-US-SE-4 | At-risk status uncertain | Form 6198 may be required | Flag — if any nonrecourse debt or sheltered investment |
| T2-US-SE-5 | SE optional method consideration | Low-income earner may want to "buy" SS credits | Skip unless taxpayer asks; present if near retirement |
| T2-US-SE-6 | Home office depreciation: claim or skip | 1250 recapture applies either way; claiming is usually better | Flag — reviewer should confirm taxpayer understands trade-off |

---

## Section 7 — Excel Working Paper Template

```
US SCHEDULE C / SE WORKING PAPER (SOLE PROPRIETOR / SMLLC)
Taxpayer: _______________  SSN/EIN: _______________  TY: 2025

SECTION A — SCHEDULE C INCOME
                                            USD
Line 1 (Gross receipts):                  ___________
Line 2 (Returns and allowances):           ___________
Line 3 (Net receipts):                    ___________
Line 4 (COGS):                             ___________
Line 5 (Gross profit):                    ___________
Line 6 (Other income):                    ___________
Line 7 (Gross income):                    ___________

SECTION B — SCHEDULE C EXPENSES
Line 8 (Advertising):                     ___________
Line 9 (Car and truck):                   ___________
Line 11 (Contract labor):                 ___________
Line 13 (Depreciation/179):               ___________
Line 15 (Insurance):                      ___________
Line 17 (Legal and professional):          ___________
Line 18 (Office expense):                 ___________
Line 20b (Other business property):        ___________
Line 22 (Supplies):                        ___________
Line 24a (Travel):                         ___________
Line 24b (Meals at 50%):                  ___________
Line 25 (Utilities):                       ___________
Line 27b (Other expenses):                ___________
Line 28 (TOTAL EXPENSES):                 ___________

SECTION C — BOTTOM LINE
Line 29 (Tentative profit):               ___________
Line 30 (Home office):                    ___________
  Method: [ ] Simplified  [ ] Actual (Form 8829)
Line 31 (NET PROFIT OR LOSS):             ___________
Line 32: [ ] 32a (all at risk)  [ ] 32b (Form 6198)

SECTION D — FORM 8829 (IF ACTUAL METHOD)
Office sq ft: ___ / Total sq ft: ___ = Business %: ___
Indirect expenses (mortgage, tax, insurance, utilities): ___________
Business portion:                          ___________
Direct expenses:                           ___________
Depreciation:                              ___________
Prior-year carryover:                      ___________
Tentative deduction:                       ___________
280A(c)(5) limitation applied? [ ] No  [ ] Yes (capped at $___)
Carryover to next year:                    ___________
FORM 8829 DEDUCTION:                      ___________

SECTION E — SCHEDULE SE
Net SE earnings (Line 31 x 92.35%):       ___________
W-2 SS wages (if any):                    ___________
Remaining SS base:                         ___________
SS portion (12.4%):                        ___________
Medicare portion (2.9%):                   ___________
SE TAX (Line 12):                          ___________
Deductible half (Line 13):                ___________

SECTION F — ADDITIONAL MEDICARE TAX CHECK
Combined earned income (SE + W-2):         ___________
Filing status threshold:                   ___________
Excess (if any):                           ___________
Additional Medicare Tax (0.9%):            ___________
Form 8959 required? [ ] No  [ ] Yes

SECTION G — DOWNSTREAM OUTPUTS
Schedule 1 line 3 (business income):       ___________
Schedule 1 line 15 (deductible half SE):   ___________
Schedule 2 line 4 (SE tax):               ___________
Net SE earnings (for retirement calc):     ___________

SECTION H — REVIEWER FLAGS
[ ] Upstream bookkeeping working paper verified?
[ ] 92.35% adjustment applied?
[ ] SS wage base coordination correct (W-2)?
[ ] Additional Medicare Tax on Form 8959 (not SE)?
[ ] Home office 280A(c)(5) limitation checked?
[ ] Home depreciation 1250 recapture flagged?
[ ] $400 minimum SE threshold checked?
[ ] 1099 totals cross-checked with Line 1?
[ ] At-risk indicator stated (Line 32)?
[ ] EFTPS payments excluded from expenses?
```

---

## Section 8 — Bank Statement Reading Guide

### Chase (JPMorgan Chase)
- Export: CSV/OFX from Chase Business Online → "Download account activity"
- Columns: `Details,Posting Date,Description,Amount,Type,Balance,Check or Slip #`
- Amount format: positive = credit, negative = debit (or vice versa depending on download type)
- Date: MM/DD/YYYY
- Credits: `ACH CREDIT [sender]`, `WIRE TYPE:WIRE IN [sender]`, `ZELLE FROM [name]`
- Debits: `ACH DEBIT [payee]`, `CHASE CREDIT CRD AUTOPAY`, `CHECKCARD [merchant]`

### Wells Fargo
- Export: CSV from Wells Fargo Business Online → "Download" → CSV
- Columns: `Date,Amount,*,Check Number,Description`
- Negative amount = debit; positive = credit
- Date: MM/DD/YYYY
- Credits: `ACH CREDIT [sender]`, `WIRE TRANSFER [sender]`, `ONLINE TRANSFER FROM [acct]`
- Debits: `PURCHASE AUTHORIZED [merchant]`, `BILL PAY [payee]`

### Bank of America
- Export: CSV from BOA Business Online → "Download Transactions"
- Columns: `Date,Description,Amount,Running Bal.`
- Negative = debit; positive = credit
- Credits: `ACH CREDITS [sender]`, `WIRE [sender]`

### Citibank
- Export: CSV from Citi Business Online
- Standard US format; `Date,Description,Debit,Credit,Status`

### US Bank
- Export: CSV from USB Business Online
- Standard: `Date,Transaction,Name,Memo,Amount`

### Mercury (Startup Banking)
- Export: CSV from Mercury dashboard → "Transactions" → "Export"
- Columns: `Date,Description,Amount,Status,Bank Description,Note`
- Clean format; positive = credit, negative = debit
- Stripe/PayPal payouts clearly labeled

### Relay Financial
- Export: CSV from Relay dashboard
- Columns: `Date,Description,Amount,Balance`
- Positive = credit; negative = debit

### Novo / Bluevine (SMB Digital)
- Export: CSV from dashboard
- Simple format; single amount column with sign

### Square / Cash App for Business
- Settlements appear as `SQ *[business name]` or `SQUARE INC` deposits
- Gross-up required — Square deducts 2.6% + $0.10 before settlement

### Stripe
- Payouts appear as `STRIPE TRANSFER` or `STRIPE` in bank statement
- Cross-reference with Stripe dashboard → Payouts for gross amounts and fees
- 1099-K issued by Stripe if > $600

### PayPal
- Payouts appear as `PAYPAL INST XFER` or `PAYPAL TRANSFER`
- Cross-reference with PayPal activity → Reports for gross amounts
- 1099-K issued if > $600

### Key US Banking Notes
- US banks use MM/DD/YYYY date format
- Amount sign conventions vary by bank and export format — always verify
- ACH (Automated Clearing House) is the standard inter-bank transfer
- Zelle is an instant payment system; appears as `ZELLE FROM/TO [name]`
- EFTPS (Electronic Federal Tax Payment System) payments are estimated tax — never an expense

---

## Section 9 — Onboarding Fallback

**Upstream bookkeeping check:**
> "I need the bookkeeping classification to run first. Schedule C computation requires classified transaction totals from us-sole-prop-bookkeeping. Do you want me to run the bookkeeping skill on your transaction data first, or do you already have classified Schedule C line totals?"

**Home office method:**
> "Do you use a home office for your business? If so, there are two methods: the simplified method ($5 per square foot, maximum $1,500, no depreciation or carryover) and the actual method (Form 8829, allows depreciation but creates recapture risk on future home sale). You can switch between methods each year — there is no lock-in. Which method do you prefer?"

**W-2 coordination:**
> "Do you (or your spouse, if filing jointly) have W-2 wages from any job in 2025? If yes, I need the total from Box 3 (Social Security wages) on each W-2. This affects the Social Security portion of your self-employment tax because the $176,100 wage base cap applies to combined earnings."

**1099 cross-check:**
> "Did you receive any 1099-NEC, 1099-MISC, or 1099-K forms for 2025? The IRS computer-matches these against your Schedule C gross receipts. I need to verify that your Line 1 gross receipts equal or exceed the total of all 1099 forms received."

---

## Section 10 — Reference Material

### Key Legislation
- **IRC 61** — Gross income definition
- **IRC 164(f)** — Deductible half of self-employment tax
- **IRC 168(c)** — Recovery periods (39-year for home office depreciation)
- **IRC 280A** — Business use of home
- **IRC 280A(c)(5)** — Gross income limitation
- **IRC 465** — At-risk limitations
- **IRC 1401** — Self-employment tax rates
- **IRC 1402** — Net earnings from self-employment
- **IRC 1402(a)(12)** — 92.35% adjustment
- **IRC 1402(b)(2)** — $400 minimum threshold
- **IRC 1402(l)** — Nonfarm optional method
- **IRC 3101(b)(2)** — Additional Medicare Tax thresholds

### IRS Publications and Forms
- **Pub 334 (2025)** — Tax Guide for Small Business
- **Pub 587 (2025)** — Business Use of Your Home
- **Pub 946 (2025)** — How to Depreciate Property
- **Schedule C (Form 1040) Instructions (2025)**
- **Schedule SE (Form 1040) Instructions (2025)**
- **Form 8829 Instructions (2025)**
- **Form 8959 Instructions (2025)** — Additional Medicare Tax

### Filing Deadlines

| Deadline | Event |
|---|---|
| April 15, 2026 | Return due (TY2025) |
| October 15, 2026 | Extended due date |
| Quarterly (4/15, 6/15, 9/15, 1/15) | Estimated tax payments (EFTPS) |

### Key Court Decisions
- **Commissioner v. Soliman, 506 U.S. 168 (1993)** — Principal place of business test
- **Welch v. Helvering, 290 U.S. 111 (1933)** — "Ordinary and necessary" standard

### 2025 Year-Specific Figures Summary

| Figure | Value |
|---|---|
| SS wage base | $176,100 |
| SE tax rate | 15.3% (12.4% + 2.9%) |
| 92.35% adjustment | 0.9235 |
| Additional Medicare Tax | 0.9% above $200K/$250K/$125K |
| Simplified home office rate | $5/sq ft, max 300 sq ft = $1,500 |
| Standard mileage rate | $0.70/mile |
| 179 expensing limit | $1,250,000 (OBBBA) |
| Bonus depreciation | 100% (OBBBA restored) |
