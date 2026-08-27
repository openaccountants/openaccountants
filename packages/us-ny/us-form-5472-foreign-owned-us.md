---
name: us-form-5472-foreign-owned-us
description: Tier 2 US federal content skill for Form 5472 — Information Return of a 25% Foreign-Owned US Corporation or US Trade-or-Business of a Foreign Corp under IRC §§6038A and 6038C. Covers tax year 2025 including the 2017 T.D. 9796 expansion treating foreign-owned single-member US LLCs as separate "reporting corporations" requiring annual Form 5472 plus a pro forma Form 1120, the $25,000 per-year automatic penalty, reportable related-party transactions with NO de minimis threshold, the §482 transfer pricing nexus, indirect ownership via §318 with §6038A modifications, and the 7-year recordkeeping obligation for foreign owners.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Christopher Aryee
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Form 5472 Foreign Owned US

## Form 5472 — Information Return of 25% Foreign-Owned US Corporations and Foreign Corporations Engaged in a US Trade or Business

## 1. Scope and Purpose

- **Form 5472 purpose** — Form 5472 is the principal information return used by the IRS to monitor cross-border related-party transactions involving: (1) A US corporation that is 25% or more foreign-owned (directly or indirectly), under IRC §6038A, or (2) A foreign corporation engaged in a US trade or business (with effectively connected income), under IRC §6038C, or (3) Since the 2017 Treasury regulations (T.D. 9796), a foreign-owned single-member US LLC (disregarded entity for income tax) that is now treated as a separate "reporting corporation" solely for §6038A reporting purposes. This skill covers all three categories for tax year 2025. It is a Tier 2 content skill and MUST be loaded alongside us-tax-workflow-base v0.2 or later. It assumes a Circular 230 reviewer signs off on every output.  _(IRC §6038A; IRC §6038C)_

### What this skill DOES cover

- Foreign-owned US C corporations of any size (including small startups with foreign founders).
- Single-member US LLCs (SMLLCs) owned 100% by a non-US person — the post-2017 expansion.
- US corporations with 25% or more foreign ownership at any time during the year.
- Foreign corporations with US permanent establishment or ECI requiring §6038C reporting.
- Determination of "reportable transactions" and the absence of a de minimis threshold.
- §482 transfer pricing nexus and recordkeeping obligations.

### What this skill does NOT cover (refusal catalogue)

- **Out of scope items** — - Form 5471 (US-owned foreign corporations — different direction, different form). - Form 8865 (US partnerships in foreign partnerships). - Form 8858 (foreign disregarded entities owned by US persons — also different direction). - Form 1042 / 1042-S withholding on FDAP payments. - §367 outbound transfer reporting. - BEAT (§59A) base erosion computations — see us-gilti-fdii-beat. - §482 transfer pricing study preparation (out-of-scope; refer to specialist). - Multi-jurisdictional treaty analysis beyond the LLC characterization question. If the engagement falls outside scope, refuse politely and refer the taxpayer to a specialist or load the correct skill.

## 2. Statutory Architecture: §6038A vs §6038C

The two statutes are siblings but apply to different entities. Knowing which applies governs the filing mechanics.

### §6038A — Reporting Corporations

- **§6038A reporting corporation definition** — Applies to: - A domestic corporation that is 25% foreign-owned at any time during the tax year, OR - A foreign corporation engaged in a US trade or business (this overlaps with §6038C and is generally administered through §6038A regulations). Under Treas. Reg. §1.6038A-1(c)(1), the term "reporting corporation" includes both: "(i) A domestic corporation that is 25-percent foreign-owned, and (ii) A foreign corporation engaged in trade or business within the United States." The 2017 expansion added a third category by regulation: Treas. Reg. §1.6038A-1(c)(1)(iii): A domestic disregarded entity that is wholly owned (directly or indirectly) by one foreign person is treated as a domestic corporation separate from its owner for the limited purposes of §6038A reporting requirements. This is the rule that pulls foreign-owned US SMLLCs into the §6038A regime, even though for income tax they remain disregarded.  _(Treas. Reg. §1.6038A-1(c)(1); Treas. Reg. §1.6038A-1(c)(1)(iii))_

### §6038C — Foreign Corporation Reporting

- **§6038C scope** — Applies to a foreign corporation that is "engaged in trade or business within the United States" at any time during the tax year, requiring: - Reporting of any related-party transaction with foreign related parties. - Reporting of transactions with US related parties as well (broader than §6038A in this respect). - Maintenance of records sufficient to determine the correct US tax treatment. In practice, foreign corporations file Form 5472 attached to their Form 1120-F (US tax return of a foreign corporation), whereas US corporations and foreign-owned SMLLCs file Form 5472 attached to Form 1120 (or pro forma 1120 for SMLLCs).  _(IRC §6038C)_

## 3. The 25% Foreign Ownership Tests

A US corporation is a "reporting corporation" under §6038A if, at any time during the year, one or more 25% foreign shareholders exist. A "25% foreign shareholder" under §6038A(c)(2) is any foreign person owning at least 25% of the total voting power OR total value of the corporation's stock. There are three lenses to apply, in order:

### 3.1 Direct ownership

- **Direct ownership test** — The foreign person owns 25% or more of the vote or value of the US corporation's stock directly. This is the simple case. Example. A French national personally owns 30% of a Delaware C corp's common stock. The Delaware corp is a reporting corporation, and the French national is a foreign related party.

### 3.2 Indirect ownership

