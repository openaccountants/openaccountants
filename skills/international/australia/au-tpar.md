---
name: au-tpar
description: >
  Use this skill for any Australian Taxable payments annual report (TPAR) question
  under the taxable payments reporting system: which businesses must lodge, the
  10% test and the building and construction 50% test, which contractor payments
  to report or exclude, the contractor details required, how to lodge online,
  non-lodgment advice, amendments, and failure to lodge penalties. Trigger on
  "TPAR", "taxable payments annual report", "taxable payments reporting system",
  "TPRS", "contractor payments report", "28 August", "report subcontractor
  payments", "cleaning contractors ATO report", "courier TPAR", "IT services
  TPAR", "security services TPAR". Covers the 2026-27 report due 28 August 2027.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 income year (1 July 2026 to 30 June 2027)"
last_updated: 2026-09-27
review_status: pending_review
depends_on:
  - au-lodgment-deadlines-penalties
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Taxable Payments Annual Report

## Australia Taxable Payments Annual Report (TPAR) v1.0

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## Section 1 - Quick Reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Year covered | Payments made from 1 July 2026 to 30 June 2027, reported by 28 August 2027 |
| Who lodges | Businesses that pay contractors for building and construction, cleaning, courier, road freight, information technology, or security, investigation or surveillance services, and government entities that pay for services or make grants |
| The test | 10% or more of business income from the relevant service (building and construction uses a 50% test instead) |
| Basis | Cash: payments made on or before 30 June, including GST |
| What to report per contractor | ABN, name, address, gross amount paid including GST, GST, and tax withheld where no ABN was quoted |
| How to lodge | SBR-enabled software, a TPAR data file, Online services for business, Online services for individuals and sole traders, or a registered agent; paper is no longer accepted |
| Not required | Lodge a non-lodgment advice so the ATO does not chase the report |
| Late lodgment | Failure to lodge on time penalty of one penalty unit ($364 from 1 July 2026) per 28 days or part, up to five units, multiplied for medium and large withholders |
| Primary legislation | Taxation Administration Act 1953, Schedule 1, Division 396 (third party reporting) |
| Tax authority | Australian Taxation Office |
| Reviewed by | Pending. Australian CPA or CA review required |

## Section 2 - The workflow

**Step 1. Identify the services the business provides.**
Only the six taxable payments reporting system (TPRS) service types, and government entities, are
in scope. See Section 3.

**Step 2. Apply the test.**
Building and construction businesses ask whether 50% or more of income or activity is from those
services, in the current or the previous year. Every other TPRS business asks whether 10% or more
of its business income is from the relevant service. See Section 3.

**Step 3. Extract the contractor payments for those services.**
Include invoices that mix labour and materials; exclude materials only, incidental labour,
labour hire, employees, consolidated group members and private work. See Section 4.

**Step 4. Confirm the contractor details.**
Check each ABN on ABN Lookup, keep name and address, and record GST and any no-ABN withholding.
See Section 5.

**Step 5. Reconcile to the ledger on a cash basis.**
Report what was paid in the year, not what was invoiced. An invoice unpaid at 30 June is reported
in the year it is paid.

**Step 6. Lodge by 28 August, or lodge a non-lodgment advice.**
See Section 6.

**Step 7. Amend if a detail or amount was wrong.**
See Section 6.

## Section 3 - Who must lodge

**Taxable payments reporting system services**

| Service | Who is caught | Test |
| --- | --- | --- |
| Building and construction | A business primarily in building and construction services that pays contractors for those services and has an ABN | 50% or more of business income or business activity in the current year, or 50% or more of income in the previous year |
| Cleaning | A business providing cleaning services that pays contractors to deliver them | 10% or more of business income from cleaning services |
| Courier and road freight | Combine the two when testing | 10% or more of business income from courier and road freight services together |
| Information technology | A business providing IT services that pays contractors to deliver them | 10% or more of business income from IT services |
| Security, investigation or surveillance | A business providing those services that pays contractors to deliver them | 10% or more of business income from those services |
| Government entities | Government entities that pay for services or make grants | Payments to entities for services, and grants paid to people or organisations with an ABN |

