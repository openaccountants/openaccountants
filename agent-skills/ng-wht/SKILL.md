---
name: ng-wht
description: "Classify and compute Nigerian deduction-at-source obligations for 2026 under NTAA section 51 and the preserved 2024 Withholding Regulations. Covers corporate/non-corporate resident and non-resident columns, payment timing, exemptions, missing TIN, credit receipts, treaty limits, remittance and penalties. PAYE and VAT withholding are separate workflows. Retains the original services, UK royalty and dividend cases with corrected law."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ng-wht"
  jurisdiction: "NG"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Nigeria withholding tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Outgoing payments by a Nigerian business or collecting agent, and the corresponding recipient receipt/credit. The Deduction of Tax at Source (Withholding) Regulations 2024, S.I.34, effective from 1 January 2025, revoked the earlier withholding regulations. The old 1997 matrix is therefore not the 2025 baseline either. For 2026, NTAA section 51 expressly applies deduction regulations; NTA section 198 preserves subsidiary legislation unless inconsistent. This is income-tax withholding, separate from employer PAYE ([ng-payroll](ng-payroll.md)) and VAT withholding ([nigeria-vat](nigeria-vat.md)). [Regulations 11 and 12](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf); [NTAA section 51](https://nass.gov.ng/documents/download/11250); [NTA section 198](https://nass.gov.ng/documents/download/11249).

## Ask the client first

Use the intake and existing contracts first. Obtain payer identity/entity/Tax ID and collecting-agent capacity; recipient name, company versus non-corporate status, residence, Tax ID or alternative identifier; actual service/goods/rights supplied; gross income consideration, separately stated VAT and expense breakdown; payment, set-off and related-party accrual dates; invoice and settlement currency; small-payer evidence and calendar-month transaction totals; treaty residence/beneficial ownership and PE facts; receipts for tax already deducted. A payer's residence does not by itself decide where a recipient's WHT goes.

## The method, step by step

### 1. Decide whether the payer must deduct [Regulation 4](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf)

Regulation 4 lists corporate/unincorporated bodies other than an individual, government MDAs, statutory bodies, public authorities, other institutions/organisations/establishments/enterprises including tax-exempt ones, and their payment agents. Do not assert every private consumer must withhold. A sole trader's business capacity may need the applicable authority's determination; do not infer it merely from an invoice.

The small-payer exception requires the specified small company or unincorporated body of equivalent attributes, a supplier with valid TIN, AND a transaction value no more than NGN 2,000,000 during the relevant calendar month. It is not a blanket exemption for all payments made to a small supplier. The regulation refers to CITA section 105; how the repealed definition maps to a 2026 borderline payer needs the applicable interpretation. Hold that exemption if classification is unresolved. Do not divide a monthly commercial arrangement into smaller invoices to assume it qualifies. [Regulation 4(2)](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf).

### 2. Test the express transaction exceptions [Regulations 10 and 13](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf)

Exempt from deduction: the specified securities-lending compensating payments; qualifying REIT/REIC distributions; across-the-counter transactions; direct-debit interest/fees to a Nigerian bank from funds domiciled there; goods manufactured or materials produced by the supplier; imports that create no Nigerian taxable presence for the foreign supplier; income/profits exempt from income tax; telephone charges, internet data and airline tickets; normally supplier-incurred out-of-pocket expenses distinguishable from contract fees; insurance premium; LPG, CNG, PMS, AGO, LPFO, DPK and JET-A1; a broker's industry-normal commission retained from principal collections; and the specified entrepreneurship/academic/technology/science game or reality-show winnings. Income-tax liability itself is not removed merely because deduction is exempt.

Across-the-counter means no established contractual relationship or prior formal arrangement, with instant cash or on-the-spot electronic payment. Manufacturing includes energy production, electricity, gas and petroleum products. Do not call all ordinary-course goods sales exempt: a reseller supplying under a contract can fall in the goods row. For reimbursements, test the actual regulation's distinguishability requirement rather than the old blanket rule that every invoice must be in the payer's name. Hold a bundled or unsubstantiated claim pending the underlying documents.

### 3. Select all four rate columns [First Schedule, pages B763 and B764](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf)

Percentages below are the statutory scheduled rates before an applicable treaty reduction, specific NTAA override, exemption or non-passive missing-TIN doubling. N/A is not a zero rate or a general exemption.

| Payment | Corporate resident | Corporate non-resident | Non-corporate resident | Non-corporate non-resident | Source |
| --- | --- | --- | --- | --- | --- |
| Dividend; interest | 10% | 10% | 10% | 10% | [First Schedule](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf) |
| Royalty | 10% | 10% | 5% | 5% | same |
| Rent, hire or lease | 10% | 10% | 10% | 10% | same |
| Commission, consultancy, technical, management and professional fees | 5% | 10% | 5% | 10% | same |
| Goods/materials supplied other than by their manufacturer/producer | 2% | N/A | 2% | N/A | same |
| Co-location and telecommunications tower services | 2% | 5% | 2% | 5% | same |
| Other supply/rendering of services not specifically listed | 2% | 5% | 2% | 5% | same |
| Construction of roads, bridges, buildings and power plants | 2% | 5% | 2% | 5% | same |
| Other construction and related activities | 5% | 10% | 5% | 10% | same |
| Brokerage fee, subject to the retained-commission exemption | 5% | 10% | 5% | 10% | same |
| Directors' fees | N/A | N/A | 15% | 20% | [First Schedule page B764](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf) |
| Compensation for loss of employment, on the taxable part | N/A | N/A | 10% | 10% | same |
| Entertainers and sportspersons, Nigerian earnings | N/A | 15% | N/A | 15% | same |
| Lottery/gaming/reality-show winnings, subject to exemption | N/A | N/A | 5% | 15% | same |

For non-passive supply/services/other eligible transactions without a recipient TIN, regulation 3(c) doubles the scheduled rate. It does not double every passive-income deduction. A missing TIN also does not justify suppressing the recipient's receipt: regulation 8 permits a NIN for an individual or RC number for a company. [Regulations 3 and 8](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf).

NTAA section 51(8) overrides the ordinary service row for a non-resident company providing technical, consulting, professional or management services to a labelled startup: 5% and final. Verify the startup label and exact supply before applying. Compensation's exempt portion is determined in [ng-cgt](ng-cgt.md); the deduction is not the recipient's final personal-tax computation. [NTAA section 51](https://nass.gov.ng/documents/download/11250); [JRB PIT Guidelines paragraph 15](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf).

### 4. Establish the tax point and base [Regulations 5 and 6](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf)

Deduct at the earlier of payment or other settlement. Between related parties, the earlier of payment or recognition of liability applies. The old universal invoice/accrual-date rule is wrong. Document set-off and settlement evidence. Classify the income consideration and separately stated VAT; WHT reduces the supplier's income payment, whereas VAT is added to the supply and belongs to a different tax account. Do not net receipted WHT out of the recipient's gross income or add it as an extra contract price: regulation 5 makes it advance or final tax of the supplier. [LIRS FAQ, WHT versus VAT](https://lirs.gov.ng/faq).

Use the transaction currency. LIRS says the authority may allow CBN-rate conversion to naira; the old universal instruction to convert every payment at any recent CBN rate was unsupported. Record the authority's currency requirement and permission before converting. A worked exchange rate below is an assumed case input, not a current market quotation. [LIRS FAQ, currency of deduction/remittance](https://lirs.gov.ng/faq).

### 5. Check final-tax and treaty treatment [NTAA section 51; NTA sections 17 and 120](https://nass.gov.ng/documents/download/11250)

Non-resident deductions are final under regulation 6(3), except where a Nigerian taxable presence makes further tax due. NTAA section 51(2) states the final-tax treatment for its non-resident passive/director/entertainer/sport categories. A Nigerian company dividend after prescribed deduction is franked income; redistribution set-off has its own rule. Individual interest on short-term securities/corporate bonds after deduction is not charged again. Do not treat every resident interest, rent, royalty or service fee as final, or claim final tax again as an ordinary credit.

Regulation3(b) requires an eligible resident of a treaty country and a reduced rate in a duly ratified treaty/protocol. Confirm actual article, residence, beneficial ownership, PE/fixed-base connection and anti-abuse conditions. A TRC alone does not establish a universal 7.5% rate. The UK treaty royalty cap is 12.5% (printed in words/fraction), subject to its conditions, so it does not reduce the scheduled 10% corporate royalty rate. Do not increase the domestic rate to the treaty ceiling. Software licences and SaaS are classified by the contract rights and treaty, not automatically treated as royalty. [UK-Nigeria treaty Articles 7, 12 and 13](https://www.gov.uk/government/publications/nigeria-tax-treaties/1987-uk-nigeria-double-taxation-agreement-in-force).

### 6. Remit, return and issue the receipt [Regulations 7 and 8](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf)

Route corporate and non-resident recipients to NRS; resident individuals/business names to their relevant State/FCT authority, including federal special categories where NTAA section 3 applies. The recipient determines the route, not a simple company-payer versus individual-payer label. [NTAA section 3](https://nass.gov.ng/documents/download/11250); [LIRS WHT FAQ](https://lirs.gov.ng/faq).

| Calendar rule | Requirement and limitation | Source |
| --- | --- | --- |
| Federal remittance | By the 21st day of the following month | [Regulation7](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf) |
| State PAYE/CGT remittance | By the 10th day of the following month | same |
| Other State deductions | Regulation7 says by the 30th of the following month. JRB paragraph 14.2 says last day. NTAA section 107 separately imposes its non-remittance consequence from the 21st. These are not the same wording: arrange the payment by the 21st for 2026 pending resolution, retaining any earlier specific deadline. | [Regulation7](https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf); [NTAA section 107](https://nass.gov.ng/documents/download/11250); [JRB paragraph 14](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf) |

Submit the deduction return with payment evidence and the Second Schedule particulars: payee name/address, TIN/NIN/RC or equivalent, transaction nature, gross amount, deducted amount, and calendar month. The Third Schedule receipt adds payer details, serial/reference and remittance details. The recipient can submit the prescribed receipt to claim credit. If a receipt was issued before the payer remitted, regulation 8(3) still credits the recipient and pursues the payer for the unpaid tax. Do not require a TaxPro Max-generated note as the only possible statutory evidence.

Reconcile monthly deductions, payments and supplier receipts; separately reconcile the recipient's income/credit register to its annual PIT/CIT return. No additional annual WHT form is invented here; comply with any actually prescribed return. Refund/set-off follows [ng-cit](ng-cit.md) or [ng-personal-income-tax](ng-personal-income-tax.md), not an assumed indefinite credit or a 6-year certificate expiry.

### 7. Penalties and correction [NTAA sections 101, 105 and 107](https://nass.gov.ng/documents/download/11250)

Failure to deduct: 40% of the amount not deducted. Failure to remit: unpaid principal plus 10% per annum administrative penalty and interest at CBN MPR; section 107 adds conviction consequences. A required return's non-filing/inaccuracy falls under section 101, NGN 100,000 first month and NGN 50,000 for each continuing month. General late-payment interest/spreads and remission are separate under sections 65 and66. Do not import the old flat company/individual monthly WHT penalties, fixed 5-point interest spread or automatic expense disallowance. An error requires a documented correction to the authority and recipient; no guessed refund promise.

## Boundary and exception table

| Original refusal/topic | Current action |
| --- | --- |
| R-NG-WHT-1 PAYE; R-NG-WHT-2 VAT withholding | Load the owning skill; do not apply the income-WHT table to a VAT or ordinary payroll liability. |
| R-NG-WHT-3 share-disposal CGT withholding | Route ng-cgt. Do not impose an assumed flat 10% seller tax or buyer deduction on every share sale. |
| R-NG-WHT-4 upstream royalties/PSC/JV | Obtain the contract and specialist legal basis. The old generic 5%/10% PSC overlay is not verified and cannot override the current row without a source. |
| R-NG-WHT-5 missing treaty evidence | Do not grant a reduced rate; resolve classification and domestic treatment, rather than invent a treaty concession. |
| R-NG-WHT-6 ordinary goods | Test the actual manufacturer, import and across-the-counter exceptions; being an ordinary sale alone is insufficient. |
| R-NG-WHT-7 private ruling/concession | Inspect the operative letter and scope; no reliance on an unseen concession. |
| R-NG-WHT-8 transition/straddle | Apply the actual tax point and transition instrument; old invoice date alone does not establish which law applies. |
| R-NG-WHT-9 State/FCT disagreement | Preserve residence/category evidence and seek the proper authority's determination. |
| R-NG-WHT-10 reimbursements/intragroup costs | Obtain invoices and contracts; no automatic highest-rate classification. |
| Construction versus standalone architect/surveyor | The construction type and professional service are separate scheduled rows. Painting, plumbing and electrical work require their actual contract classification. |
| Mixed goods/services, residence unknown, software rights unclear | Split only where evidence supports the actual components; hold final classification rather than automatically choose the higher rate. |

## Worked cases

**Original case 1, ABC Nigeria Ltd and XYZ Consulting Ltd.** Resident company recipient, valid TIN, consultancy fee NGN 5,000,000 plus separately stated VAT NGN 375,000, invoice NGN 5,375,000. Income-WHT at 5% is NGN 250,000, cash including VAT NGN 5,125,000. Deduct on payment/settlement, not mere unrelated-party invoice accrual. Remit to NRS by the federal deadline and issue the prescribed receipt. Recipient includes gross fees and claims the non-final credit. These are the preserved original inputs; VAT classification itself is assumed for the arithmetic and remains in its owning skill.

```oa-check
name: Nigeria resident consultancy invoice and missing-TIN decision
inputs:
  fee: 5000000
  vat_separately_stated: 375000
steps:
  - invoice: fee + vat_separately_stated
  - wht_with_tin: fee * 0.05
  - cash_with_tin: invoice - wht_with_tin
  - wht_without_tin: fee * 0.05 * 2
  - cash_without_tin: invoice - wht_without_tin
expected:
  invoice: 5375000
  wht_with_tin: 250000
  cash_with_tin: 5125000
  wht_without_tin: 500000
  cash_without_tin: 4875000
```

The decision changes only the non-passive missing-TIN fact. It does not permit withholding an unnamed higher rate on every ambiguous payment.

**Original case 2, ABC Nigeria Ltd and a UK-resident company.** Software licence assumed to be royalty under the actual rights, with no Nigerian PE/fixed-base connection. Gross GBP100,000, illustrative authorised conversion NGN 1,950/GBP, NGN 195,000,000. At 10%, WHT is GBP10,000 or the illustrative NGN 19,500,000, net GBP90,000 or NGN 175,500,000. ScenarioA has no TRC; ScenarioB has a valid HMRC TRC and all treaty conditions. Article 12's 12.5% ceiling does not lower 10%, so both scenarios give the same result. The former 7.5%, NGN 14,625,000/GBP92,500 result was wrong. Do not assume the licence/SaaS classification or currency permission for an actual contract.

```oa-check
name: Nigeria UK royalty domestic rate against treaty ceiling
inputs:
  gbp: 100000
  illustrative_ngn_per_gbp: 1950
steps:
  - ngn: gbp * illustrative_ngn_per_gbp
  - domestic_wht: ngn * 0.10
  - treaty_ceiling: ngn * 0.125
  - eligible_wht: min(domestic_wht, treaty_ceiling)
  - net_ngn: ngn - eligible_wht
  - net_gbp: gbp - eligible_wht / illustrative_ngn_per_gbp
expected:
  ngn: 195000000
  domestic_wht: 19500000
  treaty_ceiling: 24375000
  eligible_wht: 19500000
  net_ngn: 175500000
  net_gbp: 90000
```

**Original case 3, NewCo Nigeria Ltd and OldCo Nigeria Ltd.** Nigerian dividend NGN 100,000,000, prescribed 10% deduction NGN 10,000,000, cash NGN 90,000,000. Preserve the receipt as franked-income evidence. Do not also tax that dividend as ordinary company income or credit the final deduction against unrelated profits. A later redistribution requires the statutory set-off analysis.

```oa-check
name: NewCo Nigeria dividend to OldCo Nigeria
inputs:
  gross_dividend: 100000000
steps:
  - deduction: gross_dividend * 0.10
  - cash: gross_dividend - deduction
expected:
  deduction: 10000000
  cash: 90000000
```

## When to refuse or refer

Use the boundary table. A working paper may show a clearly labelled alternative, but cannot select residence, treaty eligibility, royalty rights, a petroleum overlay or a missing exemption as a guess. Do not submit a return or contact a recipient from this reference. Resolve any transition or deadline conflict before a disputed final filing position.

## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| JRB official Gazette S.I.34: complete regulations 1 to14 and all three Schedules; both rate-table page images checked | https://www.jrb.gov.ng/documents/withholding-regulations-2024.pdf | 2026-11-16 |
| National Assembly NTAA: sections 3, 28, 51, 55, 65, 66, 101, 105 and107 | https://nass.gov.ng/documents/download/11250 | 2026-11-16 |
| National Assembly NTA: sections 17, 120 and198, preserving compatible subsidiary rules | https://nass.gov.ng/documents/download/11249 | 2026-11-16 |
| JRB PIT Guidelines: paragraphs 12 to16,20 and26; State deadline wording and compensation interaction | https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf | 2026-11-16 |
| LIRS FAQ: WHT matrix, recipient-based authority, currency, remittance, final-tax and receipt questions | https://lirs.gov.ng/faq | 2026-11-16 |
| HMRC full treaty Article 12, neighbouring Articles 7 and13 and entry-into-force page; no worldwide treaty network review | https://www.gov.uk/government/publications/nigeria-tax-treaties/1987-uk-nigeria-double-taxation-agreement-in-force | 2026-11-16 |

Not yet confirmed: mapping the regulation 4 CITA small-payer definition to a borderline 2026 payer; a resolution of State30th/last-day guidance against NTAA section 107's21st-day sanction trigger; a sole trader's agent capacity in disputed circumstances; the actual software/SaaS classification, conversion permission and authenticated portal fields; special PSC/JV withholding instructions; any blanket expense-disallowance or common-law receipt-damages claim; current SEP implementing details. Specifically held from the original SEP2020 topic: the asserted NGN 25m Nigerian turnover, .ng-domain and local-payment-infrastructure triggers and automatic10% B2B consequence. NTA section17 is the current non-resident source/taxable-presence owner; classify the actual payment under the sourced matrix and refer the implementing-order question rather than reuse those unverified triggers. The original treaty matrix/network is retained as an unconfirmed topic list, not rates or an in-force claim: UK, Netherlands, Canada, France, China, South Africa, Singapore, Belgium, UAE, Czech Republic, Pakistan, Philippines, Romania, Slovakia, South Korea, Spain, Sweden, Italy and Cameroon. Only the UK royalty article was checked here. The earlier generic7.5% treaty caps,1997 tax-point rule,NGN 10,000/25,000 de-minimis claims,2.5% construction rate and assumed future single schedule are replaced by the sourced rules above.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ng-wht` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ng-wht. If neither is available, confirm every figure against the official source pages cited above before relying on it.