- **Indirect ownership / §318 attribution modifications** — A foreign person is treated as owning stock owned by a foreign or domestic entity in which the foreign person has an ownership interest. Treas. Reg. §1.6038A-1(d) applies the constructive ownership rules of IRC §318 with the modifications in §6038A(c)(5). Key modifications: - The 50% threshold in §318(a)(2)(C) for corporate-to-shareholder attribution is reduced to 10% for §6038A purposes (Treas. Reg. §1.6038A-1(d)(2)(ii)). - Attribution flows through chains of entities (foreign → foreign → US LLC). Example. UK Holdings Ltd owns 100% of Cayman Sub Ltd. Cayman Sub owns 40% of Delaware LLC (treated as a US C corp under check-the-box). UK Holdings is indirectly attributed 40% of Delaware LLC. Delaware LLC is a §6038A reporting corp; UK Holdings, Cayman Sub, and any foreign shareholder of UK Holdings owning 10%+ are all candidates for "foreign related party" classification.  _(Treas. Reg. §1.6038A-1(d); Treas. Reg. §1.6038A-1(d)(2)(ii); IRC §318; §6038A(c)(5))_

### 3.3 Constructive (family) ownership

- **Family attribution under §318(a)(1)** — Under §318(a)(1), an individual is treated as owning stock owned by spouse, children, grandchildren, and parents. For §6038A, this family attribution is fully applied. Example. A foreign national owns 15% directly. His spouse owns 12% directly. Combined attributed ownership = 27%. He is a 25% foreign shareholder; spouse separately is also a 25% foreign shareholder.  _(IRC §318(a)(1))_

### 3.4 Foreign related party

- **Foreign related party identification** — Once a 25% foreign shareholder exists, the regulations identify foreign related parties under §6038A(c)(2): - The 25% foreign shareholder. - Any other person related to the reporting corporation OR the 25% shareholder under §267(b) or §707(b)(1) (family + 25% common ownership of corporations + 50% partnership interests). - Any other foreign person related under §482. All monetary or non-monetary transactions with these foreign related parties are reportable.  _(§6038A(c)(2); §267(b); §707(b)(1); §482)_

### 3.5 The SMLLC short-circuit: 100% triggers the test automatically

- **100% foreign-owned SMLLC automatic trigger** — For a US LLC that is wholly owned by one foreign person (an individual, foreign corporation, foreign partnership, foreign estate, or foreign trust), the 100% ownership obviously satisfies the 25% test. There is no need to perform a vote-vs-value analysis: the disregarded SMLLC is, by definition, a reporting corporation under Treas. Reg. §1.6038A-1(c)(1)(iii).  _(Treas. Reg. §1.6038A-1(c)(1)(iii))_

## 4. The 2017 SMLLC Expansion (T.D. 9796) — AUDIT FLASH POINT

This is the single most misunderstood rule in cross-border small-entity practice.

### 4.1 What the regulation did

- **T.D. 9796 regulatory changes** — Effective for tax years beginning on or after January 1, 2017 (with the form-and-filing mechanics effective for tax years beginning on or after January 1, 2017), the Treasury issued T.D. 9796, amending Treas. Reg. §1.6038A-1 and §301.7701-2 to provide: - A domestic eligible entity (i.e., a US LLC or other entity electing to be disregarded) wholly owned by one foreign person is treated as a domestic corporation for the limited purposes of §6038A reporting and recordkeeping. - The entity must obtain a US EIN (Form SS-4) and file Form 5472 annually attached to a "pro forma" Form 1120.  _(T.D. 9796; Treas. Reg. §1.6038A-1; Treas. Reg. §301.7701-2)_

### 4.2 Why Treasury did this

Pre-2017, a foreign individual could form a Delaware (or Wyoming, New Mexico, etc.) LLC, treat it as disregarded for US income tax, do business through it (receive payments, open bank accounts, hold assets), and never file anything with the IRS if the activity was not effectively connected to a US trade or business. The IRS had no visibility into these entities at all. T.D. 9796 closes that gap by requiring an annual information return regardless of whether tax is owed.

### 4.3 What the SMLLC owner must do

- **Annual SMLLC compliance steps** — For each tax year that the SMLLC is foreign-owned, the LLC must: 1. Have an EIN. Obtain via Form SS-4 if not already done. The "responsible party" line allows a foreign individual without an SSN/ITIN to provide a foreign tax ID; the EIN is issued by phone (international applicants) or by fax/mail (no online EIN for entities whose responsible party lacks an SSN/ITIN). 2. File a "pro forma" Form 1120 by the corporate due date (generally April 15 for calendar year; 6-month extension via Form 7004). Pro forma means: complete only the identifying information on Form 1120 (name, address, EIN, tax year), write "Foreign-owned U.S. DE" across the top, and leave the income/deduction lines blank. Attach a complete Form 5472. 3. File the Form 1120 + 5472 by mail or fax to the special address listed in the Form 5472 instructions (Internal Revenue Service, 1973 Rulon White Blvd., M/S 6112 Attn: PIN Unit, Ogden, UT 84201, or fax to 855-887-7737 — check the latest instructions each filing season). 4. Maintain records for all reportable transactions for as long as they may become material to the administration of any internal revenue law (IRC §6001; Treas. Reg. §1.6038A-3; see §10 below). There is no fixed 7-year statutory period; under §6501(c)(8), if the Form 5472 is not filed, the limitations period for the entire return stays open until three years after the required information is furnished.  _(§6038A(e))_

### 4.4 No income, no activity, no escape

