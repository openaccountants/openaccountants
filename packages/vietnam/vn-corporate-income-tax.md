---
name: vn-corporate-income-tax
description: >
  Vietnam corporate income tax (thuế thu nhập doanh nghiệp, TNDN) for tax year
  2026 under Law 67/2025/QH15 as amended by Law 09/2026/QH16 and Decree
  141/2026. Use for the 20% standard rate, the 15% and 17% rates for companies
  with prior-year revenue up to VND 3 billion and 50 billion, the new exemption
  for companies with revenue of VND 1 billion or less, the three-year SME
  exemption, incentive rates, loss carry-forward, dividends between Vietnamese
  companies, provisional payments, annual finalisation and late payment interest.
  Tier 2, not reviewed by an accountant.
version: "2.0"
jurisdiction: VN
tax_year: 2026
tax_year_notes: "Tax period 2026 (calendar year, or a financial year the company has notified). Law 67/2025/QH15 applies from tax period 2025."
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Vietnam Corporate Income Tax v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies and other organisations with taxable income in Vietnam for tax period 2026 (Law 67/2025/QH15 Art. 2): enterprises formed under Vietnamese law (taxed on income arising in and outside Vietnam), foreign enterprises with a permanent establishment (income connected to it, wherever it arises), foreign enterprises without a permanent establishment (Vietnam-source income, usually through the foreign contractor regime), cooperatives, public service units and other organisations with business income.

The tax period is the calendar year or a financial year the company chooses and notifies to its tax office (Art. 5). Individuals and household businesses are in [vietnam-pit](vietnam-pit.md); payroll in [vn-payroll-social](vn-payroll-social.md); VAT in [vietnam-vat](vietnam-vat.md).

### Refusals and boundaries

- Oil and gas and rare-resource rates depend on the contract or the mine: name the range, then refer.
- Investment incentives depend on the project's licence, sector and location: confirm the investment certificate before applying any incentive rate or holiday.
- Global minimum tax (top-up tax) for large groups, transfer pricing documentation and interest caps: refer; not covered here.
- Foreign contractor tax percentages on payments abroad: refer to the implementing decree and the treaty; the figures are on the "Not yet confirmed" line.

## Rates, bands and thresholds

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Standard rate | 20% | All companies unless a lower or special rate applies, Art. 10(1) | https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45557/57755-1-2025965-96667-2025-qh15.pdf |
| Small company rate | 15% | Total revenue of the immediately preceding tax period not above VND 3 billion, Art. 10(2) | same |
| Medium company rate | 17% | Preceding-period total revenue above VND 3 billion and not above 50 billion, Art. 10(3) | same |
| Oil and gas | 25% to 50% | Rate fixed per contract by the Prime Minister, Art. 10(4)(a) | same |
| Rare and precious resources (gold, silver, platinum, tin, tungsten, antimony, gems, rare earths) | 50%; 40% where 70% or more of the mine area is in an especially difficult area | Art. 10(4)(b) | same |
| Exemption for very small companies | Income exempt where total annual revenue is VND 1 billion or less | Prior-period revenue (annualised if under 12 months); not for a subsidiary or associate of a company that does not itself qualify; Decree 141/2026 Art. 2, from 1 January 2026 | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf |
| New SME exemption | Exempt for 3 years from the first enterprise registration certificate | Small and medium enterprises, Resolution 198/2025/QH15 Art. 10(4) | https://xaydungchinhsach.chinhphu.vn/chinh-sach-dac-biet-phat-trien-kinh-te-tu-nhan-ho-tro-tai-chinh-tin-dung-thue-phi-le-phi-uu-dai-lua-chon-nha-thau-119250518063622747.htm |
| Company formed from a household business | Exempt for 2 consecutive years from first taxable income | Companies on the 15% or 17% rate, Art. 15(4) | https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45557/57755-1-2025965-96667-2025-qh15.pdf |
| Incentive rate, top tier | 10% for 15 years | Qualifying new projects by sector or location, high-tech zones, Art. 13(1) | same |
| Incentive rate, second tier | 17% for 10 years | Qualifying projects in Art. 13(4) | same |
| Tax holiday with the 10% rate | Up to 4 years exempt, then 50% reduction for up to 9 years | Art. 14(1)(a) | same |
| Tax holiday with the 17% rate | Up to 2 years exempt, then 50% reduction for up to 4 years | Art. 14(2) | same |
| Loss carry-forward | Up to 5 consecutive years from the year after the loss | Art. 16(1) | same |
| Late payment interest | 0.03% per day | Law 108/2025/QH15 Art. 16(2)(a) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf |

