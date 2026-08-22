---
name: estonia-social-contributions
description: Use this skill whenever asked about Estonian social security contributions, social tax (sotsiaalmaks), unemployment insurance premiums (töötuskindlustusmakse), or mandatory funded pension (II-pillar / kogumispension) for employers, employees, board members, or self-employed (FIE). Trigger on phrases like "how much social tax do I pay in Estonia", "Estonian payroll on-cost", "sotsiaalmaks 33%", "employer cost above gross", "II pillar pension contribution", "unemployment insurance premium", "minimum social tax base", "Form TSD", "FIE social tax", "Estonia net salary calculation", "what is the employer cost on top of salary", or any question about Estonian social charges. Also trigger when classifying bank-statement transactions that relate to EMTA (Maksu- ja Tolliamet) tax payments, Töötukassa unemployment premiums, or II-pillar pension transfers from Estonian banks (Swedbank, SEB, LHV, Luminor). Also trigger when computing Estonian payroll where the 22% flat income tax, the basic exemption (maksuvaba tulu), and the social tax floor interact. This skill covers social tax (33%), unemployment insurance (employee 1.6% + employer 0.8%), II-pillar funded pension (2/4/6%), the minimum monthly social tax base, the 22% flat PIT, the basic exemption, Form TSD filing, FIE advance payments, bank-statement classification patterns, and edge cases. ALWAYS read this skill before touching any Estonian social-contribution or payroll-charge work.
version: 0.1
jurisdiction: EE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia Social Security Contributions (Social Tax, Unemployment Insurance, II-Pillar Pension)

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Estonia (Republic of Estonia) |
| Primary Legislation | Social Tax Act (Sotsiaalmaksuseadus) |
| Supporting Legislation | Unemployment Insurance Act (Töötuskindlustuse seadus); Funded Pensions Act (Kogumispensionide seadus); Income Tax Act (Tulumaksuseadus) |
| Tax Authority | Estonian Tax and Customs Board (Maksu- ja Tolliamet, EMTA) -- emta.ee |
| Other administrators | Estonian Unemployment Insurance Fund (Töötukassa); II-pillar registrar (Pensionikeskus) |
| Currency | EUR only |
| Social tax (sotsiaalmaks) | 33% (employer-paid, ON TOP of gross), 20pp pension + 13pp health [EMTA tax-rates] |
| Employer unemployment insurance | 0.8% of gross payroll [EMTA tax-rates] |
| Employee unemployment insurance | 1.6% of gross (withheld) [EMTA tax-rates] |
| Mandatory funded pension (II pillar) | Employee 2% / 4% / 6% (default 2%) (withheld) [EMTA tax-rates; PwC] |
| Personal income tax (PIT) | 22% flat, 2025 and 2026 [EMTA tax-rates] |
| Min monthly social tax base 2025 | EUR 820/month => min social tax EUR 270.60/month [EMTA tax-rates] |
| Min monthly social tax base 2026 | EUR 886/month => min social tax EUR 292.38/month [EMTA tax-rates] |
| Total employer on-cost above gross | 33.8% (33% social tax + 0.8% employer unemployment) [EMTA tax-rates] |
| Filing / payment frequency | Monthly (Form TSD) |
| Filing/payment deadline | By the 10th of the month following payment [EMTA social-tax] |
| Validated by | Pending -- requires sign-off by an Estonian tax adviser / vandeaudiitor |
| Validation date | Pending |

**Read this whole section before computing or classifying anything.**

