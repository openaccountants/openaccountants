---
name: us-fbar-fatca-reporting
description: "US foreign-account and foreign-asset reporting for US persons: the FBAR (FinCEN Form 114) and FATCA (Form 8938, IRC §6038D). Covers the $10,000 FBAR aggregate threshold, the higher Form 8938 thresholds, who must file, what each regime counts, deadlines, the willful/non-willful penalty regime, and the streamlined and delinquent-FBAR remediation paths. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
version: 0.1
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - cross-border-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US foreign account and asset reporting: FBAR (FinCEN Form 114) and Form 8938 (FATCA)

## Scope and who this is for

This Guide decides whether a US person must file an FBAR, a Form 8938, both, or neither, for **calendar/tax year 2026** (filed in 2027), with a dated section for **2025** reports that are still inside their extended deadline on 15 October 2026. It covers individuals first; domestic entities are covered only at threshold level.

Two separate regimes. Filing one never satisfies the other.

| | FBAR (FinCEN Form 114) | Form 8938 |
| --- | --- | --- |
| Law | Bank Secrecy Act, 31 USC 5314; 31 CFR 1010.350; penalties 31 USC 5321 | IRC section 6038D |
| Filed with | FinCEN, electronically through the BSA E-Filing System. Not attached to the tax return | Attached to the annual income tax return (Form 1040, 1040-NR, 1041, 1065, 1120) |
| Who | "United States person": citizen, resident, and US corporations, partnerships, LLCs, trusts and estates | "Specified person": specified individuals and specified domestic entities |
| Counts | Foreign financial accounts only (financial interest **or** signature or other authority) | Specified foreign financial assets: foreign accounts **plus** foreign securities, partnership interests, instruments and entity interests held outside an account |

Sources: IRS FBAR page https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar ; IRS comparison chart https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements ; Form 8938 instructions https://www.irs.gov/instructions/i8938 .

This Guide produces a working paper. It is not a filed FBAR or return, and it never decides whether conduct was willful.

## Ask the client first

- Is the person a US citizen, a green-card holder, or a resident under the substantial presence test for any part of the year? Did they elect to be treated as resident to file jointly? Are they a dual-status or treaty-resident filer?
- For each foreign account: institution, country, type, account currency, the **highest balance during the calendar year**, the **31 December balance**, and whether the person owns it, co-owns it, holds it through an entity or trust, or can only sign on it.
- Any foreign holdings **outside** an account: shares or bonds of foreign issuers held in certificate form, foreign partnership interests, foreign hedge or private equity funds, interests in foreign trusts or estates, foreign pensions, cash-value foreign life insurance or annuities.
- If the person can sign on an employer's foreign account: who is the employer? Is it a bank, an SEC/CFTC-registered institution or an Authorized Service Provider? Is it, or its US parent, listed on a US national securities exchange or registered under section 12(g) of the Securities Exchange Act? Does the person have any financial interest in the account?
- Filing status for the income tax return, and whether the person lived abroad (tax home abroad plus a presence-abroad test, see Form 8938 thresholds).
- Is the person required to file an income tax return at all for the year?
- Were FBARs and Forms 8938 filed in prior years? If not: was the income reported and tax paid? Has the IRS opened an examination or contacted the person about the missing reports?

## The method, step by step

