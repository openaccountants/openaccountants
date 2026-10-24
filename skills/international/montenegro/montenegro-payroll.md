---
name: montenegro-payroll
description: "Prepare Montenegro 2026 employment payroll workpapers: classify cash/noncash earnings, compute marginal salary PIT on gross, reconcile employee and employer contributions, keep local prirez separate from net salary, and map ordinary salary/aggregate tax to IOPPD. Includes ten executable salary, gross-up, benefit, multiple-payer, reporting, Chamber and disability-levy controls. Use for bruto/neto, withholding, code 097, IOPPD amendments and foreign salary. Current local decisions, benefit valuation, minimum salary, special levy/status implementation and reliefs, actual IRMS acceptance, historical arrears and independent review remain open. Source-cited preparation draft."
version: 0.3
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
sources:
  - url: "https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0"
    title: "PIT consolidation through 160/25"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0"
    title: "Enacted 160/25 PIT amendment applying January 2026"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0"
    title: "Employment payroll calculation instruction through 103/24"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/28aa7760-8d39-440d-8874-1ffcc5773095?version=1.0"
    title: "IOPPD reporting rule, instructions and code list through 124/24"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/5cb52f80-2fcc-4f77-8111-07ea8b6d8ff1?version=1.0"
    title: "Official IOPPD calculation-code workbook, October 2024/January 2025 revisions"
    as_of: "2026-10-24"
  - url: "https://www.sluzbenilist.me/propisi/389055/download"
    title: "151/25 Chamber contribution decision for 2026"
    as_of: "2026-10-24"
  - url: "https://www.zzzcg.me/wp-content/uploads/2018/01/Zakon-o-profesionalnoj-rehabilitaciji-i.pdf"
    title: "Disability employment law through 55/16, quota and levy Articles 21–23"
    as_of: "2026-10-24"
  - url: "https://www.sluzbenilist.me/propisi/385768/download"
    title: "122/25 disability-employment amendment and application gate"
    as_of: "2026-10-24"
  - url: "https://www.sluzbenilist.me/propisi/395547/download"
    title: "92/26 unified-assessment commencement deferral to December 2026"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0"
    title: "Ministry local-finance law reproduction, Articles 8–9"
    as_of: "2026-10-24"
---

# Montenegro payroll preparation v0.3

## Who this applies to

Prepare 2026 employment-income withholding and payroll ledgers for an established employee/payer/insurance period. Personal earnings include cash and specified noncash remuneration, temporary/occasional employment and supplementary work under labour rules. Independent business, dividends, rent and other receipts need their own classification, not automatic salary treatment. [PIT Articles 12, 14–16][pit]

This source-cited draft replaces the retained secondary-source summary at Git checkpoint `db00f70a`. The PIT consolidation through 160/25, actual January 2026 amendment, employment instruction and actual IOPPD rule/instructions were read. The May 70/26 amendment changes gambling income provisions, not the employment bands used here. The September proposal changes salary bands from January 2027 if enacted as proposed; it is not current 2026 law. No accepted return or named accountant review is claimed. [PIT][pit]; [160/25 Article 21][amend]; [70/26 Articles 1–3][may]; [proposal Articles 1–2][proposal]

The [contribution Guide](montenegro-social-contributions.md) owns insurance status, principal/supplementary entrepreneurship, statutory floors, annual refund and additional service. Its remaining cap/floor and exceptional-population limits apply here too. All seven country domains remain partial.

## Salary bands, separate bases and charges

| Item | Ordinary 2026 treatment | Source |
| --- | --- | --- |
| Salary PIT | 0% through EUR 700 monthly gross; 9% on the next EUR 300; 15% above EUR 1,000 | PIT Articles 10(1)(1), 15, 46; instruction Article 3 |
| Employee contributions | PIO 10%, unemployment 0.5%, on established contribution base | Contribution law Articles 9, 15, 18; instruction Article 4 |
| Employer contributions | Ordinary PIO 0%, unemployment 0.5%, Labour Fund 0.2% | Instruction Article 5; contribution law Articles 15, 18 |
| Municipal prirez | Applicable local rate × salary PIT; local decision required | Local-finance Articles 8–9; instruction Article 6 |
| PIT payment | Each payment, using applicable payment-date law, subject to specific historical-award provision | PIT Articles 46, 60k |
| Monthly IOPPD | By 15th of following month; electronic; complete replacement data on amendment | PIT Article 47; reporting rule Articles 5–7 |
| Employee annual statement | By 31 January for preceding year | PIT Article 47; instruction Article 9 |

