---
name: au-lodgment-deadlines-penalties
description: >
  Use this skill for Australian lodgment and payment deadlines, and for what happens when one is
  missed: failure to lodge on time penalties, shortfall and false or misleading statement
  penalties, general interest charge, shortfall interest charge, remission, safe harbour for
  registered agent clients, and the correction pathways (later BAS, revised activity statement,
  amendment, objection). Trigger on phrases like "when is my tax return due", "BAS due date",
  "late lodgment penalty", "failure to lodge", "FTL penalty", "penalty units", "general interest
  charge", "GIC rate", "shortfall interest charge", "remission of interest", "ATO payment plan",
  "how long do I have to amend", "period of review", "voluntary disclosure", "tax agent lodgment
  program". Covers federal obligations administered by the ATO only.
version: 0.1
jurisdiction: AU
tax_year: 2026
last_updated: 2026-09-17
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Lodgment Deadlines, Penalties and Interest

## Australia Lodgment Deadlines, Penalties and Interest v0.1

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## What this file is

**Obligation category:** Administration
**Functional role:** Deadline, penalty and interest reference across every ATO-administered role
**Status:** Source-cited draft, pending accountant review

Due dates in Australia are not a fixed calendar. The same obligation has different dates for a
self-lodger and for a registered agent's client, and an agent's date depends on the client's
category and on whether prior year returns were lodged on time. Treat every date below as the
starting point for a check against the taxpayer's own ATO record, not as the answer.

This file covers federal obligations administered by the ATO. State and territory obligations,
including payroll tax, land tax and duties, have their own deadlines and penalty regimes set by
each revenue office. See `au-land-tax.md` and `au-stamp-duty.md`.

## Section 1 - Scope statement

This skill covers:

- Lodgment and payment due dates for the main ATO obligations of a 30 June balancing entity.
- The difference between a statutory due date, a concession attached to electronic lodgment, and
  a registered agent lodgment program date.
- Deferrals and disaster support.
- Failure to lodge on time penalty, including the penalty unit amount and the entity size
  multipliers.
- Shortfall and false or misleading statement penalties, and the reductions for voluntary
  disclosure.
- General interest charge and shortfall interest charge, including the deductibility change.
- Remission of penalties and interest, penalty relief, and agent safe harbour.
- Which correction pathway applies: later BAS, revised activity statement, amendment or objection.

This skill does NOT cover:

- The substantive computation of any tax. See the domain guide for that tax.
- The BAS preparation workflow. See `au-bas-preparation.md`.
- Superannuation guarantee charge deadlines and the payday super regime. See
  `au-super-guarantee.md`.
- State and territory taxes.
- Director penalty notices, garnishee notices and departure prohibition orders beyond the summary
  in Section 9. These are debt recovery actions requiring specific advice.

## Section 2 - Establish the facts before you quote a date

**Facts that change the date**

| Fact | Why it changes the date |
| --- | --- |
| Is the taxpayer lodging through a registered tax or BAS agent | Agent clients receive lodgment program dates that self-lodgers do not |
| Were prior year returns lodged on time | An overdue prior year return generally pulls the current date forward to 31 October |
| Entity type, and taxable or non-taxable in the last year lodged | Company, trust and not-for-profit dates differ from individual dates |
| Balance date | A substituted accounting period changes every income tax date |
| Which roles are registered | GST, PAYG withholding, PAYG instalments, FBT and others each have their own cycle |
| Withholder size for PAYG withholding | Determines whether withheld amounts are remitted quarterly, monthly or more often |
| Is the taxpayer in a declared disaster area | Concessional deferrals may apply automatically |

## Section 3 - Activity statement deadlines

**Activity statement deadlines**  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas); [ATO, When are PAYG instalments due](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due))_

| Obligation | Due date | Notes |
| --- | --- | --- |
| Monthly activity statement | 21st of the following month | No electronic lodgment concession |
| Quarterly BAS, quarter 1 (Jul to Sep) | 28 October | An extra 2 weeks may apply if lodged online |
| Quarterly BAS, quarter 2 (Oct to Dec) | 28 February | No further extension, the date already includes one month |
| Quarterly BAS, quarter 3 (Jan to Mar) | 28 April | An extra 2 weeks may apply if lodged online |
| Quarterly BAS, quarter 4 (Apr to Jun) | 28 July | An extra 2 weeks may apply if lodged online |
| Quarterly PAYG instalment | Same dates as the quarterly BAS | Monthly instalments apply where instalment income exceeds $20 million |

