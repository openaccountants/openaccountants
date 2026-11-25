---
name: vu-corporate-income-tax
description: "Vanuatu company taxation, tax year 2026: no ordinary corporate income tax; rent tax on companies at 12.5% of all chargeable rent; the International Companies Act s 118 exemptions (income, estate, stamp duty, exchange control) and the conflict between its 20-year and 31 December 2099 durations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vu-corporate-income-tax"
  jurisdiction: "VU"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# Vanuatu corporate income tax

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file or take a position without professional review.

## Who this applies to

Local companies (Companies Act No. 25 of 2012), overseas companies doing business in Vanuatu, and international companies under the International Companies Act [Cap 222]. Vanuatu has no ordinary domestic corporate income tax: no company income tax rate, profits base or annual income tax return. A company still meets VAT ([VAT](vu-vat-gst.md)), the business licence and annual return fee ([company formation](vu-company-formation.md)), and rent tax on Vanuatu land it lets.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Ordinary corporate income tax | None | 2026 | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf |
| Rent tax, taxpayer not a natural person | 12.5% of all chargeable rent for the six-month period; the VT 200,000 natural-person threshold does not apply (Sch 1) | 2026 | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf |
| International company: income, profits, capital gains, distributions | Exempt for the company or its shareholder where the amounts accrue to or are derived by or from the company (s 118(1)) | 2026 | https://www.vfsc.vu/wp-content/uploads/2026/04/International-Companies-Act-CAP.-222-Consolidated-Edition-2026.pdf |
| International company: exemption duration, s 118(4) | Twenty years from the date of registration | 2026 | https://www.vfsc.vu/wp-content/uploads/2026/04/International-Companies-Act-CAP.-222-Consolidated-Edition-2026.pdf |
| International company: exemption duration, s 118(5) | Until 31 December 2099 | 2026 | https://www.vfsc.vu/wp-content/uploads/2026/04/International-Companies-Act-CAP.-222-Consolidated-Edition-2026.pdf |

## The base

There is no profits base. Rent tax falls on chargeable rent from leases of land in Vanuatu, excluding rent to the extent that a VAT-registered company derives rent subject to VAT; check the Rent Taxation Act's rules on exemptions, subleases, deemed rent and bad debts (ss 3 to 11A).

International Companies Act s 118, read from the 2026 consolidation:

- **Income.** Section 118(1) exempts the company from business licence fees unless it carries on business in Vanuatu. The income, profits, capital gains and distributions exemption applies to the company or its shareholder where the amounts accrue to or are derived by or from that company.
- **Estate and gift.** s 118(2): no estate, inheritance, succession or gift tax, duty or other charge on shares, debt obligations or other securities of an international company.
- **Stamp duty.** The second s 118(2): exempt are transfers of property other than real property situate in Vanuatu to or by the company; transactions in its shares, debt obligations or securities; and all other transactions relating to its business. Real property in Vanuatu is outside the exemption.
- **Exchange control.** Section 118(3) exempts the international company and securities transactions between its security holders. Under s 118(3A), the exemption is unavailable when the international company transfers securities in a Companies Act company, and that transfer must comply with the Companies Act. Section 118(6) also disapplies s 118(3) when beneficial or equitable ownership of an international company that is a shareholder in a Companies Act company is transferred. Check which ownership and reporting rules apply to that transfer.
- **Duration conflict.** The 2026 consolidation gives twenty years from registration in s 118(4) and an end date of 31 December 2099 in s 118(5). The 2006 consolidation put the twenty-year term in s 118(5). Schedule item 32 of Act No. 4 of 2016 expressly repealed and replaced that subsection with the 2099 end date. Seek confirmation of the applicable term before relying on an exemption for a company registered more than twenty years ago. The 2026 consolidation also numbers two subsections (2).

## Deadlines and filing

