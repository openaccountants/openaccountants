---
name: my-epf-socso
description: Use this skill whenever asked about Malaysia EPF (KWSP), SOCSO (PERKESO), or EIS contributions. Trigger on phrases like "EPF Malaysia", "KWSP", "Kumpulan Wang Simpanan Pekerja", "SOCSO", "PERKESO", "EIS", "Employment Insurance System", "employer contribution Malaysia", "employee contribution Malaysia", "i-Saraan", "self-employed EPF", "social security Malaysia", or any question about mandatory employment contributions in Malaysia. Covers EPF rates, SOCSO rates, EIS rates, self-employed options, and registration. ALWAYS read this skill before advising on Malaysian employment contributions.
version: 1.0
jurisdiction: MY
tax_year: 2026
last_updated: 2026-09-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - my-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malaysia employer contributions: EPF (KWSP), SOCSO (PERKESO) including LINDUNG 24 Jam, EIS, and registration (2026, with notes on earlier months)

Figures are for 2026 contribution months (calendar year 2026) unless a line says otherwise. SOCSO and EIS amounts come from PERKESO's schedules. The ceiling for both is RM6,000 a month, from 1 October 2024 ([PERKESO contribution rate](https://www.perkeso.gov.my/en/rate-of-contribution.html)). From 1 June 2026 there is a new employee-funded SOCSO scheme, LINDUNG 24 Jam. Since 8 July 2026 it is voluntary for local employees and mandatory for foreign workers ([PERKESO LINDUNG 24 Jam](https://www.perkeso.gov.my/en/skim-kemalangan-bukan-bencana-kerja-lindung-24-jam.html)).

**EPF figures are not reproduced in this edition.** The EPF (KWSP) website blocked automated access when this Guide was prepared, so we could not check the EPF rate table against an official page. This Guide explains how to apply EPF and tells you where to read the rate. It does not state a rate we could not verify. Before quoting an EPF percentage, read it from the Third Schedule to the EPF Act 1991 or the contribution calculator on the KWSP website (kwsp.gov.my).

## Scope and who this is for

- **Covers:** private-sector employers in Malaysia with one or more employees, and their payroll advisers. It covers:
  - EPF (Employees Provident Fund, KWSP): who must contribute, how the Third Schedule works, foreign employees, and what to check with KWSP;
  - SOCSO (PERKESO) under the Employees' Social Security Act 1969 (Act 4): the Employment Injury Scheme, the Invalidity Scheme and the new Non-Employment Injury Scheme (LINDUNG 24 Jam);
  - EIS (Employment Insurance System, LINDUNG KERJAYA) under the Employment Insurance System Act 2017 (Act 800);
  - registration, monthly payment, late-payment interest and penalties for SOCSO and EIS;
  - how the employee's EPF and SOCSO/EIS contributions feed into Monthly Tax Deduction (PCB/MTD) reliefs.
- **Does not cover:**
  - the MTD/PCB tax calculation itself;
  - the HRD Corp training levy (see "When to refuse or refer");
  - public-sector pension schemes;
  - the self-employed EPF scheme (i-Saraan) beyond a pointer;
  - benefit claims.

## Ask the client first

1. **Who is on the payroll?** For each person:
   - citizen, permanent resident or foreign worker;
   - date of birth, which gives the age in the contribution month;
   - whether they paid SOCSO before age 55 (and EIS before age 57);
   - start date.
2. **Is anyone a domestic worker, a spouse of the employer, a casual worker outside your business, or a civil servant?** These groups are treated differently under Act 800 (see the boundary table).
3. **What does each person get paid?** For each month, split out:
   - salary, overtime, commission, service charge, leave pay and allowances;
   - annual bonus, gratuity, mileage claims and payments to statutory funds, which are **not** SOCSO/EIS wages.
4. **LINDUNG 24 Jam status.** Did any existing local employee opt out through the LINDUNG Faedah Portal during the window of 13 July to 31 August 2026? Does any new local hire want to opt out? For a new hire, the employer must file the opt-out notice before the first month's deduction. Does anyone have more than one employer?
5. **Is the business registered with PERKESO (ASSIST Portal) and with KWSP?** Since when? Are there unpaid or late months?
6. **Headcount and industry,** to decide whether HRD Corp levy rules may apply (refer out).

