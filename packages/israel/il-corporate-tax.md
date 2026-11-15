---
name: il-corporate-tax
description: Use this skill when advising on Israeli corporate tax strategy, profit extraction methods, or controlling shareholder (בעל שליטה) tax planning. Trigger on phrases like "corporate tax Israel", "dividend vs salary Israel", "baal shlita", "בעל שליטה", "halokat dividendim", "חלוקת דיבידנדים", "shareholder loan Israel", "halvaat baalim", "הלוואת בעלים", "Section 3 tet", "סעיף 3 ט", "dmei nihul", "דמי ניהול", "management fees Israel", "chevra me'atim", "חברה מעטים", or any Israeli corporate tax extraction query. ALWAYS read this skill before advising on Israeli corporate profit extraction.
version: 1.2
jurisdiction: IL
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: decision
---

# Israel: company tax and owner extraction

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

> **General reference only.** Prepare a company/shareholder comparison and compliance brief for an Israeli CPA. Cash withdrawal, distributable profit and taxable benefit are different bases.

## Scope

2026 ordinary company income tax, individual dividend/salary comparison, shareholder loans, management fees and closely held company warnings. Special investment regimes, foreign tax credit computations, company-law distribution legality and a complete s.62A/s.81 retained-profit computation require specialist work.

| Quick reference | Rate or threshold with conditions | Official source |
|---|---|---|
| Ordinary company taxable income | 23%, subject to special-rate/excluded income rules | ITO s.126(a)-(c), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Dividend to individual | 25%; 30% if material shareholder on receipt or at any time in prior 12 months | ITO s.125B(1)-(2), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Material shareholder | At least 10% of a control right, directly/indirectly, alone/together under statutory definition | ITO s.88, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Prescribed s.3(i) interest in 2026 | 6.53%; interest benefit is not a tax on principal and not protection from s.3(i1) withdrawal taxation | ITO s.3(i) 2026 footnote; booklet p.15, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Closely held extra tax | 2% on statutorily computed excess profits after the year's dividend subtraction, subject to exceptions; not 2% of all retained earnings | ITO ss.81B-81C, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

Personal bands, credit-point value and both surtax bases are owned by [il-income-tax-returns](il-income-tax-returns.md). Self-employed contributions, applicable to a genuine self-employed fee recipient, are owned by [il-freelancer-ops](il-freelancer-ops.md). VAT is owned by [israel-vat](israel-vat.md).

## Ask the client first

Obtain company residence and regime; taxable and distributable profits, losses, cash requirements and ownership/control history; all shareholder/related-party balances, withdrawals, repayments and private asset use; other shareholder income and capital-source income; age/residence/NI classification; payroll and employer costs; pension/study-fund deposits and limits; service contracts and actual work; current tax/withholding certificates and returns. Do not default to a material holding or closely held classification without the documents.

## The method, step by step

### Compute company tax before a dividend

Start with taxable profit after permitted deductions and adjustments, not bank cash. Apply s.126 and any proven special regime. Domestic intercorporate dividends and foreign dividends have distinct s.126 rules; an individual's extraction calculation does not answer the recipient-company question. A dividend is paid from after-company-tax distributable amounts and is not a company expense ([ITO ss.125B,126](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

For an individual, material status includes the statutory control rights and joint/indirect holdings, and the higher dividend rate has a preceding-period test. Do not replace it with “currently owns more than 10%.” Check company-law earnings/solvency and approvals separately before distribution. A tax calculation is not proof a distribution is legally available.

### Compare actual salary and dividend costs

Salary for actual services needs the allowable expense and timing rules, including s.18(b) closely held-company payment timing, payroll withholding, employer/employee NI and pension/study-fund costs. Dividends have company tax first, shareholder dividend tax and potentially both surtax bases. Any NI treatment of the actual receipt must be established; do not assume every reclassified shareholder withdrawal is free of NI.

An ordinary 23% company rate followed by a 30% dividend rate gives a **derived** combined rate of 46.1% before surtax: 0.23 + 0.77 x 0.30. A 25% shareholder rate gives 42.25%, derived. These figures compare one unit of **pre-company-tax profit**, not a fixed amount of cash already available to distribute ([ITO ss.125B,126](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)). The old approximate salary 55%-60%, fee 50%-55% and dividend “up to 52%” ranges are not a reliable decision rule.

