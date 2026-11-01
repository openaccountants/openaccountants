---
name: sd-corporate-income-tax
description: >
  Prepare Sudan company business profit workpapers for 2026 intake from the official Income Tax Act and identified amendments, without treating an incomplete historical chain as current certification. Covers ordinary resident companies, industrial businesses, foreign branches and sector classification, with expense, capital allowance, loss and collection controls. Match Sudan corporate income tax, business profits tax, BPT, taxable profits, company losses and ضريبة أرباح الأعمال requests. Separate general company profit from telecom net income, agriculture and concession arrangements. Document accounting periods, audited evidence, withholding credits and unresolved regulations. This Guide supports a broad statutory baseline computation and review handoff, with a firm stop before an operative filing or rate conclusion.
version: 0.3
jurisdiction: SD
tax_year: 2026
last_updated: 2026-11-01
authored_by: Ahmed Hassan
review_status: pending_review
trust_label: Accountant-authored
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tax_year_notes: "2026 intake; opened historical statutory baseline only; later enacted chain unresolved"
---

# Sudan company business profits v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **2026 intake, partial statutory baseline.** Figures below reproduce identified opened instruments, not a completed operative 2026 consolidation. Before filing, paying, granting relief or advising registration, reconcile later enacted amendments and obtain the missing regulations, current forms and directions named in Sources. Passing arithmetic or format checks does not clear this gate. Amounts are source-period SDG; no currency redenomination or indexation is assumed.

## Who this applies to

Ordinary company business-profit preparation, including industrial classification and foreign-company intake. Use [cross-border](sd-cross-border-residence.md) for residence/source/agent questions and [transfer pricing](sd-transfer-pricing.md) for associated dealings. Investment licences, concessions, banks, insurance and extractive activities require their own operative terms. Do not infer a single general rate for every sector.

## Rates, bands and thresholds

