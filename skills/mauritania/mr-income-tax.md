---
name: mr-income-tax
description: "Prepare a source-based Mauritania research file for individual business profit, employment and property-income classification in the 2026 country pack. Use this Guide to identify the taxpayer, classify the transaction, assemble the relevant documents and compare the cited statutory baseline with later amendments. It covers the stated ordinary cases, computation conditions, filing obligations and worked decisions, with official source links and explicit limits. Trigger phrases include Mauritania tax, DGI, taxpayer registration, taxable base, payment deadline and compliance evidence. This is a partial research draft: the complete operative amendment chain and current submission procedures are not established, and no licensed accountant has attested this revision."
jurisdiction: MR
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.2
tax_year_notes: "2026 research draft; cited historical baseline and selected later replacements; operative amendment chain incomplete"
---

# Mauritania Individual Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research draft, source baseline only.** The computations below reproduce the cited official code/provisions, not a certified complete statement of operative 2026 law. The January 2023 official code lists amendments only through the January 2022 Finance Act. Selected later Finance Acts were read, including the 2024 transfer-pricing replacement, but the complete commencement/publication chain is not closed. The signed/stamped rectifying Finance Act is visibly numbered 2026-035 on physical page 6. It changes material expense, digital-service and compliance rules; the retained comparison-column headings do not establish proposal status, and its upload date does not prove the operative date. [N02] Resolve the amendment file before using these baselines to file, pay or advise. No accountant has signed this revision.

## Who this applies to

