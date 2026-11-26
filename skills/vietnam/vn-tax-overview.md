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
version: "2.1"
jurisdiction: VN
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Vietnam Tax Overview v2.1

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
| Corporate income tax, smaller companies | 15% (preceding-period revenue up to VND 3 billion); 17% (over VND 3 billion to VND 50 billion inclusive) | Check annualisation, first-period and related-company rules in the CIT skill | same |
| PIT on employment income of residents | 5% to 35% in five bands | Law 109/2025/QH15 Art. 9 | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/109signed-17692403594311667615452.pdf |
| PIT on employment income of non-residents | 20% flat | Art. 21 | same |
| Personal deduction | VND 15.5 million a month | Art. 10(1)(a) | same |
| Real estate transfer | 2% of the statutory transfer value | Arts. 14 and 24. Exemptions apply to specified family transfers and qualifying sole-home sales under Art. 4(1)–(2) | same |
| Household business and individual business threshold | No business PIT at total annual revenue of VND 1 billion or less | Resident business. Decree 141/2026 Art. 1, from 1 January 2026 | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf |
| Very small company CIT exemption | Annual revenue of VND 1 billion or less | Qualifying Vietnamese entities under Decree 141/2026 Art. 2. Check preceding-period, new entity and related-party rules | same |
| Temporary 2026 and 2027 income tax reduction | 30% of eligible resident business PIT or CIT payable | Actual annual revenue in the year of the claim up to VND 10 billion. Check entity eligibility and split-company exclusions | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/11/398_2026_nd-cp_29102026-signed.signed.pdf |
| Business licence fee | None from 1 January 2026 | Resolution 198/2025/QH15 Art. 10(7) | https://xaydungchinhsach.chinhphu.vn/tu-thang-1-2026-nguoi-nop-thue-khong-phai-nop-le-phi-mon-bai-119260126110926562.htm |
| Social insurance salary cap | VND 46.8 million a month to 30 June 2026; 50.6 million from 1 July 2026 | 20 times the reference level | https://xaydungchinhsach.chinhphu.vn/tu-1-7-nhieu-khoan-tro-cap-bhxh-thay-doi-the-nao-khi-luong-co-so-tang-119260523163024829.htm |
| Late payment interest | 0.03% per day | Law 108/2025/QH15 Art. 16(2)(a) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf |

For eligible standard-rate supplies, VAT drops from 10% to 8% through 31 December 2026. See [vietnam-vat](vietnam-vat.md) for excluded supplies and the separate direct-method reduction.

## The base

- **Individuals:** test at least 183 days in the calendar year or first 12 consecutive months, or an eligible regular home, taking into account foreign tax residence evidence where applicable (Law 109/2025 Art. 2 and Decree 253/2026 Art. 4). Apply the resident employment bands after eligible insurance and family deductions. Resident businesses above VND 1 billion in annual revenue generally use the income method, with a revenue-method option up to VND 3 billion for eligible activities.
- **Companies:** revenue less deductible costs plus other income, less exempt income and allowable losses carried forward for up to 5 consecutive years from the year after the loss (Law 67/2025 Arts. 7 and 16).
- **Payroll:** apply each scheme's wage base. The social insurance cap is 20 times the reference level and the unemployment insurance cap is 20 times the applicable regional monthly minimum wage. See [vn-payroll-social](vn-payroll-social.md).

## Deadlines and filing

| Item | Deadline |
| --- | --- |
| Monthly returns (withholding, VAT for monthly filers) | 20th day of the following month |
| Quarterly returns | Last day of the first month of the next quarter |
| CIT provisional payments | Last day of the first month of the next quarter under the July 2026 rules. For periods under the previous law, the ordinary deadline was the 30th of that month |
| CIT and employer PIT annual finalisation | Last day of the 3rd month after year end |
| Individual self-filed PIT finalisation | Last day of the 4th month after year end |

Check the next-working-day rule and any applicable extension. Employers and companies can file through the Tax Department's eTax portal at https://thuedientu.gdt.gov.vn/.

## Penalties and interest

