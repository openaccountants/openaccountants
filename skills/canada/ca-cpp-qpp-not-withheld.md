---
name: ca-cpp-qpp-not-withheld
description: "What an employer does when CPP contributions or EI premiums (and, for Quebec employees, QPP contributions) were not withheld or were under-withheld, for tax year 2026 and earlier years: the CRA pensionable and insurable earnings review (PIER) and its 30-day reply window; paying or disputing a PIER; the employer's liability for both the employee's and the employer's shares (Canada Pension Plan s. 21(2), Employment Insurance Act s. 82(4)); recovering the employee's share only from later pay within 12 months, one missed amount per pay (CPP s. 21(4), EI Act s. 82(6)); interest and failure-to-remit penalties; the Quebec QPP liability (QPP Act ss. 59, 60, 63; Tax Administration Act s. 59.2). Trigger on: PIER, PIER report, CPP not deducted, EI under-deducted, recover CPP from employee, QPP not withheld, CPP deficiency. Out of scope: computing CPP, EI or QPP (canada-payroll, qc-employer-contributions), self-employed CPP (ca-fed-cpp-ei), slip mechanics (ca-t4-rl1-amended-cancelled)."
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

# Canada: CPP, EI and QPP not withheld, and the PIER v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

An employer failed to deduct, or deducted too little, Canada Pension Plan (CPP) contributions or Employment Insurance (EI) premiums from an employee's pay, and either found it itself or received a pensionable and insurable earnings review (PIER) from the Canada Revenue Agency (CRA). For employees in Quebec the same question arises for Quebec Pension Plan (QPP) contributions, which Revenu Quebec collects. This skill covers who pays, how much of it can be taken back from the employee and when, how to answer a PIER, and the interest and penalties the statutes set. It applies to 2026 payroll and to corrections of earlier years.

It does not compute the contribution or premium itself: the 2026 rates, maximums and exemptions are in [canada-payroll](canada-payroll.md) (federal) and [qc-employer-contributions](quebec/qc-employer-contributions.md) (Quebec). Over-deductions, which are refunded through Form PD24, and slip amendments belong to `ca-t4-rl1-amended-cancelled`. Self-employed CPP is [ca-fed-cpp-ei](ca-fed-cpp-ei.md).

## Ask the client first

1. Which contributions are short: CPP, EI, QPP, or more than one; for which employees, which pay dates and which calendar year?
2. Was the employee employed in Quebec (QPP and Revenu Quebec) or elsewhere in Canada (CPP and the CRA)? Did anyone work in both?
3. Has the T4 (and RL-1) for that year been filed? Has the CRA sent a PIER report, and what is its reply date?
4. Is the employee still on the payroll, and how many pays remain within 12 months of each pay that was short?
5. Does the employer agree with the CRA's figures, for example on exempt employment, age, a CPP election, or province of employment?
6. Was any of the amount actually deducted from pay but not remitted? That is a different and more serious failure.

## The method, step by step

### Step 1: who owes what [Canada Pension Plan ss. 9(1), 21(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html); [Employment Insurance Act ss. 68, 82(1), 82(4), 84](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-82.html)

