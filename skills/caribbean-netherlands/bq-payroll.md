---
name: bq-payroll
description: >
  Analyse 2026 payroll taxes in Bonaire, Sint Eustatius and Saba. Use for
  employee classification, withholding, monthly tables, employer premiums,
  payroll records, declarations, annual statements and reconciliation. Separates
  the wage, taxable-wage and contribution bases, combined employee withholding
  and employer costs. Includes verified monthly table rows, statutory filing
  periods, statement deadlines, primary sources and fictional balanced payroll
  examples. Records discrepancies in the official explanatory examples, elderly
  allowance and calculation sheet. This source-cited draft holds unverified
  special payments, elderly treatment, labour conditions, pensions, rounding
  and return mapping. Load with the payroll workflow base and BES contribution
  reference; professional review remains required.
jurisdiction: BQ
category: payroll
tax_year: 2026
tax_year_notes: "2026 payroll withholding and employer charges; payment date and assigned return period matter"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - payroll-workflow-base
  - bq-social-contributions
---

# Bonaire, Sint Eustatius and Saba: payroll taxes in 2026

Establish the employee, withholding agent, payment date, pay period and insurance
status before using a table. Monthly **pay** does not establish a monthly
**return**. The employee's combined withholding is separate from the employer's
programme charges. This is a source-cited reference pending professional review,
not a complete operational payroll companion or country pack.

Load `workflow-base`, `payroll-workflow-base` and `bq-social-contributions`.
Preserve profile confirmation, source gates, refusals, four universal outputs
and all five payroll outputs: payslips, journals, employer cost summary, filing
calendar and reviewer brief. Missing mandatory country slots hold the complete
financial output package; a labelled reference calculation remains available.

## Employment and the withholding agent

Wage Tax BES articles 2–4 define employees, deemed employments and withholding
agents. Test the actual relationship, including supervision and the statutory
deemed categories; an invoice or contractor label is insufficient. Directors,
substantial-interest workers, working children, commission workers, certain
contract-work relationships, artists and sportspeople have specific provisions.
Non-resident employee and foreign-employer rules also require their own tests.
The short-visit provision permits delegated relief; it does not itself make every
visit under three months exempt. [W, articles 1–4][W]

Identify insurance separately. A wage-tax employee is not necessarily a ZV, OV,
CES or healthcare employee for premium purposes. Read the person/programme
rules in `bq-social-contributions`; its ordinary examples do not establish an
overseas, director, public-sector or special worker's status.

An employer taking on its first employee registers with Belastingdienst
Caribisch Nederland using the employer-registration form. Retain the authority's
registration, assigned return-period and reference confirmation. The manual's
registration section identifies the CRIB correspondence number. The employer
retains identification documents, identity values and payment details outside
the agent. Record only stable references and verified status in the agent's
workpapers. [M, section 2.1][M]; [W, articles 19–19a][W]; [U, articles 4a–4e][U]

## Wage and taxable-wage bases

Wage broadly includes monetary and noncash employment benefits and specified
rights, subject to article 6's exclusions. Qualifying employee pension and
specified exempt-right contributions have their own treatment. Benefits in
kind use article 6c's valuation rules, with separate conditions for vehicles,
employee reimbursements, tips and delegated valuations. A wage value does not
increase cash earnings. Directors' customary-wage rules in article 6d require
their complete comparison, start-up and related-party tests; no flat presumed
salary is selected here. [W, articles 5–6e][W]

The wage-tax base is wage less the applicable fixed expense deduction. For a
current employment, article 6e gives a USD 280 annual deduction, capped by wage,
and prescribes conversion to other pay periods. Do not apply it to every
former-employment pension payment or also subtract it from the employer-premium
wage. Other deductions require their actual legal basis or inspector's decision.
[W, articles 5 and 6e][W]

The 2025-onwards payroll-record model distinguishes these columns:

| Column | Component | Control |
|---|---|---|
| 5 | Total specified wage components | Reconcile cash/noncash components to the payroll record. |
| 6 | Qualifying employee contributions to exempt rights | Establish the precise statutory treatment; not every personal premium belongs here. |
| 7 | Employer ZV/OV/CES and healthcare wage base | Column 5 less column 6. |
| 10 | Fixed expense deduction | Applies to the withholding base, not the employer-premium base. |
| 11 | Applicable inspector's decision | Use the actual amount, employer and effective period; do not invent an allowance. |
| 12 | Combined employee-withholding base | Column 7 less columns 10 and 11. |
| 13 | Employee withholding from the applicable table | Keep employer contributions separate. |
| 16 | Cash amount payable | Reconcile the record's cash components, deductions and reimbursements; noncash benefits are not paid as cash. |

[M, chapter 6, columns 5–16][M]; [U, article 4a][U]; [W]