- **Weekend or public holiday due date** — A due date that falls on a weekend or public holiday moves to the next business day.  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas))_

## Section 4 - Income tax and annual return deadlines

**Income tax and annual return deadlines**  _([ATO, Due dates by topic: income tax](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-topic/income-tax))_

| Obligation | Common date | What moves it |
| --- | --- | --- |
| Individual and sole trader income tax return, self-lodged | 31 October | Lodging through an agent usually moves this to a lodgment program date |
| Partnership and trust return, self-lodged | 31 October | Trust category and prior year compliance can move it to 15 January or 28 February |
| Company return | 28 February for a self-preparer not due earlier; 31 October where the prior year return was late or a prior year return was overdue at 30 June | Medium to large taxpayers have earlier dates |
| Taxable not-for-profit return or non-lodgment advice | 15 May | Automatic concession unless a substituted accounting period applies |
| Agent-lodged returns generally | Per the ATO lodgment program, commonly 15 May for many client categories | Depends on client category and prior year compliance |
| FBT return | 21 May self-lodged | Agent lodgment program dates apply to agent clients. See `au-fbt-year.md` |

**The agent lodgment program is not a taxpayer entitlement.** It is a concession administered
through the agent's client list, it is conditional on the client being on that list by the
relevant date, and it can be withdrawn where the client's lodgment record is poor. A taxpayer who
engages an agent in April cannot assume the May date.

## Section 5 - Deferrals, extensions and disaster support

1. **Electronic lodgment concession.** Quarterly BAS lodgers may receive an extra two weeks for
   quarters 1, 3 and 4 when lodging online. Quarter 2 is excluded because its due date already
   carries a one month extension.
2. **Agent deferral.** A registered agent can request a deferral for a client, or a bulk deferral
   where a practice-level event prevents lodgment.
3. **Individual deferral.** A taxpayer can request more time. Apply before the due date; a request
   made after the due date does not undo a penalty that has already accrued.
4. **Disaster support.** Taxpayers in areas affected by a declared natural disaster may receive
   automatic deferrals of lodgment and payment, and in some cases faster processing of refunds.
5. **Payment arrangements.** An inability to pay is not a reason to delay lodgment. Lodge on time
   and negotiate a payment arrangement. General interest charge continues to accrue under a
   payment arrangement unless the ATO remits it.

## Section 6 - Failure to lodge on time penalty

