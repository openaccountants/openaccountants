---
name: my-epf-socso
description: "Use this skill whenever asked about Malaysia EPF (KWSP), SOCSO (PERKESO), or EIS contributions. Trigger on phrases like \"EPF Malaysia\", \"KWSP\", \"Kumpulan Wang Simpanan Pekerja\", \"SOCSO\", \"PERKESO\", \"EIS\", \"Employment Insurance System\", \"employer contribution Malaysia\", \"employee contribution Malaysia\", \"i-Saraan\", \"self-employed EPF\", \"social security Malaysia\", or any question about mandatory employment contributions in Malaysia. Covers EPF rates, SOCSO rates, EIS rates, self-employed options, and registration. ALWAYS read this skill before advising on Malaysian employment contributions."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/my-epf-socso"
  jurisdiction: "MY"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# Malaysia employer contributions: EPF (KWSP), SOCSO (PERKESO) including LINDUNG 24 Jam, EIS, and registration (2026, with notes on earlier months)

Figures are for 2026 contribution months (calendar year 2026) unless a line says otherwise. SOCSO and EIS amounts come from PERKESO's schedules. The ceiling for both is RM 6,000 a month, from 1 October 2024 ([PERKESO contribution schedule](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf)). From 1 June 2026 there is a new employee-funded SOCSO scheme, LINDUNG 24 Jam. From 8 July 2026 a transitional opt-out applied to existing local employees. Cover remains mandatory for first-time entrants and foreign workers ([PERKESO LINDUNG 24 Jam](https://www.perkeso.gov.my/skim-kemalangan-bukan-bencana-kerja-lindung-24-jam.html)).

**Read the wage band before calculating.** EPF rates are now verified from KWSP's current [Third Schedule](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025); SOCSO and EIS use their own schedules. Do not use the SOCSO wage exclusions for EPF or assume that a percentage gives the scheduled ringgit amount. Check the employee's actual LINDUNG participation, not just the word “voluntary”. First-time PERKESO entrants must contribute; existing local workers cannot newly opt out after 31 August 2026 ([FAQ v 2.3 Q 25 to Q 29](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf)).

## Scope and who this is for

- **Covers:** private-sector employers in Malaysia with one or more employees, and their payroll advisers. It covers:
  - EPF (Employees Provident Fund, KWSP): who must contribute, how the Third Schedule works, foreign employees, and what to check with KWSP;
  - SOCSO (PERKESO) under the Employees' Social Security Act 1969 (Act 4): the Employment Injury Scheme, the Invalidity Scheme and the new Non-Employment Injury Scheme (LINDUNG 24 Jam);
  - EIS (Employment Insurance System, LINDUNG KERJAYA) under the Employment Insurance System and Employment Services Act 2017 (Act 800);
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
   - citizenship or immigration status, including the prescribed identity card where relevant;
   - date of birth, which gives the age in the contribution month;
   - prior SOCSO coverage and contributions, and whether EIS contributions were payable before age 57;
   - start date.
2. **Is anyone a domestic worker, a spouse of the employer, a casual worker outside your business, or a civil servant?** Check their employment and eligibility against the boundary table.
3. **What does each person get paid?** For each month, split out:
   - salary, overtime, commission, service charge, leave pay and allowances;
   - annual bonus, gratuity, mileage claims and employer payments to statutory funds, which are excluded from SOCSO/EIS wages.
4. **LINDUNG 24 Jam status.** Did any existing local employee opt out through the LINDUNG Faedah Portal during the window of 13 July to 31 August 2026? Has a previously opted-out employee rejoined? A first-time PERKESO entrant must contribute, and no new opt-out is permitted after 31 August 2026. Obtain the ASSIST status and PERKESO notification, including any selected employer. Does anyone have more than one employer?
5. **Is the business registered with PERKESO (ASSIST Portal) and with KWSP?** Since when? Are there unpaid or late months?
6. **Headcount and industry,** to decide whether HRD Corp levy rules may apply (refer out).

## The method, step by step

