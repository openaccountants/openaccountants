---
name: jp-nonpermanent-resident
description: "Japan non-permanent resident regime: nationality and aggregate residence test, foreign income paid in Japan, annual deemed remittance allocation, securities exceptions and transition to worldwide taxation. Trigger on Japan non-permanent resident, Japan tax resident foreign income, Japan 5-year rule, move to Japan taxes, Japan remittance basis, Japan income tax non-permanent, working in Japan foreign income, or Japan PR tax status. Load before advising on limited foreign-income taxation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/jp-nonpermanent-resident"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Japan non-permanent resident income scope v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Determine an individual's Japanese national income-tax residence category and which income enters the 2026 computation. Tax-law non-permanent residence differs from immigration permanent residence. This is a scope working paper for a Japanese tax accountant (税理士); `jp-income-tax` does not compute a non-permanent resident's complete return.

| Quick reference | Conditions and rule | Official source |
| --- | --- | --- |
| Resident | Japanese domicile, objectively determined centre of life, or continuous residence for at least 1 year | Income Tax Act arts. 2, 3; Order arts. 13-15: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2875.htm |
| Non-permanent resident | Resident without Japanese nationality; aggregate Japanese domicile/residence of 5 years or less during the past 10 years | Income Tax Act arts. 2, 5, 7: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2010.htm |
| Other resident | Resident failing either non-permanent-resident condition; worldwide income is within scope | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2010.htm |
| Non-resident | Not a resident; domestic-source income only, under the applicable detailed rules | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2010.htm |

Exactly 5 years remains within the test; do not switch merely on reaching that total. Track the rolling lookback and exact dates. A break does not erase earlier residence within the window. Temporary absence may leave residence continuous: the NTA's 2025-2026 filing-cycle guide names a retained home, household or personal effects as relevant facts.

## Ask the client first

Obtain nationality; domicile facts; every arrival, departure and residence interval; retained home/family during absences; foreign residence and treaty claims; each income type, source and payment location; receipts and costs; every remittance, cash import, foreign-card settlement and Japanese debt paid from abroad; security acquisition dates, residence at acquisition, custody and disposal route. Obtain annual statements for every account. Employer nationality, payment currency and account location do not alone establish income source.

## The method, step by step

1. Establish residence from domicile or continuous residence, then test nationality and the aggregate lookback. A full-time job and home in Japan can establish domicile on arrival; a work visa alone is not the test. Refer dual residence for the actual treaty; No. 2875 gives examples, not a universal tie-breaker.
2. Classify income under Japanese source rules. All income **other than statutory foreign-source income** enters a non-permanent resident's scope wherever paid. Japanese employment, business, rent and dividends need their actual source analysis, not merely a Japanese employer label.
3. Include foreign-source income paid in Japan even without an overseas remittance. Include foreign-source income paid abroad to the extent deemed remitted. The annual rule is not tracing particular money. Separate accounts assist evidence but do not switch it off.
4. Basic Circular 7-3 requires adjusted totals of non-foreign-source and foreign-source income paid abroad. Remittances first cover the non-foreign-source amount paid abroad; the excess is deemed remitted foreign-source income, capped at that foreign-source amount. A negative non-foreign-source amount does not increase the allowance. A negative foreign-source total produces no deemed-remitted amount under that paragraph. Multiple foreign income types need the Order's category allocation; the simple total is not a complete return computation.
5. Count remittances broadly. Circular 7-6 includes ordinary transfers, imported currency and substitutes such as paying Japanese borrowing from foreign deposits. Examine foreign-card spending in Japan as a substituted payment. Funding a transfer with old savings does not itself exclude it from annual deemed-income allocation.
6. Do not repeat the old assertion that every foreign share/property gain escapes tax unless remitted. Circular 7-1 identifies special securities by acquisition on or before the date 10 years before disposal, acquisition while not a non-permanent resident, or acquisition by 31 March 2017. Order art. 17(1) additionally requires disposal on a foreign financial market, through a foreign broker, or securities recorded/held in an account at the specified foreign financial business overseas. Where both the special acquisition test and a qualifying foreign route are met, the gains enter the foreign-source scope subject to the non-permanent resident payment/remittance rule; other source rules and treaty effects still require review. Test the actual qualifying route. Article 17(2) identifies acquisition dates oldest-first among the same security; this is a scope-lot test, not an election of tax cost basis. Corporate reorganisations in art. 17(3) can carry acquisition history, so refer those before claiming exemption.
7. Reassess on residence/nationality changes. Worldwide taxation applies during residence outside the non-permanent category; a visa change is a different question. For a category change, art. 17(4)(6) confines the remittance computation to income arising and remittances made during the non-permanent-resident period; refer the actual split-period return, treaty relief and foreign credits.