| Rule | What the law says | Official source |
|---|---|---|
| CPP: employer that fails to deduct and remit | "liable to pay to Her Majesty the whole amount that should have been deducted and remitted from the time it should have been deducted" (CPP s. 21(2)) | [CPP s. 21](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| CPP: employer's own contribution | Owed on every employee in pensionable employment, whether or not the employee's share was deducted (CPP s. 9(1)); remitted with the employee's share (s. 21(1)) | [CPP s. 9](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-9.html) |
| EI: employer that fails to deduct and remit | Liable for "the whole amount that should have been deducted and remitted" (EI Act s. 82(4)) | [EI Act s. 82](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-82.html) |
| EI: employer's premium | 1.4 times the employee premiums the employer is required to deduct (EI Act s. 68) | [EI Act s. 68](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-68.html) |
| EI: employer's premium cannot be passed on | Not recoverable from the insured person by withholding or otherwise (EI Act s. 84) | [EI Act s. 84](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-84.html) |
| Ruling defence | No liability, interest or penalty where a written CRA ruling said no deduction was needed, the ruling was not based on materially incorrect information, and a later decision says the deduction was due (CPP s. 21(3); EI Act s. 82(5)); the employer still owes its own share, without interest or penalty | [CPP s. 21](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |

The CRA states the practical result: if you under-deducted, "you are responsible for remitting the balance due for both the employer's and employee's shares" ([CRA, Make corrections before filing](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-corrections.html)). The CRA may assess the employer for amounts payable (CPP s. 22(1); EI Act s. 85(1)). For a corporation, directors at the time of the failure are jointly and severally liable (CPP s. 21.1(1)).

### Step 2: recover the employee's share, within the limits [CPP s. 21(4)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html); [EI Act s. 82(6)](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-82.html)

| Limit | Rule | Official source |
|---|---|---|
| Only from later pay | The amount may be deducted "from any subsequent payment of remuneration made to the employee within 12 months after the making of the payment from which the amount was required to be deducted" (CPP s. 21(4)); EI Act s. 82(6) has the same 12-month rule | [CPP s. 21](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| One missed amount per pay | On top of the normal deduction, no more than one previously missed amount may be taken from a single pay (CPP s. 21(4); EI Act s. 82(6)) | [EI Act s. 82](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-82.html) |
| CRA conditions | The recovered amount can equal but not exceed what should have been deducted from each payment; nothing outstanding for more than 12 months; income tax deductions cannot be adjusted to cover the shortfall | [CRA, Make corrections before filing](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-corrections.html) |
| Reporting a prior-year recovery | A prior-year shortfall recovered in the current year is not reported on the current year's T4 | [RC4120, CPP and EI underdeductions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |

What cannot be recovered inside these limits stays a cost of the employer. The statutes give no other route to take the employee's share back through payroll; any private claim against the employee is outside this skill.

### Step 3: the PIER [CRA, Pensionable and insurable earnings review (PIER)](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/receiving-payroll/earnings-review.html)

Each year the CRA compares the CPP and EI required on the pensionable and insurable earnings reported on the T4 slips with the CPP and EI reported. Differences are printed on a PIER listing, sent with a PIER summary showing any balance due and a remittance voucher. The PIER arrives in My Business Account or Represent a Client (where it stays available for the last 5 years) and by mail.

| Day | What happens | Official source |
|---|---|---|
| Day 1 | PIER package sent; reply requested within 30 calendar days | [CRA PIER page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/receiving-payroll/earnings-review.html) |
| Day 45 | Notice of assessment if there is no reply and no payment in full; it includes applicable penalties or interest | [CRA PIER page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/receiving-payroll/earnings-review.html) |
| Day 65 | The CRA issues the amended T4s to the employer | [CRA PIER page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/receiving-payroll/earnings-review.html) |

How to answer:

1. Check each listed employee: pensionable and insurable earnings in boxes 26 and 24, age, exempt employment, province of employment (a Quebec employee pays QPP, not CPP), and any period the employee was not in pensionable or insurable employment. RC4120 notes that correct amounts in boxes 24 and 26 reduce unnecessary PIERs, "especially if the employee worked both inside and outside of Quebec".
2. Agree: pay the exact amount on the PIER by the deadline. No reply is needed. In My Business Account the PIER overview has a "Proceed to pay" option (not in Represent a Client).
3. Disagree with some or all of it: return the PIER with the corrected information and an explanation, through My Business Account or Represent a Client, by mail to the return address on the PIER, or by fax to the National Verification and Collections Centre. Pay any part that is not disputed.
4. Do not send amended T4 slips because of a PIER. The CRA prepares two copies of each amended T4: one for the employer's records, one for the employee (RC4120 and the CRA PIER page).
5. Several payroll accounts: the CRA compares all T4 returns under the business number and contacts the employer only if it finds a deficiency.

### Step 4: interest and penalties [CPP s. 21(6)-(7)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html); [EI Act s. 82(8)-(9)](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-82.html)

| Item | Rate or rule | Official source |
|---|---|---|
| Interest | Prescribed rate, from the day the amount should have been remitted to the day it is remitted (CPP s. 21(6); EI Act s. 82(8)) | [CPP s. 21](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| Received on time but not in the required manner | 3% of the amount | [CPP s. 21(7)(a)(i)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| Received 1 to 3 days late | 3% | [CPP s. 21(7)(a)(ii)(A)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| 4 to 5 days late | 5% | [CPP s. 21(7)(a)(ii)(B)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| 6 to 7 days late | 7% | [CPP s. 21(7)(a)(ii)(C)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| Not remitted by the 7th day after it was due | 10% | [CPP s. 21(7)(a)(iii)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| Second failure in the year, knowingly or with gross negligence | 20% | [CPP s. 21(7)(b)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-21.html) |
| EI premiums | The same 3%, 5%, 7%, 10% and 20% structure | [EI Act s. 82(9)](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-82.html) |

These are failure-to-remit penalties. The PIER page says the notice of assessment "will include applicable penalties or interest, or both"; which penalty the CRA applies to a PIER deficiency, and at what rate, is the CRA's assessment, so present the statutory figure as the most it can be. Relief from penalties and interest is a taxpayer relief request (Form RC4288).

### Step 5: the employee's pension record [CPP s. 15(1.1)](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-15.html)

If the employer did not deduct and the employee notified the Minister of the failure before June 30 of the following year, the amount that should have been deducted is counted toward the employee's contributions for the year (CPP s. 15(1.1) for the base contribution, with parallel rules for the first and second additional contributions). When the employer later pays an amount it failed to deduct, CPP s. 21(3.1) deems that notice given in the ruling case. Tell the employee; do not compute the employee's CPP record here.

### Step 6: Quebec employees and QPP [Act respecting the Quebec Pension Plan ss. 34, 52, 57, 59, 60, 63](https://www.legisquebec.gouv.qc.ca/en/document/cs/R-9); [Tax Administration Act ss. 59.2, 61](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002)

| Rule | What the law says | Official source |
|---|---|---|
| Duty to deduct | "An employer shall deduct from the remuneration paid to his employee for pensionable employment such amount as is prescribed on account of the employee's contributions." (QPP Act s. 59) | [QPP Act](https://www.legisquebec.gouv.qc.ca/en/document/cs/R-9) |
| Failure to deduct | "An employer who fails to deduct a prescribed amount from the remuneration of an employee is liable to pay such amount to the Minister." (s. 60) | [QPP Act](https://www.legisquebec.gouv.qc.ca/en/document/cs/R-9) |
| Employer's own contribution | Equal to the contributions each employee must make (s. 52); paid to the Minister with the amounts required to be deducted, on the dates in Taxation Act s. 1015 (s. 63) | [QPP Act](https://www.legisquebec.gouv.qc.ca/en/document/cs/R-9) |
| Employee's record | An amount the employer pays on account of the employee's contribution that it failed to deduct is deemed deducted for that year (s. 57) | [QPP Act](https://www.legisquebec.gouv.qc.ca/en/document/cs/R-9) |
| Collection | The Minister of Revenue collects the contributions and remits them to Retraite Quebec with the interest and penalties (s. 34) | [QPP Act](https://www.legisquebec.gouv.qc.ca/en/document/cs/R-9) |
| Penalty for failure to deduct | "a penalty of 15% of that amount", for an amount a person was required to deduct, withhold or collect under a fiscal law (TAA s. 59.2) | [TAA](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002) |
| Interest | A debt owed to the State under a fiscal law bears interest at the regulated rate (TAA s. 28) | [TAA](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002) |
| Offence | Contravening QPP Act ss. 59 and 63 is an offence: a fine of $800 to $10,000, or the fine and up to six months' imprisonment, on top of any penalty (TAA s. 61) | [TAA](https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002) |

The QPP Act text read for this skill contains no rule like CPP s. 21(4) allowing the employer to take the missed amount from later pay. Whether Revenu Quebec allows recovery from the employee, how a QPP correction is reported (RL-1 and RLZ-1.S), and how Revenu Quebec reviews QPP the way the PIER reviews CPP are set out in its employer guide TP-1015.G-V, which this skill could not read (see Not yet confirmed). Until that guide is read, treat the full QPP shortfall as the employer's cost and do not deduct it from later pay.

## Boundary and exception table

| Situation | Action |
|---|---|
| Amounts were deducted from pay but not remitted | Not a "not withheld" case: the deducted amount is held for the Crown; refer at once |
| Employee worked in and outside Quebec in the year | Check that CPP and QPP each sit on the right slip before answering a PIER |
| Employee was exempt (age, election, excluded employment) | Dispute the PIER line with the evidence; do not pay it |
| Employee left before the shortfall was found | No later pay, so no recovery; the employer bears the employee's share |
| Corporation cannot pay | Directors' liability (CPP s. 21.1); refer |
| Over-deduction rather than under-deduction | Form PD24 and `ca-t4-rl1-amended-cancelled` |
| Worker status disputed (employee or contractor) | Ruling under CPP s. 26.1 or EI Act s. 90; refer |

## Worked cases

Amounts are hypothetical inputs taken as given on a PIER or the payroll records; the 2026 rates themselves are in [canada-payroll](canada-payroll.md).

### PIER shows CPP and EI shortfalls for one employee who has left

A 2025 PIER shows the employee's CPP was short by $400 and EI by $120. The employer agrees. It owes the employee's shares plus its own: CPP employer share equal to the employee's ($400) and EI employer premium at 1.4 times ($168). The employee left in December 2025, so nothing can be recovered from later pay. Paying the PIER amount in full by the reply date closes it without a reply. If it were assessed instead and the 10% failure-to-remit rate were applied to the full amount, the statutory maximum penalty would be $108.80 before interest.

```oa-check
name: PIER deficiency, employee and employer shares, no recovery possible
inputs:
  cpp_employee_short: 400
  ei_employee_short: 120
  recoverable_pays: 0
steps:
  cpp_employer: cpp_employee_short
  ei_employer: ei_employee_short * 1.4
  total_due: cpp_employee_short + cpp_employer + ei_employee_short + ei_employer
  employee_share_recovered: min(cpp_employee_short + ei_employee_short, recoverable_pays)
  employer_cost: total_due - employee_share_recovered
  max_penalty_if_assessed: total_due * 0.10
expected:
  ei_employer: 168
  total_due: 1088
  employer_cost: 1088
  max_penalty_if_assessed: 108.80
```

### Shortfall found in time: recover from later pay, or absorb it

A current employee was paid every two weeks. On four pays in October and November 2026 the employer deducted no CPP; each should have carried $100. The employer finds the error in December 2026. All four pays are within the last 12 months, so each later pay may carry the normal deduction plus one missed $100. Over the next four pays the employer recovers $400; the employer also remits its own $400, so the total remitted for the shortfall is $800 and the net cost to the employer is its own $400.

The decision the employer faces is timing. Each missed amount must be recovered within 12 months of the pay it was missed on. If the employee is about to leave and only two pays remain, only $200 can be recovered, and the employer bears the other $200 on top of its own share.

```oa-check
name: Recovery from later pay within the 12-month and one-per-pay limits
inputs:
  missed_pays: 4
  missed_per_pay: 100
  pays_left_if_staying: 4
  pays_left_if_leaving: 2
steps:
  employee_short: missed_pays * missed_per_pay
  employer_share: employee_short
  total_remitted: employee_short + employer_share
  recovered_if_staying: min(missed_pays, pays_left_if_staying) * missed_per_pay
  recovered_if_leaving: min(missed_pays, pays_left_if_leaving) * missed_per_pay
  employer_cost_staying: total_remitted - recovered_if_staying
  employer_cost_leaving: total_remitted - recovered_if_leaving
expected:
  total_remitted: 800
  recovered_if_staying: 400
  recovered_if_leaving: 200
  employer_cost_staying: 400
  employer_cost_leaving: 600
```

## When to refuse or refer

Refer to a qualified Canadian payroll professional when amounts were deducted but not remitted, when the shortfall is large or covers several years, when worker status, exempt employment or province of employment is disputed, when directors' liability or insolvency is in view, and for any Quebec QPP correction until Revenu Quebec's guide TP-1015.G-V has been read. Do not compute 2026 contributions here and do not advise deducting a shortfall from pay outside the 12-month, one-per-pay rule. This skill does not file a PIER reply or make a payment.

## Sources

| Source | URL | Read for; read on |
|---|---|---|
| CRA, Pensionable and insurable earnings review (PIER) (page dated 2025-09-09) | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/receiving-payroll/earnings-review.html | What a PIER is, contents, 30-day reply, day 45 and day 65, response channels, payment, amended T4s, multiple accounts; read 2026-11-21 in a browser (the site refuses scripted downloads) |
| CRA, Make corrections before filing | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-corrections.html | Under-deducted CPP and EI: both shares, recovery conditions, 12 months; read 2026-11-21 in a browser |
| CRA, RC4120 Employers' Guide, Filing the T4 Slip and Summary, Rev. 25 (2025 slips; 2026 edition not yet published) | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html | PIER section, CPP and EI underdeductions, do not amend for PIER; read 2026-11-21 in a browser |
| Canada Pension Plan, ss. 9(1), 15(1.1), 21, 21.1, 22(1), 23(1) (current to 2026-10-29) | https://laws-lois.justice.gc.ca/eng/acts/C-8/FullText.html | Liability, recovery, interest, penalties, assessment, directors, employee record; read 2026-11-21 |
| Employment Insurance Act, ss. 68, 82, 84, 85(1) (current to 2026-10-29) | https://laws-lois.justice.gc.ca/eng/acts/E-5.6/FullText.html | Employer premium, liability, recovery, interest, penalties, assessment; read 2026-11-21 |
| Act respecting the Quebec Pension Plan (R-9), ss. 34, 52, 57, 59, 60, 63 | https://www.legisquebec.gouv.qc.ca/en/document/cs/R-9 | Employer duty and liability for QPP; read 2026-11-21 |
| Tax Administration Act (A-6.002), ss. 28, 59.2, 61 | https://www.legisquebec.gouv.qc.ca/en/document/cs/A-6.002 | Interest, 15% failure-to-deduct penalty, offence; read 2026-11-21 |

Not yet confirmed: Revenu Quebec's employer guide TP-1015.G-V and any form TP-1015.G could not be read (revenuquebec.ca returned a bot-protection page and the archive copy was refused on 2026-11-21), so this skill does not say what TP-1015.G is, whether Revenu Quebec lets an employer recover unwithheld QPP from later pay, how a QPP shortfall is corrected on the RL-1 and RLZ-1.S, or whether Revenu Quebec runs a QPP review like the PIER. That TAA s. 59.2 is applied by Revenu Quebec to unwithheld QPP is a reading of the statute (the QPP Act contributions are collected by the Minister, QPP Act s. 34), not confirmed from a Revenu Quebec publication. Which penalty the CRA actually assesses on a PIER deficiency (beyond "applicable penalties or interest") was not found in a CRA publication; the CRA page on payroll penalties returned no readable text.
