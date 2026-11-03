---
name: gn-corporate-income-tax
description: "Guinea corporate income-tax and minimum-tax working method for an ordinary company in the declarative regime for 2026. Use it to test IS versus TPU scope, bridge accounting profit to taxable profit, apply ordinary loss limits, select the statutory corporate rate, compute the prior-year-turnover IMF with the correct floor and ceiling, and reconcile instalments, annual settlement and distinct credit balances. It also distinguishes payer withholding from the company's own profit tax. The method uses enacted CGI provisions and finance-law amendments corroborated by the April 2026 DGI précis. Establish their applicability to the actual period, including any October rectification, before live use. Sector regimes, specialised deductions, group relief, treaty relief and complete transfer-pricing documentation remain separate gaps."
jurisdiction: GN
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 1.1
---

# Guinea corporate income tax and IMF v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

**Governing-version prerequisite:** establish the operative CGI provisions, amendments and administrative interpretation for the actual period, including any October 2026 rectification. The enacted base, 2022-2025 amendment chain and DGI précis updated for LFI 2026 are available; the October promulgated wording/effect has not been retrieved. If applicability is unresolved, label the output hypothetical source-version analysis and stop before a live liability, deduction, withholding, filing or payment conclusion. Do not infer that an unretrieved amendment was not enacted.

