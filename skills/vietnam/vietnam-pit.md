---
name: vietnam-pit
description: >
  Use this skill whenever asked about Vietnam personal income tax (thuế thu nhập
  cá nhân, TNCN) for tax year 2026, for employees, self-employed individuals and
  household businesses. Trigger on phrases like thuế TNCN, Vietnam income tax,
  giảm trừ gia cảnh, biểu thuế lũy tiến, PIT Vietnam, personal deduction Vietnam,
  dependent deduction Vietnam, hộ kinh doanh tax, quyết toán thuế TNCN, or any
  question about computing or filing personal income tax in Vietnam. Covers the
  five-band schedule of Law 109/2025/QH15 (5%, 10%, 20%, 30%, 35%), the family
  deductions of VND 15.5 million and 6.2 million a month, the business income
  regime with the VND 1 billion threshold set by Decree 141/2026, other income,
  non-residents and the 2026 filing deadlines. Tier 2, not reviewed by an
  accountant.
version: "2.0"
jurisdiction: VN
tax_year: 2026
tax_year_notes: "Calendar tax year 2026. Law 109/2025/QH15 applies to employment and business income of residents from tax period 2026 and to all other income from 1 July 2026."
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Vietnam Personal Income Tax (Thuế Thu Nhập Cá Nhân, TNCN) v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals with Vietnam personal income tax obligations for the calendar tax year 2026: resident employees, resident individuals and household businesses with business income, and non-residents with Vietnam-source income. Companies are in [vn-corporate-income-tax](vn-corporate-income-tax.md); social insurance is in [vn-payroll-social](vn-payroll-social.md); VAT is in [vietnam-vat](vietnam-vat.md).

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Vietnam |
| Tax | Thuế thu nhập cá nhân (TNCN), personal income tax |
| Currency | VND |
| Tax year | Calendar year 2026 (1 January to 31 December) |
| Law | Law 109/2025/QH15 (passed 10 December 2025, in force 1 July 2026; employment and business income of residents from tax period 2026), as amended by Law 09/2026/QH16 |
| Authority | Tax Department (Cục Thuế), Ministry of Finance |
| Filing portal | thuedientu.gdt.gov.vn (eTax); eTax Mobile for individuals |
| Contributor | Open Accountants Community |

**Which law applies in 2026.** Law 109/2025/QH15 Art. 29(2) applies the new rules on business income and on employment income of residents from tax period 2026, so the full 2026 year of salary and business income uses the new schedule and deductions. Its other rules (investment income, capital and property transfers, prizes, royalties, inheritances, gifts, non-residents) take effect on 1 July 2026 (Art. 29(1)); income of those kinds received from 1 January to 30 June 2026 falls under the old Law 04/2007/QH12 as amended, whose figures are not restated here (see "Not yet confirmed").

**Residence (Art. 2).** A resident is present in Vietnam 183 days or more in a calendar year or in 12 consecutive months from first arrival, or has a regular place of residence in Vietnam (a registered permanent residence, or a rented home under a fixed-term lease). Everyone else is a non-resident.

| Status | Taxed on | Employment income |
| --- | --- | --- |
| Resident | Worldwide income | Five-band schedule after deductions |
| Non-resident | Vietnam-source income only | Flat 20% of gross pay for work in Vietnam |

### Refusals and boundaries

- Never apply the old seven-band schedule, or the old 11 million and 4.4 million deductions, to 2026 salary or business income.
- Never claim a dependant deduction without the dependant's registration and the support condition met; each dependant counts once, against one taxpayer (Art. 10(3)).
- Never apply resident rates to a confirmed non-resident.
- Escalate to a licensed Vietnamese tax agent (đại lý thuế): foreign tax credits for residents with overseas income, tax equalisation, equity compensation, crypto income, transfer pricing on related-party business income.

