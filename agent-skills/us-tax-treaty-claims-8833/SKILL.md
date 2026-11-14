---
name: us-tax-treaty-claims-8833
description: "Decide when a US income tax treaty position must be disclosed on Form 8833 for tax year 2026, and how. Covers section 6114 (disclosure of positions that a treaty overrules or modifies the Internal Revenue Code), the waivers in Regulations section 301.6114-1(c), positions that must always be reported (residence tie-breaker, US real property gains, branch profits, permanent establishment, foreign tax credits the Code does not allow), the saving clause and its exceptions for US citizens and residents, dual-resident taxpayers filing Form 1040-NR, and the section 6712 penalty of $1,000 per failure ($10,000 for a C corporation). Trigger on \"Form 8833\", \"treaty-based return position\", \"treaty benefits disclosure\", \"saving clause\", \"tie-breaker rule\", \"dual resident\", \"treaty exemption on my return\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-tax-treaty-claims-8833"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US treaty-based return positions and Form 8833, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 6114, 6712 and 894, Form 8833 (Rev. December 2022) and its instructions, and IRS Pub. 519 (2025), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Anyone who takes the position on a US return that a treaty overrules or modifies the Internal Revenue Code, and so reduces (or may reduce) their tax, must disclose it on Form 8833 unless the regulations waive it. One form per position, every year. Missing it costs **$1,000** per failure, **$10,000** for a C corporation, on top of any other penalty. US citizens and most residents cannot use most treaty benefits at all, because of the saving clause.

## Scope and who this is for

In scope: individuals (citizens, residents, dual residents and nonresident aliens) and entities filing a 2026 US federal income tax return that relies on an income tax treaty, estate and gift tax treaty or friendship, commerce and navigation treaty. The skill decides whether Form 8833 is needed, what goes on it and what happens if it is missed.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether the person is a US resident under the Code (green card, substantial presence) | `us-tax-residency` |
| The nonresident return itself | `us-form-1040-nr-nonresident-return` |
| Foreign tax credit computation | `us-foreign-tax-credit-1116` |
| Foreign earned income exclusion | `us-foreign-earned-income-2555` |
| Long-term residents who claim treaty residence (deemed expatriation) | `us-expatriation-exit-tax` |
| Withholding agents claiming treaty rates on payments (Forms W-8BEN, 1042-S) | Refer (R-TRT-WHT) |
| What a specific treaty article means for a specific income item | Read the treaty and the Treasury technical explanation; refer where unclear |

## Ask the client first