## The method, step by step

1. **Register the employer.** Register with PERKESO on the ASSIST Portal. Upload:
   - Borang 1 (employer) and Borang 2 (employee) for Act 4;
   - Borang SIP 1 and SIP 2 for EIS ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).

   For foreign workers, use the foreign-worker registration form instead of Borang 2. SIP 1 and SIP 2 are not required for them ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)). Act 800 requires an employer to register "within such period and in such manner as prescribed" ([Act 800, s.14](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf)). Register the business when you hire the first employee, and confirm the prescribed period with PERKESO. Register each employee who starts later within thirty days of the start date (Act 800, s.16(1)(b)). Register with KWSP as an employer at the same time.
2. **Classify each employee for SOCSO (Act 4).**
   - **First Category:** Employment Injury + Invalidity. It covers employees under 60.
   - **Second Category:** Employment Injury only, paid by the employer. It covers employees who have reached 60, and anyone who first becomes eligible at age 55 or over with no earlier contributions ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html)).
3. **Decide LINDUNG 24 Jam (Non-Employment Injury Scheme) for each employee.**
   - **Foreign workers:** mandatory.
   - **Local employees:** voluntary from 8 July 2026, with opt-in by default. Only an employee who opted out through PERKESO is excluded. For a new local hire, the employer registers the employee on ASSIST. If the employee chooses to opt out, the employer submits the Notis Pelepasan Liabiliti (liability release notice) before the first month's contribution is deducted ([PERKESO LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf), Q28).
   - The contribution is the employee's alone, but the employer deducts it and pays it to PERKESO. There is no age limit.
