---
name: sy-currency-transition-and-tax-records
description: >
  Syria 2026 currency redenomination and financial-document research draft. Covers the 100-to-1 conversion, tax-obligation scope, ambiguous documents and the end of old-note circulation, with two reconciliation examples. Does not establish current tax rates, thresholds or a complete country pack.
jurisdiction: SY
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://sana.sy/presidency/2364708/"
    title: "SANA: full text of Decree 293/2025"
    as_of: "2026-10-22"
  - url: "https://sana.sy/economy/syrian-economy/2543099/"
    title: "SANA: Central Bank statement on old-note withdrawal, 2 August 2026"
    as_of: "2026-10-22"
  - url: "https://sana.sy/economy/syrian-economy/2603216/"
    title: "SANA: Finance Ministry statement on tax reform and local fees"
    as_of: "2026-10-22"
---

# Syria: currency transition and tax records

## Scope

This Guide addresses a prerequisite for using Syrian monetary tax figures: identifying their denomination. It is not an income-tax schedule or filing instruction. Sources are the decree reproduced in full by the official news agency and its reports of government statements; Arabic controls. Implementation in the taxpayer's location and later measures must be established separately.

## Conversion and documentary rules

Decree 293/2025 starts replacement on **1 January 2026** at **100 old Syrian pounds to one new pound**. Article 8 extends the conversion to wages, prices and financial obligations, including tax obligations; dual display applies during replacement periods. Article 7 prohibits charges on conversion/replacement itself, not taxes on unrelated transactions.

Article 9 preserves the old-currency value basis for pre-replacement documents unless otherwise agreed. Article 10 requires clarification of currency for undated or replacement-period documents before payment, through specification, agreement or judgment. Do not infer denomination from the number alone. [Decree 293/2025, articles 1, 3 and 7–10](https://sana.sy/presidency/2364708/).

## Old notes: historical windows are not current payment permission

The Central Bank statement reported on **2 August 2026** says replacement ended **30 July 2026** and old notes lost legal-tender status. It describes withdrawal beginning 31 July for five years, with a temporary banks/post-office window on 2–6 August, followed by the Central Bank in Damascus and an appointment application. The temporary window has passed. Withdrawal of old notes is distinct from permission to use them to settle debts. Confirm current arrangements before attempting redemption. [Central Bank statement reported by SANA](https://sana.sy/economy/syrian-economy/2543099/).

## Tax rules must also be checked for the relevant period

The Finance Ministry statement reported in October 2026 describes preparations for a new tax system at the start of the following year. That announcement does not establish an enacted rate or commencement rule. It also distinguishes local licensing charges from new central taxes. Do not apply announced reform terms as if they were operative law, or assume converting a historical threshold makes it legally current. [Finance Ministry statement reported by SANA](https://sana.sy/economy/syrian-economy/2603216/).

## Example 1: confirmed old-denomination liability

Assume an independently established liability is 2,500,000 old pounds, with no subsequent adjustment. Its unit conversion is 25,000 new pounds. This does not verify the underlying assessment or payment channel.

```oa-check
name: Syria old liability denomination conversion
inputs:
  old_liability: 2500000
  old_per_new: 100
steps:
  - new_liability: old_liability / old_per_new
expected:
  new_liability: 25000
```

## Example 2: reconcile a mixed-denomination ledger

Assume a confirmed receivable of 1,000,000 old pounds and a payment of 4,000 new pounds. Convert first: 10,000 new less 4,000 new leaves 6,000 new. Retain both original denomination and conversion evidence. Subtracting the raw numbers would be meaningless.

```oa-check
name: Syria mixed denomination reconciliation
inputs:
  old_receivable: 1000000
  old_per_new: 100
  new_payment: 4000
steps:
  - new_receivable: old_receivable / old_per_new
  - new_balance: new_receivable - new_payment
expected:
  new_receivable: 10000
  new_balance: 6000
```

## Records and remaining work

For each figure retain the original source, date, denomination, assessment period, conversion and reconciliation. Preserve historical records; do not overwrite their original amounts. Ambiguous documents require resolution before using these examples. These record controls are recommendations, not a verified statutory retention period.

Remaining work includes current tax laws and amendments, threshold changes, return-form units, rounding instructions, payment procedures, legal tender and redemption updates, and territorial implementation. No complete tax-system, compliance or country coverage is claimed.

## Sources

- [Decree 293/2025 reproduced by SANA](https://sana.sy/presidency/2364708/).
- [Central Bank withdrawal statement, 2 August 2026](https://sana.sy/economy/syrian-economy/2543099/).
- [Finance Ministry reform statement](https://sana.sy/economy/syrian-economy/2603216/).

## Disclaimer

Source-cited research draft. No professional attestation. Verify applicable law and facts before filing or payment.
