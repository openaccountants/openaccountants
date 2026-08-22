---
name: us-1099-nec-issuance
description: Tier 2 content skill for determining which contractor payments made by a US sole proprietor or single-member LLC require issuing Form 1099-NEC and producing the information returns for tax year 2025. Covers the §6041A $600 reporting threshold (rising to $600 for electronic payments after repeated deferrals of the §6050W $600 threshold), the corporate exception under Treas. Reg. §1.6041-3(p), the attorney exception under §6045(f), the medical/health care exception under §6041A(a)(2), the Form W-9 collection requirement, backup withholding at 24% under §3406, the January 31 filing deadline under §6071(c), e-filing requirements under §6011(e) and the 2025 threshold of 10 forms, penalties for failure to file under §6721 and failure to furnish under §6722, TIN matching and B-notice procedures, and state filing requirements. MUST be loaded alongside us-tax-workflow-base v0.1+. Federal only.
version: 0.2
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: A licensed accountant (name withheld at their request)
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US 1099 NEC Issuance

## US 1099-NEC Issuance Skill v0.2

## Verified rates & thresholds (accountant-reviewed)

- **Review statement** — Reviewed against the cited tax authorities by a licensed accountant on 2026-06-03. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.  _(n/a)_

### 1099-NEC

- **Threshold** — $600 for 2025 payments (OBBBA raises the threshold to $2,000 for payments after 12/31/2025)  _(IRC 6041A; OBBBA.)_
- **Backup WH** — 24% backup withholding (made permanent by OBBBA)  _(IRC 3406.)_
- **Due** — File with IRS and furnish recipient by January 31 (no automatic 30-day extension)  _(IRC 6071(c); 1099-NEC instr.)_
- **After Aug 1** — 2025 late-filing penalty tiers $60/$130/$330; $330 applies if filed after Aug 1 or not filed  _(IRC 6721; 2025 General Instr. for Certain Information Returns.)_

## What this file is, and what it is not

This file is a content skill that loads on top of us-tax-workflow-base v0.1. It provides the rules for determining which payments to non-employees require issuing Form 1099-NEC, and for producing the information returns correctly and on time. It does not classify the underlying business expenses — that comes from us-sole-prop-bookkeeping. It does not compute Schedule C deductions — the expense is deductible regardless of whether the 1099-NEC is issued (though failure to issue may increase audit risk and trigger penalties).

Tax year coverage. This skill is current for tax year 2025 (forms due January 31, 2026) as of its currency date (April 2026). It reflects the One Big Beautiful Bill Act (Public Law 119-21, signed July 4, 2025) and all IRS guidance available as of the currency date.

Scope. This skill determines, for each payee, whether a 1099-NEC is required, captures the required data fields, flags missing W-9s, computes backup withholding obligations, identifies penalties for late or missing filings, and produces a checklist for the reviewer. It does not prepare the actual electronic filing — that is done through IRS FIRE system, an IRS-approved e-file provider, or paper forms.

The reviewer is the customer of this output. Per the base, this skill assumes a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) reviews and signs off. The skill produces working papers, not filed returns.

## Section 1 — Scope statement

This skill covers Form 1099-NEC issuance for tax year 2025 for filers who are:

- US sole proprietors filing Schedule C, OR
- Single-member LLCs treated as disregarded entities for federal income tax purposes

For the following kinds of work:

- Identifying which payments require a 1099-NEC (the $600 threshold, service vs non-service payments, payee entity type)
- Applying the corporate exception and its carve-outs (attorneys, medical/health care)
- Flagging missing Form W-9s and computing backup withholding obligations
- Verifying TINs and handling B-notices
- Producing the 1099-NEC data for each required payee (Boxes 1, 4, 5-7)
- Computing filing penalties under §6721 and §6722 for late or missing forms
- Identifying the e-filing requirement threshold
- Flagging state filing requirements (Combined Federal/State Filing Program)

This skill does NOT cover:

- Form 1099-MISC — different form for rents, royalties, prizes, etc.
- Form 1099-K — issued by payment settlement entities (PayPal, Stripe, etc.), not by the payer
- Form 1099-INT, 1099-DIV, or other information returns — out of scope
- The Schedule C deduction for the underlying payment — handled by us-sole-prop-bookkeeping
- State-specific information return requirements beyond the Combined Federal/State Filing Program
- Worker classification (employee vs independent contractor) — flagged for reviewer but not adjudicated

