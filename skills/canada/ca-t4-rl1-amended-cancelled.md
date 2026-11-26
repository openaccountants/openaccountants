---
name: ca-t4-rl1-amended-cancelled
description: "Correct filed Canadian T4 and Quebec RL-1 slips: amend, cancel, add or replace; Web Forms, XML and paper correction procedures; employee copies, summaries, filing thresholds and bounded penalty examples. Trigger on amended T4, cancelled T4, additional T4, duplicate T4, report type code A, amended RL-1, cancelled RL-1 and RLZ-1.S."
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
category: payroll
type: computation
version: 1.1
---

# Canada: amended, cancelled and additional T4 and RL-1 slips

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this Guide for an employer correcting slips already filed with the CRA or Revenu Québec. Prepare a correction working paper; this Guide does not file, sign or send it. Payroll calculations and disputed worker status are outside this correction procedure.

The T4 procedures below use the currently available CRA RC4120 Rev. 25; they are not a statement that a 2026 edition has been published. The RL-1 procedure uses RL-1.G-V (2026-10), for 2026. For an earlier year's correction, use that year's form and box definitions rather than copying 2026 amounts.

## Ask the client first

Collect the year, original slips and summaries, filing/processing confirmations, payroll account, error and correct supporting amounts, slip counts by type, original filing channel, employee-copy dates, any PIER or assessment, and whether the employer is a registered charity. Identify separately which T4 and RL-1 entries need correction.

## The method, step by step

### T4: choose the action

Sources: [CRA corrections](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/make-corrections-after-filing/amend.html) and [RC4120, Step 8](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html).

| Situation | Action |
|---|---|
| A box or code on a filed slip is wrong | Amend it once the original return has been processed. Do not send amended or cancelled slips while the original remains unprocessed. |
| Only the employee's address changes | Do not amend the T4. |
| A PIER report arrives | Respond to the PIER report with the changes required for the employees listed; do not send an amendment just because of that report. |
| An employee was omitted | Add the slip as a new original return. For paper, mark it ADDITIONAL, complete all necessary boxes, give two copies to the employee and send one copy to an NVCC with an explanatory letter. Do not amend the T4 Summary. |
| A slip was issued in error, including to a sole proprietor or partner in an unincorporated business | Cancel it. |
| The employee lost or destroyed the slip | Mark a paper replacement DUPLICATE, issue it to the employee and keep a copy. Do not send the replacement to the CRA. |
| CPP or EI was overdeducted and the T4 was already filed | Do not adjust the T4 amounts to resolve the overdeduction. Use Form PD24 for the employer portion: within four years after the end of the overpayment year for CPP, three years for EI. |

