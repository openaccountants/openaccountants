---
name: jp-incorporation
description: "Use this skill whenever asked about incorporating in Japan -- transitioning from sole proprietorship (個人事業主) to a corporation (法人). Trigger on phrases like \"incorporation Japan\", \"法人成り\", \"会社設立\", \"should I incorporate\", \"法人化\", \"株式会社\", \"合同会社\", \"KK vs GK\", \"corporate tax vs income tax\", \"法人税\", \"when to incorporate\", \"法人成りのタイミング\", \"micro corporation\", \"マイクロ法人\", \"officer compensation\", \"役員報酬\", \"social insurance comparison\", \"社会保険\", \"個人事業 vs 法人\", \"定期同額給与\", \"consumption tax exemption reset\", \"消費税の免税リセット\", or any question about whether, when, and how a Japanese sole proprietor should form a company. This skill covers tax burden comparison, breakeven analysis, corporate form selection, establishment procedures, filing deadlines, officer compensation strategy, and social insurance optimization. ALWAYS read this skill before advising on Japanese incorporation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/jp-incorporation"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# JP Incorporation

> **Based on work by [Kazuki Nagata (@kazukinagata)](https://github.com/kazukinagata/shinkoku)**, licensed under MIT. Adapted for the OpenAccountants format.

> **General reference only.** This skill produces working papers for professional review. It has not been approved by an accountant for any particular person, entity, election or filing. Confirm the applicable facts and official forms before filing, paying or taking a position.

## Scope

2026 financial decision whether a Japanese sole proprietor should incorporate (法人成り), when to transition and how to compare officer remuneration with retained profit. Produce estimated household-plus-company cash flows and a transition checklist. `japan-formation` handles the legal registration process; this skill does not repeat or replace it.

Quick reference: there is no statutory income breakeven at which incorporation automatically saves money. Compare income taxes, local taxes, both shares of compulsory insurance, fixed administration, formation costs, consumption tax and cash actually available to the household. Do not compare a proprietor's full profit with only the company's retained-profit tax.

## Ask the client first

- Residence, municipality, age, household/dependants, other income, deductions and current insurance.
- Sustainable business profit before owner pay, required household withdrawals, expected growth and retained cash.
- Blue-return status, actual books, current consumption-tax/invoice status and sales/payroll by relevant period.
- Proposed capital, ownership/group, KK/GK, officer duties, proposed remuneration and first year-end.
- Current local tax/insurance assessments and quotations for company insurance, accounting, registration and recurring administration.
- Contracts, inventory/assets, receivables/payables and whether any personal business continues.

## The method, step by step

### Compare like-for-like annual cash flows

For the proprietor start with business revenue less evidenced business expenses, then apply the available blue-return deduction and personal deductions. Compute national tax/surtax and actual local taxes plus national health/pension obligations. For the company start with the same pre-owner-pay operating result; deduct qualifying officer remuneration, employer insurance and extra company costs to determine taxable retained profit after tax adjustments. Compute company national/local taxes, then the officer's personal taxes and employee insurance. Add all burdens. Treat company retained profit separately from spendable household cash and test later distribution/exit costs.

| Component | Rule and full boundary | Official source |
|---|---|---|
| Individual blue deduction | Up to JPY 550,000 with regular books, required statements and timely filing; JPY 650,000 only with qualifying e-Tax/electronic conditions; otherwise up to JPY 100,000; positive eligible income limits apply ; monetary amounts derived from Japanese 万/億 units | Special Measures Act art.25-2; NTA No.2072, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| National personal tax | 5%-45% progressive, applied to taxable income after deductions and statutory rounding; not gross business profit | Income Tax Act art.89; NTA No.2260, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Reconstruction surtax for 2026 | 2.1% of the relevant national income-tax amount; apply credits/rounding in the actual return | NTA No.2260, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Eligible small-company national corporation tax | 15% on first JPY 8,000,000 annual income, 23.2% above; capital no more than JPY 100,000,000 alone is insufficient: large-owner, group and excluded-business tests apply ; monetary amounts derived from Japanese 万/億 units | Corporate Tax Act art.66; Special Measures Act art.42-3-2; NTA No.5759, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5759.htm |
| Important corporate reduced-rate exceptions | Excluded businesses use 19% on first annual JPY 8,000,000; income above annual JPY 1,000,000,000 makes that first slice 17% for affected years beginning from 1 April 2025; do not apply these rates blindly to every company ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5759.htm |
| Corporate workplace insurance | Compulsory coverage can apply even where the only insured worker is a remunerated owner; obtain actual standard remuneration and insurance assessments | Japan Pension Service, https://www.nenkin.go.jp/service/kounen/tekiyo/jigyosho/20150311.html |
| New-corporation consumption-tax capital test | Capital/contributions at least JPY 10,000,000 at the start of a no-base-period year disqualify the general exemption; invoice registration and other exceptions also override it ; monetary amounts derived from Japanese 万/億 units | Consumption Tax Act arts.9,12-2,12-3; NTA No.6503, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6503.htm |

Use the current-year personal basic deduction. For normal 2026 resident returns under the provisions effective 1 December 2026: total income no more than JPY 4,890,000 gives JPY 1,040,000; over that to JPY 6,550,000 gives JPY 670,000; over that to JPY 23,500,000 gives JPY 620,000; the higher-income taper is JPY 480,000 to JPY 24,000,000, JPY 320,000 to JPY 24,500,000, JPY 160,000 to JPY 25,000,000, then zero. Early death/departure returns filed before 1 December have special timing, with correction relief after commencement; nonresidents do not get the resident additions. Source: Income Tax Act art.86 and Special Measures Act art.41-16-2; NTA No.1199, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm.

### Officer remuneration and family work

Qualifying deductible remuneration includes fixed periodic pay, qualifying pre-notified fixed pay and qualifying performance-related pay; unreasonable excess and sham payments remain non-deductible. Fixed periodic pay normally has intervals no longer than 1 month with equal gross amounts or qualifying equal net amounts. Ordinary annual revisions generally occur within 3 months of the accounting period start; substantial role changes or genuine severe business deterioration can support the specified exceptions, while temporary cash shortage or a missed target is not enough. Do not state all officer bonuses are prohibited or deductible. Source: Corporate Tax Act art.34; NTA No.5211, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5211.htm.

Salary-income deduction for 2026 is not the old minimum JPY 650,000 schedule. The schedule effective 1 December 2026 gives JPY 740,000 up to receipts JPY 2,200,000; 30% plus JPY 80,000 up to JPY 3,600,000; 20% plus JPY 440,000 up to JPY 6,600,000; 10% plus JPY 1,100,000 up to JPY 8,500,000; maximum JPY 1,950,000 above that. For receipts below JPY 6,600,000 use the statutory lookup and special low-income adjustments on the NTA page; the smooth percentage table is not the final statutory result for every yen. Combine multiple salary statements before applying it. Source: Income Tax Act art.28/Appendix5; NTA No.1410, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm.

Compare remuneration alternatives only after allowing for both insurance shares, local tax, company deductions and household cash needs. Family pay must correspond to real documented duties and reasonable remuneration; obtain payroll and related-party advice. Do not promise the old family-splitting saving or prescribe a fixed owner/spouse amount.

### Consumption-tax and transition decision

A new company generally lacks a base period in its initial years, but the exemption is conditional. Check capital at each year's start, specified-period sales/payroll, qualified-invoice registration, taxable-business election, restructuring exceptions and specified newly established corporation rules. The latter include controlling-party/group tests and relevant-period taxable sales above JPY 500,000,000 or total revenue above JPY 5,000,000,000 under the applicable rule. A short first year is not an automatic exemption guarantee. Invoice registration belongs to the new legal person; the proprietor's number is not transferred. Source: NTA No.6503, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6503.htm.

Choose KK or GK based on investment, governance, transfer/distribution terms and counterparties, as well as fees. KK articles are notarised; GK articles are not under the KK rule. Director terms and reappointment obligations differ, and GK profit-sharing can be set by articles. A GK cannot simply issue listed shares without a legal conversion. Obtain legal advice before fundraising. Companies Act arts.30,332,575-590,622, https://laws.e-gov.go.jp/law/417AC0000000086.

Choose a transition date from real contracts and reporting periods. Inventory, fixed assets, debtors/creditors and loans require documented transfer terms and tax review; book value is not an automatic safe price. Close or retain the personal business deliberately, file its final individual return, and review estimated-tax reduction. Complete new-company notices and assess cessation of the proprietor's income-tax, blue-return, payroll, consumption-tax, invoice and prefectural registrations. Do not cancel the individual's invoice registration automatically while it still makes taxable supplies. The exact closure forms/deadlines are a referral boundary below.

## Boundary and exception table

| Issue | Decision response |
|---|---|
| Low income or large household withdrawals | Extra insurance, accounting and per-capita local tax can outweigh the national corporate-rate difference; compute both options |
| High income with retained capital needs | Test company retention and future extraction; a lower current company rate alone does not prove lifetime saving |
| Local tax and administration | Include actual per-capita corporate inhabitant tax even in loss years when applicable; obtain prefectural/municipal rates and adviser quote, not a national fee approximation |
| Social insurance benefits | Compare dependants, sickness/maternity entitlement, disability and pension accrual using actual eligibility; employer premiums are not the only difference |
| Micro-corporation plus personal business | Require real separate activity, duties and valid insurance status; disclose denial/recharacterisation risk and both entities' costs; no artificial division of the same client work or paper-company recommendation |
| Consumption-tax recovery | A taxable election can help input recovery but creates ongoing obligations and may affect future exemption; model before choosing |

## Worked cases

Case 1 is a hypothetical full comparison with amounts supplied by separately prepared tax/insurance schedules, not prescribed 2026 rates. At pre-owner-pay profit JPY 5,000,000 the proprietor's tax is JPY 600,000, insurance JPY 700,000 and administration JPY 100,000: total JPY 1,400,000. The combined company/owner tax is JPY 500,000, both insurance shares JPY 1,200,000 and administration JPY 400,000: total JPY 2,100,000. Remaining combined cash is JPY 3,600,000 versus JPY 2,900,000. Staying personal is ahead by JPY 700,000 under these inputs.

```oa-check
name: Decision favors proprietor after both insurance shares and administration
inputs:
  profit: 5000000
  proprietor_tax: 600000
  proprietor_insurance: 700000
  proprietor_admin: 100000
  combined_corporate_owner_tax: 500000
  combined_insurance: 1200000
  corporate_admin: 400000
steps:
  - personal_burden: proprietor_tax + proprietor_insurance + proprietor_admin
  - company_burden: combined_corporate_owner_tax + combined_insurance + corporate_admin
  - personal_cash: profit - personal_burden
  - combined_company_cash: profit - company_burden
  - personal_advantage: company_burden - personal_burden
expected:
  personal_burden: 1400000
  company_burden: 2100000
  personal_cash: 3600000
  combined_company_cash: 2900000
  personal_advantage: 700000
```

Case 2 uses hypothetical reviewed schedules for a different business with JPY 15,000,000 profit. Personal tax/insurance/admin are JPY 4,000,000/1,500,000/100,000. Combined company-owner tax/insurance/admin are JPY 3,000,000/1,800,000/500,000. Incorporation reduces annual burden by JPY 300,000. If separately quoted formation costs are JPY 450,000, simple cash payback is 1.5 years, before growth, financing, distribution/exit costs and benefit differences. The opposite decisions show why no universal profit threshold is valid.

```oa-check
name: Decision favors incorporation but formation costs delay payback
inputs:
  profit: 15000000
  personal_tax: 4000000
  personal_insurance: 1500000
  personal_admin: 100000
  combined_tax: 3000000
  combined_insurance: 1800000
  company_admin: 500000
  quoted_formation: 450000
steps:
  - personal_burden: personal_tax + personal_insurance + personal_admin
  - company_burden: combined_tax + combined_insurance + company_admin
  - annual_saving: personal_burden - company_burden
  - payback_years: quoted_formation / annual_saving
expected:
  personal_burden: 5600000
  company_burden: 5300000
  annual_saving: 300000
  payback_years: 1.5
```

## When to refuse or refer

Never present incorporation as universally beneficial, specify definitive officer pay without facts, omit either insurance share, ignore local fixed tax/adviser costs, assume invoice-registered companies remain exempt, or recommend a paper micro-corporation. Label projections estimated and obtain tax, company-law and insurance review. No-work family salaries, artificial splitting, undocumented asset transfers and immigration cases require specialist advice.

## Filing and payment

Follow `japan-formation` for registration, corporate establishment and blue-return notices, payroll opening and insurance enrolment. Prepare a dated handoff for continuing/closing the personal business and each relevant tax/insurance registration. Carry separate year-end returns, remittances and receipt records for proprietor and company. No incorporation date retroactively moves the proprietor's earned income into the company.

## Completion checklist

Both cash-flow options reconciled to the same operating profit; personal/company tax schedules and municipality specified; both insurance shares and benefits tested; household withdrawals and retained earnings distinguished; remuneration and family duties documented; consumption-tax exceptions checked; formation/recurring quotes included; transfers/notices/cessation actions assigned.

## Sources

| Source | URL | Read on |
|---|---|---|
| NTA No.2072; Read for deduction conditions and income limits | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm | 2026-11-14 |
| NTA No.2260; Read for progressive rates, surtax and rounding | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm | 2026-11-14 |
| NTA No.1199; Read for 2026 deduction/taper and early-return/nonresident exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm | 2026-11-14 |
| NTA No.1410; Read for 2026 salary deduction and lookup-table overrides | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm | 2026-11-14 |
| NTA No.5759; Read for all SME rate exceptions and controlling-owner exclusions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5759.htm | 2026-11-14 |
| NTA No.5211; Read for deductible classes, excessive pay and revision exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5211.htm | 2026-11-14 |
| Japan Pension Service; Read for corporate workplaces including owner-only coverage | https://www.nenkin.go.jp/service/kounen/tekiyo/jigyosho/20150311.html | 2026-11-14 |
| NTA No.6503; Read for all no-base-period exceptions and specified-new-company tests | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6503.htm | 2026-11-14 |
| Companies Act; Read for form, articles, governance and profit-sharing rules | https://laws.e-gov.go.jp/law/417AC0000000086 | 2026-11-14 |

Not yet confirmed: Old income breakeven recommendations at JPY 5,000,000 through JPY 15,000,000 and the five 2025 simulation tables are not sourced tax results; old enterprise/local-tax rates and surcharges, NHI/pension premium amounts, health/nursing rates, benefit amounts, remuneration caps and premium plateaus; fee ranges and universal JPY 70,000 minimum local tax; fixed officer-pay targets, JPY 570,000 family saving, JPY 63,000 micro-company pay and JPY 890,000 saving; automatic short-first-year/19-month exemption and 2-wari endpoint; exact proprietor closure/cessation/cancellation deadlines and labour-insurance forms. They are excluded from usable guidance until the relevant current official rules and locality/client facts are obtained. Historical topics remain decision inputs above, not recommended strategies or current rates.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `jp-incorporation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/jp-incorporation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
