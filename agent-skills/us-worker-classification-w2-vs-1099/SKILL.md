---
name: us-worker-classification-w2-vs-1099
description: "Decide whether a US worker is an employee (Form W-2) or an independent contractor (Form 1099-NEC) for federal employment tax in 2026, using the IRS common-law test (behavioral control, financial control, type of relationship), statutory employees and nonemployees, Form SS-8 determinations, the section 530 relief provision, the Voluntary Classification Settlement Program (Form 8952), and the section 3509 rates that measure the exposure when an employee was treated as a contractor. Includes a worked decision, employee or contractor, with the cost of getting it wrong. Trigger on \"employee or contractor\", \"W-2 or 1099\", \"misclassification\", \"Form SS-8\", \"section 530\", \"VCSP\", \"Form 8952\", \"can I pay them as a 1099\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-worker-classification-w2-vs-1099"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US worker classification, employee or independent contractor, tax year 2026

> **Source-cited draft.** Built from IRS Pub. 15-A (2026), Form SS-8 and its instructions, Form 8952 (Rev. November 2024) and 26 U.S.C. 3509, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Scope and who this is for

In scope: a US business (or household) that pays a worker and must decide, for federal employment tax, whether that worker is an employee (withhold income tax, pay social security, Medicare and FUTA, issue Form W-2) or an independent contractor (no withholding, Form 1099-NEC). Also: what to do when the past treatment may be wrong.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Running payroll for employees, Forms 941 and 940 | `us-form-941-940-payroll` |
| Household workers (nanny, cleaner, caregiver) and Schedule H | `us-household-employment-schedule-h` |
| Issuing Form 1099-NEC to contractors, its threshold and deadlines | `us-1099-nec-issuance` |
| The contractor's own Schedule C and self-employment tax | `us-schedule-c-and-se-computation` |
| State tests (ABC tests, state unemployment and wage law) | the state's payroll skill and `us-state-payroll-matrix` |
| Labor law (minimum wage, overtime, benefits) | Not tax: refer to an employment lawyer |

## Ask the client first

