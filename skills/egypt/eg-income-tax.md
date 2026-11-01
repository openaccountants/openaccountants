---
name: eg-income-tax
description: Use this skill whenever asked about Egyptian personal income tax for resident individuals, sole proprietors, freelancers, or professionals , to compute, review, or explain it. Trigger on phrases like "Egypt income tax", "ضريبة الدخل", "Egyptian tax brackets", "sole proprietor tax Egypt", "freelancer tax Egypt", "professional income tax Egypt", "إقرار ضريبة الدخل", or any request to prepare or check an Egyptian individual income tax return. ALWAYS read this skill before touching any Egypt personal income tax work.
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Income Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers Egyptian personal income tax (ضريبة الدخل على الأشخاص الطبيعيين) for tax year 2026: employees in outline, sole proprietors (منشأة فردية) and professionals (مهن حرة). Reply in the user's language, English or Arabic. All amounts are in EGP. Tax year: calendar year.

## Who this applies to

- **Residents** (Law 91 art. 2): a person with a permanent home in Egypt; or present more than 183 days, continuous or not, within 12 months; or an Egyptian working abroad and paid from an Egyptian treasury.
- **Scope of the tax** (Law 91 art. 6): annual tax on the total net income of resident and non-resident individuals for income realised in Egypt, from four sources: salaries, commercial or industrial activity, professional or non-commercial activity, and real estate. Art. 5 defines Egyptian-source income. The earlier version of this skill said residents pay on worldwide income; the text of art. 6 does not say that.
- **Not here:** companies (`eg-corporate-tax`); the turnover regime (`eg-sme-tax`); real estate disposals and rents (`eg-real-estate-tax`); withholding (`eg-withholding-tax`); payroll operation (`eg-payroll`); crypto (`eg-crypto-tax`).

## Rates, bands and thresholds

Egypt withdraws the lower bands as income rises. Pick the row by total annual net income, then apply that row's bands to the whole income.

| Item | Amount (EGP) and rate | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Income up to 600,000 | 0 to 40,000: 0%; over 40,000 to 55,000: 10%; over 55,000 to 70,000: 15%; over 70,000 to 200,000: 20%; over 200,000 to 400,000: 22.5%; over 400,000: 25% | Whole annual net income does not exceed 600,000 (Law 91 art. 8, as replaced by Law 7/2024) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf |
| Over 600,000, not over 700,000 | 1 to 55,000: 10%; then 15%, 20%, 22.5%, 25% as above | The 0% band is gone | 2026 | same |
| Over 700,000, not over 800,000 | 1 to 70,000: 15%; then 20%, 22.5%, 25% | The 0% and 10% bands are gone | 2026 | same |
| Over 800,000, not over 900,000 | 1 to 200,000: 20%; then 22.5%, 25% | 0%, 10%, 15% bands gone | 2026 | same |
| Over 900,000, not over 1,200,000 | 1 to 400,000: 22.5%; over 400,000: 25% | 0% to 20% bands gone | 2026 | same |
| Over 1,200,000 | 1 to 1,200,000: 25%; over 1,200,000: 27.5% | Every lower band gone | 2026 | same |
| Rounding | Down to the nearest EGP 10 | Applies to total annual net income before the table | 2026 | same |

| Item | Amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Personal exemption | EGP 20,000 a year | Law 91 art. 13(1) as replaced by Law 7/2024. Art. 13 sits in the salaries chapter; see "Not yet confirmed" for business income | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf |
| Delay charge | Central Bank rate on 1 January before the due date plus 2%; 20.50% on 1 Jan 2026, so 22.50% a year on a date falling in 2026 | Law 91 art. 110; part months and pounds dropped | 2026 | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf |
| Delay charge ceiling | Delay charge or additional tax may not exceed 100% of the principal tax | Law 206/2020 new article, added by Law 7/2025 | 2026 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf |
| Built property disposal | 2.5% of gross value, no deduction, paid within 60 days | Law 91 art. 42 as replaced by Law 151/2026; the correction notice makes it "built" property and fixes the article number. Detail in `eg-real-estate-tax` | 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf |
| Dividends to non-resident individuals | 10%; 5% if the securities are listed in Egypt | Dividend article of Law 91 as replaced by Law 151/2026 art. 1; no costs deducted | 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Listed Egyptian securities, capital gains | Exempt; losses not deductible and not carried forward | Law 91 art. 31 item 7, added by Law 151/2026 art. 2. Not exempt where the disposal delists the company | From 29 Jul 2026 | same |
| Unlisted securities and company shares, capital gains | Taxed; a non-resident seller computes and pays within 60 days | Unlisted-gains articles of Law 91 as replaced by Law 151/2026 art. 1; gain is price less acquisition cost and brokerage | From 29 Jul 2026 | same |

