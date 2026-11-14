---
name: il-income-tax
description: "Compute an Illinois resident's 2026 individual income tax on Form IL-1040 for a sole proprietor or single-member LLC owner. Covers the flat 4.95% rate, Illinois base income from federal adjusted gross income with Schedule M additions and subtractions, the 2026 exemption allowance of $2,925 per exemption plus $1,000 for age 65 or blindness, the $250,000 and $500,000 income cut-offs that remove the exemption and the property tax and K-12 credits, the 5% property tax credit, the K-12 education expense credit, the refundable earned income tax credit at 20% of the federal credit, the child tax credit, and the bonus depreciation add-back. Trigger on \"Illinois income tax\", \"IL-1040\", \"Schedule M Illinois\", \"Illinois exemption allowance\", \"Illinois property tax credit\", \"Illinois EITC\". Load us-schedule-c-and-se-computation first for the federal profit."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-income-tax"
  jurisdiction: "US-IL"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Illinois individual income tax (Form IL-1040), tax year 2026

> **Source-cited draft.** Built from 35 ILCS 5/201, 5/203, 5/204, 5/207, 5/208, 5/212 and 5/505 (Illinois General Assembly), IDOR Informational Bulletin FY 2026-15 and the 2026 Form IL-1040-ES, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Illinois taxes a resident's net income at a flat **4.95%** (35 ILCS 5/201(b)(5.4)). Net income is Illinois base income (federal adjusted gross income plus Schedule M additions, minus Schedule M subtractions) minus the exemption allowance: **$2,925** per exemption for 2026, plus **$1,000** for a taxpayer or spouse who is 65 or older or blind. There is no standard or itemized deduction. If federal adjusted gross income is over **$250,000** (over **$500,000** on a joint return), the exemption allowance, the property tax credit and the K-12 education expense credit are all lost in full: it is a cliff, not a phase-out. The 2026 return is due **15 April 2027**.

## Scope and who this is for

In scope: a full-year Illinois resident filing Form IL-1040 for tax year 2026 whose business income is a Schedule C sole proprietorship or a single-member LLC disregarded for federal tax, with Schedule M, Schedule ICR (property tax and K-12 credits) and Schedule IL-E/EITC.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal Schedule C profit and self-employment tax (they set federal adjusted gross income) | `us-schedule-c-and-se-computation` |
| Federal Form 1040 and adjusted gross income | `us-form-1040-individual-return` |
| Illinois estimated payments during 2026 (Form IL-1040-ES) | `il-estimated-tax` |
| Illinois withholding by an employer | `il-payroll` |
| Partnerships, S corporations, corporations, replacement tax, the pass-through entity tax | `il-pprt` |
| Federal bonus depreciation figures | `us-section-179-and-bonus-depreciation` |
| Moving into or out of Illinois, multi-state residency | `us-multi-state-residency-and-allocation` |

## Ask the client first