1. **Citizenship and residence status** in 2026 under US law (citizen, green card holder, substantial presence, nonresident), and where the person is resident under the other country's law.
2. **Which treaty and which article** the client wants to rely on, and the income item and amount (or a reasonable estimate).
3. **Whether the income was already reported** to the IRS on a Form W-2, 1099 or 1042-S, and whether the payer already applied the treaty rate.
4. **For an entity:** C corporation or not; related-party payments; limitation on benefits test relied on.
5. **Prior years:** has the client claimed the same position before without a Form 8833, and is the claim time-limited (student, teacher)?
6. **Long-term resident check:** has the person held a green card in at least 8 of the last 15 tax years? A treaty residence claim then counts as expatriation.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Penalty for failing to disclose a treaty-based return position, per failure | USD 1,000 | [26 U.S.C. 6712(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6712.htm) |
| Penalty per failure, C corporation | USD 10,000 | [26 U.S.C. 6712(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6712.htm) |
| Individual determining residence under a treaty: Form 8833 required when payments or income items total more than | USD 100,000 | [IRS Pub. 519 (2025), chapter 9](https://www.irs.gov/pub/irs-pdf/p519.pdf) |
| FDAP income from a related payor: reporting required when it exceeds, in the aggregate | USD 500,000 | [Form 8833 (Rev. December 2022), instructions](https://www.irs.gov/pub/irs-pdf/f8833.pdf) |
| Waiver for FDAP income properly reported on Form 1042-S to a taxpayer that is not an individual or a State: amounts not more than | USD 500,000 for the tax year | [Form 8833 (Rev. December 2022), instructions](https://www.irs.gov/pub/irs-pdf/f8833.pdf) |
| Long-term resident test (green card years) | 8 of the last 15 tax years | [Form 8833 (Rev. December 2022), instructions](https://www.irs.gov/pub/irs-pdf/f8833.pdf) |

None of these amounts is indexed for inflation. Treaty withholding rates differ by treaty and article: read the treaty.

### Step 1: is there a treaty-based return position?

1. A position exists when the taxpayer maintains that a treaty overrules or modifies a provision of the Code and that this causes, or potentially causes, a reduction of tax on the return. Source: [26 U.S.C. 6114(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapB-sec6114.htm); [Form 8833 instructions](https://www.irs.gov/pub/irs-pdf/f8833.pdf).
2. Treaties and the Code have equal standing; neither automatically prevails. Source: [26 U.S.C. 894(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec894.htm) (income affected by a treaty is subject to the treaty "with due regard to any treaty obligation").

### Step 2: does the saving clause stop the claim?

3. Most US treaties contain a saving clause: the United States keeps the right to tax its citizens and residents as if the treaty had not come into effect. A US citizen or resident alien generally cannot use the treaty to cut US tax. Source: [Pub. 519, chapter 9](https://www.irs.gov/pub/irs-pdf/p519.pdf).
4. Look for the exception list in the saving clause article. Typical exceptions: relief from double taxation (foreign tax credit article), some social security and pension articles, and the student, trainee, teacher and researcher articles for residents who are not green card holders. Example in Pub. 519: French social security benefits paid to a US resident are excepted by Article 29(3) of the US-France treaty. If no exception applies, stop: there is no treaty benefit to claim.

### Step 3: is reporting specifically required?

5. These positions must be reported on Form 8833 (Regulations section 301.6114-1(b), as listed in the Form 8833 instructions), subject to the waivers in Step 4:
   - a nondiscrimination article prevents an otherwise applicable Code provision;
   - a treaty reduces or modifies tax on gain or loss from disposing of a US real property interest;
   - a treaty reduces or modifies the branch profits tax or the tax on excess interest (section 884);
   - a treaty exempts or reduces tax on dividends or interest paid by a foreign corporation that are US-source;
   - FDAP income a foreign person receives from a US person, in the three cases the instructions list (not properly reported on Form 1042-S and the payee is a related foreign corporation; related payee with more than USD 500,000 and a limitation on benefits article; extra treaty conditions such as ownership period);
   - effectively connected income is not attributable to a US permanent establishment or fixed base, or a treaty modifies profits attributable to one;
   - a treaty alters the source of income or deduction (unless the taxpayer is an individual);
   - a treaty grants a credit for a foreign tax the Code does not allow;
   - an individual's residence is determined under a treaty and apart from the Code (the tie-breaker; for individuals, Pub. 519 states the requirement where payments or income items total more than USD 100,000).

### Step 4: is reporting waived?

6. Reporting is waived (Regulations section 301.6114-1(c), as listed in the Form 8833 instructions) for, among others:
   - a treaty that reduces or modifies tax on an individual's income from dependent personal services, pensions, annuities, social security and other public pensions, or income of artists, athletes, students, trainees or teachers;
   - a Social Security Totalization Agreement or Diplomatic or Consular Agreement;
   - a reduced rate or exemption on FDAP income where the beneficial owner is an individual or a governmental entity;
   - FDAP income properly reported on Form 1042-S in the listed cases (including a non-individual with not more than USD 500,000 for the year);
   - a partner or beneficiary whose partnership, trust or estate has already disclosed the position.
7. Pub. 519 adds, for individuals: no Form 8833 for a reduced withholding rate on interest, dividends, rent, royalties or other FDAP income, and none for Canadian or German social security benefits. A waiver does not apply to amounts the Form 8833 instructions specifically require to be reported.

### Step 5: complete and file Form 8833

8. One Form 8833 for each treaty-based return position, each year. Payments of the same type from the same payor can be treated as one item. Source: [Form 8833 instructions](https://www.irs.gov/pub/irs-pdf/f8833.pdf).
9. Line 1: treaty country and article(s). Line 2: the Code provision(s) overruled or modified. Line 3: the payor's name, identifying number and US address (for FDAP income). Line 4: the limitation on benefits test relied on (if the treaty has one). Line 5: whether reporting is specifically required, and which subsection. Line 6: the explanation, a short summary of facts, and the nature and amount (or a reasonable estimate) of each item.
10. Attach to the return (Form 1040, 1040-NR, 1120-F and so on). If no return is otherwise required, file one anyway to make the disclosure.
11. On Form 1040, exempt income already reported on a W-2, 1099 or 1042-S is entered in full on its normal line and backed out in parentheses on Schedule 1 (Form 1040) line 8z as "Exempt income", with the treaty country and article (Pub. 519 (2025); the 2026 line number is not yet confirmed).

### Step 6: dual residents

12. A dual-resident individual who uses the treaty tie-breaker to be resident in the other country is a nonresident alien for figuring US income tax for that part of the year and files Form 1040-NR with Form 8833 attached (Regulations section 301.7701(b)-7). The person is still a US resident for other purposes. A long-term resident who does this is treated as having expatriated (section 877A, Form 8854): stop and use `us-expatriation-exit-tax`.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| US citizen claims a treaty exemption on foreign pension or wages | Usually blocked by the saving clause; check the exceptions article |
| Resident alien (not green card holder) student keeps a student-article exemption | Allowed only if the saving clause excepts that article (for example US-China protocol paragraph 2); reporting is generally waived for students; report on Schedule 1 in parentheses |
| Nonresident alien gets a reduced treaty rate withheld on dividends | No Form 8833 (waived) |
| Individual claims treaty residence under the tie-breaker | Form 8833 with Form 1040-NR; check the long-term resident rule |
| Foreign person sells US real property and claims treaty relief | Form 8833 always required |
| Foreign tax credit for a tax the Code would not credit | Form 8833 required |
| C corporation fails to disclose | USD 10,000 per failure |
| Same position for several years | One Form 8833 each year |
| Treaty claim is time-limited (students 4 to 5 years, teachers 2 to 3 years usually) | Count the years; once past the limit the exemption ends (Pub. 519) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether a waiver applies | Treat the position as reportable and file Form 8833; a disclosure that was not needed costs nothing |
| Amount of the income item | Use a reasonable estimate on line 6 and say it is an estimate |
| Residence under foreign law | Ask; do not apply a tie-breaker without it |
| Green card history | Ask before any treaty residence claim |

## Worked cases

**Case 1, a decision: file Form 8833 or risk the penalty?** A dual-resident individual with USD 140,000 of income items decides residence under the treaty tie-breaker and, in the same year, claims relief on a US real property gain and a foreign tax credit the Code would not allow: three positions, each specifically reportable. A related C corporation in the group also has two specifically reportable positions (a branch profits tax reduction and a permanent establishment position). The income is above the USD 100,000 level in Pub. 519, so the residence position is reportable. Undisclosed, the exposure is 3 x USD 1,000 = USD 3,000 for the individual and 2 x USD 10,000 = USD 20,000 for the corporation, in addition to any other penalty. Decision: file five Forms 8833 (three and two); the cost is preparation time only.

```oa-check
name: Form 8833 penalty exposure, individual and C corporation (2026)
inputs:
  individual_positions: 3
  corporate_positions: 2
  penalty_individual: 1000
  penalty_c_corp: 10000
  income_items: 140000
  residence_threshold: 100000
steps:
  - individual_exposure: individual_positions * penalty_individual
  - corporate_exposure: corporate_positions * penalty_c_corp
  - total_exposure: individual_exposure + corporate_exposure
  - forms_to_file: individual_positions + corporate_positions
  - excess_over_threshold: max(income_items - residence_threshold, 0)
expected:
  individual_exposure: 3000.00
  corporate_exposure: 20000.00
  total_exposure: 23000.00
  forms_to_file: 5.00
  excess_over_threshold: 40000.00
```

**Case 2, a reduced treaty rate on dividends, no Form 8833.** A nonresident alien individual receives USD 10,000 of US-source portfolio dividends. Without a treaty, FDAP dividends of a nonresident alien are taxed at 30% (Pub. 519). Under the treaty with the client's country (assume its dividend article sets 15% for portfolio dividends: read the treaty), the tax is USD 1,500, a USD 1,500 saving. The beneficial owner is an individual and the rate was applied on Form 1042-S, so reporting is waived: no Form 8833.

```oa-check
name: Treaty reduced rate on portfolio dividends (2026)
inputs:
  dividends: 10000
  statutory_rate: 0.30
  treaty_rate: 0.15
steps:
  - tax_without_treaty: dividends * statutory_rate
  - tax_with_treaty: dividends * treaty_rate
  - saving: tax_without_treaty - tax_with_treaty
expected:
  tax_without_treaty: 3000.00
  tax_with_treaty: 1500.00
  saving: 1500.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-TRT-LTR | Long-term resident claiming treaty residence | Refer: deemed expatriation, `us-expatriation-exit-tax` |
| R-TRT-WHT | Withholding agent applying treaty rates on payments | Refer: Chapter 3 withholding and Form 1042-S are outside this skill |
| R-TRT-LOB | Entity must show it meets a limitation on benefits test | Refer: the test differs by treaty |
| R-TRT-CA | Double tax not resolved by the treaty; competent authority request | Refer (Rev. Proc. 2015-40 or its successor) |
| R-TRT-INTERP | Meaning of an article is unclear for the facts | Refer: read the treaty and technical explanation with a reviewer |
| R-TRT-ESTATE | Estate or gift tax treaty position | Refer: estate and gift returns are outside this skill |

## Filing and payment

Form 8833 is attached to the 2026 return: Form 1040 or 1040-NR due **15 April 2027**; Form 1120-F and other entity returns on their own due dates. Where no return is otherwise required, file a return at the IRS service center where it would normally be filed to make the disclosure (Form 8833 instructions). The penalty can be waived for reasonable cause and good faith (26 U.S.C. 6712(b)).

## Completion checklist

- Saving clause and its exceptions checked for citizens and residents.
- Each position tested against the specifically-required list and the waivers.
- One Form 8833 per position, lines 1 to 6 complete, amounts or estimates on line 6.
- Dual residents: Form 1040-NR used and long-term resident status checked.
- Exempt income already on an information return backed out on Schedule 1 with treaty country and article.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 6114 (govinfo). Read for (a) disclosure of the position that a treaty overrules or modifies a law, and (b) waiver authority. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapB-sec6114.htm | 2026-11-13 |
| 26 U.S.C. 6712 (govinfo). Read for (a) "$1,000 ($10,000 in the case of a C corporation) on each such failure", (b) reasonable cause waiver and (c) penalty in addition to others. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6712.htm | 2026-11-13 |
| 26 U.S.C. 894 (govinfo). Read for (a) income affected by treaty. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec894.htm | 2026-11-13 |
| Form 8833 (Rev. December 2022) with instructions. Read for the penalty line, who must file, positions specifically required under Regulations section 301.6114-1(b), waivers under 301.6114-1(c), the $500,000 amounts, dual-resident taxpayers, the 8 of 15 years long-term resident rule, and lines 1 to 6. | https://www.irs.gov/pub/irs-pdf/f8833.pdf | 2026-11-13 |
| IRS Pub. 519 (2025), chapter 9. Read for the saving clause and exceptions, the US-France and US-China examples, Schedule 1 line 8z reporting, time limits, the Form 8833 requirement list including the more than $100,000 residence case, the exceptions, and the $1,000 penalty. | https://www.irs.gov/pub/irs-pdf/p519.pdf | 2026-11-13 |

Not yet confirmed: no 2026 edition of Pub. 519 or 2026 Form 1040 Schedule 1 was published when read, so the Schedule 1 line for backed-out exempt income (line 8z in 2025) is not confirmed for 2026. Regulations section 301.6114-1 was read only as summarised in the Form 8833 instructions, not in the regulation text itself. The 15% treaty rate in Case 2 is an assumption for illustration, not a figure for any named treaty.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-tax-treaty-claims-8833` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-tax-treaty-claims-8833. If neither is available, confirm every figure against the official source pages cited above before relying on it.