## Section 2 — Year coverage and currency

Tax year covered: 2025 (forms due to recipients and the IRS by January 31, 2026).

Currency date: April 2026.

Legislation reflected:
- Internal Revenue Code as in force for tax year 2025
- One Big Beautiful Bill Act (OBBBA), Public Law 119-21, signed July 4, 2025
- American Rescue Plan Act of 2021 §9674 (§6050W threshold reduction — repeatedly deferred)
- IRS Notice 2024-85 (deferral of $600 threshold for third-party settlement organizations to 2026; $5,000 threshold for TY2025)
- IRS Form 1099-NEC Instructions for tax year 2025
- IRS General Instructions for Certain Information Returns (2025)
- Treasury Regulations under §6041, §6041A, §6045(f), and §3406

Currency limitations:
- The §6050W reporting threshold for third-party settlement organizations (Form 1099-K) has been repeatedly deferred. For TY2025, the transitional threshold is $5,000 (per IRS Notice 2024-85). This does NOT affect the 1099-NEC threshold, which remains at $600 under §6041A. However, some payments previously reported on 1099-NEC may also be reported on 1099-K by the payment processor, creating potential duplicate reporting that must be managed.

## Section 3 — Year-specific figures table for tax year 2025

### Filing thresholds

**Filing thresholds**  _(IRC §6041A(a); §6041(a))_

| Figure | Value for TY2025 | Primary source |
| --- | --- | --- |
| 1099-NEC filing threshold (nonemployee compensation) | $600 | IRC §6041A(a); §6041(a) |
| Applies to: payments for services | Yes | IRC §6041A(a)(1) |
| Applies to: payments for goods/merchandise | No | IRC §6041A applies to services; goods are not reportable on 1099-NEC |
| Direct sales threshold (consumer products for resale) | $5,000 | IRC §6041A(b) — reported in Box 2 of 1099-NEC |

### Backup withholding

**Backup withholding**  _(IRC §3406(a)(1))_

| Figure | Value for TY2025 | Primary source |
| --- | --- | --- |
| Backup withholding rate | 24% | IRC §3406(a)(1) |
| Triggers: payee fails to provide TIN | Yes | IRC §3406(a)(1)(A) |
| Triggers: IRS B-notice (incorrect TIN) | Yes | IRC §3406(a)(1)(B) |
| Triggers: payee fails to certify not subject to backup withholding | Yes | IRC §3406(a)(1)(D) |

### Filing deadlines

**Filing deadlines**  _(IRC §6071(c))_

| Figure | Value for TY2025 forms | Primary source |
| --- | --- | --- |
| Due date to recipient | January 31, 2026 (Saturday, so due February 2, 2026) | IRC §6071(c) |
| Due date to IRS (paper) | January 31, 2026 (same — February 2, 2026) | IRC §6071(c) |
| Due date to IRS (electronic) | January 31, 2026 (same — February 2, 2026) | IRC §6071(c) |
| Extension available? | NO — there is no automatic extension for 1099-NEC | IRC §6071(c); IRS instructions |
| 30-day extension by letter? | Only for extraordinary circumstances | IRS Pub 1220, §6081 |

- **Saturday due-date shift note** — January 31, 2026 falls on a Saturday. Per IRC §7503, when a due date falls on a Saturday, Sunday, or legal holiday, the deadline shifts to the next business day — Monday, February 2, 2026.  _(IRC §7503)_

### E-filing threshold

**E-filing threshold**  _(IRC §6011(e); Treas. Reg. §301.6011-2; T.D. 9972 (Feb 2023))_

| Figure | Value for TY2025 | Primary source |
| --- | --- | --- |
| E-filing required if filing ≥ | 10 information returns | IRC §6011(e); Treas. Reg. §301.6011-2; T.D. 9972 (Feb 2023) |

- **E-filing threshold note** — The threshold was reduced from 250 to 10 by T.D. 9972 (February 2023), effective for returns filed in calendar year 2024 and later. For TY2025 forms (filed in January/February 2026), the 10-form threshold applies. The count includes ALL information returns filed (1099-NEC, 1099-MISC, 1099-K, W-2, etc.), not just 1099-NEC.  _(T.D. 9972 (Feb 2023))_

