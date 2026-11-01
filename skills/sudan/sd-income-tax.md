---
name: sd-income-tax
description: >
  Prepare Sudan individual income tax workpapers for 2026 intake using the official Income Tax Act and the particular amendments actually opened. Covers employees, sole traders, professionals, landlords and nonresidents with local income, while separating employment bands from business profits. Match Sudan personal income tax, PAYE brackets, freelance tax, rental deductions and ضريبة الدخل questions. Identify income categories, evidence deductions, test mixed income and document the applicable source period before calculating. The later enacted chain, complete income regulations and current forms remain unresolved. This Guide supports source baseline preparation and referral, with explicit stops before filing or treating historical figures as operative 2026 law.
version: 0.2
jurisdiction: SD
tax_year: 2026
last_updated: 2026-11-01
authored_by: Ahmed Hassan
review_status: pending_review
trust_label: Accountant-authored
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tax_year_notes: "2026 intake; opened historical statutory baseline only; later enacted chain unresolved"
---

# Sudan personal and unincorporated income tax v 0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **2026 intake, partial statutory baseline.** Figures below reproduce identified opened instruments, not a completed operative 2026 consolidation. Before filing, paying, granting relief or advising registration, reconcile later enacted amendments and obtain the missing regulations, current forms and directions named in Sources. Passing arithmetic or format checks does not clear this gate. Amounts are source-period SDG; no currency redenomination or indexation is assumed.

## Who this applies to

Individuals with employment, professional, business or rental income. Establish residence and territorial scope through [cross-border residence](sd-cross-border-residence.md), and payroll contributions through [payroll](sd-payroll-social.md). Capital disposals belong to [capital gains](sd-capital-gains.md), not an invented capital-gain schedule inside this Act. Classify employment separately from business before selecting a scale.

## Rates, bands and thresholds

