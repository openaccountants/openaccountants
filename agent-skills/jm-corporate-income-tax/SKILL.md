---
name: jm-corporate-income-tax
description: "Jamaica corporate income tax for year of assessment 2026. Covers the 25% rate for unregulated companies and 33 1/3% for regulated companies (Bank of Jamaica, Financial Services Commission, Office of Utilities Regulation, Ministry of Finance), the large unregulated company box on Form IT02, the 5% cap on approved donations, capital allowances on Schedule 2, the 15 March deadline for IT02 and the IT07 estimate, the 3% specified-services withholding credit and the transfer pricing schedule. Trigger on Jamaica company tax, corporate income tax Jamaica, IT02, IT07, regulated company, unregulated company, TAJ company return. Built from Tax Administration Jamaica and Jamaica Information Service pages; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/jm-corporate-income-tax"
  jurisdiction: "JM"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Jamaica Corporate Income Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Bodies corporate subject to Jamaican income tax for the **year of assessment 2026** (calendar year to 31 December 2026), filing Form IT02 with Tax Administration Jamaica (TAJ). Amounts are J$.

- **In:** resident companies; the classification as regulated, large unregulated or other unregulated; the computation from accounts profit to tax; filing and estimates.
- **Out:** unincorporated bodies and partnerships (Form IT03); individuals (use `jm-income-tax`); GCT (use `jamaica-gct`); payroll (use `jm-payroll-social`); financial-sector asset tax and special incentive regimes (Special Economic Zones, Junior Stock Exchange), which are listed under Not yet confirmed.

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| Unregulated company rate | 25% | Companies not regulated by the bodies below; in force from 1 January 2013 | Jamaica Information Service, new threshold and corporate income tax rate: https://jis.gov.jm/new-threshold-and-corporate-income-tax-rate-january-1/ |
| Regulated company rate | 33 1/3% | The rate "remains" for regulated companies | same |
| Regulated company, IT02 Box 5 | Regulated by the Financial Services Commission, Bank of Jamaica, Office of Utilities Regulation or Ministry of Finance | Tick the box that fits | TAJ, notes and instructions for returns IT01 to IT05: https://www.jamaicatax.gov.jm/documents/10181/106853/notes_and_instructions.pdf/0e07453f-7925-4475-ab0e-c5457a8b3214 |
| Large unregulated company, IT02 Box 5 | Not regulated and gross income of J$500 million or more | Classification box on the return | same |
| Approved donations cap | 5% of chargeable income, computed as 1/21 of the income before donations (Line 29) | Charitable and educational institutions approved by the Minister of Finance by order | same |
| IT02 annual return and payment of balance | 15 March following the year of assessment | No provision for an extension; file an IT07 provisional estimate if the return cannot be made | same |
| Withholding on specified services | 3% of the invoice value before GCT | Withheld by tax withholding agents on invoices of J$50,000 or more; credit against the company's tax | TAJ, withholding tax on specified services brochure: https://www.jamaicatax.gov.jm/documents/10181/917523/wtss_brochure_sept2015+-.pdf/ddde1b72-c11c-4130-b273-fb4697c0da90 |

The rate the earlier version gave for building societies (30%), life assurance companies (25%) and renewable-energy power producers (25%), and the 0.25% asset tax on specified financial bodies, are not in the table: no official page read today confirmed them (see Not yet confirmed).

### Formula

```
gross operating profit (IT02 lines 8 to 11, per the accounts)
+ / - tax adjustments (line 12): add back depreciation and disallowed items
- capital allowances (line 24, Schedule 2)
- covenanted donations (line 26)
= income before donations (line 29)
- approved donations, at most line 29 / 21 (line 30)
= chargeable income (line 31)
tax = chargeable income x 25% (unregulated) or 33 1/3% (regulated)
less credits (lines 37 to 40): withholding certificates, specified-services 3%
less estimated tax paid (line 43)
= balance due by 15 March
```

## The base

- **Accounts profit** for each activity goes to lines 8 to 11 (gross receipts, cost of sales, gross operating profit, business and administrative expenses), with a breakdown where more than one activity is carried on.
- **Capital allowances** replace accounting depreciation; attach Schedule 2.
- **Covenanted donations** to the University of the West Indies, the University of Technology or another approved institution (deed of covenant; attach proof and Schedule 4).
- **Donations** to approved charitable and educational bodies, capped at 5% of chargeable income.
- **Dividends received from Jamaican resident companies** are taken out of chargeable income at line 34 and taxed separately at line 35; the 2026 rate is listed under Not yet confirmed.
- **Credits** must be backed by certificates; refunds from earlier years are not credits.
- **Connected-person transactions** are declared on Income Tax Schedule 8 (transfer pricing; Income Tax (Amendment) (No. 2) Act, 2015 and the Transfer Pricing Documentation Regulations, 2015).

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | TRN for the company | At incorporation (see `jm-company-formation`) |
| 2 | Form IT07, declaration of estimated income and tax payable, with quarterly payments | 15 March for the current year; revise if the estimate changes |
| 3 | Form IT02 with balance sheet, profit and loss account, subsidiary accounts and the tax computation; Schedules 2, 4 and 8 as they apply | 15 March 2027 for YA 2026 |
| 4 | Pay the balance (line 43) | With the return, 15 March |

Filed online through the TAJ portal. If the return cannot be made by 15 March, TAJ asks for a written explanation and an IT07 provisional estimate by 15 March; there is no extension of the time to file.

## Penalties and interest

