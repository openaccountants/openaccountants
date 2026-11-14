---
name: us-form-8832-entity-classification
description: >
  Decide the federal tax classification of an eligible entity and file Form
  8832 when the default is not the one the owners want. Covers domestic and
  foreign default rules, the 75-day retroactive and 12-month prospective
  window, the 60-month limit on a second change, late relief under Rev. Proc.
  2009-41 (3 years and 75 days), and the deemed transactions when a
  classification changes. A per se corporation cannot elect. A timely S
  election is not filed on this form. Trigger on "Form 8832", "check the box",
  "entity classification", "disregarded entity", "eligible entity", "late
  classification relief". Tax year 2026. Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
category: formation
type: decision
---

# US Form 8832, entity classification election, tax year 2026

> **Source-cited draft.** Built from Form 8832 (Rev. December 2013, including the mailing-address update printed on that PDF), Treas. Reg. 301.7701-3 on eCFR, Rev. Proc. 2009-41, and 26 U.S.C. 11(b), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Do not file Form 8832 if the default is already the classification the owners want. A domestic eligible entity with two or more owners defaults to a **partnership**. A domestic eligible entity with one owner defaults to **disregarded**. A foreign eligible entity defaults to a **corporation** when every owner has limited liability. An election can take effect no more than **75 days** before the filing date and no more than **12 months** after it. Late relief under Rev. Proc. 2009-41 is open for **3 years and 75 days** after the requested effective date, and only if the other conditions in that procedure are met. A second change is generally locked for **60 months**.

## Scope and who this is for

In scope: whether an eligible business entity is a partnership, a corporation (association), or disregarded for federal tax, and how to make or correct that choice on Form 8832.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether the owners should elect S status, Form 2553, and reasonable compensation | `us-s-corp-election-decision` |
| Preparing Form 1120 after an association election | `us-form-1120-c-corp` |
| Preparing Form 1065 for a default partnership | `us-form-1065-partnership` |
| A disregarded owner's Schedule C | `us-schedule-c-and-se-computation` |
| State filing of the LLC or corporation | the state's formation skill |

## Ask the client first

