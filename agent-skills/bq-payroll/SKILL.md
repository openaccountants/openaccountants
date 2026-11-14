---
name: bq-payroll
description: "Analyse 2026 payroll taxes in Bonaire, Sint Eustatius and Saba. Use for employee classification, withholding, monthly tables, employer premiums, payroll records, declarations, annual statements and reconciliation. Separates the wage, taxable-wage and contribution bases, combined employee withholding and employer costs. Includes verified monthly table rows, statutory filing periods, statement deadlines, primary sources and fictional balanced payroll examples. Records discrepancies in the official explanatory examples, elderly allowance and calculation sheet. This source-cited draft holds unverified special payments, elderly treatment, labour conditions, pensions, rounding and return mapping. Load with the payroll workflow base and BES contribution reference; professional review remains required."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bq-payroll"
  jurisdiction: "BQ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bonaire, Sint Eustatius and Saba: payroll taxes in 2026

> **Built from the law. Not yet approved.** Written by Ryan Duguid and imported from his fork; conformed to the OpenAccountants standard by Claude. Not reviewed by an accountant. All outputs must be reviewed by a qualified tax professional before filing or payment. Tax year 2026. Currency: US dollars (USD).

## Scope

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

## Ask the client first

1. **Who the employer is and on which island** the employee works, and the payment date and pay period.
2. **The employee's age at 1 January 2026, residence, and whether the tax-free sum is used with this employer** or another one.
3. **Gross cash wage and any benefits in kind**, pension contributions or reimbursements for the period.
4. **Insurance coverage for each programme** (ZV, OV, cessantia, healthcare): the employer charges depend on it.
5. **The return period the Belastingdienst Caribisch Nederland has assigned** and payroll returns filed so far.

## The method, step by step

### Employment and the withholding agent

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

### Wage and taxable-wage bases

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

### Withholding method and selected 2026 monthly rows

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

| Monthly taxable-pay row | No tax-free sum, no elderly allowance | Tax-free sum, no elderly allowance | Published elderly column, held | Source of the figure |
|---|---:|---:|---:|---|
| 1,914 | 562.71 | 24.79 | 41.08 | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/maandtabel-2026/maand-tabel-2026.pdf |
| 1,920 | 564.48 | 26.55 | 41.08 | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/maandtabel-2026/maand-tabel-2026.pdf |
| 1,974 | 580.35 | 42.43 | 41.08 | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/maandtabel-2026/maand-tabel-2026.pdf |
| 2,118 | 622.69 | 84.77 | 41.08 | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/maandtabel-2026/maand-tabel-2026.pdf |
| 2,124 | 624.45 | 86.53 | 41.08 | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/maandtabel-2026/maand-tabel-2026.pdf |
| 6,582, the final published row | 2,128.50 | 1,425.91 | 53.66 | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/maandtabel-2026/maand-tabel-2026.pdf |

The final table page states the method for taxable pay above its last row:
38.4% of the excess, added to the last applicable withholding amount. Obtain
the complete conditions and rounding before using that tail for an actual
payroll. Do not extend the printed rows or use a different document's table-end
amount as though it appeared in this table. [T, page 27][T]

#### Source discrepancies and held branches

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

## Worked cases

### Employer charges and fictional payroll check

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

### Recomputed cases

**Case 1, employer cost on a USD 2,000 monthly wage.** All four employer programmes apply: ZV 0.7%, OV 0.2%, cessantia 0.1% and healthcare 9.3%, together USD 206. With the tax-free sum used here, the combined employee withholding from the monthly table row USD 1,974 is USD 42.43, so net pay is USD 1,957.57 and the employer's cost is USD 2,206 (first column of the table above).

```oa-check
name: BES monthly payroll, USD 2,000 wage, tax-free sum used here (2026)
inputs:
  wage: 2000
  fixed_deduction: 23.33
  table_withholding: 42.43
steps:
  - taxable_pay: wage - fixed_deduction
  - employer_charges: wage * (0.007 + 0.002 + 0.001 + 0.093)
  - net_pay: wage - table_withholding
  - employer_cost: wage + employer_charges
expected:
  taxable_pay: 1976.67
  employer_charges: 206
  net_pay: 1957.57
  employer_cost: 2206
```

**Case 2, a decision: which employer applies the tax-free sum?** The same employee has a second job and lawfully uses the tax-free sum with the other employer. This employer then uses the no-tax-free-sum column: withholding at row USD 1,974 is USD 580.35, net pay USD 1,419.65. The tax-free sum is worth USD 537.92 a month in withholding to whichever employer applies it; it may be used with only one.

```oa-check
name: Tax-free sum used elsewhere, row USD 1,974 (2026)
inputs:
  wage: 2000
  with_sum: 42.43
  without_sum: 580.35
steps:
  - net_without_sum: wage - without_sum
  - monthly_value_of_sum: without_sum - with_sum
expected:
  net_without_sum: 1419.65
  monthly_value_of_sum: 537.92
```

