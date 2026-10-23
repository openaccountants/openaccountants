---
name: uk-transfer-pricing
description: "UK transfer pricing under TIOPA 2010 Part 4 for chargeable periods beginning in 2026, after the Finance Act 2026 reform. Covers the arm's length rule (s.147), the participation condition and its new extensions (ss.148A, 162A, 162B), the SME exemption defined through the EU Recommendation 2003/361 euro limits (ss.166 to 173), the new UK-to-UK exemption (s.164A), the unassessed transfer pricing profits charge that replaced diverted profits tax (Part 4A, ss.217A to 217T, CT rate plus 6 points), master file and local file records (SI 2023/818), country-by-country reporting (EUR 750m), the planned international controlled transactions schedule, method choice and benchmarking, compensating adjustments, APAs and penalties. Tax year 2026. Trigger on: TIOPA Part 4, arm's length UK, UTPP, unassessed transfer pricing profits, DPT repeal, UK-to-UK exemption, SME exemption transfer pricing, local file UK, CbCR UK, ICTS. Out of scope: CT rates and base (uk-corporation-tax), non-resident individuals (uk-non-resident-sa109), VAT (uk-vat-return)."
version: 2.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-23
authored_by: OpenAccountants team
reviewed_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - transfer-pricing-workflow-base
category: international
tier: 2
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK transfer pricing (TIOPA 2010 Part 4 and Part 4A), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in the UK.

This skill covers UK transfer pricing for chargeable periods beginning on or after 1 January 2026. Finance Act 2026 (c. 11, Royal Assent 18 March 2026) made three changes that matter for every client:

1. **Diverted profits tax is abolished** and replaced by a corporation tax charge on "unassessed transfer pricing profits" (UTPP) in new TIOPA 2010 Part 4A, for accounting periods beginning on or after 1 January 2026 (FA 2026 s.46 and Sch 5).
2. **Part 4 is reformed** (FA 2026 s.47 and Sch 6): a UK-to-UK exemption, new participation rules, new guarantee and financing rules, a single valuation standard for intangibles, and an updated OECD reference. Most of it applies to chargeable periods commencing on or after 1 January 2026 (Sch 6 para 32).
3. **A power to require an international controlled transactions schedule** (FA 2026 s.48). The regulations are still in draft, for accounting periods beginning on or after 1 January 2027.

The SME exemption did not change. The government consulted on removing it for medium-sized enterprises and decided to keep it, with the euro limits unchanged.

See also: `uk-corporation-tax` (rates, marginal relief, CT600, payment dates, interest and the general penalty table), `uk-non-resident-sa109` (non-resident individuals) and the method skill `transfer-pricing-workflow-base` (functional analysis, method choice, benchmarking workflow, documentation package).

## Who this applies to

**The basic rule (TIOPA 2010 s.147).** Part 4 applies where provision is made or imposed between two persons by a transaction or series of transactions, the participation condition is met, and the actual provision differs from the arm's length provision. If the actual provision gives one party a potential advantage in UK tax, that party's profits and losses are calculated as if the arm's length provision had been made (s.147(3)). The rule only increases UK profits or reduces UK losses. A taxpayer cannot use it to cut its own profit; the other side gets relief through a compensating adjustment claim (s.174).

**Who is a person.** Part 4 applies for corporation tax and income tax, so it reaches companies, partnerships, trustees and individuals carrying on a business. Most cases are companies.

**The participation condition (s.148).** One party directly or indirectly participates in the management, control or capital of the other, or the same person or persons participate in both, at the time the provision is made. From 1 January 2026 three additions apply:
- **s.148A.** HMRC may give a transfer pricing notice treating the condition as met where the old indirect-participation rules (ss.157 to 161) take the case out but there is participation on the ordinary meaning of the words.
- **s.162A.** Two persons under common management arrangements, with a mechanism intended to align shareholders' economic interests, are each treated as controlling the other.
- **s.162B.** Arrangements with a main purpose of avoiding the participation condition are disregarded.
- **s.161 (financing).** The "acting together" rule for financing arrangements was rewritten, with a test for parties holding parallel equity interests.

