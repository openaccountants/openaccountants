---
name: au-gst-bas
description: Australian Business Activity Statement (BAS) — non-GST sections. Covers PAYG withholding (labels W1-W5), PAYG income tax instalments (labels T1-T9), FBT instalments (label F1), and PAYG withholding reconciliation. Complements australia-gst.md which covers GST labels (1A-9).
version: 1.2
jurisdiction: AU
tax_year: 2025
last_updated: 2026-08-11
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU GST Bas

## AU GST Bas

## Australia BAS — Non-GST Sections v1.1

## What this file is

**Obligation category:** CT (Consumption Tax) / ET (Estimated Tax) / WHT (Withholding Tax)
**Functional role:** Return — complementary to `australia-gst.md`
**Status:** Source-cited draft — pending accountant review

This file covers the non-GST sections of the Business Activity Statement. For GST labels (1A through 9), see `australia-gst.md` in this directory.

**Tax year coverage.** This skill targets the **2024-25 income year** (1 July 2024 to 30 June 2025).

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

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

## Section 2 — Filing requirements

### 2.1 Who must lodge a BAS

- **Activity-statement lodgement obligation** — Lodgement depends on the entity's tax roles, reporting method and the form the ATO issues. Lodge each required BAS or activity statement by its due date. Quarterly Forms R (PAYG instalment), S (GST instalment) and T (PAYG and GST instalment) generally need only be lodged when varying the instalment amount.  _([ATO — activity statements and nil lodgments](https://www.ato.gov.au/api/public/content/0-0b929c4e-ddac-4b4f-a627-7427575b94a2))_

### 2.2 Lodgement frequency

**Lodgement frequency**  _(TAA 1953 Sch 1 s 31-5)_

| Situation | BAS frequency | Source |
| --- | --- | --- |
| GST turnover < $10M, no monthly election | Quarterly | TAA 1953 Sch 1 s 31-5 |
| GST turnover >= $10M | Monthly | TAA 1953 Sch 1 s 31-5 |
| Voluntary monthly reporter | Monthly | ATO election |
| PAYG withholding-only (no GST) | Quarterly | TAA 1953 Sch 1 Div 16 |

### 2.3 Due dates (quarterly)

**Due dates (quarterly)**  _(ATO lodgement programme)_

| Quarter | Period | Due date |
| --- | --- | --- |
| Q1 | 1 Jul – 30 Sep | 28 October |
| Q2 | 1 Oct – 31 Dec | 28 February |
| Q3 | 1 Jan – 31 Mar | 28 April |
| Q4 | 1 Apr – 30 Jun | 28 July (if lodging electronically, may be extended to 25 August for Q4) |

- **Weekend/holiday due date rule** — If the due date falls on a weekend or public holiday, the due date is the next business day. Tax agents may have extended lodgement programmes.  _(ATO lodgement programme)_

## Section 3 — Rates and thresholds

### 3.1 PAYG withholding

**PAYG withholding rates and rules**  _(TAA 1953 Sch 1 Div 12)_

| Item | Detail | Source |
| --- | --- | --- |
| Withholding obligation trigger | Making payments to employees, directors, or contractors who do not quote an ABN | TAA 1953 Sch 1 Div 12 |
| No-ABN withholding rate | 47% of the payment amount | TAA 1953 Sch 1 s 12-190 |
| Voluntary agreement rate | As per the ATO tax tables or agreed rate | TAA 1953 Sch 1 s 12-55 |
| Labour hire withholding | As per ATO tax tables | TAA 1953 Sch 1 s 12-60 |

### 3.2 PAYG income tax instalments

**PAYG income tax instalment rates and thresholds**  _(TAA 1953 Sch 1 s 45-5)_

