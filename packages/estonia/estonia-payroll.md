---
name: estonia-payroll
description: Use this skill whenever asked about Estonia payroll processing for employed persons. Trigger on phrases like "Estonia payroll", "Estonian payroll", "palgaarvestus", "sotsiaalmaks", "social tax Estonia", "income tax withholding Estonia", "tulumaks kinnipidamine", "töötuskindlustusmakse", "unemployment insurance premium Estonia", "II pillar", "II sammas", "kohustuslik kogumispension", "funded pension Estonia", "Form TSD", "TSD declaration", "net salary Estonia", "gross to net Estonia", "palk", "netopalk", "EMTA payroll", "Maksu- ja Tolliamet payroll", "basic exemption Estonia", "maksuvaba tulu", "minimum wage Estonia", "employer cost Estonia", "what does an Estonian employee cost", or any question about computing employee pay, withholding income tax, social tax, unemployment premiums, or funded-pension contributions for Estonia-based employees. This skill covers flat 22% income tax withholding (after basic exemption), 33% employer social tax (uncapped, with a monthly minimum base), employee/employer unemployment insurance premiums, mandatory funded (II pillar) pension contributions, the basic exemption, minimum wage, employment-register registration, bank statement classification patterns, and monthly Form TSD filing. ALWAYS read this skill before processing any Estonia payroll.
version: 0.1
jurisdiction: EE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia Payroll

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Estonia (Republic of Estonia) |
| Currency | EUR only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax basis | Cash basis -- tax and contributions follow amounts actually PAID in the calendar month |
| Tax withholding system | Flat-rate income tax withheld monthly at source by the employer (withholding agent) |
| Tax authority | Estonian Tax and Customs Board (Maksu- ja Tolliamet, EMTA), portal e-MTA at emta.ee |
| Social insurance administration | EMTA (collection); Social Insurance Board (Sotsiaalkindlustusamet); Unemployment Insurance Fund (Töötukassa); II pillar register run by Pensionikeskus |
| Key legislation | Income Tax Act (Tulumaksuseadus, TuMS); Social Tax Act (Sotsiaalmaksuseadus, SMS); Unemployment Insurance Act (Töötuskindlustuse seadus); Funded Pensions Act (Kogumispensionide seadus); Taxation Act (Maksukorralduse seadus, MKS) |
| Combined payroll return | Form TSD (single monthly declaration), filed via e-MTA |
| Filing/payment deadline | By the 10th day of the month following the month of payment |
| Income tax (flat) 2025 and 2026 | 22% withheld at source (after basic exemption) |
| Social tax 2025 and 2026 | 33% of gross (employer-paid, uncapped) -- 20% public pension + 13% public health |
| Validated by | Pending -- requires sign-off by an Estonian tax professional |
| Skill version | 0.1 |

**Read this whole section before computing or classifying anything.**

### Charge overview (standard resident employee)

**Charge overview table**

| Charge | Who pays | Rate | Capped? |
| --- | --- | --- | --- |
| Income tax (withholding) | Employee (withheld) | 22% flat (after basic exemption) | n/a |
| Social tax (sotsiaalmaks) | Employer | 33% (20% pension + 13% health) | No -- uncapped, but monthly **minimum base** applies |
| Unemployment premium -- employee (töötuskindlustusmakse) | Employee (withheld) | 1.6% of gross wages | No |
| Unemployment premium -- employer | Employer | 0.8% of payroll base | No |
| Mandatory funded pension (II pillar) -- employee | Employee (withheld) | 2% / 4% / 6% (default 2%) | No |
| Funded pension (II pillar) -- state addition | State (from the employer's 33% social tax; NOT an extra employer cost) | 4% of gross (member's account) | No |

- **Employer-side cost on top of gross** — 33% social tax + 0.8% unemployment = ~33.8%.  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax); [EMTA -- unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums))_
- **Employee-side withholdings from gross** — 22% income tax (after basic exemption) + 1.6% unemployment + 2/4/6% II pillar.  _([EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))_

> The state's 4% II pillar addition is drawn FROM the 20-point pension share of the employer's social tax and transferred by EMTA to the member's account -- it does not increase the employer's cash outlay. Source: [EMTA -- contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension). [RESEARCH GAP -- some secondary summaries (e.g. PwC) still cite 2%, the pre-2024 figure; reviewer to confirm the current addition against the Funded Pensions Act text.]

## Section 2 -- Conservative Defaults

Apply these when an input is ambiguous and the gap does not require a hard refusal (Section 3). Each default is the cautious choice; record any default applied in the working paper.

**Conservative defaults table**

