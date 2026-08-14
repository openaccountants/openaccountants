---
name: lithuania-pit
description: Use this skill whenever asked to prepare, review, or classify transactions for Lithuania Personal Income Tax (Gyventojų pajamų mokestis / GPM), annual return filing with VMI, or advise on Lithuanian income tax rates and Sodra contributions. Trigger on phrases like "GPM", "pajamų mokestis", "Lithuanian income tax", "VMI", "Sodra", or any Lithuania personal tax request. ALWAYS read this skill before touching any Lithuania PIT work.
version: 1.0
jurisdiction: LT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - foundation
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lithuania Pit

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Lietuvos Respublika (Republic of Lithuania) |
| Tax | Gyventojų pajamų mokestis (GPM — Personal Income Tax) |
| Currency | EUR (€) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Current tax year | 2025 |
| Tax authority | VMI (Valstybinė mokesčių inspekcija — State Tax Inspectorate) |
| Filing portal | https://deklaravimas.vmi.lt |
| Filing deadline | 1 May of following year |
| Source credit | `sarunas/income-tax-calculator` (MIT, 21 stars) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Lithuanian mokesčių konsultantas |
| Skill version | 1.0 |

## Section 2 — Income tax rates (GPM tarifai) — 2025

### Employment income (su darbo santykiais susijusios pajamos)

**Employment income rates**

| Annual taxable income (EUR) | Rate |
| --- | --- |
| Up to €108,480 (60 × average salary) | **20%** |
| Over €108,480 | **32%** |

### Individual activity income (individualios veiklos pajamos)

**Individual activity income rates**

| Type | Rate |
| --- | --- |
| Business certificate (verslo liudijimas) | Fixed patent fee |
| Individual activity (freelance) — on profit | **15%** |
| Alternative: 5% on gross (if expenses not tracked) | **5%** gross + VSD/PSD |

### Capital income (kapitalo pajamos)

**Capital income rates**

| Type | Rate |
| --- | --- |
| Interest income | 15% |
| Dividends | 15% |
| Capital gains (securities, property) | 15% |
| Rental income (nuomos pajamos) | 15% (or 20% if registered activity) |

### Other

**Other rates**

| Type | Rate |
| --- | --- |
| Lottery / gambling winnings > €3,000 | 15% |
| Foreign dividends | 15% |

## Section 3 — Social insurance (Sodra) contributions

### Employee (darbuotojas)

**Employee Sodra contributions**

| Contribution | Rate | Cap |
| --- | --- | --- |
| Pension (pensijų) | 8.72% | No cap |
| Health (sveikatos) | 6.98% | No cap |
| **Total employee** | **15.7%** | — |

Note: Additional voluntary pension (II/III pillar) — 2.7% or more (state co-finances).

### Employer (darbdavys)

**Employer Sodra contributions**

| Contribution | Rate |
| --- | --- |
| Social insurance (VSD) | 1.77% |
| Guarantee fund | 0.16% |
| Long-term employment | 0.16% |
| **Total employer** | **~2.09%** |

### Self-employed (individualios veiklos vykdytojas)

**Self-employed Sodra contributions**

| Contribution | Base | Rate |
| --- | --- | --- |
| VSD (pension) | 90% of profit | 15.52% (or min on declared amount) |
| PSD (health) | 90% of profit | 6.98% |

## Section 4 — Non-taxable income amount (NPD)

**NPD schedule**

| Annual employment income | Monthly NPD (2025) |
| --- | --- |
| Up to ~€840/month | Full NPD: **€747** |
| €840 – €2,167/month | Proportionally reduced |
| Over €2,167/month | NPD = €0 |

- **NPD formula** — NPD = 747 − 0.5 × (monthly income − 840)

## Section 5 — Deductions and credits

**Deductions and credits**

