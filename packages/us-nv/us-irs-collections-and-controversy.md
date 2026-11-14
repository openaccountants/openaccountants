---
name: us-irs-collections-and-controversy
description: IRS notices, audits, collections and appeals for US federal income tax in 2026, for individuals and small businesses and their representatives. Covers reading a notice and its deadline (CP2000, CP3219A, CP14, CP504, LT11 and Letter 1058, Letter 3172, CP59), the 90-day Tax Court clock, the 30-day Collection Due Process window (Form 12153), the 10-year collection statute and what suspends it, payment plans and their 2026 fees, currently not collectible, offers in compromise (USD 205 fee, 20% down), liens and levies (2026 levy exemptions), passport certification (USD 66,000 for 2026), failure to file and pay, accuracy and fraud penalties, interest, the new Automatic Exemption from Penalty, First Time Abate, reasonable cause, and innocent spouse relief. Federal only.
version: "2.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: references
type: situation-rules
---

# IRS notices, audits, collections and appeals, tax year 2026

> **Source-cited draft.** Built from IRS pages on notices, payment plans, offers in compromise, penalties, penalty relief, interest and passport certification, Publications 5, 594 and 1660, IRM 5.1.19, Rev. Proc. 2025-32, and 26 U.S.C. 6015, 6213, 6330, 6332, 6334, 6404, 6501, 6502, 6503, 6532, 6651, 6662, 6663, 6664, 7430, 7463 and 7521 (govinfo), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Every IRS notice starts a clock that runs from the date printed on it. The two that cannot be missed: a statutory notice of deficiency gives **90 days** (150 if addressed outside the US) to petition the Tax Court, and a final notice of intent to levy (LT11 or Letter 1058) gives **30 days** to ask for a Collection Due Process hearing on Form 12153. The IRS has **10 years** from each assessment to collect it, longer if something suspends the clock. An individual who owes **USD 50,000 or less** and has filed every return can set up a long-term payment plan online. An offer in compromise costs a **USD 205** fee and, for a lump-sum offer, **20%** of the offer with the application. For 2026 a debt over **USD 66,000** with a lien or levy can be certified to the State Department for passport action.

## Scope and who this is for

In scope: procedure for individuals and small businesses on federal income tax: how to read an IRS notice, which deadline it starts, and which route (response, payment plan, offer, hearing, appeal or court) fits the client. Figures are those the IRS publishes for 2026. It does not decide the underlying tax.

