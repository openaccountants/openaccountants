---
name: corporate-income-tax-workflow-base
description: "Shared 2026 corporate income tax preparation method covering accounts-to-tax reconciliation, country-specific rate and relief handoff, credits counted once, payment reconciliation, current and deferred tax, intake, outputs and specialist refusals. Includes bounded UK and Singapore applications. Load the actual current country method and enacted regime before computing liability or filing."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
type: cross-country-method
last_updated: 2026-11-14
category: foundation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Corporate Income Tax Workflow Base

## Corporate Income Tax Workflow Base v0.2

## Scope

This is the **shared workflow base** for any corporate income tax content skill. It does not set a worldwide tax rate. The bounded country applications below illustrate the handoff rather than replacing the country method. It contains:

- The standard runbook for preparing a corporate income tax computation, return, and reviewer brief
- The structured intake form for gathering inputs from a corporate client
- The output specification for a reviewer-ready working paper
- The global refusal catalogue : situations a content skill must escalate to a credentialed practitioner without computing
- The 18 self-checks
- The citation discipline
- The Pillar Two interaction protocol
- The slot contract that every country-level content skill must fill

**Every corporate income tax skill must be read with the shared workflow and the actual current country rules.** This 2026 method does not set a country tax rate or certify an annual return edition. Internal [T1]/[T2]/[T3] workpaper flags and the historical phrase Shared workflow base are not professional approval labels.

**Answer first:** obtain the company/period/residence, actual accounts and currency, activity/regime, group and cross-border position, prior losses/credits and proved payments. The complete intake remains below. Deliver a tax reconciliation, payment bridge and review pack, not an unsupported final filing.

## Section 1 : Audience and assumptions

This base assumes:

- The **taxpayer** is a **corporation** (incorporated entity) : not a partnership, trust, sole proprietorship, or individual
- Establish the accounts' functional/presentation currency, each tax-computation currency and the return/payment currency separately from current local rules. They need not all be identical; the Singapore example below distinguishes them
- The corporation maintains accounting records under either local GAAP or IFRS (see `ifrs-local-gaap-reconciliation.md` for reconciliation)
- A **credentialed reviewer** (CPA / CA / CTA / Steuerberater / equivalent) reviews and signs off on every output before it is filed
- The corporation is in scope for the country's general corporate income tax : NOT a special regime (banking, insurance, REIT, fund, oil and gas, mining, shipping, aviation, charity : these require sector skills)

## The method, step by step

### Step 0 : Onboarding (always first)

0. **Onboarding intake** : Run the intake form (Section 4). Confirm: - Country of incorporation - Country of tax residence under actual domestic and treaty rules, including incorporation/management tests where relevant - Filing year-end date - Corporate size and threshold tests (small / medium / large / MNE) - Accounting framework (local GAAP / IFRS / Ind AS / etc.) - Any consolidated / group tax filing status (Organschaft, intégration fiscale, group relief, etc.) - Any in-scope regime overlays (Pillar Two, CFC, BEAT, GILTI) If any of: cross-border activities; multiple shareholders with different tax residences; loss-making with restructuring; ongoing audit; M&A in the year → flag to reviewer before computation.

### Step 1 : Reconcile accounting profit to tax profit

0. **Reconciliation walk-through** : Start from the audited / approved profit-before-tax (PBT) per the corporation's accounting framework. Walk through the adjustment categories table.

**Adjustment categories**

| Adjustment category | Direction | Example |
| --- | --- | --- |
| Non-deductible expenses | Add back | Fines, penalties, certain entertainment |
| Tax-exempt income | Subtract | Inter-corporate dividends within participation exemption; certain investment income |
| Timing differences | ± | Depreciation (book vs tax), provisions, IFRS leases |
| Disallowed depreciation / interest | ± | Interest deduction limitations |
| Loss utilization | ± | Brought-forward losses; group relief |
| GAAR / anti-abuse override | If applicable | Refer to reviewer |

### Step 2 : Apply jurisdiction-specific rate

