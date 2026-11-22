---
name: ca-nol-suspension-and-business-credit-limit
description: >
  California's suspension of the net operating loss carryover deduction and
  the USD 5,000,000 cap on business credits, for tax year 2026, for both
  personal income tax filers (individuals, estates, trusts, owners of
  pass-through businesses) and corporations. Covers who is exempt (under
  USD 1,000,000 of net business income or modified AGI, or of corporate
  income subject to California tax; disaster loss carryovers), the 3, 2 and
  1 year carryover extensions, which credits sit outside the cap (low-income
  housing, PTE elective tax credit, AMT credit, personal credits such as
  CalEITC), combined-report groups, the FTB 3870 refundable credit election
  (20% a year for 5 years from the third year after the election), and the
  2026 SB 122 extension of the credit cap through 2029 and the permanent
  70%-or-USD 5,000,000 cap from 2030. Trigger on "California NOL suspension",
  "SB 167", "SB 175", "SB 122 credit limitation", "FTB 3870", "California
  R&D credit cap 5 million", "FTB 3805Q", "FTB 3805V".
version: 0.1
jurisdiction: US-CA
category: state-tax
tax_year: 2026
last_updated: 2026-11-21
tier: 2
domain: tax
type: computation
---

# California NOL suspension and USD 5,000,000 business credit limit, tax year 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from the FTB net operating loss page (last updated 12/01/2025), FTB What's New with Tax Forms (last updated 08/28/2026), FTB Tax News March 2025 and August 2026, the FTB analysis of SB 122 (amended 12 June 2026) and the FTB list of expiring provisions, read on 2026-11-21. The California statute site (leginfo.legislature.ca.gov) refused our reader, so statute sections are cited only where an FTB page names them. No accountant has reviewed it.

**Answer first.** For taxable years beginning in **2024, 2025 and 2026**, California does not allow the NOL carryover deduction to taxpayers at or above **USD 1,000,000** of income (individuals: net business income or modified AGI; corporations: income subject to California tax). The NOL is still computed and carried forward, and the carryover period is lengthened to make up for it. Over the same years, business credits (carryovers included) cannot cut tax by more than **USD 5,000,000** a year; the excess carries over, or the taxpayer can elect on **FTB 3870** to get it back as a refund, 20% a year for 5 years starting in the third year after the election. Legislation enacted in 2026 (SB 122) **extends the credit cap through taxable years beginning before 1 January 2030** and makes a permanent cap (the greater of 70% of tax or USD 5,000,000) from 2030. SB 122 did not extend the NOL suspension: 2026 is its last year.

**Tax year.** 2026 (taxable years beginning on or after 1 January 2026 and before 1 January 2027).

**Circular 230 disclosure.** This material is general information, not written advice on a specific transaction under 31 CFR 10.37. It is not intended to be used, and cannot be used, to avoid penalties.

## Scope and who this is for

