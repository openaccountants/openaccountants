---
name: bj-payroll-social
description: "Benin 2026 employer payroll tax (VPS): ordinary and private-teaching rates, salary-base link, conditional employee exemptions and monthly tax schedule. CNSS rates, ceilings and remittance remain explicit source gaps, so this does not compute complete payroll costs or net pay. Two executable VPS decisions; no accountant attestation."
jurisdiction: BJ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
version: 0.1
---

# Benin employer payroll tax VPS working paper v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Prepare the employer VPS schedule alongside the [salary ITS working paper](bj-income-tax.md). Persons paying salaries and accessory remuneration are within article 191, subject to article 192 exemptions. This Guide refreshes the tax side of payroll. It does not certify current CNSS contribution rates, ceiling, risk classification or remittance procedure: the official CNSS guidance failed to open, including in a normal browser. Do not compute a complete payroll cost or net salary while that social-security schedule is unresolved. [CGI 2026, art. 191](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) [CGI 2026, art. 192](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89)

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| Ordinary VPS | 4% of the statutory salary-tax base, paid by the employer | [CGI 2026, art. 193](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89); [CGI 2026, art. 194](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) |
| Private teaching establishments | 2% of the same base | [CGI 2026, art. 194](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) |
| New enterprise, first exercise | Exemption for employment of Beninese-national employees, subject to article 192(3) | [CGI 2026, art. 192](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) |
| Beninese employee first employment | Two-year exemption from hiring, conditional on CNSS declaration under article 192(4) | [CGI 2026, art. 192](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) |
| Other exemptions | Diplomatic/international bodies, TPS taxpayers, qualifying sport/art remuneration, qualifying trainees and domestic employees have distinct article 192 conditions; do not treat every non-profit as exempt | [CGI 2026, art. 192](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) |

## The base

1. Reconcile employee taxable salary bases to the ITS schedule. VPS has the identical base; gross payroll without statutory classification is not an automatic substitute. [CGI 2026, art. 193](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89)
2. For each line, establish the employer category and employee-specific exemption evidence. Record nationality, hiring date, first-employment evidence and CNSS declaration where article 192(3)–(4) is claimed. The domestic-employment exemption requires both CNSS declaration and payment. The sports/artists limit and trainee conditions must be established before any exclusion. [CGI 2026, art. 192](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89)
3. Split the VPS base into ordinary, private-teaching and supported-exempt lines, then apply the appropriate rate only to the taxable category. Do not deduct VPS from the employee as an ITS withholding. The legal charge is on the person paying remuneration. [CGI 2026, art. 191](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) [CGI 2026, art. 193](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) [CGI 2026, art. 194](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89)
4. Keep a separate CNSS schedule marked **not calculated** until current authoritative contribution bases, rates, risk category, ceilings and payment procedure are obtained. The old employer total omitted the separate injury-risk issue and cannot be reused as a verified all-in rate.

## Deadlines and filing

VPS is declared on the same declaration as ITS and paid on the conditions of articles 127–129, including the 10th of the following month. The annual salary information requirement is in article 472; retain employee and benefit details for it. [CGI 2026, art. 195](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89) [CGI 2026, art. 129](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=64) [CGI 2026, art. 472](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=204)

Produce the employer tax schedule, exemption evidence and monthly declaration reconciliation for the authorised DGI filer. Authenticated fields and acknowledgements were not accessed. CNSS has its own unresolved declaration/payment process; no DGI date is copied into the CNSS schedule.

## Penalties and interest

General filing/payment sanctions and the conditional 2026 first-declaration relief are recorded once in the [overview](bj-tax-overview.md#penalties-and-interest). Assess the facts before using any relief. This working paper does not prepare a penalty assessment. CNSS sanctions are unverified and are not inferred from the tax code.

## Cross-border points

Nationality matters to the specific new-company/first-employment exemptions; it is not a blanket salary-tax or social-security exclusion. Foreign employment and residence belong in the salary Guide. Do not assume that a foreign social-security certificate removes Benin CNSS obligations without the applicable instrument. [CGI 2026, art. 192](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=89)

## Two worked examples that recompute

**Ordinary employer.** Assume a checked taxable payroll base of FCFA 2 million, no exempt lines and no private-teaching status. VPS is 80,000. Employee ITS and CNSS are separate and are not calculated in this example.

```oa-check
name: Ordinary employer VPS
inputs:
  taxable_payroll_base: 2000000
steps:
  vps: taxable_payroll_base*0.04
expected:
  vps: 80000
```

**Private school with evidenced exempt lines.** A qualifying private school has total salary-tax bases of FCFA 2 million, of which 500,000 is evidenced as exempt under article 192. Apply the school rate to the remaining 1.5 million: VPS 30,000. If the exemption evidence is missing, hold the exemption decision and calculate the no-exemption comparison of 40,000; the difference is 10,000.

```oa-check
name: Private school exemption evidence decision
inputs:
  total_base: 2000000
  supported_exempt_base: 500000
steps:
  taxable_base: total_base-supported_exempt_base
  vps_with_evidence: taxable_base*0.02
  vps_without_exemption: total_base*0.02
  difference: vps_without_exemption-vps_with_evidence
expected:
  taxable_base: 1500000
  vps_with_evidence: 30000
  vps_without_exemption: 40000
  difference: 10000
```

## Ask the client first

- What is the employer type and applicable tax regime?
- Which employee salary-tax bases are already checked?
- Are any VPS exemptions claimed, and what are the nationality, hiring and first-employment facts?
- Is each CNSS registration/payment condition evidenced?
- What official current CNSS assessment, risk category, ceiling and payment instruction is available?
- What prior declarations, receipts and payroll differences need reconciliation?

## Sources

| Official source | What was actually read | Read on |
|---|---|---|
| [DGI official CGI, 2026 edition](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf) | Articles 120, 127–129, 191–195 and 472, including adjacent conditions in the extracted official text. The cover consolidates the original 2026 finance law, not the June rectifying law. | 2026-11-01 |
| [Signed law 2026-10 of 24 June 2026](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf) | Tax provisions arts. 1–19 and final arts. 48–49, PDF pages 1–6 and 17 visually read; adjacent article 20 heading read. OCR of the whole capture is not a whole-law review. | 2026-11-01 |

Not yet confirmed: current CNSS employer pension, family allowances and industrial-injury rates, employee pension rate, contribution base/ceiling and CNSS remittance deadline. These preserve all legacy social-contribution topics as unresolved, rather than presenting the old percentages as current. Official CNSS contribution guidance returned HTTP 500 and a WordPress critical-error page in the ordinary browser, so no successful read date is claimed for it; authenticated DGI portal screens, exact field identifiers and payment-confirmation workflow; later instruments not identified by the sources read; application to a particular taxpayer. Independent pack review is pending; no accountant has attested to this version.

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