1. **Register the employer.** Register with PERKESO on the ASSIST Portal. Upload:
   - Borang 1 (employer) and Borang 2 (employee) for Act 4;
   - Borang SIP 1 and SIP 2 for EIS ([PERKESO employer registration](https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).

   Use the applicable PERKESO foreign-worker registration form. Submit EIS forms for employees within Act 800, including any foreign employee who qualifies under First Schedule paragraph 10 ([PERKESO employer registration](https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/)). Act 800 requires an employer to register "within such period and in such manner as prescribed" ([Act 800, s.14](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf)). Register the business when you hire the first employee. The EIS employer application is due within 30 days from the Act applying to the industry (P.U.(A)452/2017 reg.2). Use SIP 2 to register employees already employed on the date of industry registration and to register later hires within 30 days of entering employment (Act 800 s. 16(1)). [Register with KWSP](https://www.kwsp.gov.my/en/employer/responsibilities/registration) within 7 days of first becoming liable to contribute. [EIS registration regulations regs.2 to 4](https://perkeso.gov.my/images/akta/ACT%20800/P.U%28A%29/P.U.%20%28A%29%20452%20-%20PP%20SIP%20%28Pendaftaran%20dan%20Caruman%29%202017_PERATURAN-PERATURAN%20SISTEM%20INSURANS%20PEKERJAAN%20%28PENDAFTARAN%20DAN%20CARUMAN%29%202017.pdf).
2. **Classify each employee for SOCSO (Act 4).**
   - **First Category:** Employment Injury and Invalidity for employees under 60 who qualify for Invalidity. Check the first-entry rule below.
   - **Second Category:** Employment Injury only, paid by the employer. It covers employees who have reached 60, and anyone who first becomes eligible at age 55 or over with no earlier contributions ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html)).
3. **Decide LINDUNG 24 Jam (Non-Employment Injury Scheme) for each employee.**
   - **Foreign workers:** mandatory.
   - **Local employees:** the voluntary change on 8 July 2026 had a closed opt-out window. Existing locals who did not opt out by 31 August remain in; first-time entrants are mandatory and the employer registers them on ASSIST and deducts from the first salary month ([PERKESO LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf), Q 25 to Q 29).
   - The contribution is the employee's alone, but the employer deducts it and pays it to PERKESO. There is no age limit.
