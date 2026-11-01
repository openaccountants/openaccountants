---
name: bj-income-tax
description: "Prepare a monthly Benin salary income-tax working paper for 2026 under the ITS chapter. Use this Guide to establish salary-tax scope and residence conditions, identify the supported taxable-pay inputs, apply monthly bands and distinguish the separate March and June levies. It also identifies employer declarations and the special foreign-payer reporting route. Two executable salary examples recompute ordinary and additional tax. Complete benefit valuation, exceptional pay, nonsalary personal income and unsupported legacy deductions remain outside the verified calculation scope. The output is a payroll tax schedule, not an authenticated filing or accountant attestation. Trigger phrases include Benin ITS, salary tax, monthly payroll bands and foreign employer."
jurisdiction: BJ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.2
---

# Benin monthly salary ITS working paper v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Calculate a monthly Benin salary-tax (ITS) working paper in 2026. This replaces the legacy generic IRPP description with the actual salary-tax chapter; business, investment and property income need their own tax classification. Salary and company-manager remuneration within article 119 enter this job. [CGI 2026, art. 54](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=34) [CGI 2026, art. 119](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=60)

Salary is taxable where the recipient is domiciled in Benin even if the work or employer is abroad; for a non-domiciled recipient, Benin activity or a Benin-established employer is the statutory connecting factor. Article 121 tests permanent home, then vital interests, then habitual presence of at least 183 days in a twelve-month period under its fallback conditions. Check treaty facts separately before a cross-border result. [CGI 2026, art. 121](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=60)

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| Monthly taxable salary up to FCFA 60,000 | 0% | [CGI 2026, art. 125](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62) |
| Slice FCFA 60,001–150,000 | 10% | [CGI 2026, art. 125](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62) |
| Slice FCFA 150,001–250,000 | 15% | [CGI 2026, art. 125](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62) |
| Slice FCFA 250,001–500,000 | 19% | [CGI 2026, art. 125](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62) |
| Slice over FCFA 500,000 | 30% | [CGI 2026, art. 125](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62) |
| ORTB levy, March salary | Add FCFA 1,000 | [CGI 2026, art. 125](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62) |
| ORTB levy, June salary | Add FCFA 3,000; exempt from this June levy where taxable income does not exceed the first band | [CGI 2026, art. 125](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62) |

## The base

1. Reconcile monthly gross salary, overtime, bonuses and cash/benefit allowances, including transport, to the taxable components under article 122. Illness indemnities are included. [CGI 2026, art. 122](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=61)
2. Screen the actual exemptions in article 120 and exclusions in article 124. Statutory dismissal compensation is distinguished from taxable notice/leave compensation. Family social-security-type allowances have the article 120 cap condition; this is not a family-quotient deduction. Training and collective health insurance have their stated exclusions, and individual health cover has its own limit. Hold any exemption whose factual limit has not been evidenced. [CGI 2026, art. 120](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=60) [CGI 2026, art. 124](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62)
3. Value benefits under article 123: actual value is the starting rule and the listed housing, domestic help, utilities, food and vehicles have statutory monthly valuations. Obtain the employee category, base salary and benefit details before applying that table. This Guide does not compute a benefit value from missing facts. [CGI 2026, art. 123](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=61)
4. Apply each band only to its slice of the resulting monthly base, then add the March/June levy when required. Do not multiply the monthly thresholds by twelve and apply them as a general personal annual scale. [CGI 2026, art. 122](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=61) [CGI 2026, art. 125](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=62)
5. Separate exceptional remuneration, including end-of-career amounts and thirteenth-month pay. Article 126 uses an average-salary method and special conditions; do not put an unresolved exceptional payment through the ordinary examples. [CGI 2026, art. 126](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=63)

## Deadlines and filing

The payer withholds when salary is paid and records each beneficiary, amount, date, nature of withholding and receipt reference. Put the tax on the payslip. Remit the monthly deductions by the 10th of the following month with the prescribed monthly declaration. [CGI 2026, art. 127](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=63) [CGI 2026, art. 128](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=64) [CGI 2026, art. 129](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=64)