| Ambiguity | Default | Basis |
| --- | --- | --- |
| Unknown II pillar employee rate | Withhold **2%** (statutory default) unless the employee has elected 4% or 6% via Pensionikeskus -- verify the election rather than assume; the same rate applies across all employers | [EMTA -- contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension); [Pensionikeskus](https://www.pensionikeskus.ee/en/ii-pillar/mandatory-funded-pension/) |
| Basic exemption application status unknown | Apply **0** monthly basic exemption unless the employee has filed a written application electing it with this employer; only one payer may apply it | [EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Gross pay below the monthly minimum base | Charge social tax on at least the monthly minimum base (EUR 820 in 2025 / EUR 886 in 2026) for any employee with active employment, unless a documented exemption applies (e.g. part-month, parental leave) | [EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax) |
| Unknown income tax rate | 22% flat (2025 and 2026) | [EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Unknown unemployment premium rates | Employee 1.6% / employer 0.8% (fixed 1 Jan 2025 through end 2028) | [EMTA -- unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums) |
| Unknown birth year for II pillar obligation | STOP -- ask. II pillar is mandatory only for residents born after 31 Dec 1982 (R-EE-PAY-2) | [EMTA -- contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension); [Pensionikeskus](https://www.pensionikeskus.ee/en/ii-pillar/mandatory-funded-pension/) |
| Unknown whether worker is of pensionable age | Ask -- the employee 1.6% premium is NOT withheld from persons of pensionable age (the 0.8% employer premium still applies) | [EMTA -- unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums) |
| Unknown tax period (2025 vs 2026) | Ask -- minimum social tax base and basic exemption differ between years (R-EE-PAY-1) | [EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |

## Section 3 -- Required Inputs and Refusal Catalogue

### Required inputs

**Minimum viable** -- gross monthly remuneration and the tax period (which calendar year). Without the period, STOP: the minimum social tax base (EUR 820 vs EUR 886) and the basic exemption rules differ between 2025 and 2026.

**Recommended** -- employee birth year (drives II pillar obligation: mandatory for residents born after 31 December 1982), the employee's elected II pillar rate (2/4/6%), whether the worker is of pensionable age (affects the employee unemployment premium), residency status, and whether the employee has filed a written basic-exemption application with this employer.

**Ideal** -- the prior month's Form TSD, bank statements showing EMTA payroll debits, the employment-register (töötamise register / TÖR) entry, and the employee's basic-exemption application.

### Refusal catalogue

- **R-EE-PAY-1** — Tax period unknown. Trigger: the calendar year of the payment is not provided. Message: "The tax period is mandatory. The minimum social tax base (EUR 820 in 2025 vs EUR 886 in 2026), the minimum social tax (EUR 270.60 vs EUR 292.38), and the basic exemption rules (income taper in 2025 vs flat EUR 700/month in 2026) all differ by year. Cannot proceed without confirming the period."  _([EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))_
- **R-EE-PAY-2** — II pillar obligation / birth year unknown. Trigger: II pillar must be computed but the employee's birth year or membership/election status is not provided. Message: "Mandatory funded pension (II pillar) is compulsory only for Estonian residents born after 31 December 1982; the elected employee rate may be 2%, 4% or 6% (default 2%) and applies across all employers. Cannot determine the II pillar withholding without the birth year and membership/rate status. Confirm via Pensionikeskus or e-MTA before computing."  _([EMTA -- contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension))_
- **R-EE-PAY-3** — Non-standard worker (non-resident, e-resident/non-resident employer, posted worker, board member, FIE). Trigger: the worker is a non-resident, an e-resident running a foreign company, a posted/seconded worker, a board member receiving board fees, or a self-employed person (FIE). Message: "Special regimes (non-residents, e-residents/non-resident employers, posted workers, board-member fees, self-employed FIE) have material nuances not fully expanded in this skill -- including which state's social security applies and Annex 2 (non-resident) reporting on Form TSD. Escalate to an Estonian tax professional."
- **R-EE-PAY-4** — Social tax base reductions and arrears. Trigger: the worker started or ended mid-month, works part-time below the minimum base, claims a reduction from the minimum social tax obligation (e.g. parental leave, incapacity, reduced work capacity), or has unpaid payroll-tax arrears. Message: "Reductions to the minimum monthly social tax base (mid-month start/end, statutory part-time exceptions, periods of incapacity, parental leave, reduced-work-capacity employees) and arrears with accruing 0.06%/day interest require case-specific confirmation. Do not estimate arrears without an e-MTA statement. Escalate to an Estonian tax professional."  _([EMTA -- payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests))_

## Section 4 -- Transaction / Payment Pattern Library

This is the deterministic pre-classifier for bank statement transactions related to Estonian payroll. When a transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Payroll-tax payments to EMTA always EXCLUDE from any VAT return classification -- they are payroll/statutory obligations, not VATable supplies. The single monthly EMTA debit normally bundles income tax + social tax + both unemployment premium shares + II pillar; it is **not** separable from the bank line alone (use Form TSD for the breakdown).

### 4.1 EMTA payroll-tax payments (income tax, social tax, unemployment, II pillar)

**EMTA payroll-tax payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MAKSU- JA TOLLIAMET, EMTA | EXCLUDE -- payroll tax to EMTA | Bundled monthly TSD payment |
| MAKSUAMET, TOLLIAMET, RIIGIMAKSUD | EXCLUDE -- payroll tax to EMTA | Same |
| SOTSIAALMAKS, SOCIAL TAX | EXCLUDE -- social tax (employer) | 33% employer charge |
| TÖÖTUSKINDLUSTUSMAKSE, UNEMPLOYMENT INSURANCE | EXCLUDE -- unemployment premium | Employer 0.8% + employee 1.6% |
| KOGUMISPENSION, II SAMMAS, FUNDED PENSION | EXCLUDE -- II pillar contribution | Employee 2/4/6% withheld |
| TULUMAKS, INCOME TAX, KINNIPEETUD TULUMAKS | EXCLUDE -- withholding income tax | 22% flat |
| TSD, MAKSEKORRALDUSE VIITENUMBER | EXCLUDE -- TSD payroll-tax payment | EMTA reference-number payment |

### 4.2 EMTA debits appearing on specific Estonian banks

**EMTA debits by bank table**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| Swedbank | "MAKSU- JA TOLLIAMET" / "EMTA" / "RIIGIMAKSUD" | EXCLUDE -- payroll tax |
| SEB Pank | "MAKSU- JA TOLLIAMET" / "EMTA TSD" | EXCLUDE -- payroll tax |
| LHV Pank | "EMTA" / "MAKSUAMET" / "SOTSIAALMAKS" | EXCLUDE -- payroll tax |
| Luminor | "MAKSU- JA TOLLIAMET" / "RIIGIMAKS" | EXCLUDE -- payroll tax |
| Coop Pank | "EMTA" / "MAKSUAMET" | EXCLUDE -- payroll tax |
| Wise / Revolut | Rare -- EMTA payments typically come from local Estonian accounts | If present, EXCLUDE |

### 4.3 Wages and net-pay transfers (NOT a tax payment -- do not confuse)

**Wages and net-pay transfers table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PALK, TÖÖTASU, SALARY, NETOPALK (outgoing) | EXCLUDE -- payroll wage expense | Net pay to employee, not a tax payment |
| PALK, NETOPALK (incoming) | EXCLUDE -- employment income received | Not a tax payment |
| DIVIDEND, DIVIDENDID (outgoing) | EXCLUDE -- dividend, not payroll | Separate distribution-tax regime (22/78); not payroll |

### 4.4 Pension and benefit credits (received -- not a contribution)

**Pension and benefit credits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION, RIIKLIK PENSION | EXCLUDE -- state pension income received | Not a contribution paid |
| TÖÖTUKASSA (incoming) | EXCLUDE -- unemployment benefit received | Not a premium paid |
| HAIGUSHÜVITIS, SICK PAY (incoming) | EXCLUDE -- benefit received | Not a contribution |

## Section 5 -- Worked Examples

Six worked examples for a hypothetical Tallinn-based company paying resident employees. All figures are illustrative; bank-statement amounts use the local format (comma decimal separator, space thousands separator, EUR).

### Example 1 -- Standard monthly EMTA payroll-tax debit (Swedbank)

**Input line:**
`10.02.2025 ; MAKSU- JA TOLLIAMET ; DEBIT ; TSD JAANUAR 2025 ; -1 234,56 ; EUR`

**Reasoning:**
Matches "MAKSU- JA TOLLIAMET" (pattern 4.1 / 4.2 Swedbank). This is the bundled monthly Form TSD payment for January 2025 wages, due by 10 February 2025. It bundles withheld income tax (22%), employer social tax (33%), unemployment premiums (employee 1.6% + employer 0.8%) and II pillar (employee's 2/4/6%). The single bank line cannot be decomposed -- use the filed TSD for the split. Source: [EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax).

**Classification:** EXCLUDE -- payroll tax to EMTA. Not a VATable supply.

### Example 2 -- Gross-to-net on a EUR 2,000 gross salary (2025)

**Input:** Gross monthly salary EUR 2,000, resident employee born 1990 (II pillar mandatory, default 2%), basic-exemption application on file. 2025.

**Reasoning (computation):**
- Social tax (employer): EUR 2,000 x 33% = **EUR 660.00** (above the EUR 820 minimum base, so actual gross applies; uncapped). Source: [EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax).
- Unemployment premium, employer: EUR 2,000 x 0.8% = **EUR 16.00**.
- **Total employer cost on top of gross = EUR 676.00; total cost to employer = EUR 2,676.00.**
- Withheld from employee: unemployment 1.6% = EUR 32.00; II pillar 2% = EUR 40.00.
- Basic exemption (2025, income taper): annual income = EUR 2,000 x 12 = EUR 24,000, which is between EUR 14,400 and EUR 25,200, so the exemption is tapered. Annual exemption = 7,848 - (7,848 / 10,800) x (24,000 - 14,400) = 7,848 - 0.72667 x 9,600 = 7,848 - 6,976.00 = **EUR 872.00/year (EUR 72.67/month)**. Source: [EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates).
- Income tax base = gross - unemployment 1.6% - II pillar 2% - monthly basic exemption = 2,000 - 32.00 - 40.00 - 72.67 = **EUR 1,855.33**. Income tax 22% = **EUR 408.17**.
- Net pay to employee = 2,000 - 32.00 - 40.00 - 408.17 = **EUR 1,519.83**.

**Classification:** Payroll computation. Employer-side cost EUR 2,676.00; the EMTA debit is EXCLUDED from VAT.

> Note on the II pillar state addition: EMTA's current guidance describes the state adding 4% of gross wage (drawn from the 20-point pension share of the employer's 33% social tax) to the II pillar member's account, on top of the employee's own 2/4/6% withholding -- this is NOT an extra cash cost to the employer. Source: [EMTA -- contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension). [RESEARCH GAP -- PwC's summary still states 2% (pre-2024 figure); reviewer to confirm the current addition against the Funded Pensions Act.]

### Example 3 -- Below-minimum part-time pay triggers the minimum social tax base (2025)

**Input:** Part-time resident employee, gross monthly pay EUR 500 in 2025, active employment all month.

**Reasoning:**
Gross EUR 500 is below the 2025 monthly minimum social tax base of EUR 820. Absent a documented reduction circumstance (mid-month start/end, statutory part-time exceptions, incapacity, parental leave -- see R-EE-PAY-4), the employer owes social tax on at least EUR 820: EUR 820 x 33% = **EUR 270.60 minimum monthly social tax**, NOT EUR 500 x 33% = EUR 165.00. Source: [EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax).

**Classification:** Social tax computed on the EUR 820 minimum base = EUR 270.60. Flag for reviewer whether a base reduction applies. EXCLUDE the EMTA debit from VAT.

### Example 4 -- Worker of pensionable age (employee unemployment premium not withheld)

**Input:** Resident employee aged 67, gross EUR 1,500, 2025.

**Reasoning:**
The employee's 1.6% unemployment premium is NOT withheld from persons of pensionable age (nor from those granted early-retirement / flexible old-age pension). The employer's 0.8% premium IS still due even for pensionable-age employees. Social tax (33% = EUR 495.00) and income tax (22%) apply normally; the employer unemployment premium = EUR 1,500 x 0.8% = EUR 12.00. Source: [EMTA -- unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums).

**Classification:** Social tax EUR 495.00 + income tax apply; employer unemployment premium EUR 12.00 applies; employee 1.6% premium does NOT apply. Flag for reviewer on borderline pension-age timing.

### Example 5 -- Net wage transfer to employee (NOT a tax payment)

**Input line:**
`31.01.2025 ; JAAN TAMM PALK JAAN 2025 ; DEBIT ; NETOPALK ; -1 519,83 ; EUR`

**Reasoning:**
Matches "PALK" / "NETOPALK" (pattern 4.3). This is the net wage paid to the employee, not a payroll-tax payment to EMTA. Do not classify as social tax. The associated taxes are settled separately via the monthly TSD payment to EMTA (see Example 1).

**Classification:** EXCLUDE -- payroll wage expense. NOT a tax payment to EMTA.

### Example 6 -- Late TSD payment with interest (arrears)

**Input line:**
`25.03.2025 ; MAKSU- JA TOLLIAMET ; DEBIT ; INTRESS / VIIVIS ; -45,80 ; EUR`

**Reasoning:**
Matches "MAKSU- JA TOLLIAMET" (pattern 4.1) but the reference indicates "intress / viivis" (interest). Late-payment interest on tax arrears runs at 0.06% per day (approx. 21.9% per annum) on unpaid tax from the day after the due date until payment. No interest is claimed if the amount is under EUR 10. The interest portion cannot be split from principal without an e-MTA statement. Source: [EMTA -- payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests).

**Classification:** EXCLUDE from VAT. Flag for reviewer -- request the e-MTA statement to split tax principal from late-payment interest (0.06%/day).

## Section 6 -- Tier 1 Rules

These rules apply when bank statement data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- Income tax withholding (flat 22%)

- **Income tax withholding formula** — income_tax = (gross - employee_unemployment_1.6% - II_pillar - monthly_basic_exemption) x 22%  _([EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))_
- **Flat income tax rate 2025/2026** — 22% (raised from 20% on 1 January 2025; withheld at source after deducting basic exemption, employee unemployment premium, II pillar contribution)  _([EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))_

### Rule 2 -- Basic exemption, 2025 (income taper -- the "tax hump")

**Basic exemption 2025 table**

| Item | 2025 |
| --- | --- |
| Maximum monthly basic exemption | EUR 654/month (EUR 7,848/year) |
| Full exemption | Monthly income up to EUR 1,200 (annual income up to EUR 14,400) |
| Taper formula | `7,848 - 7,848/10,800 x (annual_income - 14,400)` |
| Reaches EUR 0 | At annual income EUR 25,200 (nil above) |
| Pensionable-age basic exemption | EUR 776/month (EUR 9,312/year), applied automatically |

- **Application condition** — The monthly basic exemption is applied only if the employee has filed a written application, and by only one payer. [RESEARCH GAP -- the precise monthly withholding-agent taper formula should be cross-checked against the EMTA basic-exemption calculation page for edge cases; the pensionable-age exemption (EUR 776/month) should be re-confirmed on that page. Reviewer to confirm.]  _([EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))_

### Rule 3 -- Basic exemption, 2026 (CONFIRMED change -- flat, no taper)

- **2026 basic exemption change** — From 1 January 2026 the working-age basic exemption is a flat EUR 8,400/year (EUR 700/month) that does NOT decrease with income -- the income-based taper ("tax hump") is abolished. The pensionable-age exemption remains EUR 776/month (EUR 9,312/year).  _([EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates); [EY -- significant tax changes in Estonia in 2025-2026](https://www.ey.com/en_ee/insights/tax/significant-tax-changes-in-estonia-in-2025-2026))_

### Rule 4 -- Social tax formula

- **Social tax formula** — social_tax = max(gross_remuneration, minimum_base) x 33%  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax))_
- **Social tax components and cap** — 33% = 20% public pension insurance + 13% public health insurance. Minimum monthly base = EUR 820/month in 2025 (minimum social tax EUR 270.60) and EUR 886/month in 2026 (minimum social tax EUR 292.38). Social tax is uncapped -- there is no upper ceiling for regular employees.  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax))_

### Rule 5 -- Social tax is employer-paid, never withheld

- **Employer-paid social tax** — The full 33% social tax is paid by the EMPLOYER on top of gross pay (it also applies to directors' fees, service fees, and fringe benefits). The employee share is 0% -- it is NOT deducted from the employee's wage.  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax))_

### Rule 6 -- Minimum monthly social tax always applies

- **Minimum monthly social tax** — Even where gross pay is below the minimum base, the employer owes social tax on at least the minimum base: EUR 270.60/month in 2025 (820 x 33%) and EUR 292.38/month in 2026 (886 x 33%), unless a documented exemption applies (mid-month start/end, certain part-time exceptions, incapacity, reduced work capacity, parental leave, sometimes secondary employers -- see Tier 2).  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax))_

### Rule 7 -- Unemployment insurance premiums (rates fixed 1 Jan 2025 -- end 2028)

**Unemployment insurance premiums table**

| Share | Who pays | Rate | Base |
| --- | --- | --- | --- |
| Employee | Employee (withheld) | 1.6% | Gross wages/remuneration subject to the premium |
| Employer | Employer | 0.8% | Total gross wages of all employees (including those of pensionable age) |

- **No floor/ceiling; fixed rates** — No stated floor or ceiling. Rates are fixed at 1.6% / 0.8% for 2025-2028.  _([EMTA -- unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums))_

### Rule 8 -- Employee unemployment premium ceases at pensionable age

- **Pensionable-age exemption from employee premium** — The employee's 1.6% premium is NOT withheld from persons of pensionable age, or from those granted early-retirement / flexible old-age pension. The employer's 0.8% premium is still due even for pensionable-age employees.  _([EMTA -- unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums))_

### Rule 9 -- Mandatory funded pension (II pillar)

- **II pillar mandatory contribution rules** — The employee contributes 2%, 4% or 6% of gross salary (employee's election; statutory default 2%), withheld by the employer. Compulsory for residents born after 31 December 1982 (i.e. born 1983 or later); the obligation begins on 1 January of the year after the person turns 18. From 1 January 2025 the employee may elect 4% or 6% (application by 30 November, effective the following 1 January); the same elected rate applies across all employers. The employer checks the applicable rate via Pensionikeskus (1 Jan / 1 May / 1 Sep query points).  _([EMTA -- contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension); [Pensionikeskus](https://www.pensionikeskus.ee/en/ii-pillar/mandatory-funded-pension/))_

### Rule 10 -- II pillar state addition (4%, NOT an extra employer cost)

- **State II pillar addition** — For a II pillar member, the state transfers 4% of gross wage to the member's pension account, drawn from the 20-point pension-insurance share of the employer's 33% social tax. EMTA calculates and transfers it; it is not an additional cash cost to the employer. [RESEARCH GAP -- PwC still cites 2% (pre-2024 figure); reviewer to confirm the current addition against the Funded Pensions Act.]  _([EMTA -- contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension))_

### Rule 11 -- Employer total on-cost

- **Employer total on-cost summary** — Employer-side cost on top of gross = 33% social tax + 0.8% unemployment = ~33.8%. Employee-side withholdings from gross = 22% income tax (after basic exemption) + 1.6% unemployment + 2/4/6% II pillar.  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax); [EMTA -- unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums))_

