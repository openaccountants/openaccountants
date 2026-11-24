---
name: id-tax-optimization
description: "Use this skill whenever asked about Indonesian tax planning, regime selection, or year-end optimization for self-employed individuals (Orang Pribadi) and small businesses. Trigger on phrases like \"Indonesia tax planning\", \"PPh Final vs progressive Indonesia\", \"UMKM 0.5% break-even\", \"PP 55/2022\", \"optimize Indonesian tax\", \"PTKP planning\", \"Indonesian tax savings\", \"NPPN vs pembukuan\", \"PT Perorangan vs OP\", \"perencanaan pajak Indonesia\", \"hemat pajak\", \"tarif final UMKM\". Covers regime selection (UMKM Final 0.5%, NPPN deemed-profit, pembukuan), entity choice (OP vs PT Perorangan vs PT), Pasal 6/Pasal 9 deduction planning, PTKP optimization, PPh Final Pasal 4(2) for rental and construction, BPJS wage-cap planning, year-end timing. Out of scope: aggressive avoidance, treaty shopping, transfer pricing, paper-PT structures, CFC planning, and anything caught by PP 55/2022 substance rules or Pasal 18 UU PPh. ALWAYS read this skill before advising on Indonesian tax planning."
jurisdiction: ID
tax_year: 2026
last_updated: 2026-11-22
version: "1.1"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
category: tax-optimization
type: decision
---

# ID Tax Optimization

## Indonesia Tax Optimization -- Self-Employed & Small Business Skill v1.1

## Scope

Use the 2026 rules below for calendar-year planning. For 2025, use the historical UMKM periods in Section 3 and check the express 2025 transition in PP 20/2026. The PTKP and progressive rate tables apply to both calendar years.

## Rates, bands and thresholds


### Tax Optimization