Sources: [PIT][pit], [contributions][social], [instruction][instruction], [local finance][local], [IOPPD][ioppd]. These are the specified ordinary charges, not a conclusion that no other employment levy applies. The contribution floor and labour-law minimum salary are different checks. No current minimum salary or annual cap figure is certified here.

PIT uses gross personal earnings under Article 15. Do not deduct PIO/unemployment before calculating PIT. The zero band is part of the monthly marginal calculation; it is not another EUR 700 deduction after applying the bands. For established ordinary monthly taxable gross G:

`PIT = 0.09 × max(min(G, 1000) − 700, 0) + 0.15 × max(G − 1000, 0)`.

This expresses the instruction's EUR 27 fixed first-band tax above EUR 1,000. The law prints cent expressions at band boundaries; use current authority rounding/validation for fractional-cent issues. Examples use explicit cents rounding and established whole-month gross. Do not reset the monthly bands on every instalment paid to the same person in that period. Keep cumulative gross/tax/payment records and reconcile all salary-type codes before reporting tax through 097. [PIT Articles 10, 15, 46][pit]; [instruction Articles 3, 10][instruction]; [IOPPD instructions, column 8/code 097][ioppd]

## Net pay and municipal surtax allocation

Keep Bruto I, employee deductions, net salary, payer-side charges and total funding distinct. Under the Ministry's calculation structure, net salary is gross minus salary PIT and employee contributions. Prirez is separately recorded in payer-side funding, not deducted again from that net salary. The current employment instruction places prirez in its charges-on-earnings section; the Ministry's generic example explicitly shows it outside net in Bruto II. The example is dated 2022 and is used for allocation/layout only, **not** its superseded pension rates, minimum wage, blanket local-rate note or other levy assumptions. [Instruction Articles 2–7][instruction]; [Ministry generic example][example]

For ordinary cash salary with contribution base equal to taxable gross and established local rate r:

- Employee deductions: salary PIT + 10% PIO + 0.5% unemployment.
- Net salary: gross less those employee deductions.
- Specified employer funding: gross + 0.5% employer unemployment + 0.2% Labour Fund + r × PIT.
- Add all separately applicable levies, noncash cost, reimbursements or other costs before describing a result as total employer cost. [Instruction Articles 2–6][instruction]; [Ministry allocation example][example]

The statutory ceilings of up to 13%, or up to 15% for the capital/old capital, do not enact a single local rate for every municipality. Obtain the operative municipality decision, geographical/payer rules and local filing/payment details. The [municipality-hosted Bar ordinance][bar] specifies 13% of PIT and monthly local reporting/payment, but its current amendment chain and any taxpayer's situs are not cleared here. Do not copy that rate nationwide or treat national IOPPD as the local prirez filing. The controls below use explicit assumed local rates, not a certified municipality assignment. [Local-finance Articles 8–9][local]; [instruction Article 6][instruction]; [Bar Articles 3–7][bar]

## Additional employer and business charges

### Chamber contribution for 2026

The actual 151/25 decision applies from 1 January 2026 and requires **Chamber members** to pay 0.27%. Point 2 uses gross employee salaries reported in IOPPD; for entrepreneurs it uses independent-activity income shown in GPP-FL. Payment follows the relevant IOPPD/GPP-FL submission. Establish membership, legal person/entrepreneur capacity, correct income population and any exception before multiplying. Do not use the employer's sales turnover, net salary or the duplicated code-097 reporting base as a second economic salary amount. [Decision points 1–3, 6][chamber]

Point 4 excludes the specified persons entered in the artisan register after its establishment. Retain actual registration and applicable effective date. The municipality's April 2026 notice reports the register began operating on 1 March 2026, but that does not establish that a particular employer is registered or all its earlier payments are refundable. An exemption from the business Chamber contribution does not prove no separate craft-Chamber obligation. Actual craft dues, membership cases, partial-period treatment and current payment instructions require their own evidence. The published decision lists payment accounts; confirm the current recipient/account before payment, not from an old generic payroll template. [Decision points 4–5][chamber]; [municipal registration notice][artisan]