- **Base penalty** — The FTL penalty is charged per document, not per dollar, and accrues by elapsed time. One penalty unit for every 28 days, or part of 28 days, that the document is overdue, to a maximum of five penalty units.  _([TAA 1953 Schedule 1 s 286-80](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

**Penalty unit amount**  _([ATO, Penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units))_

| When the infringement occurred | Penalty unit |
| --- | --- |
| On or after 1 July 2026 | $364 |
| 7 November 2024 to 30 June 2026 | $330 |
| 1 July 2023 to 6 November 2024 | $313 |
| 1 January 2023 to 30 June 2023 | $275 |

**Entity size multiplier**  _([TAA 1953 Schedule 1 s 286-80](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

| Entity | Multiplier | Maximum base penalty at $364 per unit |
| --- | --- | --- |
| Individual or small withholder | 1 | $1,820 |
| Medium withholder | 2 | $3,640 |
| Large withholder | 5 | $9,100 |
| Significant global entity | 500 | $910,000 |

- **Medium and large withholder** — A medium withholder withholds more than $25,000 but less than $1 million in an income year, and had assessable income for the year, or GST turnover for the month the document was due, of between $1 million and $20 million. A large withholder withholds more than $1 million in the previous income year, or had assessable income or GST turnover of $20 million or more.  _([TAA 1953 Schedule 1 s 286-80](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_
- **Documents FTL penalty applies to** — FTL penalty applies to activity statements, tax returns, FBT returns, PAYG withholding annual reports, Single Touch Payroll reports, annual GST returns and information reports, and taxable payments annual reports. The ATO states that it generally does not apply the penalty in isolated cases of late lodgment, and that it warns the taxpayer before applying it.  _([ATO, Failure to lodge on time penalty](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty))_

## Section 7 - Shortfall and statement penalties

**Shortfall behaviour penalties**  _([TAA 1953 Schedule 1 s 284-225](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-284-225))_

| Behaviour | Base penalty |
| --- | --- |
| Failure to take reasonable care | 25% of the shortfall |
| Recklessness | 50% of the shortfall |
| Intentional disregard of the law | 75% of the shortfall |

- **Penalty variation and no-penalty cases** — The percentages are doubled for a significant global entity. The base penalty can be increased for aggravating circumstances, reduced for mitigating circumstances, or remitted where that is fair and reasonable. **No penalty generally applies** where the taxpayer or the agent took reasonable care, or where the taxpayer applied the law in a way that agrees with ATO advice, published statements or general administrative practice.  _([TAA 1953 Schedule 1 s 284-225](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-284-225))_
- **Voluntary disclosure reductions** — A qualifying disclosure made before the ATO notifies an examination generally reduces the base penalty by 80% where the shortfall is $1,000 or more, and by 100% where it is under $1,000. A qualifying disclosure after notification generally attracts a 20% reduction. Apply the statutory conditions.  _([TAA 1953 Schedule 1 s 284-225](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-284-225))_
- **Penalty relief for inadvertent errors** — **Penalty relief for inadvertent errors.** Available to individuals and to entities with turnover under $10 million, including small businesses, SMSFs, strata title bodies, not-for-profits and co-operatives. It applies to errors from failing to take reasonable care or from taking a position on income tax that is not reasonably arguable. It cannot be applied for; the ATO grants it during an audit. Once granted, no further relief is available for three years, and it is unavailable where there has been reckless or intentional conduct, evasion or phoenix activity in the past three years.  _([ATO, Penalty relief](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-relief))_
- **Agent safe harbour** — **Agent safe harbour.** A client is not liable for an FTL penalty or a false or misleading statement penalty where the client gave the registered tax or BAS agent all relevant tax information, and the failure resulted from the agent's conduct rather than the client's. The burden of proving that the information was provided rests on the taxpayer, and safe harbour does not apply where the agent was reckless or intentionally disregarded the law.  _([ATO, Safe harbour](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/your-practice/tax-and-bas-agents/safe-harbour); [ATO, Penalties for making false or misleading statements](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements))_

## Section 8 - Interest charges

**GIC versus SIC comparison**

|  | General interest charge (GIC) | Shortfall interest charge (SIC) |
| --- | --- | --- |
| When it applies | An amount remains unpaid after the date it should have been paid, including a late-lodged return, an underestimated instalment or an unpaid BAS | An income tax assessment is amended and a shortfall results |
| Why it differs | The taxpayer knew the amount was due | The taxpayer was generally unaware of the shortfall until the amended assessment issued |
| Rate basis | 90-day Bank Accepted Bill rate plus a 7 percentage point uplift | 90-day Bank Accepted Bill rate plus a 3 percentage point uplift |
| Compounding | Daily | Daily |
| Statutory basis | TAA 1953 s 8AAD | TAA 1953 Schedule 1 s 280-105 |

**Published rates**  _([ATO, General interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [ATO, Shortfall interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates))_

| Quarter | GIC annual | GIC daily | SIC annual | SIC daily |
| --- | --- | --- | --- | --- |
| October to December 2026 | 11.51% | 0.03153425% | 7.51% | 0.02057534% |
| July to September 2026 | 11.43% | 0.03131507% | 7.43% | 0.02035616% |
| April to June 2026 | 10.96% | 0.03002740% | 6.96% | 0.01906849% |
| January to March 2026 | 10.65% | 0.02917808% | 6.65% | 0.01821918% |

- **Quarter boundary rate** — **A liability spanning a quarter boundary uses each quarter's own daily rate.** Do not apply one rate across the whole period.  _([ATO, Shortfall interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates))_
- **Deductibility change 1 July 2025** — **Deductibility changed on 1 July 2025.** GIC and SIC incurred on or after 1 July 2025 cannot be claimed as a deduction. A charge incurred before that date remains deductible in the year incurred, and a later remission of a previously deducted charge must be returned as income in the year of remission. A remission of a charge incurred on or after 1 July 2025 is not assessable, because no deduction was available.  _([ATO, General interest charge](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/interest-we-charge/general-interest-charge))_
- **Remission** — **Remission.** Both charges can be remitted. GIC may be remitted where there are extenuating circumstances. Request remission in writing, set out what caused the delay, what was done to fix it and when, and attach evidence. A remission request is not a reason to delay payment: interest keeps accruing while it is considered.  _([ATO, General interest charge](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/interest-we-charge/general-interest-charge))_

## Section 9 - Escalation beyond penalties and interest

Where a liability remains unpaid, the ATO has recovery powers that go beyond interest. In outline
only, because each requires specific advice:

- **Director penalty notices.** A company director can become personally liable for unpaid PAYG
  withholding, GST and superannuation guarantee charge. Some amounts become locked down and
  cannot be avoided by placing the company into administration once reporting is more than three
  months late.
- **Garnishee notices.** The ATO can require a third party, including a bank, to pay money owed
  to the taxpayer directly to the ATO.
- **Departure prohibition orders.** These can prevent a person with a tax debt from leaving
  Australia.
- **Disclosure of business tax debts to credit reporting bureaus.** Available where statutory
  criteria are met.

Any of these is a signal to involve a registered tax agent or a lawyer immediately. Lodging the
next statement does not address them.

## Section 10 - Correction pathways

**Correction pathways**

| Situation | Pathway |
| --- | --- |
| GST error in an earlier BAS, within the credit or debit error limits | Correct on a later BAS. See `au-bas-preparation.md` Section 7 |
| GST error outside those limits, but within the period of review | Revise the earlier activity statement |
| Error in an income tax return | Request an amendment |
| Out of time to amend, or disputing the law or the facts | Lodge an objection. An extension of time to object can be requested |
| Circumstances changed after correct original reporting | This is an adjustment, not an error. Report it in the current period |

**Amendment time limits for income tax**  _([ATO, Time limits on tax return amendments](https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments))_

| Taxpayer | Period |
| --- | --- |
| Individual | 2 years from the day after the notice of assessment is sent |
| Sole trader, 2023-24 and earlier income years | 2 years |
| Sole trader, 2024-25 and later income years | 4 years |
| Other taxpayers | Generally 4 years, subject to the specific provision |

- **Period of review for indirect taxes** — **Period of review for indirect taxes.** Four years and one day from the day the activity statement is lodged. A GST credit is separately subject to a four-year credit time limit, which cannot be extended by an amendment.  _([ATO, Time limits on tax return amendments](https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments))_
- **Amendment increasing tax as voluntary disclosure** — **An amendment that increases tax is treated as a voluntary disclosure**, which usually attracts the concessional penalty treatment in Section 7. Making the disclosure in the approved form matters: agreeing with a shortfall the ATO has already identified is not a voluntary disclosure.  _([ATO, Voluntary disclosures](https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-approved-form/about-the-voluntary-disclosure))_

## Section 11 - Worked example

**Facts.** Harbourline Freight Pty Ltd is a monthly activity statement lodger and a small
withholder. Its June 2026 activity statement was due on 21 July 2026 with a net amount of $24,000.
It lodged and paid on 21 September 2026. It has no prior penalty relief and no agent safe harbour
issue. All figures are synthetic.

**Step 1, days overdue.**

```
Due date                     21 July 2026
Lodged and paid              21 September 2026
Days overdue                 62
```

**Step 2, failure to lodge on time penalty.**

```
28-day periods, counting part periods   62 / 28 = 2.21, rounded up to 3
Maximum is 5 periods, so 3 applies
Penalty unit, infringement after 1 July 2026     $364
Entity multiplier, small withholder              x 1
FTL penalty                 3 x $364 x 1       = $1,092
```

**Step 3, general interest charge.**

The whole 62 day period falls in the July to September 2026 quarter, so one daily rate applies.
A period spanning a quarter boundary would need each quarter's own rate.

```
Unpaid amount                                    $24,000
Daily rate, July to September 2026 quarter       0.03131507%
Compounded daily for 62 days
  $24,000 x ((1 + 0.0003131507) ^ 62 - 1)      = $470.45
```

**Step 4, total cost of being late.**

```
FTL penalty                                      $1,092.00
GIC                                                $470.45
Total                                            $1,562.45
```

**Step 5, what to do about it.** Neither amount is deductible: administrative penalties are never
deductible, and GIC incurred on or after 1 July 2025 is not deductible either. The company can
request remission of both, in writing, setting out the cause of the delay and the steps taken to
correct it. If the delay was caused by the registered agent after the company had provided all
relevant information, the agent safe harbour may remove the FTL penalty, although it does not
remove GIC.

**What the example shows.** The penalty is priced in 28-day blocks of elapsed time, not as a
percentage of the liability, so a nil-balance statement lodged this late costs exactly the same
$1,092. The interest works the other way: it scales with the amount owed and with the number of
days. Lodging on time while negotiating payment would have removed the larger of the two amounts
in this example.

## Section 12 - Common errors

- Quoting an agent lodgment program date to a taxpayer who is not on that agent's client list.
- Assuming the online BAS concession applies to quarter 2. It does not.
- Assuming the online BAS concession applies to monthly lodgers. It does not.
- Treating lodgment and payment as one obligation, so a taxpayer who cannot pay does not lodge.
  This adds an FTL penalty to interest that would have accrued anyway.
- Deducting GIC or SIC incurred on or after 1 July 2025.
- Applying one GIC rate across a period that spans a quarter boundary.
- Correcting a GST error on a later BAS after the debit error time limit has passed.
- Requesting an amendment when the correct pathway is an objection, and running out of time.
- Treating an adjustment event as an error, or an error as an adjustment.
- Assuming a remission request pauses interest. It does not.

## Section 13 - Self-checks

- [ ] The entity type, balance date and agent status are confirmed before any date is quoted.
- [ ] Prior year lodgment status has been checked, because it can pull the current date forward.
- [ ] The correct penalty unit amount for the date of the infringement has been used.
- [ ] The entity size multiplier has been applied, or explicitly confirmed as 1.
- [ ] GIC has been calculated with each quarter's own daily rate, compounded daily.
- [ ] GIC and SIC incurred on or after 1 July 2025 are not treated as deductible.
- [ ] The correction pathway matches the situation and is within its time limit.
- [ ] Any voluntary disclosure is in the approved form.
- [ ] Rates and penalty unit amounts have been rechecked against the ATO pages cited below.

## Section 14 - Sources

- Taxation Administration Act 1953, s 8AAD (GIC rate), Schedule 1 s 280-105 (SIC),
  Schedule 1 Division 284 (shortfall penalties) including s 284-225 (voluntary disclosure
  reductions), Schedule 1 s 286-80 (failure to lodge on time).
- ATO, Failure to lodge on time penalty,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty
- ATO, Penalty units,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units
- ATO, Penalties for making false or misleading statements,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements
- ATO, Penalty relief,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-relief
- ATO, General interest charge,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/interest-we-charge/general-interest-charge
- ATO, General interest charge rates,
  https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates
- ATO, Shortfall interest charge rates,
  https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates
- ATO, Safe harbour,
  https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/your-practice/tax-and-bas-agents/safe-harbour
- ATO, Time limits on tax return amendments,
  https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments
- ATO, Due dates for lodging and paying your BAS,
  https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas
- ATO, Due dates by topic: income tax,
  https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-topic/income-tax

Rates and penalty unit amounts were checked on 16 September 2026. The GIC and SIC rates for the
January to March 2027 quarter had not been published at that date. Confirm every rate and date
against the cited ATO page before relying on it.

## Section 15 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions or outcomes arising from the use of this skill. All outputs
must be reviewed and signed off by a qualified professional in the relevant jurisdiction before
lodging or acting upon them.

The most up-to-date version of this skill is maintained at
[openaccountants.com](https://www.openaccountants.com).

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
