---
name: ml-income-tax
description: >
  Mali wage income tax research draft for 2026, reconstructing the older DGI Impôt sur les Traitements et Salaires provisions without claiming an operative 2026 amendment chain. Use it for conditional annual ITS workpapers covering employment income, residence and source, pension deductions, annual progressive bands, family reductions and reconciliation of amounts withheld, with final ITS held where the neighbouring relief formula is unresolved. It corrects the former Guide's unsupported flat non-resident rate and distinguishes a housing-lease residence condition from a universal day-count test. The DGI's August 2025 bulletin clarifies a disputed 2024 table but does not prove later continuity. This draft includes two executable annual cases. Other personal income categories, current payroll conversion rules, forms and treaty procedures remain outside verified coverage.
jurisdiction: ML
category: international
tax_year: 2026
tax_year_notes: "2026 research draft only; older DGI source baseline, operative 2026 amendment chain unproved."
version: 0.1
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mali wage income tax source-reference draft v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research draft; operative 2026 law is unproved.** This is a conditional source-reference workpaper, not an approved current-law computation. The DGI online consolidation contains amendments labelled through 2017 in the provisions used here. No complete later amendment chain or enacted 2026 fiscal Annex U has been reconciled. Read every rule below as a statement of that identified source baseline, not proof it applies unchanged in 2025 or 2026. Do not calculate a client's 2026 liability or instruct a 2026 filing from this draft. The current-year metadata identifies the research job; it is not evidence of currentness or a technical retrieval/publication safeguard.

## Who this applies to