Keep Chamber contribution outside employee net in the employer/business liability schedule. The original six payroll controls intentionally exclude it; the seventh shows its incremental funding effect for an established liable member. An entrepreneur's annual contribution is a different base/payment event, not an employee deduction or a second salary return. Any PIT deduction timing and treatment need their own business-base reconciliation. [Decision points 1–3][chamber]

### Disability-employment quota and special levy

Read the original law's Articles 21–23 with the 122/25 amendment and 92/26 commencement change. Article 21 requires at least one qualifying worker for employers with 20–50 employees, and at least 5% for more than 50, with statutory rounding. Article 22 charges 20% of the preceding-year national average monthly salary for each required worker not employed. For employers with **more than 10 and fewer than 20** employees and no qualifying worker, it specifies a monthly 5% contribution instead. Those are employer/shortfall charges, not 20%/5% of each employee's pay. Establish monthly headcount, recognised qualifying status, quota credit and exceptions. [Articles 21–23][disability]

Article 21's 24-month new-employer wording is expressly linked to its paragraph 2; do not turn it into a blanket exemption for every new employer. Article 22a exempts qualifying disability organisations/associations as employers. Before the later reform's application, Article 21(5) has a specified severe-disability double-count rule. Record actual status and period, not a self-selected headcount discount. Borderline headcounts, fractional quota rounding, multiple establishments, status changes and the exact scope of exceptions require current authority confirmation. The controls use 15 employees or an exact-integer quota, no new-employer/association/severe-disability adjustment. [Articles 21–22a][disability]

The actual 122/25 amendment changes the status/support system and repeals specified old provisions from its application date, including Article 21(5). Its Article 10 ties application to commencement of unified assessment. The actual 92/26 amendment moves that commencement in Article 60(1) from 1 July to **1 December 2026**. Do not apply the new status/repeal regime to these October 2026 controls merely because 122/25 was enacted earlier. Recheck later amendments/commencement before December or later payroll, and retain continuation/reassessment decisions. [122/25 Articles 9–10][disability-amend]; [92/26 Articles 1–2][deferral]

Article 22 specifies the preceding-year average monthly salary. The extracted law/agency guidance does not itself explicitly label that statistical series gross or net; a government draft explanation describes gross, but is not a substitute for the operative current calculation/authority field guidance. **The exact statistical-series selection and resulting 2026 nominal levy are not certified here.** The two levy controls below therefore use an expressly hypothetical already-established reference base, not a claim that it is the published 2026 amount. [Article 22][disability]; [agency explanation][disability-agency]

Pay the applicable levy at monthly salary/compensation payment, with tax-authority control under Article 23. Published IOPPD instructions have a separate disability item for employee/qualifying-person counts, base, rate and contribution. Keep the company-level charge separate from per-person contribution rows, reconcile any status/shortfall change and current authority acknowledgement/payment ledger. Current reporting fields, statistical-base guidance, payment account and corrections remain open. Do not offset a subsidy or assumed quota credit without the legal decision. [Articles 22–23][disability]; [IOPPD instructions][ioppd]

## Earnings, benefits and exclusions

Article 14 covers salary/compensation, employee board/body remuneration, vouchers/shares/goods, benefits, debt forgiveness and employer-paid personal expenses, plus labour-law temporary/occasional and supplementary work. Noncash valuation follows the nominal/market/expense rules in Article 14(2). Maintain a payment-by-payment matrix: cash amount, taxable gross benefit, PIT exemption, contribution inclusion/exclusion, evidence and reporting code. Noncash value is not additional cash paid to the employee. [PIT Articles 14–15][pit]

Article 5a contains specific limits/conditions, including increased-cost allowances, death/illness assistance, retirement/redundancy, scholarships, newborn payments, education and jubilee awards. For example, the 2026 amendment raises qualifying death solidarity assistance to EUR 2,000 and distinguishes an employee newborn payment up to EUR 1,000 from social/child-protection-law receipts. These are receipt-specific exemptions, not a general allowance for arbitrary payments. Travel/car limits require the actual implementing instrument; none is invented here. [PIT Articles 5–5a][pit]; [160/25 Article 2][amend]

