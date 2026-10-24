---
name: fi-property-transfer-tax
description: >
  Prepare Finnish property-transfer tax calculations for real estate and
  housing-company shares, distinguish contract and ownership-transfer dates,
  and reconcile the debt-free price. Statutory, exception and named Finnish accountant review
  remain outstanding.
jurisdiction: FI
category: property
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.3
---

# Finland property transfer tax v0.3

## Who this applies to

Use this draft for a buyer of Finnish real estate, a building or housing/real-estate-company shares. Classify the legal asset before calculating tax. A dwelling can be acquired through shares rather than direct ownership of land/buildings. The following official rates are displayed on Vero's current transfer-tax page: [Transfer-tax overview][overview]

| Acquisition | Rate |
|---|---|
| Real estate and buildings | 3% |
| Housing-company or real-estate-company shares | 1.5% |

Sections 6 and 20 of the Transfer Tax Act support the respective 3% and 1.5% rates. Direct-estate consideration and property-company debt rules differ; apply the correct base before multiplying. [Transfer Tax Act][law]

This is a transfer-tax draft. Annual property tax, rental income, capital gains, VAT and financing deductions require separate work.

## Housing shares: establish the debt-free base

Vero's apartment guidance includes the purchase price, other agreed consideration and the unpaid company-loan portion allocated to the acquired shares. Immediate repayment versus later instalments does not remove that loan from the base. Reconcile the agreement and company records before applying the rate. [Housing-company shares][shares]

Keep the following preparation evidence: share identifiers, ownership percentage, purchase consideration, allocated debt statement, payment terms and the effective ownership-transfer date. Explain any mismatch between advertised cash price, contract consideration and debt-free price. These are practical reconciliation controls; unusual consideration and corporate transactions require further legal analysis.

## Deadlines and who files

| Purchase route | Ordinary guidance |
|---|---|
| Real estate requiring title/leasehold registration | Buyer files and pays before applying; registration application within six months of signing |
| Building without title registration | Buyer files and pays within six months of signing |
| Existing housing shares, private transaction | File and pay within two months of signing |
| Existing housing shares through an agent | Pay at signing; agent files |
| New construction under the stated ownership-transfer arrangement | Buyer files and pays within two months of ownership transfer, including agent-assisted sales |

[Vero deadline table][deadlines]. An agent does not take over the buyer's filing responsibility for a direct real-estate acquisition. Do not automatically start every two-month period from the same event. The guidance says first-home relief ended for purchases from 1 January 2024; historical purchases require their own eligibility and filing check. [Deadline table][deadlines]

Confirm any special acquisition route, holiday rule and current instructions before calendaring the actual transaction. No live filing or title registration was tested for this draft.

### Conditional additional consideration from 2026

For contracts made from **1 January 2026**, Act 1143/2025 adds a separate rule for contractual contingent consideration whose payment obligation and amount become confirmed after the ordinary tax-payment deadline. Pay the tax on that additional part within **two months of that confirmation**, rather than deferring the original purchase tax. It applies to direct real estate and securities under sections 7(2) and 21(5). Earlier contracts follow the previous rules. [Amending Act 1143/2025, including commencement][amendment]

Retain the original agreement, contingency terms, original return/payment, date both obligation and amount became confirmed, calculation and supplemental filing evidence. Do not use the bank-payment date as the confirmation date without establishing the contractual facts. Current return/correction mechanics and exceptional deadlines still need checking before filing.

## Non-resident buyers and scope traps

Vero distinguishes ordinary corporate stock from housing/real-estate-company shares when both parties are non-residents. Its corporate-stock guidance still directs non-resident property-company-share buyers to register, file and pay. Do not transplant an ordinary corporate-stock exemption to housing shares. Foreign property-holding companies and indirect transfers need further scope review. [Corporate-stock guidance][stock]

Likewise, “first home”, a gift label or a stock-exchange connection does not itself establish exemption. Consideration, asset category, acquisition date and the exact exemption must be checked. This draft supplies no blanket exemption finding.

## Preparation sequence

1. Identify the buyer, seller, residences, asset and percentage acquired.
2. Read the signed agreement and establish the relevant signing/ownership dates.
3. Reconcile consideration and company debt to the supported tax base.
4. Identify the correct filer, return route, due date and payment reference.
5. Preserve submission confirmation, tax payment and registration evidence.