## Rates, bands and thresholds

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Band 1 (employment income of residents) | 5% | Taxable income to VND 10 million a month, 120 million a year | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/109signed-17692403594311667615452.pdf |
| Band 2 | 10% | Over 10 to 30 million a month, over 120 to 360 million a year | same |
| Band 3 | 20% | Over 30 to 60 million a month, over 360 to 720 million a year | same |
| Band 4 | 30% | Over 60 to 100 million a month, over 720 million to 1.2 billion a year | same |
| Band 5 | 35% | Over 100 million a month, over 1.2 billion a year | same |
| Personal deduction | VND 15.5 million a month (186 million a year) | Resident, employment income, Art. 10(1)(a) | same |
| Dependant deduction | VND 6.2 million a month per dependant | Registered dependant, Art. 10(1)(b) | same |
| Business income threshold | VND 1 billion annual revenue or less: no PIT | Resident individual or household business; Law 09/2026/QH16 lets the Government set the threshold and Decree 141/2026 Art. 1 replaced 500 million with 1 billion in Decree 68/2026, from 1 January 2026 | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf |
| Business income, income method, revenue above threshold to VND 3 billion | 15% of (revenue less costs) | Art. 7(2)(b) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/109signed-17692403594311667615452.pdf |
| Business income, revenue over 3 to 50 billion | 17% of (revenue less costs) | Art. 7(2)(c) | same |
| Business income, revenue over 50 billion | 20% of (revenue less costs) | Art. 7(2)(d) | same |
| Revenue method (option, revenue above threshold to 3 billion): distribution and supply of goods | 0.5% of revenue above the threshold | Art. 7(3)(b) | same |
| Revenue method: services, construction without materials | 2% | Art. 7(3)(c) | same |
| Revenue method: asset leasing, insurance agency, lottery agency, multi-level sales agency | 5% | Art. 7(3)(c) | same |
| Revenue method: production, transport, services tied to goods, construction with materials | 1.5% | Art. 7(3)(d) | same |
| Revenue method: digital content (games, digital film, music, photos, digital advertising) | 5% | Art. 7(3)(đ) | same |
| Revenue method: other business | 1% | Art. 7(3)(e) | same |
| Property rental (other than accommodation business) | 5% of revenue above the threshold | Art. 7(4) | same |
| Investment income (dividends, interest not exempt), resident | 5% per payment | Art. 12, from 1 July 2026 | same |
| Capital transfer, resident | 20% of gain; 2% of price where cost cannot be determined | Art. 13(1), from 1 July 2026 | same |
| Securities transfer | 0.1% of price per transfer | Art. 13(2), Art. 23(2) | same |
| Real estate transfer | 2% of transfer price | Art. 14, Art. 24 | same |
| Prizes | 10% of value above VND 20 million per prize | Art. 15, from 1 July 2026 | same |
| Royalties, franchising | 5% of amount above VND 20 million per contract | Art. 16, 17, from 1 July 2026 | same |
| Inheritances and gifts | 10% of value above VND 20 million per receipt | Art. 18, from 1 July 2026 | same |
| Non-resident employment income | 20% of gross pay for work in Vietnam | Art. 21 | same |
| Non-resident business income | Goods 1%; services 5%; production, transport, construction with materials 2%; digital content 5%; other 2% of revenue | Art. 20(3) | same |
| Non-resident investment income | 5% | Art. 22 | same |
| Non-resident capital transfer | 20% of gain; 2% of price where cost cannot be determined | Art. 23(1) | same |

## The base

**Employment income of residents (Art. 8).** Taxable income = employment income for the period, less compulsory social insurance, health insurance and unemployment insurance contributions, compulsory professional liability insurance for certain professions, supplementary pension contributions under the Social Insurance Law, voluntary pension and life insurance up to the Government cap, the family deductions (Art. 10) and the charity, health and education deductions (Art. 11). The employee contribution rates are owned by [vn-payroll-social](vn-payroll-social.md).

1. Gross employment income: salary, wages, remuneration, cash and non-cash benefits, allowances other than the listed exempt allowances (Art. 3(2)).
2. Less exempt items (Art. 4), including night-shift and overtime pay and pay for untaken leave (Art. 4(8), new in 2026).
3. Less employee compulsory insurance (see the payroll skill).
4. Less VND 15.5 million personal deduction and VND 6.2 million per registered dependant, per month.
5. Less allowable charity (approved funds and organisations only), and health and education costs at the level the Government sets (Art. 11(2)).
6. Apply the five bands to the result.

**Quick computation (monthly).** Tax = 5% of the first 10 million, plus 10% of 10 to 30 million (2.0 million), plus 20% of 30 to 60 million (6.0 million), plus 30% of 60 to 100 million (12.0 million), plus 35% above 100 million. Cumulative tax at each band top: 0.5 million, 2.5 million, 8.5 million, 20.5 million.

