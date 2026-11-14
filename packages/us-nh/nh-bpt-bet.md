---
name: nh-bpt-bet
description: >
  New Hampshire BPT and BET for 2026, including corporations, partnerships, proprietors and separate SMLLCs: rates, independent filing tests, reasonable compensation, depreciation, NOL, apportionment, BET credit, forms and payments.
jurisdiction: US-NH
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-11-13
version: "0.2"
type: computation
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - us-form-1120-c-corp
  - us-schedule-c-and-se-computation
---

# New Hampshire Business Profits Tax and Business Enterprise Tax, 2026

> **Source-cited draft.** Built from RSA 77-A, RSA 77-E, RSA 21-J and DRA business-tax publications read 2026-11-13. No accountant has reviewed this skill. General reference only; a qualified professional must review the facts, workpapers and filing. Circular 230 section 10.37: do not assume entity classification, compensation, nexus or credit eligibility.

**Answer first.** The 2026 BPT is **7.5%** of New Hampshire taxable business profits; BET is **0.55%** of adjusted, apportioned compensation, interest and dividends. Test the taxes separately. The published thresholds for periods beginning on or after January 1, 2025 continue into 2026: BPT gross business income **over USD 109,000**; BET gross receipts **over USD 298,000 or enterprise value tax base over USD 298,000**. The ordinary case pays BET and credits it against BPT, without a second charge for the same credited amount.

**Period distinction.** Statutory rules below cover tax year 2026. The line mappings expressly labelled **2025-2026 filing cycle** use the latest forms listed by DRA when read, the 2025 forms. They are not confirmation of unpublished 2026 line numbers. The announced 2027 BET threshold and future rate-trigger rules must not be applied early.

## Scope

Businesses with New Hampshire business activity: corporations, S corporations, partnerships, proprietorships, LLCs, fiduciaries, and relevant nonprofit business activity. State BPT can apply to a Schedule C business even though NH has no individual wage tax. A federal disregarded SMLLC is a **separate NH business organization**, not automatically combined with its owner's sole proprietorship. Grantor trusts have their statutory owner-return exception. [RSA 77-A:1 I, III](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm), [RSA 77-E:1 III](https://gc.nh.gov/rsa/html/V/77-E/77-E-1.htm), [BT-SUMMARY instructions, SMLLC section, 2025-2026 filing cycle](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bt-summary-instructions-2025.pdf).

This skill retains the ordinary entity and multistate rules; complex water's-edge groups and special elections require professional computation. Payroll withholding/UI is in `nh-payroll`; personal-tax repeal is in `nh-interest-dividends-note`. The federal computations and figures belong in `us-schedule-c-and-se-computation`, `us-form-1120-c-corp`, `us-form-1065-partnership`, `us-form-1120-s-s-corporation-return`, `us-qbi-deduction` and `us-s-corp-election-decision`. Do not import a federal rate or limit into NH without checking NH's static conformity.

Selective meals/rentals, real estate transfer, communications, tobacco, beer, electricity, utility-property and municipal property taxes are separate jobs. Their legacy numerical claims are identified under Sources rather than offered as current computations here.

## Ask the client first

