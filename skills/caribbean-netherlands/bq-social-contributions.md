---
name: bq-social-contributions
description: >
  Analyse 2026 statutory contributions in Bonaire, Sint Eustatius and Saba.
  Use for AOV, AWW, healthcare, employee insurance, cessantia, self-employed
  income, contribution ceilings and annual reconciliation. Establishes separate
  insured-person and employer charges, the taxable-sum base, insurance exclusions,
  tax credits and remittance evidence. Includes primary legislation, annual
  resident examples and separate employer wage calculations. Distinguishes
  contribution ceilings from benefit limits and annual assessment from payroll
  withholding. This source-cited draft holds unverified partial-year, overseas,
  voluntary, special-status, rounding and return-mapping branches. Load with the
  social contributions workflow base and the relevant income or payroll guide.
  It does not authorise filing or payment.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Calendar 2026 contributions; insured status and period established separately"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
  - bq-income-tax
---

# Bonaire, Sint Eustatius and Saba: contributions in 2026

Determine insured status **for each programme** before applying a percentage.
AOV, AWW and healthcare have different coverage rules. Employee status for wage
tax does not by itself settle employee insurance, cessantia or healthcare.
This Tier 2 reference supplies selected statutory contribution rules and
conditional examples; it does not certify a complete operational companion or
country pack.

Load `workflow-base`, `social-contributions-workflow-base` and `bq-income-tax`.
Keep their source gates, profile confirmation, refusals, four universal outputs
and five contribution outputs. Payroll owns the per-payslip computation; this
reference supports the annual position and reconciliation. An unfilled mandatory
country slot holds the complete financial output package.

## Programme, person and period

The ordinary AOV insured class begins at age 15 and ends at age 65, subject to
the residence, non-resident and exclusion rules in AOV article 5. AWW article 6
begins at age 15 and does **not** impose that AOV upper-age condition. Residence
is determined from circumstances, with the statutes' separate temporary-presence
and absence rules. Tax residence alone does not establish every insurance
status. [AOV, articles 1–6][AOV]; [AWW, articles 1–6][AWW]

Read the insured-circle decree with those Acts. It contains exclusions and
extensions for foreign-covered employment, specified public/international
service, short-stay artists/sportspeople, certain children, students and other
cases. The ministerial regulation adds further rules. Do not infer that a
person pays all programmes merely because they live or work in BES. The
ministerial regulation changed during 2026; establish the period before using
an exclusion. Cross-border, posting and uncertain special-status decisions are
held by this reference. [CIRCLE, articles 1–9][CIRCLE]; [REG]

From 22 July 2026, the ministerial amendment removes the specified Canadian/IBM
and English/Barclays AOV exclusions and the specified Saipem AOV/AWW exclusion.
The earlier text's nationality, employer, foreign-cover and residence-duration
conditions must not be applied after their repeal. The Dutch pensionable
public-service posting exclusion remains in article 4. A repealed exclusion
does not by itself prove every other coverage condition or resolve historical
premium/benefit consequences. [REG-OLD, articles 4–5][REG-OLD]; [REG]; [REG-CHANGE]

Healthcare has its own lawful-residence, employment, permit, study, public-service,
foreign-work, Dutch-insurance and other conditions in decree articles 2–5.
Article 4 includes express exceptions to its exceptions; article 29 contains a
separate transitional insurance-contract rule. Check the complete applicable
branch, rather than copying AOV status. The insured person's income contribution
in article 11 also applies outside employee payroll where its conditions are
met. The employer charge in article 12 is a separate wage-based liability.
[HEALTH, articles 1–5, 11–12 and 29][HEALTH]

The employer ZV/OV/CES programmes also have separate worker definitions and
exceptions. Directors, public-sector employees, seafarers and other categories
must be tested against the particular Act and any delegated rule. Do not
extend an ordinary employee's three-rate combination to every wage-tax
employment relationship. [ZV, articles 1–1a][ZV]; [OV, articles 1–1a][OV];
[CES, articles 1–1a][CES]

The AOV texts effective from January and July 2026 retain the same selected
insured-person and contribution provisions. The July amendment adds allowance
administration provisions and a punctuation correction; it does not establish
a new contribution percentage or ceiling. Pending/undated amendments are not
treated as operative. [AOV-JAN]; [AOV]; [JULY, article VII][JULY]; [START]

## Rates and bases

These are calendar 2026 figures in US dollars. They require established status
and the correct base; a percentage alone cannot determine a liability.