### Penalties for failure to file (§6721) and failure to furnish (§6722)

**Penalties for failure to file (§6721) and failure to furnish (§6722)**  _(IRC §6721)_

| Timing of correction | Penalty per form (2025) | Maximum per year (small business ≤ $5M gross receipts) | Primary source |
| --- | --- | --- | --- |
| Filed within 30 days of due date | $60 | $220,500 | IRC §6721(b)(1); inflation-adjusted |
| Filed after 30 days but by August 1 | $130 | $630,500 | IRC §6721(b)(2); inflation-adjusted |
| Filed after August 1 or not filed | $330 | $1,261,000 ($3,783,000 for large filers) | IRC §6721(a); inflation-adjusted |
| Intentional disregard | $660 per form, no maximum | No cap | IRC §6721(e) |

- **Penalty adjustment note** — Penalty amounts are inflation-adjusted annually. The figures above are for returns required to be filed in calendar year 2026 (i.e., TY2025 forms). The same penalty structure applies to failure to furnish correct payee statements under §6722.  _(IRC §6721; IRC §6722)_

## Section 4 — Primary source library

### Statute (Internal Revenue Code, Title 26 USC)

- **IRC §6041** — Information at source (payments of $600 or more in the course of trade or business)  _(IRC §6041)_
- **IRC §6041A** — Returns regarding payments of remuneration for services and direct sales  _(IRC §6041A)_
- **IRC §6041A(a)(1)** — $600 threshold for service payments  _(IRC §6041A(a)(1))_
- **IRC §6041A(a)(2)** — Payments to corporations generally exempt; medical and legal exceptions  _(IRC §6041A(a)(2))_
- **IRC §6045(f)** — Returns of brokers — payments to attorneys (always reportable regardless of entity type)  _(IRC §6045(f))_
- **IRC §6050W** — Returns relating to payments made in settlement of payment card and third-party network transactions (Form 1099-K, separate from 1099-NEC)  _(IRC §6050W)_
- **IRC §6071(c)** — Due date for 1099-NEC: January 31  _(IRC §6071(c))_
- **IRC §6109** — Identifying numbers (TIN requirement)  _(IRC §6109)_
- **IRC §6721** — Failure to file correct information returns (penalty on filer for IRS copy)  _(IRC §6721)_
- **IRC §6722** — Failure to furnish correct payee statements (penalty on filer for payee copy)  _(IRC §6722)_
- **IRC §6724** — Waiver of penalties for reasonable cause  _(IRC §6724)_
- **IRC §3406** — Backup withholding  _(IRC §3406)_
- **IRC §3406(a)(1)** — Backup withholding rate and triggers  _(IRC §3406(a)(1))_
- **IRC §6011(e)** — Electronic filing requirement  _(IRC §6011(e))_
- **IRC §7503** — Time for performance of acts where last day falls on Saturday, Sunday, or legal holiday  _(IRC §7503)_

### Treasury Regulations

- **Treas. Reg. §1.6041-1** — Return of information as to payments of $600 or more  _(Treas. Reg. §1.6041-1)_
- **Treas. Reg. §1.6041-3(p)** — Exemption for payments to corporations (the corporate exception)  _(Treas. Reg. §1.6041-3(p))_
- **Treas. Reg. §1.6041-3(p)(1)-(4)** — Exceptions to the corporate exception (attorneys, medical, fish purchases, substitute payments)  _(Treas. Reg. §1.6041-3(p)(1)-(4))_
- **Treas. Reg. §1.6045-5** — Information reporting on payments to attorneys  _(Treas. Reg. §1.6045-5)_
- **Treas. Reg. §31.3406-0 through §31.3406(j)-1** — Backup withholding procedures  _(Treas. Reg. §31.3406-0 through §31.3406(j)-1)_
- **Treas. Reg. §301.6011-2** — Electronic filing of information returns (10-form threshold)  _(Treas. Reg. §301.6011-2)_
- **T.D. 9972 (Feb 2023)** — Final regulations reducing e-filing threshold to 10 returns  _(T.D. 9972 (Feb 2023))_

### IRS Publications and Guidance