A Benin-domiciled taxpayer paid by a foreign-established payer must make a spontaneous monthly salary declaration and payment on the same terms. The salary withholding is final under article 128(3); it is not a universal annual IRPP return for all income. An annual salary information statement remains due by 30 April under article 472, including its specified foreign-payer cases. [CGI 2026, art. 128](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=64) [CGI 2026, art. 472](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=204)

Prepare the payroll and monthly/annual summaries for the authorised filer. Authenticated DGI form fields, submission and payment acknowledgements were not accessed; this is not a completed payroll filing.

## Penalties and interest

General filing/payment sanctions and the conditional 2026 first-declaration relief are recorded once in the [overview](bj-tax-overview.md#penalties-and-interest). Assess the facts before using any relief. This working paper does not prepare a penalty assessment.

## Cross-border points

Record residence, work location, payer location and any treaty before accepting foreign payroll treatment. Foreign employment does not by itself remove a Benin-domiciled recipient from article 121. The company and foreign-service withholding rules are separate in the [cross-border Guide](bj-cross-border-withholding.md). [CGI 2026, art. 121](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=60) [CGI 2026, art. 128](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=64)

## Two worked examples that recompute

**Ordinary month.** Assume the taxable salary base, after evidenced statutory treatment, is FCFA 200,000 in an ordinary month. The first band is untaxed, the next slice gives 9,000 and the next gives 7,500, total ITS 16,500. No March/June levy arises.

```oa-check
name: Ordinary monthly ITS
inputs:
  salary_base: 200000
steps:
  band10: max(0,min(salary_base,150000)-60000)*0.10
  band15: max(0,min(salary_base,250000)-150000)*0.15
  band19: max(0,min(salary_base,500000)-250000)*0.19
  band30: max(0,salary_base-500000)*0.30
  its: band10+band15+band19+band30
expected:
  its: 16500
```

**June levy changes the amount.** A confirmed taxable base of FCFA 600,000 gives band tax of 101,500. It is above the first band, so the June levy adds 3,000. The withholding schedule totals 104,500. This example has no exceptional remuneration.

```oa-check
name: June ITS and levy
inputs:
  salary_base: 600000
steps:
  band10: max(0,min(salary_base,150000)-60000)*0.10
  band15: max(0,min(salary_base,250000)-150000)*0.15
  band19: max(0,min(salary_base,500000)-250000)*0.19
  band30: max(0,salary_base-500000)*0.30
  band_tax: band10+band15+band19+band30
  tax_plus_june_levy: band_tax+3000
expected:
  band_tax: 101500
  tax_plus_june_levy: 104500
```

## Ask the client first

- Which month, payment date and type of remuneration are being processed?
- Where are the worker, work and payer located, and what residence/treaty evidence exists?
- What cash pay, benefits, employee category and base salary are documented?
- Which statutory exemptions/exclusions and their limits are supported?
- Is any amount exceptional remuneration, and is the required salary history available?
- Are there foreign payers, previous withholding, payslips and annual salary-statement obligations?

## Sources

| Official source | What was actually read | Read on |
|---|---|---|
| [DGI official CGI, 2026 edition](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf) | Articles 54, 119–129 and 472, including adjacent conditions in the extracted official text. The cover consolidates the original 2026 finance law, not the June rectifying law. | 2026-11-01 |
| [Signed law 2026-10 of 24 June 2026](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf) | Tax provisions arts. 1–19 and final arts. 48–49, PDF pages 1–6 and 17 visually read; adjacent article 20 heading read. OCR of the whole capture is not a whole-law review. | 2026-11-01 |

Not yet confirmed: application of the complete article 123 benefit table and article 126 exceptional-pay calculation to a live case; the legacy claims of a family quotient, employee-CNSS deduction and professional-expense allowance were not substantiated by the salary chapter and are not used; the legacy generic annual IRPP return/deadline outside the specific salary information statement; non-salary personal-income computations and treaty interaction; authenticated DGI portal screens, exact field identifiers and payment-confirmation workflow; later instruments not identified by the sources read; application to a particular taxpayer. Independent pack review is pending; no accountant has attested to this version.

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
