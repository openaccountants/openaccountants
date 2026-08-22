---
name: au-fbt-year
description: >
  Use this skill whenever asked about the Australian FBT annual cycle -- the FBT year
  (1 April to 31 March, not the income year), return lodgment dates (21 May self, 25 June
  agent-electronic), quarterly BAS instalments and variation, what goes in the return
  (Type 1/2 grossed-up aggregates, employee contributions, otherwise-deductible), the
  STP/RFBA interplay (reported by 14 July against the following income year), small-employer
  annual RFBA reporting, paper-to-digital transition, and exemption/rebate reconciliation.
  Trigger on "FBT year end", "FBT return", "FBT instalment", "vary FBT", "RFBA timing",
  "FBT due date". Read au-fbt first for benefit-level computation; this skill covers the CYCLE.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "FBT year ending 31 March 2027"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia FBT Annual Cycle -- Employer Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Companion skill.** This guide covers the FBT annual CYCLE -- dates, instalments, return mechanics, STP/RFBA timing, reconciliation. It deliberately does NOT repeat benefit-level computation (car statutory formula, operating cost, EV exemption, meal entertainment methods, minor benefits, LAFHA, loan benchmark). For all of that, read **au-fbt** first and apply it; come back here for when things are due and how the year closes out.

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Australia |
| Primary legislation | Fringe Benefits Tax Assessment Act 1986 (FBTAA) |
| Tax authority | Australian Taxation Office (ATO) |
| FBT year | 1 April to 31 March -- does NOT align with the income year (1 July -- 30 June) |
| Current FBT year | Ending 31 March 2027 (1 April 2026 -- 31 March 2027) |
| Most recent closed FBT year | Ended 31 March 2026 (return was due 21 May / 25 June 2026) |
| Currency | AUD only |
| FBT rate | 47% |
| Type 1 / Type 2 gross-up | 2.0802 / 1.8868 |
| Return due -- self-lodger, or agent lodging on paper | 21 May (lodge AND pay) |
| Return due -- tax agent lodging electronically | 25 June (client on the agent's FBT client list by 21 May) |
| Instalment trigger | Prior-year FBT payable $3,000 or more -> quarterly instalments next year via activity statements |
| Instalment variation | Labels F2/F3/F4 on the BAS; penalty risk if total instalments/estimates < 90% of actual liability |
| RFBA trigger | Individual reportable fringe benefits taxable value > $2,000 in the FBT year |
| RFBA factor | Always x 1.8868 (Type 2), whole dollars |
| RFBA reported | Through STP, for the income year ending straight after the FBT year (FBT year ended 31 Mar 2027 -> income year ended 30 Jun 2027), finalised by 14 July |
| Penalty unit | $364 from 1 July 2026 |
| Contributor | Open Accountants |
| Validated by | Pending |

**The one rule that drives everything:** FBT runs on its own calendar. A July-June income-year export misses April-June of the FBT year. Every sweep, reconciliation, declaration and due date in this guide keys off 1 April -- 31 March.

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown prior-year FBT payable | Ask -- decides whether instalments apply this year |
| Unknown whether client is on an agent's FBT client list | Assume the 21 May date governs until confirmed in writing |
| Unknown GST creditability of a benefit | Ask -- decides Type 1 vs Type 2; never assume Type 1 |
| RFBA needed but FBT return not yet finalised | Report the best current estimate via STP, then correct by update event before finalisation |
| Not-for-profit employer, salary packaging design, novated lease structuring, international assignees | STOP -- refusal catalogue (Section 8) |

---

## Section 2 -- The FBT year and why the mismatch matters

The FBT year is **1 April to 31 March** (s 136(1) FBTAA, definition of "year of tax"). It is NOT the income year. Consequences bookkeepers hit every cycle:

1. **GL exports.** A standard 1 July -- 30 June ledger export captures only 9 of the 12 FBT months. Export **1 April to 31 March exactly** for FBT work. April--June 2026 belongs to the FBT year ending 31 March 2027 even though it sits in the 2026-27 income year.
2. **Two tax years on every desk.** In May/June you are simultaneously closing the FBT year just ended (31 March) and the income year about to end (30 June). They are different populations of transactions.
3. **Declarations and logbooks** are framed by FBT year. A declaration dated for "the year ended 30 June" is the wrong period; employer declarations must be held before the declaration date for the FBT year (see au-fbt Rule 10 for the approved-form/alternative-records position from 1 April 2024).
4. **RFBA crosses the boundary.** FBT is computed to 31 March but reported to the employee through STP against the income year that ends straight after (30 June) -- see Section 6.

---

## Section 3 -- Lodgment dates and the return cycle

### 3.1 Who must lodge

Lodge an FBT return for the FBT year if you either have FBT payable on benefits provided, OR you paid FBT instalments through activity statements during the year (lodge to reconcile -- instalments in excess of the actual liability are refunded after lodgment). Registered for FBT but no return needed? Send a **notice of non-lodgment (NAT 3094)** by the date the return would have been due, or the ATO will chase a return later.

### 3.2 Due dates (ATO "Lodging your FBT return and paying" + agent lodgment program)

| Lodgment path | Due date (lodge AND pay) |
|---|---|
| Self-lodger (paper or SBR software) | **21 May** |
| Tax agent lodging on paper | **21 May** |
| Tax agent lodging electronically (Practitioner lodgment service) | **25 June** -- client must be an FBT client of the agent **by 21 May** |

Mechanics that catch people:

- Weekend/public-holiday due dates roll to the next business day.
- A client added to the agent's FBT client list **after** 21 May does not get the June date -- they revert to 21 May, already late if unlodged.
- First time lodging through an agent? Contact them **before 21 May** so they can add you to their FBT client list in time.
- Extensions: through the agent if agent-lodged; phone 13 28 66 if self-lodging. Payment difficulty -- contact the ATO before the due date.
- Processing: electronic lodgments generally ~14 days; paper ~50 business days; refunds within 28 days.
- State/territory government employer nominations (or variations/revocations): final date **21 May**.

### 3.3 The hard sequencing rule for instalment payers

You must lodge **all** activity statements for the FBT year ending 31 March -- **including the March quarter BAS** -- before lodging the FBT return. The return will not be processed until every activity statement is in. Diarise the March-quarter BAS first, then the FBT return.

---

## Section 4 -- Instalment mechanics: FBT is prepaid through the BAS

### 4.1 The trigger and the default amount

If FBT payable for a year is **$3,000 or more**, the next year you pay quarterly FBT instalments through your activity statements. The ATO pre-populates **label F1** each quarter based on the FBT payable on your most recent FBT assessment. Not varying? Copy F1 to **6A** in the BAS summary.

### 4.2 Variation (labels F2, F3, F4)

Vary when this year's liability will differ from last year's -- employees with cars left, the fleet shrank, a packaging program ended, a rebate is now claimed.

- **F2** -- your estimate of total FBT liability for the FBT year ending 31 March.
- **F3** -- varied amount for the quarter:

```
F3 = (F2 x relevant %) - (previous instalment liabilities - previous credits claimed)

Quarter ending 30 June 25% | 30 September 50% | 31 December 75% | 31 March 100%
```

Positive result -> enter at F3 (and copy to 6A). Negative or zero -> enter '0' at F3; a negative result may support a credit at **6B** (no minus sign).
- **F4** -- reason code: 22 current business structure not continuing; 30 change in fringe benefits for employees; 31 change in employees with fringe benefits; 32 fringe benefits rebate now claimed.

### 4.3 The 90% penalty rule

If you vary and your total instalments for the year -- or the estimates you based them on -- are **less than 90% of your actual FBT liability**, you may incur a penalty. Practical control: only vary down when you have the computation to support the new estimate, keep that workpaper on file, and re-run the estimate before the March quarter (100% cumulative point) so the final quarter trues the year up.

### 4.4 Year-end set-off

At the annual return, instalments paid offset the actual liability: shortfall payable with the return; excess refunded after lodgment. Instalments are reported at Item 20 of the return (see Section 5).

---

## Section 5 -- What goes in the return

Computation of each benefit's taxable value belongs to **au-fbt**. The return assembles those values:

| Return item | Content |
|---|---|
| Item 23 (per benefit category) | Gross taxable value (a), less employee contributions (b), less value of reductions (c) = taxable value of benefits, per category (cars statutory, cars operating cost, loans, expense payments, meal entertainment, etc.). Contributions + reductions exceeding the benefit -> show **zero**, never negative |
| Item 14A | Type 1 aggregate = GST-creditable benefits x **2.0802** (include GST-creditable excluded benefits) |
| Item 14B | Type 2 aggregate = non-GST-creditable benefits x **1.8868** |
| Item 15 | Fringe benefits taxable amount = 14A + 14B |
| Item 16 | Tax payable = 47% x Item 15 |
| Items 17/18 | Rebatable employers only -- aggregate non-rebatable amount / rebate (out of scope here: R-AU-FY-3) |
| Item 19 | Sub-total |
| Item 20 | Less instalment amounts reported on activity statements |
| Item 21 | Payment due (may round down to nearest 5c) |

**Employee contributions** reduce the taxable value of THAT benefit only (after-tax; no cross-application; assessable income to the employer with GST consequences -- au-fbt Rule 9). **Otherwise-deductible rule** reductions sit in column (c) and need the declaration in the approved form held before the declaration date, or adequate alternative records under the Commissioner's instruments (from 1 April 2024; logbooks and odometer records still need the approved form) -- au-fbt Rule 10.

**Exemptions and rebates at year end:** exempt benefits (minor benefits under s 58P, exempt EVs, s 58X devices) never enter Items 14A/14B -- but exempt EVs still generate a notional taxable value for RFBA purposes (Section 6). Rebatable employers (Items 17/18) compute the rebate against a per-employee grossed-up cap -- that computation is a refusal item here (R-AU-FY-3) because the capping regimes interact with PBI/hospital status.

**No FBT and no instalments?** Don't lodge nil returns -- use the non-lodgment notice (Section 3.1).

---

## Section 6 -- STP / RFBA interplay: the income-statement side of the cycle

### 6.1 The timing bridge

RFBA is measured on the **FBT year** (taxable value of reportable benefits 1 April -- 31 March) but reported against the **income year that ends straight after**. Benefits provided in the FBT year ending 31 March 2027 are reported through STP for the income year ending 30 June 2027 and appear on the employee's income statement once you make your **STP finalisation declaration by 14 July 2027**. RFBA is not assessable income -- it feeds income tests (Medicare levy surcharge, family assistance, child support, STSL and similar).

### 6.2 The computation (one line, always Type 2)

Individual reportable fringe benefits taxable value > **$2,000** (strictly greater) -> RFBA = taxable value x **1.8868**, reported in whole dollars. Always the Type 2 factor even where Type 1 was used for the FBT itself. Exclusions from the individual amount: car parking benefits, non-salary-packaged meal entertainment (and related travel/accommodation and entertainment facility leasing), pooled/shared car benefits, remote-area concessions, and the safety/emergency-health items. INCLUDES the notional taxable value of exempt electric cars, and benefits exempt solely because the employer is FBT-exempt (NFPs compute notional TV as if taxable). Full list: FBT guide for employers, Ch 5. Detail: au-fbt Rule 9.

### 6.3 Reporting paths -- including the small-employer annual pattern

- **In-year voluntary reporting:** YTD RFBA may be provided through a pay event (if available in payroll) or an update event at any time up to the finalisation due date. Once reported, keep carrying the YTD amount in later events.
- **Annual April pattern (small employers):** because the RFBA can't be finalised until the FBT year closes on 31 March, small employers commonly compute RFBA in April as part of FBT year-end work and push it through a single STP update event soon after -- well before the 14 July finalisation declaration. There is no separate "election" form; the obligation is simply discharged by reporting through STP before finalisation. (If you can't or don't report through STP, you must give the employee a payment summary and lodge a payment summary annual report -- and that summary must exclude anything already reported through STP.)
- **Finalisation:** arm's-length employees -- declaration by **14 July**; employers with 20+ employees reporting closely held payees -- 30 September for those payees; small employers (19 or fewer) with ONLY closely held payees -- the payee's tax return due date.

### 6.4 The April--June leaver rule

An employee who leaves between 1 April and 30 June with reportable benefits over $2,000 **in that stub period** is reported in the NEXT income year (e.g. benefits April--June 2027 -> income year ending 30 June 2028), even with no wages to report. This is the single most-missed RFBA item -- run a leaver check after 30 June before finalising.

---

## Section 7 -- GL sweep for the cycle, year-end checklist, and the paper-to-digital transition

### 7.1 Cycle-specific sweep table (export 1 April -- 31 March)

| GL account pattern | Cycle question | Where it lands |
|---|---|---|
| Entertainment, staff functions, client meals | Method elected? (actual / 50-50 / register -- au-fbt Rule 8); minor-benefit per-head screens | Item 23P or excluded; non-salary-packaged meal entertainment is NOT in RFBA |
| Motor vehicle costs -- fuel, rego, insurance, repairs | Every vehicle matched to the car register? A car with running costs but no register entry = missed benefit | Items 23A/23B |
| Car leases -- operating/finance lease payments on employee cars | Statutory vs operating cost method per car per year | Items 23A/23B |
| Novated lease payments (payroll clearing + lease invoices) | Post-1-April-2025 PHEV? EV exemption conditions? RFBA notional TV for exempt EVs | Items 23A/23B or exempt + RFBA; structuring itself is R-AU-FY-2 |
| Parking -- leased spaces, commercial car park invoices, reimbursements | Employer-premises parking benefit (threshold $11.48/day) vs reportable expense-payment reimbursement | Parking benefit NOT in RFBA; reimbursement IS |
| Employee reimbursements, round-dollar allowances | Expense payment benefits; otherwise-deductible declarations held? | Item 23E with reductions |
| Staff gifts, welfare, amenities | <$300 and infrequent per occasion? | Exempt (s 58P) or residual/property categories |
| Loans to employees / directors' debit loans | Benchmark 8.27% vs rate charged; Div 7A first for shareholders (au-fbt T2-6) | Item 23 (loans) |
| FBT instalments paid (BAS clearing account) | Reconcile to ATO activity statement account BEFORE the return | Item 20 |

### 7.2 FBT year-end checklist (April--June)

1. Export GL 1 April -- 31 March; run the sweep; build/refresh the car register and entertainment attendee analysis.
2. Collect declarations, logbooks, odometer records, lease and packaging documents BEFORE the declaration date.
3. Compute taxable values (au-fbt), split Type 1/Type 2, assemble Items 14--23; reconcile instalments to the ATO account.
4. Lodge the March-quarter BAS (return won't process until all activity statements are lodged).
5. Compute per-employee RFBA; push through STP update event; diarise the April--June leaver re-check after 30 June.
6. Lodge and pay by 21 May (or 25 June via agent-electronic); make the STP finalisation declaration by 14 July.

### 7.3 Transition off 25-year-old paper systems

Legacy pattern: shoebox of receipts, spreadsheet car register, paper FBT return posted in May, payment summaries typed in June. Modern equivalent:

- **GL codes**: separate accounts for entertainment/sustenance, per-vehicle cost centres, a novated-lease clearing account, and an FBT-instalment clearing account mapped to BAS label 6A -- so the sweep is a report, not an archaeological dig.
- **SBR-enabled software** lodges the FBT return electronically; self-lodgers no longer need the paper form, and agents lodging electronically get the 25 June date. Electronic processes in ~14 days vs ~50 business days for paper.
- **STP payroll software** carries RFBA as a YTD component; the April update-event pattern replaces the typed payment summary.
- **Records**: from 1 April 2024, adequate alternative records can replace several approved-form declarations -- digital logs and odometer photos kept through the year beat a May paper chase. (Logbooks and odometer records still need the approved form.)
- Keep the workpaper file: sweep export, car register, attendee analysis, declarations, variation estimates, STP event references. Five-year retention, FBT-year indexed.

---

## Section 8 -- Worked examples

### Example 1 -- Return assembly with instalment credit

GST-registered employer, FBT year ended 31 March 2026. Type 1 taxable values $11,000 (car $10,000 statutory + $1,000 meal entertainment), Type 2 taxable values $9,000 (expense payments). Instalments paid via BAS: $16,000.

```
14A: $11,000 x 2.0802 = $22,882.20
14B: $9,000  x 1.8868 = $16,981.20
15:  $39,863.40
16:  47% x $39,863.40 = $18,735.80 (ATO example rounds to $18,735.61 on their inputs)
19:  $18,735.80
20:  less instalments $16,000
21:  payment due $2,735.80 -- lodge and pay by 21 May 2026 (self-lodger)
```

(Arithmetic mirrors the ATO FBT return 2026 instructions, Items 14--21.)

### Example 2 -- Varying an instalment in the December quarter

F1 shows $10,000/quarter (notional $40,000 for the year). Several employees with cars left; estimate annual liability $28,000.

```
F2 = $28,000; December quarter relevant % = 75%
F3 = ($28,000 x 75%) - ($20,000 - $0) = $21,000 - $20,000 = $1,000
Enter $1,000 at F3 and 6A; F4 reason code 31 (change in employees with fringe benefits)
```

(Per the ATO BAS FBT-instalment page example.) Keep the estimate workpaper: total instalments must not fall below 90% of the actual liability without penalty exposure.

### Example 3 -- The sequencing trap

Employer paid instalments all year and is owed a $3,400 refund for the FBT year ended 31 March 2026. They lodge the FBT return on 10 May 2026 but the March-quarter BAS is outstanding. The return is NOT processed -- the refund waits until the March BAS is lodged. Lodge all four activity statements first, then the return.

### Example 4 -- RFBA across the year boundary

Employee's reportable taxable values for the FBT year ended 31 March 2026: car $3,000 + home internet reimbursement $500 = $3,500 (car parking of $450 is excluded from RFBA). > $2,000, so:

```
RFBA = $3,500 x 1.8868 = $6,603.80 -> report $6,603 (whole dollars, rounded down)
Reported through STP for the income year ended 30 June 2026; finalisation declaration by 14 July 2026.
```

(Per the ATO reportable-fringe-benefits page example, restated for the current cycle.) Not assessable income; income tests only.

### Example 5 -- Small employer, annual April RFBA pattern + leaver rule

Small employer (8 staff), one packaged car. FBT year ends 31 March 2027. In mid-April 2027 they compute the employee's RFBA ($5,660 on a $3,000 taxable value) and lodge a single STP update event with the YTD RFBA; finalisation declaration follows by 14 July 2027. The employee resigns effective 12 May 2027 and receives $2,300 of reportable benefits in April--May 2027 (the new FBT year): that $2,300 x 1.8868 = $4,339 (whole dollars) is reported in the NEXT income year (ending 30 June 2028) even though there may be no wages then. Miss this and the employee's 2027-28 income statement is wrong.

---

## Section 9 -- Refusal catalogue

Escalate; do not compute.

| Ref | Trigger | Why it stops here | Route |
|---|---|---|---|
| R-AU-FY-1 | Salary packaging design -- "how should we package?", effective-cost modelling, package redesign | Design advice shapes remuneration strategy and needs the employer's full facts, industrial instruments and individual circumstances; this guide is compliance mechanics only | Registered tax agent / remuneration specialist |
| R-AU-FY-2 | Novated lease structuring -- choosing structures, residual settings, packaging-through-lease design | Structuring advice intersects financing law, payroll configuration and the EV exemption transition (announced wind-back from 1 April 2027, not yet law); computation of a GIVEN lease's FBT is au-fbt | Specialist adviser; verify enactment status before advising |
| R-AU-FY-3 | Non-profit rebate/capping advice -- rebatable employer Items 17/18, PBI/hospital caps, which entity in a group claims | Per-employee grossed-up caps and entity-status analysis are specialist; errors are expensive and audited | NFP tax specialist |
| R-AU-FY-4 | International assignees -- expatriate benefits, tax-equalised packages, cross-border benefits, dual-year FBT/income interactions | Residency, DTA, and assignment-policy questions beyond the FBTAA mechanics | Global mobility / expatriate tax specialist |

Also still live from au-fbt: NFP capping regimes (R-AU-FBT-1), car parking valuation (R-AU-FBT-3), and never compute ESS or Div 7A outcomes inside an FBT job.

---

## Section 10 -- Reference material

### Key dates and figures (cycle summary, FBT year ending 31 March 2027)

| Item | Value |
|---|---|
| FBT year | 1 April 2026 -- 31 March 2027 |
| Return + payment, self/paper | 21 May 2027 |
| Return + payment, agent electronic | 25 June 2027 (client listed by 21 May 2027) |
| Instalment trigger | Prior-year FBT payable >= $3,000 |
| Variation penalty threshold | Instalments/estimates < 90% of actual liability |
| Variation reason codes | 22 / 30 / 31 / 32 |
| Return items | 14A x2.0802; 14B x1.8868; 16 = 47% x 15; 20 instalments; 21 payment due |
| RFBA trigger / factor | > $2,000 / x1.8868 whole dollars |
| RFBA income-year allocation | Income year ending straight after the FBT year |
| STP finalisation | 14 July (arm's length); 30 Sep closely held (20+ employees); payee's return due date (small, closely-held-only) |
| Penalty unit | $364 from 1 July 2026 |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| FBT year, rate, gross-ups, RFBA threshold/factor | ato.gov.au -- Fringe benefits tax: rates and thresholds |
| Lodgment and payment dates, non-lodgment, instalment set-off, processing times | ato.gov.au -- Lodging your FBT return and paying (QC 71178, updated 1 April 2026) |
| Agent lodgment program dates, FBT client list by 21 May | ato.gov.au -- Registered agent lodgment program: FBT return (QC 34541, updated 1 July 2026) |
| BAS labels F1/F2/F3/F4, 6A/6B, 90% rule, reason codes, variation example | ato.gov.au -- Fringe benefits tax (FBT) instalment (QC 33675) |
| Return items 14--23, Type 1/2 assembly, zero-not-negative rule, item 20/21 | ato.gov.au -- FBT return 2026 instructions: calculation details for taxable employers (QC 106238) |
| RFBA steps, exclusions, always-Type-2 factor, income-year allocation, April--June leaver rule | ato.gov.au -- Reportable fringe benefits (QC 71180); FBT guide for employers Ch 5 |
| Voluntary in-year RFBA reporting via pay/update events; payment summary fallback | ato.gov.au -- STP Phase 2 employer reporting guidelines: other components (QC 66099, updated 2 May 2026) |
| STP finalisation 14 July; closely held concessions | ato.gov.au -- End-of-year finalisation through STP |
| Statutory framework | Fringe Benefits Tax Assessment Act 1986 (esp. s 136(1) "year of tax"; Pt XIA record-keeping exemption; s 58P minor benefits; Div 9A meal entertainment) |
| Penalty unit $364 from 1 July 2026 | ato.gov.au -- penalty units indexation announcement |

### Test suite

**Test 1:** Prior-year FBT payable $2,800. -> No instalments next year (< $3,000). Single annual payment with the return.

**Test 2:** Prior-year FBT payable $4,200; return lodged by agent electronically, client listed 18 May. -> Quarterly instalments this year; return due 25 June.

**Test 3:** Client added to agent's FBT list 26 May, return unlodged. -> 21 May date governs; already late.

**Test 4:** F2 estimate $20,000 varied in the March quarter; prior instalments $13,500, no credits. -> F3 = ($20,000 x 100%) - $13,500 = $6,500 at F3/6A.

**Test 5:** Type 1 $6,000, Type 2 $2,500, instalments $9,000. -> 14A $12,481.20; 14B $4,717.00; 15 $17,198.20; 16 = 47% x $17,198.20 = $8,083.15; 21 = $8,083.15 - $9,000 = refund $916.85 after lodgment (and after all BAS lodged).

**Test 6:** Individual reportable TV exactly $2,000. -> No RFBA (must exceed). $2,000.01 -> RFBA $3,773 (ATO rates page example).

**Test 7:** Employee leaves 20 April 2027 with $2,400 reportable benefits April 2027. -> Report in income year ending 30 June 2028, not the current finalisation.

**Test 8:** Non-salary-packaged meal entertainment $4,000 + car parking $1,200 + car $5,000, one employee. -> RFBA base = $5,000 only; $5,000 x 1.8868 = $9,434 reported (whole dollars).

### Prohibitions

- NEVER use a July--June export for FBT work -- export 1 April to 31 March
- NEVER promise a client the 25 June date before confirming they are on the agent's FBT client list by 21 May
- NEVER lodge the FBT return while any activity statement for the FBT year (including the March quarter) is outstanding
- NEVER vary instalments down without a documented estimate -- sub-90% exposes penalties
- NEVER use the Type 1 gross-up without confirmed GST creditability
- NEVER report RFBA against the FBT year's own dates -- it belongs to the following income year's STP finalisation
- NEVER include car parking, non-salary-packaged meal entertainment or pooled-car values in an RFBA base; NEVER omit exempt-EV notional values from it
- NEVER show a negative taxable value at Item 23 -- floor at zero
- NEVER compute rebatable-employer Items 17/18, salary packaging designs, novated lease structures, or assignee packages -- refusal catalogue
- NEVER present figures as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by OpenAccountants.

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
