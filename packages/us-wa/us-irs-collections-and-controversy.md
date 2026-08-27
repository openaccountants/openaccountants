---
name: us-irs-collections-and-controversy
description: Tier 2 US federal content skill for IRS notices, audits, collections, and controversy procedures. Covers common notices (CP2000, CP14, CP504, LT11/CP90), the 30-day Collection Due Process window under §6330 (Form 12153), the 10-year Collection Statute Expiration Date under §6502, collection alternatives (installment agreement, currently-not-collectible, offer in compromise, partial-pay IA), audit types and the §7430 attorney fees rule, Tax Court / District Court / Claims Court forum choice, §6662 accuracy and §6663 fraud penalties, First-Time Abatement (Notice 2014-2), and §6015 innocent spouse relief. Tax year 2025.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US IRS Collections And Controversy

## 1. Scope

This skill governs the post-filing life of a US federal tax return: what happens when the IRS disagrees with what was filed, when balances go unpaid, when an examination is opened, and how a CPA (or Enrolled Agent or attorney admitted under Circular 230) navigates the resulting procedural maze. It is the workhorse of small-firm tax practice — by some estimates more than half of a typical sole practitioner's hours after April 15 are spent on notice response, installment agreements, transcript reconciliation, and audit defense rather than on return preparation itself.

The skill covers, for tax year 2025:

- The anatomy of an IRS notice: how the CP/LT numbering system works, where critical dates appear, and how to decode the notice without reading every line.
- The full catalog of common notices a small-firm CPA will see, with response windows, escalation paths, and the legal effect of each.
- The collection timeline from assessment to levy, the 10-year Collection Statute Expiration Date (CSED) under §6502, and the events that extend it.
- Collection alternatives: full pay, short-term plan, streamlined installment agreement, non-streamlined IA, Partial Pay Installment Agreement (PPIA), Currently Not Collectible (CNC) status, Offer in Compromise (OIC) under §7122, Innocent Spouse Relief under §6015, and Injured Spouse allocation under §6402(e).
- Audit types (correspondence, office, field) and the audit timeline from selection through 30-day letter and Statutory Notice of Deficiency.
- Forum choice: Tax Court (pre-payment, deficiency cases, §7463 small case option) versus District Court (refund suit, pay first) versus Court of Federal Claims (refund suit, no jury, specialized).
- IRS Independent Office of Appeals: when to go, what to expect, statistical settlement rates.
- Collection Due Process (CDP) hearing under §6330: the 30-day window, Form 12153, and the preservation of Tax Court rights.
- Collection Appeals Program (CAP) under Form 9423: faster, less procedural, but no Tax Court access.
- Federal tax lien mechanics (NFTL, discharge, subordination, withdrawal under the Fresh Start initiative) and levy mechanics under §6331.
- Taxpayer rights under §7521 (audio recording, representation, refusal to attend).
- Penalty exposure: §6651 (failure to file/pay), §6662 (accuracy), §6663 (fraud), §6651(f) (fraudulent failure to file), §7201/§7203/§7206 (criminal).
- Penalty abatement: First-Time Abatement (FTA) under Notice 2014-2 and IRM 20.1.1.3.3.2.1, Reasonable Cause under §6651(a), and the statutory exception for erroneous IRS written advice under §6404(f).
- The Form 2848 power of attorney and Form 8821 tax information authorization mechanics, including the IRS Centralized Authorization File (CAF) workflow.
- The CPA-led resolution playbook: pull transcripts, secure authorizations, identify status, compute liability and CSED, evaluate alternatives, respond, calendar follow-up.

Out of scope (refusal catalogue, see `us-tax-workflow-base` §9):

- **Criminal tax defense** beyond the recognition stage. Once the IRS Criminal Investigation Division (CID) is involved or a special agent appears, the engagement must be transferred to a criminal tax attorney and the CPA's role narrows dramatically (no work product privilege under *United States v. Arthur Young* for tax-preparer accountants in criminal matters; only the §7525 federally authorized tax practitioner privilege in non-criminal federal matters, which evaporates the moment CID enters).
- **Bankruptcy discharge of tax debt.** The interaction with §523(a)(1) and the three-year, two-year, and 240-day tests, plus the tolling rules from *Young v. United States* and *In re Putnam*, are bankruptcy work and must be referred to a bankruptcy attorney. This skill mentions bankruptcy only as a CSED-tolling event.
- **Whistleblower claims** under §7623 (Form 211).
- **International collection matters** beyond noting that the CSED is suspended while the taxpayer is outside the United States for a continuous period of 6 months or more under §6503(c).
- **Trust Fund Recovery Penalty (TFRP)** under §6672, except as flagged at the recognition stage. TFRP defense is its own specialty.
- **Tax-exempt organization examinations** under §501(c).
- **Employment tax CDP** is technically within scope but the substantive employment tax determination work is in `us-form-941-940-payroll`.
- **State tax collection** is outside this skill except where state action is triggered by federal action (e.g., state refund offset under §6402).

Always loaded with: `us-tax-workflow-base` v0.2 or later. Frequently loaded alongside `us-form-1040-individual-return` (when the underlying issue is a 1040 deficiency), `us-sole-prop-bookkeeping` and `us-schedule-c-and-se-computation` (when the AUR or audit hits Schedule C), or any other content skill that produced the originally filed return.

A reviewer credentialed under Circular 230 must sign off before any document leaves the engagement. The penalty for unauthorized practice before the IRS is real, and the Office of Professional Responsibility (OPR) actively investigates Circular 230 violations.

## 2. IRS Notice Anatomy

Every IRS notice issued to a taxpayer follows a standardized format dictated by the Taxpayer Bill of Rights (Publication 1) and IRM 21.3.1. Understanding the format lets a practitioner triage a stack of notices in seconds.

### 2.1 The five things to read first

- **Five things to read first on a notice** — 1. The notice number (top right corner): CPnnn, CPnnnA, or LTnn. CP notices are generated by automated systems; LT notices are generated by ACS or Revenue Officers. 2. The notice date (top right, below the notice number) — critical response deadlines run from this date, not receipt date; mail delays do not extend statutory deadlines except as expressly provided (e.g., §7502 mailbox rule for taxpayer filings, narrow petition-filing contexts). 3. Taxpayer identifying information — name, address, TIN (often last four digits). Verify it matches the client. 4. The tax year and form at issue, e.g. 'Tax Year 2023, Form 1040' or 'Tax Period December 31, 2023, Form 941.' 5. The amount the IRS thinks is owed — a bottom-line number with an 'as of' date and a footnote that interest and penalties continue to accrue.  _(Publication 1; IRM 21.3.1; §7502)_

### 2.2 The body of the notice

- **Notice body structure** — The body of a CP notice is generated from canned paragraphs assembled from IRM 21.3 keyed to the assessment, the proposed adjustment, prior filing history, and collection status. The paragraph layout is predictable; the 'What you need to do' section appears in the same place for a given CP number; the response address and deadline are always boxed or bolded. A practitioner reads, in order: notice number → date → tax year → amount → 'What you need to do' → 'If you disagree' → response address.  _(IRM 21.3)_

### 2.3 The notice always tells you what it wants

- **Four required notice elements** — Every notice contains, somewhere in the first page: the action required (pay, respond, do nothing, etc.); the deadline; the consequence of inaction; the right of response. If these four elements cannot be found, the practitioner is reading the wrong notice or page. Notices sometimes arrive in two parts (e.g., a CP2000 always comes with a response form, often Form 5564 or a notice-specific response page); both parts matter.

### 2.4 Notices that are NOT actually from the IRS

A separate hazard category: notices that purport to be from the IRS but are not. The IRS does not initiate first contact by phone, email, or text. The IRS does not demand payment via gift cards or wire transfer. Any 'IRS notice' arriving by email is a phishing attempt. Any 'IRS agent' demanding immediate payment by phone is an impostor. Verify by calling the practitioner priority line (PPL) at 1-866-860-4259 with a valid Form 2848 on file.

A small but real subset: state-level 'tax resolution' companies that send notices designed to look like IRS notices, soliciting the taxpayer to call a private number. These are advertising, not government action. The giveaway: the return address is a private PO box, not Cincinnati, Fresno, Kansas City, Andover, Austin, Memphis, Ogden, or Philadelphia (the IRS submission processing centers).

## 3. Common Notices Catalog

This section covers the notices a small-firm CPA encounters most often. Each entry gives the CP number, the trigger, the response window, the legal effect, and the recommended action.

### 3.1 CP2000 — Notice of Underreported Income (Automated Underreporter, AUR)

- **CP2000 trigger and legal effect** — Trigger: the IRS's Information Returns Processing (IRP) matching system compared third-party information returns (W-2, 1099-NEC, 1099-INT, 1099-DIV, 1099-K, 1099-B, K-1, SSA-1099, etc.) against the return and found a discrepancy. Common causes include a late 1099-NEC, an unreported 1099-B believed to be inside a retirement account, or a 1099-K triggered after the phased-in §6050W threshold (for 2025 the reporting threshold is $2,500, with the full $600 threshold scheduled for 2026 — verify current threshold). Legal effect: a CP2000 is a proposal, not an assessment; unless the taxpayer agrees or disputes, the IRS will issue a CP3219A Statutory Notice of Deficiency and ultimately assess. A CP2000 is not an audit — it is a document-matching letter; it does not toll the §6501 three-year statute of limitations on assessment, does not block amendment, and does not require Form 2848 to discuss (Form 8821 suffices for information access).  _(§6050W; §6501)_
- **CP2000 response window and options** — Response window: 30 days from the notice date; a 30-day extension is routinely granted on request (call AUR unit or fax a written extension request). Response options: 1. Agree — sign the response form, return it, and pay or set up an IA; the proposed adjustment becomes the assessment ~6 weeks later. 2. Disagree in full — submit a written statement and supporting documentation (e.g., dispute the 1099 via Form 4598 to the payer, point to the correct Schedule C line, attach broker confirmation for basis, attach return excerpt for K-1). 3. Partial agreement — agree to some adjustments, disagree to others, mark up the response form. 4. Request an extension — routine for 30 days, longer on request.