| Item | Opened source wording and conditions | Official source |
|---|---|---|
| Employment, resident annual source-period scale | First SDG 36,000 nil; next 24,000 at 5%; next 24,000 at 10%; next 240,000 at 15%; excess 20%. Nonresident exempt-threshold exclusion needs separate calculation, not a flat 20% shortcut. | [Income Tax Amendment 2021 s.2(f), replacement Schedule III(B), PDF2](https://tax.gov.sd/wp-content/uploads/2025/02/law32-34.pdf) |
| Business/professional individual annual source-period scale | First 3000 nil; next 3000 at 5%; next 4000 at 10%; excess 30%, following the 2019 amendment. Do not substitute the employment scale. | [Income Tax Amendment 2019 s.2(2)(a), PDF1; principal Schedule III(A)(a), PDF136](https://tax.gov.sd/wp-content/uploads/2025/02/law21.pdf) |
| Rental standard expenses | 25% after 2021 amendment, only under s.25 conditions; compare substantiated actual expenses and contractual allocation. | [Income Tax Amendment 2021 s.2(a), PDF1; principal s.25](https://tax.gov.sd/wp-content/uploads/2025/02/law32-34.pdf) |
| Mixed income boundary | Other income no more than one quarter of personal income: total enters personal scale; above that, schedules separate with statutory threshold interaction. | [s.30; PDF52–53](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Older age/service exemptions | Schedule I 2(c)(first and second) deleted in 2022. Do not grant the old over 50 exemption. | [Income Tax Amendment 2022 s.2(5), PDF2; principal Schedule I2(c)](https://tax.gov.sd/wp-content/uploads/2025/02/law38-39.pdf) |

## The base

1. Reconcile salary, allowances, benefits, reimbursements and credited amounts under s.26; retain approval evidence for exclusions. Employer housing needs the s.27 valuation prescription, not a flat percentage. See the cited principal Act ss.26–28.
2. Record pension/insurance/post-service deductions and termination gratuity separately under s.28. Do not automatically deduct every employee contribution or apply a generic allowance in addition to a band exemption.
3. Prepare a distinct business/professional schedule from business receipts less s.18 allowable production expenses. Remove private/capital costs, tax and unsupported reserves. Capital allowances and loss conditions are owned by [company business-profit computation](sd-corporate-income-tax.md).
4. Prepare a rental schedule under s.25. Obtain rent contracts, expense allocation and audited actual-expense records before comparing the standard allowance; do not award expenses borne by a tenant.
5. Apply s.30 to mixed income. The quarter boundary is a classification rule, not authority to tax every receipt at the employment scale. Reconcile tax already deducted using evidence, not assumed finality.

## Deadlines and filing

1. Obtain TIN, period, income schedules, employer certificate, contracts, expense proof and assessment/return notices. The principal return-notice framework is s.38; the actual current self-assessment filing form and boxes are unresolved.
2. Under the opened principal s.38, a person with no notice within three months after basis-period end must notify within the next fourteen days. Do not relabel this as a universal 31 March return date.
3. Retain income-tax books/support for the statutory period and approved Arabic translations as required by the 2022 addition. Present the employer annual list under s.41 where applicable; it does not establish monthly PAYE remittance timing.
4. Stop before submitting or paying until the current return, regulation, deadline and payment reference are established. Save acknowledgement, assessment and payment receipt when an authorised filing is eventually completed. No portal login or actual filing was tested.

## Penalties and interest

The principal Act permits sanctions and recovery; applicable current regulations and amendment interactions have not been fully reconciled. No fixed late-filing fee, monthly interest rate or automatic audit multiplier is approved here. Retain notice/service dates and amounts for review under ss.44,62–63 rather than inventing a penalty.

## Cross-border points

Use the residence/foreign-income and treaty-order workflow in [cross-border residence](sd-cross-border-residence.md). Nonresident personal income loses the exempt threshold under the 2021 replacement schedule; its precise band application must be resolved before computation. Do not assume an automatic foreign-tax credit or a treaty exemption.

## Two worked examples that recompute

### Resident employment scale, historical 2021 wording

Assume an ordinary resident with annual TAXABLE personal income SDG 400,000, no mixed income, and the opened 2021 scale expressly selected for this illustration. The four taxable slices give 1,200 +2,400 +36,000 +15,200 =54,800. This does not confirm the rate for a 2026 filing.

```oa-check
name: 2021 resident annual employment scale
inputs:
  income: 400000
steps:
  - five: min(max(income-36000,0),24000)*0.05
  - ten: min(max(income-60000,0),24000)*0.10
  - fifteen: min(max(income-84000,0),240000)*0.15
  - twenty: max(income-324000,0)*0.20
  - tax: five+ten+fifteen+twenty
expected:
  tax: 54800
```

### Choose rental expense route from evidence

For a source-period eligible landlord bearing the relevant expenses, rent100,000 and substantiated audited allowable expenses30,000 give actual base70,000, compared with75,000 under the standard25% route. Actual evidence reduces the base5,000. If the tenant bears those expenses, this comparison is invalid; do not elect it from arithmetic alone.

```oa-check
name: Rental actual versus standard expense route
inputs:
  rent: 100000
  actual_cost: 30000
steps:
  - actual_base: rent-actual_cost
  - standard_base: rent*(1-0.25)
  - difference: standard_base-actual_base
expected:
  actual_base: 70000
  standard_base: 75000
  difference: 5000
```

## Ask the client first

- Residence evidence and travel dates; ordinary residence facts, not passport alone.
- Exact basis/accounting period, employment and other income separately.
- Contracts, benefit valuation and reimbursement proof; employer withholding certificates.
- Business books, audited rental expenses and which party bears each cost.
- Age/service exemption relied upon, notices already received and foreign taxes paid.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| income-en; selected s.9; PDF 22–23; s.26; PDF 48–50; ss.26(b),27; PDF 50–51; s.28; PDF 51; s.30; PDF 52–53; s.18(1); PDF 29–30; s.18(2); PDF 30–32; s.38; PDF 58–61; s.39(4)–(6); PDF 62–63; s.41; PDF 66–67; s.62(1),(6); PDF 90–91; s.63; PDF 92 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf | 2026-11-01 |
| law 32-34; selected Income Tax Amendment 2021 s.2(f), replacement Schedule III(B), PDF 2; Income Tax Amendment 2021 s.2(a), PDF 1; principal s.25 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law32-34.pdf | 2026-11-01 |
| law 21; selected Income Tax Amendment 2019 s.2(2)(a), PDF 1; principal Schedule III(A)(a), PDF 136 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law21.pdf | 2026-11-01 |
| law 38-39; selected Income Tax Amendment 2022 s.2(5), PDF 2; principal Schedule I 2(c); Income Tax Amendment 2022 s.2(1), PDF 1 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law38-39.pdf | 2026-11-01 |

Writer short-quote ledger: [evidence/ledgers/sd-income-tax.md](../../evidence/ledgers/sd-income-tax.md). Source hashes and actual read scopes are in the Sudan source manifest/read record. Independent review is pending; preserved platform attribution is historical metadata, not a new review of this version.

Legacy-topic controls below refer to the exact original material and line-independent destination records in [the complete old-topic map](../../evidence/ledgers/sd-old-topic-map.md). Each control retains its original rules, figures, groups, procedures and exceptions for source reconciliation. Supported content is replaced above with citations; any remaining original claim under that control is explicitly unconfirmed, not a usable default.

- SD-OLD-048: Section 1 - Scope statement. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-049: Required inputs. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-050: Refusal catalogue. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-051: Personal income tax rates (employment / salary). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-052: Personal tax-free allowance (exemption). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-054: Individual annual return deadline. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-055: Conservative defaults. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-057: Step 2 - Classify income. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-058: Step 3 - Apply personal allowance. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-059: Step 4 - Compute tax on progressive scale. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-060: Step 5 - Apply credits. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-061: Tax exemption categories (Schedule 1, Income Tax Act 1986). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-063: Currency conversion. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-064: Income subject to tax (Art 4, Income Tax Act 1986). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-065: Record-keeping. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-066: Self-assessment and penalties. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-069: Example 3 - Rental income. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-070: Example 4 - Sole proprietor (commercial activity). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-071: Example 5 - Employee over 50 years old (exemption). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-072: Section 7 - Self-checks. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-073: Section 8 - Bank statement reading guide. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-074: Key Arabic banking terms. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-075: Section 9 - Reference material. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-076: PROHIBITIONS. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.

Not yet confirmed: Current enacted amendment chain after the opened instruments; complete 2021 income regulations and 2022 depreciation-table legal effect; current personal allowances, nonresident band application, mixed-income threshold mechanics, family/dependent deductions and foreign-remuneration rules; live return codes, monthly PAYE form/deadline, self-assessment payment/audit procedures and all current sanctions. Legacy claims of SDG 3,000 general personal allowance,15% employment top rate, flat 20% nonresident rate, over 50 exemption and a universal 31 March deadline are not authorised. Zakat, benefits of specific deposits/pensions/diplomats, education/medical relief, donations, bad debts and foreign-credit entitlement require their own operative texts and facts. Residual claims in all legacy-topic controls listed above remain held until individually reconciled.

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
