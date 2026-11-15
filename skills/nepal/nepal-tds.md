---
name: nepal-tds
description: ALWAYS read this skill before touching any Nepal TDS / withholding tax work. Use whenever asked to compute or deduct Nepal withholding tax (TDS) on rent, interest, dividends, service/contract payments, or payments to non-residents under the Income Tax Act 2058. Trigger on phrases like "Nepal TDS", "Nepal withholding", "TDS rates Nepal", "Section 88 Nepal", "rent TDS Nepal 10%", "dividend TDS Nepal 5%", "interest TDS Nepal 6%", "contract TDS Nepal 1.5%", or "FY 2082/83 TDS". Out of scope ; personal income tax computation (separate skill), corporate tax (separate skill), payroll/SSF salary TDS (use the payroll skill), and VAT.
jurisdiction: NP
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
version: 2.0
type: computation
tax_year_notes: "Calendar 2026 includes FY 2082/83 (2025/26) and FY 2083/84 (2026/27); apply the labelled period."
---

# Nepal TDS and withholding tax

## Scope

Compute common non-salary Nepal-source withholding for a resident payer. Calendar 2026 spans FY 2082/83 and FY 2083/84. The table below applies in both periods except the expressly dated insurance-agent change. This is a source-cited draft; this version has no accountant approval.

Load `nepal-payroll` for salary withholding and SSF, `nepal-income-tax` for the recipient's annual computation, `nepal-corporate-tax` for companies, and `nepal-vat` for VAT. A withholding percentage does not decide VAT or final annual liability.

## Ask the client first

- Payment date and Nepali income year; gross consideration, invoice VAT and any contractual gross-up.
- Payer and payee residence, natural person or entity, PAN and verified VAT status.
- Exact payment category, contract and any related payments under that contract.
- Whether interest is connected with a business, the lender's legal status and any statutory exemption.
- For rent, the owner's legal identity and whether this is house rent, vehicle hire or another rental.
- For a foreign recipient, treaty residence, beneficial entitlement, permanent establishment and any IRD notice. Missing facts stop a final computation; a higher assumed rate is not a legal default.

## The method, step by step

### 1. Identify the statutory category

Employment goes to section 87; investment returns and services go to section 88; windfalls to section 88A; qualifying supply, labour and construction/installation contracts to section 89. Section 89 excludes payments already covered by sections 87, 88 or 88A and exempt payments. Do not move a consultancy invoice into the contract category just because a contract exists. [Act §§87-89, including the contract definition and exclusions](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=107).

### 2. Apply the conditional rate

Figures written as words in the Act are shown as numerals below (in words on the page). Use the payment base required by the section; establish consideration separately from separately invoiced VAT, and refer unresolved gross-up or bundled invoices.