- **Filing obligation independent of activity** — The filing obligation is independent of activity. An SMLLC with: $0 of revenue, $0 of expenses, $0 of US-source income, No US business activity — still must file Form 5472 + pro forma 1120 if any reportable transaction occurred — and the regulations define reportable transactions broadly enough that the formation contribution by the foreign owner is itself reportable (capital contribution = reportable transaction). In practice, virtually every foreign-owned SMLLC has at least one reportable transaction each year (capital contributions, owner draws/distributions, reimbursements, transfers between owner and LLC). AUDIT FLASH POINT. Foreign founders setting up Stripe Atlas, Firstbase, doola, Clerky, or other DIY US LLC formation packages routinely believe the SMLLC has "no tax filing obligation" because it is disregarded. This is wrong. The $25,000-per-year automatic penalty under §6038A(d) applies, and IRS enforcement has been increasing since 2020. Always ask a foreign founder client whether they have filed Form 5472 for every year the LLC has existed.  _(§6038A(d))_

## 5. Reportable Transactions — NO De Minimis Threshold

Form 5472 reports all monetary and non-monetary transactions between the reporting corporation and any foreign related party. Treas. Reg. §1.6038A-2(b) lists the categories; the form's Parts IV, V, and VI carry the dollar amounts.

### 5.1 Categories of reportable transactions

**Principal categories on Form 5472 Parts IV–V**  _(Treas. Reg. §1.6038A-2(b))_

| Line / Part | Category |
| --- | --- |
| Part IV Line 1 | Sales of stock in trade (inventory) |
| Part IV Line 2 | Sales of tangible property other than inventory |
| Part IV Line 3 | Platform contribution transaction payments received |
| Part IV Line 4 | Cost sharing transaction payments received |
| Part IV Line 5 | Rents received (for use of tangible property) |
| Part IV Line 6 | Royalties received (patents, trademarks, copyrights, know-how) |
| Part IV Line 7 | Sales, leases, licenses, etc. of intangible property |
| Part IV Line 8 | Consideration received for technical, managerial, engineering, construction, scientific, or like services |
| Part IV Line 9 | Commissions received |
| Part IV Line 10 | Amounts borrowed (beginning and ending balances) |
| Part IV Line 11 | Interest received |
| Part IV Line 12 | Premiums received for insurance or reinsurance |
| Part IV Line 13 | Other amounts received |
| Part V (mirror) | All of the above, but paid to foreign related party |
| Part VI | Non-monetary and less-than-full consideration transactions |
| Part VII | Additional reportable transactions (capital contributions, distributions, etc.) |

### 5.2 No de minimis — every dollar counts

- **No de minimis threshold** — There is no threshold below which a transaction is exempt. A single $50 reimbursement from the foreign owner to the LLC is reportable. A $1 capital contribution is reportable. This is in contrast to many other international tax forms (e.g., Form 5471 Schedule M, Form 8938) which have explicit thresholds. AUDIT FLASH POINT. Practitioners who file Form 5472 only when transactions exceed $50,000 are applying a wrong rule (possibly confused with Form 5471 Category 4 thresholds or with the §6038B reporting threshold). All §6038A regulations require reporting of every monetary transaction. Two regulatory carve-outs relieve compliance burdens without changing the filing duty. Under the small corporation exception (Treas. Reg. §1.6038A-1(h)), a reporting corporation with less than $10,000,000 of US gross receipts for the taxable year is exempt from the §6038A record-maintenance and agent-authorization requirements, but NOT from filing Form 5472 itself. Under the safe harbor of Treas. Reg. §1.6038A-1(i), the record-maintenance and agent-authorization requirements also do not apply where the aggregate value of gross payments to and from all foreign related parties is $5,000,000 or less AND less than 10% of US gross income. Separately, the Instructions for Form 5472 (12/2024) permit transactions of $50,000 or less to be reported as "$50,000 or less" rather than as an exact dollar amount.  _(Treas. Reg. §1.6038A-2(b))_

### 5.3 Aggregation

- **Aggregation and per-related-party filing** — Transactions of the same type with the same foreign related party are aggregated and reported as a single dollar figure on the appropriate line. A separate Form 5472 is filed for each foreign related party with which there are reportable transactions. So a US LLC with one French founder who personally lent money to the LLC and also received management fees would file one Form 5472 (covering both transactions with the same person), but a US LLC with a French founder + a UK passive investor would file two Forms 5472 (one per related party).

### 5.4 Non-monetary and indirect transactions

- **Extended reporting categories** — Treas. Reg. §1.6038A-2(b)(3) extends reporting to: - Property transfers at less than full consideration. - Services rendered without arm's-length compensation. - Capital contributions of property or cash. - Distributions to the foreign owner. - Loans (beginning and ending balances reported on Lines 10 / corresponding lines in Part V). - Guarantee fees, foreign-currency exchanges, and similar items.  _(Treas. Reg. §1.6038A-2(b)(3))_

## 6. The Pro Forma Form 1120 for Foreign-Owned SMLLCs

The pro forma Form 1120 is the "envelope" through which an SMLLC's 5472 is filed. The form itself is a vehicle for the EIN and identifying information — no income, deductions, or tax is reported on it.

### 6.1 Completing the pro forma 1120

