---
name: bangladesh-pit
description: Use this skill whenever asked to prepare, review, or classify transactions for Bangladesh Personal Income Tax, annual return filing with NBR, or advise on Bangladeshi income tax slabs, exemptions, and investment rebates. Trigger on phrases like "আয়কর", "income tax Bangladesh", "NBR", "TIN", "salary tax BD", or any Bangladesh personal tax request. ALWAYS read this skill before touching any Bangladesh PIT work.
version: 1.0
jurisdiction: BD
tax_year: 2024
last_updated: 2026-07-13
review_status: pending_review
depends_on: - foundation
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bangladesh Pit

## Bangladesh Personal Income Tax (আয়কর) Skill v1.0

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Bangladesh (বাংলাদেশ) |
| Tax | আয়কর (Income Tax) |
| Currency | BDT (Bangladeshi Taka / ৳) |
| Tax year | 1 July – 30 June |
| Current tax year | 2024-25 (July 2024 – June 2025) |
| Tax authority | National Board of Revenue (NBR / জাতীয় রাজস্ব বোর্ড) |
| Return form | IT-11GA (individual) |
| Filing portal | https://etaxnbr.gov.bd |
| Filing deadline | 30 November (individual); extendable to 31 January |
| TIN | 12-digit Taxpayer Identification Number |
| Minimum tax | ৳5,000 (Dhaka/Chittagong city); ৳4,000 (other city); ৳3,000 (elsewhere) |
| Source credit | `ssi-anik/bd-income-tax-calculator` (MPL-2.0, 87 stars) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Bangladeshi CA or tax consultant |
| Skill version | 1.0 |

## Section 2 — Tax-free threshold by taxpayer category

**Tax-free threshold by taxpayer category**

| Taxpayer category | Tax-free threshold (BDT) |
| --- | --- |
| General (male, under 65) | 3,50,000 |
| Female or age 65+ | 4,00,000 |
| Specially-abled (প্রতিবন্ধী) | 4,75,000 |
| Gazetted freedom fighter (মুক্তিযোদ্ধা) | 5,00,000 |

## Section 3 — Progressive tax slabs

Tax is applied on income exceeding the tax-free threshold:

**Progressive tax slabs**

| Slab (on taxable income above threshold) | Rate |
| --- | --- |
| First ৳1,00,000 | 5% |
| Next ৳4,00,000 | 10% |
| Next ৳5,00,000 | 15% |
| Next ৳5,00,000 | 20% |
| Next ৳20,00,000 | 25% |
| Remainder above ৳35,00,000 | 30% |

- **Minimum tax rule** — Even if calculated tax is less, minimum tax applies based on location.

## Section 4 — Salary income exemptions

For salaried employees, the following components have exemptions:

**Salary income exemptions**

| Component | Tax-free limit |
| --- | --- |
| Basic salary | Fully taxable |
| House rent allowance | 50% of basic OR actual rent, whichever is lower; max ৳25,000/month |
| Medical allowance | 10% of basic; max ৳10,000/month |
| Conveyance allowance | Max ৳2,500/month |
| Leave fare assistance (LFA) | Actual or per employer policy |
| Festival bonus | Fully taxable |

- **Taxable salary formula** — Taxable salary = Gross salary − exempt portions of HRA, medical, conveyance

## Section 5 — Investment tax rebate (বিনিয়োগ রেয়াত)

Eligible investments include: life insurance premiums, provident fund contributions, mutual fund units, approved savings certificates, pension schemes, listed shares (held 1+ year), DPS, and donations.

### Rebate calculation

**Rebate calculation**

| Total taxable income | Rebate rate tiers |
| --- | --- |
| Up to ৳10,00,000 | 15% on first ৳2,50,000 of qualifying investment |
| ৳10,00,001 – ৳30,00,000 | 15% on first ৳2,50,000 + 12% on next ৳5,00,000 |
| Over ৳30,00,000 | 15% on first ৳2,50,000 + 12% on next ৳5,00,000 + 10% on remainder |

