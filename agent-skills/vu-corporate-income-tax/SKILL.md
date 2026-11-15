---
name: vu-corporate-income-tax
description: "Vanuatu company taxation, tax year 2026: no ordinary corporate income tax; rent tax on companies at 12.5% of all chargeable rent; the International Companies Act s 118 exemptions (income, estate, stamp duty, exchange control) and the conflict between its 20-year and 31 December 2099 durations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vu-corporate-income-tax"
  jurisdiction: "VU"
  tax_year: "2026"
  last_updated: "2026-11-14"
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
| International company: income, profits, capital gains, distributions | Company and shareholder not subject to any tax (s 118(1)) | 2026 | https://www.vfsc.vu/wp-content/uploads/2026/04/International-Companies-Act-CAP.-222-Consolidated-Edition-2026.pdf |
| International company: exemption duration, s 118(4) | Twenty years from the date of registration | 2026 | https://www.vfsc.vu/wp-content/uploads/2026/04/International-Companies-Act-CAP.-222-Consolidated-Edition-2026.pdf |
| International company: exemption duration, s 118(5) | Until 31 December 2099 | 2026 | https://www.vfsc.vu/wp-content/uploads/2026/04/International-Companies-Act-CAP.-222-Consolidated-Edition-2026.pdf |

## The base

There is no profits base. Rent tax falls on chargeable rent from leases of land in Vanuatu, excluding rent to the extent that a VAT-registered company derives rent subject to VAT; check the Rent Taxation Act's rules on exemptions, subleases, deemed rent and bad debts (ss 3 to 11A).

International Companies Act s 118, read from the 2026 consolidation:

- **Income.** s 118(1): a company is not, unless carrying on business in Vanuatu, subject to any business licence fee. A company or a shareholder is not subject to any tax on income, profits, capital gains or distributions. The licence-fee exemption carries the "not carrying on business in Vanuatu" condition; the income sentence does not, and it reaches shareholders.
- **Estate and gift.** s 118(2): no estate, inheritance, succession or gift tax, duty or other charge on shares, debt obligations or other securities of an international company.
- **Stamp duty.** The second s 118(2): exempt are transfers of property other than real property situate in Vanuatu to or by the company; transactions in its shares, debt obligations or securities; and all other transactions relating to its business. Real property in Vanuatu is outside the exemption.
- **Exchange control.** s 118(3): none applies. But s 118(3A) and (6): a transfer by an international company of securities in a Companies Act company, or of beneficial ownership of an international company that is a shareholder in a Companies Act company, must comply with the Companies Act.
- **Duration conflict.** s 118(4) says the exemptions run twenty years from registration; s 118(5) says they run until 31 December 2099. Both sit in the 2026 consolidation. (5) reads like a later amendment that should have replaced (4), but that is an inference. Do not advise reliance on the exemption for a company registered more than twenty years ago without resolving it. The consolidation also has two subsections numbered (2) and a stray closing quotation mark after (5).

## Deadlines and filing

No corporate income tax return. Rent tax: return all rent within 28 days after each period ending 31 May and 30 November and pay by the return date (ss 11 and 14); see [personal income tax](vu-income-tax.md) for the period rules. Annual return and business licence dates: [company formation](vu-company-formation.md).

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

**2. International company registered in 2002.** Under s 118(4) the exemptions end in 2022 (2002 plus twenty years, derived); under s 118(5) they run to 31 December 2099. The two readings differ by 77 years (derived), which is why the conflict must be resolved before reliance.

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
| Rent Taxation Act [Cap 196], Consolidated Edition 2020, Sch 1 (Read for the company rate) | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf | 2026-11-14 |
| Vanuatu Competent Authority, AEOI guide v4 (Read for no income tax system) | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf | 2026-11-14 |
| DCIR rent tax guide (Read for the company case and penalties line) | https://vanuatucustoms.gov.vu/images/Brochures/IRD/eng/Rent_Tax_Guide.pdf | 2026-11-14 |

Not yet confirmed: which of s 118(4) and s 118(5) governs (the 2026 International Companies bill does not settle it; its Gazette Act and operative date were not found); whether any withholding tax applies to dividends, interest or royalties paid to non-residents (the old guide's 0% came from a private website); rent tax penalty amounts; international-company reporting duties to the VFSC.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vu-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vu-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
