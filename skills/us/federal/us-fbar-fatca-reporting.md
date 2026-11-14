---
name: us-fbar-fatca-reporting
description: "Decide whether a US person must file an FBAR (FinCEN Form 114), a Form 8938 (FATCA, IRC section 6038D), both or neither for calendar and tax year 2026. Covers the FBAR aggregate test (more than USD 10,000 at any time), the Form 8938 thresholds for people living in the US and abroad, what each regime counts, signature authority and its exceptions, due dates, the FBAR and Form 8938 penalties, the assessment periods, and the late-filing and Streamlined routes. Trigger on FBAR, FinCEN 114, Form 8938, FATCA, foreign bank account reporting, specified foreign financial assets. Produces a working paper and a reviewer brief, not a filed report. Load alongside cross-border-tax-workflow-base."
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - cross-border-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# US foreign account and asset reporting: FBAR (FinCEN Form 114) and Form 8938 (FATCA), tax year 2026

> **Source-cited draft.** Built from the IRS FBAR page, the IRS comparison of Form 8938 and FBAR requirements, the Instructions for Form 8938 (Rev. November 2021, continuous use), 31 CFR 1010.350 and 1010.821, 31 U.S.C. 5314 and 5321, 26 U.S.C. 6038D, 6501 and 6662, Treas. Reg. 1.6038D-2, IRM 4.26.16, FinCEN Notice FIN-2025-NTC3 and the IRS Streamlined pages, read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Two separate reports; filing one never satisfies the other. **FBAR:** a US person files FinCEN Form 114 if the combined maximum value of all their foreign financial accounts **exceeded USD 10,000 at any time** in calendar year 2026; it is due 15 April 2027 with an automatic extension to 15 October 2027, filed with FinCEN, not with the tax return. **Form 8938:** an individual living in the US attaches it to the 2026 return if specified foreign financial assets were more than USD 50,000 on 31 December or more than USD 75,000 at any time (USD 100,000 and USD 150,000 married filing jointly); living abroad, the figures are USD 200,000 and USD 300,000 (USD 400,000 and USD 600,000 joint). No income tax return due means no Form 8938.

## Scope and who this is for

This skill decides whether a US person must file an FBAR, a Form 8938, both, or neither, for **calendar/tax year 2026** (filed in 2027), with a dated section on **2025** reports, whose extended deadline passed on 15 October 2026. It covers individuals first; domestic entities are covered only at threshold level.

Two separate regimes. Filing one never satisfies the other.

| | FBAR (FinCEN Form 114) | Form 8938 |
| --- | --- | --- |
| Law | Bank Secrecy Act, 31 U.S.C. 5314; 31 CFR 1010.350; penalties 31 U.S.C. 5321 and 31 CFR 1010.821 | 26 U.S.C. 6038D; Treas. Reg. 1.6038D-1 to -8 |
| Filed with | FinCEN, electronically through the BSA E-Filing System. Not attached to the tax return | Attached to the annual income tax return (Form 1040, 1040-NR, 1041, 1065, 1120) |
| Who | "United States person": citizen, resident, and US corporations, partnerships, LLCs, trusts and estates | "Specified person": specified individuals and specified domestic entities |
| Counts | Foreign financial accounts only (financial interest **or** signature or other authority) | Specified foreign financial assets: foreign accounts **plus** foreign securities, partnership interests, instruments and entity interests held outside an account |

This skill produces a working paper. It is not a filed FBAR or return, and it never decides whether conduct was willful.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Foreign trusts, Forms 3520 and 3520-A, large foreign gifts | `us-foreign-trust-reporting` |
| Controlled foreign corporations, Form 5471 | `us-form-5471-cfc-information` |
| Foreign partnerships, Form 8865 | `us-form-8865-foreign-partnership` |
| Foreign-owned US companies, Form 5472 | `us-form-5472-foreign-owned-us` |
| Foreign earned income exclusion and housing, Form 2555 | `us-foreign-earned-income-2555` |
| Foreign tax credit, Form 1116 | `us-foreign-tax-credit-1116` |
| Nonresident and dual-status returns | `us-form-1040-nr-nonresident-return` |
| The shared cross-border intake and reviewer brief | `cross-border-tax-workflow-base` |

## Ask the client first