The late-filing penalty and interest rate for a late IT02 were not confirmed on a TAJ page read for this version (see Not yet confirmed). For withholding obligations the employer and withholding agent rules in `jm-payroll-social` (50% a year on late PAYE) do not extend to corporate income tax.

## Cross-border points

- Non-resident individuals pay 25% without a threshold; treaty rates for dividends, interest, royalties and management fees are listed in `jm-income-tax` (Cross-border points), from TAJ's non-residents guide.
- Rent paid to a non-resident: 25% withheld by the payer (TAJ non-residents guide).
- Withholding on payments to non-resident companies (dividends, interest, royalties, management fees) at the domestic rate: see Not yet confirmed.

## Two worked examples that recompute

### Example 1: Chargeable income J$20,000,000, unregulated or regulated

An unregulated company pays 25%, J$5,000,000. A company regulated by the Financial Services Commission pays 33 1/3%, J$6,666,666.67. The regulator, not the size, decides the rate; size only decides the Box 5 tick for unregulated companies.

```oa-check
name: JM 2026 company tax, unregulated vs regulated
inputs:
  chargeable: 20000000
steps:
  - tax_unregulated: chargeable * 0.25
  - tax_regulated: round(chargeable / 3, 2)
  - difference: tax_regulated - tax_unregulated
expected:
  tax_unregulated: 5000000
  tax_regulated: 6666666.67
  difference: 1666666.67
```

### Example 2: How much of a donation is deductible? J$3,000,000 or J$1,500,000 given

Income before donations (line 29) is J$42,000,000, so the cap is J$2,000,000 (1/21). A J$3,000,000 donation is allowed at J$2,000,000: chargeable income J$40,000,000, tax J$10,000,000. A J$1,500,000 donation is allowed in full: chargeable income J$40,500,000, tax J$10,125,000. Giving the extra J$1,500,000 saves only J$125,000 of tax, because J$1,000,000 of it is above the cap.

```oa-check
name: JM 2026 unregulated company, donation cap both ways
inputs:
  line29: 42000000
  gift_big: 3000000
  gift_small: 1500000
steps:
  - cap: line29 / 21
  - allowed_big: min(gift_big, cap)
  - tax_big: (line29 - allowed_big) * 0.25
  - allowed_small: min(gift_small, cap)
  - tax_small: (line29 - allowed_small) * 0.25
  - saving: tax_small - tax_big
expected:
  cap: 2000000
  allowed_big: 2000000
  tax_big: 10000000
  allowed_small: 1500000
  tax_small: 10125000
  saving: 125000
```

## Ask the client first

1. Is the company regulated by the Bank of Jamaica, the Financial Services Commission, the Office of Utilities Regulation or the Ministry of Finance? If not, was gross income J$500 million or more?
2. Is it resident in Jamaica, and does it have a branch or income abroad?
3. Accounts for the year, the capital allowances schedule and the fixed asset register.
4. Donations made, to which bodies, and whether each is approved by ministerial order or covenanted.
5. Withholding certificates received (including 3% specified-services certificates) and IT07 estimated payments.
6. Transactions with connected persons, for Schedule 8.

## Sources

| Source | URL | Read on |
|---|---|---|
| Jamaica Information Service, "New threshold and corporate income tax rate January 1" (republished 3 November 2025): read for the 25% rate for unregulated companies from 1 January 2013 and the 33 1/3% for regulated companies | https://jis.gov.jm/new-threshold-and-corporate-income-tax-rate-january-1/ | 2026-11-14 |
| TAJ, notes and instructions for returns IT01 to IT05 (revised November 2013): read for the IT02 section, Box 5 classification, lines 8 to 43, the donations cap, the 15 March date and the IT07 estimate | https://www.jamaicatax.gov.jm/documents/10181/106853/notes_and_instructions.pdf/0e07453f-7925-4475-ab0e-c5457a8b3214 | 2026-11-14 |
| TAJ, withholding tax on specified services brochure: read for the 3% rate and the J$50,000 invoice threshold | https://www.jamaicatax.gov.jm/documents/10181/917523/wtss_brochure_sept2015+-.pdf/ddde1b72-c11c-4130-b273-fb4697c0da90 | 2026-11-14 |
| TAJ, transfer pricing page: read for the Schedule 8 form and the 2015 amendment act and documentation regulations | https://www.jamaicatax.gov.jm/web/guest/transfer-pricing | 2026-11-14 |
| TAJ, non-residents and income tax: read for the non-resident rate and rent withholding | https://www.jamaicatax.gov.jm/documents/10194/20399532/1-Non-residents+and+Income+Tax+Final+Document.pdf/d8ccd3fa-4a99-e798-1a4b-841e952d82ba | 2026-11-14 |

Not yet confirmed: the earlier version's rates for building societies (30%), life assurance companies (25%) and renewable-energy independent power producers (25%); the 0.25% asset tax on deposit-taking institutions, securities dealers and insurers (TAJ's assets tax page was read but its technical note was not found); the 2026 rate on dividends received from resident companies (TAJ notes of 2013 show 15% from 1 April 2013); domestic withholding on dividends, interest, royalties and management fees paid to non-resident companies (earlier version: 15%, 15%, 33 1/3%, 33 1/3%) and the remittance time of 14 days after the month for those; quarterly IT07 instalment dates for companies (earlier version: 15 March, June, September, December); late-filing penalty and interest on corporate tax; the loss carry-forward rule for companies; the earlier version's statement that resident dividend withholding is 15%. The Income Tax Act on laws.moj.gov.jm returned an error (503) and was not read.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `jm-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/jm-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