Do not show negative dollar amounts on T4 slips. If an employee worked in more than one province or territory, prepare a slip for each province or territory. File a separate T4 return for each payroll account. [RC4120, Steps 3–4](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

### T4: make the correction

You can amend or cancel through Web Forms, Internet file transfer or paper regardless of the original filing channel. File original and amended slips in separate returns. [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

| Channel | Amendment | Cancellation |
|---|---|---|
| Web Forms | Select amended; include only affected slips, preserve unchanged data and correct the wrong fields. Review the generated amended Summary, submit, and explain the reason for each recipient in the amendment dialogue. | Select amended; enter the exact previously reported data and choose cancel. Review the generated amended Summary and submit. |
| Internet file transfer (XML) | Include only affected slips with all unchanged data and corrected fields; use A on the Summary and slips. Total only the amended slips on the amended Summary. Include the reason and recipient's name in the Filer amendment note. | Include only slips to cancel, with all original data; use A on the Summary and C on the slips. Total only those slips on the amended Summary. |
| Paper | Write AMENDED, complete all necessary boxes including unchanged information, give two copies to the employee and send one copy to an NVCC with an explanatory letter. Do not file an amended Summary. | Write CANCELLED; complete all necessary boxes including unchanged information, give two copies to the employee and send one copy to an NVCC with an explanatory letter. Do not file an amended Summary. |

Source for every channel: [RC4120, Choose the filing method to amend, add, replace, or cancel T4 slips](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html).

### Quebec: correct the RL-1 separately

Follow the [RL-1 guide, sections 4.4–4.5](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/) for the provincial slip; correcting the T4 alone does not transmit an RL-1 correction.

| Error | RL-1 action |
|---|---|
| Wrong amount on an already filed slip | File an amended slip. |
| Only the recipient's address is wrong | Resend the original to the recipient only; do not amend. |
| Wrong individual's SIN, first name or last name; wrong CCPC name or identification number | Cancel the slip and file a new one. |
| Slip should not have been filed | Cancel it. |
| Lost or destroyed employee copy | Give a new copy of copy 2 of the original; do not prepare a new slip. |

For an original filed **on paper or through My Account**, amend using the fillable PDF: write Modifié; enter A in Code du relevé, and the original slip's upper-right number in N° du dernier relevé transmis; enter corrected and unchanged amounts. To cancel, photocopy the original, write Annulé and code D, and keep the original upper-right number legible. Mail these amended or cancelled slips to Revenu Québec. [RL-1 guide, 4.5.2](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/)

Always complete and file an amended RL-1 summary when amending or cancelling an RL-1, regardless of how the documents are filed; enclose an explanatory letter with the mailed amended summary. This differs from the paper T4 Summary procedure. [RL-1 guide, 4.5.3](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/)

For an RL-1 originally transmitted in an authorized-software XML file, the RL-1 guide directs preparers to ED-425-V. Check this point with one of our partner accountants.

### Deadlines, copies and original filing threshold

The ordinary T4 filing deadline is the last day of February after the calendar year concerned. A Saturday, Sunday or CRA-recognized public holiday moves it to the next business day. Thus the ordinary deadline for 2026 T4s is **1 March 2027**, derived because 28 February is Sunday. Give the employee's copies by the filing deadline; the paper route uses two copies, delivered in person or sent to the last known address. [ITR 205 and 209](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-205.html), [ITR 209](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-209.html), [CRA deadlines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html)

For T4 cessation or death deadlines: Check this point with one of our partner accountants.

For an ordinary continuing employer, RL-1 slips, the summary and recipient copies are due by the last day of February following the year covered. The paper employee copy is copy 2. For Quebec weekend/holiday adjustments, cessation, permanently stopping remittances or death: Check this point with one of our partner accountants. [RL-1 guide, 4.2–4.4](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/)

For electronic delivery to employees, including consent, secure portals, paper requests and employees on leave or no longer employed: Check this point with one of our partner accountants.

T4 originals must be filed electronically when more than five returns of that type are required for the calendar year. Each slip counts as a return. CRA permits later amendments, additions and deletions on paper or electronically after the original filing. [ITR 205.1](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-205.1.html), [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

More than five RL-1 slips require online filing. Do not extend the CRA's paper-correction permission to Quebec: use the RL-1 channel rules above. [RL-1 guide, 4.3–4.5](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/)

### Penalties used in the cases

These are statutory illustrations, not an estimate of every possible assessment. The federal penalties below exclude registered charities under ITA 162(7), (7.01) and (7.02). The examples assume the employer is not a registered charity; that eligibility fact must be obtained for an actual employer. [ITA 162](https://laws-lois.justice.gc.ca/fra/lois/I-3.3/section-162.html)

| Failure and scope | Amount (statutory) | Source |
|---|---|---|
| 6–50 original T4 slips filed on paper when electronic filing is required | $125 for that return type | [ITA 162(7.02)(a)](https://laws-lois.justice.gc.ca/fra/lois/I-3.3/section-162.html) |
| 6–50 original RL-1 slips filed in the wrong manner | $125 for that return type | [TAA 59.0.0.3(a)](https://www.legisquebec.gouv.qc.ca/fr/document/lc/A-6.002) |
| 1–50 T4 slips filed late | Greater of $100 and $10 per day, counting at most 100 days | [ITA 162(7.01)(a)](https://laws-lois.justice.gc.ca/fra/lois/I-3.3/section-162.html) |
| 51–500 T4 slips filed late | Greater of $100 and $15 per day, counting at most 100 days | [ITA 162(7.01)(b)](https://laws-lois.justice.gc.ca/fra/lois/I-3.3/section-162.html) |
| T4 employee copies given late | $25 per day for each slip, minimum $100, maximum $2,500; excludes failures for which another ITA provision imposes a penalty, except the provisions retained by 162(7) | [RC4120, Giving your employees their T4 slips](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html), [ITA 162(7)](https://laws-lois.justice.gc.ca/fra/lois/I-3.3/section-162.html) |

CRA recalculates a late-filing penalty when slips are added or cancelled, using the revised late-slip count and days late, and issues a new assessment. CRA also has a relieving administrative policy for small-filer late returns; distinguish that policy from the statutory calculation. [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html), [CRA penalty policy](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html)

For other slip-count bands, Quebec late-filing or employee-copy penalties, missing-information penalties and their reasonable-effort/SIN exceptions, interest, or penalty relief (including Form RC4288): Check this point with one of our partner accountants.

## Worked cases

All original amounts and counts below are hypothetical inputs. Assume a non-charity employer and no waiver of the applicable original-filing requirement or penalty relief. These conditions are not established merely by the counts.

### Late T4 return, then slips cancelled

The employer filed **60 T4 slips 20 days late**; **10** were wrongly issued to partners in an unincorporated business. Before cancellation, the statutory penalty is max($100, 20 × $15) = **$300**. After cancelling those slips, **50** remain: max($100, 20 × $10) = **$200**, a **$100** reduction. This illustrates the statutory recalculation, not a promise of an assessment reduction for an actual employer. [ITA 162(7.01)](https://laws-lois.justice.gc.ca/fra/lois/I-3.3/section-162.html), [RC4120 recalculation](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

```oa-check
name: Late T4 penalty recalculated after cancelling slips
inputs:
  slips_filed: 60
  slips_cancelled: 10
  days_late: 20
steps:
  penalty_before: max(100, 15 * min(days_late, 100))
  slips_after: slips_filed - slips_cancelled
  penalty_after: max(100, 10 * min(days_late, 100))
  reduction: penalty_before - penalty_after
expected:
  slips_after: 50
  penalty_before: 300
  penalty_after: 200
  reduction: 100
```

### Paper filing and late employee copies

A Quebec employer has **8 employees**, with **8 original T4 slips** and **8 original RL-1 slips**, all filed on paper on time. The statutory wrong-manner penalties are **$125 federally** and **$125 provincially**. **Three** employees receive T4 copies **12 days late**: max($100, 12 × $25) = **$300 each**, below the **$2,500** cap; total **$900** for the copies, or **$1,150** including both wrong-manner penalties. Assume these are three distinct slip-delivery failures and no other statutory provision displaces the 162(7) penalty; no additional Quebec employee-copy penalty is calculated. Later T4 corrections can use paper under CRA's correction guidance; this is not permission to file the eight originals on paper. [ITA 162(7), (7.02)](https://laws-lois.justice.gc.ca/fra/lois/I-3.3/section-162.html), [TAA 59.0.0.3](https://www.legisquebec.gouv.qc.ca/fr/document/lc/A-6.002), [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

```oa-check
name: Wrong-manner and late-copy penalties, T4 and RL-1
inputs:
  t4_slips_on_paper: 8
  rl1_slips_on_paper: 8
  late_copies: 3
  days_late_copies: 12
steps:
  federal_manner: 125
  quebec_manner: 125
  per_copy: min(2500, max(100, 25 * min(days_late_copies, 100)))
  copies_penalty: per_copy * late_copies
  total: federal_manner + quebec_manner + copies_penalty
expected:
  per_copy: 300
  copies_penalty: 900
  total: 1150
```

## When to refuse or refer

For salary overpayments and affected boxes; CPP, EI or QPP not withheld; pension adjustments in box 52; whole-return cancellation or wrong accounts; successor employers; disputed worker status; T4A/NR4 implications; or an existing CRA/Revenu Québec review: Check this point with one of our partner accountants.

For XML original-return coding or a correction outside the editions and procedures identified above: Check this point with one of our partner accountants.

## Sources

- [CRA RC4120, Rev. 25](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html): read for Step 8 correction channels, Step 4 copies, overdeductions and late-penalty recalculation on 2026-11-26.
- [CRA correction instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/make-corrections-after-filing/amend.html) and [filing deadlines and penalty policy](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html): read for the amended/additional/replacement instructions and the deadline and relieving-policy tables on 2026-11-26.
- Income Tax Regulations [205](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-205.html), [205.1](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-205.1.html) and [209](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-209.html): read for the ordinary filing date, electronic-filing threshold and paper-copy provisions on 2026-11-26.
- [Income Tax Act 162, official French text](https://laws-lois.justice.gc.ca/fra/lois/I-3.3/section-162.html): subsections (7), (7.01) and (7.02), read 2026-11-26.
- [Revenu Québec RL-1.G-V (2026-10)](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/): sections 4.2–4.5; prior applicable 2026-11-23 reads of deadlines and employee distribution reused, applicability confirmed and correction instructions read 2026-11-26.
- [Quebec Tax Administration Act](https://www.legisquebec.gouv.qc.ca/fr/document/lc/A-6.002) 37.1.1 and 59.0.0.3, and [Regulation respecting fiscal administration](https://www.legisquebec.gouv.qc.ca/fr/document/rc/A-6.002,%20r.%201?cible=) 37.1.1R1–R2: official French operative text read 2026-11-26.

Not yet confirmed: procedures outside the stated editions and the specialist cases identified above are referred; no unverified figure is offered as usable guidance.