1. **Status.** Is the person a US citizen, a green-card holder, or a resident under the substantial presence test for any part of 2026? Did they elect to be treated as resident to file jointly? Are they a dual-status or treaty-resident filer?
2. **Each foreign account:** institution, country, type, account currency, the **highest balance during 2026**, the **31 December 2026 balance**, and whether the person owns it, co-owns it, holds it through an entity or trust, or can only sign on it.
3. **Holdings outside an account:** shares or bonds of foreign issuers held in certificate form, foreign partnership interests, foreign hedge or private equity funds, interests in foreign trusts or estates, foreign pensions, cash-value foreign life insurance or annuities.
4. **Signature authority over an employer's account:** who is the employer? Is it a bank, an SEC/CFTC-registered institution or an Authorized Service Provider? Is it, or its US parent, listed on a US national securities exchange or registered under section 12(g) of the Securities Exchange Act? Does the person have any financial interest in the account?
5. **Filing status and residence:** the income tax filing status, whether the person lived abroad (tax home abroad plus a presence-abroad test), and whether an income tax return is required at all for 2026.
6. **History:** were FBARs and Forms 8938 filed in prior years? If not: was the income reported and tax paid? Has the IRS opened an examination or contacted the person about the missing reports?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| FBAR required if aggregate maximum value of foreign financial accounts exceeded | USD 10,000 at any time in the calendar year | [IRS FBAR page, Who must file](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) |
| FBAR indirect financial interest: ownership of the account-holding corporation, partnership or other entity | more than 50 percent | [31 CFR 1010.350(e)(2)(ii)](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-350.xml) |
| FBAR short-form reporting: financial interest in, or signature authority over | 25 or more accounts | [31 CFR 1010.350(g)(1) and (2)](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-350.xml) |
| FBAR due date, calendar year 2026 | 15 April 2027 | [IRS FBAR page, When to file](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) |
| FBAR automatic extension, no request needed | 15 October 2027 | [IRS FBAR page, When to file](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) |
| FBAR record retention | 5 years from the FBAR due date | [IRS FBAR page, Keeping records](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) |
| Signature authority only, no financial interest (financial professionals): extended due date for calendar year 2025 | 15 April 2027 | [FinCEN Notice FIN-2025-NTC3](https://www.fincen.gov/system/files/2025-12/FBAR-FBAR-Filing-Requirement-for-Certain-Financial-Professionals.pdf) |
| Form 8938, unmarried or married filing separately, living in the US | more than USD 50,000 on the last day or more than USD 75,000 at any time | [Instructions for Form 8938, Reporting Thresholds](https://www.irs.gov/pub/irs-pdf/i8938.pdf) |
| Form 8938, married filing jointly, living in the US | more than USD 100,000 on the last day or more than USD 150,000 at any time | [Instructions for Form 8938, Reporting Thresholds](https://www.irs.gov/pub/irs-pdf/i8938.pdf) |
| Form 8938, unmarried or married filing separately, living abroad | more than USD 200,000 on the last day or more than USD 300,000 at any time | [Instructions for Form 8938, Reporting Thresholds](https://www.irs.gov/pub/irs-pdf/i8938.pdf) |
| Form 8938, married filing jointly, living abroad | more than USD 400,000 on the last day or more than USD 600,000 at any time | [Instructions for Form 8938, Reporting Thresholds](https://www.irs.gov/pub/irs-pdf/i8938.pdf) |
| Form 8938, specified domestic entity | more than USD 50,000 on the last day or more than USD 75,000 at any time | [Instructions for Form 8938, Specified Domestic Entities](https://www.irs.gov/pub/irs-pdf/i8938.pdf) |
| Presence abroad test, physical presence | at least 330 full days in any 12 consecutive months ending in the tax year | [Instructions for Form 8938, Presence abroad](https://www.irs.gov/pub/irs-pdf/i8938.pdf) |
| Statutory floor behind the Form 8938 thresholds | USD 50,000 (or a higher amount the Secretary prescribes) | [26 U.S.C. 6038D(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038D.htm) |
| Form 8938 failure-to-file penalty | USD 10,000 | [26 U.S.C. 6038D(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038D.htm) |
| Form 8938 continuing failure, more than 90 days after notice | USD 10,000 per 30-day period or part, capped at USD 50,000 | [26 U.S.C. 6038D(d)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038D.htm) |
| Accuracy-related penalty on an undisclosed foreign financial asset understatement | 40 percent | [26 U.S.C. 6662(j)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm) |
| Assessment period held open after a Form 8938 failure | not before 3 years after the information is furnished | [26 U.S.C. 6501(c)(8)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6501.htm) |
| Omitted gross income from specified foreign financial assets that opens a 6-year assessment period | more than USD 5,000 | [26 U.S.C. 6501(e)(1)(A)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6501.htm) |
| FBAR non-willful penalty, statutory | up to USD 10,000 | [31 U.S.C. 5321(a)(5)(B)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title31/html/USCODE-2024-title31-subtitleIV-chap53-subchapII-sec5321.htm) |
| FBAR willful penalty, statutory | greater of USD 100,000 or 50 percent of the account balance at the violation | [31 U.S.C. 5321(a)(5)(C) and (D)](https://www.govinfo.gov/content/pkg/USCODE-2024-title31/html/USCODE-2024-title31-subtitleIV-chap53-subchapII-sec5321.htm) |
| FBAR non-willful penalty, inflation-adjusted maximum (penalties assessed on or after 17 January 2025) | USD 16,536 per violation | [31 CFR 1010.821, table](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-821.xml) |
| FBAR willful penalty, inflation-adjusted maximum (penalties assessed on or after 17 January 2025) | USD 165,353, or 50 percent of the balance if greater | [31 CFR 1010.821, table](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-821.xml) |
| FBAR civil penalty assessment period | 6 years from the violation | [31 U.S.C. 5321(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title31/html/USCODE-2024-title31-subtitleIV-chap53-subchapII-sec5321.htm) |
| Streamlined Domestic Offshore miscellaneous offshore penalty | 5 percent of the highest aggregate balance/value of the affected assets | [IRS Streamlined Domestic Offshore Procedures](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states) |
| Streamlined Foreign Offshore non-residency test | no US abode and outside the US at least 330 full days, in at least 1 of the 3 most recent years | [IRS Streamlined Foreign Offshore Procedures](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states) |
| Streamlined look-back | 3 most recent tax years and 6 most recent FBAR years | [IRS Streamlined Foreign Offshore Procedures](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states) |

None of the FBAR or Form 8938 thresholds is indexed for inflation: they are the same for 2025 and 2026. The FBAR penalty maximums are adjusted for inflation by FinCEN (31 CFR 1010.821); the Form 8938 penalties are not.

### The steps

1. **Confirm US-person status** for each regime separately (see the two subsections below). The definitions are close but not identical.
2. **Convert to US dollars.** FBAR: use periodic statements for the maximum value in the account currency, then convert at the official Treasury Reporting Rates of Exchange rate in effect at the end of the calendar year, and record the rate and its source ([IRM 4.26.16](https://www.irs.gov/irm/part4/irm_04-026-016)). Form 8938: use the US Treasury Bureau of the Fiscal Service rate on the last day of the tax year, even for an asset sold earlier in the year; an account statement's own conversion rate may be relied on for a financial account. If no Treasury rate exists, use another publicly available rate and disclose it on Form 8938 ([Instructions for Form 8938](https://www.irs.gov/pub/irs-pdf/i8938.pdf)).
3. **FBAR test.** Add the **maximum** value of every foreign financial account in which the person has a financial interest or signature or other authority. If the total **exceeded USD 10,000 at any time** during the calendar year, an FBAR is required and every such account is reported, including small ones ([IRS comparison chart](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements)). A jointly owned account is reported at its full value on each owner's FBAR, not prorated (IRM 4.26.16).
4. **Form 8938 test.** Confirm an income tax return is required for 2026. Build the list of specified foreign financial assets (not just accounts). Pick the threshold pair for the filing status and residence. Form 8938 is required if the total is **more than** the last-day figure **or more than** the any-time figure, unless an exception applies (see the boundary and exception table). Summing each asset's own maximum value for the any-time test can only overstate the true peak; where that sum is over the line, check the true peak before concluding.
5. **Map every asset to both regimes independently** (boundary and exception table).
6. **Set deadlines** (Filing and payment).
7. **Flag, do not decide**: willfulness, foreign pension treatment, and entity or trust look-through.

### FBAR: who and what counts

- Threshold: aggregate value of foreign financial accounts **exceeded USD 10,000 at any time** during the calendar year. The test is aggregate across accounts, not per account: "if you have 2 accounts with a combined account balance greater than $10,000 at any one time, both accounts would have to be reported" ([IRS comparison chart](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements)). A total of exactly USD 10,000 does not exceed USD 10,000.
- Whether the account produced taxable income has no effect.
- Financial interest includes accounts held in the name of an agent or nominee, a corporation or partnership in which the person owns directly or indirectly more than 50% of the vote, value, profits or capital, a grantor trust the person owns for tax purposes, and a trust in which the person either has a present beneficial interest in more than 50% of the assets or receives more than 50% of the current income ([31 CFR 1010.350(e)](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-350.xml)).
- Signature or other authority means "the authority of an individual (alone or in conjunction with another) to control the disposition of money, funds or other assets held in a financial account by direct communication (whether in writing or otherwise) to the person with whom the financial account is maintained" ([31 CFR 1010.350(f)(1)](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-350.xml)). It is reportable even with no ownership. Five exceptions in 31 CFR 1010.350(f)(2) apply only if the officer or employee has **no financial interest** in the account:
  - (i) an officer or employee of a bank examined by the OCC, the Federal Reserve Board, the FDIC, the Office of Thrift Supervision or the NCUA, for accounts owned or maintained by the bank;
  - (ii) an officer or employee of a financial institution registered with and examined by the SEC or CFTC, for accounts owned or maintained by that institution;
  - (iii) an officer or employee of an Authorized Service Provider (an SEC-registered and SEC-examined entity serving an investment company registered under the Investment Company Act of 1940), for accounts owned or maintained by an SEC-registered investment company;
  - (iv) an officer or employee of an entity with a class of equity securities (or ADRs) listed on a US national securities exchange, for that entity's foreign accounts; and an officer or employee of a US subsidiary of such a listed US entity, for the subsidiary's accounts, but only if the subsidiary is included in the parent's consolidated FBAR;
  - (v) an officer or employee of an entity with a class of equity securities (or ADRs) registered under section 12(g) of the Securities Exchange Act, for that entity's foreign accounts.
- Accounts the IRS FBAR page says need not be reported: correspondent/nostro accounts; accounts owned by a governmental entity or an international financial institution; accounts maintained on a US military banking facility; accounts held in an IRA of which the person is owner or beneficiary, or in a retirement plan of which the person is a participant or beneficiary; and accounts of a trust of which the person is a beneficiary, if a US person (trust, trustee or agent) files an FBAR reporting them ([IRS FBAR page](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar)).

### Form 8938: who and what counts

The same thresholds apply for tax years 2025 and 2026 under the continuous-use instructions (Rev. November 2021), which were still the current edition on 2026-11-14.

| Filing status | Living in the US: last day of year | Living in the US: any time in year | Living abroad: last day | Living abroad: any time |
| --- | --- | --- | --- | --- |
| Unmarried | more than USD 50,000 | more than USD 75,000 | more than USD 200,000 | more than USD 300,000 |
| Married filing jointly | more than USD 100,000 | more than USD 150,000 | more than USD 400,000 | more than USD 600,000 |
| Married filing separately | more than USD 50,000 | more than USD 75,000 | more than USD 200,000 | more than USD 300,000 |

- "Living abroad" requires a tax home in a foreign country **and** one presence-abroad test: (a) a US citizen who was a bona fide resident of a foreign country or countries for an uninterrupted period that includes an entire tax year, or (b) a US citizen or resident present in a foreign country or countries at least 330 full days in any 12 consecutive months ending in the tax year ([Instructions for Form 8938](https://www.irs.gov/pub/irs-pdf/i8938.pdf)).
- Joint filers count a jointly owned asset once. Separate filers who are both specified individuals each count one half of a jointly owned asset; if the spouse is not a specified individual, the full value counts ([Treas. Reg. 1.6038D-2](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol15/xml/CFR-2025-title26-vol15-sec1-6038D-2.xml)).
- If the person does not have to file an income tax return for the year, no Form 8938 is required, whatever the asset value.
- Specified domestic entities (certain closely held passive corporations and partnerships, and certain domestic trusts): more than USD 50,000 on the last day or more than USD 75,000 at any time.
- A foreign pension, estate or deferred compensation interest whose value the person does not know or have reason to know is valued at the distributions received in the year, or zero if none.
- An asset held for investment outside an account may generally be valued at its last-day value, unless the person knows or has reason to know from readily accessible information that this is not a reasonable estimate of its maximum value ([Instructions for Form 8938](https://www.irs.gov/pub/irs-pdf/i8938.pdf)).

## Boundary and exception table

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
| Foreign accounts and non-account assets of a grantor trust of which the person is grantor | Yes, as to foreign accounts | Yes, as to both |
| Foreign real estate held directly; foreign currency or precious metals held directly; art, jewelry, cars | No | No |
| Foreign real estate held through a foreign entity | No | The entity is reportable, valued including the real estate |
| Foreign government social security type benefits | No | No |
| Accounts of an entity the person owns more than 50% of | Yes, as indirect financial interest | No (the entity interest itself may be) |

Source: [IRS comparison chart](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) (page updated 19 September 2026).

### Further exceptions

- **FBAR, US retirement plans only.** Participants and beneficiaries of US plans under IRC sections 401(a), 403(a), 403(b), and owners and beneficiaries of IRAs and Roth IRAs, need not report foreign accounts held by the plan ([31 CFR 1010.350(g)(4)](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-350.xml)). This exception is for US plans. Do not apply it to a foreign pension; treat a foreign pension as a review item.
- **FBAR, spouses.** A spouse need not file separately if all their foreign accounts are jointly owned with the filing spouse, they signed FinCEN Form 114a, and the spouse reports the joint accounts on a timely FBAR. Income tax filing status has no effect on this ([IRS FBAR page](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar)).
- **FBAR, consolidated report.** A person whose foreign accounts are all reported on a consolidated FBAR (filed by a US entity owning more than 50% of the account holder, 31 CFR 1010.350(g)(3)) need not file their own.
- **FBAR, 25 or more accounts.** A person with a financial interest in, or signature authority over, 25 or more accounts may report only the number of accounts and basic information, and must give full details if asked ([31 CFR 1010.350(g)(1) and (2)](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-350.xml)).
- **FBAR, certain trust beneficiaries.** A beneficiary of a trust in which they have a present beneficial interest in more than 50% of the assets or current income need not report the trust's accounts if the trust, its trustee or its agent is a US person that files an FBAR disclosing them ([31 CFR 1010.350(g)(5)](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-350.xml)).
- **Form 8938, duplicative reporting.** A specified individual who reports assets on a timely Form 3520, 3520-A, 5471, 8621 or 8865 does not repeat them on Form 8938, but completes Part IV. Rev. Proc. 2020-17 (relief from Forms 3520/3520-A for certain tax-favoured foreign retirement trusts) does **not** remove the Form 8938 obligation ([Instructions for Form 8938, Reminders](https://www.irs.gov/pub/irs-pdf/i8938.pdf)).
- **Form 8938, dual resident taxpayers** (treaty tie-breaker, Reg. 301.7701(b)-7). Two cases:
  - Nonresident at the end of the tax year: no Form 8938 reporting for the part of the year covered by Form 1040-NR, provided the person complies with Reg. 301.7701(b)-7(b) and (c), including timely filing Form 1040-NR and attaching Form 8833.
  - Resident at the end of the tax year: no Form 8938 reporting for the part of the year reflected on the schedule to Form 1040 or 1040-SR required by Reg. 1.6012-1(b)(2)(ii)(a), provided the person complies with that regulation, including timely filing Form 1040 or 1040-SR with a properly completed Form 8833.

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Highest balance of an account during the year | Use the highest periodic statement balance; ask for every statement before filing |
| Year-end Treasury exchange rate not yet published for 31 December 2026 | Do not finalise the FBAR or Form 8938 totals; compute with the latest published quarterly rate as a draft only and mark it |
| Whether the person lives abroad for Form 8938 | Use the lower living-in-the-US thresholds until the tax home and a presence-abroad test are documented |
| Whether an income tax return is required | Assume it is; ask |
| Whether the employer qualifies for a signature-authority exception | Treat the account as reportable until the employer's status is confirmed |
| Value of a foreign pension or estate interest the person cannot find out | Distributions received in the year, or zero (Form 8938 only); flag for review |
| Prior-year FBARs and Forms 8938 | Assume not filed until copies or BSA Identifiers are produced |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Several small accounts whose peaks add up near USD 10,000 | The FBAR test is aggregate; one day over the line changes the answer |
| Signature authority over an employer's or relative's account | Reportable without any ownership, unless an exception applies |
| Foreign shares, partnership or fund interests held outside an account | Not on the FBAR but counted for Form 8938 |
| Foreign pension, provident fund or cash-value insurance | Often missed on both reports; treatment needs review |
| Foreign income not reported in past years | The 6-year assessment period and the Streamlined route come into play |
| Any IRS letter, examination or penalty proposal | Late-filing and Streamlined routes may no longer be open |

## Worked cases

Thresholds: [IRS comparison chart](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) and [Instructions for Form 8938](https://www.irs.gov/pub/irs-pdf/i8938.pdf). In the `oa-check` blocks, `clamp(value - threshold, 0, 1)` returns 1 when a whole-dollar total is more than the threshold and 0 when it is not; 1 means "required".

**Case A: small accounts add up.** Unmarried US resident. Three foreign bank accounts with highest balances in 2026 of USD 4,000, USD 3,500 and USD 3,000; year-end total well under USD 50,000; no other foreign assets.
- FBAR: USD 4,000 + USD 3,500 + USD 3,000 = USD 10,500, which exceeded USD 10,000. FBAR required, reporting all three accounts.
- Form 8938: below USD 50,000 last day and USD 75,000 any time. Not required.

**Case B: exactly at the line.** Same person, but the highest combined balance on any day was exactly USD 10,000. The aggregate did not exceed USD 10,000, so no FBAR is required on these facts. Check the peak with statements; one day over the line changes the answer.

**Case C, a decision both ways: does living abroad change the answer?** Married filing jointly, tax home in Germany, both bona fide residents for all of 2026. Joint foreign accounts: year-end USD 350,000, highest in the year USD 450,000.
- FBAR: required (each spouse, or one spouse with Form 114a for jointly owned accounts).
- Form 8938, living abroad: USD 350,000 is not more than USD 400,000 (USD 50,000 of headroom) and USD 450,000 is not more than USD 600,000 (USD 150,000 of headroom). Not required.
- Form 8938, had they lived in the US: USD 350,000 is more than USD 100,000 and USD 450,000 is more than USD 150,000. Required. The figure that decides is the presence-abroad test: if either spouse fails it, use the US thresholds.

```oa-check
name: Couple abroad, FBAR and Form 8938 both ways (2026)
inputs:
  year_end_value: 350000
  max_value: 450000
  fbar_threshold: 10000
  abroad_last_day: 400000
  abroad_any_time: 600000
  us_last_day: 100000
  us_any_time: 150000
steps:
  - fbar_required: clamp(max_value - fbar_threshold, 0, 1)
  - f8938_abroad: max(clamp(year_end_value - abroad_last_day, 0, 1), clamp(max_value - abroad_any_time, 0, 1))
  - f8938_if_in_us: max(clamp(year_end_value - us_last_day, 0, 1), clamp(max_value - us_any_time, 0, 1))
  - headroom_last_day: abroad_last_day - year_end_value
  - headroom_any_time: abroad_any_time - max_value
expected:
  fbar_required: 1
  f8938_abroad: 0
  f8938_if_in_us: 1
  headroom_last_day: 50000
  headroom_any_time: 150000
```

**Case D: shares held outside an account.** Unmarried US resident holds foreign-issuer share certificates worth USD 80,000 all year, and no foreign accounts.
- FBAR: not a financial account. Not required.
- Form 8938: USD 80,000 is more than USD 50,000 on the last day and more than USD 75,000 during the year. Required.

**Case E: employee signer.** A US employee of a US operating company can instruct payments from the company's foreign bank account but owns none of it. FBAR: the answer turns on the employer. If the company has a class of equity securities (or ADRs) listed on a US national securities exchange or registered under section 12(g), and the employee has no financial interest, no FBAR is needed for those accounts. The same applies if the company is a US subsidiary of a listed US parent and is included in the parent's consolidated FBAR. If the company is privately held, with no listed or 12(g)-registered parent, and is not a bank, an SEC/CFTC-registered institution or an Authorized Service Provider, the account is reportable under signature authority. Where it is reportable, check the latest FinCEN notice extending the due date for certain signature-only employees and officers (for calendar year 2025, FIN-2025-NTC3 moved it to 15 April 2027). Form 8938: not reportable by the employee.

**Case F: one late FBAR, five accounts, non-willful.** For a non-willful violation, the failure to file one legally compliant FBAR is a single violation, so at most one non-willful penalty applies for that year, not one per account ([IRM 4.26.16](https://www.irs.gov/irm/part4/irm_04-026-016), which incorporates the IRS guidance issued after Bittner v. United States). The current maximum is USD 16,536 (rates table).

**Case G, the edge: the last-day test alone triggers Form 8938.** Unmarried US resident. Three foreign accounts, highest balances USD 4,000, USD 3,500 and USD 3,000, year-end balances USD 2,500, USD 3,000 and USD 1,500. Also foreign-issuer share certificates (not in an account) worth USD 45,000 on 31 December 2026, with no information that the 2026 high was different.
- FBAR: accounts only. USD 10,500 exceeded USD 10,000. Required. The shares are not on the FBAR.
- Form 8938 last day: USD 2,500 + USD 3,000 + USD 1,500 + USD 45,000 = USD 52,000, more than USD 50,000. Any time: USD 4,000 + USD 3,500 + USD 3,000 + USD 45,000 = USD 55,500, not more than USD 75,000. One test is enough: Form 8938 required, listing the three accounts and the shares.

```oa-check
name: Accounts plus shares outside an account, unmarried US resident (2026)
inputs:
  acct1_max: 4000
  acct2_max: 3500
  acct3_max: 3000
  acct1_ye: 2500
  acct2_ye: 3000
  acct3_ye: 1500
  shares: 45000
  fbar_threshold: 10000
  last_day_threshold: 50000
  any_time_threshold: 75000
steps:
  - fbar_aggregate: acct1_max + acct2_max + acct3_max
  - fbar_required: clamp(fbar_aggregate - fbar_threshold, 0, 1)
  - f8938_last_day_total: acct1_ye + acct2_ye + acct3_ye + shares
  - f8938_any_time_total: fbar_aggregate + shares
  - last_day_met: clamp(f8938_last_day_total - last_day_threshold, 0, 1)
  - any_time_met: clamp(f8938_any_time_total - any_time_threshold, 0, 1)
  - f8938_required: max(last_day_met, any_time_met)
expected:
  fbar_aggregate: 10500
  fbar_required: 1
  f8938_last_day_total: 52000
  f8938_any_time_total: 55500
  last_day_met: 1
  any_time_met: 0
  f8938_required: 1
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-FB-WILLFUL | Any sign of willfulness (deliberate concealment, advice ignored, nominee structures) | Stop and refer to tax counsel before anything is filed; the IRS points such taxpayers to its Criminal Investigation Voluntary Disclosure Practice |
| R-FB-CONTACT | The IRS has already contacted the person, opened an examination or proposed FBAR penalties | Refer: the late-filing and Streamlined routes may be closed |
| R-FB-LOOKTHROUGH | Foreign pensions, foreign trusts, or entities where more-than-50% look-through or grantor-trust status is unclear (31 CFR 1010.350(e)) | Refer; see `us-foreign-trust-reporting` for trusts |
| R-FB-TREATY | Treaty-resident or dual-status filers claiming nonresident treatment | Refer; see `us-form-1040-nr-nonresident-return` |
| R-FB-STREAMLINED | Choosing between Streamlined Domestic and Foreign, or signing the non-willful certification | Refer. The certification is the client's own statement of facts; a preparer does not supply it |

## Filing and payment

**FBAR, calendar year 2026**
1. File FinCEN Form 114 electronically through the BSA E-Filing System. It is not filed with the tax return. Paper filing needs a prior exemption from FinCEN.
2. Due **15 April 2027**, with an **automatic extension to 15 October 2027**. No request is needed. Disaster relief notices can extend further. FinCEN also keeps extending the due date for certain employees or officers who have signature or other authority over, but no financial interest in, certain foreign financial accounts; for calendar year 2025 the date is 15 April 2027 (FIN-2025-NTC3). Check for the notice covering calendar year 2026 ([IRS FBAR page](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar)).
3. An attorney, CPA or enrolled agent filing for a client registers as a BSA E-Filer, and the client signs FinCEN Form 114a, which is kept, not filed.
4. To amend, tick "Amended" and give the prior BSA Identifier.
5. Records: keep name on the account, account number, institution name and address, type, and maximum value, generally for 5 years from the FBAR due date. An officer or employee reporting signature authority over an employer's account need not keep these records personally; the employer keeps them.

**Form 8938, tax year 2026**
1. Attach to the 2026 annual return and file by the return's due date **including extensions** (for a calendar-year Form 1040, 15 April 2027, or 15 October 2027 if extended). Do not send it to the IRS on its own; it goes with an annual return or an amended return.
2. There is no separate payment. Tax on the income from the assets is paid with the return.

### FBAR penalties

| Violation | Statutory amount (31 U.S.C. 5321(a)(5)) | Inflation-adjusted maximum for penalties assessed on or after 17 January 2025 (31 CFR 1010.821) |
| --- | --- | --- |
| Non-willful | up to USD 10,000 | USD 16,536 per violation |
| Willful | greater of USD 100,000 or 50% of the account balance at the time of the violation | USD 165,353, or 50% of the balance if greater |

- Non-willful penalties apply per FBAR (one violation per annual report). Willful penalties apply per account, so one late FBAR can produce several willful penalties (IRM 4.26.16).
- No non-willful penalty applies if the violation was due to reasonable cause **and** the balance was properly reported (31 U.S.C. 5321(a)(5)(B)(ii)). The reasonable cause exception does not apply to willful violations (5321(a)(5)(C)(ii)).
- Criminal penalties may apply in addition.
- FinCEN adjusts these maximums for inflation. The 17 January 2025 adjustment was still the latest version of 31 CFR 1010.821 in the eCFR on 2026-11-14. Check for a later FinCEN adjustment before quoting a figure for a penalty assessed in 2027.
- Assessment period: 6 years from the date of the violation (31 U.S.C. 5321(b)(1)). For calendar years 2016 onward, the IRS treats the violation date as the end of 15 April of the following year if a complete and accurate FBAR is not filed by 15 October (IRM 4.26.16).

### Form 8938 penalties and time limits

- Failure to file a complete and correct Form 8938 by the due date including extensions: USD 10,000.
- Continuing failure more than 90 days after the IRS mails a notice: a further USD 10,000 for each 30-day period or part of one, capped at USD 50,000 of additional penalty (maximum USD 60,000 in total).
- Joint filers are treated as a single person for these penalties, with joint and several liability.
- If the IRS asks for values and the person does not provide enough to value the assets, they are presumed to exceed the threshold (26 U.S.C. 6038D(e)).
- Reasonable cause and not willful neglect removes the penalty. A foreign law penalising disclosure is not reasonable cause.
- Accuracy-related penalty of 40% of an underpayment from a transaction involving an undisclosed specified foreign financial asset (26 U.S.C. 6662(j)).
- **Statute of limitations.** If Form 8938 is not filed, or an asset is omitted, the assessment period for the tax year does not end before 3 years after the information is furnished (26 U.S.C. 6501(c)(8)). If the failure was due to reasonable cause and not willful neglect, this extension applies only to the related items. Separately, an omission from gross income of more than USD 5,000 attributable to specified foreign financial assets allows assessment within 6 years (26 U.S.C. 6501(e)(1)(A)(ii)), counted without regard to the Form 8938 threshold or exceptions.

### 2025 reports (dated note, 14 November 2026)

- The **calendar-year 2025 FBAR** was due 15 April 2026 with the automatic extension to **15 October 2026**. That date has passed: a 2025 FBAR filed now is late and follows "Past years not filed" below. Exception: a signature-only employee or officer covered by FIN-2025-NTC3 has until 15 April 2027.
- The **2025 Form 8938** goes with the 2025 return; for an extended calendar-year individual return the due date was 15 October 2026. If the return was filed without it, file an amended return with Form 8938 attached.
- The FBAR and Form 8938 thresholds for 2025 are the same as for 2026. The FBAR penalty maximums above apply to penalties assessed on or after 17 January 2025.

### Past years not filed

- **Late FBARs, no IRS contact.** If the IRS has not contacted the person and they are not under civil or criminal investigation, file the late FBARs as soon as possible, choosing the late-filing reason in the form (or "other" with a written explanation, [FinCEN, Filing Late](https://www.fincen.gov/filing-late)). A penalty will not be asserted for an account where the failure was not willful, was due to reasonable cause, and the account is properly reported on the delinquent FBAR (IRM 4.26.16.3.11, [IRM 4.26.16](https://www.irs.gov/irm/part4/irm_04-026-016)). The former standalone "Delinquent FBAR Submission Procedures" page is no longer at its old IRS address; follow the IRS FBAR page instructions.
- **Unreported income as well: Streamlined Filing Compliance Procedures** ([IRS](https://www.irs.gov/individuals/international-taxpayers/streamlined-filing-compliance-procedures)). Individuals and estates only; the person certifies non-willful conduct ("negligence, inadvertence, or mistake or conduct that is the result of a good faith misunderstanding of the requirements of the law"). Not available if the IRS has opened a civil examination for any year, or during a criminal investigation. Both versions require the 3 most recent tax years (amended or delinquent returns with information returns such as Form 8938) and the 6 most recent FBAR years, with tax and interest paid.
  - **Foreign Offshore** (non-residency test met in at least one of the last 3 years; both spouses for joint filers): no failure-to-file, failure-to-pay, accuracy-related, information return or FBAR penalties ([IRS](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states)).
  - **Domestic Offshore** (returns previously filed, if required, for the 3 years): a miscellaneous offshore penalty of 5% of the highest year-end aggregate balance of the affected assets across the covered years ([IRS](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states)).
- Possible willful conduct: refer to counsel (R-FB-WILLFUL).

## Completion checklist

- [ ] US-person status confirmed for FBAR and specified-person status for Form 8938.
- [ ] Every foreign account listed with maximum and year-end values, converted at the year-end rate, source recorded.
- [ ] FBAR tested on the aggregate of maximum values; the "exceeded USD 10,000" line applied, not "USD 10,000 or more".
- [ ] Signature-authority-only and more-than-50% indirect accounts captured, with exceptions checked.
- [ ] Specified foreign financial assets list built, including holdings outside accounts.
- [ ] Correct threshold pair from the table for filing status and residence; presence-abroad test documented if used.
- [ ] Confirmed that an income tax return is required before concluding Form 8938 is required.
- [ ] Each asset mapped to both regimes; duplicative-reporting and US-retirement exceptions applied only where they fit.
- [ ] Deadlines diarised: FBAR 15 April 2027, automatic 15 October 2027; Form 8938 with the 2026 return including extensions.
- [ ] Prior-year gaps identified; remediation route flagged; willfulness left to counsel.
- [ ] FBAR penalty maximums re-checked against 31 CFR 1010.821 before quoting.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS, Report of Foreign Bank and Financial Accounts (FBAR) page (updated 30 July 2026). Read for who must file, the USD 10,000 aggregate test, the exempt accounts, the spouse and consolidated exceptions, 15 April and 15 October, BSA E-Filing, Form 114a and the 5-year records rule. | https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar | 2026-11-14 |
| IRS, Comparison of Form 8938 and FBAR requirements (updated 19 September 2026). Read for the threshold rows, the "2 accounts" aggregate quote, exchange-rate rules, due dates and the asset-type table. | https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements | 2026-11-14 |
| Instructions for Form 8938 (Rev. November 2021, continuous use). Read for the six individual thresholds, specified domestic entities, the presence-abroad tests (330 full days), no return no Form 8938, valuation, exchange rates, Rev. Proc. 2020-17, duplicative reporting, and the USD 10,000 / USD 50,000 / 40% penalties. | https://www.irs.gov/pub/irs-pdf/i8938.pdf | 2026-11-14 |
| 31 CFR 1010.350 (govinfo, 2025 edition). Read for (a) the reporting duty, (e) financial interest and the more-than-50% tests, (f) signature authority and its five exceptions, (g)(1) to (5) the 25-account, consolidated, retirement plan and trust beneficiary rules. | https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-350.xml | 2026-11-14 |
| 31 CFR 1010.821 (govinfo, 2025 edition). Read for the inflation-adjusted maximums for 31 U.S.C. 5321(a)(5)(B)(i), USD 16,536, and (a)(5)(C)(i)(I), USD 165,353. eCFR version history checked the same day: latest substantive version 17 January 2025. | https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/xml/CFR-2025-title31-vol3-sec1010-821.xml | 2026-11-14 |
| 31 U.S.C. 5321 (govinfo). Read for (a)(5)(B) USD 10,000 and the reasonable cause exception, (a)(5)(C) and (D) USD 100,000 or 50 percent, and (b)(1) the 6-year assessment period. | https://www.govinfo.gov/content/pkg/USCODE-2024-title31/html/USCODE-2024-title31-subtitleIV-chap53-subchapII-sec5321.htm | 2026-11-14 |
| 31 U.S.C. 5314 (govinfo). Read for the duty to keep records and file reports on foreign financial agency relations. | https://www.govinfo.gov/content/pkg/USCODE-2024-title31/html/USCODE-2024-title31-subtitleIV-chap53-subchapII-sec5314.htm | 2026-11-14 |
| 26 U.S.C. 6038D (govinfo). Read for (a) the USD 50,000 floor, (d) the USD 10,000 penalty, 90 days, 30-day periods and USD 50,000 cap, and (e) the presumption. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038D.htm | 2026-11-14 |
| 26 U.S.C. 6501 (govinfo). Read for (c)(8) the 3-year extension and the reasonable cause limit, and (e)(1)(A)(ii) the more-than-USD 5,000 omission and 6 years. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6501.htm | 2026-11-14 |
| 26 U.S.C. 6662 (govinfo). Read for (j) the undisclosed foreign financial asset understatement at 40 percent. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm | 2026-11-14 |
| Treas. Reg. 1.6038D-2 (govinfo, 2025 edition). Read for the USD 50,000 / USD 75,000 thresholds and the joint-ownership counting rules for married specified individuals. | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol15/xml/CFR-2025-title26-vol15-sec1-6038D-2.xml | 2026-11-14 |
| IRM 4.26.16, Report of Foreign Bank and Financial Accounts (effective 26 August 2025). Read for the Treasury Reporting Rates conversion, joint accounts at full value, the violation date, per-report non-willful and per-account willful penalties after Bittner, and 4.26.16.3.11 delinquent FBARs. | https://www.irs.gov/irm/part4/irm_04-026-016 | 2026-11-14 |
| FinCEN Notice FIN-2025-NTC3 (8 December 2025). Read for the extension to 15 April 2027 for signature-only financial professionals for calendar year 2025. | https://www.fincen.gov/system/files/2025-12/FBAR-FBAR-Filing-Requirement-for-Certain-Financial-Professionals.pdf | 2026-11-14 |
| FinCEN, Filing Late. Read for the late-filing reason and the "other" explanation. | https://www.fincen.gov/filing-late | 2026-11-14 |
| IRS, Streamlined Filing Compliance Procedures (updated 11 July 2026). Read for eligibility, the non-willful definition and the civil examination bar. | https://www.irs.gov/individuals/international-taxpayers/streamlined-filing-compliance-procedures | 2026-11-14 |
| IRS, U.S. taxpayers residing outside the United States (updated 11 July 2026). Read for the non-residency test (330 full days, no US abode), 3 tax years and 6 FBAR years, and no penalties. | https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states | 2026-11-14 |
| IRS, U.S. taxpayers residing in the United States (updated 10 July 2026). Read for the 5 percent miscellaneous offshore penalty. | https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states | 2026-11-14 |

Not yet confirmed: the FinCEN notice extending the signature-only due date for calendar year 2026 had not been issued when read (FinCEN has issued one each December); the 31 December 2026 Treasury Reporting Rates of Exchange are not yet published; whether FinCEN will make an inflation adjustment to 31 CFR 1010.821 for penalties assessed in 2027 is not known; the dual-resident rules under Reg. 301.7701(b)-7 and 1.6012-1(b)(2)(ii)(a) are kept from the earlier version and were not re-read against the regulations today.
