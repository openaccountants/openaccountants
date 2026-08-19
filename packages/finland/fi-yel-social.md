---
name: fi-yel-social
description: Use this skill whenever asked about Finland YEL pension insurance or social security for self-employed persons. Trigger on phrases like "YEL", "YEL insurance", "yrittäjän eläkelaki", "self-employed pension Finland", "Finnish pension insurance", "entrepreneur pension", "YEL income", "YEL contribution", "sickness allowance Finland", "disability pension self-employed Finland", "new entrepreneur discount", or any question about mandatory social insurance obligations for Finnish self-employed. Covers YEL contribution rates, income thresholds, provider selection, tax deductibility, and social security benefits. ALWAYS read this skill before advising on Finnish self-employed social insurance.
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

# FI Yel Social

## Section 1 -- Quick Reference

**Section 1 Quick Reference**

| Field | Value |
| --- | --- |
| Country | Finland (Republic of Finland / Suomen tasavalta) |
| System | YEL -- Self-Employed Persons' Pensions Act (Yrittäjän eläkelaki 1272/2006) |
| Currency | EUR only |
| Insurance year | Calendar year (1 January -- 31 December) |
| Primary legislation | Self-Employed Persons' Pensions Act (YEL, 1272/2006) |
| Supervising authority | Financial Supervisory Authority (Finanssivalvonta / FIN-FSA) |
| Key bodies | Pension insurance companies: Varma, Ilmarinen, Elo, Veritas |
| Validated by | Pending |
| Validation date | Pending |
| Skill version | 1.0 |

### YEL Contribution Rates (2025)

**YEL Contribution Rates (2025)**

| Age Group | Contribution Rate |
| --- | --- |
| 18 -- 52 years | 24.10% |
| 53 -- 62 years | 25.60% |
| 63 -- 69 years | 24.10% |

### New Entrepreneur Discount (2025)

**New Entrepreneur Discount (2025)**

| Item | Value |
| --- | --- |
| Discount | 22% off the standard contribution rate |
| Duration | First 48 months (4 years) of YEL insurance |
| Effective rate (ages 18-52, 63-69) | 18.798% |
| Effective rate (ages 53-62) | 19.968% |
| Eligibility | First-time YEL insurance; not previously insured under YEL for more than 18 months |

### YEL Income Thresholds (2025)

**YEL Income Thresholds (2025)**

| Threshold | Amount (EUR/year) |
| --- | --- |
| Minimum YEL income (mandatory insurance threshold) | €9,208.43 |
| Maximum YEL income | €209,125.00 |
| Unemployment benefit eligibility threshold | €15,128.00 |

### 2026 Comparison

**2026 Comparison**

| Item | 2025 | 2026 |
| --- | --- | --- |
| Contribution rate (all ages) | 24.10% / 25.60% | 24.40% (uniform) |
| Minimum YEL income | €9,208.43 | €9,423.09 |
| Maximum YEL income | €209,125.00 | €214,000.00 |

## Section 2 -- Who Must Have YEL Insurance

### 2.1 Mandatory

YEL insurance is mandatory if ALL of the following apply:

### 2.1 Mandatory

**2.1 Mandatory**

| Condition | Requirement |
| --- | --- |
| Age | 18 -- 69 years |
| Self-employment | Working as a sole trader (toiminimi), freelancer, or partner in a general/limited partnership with >30% ownership |
| Duration | Self-employment has continued or is expected to continue for at least 4 months |
| YEL income | Estimated work input value ≥€9,208.43/year (2025) |
| Residence | Working in Finland |

### 2.2 Not Required

**2.2 Not Required**

| Situation | Reason |
| --- | --- |
| Annual work input value <€9,208.43 | Below mandatory threshold |
| Self-employment <4 months | Too short |
| Under 18 or over 69 | Outside age range |
| Light entrepreneurship (laskutuspalvelu) | May be considered employment -- depends on status |

### 2.3 Must Arrange Within

