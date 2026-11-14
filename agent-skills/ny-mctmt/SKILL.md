---
name: ny-mctmt
description: "New York Metropolitan Commuter Transportation Mobility Tax (MCTMT, Tax Law Article 23) for 2026, for employers and for the self-employed in the 12-county Metropolitan Commuter Transportation District. Employers are subject in a quarter only when payroll expense across both zones is more than $312,500, then pay the zone rate on all of that zone's payroll on Form MTA-305 (Zone 1 0.055%, 0.115%, 0.60% or 0.895%; Zone 2 0.055%, 0.115%, 0.34% or 0.635% for quarters from 1 July 2025). Self-employed individuals and partners pay 0.60% (Zone 1) or 0.34% (Zone 2) on net earnings allocated to a zone once that zone's earnings exceed $150,000 for tax year 2026 ($50,000 for 2025 and earlier), on Form IT-201 or IT-203 with estimates on IT-2105. Trigger on \"MCTMT\", \"MTA payroll tax\", \"MTA-305\", \"metropolitan commuter tax\", \"Zone 1 Zone 2\", \"MCTD\". New York only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ny-mctmt"
  jurisdiction: "US-NY"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# New York MCTMT for employers and the self-employed, tax year 2026

> **Source-cited draft.** Built from the Tax Department's MCTMT employer page, its New York City, Yonkers and MCTMT page, the 2026 instructions for Forms IT-2105 and IT-2658, the 2025 instructions for Form IT-201 and Publication 420, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** The MCTMT is a New York State tax paid to fund the Metropolitan Transportation Authority. It applies only in the Metropolitan Commuter Transportation District (MCTD): Zone 1 is the five New York City counties (New York, Bronx, Kings, Queens, Richmond); Zone 2 is Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess and Westchester.

- **Employers:** subject for a calendar quarter only if they must withhold New York income tax **and** their payroll expense for covered employees across **both zones** is **greater than USD 312,500** in that quarter. The rate for each zone then applies to **all** of that zone's payroll expense. File Form MTA-305 by the last day of the month after the quarter. No extensions.
- **Self-employed (including partners):** for **tax year 2026**, subject in a zone only if net earnings from self-employment allocated to **that zone exceed USD 150,000** (it was USD 50,000 for 2025 and earlier). The tax is **0.60%** of all Zone 1 earnings or **0.34%** of all Zone 2 earnings. It is reported on the personal income tax return and paid through estimated tax on Form IT-2105.

## Scope and who this is for