| Deduction | Limit | Notes |
| --- | --- | --- |
| Life insurance premiums | €2,000/year | Contracts 10+ years |
| Pension fund contributions (III pillar) | €2,000/year | Voluntary |
| Renovation of housing | 30% of expenses | Max €20,000 base |
| Charitable donations | Up to 1.2% of GPM can be redirected | Via declaration |
| Education expenses | Limited | Vocational/higher education |

## Section 6 — Computation method

### Employment income

- **Employment income computation steps** — Step 1: Gross salary Step 2: − Sodra employee (15.7%) Step 3: = Taxable income Step 4: − NPD (non-taxable amount, formula-based) Step 5: = GPM base Step 6: Apply 20% (or 32% above ceiling) Step 7: = GPM amount Step 8: Net salary = Gross − Sodra − GPM

### Individual activity

- **Individual activity computation steps** — Step 1: Gross revenue from activity Step 2: − Documented expenses (or use 30% flat deduction) Step 3: = Profit Step 4: − VSD (15.52% on 90% of profit) Step 5: − PSD (6.98% on 90% of profit) Step 6: = Taxable income Step 7: Apply 15% GPM Step 8: = Tax due

## Section 7 — Worked example

**Scenario:** Employee in Vilnius, monthly gross salary €3,000. No additional deductions.

**Worked example table**

| Step | Monthly | Annual |
| --- | --- | --- |
| Gross salary | 3,000 | 36,000 |
| − Sodra employee (15.7%) | (471) | (5,652) |
| Taxable before NPD | 2,529 | 30,348 |
| − NPD | 0 (income > €2,167) | 0 |
| GPM base | 2,529 | 30,348 |
| GPM at 20% | (505.80) | (6,069.60) |
| **Net salary** | **2,023.20** | **24,278.40** |

Effective tax rate: (471 + 505.80) / 3,000 = **32.6%** (tax + social combined)

## Section 8 — Capital gains / Investment income

Per `sarunas/income-tax-calculator` (MIT):

**Capital gains / investment income table**

| Event | Tax treatment |
| --- | --- |
| Sale of listed securities | 15% on gain (purchase price deductible) |
| Sale of real estate (owned < 10 years) | 15% on gain |
| Sale of real estate (owned ≥ 10 years, registered) | Exempt |
| Dividends from Lithuanian companies | 15% (withheld at source) |
| Interest from deposits | 15% (withheld by bank) |

- **Annual exempt amount for securities gains** — €500 EUR (gains below this are tax-free)

## Section 9 — Filing guidance

### Who must file?

- **Who must file** — All residents with income not fully taxed at source; Self-employed / individual activity; Capital gains recipients; Those claiming deductions/credits; Those redirecting 1.2% to charity

### Key dates

**Key dates table**

| Event | Deadline |
| --- | --- |
| Tax year end | 31 December |
| Annual declaration deadline | 1 May |
| Payment deadline | 1 May |
| Employer monthly reporting | 15th of following month |

### Filing method

- **Filing method** — **deklaravimas.vmi.lt** — pre-filled annual return (most employed persons); VMI prepares preliminary declaration; taxpayer reviews and confirms; Amendments possible within 5 years

## Section 10 — Conservative defaults

**Conservative defaults table**

| Situation | Conservative position |
| --- | --- |
| Income source unclear | Classify as employment (highest rate); flag |
| Individual activity expense documentation weak | Use 30% flat deduction only; flag |
| Capital gains holding period uncertain | Treat as < 10 years (taxable); flag |
| Foreign income | Include if Lithuanian tax resident; flag treaty |
| Crypto gains | Classify as capital gains 15%; flag |

## Section 11 — Sources

**Sources table**

| Source | URL |
| --- | --- |
| VMI (State Tax Inspectorate) | https://www.vmi.lt |
| Sodra (Social insurance) | https://www.sodra.lt |
| `sarunas/income-tax-calculator` (MIT) | https://github.com/sarunas/income-tax-calculator |
| GPM Law (Gyventojų pajamų mokesčio įstatymas) | Nr. IX-1007 |

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
