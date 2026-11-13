---
name: us-education-credits-8863
description: Compute the 2026 US American opportunity credit and lifetime learning credit on Form 8863, with the new valid Social Security number rule from Public Law 119-21 section 70606, the unindexed $80,000 to $90,000 ($160,000 to $180,000 joint) phase-out, the 40% refundable part and the under-24 rule, and how the credits meet tax-free scholarships, 529 plans, Coverdell ESAs, employer educational assistance and the student loan interest deduction. Trigger on "education credit", "AOTC", "American opportunity credit", "lifetime learning credit", "Form 8863", "1098-T", "tuition credit". Federal only.
version: "3.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US education credits on Form 8863, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 25A, 221, 529 and 530, Public Law 119-21 sections 70412, 70413, 70414 and 70606, Rev. Proc. 2025-32, IRS Pub. 15-B (2026), the draft 2026 Instructions for Form 8863 and IRS Pub. 970, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 the American opportunity credit (AOTC) is up to **USD 2,500 per eligible student** (100% of the first USD 2,000 and 25% of the next USD 2,000 of adjusted expenses), and **40%** of it is refundable. The lifetime learning credit (LLC) is **20% of up to USD 10,000** of expenses per return, so at most USD 2,000. Both phase out between modified AGI of **USD 80,000 and USD 90,000** (USD 160,000 and USD 180,000 joint); these limits are fixed in the statute and not indexed. New for 2026: the claimant needs a **valid Social Security number** (one spouse is enough on a joint return), and so does a dependent student. An ITIN or ATIN no longer works. Married filing separately gets neither credit.

## Scope and who this is for

In scope: US citizens and resident aliens filing Form 1040 for tax year 2026 who pay college or other postsecondary costs for themselves, a spouse or a dependent. The skill computes the AOTC and LLC on Form 8863 and covers where the credits meet tax-free scholarships, 529 plans, Coverdell ESAs, employer educational assistance (section 127) and the student loan interest deduction (section 221).

Out of scope, and where it goes:

| Topic | Where |
| --- | --- |
| The whole Form 1040, filing status and dependency | `us-form-1040-individual-return` |
| 529 plans in their own right, the 529-to-Roth IRA rollover and Trump accounts | `us-529-and-trump-accounts` |
| Employer-side section 127 plan rules and payroll reporting | `us-form-941-940-payroll` |
| Nonresident or dual-status returns (Form 1040-NR) | `us-form-1040-nr-nonresident-return` |
| State education credits and state 529 deductions or recapture | the state's own tax site; states set their own rules |
| Qualified tuition reduction for school employees, student loan discharge, ABLE accounts, business deduction for work-related education | refer (see the refusal table) |
| Every 2026 federal change in one list | `us-2026-federal-tax-changes` |

The tuition and fees deduction (old section 222) was repealed for tax years beginning after 31 December 2020. Never compute it for 2026.

529 plans and Coverdell ESAs are covered here only where they meet the credits. Their main 2026 rules, kept because they change the planning: for distributions after 4 July 2025, 529 elementary and secondary expenses go beyond tuition to curriculum and curricular materials, books and instructional materials, online materials, tutoring by a licensed teacher or subject expert who is not related to the student, standardized and admission test fees, dual-enrollment fees and educational therapies for students with disabilities (section 529(c)(7) as rewritten by Public Law 119-21 section 70413(a)); postsecondary credentialing expenses count from the same date (section 529(e)(3)(C) and (f), section 70414); registered apprenticeship costs count (section 529(c)(8)); computers, software and internet access used mainly by the beneficiary while enrolled count (section 529(e)(3)(A)(iii)); a change of beneficiary to a member of the beneficiary's family has no income tax consequence (Pub. 970, chapter 7); and a Coverdell balance must be distributed when the beneficiary reaches age 30, except as section 530(d)(7) provides (section 530(b)(1)(E)).

## Ask the client first

