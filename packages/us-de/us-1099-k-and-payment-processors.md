---
name: us-1099-k-and-payment-processors
description: "Tier 2 US federal content skill for Form 1099-K reporting under IRC §6050W for tax year 2025. Covers the current federal TPSO threshold restored by OBBBA: more than $20,000 and more than 200 transactions, reconciliation between gross 1099-K amounts and Schedule C / Schedule 1 / Schedule D reporting, IRS-recommended treatment of personal items sold at loss (Schedule 1 Lines 8z + 24z offset), hobby vs business §183 determination, PayPal/Venmo Friends-and-Family vs Goods-and-Services categorization, marketplace facilitator sales-tax exclusion under Wayfair, ride-share and content-creator double-form scenarios (1099-K + 1099-NEC), the 2025 1099-DA digital asset transition, and IRS CP2000 matching defense."
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Form 1099-K: payment cards, payment apps and marketplaces (tax year 2026)

Figures are for tax year 2026 (Forms 1099-K for calendar 2026, furnished in early 2027). A short dated section below covers **2025 returns**, which are still being filed on extension until 15 October 2026. This Guide is written from the payee's side: an individual, sole proprietor or single-member LLC who received a Form 1099-K and must reconcile it to Form 1040. It does not cover an issuer's own filing duties, entity returns (Forms 1065, 1120, 1120-S), or which Schedule C deductions are allowed.

## Scope and who it's for

