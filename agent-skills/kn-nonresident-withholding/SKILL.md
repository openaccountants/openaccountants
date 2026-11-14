---
name: kn-nonresident-withholding
description: "Saint Kitts and Nevis withholding tax on payments to non-residents for 2026 under section 36 of the Income Tax Act, Cap. 20.22 (as amended in 2014 and 2016): 15% of the amount paid on interest, distributions, rents, royalties, management, professional, technical and other service fees, recharges and other payments, whether or not the payment is income or expense to the recipient; year-end accruals treated as paid; a certificate to the payee; quarterly returns and payment by the 15th of March, June, September and December; payer liability; and the IRD late payment penalty of 10% plus 1% a month interest. Trigger phrases include St Kitts withholding tax, Nevis withholding 15%, paying a foreign consultant St Kitts."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kn-nonresident-withholding"
  jurisdiction: "KN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Saint Kitts and Nevis withholding on payments to non-residents

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Withholding from payments to non-residents in 2026 under s.36 of the Income Tax Act, Cap. 20.22 (2017 revision, reflecting Act 3 of 2014 and Act 2 of 2016), administered by the Inland Revenue Department. Amounts are EC$. Corporation tax: [kn-corporate-income-tax](kn-corporate-income-tax.md). The absence of personal income tax on residents' ordinary wages does not settle a cross-border service payment.

## Ask the client first

1. Is the payee resident in the Federation? Determine it under the Act.
2. What is the payment: interest, distribution, rent, royalty, management or head office charge, professional or technical fee, insurance premium, recharge, other service?
3. Is the contract price gross or net of tax?
4. Is the payer on an accruals basis with an amount charged but unpaid at year end?
5. Does a treaty give a lower rate (treaty schedules in the Act cap some at 15%)?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Rate, s.36(1) | Fifteen percent of the amount paid, whether or not the payment produces profits for the recipient or is of an income or expense nature | [Income Tax Act, Cap. 20.22, s.36](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf) |
| Certificate, s.36(2)(a) | To the non-resident, stating the payment and the tax withheld | same |
| Return and payment, s.36(2)(b) | Quarterly, on or before the 15th day of March, June, September and December, for the preceding quarter | same |
| Accruals, s.36(6) | An amount charged as an expense but unpaid is treated as paid on the last day of the basic or financial year | same |
| Payer liability, s.36(4) | A payer who fails to withhold or to pay over is liable for the tax | same |
| Late payment penalty | 10% of the tax due | [IRD FAQs](https://www.sknird.com/faqs/) |
| Late payment interest | 1% per month or part | same |

### Steps

1. **Residence:** test the payee under the Act.
2. **Scope:** the payment types in s.36(1), including deemed branch profit remittances.
3. **Withhold** 15% of the gross amount (gross up if the price is net).
4. **Certificate** to the payee.
5. **File and pay** the quarterly return by the 15th; SMARTS is the channel.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Treaty country | The headline rate does not settle treaty entitlement; check residence and the treaty | [Cap. 20.22](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf) |
| Contract price net of tax | Gross up: gross = net / 0.85 | same |
| Accrued at year end, paid later | Tax due as if paid on the year end | same |
| September to November 2026 quarter | Due 15 December 2026 (IRD calendar) | [IRD tax calendar](https://www.sknird.com/tax-calendar/) |
| Payment to a resident | Not s.36; s.37 retained for some deductible payments to residents | [Cap. 20.22, s.37](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf) |

## Worked cases

### Case 1: a foreign consultant's EC$20,000 fee

Withhold 3,000 and pay the consultant 17,000.

```oa-check
name: St Kitts withholding on 20,000 consulting fee
inputs:
  fee: 20000
steps:
  - tax: fee * 0.15
  - net: fee - tax
expected:
  tax: 3000
  net: 17000
```

### Case 2 (decision): pay on time, or two months late?

Tax withheld 3,000 is paid two months after the due date: penalty 300 and interest 60 (2 x 1% x 3,000), 360 in all. Paying on time costs nothing extra. If the contract promised the consultant 20,000 net, the gross is 23,529.41 and the tax 3,529.41 (derived).

```oa-check
name: St Kitts withholding late by two months, and net-of-tax gross-up
inputs:
  tax: 3000
  months: 2
  net_fee: 20000
steps:
  - penalty: tax * 0.10
  - interest: tax * 0.01 * months
  - cost_of_delay: penalty + interest
  - gross: round(net_fee / 0.85, 2)
  - tax_on_gross: round(gross - net_fee, 2)
expected:
  penalty: 300
  interest: 60
  cost_of_delay: 360
  gross: 23529.41
  tax_on_gross: 3529.41
```

## When to refuse or refer

- Treaty claims and branch profit remittances.
- Residence disputes.
- Payments that may be employment income of a non-resident working in the Federation.

## Filing and payment

1. Withhold at payment (or at year end for accruals).
2. Issue a certificate to the payee.
3. File the quarterly return and pay by the 15th of March, June, September and December.

## Completion checklist

- Payee residence tested; payment type in s.36(1).
- 15% of the gross; certificate issued.
- Quarterly return and payment on time.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act Cap. 20.22 (2017 revision): read for s.36 (15%, payment types, certificate, quarterly return, payer liability, accruals) and s.37 | https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf | 2026-11-14 |
| IRD FAQs: read for the 10% late payment penalty and 1% a month interest on withholding tax | https://www.sknird.com/faqs/ | 2026-11-14 |
| IRD tax calendar: read for 15 December 2026 | https://www.sknird.com/tax-calendar/ | 2026-11-11 |
| IRD withholding tax form guide: read for the filing form | https://eservicesskn.sknird.com/UserFiles/FormGuide/Sam170217075715.pdf | 2026-11-11 |

Not yet confirmed: amendments after the 2017 revision; current treaty rates; the IRD form guide and calendar were read by Ryan Duguid on 2026-11-11 and not re-opened here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kn-nonresident-withholding` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kn-nonresident-withholding. If neither is available, confirm every figure against the official source pages cited above before relying on it.
