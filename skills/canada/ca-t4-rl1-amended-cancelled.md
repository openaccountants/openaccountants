---
name: ca-t4-rl1-amended-cancelled
description: "Correct T4 slips already filed with the CRA and RL-1 slips filed with Revenu Quebec, for tax year 2026 and earlier years: when to amend, cancel, add an additional slip or issue a duplicate; the T4 report type codes for Internet file transfer (A on the summary and slips, C on cancelled slips); paper markings and copies; when the T4 Summary is or is not re-filed; the electronic filing threshold of more than 5 slips; deadlines and the federal and Quebec penalties for late, paper or incomplete slips. Trigger on: amended T4, cancel T4 slip, T4 issued in error, additional T4, duplicate T4, report type code A, RL-1 amended, RL-1 cancelled, RLZ-1.S, late T4 penalty, T4 filed on paper penalty. Out of scope: computing CPP, EI or tax (canada-payroll), PIER notices and unwithheld CPP or QPP (ca-cpp-qpp-not-withheld), pension adjustment (ca-pension-adjustment), Quebec contributions (qc-employer-contributions)."
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-21
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
category: payroll
type: computation
version: 1.0
---

# Canada: amended, cancelled and additional T4 and RL-1 slips v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

An employer (or a payroll service acting for one) has already filed T4 slips with the Canada Revenue Agency (CRA), and for Quebec employees RL-1 slips with Revenu Quebec, and finds an error, a missing slip, a slip that should never have been issued, or an employee who lost a slip. This skill sets out which correction to make, how to make it on each filing channel, what goes to the employee, and the penalties the Income Tax Act and the Quebec Tax Administration Act attach to late, wrongly filed or incomplete slips. It applies to 2026 slips (filed in early 2027) and to corrections of earlier years.

It does not compute the amounts on the slip. Income tax, CPP and EI amounts come from [canada-payroll](canada-payroll.md); Quebec QPP, QPIP and employer contributions from [qc-employer-contributions](quebec/qc-employer-contributions.md). A pensionable and insurable earnings review (PIER) and CPP or QPP that was not withheld belong to `ca-cpp-qpp-not-withheld`; a pension adjustment in box 52 to `ca-pension-adjustment`.

The CRA guide used is RC4120, Employers' Guide, Filing the T4 Slip and Summary, edition Rev. 25 (for 2025 slips). The edition for 2026 slips was not published when this skill was written; re-read the new edition when it appears.

## Ask the client first

1. Which slips, for which calendar year, and has the CRA (or Revenu Quebec) already received and processed the original return?
2. What exactly is wrong: an amount or box, the employee's identity or SIN, only the address, a slip issued to someone who was not an employee, a missing employee, or a lost slip?
3. How was the original filed (Web Forms, Internet file transfer, My Business Account or Represent a Client, or paper), and how many slips of that type does the employer file for the year?
4. Was the original return late, and if so by how many days? Did the CRA send a penalty notice or a PIER report?
5. Are any of the employees employed in Quebec, so that an RL-1 is also affected?
6. Have the employees already been given their copies, and on paper or electronically with consent?

## The method, step by step

### Choose the correction [RC4120, Choose the filing method to amend, add, replace, or cancel T4 slips](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

