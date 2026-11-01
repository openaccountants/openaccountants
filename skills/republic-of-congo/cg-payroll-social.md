---
name: cg-payroll-social
description: "Prepare Republic of Congo payroll by distinguishing employee salary tax, employer charges, social enrolment and limited 2026 support. Salary arithmetic uses the initial 2026 ITS provisions linked from the income Guide, while unresolved social-rate conflicts remain explicit. This is a source-cited research draft for the Republic of Congo, country code CG, using fetched official law and authority material. The initial 2026 statutory baseline is distinguished from unresolved later amendments and operating procedures. Trigger phrases include Congo-Brazzaville tax, tax calculation, tax return, source verification and country compliance. It is general reference, with explicit partial coverage and no accountant attestation. Use the linked country Guides for related jobs and obtain the missing facts before calculating or filing."
jurisdiction: CG
category: payroll
tax_year: 2026
tax_year_notes: "Initial 2026 enacted-law baseline; later 2026 currentness and filing procedures remain partial"
last_updated: 2026-11-01
version: 1.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Republic of Congo Payroll and Social Contributions v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Draft scope:** Employers and employees with salary within Congo ITS. The social-security side is partial: no unverified employee/employer split, wage ceiling or contribution remittance is presented as settled. Independent pack review is pending. Initial 2026 law is not represented as a fully consolidated or operational 2026 position.

## Who this applies to

Employers and employees with salary within Congo ITS. The social-security side is partial: no unverified employee/employer split, wage ceiling or contribution remittance is presented as settled.

## Rates, bands and thresholds

| Item | Treatment | Authority |
|---|---|---|
| Linked computations | Use the owning Guide linked below; no separate headline rate is created here. | [Initial 2026 Finance Act](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf) |

## The base

Collect gross cash, benefits, applicable exemptions, employee retirement amounts actually established under the governing social law, and evidenced family parts. Use I12–I18 in [income tax](cg-income-tax.md) for ITS. An input retirement amount in an example is a fact, not a newly asserted 4% contribution rate. Compute employer-only costs separately after the P03/P04 conflict is resolved.