**Contribution overview (employment relationship)**  _(Source for all rows: EMTA tax-rates page (https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates); II-pillar default and rates also per PwC Worldwide Tax Summaries (https://taxsummaries.pwc.com/estonia/individual/other-taxes).)_

| Charge | Who pays | Rate | Withheld or on-top |
| --- | --- | --- | --- |
| Social tax (sotsiaalmaks) | Employer | 33% | ON TOP of gross |
| Unemployment insurance -- employer | Employer | 0.8% | ON TOP of gross |
| Unemployment insurance -- employee | Employee | 1.6% | Withheld from gross |
| Funded pension II pillar -- employee | Employee | 2% / 4% / 6% (default 2%) | Withheld from gross |
| Income tax (tulumaks) | Employee | 22% flat | Withheld from gross |

**Side totals (sanity check):**

- Total employer on-cost = 33% + 0.8% = **33.8%** of gross. [EMTA tax-rates]
- Total employee withholdings = 22% income tax (on income above basic exemption) + 1.6% unemployment + 2/4/6% funded pension. [EMTA tax-rates]

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown II-pillar membership | Assume the statutory default rate of 2% if the person is a member; if membership unknown, STOP and ask (mandatory for residents born after 31 Dec 1982) [EMTA tax-rates; PwC] |
| Unknown total employer cost | Compute as gross x 1.338, subject to the monthly minimum social tax base [EMTA tax-rates] |
| Unknown whether basic exemption applies | Apply the monthly basic exemption ONLY if the employee filed an application with the employer; otherwise withhold PIT on the full taxable amount [EMTA private-client] |
| Unknown tax year | Use 2025 figures; note 2026 changes (flat EUR 700 exemption, EUR 886 social-tax floor) [EMTA tax-rates] |
| Unknown whether person is of pensionable age | Ask -- pensioners are exempt from the 1.6% employee unemployment withholding [EMTA tax-rates] |
| Unknown employment status (employee vs FIE) | Ask -- FIE social tax is computed and paid differently (quarterly advances) [EMTA social-tax] |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- gross monthly remuneration, tax year, and II-pillar membership status (Y/N, and chosen rate if known). Without II-pillar membership status, STOP for employee net-pay computations -- the employee withholding cannot be fixed without it.

**Recommended** -- whether the employee filed a basic-exemption application with the employer, the employee's age band (pensionable age affects unemployment-premium liability), and whether the person is an employee, board member, or FIE.

**Ideal** -- the EMTA TSD declarations for the period, payslips, and bank statements showing EMTA/Töötukassa debits and net-salary credits.

### Refusal catalogue

- **R-EE-SOC-1** — II-pillar membership unknown. Trigger: employee net-pay or withholding computation requested without knowing whether the person is a funded-pension (II-pillar) member or their chosen rate. Message: "The mandatory funded pension contribution is 2%, 4% or 6% (default 2%) for II-pillar members, and zero for non-members. Net pay cannot be computed without confirming membership and the elected rate. Membership is mandatory for residents born after 31 December 1982."  _(EMTA tax-rates; PwC)_
- **R-EE-SOC-2** — Cross-border / posted workers and A1 certificates. Trigger: employee works in more than one EU/EEA state, is posted abroad, or holds an A1 certificate. Message: "Where social-security liability arises is governed by EU Regulation 883/2004 and any A1 certificate, not by this skill. Do not apply Estonian social tax without confirming the applicable legislation. Escalate to a qualified Estonian tax adviser."  _(RESEARCH GAP -- reviewer to confirm coordination treatment)_
- **R-EE-SOC-3** — FIE arrears / reducing circumstances. Trigger: sole proprietor (FIE) with unpaid social tax advances, or claims to a reduced minimum (part-time, receiving a pension, first-year, etc.). Message: "FIE social tax minimums and reducing circumstances are case-specific. Do not quantify FIE social tax or arrears without the EMTA assessment. Escalate to a qualified Estonian tax adviser."  _(EMTA social-tax)_
- **R-EE-SOC-4** — Fringe benefits and special remuneration. Trigger: the package includes fringe benefits (erisoodustus), stock options, or in-kind benefits. Message: "Fringe benefits attract income tax AND social tax on the grossed-up value (benefit + income tax thereon), declared on Form TSD annexes by the employer. This grossing-up is outside the simple wage formula in this skill. Escalate to a qualified Estonian tax adviser."  _(EMTA social-tax)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank-statement transactions related to Estonian social charges and payroll taxes. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Estonian social tax, unemployment premiums, withheld income tax and funded-pension contributions are remitted together to EMTA on Form TSD -- a single EMTA debit usually covers all of them. These are statutory payroll obligations, not VAT-bearing supplies, so they EXCLUDE from any VAT return classification.

### 3.1 EMTA consolidated payroll-tax debits (TSD liability)

**EMTA consolidated payroll-tax debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MAKSU- JA TOLLIAMET, MAKSUAMET, EMTA | EXCLUDE -- payroll tax remittance | Combined TSD liability (income tax + social tax + unemployment + pension) |
| SOTSIAALMAKS, SOCIAL TAX | EXCLUDE -- social tax | Employer 33% social tax |
| TSD, TSD DEKLARATSIOON | EXCLUDE -- TSD payroll tax | Monthly declaration liability |
| TULUMAKS, INCOME TAX (outgoing) | EXCLUDE -- withheld income tax | 22% PIT remitted to EMTA |
| EE_______________ (EMTA reference acc.) | EXCLUDE -- EMTA tax account top-up | Estonia uses a single EMTA prepayment account |

### 3.2 Unemployment insurance and pension references

**Unemployment insurance and pension references**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TÖÖTUSKINDLUSTUSMAKSE | EXCLUDE -- unemployment insurance premium | Employee 1.6% + employer 0.8% |
| TÖÖTUKASSA | EXCLUDE -- unemployment insurance fund | Usually flows via EMTA TSD, not direct |
| KOGUMISPENSION, II SAMBA, II PILLAR | EXCLUDE -- funded pension contribution | Employee 2/4/6%, remitted via EMTA |
| PENSIONIKESKUS | EXCLUDE -- II-pillar registrar | Pension contribution routing |

### 3.3 Debits that are NOT social contributions (do not confuse)

**Debits that are NOT social contributions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KÄIBEMAKS, KMD, VAT | EXCLUDE -- VAT, not social | Value-added tax (standard rate 24% from 1 Jul 2025) [koda.ee] |
| TULUMAKS (corporate distribution) | EXCLUDE -- corporate income tax on distribution (22/78) | CIT is independent of social tax [key rules] |
| FIE ETTEMAKS, FIE AVANSS | EXCLUDE -- FIE social-tax advance | Self-employed quarterly advance, not employee payroll |

### 3.4 Salary and net-pay movements (exclude from social classification)

**Salary and net-pay movements**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PALK, NETOPALK, SALARY (outgoing) | EXCLUDE -- payroll expense (net pay) | Net salary paid to employee, not a contribution |
| PALK, SALARY (incoming) | EXCLUDE -- employment income received | Not a contribution |
| TÖÖTASU, JUHATUSE LIIKME TASU | EXCLUDE -- wages / board fee | Gross remuneration line |

### 3.5 Benefits received (not contributions)

**Benefits received**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION, VANADUSPENSION | EXCLUDE -- pension income received | Benefit, not a contribution paid |
| HAIGUSHÜVITIS, TÖÖTUSHÜVITIS | EXCLUDE -- sickness / unemployment benefit received | Inbound benefit, not a contribution |

## Section 4 -- Worked examples

Six bank-statement / payroll classifications for a hypothetical Estonian OÜ (private limited company) and its staff. All amounts in EUR. Net-pay arithmetic uses the Estonian base: income tax is charged on gross minus the employee unemployment premium, minus the employee funded-pension contribution, minus the applicable monthly basic exemption.

### Example 1 -- Standard salary, II-pillar member at 2% (2026)

**Input line:**
`05.02.2026 ; NETOPALK VEEBRUAR ; DEBIT ; J. TAMM PALK ; -1,657.84 ; EUR`

**Reasoning:**
Gross EUR 2,000/month; employee is an II-pillar member at the default 2%; basic-exemption application on file (2026 flat EUR 700/month). [EMTA tax-rates]
- Employee unemployment 1.6%: 2,000 x 1.6% = **32.00**
- Employee funded pension 2%: 2,000 x 2% = **40.00**
- PIT base: 2,000 - 32.00 - 40.00 - 700.00 = **1,228.00**
- Income tax 22%: 1,228.00 x 22% = **270.16**
- Net pay: 2,000.00 - 32.00 - 40.00 - 270.16 = **1,657.84** -> matches the debit.

Employer side (not in the net-pay debit): social tax 2,000 x 33% = 660.00; employer unemployment 2,000 x 0.8% = 16.00; total employer cost = 2,000 x 1.338 = **2,676.00**. [EMTA tax-rates]

**Classification:** EXCLUDE -- net salary (payroll expense). The EMTA TSD remittance covering income tax, social tax, unemployment and pension is a separate debit (see Example 3).

### Example 2 -- Minimum-wage earner, NOT an II-pillar member (2025)

**Input line:**
`07.03.2025 ; PALK ; DEBIT ; MIINIMUMPALK VEEBR ; -823.90 ; EUR`

**Reasoning:**
Gross EUR 886/month (2025 national minimum wage); employee born before 1983 and not an II-pillar member (no pension withholding); basic-exemption application on file. Annual income approx EUR 10,632 is below EUR 14,400, so the 2025 basic exemption is the full EUR 654/month. [EMTA tax-rates; palgakalkulaator.ee]
- Employee unemployment 1.6%: 886 x 1.6% = **14.18** (14.176 rounded)
- Funded pension: **0.00** (not a member)
- PIT base: 886.00 - 14.18 - 654.00 = **217.82**
- Income tax 22%: 217.82 x 22% = **47.92** (47.9204 rounded)
- Net pay: 886.00 - 14.18 - 47.92 = **823.90** -> matches the debit.

Employer side: social tax 886 x 33% = 292.38 (here the actual base 886 exceeds the 2025 floor of 820, so the EUR 270.60 minimum does not bind); employer unemployment 886 x 0.8% = 7.09; total employer cost = 886 x 1.338 = **1,185.47**. [EMTA tax-rates]

**Classification:** EXCLUDE -- net salary (payroll expense).

### Example 3 -- Consolidated EMTA payroll-tax remittance (TSD)

**Input line:**
`10.03.2026 ; MAKSU- JA TOLLIAMET ; DEBIT ; TSD 02/2026 ; -1,018.16 ; EUR`

**Reasoning:**
Matches "MAKSU- JA TOLLIAMET" / "TSD" (pattern 3.1). For the Example 1 employee (gross EUR 2,000, 2026, 2% pension, EUR 700 exemption), the TSD liability for the month is:
- Income tax withheld: **270.16**
- Social tax (employer): **660.00**
- Employer unemployment 0.8%: **16.00**
- Employee unemployment 1.6%: **32.00**
- Funded pension 2%: **40.00**
- Total TSD remittance: 270.16 + 660.00 + 16.00 + 32.00 + 40.00 = **1,018.16** -> matches the debit. [EMTA social-tax]

**Classification:** EXCLUDE from VAT. Payroll-tax remittance to EMTA covering income tax, social tax, both unemployment premiums and the funded-pension contribution.

### Example 4 -- VAT payment (NOT a social contribution)

**Input line:**
`20.08.2025 ; MAKSU- JA TOLLIAMET ; DEBIT ; KMD 07/2025 ; -4,800.00 ; EUR`

**Reasoning:**
Same EMTA counterparty, but the reference is "KMD" (käibemaksudeklaratsioon -- VAT return), pattern 3.3. This is value-added tax (standard rate 24% from 1 Jul 2025), NOT social tax or any payroll charge. Do not classify as a social contribution. [koda.ee]

**Classification:** EXCLUDE from social classification. This is a VAT remittance -- handle under the Estonia VAT skill, not this one.

### Example 5 -- Minimum social tax floor bites (part-month / low pay, 2025)

**Input line:**
`10.07.2025 ; MAKSU- JA TOLLIAMET ; DEBIT ; SOTSIAALMAKS 06/2025 ; -270.60 ; EUR`

**Reasoning:**
The employee's gross for the month was only EUR 600 (e.g. a part-month start), but the social tax base cannot fall below the EUR 820 monthly minimum unless a statutory exception applies. [EMTA tax-rates]
- Social tax on actual gross: 600 x 33% = 198.00
- Social tax on minimum base: 820 x 33% = **270.60** -- this floor applies.
- The employer therefore declares and pays **EUR 270.60** social tax, not EUR 198.00.

**Classification:** EXCLUDE from VAT. Social tax at the statutory monthly minimum. Flag for reviewer that the floor was applied -- confirm no exception (part-time below threshold, pensioner, etc.).

### Example 6 -- FIE quarterly social-tax advance (self-employed, NOT employee payroll)

**Input line:**
`16.06.2025 ; MAKSU- JA TOLLIAMET ; DEBIT ; FIE AVANSS Q2 ; -811.80 ; EUR`

**Reasoning:**
Matches "FIE AVANSS" (pattern 3.3) -- a sole proprietor's quarterly advance social-tax payment, not an employee withholding. 2025 minimum quarterly advance = 820 x 3 x 33% = **EUR 811.80**, absent reducing circumstances; due 15th of the third month of the quarter (Q2 deadline 16 Jun 2025 -- 15 Jun fell on a weekend). [EMTA social-tax]

**Classification:** EXCLUDE from VAT. FIE social-tax advance. This is the proprietor's own social tax, not a payroll cost of the business's employees.

## Section 5 -- Tier 1 rules

These rules apply when payroll/bank data is clear and all required inputs are available. Apply exactly as written. All figures cited to EMTA tax-rates unless noted.

### Rule 1 -- Social tax is 33%, employer-paid, ON TOP of gross

- **Rule 1** — Social tax (sotsiaalmaks) = 33% of gross remuneration, paid entirely by the employer in addition to gross salary -- never withheld from the employee. Split: 20 percentage points fund state pension insurance, 13 percentage points fund state health insurance.  _(EMTA tax-rates)_

### Rule 2 -- No upper ceiling on employer social tax (employees)

- **Rule 2** — Social tax applies from the first euro of remuneration with no cap for employees. There is no maximum. (Self-employed FIE have an annual cap of 15x the sum of minimum monthly bases -- see Rule 9.)  _(EMTA tax-rates; PwC)_

### Rule 3 -- Minimum monthly social tax base

**Minimum monthly social tax base table**  _(EMTA tax-rates)_

| Year | Minimum base | Minimum social tax |
| --- | --- | --- |
| 2025 | EUR 820/month | EUR 270.60/month (820 x 33%) |
| 2026 | EUR 886/month | EUR 292.38/month (886 x 33%) |

- **Floor exceptions** — The floor secures health-insurance coverage even on low/part-time pay. It does NOT apply in certain cases (e.g. some part-time arrangements, recipients of a state pension).  _(EMTA tax-rates)_

### Rule 4 -- Unemployment insurance premiums

- **Rule 4** — Employee premium = 1.6% of gross (withheld). Employer premium = 0.8% of total gross payroll (on top). No floor, no cap. Employees who have reached old-age pensionable age, or who receive an early-retirement pension, are exempt from the employee 1.6% withholding (the employer 0.8% still applies).  _(EMTA tax-rates)_

### Rule 5 -- Mandatory funded pension (II pillar)

- **Rule 5** — Member rate = 2% / 4% / 6%, chosen by application to the registrar; the statutory default is 2% if no higher-rate application is filed. Mandatory for residents born after 31 December 1982; voluntary opt-in for others. No floor, no cap. The state additionally directs 4 percentage points of the social tax pension portion to the member's II-pillar account at no extra employer cost.  _(EMTA tax-rates; PwC)_

### Rule 6 -- Personal income tax is a flat 22%

- **Rule 6** — Income tax (tulumaks) = 22% flat in 2025 and 2026 (raised from 20% effective 1 Jan 2025). No progressive brackets. Withheld monthly by the employer.  _(EMTA tax-rates)_

### Rule 7 -- Income tax base (order of deductions)

- **Rule 7** — For employees, withhold income tax on: gross - employee unemployment premium (1.6%) - employee funded pension (2/4/6%, if a member) - the applicable monthly basic exemption. The unemployment premium and funded-pension contribution reduce the income-tax base before the 22% rate applies.  _(EMTA tax-rates; EMTA private-client)_

### Rule 8 -- Basic exemption (maksuvaba tulu)

**Basic exemption table**

| Year | Basic exemption |
| --- | --- |
| 2025 | Income-dependent ("tax hump"): up to EUR 654/month (EUR 7,848/yr); tapers to zero as annual income rises from EUR 14,400 to EUR 25,200. EUR 776/month (EUR 9,312/yr) for persons of pensionable age. [EMTA 2025 declarations overview] |
| 2026 | Flat EUR 700/month (EUR 8,400/yr) for all residents regardless of income (tax hump abolished); EUR 776/month (EUR 9,312/yr) for persons of pensionable age. [EMTA tax-rates] |

- **Application requirement** — Apply the monthly exemption in payroll ONLY if the employee filed an application with the employer. The exact 2025 taper thresholds (EUR 14,400 / EUR 25,200) should be confirmed against the Income Tax Act. [RESEARCH GAP -- reviewer to confirm 2025 taper thresholds against Tulumaksuseadus]  _(RESEARCH GAP -- reviewer to confirm 2025 taper thresholds against Tulumaksuseadus)_

### Rule 9 -- Self-employed (FIE) social tax

- **Rule 9** — FIE pay 33% social tax on business income, via quarterly advance payments. 2025 minimum advance = 820 x 3 x 33% = EUR 811.80/quarter absent reducing circumstances. Annual cap = 15x the sum of minimum monthly bases. Advance deadlines (2025): 17 Mar, 16 Jun, 15 Sep, 15 Dec.  _(EMTA social-tax)_

### Rule 10 -- Standard on-cost and deductions summary

- **Rule 10** — Standard employer on-cost above gross = 33.8% (33% social tax + 0.8% employer unemployment). Standard employee deductions = 22% income tax (on income above the exemption) + 1.6% unemployment + 2/4/6% funded pension (if a member).  _(EMTA tax-rates)_

### Rule 11 -- Monthly declaration and payment (Form TSD)

- **Rule 11** — Employers declare and pay income tax withheld, social tax, both unemployment premiums and the funded-pension contribution on Form TSD (with annexes), due by the 10th day of the month following the payment month; the tax is paid by the same date. Public-sector bodies use the equivalent Form ESD.  _(EMTA social-tax)_

### Rule 12 -- The 2026 "security/defence tax" does NOT apply

- **Rule 12** — The planned 2% personal-income security/defence tax (originally to take effect 1 Jan 2026) was abolished by Parliament in June 2025 -- do not apply it. PIT remains 22% (the once-discussed rise to 24% was cancelled). The temporary 2% VAT surcharge was made permanent, so the standard VAT rate is 24% from 1 Jul 2025. Social tax obligations are independent of corporate income tax (CIT is levied only on distributions at 22/78; the reduced 14/86 regular-dividend rate was abolished from 1 Jan 2025).  _(koda.ee; key rules)_

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation. Do not resolve them unilaterally.

### T2-1 -- II-pillar membership and rate uncertain

**Trigger:** Net-pay or withholding requested without confirmed II-pillar membership or the elected rate.

**Issue:** Non-members have zero pension withholding; members withhold 2%, 4% or 6%. Membership is mandatory for residents born after 31 Dec 1982, but an earlier birth year does not rule out a voluntary opt-in. The rate is whatever the person applied for (default 2%).

**Action:** Flag for reviewer. Confirm membership and elected rate via the registrar before finalising net pay.

### T2-2 -- Pensionable-age / early-retirement employees

**Trigger:** Employee is at or above old-age pensionable age, or receives an early-retirement pension.

**Issue:** Such employees are exempt from the employee 1.6% unemployment withholding; the employer 0.8% still applies. The minimum social tax base may also not bind for pensioners. Pensionable-age employees also use the higher EUR 776/month basic exemption.

**Action:** Flag for reviewer. Confirm age/pension status before withholding.

### T2-3 -- Board-member (juhatuse liige) fees vs employment

**Trigger:** Remuneration is a board-member fee rather than (or in addition to) an employment wage.

**Issue:** Board fees attract social tax and income tax, but the unemployment insurance premium treatment differs (board members are generally NOT subject to the unemployment premium). The mix of an employment contract plus a board fee complicates the withholding.

**Action:** Flag for reviewer. [RESEARCH GAP -- reviewer to confirm unemployment-premium treatment of board fees against the Unemployment Insurance Act]

### T2-4 -- Cross-border / posted workers (A1)

**Trigger:** Work in more than one EU/EEA state, posting, or an A1 certificate.

**Issue:** The state in which social charges are due is set by EU Regulation 883/2004 and any A1 certificate, not by where the payroll is run.

**Action:** Escalate to a qualified Estonian tax adviser. Do not apply Estonian social tax by default. [RESEARCH GAP -- reviewer to confirm coordination treatment]

### T2-5 -- Fringe benefits (erisoodustus)

**Trigger:** Package includes in-kind benefits, company car, options, etc.

**Issue:** Fringe benefits are taxed at the employer level on a grossed-up base (benefit value + income tax thereon), with social tax also applying. This is outside the simple wage formula here.

**Action:** Flag for reviewer. Compute fringe-benefit tax separately on the TSD annexes.

### T2-6 -- Minimum social tax floor exceptions

**Trigger:** Low or part-month pay where the EUR 820 (2025) / EUR 886 (2026) floor would otherwise bite.

**Issue:** The floor does not apply in certain statutory cases (some part-time arrangements, state-pension recipients, etc.). Applying or omitting the floor incorrectly mis-states the employer cost.

**Action:** Flag for reviewer to confirm whether an exception applies.

## Section 7 -- Excel working paper template

When producing an Estonian social-contribution / net-pay computation, structure the working paper as follows:

```
ESTONIA SOCIAL CONTRIBUTIONS & NET PAY -- WORKING PAPER
Client / employer: [name]
Employee: [name]
Tax Year: [2025 / 2026]
Prepared: [date]

INPUT DATA
  Gross monthly remuneration:        EUR [____]
  II-pillar member:                  [YES/NO]
  Funded pension rate (if member):   [2% / 4% / 6%]   (default 2%)
  Basic-exemption application filed: [YES/NO]
  Pensionable age:                   [YES/NO]
  Status:                            [Employee / Board member / FIE]

EMPLOYER COST (ON TOP OF GROSS)
  Social tax 33% (min base check):   EUR [____]   (>= 820 x 33% in 2025 / 886 x 33% in 2026)
  Employer unemployment 0.8%:        EUR [____]
  Total employer on-cost (33.8%):    EUR [____]   (= gross x 1.338, subject to floor)
  TOTAL EMPLOYER OUTLAY:             EUR [____]   (= gross + on-cost)

EMPLOYEE WITHHOLDINGS (FROM GROSS)
  Unemployment insurance 1.6%:       EUR [____]   (0 if pensionable age)
  Funded pension 2/4/6%:             EUR [____]   (0 if not a member)
  Basic exemption applied:           EUR [____]   (654 or 776 in 2025 / 700 or 776 in 2026)
  Income tax base:                   EUR [____]   (= gross - unemployment - pension - exemption)
  Income tax 22%:                    EUR [____]
  NET PAY:                           EUR [____]   (= gross - unemployment - pension - income tax)

MONTHLY TSD REMITTANCE TO EMTA
  Income tax withheld:               EUR [____]
  Social tax:                        EUR [____]
  Employer unemployment:             EUR [____]
  Employee unemployment:             EUR [____]
  Funded pension:                    EUR [____]
  TOTAL TSD (due 10th next month):   EUR [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How Estonian social charges and payroll taxes appear

Estonia uses a single EMTA prepayment account: employers transfer one consolidated amount to the Estonian Tax and Customs Board (Maksu- ja Tolliamet) to cover the whole TSD liability -- income tax, social tax, both unemployment premiums and the funded-pension contribution. You will rarely see the components split on the bank statement; they are split inside the TSD declaration.

**Swedbank / SEB / LHV / Luminor (the main Estonian banks):**
- Counterparty: "MAKSU- JA TOLLIAMET" (sometimes "MAKSUAMET" or "EMTA")
- Reference: "TSD MM/YYYY", "SOTSIAALMAKS", "TULUMAKS", or an EMTA reference number
- Timing: monthly, on or before the 10th of the following month
- Amount: the full TSD liability for the prior month

**Key identification tips:**
1. EMTA payroll-tax debits are outgoing (DEBIT), monthly, on/before the 10th.
2. The same EMTA counterparty also collects VAT ("KMD") and other taxes -- read the reference to tell payroll tax ("TSD"/"SOTSIAALMAKS") from VAT ("KMD"/"KÄIBEMAKS").
3. Net-salary lines ("PALK"/"NETOPALK"/"TÖÖTASU") are separate outgoing payments to employees -- not contributions.
4. FIE advance payments ("FIE AVANSS"/"ETTEMAKS") are the proprietor's own social tax, quarterly (15th of the third month), not employee payroll.
5. Inbound benefit credits ("PENSION", "HAIGUSHÜVITIS") are benefits received, not contributions.

### Glossary (Estonian -> English)

**Glossary table**

| Estonian | English |
| --- | --- |
| sotsiaalmaks | social tax |
| töötuskindlustusmakse | unemployment insurance premium |
| kogumispension / II sammas | funded pension / II pillar |
| tulumaks | income tax |
| maksuvaba tulu | basic exemption (tax-free income) |
| palk / töötasu | salary / wages |
| netopalk | net pay |
| juhatuse liikme tasu | board member's fee |
| erisoodustus | fringe benefit |
| FIE (füüsilisest isikust ettevõtja) | sole proprietor / self-employed |
| käibemaks (KMD) | value-added tax (VAT return) |
| Maksu- ja Tolliamet (EMTA) | Tax and Customs Board |
| Töötukassa | Unemployment Insurance Fund |
| miinimumpalk | minimum wage |

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Identify the employer.** Confirm whether this is an OÜ/AS running payroll, or a FIE.
2. **Scan for EMTA debits** -- find monthly outgoing payments to "MAKSU- JA TOLLIAMET" referencing "TSD"/"SOTSIAALMAKS"/"TULUMAKS". Separate these from "KMD"/VAT debits.
3. **Scan for net-salary debits** -- "PALK"/"NETOPALK"/"TÖÖTASU" outgoing payments to individuals.
4. **Reverse-estimate the on-cost:** for a known monthly net salary, the employer outlay is roughly gross x 1.338; gross cannot be recovered exactly from net without the II-pillar rate and the basic-exemption status. Note assumptions explicitly.
5. **Check the floor:** any month where social tax is below EUR 270.60 (2025) / EUR 292.38 (2026) implies either an exception or an error -- flag it.
6. **Flag for reviewer:** "Estonian social-contribution figures derived from bank-statement amounts only. II-pillar membership, basic-exemption applications, and age/pension status have not been independently verified. Reviewer must confirm before filing any TSD or relying on the net-pay figures."

## Section 10 -- Reference material

### Rate brackets and key thresholds

**Rate brackets and key thresholds table**

| Item | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Personal income tax | 22% flat | 22% flat | EMTA tax-rates |
| Social tax | 33% (20pp pension + 13pp health) | 33% | EMTA tax-rates |
| Employer unemployment insurance | 0.8% | 0.8% | EMTA tax-rates |
| Employee unemployment insurance | 1.6% | 1.6% | EMTA tax-rates |
| Funded pension (II pillar) | 2% / 4% / 6% (default 2%) | 2% / 4% / 6% (default 2%) | EMTA tax-rates; PwC |
| State II-pillar top-up | 4pp of social tax pension portion, no extra employer cost | 4pp | PwC |
| Min monthly social tax base | EUR 820 (=> EUR 270.60 tax) | EUR 886 (=> EUR 292.38 tax) | EMTA tax-rates |
| Basic exemption (standard) | up to EUR 654/mo, tapering 14,400->25,200 [taper RESEARCH GAP] | EUR 700/mo flat | EMTA 2025 overview; EMTA tax-rates |
| Basic exemption (pensionable age) | EUR 776/mo (EUR 9,312/yr) | EUR 776/mo (EUR 9,312/yr) | EMTA tax-rates / 2025 overview |
| National minimum wage | EUR 886/mo; EUR 5.31/hr | EUR 946/mo; EUR 5.67/hr (from 1 Apr 2026) | palgakalkulaator.ee; ERR |
| Total employer on-cost above gross | 33.8% | 33.8% | EMTA tax-rates |
| FIE min quarterly social-tax advance | EUR 811.80 (820 x 3 x 33%) | EUR 877.14 (886 x 3 x 33%) [derived, not separately quoted] | EMTA social-tax |
| VAT registration threshold | EUR 40,000 taxable turnover / calendar year | EUR 40,000 | PwC |
| II-pillar mandatory membership | residents born after 31 Dec 1982 | residents born after 31 Dec 1982 | PwC |

### Forms

**Forms table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| TSD (annex 1/2) | Monthly employer declaration of income tax withheld, social tax, unemployment premiums, funded pension; also fringe benefits | By the 10th of the following month | EMTA social-tax |
| ESD | Equivalent declaration for state/municipal (public-sector) bodies | By the 10th of the following month | EMTA social-tax |
| FIE social-tax advances | Quarterly advance social tax for sole proprietors | 15th of the third month of each quarter (2025: 17 Mar, 16 Jun, 15 Sep, 15 Dec) | EMTA social-tax |
| Annual personal income tax return | Reconciliation of PIT, basic exemption and additional liabilities | 15 Feb -- 30 Apr following the tax year (2025 income by 30 Apr 2026) | EMTA private-client |

### Penalties

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| Late payment interest | Statutory interest on overdue tax at 0.06% per day (~21.9% per annum) under the Taxation Act [re-check against current statute] | PwC |
| Late or non-declaration | EMTA may issue compliance notices with penalty payments and assess tax; failure to declare/withhold can trigger misdemeanour fines | EMTA social-tax |

### Worked employer-cost / net-pay table (recomputed)

**Worked employer-cost / net-pay table**

| Gross/mo | Year | II-pillar | Exemption | EE unemp 1.6% | EE pension | PIT base | PIT 22% | Net pay | Employer cost (x1.338) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EUR 1,000 | 2026 | 2% | 700 | 16.00 | 20.00 | 264.00 | 58.08 | 905.92 | 1,338.00 |
| EUR 2,000 | 2026 | 2% | 700 | 32.00 | 40.00 | 1,228.00 | 270.16 | 1,657.84 | 2,676.00 |
| EUR 886 | 2025 | none | 654 | 14.18 | 0.00 | 217.82 | 47.92 | 823.90 | 1,185.47 |
| EUR 6,000 | 2026 | 6% | 700 | 96.00 | 360.00 | 4,844.00 | 1,065.68 | 4,478.32 | 8,028.00 |

(PIT base = gross - EE unemployment - EE pension - exemption; Net pay = gross - EE unemployment - EE pension - PIT. All cents reconciled. Figures cited to EMTA tax-rates; 2025 basic exemption per EMTA 2025 declarations overview.)

### Test suite

Gross EUR 1,000/mo, 2026, II-pillar 2%, exemption EUR 700 applied. -> EE unemployment 16.00; pension 20.00; PIT base 264.00; PIT 58.08; net pay EUR 905.92. Employer cost EUR 1,338.00.

Gross EUR 2,000/mo, 2026, II-pillar 2%, exemption EUR 700 applied. -> EE unemployment 32.00; pension 40.00; PIT base 1,228.00; PIT 270.16; net pay EUR 1,657.84. Employer cost EUR 2,676.00; monthly TSD EUR 1,018.16.

Gross EUR 886/mo (2025 minimum wage), not II-pillar member, exemption EUR 654. -> EE unemployment 14.18; pension 0; PIT base 217.82; PIT 47.92; net pay EUR 823.90. Employer cost EUR 1,185.47.

Gross EUR 6,000/mo, 2026, II-pillar 6%, exemption EUR 700. -> EE unemployment 96.00; pension 360.00; PIT base 4,844.00; PIT 1,065.68; net pay EUR 4,478.32. Employer cost EUR 8,028.00.

Actual gross EUR 600 for the month, 2025; social tax floor applies. -> social tax = max(600 x 33%, 820 x 33%) = EUR 270.60 (floor binds). Flag whether an exception applies.

Gross EUR 2,000/mo, 2025, exemption NOT applied (no application filed), II-pillar 2%. -> EE unemployment 32.00; pension 40.00; PIT base = 2,000 - 32 - 40 - 0 = 1,928.00; PIT 22% = 424.16; net pay = 2,000 - 32 - 40 - 424.16 = EUR 1,503.84. Employer cost EUR 2,676.00.

FIE, 2025, no reducing circumstances. -> minimum quarterly social-tax advance = 820 x 3 x 33% = EUR 811.80; due 17 Mar, 16 Jun, 15 Sep, 15 Dec 2025.

Pensionable-age employee, gross EUR 1,500/mo, 2026, exemption EUR 776, not II-pillar member. -> EE unemployment 0.00 (exempt); pension 0; PIT base = 1,500 - 0 - 0 - 776 = 724.00; PIT 22% = 159.28; net pay = 1,500 - 159.28 = EUR 1,340.72. Employer side: employer unemployment 0.8% still applies (1,500 x 0.8% = 12.00); social tax 1,500 x 33% = 495.00; employer cost = 1,500 + 495.00 + 12.00 = EUR 2,007.00.

### Prohibitions

- NEVER withhold social tax from the employee -- the 33% social tax is an EMPLOYER cost ON TOP of gross.
- NEVER apply an upper cap to employer social tax for employees -- there is no ceiling.
- NEVER omit the minimum monthly social tax base (EUR 820 in 2025 / EUR 886 in 2026) without confirming a statutory exception applies.
- NEVER compute employee net pay without confirming II-pillar membership and the elected funded-pension rate.
- NEVER apply the monthly basic exemption in payroll unless the employee filed an application with the employer.
- NEVER apply the abolished 2% security/defence tax -- it was repealed in June 2025 and does NOT apply.
- NEVER use a PIT rate other than 22% for 2025 or 2026 (do not use the cancelled 24% figure, and do not use the old 20%).
- NEVER confuse the EMTA VAT debit ("KMD") with the EMTA payroll-tax debit ("TSD") -- they are different taxes.
- NEVER treat FIE advance social-tax payments as the employer's payroll cost for its employees.
- NEVER present figures as definitive -- label as estimated and direct the client to their EMTA e-services data and a qualified Estonian tax adviser.

## Reference sources

- Tax rates -- Estonian Tax and Customs Board (business client): https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates
- Social tax -- Estonian Tax and Customs Board: https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax
- Tax rates -- Estonian Tax and Customs Board (private client): https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates
- Overview on what to consider when submitting declarations in 2025 for companies -- EMTA: https://www.emta.ee/en/news/overview-what-consider-when-submitting-declarations-2025-companies
- Estonia -- Individual -- Other taxes (PwC Worldwide Tax Summaries): https://taxsummaries.pwc.com/estonia/individual/other-taxes
- Estonia -- Significant tax changes apply in 2025-2026 (EY) -- NOTE: reflects the superseded security-tax plan; cross-check: https://www.ey.com/en_gl/technical/tax-alerts/estonia-significant-tax-changes-apply-in-2025-2026
- Security Tax Abolished, but VAT and Income Tax to Rise -- Estonian Chamber of Commerce and Industry (koda.ee): https://www.koda.ee/en/news/security-tax-abolished-vat-and-income-tax-rise-24
- Employers and unions agree on 946 euro as Estonia's new minimum wage -- ERR: https://news.err.ee/1609943096/employers-and-unions-agree-on-946-as-estonia-s-new-minimum-wage
- Minimum Wage in Estonia -- Current Rates and History (Palgakalkulaator): https://www.palgakalkulaator.ee/en/teadmiseks/miinimumpalk

- **Minimum social tax base (2026)** — 886 EUR  _(EMTA tax-rates page; https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates)_
- **Basic exemption (2026)** — 700 EUR/month  _(EMTA tax-rates page; https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates)_
- **Minimum wage (from 1 Apr 2026)** — 946 EUR  _(Employers and unions agree on 946 euro as Estonia's new minimum wage -- ERR: https://news.err.ee/1609943096/employers-and-unions-agree-on-946-as-estonia-s-new-minimum-wage)_
- **Security/defence tax repeal** — The original Security Tax Act would have added a 2% personal-income tax from 2026 but was repealed in June 2025. (per ERR and koda.ee)  _(Security Tax Abolished, but VAT and Income Tax to Rise -- Estonian Chamber of Commerce and Industry (koda.ee): https://www.koda.ee/en/news/security-tax-abolished-vat-and-income-tax-rise-24)_
- **Personal income tax (PIT) rate** — 22 % (the once-discussed rise to 24% was cancelled)  _(Tax rates -- Estonian Tax and Customs Board (private client): https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates)_
- **VAT standard rate** — 24 % (now permanent)  _(Security Tax Abolished, but VAT and Income Tax to Rise -- Estonian Chamber of Commerce and Industry (koda.ee): https://www.koda.ee/en/news/security-tax-abolished-vat-and-income-tax-rise-24)_
- **2026 FIE quarterly advance** — 886 x 3 x 33% = EUR 877.14 EUR (derived arithmetically from the published base, not separately quoted)
- **State pension-portion transfer for II-pillar members** — 4 percentage points (sourced from PwC; verify the precise mechanism against the Funded Pensions Act if exact accuracy is required)  _(Estonia -- Individual -- Other taxes (PwC Worldwide Tax Summaries): https://taxsummaries.pwc.com/estonia/individual/other-taxes)_
- **Late-payment interest rate** — 0.06 %/day (long-standing statutory rate per the Taxation Act; should be re-checked against the current statute)
- **2025 basic-exemption taper thresholds** — EUR 14,400 / EUR 25,200 (income-dependent; a reviewer should confirm these against the Income Tax Act)  _(unsure - needs reviewer confirmation against Income Tax Act)_

2026 figures (minimum social tax base EUR 886, basic exemption EUR 700/month, minimum wage EUR 946 from 1 Apr 2026) are officially confirmed on the EMTA tax-rates page and the agreed minimum-wage announcement and are treated as current. The legislative status of the "security/defence tax" was volatile in 2025: the original Security Tax Act would have added a 2% personal-income tax from 2026 but was repealed in June 2025 (per ERR and koda.ee); the EY 2025-2026 alert reflects the earlier, superseded plan, so cross-check before relying on it for the 2026 personal-income position. PIT remains 22% (the once-discussed rise to 24% was cancelled); the VAT standard rate is now 24% permanently. The 2026 FIE quarterly advance (886 x 3 x 33% = EUR 877.14) is derived arithmetically from the published base, not separately quoted. The 4pp state pension-portion transfer figure for II-pillar members is sourced from PwC; verify the precise mechanism against the Funded Pensions Act if exact accuracy is required. The 0.06%/day late-payment interest rate is the long-standing statutory rate per the Taxation Act and should be re-checked against the current statute. A reviewer should confirm the income-dependent 2025 basic-exemption taper thresholds (EUR 14,400 / EUR 25,200) against the Income Tax Act.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