1. What legal entities and owners exist, what is each federal classification, and what are the exact taxable periods?
2. What are **gross** everywhere business income/receipts, business-asset sale proceeds and the pre-apportionment enterprise value tax base for each entity?
3. Where are tangible goods delivered, services delivered, property and payroll located, and where is the business taxable? Is there a unitary group?
4. What actual services did each proprietor/partner perform, what compensation deduction is proposed, and is the business/group using the shared safe harbour or substantiation?
5. What NH/federal depreciation basis differences, interest adjustments, NOL schedules, prior BET credits and other awarded credits exist?
6. What tax has been paid, what prior-year liability/period is available for estimates, and is this the first filing period or a genuine closure?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 amount or condition | Official source |
|---|---|---|
| BPT rate | 7.5% for periods ending on or after December 31, 2023 | [RSA 77-A:2 III](https://gc.nh.gov/rsa/html/V/77-A/77-A-2.htm) |
| BET rate | 0.55% for periods ending on or after December 31, 2022 | [RSA 77-E:2 II](https://gc.nh.gov/rsa/html/V/77-E/77-E-2.htm) |
| BPT ordinary filing threshold | Gross business income from everywhere exceeds USD 109,000, periods beginning on/after January 1, 2025, including 2026 | [DRA Business Taxes](https://www.revenue.nh.gov/taxes-glance/business-taxes), [RSA 77-A:6 I indexation](https://gc.nh.gov/rsa/html/V/77-A/77-A-6.htm) |
| BET ordinary filing threshold | Gross receipts from everywhere **or** enterprise value tax base exceeds USD 298,000 for periods beginning on/after January 1, 2025, including 2026 | [DRA Business Taxes](https://www.revenue.nh.gov/taxes-glance/business-taxes), [RSA 77-E:5 I](https://gc.nh.gov/rsa/html/V/77-E/77-E-5.htm) |
| Compensation record-keeping safe harbour | Up to USD 75,000 total per business or related business group, not per partner; actual services still required; cannot reduce taxable profits below zero | [RSA 77-A:4 III](https://gc.nh.gov/rsa/html/V/77-A/77-A-4.htm) |
| NH section 179 expense cap | USD 500,000 for property placed in service on/after January 1, 2018, subject to the adopted IRC; separate NH basis records | [RSA 77-A:3-a](https://gc.nh.gov/rsa/html/V/77-A/77-A-3-a.htm) |
| Bonus depreciation | Apply the IRC without section 168(k); no federal bonus deduction in NH | [RSA 77-A:3-b I](https://gc.nh.gov/rsa/html/V/77-A/77-A-3-b.htm) |
| Ordinary IRC reference date | December 31, 2018 for periods beginning on/after January 1, 2020, subject to statutory exceptions | [RSA 77-A:1 XX(o)](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm) |
| NH NOL | Apportion in loss year, deduct after current-year apportionment; carry forward 10 years; generated loss carryforward capped at USD 10 million for periods ending on/after January 1, 2013 | [RSA 77-A:4 XIII](https://gc.nh.gov/rsa/html/V/77-A/77-A-4.htm) |
| Unused BET credit | 10 taxable periods for credit from periods ending on/after December 31, 2014; older credit had five periods | [RSA 77-A:5 X](https://gc.nh.gov/rsa/html/V/77-A/77-A-5.htm) |
| BPT estimated-tax declaration | Statute exempts annual estimate below USD 200; later-quarter estimate over USD 200 requires declaration | [RSA 77-A:6 II](https://gc.nh.gov/rsa/html/V/77-A/77-A-6.htm) |
| BET estimated-tax declaration | Statute exempts annual estimate below USD 260; later-quarter estimate over USD 260 requires declaration | [RSA 77-E:5 II](https://gc.nh.gov/rsa/html/V/77-E/77-E-5.htm) |
| Regular estimated instalments | 25% on 15th of months 4, 6, 9 and 12; calendar-year April 15, June 15, September 15, December 15 | [RSA 77-A:7 I](https://gc.nh.gov/rsa/html/V/77-A/77-A-7.htm), [RSA 77-E:6 I](https://gc.nh.gov/rsa/html/V/77-E/77-E-6.htm) |
| Return due date | Partnership: 15th of month 3 after period ends; exempt organization: month 5; other organizations: month 4 | [RSA 77-A:6 I](https://gc.nh.gov/rsa/html/V/77-A/77-A-6.htm), [RSA 77-E:5 I](https://gc.nh.gov/rsa/html/V/77-E/77-E-5.htm) |
| Filing extension, 2025-2026 filing cycle | Automatic 7 months if 100% of taxes due paid by original deadline; BT-EXT if payment needed; filing extension does not extend payment | [BT-SUMMARY instructions, extension section](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bt-summary-instructions-2025.pdf) |
| DRA late filing | Greater of 5% of net unpaid tax or USD 10 per month/part; total capped at greater of 25% or USD 50; extension/reasonable-cause exceptions | [RSA 21-J:31](https://gc.nh.gov/rsa/html/I/21-J/21-J-31.htm) |
| DRA late payment | 10% of nonpayment/underpayment; fraud 50%, with statutory interaction and reasonable-cause conditions | [RSA 21-J:33 I-II](https://gc.nh.gov/rsa/html/I/21-J/21-J-33.htm) |
| DRA interest for days in calendar 2026 | 9% annual; published daily decimal .000247; historical 2025 was 10% | [BT-SUMMARY instructions, line 4(a), 2025-2026 filing cycle](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bt-summary-instructions-2025.pdf) |

The historical DRA rate table records BPT 8.2% for periods ending in 2016-2017, 7.9% from December 31, 2018, 7.7% from December 31, 2019, and 7.6% from December 31, 2022 before the current rate. BET statutory history in RSA 77-E:2 records 0.6% from December 31, 2019 before the current rate. These are historical rates, not 2026 alternatives. [DRA BPT FAQ](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/business-profits-tax), [RSA 77-E:2](https://gc.nh.gov/rsa/html/V/77-E/77-E-2.htm).

### 1. Decide what must be filed

Test BPT and BET independently before apportioning. Gross business income and receipts are defined broadly, before cost of goods sold, expenses and losses: include rents, services, asset-sale proceeds, interest, royalties and other business income as defined in [RSA 77-A:1 VI](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm) and [RSA 77-E:1 X](https://gc.nh.gov/rsa/html/V/77-E/77-E-1.htm). A loss does not eliminate a threshold-based return. A sale or exchange of an ownership interest can require a BPT return regardless of the ordinary threshold ([RSA 77-A:6 I-a](https://gc.nh.gov/rsa/html/V/77-A/77-A-6.htm)).

Do not tick FINAL just because receipts fall below the threshold. The published BT-SUMMARY instructions say FINAL only when the organization no longer exists or no longer has NH business activity. Proprietorship installment sales can require returns until all instalments are reported where the original gross sale price exceeded the filing threshold; an election to recognize the whole gain uses DP-95. Separately owned spousal businesses do not combine just because the spouses file one federal Form 1040. [NH-1040 instructions, lines 1(a)-1(i), 2025-2026 filing cycle](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/nh-1040-instructions-2025.pdf).

### 2. Reconcile federal income to New Hampshire gross business profits

| Entity | Starting computation | Authority |
|---|---|---|
| Proprietor, profession, rental or farm activity | Business net profit/loss and gains/losses on business assets; not merely AGI | [RSA 77-A:1 III(d)](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm) |
| Partnership / partnership LLC | Federal ordinary income plus partner payments and separately allocated income/gains, less allocated deductions/losses as specified | [RSA 77-A:1 III(c)](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm) |
| C corporation | Taxable income before NOL and corporate special deductions, recomputed under NH's adopted IRC | [RSA 77-A:1 III(a), XX](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm) |
| S corporation | Entity-level net profit from all business activity; DRA requires DP-120, then NH-1120 | [RSA 77-A:1 I, III(b)](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm), [BT-SUMMARY instructions, 2025-2026 filing cycle](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bt-summary-instructions-2025.pdf) |
| Trust / estate with business activity | Net business profits and business-asset gains; grantor exception handled at owner level | [RSA 77-A:1 I, III(e)](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm) |
| Disregarded SMLLC | Separate NH entity return using the owner's federal classification; NH-1040, NH-1041, NH-1065 or NH-1120 as appropriate | [BT-SUMMARY instructions, SMLLC section, 2025-2026 filing cycle](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bt-summary-instructions-2025.pdf) |

Keep a reconciliation of every federal/NH difference. [RSA 77-A:3-b](https://gc.nh.gov/rsa/html/V/77-A/77-A-3-b.htm) disallows federal bonus depreciation and section 181 expensing and applies NH's section 179 rule. Add the federal excess and deduct the separately calculated NH depreciation; reverse basis differences on disposal. The difference is a timing/basis difference, not a permanent deduction loss. Do not repeat the old assertion that 2025 assets universally took a particular federal bonus percentage.

[RSA 77-A:4 II, VII, IX-XI, XIII-XV, XIX-XX](https://gc.nh.gov/rsa/html/V/77-A/77-A-4.htm) supplies further adjustments:

- Deduct qualifying direct US-obligation interest, net of related expenses; add back related expenses if not already netted. Do not deduct them twice.
- Add back deducted state net income taxes, net-income franchise taxes and capital-stock taxes. The published NH-1040 instructions say deducted BPT is added back; BET is not measured by income and is not added back on that line.
- Apply the wage-credit adjustment, foreign dividend gross-up deduction, qualified charitable/research property adjustments, business-interest adjustments and QIC-holder rules when relevant; preserve the supporting schedules. Ordinary out-of-state municipal income follows the NH-adopted federal computation and applicable adjustments, not an unsupported blanket addition rule.
- For section 163(j), deduct current-year disallowed interest, add federally used carryforwards already deducted in NH, and deduct the pre-2024 disallowed balance in three equal parts across the specified consecutive years beginning in 2024. Never duplicate the deduction.
- An ownership-interest transaction with a federal asset-basis step-up has a default NH basis adjustment and an irrevocable timely-return election under paragraph XIV. Refer the election before preparing the return.

The detailed line descriptions in the [NH-1040 instructions, 2025-2026 filing cycle, lines 2 and 6](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/nh-1040-instructions-2025.pdf) explain Schedule IV attachments, asset-basis reconciliation, US interest, taxes and interest adjustments. They do not establish 2026 line numbering.

### 3. Reasonable compensation: shared safe harbour or supported actual amount

[Read RSA 77-A:4 III(a)-(g)](https://gc.nh.gov/rsa/html/V/77-A/77-A-4.htm) as a whole. A proprietor/partner/member must have actually provided personal services. The business or related business group may elect a total USD 75,000 record-keeping safe harbour. It is **not USD 75,000 for every owner** and is not indexed. The group allocation is reduced by specified owners' compensation deducted by corporate group members.

Alternatively, claim the fair and reasonable value of actual services using the adopted section 162 standard. Keep duties, hours, qualifications, comparable-pay support and the relationship between claimed compensation and reported earned income. The deduction cannot reduce taxable business profits below zero; net rental income and business-asset selling commissions have their statutory conditions. Corporate shareholder wages are already in the corporation's expense calculation; a C/S shareholder does not get a second proprietor compensation deduction.

**Decision in both directions.** If supported services are worth less than the safe-harbour ceiling and there is sufficient profit, the shared safe harbour can reduce record-keeping. If a supported actual amount exceeds it, substantiation may save BPT; compare both bases, the BET floor and compliance cost. Do not fabricate a market salary as legal evidence. If profit is only USD 30,000, a proposed USD 75,000 deduction is limited to USD 30,000; the excess does not itself create an NOL. The NH-1040 instructions separately discuss a later-year adjustment for intended prior-year under-compensation where adequate records exist; this is not an automatic carryforward deduction.

### 4. Apportion and then use NH NOL

[Print the sourcing conditions from RSA 77-A:3](https://gc.nh.gov/rsa/html/V/77-A/77-A-3.htm) with the computation. For periods ending on/after December 31, 2022, ordinary business profits use the single sales factor. A business must meet the multistate taxability test before apportioning.

- Tangible goods: destination receipts, plus the stated origin shipments to the US government or a state where the business is not taxable. The old statement that NH has no throwback rule was incorrect.
- Services: where delivered; real property: where located; rented tangible property: where located; intangibles: where used. Approximate if the location cannot be determined.
- Other-than-tangible sales assigned to a state where the business is not taxable, or not determinable/approximable, are excluded from the denominator. The old blanket claim of a nowhere-sales benefit was incorrect.
- Foreign dividends have their separate statutory formula. Related unitary businesses use combined factors under paragraph III; do not turn a simple two-customer example into proof of group treatment.

The old developer example survives **only with taxability established**: USD 120,000 of services delivered in California and USD 40,000 delivered in NH, with the business taxable in both, give a 25% NH factor. Adjusted profit after compensation of USD 80,000 produces USD 20,000 NH profits and USD 1,500 BPT before credits. Without the taxability premise, that denominator cannot be assumed.

Apply the NH NOL **after** current apportionment, using an NOL apportioned once in its loss year. [RSA 77-A:4 XIII](https://gc.nh.gov/rsa/html/V/77-A/77-A-4.htm) provides ten forward years and the generated-loss cap. The DRA FAQ says periods ending on/after December 31, 2022 follow section 172 as adopted by NH; do not use the old blanket assertion that the federal percentage limitation never applies. Use DP-131-A and DP-132, attach the deduction worksheet and prove the loss year. No NH refund-producing NOL carryback is supported; pre-July 2005 historical notional carryback calculations are a separate issue in the [DRA BPT FAQ](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/business-profits-tax).

### 5. Compute BET from its own definitions

[Read RSA 77-E:1 V, VI, IX-XI](https://gc.nh.gov/rsa/html/V/77-E/77-E-1.htm) and [77-E:3](https://gc.nh.gov/rsa/html/V/77-E/77-E-mrg.htm) with the [BET instructions, 2025-2026 filing cycle](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bet-instructions-2025.pdf):

1. **Compensation:** qualifying employee/officer/director payments and specified benefits/deferred compensation, plus the BPT proprietor/partner deduction and remaining statutory self-employment earnings without duplicating them. The state statute does not supply the old skill's Social Security wage-base cap. Do not cap all BET compensation at a federal payroll base. Guaranteed payments, losses and distributive amounts must follow the instructions; do not mechanically add the same partner income twice.
2. **Interest:** amounts paid or accrued for the use or forbearance of money or property, with the statute's exclusions. Do not restrict the statutory definition to a hand-picked list of federally deducted bank costs.
3. **Dividends:** NH's own definition covers distributions from accumulated revenues/profits to owners, with specified exclusions. It is not limited to federal C-corporation dividends. The old categorical exemption of partnership and S-corporation distributions is incorrect; distinguish distributed capital and the statutory exceptions.
4. Sum the components, apply retained-in-business self-employment and qualifying inter-enterprise dividend adjustments without reusing the BPT compensation deduction. A compensation deduction under BPT does not simply disappear from BET.
5. If multistate, [RSA 77-E:4](https://gc.nh.gov/rsa/html/V/77-E/77-E-4.htm) apportions compensation by the statutory work/payroll rule, interest by **owned real and tangible property**, and dividends by the equally weighted compensation, property and sales factors. This is not interest-expense location or dividends solely at commercial domicile.
6. Apply 0.55% and eligible BET credits. The simple pre-apportionment example remains: USD 180,000 employee wages plus USD 40,000 correctly determined owner compensation plus USD 8,000 interest gives USD 228,000 EVTB and USD 1,254 BET **only if a separate filing trigger is met**, for example gross receipts above the threshold. Otherwise the below-threshold base alone does not require a return.

BET is legally entity-based; [RSA 77-E:1 III](https://gc.nh.gov/rsa/html/V/77-E/77-E-1.htm) prohibits consolidated/combined reporting as defined there. DRA offers group presentation schedules; those do not authorize disregarding entity computations. Reconcile every member, its factors and the cross-member BPT credit under [RSA 77-E:13](https://gc.nh.gov/rsa/html/V/77-E/77-E-13.htm), rather than summing group wages and eliminating items without authority.

### 6. Credit BET against BPT exactly once

[Rules: RSA 77-A:5 X](https://gc.nh.gov/rsa/html/V/77-A/77-A-5.htm), [77-E:13](https://gc.nh.gov/rsa/html/V/77-E/77-E-13.htm). Track credit by origin period, use and expiry. For periods ending on/after December 31, 2014, unused BET credit carries ten periods. The old five-period instruction is not current. Use the Business Enterprise Tax Credit Worksheet (BET-CW); other credits require their statutory schedules. Do not assume an ordering/FIFO rule not established by the worksheet.

For a stand-alone taxpayer with no other credits or carryovers: current BET credit is the smaller of BET and BPT. BPT net = BPT minus credit, at least zero; total state business tax = BET plus BPT net. That equals the larger gross tax in this simple case. With other credits or carried BET, recompute rather than automatically applying a maximum formula.

### 7. Follow the filing forms and payment sequence

**Published mapping: 2025-2026 filing cycle only.** The [current forms list](https://www.revenue.nh.gov/resource-center/current-year-forms-and-instructions) and [BT-SUMMARY instructions](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bt-summary-instructions-2025.pdf) were read together.

| Taxpayer / item | Form and flow |
|---|---|
| Proprietor, individual-owned disregarded SMLLC | Separate NH-1040 Business Profits Tax return; SMLLC uses its own FEIN or DRA DIN, not an assumed owner combined return |
| Partnership / partnership LLC | NH-1065 with relevant federal and state reconciliation schedules |
| C or S corporation | NH-1120; S corporation also DP-120; retain applicable information reports listed by DRA |
| Fiduciary | NH-1041 |
| Water's-edge unitary BPT group | NH-1120-WE with affiliation/member schedules; separate entity analysis remains necessary |
| BET | Form BET; apportioned filers use BET-80 or relevant group schedule; current return instructions determine the correct attachment |
| BPT apportionment and NOL | DP-80; DP-131-A for loss history and DP-132 for allowable deduction; Schedule IV for required detailed adjustments |
| BET credit / other credits | BET-CW; DP-160 for other statutory credits |
| Every required BPT and/or BET filer | **BT-SUMMARY**; omitting it makes the filing incomplete |

In [NH-1040, 2025-2026 filing cycle](https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/nh-1040-instructions-2025.pdf): line 1 collects business activities; line 2 reconciles the IRC; line 6 adjustments include compensation/taxes/interest; line 8 is apportionment; line 9 profit before NOL; line 10 allowable NOL; line 11 taxable business profits; line 12 gross BPT; line 13 credit; line 14 BPT net goes to **BT-SUMMARY 1(b)**. For the simple un-apportioned BET form, lines 1-3 components total on line 4, line 5 tax, line 6 credits, line 7 net goes to **BT-SUMMARY 1(a)**. Do not use the simple BET form flow as the complete multistate apportionment method.

Open **Granite Tax Connect** from DRA's [Business Taxes page](https://www.revenue.nh.gov/taxes-glance/business-taxes). Select the correct entity, tax and period, complete the BPT/BET computation and required attachments, then BT-SUMMARY. In the published summary, Step 2 identifies entity, LLC status, amended/final and filing tests; Step 3 completes the tax returns; Step 4 lines 1(a)-(c) sum net BET/BPT; 2(a)-(e) reconcile extension, estimates, prior overpayment and amendment payments; line 3 balance; line 4 interest/penalties; line 5 payment; lines 6-7 overpayment, carryforward/refund; Step 5 signature/authorization. Retain filing confirmation and payment reference, and match the payment to the correct FEIN/DIN and taxable period. Paper returns go to the address on the current instructions; do not email or fax a return.

### 8. Estimates, extensions and enforcement

Test each tax against **its own** declaration amount; USD 260 is BET, not a combined BPT-plus-BET threshold. The statute says estimates below each amount are exempt and addresses amounts exceeding it later; for exact-boundary liabilities use the current return/agency instructions rather than inventing a combined rule. Calendar instalments fall in April, June, September and December, unlike federal personal estimates; federal figures belong in `us-quarterly-estimated-tax`.

[RSA 21-J:32](https://gc.nh.gov/rsa/html/I/21-J/21-J-32.htm) computes underpayment by instalment using the 90% current-tax standard and exceptions including a qualifying prior 12-month return **showing a liability**, recomputation at current rates, annualization, and first filing period. The old USD 40,000/110% rule is not in that statute. A zero-liability prior return is not the specified liability-showing prior-year exception. Use DP-2210/2220 for both taxes; different quarters can use different available exceptions. First-period relief from estimated-tax penalty is not exemption from filing or paying the business tax.

Pay the full annual balance by the original due date; a valid filing extension does not defer payment. Use BT-EXT if needed to complete payment for the published automatic extension. The late-filing and late-payment rules in the rates table are separate from interest. Use the rate for each calendar period of delinquency; 9% is confirmed for calendar 2026, **not automatically for payments in 2027**.

### 9. Federal coordination boundary

NH's compensation deduction changes NH BPT; it does not create a federal W-2 or itself reduce federal Schedule C profit. The federal treatment of tax payments depends on the tax, entity, accounting method and deduction category. The old advice to put every proprietor BPT/BET payment on Schedule C, its blanket SALT-cap statement, and its statement that NH tax payments cannot affect federal QBI/SE/retirement calculations are not verified by NH law and must not be used. Route to the federal owner skills. Do not double-count a credited BET payment as though gross BPT and BET were both payable. The entity-level BPT means an S election does not simply remove NH business tax; any entity-choice analysis must include state compliance and compensation treatment as well as the federal decision.

## Boundary and exception table

| Situation | Rule or boundary |
|---|---|
| No profit but gross filing test met | File; BET can be payable despite a BPT loss |
| Federal disregarded LLC | Separate NH entity, with owner-classification form and its own identifier |
| Partners each claim the full safe harbour | Incorrect; share business/related-group ceiling or substantiate actual services |
| Personal interest/dividend receipts | Repeal skill handles personal tax; business income/distributions still need entity analysis |
| Unitary businesses | BPT combined reporting when statutory conditions hold, even if only one group member has NH activity; detailed membership and credit allocations require review |
| Overseas corporation / 80-20 entity | Read RSA 77-A:1 XV-XIX: foreign-incorporation and foreign payroll/property tests plus 80/20 certification conditions; do not replace them with a generic foreign-revenue test |
| P.L. 86-272 claim | Use `us-pl-86-272-income-tax-nexus`; analyze BPT and BET separately rather than assuming both exempt |
| Qualified investment or regenerative manufacturing election | Specific statutory exception, not ordinary business-tax exemption |

The group and entity boundaries above come from [RSA 77-A:1](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm), [77-A:3 III](https://gc.nh.gov/rsa/html/V/77-A/77-A-3.htm), [77-A:6 IV](https://gc.nh.gov/rsa/html/V/77-A/77-A-6.htm), and [77-E:1 III](https://gc.nh.gov/rsa/html/V/77-E/77-E-1.htm).

## Worked cases

All taxpayers and compensation facts are invented. Calculation examples keep cents to expose the arithmetic; published return instructions require whole-dollar entries, so round each actual return line as directed and reconcile the final payment.

**Case 1, Aisha, proprietor decision.** Gross receipts USD 300,000; expenses USD 80,000; net business profit USD 220,000. Services are delivered USD 90,000 in NH and USD 210,000 outside, with taxability established in those markets; NH factor 30%. Aisha performed actual services. Compare the shared safe-harbour deduction USD 75,000 with a fully substantiated USD 115,000 actual-services deduction. For the BET illustration, the separately reconciled statutory owner-compensation input is USD 203,170, with no interest/dividends/retained adjustment, and work entirely in NH. This is a supplied input, not a federal wage-base computation.

Safe harbour: BPT (220,000 - 75,000) x 30% x 7.5% = USD 3,262.50. Supported actual amount: (220,000 - 115,000) x 30% x 7.5% = USD 2,362.50. BET = 203,170 x 0.55% = USD 1,117.435 before return rounding. Both taxes must be filed because gross receipts exceed both thresholds. Credited BET leaves the total equal to BPT in each case: the supported deduction saves USD 900. If evidence supported only USD 60,000, BPT under that actual amount would be USD 3,600, compared with USD 3,262.50 under the eligible safe harbour. That is the opposite decision direction. The old USD 3,332 purported federal deduction is not a valid sum of state liabilities.

```oa-check
name: Aisha compensation decision both directions, NH 2026
inputs:
  profit: 220000
  factor: 0.30
  owner_compensation_input: 203170
steps:
  - safe_bpt: (profit - 75000) * factor * 0.075
  - supported_bpt: (profit - 115000) * factor * 0.075
  - low_actual_bpt: (profit - 60000) * factor * 0.075
  - bet: owner_compensation_input * 0.0055
  - safe_net_bpt: max(safe_bpt - bet, 0)
  - supported_net_bpt: max(supported_bpt - bet, 0)
  - safe_total: bet + safe_net_bpt
  - supported_total: bet + supported_net_bpt
  - savings: safe_total - supported_total
expected:
  safe_bpt: 3262.50
  supported_bpt: 2362.50
  low_actual_bpt: 3600
  bet: 1117.435
  safe_total: 3262.50
  supported_total: 2362.50
  savings: 900
```

**Case 2, Granite Marketing LLC, two partners.** Partnership ordinary income USD 55,000 is after USD 180,000 guaranteed payments. Add the payments for NH starting profit USD 235,000. A shared USD 75,000 record-keeping safe harbour leaves USD 160,000 at 100% NH apportionment, BPT USD 12,000. Assume correctly reconciled BET compensation USD 800,000 (USD 620,000 employee wages plus USD 180,000 owner compensation), interest USD 25,000 and no taxable distributions: BET USD 4,537.50. Net BPT is USD 7,462.50; total USD 12,000. If USD 150,000 actual owner services are substantiated, BPT becomes USD 6,375 and total USD 6,375, but that deduction is **not** two safe harbours.

```oa-check
name: Granite partnership shared compensation ceiling, NH 2026
inputs:
  ordinary_income: 55000
  guaranteed_payments: 180000
  employee_wages: 620000
  owner_compensation_input: 180000
  interest: 25000
steps:
  - nh_start: ordinary_income + guaranteed_payments
  - safe_profit: nh_start - 75000
  - bpt: safe_profit * 0.075
  - bet_base: employee_wages + owner_compensation_input + interest
  - bet: bet_base * 0.0055
  - bpt_net: max(bpt - bet, 0)
  - total: bet + bpt_net
  - supported_actual_bpt: (nh_start - 150000) * 0.075
expected:
  nh_start: 235000
  safe_profit: 160000
  bpt: 12000
  bet_base: 825000
  bet: 4537.50
  bpt_net: 7462.50
  total: 12000
  supported_actual_bpt: 6375
```

**Case 3, Lakeside Software Inc.** Receipts USD 850,000 establish both filing triggers; federal corporate taxable income before NOL/special deductions, already reconciled to NH, is USD 400,000. A valid 75% NH sales factor produces BPT USD 22,500. Statutory compensation USD 260,000, entirely NH, with zero interest/dividends yields BET USD 1,430. Net BPT USD 21,070; total USD 22,500. No separate proprietor compensation deduction applies to the shareholder-employees' already deducted wages.

```oa-check
name: Lakeside corporate BPT and BET, NH 2026
inputs:
  profits: 400000
  sales_factor: 0.75
  compensation: 260000
steps:
  - bpt: profits * sales_factor * 0.075
  - bet: compensation * 0.0055
  - net_bpt: max(bpt - bet, 0)
  - total: bet + net_bpt
expected:
  bpt: 22500
  bet: 1430
  net_bpt: 21070
  total: 22500
```

**Case 4, Granite loss-year boundary, corrected assumptions.** Receipts USD 1.2 million; federal partnership loss USD 250,000 after USD 150,000 partner payments; NH profit before compensation is negative USD 100,000, so no compensation deduction creates a larger loss. The correctly reconciled BET compensation **including applicable partner net earnings/losses** is assumed to be USD 630,000, interest USD 20,000, no distributions/retained adjustment, all NH. BET USD 3,575 remains payable; BPT is zero. The unused current BET credit potentially carries for ten taxable periods. Do not copy the old USD 750,000 BET base without reconciling partner losses. The negative NH profit is not automatically a certified NOL amount; determine it under NH-adopted section 172 and loss-year apportionment.

```oa-check
name: Granite loss year still owes BET, NH 2026
inputs:
  federal_loss: -250000
  partner_payment_addback: 150000
  reconciled_compensation: 630000
  interest: 20000
steps:
  - profit_before_compensation: federal_loss + partner_payment_addback
  - bpt: max(profit_before_compensation, 0) * 0.075
  - bet: (reconciled_compensation + interest) * 0.0055
  - unused_bet_credit: max(bet - bpt, 0)
  - total: bet + max(bpt - bet, 0)
expected:
  profit_before_compensation: -100000
  bpt: 0
  bet: 3575
  unused_bet_credit: 3575
  total: 3575
```

## When to refuse or refer

Refer disputed nexus, denominator exclusions, unitary/water's-edge membership, foreign dividends, section 179 phaseout, NOL percentage limits, special-credit ordering and ownership-basis elections for a professional calculation using the full record. Do not certify a tax amount from this skill when those core inputs remain missing. Federal tax deductibility is a federal-owner job, not a state-law inference.

## Filing and payment

Calendar 2026 partnership returns are statutorily due March 15, 2027; ordinary corporations, proprietors, fiduciaries and combined returns April 15, 2027; exempt-organization return classes use the statutory fifth-month rule. Confirm the relevant 2026 published return instructions before filing. Pay estimates during the taxable year on the separate BPT/BET schedules. Preserve the original payment deadline when using an extension, and confirm the interest rate for any 2027 delinquency.

## Completion checklist

- Every legal entity, including federal disregarded LLC, tested separately where NH requires.
- Gross everywhere filing tests recorded before apportionment; asset/ownership sale rules checked.
- Federal-to-NH IRC/basis reconciliation attached; compensation ceiling or supporting records established.
- BPT and BET definitions/factors kept separate; NOL applied at correct stage.
- BET credit used once, origin/expiry tracked, other credits supported.
- Required BPT/BET, BT-SUMMARY, schedules and federal attachments complete.
- Estimates, extension payments and final balance reconciled to receipts.

## Sources

| Source | URL | Read on |
|---|---|---|
| RSA 77-A:1. Read for I, III, IV, VI, XII-XX: separate entities, starting income, gross threshold base, nexus, unitary/water's-edge definitions and IRC date. | https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm | 2026-11-13 |
| RSA 77-A:2. Read for III: current BPT rate. | https://gc.nh.gov/rsa/html/V/77-A/77-A-2.htm | 2026-11-13 |
| RSA 77-A:3. Read for the full section: single sales factor, tangible throwback, service location, denominator exclusions, foreign dividends and combined factors. | https://gc.nh.gov/rsa/html/V/77-A/77-A-3.htm | 2026-11-13 |
| RSA 77-A:3-a and 3-b. Read for NH section 179 cap and exclusions of bonus/section 181. | https://gc.nh.gov/rsa/html/V/77-A/77-A-3-a.htm ; https://gc.nh.gov/rsa/html/V/77-A/77-A-3-b.htm | 2026-11-13 |
| RSA 77-A:4. Read for II-III, VII, IX-XV and XIX-XX: compensation including shared safe harbour, base adjustments, NOL, basis elections and interest. | https://gc.nh.gov/rsa/html/V/77-A/77-A-4.htm | 2026-11-13 |
| RSA 77-A:5. Read for X: ten-period BET credit and neighboring credits to avoid treating it as an unconditional maximum formula. | https://gc.nh.gov/rsa/html/V/77-A/77-A-5.htm | 2026-11-13 |
| RSA 77-A:6 and 7. Read for filing/ownership sale requirements, separate estimates, return dates and instalments. | https://gc.nh.gov/rsa/html/V/77-A/77-A-6.htm ; https://gc.nh.gov/rsa/html/V/77-A/77-A-7.htm | 2026-11-13 |
| RSA 77-E:1 and 2. Read for entity-level BET, compensation/distribution/interest definitions and current rate. | https://gc.nh.gov/rsa/html/V/77-E/77-E-1.htm ; https://gc.nh.gov/rsa/html/V/77-E/77-E-2.htm | 2026-11-13 |
| RSA 77-E chapter. Read for sections 3-6 and future-effective provisions: retained-compensation adjustments, thresholds, instalments and 2027 boundary. | https://gc.nh.gov/rsa/html/V/77-E/77-E-mrg.htm | 2026-11-13 |
| RSA 77-E:4 and 13. Read for component-specific BET apportionment and member-level BPT credit allocations. | https://gc.nh.gov/rsa/html/V/77-E/77-E-4.htm ; https://gc.nh.gov/rsa/html/V/77-E/77-E-13.htm | 2026-11-13 |
| RSA 21-J:31, 32 and 33. Read for filing/payment penalties and every estimated-tax exception, including first-period relief and prior liability condition. | https://gc.nh.gov/rsa/html/I/21-J/21-J-31.htm ; https://gc.nh.gov/rsa/html/I/21-J/21-J-32.htm ; https://gc.nh.gov/rsa/html/I/21-J/21-J-33.htm | 2026-11-13 |
| DRA Business Taxes. Read for USD 109,000 / USD 298,000 thresholds from 2025 onward and current tax/form portal links. | https://www.revenue.nh.gov/taxes-glance/business-taxes | 2026-11-13 |
| DRA BPT FAQ. Read for historical rate/threshold tables, filing dates, estimates, S corporations, installment sales and NOL rules. | https://www.revenue.nh.gov/resource-center/frequently-asked-questions/business-profits-tax | 2026-11-13 |
| Current forms catalogue. Read for the Business Taxes entries; the listed forms were 2025, not confirmation of 2026 line numbers. | https://www.revenue.nh.gov/resource-center/current-year-forms-and-instructions | 2026-11-13 |
| BT-SUMMARY instructions, 2025-2026 filing cycle. Read for the full instructions: separate SMLLCs, both filing tests, separate estimate amounts, seven-month filing extension, all summary steps and calendar 2026 interest. Its Step 2 prose prints 0.055% for BET; RSA 77-E:2 and BET line 5 establish 0.55%, which controls here. | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bt-summary-instructions-2025.pdf | 2026-11-13 |
| BET instructions, 2025-2026 filing cycle. Read for the full instructions: component definitions, partner compensation, lines 1-7 and summary flow. | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/bet-instructions-2025.pdf | 2026-11-13 |
| NH-1040 instructions, 2025-2026 filing cycle. Read for lines 1-14 and general instructions: spousal/SMLLC separation, IRC differences, depreciation, compensation, taxes, interest, NOL and credit flow. | https://www.revenue.nh.gov/sites/g/files/ehbemt736/files/documents/nh-1040-instructions-2025.pdf | 2026-11-13 |

DRA HTML and PDF sources were retrieved with basic Firecrawl after direct and ordinary browser reads were blocked; no stealth, CAPTCHA or TLS bypass was used.

Not yet confirmed: final 2026 form lines and portal field labels; full NH-adopted section 172 percentage-limit computation for a particular NOL; detailed section 179 phaseout; current BET-CW credit ordering/FIFO and all statutory group schedules; the old claim that a greater-than-50% IRC 1563 ownership test and a generic Finnigan label determine every group; historical BPT/BET rates before the periods shown by the read sources (including old 8.5%, 0.75% and 0.675% assertions); the old suggestion to automatically close below-threshold accounts; the legacy session-law/enactment-date claims (including 1970 BPT, 1993 BET and the old NOL amendment history); the old categorical claim that no separate PTET election exists or is ever needed; the old federal Schedule C/BPT/BET deduction, SALT-cap, QBI, SE and retirement claims, which must be resolved in their federal owners; legacy out-of-scope RETT 1.5%, meals/rentals 8.5% and communications 7% computations, and estate/inheritance assertions. These items are not usable tax instructions in this skill. No accountant has approved it.
