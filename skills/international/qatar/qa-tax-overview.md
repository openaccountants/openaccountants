---
name: qa-tax-overview
description: >
  Qatar individual income tax and taxable business income for 2026, covering
  non-Qatari sole traders, independent professionals, rental activities, Qatari
  and GCC exemptions, non-business investments and business-asset disposals.
  Use for Qatar personal tax, self-employed consultants, freelancers, individual
  business profit, professional expense elections, rental income and departure
  filings. Distinguishes excluded employment remuneration from taxable activities,
  provides the ordinary actual-expense and professional deemed-expense calculations,
  and explains exemptions, loss carryforward, registration, returns, penalties
  and foreign-income routing. Preserves the existing overview slug while supplying
  the pack's individual income-tax computation. Treaty-specific conclusions and
  special-regime computations require separate analysis.
jurisdiction: QA
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.1
---

# Qatar individual income tax and business income v0.1

## Who this applies to

Qatar excludes salaries, wages, allowances and similar employment remuneration
from the income-tax law under promulgation art. 2(3). This is an **exclusion**,
not a universal 0% rate for every individual. Non-Qatari sole traders and
independent professionals can have taxable Qatar-source business or rental
income: ITL arts. 1–3. A residence permit does not turn freelance fees into wages.

ITL art. 1 residence tests include an available permanent home, presence exceeding
183 days in the year or Qatari nationality; treaty residence is separately tested.
ITL art. 4(12) exempts the gross income of Qatari natural persons resident in
Qatar. GCC citizens receive the same exemptions and conditions under ER
art. 2(14) and Law 9/1989. Verify nationality, residence and the actual income
recipient rather than applying a company-ownership exemption to every individual.
Sources: [current ITL, promulgation art. 2 and arts. 1–4](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065), [ER art. 2](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35).

## Rates, bands and thresholds