## Withholding method and selected 2026 monthly rows

Wage is recognised at the article 10 receipt/set-off/availability/collectibility
events, with its special timing conditions. Withhold under the table applicable
at the statutory withholding time. Articles 8–8b and the implementing regulation
provide period tables, special-payment tables and the conversion framework.
Do not make a cumulative year-to-date method the default. [W, articles 8–11][W];
[U, articles 2–4][U]

The ordinary statutory annual schedule is the one in `bq-income-tax`: 29.4%
through an ordinary taxable sum of USD 53,198, then the published USD 15,640
constant plus 38.4% of the excess. **The published period table is a separate
withholding source.** Do not replace its rows with a simple division of a final
annual assessment or silently change its constants. The annual tax-free sum is
USD 21,956. A worker with overlapping employments can use the tax-free sum and
elderly allowance with only one withholding agent unless wage is aggregated
under the applicable rules. [W, articles 8–8a][W]; [IB]; [INDEX]; [T]

For an established ordinary monthly table case, choose the correct allowance
column. If taxable pay lies between listed rows, use the next lower listed
taxable-pay amount. The table contains combined wage tax, AOV/AWW and the
insured-person healthcare charge; do not add those employee premiums again.
Insured status still matters to component allocation and employer charges.
[E, pages 1–2][E]; [W, articles 12a–12c][W]

The following rows were checked as aligned native PDF cells. They are selected
reference rows, not an embedded complete table or a substitute for current
instructions. The elderly column is retained for source comparison only and
is held for computation, as explained below. Amounts are USD. [T, pages 9–10 and 27][T]

| Monthly taxable-pay row | No tax-free sum, no elderly allowance | Tax-free sum, no elderly allowance | Published elderly column, held |
|---|---:|---:|---:|
| 1,914 | 562.71 | 24.79 | 41.08 |
| 1,920 | 564.48 | 26.55 | 41.08 |
| 1,974 | 580.35 | 42.43 | 41.08 |
| 2,118 | 622.69 | 84.77 | 41.08 |
| 2,124 | 624.45 | 86.53 | 41.08 |
| 6,582, the final published row | 2,128.50 | 1,425.91 | 53.66 |

The final table page states the method for taxable pay above its last row:
38.4% of the excess, added to the last applicable withholding amount. Obtain
the complete conditions and rounding before using that tail for an actual
payroll. Do not extend the printed rows or use a different document's table-end
amount as though it appeared in this table. [T, page 27][T]

### Source discrepancies and held branches

The explanation's page 4 prints USD 526.71 for the no-allowance amount at a
USD 1,914 row. The actual monthly table prints USD 562.71. Page 6's narrative
mentions USD 1,416.33 at the last row, but its own table and total use
USD 1,425.91. Positioned native text confirms these are in the source, rather
than an OCR substitution. The selected rows above come from the actual table.
[E, pages 4 and 6][E]; [T, pages 9 and 27][T]

The calculation sheet and manual show an elderly allowance of USD 1,677; the
current statute and indexation instrument show USD 1,678. The manual's birth-date
shortcut also does not match its stated age-at-year-start test for 2026. Use the
statutory age condition when analysing eligibility; do not copy that shortcut.
This reference **holds payroll calculations relying on the elderly reduction**
until the applicable withholding treatment is established. Publishing a table
cell here does not select it as the legally correct relief. [C]; [M, chapter 15][M];
[IB, article 24][IB]; [INDEX]; [AOV, articles 5–6][AOV]

The calculation sheet's monthly end amount differs from the actual table's
last row. Its direct annual percentage calculation must also be distinguished
from the statute's published upper-band constant. These differences prevent
this reference from certifying a general payroll-software algorithm. Other
frequencies, special bonuses/overtime, gross-ups, anonymous-rate cases,
termination, noncash/insufficient-cash cases and corrections require their
complete instructions. The website's quarter-table label currently links to
the special-payment document; do not treat that link as a read quarterly table.
[C]; [T]; [W, articles 8a–12 and 20–21b][W]; [TABLES]

## Employer charges and fictional payroll check

For each programme, establish worker coverage and the wage base separately.
The ordinary 2026 employer rates are ZV 0.7%, OV 0.2%, CES 0.1% and healthcare
9.3%. The actual employee may not belong to every programme. These wage-based
charges have no tax-free sum, elderly allowance or insured-person USD 38,390
ceiling. Neither the fixed expense deduction nor the inspector's employee
withholding decision reduces that employer base. [RATES]; [CARE-RATES]; [C, page 2][C];
[M, chapter 6][M]

