---
name: vn-tax-overview
description: >
  Vietnam tax system at a glance for 2026. Use to find which Vietnam skill
  answers a question and for the headline figures that changed in 2025 and
  2026 - new laws on personal income tax (Law 109/2025/QH15), corporate income
  tax (Law 67/2025/QH15), tax administration (Law 108/2025/QH15), the April 2026
  amending Law 09/2026/QH16, the VND 1 billion threshold for household
  businesses and very small companies (Decree 141/2026), the end of the
  business licence fee and the mid-2026 social insurance cap. Tier 2, not
  reviewed by an accountant.
version: "2.0"
jurisdiction: VN
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Vietnam Tax Overview v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking a general question about Vietnamese tax for 2026: individuals, household businesses, companies and foreign investors. Vietnam taxes at national level through the Tax Department (Cục Thuế) of the Ministry of Finance. The tax year is the calendar year (companies may notify a different financial year) and the currency is the dong (VND). Residents are taxed on worldwide income; non-residents on Vietnam-source income.

| Question | Skill |
| --- | --- |
| Salary, self-employment, household business, capital gains of individuals | [vietnam-pit](vietnam-pit.md) |
| Company tax, incentives, losses | [vn-corporate-income-tax](vn-corporate-income-tax.md) |
| VAT rates, registration, returns, the temporary VAT cut | [vietnam-vat](vietnam-vat.md) |
| Social, health and unemployment insurance, payroll withholding | [vn-payroll-social](vn-payroll-social.md) |
| Setting up a company | [vn-company-formation](vn-company-formation.md) |
| Where the official texts are | [references](references.md) |

**What changed for 2026.** Law 109/2025/QH15 replaces the 2007 PIT law (five bands, higher family deductions, from tax period 2026 for salaries and business income, 1 July 2026 for the rest). Law 67/2025/QH15 replaced the CIT law from tax period 2025 (15% and 17% rates for smaller companies). Law 108/2025/QH15 on tax administration took effect on 1 July 2026. Law 09/2026/QH16 (24 April 2026) let the Government set the revenue thresholds, and Decree 141/2026 set VND 1 billion from 1 January 2026. Presumptive (lump-sum) tax for household businesses was replaced by declaration. The business licence fee ended on 1 January 2026.

### Refusals and boundaries

This file gives headline figures only. For a computation, load the owning skill. Transfer pricing, global minimum tax, customs, special consumption tax and land taxes are not covered by the Vietnam pack yet: refer.

## Rates, bands and thresholds

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Corporate income tax, standard | 20% | Law 67/2025/QH15 Art. 10(1) | https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45557/57755-1-2025965-96667-2025-qh15.pdf |
| Corporate income tax, smaller companies | 15% (prior-year revenue to VND 3 billion); 17% (over 3 to 50 billion) | Art. 10(2) and (3) | same |
| PIT on employment income of residents | 5% to 35% in five bands | Law 109/2025/QH15 Art. 9 | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/109signed-17692403594311667615452.pdf |
| PIT on employment income of non-residents | 20% flat | Art. 21 | same |
| Personal deduction | VND 15.5 million a month | Art. 10(1)(a) | same |
| Real estate transfer | 2% of the price | Art. 14; exempt for the only home and within the family (Art. 4(1) and (2)) | same |
| Household business and individual business threshold | No PIT at annual revenue of VND 1 billion or less | Decree 141/2026 Art. 1, from 1 January 2026 | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf |
| Very small company CIT exemption | Revenue of VND 1 billion or less | Decree 141/2026 Art. 2 | same |
| Business licence fee | None from 1 January 2026 | Resolution 198/2025/QH15 Art. 10(7) | https://xaydungchinhsach.chinhphu.vn/tu-thang-1-2026-nguoi-nop-thue-khong-phai-nop-le-phi-mon-bai-119260126110926562.htm |
| Social insurance salary cap | VND 46.8 million a month to 30 June 2026; 50.6 million from 1 July 2026 | 20 times the reference level | https://xaydungchinhsach.chinhphu.vn/tu-1-7-nhieu-khoan-tro-cap-bhxh-thay-doi-the-nao-khi-luong-co-so-tang-119260523163024829.htm |
| Late payment interest | 0.03% per day | Law 108/2025/QH15 Art. 16(2)(a) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf |

VAT rates and the temporary 2% reduction are owned by [vietnam-vat](vietnam-vat.md) and are not restated here.

## The base

- **Individuals:** residence by 183 days or a regular home (Law 109/2025 Art. 2); employment income after insurance and family deductions on the five bands; business income above VND 1 billion revenue by the income method or, up to 3 billion, the revenue method.
- **Companies:** revenue less deductible costs plus other income, less exempt income and losses carried forward up to five years (Law 67/2025 Art. 7 and 16).
- **Payroll:** contributions on the contract salary within the floor and the 20-times cap.