Contribution law Article 18a separately excludes specified noncash benefits unless replacing unpaid salary. Thus a taxable noncash benefit can have a different contribution result. Keep genuine salary replacement, ordinary cash bonuses, reimbursement and benefit valuation separate. The amended zimnica contribution limit does not establish a PIT exemption for that payment. Labour Fund treatment for noncash/exempt benefits needs separate rule/application verification. [Contribution Articles 3a, 18a][social]; [PIT Articles 14–15][pit]

For qualifying acquired digital-nomad status, inspect the actual personal and contribution relief conditions; foreign payer or remote work alone does not establish relief. Do not reuse an expired employment-incentive code as a new 2026 exemption. Full immigration/status, incentive eligibility and exceptional benefit cases remain open. [PIT Articles 32c–32d][pit]; [contribution Articles 18c–18d, 31a][social]

## Inputs and run sequence

1. Obtain employer/person identifiers, contract and registered insurance status, work/residence countries, municipality, pay period/payment date, hours/absence, all concurrent payers, gross/net contract terms and prior instalments. Establish the current labour/collective-agreement floor and statutory contribution base. [PIT Articles 3–4, 14–15, 46][pit]; [contribution Articles 4–13][social]
2. Classify cash and benefits, prove exemptions/valuation and distinguish taxable gross from contribution gross. Keep expense reimbursements and actual benefit provision separate from cash paid. [PIT Articles 5a, 14–15][pit]; [contribution Article 18a][social]
3. Calculate monthly aggregate PIT, person-side contributions, net cash, payer-side contribution/prirez schedules and other applicable employment levies. Reverse a desired net only after selecting the correct band and insurance status; recompute components at cents. [Instruction Articles 2–7][instruction]
4. Assemble IOPPD rows by person, code and actual insurance periods, with salary tax through aggregate code 097. Reconcile reported liabilities to payroll ledger and paid amounts; do not treat a sum of repeated report bases as actual payroll expense. [Reporting rule/instructions][ioppd]
5. Submit on the current authority electronic service, retain acknowledgement and reconcile payment/authority ledger. File the separate local declaration where required and deliver the annual employee statement. For changes, retain the original and the full replacement return, authority response and payment adjustment. [PIT Article 47][pit]; [reporting Articles 5–7][ioppd]; [local example Article 5][bar]

## IOPPD form assembly and correction

The actual authority attachment is **RTF despite its generic download label**, not a PDF. Its rule, instructions and code list through 124/24 were extracted/read. The official XLS code workbook was inspected read-only. These establish the following published preparation mapping; authenticated current IRMS schema acceptance and all later code changes are not certified. [Rule/instructions][ioppd]; [code workbook][codes]

| Field | Published instruction |
| --- | --- |
| 0.1 / 0.2 / 0.3 | Reporting month/year; original or amended report marker |
| 1.1–1.4 | Payer identifier/name and preparer contact details |
| Columns 2 / 3 | Insured person's identifier/name |
| Column 4 | Calculation code; ordinary salary 001, applicable sick-pay separate code, aggregate salary tax 097 |
| Columns 5 / 6 | First/last day of relevant insured period within report period, subject to specified quarterly exception |
| Column 7 | Gross base for the particular row, not necessarily unique economic earnings |
| Column 8 | Income tax; employment tax calculated exclusively through 097 for total personal earnings over EUR 700 |
| Columns 9 / 11 | Employee PIO / unemployment |
| Column 12 / 14 / 15 | Payer PIO / unemployment / Labour Fund |
| Columns 10 / 13 | Historical health contribution fields for the stated periods through December 2021, not current 2026 charges |
| Totals / separate disability item | Published column sums and distinct disability non-employment levy inputs; quota/rate method below; current statistical-series/status/schema implementation still open |

Source: [IOPPD instructions, general/special parts][ioppd]. The XLS `Kontrole poreza i doprinosa` sheet confirms ordinary salary row 3 contribution rates and tax through 097, and row 104 aggregate-tax purpose. It contains historic text, malformed historical dates, and row 109 zimnica wording predating the actual 2026 amendment. It must not override law or supply a current floor/exemption from its old labels. The printed 097 inclusion lists also differ between materials; special income-code inclusion needs current authority confirmation, not a guessed merged list. [Workbook][codes]; [contribution Article 18a][social]