If the taxpayer ignores a CP2000, the IRS issues a CP3219A (Statutory Notice of Deficiency), and the 90-day Tax Court clock starts. Missing the 90-day window means the deficiency becomes a final assessment that can only be challenged through a refund suit (pay first, sue second) or a CDP hearing tied to a future collection action. Many taxpayers ignore CP2000s thinking they are 'junk mail.' The CPA's job at intake is to ask: 'Did you get any letters from the IRS?' Always.

### 3.2 CP3219A — Statutory Notice of Deficiency ("90-day letter")

- **CP3219A trigger and legal effect** — Trigger: issued when (a) a CP2000 has gone unresolved, (b) an audit has been completed and the taxpayer did not agree, or (c) the IRS has proposed a deficiency through some other examination channel. Legal effect: this is the ticket to Tax Court. Under §6213(a), the taxpayer has 90 days (150 if the notice is addressed to a person outside the United States) from the date of the notice to file a petition with the United States Tax Court. If timely filed, the IRS is barred from assessing the deficiency until the Tax Court rules. If not filed within 90 days, the deficiency is assessed and collection begins. The 90-day deadline is jurisdictional; the Tax Court has no power to extend it. The §7502 mailbox rule applies (postmark date counts), but a petition mailed late is dead.  _(§6213(a); §7502)_
- **CP3219A response window and options** — Response window: 90 days, no extension possible. Response options: 1. File a Tax Court petition (Form 2 or the Court's electronic petition system); filing fee $60; if the deficiency including penalties is $50,000 or less per tax year, the taxpayer may elect 'small tax case' status under §7463, simplifying procedure (no formal pleadings, no appeal) but the decision is final. 2. Sign Form 5564 (the waiver attached to the notice) and let the assessment proceed. 3. Negotiate with IRS Appeals while the 90-day clock runs — many CP3219A cases settle in Appeals before the 90-day deadline expires, but filing the Tax Court petition is the only way to preserve rights once the 90 days run, even if Appeals is engaged.  _(§7463)_

If a CPA is engaged on day 80 of a CP3219A with no Tax Court petition drafted, the practitioner should consider filing a 'skeleton' petition immediately (a one-page petition contesting the deficiency and reserving the right to amend) to preserve the deadline, then negotiate from inside the litigation posture. A late petition is dismissed for lack of jurisdiction; the taxpayer is then left with the pay-first refund-suit forum or a CDP hearing tied to a later collection action.

### 3.3 CP14 — First Notice of Balance Due

- **CP14 trigger, legal effect, response** — Trigger: a tax has been assessed and is unpaid — most commonly the taxpayer filed a return showing tax due but didn't pay, or paid less than the full amount. Legal effect: first notice of an assessed balance; under §6303 the IRS must send a notice and demand within 60 days of assessment, and the CP14 satisfies that requirement; the 10-year CSED clock (§6502) starts on the assessment date, not the CP14 date. Response window: 21 calendar days to pay under §6601(e)(3) (the '10 days' figure on the notice is the cutoff before additional failure-to-pay penalty accrues, not a statutory deadline). Response options: 1. Pay online at IRS Direct Pay, EFTPS, or IRS.gov payment portal. 2. Set up an installment agreement — use the IRS Online Payment Agreement tool for amounts up to $50,000 (streamlined), or Form 9465 by mail otherwise. 3. Request abatement if the underlying tax or penalty is incorrect.  _(§6303; §6502; §6601(e)(3))_

### 3.4 CP501 — Reminder of Balance Due

- **CP501 trigger and legal effect** — Trigger: ~5 weeks after CP14 if unpaid. Legal effect: reminder only, no new rights or obligations. Response window: implicit — respond before the next escalation (CP503 in another ~5 weeks).

### 3.5 CP503 — Second Reminder

- **CP503 trigger and legal effect** — Trigger: ~5 weeks after CP501. Legal effect: reminder only; tone escalates.

### 3.6 CP504 — Final Notice of Intent to Levy State Tax Refund

- **CP504 trigger and legal effect** — Trigger: ~5 weeks after CP503; the IRS's first hard escalation. Legal effect: under §6331(d), this notice gives the IRS authority to levy on the taxpayer's state tax refund 30 days after the notice. It also signals that the next notice (LT11 or CP90) will give authority to levy paychecks, bank accounts, and other property. CP504 is NOT a final levy notice for wages or bank accounts — that is LT11 / CP90 / Letter 1058.  _(§6331(d))_
- **CP504 response window and options** — Response window: 30 days. Response options: 1. Pay in full. 2. Enter into an installment agreement (stops further collection). 3. Request CNC status (suspends collection on hardship grounds). 4. Submit an OIC (stops collection while pending). 5. Note: CP504 does NOT confer Collection Due Process rights — the CDP right attaches to LT11/CP90, not CP504. A CDP request filed against a CP504 is not jurisdictionally valid (though the IRS may treat it as an equivalent hearing request, which does not preserve Tax Court rights).

### 3.7 LT11 / CP90 / Letter 1058 — Final Notice of Intent to Levy and Notice of Your Right to a Hearing

- **LT11/CP90/1058 trigger and legal effect** — Trigger: ~5 weeks after CP504. Different versions (LT11 from ACS, CP90 from IRS systems, Letter 1058 from Revenue Officers) but identical legal effect. Legal effect: this notice opens the Collection Due Process (CDP) window under §6330. The taxpayer has 30 days from the notice date to file Form 12153 (Request for a Collection Due Process or Equivalent Hearing). If filed timely: all collection action is suspended (§6330(e)); the CSED is tolled (§6330(e)); the taxpayer is entitled to a hearing with the IRS Independent Office of Appeals; after the hearing, the taxpayer may petition the Tax Court for review of the Appeals determination under §6330(d). If Form 12153 is filed after the 30-day window (within one year), the taxpayer gets an 'equivalent hearing' — same hearing officer, similar procedure, but no Tax Court right at the end.  _(§6330; §6330(e); §6330(d))_

The 30-day CDP window is the single most important deadline in collections practice. Missing it converts the CDP right into the much weaker 'equivalent hearing' right and forfeits all Tax Court access for that levy. If a client walks in with an LT11 dated 25 days ago, the practitioner files Form 12153 the same day, by fax with confirmation of receipt, and confirms by certified mail.

- **LT11/CP90/1058 response window and options** — Response window: 30 days for CDP; 1 year for equivalent hearing. Response options: 1. File Form 12153 for a CDP hearing, raising any relevant issue: spousal defenses, collection alternatives (IA, OIC, CNC), challenges to the underlying liability if no prior opportunity to dispute existed, lien withdrawal, etc. 2. Negotiate directly with ACS to set up an installment agreement and skip the CDP — faster but forfeits CDP rights. 3. Pay in full — moots the levy.

### 3.8 CP148A / CP148B — Federal Tax Lien Notice

- **CP148A/B trigger and legal effect** — Trigger: the IRS has filed a Notice of Federal Tax Lien (NFTL) in the public records of the county where the taxpayer resides or owns property. Legal effect: under §6321 a federal tax lien arises automatically when (a) assessment is made, (b) the IRS makes demand for payment, and (c) the taxpayer fails to pay. The NFTL is the public notice of that lien; it perfects the IRS's priority against most subsequent creditors under §6323. The NFTL appears on credit reports (until Fair Credit Reporting Act tradeline removal rules; the IRS has its own withdrawal procedures under the Fresh Start program).  _(§6321; §6323)_
- **CP148A/B response window and options** — Response window: 30 days to request a CDP hearing on the NFTL filing (different from a CDP hearing on a levy). Response options: 1. CDP hearing on lien filing (Form 12153) within 30 days. 2. Request lien withdrawal under §6323(j) if the lien was filed prematurely or in error, or under the Fresh Start 'lien withdrawal after IA' rules. 3. Pay in full and request a Certificate of Release.  _(§6323(j))_

### 3.9 CP523 — Default of Installment Agreement

- **CP523 trigger and legal effect** — Trigger: the taxpayer missed a payment on an installment agreement, failed to file a subsequent year's return, failed to pay a subsequent year's tax, or otherwise violated the terms of the agreement. Legal effect: the IA is in default; levy action will resume 30 days after the notice unless the default is cured; the taxpayer has 30 days to request a CDP hearing or negotiate reinstatement.
- **CP523 response window and options** — Response window: 30 days. Response options: 1. Cure the default (make the missed payment, file the missing return). 2. Reinstate the IA (may require a reinstatement fee and a renewed 433-F). 3. Negotiate a new IA if circumstances have changed.

A taxpayer with a $50,000 streamlined IA who misses a payment and then ignores the CP523 will, 30 days later, have a levy on payroll, with no CDP right preserved (CP523 itself does include CDP rights under §6330 for the renewed levy; verify this is preserved in the response).

### 3.10 CP08, CP09, CP27 — Refund-Side Notices

These are the friendly notices. The IRS has determined that the taxpayer may qualify for Earned Income Tax Credit (EITC), Additional Child Tax Credit, or other refundable credits that were not claimed. The notice invites the taxpayer to file a Schedule EIC or claim the credit and receive a refund. Response is voluntary; failure to respond costs the taxpayer money, not the IRS.

### 3.11 CP11 / CP12 / CP13 — Math Error Notices

- **Math error notices trigger and legal effect** — Trigger: the IRS, during return processing, identified a 'math or clerical error' under §6213(b) — an arithmetic mistake, a transposition, a missing schedule, an unsupported credit (e.g., the wrong CTC amount), or a credit the IRS's records show the taxpayer is not entitled to. Legal effect: under §6213(b), the IRS may assess the corrected amount without issuing a Statutory Notice of Deficiency. However, the taxpayer has 60 days to request abatement of the math error assessment. If timely requested, the assessment is abated and the IRS must follow normal deficiency procedures (i.e., issue a 90-day letter) to re-assess.  _(§6213(b))_
- **Math error response window and options** — Response window: 60 days for the special math error abatement procedure under §6213(b)(2). Response options: 1. Accept — if CP11 (additional tax), pay; if CP12 (refund reduced), do nothing. 2. Request abatement within 60 days — this forces the IRS into normal deficiency procedures. The 60-day math error abatement window is widely overlooked; many taxpayers receive a CP11 with reduced refund or increased tax, assume the IRS is right, and never invoke the §6213(b)(2) abatement procedure.  _(§6213(b)(2))_

### 3.12 Letter 2202 / 2205 — Initial Audit Contact

- **Letter 2202/2205 trigger, effect, response** — Trigger: the IRS Examination function has selected the return for audit. Legal effect: this is the start of an examination. The 2202 series is correspondence audit; the 2205 series is in-person audit. The notice will identify the agent, the issues, and the requested documents (often via an attached Form 4564 Information Document Request, IDR). Response window: typically 30 days; the IDR may have separate deadlines. Response options: 1. Engage representation — file Form 2848; the CPA can attend in lieu of the taxpayer under §7521(c). 2. Respond to the IDR — provide responsive documents only; do not volunteer. 3. Negotiate the scope — audits begin with a stated scope but expand if issues are found; keep the scope tight.  _(§7521(c))_

### 3.13 Letter 525 / 692 / 950 — 30-Day Letter (Audit Report)

- **30-day letter trigger, effect, response** — Trigger: the audit has concluded with proposed adjustments. The IRS issues the report (Form 4549, Examination Changes) with a 30-day cover letter inviting the taxpayer to (a) agree, (b) protest to Appeals, or (c) do nothing (which leads to the 90-day letter). Legal effect: the 30-day letter is the gateway to IRS Appeals. A timely protest under IRM 4.10.8 (formal written protest if proposed adjustments exceed $25,000 per period; small case request otherwise) transfers the case to the Independent Office of Appeals. There is no statutory right to Appeals — it is administrative. A taxpayer who skips Appeals and goes straight to Tax Court forfeits the chance to settle in the administrative forum. Response window: 30 days (extendable on request).  _(IRM 4.10.8)_

### 3.14 Letter 3174 — Reminder of Balance Due (Pre-Levy)

A reminder issued by Revenue Officers (RO) in field collections cases, typically before the formal levy notice. Often signals that an RO has been assigned and the case is no longer in the automated ACS pipeline. Treat as a soft deadline; the RO is human and can be negotiated with directly.

### 3.15 CP59 / CP63 — Notice of Unfiled Returns

- **CP59/CP63 trigger, effect, response** — Trigger: the IRS records show the taxpayer was required to file but did not. Legal effect: no assessment yet. If the IRS does not receive a return, it may file a Substitute for Return (SFR) under §6020(b), which uses W-2/1099 income and zero deductions and married-filing-separately status to produce a worst-case liability. SFR assessments are notoriously high. Response window: varies; respond quickly. Response options: 1. File the missing return — almost always preferable to SFR. 2. Request a non-filing exemption if the taxpayer was below the filing threshold.  _(§6020(b))_

## 4. The Collection Timeline

The IRS collection process follows a deterministic timeline driven by the §6303 demand letter (CP14) and the §6331 levy notice (LT11/CP90). Understanding the timeline lets a practitioner predict the next notice and prepare in advance.

### 4.1 Timeline (typical case, ACS pipeline)

**Collection timeline (ACS pipeline)**  _(§6203; §6303; IRM 5.19; §6331(d); §6330; §6331; §6502)_

| Day | Event | Legal authority |
| --- | --- | --- |
| 0 | Tax assessed (date the IRS posts the assessment to the master file). | §6203 |
| 1–21 | Notice and demand issued (CP14). | §6303 |
| 35–60 | CP501 reminder. | IRM 5.19 |
| 70–95 | CP503 second reminder. | IRM 5.19 |
| 105–130 | CP504 — final notice for state refund levy. | §6331(d) (partial) |
| 135–165 | LT11 / CP90 / 1058 — Final Notice of Intent to Levy and CDP rights. | §6330 |
| 165+30 | Levy may issue 30 days after LT11 if no CDP filed. | §6331 |
| 165–225 | Levy on wages, bank accounts, Social Security, IRA, business assets. | §6331 |
| Assessment + 10 years | CSED expires. Debt becomes uncollectable. | §6502 |

- **Timeline variability** — The timeline is approximate. Cases assigned to a Revenue Officer (RO) can move faster (the RO can issue a Letter 1058 without waiting through the full automated sequence). Cases in the Automated Collection System (ACS) follow the timeline above, with some variation. High-priority cases (large dollar, repeat offenders, Trust Fund Recovery candidates) accelerate.

### 4.2 Levy mechanics under §6331

- **Levy trigger and common levy targets** — Once 30 days have passed since LT11/CP90 with no CDP request and no payment arrangement, the IRS may levy. Common levy targets: Wage levy (Form 668-W) — continuous on each paycheck; the exempt amount under §6334(d) is computed from the standard deduction and personal exemptions (for 2025 the IRS publishes Publication 1494 tables; the exempt amount for a single filer with no dependents is roughly $14,600/year divided by pay periods — verify against the most current Publication 1494); everything above the exempt amount goes to the IRS until released. Bank levy (Form 668-A) — one-shot levy on the account balance at the moment the bank receives the levy; the bank holds funds for 21 days (§6332(c)) before remitting, giving a narrow negotiation window. Accounts receivable levy — levies on the taxpayer's customers, catastrophic for businesses. Social Security levy under the Federal Payment Levy Program (FPLP) — up to 15% of SS benefits. IRA/401(k) levy — allowed under §6331(a) but rare; triggers a taxable distribution (IRS does not absorb the income tax consequence) plus possible early withdrawal penalty. Asset seizure — cars, homes (residential real property requires court order under §6334(e)), business equipment — last resort.  _(§6331; §6334(d); §6332(c); §6331(a); §6334(e))_

### 4.3 The bank levy 21-day window

- **Bank levy 21-day negotiation window** — The 21-day hold on bank levies is a CPA's most important collection tool. When a client calls with 'the IRS just took my checking account,' the practitioner has 21 days from the bank's receipt of the levy (Form 668-A) to negotiate a release. Standard arguments: levy was issued without proper §6330 notice (rare but case-determinative); levy causes immediate economic hardship (§6343(a)(1)(D)) — file Form 911 (Taxpayer Advocate request); funds in the account are exempt (e.g., Social Security deposits); IA or OIC is being established; funds in the account belong to a third party (joint account with parent; trust funds). A bank levy negotiation typically settles by the IRS releasing the levy in exchange for the taxpayer entering an installment agreement.  _(§6330; §6343(a)(1)(D))_

## 5. The 10-Year Collection Statute Expiration Date (§6502)

### 5.1 The core rule

- **CSED core rule** — Under §6502(a)(1), the IRS must collect (or commence court proceedings to collect) within 10 years from the date of assessment. After the CSED, the debt is unenforceable. Practitioners refer to this as the 'CSED' — Collection Statute Expiration Date. The CSED is computed by month and year. A tax assessed on March 15, 2015 has a CSED of March 15, 2025, adjusted upward for any tolling events.  _(§6502(a)(1))_

### 5.2 Tolling events that extend the CSED

**CSED tolling events table**  _(§6331(k)(1); §6331(k)(2); §6330(e); §6503(h); §6503(c); §7508A; §6502(a)(2); §6503(a); §6015(e)(2))_

| Event | Authority | Tolling effect |
| --- | --- | --- |
| Pending Offer in Compromise | §6331(k)(1) | Tolled while pending + 30 days |
| Pending installment agreement request | §6331(k)(2) | Tolled while pending + 30 days |
| Collection Due Process hearing | §6330(e) | Tolled while pending |
| Bankruptcy automatic stay | §6503(h) | Tolled while stay in effect + 6 months |
| Taxpayer outside US continuous 6 months | §6503(c) | Tolled while outside |
| Military deferment (combat zone or §7508) | §7508A | Tolled per statute |
| Form 900 waiver | §6502(a)(2) | Tolled as agreed (rare; only with IA in specific cases) |
| Pending Tax Court proceeding | §6503(a) | Tolled |
| Pending innocent spouse claim | §6015(e)(2) | Tolled |

Before recommending any collection alternative, the practitioner must compute the CSED. If the CSED is 18 months away, a 5-year IA is not actually a 5-year IA — it is an 18-month IA that becomes a PPIA when the CSED expires. If the CSED is 8 months away and the IRS has not acted, the right answer may be do nothing and wait. Aggressive collection action by a CPA can extend the CSED (a pending OIC or pending IA request tolls the clock), turning what was a near-expiration into a multi-year continuation.

### 5.3 Pulling the CSED

- **How to compute the CSED** — 1. Pull the Account Transcript via the Transcript Delivery System (TDS) or e-Services (requires CAF-authorized power of attorney). 2. Identify the Transaction Code 150 (return filed/assessed) for the year in question — the date of TC 150 is the assessment date. 3. Add 10 years. 4. Adjust for any tolling events shown in the transcript (TC 480 OIC pending, TC 520 bankruptcy, TC 971 various, etc.). The transcript will sometimes show the CSED directly in the upper portion of the account transcript, but the practitioner must independently verify against the transaction codes.

### 5.4 What happens at CSED

- **CSED expiration effects** — At CSED, the IRS abates the assessment under IRM 5.1.19. The lien expires (a self-releasing NFTL contains language stating it self-releases at CSED, so the lien is automatically released as a matter of public record). Future returns are unaffected. The taxpayer owes nothing.  _(IRM 5.1.19)_

Occasionally a CPA pulls a transcript and finds an assessment 12 years old that the IRS never collected and that the CSED has expired. The taxpayer should not pay it. The CPA should file Form 843 (or simply ignore the assessment if no collection action is pending; the lien self-released, and the IRS systems will eventually abate). Verify by pulling a current transcript showing the abatement.

## 6. Collection Alternatives

Once a balance is assessed and the taxpayer cannot pay in full, the practitioner chooses among five alternatives, in rough order of cost: full pay, short-term plan, installment agreement, currently not collectible, offer in compromise. A sixth (innocent spouse relief) addresses joint liability rather than collection per se.

### 6.1 Pay in Full

- **Pay in full** — Cheapest. Eliminates interest and penalty accrual. The taxpayer pays the balance shown on the most recent notice. The CPA verifies the balance against the transcript (not the notice — notices lag 1–2 weeks).

### 6.2 Short-Term Payment Plan (≤ 180 days)

- **Short-term payment plan terms** — Available online via the IRS Online Payment Agreement tool. No setup fee. Interest and §6651(a)(2) failure-to-pay penalty continue to accrue (interest at the federal short-term rate plus 3%, currently around 8% per year for individual underpayments; penalty at 0.5% per month, capped at 25%). Suitable for taxpayers who can pay within 6 months and want to avoid a formal IA.  _(§6651(a)(2))_

### 6.3 Long-Term Installment Agreement

#### 6.3.1 Streamlined IA

- **Streamlined IA eligibility** — Available for aggregate assessed balance (tax + penalty + interest) of $50,000 or less, paid within 72 months or by CSED, whichever is earlier. Streamlined IAs do not require Form 433-F (Collection Information Statement); the IRS does not verify ability to pay. This is the workhorse IA.

**Streamlined IA setup fees (2025)**  _(2025 published rates; verify against the IRS user fee schedule)_

| Setup method | Fee |
| --- | --- |
| Direct debit setup via Online Payment Agreement | $31 |
| Non-direct-debit setup via Online Payment Agreement | $130 |
| Direct debit setup via mail/phone (Form 9465) | $107 |
| Non-direct-debit setup via mail/phone | $225 |
| Low-income taxpayers (at or below 250% of federal poverty level) | $43 |

#### 6.3.2 Non-Streamlined IA

- **Non-streamlined IA requirements** — Required when (a) the balance exceeds $50,000, (b) the term exceeds 72 months, or (c) the IRS wants verification of ability to pay. Requires Form 433-F (or 433-A or 433-B for higher-dollar cases) showing income, expenses, assets, liabilities. IRS analyzes the taxpayer's 'monthly disposable income' against IRS-published National Standards (food, clothing, personal care, miscellaneous), Local Standards (housing, transportation), and Other Necessary Expenses (taxes, court-ordered payments, medical insurance, child support). The agreed monthly payment is monthly disposable income. The process is adversarial; the IRS often disallows actual expenses that exceed published standards; the CPA's job is to document deviations (high medical expenses, regional cost-of-living deviations, etc.).

#### 6.3.3 Partial Pay Installment Agreement (PPIA)

- **PPIA definition and criteria** — A PPIA is an IA at a payment level that will not fully satisfy the liability before CSED. It is the IRS's recognition that the taxpayer cannot pay the full balance within the collection statute. The IRS reviews PPIAs every 2 years to check whether circumstances have improved. PPIA is appropriate when: the taxpayer's monthly disposable income is positive but small (e.g., $300/month) and the balance is large (e.g., $200,000); the CSED is short enough that the small monthly payment will not retire the debt; the taxpayer has insufficient assets to seriously consider an OIC. PPIA requires Form 433-F or 433-A and IRS analysis identical to non-streamlined IA.

An OIC requires a 20% upfront payment plus disclosure of all assets and 5 years of post-acceptance compliance. A PPIA requires a small monthly payment and runs the CSED clock. For a taxpayer with a CSED 3 years away and $300/month disposable income, a PPIA pays ~$10,800 over the CSED period and discharges (effectively) the rest at CSED, with no upfront payment. The OIC equivalent might require $20,000+ upfront. Always run the comparison.

### 6.4 Currently Not Collectible (CNC) Status

- **CNC criteria and effects** — Under §6343 and IRM 5.16, the IRS will place an account in CNC (status 53) if collection would create economic hardship — i.e., the taxpayer cannot meet basic living expenses if the IRS collects. CNC requires Form 433-F. The IRS analyzes the same income/expense framework as for an IA. If disposable income is zero or negative, CNC is granted. Effects of CNC: collection action stops, no levies; the CSED continues to run (CNC is a CPA's most powerful tool when CSED is approaching: zero payment, CSED unaffected); the lien may remain in place (and may even be filed during CNC if not already); the IRS reviews CNC accounts periodically (typically every 12–24 months) by re-checking the taxpayer's income on subsequent returns — if income increases above thresholds, CNC is lifted; refunds in subsequent years are seized under §6402 and applied to the CNC balance. CNC is the right answer for taxpayers with low fixed income (retirees, disabled, unemployed) and large back balances. It is also the right interim answer while an OIC is being prepared.  _(§6343; IRM 5.16; §6402)_

### 6.5 Offer in Compromise (OIC) under §7122

The OIC allows a taxpayer to settle the tax liability for less than the full amount.

#### 6.5.1 The three statutory grounds

- **OIC three statutory grounds** — Under §7122 and Treas. Reg. §301.7122-1, the IRS will compromise on three grounds: 1. Doubt as to Liability (DATL) — genuine dispute over whether the tax is owed, filed on Form 656-L, rare, requires substantive legal argument. 2. Doubt as to Collectibility (DATC) — the taxpayer cannot pay the full liability and the IRS will not be able to collect it; the most common ground, filed on Form 656. 3. Effective Tax Administration (ETA) — collection would create economic hardship or be inequitable, even though the taxpayer technically could pay; filed on Form 656 with an ETA narrative; rare and granted sparingly.  _(§7122; Treas. Reg. §301.7122-1)_

#### 6.5.2 The Reasonable Collection Potential (RCP) calculation

- **RCP formula** — RCP = Net Realizable Equity in Assets (NRE) + (monthly disposable income × 12 or 24). For each asset: fair market value × 80% (quick sale discount) minus encumbrances (common assets: real estate, vehicles, retirement accounts after deemed tax cost of typically 70% inclusion, bank accounts less $1,000 exempt, business equipment, accounts receivable, life insurance cash value with $1,000 exempt). Future income multiplier: 12 months if 'Lump Sum Cash' offer (paid within 5 months of acceptance); 24 months if 'Periodic Payment' offer (paid in 6–24 monthly installments). The IRS will not accept an OIC below RCP except on ETA grounds.  _(IRM 5.8.5)_

#### 6.5.3 OIC mechanics

- **OIC application fee and initial payment** — Application fee: $205 (waived for low-income taxpayers). Initial payment with offer: Lump Sum — 20% of the offer amount; Periodic — the first monthly installment, with continued monthly installments while the IRS evaluates (up to 24 months). Forms: Form 656 (Offer in Compromise) + Form 433-A (OIC) for individuals or Form 433-B (OIC) for businesses; the 433-A (OIC) is more detailed than the standard 433-A used in IAs. Processing time: 9–24 months; the IRS has 24 months under §7122(f) to evaluate, after which the offer is deemed accepted if no decision has issued (in practice, IRS evaluators meet the deadline). Acceptance rate: approximately 30% in recent years (IRS Data Book); acceptance rate is highly correlated with practitioner involvement — pro se offers acceptance is lower; CPA/EA-prepared offers significantly higher. All collection action is suspended while the OIC is pending under §6331(k)(1). The CSED is tolled while the OIC is pending plus 30 days under §6331(k)(1).  _(§7122(f); §6331(k)(1))_

#### 6.5.4 OIC compliance and the 5-year trap

- **OIC 5-year compliance requirements** — If accepted, the taxpayer must: 1. File all required returns on time for 5 years after acceptance. 2. Pay all tax liabilities on time for 5 years after acceptance. 3. Comply with the terms of the offer (pay the offer amount as agreed).

If the taxpayer fails any of these conditions within 5 years, the OIC is defaulted, the original liability is restored in full (less any payments made), the IRS may immediately resume collection, and the CSED for the original liability is reinstated as if the OIC had never been accepted. The Tax Court has consistently upheld this in cases like Bergdale v. Commissioner and Mason v. Commissioner. The CPA who shepherds a client through OIC acceptance must remain engaged for the 5-year compliance period, or hand off to a successor with explicit notice of the compliance obligation.

### 6.6 Innocent Spouse Relief under §6015

- **Innocent spouse relief overview** — A joint return creates joint and several liability for both spouses (§6013(d)(3)). Innocent spouse relief lets a spouse escape that liability for certain understatements caused by the other spouse. Three forms of relief: 1. §6015(b) — 'traditional' innocent spouse: available when the requesting spouse did not know or have reason to know of the understatement, and it would be inequitable to hold them liable; limited to understatements (not underpayments where reported tax is unpaid). 2. §6015(c) — separation of liability: available to spouses who are divorced, legally separated, or living apart for the past 12 months; allocates the deficiency between the spouses based on who earned the income / claimed the deductions. 3. §6015(f) — equitable relief: catchall for cases not covered by (b) or (c); includes both understatements and underpayments; applied via the factors in Rev. Proc. 2013-34 — marital status, economic hardship, knowledge, abuse, mental/physical health, etc. Form 8857 must be filed within 2 years of the IRS's first collection action against the requesting spouse for §6015(b) and (c); §6015(f) has no statutory deadline but practical deadlines exist (CSED, collection action). Tax Court has jurisdiction under §6015(e) to review denials.  _(§6013(d)(3); §6015(b); §6015(c); §6015(f); Rev. Proc. 2013-34; §6015(e))_

### 6.7 Injured Spouse Allocation under §6402

- **Injured spouse allocation definition** — Distinct from innocent spouse: injured spouse addresses the situation where a joint refund is seized to pay one spouse's separate debt (back taxes, student loans, child support). The 'injured' (non-debtor) spouse files Form 8379 to allocate the refund — recovering their share of the joint refund based on their share of the income, withholding, and credits. Form 8379 may be filed with the original joint return or separately afterward. The IRS allocates the refund and issues the injured spouse's share. Injured spouse is not a defense to collection; it only protects the non-debtor's share of refunds.  _(§6402)_

### 7.1 Audit types

**Audit types table**

| Type | Where | Complexity | Typical issues |
| --- | --- | --- | --- |
| Correspondence | By mail | Low | Schedule A items, 1099-K mismatches, EITC eligibility, basis on stock sales |
| Office | At an IRS office | Medium | Schedule C profitability, S-corp reasonable compensation, multiple-year issues |
| Field | At taxpayer/business location | High | Wealth taxpayers, business operations, related-party transactions, foreign income |
| Compliance check / soft letter | By mail | None (not an audit) | Pre-audit signaling; IRS asks the taxpayer to consider amending |

## 7. Audit Types and Timeline

### 7.2 The audit timeline

- **Twelve-step audit timeline** — 1. Selection — returns are selected via: Discriminant Inventory Function (DIF) score (each return scored algorithmically against statistical norms, high-scoring returns flagged for human review); information return matching (1099/W-2 mismatches exceeding AUR thresholds); related-party referrals (an audit of one taxpayer surfaces issues with a related taxpayer); Random NRP (National Research Program) selection (approximately 0.1% of returns selected at random for full-scope audits used to calibrate DIF); whistleblower referrals under §7623. 2. Initial contact — Letter 2202 (correspondence audit) or Letter 2205 (in-person); the letter identifies the issues at intake. 3. Information Document Request (IDR) — Form 4564, lists documents the agent needs, often issued multiple times during the audit. 4. Examination — document review, interviews, third-party contacts (subject to §7602(c) notice requirements). 5. Closing conference — agent presents proposed adjustments. 6. Form 4549 (Examination Changes) — written report with adjustments, accompanied by Form 886-A (Explanation of Items); taxpayer signs to agree or refuses. 7. 30-day letter (Letter 525 / 692 / 950) — cover letter inviting protest to Appeals. 8. Protest to Appeals — formal written protest under IRM 4.10.8. 9. Appeals conference — settlement discussion with Independent Office of Appeals. 10. Statutory Notice of Deficiency (90-day letter, CP3219A) — if no agreement. 11. Tax Court petition — within 90 days. 12. Tax Court trial or settlement — most cases settle.  _(§7623; §7602(c); IRM 4.10.8)_

### 7.3 §7430 — Recovery of Attorney Fees

- **§7430 attorney fee recovery conditions** — If the taxpayer prevails in an administrative or court proceeding against the United States, §7430 permits recovery of reasonable administrative and litigation costs, including attorney fees, subject to limits: attorney fee rate cap of $190/hour for 2025 (verify; the cap is inflation-indexed under §7430(c)(1)(B)(iii)); the taxpayer must have substantially prevailed with respect to either the amount in controversy or the most significant issue; the IRS's position must not have been substantially justified (if the IRS prevails on a key issue at trial but loses overall, the IRS position was probably substantially justified and §7430 fees are denied); the taxpayer must have exhausted administrative remedies (gone through Appeals before going to court, or shown why exhaustion was futile); the taxpayer must not have unduly protracted the proceeding; net worth caps apply (under §2412(d)(2)(B) incorporated by reference): individuals with net worth over $2 million and businesses with over $7 million / 500 employees cannot recover.  _(§7430; §7430(c)(1)(B)(iii); §2412(d)(2)(B))_

§7430 is most useful in cases where the IRS issued a deficiency that was ultimately abated or significantly reduced after litigation. CPAs do not recover their fees under §7430 in their capacity as authorized practitioners except in narrowly defined circumstances; §7430(c)(3) does allow recovery for 'any individual authorized to practice before the Tax Court' who is acting as an attorney, and the regulation extends to non-attorneys in some contexts. Verify the most recent §7430 guidance before relying on CPA fee recovery.

## 8. Forum Choice: Tax Court vs. District Court vs. Court of Federal Claims

When a deficiency proceeds to litigation, the taxpayer chooses among three forums.

### 8.1 United States Tax Court

- **Tax Court features** — Pre-payment forum — the taxpayer does NOT need to pay the deficiency first. Jurisdiction triggered by 90-day letter (CP3219A); petition filed within 90 days (150 if outside US) of the notice. Filing fee $60. No jury — bench trial before a Tax Court Judge or Special Trial Judge. §7463 small tax case ('S case') — if deficiency including penalties is $50,000 or less per year, the taxpayer may elect S case status; simplified procedure, no formal pleadings, no appeal (decision is final). Discovery is limited — Tax Court Rule 70 imposes a 'stipulation' requirement: parties must stipulate to all facts not in dispute before invoking formal discovery. Precedent value — Tax Court decisions are appealable to the federal Court of Appeals in the circuit where the taxpayer resides (under §7482); decisions in 'Tax Court Reports' (T.C. opinions) are precedential; 'Memo' decisions (T.C. Memo) are not binding but are persuasive. Geographic flexibility — Tax Court travels; trials are held in approximately 70 cities nationwide.  _(§7463; §7482; Tax Court Rule 70)_

### 8.2 United States District Court

- **District Court features** — Pay-first forum — the taxpayer must pay the deficiency in full, file a claim for refund (Form 843 or amended return), wait 6 months (or until denial), and then sue under 28 U.S.C. §1346(a)(1). Statute of limitations: §6532 — suit must be filed within 2 years of the IRS denying the refund claim. Jury available — only forum where a jury is available. Full federal civil discovery — FRCP 26–37. No deference to Tax Court precedent — district courts often diverge. Appeals to the federal Court of Appeals in the relevant circuit.  _(28 U.S.C. §1346(a)(1); §6532; FRCP 26-37)_

### 8.3 United States Court of Federal Claims

- **Court of Federal Claims features** — Pay-first forum — same as District Court. Jurisdiction under 28 U.S.C. §1491. No jury — bench trial. Specialized court (handles tax, contract, and other federal monetary claims). Appeals to the Federal Circuit (uniformly, regardless of taxpayer location) — this gives more uniform precedent than the regional Courts of Appeals.  _(28 U.S.C. §1491)_

### 8.4 Forum choice considerations

**Forum choice considerations table**

| Factor | Tax Court | District Court | Claims Court |
| --- | --- | --- | --- |
| Pay first? | No | Yes | Yes |
| Jury? | No | Yes | No |
| Discovery? | Limited | Full | Full |
| Small case option? | Yes (≤$50k) | No | No |
| Tax expertise of judges? | High | Variable | High |
| Geographic convenience? | High (travels) | High (where taxpayer lives) | Low (DC) |
| Filing fee? | $60 | Higher; varies | $400+ |
| Appeal to? | Regional CA | Regional CA | Federal Circuit |

Most small-firm controversy work goes to Tax Court because the pre-payment posture and the $60 filing fee make it accessible. Refund suits are reserved for cases where the taxpayer has already paid (e.g., refused to file a Tax Court petition timely) or where the favorable precedent is in District Court or Claims Court rather than Tax Court.

## 9. The IRS Independent Office of Appeals

The Appeals office is the most underused asset in IRS controversy practice. Approximately 80% of cases reaching Appeals settle without litigation.

### 9.1 What Appeals is

- **Appeals office characteristics** — An administrative office within the IRS, but functionally separate from Examination and Collection. Staffed by Appeals Officers (AOs) who consider the hazards of litigation — i.e., the probability the IRS would lose in court. Authorized to settle cases on grounds Examination cannot (50/50 settlements, percentage settlements, mutual concessions).

### 9.2 When to go to Appeals

- **When to engage Appeals** — After a 30-day letter (audit results) — file a written protest under IRM 4.10.8. After a CDP hearing request (Form 12153) — Appeals conducts the CDP hearing. After a CAP filing (Form 9423) — Appeals reviews the collection action. Direct requests via Fast Track Settlement (FTS) during the audit, before the 30-day letter.  _(IRM 4.10.8)_

### 9.3 Appeals procedures

- **Appeals procedure steps** — Pre-conference position paper — practitioner submits the taxpayer's view of facts and law. Appeals conference — typically by phone or video, informal compared to court. AO determination — may settle, partially settle, or sustain the IRS position; if settled, the taxpayer signs Form 870 or a Form 906 closing agreement. If not settled, the case proceeds to the 90-day letter (if pre-assessment) or to court (if post-assessment).

### 9.4 Strategic considerations

- **Appeals strategic considerations** — Appeals will settle on hazards of litigation, not just on agreement with the taxpayer's view. If the practitioner can identify a 30% chance of taxpayer victory at trial, Appeals may settle at 30%. Appeals will not consider new issues that the taxpayer did not raise with Examination, except in narrow circumstances. Appeals will consider new evidence the taxpayer was unable to produce earlier. The AO has wide discretion; outcomes vary by AO. Sometimes a request to a different AO is appropriate (typically through an Appeals Team Manager).

## 10. Collection Due Process (CDP) under §6330

The CDP hearing is the most important procedural right in collections.

### 10.1 Triggering events

- **§6320 — Notice of Federal Tax Lien Filing** — 30-day window from CP148.  _(§6320)_
- **§6330 — Notice of Intent to Levy** — 30-day window from LT11/CP90/Letter 1058.  _(§6330)_

### 10.2 Filing the CDP request

- **Form 12153 filing requirements** — Form 12153 (Request for a Collection Due Process or Equivalent Hearing). Filed within 30 days of the notice date. File by mail (certified, return receipt) or fax. Always confirm receipt. Identify all issues the taxpayer wants to raise. Issues not raised are forfeited.  _(Form 12153)_

### 10.3 Issues that may be raised at CDP

- **Issues raisable at CDP per §6330(c)** — Appropriateness of the collection action (lien vs. levy vs. nothing). Collection alternatives (IA, OIC, CNC). Spousal defenses (innocent spouse). Existence or amount of the underlying tax liability — only if the taxpayer did not previously have an opportunity to dispute it (no 90-day letter issued, or 90-day letter issued and no petition filed but no actual receipt of the notice).  _(§6330(c))_

### 10.4 Equivalent Hearing

- **Equivalent Hearing rules** — If filed within 1 year of the notice but more than 30 days, the taxpayer gets an "equivalent hearing." Same procedure, but: No Tax Court appeal. §6330(d) requires a timely CDP request. The IRS may resume collection during the equivalent hearing.  _(§6330(d))_

### 10.5 CDP determination

- **CDP determination and Tax Court review** — After the hearing, the AO issues a Notice of Determination. The taxpayer has 30 days to petition the Tax Court for review under §6330(d). The Tax Court reviews: The underlying liability de novo (if properly raised). Other issues for abuse of discretion.  _(§6330(d))_

### 10.6 CDP strategic value

Even when the taxpayer ultimately cannot win on the merits, a CDP filing: Stops collection. Tolls the CSED only marginally (it's tolled during the CDP proceeding, but if the CDP achieves an IA or OIC, the broader value usually outweighs the tolling). Buys time to organize finances, prepare an OIC, or wait out the CSED.

**AUDIT FLASH POINT — file CDP defensively.** If a client receives an LT11/CP90 and the situation is unclear, file Form 12153 by day 28 to preserve all options. The CDP can be withdrawn later if the issues resolve. The 30-day deadline cannot be re-opened.

## 11. Collection Appeals Program (CAP) — Form 9423

CAP is a faster, less procedural alternative to CDP for certain collection actions.

### 11.1 When CAP applies

- **CAP applicability** — Lien filings before NFTL (rarely used). Levy actions (before or after the levy). Installment Agreement terminations / rejections / modifications / denials. Trust Fund Recovery Penalty proposed assertions.

### 11.2 CAP procedure

- **CAP procedure** — File Form 9423 (Collection Appeal Request). Goes directly to Appeals; bypasses ACS or RO escalation. Faster than CDP: typically resolved within 1–4 weeks. No Tax Court access from CAP. The Appeals determination is administratively final.  _(Form 9423)_

### 11.3 CAP vs CDP

CDP preserves Tax Court rights. CAP does not. CAP is faster. CDP can take months. CAP is the right tool for IA defaults and disputes. CDP is the right tool for first-time levy notices.

## 12. Lien Mechanics

### 12.1 The federal tax lien — §6321

- **Federal tax lien arising** — The lien arises automatically when (a) assessment is made, (b) demand for payment, (c) failure to pay. No filing required; the lien attaches to all property and rights to property of the taxpayer, present and future.  _(§6321)_

### 12.2 Notice of Federal Tax Lien (NFTL) — §6323

- **NFTL priority perfection** — The NFTL is the public filing that perfects the lien's priority. Without an NFTL, the lien is valid against the taxpayer but loses priority to subsequent purchasers, holders of security interests, mechanic's lienors, and judgment lien creditors. The NFTL is filed in the public records of the county where the taxpayer resides or where real property is located. It appears on credit reports under historical FCRA rules; recent FCRA amendments have removed tax liens from most credit reports, but the underlying lien still attaches to property.  _(§6323)_

### 12.3 Lien removal options

**Lien removal options**  _(§6325)_

| Option | Authority | Effect |
| --- | --- | --- |
| Release | §6325(a) | Full satisfaction or unenforceability. Self-releasing NFTL releases automatically at CSED. |
| Discharge | §6325(b) | Specific property is released from the lien (e.g., to allow sale). Other property remains encumbered. |
| Subordination | §6325(d) | Another creditor takes priority over the IRS on specific property (e.g., to refinance). |
| Withdrawal | §6325(j) | NFTL is removed from public records as if never filed. Lien itself remains, but priority is lost. |

### 12.4 Withdrawal under the Fresh Start initiative

- **Fresh Start lien withdrawal procedure** — Under the Fresh Start program (IRS announcement 2011 onward), a taxpayer in a direct-debit installment agreement with a balance under $25,000 may request lien withdrawal after 3 successful payments. The procedure: Set up a direct-debit IA (essential — non-direct-debit IAs don't qualify). Make 3 monthly payments by direct debit. File Form 12277 (Application for Withdrawal of Filed NFTL). Wait for IRS approval. Lien withdrawal is significant for clients trying to refinance a home or obtain credit. The withdrawal does not affect the underlying balance; it only removes the public lien notice.  _(Fresh Start initiative; Form 12277)_

## 13. Levy Mechanics under §6331

### 13.1 Levy types

- **Continuous wage levy** — Continuous wage levy (Form 668-W). Attaches to each paycheck until released or balance paid.  _(Form 668-W)_
- **One-time bank levy** — One-time bank levy (Form 668-A). 21-day hold (§6332(c)) before bank remits.  _(§6332(c))_
- **Accounts receivable levy** — Attaches to amounts owed by third parties to the taxpayer.
- **Asset seizure** — Asset seizure (real or personal property). Real property requires court approval (§6334(e)).  _(§6334(e))_

### 13.2 Exempt property under §6334

- **Wearing apparel and school books** — exempt  _(§6334(a)(1))_
- **Fuel, provisions, furniture, personal effects exemption** — 11,000 USD (2025; verify against most recent inflation adjustment)  _(§6334(g))_
- **Books and tools of trade exemption** — 5,000 USD (2025)  _(§6334)_
- **Other exempt items** — Unemployment benefits, certain workers' comp, certain public assistance. Minimum exempt wages per Publication 1494 (varies by filing status and pay frequency). Court-ordered child support payments. Service-connected disability benefits.  _(Publication 1494)_

### 13.3 Levy release grounds — §6343

- **Levy release grounds** — The IRS will release a levy if: The liability has been paid. The CSED expired. The taxpayer is in an installment agreement (and the IA terms permit release). The levy creates immediate economic hardship. The fair market value of the property exceeds the liability and partial release would not affect collection.  _(§6343)_

Filing Form 911 (Taxpayer Advocate request) is an effective accelerant for hardship-based releases.

## 14. Penalty Abatement

### 14.1 §6651 — Failure to file / failure to pay

- **§6651(a)(1) — Failure to file** — 5% per month, max 25%, of the unpaid tax. Minimum penalty for failure to file > 60 days: lesser of $485 (2024; verify inflation adjustment for 2025) or 100% of the tax.  _(§6651(a)(1))_
- **§6651(a)(2) — Failure to pay** — 0.5% per month, max 25%, of the unpaid tax. Increases to 1% per month after the IRS issues a §6331(d) notice.  _(§6651(a)(2))_
- **§6651(a)(3) — Failure to pay after deficiency notice** — 0.5% per month.  _(§6651(a)(3))_
- **Combined cap when both §6651(a)(1) and (a)(2) apply** — The §6651(a)(1) and §6651(a)(2) penalties are reduced when both apply: combined cap of 5% per month (the failure-to-file penalty is reduced by the failure-to-pay penalty in the same month).  _(§6651)_
- **§6651(f) — Fraudulent failure to file** — 15% per month, max 75%.  _(§6651(f))_

### 14.2 §6662 — Accuracy-related penalty

- **§6662 base rate** — 20% (or 40% in certain cases) of the underpayment attributable to: Negligence or disregard of rules / regulations.  _(§6662)_
- **Substantial understatement of income tax threshold** — Greater of 10% of the correct tax or $5,000 for individuals; for corporations, the higher of 10% or $10,000, or for certain large corporations, lesser of 10% or $10 million.  _(§6662)_
- **Substantial valuation misstatement** — 150% or more of correct value: 20%.  _(§6662)_
- **Gross valuation misstatement** — 200% or more: 40%.  _(§6662)_
- **Transfer pricing adjustments** — Subject to §6662 accuracy-related penalty.  _(§6662)_
- **Reportable transaction understatements** — 20% (30% if no disclosure).  _(§6662)_

### 14.3 §6663 — Fraud penalty

- **Civil fraud penalty** — 75% of the underpayment attributable to fraud. Civil fraud requires clear and convincing evidence (a higher standard than the preponderance standard for §6662). Practitioner-prepared returns where the practitioner relied on taxpayer information are rarely §6663 cases against the practitioner.  _(§6663)_

### 14.4 Criminal penalties — §§7201, 7203, 7206

- **§7201 — Tax evasion** — Felony, up to 5 years, $100,000 fine ($500,000 for corporations).  _(§7201)_
- **§7203 — Willful failure to file / pay** — Misdemeanor, up to 1 year per year.  _(§7203)_
- **§7206 — Fraud and false statements** — Felony, up to 3 years.  _(§7206)_
- **§7207 — Submitting false documents** — Up to 1 year.  _(§7207)_

Criminal exposure shifts the engagement to a criminal tax attorney immediately.

### 14.5 First-Time Abatement (FTA) — Notice 2014-2 / IRM 20.1.1.3.3.2.1

- **FTA eligibility conditions** — The IRS will administratively abate failure-to-file, failure-to-pay, and failure-to-deposit penalties for a single tax period if: 1. The taxpayer has no penalties of the relevant type in the prior 3 tax years (other than the §6654 estimated tax penalty). 2. All currently required returns have been filed (or extensions filed). 3. The taxpayer has paid, or arranged to pay, any tax due.  _(Notice 2014-2 / IRM 20.1.1.3.3.2.1)_
- **FTA process** — FTA is granted by phone (PPL) or letter. No forms required. Fast and reliable.  _(Notice 2014-2 / IRM 20.1.1.3.3.2.1)_

FTA is a once-per-3-years opportunity. If a client has multiple years of penalties, use FTA on the year with the largest penalty.

### 14.6 Reasonable Cause — §6651, §6664, IRM 20.1.1

- **Reasonable cause standard** — Penalty abatement for reasonable cause is available when the taxpayer can demonstrate that the failure was due to facts beyond the taxpayer's control, despite the exercise of ordinary business care and prudence.  _(§6651, §6664, IRM 20.1.1)_
- **Common reasonable cause grounds** — Illness or hospitalization of the taxpayer or immediate family. Death of taxpayer or family member. Natural disaster (often pre-empted by automatic disaster relief). Inability to obtain records despite reasonable efforts. Reliance on a tax professional (limited; the taxpayer must show that reliance was reasonable — Boyle limits this to substantive advice, not ministerial filings). Mistake of law (rarely accepted). Erroneous IRS written advice — §6404(f) (statutory exception, mandatory abatement if proven).  _(IRM 20.1.1; Boyle; §6404(f))_

The taxpayer must document the facts contemporaneously and provide supporting evidence (medical records, death certificates, etc.).

### 14.7 Statutory exception — §6404(f)

- **§6404(f) mandatory abatement** — If the taxpayer wrote to the IRS, asked a specific question, received written advice, and relied on it, and the advice was wrong, the IRS must abate any penalty resulting from that reliance under §6404(f). Limited to written advice; oral advice does not qualify.  _(§6404(f))_

## 15. Taxpayer Rights under §7521

- **§7521(a) — Right to record interviews** — The taxpayer may make an audio recording of any in-person interview, with 10 days' prior notice.  _(§7521(a))_
- **§7521(b)(1) — Right to clear and complete explanation** — The IRS officer must explain the audit process and the taxpayer's rights at or before the first in-person interview.  _(§7521(b)(1))_
- **§7521(b)(2) — Right to representation** — The taxpayer may be represented by any person authorized to practice before the IRS (CPA, EA, attorney, enrolled actuary, enrolled retirement plan agent, or registered tax return preparer in limited contexts).  _(§7521(b)(2))_
- **§7521(c) — Right not to attend** — If the taxpayer is represented, the IRS cannot require the taxpayer to be present. The representative attends alone. Exception: if the IRS issues an administrative summons under §7602.  _(§7521(c))_

### 15.1 Form 2848 — Power of Attorney

- **Form 2848 authorizations** — Authorizes a Circular 230 practitioner to represent the taxpayer: Receive and discuss confidential return information. Sign certain documents (waivers, consents to extend statute of limitations). Receive notices and refunds (if box checked). Appear at IRS interviews and conferences.  _(Form 2848)_
- **Form 2848 required specifications** — The 2848 must specify: Tax form (1040, 1120, 941, etc.). Tax years — can cover 3 years past and 3 years forward, plus the current year. Common practice: file with prior 3 years and current year (e.g., 2022, 2023, 2024, 2025 in 2025) plus future 3 years. Acts authorized — full representation, limited representation, signing returns (rare), etc.  _(Form 2848)_
- **CAF processing time** — The 2848 is processed by the IRS Centralized Authorization File (CAF) and typically takes 5–10 business days to post. Once posted, the practitioner can pull transcripts via the Transcript Delivery System (TDS) and call the Practitioner Priority Service (PPS).

### 15.2 Form 8821 — Tax Information Authorization

- **Form 8821 purpose** — Authorizes the recipient to receive (but not represent) the taxpayer. Useful for situations where the practitioner needs transcripts but is not yet in a representation engagement. Faster to file than 2848 in some cases.  _(Form 8821)_

## 16. The CPA-Led Resolution Playbook

The mechanical workflow for a collections case, in order.

### Step 1 — Intake

0. **Intake** — Collect all IRS notices the taxpayer has received. Sort by date. Identify all open tax periods. Identify all unfiled returns. Identify the taxpayer's current income and asset picture (high-level). Take a retainer commensurate with the work.

### Step 2 — Authorization

0. **Authorization** — Form 2848 for representation. Cover all relevant years and forms. Form 8821 if a faster route to transcripts is needed. Wait for CAF posting (5–10 business days; can be faxed to the PPS for expedited posting in urgent cases).

### Step 3 — Transcript pull

0. **Transcript pull** — Pull Account Transcripts for each open year. Identify assessment dates (TC 150), penalty assessments (TC 240, 270, 280), interest assessments (TC 196), and collection events (TC 580 IA, TC 530 CNC, TC 480 OIC pending, TC 520 bankruptcy). Pull Wage and Income Transcripts for each year to identify 1099s and W-2s. Pull Return Transcripts for each filed year. Pull Record of Account Transcripts for the combined view.

### Step 4 — Compute the picture

0. **Compute the picture** — Current balance per year. CSED per year. Penalty composition. Identify any FTA-eligible periods. Identify any years with potential reasonable cause arguments. Identify unfiled years and prepare/file them (cannot do an IA or OIC with unfiled returns).

### Step 5 — Choose the alternative

0. **Run the comparison** — Run the comparison of collection alternatives.

**Alternative comparison table**  _(unsure - no explicit citation in source)_

| Alternative | Best when | Worst when |
| --- | --- | --- |
| Full pay | Funds available | High balance, low cash |
| Short-term plan | < 6 months payoff | > 6 months |
| Streamlined IA | < $50k, < 72 months | > $50k or > 72 months |
| Non-streamlined IA | > $50k, can verify disposable income | High asset, no disposable income |
| PPIA | Low income, near CSED, no assets | Short CSED, high income |
| CNC | Hardship, near CSED | Improving income |
| OIC | High balance, low assets, low future income | Recent acceptance, large assets |
| Innocent spouse | Joint return, spouse-caused understatement | Both spouses knew |

### Step 6 — Respond

0. **Respond** — Prepare the appropriate form (9465, 433-F, 656, 12153, etc.). File by certified mail or fax with confirmation. Submit any required payment.

### Step 7 — Calendar follow-up

0. **Calendar follow-up** — Track the IRS's processing timeline (IA: 30 days; OIC: 9–24 months; CDP: 6–12 months). Calendar all post-acceptance compliance obligations (e.g., OIC 5-year compliance). Calendar CSED expiration dates. Calendar the next pull of transcripts to verify status.

### Step 8 — Maintain the engagement

0. **Maintain the engagement** — Each tax year going forward, file and pay on time (especially for OIC clients in the 5-year compliance period). Re-pull transcripts annually to catch any new assessments. Update Form 2848 every 3 years before the prior-year window rolls off.

## 17. Worked Examples

### 17.1 Example 1 — CP2000 Response (a typical Schedule C miss)

**Facts.** Client Maria received a CP2000 dated September 1, 2025 for tax year 2023. The notice proposes additional tax of $4,820 plus interest of $312 plus a §6662(a) accuracy-related penalty of $964, for a total of $6,096. The notice identifies a 1099-NEC from a client of Maria's freelance design business, payer "Acme Marketing LLC," reporting $18,500. Maria's 2023 return reported Schedule C gross receipts of $74,200; she does not recall the Acme 1099.

**Step 1 — Pull transcripts.** Wage and Income transcript confirms the Acme 1099-NEC for $18,500. No other unreported income.

**Step 2 — Reconcile to records.** Maria checks her bank statements. She finds two deposits from Acme totaling $18,500: one for $10,000 on March 15, 2023 and one for $8,500 on August 8, 2023. She finds both in her QuickBooks "Sales" account. Her return reflects them.

**Step 3 — Verify the return.** Pull her 2023 Schedule C. Gross receipts $74,200. Acme's $18,500 is included. The CP2000 is wrong: the IRS is double-counting income that was reported.

**Step 4 — Build the response.**

- Cover letter explaining the situation.
- Annotated copy of Schedule C with the Acme deposits circled.
- Bank statement excerpts showing the deposits.
- QuickBooks Sales report tying to the gross receipts line.
- Marked CP2000 response form indicating DISAGREE with explanation.

**Step 5 — File.** Mail certified to the AUR unit address on the notice. Calendar 60 days for IRS response.

**Step 6 — Outcome.** Approximately 8 weeks later, IRS issues Notice CP2005 (CP2000 closed, no change). No additional tax, no penalty.

**Time and cost.** ~3 billable hours. The takeaway: a CP2000 is not a deficiency; it is a starting point. Read the underlying records before agreeing or panicking.

### 17.2 Example 2 — Structuring an $80,000 Installment Agreement

**Facts.** Client James is a sole proprietor with a $79,200 balance for tax years 2022 ($31,500) and 2023 ($47,700), assessed in October 2024 and June 2025 respectively. He received a CP14 for each, then a CP501 and CP503, and most recently an LT11 dated October 12, 2025 (today's date is November 7, 2025).

James's 2024 return showed Schedule C net income of $94,000. His current disposable income (Form 433-F analysis) is approximately $1,800/month after reasonable living expenses. His assets: $2,200 in checking, an 8-year-old vehicle ($12,000 trade-in value, no loan), no other significant assets.

**Step 1 — Triage the LT11.** The 30-day CDP window expires November 11. Even if everything else is in motion, file Form 12153 by November 10 to preserve CDP rights. Mark "Installment Agreement" as the requested collection alternative.

**Step 2 — Determine streamlined eligibility.** Aggregate balance $79,200 > $50,000 streamlined threshold. Streamlined not available unless the balance is paid down below $50k first.

**Option A — Pay down to streamlined.** James pays $29,500 from a relative's loan or savings to bring the balance to ~$49,700. Then submits a streamlined IA online at, say, $700/month over 72 months. Setup fee $31 direct debit. Done.

**Option B — Non-streamlined IA.** Submit Form 9465 with Form 433-F showing $1,800 disposable income. IRS proposes $1,800/month. Over 72 months that's $129,600 — more than enough to cover the $79,200 plus accrued interest. Approved.

**Step 3 — Decision.** Without the $29,500 cushion, go with Option B. James commits to $1,800/month direct debit. Setup fee $107 (direct debit, by mail).

**Step 4 — Lien strategy.** With balance over $25,000, the IRS may file an NFTL. To avoid: under the Fresh Start program, a taxpayer with balance ≤ $25,000 in a direct-debit IA can request no NFTL filing. James is above. Practitioner notes that after 3 direct-debit payments, James can request lien withdrawal if a lien has been filed (Form 12277).

**Step 5 — File.**

- Form 12153 (CDP) by November 10.
- Form 9465 and 433-F (IA) immediately.
- Withdraw Form 12153 once IA is approved (or let Appeals process it; Appeals will likely confirm the IA).

**Step 6 — Compliance.** James must file and pay all subsequent returns on time. Any default triggers CP523.

**Time and cost.** ~6 billable hours. CSED for 2022 portion: October 2034. CSED for 2023 portion: June 2035. Both are well beyond IA payoff.

### 17.3 Example 3 — Offer in Compromise for $300,000 Liability

**Facts.** Client Patricia has unpaid tax of $312,000 from tax years 2018, 2019, and 2020 (assessment dates 2020, 2021, and 2022 respectively). She is 64, divorced, lives in a rental apartment, and receives Social Security of $1,900/month plus part-time consulting income averaging $1,400/month. Her only significant asset: a 401(k) with $42,000 balance.

**Step 1 — CSED analysis.**

- 2018 (assessed March 2020): CSED March 2030. 4.3 years remaining.
- 2019 (assessed June 2021): CSED June 2031. 5.6 years remaining.
- 2020 (assessed February 2022): CSED February 2032. 6.3 years remaining.

**Step 2 — Compute RCP for a Lump Sum Cash OIC.**

Net Realizable Equity:

- Checking: $1,200 less $1,000 exempt = $200.
- Vehicle (10-year-old sedan, $4,500 FMV): 80% × $4,500 = $3,600 less $3,450 vehicle exemption (Form 433-A OIC standard) = $150.
- 401(k): $42,000 × 70% (after deemed 30% tax cost) = $29,400.
- **NRE total: $29,750.**

Future Income (Lump Sum, 12-month multiplier):

- Total income: $1,900 SS + $1,400 consulting = $3,300/month.
- Allowable expenses (IRS standards):
  - Housing & utilities (regional): $1,600.
  - Food, clothing, etc.: $750.
  - Transportation operating: $250.
  - Healthcare: $130.
  - Health insurance: $250.
  - Total: $2,980.
- **Disposable income: $320/month.**
- **Future income value: $320 × 12 = $3,840.**

**RCP = $29,750 + $3,840 = $33,590.**

Offer at $33,600 (round up slightly to avoid the IRS arguing the RCP).

**Step 3 — Compare alternatives.**

- **Full pay:** $312,000. Not feasible.
- **Streamlined IA:** Not available (balance > $50k).
- **Non-streamlined IA:** $320/month × 60 months (5 years) = $19,200. Doesn't satisfy balance; would default to a PPIA.
- **PPIA:** $320/month for the remaining CSED. Most of the debt expires uncollected at CSED. Total paid over remaining CSED (~6 years average): $320 × 72 = $23,040.
- **CNC:** Zero payment, but the IRS may pull her into IA if income increases. CSED runs.
- **OIC:** $33,600 lump sum (20% = $6,720 with offer, $26,880 within 5 months of acceptance).

**Step 4 — Decision factors.**

- The OIC at $33,600 settles the entire $312,000.
- The PPIA pays only $23,040 over the CSED, but Patricia owes nothing further at CSED. Total cost of PPIA: $23,040. Net benefit to Patricia: same outcome (no debt after CSED) for $10,000 less cash.
- BUT: PPIA leaves the lien in place until CSED. OIC requires lien withdrawal procedures but releases the lien upon payment.
- BUT: PPIA requires Patricia to maintain compliance throughout the CSED. Any year of non-compliance triggers default. OIC requires 5 years of compliance (and the OIC is shorter compliance period than PPIA).
- BUT: PPIA requires Patricia to pass biennial financial reviews. If her consulting income jumps, the IRS may raise the payment.

**Step 5 — Recommendation.**

Recommend the OIC. Reasons:

1. Definitive resolution. Patricia is 64 and the certainty matters more than the cash.
2. Lien release upon payment.
3. Patricia must raise $33,600 in cash. She can borrow $20,000 from her 401(k) (she's over 59½ so no early withdrawal penalty under §72(t); the distribution is taxable but the OIC accepted balance accounts for the 401(k) value already; the trick is paying the resulting tax — she will need to plan for the $4,000–6,000 income tax on the distribution).
4. Five years of compliance is achievable for a Social Security recipient with limited consulting income.

**Step 6 — File.**

- Form 656 (Offer in Compromise).
- Form 433-A (OIC).
- Application fee $205.
- 20% upfront: $6,720.
- Document everything: assets, income, expenses, allowable deviations.

**Step 7 — Wait.** IRS evaluator assigned in ~3 months. Counter-offer is possible. Decision in 9–18 months.

**AUDIT FLASH POINT — OIC 5-year compliance.** If Patricia, in any of the next 5 years, files a return late or fails to pay any tax owed, the OIC defaults, and the $312,000 (less the $33,600 paid) is restored. The CPA must remain engaged to ensure timely filing each year.

**Time and cost.** ~20 billable hours over 12–18 months. Engagement structured as fixed fee plus contingent success bonus.

## 18. Provenance

This skill is grounded in the following authorities and resources:

- **Internal Revenue Code:** §6020 (Substitute for Return), §6151 (timely payment), §6201 (assessment authority), §6203 (record of assessment), §6212 (notice of deficiency), §6213 (90-day window and math error abatement), §6303 (notice and demand), §6320 (lien CDP), §6321 (lien arises), §6323 (NFTL priority), §6325 (release / discharge / subordination / withdrawal), §6330 (levy CDP), §6331 (levy authority), §6332 (bank levy 21-day hold), §6334 (exempt property), §6343 (release of levy), §6402 (refund offset, injured spouse), §6404 (interest abatement, erroneous IRS advice exception), §6501 (assessment SOL), §6502 (collection SOL / CSED), §6503 (tolling), §6532 (refund suit SOL), §6601 (interest), §6651 (failure to file / pay penalty), §6654 (estimated tax penalty), §6662 (accuracy-related penalty), §6663 (fraud penalty), §6672 (Trust Fund Recovery Penalty), §6664 (reasonable cause), §7122 (compromise authority), §7201 (evasion), §7203 (willful failure), §7206 (fraud and false statements), §7430 (attorney fee recovery), §7463 (Tax Court small cases), §7482 (appellate jurisdiction), §7508 (combat zone), §7521 (interview rights), §7525 (federally authorized tax practitioner privilege), §7602 (examination authority), §7623 (whistleblower).

- **Treasury Regulations:** Treas. Reg. §301.6320-1, §301.6330-1, §301.7122-1, §301.6502-1, §1.6664-4 (reasonable cause).

- **IRS guidance:**
  - **Notice 2014-2** (First-Time Abatement, codifying IRM 20.1.1.3.3.2.1).
  - **Rev. Proc. 2013-34** (innocent spouse §6015(f) factors).
  - **Publication 1** (Your Rights as a Taxpayer).
  - **Publication 594** (The IRS Collection Process).
  - **Publication 1494** (exempt amount from wage levy tables).
  - **Publication 1660** (Collection Appeal Rights).
  - **Publication 4681** (Canceled Debts, Foreclosures, Repossessions, and Abandonments).

- **Internal Revenue Manual (IRM):**
  - IRM 4.10.8 (formal protest requirements).
  - IRM 5.1.19 (CSED).
  - IRM 5.8 (Offer in Compromise).
  - IRM 5.14 (Installment Agreements).
  - IRM 5.16 (Currently Not Collectible).
  - IRM 5.19 (Liability Collection).
  - IRM 20.1.1 (penalty handbook).
  - IRM 21.3 (taxpayer contacts).
  - IRM 25.15 (innocent spouse).

- **Key case law:**
  - *United States v. Boyle*, 469 U.S. 241 (1985) — reliance on tax professional for ministerial filing not reasonable cause.
  - *Young v. United States*, 535 U.S. 43 (2002) — bankruptcy tolling of §523(a)(1)(A) priority period.
  - *United States v. Arthur Young & Co.*, 465 U.S. 805 (1984) — no work product privilege for accountants in tax investigations.
  - *Bergdale v. Commissioner*, T.C. Memo 2014-152 — OIC default consequences.
  - Various Tax Court decisions on §6330 CDP review (numerous).

- **Forms cited:**
  - Form 656 / 656-L — Offer in Compromise.
  - Form 433-A / 433-A (OIC) / 433-B / 433-B (OIC) / 433-F — Collection Information Statements.
  - Form 843 — Claim for Refund and Request for Abatement.
  - Form 911 — Request for Taxpayer Advocate Service Assistance.
  - Form 2848 — Power of Attorney.
  - Form 4549 — Examination Changes.
  - Form 4564 — Information Document Request.
  - Form 5564 — Notice of Deficiency Waiver.
  - Form 8821 — Tax Information Authorization.
  - Form 8379 — Injured Spouse Allocation.
  - Form 8857 — Request for Innocent Spouse Relief.
  - Form 9423 — Collection Appeal Request.
  - Form 9465 — Installment Agreement Request.
  - Form 12153 — Request for CDP / Equivalent Hearing.
  - Form 12277 — Application for Withdrawal of NFTL.

## Verification status

pending. This skill has not been reviewed by a Circular 230 practitioner. All dollar amounts, fee schedules, and inflation-indexed figures should be verified against current IRS publications before use in client work. The skill reflects 2025 procedure but does not incorporate any guidance issued after November 15, 2025.

## Companion skills

- `us-tax-workflow-base` (workflow scaffolding — always loaded).
- `us-form-1040-individual-return` (when the underlying issue is a 1040 deficiency).
- `us-sole-prop-bookkeeping` and `us-schedule-c-and-se-computation` (when the AUR or audit hits Schedule C).
- `us-form-941-940-payroll` (when employment tax is at issue, including TFRP).
- `us-federal-return-assembly` (when post-resolution amended return is needed).

## Refusal triggers from this skill

- **CID involvement** — Any indication of CID involvement → refer to criminal tax counsel.  _(Refusal triggers from this skill)_
- **Bankruptcy filing** — Any bankruptcy filing or contemplated filing → refer to bankruptcy counsel.  _(Refusal triggers from this skill)_
- **TFRP defense** — Trust Fund Recovery Penalty defense → refer to specialty.  _(Refusal triggers from this skill)_
- **Whistleblower claims** — Whistleblower claims → refer to specialty.  _(Refusal triggers from this skill)_
- **International collection / FBAR / FATCA** — International collection / FBAR / FATCA penalties → refer to international tax specialty.  _(Refusal triggers from this skill)_

## End of skill

End of skill `us-irs-collections-and-controversy` v0.1.

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
