---
name: sweden-payroll
description: Use this skill whenever asked about Swedish payroll processing, employee salary calculations, preliminärskatt (preliminary income tax / PAYE), arbetsgivaravgifter (employer social contributions), employer cost calculations, net-to-gross or gross-to-net conversions, Swedish payslip structure, arbetsgivardeklaration filings, or any question about computing wages, deductions, or employer obligations in Sweden. Trigger on phrases like "Swedish payroll", "preliminärskatt", "arbetsgivaravgifter", "employer contributions Sweden", "PAYE Sweden", "net salary Sweden", "lönespecifikation", "kommunalskatt", "municipal tax Sweden", "statlig inkomstskatt", "Skatteverket filing", "kollektivavtal", "ITP pension", or "semesterersättning".
version: 1.0
jurisdiction: SE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden Payroll

## Sweden Payroll Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Sweden (Kingdom of Sweden) |
| Currency | SEK (Swedish Krona) |
| Payroll frequency | Monthly (typically paid 25th of month) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Socialavgiftslagen (2000:980); Inkomstskattelagen (1999:1229); Skatteförfarandelagen (2011:1244) |
| Tax authority | Skatteverket (Swedish Tax Agency) |
| Employee SS rate | 0% (no separate employee social security contribution) |
| Employer SS rate | 31.42% of gross salary (arbetsgivaravgifter) |
| Income tax | Municipal ~32.38% average + State 20% above SEK 643,100/year |
| Minimum wage | No statutory minimum -- set by collective agreements (kollektivavtal) |
| Filing | Monthly arbetsgivardeklaration by 12th of following month |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (Preliminärskatt)

### Tax Components

**Tax Components**

| Component | Rate (2026) | Applies to |
| --- | --- | --- |
| Municipal tax (kommunalskatt) | ~28.93% -- 35.65% (average 32.38%) | All taxable income |
| State income tax (statlig inkomstskatt) | 20% | Annual income above SEK 643,100 |
| Church tax (kyrkoavgift) | ~1% -- 1.5% | Members of Swedish Church only |
| Funeral fee (begravningsavgift) | ~0.25% | All taxpayers |

### How Withholding Works

Swedish employers withhold preliminary income tax (preliminärskatt/PAYE) based on tax tables issued annually by Skatteverket. Each employee has a tax table determined by:

**Withholding factors**

| Factor | Detail |
| --- | --- |
| Municipality of residence | Determines kommunalskatt rate |
| Table type (kolumn) | Column in table based on deductions (standard: column 1) |
| Special income tax for non-residents (SINK) | Flat 22.5% (from 1 January 2026, reduced from 25%) |
| A-skatt vs F-skatt | A = employee withholding; F = self-employed (no withholding by payer) |

### Key Tax Deductions (Reducing Taxable Income)

**Key Tax Deductions**

| Deduction | Amount (2026) |
| --- | --- |
| Basic deduction (grundavdrag) | SEK 15,400 -- 40,000 (income-dependent) |
| Job tax credit (jobbskatteavdrag) | Automatic, income-dependent (max ~SEK 36,000/year) |
| Pension contributions (employee voluntary) | Deductible up to limits |
| Interest on debt | 30% tax reduction on interest paid |

### Withholding Mechanism

- Employer downloads/applies Skatteverket tax tables monthly
- Tax tables already incorporate grundavdrag and jobbskatteavdrag
- No separate calculation needed -- look up gross monthly salary in table
- Employees can apply for adjusted tax (jämkning) if deductions warrant lower withholding
- Non-table tax (särskild beräkningsgrund) possible for specific situations

### Effective Tax Rates (Approximate, 2026)

**Effective Tax Rates**

| Monthly Gross (SEK) | Effective Tax Rate (incl. jobbskatteavdrag) |
| --- | --- |
| 25,000 | ~22% |
| 35,000 | ~26% |
| 50,000 | ~31% |
| 75,000 | ~37% |
| 100,000 | ~42% |

## Section 3 -- Social Security: Employee Deductions

**Employee social security contributions**

| Contribution | Rate |
| --- | --- |
| Employee social security contributions | **0%** |

Sweden is unique: employees pay NO separate social security contributions. All social insurance funding comes from employer contributions (arbetsgivaravgifter) and general taxation. The income tax employees pay covers both income tax and indirectly funds the welfare system.