- **Pro forma 1120 completion steps** — Per the Form 5472 instructions (revised annually; cite the 2024 / 2025 instructions in working papers): 1. Top of form: write "Foreign-owned U.S. DE" across the top so it is clearly visible. The instructions do not require red ink or any particular ink color. 2. Item B (Employer Identification Number): enter the LLC's EIN. 3. Item A (Check applicable boxes): leave blank or check "Initial return" / "Final return" as applicable. 4. Name and address: the LLC's legal name and US mailing address. 5. Income (Lines 1–11), Deductions (Lines 12–29), Tax (Lines 30–37): leave blank. 6. Signature: signed by an officer of the LLC (i.e., the foreign owner or a US-resident manager). A paid preparer signs if applicable.  _(Form 5472 instructions)_

### 6.2 Filing channel for SMLLC pro forma 1120

- **Cannot e-file; mail or fax only** — The pro forma 1120 + 5472 cannot be e-filed (e-file rejects pro forma returns). It must be filed by: Mail to the special address in the Form 5472 instructions (Ogden, UT M/S 6112), or Fax to the dedicated fax line listed in the instructions. Most practitioners fax to obtain a transmission record; the fax confirmation is the only easily obtainable evidence of timely filing.  _(Form 5472 instructions)_

### 6.3 What is NOT required for SMLLC pro forma filings

- **Not required items** — - No Schedule C (1120), no Schedule J, no Schedule K, etc. - No estimated tax payments (no income tax is owed). - No Form 7004 extension is needed unless the LLC needs more time — and an extension is available if filed by the due date.

## 7. Due Dates and Extensions

**Due dates and extensions by filer type**

| Filer | Return | 2025 Original Due Date | Extended Due Date (Form 7004) |
| --- | --- | --- | --- |
| Calendar-year C corp | Form 1120 + 5472 | April 15, 2026 | October 15, 2026 |
| Foreign-owned SMLLC | Pro forma 1120 + 5472 | April 15, 2026 | October 15, 2026 |
| Foreign corp with ECI | Form 1120-F + 5472 | April 15, 2026 (if US office) or June 15, 2026 (if no US office) | October 15, 2026 / December 15, 2026 |
| Fiscal-year C corp | Form 1120 + 5472 | 15th day of 4th month after FY end | 6 months later |

## 7. Due Dates and Extensions

- **Extension and no separate deadline rule** — Extension: Form 7004 filed by the original due date extends the filing deadline by 6 months. The extension extends the time to file 5472 as well as the underlying 1120. No separate 5472 filing date. A common error is to think the 5472 has an independent deadline. It does not — its deadline tracks the income tax return.

## 8. §6038A(d) Penalty — $25,000 Per Year, Automatic

This is the rule that gives Form 5472 its enforcement teeth.

### 8.1 The base penalty

- **§6038A(d)(1) base penalty per failure per year** — $25,000 USD (per reporting corporation per failure per year; doubled from $10,000 to $25,000 by §13305 of the Tax Cuts and Jobs Act (effective for tax years beginning after December 31, 2017))  _(IRC §6038A(d)(1))_

### 8.2 The continuing-failure penalty

- **Continuing failure additional penalty** — Under §6038A(d)(2), if the failure continues for more than 90 days after the IRS mails notice, an additional $25,000 per 30-day period (or fraction thereof) is imposed, with no cap. A multi-year failure can therefore accumulate substantial penalties.  _(§6038A(d)(2))_

### 8.3 Automated assessment

- **CP-215 automated penalty assessment** — The IRS uses automated penalty assessment for Form 5472. When a Form 5472 is filed late, missing, or incomplete, the system issues a CP-215 notice (or similar) assessing the $25,000 penalty. Practitioners report a high rate of automated assessment with no manual review. The taxpayer must respond and request abatement; the penalty is not "negotiable" at intake.

### 8.4 Reasonable cause abatement

- **Reasonable cause abatement standard** — §6038A(d)(3) and Treas. Reg. §1.6038A-4(b) provide for abatement upon a showing of reasonable cause. Reasonable cause is fact-specific but typically requires: A written statement explaining the failure. Evidence of ordinary business care and prudence. Reliance on a competent tax professional (with documentation). Promptness of cure (file as soon as the failure is discovered). The IRS publishes guidance in IRM 20.1.9 on penalty abatement for international information returns. First-time abatement (FTA) under IRM 20.1.1.3.6.1 is not generally available for §6038A penalties (FTA applies to common penalties but international information return penalties are excluded). Practitioners typically must rely on reasonable cause arguments.  _(§6038A(d)(3); Treas. Reg. §1.6038A-4(b); IRM 20.1.9; IRM 20.1.1.3.6.1)_

### 8.5 Streamlined Filing Compliance Procedures and other amnesty regimes

- **SFCP and DIIRSP ineligibility** — Foreign-owned SMLLCs with multi-year non-filing are not eligible for the SFCP (which is for individual income tax), but the Delinquent International Information Return Submission Procedures (DIIRSP) remain available. DIIRSP was not terminated: the IRS revised it in November 2020 to remove the automatic penalty-relief language, and taxpayers may still correct noncompliance by submitting the missing Forms 5472 (attached to amended or delinquent pro forma returns) before IRS contact, supported by a reasonable cause statement. Even so, the IRS often assesses the §6038A(d) penalty automatically on receipt of a late form, so be prepared to argue reasonable cause afterward through abatement requests.

### 8.6 §6662 accuracy-related penalty

- **§6662 accuracy-related penalty rates** — In addition to §6038A penalties, the §6662 accuracy-related penalty (20% of underpayment, 40% for gross valuation misstatement) applies if related-party transactions are mispriced under §482. This is the indirect cost of inaccurate 5472 reporting — see §9 below.  _(IRC §6662)_

## 9. §482 Transfer Pricing Implications — AUDIT FLASH POINT