To talk to the IRS for a client, a practitioner needs Form 2848, which authorises a person eligible to practise before the IRS to represent the client ([About Form 2848](https://www.irs.gov/forms-pubs/about-form-2848)), or Form 8821, which only lets the named person inspect or receive the client's information ([About Form 8821](https://www.irs.gov/forms-pubs/about-form-8821)).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Business extensions and timely mailing (section 7502) | `us-corporate-extension-form-7004-and-the` |
| Underpayment of estimated tax | `us-quarterly-estimated-tax` |
| The individual return itself | `us-form-1040-individual-return` |
| FBAR and FATCA penalties | `us-fbar-and-fatca-8938` (refer) |
| Payroll tax deposits and the trust fund recovery penalty | `us-form-941-and-940-payroll` (refer on the penalty) |
| State tax collection | the state's own procedures |

## Ask the client first

- Every IRS letter received, with its notice number (top right, e.g. CP2000, CP14, CP504, LT11, Letter 1058, Letter 3172, CP3219A) and its **date**. Deadlines run from the notice date, not the day it arrived.
- Which tax years and forms are involved, and whether any return is still unfiled. Most relief (payment plans, offers) needs all required returns filed.
- Whether the client agrees the tax is owed. Disputing the amount and paying it over time are different routes.
- Whether a payment plan, offer in compromise or bankruptcy is or was in place, and whether a plan ever defaulted.
- Monthly income, basic living costs and assets (bank, vehicles, home equity, retirement accounts), if the client cannot pay in full.
- For a joint return: whether the problem comes from the other spouse's income or deductions, and whether the spouses are now divorced, separated or living apart.
- Whether the client lives or has lived outside the United States for 6 months or more, or served in a combat zone (both change deadlines or the collection clock).
- Whether a special agent or anyone from IRS Criminal Investigation has made contact. If so, stop and refer (see "When to refuse or refer").

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| CP2000 response period | 30 days from the notice date (60 days if living outside the US) | [IRS Topic 652](https://www.irs.gov/taxtopics/tc652) |
| Tax Court petition after a statutory notice of deficiency | 90 days (150 days if addressed to a person outside the US) | [26 U.S.C. 6213(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapB-sec6213.htm) |
| Math-error abatement request | 60 days after the notice | [26 U.S.C. 6213(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapB-sec6213.htm) |
| CP14 payment due date | generally 21 calendar days, or 10 business days if USD 100,000 or more | [IRS failure to pay penalty page](https://www.irs.gov/payments/failure-to-pay-penalty) |
| Collection Due Process hearing request | 30 days | [26 U.S.C. 6330(a)(3)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap64-subchapD-partI-sec6330.htm) |
| Collection statute | 10 years after assessment | [26 U.S.C. 6502(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6502.htm) |
| Formal protest needed if the proposed change for any period exceeds | USD 25,000 | [Publication 5](https://www.irs.gov/pub/irs-pdf/p5.pdf) |
| Small tax case limit, per year | USD 50,000 | [26 U.S.C. 7463](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap76-subchapC-partII-sec7463.htm) |
| Attorney fee award cap, fees incurred in 2026 | USD 260 per hour | [Rev. Proc. 2025-32, section 3.61](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Online long-term payment plan, individuals | USD 50,000 or less, all returns filed | [IRS payment plans page](https://www.irs.gov/payments/payment-plans-installment-agreements) |
| Online short-term plan (180 days or less), individuals | less than USD 100,000 | [IRS payment plans page](https://www.irs.gov/payments/payment-plans-installment-agreements) |
| Long-term plan fee, direct debit | USD 29 online; USD 107 by phone, mail or in person | [IRS payment plans page](https://www.irs.gov/payments/payment-plans-installment-agreements) |
| Long-term plan fee, other payment methods | USD 69 online; USD 178 by phone, mail or in person | [IRS payment plans page](https://www.irs.gov/payments/payment-plans-installment-agreements) |
| Long-term plan fee, low-income, not direct debit | USD 43 (may be reimbursed) | [IRS payment plans page](https://www.irs.gov/payments/payment-plans-installment-agreements) |
| Revise a plan | USD 6 online; USD 89 by phone, mail or in person | [IRS payment plans page](https://www.irs.gov/payments/payment-plans-installment-agreements) |
| Simple Payment Plan, businesses with trust fund taxes | USD 25,000 or less | [IRS Simple Payment Plans page](https://www.irs.gov/payments/simple-payment-plans-for-individuals-and-businesses) |
| Offer in compromise application fee | USD 205 | [IRS offer in compromise page](https://www.irs.gov/payments/offer-in-compromise) |
| Lump-sum offer, payment with the application | 20% of the offer | [IRS offer in compromise page](https://www.irs.gov/payments/offer-in-compromise) |
| Bank levy holding period | 21 days | [26 U.S.C. 6332(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap64-subchapD-partII-sec6332.htm) |
| Levy exemption, household goods and personal effects, 2026 | USD 11,980 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Levy exemption, books and tools of the trade, 2026 | USD 5,990 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Seriously delinquent tax debt (passport), calendar year 2026 | USD 66,000 | [Rev. Proc. 2025-32, section 3.60](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Failure to file, per month or part month | 5%, to 25% | [26 U.S.C. 6651(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm) |
| Failure to file minimum, Forms 1040 and 1120 due after 31 December 2025 (2025 returns) | USD 525 or 100% of the tax if less | [IRS failure to file penalty page](https://www.irs.gov/payments/failure-to-file-penalty) |
| Failure to file minimum, returns required to be filed in 2027 (2026 returns) | USD 535 or 100% of the tax if less | [Rev. Proc. 2025-32, section 3.52](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Failure to pay, per month or part month | 0.5%, to 25%; 0.25% during an approved plan (individual who filed on time); 1% after 10 days from a notice of intent to levy | [IRS failure to pay penalty page](https://www.irs.gov/payments/failure-to-pay-penalty) |
| Accuracy-related penalty | 20% (40% for a gross valuation misstatement) | [26 U.S.C. 6662](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm) |
| Substantial understatement, individuals | exceeds the greater of 10% of the tax required to be shown or USD 5,000 | [26 U.S.C. 6662(d)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm) |
| Civil fraud penalty | 75% | [26 U.S.C. 6663](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6663.htm) |
| Underpayment interest rate, each quarter of 2026 except April to June | 7% (6% for April to June 2026) | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |

The fees, the levy exemptions, the passport amount, the attorney fee cap and the failure to file minimum change each year. The statutory periods and penalty rates do not.

### Steps

1. **Identify the notice and its clock.** Read the notice number, date, tax year and amount. Use the notice table below to find the legal effect and the deadline. Calendar the deadline the same day. If a Collection Due Process (CDP) or Tax Court deadline is close, file first and build the case afterwards.
2. **Get authority and the facts.** File Form 2848 or 8821. Pull the account, wage-and-income and return transcripts for every open year. From the account transcript take the assessment date for each year (this starts the 10-year collection clock) and any suspension events. Never work from the notice balance alone.
3. **Decide whether the tax is right.** If the proposed or assessed tax is wrong, dispute it by the route the notice allows (CP2000 response, audit protest, Tax Court petition, math-error abatement request). If it is right, go to step 4.
4. **Fix compliance.** File any missing returns and bring current-year payments up to date. Without this, the IRS will not grant a payment plan online or process an offer.
5. **Compute the collection picture.** For each year: balance, penalties by type, and the collection statute expiration date (CSED) adjusted for suspensions. Check whether penalty relief (AEP, First Time Abate or reasonable cause) removes part of the balance.
6. **Choose the route.** In order of cost: pay in full; short-term plan (180 days); long-term payment plan; partial-payment plan; currently not collectible; offer in compromise. Compare each against the CSED.
7. **File the right form by the deadline** and keep proof of the date (fax confirmation, certified mail receipt, upload receipt).
8. **Follow up.** Calendar every later deadline (IRS decision, 30-day appeal windows, offer compliance for 5 years, payment-plan terms, CSEDs) and re-pull transcripts to confirm the IRS posted what was agreed.

### Notices and their deadlines

| Notice | What it means | Deadline and effect | Source |
| --- | --- | --- | --- |
| CP2000 | Proposed change from matching third-party forms (W-2, 1099) to the return. Not a bill, not an assessment. | Respond within 30 days of the notice date, or 60 days if the client lives outside the US. No response means a statutory notice of deficiency. | [Topic 652](https://www.irs.gov/taxtopics/tc652) |
| CP3219A | Statutory notice of deficiency ("90-day letter") from the matching programme. | Tax Court petition within 90 days of mailing, 150 days if addressed to a person outside the US. The IRS cannot extend it. If no petition is filed, the tax is assessed and billed. | [CP3219A](https://www.irs.gov/individuals/understanding-your-cp3219a-notice); [26 U.S.C. 6213](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapB-sec6213.htm) |
| Math-error notices (e.g. CP11, CP12) | IRS corrected a math or clerical error and assessed without a deficiency notice. | Request abatement within 60 days after the notice; the IRS must then abate and use normal deficiency procedures to reassess. | [26 U.S.C. 6213(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapB-sec6213.htm) |
| CP14 | First bill for an assessed balance. | Pay by the notice due date, generally 21 calendar days after the notice, or 10 business days if the amount is USD 100,000 or more. After that, failure-to-pay penalty runs on tax that was not shown on the return. | [Failure to pay penalty](https://www.irs.gov/payments/failure-to-pay-penalty) |
| CP501 / CP503 | Reminders of the unpaid balance. | No new rights. Act before CP504. | [Publication 594](https://www.irs.gov/pub/irs-pdf/p594.pdf) |
| CP504 | Notice of intent to levy under section 6331(d). The IRS can take a state tax refund and start looking for other assets. | Pay or arrange payment immediately. No CDP right yet: the IRS must still send the final notice with hearing rights before levying other assets. A Collection Appeals Program (CAP) appeal is available before action. | [CP504](https://www.irs.gov/individuals/understanding-your-cp504-notice); [CDP FAQs](https://www.irs.gov/appeals/collection-due-process-cdp-faqs) |
| LT11 or Letter 1058 | Final notice of intent to levy and right to a hearing. | CDP hearing request (Form 12153) within 30 days of the notice date. Later, but within one year: equivalent hearing only. | [Publication 594](https://www.irs.gov/pub/irs-pdf/p594.pdf); [Publication 1660](https://www.irs.gov/pub/irs-pdf/p1660.pdf) |
| Letter 3172 | Notice of federal tax lien filing and right to a hearing. | CDP request within the 30 days after the 5-business-day period that follows the lien filing (the letter states the date). | [CDP FAQs](https://www.irs.gov/appeals/collection-due-process-cdp-faqs); [Publication 1660](https://www.irs.gov/pub/irs-pdf/p1660.pdf) |
| CP59 (no return filed) | IRS has no record of a required return. | File the return immediately, or explain on Form 15103 why none is due. If the client does not file, the IRS may file a substitute return that may not allow deductions and exemptions the client could claim. | [CP59](https://www.irs.gov/individuals/understanding-your-cp59-notice); [Publication 594](https://www.irs.gov/pub/irs-pdf/p594.pdf) |
| Audit report with 30-day letter | Examination is finished and proposes changes. | Agree, or protest to Appeals by the date in the letter. No protest leads to a statutory notice of deficiency. | [Publication 5](https://www.irs.gov/pub/irs-pdf/p5.pdf) |

### CP2000: underreported income ([Topic 652](https://www.irs.gov/taxtopics/tc652))

A CP2000 comes from the Automated Underreporter. It is a proposal: the client can agree, partly agree or disagree.

1. Compare every item on the notice with the return and the wage-and-income transcript. A common false match is income that was reported, but on a different line or schedule.
2. Complete and sign the response form (both spouses for a joint return). Mark agree or disagree and attach a signed statement and documents for each item disputed.
3. If the notice is right but the client has other items to report, send Form 1040-X marked "CP2000" with the response.
4. Send it by the IRS document upload tool, fax or mail to the address on the notice, by the response date. To get more time, send an extension request with a reply.
5. If there is tax due, paying the proposed amount within 30 days stops more interest (the CP2000 interest runs to 30 days from the notice date). If the client cannot pay, they can ask for a payment plan and must still return the response form.

If the IRS gets no response, it sends a statutory notice of deficiency, and from then on the 90-day Tax Court clock controls. [Understanding your CP2000 notice](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice)

### Audits, Appeals and court ([Publication 5](https://www.irs.gov/pub/irs-pdf/p5.pdf))

- **Protest.** After an audit the IRS sends a report and a 30-day letter. A formal written protest is required if the proposed change in tax and penalties for any tax period is more than USD 25,000; if any one period is over USD 25,000, the formal protest must cover all periods. If the total for each period is USD 25,000 or less, a small case request is enough.
- **Deficiency notice.** If there is no agreement, the IRS issues the statutory notice of deficiency. The client then has 90 days (150 if the notice is addressed to a person outside the US) to petition the Tax Court without paying first. [26 U.S.C. 6213](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapB-sec6213.htm)
- **Small tax case.** If neither the deficiency in dispute nor any claimed overpayment exceeds USD 50,000 for any one year, the taxpayer can elect small tax case procedure. The decision cannot be appealed. [26 U.S.C. 7463](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap76-subchapC-partII-sec7463.htm)
- **Refund route.** Alternatively the client pays, files a refund claim, and sues in District Court or the Court of Federal Claims. Suit cannot start until 6 months after the claim (unless the IRS decides sooner) and must start within 2 years of the IRS mailing a notice of disallowance. [26 U.S.C. 6532](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapD-sec6532.htm)
- **Interview rights.** On advance request, the client may audio-record an in-person IRS interview at their own expense. A client who asks to consult a representative mid-interview must have the interview suspended (except under an administrative summons). A representative holding a written power of attorney can attend in place of the client unless the client is summonsed. [26 U.S.C. 7521](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7521.htm)
- **Assessment period.** The IRS generally has 3 years after the return was filed to assess. It has 6 years if gross income omitted is more than 25% of the gross income stated on the return, and no limit if no return was filed or the return was fraudulent. [26 U.S.C. 6501](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6501.htm)
- **Costs.** A taxpayer who substantially prevails may recover reasonable costs under section 7430, subject to conditions (including that the IRS position was not substantially justified and administrative remedies were exhausted). For fees incurred in calendar year 2026 the attorney-fee cap is USD 260 per hour. [26 U.S.C. 7430](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap76-subchapB-sec7430.htm); [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)

### The collection clock (CSED) ([IRM 5.1.19](https://www.irs.gov/irm/part5/irm_05-001-019))

The IRS has 10 years from the date of each assessment to collect it ([26 U.S.C. 6502](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6502.htm)). An audit addition or a penalty can carry its own date. After the CSED, the IRS can no longer pursue that assessment.

Events that suspend or extend the CSED:

| Event | Effect on the CSED |
| --- | --- |
| Offer in compromise | Suspended while the offer is pending, for 30 days after a rejection, and while a timely appeal of the rejection is in Appeals. For a joint liability, only for the spouse who made the offer. |
| Installment agreement request | Suspended while the request is pending, for 30 days after a rejection or termination, and while a timely appeal is in Appeals. |
| Timely CDP hearing request | Suspended from receipt of the request until it is withdrawn or the determination (including court appeals) is final. At least 90 days remain after a final determination. Not suspended for an equivalent hearing. |
| Bankruptcy | Suspended while the IRS is barred from collecting, plus six months. |
| Taxpayer outside the US for a continuous 6 months or more | Suspended while outside; the CSED cannot end sooner than six months after the return. |
| Innocent spouse request | For the requesting spouse: from filing until the 90-day Tax Court period ends or a Tax Court decision is final, plus 60 days. |
| Combat zone service | Suspended; the IRS example adds 180 days after the service ends. |
| Military deferment (Servicemembers Civil Relief Act) | Collection may be deferred up to 180 days if military service materially affects ability to pay; the CSED is suspended during military service and for 270 days afterwards. |
| Form 900 waiver | Extends the CSED; used only with some partial-payment installment agreements. |
| Suit to reduce the tax to judgment | Suspends during the suit; a judgment gives a new 20-year period. |

Overlapping suspensions run at the same time, not one after another. Read the CSED from the account transcript and check it against these events. Before choosing a route, compare the CSED with the proposed plan. An offer or a plan request suspends the clock; currently-not-collectible status is not among the suspension events listed in IRM 5.1.19. [Payment plans](https://www.irs.gov/payments/payment-plans-installment-agreements); [26 U.S.C. 6330](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap64-subchapD-partI-sec6330.htm); [26 U.S.C. 6503](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6503.htm)

### Paying over time ([Payment plans](https://www.irs.gov/payments/payment-plans-installment-agreements))

| Option | Who qualifies | Setup fee |
| --- | --- | --- |
| Pay in full now | Anyone | USD 0; stops further penalties and interest |
| Short-term plan (180 days or less) | Individuals owing less than USD 100,000 in combined tax, penalties and interest can apply online | USD 0 |
| Long-term plan, direct debit | Online for individuals owing USD 50,000 or less who have filed all required returns | USD 29 online; USD 107 by phone, mail or in person |
| Long-term plan, other payment method | Same | USD 69 online; USD 178 by phone, mail or in person |
| Low-income taxpayer (AGI at or below 250% of the federal poverty level) | Individuals in a long-term plan | Direct debit: fee waived. Otherwise USD 43, which may be reimbursed if conditions are met |
| Revise an existing plan | Anyone | USD 6 online; USD 89 by phone, mail or in person; USD 0 for changes to a direct-debit plan |
| Revise a plan, low-income taxpayer | Individuals meeting the low-income test | USD 6 online or USD 43 by phone, mail or in person, either of which may be reimbursed if conditions are met |

Rules to check:

- **Simple Payment Plan.** Individuals with USD 50,000 or less of assessed tax, penalties and interest who are current with all filing and payment requirements qualify without a collection information statement or lien determination. Businesses qualify at USD 50,000 or less without trust fund taxes, or USD 25,000 or less with trust fund taxes (USD 50,000 or less for an out-of-business sole proprietorship). The IRS says most taxpayers have up to 10 years to pay; a plan that would run past the CSED is a partial-payment case. [Simple Payment Plans](https://www.irs.gov/payments/simple-payment-plans-for-individuals-and-businesses)
- **Over USD 50,000.** Either pay the balance down to USD 50,000 or less first, or apply with Form 9465 and, where its instructions require, Form 433-F, and expect the IRS to set the payment from income and allowable expenses.
- **Partial payment plan.** If the client cannot pay in full by the collection statute expiration date (generally 10 years), they may qualify for a partial payment installment agreement. It needs full financial disclosure. [Publication 594](https://www.irs.gov/pub/irs-pdf/p594.pdf)
- **While a request is pending,** and for 30 days after a rejection or termination (plus any appeal), the IRS generally will not levy.
- **Penalty during a plan.** For an individual who filed on time, the failure-to-pay penalty drops to 0.25% a month while an approved plan is in place. [Failure to pay penalty](https://www.irs.gov/payments/failure-to-pay-penalty)
- **Default.** Pay at least the monthly amount, file and pay all later returns on time; a reinstatement fee may apply after default. Refunds are applied to the debt until it is paid. A notice of intent to terminate can be appealed within 30 days. [Publication 1660](https://www.irs.gov/pub/irs-pdf/p1660.pdf)

### Currently not collectible ([IRS: temporarily delay collection](https://www.irs.gov/businesses/small-businesses-self-employed/temporarily-delay-the-collection-process))

If the client cannot pay because of financial hardship, the IRS may place the account in currently-not-collectible (CNC) status. It may ask for Form 433-F, 433-A or 433-B and proof of income, living expenses, bank accounts and assets.

- Most collection stops, but the debt is not forgiven. Penalties and interest keep accruing.
- The IRS may file a lien, apply future refunds to the debt, review the finances later and resume collection if the client's ability to pay improves. There is no fixed period.
- CNC suits clients with low fixed income and no equity, especially near the CSED.

### Offer in compromise ([IRS: offer in compromise](https://www.irs.gov/payments/offer-in-compromise))

An offer settles the debt for less than the full amount. The IRS generally approves an offer when it represents the most the IRS can expect to collect within a reasonable period.

- **Eligibility.** All required returns filed and estimated payments made; not in an open bankruptcy; a valid extension for the current-year return if applying for that year; employers must have made deposits for the current and past 2 quarters.
- **Grounds.** Doubt as to collectibility or effective tax administration on Form 656; doubt as to liability on Form 656-L, never submitted at the same time as the others. [Form 656-B](https://www.irs.gov/pub/irs-pdf/f656b.pdf)
- **Fee and payments.** USD 205 application fee, non-refundable. Lump-sum offer: 20% of the offer with the application, the rest in five or fewer payments within 5 months of acceptance. Periodic offer: first payment with the application, then monthly while the IRS considers it; the balance is paid within 6 to 24 months.
- **Low-income certification.** An individual who meets the low-income certification guidelines in Form 656-B sends no fee and no initial or monthly payments while the offer is considered.
- **Minimum offer (Form 656-B worksheet).** Equity in assets, plus remaining monthly income times 12 for an offer paid in 5 months or less, or times 24 for an offer paid in 6 to 24 months.
- **While pending.** Other collection is suspended, a lien may be filed, the collection period is extended, and payments are applied to the debt. If the IRS makes no determination within two years of receipt (not counting any appeal), the offer is accepted automatically.
- **Refunds.** The IRS may keep refunds for returns assessed before the offer is accepted.
- **Rejected offer.** Appeal within 30 days on Form 13711.
- **After acceptance.** The client must file and pay every tax on time for five years after acceptance, or the IRS may default the offer and reinstate the original debt less payments, with interest and penalties. Liens are not released until the offer terms are met.

### Liens and levies ([Understanding a federal tax lien](https://www.irs.gov/businesses/small-businesses-self-employed/understanding-a-federal-tax-lien))

- **Lien.** Attaches to all the client's assets and to assets acquired later. Paying in full gets it released within 30 days. Discharge frees one property; subordination lets another creditor go first; withdrawal removes the public notice (the debt remains).
- **Withdrawal with a direct-debit plan (Fresh Start).** Available if the client owes USD 25,000 or less (or pays down to that first), the direct-debit plan pays in full within 60 months or before the CSED, whichever is earlier, the client is otherwise compliant, has made three consecutive direct-debit payments, and has never defaulted on a direct-debit plan. Apply on Form 12277.
- **Bank levy.** The bank must hold deposits for 21 days after the levy before sending them to the IRS. Use that window to resolve ownership disputes or a release. [26 U.S.C. 6332](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap64-subchapD-partII-sec6332.htm)
- **Wage and federal-payment levies.** A wage levy continues until the debt is paid, other arrangements are made, the collection period ends or the levy is released; a minimum exempt amount stays with the taxpayer. The Federal Payment Levy Program can generally take up to 15% of federal payments such as Social Security. [Publication 594](https://www.irs.gov/pub/irs-pdf/p594.pdf)
- **Property exempt from levy for 2026:** household goods and personal effects up to USD 11,980; books and tools of the taxpayer's trade up to USD 5,990. [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)
- **Passport ([IRS: passport revocation or denial](https://www.irs.gov/businesses/small-businesses-self-employed/revocation-or-denial-of-passport-in-cases-of-certain-unpaid-taxes)).** For 2026 a "seriously delinquent tax debt" is legally enforceable, unpaid federal tax debt (with assessed penalties and interest) totaling more than USD 66,000, where the IRS has filed a lien notice and administrative remedies have lapsed or been exhausted, or the IRS has issued a levy. Excluded: debts being paid on time under an approved installment agreement or an accepted offer, debts with a timely requested levy CDP hearing, and debts suspended by an innocent spouse request. The IRS also does not certify accounts in hardship CNC status, pending plan or offer requests, bankruptcy, identity-theft victims or federally declared disaster areas, and postpones certification for combat-zone service. The State Department can then refuse or revoke the passport.
- **Principal residence.** It cannot be levied unless a US district court judge or magistrate approves the levy in writing. [26 U.S.C. 6334](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap64-subchapD-partII-sec6334.htm)
- **Release.** The IRS releases a levy if, among other grounds, it creates economic hardship or was issued improperly. Hardship cases can also go to the Taxpayer Advocate Service. [Publication 594](https://www.irs.gov/pub/irs-pdf/p594.pdf)

### Collection Due Process and the Collection Appeals Program ([Publication 1660](https://www.irs.gov/pub/irs-pdf/p1660.pdf))

- **CDP hearing.** Request on Form 12153 within 30 days of the LT11 or Letter 1058 (or within the Letter 3172 lien window). Raise every issue: collection alternatives (plan, offer, CNC), lien withdrawal, spousal defences, and the underlying tax only where the client had no earlier opportunity to dispute it. For alternatives, attach Form 433-A or 433-B. [CDP FAQs](https://www.irs.gov/appeals/collection-due-process-cdp-faqs)
- **Effect.** A timely levy CDP request suspends that levy action and the CSED while the hearing and appeals are pending. [26 U.S.C. 6330](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap64-subchapD-partI-sec6330.htm)
- **Tax Court review.** The client may petition the Tax Court within 30 days of the Appeals determination. Publication 594 says the court may consider a later petition only if the client was diligent and the delay came from extraordinary circumstances beyond their control; do not plan on it. [Publication 594](https://www.irs.gov/pub/irs-pdf/p594.pdf)
- **Equivalent hearing.** A request after the 30 days but within one year of the levy notice (for a lien: one year plus 5 business days after the lien filing) gets an equivalent hearing with Appeals. There is no Tax Court review, and the CSED is not suspended.
- **Collection Appeals Program (CAP), Form 9423.** Faster; available before or after a lien, levy or seizure, and for rejected, modified or terminated installment agreements. There is no Tax Court review of a CAP decision. For some actions the client must first ask for a conference with a Collection manager.

### Penalties and interest

| Penalty | Rate and rule | Source |
| --- | --- | --- |
| Failure to file (section 6651(a)(1)) | 5% of unpaid tax for each month or part month late, up to 25%. If the return is more than 60 days late, the minimum is the lesser of a fixed amount or 100% of the tax: USD 525 for Form 1040 and 1120 returns due after 31 December 2025 (this includes 2025 returns); USD 535 for income tax returns required to be filed in 2027 (2026 returns). | [Failure to file penalty](https://www.irs.gov/payments/failure-to-file-penalty); [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Failure to pay (section 6651(a)(2), (a)(3)) | 0.5% of unpaid tax for each month or part month, up to 25%. Reduced to 0.25% during an approved plan for an individual who filed on time. Rises to 1% a month if the tax is not paid within 10 days after a notice of intent to levy. | [Failure to pay penalty](https://www.irs.gov/payments/failure-to-pay-penalty) |
| Both in the same month | The failure-to-file penalty is reduced by the failure-to-pay penalty: 4.5% plus 0.5% instead of 5%. | [Failure to pay penalty](https://www.irs.gov/payments/failure-to-pay-penalty) |
| Fraudulent failure to file (section 6651(f)) | 15% a month, up to 75%. | [26 U.S.C. 6651](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm) |
| Accuracy-related (section 6662) | 20% of the underpayment due to negligence or a substantial understatement. Individuals: the understatement exceeds the greater of 10% of the tax required to be shown or USD 5,000 (the IRS applies 5% instead of 10% if the return claims the section 199A deduction). Corporations other than S corporations and personal holding companies: exceeds the lesser of 10% of the tax required to be shown (or, if greater, USD 10,000) or USD 10,000,000. | [Accuracy-related penalty](https://www.irs.gov/payments/accuracy-related-penalty); [26 U.S.C. 6662](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm) |
| Valuation misstatements | Substantial valuation misstatement (value or adjusted basis claimed is 150% or more of the correct amount): 20%. Gross valuation misstatement (200% or more): 40% on that portion. | [26 U.S.C. 6662](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm) |
| Civil fraud (section 6663) | 75% of the part of the underpayment due to fraud. | [26 U.S.C. 6663](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6663.htm) |
| Interest (section 6621) | Federal short-term rate plus 3 percentage points, set each quarter and compounded daily. The underpayment rate is 7% for January to March, July to September and October to December 2026, and 6% for April to June 2026. By law interest cannot be removed or reduced unless the penalty is removed or reduced. | [Quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates); [Failure to file penalty](https://www.irs.gov/payments/failure-to-file-penalty) |

### Penalty relief ([Administrative penalty relief](https://www.irs.gov/payments/penalty-relief-due-to-first-time-abate-or-other-administrative-waiver))

Covers failure-to-file (sections 6651(a)(1), 6698(a)(1), 6699(a)(1)), failure-to-pay (section 6651(a)(2) and (a)(3)) and failure-to-deposit (section 6656) penalties, whatever the amount. It does not cover accuracy-related or fraud penalties; for those, no penalty applies to any portion of an underpayment where the client shows reasonable cause and good faith, except for portions from transactions lacking economic substance (section 6662(b)(6)) or deductions disallowed under section 6662(b)(10). Reportable transaction understatements (section 6662A) have a separate, stricter reasonable-cause test that requires adequate disclosure ([26 U.S.C. 6664(c) and (d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6664.htm)).

- **Timely compliance history.** The same type of return was filed on time for the prior three years (or 12 consecutive quarters), and either no penalty was assessed other than the estimated tax penalty, or a penalty was later removed for reasonable cause or IRS error. Businesses also: failure-to-deposit not waived four or more times in that period, and no penalty for avoiding EFTPS.
- **Automatic Exemption from Penalty (AEP), from summer 2026.** For 2025 tax-year returns (Forms 1040, 1065, 1120) and 2026 quarterly returns (Forms 940, 941, 943, 944, 945, CT-1), and later ones, a late original return or payment from a taxpayer with that history is not assessed the penalty, and failure-to-pay does not accrue. No request is needed; the IRS sends a letter. If a penalty was assessed anyway, contact the IRS.
- **First Time Abate (FTA).** For periods before AEP, and for 2025 tax-year or 2026 quarterly returns that were not considered for AEP, the client must ask: by phone at the number on the notice, by written statement, or on Form 843. The penalty is assessed first and then removed, and failure-to-pay may keep accruing until the tax is paid. IRM 20.1.1.3.3.2.1 describes FTA as relief the first time a taxpayer is subject to these penalties for a single return. [IRM 20.1.1](https://www.irs.gov/irm/part20/irm_20-001-001r)
- **Not available for** returns filed once or infrequently (event-based), the daily delinquency penalty, or information reporting that depends on another filing.
- **Reasonable cause** is the fallback if the client does not qualify: show good faith and why the obligation could not be met. Document the facts and dates.
- **Erroneous written IRS advice.** The IRS must abate any penalty attributable to erroneous written advice from an IRS employee if the advice answered a specific written request from the client, the client reasonably relied on it, and the penalty did not result from the client giving inadequate or inaccurate information. Oral advice does not qualify. [26 U.S.C. 6404(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap65-subchapA-sec6404.htm)

### Innocent spouse relief ([IRS: innocent spouse relief](https://www.irs.gov/individuals/innocent-spouse-relief))

Both spouses on a joint return are liable for the whole tax, even after divorce, even if the divorce decree says otherwise, and even if one spouse earned all the income. Form 8857 asks for all three types of relief at once.

- **Innocent spouse relief (section 6015(b)).** An understatement caused by the other spouse's errors that the requesting spouse did not know about. Not available if the requester actually knew, or a reasonable person would have known, of the errors (abuse victims have an exception).
- **Separation of liability (section 6015(c)).** For spouses who are divorced or legally separated, or who were not members of the same household at any time in the 12 months ending on the date the election is filed: pay only their share of the understatement.
- **Equitable relief (section 6015(f)).** When neither of the others applies and holding the requester liable would be unfair; covers underpayments as well as understatements.
- **Deadlines.** (b) and (c): no later than 2 years after the IRS began collection activities against the requesting spouse. (f): for an unpaid balance, before the collection period under section 6502 ends (generally 10 years, subject to suspension); for a refund, within 3 years after the return was filed or 2 years after the tax was paid, whichever is later. [26 U.S.C. 6015](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartB-sec6015.htm); [Equitable relief](https://www.irs.gov/individuals/equitable-relief)
- **Not available** for tax on the requester's own income (community-property cases aside), household employment taxes, individual shared responsibility payments, business taxes or trust fund recovery penalties; or where the requester signed an offer or a closing agreement for the same taxes, a court made a final decision denying relief, or the requester took part in a related court proceeding and did not ask for relief.
- **Appeal and Tax Court.** Appeal an IRS decision within 30 days of the determination letter. A Tax Court petition is due within 90 days after the final determination letter is mailed, and can be filed if the IRS has not decided 6 months after the request.
- **Injured spouse** is different: Form 8379 recovers the non-debtor spouse's share of a joint refund taken for the other spouse's debt.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Balance exactly USD 50,000 | Qualifies for the online long-term plan and a Simple Payment Plan ("USD 50,000 or less"). |
| Short-term plan at exactly USD 100,000 | Not available online: the test is "less than USD 100,000". |
| Audit change of exactly USD 25,000 for each period | Small case request is enough; over USD 25,000 in any period needs a formal protest for all periods. |
| Deficiency of exactly USD 50,000 in one year | Small tax case election allowed; over USD 50,000 for any one year is not. |
| CDP request after the 30 days | Equivalent hearing only: no Tax Court, no CSED suspension. |
| CP504 received | Not a CDP notice. Call, arrange payment, or use CAP. |
| Unfiled returns | No online long-term plan, and no offer. File first. |
| Offer while in open bankruptcy | Not eligible. Refer to bankruptcy counsel. |
| Equivalent hearing or CAP decision | No Tax Court review. |
| Innocent spouse relief for tax on own income | Not available (community-property exceptions only). |
| 2025 return filed late in 2026 | AEP can apply (2025 is its first tax year); failure to file minimum USD 525 |
| 2026 return filed late in 2027 | Failure to file minimum USD 535 |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Notice date | Treat the earliest plausible date as the notice date and file now; get the notice |
| Assessment date for the CSED | Do not compute the CSED from the tax year; pull the account transcript |
| Whether all returns are filed | Assume not until the transcripts confirm it; no plan or offer until they are |
| Client's address outside the US | Use the 90-day and 30-day periods, not 150 or 60, until residence is confirmed |
| Compliance history for AEP or FTA | Assume none qualifies until the prior three years are checked on the transcripts |
| Financial information for an offer or CNC | Do not estimate; get Form 433-A or 433-F with documents |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| LT11, Letter 1058 or Letter 3172 in hand | 30-day CDP window; after that, equivalent hearing only |
| Statutory notice of deficiency | 90-day Tax Court deadline that the IRS cannot extend |
| Balance near or over USD 66,000 with a lien or levy | Passport certification for 2026 |
| Bank levy received | 21-day window before the bank pays the IRS |
| CSED within 2 to 3 years | Compare partial-pay plan, CNC and offer against simply running out the clock |
| Contact from Criminal Investigation or a special agent | Stop; refer to a criminal tax attorney |

## Worked cases

**Case 1: CP2000, income already reported.** A CP2000 proposes tax on a 1099-NEC the client says was included in Schedule C gross receipts. Match the payer's deposits to the ledger and the Schedule C total. Mark "disagree", attach a signed statement, the ledger report and bank entries, and send it within 30 days of the notice date. Result: the IRS closes the notice with no change, or issues a statutory notice of deficiency that starts the 90-day Tax Court clock. [Topic 652](https://www.irs.gov/taxtopics/tc652)

**Case 2: choosing a payment plan ([Payment plans](https://www.irs.gov/payments/payment-plans-installment-agreements)).** An individual, all returns filed, owes USD 38,000 in assessed tax, penalties and interest. That is USD 50,000 or less, so they can apply online for a long-term plan, and a direct-debit plan set up online costs USD 29. A second client owes USD 62,000: to use the online route they must first pay down USD 12,000; otherwise they apply on Form 9465 (with Form 433-F if required), and a direct-debit plan set up by mail costs USD 107.

**Case 3: late filing and payment penalties ([Failure to file penalty](https://www.irs.gov/payments/failure-to-file-penalty)).** An individual's 2025 return was due 15 April 2026, had no extension, and was filed on 10 July 2026 showing USD 10,000 of tax, none paid. It is 3 months late and more than 60 days late. The client had a failure-to-file penalty on the 2023 return, so neither AEP nor FTA applies. Failure to pay for 3 months at 0.5%: USD 150. Failure to file for 3 months at 4.5% (5% reduced by the 0.5% failure-to-pay each month): USD 1,350. Minimum penalty test: the lesser of USD 525 and 100% of the tax is USD 525, below USD 1,350, so the minimum does not change the result. Penalties so far: USD 1,500, plus interest. Failure-to-pay keeps running until the tax is paid.

```oa-check
name: Late 2025 return, failure to file and pay (filed July 2026)
inputs:
  tax: 10000
  months: 3
  ftf_minimum: 525
steps:
  - ftp: tax * 0.005 * months
  - ftf_computed: tax * 0.045 * months
  - ftf_floor: min(ftf_minimum, tax)
  - ftf: max(ftf_computed, ftf_floor)
  - total: ftp + ftf
expected:
  ftp: 150.00
  ftf_computed: 1350.00
  ftf_floor: 525.00
  ftf: 1350.00
  total: 1500.00
```

**Case 4: CDP deadline ([Publication 594](https://www.irs.gov/pub/irs-pdf/p594.pdf)).** An LT11 is dated 5 October 2026. Form 12153 must be sent within 30 days of the notice date, by 4 November 2026. A request sent on 5 November 2026 gets only an equivalent hearing, which can be requested until 5 October 2027.

**Case 5: Tax Court deadline ([26 U.S.C. 6213](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapB-sec6213.htm)).** A statutory notice of deficiency is mailed on 1 September 2026 to a client in Ohio: the petition is due 30 November 2026 (90 days). Had it been addressed to the client in Portugal: 29 January 2027 (150 days). The petition deadline printed on the notice controls if it is later.

**Case 6, a decision: lump-sum offer or payment plan ([Offer in compromise](https://www.irs.gov/payments/offer-in-compromise)).** A client who owes USD 62,000 offers USD 20,000 as a lump sum. The application goes with the USD 205 fee and 20% of the offer, USD 4,000. The other USD 16,000 is paid in five or fewer payments within 5 months of acceptance. Cash needed up front: USD 4,205, and none of it is refunded if the offer is rejected (the 20% is applied to the debt). If the client meets the low-income certification guidelines, neither the fee nor the USD 4,000 is sent. Choose the offer only if USD 20,000 is at least the reasonable collection potential on the Form 656-B worksheet; otherwise expect rejection and use a plan.

```oa-check
name: Lump-sum offer in compromise, cash with the application
inputs:
  offer: 20000
  fee: 205
  debt: 62000
steps:
  - down_payment: offer * 0.20
  - cash_with_application: down_payment + fee
  - balance_after_acceptance: offer - down_payment
  - amount_forgiven_if_accepted: debt - offer
expected:
  down_payment: 4000.00
  cash_with_application: 4205.00
  balance_after_acceptance: 16000.00
  amount_forgiven_if_accepted: 42000.00
```

**Case 7: CSED after a rejected offer ([IRM 5.1.19](https://www.irs.gov/irm/part5/irm_05-001-019)).** Tax assessed on 1 June 2020 has a base CSED of 1 June 2030. An offer was pending from 1 March 2025 until it was rejected on 31 August 2025, and the client did not appeal. The CSED is suspended for the pending period plus the 30-day appeal window, which moves it roughly seven months, to about the end of December 2030. Take the exact date from the transcript (TC 480 and TC 481).

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-COL-CI | Any contact from IRS Criminal Investigation, a special agent, or facts suggesting fraud | Refer to a criminal tax attorney before anyone speaks to the IRS |
| R-COL-BK | Bankruptcy, filed or planned | Refer to bankruptcy counsel (it suspends the collection clock and changes which taxes survive) |
| R-COL-TFRP | Trust fund recovery penalty (section 6672) defence, employment-tax liability disputes, whistleblower claims | Refer to a specialist |
| R-COL-INTL | International information-return penalties, FBAR and FATCA penalties | Refer to an international tax specialist |
| R-COL-STATE | State tax collection | Outside this skill; follow the state's own procedures |
| R-COL-COURT | Tax Court litigation beyond filing a timely petition, and refund suits | Refer to a practitioner admitted to the relevant court |
| R-COL-PERJURY | The client wants to leave assets or income off a collection information statement | Refuse: the statements are signed under penalty of perjury |

## Filing and payment

| Action | Form or channel | Deadline |
| --- | --- | --- |
| Authorise representative | Form 2848 or 8821 | Before calling the IRS for the client |
| Answer CP2000 | Response form, upload tool, fax or mail | 30 days from the notice (60 days if outside the US) |
| Abate math-error assessment | Written request | 60 days after the notice |
| Protest audit report | Formal protest or small case request | Date in the 30-day letter |
| Petition Tax Court on a deficiency | Petition to the US Tax Court | 90 days from mailing (150 days if addressed outside the US) |
| Request CDP hearing | Form 12153 | 30 days from the LT11 or Letter 1058; the Letter 3172 date for liens |
| Equivalent hearing | Form 12153 | One year from the levy notice |
| Petition Tax Court after CDP | Petition | 30 days from the Appeals determination |
| Payment plan | Online account, or Form 9465 (with 433-F if required) | Any time; before a levy if possible |
| Appeal plan termination | Publication 1660 procedures | 30 days from the notice of intent to terminate |
| Offer in compromise | Form 656 with Form 433-A (OIC) or 433-B (OIC), fee and payment | Any time, once all returns are filed |
| Appeal rejected offer | Form 13711 | 30 days from rejection |
| Innocent spouse | Form 8857 | 2 years after collection began for (b) and (c); collection or refund period for (f) |
| Penalty relief (FTA or reasonable cause) | Phone, written statement or Form 843 | As soon as the penalty notice arrives |
| Bank levy | Call the number on the levy; Taxpayer Advocate for hardship | Within the 21 days the bank holds the funds |

**2025 returns filed in 2026.** Extended 2025 individual returns are due 15 October 2026. For a 2025 return filed more than 60 days late, the failure-to-file minimum is USD 525, and AEP can apply (2025 is its first year). Returns for 2026, filed in 2027, carry a USD 535 minimum. [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)

## Completion checklist

- [ ] Every notice logged with number, date, tax year and deadline; the earliest deadline is calendared.
- [ ] Form 2848 or 8821 filed and posted.
- [ ] Account, wage-and-income and return transcripts pulled for all open years.
- [ ] Assessment date and CSED computed per year, with suspensions checked.
- [ ] Unfiled returns filed; current-year payments on track.
- [ ] Disputed tax challenged by the correct route before its deadline.
- [ ] AEP, FTA and reasonable cause checked for every failure-to-file, failure-to-pay and deposit penalty.
- [ ] Collection route chosen and compared against the CSED; fees and payments taken from the current IRS page.
- [ ] Proof of filing kept for every deadline-sensitive submission.
- [ ] Follow-up dates calendared: IRS decisions, 30-day appeal windows, plan terms, 5-year offer compliance.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for the levy exemptions (USD 11,980 and USD 5,990), section 3.52 (USD 535), section 3.60 (USD 66,000) and section 3.61 (USD 260 per hour). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| IRS payment plans page. Read for the online thresholds (USD 50,000, less than USD 100,000) and the fee table. | https://www.irs.gov/payments/payment-plans-installment-agreements | 2026-11-13 |
| IRS Simple Payment Plans page. Read for USD 50,000 and USD 25,000 and "up to 10 years". | https://www.irs.gov/payments/simple-payment-plans-for-individuals-and-businesses | 2026-11-13 |
| IRS offer in compromise page. Read for the USD 205 fee and 20% with a lump-sum offer. | https://www.irs.gov/payments/offer-in-compromise | 2026-11-13 |
| IRS failure to file penalty page. Read for the minimum penalty table (USD 525 for returns due after 31 December 2025). | https://www.irs.gov/payments/failure-to-file-penalty | 2026-11-13 |
| IRS failure to pay penalty page. Read for 0.5%, 0.25%, 1%, 4.5% plus 0.5%, and 21 calendar days or 10 business days. | https://www.irs.gov/payments/failure-to-pay-penalty | 2026-11-13 |
| IRS quarterly interest rates page. Read for the 2026 underpayment rates by quarter. | https://www.irs.gov/payments/quarterly-interest-rates | 2026-11-13 |
| IRS administrative penalty relief page. Read for FTA and AEP (2025 tax year returns and 2026 quarterly returns). | https://www.irs.gov/payments/penalty-relief-due-to-first-time-abate-or-other-administrative-waiver | 2026-11-13 |
| IRS passport revocation or denial page. Read for the USD 66,000 2026 threshold and the exclusions. | https://www.irs.gov/businesses/small-businesses-self-employed/revocation-or-denial-of-passport-in-cases-of-certain-unpaid-taxes | 2026-11-13 |
| IRS Topic 652. Read for the 30 and 60 day CP2000 response periods. | https://www.irs.gov/taxtopics/tc652 | 2026-11-13 |
| IRS Collection Due Process FAQs. Read for CDP timing and the lien window. | https://www.irs.gov/appeals/collection-due-process-cdp-faqs | 2026-11-13 |
| IRM 5.1.19. Read for the CSED and suspension events. | https://www.irs.gov/irm/part5/irm_05-001-019 | 2026-11-13 |
| Publication 5, Publication 594, Publication 1660, Form 656-B. Read for protests, notices, CDP and CAP, and offer terms. | https://www.irs.gov/pub/irs-pdf/p594.pdf | 2026-11-13 |
| 26 U.S.C. 6213 (govinfo). Read for (a) 90 and 150 days and (b) the 60-day math-error request. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapB-sec6213.htm | 2026-11-13 |
| 26 U.S.C. 6502 (govinfo). Read for (a) 10 years after assessment. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6502.htm | 2026-11-13 |
| 26 U.S.C. 6332 (govinfo). Read for (c) the 21-day bank hold. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap64-subchapD-partII-sec6332.htm | 2026-11-13 |
| 26 U.S.C. 6651, 6662, 6663, 6664 (govinfo). Read for the penalty rates, the USD 5,000 and 10% test, 75% fraud and reasonable cause. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm | 2026-11-13 |
| 26 U.S.C. 7463 (govinfo). Read for the USD 50,000 small tax case limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap76-subchapC-partII-sec7463.htm | 2026-11-13 |
| 26 U.S.C. 6015 (govinfo). Read for the 2-year election period in (b) and (c). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartB-sec6015.htm | 2026-11-13 |
| 26 U.S.C. 6404 (govinfo). Read for (f) erroneous written advice. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap65-subchapA-sec6404.htm | 2026-11-13 |

Not yet confirmed: the IRS interest rate for January to March 2027 is not yet announced; the IRS pages for CP504, CP59, CP3219A, liens, innocent spouse, equitable relief, accuracy-related penalty and IRM 20.1.1 were not re-read this session and are carried from the 2026-10-16 version; the 2027 payment plan and offer fees are not yet published.