### Rates, bands and thresholds

National aggregate-income rates apply after deductions and rounding taxable income down to JPY 1,000, not on gross foreign receipts. Separately taxed gains use their own computation. Quick-table tax is the whole taxable amount times the rate, less the stated deduction.

| Rounded taxable income JPY | Rate | Deduction JPY | Official source |
| --- | --- | --- | --- |
| 1,000-1,949,000 | 5% | 0 | Income Tax Act art. 89; General Act art. 118: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 1,950,000-3,299,000 | 10% | 97,500 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 3,300,000-6,949,000 | 20% | 427,500 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 6,950,000-8,999,000 | 23% | 636,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 9,000,000-17,999,000 | 33% | 1,536,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 18,000,000-39,999,000 | 40% | 2,796,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| At least 40,000,000 | 45% | 4,796,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Reconstruction surtax, 2026 | 2.1% of base national income tax, not inhabitant tax | Separate charge | Reconstruction Finance Act arts. 8-13: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |

No. 2260 flags the separate very-high-income minimum tax and enacted surtax changes from 2027; this file computes neither. Municipal/prefectural inhabitant tax has its own base and deductions. The national reconstruction surtax does not apply to that local levy.

## Boundary and exception table

| Fact | Treatment | Official source |
| --- | --- | --- |
| Foreign-source income retained abroad without remittance | Outside scope only if not paid in Japan and genuinely statutory foreign-source income | Income Tax Act art. 7: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2010.htm |
| Foreign-source income paid directly into Japan | Within scope without later transfer | Circular 7-4: https://www.nta.go.jp/law/tsutatsu/kihon/shotoku/02/01.htm |
| Other income paid abroad | Within scope; also affects first allocation of remittances | Circular 7-2/7-3: https://www.nta.go.jp/law/tsutatsu/kihon/shotoku/02/01.htm |
| Japanese national | Cannot qualify as a non-permanent resident | Income Tax Act art. 2: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2010.htm |
| Temporary absence | Examine continuity, never reset earlier aggregate residence automatically | NTA guide section 1-3, 2025-2026 filing cycle: https://www.nta.go.jp/english/taxes/individual/pdf/incometax_2025/04.pdf |
| Unpaid income with unclear payment location | Determine from specific facts and past practice | Circular 7-5: https://www.nta.go.jp/law/tsutatsu/kihon/shotoku/02/01.htm |

## Worked cases

Scope allocations before deductions or tax, derived from Circular 7-3, not final liabilities. Case A scales the NTA guide's example into JPY: 260,000 remitted first covers 250,000 of non-foreign income paid abroad, then 10,000 of foreign income paid abroad.

```oa-check
name: Non-permanent resident annual remittance allocation
inputs:
  nonforeign_japan: 500000
  nonforeign_abroad: 250000
  foreign_japan: 150000
  foreign_abroad: 100000
  remittances: 260000
steps:
  - foreign_remitted: min(max(remittances - max(nonforeign_abroad, 0), 0), max(foreign_abroad, 0))
  - in_scope: nonforeign_japan + nonforeign_abroad + foreign_japan + foreign_remitted
  - outside_scope: foreign_abroad - foreign_remitted
expected:
  foreign_remitted: 10000
  in_scope: 910000
  outside_scope: 90000
```