| Item | Rule and conditions | Authority |
|---|---|---|
| Salary tax and employer charges are separate | Employee ITS withholding follows 114–116I, owned by the income Guide. Do not deduct an employer-only charge as if it were employee tax. The 2026 TUS amendment changes the fund allocation, including CNSS collection for assigned portions; it does not establish the old resident/nonresident/petroleum headline rates. | [CGI116G–H;2026 TUS8](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger P01 |
| Social enrolment and limited2026 support | FinanceAct 5 requires an individual employer or an employer using informal labour to affiliate to a social-security fund. For 2026 the State bears all IRPP and half employer social/universal-health contributions for the first 25,000 specified declarants. The clause is not a general exemption for all employers; proof of inclusion and actual administration remain unconfirmed. | [FinanceAct2026 art5](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger P02 |
| 2026 continuity clause | FinanceAct 2026 art 5 leaves retirement, social and universal-health contribution rates at those set by texts in force. It does not itself resolve the conflicting 2025 Gazette and 2026 calendar or establish branch-specific wage caps. Obtain the governing instruments before computing contributions. | [FinanceAct2026 art5](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger P04 |
| Prior Gazette social conflict | The 2025 enacted Gazette art 9 prints employer CNSS 20.28% and employee 4.55%. The 2026 calendar instead gives combined 24.28%. These incompatible official publications are recorded as evidence, not resolved payroll rates. 2026Act5 preserves rates set by texts in force; the governing reconciliation and ceilings remain unconfirmed. | [FinanceAct47-2024 art9, Gazette p3](https://www.sgg.cg/JO/2024/congo-jo-2024-15-sp.pdf); ledger P05 |

## Deadlines and filing

Use I18 for employer withholding versus annual multi-source reconciliation. The 2026 calendar records payroll/social 15th entries but current returns, employer-size frequency, tax/social collection allocation and payment references are not verified. Do not replace the old 20th date with a complete filing assurance based only on the calendar.

| Item | Rule and conditions | Authority |
|---|---|---|
| Calendar evidence and conflicting social split | The official 2026 ACPCE calendar lists combined CNSS 24.28%, CAMU employee 2.27%/employer 4.55%, and monthly 15th entries. The preceding enacted 2025 Gazette art 9 instead prints CNSS employee 4.55% with employer 20.28%. This contradiction is unresolved; none of those split rates, ceilings or remittance routes is certified as an operative 2026 payroll calculation here. | [ACPCE2026calendar p2; compare2025 Gazette art9](https://acpce.cg/wp-content/uploads/2026/02/Calendrier-des-obligations-fiscales-et-sociales-au-titre-de-lannee-2026.pdf); ledger P03 |

## Penalties and interest

Current payroll/social late-filing, contribution and underpayment penalties are unconfirmed. The voluntary-tax correction clause C14 has limited triggering conditions and is not automatically a CNSS penalty rule.

## Cross-border points

For assignees, establish ITS territoriality under I13, the actual treaty/social agreement and employer facts. The old blanket 20% secondment rate and special TUS categories remain on hold.

## Two worked examples that recompute

### 1. Salary quotient computation with supplied retirement amount

Assume a full-year salary XAF 3,000,000, no benefits/exemptions, an independently established deductible employee retirement contribution 120,000, and 1 part. Under I14–I17 taxable salary is(3,000,000−120,000)×80%=2,304,000. The first 615,000 gives 1,200; the next 885,000 gives 88,500; the remaining 804,000 gives 120,600. Annual ITS is 210,300. This does not compute the legally required CNSS contribution or a final monthly remittance.

```oa-check
name: Salary quotient computation with supplied retirement amount
inputs:
  gross: 3000000
  retirement: 120000
steps:
  - net_taxable: floor((gross - retirement) * 0.80 / 1000) * 1000
  - fixed_first: 1200
  - second_band: (1500000 - 615000) * 0.10
  - third_band: (net_taxable - 1500000) * 0.15
  - annual_its: fixed_first + second_band + third_band
expected:
  net_taxable: 2304000
  annual_its: 210300
```

### 2. Decision: correct payroll family evidence

Using the same facts but a verified married employee with no children and 2 parts, quotient is 1,152,000; per-part tax 54,900 and annual ITS 109,800. A payroll setup incorrectly using 1 part would give 210,300, over-withholding 100,500. Correct the setup to the evidenced legal status; the employee does not elect whichever number is cheaper. Annual-to-monthly withholding implementation remains to verify.

```oa-check
name: Decision: correct payroll family evidence
inputs:
  taxable: 2304000
  correct_parts: 2
steps:
  - quotient: taxable / correct_parts
  - tax_per_part: 1200 + (quotient - 615000) * 0.10
  - correct_annual: tax_per_part * correct_parts
  - incorrect_one_part: 1200 + 885000 * 0.10 + (taxable - 1500000) * 0.15
  - over_withheld: incorrect_one_part - correct_annual
expected:
  quotient: 1152000
  correct_annual: 109800
  incorrect_one_part: 210300
  over_withheld: 100500
```

## Ask the client first

- Employer/employee residence, work location and income sources?
- Gross salary, benefits and exemption evidence?
- Actual governing social scheme and established retirement amount?
- Marital/dependant documents and relevant dates?
- Affiliation, support-programme inclusion and notices?

## Sources

| Source and portion actually read | Official URL | Read on |
|---|---|---|
| ACPCE 2026 fiscal and social calendar. All five pages OCR after 180-degree correction; annual/monthly/varied deadlines and rate table. Conflicts with statute are recorded, not silently resolved. | https://acpce.cg/wp-content/uploads/2026/02/Calendrier-des-obligations-fiscales-et-sociales-au-titre-de-lannee-2026.pdf | 2026-11-01 |
| Finance Act 42-2025, official gazette special 3-2026. Enacted initial 2026 law: cover; art 5; art 47 replacement CGI 2–11,15–19,21,25,42,45–49,69–86A,86C–G,92–92E,93–99,102,104–110A,111C–116I,128–131(excerpts through part 6); amendments 374ter and VAT 24/29; state invoice rule 7.2.4; final arts 61–62. Focused provisions with neighbors, not all fiscal schedules or all 116pages read. | https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf | 2026-11-01 |
| Finance Act 47-2024, official gazette special 15/2024. Cover and art 9 social contribution table on pages 2–3 only. Employee CNSS 4.55% in gazette conflicts with other official 2026 material; not used as operative split. | https://www.sgg.cg/JO/2024/congo-jo-2024-15-sp.pdf | 2026-11-01 |

Figure/rule quotations and source hashes: [country ledger](../../evidence/ledgers/republic-of-congo-draft-20261101/cg-payroll-social.md). Every worked figure is conditional on the stated example facts.

Not yet confirmed: Later 2026 law and implementation; CNSS employee/employer/branch splits and wage ceilings, including the conflicting 4% legacy and 4.55% Gazette; CAMU governing rates/base and remittance; TUS headline rates and residency/petroleum categories; current SMIG; operative monthly withholding tables/returns/boxes/payment routes; departmental/regional local tax; social/tax penalties. Do not use this partial pack to run a live payroll.

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