- **The 10% test** — Add up the payments received for the relevant service in the year, divide by current business income (or projected income for a business operating less than 12 months), and multiply by 100. At 10% or more, and with contractor payments made for that service, a TPAR is required.  _([ATO, Work out if you need to lodge a TPAR](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar))_
- **Building and construction** — The definition is broad: alteration, assembly, construction, demolition, design, excavation, installation, maintenance (other than of equipment and tools), project management, repair, site preparation and similar work on any building, structure, works, surface or sub-surface. Cabinet making, landscaping, surveying, architectural drafting, engineering and equipment hire with an operator are all in; a hardware retailer that arranges installation, and testing and tagging of tools, are not.  _([ATO, Building and construction services](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/building-and-construction-services))_
- **Once in, in for two years** — A business above 50% in one year must lodge for the following year as well, because the test also looks back at the previous year.  _([ATO, Building and construction services](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/building-and-construction-services))_
- **Separate entities** — A retailer that sets up a separate installation entity moves the reporting obligation to that entity, whose income is wholly from building and construction services.  _([ATO, Building and construction services](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/building-and-construction-services))_
- **Government entities** — Report payments for services and grants to ABN holders, including the grant date and program name, and whether a statement by a supplier was received.  _([ATO, Payments government entities need to report](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/payments-government-entities-need-to-report-in-their-tpar))_

## Section 4 - What to report and what to leave out

**Reportable and non-reportable payments**

| Report | Do not report |
| --- | --- |
| Payments to contractors and subcontractors for the relevant service, whether sole traders, companies, partnerships or trusts | Payments for materials only |
| The whole invoice where it covers both labour and materials | Labour that is incidental to a supply of materials |
| Payments made on or before 30 June, including GST | Invoices unpaid at 30 June |
| Amounts withheld where the contractor quoted no ABN, if not reported on the no-ABN annual report | Workers supplied under a labour hire or on-hire arrangement |
| Payments to a subcontractor engaged by the business, even where that subcontractor sub-lets the work | Payments to employees and other PAYG withholding payments, which go through STP |
| | Payments to foreign residents subject to foreign resident withholding, and foreign residents for work performed overseas |
| | Payments to another member of the same income tax consolidated group |
| | Payments for private or domestic projects, including a business owner's own home |

- **Cash basis** — Only payments made on or before 30 June are reported. Report an invoice paid in July in the following year's TPAR.  _([ATO, Payments businesses need to report in their TPAR](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/payments-businesses-need-to-report-in-their-tpar))_
- **No-ABN withholding** — Where a supplier gives no ABN and the payment exceeds $75 excluding GST, withhold the top rate of 47%, give the supplier a payment summary, and report the withheld amount either in the TPAR or in the PAYG withholding where ABN not quoted annual report, never in both.  _([ATO, Withholding if ABN is not provided](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-suppliers/withholding-if-abn-not-provided))_
- **Consolidated groups** — Members of an income tax consolidated or multiple entry consolidated group do not report payments to each other, because the group is taxed as one entity.  _([ATO, Payments businesses need to report in their TPAR](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/payments-businesses-need-to-report-in-their-tpar))_
- **Mixed private and business payments** — A cleaning agency reports the contractors who clean its clients' premises, but not the contractor it pays from a personal account to clean the owner's home.  _([ATO, Payments businesses need to report in their TPAR](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/payments-businesses-need-to-report-in-their-tpar))_

## Section 5 - Contractor details and records

