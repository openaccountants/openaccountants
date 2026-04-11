---
name: au-payg-instalments
description: >
  Australian PAYG Instalments computation for sole traders. Covers entry/exit thresholds, instalment rate method (T1/T2), instalment amount method (T7), GDP uplift factor, voluntary variation, GIC exposure on under-estimation, and quarterly/annual election.
version: 1.0
jurisdiction: AU
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
related:
  - au-gst-bas.md
---

# Australia PAYG Instalments v1.0

## What this file is

**Obligation category:** ET (Estimated Tax)
**Functional role:** Computation
**Status:** Complete

This file provides the detailed computation logic for PAYG income tax instalments payable by sole traders via the Business Activity Statement (BAS). The BAS labels for PAYG instalments (T1-T9) are also summarised in `au-gst-bas.md`, but this skill provides the full computation detail and worked examples.

**Tax year coverage.** This skill targets the **2024-25 income year** (1 July 2024 to 30 June 2025).

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers:

- **Forms:** BAS labels T1 through T9
- **Entity types:** Sole proprietors who are in the PAYG instalment system
- Entry into and exit from the PAYG instalment system
- Instalment rate method vs instalment amount method
- Variation of instalments
- GIC consequences of under-estimation
- Annual instalment election

This skill does NOT cover:

- PAYG withholding (W labels) — see `au-gst-bas.md`
- Companies, trusts, or partnerships as instalment payers
- GST computation — see `australia-gst.md`

---

## Section 2 — Filing requirements

### 2.1 Statutory basis

The PAYG instalment system is governed by TAA 1953 Sch 1 Div 45. It requires taxpayers with business and investment income above a threshold to make quarterly pre-payments of income tax through their BAS.

### 2.2 Who enters the system

A taxpayer is automatically entered into the PAYG instalment system if their most recent income tax assessment shows:

| Condition | Threshold | Source |
|-----------|-----------|--------|
| Instalment income | >= $4,000 | TAA 1953 Sch 1 s 45-5(1)(a) |
| AND notional tax | >= $1,000 | TAA 1953 Sch 1 s 45-5(1)(b) |

**Instalment income** = gross business income + gross investment income. It excludes salary/wages (already subject to PAYG withholding), net capital gains, and exempt income.

**Notional tax** = estimated tax on instalment income calculated by the ATO from the prior year assessment.

### 2.3 Voluntary entry

A taxpayer who does not meet the automatic entry thresholds may voluntarily enter the system. This is useful to spread expected tax liability across the year. Source: TAA 1953 Sch 1 s 45-15.

### 2.4 How to exit

A taxpayer can apply to exit the system if:
- Their notional tax drops below $500, OR
- They have ceased deriving instalment income.

Notify the ATO through the Business Portal or by phone. Source: TAA 1953 Sch 1 s 45-10.

### 2.5 Quarterly due dates

Same as BAS due dates — see `au-gst-bas.md` Section 2.3.

---

## Section 3 — Rates and thresholds

| Item | 2024-25 Value | Source |
|------|---------------|--------|
| Instalment income threshold | $4,000 | TAA 1953 Sch 1 s 45-5 |
| Notional tax threshold | $1,000 | TAA 1953 Sch 1 s 45-5 |
| Exit threshold | Notional tax < $500 | TAA 1953 Sch 1 s 45-10 |
| GDP uplift factor | 6% (subject to ATO annual determination) | TAA 1953 Sch 1 s 45-405 |
| GIC rate | Base rate (90-day bank bill rate) + 7%, updated quarterly | TAA 1953 Sch 1 s 45-230, TAA s 8AAD |
| Variation safe harbour | 85% of correct instalment amount | TAA 1953 Sch 1 s 45-230 |
| Annual instalment election turnover threshold | Instalment income < $2M and GST turnover < $2M | TAA 1953 Sch 1 s 45-140 |

---

## Section 4 — Computation rules

### 4.1 Method selection

The ATO determines the method for each taxpayer. Two methods:

| Method | Labels used | How it works |
|--------|------------|--------------|
| Instalment amount | T7 | ATO notifies a fixed dollar amount per quarter |
| Instalment rate | T1, T2, T9 | Taxpayer reports actual instalment income, multiplied by ATO-notified rate |

Taxpayers using the instalment amount method may switch to the instalment rate method by notifying the ATO. The reverse switch is not available — the ATO assigns instalment amount when appropriate.

### 4.2 Instalment rate method — step by step

**Step 1.** Calculate instalment income for the quarter (label T1).

Instalment income includes:
- Gross business income (sales, fees, commissions)
- Interest income
- Dividend income (unfranked amount + franking credits)
- Rental income (gross rent)
- Royalties
- Trust distributions (assessable amount)