## Deadlines and filing

| Item | Deadline |
| --- | --- |
| Monthly returns (withholding, VAT for monthly filers) | 20th day of the following month |
| Quarterly returns and CIT provisional payments | Last day of the first month of the next quarter |
| CIT and employer PIT annual finalisation | Last day of the 3rd month after year end |
| Individual self-filed PIT finalisation | Last day of the 4th month after year end |

Source: Decree 252/2026 as published on the Government portal (see Sources). Filing is online through thuedientu.gdt.gov.vn.

## Penalties and interest

Late payment interest is 0.03% per day (Law 108/2025/QH15 Art. 16(2)(a)). Administrative fines for late filing and under-declaration were not read for 2026 (see "Not yet confirmed").

## Cross-border points

- Payments abroad for services, interest and royalties are taxed through the foreign contractor regime (VAT plus CIT or PIT withheld by the Vietnamese payer); see [vn-corporate-income-tax](vn-corporate-income-tax.md).
- Dividends to individuals: 5% PIT; between Vietnamese companies: exempt income for the recipient.
- Non-residents transferring capital in a Vietnamese entity are taxed whether the transfer is made in Vietnam or abroad (Law 109/2025 Art. 23(1)).

## Two worked examples that recompute

### Example 1: should a tutor with VND 1.2 billion revenue worry about PIT? Compare 900 million

At 900 million revenue she is under the VND 1 billion threshold: no PIT. At 1.2 billion, using the revenue method for services (2% of revenue above the threshold), PIT is 2% of 200 million = 4 million.

```oa-check
name: VN 2026 household business threshold, two revenue levels
inputs:
  threshold: 1000000000
  revenue_low: 900000000
  revenue_high: 1200000000
steps:
  - tax_low: max(revenue_low - threshold, 0) * 0.02
  - tax_high: max(revenue_high - threshold, 0) * 0.02
expected:
  tax_low: 0
  tax_high: 4000000
```

### Example 2: selling a flat for VND 3 billion, second home against only home

A second home: PIT is 2% of the price, 60 million. If it is the seller's only home and residential land in Vietnam, the gain is exempt (Art. 4(2)): no PIT.

```oa-check
name: VN 2026 real estate transfer, second home vs only home
inputs:
  price: 3000000000
  only_home: 1
steps:
  - tax_second_home: price * 0.02
  - tax_only_home: price * 0.02 * (1 - only_home)
expected:
  tax_second_home: 60000000
  tax_only_home: 0
```

## Ask the client first

1. Individual or company, and resident or not.
2. The tax and the period (2026 or earlier; before or after 1 July 2026 for non-salary income of individuals).
3. Revenue of the business for the year (the VND 1 billion threshold).
4. For a property sale: whether it is the only home, and the relationship with the buyer.
5. Any foreign party in the transaction.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Law 67/2025/QH15 Art. 10 CIT rates and Art. 16 losses | https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45557/57755-1-2025965-96667-2025-qh15.pdf | 2026-11-14 |
| Read for Law 109/2025/QH15 Art. 2, 4, 9, 10, 14, 21, 23 and 29 | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/109signed-17692403594311667615452.pdf | 2026-11-14 |
| Read for Law 09/2026/QH16 Art. 1 to 3 and 5 (thresholds delegated, effective 1 January 2026) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/27/469536-1779329464_v1_1779843299_signed.pdf | 2026-11-14 |
| Read for Decree 141/2026/ND-CP Art. 1 and 2 (VND 1 billion thresholds) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf | 2026-11-14 |
| Read for the end of the business licence fee from 1 January 2026 | https://xaydungchinhsach.chinhphu.vn/tu-thang-1-2026-nguoi-nop-thue-khong-phai-nop-le-phi-mon-bai-119260126110926562.htm | 2026-11-14 |
| Read for the social insurance cap of VND 50.6 million from 1 July 2026 | https://xaydungchinhsach.chinhphu.vn/tu-1-7-nhieu-khoan-tro-cap-bhxh-thay-doi-the-nao-khi-luong-co-so-tang-119260523163024829.htm | 2026-11-14 |
| Read for Law 108/2025/QH15 Art. 16(2)(a) late payment interest and its 1 July 2026 effective date | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf | 2026-11-14 |
| Read for the Decree 252/2026 filing deadlines | https://xaydungchinhsach.chinhphu.vn/quy-dinh-thoi-han-nop-ho-so-khai-thue-119260703120801722.htm | 2026-11-14 |

Not yet confirmed: administrative fines for late filing and under-declaration in 2026; foreign contractor tax percentages; the VAT figures (owned by vietnam-vat, not re-read here).