In scope: the employer MCTMT (who is subject, the quarterly threshold, the zone rates, covered employees, Form MTA-305, excluded employers) and the MCTMT on self-employed individuals and individual partners (the threshold, the rates, allocation to zones, the return lines, estimated payments and the partnership's role). This skill is the one home of the MCTMT figures; `ny-payroll` links here.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| New York withholding, NYS-45, unemployment insurance, PFL, disability benefits | `ny-payroll` |
| The 30% MTA surcharge on corporations under Article 9-A (a different tax) | `ny-corporate-franchise-article-9a` |
| The 0.375% MCTD sales tax (a different tax) | `ny-sales-tax` |
| The full IT-201 resident return | `ny-it-201-resident-return` |
| New York estimated tax for individuals (the income tax part of IT-2105) | `ny-estimated-tax` |
| Federal net earnings from self-employment (Schedule SE) | `us-schedule-c-and-se-computation` |
| Where a remote employee or owner is treated as working for income tax | `us-multi-state-residency-and-allocation` |
| PTET (MCTMT is not part of the PTET base) | `ny-pte-tax-ptet` |
| NYC unincorporated business tax (a separate city tax) | `nyc-ubt` |

## Ask the client first

1. **Employer or self-employed, or both?** An owner of a business with staff can owe both: the employer tax on staff payroll and the self-employed tax on their own earnings.
2. **For an employer, payroll expense by quarter and by zone.** Wages and other compensation for covered employees in Zone 1 and in Zone 2 for each calendar quarter, and whether the employer withholds New York income tax.
3. **What kind of employer?** Federal agency, United Nations, interstate agency, federally chartered credit union, household employer, school or library, or a local government (county, city, town, village, public authority): each changes the answer.
4. **For the self-employed, net earnings from self-employment for 2026 by source** (Schedule SE line 6 for each business, and each partnership's Zone 1 and Zone 2 percentages from Form IT-204-IP), and where each business is carried on: inside Zone 1, inside Zone 2, or partly outside the MCTD.
5. **Married filing jointly?** The threshold is tested for each spouse separately.
6. **Any earnings from a START-UP NY tax-free area?** They are excluded through Form IT-6-SNY.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Employer threshold: payroll expense across both zones in the calendar quarter must be greater than | USD 312,500 | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer, Zone 1, quarters beginning on or after 1 July 2025: Zone 1 payroll expense over USD 0, not over USD 375,000 | 0.055% | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer, Zone 1: over USD 375,000, not over USD 437,500 | 0.115% | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer, Zone 1: over USD 437,500, not over USD 2,500,000 | 0.60% | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer, Zone 1: over USD 2,500,000 (local government employers pay 0.60% instead) | 0.895% | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer, Zone 2, quarters beginning on or after 1 July 2025: Zone 2 payroll expense over USD 0, not over USD 375,000 | 0.055% | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer, Zone 2: over USD 375,000, not over USD 437,500 | 0.115% | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer, Zone 2: over USD 437,500, not over USD 2,500,000 | 0.34% | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer, Zone 2: over USD 2,500,000 | 0.635% | [Tax Department, MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Self-employed threshold, net earnings allocated to one zone, tax year 2026 and after (each zone, each individual) | USD 150,000 | [Tax Department, New York City, Yonkers, and MCTMT](https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm) |
| Self-employed threshold, tax years 2025 and prior | USD 50,000 | [Tax Department, New York City, Yonkers, and MCTMT](https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm) |
| Self-employed rate, Zone 1, on all Zone 1 net earnings once over the threshold | 0.60% | [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Self-employed rate, Zone 2, on all Zone 2 net earnings once over the threshold | 0.34% | [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |

The earlier employer tables, for quarters beginning before 1 July 2025, are in the boundary table below. None of these figures is indexed.

### Employers

1. **Is the employer in the tax at all?** It must be required to withhold New York State income tax from wages. Excluded employers: an agency or instrumentality of the United States (named as such by a federal law or a federal court decision; a private federal contractor is not one); the United Nations; an interstate agency or public corporation created under a compact with another state or Canada; a federally chartered credit union; a household employer, on wages to household employees; an eligible educational institution (public school district, BOCES, public elementary or secondary school, a school serving students with disabilities under Education Law Article 85 or 89, a nonpublic elementary or secondary school with grade one or above, and, from the first quarter of 2016, public library systems and public and free association libraries); and, for quarters beginning on or after 1 July 2025, a local government employer whose covered employees are in Zone 2. A local government employer is a county, city, town, village or other political subdivision, a public improvement or special district, a public authority, commission, community college or public benefit corporation, any other public corporation or unit of government, and the county and sheriff where the sheriff is elected. Source: [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm).
2. **Find covered employees.** A covered employee is one whose services are allocated to the MCTD. For someone working both inside and outside the MCTD, apply the Publication 420 tests in order (localization, then base of operations, then direction and control); once a test allocates the services to the MCTD, all of them are allocated there and no further test is applied. Source: [Publication 420](https://www.tax.ny.gov/pdf/publications/mctmt/pub420.pdf), "Determining if an employee is a covered employee". Publication 420's rate pages are out of date; use only its allocation and payroll-expense rules.
3. **Add up payroll expense for the quarter, by zone.** Payroll expense is wages and compensation for covered employees, including wages subject to federal social security and Medicare and to the railroad retirement tax ([Publication 420](https://www.tax.ny.gov/pdf/publications/mctmt/pub420.pdf)). The zone follows where the covered employee's services are allocated, not where the employer is headquartered.
4. **Apply the quarterly threshold to the MCTD total.** If Zone 1 plus Zone 2 payroll expense is not greater than USD 312,500, the employer owes nothing and files no return for that quarter. Each quarter is tested on its own; there is no annualizing.
5. **Apply each zone's rate to all of that zone's payroll.** Find the Zone 1 payroll in the Zone 1 table and multiply the **whole** Zone 1 payroll by that row's rate; do the same for Zone 2. The schedule is not graduated: one rate covers the whole zone payroll. Add the two. Source: [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm).
6. **File Form MTA-305 and pay** (see "Filing and payment"). MCTMT is an employer tax: it is never withheld from employees, and PFL or other employee deductions do not reduce payroll expense.

### Self-employed individuals and partners

7. **Who.** Sole proprietors (including single-member LLCs disregarded for federal tax), partners in partnerships, members of LLCs treated as partnerships, and partners of LLPs treated as partnerships, with net earnings from self-employment allocated to Zone 1 or Zone 2. A person who takes part in the control, management or operations of a partnership is not treated as a limited partner for the IRC 1402(a)(13) exclusion, whatever the agreement calls them, so their distributive share counts [Tax Law 800(e)]. The partnership itself does not pay MCTMT on partners' shares (it pays estimates for nonresident partners, below). Source: [IT-201-I (2025)](https://www.tax.ny.gov/forms/current-forms/it/it201i.htm), lines 54a to 54e.
8. **Net earnings from self-employment** are generally Schedule SE (Form 1040) Part I line 6 for each source, so the 92.35% factor is already applied. Earnings from employment that IRC 1402 treats as a trade or business (a US citizen employed by a foreign government or an international organization, some church employees, ministers) are included. If the earnings are not subject to federal self-employment tax (for example a nonresident noncitizen), compute them on Schedule SE as if they were. Source: same.
9. **Allocate each source to a zone.** If all the activity of a business is inside a zone, all its net earnings go to that zone. If it is carried on both inside and outside the zone, use Form IT-203-A (business allocation schedule). For a partnership, multiply the partner's net partnership income by the Zone 1 and Zone 2 percentages on Form IT-204-IP, lines 29b and 29c. Add all sources for each zone. Source: same.
10. **Test each zone against the threshold, person by person.** For 2026, a zone counts only if that individual's net earnings allocated to that zone exceed USD 150,000. The test is per zone, not on the MCTD total, and per spouse even on a joint return: a spouse at or under the threshold in a zone is left out of that zone's line. Sources: [New York City, Yonkers, and MCTMT](https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf).
11. **Compute the tax.** 0.60% of the whole Zone 1 amount and 0.34% of the whole Zone 2 amount (IT-201 lines 54a to 54e; IT-203 has matching lines). It is not graduated. No tax credit can be used against the MCTMT, and no exemption in other New York law applies except START-UP NY earnings. Source: [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf). Residence does not matter: a nonresident of New York is taxed on earnings allocated to a zone.
12. **Pay during the year** through Form IT-2105 with the income tax estimates, after subtracting any estimated MCTMT a partnership paid for the partner on Form IT-2658 (see "Filing and payment").

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Employer MCTD payroll exactly USD 312,500 in a quarter | Not subject: the test is "greater than" | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employer with USD 300,000 in Zone 1 and USD 100,000 in Zone 2 | Subject: the USD 312,500 test is on both zones together (USD 400,000). Zone 1 and Zone 2 both at 0.055% | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| One busy quarter, three quiet ones | Only the busy quarter is taxable; there is no annualizing | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Zone 1 payroll of exactly USD 2,500,000 | 0.60% (the 0.895% row starts over USD 2,500,000) | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Local government employer, Zone 1, payroll over USD 2,500,000 | 0.60%, not 0.895% | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Local government employer, Zone 2, quarter beginning on or after 1 July 2025 | Not subject | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Quarter beginning before 1 July 2025 (for example Q1 or Q2 2025) | Zone 1: 0.11% (over 0, not over 375,000), 0.23% (to 437,500), 0.60% (over 437,500). Zone 2: 0.11%, 0.23%, 0.34%. No top tier | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) (tables 1a and 2a) |
| Quarter before July 2023 | Refer: an older single-district schedule applied | [Publication 420](https://www.tax.ny.gov/pdf/publications/mctmt/pub420.pdf) |
| Household employer | Not subject on wages to household employees; an agency placing workers in homes is not a household employer | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Employee works in Albany or New Jersey part of the time | Apply the Publication 420 covered-employee tests; Albany and all places outside New York are outside the MCTD | [Publication 420](https://www.tax.ny.gov/pdf/publications/mctmt/pub420.pdf) |
| Yonkers or White Plains | Westchester County, so Zone 2, not Zone 1 | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Self-employed with USD 140,000 in Zone 1 and USD 140,000 in Zone 2, 2026 | No MCTMT: neither zone exceeds USD 150,000, even though the MCTD total is USD 280,000 | [New York City, Yonkers, and MCTMT](https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm) |
| Self-employed Zone 1 earnings exactly USD 150,000, 2026 | No MCTMT in Zone 1: earnings must exceed the threshold | [New York City, Yonkers, and MCTMT](https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm) |
| Self-employed, 2025 return (filed in 2026) | Threshold USD 50,000 per zone, same rates | [IT-201-I (2025)](https://www.tax.ny.gov/forms/current-forms/it/it201i.htm) |
| Married couple, both self-employed in Zone 1, USD 200,000 and USD 90,000 in 2026 | Only the USD 200,000 spouse is taxed: 0.60% of USD 200,000. The USD 90,000 is left off line 54a | [IT-201-I (2025)](https://www.tax.ny.gov/forms/current-forms/it/it201i.htm) |
| Nonresident of New York working in Manhattan | Subject on net earnings allocated to Zone 1 | [IT-2658-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2658i.pdf) |
| Limited partner who manages the business | Treated as not a limited partner: the distributive share counts [Tax Law 800(e)] | [IT-201-I (2025)](https://www.tax.ny.gov/forms/current-forms/it/it201i.htm) |
| Earnings from a START-UP NY tax-free area | Excluded from the base through Form IT-6-SNY; still counted to see whether the threshold is passed | [IT-201-I (2025)](https://www.tax.ny.gov/forms/current-forms/it/it201i.htm) |
| Rental income, dividends, capital gains | Not net earnings from self-employment, so not in the base | [IT-201-I (2025)](https://www.tax.ny.gov/forms/current-forms/it/it201i.htm) |
| S corporation shareholder | The shareholder's share of S corporation income is not self-employment earnings; wages paid to the shareholder are employer payroll expense | [IT-201-I (2025)](https://www.tax.ny.gov/forms/current-forms/it/it201i.htm); [Publication 420](https://www.tax.ny.gov/pdf/publications/mctmt/pub420.pdf) |
| Tax credits | None can reduce the MCTMT | [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Zone of a work location | Look up the county; if unknown, do not guess the zone |
| Whether an employee is a covered employee | Apply the Publication 420 tests; until then treat the payroll as covered if the employee reports to an MCTD office |
| Partnership's zone percentages | Ask for Form IT-204-IP lines 29b and 29c; do not assume 100% |
| Self-employed earnings split between zones | Ask; use Form IT-203-A when a business is partly outside a zone |
| Tax year of the return | 2026 rules (USD 150,000) only for tax year 2026; 2025 returns use USD 50,000 |

### Red flags

| Flag | Why it matters |
| --- | --- |
| Employer near USD 312,500 a quarter | A small change decides whether a return is due at all |
| Zone payroll just over USD 375,000, USD 437,500 or USD 2,500,000 | The whole zone payroll moves to the next rate |
| Self-employed near USD 150,000 in a zone | One dollar over means tax on the whole amount (0.60% of USD 150,001 is about USD 900) |
| A 2025 computation reused for 2026 | The self-employed threshold rose from USD 50,000 to USD 150,000 |
| Partner with a large Zone 1 share and no IT-2658 payments | Estimated MCTMT may be due by the partner |

## Worked cases

**Case 1, an employer in 2026.** In the first quarter of 2026 a private employer has payroll expense of USD 450,000 for covered employees in Zone 1 and USD 200,000 in Zone 2. The MCTD total is USD 650,000, greater than USD 312,500, so it is subject. Zone 1: USD 450,000 is over USD 437,500 and not over USD 2,500,000, so 0.60% of USD 450,000 = USD 2,700. Zone 2: USD 200,000 is not over USD 375,000, so 0.055% of USD 200,000 = USD 110. Total MCTMT USD 2,810, on Form MTA-305 by 30 April 2026. This is the Tax Department's own example. A private employer with USD 3,000,000 of Zone 1 payroll in a 2026 quarter pays 0.895% on all of it, USD 26,850; a local government employer pays 0.60%, USD 18,000.

```oa-check
name: Employer MCTMT, Zone 1 and Zone 2, quarter in 2026
inputs:
  zone1_payroll: 450000
  zone2_payroll: 200000
  zone1_rate: 0.006
  zone2_rate: 0.00055
steps:
  - mctd_total: zone1_payroll + zone2_payroll
  - zone1_tax: zone1_payroll * zone1_rate
  - zone2_tax: zone2_payroll * zone2_rate
  - total: zone1_tax + zone2_tax
expected:
  mctd_total: 650000
  zone1_tax: 2700.00
  zone2_tax: 110.00
  total: 2810.00
```

**Case 2, a decision: is the self-employed MCTMT due, zone by zone, under the 2026 rule?** A single consultant has 2026 net earnings from self-employment of USD 240,000: USD 180,000 allocated to Zone 1 (a Manhattan office) and USD 60,000 to Zone 2 (work done from a Nassau County office). For 2026, Zone 1 exceeds USD 150,000, so 0.60% x USD 180,000 = USD 1,080. Zone 2 does not exceed USD 150,000, so there is no Zone 2 tax. MCTMT for 2026: USD 1,080. Under the 2025 rule (USD 50,000 per zone) the same earnings would also have been taxed in Zone 2: 0.34% x USD 60,000 = USD 204, total USD 1,284. Decision: report only the Zone 1 amount on the 2026 return and size the 2026 IT-2105 estimates on USD 1,080, not on last year's pattern.

```oa-check
name: Self-employed MCTMT by zone, 2026 threshold against the 2025 threshold
inputs:
  zone1_earnings: 180000
  zone2_earnings: 60000
  threshold_2026: 150000
  threshold_2025: 50000
steps:
  - zone1_over_2026: min(1, ceil(max(zone1_earnings - threshold_2026, 0) / 1000000))
  - zone2_over_2026: min(1, ceil(max(zone2_earnings - threshold_2026, 0) / 1000000))
  - tax_2026: zone1_over_2026 * zone1_earnings * 0.006 + zone2_over_2026 * zone2_earnings * 0.0034
  - zone1_over_2025: min(1, ceil(max(zone1_earnings - threshold_2025, 0) / 1000000))
  - zone2_over_2025: min(1, ceil(max(zone2_earnings - threshold_2025, 0) / 1000000))
  - tax_2025_rules: zone1_over_2025 * zone1_earnings * 0.006 + zone2_over_2025 * zone2_earnings * 0.0034
expected:
  zone1_over_2026: 1
  zone2_over_2026: 0
  tax_2026: 1080.00
  tax_2025_rules: 1284.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-MCT-ALLOC | Covered-employee status of a multi-location or remote employee is contested | Refer: apply Publication 420 with full facts; for income tax residence and day counts use `us-multi-state-residency-and-allocation` |
| R-MCT-OLD | Any quarter before July 2023, or a self-employed year before 2015 | Refer: older schedules and forms (including the former Form MTA-6) applied |
| R-MCT-GOV | Federal instrumentality status, interstate agencies, public authorities | Refer: the exclusion depends on a statute or court decision naming the body |
| R-MCT-PEO | Professional employer organizations and common pay agents | Refer to the Tax Department's PEO and common pay agent pages |
| R-MCT-CARRIER | Interstate rail or motor carrier employees | Refer: federal preemption questions are outside this skill |
| R-MCT-AUDIT | Audits, assessments, Tax Appeals Tribunal | Refer to a New York CPA, EA or attorney |
| R-MCT-CLERGY | Ministers, members of religious orders, church employees | Refer: special Schedule SE rules decide the base |
| R-MCT-TREATY | Nonresident alien claiming a treaty exemption | Refer: no treaty rule is on the pages read |
| R-MCT-SNY | START-UP NY earnings | Refer to Form IT-6-SNY and its instructions |

## Filing and payment

- **Employers, Form MTA-305.** Quarterly: 1 January to 31 March due 30 April; 1 April to 30 June due 31 July; 1 July to 30 September due 31 October; 1 October to 31 December due 31 January. A due date on a Saturday, Sunday or legal holiday moves to the next business day. No extensions of time to file or pay. An employer not subject for a quarter files nothing for it; one that made MCTMT payments in the quarter, or has an overpayment carried from an earlier quarter, must file to claim a refund or a credit to the next quarter. File and pay through Online Services (Web File MTA-305, or the MCTMT upload), on paper Form MTA-305 with a check or money order, or through PrompTax: employers required to use PrompTax for withholding must pay MCTMT through PrompTax. MTA-305 is a separate return, not a part of Form NYS-45. Source: [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm).
- **Self-employed, annual return.** Report on Form IT-201 lines 54a to 54e (IT-203 has the matching lines), due 15 April 2027 for tax year 2026. Source: [IT-201-I (2025)](https://www.tax.ny.gov/forms/current-forms/it/it201i.htm).
- **Self-employed, estimated tax.** Pay with Form IT-2105 (or online) together with New York State, New York City and Yonkers estimates, if any MCTMT is expected after subtracting estimated MCTMT paid by a partnership. For 2026: 15 April, 15 June, 15 September 2026 and 15 January 2027. No penalty if the total of New York State, New York City, Yonkers and MCTMT paid on time is at least 90% of the 2026 tax, or 100% of the 2025 tax (110% if the 2025 New York AGI, or net earnings allocated to the MCTD, was more than USD 150,000, or USD 75,000 if married filing separately for 2026), or 90% of the annualized tax. Source: [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf).
- **Partnerships with nonresident partners.** The partnership pays estimated tax, including estimated MCTMT, for nonresident individual partners on Form IT-2658 at 0.60% (Zone 1) and 0.34% (Zone 2) of the partner's estimated allocated net earnings; due 15 April, 15 June, 15 September 2026 and 15 January 2027. Source: [IT-2658-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2658i.pdf).
- **Penalties and interest.** Late filing and late payment follow the Tax Law penalty rules; use the Tax Department's penalty and interest calculator rather than a rate in this skill.

## Completion checklist

- Employer: withholding requirement confirmed, excluded-employer list checked, covered employees found with the Publication 420 tests.
- Employer: MCTD total tested against USD 312,500 for each quarter separately.
- Employer: the right table used for the quarter's start date (before, or on or after, 1 July 2025), and one rate applied to all of each zone's payroll.
- Employer: MTA-305 filed by the quarterly due date, or no return for a quarter not subject (unless claiming a refund).
- Self-employed: Schedule SE line 6 per source, allocated with IT-203-A or IT-204-IP.
- Self-employed: each zone tested against USD 150,000 (2026) per individual, not on the MCTD total.
- Self-employed: 0.60% and 0.34% applied to the whole zone amount; no credits taken against it.
- IT-2105 estimates sized with the MCTMT included; partnership IT-2658 payments subtracted.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Tax Department, Employers: MCTMT (updated 2 July 2026). Read for the USD 312,500 test across both zones, tables 1a, 1b, 2a and 2b, the local government rules, the excluded employers, the Tax Department example (USD 2,810), due dates and how to file. | https://www.tax.ny.gov/bus/mctmt/emp.htm | 2026-11-13 |
| Tax Department, MCTMT landing page (updated 2 July 2026). Read for the zone counties and the employer, PEO, common pay agent and self-employed pages. | https://www.tax.ny.gov/bus/mctmt/ | 2026-11-13 |
| Tax Department, New York City, Yonkers, and MCTMT (updated 30 June 2026). Read for the self-employed threshold: USD 50,000 for 2025 and prior, USD 150,000 for 2026 and after, per zone and per individual. | https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm | 2026-11-13 |
| Instructions for Form IT-2105 (2026). Read for the self-employed rates (0.60% Zone 1, 0.34% Zone 2) above USD 150,000, who must pay estimates, no credits against MCTMT, and the safe harbours. | https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf | 2026-11-13 |
| Instructions for Form IT-2658 (2026). Read for the estimated MCTMT worksheets (0.60%, 0.34%), 2026 due dates and Tax Law 800(e). | https://www.tax.ny.gov/pdf/current_forms/it/it2658i.pdf | 2026-11-13 |
| Instructions for Form IT-201 (2025). Read for lines 54a to 54e: who is self-employed, net earnings from self-employment, zone allocation, IT-204-IP lines 29b and 29c, joint filers and START-UP NY. | https://www.tax.ny.gov/forms/current-forms/it/it201i.htm | 2026-11-13 |
| Publication 420, Guide to the MCTMT. Read for "Determining if an employee is a covered employee" and payroll expense only; its rate pages are out of date. | https://www.tax.ny.gov/pdf/publications/mctmt/pub420.pdf | 2026-11-13 |

Not yet confirmed: the 2026 instructions for Forms IT-201 and IT-203 were not yet published when read, so the line numbers (54a to 54e) are taken from the 2025 form (2025-2026 filing cycle); the MCTMT penalty rates are not quoted because no MCTMT page read today prints them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ny-mctmt` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ny-mctmt. If neither is available, confirm every figure against the official source pages cited above before relying on it.