Form 5472 is the gateway to §482 transfer pricing audits. The transactions disclosed on Parts IV–V are the very transactions that the IRS examines under the arm's-length standard.

### 9.1 §482 in one paragraph

- **§482 authority and standard** — IRC §482 authorizes the IRS to reallocate income, deductions, credits, or allowances between controlled taxpayers if doing so is necessary to prevent evasion of taxes or clearly reflect income. The standard is the arm's-length result — what unrelated parties would have agreed to under similar circumstances. Treas. Reg. §1.482-0 through §1.482-9 spell out the methods (CUP, CPM, profit-split, etc.) and documentation.  _(IRC §482; Treas. Reg. §1.482-0 through §1.482-9)_

### 9.2 Documentation safe harbor under §6662(e)

- **Contemporaneous transfer pricing documentation safe harbor** — If a taxpayer maintains contemporaneous transfer pricing documentation that meets the standards of Treas. Reg. §1.6662-6(d), the §6662(e) substantial-valuation-misstatement penalty is avoided even if the §482 adjustment is large. Documentation must include: A general description of the taxpayer's business and industry. A description of the controlled transactions. An analysis of the §482 method selected and why it is the best method. Comparables and benchmarks. A summary of any other methods considered and rejected. For most foreign-owned SMLLCs with simple cross-border transactions (e.g., management fees, royalties, reimbursements), formal documentation is rarely prepared. The practical advice for a small-entity engagement is: Use a defensible pricing method (often "cost plus" for services, "comparable uncontrolled price" for sales of goods). Document the rationale in a memo to file — not a formal study, but a written record of how each related-party charge was set. Be prepared to defend if the IRS examines a Form 5472 disclosure.  _(Treas. Reg. §1.6662-6(d); §6662(e))_

### 9.3 The disclosure-creates-audit risk

- **Full disclosure requirement** — Some practitioners advise foreign founders to minimize the amounts shown on Form 5472 to avoid drawing attention. This is incorrect and constitutes a violation of §6038A(b) which requires "true, accurate, and complete" disclosure. The correct posture is full disclosure with defensible pricing.  _(§6038A(b))_

### 9.4 Coordination with BEAT and GILTI

- **BEAT and GILTI applicability thresholds** — If the reporting corporation is a US C corp with > $500M average gross receipts (high threshold — unlikely to apply to small foreign-owned LLCs), BEAT under §59A may apply to deductible payments to foreign related parties. GILTI (§951A) applies to US shareholders of CFCs and is on a separate axis. For typical foreign founder LLC engagements, BEAT and GILTI do not apply, but the practitioner should confirm. See us-gilti-fdii-beat.  _(IRC §59A; IRC §951A)_

## 10. §6038A(e) — Recordkeeping and Authorization of Agent

§6038A(e) imposes two ongoing obligations on the foreign owner / reporting corporation beyond the annual Form 5472 filing.

### 10.1 The 7-year recordkeeping obligation

- **Minimum recordkeeping period** — No fixed statutory period. Records must be kept for as long as they may become material to the administration of any internal revenue law (IRC §6001; Treas. Reg. §1.6038A-3). Under IRC §6501(c)(8), if the Form 5472 is not filed, the limitations period for the entire return stays open until three years after the required information is furnished. years (Treas. Reg. §1.6038A-3 requires the reporting corporation to maintain permanent books and records sufficient to establish the correctness of the Form 5472 returns filed and the correct US tax treatment of any related-party transaction. Records must be maintained for at least the period of limitations for the relevant return, which under §6501(c)(8) does not begin until the Form 5472 is filed. As a practical matter, records must be kept for at least 7 years (and often longer where 5472 filing history is uncertain).)  _(Treas. Reg. §1.6038A-3; §6501(c)(8))_

### 10.2 The "authorization of agent" requirement

- **Authorization of agent requirement and noncompliance penalty** — §6038A(e) requires the foreign related party to authorize the reporting corporation to act as its agent for purposes of §7602 (summonses), §7603 (service of summonses), §7604 (enforcement of summonses), and §7605 (time and place of examination). The authorization must be in writing. Failure to authorize the agent — or to comply with an IRS summons after authorization — triggers the §6038A(e)(3) "noncompliance penalty": the IRS may determine the reporting corporation's deductions and cost of goods sold based solely on its own information, effectively disallowing all related-party deductions and cost of goods sold and assessing tax accordingly. This is a draconian remedy reserved for serious non-cooperation cases.  _(§6038A(e); §6038A(e)(3); §7602; §7603; §7604; §7605)_

### 10.3 Practical compliance for foreign founder LLCs

