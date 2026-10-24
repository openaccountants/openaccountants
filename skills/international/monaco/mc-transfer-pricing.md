---
name: mc-transfer-pricing
description: "Monaco transfer pricing reference for 2026 based on the normal foreign commercial and financial conditions rule in Ordinance 3.152. Covers foreign counterparties, controlled and common control profit transfers, comparison evidence, related deduction restrictions and ordinary business profits tax adjustments. Use for Monaco related party pricing, foreign management fees, finance charges and arm length working papers. Includes two reproducible adjustment illustrations with explicit assumptions. Formal documentation, country by country reporting, special penalties and agreement procedures remain unresolved. Partial source cited draft awaiting a named Monaco professional review."
jurisdiction: MC
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 1.1
---

# Monaco transfer pricing and normal foreign conditions

> **Source-cited draft; partial scope.** Checked 24 October 2026. No named Monaco professional has reviewed this Guide. It produces a working paper, not a filing or a final tax position. Read the [country gap register](README.md) before use.

## Who this applies to

Tax year 2026. Ordinance 3.152 article 14 first addresses **non-normal commercial or financial conditions with any foreign resident or established person**, not only transactions with a specified ownership percentage. It then expressly addresses capital/management participation, dependence/control and common-control indirect profit transfers. Its first limb refers to ISB, turnover taxes and other named taxes. Screen all foreign conditions before narrowing the analysis to a group relationship. [Art. 14](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

This Guide covers the normal-conditions adjustment rule and working-paper arithmetic. It does not establish formal local/master-file, country-by-country reporting, disclosure, safe-harbour or advance-agreement requirements. Absence of those rules from this draft is not a finding that none exists.

## Rates, bands and thresholds

| Item | Amount or rule | Period | Official source |
|---|---|---|---|
| Article 14 first-limb relationship threshold | No ownership percentage specified in that limb | 2026 | [Art. 14](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Ordinary ISB rate on an established taxable adjustment | 25% | 2026 | [Art. 21](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| TP documentation/reporting thresholds | Not established here | Gap | [Art. 14 only; not proof of filing obligations](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |

## The base

1. Obtain the contracts, invoices, counterparties, ownership/control and functions, assets and risks. Identify the foreign commercial/financial condition actually imposed.
2. Evidence normal market conditions or usual service tariffs. Article 14 requires restoration of the accounting/tax result to normal conditions. A quoted “market price” is an assumption until comparability evidence supports it.
3. For controlled enterprises, reconcile profits transferred through purchase/sale pricing or any other means, including common-control arrangements. Avoid counting the same adjustment under multiple limbs.
4. If precise adjustment evidence is unavailable, article 14 permits comparison with similar normally operated enterprises. This is not authority to invent a markup.
5. Reconcile the adjustment to the ordinary ISB result, losses and credits; do not assume every adjustment produces immediate cash tax. [Arts. 7, 14, 21–22](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

Payments of specified fees, royalties, commissions and similar non-salary items to Monaco residents also face article 12: the recipient must be independent and the payer must substantiate a genuine arrangement not concealing realised/transferred profit. A domestic payment is not automatically deductible because article 14 concerns foreign relations. Shareholder interest and executive remuneration need separate articles 9 and 13 checks. [Arts. 9, 12–14](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

## Deadlines and filing

For ordinary ISB, include the accounting-to-tax reconciliation and article 23 disclosures by the return deadline: within three months of year end, or before 1 April next year if no year closes. Record counterparties, terms and evidence in the review file. These are working-paper steps; this Guide has not established a TP-specific return, documentation deadline, retention period, CbCR filing duty or filing route. [Art. 23](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

## Penalties and interest

Article 14 supplies the adjustment authority, not a complete separate TP penalty schedule. For an ISB assessment, articles 34–37 contain the ordinary declaration/payment and adjustment sanctions. Article 35 provides conditional late-payment 3% within the first month after due date plus 1% per additional month or fraction; article 36 permits up to 150% on good-faith assessments/adjustments, and article 37 four times the tax for bad faith/fraud. Determine procedure and facts before applying a penalty. Any separate documentation/reporting sanctions remain unverified. [Arts. 34–37](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

## Cross-border points

Check the counterparty jurisdiction independently for deductibility, withholding, corresponding relief and treaty coverage. This Guide does not promise a corresponding adjustment or a mutual-agreement route. Do not treat an ISB adjustment as automatically the same VAT base adjustment: article 14 mentions multiple taxes, whose own rules still need analysis. Large-group reporting and minimum-tax implementation remain gaps. [Arts. 14, 22](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152); [Project 1.129, project status only](https://legimonaco.mc/projet/1.129).

## Two worked examples that recompute

### Underpriced foreign sale

Assume 100 units sold to a controlled foreign company at EUR 800 per unit. Reliable comparable evidence establishes EUR 1,000 under equivalent conditions. Revenue is understated by EUR 20,000. For an otherwise fully taxable ordinary ISB business with no losses or credits, the incremental ISB is EUR 5,000. Article 14 controls the adjustment; EUR 1,000 is an assumed evidenced price, not a safe harbour.

```oa-check
name: Foreign sale normal price adjustment
inputs:
  units: 100
  charged: 800
  normal: 1000
steps:
  - booked: units * charged
  - normal_revenue: units * normal
  - adjustment: normal_revenue - booked
  - extra_isb: adjustment * 0.25
expected:
  adjustment: 20000
  extra_isb: 5000
```

### Excess foreign finance charge

Assume a booked EUR 10,000 foreign finance charge, with independently supported normal terms giving EUR 6,000, and all other deduction rules already satisfied for that EUR 6,000. The EUR 4,000 excess is added back and incremental ordinary ISB is EUR 1,000, assuming no losses/credits. This is not an approved interest rate and does not replace article 9's separate financial-expense restrictions.

```oa-check
name: Foreign finance normal terms with separate deduction tests assumed
inputs:
  booked_charge: 10000
  normal_charge: 6000
steps:
  - addback: max(0, booked_charge - normal_charge)
  - extra_isb: addback * 0.25
expected:
  addback: 4000
  extra_isb: 1000
```

## Ask the client first

- Which foreign counterparties, ownership/control and actual arrangements exist?
- What contracts, functions and comparable prices or service tariffs support the terms?
- What domestic fees, royalties, financing and executive payments also need deduction tests?
- What group size, reporting entities and other-country filings are involved?
- What periods, losses, credits or existing adjustments affect the tax result?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Ordinance 3.152, arts. 7, 9, 12–14, 21–23, 34–37 | https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152 | 2026-10-24 |
| Project 1.129, project status only | https://legimonaco.mc/projet/1.129 | 2026-10-24 |

**Not yet confirmed:** formal documentation, CbCR, disclosures, retention periods, safe harbours, agreements and separate penalties. No threshold exemption is inferred.
