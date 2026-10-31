---
name: iceland-social-contributions
description: >
  Iceland 2026 employer social levy (tryggingagjald), mandatory occupational
  pension, contribution bases, self-employed calculated remuneration,
  filing, separate pension deadlines and A1 evidence. Use for payroll social
  costs, pension deductions, employer pension, seamen and contribution
  remittance reconciliation. Includes source conflicts and recomputable cases.
version: 0.7
jurisdiction: IS
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland social contributions and mandatory pension v0.7

Tax year 2026, amounts in ISK. This method separates the employer levy, employee pension and employer pension, and produces contribution workpapers. General reference only: check the facts of each case against the cited law. The [payroll skill](iceland-payroll.md) handles income-tax withholding and net pay. The linked statutes are Alþingi's 1 October 2026 compilation (158a).

## Who this applies to

The levy applies to employers paying or calculating taxable remuneration, including individuals, companies, public bodies, foreign contractors and self-employed people. Intermediaries handling wage payments have reporting/payment responsibilities. An owner-manager's calculated remuneration is included. Check any statutory exemption before calculating. [Act 113/1990, Articles 4–6](https://www.althingi.is/lagas/nuna/1990113.html)

Employees and self-employed people must acquire occupational pension rights from age 16 until 70. The 2026 employer notice states that no employee or employer contribution is paid for an employee aged 70 or over, and that children aged 15 or younger do not pay into a pension fund. Determine the actual applicable special law, collective agreement, employment contract and fund before selecting the contribution split. The statutory minimum total does not itself prescribe one universal employer/employee split. [Act 129/1997, Articles 1–3](https://www.althingi.is/lagas/nuna/1997129.html), [2026 employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

Self-employment requires a supported calculated-remuneration determination, not an arbitrary percentage of turnover or drawings. Use the current occupational category, working time and facts; carry that determination into both the contribution and income-tax workpapers. [Income Tax Act, Article 58](https://www.althingi.is/lagas/nuna/2003090.html) and [2026 calculated-remuneration guidance](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026)

## Rates, bands and thresholds

| Item | Amount / boundary | Period and conditions | Official source |
| --- | --- | --- | --- |
| General aggregate payroll levy | 6.35% | 2026 ordinary base; this includes the following four components, not four additions to 6.35%. | [2026 employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |
| General component | 4.90% | 2026 | [Act 113/1990, Article 2](https://www.althingi.is/lagas/nuna/1990113.html) |
| Employment-insurance component | 1.35% | 2026 | [2026 employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |
| Wage-guarantee fund and market fees | 0.05% each | 2026; already included in aggregate | [2026 employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |
| Fishing-vessel seamen's additional insurance | 0.65 percentage points; aggregate 7.00% | 2026 where the additional insurance applies; annual guidance provides for an operator that has cancelled this insurance. Obtain the applicable insurance evidence. | [2026 employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf), [annual reporting guidance](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/) |
| Mandatory pension total | At least 15.5% | Employees and self-employed people alike; current law; transitional 12% only where the qualifying current collective agreement still provides it, until a new agreement takes effect | [Act 129/1997, Article 2 and transitional provision V](https://www.althingi.is/lagas/nuna/1997129.html) |
| Ordinary payroll illustration | Employee 4%; employer adjustable default 11.5% | 2026 employer instructions; confirm actual terms rather than imposing this split | [2026 employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |
| Mandatory pension age | From 16 until 70 | Employer notice: no contributions for an employee aged 70 or over; none for children aged 15 or younger. Fund/contract terms and date-of-birth records control the actual payroll period | [Act 129/1997, Article 1](https://www.althingi.is/lagas/nuna/1997129.html), [2026 employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |
| Employee income-tax deduction | Up to 4% mandatory plus a separate up to 4% qualifying additional contribution | Contributions paid regularly to eligible recipients; these limits do not create an employer matching obligation | [Income Tax Act, Article 30(A)(4)–(5)](https://www.althingi.is/lagas/nuna/2003090.html) |
| Employer pension income-tax boundary | 12% of contribution base plus 2,000,000 a year | Article 28(5), subject to the collective-agreement/statutory exception below | [Income Tax Act, Article 28(5)](https://www.althingi.is/lagas/nuna/2003090.html) |
| Self-employed annual levy-base floor | 748,224 | Whole-year Article 6(3) floor for full-time work; not a replacement for a higher properly calculated remuneration base | [Act 113/1990, Article 6](https://www.althingi.is/lagas/nuna/1990113.html) |
| Small-payroll payment exception | Average below 42,000 monthly; annual 504,000 trigger (annual filing where the year's total does not reach 504,000) | Apply Article 15 conditions, not a general exemption from liability | [Act 113/1990, Article 15](https://www.althingi.is/lagas/nuna/1990113.html) |
| A1 reduced levy | No 2026 rate published (see Not yet confirmed) | Authority page gives 0.425% for wage years 2014–2023 and 0.293% for 2024 and 2025 only; without a valid A1 certificate the full levy applies | [A1 administrative guidance](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) |

The general levy has no contribution ceiling in Articles 6–8. Do not truncate its base at a pension-income, income-tax or foreign-social-security ceiling. [Act 113/1990](https://www.althingi.is/lagas/nuna/1990113.html)

## The base

### 1. Establish separate bases

**Levy.** Start with taxable work remuneration, including bonus, holiday pay, taxable benefits and owner-manager remuneration. Include employer pension contributions under Article 7(1). Employee pension withholding does not reduce this employer base. Benefits use the authority's tax valuation, with market value for other benefits. Vehicle allowances and per diems need their specific statutory treatment, not one blanket reimbursement exemption. [Act 113/1990, Articles 6–8](https://www.althingi.is/lagas/nuna/1990113.html)

Article 9 excludes specified pensions, social benefits, insured accident compensation, unemployment benefits and other named payments. Match the legal payment category to the underlying statement before excluding it. A bank reference containing “pension” does not establish whether the payment is a pension contribution, a benefit or a wage cost. [Act 113/1990, Article 9](https://www.althingi.is/lagas/nuna/1990113.html)

**Pension.** Article 3 uses remuneration for work, but excludes benefits paid in kind (for example clothing, food and housing) and reimbursements of incurred costs (for example vehicle allowances, per diems and meal money). Pension and levy bases therefore differ. The pension statute also excludes specified benefits and includes unemployment benefits; do not copy the levy-exemption list into the pension calculation. [Act 129/1997, Article 3](https://www.althingi.is/lagas/nuna/1997129.html)

For the stated 2026 car, food, housing and other benefit valuations, use the [payroll skill's benefit workpaper](iceland-payroll.md). Carry the supported tax value into the levy base under Article 8, while testing the statutory minimum pension exclusion and actual contractual base separately. The car/payroll example demonstrates this split; the benefit's noncash tax value is not a second cash wage or proof of the employer's actual benefit cost. [Levy Act, Articles 7–8](https://www.althingi.is/lagas/nuna/1990113.html); [Pension Act, Article 3](https://www.althingi.is/lagas/nuna/1997129.html)

### 2. Calculate ordinary contributions

For a documented ordinary arrangement at employee 4% and employer 11.5%, without other contributions or sector charges:

```text
employee pension = established pension base × 4%
employer pension = established pension base × 11.5%
levy base = remuneration and benefits within levy scope + employer pension
levy = established levy base × 6.35%
employer social cost = employer pension + levy
pension fund remittance = employee pension + employer pension
```

The levy is an employer cost, not a deduction from employee pay. The employee contribution is withheld from pay and remitted with the employer contribution to the pension provider. Income-tax withholding goes to Skatturinn separately. [Act 113/1990, Articles 4, 7 and 10](https://www.althingi.is/lagas/nuna/1990113.html), [Act 129/1997, Article 7](https://www.althingi.is/lagas/nuna/1997129.html)

At these assumed rates, employer social cost is **18.58025% of cash wages**, not 17.85%: 11.5% + (100% + 11.5%) × 6.35%. This is an illustration, not a universal total employment-cost rate. Other contractual, insurance, holiday, benefit or sector charges require their own evidence. For financial-services employers, use the [corporate skill's financial-sector method](is-corporate-income-tax.md) to screen and compute the separate remuneration tax, including its employer-pension base and statutory exclusions. The ordinary cost illustration above does not include that charge. [Act 165/2011, Articles 2–6](https://www.althingi.is/lagas/nuna/2011165.html)

### 3. Additional contributions and income-tax treatment

Record supplementary contributions from the actual agreement and fund instructions. A different recipient, a private-pension label or the income-tax deduction ceiling does not alone prove an automatic additional employer 2% obligation. The pension statute allows additional protection agreements; identify the governing terms before adding a match. Skatturinn describes supplementary pension savings (viðbótarlífeyrissparnaður) as a 4% employee contribution with a 2% employer contribution; whether the 2% employer part is owed comes from the applicable collective agreement or contract, not from Act 129/1997. [Act 129/1997, Articles 2 and 8–10](https://www.althingi.is/lagas/nuna/1997129.html), [withholding 2026](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026)

Article 28(5) of the Income Tax Act frames the employer-contribution tax boundary as **12% of the base plus 2,000,000 a year**. It is not the lower of those amounts and not two independent limits. Contributions provided by collective agreement or fixed by law are expressly excluded from taxable income. Establish the contractual/statutory category before computing any taxable excess; an exceptional contribution needs its own legal workpaper. Example: a voluntary employer contribution of 14% on annual remuneration of 2,500,000 is 350,000; the boundary is 12% × 2,500,000 + 2,000,000 = 2,300,000, so no part of it is taxable to the employee. [Income Tax Act, Article 28(5)](https://www.althingi.is/lagas/nuna/2003090.html)

For self-employed people, establish remuneration and the applicable pension arrangement first. The self-employed person pays the whole statutory minimum of 15.5% on the own-remuneration base (Act 129/1997, Articles 1–3): the personal part (deductible up to 4%, plus up to 4% supplementary, under Income Tax Act Article 30(A)(5)) and the remainder as the counter-contribution on own remuneration, which is entered on RSK 4.05 and forms part of the levy base with the remuneration. Reconcile the personal and business pension components and include the applicable employer pension in the levy base. Deduct supported business payroll costs and the eligible personal pension separately, without deducting the same contribution twice. [Act 129/1997, Articles 1–3](https://www.althingi.is/lagas/nuna/1997129.html), [Act 113/1990, Article 7](https://www.althingi.is/lagas/nuna/1990113.html), [Income Tax Act, Articles 30–31](https://www.althingi.is/lagas/nuna/2003090.html), [starting a business: counter-contribution on RSK 4.05](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)

## Deadlines and filing

| Obligation | Method and deadline | Official source |
| --- | --- | --- |
| Monthly levy | Calendar-month period; due first of following month, final due date 14 days later. Reconcile current calendar/claim for non-working days. Submit with payroll reporting through the taxpayer service or supported software. | [Act 113/1990, Article 10](https://www.althingi.is/lagas/nuna/1990113.html), [2026 employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |
| Pension | Contribution period no longer than a month; due tenth of following month, final due date the last day of that month. Pay the fund/provider, not the tax authority; also check fund rules and agreement. | [Act 129/1997, Article 7](https://www.althingi.is/lagas/nuna/1997129.html) |
| Small-payroll exception | Where Article 15 applies, first report/pay when combined annual remuneration/wages reaches 504,000, then each due date. If below 504,000 for the year, one annual settlement treated as December is permitted. | [Act 113/1990, Article 15](https://www.althingi.is/lagas/nuna/1990113.html) |
| Annual levy reconciliation | File the required wage information and reconcile assessed levy to monthly reporting and payments. Legal entities use their applicable electronic tax return; sole-trader reconciliation uses the appropriate personal/business schedules. Annual return instructions labelled 2026 relate to 2025 wages, not a published 2027 deadline. | [Act 113/1990, Article 12](https://www.althingi.is/lagas/nuna/1990113.html), [annual wage-return guidance](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/) |
| Levy outside withholding | Article 12(6): due 1 June for individuals and 1 November for legal entities, final due date one month later; Article 16 runs default interest from those due dates. | [Act 113/1990, Articles 12 and 16](https://www.althingi.is/lagas/nuna/1990113.html) |

**Out-of-date authority pages.** The general levy page says 1 July for payments outside withholding; the collections page says 1 June for individuals and 1 October for legal entities. Current Article 12(6) says 1 June and 1 November, and the statute governs. Normal taxable benefits remain in monthly reporting. [Levy page](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald), [collections page](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/), [Act 113/1990](https://www.althingi.is/lagas/nuna/1990113.html)

Each payroll period needs: wage/benefit components, separate pension and levy bases, employee and employer pension, levy category, filed return and acceptance, payment claim, bank settlement and fund allocation. Match all of them to the ledger. The broadcasting fee (útvarpsgjald) and the Senior Citizens' Construction Fund fee are per-person charges assessed with income tax, not social contributions; the [income tax skill](iceland-income-tax.md) covers them. A bank debit to SKATTURINN/RSK can bundle several liabilities; split it from the return/account statement. A fund debit (for example Gildi, LSR or Birta) needs its contribution statement; a name match alone does not prove pension cost, period or payment allocation. Unmatched amounts remain a reconciliation difference, not an assumed deductible expense.

## Penalties and interest

**Do not apply the PAYE daily surcharge to the levy.** Act 113/1990 Article 10 expressly excludes the 1%-per-day surcharge in Act 45/1987 Article 28(2)(1). If monthly levy remains unpaid at the final due date, default interest runs from the first due date. The authority's collections guidance also states that no surcharge is calculated on this levy. [Act 113/1990, Articles 10–11](https://www.althingi.is/lagas/nuna/1990113.html), [collection rules](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/)

Missing or deficient reports can lead to estimates, collection and other statutory sanctions. Annual assessment/reassessment procedures use the Income Tax Act where applicable; keep a separate analysis for an assessment-base surcharge or offence, rather than treating the monthly levy exclusion as immunity from all sanctions. [Act 113/1990, Articles 11 and 14](https://www.althingi.is/lagas/nuna/1990113.html)

Pension contributions have their own due dates and provider collection rules. Obtain the fund statement and applicable rules for pension arrears; do not import the tax authority's daily surcharge into a pension calculation. A quantified default-interest calculation needs the dated rate, principal, statutory starting date, payment allocation and applicable collection method. This skill does not fix a variable interest rate. [Act 129/1997, Article 7](https://www.althingi.is/lagas/nuna/1997129.html)

## Cross-border points

Social-security coverage, pension coverage and income-tax residence are distinct determinations. Skatturinn applies a reduced levy to EEA nationals hired for a year or less whose employer presents an A1 certificate issued by the home state showing the worker stays insured there; retain the certificate, authority, named worker and covered dates. Without a valid A1 for the dates, the full levy applies. The authority's A1 table gives 0.425% for wage years 2014 to 2023 and 0.293% for 2024 and 2025, and has no 2026 rate. **No 2026 reduced levy is computed here.** Report qualifying non-Iceland-insured remuneration separately. [A1 guidance](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald), [annual reporting guidance](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/)

The statute behind the historical rates: Act 113/1990, Article 3(2)(4) allocates 0.325% of the levy base to pension-fund disability equalisation, and transitional provision III lowered that allocation to 0.193% for 2024 and 2025 only. The authority has not published how this applies to A1 workers for 2026, so the 2026 A1 rate stays on the "Not yet confirmed" line. [Act 113/1990, Article 3 and transitional III](https://www.althingi.is/lagas/nuna/1990113.html), [2026 fee components](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

For outbound work, Article 7(5) includes remuneration paid by Icelandic parties to Iceland-domiciled people for work abroad. Do not exclude it solely because the workdays are foreign. A social-security agreement, coverage determination and occupational pension treatment must be considered for the actual countries and dates before calculating a final cross-border result. The [cross-border skill](is-cross-border.md) supplies income-tax screening, not a substitute coverage decision. [Act 113/1990, Article 7](https://www.althingi.is/lagas/nuna/1990113.html)

## Worked examples

Hypothetical ordinary arrangements below assume confirmed pension bases and a documented 4% employee / 11.5% employer split. Exact decimal results validate arithmetic; follow the accepted service/fund rounding for actual reporting. None proves benefit classification or a foreign exemption.

### 1. Ordinary monthly cash wages

Cash wages 600,000 produce employee pension 24,000 and employer pension 69,000. The levy base is **669,000**, not 600,000; levy is **42,481.50**. Employer pension plus levy is **111,481.50**; total employer wage/contribution cost is **711,481.50**. Pension remittance is **93,000**. The authority's example rounds levy to 42,482; preserve that reporting result separately from this decimal control. [2026 employer example](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

```oa-check
name: Iceland ordinary monthly pension and levy, 2026
inputs:
  cash_wages: 600000
steps:
  - employee_pension: cash_wages * 0.04
  - employer_pension: cash_wages * 0.115
  - levy_base: cash_wages + employer_pension
  - levy: levy_base * 0.0635
  - employer_social_cost: employer_pension + levy
  - employer_total: cash_wages + employer_social_cost
  - fund_remittance: employee_pension + employer_pension
expected:
  employee_pension: 24000
  employer_pension: 69000
  levy_base: 669000
  levy: 42481.50
  employer_social_cost: 111481.50
  employer_total: 711481.50
  fund_remittance: 93000
```

### 2. Taxable benefit with a different pension base

Cash wages 400,000 plus an already correctly valued taxable in-kind benefit of 20,000: assume that benefit falls within the Article 3 pension exclusion and Article 8 levy inclusion. Pension stays on 400,000: employee 16,000, employer 46,000. Levy base becomes **466,000**, levy **29,591**. This is not a claim that the benefit's actual employer cost equals its tax valuation. [Act 129/1997, Article 3](https://www.althingi.is/lagas/nuna/1997129.html), [Act 113/1990, Articles 7–8](https://www.althingi.is/lagas/nuna/1990113.html)

```oa-check
name: Iceland in-kind benefit separates pension and levy bases
inputs:
  cash_wages: 400000
  taxable_benefit: 20000
steps:
  - employee_pension: cash_wages * 0.04
  - employer_pension: cash_wages * 0.115
  - levy_base: cash_wages + taxable_benefit + employer_pension
  - levy: levy_base * 0.0635
  - fund_remittance: employee_pension + employer_pension
expected:
  employee_pension: 16000
  employer_pension: 46000
  levy_base: 466000
  levy: 29591
  fund_remittance: 62000
```

### 3. Self-employed remuneration and a short bank payment

For established monthly remuneration 1,000,000 and documented pension components 40,000 personal plus 115,000 business/employer, levy base is 1,115,000 and levy **70,802.50**. Total pension plus levy is **225,802.50**. If supported statements show only 217,500 paid against these liabilities, the unresolved difference is **8,302.50**; it is not assumed rounding, waived liability or an extra expense. Classify and reconcile each recipient before concluding what is unpaid. [Act 113/1990, Articles 6–7](https://www.althingi.is/lagas/nuna/1990113.html), [Act 129/1997, Article 3](https://www.althingi.is/lagas/nuna/1997129.html)

```oa-check
name: Iceland self-employed contribution reconciliation
inputs:
  remuneration: 1000000
  statement_payments: 217500
steps:
  - personal_pension: remuneration * 0.04
  - employer_pension: remuneration * 0.115
  - levy: (remuneration + employer_pension) * 0.0635
  - contributions: personal_pension + employer_pension + levy
  - difference: contributions - statement_payments
expected:
  personal_pension: 40000
  employer_pension: 115000
  levy: 70802.50
  contributions: 225802.50
  difference: 8302.50
```

## Ask the client first

- Which payer, worker, dates, age, work locations and employment/self-employment classification apply?
- Which contract, collective agreement, fund and pension components govern, including any supplementary contribution or transitional arrangement?
- What cash wages, benefits, reimbursements, calculated remuneration and exclusions are supported by source records?
- Does a valid foreign-coverage/A1 determination cover these exact dates, and what current levy decision applies?
- What returns, assessments, bank/fund statements, corrections and arrears reconcile to the period's liabilities?

**When to refer.** Refer A1 and coordination cases, fund contract and arrears disputes, complex benefit classification and sector cases outside the stated financial-sector workpaper. Do not reuse the historical 0.425% A1 rate or the former wages-only cost percentages (17.85% / 21.85%) for a 2026 result.

<!-- openaccountants-cta-block -->

## Talk to an accountant

For advice on your facts, [contact OpenAccountants](https://www.openaccountants.com/contact).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Social Security Levy Act 113/1990, Articles 1–16 and transitional III (components 4.90% / 1.35%, base, floor 748,224, exclusions, monthly and annual collection, 42,000 / 504,000) | https://www.althingi.is/lagas/nuna/1990113.html | 2026-10-30 |
| Mandatory Pension Act 129/1997, Articles 1–3, 7–10 and transitional V (15.5%, ages 16 to 70, base, due dates) | https://www.althingi.is/lagas/nuna/1997129.html | 2026-10-30 |
| Income Tax Act 90/2003, Articles 28(5), 30(A)(4)–(5), 31 and 58 | https://www.althingi.is/lagas/nuna/2003090.html | 2026-10-30 |
| Skatturinn, employer notice RSK 6.01 no. 1/2026 (rates, 11.5% default, ages, 600,000 example) | https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf | 2026-10-30 |
| Skatturinn, withholding 2026 (levy breakdown, pension deduction, supplementary pension 4% / 2%) | https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026 | 2026-10-30 |
| Skatturinn, social security levy (tryggingagjald): A1 rates by year, 1 July date | https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald | 2026-10-30 |
| Skatturinn, collection of all taxes and duties (no surcharge on the levy, 1 October date) | https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/ | 2026-10-30 |
| Skatturinn, wage slips and annual wage return (launamiðar og launaframtal) | https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/ | 2026-10-30 |
| Skatturinn, starting a business (counter-contribution on own remuneration, RSK 4.05) | https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/ | 2026-10-30 |
| Skatturinn, calculated remuneration 2026 (reiknað endurgjald) | https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026 | 2026-10-30 |
| Financial Activities Tax Act 165/2011, Articles 2–6 | https://www.althingi.is/lagas/nuna/2011165.html | 2026-10-23 |

Not yet confirmed: the reduced levy rate for A1-certificate workers for 2026; whether a 2% employer match on supplementary pension savings, or an extra 2% employer contribution where the employee chooses another pension fund, is owed in a given case (set by collective agreements, not by statute); the old version's statements that Iceland has no statutory minimum wage and that collective agreements set wage floors (not checked against an official source).
