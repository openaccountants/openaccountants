---
name: ca-form-3853-coverage
description: California's individual health coverage mandate and the Individual Shared Responsibility Penalty on form FTB 3853 for California residents, tax year 2026 returns. Month by month test of minimum essential coverage for each household member, the exemption codes A to N (short coverage gap of 3 months or less, unaffordable coverage, income below the filing threshold, health care sharing ministry, part-year resident and others), the penalty as the larger of a flat dollar amount ($950 per adult, $475 per child, capped at $2,850 in 2025) or 2.5% of household income over the filing threshold, capped at the state average bronze premium, and where it lands on Form 540 line 92. Uses the 2025 FTB 3853 amounts for the 2025-2026 filing cycle until the 2026 instructions are published. Trigger on "California health insurance penalty", "FTB 3853", "California individual mandate", "Covered California penalty", "no health insurance California tax", "line 92".
version: "1.0"
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# California health coverage mandate and form FTB 3853

> **Source-cited draft.** Built from the 2025 Instructions for form FTB 3853 (revised 03-26), the 2025 Form 540 and R&TC 61015, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Every California resident, and each spouse and dependent, must have minimum essential coverage (MEC) for each month or an exemption for that month. A month with neither carries a penalty, paid with the return on Form 540 line 92. The annual penalty for a household uncovered all year is the **larger** of a flat amount ($950 per adult and $475 per child under 18, capped at $2,850) or **2.5%** of household income above the filing threshold, but never more than the state average bronze premium ($377 per person per month, $4,524 a year for one person). Those are the **2025** amounts; the FTB had not published the 2026 instructions on 2026-11-13, and the 2026 amounts are indexed. Coverage on any one day of a month counts for the whole month.

## Scope and who this is for

In scope: residents and part-year residents filing Form 540 or 540NR for 2026 who cannot tick the full-year coverage box. Out of scope: the federal premium tax credit and Form 8962 (`us-federal-return-assembly`), employer reporting duties on Forms 1094 and 1095 (employers; see the FTB 3853 instructions), and the rest of the return (`ca-540-individual-return`). Penalty figures are owned here; the tax figures are in `ca-income-tax`.

## Ask the client first

1. **For each household member and each month of 2026, what coverage did they have** (employer plan, Covered California, Medi-Cal, Medicare Part A, TRICARE, VA, a student plan)? Get Forms 1095-A, 1095-B or 1095-C.
2. **Any month with no coverage: why?** Cost (affordability), a short gap, being abroad, living in another state, a health care sharing ministry, incarceration, a birth or death in the household, a Marketplace hardship or religious exemption with an exemption certificate number (ECN).
3. **Household income** (MAGI of everyone required to file) and gross income, filing status, ages and number of dependents: the filing threshold and the 2.5% test.
4. **Who in the household was 18 or older in each month** (an individual turning 18 on the first of a month counts as 18 for that month).
5. **Was Covered California coverage paid with advance premium tax credit?** Form 8962 federally, and 1095-A months here.

## The method, step by step

1. **Build the month grid.** For each person, mark each month Z (coverage), an exemption code, or X (no coverage and no exemption). Coverage for at least 1 day in a month counts as coverage for that month.
2. **Full year covered for everyone?** Tick the Form 540 line 92 box and stop; form FTB 3853 is not filed.
3. **Income below the filing threshold?** If applicable household income or gross income is below the filing threshold, check the box in Part II: no penalty for anyone, but form FTB 3853 is still filed.
4. **Claim exemptions** in Part III using the codes in the table below (Marketplace exemptions need the ECN in Part I).
5. **Compute the penalty** on the FTB 3853 worksheets for the X months only:
   - flat dollar amount: $950 for each person 18 or older and $475 for each person under 18, capped at $2,850 (Worksheet A when months differ, or when someone turned 18);
   - percentage amount: (applicable household income less the filing threshold) times 2.5%, rounded;
   - take the larger of the two;
   - cap at the state average bronze premium for the household size ($377 per person per month; $4,524 for one person for the year);
   - for part of a year, each monthly penalty is one-twelfth of these amounts.
6. **Report** the result on Form 540 line 92 (Form 540NR line 91). It is netted against payments on lines 95 and 96.

### Rates, bands and thresholds