| Payment and complete condition | Rate and period | Official provision |
|---|---|---|
| Nepal-source interest, royalty, service fee, commission, sales bonus or other return paid by a resident person; only where no specific exception or exemption applies | 15%; both periods | [§88(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=107) (in words on the page) |
| Nepal-source rent paid by a resident person, subject to the house-rent and vehicle exceptions below | 10%; both periods | [§88(1), proviso (5)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=108) (in words on the page) |
| House rent received by a natural person | No federal withholding under this provision; establish any separate local rental tax instead | [§88(1), proviso (5)(ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=108) |
| Vehicle rent paid to a VAT-registered person carrying on a vehicle-rental business | 1.5%; both periods | [§88(1), proviso (5)(क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=108) (in words on the page) |
| Dividend paid by a resident company or partnership | 5%, including a non-resident recipient; final withholding under §92 | [§88(2)(क)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=110); [§92(1)(क),(च)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=115) (in words on the page) |
| Nepal-source deposit/debenture/government-bond interest paid by a listed company, resident bank, financial institution, cooperative or other statutory bond issuer to a natural person, unrelated to carrying on a business | 6%; both periods; final treatment subject to §92 | [§88(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=110); [§92(1)(ङ)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=115) (in words on the page) |
| Interest to an entity where no special exemption or rate applies | 15%; do not apply to exempt interest or interest paid to a resident bank/financial institution | [§88(1),(4)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=107); [§88(4)(ख)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=110) (in words on the page) |
| Service fee paid to a resident VAT-registered service provider, or to a resident entity carrying out VAT-exempt transactions | 1.5%; both periods | [§88(1), proviso (4)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=108) (in words on the page) |
| Resident service fee outside that exception | 15% unless another specific rule applies | [§88(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=107) (in words on the page) |
| Freight service or freight-vehicle rental | 2.5%; reduced to 1.5% when the recipient is VAT registered and carries on that freight/rental business | [§88(1), proviso (8)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=109) (in words on the page) |
| Service fee or commission to a resident natural-person insurance agent | 20%, final withholding, from Shrawan 1, 2083; do not use the ordinary service/commission rate | [Finance Act §57(17),(20)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=195); [§1(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=1) (in words on the page) |
| Resident contract/supply payment within §89, exceeding NPR 50,000 after the aggregation test | 1.5%; both periods | [§89(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=111) (in words on the page) |
| Qualifying contract/agreement payment to a non-resident under §89(3)(क) | 5%; distinguish non-resident insurance/reinsurance at 1.5%, an IRD-notified rate, and section 88 service/royalty payments | [§89(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=111); [§89(3)(ख)-(ग)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=112) (in words on the page) |
| Ordinary windfall gains | 25%, final withholding; statutory qualifying national/international awards and Gazette exemptions are exceptions | [§88A](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=111); [§92](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=116) (in words on the page) |

For the contract threshold, aggregate payments in the **preceding 10 days**, under the same contract, by the payer or an associated person to the payee or an associated person. This is not a per-invoice threshold. The rate applies to the gross qualifying payment, not just the excess over the threshold. [§89(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=111).

For section 88, payments by a natural person outside a business, exempt payments and payments covered by employment withholding are excluded as provided by subsection (4). The original blanket description of 15% as "refuted" was too broad: 15% is the statutory residual rate, while specific categories override it. Dividend withholding is 5%, not the legacy disputed 10%. [§88(1)-(4)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=107); [§88(2),(4)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=110).

A qualifying award in the statutory fields, including agriculture from Shrawan 1, 2083, is exempt up to NPR 500,000; only the excess is taxed, unless a Gazette exemption applies. Do not turn every lottery or commercial prize into an exempt award. [§88A(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=111); [Finance Act §57(18)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=195).

### 3. Compute and document

Withholding = qualifying payment base × applicable rate. Net cash = gross payment less withholding, with invoice VAT and any other charges reconciled separately. Record why the category and exception apply, recipient PAN, gross amount, payment date, rate, tax, net payment and deposit reference. A bank label alone cannot establish residence, business connection or an exemption.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| R-NP-TDS-1: Salary TDS | Use `nepal-payroll`; do not substitute a flat service rate. |
| R-NP-TDS-2: Foreign service, royalty, technical fee or treaty claim | The domestic residual rate is in §88, but a final answer requires source, recipient and treaty analysis. Refer when those facts or the applicable treaty are absent. A 5% non-resident contract rate is not universal. |
| R-NP-TDS-3: Payment not in this common-category table | Open the full current §88/§89 schedule and any amending notice. This is not an exhaustive payment catalogue. |
| Interest recipient or VAT status unknown | Hold the final classification; do not assume an entity or infer registration from a bank narration. |
| Non-business individual payer | Apply the statutory payer exclusions before choosing a rate. |
| Federal house-rent exclusion | Do not equate no federal TDS with exemption from local house-rent tax; local rate/return requires separate sourcing. |

## Worked cases

These amounts are hypothetical inputs, not statutory thresholds. No gross-up is assumed and any invoice VAT is separately resolved.

### 1. Rent: entity versus natural-person house owner

The retained NPR 200,000 rent example needs the landlord's identity. If the recipient is a resident company and ordinary 10% rent withholding applies, TDS is NPR 20,000 and net rent NPR 180,000. If it is house rent received by a natural person, this federal provision requires no withholding: NPR 0, with local rental-tax treatment checked separately. This is why "resident landlord" alone was insufficient.

```oa-check
name: Rent owner changes federal withholding
inputs:
  rent: 200000
steps:
  - entity_tds: rent * 0.10
  - entity_net: rent - entity_tds
  - natural_person_federal_tds: rent * 0
expected:
  entity_tds: 20000
  entity_net: 180000
  natural_person_federal_tds: 0
```

### 2. Non-business individual bank interest

NPR 100,000 of qualifying Nepal-source bank interest to a natural person, unrelated to business, gives 6% × NPR 100,000 = NPR 6,000 withholding; cash NPR 94,000. An entity cannot use this natural-person exception.

```oa-check
name: Qualifying natural-person deposit interest
inputs:
  interest: 100000
steps:
  - tds: interest * 0.06
  - net: interest - tds
expected:
  tds: 6000
  net: 94000
```

### 3. Dividend

NPR 500,000 of qualifying resident-company dividend gives 5% × NPR 500,000 = NPR 25,000 final withholding and NPR 475,000 cash.

```oa-check
name: Resident-company dividend
inputs:
  dividend: 500000
steps:
  - tds: dividend * 0.05
  - net: dividend - tds
expected:
  tds: 25000
  net: 475000
```

### 4. Resident supply contract

NPR 300,000 of qualifying section 89 supply consideration gives 1.5% × NPR 300,000 = NPR 4,500 withholding and NPR 295,500 cash. It is not 1.5% of the amount above the threshold. Separate VAT and excluded payment categories must already have been resolved.

```oa-check
name: Resident qualifying supply contract
inputs:
  payment: 300000
steps:
  - tds: payment * 0.015
  - net: payment - tds
expected:
  tds: 4500
  net: 295500
```

## When to refuse or refer

Do not issue a final withholding instruction with unresolved recipient identity, treaty, source, VAT status, payment base or statutory category. Do not assert every entity interest payment is taxable, every rent payment bears federal TDS, or every non-resident contract is a service fee. Never file automatically; produce a working paper for practitioner review.

## Filing and payment

At payment, deduct the applicable tax. Under section 90(1)-(2), submit the monthly withholding statement in IRD's prescribed format and deposit the tax **within 25 days after the Nepali month ends**. An omitted deduction does not eliminate the payer's statutory liability. [§90](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=113).

Use the [IRD Taxpayer Portal](https://ird.gov.np/) and its eTDS facility: identify the payer PAN and period, enter the payee PAN, payment category and date, gross payment and tax, reconcile the statement total to payroll/payables, obtain the submission/reference number, complete the verification required by the account, and match the payment voucher to the statement. Do not call a saved draft a filed return. Exact current screen labels and category codes must be confirmed in the authenticated portal before submission.

Issue the section 91 withholding certificate with payment and tax details. Generally it is due within 25 days after the withholding month ends; employment certificates follow the separate year-end/termination rule in `nepal-payroll`. [§91(1)-(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=114).

Final withholding under section 92 is distinguished from an advance credit under section 93. Do not add final-tax income and its withholding again into the ordinary annual tax computation. [§92](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=115); [§93](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=116).

## Completion checklist

Confirm the period and recipient; record the exact statutory category and exception; test associated contract payments; recompute gross, withholding and net; reconcile submission and payment references; issue the certificate; flag every unresolved treaty or portal item for review.

## Sources

| Source and actual material read | Official URL | Read on |
|---|---|---|
| Read for Income Tax Act §§87-93; common payments, exclusions, aggregation, certificates and final versus advance tax; PDF pages 107-116 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf) | 2026-11-15 |
| Read for enacted Finance Act 2083 §1(2), §57(17)-(20); insurance-agent and award changes; PDF pages 1,195-196 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf) | 2026-11-15 (in words on the page) |

Not yet confirmed: local house-rent tax rates and procedures; taxpayer-specific treaty entitlement, beneficial ownership and permanent-establishment analysis; current authenticated eTDS screen labels/category codes and any taxpayer-specific notice. No unresolved item is a usable default rate.

Legacy provenance: the prior draft named PKF T.R. Upadhya & Co. and Union Nepal as secondary research material. The operative statements in this version are re-anchored to the official Act and enacted amendments above; the old instruction that nothing had been checked against primary sources no longer describes this version.

## Disclaimer

For informational and computational purposes only; not tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Nepali professional (CA / registered tax practitioner) before filing or acting upon. Latest verified version at [openaccountants.com](https://openaccountants.com).