1. **Filing status, and residence for the whole year.** Married filing separately rules out both credits. Was the taxpayer or spouse a nonresident alien for any part of 2026, and if so did they elect resident treatment under section 6013(g) or (h)?
2. **Social Security numbers.** Does the taxpayer (or at least one spouse on a joint return) have an SSN that is valid for employment and was issued before the return's due date, including extensions? Does each dependent student have one?
3. **Who claims the student as a dependent for 2026.** If someone claims the student, only that person can take the credit.
4. **For each student:** the program (degree or recognized credential?), the load in each academic period (at least half-time?), the years of postsecondary education completed before 2026, every tax year anyone claimed the AOTC or the older Hope credit for this student, and any felony drug conviction by the end of 2026.
5. **What was paid, and with what money.** Form 1098-T and the school's EIN, the bursar's statement of what was actually paid in 2026 and for which term, receipts for course materials bought elsewhere, every scholarship, grant (including Pell), veterans' benefit and employer payment, whether each grant may be used for room and board, and any Form 1099-Q (529 or Coverdell distributions).
6. **Modified AGI**, and any earlier AOTC denial (and whether it was found reckless or fraudulent). For a student claiming on their own return: age at year end, full-time status, earned income compared with support, whether a parent is alive and whether the student files jointly (the under-24 rule).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| AOTC: share of the first USD 2,000 of adjusted expenses per student | 100% | [26 U.S.C. 25A(b)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| AOTC: share of expenses above USD 2,000 up to USD 4,000 | 25% | [26 U.S.C. 25A(b)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| AOTC maximum per eligible student (result of the two rows above) | USD 2,500 | [26 U.S.C. 25A(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| AOTC: refundable share of the credit after the phase-out (none under the under-24 rule) | 40% | [26 U.S.C. 25A(i)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| AOTC: number of tax years per student | 4 | [26 U.S.C. 25A(b)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| LLC rate, per return | 20% | [26 U.S.C. 25A(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| LLC expense cap, per return, however many students | USD 10,000 | [26 U.S.C. 25A(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| Phase-out start, both credits, other than joint (not indexed) | MAGI over USD 80,000 | [26 U.S.C. 25A(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| Phase-out range, other than joint (no credit at USD 90,000 or more) | USD 10,000 | [26 U.S.C. 25A(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| Phase-out start, joint return (not indexed) | MAGI over USD 160,000 | [26 U.S.C. 25A(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| Phase-out range, joint return (no credit at USD 180,000 or more) | USD 20,000 | [26 U.S.C. 25A(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm) |
| Identification, tax years beginning after 31 December 2025 | valid SSN of the claimant, and of the student if not the taxpayer or spouse | [Public Law 119-21, section 70606](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Student loan interest deduction, maximum | USD 2,500 | [26 U.S.C. 221(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec221.htm) |
| Student loan interest phase-out, other than joint | MAGI USD 85,000 to USD 100,000 | [Rev. Proc. 2025-32, section 4.29](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Student loan interest phase-out, joint | MAGI USD 175,000 to USD 205,000 | [Rev. Proc. 2025-32, section 4.29](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Educational assistance exclusion (section 127), per employee, includes student loan repayments | USD 5,250 | [IRS Pub. 15-B (2026)](https://www.irs.gov/pub/irs-pdf/p15b.pdf) |
| 529 elementary and secondary expenses, per beneficiary, taxable years beginning after 2025 | USD 20,000 | [Public Law 119-21, section 70413(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| 529 student loan repayments, lifetime per individual | USD 10,000 | [26 U.S.C. 529(c)(9)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm) |
| Coverdell ESA contributions, per beneficiary per year (not indexed) | USD 2,000 | [26 U.S.C. 530(b)(1)(A)(iii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec530.htm) |
| Coverdell contribution phase-out start (USD 190,000 joint), over a USD 15,000 (USD 30,000 joint) range | MAGI over USD 95,000 | [26 U.S.C. 530(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec530.htm) |
| Additional tax on the taxable part of a 529 or Coverdell distribution | 10% | [26 U.S.C. 530(d)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec530.htm) |
| Paid preparer due-diligence penalty (section 6695(g)), per failure, returns filed in 2027 | USD 665 | [Rev. Proc. 2025-32, section 4.54](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

The section 127 limit is indexed only for taxable years beginning after 2026 (section 127(d), added by Public Law 119-21 section 70412). Public Law 119-21 did not change the credit amounts or the phase-out limits; the 2020 law that aligned the LLC limits with the AOTC limits also removed the old LLC indexing.

### Steps

1. **Check the bars before computing anything.** No credit at all if: the filing status is married filing separately (section 25A(g)(6)); the taxpayer or spouse was a nonresident alien for any part of the year without an election under section 6013(g) or (h) (section 25A(g)(7)); the taxpayer can be claimed as someone else's dependent; or MAGI is at or above the ceiling. For the AOTC only, also check the ban period after an improper claim and the Form 8862 requirement (section 25A(b)(4)).
2. **Apply the 2026 identification rule.** The claimant must show a Social Security number valid for employment and issued before the due date of the return including extensions; on a joint return only one spouse needs one, even if the other spouse is the student. When the student is a dependent, the student must have one too. The AOTC also needs the EIN of each school paid. A missing SSN or EIN can be assessed as a math error without a deficiency notice (section 6213(g)(2)(J) as amended by section 70606(b)). Source: [Public Law 119-21, section 70606](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [draft 2026 Instructions for Form 8863](https://www.irs.gov/pub/irs-dft/i8863--dft.pdf).
3. **Decide who claims each student.** If the student is claimed as a dependent, all the student's expenses, including those paid by the student or a third party, count as paid by the person claiming the student, and only that person can take a credit. If nobody claims the student, only the student can (Pub. 970, chapter 2).
4. **Test each student for the AOTC** (all tests, see the boundary table). If any test fails, use the LLC for that student. Never claim both credits for the same student in the same year.
5. **Add up qualified expenses paid in 2026** for academic periods beginning in 2026 or in the first 3 months of 2027. Use what was paid, not what was billed and not what Form 1098-T shows.
6. **Reduce to adjusted qualified education expenses.** Subtract tax-free scholarships and grants, tax-free employer assistance, veterans' benefits, other tax-free aid for that period and refunds; take out expenses already used for a tax-free 529 or Coverdell distribution. If a grant may be used for room and board, test whether including it in the student's income gives a larger credit (Case 2).
7. **Tentative credit.** AOTC per student: 100% of the first USD 2,000 plus 25% of the next USD 2,000 (enter no more than USD 4,000 on Form 8863 line 27). LLC per return: 20% of up to USD 10,000 of the combined adjusted expenses of every student not claimed for the AOTC (line 31).
8. **Phase-out.** Multiply each credit by (ceiling minus MAGI) divided by the range: ceiling USD 90,000 and range USD 10,000, or USD 180,000 and USD 20,000 on a joint return; at or above the ceiling the credit is zero. MAGI is AGI plus any excluded foreign earned income or housing and excluded American Samoa or Puerto Rico income (section 25A(d)(2)).
9. **Split the AOTC.** 40% of the AOTC left after the phase-out is refundable (Form 8863 line 8, to Form 1040 line 29), unless the claimant falls within the under-24 rule, in which case all of it is nonrefundable.
10. **Limit the nonrefundable part to tax** with the Credit Limit Worksheet (line 19), to Schedule 3 (Form 1040), line 3.
11. **Paid preparers:** complete Form 8867 for a return claiming the AOTC, check the expenses actually paid rather than relying on Form 1098-T, and keep the records.

## Boundary and exception table

### Who can claim

| Situation | Rule |
| --- | --- |
| Married filing separately | No AOTC and no LLC (section 25A(g)(6)) |
| Nonresident alien for any part of the year (taxpayer or spouse) | No credit unless treated as a resident by an election under section 6013(g) or (h) (section 25A(g)(7)) |
| Taxpayer can be claimed as someone else's dependent | No credit on the taxpayer's own return |
| Student claimed as a dependent | Only the person claiming the student takes a credit; expenses paid by the student or a third party (a grandparent) count as paid by that person |
| Student could be claimed but is not | Only the student can claim, using expenses the student paid or is treated as paying; the under-24 rule may make the AOTC wholly nonrefundable |
| Tuition paid directly to the school under a court-approved divorce decree | Treated as paid by the student, and so by whoever claims the student (Pub. 970, chapter 2) |
| 2026 identification | Valid SSN (valid for employment, issued before the due date including extensions) for the claimant, one spouse being enough on a joint return; a dependent student needs one too; ITIN and ATIN do not qualify |

### AOTC student tests

| Test | Condition, with its boundary |
| --- | --- |
| First 4 years | The student had **not completed** the first 4 years of postsecondary education **before 2026**, as determined by the school. Credit given only for proficiency exams does not count. The graduate-student box on Form 1098-T is information, not the test |
| 4 prior tax years | The AOTC (or Hope credit) was claimed for this student, by anyone, for **3 or fewer** earlier tax years. Count tax years claimed, not academic years |
| Program and load | Enrolled in a program leading to a degree, certificate or other recognized credential **and** carrying **at least half** the normal full-time load, for at least one academic period beginning in 2026. A period starting January to March 2027 counts if paid in 2026 |
| Felony drug conviction | No federal or state felony conviction for possessing or distributing a controlled substance by the end of 2026 |
| Form 1098-T | Needed for both credits unless the school is not required to issue one (qualified nonresident alien students, expenses paid entirely by scholarships, a formal billing arrangement, courses with no academic credit). If a school that must issue one does not, the taxpayer or student must request it after 1 February 2027 and before filing, cooperate with the school, and be able to prove enrollment and payment (draft 2026 Form 8863 instructions) |
| School's EIN | Required for the AOTC, not for the LLC |
| Eligible school | Any college, university, vocational school or other postsecondary school eligible for federal student aid, including some schools abroad |

### LLC conditions

Any number of tax years; no degree or credential program needed; one course is enough; a felony drug conviction does not bar it.

### Qualified expenses for each credit

| Expense | AOTC | LLC |
| --- | --- | --- |
| Tuition and fees required for enrollment or attendance | Yes | Yes |
| Books, supplies and equipment needed for the course | Yes, wherever bought | Only if they must be paid to the school as a condition of enrollment |
| Activity, athletic or other non-academic fees | Only if they must be paid to the school as a condition of enrollment | Same |
| Room and board, insurance, medical costs (including student health fees), transportation, personal costs | Never | Never |
| Sports, games, hobbies or non-credit courses | Only if part of the degree program | Also if the course helps the student get or improve job skills |
| Courses to get or improve job skills, with no degree | No | Yes |
| Expenses paid with a loan | Count in the year paid, not when the loan is repaid | Same |

### No double benefit

- **Scholarships and grants:** a tax-free scholarship reduces the expenses. A grant that by its terms **may** be used for non-qualified costs such as room and board can instead be included in the student's income, and the expenses it would have covered stay available for the credit. This does not work for a grant that must be used for tuition, or for certain tribal government benefits. Emergency financial aid grants under the CARES Act, the 2021 Relief Act and the American Rescue Plan do not reduce the expenses.
- **529 plans and Coverdell ESAs:** a credit can be claimed in the same year as a tax-free distribution, but not on the same expenses. Take the credit expenses out before working out the tax-free part of the distribution. The 10% additional tax does **not** apply to earnings that are taxable only because the expenses were used for the AOTC or LLC (Pub. 970, chapters 6 and 7). Room and board for a student enrolled at least half-time is a qualified 529 expense, within limits, but never a credit expense (section 529(e)(3)).
- **Employer assistance (section 127):** expenses paid with tax-free employer assistance cannot be used for any other deduction or credit. Employer payments of an employee's student loan principal or interest are covered by section 127 permanently for payments after 31 December 2025, within the same annual limit (Public Law 119-21 section 70412). Interest paid that way cannot also be deducted as student loan interest.
- **Business deductions:** expenses deducted elsewhere, for example on Schedule C, cannot also be used for a credit.
- **Student loan interest:** a separate deduction, not allowed for married filing separately or for someone who can be claimed as a dependent, and the taxpayer must be legally obliged to pay the loan (Pub. 970, chapter 4).

### Refunds, prepayments and bans

| Situation | Rule |
| --- | --- |
| Paid in December 2026 for a term starting January to March 2027 | Counts only in 2026, the year paid. Amounts paid in 2025 or 2027 never count for 2026 |
| Refund or tax-free aid received in 2026, or before the 2026 return is filed | Reduce the 2026 expenses |
| Refund or tax-free aid received after the return is filed | Refigure the credit and add the difference as tax for the year the refund or aid was received (recapture) |
| Earlier AOTC finally found due to **reckless or intentional disregard** | No AOTC for the 2 tax years after the most recent tax year with that final determination (section 25A(b)(4)) |
| Earlier AOTC finally found **fraudulent** | No AOTC for the 10 tax years after the most recent such tax year |
| AOTC denied or reduced for any reason other than a math or clerical error, for a tax year beginning after 2015 | Attach Form 8862 to the next return claiming the AOTC |
| Under-24 rule (refundable part) | All nonrefundable if the claimant at the end of 2026 was (a) under 18, or (b) 18 with earned income less than half of support, or (c) over 18 and under 24, a full-time student, with earned income less than half of support; **and** at least one parent was alive; **and** the claimant does not file a joint return |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether the claimant's SSN is valid for employment | No credit until confirmed; ask for the card or the SSA letter |
| Years of earlier AOTC claims | Do not claim the AOTC until the prior returns are checked; show the LLC as the fallback |
| Amount actually paid in 2026 | Use the bursar's statement; never Form 1098-T alone |
| Whether a grant may be used for room and board | Treat it as tax-free and reducing expenses; ask for the award letter |
| Felony drug conviction | Ask directly; the AOTC cannot be claimed without the answer |

### Red flags to raise

| Flag | Why it matters |
| --- | --- |
| Dependent student with only an ITIN | No credit for that student in 2026 |
| AOTC claimed for a fifth year, or for a graduate student | Fails the 4-year tests |
| Same expenses on Form 8863 and in a tax-free 529 or Coverdell distribution | Double benefit; recompute the distribution |
| MAGI just above USD 80,000 or USD 160,000 | Phase-out applies; check whether a deductible retirement contribution lowers MAGI |
| Earlier AOTC denial | Form 8862 and a possible ban period |

## Worked cases

**Case 1, AOTC in the phase-out (married filing jointly).** MAGI is USD 170,000. One dependent student is a full-time sophomore with no earlier AOTC claims and no conviction, and everyone has a valid SSN. Tuition and required fees paid in 2026 are USD 6,000 and there is a USD 1,000 tax-free grant, so adjusted expenses are USD 5,000, capped at USD 4,000 for the AOTC. Tentative credit: USD 2,000 plus 25% of USD 2,000, which is USD 2,500. Phase-out fraction: (USD 180,000 minus USD 170,000) divided by USD 20,000 = 0.5, so the credit is USD 1,250. The refundable part is 40%, USD 500 (Form 1040 line 29). The other USD 750 is nonrefundable and limited to tax (Schedule 3 line 3).

```oa-check
name: AOTC with the joint phase-out (2026)
inputs:
  tuition_paid: 6000
  tax_free_grant: 1000
  magi: 170000
  ceiling: 180000
  range: 20000
steps:
  - adjusted: min(tuition_paid - tax_free_grant, 4000)
  - tentative: min(adjusted, 2000) + 0.25 * max(adjusted - 2000, 0)
  - fraction: clamp((ceiling - magi) / range, 0, 1)
  - credit: tentative * fraction
  - refundable: credit * 0.40
  - nonrefundable: credit - refundable
expected:
  adjusted: 4000
  tentative: 2500
  fraction: 0.5
  credit: 1250
  refundable: 500
  nonrefundable: 750
```

**Case 2, a decision: include part of a Pell grant in income?** A dependent first-year student has USD 5,000 of tuition and required fees and USD 4,000 of room and board. A USD 5,000 Pell grant may be used for either. The parents file jointly with MAGI under USD 160,000, so there is no phase-out. Option A: the whole grant is applied to tuition; adjusted expenses are USD 0 and so is the credit. Option B: USD 4,000 of the grant is applied to room and board and included in the student's income; only USD 1,000 of the grant is tax-free, adjusted expenses are USD 4,000 and the parents' AOTC is USD 2,500, of which USD 1,000 is refundable. Option B gains USD 2,500 of credit at the cost of tax on USD 4,000 of the student's income (a taxable scholarship counts as earned income for a dependent's standard deduction, so the cost is often little or nothing). Recommend Option B unless the student's own tax, or a credit the student loses (such as an earned income credit if the student is the claimant), costs more than USD 2,500. This follows Example 2 in the Form 8863 instructions.

```oa-check
name: Pell grant allocation decision (2026)
inputs:
  tuition: 5000
  pell: 5000
  pell_to_room_board: 4000
steps:
  - adjusted_a: max(tuition - pell, 0)
  - credit_a: min(adjusted_a, 2000) + 0.25 * clamp(adjusted_a - 2000, 0, 2000)
  - adjusted_b: min(max(tuition - (pell - pell_to_room_board), 0), 4000)
  - credit_b: min(adjusted_b, 2000) + 0.25 * clamp(adjusted_b - 2000, 0, 2000)
  - refundable_b: credit_b * 0.40
  - gain: credit_b - credit_a
expected:
  adjusted_a: 0
  credit_a: 0
  adjusted_b: 4000
  credit_b: 2500
  refundable_b: 1000
  gain: 2500
```

**Case 3, LLC for graduate school (single).** MAGI is USD 85,000. The taxpayer finished 4 years of college before 2026, so no AOTC. They pay USD 12,000 of tuition and required fees for a master's programme and USD 800 for textbooks from an outside store that did not have to be paid to the school; the textbooks do not count for the LLC. The capped base is USD 10,000, 20% of it is USD 2,000, the phase-out fraction is (USD 90,000 minus USD 85,000) divided by USD 10,000 = 0.5, so the LLC is USD 1,000, all nonrefundable.

**Case 4, 529 distribution and AOTC in the same year (joint, MAGI below USD 160,000).** A freshman living at home has USD 10,000 of tuition and fees. The 529 plan pays out USD 10,000, of which USD 2,000 is earnings. The parents claim the AOTC on USD 4,000 of the expenses (credit USD 2,500), leaving USD 6,000 for the distribution. Tax-free earnings: USD 2,000 x USD 6,000 / USD 10,000 = USD 1,200. The other USD 800 of earnings is taxable, but the 10% additional tax does not apply to it, because it is taxable only because those expenses were used for the credit (Pub. 970, chapter 7). Planning point: had the student been at least half-time with room and board to set against the 529, the whole distribution could have stayed tax-free.

**Case 5, the 2026 SSN rule, family with ITINs (decision).** A married couple files jointly; one spouse has an SSN valid for employment, the other an ITIN. Their dependent college student has only an ITIN. The joint return meets the claimant rule, but there is no AOTC or LLC for the dependent student's expenses, because the student has no valid SSN. If the ITIN spouse were the student, the credit would be allowed: only one spouse needs a valid SSN, and the spouse is not "an individual other than the taxpayer or the taxpayer's spouse" (section 25A(g)(1)(A)(ii) as amended).

**Case 6, filing status and residence bars (decision).** A married taxpayer paying their own tuition files separately: no AOTC and no LLC, whatever the MAGI. In a second family one spouse was a nonresident alien for part of the year: no credit unless the couple elects under section 6013(g) or (h) to treat that spouse as a resident and files jointly.

**Case 7, the student claims on their own return (decision).** The student is 20, single, full-time, with earned income under half of support, MAGI USD 12,000, both parents alive, second year of a degree, no earlier AOTC claims and a valid SSN. Tuition paid is USD 6,000 with no tax-free aid. The parents are entitled to claim the student but choose not to, so only the student can claim. The whole USD 2,500 AOTC is nonrefundable under the under-24 rule and helps only if the student owes tax. Compare it first with the parents' credit after their phase-out and with anything else they lose by not claiming the student.

**Case 8, refund after filing (recapture).** USD 8,000 of tuition was paid in December 2026 for a spring 2027 term and the LLC claimed on the 2026 return was USD 1,600. After filing, a USD 1,400 refund arrives for dropped courses. The refigured 2026 credit is (USD 8,000 minus USD 1,400) x 20% = USD 1,320; the USD 280 difference is added as tax on the 2027 return (Form 8863 instructions, "Credit recapture").

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-ED-TEST | Any AOTC student test fails | Refuse the AOTC; test the LLC instead |
| R-ED-PROOF | Expenses cannot be supported beyond Form 1098-T | Refuse until the bursar's statement and receipts are in the file; a paid preparer must verify the amounts paid (Form 8867) |
| R-ED-BAN | Return in a 2-year or 10-year ban period, or Form 8862 required but missing | Refuse the AOTC; never leave out Form 8862 |
| R-ED-SSN | 2026 claimant or dependent student without a valid SSN | Refuse the credit for that student; never substitute an ITIN |
| R-ED-NRA | Nonresident or dual-status taxpayer, or a possible section 6013(g) or (h) election | Refer to a specialist and Pub. 519 (`us-form-1040-nr-nonresident-return`) |
| R-ED-SCHOL | Qualified tuition reduction for school employees, teaching or research stipends (payment for services is taxable), athletic or NIL arrangements | Refer; apply Pub. 970, chapter 1 to the award letter |
| R-ED-STATE | State credits, state 529 deductions or recapture | Refer to the state's own tax site |

## Filing and payment

Attach Form 8863 to the 2026 Form 1040 or 1040-SR. Complete a separate Part III for each student before Parts I and II. Part III lines (unchanged in the 2026 draft): 23, AOTC claimed for any 4 tax years before 2026; 24, at least half-time in a credential program; 25, first 4 years completed before 2026; 26, felony drug conviction; 27 to 30, AOTC; 31, LLC. The refundable AOTC goes on Form 1040 line 29; the nonrefundable credits go on Schedule 3 (Form 1040), line 3. The 2026 return is due **15 April 2027**; an extension to 15 October 2027 moves only the filing date, not payment. A credit missed on the 2026 return can be claimed on an amended return within the refund period, provided the SSN rule was met by the due date including extensions.

Paid preparers file Form 8867 with any return claiming the AOTC and keep it, the worksheets, the client documents relied on and a record of the questions and answers for 3 years from the latest of the dates in the Form 8867 instructions. The penalty is USD 665 per failure for returns filed in 2027 (Rev. Proc. 2025-32).

Keep Form 1098-T, the bursar's statements, receipts for course materials, scholarship award letters and Forms 1099-Q with the return file.

## Completion checklist

- Filing status and residence confirmed: not married filing separately, and no part-year nonresident without an election.
- Valid SSN for the claimant (one spouse on a joint return) and for each dependent student, issued before the due date.
- Each student claimed by exactly one person, and the credit on that person's return.
- AOTC tests (first 4 years, 4 prior tax years, program and load, felony, Form 1098-T, EIN) checked student by student; otherwise the LLC, never both for one student.
- Expenses are amounts paid for eligible terms, reduced by tax-free aid and refunds; 529, Coverdell and section 127 money not used for the same expenses; including a grant in income tested where allowed.
- AOTC expenses capped at USD 4,000 per student and LLC expenses at USD 10,000 per return; phase-out on the unindexed limits.
- Under-24 rule checked before showing any refundable AOTC; nonrefundable part limited to tax.
- Ban period and Form 8862 checked for any earlier denied AOTC.
- Paid preparer: Form 8867 completed and records kept for 3 years.
- State treatment referred separately.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 25A (govinfo, 2024 edition). Read for (b)(1) 100% of USD 2,000 and 25% up to USD 4,000, (b)(2)(A) 4 years, (b)(4) bans, (c)(1) 20% of USD 10,000, (d) USD 80,000 / USD 160,000 over USD 10,000 / USD 20,000, (g)(6), (g)(7) and (i)(5) 40% refundable. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25A.htm | 2026-11-13 |
| Public Law 119-21. Read for section 70606 (SSN rule and section 6213(g)(2)(J), taxable years beginning after 31 December 2025), section 70412 (section 127 student loans made permanent, indexed after 2026) and sections 70413 and 70414 (529 changes, USD 20,000). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.29 (student loan interest USD 85,000 to USD 100,000, USD 175,000 to USD 205,000) and section 4.54 (section 6695(g) penalty USD 665). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Draft 2026 Instructions for Form 8863. Read for What's New (valid SSN), the 1098-T request after 1 February 2027, the under-24 questions and lines 8, 19 and 23 to 31. | https://www.irs.gov/pub/irs-dft/i8863--dft.pdf | 2026-11-13 |
| Instructions for Form 8863 (2025), the latest final edition. Read for Example 2 (Pell grant) and credit recapture. | https://www.irs.gov/pub/irs-pdf/i8863.pdf | 2026-11-13 |
| IRS Pub. 970 (2025), Tax Benefits for Education. Read for chapters 2 and 3 (who claims), 4 (student loan interest), 6 and 7 (Coverdell and 529 coordination). | https://www.irs.gov/pub/irs-pdf/p970.pdf | 2026-11-13 |
| IRS Pub. 15-B (2026). Read for the USD 5,250 educational assistance exclusion. | https://www.irs.gov/pub/irs-pdf/p15b.pdf | 2026-11-13 |
| 26 U.S.C. 221 (govinfo). Read for (b)(1), the USD 2,500 maximum. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec221.htm | 2026-11-13 |
| 26 U.S.C. 529 (govinfo). Read for (c)(8), (c)(9)(B) USD 10,000 and (e)(3). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm | 2026-11-13 |
| 26 U.S.C. 530 (govinfo). Read for (b)(1)(A)(iii) USD 2,000, (b)(1)(E) age 30, (c)(1) USD 95,000 / USD 190,000 over USD 15,000 / USD 30,000 and (d)(4) 10%. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec530.htm | 2026-11-13 |

Not yet confirmed: the 2026 Instructions for Form 8863 and the 2026 Pub. 970 were a draft and not yet published when read; the SSN rule above is taken from the Act itself, and the Form 8863 line numbers should be rechecked on the final 2026 form.