| Item | Figure (2025-2026 filing cycle) | Conditions | Source |
| --- | --- | --- | --- |
| Flat amount per adult | $950 | Each person at least 18; Step 2 line 1 | [2025 FTB 3853 instructions](https://www.ftb.ca.gov/forms/2025/2025-3853-instructions.pdf) |
| Flat amount per child | $475 | Each person under 18; Step 2 line 2 | same |
| Flat amount cap | $2,850 | Step 2 line 4 (300% of the adult amount, R&TC 61015(b)(1)(B)) | same; [R&TC 61015](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=61015) |
| Percentage amount | 2.5% of applicable household income over the filing threshold | Step 4 line 5 | same |
| Bronze premium cap | $377 per individual per month; $4,524 (1 person), $9,048 (2), $13,572 (3), $18,096 (4), $22,620 (5 or more) for the year | Step 5 | [2025 FTB 3853 instructions](https://www.ftb.ca.gov/forms/2025/2025-3853-instructions.pdf) |
| Affordability exemption | Required contribution more than 7.28% of household income | Codes A and B | same |
| Short coverage gap | 3 continuous months or less; only the first gap in the year | Code C | same |
| Filing threshold, single or head of household under 65, no dependents | Gross income $22,941; California AGI $18,353 | Do I Have to File chart | same |
| Filing threshold, joint, both under 65, 2 or more dependents | Gross income $73,595 | same | same |
| Statutory base | Applicable dollar amount of $695, indexed after 2019; children half | R&TC 61015(c) and (d) | [R&TC 61015](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=61015) |

## Boundary and exception table

| Code | Exemption | Granted by | Source |
| --- | --- | --- | --- |
| (none, Part II) | Applicable household income or gross income below the filing threshold | Tax return | [2025 FTB 3853 instructions](https://www.ftb.ca.gov/forms/2025/2025-3853-instructions.pdf) |
| A | Coverage unaffordable: required contribution more than 7.28% of household income | Tax return | same |
| B | Aggregate self-only employer coverage unaffordable (more than 7.28%) | Tax return | same |
| C | Short coverage gap of 3 continuous months or less (first gap only) | Tax return | same |
| D | Citizens living abroad (330 full days in 12 months, or bona fide foreign residence), bona fide residents of a US territory, individuals not lawfully present | Tax return | same |
| E | Non-resident or part-year resident: a bona fide resident of another state for that month | Tax return | same |
| F | Member of a health care sharing ministry | Tax return | same |
| G | Members of Indian tribes or eligible for Indian Health Service | Tax return | same |
| H | Incarceration after disposition of charges | Tax return | same |
| I | Months up to and including the month a person joined the household by birth or adoption | Tax return | same |
| J | Months after the month a household member died | Tax return | same |
| K | General hardship | Marketplace (ECN) | same |
| L | Recognized religious sect | Marketplace (ECN) | same |
| M | Unaffordable based on projected income | Marketplace (ECN) | same |
| N | Limited or restricted-scope Medi-Cal, or Share-of-Cost Medi-Cal while the share of cost was not met | Tax return | same |

| Situation | Treatment |
| --- | --- |
| Gap of exactly 3 months (January to March) | Exempt under code C for all 3 months |
| Gap of 4 months (January to April) | Not exempt for any of the 4 months |
| Two gaps (February and March, then October and November) | Only February and March are exempt; October and November are penalty months |
| Coverage ended April 5 and resumed July 25 | April and July count as covered (at least 1 day); May and June are the gap, 2 months, code C |
| Health care sharing ministry only | Not MEC, but exemption F applies for those months |
| Short-term or dental-only plan | Not MEC; test the month for another exemption |
| Medi-Cal for part of the year | Full-scope Medi-Cal is MEC; limited-scope or unmet share-of-cost months take code N |
| High income, no coverage | The 2.5% amount usually exceeds the flat amount; the bronze cap is the ceiling |
| 1095 form not received | Report from the client's own records; do not delay filing |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Ticking the full-year box without 1095 forms for every person | A wrong tick hides a penalty and invites an FTB notice |
| A dependent claimed by someone else | Only the person who claims the dependent reports the dependent's months |
| Turning 18 during the year | Moves the person from $475 to $950 from that month (Worksheet A) |

## Worked cases

### Case 1: single filer, no coverage all year

A single filer under 65 with no dependents had no coverage and no exemption for any month. Applicable household income is $80,000; the filing threshold is $22,941. Flat amount $950. Percentage amount: ($80,000 less $22,941) times 2.5% = $1,426 (rounded). The larger is $1,426, below the $4,524 bronze cap. Penalty $1,426 on Form 540 line 92 (2025 amounts, pending the 2026 instructions).

```oa-check
name: CA FTB 3853 single uncovered all year (2025 amounts)
inputs:
  income: 80000
  threshold: 22941
  adults: 1
  children: 0
  bronze_year: 4524
steps:
  - flat: min(adults * 950 + children * 475, 2850)
  - pct: round((income - threshold) * 0.025, 0)
  - larger: max(flat, pct)
  - penalty: min(larger, bronze_year)
expected:
  flat: 950
  pct: 1426
  larger: 1426
  penalty: 1426
```

### Case 2: family of four, uncovered 6 months, and whether a short gap would have helped (decision)

A married couple filing jointly with two children under 18 had no coverage for July to December (6 months, more than 3, so no code C). Household income is $150,000; the filing threshold for a joint return with 2 or more dependents is $73,595. Annual flat amount: 2 x $950 + 2 x $475 = $2,850, at the cap. Annual percentage amount: ($150,000 less $73,595) x 2.5% = $1,910. The larger is $2,850; for 6 months it is $1,425, against a bronze cap of $377 x 4 people x 6 months = $9,048. Penalty $1,425. Had they enrolled from October, the gap would have been July to September, 3 months, all exempt under code C: penalty nil.

```oa-check
name: CA FTB 3853 family of four, 6 uncovered months against a 3-month gap (2025 amounts)
inputs:
  income: 150000
  threshold: 73595
  adults: 2
  children: 2
  months: 6
  people: 4
steps:
  - flat: min(adults * 950 + children * 475, 2850)
  - pct: round((income - threshold) * 0.025, 0)
  - annual: max(flat, pct)
  - part_year: annual * months / 12
  - bronze_cap: 377 * people * months
  - penalty: min(part_year, bronze_cap)
  - penalty_if_3_month_gap: 0
  - saving: penalty - penalty_if_3_month_gap
expected:
  flat: 2850
  pct: 1910
  annual: 2850
  part_year: 1425
  bronze_cap: 9048
  penalty: 1425
  saving: 1425
```

## When to refuse or refer

- Refer any household where the affordability test needs the employer's offer details (Form 1095-C lines 14 and 16) and the answer is close to 7.28%.
- Refer Marketplace exemption claims (K, L, M) without an ECN; the client must apply to Covered California.
- Refer part-year residents where the residency date itself is in doubt (`ca-residency-leaving-california`).
- Do not state a 2026 penalty amount as final until the 2026 FTB 3853 instructions are published.

## Filing and payment

| Step | Where | Source |
| --- | --- | --- |
| Full-year coverage | Tick the box on Form 540 line 92; no FTB 3853 | [2025 Form 540](https://www.ftb.ca.gov/forms/2025/2025-540.pdf) |
| Any month not covered | Attach form FTB 3853 (Parts I to III and the worksheets) | [2025 FTB 3853 instructions](https://www.ftb.ca.gov/forms/2025/2025-3853-instructions.pdf) |
| Penalty | Form 540 line 92 (540NR line 91; 540 2EZ line 27); netted on lines 95 and 96 of Form 540 | same |
| Due | With the 2026 return, April 15, 2027 | `ca-540-individual-return` |

## Completion checklist

- [ ] Month grid built for every household member from 1095 forms or records.
- [ ] Filing-threshold exemption tested first (Part II).
- [ ] Each uncovered month tested for codes A to N; only the first short gap used.
- [ ] Flat amount, percentage amount and bronze cap computed; part-year months prorated.
- [ ] Line 92 box or penalty entered; FTB 3853 attached when any month is uncovered.
- [ ] Every 2025 amount flagged for replacement once the 2026 instructions are out.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2025 Instructions for form FTB 3853 (REV 03-26). Read for the exemption chart (codes A to N, 7.28%), the short gap rules, Step 2 ($950, $475, $2,850), Step 4 (2.5%), Step 5 ($377 and the household caps), the penalty worksheet and the Do I Have to File chart. | https://www.ftb.ca.gov/forms/2025/2025-3853-instructions.pdf | 2026-11-13 |
| 2025 Form 540. Read for lines 92, 95 and 96. | https://www.ftb.ca.gov/forms/2025/2025-540.pdf | 2026-11-13 |
| R&TC 61015 (California Legislative Information, through Firecrawl). Read for (a) the lesser-of rule and bronze premium, (b) the greater-of rule and 2.5%, (c) $695 and the half rate for children, (d) indexing. | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=61015 | 2026-11-13 |

Not yet confirmed: every 2026 amount (flat amount, cap, bronze premium, affordability percentage and filing thresholds); the 2026 FTB 3853 instructions were not published on 2026-11-13, so the 2025 amounts are shown for the 2025-2026 filing cycle.