### Rule 12 -- Minimum wage (reference -- not a tax base)

**Minimum wage table**  _([Palgakalkulaator -- minimum wage in Estonia](https://www.palgakalkulaator.ee/en/teadmiseks/miinimumpalk))_

| Period | Monthly | Hourly | Effective |
| --- | --- | --- | --- |
| 2025 | EUR 886 | EUR 5.31 | 1 January 2025 |
| 2026 (Jan-Mar) | EUR 886 | EUR 5.31 | continues |
| 2026 (from 1 Apr) | EUR 946 | EUR 5.67 | 1 April 2026 |

- **Distinction from minimum social tax base** — The minimum wage is distinct from the minimum social tax base (they coincide at EUR 886 in 2025 and Jan-Mar 2026). [RESEARCH GAP -- the April 2026 increase to EUR 946 follows a recent government regulation; reviewer to re-verify close to the period.]  _([Palgakalkulaator -- minimum wage in Estonia](https://www.palgakalkulaator.ee/en/teadmiseks/miinimumpalk))_

### Rule 13 -- Form TSD: monthly declaration and payment

- **Form TSD rule** — Form TSD (tulu- ja sotsiaalmaksu deklaratsioon) is the single combined monthly return reporting withheld income tax, social tax, both unemployment premium shares, and mandatory funded pension contributions. Annex 1 covers payments to resident natural persons; Annex 2 covers non-residents. Filed and paid via e-MTA by the 10th day of the month following the month of payment; the tax/contributions are also payable by the 10th.  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax))_

### Rule 14 -- Employment register before work commences

- **Employment register requirement** — The employer must enter each employment relationship in the Employment Register (töötamise register / TÖR via e-MTA) before the employee begins work (on or before the first day), recording the contract type, workplace address, job title, working-time rate and start date.  _([EMTA -- employment register](https://www.emta.ee/en/business-client/registration-business/employment-register))_

### Rule 15 -- Corporate-tax context (distributions only)

- **Distribution tax context** — Estonia taxes distributed profits, not retained earnings (the well-known deferral model). Dividends are NOT payroll and fall under a separate distribution-tax regime. This is context only for the dividend/payroll boundary.  _([PwC Worldwide Tax Summaries -- Estonia](https://taxsummaries.pwc.com/estonia/individual/other-taxes))_

## Section 7 -- Tier 2 Catalogue (Reviewer Judgement)

When data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation rather than computing automatically.

### T2-1 -- Minimum social tax base reductions

- **T2-1** — Trigger: Employee starts or ends employment mid-month, works part-time below the minimum base, is a reduced-work-capacity employee or pensioner, or had periods of temporary incapacity / parental leave. Issue: The minimum monthly social tax base (EUR 820 in 2025 / EUR 886 in 2026) can be reduced or disapplied in specified circumstances; the mechanics are fact-specific. Action: Flag for reviewer. Do not apply a reduced minimum base without confirmation (R-EE-PAY-4).

### T2-2 -- Pensionable-age worker (premium treatment)

- **T2-2** — Trigger: Worker is at or near the statutory pension age during the pay period. Issue: The employee 1.6% premium is not withheld from pensionable-age workers, but the employer 0.8% premium still applies; exact cut-off timing for a worker crossing the threshold mid-period needs confirmation. Action: Flag for reviewer.

### T2-3 -- II pillar rate change, opt-in, or state addition mechanics

- **T2-3** — Trigger: Employee elected (or wishes to elect) 4% or 6%, voluntarily joined the scheme, or the state's 4% addition must be quantified. Issue: Using the wrong elected rate misstates the withholding; the state's 4% addition is drawn from the employer's social tax, and some secondary sources still cite 2%. Action: Flag for reviewer. Confirm the elected rate and effective date via Pensionikeskus / e-MTA. [RESEARCH GAP -- state-addition figure.]

### T2-4 -- Payroll-tax arrears and interest

- **T2-4** — Trigger: Client has unpaid TSD liabilities from prior months. Issue: Late-payment interest accrues at 0.06% per day (~21.9% p.a.) on unpaid tax from the day after the due date; no interest is claimed below EUR 10. Action: Do not quantify arrears without an e-MTA statement. Escalate (R-EE-PAY-4).

### T2-5 -- Board-member fees and director remuneration

- **T2-5** — Trigger: Payment is a board member's (juhatuse liige) fee rather than employment salary. Issue: Board-member fees are subject to social tax and income tax, but unemployment-premium and II-pillar treatment can differ from ordinary employment. Action: Flag for reviewer. See R-EE-PAY-3.

### T2-6 -- Non-resident, e-resident, or posted-worker payroll

- **T2-6** — Trigger: Employee is a non-resident, employer is a non-resident/e-resident foreign company, or the worker is posted/seconded (A1 certificate, totalisation). Issue: Which state's social security applies, registration obligations, Annex 2 reporting on Form TSD, and whether Estonian social tax is due at all depend on EU coordination rules and treaties. Action: Flag for reviewer. Escalate per R-EE-PAY-3.

### T2-7 -- Annual basic-exemption reconciliation

- **T2-7** — Trigger: The 2025 income-dependent exemption was over- or under-applied during the year (common where total annual income crossed EUR 14,400 / EUR 25,200). Issue: The employee may owe additional tax or be due a refund on the annual individual return. Action: Flag for reviewer; the individual return (tuludeklaratsioon) is generally due by 30 April following the tax year.  _([EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))_

## Section 8 -- Excel Working Paper Template

When producing an Estonian payroll computation, structure the working paper as follows:

```
ESTONIA PAYROLL COMPUTATION -- WORKING PAPER
Client: [name]
Tax Period (month/year): [____]   (2025 or 2026 -- REQUIRED)
Prepared: [date]

INPUT DATA
  Gross monthly remuneration:       EUR [____]
  Employee birth year:              [____]
  II pillar member (born 1983+?):   [YES/NO]
  II pillar elected rate:           [2% / 4% / 6%]   (default 2%)
  Of pensionable age?:              [YES/NO]
  Basic-exemption application on file?: [YES/NO]
  Resident standard employee?:      [YES/NO]   (NO -> escalate, R-EE-PAY-3)

CONSTANTS (select by year)
  Minimum social tax base:          EUR [820 (2025) / 886 (2026)]
  Minimum monthly social tax:       EUR [270.60 (2025) / 292.38 (2026)]
  Social tax rate:                  33%   (20% pension + 13% health)
  Unemployment -- employer:          0.8%
  Unemployment -- employee:          1.6%   (0% if pensionable age)
  Income tax rate:                  22%
  Basic exemption (monthly):        EUR [2025 taper up to 654 / 2026 flat 700; 776 pensionable]

EMPLOYER-SIDE COST
  Social tax (max(gross, min base) x 33%):  EUR [____]
  Unemployment employer (gross x 0.8%):     EUR [____]
  Total employer cost on top of gross:      EUR [____]
  Total cost to employer (gross + above):   EUR [____]

EMPLOYEE-SIDE WITHHOLDINGS
  Unemployment employee (gross x 1.6%):     EUR [____]
  II pillar (gross x 2/4/6%):               EUR [____]
  Monthly basic exemption applied:          EUR [____]
  Taxable base (gross - 1.6% - II pillar - basic exemption): EUR [____]
  Income tax (taxable base x 22%):          EUR [____]
  Net pay to employee:                      EUR [____]

FORM TSD (monthly, due by 10th of following month)
  Withheld income tax:              EUR [____]
  Social tax:                       EUR [____]
  Unemployment (employer+employee): EUR [____]
  II pillar (employee):             EUR [____]
  Total TSD payment to EMTA:        EUR [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their tax impact]
```

## Section 9 -- Bank Statement / Terminology Reading Guide

### How payroll-tax debits appear on Estonian bank statements

**Swedbank:** "MAKSU- JA TOLLIAMET" / "EMTA" / "RIIGIMAKSUD" -- around the 10th of the month (TSD payment for the prior month's wages); bundled monthly figure (income tax + social tax + unemployment + II pillar).
**SEB Pank:** "MAKSU- JA TOLLIAMET" / "EMTA TSD" -- same monthly cycle (by the 10th).
**LHV Pank:** "EMTA" / "MAKSUAMET" / "SOTSIAALMAKS" -- same monthly cycle.
**Luminor / Coop Pank:** "MAKSU- JA TOLLIAMET" / "RIIGIMAKS" / "EMTA" -- same monthly cycle.

**Key identification tips:**
1. EMTA payroll-tax debits are outgoing (DEBIT) and recur monthly around the 10th.
2. A single EMTA debit usually bundles ALL payroll taxes for the month -- you cannot split income tax / social tax / unemployment / II pillar from the bank line alone; use the filed Form TSD.
3. Do not confuse the EMTA tax debit with the separate net-wage transfer ("PALK" / "NETOPALK") to the employee.
4. Inbound credits from "TÖÖTUKASSA" or "PENSION" are benefits received, not premiums/contributions paid.
5. Irregular EMTA debits referencing "intress" / "viivis" are late-payment interest (0.06%/day) -- flag for reviewer.
6. Amounts use a comma decimal separator and space thousands separator (e.g. `1 234,56`).

### Estonian payroll terminology (glossary)

**Glossary table**

| Estonian | English |
| --- | --- |
| Palgaarvestus | Payroll / wage computation |
| Tulumaks / kinnipeetud tulumaks | Income tax / withheld income tax |
| Sotsiaalmaks | Social tax (33%) |
| Töötuskindlustusmakse | Unemployment insurance premium |
| Kohustuslik kogumispension / II sammas | Mandatory funded pension / II pillar |
| Maksuvaba tulu | Basic exemption (tax-free allowance) |
| Palk / töötasu / netopalk | Wage / remuneration / net pay |
| Töötamise register (TÖR) | Employment register |
| Maksu- ja Tolliamet (EMTA) | Tax and Customs Board |
| Sotsiaalkindlustusamet | Social Insurance Board |
| Töötukassa | Unemployment Insurance Fund |
| Pensionikeskus | Funded-pension register administrator |
| Viivis / intress | Late-payment interest |
| Juhatuse liige | Board member |
| FIE (füüsilisest isikust ettevõtja) | Self-employed natural person |
| Vorm TSD | Form TSD (combined monthly payroll return) |

## Section 10 -- Onboarding Fallback

If the client provides only a bank statement and no other information:

1. **Scan for EMTA debits** -- identify all outgoing payments matching Section 4 patterns (MAKSU- JA TOLLIAMET / EMTA / SOTSIAALMAKS / TSD).
2. **Identify the monthly cycle** -- TSD payments recur around the 10th of each month; confirm one per pay month.
3. **Do NOT decompose the bundled figure from the bank line** -- the single EMTA debit mixes income tax, social tax, unemployment premiums and II pillar. Request the filed Form TSD for the authoritative split.
4. **Separate net-wage transfers** -- "PALK" / "NETOPALK" debits are wages to employees, not tax payments.
5. **Flag inbound benefit credits** -- "PENSION" / "TÖÖTUKASSA" / "HAIGUSHÜVITIS" are benefits received, not contributions.
6. **Flag for reviewer:** "Payroll classification derived from bank statement amounts only. Tax period, employee birth year, II pillar rate, basic-exemption status and pension-age status have not been independently verified. Reviewer must confirm against the filed Form TSD before relying on figures."

## Section 11 -- Reference Material

### Quick computation examples (standard resident employee, born 1990, II pillar 2%)

**Quick computation examples table**  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax); [EMTA -- unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums))_

| Period | Gross / month | Social tax (employer 33%) | Unemp. employer 0.8% | Total employer cost on top | Unemp. employee 1.6% | II pillar 2% |
| --- | --- | --- | --- | --- | --- | --- |
| 2025 | EUR 500 (below min base) | EUR 270.60 (on EUR 820 min) | EUR 4.00 | EUR 274.60 | EUR 8.00 | EUR 10.00 |
| 2025 | EUR 820 (= min base) | EUR 270.60 | EUR 6.56 | EUR 277.16 | EUR 13.12 | EUR 16.40 |
| 2025 | EUR 2,000 | EUR 660.00 | EUR 16.00 | EUR 676.00 | EUR 32.00 | EUR 40.00 |
| 2026 | EUR 886 (= min base) | EUR 292.38 | EUR 7.09 | EUR 299.47 | EUR 14.18 | EUR 17.72 |
| 2026 | EUR 3,000 | EUR 990.00 | EUR 24.00 | EUR 1,014.00 | EUR 48.00 | EUR 60.00 |

Note: income tax (22%) is computed on (gross - 1.6% unemployment - II pillar - applicable basic exemption); it is omitted from the employer-cost columns because it is an employee withholding. All rows verified to the cent.

### Forms

**Forms table**  _([EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax); [EMTA -- employment register](https://www.emta.ee/en/business-client/registration-business/employment-register); [EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))_

| Form | Purpose | Deadline |
| --- | --- | --- |
| Form TSD (tulu- ja sotsiaalmaksu deklaratsioon) | Combined monthly declaration of withheld income tax, social tax, unemployment premiums (employer + employee), and mandatory funded pension contributions; Annex 1 = residents, Annex 2 = non-residents; filed via e-MTA | By the 10th of the month following the month of payment; tax/contributions also payable by the 10th |
| Employment register entry (töötamise register, TÖR) | Register each employment relationship (contract type, workplace, job title, working-time rate, start date) | Before the employee begins work (on or before the first day) |
| Individual annual income tax return (tuludeklaratsioon) | Resident individual annual reconciliation of income and basic exemption | Generally by 30 April following the tax year |

### Thresholds

**Thresholds table**

| Threshold | Value | Source |
| --- | --- | --- |
| Social tax minimum monthly base (2025) | EUR 820/month -> minimum social tax EUR 270.60/month | [EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax) |
| Social tax minimum monthly base (2026) | EUR 886/month -> minimum social tax EUR 292.38/month | [EMTA -- social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax) |
| Basic exemption, working age (2025) | Up to EUR 654/month (EUR 7,848/year); full up to EUR 1,200/month income; tapers to EUR 0 between annual income EUR 14,400 and EUR 25,200 | [EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Basic exemption, working age (2026) | Flat EUR 700/month (EUR 8,400/year), no taper | [EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Basic exemption, pensionable age (2025 and 2026) | EUR 776/month (EUR 9,312/year), applied automatically | [EMTA -- tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| II pillar obligation | Mandatory for residents born 1983 or later | [EMTA -- contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension) |
| Minimum wage (2025) | EUR 886/month; EUR 5.31/hour | [Palgakalkulaator](https://www.palgakalkulaator.ee/en/teadmiseks/miinimumpalk) |
| Minimum wage (2026) | EUR 886/month Jan-Mar; EUR 946/month (EUR 5.67/hour) from 1 April | [Palgakalkulaator](https://www.palgakalkulaator.ee/en/teadmiseks/miinimumpalk) |

### Penalties

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| Late-payment interest on tax arrears | 0.06% per day (~21.9% p.a.) on unpaid tax/contributions from the day after the due date until paid. No interest claimed if the amount is under EUR 10. | [EMTA -- payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests) |
| Failure to register employment / late TSD | Misdemeanour fines under the Taxation Act (MKS); EMTA may issue assessment notices and apply enforcement. | [EMTA / Taxation Act (MKS)](https://www.emta.ee/en/business-client/registration-business/employment-register) -- [RESEARCH GAP -- exact monetary fine schedule not captured from a primary authoritative source; reviewer to confirm.] |

### Test Suite

All amounts independently recomputed and reconciled to the cent.

**Test 1:** 2025, gross EUR 2,000, resident born 1990, II pillar 2%. -> Social tax = EUR 660.00; unemployment employer = EUR 16.00; employer cost on top = EUR 676.00; total cost to employer = EUR 2,676.00; unemployment employee = EUR 32.00; II pillar employee = EUR 40.00; tapered monthly basic exemption EUR 72.67; income tax base EUR 1,855.33; income tax EUR 408.17; net pay EUR 1,519.83.

**Test 2:** 2025, gross EUR 500 part-time, no reduction circumstance. -> Social tax on the EUR 820 minimum base = EUR 270.60 (NOT EUR 165.00). Flag whether a base reduction applies.

**Test 3:** 2026, gross EUR 886 (= minimum base), born 1990, II pillar 2%. -> Social tax = EUR 292.38; unemployment employer = EUR 7.09; unemployment employee = EUR 14.18; II pillar = EUR 17.72.

**Test 4:** Worker of pensionable age, gross EUR 1,500, 2025. -> Social tax = EUR 495.00 and income tax (22%) apply; employer unemployment premium EUR 12.00 (0.8%) applies; employee 1.6% premium does NOT apply.

**Test 5:** Resident born 1980, no opt-in. -> II pillar is NOT mandatory (born before 1 Jan 1983); apply only if the employee voluntarily joined. Confirm membership before withholding.

**Test 6:** Employee elected 6% II pillar, gross EUR 2,500, 2025. -> II pillar withheld = EUR 150.00 (6%); social tax = EUR 825.00; unemployment employer = EUR 20.00; unemployment employee = EUR 40.00.

**Test 7:** Period not stated, gross EUR 700. -> STOP (R-EE-PAY-1). Cannot determine minimum base / basic exemption without the calendar year.

**Test 8:** 2026, gross EUR 3,000, born 1995, II pillar 2%, basic-exemption applied. -> Social tax = EUR 990.00; unemployment employer = EUR 24.00; employer cost on top = EUR 1,014.00; unemployment employee = EUR 48.00; II pillar = EUR 60.00; flat basic exemption EUR 700/month (no taper in 2026).

### Sources

- [EMTA -- Social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax) (Estonian Tax and Customs Board)
- [EMTA -- Unemployment insurance premiums](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums)
- [EMTA -- Tax rates (private client)](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates)
- [EMTA -- Contributions to mandatory funded pension](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension)
- [EMTA -- Employment register](https://www.emta.ee/en/business-client/registration-business/employment-register)
- [EMTA -- Payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests)
- [PwC Worldwide Tax Summaries -- Estonia (Individual, Other taxes)](https://taxsummaries.pwc.com/estonia/individual/other-taxes)
- [EY Estonia -- Significant tax changes in Estonia in 2025-2026](https://www.ey.com/en_ee/insights/tax/significant-tax-changes-in-estonia-in-2025-2026)
- [Palgakalkulaator -- Minimum wage in Estonia](https://www.palgakalkulaator.ee/en/teadmiseks/miinimumpalk)
- [Pensionikeskus -- Mandatory funded pension](https://www.pensionikeskus.ee/en/ii-pillar/mandatory-funded-pension/)

### Caveats

Figures are 2025 unless noted. CONFIRMED 2026 items (per EMTA / government): income tax stays 22% (a previously legislated rise to 24% and a 2% "security tax" surcharge were repealed); the working-age basic exemption becomes a flat EUR 8,400/year (EUR 700/month) with no taper; the social tax monthly minimum base rises to EUR 886 (minimum EUR 292.38/month); minimum wage EUR 886 Jan-Mar then EUR 946 (EUR 5.67/hour) from 1 April 2026. Points to verify before relying: (1) the II pillar state addition -- EMTA's current guidance describes the state adding 4% of gross wage (from the employer's social tax), while PwC still cites 2% (pre-2024 figure); 4% is used here per the authority but should be confirmed against the Funded Pensions Act; (2) the April 2026 minimum-wage regulation is recent -- re-verify close to the period; (3) the exact monetary fine schedule for late TSD / failure to register employment was not captured from a primary source (only the 0.06%/day interest is confirmed); (4) the precise 2025 monthly basic-exemption withholding formula for edge cases should be cross-checked against the EMTA calculation page. No personal income tax ceiling and no social tax ceiling exist for ordinary employees. Research confidence: high.

## PROHIBITIONS

- **Prohibitions list** — - NEVER withhold social tax from the employee -- the full 33% is an employer charge, never deducted from the worker. - NEVER apply an upper ceiling to social tax -- it is uncapped for regular employees. - NEVER skip the minimum social tax base -- gross below EUR 820 (2025) / EUR 886 (2026) still owes social tax on the minimum base unless a documented exemption applies. - NEVER use 20% income tax for 2025 or 2026 -- the flat rate is 22% from 1 January 2025. - NEVER apply the monthly basic exemption without a written employee application on file, and never via more than one payer. - NEVER mix the 2025 and 2026 constants (minimum base EUR 820 vs EUR 886; basic exemption income taper vs flat EUR 700). - NEVER compute II pillar without confirming membership (mandatory only for residents born 1983 or later) and the elected rate (default 2%). - NEVER add the state's 4% II pillar addition to the employer's cash cost -- it is drawn from the employer's existing social tax, not an extra outlay. - NEVER withhold the employee unemployment premium (1.6%) from a person of pensionable age -- but DO still charge the employer 0.8%. - NEVER treat the minimum wage (EUR 886 in 2025 / EUR 946 from 1 Apr 2026) as the minimum social tax base -- they are different figures. - NEVER decompose a bundled EMTA bank debit into individual taxes from the bank line alone -- use the filed Form TSD. - NEVER miss the Form TSD deadline (the 10th of the month following payment) -- late payment accrues interest at 0.06%/day. - NEVER advise on arrears or late-payment interest without an e-MTA statement -- do not estimate. - NEVER apply standard rules to non-residents, e-residents, posted workers, board members or FIE without escalating to an Estonian tax professional. - NEVER present payroll computations as definitive -- always label as estimated and direct the client to e-MTA / their filed Form TSD and a qualified Estonian professional.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an Estonian tax professional or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
