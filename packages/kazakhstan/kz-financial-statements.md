---
name: kz-financial-statements
description: "Kazakhstan 2026 accounting and statements: conditional entrepreneur exemption, applicable reporting standards, annual delivery and depositary requirements."
version: 1.1
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: tax

type: situation-rules
---

# Kazakhstan accounting and financial statements v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

ИП and entities determining their applicable statutory accounting/reporting framework, and public-interest bodies submitting to the financial-report depositary. Tax returns are a separate job. Do not infer accounting exemption solely from being ИП or audit liability solely from the label “IFRS”.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| ИП exemption from full accounts/statements | All art. 2(2) conditions: simplified declaration, annual income ≤135,000 МРП, not VAT registered and not natural monopoly; primary documents still required | https://adilet.zan.kz/rus/docs/Z070000234_ |
| Failure or voluntary election | Full accounting/statements start from the following month (art. 2(2)) | https://adilet.zan.kz/rus/docs/Z070000234_ |
| Ordinary small entities | National standard; permitted election to IFRS for SMEs or full IFRS (art. 2(3),(5)) | https://adilet.zan.kz/rus/docs/Z070000234_ |
| Ordinary medium entities | IFRS for SMEs; permitted election to full IFRS (art. 2(3-1),(5)) | https://adilet.zan.kz/rus/docs/Z070000234_ |
| Large/public-interest and specified financial entities | Full IFRS; small/medium non-public-interest microfinance uses IFRS for SMEs plus National Bank rules (art. 2(3-2),(4)) | https://adilet.zan.kz/rus/docs/Z070000234_ |
| Ordinary annual report delivery | By 30 April following reporting year; financial entities have the art. 19(3-1) regulator schedule exception | https://adilet.zan.kz/rus/docs/Z070000234_ |
| Public-interest depositary annual submission | By 31 August following reporting year, excluding inactive during the period and those bankrupt before 1 January of the reporting period (2026 amended rules para. 3) | https://adilet.zan.kz/rus/docs/V2600039667 |
| Depositary acceptance response | Within 3 working days; accepted only on inclusion notice (base rules para. 9; figure in words on the page) | https://adilet.zan.kz/rus/docs/V2200026686 |

## The base

Determine statutory enterprise-size/public-interest status from actual evidence and current classification law, then apply Accounting Law art. 2; do not default an unknown ТОО to small status. For small entities the national standard is the starting framework, subject to the legal elections and financial-entity exceptions above. Medium does not automatically mean full IFRS. Full financial statements and their components follow the selected standard and Accounting Law art. 15; a simplified national-standard form cannot be imposed on a full-IFRS filer.

An otherwise qualifying simplified ИП IT freelancer keeps tax registers and primary documents rather than full statutory statements. An ИП on general taxation or exceeding the lower accounting exemption cannot rely on that statement. Incorporating a ТОО triggers the legal-entity framework analysis, not continuation of the individual exemption. Use `kz-bookkeeping` for the evidence and start-month controls.

Audit liability is a separate test under current Audit Law art. 5(2), including any sector/size/public-interest rule. Do not assert every medium/large IFRS filer is audited solely on that basis. For a mandatory-audit depositary filer, the 2026 amendment requires an audit report PDF scan of the signed and stamped-if-any report; a parent with subsidiaries supplies the consolidated audit report (para. 6). Voluntary audit submission is optional.

## Deadlines and filing

Separate ordinary delivery to the persons/bodies specified in Accounting Law art. 19 from publication in the depositary; their deadlines differ. For a public-interest depositary submission: prepare the approved annual statements, approval decision, required audit report and entity-identification data. Use the portal personal cabinet/“Единая система сдачи отчетности” under base rules paras. 7–8; form the electronic report, obtain management and chief-accountant digital signatures and send it. Retain the inclusion/refusal notice: upload alone is not acceptance. Base para. 9 says submitted statements and audit reports cannot be replaced/deleted through this process, so resolve errors before signing and refer subsequent corrections to the authority’s applicable procedure. New organisations report from registration through 31 December under amended para. 4. Do not substitute a tax-cabinet receipt for depositary acceptance.

## Penalties and interest

Numerical administrative penalties and consequences of a missed audit/publication duty require the applicable current provision and filer category. Keep evidence of the breach and response; no universal penalty is asserted.

## Cross-border points

Foreign branches/PEs registered in Kazakhstan fall within the Accounting Law’s scope, with specific financial-branch and regulator rules. Group consolidation, foreign reporting frameworks and sector regulation require specialist review. Statutory accounts do not replace income/VAT/payroll declarations.

## Two worked examples that recompute

Case 1: hypothetical simplified ИП annual income KZT 580,000,000, no VAT/natural-monopoly status. With a 2026 accounting ceiling KZT 583,875,000, headroom is KZT 3,875,000. The income condition is met; all other conditions still require evidence.

```oa-check
name: IP financial-statement exemption headroom
inputs:
  income: 580000000
  mrp: 4325
steps:
  - ceiling: 135000 * mrp
  - headroom: ceiling - income
expected:
  headroom: 3875000
```

Case 2: hypothetical income of KZT 580,000,000 followed by KZT 10,000,000 takes cumulative income to KZT 590,000,000, exceeding the accounting exemption by KZT 6,125,000. Establish that month and start accounting/statements the next month. A move to ТОО would separately remove the individual exemption regardless of this headroom.

```oa-check
name: Accounting exemption breach
inputs:
  prior_income: 580000000
  new_income: 10000000
  mrp: 4325
steps:
  - total: prior_income + new_income
  - ceiling: 135000 * mrp
  - excess: max(total - ceiling, 0)
expected:
  total: 590000000
  excess: 6125000
```

## Ask the client first

- Legal form, annual income, regime, VAT/natural-monopoly status and exemption/election history?
- Actual enterprise-size, public-interest, financial/microfinance status and approved accounting policy?
- Reporting year, group/subsidiaries and mandatory-audit basis?
- Approved statements, approval decision, signatures and depositary status?
- Regulator-specific delivery/audit requirements and unresolved corrections?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for current Accounting Law arts. 1–2, 15 and 19, ordinary browser | https://adilet.zan.kz/rus/docs/Z070000234_ | 2026-11-14 |
| Read for depositary rules paras. 7–9, ordinary browser | https://adilet.zan.kz/rus/docs/V2200026686 | 2026-11-14 |
| Read for 2026 amendment replacing paras. 3–4 and 6, ordinary browser | https://adilet.zan.kz/rus/docs/V2600039667 | 2026-11-14 |
| Read for 2026 budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru | 2026-11-14 |

Not yet confirmed: Current enterprise-size thresholds, full mandatory-audit classification under Audit Law art. 5(2), regulator-specific calendars, exact national-standard statement forms and numerical penalties. The old all-ИП exemption, automatic medium/full-IFRS rule and automatic audit generalisation are superseded.