Case B tests the domestic-payment exception. With no remittance, foreign income paid in Japan remains in scope; only the foreign income paid and retained abroad is excluded.

```oa-check
name: Foreign income paid in Japan without remittance
inputs:
  nonforeign: 4000000
  foreign_japan: 300000
  foreign_abroad: 700000
  remittances: 0
steps:
  - foreign_remitted: min(remittances, foreign_abroad)
  - in_scope: nonforeign + foreign_japan + foreign_remitted
  - outside_scope: foreign_abroad - foreign_remitted
expected:
  in_scope: 4300000
  outside_scope: 700000
```

## When to refuse or refer

Refer uncertain residence, dual residence, securities/property sourcing, mid-year category changes, foreign credits, treaty interactions or very high income to a Japanese tax accountant. Do not claim a remittance exemption without source classification and annual statements. Non-resident returns need separate domestic-source and withholding analysis. This paper authorises no filing, payment or tax position.

## Filing and payment

A required individual return ordinarily runs from 16 February to 15 March of the following year, with payment by that deadline, subject to holidays and extensions (NTA No. 2020). For 2026 income this ordinarily means 16 February-15 March 2027, derived from that rule. Death/departure and tax-agent timing need separate confirmation. Use NTA return preparation with e-Tax or paper; retain the scope working paper and receipt. Filing does not pay the tax: select and complete the payment route separately.

## Completion checklist

- Residence, nationality, rolling lookback and absences documented.
- Receipts classified by statutory source and payment location.
- Annual remittances reconciled; separate accounts not treated as an exemption.
- Securities conditions, treaties and foreign credits resolved or held.
- National and local taxes separate; output marked estimated, not reviewed.

## Sources

| Source | Official URL | Read on | Material read |
| --- | --- | --- | --- |
| NTA No. 2010 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2010.htm | 2026-11-14 | Read for all categories, nationality, lookback and scope; entire table and statutory references; law dated 1 April 2026 |
| NTA No. 2875 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2875.htm | 2026-11-14 | Read for objective domicile facts, residence and treaty examples |
| NTA Income Tax Basic Circular art. 7 | https://www.nta.go.jp/law/tsutatsu/kihon/shotoku/02/01.htm | 2026-11-14 | Read for 7-1 securities, 7-2/7-3 allocation, 7-4 domestic payment, 7-5 unpaid income, 7-6 substitutes |
| Income Tax Enforcement Order art. 17 | https://laws.e-gov.go.jp/law/340CO0000000096 | 2026-11-14 | Read for entire art. 17 via official e-Gov API; revision effective 22 May 2026; securities routes, acquisition history and all annual/mid-year allocation paragraphs |
| NTA No. 2260 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm | 2026-11-14 | Read for all national rate rows, rounding and all notes, including minimum tax and later surtax boundaries |
| NTA No. 2020 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2020.htm | 2026-11-14 | Read for ordinary filing/payment, exceptions, forms and payment routes |
| NTA English guide section 1-3 | https://www.nta.go.jp/english/taxes/individual/pdf/incometax_2025/04.pdf | 2026-11-14 | Read for categories, temporary absence and full remittance example; historical 2025-2026 filing cycle only |

Not yet confirmed: case-specific securities custody/disposal records and corporate-reorganisation history; foreign property-gain sourcing; particular foreign-card settlements; specific treaty/foreign-credit eligibility; split-period residence dates; municipal inhabitant-tax rates and deductions. The old local 10% and approximate combined top 55% are withdrawn from usable instructions pending local sourcing. The 2025-2026 English guide does not establish a 2026 return form.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `jp-nonpermanent-resident` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/jp-nonpermanent-resident. If neither is available, confirm every figure against the official source pages cited above before relying on it.