Use both s.121B bases from the annual-return skill. Ordinary dividends are capital-source income under that definition, but the additional charge applies only to the separately measured excess capital-source base. A general threshold crossing does not add 5% to the whole dividend. Do not present “NIS 200,000 / NIS 500,000” extraction bands or “salary to the 20% bracket” as universal optimal levels.

### Working-age controlling-shareholder payroll contributions

The National Insurance page's column 2 covers a controlling shareholder in a closely held company who holds at least 10% of shares or a director-appointment right, aged 18 to before retirement. This classification is not interchangeable with every tax-law definition of control. Special age/residence/pension cases need the relevant column.

| Monthly wage slice (NIS) | Employee total NI plus health | Employer NI | Official source |
|---|---|---|---|
| Up to 7,703 | 4.25% | 4.46% | National Insurance column 2, 2026 band, https://www.btl.gov.il/Insurance/Rates/Pages/%D7%9C%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D%20%D7%A9%D7%9B%D7%99%D7%A8%D7%99%D7%9D.aspx |
| Above 7,703 to maximum 51,910 | 11.96% | 7.38% | same |
| Above maximum 51,910 | No further contributions on that excess (derived from maximum) | No further contributions on that excess | same |

The page also gives ordinary resident employee employer rates of 4.51%/7.60%, and employee totals of 4.27%/12.17%, in column 1. Use the correct class, not the old table's attempt to infer a shareholder NI/health split from ordinary employee components. Apply the annual/monthly basis and employment facts correctly before a full extraction comparison. Salary-related benefits require eligibility and statutory caps; they do not establish an automatic “minimum salary before dividends.”

### Shareholder loan: benefit tax and withdrawal tax

Under s.3(i), a below-prescribed-interest loan benefit can be employment income if linked to employment, business income if linked to service provision, or s.2(4) income for the residual controlling-shareholder branch. It is **not automatically salary**. Section 3(i) has its own controlling-person definition: holds or is entitled to acquire at least 5% of issued shares, votes, profits or liquidation assets, or a director-appointment right, directly/indirectly alone/with a relative. This differs from s.88 material holding and NI control. The service-provider limb excludes a loan proved unrelated to the services; international loans under s.85A and residual corporate borrowers other than the statutory family/transparent-company exceptions need separate treatment. Prescribed 6.53% interest is a benefit-valuation input; the booklet's NIS 8,640 CPI-linked loan ceiling has its specific s.3(i) context and is not a shareholder withdrawal safe harbour ([ITO s.3(i)](https://www.btl.gov.il/Laws1/00_0103_000000.pdf); [2026 booklet p.15](https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf)).