Listed share gains tax left unpaid for 16 June 2023 to the law's start date is forgiven (Law 151 art. 5).

## The base

1. Take net income by source. For a business or profession: receipts less costs needed to earn them, from regular books backed by documents (Law 91 arts. 18, 19, 28).
2. Add the sources into total net income and round down to EGP 10.
3. Pick the table row and apply the bands.
4. Credit tax withheld and advance payments.

**Costs.** Bad debts need serious collection steps: a payment order, a first-instance judgment, or a claim in bankruptcy enforcement (art. 28 first para. item 4 as replaced by Law 151). A personal expense, a fine and income tax itself are not costs.
**Donations by professionals** (art. 27): deductible up to net annual income for government bodies; up to 10% of net income for registered Egyptian charities, schools and hospitals under state supervision and Egyptian research bodies; not deductible again against another source.
**Losses** (art. 29): carried forward to the fifth following year at the latest.
**New professionals** (art. 31 item 5): members of a professional syndicate are exempt for three years from starting the profession.
**Authors** (art. 31): income from writing and translating religious, scientific, cultural and literary books and articles is exempt, except sale for audio or video production.
**Health contribution** (art. 23 item 10, added by Law 151; art. 33 item 5 for the matching item): the solidarity contribution under the Universal Health Insurance Law art. 40(9) is a deductible item.
**Egyptian-source fees of a non-resident:** see `eg-withholding-tax`.

### Classify transactions

### Income (دخل / إيرادات)

**Income keyword table**

| Keyword (AR) | Keyword (EN) | Treatment |
| --- | --- | --- |
| إيراد / مبيعات / تحصيل | revenue / sales / receipt | Business income (commercial/industrial) |
| أتعاب / استشارات | fees / consulting | Professional (non-commercial) income |
| تحويل وارد / إيداع عميل | incoming transfer / client deposit | Income: confirm it is trading receipt |
| مرتب / راتب | salary / payroll | Employment income (separate computation) |
| إيجار مستحق | rent received | Real-estate revenue (separate category) |
| فوائد / عوائد | interest / yield | Investment income: exclude from business profit |

### Deductible expenses (مصروفات قابلة للخصم)

**Deductible expenses table**

| Keyword (AR) | Keyword (EN) | Treatment |
| --- | --- | --- |
| إيجار مكتب / محل | office / shop rent | Deductible if business-use |
| رواتب الموظفين | staff wages | Deductible |
| كهرباء / مياه / إنترنت | utilities / internet | Deductible (business portion) |
| مشتريات / بضاعة | purchases / stock | Cost of goods sold |
| إهلاك أصول | depreciation | Deductible per law schedules |
| تأمينات اجتماعية | social insurance | Deductible employer/owner contributions |
| دعاية وإعلان | advertising | Deductible if documented |
| صيانة | maintenance | Deductible |

### Non-deductible / disallowed (غير قابل للخصم)

**Non-deductible table**

| Keyword (AR) | Keyword (EN) | Treatment |
| --- | --- | --- |
| مصاريف شخصية / سحب شخصي | personal / owner drawings | **Non-deductible** |
| غرامات / جزاءات | fines / penalties | **Non-deductible** |
| ضريبة الدخل | income tax paid | **Non-deductible** |
| مصروف بدون فاتورة | expense without invoice | **Non-deductible** (no support) |
| توزيعات أرباح موزعة | distributed profits/dividends | Not an expense |

### Exclusions (مستبعد من الربح)

**Exclusions table**

| Item (AR) | Item (EN) | Treatment |
| --- | --- | --- |
| إيرادات معفاة | exempt income | Exclude from taxable base |
| دخل خاضع لخصم نهائي | income under final WHT | Exclude from progressive base (already taxed) |
| رأس مال / قروض واردة | capital injection / loan in | Not income |


### Working paper

**Excel working paper columns**