Code 097 repeats an income base for tax reporting; it is not another salary payment, expense or contribution base. Reconcile economic earnings once from salary/benefit records, calculate aggregate tax once, and separately follow required form column totals. A salary/sick-pay split must not grant a separate zero band to each row. The control below illustrates this duplication risk, not a portal-ready payload. [IOPPD instructions, columns 4–8 and totals][ioppd]

Rule Article 6 requires an amended period report with complete data for all persons concerned, not only the changed employee/difference. Article 8's retained OPD1 exception concerns earlier-period unpaid earnings and needs the original rules/application dates; do not automatically send every arrear as a current 001 row or make OPD1 the ordinary 2026 return. [IOPPD Articles 6–8][ioppd]

## Worked examples

Hypothetical full-month 2026 EUR cases with established employee/status/base, salary above the applicable verified floor, no additional service, exemptions, annual PIO refund or other employment levies except those stated. Local rates are explicit scenario inputs. Each example tests its stated method, not an accepted filing or universally complete employer cost. Cents use half-up rounding per component for these workpapers; current portal validation remains open.

### 1. Ordinary upper-band payroll and cash reconciliation

Gross 2,000, local rate assumed 15%. PIT 177, employee contributions 210, net 1,613; specified payer funding 2,040.55. Prirez is included in payer funding, not deducted from net again. [PIT Articles 10, 15, 46][pit]; [instruction Articles 2–6][instruction]; [allocation example][example]

```oa-check
name: Montenegro ordinary cash payroll and payer reconciliation
inputs:
  gross: 2000
  local_rate: 0.15
steps:
  - pit: round(27 + (gross - 1000) * 0.15, 2)
  - employee_pio: round(gross * 0.10, 2)
  - employee_unemployment: round(gross * 0.005, 2)
  - net: gross - pit - employee_pio - employee_unemployment
  - employer_unemployment: round(gross * 0.005, 2)
  - labour_fund: round(gross * 0.002, 2)
  - prirez: round(pit * local_rate, 2)
  - specified_funding: gross + employer_unemployment + labour_fund + prirez
  - remittances: pit + employee_pio + employee_unemployment + employer_unemployment + labour_fund + prirez
  - cash_reconciliation: specified_funding - net - remittances
expected:
  pit: 177
  employee_pio: 200
  employee_unemployment: 10
  net: 1613
  employer_unemployment: 10
  labour_fund: 4
  prirez: 26.55
  specified_funding: 2040.55
  remittances: 427.55
  cash_reconciliation: 0
```

### 2. Salary at the first taxed-band ceiling

Gross 1,000, local rate assumed 13%. PIT is 27, net 868, specified funding 1,010.51. Do not apply 9% to the entire 1,000 or deduct contributions before calculating PIT. [PIT Articles 10, 15][pit]; [instruction][instruction]

```oa-check
name: Montenegro salary band ceiling
inputs:
  gross: 1000
  local_rate: 0.13
steps:
  - pit: round(max(min(gross, 1000) - 700, 0) * 0.09 + max(gross - 1000, 0) * 0.15, 2)
  - net: gross - pit - round(gross * 0.10, 2) - round(gross * 0.005, 2)
  - prirez: round(pit * local_rate, 2)
  - specified_funding: gross + round(gross * 0.005, 2) + round(gross * 0.002, 2) + prirez
expected:
  pit: 27
  net: 868
  prirez: 3.51
  specified_funding: 1010.51
```

### 3. Net-to-gross in the established upper band

Target cash net 1,500. For this status/band, net before cents = 0.745 × gross + 123; gross = (net − 123)/0.745. Recompute each component after rounding gross to cents. This is not a universal gross-up factor for benefits, partial periods, nonemployees or exempt/capped cases. [PIT Articles 10, 15][pit]; [instruction Articles 2–5][instruction]

```oa-check
name: Montenegro upper band net to gross
inputs:
  target_net: 1500
steps:
  - gross: round((target_net - 123) / 0.745, 2)
  - pit: round(27 + (gross - 1000) * 0.15, 2)
  - employee_pio: round(gross * 0.10, 2)
  - employee_unemployment: round(gross * 0.005, 2)
  - actual_net: gross - pit - employee_pio - employee_unemployment
expected:
  gross: 1848.32
  pit: 154.25
  employee_pio: 184.83
  employee_unemployment: 9.24
  actual_net: 1500
```