1. **What does the worker do, and is it a key part of the client's regular business?**
2. **Control of the work:** who sets the hours, the place, the order of tasks, the methods? Is the worker trained in the client's way of working? Are there performance reviews?
3. **Money side:** how is the worker paid (hourly, salary, a fixed fee per job)? Who pays the tools, software, travel and other costs, and are they reimbursed? Has the worker invested in their own equipment? Can they make a loss?
4. **Market:** does the worker have other clients, a business name, a website, their own insurance? Can they hire helpers or send a substitute?
5. **Relationship:** is there a written contract, and what does it say? Any benefits (health, paid leave, retirement)? Is it open-ended or for one project?
6. **Past treatment:** how long has the worker been paid this way, were Forms 1099 filed every year, and has the client ever treated anyone in a similar job as an employee?
7. **IRS contact:** is the client under an employment tax audit now, or has a worker filed Form SS-8 or claimed unemployment?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Section 3509(a) income tax withholding liability, as a share of wages | 1.5 percent | [26 U.S.C. 3509(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap25-sec3509.htm) |
| Section 3509(a) employee social security and Medicare liability, as a share of the normal employee tax | 20 percent | [26 U.S.C. 3509(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap25-sec3509.htm) |
| Section 3509(b) rates when Forms 1099 or W-2 were not filed: income tax | 3 percent | [26 U.S.C. 3509(b)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap25-sec3509.htm) |
| Section 3509(b) rates when Forms 1099 or W-2 were not filed: employee share | 40 percent | [26 U.S.C. 3509(b)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap25-sec3509.htm) |
| Employer social security rate | 6.2% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Employer Medicare rate | 1.45% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Social security wage base | USD 184,500 | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Form 8952 line 19 rate, on all compensation | 3.24% | [Form 8952 (Rev. November 2024), line 19](https://www.irs.gov/pub/irs-pdf/f8952.pdf) |
| Form 8952 line 22 rate, on compensation up to the social security wage base | 7.44% | [Form 8952 (Rev. November 2024), line 22](https://www.irs.gov/pub/irs-pdf/f8952.pdf) |
| VCSP payment, share of the line 23 amount | 10% | [Form 8952 (Rev. November 2024), line 24](https://www.irs.gov/pub/irs-pdf/f8952.pdf) |
| File Form 8952 at least this long before the date employee treatment starts | 120 days | [Form 8952 (Rev. November 2024), line 17](https://www.irs.gov/pub/irs-pdf/f8952.pdf) |
| Fee for a Form SS-8 determination | none | [Instructions for Form SS-8 (Rev. January 2024)](https://www.irs.gov/pub/irs-pdf/iss8.pdf) |

The 3.24% is 1.5% income tax plus 1.45% employer Medicare plus 20% of the 1.45% employee Medicare. The 7.44% is 6.2% employer social security plus 20% of the 6.2% employee social security. Together, 10.68% of wages up to the base is the yearly section 3509(a) cost.

### Step 1: statutory categories first

1. Some workers are **statutory employees** for social security and Medicare whatever the common-law answer (certain drivers distributing food or laundry, full-time life insurance agents, home workers using the client's materials, full-time traveling salespeople). Some are **statutory nonemployees** (direct sellers, licensed real estate agents paid on output, certain companion sitters). Check Pub. 15-A section 1 before the common-law test. Source: [IRS Pub. 15-A (2026)](https://www.irs.gov/pub/irs-pdf/p15a.pdf).

### Step 2: the common-law test, three groups of facts

2. **Behavioral control:** does the business have the right to direct and control how the work is done, through instructions (when, where, how, which tools, who assists, where to buy supplies, the order of tasks) and training in its own methods? The right to control counts even if it is not used.
3. **Financial control:** unreimbursed business expenses (especially fixed costs), a real investment in tools or facilities, offering the service to the market, the method of pay (a regular wage points to an employee; a flat fee per job to a contractor), and the chance of a profit or a loss.
4. **Type of relationship:** written contracts (what the parties intended, not decisive alone), employee-type benefits, whether the relationship is expected to continue indefinitely, and whether the work is a key part of the business's regular activity.
5. Weigh all the facts; no single factor decides, and the label in the contract does not decide. Source: [IRS Pub. 15-A (2026), section 2](https://www.irs.gov/pub/irs-pdf/p15a.pdf).

### Step 3: the options side by side

| Option | What it costs or gives | When it fits |
| --- | --- | --- |
| Treat as employee now | Employer 7.65% social security and Medicare, FUTA, state unemployment, withholding and Form W-2; no back-tax exposure from here on | Control facts point to employee |
| Keep as contractor | Form 1099-NEC only; exposure to section 3509 back taxes, penalties and interest if wrong | Facts clearly point to a contractor, and Forms 1099 are filed |
| Ask the IRS: Form SS-8 | Formal determination, binding on the IRS for that worker or class if the facts do not change; no fee; not for proposed or hypothetical arrangements | Real doubt, an existing relationship, time to wait |
| VCSP: Form 8952 | Reclassify going forward; pay 10% of the section 3509(a) amount for the most recently completed year, under a closing agreement with the IRS | Past contractor treatment, Forms 1099 filed for 3 years, not under audit |
| Section 530 relief | No federal employment tax for the worker if the client had a reasonable basis, filed all Forms 1099 consistently, and treated no one in a substantially similar job as an employee since 1977 | A defence in an audit; not a choice for new hires |

### Step 4: the figure that decides

6. The decision is made on the facts in step 2, not on cost. The cost figures show what is at stake: the yearly section 3509(a) exposure (10.68% of wages up to the base, more with interest and penalties, 3509(b) rates if Forms 1099 were not filed) against the VCSP payment (one tenth of one year's 3509(a) amount) or the employer's normal 7.65% plus FUTA going forward.
7. Section 3509 does not apply where the employer intentionally disregarded the withholding rules; then the full employee and employer taxes apply. Source: [26 U.S.C. 3509(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap25-sec3509.htm).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Contract says "independent contractor" but the business sets hours and methods | Employee: the facts govern, not the label |
| Former employee rehired to do the same job as a "consultant" | Strong sign of an employee; section 530 consistency fails |
| Worker has an LLC or a business name | Not decisive: test the relationship itself |
| Highly skilled professional given little instruction | The right to control the details still decides; lack of instruction alone does not make a contractor |
| Worker supplied by a staffing firm or PEO | Usually the firm's employee; a CPEO is the employer for wages it pays |
| Owner of an S corporation working in the business | An employee of the corporation: see `us-s-corp-election-decision` |
| Partner in a partnership | Not an employee of the partnership: self-employment tax applies |
| State uses an ABC test | State result may differ from the federal one: check the state skill |
| Under an employment tax audit | VCSP is not available; section 530 and the Classification Settlement Program are argued in the audit: refer |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Who controls the methods | Treat as employee until the client shows otherwise |
| Whether Forms 1099 were filed for past years | Assume not filed: section 3509(b) rates, no section 530, no VCSP |
| Similar workers treated as employees | Assume yes if the client has any employees in the same role |
| Wages above the social security base | Assume none above USD 184,500 |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Worker works only for the client, full time, open-ended | Employee indicators on two of three groups |
| Worker files Form SS-8 or claims unemployment | Often starts an IRS or state inquiry |
| No Forms 1099 filed | Section 3509(b) doubled rates; section 530 and VCSP lost |
| Mixed treatment: employees and contractors in the same role | Section 530 consistency fails |
| Large back exposure across several years | Refer before any filing |

## Worked cases

**Case 1, a decision: employee or contractor?** A design agency pays a designer USD 60,000 a year as a contractor and files Form 1099-NEC each year. The agency sets her hours, gives her its brief templates and software, reviews her work weekly, and she has no other clients: on the Pub. 15-A facts she is an employee.

Cost of treating her as an employee for 2026: employer social security and Medicare 7.65% x USD 60,000 = USD 4,590, plus FUTA (see `us-form-941-940-payroll`). Exposure for each past year if the IRS reclassifies her and section 3509(a) applies: 3.24% x USD 60,000 = USD 1,944 plus 7.44% x USD 60,000 = USD 4,464, total USD 6,408 a year, before penalties and interest. If the Forms 1099 had not been filed, section 3509(b): 3% income tax (USD 1,800), 40% of the employee's 7.65% (USD 1,836) and the employer's 7.65% (USD 4,590), USD 8,226 a year. Recommend: treat her as an employee and consider the VCSP for the past (Case 2), because the facts, not the cost, decide and the yearly exposure grows with each year left open.

```oa-check
name: Employee or contractor, cost and section 3509 exposure (2026)
inputs:
  compensation: 60000
  employer_fica_rate: 0.0765
steps:
  - employer_fica_as_employee: compensation * employer_fica_rate
  - line_19_part: compensation * 0.0324
  - line_22_part: compensation * 0.0744
  - exposure_3509a_per_year: line_19_part + line_22_part
  - exposure_3509b_per_year: compensation * 0.03 + compensation * employer_fica_rate * 0.40 + compensation * employer_fica_rate
expected:
  employer_fica_as_employee: 4590.00
  line_19_part: 1944.00
  line_22_part: 4464.00
  exposure_3509a_per_year: 6408.00
  exposure_3509b_per_year: 8226.00
```

**Case 2, the VCSP payment.** The agency has two designers paid as contractors, USD 60,000 each in 2025 (the most recently completed year), both under the social security wage base, with Forms 1099 filed for 2023, 2024 and 2025 and no audit. It files Form 8952 at least 120 days before it starts treating them as employees.

Form 8952: line 18, USD 120,000. Line 19: x 3.24% = USD 3,888. Line 20: nothing above the wage base, so line 21 is USD 120,000. Line 22: x 7.44% = USD 8,928. Line 23: USD 12,816 (the full one-year section 3509(a) amount). Line 24, the VCSP payment: 10% = USD 1,281.60, paid with the signed closing agreement.

```oa-check
name: VCSP payment on Form 8952 (2026)
inputs:
  line_18_compensation: 120000
  line_20_above_wage_base: 0
steps:
  - line_19: line_18_compensation * 0.0324
  - line_21: line_18_compensation - line_20_above_wage_base
  - line_22: line_21 * 0.0744
  - line_23: line_19 + line_22
  - line_24_vcsp_payment: line_23 * 0.10
expected:
  line_19: 3888.00
  line_22: 8928.00
  line_23: 12816.00
  line_24_vcsp_payment: 1281.60
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-WC-AUDIT | Client is under an IRS, Department of Labor or state employment audit | Refer: VCSP not available; section 530 and settlement are argued in the audit |
| R-WC-INTENT | Facts suggest intentional disregard (cash pay off the books, no Forms 1099) | Refer: section 3509 does not apply; full taxes and possible penalties |
| R-WC-STATE | The question is a state ABC test or state wage law | Use the state payroll skill; labor law to a lawyer |
| R-WC-BENEFITS | Retirement plan or health plan eligibility of reclassified workers | Refer: plan rules are outside this skill |
| R-WC-GOV | State or local government worker, Section 218 agreement | Refer: only the SSA decides Section 218 coverage |

## Filing and payment

Employees from the reclassification date: payroll on Forms 941 and 940, Form W-2 by 1 February 2027 for 2026 wages (`us-form-941-940-payroll`). Contractors: Form 1099-NEC (`us-1099-nec-issuance`). Form SS-8 is filed with the IRS by the firm or the worker. Form 8952 is filed at least 120 days before the date the client wants to start employee treatment; the VCSP payment goes with the signed closing agreement, not with the form.

## Completion checklist

- Statutory employee and nonemployee categories checked first.
- Facts recorded under behavioral control, financial control and type of relationship.
- Past treatment checked: Forms 1099 filed, similar workers, audit status.
- Exposure measured at section 3509(a) or (b) rates as fits the facts.
- Option chosen (employee now, SS-8, VCSP, keep as contractor with section 530 basis documented) and the reason written down.
- State test checked separately.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Pub. 15-A (2026), Employer's Supplemental Tax Guide. Read for statutory employees and nonemployees, misclassification and the relief provision (reasonable basis, information returns, no similar worker treated as employee after 1977), the common-law three categories, Form SS-8 and the VCSP. | https://www.irs.gov/pub/irs-pdf/p15a.pdf | 2026-11-13 |
| IRS Pub. 15 (2026). Read for 6.2%, 1.45% and the USD 184,500 wage base. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-13 |
| 26 U.S.C. 3509 (govinfo). Read for (a) 1.5 percent and 20 percent, (b) 3 percent and 40 percent, (c) intentional disregard. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap25-sec3509.htm | 2026-11-13 |
| Form 8952 (Rev. November 2024). Read for line 17 (120 days), lines 18 to 24 (3.24%, 7.44%, 10%) and the representation on Forms 1099 for the 3 preceding years. | https://www.irs.gov/pub/irs-pdf/f8952.pdf | 2026-11-13 |
| Form SS-8 (Rev. December 2023) and its instructions (Rev. January 2024). Read for what the IRS will not determine, binding effect, information letters and no fee. | https://www.irs.gov/pub/irs-pdf/iss8.pdf | 2026-11-13 |

Not yet confirmed: the IRS VCSP web page (IRS.gov/VCSP) was not opened, so the VCSP eligibility list beyond what Form 8952 states is not quoted; section 530 of the Revenue Act of 1978 was read only through Pub. 15-A's summary, not in its own text.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-worker-classification-w2-vs-1099` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-worker-classification-w2-vs-1099. If neither is available, confirm every figure against the official source pages cited above before relying on it.
