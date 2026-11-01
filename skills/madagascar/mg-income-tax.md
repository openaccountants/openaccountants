---
name: mg-income-tax
description: "Madagascar 2026 monthly salary IRSA computation including new top band, taxable benefits, dependent relief and foreign-employer payment; partial personal-tax scope."
jurisdiction: MG
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Madagascar personal income tax: ordinary salary IRSA

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Madagascar.

## Who this applies to

Use for ordinary employment income and assimilated remuneration under CDI 01.03.02, including public/private, temporary and occasional work, bonuses and taxable allowances. A tax resident is covered on salary income regardless of origin; a non-resident is covered on Malagasy-source salary income, subject to treaties (01.03.04–05). Residence uses the tests in 01.01.05, including principal stay of 183 cumulative days in twelve months, principal professional activity or economic-interest centre. Majority SARL manager remuneration is excluded from IRSA by 01.03.03 6° and routes to IR. Non-salary business income routes to [business regimes](mg-corporate-income-tax.md). [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Rates, bands and thresholds

| Ordinary monthly taxable tranche / condition | 2026 rate / amount | Official source |
|---|---|---|
| Up to MGA 350,000 | 0% marginal rate | [CDI 01.03.16 A](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |
| Above MGA 350,000 through 400,000 | 5% | same |
| Above MGA 400,000 through 500,000 | 10% | same |
| Above MGA 500,000 through 600,000 | 15% | same |
| Above MGA 600,000 through 4,000,000 | 20% | same |
| Above MGA 4,000,000 | 25% | same |
| Monthly base rounding | Down to MGA 100 | same |
| Minimum ordinary monthly tax | MGA 3,000, including a base in the zero-rate tranche | same |
| Eligible dependant; taxable base above MGA 350,000 | MGA 2,000 monthly tax reduction, never below minimum | [CDI 01.03.19](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |

Apply marginal rates, not the top rate to the whole salary. The old Guide’s 20% maximum is replaced by the 2026 top band. Dependant relief is a tax reduction, not a deduction from salary. The child/ancestor must lack separate income: direct descendants and spouse’s descendants including adopted children under 21 on 1 January, disabled descendants, or students under 25; direct ancestors of either spouse without resources. Relief goes to the spouse receiving family allowances (01.03.19).

## The base

1. Reconcile pay, bonuses and taxable allowances plus benefits and any employee tax borne by the employer (01.03.07).
2. Value mixed-use employer car at 15% of actual monthly insurance, fuel, maintenance and repair costs; housing at 50% actual rent (or statutory monthly rental value), capped at 25% fixed cash pay; phone at 15% actual monthly employer cost. Other benefits use full actual value. Subtract employee reimbursements only up to that benefit’s value (01.03.08).
3. Deduct qualifying pension/retirement withholdings up to 10% of the relevant gross remuneration and qualifying employee health contributions up to 2% gross salary; apply the statutory conditions. Prior-year obligatory maintenance/annuities require a request before 1 May and the written tax-service notification; do not silently deduct them in payroll (01.03.09,11).
4. Remove only an identified 01.03.03 exemption. The retirement indemnity exemption stops at one year’s salary; overtime exemption is limited to 20 hours and implementing conditions. Do not extrapolate these to all severance or bonuses.
5. Round base, sum marginal tax, then apply evidenced dependant reductions and the minimum. [CDI 01.03.03,07–11,16,19](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Deadlines and filing

Employer withholding occurs at payment (CPF I-20–21). The employer declares and pays within the first fifteen days of the following month using the prescribed form and an employee-by-employee statement regardless of each salary amount (I-23). [Payroll operations](mg-payroll-social.md) handles permitted frequency exceptions. With a foreign employer, the taxpayer calculates and pays directly or through an accredited resident representative, attaching payslip/supporting evidence (I-22,25). Multiple payers each withhold provisionally; the authority calculates final withholding. Declare monthly income by payer before 15 January and a change within fifteen days (I-24; CDI 01.03.13). [CPF](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf). Portal boxes and payment-reference instructions remain unverified; obtain the current prescribed form before filing.

## Penalties and interest

Failure to withhold salary tax exposes the payer to 40% of omitted tax, in addition to the tax; withholding that is collected but not paid over attracts 80% of those sums (CDI 20.01.54.1). Late-remittance penalties under 20.01.53 attach to the employer under CPF I-20; use the payer’s applicable band in [corporate/business penalties](mg-corporate-income-tax.md). An overpayment caused by payer error can be credited against subsequent payments within six months after the error month; otherwise a tax-service certificate supports Treasury refund (CDI 01.03.15). [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf); [CPF](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf).

## Cross-border points

Foreign payment does not remove resident IRSA. Employment performed in Madagascar, pay from an employer in Madagascar and resident worldwide salary are addressed by 01.03.04. Apply an actual treaty to the worker’s residence and employment facts before relief. Self-payment for a foreign employer is an express rule, not an optional omission from payroll. [CDI 01.03.04–05](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf); [CPF I-22](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf).

## Two worked examples that recompute

Hypothetical monthly bases already reconciled for permitted deductions and exemptions. First, a high earner demonstrates the new top band.

```oa-check
name: IRSA above new top-band threshold
inputs:
  base: 5000099
  dependants: 2
steps:
  - rounded: floor(base / 100) * 100
  - tax_before_relief: 50000 * 0.05 + 100000 * 0.10 + 100000 * 0.15 + 3400000 * 0.20 + (rounded - 4000000) * 0.25
  - tax: max(3000, tax_before_relief - dependants * 2000)
expected:
  rounded: 5000000
  tax_before_relief: 957500
  tax: 953500
```

Second, the minimum remains payable even when a marginal tranche is zero.

```oa-check
name: Zero tranche still has statutory minimum
inputs:
  base: 300099
steps:
  - rounded: floor(base / 100) * 100
  - marginal_tax: rounded * 0
  - tax: max(3000, marginal_tax)
expected:
  rounded: 300000
  tax: 3000
```

## Ask the client first

Get residence and workday facts, each payer’s location, payslips and payment dates, fixed and variable cash pay, benefit costs and reimbursements, pension/health deductions and approval evidence, family details and the spouse receiving allowances, overtime/severance records, other employers and tax-service notifications. Ask separately about business, rent, investment and disposal income.

## Sources

 | Source and provisions actually read | Read on |
|---|---|
| [DGI 2026 CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), 01.01.05; 01.03.01–19; 20.01.54.1 | 2026-11-01 |
| [DGI 2026 CPF](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf), I-20–25 | 2026-11-01 |

| [Signed Loi 2026-004, LFR 2026](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf), tax amendments and article 22 entry provision read | 2026-11-01 |

**Not yet confirmed:** Exact radio/posted publication date activating the July LFR under article 22; do not resolve a transaction at that transition without the publication evidence. special exceptional/unit-rate remuneration list under 01.03.16 B; implementing canteen/overtime limits; non-salary personal regimes beyond the business router; current forms/portal boxes. The old blanket 31 March business-return date is not established and is not a salary deadline.

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