- **Investment rebate cap** — Max qualifying investment = 25% of total taxable income OR ৳1,50,00,000 (1.5 crore), whichever is lower.

## Section 6 — Computation method

Step 1: Calculate total income from all heads
        (Salary, House Property, Business/Profession, Capital Gains, Other Sources)
Step 2: Determine taxpayer category → tax-free threshold
Step 3: Taxable income = Total income − tax-free threshold
Step 4: Apply progressive slabs (Section 3)
Step 5: = Gross tax
Step 6: − Investment rebate (Section 5)
Step 7: = Net tax payable
Step 8: Ensure ≥ minimum tax (Section 1)
Step 9: − Tax Deducted at Source (TDS) / Advance Income Tax (AIT)
Step 10: = Final tax payable or refund

## Section 7 — Worked example

**Scenario:** Male employee in Dhaka, age 35, annual salary: Basic ৳60,000/month, HRA ৳30,000/month, Medical ৳6,000/month, Conveyance ৳2,500/month, Festival bonus ৳1,20,000/year. Investment in savings certificates: ৳3,00,000.

**Component breakdown table**

| Component | Annual | Exempt | Taxable |
| --- | --- | --- | --- |
| Basic | 7,20,000 | 0 | 7,20,000 |
| House rent | 3,60,000 | 3,00,000 (25K×12) | 60,000 |
| Medical | 72,000 | 72,000 (10%×basic, within cap) | 0 |
| Conveyance | 30,000 | 30,000 (2,500×12) | 0 |
| Festival bonus | 1,20,000 | 0 | 1,20,000 |
| **Total** | **13,02,000** |  | **9,00,000** |

Tax calculation (male, general threshold ৳3,50,000):

**Tax calculation table**

| Slab | Amount | Rate | Tax |
| --- | --- | --- | --- |
| Threshold (exempt) | 3,50,000 | 0% | 0 |
| Next 1,00,000 | 1,00,000 | 5% | 5,000 |
| Next 4,00,000 | 4,00,000 | 10% | 40,000 |
| Remaining 50,000 | 50,000 | 15% | 7,500 |
| **Gross tax** |  |  | **52,500** |

Investment rebate: min(25% × 9,00,000 = 2,25,000; actual 3,00,000) → qualifying = ₹2,25,000
Rebate: 15% × 2,25,000 = ৳33,750

**Net tax: 52,500 − 33,750 = ৳18,750** (above minimum tax of ৳5,000 ✓)

## Section 8 — Filing guidance

### Who must file?

- Any person with TIN (mandatory for many services: bank account >1M, credit card, import/export, company directorship, city corporation trade license)
- Any person with taxable income above threshold

### Key dates

**Key dates**

| Event | Deadline |
| --- | --- |
| Tax year end | 30 June |
| Return filing deadline | 30 November |
| Extended deadline | 31 January (with application) |
| Tax Day (return submission event) | November |

### Heads of income

**Heads of income**

| Head | Examples |
| --- | --- |
| Salary | Employment income |
| House property | Rental income |
| Business/Profession | Self-employment, trade |
| Capital gains | Sale of property, shares |
| Other sources | Interest, dividends, royalties |

## Section 9 — Conservative defaults

**Conservative defaults**

| Situation | Conservative position |
| --- | --- |
| Salary component unclear | Classify as taxable; flag for reviewer |
| Investment rebate documentation missing | Do not claim; flag |
| TDS certificate unavailable | Do not offset; flag |
| Foreign income | Include if resident; flag treaty applicability |
| Minimum tax vs calculated | Apply minimum tax if calculated is lower |

## Section 10 — Sources

**Sources**

| Source | URL |
| --- | --- |
| NBR (National Board of Revenue) | https://nbr.gov.bd |
| e-Tax NBR | https://etaxnbr.gov.bd |
| Income Tax Ordinance, 1984 | — |
| `ssi-anik/bd-income-tax-calculator` (MPL-2.0) | https://github.com/ssi-anik/bd-income-tax-calculator |

## *OpenAccountants — open-source accounting skills for AI*

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed by a qualified professional before filing.*

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
