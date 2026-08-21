---
name: fi-prepayments
description: Use this skill whenever asked about Finland prepayment tax (ennakkovero) for self-employed individuals. Trigger on phrases like "ennakkovero", "ennakkoverot", "prepayment tax Finland", "Finnish tax prepayments", "residual tax Finland", "jäännösvero", "tax instalments Finland", "OmaVero prepayment", "prepayment certificate", "ennakkoperintä", or any question about paying tax during the year as a Finnish self-employed person. Covers prepayment calculation, payment schedules, adjustment requests, residual tax, and penalties. ALWAYS read this skill before advising on Finnish tax prepayments.
version: 1.0
jurisdiction: FI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - fi-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FI Prepayments

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Finland (Republic of Finland / Suomen tasavalta) |
| Tax | Prepayment Tax (ennakkovero / förskottsskatt) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Act on Tax Prepayments (ennakkoperintälaki 1118/1996); Income Tax Act (tuloverolaki 1535/1992) |
| Tax authority | Finnish Tax Administration (Verohallinto / Vero) |
| Portal | OmaVero (https://www.vero.fi/omavero) |
| Applies to | Self-employed (elinkeinonharjoittaja / ammatinharjoittaja), rental income, capital gains, other income not subject to withholding |
| Validated by | Pending |
| Validation date | Pending |
| Skill version | 1.0 |

### Key Terms

**Key Terms**

| Finnish Term | English | Meaning |
| --- | --- | --- |
| Ennakkovero | Prepayment tax | Tax paid in advance during the tax year |
| Ennakkoperintä | Tax prepayment / withholding | The system of collecting tax before final assessment |
| Jäännösvero | Residual tax | Tax still owed after prepayments are applied to the final assessment |
| Veronpalautus | Tax refund | Refund if prepayments exceed final tax liability |
| Ennakkoverolippu | Prepayment tax slip | The notice showing prepayment amounts and due dates |
| Huojennus | Reduction / relief | Applying for reduced prepayments |

## Section 2 -- Who Must Pay Ennakkovero

### 2.1 Mandatory

**2.1 Mandatory**

| Category | Obligation |
| --- | --- |
| Self-employed sole traders (toiminimiyrittäjä) | Must pay ennakkovero on estimated business income |
| Freelancers (ammatinharjoittaja) | Must pay ennakkovero on estimated professional income |
| Rental income recipients | Must pay if rental income not covered by employer withholding adjustment |
| Capital gains recipients | Must pay on estimated gains if significant |
| Partners in partnerships (Ay/Ky) | Must pay on estimated share of partnership income |

### 2.2 Not Required

**2.2 Not Required**

| Category | Reason |
| --- | --- |
| Employees (only wage income) | Employer withholding (ennakonpidätys) covers tax |
| First-year entrepreneurs with no prior estimate | Verohallinto cannot assess; must request prepayment registration |

## Section 3 -- How Ennakkovero Is Calculated

### 3.1 Basis of Calculation

- **Prior year final assessment** — If you filed a tax return for the prior year, Verohallinto uses that as the baseline and adjusts for inflation and any known changes.  _(Section 3.1)_
- **Estimated income** — For new entrepreneurs, you provide an estimate of expected annual income and expenses to Verohallinto via OmaVero.  _(Section 3.1)_
- **Taxpayer request** — You can request a change at any time during the year if your income projection changes.  _(Section 3.1)_

### 3.2 Components Included

**3.2 Components Included**

| Component | Included |
| --- | --- |
| State income tax (progressive rates) | Yes |
| Municipal tax (kunnallisvero) | Yes |
| Church tax (if applicable) | Yes |
| Health insurance contributions | Yes |
| Capital income tax (30%/34%) | Yes, on estimated capital income portion |
| YEL pension contributions | No -- paid separately to pension insurance company |
| VAT | No -- separate system |

### 3.3 New Entrepreneurs

- Register for prepayment via OmaVero or contact Verohallinto
- Provide estimated annual revenue and expenses
- Verohallinto issues a prepayment decision (ennakkoveropäätös) with amounts and due dates
- If no estimate provided, Verohallinto may set prepayments based on industry averages

## Section 4 -- Payment Schedule

### 4.1 Standard Schedule

**4.1 Standard Schedule**

| Total Annual Ennakkovero | Number of Instalments | Typical Due Dates |
| --- | --- | --- |
| Under €170 | 1 instalment | March |
| €170 -- €500 | 2 instalments | March and September |
| Over €500 | Up to 12 monthly instalments | 23rd of each month (or next business day) |

Prepayments are divided into instalments across the tax year. The number of instalments depends on the total amount:

Most self-employed with meaningful income pay monthly instalments, typically due on the 23rd of each month.

### 4.2 Payment Methods

**4.2 Payment Methods**

| Method | Detail |
| --- | --- |
| OmaVero | View amounts, due dates, and pay directly |
| Bank transfer | Using the reference number from OmaVero / prepayment decision |
| Direct debit (suoramaksu) | Can be set up via OmaVero for automatic monthly payments |
| e-Invoice | Available through some banks |

## Section 5 -- Adjusting Prepayments During the Year

### 5.1 When to Adjust

- Income significantly higher or lower than estimated
- Business started or ceased mid-year
- Major deductible expense occurred (e.g., large equipment purchase)
- Change in municipality or church membership
- YEL income changed significantly

### 5.2 How to Adjust

1. Log in to OmaVero
2. Navigate to "Prepayment tax" (Ennakkovero)
3. Submit a new estimate of annual income and expenses
4. Verohallinto recalculates and issues a revised prepayment decision
5. Remaining instalments are adjusted; already-paid amounts are credited
6. No fee or penalty for requesting an adjustment

### 5.3 Important Notes

- Adjustments can be made multiple times during the year
- Reducing prepayments too aggressively may result in residual tax + interest
- Increasing prepayments voluntarily is always possible
- Changes typically take effect within a few business days

## Section 6 -- Residual Tax and Refunds

### 6.1 After Filing

After the annual tax return is filed and assessed (typically by October-November):

**6.1 After Filing**

| Scenario | Outcome |
| --- | --- |
| Prepayments < final tax liability | Residual tax (jäännösvero) is due |
| Prepayments > final tax liability | Tax refund (veronpalautus) is issued |
| Prepayments = final tax liability | No further action |

### 6.2 Residual Tax (Jäännösvero)

**6.2 Residual Tax (Jäännösvero)**

| Item | Detail |
| --- | --- |
| Notification | Via OmaVero and/or mail |
| Payment deadline | Typically December of the assessment year or February of the following year (in two instalments if >€170) |
| Interest | Late payment interest at base rate + 7 percentage points (Verohallinto publishes the annual rate) |
| Penalty-free threshold | Minor residual tax (under certain limits) may not incur interest |

### 6.3 Tax Refund (Veronpalautus)

**6.3 Tax Refund (Veronpalautus)**

| Item | Detail |
| --- | --- |
| Timing | Typically paid in August-December of the year following the tax year |
| Method | Direct deposit to bank account registered in OmaVero |
| Interest on refund | Verohallinto pays a small credit interest on overpaid amounts |

## Section 7 -- Penalties for Underpayment

**Section 7 -- Penalties for Underpayment**

| Situation | Consequence |
| --- | --- |
| Insufficient prepayments (honest estimate) | Residual tax + interest at prescribed rate |
| No prepayment registration at all | Verohallinto may impose prepayments retrospectively; penalty interest applies |
| Deliberate underestimation | Tax increase (veronkorotus) of 2-10% on additional tax may apply |
| Late payment of instalment | Interest accrues from due date; persistent non-payment may lead to enforcement (ulosotto) |

## Section 8 -- Worked Examples

### Example 1 -- Standard Annual Cycle

**Situation:** Freelance designer, second year of business. Prior year final tax was €12,000.

1. **January:** Verohallinto issues 2025 prepayment decision based on 2024 final tax. Monthly instalments of ~€1,000, due 23rd of each month.
2. **June:** Business is slower than expected. Designer estimates 2025 income will be 30% lower. Submits adjustment via OmaVero.
3. **July:** Revised decision: remaining monthly instalments reduced to ~€583.
4. **April 2026:** Files 2025 tax return showing final tax of €9,500.
5. **Assessment:** Total prepayments made = €8,498 (6 × €1,000 + 6 × €583). Residual tax = €1,002, due in two instalments.

### Example 2 -- First-Year Entrepreneur

**Situation:** Software consultant starts business in March 2025. Estimates €50,000 gross revenue, €10,000 expenses.

1. **March:** Registers for ennakkovero via OmaVero. Provides estimate: net income €40,000.
2. **March:** Verohallinto issues prepayment decision: approximately €10,000-€12,000 total for the year, payable in 10 monthly instalments (March-December).
3. **Filing 2026:** Actual net income was €45,000. Small residual tax due.

## Section 9 -- Interaction with Other Taxes

**Section 9 -- Interaction with Other Taxes**

| System | Interaction |
| --- | --- |
| Employer withholding (ennakonpidätys) | If self-employed person also has employment income, employer withholding reduces the amount of ennakkovero needed |
| YEL pension insurance | Paid separately; not included in ennakkovero but is tax-deductible |
| VAT (ALV) | Completely separate system; VAT payments and refunds do not affect ennakkovero |
| Municipal tax | Included in ennakkovero calculation |

## Section 10 -- OmaVero Quick Guide

### Key Actions in OmaVero for Prepayments

**Key Actions in OmaVero for Prepayments**

| Action | Path |
| --- | --- |
| View prepayment decision | OmaVero → Ennakkovero → Current year |
| Request adjustment | OmaVero → Ennakkovero → Muuta ennakkoveroa (Change prepayment) |
| View payment schedule | OmaVero → Ennakkovero → Maksuerät (Instalments) |
| Pay ennakkovero | OmaVero → Maksaminen (Payments) |
| Set up direct debit | OmaVero → Maksaminen → Suoramaksu |
| View residual tax | OmaVero → Verotuspäätös (Tax assessment decision) |
| Check refund status | OmaVero → Veronpalautus (Tax refund) |

## Prohibitions

- NEVER treat ennakkovero payments as a deductible expense -- they are a credit against final tax liability
- NEVER advise skipping prepayment registration -- penalties and interest will apply
- NEVER assume prior year amounts are correct for current year without checking
- NEVER ignore the possibility of adjusting prepayments when income changes significantly
- NEVER present calculations as definitive -- always label as estimated
- NEVER advise on corporate (Oy) or partnership (Ky/Ay) prepayment tax -- different rules apply

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
