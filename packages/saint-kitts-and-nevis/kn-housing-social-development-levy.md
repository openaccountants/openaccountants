---
name: kn-housing-social-development-levy
description: >
  Saint Kitts and Nevis Housing and Social Development Levy on wages for 2026. Covers
  the exemption cutoffs from 1 July 2025 (EC$520 a week, EC$1,040 fortnightly,
  EC$1,126.67 twice monthly, EC$2,253.33 monthly), the employee levy of 3.5% of total
  earnings to EC$6,500 a month, 10% from EC$6,500.01 to EC$8,000 and 12% above, the
  employer's 3% on all wages, no ceiling, payment with Form C3, the 10% and 1% a month
  late penalties, and the severance payment contribution of 1%. Trigger phrases include
  St Kitts housing levy, HSD levy, social development levy Nevis.
version: 1.0
jurisdiction: KN
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Kitts and Nevis Housing and Social Development Levy

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

The Housing and Social Development Levy (Act 7 of 1997) on ordinary wages in 2026, collected by the Social Security Board for the Comptroller of Inland Revenue, and the employer's severance payment contribution collected with it. Amounts are EC$. Social security contributions are in [kn-social-security-contributions](kn-social-security-contributions.md), with a different ceiling.

## Ask the client first

1. Pay frequency (weekly, fortnightly, twice monthly, monthly) and gross wages for the period.
2. Every wage component, and any December bonus or extra salary.
3. Is the employer registered with the Board and filing Form C3?
4. Any late payments outstanding?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Exemption, weekly pay | No employee levy on wages up to and including EC$520 (from 1 July 2025) | [Board notice, 16 July 2025](https://socialsecurity.kn/press/change-of-levy-deduction-threshold/) |
| Exemption, fortnightly pay | Up to and including EC$1,040 | same |
| Exemption, twice-monthly pay | Up to and including EC$1,126.67 | same |
| Exemption, monthly pay | Up to and including EC$2,253.33 | same |
| Employee levy, EC$2,253.34 to EC$6,500 a month | 3.5% of total earnings | same |
| Employee levy, EC$6,500.01 to EC$8,000 | 3.5% to 6,500 plus 10% of the part between 6,500.01 and 8,000 | same |
| Employee levy, above EC$8,000 | Plus 12% of the part above 8,000 | same |
| Employer levy | 3% of all wages, including wages below the employee cutoff | same |
| Ceiling | None for the levy or the severance contribution | [Board employers' guide](https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf) |
| Severance payment contribution | 1% of total wages, paid by the employer only | same |
| Late payment | 10% for the first month of default plus 1% for each further month | same |
| Minimum wage | EC$500 a week from 1 July 2025 | [Board notice, 16 July 2025](https://socialsecurity.kn/press/change-of-levy-deduction-threshold/) |

### Steps

1. **Pay frequency:** use the cutoff for that frequency; never the weekly one for a monthly worker.
2. **At or below the cutoff:** no employee levy; employer still pays 3%.
3. **Above the cutoff:** 3.5% of total earnings up to 6,500 (not of the excess over the cutoff), then 10% and 12% on the higher slices. The higher slices are stated monthly; for other pay frequencies ask the Board for its guidelines.
4. **Employer:** 3% levy plus 1% severance contribution on all wages.
5. **Report** on Form C3 with social security and pay monthly, with social security contributions.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Monthly wages 2,253.33 | Employee levy 0; employer 67.60 | [Board notice](https://socialsecurity.kn/press/change-of-levy-deduction-threshold/) |
| Monthly wages 2,253.34 | Employee levy 3.5% of the whole 2,253.34 = 78.87; the jump is by design | same |
| Employers' guide exemption of "less than EC$18,720 a year" | Superseded by the July 2025 cutoffs | [Board notice](https://socialsecurity.kn/press/change-of-levy-deduction-threshold/); [guide](https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf) |
| Social security ceiling of 6,500 | Does not cap the levy | [Board employers' guide](https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf) |
| December 2025 bonuses | Paid without levy deductions under the Board's 18 December 2025 notice; that notice does not cover December 2026 | [Board notice, 18 December 2025](https://socialsecurity.kn/press/treatment-of-bonus-paid-in-december-2/) |

## Worked cases

### Case 1: monthly wages at several levels

Employee levy and employer levy: 4,000 gives 140 and 120; 7,000 gives 277.50 and 210; 9,000 gives 497.50 and 270.

```oa-check
name: St Kitts housing levy, monthly 4,000, 7,000 and 9,000
inputs:
  w1: 4000
  w2: 7000
  w3: 9000
steps:
  - ee1: w1 * 0.035
  - er1: w1 * 0.03
  - ee2: min(w2, 6500) * 0.035 + max(min(w2, 8000) - 6500, 0) * 0.10
  - er2: w2 * 0.03
  - ee3: min(w3, 6500) * 0.035 + max(min(w3, 8000) - 6500, 0) * 0.10 + max(w3 - 8000, 0) * 0.12
  - er3: w3 * 0.03
expected:
  ee1: 140
  er1: 120
  ee2: 277.5
  er2: 210
  ee3: 497.5
  er3: 270
```

### Case 2 (decision): what does a pay rise across the cutoff cost?

A monthly worker on 2,253.33 pays no levy. A rise of one cent to 2,253.34 brings levy of 78.87, so net pay falls by 78.86. A rise has to be more than about 81.73 (3.5% of the new wage plus the rise itself) before net pay goes up. Plan pay rises near the cutoff with this in mind; the employer's 3% applies either way.

```oa-check
name: St Kitts levy cliff at the monthly cutoff
inputs:
  below: 2253.33
  above: 2253.34
steps:
  - levy_above: round(above * 0.035, 2)
  - net_change: round((above - levy_above) - below, 2)
  - breakeven_wage: round(below / 0.965, 2)
expected:
  levy_above: 78.87
  net_change: -78.86
  breakeven_wage: 2335.06
```

## When to refuse or refer

- December 2026 bonuses: wait for a current Board notice or the law.
- Non-monthly pay above EC$6,500 equivalents, irregular pay and special payments: ask the Board.
- Statutory exemptions other than the cutoff; the levy Act amendments.

## Filing and payment

1. Include employee levy, employer levy and severance contribution on Form C3 with social security.
2. Pay monthly by the same deadline as social security (end of the following month); late amounts carry 10% then 1% a month ([Board employers' guide](https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf)).
3. Keep separate ledger lines for each liability and reconcile them to the C3 total.

## Completion checklist

- Cutoff for the right pay frequency.
- 3.5% on total earnings; 10% and 12% slices.
- Employer 3% and severance 1% on all wages; no ceiling.

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Board notice "Change of levy deduction threshold", 16 July 2025: read for the cutoffs by pay frequency, the 3.5%, 10% and 12% slices, the employer 3% and the EC$500 weekly minimum wage | https://socialsecurity.kn/press/change-of-levy-deduction-threshold/ | 2026-11-14 |
| Board employers' guide 2018, pages 16 to 20: read for the severance contribution of 1%, the old EC$18,720 exemption, no ceiling for the levy, and the 10% plus 1% a month penalties | https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf | 2026-11-14 |
| Board notice "Treatment of bonus paid in December", 18 December 2025: read for the December 2025 levy exemption on bonuses and extra salary | https://socialsecurity.kn/press/treatment-of-bonus-paid-in-december-2/ | 2026-11-14 |
| Board housing levy page: read for the levy Act (7 of 1997) and the Board's collection role | https://socialsecurity.kn/housing-levy/ | 2026-11-14 |

Not yet confirmed: the Housing and Social Development Levy Act and its amendments (not opened); the higher slices for non-monthly pay; any December 2026 bonus notice; rounding rules.