- Anyone who received a Form 1099-K from a card processor, a payment app or an online marketplace, or who expects one, for 2026 or 2025.
- Anyone who got a Form 1099-K they believe is wrong: gifts, reimbursements, personal items sold at a loss, a duplicate, or the wrong taxpayer ID.
- Anyone who received a CP2000 notice proposing tax on Form 1099-K amounts.
- The rule that drives everything: the form reports **gross payments**, not income. "Just because a payment is reported on Form 1099-K doesn't mean it's taxable", and income is reportable even without a form. [What to do with Form 1099-K](https://www.irs.gov/businesses/what-to-do-with-form-1099-k)

## Ask the client first

- Every Form 1099-K received for the year, **whatever the amount**, plus each platform's annual earnings or transaction statement. Also every Form 1099-NEC, 1099-MISC and 1099-DA.
- What each account was used for: selling goods, providing services, renting property, selling personal belongings, or receiving gifts and shared-cost repayments.
- For personal items sold: the item, what the client paid, and the sale price, item by item. A mix of gains and losses cannot be netted.
- Whether the activity is a business run for profit or a hobby: books, a separate account, time spent, profit history.
- Refunds, returns, chargebacks, platform and processor fees, shipping charged, cash back given, and sales tax collected. For sales tax, also who the tax is imposed on under state law.
- Whether the client gave the platform a correct SSN, ITIN or EIN, and whether Box 4 shows federal tax withheld.
- Whether any card terminal or account was shared with another person, or changed owner or entity during the year.
- Any CP2000 or other IRS notice for this or an earlier year that relates to Form 1099-K.

## The method, step by step

1. **Collect and check each form.** Check the payee name and TIN, the filer, Box 1a, and Box 4. If the TIN or the Box 1a amount is wrong, ask the filer (not the IRS) for a corrected form. Do not wait for it before filing. [Correcting a Form 1099-K](https://www.irs.gov/businesses/what-to-do-with-form-1099-k)
2. **Split Box 1a by what each payment was.** The categories are: business or rental receipts; hobby receipts; personal items sold at a gain; personal items sold at a loss; and amounts that are not the client's income at all (gifts, reimbursements, a duplicate, someone else's sales). Use the platform statement and the client's records. The form itself does not show this split.
3. **Report each slice in its own place.** Use the table in "Where each slice goes" below. Business gross receipts go on Schedule C line 1, gross before fees. Returns and allowances go on line 2. Fees and other costs go in expenses.
4. **Bridge the forms to the return.** Total every information return (1099-K, 1099-NEC, 1099-MISC). Then show, line by line, where each dollar went and why any amount is excluded (a duplicate, sales tax imposed on the buyer, a personal loss item, an error). Add income that no form reported. Keep the bridge in the file, and attach a short statement to the return when the forms total more than what the return shows.
5. **Claim any backup withholding** shown in Box 4 as federal income tax withheld.
6. **File and keep the evidence.** Keep the forms, the platform statements, the correspondence asking for corrected forms, and the purchase records for personal items. If a CP2000 arrives, answer by the date on the notice using the same bridge.

## Thresholds and figures by year

| Point | Rule | Years and source |
|---|---|---|
| Payment cards (credit, debit, gift cards) | No threshold. A payment card processor reports whatever the volume, "if you received $0.01 of payments from a payment card transaction". | All years. [FAQ Q2](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information) |
| Payment apps and online marketplaces (TPSOs) | Reporting is required only if gross payments for goods or services exceed $20,000 **and** the number of transactions exceeds 200. Both tests must be met, and both are "more than". | Calendar 2022 onward. [26 U.S.C. §6050W(e)](https://www.law.cornell.edu/uscode/text/26/6050W) |
| Why 2022 onward | P.L. 119-21 §70432 (signed 4 July 2025) rewrote §6050W(e) "as if included in" ARPA §9674, which applied to returns for calendar years beginning after 31 December 2021. So the ARPA figure of $600 never took effect. The IRS's administrative transition thresholds for 2022-2026 no longer set the rule. | Retroactive to 2022. [§6050W effective-date notes](https://www.law.cornell.edu/uscode/text/26/6050W) |
| Voluntary and state forms | A TPSO may still send a form below the federal threshold, and "your state may have a lower reporting threshold". | All years. [FAQ Q2, Q5](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information) |
| Box 1a | "Gross amount" is taken "without regard to any adjustments for credits, cash equivalents, discount amounts, fees, refunded amounts, shipping amounts, or any other amounts." | All years. [Form 1099-K instructions](https://www.irs.gov/instructions/i1099k) |
| New Boxes 1c and 1d | Cash tips included in Box 1a, and the tipped occupation code, as required by P.L. 119-21 §70201. | 2026 forms. [Form 1099-K instructions (12/2026)](https://www.irs.gov/instructions/i1099k) |
| Backup withholding | 24% on reportable payments when the payee's TIN is missing or incorrect. For TPSO payments, this applies only once the year's threshold is exceeded (see "Backup withholding"). | TPSO rule from calendar 2025. [Backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding) |

"Below the threshold" does **not** mean "no form" and does not mean "not taxable". A client under $20,000 may still hold a card-processor form, a voluntary TPSO form or a state-driven form, and must report the income regardless. [Understanding your Form 1099-K](https://www.irs.gov/businesses/understanding-your-form-1099-k)

A caution about the IRS's own wording: the 2025 Form 1040 instructions say "payment card companies, payment apps, and online marketplaces" need send a form only above the threshold. The statute and FAQ Q2 limit the threshold to TPSOs, and card processors have none. Follow the statute. [2025 Form 1040 instructions](https://www.irs.gov/instructions/i1040gi); [FAQ Q2](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information)

## Where each slice goes

| Slice of Box 1a | Where it goes | Condition or boundary |
|---|---|---|
| Sales of goods or services in a trade or business (gig work, freelance, online shop) | Schedule C line 1, gross. Returns and allowances go on line 2. Platform and processor fees are expenses. | A partnership or corporation reports on its own return. A form in the owner's name and SSN for an entity's income needs to be corrected. |
| Rental receipts | Schedule E or Schedule C, depending on the activity | One terminal serving two businesses: report each business's receipts on its own schedule. |
| Hobby receipts (not engaged in for profit) | Schedule 1 line 8j | No expense deduction (see "Hobby or business"). Not self-employment income. |
| Personal item sold at a **gain** | Form 8949 and Schedule D | The gain is sale price minus what the client paid. Short or long term depends on holding period. |
| Personal item sold at a **loss** | Entry space at the top of Schedule 1, or Form 8949 with code "L" | The loss is not deductible. The entry only zeroes out the reported amount. |
| Gifts, repayments of shared costs, someone else's payments, a duplicate form | Entry space at the top of Schedule 1, as an amount "included in error" | Ask the filer for a corrected form first, and file anyway. |
| Cash back given at a card terminal | Not gross receipts and not an expense | Keep the cash-back records. |
| Sales tax **imposed on the buyer** that the seller collected and paid over | Not in gross receipts and not deductible | If the state lets the seller keep part of it, that part is Schedule C line 6 income. |
| Sales tax **imposed on the seller** | In gross receipts on line 1, and deductible on line 23 | Check the state law. The platform label does not decide it. |

Sources: [What to do with Form 1099-K](https://www.irs.gov/businesses/what-to-do-with-form-1099-k); [Schedule C instructions (2025), lines 1, 2, 6 and 23](https://www.irs.gov/instructions/i1040sc); [Form 1040 instructions (2025), Schedule 1](https://www.irs.gov/instructions/i1040gi).

## Reconciling Box 1a to Schedule C

- **Start from gross.** Put gross receipts on line 1, and include amounts no form reported (cash, checks, bank transfers). Refunds on goods returned go on line 2. Processor and platform fees are deducted as expenses, not netted out of line 1. Box 1a already includes fees, refunds and shipping, so netting them before line 1 makes line 1 look short of the form. [Schedule C instructions](https://www.irs.gov/instructions/i1040sc); [Form 1099-K Box 1a](https://www.irs.gov/instructions/i1099k)
- **Duplicates with Form 1099-NEC.** Card and third-party-network payments "must be reported on Form 1099-K ... and are not subject to reporting on Form 1099-MISC or Form 1099-NEC". A client paid by card who also receives a 1099-NEC from the customer has been reported twice. Report the income **once** and explain the duplicate in the bridge statement. If the 1099-NEC totals exceed line 1, the Schedule C instructions require a statement explaining the difference. [Forms 1099-MISC/NEC instructions](https://www.irs.gov/instructions/i1099mec); [Schedule C line 1](https://www.irs.gov/instructions/i1040sc)
- **Multiple forms.** Use every form together with the client's records. A client can receive several forms for different platforms. [FAQ Q11](https://www.irs.gov/newsroom/form-1099-k-faqs-what-to-do-if-you-receive-a-form-1099-k)
- **Shared terminal, business sold, entity change.** Box 1a may include receipts that belong to someone else, or to another period or entity. Where required, file and furnish information returns for the other party's share, or get a corrected form from the filer. Keep the agreements and dated records. [What to do with Form 1099-K](https://www.irs.gov/businesses/what-to-do-with-form-1099-k)

## Personal items: loss versus gain

- A personal item is something owned for personal use (a car, furniture, clothing, jewelry, tickets). Treat each item separately. A gain is taxable. A loss is not deductible, and gains cannot be offset by losses. [What to do with Form 1099-K](https://www.irs.gov/businesses/what-to-do-with-form-1099-k)
- **Loss items.** Enter the loss items' share of Box 1a in the entry space at the top of Schedule 1. If Forms 8949 and Schedule D are being filed anyway, the loss can instead go on Form 8949: proceeds, basis, code "L" in column (f), and the nondeductible loss as a positive amount in column (g), giving zero. [FAQ Q6](https://www.irs.gov/newsroom/form-1099-k-faqs-what-to-do-if-you-receive-a-form-1099-k)
- **Gain items.** Report on Form 8949 and Schedule D, not in the Schedule 1 entry space. [Form 1040 instructions (2025)](https://www.irs.gov/instructions/i1040gi)
- **Basis records.** If the purchase price is not remembered, reconstruct it from card or bank statements or the seller's records. Examiners may accept reconstructed records or oral testimony when records are lost. [FAQ Q7](https://www.irs.gov/newsroom/form-1099-k-faqs-what-to-do-if-you-receive-a-form-1099-k)
- **Older years.** The Schedule 1 line 8z plus line 24z pair is the 2022-2023 method. From tax years beginning in 2024, use the entry space at the top of Schedule 1. [FAQ Q7, common situations](https://www.irs.gov/newsroom/form-1099-k-faqs-common-situations)

## Hobby or business

- An activity run with the intention of making a profit is a business (Schedule C). An activity not engaged in for profit goes on Schedule 1 line 8j. [Pub. 525](https://www.irs.gov/publications/p525)
- Weigh all facts and circumstances, and no single factor decides. The regulation lists nine factors, including: how businesslike the activity is; expertise; time and effort; expected appreciation of assets; success in other activities; history of income or losses; occasional profits; the taxpayer's financial status; and personal pleasure. [Treas. Reg. §1.183-2(b)](https://www.law.cornell.edu/cfr/text/26/1.183-2)
- **Presumption:** if gross income exceeds deductions in 3 or more of 5 consecutive years ending with the current year (2 of 7 for horse breeding, training, showing or racing), the activity is presumed to be for profit unless the IRS shows otherwise. [26 U.S.C. §183(d)](https://www.law.cornell.edu/uscode/text/26/183)
- **Hobby expenses:** these are miscellaneous itemized deductions. §67(h) allows none for any tax year beginning after 2017, and P.L. 119-21 §70110 made that permanent. Pub. 525 (2025) still says they are deductible up to the hobby income if the taxpayer itemizes. That conflicts with the statute, so do not rely on it. Whether cost of goods sold may reduce hobby gross receipts is a refer point. [26 U.S.C. §67](https://www.law.cornell.edu/uscode/text/26/67)

## Backup withholding

- If the payee has not given a correct TIN, the payer must withhold 24% from reportable payments. [Backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding)
- **Card payments:** no threshold, so withholding can apply from the first payment when the TIN is missing. Box 4 reports withholding on payments "required to be aggregately reported in box 1a". [Form 1099-K instructions, Box 4](https://www.irs.gov/instructions/i1099k)
- **TPSO payments, calendar 2025 onward:** a payment counts as a reportable payment for backup withholding **only if**, at that point in the year, the payee's transactions exceed 200 **and** the amount exceeds the §6050W(e) dollar figure. The exception: if any of the payor's TPSO payments to that payee in the **prior** year were reportable, withholding can apply from the start of the year. [26 U.S.C. §3406(b)(8) and effective-date note](https://www.law.cornell.edu/uscode/text/26/3406)
- A TPSO that performed backup withholding for a payee must file Form 945 and a Form 1099-K for that payee, even below the threshold. [FAQ Q5](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information)
- **The client's side:** give the platform a correct SSN, ITIN or EIN. An ITIN is acceptable. Claim any Box 4 amount as federal income tax withheld on the return for the year the income was received. [FAQ Q9-Q10](https://www.irs.gov/newsroom/form-1099-k-faqs-what-to-do-if-you-receive-a-form-1099-k); [Backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding)

## Digital assets: Form 1099-DA

- Brokers that take possession of the digital assets they sell for customers file Form 1099-DA. The brokers covered are custodial platforms, certain hosted wallets, kiosks and certain processors of digital asset payments. Gross proceeds are reported for transactions on or after 1 January 2025. Basis is reported for certain transactions on or after 1 January 2026. Non-custodial ("decentralized") brokers are outside these regulations. [Digital assets](https://www.irs.gov/filing/digital-assets)
- **Basis is reported only for covered securities.** A covered security is a digital asset acquired **after 2025** in a custodial account with the broker and held there until the sale. For 2026 sales of noncovered assets (for example, coins bought before 2026 or transferred in), basis is not required, and the client must supply basis from their own records. [Instructions for Form 1099-DA (2026)](https://www.irs.gov/instructions/i1099da)
- **Relief for brokers:** for 2025 transactions, the IRS will not impose filing or furnishing penalties on brokers who make good-faith efforts. There is also backup-withholding relief for all transactions in 2025 and 2026. [Digital assets](https://www.irs.gov/filing/digital-assets)
- Proceeds are not income. Compute gain or loss from the transaction history on Form 8949. If a Form 1099-K and a Form 1099-DA appear to report the same digital-asset activity, report each sale once and document why. Refer when the history is incomplete.

## State reporting

States may require Forms 1099-K below the federal threshold. The IRS says so, but a state threshold must be read on that state's own revenue site, not on a secondary list. A state-driven form carries the same federal consequence as any other form: every amount on it must be reconciled on the federal return. [FAQ Q2 and Q5](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information)

## CP2000 response

- A CP2000 means third-party information did not match the return. It proposes changes and is not a bill. Reply **by the date on the notice**: sign the response form, say whether you agree or disagree, and attach support. If you do not reply, the IRS may send another notice and a bill. [Understanding your CP2000](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice)
- **If you disagree,** send the bridge showing where each Box 1a dollar was reported or why it is excluded. Include copies of the 1099-K and any duplicate 1099-NEC, the platform annual statements, bank or processor statements for fees and refunds, purchase evidence for personal items, and correspondence with the filer about a corrected form.
- **If the notice is right and there is other income or deductions to report,** file Form 1040-X marked "CP2000" with the response. If other years have the same issue, amend them too. [Understanding your CP2000](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice)
- **Penalty exposure:** an accuracy-related penalty of 20% of the underpayment can apply for negligence or a substantial understatement. It is not automatic, so address it in the reply where facts support reasonable cause. [26 U.S.C. §6662](https://www.law.cornell.edu/uscode/text/26/6662)
- Correct reporting with an attached bridge statement reduces mismatch risk. It does not guarantee that no notice is issued.

## Worked cases

**Case A: personal items, loss and gain on one form (IRS example).** A client bought a couch for $1,000 and sold it for $700, and bought a handbag for $800 and sold it for $1,200. The Form 1099-K shows $1,900 in Box 1a. Enter $700 in the entry space at the top of Schedule 1 (the couch loss is not deductible). Report the handbag on Form 8949 and Schedule D: a $400 gain. [Form 1040 instructions (2025), Schedule 1](https://www.irs.gov/instructions/i1040gi)

**Case B: online seller with a duplicate 1099-NEC (hypothetical figures).**
The facts:
- A card-processor Form 1099-K shows $48,000. It includes $6,000 that one business customer paid by card, and that customer also issued a Form 1099-NEC for $6,000. Card payments are reported on Form 1099-K only. [Forms 1099-MISC/NEC instructions](https://www.irs.gov/instructions/i1099mec)
- Box 1a also includes $2,000 of state sales tax imposed on buyers that the client collected and paid over. There were $1,500 of refunds for returned goods and $1,400 of processor fees. [Schedule C instructions](https://www.irs.gov/instructions/i1040sc)
- The client also had $3,000 of cash sales that no form reported. Those still go on line 1. [Schedule C instructions](https://www.irs.gov/instructions/i1040sc)

The reconciliation:

| Line | Amount |
|---|---|
| Information returns: 1099-K plus 1099-NEC ([bridge rule](https://www.irs.gov/instructions/i1040sc)) | $54,000 |
| Less: duplicate 1099-NEC | $6,000 |
| Less: sales tax imposed on buyers | $2,000 |
| Add: cash sales not on any form | $3,000 |
| Schedule C line 1, gross receipts | $49,000 |
| Schedule C line 2, returns and allowances | $1,500 |
| Processor fees, deducted as an expense, not netted | $1,400 |

Attach a short statement giving this bridge. [Schedule C line 1 statement](https://www.irs.gov/instructions/i1040sc)

**Case C: roommate rent through a payment app.** A roommate's share of rent reached the client through a goods-and-services payment, and a Form 1099-K was issued. Ask the filer for a corrected form showing zero. If none arrives in time, file anyway and enter the amount in the entry space at the top of Schedule 1 as an amount included in error. It is not income. [What to do with Form 1099-K](https://www.irs.gov/businesses/what-to-do-with-form-1099-k); [Form 1040 instructions (2025)](https://www.irs.gov/instructions/i1040gi)

**Case D: under the TPSO threshold.** A client sold goods through a marketplace for more than $20,000 but in only 150 transactions. The marketplace has no federal duty to file, because both tests must be exceeded. The receipts are still reportable, and a voluntary or state form may arrive anyway. [26 U.S.C. §6050W(e)](https://www.law.cornell.edu/uscode/text/26/6050W)

## When to refuse or refer

- Refer if the client insists on leaving out receipts because "no form was issued" or because a form was below a threshold. Income is reportable regardless, so do not prepare a return that omits it.
- Refer if a Form 1099-K is in an individual's name but the income belongs to a partnership, corporation or S corporation. The form needs correcting and the entity return is out of scope.
- Refer a hobby-versus-business decision with multi-year Schedule C losses against other income, or any question on hobby cost of goods sold.
- Refer digital-asset histories that cannot be rebuilt, where basis is missing for noncovered assets, or where Forms 1099-K and 1099-DA overlap.
- Refer a CP2000 that has already moved to a bill, a statutory notice of deficiency, or proposed penalties the client wants to contest. Refer too when the tax at stake is large.
- Refer where a state threshold or state reporting duty matters and the rule cannot be confirmed on the state's own site.

## Filing and payment steps with deadlines

- **Forms to the payee:** the filer must furnish Form 1099-K by 31 January of the following year: 31 January 2027 for 2026 activity. [26 U.S.C. §6050W(f)](https://www.law.cornell.edu/uscode/text/26/6050W)
- **Wrong form:** contact the filer shown at the top left of the form, or the payment settlement entity shown at the bottom left. The IRS cannot correct a Form 1099-K. Do not delay filing waiting for a correction. [What to do with Form 1099-K](https://www.irs.gov/businesses/what-to-do-with-form-1099-k)
- **2026 return:** file Form 1040 with Schedule C, Schedule 1, Form 8949 and Schedule D as needed. The 2026 Form 1040 and Schedule 1 instructions were not yet published when this Guide was written (September 2026). Confirm that the top-of-Schedule-1 entry space is unchanged and confirm the April 2027 due date when they appear. [Form 1040 instructions](https://www.irs.gov/instructions/i1040gi)
- **Extension:** Form 4868 gives an automatic 6-month extension to file. It does not extend the time to pay, and interest runs on unpaid tax from the original due date. [Form 1040 instructions (2025)](https://www.irs.gov/instructions/i1040gi)
- **CP2000:** reply by the date printed on the notice, by upload, fax or mail as the notice says. [Understanding your CP2000](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice)

## 2025 returns (still open until 15 October 2026 on extension)

- The 2025 return was due 15 April 2026. With Form 4868 filed by then, the filing deadline is 15 October 2026, but tax was due in April. [Form 1040 instructions (2025)](https://www.irs.gov/instructions/i1040gi)
- **TPSO threshold for 2025:** more than $20,000 and more than 200 transactions, the same as 2026. [Form 1040 instructions (2025)](https://www.irs.gov/instructions/i1040gi)
- **Personal-item losses and erroneous amounts:** use the entry space at the top of the 2025 Schedule 1. Several forms may be combined into one amount. [FAQ Q6, common situations](https://www.irs.gov/newsroom/form-1099-k-faqs-common-situations)
- **Tips:** 2025 Forms 1099-K do not separate tips. For the 2025 qualified-tips deduction (Schedule 1-A), a non-employee may use tip amounts included in a 1099-K total if they are substantiated. Platform earnings statements or daily tip logs qualify. Cash tips that do not appear on any Form 1099 cannot be included. From 2026, Box 1c shows cash tips separately. [Form 1040 instructions (2025), Schedule 1-A](https://www.irs.gov/instructions/i1040gi); [Form 1099-K instructions](https://www.irs.gov/instructions/i1099k)
- **1099-DA:** 2025 forms report gross proceeds. Basis reporting starts with 2026 transactions in covered assets. [Digital assets](https://www.irs.gov/filing/digital-assets)

## Completion checklist

- [ ] Every Form 1099-K, 1099-NEC, 1099-MISC and 1099-DA received is on the bridge, whatever its amount.
- [ ] Box 1a has been split into business, rental, hobby, personal gain, personal loss and not-income slices, from records rather than guesses.
- [ ] Schedule C line 1 is gross. Returns are on line 2. Fees are expenses. Sales tax is treated according to who it is imposed on.
- [ ] Any 1099-NEC that duplicates a card or app payment is reported once and explained.
- [ ] Personal losses and errors are in the top-of-Schedule 1 entry space (or on Form 8949 with code "L"). Gains are on Form 8949 and Schedule D.
- [ ] Hobby income is on Schedule 1 line 8j with no expenses deducted. The for-profit analysis is documented.
- [ ] Box 4 backup withholding is claimed. The client's TIN has been fixed with the platform.
- [ ] Digital-asset gain or loss is computed from the transaction history, with basis supplied for noncovered assets.
- [ ] Requests for corrected forms, platform statements and basis evidence are kept in the file.
- [ ] Any CP2000 reply is sent before the date on the notice.

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