Late payment interest is 0.03% per day (Law 108/2025/QH15 Art. 16(2)(a)). Late filing penalties depend on the delay and tax due. An incorrect declaration causing a shortfall ordinarily incurs a 20% penalty on the shortfall, subject to the applicable offence and exceptions. See Decree 125/2020 as amended, Arts. 9, 13 and 16.

## Cross-border points

- Determine VAT and income tax separately for payments to foreign contractors. Under the direct withholding method the Vietnamese payer generally withholds and remits the applicable tax. For example, loan interest can attract CIT without VAT. See [vn-corporate-income-tax](vn-corporate-income-tax.md).
- Dividends to individuals generally attract 5% PIT. A Vietnamese recipient company generally excludes dividends from domestic investments where the distributing enterprise has accounted for Vietnamese CIT, including where it received a CIT incentive.
- Non-residents transferring capital in a Vietnamese entity are taxed whether the transfer is made in Vietnam or abroad (Law 109/2025 Art. 23(1)).

## Two worked examples that recompute

### Example 1: should a tutor with VND 1.2 billion revenue worry about PIT? Compare 900 million

Assume a Vietnamese tax resident with eligible tutoring services and no other business revenue. At VND 900 million, the tutor owes no business PIT. At VND 1.2 billion using the optional revenue method, PIT before relief is (VND 1.2 billion − VND 1 billion) × 2% = VND 4 million. The 30% reduction for eligible 2026 business income reduces PIT payable to VND 2.8 million.

```oa-check
name: VN 2026 household business threshold, two revenue levels
inputs:
  threshold: 1000000000
  revenue_low: 900000000
  revenue_high: 1200000000
  relief_rate: 0.30
steps:
  - tax_low: max(revenue_low - threshold, 0) * 0.02
  - tax_high_before_relief: max(revenue_high - threshold, 0) * 0.02
  - tax_high: tax_high_before_relief * (1 - relief_rate)
expected:
  tax_low: 0
  tax_high_before_relief: 4000000
  tax_high: 2800000
```

### Example 2: selling a flat for VND 3 billion, second home against only home

Assume a November 2026 sale to an unrelated buyer for a statutory transfer value of VND 3 billion. For a second home the PIT is VND 3 billion × 2% = VND 60 million. For an existing completed flat that is the seller's only qualifying home in Vietnam, the sale is exempt if the seller has held title for at least 183 days, transfers the entire property and declares the exemption.

```oa-check
name: VN 2026 real estate transfer, second home vs only home
inputs:
  price: 3000000000
  sole_home_exemption_eligible: 1
steps:
  - tax_second_home: price * 0.02
  - tax_only_home: price * 0.02 * (1 - sole_home_exemption_eligible)
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
| Decree 398/2026 Arts. 2–4, temporary income tax reduction | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/11/398_2026_nd-cp_29102026-signed.signed.pdf | 2026-11-26 |
| Decree 253/2026, sole-home exemption | https://xaydungchinhsach.chinhphu.vn/ca-nhan-chuyen-nhuong-co-duy-nhat-mot-nha-o-quyen-su-dung-dat-o-tai-viet-nam-duoc-mien-thue-thu-nhap-ca-nhan-11926070309365282.htm | 2026-11-26 |
| Decree 252/2026 Arts. 3 and 24, provisional CIT payment | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/252-ndcp.signed.pdf | 2026-11-26 |
| Previous Tax Administration Law, Art. 55 | https://congbao.chinhphu.vn/tai-ve-van-ban-so-29-vbhn-vpqh-44473-55499?format=pdf | 2026-11-26 |
| Decree 125/2020 as amended, consolidated tax penalties | https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-quy-dinh-xu-phat-vi-pham-hanh-chinh-ve-thue-hoa-don-119260828152453688.htm | 2026-11-26 |
| Resolution 204/2025, temporary VAT reduction | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/6/204-qh15.signed.pdf | 2026-11-26 |
| Employment Law 74/2025 Art. 34(2), unemployment insurance cap | https://congbao.chinhphu.vn/tai-ve-van-ban-so-74-2025-qh15-45562-57700?format=pdf | 2026-11-26 |

Not yet confirmed: the amount of a case-specific penalty or foreign contractor liability without the transaction or offence facts.