0. **Apply rate** : Apply the headline corporate income tax rate from the content skill. Where multiple rates apply (small-company rate, lower rate on first slice, surcharges), apply per the content skill's bracket schedule.

### Step 3 : Apply credits and offsets

0. **Credits and offsets** : - R&D credits (see `rd-tax-credits-matrix.md`) - Patent / IP box benefit (see `ip-patent-box-matrix.md`) - Foreign tax credits - Group relief utilisation - Withholding tax credits on receipts - Anti-double taxation relief

### Step 4 : Compute and reconcile

0. **Compute and reconcile:** compute gross current tax under the country's rate/base rules, then apply each eligible credit/offset once to reach net current tax liability. Deduct proven advance payments and other payment credits once to reach the settlement balance. A foreign tax credit already deducted at Step 3 must not be deducted again here. Reconcile the current-tax provision and settlement separately; deferred tax belongs in the accounting provision, not in the tax payment balance. Record any legal limitation, carryforward, refund route and material variance.

### Step 5 : Pillar Two overlay (if applicable)

0. **Pillar Two overlay:** load `pillar-two-globe-minimum-tax.md` and the actual enacted country implementation. Establish the tested period, group/consolidation history, excluded entities and other scope conditions before computing. A single current-year revenue number is insufficient. Keep Adjusted Covered Taxes, GloBE Income, jurisdictional ETR, SBIE, safe harbours/de minimis and IIR/UTPR/QDMTT separate; do not calculate a top-up as the difference between a headline domestic rate and a global minimum. The Singapore scope example below gives one sourced implementation, not universal adoption.

### Step 6 : Cross-border overlays

0. **Cross-border overlays** : If the corporation has cross-border activity: - **Permanent establishment risk** : see `permanent-establishment-risk.md` - **Withholding tax on outbound payments** : see `withholding-tax-matrix.md` - **CFC inclusion** : apply local CFC rules - **BEPS Action 5 IP regime nexus** : see `ip-patent-box-matrix.md` - **DAC6 / MDR reporting** : see `dac6-mdr-reportable-arrangements.md` - **CbCR / Action 13** : see CbCR skill (forthcoming) - **Transfer pricing documentation** : see `transfer-pricing-workflow-base.md`

### Step 7 : Deferred tax provision

0. **Deferred tax provision:** use the actual accounting framework. Under IFRS, identify temporary differences between carrying amounts and tax bases, applicable recognition exceptions and recoverability; measure using the applicable enacted/substantively enacted law at the reporting date. Apply the IAS 12 Pillar Two deferred-tax exception and targeted disclosures where relevant. Do not treat every accounting timing difference as a recognised deferred-tax balance. Keep the separate GloBE DTL recapture workpaper, its actual timing rules and exceptions, outside the ordinary tax-payment calculation. The detailed recapture rule must come from the current implementation and specialist skill. [IFRS IAS 12 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/).

### Step 8 : Filing assembly

0. **Filing assembly** : Produce: - The return / forms required by the jurisdiction - The reviewer brief (Section 5) - The tax provision schedule for the audit - The tax payment schedule - The supporting documentation index

## Country applications

### United Kingdom