There is no corporate income tax return. Return all rent within 28 days after each period ending 31 May and 30 November and pay by the return date (ss 11 and 14). Check the [DCIR calendar](https://vanuatucustoms.gov.vu/index.php/important-dates) for the actual due date. See [personal income tax](vu-income-tax.md) for the period rules and [company formation](vu-company-formation.md) for annual return and business licence dates.

## Penalties and interest

Rent tax penalties and interest apply for late filing and payment (DCIR rent tax guide, https://vanuatucustoms.gov.vu/images/Brochures/IRD/eng/Rent_Tax_Guide.pdf). Amounts sit in the Tax Administration Act, not read here.

## Cross-border points

No ordinary profits tax means no domestic relief for foreign tax and no controlled foreign company rules. Whether Vanuatu withholds tax on payments to non-residents was not established from an official source (see Not yet confirmed). International companies are reportable entities for Common Reporting Standard purposes when they are financial institutions; see [tax overview](vu-tax-overview.md).

## Two worked examples that recompute

**1. Local company lets a warehouse, VT 300,000 chargeable rent in one six-month period, not VAT-registered, no special adjustment.** Tax is 300,000 times 12.5% = VT 37,500 (derived). No threshold applies to a company.

```oa-check
name: Vanuatu rent tax company 300000
inputs:
  rent: 300000
steps:
  - tax: rent * 0.125
expected:
  tax: 37500
```

**2. International company registered in 2002.** On a twenty-year reading, the exemptions end on the registration anniversary in 2022 (2002 plus twenty years, derived). The 2099 reading gives 31 December 2099. The expiry years differ by 77 (derived). The registration date is needed to calculate the exact interval between the two dates.

```oa-check
name: Vanuatu ICA exemption duration gap
inputs:
  registered: 2002
  term: 20
  outer: 2099
steps:
  - end_s118_4: registered + term
  - gap_years: outer - end_s118_4
expected:
  end_s118_4: 2022
  gap_years: 77
```

## Ask the client first

- Local company, overseas company or international company? Date of registration?
- Does it carry on business in Vanuatu?
- Does it let Vanuatu land, and is it VAT-registered?
- Any transfer of Vanuatu real property or of shares in a Companies Act company?

## Sources

| Source | URL | Read on |
|---|---|---|
| International Companies Act [Cap 222], Consolidated Edition 2026, s 118 (Read for the exemptions and both durations) | https://www.vfsc.vu/wp-content/uploads/2026/04/International-Companies-Act-CAP.-222-Consolidated-Edition-2026.pdf | 2026-11-14 |
| International Companies Act [Cap 222], Consolidated Edition 2006, s 118(5) (original twenty-year term) | https://www.vfsc.vu/wp-content/uploads/2025/06/222-International-Companies-Act-1.pdf | 2026-11-22 |
| International Companies (Amendment) Act No. 4 of 2016, Schedule items 31–33 (replacement of s 118(5) and transfer rules) | https://www.vfsc.vu/wp-content/uploads/2025/06/International-Companies-Amendment-Act-No.-4-of-2016.pdf | 2026-11-22 |
| DCIR Important Dates (operational rent tax dates) | https://vanuatucustoms.gov.vu/index.php/important-dates | 2026-11-22 |
| Rent Taxation Act [Cap 196], Consolidated Edition 2020, Sch 1 (Read for the company rate) | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf | 2026-11-14 |
| Vanuatu Competent Authority, AEOI guide v4 (Read for no income tax system) | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf | 2026-11-14 |
| DCIR rent tax guide (Read for the company case and penalties line) | https://vanuatucustoms.gov.vu/images/Brochures/IRD/eng/Rent_Tax_Guide.pdf | 2026-11-14 |

Not yet confirmed: which of s 118(4) and s 118(5) governs (the 2026 International Companies bill does not settle it; its Gazette Act and operative date were not found); whether any withholding tax applies to dividends, interest or royalties paid to non-residents (the old guide's 0% came from a private website); rent tax penalty amounts; international-company reporting duties to the VFSC.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vu-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vu-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
