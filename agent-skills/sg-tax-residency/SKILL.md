---
name: sg-tax-residency
description: "Use this skill for any question about Singapore tax residency for individuals for Year of Assessment 2026 (income of calendar 2025) and YA 2027. Trigger on Singapore tax resident, SG residency 183 days, three-year concession, straddling two years, move to Singapore tax, Singapore non-resident tax rate, 15% or resident rates, non-resident director fee 24%, Employment Pass tax, Singapore PR taxes, foreign-sourced income exempt Singapore, territorial taxation Singapore. Covers the IRAS residency tests, the resident progressive rates from YA 2024 (0% to 24%), non-resident rates and withholding, and the remittance exemption for resident individuals."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sg-tax-residency"
  jurisdiction: "SG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Singapore tax residency for individuals, YA 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Have a qualified Singapore tax adviser review before relying on it.

## Scope

Whether an individual is a Singapore tax resident for a Year of Assessment (YA), and what that changes. Singapore taxes on a preceding-year basis: YA 2026 taxes income earned from 1 January to 31 December 2025, and residence for YA 2026 is tested on 2025. The Inland Revenue Authority of Singapore (IRAS) administers the Income Tax Act 1947. Detailed computation of individual tax, reliefs and filing: `sg-income-tax`. Capital gains: `sg-zero-cgt`.

## Ask the client first

1. **Citizen, Permanent Resident or foreigner?**
2. **Dates in Singapore** in the calendar year before the YA, and in the years either side.
3. **Employment or other role.** Employee, company director, professional or public entertainer (the straddling-years rule excludes the last three).
4. **Work pass** and its validity.
5. **Income types**: Singapore employment, director's fees, business, rental, foreign income brought into Singapore.

## The method, step by step

1. **Citizens and Permanent Residents** are resident if they normally reside in Singapore, except for temporary absences.
2. **Foreigners** are resident for a YA if they stayed or worked in Singapore:
   - for at least 183 days in the previous calendar year; or
   - continuously for 3 consecutive years (the 3-year administrative concession: resident for all three years, even if under 183 days in the first or third); or
   - as an employee, for a continuous period straddling 2 calendar years with at least 183 days in total, counting presence immediately before and after the employment (from 1 January 2007; not for directors, public entertainers or professionals).
3. Days of employment include weekends, public holidays, and temporary or work-related absences (leave, business trips).
4. A foreigner with a work pass valid for at least 1 year is treated as resident at first; IRAS reviews the status at tax clearance when the employment ends.
5. **Resident**: taxed on Singapore income at the progressive rates below after reliefs; foreign-sourced income received in Singapore is exempt, except income received through a partnership in Singapore.
6. **Non-resident**: employment income at the higher of 15% flat and the resident rates (no reliefs); director's fees, consultancy fees and other income at 24%, with withholding on certain payments.

### Rates, bands and thresholds

| Chargeable income (S$), resident, YA 2024 onwards | Rate | Tax on the band (S$) | Tax at top of band (S$) | Source |
| --- | --- | --- | --- | --- |
| First 20,000 | 0% | 0 | 0 | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates |
| Next 10,000 (to 30,000) | 2% | 200 | 200 | same |
| Next 10,000 (to 40,000) | 3.5% | 350 | 550 | same |
| Next 40,000 (to 80,000) | 7% | 2,800 | 3,350 | same |
| Next 40,000 (to 120,000) | 11.5% | 4,600 | 7,950 | same |
| Next 40,000 (to 160,000) | 15% | 6,000 | 13,950 | same |
| Next 40,000 (to 200,000) | 18% | 7,200 | 21,150 | same |
| Next 40,000 (to 240,000) | 19% | 7,600 | 28,750 | same |
| Next 40,000 (to 280,000) | 19.5% | 7,800 | 36,550 | same |
| Next 40,000 (to 320,000) | 20% | 8,000 | 44,550 | same |
| Next 180,000 (to 500,000) | 22% | 39,600 | 84,150 | same |
| Next 500,000 (to 1,000,000) | 23% | 115,000 | 199,150 | same |
| Above 1,000,000 | 24% | | | same |
| Non-resident employment income | higher of 15% or resident rates | | | same |
| Non-resident director's fees, consultancy and other income | 24% | | | same |
| Non-resident professionals, withholding | 15% of gross or 24% of net | | | same |
| Non-resident public entertainers | 15% concessionary | | | same |
| Interest and loan fees to non-residents | 15% reduced final rate (conditions) or 24% | | | same |
| Physical presence test | 183 days in the previous calendar year | | | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency |
| Administrative concession | 3 consecutive years | | | same |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Stayed 1 Apr 2025 to 3 Oct 2025 (186 days) | Resident for YA 2026 (IRAS example) |
| Stayed 3 Nov 2023 to 7 May 2025 | Resident for YA 2024 to 2026 under the 3-year concession (IRAS example) |
| Employee, 1 Oct 2025 to 31 Mar 2026 (182 days plus presence before and after) | Straddling rule: resident for both years if 183 days or more in total |
| Director, professional or public entertainer straddling two years | Straddling rule does not apply; test each year separately |
| Foreign dividends, branch profits or service income brought in by a resident individual | Exempt, unless received through a Singapore partnership |
| Capital gains | Not taxed as such; see `sg-zero-cgt` for when gains are trading income |
| Rebate for YA 2026 | IRAS lists rebates for YA 2024 (50%, cap S$200) and YA 2025 (60%, cap S$200) only; do not apply one for YA 2026 unless announced |