- **Details per contractor** — ABN (each ABN if it changed during the year), business or individual name, address, and the year's totals of gross amount paid including GST and any tax withheld, total GST paid and total tax withheld where no ABN was quoted. The ATO may ask for phone, email and bank details.  _([ATO, TPAR contractor details to report](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/tpar-contractor-details-to-report))_
- **Check the ABN** — Match the ABN on each invoice to the contractor record and confirm the name and GST registration on ABN Lookup or the ATO app; create a new record when the ABN changes.  _([ATO, TPAR contractor details to report](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/tpar-contractor-details-to-report))_
- **Records** — Keep the contractor's name, address, ABN and the amounts paid including GST, and use the ATO's taxable payments reporting worksheet where the software cannot produce the report.  _([ATO, Lodge your TPAR](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar))_
- **Payee statements** — Nothing has to be given to the contractor, but the ATO's payee information statement can be used to tell them what was reported, in whole dollars.  _([ATO, TPAR contractor details to report](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/tpar-contractor-details-to-report))_

## Section 6 - Lodging, non-lodgment advice and amendments

- **Channels** — Lodge through SBR-enabled software, by uploading a data file that meets the TPAR specification, through Online services for business (Lodgments, then Taxable payments annual report), through Online services for individuals and sole traders, or through a registered tax or BAS agent using Online services for agents. Drafts can be saved and resumed, and the History section holds receipts.  _([ATO, Lodge your TPAR](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar))_
- **No paper** — Paper TPAR lodgments have not been accepted since 28 August 2025.  _([ATO, Lodge your TPAR](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar))_
- **Non-lodgment advice** — A business that has lodged before but does not need to lodge for a year should submit the TPAR non-lodgment advice form, which tells the ATO not to expect a report for that year.  _([ATO, TPAR non-lodgment advice](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/tpar-non-lodgment-advice))_
- **Amendments** — Correct a contractor's details or amounts by lodging an amended TPAR through the same channels; the ATO's amendment page sets out the steps for each channel.  _([ATO, Amend a lodged TPAR](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/amend-a-lodged-tpar))_

## Section 7 - Penalties

- **Failure to lodge on time** — The base penalty is one penalty unit for each 28 days or part that the report is overdue, up to five units. Medium withholders pay twice the base, large withholders five times, and significant global entities 500 times. The ATO warns before penalising and considers remission, but a TPAR is a third-party data report, so the usual practice of not penalising a late nil or refund lodgment does not apply.  _([ATO, Failure to lodge on time penalty](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty))_
- **Penalty unit** — $364 for infringements on or after 1 July 2026 and $330 from 7 November 2024 to 30 June 2026, so a small business four months late in 2027 faces up to $1,820.  _([ATO, Penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units))_
- **Safe harbour** — No penalty applies where the business gave a registered tax or BAS agent everything needed to lodge on time and the agent's failure was not reckless or intentional.  _([ATO, Failure to lodge on time penalty](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty))_

## Section 8 - Worked example

**Worked example facts**

| Item | Detail |
| --- | --- |
| Business | Sparkle Commercial Cleaning Pty Ltd, GST registered, operating for the whole of 2026-27 |
| Business income for 2026-27 | $600,000 |
| Receipts for cleaning services | $90,000; the rest is sales of cleaning products |
| Contractor A | Sole trader with an ABN, GST registered, paid $44,000 for cleaning during the year including $4,000 GST |
| Contractor B | Company with an ABN, not GST registered, paid $12,500 for cleaning |
| Contractor C | Individual who quoted no ABN, invoice $2,000 for cleaning, paid in March 2027 |
| Supplier D | Chemicals wholesaler, paid $8,000 for products only |
| Contractor E | Sole trader with an ABN, cleaning invoice of $3,300 dated 20 June 2027, paid on 8 July 2027 |
| Labour hire firm F | Supplied two cleaners on an on-hire basis, paid $30,000 |

**Facts.** All figures are synthetic.

**Step 1, the test.** $90,000 of $600,000 is 15%, so cleaning services are 10% or more of business
income, and the company paid contractors for cleaning. A TPAR for 2026-27 is due by 28 August 2027.

**Step 2, the payments.**

