---
name: us-form-8865-foreign-partnership
description: "Decide whether a US person must file Form 8865 for a foreign partnership for tax year 2026, which of the four filer categories applies, which schedules that category requires, and the penalty for missing it. Covers control above 50 percent, the 10 percent Category 2 test, a section 721 contribution of property when the interest is at least 10 percent or the property exceeds USD 100,000, section 6046A reportable events, the constructive-owner and multiple-filer exceptions, and the USD 10,000 and 10 percent of value penalties. Does not prepare Form 1065 and does not compute section 721(c) gain deferral. Trigger on \"Form 8865\", \"foreign partnership\", \"controlled foreign partnership\", \"Category 1 filer\", \"section 6038B\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-form-8865-foreign-partnership"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US Form 8865, return for certain foreign partnerships, tax year 2026

> **Source-cited draft.** Built from the 2025 Instructions for Form 8865, the edition at irs.gov/instructions/i8865 when read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A US person files Form 8865 with the income tax return for the year, one form for each foreign partnership, if any of four categories applies. **Category 1** is control: more than a 50 percent interest at any time in the partnership's year. **Category 2** is a 10 percent or greater interest while US persons who each own at least 10 percent control the partnership, and only if nobody was a Category 1 filer that year. **Category 3** is a contribution of property for a partnership interest if, right after, the person owns at least 10 percent, or the property contributed by that person and related persons in the 12 months ending on the transfer exceeds **USD 100,000**. **Category 4** is a reportable acquisition, disposition, or change in a direct proportional interest under section 6046A. A missed Category 1 or 2 filing starts at **USD 10,000** per partnership per year. A missed Category 3 filing is **10 percent** of the property's fair market value, capped at **USD 100,000** unless the failure is intentional.

## Scope and who this is for

In scope: a US person (a citizen or resident, a domestic partnership, a domestic corporation, or an estate or trust that is not foreign) and an interest in a partnership that is not organized in the United States or under US or state law.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Preparing Form 1065 for a domestic partnership, or for a foreign partnership that files Form 1065 | `us-form-1065-partnership` |
| A controlled foreign corporation, Form 5471 | `us-form-5471-cfc-information` |
| A foreign-owned US corporation, Form 5472 | `us-form-5472-foreign-owned-us` |
| FBAR and Form 8938 thresholds | `us-fbar-and-fatca-8938` |
| Whether the foreign entity is a partnership or a corporation | `us-form-8832-entity-classification` |

`us-form-8832-entity-classification` is the classification skill. If that file is not in the pack yet, use Form 8832 and Treas. Reg. 301.7701-3 directly. Form 8865 follows the classification. It does not decide it.

## Ask the client first

