---
name: nepal-income-tax
description: "Use this skill whenever asked about Nepal income tax for natural persons (individuals and the self-employed). Trigger on phrases like \"how much tax do I pay in Nepal\", \"Nepal income tax slabs\", \"D-01 return\", \"PAN income tax\", \"SSF contribution\", \"Social Security Fund\", \"presumptive tax Nepal\", \"turnover tax\", \"tax rate FY 2082/83\", \"natural person tax\", \"income tax return Nepal\", \"TDS Nepal\", or any question about filing or computing income tax for a resident natural person, sole proprietor, or small business in Nepal. Also trigger when preparing or reviewing a D-01 return, computing the 1% Social Security Tax slab, applying the female-taxpayer rebate, or advising on advance/installment tax. This skill covers natural-person slabs (single/couple), the SST mechanism, SSF contributions, presumptive and turnover-based small-business regimes, deductions/rebates, filing deadlines, and penalties under the Income Tax Act, 2058. ALWAYS read this skill before touching any Nepal income tax work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nepal-income-tax"
  jurisdiction: "NP"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# Nepal individual income-tax computation

## Who this applies to

Resident natural persons, including registered sole proprietors, preparing an annual income-tax working paper. Companies and partnerships use `nepal-corporate-tax`; withholding uses `nepal-tds`, salary processing and SSF use `nepal-payroll`, and VAT uses `nepal-vat`. The existing corporate file has separate historical coverage and approval; do not infer a current corporate rate from this individual computation.

Calendar 2026 includes FY 2082/83 (2025/26) and FY 2083/84 (2026/27), each Shrawan 1 through Ashad-end. Finance Act 2083 section 57 changes the personal scale from **Shrawan 1, 2083**. Do not apply the new scale retrospectively to the earlier income year. This is a source-cited draft without accountant approval. [Enacted Finance Act §1(2), §57](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=1).