| Col | Header (EN) | Header (AR) |
| --- | --- | --- |
| A | Date | التاريخ |
| B | Description | البيان |
| C | Counterparty | الطرف الآخر |
| D | Category (income/expense/non-deductible/exclusion) | التصنيف |
| E | Amount EGP | المبلغ |
| F | Document ref (e-invoice no.) | رقم الفاتورة الإلكترونية |
| G | Deductible? (Y/N) | قابل للخصم؟ |
| H | Note / disallowance reason | ملاحظات |


Keep one row per band so a reviewer can trace the tax. Summary order: receipts, deductible costs, net profit, insurance relief, taxable income, tax from the table, credits, payable.

### Reading bank statements

Egyptian statements (كشف حساب) appear in Arabic, English, or both. Common formats:

- **National Bank of Egypt: البنك الأهلي المصري (NBE):** Arabic-first; debit = مدين, credit = دائن. Look for مبيعات / تحصيل (income) and سحب / مدفوعات (payments).
- **Banque Misr: بنك مصر:** bilingual; transfers labelled تحويل (transfer), إيداع (deposit), سحب (withdrawal).
- **Commercial International Bank: CIB (البنك التجاري الدولي):** often English-first with Arabic memo lines; POS/merchant settlements show as "POS Settlement" or تسوية نقاط بيع → business income.

### Key Arabic banking terms

**Key Arabic banking terms table**

| Arabic | English |
| --- | --- |
| كشف حساب | bank statement |
| رصيد | balance |
| مدين | debit |
| دائن | credit |
| إيداع | deposit |
| سحب | withdrawal |
| تحويل | transfer |
| تحصيل | collection / receipt |
| مرتجع | refund / return |
| رسوم بنكية | bank charges (deductible business expense) |
| فائدة دائنة | interest earned (investment income: exclude from business profit) |
| نقاط البيع | point of sale (POS) |

Reconcile statement receipts to declared revenue; unexplained deposits should be queried, not assumed taxable or non-taxable (apply R-EG-1/R-EG-2 discipline).


## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Register | Tell ETA within 30 days of starting: form 1 (individual) with documents; ETA reviews, then issues the registration number and tax card | Law 91 notice article; ETA Services Guide, registration |
| Annual return | Before 1 April of the following year for individuals (Law 206/2020, returns chapter) | Law 206 |
| Return even if exempt | The return is still due for exempt periods | Law 206 |
| Incomplete return | A return missing the form's tables is not counted as filed | Law 206 |