4. **Classify each employee for EIS (Act 800).** Apply EIS to eligible employees from age 18 until they reach 60. From age 57, exclude an employee for whom no EIS contributions were payable before 57. The [Act 800 First Schedule](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf) also excludes members of the federal and state public services, local-authority and statutory-body employees, and casual workers engaged outside the employer's industry. Eligible domestic workers and spouses employed under a contract of service can qualify. For a non-citizen, check paragraph 10 for the prescribed permanent-resident identity card or temporary-resident identity card, including the applicable immigration or undetermined-citizenship tests. From 1 October 2026 the employer may recover the employee's contribution through wages and must bear its own share under [Act A1796 s. 6](https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/3696918_BI/Act%20A1796%20-%20EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202026.pdf).
5. **Work out wages for SOCSO/EIS.** Include:
   - salary, overtime, commission, service charge and leave pay;
   - allowances (shift, meal, cost of living, housing, etc.).

   Exclude:
   - employer payments to statutory funds;
   - mileage claims;
   - gratuity or termination payments;
   - the annual bonus ([PERKESO employer registration, "Definition Of Wages"](https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
6. **Read the amount from the schedule, not a percentage.** SOCSO and EIS are fixed ringgit amounts per scheduled wage band; the lowest bands are narrower than RM 100. The percentages describe the design, and the table decides the amount. Wages above RM 6,000 use the top band.
7. **Apply EPF separately.** Classify the employee under Third Schedule Part A (under 60 citizen/PR/pre-August 1998 member), Part C (older PR/pre-August 1998 member), Part E (citizen 60+) or Part F (other non-citizens), with the actual wage period and membership history. KWSP states that contributions run up to age 75; resolve the boundary month with KWSP rather than extending these categories indefinitely. Read that part's ringgit wage band, not a payroll-wide flat percentage. Part F has applied from October 2025 wages. Contributions are not capped at the SOCSO/EIS ceiling. Do not assume EPF excludes an annual bonus merely because SOCSO does. [Third Schedule](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025); [KWSP mandatory contributions](https://www.kwsp.gov.my/en/employer/responsibilities/mandatory-contribution).

8. **Pay by the 15 th of the following month.** Pay SOCSO and EIS through ASSIST (FPX, direct debit, internet banking or a bank counter) ([PERKESO contribution payment](https://perkeso.gov.my/en/contribution-payment.html)). Pay EPF through KWSP's employer channel by the 15 th of the following month ([KWSP non-citizen contribution guidance](https://www.kwsp.gov.my/en/employer/responsibilities/non-malaysian-citizen-employees)).
9. **Keep records.** For each employee, keep a monthly record of:
   - name, identity card number and occupation;
   - contributions;
   - wages and allowances.

   Keep them for seven years from the last entry ([PERKESO employer registration](https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
10. **Feed the payroll tax reliefs.** The employee's EPF and SOCSO/EIS contributions reduce the MTD calculation, within the reliefs listed below.

### Rates, bands and thresholds

### SOCSO (Act 4): rates and ceiling ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [PERKESO contribution schedule](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf))

| Item | Employer | Employee | Notes |
| --- | --- | --- | --- |
| First Category (Employment Injury + Invalidity), under 60 | 1.75% | 0.5% | Amounts per the Third Schedule table  [Source](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Second Category (Employment Injury only), 60 and over, or first eligible at 55+ | 1.25% | nil | Paid by the employer  [Source](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Wage ceiling from 1 October 2024 | RM 6,000 | RM 6,000 | Before October 2024: RM 5,000  [Source](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |

### LINDUNG 24 Jam (Non-Employment Injury Scheme), from 1 June 2026 ([PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf); [PERKESO LINDUNG 24 Jam](https://www.perkeso.gov.my/skim-kemalangan-bukan-bencana-kerja-lindung-24-jam.html))

| Phase | Years from 1 June 2026 | Employee rate | Employer rate |
| --- | --- | --- | --- |
| Phase 1 | 1 June 2026 to 31 May 2028 (years 1-2) | 0.75% | nil  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Phase 2 | 1 June 2028 to 31 May 2031 (years 3-5) | 1.00% | nil  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Phase 3 | From 1 June 2031 (year 6 onwards) | 1.25% | nil  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |

The rate applies to monthly wages up to the RM 6,000 ceiling. [P.U. (B) 196/2026](https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/3521924/PUB%20196%20%282026%29.pdf) appoints all 3 phase dates.

The combined split in Phase 1 for a First Category employee who is covered by LINDUNG 24 Jam:
- **Employer:** 1.25% Employment Injury + 0.5% Invalidity = 1.75%.
- **Employee:** 0.5% Invalidity + 0.75% LINDUNG 24 Jam = 1.25%.

([PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf))

### SOCSO table extracts, monthly amounts from June 2026 ([PERKESO table including LINDUNG 24 Jam](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf))

These extracts are for checking only. Use the full table for any other band.

| Monthly wages | First Cat. employer | First Cat. employee (Invalidity) | LINDUNG 24 Jam (employee) | First Cat. total | Second Cat. employer | Second Cat. LINDUNG 24 Jam (employee) | Second Cat. total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Over RM 2,400, not over RM 2,500 | RM 42.85 | RM 12.25 | RM 18.35 | RM 73.45 | RM 30.60 | RM 18.35 | RM 48.95  [Source](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf) |
| Over RM 3,900, not over RM 4,000 | RM 69.15 | RM 19.75 | RM 29.65 | RM 118.55 | RM 49.40 | RM 29.65 | RM 79.05  [Source](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf) |
| Over RM 5,900, and all wages over RM 6,000 | RM 104.15 | RM 29.75 | RM 44.65 | RM 178.55 | RM 74.40 | RM 44.65 | RM 119.05  [Source](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf) |

- **Local employee who opted out of LINDUNG 24 Jam:** leave out the LINDUNG 24 Jam column. The total is then the employer amount plus the Invalidity amount (First Category), or the employer amount alone (Second Category).
- **Maximum monthly SOCSO without LINDUNG 24 Jam:** RM 104.15 employer + RM 29.75 employee = RM 133.90.

### EIS (Act 800) ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [Act A1725, Second Schedule amendment](https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf); [Act 800](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf))

| Item | Employer | Employee | Total |
| --- | --- | --- | --- |
| Rate (on assumed monthly wage) | 0.2% | 0.2% | 0.4% [Source](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Wages over RM 5,900 (top band, ceiling RM 6,000) | RM 11.90 | RM 11.90 | RM 23.80  [Source](https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf) |

Act A1725 raised the EIS ceiling from "five thousand ringgit" to "six thousand ringgit" and added the bands above RM 5,000. Under the Act, EIS contributions stop when the employee reaches the minimum retirement age.

### Self-employed and housewives' SOCSO schemes

[PERKESO's separate schemes](https://perkeso.gov.my/en/our-services/employer-employee/kadar-caruman.html) use their own amounts. Under Act 789, the 4 insured monthly earnings options of RM 1,050, RM 1,550, RM 2,950 and RM 3,950 cost RM 13.10, RM 19.40, RM 36.90 and RM 49.40 a month respectively. Under Act 838, pay RM 120 in advance for 12 consecutive months.

### Payroll tax reliefs that use these contributions, 2026 ([MTD specification 2026](https://www.hasil.gov.my/wp-content/uploads/spesifikasi-kaedah-pengiraan-berkomputer-pcb-2026.pdf); [TP 1 explanatory notes 2026](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf))

| Relief | Limit |
| --- | --- |
| EPF, mandatory and voluntary, or other approved scheme | RM 4,000  [Source](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf) |
| Shared limit for life insurance, family takaful and additional voluntary EPF | RM 3,000  [Source](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf) |
| SOCSO contributions under Act 4 or Act 800 (includes EIS) | RM 350  [Source](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf) |

- **Employee share only:** the employer's EPF share does not count towards the employee's relief. Voluntary EPF used in the RM 4,000 bucket cannot be claimed again in the separate RM 3,000 bucket shared with eligible insurance/takaful.
- **No mandatory EPF:** under the MTD specification, a person with no mandatory EPF contribution (for example, one paid only a director's fee) can claim eligible voluntary EPF of up to RM 7,000 across the 2 buckets, subject to the amount already claimed for insurance or takaful in the RM 3,000 bucket.

### EPF categories and the October 2025 schedule

| Employee category | General employee and employer rates; use the schedule for actual amounts | Official source |
|---|---|---|
| Under 60 citizen, PR or non-citizen member before 1 August 1998; wages up to RM 5,000 | Employee 11%; employer 13%, Part A | [Third Schedule Part A](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| Same category; wages over RM 5,000 | Employee 11%; employer 12%, Part A | [Third Schedule Part A](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| Citizen 60+ | Employee 0%; employer 4%, Part E | [Third Schedule Part E](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| PR or pre-August 1998 non-citizen member 60+; wages up to RM 5,000 | Employee 5.5%; employer 6.5%, Part C | [Third Schedule Part C](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| Same older PR/member category; wages over RM 5,000 | Employee 5.5%; employer 6%, Part C | [Third Schedule Part C](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| Other non-citizen employees, from October 2025 wages | Employee 2%; employer 2%, Part F; domestic-servant and work-pass coverage must follow KWSP's actual scope | [Third Schedule Part F](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025); [KWSP foreign-worker scope](https://www.kwsp.gov.my/en/employer/responsibilities/non-malaysian-citizen-employees) |
| Part A worked wage band RM 3,980.01 to RM 4,000 | Employer RM 520; employee RM 440; total RM 960 | [Third Schedule Part A printed page 10](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |

The statutory schedule decides the wage bands and rounding. When a bonus alone increases wages from RM 5,000 or less to above RM 5,000 for the month, use the schedule’s special employer rate of 13% under Part A or 6.5% under Part C. Its Part F para 2 requires rounding the **total** contribution to the next ringgit; the foreign-worker FAQ's RM 1,751 example instead rounds each share up. This conflict is not resolved by applying the higher employee deduction. Whole-ringgit, exact-percentage cases below avoid that difference; a fractional Part F payroll needs KWSP confirmation of the employee/employer allocation under the statute.

The employer late-payment charge uses the lower of the relevant year's declared conventional/Shariah dividends plus one percentage point, minimum RM 10, rounded up to a ringgit. Dividends on late contributions are a separate amount. KWSP uses the preceding year's dividend rate while the current year's rate is undeclared. See the [KWSP late-payment calculator](https://secure.kwsp.gov.my/KWSP_files/latePayment/LatePaymentCalculatorStep1-en.html) for its calculation rules ([KWSP overdue-contributions section](https://www.kwsp.gov.my/en/employer/responsibilities/mandatory-contribution)).

## Boundary and exception table

| Situation | SOCSO (Act 4) | LINDUNG 24 Jam | EIS (Act 800) | Source |
| --- | --- | --- | --- | --- |
| Local employee under 55, first joins | First Category | Mandatory | Yes, if aged 18 or over and within Act 800 | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Employee first entering PERKESO at 55 or 56 | Second Category | Mandatory | Yes, if within Act 800 | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Employee aged 57 to 59 with no EIS contributions payable before 57 | Second Category if first entering at 55 or older | Mandatory for first-time entrants. Check coverage for existing workers | Exempt | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Employee who has reached 60 | Second Category (employer only) | Yes, unless they opted out (no age limit) | No | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Foreign worker with a valid passport and work pass | First Category if they first join before 55; Second Category if they join at 55+ or have reached 60 | Mandatory | Excluded unless the employee meets a First Schedule paragraph 10 exception | [PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf); [PERKESO employer registration](https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/) |
| Domestic worker | Separate domestic-worker rules | Check status under Act 4 | Covered from 1 June 2021 if otherwise eligible for EIS | [PERKESO domestic-worker rules](https://www.perkeso.gov.my/en/our-services/protection/domestic-workers.html) |
| Public servant, or local authority or statutory body employee | Refer | Refer | Outside EIS under official eligibility FAQ | [Act 800, First Schedule](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf) |
| Employer's spouse, or a casual worker engaged outside the employer's industry | Check employee status under Act 4 | Check coverage under Act 4 | A spouse can qualify. Casual work outside the employer's industry is excluded | [Act 800, First Schedule](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf) |
| Temporary or part-time worker | Must be registered | As for others | As for others | [PERKESO FAQ](https://perkeso.gov.my/hubungi-kami/saluran-hubungan/soalan-lazim.html) |
| Employee with two employers | Confirm each employer's share with PERKESO | Only one employer (chosen by the employee, or set by PERKESO) deducts | Each employer contributes separately under Act 800 s. 19 | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Month with no wages paid | Contributions follow wages payable for the wage period | Cover can continue if opted in with at least one active contribution in the previous three months; FAQ Q 46 | Contributions follow wages payable for the wage period | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Accident outside Malaysia | Work-related: normal rules | Not covered | n/a | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |

**Opt-out mechanics (local employees).**
- **Who acts (existing employees, 2026 window):** the employee, through the LINDUNG Faedah Portal, or with a paper liability release notice if the portal is offline.
- **New first-time local entrants:** register on ASSIST and deduct from the first salary month. They must contribute, and there is no new opt-out after 31 August 2026 (FAQ Q 26 to Q 29).
- **Window:** 13 July to 31 August 2026.
- **Default:** anyone who did not opt out stays covered ("Once In, Always In"). An employee who opted out can later opt in at any time; cover starts at the date/time of election, but the contribution uses the full wages of that month (FAQ Q 6,Q 7,Q 45).
- **June 2026:** mandatory for everyone, and not refundable. Any shortfall in June 2026 deductions must be made up from the employee's wages.
- **Refunds:** the employer claims them through ASSIST for July 2026 onwards; employees cannot claim directly.
- **Opting in mid-month:** the contribution for that month is based on the full month's wages (FAQ Q 45).
- **Grace period:** PERKESO gave employers six (6) months after the scheme started with no penalty or legal action for LINDUNG 24 Jam contribution non-compliance. Other non-compliance is still enforced (FAQ Q 41) ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf)).

## Worked cases

In these cases, "employee total" means the SOCSO and EIS deducted from pay; EPF is left out. All amounts are from the schedules linked above.

### Case 1: citizen aged 35, wages RM 4,000, July 2026, has not opted out ([PERKESO table](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf); [Act 800](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf))

- **Wages:** RM 3,700 salary + RM 300 housing allowance = RM 4,000. The allowance is wages. The band is over RM 3,900, not over RM 4,000.
- **SOCSO First Category:** employer RM 69.15; employee RM 19.75 Invalidity + RM 29.65 LINDUNG 24 Jam = RM 49.40.
- **EIS:** RM 7.90 each from the Second Schedule of Act 800.
- **SOCSO and EIS totals:** employee RM 57.30 and employer RM 77.05. With EPF wages also RM 4,000, Part A adds RM 440 for the employee and RM 520 for the employer, giving RM 497.30 and RM 597.05 respectively.
- **Participation decision:** a recorded, valid historical opt-out removes RM 29.65 from this employee's SOCSO deduction. It does not remove ordinary Invalidity or EIS obligations. A newly proposed opt-out is not available after 31 August.

### Case 2: citizen aged 40, wages RM 8,000, opted out of LINDUNG 24 Jam ([PERKESO contribution schedule](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf); [Act A1725](https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf))

- **Ceiling:** wages are above the RM 6,000 ceiling, so the top band applies.
- **SOCSO:** employer RM 104.15; employee RM 29.75.
- **EIS:** RM 11.90 each.
- **Totals:** employee RM 29.75 + RM 11.90 = RM 41.65; employer RM 104.15 + RM 11.90 = RM 116.05.

### Case 3: foreign worker aged 30, wages RM 2,500, August 2026 ([PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf); [PERKESO table](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf))

- **Category:** First Category, and LINDUNG 24 Jam is mandatory.
- **SOCSO:** employer RM 42.85; worker RM 12.25 + RM 18.35 = RM 30.60.
- **EIS:** none for the assumed work-pass holder who meets none of the First Schedule paragraph 10 exceptions.
- **EPF:** assuming Part F eligibility and EPF wages RM 2,500, employee 2%=RM 50 and employer 2%=RM 50. This exact-ringgit case avoids the fractional rounding conflict. [Part F](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025).

### Case 4: citizen aged 61, wages RM 4,000, has not opted out ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [PERKESO table](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf))

- **SOCSO Second Category:** employer RM 49.40; LINDUNG 24 Jam deducted from the employee RM 29.65; total RM 79.05.
- **EIS:** none, because the employee has reached 60.

### Case 5: new hire aged 56, never paid SOCSO or EIS, wages RM 2,500 ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [Act 800](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf))

- **SOCSO:** first eligible at 55 or over, so Second Category. Employer RM 30.60; LINDUNG 24 Jam RM 18.35 from the employee. The old new-hire opt-out exception is wrong. A first-time entrant is mandatorily covered; deduct from the first salary month ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf), Q 25 to Q 29).
- **EIS:** RM 4.90 each for the eligible employee under 57.
- **SOCSO and EIS totals:** employee RM 18.35 + RM 4.90 = RM 23.25 and employer RM 30.60 + RM 4.90 = RM 35.50.

### Case 6: annual bonus and late payment ([PERKESO employer registration](https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/); [PERKESO FAQ](https://perkeso.gov.my/hubungi-kami/saluran-hubungan/soalan-lazim.html))

- **Bonus:** in December the employee earns RM 3,950 salary plus an annual bonus of RM 5,000. The annual bonus is not SOCSO/EIS wages, so the band stays over RM 3,900, not over RM 4,000.
- **Late payment:** assume a RM 500 contribution for one employee is 14 days late within one month. Interest is 6% a year for each day late: RM 500 x 6% x 14 / 365 = about RM 1.15. That is less than RM 5, so RM 5 is charged.


### Recomputing the participation decision and top-band case

Case 1 compares continuing coverage with a valid historical opt-out. The opt-out reduces employee SOCSO by RM 29.65. Case 2 uses the top band in Act A1725.

```oa-check
name: July4000 SOCSO, EIS and separate EPF
inputs:
  socso_employer: 69.15
  invalidity_employee: 19.75
  lindung_employee: 29.65
  eis_each: 7.90
  epf_employee: 440
  epf_employer: 520
steps:
  - employee_in: invalidity_employee + lindung_employee
  - employee_out: invalidity_employee
  - difference: employee_in - employee_out
  - employee_with_epf: employee_in + eis_each + epf_employee
  - employer_with_epf: socso_employer + eis_each + epf_employer
expected:
  employee_in: 49.40
  employee_out: 19.75
  difference: 29.65
  employee_with_epf: 497.30
  employer_with_epf: 597.05
```

```oa-check
name: Ceiling8000 valid historical opt-out and foreign2500 EPF
inputs:
  socso_employer: 104.15
  socso_employee: 29.75
  eis_each: 11.90
  foreign_epf_wages: 2500
  foreign_epf_rate: 0.02
steps:
  - employee_total: socso_employee + eis_each
  - employer_total: socso_employer + eis_each
  - foreign_epf_each: foreign_epf_wages * foreign_epf_rate
  - foreign_epf_total: foreign_epf_each * 2
expected:
  employee_total: 41.65
  employer_total: 116.05
  foreign_epf_each: 50
  foreign_epf_total: 100
```

### Earlier months: October 2024 to June 2026

- **October 2024 to May 2026:** the RM 6,000 ceiling applied, and there was no LINDUNG 24 Jam column. Use the employer and Invalidity columns only ([PERKESO contribution schedule](https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf)).
- **Before October 2024:** the ceiling was RM 5,000.
- **June 2026:** LINDUNG 24 Jam was mandatory for every employee under the Employees' Social Security (Amendment) Act 2026. June contributions cannot be refunded. If they were not deducted, the employer must deduct the arrears ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf)).
- **Returns being filed now:** the 2025 employer return (Form E) and employees' EA statements are handled under the income tax rules and are outside this skill.

## When to refuse or refer

- **Voluntary self-employed EPF and fractional Part F contributions:** see [KWSP i-Saraan](https://www.kwsp.gov.my/en/member/savings/i-saraan) for the standard 20% incentive, capped at RM 500 annually and RM 5,000 over the member's lifetime or until age 60, whichever comes first. Confirm the fractional Part F allocation with KWSP.
- **HRD Corp levy:** whether an employer must register and pay the levy depends on its industry and headcount under the Pembangunan Sumber Manusia Berhad Act 2001. This skill does not state the rates. Refer to HRD Corp.
- **Foreign workers and EIS:** verify the immigration and identity documents required by First Schedule paragraph 10 before withholding EIS.
- **Domestic workers, public-sector staff and employees with several employers:** apply the boundary table and refer unclear classifications to PERKESO.
- **Prosecution or compound notices, and disputes over arrears:** refer to a lawyer or a PERKESO/KWSP office.

## Filing and payment

- **SOCSO and EIS due date:** "no later than the 15 th day of each succeeding month". For example, July contributions are due by 15 August ([PERKESO contribution payment](https://perkeso.gov.my/en/contribution-payment.html)).
- **Channels:** ASSIST Portal with FPX, direct debit, internet banking, or a bank counter using the ACR reference.
- **Late interest (SOCSO/EIS):** 6% per annum for each day late. The [PERKESO FAQ](https://perkeso.gov.my/hubungi-kami/saluran-hubungan/soalan-lazim.html) states a monthly minimum of RM 5. For EIS, [P.U. (A) 452/2017 reg. 10](https://perkeso.gov.my/images/akta/ACT%20800/P.U%28A%29/P.U.%20%28A%29%20452%20-%20PP%20SIP%20%28Pendaftaran%20dan%20Caruman%29%202017_PERATURAN-PERATURAN%20SISTEM%20INSURANS%20PEKERJAAN%20%28PENDAFTARAN%20DAN%20CARUMAN%29%202017.pdf) applies the minimum to each employee for each month or part of a month and rounds amounts over RM 5 up to the next multiple of RM 5. Pay EIS interest within 14 days of the demand notice.
- **Penalties (Act 4):** failure to register or contribute can lead to prosecution: a fine not exceeding ten thousand ringgit, imprisonment of up to two years, or both. The foreign-worker page states the same maximum, RM 10,000.00 or 2 years ([PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf)).
- **Penalties (Act 800):** up to RM 10,000, 2 years' imprisonment or both for failure to register the industry or register employees as required (ss. 14(2) and 16(5)). The registration regulations apply the same maxima to specified notification failures (regs. 2(3) and 4(4)) ([Act 800, s.14](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf)).
- **Registering employees (Act 800):** register employees already employed when the industry is registered on that date. Register later hires within 30 days from entry into employment ([Act 800, s.16(1)(b)](https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf)).
- **Accidents:** notify PERKESO of a work-related accident within 48 hours after the employer receives notice.
- **Ceasing to be an employer:** submit Form 1 A (Act 4) and Form SIP 3 (Act 800) within 30 days of ceasing ([PERKESO employer registration](https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
- **EPF:** use KWSP's employer channels by the 15 th of the next month. Reconcile the contribution receipt and account allocation; the overdue-charge method is above. [KWSP](https://www.kwsp.gov.my/en/employer/responsibilities/non-malaysian-citizen-employees).

## Completion checklist

- [ ] Every employee is classified: citizen or PR or foreign worker, age, and earlier SOCSO/EIS history.
- [ ] Employer and employees are registered on ASSIST (Borang 1 and 2, SIP 1 and 2 where required; see [PERKESO employer registration](https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/)) and with KWSP.
- [ ] SOCSO/EIS wages exclude the annual bonus, gratuity, mileage claims and statutory fund payments.
- [ ] SOCSO category and band are read from the current table, with top band for wages over RM 6,000.
- [ ] LINDUNG 24 Jam is deducted for foreign workers and for local employees who did not opt out; June 2026 arrears are handled.
- [ ] EIS eligibility is checked for employees aged 18 to under 60, including the contribution history and First Schedule tests.
- [ ] EPF rates are read from the KWSP Third Schedule for each employee's category.
- [ ] Payment is made by the 15 th of the following month and receipts are kept; records are kept for seven years.
- [ ] Employee contributions are passed to the MTD calculation within the RM 4,000 EPF and RM 350 SOCSO relief limits.

## Sources

| Source and scope read | Official URL | Read on |
|---|---|---|
| PERKESO contributions. Read for category ages, first-entry exception, EIS ages and 0.4% split. | https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html | 2026-11-14 |
| PERKESO current LINDUNG page. Read for voluntary-local versus mandatory-foreign scope and non-employment exclusions. | https://www.perkeso.gov.my/skim-kemalangan-bukan-bencana-kerja-lindung-24-jam.html | 2026-11-14 |
| LINDUNG FAQ v2.3. Read for Q 1 to 48 and 50 to 56 for current opt-out closure, first entrants, phased rates, wages, multi-employer, refunds, grace, penalties and no-wage continuity. | https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf | 2026-11-14 |
| Act A1788 s. 16 and Third Schedule Parts I and IV, bands 29, 44, 64 and 65. | https://www.perkeso.gov.my/images/akta/ACT%204/Act_A1788_-_EMPLOYEES_SOCIAL_SECURITY_AMENDMENT_ACT_2026.pdf | 2026-11-14 |
| Act A1725. Read for s.2 and Second Schedule amendments for RM 6,000 ceiling and RM 11.90 top-band EIS shares. | https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf | 2026-11-14 |
| PERKESO employer registration. Read for registration forms and foreign exception, wage inclusions/exclusions, seven-year records, accident and cessation duties. | https://www.perkeso.gov.my/en/our-services/employer-employee/employer-registration/ | 2026-11-14 |
| PERKESO payment. Read for 15 th deadline,6% daily late interest and available payment channels. | https://perkeso.gov.my/en/contribution-payment.html | 2026-11-14 |
| PERKESO Malay FAQ. Read for the RM 5 monthly interest minimum. | https://perkeso.gov.my/hubungi-kami/saluran-hubungan/soalan-lazim.html | 2026-11-14 |
| P.U.(A)452/2017. Read for English regs.2 to 9 for employer 30-day application, employee-register cross-reference, cessation, seven-year records and 15 th deadline. | https://perkeso.gov.my/images/akta/ACT%20800/P.U%28A%29/P.U.%20%28A%29%20452%20-%20PP%20SIP%20%28Pendaftaran%20dan%20Caruman%29%202017_PERATURAN-PERATURAN%20SISTEM%20INSURANS%20PEKERJAAN%20%28PENDAFTARAN%20DAN%20CARUMAN%29%202017.pdf | 2026-11-14 |
| KWSP Third Schedule effective October 2025. Read for Part A coverage and RM 4,000 band, Part C/E category conditions and Part F including para 2 total rounding. | https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025 | 2026-11-14 |
| KWSP mandatory contributions. Read for current category table, band-versus-percentage examples and overdue charge/dividend method. | https://www.kwsp.gov.my/en/employer/responsibilities/mandatory-contribution | 2026-11-14 |
| KWSP non-citizen employees. Read for October 2025 commencement, category exceptions, coverage and 15 th deadline; fractional example conflicts with statutory total rounding. | https://www.kwsp.gov.my/en/employer/responsibilities/non-malaysian-citizen-employees | 2026-11-14 |
| LHDN 2026 MTD specification. Read for EPF bucket insectiond andSOCSO optional deductionk and contributions examples. | https://www.hasil.gov.my/wp-content/uploads/spesifikasi-kaedah-pengiraan-berkomputer-pcb-2026.pdf | 2026-11-14 |
| LHDN 2026 TP 1 notes. Read for C 11 and C 14 for shared RM 3,000/RM 4,000 buckets and RM 350 Act 4/800 relief. | https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf | 2026-11-14 |
| Act 800 ss. 14, 16, 19 and First and Second Schedules. | https://www.perkeso.gov.my/images/akta/ACT%20800/Akta%20800_EMPLOYMENT%20INSURANCE%20SYSTEM%20ACT%202017.pdf | 2026-11-22 |
| Act A1796 ss. 3 and 6, title and contribution recovery. | https://lom.agc.gov.my/ilims/upload/portal/akta/outputaktap/3696918_BI/Act%20A1796%20-%20EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202026.pdf | 2026-11-22 |
| P.U. (B) 196/2026, LINDUNG 24 Jam commencement and phase dates. | https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/3521924/PUB%20196%20%282026%29.pdf | 2026-11-22 |
| PERKESO domestic-worker eligibility and commencement. | https://www.perkeso.gov.my/en/our-services/protection/domestic-workers.html | 2026-11-22 |
| KWSP employer registration and 7-day deadline. | https://www.kwsp.gov.my/en/employer/responsibilities/registration | 2026-11-22 |
| PERKESO self-employment and housewife contribution tables. | https://perkeso.gov.my/en/our-services/employer-employee/kadar-caruman.html | 2026-11-22 |
| KWSP i-Saraan eligibility and incentives. | https://www.kwsp.gov.my/en/member/savings/i-saraan | 2026-11-22 |

Not yet confirmed: the EPF contribution month at the age-75 boundary and the allocation of fractional Part F contributions. Confirm these with KWSP. An arrears assessment requires the actual dates, declared dividend rates and KWSP's notice.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `my-epf-socso` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/my-epf-socso. If neither is available, confirm every figure against the official source pages cited above before relying on it.