### Employee Pension Contributions (Voluntary)

**Employee Pension Contributions**

| Type | Detail |
| --- | --- |
| Tjänstepension (occupational pension) | Employer-paid via collective agreement (ITP/SAF-LO) |
| Private pension savings | Employee's own choice; tax-deductible within limits |
| Mandatory public pension (allmän pension) | Funded through employer's ålderspensionsavgift (10.21%) |

## Section 4 -- Social Security: Employer Contributions (Arbetsgivaravgifter)

### Full Rate Breakdown (2026)

**Full Rate Breakdown**

| Component | Rate |
| --- | --- |
| Ålderspensionsavgift (old-age pension) | 10.21% |
| Sjukförsäkringsavgift (sickness insurance) | 3.55% |
| Föräldraförsäkringsavgift (parental insurance) | 2.60% |
| Efterlevandepensionsavgift (survivors' pension) | 0.60% |
| Arbetsmarknadsavgift (labour market/unemployment) | 2.64% |
| Arbetsskadeavgift (occupational injury) | 0.20% |
| Allmän löneavgift (general payroll tax) | 12.62% |
| **Total arbetsgivaravgifter** | **31.42%** |

### Reduced Rates

**Reduced Rates**

| Category | Rate | Condition |
| --- | --- | --- |
| Employees aged 67+ at year start | 10.21% | Only ålderspensionsavgift |
| Born 1937 or earlier | 0% | No contributions at all |
| Youth (19-23) from 1 April 2026 | 20.81% | On salary up to SEK 25,000/month; full 31.42% above |
| R&D reduction | 10.21% | On portion of salary for qualifying R&D work (max 450,000 SEK/month per company) |

### Youth Discount (Temporary: 1 April 2026 -- 30 September 2027)

**Youth Discount**

| Parameter | Detail |
| --- | --- |
| Eligible employees | Born 2003-2007 (aged 19-23 during 2026) |
| Reduced rate | 20.81% (ålderspensionsavgift + 50% of remaining) |
| Cap | SEK 25,000/month gross; full 31.42% on excess |
| Duration | 1 April 2026 -- 30 September 2027 |

### Special Payroll Tax on Pension Costs (SLP)

**SLP Parameters**

| Parameter | Detail |
| --- | --- |
| Rate | 24.26% |
| Applies to | Employer pension contributions (ITP, SAF-LO, other occupational pension) |
| Paid by | Employer |
| Filing | Reported in arbetsgivardeklaration |

### No Salary Cap

Unlike many countries, Swedish arbetsgivaravgifter apply to the FULL gross salary with NO upper ceiling. There is no equivalent of a social security wage base.

## Section 5 -- Minimum Wage and Overtime

### Minimum Wage

Sweden has NO statutory minimum wage. Pay floors are set entirely by:

**Minimum Wage Sources**

| Source | Coverage |
| --- | --- |
| Collective agreements (kollektivavtal) | ~90% of workforce |
| Sector-specific negotiations | Between trade unions and employer associations |
| ~700 different agreements | Different rates by sector, role, age, experience |

### Indicative Sector Minimums (2026)

**Indicative Sector Minimums**

| Sector | Approximate Monthly Minimum (SEK) |
| --- | --- |
| Hotel and restaurant (HRF) | 25,000 -- 26,000 |
| Retail (Handels) | 25,000 -- 26,000 |
| Warehousing/logistics | 28,000 -- 29,000 |
| Manufacturing (IF Metall) | 27,000 -- 29,000 |
| Construction (Byggnads) | 30,000 -- 33,000 |
| IT (Unionen/IT-avtalet) | No fixed minimum (individual negotiation) |

### Work Permit Salary Threshold (2026)

- **Work permit salary threshold** — From June 2026: SEK 33,390/month minimum for work permit holders (increased from prior threshold). SEK/month

### Working Hours and Overtime

**Working Hours and Overtime**

| Parameter | Standard |
| --- | --- |
| Standard working week | 40 hours |
| Maximum including overtime | 48 hours average per 4-week period |
| Overtime limit | 200 hours/year (extendable to 300 via collective agreement) |
| Overtime compensation | Typically 50-100% supplement (set by kollektivavtal) |
| Unsocial hours (OB-tillägg) | Supplements for evening/night/weekend (kollektivavtal-dependent) |

## Section 6 -- Mandatory Benefits

**Mandatory Benefits**

| Benefit | Detail |
| --- | --- |
| Annual leave (semester) | 25 days minimum per year (Semesterlagen) |
| Holiday pay (semesterlön) | 12% of annual earnings for non-salaried; regular pay + supplement for salaried |
| Sick pay (sjuklön) | Day 1: waiting day (karensdag, no pay); Days 2-14: 80% from employer; Day 15+: Försäkringskassan |
| Parental leave | 480 days shared between parents (Försäkringskassan pays ~80% up to ceiling) |
| Occupational pension (tjänstepension) | Via collective agreement: ITP (white-collar) or SAF-LO (blue-collar) |
| Life/disability insurance (TGL/TFA) | Typically via collective agreement |
| Unemployment insurance (A-kassa) | Voluntary union-based system; employer pays arbetsmarknadsavgift |

### Occupational Pension (Tjänstepension)

**Occupational Pension Plans**

| Plan | Applies to | Contribution |
| --- | --- | --- |
| ITP 1 (defined contribution) | White-collar (Unionen, Ledarna, etc.) born 1979+ | 4.5% on salary up to ~SEK 52,000/month; 30% above |
| ITP 2 (defined benefit) | White-collar born before 1979 | ~10-30% of salary depending on age |
| SAF-LO (Avtalspension) | Blue-collar (IF Metall, Handels, etc.) | 4.5% up to ceiling + 30% above |

### Holiday Pay (Semesterersättning)

**Holiday Pay Methods**

| Method | Calculation |
| --- | --- |
| Salaried employee (sammanfallande) | Regular monthly salary during vacation + semestertillägg (0.8% per day × annual salary / 12) |
| Hourly/non-salaried | 12% of total earnings during qualifying year |
| Unused vacation payout | 12% calculation or equivalent daily rate |

## Section 7 -- Payslip Requirements

Swedish employers should provide a lönespecifikation (payslip) for each salary payment. While not as strictly mandated by statute as in some countries, it is standard practice and often required by collective agreement.

**Payslip Requirements**

| Element | Standard Practice |
| --- | --- |
| Employer identification | Yes |
| Employee name and personnummer | Yes |
| Pay period | Yes |
| Gross salary (grundlön) | Yes |
| Overtime pay (övertidsersättning) | Yes (if applicable) |
| OB-tillägg (unsocial hours) | Yes (if applicable) |
| Holiday pay / supplement | Yes (when applicable) |
| Taxable benefits (förmånsvärde) -- company car, etc. | Yes |
| Preliminary tax withheld (preliminärskatt) | Yes |
| Net salary (nettolön) | Yes |
| Employer contributions (arbetsgivaravgifter) | Often shown for transparency |
| Pension contributions (tjänstepension) | Often shown |
| Accumulated year-to-date figures | Common |
| Vacation days balance | Common |

### Annual Tax Statement

**Annual Tax Statement**

| Document | Deadline |
| --- | --- |
| Kontrolluppgift (KU10/KU13/KU14) | 31 January of following year (submitted to Skatteverket) |
| Employee receives copy | February (for personal tax declaration) |

## Section 8 -- Filing Obligations

**Filing Obligations**

| Filing | Frequency | Deadline | Authority |
| --- | --- | --- | --- |
| Arbetsgivardeklaration (employer PAYE return) | Monthly | 12th of following month (17th for January and August) | Skatteverket |
| Arbetsgivardeklaration -- individuppgift | Monthly | Same as above (per-employee details) | Skatteverket |
| Payment of tax + contributions | Monthly | Same day as declaration deadline (12th/17th) | Skatteverket |
| Kontrolluppgift (annual income statement) | Annual | 31 January following year | Skatteverket |
| Inkomstdeklaration 2 (corporate tax return) | Annual | 1 July (for calendar-year companies) | Skatteverket |

### Arbetsgivardeklaration Details

**Arbetsgivardeklaration Details**

| Parameter | Detail |
| --- | --- |
| Content | Per-employee: gross salary, benefits, preliminary tax withheld; aggregated: total arbetsgivaravgifter |
| Submission | Electronic via Skatteverket portal, file upload, or API (AGI) |
| Individuppgift | Mandatory per-employee reporting since 2019 |
| Penalties | Late filing: SEK 625/month (up to SEK 6,250); incorrect: revision + possible tax surcharge |
| Payment | Paid to Skatteverket tax account (skattekonto) by declaration deadline |

### Key Annual Calendar

**Key Annual Calendar**

| Month | Obligation |
| --- | --- |
| January | Arbetsgivardeklaration for December (deadline 17th); Kontrolluppgift deadline 31st |
| February | Employees receive income statements for personal tax filing |
| March-May | Employee personal tax declarations (1 March -- 2 May) |
| June | Holiday pay processing (semesterlön for summer holidays) |
| August | Arbetsgivardeklaration deadline 17th (extended) |
| December | Year-end adjustments; final December payroll |

## Section 9 -- Common Payroll Patterns

### Pattern 1: Standard Monthly Salary (Municipal Tax 32.38%, No State Tax)

```
Gross monthly salary:                SEK 38,000
- Preliminary tax (~26%):           -SEK  ~9,900
= Net salary:                        SEK ~28,100

Employer cost:
  Gross salary:                      SEK 38,000
+ Arbetsgivaravgifter (31.42%):    +SEK  11,940
+ Tjänstepension ITP1 (4.5%):     +SEK   1,710
+ SLP on pension (24.26%):         +SEK     415
= Total employer cost:               SEK ~52,065
```

### Pattern 2: High-Income Employee (State Tax Applies)

```
Gross monthly salary:                SEK 75,000
Annual: SEK 900,000 (exceeds SEK 643,100 threshold)
- Preliminary tax (~37%):           -SEK  ~27,750
= Net salary:                        SEK ~47,250

Employer cost:
  Gross salary:                      SEK  75,000
+ Arbetsgivaravgifter (31.42%):    +SEK  23,565
+ ITP1: 4.5% up to 52,262 + 30% above: +SEK ~9,173
+ SLP 24.26% on pension:           +SEK   2,225
= Total employer cost:               SEK ~109,963
```

### Pattern 3: Young Employee (Age 19-23, from April 2026)

```
Gross monthly salary:                SEK 25,000
- Preliminary tax (~22%):           -SEK   5,500
= Net salary:                        SEK  19,500

Employer cost:
  Gross salary:                      SEK 25,000
+ Arbetsgivaravgifter (20.81%):    +SEK   5,203 (reduced rate)
+ Pension (SAF-LO 4.5%):          +SEK   1,125
+ SLP on pension (24.26%):         +SEK     273
= Total employer cost:               SEK ~31,601
```

### Pattern 4: Employee Aged 67+

```
Gross monthly salary:                SEK 45,000
- Preliminary tax:                  -SEK  ~12,000
= Net salary:                        SEK  ~33,000

Employer cost:
  Gross salary:                      SEK 45,000
+ Arbetsgivaravgifter (10.21%):    +SEK   4,595 (only ålderspensionsavgift)
= Total employer cost:               SEK ~49,595
```

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Skill | Interaction |
| --- | --- |
| sweden-bookkeeping | Payroll journal entries (7xxx accounts), employer contribution accruals, holiday pay liability |
| payroll-workflow-base | General payroll processing workflow; Sweden-specific overrides in this skill |

### Sweden-Specific Payroll Considerations

- **No employee SS contributions**: All social insurance is funded by employer. Employees only pay income tax.
- **No statutory minimum wage**: Always check applicable kollektivavtal. Non-covered employers set wages individually but risk industrial action.
- **Collective agreement is king**: ITP/SAF-LO pension, TGL insurance, overtime rates, and many benefits are determined by the applicable collective agreement, not by statute.
- **Tax tables**: Employers must apply correct kommun-based table. Employees moving between municipalities may have different rates mid-year.
- **Förmånsvärde (taxable benefits)**: Company cars, housing, meals, etc. have standardised taxable values set by Skatteverket. These are added to gross salary for tax purposes AND subject to arbetsgivaravgifter.
- **Karensdag (qualifying day)**: First sick day is unpaid (since 2019, previously first day only had deduction of 20% of average weekly salary).
- **Semesterlagen**: 25 vacation days minimum. Employees CANNOT waive this right. Carried-over days above 25 may be saved for up to 5 years.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