This fictional monthly case stipulates an ordinary age-40 full-year resident
employee, all programme coverage established, USD 2,000 cash wage and employer
base, current employment, no noncash benefit, pension/exempt-right contribution,
inspector adjustment, reimbursement or other deduction. The established monthly
fixed deduction is USD 23.33. Column 12 is USD 1,976.67, so the lower published
row is USD 1,974. The second column below instead stipulates that the tax-free
sum is lawfully used with another employer; it is **not** a default for missing
identity or residence. No elderly allowance is selected. [W]; [T, page 9][T]; [E]; [C]

| Component, USD | Tax-free sum used here | Tax-free sum used elsewhere |
|---|---:|---:|
| Cash wage / employer-premium base | 2,000 | 2,000 |
| Fixed expense deduction for withholding only | 23.33 | 23.33 |
| Taxable pay before table lookup | 1,976.67 | 1,976.67 |
| Published lower table row | 1,974 | 1,974 |
| Combined employee withholding | 42.43 | 580.35 |
| Cash net pay | 1,957.57 | 1,419.65 |
| Employer ZV | 14 | 14 |
| Employer OV | 4 | 4 |
| Employer CES | 2 | 2 |
| Employer healthcare | 186 | 186 |
| Total employer contributions | 206 | 206 |
| Employer wage plus contribution cost | 2,206 | 2,206 |
| Combined withholding and employer-payable components | 248.43 | 786.35 |

For the first case, the arithmetic journal debits wages USD 2,000 and employer
contribution expense USD 206; it credits net-pay liability USD 1,957.57,
withholding liability USD 42.43 and employer-contribution liabilities totalling
USD 206. Debits and credits are USD 2,206. Keep the programme subaccounts and
payment reconciliation identifiable; no cash payment is made by the example.
Exact-cent employer amounts avoid selecting an unverified fractional-cent
method. These checks do not certify eligibility, a real payslip, return-field
mapping or a final payroll run.

## Records, returns and deadlines

The implementing regulation requires a payroll record before the first wage
payment in each calendar year, with ongoing updates and the prescribed data.
The employee declaration and employer identity verification have separate
before-work/before-first-pay rules. The employer fulfils and retains those
records; the agent receives status confirmation, not identity-document uploads.
Preserve the specific declaration and identification retention periods, measured
from their stated end-of-year events. [U, articles 4a–4b and 4e][U]; [W, articles 19–19a][W]

The ordinary remittance period is the calendar quarter under the general tax
implementing regulation. Household-service wage has a half-year rule;
foreign artist/topsportsperson wage has a monthly rule. The inspector may assign
monthly periods in the specified cases. Permanent cessation replaces the period
with its elapsed part. Confirm the actual period and applicable combined-premium
rules before generating the employer's calendar. [B-RULES, article 8.8][B-RULES];
[W, articles 12a–12d][W]

B1 articles 8.5 and 8.11 supply the general fifteen-day filing/payment term after
the assigned period. For the ordinary calendar quarters, the 2026 manual lists
15 April, 15 July, 15 October 2026 and 15 January 2027. Check any granted extension
and applicable non-working-day rule; do not turn a pay frequency into a filing
period. B1 article 8.11(5) specifically extends the payment-on-return period by
the duration of a granted filing extension. Retain the decision. [B1]; [M, chapter 8][M]

The declaration separates employee-insurance base, employer-healthcare base,
employee-withholding base and their respective amounts. Reconcile programme
schedules, payroll records, the declaration and the authority receipt. A bank
debit alone is insufficient. Use the reference on the actual declaration;
payment details remain with the authorised reviewer. An assigned nil return
still requires the applicable declaration. [M, sections 8–8.4][M]; [B1, article 8.11(3)][B1]

Keep these reporting events separate. [U, articles 4c–4f][U]; [W, article 19(1)(d)][W]

| Event | Statutory requirement |
|---|---|
| Employee annual statement | Within one month after calendar year-end. |
| Employment ends during the year | Mandatory employee statement within two weeks after termination; preserve the Act's separate ten-day request duty where it applies. |
| Collective wage statement to inspector | Within three months after year-end; within one month after withholding liability ends during the year. |
| Expected cessation of withholding liability for at least twelve months | Notify within one month after the specified period ends. |
| Employee declaration retention | At least seven years after the end of the year in which employment ended or a replacement declaration was submitted. |
| Identification records retention | At least seven years after the end of the year employment ended. |

General tax administration records have their own seven-year rule under B1
article 8.86. Separate company-law records may have different duties; do not
treat a payroll retention period as permission to destroy another required
record. This reference authorises no deletion.

Late/missing returns, underpayment, correction, penalties, interest and objections
require the applicable statutory and policy branch. WAGE article 12d provides a
single application of the specified penalty provisions for simultaneous levies;
do not multiply a combined-return penalty by the number of programmes. This
reference does not calculate a penalty from a headline maximum. [W]; [B1]

## Completion conditions and self-checks

