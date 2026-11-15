---
name: mongolia-vat
description: "Source-cited draft: Prepare and review Mongolia VAT classifications and monthly returns for 2026. Load vat-workflow-base v0.1 or later alongside this skill. Not reviewed by an accountant."
version: 2.1
jurisdiction: MN
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Mongolia VAT

## Scope

Prepare, review and classify ordinary Mongolia VAT transactions and the monthly return for 2026. Load **vat-workflow-base v0.1 or later** alongside this skill. Confirm registration, transaction facts and documents before classification. Mining/natural-resource special regimes and free-trade-zone entities are referred below.

**Quick reference:** the standard rate is 10%; qualifying exports can be zero-rated, but exempt exports are different. The return/payment deadline is the 10th of the following month. The official e-tax portal is [ETAX.MTA.MN](https://etax.mta.mn), linked in the MTA manual. The local currency is MNT (Mongolian Tugrik). [VAT Law arts. 11-16](https://legalinfo.mn/mn/detail?lawId=11227); [MTA manual, printed pp. 13-17](https://mta.gov.mn/files/pdf/pqw1d68akoi//6576bcd3bc0423573f2e6bd6.pdf); [Accounting Act art. 7](https://legalinfo.mn/mn/detail?lawId=11191).

### Rates and registration

| 2026 rule and conditions | Rate, amount or period | Official source |
| --- | --- | --- |
| Ordinary taxable domestic supplies and imports, unless a specific exemption/zero rate applies | 10% | VAT art. 11.1 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Qualifying exports with customs/contract evidence and within the statutory categories; not an exempt export | 0% | VAT art. 12, especially 12.2-12.4 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Compulsory registration, taxable operational sales reaching the threshold; excludes fixed-asset disposals from this test | MNT 50,000,000 for 2026; the larger enacted threshold begins in 2027 | VAT arts. 4.1.8, 5.2-5.5 and future-change notes [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Eligible voluntary registration | At least 20% of that threshold, MNT 10,000,000 derived, for 2026 | VAT art. 6.5 and future-change note [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Application after reaching the threshold | Within 10 working days | VAT art. 6.1 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Registration after receiving the application | Within 3 working days (in words on the page); taxable treatment starts from certificate issuance as specified in art. 10.1 | VAT arts. 6.2, 10.1 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Monthly return and payment | By the 10th of the following month | VAT art. 16.1 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Statutory consumer receipt transmission | Within 3 days (in words on the page); issue the receipt on each sale | VAT arts. 17.3.1-17.3.3 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| VAT invoice records between withholding taxpayers | Send to the integrated system within 7 days | VAT art. 17.3.4 [law](https://legalinfo.mn/mn/detail?lawId=11227) |

Exclusively exempt activity has its statutory registration exclusion; do not register solely from exempt receipts without testing art. 6.3. The threshold is not a safe harbour against every VAT obligation: the ordinary registration condition does not apply to the art. 7.2.5 non-resident-to-resident transactions covered by art. 7.4. Petrol/diesel and special sectors require their specific statutory rules, not the headline rate. [VAT arts. 6.3, 7.2.5, 7.4, 11.3-11.4](https://legalinfo.mn/mn/detail?lawId=11227).

## Ask the client first

Obtain the MTA TIN, certificate and effective date, filing month, business activity and VAT status; ask whether the business exports and obtain its export documents. Obtain opening credit, prior returns, sales and purchase ledgers, VAT invoices with counterparty TINs, E-barimt records/corrections, customs import/export documents and foreign-service contracts/invoices. Identify mixed/private use and asset purchases.

A bank statement is the minimum **starting intake**, from Khan Bank, Golomt Bank, TDB (Trade and Development Bank), XacBank, State Bank or another bank. It is not sufficient evidence to file the return or claim credit. Retain source invoices and investigate cash withdrawals, unclear transfers and foreign counterparties. For foreign currency, establish the statutory Bank of Mongolia exchange rate at the art. 10.2 tax point; the transaction date/rate must be evidenced (art. 9.3). Cyrillic descriptions and transliterated equivalents are matching aids, not tax conclusions.

## The method, step by step

1. **Confirm registration and period.** Reconcile the certificate's effective date, taxable sales, fixed-asset disposals and any exemption. Do not apply a future threshold to 2026.
2. **Set the tax point and base.** Under art. 10.2 use the earliest applicable payment, invoice or purchase-receipt event; utilities have their specific invoice/payment rule and imports use the customs event. Imported goods' base includes customs value, customs duty, excise and other applicable taxes under art. 9.1, not merely an unexplained CIF-plus-duty amount. Avoid duplicate VAT already accounted for at customs.
3. **Classify output.** Apply the standard rate only once taxable domestic treatment is established. For exports verify the statutory category, customs evidence and non-resident contract where required. Domestic legs of international transport and property-related services are not automatically zero-rated (arts. 12.2-12.4). Raw, washed or combed cashmere and the specified hides/skins exported under art. 13.1.21 are exempt, not zero-rated.
4. **Classify purchases and non-resident payments.** Separate ordinary eligible domestic/import input VAT from the purchaser-withheld VAT on taxable non-resident supplies under art. 16.1.2. Establish supplier residence, actual supply, place/source, contract and statutory taxable value; do not infer liability or a gross-up from a brand or bank debit. The MTA manual expressly puts VAT withheld from a non-resident among non-deductible items (printed p. 14); do not post an automatic equal input credit.
5. **Validate input credit.** Arts. 14.1, 14.4-14.5 require the eligible business purpose, paid VAT and proper supporting VAT invoice/customs evidence. The application-to-certificate interval has its specified rule. Private/staff use, exempt activity and unrelated/pre-operating acquisitions fall within art. 14.6 restrictions. Passenger cars and their parts have the art. 14.7 restriction and licensed-reseller exception. Apportion taxable/exempt mixed use under art. 14.9. Asset credits may have statutory spreading, so do not treat every asset invoice as an immediate full deduction.
6. **Reconcile receipts and working paper.** Match bank movements to invoices, E-barimt and customs; resolve returns, cancellations, missing receipts, duplicated invoices and credit brought forward. Under art. 17 register payment information, issue receipts on sales, and send consumer receipts/VAT invoice data within the sourced periods above. The MTA manual's printed p. 17 describes checking purchase/sale data and bringing import/export information into the return; do not silently force an auto-populated total.
7. **Prepare the monthly return.** In the authenticated taxpayer's e-tax account choose the period and applicable VAT return. The MTA manual refers to TT-03A, with rows 5-6 populated from system records, and describes saving, refreshing/rechecking, saving again and sending. Reconcile displayed fields to the records before authorised submission; preserve the acknowledgment, return and payment evidence. Current live screen labels/box mapping are not fully confirmed here.
8. **Settle and retain.** Reconcile output, non-resident withholding, allowed domestic/import inputs and carried credits to the return and pay by the statutory date. Excess credit is subject to art. 14.8 and the art. 15 carry-forward/offset/refund procedure; a refund is not automatic. Keep any requested refund and its evidence separate from a casual negative balance.

[VAT arts. 6-17](https://legalinfo.mn/mn/detail?lawId=11227); [MTA manual, printed pp. 13-14 and 17](https://mta.gov.mn/files/pdf/pqw1d68akoi//6576bcd3bc0423573f2e6bd6.pdf).

### Supplier pattern library and statement treatment

These patterns preserve the intake library. Every result is conditional on the actual transaction and evidence; a brand never proves an exemption, supplier residence or input entitlement.

| Patterns | Classification to investigate | Conditions/source |
| --- | --- | --- |
| KHAN BANK, XAAH BAHK; GOLOMT, GOLOMT BANK; TDB, TRADE AND DEVELOPMENT; XACBANK, STATE BANK | Exclude qualifying exempt bank charges from input VAT | Check the particular financial service under VAT art. 13.5; not every purchase from a bank is exempt [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| INTEREST, LOAN, REPAYMENT | Separate interest/qualifying financial service from loan principal | Principal is not a purchase of taxable goods/services; inspect art. 13.5 financial category [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| MTA, TAX AUTHORITY; CUSTOMS, MONGOLIAN CUSTOMS; SOCIAL INSURANCE, NDSH | Reconcile tax, duty and social payments; do not claim their bank-payment amount as input VAT | Import VAT may instead be supported by customs documents under arts. 14.1, 16.2; classify each customs component [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| UBEDN, CENTRAL ELECTRICITY; USUG, WATER SUPPLY; MOBICOM, UNITEL, SKYTEL | Ordinary taxable electricity, water or telecom supply: 10% where no specific exemption applies | Verify invoice, VAT and business use; arts. 7.2.6, 11.1, 14 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| GOOGLE, MICROSOFT, META, AWS; ZOOM, SLACK, CANVA | Investigate taxable non-resident services; 10% purchaser withholding where the statutory conditions apply | Arts. 7.2.5, 7.4, 11.1, 16.1.2 [law](https://legalinfo.mn/mn/detail?lawId=11227); no automatic input offset, [MTA manual p. 14](https://mta.gov.mn/files/pdf/pqw1d68akoi//6576bcd3bc0423573f2e6bd6.pdf) |
| SALARY, WAGES | Exclude employment remuneration from VAT purchases | Do not confuse a contractor's actual supply with employment; check the art. 7 supply definition [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| OWN TRANSFER, INTERNAL | Exclude a genuine movement of own money from sales/purchases | Evidence both accounts; any underlying supply is classified separately under art. 7 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| CASH WITHDRAWAL | Exclude the withdrawal itself and investigate what it paid for | Default exclusion is an evidence hold, not a denial of every later supported purchase; art. 14 evidence rules [law](https://legalinfo.mn/mn/detail?lawId=11227) |

### Conservative defaults and working-paper fields

The old “unknown rate = 10%” and “unknown location = domestic Mongolia” defaults cannot decide law. Hold unclassified sales and unknown counterparty location until facts establish treatment. Use the standard rate only for an established taxable supply; mark every unresolved line for follow-up before filing. Unknown purchase VAT status or business-use proportion means **no input credit claimed pending evidence** (effectively 0% recovery in the draft), not a permanent legal disallowance. [VAT arts. 7, 11-14](https://legalinfo.mn/mn/detail?lawId=11227).

Use the vat-workflow-base Section 3 Excel working paper with separate columns for Output 10%, Zero-rated, Exempt, Input domestic, Input imports, **non-resident VAT withheld with no automatic input credit**, credit brought forward and Net VAT. Preserve the original bank date, counterparty, gross amount, invoice/customs reference, net base, VAT, field, evidence/default flag and exclusion reason. Khan Bank/Golomt CSV exports and other bank formats need reconciliation, not automatic trust in a description.

## Boundary and exception table

| Situation | Treatment or required hold | Source |
| --- | --- | --- |
| Financial services | Exempt only for specified services; verify fee character | VAT art. 13.5 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Residential rent | Verify actual residential use and statutory rental category; commercial premises are not covered by this label | VAT art. 13.5 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Healthcare | Covered health services can be exempt; medicines/equipment are not included merely because a provider is medical | VAT arts. 13.5, 13.7 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Education | Verify authorised/licensed activity and charter scope | VAT art. 13.5 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Public transport | Use the specified statutory public-transport category; do not assume every taxi/transport service is exempt | VAT art. 13.5.13 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Raw, washed or combed cashmere export | Exempt, no related exempt-output input credit; finished-product exports require a separate classification | VAT arts. 13.1.21, 14.6.3 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Vehicle costs | Default hold/no recovery until passenger/commercial status, use and the reseller exception are evidenced | VAT arts. 14.6-14.7 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| Entertainment | Default hold on input credit pending business purpose and evidence; do not invent an across-the-board category rule | VAT arts. 14.4-14.6 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| SaaS entities | Investigate recipient-withholding treatment; never assume an equal input credit | VAT art. 16.1.2 [law](https://legalinfo.mn/mn/detail?lawId=11227); [MTA manual p. 14](https://mta.gov.mn/files/pdf/pqw1d68akoi//6576bcd3bc0423573f2e6bd6.pdf) |
| Cash withdrawals | Exclude cash movement itself; obtain purchase evidence before input credit | VAT art. 14 [law](https://legalinfo.mn/mn/detail?lawId=11227) |
| E-barimt compliance | Ask whether all required sales/receipts are registered and sent; reconcile rather than filing through a known mismatch | VAT art. 17 [law](https://legalinfo.mn/mn/detail?lawId=11227) |

## Worked cases

The historical case dates, counterparties and transaction lines are retained. Computations assume the additional facts stated; bank text alone does not establish those facts.

### Case 1: standard domestic sale

**Input line:** `05.04.2026 ; MONGOLIAN TRADING LLC ; CREDIT ; Invoice MN-041 ; MNT 11,000,000`

Assume a registered seller, ordinary taxable domestic sale, and VAT-inclusive consideration. MNT 11,000,000 / 1.10 = **MNT 10,000,000 net**; output VAT is **MNT 1,000,000**, derived. Post Output, no default/exclusion, with the invoice and E-barimt record.

```oa-check
name: Historical domestic sale with VAT-inclusive price
inputs:
  gross: 11000000
  rate: 10
steps:
  - net: gross / (1 + rate / 100)
  - output_vat: gross - net
expected:
  net: 10000000
  output_vat: 1000000
```

### Case 2: cashmere export classification matters

**Input line:** `15.04.2026 ; CHINESE BUYER CO ; CREDIT ; Cashmere export ; MNT 80,000,000`

If the evidence confirms **raw, washed or combed cashmere** within art. 13.1.21, MNT 80,000,000 is **exempt** turnover, output VAT **MNT 0**, with no related exempt-output input credit. The old zero-rated label is corrected. A finished cashmere product could instead meet art. 12 export zero-rating conditions; obtain product/customs details before choosing. No amount alone proves classification.

### Case 3: non-resident digital service, no automatic input credit

**Input line:** `18.04.2026 ; GOOGLE ; DEBIT ; Google Workspace ; MNT -500,000`

Assume documents establish a covered non-resident service and a statutory VAT-exclusive taxable base of MNT 500,000. Purchaser-withheld VAT is **MNT 50,000** at 10%; input credit for that withheld VAT is **MNT 0** under the cited MTA instruction. The old “Output + Input” posting is corrected. The bank debit alone does not establish the pre-VAT base or contractual gross-up.

```oa-check
name: Historical non-resident service without automatic input credit
inputs:
  confirmed_exclusive_base: 500000
  rate: 10
  allowed_input: 0
steps:
  - withheld_vat: confirmed_exclusive_base * rate / 100
  - net_vat: withheld_vat - allowed_input
expected:
  withheld_vat: 50000
  net_vat: 50000
```

### Case 4: qualifying bank service fee

**Input line:** `30.04.2026 ; KHAN BANK ; DEBIT ; Service fee ; MNT -15,000`

Assume the invoice establishes a financial service within art. 13.5. Record **MNT 15,000** as the exempt charge, no input VAT. Exclude it from VAT credit; retain it in the accounting reconciliation. If the fee is for another taxable supply, reopen classification rather than applying the bank-name pattern.

## When to refuse or refer

- **R-MN-1: Mining and natural resources.** Trigger: client in mining with a special regime. Message: “Mining sector has bespoke VAT and royalty rules. Please escalate.” Keep the transaction pending and obtain the applicable product/licence/regime analysis.
- **R-MN-2: Free trade zone entity.** Trigger: client in Altanbulag or Zamiin-Uud FTZ. Message: “Free trade zone entities have special VAT treatment. Please escalate.” Do not reuse domestic defaults.
- Refer unsupported exemptions, mixed-use asset allocations, uncertain non-resident contracts, missing customs evidence, disputed credit and unresolved E-barimt mismatches before filing. No estimate/default flag is permission to file a known unclassified line.

## Filing and payment

File and pay monthly by the sourced deadline above; reconcile customs import VAT separately. The authority's manual identifies ETAX.MTA.MN and the TT-03A workflow, including checking receipts/corrections and importing customs records. Its printed page 17 describes the save/refresh/save/send sequence. Use the actual authorised account's current form, review its populated rows against the working paper, submit only the reviewed result and retain confirmation and the tax payment reference. This skill does not claim a fully mapped live E-barimt integration or current box-by-box portal layout.

VAT late-payment interest follows the year's separately determined rate under [General Tax Law art. 73](https://legalinfo.mn/mn/detail?lawId=14403). Obtain the notice, due date, actual payment date and applicable decision before calculating; no unsourced penalty rate is supplied.

## Completion checklist

- TIN, registration effective date, month, activity, exports and credit brought forward confirmed.
- Bank/ledger/invoice/customs/E-barimt totals reconciled; internal transfers, cash movements and tax payments explained.
- Ordinary taxable, zero-rated and exempt sales separated; export cashmere product identified.
- Eligible domestic/import inputs evidenced, mixed/private and blocked items held or excluded; non-resident withholding not automatically credited.
- Mining/FTZ refusals resolved through the correct review; all unresolved lines cleared before filing.
- Return reviewed, acknowledgment and payment evidence retained; carry-forward/refund handled under the statutory procedure.

## Sources

| Official source | Read for | Read date |
| --- | --- | --- |
| [VAT Law, consolidated Mongolian](https://legalinfo.mn/mn/detail?lawId=11227) | Read for arts. 4-12, relevant exemption categories in art. 13, art. 14 credit rules, arts. 15-17 filing/refund/system rules; future threshold amendment separated from 2026 | 2026-11-15 |
| [MTA practical VAT manual](https://mta.gov.mn/files/pdf/pqw1d68akoi//6576bcd3bc0423573f2e6bd6.pdf) | Read for printed pp. 13-14 and 17: credit/non-credit categories, explicit non-resident VAT credit block and e-tax return workflow; printed p. 14 visually rendered. Undated manual corroborated against operative law | 2026-11-15 |
| [Accounting Act](https://legalinfo.mn/mn/detail?lawId=11191) | Read for art. 7 national currency/reporting context | 2026-11-15 |
| [General Tax Law](https://legalinfo.mn/mn/detail?lawId=14403) | Read for art. 73 late-payment interest framework | 2026-11-15 |

**Not yet confirmed:** current live TT-03A box mapping and E-barimt integration/API/upload specifications; the applicable annual arrears-interest decision; particular mining/FTZ regimes (refused); uncertain product, place-of-supply or exemption facts must be resolved from their specific official rules. The old e-tax.mta.mn spelling is replaced with the portal printed in the MTA manual; the public portal responds as the electronic tax system, but authenticated fields were not inspected.

### Change log

- v2.0 (April 2026): historical ten-section rewrite.
- v2.1 (15 November 2026): source-read 2026 revision; corrected cashmere export, foreign-service input credit, import base and unsafe statement defaults; retained historical cases and supplier/refusal coverage.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