Instalment income excludes:
- Salary and wages
- Net capital gains
- Exempt income
- GST collected
- Non-assessable non-exempt income

**Step 2.** Obtain the ATO-notified instalment rate (label T2).

The ATO calculates this as: (notional tax / instalment income from prior year) x GDP uplift factor. The rate is expressed as a percentage (e.g., 12.50%).

**Step 3.** Calculate the instalment amount:

```
T9 = T1 x T2
```

Round to whole dollars.

**Step 4.** Report T1, T2, and T9 on the BAS. Pay T9 by the BAS due date.

#### Worked example — instalment rate method

| Item | Amount |
|------|--------|
| Quarter 1 business income | $42,000 |
| Quarter 1 interest income | $800 |
| Quarter 1 instalment income (T1) | $42,800 |
| ATO-notified instalment rate (T2) | 8.50% |
| Instalment payable (T9) = $42,800 x 8.50% | $3,638 |

### 4.3 Instalment amount method — step by step

**Step 1.** The ATO notifies the instalment amount on the pre-filled BAS (label T7).

The amount is calculated as: (prior year notional tax / 4) x GDP uplift factor.

**Step 2.** The taxpayer reports T7 on the BAS and pays by the due date.

**Step 3.** No calculation of instalment income is required.

#### Worked example — instalment amount method

| Item | Amount |
|------|--------|
| Prior year notional tax | $12,000 |
| GDP uplift factor | 1.06 |
| Annual instalment amount | $12,720 |
| Quarterly instalment (T7) = $12,720 / 4 | $3,180 |

### 4.4 Variation of instalments

A taxpayer can vary either the instalment rate (T2) or the instalment amount (T7) downward if they believe the ATO-notified figure will result in over-payment.

**Step 1.** Estimate the current year's tax liability.

**Step 2.** Calculate the appropriate instalment rate or amount for the remaining quarters.

**Step 3.** Report the varied rate or amount on the BAS. Provide a reason code at T3.

**Step 4.** GIC exposure check — if the total of varied instalments for the year is less than 85% of the "benchmark instalment" (i.e., the instalment that would have been correct based on the actual assessment), a general interest charge applies on the shortfall from each instalment due date to the date the annual assessment is due. Source: TAA 1953 Sch 1 s 45-230.

### 4.5 Credit on annual assessment

**Step 1.** At year-end, the total PAYG instalments paid during the year are credited against the taxpayer's annual income tax assessment.

**Step 2.** If instalments exceed the actual tax liability, the taxpayer receives a refund (or offset against other debts).

**Step 3.** If instalments are less than the actual tax liability, the shortfall is payable with the annual assessment.

---

## Section 5 — Edge cases and special rules

### 5.1 First year of business

New sole traders are not entered into the PAYG instalment system until after their first income tax assessment. No instalments are payable during the first year of business. This can create a tax shock in Year 2 when the taxpayer must pay both the Year 1 balance and begin Year 2 instalments.

**Recommendation:** Flag this to the reviewer. The client should set aside estimated tax during Year 1.

### 5.2 Seasonal or irregular income

Taxpayers with seasonal income may benefit from the instalment rate method, as the instalment amount automatically adjusts with income each quarter. If using the instalment amount method, consider varying the amount in low-income quarters.

### 5.3 Multiple business activities

If a sole trader operates multiple businesses, instalment income is the total across all activities. The instalment rate applies to the aggregate.

### 5.4 Investment income included

Instalment income includes investment income (interest, dividends, rent). Taxpayers who are employees with significant investment income may enter the PAYG instalment system even without a business.

### 5.5 Interaction with Medicare levy and Medicare levy surcharge

The ATO-notified instalment rate already factors in the Medicare levy (2%) and any Medicare levy surcharge. No separate adjustment is needed by the taxpayer.

### 5.6 Death of a taxpayer

If a sole trader dies during the income year, the legal personal representative must lodge any outstanding BAS and pay any outstanding instalments. Source: TAA 1953 Sch 1 s 45-25.

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] Taxpayer meets the entry threshold ($4,000 instalment income AND $1,000 notional tax)
- [ ] Correct method identified (instalment rate vs instalment amount)
- [ ] Instalment income (T1) includes only the correct components (no salary, no CGT, no GST)
- [ ] Instalment rate (T2) matches the ATO notification or is validly varied
- [ ] If varied, the 85% safe harbour is checked against estimated actual tax
- [ ] GDP uplift factor is current year's factor
- [ ] Quarterly due dates are correctly identified
- [ ] Year-end credit against annual assessment is noted
- [ ] First-year-of-business exception is checked
- [ ] Rates and thresholds match the 2024-25 income year
- [ ] Output format matches the base skill spec

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