```
Contractor A   gross 44,000   GST 4,000   withheld     0   report
Contractor B   gross 12,500   GST     0   withheld     0   report
Contractor C   gross  2,000   GST     0   withheld   940   report (47% no-ABN withholding, net paid 1,060)
Supplier D     materials only                              exclude
Contractor E   paid after 30 June 2027                     report in the 2027-28 TPAR
Labour hire F  on-hire arrangement                         exclude
```

**Step 3, the report.**

```
Contractors reported                              3
Total gross amount including GST             58,500
Total GST                                     4,000
Total tax withheld where no ABN quoted          940
```

**Step 4, the no-ABN amount.** The $940 withheld from Contractor C is reported in the TPAR only.
It is not also included in a PAYG withholding where ABN not quoted annual report, and Contractor C
was given a payment summary at the time of payment.

**Step 5, if the test had failed.** Had cleaning receipts been $50,000, the share would have been
8.3%, no TPAR would be required, and the company would lodge a non-lodgment advice if the ATO had
it on the TPRS list from an earlier year.

## Section 9 - Common errors

- Applying the 10% test to a building and construction business instead of the 50% test, or forgetting the look-back to the previous year.
- Testing courier and road freight separately when the receipts must be combined.
- Reporting on an accruals basis and including invoices unpaid at 30 June.
- Excluding an invoice because it includes materials, when the whole invoice is reportable once labour is more than incidental.
- Reporting payments to employees, labour hire workers or consolidated group members.
- Reporting the no-ABN withholding both in the TPAR and in the no-ABN annual report.
- Using an old ABN after a contractor changes entity mid-year.
- Assuming a late TPAR carries no penalty because no tax is payable with it.
- Lodging on paper, which the ATO no longer accepts.
- Not lodging a non-lodgment advice when the obligation ends.

## Section 10 - Self-checks

- [ ] The service type and the correct test (10% or 50%) are documented for the year.
- [ ] Courier and road freight receipts are combined for the test.
- [ ] Contractor payments are extracted on a cash basis for 1 July to 30 June.
- [ ] Every reported invoice is for the relevant service and is not materials only or incidental labour.
- [ ] Each ABN has been checked on ABN Lookup and matches the invoice.
- [ ] Gross amounts include GST and any tax withheld, and GST is shown separately.
- [ ] No-ABN withholding is reported in one annual report only.
- [ ] Employees, labour hire workers, consolidated group members and private work are excluded.
- [ ] The report is lodged by 28 August, or a non-lodgment advice is lodged.
- [ ] Any error found later is corrected through an amended TPAR.

## Section 11 - Sources

- Taxation Administration Act 1953, Schedule 1, Division 396, Subdivision 396-B (reporting by third parties) and the Taxation Administration Amendment Regulation 2012 (No. 1) definition of the building and construction industry.
- ATO, Taxable payments annual report (TPAR), https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report
- ATO, Work out if you need to lodge a TPAR, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar
- ATO, Payments businesses need to report in their TPAR, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/payments-businesses-need-to-report-in-their-tpar
- ATO, Building and construction services, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/building-and-construction-services
- ATO, Payments government entities need to report in their TPAR, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/payments-government-entities-need-to-report-in-their-tpar
- ATO, Lodge your TPAR, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar
- ATO, TPAR contractor details to report, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/tpar-contractor-details-to-report
- ATO, TPAR non-lodgment advice, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/tpar-non-lodgment-advice
- ATO, Amend a lodged TPAR, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/amend-a-lodged-tpar
- ATO, Withholding if ABN is not provided, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-suppliers/withholding-if-abn-not-provided
- ATO, Failure to lodge on time penalty, https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty
- ATO, Penalty units, https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units

Sources were checked on 27 September 2026.

> **Working paper only, not a lodged report.** Have a qualified Australian CPA or CA review the service test and the contractor extract before lodging. The ATO matches TPAR data against contractors' returns, so an omitted or misclassified contractor is visible.

> Contributed by Ryan Duguid.

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