1. **Who the US person is,** and whether the interest is owned directly or through another person, including a spouse, sibling, ancestor, or lineal descendant.
2. **The interest,** as a percent of capital, of profits, and of deductions or losses, at every point in the partnership's year. More than 50 percent of any one of those is control.
3. **Other US owners.** Did any US person control the partnership this year, and did US persons who each own at least 10 percent together control it?
4. **Contributions this year and in the prior 12 months,** with fair market value, by the person and by related persons, and the interest immediately after each contribution.
5. **Acquisitions, dispositions, and changes** in the direct interest, measured against the last reportable event (or against 31 December 1999 if the person owned at least 10 percent then and has had no reportable event since).
6. **Whether a return is otherwise required,** and its due date including extensions. Form 8865 rides on that return.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Who it applies to | Source |
| --- | --- | --- | --- |
| Category 1, control | More than a 50 percent interest | A 50 percent interest is 50 percent of capital, of profits, or of deductions or losses. Control is more than that. Exactly 50 percent is not control. Constructive ownership counts | [Instructions for Form 8865 (2025), Category 1 and 50 percent interest](https://www.irs.gov/instructions/i8865) |
| Category 2, minimum interest | 10 percent or greater | While the partnership is controlled by US persons each owning at least 10 percent. If anyone was a Category 1 filer during that partnership year, there is no Category 2 filer | [Instructions for Form 8865 (2025), Category 2](https://www.irs.gov/instructions/i8865) |
| Category 3, interest test | At least 10 percent immediately after the contribution | Direct or constructive. A contribution for a partnership interest (a section 721 transfer) | [Instructions for Form 8865 (2025), Category 3](https://www.irs.gov/instructions/i8865) |
| Category 3, value test | More than USD 100,000 | Property contributed by the person, plus property contributed by related persons, during the 12-month period ending on the transfer. Exactly USD 100,000 does not exceed the line | [Instructions for Form 8865 (2025), Category 3](https://www.irs.gov/instructions/i8865) |
| Category 4, reportable change | At least a 10 percent interest, direct | Crossing 10 percent, or a later increase or decrease of at least 10 percent of the partnership compared with the last reportable event | [Instructions for Form 8865 (2025), Category 4](https://www.irs.gov/instructions/i8865) |
| Category 1 and 2 initial penalty | USD 10,000 per foreign partnership per year | Failure to furnish the required information on time. Reasonable cause is in section 6038 | [Instructions for Form 8865 (2025), Penalties](https://www.irs.gov/instructions/i8865) |
| Category 1 and 2 continuation penalty | USD 10,000 per foreign partnership for each 30-day period, or part of a period, after the 90-day notice period, up to an extra USD 50,000 | Starts only after the IRS mails a notice and 90 days pass with the failure still open | [Instructions for Form 8865 (2025), Penalties](https://www.irs.gov/instructions/i8865) |
| Foreign tax credit reduction, Category 1 and 2 | 10 percent of the foreign taxes available for credit under sections 901 and 960, plus a further 5 percent for each 3-month period, or part, after the 90-day notice | The instructions point to section 6038 for the maximum reduction | [Instructions for Form 8865 (2025), Penalties](https://www.irs.gov/instructions/i8865) |
| Category 3 penalty | 10 percent of the fair market value of the property at the time of the contribution, not over USD 100,000 | The cap does not apply if the failure is due to intentional disregard. The transferor also recognizes gain as if the property had been sold for fair market value | [Instructions for Form 8865 (2025), Penalties](https://www.irs.gov/instructions/i8865) |
| Category 4 initial penalty | USD 10,000 | Failure to report the information section 6046A requires, unless reasonable cause. A section 7203 criminal penalty may also apply | [Instructions for Form 8865 (2025), Penalties](https://www.irs.gov/instructions/i8865) |
| Category 4 continuation penalty | USD 10,000 for each 30-day period, or part, after the 90-day notice period, up to an extra USD 50,000 | Same notice rule as Category 1 and 2 | [Instructions for Form 8865 (2025), Penalties](https://www.irs.gov/instructions/i8865) |

The instructions state these dollar amounts as fixed figures. They are not described there as indexed for 2026.

### Which category, then which schedules

1. **One form per foreign partnership.** A person in more than one category for that partnership files every schedule each of those categories requires. Source: [Instructions for Form 8865 (2025), Who Must File](https://www.irs.gov/instructions/i8865).
2. **Category 1.** More than 50 percent of capital, or of profits, or of deductions or losses, at any time during the partnership's tax year. There can be more than one Category 1 filer. A US transferor who must report a section 721(c) partnership is also a Category 1 filer for that reporting, satisfied by Schedule G and, in some cases, Schedule H. Section 721(c) gain deferral is not computed in this skill.
3. **Category 2.** At least 10 percent, and the partnership is controlled by US persons who each own at least 10 percent. Drop Category 2 entirely if any Category 1 filer existed during that partnership year.
4. **Category 3.** A contribution of property for an interest this year, if either the 10 percent test or the USD 100,000 test is met. Either one is enough. If a domestic partnership contributes and files a complete Form 8865 for the contribution, its partners do not also report that transfer. A later disposition of previously reported appreciated property, while the US person is still a partner, is also Category 3.
5. **Category 4.** Three reportable events, all measured on the direct interest. An acquisition that moves the person to 10 percent or more, or that increases the direct interest by at least 10 percent since the last reportable event. A disposition that drops the person below 10 percent, or that decreases the direct interest by at least 10 percent since the last reportable event. Any other change in the direct proportional interest of at least 10 percent since the last reportable event, including a change caused by another partner's withdrawal or by the partnership agreement. A person who owned at least 10 percent on 31 December 1999 measures the first later event from that date.
6. **Constructive ownership** for the 10 percent and 50 percent tests uses section 267(c), other than section 267(c)(3). An interest owned by a corporation, partnership, estate, or trust is treated as owned proportionately by its owners. An individual is treated as owning an interest owned by a spouse, sibling, ancestor, or lineal descendant. An interest owned by a nonresident alien is attributed under the family rule only if the person to whom it would be attributed already owns a direct or indirect interest under section 267(c)(1) or (5).
7. **Schedules.** Use the filing-requirements chart in the instructions rather than a shortened list. The instructions' own example of a person who is both Category 2 and Category 3: file what Category 2 requires (page 1, Schedules A, A-2, N, K-1, and K-3) plus what Category 3 adds (Schedules A-1 and O). Category 4 adds Schedule P, unless the Category 3 overlap exception below applies. A separate form is filed for each foreign partnership.
8. **If the foreign partnership files Form 1065,** a Category 1 filer may attach the partnership's Form 1065 schedules in place of the matching Form 8865 schedules, and still completes Form 8865 pages 1 and 2 and Schedules A, A-1, A-2, A-3, G, H, M, and N. A Category 2 filer may attach the Schedules K-1 and K-3 received from the partnership instead of Form 8865 Schedules K-1 and K-3, and still completes pages 1 and 2 and Schedules A, A-2, and N. Source: [Instructions for Form 8865 (2025), Relief when the foreign partnership files Form 1065](https://www.irs.gov/instructions/i8865).

### Exceptions that remove a filing, not the penalty if the exception is done wrong

9. **Several Category 1 filers.** Only one files Form 8865. It must contain everything each of them would have filed, including a separate Schedule N, K-1, and K-3 for each. A person with a controlling interest in losses or deductions cannot be the one filer if another US person has a controlling interest in capital or profits. Each person who does not file attaches a "Controlled Foreign Partnership Reporting" statement to that person's own return. A person who also has a Category 3 or Category 4 duty still files a separate Form 8865 for that duty. If the chosen filer files an incomplete form, the others can still be penalized.
10. **Constructive owners with no direct interest.** A Category 1 or 2 filer who owns only constructively, through a US person, does not file Form 8865 if that US person files, or if another Category 1 filer files under the multiple-filer exception. The indirect partner still attaches the "Controlled Foreign Partnership Reporting" statement.
11. **Category 3 reported, so Category 4 is not repeated.** A contribution that is both Category 3 and Category 4 is reported once, under Category 3, if that reporting is proper. The acquisition still counts as the last reportable event for a later Category 4 test.
12. **Other exceptions read in the instructions.** Trusts for state and local government employee retirement plans do not file. The common parent of a consolidated group may file one Form 8865 for the group members who are Category 1 or 2 filers.

### How a failure is priced

The initial Category 1 or 2 penalty is USD 10,000 for that partnership for that year. The continuation penalty does not start until the IRS mails a notice and 90 days pass. After that, each 30 days or part of 30 days adds USD 10,000, and the extra amount stops at USD 50,000. The foreign tax credit haircut is separate from that dollar penalty. Category 3 is 10 percent of fair market value, stopped at USD 100,000 unless the miss is intentional, and the contribution is taxed as a sale at fair market value. Category 4 uses the same USD 10,000 and continuation structure as Category 1, with its own cap of an extra USD 50,000.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Exactly 50 percent of capital, profits, and deductions or losses | Not Category 1. Category 2 is still possible |
| More than 50 percent of only one of capital, profits, or deductions or losses | Category 1 |
| A Category 1 filer exists for that partnership year | No Category 2 filer, including people who would otherwise be over 10 percent |
| Contribution, 8 percent after, property USD 100,000 exactly | Not Category 3 on either test. The value test is "exceeds" |
| Contribution, 8 percent after, property USD 100,001 | Category 3 on the value test |
| Contribution, exactly 10 percent after, property USD 1 | Category 3 on the interest test |
| Contribution that is both Category 3 and Category 4, reported properly as Category 3 | Do not also report it as Category 4. It is still the baseline for the next Category 4 change |
| From 9 percent direct to 10 percent direct | Category 4 acquisition |
| From 11 percent to 21 percent since the last reportable event | Category 4 acquisition |
| Only a constructive interest, and the US person underneath files a complete Form 8865 | No Form 8865 from the indirect owner. The statement is still required |
| Domestic partnership files a complete Form 8865 for its own contribution | Its partners do not also file Category 3 for their shares of that contribution |
| Foreign partnership files Form 1065 | Substitute the listed schedules only. Form 8865 itself is still filed |
| Section 721(c) property and the gain deferral method | Schedules G and H may be required. Do not compute the gain here |

## Worked cases

**Case 1, a decision: is the contribution Category 3?** A US individual transfers property to a foreign partnership. Two possibilities. First, the property is worth USD 80,000 and the person owns 8 percent immediately after. That is under 10 percent, and USD 80,000 does not exceed USD 100,000. There is no Category 3 filing and no section 6038B penalty for this transfer. Second, the property is worth USD 120,000 and the person still owns 8 percent after. The interest test fails and the value test is met, because USD 120,000 exceeds USD 100,000. Category 3 applies. If it is not reported, the penalty is 10 percent of USD 120,000, which is USD 12,000, and the USD 100,000 cap does not reduce it. The contribution is also taxed as a sale at USD 120,000. The gain depends on basis, which this case does not have, so the gain is not computed here. The decision figure is the penalty: USD 0 if both tests fail, USD 12,000 if the value test is the one that is met.

```oa-check
name: Category 3 value test, under the line against over the line (2026)
inputs:
  fmv_under: 80000
  fmv_over: 120000
  value_line: 100000
  penalty_rate: 0.10
  penalty_cap: 100000
steps:
  - room_under_the_line: max(value_line - fmv_under, 0)
  - room_over_the_line: max(value_line - fmv_over, 0)
  - penalty_if_under: 0
  - penalty_if_over: min(fmv_over * penalty_rate, penalty_cap)
expected:
  room_under_the_line: 20000.00
  room_over_the_line: 0.00
  penalty_if_under: 0.00
  penalty_if_over: 12000.00
```

**Case 2, Category 1 continuation penalty.** A US person owns 60 percent of the capital of a foreign partnership for all of the partnership's 2026 year. That is Category 1. No Form 8865 is filed. The IRS mails a notice. The failure is still open 90 days after the notice, and for 120 days after that 90th day. One hundred and twenty days is four 30-day periods. The initial penalty is USD 10,000. The continuation penalty is USD 10,000 times 4, which is USD 40,000, and that is under the extra USD 50,000 cap, so the cap does not cut it. The dollar penalties total USD 50,000. The separate 10 percent reduction of foreign tax credit is not in this total.

```oa-check
name: Category 1 penalty after notice, four continuation periods (2026)
inputs:
  initial: 10000
  per_period: 10000
  periods: 4
  extra_cap: 50000
steps:
  - continuation: min(per_period * periods, extra_cap)
  - total_penalty: initial + continuation
expected:
  continuation: 40000.00
  total_penalty: 50000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-8865-CLASS | It is not clear the entity is a partnership | Classify it first. A per se corporation is not a partnership |
| R-8865-721C | Section 721(c) property, gain deferral, or an acceleration event | Schedules G and H. Refer. Do not compute the deferred gain here |
| R-8865-CONST | Ownership runs through several entities or through family, including a nonresident alien | Build the section 267(c) chart before deciding the percent. A wrong percent picks the wrong category |
| R-8865-1065 | The foreign partnership files Form 1065 | Use only the schedule substitution the instructions allow. The Form 8865 is still required |
| R-8865-FBAR | The question is an FBAR or Form 8938 | `us-fbar-and-fatca-8938`. A Form 8865 duty does not replace those, and they do not replace Form 8865 |
| R-8865-CRIM | The return was left off on purpose, or the facts given to the IRS were false | Sections 7203, 7206, and 7207 are named in the instructions. Refer |

## Filing and payment

Attach Form 8865 to the filer's income tax return, or to the partnership or exempt-organization return if that is the return the person files, and file both by that return's due date, including extensions. If the person has no return to file, file Form 8865 at the time and place that return would have been filed. There is no separate tax on Form 8865. The penalty above is not a tax shown on the form. It is assessed for a miss.

The 2025 instructions say to file the 2025 form with the return for a tax year beginning in 2025. The 2026 form had not replaced that page when this skill was written. Use the form for the year being filed once the IRS posts it, and keep the category tests above unless that form's instructions change them.

A copy of Form 8832 is attached to the same return when the instructions for Form 8832 require it.

## Completion checklist

- Each foreign partnership tested separately for Categories 1, 2, 3, and 4.
- Percents measured on capital, profits, and deductions or losses, with constructive ownership applied.
- Category 2 switched off if any Category 1 filer existed that year.
- Contributions tested twice: interest right after, and 12-month value including related persons. Exactly USD 100,000 does not meet the value test.
- Category 4 measured from the last reportable event, not from zero, except the 31 December 1999 starting rule.
- A multiple-filer or constructive-owner exception used only with the required statement, and not used to skip a Category 3 or 4 duty.
- Schedules taken from the instructions' chart for every category that applies.
- Form 1065 schedules substituted only where the instructions allow it.
- Form 8865 attached to the return and filed by that return's due date, including extensions.
- Penalty quoted from the category that was missed, including the notice timing before any continuation amount.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form 8865 (2025). Read for the four categories, the 50 percent and 10 percent definitions, the USD 100,000 contribution test, constructive ownership, the filing-requirements example (Category 2 plus Category 3), the exceptions, the Form 1065 schedule substitution, when and where to file, and the penalty amounts. | https://www.irs.gov/instructions/i8865 | 2026-11-13 |

Not yet confirmed: the 2026 Form 8865 and its instructions were not the edition at this URL when read, so 2026 form line numbers are not stated. The maximum reduction of the foreign tax credit under section 6038, beyond the 10 percent and the further 5 percent the instructions state, was not opened in the statute. The section 6662(j) understatement penalty for an undisclosed foreign financial asset is named in the instructions and was not computed.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-form-8865-foreign-partnership` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-form-8865-foreign-partnership. If neither is available, confirm every figure against the official source pages cited above before relying on it.