Section 3(i1), separately, covers qualifying material-shareholder/relative company withdrawals and private asset use. The definition excludes non-transparent corporate shareholders and already fully taxed withdrawals/use. Its asset definition is specific: mainly private-use dwelling/content, art/jewellery, mainly private-use aircraft/vessel or prescribed assets, not every private item. Clause (9) separately excludes indirect-withdrawal treatment for a genuine economic-purpose loan to another non-transparent company, with the defined transparent-company exception. Refer corporate-borrower, indirect-loan and asset-definition cases before using the individual outline. For money, the charge date is generally the end of the tax year following withdrawal; for assets, year-end of first use and each following year until returned. The cumulative-money exclusion tests whether withdrawals exceeded NIS 100,000 at any time in the tax year or preceding year (amount expressed in words in statute), not whether a chosen year-end balance is below that figure. Money repayments/reborrowings within 2 years and asset reuse within 3 years have anti-recycling rules; the money exception concerns a one-off redraw returned within 60 days. A credited balance repaid within 18 months from its deduction date is recaptured up to that repayment. The money bank-loan deduction requires a bank loan for at least 2 years, passed to the shareholder within 60 days, with the shareholder bearing all costs and no company security. The apartment deduction requires a bank balance secured by a fixed security/mortgage on that same apartment for at least 3 years. These deductions have the full statutory timing and balance conditions ([ITO s.3(i1)(1)-(9)](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

At the charge date, the statutory order is dividend to the extent the company has the relevant profits/share, otherwise employment income where an employment relationship exists, otherwise business/professional income. Section 3(i) can apply until the money charge date. For private asset use, s.3(i1)(7) also imposes ongoing income until return: the higher of market use value or prescribed rate times asset cost, less actual use payments. Do not mistake the annual principal/use charge dates for the only liability. The old claim that paying annual interest lets a loan defer extraction tax indefinitely is withdrawn. A signed loan agreement, repayment schedule, documented purpose and bank evidence remain necessary working-paper inputs, not a guarantee against reclassification.

The old “short term under 12 months” bridge suggestion is not the statutory charge-date test. Model actual dates, repayment, redraw and tax classification before selecting a loan. Principal, interest benefit and shareholder tax cannot be compared with a pre-tax-profit dividend without adjusting the bases.

### Management fees

Document the genuine service, recipient business/entity, agreement, invoicing, business purpose and amount; review s.18(b) closely held-company deduction timing separately from an invoice or accrual. A shareholder's invoice does not by itself make the company deduction valid or the receipt capital income. For a genuine self-employed recipient, load the freelancer and VAT skills; for a recipient company use its own taxable-income rules. Review arm's-length pricing and related-party characterization. Section 85A concerns an **international** related-party transaction and is not a universal domestic management-fee citation ([ITO s.85A](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)). Excessive or unsupported fees, artificial structures and disguised distributions require specialist review.

### Closely held undistributed-profit regime

The old shorthand “2% unless 6% distributed” omitted the statutory base and alternative exceptions. The 2% addition applies to **excess profits** under s.81C, after subtraction of the year's dividend, rather than all accounting retained earnings. The defined base has excluded profits and protective amounts. Do not compute it without the full s.81A/s.81C asset, expense, ownership and profit schedules.

| Exception test for the year | Condition | Official source |
|---|---|---|
| Losses | Qualifying ss.28/29/92 losses exceed 10% of previous year-end accumulated profits | ITO s.81B(b)(1), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Distribution alternative | Tax-paid dividends exceed 50% of previous year-end excess profits | ITO s.81B(b)(2), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Distribution alternative | Tax-paid dividends are at least 6% of previous year-end accumulated profits | ITO s.81B(b)(3), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

The s.81B(b) definition of tax-paid dividends excludes a s.126(b) exempt intercompany dividend unless the distributing company elects the specified highest s.125B plus s.121B tax under the regulations; simply moving cash between companies may not qualify. Section 81C compares the defined prior-year-end taxable accumulated-profit amount with the largest statutory protective amount, including a NIS 750,000 amount with common-control allocation rules (amount expressed as 750 thousand in the statute), an expense-based amount and the defined asset-based amount. These are **not additive**. Section 81C(c) has a separate branch where exempt accumulated profits are elected under paragraph (1) of the s.81A definition: compare only the NIS 750,000 and expense protective amounts, excluding the asset protective amount. A complete base and anti-avoidance computation is outside this extraction outline; preserve the regime as an explicit review item, not a reason to automatically pay a dividend.

## Worked cases

### Equal pre-tax company profit: dividend versus salary before payroll costs

Assume ordinary pre-tax profit/cost budget of NIS 100,000, an individual qualifying for the 30% dividend rate, no surtax and no special regime. Company tax NIS 23,000 leaves NIS 77,000; shareholder tax NIS 23,100 leaves NIS 53,900, combined NIS 46,100. If an **entire deductible salary slice** is in the 35% band, its net **before NI, employer costs and pension** is NIS 65,000; at 47% it is NIS 53,000. The NIS 11,100 or NIS -900 difference is not a final extraction recommendation: recompute the full salary cost and eligible reliefs. The salary slices are alternative assumed cases, not simultaneous rates on the same person's entire income.

```oa-check
name: Same pre-tax budget dividend versus salary slices
inputs:
  budget: 100000
steps:
  - company_tax: budget*0.23
  - dividend: budget-company_tax
  - shareholder_tax: dividend*0.30
  - dividend_net: dividend-shareholder_tax
  - combined_tax: company_tax+shareholder_tax
  - salary_net_35_before_payroll: budget*(1-0.35)
  - salary_net_47_before_payroll: budget*(1-0.47)
  - difference_35: salary_net_35_before_payroll-dividend_net
  - difference_47: salary_net_47_before_payroll-dividend_net
expected:
  company_tax: 23000
  dividend: 77000
  shareholder_tax: 23100
  dividend_net: 53900
  combined_tax: 46100
  difference_35: 11100
  difference_47: -900
```

### Loan benefit does not settle principal taxation

Retain NIS 500,000 outstanding for an assumed whole year, no interest paid and applicable 6.53% s.3(i) rate. Benefit is NIS 32,650. If the correctly classified incremental benefit is wholly taxed at an assumed 47% marginal rate, tax is NIS 15,345.50 (NIS 15,346 only when rounded to the nearest shekel). This does not calculate the separate s.3(i1) withdrawal charge, contributions or surtax. The old NIS 230,500 dividend comparison used NIS 500,000 **pre-tax profit**, giving NIS 269,500 net; it was not tax on a NIS 500,000 distributable cash dividend. Never compare those unmatched bases.

```oa-check
name: Interest benefit and separate dividend base
inputs:
  principal: 500000
steps:
  - benefit: principal*0.0653
  - assumed_benefit_tax: benefit*0.47
  - tax_on_pretax_profit: principal*(0.23+0.77*0.30)
  - net_from_pretax_profit: principal-tax_on_pretax_profit
expected:
  benefit: 32650
  assumed_benefit_tax: 15345.50
  tax_on_pretax_profit: 230500
  net_from_pretax_profit: 269500
```

## When to refuse or refer

Refer uncertain control/residence, related-party services, s.62A attribution, s.81 excess profits, foreign/intercompany dividends, shareholder withdrawals/private assets, special NI classes, distributions without company-law approval, and unsupported pension/study-fund benefits. Do not promise an optimal method from one tax rate or assume a NIS 6,500 monthly salary floor.

## Filing and payment

Prepare the company return (Form 1214), shareholder annual return, actual payroll/withholding returns and supporting extraction schedule as applicable. Reconcile company tax, dividend withholding and shareholder surtax; document board/company-law approval separately. Form 126/856 treatment and deposit dates depend on the actual receipt/reporting regime; the old universal 15th/April 30 claims are not asserted here. Confirm current forms, deadlines and professional authorization before filing.

## Completion checklist

Confirm ownership/holding period and company regime; separate tax profit, distributable profit and cash; compare equal cost bases; apply actual payroll/pension/NI; compute both surtax bases; reconcile loans/withdrawal dates and related-party contracts; screen s.62A/s.81; obtain company-law and CPA review; document return/payment requirements.

## Sources

| Source | URL | Read on |
|---|---|---|
| Consolidated Income Tax Ordinance; Read for s.3(i),(i1) classification, timing, exclusions and repayment rules; s.88 material holder; ss.125B/126 dividend/company rate; ss.81B-81C base/exceptions and s.85A international scope | https://www.btl.gov.il/Laws1/00_0103_000000.pdf | 2026-11-14 |
| ITA 2026 deduction booklet; Read for p.15 prescribed s.3(i) rate and CPI-linked loan ceiling, not an extraction safe harbour | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf | 2026-11-14 |
| National Insurance employee page; Read for column 2 working-age controlling-shareholder definition, contribution totals, employer rates, 2026 band/maximum and column 1 comparison | https://www.btl.gov.il/Insurance/Rates/Pages/%D7%9C%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D%20%D7%A9%D7%9B%D7%99%D7%A8%D7%99%D7%9D.aspx | 2026-11-14 |

Not yet confirmed: full s.62A attribution and s.81 excess-profit/asset/expense/profit exclusions computation; s.3(j) prescribed rate (old 4.9% not retained as instruction); exact benefit-reporting fields, Forms 126/856 and withholding/deposit dates; company-law distribution/solvency approval requirements and pension/study-fund relief limits. The old NIS 6,500 salary expectation, NIS 200,000/NIS 500,000 optimal-extraction bands, 55%-60%/50%-55% effective ranges and dividend up-to-52% shortcut are unsupported. The old shareholder NI/health component split should not be inferred from ordinary employee figures. Self-employed 52% NI deduction and contribution rates have their home in the freelancer skill. No loan interest-only strategy is represented as an exemption from principal withdrawal tax.