In scope: any California return that has an NOL carryover or business credits in a taxable year beginning in 2026: Forms 540 and 540NR (including owners of sole proprietorships, partnerships, LLCs and S corporations), 541 for estates and trusts, and Form 100 and other corporate returns, including combined-report groups ([FTB, Net operating loss](https://www.ftb.ca.gov/file/business/deductions/net-operating-loss.html); [FTB What's New](https://www.ftb.ca.gov/forms/whats-new.html)).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Computing the NOL itself (what is a loss, federal differences) | refer; FTB 3805V (individuals, estates, trusts) or FTB 3805Q (corporations) |
| The individual tax figures these rules sit beside | `ca-income-tax`, `ca-540-individual-return` |
| The PTE elective tax credit | `ca-pte-elective-tax` |
| Whether a particular credit (R&D, CalCompetes, film) is earned | refer |
| Disaster loss deductions themselves | refer |

## Ask the client first

- Is the taxpayer an individual, estate or trust, or a corporation? Is the corporation in a combined report, and with whom?
- For an individual: what are net business income and modified AGI for 2026? For a corporation: what is income subject to California tax for 2026?
- What NOL carryovers exist, by the year each loss arose, and is any of it a disaster loss carryover?
- What business credits are available for 2026 (current year and carryovers), credit by credit, and what is tax (or net tax) before credits?
- Was an FTB 3870 election made for 2024 or 2025? Does the client want refundability for 2026, and will the 2026 return be filed on time (the election needs an original, timely return)?
- Is it an S corporation, and are the credits claimed at entity level?

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| NOL carryover deduction suspended | taxable years beginning on or after 1 January 2024 and before 1 January 2027 | The NOL is still computed and carried over | [FTB What's New](https://www.ftb.ca.gov/forms/whats-new.html) |
| Not affected: personal income tax filers | net business income or modified AGI of less than USD 1,000,000 | Also not affected: disaster loss carryovers | [FTB, Net operating loss](https://www.ftb.ca.gov/file/business/deductions/net-operating-loss.html) |
| Not affected: corporations | income subject to California taxation of less than USD 1,000,000 | Also not affected: disaster loss carryovers | same |
| Carryover extension, losses from years beginning before 1 January 2024 | 3 years | Suspended losses only | [FTB What's New](https://www.ftb.ca.gov/forms/whats-new.html) |
| Carryover extension, losses from years beginning in 2024 | 2 years | same | same |
| Carryover extension, losses from years beginning in 2025 | 1 year | same | same |
| Business credit cap, 2024 to 2026 | USD 5,000,000 a year | Total business credits, including carryovers, may not reduce net tax (personal) or tax (corporate) by more; applied on an aggregate basis to a combined-report group | [FTB Tax News, March 2025](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/03.html) |
| Business credit cap extended by SB 122 | taxable years beginning before 1 January 2030 | The cap and the annual refundable credit election periods are extended by three years | [FTB Tax News, August 2026](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2026/08.html) |
| Permanent cap from 2030 | greater of 70% of tax or net tax, or USD 5,000,000 | Taxable years beginning on or after 1 January 2030; disallowed amounts carry over | same |
| Refundable credit election (FTB 3870) | 20% a year for 5 years | Of the credit disallowed by the cap; the refund period starts in the third taxable year after the election year | [FTB Tax News, March 2025](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/03.html); [FTB SB 122 analysis](https://www.ftb.ca.gov/tax-pros/law/legislation/2025-2026/SB122-061226.pdf) |

### Steps

1. **NOL: test the USD 1,000,000 line.** Individual, estate or trust: if net business income or modified AGI is under USD 1,000,000, the 2026 NOL deduction is allowed as normal. Corporation: if income subject to California taxation is under USD 1,000,000, the same. Disaster loss carryovers are allowed in every case ([FTB, Net operating loss](https://www.ftb.ca.gov/file/business/deductions/net-operating-loss.html)).
2. **NOL: at or above the line,** take no NOL carryover deduction for 2026. Still compute the 2026 NOL (if any) and carry every loss forward on FTB 3805V (individuals, estates, trusts) or FTB 3805Q (corporations).
3. **NOL: extend each suspended carryover.** Add 3 years to losses from years beginning before 2024, 2 years to 2024 losses, 1 year to 2025 losses ([FTB What's New](https://www.ftb.ca.gov/forms/whats-new.html)). A 2026 loss gets no extension: no later year is suspended.
4. **Credits: separate business credits from the rest.** The cap does not apply to the low-income housing credit or the credit for prior-year AMT ([FTB What's New](https://www.ftb.ca.gov/forms/whats-new.html)), nor to the PTE elective tax credit ([FTB Tax News, March 2025](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/03.html)). For personal income tax, the FTB's SB 122 analysis also lists as outside it: earned income, young child, foster youth, household and dependent care, SBRA elective tax, adoption costs, renters, personal exemption, joint custody head of household, dependent parent, senior head of household and excess unemployment compensation contributions credits, and annual refundable credit amounts ([FTB SB 122 analysis](https://www.ftb.ca.gov/tax-pros/law/legislation/2025-2026/SB122-061226.pdf)).
5. **Credits: apply business credits first,** against net tax (personal) or tax (corporate), before other credits ([FTB Tax News, March 2025](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/03.html)). Cap the total at USD 5,000,000, for a combined-report group across all members together.
6. **Credits: the excess.** Either carry it over (the carryover period is lengthened by the number of years the credit was not allowed), or elect refundability on FTB 3870.
7. **The FTB 3870 election.** Annual and irrevocable, on FTB 3870 attached to an **original, timely filed** return for the year. If made for any credit disallowed by the cap that year, it must be made for all of them. The refund is 20% of the elected amount in each of 5 years, beginning with the third taxable year after the election year. An S corporation cannot elect refundability for credits taken at entity level ([FTB Tax News, March 2025](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/03.html)).
8. **Look ahead to 2027.** The NOL suspension ends with taxable years beginning in 2026 ([FTB, Expiring provisions](https://www.ftb.ca.gov/about-ftb/data-reports-plans/Summary-of-Federal-Income-Tax-Changes/Expiring-Provisions.html); [FTB Tax News, August 2026](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2026/08.html) lists no NOL change). The USD 5,000,000 credit cap continues for 2027 to 2029 under SB 122, then becomes the greater of 70% of tax or USD 5,000,000. From 2027 the refundable motion picture amount from the one-time election is not counted toward the cap ([FTB SB 122 analysis](https://www.ftb.ca.gov/tax-pros/law/legislation/2025-2026/SB122-061226.pdf)).

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Individual with MAGI USD 900,000 and an NOL carryover | NOL deduction allowed in 2026 | [FTB, Net operating loss](https://www.ftb.ca.gov/file/business/deductions/net-operating-loss.html) |
| Disaster loss carryover, income over USD 1,000,000 | Allowed; not affected by the suspension | same |
| Combined-report group, credits spread across members | One USD 5,000,000 cap for the group in aggregate | [FTB Tax News, March 2025](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/03.html) |
| Credits disallowed, no FTB 3870 | Carry over, with the period lengthened by the years disallowed | same |
| Late-filed or amended return | FTB 3870 cannot be made: it needs an original, timely return | same |
| S corporation entity-level credits | No refundability election at entity level | same |
| Pass-through owner's share of business credits | Counted in the owner's own USD 5,000,000 cap on the personal return | [FTB What's New](https://www.ftb.ca.gov/forms/whats-new.html) |

**AUDIT FLASH POINT** The FTB 3870 election is irrevocable and all-or-nothing for the year. Electing for one credit elects for every credit disallowed that year, and the refunds do not start until the third year after the election.

## Worked cases

Both cases are made up for illustration; the rules come from the linked FTB pages.

**Case 1: a corporation with an old NOL in 2026.** A calendar-year corporation has 2026 income subject to California tax of USD 3,200,000 before any NOL. It carries an NOL of USD 2,000,000 from 2022 and USD 600,000 from 2024; no disaster losses. Income is over USD 1,000,000, so no NOL deduction is allowed for 2026: income subject to tax stays USD 3,200,000 and USD 2,600,000 carries forward. The 2022 loss gets 3 extra years of carryover and the 2024 loss 2 extra years. If 2026 income had been USD 950,000, the full USD 950,000 could have been offset.

```oa-check
name: Corporation 2026, NOL suspended above USD 1,000,000
inputs:
  income_before_nol: 3200000
  nol_2022: 2000000
  nol_2024: 600000
steps:
  - nol_deduction: 0
  - income_after_nol: income_before_nol - nol_deduction
  - carried_forward: nol_2022 + nol_2024
  - extension_years_2022_loss: 3
  - extension_years_2024_loss: 2
expected:
  nol_deduction: 0.00
  income_after_nol: 3200000.00
  carried_forward: 2600000.00
  extension_years_2022_loss: 3
  extension_years_2024_loss: 2
```

**Case 2, a decision: carry over the excess R&D credit, or elect refundability?** A corporation's 2026 tax before credits is USD 12,000,000. It has USD 9,000,000 of California research credit available and no other credits. The cap allows USD 5,000,000; USD 4,000,000 is disallowed.

- **Way 1: carry over.** USD 4,000,000 carries to 2027, its carryover period lengthened by the year it was disallowed. But the cap still applies in 2027 to 2029 (SB 122), so it is usable only in a year when credits stay under USD 5,000,000.
- **Way 2: elect on FTB 3870 with the timely original 2026 return.** USD 4,000,000 becomes refundable at 20% a year: USD 800,000 in each of 2029, 2030, 2031, 2032 and 2033 (the third taxable year after 2026 is 2029).
- **What decides it:** whether the company expects to have room under the cap in 2027 to 2029. A company that will keep generating more than USD 5,000,000 of credits a year never gets room under the cap, so the refund is the only way to see the cash; a company whose credits will drop below USD 5,000,000 may use the carryover sooner than 2029.

```oa-check
name: USD 5,000,000 cap and FTB 3870 refund schedule, 2026 election
inputs:
  tax_before_credits: 12000000
  credit_available: 9000000
  cap: 5000000
  election_year: 2026
steps:
  - credit_used: min(credit_available, cap, tax_before_credits)
  - tax_after_credits: tax_before_credits - credit_used
  - disallowed: credit_available - credit_used
  - annual_refund: disallowed * 0.20
  - first_refund_year: election_year + 3
  - last_refund_year: first_refund_year + 4
expected:
  credit_used: 5000000.00
  tax_after_credits: 7000000.00
  disallowed: 4000000.00
  annual_refund: 800000.00
  first_refund_year: 2029
  last_refund_year: 2033
```

## When to refuse or refer

- Computing the NOL itself, an NOL of a nonresident or part-year resident, or an NOL inside a combined report: refer (FTB 3805V or 3805Q).
- Whether a credit is earned, its amount, and its own carryover life: refer to the credit's own rules.
- Whether the 2027 to 2029 cap will bind, and modelling the 2030 permanent cap: refer; this skill only states the rule.
- A fiscal-year taxpayer whose year straddles 1 January 2027: the rules follow the taxable year's **beginning** date; confirm with a practitioner.

## Filing and payment

- Individuals, estates and trusts: the suspension and the extended carryover are worked on FTB 3805V; the business credit cap and credit ordering on Schedule P (540) for the year (see `ca-540-individual-return`) ([FTB, Net operating loss](https://www.ftb.ca.gov/file/business/deductions/net-operating-loss.html)).
- Corporations: FTB 3805Q with Form 100 and the credit schedules.
- FTB 3870: attach to the original, timely filed 2026 return; one election per year, covering every credit the cap disallowed that year ([FTB What's New](https://www.ftb.ca.gov/forms/whats-new.html)).

## Completion checklist

- [ ] Taxpayer type and the USD 1,000,000 test confirmed on the right income measure.
- [ ] NOL carryovers listed by loss year; disaster losses separated.
- [ ] Extended carryover years recorded (3, 2, 1).
- [ ] Credits sorted into business credits under the cap and credits outside it.
- [ ] Business credits applied first and capped at USD 5,000,000 (group-wide for a combined report).
- [ ] Refund or carryover decision made before the original return is filed; FTB 3870 attached if elected.
- [ ] Client told the cap continues for 2027 to 2029 and the NOL suspension ends after 2026.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| FTB, Net operating loss (last updated 12/01/2025). Read for the 2024 to 2026 suspension, the USD 1,000,000 tests for individuals and for corporations, disaster losses, FTB 3805V and 3805Q. | https://www.ftb.ca.gov/file/business/deductions/net-operating-loss.html | 2026-11-21 |
| FTB, What's New with Tax Forms (last updated 08/28/2026). Read for the SB 167 and SB 175 items: suspension period, exemptions, the 3, 2 and 1 year extensions, the USD 5,000,000 cap, the LIHC and AMT-credit exclusions, ordering, carryover extension and FTB 3870. | https://www.ftb.ca.gov/forms/whats-new.html | 2026-11-21 |
| FTB Tax News, March 2025. Read for the NOL suspension, the business credit cap, the PTE credit exclusion, combined reports, and the FTB 3870 election (20% over 5 years from the third year, S corporation rule). | https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2025/03.html | 2026-11-21 |
| FTB Tax News, August 2026. Read for SB 122 and SB 180: the cap extended to taxable years beginning before 1 January 2030 and the permanent 70% or USD 5,000,000 cap from 2030. | https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2026/08.html | 2026-11-21 |
| FTB, Bill analysis, SB 122 (amended 12 June 2026). Read for Provision 1 (extension, the refundable election described, excluded credits, motion picture refund from 2027) and Provision 2 (permanent cap from 2030). | https://www.ftb.ca.gov/tax-pros/law/legislation/2025-2026/SB122-061226.pdf | 2026-11-21 |
| FTB, Expiring provisions in the California Revenue and Taxation Code (last updated 03/02/2026, before SB 122). Read for R&TC 17276.24 and 24416.24 (NOL suspension) and 17039.4 and 23036.4 (credit cap), both shown ending 12/31/2026, and footnotes 5 and 6 on the Department of Finance determinations. | https://www.ftb.ca.gov/about-ftb/data-reports-plans/Summary-of-Federal-Income-Tax-Changes/Expiring-Provisions.html | 2026-11-21 |

Not yet confirmed: the text of R&TC 17276.24, 24416.24, 17039.4, 23036.4, 17039.5 and 23036.5 as amended by SB 122 (leginfo.legislature.ca.gov refused our reader); the chaptered text of SB 122 (the FTB analysis read is of the 12 June 2026 amended bill, and Tax News August 2026 confirms the extension and the 2030 cap); whether any Director of Finance determination by 14 May 2026 lifted either rule for 2026 (no FTB page read says so, and FTB What's New dated 28 August 2026 still lists both for 2026); the refund percentage and timing for FTB 3870 elections made for 2027 to 2029; whether "net business income or modified adjusted gross income" means the suspension applies when either measure reaches USD 1,000,000.

> **Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