- **IRS General Instructions for Certain Information Returns (2025)** — Master guide for all 1099 forms  _(IRS General Instructions for Certain Information Returns (2025))_
- **IRS Instructions for Form 1099-NEC (2025)** — Specific instructions  _(IRS Instructions for Form 1099-NEC (2025))_
- **IRS Pub 1220 (2025)** — Specifications for Electronic Filing of Forms 1098, 1099, 5498, and W-2G  _(IRS Pub 1220 (2025))_
- **IRS Pub 1281** — Backup Withholding for Missing and Incorrect Name/TIN(s)  _(IRS Pub 1281)_
- **IRS Notice 2024-85** — Deferral of $600 1099-K threshold to 2026; $5,000 transitional for 2025  _(IRS Notice 2024-85)_

### Form W-9

- **Form W-9 (Rev. March 2024)** — Request for Taxpayer Identification Number and Certification  _(Form W-9 (Rev. March 2024))_

## Section 5 — The basic 1099-NEC filing rule

### When to issue

- **1099-NEC required when all true** — A Form 1099-NEC is required when ALL of the following are true: 1. You made a payment of $600 or more during the calendar year 2. The payment was for services performed in the course of your trade or business (not for merchandise, rent, or other non-service items) 3. The payee is not your employee (employees receive W-2, not 1099-NEC) 4. The payee is not a corporation (unless an exception applies — see Section 6) 5. The payment was made to an individual, partnership, estate, or LLC that is not classified as a corporation for federal tax purposes  _(IRC §6041A)_

### What counts as "services"

- **Services include** — Professional fees (accounting, legal, consulting, design, programming); Contract labor (freelancers, independent contractors, subcontractors); Commissions paid to non-employees; Fees paid to independent directors on a board; Prizes and awards for services (non-employee); Payment for parts AND labor where the labor component cannot be separated (report the full amount)  _(IRC §6041A(a)(1))_
- **Services do NOT include** — Payments for merchandise or goods (no 1099-NEC; may require 1099-MISC for certain categories); Rent payments (reported on 1099-MISC Box 1); Royalties (reported on 1099-MISC Box 2); Payments made via credit card, debit card, or third-party payment network (e.g., PayPal, Stripe) — these are reported by the payment settlement entity on Form 1099-K, NOT by the payer on 1099-NEC; Payments to employees (reported on W-2)  _(IRC §6041A applies to services; goods are not reportable on 1099-NEC)_

### The $600 threshold

- **Threshold applies per payee, per year** — The threshold applies per payee, per calendar year. If total payments to a single payee for services reach $600, the entire amount is reported — not just the amount over $600.  _(IRC §6041A(a))_

## Section 6 — The corporate exception and its carve-outs

### General rule: corporations are exempt

- **Corporations generally exempt** — Under Treas. Reg. §1.6041-3(p), payments to corporations (C-corps and S-corps) are generally exempt from 1099-NEC reporting. This includes: C-corporations; S-corporations; LLCs that have elected corporate treatment (checked "C Corporation" or "S Corporation" on Form W-9 Line 3). How to identify corporate payees: The payee's Form W-9 indicates entity type on Line 3. If the payee checks "C Corporation" or "S Corporation," no 1099-NEC is required (unless an exception below applies).  _(Treas. Reg. §1.6041-3(p))_

### Exception 1 — Attorneys and legal fees (ALWAYS report)

- **Attorney exception** — Under IRC §6045(f) and Treas. Reg. §1.6045-5, payments to attorneys for legal services must ALWAYS be reported, regardless of whether the attorney is: A sole practitioner; A partnership (law firm); A professional corporation (P.C.); An S-corporation; An LLC taxed as any entity type. This is the broadest exception. If you paid $600 or more to any attorney or law firm for legal services, you must issue a 1099-NEC. The payment is reported in Box 1 (nonemployee compensation) if the attorney performed services for you. If the payment is to an attorney as part of a settlement (gross proceeds), it is reported on 1099-MISC Box 10, not 1099-NEC.  _(IRC §6045(f); Treas. Reg. §1.6045-5)_

### Exception 2 — Medical and health care payments