Record any unverified condition before advising on payment. Payment and filing are separate completion checks.

## Worked examples

### 1. Housing shares with allocated company debt

Assume cash consideration of EUR 180,000 and allocated unpaid housing-company debt of EUR 60,000, no other consideration and no exemption. Base EUR 240,000 at 1.5% gives EUR 3,600. Using cash consideration alone would understate the assumed tax by EUR 900.

```oa-check
name: Finland housing share debt free price
inputs:
  cash_consideration: 180000
  allocated_company_debt: 60000
  transfer_tax_rate: 0.015
steps:
  established_base: cash_consideration + allocated_company_debt
  transfer_tax: established_base * transfer_tax_rate
  cash_only_tax: cash_consideration * transfer_tax_rate
  omitted_tax: transfer_tax - cash_only_tax
expected:
  established_base: 240000
  transfer_tax: 3600
  cash_only_tax: 2700
  omitted_tax: 900
```

### 2. Direct real-estate acquisition

Assume EUR 250,000 is the correctly established taxable consideration for a direct real-estate purchase and no exemption applies. At 3%, transfer tax is EUR 7,500. This example assumes the base and asset classification; it does not establish additional-consideration or special-transaction treatment.

```oa-check
name: Finland assumed direct real estate transfer tax
inputs:
  established_consideration: 250000
  rate: 0.03
steps:
  transfer_tax: established_consideration * rate
expected:
  transfer_tax: 7500
```

### 3. Additional consideration confirmed after the ordinary deadline

Assume a direct-estate contract signed in February 2026, correctly taxed original consideration of EUR 250,000 and contractual contingent consideration of EUR 50,000 whose obligation and amount become confirmed in November, after the ordinary deadline. At the assumed applicable 3% rate, additional tax is EUR 1,500, making total purchase tax EUR 9,000. The two-month additional-payment clock follows that confirmation; actual dates and filing mechanics need a separate check. No exemption or other consideration is assumed.

```oa-check
name: Finland assumed contingent real estate consideration tax
inputs:
  original_taxed_consideration: 250000
  later_confirmed_additional_consideration: 50000
  established_rate: 0.03
steps:
  original_tax: original_taxed_consideration * established_rate
  additional_tax: later_confirmed_additional_consideration * established_rate
  combined_tax: original_tax + additional_tax
expected:
  original_tax: 7500
  additional_tax: 1500
  combined_tax: 9000
```

## Ask the client first

- What legal asset and share are being acquired, and by whom?
- What are the signed agreement and ownership-transfer dates?
- What consideration and company debt are attached to the asset?
- Was an agent involved, and is the property newly constructed?
- What exemption is claimed, and what evidence supports it?
- Which filings, payments and registrations already exist?

## Sources and review limits

Official Vero text retrieved in the search index on 23 October 2026:

- [Transfer Tax Act][law], sections 4, 6–7, 15 and 20–21, read directly from embedded Finnish statutory text on 23 October 2026. [Amending Act 1143/2025][amendment] was read in its official two-page PDF, including the contract-date transition.

- [Current overview][overview], updated 7 January 2026.
- [Housing-share base guidance][shares].
- [Deadline table][deadlines].
- [Corporate-stock/non-resident distinction][stock].

Not yet confirmed: remaining Transfer Tax Act/amendment scope; detailed consideration and reorganisation cases; indirect/foreign property-company transfers; exemptions and other historical transitions; refunds, penalties, interest, supplemental filing mechanics and holiday rules. Named Finnish accountant review remains outstanding; the independent source-review scope is recorded in the [country README](README.md#evidence-and-next-action). Property and country coverage remain partial.

[law]: https://www.finlex.fi/fi/lainsaadanto/1996/931
[amendment]: https://www.finlex.fi/api/media/statute/896509/mainPdf/main.pdf?timestamp=2025-12-11T05%3A12%3A12.000Z

[overview]: https://www.vero.fi/en/individuals/property/transfer-tax/
[shares]: https://www.vero.fi/en/individuals/property/transfer-tax/buyer-of-a-flat/
[deadlines]: https://www.vero.fi/en/individuals/property/transfer-tax/instructions-for-filing-and-paying-transfer-tax/table-of-filing-and-payment-deadlines/
[stock]: https://www.vero.fi/en/individuals/property/transfer-tax/corporate-stock/