| Programme | Liable person | 2026 rate | Base and ceiling |
|---|---|---:|---|
| AOV | Insured person | 25% | Ordinary taxable sum under Income Tax BES article 24(1); annual maximum base USD 38,390. AOV articles 26–28; RATES article VI(D); IB article 24a(7). |
| AWW | Insured person | 1.3% | Same statutory taxable-sum definition and annual maximum base USD 38,390. AWW articles 29–31; RATES article VII(C); IB article 24a(7). |
| Healthcare, income contribution | Insured person | 0.5% | Taxable sum as defined by HEALTH article 1(h), with article 11's USD 38,390 maximum through IB article 24a(7). CARE-RATES article 1. |
| ZV sickness insurance | Employer | 0.7% | Established worker's wage under the Act; no tax-free sum, elderly allowance or annual insured-person ceiling. ZV article 8; RATES article XI(B); CALC page 2. |
| OV accident insurance | Employer | 0.2% | Established worker's wage under the Act; same distinction from personal allowances and ceilings. OV article 8; RATES article X(B); CALC page 2. |
| CES cessantia | Employer | 0.1% | Established worker's wage, under CES article 7; RATES article III; CALC page 2. |
| Healthcare, employer charge | Employer | 9.3% | Wage under HEALTH article 12; no personal tax-free sum, elderly allowance or insured-person annual ceiling. CARE-RATES article 2; CALC page 2. |

[RATES]; [CARE-RATES]; [IB]; [CALC]

For an ordinary full-year insured person's established non-negative taxable sum
`S`, the selected annual Acts cap each applicable income-contribution base at
USD 38,390. Apply each applicable programme separately. AOV/AWW/healthcare
premiums are not a second tax on gross receipts before the statutory taxable
sum. Do not give a separate annual ceiling to each income source or simply
divide an annual ceiling among payroll months. Partial-year and multiple-payer
withholding require their actual period rules and an annual reconciliation.
[AOV, article 26][AOV]; [AWW, article 29][AWW]; [HEALTH, articles 1(h) and 11][HEALTH]; [IB]

For a sole trader, establish the taxable sum through the personal-income rules,
not turnover, drawings or a prior-year assumed class. The insured person's
healthcare charge is separate from an employer's article 12 charge. An ordinary
sole trader's profit is not an employer wage base merely because it is taxable
personal income. This statement does not determine a director's wage or a
special employee/voluntary scheme. [IB]; [HEALTH, articles 1 and 11–12][HEALTH]; [ZV]; [OV]; [CES]

Employee-insurance **benefit** daily-wage limits are not ceilings for the employer
premiums in this table. The Acts and annual rate instrument distinguish their
benefit provisions from premium provisions; the official calculation guidance
expressly states no maximum base for those employer charges. Do not cap employer
ZV/OV or healthcare at USD 38,390. [RATES, articles X–XI][RATES]; [ZV, articles 5 and 8][ZV];
[OV, articles 5 and 8][OV]; [CALC, page 2][CALC]

## Income-tax credits and annual examples

Income Tax BES article 24a(2)–(7) supplies the corresponding contribution
credits; article 24c combines assessment where applicable. The income-tax
workpaper shows tariff tax, each credit, remaining income tax and each separate
premium. An equal credit and premium cancel in the combined arithmetic. They
are not two deductions and do not justify an independent refundable credit.
This reference does not settle a credit exceeding tariff tax. [IB]

The following fictional cases assume a full-year ordinary resident, age 40,
insured for all three income programmes throughout 2026, no foreign coverage,
posting, special exclusion or status change, and an already established taxable
sum from the income-tax workpaper. Every figure is an intermediate arithmetic
check, before final assessment rounding and evidenced settlement. [AOV]; [AWW];
[HEALTH]; [RATES]; [CARE-RATES]; [IB]

| Annual item, USD | Within ceiling | Above ceiling | Zero taxable sum | Sole trader |
|---|---:|---:|---:|---:|
| Established ordinary taxable sum | 30,000 | 40,000 | 0 | 25,000 |
| Base for each applicable income programme | 30,000 | 38,390 | 0 | 25,000 |
| AOV, 25% | 7,500 | 9,597.50 | 0 | 6,250 |
| AWW, 1.3% | 390 | 499.07 | 0 | 325 |
| Healthcare, 0.5% | 150 | 191.95 | 0 | 125 |
| Total separate premiums / corresponding credits | 8,040 | 10,288.52 | 0 | 6,700 |
| Ordinary tariff tax before contribution credits | 8,820 | 11,760 | 0 | 7,350 |
| Income tax after those credits | 780 | 1,471.48 | 0 | 650 |
| Combined income tax and premiums | 8,820 | 11,760 | 0 | 7,350 |

The zero case stipulates an established taxable sum of zero. It does not invent
a minimum premium, a negative-base treatment or a benefit entitlement. The
above-ceiling example caps the three **income** programmes, not employer
charges. The sole-trader case selects no employer payroll, private pension,
voluntary scheme or special maternity computation.

For a separate ordinary employee whose established employer-premium wage is
USD 2,000, with coverage established for all four employer programmes, ZV is
USD 14, OV USD 4, CES USD 2 and employer healthcare USD 186: total USD 206.
No personal allowance is deducted from that base. These exact arithmetic amounts
do not select a general fractional-cent rounding convention or establish wage
classification. [ZV]; [OV]; [CES]; [HEALTH]; [RATES]; [CARE-RATES]; [CALC]

## Declaration, remittance and reconciliation

