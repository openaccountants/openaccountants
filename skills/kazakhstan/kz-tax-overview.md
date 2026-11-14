---
name: kz-tax-overview
description: "Kazakhstan 2026 tax pack router: current common indices and dedicated Guides for income, VAT, social payments, formation, accounts and digital assets."
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax

version: 0.1
type: router
category: international
---

# Kazakhstan tax pack overview v0.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Scope

The 2026 Kazakhstan pack entry point. Use it to identify the right job and the common index, then load the owning skill. Taxpayer status and the reporting period come before a headline rate. Ordinary CIT and individual income-tax periods use the calendar year, 1 January to 31 December (arts. 358 and 415); special commencement/cessation rules and other taxes have their own periods. The governing current Tax Code is Code No. 214-VIII of 18 July 2025; its commencement/exception provisions are in art. 848. Do not reuse the old reference to the superseded 2008 code as the operative 2026 law.

## Ask the client first

- Individual/ИП, legal entity, resident/non-resident or PE?
- Income type, actual activity and tax regime/election evidence?
- Reporting year/period, income, costs, staff and foreign transactions?
- VAT/other registration, accepted returns and outstanding obligations?

## The method, step by step

Use KZT (теңге). State Revenue Committee (КГД) under the Ministry of Finance administers the tax jobs; taxpayer-cabinet/e-Salyq and IS ESF are the operational channels, while pension/health funds have separate allocation records.

| Common input | 2026 value | Official source |
|---|---|---|
| МРП, monthly calculation index | KZT 4,325 from 1 January; budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru |
| МЗП, minimum monthly wage | KZT 85,000 from 1 January; budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru |

1. Establish residence under Tax Code arts. 221–222: residents generally have worldwide income scope; non-residents Kazakhstan-source scope, with PE exceptions. `kz-income-tax` owns the day test, income categories, progressive PIT, dividends/deductions and distinct business versus other-individual filing jobs.
2. For ordinary company income use `kz-corporate-income-tax`: the headline ordinary rate is not a substitute for sector qualification, loss computation or withholding classification. Do not copy a company rate onto an ИП.
3. For ИП/small-business special regimes, load `kz-simplified-regime`. Patent/retail are historical transitions; no valid current election is inferred from an old return. Use `kz-freelance-intake` to reconcile documents before questions and `kz-return-assembly` for the completed package.
4. For VAT/NDS load `kazakhstan-vat`: standard/reduced/zero/exempt/place-of-supply distinctions, threshold, registration and imports need their own tests. The old ordinary 2025 VAT and flat PIT shorthand are not current instructions.
5. For staff load `kz-payroll`; for ordinary ИП own payments or employer contribution components load `kz-social-contributions`, with `kz-payroll-social` as the component checklist. Keep employee deductions and employer costs separate.
6. For registration choose `kz-formation` (ИП) or `kz-company-formation` (ТОО). For records, invoice/receipt obligations and statutory statements use `kz-bookkeeping`, `kz-einvoice` and `kz-financial-statements`.
7. For digital assets/mining use `kz-crypto-tax`; for lawful regime comparison use `kz-tax-optimization`. Treat non-resident/treaty/transfer-pricing matters as their own source check/referral, not a missing rate to guess.

## Worked cases

Case 1: a hypothetical 30-МРП monthly input produces KZT 129,750 at the current index, rather than the KZT 117,960 produced by the old 2025 index. Use the result only where the owning rule specifies 30 МРП; this router does not create a deduction.

```oa-check
name: Current index changes a rule-owned amount
inputs:
  units: 30
  current_mrp: 4325
  old_mrp: 3932
steps:
  - current_amount: units * current_mrp
  - old_amount: units * old_mrp
  - difference: current_amount - old_amount
expected:
  current_amount: 129750
  old_amount: 117960
  difference: 11790
```

Case 2: a hypothetical rule-owned cap of 7 МЗП produces KZT 595,000 using the current minimum wage. A chosen income of KZT 700,000 exceeds that cap by KZT 105,000; load the contribution skill to establish which payment actually uses it.

```oa-check
name: Route a cap comparison to the owning rule
inputs:
  units: 7
  mw: 85000
  chosen: 700000
steps:
  - cap: units * mw
  - excess: max(chosen - cap, 0)
expected:
  cap: 595000
  excess: 105000
```

## When to refuse or refer

Do not compute from a headline without taxpayer/category/period facts. Do not treat the old MCI, flat PIT, VAT rate, universal individual declaration deadline or old code citation as fallback guidance. Refer unresolved residence/treaty, sector, transfer-pricing, farm, liquidation or source gaps. This router does not file, approve or contact a taxpayer/accountant.

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for 2026 budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru | 2026-11-14 |
| Read for Tax Code arts. 221–222, 363, 447 onward, 715–727 and 848 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |

Not yet confirmed: Case-specific treaty/transfer-pricing rules and any electronic form field not checked in the owning skill. Old annual-declaration and rate shortcuts are replaced by explicit linked homes; no universal deadline is asserted.