For a small foreign-owned SMLLC, "records" means: - The LLC's bank statements showing all owner contributions and distributions. - Any loan agreements between owner and LLC. - Any service agreements or invoices between owner and LLC. - Documentation of the foreign owner's address and tax ID. - The agent authorization (typically a one-page statement signed at engagement, kept in the LLC's books). Practitioners should include a records checklist in the engagement letter and remind the client annually.

## 11. Common Scenarios

### Scenario A — UK founder with a Delaware LLC for Stripe and US banking

Aisha is a UK resident running a SaaS business. She forms a Delaware single-member LLC ("Frostbite LLC") to obtain a Stripe account, a Mercury bank account, and to receive USD payments from US customers. The LLC is disregarded for US income tax (no check-the-box election); Aisha reports the LLC's income on her UK Self Assessment and pays UK tax.

Form 5472 analysis:

- Frostbite LLC is a domestic eligible entity wholly owned by one foreign person → reporting corporation under Treas. Reg. §1.6038A-1(c)(1)(iii).
- Filing required: pro forma 1120 + Form 5472.
- Reportable transactions: capital contributions ($X), owner draws ($Y), any payments between Aisha personally and the LLC (e.g., reimbursements for software subscriptions Aisha paid on personal card and was reimbursed for).
- Even if Frostbite LLC has $0 in customer revenue, the capital contribution to fund the LLC at formation is a reportable transaction → filing required.
- Due date: April 15, 2026 (calendar year). Extension to October 15 via Form 7004.
- Filing channel: mail or fax to Ogden, UT (cannot e-file pro forma).
- AUDIT FLASH POINT: Aisha used Stripe Atlas for formation and was not told about the 5472 requirement. She has been operating for 3 years. Three years × $25,000 = $75,000 potential automatic penalty exposure. Practitioner files all three delinquent years with reasonable cause statements as soon as engaged.

### Scenario B — German parent with US R&D subsidiary

GreenMobil GmbH (Germany) owns 100% of GreenMobil USA Inc., a Delaware C corp that conducts R&D and licenses results back to the German parent. GreenMobil USA pays royalties to GreenMobil GmbH (no — wait, R&D fees flow the other direction). GreenMobil GmbH pays cost-plus R&D fees to GreenMobil USA under an intercompany services agreement.

Form 5472 analysis:

- GreenMobil USA Inc. is a domestic corp 100% foreign-owned → reporting corporation under §6038A.
- Files Form 1120 (real return, with income / expenses / tax) + Form 5472 attached.
- Reportable transactions on Part IV (amounts received): Line 8 (consideration received for services): R&D services fee from German parent. Line 11 (interest received): if any intercompany loans.
- Reportable transactions on Part V (amounts paid): Line 6 (royalties paid): if GreenMobil USA pays for use of German parent's IP.
- §482 transfer pricing: cost-plus method typical for R&D services; documentation under Treas. Reg. §1.6662-6 strongly recommended (this is a real operating company with material flows).
- BEAT (§59A): GreenMobil USA gross receipts likely well below $500M; BEAT does not apply.
- Due date: April 15, 2026 (or extended via Form 7004).

### Scenario C — Foreign passive investor at 30% in US C corp

A Brazilian individual, Renata, owns 30% of TechCo Inc., a Delaware C corp that builds software and is otherwise US-owned. Renata invested capital but is not active in the business. TechCo pays Renata quarterly dividends.

Form 5472 analysis:

- TechCo is 30% foreign-owned → reporting corporation under §6038A (one or more 25% foreign shareholders).
- Renata is a 25% foreign shareholder → foreign related party.
- Reportable transactions: Dividends paid to Renata (Part V or Part VII — dividends are a reportable transaction even though they are not "monetary transactions" in the ordinary sense; they appear in the "Distributions" line of Part V if cash, or in Part VI if non-cash).
- Note: dividends paid to a foreign shareholder are also subject to FDAP withholding under §1441 at 30% (or treaty rate, e.g., 15% under US-Brazil treaty if applicable). Form 1042 / 1042-S separately. Form 5472 is informational only; it does not discharge the withholding obligation.
- One Form 5472 is filed (one foreign related party). Other US shareholders are not reported on Form 5472.
- Due date: April 15, 2026.

## 12. Common Errors and Practitioner Pitfalls

### Error 1 — "My SMLLC is disregarded so I don't have to file anything"

- **Correction** — Wrong. Post-2017, a foreign-owned SMLLC must file Form 5472 + pro forma 1120 annually regardless of income or activity. See §4 above. AUDIT FLASH POINT.

### Error 2 — "I'll just file Form 5472 without a Form 1120"

- **Correction** — Wrong. Form 5472 is always an attachment to an underlying corporate return. For SMLLCs the underlying return is the pro forma 1120. Filing a naked Form 5472 will be rejected or treated as a non-filing.

### Error 3 — "Only transactions over $50,000 need to be reported"

- **Correction** — Wrong. There is no de minimis filing threshold: every reportable transaction must be reported. The instructions do allow transactions of $50,000 or less to be reported as "$50,000 or less" rather than an exact amount, and Treas. Reg. §1.6038A-1(h) and (i) relieve smaller filers of the record-maintenance and agent-authorization requirements only, never the filing itself. See §5.2 above.

### Error 4 — "I'll skip family members from the related-party analysis"

- **Correction** — Wrong. §318(a)(1) family attribution applies in full. Spouse, children, grandchildren, and parents of a 25% foreign shareholder may themselves be 25% foreign shareholders, and transactions with them are reportable.  _(§318(a)(1))_

### Error 5 — "The LLC was inactive so I don't need to file"

- **Correction** — Wrong. The capital contribution at formation is a reportable transaction. Any owner draw or reimbursement is reportable. "Inactive" almost never means "zero reportable transactions" for a foreign-owned SMLLC.

### Error 6 — "I'll e-file the pro forma 1120"

- **Correction** — Wrong. Pro forma 1120 cannot be e-filed (returns with $0 income are typically rejected by IRS e-file). File by mail or fax per the Form 5472 instructions.

### Error 7 — "The foreign owner doesn't have an SSN/ITIN, so the LLC can't get an EIN"

- **Correction** — Wrong. Form SS-4 can be submitted with a foreign tax ID (or "FOREIGN") on the responsible party line. The international applicant calls the IRS dedicated phone line (267-941-1099, not toll-free) or faxes/mails the SS-4. Online EIN issuance is blocked for entities whose responsible party lacks an SSN/ITIN, but phone/fax/mail channels remain open.

### Error 8 — "Late 5472? I'll just request first-time abatement"

- **Correction** — Wrong. FTA generally does not apply to §6038A penalties (international information return penalty exclusion in IRM 20.1.1.3.6.1). Reasonable cause must be argued on the merits.  _(IRM 20.1.1.3.6.1)_

### Error 9 — "I'll attach Form 5472 to my Form 1040"

- **Correction** — Wrong. Form 5472 is never attached to an individual income tax return. The foreign owner does not file 5472 in their personal capacity. The reporting corporation (or pro forma corporation) files it.

### Error 10 — "We minimized the reported amounts to avoid an audit"

- **Correction** — Wrong and a violation of §6038A(b) (which requires "true, accurate, and complete" returns). Report actual amounts and prepare defensible §482 documentation.  _(§6038A(b))_

## 13. Worked Examples

### Worked Example 1 — UK Founder Stripe-Only US LLC

Facts. Aisha (UK resident, UK national) formed Frostbite LLC (Delaware SMLLC) on March 1, 2025. She contributed £8,000 (USD equivalent $10,200 at formation). The LLC opened a Mercury bank account and a Stripe account. By December 31, 2025, the LLC had received $14,500 in Stripe payments from US customers. Aisha withdrew $9,000 during the year for personal use (owner draws). No other transactions with related parties.

Step 1 — Reporting corporation determination. Frostbite LLC is a domestic eligible entity wholly owned by one foreign person (Aisha, UK individual). Under Treas. Reg. §1.6038A-1(c)(1)(iii), it is a reporting corporation. Filing required.

Step 2 — Foreign related parties. Aisha personally is the only foreign related party.

Step 3 — Reportable transactions with Aisha.

**Reportable transactions table**

| Description | Amount | Form 5472 Line |
| --- | --- | --- |
| Capital contribution from Aisha to LLC | $10,200 | Part VII Line 25 (or capital contributions line per current form) |
| Distributions / owner draws from LLC to Aisha | $9,000 | Part VII (distributions line) |

The $14,500 in Stripe customer revenue is not a related-party transaction (customers are unrelated) and is not reported on 5472. However, it is reported on Aisha's UK Self Assessment as her personal trading income (LLC is disregarded for income tax).

Step 4 — Form preparation. Pro forma Form 1120: write "Foreign-owned U.S. DE" across the top; complete Item B (EIN), name and address; leave all income / deduction / tax lines blank; sign as "Member/Manager." Form 5472: Part I: identifying info for Frostbite LLC. Part II: identifying info for Aisha (name, address, country of citizenship UK, foreign tax ID = UK NI Number, relationship = direct 25%+ shareholder). Part III: skipped (not a foreign corp). Part IV: blank (no amounts received from Aisha in the listed categories — capital contributions go to Part VII not Part IV/V). Part V: blank. Part VI: blank (no non-monetary transactions other than the capital contribution). Part VII: capital contribution $10,200; distributions $9,000.

Step 5 — Filing. Mail or fax pro forma 1120 + 5472 to Ogden, UT M/S 6112 by April 15, 2026 (or October 15, 2026 with Form 7004 extension filed by April 15, 2026).

Step 6 — Recordkeeping. Retain LLC bank statements, formation documents, and a memo describing the related-party transactions for 7+ years. Have Aisha sign an authorization of agent statement under §6038A(e) at engagement.

### Worked Example 2 — German Parent with US R&D Sub

Facts. GreenMobil USA Inc. (Delaware C corp, calendar year, EIN 88-1234567) is 100% owned by GreenMobil GmbH (Germany). For tax year 2025: GreenMobil USA performs R&D for the German parent under a cost-plus 8% intercompany services agreement. Service fees paid by parent to GreenMobil USA in 2025: $4,200,000. GreenMobil USA paid royalties to parent for use of German parent's process patents: $620,000. No loans, no other transactions.

Step 1 — Reporting corporation. GreenMobil USA is a US corp 100% foreign-owned. Reporting corporation under §6038A. Filing required.

Step 2 — Foreign related party. GreenMobil GmbH is the only foreign related party.

Step 3 — Reportable transactions.

**Reportable transactions table**

| Description | Amount | Form 5472 Line |
| --- | --- | --- |
| Services fee received from parent | $4,200,000 | Part IV Line 8 |
| Royalties paid to parent | $620,000 | Part V Line 6 |

Step 4 — §482 transfer pricing. Cost-plus 8% on services: defensible if 8% mark-up is within the arm's-length range for comparable contract R&D providers. Practitioner recommends contemporaneous documentation under Treas. Reg. §1.6662-6 — typically commissioned annually from a transfer pricing specialist.

Step 5 — Form preparation. Real Form 1120 with full income, deduction, and tax computation. Attach Form 5472 with Part IV Line 8 = $4,200,000 and Part V Line 6 = $620,000. One Form 5472 only (one foreign related party).

Step 6 — Withholding. Royalty payments to a German parent are subject to §1441 FDAP withholding. Under Article 12 of the US-Germany income tax treaty (1989, as amended), the withholding rate on royalties is 0% (with exceptions for IP rented for use of motion picture films, where 15% applies). Form W-8BEN-E from the German parent on file; Form 1042 / 1042-S filed separately.

Step 7 — Filing. April 15, 2026 for calendar year 2025; extension to October 15 via Form 7004.

### Worked Example 3 — Brazilian Passive Investor at 30%

Facts. TechCo Inc. (Delaware C corp). Cap table: Domestic founders (US persons): 70%. Renata (Brazilian individual): 30%. In 2025, TechCo declared $200,000 in dividends. Renata received $60,000 (her 30% share). Renata has no other transactions with TechCo.

Step 1 — Reporting corporation. TechCo is 30% foreign-owned (Renata is a 25% foreign shareholder). Reporting corporation under §6038A. Filing required.

Step 2 — Foreign related parties. Renata personally. Domestic shareholders are not reported.

Step 3 — Reportable transactions.

**Reportable transactions table**

| Description | Amount | Form 5472 Line |
| --- | --- | --- |
| Dividends paid to Renata | $60,000 | Part V (distributions / dividends paid) |

Step 4 — Form preparation. Real Form 1120. Attach Form 5472 reporting $60,000 dividends paid to Renata.

Step 5 — FDAP withholding. Dividends to Brazilian residents: the US-Brazil treaty is not in force (signed but never ratified). Default §1441 rate of 30% applies. TechCo withholds $18,000 (30% of $60,000) and reports on Form 1042 / 1042-S. Renata receives net $42,000.

Step 6 — Filing. April 15, 2026 for calendar year 2025.

## 14. Self-Checks (Reviewer Checklist)

Before signing off on a Form 5472 deliverable, the reviewer confirms:

- [ ] Reporting corporation status correctly identified (§6038A vs §6038C vs SMLLC-by-regulation).
- [ ] EIN in place; if SMLLC, evidence of SS-4 submission and EIN assignment letter on file.
- [ ] All foreign related parties identified — direct, indirect (with §318 attribution as modified by §6038A), and family.
- [ ] Separate Form 5472 prepared for each foreign related party with reportable transactions.
- [ ] All reportable transactions enumerated; no de minimis exclusion applied.
- [ ] Capital contributions and distributions reported in Part VII for SMLLCs (commonly missed).
- [ ] Pro forma 1120 marked "Foreign-owned U.S. DE" at top, identifying info only, signed.
- [ ] Filing channel is mail or fax (not e-file for SMLLC pro forma); fax confirmation retained.
- [ ] Due date tracked; Form 7004 extension filed timely if needed.
- [ ] §482 documentation prepared or referred to specialist for material transactions.
- [ ] §6038A(e) agent authorization signed by foreign owner; retained in records.
- [ ] Prior years checked for filing history — if delinquent, reasonable cause statement prepared.
- [ ] Withholding (Form 1042 / 1042-S) considered separately if FDAP payments made to foreign related parties.

## 15. Provenance

**Provenance table**

| Source | Citation |
| --- | --- |
| Statutory base | IRC §6038A; IRC §6038C; IRC §6662; IRC §482; IRC §318; IRC §267(b); IRC §707(b)(1) |
| 2017 SMLLC expansion regulation | T.D. 9796, 81 Fed. Reg. 89849 (December 13, 2016); Treas. Reg. §1.6038A-1(c)(1)(iii); Treas. Reg. §301.7701-2(c)(2)(vi) |
| Penalty doubling | Tax Cuts and Jobs Act §13305 (Pub. L. 115-97); penalty increased from $10,000 to $25,000 for tax years beginning after 12/31/2017 |
| Reporting regulations | Treas. Reg. §1.6038A-1 (definitions); §1.6038A-2 (reportable transactions); §1.6038A-3 (records); §1.6038A-4 (penalties); §1.6038A-5 (agent authorization) |
| §6662 transfer pricing documentation | Treas. Reg. §1.6662-6 |
| Form and instructions | Form 5472 (Rev. December 2024 — confirm 2025 revision); Instructions for Form 5472 (annual revision) |
| IRM | IRM 20.1.9 (international information return penalties); IRM 20.1.1.3.6.1 (FTA exclusions) |
| Special filing address | Internal Revenue Service, 1973 Rulon White Blvd., M/S 6112 Attn: PIN Unit, Ogden, UT 84201 — confirm in current Form 5472 instructions each filing season |

### Verification status

This skill is marked verified_by: pending. It must be reviewed by a Circular 230 practitioner (Enrolled Agent, CPA, or attorney) with cross-border tax expertise before being relied upon for client engagements. The §1.6038A regulations and the Form 5472 instructions should be cross-checked at each filing season — the instructions are revised annually and may add or change reportable transaction categories, filing addresses, or fax numbers.

### Coordination with other skills

- Load alongside us-tax-workflow-base v0.2+ for workflow scaffolding.
- For C-corp Form 1120 mechanics, load us-form-1120-c-corp.
- For partnership filings (if foreign-owned partnership), see Form 8865 (separate skill — out of scope here).
- For BEAT / GILTI / FDII implications of cross-border flows, load us-gilti-fdii-beat.
- For Form 1042 withholding on FDAP payments to foreign related parties, refer out (separate skill).
- For check-the-box election analysis on foreign-owned LLC, refer out.

### Annual update flags

- Confirm Form 5472 revision date in use (currently December 2024; watch for 2025/2026 revisions).
- Confirm the Ogden filing address and fax number in current instructions.
- Watch for changes to the §6038A(d) penalty amount (currently $25,000; could change by statute).
- Watch for changes to the SMLLC pro forma 1120 filing channel (e-file may become available in future).
- Confirm treaty rates for FDAP withholding on dividends / royalties / interest paid to foreign related parties (separate Form 1042 workstream, but informs 5472 reporting amounts).

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