## Worked cases

Case 1. A foreign employee stayed in Singapore for all of 2025 and has chargeable income of S$150,000 for YA 2026. She is resident. Tax: S$7,950 on the first S$120,000 plus 15% of S$30,000 = S$12,450.

```oa-check
name: Resident, chargeable income S$150,000, YA 2026
inputs:
  chargeable: 150000
steps:
  - tax: 7950 + (chargeable - 120000) * 0.15
expected:
  tax: 12450.00
```

Case 2, decision: does staying past 183 days matter? A foreign manager earns S$100,000 of Singapore employment income in 2025. If he leaves after 150 days (not straddling, no 3-year concession), he is non-resident: tax is the higher of 15% x S$100,000 = S$15,000 and resident rates on S$100,000 = S$3,350 + 11.5% of S$20,000 = S$5,650, so S$15,000. If he stays 183 days or more he is resident and pays S$5,650 before any reliefs. Staying resident saves S$9,350; the figure that decides it is the 183-day count.

```oa-check
name: Non-resident versus resident on S$100,000 employment income
inputs:
  income: 100000
steps:
  - flat: income * 0.15
  - progressive: 3350 + (income - 80000) * 0.115
  - non_resident_tax: max(flat, progressive)
  - saving: non_resident_tax - progressive
expected:
  flat: 15000.00
  progressive: 5650.00
  non_resident_tax: 15000.00
  saving: 9350.00
```

## When to refuse or refer

| Trigger | Message |
| --- | --- |
| Dual residence under a treaty | "Treaty tie-breaker rules need the full facts and a Certificate of Residence; refer." |
| Foreign income received through a Singapore partnership | "This is not covered by the individual remittance exemption; refer." |
| Not ordinarily resident scheme or other legacy concessions | "Legacy schemes have their own conditions; refer." |
| Tax clearance (IR21) on leaving | "Employer must file IR21; see `sg-income-tax` or refer." |

## Filing and payment

Residents and non-residents file Form B1 or B (see `sg-income-tax`) for YA 2026 on income of 2025. Employers of foreign employees who leave must seek tax clearance. Withholding on payments to non-residents is the payer's duty.

## Completion checklist

- Status (citizen, PR, foreigner) and day count recorded for the previous calendar year.
- 3-year concession and straddling rule tested.
- Role checked (director, professional, entertainer).
- Rates applied for the right status.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the resident rates from YA 2024, non-resident rates, withholding rates and YA 2024 and YA 2025 rebates | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates | 2026-11-14 |
| Read for the residency tests, the 3-year concession, the straddling rule, work pass treatment, examples and the remittance exemption for residents | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency | 2026-11-14 |

Not yet confirmed: work pass salary thresholds in the old file (Employment Pass S$5,000 a month, S Pass S$3,150; set by the Ministry of Manpower, not opened today); any YA 2026 personal income tax rebate (none listed by IRAS on the rates page read today); treatment of one-tier dividends received by individuals (not on the IRAS pages read; read the IRAS dividend page before restoring).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sg-tax-residency` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sg-tax-residency. If neither is available, confirm every figure against the official source pages cited above before relying on it.