Employer registration and the assigned return period must be established with
Belastingdienst Caribisch Nederland. Retain the registration/period confirmation
and the actual declaration. The employer retains identity documents, CRIB values
and payment details outside the agent; use stable references and confirmations
in workpapers. B1 article 8.86 imposes identification-number and administration
duties; it does not authorise an agent to collect or submit those records. [B1]

Wage tax and applicable premiums are remitted through the combined payroll
declaration under Wage Tax BES articles 12a–12d. The annual personal position
uses the combined assessment where Income Tax BES article 24c applies. Preserve
each programme's base, amount and taxpayer before reconciling a bundled payment.
Do not claim separate social payments again as personal-income expenses or
credits without their applicable authority. [WAGE]; [IB]

The prescribed ordinary wage-tax return period is a calendar quarter, with the
specific half-year/monthly and inspector-assigned exceptions in B-RULES article
8.8. Keep the AOV Act's article 29a remittance wording visible when examining
programme-specific procedure; it does not establish the actual assigned
combined payroll-return period. Read the combined-levy provisions and retain
the authority's period confirmation. [B-RULES]; [WAGE]; [AOV]

For remittances on return, B1 articles 8.5 and 8.11 generally require filing and
payment within fifteen days after the assigned period. Article 8.11(5) expressly
extends its fifteen-day payment period by a granted filing extension's duration.
Use the actual period and decision, and check exceptions and non-working-day
rules before producing dates. Do not import assessment-payment terms into a
payroll remittance. [B1]; [WAGE]

Match a bank debit to the authority receipt, declaration, taxpayer reference,
period and allocation. A transfer labelled tax, a payroll net-pay batch, private
pension payment, refund, loan or own-account transfer does not prove a statutory
contribution remittance. Keep unmatched and unapplied amounts visible. Do not
invent a bank-specific narrative or payment reference. Annual withholding and
provisional payments require authority reconciliation before an additional
balance or refund is selected. [B1]; [WAGE]; [IB]

Use `bq-payroll` for the payroll deadline, annual-statement and source-condition
details. The general and programme-specific penalty/collection provisions need
their complete applicable branch before any actual penalty or interest is
calculated. A statutory maximum is not an automatic charge. [B1]; [AOV]; [AWW];
[HEALTH]; [ZV]; [OV]; [CES]

## Completion conditions and refusals

No additional missing-fact default is authorised. Missing insured status,
programme inclusion, base, source evidence, exemption, period, rounding or
payment allocation remains Needs Input or a source hold. Do not default a
programme to insured, exempt or zero because a record is absent.

This reference holds partial-year changes, negative taxable sums, directors and
other uncertain worker classes, overseas/posted workers, special or voluntary
cover, pension/benefit entitlement, unverified fractional-cent methods and
unmapped returns. Establish each mandatory companion slot before delivering
the complete universal/domain package. No live taxpayer, portal declaration,
engagement workbook or practitioner sign-off was tested.

Check programme status separately; annual versus wage bases; cap versus benefit
limit; credits versus premiums; employer cost versus employee deduction; each
remittance's taxpayer/period; and the four universal plus five domain outputs.
Recalculate all engagement figures and obtain professional review before use.

## Primary sources

Selected provisions were read on 17 October 2026. The AOV January/July texts,
insured-circle decree, healthcare decree, programme premium provisions, 2026
rate instruments and Income Tax BES cross-references support the scope above.
The ministerial regulation's July change needs period-specific treatment.
This does not claim a full benefit, historical or treaty review.

[AOV]: https://wetten.overheid.nl/BWBR0028459/2026-07-01
[AOV-JAN]: https://wetten.overheid.nl/BWBR0028459/2026-01-01
[AWW]: https://wetten.overheid.nl/BWBR0028387/2026-01-01
[CIRCLE]: https://wetten.overheid.nl/BWBR0028533/2022-07-01
[REG]: https://wetten.overheid.nl/BWBR0029205/2026-07-22
[REG-OLD]: https://wetten.overheid.nl/BWBR0029205/2024-01-01
[REG-CHANGE]: https://zoek.officielebekendmakingen.nl/stcrt-2026-25854.html
[HEALTH]: https://wetten.overheid.nl/BWBR0029404/2025-01-01
[ZV]: https://wetten.overheid.nl/BWBR0028728/2026-01-01
[OV]: https://wetten.overheid.nl/BWBR0028497/2026-01-01
[CES]: https://wetten.overheid.nl/BWBR0028304/2025-01-01
[RATES]: https://zoek.officielebekendmakingen.nl/stcrt-2025-39413.html
[CARE-RATES]: https://wetten.overheid.nl/BWBR0029426/2026-01-01
[IB]: https://wetten.overheid.nl/BWBR0029281/2026-01-01
[WAGE]: https://wetten.overheid.nl/BWBR0029283/2025-04-01
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[B-RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[JULY]: https://zoek.officielebekendmakingen.nl/stb-2026-18.html
[START]: https://zoek.officielebekendmakingen.nl/stb-2026-76.html
[CALC]: https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/rekenregels-2026/rekenregels-tabellen-lb-en-premies-2026.pdf

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
