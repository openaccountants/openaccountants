---
name: uk-transfer-pricing
description: "UK transfer pricing under TIOPA 2010 Part 4 for chargeable periods beginning in 2026, after the Finance Act 2026 reform. Covers the arm's length rule (s.147), the participation condition and its new extensions (ss.148A, 162A, 162B), the SME exemption defined through the EU Recommendation 2003/361 euro limits (ss.166 to 173), the new UK-to-UK exemption (s.164A), the unassessed transfer pricing profits charge that replaced diverted profits tax (Part 4A, ss.217A to 217T, CT rate plus 6 points), master file and local file records (SI 2023/818), country-by-country reporting (EUR 750m), the international controlled transactions schedule from 2027, method choice and benchmarking, compensating adjustments, APAs and penalties. Tax year 2026. Trigger on: TIOPA Part 4, arm's length UK, UTPP, unassessed transfer pricing profits, DPT repeal, UK-to-UK exemption, SME exemption transfer pricing, local file UK, CbCR UK, ICTS. Out of scope: CT rates and base (uk-corporation-tax), non-resident individuals (uk-non-resident-sa109), VAT (uk-vat-return)."
version: 2.2
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - transfer-pricing-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: transfer-pricing
type: situation-rules
---

# UK transfer pricing (TIOPA 2010 Parts 4 and 4A), 2026

> **General reference only.** This Guide has not been reviewed for any person's facts. Do not file, pay or take a tax position without review by a qualified UK professional.

## Who this applies to

For 2026, establish the accounting or chargeable period, participation, exemptions and actual arm's length result before calculating any adjustment. Obtain the ownership and management chart, worldwide enterprise data, contracts, actual conduct, pricing evidence and counterparty tax. Use `transfer-pricing-workflow-base` for the working papers and `uk-corporation-tax` for the full corporation tax computation.

The ordinary rule applies to provision between two persons by a transaction or series, where the participation condition is met, the oil-transaction exclusion does not apply and actual terms differ from terms between independent enterprises. If actual terms confer a potential UK tax advantage, calculate the advantaged person's profits/losses on arm's length terms; if both are advantaged, adjust both. The advantage is lower profits or higher losses, so this is not a unilateral right to reduce one's own taxable profits. See [TIOPA s.147](https://www.legislation.gov.uk/ukpga/2010/8/section/147) and [s.155](https://www.legislation.gov.uk/ukpga/2010/8/section/155).

The adjustment remains subject to the overrides in s.147(6), including capital allowances, chargeable gains, qualifying FX, oil-related expenditure and group mismatch schemes. Do not use this ordinary calculation to decide those specialist outcomes: **Check this point with one of our partner accountants.**

