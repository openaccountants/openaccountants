---
name: il-freelancer-ops
description: Use this skill when advising Israeli freelancers (עצמאים) on business operations, tax deadlines, threshold monitoring, invoice requirements, and accountant package preparation. Trigger on phrases like "osek patur threshold", "freelancer Israel taxes", "עוסק פטור", "עוסק מורשה", "עסק זעיר", "esek za'ir", "mkdamot", "מקדמות", "havila l'roe cheshbon", "bituach leumi self-employed", "ביטוח לאומי עצמאי", "freelancer deadlines Israel", or any Israel freelancer operations query. ALWAYS read this skill before advising on Israeli freelancer tax operations.
version: 1.2
jurisdiction: IL
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
---

# Israel: freelancer registration, records and compliance

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Scope

Prepare a 2026 compliance and accountant-handoff plan for an Israeli sole proprietor. VAT status, the income-tax micro-business regime and National Insurance status are separate classifications. Use [israel-vat](israel-vat.md) for VAT computation and [il-income-tax-returns](il-income-tax-returns.md) for annual tax, bands and pension-relief ceilings. Do not assume that a small business is exempt from income tax or National Insurance.

| Quick reference | Rule and conditions | Official source |
|---|---|---|
| VAT Patur ceiling | Turnover across all businesses does not exceed NIS 122,833 in 2026; reg.13 compulsory professions override turnover | VAT Law s.1, https://www.btl.gov.il/Laws1/00_0022_000000.pdf |
| Micro-business deduction | 30% of qualifying turnover replaces actual business expenses, subject to ss.87B-87E conditions; can apply to Patur or Murshe within the statutory ceiling | ITO ss.87B-87E, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Patur annual declaration | Previous calendar year's turnover by 31 January | Rights guide VAT annex s.4, https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf |
| Micro-business short report | Service baseline 31 March following the year; tax-year 2025 alone extended to 31 August 2026 | ITA reporting service, https://www.gov.il/he/service/report-and-payment-for-micro-business-owner |

## Ask the client first

Obtain VAT, income-tax and National Insurance registrations and notices; actual occupation and expected annual turnover; employees and other work/income; current/former employer and related-party customer revenue; acceptable books; any transparent-entity income or company control; invoices/receipts, bank and cash records; advance-payment rates and dates; pension certificates/insured income; and prior-year micro-business choices. Identify spouse/full-return obligations and specialist foreign/property/crypto activity. Check the actual authority-assigned VAT period and National Insurance contribution class rather than using a default.

## The method, step by step

### Choose and document the three separate statuses

A Murshe may issue tax invoices and must account for VAT on taxable supplies; 18% is the standard rate from 1 January 2025 under ITA Interpretation01/2025, subject to the actual tax point and supply treatment, not every invoice. Input deductions need lawful documents and taxable use. A Patur cannot charge VAT, issue tax invoices or deduct input VAT; it still keeps records, issues receipts and makes its annual turnover declaration. Doctors, architects, technicians and bookkeepers are examples of compulsory Murshe professions under registration reg.13, irrespective of turnover. Register/change VAT classification through the VAT authority, not by treating an income-tax micro-business election as a VAT exemption ([rights guide VAT annex](https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf)).

Baal/Esek Za'ir is an income-tax status. Under s.87B, an individual must be a resident, within the turnover ceiling linked to the VAT Patur definition, and registered with the assessing officer. The 30% deduction replaces ordinary deductions under ss.17-27, **except the express s.17(5a) qualifying study-fund deduction**, whose actual eligibility/caps require separate review; s.87D also excludes the ordinary s.47A National Insurance deduction for this business income. Asset-disposal depreciation adjustment and cessation-year rules have their own s.87D conditions, so do not assume switching regime leaves basis or deductions unchanged ([ITO ss.87B-87D](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

### Screen every micro-business exclusion

