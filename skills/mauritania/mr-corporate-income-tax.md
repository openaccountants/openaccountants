---
name: mr-corporate-income-tax
description: "Prepare a source-based Mauritania research file for ordinary company profit and minimum-tax computation in the 2026 country pack. Use this Guide to identify the taxpayer, classify the transaction, assemble the relevant documents and compare the cited statutory baseline with later amendments. It covers the stated ordinary cases, computation conditions, filing obligations and worked decisions, with official source links and explicit limits. Trigger phrases include Mauritania tax, DGI, taxpayer registration, taxable base, payment deadline and compliance evidence. This is a partial research draft: the complete operative amendment chain and current submission procedures are not established, and no licensed accountant has attested this revision."
jurisdiction: MR
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.1
tax_year_notes: "2026 research draft; cited historical baseline and selected later replacements; operative amendment chain incomplete"
---

# Mauritania Corporate Income Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research draft, source baseline only.** The computations below reproduce the cited official code/provisions, not a certified complete statement of operative 2026 law. The January 2023 official code lists amendments only through the January 2022 Finance Act. Selected later Finance Acts were read, including the 2024 transfer-pricing replacement, but the complete commencement/publication chain is not closed. The Ministry’s August 2026 rectifying publication changes material expense, digital-service and compliance rules; its upload date does not prove their operative date. Resolve the amendment file before using these baselines to file, pay or advise. No accountant has signed this revision.

## Who this applies to