No additional missing-fact default is authorised. Unknown insurance, allowance
election, residence, wage classification, inspector decision or evidence remains
Needs Input or a source hold. The statutory anonymous-rate branch is not a
general substitute for asking which rules apply; establish its actual trigger.

### Minimum wage check

The 2026 gross hourly minimum for a covered worker aged 21 or older is
USD 10.69 in Bonaire, USD 10.61 in Sint Eustatius and USD 10.66 in Saba. Establish
the Minimum Wages Act's employment, wage and normal-hours definitions separately
from the wage-tax base. Overtime, holiday bonuses and the other article 7
exclusions cannot simply be counted as ordinary minimum-wage pay. [MIN, articles
2–9][MIN]; [RATES, article IX][RATES]

For time-based pay, article 8 gives worked weekly hours times the hourly minimum
for weekly pay; monthly pay multiplies that weekly amount by 52 and divides by
12. Unless otherwise agreed, the statutory conversion rounds **up to whole
dollars**. That rule is not the tax-table rounding rule. Younger workers and
any ministerially approved reduction require their own applicable conditions.
[MIN, articles 8, 11 and 12a][MIN]

For covered workers aged 16–20 in 2026, the youth decree gives these percentages
of the applicable island's adult minimum: ages 16–17, 65%; age 18, 75%; age 19,
85%; age 20, 90%. Use the current legal age class and applicable employment
conditions. A sector reduction under MIN article 11 requires its decision and
cannot simply be assumed; article 12a provides a different individual decision
route. [YOUTH, articles 1–2][YOUTH]; [MIN]

The September 2026 amendment adds a 55% age-15 band **from 1 January 2027**.
Its publication during 2026 does not make that band a 2026 rule. This reference
does not calculate a 15-year-old's entitlement or a future-year payroll.
[YOUTH-CHANGE, articles II–III][YOUTH-CHANGE]

For a stipulated covered adult Bonaire employee working 40 ordinary hours a
week, the standard monthly minimum calculation is USD 1,852.9333… before that
whole-dollar rounding, or USD 1,853 rounded up. The USD 2,000 fictional monthly
wage above exceeds this amount. The 40 hours are a case assumption, not a
statement of the statutory maximum working week. No youth or reduced minimum
is selected. [MIN]; [RATES]

Before a complete payroll output, establish every mandatory country slot,
including labour-law hours/overtime, applicable minimum wage/age rules,
mandatory benefits and pensions, termination, pay-frequency constraints, all
applicable withholding instructions, monetary rounding, actual payroll record
and declaration mapping, calendar and correction procedures. This draft does
not certify those unfilled slots or a live taxpayer/portal/workbook run.

Check employee withholding versus employer cost; column 7 versus column 12;
cash versus noncash pay; one use of an allowance; lower-row selection and correct
column; no second addition of employee premiums; exact programme coverage;
pay versus return period; statement deadlines; evidence-backed payments; and
all universal/domain outputs and reconciliations. Obtain professional sign-off.

## Primary sources and verification scope

Read on 17 October 2026. Selected WAGE provisions, the full implementing
regulation, selected general tax provisions, relevant insurance provisions and
2026 rate instruments were read. The 2026 explanation and calculation PDFs
were read as native text; the monthly rows used here were verified as aligned
positioned cells. Selected manual chapters were read, including registration,
bases, records, reporting and allowances. The full 92-page manual and every
row of every period table were not reviewed. No OCR or authentic-layout visual
comparison was used to establish these values.

[W]: https://wetten.overheid.nl/BWBR0029283/2025-04-01
[U]: https://wetten.overheid.nl/BWBR0029331/2025-04-01
[IB]: https://wetten.overheid.nl/BWBR0029281/2026-01-01
[INDEX]: https://zoek.officielebekendmakingen.nl/stcrt-2025-40487.html
[AOV]: https://wetten.overheid.nl/BWBR0028459/2026-07-01
[MIN]: https://wetten.overheid.nl/BWBR0028170/2026-01-01
[YOUTH]: https://wetten.overheid.nl/BWBR0028325/2010-10-10
[YOUTH-CHANGE]: https://zoek.officielebekendmakingen.nl/stb-2026-279.html
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[B-RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[RATES]: https://zoek.officielebekendmakingen.nl/stcrt-2025-39413.html
[CARE-RATES]: https://wetten.overheid.nl/BWBR0029426/2026-01-01
[TABLES]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/loonheffing/tabellen-en-rekenregels
[T]: https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/maandtabel-2026/maand-tabel-2026.pdf
[E]: https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/toelichting-2026/toelichting-tabellen-lb-en-premies-2026.pdf
[C]: https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/rekenregels-2026/rekenregels-tabellen-lb-en-premies-2026.pdf
[M]: https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/2026/handboek-loonheffingen-2026/bes-handboek-loonheffingen-2026.pdf

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
