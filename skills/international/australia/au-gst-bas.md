---
name: au-gst-bas
description: >
  Australian Business Activity Statement (BAS) — non-GST sections. Covers PAYG withholding (labels W1-W5), PAYG income tax instalments (labels T1-T9), FBT instalments (label F1), and PAYG withholding reconciliation. Complements australia-gst.md which covers GST labels (1A-9).
version: 1.0
jurisdiction: AU
tax_year: 2025
category: international
depends_on:
  - gst-workflow-base
related:
  - australia-gst.md
---

# Australia BAS — Non-GST Sections v1.0

## What this file is

**Obligation category:** CT (Consumption Tax) / ET (Estimated Tax) / WHT (Withholding Tax)
**Functional role:** Return — complementary to `australia-gst.md`
**Status:** Complete

This file covers the non-GST sections of the Business Activity Statement. For GST labels (1A through 9), see `australia-gst.md` in this directory.

**Tax year coverage.** This skill targets the **2024-25 income year** (1 July 2024 to 30 June 2025).

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers:

- **PAYG withholding labels** (W1 through W5) — amounts withheld from payments to employees and contractors
- **PAYG income tax instalment labels** (T1 through T9) — quarterly pre-payments of income tax
- **FBT instalment label** (F1) — fringe benefits tax quarterly instalments
- **Fuel tax credits** (7C, 7D) — overview only
- **BAS lodgement and payment deadlines**
- **Entity types:** Sole proprietors and individual taxpayers who lodge BAS

This skill does NOT cover:

- GST labels (1A through 9) — see `australia-gst.md`
- Partnerships, companies, trusts, or superannuation funds
- Wine equalisation tax (WET) or luxury car tax (LCT)
- Detailed fuel tax credit calculations

---

## Section 2 — Filing requirements

### 2.1 Who must lodge a BAS

Any entity registered for GST, or with a PAYG withholding obligation, or entered into the PAYG instalment system must lodge a BAS. Source: TAA 1953 Sch 1 Div 16.

### 2.2 Lodgement frequency

| Situation | BAS frequency | Source |
|-----------|---------------|--------|
| GST turnover < $10M, no monthly election | Quarterly | TAA 1953 Sch 1 s 31-5 |
| GST turnover >= $10M | Monthly | TAA 1953 Sch 1 s 31-5 |
| Voluntary monthly reporter | Monthly | ATO election |
| PAYG withholding-only (no GST) | Quarterly | TAA 1953 Sch 1 Div 16 |

### 2.3 Due dates (quarterly)

| Quarter | Period | Due date |
|---------|--------|----------|
| Q1 | 1 Jul – 30 Sep | 28 October |
| Q2 | 1 Oct – 31 Dec | 28 February |
| Q3 | 1 Jan – 31 Mar | 28 April |
| Q4 | 1 Apr – 30 Jun | 28 July (if lodging electronically, may be extended to 25 August for Q4) |

If the due date falls on a weekend or public holiday, the due date is the next business day. Tax agents may have extended lodgement programmes. Source: ATO lodgement programme.

---

## Section 3 — Rates and thresholds

### 3.1 PAYG withholding

| Item | Detail | Source |
|------|--------|--------|
| Withholding obligation trigger | Making payments to employees, directors, or contractors who do not quote an ABN | TAA 1953 Sch 1 Div 12 |
| No-ABN withholding rate | 47% of the payment amount | TAA 1953 Sch 1 s 12-190 |
| Voluntary agreement rate | As per the ATO tax tables or agreed rate | TAA 1953 Sch 1 s 12-55 |
| Labour hire withholding | As per ATO tax tables | TAA 1953 Sch 1 s 12-60 |

### 3.2 PAYG income tax instalments

| Item | Amount / Rate | Source |
|------|---------------|--------|
| Entry threshold | Instalment income >= $4,000 AND notional tax >= $1,000 in prior year | TAA 1953 Sch 1 s 45-5 |
| Instalment rate | As notified by the ATO (varies per taxpayer) | ATO instalment rate notice |
| GDP-adjusted rate | ATO may adjust the instalment rate annually by a GDP uplift factor | TAA 1953 Sch 1 s 45-405 |
| GDP uplift factor 2024-25 | 6% (to be confirmed by ATO each year) | ATO legislative instrument |
| Voluntary entry | Taxpayers can voluntarily enter the system | TAA 1953 Sch 1 s 45-15 |

### 3.3 FBT instalments

| Item | Amount / Rate | Source |
|------|---------------|--------|
| FBT instalment threshold | Notional FBT amount >= $3,000 in prior FBT year | TAA 1953 Sch 1 s 45-60 |
| FBT year | 1 April to 31 March | FBTAA 1986 s 149 |
| Instalment rate | 25% of prior year FBT liability each quarter | TAA 1953 Sch 1 s 45-400 |