Ordinary Mauritanian companies in normal or intermediate IS regimes. Select the legal person and regime first; fisheries, transport, margin businesses and special investment/mining/petroleum regimes require their own rules. Cross-border withholding belongs in [the cross-border Guide](mr-cross-border.md).

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| Normal regime [C03] | Annual turnover excluding tax above MRU 5,000,000 brings the normal real regime. Prorate the limit for a start or cessation during the year; a fall below the limit needs two consecutive years before moving down. | [CGI art. 44](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |
| Intermediate regime [C04] | A company at or below MRU 5,000,000 annual turnover excluding tax uses the intermediate real regime, subject to the normal-regime transition rule. Crossing above moves it to normal the following year. | [CGI art. 46](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |
| Normal IS calculation [C05] | For an ordinary normal-regime company, compare 25% of taxable net profit, 2% of taxable products under art. 8 excluding transfers and reversals of charges, and the MRU 100,000 minimum. Pay the greatest before credits. This is not a universal 2.5% turnover formula. | [CGI art. 51(1)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |
| Intermediate IS calculation [C06] | Compare 25% of taxable net profit with 2.5% of taxable products under art. 8 excluding transfers and reversals of charges. Do not import the normal-regime fixed minimum into this paragraph. Special art. 225 margin businesses need their separate base. | [CGI art. 51(2)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |

## The base

- **Tax and legal persons [C01].** IS replaces IBIC and IMF. Capital companies, including a single-member SARL, fall within IS; classify other entities under arts. 2–4 before computing. [CGI arts. 1–4](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Territorial business profits [C02].** Use profits of enterprises operated in Mauritania and profits allocated by a double-tax agreement. Residence means registered office or effective management in Mauritania; nonresident enterprises with a local permanent establishment are included. [CGI art. 5](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Accounting bridge and rounding [C07].** Start with the net result of all operations, including disposals, and reconcile net assets, contributions and withdrawals under art. 7. Round taxable net profit or taxable products down to the nearest MRU 10. Art. 8 products use the accrued-right principle. [CGI arts. 7–9](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Ordinary deductible expenses [C08].** Expenses must serve the business, be real, documented with a regular invoice or import declaration bearing the supplier NIF, be booked as expenses, reduce net assets, not create exempt income and belong to the period. The later 2026 replacement of art. 14 needs its commencement resolved before this baseline can support a filing. [CGI art. 14(1)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Cash-payment exclusion [C09].** An expense paid in cash to another business is not deductible where its unit amount exceeds MRU 200,000; the limit is MRU 50,000 for fishery-product exporting and processing businesses. Do not split a payment to assume deductibility. [CGI art. 14(3)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Accounting year [C10].** Close accounts at 31 December. A new enterprise can close its first balance sheet at the following year-end, but must prepare a provisional operating account at the first 31 December, tax it immediately and deduct that tax from the first balance-sheet assessment. [CGI art. 50(3)–(5)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Withholding credits [C13].** IRCM and IRF withheld on income included in business profits are creditable against IS; unused credits carry forward. Credits relating to an IS exemption are definitively retained by the Treasury. Keep certificates and match income before claiming. [CGI arts. 53–54](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Privileged-tax jurisdictions [C14].** Deducted payments to a recipient in a privileged-tax jurisdiction must be added back unless the enterprise proves a real transaction and an amount that is neither abnormal nor excessive. The comparison is tax payable less than half the ordinary Mauritanian equivalent, not a country-name blacklist. [CGI art. 23](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).

## Deadlines and filing

- **Return and payment calendar [C11].** Declare the previous 31 December result by 31 March. For ordinary normal/intermediate IS, pay 40% by 31 March, 30% by 30 June and the balance by 30 September of the following year, using the prescribed return and financial statements. [CGI arts. 58(1), 59(1)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Return attachments [C12].** Normal-regime attachments include prescribed annual financial statements and annexes, annual salary declaration, third-party fee declaration, partner/distribution declaration, depreciation/provision table and detailed rent schedule. Intermediate companies attach simplified prescribed financial statements and annexes. Both provide constitutional amendments where relevant and statutory-body minutes within seven months of closing. [CGI arts. 61(1)–(2), 62](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).

**Return preparation, not a confirmed live portal submission.** DGI’s actual corporate form IMPRIME n°20213611 asks for regime, A identification, B base, C comparison, D credits and E instalments. Reconcile C1 profit × 25%, C2 products × the selected regime rate, C3 minimum and C4 greatest amount; D7 subtracts D1–D6 credits, D8 records carryforward, E1–E3 allocate payment. Read the form’s transport/fisheries exclusions. Retain the service’s receipt/quittance. The live 2026 online mandate and confirmation screens remain a hold. [Official form](https://impots.gov.mr/DGI/files/IS-RN-RI-fr-pdf.pdf). [C17]

## Penalties and interest

- **Annual filing sanctions [C15].** The baseline LPF L.131(3) imposes 1% of tax-inclusive turnover for a missing/late annual return or mandatory document, with ordinary minimums MRU 50,000 normal and MRU 35,000 intermediate, and separate exempt/convention-company minimums MRU 150,000 and MRU 75,000. Confirm which failure is assessed; do not silently substitute a generic late-payment percentage. [LPF art. L.131(3)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Recovery penalty trigger [C16].** For a spontaneous-payment tax covered by a recovery notice, L.136(1) gives a 10% principal surcharge, counted from the fourth day after notification of that notice. It is not a daily interest rate or an automatic charge starting on the ordinary return due date. [LPF art. L.136(1)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).

## Cross-border points

For associated-party adjustments and reporting, use [transfer pricing](mr-transfer-pricing.md). For withholding and PE questions use [cross-border](mr-cross-border.md). Those obligations are distinct from the company profit computation.

## Two worked examples that recompute

### 1. Normal IS baseline: profit beats products and minimum

Assume the ordinary normal baseline applies, profit MRU 1,200,000 and eligible products MRU 8,000,000 with no credits. Compare 300,000, 160,000 and 100,000: MRU 300,000. Baseline instalments are 120,000, 90,000 and 90,000.

```oa-check
name: Normal IS baseline: profit beats products and minimum
inputs:
  profit: 1200000
  products: 8000000
steps:
  - profit_tax: profit * 0.25
  - products_tax: products * 0.02
  - tax: max(profit_tax, products_tax, 100000)
  - first: tax * 0.4
  - second: tax * 0.3
  - balance: tax - first - second
expected:
  tax: 300000
  first: 120000
  second: 90000
  balance: 90000
```

### 2. Choose the statutory limb, not the lower apparent rate

Assume the normal baseline applies: eligible products MRU 8m, taxable profit MRU 200,000. Profit limb is 50,000; products limb is 160,000, above the 100,000 floor. Choose 160,000. If profit were 800,000 with the same products, choose profit tax 200,000 instead.

```oa-check
name: Choose the statutory limb, not the lower apparent rate
inputs:
  products: 8000000
  low_profit: 200000
  high_profit: 800000
steps:
  - products_tax: products * 0.02
  - low_tax: max(low_profit * 0.25, products_tax, 100000)
  - high_tax: max(high_profit * 0.25, products_tax, 100000)
expected:
  low_tax: 160000
  high_tax: 200000
```

## Ask the client first

- Legal form, registered office, effective management and any PE?
- Turnover/product reconciliation, ordinary or special sector, and regime history?
- Accounting profit bridge, cash payments, supplier NIFs and supporting documents?
- Withholding certificates, instalments and carried credits?
- Which enacted amendments and commencement dates govern this period?

## Sources

| Source and exact scope read | URL | Read on |
|---|---|---|
| cgi2023: Official version cover/amendment list and selected CGI arts. 1–14, 23–24, 40–46, 49–67, 68–98, 99–118, 119–137, 150–157, 209–215 (exemption list introductory categories only), 216–221, 227–250, 253–254, LPF L.131–L.139. Not the entire 168-page code or full sector/special regimes. | https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf | 2026-11-01 |
| is-form: Full one-page DGI corporate form including regime and C/D/E calculation/payment sections; not a live online filing. | https://impots.gov.mr/DGI/files/IS-RN-RI-fr-pdf.pdf | 2026-11-01 |
| Amendment hold: August 2026 comparison text, art. 3.1 printed pp. 6–18; operative date not established | https://www.finances.gov.mr/sites/default/files/2026-08/LFR%202026%20FR.pdf | 2026-11-01 |

Not yet confirmed: full operative 2026 amendment chain, including any 2022/2023 changes not established here and August 2026 commencement; current DGI electronic filing mandate, screens, submission confirmation and payment-reference procedure; special fisheries, transport and art. 225 margin computations; detailed depreciation, losses and incentives; all old nonresident royalty claims must be classified under actual service/capital provisions before a rate is selected.

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