- **Deadline to arrange YEL insurance** — YEL insurance must be taken out within 6 months of starting self-employment. Insurance is retroactive to the start date. Failure to arrange YEL results in Eläketurvakeskus (Finnish Centre for Pensions) arranging it compulsorily + a penalty surcharge.

## Section 3 -- YEL Income (Työtulo)

### 3.1 Definition

- **YEL income (vahvistettu työtulo)** — YEL income (vahvistettu työtulo) is the estimated monetary value of the self-employed person's annual work input -- equivalent to what you would pay a similarly skilled employee to do the same work. YEL income is NOT: - Actual business revenue - Net profit - Taxable income

### 3.2 Setting YEL Income

**3.2 Setting YEL Income**

| Factor | Consideration |
| --- | --- |
| Industry | Average salary for the sector |
| Hours | Full-time vs part-time |
| Skill level | Professional qualifications |
| Turnover | Indicative but not determinative |

- **Standardised YEL income calculation service** — Since 2023, pension providers use a standardised YEL income calculation service based on field of business and turnover, providing a recommended level (±30% range).

### 3.3 YEL Income Reviews

- **YEL income review frequency** — Pension providers review YEL income every 3 years  _(2023 YEL reform)_
- **Maximum increase per review** — €4,000  _(2023 YEL reform)_
- **Cap application from 2026** — From 2026, this cap applies to all insured (including those who started in 2023-2025)  _(2023 YEL reform)_
- **Proactive adjustment** — Self-employed can proactively adjust YEL income at any time via their pension provider  _(2023 YEL reform)_

## Section 4 -- Contribution Calculation

### 4.1 Formula

- **Annual YEL contribution formula** — Annual YEL contribution = Confirmed YEL income × Contribution rate

### 4.2 Examples (2025)

**4.2 Examples (2025)**

| Scenario | YEL Income | Age | Rate | Annual Contribution | Monthly Equivalent |
| --- | --- | --- | --- | --- | --- |
| Minimum, standard | €9,208.43 | 35 | 24.10% | €2,219.23 | €184.94 |
| Minimum, new entrepreneur | €9,208.43 | 35 | 18.798% | €1,731.03 | €144.25 |
| Median | €28,000 | 40 | 24.10% | €6,748.00 | €562.33 |
| Median, new entrepreneur | €28,000 | 40 | 18.798% | €5,263.44 | €438.62 |
| Unemployment threshold | €15,128 | 30 | 24.10% | €3,645.85 | €303.82 |
| Higher income | €60,000 | 55 | 25.60% | €15,360.00 | €1,280.00 |

### 4.3 Flexible Contributions

Self-employed can temporarily adjust contributions:

**4.3 Flexible Contributions**

| Direction | Range | Effect |
| --- | --- | --- |
| Increase | Up to +100% of standard contribution | Increases pension accrual for that year |
| Decrease | Down to -20% of standard contribution | Reduces pension accrual; stricter conditions |
| Duration | One year at a time | Must notify pension provider |
| Effect on YEL income | None -- confirmed income stays the same | Only affects actual contribution paid |

## Section 5 -- Tax Treatment

### 5.1 Deductibility

**5.1 Deductibility**

| Item | Treatment |
| --- | --- |
| YEL contributions paid by self-employed person | Fully deductible from personal income taxation |
| Deduction location | Personal tax return (not business income deduction) |
| Can be allocated to spouse | Yes, if both agree -- can be deducted from either spouse's income |
| Effect on business income | Reduces total taxable income; does NOT reduce business net profit |

### 5.2 Important Distinction

- **YEL deduction location** — YEL contributions are deducted from the self-employed person's personal taxes, not from business profits. They appear on the personal tax return, not the income statement (tuloslaskelma) of the business.

## Section 6 -- Benefits Linked to YEL Income

YEL income determines the basis for multiple social security benefits:

**Section 6 -- Benefits Linked to YEL Income**