4. **Classify each employee for EIS (Act 800).** Employees aged 18 to 60 contribute. Anyone aged 57 or over with no EIS contributions before 57 is exempt. Public servants, local authority and statutory body employees, domestic servants and the employer's spouse are outside the Act.
5. **Work out wages for SOCSO/EIS.** Include:
   - salary, overtime, commission, service charge and leave pay;
   - allowances (shift, meal, cost of living, housing, etc.).

   Exclude:
   - employer payments to statutory funds;
   - mileage claims;
   - gratuity or termination payments;
   - the annual bonus ([PERKESO employer registration, "Definition Of Wages"](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
6. **Read the amount from the schedule, not a percentage.** SOCSO and EIS are fixed ringgit amounts per wage band of RM100. The percentages describe the design, and the table decides the amount. Wages above RM6,000 use the top band.
7. **Apply EPF.** For each employee:
   - take the employee's EPF wages;
   - find the row for the wage band and the employee's category (age, citizenship or residence, and for older members the date they joined);
   - deduct the employee share and add the employer share.

   Read the rates from the Third Schedule on the KWSP website. For non-Malaysian-citizen employees, there has been a separate mandatory contribution since October 2025 wages under the EPF (Amendment) Act 2025. Confirm the rate and coverage with KWSP.
8. **Pay by the 15th of the following month.** Pay SOCSO and EIS through ASSIST (FPX, direct debit, internet banking or a bank counter) ([PERKESO contribution payment](https://www.perkeso.gov.my/en/our-services/employer-employee/pembayaran.html)). Pay EPF through KWSP's employer channel by KWSP's due date.
9. **Keep records.** For each employee, keep a monthly record of:
   - name, identity card number and occupation;
   - contributions;
   - wages and allowances.

   Keep them for seven years from the last entry ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
10. **Feed the payroll tax reliefs.** The employee's EPF and SOCSO/EIS contributions reduce the MTD calculation, within the reliefs listed below.

## Figures for 2026

### SOCSO (Act 4): rates and ceiling ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [PERKESO contribution rate](https://www.perkeso.gov.my/en/rate-of-contribution.html))

| Item | Employer | Employee | Notes |
| --- | --- | --- | --- |
| First Category (Employment Injury + Invalidity), under 60 | 1.75% | 0.5% | Amounts per the Third Schedule table |
| Second Category (Employment Injury only), 60 and over, or first eligible at 55+ | 1.25% | nil | Paid by the employer |
| Wage ceiling from 1 October 2024 | RM6,000 | RM6,000 | Before October 2024: RM5,000 |

### LINDUNG 24 Jam (Non-Employment Injury Scheme), from 1 June 2026 ([PERKESO foreign workers](https://www.perkeso.gov.my/en/our-services/protection/foreign-worker.html); [PERKESO LINDUNG 24 Jam](https://www.perkeso.gov.my/en/skim-kemalangan-bukan-bencana-kerja-lindung-24-jam.html))

| Phase | Years from 1 June 2026 | Employee rate | Employer rate |
| --- | --- | --- | --- |
| Phase 1 | 1 June 2026 to 31 May 2028 (years 1-2) | 0.75% | nil |
| Phase 2 | 1 June 2028 to 31 May 2031 (years 3-5) | 1.00% | nil |
| Phase 3 | From 1 June 2031 (year 6 onwards) | 1.25% | nil |

The rate applies to monthly wages up to the RM6,000 ceiling. PERKESO says the phased increases are subject to confirmation of their effective dates ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf), Q31).

The combined split in Phase 1 for a First Category employee who is covered by LINDUNG 24 Jam:
- **Employer:** 1.25% Employment Injury + 0.5% Invalidity = 1.75%.
- **Employee:** 0.5% Invalidity + 0.75% LINDUNG 24 Jam = 1.25%.

([PERKESO foreign workers](https://www.perkeso.gov.my/en/our-services/protection/foreign-worker.html))

### SOCSO table extracts, monthly amounts from June 2026 ([PERKESO table including LINDUNG 24 Jam](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf))

These extracts are for checking only. Use the full table for any other band.

| Monthly wages | First Cat. employer | First Cat. employee (Invalidity) | LINDUNG 24 Jam (employee) | First Cat. total | Second Cat. employer | Second Cat. LINDUNG 24 Jam (employee) | Second Cat. total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Over RM2,400, not over RM2,500 | RM42.85 | RM12.25 | RM18.35 | RM73.45 | RM30.60 | RM18.35 | RM48.95 |
| Over RM3,900, not over RM4,000 | RM69.15 | RM19.75 | RM29.65 | RM118.55 | RM49.40 | RM29.65 | RM79.05 |
| Over RM5,900, and all wages over RM6,000 | RM104.15 | RM29.75 | RM44.65 | RM178.55 | RM74.40 | RM44.65 | RM119.05 |

- **Local employee who opted out of LINDUNG 24 Jam:** leave out the LINDUNG 24 Jam column. The total is then the employer amount plus the Invalidity amount (First Category), or the employer amount alone (Second Category).
- **Maximum monthly SOCSO without LINDUNG 24 Jam:** RM104.15 employer + RM29.75 employee = RM133.90.

### EIS (Act 800) ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [Act A1725, Second Schedule amendment](https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf); [Act 800](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf))

| Item | Employer | Employee | Total |
| --- | --- | --- | --- |
| Rate (on assumed monthly wage) | 0.2% | 0.2% | 0.4% |
| Wages over RM2,400, not over RM2,500 | RM4.90 | RM4.90 | RM9.80 |
| Wages over RM3,900, not over RM4,000 | RM7.90 | RM7.90 | RM15.80 |
| Wages over RM5,900 (top band, ceiling RM6,000) | RM11.90 | RM11.90 | RM23.80 |

Act A1725 raised the EIS ceiling from "five thousand ringgit" to "six thousand ringgit" and added the bands above RM5,000. Under the Act, EIS contributions stop when the employee reaches the minimum retirement age.

### Self-employed and housewives' SOCSO schemes ([PERKESO contribution rate](https://www.perkeso.gov.my/en/rate-of-contribution.html))

| Scheme | Contribution |
| --- | --- |
| Self-Employment Social Security Scheme (Act 789) | RM13.10, RM19.40, RM36.90 or RM49.40 a month (insured monthly earnings RM1,050, RM1,550, RM2,950 or RM3,950) |
| Housewives' Social Security Scheme (Act 838) | RM120 paid in advance for 12 consecutive months |

### Payroll tax reliefs that use these contributions, 2026 ([MTD specification 2026](https://www.hasil.gov.my/wp-content/uploads/spesifikasi-kaedah-pengiraan-berkomputer-pcb-2026.pdf); [TP1 explanatory notes 2026](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf))

| Relief | Limit |
| --- | --- |
| EPF, mandatory and voluntary, or other approved scheme | RM4,000 |
| Life insurance or family takaful (a separate limit) | RM3,000 |
| SOCSO contributions under Act 4 or Act 800 (includes EIS) | RM350 |

- **Employee share only:** the employer's EPF share does not count towards the employee's relief.
- **No mandatory EPF:** under the MTD specification, a person with no mandatory EPF contribution (for example, one paid only a director's fee) can claim voluntary EPF of up to RM7,000.

### EPF: what to check with KWSP

- **Rates:** read the employee and employer rates from the Third Schedule to the EPF Act 1991 for the right wage band and category. Rates differ by:
  - wage band;
  - age (below 60, or 60 and over);
  - citizenship or residence;
  - for some older members, the date they first joined.

  Do not rely on percentages recalled from earlier years. The rules for employees aged 60 and over, in particular, have changed more than once.
- **Non-citizen employees:** a mandatory contribution from October 2025 wages, under the EPF (Amendment) Act 2025, has been reported. We could not verify it on an official page. Confirm with KWSP:
  - the gazetted rate;
  - the exclusion for domestic servants;
  - which work passes are covered.
- **Due date, late-payment charge and dividend on late contributions:** confirm with KWSP. This edition could not verify them.

## Boundaries and exceptions

| Situation | SOCSO (Act 4) | LINDUNG 24 Jam | EIS (Act 800) | Source |
| --- | --- | --- | --- | --- |
| Local employee under 55, first joins | First Category | Yes, unless they opted out | Yes, if aged 18 or over | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| New employee aged 55 to 56, no earlier SOCSO contributions | Second Category | Yes, unless they opted out | Yes (under 57) | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| New employee aged 57 to 59, no earlier EIS contributions | Second Category if no earlier SOCSO | Yes, unless they opted out | Exempt | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Employee who has reached 60 | Second Category (employer only) | Yes, unless they opted out (no age limit) | No | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf) |
| Foreign worker with a valid passport and work pass | First Category if they first join before 55; Second Category if they join at 55+ or have reached 60 | Mandatory | PERKESO's registration guidance does not require SIP forms for foreign workers; confirm EIS status with PERKESO | [PERKESO foreign workers](https://www.perkeso.gov.my/en/our-services/protection/foreign-worker.html); [PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/) |
| Domestic worker | Separate domestic-worker rules | Refer to PERKESO | Outside Act 800 | [Act 800, First Schedule](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf) |
| Public servant, or local authority or statutory body employee | Refer | Refer | Outside Act 800 | [Act 800, First Schedule](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf) |
| Employer's spouse, or a casual worker not employed for the business | Refer | Refer | Outside Act 800 | [Act 800, First Schedule](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf) |
| Temporary or part-time worker | Must be registered | As for others | As for others | [PERKESO FAQ](https://www.perkeso.gov.my/en/contact-us/pejabat-perkeso-new/frequently-asked-question.html) |
| Employee with two employers | Confirm each employer's share with PERKESO | Only one employer (chosen by the employee, or set by PERKESO) deducts | Confirm with PERKESO (Act 800 s.19) | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf) |
| Month with no wages paid | Contributions follow wages paid | No cover that month | Contributions follow wages paid | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf) |
| Accident outside Malaysia | Work-related: normal rules | Not covered | n/a | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf) |

**Opt-out mechanics (local employees).**
- **Who acts (existing employees, 2026 window):** the employee, through the LINDUNG Faedah Portal, or with a paper liability release notice if the portal is offline.
- **New local hires (after the window):** the employer registers the new employee on ASSIST. If the employee chooses to opt out, the employer submits the Notis Pelepasan Liabiliti before the first month's contribution is deducted (FAQ Q28).
- **Window:** 13 July to 31 August 2026.
- **Default:** anyone who did not opt out stays covered ("Once In, Always In"). An employee who opted out can later opt in, from the month of the choice.
- **June 2026:** mandatory for everyone, and not refundable. Any shortfall in June 2026 deductions must be made up from the employee's wages.
- **Refunds:** the employer claims them through ASSIST for July 2026 onwards; employees cannot claim directly.
- **Opting in mid-month:** the contribution for that month is based on the full month's wages (FAQ Q50).
- **Grace period:** PERKESO gave employers six (6) months after the scheme started with no penalty or legal action for LINDUNG 24 Jam contribution non-compliance. Other non-compliance is still enforced (FAQ Q37) ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf)).

## Worked cases

In these cases, "employee total" means the SOCSO and EIS deducted from pay; EPF is left out. All amounts are from the schedules linked above.

### Case 1: citizen aged 35, wages RM4,000, July 2026, has not opted out ([PERKESO table](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf); [Act 800](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf))

- **Wages:** RM3,700 salary + RM300 housing allowance = RM4,000. The allowance is wages. The band is over RM3,900, not over RM4,000.
- **SOCSO First Category:** employer RM69.15; employee RM19.75 Invalidity + RM29.65 LINDUNG 24 Jam = RM49.40.
- **EIS:** RM7.90 employer and RM7.90 employee.
- **Totals:** employee RM49.40 + RM7.90 = RM57.30; employer RM69.15 + RM7.90 = RM77.05.
- **If the employee had opted out:** the employee pays RM19.75 + RM7.90 = RM27.65.

### Case 2: citizen aged 40, wages RM8,000, opted out of LINDUNG 24 Jam ([PERKESO contribution rate](https://www.perkeso.gov.my/en/rate-of-contribution.html); [Act A1725](https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf))

- **Ceiling:** wages are above the RM6,000 ceiling, so the top band applies.
- **SOCSO:** employer RM104.15; employee RM29.75.
- **EIS:** RM11.90 each.
- **Totals:** employee RM29.75 + RM11.90 = RM41.65; employer RM104.15 + RM11.90 = RM116.05.

### Case 3: foreign worker aged 30, wages RM2,500, August 2026 ([PERKESO foreign workers](https://www.perkeso.gov.my/en/our-services/protection/foreign-worker.html); [PERKESO table](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf))

- **Category:** First Category, and LINDUNG 24 Jam is mandatory.
- **SOCSO:** employer RM42.85; worker RM12.25 + RM18.35 = RM30.60.
- **EIS:** PERKESO does not ask for SIP forms for foreign workers, so confirm with PERKESO before deducting EIS.
- **EPF:** a mandatory non-citizen contribution has been reported; confirm the rate and coverage with KWSP.

### Case 4: citizen aged 61, wages RM4,000, has not opted out ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [PERKESO table](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf))

- **SOCSO Second Category:** employer RM49.40; LINDUNG 24 Jam deducted from the employee RM29.65; total RM79.05.
- **EIS:** none, because the employee has reached 60.

### Case 5: new hire aged 56, never paid SOCSO or EIS, wages RM2,500 ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [Act 800](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf))

- **SOCSO:** first eligible at 55 or over, so Second Category. Employer RM30.60; LINDUNG 24 Jam RM18.35 from the employee. The exception is where the employee chooses to opt out and the employer files the Notis Pelepasan Liabiliti when registering them on ASSIST, before the first deduction ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf), Q28).
- **EIS:** the employee is under 57, so EIS applies. RM4.90 each.
- **Totals:** employee RM18.35 + RM4.90 = RM23.25; employer RM30.60 + RM4.90 = RM35.50.

