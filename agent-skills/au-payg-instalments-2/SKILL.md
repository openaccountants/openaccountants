---
name: au-payg-instalments-2
description: "Calculate and vary Australian PAYG instalments using the correct activity statement fields, forecasts and credit rules."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/au-payg-instalments-2"
  jurisdiction: "AU"
  last_updated: "2026-09-08"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Australian PAYG instalments

## Australian PAYG instalments

PAYG instalments prepay income tax on business and investment income. They are separate from GST and PAYG withholding on wages. Use the taxpayer's current activity statement or instalment notice to identify the method, frequency and due date. Sources checked on 8 September 2026.

## Read the notice and reconcile income

The ATO may offer an instalment amount, an instalment rate, or a choice. When a choice is available, the method selected on the first activity statement applies for the rest of that income year. Do not assume every taxpayer can switch methods each quarter. The ATO calculates its notified amount or rate using tax return information and applicable adjustments. Use the notice rather than a historical GDP adjustment percentage.

For the rate method, reconcile instalment income to gross business and investment income excluding GST. It is not net profit: business deductions do not reduce T1. Review unusual receipts against the ATO's definition of instalment income. Salary subject to PAYG withholding and net capital gains are generally excluded. A capital gain can still create a final income tax liability, so include it in the whole-year cash forecast separately. [ATO: calculate PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments).

**Method / Statement fields**  _([ATO: calculate PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments))_

| Method | Statement fields |
| --- | --- |
| Notified amount | T7 shows the ATO amount; transfer the payable amount to 5A where the form requires it |
| Notified rate | T1 is period instalment income; T2 is the notified percentage; multiply income by that percentage to calculate the instalment |
| Varied amount | T8 is estimated annual tax on instalment income; T9 is the varied period amount; T4 is the reason code; 5A is payable |
| Varied rate | T1 is period income; T3 is the varied percentage; T11 and 5A show the calculated instalment; T4 is the reason code |
| Variation credit | 5B records an eligible credit for earlier instalments in the same income year |

- **Zero instalment rate reporting and retention** — If the instalment rate is zero, still report instalment income as required. Retain the statement and the reconciliation used to complete it.

## Decide whether to vary

A variation changes prepayments, without changing the final income tax liability. Estimate the tax attributable to instalment income using a current full-year forecast. Include the taxpayer's other income, deductions and relevant offsets in the estimate; multiplying turnover by a marginal tax rate will usually give the wrong answer.

Under the rate method, the instalment already rises or falls with income. A changed profit margin may justify varying the rate. A temporary cash shortage alone does not establish that the forecast tax is lower. If payment is difficult, lodge the statement and discuss payment arrangements with the ATO.

The variation must be lodged by the instalment due date and before the income tax return for that year is lodged. It applies to the remaining instalments until another variation or the end of the year. [ATO: varying PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments).

## Calculate the variation

- **Quarterly amount instalment cumulative targets** — For quarterly amount instalments, the cumulative targets are 25%, 50%, 75% and 100% of estimated annual tax. Deduct earlier instalments and add back earlier variation credits as required. If entry to PAYG occurs partway through the year, the first instalment quarter is treated as the first quarter for this calculation. Do not assume the taxpayer must immediately catch up to the calendar quarter's percentage.  _([ATO: variation calculations and field instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Negative amount and credit handling** — If the resulting amount is negative, enter zero at T9 and 5A. An eligible credit for earlier instalments can be claimed as a positive amount at 5B. Claiming it is optional; instalments are also reconciled through the annual assessment. Taxpayers paying twice a year use the separate April and July calculation in the ATO instructions.
- **Varied rate formula** — Varied rate (%) = estimated annual tax on instalment income ÷ estimated annual instalment income × 100  _([ATO: variation calculations and field instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Applying the varied rate** — Apply the varied percentage to actual instalment income for the period. If estimated annual instalment income is zero, follow the ATO's zero variation instructions rather than dividing by zero. Select the T4 reason that matches the circumstances. [ATO: variation calculations and field instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments).  _([ATO: variation calculations and field instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_

## Retain the estimate and reconcile the assessment

- **85% underestimate threshold for general interest charge** — Where varied instalments are below 85% of the relevant tax payable, general interest charge may apply to the difference; penalties can also arise. The 85% figure is not a target for deliberately understating tax or immunity from other interest charges. % (An underestimate can leave a tax bill.)

Keep the forecast, assumptions, calculation, reason code and lodged statement. Review the forecast when trading conditions change. Match instalment credits on the income tax assessment to the instalment account and investigate differences before treating an expected credit as available cash.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-09-08. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `au-payg-instalments-2` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/au-payg-instalments-2. If neither is available, confirm every figure against the official source pages cited above before relying on it.