- **Medical and health care exception** — Under IRC §6041A(a)(2) and Treas. Reg. §1.6041-3(p)(3), payments for medical or health care services must be reported on 1099-MISC Box 6 (not 1099-NEC) regardless of corporate status. This applies to payments to: Physicians and medical professionals; Hospitals; Medical corporations. Note for sole proprietors: This exception is most relevant to businesses that pay for occupational health services, drug testing, or similar. It does NOT apply to the taxpayer's own health insurance premiums (those are a personal deduction under §162(l), not a 1099 situation).  _(IRC §6041A(a)(2); Treas. Reg. §1.6041-3(p)(3))_

### Exception 3 — Fish purchases

- **Fish purchase exception** — Under IRC §6050R, payments of $600 or more for fish purchased for resale are reportable regardless of corporate status. Reported on 1099-MISC Box 11. Unlikely to apply to most sole proprietors in scope.  _(IRC §6050R)_

### Exception 4 — Substitute payments in lieu of dividends or interest

- **Substitute payment exception** — Under Treas. Reg. §1.6041-3(p)(4), substitute payments in lieu of dividends or tax-exempt interest are reportable regardless of corporate status. Unlikely to apply to most sole proprietors in scope.  _(Treas. Reg. §1.6041-3(p)(4))_

## Section 7 — Form W-9 collection and backup withholding

### The W-9 requirement

- **W-9 provides** — Before making the first payment to a new contractor, the payer should collect a completed Form W-9. The W-9 provides: Payee's legal name; Business name (if different); Federal tax classification (individual, partnership, C-corp, S-corp, LLC, etc.); Exemption codes (if applicable); TIN (SSN or EIN); Certification that the TIN is correct and the payee is not subject to backup withholding.  _(Form W-9 (Rev. March 2024))_

### What happens without a W-9

- **Backup withholding obligation without W-9** — If the payee fails to provide a W-9 (or provides one without a TIN), the payer is required to begin backup withholding at 24% on all subsequent payments. Backup withholding mechanics: 1. Withhold 24% from each payment 2. Deposit withheld amounts using Form 945 (Annual Return of Withheld Federal Income Tax) 3. Report the withholding on the 1099-NEC in Box 4 4. File Form 945 by January 31 of the following year Practical reality: Many small business owners do not know about the backup withholding requirement and simply fail to collect W-9s. The skill flags missing W-9s and notes the backup withholding obligation, but most sole proprietors will not have actually withheld. The reviewer should note the compliance gap.  _(IRC §3406(a)(1)(A))_

### TIN matching

- **TIN Matching program** — The IRS offers an online TIN Matching program (available through the IRS e-Services portal) that allows payers to verify that a payee's name/TIN combination matches IRS records before filing. This is optional but recommended, especially for payees with unfamiliar names or when the W-9 appears inconsistent.  _(IRS e-Services)_

### B-notices (IRS CP2100 / CP2100A)

- **B-notice procedures** — If the IRS identifies a name/TIN mismatch on a filed 1099, it sends a B-notice to the filer: - First B-notice (CP2100/CP2100A): The filer must solicit a new W-9 from the payee within 15 business days and begin backup withholding if the payee does not respond within 30 days - Second B-notice (within 3 years): The filer must instruct the payee to contact the IRS or SSA to verify their TIN. The filer must begin backup withholding immediately and cannot accept a new W-9 alone — the payee must provide IRS/SSA validation  _(IRS CP2100/CP2100A procedures)_

## Section 8 — Filing mechanics

### Paper vs electronic filing

**Paper vs electronic filing**  _(IRS FIRE system)_

| Filing method | When required | How |
| --- | --- | --- |
| Paper (Copy A to IRS) | Fewer than 10 total information returns | Mail to IRS with Form 1096 transmittal |
| Electronic (FIRE system or approved provider) | 10 or more total information returns | IRS FIRE system, IRS-approved e-file provider, or commercial software |

- **10-form count includes all info returns** — The 10-form count includes ALL information returns (1099-NEC, 1099-MISC, 1099-K, W-2, 1099-INT, etc.), not just 1099-NECs. A sole proprietor who issues 5 1099-NECs but also files 6 W-2s for employees exceeds the threshold and must e-file everything.  _(IRC §6011(e); Treas. Reg. §301.6011-2)_

### Copies and distribution

**Copies and distribution**  _(IRS Form 1099-NEC Instructions)_