This job covers ITS on remuneration paid in exchange for or in connection with employment, including bonuses and other forms of remuneration; article 2 also includes pensions, annuities and specified management remuneration. It is not a comprehensive personal-income code: business profit, property income, investment income and capital gains have separate chapters. [CGI arts. 1–5, 15 onwards, 43](https://www.dgi.gouv.ml/CGI/).

In the older article 4, ordinary residence and work/source conditions matter regardless of nationality. A person habitually resident in Mali can remain within ITS where work or employer is abroad. A non-resident's specified condition is both work exercised in Mali and employer/payer established there, subject to the treaty clause. Do not substitute a general flat non-resident percentage. [CGI art. 4](https://www.dgi.gouv.ml/CGI/).

The article's 183-day wording concerns the period of rented housing made available under one or successive leases. It is not a universal 183-days-physically-present test. Ownership/usufruct housing and, without qualifying housing, principal stay are separate limbs. Apply the full text to the facts and any actual treaty. [CGI art. 4(II)(1)–(2)](https://www.dgi.gouv.ml/CGI/).

## Rates, bands and thresholds

All amounts are annual XOF taxable-income slices in article 10 as enacted by Loi 2016-010 of 19 April 2016, effective from 1 July 2015. The complete amending law and table were read in official gazette pages 723–724 (PDF pages 3–4), corroborating the older DGI consolidation. They are source-baseline figures, not an approved 2026 grid. [CGI arts. 9–10](https://www.dgi.gouv.ml/CGI/).

| Item | Older source amount/rule | Official source |
|---|---|---|
| First annual slice | XOF 0–330,000 at 0% | [CGI art. 10](https://www.dgi.gouv.ml/CGI/) |
| Second slice | XOF 330,001–578,400 at 5% | [CGI art. 10](https://www.dgi.gouv.ml/CGI/) |
| Third slice | XOF 578,401–1,176,400 at 12% | [CGI art. 10](https://www.dgi.gouv.ml/CGI/) |
| Fourth slice | XOF 1,176,401–1,789,733 at 18% | [CGI art. 10](https://www.dgi.gouv.ml/CGI/) |
| Fifth slice | XOF 1,789,734–2,384,195 at 26% | [CGI art. 10](https://www.dgi.gouv.ml/CGI/) |
| Sixth slice | XOF 2,384,196–3,494,130 at 31% | [CGI art. 10](https://www.dgi.gouv.ml/CGI/) |
| Top slice | Above XOF 3,494,130 at 37% | [CGI art. 10](https://www.dgi.gouv.ml/CGI/) |
| Pension/retirement withholding deduction | Ordinary ceiling 4% of gross wages, with special statutory-domain exceptions | [CGI art. 7(a)](https://www.dgi.gouv.ml/CGI/) |
| Family reduction of gross tax | Single/divorced/widowed without dependants: 0%; married without children: 10%; 2.5% per dependent child through the tenth; adult disabled child gives 10% | [CGI arts. 11–12](https://www.dgi.gouv.ml/CGI/) |
| Neighbouring two-point relief | Arts. 12-A–12-B describe a two-percentage-point reduction, but the online multiplication wording is unresolved; no final ITS calculation is certified | [CGI arts. 12-A–12-B, Loi 2008-002](https://www.dgi.gouv.ml/CGI/) |
| Withholding base rounding | Net taxable income rounded down to XOF 1,000 | [LPF art. 410](https://www.dgi.gouv.ml/CGI/) |

The DGI's August 2025 bulletin says article 10 remained unchanged for 2024 and that a different grid printed in the finance law's tax-expenditure annex was a material error. That statement resolves what the DGI said about 2024; neither the bulletin nor the older consolidation establishes an unchanged 2026 grid. [Impôt COM no. 38, p. 36, reply to letter 1](https://www.dgi.gouv.ml/wp-content/uploads/2025/12/IMPOT_COM-38.pdf#page=36).

## The base

1. Establish wage category, residence and the relevant work/payer facts, then total taxable cash and benefits for the period. Evidence, rather than a blanket exclusion for allowances, determines whether an amount is exempt or deductible. Articles 3 and 5–8 and their embedded implementing orders address the exceptions and valuation. Complex benefits and expatriate allowances need the actual applicable instruments and their later amendments before a client calculation. [CGI arts. 1–8](https://www.dgi.gouv.ml/CGI/).
2. Deduct evidenced pension/retirement withholding within article 7(a)'s ordinary ceiling or the proved special statutory ceiling. The former statement that all employee social/AMO contributions are deductible is not established by that wording. Do not deduct AMO automatically from ITS merely because it is an employee contribution. Contribution calculations belong in [payroll/social](ml-payroll-social.md). [CGI art. 7](https://www.dgi.gouv.ml/CGI/).
3. Use the source's annual bands progressively: each rate applies only to its slice. For computational continuity, the second slice has width 578,400 minus 330,000; do not subtract the printed first whole-franc value and lose one franc per band. Round the taxable base as prescribed for withholding. [CGI arts. 9–10; LPF art. 410](https://www.dgi.gouv.ml/CGI/).
4. Apply family reductions to gross tax, not to income. Establish qualifying children under article 12, their separate income, studies/disability/adoption facts and the situation at 1 January. Married spouses can request allocation of their global child reduction without changing its total; do not duplicate child relief. The adult-disabled-child case and adoption limits need the exact statutory conditions, not a generic dependant count. [CGI arts. 11–12](https://www.dgi.gouv.ml/CGI/).
5. **Stop before final ITS:** the adjacent articles 12-A–12-B describe a further two-percentage-point relief. The online article 12-B says to multiply the amount of assessed tax by the reduced effective rate, although its denominator is annual taxable income. That wording does not establish the intended final multiplication base. Do not silently interpret, omit or apply that step. The 2016 amending law changes articles 9–10 only; it does not resolve the article 12-B wording. The cases below end at the supported articles 9–11 subtotal. Obtain the operative primary text/correction before calculating final annual ITS. [CGI arts. 12-A–12-B](https://www.dgi.gouv.ml/CGI/); [Loi 2016-010, article unique](https://sgg-mali.ml/JO/2016/mali-jo-2016-19.pdf#page=3).
6. Once the final legal computation is resolved, reconcile the annual total with actual ITS withheld. The older LPF treats insufficient withholding as payments on account and provides a tax-credit certificate/excess-credit mechanism. Do not invent an automatic cash refund or net a credit without the required evidence. [LPF arts. 29–35, 418](https://www.dgi.gouv.ml/CGI/).

## Deadlines and filing

The source requires employer annual wage summaries in January for the previous year. It specifically requires an annual declaration for multiple-employer employees and information from Mali-domiciled recipients of foreign-employer wages. The old Guide's universal individual 31 March deadline is not supported by these provisions. [LPF arts. 29–35](https://www.dgi.gouv.ml/CGI/).

Monthly ITS is collected at payment by a Mali employer; a Mali-domiciled employee receiving taxable amounts from an employer abroad must calculate and pay under the source's self-payment rule. Employer remittance timing, the small-retention exception, payslips and annual certificates are explained in [payroll/social](ml-payroll-social.md). [LPF arts. 410–418](https://www.dgi.gouv.ml/CGI/).

Prepare a wage/benefit reconciliation, legal deduction schedule, annual band calculation, documented family reduction, and comparison to withholding certificates. Obtain the prescribed current declaration and filing route; map these working-paper amounts to its actual fields, then retain declaration, acknowledgement and payment/credit certificate. Current form identifiers, payroll conversion tables and authenticated filing steps are unverified. The annual worked cases below do not prescribe dividing annual tax to operate a particular month's payroll.

## Penalties and interest

The older LPF distinguishes failure to declare withheld amounts (article 36), understatement of required withholding (article 37), failure to retain/present payroll records (article 38), and incorrect annual employee information (article 39). It also separates failure to withhold, incorrect remittance and late payment in articles 419–421. These are distinct fact patterns; the employer controls are set out in [payroll/social](ml-payroll-social.md). No blanket penalty total is computed here. [LPF arts. 36–39, 419–421](https://www.dgi.gouv.ml/CGI/).

## Cross-border points

Apply article 4's domestic and treaty conditions before using any band, then determine who must withhold or self-pay under LPF article 411. A foreign employer does not by itself remove a Mali-resident employee from the source's charge. The former flat non-resident employment rate was unsupported; the 30% rate in the non-permanent-establishment business-payment chapter is not automatically a wage tax. Treaty status, government service and foreign-tax relief remain case-specific unverified jobs. [CGI arts. 4, 13, 94–98; LPF arts. 34, 411–412](https://www.dgi.gouv.ml/CGI/).

## Two worked examples that recompute

These are conditional intermediate annual tests of articles 7 and 9–11 using the older source grid. Both stop before unresolved articles 12-A–12-B relief, final rounding and any remittance. Neither result is final annual ITS, a 2026 liability or a monthly payroll algorithm.

**Annual salary and pension deduction.** Gross cash wage XOF 1.5 million, no benefits/exemptions, pension withholding XOF 54,000, single with no qualifying child. The pension amount is within the source ceiling of XOF 60,000. Net annual taxable income is XOF 1,446,000. The intermediate articles 9–11 subtotal is XOF 132,708 using the first four slices, before the unresolved two-point relief.

```oa-check
name: Older DGI annual ITS source test, pension and bands
inputs:
  gross: 1500000
  pension: 54000
steps:
  deductible_pension: min(pension, gross * 0.04)
  taxable: floor((gross - deductible_pension) / 1000) * 1000
  band2: max(min(taxable, 578400) - 330000, 0) * 0.05
  band3: max(min(taxable, 1176400) - 578400, 0) * 0.12
  band4: max(min(taxable, 1789733) - 1176400, 0) * 0.18
  intermediate_tax: band2 + band3 + band4
expected:
  taxable: 1446000
  intermediate_tax: 132708
```

**Does documented family status change the result?** For the same supported XOF 3 million taxable annual income, compare single/no child with married/two ordinary qualifying dependent children and no spouse double claim. The article 10 band subtotal is XOF 540,039.61. The documented family case applies 15% to gross tax, reducing it by XOF 81,005.9415 to XOF 459,033.6685 before unresolved two-point relief and final official rounding. Without that evidence the single/no-child case has no reduction. This compares legal fact patterns, not an election to invent family status.

```oa-check
name: Older DGI annual ITS source test, family decision
inputs:
  taxable: 3000000
steps:
  band2: (578400 - 330000) * 0.05
  band3: (1176400 - 578400) * 0.12
  band4: (1789733 - 1176400) * 0.18
  band5: (2384195 - 1789733) * 0.26
  band6: (taxable - 2384195) * 0.31
  gross_tax: band2 + band3 + band4 + band5 + band6
  family_rate: 0.10 + 2 * 0.025
  reduction: gross_tax * family_rate
  family_subtotal: gross_tax - reduction
expected:
  gross_tax: 540039.61
  reduction: 81005.9415
  family_subtotal: 459033.6685
```

## Ask the client first

- Is this employment/pension income, business profit or another income category, and for which year?
- What housing, principal-stay, work-location and employer/payer facts establish residence and source; is a treaty claimed?
- What cash, benefits, reimbursements and pension deductions are supported by documents?
- What were marital/child facts at 1 January, and has another spouse claimed the same child reduction?
- Were there multiple employers or an overseas employer, and what ITS was actually withheld/paid?
- Has the complete operative amendment chain and current declaration/payroll method been obtained?

## Sources

| Source and actual scope | URL | Read on |
|---|---|---|
| DGI, CGI and LPF online consolidation; exact articles cited above and their neighbouring provisions, older amendment labels through 2017; not a 2026 consolidation | https://www.dgi.gouv.ml/CGI/ | 2026-11-01; selected chapters read offline, not the entire code |
| Loi 2016-010, article unique; complete law and new arts. 9–10 including table, official gazette pp. 723–724 | https://sgg-mali.ml/JO/2016/mali-jo-2016-19.pdf#page=3 | 2026-11-01; PDF pp. 3–4 read; no later continuation inferred |
| DGI, Impôt COM no. 38, August 2025, p. 36; complete reply to letter 1 about article 10 and the erroneous 2024 finance-law tax-expenditure grid | https://www.dgi.gouv.ml/wp-content/uploads/2025/12/IMPOT_COM-38.pdf#page=36 | 2026-11-01; this reply read, not the whole issue |

Not yet confirmed: complete later amendment chain and enacted 2026 Annex U; operative 2026 ITS grid, family/deduction rules and forms; current monthly payroll conversion and final rounding; primary resolution of the article 12-B multiplication wording and complete two-point-relief amendment chain; AMO deductibility for ITS; expatriate/benefit implementing amendments; treaties, foreign-tax relief and other individual income categories. The August 2025 reply confirms a 2024 issue only. No 2025/2026 continuity, current-year approval or accountant attestation is claimed.

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