### 4. Taxable genuine noncash benefit, separate contribution base

Cash gross salary 2,000 plus established taxable market-value benefit 200. Assume it is an Article 18a(3) excluded noncash benefit and does not replace unpaid salary. PIT base 2,200, contribution base 2,000, PIT 207, cash net 1,583 plus benefit provided in kind. Labour Fund/other costs on the benefit and any tax gross-up undertaking are outside this control. [PIT Articles 14(1)(4), 14(2), 15][pit]; [contribution Article 18a(3)][social]

```oa-check
name: Montenegro noncash benefit separate payroll bases
inputs:
  cash_gross: 2000
  taxable_benefit: 200
steps:
  - pit_base: cash_gross + taxable_benefit
  - contribution_base: cash_gross
  - pit: round(27 + (pit_base - 1000) * 0.15, 2)
  - employee_contributions: round(contribution_base * 0.10, 2) + round(contribution_base * 0.005, 2)
  - net_cash: cash_gross - pit - employee_contributions
expected:
  pit_base: 2200
  contribution_base: 2000
  pit: 207
  employee_contributions: 210
  net_cash: 1583
```

### 5. Concurrent employers: aggregate PIT exposure

Same month gross 1,200 from employer A and 800 from B, each payer's assumed PIT 57 and 9. Aggregate gross 2,000 implies 177 under the employment scale, versus 66 withheld: indicative difference 111. Articles 43(4)(5)/43a require the annual return and authority assessment for qualifying multiple-payer income; this control is a monthly exposure workpaper, not an instruction for employer A to collect the other payer's liability or a substitute for that decision. [PIT Articles 10, 43, 43a][pit]

```oa-check
name: Montenegro concurrent employers indicative tax difference
inputs:
  gross_a: 1200
  gross_b: 800
steps:
  - withheld_a: 27 + (gross_a - 1000) * 0.15
  - withheld_b: (gross_b - 700) * 0.09
  - total_gross: gross_a + gross_b
  - aggregate_pit: 27 + (total_gross - 1000) * 0.15
  - indicative_difference: aggregate_pit - withheld_a - withheld_b
expected:
  withheld_a: 57
  withheld_b: 9
  total_gross: 2000
  aggregate_pit: 177
  indicative_difference: 111
```

### 6. Ordinary salary and qualifying sick-pay rows, one aggregate tax row

Salary 1,500 plus correctly calculated/eligible short sick-pay compensation 500 in the same month. Contributions are allocated over the actual rows/periods, aggregate code 097 base 2,000 and PIT 177. Its repeated base is not a second 2,000 payment. Sick-pay entitlement, underlying amount and reimbursement decision are assumptions. [IOPPD instructions, codes 001/006/097 and columns 7–15][ioppd]; [code workbook][codes]

```oa-check
name: Montenegro IOPPD salary and sick pay aggregate tax control
inputs:
  salary_base: 1500
  sick_base: 500
steps:
  - economic_gross: salary_base + sick_base
  - salary_pio: salary_base * 0.10
  - sick_pio: sick_base * 0.10
  - total_pio: salary_pio + sick_pio
  - employee_unemployment: economic_gross * 0.005
  - code_097_pit: 27 + (economic_gross - 1000) * 0.15
  - repeated_report_bases: salary_base + sick_base + economic_gross
  - net_cash: economic_gross - total_pio - employee_unemployment - code_097_pit
expected:
  economic_gross: 2000
  salary_pio: 150
  sick_pio: 50
  total_pio: 200
  employee_unemployment: 10
  code_097_pit: 177
  repeated_report_bases: 4000
  net_cash: 1613
```

### 7. Chamber contribution added to ordinary employee funding

Established liable Chamber member, no artisan exception, one employee gross 2,000 and assumed local prirez rate 15%. Original control 1's specified funding 2,040.55 excludes Chamber. Contribution 0.27% × 2,000 = 5.40; expanded specified funding 2,045.95. Employee net stays 1,613. Other levies still need separate applicability checks. [Chamber decision points 1–3][chamber]; [instruction][instruction]