- **Individual turnover up to IDR 500M**. The first IDR 500 million of cumulative annual turnover of an eligible individual is outside the 0.5% final base. A qualifying entity applies 0.5% to its entire qualifying turnover. [PP 55/2022 art. 60](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf).
- **Turnover up to IDR 4.8B**. Compare available regimes using the actual margin, activities and applicable deductions or allowance. Check prior-year and related turnover, the founder's one-person companies and any PH/MT aggregation. Revenue from specified independent professional services is excluded. Ordinary PTs qualify only under the applicable transition. [PP 20/2026 arts. 56–58 and art. II](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf).
- **Turnover exceeds IDR 4.8B during an eligible year**. Determine eligibility for the following tax year. A qualifying existing taxpayer generally finishes the current year on final tax and moves to ordinary rates the following year. [PP 20/2026 art. 57](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf), [PP 55/2022 art. 61](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf).
- **Operating losses expected**. Compare bookkeeping. An ordinary fiscal loss generally carries forward for up to five years. Check the terms of any longer investment facility. [Income Tax Law art. 6](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf), [PMK 81/2024 arts. 407–418](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf).
- **Domestic dividends from a PT**. A resident individual can exclude the amount invested in qualifying Indonesian instruments on time. The uninvested amount generally attracts 10% final income tax. Resident corporate recipients have a separate domestic dividend exclusion. [Income Tax Law art. 4(3)(f)](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf), [PMK 18/2021](https://jdih.kemenkeu.go.id/api/download/39fdb2fc-1736-4ebb-80f5-d257f75df0b5/18~PMK.03~2021Per.pdf), [PP 19/2009](https://jdih.kemenkeu.go.id/api/download/fulltext/2009/19TAHUN2009PP.htm).
- **Owner salary from a PT**. Genuine commercially reasonable pay for work can be deductible to the company, subject to PPh 21. Review related-party terms under Income Tax Law arts. 6, 9, 18 and 21.
- **KK (default joint)**. Married taxpayers generally follow combined family taxation approach unless separate tax-rights/obligations arrangements apply under prevailing Indonesian income-tax regulations. PTKP treatment depends on marital and dependent status under applicable rules.  _(UU PPh Art. 8; PP 58/2023; PMK 168/2023; PMK 101/PMK.010/2016.; note: UU PPh as amended by UU HPP No. 7/2021.)_

## Section 1 -- Quick Reference: When Each Regime / Entity Wins

**Quick reference**

| Field | Treatment |
| --- | --- |
| Country | Republic of Indonesia (Republik Indonesia) |
| Tax authority | Direktorat Jenderal Pajak (DJP) -- Ministry of Finance (Kementerian Keuangan) |
| Primary rules | Income Tax Law as amended by UU 7/2021, PP 55/2022 as amended by PP 20/2026, PP 58/2023, PMK 168/2023, PER-17/PJ/2015, the KUP Law as amended, the Company Law as amended and PP 8/2021 [Income Tax Law amendments](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) |
| Currency | Indonesian Rupiah (IDR) |
| Tax year | Calendar year (1 January to 31 December) unless another year applies [KUP art. 1](https://jdih.kemenkeu.go.id/api/download/50e4f976-7d46-4bbc-9230-e213a1674197/SDSN%20Pajak.pdf) |
| Annual income tax return deadline | Three months after year end for individuals and four for companies, normally 31 March and 30 April respectively. Check any valid extension. [PER-3/PJ/2026 arts. 4–6](https://www.pajak.go.id/id/peraturan/XD3LOZQlkm-per-3-pj-2026) |
| Anti-avoidance | PP 55/2022 art. 32(4) applies economic substance where the listed mechanisms do not prevent tax avoidance. Income Tax Law art. 18 governs special relationships and adjustments. Apply PMK 112/2025 for current treaty procedures. [PP 55/2022 art. 32](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf), [PMK 112/2025](https://jdih.kemenkeu.go.id/dok/pmk-112-tahun-2025) |

### When each option wins -- one-line rules of thumb

**Situation / Best option table**

| Situation | Best option |
| --- | --- |
| Individual with turnover up to IDR 500M | An eligible individual's final PPh is zero. Compare ordinary tax after PTKP when deciding whether to opt for ordinary rates. |
| Turnover above IDR 500M and up to IDR 4.8B | Compare both ordinary methods where eligible and final PPh where the taxpayer and activities qualify. |
| Historic UMKM eligibility period ended | Apply the 2026 transition before deciding whether final PPh is still available. |
| Turnover exceeds IDR 4.8B | Verify the year ordinary tax begins. Plan bookkeeping and assess legal structure separately. |
| Operating losses expected | Bookkeeping permits ordinary fiscal-loss relief, where the eligibility and carry-forward conditions are met. |
| Land/building rental income | PPh Final Pasal 4(2) 10% applies automatically |
| Construction services | PPh Final Pasal 4(2) per PP 9/2022 -- rate by SBU class |

## Ask the client first

1. Gross annual turnover (peredaran bruto) -- last 3 years + current-year projection.
2. Net margin -- approximate net / gross. Critical for break-even.
3. Entity form -- OP, CV/firma, PT Perorangan, PT, koperasi.
4. Date of registration, historic UMKM years, any election of ordinary rates and relevant 2026 transition.
5. NPWP status and family tax arrangement, including PH, MT or HB where applicable.
6. Marital status and whether the spouse's income is combined.
7. Dependants entirely supported at the start of year, up to three under Income Tax Law art. 7(1)(d).
8. Income sources -- usaha / pekerjaan bebas / employment / rental / capital / foreign.
9. BPJS enrolment -- Kesehatan and Ketenagakerjaan (JHT/JKK/JKM/JP).
10. KLU code -- determines NPPN % and PPh Final classification.

## The method, step by step

## Section 3 -- Regime Selection: Break-Even Between the Three OP Regimes

Indonesian self-employed individuals (Orang Pribadi) generally choose between three regimes for taxing business / professional income. Each has dramatically different mechanics.

### 3.1 The three regimes summarized

**Three regimes table**

| Regime | Legislation | Mechanics |
| --- | --- | --- |
| **UMKM Final 0.5%** | PP 55/2022 and PP 20/2026 | Apply 0.5% monthly to qualifying gross turnover above the cumulative IDR 500M individual exclusion. Eligible companies have no individual exclusion. No ordinary expense deduction. |
| **Progressive with NPPN** (deemed net income) | Income Tax Law art. 14(2), PER-17/PJ/2015 and PMK 81/2024 | Eligible individuals with relevant prior-year turnover below IDR 4.8B multiply each activity's gross by its applicable percentage, subtract PTKP and apply progressive rates. Notify DJP in the first three months of the year or, for a new registrant, by the earlier of three months after registration and year end. |
| **Progressive with Pembukuan** | Income Tax Law art. 14 and KUP art. 28 | Keep consistent tax books using the applicable accrual or cash basis. Deduct permitted expenses and apply the individual PTKP and progressive rates to the ordinary income base. See PMK 81/2024 arts. 448–452 for exceptions to the books requirement. |

**UMKM duration.** Former PP 55 art. 59 gave individuals seven tax years, ordinary PTs three and eligible one-person PTs, cooperatives, CVs, firms and village enterprises four. PP 20/2026, effective 22 April 2026, repealed that article. It sets a separate four-tax-year cooperative rule. Apply art. II to eligible individual, one-person PT and cooperative transitions, including its express 2025 treatment. Ordinary PTs, CVs, firms and listed village enterprises already within an eligible former period can complete their remaining term subject to the old eligibility tests. [Former PP 55/2022 art. 59](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf), [PP 20/2026 art. 57 and art. II](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf).

### 3.2 PTKP and progressive brackets

**PTKP table**  _([PMK 101/PMK.010/2016 art. 1](https://jdih.kemenkeu.go.id/api/download/FullText/2016/101~PMK.010~2016Per.pdf))_

| Code | Annual PTKP (IDR) |
| --- | --- |
| TK/0 (single, no dependents) | 54,000,000 |
| TK/1 | 58,500,000 |
| TK/2 | 63,000,000 |
| TK/3 | 67,500,000 |
| K/0 (married, no dependents) | 58,500,000 |
| K/1 | 63,000,000 |
| K/2 | 67,500,000 |
| K/3 | 72,000,000 |
| K/I/0 (married, spouse's income combined, no dependents) | 112,500,000 |
| K/I/3 | 126,000,000 |

**Progressive brackets table**  _([Income Tax Law art. 17(1)(a)](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf))_

| Annual taxable income (IDR) | Rate |
| --- | --- |
| 0 -- 60,000,000 | 5% [PPh art. 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) |
| 60,000,001 -- 250,000,000 | 15% [PPh art. 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) |
| 250,000,001 -- 500,000,000 | 25% [PPh art. 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) |
| 500,000,001 -- 5,000,000,000 | 30% [PPh art. 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) |
| > 5,000,000,000 | 35% [PPh art. 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) |

Round annual taxable income down to full thousands of rupiah before applying the brackets. [Income Tax Law art. 17(4)](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf).
### 3.3 The UMKM Final 0.5% zero-rate band

- **UMKM zero-rate band**. For OP, the first IDR 500 million of gross annual turnover is taxed at 0%. The 0.5% applies only above that. Example: R = 800M → PPh Final = 0.5% × 300M = IDR 1,500,000.  _(PP 55/2022 Art. 60)_

### 3.4 Break-even formula -- UMKM vs Progressive with NPPN

For one eligible individual with one qualifying activity, no other ordinary income and proper NPPN notification, let R = gross revenue, n = NPPN fraction and P = PTKP. Final PPh is 0.005 × max(R − 500,000,000, 0). Compare it with the progressive tax on max(n × R − P, 0), rounded down to whole thousands of rupiah before the brackets. Recompute for additional activities or ordinary income.

### 3.5 NPPN rates for specific activities

The columns cover the 10 cities specified in PER-17/PJ/2015, other provincial capitals and other locations. Match the actual activity code (KLU) before computing a result. [PER-17/PJ/2015 arts. 4 and 6](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto).

| Exact KLU | Specified cities | Other provincial capitals | Other locations |
| --- | --- | --- | --- |
| 62010 Computer programming activities | 50% | 50% | 50% |
| 47111 Retail sales primarily food, beverages or tobacco in supermarkets, minimarkets and hypermarkets | 30% | 25% | 20% |

Rates for other legal, consulting, restaurant and construction activities are not yet confirmed here. Check the exact Annex I classification before applying any percentage. Exclude receipts subject to a separate final regime from the ordinary NPPN calculation.

### 3.6 Pembukuan -- when it beats both UMKM and NPPN

- Actual margin < NPPN deemed margin (NPPN taxes phantom income).
- Operating losses expected -- only pembukuan allows 5-year loss carry-forward (Pasal 6(2)).
- Heavy capex -- only pembukuan allows depreciation (Pasal 11).
- Mixed usaha + pekerjaan bebas income; or PPh 24 foreign tax credit claims.

## Section 4 -- Entity Choice: OP vs PT Perorangan vs PT

### 4.1 The three entity types in the small-business space

**Entity types table**

| Entity | Legislation | Liability | Tax treatment |
| --- | --- | --- | --- |
| Orang Pribadi (OP) -- sole trader | UU PPh (no separate entity law -- registered via NPWP only) | Unlimited personal liability | Personal PPh (regimes in Section 3) |
| PT Perorangan (single-shareholder micro or small PT) | Company Law as amended by UU 6/2023 and PP 8/2021 | Generally limited | 22% ordinary before applicable relief, or 0.5% final when eligible under PP 20/2026. |
| PT (Perseroan Terbatas) | Company Law as amended and PP 8/2021 | Generally limited | 22% ordinary before applicable relief. Check PP 20/2026 art. II for the remaining period of existing qualifying PTs. |

### 4.2 Tax + administrative cost trade-off

**Cost trade-off table**

| Factor | OP | PT Perorangan | PT |
| --- | --- | --- | --- |
| Setup cost | Check applicable activity and licensing fees | IDR 50,000 AHU filing fee for an eligible micro or small one-person company | Check AHU fees by capital and obtain an actual quote for professional costs |
| Capital | No separate share capital | Founders set authorised capital and issue and fully pay at least 25%. Check micro/small and sector rules. | Founders set authorised capital and issue and fully pay at least 25%. Check applicable sector rules. |
| Statutory audit | Check any activity-specific rule | Apply the company audit tests and other relevant legal requirements | Required for at least IDR 50B in assets and/or turnover, relevant public fundraising or debt instruments, listed companies, a Persero and other cases required by law |
| Monthly PPh 25 | Check instalments on ordinary income including when using NPPN | Check ordinary liability and applicable instalment rules | Check ordinary liability and applicable instalment rules |
| Annual filing | Coretax individual return, generally by 31 March | Coretax corporate return, generally by 30 April | Coretax corporate return, generally by 30 April |
| Domestic dividend to resident individual | N/A | 10% final on the part that fails the investment exclusion | Same |
| Salary to owner | Drawings are personal | Genuine reasonable pay for business work can be deductible, with PPh 21 as applicable | Same |

[PP 8/2021 arts. 3–5](https://jdih.kemenkeu.go.id/api/download/680a952b-3f39-4e9c-86ea-4e4e1d1470e4/8TAHUN2021PP.pdf), [Company Law art. 68](https://peraturan.bpk.go.id/Download/29563/UU%20Nomor%2040%20Tahun%202007.pdf), [Income Tax Law art. 25](https://jdih.kemenkeu.go.id/api/download/fulltext/2008/36TAHUN2008UU.htm), [PER-12/PJ/2026](https://pajak.go.id/id/peraturan/yNdK4DJlB8-per-12-pj-2026).

[PP 45/2024 fee schedule](https://peraturan.bpk.go.id/Download/365416/PP%20Nomor%2045%20Tahun%202024.pdf).

### 4.3 Decision heuristic

First identify legal structure and the applicable licensing, liability and micro or small business criteria. Then compare the individual's lawful options with the company's ordinary income tax and salary or dividend costs. If the relevant individual and company turnover must be added under PP 20/2026, use the combined amount. For ordinary company income, assess eligibility for the art. 31E reduction before using 22% throughout. [PP 7/2021 art. 35](https://peraturan.bpk.go.id/Download/154506/PP%20Nomor%207%20Tahun%202021.pdf), [PP 20/2026 arts. 57–58](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf), [Income Tax Law art. 31E](https://jdih.kemenkeu.go.id/api/download/fulltext/2008/36TAHUN2008UU.htm).

### 4.4 Domestic dividends

A resident individual generally pays 10% final on the portion of a domestic dividend that fails the qualifying investment exclusion. Invest in eligible Indonesian instruments by the end of the third month after the tax year of receipt, hold the investment for at least three tax years from that year and report it as required. A resident corporate recipient has a separate exemption for domestic dividends. [Income Tax Law art. 4(3)(f)](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf), [PMK 18/2021 arts. 34–41](https://jdih.kemenkeu.go.id/api/download/39fdb2fc-1736-4ebb-80f5-d257f75df0b5/18~PMK.03~2021Per.pdf), [PP 19/2009 art. 1](https://jdih.kemenkeu.go.id/api/download/fulltext/2009/19TAHUN2009PP.htm).

Example: A company pays 22% ordinary income tax on IDR 100 of taxable profit and distributes all IDR 78 remaining to a resident individual. Without a qualifying investment, final dividend tax is IDR 7.80, for IDR 29.80 combined. Investing the full dividend as prescribed leaves IDR 22 combined, a saving of 7.8 percentage points on the original profit.

## Section 5 -- PTKP Optimization

PTKP (Penghasilan Tidak Kena Pajak) is the personal allowance deducted before applying progressive brackets. It only matters under the progressive regimes (NPPN or pembukuan). It is irrelevant under UMKM Final.

### 5.1 Joint vs separate assessment for married couples

**Marital assessment status table**  _(Pasal 8(1)-(3) UU PPh)_

| Status | NPWP arrangement | When to use |
| --- | --- | --- |
| **KK** (default family assessment) | Family tax unit | Where the spouse's ordinary income is combined, use K/I and the supported dependants. A spouse's income solely from one employer is excluded from the combined computation if PPh 21 was withheld and the job is unrelated to the family business or professional work. |
| **PH** (property and income separation) | Written separation agreement | Tax combined net income, then allocate by each spouse's share of net income. |
| **MT** (spouse elects separate administration) | Separate tax administration | Tax combined net income, then allocate by each spouse's share of net income. |
| **HB** (court-ordered separation) | Separate tax administration | Each computes their own tax and allowance from their actual circumstances. |

### 5.2 Joint filing benefit when one spouse's income is final

- **Joint filing exclusion of final income**. If one spouse earns income already taxed as PPh Final (e.g., UMKM under PP 55/2022 or PPh Final 4(2) rental), that income is excluded from the joint progressive calculation per Pasal 4(2). Joint filing then only adds non-Final income while Final income is settled. This is legislative design, not avoidance.  _(Pasal 4(2))_

### 5.3 Supported dependants

Add IDR 4,500,000 for each fully supported dependant, up to three. Qualifying dependants are direct-line relatives by blood or marriage and adopted children. Use circumstances at the beginning of the tax year or part-year, normally 1 January for the calendar year. [Income Tax Law art. 7(1)(d), (2)](https://jdih.kemenkeu.go.id/api/download/fulltext/2008/36TAHUN2008UU.htm), [PMK 101/PMK.010/2016 art. 1](https://jdih.kemenkeu.go.id/api/download/FullText/2016/101~PMK.010~2016Per.pdf).

### 5.4 PTKP worked comparison

Assume deemed net income of IDR 200 million and no other income. With K/2 (married with two eligible dependants), deduct IDR 67.5 million. The taxable IDR 132.5 million gives IDR 13.875 million PPh. With TK/0 (a different taxpayer, single with no dependants), deduct IDR 54 million. The taxable IDR 146 million gives IDR 15.9 million PPh. The difference is IDR 2.025 million and reflects both marriage and dependants. If the Coretax family data is incomplete, reconcile it with the taxpayer's evidence and apply the status established under art. 7. [Income Tax Law arts. 7 and 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf).

```oa-check
name: Compare the K/2 and TK/0 personal allowances
inputs:
  deemed_net: 200000000
  k2_ptkp: 67500000
  tk0_ptkp: 54000000
  band_end: 60000000
  first_rate: 0.05
  second_rate: 0.15
steps:
  - k2_taxable: deemed_net - k2_ptkp
  - tk0_taxable: deemed_net - tk0_ptkp
  - k2_tax: band_end * first_rate + (k2_taxable - band_end) * second_rate
  - tk0_tax: band_end * first_rate + (tk0_taxable - band_end) * second_rate
  - difference: tk0_tax - k2_tax
expected:
  k2_taxable: 132500000
  tk0_taxable: 146000000
  k2_tax: 13875000
  tk0_tax: 15900000
  difference: 2025000
```

## Section 6 -- Deductible Expense Planning (Pasal 6) and Pasal 9 Non-Deductibles

Only relevant under pembukuan (full bookkeeping). Under NPPN, the deemed-profit % includes implicit expense allowance; under UMKM Final, expenses are irrelevant.

### 6.1 Pasal 6 UU PPh -- deductible business expenses

**Pasal 6 deductible expense categories table**

| Category | Reference | Planning note |
| --- | --- | --- |
| Costs of obtaining, collecting, maintaining income | Pasal 6(1)(a) | The general rule -- direct nexus required. |
| Depreciation / amortization | Pasal 6(1)(b); Pasal 11, 11A | See Section 6.3. |
| Qualifying pension fund contributions | Pasal 6(1)(c) | Check the required fund authorisation and payer. |
| Realised losses on disposal of eligible business assets | Pasal 6(1)(d) | Check asset use and the disposal provisions. |
| Foreign exchange losses | Pasal 6(1)(e) | Follow the applicable accounting and tax treatment. |
| Specified R&D in Indonesia | Pasal 6(1)(f) and PMK 153/2020 | Up to 300% total, including conditional additional deductions under [PMK 153/2020](https://jdih.kemenkeu.go.id/api/download/e07e1487-b034-4890-a961-1d44209292c5/153~PMK.010~2020Per.pdf). |
| Qualifying work practice, apprenticeships or training | Pasal 6(1)(g) and PMK 128/2019 | Up to 200% total, including conditional additional deductions under [PMK 128/2019](https://jdih.kemenkeu.go.id/api/download/fulltext/2019/128~PMK.010~2019Per.pdf). |
| Bad debts written off | Pasal 6(1)(h) | Submit the debt list and establish the qualifying recovery evidence or small-debtor exception. [PMK 207/2015](https://jdih.kemenkeu.go.id/dok/207-pmk-010-2015/files) amends the implementing conditions. |
| Eligible donations | Pasal 6(1)(i)–(m), PP 93/2010 | The PP 93 ceiling is 5% of the preceding year's net fiscal income, subject to the eligible donation type, recipient and documentation. Apply the ministerial procedure for the year. [PP 93/2010](https://jdih.kemenkeu.go.id/dok/pp-93-tahun-2010/files), [PMK 114/2025](https://www.jdih.kemenkeu.go.id/api/download/956c4a77-a4bb-4c97-a4a9-989bc6a98c79/2025pmkeuangan114.pdf). |

### 6.2 Pasal 9 -- non-deductible items (always disallowed)

**Pasal 9 non-deductible items table**

| Item | Reference | Note |
| --- | --- | --- |
| Dividend distributions | Pasal 9(1)(a) | Use reinvestment exemption (§4.4). |
| Reserves / provisions (except sector-approved) | Pasal 9(1)(c) | No general bad-debt provision. |
| Individual’s personal life, health and accident premiums | Pasal 9(1)(d) | Check the exception for qualifying employer-paid premiums included in the employee's income. |
| Excess related-party remuneration | Pasal 9(1)(f) | Apply the commercially reasonable amount. |
| Personal donations or expenses | Pasal 9(1)(b), (g)–(i) | Separate these from eligible business expenditure. |
| Individual's drawings | Pasal 6(1)(a) | Drawings do not reduce business income. Allow genuine commercially reasonable pay for work where the statutory tests and payroll duties are met. |
| Income tax and tax sanctions | Pasal 9(1)(h), (k) | Check the business nexus and treatment of other taxes. |
| Entertainment without supporting evidence | Pasal 6(1)(a) | Keep evidence of business purpose, expenditure and the required nominative list. |

### 6.3 Depreciation

**Depreciation groups** _([Income Tax Law art. 11](https://jdih.kemenkeu.go.id/api/download/fulltext/2008/36TAHUN2008UU.htm), [PMK 72/2023](https://jdih.kemenkeu.go.id/api/download/46cededa-86ae-4cc9-93e5-b6bef8892074/2023pmkeuangan072.pdf)):_

| Group | Life | Straight-line | Declining-balance |
| --- | --- | --- | --- |
| I (computers, office equipment) | 4 yr | 25% | 50% |
| II | 8 yr | 12.5% | 25% |
| III | 16 yr | 6.25% | 12.5% |
| IV | 20 yr | 5% | 10% |
| Building -- permanent | 20 yr by default | 5% by default | n/a |
| Building -- non-permanent | 10 yr | 10% | n/a |

Use the statutory asset group and apply the allowed method consistently. For a permanent building with an accounting life over 20 years, check whether to use the actual life and the associated notification. Depreciation normally starts in the acquisition expenditure month, or at completion for assets under construction. To start at first use or production for an unused or unproductive asset, obtain the required DJP approval. [PMK 72/2023 arts. 2–6](https://jdih.kemenkeu.go.id/api/download/46cededa-86ae-4cc9-93e5-b6bef8892074/2023pmkeuangan072.pdf).

## Section 7 -- PPh Final Pasal 4(2) Planning

Calculate income subject to a prescribed final tax separately from ordinary tax. Apply the terms of the specific final regime, including the option to elect ordinary rules for eligible UMKM.

### 7.1 Rental of land and/or buildings

- **Rental of land/buildings final tax rate**. 10% of gross rent. [PP 34/2017 art. 4](https://jdih.kemenkeu.go.id/FullText/2017/34TAHUN2017PP.pdf).

**Rental planning strategy table**

| Strategy | Detail |
| --- | --- |
| Gross-up clause in lease | Make the lease state who bears the 10% PPh Final to avoid disputes. [PP 34/2017 art. 4](https://jdih.kemenkeu.go.id/FullText/2017/34TAHUN2017PP.pdf). |
| Service charges | Include maintenance, security, cleaning and other charges related to the leased land or building in the gross base, including under a separate agreement. [PP 34/2017 art. 4(2)](https://jdih.kemenkeu.go.id/FullText/2017/34TAHUN2017PP.pdf). |
| Furnished rental | Include facilities related to the premises. Check the facts before treating a genuinely independent movable-property transaction separately. [PP 34/2017 art. 4](https://jdih.kemenkeu.go.id/FullText/2017/34TAHUN2017PP.pdf) |
| Subleasing | Apply 10% to qualifying gross sublease rent. Do not subtract the rent that the sublessor pays. [PP 34/2017 art. 4](https://jdih.kemenkeu.go.id/FullText/2017/34TAHUN2017PP.pdf) |

### 7.2 Construction services

**Construction services final tax rate table**  _([PP 9/2022 art. 3](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf#page=5))_

| Service type | Certificate | Rate |
| --- | --- | --- |
| Construction work, small business or eligible individual | Qualifying business or competency certificate | 1.75% [PP 9/2022 art. 3](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf) |
| Other construction work | Qualifying certificate | 2.65% [PP 9/2022 art. 3](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf) |
| Construction work | No qualifying certificate | 4% [PP 9/2022 art. 3](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf) |
| Construction consulting | Qualifying certificate | 3.5% [PP 9/2022 art. 3](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf) |
| Construction consulting | No qualifying certificate | 6% [PP 9/2022 art. 3](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf) |
| Integrated construction | With or without a qualifying business certificate | 2.65% with, 4% without [PP 9/2022 art. 3](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf) |

On qualifying payments, compare certified and uncertified rates for the same activity. The differences are 2.25 percentage points for small construction work, 1.35 for other construction work and integrated work and 2.5 for consulting. A qualifying individual can use the applicable competency certificate. Determine whether the actual savings exceed certification costs. [PP 9/2022 art. 3](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf).

### 7.3 Other final categories

- Bank deposit/savings interest generally 20%, with an exception for qualifying unsplit balances up to IDR 7.5M. Taxable bond interest for residents and permanent establishments is generally 10%. Lottery prizes are taxed at 25% of gross value. [PP 131/2000 arts. 2–3](https://jdih.kemenkeu.go.id/api/download/fulltext/2000/131TAHUN2000PP.pdf), [PP 91/2021 arts. 2–3](https://jdih.kemenkeu.go.id/api/download/03829d02-e7a8-4dd6-a7ff-d881f854b218/91TAHUN2021PP.pdf), [PP 132/2000 art. 2](https://peraturan.bpk.go.id/Download/43366/PP%20No.132%20TH%202000.pdf).
- Ordinary stock-exchange sales generally 0.1% of gross sale value, with separate founder-share rules. Qualifying land/building transfers generally 2.5%, with distinct 1% and 0% categories and statutory exemptions. [DJP art. 4(2) guidance](https://www.pajak.go.id/id/pph-pasal-4-ayat-2), [PP 34/2016 arts. 2 and 6](https://jdih.kemenkeu.go.id/api/download/FullText/2016/34TAHUN2016PP.pdf).
- Domestic dividends received by resident individuals follow Section 4.4.

## Section 8 -- BPJS Optimization

Indonesian social security comes in two branches:

### 8.1 BPJS Kesehatan (health) -- Perpres 64/2020

For self-funded PBPU participants, Perpres 64/2020 specifies IDR 150,000 for Class I, IDR 100,000 for Class II and a participant share of IDR 35,000 for Class III after the government contributes IDR 7,000 toward the IDR 42,000 monthly contribution. Check current classification and regulatory transition before quoting a bill. For ordinary wage recipients, the contribution is 5% of insured wages (4% employer and 1% worker) with the general IDR 12M per month ceiling. Check the statutory wage components, relevant minimum and any additional family contributions. [Perpres 64/2020 arts. 30, 32 and 34](https://jdih.djsn.go.id/assets/file/64-bpjs-2020.pdf), [Perpres 82/2018 arts. 33, 35](https://peraturan.bpk.go.id/Download/254897/Perpres%20Nomor%2082%20Tahun%202018.pdf), [Perpres 59/2024](https://jdih.djsn.go.id/assets/file/peraturan%20presiden%20nomor%2059%20tahun%202024.pdf).

### 8.2 BPJS Ketenagakerjaan (employment)

| Programme | Employer | Employee | Wage cap |
| --- | --- | --- | --- |
| JKK (work accident) | 0.24% to 1.74%, by risk class | 0 | No general cap |
| JKM (death) | 0.30%, before any applicable temporary relief | 0 | No general cap |
| JHT (old age) | 3.7% | 2% | No general cap |
| JP (pension) | 2% | 1% | Adjusted annually. The 2026 contribution wage ceiling is not yet confirmed here. Verify the operative BPJS notice for the payroll month. |

Calculate JP using the prescribed wage base, including its cap. The published pension benefit limits are separate figures. Self-employed individuals can have employment cover through the non-wage participant route, including JKK, JKM and optional JHT. [PP 45/2015 art. 29](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104556_PP%2045%20Tahun%202015.pdf), [BPJS non-wage participants](https://www.bpjsketenagakerjaan.go.id/bukan-penerima-upah.html).

### 8.3 BPJS and tax

| Payment | Income tax treatment |
| --- | --- |
| Employer contribution | Apply the ordinary business expense and payroll rules to the actual programme. Income Tax Law art. 6(1)(c) specifically addresses qualifying pension fund contributions. Employer-paid health, accident and death premiums are included in employee gross income under PMK 168/2023 where prescribed. |
| Worker contribution | Deduct qualifying employee pension and old-age contributions through the employer from the final annual PPh 21 net calculation. Interim TER ordinarily uses gross remuneration. Employee health contributions do not reduce that base. |
| Individual's own health contribution | Generally a personal cost. Assess employer contributions for genuine employees separately under ordinary tax and payroll rules. |

[Income Tax Law arts. 6 and 9](https://jdih.kemenkeu.go.id/api/download/fulltext/2008/36TAHUN2008UU.htm), [PMK 168/2023 arts. 5 and 9–10](https://jdih.kemenkeu.go.id/api/download/e60a82e0-b218-40f5-9d18-b924aa1e11ce/2023pmkeuangan168.pdf).

[PP 44/2015](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104557_PP%2044%20Tahun%202015.pdf), [PP 49/2023](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/Salinan_PP_Nomor_49_Tahun_2023.pdf) and [PP 46/2015](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104556_PP%2046%20Tahun%202015.pdf) set the JKK, JKM and JHT contribution rules.

## Section 9 -- Year-End Timing of Expenses & Income Recognition

Apply the permitted accrual or cash basis consistently for tax books. Changes of basis require approval. Check the conditions of the simplified cash method for the qualifying individual. The UMKM base is eligible gross income received or obtained under the applicable basis. [KUP art. 28(5)–(6)](https://jdih.kemenkeu.go.id/api/download/50e4f976-7d46-4bbc-9230-e213a1674197/SDSN%20Pajak.pdf), [PMK 81/2024 arts. 456–458](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf), [PP 55/2022 arts. 56 and 60](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf).

### 9.1 Income deferral techniques (accrual basis)

**Income deferral techniques table**

| Technique | Notes |
| --- | --- |
| January invoice | Recognise income on the applicable basis. Later invoicing alone cannot defer income already earned in December on accrual. |
| Project milestones | Assess actual performance and contractual rights under the applicable accounting and tax rules. |
| Advance receipt | Assess whether it is a refundable liability, consideration or earned income under the facts and applicable basis. |
| Accrued discount | Check the contract and the date all conditions are met. |

### 9.2 Expense acceleration techniques

**Expense acceleration techniques table**

| Technique | Notes |
| --- | --- |
| Prepay annual contracts in December | Under accrual, only the portion accruing to current year is deductible (unless service fully delivered in year). |
| Year-end bonus | Check when the amount is an allowable accrued expense. Withholding applies when paid or due, as prescribed. [PMK 168/2023 art. 19](https://jdih.kemenkeu.go.id/api/download/e60a82e0-b218-40f5-9d18-b924aa1e11ce/2023pmkeuangan168.pdf). |
| Asset purchase | Apply the month of acquisition expenditure or the applicable exception in Section 6.3. |
| Bad debt write-off | Check the statutory debt list and separate recovery-evidence conditions or applicable exception. |
| R&D or vocational training | Apply the eligibility and scheme conditions in Section 6.1. |

### 9.3 Notifications

Ordinary taxation is the election for an otherwise eligible UMKM taxpayer. A continuing taxpayer notifies DJP by the end of the tax year for the next tax year. A new registration can elect ordinary taxation on registration. Check the distinct NPPN notice deadlines in Section 3. Compare projected revenue and margins before the relevant notice date. [PMK 164/2023 art. 5](https://jdih.kemenkeu.go.id/api/download/a99b8e80-9694-46ab-8de1-63c2484aa636/2023pmkeuangan164.pdf), [PMK 81/2024 art. 450](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf).

## Worked cases

### Software developer break-even

### Setup

Single Indonesian-resident individual carrying on computer programming activities (KLU 62010) in Jakarta:

- Gross business receipts of IDR 1.2 billion.
- Allowable ordinary operating expenses of IDR 200 million, leaving an 83.33% actual margin.
- The NPPN example assumes 50% for the exact KLU and valid notification.
- TK/0 gives IDR 54 million PTKP.
- Test UMKM separately. Establish that these meet the qualifying business income tests, including the independent professional income exclusions, and that art. 57 and any transition are satisfied.

### Option A -- Eligible UMKM Final

If legally available, PPh = 0.5% × (1,200,000,000 − 500,000,000) = IDR 3,500,000. [PP 55/2022 art. 60](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf), [PP 20/2026 arts. 56–57 and art. II](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf).

### Option B -- Progressive PPh with NPPN

- **Option B calculation**. Deemed net = 50% × 1,200,000,000 = 600,000,000. Taxable = 600,000,000 − 54,000,000 = 546,000,000. PPh (brackets 5/15/25/30): 3,000,000 + 28,500,000 + 62,500,000 + 13,800,000 = IDR 107,800,000.

### Option C -- Progressive PPh with Pembukuan

- **Option C calculation**. Actual net = 1,200,000,000 − 200,000,000 = 1,000,000,000. Taxable = 1,000,000,000 − 54,000,000 = 946,000,000. PPh: 3,000,000 + 28,500,000 + 62,500,000 + 133,800,000 = IDR 227,800,000.

### Verdict

**Verdict comparison table**

| Regime | PPh (IDR) | Effective rate on revenue and source |
| --- | --- | --- |
| **UMKM Final 0.5% if eligible** | **3,500,000** | 0.29% [PP 55/2022 art. 60](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf) |
| Progressive + NPPN | 107,800,000 | 8.98% [PPh art. 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) |
| Progressive + Pembukuan | 227,800,000 | 18.98% [PPh art. 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) |

The lowest computed amount is available only when the taxpayer and income qualify for UMKM. For excluded professional receipts, compare NPPN where available and ordinary bookkeeping. Verify eligibility each year using the prevailing rules.

### Break-even

At IDR 1.2 billion revenue and TK/0, ignoring statutory thousand-rupiah rounding, ordinary PPh equals IDR 3.5 million when taxable income is about IDR 63.333 million: IDR 3 million on the first IDR 60 million and 15% on approximately IDR 3.333 million. Adding PTKP gives about IDR 117.333 million net, a margin near 9.78%. Actual break-even varies with the income, allowance and other amounts entering ordinary tax.

With NPPN at 50%, compare applying ordinary rates to deemed net and actual net. A lower net cannot increase ordinary tax on these assumptions. Both calculations can tie when below PTKP or on the same rounded taxable amount. [Income Tax Law arts. 14 and 17](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf), [PMK 101/PMK.010/2016 art. 1](https://jdih.kemenkeu.go.id/api/download/FullText/2016/101~PMK.010~2016Per.pdf).

```oa-check
name: Compare Indonesian final, deemed and actual profit regimes
inputs:
  turnover: 1200000000
  qualifying_expenses: 200000000
  exempt_band: 500000000
  final_rate: 0.005
  norm: 0.50
  ptkp: 54000000
  first_band: 60000000
  second_band: 190000000
  third_band: 250000000
  first_rate: 0.05
  second_rate: 0.15
  third_rate: 0.25
  fourth_rate: 0.30
steps:
  - final_tax: (turnover - exempt_band) * final_rate
  - norm_taxable: turnover * norm - ptkp
  - actual_taxable: turnover - qualifying_expenses - ptkp
  - tax_first_three: first_band * first_rate + second_band * second_rate + third_band * third_rate
  - ceiling_first_three: first_band + second_band + third_band
  - norm_tax: tax_first_three + (norm_taxable - ceiling_first_three) * fourth_rate
  - actual_tax: tax_first_three + (actual_taxable - ceiling_first_three) * fourth_rate
expected:
  final_tax: 3500000
  norm_taxable: 546000000
  actual_taxable: 946000000
  norm_tax: 107800000
  actual_tax: 227800000
```

## Section 11 -- Conservative Defaults

**Conservative defaults table**

| Scenario | Default |
| --- | --- |
| UMKM eligibility unclear | Confirm the past registrations, activities, turnover and applicable transition. If corrections are necessary, identify the applicable KUP sanction and the ministerial rate at the relevant start date. KUP art. 19 uses a variable rate, generally capping the specified interest at 24 months and counting part-months as full. [Consolidated KUP art. 19](https://jdih.kemenkeu.go.id/api/download/50e4f976-7d46-4bbc-9230-e213a1674197/SDSN%20Pajak.pdf). |
| NPPN activity or location unclear | Verify the actual code and statutory geographic class. Mark the calculation not yet confirmed while evidence is missing. |
| Mixed business and employment income | Separate qualifying final income and calculate ordinary tax on the appropriate ordinary receipts. |
| Missing Coretax family data | Gather the evidence applicable at the start of the tax year or part-year and reconcile the Coretax record. |
| Spouse earns income | Apply default joint rules and check the one-employer exception or PH, MT or HB facts under art. 8. |
| Asset purchase | Capitalise qualifying expenditure with a useful life exceeding one year. Apply the approved tax depreciation treatment. |
| No evidence of qualifying entertainment or incentive spend | Obtain the requisite business records and satisfy the underlying statutory conditions. |
| Individual domestic dividend | Check the amount, qualifying investment, timing and reports from Section 4.4. |
| Mixed rental contract | Apply 10% final to the gross related amounts, including lease-related services billed separately. |

## When to refuse or refer

- **R-1**. Treaty shopping and conduit arrangements. [PMK 112/2025](https://jdih.kemenkeu.go.id/dok/pmk-112-tahun-2025).
- **R-2**. Controlled foreign companies. [PMK 93/2019](https://jdih.kemenkeu.go.id/dok/93-pmk-03-2019).
- **R-3**. Transfer pricing structures, intra-group services and royalty restructuring. [PMK 172/2023](https://www.jdih.kemenkeu.go.id/api/download/b0b74668-cf4d-456b-bb23-be5e1aeac2cb/2023pmkeuangan172.pdf).
- **R-4**. Tax amnesty or voluntary disclosure participation.
- **R-5**. Companies without substantive operations and arrangements that depend on form overriding substance. [PP 55/2022 art. 32](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf).
- **R-6**. Artificial split invoicing between an individual and a controlled company. Check Income Tax Law art. 18 and PP 20/2026 arts. 57–58.
- **R-7**. Sector-specific regimes for mining, oil and gas, plantations and financial services.
- **R-8**. Property development. [PP 34/2016](https://jdih.kemenkeu.go.id/api/download/FullText/2016/34TAHUN2016PP.pdf).
- **R-9**. Marketplace seller VAT and designated platform collection of PPh 22. [DJP guidance on PMK 37/2025](https://pajak.go.id/id/tentang-pajak/marketplace).
- **R-10**. Cryptocurrency mining and staking. [PMK 50/2025](https://jdih.kemenkeu.go.id/api/download/66a7633b-9e1b-4a54-9046-5320aa96c7e1/2025pmkeuangan050.pdf) applies from 1 August 2025.

## Sources

| Official source | Provisions checked | Read on |
| --- | --- | --- |
| [UU 7/2021](https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf) | Arts. 2–3, amendments to KUP and PPh | 2026-11-24 |
| [Consolidated KUP](https://jdih.kemenkeu.go.id/api/download/50e4f976-7d46-4bbc-9230-e213a1674197/SDSN%20Pajak.pdf) | Arts. 3, 19 and 28, returns, interest and records | 2026-11-24 |
| [UU 36/2008](https://jdih.kemenkeu.go.id/api/download/fulltext/2008/36TAHUN2008UU.htm) | Arts. 6–9, 11, 14, 17, 25 and 31E, read with the later amendments | 2026-11-24 |
| [Company Law](https://peraturan.bpk.go.id/Download/29563/UU%20Nomor%2040%20Tahun%202007.pdf) | Arts. 1, 3 and 68, legal structure and audit | 2026-11-24 |
| [PP 8/2021](https://jdih.kemenkeu.go.id/api/download/680a952b-3f39-4e9c-86ea-4e4e1d1470e4/8TAHUN2021PP.pdf) | Arts. 3–5, authorised and paid capital | 2026-11-24 |
| [PP 45/2024](https://peraturan.bpk.go.id/Download/365416/PP%20Nomor%2045%20Tahun%202024.pdf) | Annex I item 28, one-person company fee | 2026-11-24 |
| [PP 55/2022](https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf) | Arts. 32 and 56–62, substance and former final tax | 2026-11-24 |
| [PP 20/2026](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf) | Arts. 56–58 and art. II, scope and transition | 2026-11-24 |
| [PMK 164/2023](https://jdih.kemenkeu.go.id/api/download/a99b8e80-9694-46ab-8de1-63c2484aa636/2023pmkeuangan164.pdf) | Arts. 5–8, elections and settlement | 2026-11-24 |
| [PMK 81/2024](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf) | Arts. 448–458, NPPN and bookkeeping | 2026-11-24 |
| [PMK 101/PMK.010/2016](https://jdih.kemenkeu.go.id/api/download/FullText/2016/101~PMK.010~2016Per.pdf) | Art. 1, PTKP | 2026-11-24 |
| [PER-17/PJ/2015](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto) | Arts. 4 and 6, NPPN regions and calculation | 2026-11-24 |
| [PMK 18/2021](https://jdih.kemenkeu.go.id/api/download/39fdb2fc-1736-4ebb-80f5-d257f75df0b5/18~PMK.03~2021Per.pdf) | Arts. 34–41, dividend investment and reporting | 2026-11-24 |
| [PP 19/2009](https://jdih.kemenkeu.go.id/api/download/fulltext/2009/19TAHUN2009PP.htm) | Art. 1, individual domestic dividend rate | 2026-11-24 |
| [PMK 72/2023](https://jdih.kemenkeu.go.id/api/download/46cededa-86ae-4cc9-93e5-b6bef8892074/2023pmkeuangan072.pdf) | Arts. 2–6, asset classes and timing | 2026-11-24 |
| [PP 34/2017](https://jdih.kemenkeu.go.id/FullText/2017/34TAHUN2017PP.pdf) | Art. 4, gross rental base | 2026-11-24 |
| [PP 9/2022](https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf) | Art. 3, construction rates | 2026-11-24 |
| [PMK 168/2023](https://jdih.kemenkeu.go.id/api/download/e60a82e0-b218-40f5-9d18-b924aa1e11ce/2023pmkeuangan168.pdf) | Arts. 5, 9–10 and 19, payroll amount and timing | 2026-11-24 |
| [PER-12/PJ/2026](https://pajak.go.id/id/peraturan/yNdK4DJlB8-per-12-pj-2026) | Art. II, Coretax reporting transition | 2026-11-24 |

Use the current Coretax individual or corporate annual return and the applicable payroll withholding certificates. [DJP Coretax filing guidance](https://pajak.go.id/id/coretaxpedia/penghasilan-dalam-pelaporan-spt-tahunan).

**Not yet confirmed:** The 2026 JP contribution wage ceiling, Annex I NPPN rates for unspecified legal, consulting, restaurant or construction activities and the exact text of the older nominative entertainment circular. Check the actual issue or refer the affected calculation.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (Konsultan Pajak bersertifikat A/B/C, Akuntan Publik, or other Indonesian-licensed practitioner) before filing or acting upon.