1. **Filing status and dependents** on the 2026 federal return. Each exemption claimed federally is one Illinois exemption of $2,925 (35 ILCS 5/204(c)).
2. **Age 65 or older, or blind, at the end of 2026** (taxpayer and spouse). Each adds $1,000.
3. **Federal adjusted gross income** (Form 1040 line 11). Over $250,000, or over $500,000 joint, removes the exemption and two credits.
4. **Interest and dividends excluded federally** (municipal bonds of other states) and **U.S. Treasury interest**: an addition and a subtraction.
5. **Social Security, railroad retirement, IRA, pension and 401(k) distributions** in federal adjusted gross income: subtracted.
6. **Bonus depreciation** claimed on the federal return for 2026 (section 168(k) or 168(n)): added back.
7. **Real property tax paid in 2026 on the principal residence**, and **K-12 tuition, book and lab fees** paid for each Illinois pupil.
8. **Federal earned income credit** amount, and any dependent under 12 (child tax credit).
9. **Illinois withholding** (W-2 box 17) and **2026 estimated payments** made.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Individual income tax rate on net income (taxable years beginning on or after 1 July 2017) | 4.95% | [35 ILCS 5/201(b)(5.4)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| Exemption allowance per exemption, tax year 2026 | $2,925 | [IDOR Bulletin FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html) |
| Exemption allowance per exemption, tax year 2025 (for 2025 returns filed in 2026) | $2,850 | [IDOR Bulletin FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html) |
| Additional exemption, taxpayer (or spouse) 65 or older before the end of the year | $1,000 each | [35 ILCS 5/204(d)(1)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204) |
| Additional exemption, taxpayer (or spouse) blind at the end of the year | $1,000 each | [35 ILCS 5/204(d)(2)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204) |
| No exemption at all if adjusted gross income exceeds: joint return | $500,000 | [35 ILCS 5/204(g)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204) |
| No exemption at all if adjusted gross income exceeds: all other returns | $250,000 | [35 ILCS 5/204(g)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204) |
| Property tax credit: share of real property tax paid on the principal residence | 5% | [35 ILCS 5/208](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K208) |
| Property tax credit not allowed if adjusted gross income exceeds $500,000 joint or $250,000 other | same cut-offs | [35 ILCS 5/208](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K208) |
| K-12 education expense credit: share of qualified expenses (expenses per pupil above $250) | 25% | [35 ILCS 5/201(m)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| K-12 credit: first expenses per pupil that do not count | $250 | [35 ILCS 5/201(m)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| K-12 credit: maximum per family (tax years ending on or after 31 December 2017) | $750 | [35 ILCS 5/201(m)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| K-12 credit not allowed if adjusted gross income exceeds $500,000 joint or $250,000 other | same cut-offs | [35 ILCS 5/201(m)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201) |
| Earned income tax credit: share of the federal credit (taxable years beginning on or after 1 January 2023), refundable | 20% | [35 ILCS 5/212(a), (b)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K212) |
| Child tax credit: share of the Illinois EITC, for a qualifying dependent under 12 (2025-2026 filing cycle) | 40% | [IDOR Bulletin FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html) |
| Return due date, calendar year (15th day of the 4th month after year end) | 15 April 2027 | [35 ILCS 5/505(a)(2)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K505) |

The rate and the $1,000 additions are fixed in the statute. The exemption allowance is $2,050 plus a cost-of-living adjustment each year (35 ILCS 5/204(b)(7) and (d-5)), so it changes every year; the $250,000 and $500,000 cut-offs are not indexed.

### From federal adjusted gross income to tax

1. **Line 1, federal adjusted gross income** from federal Form 1040 line 11. Because Illinois starts from adjusted gross income, the federal standard deduction, itemized deductions and the qualified business income deduction never reach the Illinois return.
2. **Additions (Form IL-1040 lines 2 and 3, Schedule M)**, from 35 ILCS 5/203(a)(2):
   - interest and dividends excluded from federal gross income, such as interest on other states' municipal bonds (203(a)(2)(A));
   - Illinois income tax deducted in arriving at adjusted gross income (203(a)(2)(B));
   - the bonus depreciation deduction taken federally: for taxable years 2026 and later, under section 168(k) or 168(n) (203(a)(2)(D-15));
   - in the year bonus-depreciated property is sold or fully depreciated, the earlier subtractions for that property (203(a)(2)(D-16));
   - gain excluded federally under section 1202, for taxable years ending on and after 31 December 2026 (203(a)(2)(D-26)).
3. **Subtractions (lines 5 to 7, Schedule M)**, from 35 ILCS 5/203(a)(2):
   - qualified retirement plan, IRA and government retirement distributions included in adjusted gross income (203(a)(2)(F)); from tax year 2025 IDOR moved certain retirement payments to retired partners to Schedule M line 14 ([Bulletin FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html));
   - Illinois income tax refunds included in adjusted gross income (203(a)(2)(H));
   - Social Security and railroad retirement benefits included in adjusted gross income (203(a)(2)(L));
   - income exempt from Illinois tax by U.S. law, such as U.S. Treasury interest (203(a)(2)(N));
   - the depreciation the taxpayer would have taken without bonus depreciation, on property added back under D-15 (203(a)(2)(Z));
   - medical debt relief included in adjusted gross income (Schedule M line 18, tax years beginning on or after 1 January 2025, [Bulletin FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html)).
4. **Line 9, Illinois base income** = line 1 + additions - subtractions.
5. **Line 10, exemption allowance.** If federal adjusted gross income is over $250,000 (over $500,000 joint), enter zero. Otherwise: number of federal exemptions (taxpayer, spouse on a joint return, each dependent) x $2,925, plus $1,000 for each 65-or-older and each blind box. A person who can be claimed as a dependent by someone else and whose base income exceeds the basic amount gets no basic amount (35 ILCS 5/204(b)).
6. **Line 11, net income** = line 9 - line 10, not below zero.
7. **Line 12, tax** = line 11 x 4.95%.
8. **Nonrefundable credits** (Schedule ICR): property tax credit 5% of real property tax paid in 2026 on the principal residence (the residence share only for multi-unit, mixed-use or farm buildings); K-12 credit 25% of each pupil's tuition, book and lab fees above $250, at most $750 per family; credit for tax paid to other states. Neither the property tax credit nor the K-12 credit is allowed above the $250,000 or $500,000 cut-off, and neither can take the tax below zero.
9. **Refundable credits** (Schedule IL-E/EITC): Illinois EITC 20% of the federal earned income credit; any excess over the tax is refunded (35 ILCS 5/212(b)). From 2023 the Illinois credit is also allowed to workers aged 18 to 24 and 65 or older without a qualifying child, and to ITIN filers, computed as if the federal age and Social Security number rules did not apply (212(b-5), (b-10), (b-15)). Child tax credit: 40% of the Illinois EITC for a filer with a qualifying dependent under 12 (Bulletin FY 2026-15, 2025 Schedule IL-E/EITC line 12).
10. **Payments**: Illinois withholding, pass-through withholding, 2026 estimated payments and any 2025 overpayment applied. The balance is due, or refunded.

### Net losses

For an individual, an Illinois net loss carries forward to each of the 20 taxable years after the loss year for losses in taxable years ending on or after 31 December 2021 (35 ILCS 5/207(a)(4)). The $500,000 annual cap on carryover deductions in 35 ILCS 5/207(d) applies only to a corporation other than an S corporation, not to an individual.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Federal adjusted gross income $250,001 (single) or $500,001 (joint) | Exemption, property tax credit and K-12 credit all zero; the EITC is not affected by the cut-off |
| Federal adjusted gross income exactly $250,000 (single) or $500,000 (joint) | Not over the cut-off: all three are allowed ("exceeds" in 204(g), 208, 201(m)) |
| Bonus depreciation taken federally in 2026 | Add it back (D-15), subtract the depreciation without bonus (Z) in 2026 and later years, reverse on disposal (D-16) |
| Social Security in federal adjusted gross income | Subtract all of it (L) |
| Gambling winnings | Included in base income through adjusted gross income; gambling losses are a federal itemized deduction and so never reduce Illinois base income |
| Dependent of another taxpayer with base income above the basic amount | No basic exemption amount (204(b)) |
| Taxpayer turns 65 during 2026 | $1,000 additional exemption if 65 before the end of the taxable year (204(d)(1)(A)) |
| Individual net loss | Carry forward 20 years; no $500,000 cap (that cap is corporate only) |
| Part-year resident or nonresident | Out of scope: Schedule NR (refuse, R-IL-NR) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Number of federal exemptions | Taxpayer only (one exemption); ask for the federal dependents |
| Age and blindness | No additional $1,000; ask |
| Whether federal adjusted gross income passes the cut-off | Compute both ways if within USD 5,000 of the cut-off; ask for the final federal figure |
| Bonus depreciation on the federal return | Assume none; ask for federal Form 4562 |
| Property tax paid | No credit until the 2026 tax bill paid on the principal residence is seen |
| Federal earned income credit | No Illinois EITC until the federal figure is final |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Adjusted gross income within a few thousand dollars of $250,000 or $500,000 | A deductible federal adjustment (for example a SEP contribution) can restore the exemption and two credits (Case 2) |
| Federal bonus depreciation or section 1202 exclusion | Illinois additions that raise base income |
| Retirement income in adjusted gross income | Usually fully subtracted; check it is not taxed twice |
| No Illinois withholding and tax over $1,000 | Estimated payments were due during 2026 (`il-estimated-tax`) |

## Worked cases

**Case 1, a single freelancer.** A single filer, under 65, has 2026 federal adjusted gross income of $100,000, all Schedule C profit, and no Schedule M items. She paid $6,000 of real property tax on her home.

Base income $100,000. Exemption $2,925 (adjusted gross income is under $250,000). Net income $97,075. Tax 4.95% = $4,805.21. Property tax credit 5% x $6,000 = $300. Tax after credits $4,505.21.

```oa-check
name: Illinois single filer, AGI 100,000 with property tax credit (2026)
inputs:
  agi: 100000
  exemptions: 1
  exemption_amount: 2925
  property_tax: 6000
steps:
  - exemption: exemptions * exemption_amount
  - net_income: max(agi - exemption, 0)
  - tax: round(net_income * 0.0495, 2)
  - property_credit: min(property_tax * 0.05, tax)
  - tax_after_credits: tax - property_credit
expected:
  exemption: 2925.00
  net_income: 97075.00
  tax: 4805.21
  property_credit: 300.00
  tax_after_credits: 4505.21
```

**Case 2, a decision: does a $2,000 deductible contribution that brings adjusted gross income under $500,000 pay off in Illinois?** A married couple filing jointly, both under 65, two dependents (four exemptions), one pupil with $3,250 of private school tuition, $10,000 of property tax on their home. Without the contribution their federal adjusted gross income is $501,000; a $2,000 SEP contribution takes it to $499,000. No Schedule M items.

Without: over $500,000, so no exemption and no property tax or K-12 credit. Tax 4.95% x $501,000 = $24,799.50.

With: exemption 4 x $2,925 = $11,700. Net income $487,300. Tax $24,121.35. Property tax credit $500. K-12 credit 25% x ($3,250 - $250) = $750, which is the $750 maximum. Tax after credits $22,871.35. Illinois tax falls by **$1,928.15**, before any federal saving on the contribution. Recommend the contribution if the couple can fund it; the cut-off is a cliff, so even a small adjustment across it is worth checking.

```oa-check
name: Illinois joint filers either side of the 500,000 cut-off (2026)
inputs:
  agi_without: 501000
  agi_with: 499000
  exemptions: 4
  exemption_amount: 2925
  property_tax: 10000
  tuition: 3250
steps:
  - tax_without: round(agi_without * 0.0495, 2)
  - net_with: agi_with - exemptions * exemption_amount
  - tax_with_before_credits: round(net_with * 0.0495, 2)
  - property_credit: property_tax * 0.05
  - k12_credit: min(max(tuition - 250, 0) * 0.25, 750)
  - tax_with: tax_with_before_credits - property_credit - k12_credit
  - illinois_saving: tax_without - tax_with
expected:
  tax_without: 24799.50
  net_with: 487300.00
  tax_with_before_credits: 24121.35
  k12_credit: 750.00
  tax_with: 22871.35
  illinois_saving: 1928.15
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-IL-NR | Part-year resident or nonresident (Schedule NR) | Refer: allocation of Illinois-source income is outside this skill |
| R-IL-K1 | Partnership or S corporation income with Schedule K-1-P, or a pass-through entity tax credit | Use `il-pprt` for the entity; the individual credit is reviewed by a preparer |
| R-IL-1041 | Trust or estate return (IL-1041) | Refer |
| R-IL-X | Amended return (IL-1040-X) | Refer |
| R-IL-RES | Domicile in doubt (two homes, recent move) | Refer: residency is decided on facts outside this skill |
| R-IL-1299 | Schedule 1299-C business credits (EDGE, REV, MICRO, film, apprenticeship) | Refer: certificate-based credits |

## Filing and payment

File Form IL-1040 with Schedules M, ICR and IL-E/EITC through MyTax Illinois (mytax.illinois.gov) or commercial software. The 2026 return and payment are due **15 April 2027** (35 ILCS 5/505(a)(2)). IDOR grants an automatic six-month extension of time to file: for the 2025 return filed in 2026, IDOR gives an original due date of 15 April 2026 and an extended due date of 15 October 2026 ([Bulletin FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html)). The extension does not extend the time to pay. Estimated payments for 2026 are in `il-estimated-tax`.

## Completion checklist

- Federal adjusted gross income taken from the final federal return, line 11.
- Every addition (other-state bond interest, bonus depreciation, section 1202 exclusion) and subtraction (retirement, Social Security, Treasury interest) traced to a document.
- Cut-off tested against federal adjusted gross income, not base income.
- Exemption at $2,925 per exemption for 2026 (not the 2025 $2,850), plus $1,000 per 65-or-blind box.
- Property tax credit on the principal residence only; K-12 credit per pupil above $250, family cap $750.
- EITC at 20% of the federal credit; child tax credit only with a dependent under 12.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 35 ILCS 5/201 (Illinois General Assembly). Read for (b)(5.4) the 4.95% individual rate and (m) the K-12 credit: 25%, $250, $750, $250,000 and $500,000 cut-offs. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201 | 2026-11-13 |
| 35 ILCS 5/203. Read for (a)(2) additions (A), (B), (D-15), (D-16), (D-26) and subtractions (F), (H), (L), (N), (Z). | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K203 | 2026-11-13 |
| 35 ILCS 5/204. Read for (b) the basic amount and dependent rule, (c) one exemption per federal exemption, (d) $1,000 for 65 or blind, (d-5) cost-of-living adjustment, (g) the $250,000 and $500,000 cut-offs. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204 | 2026-11-13 |
| 35 ILCS 5/207. Read for (a)(4) the 20-year carryforward and (d) the corporate-only $500,000 cap. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K207 | 2026-11-13 |
| 35 ILCS 5/208. Read for the 5% residential property tax credit and its cut-offs. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K208 | 2026-11-13 |
| 35 ILCS 5/212. Read for (a) 20% of the federal credit, (b) refundability, (b-5), (b-10), (b-15). | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K212 | 2026-11-13 |
| 35 ILCS 5/505. Read for (a)(2) the 15th day of the 4th month due date. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K505 | 2026-11-13 |
| IDOR Informational Bulletin FY 2026-15, What's New for Illinois Income Taxes (December 2025). Read for the 2025 exemption $2,850, the 2026 exemption $2,925, the 15 April and 15 October 2026 dates, Schedule M lines 14 and 18, the child tax credit at 40%, and the cut-off reminder. | https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html | 2026-11-13 |
| 2026 Form IL-1040-ES. Read for the worksheet (base income, exemption, 4.95%). | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf | 2026-11-13 |

Illinois sites refused direct connections from this machine; every page above was read through a Firecrawl fetch of the official URL on 2026-11-13.

Not yet confirmed: the child tax credit percentage and its income limits for tax year 2026 (the 40% figure is from the 2025 Schedule IL-E/EITC as described in Bulletin FY 2026-15; the statute section that now holds the credit was not read, and 35 ILCS 5/212.1 is repealed); the 2026 Form IL-1040 line numbers (the 2026 form was not published when read; line numbers above follow the 2025 form described in the bulletin); IDOR's automatic six-month extension for the 2026 return (stated by IDOR for 2025 only); the residency test (domicile and presence for other than a temporary purpose, 35 ILCS 5/1501(a)(20), not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