| Copy | Recipient | Due date |
| --- | --- | --- |
| Copy A | IRS | January 31 (February 2, 2026 for TY2025) |
| Copy 1 | State tax department (if applicable) | Varies by state |
| Copy B | Payee (recipient) | January 31 (February 2, 2026 for TY2025) |
| Copy 2 | Payee (for state return, if applicable) | With Copy B |
| Copy C | Filer's records | Retain for at least 3 years |

### Form 1096 transmittal (paper filing only)

- **Form 1096 requirement** — When filing paper 1099-NECs, the filer must include Form 1096 as a cover sheet. One Form 1096 is submitted per type of form (e.g., one 1096 for all 1099-NECs, a separate 1096 for all 1099-MISCs).  _(IRS General Instructions for Certain Information Returns (2025))_

### Corrected returns

- **Corrected return procedure** — If a 1099-NEC was filed with errors, a corrected return must be filed: - Check the "CORRECTED" box on the form - File with the IRS and furnish to the payee - Two types of corrections: Type 1 (wrong amount, code, or checkbox) and Type 2 (wrong payee name/TIN — requires filing a zero return for the incorrect payee and a new return for the correct payee)  _(IRS General Instructions for Certain Information Returns (2025))_

## Section 9 — State filing requirements

### Combined Federal/State Filing Program (CF/SF)

- **CF/SF program** — The IRS offers the CF/SF program, which automatically forwards 1099 data to participating state tax agencies when the filer e-files through the FIRE system. Many (but not all) states participate. Participating states include most states with an income tax. Notable non-participants or states with special requirements include: - States with no income tax (TX, FL, NV, WA, WY, SD, AK, NH, TN) — no state filing required - States that require separate filing even if participating in CF/SF (varies; check current year list)  _(IRS Combined Federal/State Filing Program)_

### State-specific thresholds

Some states have lower reporting thresholds than the federal $600. The skill flags this for reviewer attention but does not track all 50 state thresholds. The reviewer should verify state requirements for each payee's state.

## Section 10 — Conservative defaults table

**Conservative defaults table**  _(Various — see individual rationale cells)_

| Situation | Conservative default | Rationale |
| --- | --- | --- |
| Payee's entity type unknown (no W-9) | Treat as non-corporate; issue 1099-NEC | Avoids §6721 penalty for failure to file |
| Payment includes both goods and services, amounts unclear | Report full amount on 1099-NEC | Cannot exclude goods component without clear documentation |
| Payment made via Venmo/Zelle personal (not business) account | Issue 1099-NEC | Personal P2P payments are not reportable by the payment processor; payer retains 1099-NEC obligation |
| Payee provided TIN but no W-9 | Issue 1099-NEC with TIN provided; flag missing W-9 for reviewer | Better to file with a TIN than to not file at all |
| Payment just below $600 to a single payee | Do not issue 1099-NEC but document the total | Threshold is statutory; no obligation below $600 |
| Attorney's law firm is an S-corp | Issue 1099-NEC (attorney exception overrides corporate exception) | §6045(f) applies regardless of entity type |
| Unsure whether payee performed "services" vs provided "goods" | Treat as services; issue 1099-NEC | Conservative; penalties for failure to file exceed any cost of over-reporting |

## Section 11 — PROHIBITIONS

The skill MUST NOT:

1. File 1099-NECs or transmit data to the IRS — the skill produces working papers and data; filing execution is the filer's responsibility
2. Classify workers as employees vs independent contractors — this is a complex legal determination (common law test, Form SS-8, state ABC tests) that the skill flags for reviewer attention but does not adjudicate
3. Advise payers to avoid 1099 obligations by paying via credit card — while credit card payments shift reporting to the payment processor (1099-K), deliberately restructuring payments to avoid 1099-NEC is not a legitimate compliance strategy
4. Accept a payee's verbal assertion of corporate status — entity type must be documented on Form W-9; verbal or email claims are insufficient
5. Report the same payment on both 1099-NEC and 1099-K — if the payment was made via a payment settlement entity (credit card, PayPal Business, etc.), the payment processor issues the 1099-K and the payer does NOT issue a 1099-NEC for that payment
6. Waive backup withholding requirements — if a W-9 is missing, the legal obligation to backup withhold exists regardless of practical difficulty
7. Issue 1099-NEC to employees — employees receive W-2; misclassification has severe consequences (§3509 penalties, FICA liability, worker protections)
8. Ignore state filing requirements — flag for reviewer even when out of scope for detailed state analysis