**Dependants (Art. 10(4)).** Minor children; children who have lost civil capacity, are disabled or unable to work; and persons with no income or income below the level the Minister of Finance sets: adult children in university, college or vocational study, a spouse unable to work, parents past working age or unable to work, and other unsupported persons the taxpayer directly supports.

**Business income of residents (Art. 7).** Revenue up to VND 1 billion a year: no PIT (threshold from Decree 141/2026). Above it, tax = (revenue less costs) times 15%, 17% or 20% by revenue band. Where revenue is above the threshold and up to VND 3 billion, the individual may instead choose the revenue method: (revenue above the threshold) times the activity rate. Property rental (not accommodation business) always uses revenue above the threshold times 5%.

**Exempt income (Art. 4), main items.** Real estate transfers, inheritances and gifts of real estate between spouses, parents and children (natural, adopted, in-law), grandparents and grandchildren, and siblings; transfer of the taxpayer's only home and residential land in Vietnam; interest on government and local government bonds, bank deposits and life insurance; remittances; night-shift and overtime pay and pay for untaken leave; social insurance pensions and payments from supplementary and voluntary pension funds; state and programme scholarships; insurance and compensation payments; income from approved charities and foreign humanitarian aid; salaries of Vietnamese seafarers on international routes; first transfer of carbon credits and green bond interest; pay for state science and technology tasks; income of investors and founders in innovative start-ups; after-CIT income of a private enterprise owner or single-member LLC owner. Art. 5 adds a five-year exemption for qualifying high-tech and digital technology staff and an exemption for open-ended fund certificates held two years or more.

### Conservative defaults

| Situation | Default |
| --- | --- |
| Residence unknown | Treat as resident and ask for days present and housing |
| Number of dependants unknown | Zero dependants |
| Dependant registration unclear | Do not claim |
| Income category unclear | Employment income |
| Allowance taxability unclear | Taxable |
| Business revenue unclear against the threshold | Ask for full-year revenue before applying the 1 billion threshold |

### Red flags

| Flag | Why |
| --- | --- |
| Monthly withholding used the old seven bands | Over-withholding to refund at finalisation |
| A second income source with no withholding | Self-filing needed |
| Dependant claimed by two taxpayers | Each dependant counts once (Art. 10(3)) |
| Business revenue near VND 1 billion or 3 billion | The threshold and the band change the method |

## Deadlines and filing

| Item | Deadline | Source |
| --- | --- | --- |
| Employer monthly withholding return | 20th day of the following month | Decree 252/2026, as published by the Government portal |
| Employer quarterly return (quarterly filers) | Last day of the first month of the next quarter | same |
| Employer annual finalisation for employees | Last day of the 3rd month after year end (31 March 2027 for 2026) | same |
| Individual self-filed finalisation of employment income | Last day of the 4th month after year end (30 April 2027 for 2026) | same |
| Household and individual business filing | Under Decree 68/2026 as amended by Decree 141/2026 | Decree 141/2026 |

An individual with one employer and no other income may authorise that employer to finalise. An individual self-files when there is income from two or more sources with tax still payable, income not subject to withholding, or foreign income (residents), or to claim deductions the employer did not apply. A first-year resident who is in Vietnam less than 183 days in the calendar year but 183 days in 12 consecutive months files by the last day of the 4th month after the 12-month period ends. Household businesses with revenue above VND 1 billion must use electronic invoices with a tax authority code (Decree 141/2026 Art. 1(2)).

## Penalties and interest

| Item | Figure | Source |
| --- | --- | --- |
| Late payment interest | 0.03% per day of the unpaid tax | Law 108/2025/QH15 Art. 16(2)(a) |
| Late filing, under-declaration and evasion fines | Not stated here: the administrative penalty decree was not read for 2026 | Not yet confirmed |

Failure to register a dependant means the deduction is refused, with back tax and late payment interest.

## Cross-border points

- Non-residents pay flat rates on gross amounts (Art. 20 to 27); no family deductions.
- A resident's capital transfer is taxed wherever the transfer happens; a non-resident's transfer of capital in a Vietnamese entity is taxed whether made in Vietnam or abroad (Art. 23(1)).
- Tax treaties may reduce Vietnam's taxing right; the treaty text decides. Foreign tax credits for residents: escalate.
- Foreign employees' social insurance: see [vn-payroll-social](vn-payroll-social.md).

## Two worked examples that recompute

### Example 1: single employee, VND 40 million a month, no dependants (2026)