1. **Confirm US-person status** for each regime separately (see the two threshold sections). The definitions are close but not identical.
2. **Convert to US dollars.** FBAR: use periodic statements for the maximum value in the account currency, then convert at the official Treasury Reporting Rates of Exchange rate in effect at the end of the calendar year, and record the rate and its source (IRM section 4.26.16, https://www.irs.gov/irm/part4/irm_04-026-016). Form 8938: use the US Treasury Bureau of the Fiscal Service rate on the last day of the tax year, even for an asset sold earlier in the year; an account statement's own conversion rate may be relied on for a financial account. If no Treasury rate exists, use another public rate and disclose it on Form 8938.
3. **FBAR test.** Add the **maximum** value of every foreign financial account in which the person has a financial interest or signature or other authority. If the total **exceeded $10,000 at any time** during the calendar year, an FBAR is required and every such account is reported, including small ones (https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements).
4. **Form 8938 test.** Build the list of specified foreign financial assets (not just accounts). Pick the threshold pair for the filing status and residence. Form 8938 is required if the total is **more than** the last-day figure **or more than** the any-time figure, unless an exception applies (see the boundary and exception table).
5. **Map every asset to both regimes independently** (boundary and exception table).
6. **Set deadlines** (filing steps below).
7. **Flag, do not decide**: willfulness, foreign pension treatment, and entity or trust look-through.

## Thresholds and figures, with years

### [FBAR thresholds](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements)

- Threshold: aggregate value of foreign financial accounts **exceeded $10,000 at any time** during the calendar year. The test is aggregate across accounts, not per account: "if you have 2 accounts with a combined account balance greater than $10,000 at any one time, both accounts would have to be reported" (IRS comparison chart). A total of exactly $10,000 does not exceed $10,000.
- Whether the account produced taxable income has no effect.
- Financial interest includes accounts held in the name of an agent or nominee, a corporation or partnership in which the person owns directly or indirectly more than 50% of the vote, value, profits or capital, a grantor trust the person owns for tax purposes, and a trust in which the person either has a present beneficial interest in more than 50% of the assets or receives more than 50% of the current income (31 CFR 1010.350(e), https://www.law.cornell.edu/cfr/text/31/1010.350).
- Signature or other authority means authority "to control the disposition of money, funds or other assets held in a financial account by direct communication" to the institution (31 CFR 1010.350(f)). It is reportable even with no ownership. Five exceptions in 31 CFR 1010.350(f)(2) apply only if the officer or employee has **no financial interest** in the account:
  - (i) an officer or employee of a bank examined by the OCC, the Federal Reserve Board, the FDIC, the Office of Thrift Supervision or the NCUA, for accounts owned or maintained by the bank;
  - (ii) an officer or employee of a financial institution registered with and examined by the SEC or CFTC, for accounts owned or maintained by that institution;
  - (iii) an officer or employee of an Authorized Service Provider (an SEC-registered and SEC-examined entity serving an investment company registered under the Investment Company Act of 1940), for accounts owned or maintained by an SEC-registered investment company;
  - (iv) an officer or employee of an entity with a class of equity securities (or ADRs) listed on a US national securities exchange, for that entity's foreign accounts; and an officer or employee of a US subsidiary of such a listed US entity, for the subsidiary's accounts, but only if the subsidiary is included in the parent's consolidated FBAR;
  - (v) an officer or employee of an entity with a class of equity securities (or ADRs) registered under section 12(g) of the Securities Exchange Act, for that entity's foreign accounts.
- These amounts are the same for 2025 and 2026.

### [Form 8938 thresholds (individuals)](https://www.irs.gov/instructions/i8938)

The same thresholds apply for tax years 2025 and 2026 under the current continuous-use instructions (revised 11/2021).

| Filing status | Living in the US: last day of year | Living in the US: any time in year | Living abroad: last day | Living abroad: any time |
| --- | --- | --- | --- | --- |
| Unmarried | more than $50,000 | more than $75,000 | more than $200,000 | more than $300,000 |
| Married filing jointly | more than $100,000 | more than $150,000 | more than $400,000 | more than $600,000 |
| Married filing separately | more than $50,000 | more than $75,000 | more than $200,000 | more than $300,000 |

- "Living abroad" requires a tax home in a foreign country **and** one presence-abroad test: (a) a US citizen who was a bona fide resident of a foreign country for an uninterrupted period that includes an entire tax year, or (b) a US citizen or resident present in a foreign country at least 330 full days in any 12 consecutive months ending in the tax year.
- Joint filers count a jointly owned asset once. Separate filers who are both specified individuals each count one half.
- If the person does not have to file an income tax return for the year, no Form 8938 is required, whatever the asset value.
- Specified domestic entities (certain closely held passive corporations and partnerships, and certain domestic trusts): more than $50,000 on the last day or more than $75,000 at any time.
- A foreign pension, estate or deferred compensation interest whose value the person does not know or have reason to know is valued at the distributions received in the year, or zero if none.

## [Boundary and exception table](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements)

| Situation | FBAR | Form 8938 |
| --- | --- | --- |
| Deposit or custody account at a foreign financial institution | Yes | Yes |
| Account at a foreign branch of a US financial institution | Yes | No |
| Account at a US branch of a foreign financial institution | No | No |
| Signature authority only, no financial interest | Yes, subject to exceptions | No, unless the person otherwise has an interest |
| Foreign stock or securities held in a foreign account | The account is reported; contents are not listed separately | Same |
| Foreign stock or securities not held in an account | No | Yes |
| Foreign partnership interest; foreign hedge or private equity fund | No | Yes |
| Foreign mutual fund | Yes | Yes |
| Foreign-issued life insurance or annuity with cash value | Yes | Yes |
| US mutual fund investing abroad | No | No |
| Foreign real estate held directly; foreign currency or precious metals held directly; art, jewelry, cars | No | No |
| Foreign real estate held through a foreign entity | No | The entity is reportable, valued including the real estate |
| Foreign government social security type benefits | No | No |
| Accounts of an entity the person owns more than 50% of | Yes, as indirect financial interest | No (the entity interest itself may be) |

Source: IRS comparison chart (updated 19 Sep 2026). Further exceptions:

- **FBAR, US retirement plans only.** Participants and beneficiaries of US plans under IRC sections 401(a), 403(a), 403(b), and owners and beneficiaries of IRAs and Roth IRAs, need not report foreign accounts held by the plan (31 CFR 1010.350(g)(4)). This exception is for US plans. Do not apply it to a foreign pension; treat a foreign pension as a review item.
- **FBAR, spouses.** A spouse need not file separately if all their foreign accounts are jointly owned with the filing spouse, they signed FinCEN Form 114a, and the spouse reports the joint accounts on a timely FBAR. Income tax filing status has no effect on this.
- **FBAR, 25 or more accounts.** A person with a financial interest in, or signature authority over, 25 or more accounts may report only the number of accounts and basic information, and must give full details if asked.
- **Form 8938, duplicative reporting.** A specified individual who reports assets on a timely Form 3520, 3520-A, 5471, 8621 or 8865 does not repeat them on Form 8938, but completes Part IV. Rev. Proc. 2020-17 (relief from Forms 3520/3520-A for certain tax-favoured foreign retirement trusts) does **not** remove the Form 8938 obligation.
- **Form 8938, dual resident taxpayers** (treaty tie-breaker, Reg. 301.7701(b)-7). Two cases:
  - Nonresident at the end of the tax year: no Form 8938 reporting for the part of the year covered by Form 1040-NR, provided the person complies with Reg. 301.7701(b)-7(b) and (c), including timely filing Form 1040-NR and attaching Form 8833.
  - Resident at the end of the tax year: no Form 8938 reporting for the part of the year reflected on the schedule to Form 1040 or 1040-SR required by Reg. 1.6012-1(b)(2)(ii)(a), provided the person complies with that regulation, including timely filing Form 1040 or 1040-SR with a properly completed Form 8833.
- **FBAR, certain trust beneficiaries.** A beneficiary of a trust in which they have a present beneficial interest in more than 50% of the assets or current income need not report the trust's accounts if the trust, its trustee or its agent is a US person that files an FBAR disclosing them (31 CFR 1010.350(g)(5)).

## Worked cases ([FBAR and Form 8938 thresholds](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements))

**Case A: small accounts add up.** Unmarried US resident. Three foreign bank accounts with highest balances in 2026 of $4,000, $3,500 and $3,000; year-end total well under $50,000; no other foreign assets.
- FBAR: $4,000 + $3,500 + $3,000 = $10,500, which exceeded $10,000. FBAR required, reporting all three accounts.
- Form 8938: below $50,000 last day and $75,000 any time. Not required.

**Case B: exactly at the line.** Same person, but the highest combined balance on any day was exactly $10,000. The aggregate did not exceed $10,000, so no FBAR is required on these facts. Check the peak with statements; one day over the line changes the answer.

**Case C: couple living abroad.** Married filing jointly, tax home in Germany, both bona fide residents for all of 2026. Joint foreign accounts: year-end $350,000, highest in the year $450,000.
- FBAR: required (each spouse, or one spouse with Form 114a for jointly owned accounts).
- Form 8938: $350,000 is not more than $400,000 and $450,000 is not more than $600,000. Not required. Had they lived in the US, both $100,000 and $150,000 would be exceeded and Form 8938 would be required.

**Case D: shares held outside an account.** Unmarried US resident holds foreign-issuer share certificates worth $80,000 all year, and no foreign accounts.
- FBAR: not a financial account. Not required.
- Form 8938: $80,000 is more than $50,000 on the last day and more than $75,000 during the year. Required.

**Case E: employee signer.** A US employee of a US operating company can instruct payments from the company's foreign bank account but owns none of it. FBAR: the answer turns on the employer. If the company has a class of equity securities (or ADRs) listed on a US national securities exchange or registered under section 12(g), and the employee has no financial interest, no FBAR is needed for those accounts. The same applies if the company is a US subsidiary of a listed US parent and is included in the parent's consolidated FBAR. If the company is privately held, with no listed or 12(g)-registered parent, and is not a bank, an SEC/CFTC-registered institution or an Authorized Service Provider, the account is reportable under signature authority. Where it is reportable, check the latest FinCEN notice extending the due date for certain signature-only employees and officers. Form 8938: not reportable by the employee.

**Case F: one late FBAR, five accounts, non-willful.** For a non-willful violation, the failure to file one legally compliant FBAR is a single violation, so at most one non-willful penalty applies for that year, not one per account (IRM section 4.26.16, which incorporates the IRS guidance issued after Bittner v. United States). The current maximum is under Penalties and time limits.

## Penalties and time limits

### [FBAR penalties](https://www.law.cornell.edu/cfr/text/31/1010.821) (31 USC 5321; 31 CFR 1010.821)

| Violation | Statutory amount | Inflation-adjusted maximum for penalties assessed on or after 17 January 2025 |
| --- | --- | --- |
| Non-willful | up to $10,000 | $16,536 per violation |
| Willful | greater of $100,000 or 50% of the account balance at the time of the violation | $165,353, or 50% of the balance if greater |

- Non-willful penalties apply per FBAR (one violation per annual report). Willful penalties apply per account, so one late FBAR can produce several willful penalties.
- No non-willful penalty applies if the violation was due to reasonable cause **and** the balance was properly reported (31 USC 5321(a)(5)(B)(ii)). The reasonable cause exception does not apply to willful violations.
- Criminal penalties may apply in addition.
- FinCEN adjusts these maximums for inflation. The 17 January 2025 adjustment is the latest in the eCFR table (https://www.law.cornell.edu/cfr/text/31/1010.821) as checked on 25 September 2026. Check the eCFR table and federalregister.gov for a later FinCEN adjustment before quoting a figure.
- Assessment period: 6 years from the date of the violation (31 USC 5321(b)(1), https://www.law.cornell.edu/uscode/text/31/5321). For calendar years 2016 onward, the IRS treats the violation date as the end of 15 April of the following year if a complete FBAR is not filed by 15 October.
- Records: keep name on the account, account number, institution name and address, type, and maximum value, generally for 5 years from the FBAR due date.

### Form 8938 (IRC 6038D, https://www.law.cornell.edu/uscode/text/26/6038D)

- Failure to file a complete and correct Form 8938 by the due date including extensions: $10,000.
- Continuing failure more than 90 days after the IRS mails a notice: a further $10,000 for each 30-day period or part of one, capped at $50,000 of additional penalty (maximum $60,000 in total).
- Joint filers are treated as a single person for these penalties, with joint and several liability.
- If the IRS asks for values and the person does not provide enough to value the assets, they are presumed to exceed the threshold.
- Reasonable cause and not willful neglect removes the penalty. A foreign law penalising disclosure is not reasonable cause.
- Accuracy-related penalty of 40% of an underpayment from a transaction involving an undisclosed specified foreign financial asset.
- **Statute of limitations.** If Form 8938 is not filed, or an asset is omitted, the assessment period for the tax year does not end before 3 years after the information is furnished (IRC 6501(c)(8)). If the failure was due to reasonable cause and not willful neglect, this extension applies only to the related items. Separately, an omission from gross income of more than $5,000 attributable to specified foreign financial assets allows assessment within 6 years (IRC 6501(e)(1)(A)(ii)), counted without regard to the Form 8938 threshold or exceptions (https://www.law.cornell.edu/uscode/text/26/6501).

## Filing and payment steps, with deadlines

**FBAR**
1. File FinCEN Form 114 electronically through the BSA E-Filing System. It is not filed with the tax return. Paper filing needs a prior exemption from FinCEN.
2. Due **15 April** after the calendar year, with an **automatic extension to 15 October**. No request is needed. Disaster relief notices can extend further. FinCEN also keeps extending the due date for certain employees or officers who have signature or other authority over, but no financial interest in, certain foreign financial accounts. Check the most recent FinCEN notice for certain financial professionals (https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar).
3. An attorney, CPA or enrolled agent filing for a client registers as a BSA E-Filer, and the client signs FinCEN Form 114a, which is kept, not filed.
4. To amend, tick "Amended" and give the prior BSA Identifier.

**Form 8938**
1. Attach to the annual return and file by the return's due date **including extensions**. Do not send it to the IRS on its own; it goes with an annual return or an amended return.
2. There is no separate payment. Tax on the income from the assets is paid with the return.

### 2025 reports (dated note, 25 September 2026)

- The **calendar-year 2025 FBAR** was due 15 April 2026 with the automatic extension to **15 October 2026**. It is still timely until then.
- The **2025 Form 8938** goes with the 2025 return; for an extended individual return the due date is 15 October 2026.
- The FBAR and Form 8938 thresholds for 2025 are the same as for 2026. The FBAR penalty maximums above apply to penalties assessed on or after 17 January 2025.

### Past years not filed

- **Late FBARs, no IRS contact.** If the IRS has not contacted the person and they are not under civil or criminal investigation, file the late FBARs as soon as possible, choosing the late-filing reason in the form (or "other" with a written explanation, https://www.fincen.gov/filing-late). The IRS will not assert a penalty for an account where the failure was not willful, was due to reasonable cause, and the account is properly reported on the delinquent FBAR (IRM section 4.26.16.3.11, https://www.irs.gov/irm/part4/irm_04-026-016). The former standalone "Delinquent FBAR Submission Procedures" page is no longer at its old IRS address; follow the IRS FBAR page instructions.
- **Unreported income as well: Streamlined Filing Compliance Procedures** (https://www.irs.gov/individuals/international-taxpayers/streamlined-filing-compliance-procedures). Individuals and estates only; the person certifies non-willful conduct ("negligence, inadvertence, or mistake or conduct that is the result of a good faith misunderstanding of the requirements of the law"). Not available if the IRS has opened a civil examination for any year, or during a criminal investigation. Both versions require the 3 most recent tax years (amended or delinquent returns with information returns such as Form 8938) and the 6 most recent FBAR years, with tax and interest paid.
  - **Foreign Offshore** (non-residency test met in at least one of the last 3 years; both spouses for joint filers): no failure-to-file, failure-to-pay, accuracy-related, information return or FBAR penalties (https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states).
  - **Domestic Offshore** (returns previously filed, if required, for the 3 years): a miscellaneous offshore penalty of 5% of the highest year-end aggregate balance of the affected assets across the covered years (https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states).
- Possible willful conduct: refer to counsel; the IRS points such taxpayers to its Criminal Investigation Voluntary Disclosure Practice.

## When to refuse or refer

- Any sign of willfulness (deliberate concealment, advice ignored, nominee structures): stop and refer to tax counsel before anything is filed.
- The IRS has already contacted the person, opened an examination or proposed FBAR penalties.
- Foreign pensions, foreign trusts, or entities where more-than-50% look-through or grantor-trust status is unclear (31 CFR 1010.350(e), https://www.law.cornell.edu/cfr/text/31/1010.350).
- Treaty-resident or dual-status filers claiming nonresident treatment.
- Choosing between Streamlined Domestic and Foreign, or signing the non-willful certification. The certification is the client's own statement of facts; a preparer does not supply it.

## [Completion checklist](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements)

- [ ] US-person status confirmed for FBAR and specified-person status for Form 8938.
- [ ] Every foreign account listed with maximum and year-end values, converted at the year-end rate, source recorded.
- [ ] FBAR tested on the aggregate of maximum values; the "exceeded $10,000" line applied, not "$10,000 or more".
- [ ] Signature-authority-only and more-than-50% indirect accounts captured, with exceptions checked.
- [ ] Specified foreign financial assets list built, including holdings outside accounts.
- [ ] Correct threshold pair from the table for filing status and residence; presence-abroad test documented if used.
- [ ] Confirmed that an income tax return is required before concluding Form 8938 is required.
- [ ] Each asset mapped to both regimes; duplicative-reporting and US-retirement exceptions applied only where they fit.
- [ ] Deadlines diarised: FBAR 15 April, automatic 15 October; Form 8938 with the return including extensions.
- [ ] Prior-year gaps identified; remediation route flagged; willfulness left to counsel.
- [ ] FBAR penalty maximums re-checked against the eCFR table before quoting.

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