| Item | Amount/test | Year | Official article |
|---|---|---|---|
| Ordinary taxable individual business income | 10% | 2026 | [ITL art. 9](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Independent-profession expense election | Deduct 30% of gross professional income instead of all actual allowable costs; tax base 70% | 2026 | [ER art. 19](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Small non-mechanised craft exemption | Gross income no more than QAR 200,000, average workforce no more than 3, one establishment; all conditions required | 2026 | [ITL art. 4(9); ER art. 2(7)](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065) |
| Business losses | Carry forward at most 5 subsequent years; no exempt-source losses | 2026 | [ER art. 5(4)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Approved cash basis | Previous-period gross income no more than QAR 1,000,000; GTA application/approval | 2026 | [ER art. 4(2)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |

## The base

1. Separate employment remuneration, taxable activity, investment income and
   disposals. Activity includes professions, trade and exploitation of movable
   or immovable property: ITL art. 1. Rental receipts are not employment wages.
2. Test each exemption. ITL art. 4(2) exempts bank interest/returns for natural
   persons who do not conduct a taxable activity; art. 4(4) exempts natural-person
   real-estate/securities disposal gains when not business assets. Do not apply
   that capital-gains exemption to rental income or to disposal of a business
   asset. Qualifying agriculture/marine fishing under art. 4(10) does not exempt
   complementary industrial/commercial operations: ER art. 2(8).
3. For the craft exemption prove all three conditions. ER art. 2(7) excludes
   small hand tools from the machine concept, calculates average workers using
   worker-days divided by 360 and disregards storage-only establishments for
   the establishment count. A professional consultant does not qualify merely
   because turnover is small.
4. **Actual-expense route:** take accrued taxable receipts and gains, deduct
   actual documented necessary business expenses for the year, replace book
   depreciation with eligible tax depreciation, and exclude personal costs,
   capital improvements, fines and costs of exempt income. Proprietor/spouse/
   children remuneration and interest paid on the proprietor's own deposits
   are barred: ITL arts. 7–8; ER arts. 5–6, 10–18. Use
   [qa-corporate-income-tax](qa-corporate-income-tax.md) for the common expense,
   asset, provision and loan limits; the same ordinary tax-base rules apply.
5. **Professional election:** a person independently using scientific, technical
   or practical expertise can request the ER art. 19 30% expense deduction in
   writing/electronically for the year. Silence for 60 days is acceptance; the
   election continues until cancelled by a request attached to the return.
   Compute `gross professional income × 70% × 10%` before any separately
   established eligible prior loss/credit. Do not also deduct actual expenses
   or depreciation, or apply the election automatically to a retailer/landlord.
6. Offset proved unexpired taxable-business loss vintages against positive
   net income, within ER art. 5(4)'s five-year window; do not use losses from
   exempt income. Record the chosen expense route and loss use in the working
   paper. Multiply the final taxable base by 10%, then apply any qualifying
   foreign tax credit under ITL art. 20.
7. Business-asset disposals use `max(consideration, market value) - cost` for
   non-depreciable assets and minus net book value for depreciable assets:
   ER art. 5(2). Departure is not an automatic tax-free disposal. See the
   cross-border Guide for cessation, migration and final filing.

Sources: [ITL arts. 1–9 and 20](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065), [ER arts. 2, 4–20](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35).

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

A nonresident's PE income and final gross-payment withholding require separate
classification. For a resident-managed Qatari project, specified foreign income
is within ITL arts. 2 Bis–2 Bis/5; do not label the entire system strictly
territorial. Foreign PE income, foreign gains/directors' fees, substance and
foreign-tax credits follow their actual conditions. Use
[qa-cross-border-tax](qa-cross-border-tax.md) for that computation and the
applicable treaty. Qatar employment exclusion does not determine whether the
salary is taxable in another country.

Social insurance is separate: see [qa-payroll-social](qa-payroll-social.md) for
Qatari/GCC employees, optional Qatari self-employed coverage and expatriates.

## Two worked examples that recompute

### 1. Non-Qatari sole trader using actual expenses

A non-Qatari ordinary sole trader earns QAR 300,000 taxable business receipts.
Documented allowable costs are QAR 100,000 and eligible tax depreciation is
QAR 20,000. A further QAR 10,000 private expense is excluded, not deducted.
An evidenced unexpired QAR 30,000 business loss reduces the QAR 180,000 net
income to QAR 150,000; tax is QAR 15,000. No craft, nationality or treaty
exemption is assumed. Authority: ITL arts. 7–9; ER arts. 5–6 and 14–16.

```oa-check
name: Qatar individual business actual costs and loss
inputs:
  taxable_receipts: 300000
  allowable_costs: 100000
  tax_depreciation: 20000
  eligible_prior_loss: 30000
  rate: 0.10
steps:
  net_income: taxable_receipts - allowable_costs - tax_depreciation
  loss_used: min(eligible_prior_loss, max(0, net_income))
  taxable_income: max(0, net_income - loss_used)
  tax: taxable_income * rate
expected:
  net_income: 180000
  loss_used: 30000
  taxable_income: 150000
  tax: 15000
```

### 2. Accepted professional election and excluded wages

A non-Qatari independent professional has QAR 400,000 professional fees and
QAR 120,000 separate genuine employment remuneration. Assume the ER art. 19
election has taken effect and no loss/credit/exemption applies to the fees.
Only the professional fees enter this computation; 30% deemed costs are
QAR 120,000, taxable professional income QAR 280,000 and tax QAR 28,000.
Actual expenses cannot be deducted again. Authority: promulgation art. 2(3),
ITL art. 9 and ER art. 19.

```oa-check
name: Qatar professional election with separate employment
inputs:
  professional_fees: 400000
  deemed_cost_rate: 0.30
  rate: 0.10
steps:
  deemed_costs: professional_fees * deemed_cost_rate
  taxable_professional_income: professional_fees - deemed_costs
  tax: taxable_professional_income * rate
expected:
  deemed_costs: 120000
  taxable_professional_income: 280000
  tax: 28000
```

## Ask the client first

- What are nationality, domestic/treaty residence and the identity of the actual
  income earner?
- Which receipts are genuine employment, independent fees, rent, investment
  returns or business/private asset gains?
- What records support expenses, asset use, gains and prior loss vintages?
- Is a professional/cash-basis election actually effective, and what application
  and GTA response establish it?
- For a claimed craft exemption, what are tools, gross income, worker-days and
  establishment count?
- What foreign income/tax, PE activity, departure, cessation and outstanding
  filing obligations exist?

## Sources

| Source | URL | Read on |
|---|---|---|
| Current Arabic Income Tax Law 24/2018, including amendments; articles cited above | https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065 | 2026-10-24 |
| Current Arabic ER 39/2019, including amendments; articles cited above | https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35 | 2026-10-24 |
| GTA 2024 English compilation, checked against Arabic and later amendments | https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf | 2026-10-24 |
| Law 22/2024, arts. 3 and 5, general penalties effective 1 January 2025 | https://almeezan.qa/legislations/3643a42a-bdc0-4546-95d6-975557616a1b | 2026-10-24 |
| GTA investor guide, current operational filing instructions | https://www.gta.gov.qa/en/investors-guide | 2026-10-24 |

Not yet confirmed: none within the ordinary scope stated in this Guide.
Special regimes and transaction-specific treaty entitlement require their own
source and factual analysis.

General reference only. A qualified Qatar tax professional must review the
facts, records, elections and applicable law before filing or acting. This is a
source-cited draft, not professional attestation.

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