A resident individual is one whose normal abode is in Nepal, who is present in Nepal for at least **183 days in a continuous 365-day period**, or who is posted abroad by the Nepal Government during the income year. The day test is not simply presence within one fiscal year. Residents generally bring worldwide assessable income into the computation; non-residents bring Nepal-source income, subject to statutory exemptions/final withholding. [Act §2(कङ)(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=11); [§6](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=19).

## Rates, bands and thresholds

### Current FY 2083/84 scale

Same scale for a natural person or an electing couple. The first-band charge applies to employment income and is excluded for registered sole proprietors, pension income and the statutory pension/SSF-contributor cases. Establish the actual exception; absence of SSF evidence does not authorise invented tax. Figures stated as words in the Act are rendered in numerals below (in words on the page). Cumulative amounts and the final marginal rate are derived, with the statutory first-band charge included; remove that charge where the exception applies.

| Annual taxable-income slice | Marginal rate | Cumulative tax at upper end, derived | Official provision |
|---|---|---|---|
| First NPR 1,000,000 of employment taxable income | 1%, subject to the stated exceptions | NPR 10,000 | [§57(26)(क), Schedule 1 §1(1)(क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=198) (in words on the page) |
| Above NPR 1,000,000 through NPR 1,500,000 | 10% | NPR 60,000 | [Schedule 1 §1(1)(ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=198) (in words on the page) |
| Above NPR 1,500,000 through NPR 2,500,000 | 20% | NPR 260,000 | [Schedule 1 §1(1)(ग)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=198) (in words on the page) |
| Above NPR 2,500,000 through NPR 4,000,000 | 27% | NPR 665,000 | [Schedule 1 §1(1)(घ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=198) (in words on the page) |
| Above NPR 4,000,000 | 29%, derived: 27% plus 2 percentage points on the excess | No upper limit | [Schedule 1 §1(1)(घ)-(ङ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=198) |

Apply marginal slices, not the top percentage to the entire income. Couple election under section 50 still requires both resident spouses' written notice and carries joint/several responsibility, but the separate higher couple band is deleted for this current period. A resident widow/widower supporting dependants has the statutory couple treatment. [§50(1)-(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=70); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=71); [§57(26)(ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=198).

### Historical FY 2082/83 scale, only for the labelled earlier-year cases

| Single slice | Rate | Cumulative tax at upper end, derived, including first-band employment charge | Official source |
|---|---|---|---|
| First NPR 500,000 | 1%, with statutory exceptions | NPR 5,000 | [Schedule 1 §1(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=157) (in words on the page) |
| Next NPR 200,000, through NPR 700,000 | 10% | NPR 25,000 | [Schedule 1 §1(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=157) (in words on the page) |
| Next NPR 300,000, through NPR 1,000,000 | 20% | NPR 85,000 | [Schedule 1 §1(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=157) (in words on the page) |
| Next NPR 1,000,000, through NPR 2,000,000 | 30% | NPR 385,000 | [Schedule 1 §1(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=157) (in words on the page) |
| Next NPR 3,000,000, through NPR 5,000,000 | 36%, derived from 30% plus a 20% increase in that rate | NPR 1,465,000 | [Schedule 1 §1(1)(ङ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=157) |
| Above NPR 5,000,000 | 39%, derived from 30% plus a 30% increase in that rate | No upper limit | [Schedule 1 §1(1)(ङ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=157) |

| Electing couple slice | Rate | Cumulative tax at upper end, derived, including first-band employment charge | Official source |
|---|---|---|---|
| First NPR 600,000 | 1%, with statutory exceptions | NPR 6,000 | [Schedule 1 §1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=158) (in words on the page) |
| Next NPR 200,000, through NPR 800,000 | 10% | NPR 26,000 | [Schedule 1 §1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=158) (in words on the page) |
| Next NPR 300,000, through NPR 1,100,000 | 20% | NPR 86,000 | [Schedule 1 §1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=158) (in words on the page) |
| Next NPR 900,000, through NPR 2,000,000 | 30% | NPR 356,000 | [Schedule 1 §1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=158) (in words on the page) |
| Next NPR 3,000,000, through NPR 5,000,000 | 36%, derived as above | NPR 1,436,000 | [Schedule 1 §1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=158) |
| Above NPR 5,000,000 | 39%, derived as above | No upper limit | [Schedule 1 §1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=158) |

### Deductions and credits

| Item and condition | Limit/treatment | Official source |
|---|---|---|
| Actual contributions to a qualifying approved retirement fund, combined across funds; identify retirement-qualifying amounts from EPF/CIT/SSF/pension statements | Lower of actual qualifying contribution, 1/3 of assessable income, or NPR 500,000; both periods | [§63](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=82); [Rule 21](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AF%20(%E0%A4%B8%E0%A5%8B%E0%A4%B9%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7kddd2d.pdf#page=8) (in words on the page) |
| Investment/life insurance premium of a resident individual within Schedule 1 §1(12) | Lower of annual premium or NPR 40,000 | [Schedule 1 §1(12)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=161) (in words on the page) |
| Health insurance with a resident insurer | Lower of annual premium or NPR 20,000 | [Schedule 1 §1(16)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=162) (in words on the page) |
| Insurance of the resident individual's own private building with a resident insurer | Lower of annual premium or NPR 5,000 | [Schedule 1 §1(16क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=162) (in words on the page) |
| Donation to an IRD-approved tax-exempt organisation under §12, absent a special Gazette provision | Lower of actual eligible gift, 5% of adjusted taxable income, or NPR 300,000 in FY 2083/84; the earlier-year monetary limit is NPR 100,000 | [§12(1)-(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=33); [§57(6)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=191) (in words on the page) |
| Eligible remote-area allowance; establish government area classification | Categories A/B/C/D/E: NPR 50,000 / 40,000 / 30,000 / 20,000 / 10,000 | [Schedule 1 §1(5)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=160); [Rule 38](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AF%20(%E0%A4%B8%E0%A5%8B%E0%A4%B9%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7kddd2d.pdf#page=14) (in words on the page) |
| Resident pension income | Additional deduction of 25% of the applicable first band, limited to actual pension under Rule 39; current band gives NPR 250,000, derived; earlier single/couple give NPR 125,000 / 150,000, derived | [Schedule 1 §1(9क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=161); [Rule 39](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AF%20(%E0%A4%B8%E0%A5%8B%E0%A4%B9%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7kddd2d.pdf#page=14); [§57(26)(ङ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=199) |
| Resident individual with statutory disability status | Additional 50% of the relevant first band; current NPR 500,000, derived; earlier single/couple NPR 250,000 / 300,000, derived; establish evidence | [Schedule 1 §1(10)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=161); [§57(26)(च)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=199); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=200) |
| Nepal foreign diplomatic-mission employee's foreign allowance | Exclude 75%; include 25%, derived; not a general expatriate salary exemption | [Schedule 1 §1(6)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=160) |
| Resident woman with remuneration-only income | 10% reduction of the applicable computed tax; do not apply to business/mixed-income cases | [Schedule 1 §1(11)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=161) |
| Approved medical-treatment expenditure under §51 and Rule 17; exclude cosmetic surgery and insurance-reimbursed costs | Credit: lower of 15% of eligible expenditure plus usable carry-forward, NPR 1,500, and available tax liability; excess subject to §51(4) carry-forward | [§51](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=71); [Rule 17](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AF%20(%E0%A4%B8%E0%A5%8B%E0%A4%B9%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7kddd2d.pdf#page=7) (in words on the page) |

These are deductions/credits with different bases; do not deduct a credit from income or claim the same cost twice. The retirement limit uses assessable income, not the already reduced taxable base. Do not assume every amount labelled SSF is retirement-qualifying; obtain its scheme allocation and annual statement.

## The base

### Computation in order

1. Fix the income year, residence and entity form; obtain the full income record, not just one account.
2. Classify employment, business, investment and statutory windfall gains. Establish which receipts form part of assessable income. Employment includes salary, bonus, allowances, overtime, benefits and employer retirement contributions under §8, subject to statutory exclusions. A net salary bank credit does not establish gross taxable remuneration. From Shrawan 1, 2083, remuneration in the form of sweat shares from employment in an information-technology industry is excluded to the extent specified by the new section 8(3)(ङ); do not treat it as automatically taxable cash salary. [Finance Act §57(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=190). Final-withholding and exempt income must not be taxed again through ordinary slabs. [§§6-9](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=19); [§8](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=20); [§8 exclusions](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=21).
3. Compute business/investment profit with supported production-of-income expenses, capital allowances and required adjustments. Section 13 requires expenditure incurred by the taxpayer in the income-producing business/investment during the year; a supplier keyword cannot prove it. [§13](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=34).
4. Remove private/domestic costs, income tax, statutory fines/penalties, costs of exempt/final-tax receipts and disallowed capital expenditure, subject to the Act's exceptions. Do not import a VAT entertainment block into income tax: the income-tax production test and private-cost exclusion must be established. [§21(1),(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=42); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=43).
5. Apply approved retirement/insurance/donation deductions, additional allowances and the proper year scale; then eligible credits, including evidenced non-final TDS/instalments. Do not expense tax credits or use unsupported deductions.
6. Reconcile tax payable/refund to certificates and receipts; make the practitioner-review assumptions and unresolved items explicit.

From Shrawan 1, 2083, section 21(2)'s cash-payment restriction applies to a payment above **NPR 25,000** by any person, with the statutory exceptions for specified government/bank recipients, qualifying primary farmers/producers, retirement payments, unavailable/closed banking or unavoidable cash circumstances, and deposits into the recipient's bank account. The old turnover-based NPR 50,000 rule is historical, not the current deduction test. Separate employee-PAN, invoice-PAN and salary-bank-payment requirements in §21 also need checking; evidence of business purpose alone is insufficient. [§21(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=42); [exceptions](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=43); [§57(8)(क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=191).

### Capital assets and bad debts

Capitalise durable computers, office equipment, furniture and vehicles rather than treating every purchase as a recurring subscription. Schedule 2 classifies buildings/structures (A), computers/data-processing equipment/furniture/office equipment (B), automobiles/buses/minibuses (C), other listed plant/equipment (D) and separate intangible assets (E). Standard annual pool rates are **5%, 25%, 20%, 15%** respectively; intangibles use the statutory useful-life method, not a guessed pool percentage. These numerals come from the Schedule table. [Schedule 2 §1](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=165); [§3](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=168).

Depreciation is rate × statutory pool base after additions/disposals. Addition timing uses the later inclusion/incurrence point: first part of the year through Poush-end takes 3/3 of cost, Magh-Chaitra 2/3 and Baisakh-year-end 1/3; the remaining part joins next year, subject to the pool not dissolving. A remaining A-D balance below NPR 2,000 is additionally written off. Special accelerated/immediate allowances are exceptions requiring their own statutory eligibility; never make either full expensing or depreciation universal. [Schedule 2 §2(2)-(6)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=166); [timing](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=167); [small pool and special allowances](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=168).

For bad debts, the original income must have been recognised on the relevant accrual basis. Adjust at an eligible write-off/waiver under §25; outside banking/financial-institution prescribed rules, take all appropriate recovery steps and reasonably conclude the debt is unrecoverable. A cash-basis unpaid invoice cannot be deducted as an expense already recognised. [§25(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=47); [§25(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=48).

### Mixed use and unsupported legacy claims

Home-office rent/utilities, vehicle fuel/parking and telephone/internet need evidenced income-producing use and exclusion of private costs. A floor-area calculation or logbook is supporting evidence, not an automatic legal safe harbour. Hold unsupported portions; do not invent a business-use percentage. The old exclusive-room requirement and an extra senior-citizen deduction are not established by the official text read and are excluded pending confirmation under Sources. Female credit, remote-area classification, disability and pension relief each require their own eligibility evidence.

### Small-business alternatives

| Regime and all statutory eligibility conditions | Computation | Official source |
|---|---|---|
| Fixed/presumptive: resident natural person with Nepal-source business income only; taxable business income no more than NPR 300,000 and turnover no more than NPR 3,000,000; no §51 medical or §93 withholding credit claim; elect the regime for the year | Metro/sub-metro NPR 7,500; municipality NPR 4,000; other area NPR 2,500 | [§4(4),(4ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=17); [election](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=18); [Schedule 1 §1(7)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=160) (in words on the page) |
| Turnover regime: resident natural person with Nepal-source business income only; taxable business income no more than NPR 1,000,000, turnover above NPR 3,000,000 through NPR 10,000,000; elect for the year; excluded specialist/consultancy income does not qualify | First NPR 3,000,000 carries the relevant fixed-area tax; apply the applicable excess-turnover slices below | [§4(4क),(4ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=18); [Schedule 1 §1(17)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=163) (in words on the page) |
| Low-margin goods business with commission/value addition no more than 3%, including qualifying gas/cigarette trading | Excess turnover above NPR 3,000,000 through NPR 5,000,000: 0.25%; excess above NPR 5,000,000 through NPR 10,000,000: 0.30% | [Schedule 1 §1(17)(क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=163) (in words on the page) |
| Other qualifying non-service business | Corresponding excess slices: 1% then 0.80% | [Schedule 1 §1(17)(ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=163) (in words on the page) |
| Qualifying service business | 2% on the turnover above the first NPR 3,000,000; the first slice remains the fixed-area tax | [Schedule 1 §1(17) opening and (ग)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=163) (in words on the page) |

Excluded turnover-regime specialist/consultancy income includes doctors, engineers, auditors, lawyers, sportspersons, artists and consultants. Do not extend the specific section 4(4क) exclusion into an invented blanket section 4(4) prohibition: the fixed regime has its own statutory tests, which must all be established. A profession/turnover alone is insufficient to assign any regime. VAT registration/mandatory-registration interaction must also be reviewed through `nepal-vat`; an income-tax concession does not excuse VAT. The old vague "0.30%-1.00%, commonly 0.75%" is replaced by the exact statutory slices.

### Common withholding categories retained

Use `nepal-tds` for the original dividend, bank-interest, rent, service-fee, commission, contract and **meeting/sitting fee** triggers. A meeting fee within section 88 service fees ordinarily uses the residual rate, subject to the category/payer exclusions; the listed per-meeting final-tax allowance condition is separate. Do not lose that category or assume all casual fees are employment income. [§2(कम), continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=16); [§88(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=107); [§92(1)(ज)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=116).

### Transaction pattern library retained

Match case-insensitive descriptions, including Nepali/romanised equivalents, most-specific pattern first. These are **classification cues**, not deterministic proof of deductibility, source, gross income or final withholding. An unmatched item goes to evidence-based review. A settlement may duplicate a sale already recorded, and a platform's foreign location does not itself decide statutory source or special final-tax eligibility.

#### 3.1 Income Patterns (Credits)

**Income patterns table**

| Pattern | Working-paper route | Notes |
| --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED, BHUKTANI | Business income | Core self-employment revenue |
| PARAMARSHA, CONSULTANCY, PROFESSIONAL FEE, SEWA SHULKA | Business income | Service fees |
| ESEWA, KHALTI, IMEPAY PAYOUT | Business income | Digital-wallet settlement ; match to invoices |
| FONEPAY, CONNECTIPS SETTLEMENT | Business income | Payment-gateway settlement |
| UPWORK, FIVERR, PAYONEER, WISE PAYOUT | Review business/source classification | Freelance platform ; confirm FX and remittance docs |
| TALAB, SALARY, PARISHRAMIK, [employer] | Employment income | Goes to assessable employment income, not business |
| GHAR BHADA, RENT RECEIVED | Rental/investment review | Identify natural-person house rent and local tax; no blanket federal TDS |
| BYAJ, INTEREST RECEIVED | Investment income | Bank interest, usually TDS-deducted |
| LAABHANSH, DIVIDEND | Investment income | Check final withholding; do not double-count in ordinary taxable income |
| TAX REFUND, IRD REFUND | EXCLUDE | Reconcile the original tax/expense treatment and any recovery adjustment; not automatically sales turnover |

#### 3.2 Expense Patterns (Debits) -- Potential deduction Business Expenses

**Potential deduction business expenses table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| KARYALAYA BHADA, OFFICE RENT | Office rent | Potential deduction | Dedicated business premises (rent TDS may apply) |
| LEKHAPAL, AUDITOR, ACCOUNTANT, CA FEE | Accountancy/audit fees | Potential deduction | Business-related |
| KANUNI, LAWYER, LEGAL, ADVOCATE | Legal fees | Potential deduction | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Potential deduction |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Advertising | Potential deduction |  |
| TRAINING, SEMINAR, CONFERENCE | Training | Potential deduction | Must relate to current business |
| BANK CHARGE, SERVICE CHARGE, SPEJJEZ | Bank charges | Potential deduction | Deduct the evidenced business portion, subject to sections 13 and 21, including for a mixed-use account |
| ESEWA FEE, KHALTI FEE, GATEWAY FEE | Payment-processing fees | Potential deduction |  |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN | IT infrastructure | Potential deduction | Capitalise if a long-lived asset |

#### 3.3 Expense Patterns (Debits) -- Software / SaaS

**Software / SaaS table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365 | Software subscription | Potential deduction | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, ZOOM, SLACK | Software subscription | Potential deduction |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN | Software subscription | Potential deduction |  |

#### 3.4 Expense Patterns (Debits) -- Utilities (apportion if mixed/home use)

**Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| NEA, NEPAL ELECTRICITY, BIDYUT | Electricity | T2 if home office | Evidence the attributable business part; no private portion |
| KHANEPANI, WATER BOARD | Water | T2 if home office | Apportion |
| NTC, NCELL, WORLDLINK, VIANET, SUBISU | Telecoms/broadband | T2 | Business-use portion only; hold until supported |

#### 3.5 Expense Patterns (Debits) -- Travel

**Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| BUDDHA AIR, YETI AIRLINES, NEPAL AIRLINES | Flights | Potential deduction if business travel | Wholly business purpose |
| HOTEL, BOOKING.COM, RESORT | Accommodation | Potential deduction if business travel |  |
| PATHAO, INDRIVE, TAXI | Local transport | Potential deduction if business purpose |  |
| PETROL, DIESEL, FUEL, NOC, PUMP | Vehicle fuel | T2 ; business % only | Keep evidence of business journeys and costs. A logbook can support apportionment. |
| PARKING | Parking | T2 ; business % only |  |

#### 3.6 Private costs and non-expense cues

**Private costs and non-expense table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, BHOJANALAYA, PARTY, ENTERTAINMENT | Entertainment/personal meals | Not deductible when the stated private/non-expense condition holds | Private cost blocked; a business-entertainment claim needs evidence of its legal treatment |
| BHANSAGHAR, GROCERIES, SUPERMARKET, BHATBHATENI | Personal living | Not deductible when the stated private/non-expense condition holds | Actual private cost blocked; a store name alone proves nothing |
| FINE, JARIWANA, PENALTY | Fines/penalties | Not deductible when the stated private/non-expense condition holds | Public policy |
| IRD PAYMENT, INCOME TAX, KAR BHUKTANI | Income tax paid | Not deductible when the stated private/non-expense condition holds | Tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | Not deductible when the stated private/non-expense condition holds | Not an expense |

#### 3.7 Expense Patterns (Debits) -- Capital Items (depreciate, do not expense)

**Capital items table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | Capitalise & depreciate | Apply the Schedule 2 pool, timing and business-use conditions below |
| PRINTER, SCANNER, COPIER | Office equipment | Capitalise & depreciate | As above |
| FURNITURE, DESK, CHAIR | Furniture/fittings | Capitalise & depreciate | As above |
| VEHICLE, CAR, BIKE (business) | Motor vehicle | Capitalise & depreciate (business %) | As above |

#### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, KARJA, EMI (principal) | EXCLUDE (principal) | Business-loan interest requires its own deduction analysis |
| SSF, SOCIAL SECURITY, EPF, CIT | Retirement deduction | Verify the approved retirement-qualifying component and annual cap; do not classify employee contributions as ordinary business expenses |
| VAT PAYMENT, IRD VAT | EXCLUDE | VAT liability, not an income-tax expense |
| ADVANCE TAX, INSTALLMENT TAX | Tax credit | Credit against final liability, not an expense |

#### 3.9 Nepali Banks -- Statement Format Reference

**Bank statement format table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Nepal Rastra Bank-regulated commercial banks (NABIL, NIC ASIA, Global IME, Nepal Investment Mega) | TRANSFER, DEPOSIT, CHARGE, FONEPAY, CONNECTIPS | PDF/CSV; date often in BS and/or AD |
| eSewa / Khalti / IME Pay (wallet statements) | LOAD, PAYMENT, CASHBACK, SETTLEMENT | CSV; wallet top-ups are not income |
| connectIPS | INTERBANK TRANSFER | Clearing rail; check underlying purpose |


#### Key Nepali Banking / Tax Terms

**Key terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| भुक्तानी / BHUKTANI | Payment | Check direction for income/expense |
| तलब / TALAB / PARISHRAMIK | Salary / remuneration | Employment income |
| बहाल / GHAR BHADA / KIRAYA | Rent | Rental income or office-rent expense |
| ब्याज / BYAJ | Interest | Investment income (often TDS-deducted) |
| लाभांश / LAABHANSH | Dividend | Investment income |
| कर / KAR | Tax | Identify tax type; income tax blocked, other taxes follow the statutory exceptions |
| जरिवाना / JARIWANA | Fine / penalty | Not deductible |
| कर्जा / KARJA / EMI | Loan | Principal excluded; business interest may deduct |
| सेवा शुल्क / SEWA SHULKA | Service charge / fee | Business income or bank charge ; check context |


## Deadlines and filing

| Filing/payment obligation | Ordinary timing and condition | Official source |
|---|---|---|
| Annual income return where required | Within 3 months after income-year end, ordinarily Ashoj-end | [§96(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=124) |
| Return extension | Apply in writing before the due date; IRD may allow up to 3 months in total; not an automatic payment-interest holiday | [§98](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=127); [§119(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=147) |
| Ordinary business/investment instalments | Poush-end 40%, Chaitra-end 70%, Ashad-end 100% cumulative estimated tax, less qualifying previous instalments and credits; statutory aggregate-instalment exception applies below NPR 7,500 | [§94(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=117); [§94(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=118) (in words on the page) |
| Turnover-regime instalments | Poush-end based on turnover to Poush 20; Ashad-end based on actual turnover through Ashad 20 plus the estimated remainder, less prior payment | [§94(1क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=118) |
| Withholding statement/deposit | Monthly statement ordinarily within 25 days after the Nepali month ends; ordinary deposit has the same deadline, but §90(4क) allows a qualifying §4(4क) turnover-tax payer to deposit Chapter 17 withheld advance tax when instalment tax is paid; statement and deposit duties are distinct. Use payroll/TDS for categories/certificates | [§90(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=113) |

PAN is required before earning income/withholding where Rule 23 applies. VAT thresholds/rates and SSF registration/wages belong to the linked VAT/payroll skills; never transfer their turnover or pay bases into income-tax eligibility. [Rule 23](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AF%20(%E0%A4%B8%E0%A5%8B%E0%A4%B9%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7kddd2d.pdf#page=9).

**Forms are regime-specific.** D-01 is presumptive, D-02 turnover and D-03 the normal income-return process. The old general label "D-01 for natural persons" was wrong. The [IRD FAQ](https://ird.gov.np/faq/?gid=97) names those forms and describes the portal workflow; its historical rates are not used for the current computation. Exact current authenticated screens/boxes remain a filing check.

The salary-only return exemption is conditional: section 4(3) requires Nepal-source employment-only income, resident employers, no simultaneous employers, and claims limited to medical-treatment credit for expenses paid by the employer and retirement-contribution deductions paid by the employer itself, with no §12 donation deduction. Section 97(1) retains the cross-reference after Finance Act 2083; section 97(2)'s **income above NPR 4,000,000** requirement remains, and is not worded simply "taxable income". IRD can require returns by notice. Do not assume all fully withheld salaries are exempt from filing. [§4(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=17); [§97(2)-(5)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=127); [§57(22)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=197).

In the [IRD Taxpayer Portal](https://ird.gov.np/), select the correct year and regime/form; enter/reconcile business, employment and investment schedules, deductions and credits; use the computation to populate the actual form rather than inventing box numbers; retain the submission number, verification/acknowledgement and payment voucher. Reconcile any refund or outstanding balance to the account. Do not call a saved draft filed or submit automatically.

### Working paper and onboarding

Retain the original A-E working-paper architecture with the correct form title and year. A1 business receipts net of properly identified VAT, A2 **gross assessable** employment, A3 rental review and A4 investment review feed A5; separately identify exempt/final-tax receipts. B1-B12 retain office rent; professional fees; supplies; software; advertising; bank/gateway charges; travel; utilities; home office; vehicle use; depreciation; and other allowable costs, with B13 their total. Do not subtract expenses twice if A1 already contains net profit. C1 approved retirement, C2 life, C3 health, C4 eligible donations, C5 supported additional allowances only (no unconfirmed age deduction), C6 total; add building insurance/medical-credit schedules where relevant. D = the correctly aggregated assessable income less eligible deductions. E1 first-band charge, E2 other marginal tax, E3 gross tax, E4 eligible female/medical credits, E5 evidenced non-final TDS/advance credits, E6 payable/refund. Keep separate entries for credits, not income deductions.

Reviewer flags retain: year/status; every residence test; actual SSF contribution/exception; female-credit eligibility; the unresolved legacy age-relief claim; mixed home/vehicle/phone use; pool/timing; regime election/eligibility; retirement limits; PAN/VAT; income omitted from bank records; and certificates. Missing onboarding answers permit a labelled classification draft and pending list, never invented residence, tax rates or filing-ready deductions. With no statement or equivalent complete records, stop transaction preparation. With statements but no invoices, hold unsupported claims and clearly state that the draft cannot substantiate a return.

## Penalties and interest

These replace contradictory legacy penalty summaries. All amounts/rates below derive from the cited provisions (in words on the page where applicable); calculate the actual delay and statutory base rather than stacking unrelated charges.

| Failure and condition | Statutory consequence | Official source |
|---|---|---|
| Estimated-income statement under §95(1) not filed | Greater of NPR 5,000 per statement or 0.01% of the assessable income in it | [§117(1)(क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=145) (in words on the page) |
| Annual return late, fixed-regime §4(4) taxpayer | NPR 1,200 per return; NPR 100 per month where the period is under 1 year; no repeated annual fixed charge is inferred | [§117(1)(ग)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=145) (in words on the page) |
| Other annual return late | Greater of statutory 0.1% per year of assessable income computed before deductions/with required inclusions, or the NPR 1,200 per-return floor (NPR 100 per month for a period under 1 year); §97(2) cases have their specified final-tax-income adjustment | [§117(1)(ग)-(घ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=145) |
| Required records not retained | Greater of 0.1% of the specified assessable-income base or NPR 1,000 | [§117(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=146) (in words on the page) |
| Withholding statement under §90(1) late | 2.5% per annum of tax required to be withheld, for each month or part of delay; not an invented daily fixed penalty | [§117(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=146) (in words on the page) |
| Underpaid ordinary instalment | Normal-rate interest on the statutory shortfall; §118 includes the 90% benchmark where the estimate is incorrect and its specified end date | [§118](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=146); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=147) (in words on the page) |
| Late tax payment | Normal interest, 15% per annum, calculated for each month/part of unpaid delay; return extension does not excuse it | [definition §2(कब)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=15); [§119(1)-(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=147) (in words on the page) |
| False/misleading statement | 50% of tax shortfall for inadvertent error without intent/negligence; 100% where intentional or negligent | [§120](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=148) (in words on the page) |

Arrears, enforcement, disputed assessments and possible Finance Act 2083 temporary relief require practitioner review; never advise ignoring an outstanding assessment or assume an amnesty applies. See `nepal-vat` for the distinct relief boundaries touching income tax as well.

## Cross-border points

Ordinary non-resident natural-person taxable income uses **25%**, not resident bands or resident-only deductions/credits; establish Nepal source and any treaty before a final answer. [Schedule 1 §1(8)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=160). Residents' foreign receipts may need country-by-country foreign-tax credits, capped by Nepal's average rate, with the statutory carry-forward/election rules; do not assume full credit for foreign tax. [§71](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=91); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=92).

The UPWORK/FIVERR/PAYONEER/WISE pattern does not settle income source or the special regime. Qualifying non-business resident individuals' foreign-currency receipts for software/electronic services, consultancy or audiovisual social-media content have specific 5% collection rules under §95A(6ख)-(6घ); Finance Act 2083 §57(20) adds final treatment. Refer if business status, activity or receipts do not satisfy those conditions. [§95A(6ख)-(6घ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=122); [§57(20)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=195); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=196).

Capital gains are a referral boundary, not an ordinary bank-credit slab calculation. For the retained topics: listed interests of a resident natural person held **more than 365 days** have current 7.5% collection, those held **365 days or less** 10%; earlier rates were 5% and 7.5%. Non-business taxable land/private-building gains held **at least 5 years** have current 7.5%, less than 5 years 10%; earlier rates 5% and 7.5%. Apply the current rules only from Shrawan 1, 2083, identify taxable asset/cost/exemptions, and review final-tax versus annual-return treatment before acting. For the current year, review the separate section 95A rule for land compulsorily acquired under a government decision and the exclusion for qualifying gifts of land or a private building to government. The prior "over 5 years/at most 5 years" split misplaced the exact anniversary. [§95A(2),(5)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=121); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=122); [§57(21)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=196); [§57(26)(घ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=199).

## Two worked examples that recompute

The original seven cases and eight regression topics are retained below. All transactional amounts are hypothetical inputs. BS dates/counterparty text are retained verbatim; their existence is not evidence of an invoice or filing. Historic cases use FY 2082/83 only.

### 1. Invoice settlement and VAT decision

`2082-05-10 ; FONEPAY CREDIT ; HIMAL TRADE CONCERN ; INV 2082-014 ; +118,000.00 ; NPR`

If evidence establishes an ordinary VAT-inclusive taxable invoice, net revenue is NPR 104,424.78 and VAT NPR 13,575.22, derived. If legitimately unregistered and the amount is consideration for that sale, revenue is NPR 118,000; confirm mandatory registration separately. Do not assume every registered person's receipt includes VAT or count the wallet settlement twice.

```oa-check
name: Historical invoice settlement conditional VAT extraction
inputs:
  gross: 118000
steps:
  - net: gross / 1.13
  - vat: gross - net
  - unregistered_receipt: gross
expected:
  net: 104424.78
  vat: 13575.22
  unregistered_receipt: 118000
```

### 2. SaaS subscription

`2082-04-25 ; CARD PAYMENT ; ADOBE ; CREATIVE CLOUD ; -4,200.00 ; NPR`

If the recurring subscription was actually used in the business and all deduction/invoice conditions are met, the supported operating cost is NPR 4,200, adjusted for any separately recoverable VAT. A merchant name does not prove business use; durable acquired assets use the capital rules.

### 3. Supermarket/private spending

`2082-06-02 ; CARD ; BHATBHATENI SUPERSTORE ; ; -9,800.00 ; NPR`

If evidence identifies private living costs, deductible business expense is NPR 0. The original automatic "supermarket = personal" inference was too broad: hold for the receipt if purpose is unknown, and analyse a documented business purchase under the actual item and capital/operating rules.

### 4. Retirement contribution

`2082-04-31 ; DD ; SOCIAL SECURITY FUND ; SSF CONTRIBUTION ; -6,600.00 ; NPR`

Reconcile this retained bank date/amount to the actual statement. Only the verified approved retirement-qualifying component enters the aggregate capped deduction; the full NPR 6,600 cannot be inferred eligible solely from the narration. It is not a second business expense or an ordinary income-tax payment.

### 5. Net salary credit

`2082-05-01 ; CREDIT ; KATHMANDU TECH PVT LTD ; TALAB SHRAWAN ; +60,000.00 ; NPR`

Classify as an employment cash receipt, not self-employment revenue. Reconstruct gross assessable salary and employer contributions/benefits from the payslip and TDS certificate. The NPR 60,000 bank credit alone is not assessable employment income or proof of tax withheld.

### 6. Kathmandu fixed-regime shop

Retain annual retail turnover NPR 2,400,000. Add the missing conditions: resident natural person, Nepal-source business income only, taxable business income no more than NPR 300,000, no barred credit claim, and a valid yearly election. If all hold, the metro fixed tax is NPR 7,500. Turnover alone never established eligibility. The old automatic zero-transaction exemption is not confirmed and is not used.

### 7. Freelancer, corrected historical employment-levy error

Registered sole proprietor, Nepal-resident, FY 2082/83, single, no SSF, business receipts NPR 1,500,000, supported allowable business costs NPR 300,000 and eligible life premium NPR 40,000: taxable income NPR 1,160,000. This example assumes the normal regime is applicable/selected; do not skip the small-business election test. The first-band employment charge does not apply to the registered sole proprietor. Tax is NPR 20,000 + NPR 60,000 + NPR 48,000 = **NPR 128,000**, not the seed's NPR 133,000. No remuneration-only female credit applies to business income.

```oa-check
name: Historical sole-proprietor first-band exception
inputs:
  receipts: 1500000
  costs: 300000
  life: 40000
steps:
  - taxable: receipts - costs - life
  - tax: min(max(taxable - 500000, 0), 200000) * 0.10 + min(max(taxable - 700000, 0), 300000) * 0.20 + max(taxable - 1000000, 0) * 0.30
expected:
  taxable: 1160000
  tax: 128000
```

### 8. Current scale and contribution-status decision

For FY 2083/84 taxable employment income NPR 1,160,000, ordinary first-band tax is NPR 10,000 and the excess tax NPR 16,000: total NPR 26,000. If the statutory SSF-contributor exception applies, tax is NPR 16,000. These are annual taxable-income inputs already determined after appropriate deductions, not gross pay. Do not use the historical NPR 133,000 result in this year.

```oa-check
name: Current year first-band exception comparison
inputs:
  taxable: 1160000
steps:
  - ordinary: min(taxable, 1000000) * 0.01 + max(taxable - 1000000, 0) * 0.10
  - ssf_exception: max(taxable - 1000000, 0) * 0.10
expected:
  ordinary: 26000
  ssf_exception: 16000
```

### Retained historical regression topics

1. Earlier single non-SSF **employment** taxable NPR 1,160,000 gives NPR 133,000. That amount is not the corrected sole-proprietor case.
2. Earlier single ordinary employment taxable NPR 1,000,000 gives NPR 85,000.
3. Earlier electing-couple ordinary employment taxable NPR 2,000,000 gives NPR 356,000.
4. Earlier eligible remuneration-only resident woman with pre-credit tax NPR 133,000 has credit NPR 13,300 and tax NPR 119,700.
5. Earlier single SSF-contributor taxable NPR 700,000 gives NPR 20,000, versus NPR 25,000 without the exception.
6. The metro shop case above retains the NPR 2,400,000 input and NPR 7,500 outcome only after all fixed-regime conditions hold.
7. Retain the service-business turnover NPR 6,000,000, taxable business income no more than NPR 1,000,000. If the turnover regime is elected and the service is eligible, tax depends on area: metro NPR 7,500 + 2% × NPR 3,000,000 = **NPR 67,500**; municipality NPR 64,000; other area NPR 62,500. The old NPR 120,000 taxed the full turnover and omitted the statutory first slice.
8. Lawyer with turnover NPR 2,000,000: refuse an automatic small-regime calculation from profession and turnover alone. Specialist consultancy is excluded from the turnover regime; the fixed regime needs all its own conditions. The old blanket profession ban on both regimes is not supported by the cited current section.

```oa-check
name: Historical single employment regression cases
inputs:
  first: 500000
  second: 200000
  third: 300000
  excess: 160000
steps:
  - one_million: first * 0.01 + second * 0.10 + third * 0.20
  - mid_tax: one_million + excess * 0.30
  - female_credit: mid_tax * 0.10
  - female_after: mid_tax - female_credit
  - ssf_seven_hundred: second * 0.10
  - ordinary_seven_hundred: first * 0.01 + second * 0.10
expected:
  one_million: 85000
  mid_tax: 133000
  female_credit: 13300
  female_after: 119700
  ssf_seven_hundred: 20000
  ordinary_seven_hundred: 25000
```

```oa-check
name: Historical couple and turnover regression cases
inputs:
  turnover: 6000000
steps:
  - couple_two_million: 600000 * 0.01 + 200000 * 0.10 + 300000 * 0.20 + 900000 * 0.30
  - metro_service: 7500 + (turnover - 3000000) * 0.02
  - municipal_service: 4000 + (turnover - 3000000) * 0.02
  - other_service: 2500 + (turnover - 3000000) * 0.02
expected:
  couple_two_million: 356000
  metro_service: 67500
  municipal_service: 64000
  other_service: 62500
```

## Ask the client first

- Full fiscal-year bank/wallet statements in CSV/PDF/text and other income records; identify year, PAN, entity, residence under every test, and any treaty.
- Assessment election/spouse income and dependants where relevant, actual SSF/pension contributions, and profession, turnover, taxable profit and regime election.
- Sales/purchase invoices, gross salary/benefits, retirement statements, asset register, mixed-use evidence and prior return/assessment.
- Evidence for eligible insurance/donations, remote-area/pension/disability relief and remuneration-only female-credit conditions; an age alone does not authorise unconfirmed relief.
- TDS certificates, final/advance withholding classification, instalment receipts, VAT registration and opening balances.
- Capital disposals, arrears, enforcement and any eligibility for temporary relief.

Retain R-NP-1 through R-NP-7: unresolved assessment/year; companies/partnerships; non-resident computation; land/share/property gains; arrears/enforcement; VAT-return requests; and unproved small-business eligibility. Route them to the appropriate skill/practitioner, retaining a supported draft only. For the current period a common scale does not justify losing the couple-election facts; for a historical period missing election prevents selection of the higher couple bands. Do not substitute a guessed resident status, location, SSF status or unsupported business-use percentage. Always label the output estimated and subject to qualified review.

## Sources

| Source and actual material read | Official URL | Read on |
|---|---|---|
| District Treasury Controller Office copy of the consolidation through Finance Act 2082, including the general deduction and private expense provisions at sections 13 and 21 | [Official PDF](https://giwmscdnone.gov.np/media/files/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod_xmjdamk.pdf) | 2026-11-24 |
| Finance Act 2083 Gazette supplement 29, publication record, and Parliament authentication register with the adopted attachment | [Gazette record](https://dop.gov.np/content/13558/2083-76-ari-29-2083-3-30/) · [Parliament attachment](https://hr.parliament.gov.np/uploads/attachments/mohhlmnmjpyhdrzl.pdf#page=225) | 2026-11-24 |
| Read for Income Tax Act residence, income heads, deductions, approved retirement, medical/foreign credits, withholding, instalments/returns, penalties, historical Schedule 1 and Schedule 2; operative body only, not historical footnotes; PDF pages 11,15-22,33-34,42-43,47-48,70-71,82,91-92,107-118,121-127,144-148,157-168 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf) | 2026-11-15 |
| Read for enacted Finance Act 2083 commencement and §57 donation/cash-payment, final withholding, filing and personal/capital-gain amendments; PDF pages 1,189-200 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf) | 2026-11-15 |
| Read for Rules 17,21,23,31-33,38-39; approved medical expenses, retirement cap, PAN, salary apportionment and allowances; PDF pages 7-9,12,14 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AF%20(%E0%A4%B8%E0%A5%8B%E0%A4%B9%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7kddd2d.pdf) | 2026-11-15 |
| Read for IRD FAQ excerpts naming D-01 presumptive, D-02 turnover, D-03 normal return; historical FAQ rates not relied upon; PDF pages not applicable: HTML excerpts | [Official text](https://ird.gov.np/faq/?gid=97) | 2026-11-15 |

Not yet confirmed: legacy age-65/NPR 100,000 extra exemption; mandatory exclusive-room home-office test; automatic zero-activity presumptive-tax exemption; exact current authenticated form box/screen names and taxpayer notices; taxpayer-specific treaty/source/FX questions; the precise retirement-qualifying part of a particular SSF statement. The first three legacy claims are excluded from usable computation, not assumed true. Current SSF rates, deadlines and wage rules are sourced in nepal-payroll; VAT rates/thresholds are sourced in nepal-vat.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nepal-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nepal-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