The old file showed the 15% and 17% bands without saying they test the **preceding** period's total revenue; that test is in Art. 10(3) and decides the rate.

## The base

Taxable income = assessable income less exempt income less losses carried forward (Art. 7(1)). Assessable income = revenue less deductible expenses plus other income, including income received outside Vietnam (Art. 7(2)). Revenue is all sales, processing and service income including subsidies and surcharges, whether or not cash has been received (Art. 8).

1. Revenue for the period (Art. 8).
2. Less deductible expenses (Art. 9): expenses actually incurred for the business with lawful invoices and documents; the Art. 9 list of non-deductible items applies (for example deductible input VAT already credited).
3. Plus other income (capital transfers, real estate transfers, foreign income).
4. Less exempt income (Art. 4), including dividends and profit shares from Vietnamese companies that have already paid CIT (Art. 4(7)).
5. Less losses brought forward (Art. 16), oldest first, within five years.
6. Apply the rate. Losses of one activity may offset income of another, but real estate and investment-project transfer income may not be offset against income enjoying incentives, and mineral project transfers are computed separately (Art. 7(3) and (4)).

**Revenue method.** The Government sets a tax as a percentage of revenue for foreign enterprises without a permanent establishment, for companies with revenue up to VND 3 billion that can show revenue but not costs, and for cooperatives and public units in the same position (Art. 11(2)).

**Exemption mechanics (Decree 141/2026 Art. 2 and 4).** The VND 1 billion test uses total sales, service, financial and other income in the profit and loss appendix to the prior period's finalisation return. A new company expecting revenue of 1 billion or less pays no provisional tax; if actual revenue exceeds 1 billion it files and finalises with no late payment interest. A company that paid Q1 2026 provisional tax and qualifies stops further provisional payments and may offset or recover the overpayment.

## Deadlines and filing

| Item | Deadline | Source |
| --- | --- | --- |
| Quarterly provisional payment | By the last day of the first month of the following quarter | Decree 252/2026 via the Government portal |
| Annual finalisation return and final payment | Last day of the 3rd month after the end of the tax period (31 March 2027 for a calendar 2026 period) | same |

Returns are filed electronically on thuedientu.gdt.gov.vn. A change of financial year must be notified to the tax office before it is used (Art. 5(1)).

## Penalties and interest

Late payment interest is 0.03% per day of the tax paid late (Law 108/2025/QH15 Art. 16(2)(a)). Fines for late filing and under-declaration are set by the administrative penalty decree, not read for 2026 (see "Not yet confirmed").

## Cross-border points

- Foreign enterprises without a permanent establishment pay CIT on Vietnam-source income, normally by withholding by the Vietnamese payer as a percentage of revenue (foreign contractor tax, Art. 11(2)(a)).
- Dividends paid by a Vietnamese company to a corporate shareholder are paid out of after-tax profit; a Vietnamese corporate recipient treats them as exempt income (Art. 4(7)). Dividends to individuals carry 5% PIT: see [vietnam-pit](vietnam-pit.md).
- Vietnamese companies investing abroad declare foreign income and may credit foreign tax as the Government provides (Art. 3).
- Tax treaties can reduce withholding on interest and royalties; the treaty text decides.

## Two worked examples that recompute