### Case 6: annual bonus and late payment ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/); [PERKESO FAQ](https://www.perkeso.gov.my/en/contact-us/pejabat-perkeso-new/frequently-asked-question.html))

- **Bonus:** in December the employee earns RM3,950 salary plus an annual bonus of RM5,000. The annual bonus is not SOCSO/EIS wages, so the band stays over RM3,900, not over RM4,000.
- **Late payment:** the employer pays July 2026 contributions of RM500 fourteen days after 15 August 2026. Interest is 6% a year for each day late: RM500 x 6% x 14 / 365 = about RM1.15. That is less than RM5, so RM5 is charged.

## Earlier months: October 2024 to June 2026

- **October 2024 to May 2026:** the RM6,000 ceiling applied, and there was no LINDUNG 24 Jam column. Use the employer and Invalidity columns only ([PERKESO contribution rate](https://www.perkeso.gov.my/en/rate-of-contribution.html)).
- **Before October 2024:** the ceiling was RM5,000.
- **June 2026:** LINDUNG 24 Jam was mandatory for every employee under the Employees' Social Security (Amendment) Act 2026. June contributions cannot be refunded. If they were not deducted, the employer must deduct the arrears ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/faq-2.1.pdf)).
- **Returns being filed now:** the 2025 employer return (Form E) and employees' EA statements are handled under the income tax rules and are outside this Guide.

## When to refuse or refer

- **EPF rates, EPF late-payment charges, EPF registration timing, i-Saraan:** refer to KWSP or to a Malaysian payroll professional who can read the KWSP Third Schedule. Do not quote EPF percentages from memory.
- **HRD Corp levy:** whether an employer must register and pay the levy depends on its industry and headcount under the Pembangunan Sumber Manusia Berhad Act 2001. This Guide does not state the rates. Refer to HRD Corp.
- **Foreign workers and EIS:** refer to PERKESO where it is unclear whether EIS is due.
- **Domestic workers, public-sector staff, and employees with several employers:** refer to PERKESO.
- **Prosecution or compound notices, and disputes over arrears:** refer to a lawyer or a PERKESO/KWSP office.

## Filing and payment

- **SOCSO and EIS due date:** "no later than the 15th day of each succeeding month". For example, July contributions are due by 15 August ([PERKESO contribution payment](https://www.perkeso.gov.my/en/our-services/employer-employee/pembayaran.html)).
- **Channels:** ASSIST Portal with FPX, direct debit, internet banking, or a bank counter using the ACR reference.
- **Late interest (SOCSO/EIS):** 6% per annum for each day late, with a minimum of RM5 a month ([PERKESO FAQ](https://www.perkeso.gov.my/en/contact-us/pejabat-perkeso-new/frequently-asked-question.html)).
- **Penalties (Act 4):** failure to register or contribute can lead to prosecution: a fine not exceeding ten thousand ringgit, imprisonment of up to two years, or both. The foreign-worker page states the same maximum, RM10,000.00 or 2 years ([PERKESO foreign workers](https://www.perkeso.gov.my/en/our-services/protection/foreign-worker.html)).
- **Penalties (Act 800):** failing to register carries a fine not exceeding ten thousand ringgit, imprisonment of up to two years, or both ([Act 800, s.14](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf)).
- **Registering employees (Act 800):** employees who start after the industry is registered must be registered and insured within thirty days from the date they enter employment ([Act 800, s.16(1)(b)](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf)).
- **Accidents:** report work-related accidents within 48 hours of notification.
- **Ceasing to be an employer:** submit Form 1A (Act 4) and Form SIP 3 (Act 800) within 30 days of ceasing ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
- **EPF:** pay through KWSP's employer channels by KWSP's due date. Confirm the date and the late charges with KWSP.

## Completion checklist

- [ ] Every employee is classified: citizen or PR or foreign worker, age, and earlier SOCSO/EIS history.
- [ ] Employer and employees are registered on ASSIST (Borang 1 and 2, SIP 1 and 2 where required; see [PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)) and with KWSP.
- [ ] SOCSO/EIS wages exclude the annual bonus, gratuity, mileage claims and statutory fund payments.
- [ ] SOCSO category and band are read from the current table, with top band for wages over RM6,000.
- [ ] LINDUNG 24 Jam is deducted for foreign workers and for local employees who did not opt out; June 2026 arrears are handled.
- [ ] EIS is applied only to employees aged 18 to 60 who are not exempt.
- [ ] EPF rates are read from the KWSP Third Schedule for each employee's category.
- [ ] Payment is made by the 15th of the following month and receipts are kept; records are kept for seven years.
- [ ] Employee contributions are passed to the MTD calculation within the RM4,000 EPF and RM350 SOCSO relief limits.

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
