---
name: my-epf-socso
description: Use this skill whenever asked about Malaysia EPF (KWSP), SOCSO (PERKESO), or EIS contributions. Trigger on phrases like "EPF Malaysia", "KWSP", "Kumpulan Wang Simpanan Pekerja", "SOCSO", "PERKESO", "EIS", "Employment Insurance System", "employer contribution Malaysia", "employee contribution Malaysia", "i-Saraan", "self-employed EPF", "social security Malaysia", or any question about mandatory employment contributions in Malaysia. Covers EPF rates, SOCSO rates, EIS rates, self-employed options, and registration. ALWAYS read this skill before advising on Malaysian employment contributions.
version: 1.1
jurisdiction: MY
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - my-income-tax
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v 1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Malaysia employer contributions: EPF (KWSP), SOCSO (PERKESO) including LINDUNG 24 Jam, EIS, and registration (2026, with notes on earlier months)

Figures are for 2026 contribution months (calendar year 2026) unless a line says otherwise. SOCSO and EIS amounts come from PERKESO's schedules. The ceiling for both is RM 6,000 a month, from 1 October 2024 ([PERKESO contribution schedule](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf)). From 1 June 2026 there is a new employee-funded SOCSO scheme, LINDUNG 24 Jam. Since 8 July 2026 it is voluntary for local employees and mandatory for foreign workers ([PERKESO LINDUNG 24 Jam](https://www.perkeso.gov.my/en/?Itemid=2019&id=990&option=com_content&view=article)).

**Read the wage band before calculating.** EPF rates are now verified from KWSP's current [Third Schedule](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025); SOCSO and EIS use their own schedules. Do not use the SOCSO wage exclusions for EPF or assume that a percentage gives the scheduled ringgit amount. Check the employee's actual LINDUNG participation, not just the word “voluntary”. First-time PERKESO entrants must contribute; existing local workers cannot newly opt out after 31 August 2026 ([FAQ v 2.3 Q 25 to Q 29](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf)).

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
4. **LINDUNG 24 Jam status.** Did any existing local employee opt out through the LINDUNG Faedah Portal during the window of 13 July to 31 August 2026? Has a previously opted-out employee rejoined? A first-time PERKESO entrant must contribute, and no new opt-out is permitted after 31 August 2026. Obtain the ASSIST status and PERKESO notification, including any selected employer. Does anyone have more than one employer?
5. **Is the business registered with PERKESO (ASSIST Portal) and with KWSP?** Since when? Are there unpaid or late months?
6. **Headcount and industry,** to decide whether HRD Corp levy rules may apply (refer out).

## The method, step by step

1. **Register the employer.** Register with PERKESO on the ASSIST Portal. Upload:
   - Borang 1 (employer) and Borang 2 (employee) for Act 4;
   - Borang SIP 1 and SIP 2 for EIS ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).

   For foreign workers, use the foreign-worker registration form instead of Borang 2. SIP 1 and SIP 2 are not required for them ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)). Act 800 requires an employer to register "within such period and in such manner as prescribed" ([Act 800, s.14](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf)). Register the business when you hire the first employee. The EIS employer application is due within 30 days from the Act applying to the industry (P.U.(A)452/2017 reg.2). Register the employees through SIP 2; the regulation refers to Act 800 s.16(1) for the employee deadline. That section was not reopened and its exact later-hire timing remains unconfirmed below. Register with KWSP as well. [EIS registration regulations regs.2 to 4](https://perkeso.gov.my/images/akta/ACT%20800/P.U%28A%29/P.U.%20%28A%29%20452%20-%20PP%20SIP%20%28Pendaftaran%20dan%20Caruman%29%202017_PERATURAN-PERATURAN%20SISTEM%20INSURANS%20PEKERJAAN%20%28PENDAFTARAN%20DAN%20CARUMAN%29%202017.pdf).
2. **Classify each employee for SOCSO (Act 4).**
   - **First Category:** Employment Injury + Invalidity. It covers employees under 60.
   - **Second Category:** Employment Injury only, paid by the employer. It covers employees who have reached 60, and anyone who first becomes eligible at age 55 or over with no earlier contributions ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html)).