1. **Where it is organized,** and whether that statute calls it a corporation, a joint-stock company, an insurance company, or a bank with insured deposits. Those are corporations. They do not file Form 8832.
2. **How many owners,** and, if it is foreign, whether any owner has personal liability for the entity's debts under the statute of organization (an indemnity from someone else does not count).
3. **The classification they want,** and whether they also want S status. A timely Form 2553 is the corporate election for an eligible entity that qualifies. That path is `us-s-corp-election-decision`. Do not also file Form 8832 for the same initial choice.
4. **The requested effective date and the day Form 8832 will be signed.** Count the days. More than 75 days before the filing date, or more than 12 months after it, does not stick as written.
5. **Any earlier Form 8832.** The effective date of the last election to change classification, and whether more than half the owners now are people who owned nothing then.
6. **If the form is late:** whether every return so far matches the classification they wanted, and the reason it was not filed on time.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Who it applies to | Source |
| --- | --- | --- | --- |
| Retroactive effective date | No more than 75 days before the date Form 8832 is filed | An eligible entity specifying an effective date. A date further back takes effect 75 days before filing, not on the date written | [Treas. Reg. 301.7701-3(c)(1)(iii)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/part-301/subpart-Definitions/subject-group-ECFR6f8c3724b50e44d/section-301.7701-3) |
| Prospective effective date | No more than 12 months after the date Form 8832 is filed | Same election. A later date written on the form takes effect 12 months after filing | [Form 8832, line 8 instructions](https://www.irs.gov/pub/irs-pdf/f8832.pdf) |
| Late classification relief window | 3 years and 75 days from the requested effective date | Relief under Rev. Proc. 2009-41, and only if the failure was solely a late Form 8832, returns are consistent (or the first return is not yet due), and there is reasonable cause | [Form 8832, Late Election Relief](https://www.irs.gov/pub/irs-pdf/f8832.pdf) |
| Limit on a second change | 60 months after the effective date of an election to change classification | Does not apply to an initial election by a newly formed entity that is effective on the date of formation. The IRS may allow an earlier change, by private letter ruling, if more than 50 percent of the interests are owned by persons who owned nothing on the filing date or the effective date of the prior election | [Treas. Reg. 301.7701-3(c)(1)(iv)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/part-301/subpart-Definitions/subject-group-ECFR6f8c3724b50e44d/section-301.7701-3) |
| IRS notice of acceptance | Generally within 60 days after filing | If no notice arrives, call 1-800-829-0115 or write the service center | [Form 8832, Acceptance or Nonacceptance](https://www.irs.gov/pub/irs-pdf/f8832.pdf) |
| Entity-level tax if the election is association and no S election is made | 21 percent of taxable income | Section 11(b). A default partnership or a disregarded entity does not pay this tax. The owners' own tax is not computed here | [26 U.S.C. 11(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm) |

The 75 days, 12 months, 60 months, and 3 years and 75 days are not indexed.

### Default, then the election

1. **Stop if it is not an eligible entity.** A business entity is a corporation, and cannot elect, if it is incorporated under a federal, state, or tribal statute, a joint-stock company, an insurance company, a state-chartered bank with federally insured deposits, an entity wholly owned by a state or a foreign government, an entity that is a corporation under a Code section other than 7701(a)(3), a foreign entity on the per se list, or an entity with charters in more than one jurisdiction that is a corporation in any of them. Source: [Form 8832, Definitions, Corporation](https://www.irs.gov/pub/irs-pdf/f8832.pdf).
2. **Domestic default,** if no election is filed. Two or more owners: partnership (Form 1065). One owner: disregarded. The activity then goes on the owner's return. Source: [Treas. Reg. 301.7701-3(b)(1)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/part-301/subpart-Definitions/subject-group-ECFR6f8c3724b50e44d/section-301.7701-3).
3. **Foreign default,** if no election is filed. Two or more owners and at least one has no limited liability: partnership. Every owner has limited liability: association, taxed as a corporation. One owner who has no limited liability: disregarded. Limited liability is decided only under the statute of organization (and the organizational documents, if that statute lets the entity choose). An indemnity does not create personal liability. Source: [Treas. Reg. 301.7701-3(b)(2)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/part-301/subpart-Definitions/subject-group-ECFR6f8c3724b50e44d/section-301.7701-3).
4. **File Form 8832 only to leave the default, or to change a classification already in place.** Do not file it to keep the default. A timely Form 2553 by an eligible entity that qualifies as an S corporation is treated as the association election. Do not file Form 8832 for that initial step. Source: [Form 8832, Who Must File](https://www.irs.gov/pub/irs-pdf/f8832.pdf) and [Treas. Reg. 301.7701-3(c)(1)(v)(C)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/part-301/subpart-Definitions/subject-group-ECFR6f8c3724b50e44d/section-301.7701-3).
5. **Line 8 is the effective date,** or the filing date if line 8 is blank. Outside the 75-day / 12-month window, the date snaps to the edge of the window. It does not fail silently and it does not use the date the owners wrote. Source: [Form 8832, line 8](https://www.irs.gov/pub/irs-pdf/f8832.pdf).
6. **A change, unlike the first election of a new entity, starts the 60-month lock.** An election effective on the formation date of a newly formed entity is not a change. A change in the number of owners does not reset the 60 months, and it does not by itself change an association into a partnership or a disregarded entity. A partnership becomes disregarded when it drops to one owner, and a disregarded entity becomes a partnership when it gains a second owner, without Form 8832. Source: [Treas. Reg. 301.7701-3(c)(1)(iv) and (f)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/part-301/subpart-Definitions/subject-group-ECFR6f8c3724b50e44d/section-301.7701-3).
7. **A change has deemed transactions.** Partnership to association: the partnership contributes its assets and liabilities for stock, then liquidates. Association to partnership: the association liquidates, then the owners contribute the assets to a new partnership. Association to disregarded: the association liquidates to the single owner. Disregarded to association: the owner contributes the assets and liabilities for stock. These can be taxable. Read Treas. Reg. 301.7701-3(g) before filing a change. Source: [Form 8832, Effect of Election](https://www.irs.gov/pub/irs-pdf/f8832.pdf).

### Late relief

8. **Rev. Proc. 2009-41** can put the effective date back to the requested date if all four of these are true. The miss was only that Form 8832 was late. Either the first return is not yet due, or every required return was filed on time (or within 6 months after its due date, ignoring extensions) consistent with the requested classification, and no inconsistent return was filed. The entity has reasonable cause. And 3 years and 75 days from the requested effective date have not passed. For a change in classification, consistent filing includes returns that follow the deemed transactions in Treas. Reg. 301.7701-3(g). Check the late-relief box, complete Part II, and explain the reason on line 11. Part II is signed by an authorized person and by each affected person, someone with personal knowledge. User fees do not apply to relief under this revenue procedure. If the conditions are not met, the remaining route is a private letter ruling. Source: [Rev. Proc. 2009-41, sections 3.01 and 4](https://www.irs.gov/pub/irs-drop/rp-09-41.pdf).

### How the result is used

The accepted election sets which return the entity files: Form 1120 (`us-form-1120-c-corp`), Form 1120-S after a separate S election (`us-s-corp-election-decision`), Form 1065 (`us-form-1065-partnership`), or the owner's return (`us-schedule-c-and-se-computation`). Attach a copy of Form 8832 to the return for the year of the election. Do not sign that copy. If the entity files no return, the owners attach the copy. Failure to attach the copy does not undo a valid election. Each owner files consistently with the election.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Domestic two-owner LLC, no form filed | Partnership. Do not file Form 8832 |
| Domestic one-owner LLC, no form filed | Disregarded. Still separate for employment tax on wages paid on or after 1 January 2009, and for the listed excise taxes after 31 December 2007 |
| Foreign entity, every owner has limited liability, no form filed | Association, taxed as a corporation. Form 8832 is required to be a partnership or, for one such owner, disregarded |
| Foreign entity, one owner, that owner has no limited liability, no form filed | Disregarded |
| Entity on the per se list | Corporation. Form 8832 is not available. Confirm the name against the current regulation, not only the 2013 form |
| Timely Form 2553 and the entity qualifies | Deemed association election. Do not also file Form 8832 for that initial classification |
| Line 8 is more than 75 days before filing | Effective 75 days before the filing date |
| Line 8 is more than 12 months after filing | Effective 12 months after the filing date |
| Prior change still inside 60 months, and the new owners are not more than half | Do not file another change. A private letter ruling is the exception the regulation names |
| Election effective before 1 January 1997 | The regulation makes it effective 1 January 1997 |
| Classification change | Run the deemed contribution or liquidation in Treas. Reg. 301.7701-3(g) before treating the change as tax-free |

## Worked cases

**Case 1, a decision: leave the domestic default, or elect a corporation.** A domestic LLC with two owners has USD 100,000 of taxable income for 2026. Nobody files Form 8832. The default is a partnership. The entity does not pay the section 11 tax. The USD 100,000 passes through, and the owners' tax is computed on their own returns (`us-form-1065-partnership` and the individual skill). The same LLC files Form 8832 to be an association and does not make an S election. It files Form 1120. Entity-level tax is USD 100,000 times 21 percent, which is USD 21,000. The decision figure this skill owns is that USD 21,000. It is not a comparison with the owners' individual brackets, and it is not a reason by itself to elect. An S election, if they want pass-through after corporate classification, is a separate form and a separate decision.

```oa-check
name: Domestic two-owner LLC, default partnership against an association election (2026)
inputs:
  taxable_income: 100000
  corporate_rate: 0.21
steps:
  - entity_tax_if_default_partnership: 0
  - entity_tax_if_association: taxable_income * corporate_rate
  - extra_entity_tax: entity_tax_if_association - entity_tax_if_default_partnership
expected:
  entity_tax_if_default_partnership: 0.00
  entity_tax_if_association: 21000.00
  extra_entity_tax: 21000.00
```

**Case 2, a decision: the 75-day snap, or late relief.** The owners want the election effective 1 January 2026. They file Form 8832 on 1 June 2026, which is 151 days after 1 January. The ordinary rule allows only 75 days back, so the date on line 8 does not stick. The election takes effect on 18 March 2026, which is 75 days before 1 June. Late relief is a different route. Three years and 75 days from 1 January 2026 ends on 17 March 2029, 1,171 days after 1 January 2026. On 1 June 2026, 1,020 of those days are left, so the window is still open, but only if the miss was solely the late form, the returns are consistent or not yet due, and there is reasonable cause. A filing on 1 April 2029 is 1,186 days after 1 January 2026. That is past 1,171, so Rev. Proc. 2009-41 is closed. The figure that decides is whether the filing day is inside 1,171 days of the requested effective date.

```oa-check
name: 75-day snap against the 3-year-and-75-day relief window (2026)
inputs:
  days_to_june_1: 151
  ordinary_limit: 75
  relief_limit: 1171
  days_to_april_1_2029: 1186
steps:
  - days_past_ordinary_window: days_to_june_1 - ordinary_limit
  - relief_days_left_on_june_1: relief_limit - days_to_june_1
  - relief_days_left_on_april_1_2029: max(relief_limit - days_to_april_1_2029, 0)
expected:
  days_past_ordinary_window: 76.00
  relief_days_left_on_june_1: 1020.00
  relief_days_left_on_april_1_2029: 0.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-8832-PERSE | The name is on the foreign per se list, or the statute calls it a corporation | Do not file Form 8832. Confirm the current list in Treas. Reg. 301.7701-2(b)(8) |
| R-8832-S | They want S status | `us-s-corp-election-decision`. Form 2553, if timely and the entity qualifies, is the association election |
| R-8832-CHANGE | A classification change, not the first election of a new entity | Compute the deemed liquidation or contribution before filing. Refer if gain is likely |
| R-8832-LOCK | A change took effect less than 60 months ago and new owners are not more than half | Do not file. A private letter ruling is the route the regulation names |
| R-8832-LATE | The 75-day window is missed and relief is doubtful | Do not assume the requested date. Relief needs every condition, including reasonable cause |
| R-8832-SERIES | A series LLC, or a tier of disregarded entities | Identify the first owner that is not disregarded. Series classification was not read for this skill |

## Filing and payment

Form 8832 has no tax of its own. The tax, if any, is on the return the classification requires, and that return's due date is in that return's skill.

The entity needs its own EIN before filing. Do not write "Applied For". Do not apply for a new EIN if it already has one. A foreign person who is the single owner and has no US identifying number enters "none" on line 4b.

Signers: each owner at the time of filing, or one officer, manager, or member authorized to elect. If the effective date is before the filing date, every person who was an owner in between, and who is not an owner now, also signs.

File the original at the address in the update printed at the front of the current Form 8832 PDF (the December 2013 form's later address table is not the one that update tells filers to use):

| Principal business, office, or agency | Address |
| --- | --- |
| Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Vermont, Virginia, West Virginia, Wisconsin | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999 |
| Alabama, Alaska, Arizona, Arkansas, California, Colorado, Florida, Hawaii, Idaho, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Mexico, North Dakota, Oklahoma, Oregon, South Dakota, Tennessee, Texas, Utah, Washington, Wyoming | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201 |
| A foreign country or a US possession | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0023 |

Attach an unsigned copy to the entity's federal tax or information return for the year of the election. If the entity files no return for that year, the direct or indirect owners attach the copy, unless an entity between them and this one is already attaching it.

The service center generally answers within 60 days. Keep a certified or registered mail receipt, a stamped received copy, or the IRS acceptance letter.

## Completion checklist

- The entity is eligible. It is not a per se corporation and not incorporated by statute.
- The default was written down, and Form 8832 is being filed only because the default is not the wanted classification.
- Domestic or foreign default used the right owner count, and foreign limited liability was read from the organizing statute.
- Line 8 is inside 75 days before filing and 12 months after it, or the snap date was the one used.
- The 60-month lock was checked before a second change.
- Deemed liquidation or contribution was considered before a change was signed.
- EIN is on the form. No "Applied For".
- Late relief, if claimed, meets all four Rev. Proc. 2009-41 conditions, and Part II is signed by each affected person.
- An unsigned copy will go on the year's return.
- S status, if wanted, is on Form 2553, not doubled on this form.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Form 8832 (Rev. December 2013), including the mailing-address update at the front of the PDF. Read for the default rules, who must file, the 75-day and 12-month window, the 60-month limit, late relief under Rev. Proc. 2009-41, the deemed transactions, the EIN rule, the 60-day acceptance notice, and the updated Kansas City and Ogden addresses. | https://www.irs.gov/pub/irs-pdf/f8832.pdf | 2026-11-13 |
| Treas. Reg. 301.7701-3 (eCFR). Read for the domestic and foreign defaults, the definition of limited liability, the effective-date window, the 60-month limitation, the deemed S election, and the effect of a change in the number of members. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/part-301/subpart-Definitions/subject-group-ECFR6f8c3724b50e44d/section-301.7701-3 | 2026-11-13 |
| Rev. Proc. 2009-41. Read for section 4.01 (the four conditions, including consistent returns and the deemed-transaction returns on a change), section 3.01 (user fees do not apply to this relief), and the 3-year-and-75-day filing period. | https://www.irs.gov/pub/irs-drop/rp-09-41.pdf | 2026-11-13 |
| 26 U.S.C. 11(b). Read for the 21 percent rate used as the entity-level tax if the election is association and no S election is made. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm | 2026-11-13 |

Not yet confirmed: a country-by-country copy of the current per se list in Treas. Reg. 301.7701-2(b)(8). The December 2013 form prints a list and says the regulation controls later revisions, and that regulation was not opened as its own page. The current private-letter-ruling user fee, for a late election that does not meet Rev. Proc. 2009-41, was not opened. User fees do not apply to relief that does meet that procedure. The dollar amount of a penalty for a return inconsistent with the election was not opened. The form says penalties may be assessed and does not state the amount.