## When to refuse or refer

| Code | Situation | Action |
|---|---|---|
| R-BQ-PR-ELDERLY | The employee qualifies for the elderly reduction | Hold the payroll figure: the official sheet (USD 1,677) and the statute (USD 1,678) differ; refer to the Belastingdienst Caribisch Nederland |
| R-BQ-PR-SPECIAL | Special payments, bonuses, back pay or benefits in kind | Refer: the special-payment tables and conditions are not covered |
| R-BQ-PR-TAIL | Monthly taxable pay above the last printed table row (USD 6,582) | Refer until the tail method's conditions and rounding are confirmed |
| R-BQ-PR-STATUS | Director, posted or overseas worker, or uncertain employee status | Refer: coverage and withholding need a separate determination |

## Filing and payment

### Records, returns and deadlines

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

## Completion checklist

### Completion conditions and self-checks

No additional missing-fact default is authorised. Unknown insurance, allowance
election, residence, wage classification, inspector decision or evidence remains
Needs Input or a source hold. The statutory anonymous-rate branch is not a
general substitute for asking which rules apply; establish its actual trigger.

#### Minimum wage check

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

## Sources

| Source | URL | Read on |
|---|---|---|
| W. Read for the provisions this skill cites as [W]. | https://wetten.overheid.nl/BWBR0029283/2025-04-01 | 2026-10-17 |
| U. Read for the provisions this skill cites as [U]. | https://wetten.overheid.nl/BWBR0029331/2025-04-01 | 2026-10-17 |
| IB. Read for the provisions this skill cites as [IB]. | https://wetten.overheid.nl/BWBR0029281/2026-01-01 | 2026-10-17 |
| INDEX. Read for Bijstellingsregeling directe belastingen 2026 (Stcrt. 2025, 40487), article XII: tax-free sum USD 21,956, elderly amount USD 1,678, the USD 53,198 bracket and the USD 15,640 constant. Re-read on import. | https://zoek.officielebekendmakingen.nl/stcrt-2025-40487.html | 2026-11-14 |
| AOV. Read for the provisions this skill cites as [AOV]. | https://wetten.overheid.nl/BWBR0028459/2026-07-01 | 2026-10-17 |
| MIN. Read for the provisions this skill cites as [MIN]. | https://wetten.overheid.nl/BWBR0028170/2026-01-01 | 2026-10-17 |
| YOUTH. Read for the provisions this skill cites as [YOUTH]. | https://wetten.overheid.nl/BWBR0028325/2010-10-10 | 2026-10-17 |
| YOUTH-CHANGE. Read for the provisions this skill cites as [YOUTH-CHANGE]. | https://zoek.officielebekendmakingen.nl/stb-2026-279.html | 2026-10-17 |
| B1. Read for the provisions this skill cites as [B1]. | https://wetten.overheid.nl/BWBR0029244/2026-04-11 | 2026-10-17 |
| B-RULES. Read for the provisions this skill cites as [B-RULES]. | https://wetten.overheid.nl/BWBR0029332/2025-01-01 | 2026-10-17 |
| RATES. Read for Stcrt. 2025, 39413, articles III, VI(D), VII(C), X(B) and XI(B): 2026 rates AOV 25%, AWW 1.3%, OV 0.2%, ZV 0.7%, cessantia 0.1%. Re-read on import. | https://zoek.officielebekendmakingen.nl/stcrt-2025-39413.html | 2026-11-14 |
| CARE-RATES. Read for the provisions this skill cites as [CARE-RATES]. | https://wetten.overheid.nl/BWBR0029426/2026-01-01 | 2026-10-17 |
| TABLES. Read for the provisions this skill cites as [TABLES]. | https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/loonheffing/tabellen-en-rekenregels | 2026-10-17 |
| T. Read for the provisions this skill cites as [T]. | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/maandtabel-2026/maand-tabel-2026.pdf | 2026-10-17 |
| E. Read for the provisions this skill cites as [E]. | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/toelichting-2026/toelichting-tabellen-lb-en-premies-2026.pdf | 2026-10-17 |
| C. Read for the provisions this skill cites as [C]. | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/rekenregels-2026/rekenregels-tabellen-lb-en-premies-2026.pdf | 2026-10-17 |
| M. Read for the provisions this skill cites as [M]. | https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/2026/handboek-loonheffingen-2026/bes-handboek-loonheffingen-2026.pdf | 2026-10-17 |

### Primary sources and verification scope

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

Not yet confirmed: payroll calculations that rely on the elderly reduction (held: the official calculation sheet and manual show USD 1,677 against USD 1,678 in the statute and indexation instrument); special payments and their tables; the withholding tail above the last printed monthly row; rounding to the cent; the payroll return form and field mapping; pension and labour-law conditions. Other sources were read by Ryan Duguid on 2026-10-17; INDEX and RATES were re-read on 2026-11-14.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bq-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bq-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