| Benefit | Link to YEL Income |
| --- | --- |
| Old-age pension (vanhuuseläke) | Pension accrues at 1.5% of YEL income per year |
| Disability pension (työkyvyttömyyseläke) | Based on YEL income history |
| Sickness daily allowance (sairauspäiväraha) | Kela calculates from YEL income |
| Parental allowance (vanhempainpäiväraha) | Kela calculates from YEL income |
| Unemployment allowance | Requires YEL income ≥€15,128/year (2025) + membership in Entrepreneur Fund |
| Workers' compensation (if voluntary) | Must be at least YEL income level |

### 6.1 Pension Accrual

**6.1 Pension Accrual**

| Item | Value |
| --- | --- |
| Accrual rate | 1.5% of confirmed YEL income per year (all ages, from 2017) |
| Retirement age | Graduated by birth year; approximately 65-66 for those born in the 1970s-1980s |

### 6.2 Sickness Allowance

- Waiting period: onset day + 9 following working days (self-employed)
- Amount: calculated from YEL income
- Low YEL income = low sickness allowance
- Minimum daily allowance from Kela if no YEL or very low YEL

## Section 7 -- Provider Selection

### 7.1 Choosing a Pension Company

Self-employed persons choose their own YEL provider from authorised pension insurance companies:

**7.1 Choosing a Pension Company**

| Provider | Website |
| --- | --- |
| Varma | varma.fi |
| Ilmarinen | ilmarinen.fi |
| Elo | elo.fi |
| Veritas | veritas.fi |

### 7.2 Key Facts

- Contribution rates are identical across all providers (set by law)
- YEL income confirmation uses the same calculation service
- Providers differ in customer service, digital tools, and investment returns
- Self-employed can transfer YEL insurance between providers (with notice period)
- No cost to switch providers

## Section 8 -- Payment

### 8.1 Payment Schedule

**8.1 Payment Schedule**

| Option | Detail |
| --- | --- |
| Monthly | Due on a date chosen by the insured |
| Every 2 months | Alternative schedule |
| Every 3 months | Alternative schedule |
| Every 6 months | Alternative schedule |
| Annually | Lump sum |

### 8.2 Late Payment

**8.2 Late Payment**

| Situation | Consequence |
| --- | --- |
| Late payment | Interest at prescribed rate (2.65% in 2025) |
| Persistent non-payment | Pension company may terminate insurance; Eläketurvakeskus arranges compulsory insurance |
| Compulsory insurance | Penalty surcharge applies (up to 50% increase) |

## Section 9 -- Compulsory Arrangement by Eläketurvakeskus

If a self-employed person fails to arrange mandatory YEL insurance:

1. Eläketurvakeskus (ETK) sends a notice requiring insurance
2. If not arranged within the given time, ETK takes out insurance on behalf of the person
3. Compulsory insurance is retroactive to the start of self-employment
4. A negligence increase of up to 50% is added to the contribution
5. No new entrepreneur discount is available for compulsory insurance

## Section 10 -- Interaction with Other Systems

**Section 10 -- Interaction with Other Systems**

| System | Interaction |
| --- | --- |
| TyEL (employees' pension) | If self-employed person also has employment, TyEL and YEL run in parallel; both accrue pension |
| Kela benefits | YEL income is the basis for sickness, parental, and rehabilitation allowances |
| Income tax | YEL contributions are deductible; see **fi-income-tax** skill |
| Unemployment | YEL income ≥€15,128 + Entrepreneur Fund membership required for earnings-related unemployment allowance |

## Prohibitions

- NEVER advise setting YEL income at minimum to "save money" without explaining the consequences for pension, sickness allowance, and unemployment benefits
- NEVER treat YEL contributions as a business expense -- they are a personal tax deduction
- NEVER ignore the 6-month deadline for arranging YEL insurance
- NEVER assume light entrepreneurs (laskutuspalvelu users) are exempt -- status depends on actual work arrangement
- NEVER present YEL income as equivalent to business revenue or profit
- NEVER advise on TyEL (employee pension) matters -- different system

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