HMRC distinguishes accounts profit from tax profit. Determine revenue/capital character and business purpose; a book expense is not automatically deductible and an asset purchase may require capital allowances rather than an immediate deduction. A return required by a notice still needs filing if the company has a loss or no tax. Use `uk-corporate-tax` and the actual CT600/computation instructions for current rates, reliefs, dates and fields; preparing a reconciliation is not filing it. [HMRC expenses](https://www.gov.uk/corporation-tax-rates/corporation-tax-expenses), [return obligations](https://www.gov.uk/company-tax-returns/overview).

### Singapore

IRAS requires the tax computation before Form C-S/C-S (Lite)/C. Adjust accounting profit for non-deductible expenses, non-taxable receipts, further deductions and capital allowances. Form C requires the relevant statements/computation/supporting schedules, while eligible C-S/C-S (Lite) filers retain them for request. The actual YA and basis period must be established; calendar-year 2026 work is not automatically labelled YA 2026. With a non-SGD functional currency, IRAS distinguishes computation amounts from Singapore-dollar tax payable and provides translation rules; do not copy the accounts currency blindly into every return field. [IRAS computation and currency sections](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-%28lite%29-form-c-filing/preparing-a-tax-computation).

For Singapore's enacted top-up-tax registration scope, the official page requires group consolidated revenue of at least **EUR 750 million in at least two of the four financial years immediately preceding the tested year**, plus the stated Singapore constituent-entity/JV/reverse-hybrid connection. Its ordinary measures apply to financial years beginning on or after **1 January 2025**. Record both conditions, not just a one-year threshold. Other implementation, exclusions, transition and tax computations belong to the actual specialist method. [IRAS registration scope](https://www.iras.gov.sg/taxes/pillar-2-top-up-taxes/registration-for-multinational-enterprise-top-up-tax-and-domestic-top-up-tax).

### Other countries

Keep every original adjustment, regime overlay and slot-contract question below, but obtain its actual law and current period through the country skill. No UK expense classification, Singapore functional-currency rule or Pillar Two enactment is exported to another country. A special regime or unsettled residence remains a specific referral, while supported document preparation can continue.

## Worked cases

**Profit-to-tax reconciliation before a rate.** A hypothetical company has approved profit before tax of 120,000 in its computation currency. Its verified country analysis identifies 3,000 of non-deductible expenses, book depreciation 10,000 to add back and capital allowances 12,000 to deduct, with no other adjustments/losses. Taxable profit is 121,000. Tax is not calculated until the current country rate, relief and period are loaded. These values are example inputs, not statutory rates. [HMRC distinction](https://www.gov.uk/corporation-tax-rates/corporation-tax-expenses), [IRAS adjustment method](https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-%28lite%29-form-c-filing/preparing-a-tax-computation).

```oa-check
name: Accounts profit to taxable profit, no invented country rate
inputs:
  profit_before_tax: 120000
  nondeductible_costs: 3000
  book_depreciation: 10000
  allowed_capital_allowances: 12000
steps:
  - taxable_profit: profit_before_tax + nondeductible_costs + book_depreciation - allowed_capital_allowances
  - adjustment_difference: taxable_profit - profit_before_tax
expected:
  taxable_profit: 121000
  adjustment_difference: 1000
```

**Apply one credit once.** A separately sourced country workpaper establishes gross current tax 20,000 and an allowable foreign tax credit 2,000. Proven advance payments are 15,000. Net current tax liability is 18,000 and the settlement balance is 3,000. Deducting that same foreign credit a second time would understate the balance by 2,000. A separately supported accounting deferred-tax expense of 1,000 makes total tax expense 19,000, but does not change the 3,000 current payment balance. This is a reconciliation example, not a global entitlement to a credit or deferred-tax recognition. [Current/deferred distinction](https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/).

```oa-check
name: Current tax, settlement and accounting expense are separate
inputs:
  gross_current_tax: 20000
  allowable_foreign_tax_credit: 2000
  advance_payments: 15000
  supported_deferred_tax_expense: 1000
steps:
  - net_current_tax: gross_current_tax - allowable_foreign_tax_credit
  - settlement_balance: net_current_tax - advance_payments
  - erroneous_double_credit_balance: settlement_balance - allowable_foreign_tax_credit
  - understatement: settlement_balance - erroneous_double_credit_balance
  - accounting_tax_expense: net_current_tax + supported_deferred_tax_expense
expected:
  net_current_tax: 18000
  settlement_balance: 3000
  understatement: 2000
  accounting_tax_expense: 19000
```

## Section 3 : Conservative defaults principle

- **No invented legal defaults:** uncertainty does not establish a higher-taxed income classification, a taxable receipt, an unavailable deduction or domestic-rate withholding. Retain the deduction/provision, income classification, exemption, treaty and loss/DTA questions separately with the amount, missing fact, source needed and alternative effect where computable. Continue supported reconciliations, but withhold the affected final tax conclusion or filing until resolved. A provisional scenario must be clearly labelled and must never become an assertion that a legal position is correct merely because it produces more tax.

## Ask the client first

Every corporate income tax computation begins with:

```
[BASIC INFORMATION]
1. Corporation legal name and tax ID
2. Country of incorporation
3. Country of tax residence (and any conflict with incorporation country)
4. Tax year-end (calendar year, financial year, accounting period)
5. Accounting period if shorter than 12 months (specify reason : first year, change of accounting reference date, liquidation)
6. Audit status (audited, reviewed, compiled, none) and auditor name if audited
7. Accounting framework (IFRS-IASB, IFRS-EU, local GAAP, FRS 102, Ind AS, ASBE, etc.)

[SCOPE]
8. Industry / sector : confirm not in special regime (banking, insurance, REIT, fund, oil/gas, shipping, aviation)
9. Workforce : number of employees by jurisdiction
10. Activities by country : sales, services, manufacturing, R&D, IP, finance, holding
11. Consolidated group status : is this entity part of a wider group? Top parent identity and country
12. Group's consolidated revenue (for Pillar Two scope test)

[OWNERSHIP]
13. Shareholders : name, country of residence, % held, voting rights
14. Subsidiaries : name, jurisdiction, % held, activity
15. Major intra-group flows : IP licenses, services, finance, goods
16. Permanent establishments in other jurisdictions

[PRIOR YEAR]
17. Brought-forward losses (by category and country)
18. Brought-forward credits (R&D, FTC, etc.)
19. Capital allowances pools and depreciation schedules
20. Provisional payments made in current year

[CURRENT YEAR]
21. Material new positions taken (M&A, restructuring, asset disposal, new operations)
22. Tax authority interactions in the year (audit, ruling, MAP, APA)
23. Known controversies or open assessments
24. DAC6 / MDR / similar disclosures filed in the year

[CONFIRMATIONS]
25. The user confirms they will have the output reviewed by a credentialed practitioner before filing
26. The user confirms they have the authority to provide the data above
```

## Section 5 : Output specification

Every corporate income tax skill must produce a reviewer brief containing:

```
1. Executive summary (1 page)
   - Tax position: total liability, refunds, balance due
   - Year-over-year movement and key drivers
   - Reviewer attention items (flagged [T2] or [T3])

2. Computation walk-through
   - Profit before tax (per audited financials)
   - Reconciliation to taxable profit (line-by-line adjustments with citations)
   - Tax at headline rate
   - Credits and offsets
   - Net tax liability

3. Cross-border / Pillar Two analysis (if applicable)
   - Permanent establishment risk
   - Transfer pricing position
   - Withholding tax on outbound payments
   - Pillar Two scope, ETR, Top-up Tax

4. Deferred tax provision
   - All timing differences with measurement
   - DTA recoverability assessment
   - GloBE DTL recapture risk register with the actual timing/exceptions

5. Supporting schedules
   - Capital allowances / depreciation
   - Brought-forward losses and credits
   - Foreign tax credit utilisation
   - Group relief flows
   - GAAR risk register

6. Reviewer questions
   - All [T2] items requiring reviewer judgement
   - All [T3] items requiring escalation

7. Filing assembly
   - Forms required
   - Supporting documentation index
   - Payment schedule
```

## When to refuse or refer

Refuse to compute and escalate to a credentialed practitioner if:

- **R-CIT-1** : Corporation is a regulated financial institution (bank, insurer, asset manager, fund) : load sector skill
- **R-CIT-2** : Corporation is a REIT or property collective investment vehicle : load sector skill
- **R-CIT-3** : Corporation is in extractive industries with country-by-country reporting under EU CbCR Directive : load sector skill
- **R-CIT-4** : Corporation is in shipping / aviation tonnage tax regime : load sector skill
- **R-CIT-5** : Corporation is a charity / nonprofit : load nonprofit skill
- **R-CIT-6** : Tax authority is currently auditing or has issued a notice of deficiency : controversy strategy first
- **R-CIT-7** : The user is requesting an aggressive position (GAAR risk) : reviewer must approve
- **R-CIT-8** : M&A transaction with material tax-free reorganisation election : reviewer must approve
- **R-CIT-9** : The corporation's tax residence is in dispute (POEM, treaty tie-breaker) : escalate
- **R-CIT-10** : The corporation is in liquidation or insolvency : separate procedural rules
- **R-CIT-11** : The Pillar Two threshold is met but the country has not yet enacted Pillar Two : escalate, complex
- **R-CIT-12** : The corporation has dual-resident status or hybrid mismatches : escalate

**Global refusal catalogue table**

| Refusal | Trigger |
| --- | --- |
| **R-CIT-1** | Corporation is a regulated financial institution (bank, insurer, asset manager, fund) : load sector skill |
| **R-CIT-2** | Corporation is a REIT or property collective investment vehicle : load sector skill |
| **R-CIT-3** | Corporation is in extractive industries with country-by-country reporting under EU CbCR Directive : load sector skill |
| **R-CIT-4** | Corporation is in shipping / aviation tonnage tax regime : load sector skill |
| **R-CIT-5** | Corporation is a charity / nonprofit : load nonprofit skill |
| **R-CIT-6** | Tax authority is currently auditing or has issued a notice of deficiency : controversy strategy first |
| **R-CIT-7** | The user is requesting an aggressive position (GAAR risk) : reviewer must approve |
| **R-CIT-8** | M&A transaction with material tax-free reorganisation election : reviewer must approve |
| **R-CIT-9** | The corporation's tax residence is in dispute (POEM, treaty tie-breaker) : escalate |
| **R-CIT-10** | The corporation is in liquidation or insolvency : separate procedural rules |
| **R-CIT-11** | The Pillar Two threshold is met but the country has not yet enacted Pillar Two : escalate, complex |
| **R-CIT-12** | The corporation has dual-resident status or hybrid mismatches : escalate |

## Section 7 : 18 self-checks

Before delivering output, verify:

1. [ ] Country of tax residence confirmed under its actual domestic tests and applicable treaty provisions; POEM is not presumed a universal sole test
2. [ ] Functional currency identified per IAS 21 / ASC 830 / local GAAP
3. [ ] Audited financial statements available; opinion is unmodified or modifications documented
4. [ ] PBT starting point matches the audited financials
5. [ ] All material non-deductible items added back with citations
6. [ ] All tax-exempt income subtracted with citations
7. [ ] Depreciation reconciled: book vs tax with capital allowances schedule
8. [ ] Brought-forward losses validated against last filed return
9. [ ] Foreign tax credits supported by withholding certificates / receipts
10. [ ] Transfer pricing position documented or master / local file ready
11. [ ] Permanent establishment risk in any non-residence country assessed
12. [ ] Pillar Two scope tested under each actual country implementation, including the required prior-period revenue/consolidation history
13. [ ] Deferred tax recognition, measurement, recoverability and exceptions follow the applicable framework; US GAAP and IFRS recognition tests are not interchangeable labels
14. [ ] GloBE DTL recapture register follows the actual applicable timing rules and exceptions, separate from the accounting deferred-tax balance
15. [ ] GAAR risk identified contemporaneously, not retroactively
16. [ ] DAC6 / MDR / equivalent disclosure status confirmed for the year
17. [ ] Filing deadline, payment deadline, and instalment schedule plotted
18. [ ] Output flags every [T2]/[T3] item for reviewer judgement and includes the reviewer brief

## Section 8 : Citation discipline

- **Citation discipline** : Every figure in the reviewer brief must trace to: - A statutory section (e.g., IRC §163(j), CGI Article 209, KStG §8, ITA §247) - A regulatory citation (Treas. Reg., DGFiP BOI, HMRC manual, ATO PCG) - A judicial decision where positional - The corporation's accounting records line item (general ledger account, journal entry) No figure may rely on "general practice" or "common interpretation" without explicit reviewer escalation.

## Section 9 : Slot contract for country content skills

Every country-level corporate income tax content skill must populate:

```
[REGIME IDENTIFICATION]
- Jurisdiction code (ISO 3166-1 alpha-2 or jurisdiction-specific)
- Statutory framework (act name, sections)
- Tax authority name and portal
- Filing form numbers
- Filing deadline
- Payment / instalment schedule

[RATES]
- Headline corporate income tax rate
- Small company / reduced rate (if any)
- Surcharges (national / regional / sectoral)
- Reduced rates by activity (IP box, R&D, manufacturing zone)
- Branch profits tax rate

[ADJUSTMENTS]
- Statutory list of non-deductible expenses
- Statutory list of tax-exempt income (participation exemption, etc.)
- Depreciation rules (tax life vs accounting life)
- Interest deduction limitation (ATAD-equivalent, §163(j), thin cap)

[LOSSES]
- Carryforward period
- Carryforward cap (% of profit, currency cap)
- Carryback availability
- Change of ownership restrictions
- Group relief mechanism

[CREDITS]
- R&D credit (cross-ref to skill)
- Patent / IP box (cross-ref to skill)
- Foreign tax credit mechanism
- Investment credits
- Withholding tax credits

[FILING MECHANICS]
- Form numbers
- Submission portal / format
- Supporting schedules required
- Audit thresholds

[ANTI-AVOIDANCE]
- GAAR text and key tests
- CFC rules
- Hybrid mismatch rules
- BEAT / GILTI equivalent if applicable

[PILLAR TWO OVERLAY]
- QDMTT in force?
- IIR in force?
- UTPR in force?
- Domestic top-up mechanism

[CROSS-REFERENCES]
- Withholding tax matrix (this skill)
- Pillar Two (this skill)
- DAC6 / MDR (this skill if EU)
- IP box (this skill if regime exists)
- R&D credit (this skill if regime exists)
- Free zone overlay (this skill if applicable)
- Transfer pricing workflow base
```

## Section 10 : Disclaimer

This workflow base produces working papers for review by credentialed practitioners, not direct tax advice. Every output is subject to credentialed reviewer sign-off before filing or acting upon.

The most up-to-date, verified version of this workflow base is maintained at [openaccountants.com](https://openaccountants.com).


## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| HMRC Company Tax Returns overview. Read for accounts/tax-profit distinction and continuing notice-based return duty with a loss or no tax; not every linked CT600 instruction | https://www.gov.uk/company-tax-returns/overview | 2026-11-14 |
| HMRC Corporation Tax expenses. Read for business purpose, capital/revenue distinction, specifically disallowed expenses and capital-allowance routing | https://www.gov.uk/corporation-tax-rates/corporation-tax-expenses | 2026-11-14 |
| IRAS Preparing a Tax Computation. Read What is a Tax Computation and functional-currency sections for adjustments, supporting documents and distinct computation/tax-payable currencies; not every linked relief | https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-%28lite%29-form-c-filing/preparing-a-tax-computation | 2026-11-14 |
| IRAS MTT/DTT registration. Read effective-period and Who needs to be registered sections for prior-four-year revenue test and Singapore connection; no universal country adoption inferred | https://www.iras.gov.sg/taxes/pillar-2-top-up-taxes/registration-for-multinational-enterprise-top-up-tax-and-domestic-top-up-tax | 2026-11-14 |
| IFRS Foundation IAS 12 overview. Read About and May 2023 history entry for current tax, temporary differences and Pillar Two deferred-tax exception; not the complete standard | https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/ | 2026-11-14 |

Not yet confirmed: current country/period rates, exemptions, actual return editions/fields, loss and group-relief limits, treaty/foreign-credit conditions, sector rules, residence and tax-currency choices must be obtained from their country methods and official law. Full applicable IAS 12/local-GAAP recognition exceptions and detailed GloBE DTL recapture timing/exceptions are not certified from an overview; the original blanket five-year add-back is not a universal computation rule. No unresolved deduction, exemption, classification, treaty or DTA question defaults to whichever treatment appears to collect more tax.