```oa-check
name: Montenegro Chamber contribution incremental payroll funding
inputs:
  salary_gross: 2000
  funding_before_chamber: 2040.55
  employee_net: 1613
steps:
  - chamber_due: round(salary_gross * 0.0027, 2)
  - expanded_specified_funding: funding_before_chamber + chamber_due
  - employee_net_after_employer_charge: employee_net
expected:
  chamber_due: 5.40
  expanded_specified_funding: 2045.95
  employee_net_after_employer_charge: 1613
```

### 8. Entrepreneur Chamber base differs from employee payroll

An established liable member's GPP-FL independent-activity income base is 15,000, with no artisan exception. Annual Chamber contribution 40.50, due with the relevant return submission. The input is the established statutory return-income base, not turnover, salary or a new conclusion about PIT expense deductibility. [Decision points 1–3][chamber]

```oa-check
name: Montenegro entrepreneur Chamber contribution
inputs:
  established_return_income: 15000
steps:
  - annual_chamber_contribution: round(established_return_income * 0.0027, 2)
expected:
  annual_chamber_contribution: 40.50
```

### 9. Employer with 15 workers and no qualifying disability worker

October 2026 established nonexempt employer, 15 employees, no qualifying worker. Use a **hypothetical established statutory reference base of 1,000**, not a certified national 2026 amount. Article 22's 5% employer contribution is 50 for the month; do not multiply it by all 15 employees or the salary bill. Statistical-series selection and actual amount remain an implementation gap. [Article 22][disability]

```oa-check
name: Montenegro smaller employer disability levy method
inputs:
  hypothetical_established_reference_base: 1000
steps:
  - monthly_employer_levy: hypothetical_established_reference_base * 0.05
expected:
  monthly_employer_levy: 50
```

### 10. Exact quota and shortfall for an 80-worker employer

October 2026 established nonexempt employer, 80 employees. Statutory 5% quota is exactly four; two workers count once each with documented qualifying status, no double-count or new-employer exception. Shortfall two; at a **hypothetical established reference base of 1,000**, contribution 2 × 20% × 1,000 = 400. No fractional quota issue or actual 2026 nominal levy is certified. [Articles 21–22][disability]; [date gate][deferral]

```oa-check
name: Montenegro disability quota shortfall employer levy
inputs:
  employee_count: 80
  established_qualifying_count: 2
  hypothetical_established_reference_base: 1000
steps:
  - required_count: employee_count * 0.05
  - shortfall: max(required_count - established_qualifying_count, 0)
  - monthly_employer_levy: shortfall * hypothetical_established_reference_base * 0.20
expected:
  required_count: 4
  shortfall: 2
  monthly_employer_levy: 400
```

## Payment, annual reporting and foreign salary

PIT is calculated/withheld/paid on each earnings payment under Article 46, not postponed to the following month's reporting deadline. The instruction requires simultaneous contributions/prirez payment and noncash charges by the month's last working day. Contribution Article 21 and IOPPD Article 5 specify monthly deadlines for their respective population/reporting functions. Preserve calculation period, payment event, report period and original obligation date separately. [PIT Article 46][pit]; [instruction Article 7][instruction]; [contribution Article 21][social]; [IOPPD Article 5][ioppd]

Resident recipients of foreign earnings and specified immune diplomatic/international-employer earnings have Article 46 self-calculation/payment within five days of receipt; a nonresident employer with a Montenegro establishment and no diplomatic immunity has its own employer duty. Residence, source, treaty priority, credit evidence and insurance coordination remain separate checks. Do not turn a foreign bank payer into automatic exemption or assume tax treaty relief also exempts social insurance. [PIT Articles 3–4, 44–46][pit]; [contribution Articles 5, 7][social]

Employer annual employee information is due by 31 January for the preceding year. The annual personal return is a separate taxpayer obligation for the Article 43 populations, including foreign income and qualifying multiple employers, ordinarily by end April. Article 43a provides an authority decision for the multiple-payer case. Do not multiply monthly tax by twelve and call it the final annual liability without reconciling the actual circumstances/assessment. [PIT Articles 43–43a, 47][pit]