**Out of scope of an adjustment:**
- **Small and medium-sized enterprises (s.166).** A small or medium-sized enterprise is exempt from the s.147 adjustment, with exceptions (see below).
- **Dormant companies (s.165).**
- **Qualifying UK-to-UK provision (s.164A)**, from chargeable periods commencing on or after 1 January 2026 (see below).

**The SME exemption, step by step (ss.166 to 173).**
1. Measure the whole enterprise, not the UK company alone. TIOPA s.172 uses the Annex to Commission Recommendation 2003/361/EC. Under Annex Article 6, add 100% of the data of linked enterprises (broadly, majority control) and a proportional share of partner enterprises (holdings of 25% or more). HMRC: "these limits apply to the whole group" (INTM412080).
2. Count staff in annual work units: employees, owner-managers and partners who work regularly in the business; part-timers as fractions; apprentices and students on vocational contracts left out (Annex Art 5).
3. Apply the limits in the table below. Staff must be under the ceiling, and turnover or balance sheet total (either one) must not exceed its ceiling (Annex Art 2).
4. Use the figures for the chargeable period itself, on an annual basis. The Annex's two-consecutive-periods rule, the latest-approved-accounts rule and the new-business estimate are switched off by s.172(6) and (7).
5. Convert to sterling at the average rate for the period of account, or the rate on the date the accounts were drawn up if fairer (INTM412080).
6. Check the exceptions. The exemption does not apply where:
   - the enterprise elects out for the period (s.167(2), irrevocable);
   - the other party, or a party to a relevant transaction, is resident in a non-qualifying territory, meaning a territory with no UK treaty containing a suitable non-discrimination article (ss.167(3) and 173; HMRC's list of qualifying treaties is INTM412090; Jersey and Guernsey do not qualify);
   - HMRC gives a medium-sized enterprise a transfer pricing notice (s.168), or gives a small enterprise a notice for patent box transactions (s.167A).

**The UK-to-UK exemption (s.164A).** For chargeable periods commencing on or after 1 January 2026, s.147(3) and (5) do not apply to qualifying UK to UK provision. All of these must hold throughout the period: both parties are UK resident companies; the provision affects both companies' profits and any profits are chargeable to corporation tax; both are charged at the same rate; both use the same reference currency for the provision. It is lost if: one party has a contract that s.589 CTA 2009 takes out of the derivative rules and the other does not; a foreign branch exemption adjustment (s.18A CTA 2009) touches the activities; the provision is patent box provision; or either party is an excluded company (ring fence and oil contractors, life insurers, tonnage tax, banking companies, OEICs, authorised unit trusts, investment trusts, REITs, securitisation companies, QAHCs, electricity generators within the generator levy, residential property developers: s.164A(5)). A company can elect out (irrevocable), and HMRC can give a transfer pricing notice to prevent a net loss of tax looking at both companies together (s.164A(6) to (9)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Corporation tax main rate (applies to most TP adjustments of large companies) | 25% | FY2026 | https://www.legislation.gov.uk/ukpga/2025/8/section/13 |
| UTPP rate | underlying corporation tax rate plus 6% (31% where the main rate of 25% is the underlying rate and no surcharge applies) | APs beginning on or after 1 Jan 2026 | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 |
| UTPP effective tax mismatch threshold | other party's tax on the corresponding profits less than 80% of the UK underlying corporation tax amount | APs beginning on or after 1 Jan 2026 | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 |
| Diverted profits tax | repealed (FA 2015 Part 3); still applies to APs beginning before 1 Jan 2026 | APs beginning on or after 1 Jan 2026 | https://www.legislation.gov.uk/ukpga/2026/11/section/46 |
| Small enterprise: staff | fewer than 50 | 2026 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32003H0361 |
| Small enterprise: turnover and/or balance sheet total | not exceeding EUR 10 million | 2026 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32003H0361 |
| Medium-sized enterprise: staff | fewer than 250 | 2026 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32003H0361 |
| Medium-sized enterprise: turnover / balance sheet total | turnover not exceeding EUR 50 million and/or balance sheet total not exceeding EUR 43 million | 2026 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32003H0361 |
| Partner enterprise / linked enterprise trigger | 25% or more of capital or votes / majority control | 2026 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32003H0361 |
| SME definition adopted for UK TP, with modifications | TIOPA 2010 s.172 | 2026 | https://www.legislation.gov.uk/ukpga/2010/8/section/172 |
| Master file and local file requirement | MNE groups at or above the CbCR threshold | APs beginning on or after 1 Apr 2023 | https://www.legislation.gov.uk/uksi/2023/818/regulation/2 |
| CbCR threshold | consolidated group revenue EUR 750 million, pro-rated for periods other than 12 months | 2026 | https://www.legislation.gov.uk/uksi/2016/237/regulation/3 |
| CbCR filing deadline | 12 months after the end of the reporting period | 2026 | https://www.legislation.gov.uk/uksi/2016/237/regulation/2 |
| ICTS reporting | planned for APs beginning on or after 1 Jan 2027; regulations in draft | 2027 | https://www.gov.uk/government/consultations/transfer-pricing-international-controlled-transactions-schedule |

## The taxable base

**What gets adjusted.** The adjustment replaces the actual provision with the arm's length provision in computing profits and losses (s.147(3)). The UK-side result is the difference between profits as returned and profits on arm's length terms. The adjustment flows through the CT600 computation; there is no separate transfer pricing return.

**How to find the arm's length provision.** Part 4 is read consistently with Article 9 of the OECD Model Tax Convention approved on 18 November 2025 and the OECD Transfer Pricing Guidelines 2022, as later amended, subject to UK reservations (s.164 as amended by FA 2026 Sch 6 para 18). Work in this order (detailed workflow in `transfer-pricing-workflow-base`):

1. **Map the controlled transactions.** List every provision with a participant: goods, services, royalties, loans, guarantees, cost sharing, asset transfers. Drop the ones an exemption removes (SME, UK-to-UK, dormant).
2. **Delineate each transaction.** Read the contracts, then test them against conduct. Do a functional analysis: functions performed, assets used, risks assumed and who controls them. For intangibles, ask who performs and controls development, enhancement, maintenance, protection and exploitation; HMRC's UTPP example gives a passive IP owner only a risk-free return (INTM489135).
3. **Pick the most appropriate method.** The OECD methods are comparable uncontrolled price (CUP), resale price (resale minus), cost plus, transactional net margin method (TNMM) and profit split. There is no strict hierarchy, but where two methods are equally reliable a traditional method is preferred, and CUP is preferred over the others (INTM421010). Other methods are allowed if they give an arm's length result.
4. **Benchmark.** Look for internal comparables first (the tested party's own dealings with independent parties), then external ones (INTM421080). Screen comparables for the comparability factors and remove weak ones; a small number of strong comparables beats a long list of weak ones (INTM484090).
5. **Set the range.** An interquartile range is not required by law; it helps where comparability defects remain and there are enough observations (OECD TPG para 3.57, quoted at INTM485120).
6. **Decide whether to adjust.** If the tested result is inside the arm's length range, no adjustment. If it is outside, HMRC's starting point is to adjust to the median (INTM485120).

**Specific 2026 rules.**
- **Intangibles paid for in kind** are priced as if paid in money (s.151(3)). For transfers and licences of intangible fixed assets made on or after 1 January 2026, a cross-border related-party transaction within Part 4 uses the arm's length price; other cases use market value (FA 2026 Sch 6 paras 24 to 28; INTM414020).
- **Guarantees.** Old ss.152 and 153 are repealed. A guarantee from a participator that lets a borrower borrow more than it could alone is never arm's length (s.153A). Implicit support is not a guarantee (s.154(4A)). A UK resident company can elect to be a deemed guarantor of the excess borrowing (s.153B). These apply to borrowing on or after 1 January 2026, and to all borrowing for periods commencing two years after that date (Sch 6 para 12).
- **Exchange gains and losses** on matched and similar instruments are left out of Part 4 (new s.173A), for chargeable periods commencing on or after 1 January 2026.

**Who bears the other side.** Where only one party is advantaged and the other is within UK tax, the disadvantaged party can claim a compensating adjustment (s.174). From FA 2026 this also covers a UK permanent establishment of a non-resident company (s.174(1A)), deemed always to have had effect. A foreign counterparty gets relief only under the treaty's mutual agreement procedure or its own law.

**Unassessed transfer pricing profits (Part 4A).** A company has UTPP where it made a self-assessment, its profits are subject to a transfer pricing requirement for a provision, and the requirement is not fully reflected in the return (s.217B). HMRC may assess those profits. They are charged at the UTPP rate only if all three conditions in s.217C hold:
1. **Effective tax mismatch outcome (s.217D).** The other party's relevant tax on the corresponding profits (after all reasonable steps to cut it, and net of refunds) is less than 80% of the UK underlying corporation tax amount. Withholding tax on payments to the other party counts as its tax. A transparent other party is presumed to have a mismatch.
2. **Tax design condition (s.217E).** It is reasonable to assume the structure was designed to reduce, eliminate or delay UK income tax, corporation tax or capital gains tax.
3. **Not wholly from excepted loan relationships (s.217C(2)).** Profits arising wholly from loan relationships (and hedges of them) are out.

If a condition fails, HMRC may still assess the profits, but at the ordinary rate. No relief, deduction or set-off is allowed against profits assessed at the UTPP rate (s.217R). Where the SME exemption takes the provision out of Part 4, there is no transfer pricing requirement and so no UTPP (INTM489150).

## Deadlines and filing

| Step | Deadline | Source |
|---|---|---|
| Reflect arm's length pricing in the CT600 | with the return, 12 months after the end of the accounting period | https://www.gov.uk/company-tax-returns |
| Master file and local file (groups at or above EUR 750m) | keep and preserve for the period; produce when HMRC asks by information notice | https://www.legislation.gov.uk/uksi/2023/818/regulation/4 |
| Country-by-country report (UK ultimate parent) | 12 months after the end of the reporting period | https://www.legislation.gov.uk/uksi/2016/237/regulation/2 |
| UTPP preliminary notice | HMRC: no later than 4 years after the end of the accounting period | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 |
| Representations on a preliminary notice | 30 days (60 days where HMRC relies on a transparent other party) | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 |
| UTPP assessment | HMRC: within 60 days of the preliminary notice (90 days for transparent entity cases) | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 |
| Period for amendments | 15 months from the day after the assessment; company may amend its return except in the last 21 days | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 |
| Appeal against a UTPP assessment | within 30 days after the period for amendments ends, and only once the tax is paid | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 |
| Deemed guarantor election (s.153B) | within 4 years after the end of the borrower's first period covered | https://www.legislation.gov.uk/ukpga/2026/11/schedule/6 |
| ICTS (draft) | annual schedule, for APs beginning on or after 1 January 2027 | https://www.gov.uk/government/consultations/transfer-pricing-international-controlled-transactions-schedule |

**Notes.**
- The master file and local file follow Annexes I and II to Chapter V of the OECD Guidelines (SI 2023/818 reg 5). A UK-to-UK controlled transaction can be left out of the local file unless patent box or ring fence trade applies, and transactions under an APA made on or before 31 March 2023 can be left out (reg 6).
- A company below the CbCR threshold still needs evidence that its returned figures are arm's length. HMRC expects documentation proportionate to the size and complexity of the business (INTM483030).
- UTPP is not self-assessed. It only arises when HMRC issues an assessment (INTM489105). Payment of UTPP cannot be postponed except to the extent of tax the other party has actually paid on the same profits (s.217K), and no repayment claim is allowed before the liability is settled (s.217Q).
- **APAs.** An advance pricing agreement is a written agreement with HMRC under TIOPA 2010 ss.218 to 230 covering, among other things, the treatment of provision between a company and its associates. HMRC's process is in INTM422000.

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Inaccurate return from wrong transfer pricing (category 1) | up to 30% careless, 70% deliberate, 100% deliberate and concealed of the potential lost revenue | https://www.legislation.gov.uk/ukpga/2007/11/schedule/24 |
| Disclosure reductions (category 1) | careless: down to 15% prompted, 0% unprompted; deliberate: 35% / 20%; deliberate and concealed: 50% / 30% | https://www.legislation.gov.uk/ukpga/2007/11/schedule/24 |
| Master file or local file not kept, or not produced under an information notice | inaccuracy presumed careless unless reasonable care is shown (FA 2007 Sch 24 para 3C) | https://www.legislation.gov.uk/ukpga/2007/11/schedule/24 |
| Company fails to keep and preserve records | up to £3,000 per accounting period | https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/23 |
| CbCR not filed, or information direction not met | £300, then up to £60 a day after notice | https://www.legislation.gov.uk/uksi/2016/237/regulation/12 |
| Inaccurate CbCR information | up to £3,000 per report | https://www.legislation.gov.uk/uksi/2016/237/regulation/14 |
| UTPP | the 6-point uplift itself; no reliefs against UTPP profits | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 |
| Late payment interest on extra CT | see uk-corporation-tax (Bank Rate plus 4%) | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

HMRC's Business, Assets and International transfer pricing team reviews the proposed penalty position on every transfer pricing settlement (INTM483110). Since FA 2026, transfer pricing determinations no longer need the Commissioners' sanction (old ss.208 to 211 repealed for determinations on or after 18 March 2026).

## Cross-border points

- **Foreign counterparty.** A UK upward adjustment does not reduce the foreign party's tax. Relief comes from the treaty's associated enterprises article and mutual agreement procedure (HMRC INTM423000).
- **Non-qualifying territories.** An SME dealing with a related party in a territory without a qualifying non-discrimination treaty article is inside Part 4 (s.167(3)). Check INTM412090 first; Jersey and Guernsey treaties do not qualify.
- **UK permanent establishments.** Profits of a non-UK company's UK permanent establishment are attributed under CTA 2009 ss.20 to 24 using the separate enterprise principle. For chargeable periods beginning on or after 1 January 2026 these are read with the 2025 OECD Model, the 2010 OECD attribution report and the 2022 Guidelines (FA 2026 s.49 and Sch 7). The new compensating adjustment for permanent establishments is in s.174(1A).
- **Withholding tax.** Royalties and interest paid abroad can carry UK withholding (see uk-corporation-tax). For UTPP, withholding tax on payments to the other party counts towards the other party's tax in the 80% test (s.217D(5)(b)).
- **Controlled foreign companies.** A CFC is not given the UK-to-UK exemption by being assumed UK resident (s.371SD(5A)).
- **ICTS.** FA 2026 s.48 lets HMRC require reports on international controlled transactions: provision meeting the participation condition between a UK company (or a non-resident with UK land or property income, or a partnership with a corporate member) and a non-UK person, or transactions relevant to permanent establishment profits. Exempt transactions (including SME-exempt ones) and transactions under an in-force APA are not expected to be reportable (consultation, June 2026).

## Worked examples

### Example 1: UK subsidiary paying an above-arm's-length royalty

A UK company is a distributor in a large group (1,200 staff worldwide), so it is not an SME. It has 30 associated companies. In its year to 31 December 2026 it pays its overseas parent a royalty of 8% on sales of £10,000,000, which is £800,000. A CUP benchmarking of comparable independent licences gives an interquartile range of 4.0% to 5.5% with a median of 5.0%. The filed 8% is outside the range, so the adjustment is to the median: £500,000. The excess royalty is £300,000.

The company returned taxable profits of £150,000 after deducting the full royalty. With 30 associated companies, the marginal relief upper limit is £250,000 / 31 = £8,064.52, so marginal relief is not relevant and the 25% main rate applies before and after the adjustment. Corporation tax as filed is £37,500. On arm's length terms, profits are £450,000 and tax is £112,500, so the adjustment costs £75,000 of corporation tax, plus late payment interest from the normal due date. The parent's relief, if any, comes through the treaty mutual agreement procedure. If HMRC finds the royalty structure was designed to cut UK tax and the parent's tax on the £300,000 is under 80% of the UK tax, the UTPP rate is in play instead: see Example 2.

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

### Example 2: the UTPP charge compared with the transfer pricing adjustment alone

A large UK company (accounting period 1 January to 31 December 2026) pays an affiliate that owns IP but performs none of the development or control functions. HMRC considers £2,000,000 of the payment is above arm's length, and the company did not reflect that in its CT600. The affiliate pays tax of 10% on the £2,000,000 in its own country. Assume the treaty removes UK withholding on the payment and no bank surcharge applies, so the underlying corporation tax rate is 25%.

The underlying corporation tax amount is £2,000,000 x 25% = £500,000. The corresponding amount is £2,000,000 x 10% = £200,000, which is 40% of £500,000. That is under 80%, so there is an effective tax mismatch outcome. If HMRC also shows the tax design condition, it can assess the £2,000,000 at the UTPP rate of 25% + 6% = 31%: £620,000. Had the company priced at arm's length in its return, the tax would have been £500,000. The UTPP charge costs £120,000 more, with no reliefs allowed against it, and must be paid before the company can appeal. Within the 15-month period for amendments the company can amend its return to reflect the arm's length price; HMRC must then reduce or withdraw any UTPP charge that has become excessive (s.217J(2)).

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

1. **Group size, measured on the whole group.** Staff in annual work units, turnover and balance sheet total of the enterprise with all linked enterprises and the share of partner enterprises, for this chargeable period. This decides the SME exemption.
2. **Who the counterparties are and where they are resident.** Any party in a territory without a qualifying treaty brings an SME back into Part 4. Is either side a transparent entity?
3. **The list of related-party transactions and their 2026 values,** including loans, guarantees, IP licences and asset transfers. Are any purely between UK companies charged at the same rate, and are any of them excluded companies or patent box companies?
4. **Accounting period start date.** Periods beginning before 1 January 2026 stay under diverted profits tax and the pre-reform Part 4.
5. **Consolidated group revenue** against EUR 750 million, for master file, local file and CbCR, and whether an APA is in force.
6. **What the other party pays on the income,** including withholding tax and any refunds. This decides the 80% test for UTPP.

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 2026 s.46 (UTPP, DPT repeal; APs beginning on or after 1 Jan 2026) | https://www.legislation.gov.uk/ukpga/2026/11/section/46 | 2026-10-23 |
| Finance Act 2026 Sch 5 (TIOPA Part 4A ss.217A to 217T; repeal of FA 2015 Part 3) | https://www.legislation.gov.uk/ukpga/2026/11/schedule/5 | 2026-10-23 |
| Finance Act 2026 s.47 and Sch 6 (transfer pricing reform, commencement para 32) | https://www.legislation.gov.uk/ukpga/2026/11/schedule/6 | 2026-10-23 |
| Finance Act 2026 s.48 (international controlled transactions) | https://www.legislation.gov.uk/ukpga/2026/11/section/48 | 2026-10-23 |
| Finance Act 2026 s.49 and Sch 7 (permanent establishments) | https://www.legislation.gov.uk/ukpga/2026/11/schedule/7 | 2026-10-23 |
| TIOPA 2010 s.147 (basic rule) | https://www.legislation.gov.uk/ukpga/2010/8/section/147 | 2026-10-23 |
| TIOPA 2010 s.164 (OECD principles, as amended) | https://www.legislation.gov.uk/ukpga/2010/8/section/164 | 2026-10-23 |
| TIOPA 2010 ss.166, 167, 167A, 168 (SME exemption and exceptions) | https://www.legislation.gov.uk/ukpga/2010/8/section/166 | 2026-10-23 |
| TIOPA 2010 s.172 (SME definition via Recommendation 2003/361) | https://www.legislation.gov.uk/ukpga/2010/8/section/172 | 2026-10-23 |
| TIOPA 2010 s.173 (qualifying territories) | https://www.legislation.gov.uk/ukpga/2010/8/section/173 | 2026-10-23 |
| TIOPA 2010 s.174 (compensating adjustments) | https://www.legislation.gov.uk/ukpga/2010/8/section/174 | 2026-10-23 |
| TIOPA 2010 s.218 (advance pricing agreements) | https://www.legislation.gov.uk/ukpga/2010/8/section/218 | 2026-10-23 |
| Commission Recommendation 2003/361/EC, Annex Arts 2 to 6 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32003H0361 | 2026-10-23 |
| Transfer Pricing Records Regulations 2023 (SI 2023/818) regs 1 to 6 | https://www.legislation.gov.uk/uksi/2023/818/regulation/4 | 2026-10-23 |
| CbCR Regulations 2016 (SI 2016/237) regs 2, 3, 12, 13, 14 | https://www.legislation.gov.uk/uksi/2016/237/regulation/3 | 2026-10-23 |
| Finance Act 2007 Sch 24 (inaccuracy penalties, para 3C TP records presumption) | https://www.legislation.gov.uk/ukpga/2007/11/schedule/24 | 2026-10-23 |
| Finance Act 1998 Sch 18 para 23 (record-keeping penalty) | https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/23 | 2026-10-23 |
| HMRC INTM412070 and INTM412080 (SME exemption and definition) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm412080 | 2026-10-23 |
| HMRC INTM412090 (qualifying treaties list) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm412090 | 2026-10-23 |
| HMRC INTM414020 (summary of transfer pricing reform) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm414020 | 2026-10-23 |
| HMRC INTM414310 (existing exemptions unchanged) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm414310 | 2026-10-23 |
| HMRC INTM414320 (UK-to-UK exemption) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm414320 | 2026-10-23 |
| HMRC INTM421010 (OECD methods, most appropriate method) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421010 | 2026-10-23 |
| HMRC INTM421080 (TNMM) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421080 | 2026-10-23 |
| HMRC INTM483030 (transfer pricing documentation) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483030 | 2026-10-23 |
| HMRC INTM483110 (penalties in transfer pricing cases) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483110 | 2026-10-23 |
| HMRC INTM484090 (arm's length range) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm484090 | 2026-10-23 |
| HMRC INTM485120 (interquartile range, adjust to median) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm485120 | 2026-10-23 |
| HMRC INTM489105 (UTPP introduction) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm489105 | 2026-10-23 |
| HMRC INTM489135 (UTPP mismatch examples) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm489135 | 2026-10-23 |
| HMRC INTM489150 (UTPP exceptions, SMEs) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm489150 | 2026-10-23 |
| HMRC INTM489205 (UTPP process) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm489205 | 2026-10-23 |
| HM Treasury and HMRC, Transfer pricing scope and documentation: summary of responses (SME exemption kept) | https://www.gov.uk/government/consultations/transfer-pricing-scope-and-documentation/outcome/transfer-pricing-scope-and-documentation-summary-of-responses | 2026-10-23 |
| HMRC, International Controlled Transactions Schedule technical consultation (draft regulations) | https://www.gov.uk/government/consultations/transfer-pricing-international-controlled-transactions-schedule | 2026-10-23 |

Not yet confirmed: the ICTS regulations, thresholds and penalties (still in draft; no made instrument found on legislation.gov.uk on 2026-10-23); when UTPP tax is due, since INTM489105 says within 30 days of the assessment while INTM489205 points to the normal TMA 1970 s.59D due date; whether HMRC applies a fixed number of days for producing a master file or local file (the statutory route is an information notice under FA 2008 Sch 36, which sets its own deadline); and the summary audit trail, which HMRC said in 2023 it would consult on further.