## Section 12 — Edge cases

If the payment was processed through a third-party settlement organization (PayPal Business, Stripe, Square), the payment processor is responsible for issuing Form 1099-K to the payee. The payer does NOT issue 1099-NEC for that payment. However, payments through peer-to-peer (P2P) transfers (Venmo personal, Zelle, Cash App personal) are NOT considered third-party settlement organization transactions — the payer retains the 1099-NEC obligation. The distinction turns on whether the payment processor is a "third-party settlement organization" under §6050W. Flag for reviewer when the payment method is ambiguous.

The entity type for 1099 purposes depends on the LLC's federal tax classification, as shown on its W-9. If the SMLLC is disregarded (default), report using the owner's name and SSN/EIN. If the SMLLC elected S-corp or C-corp treatment, the corporate exception applies (unless an attorney or medical exception kicks in). The W-9 controls.

Payments for services performed in the US by a nonresident alien are reported on Form 1042-S, not 1099-NEC. The payer must collect Form W-8BEN (not W-9) and withhold at 30% under §1441 (or a reduced treaty rate). This is a fundamentally different regime. The skill flags foreign payees and defers to the reviewer.

If a payee dies during the year, the 1099-NEC should be issued in the decedent's name and TIN for payments made before death. Payments to the estate after death should be issued to the estate using the estate's EIN (if obtained). Flag for reviewer.

Payments to a joint venture that is not a partnership (e.g., a qualified joint venture under §761(f) for a married couple) should be reported to each spouse separately based on their share. Payments to a disregarded entity should use the owner's TIN. The W-9 should clarify, but many joint arrangements are informal. Flag for reviewer.

Payments that reimburse a contractor for expenses (e.g., travel reimbursement) are generally included in the 1099-NEC total if paid directly to the contractor. Only amounts paid under an accountable plan with adequate accounting and return of excess are excludable — and accountable plans generally apply to employees, not independent contractors. Include reimbursements in the 1099-NEC amount. Flag for reviewer if the amounts are large.

When a sole proprietor pays a staffing agency that provides workers, the 1099-NEC goes to the staffing agency (not to the individual workers). The agency is the payee. If the agency is a corporation, the corporate exception may apply. Collect the agency's W-9.

When multiple small payments to the same payee aggregate to exactly $600 or slightly above, the 1099-NEC is required. The threshold is met at $600.00, not $600.01. Track cumulative payments per payee throughout the year.

When a sole proprietor makes a legal settlement payment, the full gross amount paid to the attorney's trust account is reportable — not just the attorney's fee portion. If the attorney distributes part to the claimant, the attorney reports that distribution. The payer reports the gross payment to the attorney. This is reported on 1099-MISC Box 10 (gross proceeds to attorney), not 1099-NEC Box 1, unless the payment is purely for legal services rendered to the payer.

Payments made in virtual currency (e.g., Bitcoin) are treated as property payments. The fair market value of the virtual currency on the date of payment is used for the $600 threshold and reporting amount. The payer must determine FMV and report on 1099-NEC if the payment was for services. Flag for reviewer due to valuation complexity.

## Section 13 — Test suite

### Test 1 — Standard contractor payment

Input: Sole proprietor paid a freelance graphic designer $8,500 during TY2025. Designer provided W-9 showing: individual, SSN, no corporate entity.
Expected output:
- 1099-NEC required: YES
- Box 1: $8,500.00
- Box 4: $0.00 (no backup withholding — W-9 on file)
- Filing deadline: February 2, 2026 (January 31 falls on Saturday)

### Test 2 — Payment to S-corporation (corporate exception applies)

Input: Sole proprietor paid an IT consulting firm $12,000 during TY2025. Firm's W-9 shows: S-Corporation, EIN.
Expected output:
- 1099-NEC required: NO (corporate exception under Treas. Reg. §1.6041-3(p))
- Document the W-9 on file showing S-corp status

### Test 3 — Payment to attorney's professional corporation