| Situation | Action | What not to do | Official source |
|---|---|---|---|
| A filed T4 slip carries a wrong amount or field | Amend the slip | Do not file negative amounts; RC4120 says "Do not show negative dollar amounts on slips" | [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |
| Only the employee's address changed | No amendment | RC4120: do not amend "if the only change is to the employee's address" | [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |
| The CRA sent a PIER report | Answer the PIER report, not an amended slip; see `ca-cpp-qpp-not-withheld` | Do not amend because of the PIER listing | [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |
| An employee was left out of the original return | Add a slip (paper: mark it "ADDITIONAL", send one copy to the NVCC with a letter) | On paper, do not file an amended T4 Summary | [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |
| A T4 was issued in error, for example to a sole proprietor or a partner in an unincorporated business | Cancel the slip (see the channel table below) | - | [RC4120, T4 slips filed in error](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |
| The employee lost or destroyed the slip | Issue a replacement marked "DUPLICATE" and keep a copy | Do not send the duplicate to the CRA | [RC4120, Replace T4 slips](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |
| CPP or EI was over-deducted and the T4 is filed | Leave the slip as it is; the employer recovers its own share on Form PD24, within four years (CPP) or three years (EI) from the end of the year | RC4120: "do not adjust the amounts you reported on the T4 slip" | [RC4120, CPP and EI overdeductions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |
| The whole T4 return was wrong (wrong account, filed twice) | Cancel the entire return online or on paper, or send a request by mail or fax to the National Verification and Collections Centre (NVCC), attention Employer Services | - | [RC4120, Cancel a T4 return](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |

RC4120 also covers salary overpayments found after filing: the slip for the year of the overpayment is amended in the ways that guide describes. Follow its examples for the box 14, 24 and 26 changes; this skill does not restate them.

### Make the correction on the right channel [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

A slip can be amended, added or cancelled online or on paper "regardless of how the T4 slips were originally filed". Online means Web Forms or Internet file transfer with a web access code, or My Business Account or Represent a Client without one.

| Channel | Amend | Cancel | Summary |
|---|---|---|---|
| Web Forms | Select the amended option; enter only the slips to amend, with all unchanged data and the corrected fields; explain the reason per employee (limit 1,250 characters) | Select the amended option; enter the exact data previously reported and choose cancel | Web Forms creates the amended T4 Summary; review it |
| Internet file transfer (XML) | Include only the slips to amend; report type code A on the T4 Summary and the slips; all data on each slip; filer amendment note (limit 1,309 characters) | Include only the slips to cancel; report type code A on the T4 Summary and code C on the slips; enter all data that was on the original slip | Only the totals of the amended (or cancelled) slips go on the amended T4 Summary |
| Paper | Write "AMENDED" at the top; complete all boxes including those that were right; two copies to the employee; one copy to the NVCC with a letter | Write "CANCELLED" at the top; complete all boxes; two copies to the employee; one copy to the NVCC with a letter | Do not file an amended T4 Summary |

File original and amended slips as separate returns. A paper amendment cannot be made until the original paper return has been processed. The source for every line of this table is the RC4120 section above. The report type code for an original return is set in the CRA XML specification, which this skill did not read (see Sources).

### Electronic filing threshold [Income Tax Regulations s. 205.1(1)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-205.1.html); [Income Tax Act s. 162(7.02)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html)

T4 is a prescribed type: it "must be filed electronically if more than five information returns of that type are required to be filed for a calendar year" (Reg. 205.1(1)). Each slip is an information return, and the penalty is counted per type of return. RC4120 adds that after the original return is filed, slips can be amended, added or deleted on paper or electronically.

| Slips of one type filed in the wrong manner | Penalty amount | Official source |
|---|---|---|
| 6 to 50 | $125 | [ITA s. 162(7.02)(a)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| 51 to 250 | $250 | [ITA s. 162(7.02)(a.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| 251 to 500 | $500 | [ITA s. 162(7.02)(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| 501 to 2,500 | $1,500 | [ITA s. 162(7.02)(c)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| more than 2,500 | $2,500 | [ITA s. 162(7.02)(d)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| 5 or fewer | nil | [ITA s. 162(7.02)(e)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |

### Deadlines and copies to the employee [Income Tax Regulations ss. 205, 206, 209](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-205.html)

| Rule | Detail, figure or amount | Official source |
|---|---|---|
| Filing date | On or before the last day of February, for the preceding calendar year (Reg. 205(1)). RC4120: if the date falls on a Saturday, Sunday or public holiday the return is due the next business day. 28 February 2027 is a Sunday, so 2026 slips are due 1 March 2027 (derived from the rule and the calendar) | [Reg. 205](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-205.html) |
| Business discontinued | Within 30 days of the discontinuance (Reg. 205(2)) | [Reg. 205](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-205.html) |
| Death of the person who must file | Legal representative files within 90 days of the date of death (Reg. 206(1)) | [Reg. 206](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-206.html) |
| Employee copies | Two paper copies to the employee by the filing date, at the last known address or in person (Reg. 209(1)-(2)); one electronic copy with the employee's express consent, in writing or electronically (Reg. 209(3)-(4)) | [Reg. 209](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-209.html) |
| T4 electronic without consent | Allowed under Reg. 209(5) unless the specified criteria in s. 221.01 of the Act are not met, the employee asks for paper, is on extended leave or is no longer an employee, or cannot reasonably be expected to have electronic access | [Reg. 209](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-209.html) |

Corrected slips (amended or cancelled) go to the employee in two copies under the RC4120 paper steps above.

### Federal penalties [Income Tax Act s. 162](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html)

| Failure | Penalty amount | Official source |
|---|---|---|
| T4 return filed late, fewer than 51 slips | Greater of $100 and $10 a day, at most 100 days | [ITA s. 162(7.01)(a)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| 51 to 500 slips | Greater of $100 and $15 a day, at most 100 days | [ITA s. 162(7.01)(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| 501 to 2,500 slips | Greater of $100 and $25 a day, at most 100 days | [ITA s. 162(7.01)(c)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| 2,501 to 10,000 slips | Greater of $100 and $50 a day, at most 100 days | [ITA s. 162(7.01)(d)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| more than 10,000 slips | Greater of $100 and $75 a day, at most 100 days | [ITA s. 162(7.01)(e)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| Slip not given to the employee on time | RC4120: $25 a day for each slip, minimum $100, maximum $2,500 (the general rule in s. 162(7): greater of $100 and $25 a day, at most 100 days) | [ITA s. 162(7)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| Required information missing from a prescribed form | $100 for each failure, subject to the exceptions in the subsection | [ITA s. 162(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |

RC4120 states that the late filing penalty "is recalculated if T4 information returns are added or cancelled", on the updated count of late slips and the days late, with a new notice of assessment. It also says the CRA applies an administrative policy that reduces the assessed penalty for small businesses; the figures above are the statutory amounts, so the assessed figure may be lower. Interest runs on unpaid penalties at the prescribed rate, compounded daily. Relief from penalties and interest is requested on Form RC4288 and is limited to the 10 calendar years before the year of the request.

### Quebec: RL-1 slips [Regulation respecting the Taxation Act ss. 1086R1, 1086R65-1086R70](https://www.legisquebec.gouv.qc.ca/en/document/cr/I-3,%20r.%201); [Tax Administration Act ss. 37.1.1, 59.0.0.3, 59.0.0.4, 59.0.2](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002)

The RL-1 is a separate return to Revenu Quebec. A T4 correction does not correct the RL-1, and the reverse; make both when the error touches both slips.

| Rule | Detail, figure or amount | Official source |
|---|---|---|
| Filing date | On or before the last day of February, for the preceding calendar year (s. 1086R65) | [Reg. I-3, r. 1](https://www.legisquebec.gouv.qc.ca/en/document/cr/I-3,%20r.%201) |
| Business ceased | Within 30 days of the cessation (s. 1086R67); death: legal representatives within 90 days (s. 1086R68) | [Reg. I-3, r. 1](https://www.legisquebec.gouv.qc.ca/en/document/cr/I-3,%20r.%201) |
| Employee copy | A copy of the part of the return that concerns the person, by the filing date; electronic with express consent; the RL-1 may be sent electronically without consent unless the employee asks for paper, is on extended leave or no longer an employee, or cannot be expected to have access (s. 1086R70) | [Reg. I-3, r. 1](https://www.legisquebec.gouv.qc.ca/en/document/cr/I-3,%20r.%201) |
| Electronic filing | RL-1 is a prescribed type; above the threshold of 5 it must be filed by technological means (TAA s. 37.1.1; Regulation respecting fiscal administration ss. 37.1.1R1(a), 37.1.1R2(a)) | [Reg. A-6.002, r. 1](https://www.legisquebec.gouv.qc.ca/en/document/cr/A-6.002,%20r.%201) |
| Wrong manner, 6 to 50 RL-1 slips | $125 | [TAA s. 59.0.0.3(a)](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002) |
| Wrong manner, 51 to 250 / 251 to 500 / 501 to 2,500 / more than 2,500 | $250 / $500 / $1,500 / $2,500 | [TAA s. 59.0.0.3(b)-(e)](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002) |
| Late, fewer than 51 / 51 to 500 / 501 to 2,500 / 2,501 to 10,000 / more than 10,000 slips | Greater of $100 and $10 / $15 / $25 / $50 / $75 a day, at most 100 days | [TAA s. 59.0.0.4](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002) |
| Required information missing on a prescribed form | $100 | [TAA s. 59.0.2](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002) |

Section 59.0.0.4 applies to the types listed in s. 37.1.1R1 (s. 59.0.0.4R1), which include the RL-1. How an amended or cancelled RL-1 is coded, which slip number it carries, and when an amended RL-1 summary (RLZ-1.S) is filed are set in Revenu Quebec's guide RL-1.G-V. This skill could not read that guide (see Not yet confirmed); open the current edition before preparing a corrected RL-1, and do not apply the T4 report type codes to it.

## Boundary and exception table

| Situation | Action |
|---|---|
| Amounts on the slip are wrong because the deductions were wrong | Fix the payroll first with [canada-payroll](canada-payroll.md); then amend the slip |
| CPP or QPP not withheld, or a PIER report | `ca-cpp-qpp-not-withheld`; do not amend for PIER |
| Pension adjustment in box 52 changes | `ca-pension-adjustment` (RC4120 sets its own amended-PA rule) |
| Employee worked in more than one province | One T4 slip per province or territory of employment (RC4120); correct the slip for the province affected |
| The worker was never an employee | Cancel the T4; the payment may belong on a different slip, which this skill does not cover |
| Several payroll accounts | One T4 return per payroll account; correct under the account that filed the slip |
| Penalty already assessed and the client wants it removed | Taxpayer relief request (Form RC4288) or a refer; this skill does not argue relief |

## Worked cases

All amounts are hypothetical inputs. Penalties are the statutory figures before any CRA administrative reduction.

### Late T4 return, then slips cancelled

An employer filed 60 T4 slips 20 days late. Sixty slips fall in the 51 to 500 band: 20 days at $15 is $300, which is more than the $100 minimum. Ten of the slips were issued in error to partners and are cancelled. The CRA recalculates on 50 late slips, which falls in the under-51 band: 20 days at $10 is $200. Cancelling the wrong slips lowers the statutory penalty by $100.

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

### Paper filing above the threshold, late copies, and the Quebec twin

A Quebec employer has 8 employees and filed 8 T4 slips and 8 RL-1 slips on paper, on time. Both types are above the threshold of 5, so the wrong-manner penalty applies to each type: $125 federally and $125 in Quebec. Three employees received their T4 copies 12 days late: 12 days at $25 is $300 a slip, above the $100 minimum and below the $2,500 maximum, so $900 for three. Later amendments to those slips may be filed on paper: RC4120 says that after the original return is filed, slips "can be amended, added, or deleted in paper, or electronic format".

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

Refer to a qualified Canadian payroll professional when the error changes who the employer is (business number, payroll account, successor employer after an amalgamation), when the worker's status as employee or contractor is disputed, when a slip correction would also change a T4A, NR4 or another slip type, or when the CRA or Revenu Quebec has opened a review or assessment. Do not prepare a corrected RL-1 until the Revenu Quebec guide RL-1.G-V has been read for its codes. This skill does not file, sign or send anything and does not request penalty relief.

## Sources

| Source | URL | Read for; read on |
|---|---|---|
| CRA, RC4120 Employers' Guide, Filing the T4 Slip and Summary, Rev. 25 (2025 slips; the 2026 edition is not yet published) | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html | Due date and weekend rule, late filing and electronic filing penalty tables, giving slips and copies, amend, add, replace and cancel T4 slips (Web Forms, Internet file transfer, paper), report type codes A and C, slips filed in error, CPP and EI overdeductions, relief and interest; read 2026-11-21 in a browser (the site refuses scripted downloads) |
| Income Tax Act, s. 162(5), (7), (7.01), (7.02) (current to 2026-10-29) | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html | Penalty amounts and bands; read 2026-11-21 |
| Income Tax Regulations, ss. 200(1), 205, 205.1, 206, 209 (current to 2026-10-29) | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/FullText.html | T4 obligation, filing date, prescribed types and electronic threshold, death, copies to the employee; read 2026-11-21 |
| Regulation respecting the Taxation Act (Quebec), ss. 1086R1, 1086R65, 1086R67, 1086R68, 1086R70 | https://www.legisquebec.gouv.qc.ca/en/document/cr/I-3,%20r.%201 | RL-1 obligation, filing date, cessation, death, copies; read 2026-11-21 |
| Tax Administration Act (Quebec), ss. 37.1.1, 59.0.0.3, 59.0.0.4, 59.0.2 | https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002 | Electronic filing duty and Quebec penalties; read 2026-11-21 |
| Regulation respecting fiscal administration (Quebec), ss. 37.1.1R1, 37.1.1R2, 59.0.0.4R1 | https://www.legisquebec.gouv.qc.ca/en/document/cr/A-6.002,%20r.%201 | RL-1 as a prescribed type and the threshold of 5; read 2026-11-21 |

Not yet confirmed: Revenu Quebec's guide RL-1.G-V (amended RL-1 code "A", cancelled RL-1 code "D", the slip number to use, whether and when an amended RL-1 summary RLZ-1.S is filed, and paper versus online rules for corrections) could not be read: revenuquebec.ca returned a bot-protection page and the web.archive.org copy was refused (HTTP 429) on 2026-11-21. The report type code for an original T4 return in the CRA XML specification was not read. The Quebec weekend and holiday rule for the RL-1 due date, and the Quebec penalty for failing to give an RL-1 copy to the employee, were not confirmed. The RC4120 edition for 2026 slips was not yet published.