### Example 1: trading company, 2025 revenue VND 2.4 billion, 2026 taxable income 300 million

Preceding-period revenue is above 1 billion (no exemption) and not above 3 billion, so the 15% rate applies to tax period 2026: 300 million times 15% = 45 million.

```oa-check
name: VN 2026 CIT small company rate from prior-year revenue
inputs:
  prior_revenue: 2400000000
  taxable_income: 300000000
steps:
  - rate: 0.15
  - tax: taxable_income * rate
expected:
  tax: 45000000
```

### Example 2: manufacturer, 2025 revenue VND 40 billion, 2026 assessable income 5 billion, 2023 loss of 1 billion unused

The 2023 loss is within five years, so it is deducted: taxable income 4 billion. Preceding-period revenue is above 3 billion and not above 50 billion, so the rate is 17%: tax 680 million. Had 2025 revenue been 55 billion, the rate would be 20% and the tax 800 million; the prior-year revenue decides.

```oa-check
name: VN 2026 CIT medium rate with loss carry-forward
inputs:
  assessable: 5000000000
  loss_bf: 1000000000
steps:
  - taxable: max(assessable - loss_bf, 0)
  - tax_17: taxable * 0.17
  - tax_if_20: taxable * 0.20
  - difference: tax_if_20 - tax_17
expected:
  taxable: 4000000000
  tax_17: 680000000
  tax_if_20: 800000000
  difference: 120000000
```

## Ask the client first

1. Total revenue (sales, services, financial and other income) of the preceding tax period, and months of operation.
2. Date of the first enterprise registration certificate and whether the company is an SME, or was converted from a household business.
3. Whether the company is a subsidiary or associate of a group, and whether the group companies would qualify for the 1 billion exemption.
4. Investment certificate: sector, location, project start, and any incentive already granted.
5. Losses brought forward, by year.
6. Payments to foreign parties (services, interest, royalties).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Law 67/2025/QH15 in the Official Gazette: Art. 2 taxpayers, Art. 4 exempt income, Art. 5 tax period, Art. 7 and 8 base and revenue, Art. 10 rates, Art. 11 method, Art. 13 and 14 incentives, Art. 15(4), Art. 16 losses, Art. 19 effect from tax period 2025 | https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45557/57755-1-2025965-96667-2025-qh15.pdf | 2026-11-14 |
| Read for Law 09/2026/QH16 Art. 3 (new CIT exemption delegated to the Government) and Art. 5 (from 1 January 2026) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/27/469536-1779329464_v1_1779843299_signed.pdf | 2026-11-14 |
| Read for Decree 141/2026/ND-CP Art. 2 (1 billion exemption and its conditions) and Art. 4 (transition for Q1 2026 and 2025 periods) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf | 2026-11-14 |
| Read for Resolution 198/2025/QH15 Art. 10(4) three-year SME exemption and Art. 10(7) end of the licence fee, as published on the Government portal | https://xaydungchinhsach.chinhphu.vn/chinh-sach-dac-biet-phat-trien-kinh-te-tu-nhan-ho-tro-tai-chinh-tin-dung-thue-phi-le-phi-uu-dai-lua-chon-nha-thau-119250518063622747.htm | 2026-11-14 |
| Read for Law 108/2025/QH15 Art. 16(2)(a) late payment interest | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf | 2026-11-14 |
| Read for the Decree 252/2026 deadlines for quarterly returns and annual finalisation, as published on the Government portal | https://xaydungchinhsach.chinhphu.vn/quy-dinh-thoi-han-nop-ho-so-khai-thue-119260703120801722.htm | 2026-11-14 |

Not yet confirmed: foreign contractor tax CIT percentages (the old file showed 5% on interest, 10% on royalties and 5% on services; the implementing decree and circular were not read); the 10-day foreign contractor remittance deadline; the 80% provisional payment rule; the revenue-method percentages for small companies under Art. 11(2)(b); late filing and under-declaration fines; global minimum tax rules.