Employee insurance at 10.5% (8% social, 1.5% health, 1% unemployment, below every cap): 4.2 million. Taxable income: 40 million less 4.2 million less 15.5 million = 20.3 million. Tax: 5% of 10 million = 0.5 million, plus 10% of 10.3 million = 1.03 million. Total 1.53 million a month. (The old file used 15% for band 2 and got 2.045 million: wrong.)

```oa-check
name: VN 2026 employee 40m a month, no dependants
inputs:
  gross: 40000000
  insurance_rate: 0.105
  personal: 15500000
steps:
  - insurance: gross * insurance_rate
  - taxable: gross - insurance - personal
  - band1: min(taxable, 10000000) * 0.05
  - band2: max(min(taxable, 30000000) - 10000000, 0) * 0.10
  - tax: band1 + band2
expected:
  insurance: 4200000
  taxable: 20300000
  tax: 1530000
```

### Example 2: designer with a household business, revenue VND 2.5 billion, costs 1.9 billion: which method?

Revenue is above VND 1 billion and not above 3 billion, so she may choose. Income method: (2.5 billion less 1.9 billion) times 15% = 90 million. Revenue method for services: (2.5 billion less 1 billion) times 2% = 30 million. The revenue method costs 60 million less; the decision turns on the cost ratio. The income method wins only where profit times 15% is below (revenue above threshold) times 2%.

```oa-check
name: VN 2026 household business, income method vs revenue method
inputs:
  revenue: 2500000000
  costs: 1900000000
  threshold: 1000000000
steps:
  - income_method: (revenue - costs) * 0.15
  - revenue_method: (revenue - threshold) * 0.02
  - saving: income_method - revenue_method
  - chosen: min(income_method, revenue_method)
expected:
  income_method: 90000000
  revenue_method: 30000000
  saving: 60000000
  chosen: 30000000
```

## Ask the client first

1. Days in Vietnam in 2026 and in the 12 months from first arrival, and whether there is a registered or leased home in Vietnam.
2. Every income source in 2026, with the dates income was received (before or after 1 July 2026 for non-employment income).
3. Number of dependants, their registration, and their own income.
4. Employee compulsory insurance actually deducted, and any voluntary pension or life insurance.
5. For business income: full-year revenue, costs with invoices, activity type, and the method chosen.
6. Whether the employer will finalise on the individual's behalf.

Self-check before finalisation: five-band schedule used; 15.5 million and 6.2 million deductions; insurance deducted before the bands; every income source categorised; withholding reconciled to the annual liability; the right deadline (31 March employer, 30 April self-filer).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Law 109/2025/QH15 in the Official Gazette: Art. 2 residence, Art. 4 and 5 exemptions, Art. 7 business income, Art. 8 base, Art. 9 bands, Art. 10 and 11 deductions, Art. 12 to 27 other income and non-residents, Art. 29 effective dates | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/109signed-17692403594311667615452.pdf | 2026-11-14 |
| Read for Law 09/2026/QH16 Art. 1 (business threshold set by the Government) and Art. 5 (effective 1 January 2026) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/27/469536-1779329464_v1_1779843299_signed.pdf | 2026-11-14 |
| Read for Decree 141/2026/ND-CP Art. 1 (1 billion threshold, e-invoices) and Art. 3 (in force 1 January 2026) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf | 2026-11-14 |
| Read for Law 108/2025/QH15 (Tax Administration) Art. 16(2)(a) late payment interest | https://congbao.chinhphu.vn/van-ban/luat-so-108-2025-qh15-468670.htm | 2026-11-14 |
| Read for the Decree 252/2026 filing deadlines (monthly, quarterly, finalisation 3rd and 4th month) as published on the Government portal | https://xaydungchinhsach.chinhphu.vn/quy-dinh-thoi-han-nop-ho-so-khai-thue-119260703120801722.htm | 2026-11-14 |

Not yet confirmed: the old Law 04/2007/QH12 thresholds and rates for non-employment income received 1 January to 30 June 2026 (prizes, royalties, inheritances, gifts; the old file showed VND 10 million thresholds); the Government cap on voluntary pension and life insurance deductions and the health and education deduction levels (implementing decree not read); the dependant income limit set by the Minister of Finance; late filing and under-declaration fines (administrative penalty decree not read for 2026); the full text of Decree 252/2026 (read through the Government portal summary only); Decree 68/2026 business filing deadlines.