Under s.87E, the deduction is unavailable where the taxpayer employs workers, lacks acceptable books, has business/professional income not produced by personal exertion, receives any business income from the current employer, has income attributed from a transparent entity, is a controlling shareholder under s.32(9), or fails an additional prescribed condition. It is also unavailable where **more than 25%** of business/professional income comes from a statutory relative or from someone who employed the taxpayer at any time in the preceding **3 tax years**. This is not a ban on every former-client employment relationship and not a rule for every unrelated single customer. After taking the deduction, electing out in the following income-producing year generally also prevents the deduction in the next **2 tax years**; apply the cessation-year deeming rule separately ([ITO s.87E](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

Reduced reporting is a separate screen: ITA's official reform explanation requires recognition as a micro-business, statutory eligibility, and neither the taxpayer nor spouse being required to file a full return for another reason. A recognized eligible business can still file a full return and claim the normative deduction; simplified reporting is not a blanket exemption from every return. The short-report service requires in-year tax coordination. A 30% deduction without attaching expense receipts to that service does not dispense with books, income records or evidence for withholding/pension claims ([ITA explanation](https://www.gov.il/BlobFolder/policy/income-tax-small-business-owner-24-210725/he/IncomeTax_procedures-210725-1.pdf); [short-report service](https://www.gov.il/he/service/report-and-payment-for-micro-business-owner)).

### Invoice and allocation controls

Keep a sequential invoice/receipt register, investigate gaps and credit notes, and reconcile payments/partial payments to the issued documents. Check actual legal invoice fields: supplier/dealer identity/address/number, tax-invoice/original designation, serial/date, transaction details, net amount, separately shown VAT, gross and signature as applicable. Patur receipts do not create deductible VAT. The VAT sibling owns the full document conditions and allocation thresholds: above NIS 10,000 before VAT from 1 January 2026, above NIS 5,000 from 1 June 2026, a missing required allocation number blocks the recipient's input claim. It is not a universal allocation requirement for every small invoice ([rights guide VAT annex ss.7-8](https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf)).

### Maintain a notice-based calendar

Use the registered monthly/bimonthly VAT period. The rights guide baseline is 15 days after period end, with online/detailed routes described in the VAT sibling; zero-activity returns remain required. Its recovered low-turnover frequency branch is unresolved, so do not default to bimonthly. The old March/May/July/September/November/January 15 calendar applies only if that reporting cycle and baseline are actually assigned, subject to live extensions.

For income-tax advances use the assessment notice, approved rate and period, then reconcile to annual liability; no universal two-month calendar is inferred. Section 87F permits micro-business advance exemption under its conditions, not automatic cancellation of any existing demand. For National Insurance use the actual projected-income assessment and payment notice; distinguish advances from final contribution adjustment. Holiday/Shabbat shifts and direct-debit extensions require the specific current notice, not an automatic Sunday assumption ([ITO ss.87F,175](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

The Patur declaration is due by 31 January for the preceding year. The micro-business reporting service gives 31 March of the following year as baseline; its 31 August 2026 extension is expressly for **2025 only**. Do not extend that relief to tax year 2026. Ordinary annual-return/representative dates, detailed-reporting duty and pension payment timing require their current instructions rather than the old fixed calendar.

### Monitor turnover before a status change

Track cumulative annual turnover, the VAT definition of turnover, and a separate forecast; profit and bank deposits are not automatically turnover. Keep the old internal alerts at 70%, 85% and 95% as **workflow choices**, not legal thresholds. On NIS 122,833, exact derived alert amounts are NIS 85,983.10, NIS 104,408.05 and NIS 116,691.35. A forecast above the ceiling prompts review now; it is not proof turnover has already exceeded it.

On an actual crossing or compulsory-profession issue, contact the VAT office through the authorized process, settle effective classification/tax treatment, change invoice format/required allocation-number setup, start assigned periodic returns and eligible input tracking, and notify customers of invoicing changes. Reassess National Insurance independently rather than assuming a VAT change necessarily increases contributions. Micro-business shares the linked ceiling but is not a way to defer VAT reclassification; any cessation-year deduction exception needs s.87D(c), not a casual promise.

### National Insurance: separate NI and health

These rates apply to a self-employed person aged **18 to before retirement age** from 1 January 2026. Other ages, pension receipt, mixed employment and classification can change the result. Do not apply the employee/controlling-shareholder table to an independent fee recipient.

| Monthly contribution-income slice | NI | Health | Total | Official source |
|---|---|---|---|---|
| Up to NIS 7,703 | 4.47% | 3.23% | 7.70% | NII working-age table, https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx |
| Above NIS 7,703 to the NIS 51,910 contribution maximum | 12.83% | 5.17% | 18.00% | NII working-age table, https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx |
| Below NIS 3,442 monthly income | Contributions use the applicable minimum-income basis | Included under relevant class | Not a fixed NIS 187 advance | NII minimum paragraph, https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx |

The Hebrew working-age table confirms the NIS 51,910 maximum; ordinary direct HTML recovery resolved the English page's malformed maximum field. Under ordinary ITO s.47A, 52% of eligible NI contributions paid for non-employment income is deductible subject to the income limit; the separate health insurance component is outside this NI contribution deduction. Under s.47A(b1), from 2025, prior-year NI refunds reduce current contributions paid before applying 52%; an excess refund produces business income equal to 52% of that excess. Reconcile refund notices as well as payments. Do not apply this on top of the micro-business s.87D normative deduction. An old NIS 7,850 maximum advance cannot be derived by simply multiplying a ceiling by 18%, since marginal bands and assessment adjustments matter ([ITO ss.47A,87D](https://www.btl.gov.il/Laws1/00_0103_000000.pdf); [NII page](https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx)).

### Pension: obligation and tax relief are different

Identify mandatory contribution status separately from s.45A credit and s.47 deduction. Obtain member status, insured/non-insured income, deposit certificates and the tax-year conditions; the annual-return skill owns the individually labelled 2026 ceilings. Do not promise both benefits are entirely forfeited from a generic missed 31 December date, or apply 5.5%/11% to unlimited NIS 300,000 income. The old mandatory 4.45%/12.55% contribution formula and average-wage basis need the applicable pension statute and actual eligibility before a deposit instruction.

## Worked cases

### Forecast above the Patur ceiling, before actual crossing

Retain the web developer with NIS 95,000 turnover after 9 months and 3 months remaining. Average monthly turnover is NIS 10,555.56 (rounded), annual forecast NIS 126,666.67, forecast excess NIS 3,833.67. Current turnover is about 77.34% of the ceiling, so it has passed the internal 70% alert, **not the 85% alert**. Begin an accountant's transition review without pretending forecast turnover is already earned.

```oa-check
name: Patur forecast and actual alert stage
inputs:
  turnover: 95000
  elapsed_months: 9
  ceiling: 122833
steps:
  - monthly_average: turnover/elapsed_months
  - projection: monthly_average*12
  - projected_excess: projection-ceiling
  - current_percent: turnover/ceiling*100
  - alert_70: ceiling*0.70
  - alert_85: ceiling*0.85
  - alert_95: ceiling*0.95
expected:
  projection: 126666.67
  projected_excess: 3833.67
  current_percent: 77.34
  alert_70: 85983.10
  alert_85: 104408.05
  alert_95: 116691.35
```

### Contribution estimate and the micro-business deduction boundary

Assume the NII has confirmed contribution income NIS 20,000/month, working-age class, no mixed employment and no further assessment adjustment, with the applicable maximum above that input. NI is NIS 1,922.03 and health NIS 884.56, total NIS 2,806.59. This is a conditional marginal calculation, not a final advance notice. Separately, an eligible micro-business with NIS 100,000 qualifying turnover deducts NIS 30,000 normatively and has NIS 70,000 before other applicable personal relief. It does not also deduct ordinary business expenses or s.47A NI from that business base; the express s.17(5a) exception still requires its own eligibility/cap review.

```oa-check
name: NI health split and separate normative business base
inputs:
  monthly_income: 20000
  micro_turnover: 100000
steps:
  - ni: 7703*0.0447+(monthly_income-7703)*0.1283
  - health: 7703*0.0323+(monthly_income-7703)*0.0517
  - total: ni+health
  - normative_expense: micro_turnover*0.30
  - micro_base: micro_turnover-normative_expense
expected:
  ni: 1922.03
  health: 884.56
  total: 2806.59
  normative_expense: 30000
  micro_base: 70000
```

Retain the old consultant's NIS 300,000 annual income, 15 December with no pension deposits: urgent evidence/eligibility review is appropriate, but the former NIS 16,500 credit base/NIS 5,775 credit and NIS 33,000 deduction are **not established deposit targets**. The applicable income ceilings, insurance status, interaction and payment rules must be applied first; the missing-deposit fact does not prove a particular tax saving.

## When to refuse or refer

Refer uncertain registration/profession status, threshold crossings, disqualifying customer/employment relationships, micro-business entry/exit, missing books, mixed employment/retirement, unsupported contribution ceilings, pension obligations, foreign income and tax-year deadlines. Do not convert a missing certificate into a tax-status default. Obtain CPA review before any registration change or filing.

## Filing and payment

For an eligible recognized micro-business, complete tax coordination during the year, then the official short-report service after year-end: enter actual turnover, supported non-salary withholding and qualifying pension information, review the computed base/tax and pay any balance separately. Keep the acknowledgment, bank/refund information and certificates; the service does not require attaching transaction/expense documents, but does require evidence for reported withholding/pension. If a full return is required, use that route and the applicable deduction rules instead ([official service](https://www.gov.il/he/service/report-and-payment-for-micro-business-owner)).

Prepare the accountant package by period using invoices-issued, invoices-received, utility-bills and bank-statements folders. Include a revenue summary with monthly breakdown. Cover sheet: period covered (month/quarter/year), gross revenue, actual expenses with deductibility status, profit before/after tax adjustments, VAT collected/eligible input, net VAT, running turnover and document counts. Keep these distinct from normative micro-business deductions. Track invoice balances and partial payments; internal aging buckets 0-29, 30-59, 60-89 and 90+ days support reminders, documented follow-up and escalation, not tax deadlines. No client message or payment is sent by this skill.

## Completion checklist

Confirm all registrations and relevant year, reconcile books/invoices/bank, test every micro-business condition, track actual/forecast turnover, confirm invoice allocations and VAT period, reconcile advance notices and contribution class, separate pension obligation from relief, assemble the package and unresolved items, obtain review and retain filing/payment acknowledgments.

## Sources

| Source | URL | Read on |
|---|---|---|
| Consolidated Income Tax Ordinance; Read for s.47A NI deduction/exclusion, ss.87B-87F micro-business residence/turnover/registration, 30% calculation and expense exclusions, disqualifiers/entry-exit and advance exemption, s.175 notice-based advances | https://www.btl.gov.il/Laws1/00_0103_000000.pdf | 2026-11-14 |
| Consolidated VAT Law; Read for s.1 Patur turnover does-not-exceed boundary across all businesses | https://www.btl.gov.il/Laws1/00_0022_000000.pdf | 2026-11-14 |
| ITA Interpretation01/2025; Read for introduction giving standard18% on Israeli transactions and goods imports with tax point from1January2025 under the2024 amending order | https://www.gov.il/BlobFolder/policy/vat_11/he/vat_represent-info-051224-2.pdf | 2026-11-14 |
| ITA 2025 rights guide, 2025-2026 filing cycle; Read for VAT annex January2026 Patur ceiling, reg.13 professions, receipts/annual declaration, invoice/allocation rules and periodic returns | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-14 |
| NII Hebrew self-employed contribution page; Read for working-age NI/health slices, NIS 51,910 maximum, minimum-income paragraph and effective date; direct HTML read recovered text after web-tool timeouts | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx | 2026-11-14 |
| ITA micro-business reform explanation; Read for pp.2-3 historical 2024/2025 ceiling and final short-report conditions, spouse/full-return test, voluntary registration and full-return deduction option | https://www.gov.il/BlobFolder/policy/income-tax-small-business-owner-24-210725/he/IncomeTax_procedures-210725-1.pdf | 2026-11-14 |
| ITA micro-business short-report service; Read for recognition/tax-coordination requirement, reporting inputs/evidence, outcome/payment and baseline plus 2025-only extension | https://www.gov.il/he/service/report-and-payment-for-micro-business-owner | 2026-11-14 |

Not yet confirmed: NI advances NIS 187/NIS 7,850 and 15th/22nd dates, ordinary income-tax 15th/19th advance calendar, detailed-reporting NIS 500,000 trigger/PCN874, automatic monthly new-business reporting and low-turnover VAT frequency remain unconfirmed. Ordinary Form 1301 29 May/30 June 2026 and CPA July31-or-later extensions, tax-year2026 full-return dates, automatic holiday shifts, pension31December forfeiture claim and mandatory4.45%/12.55% eligibility/basis remain withheld. Old pension amounts NIS11,640+1,164, NIS232,800/NIS25,608 and blanket5.5%/11% bases are not usable without full relief computation; the old NIS13,769 average-wage statement is not proof of the mandatory pension basis. Detailed s.87D cessation/asset adjustments and exceptional compensation/benefit turnover inclusions require their actual conditions before use.
