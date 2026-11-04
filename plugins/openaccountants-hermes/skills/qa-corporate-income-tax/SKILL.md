---
name: qa-corporate-income-tax
description: "Qatar ordinary corporate income tax for 2026, covering resident legal persons, foreign-owned and mixed-ownership mainland companies, Qatar permanent establishments, ownership exemptions, the accounting-to-tax reconciliation, deductions, depreciation, related-party financing, losses and foreign income. Use for Qatar company tax calculations, corporate returns, tax registration, taxable profits, business asset disposals, deduction limits and loss carryforward. Separates the ordinary income tax from petroleum agreements, QFC and free-zone regimes and Pillar Two. Includes filing and penalty rules, two independently checkable computation examples, and links to the individual, transfer-pricing and cross-border Guides for specialist computations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/qa-corporate-income-tax"
  jurisdiction: "QA"
  tax_year: "2026"
  last_updated: "2026-10-28"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Qatar corporate income tax v0.1

## Who this applies to

This Guide computes ordinary mainland income tax under Law 24/2018 (ITL) and
ER 39/2019 for 2026. Read the [current Arabic law](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) and [ER](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35); the
English compilation misnumbers some exemption subclauses and mistranslates ER
art. 6. The Arabic text controls.

Identify the taxpayer and residence under ITL art. 1, its Qatar-source income
under arts. 2–3, and any foreign income included by arts. 2 Bis–2 Bis/5. Residence
is not a blanket foreign-income exemption. A foreign enterprise with a Qatar PE
uses ER art. 7, subject to the applicable treaty; see
[qa-cross-border-tax](qa-cross-border-tax.md) for attribution and cessation.

ITL art. 4(13) exempts qualifying Qatar-resident legal persons wholly owned by
Qataris. Art. 4(14) exempts profit shares attributable to the specified Qatari
owners, including qualifying look-through shares. ER art. 2(10)–(12) requires
residence, accounting records, beneficial ownership and ownership throughout the
relevant period as applicable. GCC citizens receive the same exemptions and
conditions under ER art. 2(14) and Law 9/1989. Do not exempt the whole business
because it has a Qatari shareholder. ITL art. 33 also conditions an entity's tax
advantage on actual management in Qatar.

