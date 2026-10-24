---
name: dm-nonresident-withholding-tax
description: >
  Dominica nonresident withholding reference covering ordinary payment categories, the statutory fifteen percent rate, gross-basis calculations, remittance timing and deduction certificates. Reconciles the old scanned consolidation with the 2007 rate amendment effective in 2008 and current Inland Revenue instructions. Explains year-end accrual and business-presence boundaries and provides an evidence workflow. Does not establish treaty entitlement, all exemptions, special industry treatment, current penalties or the complete amendment chain. Intended as a source-cited research draft pending independent review, not a complete country coverage assessment.
jurisdiction: DM
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: "0.4"
verified_by: pending
---

# Dominica: nonresident withholding tax

## Source status and ordinary rate

The Third Schedule of the Income Tax Act governs deductions on specified nonresident payments. The government's scanned consolidation prints older differentiated rates. **Act 15 of 2007, section 5 replaces paragraph 3 with a 15% rate**, subject to section 50, and states final liability for the relevant income. Section 7 makes that amendment effective **1 January 2008**. Do not use the superseded rental/other-payment rates from the old scan. The [IRD withholding page](https://ird.gov.dm/index.php?Itemid=105&id=17&option=com_content&view=article) corroborates the ordinary 15% rate. [Amendment, sections 5 and 7](https://dominica.gov.dm/laws/2007/act15-2007.pdf).

This Guide does not certify a complete 2026 consolidation or eligibility for an exemption or treaty reduction. The relevant schedule pages and sections 57, 97 and 98 were inspected; the entire scanned Act has not been audited.

## Which payments need classification

Third Schedule paragraph 1 lists dividends; interest/discounts; immovable-property rentals, lease premiums and licences; movable-property rentals; royalties; management charges; specified commissions/fees; annuities and other periodic payments; distributions of the listed income through trusts; and other income payments to nonresidents. It separately addresses independent personal services performed in Dominica and contains a business/employment-presence boundary. Establish where services are performed, residence, local business presence and the actual payment category before treating every foreign invoice alike. [Third Schedule, paragraph 1](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=119).

This is not the ordinary employee PAYE calculation. The schedule itself excludes the specified employment fees and provides separate treatment for business presence. Section 57(2) creates a **rebuttable presumption of nonresidence when payment is made to an address outside Dominica**, expressly including partnerships. Obtain evidence to rebut that presumption where relevant. Citizenship, currency and bank location alone are not the stated statutory test. Treaty entitlement and permanent-establishment analysis remain outside this draft. [Section 57(2)](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=60).

## Gross amount and examples

Paragraph 2 requires deduction from the **gross payment**. With a taxable EC$20,000 gross royalty and no relief, 15% withholding is **EC$3,000**, leaving **EC$17,000** for the recipient. For a taxable EC$8,000 gross fee, the corresponding figures are **EC$1,200** and **EC$6,800**. Do not subtract the recipient's expenses before this calculation. A contract guaranteeing a net amount requires a separate gross-up review. [Third Schedule, paragraph 2](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=120); [Act 15 of 2007, section 5](https://dominica.gov.dm/laws/2007/act15-2007.pdf).

Paragraph 1(3) addresses accrual-basis expenses unpaid at year-end: the retrieved text treats the payment as made on the last day of the basis period for deduction/accounting purposes. Review accrued foreign charges at closing rather than checking only bank transfers. Later amendments and application to the particular accrual still need verification. [Third Schedule, paragraph 1(3)](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=120).

## Remit and document the deduction

Section 97(b) makes section 57 tax due **within fifteen days after the end of the month** in which it was **deducted or deductible**. The obligation does not wait for the payer to correct an omitted deduction. The IRD corroborates the fifteen-day month-end deadline. [Section 97](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=86). The payer prepares the approved return identifying the deduction and amount paid, with the deduction certificate. Keep the payment date, relevant month, amount withheld and actual remittance receipt together. Holiday adjustments and current electronic submission requirements have not been verified. [IRD instructions](https://ird.gov.dm/index.php?Itemid=105&id=17&option=com_content&view=article).

The official certificate records payer tax account number/name/address, nonresident recipient name/address, payment type and date, payment period, gross amount paid or credited, rate and deduction. Its instructions require **three copies per nonresident recipient**, forwarded with the remittance form. Two are returned with the receipt: retain one and forward the other to the recipient. Sign the declaration only when its statements about withholding and payment are true. [Official deduction certificate](https://ird.gov.dm/phocadownload/returns/whitholdingtax_certificate%20of%20deduction_fillable.pdf).

Third Schedule paragraph 4 also requires calendar-year records of payment nature, gross amount, deduction and recipient name/address, available to the Comptroller; paragraph 5 requires a return and certificate copies with remittance. Reconcile the certificate totals to the ledger and receipts. This draft does not invent a separate annual withholding-return deadline. [Third Schedule, paragraphs 4–5](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=121).

## Exceptions and remaining verification

The 2007 replacement rate is expressly subject to section 50 on international agreements. Section 57(3) allows the Comptroller to direct a lower deduction when satisfied that the recipient is resident in a treaty country whose agreement provides the lower rate. Obtain the agreement, residence/entitlement evidence and the applicable direction; a recipient's request for a reduced rate is not itself that direction. [Section 57(3)](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=60). Special airline, pension, life-assurance, employment, exemption and local-business cases require their own statutory checks. Section 98 prints interest of **1% per month or part of a month** on unpaid deductions under the specified provisions, additional to penalties, and makes that interest the payer's debt, not recoverable from the recipient. The IRD corroborates the 1% monthly rate but its short summary omits the part-month wording. Preserve that distinction when checking an assessment. The later amendment chain and penalty provisions are not fully reconciled, so this Guide does not certify a final late-payment calculation. [Section 98](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=86).

Before filing, verify recipient status, payment classification, relief evidence, gross amount, deduction timing, the approved remittance form and submission route. Keep contractual terms, invoices, accrual workings, certificate copies and IRD receipts. Full intervening-amendment reconciliation and independent review remain outstanding; this draft does not make Dominica comprehensive.

## Executable check of the existing examples

These checks reproduce the gross-payment examples above. They do not resolve the stated eligibility, amendment or procedural gaps.

```oa-check
name: Dominica existing gross payment examples
inputs:
  royalty_gross: 20000
  fee_gross: 8000
  rate: 0.15
steps:
  - royalty_tax: royalty_gross * rate
  - royalty_net: royalty_gross - royalty_tax
  - fee_tax: fee_gross * rate
  - fee_net: fee_gross - fee_tax
expected:
  royalty_tax: 3000
  royalty_net: 17000
  fee_tax: 1200
  fee_net: 6800
```

## Disclaimer

Source-cited research draft, not accountant attestation or a transaction-specific tax opinion.

## Sources


The following links collect the sources already cited above. Their applicable versions, statutory locators and unresolved limitations remain as stated in the body; this list is not a new source verification.

- [IRD withholding page](https://ird.gov.dm/index.php?Itemid=105&id=17&option=com_content&view=article)
- [Amendment, sections 5 and 7](https://dominica.gov.dm/laws/2007/act15-2007.pdf)
- [Third Schedule, paragraph 1](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=119)
- [Section 57(2)](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=60)
- [Third Schedule, paragraph 2](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=120)
- [Section 97](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=86)
- [Official deduction certificate](https://ird.gov.dm/phocadownload/returns/whitholdingtax_certificate%20of%20deduction_fillable.pdf)
- [Third Schedule, paragraphs 4–5](https://www.dominica.gov.dm/laws/chapters/chap67-01.pdf#page=121)