3. **Decide LINDUNG 24 Jam (Non-Employment Injury Scheme) for each employee.**
   - **Foreign workers:** mandatory.
   - **Local employees:** the voluntary change on 8 July 2026 had a closed opt-out window. Existing locals who did not opt out by 31 August remain in; first-time entrants are mandatory and the employer registers them on ASSIST and deducts from the first salary month ([PERKESO LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf), Q 25 to Q 29).
   - The contribution is the employee's alone, but the employer deducts it and pays it to PERKESO. There is no age limit.
4. **Classify each employee for EIS (Act 800).** Employees aged 18 to 60 contribute. Anyone aged 57 or over with no EIS contributions before 57 is exempt. Government employees, domestic workers and self-employed persons are excluded in PERKESO's contributions guidance. PERKESO's general FAQ, EIS question1, limits eligibility to citizens and permanent residents and excludes local-authority and statutory-body workers too. Resolve the employer's spouse and casual-worker exceptions against the First Schedule, which was not reopened. [EIS eligibility FAQ](https://www.perkeso.gov.my/en/contact-us/pejabat-perkeso-new/frequently-asked-question).
5. **Work out wages for SOCSO/EIS.** Include:
   - salary, overtime, commission, service charge and leave pay;
   - allowances (shift, meal, cost of living, housing, etc.).

   Exclude:
   - employer payments to statutory funds;
   - mileage claims;
   - gratuity or termination payments;
   - the annual bonus ([PERKESO employer registration, "Definition Of Wages"](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
6. **Read the amount from the schedule, not a percentage.** SOCSO and EIS are fixed ringgit amounts per scheduled wage band; the lowest bands are narrower than RM 100. The percentages describe the design, and the table decides the amount. Wages above RM 6,000 use the top band.
7. **Apply EPF separately.** Classify the employee under Third Schedule Part A (under 60 citizen/PR/pre-August 1998 member), Part C (older PR/pre-August 1998 member), Part E (citizen 60+) or Part F (other non-citizens), with the actual wage period and membership history. Read that part's ringgit wage band, not a payroll-wide flat percentage. Part F has applied from October 2025 wages. Contributions are not capped at the SOCSO/EIS ceiling. Do not assume EPF excludes an annual bonus merely because SOCSO does. [Third Schedule](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025); [KWSP mandatory contributions](https://www.kwsp.gov.my/en/employer/responsibilities/mandatory-contribution).

8. **Pay by the 15 th of the following month.** Pay SOCSO and EIS through ASSIST (FPX, direct debit, internet banking or a bank counter) ([PERKESO contribution payment](https://www.perkeso.gov.my/en/contribution-payment.html)). Pay EPF through KWSP's employer channel by the 15 th of the following month ([KWSP non-citizen contribution guidance](https://www.kwsp.gov.my/en/employer/responsibilities/non-malaysian-citizen-employees)).
9. **Keep records.** For each employee, keep a monthly record of:
   - name, identity card number and occupation;
   - contributions;
   - wages and allowances.

   Keep them for seven years from the last entry ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
10. **Feed the payroll tax reliefs.** The employee's EPF and SOCSO/EIS contributions reduce the MTD calculation, within the reliefs listed below.

### Rates, bands and thresholds

### SOCSO (Act 4): rates and ceiling ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [PERKESO contribution schedule](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf))

| Item | Employer | Employee | Notes |
| --- | --- | --- | --- |
| First Category (Employment Injury + Invalidity), under 60 | 1.75% | 0.5% | Amounts per the Third Schedule table  [Source](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Second Category (Employment Injury only), 60 and over, or first eligible at 55+ | 1.25% | nil | Paid by the employer  [Source](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Wage ceiling from 1 October 2024 | RM 6,000 | RM 6,000 | Before October 2024: RM 5,000  [Source](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |

### LINDUNG 24 Jam (Non-Employment Injury Scheme), from 1 June 2026 ([PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf); [PERKESO LINDUNG 24 Jam](https://www.perkeso.gov.my/en/?Itemid=2019&id=990&option=com_content&view=article))

| Phase | Years from 1 June 2026 | Employee rate | Employer rate |
| --- | --- | --- | --- |
| Phase 1 | 1 June 2026 to 31 May 2028 (years 1-2) | 0.75% | nil  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Phase 2 | 1 June 2028 to 31 May 2031 (years 3-5) | 1.00% | nil  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Phase 3 | From 1 June 2031 (year 6 onwards) | 1.25% | nil  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |

The rate applies to monthly wages up to the RM 6,000 ceiling. PERKESO says the phased increases are subject to confirmation of their effective dates ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf), Q 35).

The combined split in Phase 1 for a First Category employee who is covered by LINDUNG 24 Jam:
- **Employer:** 1.25% Employment Injury + 0.5% Invalidity = 1.75%.
- **Employee:** 0.5% Invalidity + 0.75% LINDUNG 24 Jam = 1.25%.

([PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf))

### SOCSO table extracts, monthly amounts from June 2026 ([PERKESO table including LINDUNG 24 Jam](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf))

These extracts are for checking only. Use the full table for any other band.

| Monthly wages | First Cat. employer | First Cat. employee (Invalidity) | LINDUNG 24 Jam (employee) | First Cat. total | Second Cat. employer | Second Cat. LINDUNG 24 Jam (employee) | Second Cat. total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Over RM 2,400, not over RM 2,500 | RM 42.85 | RM 12.25 | RM 18.35 | RM 73.45 | RM 30.60 | RM 18.35 | RM 48.95  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf) |
| Over RM 3,900, not over RM 4,000 | RM 69.15 | RM 19.75 | RM 29.65 | RM 118.55 | RM 49.40 | RM 29.65 | RM 79.05  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf) |
| Over RM 5,900, and all wages over RM 6,000 | RM 104.15 | RM 29.75 | RM 44.65 | RM 178.55 | RM 74.40 | RM 44.65 | RM 119.05  [Source](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf) |

- **Local employee who opted out of LINDUNG 24 Jam:** leave out the LINDUNG 24 Jam column. The total is then the employer amount plus the Invalidity amount (First Category), or the employer amount alone (Second Category).
- **Maximum monthly SOCSO without LINDUNG 24 Jam:** RM 104.15 employer + RM 29.75 employee = RM 133.90.

### EIS (Act 800) ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [Act A 1725, Second Schedule amendment](https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf); [Act 800](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf))

| Item | Employer | Employee | Total |
| --- | --- | --- | --- |
| Rate (on assumed monthly wage) | 0.2% | 0.2% | 0.4% [Source](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Wages over RM 5,900 (top band, ceiling RM 6,000) | RM 11.90 | RM 11.90 | RM 23.80  [Source](https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf) |

Act A 1725 raised the EIS ceiling from "five thousand ringgit" to "six thousand ringgit" and added the bands above RM 5,000. Under the Act, EIS contributions stop when the employee reaches the minimum retirement age.

### Self-employed and housewives' SOCSO schemes

These are separate from employee Act 4/EIS contributions. Their former plan amounts are retained as specific confirmation gaps under Sources because the linked rate page did not expose those tables on this read. Do not apply an employee contribution band to self-employment or housewife cover.

### Payroll tax reliefs that use these contributions, 2026 ([MTD specification 2026](https://www.hasil.gov.my/wp-content/uploads/spesifikasi-kaedah-pengiraan-berkomputer-pcb-2026.pdf); [TP 1 explanatory notes 2026](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf))

| Relief | Limit |
| --- | --- |
| EPF, mandatory and voluntary, or other approved scheme | RM 4,000  [Source](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf) |
| Life insurance or family takaful (a separate limit) | RM 3,000  [Source](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf) |
| SOCSO contributions under Act 4 or Act 800 (includes EIS) | RM 350  [Source](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf) |

- **Employee share only:** the employer's EPF share does not count towards the employee's relief. Voluntary EPF used in the RM 4,000 bucket cannot be claimed again in the separate RM 3,000 bucket shared with eligible insurance/takaful.
- **No mandatory EPF:** under the MTD specification, a person with no mandatory EPF contribution (for example, one paid only a director's fee) can claim voluntary EPF of up to RM 7,000.

### EPF categories and the October 2025 schedule

| Employee category | General employee and employer rates; use the schedule for actual amounts | Official source |
|---|---|---|
| Under 60 citizen, PR or non-citizen member before 1 August 1998; wages up to RM 5,000 | Employee 11%; employer 13%, Part A | [Third Schedule Part A](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| Same category; wages over RM 5,000 | Employee 11%; employer 12%, Part A | [Third Schedule Part A](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| Citizen 60+ | Employee 0%; employer 4%, Part E | [Third Schedule Part E](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| PR or pre-August 1998 non-citizen member 60+; wages up to RM 5,000 | Employee 5.5%; employer 6.5%, Part C | [Third Schedule Part C](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| Same older PR/member category; wages over RM 5,000 | Employee 5.5%; employer 6%, Part C | [Third Schedule Part C](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |
| Other non-citizen employees, fromOctober 2025 wages | Employee 2%; employer 2%, Part F; domestic-servant and work-pass coverage must follow KWSP's actual scope | [Third Schedule Part F](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025); [KWSP foreign-worker scope](https://www.kwsp.gov.my/en/employer/responsibilities/non-malaysian-citizen-employees) |
| Part A worked wage band RM 3,980.01 to RM 4,000 | Employer RM 520; employee RM 440; total RM 960 | [Third Schedule Part A printedp 10](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025) |

The statutory schedule decides the wage bands and rounding. Its Part F para 2 requires rounding the **total** contribution to the next ringgit; the foreign-worker FAQ's RM 1,751 example instead rounds each share up. This conflict is not resolved by applying the higher employee deduction. Whole-ringgit, exact-percentage cases below avoid that difference; a fractional Part F payroll needs KWSP confirmation of the employee/employer allocation under the statute.

The employer late-payment charge uses the lower of the relevant year's declared conventional/Shariah dividends plus one percentage point, minimum RM 10, rounded up to a ringgit. Dividends on late contributions are a separate amount. The actual declared dividend and applicable period must be obtained, rather than using an invented fixed annual rate ([KWSP overdue-contributions section](https://www.kwsp.gov.my/en/employer/responsibilities/mandatory-contribution)).

## Boundary and exception table

| Situation | SOCSO (Act 4) | LINDUNG 24 Jam | EIS (Act 800) | Source |
| --- | --- | --- | --- | --- |
| Local employee under 55, first joins | First Category | Yes, unless they opted out | Yes, if aged 18 or over | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| New employee aged 55 to 56, no earlier SOCSO contributions | Second Category | Yes, unless they opted out | Yes (under 57) | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| New employee aged 57 to 59, no earlier EIS contributions | Second Category if no earlier SOCSO | Yes, unless they opted out | Exempt | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html) |
| Employee who has reached 60 | Second Category (employer only) | Yes, unless they opted out (no age limit) | No | [PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Foreign worker with a valid passport and work pass | First Category if they first join before 55; Second Category if they join at 55+ or have reached 60 | Mandatory | Not covered; EIS eligibility is limited to Malaysian citizens and permanent residents | [PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf); [PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/) |
| Domestic worker | Separate domestic-worker rules | Refer to PERKESO | Outside EIS under official eligibility FAQ | [Act 800, First Schedule](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf) |
| Public servant, or local authority or statutory body employee | Refer | Refer | Outside EIS under official eligibility FAQ | [Act 800, First Schedule](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf) |
| Employer's spouse, or a casual worker not employed for the business | Refer | Refer | Confirm First Schedule exclusion before finalising | [Act 800, First Schedule](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf) |
| Temporary or part-time worker | Must be registered | As for others | As for others | [PERKESO FAQ](https://www.perkeso.gov.my/en/contact-us/pejabat-perkeso-new/frequently-asked-question) |
| Employee with two employers | Confirm each employer's share with PERKESO | Only one employer (chosen by the employee, or set by PERKESO) deducts | Confirm with PERKESO (Act 800 s.19) | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Month with no wages paid | Contributions follow wages paid | Cover can continue if opted in with at least one active contribution in the previous three months; FAQ Q 46 | Contributions follow wages paid | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |
| Accident outside Malaysia | Work-related: normal rules | Not covered | n/a | [LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf) |

**Opt-out mechanics (local employees).**
- **Who acts (existing employees, 2026 window):** the employee, through the LINDUNG Faedah Portal, or with a paper liability release notice if the portal is offline.
- **New first-time local entrants:** register on ASSIST and deduct from the first salary month. They must contribute, and there is no new opt-out after 31 August 2026 (FAQ Q 26 toQ 29).
- **Window:** 13 July to 31 August 2026.
- **Default:** anyone who did not opt out stays covered ("Once In, Always In"). An employee who opted out can later opt in at any time; cover starts at the date/time of election, but the contribution uses the full wages of that month (FAQ Q 6,Q 7,Q 45).
- **June 2026:** mandatory for everyone, and not refundable. Any shortfall in June 2026 deductions must be made up from the employee's wages.
- **Refunds:** the employer claims them through ASSIST for July 2026 onwards; employees cannot claim directly.
- **Opting in mid-month:** the contribution for that month is based on the full month's wages (FAQ Q 45).
- **Grace period:** PERKESO gave employers six (6) months after the scheme started with no penalty or legal action for LINDUNG 24 Jam contribution non-compliance. Other non-compliance is still enforced (FAQ Q 41) ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf)).

## Worked cases

In these cases, "employee total" means the SOCSO and EIS deducted from pay; EPF is left out. All amounts are from the schedules linked above.

### Case 1: citizen aged 35, wages RM 4,000, July 2026, has not opted out ([PERKESO table](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf); [Act 800](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf))

- **Wages:** RM 3,700 salary + RM 300 housing allowance = RM 4,000. The allowance is wages. The band is over RM 3,900, not over RM 4,000.
- **SOCSO First Category:** employer RM 69.15; employee RM 19.75 Invalidity + RM 29.65 LINDUNG 24 Jam = RM 49.40.
- **EIS:** required for the assumed eligible citizen, but the specific lower-band schedule was not reopened; do not finalise its amount from this case.
- **SOCSO totals before EIS and EPF:** employee RM 49.40; employer RM 69.15. With EPF wages also RM 4,000, the separate Part A amounts are employee RM 440 and employer RM 520. Final EIS remains a gap below.
- **Participation decision:** a recorded, valid historical opt-out removes RM 29.65 from this employee's SOCSO deduction. It does not remove ordinary Invalidity or EIS obligations. A newly proposed opt-out is not available after 31 August.

### Case 2: citizen aged 40, wages RM 8,000, opted out of LINDUNG 24 Jam ([PERKESO contribution schedule](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf); [Act A 1725](https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf))

- **Ceiling:** wages are above the RM 6,000 ceiling, so the top band applies.
- **SOCSO:** employer RM 104.15; employee RM 29.75.
- **EIS:** RM 11.90 each.
- **Totals:** employee RM 29.75 + RM 11.90 = RM 41.65; employer RM 104.15 + RM 11.90 = RM 116.05.

### Case 3: foreign worker aged 30, wages RM 2,500, August 2026 ([PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf); [PERKESO table](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf))

- **Category:** First Category, and LINDUNG 24 Jam is mandatory.
- **SOCSO:** employer RM 42.85; worker RM 12.25 + RM 18.35 = RM 30.60.
- **EIS:** none for the assumed non-citizen, non-PR worker; PERKESO's EIS FAQ restricts eligibility to citizens and PRs.
- **EPF:** assuming Part F eligibility and EPF wages RM 2,500, employee 2%=RM 50 and employer 2%=RM 50. This exact-ringgit case avoids the fractional rounding conflict. [Part F](https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025).

### Case 4: citizen aged 61, wages RM 4,000, has not opted out ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [PERKESO table](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf))

- **SOCSO Second Category:** employer RM 49.40; LINDUNG 24 Jam deducted from the employee RM 29.65; total RM 79.05.
- **EIS:** none, because the employee has reached 60.

### Case 5: new hire aged 56, never paid SOCSO or EIS, wages RM 2,500 ([PERKESO contributions](https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html); [Act 800](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf))

- **SOCSO:** first eligible at 55 or over, so Second Category. Employer RM 30.60; LINDUNG 24 Jam RM 18.35 from the employee. The old new-hire opt-out exception is wrong. A first-time entrant is mandatorily covered; deduct from the first salary month ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf), Q 25 to Q 29).
- **EIS:** the assumed eligible citizen is under 57, so EIS applies. Its specific lower-band amount was not reopened and remains unconfirmed below.
- **SOCSO amounts before EIS and EPF:** employee RM 18.35; employer RM 30.60. Do not call this the complete payroll deduction.

### Case 6: annual bonus and late payment ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/); [PERKESO FAQ](https://www.perkeso.gov.my/en/contact-us/pejabat-perkeso-new/frequently-asked-question))

- **Bonus:** in December the employee earns RM 3,950 salary plus an annual bonus of RM 5,000. The annual bonus is not SOCSO/EIS wages, so the band stays over RM 3,900, not over RM 4,000.
- **Late payment:** the employer pays July 2026 contributions of RM 500 fourteen days after 15 August 2026. Interest is 6% a year for each day late: RM 500 x 6% x 14 / 365 = about RM 1.15. That is less than RM 5, so RM 5 is charged.


### Recomputing the participation decision and top-band case

Case 1 assumes a valid historical opt-out is available as an alternative fact, not as a new election in November. The employee's SOCSO difference is RM 29.65. Case 2 uses the statutory EIS top band that was reopened in Act A 1725; it gives RM 41.65 deducted and RM 116.05 employer cost before EPF.

```oa-check
name: July4000 SOCSO participation decision and separate EPF
inputs:
  socso_employer: 69.15
  invalidity_employee: 19.75
  lindung_employee: 29.65
  epf_employee: 440
  epf_employer: 520
steps:
  - employee_in: invalidity_employee + lindung_employee
  - employee_out: invalidity_employee
  - difference: employee_in - employee_out
  - employee_before_eis: employee_in + epf_employee
  - employer_before_eis: socso_employer + epf_employer
expected:
  employee_in: 49.40
  employee_out: 19.75
  difference: 29.65
  employee_before_eis: 489.40
  employer_before_eis: 589.15
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

- **October 2024 to May 2026:** the RM 6,000 ceiling applied, and there was no LINDUNG 24 Jam column. Use the employer and Invalidity columns only ([PERKESO contribution schedule](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf)).
- **Before October 2024:** the ceiling was RM 5,000.
- **June 2026:** LINDUNG 24 Jam was mandatory for every employee under the Employees' Social Security (Amendment) Act 2026. June contributions cannot be refunded. If they were not deducted, the employer must deduct the arrears ([LINDUNG 24 Jam FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf)).
- **Returns being filed now:** the 2025 employer return (Form E) and employees' EA statements are handled under the income tax rules and are outside this skill.

## When to refuse or refer

- **EPF registration timing, i-Saraan and disputed fractional Part F allocation:** refer to KWSP or a Malaysian payroll professional. The sourced contribution categories and whole-ringgit examples are usable; do not quote an unconfirmed registration deadline or resolve the rounding conflict by guessing.
- **HRD Corp levy:** whether an employer must register and pay the levy depends on its industry and headcount under the Pembangunan Sumber Manusia Berhad Act 2001. This skill does not state the rates. Refer to HRD Corp.
- **Foreign workers and EIS:** citizens and PRs are the eligible population. Resolve an unclear citizenship/PR record before classifying the employee; do not withhold EIS merely because Act4 applies.
- **Domestic workers, public-sector staff, and employees with several employers:** refer to PERKESO.
- **Prosecution or compound notices, and disputes over arrears:** refer to a lawyer or a PERKESO/KWSP office.

## Filing and payment

- **SOCSO and EIS due date:** "no later than the 15 th day of each succeeding month". For example, July contributions are due by 15 August ([PERKESO contribution payment](https://www.perkeso.gov.my/en/contribution-payment.html)).
- **Channels:** ASSIST Portal with FPX, direct debit, internet banking, or a bank counter using the ACR reference.
- **Late interest (SOCSO/EIS):** 6% per annum for each day late, with a minimum of RM 5 a month ([PERKESO FAQ](https://www.perkeso.gov.my/en/contact-us/pejabat-perkeso-new/frequently-asked-question)).
- **Penalties (Act 4):** failure to register or contribute can lead to prosecution: a fine not exceeding ten thousand ringgit, imprisonment of up to two years, or both. The foreign-worker page states the same maximum, RM 10,000.00 or 2 years ([PERKESO LINDUNG FAQ](https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf)).
- **Penalties (Act 800):** the exact s.14 offence was not reopened. The registration regulations separately prescribe up to RM 10,000 or two years or both for specified notification failures (regs.2(3),4(4)) ([Act 800, s.14](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf)).
- **Registering employees (Act 800):** register employees through SIP 2 and resolve the exact later-hire period against s.16(1)(b), which was not reopened ([Act 800, s.16(1)(b)](https://www.perkeso.gov.my/images/imej/akta_dan_peraturan/EMPLOYMENT_INSURANCE_SYSTEM_ACT_2017_Act_800.pdf)).
- **Accidents:** report work-related accidents within 48 hours of notification.
- **Ceasing to be an employer:** submit Form 1 A (Act 4) and Form SIP 3 (Act 800) within 30 days of ceasing ([PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)).
- **EPF:** use KWSP's employer channels by the 15 th of the next month. Reconcile the contribution receipt and account allocation; the overdue-charge method is above. [KWSP](https://www.kwsp.gov.my/en/employer/responsibilities/non-malaysian-citizen-employees).

## Completion checklist

- [ ] Every employee is classified: citizen or PR or foreign worker, age, and earlier SOCSO/EIS history.
- [ ] Employer and employees are registered on ASSIST (Borang 1 and 2, SIP 1 and 2 where required; see [PERKESO employer registration](https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/)) and with KWSP.
- [ ] SOCSO/EIS wages exclude the annual bonus, gratuity, mileage claims and statutory fund payments.
- [ ] SOCSO category and band are read from the current table, with top band for wages over RM 6,000.
- [ ] LINDUNG 24 Jam is deducted for foreign workers and for local employees who did not opt out; June 2026 arrears are handled.
- [ ] EIS is applied only to employees aged 18 to 60 who are not exempt.
- [ ] EPF rates are read from the KWSP Third Schedule for each employee's category.
- [ ] Payment is made by the 15 th of the following month and receipts are kept; records are kept for seven years.
- [ ] Employee contributions are passed to the MTD calculation within the RM 4,000 EPF and RM 350 SOCSO relief limits.

## Sources

| Source and scope read | Official URL | Read on |
|---|---|---|
| PERKESO contributions. Read for category ages, first-entry exception, EIS ages and 0.4% split. | https://www.perkeso.gov.my/en/our-services/employer-employee/contributions.html | 2026-11-14 |
| PERKESO current LINDUNG page. Read for voluntary-local versus mandatory-foreign scope and non-employment exclusions. | https://www.perkeso.gov.my/en/?Itemid=2019&id=990&option=com_content&view=article | 2026-11-14 |
| LINDUNG FAQv 2.3. Read for Q 1 to 48 and 50 to 56 for current opt-out closure, first entrants, phased rates, wages, multi-employer, refunds, grace, penalties and no-wage continuity. | https://www.perkeso.gov.my/images/lindung/lindung-24-jam/FAQ_LINDUNG24Jam_v_2.3%20.pdf | 2026-11-14 |
| PERKESO Act 4 new schedule. Read for bands over 2400 to 2500, over 3900 to 4000 and over 5900/upwards, including both categories. | https://www.perkeso.gov.my/images/lindung/lindung-24-jam/NewContributionRateIncludingSKBBK.pdf | 2026-11-14 |
| Act A 1725. Read for s.2 and Second Schedule amendments for RM 6,000 ceiling and RM 11.90 top-band EIS shares. | https://www.perkeso.gov.my/images/akta/ACT%20800/ACT%20A1725%20%28BI%29_EMPLOYMENT%20INSURANCE%20SYSTEM%20%28AMENDMENT%29%20ACT%202024.pdf | 2026-11-14 |
| PERKESO employer registration. Read for registration forms and foreign exception, wage inclusions/exclusions, seven-year records, accident and cessation duties. | https://perkeso.gov.my/en/our-services/employer-employee/employer-registration/ | 2026-11-14 |
| PERKESO payment. Read for 15 th deadline,6% daily late interest and available payment channels. | https://www.perkeso.gov.my/en/contribution-payment.html | 2026-11-14 |
| PERKESO general FAQ. Read for employment questions 9 to 21 for ASSIST stages, receipt, actual-month wages and RM 5 monthly interest minimum. | https://www.perkeso.gov.my/en/contact-us/pejabat-perkeso-new/frequently-asked-question | 2026-11-14 |
| P.U.(A)452/2017. Read for English regs.2 to 9 for employer 30-day application, employee-register cross-reference, cessation, seven-year records and 15 th deadline. | https://perkeso.gov.my/images/akta/ACT%20800/P.U%28A%29/P.U.%20%28A%29%20452%20-%20PP%20SIP%20%28Pendaftaran%20dan%20Caruman%29%202017_PERATURAN-PERATURAN%20SISTEM%20INSURANS%20PEKERJAAN%20%28PENDAFTARAN%20DAN%20CARUMAN%29%202017.pdf | 2026-11-14 |
| KWSP Third Schedule effectiveOctober 2025. Read for Part A coverage and RM 4,000 band, Part C/E category conditions andPart F including para 2 total rounding. | https://www.kwsp.gov.my/documents/d/guest/third_schedule_from_-1-october-2025 | 2026-11-14 |
| KWSP mandatory contributions. Read for current category table, band-versus-percentage examples and overdue charge/dividend method. | https://www.kwsp.gov.my/en/employer/responsibilities/mandatory-contribution | 2026-11-14 |
| KWSP non-citizen employees. Read for October 2025 commencement, category exceptions, coverage and 15 th deadline; fractional example conflicts with statutory total rounding. | https://www.kwsp.gov.my/en/employer/responsibilities/non-malaysian-citizen-employees | 2026-11-14 |
| LHDN 2026 MTD specification. Read for EPF bucket insectiond andSOCSO optional deductionk and contributions examples. | https://www.hasil.gov.my/wp-content/uploads/spesifikasi-kaedah-pengiraan-berkomputer-pcb-2026.pdf | 2026-11-14 |
| LHDN 2026 TP 1 notes. Read for C 11 andC 14 for shared RM 3,000/RM 4,000 buckets and RM 350 Act 4/800 relief. | https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf | 2026-11-14 |

Not yet confirmed: the full current Act 800 First Schedule and s.16(1)(b), including spouse/casual-worker scope and later-hire registration timing; EIS lower-band shares formerly RM 4.90 at RM 2,500 and RM 7.90 at RM 4,000, and their complete totals in old cases 1 and 5, because the full base Act and standalone schedule did not reopen; self-employed plans formerly RM 13.10/RM 19.40/RM 36.90/RM 49.40 on RM 1,050/RM 1,550/RM 2,950/RM 3,950 and housewife RM 120 for 12 months because the linked rate page did not expose those tables; EPF fractional Part F employee/employer allocation where the Third Schedule rounds the total but KWSP FAQ rounds each share; EPF employer registration deadline, i-Saraan details andthe applicable declared dividend/period for an individual arrears assessment. These gaps do not prevent the sourced Act 4 andEIS top-band or whole-ringgit EPF computations above.
