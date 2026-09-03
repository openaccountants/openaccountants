---
name: foreign-employment-income-exemption-section-10-1-o-ii
description: It is not "the first R1.25 million is exempt". SARS applies a work-day ratio first and caps second, so on most facts the ratio binds long before the cap does.
jurisdiction: ZA
last_updated: 2026-09-02
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# South Africa — Foreign Employment Income Exemption, s 10(1)(o)(ii)

## South Africa — Foreign Employment Income Exemption, s 10(1)(o)(ii)

> **The single most misunderstood point.** The exemption is **not** "the first
R1,250,000 of foreign remuneration is exempt". SARS applies a work-day ratio to the
foreign-service remuneration **first**, and caps the result **second**. On most
facts the ratio binds long before the cap does, and a return prepared on the
"first R1.25m" assumption will overstate the exemption, sometimes by a very large
amount.

## Section 1 — Scope

This file covers the s 10(1)(o)(ii) exemption for a South African **tax resident** who
renders services outside the Republic as an **employee** (holder of an office or
employment).

Covered: the day tests, the apportionment formula, the annual cap, the twelve month
window, day counting, IRP5 coding, ITR12 containers.

**Not covered:** s 10(1)(o)(i), the separate and **uncapped** exemption for officers and
crew of ships — a different container and a different test. Independent contractors, who
are not employees and cannot use this section. Tax residency itself (see
`za-tax-residency`). Foreign tax credits under s 6*quat*. Double tax agreement relief,
which is a separate and sometimes better route.

## Section 2 — Three quantities, three different jobs

**Three quantities, three different jobs**  _(Income Tax Act 58 of 1962 s 10(1)(o)(ii); SARS Interpretation Note 16.)_

| Quantity | What it is | What it does |
| --- | --- | --- |
| **Full days outside the Republic** | More than 183 days in aggregate, **and** a continuous period of more than 60 full days, in any 12 consecutive months | **The gate, and only the gate.** It decides whether the exemption is available at all. It never touches a rand of the calculation. |
| **Work days outside ÷ total work days** | The apportionment ratio | **The money.** It determines how much of the remuneration is exempt. |
| **R1,250,000** | The statutory ceiling per year of assessment | Applied **last**, to the result of the ratio. |

Almost every error in this area is a confusion between these three. They are not
alternatives; all three apply, in order.

A taxpayer can pass the gate comfortably and still receive a small exemption, because
the gate and the money are computed from different things.

_Source: Income Tax Act 58 of 1962 s 10(1)(o)(ii); SARS Interpretation Note 16._

## Section 3 — The computation

- **Exemption computation** — exemption = ( work days outside RSA ÷ total work days ) × foreign-service remuneration per the IRP5 then limited to R1 250 000  _(Income Tax Act 58 of 1962 s 10(1)(o)(ii); SARS Interpretation Note 16.)_

### Worked example

An employee with a foreign assignment, remuneration attributable to the assignment
period of **R1,200,000**, who rendered services on **120** work days outside the
Republic out of **200** total work days in the year:

```
ratio       120 ÷ 200                        = 0.60
apportioned 0.60 × R1,200,000                = R720,000
cap         R720,000 is below R1,250,000     → no limiting
exemption                                      R720,000
```

Note what this means: the remuneration exceeded the cap, but the exemption is
**R720,000, not R1,250,000**. To reach the cap on this base the taxpayer would have
needed a ratio above 104%, which is impossible.

### The general point

For the cap to bind at all, the ratio must exceed `R1,250,000 ÷ remuneration`. Work out
that number before assuming the cap is the operative limit. On a base of R1,350,000 the
ratio would need to exceed **92.6%** — effectively unattainable for anyone who spends any
material time working in South Africa.

## Section 4 — The IRP5 must carry the remuneration UN-apportioned

- **IRP5 must carry remuneration un-apportioned** — SARS applies the ratio to **whatever the foreign-service codes disclose**. If the employer has already apportioned the remuneration before coding it, the remuneration is apportioned **twice** — once by the payroll, once again by SARS — and the exemption collapses. **So the foreign-service codes must carry the remuneration for the assignment period in full, un-apportioned, and let the SARS ratio do the work.** That is how Interpretation Note 16's own worked example behaves. **Practical consequence:** an under-coded certificate silently caps the taxpayer out *below* the statutory limit, and no amount of correct work on the return will recover it. Where the coding is wrong, the fix is a corrected IRP5 from the employer, not a re-computation. Check the certificate before doing anything else.  _(Interpretation Note 16's own worked example)_

## Section 5 — Choosing the twelve month window

- **Choosing the twelve month window** — The period is **any 12 consecutive months**. It need **not** be the year of assessment, and choosing it deliberately is part of the work. An assignment that straddles a year end will often produce a comfortable margin on one window and a dangerous margin on another. A window giving 185 days against a 183 day requirement is a margin of two days — one contested border stamp from failing. Shifting the window to capture a tour that crosses the year end can turn that into a margin of several weeks on identical underlying facts. Test more than one window before settling. Record which window was used and why.  _(Section 5 — Choosing the twelve month window)_

## Section 6 — Counting full days