**Participation.** Management, control or capital can be direct, indirect or common to both persons. For non-financing provision, test at the time provision is made or imposed. For financing, also test the six months **beginning with that day**; do not confuse this forward-looking test with the separate acting-together rules in s.161. [Section 148](https://www.legislation.gov.uk/ukpga/2010/8/section/148).

From chargeable periods commencing on or after 1 January 2026, the following also matter ([FA 2026 Sch 6 para 32](https://www.legislation.gov.uk/ukpga/2026/11/schedule/6)):

- Under [s.148A](https://www.legislation.gov.uk/ukpga/2010/8/section/148A), where ss.157–161 prevent participation but ordinary participation exists considering all circumstances, HMRC can give a notice treating participation as met for the period of the notice and subsequent periods. A financing-analogous notice has a financing-only limitation; refer an actual notice for review.
- [Section 162A](https://www.legislation.gov.uk/ukpga/2010/8/section/162A) treats persons under common management arrangements as controlling each other where the arrangements include a mechanism intended to align shareholders' economic interests.
- [Section 162B](https://www.legislation.gov.uk/ukpga/2010/8/section/162B) disregards arrangements with a main purpose of avoiding participation.

**Exceptions.** Test these before making an adjustment:

| Exception | Conditions and action | Source |
|---|---|---|
| Small enterprise | Fewer than 50 staff AND annual turnover **or** balance-sheet total not exceeding EUR 10 million; apply aggregation, period rules and exceptions below. These are euro limits, not Companies Act sterling limits. | Annex Article 2, reproduced by HMRC: https://www.gov.uk/hmrc-internal-manuals/corporate-intangibles-research-and-development-manual/cird92800; https://www.legislation.gov.uk/ukpga/2010/8/section/172 |
| Medium-sized enterprise | Within the SME category: fewer than 250 staff AND turnover not exceeding EUR 50 million **or** balance-sheet total not exceeding EUR 43 million, but not a small enterprise. Same aggregation and exceptions. | Annex Article 2: https://www.gov.uk/hmrc-internal-manuals/corporate-intangibles-research-and-development-manual/cird92800; https://www.legislation.gov.uk/ukpga/2010/8/section/172 |
| Dormant company | Section 165 requires dormancy throughout the accounting period ending 31 March 2004, or (if none) the three months ending then, and continued dormancy since, ignoring s.147. Current dormancy alone is insufficient. | https://www.legislation.gov.uk/ukpga/2010/8/section/165 |
| Qualifying UK-to-UK provision | For chargeable periods commencing on or after 1 January 2026; satisfy all conditions below. | https://www.legislation.gov.uk/ukpga/2010/8/section/164A; https://www.legislation.gov.uk/ukpga/2026/11/schedule/6 |

**SME measurement.** [Section 172](https://www.legislation.gov.uk/ukpga/2010/8/section/172) adopts the Annex with UK modifications. Use annualised data for the chargeable period itself; the two-consecutive-period, latest-approved-accounts and new-business estimate rules do not apply. Leave out a liquidator's or administrator's rights in that capacity. The Article 3(5) autonomous-enterprise declaration is also switched off.

Apply Annex Articles 3 and 6, not just the UK entity's accounts. Add 100% of directly/indirectly linked enterprises' data where not already consolidated; add immediate upstream/downstream partner data proportionately, using the greater capital/voting interest (and greater percentage for cross-holdings), with their linked-enterprise data and the linked enterprises' partner data as Article 6 requires. Links can arise through voting control, board appointments, contractual dominant influence or voting agreements; natural persons acting jointly can link businesses in the same or adjacent markets. A non-linked holding of at least 25% normally creates a partner relationship, subject to the specified investor exceptions. Public-body ownership of at least 25% normally prevents SME status, subject to those exceptions. For investment funds, public bodies, business angels, universities or complex chains, do not assume autonomy: **Check this point with one of our partner accountants.** [Annex Articles 3 and 6, official reproduction](https://www.gov.uk/hmrc-internal-manuals/corporate-intangibles-research-and-development-manual/cird92800).

Count annual work units: employees and persons treated as employees, owner-managers and regularly active partners benefiting financially. Part-year, seasonal and part-time work counts fractionally. Exclude apprentices/students on qualifying training contracts and maternity/parental leave duration. Turnover excludes VAT and other indirect taxes. [Annex Articles 4 and 5](https://www.gov.uk/hmrc-internal-manuals/corporate-intangibles-research-and-development-manual/cird92800). HMRC accepts sterling conversion at the period's average exchange rate or the accounts-drawing-up date rate if fairer ([INTM412080](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm412080)).

The SME exemption in [s.166](https://www.legislation.gov.uk/ukpga/2010/8/section/166) is lost for the relevant provision/period if:

- The enterprise irrevocably elects out for that period, or the other affected person **or any party to the relevant series** is resident in a non-qualifying territory when provision is made/imposed; dual residence in a qualifying territory does not rescue it ([s.167](https://www.legislation.gov.uk/ukpga/2010/8/section/167)). Section 173 includes treaty/non-discrimination and Treasury-designation routes. HMRC's treaty list is dated 1 April 2024; check the operative treaty/designations for the transaction date. HMRC says Jersey and Guernsey do not qualify. For a territory not settled by current authority: **Check this point with one of our partner accountants.** [Section 173](https://www.legislation.gov.uk/ukpga/2010/8/section/173); [INTM412090](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm412090).
- HMRC gives a medium enterprise a notice under [s.168](https://www.legislation.gov.uk/ukpga/2010/8/section/168), or a small enterprise a notice under [s.167A](https://www.legislation.gov.uk/ukpga/2010/8/section/167A) for transactions entering a party's relevant IP profits under the patent box. Check the particular notice and appeal position with a partner accountant.

**UK-to-UK exemption, s.164A.** Both persons must be companies UK resident throughout the relevant period; the provision must enter both companies' profit/loss computations, with any resulting profits chargeable to corporation tax throughout; both must be taxed on those profits at the same rate; and the reference currencies for each part of the provision must never differ. Reference currency means the currency used to calculate taxable profits from that provision, not necessarily the entity's usual functional currency. The exemption fails for a CTA 2009 s.589 contract applying to only one side, relevant foreign-branch exemption adjustments, patent-box provision, or an excluded company at any time in the period. Patent-box provision requires relevant IP income in an overlapping period and an applicable election. [Section 164A(1)–(4)](https://www.legislation.gov.uk/ukpga/2010/8/section/164A).

The excluded-company list includes ring-fence trades and specified post-cessation decommissioning cases, oil contractors, basic life assurance/general annuity business, tonnage tax, banks, OEICs, authorised unit trusts, investment trusts, REITs and REIT members, the specified securitisation/insurance-securitisation companies and transformer vehicles, QAHCs, generating undertakings within the statutory receipts/costs test and residential property developers with developer profits. Check the actual definitions in [s.164A(5)](https://www.legislation.gov.uk/ukpga/2010/8/section/164A); sector membership alone is not a substitute. The potentially advantaged person can irrevocably elect out for a provision or period; HMRC can disapply the exemption by notice to avoid a net loss of tax considering both persons ([s.164A(6)–(10)](https://www.legislation.gov.uk/ukpga/2010/8/section/164A)).

## Rates, bands and thresholds

| Item | Rate / limit and conditions | Official source |
|---|---|---|
| Ordinary corporation tax main rate | 25% in FY2025 and FY2026; use the full CT computation, including associated-company limits, rather than assuming every TP adjustment is taxed at this rate. | https://www.legislation.gov.uk/ukpga/2024/12/section/12; https://www.legislation.gov.uk/ukpga/2025/8/section/13 |
| UTPP rate | Underlying corporation tax rate plus 6 percentage points; **computed** 31% only where the underlying rate is 25% and no additional amount charged as CT applies. | https://www.legislation.gov.uk/ukpga/2010/8/section/217A |
| Banking illustration | **Computed** 34% only if the full UTPP amount bears 25% ordinary CT and an additional 3% bank surcharge after allowance and specific reliefs: 25% + 3% + 6%. Mere banking-company status does not establish this rate. | https://www.legislation.gov.uk/ukpga/2010/8/section/217A; https://www.legislation.gov.uk/ukpga/2010/4/section/269DA |
| Effective tax mismatch | Corresponding relevant tax strictly less than 80% of the underlying CT amount; equality does not meet the test. | https://www.legislation.gov.uk/ukpga/2010/8/section/217D |
| Master/local file threshold | MNE group meeting the EUR 750 million threshold, adjusted for period length and currency, in the **relevant tax period**; this is distinct from CbCR's previous-period test. See records conditions below. | https://www.legislation.gov.uk/uksi/2023/818/regulation/2; https://www.legislation.gov.uk/uksi/2016/237/regulation/3 |
| CbCR threshold | At least EUR 750 million consolidated revenue in period P; report for P+1. Proportionate adjustment for periods longer/shorter than 12 months; non-euro equivalent at P's average exchange rate. | https://www.legislation.gov.uk/uksi/2016/237/regulation/3; https://www.legislation.gov.uk/uksi/2016/237/regulation/3A |

## The base

**Method.** Map goods, services, royalties, loans, guarantees, cost sharing and asset transfers; reconcile contracts to actual conduct, functions, assets and control of risks. For IP, examine development, enhancement, maintenance, protection and exploitation; legal ownership alone does not establish the appropriate return. HMRC's [INTM489135](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm489135) illustrates a risk-free return on its particular passive-owner facts, not a universal IP-owner rule.

[TIOPA s.164](https://www.legislation.gov.uk/ukpga/2010/8/section/164) requires consistency with Article 9 of the 2025 OECD Model and the 2022 Guidelines, as amended/replaced and subject to UK reservations/declarations/elections and the Treasury's powers. Choose the most appropriate method: CUP, resale minus, cost plus, TNMM or profit split; other methods can be used if they establish an arm's length price. Where equally reliable, traditional methods are preferred to transactional profit methods and CUP to others. [INTM421010](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421010).

For TNMM, begin with reliable internal comparable transactions; if unavailable, use comparable independent transactions with functional analysis and justified adjustments. [INTM421080](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421080). Eliminate weak comparables before using a range. An interquartile range is not mandatory: it can improve reliability where comparability defects remain and observations are sizeable. Results within an acceptable arm's length range need no adjustment. Outside it, select a justified point; HMRC regards the median as likely best, rather than as an automatic statutory answer. [INTM485120](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm485120).

**UTPP.** For accounting periods beginning on or after 1 January 2026, FA 2026 s.46 replaces DPT with Part 4A. Earlier periods require the earlier DPT rules; do not use the historic 25% DPT illustration for a 2026 UTPP computation. [FA 2026 s.46](https://www.legislation.gov.uk/ukpga/2026/11/section/46). Under [s.217B](https://www.legislation.gov.uk/ukpga/2010/8/section/217B), the company must have made a self-assessment, provision must exist with another person and the required TP adjustment must be absent or incomplete. UTPP includes omitted profits and the profit-equivalent of losses wrongly included. HMRC assesses the charge; it is not a separately self-assessed uplift. If an exemption removes the TP requirement, that prerequisite is absent.

All three [s.217C](https://www.legislation.gov.uk/ukpga/2010/8/section/217C) conditions are needed for the higher rate:

1. **Mismatch.** Compare relevant tax due/payable on corresponding profits, after reasonable minimisation steps and refunds, with the underlying CT amount. Count non-refunded withholding tax as the recipient's tax. Relevant tax includes income tax, corporation tax on income, amounts treated/charged as CT (excluding the CFC charge) and foreign tax. For a transparent entity, mismatch is presumed unless HMRC is satisfied otherwise; taxes of persons treated as receiving its profits can count. [Section 217D](https://www.legislation.gov.uk/ukpga/2010/8/section/217D).
2. **Tax design.** It is reasonable to assume the structure of the transactions or related arrangements is designed to reduce, eliminate or delay any person's UK income tax, CT or CGT. [Section 217E](https://www.legislation.gov.uk/ukpga/2010/8/section/217E).
3. **Loan exclusion.** The profits must not arise wholly from arrangements producing Part 5 loan-relationship/deemed-loan-relationship debits/credits, or such a loan together with a relevant derivative entered entirely as a hedge of its risk. [Section 217C(2)](https://www.legislation.gov.uk/ukpga/2010/8/section/217C).

The underlying rate includes the ordinary rate on profits if added to other taxable profits plus the effective percentage of other amounts chargeable as CT, after specific reliefs. For small-profit/marginal-relief or partially available bank-allowance cases, do not substitute the illustrations above: **Check this point with one of our partner accountants.** No relief, deduction or set-off is allowed against either UTPP profits charged at the higher rate or the CT on them ([s.217R](https://www.legislation.gov.uk/ukpga/2010/8/section/217R)).

**Other provisions requiring a fact-specific decision.** These remain within the topic, but this Guide supplies no usable election, valuation or relief outcome:

- Financing acting-together tests under s.161 (including its separate prior-six-month test), guarantees, implicit support and deemed-guarantor elections under ss.153A–154; borrowing around 1 January 2026/1 January 2028 and the transitional election. **Check this point with one of our partner accountants.**
- Non-money intangible consideration, cross-border transfers/licences, the unconditional-contract exception and the 1 January 2026 boundary; FX on matched/qualifying instruments and straddling periods under s.173A. **Check this point with one of our partner accountants.**
- Compensating adjustments: s.174 requires a claim by the UK-taxable disadvantaged person, where only one person is advantaged, with the advantaged person's arm's length return/determination reflected consistently (s.176). The ordinary claim window is two years from that return or relevant notice (s.177), subject to the extension in s.186(3). Income-tax restrictions, financing claims and the PE extension in s.174(1A) require separate application: **Check this point with one of our partner accountants.** [Sections 174–177](https://www.legislation.gov.uk/ukpga/2010/8/section/174).

## Deadlines and filing

**Ordinary return and records.** Include the TP computation in the company tax return; the filing date is the latest of: 12 months after the accounting period; 12 months after a relevant period of account no longer than 18 months (or 30 months from its beginning if longer); and three months after service of the notice requiring the return. A live notice or amended-return deadline needs specific checking. [FA 1998 Sch 18 para 14](https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/14). Prepare and retain proportionate arm's length support even below the specified-records threshold ([INTM483030](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483030)).

SI 2023/818 applies for CT periods beginning on/after 1 April 2023 and income-tax years 2024–25 onwards. It covers relevant company, trustee and partnership return persons in qualifying MNE groups, not every individual automatically. Controlled-transaction and no-local-file-information conditions in regs 3–4 matter. Required records are the master file (Annex I, Chapter V) and local file (Annex II), in the prescribed OECD form. The local-file domestic exclusion has patent-box and ring-fence exceptions for persons in the same MNE group; its APA exclusion requires an agreement **made on or before 31 March 2023** having effect during the period. This records exclusion is distinct from the 2026 UK-to-UK adjustment exemption. [SI 2023/818 regs 1–6](https://www.legislation.gov.uk/uksi/2023/818).

Respond within the reasonable period specified in HMRC's information notice; the legislation does not impose a universal 30-day period. Do not use the old 30-day assertion to disregard an actual notice. For materiality, preparation timing, language, a summary audit trail or an unconfirmed supplementary-records notice: **Check this point with one of our partner accountants.** [FA 2008 Sch 36 para 7](https://www.legislation.gov.uk/ukpga/2008/9/schedule/36/paragraph/7).

**CbCR.** A UK ultimate parent satisfying the threshold files for P+1 within 12 months after that reporting period. Non-parent/local filing, surrogate filing, registration, XML transmission, notifications and exchange-arrangement exceptions require their own check; do not assume every UK subsidiary files, or that a generic annual notification remains required. **Check this point with one of our partner accountants.** [SI 2016/237 regs 2–10](https://www.legislation.gov.uk/uksi/2016/237).

**UTPP process.** Refer any actual notice immediately, while preserving these statutory limits:

| Stage | Operative limit and conditions | Source |
|---|---|---|
| Preliminary notice | Designated officer; no later than four years after period end. | https://www.legislation.gov.uk/ukpga/2010/8/section/217F |
| Representations | In writing within 30 days **beginning with issue day**; restricted to arithmetic/figure errors, mismatch or loan-exclusion grounds. The additional 60-day route is only for mismatch representations where the notice relies on transparency. Tax-design merits are not a general preliminary-representation ground. | https://www.legislation.gov.uk/ukpga/2010/8/section/217G |
| Assessment | After considering representations, normally within 60 days beginning with preliminary-notice issue, or 90 where its mismatch basis is transparency. If a tribunal-directed closure notice is required, assessment must wait for it; a closure notice given within that window can extend the assessment limit to 30 days beginning with its issue if later. A further preliminary notice is possible. | https://www.legislation.gov.uk/ukpga/2010/8/section/217H |
| Amend company return | Normally 15 months beginning with the day after assessment; no company amendment in the final 21 days unless the period ends early by written agreement. | https://www.legislation.gov.uk/ukpga/2010/8/section/217I |
| Correct assessment | Within that period, officer must reduce/withdraw excessive higher-rate tax; a failure of a higher-rate condition requires withdrawal or ordinary-rate reassessment at any time. Overpaid tax on those amendments is repayable. | https://www.legislation.gov.uk/ukpga/2010/8/section/217J |
| Payment/postponement | Unpostponed tax follows normal CT due-date/instalment rules. Postponement is limited to non-refunded relevant tax actually paid on corresponding profits. Apply with documentary evidence within 30 days beginning with the day after assessment **or, if later, the day paid relevant tax first becomes positive**; refusal can be referred to the tribunal within 30 days beginning with HMRC's determination document date. | https://www.legislation.gov.uk/ukpga/2010/8/section/217K |
| Appeal | Period for amendments must have ended and tax must be paid in full except validly postponed tax. Notice is due within 30 days beginning with period-end, or the next day if ended by agreement. Do not read the ordinary 30-day assessment appeal rule into this regime. | https://www.legislation.gov.uk/ukpga/2010/8/section/217M |

Section 217L prevents a relevant closure notice before the amendment period ends and restricts later closure amendments; s.217Q bars the specified advance-repayment claims, not all possible repayments. Partnership/corporate-member/Lloyd's cases use Schedule A1 modifications. **Check this point with one of our partner accountants.** The statutory payment rule in s.217K prevails over INTM489105's “due within 30 days” summary.

**ICTS from 2027.** SI 2026/1156 came into force on 26 November 2026 and applies to accounting periods beginning on/after 1 January 2027 (with a separate Lloyd's underwriting-year rule). It is no longer draft. Reporting covers specified transactions under the transfer-pricing and/or PE conditions, subject to exclusions and the made HMRC notice. Do not infer an exemption from the master/local-file rules. For non-managing agents with periods ending on/before 30 September 2027, the submission deadline is the later of 30 September 2028 and the notice date; later periods follow the relevant return deadline. The notice's relevant date is 1 September 2028. For transaction thresholds, aggregation, reporting entity, SME/APA/ICAP and charity exceptions, amendment deadlines, electronic particulars and penalties: **Check this point with one of our partner accountants.** [SI 2026/1156 regs 1–18](https://www.legislation.gov.uk/uksi/2026/1156); [made HMRC notice, paragraph 3.1](https://assets.publishing.service.gov.uk/media/6b085d1a091d49d03c56c134/International_Controlled_Transactions_Schedule_Notice_November_2026.pdf).

**APAs.** An APA is a written agreement with HMRC following an application under s.223, covering one or more statutory matters and declaring itself made under s.218. For unilateral/bilateral/multilateral applications, expression of interest, duration, rollback, fees, processing estimates and annual compliance reports, obtain the applicable agreement/process; do not use the old 3–5 year, 12–18 month or 18–36 month estimates as entitlements. **Check this point with one of our partner accountants.** [TIOPA s.218](https://www.legislation.gov.uk/ukpga/2010/8/section/218).

## Penalties and interest

A company's failure to keep/preserve required records can attract up to GBP 3,000 for the accounting period, subject to paragraph 23's claims-only and specified statement/alternative-evidence exceptions. [FA 1998 Sch 18 para 23](https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/23).

An inaccuracy involving TP, linked to failure over specified TP records or an information notice, is presumed careless unless deliberate or the taxpayer proves reasonable care; a missing file alone does not prove an inaccurate return. [FA 2007 Sch 24 para 3C](https://www.legislation.gov.uk/ukpga/2007/11/schedule/24/paragraph/3C). For category-specific careless/deliberate/concealed penalties, disclosure reductions, CbCR failure/inaccuracy penalties (including knowledge and correction conditions), general information-notice penalties and ICTS penalties: **Check this point with one of our partner accountants.** The six-point UTPP increase is a tax rate, not a substitute for every penalty question.

For HMRC settlement-team review and the former Commissioners' determination-sanction requirements, **Check this point with one of our partner accountants.** This Guide gives no procedural-validity conclusion on a live determination or settlement.

Extra CT may carry interest from its applicable normal due date or instalment dates. Use `uk-corporation-tax` and the date-specific HMRC rates; do not apply a single Bank Rate uplift to all CT liabilities. For actual interest or penalty calculations: **Check this point with one of our partner accountants.**

## Cross-border points

Foreign corresponding relief and treaty mutual agreement procedure are separate from a UK upward adjustment. For the actual treaty, foreign tax, withholding entitlement and refunds, **Check this point with one of our partner accountants.** Count qualifying withholding in the UTPP mismatch test as above, without assuming a UK withholding exemption.

For PE profit attribution and its 2026 OECD changes, CFC interaction (including assumed-residence effects on s.164A), VAT/customs consequences, accounting disclosures and Pillar Two: **Check this point with one of our partner accountants.** For low-value services (including the old 5% simplified-method illustration), materiality, safe harbours and Amount B, do not treat the old summary as an automatic exemption or margin: **Check this point with one of our partner accountants.**

## Two worked examples that recompute

### Example 1: UK subsidiary paying an above-arm's-length royalty

Retained inputs: a UK distributor; 1,200 worldwide staff; 30 associated companies; year ending 31 December 2026; sales GBP 10,000,000; royalty 8%; CUP range 4.0%–5.5%, median 5.0%; returned taxable profits GBP 150,000. Assume the staff figure is the relevant aggregated annual-work-unit figure, no exemption applies, all 30 associates count throughout the full period and the stated profits are also augmented profits. Assume reliable analysis supports the median in these particular facts; it is not an automatic adjustment for every range.

Royalty paid = GBP 800,000; arm's length royalty = GBP 500,000; addback = GBP 300,000. The upper marginal-relief limit is GBP 250,000 / 31 = GBP 8,064.52 (computed); both original and adjusted profits exceed it. With no other reliefs, credits or additional charges, and the 25% main rate in both FY2025 and FY2026, tax as filed = GBP 37,500; adjusted profits = GBP 450,000; tax = GBP 112,500; extra ordinary CT = GBP 75,000. The linked tax rates and [CTA 2010 s.18D](https://www.legislation.gov.uk/ukpga/2010/4/section/18D) support this calculation. Interest and foreign relief are not calculated. UTPP requires all the separate conditions; it is not triggered just by this addback.

```oa-check
name: GB transfer pricing royalty adjustment, main rate 25% (2026)
inputs:
  sales: 10000000
  royalty_paid_rate: 0.08
  arm_length_rate: 0.05
  profit_as_filed: 150000
  associated_companies: 30
  upper_limit: 250000
  ct_rate: 0.25
steps:
  - royalty_paid: sales * royalty_paid_rate
  - royalty_arm_length: sales * arm_length_rate
  - adjustment: royalty_paid - royalty_arm_length
  - reduced_upper_limit: round(upper_limit / (1 + associated_companies), 2)
  - profit_adjusted: profit_as_filed + adjustment
  - ct_as_filed: profit_as_filed * ct_rate
  - ct_adjusted: profit_adjusted * ct_rate
  - extra_ct: ct_adjusted - ct_as_filed
expected:
  adjustment: 300000
  reduced_upper_limit: 8064.52
  profit_adjusted: 450000
  ct_as_filed: 37500
  ct_adjusted: 112500
  extra_ct: 75000
```

### Example 2: UTPP versus the ordinary TP adjustment

Retained inputs: a large UK company, 1 January–31 December 2026; affiliate holding IP without development/control functions; GBP 2,000,000 above the accepted arm's length payment omitted from the return; foreign tax 10%; treaty removes UK withholding; no bank surcharge; underlying CT rate 25%. Assume the full foreign 10% tax remains due on these corresponding profits after all reasonable relief/election/refund steps, no other CT-like charge applies, the tax-design condition is met and the profits are not wholly from excepted loan arrangements. The arm's length amount is an assumed case fact, not inferred solely from IP title.

Underlying CT = GBP 500,000; corresponding tax = GBP 200,000; ratio 40%, below the 80% boundary of GBP 400,000. If assessed under Part 4A, 31% gives GBP 620,000, GBP 120,000 above ordinary CT of GBP 500,000. No relief/set-off is assumed against the higher-rate charge. Return correction and officer reduction follow the amendment conditions above; appeal requires payment only of the amount not validly postponed, after the amendment period. Do not describe the full charge as invariably payable before appeal when corresponding foreign tax may support postponement.

```oa-check
name: GB UTPP at CT rate plus 6 points versus the TP adjustment (AP from 1 Jan 2026)
inputs:
  utpp_profits: 2000000
  ct_rate: 0.25
  uplift: 0.06
  foreign_tax_rate: 0.10
  etmo_threshold: 0.80
steps:
  - underlying_ct_amount: utpp_profits * ct_rate
  - corresponding_amount: utpp_profits * foreign_tax_rate
  - etmo_limit: underlying_ct_amount * etmo_threshold
  - mismatch_ratio: corresponding_amount / underlying_ct_amount
  - utpp_rate: ct_rate + uplift
  - utpp_charge: utpp_profits * utpp_rate
  - tp_adjustment_only: underlying_ct_amount
  - utpp_extra: utpp_charge - tp_adjustment_only
expected:
  underlying_ct_amount: 500000
  corresponding_amount: 200000
  etmo_limit: 400000
  mismatch_ratio: 0.40
  utpp_rate: 0.31
  utpp_charge: 620000
  utpp_extra: 120000
```

## Ask the client first

Obtain the period dates; direct/indirect/common management and financing relationships; annualised worldwide staff/turnover/assets with linked/partner data; counterparty residence and actual foreign tax/refunds; transaction values, contracts, conduct, functions/assets/risks and benchmarking; UK-to-UK currency/rate/sector/election facts; MNE revenue for both current-period records and previous-period CbCR tests; any APA, HMRC notice, filing or amendment deadline. If an essential fact or a referred point is unresolved, withhold that outcome and use the partner-accountant route.

## Sources

The linked operative sections were read on 27 November 2026, except the expressly reused corporation-tax rows below. The section lists identify the portions read; they do not claim a whole-Act read.

| Source / portions read | Official source | Read on |
|---|---|---|
| TIOPA Part 4: ss.147–148A, 155, 162A–162B, 164–168, 172–174, 176–177; participation, exemptions, OECD standard and claims | https://www.legislation.gov.uk/ukpga/2010/8/part/4 | 2026-11-27 |
| TIOPA Part 4A: ss.217A–217M, 217Q–217R; gateways, rates, notice/assessment/amendment/payment/appeal safeguards | https://www.legislation.gov.uk/ukpga/2010/8/part/4A | 2026-11-27 |
| FA 2026 s.46 and Sch 6: commencement, participation/UK-to-UK provisions and special transitions | https://www.legislation.gov.uk/ukpga/2026/11/section/46; https://www.legislation.gov.uk/ukpga/2026/11/schedule/6 | 2026-11-27 |
| Recommendation 2003/361: full operative Annex Articles 1–6, reproduced by HMRC | https://www.gov.uk/hmrc-internal-manuals/corporate-intangibles-research-and-development-manual/cird92800 | 2026-11-27 |
| SME exchange rate and treaty-list caveats | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm412080; https://www.gov.uk/hmrc-internal-manuals/international-manual/intm412090 | 2026-11-27 |
| Methods, internal comparables and ranges | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421010; https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421080; https://www.gov.uk/hmrc-internal-manuals/international-manual/intm485120 | 2026-11-27 |
| Proportionate documentation; UTPP administration and IP example | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483030; https://www.gov.uk/hmrc-internal-manuals/international-manual/intm489105; https://www.gov.uk/hmrc-internal-manuals/international-manual/intm489135 | 2026-11-27 |
| TP records regulations 1–6, including OECD-format table and exclusions | https://www.legislation.gov.uk/uksi/2023/818 | 2026-11-27 |
| CbCR definitions, period/threshold, filing and penalty conditions, regs 2–20 | https://www.legislation.gov.uk/uksi/2016/237 | 2026-11-27 |
| ICTS regulations: commencement, reporting, deadlines, exemptions and penalties | https://www.legislation.gov.uk/uksi/2026/1156 | 2026-11-27 |
| Made ICTS notice: status and paragraphs 2–5; not the full transaction particulars | https://assets.publishing.service.gov.uk/media/6b085d1a091d49d03c56c134/International_Controlled_Transactions_Schedule_Notice_November_2026.pdf | 2026-11-27 |
| Information notice powers and deadline, paras 1 and 7 | https://www.legislation.gov.uk/ukpga/2008/9/schedule/36 | 2026-11-27 |
| Company return filing (para 14), records penalty and exceptions; TP careless-presumption conditions | https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/14; https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/23; https://www.legislation.gov.uk/ukpga/2007/11/schedule/24/paragraph/3C | 2026-11-27 |
| FY2025 rate; association limits/formula; bank surcharge conditions | https://www.legislation.gov.uk/ukpga/2024/12/section/12; https://www.legislation.gov.uk/ukpga/2010/4/section/18D; https://www.legislation.gov.uk/ukpga/2010/4/section/269DA | 2026-11-27 |
| FY2026 main rate and interest: reused unchanged operative reads from uk-corporation-tax; applicability checked for these cases | https://www.legislation.gov.uk/ukpga/2025/8/section/13; https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-26 |

Not yet confirmed: no usable conclusion is supplied for the expressly referred points above, including the historic safe-harbour/APA/notification assertions and the original marginal-relief UTPP question. Check this point with one of our partner accountants. EUR-Lex returned a JavaScript challenge on 27 November 2026; the SME Annex was read in full in HMRC's official reproduction at CIRD92800, with the UK modifications read in TIOPA s.172.