**Steps for a business or professional individual:**
1. Log in on the ETA tax system (https://workspace.eta.gov.eg/workspace/dashboard for merged offices) or https://eservice.incometax.gov.eg/etax for offices not yet merged.
2. Decide the regime first: to use the turnover regime file form 10/1 طلبات (see `eg-sme-tax`).
3. Complete the annual return and every attached table on the form.
4. Submit before 1 April, keep the confirmation, and pay any balance. ETA's published guide for the individual return's box numbers was not read; see "Not yet confirmed".

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Return and payment late by up to 60 days, or a wrong return showing more tax | Fine EGP 3,000 to 50,000 plus the tax; trebled on repeat | Law 206, Part 9 |
| No return for over 60 days past the due date | Fine EGP 5,000 to 200,000; doubled if repeated within three years | Law 206, Part 9 |
| Not keeping books for the required period | Fine up to EGP 50,000 | Law 206, Part 9 |
| Evasion | Prison one to three years and fine EGP 50,000 to 250,000, or either | Law 206, Part 9 |
| Late payment | Delay charge above, capped at 100% of principal | Law 91 art. 110; Law 7/2025 |
| Settling a crime with no tax at stake | Payment between half and twice the minimum fine before prosecution | Law 206 new article, added by Law 7/2025 |

Open disputes: Law 152/2026 renews the Law 79/2016 dispute committees to 31 December 2026. Apply to ETA on its form, or free on its portal (MoF decision 450/2026).

## Cross-border points

- Non-residents pay on income realised in Egypt (art. 6); art. 5 lists it.
- Treaties: the ETA treaty list is the starting point. Do not apply a treaty rate or a foreign tax credit here; route to `eg-withholding-tax`.
- Non-resident sale of unlisted shares or company interests: compute and pay within 60 days. Treasury bill gains of non-residents are outside this tax (same article).

## Two worked examples that recompute

**Case 1. Freelancer, net income EGP 90,000.** Row "up to 600,000". 10% on 15,000 = 1,500; 15% on 15,000 = 2,250; 20% on 20,000 = 4,000. Tax 7,750. No personal exemption is taken, for the reason under Sources.

```oa-check
name: Freelancer net income EGP 90,000
inputs:
  income: 90000
steps:
  - b10: (55000 - 40000) * 0.10
  - b15: (70000 - 55000) * 0.15
  - b20: (income - 70000) * 0.20
  - tax: b10 + b15 + b20
expected:
  tax: 7750.00
```

**Case 2. Decision: general system or turnover regime.** Developer, turnover 1,500,000, costs 150,000, profit 1,350,000. General: top row, 25% on 1,200,000 = 300,000, 27.5% on 150,000 = 41,250, total 341,250. Turnover regime: 0.5% = 7,500. The turnover regime wins by 333,750, before the five-year lock-in in `eg-sme-tax`. It fails if at least 90% of turnover is consulting for one or two clients.

```oa-check
name: General system against turnover regime, turnover 1.5m
inputs:
  turnover: 1500000
  costs: 150000
steps:
  - profit: turnover - costs
  - general: 1200000 * 0.25 + (profit - 1200000) * 0.275
  - simplified: turnover * 0.005
  - saving: general - simplified
expected:
  general: 341250.00
  simplified: 7500.00
  saving: 333750.00
```

The row step matters: income of 610,000 has no 0% band, so tax is 5,500 + 2,250 + 26,000 + 45,000 + 52,500 = 131,250; income of 600,000 pays 124,750. A rise of 10,000 costs 6,500.

## Ask the client first

1. Resident? Which test in art. 2?
2. Which sources: salary, business, profession, rent?
3. Total net income for 2026, and are regular books kept?
4. Is the taxpayer in the Law 6/2025 regime, or was a request filed? If yes, stop and use `eg-sme-tax`.
5. Tax withheld, advance payments, and insurance premiums paid.
6. Any open dispute or unfiled year?

Refuse to help hide receipts, invent costs or under-declare. Do not present output as a filed return or as a professional sign-off.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 91 of 2005, original text: arts. 2, 6, 13, 18, 19, 25, 27, 28, 29, 31 (OCR, figures confirmed only where a later law restates them) | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-01 |
| Law 7 of 2024, arts. 8 and 13(1) (bands, exemption; page images read; the ETA file carries an HTML page after the PDF end and opens once trimmed) | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf | 2026-11-01 |
| Law 175 of 2023 (previous band table, superseded) | https://eta.gov.eg/sites/default/files/2024-03/law_no.175-2023.pdf | 2026-11-01 |
| Law 151 of 2026, whole text; Gazette 30 bis (a), 28 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-01 |
| Correction notice to Laws 149, 150, 151 of 2026; Gazette 32 bis, 8 Aug 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-01 |
| Unified Tax Procedures Law 206 of 2020: return deadlines, Part 9 offences (OCR; article numbers for the offences not legible) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-01 |
| Law 7 of 2025, whole text (OCR) | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-01 |
| Law 152 of 2026, whole text (OCR) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.152.of_.2026.pdf | 2026-11-01 |
| MoF decision 450 of 2026, arts. 1 and 2 (OCR) | https://eta.gov.eg/sites/default/files/2026-08/mof.qarar_.no_.450.of_.2026.pdf | 2026-11-01 |
| ETA circular 1 of 2026 (Central Bank rates; page image read) | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | 2026-11-01 |
| ETA Services Guide, 2nd edition: registration and section 18 only | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | 2026-11-01 |

Not yet confirmed: whether the EGP 20,000 personal exemption (art. 13, salaries chapter) comes off business and professional income; the old skill deducted it, and Law 7/2024 art. 2 sets a start date for those taxpayers, but the examples here do not deduct it until an official page says so. The cap on life, health and pension premium relief: the old figure was the lower of 15% of net revenue or EGP 10,000, the 2005 text differs, and the amending law was not read. The non-resident's right to the exemption. Whether art. 74 is the current article number for the 30-day notice. The box numbers of the individual annual return. The deemed cost percentage where no regular books are kept (art. 28, OCR unclear). Depreciation schedules. Treatment of mixed personal and business costs beyond the general rule. Exact ETA forms for the employee annual settlement belong to `eg-payroll`.

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