Petroleum/petrochemical agreements (ITL art. 9 minimum 35%), other government
agreements, QFC/free-zone specialist regimes, regulated-bank/insurer special
provisions and detailed Pillar Two computations are separate scopes. The
[GTA minimum-tax framework](https://www.gta.gov.qa/en/global-minimum) operates
in addition to ordinary income tax.

## Rates, bands and thresholds

| Item | Amount/test | Year | Official article |
|---|---|---|---|
| Ordinary rate | 10% of taxable income | 2026 | [ITL art. 9](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Business loss carryforward | At most 5 subsequent tax years; no exempt-source losses | 2026 | [ER art. 5(4)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Cash-basis application | Previous-period gross income not exceeding QAR 1,000,000; GTA approval required | 2026 | [ER art. 4(2)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Related-party loan ceiling for interest deduction | Loans not exceeding 3 times recorded equity, plus economic-benefit and agreement conditions | 2026 | [ER art. 10(1)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Hospitality/entertainment etc. | Higher of 2% of pre-deduction net income and QAR 500,000; overseas component also capped at QAR 500,000 | 2026 | [ER art. 8(1)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Qualifying Qatar donations/zakat | Up to 3% of pre-deduction net income | 2026 | [ER art. 8(2)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Low-value fixed asset full depreciation | Asset value not exceeding QAR 5,000 in first year of use | 2026 | [ER art. 16(3)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Common annual depreciation maxima | Durable buildings 5%; vehicles 20%; office furniture/equipment 15%; computers/software 33.33% | 2026 | [ER art. 16(1), asset table](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |

## The base

Prepare a traceable tax reconciliation, not `turnover × 10%`:

1. Start with accrual-accounting profit. Revenue arises when receivable and
   expenses when the obligation arises, regardless of cash payment. An approved
   cash-basis application is available within the table's limit; silence for
   60 days is rejection. Long-term contracts exceeding 18 months use work
   completed: ER art. 4.
2. Reconcile gross receipts and gains, including business-asset disposals.
   Non-depreciable gain is `max(consideration, market value) - cost`;
   depreciable gain is `max(consideration, market value) - net book value`.
   Shares use the documented capital interest under ER art. 5(2). Remove only
   exemptions actually established under ITL art. 4, including qualifying local
   dividends under art. 4(8). See the cross-border Guide for foreign gains,
   foreign PE income, substance and credit allocation.
3. Deduct actual documented expenses necessary for the activity, relating to
   this year, recorded in the accounts and not capital improvements: ITL art. 7,
   ER art. 5(3). Add back personal/non-business costs, unlawful amounts, fines,
   recovered costs not included in receipts, and costs attributable to exempt
   income. Shared costs are allocated using accurate records; absent those,
   ER art. 6 uses taxable revenue divided by total revenue. The English book
   incorrectly suggests exempt-income costs are deductible; Arabic ER art. 6
   expressly prohibits them.
4. Add back remuneration barred by ITL art. 8(6), including the proprietor,
   spouse/children, partners and a majority-owner LLC manager. ER art. 9 allows
   board members' salaries in their separate capacity as employees of the same
   company, not an automatic deduction for board fees.
5. Apply the hospitality and donation limits separately using each provision's
   pre-deduction base; cap the deduction at actual eligible spend. Foreign
   hospitality has its additional cap. Do not turn the QAR 500,000 floor in the
   hospitality ceiling into a minimum spend or a flat deduction.
6. Replace book depreciation with eligible tax depreciation. Land and goodwill
   are excluded; the asset must be owned, depreciable and used for taxable
   business. Begin when actually used, apply business-use allocation and the
   ER art. 16 asset-class ceiling. Actual accounting depreciation below that
   ceiling does not justify inventing a larger deduction. Keep separate asset
   and disposal schedules: ER arts. 14–18. Industrial shift uplifts and special
   assets require their specified conditions, not an automatic standard rate.
7. Check financing and other limits. For a single uniform-rate related loan,
   deductible interest cannot exceed interest on `min(actual loan, 3 × equity)`
   and must meet the economic-benefit/agreement and arm's length conditions.
   Do not use that simplified expression for multiple facilities without a
   facility-level allocation. Owner interest is barred; foreign local-agent
   commissions are capped at 3% of actual activity revenue: ER arts. 10 and 20.
   Income taxes and tax borne for a nonresident are not business deductions:
   ER art. 11. Foreign income-tax relief is a credit where ITL art. 20 permits it.
8. Ordinary commercial provisions are not automatically deductible. ER art. 12
   bad debts require prior taxable recognition, at least 24 months overdue,
   provision, unsuccessful legal collection, auditor write-off certificate and
   the required return list; recoveries are taxable. ER art. 13 confines
   deductible provisions to its bank/insurer categories and conditions.
9. Maintain loss vintages and evidence. Offset eligible unexpired business losses
   against net taxable income, never below zero. A 2021 loss is usable only
   through 2026 under the five-year rule; no carryback or perpetual pool is
   supplied by ER art. 5(4). Allocate exempt/taxable profit shares and associated
   expenses consistently, without deducting the same loss against both shares.
10. Apply 10% to the final taxable share, then qualifying foreign-tax credits
    within the Qatar-tax limit. Reconcile instalments/withholding/amounts paid
    separately from the tax-base computation. Exempt income produces no foreign
    credit. Use [qa-cross-border-tax](qa-cross-border-tax.md) for the full
    foreign-income and credit working.

Authority for this computation: [ITL arts. 2–9, 20 and 33](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) and
[ER arts. 2, 4–20 and 52–64](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35). Related-party prices must be supported
under [qa-transfer-pricing](qa-transfer-pricing.md), independently of deductibility.

## Deadlines and filing

Register through Dhareeba within 60 days from the earliest approval to begin,
commercial registration or first income, or on the date of registration for
another tax purpose where applicable: [ER art. 25](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35). File the ordinary
annual return within four months after the accounting period ends, and pay the
return tax on the day of submission: [ER art. 29; ITL art. 20](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35). A calendar
2026 return is therefore due by 30 April 2027 absent a valid extension.

An extension request normally goes in at least 60 days before the final filing
date, with reasons; ER art. 30 permits up to four additional months and treats
30 days without response as rejection. Do not assume an annual extension changes
withholding or disposal deadlines. Notify tax-obligation changes within 30 days;
cessation/transfer has a 30-day notice and return rule under ER arts. 27–29.

Keep the financial statements, ledger-to-tax reconciliation, depreciation and
loss schedules, ownership/exemption evidence and relevant withholding/related-party
schedules. ER art. 33 requires audited accounts where capital **exceeds**
QAR 200,000, total income **exceeds** QAR 500,000, or the main office is abroad.
The [current GTA investor guide](https://www.gta.gov.qa/en/investors-guide#pane-faq_foreign_investors),
under its accounting-office FAQ, gives a different operational summary: exempt
100% Qatari/GCC-owned companies need a full audited return at capital at least
QAR 1 million **or** annual income at least QAR 5 million; foreign/mixed-owned
or overseas companies need audited returns regardless of size. These are not
the ER art. 33 thresholds and must not silently replace the statutory test.
Use the statute for the legal audit obligation and the GTA's current ownership/
form instructions for submission; do not waive a statutory audit solely because
an exempt company's portal offers a simplified form. Retain any specific GTA
instruction authorising a different treatment in the taxpayer's file. Neither
a simplified form nor a tax exemption means no return.
Records are retained for ten years following the year concerned, and longer
while a dispute continues: [ER arts. 32–36](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35).

## Penalties and interest

| Breach | Financial penalty | Source |
|---|---|---|
| Late ordinary return | QAR 500 per day, capped at QAR 180,000 | [ITL art. 24(1)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Late tax payment | 2% of unpaid tax for each month or part, capped at the unpaid tax | [ITL art. 24(2)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Registration/notification breach | QAR 20,000 | [ITL art. 24(3)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Exempt taxpayer fails to file required return/documents | QAR 10,000 | [ITL art. 24(4)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Audited accounts/books breach | QAR 30,000 | [ITL art. 24(5)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Specified records/retention/provision/destruction breach | QAR 30,000 | [ITL art. 24(10)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Requested information/document not supplied on time | QAR 200 per missing item, capped at QAR 72,000 | [ITL art. 24(11)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Incomplete/incorrect information | QAR 100 per item, maximum QAR 10,000 per relevant submission; if it causes incorrect tax, the provision imposes 50% of the resulting unpaid tax | [ITL art. 24(12)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |

Clauses (10)–(12) apply from 1 January 2025 under [Law 22/2024 arts. 3 and 5](https://almeezan.qa/legislations/3643a42a-bdc0-4546-95d6-975557616a1b).
They are general income-tax provisions, not confined to Pillar Two. Art. 24(10)
also addresses the last managers/persons in charge failing to retain records for
five years after dissolution. Do not shorten a longer existing retention or
active-dispute obligation, or assume all offence amounts stack automatically.

## Cross-border points

For a Qatar PE use the separate-enterprise attribution rule, the domestic
same/similar business extension subject to treaty, and the bar on notional
head-office charges under ER art. 7. Do not retain a repealed generic 3%
head-office cap from older summaries in place of the amended rule.

Foreign real estate, distributions, interest, royalties, technical-service fees
and other listed services require ITL arts. 2 Bis–2 Bis/5 analysis. Foreign gains
and directors' fees exemptions have foreign-tax/substance conditions in ER
art. 2(5). See [qa-cross-border-tax](qa-cross-border-tax.md) for the actual
inclusion/exemption/credit sequence and migration/disposal computation.
Withholding on payments to nonresidents is a different gross-payment obligation.

## Two worked examples that recompute

### 1. Book profit, disallowances and an unexpired loss

A wholly foreign-owned ordinary company has QAR 600,000 book profit after
QAR 10,000 fines, QAR 20,000 private expenses and QAR 60,000 book depreciation.
Eligible tax depreciation is QAR 40,000. It has a documented QAR 100,000
unexpired taxable-business loss. Taxable income is QAR 550,000 and ordinary
tax QAR 55,000. No ownership exemption or foreign credit is assumed.
Authority: ITL arts. 7–9; ER arts. 5, 14–16.

```oa-check
name: Qatar corporate profit reconciliation and loss
inputs:
  book_profit: 600000
  fines: 10000
  private_expenses: 20000
  book_depreciation: 60000
  tax_depreciation: 40000
  eligible_loss: 100000
  rate: 0.10
steps:
  adjusted_profit: book_profit + fines + private_expenses + book_depreciation - tax_depreciation
  loss_used: min(eligible_loss, max(0, adjusted_profit))
  taxable_income: max(0, adjusted_profit - loss_used)
  tax: taxable_income * rate
expected:
  adjusted_profit: 650000
  loss_used: 100000
  taxable_income: 550000
  tax: 55000
```

### 2. Mixed ownership and excessive related-party financing

Assume all exemption residence/beneficial-ownership/full-period conditions are
proved for a 40% Qatari profit share. The remaining 60% is taxable. Book profit
is QAR 1,000,000 after QAR 200,000 interest on a uniform-rate QAR 4,000,000
related loan. Recorded equity is QAR 1,000,000. Assume economic benefit,
agreement and arm's length pricing are established, and no other adjustments,
losses or credits. Only QAR 150,000 interest passes the 3:1 loan ceiling;
QAR 50,000 is added back. Tax is QAR 63,000 on the taxable share.
Authority: ITL arts. 4(14), 7–9; ER arts. 2 and 10.

```oa-check
name: Qatar mixed ownership and related loan ceiling
inputs:
  book_profit: 1000000
  interest: 200000
  loan: 4000000
  equity: 1000000
  equity_multiple: 3
  taxable_share: 0.60
  rate: 0.10
steps:
  permitted_loan: min(loan, equity * equity_multiple)
  permitted_interest: interest * permitted_loan / loan
  addback: interest - permitted_interest
  adjusted_profit: book_profit + addback
  taxable_income: adjusted_profit * taxable_share
  tax: taxable_income * rate
expected:
  permitted_loan: 3000000
  permitted_interest: 150000
  addback: 50000
  adjusted_profit: 1050000
  taxable_income: 630000
  tax: 63000
```

## Ask the client first

- What entity/regime, residence, ownership chain, beneficial owners and ownership
  dates support any exemption?
- What are the year end, accounts, ledger, asset register and prior loss vintages?
- Which expenses involve owners/directors, related finance, hospitality,
  donations, provisions, capital improvements or exempt income?
- What foreign income, foreign PEs, taxes paid/refunded and substance evidence exist?
- What nonresident payments, related transactions, restructurings or asset
  transfers occurred?
- Which Dhareeba forms, GTA instructions, audit requirements and filing extensions
  apply to this taxpayer?

## Sources

| Source | URL | Read on |
|---|---|---|
| Current Arabic Income Tax Law 24/2018, including amendments; articles cited above | https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065 | 2026-10-24 |
| Current Arabic ER 39/2019, including amendments; articles cited above | https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35 | 2026-10-24 |
| GTA 2024 English compilation, checked against Arabic and later amendments | https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf | 2026-10-24 |
| Law 22/2024, arts. 3 and 5, general penalties effective 1 January 2025 | https://almeezan.qa/legislations/3643a42a-bdc0-4546-95d6-975557616a1b | 2026-10-24 |
| GTA investor guide and operational return instructions | https://www.gta.gov.qa/en/investors-guide | 2026-10-24 |

Not yet confirmed: none within the ordinary scope stated in this Guide.
Special regimes and transaction-specific treaty entitlement require their own
source and factual analysis.

General reference only. A qualified Qatar tax professional must review the
facts, records, elections and applicable law before filing or acting. This is a
source-cited draft, not professional attestation.

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-28. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `qa-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/qa-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