---

## Section 4 — Computation rules

### 4.1 PAYG withholding (labels W1-W5)

**Step 1.** Identify all payments subject to withholding during the period:
- Salary and wages to employees (W1 — gross payments)
- Amounts withheld from salary and wages (W2)
- Other amounts withheld — voluntary agreements, labour hire, no-ABN withholding (W3, W4)
- Total amount withheld = W2 + W4 (reported at W5)

**Step 2.** Cross-check W1 against payroll records / STP (Single Touch Payroll) reports.

**Step 3.** Cross-check W2 against ATO PAYG withholding tax tables for each employee's earnings level.

**Step 4.** If the entity makes payments to contractors without an ABN, withhold 47% and include in W4.

**Step 5.** Total withholding at W5 is the amount payable to the ATO for the period.

### 4.2 PAYG income tax instalments (labels T1-T9)

Two methods are available:

#### Method A — Instalment amount method (label T7)

**Step 1.** ATO notifies the instalment amount on the pre-filled BAS.
**Step 2.** The taxpayer reports the notified amount at T7 (or varies it).
**Step 3.** If varying, the taxpayer calculates estimated tax for the year divided by the number of remaining quarters and reports at T7 with a reason for variation at T3.

#### Method B — Instalment rate method (labels T1-T2)

**Step 1.** Calculate instalment income for the quarter (T1). Instalment income = gross business and investment income. It does NOT include salary/wages (already subject to PAYG withholding), GST, or capital gains. Source: TAA 1953 Sch 1 s 45-120.

**Step 2.** Multiply T1 by the ATO-notified instalment rate (T2).

**Step 3.** Result = T1 x T2 = instalment amount payable (T9).

**Step 4.** The taxpayer may vary the rate (enter new rate at T2) if they believe the notified rate will result in over-payment. A general interest charge (GIC) applies if the varied amount is less than 85% of the correct amount.

### 4.3 FBT instalment (label F1)

**Step 1.** If the taxpayer has an FBT instalment obligation, the ATO pre-fills label F1 with 25% of the prior year FBT liability.

**Step 2.** The taxpayer may vary the instalment if FBT liability is expected to be lower.

**Step 3.** Report at F1. The annual FBT return (due 21 May for non-tax-agent lodgement or 25 June for tax agents) reconciles the actual liability.

### 4.4 Net BAS payable / refundable

Total BAS payable = GST payable (from australia-gst.md labels) + W5 + T9 (or T7) + F1 - any credits.

---

## Section 5 — Edge cases and special rules

### 5.1 Variation of PAYG instalments

- A taxpayer may vary their instalment amount or rate downward if they expect lower income. TAA 1953 Sch 1 s 45-205.
- **GIC exposure:** If the varied amount is less than 85% of the correct instalment, a general interest charge applies on the shortfall. The GIC rate is updated quarterly by the ATO (base rate = 90-day bank bill rate + 7%).
- **Variation uplift factor:** If the taxpayer varies for two or more consecutive quarters, the ATO may apply a higher GDP uplift factor in the following year.

### 5.2 First year of business

- New businesses are not required to pay PAYG instalments in their first year of operation (no prior-year benchmark). They enter the system from the first BAS after their first income tax assessment.
- PAYG withholding applies from the first payment to employees.

### 5.3 STP and BAS alignment

- Since 1 January 2022, employers reporting through STP Phase 2 may not need to separately report W1/W2 on the BAS if they are a "closely held" payee reporter. For most sole traders with employees, W1-W2 must still be reported on BAS.

### 5.4 Ceasing PAYG instalments

- A taxpayer can request to exit the PAYG instalment system if their notional tax falls below $500 or they cease business. Notify the ATO via the BAS or Business Portal.

### 5.5 Nil BAS

- If all labels are zero, a nil BAS must still be lodged by the due date. Failure to lodge a nil BAS attracts a failure-to-lodge (FTL) penalty of one penalty unit ($313 for 2024-25) for each 28-day period (up to 5 penalty units).

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] All withholding amounts (W1-W5) agree with payroll / STP records
- [ ] PAYG instalment income (T1) excludes salary, GST, and capital gains
- [ ] The instalment rate (T2) matches the ATO notification or is validly varied
- [ ] FBT instalment (F1) is 25% of prior year FBT liability or validly varied
- [ ] Lodgement due date has been correctly identified (including any tax agent extensions)
- [ ] GST section cross-references to australia-gst.md output
- [ ] Rates and thresholds match the 2024-25 income year
- [ ] Output format matches the base skill spec

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
