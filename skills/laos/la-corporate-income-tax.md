---
name: la-corporate-income-tax
description: "Lao PDR profit tax, tax year 2026, from the revised Law on Income Tax (Decree 145/PO, 2025): 20% standard rate, domestic minimum top-up to 15% for multinational groups, increased rates for tobacco and alcohol (22%), casinos (30%) and mining (35%), reduced 5%, 7% and 10% rates, and the commencement-date question; old-law lump-sum and withholding figures held for confirmation."
version: 1.1
jurisdiction: LA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Laos corporate income tax (profit tax)

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file or take a position without professional review.

## Who this applies to

Enterprises and other legal entities liable to profit tax in Lao PDR. The governing law is the Law on Income Tax (Revised), adopted by National Assembly Resolution No. 164/NA of 25 June 2025 and promulgated by Presidential Decree No. 145/PO of 6 August 2025; it replaces Law No. 67/NA of 18 June 2019. Article 74 names 1 September 2025 as the commencement date and refers to promulgation and publication; the Lao Official Gazette register records publication on 19 June 2026. Which rules govern a period or transaction falling between those dates needs a Lao practitioner. Payroll income tax is in [payroll](la-payroll-social.md).

## Rates, bands and thresholds

| Item | Rate | Tax year | Official URL |
|---|---|---|---|
| Standard profit tax (art. 15) | 20% | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| Domestic minimum top-up, multinational group members whose effective rate is below 15% (art. 15) | Top up to 15% | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| Tobacco products: producing, importing, selling (art. 16(1.1)) | 22%, of which 2% to the Tobacco Control Fund | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| Alcoholic beverages: producing, importing, selling (art. 16(1.2)) | 22%, of which 2% to the health promotion fund | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| Casino business (art. 16(1.3)) | 30% | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| Mineral exploration and extraction concessions, and mineral exporters (art. 16(1.4)) | 35% | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| Research and innovation, modern hospitals, medicines and medical equipment, traditional medicine, after the investment-law exemption ends (art. 16(2.1)) | 5% | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| Innovative, environmentally friendly technology, natural-resource protection and clean energy in production, after the exemption ends (art. 16(2.2)) | 7% | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| Companies listed on the securities exchange, for 10 years from listing (art. 16(2.3)) | 10% | 2026 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |

The Law gives each rate in words and digits. After the 10-year listing period the ordinary rate applies. Education and other activities outside art. 16 follow the investment-promotion law and other rules (text after art. 16(2.3)).

## The base

Profit tax falls on annual taxable profit (art. 14, with the art. 17 non-taxable receipts and art. 18 non-deductible expenses). Domestic enterprises are taxed on worldwide income and foreign enterprises on Lao-source income (old-law position, not re-read). The domestic minimum top-up applies to a legal entity in a multinational group where the effective tax actually paid by all its legal entities is below 15% under international rules; the procedures are left to separate regulations, not read here.

Small businesses that do not keep full accounts paid a lump-sum tax on turnover under the old Law No. 67/NA; those figures are on the Not yet confirmed line.

## Deadlines and filing

Ryan Duguid's reading: the annual profit tax return is due by 20 January of the following year, and financial statements by 31 March after a 31 December year end (Tax Administration Law and Accounting Law; not reopened). The Lao Tax Department publishes notices each year; check the current one.

## Penalties and interest

Not read for this guide (Tax Administration Law).

## Cross-border points

Payments to non-residents: the old law and a secondary summary gave withholding of 10% on dividends, interest, services, rent and performers, 5% on royalties and 2% on share transfers, and a separate final foreign withholding tax on foreign contractors bundling deemed profit (1.4% agriculture, 2% industry, 3% commerce and services, 6% electricity and minerals) with 10% VAT on services. The revised Law's art. 38 sets the same 10%, 5% and 2% rates for individuals by income type, but its regime for legal-entity payees was not read; all of these are on the Not yet confirmed line. The top-up rule interacts with foreign Pillar Two rules; see the separate regulations.

## Two worked examples that recompute

**1. Ordinary enterprise, taxable profit LAK 1,000,000,000.** Profit tax at 20% = LAK 200,000,000 (derived).

```oa-check
name: Laos standard profit tax
inputs:
  profit: 1000000000
steps:
  - tax: profit * 0.20
expected:
  tax: 200000000
```

**2. Beer producer, taxable profit LAK 500,000,000.** Profit tax at 22% = LAK 110,000,000, of which 2% of profit (LAK 10,000,000) goes to the health promotion fund (derived).

```oa-check
name: Laos alcohol producer profit tax
inputs:
  profit: 500000000
steps:
  - tax: profit * 0.22
  - fund_share: profit * 0.02
expected:
  tax: 110000000
  fund_share: 10000000
```

## Ask the client first

- Which activity (tobacco, alcohol, casino, mining, research, health, clean technology, listed)?
- Is an investment-law profit-tax exemption running, and when does it end?
- Accounting period, and does any part fall before 19 June 2026?
- Member of a multinational group, and its effective tax rate?
- Payments to non-residents?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on Income Tax (Revised), Lao Official Gazette scan, arts 15 and 16 on printed pages 7 and 8 (Read as rendered pages for every rate in the table) | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf | 2026-11-14 |
| Lao Official Gazette, Ministry of Finance register (Read by Ryan Duguid for the 19 June 2026 publication record) | https://laoofficialgazette.gov.la/index.php?r=site/listlegistioncp&agencies_id=2&old=0 | 2026-11-11 |

Not yet confirmed: the period between 1 September 2025 (art. 74) and publication on 19 June 2026; the top-up regulations; the lump-sum regime under the revised Law (old Law 67/NA: turnover up to LAK 50 million exempt; LAK 50 million to 400 million at 1% manufacturing and agriculture, 2% commerce, 3% services); withholding on payments to legal entities and non-residents and the foreign contractor regime (figures above, old law and secondary sources); the 20 January return and 31 March financial statement dates; penalties. The old guide's 13% rate for 4 years for listed companies and "education 5%" are not in the revised Law.