| Item | Amount / Rate | Source |
| --- | --- | --- |
| Automatic entry — individuals (including sole traders) | The ATO uses the latest tax return. Automatic entry requires all of: instalment income of $4,000 or more; tax payable on the latest notice of assessment of $1,000 or more; and estimated (notional) tax of $500 or more. | [ATO — Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments) |
| Instalment rate | As notified by the ATO (varies per taxpayer) | ATO instalment rate notice |
| GDP-adjusted rate | ATO may adjust the instalment rate annually by a GDP uplift factor | TAA 1953 Sch 1 s 45-405 |
| GDP uplift factor 2024-25 | 6% | [ATO — GDP adjustment for 2024-25 GST and PAYG instalments](https://softwaredevelopers.ato.gov.au/gdp-adjustment-2024-25-gst-and-payg-instalments) |
| Voluntary entry | A person new to business, or expecting business and investment income over the threshold, can request voluntary entry to PAYG instalments. | [ATO — Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments) |

### 3.3 FBT instalments

**FBT instalment rates and thresholds**  _(TAA 1953 Sch 1 s 45-60)_

| Item | Amount / Rate | Source |
| --- | --- | --- |
| FBT instalment threshold | Notional FBT amount >= $3,000 in prior FBT year | TAA 1953 Sch 1 s 45-60 |
| FBT year | 1 April to 31 March | FBTAA 1986 s 149 |
| Instalment rate | 25% of prior year FBT liability each quarter | TAA 1953 Sch 1 s 45-400 |

## Section 4 — Computation rules

### 4.1 PAYG withholding (labels W1-W5)

- **PAYG withholding computation steps** — **Step 1.** Identify the payments and withholding labels that apply during the period: - W1 — total salary, wages and other payments subject to withholding, where W1 must be completed; - W2 — amounts withheld from the payments shown at W1; - W3 — other amounts withheld; - W4 — amounts withheld where an ABN was not quoted; and - W5 — total amounts withheld: W2 + W3 + W4. **Step 2.** Reconcile the labels that the entity must report on its issued activity statement with payroll records, STP data and any ATO pre-fill. A small or medium withholder reporting through STP does not need to separately report W1; complete W2, W3, W4 and W5 where applicable. A large withholder that does not report through STP completes only W1; a large withholder reporting through STP does not report PAYG withholding on its activity statement. Large withholders do not complete W2, W3, W4, W5 or label 4 and must pay withheld amounts electronically on the applicable large-withholder schedule. **Step 3.** Where W2 applies, cross-check it against ATO PAYG withholding tax tables for each employee's earnings level. **Step 4.** If the entity makes payments to a supplier without an ABN, withhold 47% and account for that amount under the reporting and payment rules for the entity's withholding class. **Step 5.** Where W5 applies, report the W2 + W3 + W4 total and pay the amount due by the applicable due date.  _([ATO — PAYG withholding](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding); [ATO — PAYG withholding pre-fill for activity statements](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/stp-and-activity-statements/ato-payg-withholding-pre-fill-for-activity-statements); [ATO — changes to PAYG withholding cycles](https://www.ato.gov.au/api/public/content/0-a1d50fe2-efe7-4866-9d51-855fd171ac74))_

### 4.2 PAYG income tax instalments (labels T1-T9)

Two methods are available:

#### Method A — Instalment amount method (label T7)

- **Instalment amount method steps** — **Step 1.** ATO notifies the instalment amount on the pre-filled BAS. **Step 2.** The taxpayer reports the notified amount at T7 (or varies it). **Step 3.** If varying, the taxpayer calculates estimated tax for the year divided by the number of remaining quarters and reports at T7 with a reason for variation at T3.  _(TAA 1953 Sch 1 s 45-5)_

#### Method B — Instalment rate method (labels T1-T2)

- **Instalment rate method steps** — **Step 1.** Calculate instalment income for the quarter (T1). Instalment income = gross business and investment income. It does NOT include salary/wages (already subject to PAYG withholding), GST, or capital gains. **Step 2.** Multiply T1 by the ATO-notified instalment rate (T2). **Step 3.** Result = T1 x T2 = instalment amount payable (T9). **Step 4.** The taxpayer may vary the rate (enter new rate at T2) if they believe the notified rate will result in over-payment. A general interest charge (GIC) applies if the varied amount is less than 85% of the correct amount.  _(TAA 1953 Sch 1 s 45-120)_
- **Instalment amount formula** — T1 x T2 = instalment amount payable (T9)  _(TAA 1953 Sch 1 s 45-120)_

### 4.3 FBT instalment (label F1)

- **FBT instalment computation steps** — **Step 1.** If the taxpayer has an FBT instalment obligation, the ATO pre-fills label F1 with 25% of the prior year FBT liability. **Step 2.** The taxpayer may vary the instalment if FBT liability is expected to be lower. **Step 3.** Report at F1. The annual FBT return (due 21 May for non-tax-agent lodgement or 25 June for tax agents) reconciles the actual liability.  _(TAA 1953 Sch 1 s 45-400)_

### 4.4 Net BAS payable / refundable

- **Net BAS payable formula** — Total BAS payable = GST payable (from australia-gst.md labels) + W5 + T9 (or T7) + F1 - any credits.  _(australia-gst.md)_

## Section 5 — Edge cases and special rules

### 5.1 Variation of PAYG instalments

- **PAYG instalment variation and GIC exposure** — A taxpayer may vary their instalment amount or rate downward if they expect lower income. **GIC exposure:** If the varied amount is less than 85% of the correct instalment, a general interest charge applies on the shortfall. The GIC rate is updated quarterly by the ATO (base rate = 90-day bank bill rate + 7%). **Variation uplift factor:** If the taxpayer varies for two or more consecutive quarters, the ATO may apply a higher GDP uplift factor in the following year.  _(TAA 1953 Sch 1 s 45-205)_

### 5.2 First year of business

- **Starting PAYG instalments / first-year businesses** — The ATO works out automatic entry from information in the latest tax return. It notifies the taxpayer when they enter the PAYG instalments system, and payments start once it sends an activity statement or instalment notice. A person new to business can request voluntary entry. Under Schedule 1 section 45-15 of the Taxation Administration Act 1953, an entity is liable to pay instalments if the Commissioner has given it an instalment rate in writing.  _([ATO — Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments); [TAA 1953 Sch 1 s 45-15](https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html#_Toc235715860))_

### 5.3 STP and BAS alignment

- **STP and BAS labels** — Reporting through STP does not cancel activity-statement obligations arising from GST, PAYG instalments or other tax roles. An STP-reporting small or medium withholder does not need to separately report W1; complete the other PAYG-withholding labels required by the issued activity statement. Different reporting and payment rules apply to large withholders. ATO Online Services may pre-fill W1 and W2 from STP information for eligible electronic activity statements; use payroll records as the primary source, then verify and correct any pre-filled figures. For a small employer with 19 or fewer payees, in-scope payments to closely held payees may be reported through STP quarterly, but arm's-length payees must still be reported on or before payday. That timing concession does not itself remove BAS obligations.  _([ATO — PAYG withholding](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding); [ATO — PAYG withholding pre-fill for activity statements](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/stp-and-activity-statements/ato-payg-withholding-pre-fill-for-activity-statements); [ATO — changes to PAYG withholding cycles](https://www.ato.gov.au/api/public/content/0-a1d50fe2-efe7-4866-9d51-855fd171ac74); [ATO — STP reporting for closely held payees](https://www.ato.gov.au/Business/Single-Touch-Payroll/Concessional-reporting/Closely-held-payees/))_

### 5.4 Ceasing PAYG instalments

- **Stopping PAYG instalments** — For individuals, the ATO will automatically remove a taxpayer if one of its published automatic-exit conditions is met; this includes an estimated (notional) tax liability of less than $500. That threshold is an automatic-exit condition, not a standalone self-exit test. An individual who is no longer earning business or investment income may request to exit, subject to the ATO's eligibility requirements and listed exclusions. Individuals can request exit through myGov: **Tax > Manage > Tax registrations > Cancel** (the option is available only when eligible), through a registered tax agent, or by contacting the ATO. If the Commissioner withdraws the instalment rate, the entity ceases to be liable to pay further instalments.  _([ATO — Stopping PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments); [TAA 1953 Sch 1 s 45-90](https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html#_Toc235715874))_

### 5.5 Nil BAS / activity statement

- **Nil lodgment and FTL exposure** — If an entity has nothing to report for a BAS period but is required to lodge the BAS, it must lodge it as nil by the due date. A business that has paused trading but keeps its GST registration continues to receive a BAS and must lodge it as nil. Do not assume every zero-value activity-statement notice has that obligation: the ATO says quarterly Forms R (PAYG instalment), S (GST instalment) and T (PAYG and GST instalment) generally need only be lodged when varying the instalment amount. If a required BAS is not given to the Commissioner in approved form by its due date, the entity may be liable to an FTL administrative penalty. The base amount is one penalty unit for each 28-day period (or part) for which it remains outstanding, capped at five units; statutory multipliers apply to specified medium, large and significant-global entities. The Commissioner may remit all or part of the penalty. Use the applicable penalty-unit value for the relevant period, rather than a static tax-year dollar figure.  _([ATO — nil activity-statement guidance](https://www.ato.gov.au/api/public/content/0-0b929c4e-ddac-4b4f-a627-7427575b94a2); [ATO — paused business and nil BAS](https://www.ato.gov.au/api/public/content/0-8551e46a-7b10-44c9-b5b4-7fc8bd0c32d5); [TAA 1953 Sch 1 ss 286-75, 286-80 and 298-20](https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html); [Crimes (Amount of a Penalty Unit) Instrument 2026](https://www.legislation.gov.au/F2026N00424/asmade/2026-06-16/text/original/epub/OEBPS/document_1/document_1.html))_

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] Applicable PAYG withholding labels agree with payroll records, STP data and any ATO pre-fill
- [ ] PAYG instalment income (T1) excludes salary, GST, and capital gains
- [ ] The instalment rate (T2) matches the ATO notification or is validly varied
- [ ] FBT instalment (F1) is 25% of prior year FBT liability or validly varied
- [ ] Lodgement due date has been correctly identified (including any tax agent extensions)
- [ ] GST section cross-references to australia-gst.md output
- [ ] Rates and thresholds match the 2024-25 income year
- [ ] Output format matches the base skill spec

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

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