Input: Sole proprietor paid $4,200 to "Smith & Jones, P.C." (a professional corporation) for contract review services during TY2025. W-9 shows: C-Corporation.
Expected output:
- 1099-NEC required: YES (attorney exception under §6045(f) overrides corporate exception)
- Box 1: $4,200.00
- Filing deadline: February 2, 2026

### Test 4 — Missing W-9 with backup withholding

Input: Sole proprietor paid a handyman $3,600 during TY2025. No W-9 was collected. No backup withholding was actually performed.
Expected output:
- 1099-NEC required: YES (treat as non-corporate per conservative default)
- Box 1: $3,600.00
- Box 4: $0.00 (backup withholding was legally required but not performed)
- Reviewer flag: Missing W-9. Backup withholding at 24% ($864) should have been withheld under §3406. Compliance gap to address with client. Potential Form 945 filing obligation.

### Test 5 — Payment via PayPal Business below 1099-K threshold

Input: Sole proprietor paid a virtual assistant $2,400 via PayPal Business during TY2025. VA provided W-9 showing individual status.
Expected output:
- 1099-NEC required: NO — payment was made through a third-party settlement organization (PayPal Business). The payment processor is responsible for 1099-K reporting. The payer does not issue 1099-NEC.
- Note: PayPal's 1099-K threshold for TY2025 is $5,000 (transitional). The VA may not receive a 1099-K either if below threshold, but the payer's obligation is discharged.

### Test 6 — Penalty computation for late filing

Input: Sole proprietor was required to file 3 1099-NECs for TY2025. Filed all three on March 15, 2026 (42 days late). Small business (gross receipts < $5M).
Expected output:
- Filed within 30 days: NO (42 days > 30 days)
- Filed by August 1: YES
- Penalty tier: $130 per form (filed after 30 days but by August 1)
- Total penalty: 3 x $130 = $390
- §6722 penalty for late payee statements: same structure, additional $130 per form if payee copies were also late
- Total potential exposure: $390 (IRS) + $390 (payee) = $780

### Test 7 — Multiple payments aggregating to threshold

Input: Sole proprietor made 8 payments of $80 each to a dog walker throughout TY2025. Total: $640. W-9 on file showing individual.
Expected output:
- Total payments: $640
- Threshold: $600
- 1099-NEC required: YES
- Box 1: $640.00

## Section 14 — Cross-skill references

Inputs from upstream skills:

- From us-sole-prop-bookkeeping: The classified transaction list identifies all payments to non-employees (Schedule C Line 11 — Contract labor, and other service payments). The bookkeeping skill flags payments ≥ $600 to individual payees as potential 1099-NEC candidates.

Outputs to downstream skills:

- This skill does not feed into downstream computation skills. It produces a standalone 1099-NEC filing checklist and data set for the reviewer.

Parallel operation:

- This skill operates in parallel with the computation pipeline (Schedule C/SE, QBI, estimated tax). The 1099-NEC obligation exists independently of whether the expense is deductible.

## Section 15 — Reference material

### Validation status

This file is v0.2 of us-1099-nec-issuance, drafted in April 2026. Penalty amounts and e-filing thresholds are verified against IRC §6721, §6722, and T.D. 9972. Filing deadlines verified against IRC §6071(c) and §7503.

### Known gaps

1. State-specific filing requirements beyond the Combined Federal/State Filing Program are not tracked. The reviewer must verify state obligations for each payee.
2. The skill does not handle Form 1099-MISC, which covers rents, royalties, and other non-service payments. A future companion skill could address 1099-MISC.
3. The interaction between 1099-NEC and 1099-K for payments made via "hybrid" platforms (e.g., Venmo with both personal and business accounts) is evolving. The skill applies the conservative default of issuing 1099-NEC when the payment method is unclear.
4. The skill does not adjudicate worker classification. The distinction between employee and independent contractor is the most consequential decision in information return compliance and is deferred to the reviewer.
5. Penalty amounts are inflation-adjusted annually. The figures in Section 3 are for returns required to be filed in calendar year 2026. Future years will require updates.

### Change log

- v0.1 (April 2026): Stub.
- v0.2 (April 2026): Full skill. Tax year 2025. Built on us-tax-workflow-base v0.1.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ Book a call (https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at openaccountants.com/network.

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