Natural persons with business profits, salary or ordinary rental income. Mauritania has separate schedules rather than one universal personal-income base. This Guide owns ITS base/formulas; [payroll](mr-payroll-social.md) owns employer process and contributions. Covered baseline computations require the amendment hold to be resolved.

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| IBAPP regimes [I02] | Normal applies above MRU 5,000,000 turnover excluding tax; intermediate from MRU 3,000,000 to MRU 5,000,000; forfait strictly below MRU 3,000,000. Importers cannot use forfait. Read two-year downward transitions, next-year normal transition, immediate forfait crossing, prorating and elections under arts. 73, 77–82. | [CGI arts. 73, 77–82](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |
| IBAPP real-regime computation [I03] | Ordinary normal/intermediate IBAPP compares 30% of taxable profit with 2.5% of art. 8 taxable products excluding transfers/reversals of charges, then the respective MRU 125,000/MRU 75,000 minimum. Transport, art. 225 margin businesses, retail petroleum and artisanal fisheries have separate rules in art. 87(3), (4), (6). | [CGI art. 87](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |
| Forfait computation [I04] | Qualifying forfait taxpayers pay 3% of declared turnover using a DGI-issued or approved form by 31 March. Keep the receipts/expenses register under art. 84; this is not permission to treat an importer as forfait. | [CGI arts. 81, 84, 88](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |
| ITS formulas [I09] | For ordinary personnel outside the special written-contract categories in art. 114(6), round taxable monthly remuneration RI down to MRU 10 after base adjustments. If RI is at most 9,000, tax = RI × 15%; above 9,000 through 21,000, tax = RI × 25% minus 900; above 21,000, tax = RI × 40% minus 4,050. Fraction-month pay is prorated; nonmonthly pensions/annuities are converted to monthly. Qualifying direct written-contract personnel of press establishments, airlines and air-navigation agencies have the separate 20% maximum described in I14; do not apply these ordinary formulas to them without resolving that rule. | [CGI art. 114(1)–(6)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |
| Property income [I13] | IRF applies to rent and covered property gains outside taxable business profit, subject to the art. 75 election. Ordinary rent base is rent accrued whether received or not; subletting uses the rent difference. Art. 102(4) exempts annual rental income at most MRU 6,000 only where it is exclusive of all other income. IRF is 10%; the ordinary rent declaration/payment is before 1 March. | [CGI arts. 99, 102, 105–106](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |

## The base

- **Separate individual business tax [I01].** IBAPP taxes habitual own-account profit-making activity of natural persons and qualifying persons outside IS. Use Mauritanian profits and treaty allocations under art. 71, rather than applying one worldwide-income statement to every category of personal income. [CGI arts. 68–71](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **IBAPP tax base [I05].** Art. 74 imports IS profit rules but excludes specified exchange gains/losses, head-office charges, gifts/subsidies, deferred depreciation in loss periods, accelerated/declining depreciation and provisions. Property in the business balance sheet can enter an irrevocable IRF election under art. 75, with related expenses no longer deductible from IBAPP. [CGI arts. 74–75](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Employment territorial scope [I07].** ITS covers salary for work in Mauritania; it also covers a domiciled employee even where work or employer is abroad, and an employee domiciled abroad where the work is in Mauritania, subject to treaties. Fiscal domicile is a permanent home, or, without such a home, the centre of vital interests. [CGI art. 111](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Employment base and exemption [I08].** Use cash remuneration and salary supplements, art. 113 benefit-in-kind treatment, compulsory pension/social deductions and art. 110 exemptions. Art. 110(1)(c) excludes MRU 6,000 monthly remuneration before the art. 114 scale. The scale thresholds refer to the resulting taxable remuneration, not unadjusted gross salary. [CGI arts. 109–114](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Employment exceptions [I10].** Professional expense allowances other than housing, transport, responsibility and office allowances have a combined MRU 1,000 monthly exemption under art. 110(1)(b); family-related allocations and listed war/disability pensions have their own exemptions. Art. 110(4) exempts real-value benefits in kind not exceeding 20% of cash remuneration; art. 113 otherwise refers to 40% benefit inclusion. Obtain a category-by-category benefit reconciliation before using that interaction. [CGI arts. 110, 113](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).

- **Special ITS personnel maximum [I14].** Art. 114(6) subjects personnel working directly under written contracts with a national or foreign press company/establishment implanted in Mauritania, airlines or air-navigation agencies to the scale in force, capped at a maximum of 20%. These special categories are excluded from this Guide’s ordinary formula examples. The exact cap-computation interpretation is not established here; obtain it before computing their tax rather than inventing a flat 20% tax or a new formula. [CGI art. 114(6), physical p. 46](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).

## Deadlines and filing

- **IBAPP filing and payments [I06].** Declare by 31 March for the previous 31 December year. Ordinary real-regime IBAPP pays 40% by 31 March, 30% by 30 June and the balance by 30 September; forfait is fully payable when the return is delivered, by 31 March. [CGI arts. 90, 94–96](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Salary withholding and annual schedule [I11].** The payer withholds when paying and reports/remits by the 15th of the next month using the prescribed form with NIF, period, remuneration and total withholding. The annual per-beneficiary salary schedule is due in the first fifteen days of February; art. 117(2) sets MRU 200 per omission/inaccuracy. [CGI arts. 115–117](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Foreign employer/direct payment [I12].** An employee covered by art. 111(2)(a) declares and pays ITS on taxable income by the 15th of the month after receipt using the prescribed form at the Treasury accountant for their domicile. This is not a universal annual March salary return. [CGI art. 118](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).

## Penalties and interest

- **Annual filing sanctions [C15].** The baseline LPF L.131(3) imposes 1% of tax-inclusive turnover for a missing/late annual return or mandatory document, with ordinary minimums MRU 50,000 normal and MRU 35,000 intermediate, and separate exempt/convention-company minimums MRU 150,000 and MRU 75,000. Confirm which failure is assessed; do not silently substitute a generic late-payment percentage. [LPF art. L.131(3)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).

## Cross-border points

Classify the income before deciding scope: salary domicile/work rules in I07 do not replace the business territorial rule in I01. The old claim that all residents have a blanket exemption for any foreign income already taxed abroad is not established here. Apply an actual treaty only after reading it for the taxpayer/payment.

## Two worked examples that recompute

### 1. ITS baseline: exemption precedes formula

Assume ordinary personnel outside art. 114(6), cash-only monthly remuneration MRU 18,500, deductible compulsory contribution MRU 500 and no other deductions/benefits. Subtract the MRU 6,000 remuneration exemption, then round down to MRU 10: RI 12,000. Tax is 12,000 × 25% minus 900 = MRU 2,100. Gross-pay bands would give a wrong answer.

```oa-check
name: ITS baseline: exemption precedes formula
inputs:
  gross: 18500
  compulsory: 500
steps:
  - ri: floor(max(0, gross - compulsory - 6000) / 10) * 10
  - tax: ri * 0.25 - 900
expected:
  ri: 12000
  tax: 2100
```

### 2. Forfait or real election: compare both baseline amounts

Assume a non-importing business eligible for forfait with turnover MRU 2.4m and profit MRU 100,000. Forfait is 72,000. A valid voluntary intermediate-real election would compare profit tax 30,000, products minimum 60,000 and fixed floor 75,000, giving 75,000. This numerical comparison favours forfait by 3,000; it does not establish that an election was made or captures bookkeeping/VAT consequences.

```oa-check
name: Forfait or real election: compare both baseline amounts
inputs:
  turnover: 2400000
  profit: 100000
steps:
  - forfait: turnover * 0.03
  - real: max(profit * 0.3, turnover * 0.025, 75000)
  - difference: real - forfait
expected:
  forfait: 72000
  real: 75000
  difference: 3000
```

## Ask the client first

- Business, employment, pension, rent or investment income?
- Domicile/permanent home, vital interests, work location and employer location?
- Turnover, imports, regime history and any valid election?
- Gross pay, benefits, mandatory contributions and qualifying exemptions?
- Rental contracts, accrued amounts, other income and business-property election?

## Sources

| Source and exact scope read | URL | Read on |
|---|---|---|
| cgi2023: Official version cover/amendment list and selected CGI arts. 1–14, 23–24, 40–48, 49–67, 68–98, 99–118, 119–137, 150–157, 209–215 (exemption list introductory categories only), 216–221, 227–250, 253–254, LPF L.131–L.139. Not the entire 168-page code or full sector/special regimes. | https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf | 2026-11-01 |
| Amendment hold: signed/stamped law 2026-035 identity on physical page 6 and art. 3.1 printed pp. 6–18 read; operative date not established | https://www.finances.gov.mr/sites/default/files/2026-08/LFR%202026%20FR.pdf | 2026-11-01 |

Not yet confirmed: complete operative 2026 amendment chain and current forms/portal screens; blanket worldwide/foreign-taxed-income exemption asserted in the old Guide, not established by the provisions read; special art. 114(6) cap-computation interpretation; benefit-in-kind interaction for actual benefits, tax residence treaty tie-breaks and foreign tax relief; property disposal/holding-period relief, local property contributions and full investment-income exclusions.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