CGI 220 subjects SA, SARL and SAS, including single-member forms, investment companies and cooperatives to IS by form; other entities enter by option or profitable activity, and article 220 II specifies partial liability for particular public/association income. Confirm exemptions under article 221 and any actual investment/CGA approval before applying an ordinary-company calculation. Legal form alone does not decide the small-business regime. [CGI 220-227](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

CGI 275 generally routes turnover below GNF 1,000,000,000 to TPU. Article 276 excludes specified cases, including VAT-option taxpayers, letting properties held as business assets, petrol-station managers and gold/diamond trading counters. The VAT option under article 360 has a GNF 500,000,000 turnover or investment condition expressed as greater than or equal to that amount. Obtain the actual registration/option and taxpayer category; do not assume every company below the general threshold pays TPU or every such company can simply elect IS. This Guide computes ordinary IS/IMF after regime classification; it does not compute TPU. [CGI 275-276,360](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §1.2.1.2 and §1.6](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

## Rates, bands and thresholds

| Item | Rate, amount or condition | Official source |
|---|---|---|
| Ordinary IS | 25% of taxable profit rounded down to the next GNF 1,000 | [CGI 229](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Telephony, banks/insurance and specified petroleum import/storage/distribution companies | 35%; classify the actual statutory activity | [CGI 229 II 1](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Companies holding a mining research permit or exploitation title | 30%; special mining/stability terms need separate review | [CGI 229 II 2](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| IMF | 2% of the preceding year's turnover, regardless of current profit/loss | [LFI 2024 art. 8 replacing CGI 244](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf) |
| Medium enterprise IMF | Minimum GNF 20,000,000; maximum GNF 300,000,000 | [LFI 2024 art. 8](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf) |
| Large enterprise IMF | Minimum GNF 300,000,000; maximum GNF 2,000,000,000 | [LFI 2024 art. 8](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf) |
| Organised liberal professions | Fixed IMF GNF 10,000,000 where the statutory order/chamber condition applies | [LFI 2024 art. 8](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf) |
| Ordinary prior losses | DGI describes deduction capped at 70% of the next positive taxable profit and indefinite carry-forward of the unabsorbed balance | [CGI 107](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §1.2.3.4, charges reportées](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx) |

The source chain replaces the original Code's IMF and the 2023 3% amendment with the 2024 2% provision. The April 2026 DGI précis confirms 2% and these floors/ceilings. Keep the actual DME/DGE classification evidence; do not choose the cheaper IMF bounds as an election. [LFI 2023 art. 7](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2023.pdf); [LFI 2024 art. 8](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf); [précis §1.2.4.2](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

## The base

### Bridge accounting profit to taxable profit

1. Establish residence/territorial scope and the reporting period. CGI 223 links resident companies and Guinea permanent establishments to articles 15 bis/ter; CGI 224 imports the business-profit rules. Use the ordinary calendar year, with separately reviewed first-period exceptions. A foreign registration address alone does not settle effective management or treaty scope. [CGI 4,15 bis/ter,91,223-224](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
2. Start with the signed trial balance and accounting profit before profit tax. Reconcile sales, accrued certain receivables/payables, inventories, financial/other income and asset disposals to records. CGI 92 taxes the operations and net-asset result; inventories use cost or lower closing market value and work in progress uses cost. Do not substitute cash collected for ordinary profit recognition. [CGI 91-92](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
3. Test expenses cumulatively: direct business interest, non-excessive amount, real identified supply/service, sufficient evidence, proper period accounting and reduction in net assets. Capital extensions/transformations are assets rather than immediate repairs. Add back personal/non-business costs, profit taxes/IMF, taxes withheld for employees/third parties, and statutory tax/regulatory sanctions under their governing provisions. [CGI 93-95](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
4. Reconcile depreciation/provisions separately to the asset and provision schedules. Article 98 requires a specified probable loss/charge arising from current events, accounted for and shown on the provision schedule; reverse deductible provisions when used inconsistently or no longer needed. Do not deduct a general reserve or a provision for a known certain expense as a speculative future loss. Asset-specific depreciation rates, accelerated methods and asset-disposal reinvestment relief require the governing schedule/conditions and remain outside the automatic calculation here. [CGI 98,101-105,109](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [précis §1.2.3.4](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).
5. For finance costs, confirm the statutory withholding actually applied, the shareholder/related-party relationship, paid-up capital and the applicable official central-bank rate cap where article 97 requires it. Related lending also has an article 97 A adjusted-result limit; management/royalty/head-office charges have article 100 caps and transfer-pricing controls. Do not deduct these items solely because invoiced or insert an unverified current central-bank rate. This ordinary workpaper stops for those detailed calculations until their evidence is supplied. [CGI 97-100](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [LFI 2024 arts. 9-17](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf).
6. Include ordinary fixed-asset disposal gains in profit unless a separately established relief applies. A general standalone 15% corporate capital-gains rate is not established by the historical Guide; share transfers, indirect-control transfers, mergers, parent-subsidiary dividends and reinvestment relief each need their own conditions. [CGI 92,105,225-226,243 ter/quater](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
7. Establish the supported tax-loss opening balance, prior use and exemption history. For an ordinary positive pre-loss result, deduct no more than the smaller of available losses and 70% of that result; carry the remaining ordinary balance as described in current DGI doctrine. Do not manufacture a loss from a totally exempt period or import a foreign-establishment loss into the ordinary pool. Preserve the separate treatment needed for investment reductions and foreign operations. [CGI 107](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §1.2.3.4 and §1.2.3.6](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).
8. For a loss result, compute no negative profit IS and retain the qualifying loss separately; IMF can still apply. Floor a positive resulting taxable profit to GNF 1,000 and apply the correct article 229 rate. Keep exempt/reduced tax and any foreign tax credits separate. The examples below assume no special sector, approval, foreign income or disputed deduction. [CGI 229](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

### Compute IMF separately and reconcile credit buckets

Use the preceding calendar year's supported IMF turnover. The DGI describes amounts actually received from operating, financial and non-ordinary activities, excluding indirect taxes and specified properly booked provision reversals/charge transfers. This differs from accounting sales alone and from the accrual profit base; prepare a documented reconciliation rather than take an arbitrary turnover line. Apply the relevant medium/large floor and ceiling to 2% of that base, or the applicable fixed professional rule. [CGI 244 as replaced](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf); [DGI précis §1.2.4.2](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

Test article 245 before charging IMF: exemptions include specified partially IS-liable/exempt bodies, genuinely new companies for their first calendar year of operation (not legal-person transformations), and qualifying ceased businesses; approved investment/CGA cases have separate conditions. First-calendar-year IMF relief differs from the first-financial-year IS instalment exemption. A long first accounting period does not automatically extend IMF relief through a second calendar year. [CGI 245-246](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [précis §1.2.4.2](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

Track three separate balances: the current-year IMF paid, actual cash IS instalments, and other independently validated credits. IMF offsets only IS instalments and the annual balance for that same tax year, is not a deductible expense, and its unused excess is a definitive charge with no future carry-forward/refund. Cash instalment overpayment is a separate credit against future IS/IMF under DGI guidance, without a cash refund. Never turn unabsorbed IMF into that transferable credit. [CGI 236,246](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §1.2.5.2-3](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

## Deadlines and filing

Pay IMF spontaneously by 15 January of the year for which it is due, using prior-year turnover. The April 2026 DGI guidance continues the two instalments due by 15 June and 15 September, each one third of reference-year IS, rounded down to GNF 1,000; genuinely new companies are exempt for their first financial year. The 2023 amendment reproduces only the first sentence of article 236 I on two rounded instalments and repeals article 237. It does not reproduce the prior fraction sentence, so the continued one-third method is expressly attributed to current DGI guidance rather than inferred from the abbreviated amendment alone. Do not confuse that exemption with the IMF calendar-year rule. For reduction or dispensation of the second instalment, article 236 IV requires a motivated request at least thirty days before its due date and the administrative response process; do not reduce a payment unilaterally. [CGI 236,246](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [LFI 2023 art. 8](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2023.pdf); [DGI précis §1.2.5.1](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

File the annual result and pay the remaining IS by 30 April after year-end, even if the declared result is a loss; exemption/approved investment status does not automatically remove the return. Reconcile IMF already used, cash instalments and separately supported credits to avoid deducting the same amount twice. Filing is electronic through e-Tax/SAFIG under amended article 108 III, which also states that the expert-comptable visa is electronic. Establish the applicable visa requirement and completed validation before submission; this workpaper is not that professional visa. Retain the approved result bridge, accounts, depreciation/provision and associate-account schedules, filing acknowledgement, payment references and credit roll-forward. [CGI 108-110,241](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [LFI 2025 art. 26](https://dgb.gov.gn/wp-content/uploads/2025/02/Loi-de-Finances-Initiale-2025.pdf); [DGI précis §1.2.6](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

The current authenticated form boxes and detailed third-party declaration/circular formats have not been inspected. A prepared working paper is not a filed return or a payment receipt.

## Penalties and interest

CGI 1170 III charges interest at 1.5% per month or fraction; it runs from the first day of the month after the month in which payment was due, with the endpoint varying for adjustment, spontaneous correction or other payment. Interest is separate from fiscal penalties. The DGI précis cross-reference to article 1171 for this rate does not match the enacted Code: article 1171 governs penalty approval/motivation; the rate and clock are in article 1170. Do not calculate a live assessment without its due-date, principal, procedural category and governing version. Complete current late-filing/understatement penalties and relief/appeal procedures remain a separate gap. [CGI 1170-1171](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Cross-border points

Separate the company's own IS from amounts it must withhold as payer. The old unqualified 10% dividend/interest assertions are not retained: the enacted income-from-capital provisions set a 15% default for the specified resident/non-resident recipients, with recipient-specific exclusions and treaty conditions. Article 186 bis excludes covered income received by resident IS-liable companies; it is not safe to apply a single withholding rate to every distribution or interest payment. Article 198 sets 15% on the gross specified Guinea-source service/royalty remuneration paid to non-residents, subject to source, establishment and treaty analysis. Treat these as classification controls, not a complete withholding filing method. [CGI 186 bis-190,198](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

Establish the payee, beneficial ownership, residence, presence/permanent establishment, income category and actual treaty before deciding relief or a gross-up. Foreign credits under articles 231-232, branch profit allocation, transfer-pricing documentation and treaty tables are not completed by this ordinary-company Guide. Keep those jobs and supporting withholding certificates separate. [CGI 15 bis/ter,198,231-232](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Two worked examples that recompute

An established medium enterprise has validated preceding-year IMF turnover GNF 2,000,000,000 and reference-year IS GNF 90,000,000. Current accounting profit before tax is GNF 260,000,000, with GNF 40,000,000 of supported add-backs, no loss/relief and no other credits. Current IS is GNF 75,000,000 and IMF GNF 40,000,000. Each gross instalment is GNF 30,000,000: IMF covers all of June and GNF 10,000,000 of September, leaving GNF 20,000,000 cash in September. April balance is GNF 15,000,000. Total IMF plus IS cash is GNF 75,000,000; the IMF is not deducted twice.

```oa-check
name: Ordinary company profit bridge and same-year IMF offsets
inputs:
  preceding_year_imf_turnover: 2000000000
  reference_year_is: 90000000
  accounting_profit_before_tax: 260000000
  nondeductible_addbacks: 40000000
steps:
  - taxable_profit: floor((accounting_profit_before_tax + nondeductible_addbacks) / 1000) * 1000
  - profit_is: taxable_profit * 0.25
  - imf: min(max(preceding_year_imf_turnover * 0.02, 20000000), 300000000)
  - gross_instalment: floor((reference_year_is / 3) / 1000) * 1000
  - june_imf_used: min(imf, gross_instalment)
  - june_cash: gross_instalment - june_imf_used
  - remaining_imf: imf - june_imf_used
  - september_imf_used: min(remaining_imf, gross_instalment)
  - september_cash: gross_instalment - september_imf_used
  - april_cash: max(profit_is - imf - june_cash - september_cash, 0)
  - total_cash: imf + june_cash + september_cash + april_cash
expected:
  taxable_profit: 300000000
  profit_is: 75000000
  imf: 40000000
  gross_instalment: 30000000
  june_cash: 0
  september_cash: 20000000
  april_cash: 15000000
  total_cash: 75000000
```

For the decision case, keep the same preceding turnover and reference-year IS, but current positive pre-loss profit is GNF 100,000,000 with validated ordinary losses GNF 100,000,000. Only GNF 70,000,000 is used; GNF 30,000,000 profit remains and IS is GNF 7,500,000. IMF GNF 40,000,000 remains the definitive minimum. Cash instalments total GNF 20,000,000 and become the separate future IS/IMF credit under the stated guidance; unused IMF GNF 32,500,000 is not a refundable/carry-forward credit. Do not claim a credit of gross instalments minus profit IS, which would wrongly recover the IMF. This assumes all referenced source versions govern and no special relief applies.

```oa-check
name: Loss cap and distinct IMF versus cash instalment credits
inputs:
  preceding_year_imf_turnover: 2000000000
  reference_year_is: 90000000
  positive_profit_before_losses: 100000000
  validated_ordinary_losses: 100000000
steps:
  - losses_used: min(validated_ordinary_losses, positive_profit_before_losses * 0.70)
  - losses_carried: validated_ordinary_losses - losses_used
  - taxable_profit: floor((positive_profit_before_losses - losses_used) / 1000) * 1000
  - profit_is: taxable_profit * 0.25
  - imf: min(max(preceding_year_imf_turnover * 0.02, 20000000), 300000000)
  - gross_instalment: floor((reference_year_is / 3) / 1000) * 1000
  - june_imf_used: min(imf, gross_instalment)
  - september_imf_used: min(imf - june_imf_used, gross_instalment)
  - cash_instalments: gross_instalment * 2 - june_imf_used - september_imf_used
  - definitive_tax_floor: max(imf, profit_is)
  - unused_imf_not_transferable: max(imf - profit_is, 0)
  - transferable_cash_credit: max(imf + cash_instalments - definitive_tax_floor, 0)
expected:
  losses_used: 70000000
  losses_carried: 30000000
  taxable_profit: 30000000
  profit_is: 7500000
  imf: 40000000
  cash_instalments: 20000000
  definitive_tax_floor: 40000000
  unused_imf_not_transferable: 32500000
  transferable_cash_credit: 20000000
```

## Ask the client first

- What entity, residence, effective management, activity, tax service and IS/TPU/VAT-option evidence apply?
- What proves the operative source versions and any exemption, investment/CGA approval or special mining/stability terms?
- What current accounts, prior-year IMF turnover reconciliation and reference-year IS assessment support the calculation?
- What loss history, depreciation/provision schedules, disputed expenses and related-party/foreign transactions need separate treatment?
- What IMF payments, gross instalments, actual cash, foreign certificates and separately carried credits have already been used?
- What filing acknowledgements, payment receipts, notices and deadlines remain open?

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [DGI enacted CGI base, L/2021/032/AN](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf), corporate arts. 219-246 and relevant neighbours; profit arts. 91-110, recipient withholding arts. 186 bis-190/198, scope arts. 275-276/360 and interest art. 1170-1171. Read for the stated rules; no claim that this historical publication is a complete current consolidation. | 2026-11-01 |
| [LFI 2023](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2023.pdf), arts. 7-8, prior IMF and instalment amendments with neighbours; [LFI 2024](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf), art. 8 replacing IMF and related tax-chapter context. | 2026-11-01 |
| [LFI 2025](https://dgb.gov.gn/wp-content/uploads/2025/02/Loi-de-Finances-Initiale-2025.pdf), art. 26 electronic annual declaration with adjacent tax clauses, read against the scan. | 2026-11-01 |
| [DGI Précis fiscal 2026, 10 April version](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx), §1.2 ordinary scope, base/charges, rate/IMF, payments and annual declaration; §1.6 and VAT-option scope cross-check; cover/introduction identify current administrative doctrine. Typographical dates and incorrect interest-article cross-reference are not treated as law. | 2026-11-01 |

Not yet confirmed: final October 2026 rectifying-law promulgation/wording/effect and operative applicability of all source versions; complete TPU computation and regime-boundary administration; specialised asset depreciation, reinvestment/merger/share-transfer gains, participation relief, donations and finance/related-party deduction methods; current official central-bank rate; investment/CGA/mining/stability approvals; complete withholding filing/gross-up, treaty relief, branch allocations, foreign-credit computation and TP documentation/formats; all current penalty/appeal procedures and authenticated e-Tax fields/receipts. The ordinary methods above are substantive but the full corporate domain remains partial.

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