- **Counting full days** — A **full day** outside the Republic is a day spent **wholly** outside it. Both the departure day and the return day are therefore excluded from the count. - **Overnight flights.** Where the RSA exit stamp and the foreign entry stamp fall on different dates, the arrival day is a full day abroad. Where the flight departs and lands on the same date — common on short regional hops — only one day is lost. - **Foreign-to-foreign travel.** A day spent travelling between two foreign countries is a full day outside the Republic. The absence is not broken by transiting a third country. - **Evidence.** Build the count from passport stamps, boarding passes and the assignment schedule, date by date. A count asserted from memory will not survive verification.  _(Section 6 — Counting full days)_

## Section 7 — Work days are not automatically Monday to Friday

- **Work days are days services were actually rendered** — The ratio uses days on which services were **actually rendered**, not a calendar weekday proxy. For many assignments the two are close enough. For others they are not: touring professionals, shift workers, events staff and anyone on duty for the whole of a deployment routinely render services at weekends. Applying a weekday proxy in those cases can understate the foreign work days by a third or more, and understate the exemption in the same proportion. Build the date-by-date schedule of days actually worked, inside and outside the Republic, and use it for both the numerator and the denominator.  _(SARS Interpretation Note 16 §4.3.)_

## Section 8 — ITR12 containers

**ITR12 containers**  _(ITR12 containers 4041, 4033, 4587 and 4259.)_

| Field | What it is | Use it? |
| --- | --- | --- |
| **4041** | The s 10(1)(o)(ii) exempt amount | ✅ **This is the claim field.** |
| 4033 | The s 10(1)(o)(i) container — officers and crew of ships | ❌ A different, uncapped exemption. Not this one. |
| 4587 | An IRP5 information code | ❌ Not a claim field. |
| 4259 | Foreign income **not** reflected on a South African IRP5 | Mandatory. Enter **0** where all foreign remuneration is on an SA IRP5. |

Placing the claim in the wrong container is a common cause of a verification request even where the underlying computation is correct.

## Section 9 — Edge cases

- **Passing the gate does not size the exemption.** Treat them as separate questions and compute them separately.
- **The cap is per year of assessment**, applied after the ratio, not before.
- **Employees only.** An independent contractor cannot use this section, whatever the contract is called. Test the relationship, not the label.
- **Residency first.** A non-resident has no need of this exemption; a resident who has ceased residency mid-year has a different problem. Settle residency before computing.
- **A double tax agreement may give a better result** than s 10(1)(o)(ii) on the same facts. Where a DTA applies, compare the two before claiming.
- **Where the exemption is partial**, the non-exempt balance stays in gross income and is taxed normally, and s 6*quat* foreign tax credit relief may apply to it.

## The method, step by step

1. **Settle tax residency first.** A non-resident does not need this exemption and a part-year resident has a different problem. Everything below assumes a resident.
2. **Read the IRP5 before you compute anything.** If the employer has already apportioned the foreign-service remuneration before coding it, stop — the figure will be apportioned twice and the exemption will collapse. That is fixed with a corrected certificate, not on the return.
3. **Choose the twelve month window deliberately, and test more than one.** It need not be the year of assessment. A window that clears 183 days by two is one disputed stamp from failing; a different window on the same facts may clear it by weeks.
4. **Run the day tests as a gate only** — more than 183 full days in aggregate and more than 60 continuous. This decides whether the exemption exists. It never sizes it.
5. **Build the work-day schedule separately**, date by date, from days on which services were actually rendered. Do not use a Monday-to-Friday proxy unless you have checked it holds.
6. **Apply the ratio to the foreign-service remuneration, then apply the cap.** In that order. Work out `R1,250,000 ÷ remuneration` first: if the ratio is below it, the cap is irrelevant and quoting R1,250,000 is simply wrong.
7. **Claim in container 4041**, and put a figure in 4259.

**What breaks when the order is wrong.** Capping before apportioning overstates the exemption, often by hundreds of thousands. Using the full-day count to size the exemption instead of the work-day ratio gives a different and wrong number. And computing anything before reading the certificate risks building a correct calculation on a figure that was already reduced once.

## Section 10 — Self-checks

1. **Compute the ratio threshold.** `R1,250,000 ÷ foreign-service remuneration`. If the work-day ratio is below that number, the **cap is not the operative limit** — the ratio is. Stating the exemption as R1,250,000 in that case is wrong.
2. **Check the certificate for double apportionment.** Does the foreign-service remuneration on the IRP5 look like it has already been reduced by a time ratio? If so, applying the SARS ratio again understates the exemption. Get it corrected.
3. **Test a second twelve month window** before accepting a thin margin on the day tests.
4. **Reconcile the day counts.** Work days outside plus work days inside must equal total work days. Full days outside is a different count and will not tie to it.
5. **Confirm the container is 4041**, and that 4259 carries a figure.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted
workflows. It has not been reviewed for any specific person's facts, documents,
elections, deadlines, residency, filing status or local procedures. Do not rely on it to
file, pay, amend or take a tax position without review by a qualified professional in
South Africa.

## Sources

Income Tax Act 58 of 1962 s 10(1)(o)(ii); SARS Interpretation Note 16, in particular §4.3 on days on which services were actually rendered. ITR12 containers 4041, 4033, 4587 and 4259.

> Contributed by Brandon Iverach, SAIPA 18504 / SARS PR0025122.

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