Historic dispute/court awards fall under PIT Article 60k and contribution Article 29b's original-due-date rate rules. The reporting rule retains special earlier-period provisions. Determine the original period, legal decision and payment before selecting rates/codes; a new report does not convert all arrears into 2026 earnings. Interest, penalties and account offsets need current procedural authority. [PIT Article 60k][pit]; [contribution Article 29b][social]; [IOPPD Article 8][ioppd]

The authority's January 2026 IRMS transition notice identifies the new service; period-specific extensions do not create a recurring filing or payment extension. Current portal code validations, authorisation, late/corrected report behaviour and payment accounts have not been tested here. [Authority notice][irms]

## Sanctions and reviewer handoff

Article 53a(1) lists payer withholding/payment/reporting failures, with legal-person fine EUR 2,000–20,000 and responsible-person fine 500–1,000. Article 53v contains separate individual offences and range 500–2,000. These are specified offences, not an automatic assessment for every discrepancy. Article 53 refers other procedural matters to tax procedure; current interest, appeal/stay and enforcement methods are not completed here. [PIT Articles 53–53v][pit]

Handoff: contract/payroll register; receipt classification and benefit valuations; all payers and insurance periods; legal wage/floor/status/relief evidence; current municipal decision; statutory calculations and cents reconciliation; code/period mapping; original/full replacement reports and acknowledgements; payment/authority/local ledgers; annual statement and any personal return/assessment; current-law/source dates.

Remaining: complete current municipal decisions/situs and local forms; wage/collective-agreement floors and entitlement calculations; exact benefit/expense and relief implementation; current disability statistical-series/status/quota exceptions and Chamber membership/artisan/craft dues, union and other levy applicability; full 2026 reporting-code amendments and contradictions; actual IRMS schema/acknowledgement/corrections; historical award and procedural methods; foreign/treaty/coverage cases; independent country review and named accountant attestation. The companion individual-tax Guide has now been rebuilt, but its documented form/specialist/procedure limits remain; it does not establish missing payroll implementation.

## Sources

Read on **24 October 2026**: targeted PIT Articles 3–5a, 10, 12–16, 32c–32d, 42–47, 53–53v and 60k; actual 160/25 provisions relevant to payroll; actual 70/26 Articles 1–3; employment instruction; IOPPD rule/instructions/code list; selected official workbook rows; local-finance Articles 8–9 and Bar ordinance. January 2027 salary proposal visually read, not certified as enacted. Historic Ministry example used only for gross/net/prirez allocation. Current taxpayer facts/accepted filings were not obtained.

[pit]: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0
[amend]: https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0
[may]: https://www.sluzbenilist.me/propisi/394390/download
[instruction]: https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0
[social]: https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0
[ioppd]: https://wapi.gov.me/download/28aa7760-8d39-440d-8874-1ffcc5773095?version=1.0
[codes]: https://wapi.gov.me/download/5cb52f80-2fcc-4f77-8111-07ea8b6d8ff1?version=1.0
[local]: https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0
[bar]: https://investin.bar.me/wp-content/uploads/2024/08/Odluka-o-prirezu-porezu-na-dohodak-fizickih-lica.pdf
[example]: https://wapi.gov.me/download/f1efb281-21a8-4c03-a2ae-d6ea5c608e93?version=1.0
[proposal]: https://wapi.gov.me/download/58f7f48c-33de-4ec0-a1f4-28fd16fc7fb6?version=1.0
[chamber]: https://www.sluzbenilist.me/propisi/389055/download
[artisan]: https://www.ul-gov.me/me/aktuelnosti/prijava-u-registar-zanatlija
[disability]: https://www.zzzcg.me/wp-content/uploads/2018/01/Zakon-o-profesionalnoj-rehabilitaciji-i.pdf
[disability-amend]: https://www.sluzbenilist.me/propisi/385768/download
[deferral]: https://www.sluzbenilist.me/propisi/395547/download
[disability-agency]: https://www.zzzcg.me/programi/zaposljavanje-lica-sa-invaliditetom/
[irms]: https://www.gov.me/clanak/vazno-obavjestenje-u-vezi-sa-pocetkom-primjene-novog-integrisanog-it-sistema-poreske-uprave-irms

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax adviser in Montenegro) before implementation.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