| Item | Opened source wording and conditions | Official source |
|---|---|---|
| General company | 20% source-period business profit after 2019 amendment; classification and later-law gate apply. | [Income Tax Amendment 2019 s.2(2)(c)–(d), PDF1](https://tax.gov.sd/wp-content/uploads/2025/02/law21.pdf) |
| Industrial company | 15% source-period business profit after 2019 amendment; industrial qualification requires evidence. | [Income Tax Amendment 2019 s.2(2)(c)–(d), PDF1](https://tax.gov.sd/wp-content/uploads/2025/02/law21.pdf) |
| Telecom and specified similar companies | 30% NET income under 2021 amendment, replacing older gross-turnover treatment. | [Income Tax Amendment 2021 s.2(e), PDF2](https://tax.gov.sd/wp-content/uploads/2025/02/law32-34.pdf) |
| Agriculture | 2022 zero-to 2% classification range; Secretary General classes, base and intervening rules unresolved. Do not automatically use zero. | [Income Tax Amendment 2022 s.2(6)(b), PDF2](https://tax.gov.sd/wp-content/uploads/2025/02/law38-39.pdf) |
| Business losses | Up to 5 years, with statutory books, returns, validated accounts and continuity/force-majeure conditions. | [s.21; PDF37–39](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Employee incentive deduction | Restricted to 3 months salary annually under the opened principal provision. | [s.18(2); PDF32](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |

## The base

1. Reconcile financial statements and tax basis period, identifying each revenue source and sector. The assessment year follows the basis period; an approved different accounting period is not a different tax country.
2. Start with accounting profit. Add private/capital charges, income tax, unsupported reserves and compensated losses; deduct only wholly and actually income-producing expenses under s.18. Record paid Zakat and proof separately. Do not convert a tax incentive into an accounting expense.
3. Replace book depreciation with statutory s.20/ScheduleII allowances only after the actual asset class, qualifying cost and applicable regulations are established. The catalogue's alleged 2021 regulations PDF is another Act copy; the full governing regulations remain unread. No flat 20% machinery allowance is approved.
4. Separate revenue bad debts and recoveries, capital balancing adjustments and disposal gains. [Capital gains](sd-capital-gains.md) excludes company assets already within income-tax balancing treatment; avoid double taxation by classifying first.
5. Apply loss schedules only with the s.21 proof and continuity conditions. Keep each loss-year cohort and expiry separate; current unaudited accepted loss is not automatically carried forward.
6. Record associated payments and avoidance arrangements for the dedicated TP/antiavoidance review. Commercial charity activity is not automatically exempt. For on-account credit, retain validated audited accounts OR an income return under s.38, plus supporting deduction/payment documents under s.65(2). Section 65(1)(j) certificates/receipts satisfy tax up to proved amounts even if the collecting person fails to remit; an audited return or actual collector remittance is not universally prerequisite.

## Deadlines and filing

Obtain TIN, approved period, accounts, capital-allowance and loss schedules, advance/on-account certificates and all notices. Follow the principal s.38 return-notice framework and s.62 payment-date rule; the full current 2021 regulations, self-assessment forms, boxes, instalment dates and electronic submission workflow are not established. Do not claim Act 38(2) contains a universal modern self-assessment rule. Preserve records under s.39 and the later Arabic-translation addition. Before filing, require the actual applicable return/codes, due date, payment route/reference and evidence of submission/payment. This pack does not authorise a taxpayer action.

## Penalties and interest

Sections 44,62–63 and recovery provisions supply an enforcement framework. Current regulatory percentages, amended amounts, failure-to-file sanction and appeal/payment interactions need their actual instruments. Do not apply an unsourced flat monthly penalty or a universal twice-tax surcharge.

## Cross-border points

Foreign branches and resident foreign income need the residence, agent, treaty-order and withholding analysis in [cross-border](sd-cross-border-residence.md). A foreign-owned company is not automatically nonresident. Do not substitute a six-month PE threshold or assumed branch-remittance exemption. On-account credit is conditional and not always final.

## Two worked examples that recompute

### General versus industrial classification

On hypothetical eligible taxable profit 1,000,000, the opened 2019 general rate produces 200,000 and the industrial rate 150,000. The 50,000 difference makes verified classification essential. This comparison gives no right to industrial treatment and no 2026 rate approval.

```oa-check
name: 2019 company sector classification comparison
inputs:
  profit: 1000000
steps:
  - general: profit*0.20
  - industrial: profit*0.15
  - difference: general-industrial
expected:
  general: 200000
  industrial: 150000
  difference: 50000
```

### Loss evidence decision

A business with pre-loss profit500,000 and a300,000 unexpired loss supported by all s.21 conditions has illustrative base200,000. Without the required proof, this workpaper cannot apply that loss: the provisional base remains500,000 and the300,000 claim is held. The example compares evidence outcomes, not discretionary approval.

```oa-check
name: Loss support versus unsupported carryforward
inputs:
  preloss: 500000
  claimed_loss: 300000
steps:
  - supported_base: max(preloss-claimed_loss,0)
  - held_base: preloss
  - base_difference: held_base-supported_base
expected:
  supported_base: 200000
  held_base: 500000
  base_difference: 300000
```

## Ask the client first

- Entity, sector, incorporation and supervision/management facts.
- Basis and accounting periods; all notices, concession or investment approvals.
- Audited accounts, income streams, paid Zakat and expense support.
- Asset register and evidence for each allowance; loss-year books and continuity.
- Related parties, foreign payments, on-account certificates and actual payment proof.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| income-en; selected ss.2,15; PDF 11,27; s.18(1); PDF 29–30; s.18(2); PDF 30–32; s.18(2); PDF 32; s.20; PDF 33–37; s.21; PDF 37–39; s.16(1)–(2); PDF 27–28; s.9(3)–(4); PDF 23; s.38(1),(3)(a)–(b); PDF 58–61, taxpayer definition PDF 59; s.39(4)–(6); PDF 62–63; s.62(1),(6); PDF 90–91; s.63; PDF 92; s.65(1)(i)–(j),(2); PDF 96–97 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf | 2026-11-01 |
| law 21; selected Income Tax Amendment 2019 s.2(2)(c)–(d), PDF 1 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law21.pdf | 2026-11-01 |
| law 32-34; selected Income Tax Amendment 2021 s.2(e), PDF 2 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law32-34.pdf | 2026-11-01 |
| law 38-39; selected Income Tax Amendment 2022 s.2(6)(b), PDF 2; Income Tax Amendment 2022 s.2(1), PDF 1 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law38-39.pdf | 2026-11-01 |

Writer short-quote ledger: [evidence/ledgers/sd-corporate-income-tax.md](../../evidence/ledgers/sd-corporate-income-tax.md). Source hashes and actual read scopes are in the Sudan source manifest/read record. Independent review is pending; preserved platform attribution is historical metadata, not a new review of this version.

Legacy-topic controls below refer to the exact original material and line-independent destination records in [the complete old-topic map](../../evidence/ledgers/sd-old-topic-map.md). Each control retains its original rules, figures, groups, procedures and exceptions for source reconciliation. Supported content is replaced above with citations; any remaining original claim under that control is explicitly unconfirmed, not a usable default.

- SD-OLD-024: Section 1 - Scope statement. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-025: Section 2 - Filing requirements. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-026: Sector-differentiated BPT rates. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-028: Step 1 - Determine taxable income. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-029: Step 2 - Apply sector rate. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-030: Step 3 - Apply deductions and credits. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-031: Step 4 - Loss carryforward. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-032: Allowable deductions (Income Tax Act 1986, Art 18(1)(A)). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-033: Non-deductible expenses. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-034: Initial depreciation allowance. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-035: Free Zones and Investment Incentives. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-036: Petroleum Production Sharing Agreement (PSA) regime. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-038: Currency conversion. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-039: Tax exemptions (Schedule 1 and ministerial orders). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-041: Example 1 - Standard manufacturing company. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-042: Example 2 - Bank operating in Sudan. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-043: Example 3 - Company in a Free Zone (investment incentive). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-045: Section 7 - Self-checks. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-046: Section 8 - Reference material. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-047: PROHIBITIONS. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.

Not yet confirmed: Complete later enacted chain and current sector rates, full 2021 income regulations, depreciation implementation, agricultural classification/base, petroleum 35%, tobacco 30%, banking 30% and insurance special treatment, current concessions and production-sharing agreements; investment 5 year holidays, free-zone/customs/VAT incentives and 20% initial allowance; group consolidation, specific bad-debt conditions, audited-return exceptions, current self-assessment and instalment timetable; resident 4–15%/nonresident 14% collection rates, dividend/interest/royalty finality and specific foreign credits. All those legacy topics remain held rather than silently omitted. Current forms, payment channels and sanctions also remain incomplete. Residual claims in all legacy-topic controls listed above remain held until individually reconciled.

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
