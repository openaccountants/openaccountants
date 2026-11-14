---
name: qc-qst-return
description: "Prepare a Quebec QST/TVQ return workpaper for an ordinary self-employed person or small business under the general QST system. Establish registration and reporting period, taxable/zero-rated/exempt supply and place, collectible tax, documented ITRs, meals/use limits, corrections, import exceptions, quick-method election and current remittance rates. Reconcile QST and GST separately within the actual permitted joint or separate return route, with correct annual individual filing/payment dates and no automatic tax on all foreign SaaS."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/qc-qst-return"
  jurisdiction: "CA-QC"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Quebec QST return v3.0

## Scope

Prepare a QST/TVQ workpaper for an ordinary sole proprietor/small business under the general registration system. QST is a distinct tax administered by Revenu Québec, with federal GST/HST calculated separately. **Separate calculations do not mean joint filing is forbidden.** Revenu Québec expressly provides a joint GST/HST-QST return and detailed FPZ-2034.CD-V workpaper, as well as specific separate-return routes. The old 'never combine into a single return' prohibition and generic VD-403 return name were wrong. Establish the registrant's actual account/filing route first. [Actual FPZ-2034.G-V 2026-09 scope/return](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

| Quick reference | Entry |
|---|---|
| Place | Quebec, Canada; CAD workpaper; actual foreign-currency conversion evidence where applicable |
| Tax/statute | QST/TVQ; Act respecting the Quebec sales tax, CQLR c.T-0.1; federal GST/HST remains its own Excise Tax Act calculation |
| Administration | Revenu Québec general-system account, actual confirmation and period |
| Current sources | IN-203-V 2026-03 and FPZ-2034.G-V 2026-09; edition dates do not certify every specialised rule |
| Contributor | Open Accountants Community |

This method produces reviewable computations and proposed postings. It does not submit, register, pay or post journals. Read alongside `canada-gst-hst` for federal work. Financial institutions, real property, specified/non-resident registration, charities/PSBs and material special schemes require their actual rules; a normal small-business calculator is not a universal QST engine. [General/specified-system distinction](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

## Ask the client first

1. What are the entity/owner, business activities, residence and supplier/customer locations, general or specified QST registration, actual QST/GST numbers, effective dates and tax account? Unknown registration is not proof of non-registration.
2. What assigned fiscal year/reporting period, election, prior return, opening adjustments and annual instalments apply? Obtain the actual confirmation, not just a turnover estimate. Is the filer an individual with business income and a 31 December annual period?
3. What invoice-level sales, tax-inclusive/exclusive amounts, discounts/credits, supply types, export/delivery/service/right-of-use facts, timing/collectible tax and customer status support the period? Separate standard-rate, zero-rated, exempt and outside-scope transactions.
4. What supplier invoices, QST registration-system/status, tax paid/payable, legal purchaser, commercial-use allocation and operating/capital classification support each ITR? Obtain previous claims/carryovers, asset/vehicle/home-office use and required supporting-document information.
5. What meals/entertainment expenses, annual revenue ceiling, exceptions, reimbursement and previous full-credit adjustments apply? A bank merchant label is not enough.
6. What foreign/out-of-province goods, services or intangible-property purchases, commercial use, vendor carrying-on-business/registration/collector status and tax already charged require an import/self-assessment determination?
7. Has a valid quick-method election been accepted? Obtain eligibility population/associates, prior quarters, revenue type, goods-purchase proportion, annual credit used and special capital transactions. Do not guess an election from a bank statement.
8. What bad debts written off, subsequent recoveries, returned goods, credit notes, errors, net-tax adjustments, tax rebates and actual instalment/payment dates exist? Obtain consent/authority and accepted filing/payment receipts for subsequent human action.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure and actual population/condition | Official source |
|---|---|---|
| Ordinary QST | 9.975% of the supported price excluding GST, not HST or tax-on-tax | [RQ taxable supply rule](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/) |
| Ordinary GST comparator | 5% where that federal ordinary supply rule applies; assess HST/place and exemptions independently | [RQ separate tax rates](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/) |
| Ordinary small-supplier threshold |30,000 worldwide taxable supplies including zero-rated and associates, with statutory exclusions and separate single/four-quarter timing | [RQ small-supplier scope](https://www-prd.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/registering-for-the-gst-and-qst/small-suppliers/) |
| General assigned annual frequency | Annual taxable sales 1,500,000 or less; permitted more-frequent election and special entity rules | [IN-203 filing-frequency table](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf) |
| General assigned quarterly frequency | Over 1,500,000 through 6,000,000 inclusive; actual account and monthly-election route | [IN-203 frequency table](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf) |
| General assigned monthly frequency | Over 6,000,000; not the exact lower boundary | [IN-203 frequency table](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf) |
| Quick-method sales ceiling |400,000 including GST/HST; 418,952 including QST, with actual worldwide/associate/four-of-five-quarter population | [RQ eligibility](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/the-quick-method-of-accounting-for-calculating-gst-and-qst-remittances/who-can-use-the-quick-method/) |
| Quick-method QST goods route | 3.4% of eligible QST-inclusive Quebec sales for qualifying resale businesses meeting the 40% goods-cost condition | [RQ rates and goods test](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/) |
| Quick-method QST other eligible route | 6.6% of eligible QST-inclusive Quebec sales, often services; eligibility exclusions remain | [RQ actual rates](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/) |
| Quick-method QST reduction | 1% on first 31,421 QST-inclusive eligible sales in the fiscal-year credit population, not 30,000 or a fresh limit each return | [RQ annual credit and cumulative examples](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/) |

### Establish registration, period and supply population

Use the actual registration date/system. The ordinary small-supplier test includes associates' worldwide taxable and zero-rated supplies; it excludes the stated tax, financial-service and capital-property amounts. A single-quarter crossing causes immediate loss of small-supplier status and collection on the crossing supply; the rolling four-quarter route generally ends status after the following calendar month. Do not tax earlier supplies retroactively just because a later year exceeds a threshold. Voluntary registration, mandatory taxi/admission and specified-product/QST routes can change the result; the ordinary threshold is not an exemption for every trader. [Actual small-supplier timing](https://www-prd.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/registering-for-the-gst-and-qst/small-suppliers/), [registration exceptions](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/registering-for-the-gst-and-qst/).

Check actual general-system versus specified-system registration before input-credit or remote-sale conclusions. The non-resident-supplier route is not settled by an AWS/Google/Microsoft merchant name. Financial services, real property and non-resident/specified suppliers retain the original R-QC-QST 1-3 referral jobs. A wrong claim needs correction of its legal basis, not a fallback of 'taxable at 9.975%' or 'not registered' whenever unknown. [IN-203 system boundary and specified-supplier input treatment](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

QST ordinarily applies to taxable supplies made in Quebec at the applicable time. Goods delivery, recipient address, where a service is performed, special property/service rules and rights to use intangible property need actual place-of-supply evidence. The old 'services equal recipient location' shortcut was incomplete. Classify exempt, zero-rated and outside-Quebec supplies separately; 'out-of-province' is not automatically a zero-rated export. Exports and shipping outside Quebec require the actual category/recipient/documentation/exception. Keep federal place-of-supply separate, especially sales in HST provinces. [IN-203 place/export sections](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

Retain all original sale-pattern investigations:

- Ordinary supported goods/services generally use standard-rate treatment, with actual exclusions rather than a brand/category guess.
- Basic groceries and specified prescription drugs have conditional zero-rating, not all food/drug sales.
- Qualifying long-term residential rent and financial services can be exempt, with their own conditions; exempt inputs do not become ordinary commercial ITRs.
- Printed books require actual ISBN/printed-book criteria, with exclusions and bundled/electronic distinctions. A QST zero-rated book can remain federally taxable or subject to a separate eligible rebate.
- The old blanket **children's clothing zero-rating** is unsupported. IN-203 lists clothing/footwear as taxable, while qualifying children's diapers/training pants and specified accessories have their own QST zero-rating. Do not turn that limited rule into a general exemption for children's garments.

These jobs remain distinct in the sales register. [RQ actual taxable supplies](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/), [specific printed-book criteria](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/special-cases-gsthst-and-qst/printed-books/), [IN-203 supply categories](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

### Calculate collectible output tax and actual adjustments

For an ordinary exclusive-price taxable supply calculate price×0.09975. GST is not in that base. A 100 sale with ordinaryGST 5has QST 9.98 after appropriate invoice rounding, not 9.975% of 105. Reconcile actual invoice rounding and inclusive-price extraction instead of applying a rounded 10% rate. Tax collectible includes required collection/billed unpaid tax and specified deemed collections; it is not simply bank deposits. Amounts collected in error also need the actual return/correction route. [Actual tax base](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/), [return collectible-tax instruction](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

Keep discounts, returns, credits, bad debt/write-off and recoveries separate from normal sales. Preserve the original bad-debt investigation, but do not put it on the GST line 107as if that were QST. The detailed QST worksheet's 207 is a supported addition to recoverable ITR adjustments for actual eligible written-off debt; 204 adds tax on later recovery. Establish actual original reporting/remittance, reasonable write-off, partial collection, related-party and timing requirements before claiming. A bank reversal is not automatically a bad-debt deduction. No double recovery through both credit note and bad debt. [Actual return adjustments](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/), [IN-203 bad-debt section](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

### Determine each ITR from evidence and use

General-system ITRs recover eligible QST paid/payable for taxable or zero-rated commercial activities, subject to exact documentary, purchaser, timing and specific restrictions. Private use and exempt activities are not ordinary eligible inputs. Preserve office supplies/software, accounting/legal, meals, vehicle, home-office, personal and exempt-input pattern jobs. A supplier name/category or a bank line alone does not establish entitlement. [Actual ITR instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/), [IN-203 claim evidence/use rules](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

For ordinary operating services/non-capital personal property, actual use bands can yield nil at 10% or less, proportionate above 10% below 90%, and full at 90% or more. **Do not apply that table to every capital asset, vehicle or immovable.** Capital movable property, immovables, passenger vehicles/aircraft, individuals/partnerships, financial institutions and PSBs have different rules and change-of-use consequences. Operating motor expenses and asset acquisition/CCA-based claims are different. Home-office entitlement also requires actual business-place/use criteria and supported reasonable allocation; floor area alone does not prove every household bill qualifies. [Actual IN-203 operating/capital/home-office sections](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

Obtain required invoice information under the actual amount/document rule; the old assertion that every possible invoice must always show a supplier's QST number ignored those distinctions. Validate material supplier registration where required. QST charged by a **specified-system** supplier to a general-system registrant generally must be corrected/refunded by the supplier; it is not automatically an ITR. Retain the actual supplier/general-system status rather than claim all tax with 'QST'on the receipt. [Actual IN-203 supporting-document and specified-supplier rules](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

General ITR claim time is four years from the relevant return filing deadline, with the actual shorter two-year classes and exceptions. Do not give every entity a four-year safe harbour. Establish first eligible period, prior claims and claimant category. A new registrant, reimbursed expense, capital asset or rebate may have separate rules. [IN-203 claim timing](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf), [actual return general period](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

Meals/entertainment ordinarily permit half of eligible tax, but the original 'never more than 50%' rule was overbroad. Actual truck-driver, charity/public-institution and other exceptions require their specific facts. Quebec's revenue ceiling can restrict RTI s further: use 2% up to 32,500 revenue, 650 between 32,500 and 52,000, and 1.25% at 52,000 or above. Supported methods can claim the full amount during the year with the required later adjustment, or the allowed half currently; do not treat a temporary full claim under the actual adjustment method as automatically erroneous. [Actual RQ meals/RTI methods and ceiling](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/situations-particulieres-liees-a-la-tpstvh-et-a-la-tvq/frais-de-repas-et-de-representation-cti-et-rti/).

### Imported goods/services and foreign SaaS

Establish transaction type, import/place, actual vendor's registration/carrying-on-business status, collection already made and commercial use. IN-203 describes exceptions where imported services/intangible property acquired exclusively, generally 90% or more, for commercial activities do not require the generic self-assessment. Goods brought into Quebec by a registrant with the applicable exclusive-commercial/ITR conditions also have their actual exception. **Do not automatically self-assess every foreign cloud subscription** or every supplier outside Quebec. Partial/exempt/personal use, a financial institution, specified/general system and actual taxable import can change the route. [Actual IN-203 imports section, pages 63-64](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

If QST is actually due, use the real return line/system. Detailed general-system line 203 includes specified taxable property/services brought into Quebec; property/emission-allowance acquisition and special-purpose/non-registrant routes have distinct fields/forms. The old 'foreignSaaSline 104' was a federal/QST field error and liability shortcut. Do not manufacture an equal self-assessment/ITR pair solely to force zero tax. Retain actual scope, use, vendor and source reasoning, and refer uncertain registration/import cases. [Actual current return and import instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

### Transfer the workpaper to the actual return

Retain the Excel/working-paper job as the following reconciliation, with **GST and QST separate columns** even where the actual return is joint:

1. Tax-exclusive supplies reconciled to the books and supporting classification; actual detailed line 101 is total supplies, not QST collected. Quick method has its own inclusive-sales convention.
2. QST collectible at 203 and supported positive net-tax adjustments 204; the workpaper output subtotal.
3. Eligible ITRs 206 and supported deductible adjustments 207; the workpaper input subtotal.
4. Net QST 209 equals the output subtotal minus the input subtotal; actual instalments 210 and eligible rebates 211 with their restrictions, then the actual net-balance field 213.
5. Where relevant, separately report 214taxable immovable/emission allowance, self-assessment/special-purpose details and final 216 calculation under the actual current form; specialist property/financial rules are not inferred from this ordinary outline.

Use the latest actual form/account instructions to transfer and verify every box. The old mapping 101 tax/104 QST adjustments/106 ITR/111 net/114balanceis not a valid general QST return layout. Nor is VD-403 the ordinary return: the observed VD-403.E is a separate new-vehicle-export rebate. Never renumber a GST field to QST by habit or combine tax amounts in a way that loses audit trails. [Actual FPZ-2034.G-V line instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

Joint GST/QST filing and an authorised offset of one tax's refund against the other's debt are permitted subject to actual accounts/debt/unfiled-return conditions. That does not turn tax rates, input-credit entitlements or supplies into a single blended tax. Reconcile each tax first, then the permitted payment/refund allocation. A draft net refund is not proof it has been approved or paid. [Actual joint-return/offset conditions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

For bank-statement intake retain the original Desjardins CSV, RBC/TD/BMO/Scotiabank CSV/PDF and National Bank CSV jobs as **possible import formats**, not a promise every bank export has one fixed schema. Identify date, description, debit/withdrawal, credit/deposit, signed amount, currency and opening/closing balance from the actual file. Preserve raw exports and reconcile totals/transfers/duplicates/refunds before invoice/tax classification. A debit is not automatically an ITR and a deposit is not automatically a taxable sale. Unsupported CSV column names stay a parser check, not official tax evidence.

### Quick method is a separate elected computation

Check written accepted election, exact worldwide/associate/quarter population and ineligible entities. Accounting, legal, actuarial, fiscal/financial consulting, bookkeeping and tax-return preparation businesses are among the exclusions; 'small service business' is not universal eligibility. The actual QST inclusive ceiling differs from GST/HST inclusive ceiling. Use actual ordinary sale collection first: quick remittance rates are **not customer tax rates**. [RQ eligibility](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/the-quick-method-of-accounting-for-calculating-gst-and-qst-remittances/who-can-use-the-quick-method/), [actual current rate method](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/).

The old goods/services remittance rates were reversed: qualifying retail/wholesale goods use 3.4% QST, other eligible route commonly services 6.6%. The goods-cost 40% condition and exclusions matter. Apply each to eligible QST-inclusive Quebec sales, excluding the actual zero-rated, capital/immovable and other excluded populations; capital transactions generally remit actual tax and eligible capital ITRs separately. Operating ITRs are ordinarily already reflected in the quick rate, so do not deduct them again. Keep annual credit used and election/revocation/deadline evidence. [Actual RQ rates and goods condition](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/), [IN-203 quick-method scope/election](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

The detailed rate page and IN-203 say the 1% reduction is on the first 31,421 QST-inclusive eligible sales **per fiscal year**, used cumulatively across returns, with no unused annual carryforward. FPZ-2034.G-V line 207 wording says 'for each period', which can misleadingly suggest a fresh limit each return. The Act could not be read to settle a material conflicting claim; record both sources and **do not reset the cap each period** or finalise a disputed enhanced claim without that law check. The bounded examples below supply a supported available annual balance rather than infer a new allowance. [Detailed annual rule and cumulative example](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/), [conflicting field wording](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

### Filing, payment, records and penalties

Use actual assigned/elected frequency. The general annual-sales threshold table includes the exact 1.5 millionannual boundary, excludes it from quarterly, and includes 6 millionquarterly. Actual expected Canadian taxable sales/associates/confirmation determine assignment; charity/garment manufacturer and designated reporting-period rules differ. Do not skip nil returns merely because no tax is owed without an actual approved designated period. [Current assignment/filing guidance](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/filing-frequency/), [IN-203 frequency table/special classes](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

Monthly/quarterly returns are due one month after period-end; ordinary annual returns generally three months after year-end. A qualifying individual with business income and 31 December annual fiscal year files by 15 June but pays any balance by 30 April. This is not all annual filers or all personal property-income cases. Calendar 2026 individual return would ordinarily file 15 June 2027/pay 30 April 2027 subject to actual holiday rules and account. Required annual instalments have a separate current/prior net-tax test; filing extension does not defer quarterly payments. [Actual date/population rule](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/filing-frequency/).

Actual IN-203 annual instalment duty uses both current estimated and previous-year net tax at least 3,000 for each tax separately; quarterly instalments are due the last day of the following month. Reconcile actual amount paid rather than deduct an estimate as if settled. Keep tax due, bank processing/authority receipt and accepted submission distinct. [Actual filing/instalment schedule](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/filing-frequency/), [IN-203 instalment population](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

Current ordinary registrants generally file electronically for periods beginning after 2023, with the actual charity exception. Use current MyAccount/authorised financial-institution channel, right account/period and actual required supplementary-return submission. Payments 10,000 or more normally require electronic means with actual exception. A saved draft, successful login or ledger posting does not prove filing or payment. Return receipt and payment processing have different actual dates; account for bank processing. [Actual current instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/), [IN-203 electronic rules](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf).

Maintain supporting invoices, registration/election/use calculations, exports, adjustments and readable original electronic records. General retention is six years after the last related year, with actual late/dispute/asset/carryover extensions where required. Current FPZ guide distinguishes Quebec late-filing 25/day, maximum 2,500, failure-to-collect 15%, and late-remittance 7/11/15% by duration, from separate federal GST late-return rules. Do not copy income-tax penalties to QST or promise every error incurs all sanctions. Current interest periods and case-specific relief require actual applicable rules; no invented fixed 2026 interest rate. [Actual return penalties/receipt/records](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

## Worked cases

### Case 1: original ordinary quarterly example, now with actual QST fields

Retain the original 25,000 standard-rate sales, 2,000 supported zero-rated sales and 600 eligible documented QST ITRs. Assume ordinary general-system method, all amounts exclusive, no adjustments/instalments/other rebates and actual proper period. QST 203 is 2,493.75; 206 is 600; net 209 is **1,893.75 owing**. Line 101 includes 27,000 supplies for this stated no other-sales case; zero-rated does not mean exempt or erase the underlying sales record. [Actual base and rates](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/), [actual field meaning](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

```oa-check
name: Quebec ordinary quarterly original amounts with correct QST field mapping
inputs:
  standard_rate_sales: 25000
  supported_zero_rated_sales: 2000
  eligible_documented_itrs: 600
steps:
  - tax_exclusive_supplies_101: standard_rate_sales + supported_zero_rated_sales
  - qst_collectible_203: standard_rate_sales * 0.09975
  - eligible_itrs_206: eligible_documented_itrs
  - net_qst_209: qst_collectible_203 - eligible_itrs_206
expected:
  tax_exclusive_supplies_101: 27000
  qst_collectible_203: 2493.75
  eligible_itrs_206: 600
  net_qst_209: 1893.75
```

### Case 2: original exporter/refund scenario

Retain 5,000 standard sales, 40, 000 exports and 1,500 eligible QST expenses. Explicitly establish all export zero-rating/place/document conditions and ITR entitlement first, ordinary method, no adjustments. Collectible 498.75 minus 1,500 gives **minus 1,001.25**, a refund position. A foreign address by itself would not establish that classification. No acceptance/payment is implied. [Export/ITR scope](https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf), [return mapping](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

```oa-check
name: Quebec original supported exporter refund scenario
inputs:
  standard_rate_sales: 5000
  independently_supported_zero_rated_exports: 40000
  eligible_itrs: 1500
steps:
  - total_supplies_101: standard_rate_sales + independently_supported_zero_rated_exports
  - qst_collectible_203: standard_rate_sales * 0.09975
  - net_qst_209: qst_collectible_203 - eligible_itrs
expected:
  total_supplies_101: 45000
  qst_collectible_203: 498.75
  net_qst_209: -1001.25
```

### Case 3: original meals example under explicit ordinary restrictions

Retain 2,000 business meals and 199.50 QST. Assume actually eligible ordinary meals, sufficient remaining annual Quebec revenue ceiling, no exception, no earlier full claim and current-half method. ITR **99.75**. If the ceiling, individual use or exception differs, recompute; the old unconditional result is not universal. [Actual meals/RTI methods](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/situations-particulieres-liees-a-la-tpstvh-et-a-la-tvq/frais-de-repas-et-de-representation-cti-et-rti/).

```oa-check
name: Quebec original meals ordinary half-claim scenario
inputs:
  supported_eligible_meals_price: 2000
steps:
  - qst_on_invoice: supported_eligible_meals_price * 0.09975
  - current_half_itr: qst_on_invoice * 0.5
expected:
  qst_on_invoice: 199.50
  current_half_itr: 99.75
```

### Case 4: quick remittance service route is 6.6%, not 3.4%

Assume a fully eligible elected cleaning business on the ordinary service quick route, eligible Quebec QST-inclusive sales 21,995, verified first-year-period credit capacity at least that amount, no other eligible capital ITR/transaction/adjustment. Remittance 21, 995×6.6%=1,451.67; reduction 219.95; net **1,231.72**. The customer's tax is still collected at the ordinary actual supply rate. Do not add operating ITRs or reset the annual cap next quarter. [RQ actual service rate and cumulative example](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/).

```oa-check
name: Quebec quick-method eligible cleaning-service scenario
inputs:
  eligible_qst_inclusive_sales: 21995
  verified_remaining_annual_reduction_base: 31421
steps:
  - before_reduction: round(eligible_qst_inclusive_sales * 0.066, 2)
  - permitted_reduction: round(min(eligible_qst_inclusive_sales, verified_remaining_annual_reduction_base) * 0.01, 2)
  - net_quick_qst: before_reduction - permitted_reduction
expected:
  before_reduction: 1451.67
  permitted_reduction: 219.95
  net_quick_qst: 1231.72
```

## When to refuse or refer

- **R-QC-QST-1:** financial services/institution status, allocation or special-import rules; 'financial services are not settled by an ordinary invoice pattern.
- **R-QC-QST-2:** real property, self-supply, new-housing/rental rebate, change of use or emission allowances. Prepare the facts and use the actual specialist form/rule.
- **R-QC-QST-3:** non-resident/specified-system/platform suppliers, outside-Quebec registration/place and uncertain imports. Do not universally impose specified registration or self-assessment.

Refer disputed classification/source, materially missing invoice/use/registration evidence, special claimant/election, period/claim-deadline or actual penalty/appeal issue. Complete supported workpaper rows and name the unresolved determination instead of defaulting every unknown sale to tax or every unverified input to permanently zero. Nounsupported zero-rating, duplicate ITR, mixed tax base, fictional form, false accepted return or definitive filing advice.

## Completion checklist

- Actual legal entity/general-versus-specified registration dates/numbers and independent GST/QST accounts.
- Assigned/elected period and actual expected taxable-sales population; correct individual annual filing/payment split.
- All original sales patterns retained, actual place/supply/exemption/export evidence, no blanket zero-rating of children's clothing.
- Collectible rather than just cash tax, GST excludedQSTbase, actual invoice/inclusive-price rounding.
- All original input/vehicle/home-office/meal/use/evidence jobs, correct ordinary/capital/exception table and claim clock.
- ForeignSaaSactual vendor/use/import exception, not automatic self-assessment or line 104.
- Actual current QST 203/204/206/207/209/210/211/213 andotherrequiredfields, distinct federal columns, permitted joint filing/offset only after reconciliation.
- Electedquick method eligibility, correctgoods/services rates/inclusivepopulation/annual credit use; no operatingITRdouble claim.
- Raw bank import and invoice-ledger audit trail, baddebts/returns/recovery/instalment receipts.
- Human review/authority, actualaccepted filing/payment, readable records; proposed journal/import file only until authorised.

## Sources

| Official source actually read and scope | URL | Read on |
|---|---|---|
| Read for current ordinary tax rates/base and taxable-category boundary, not every exemption | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/ |2026-11-14|
| Read for ordinary small-supplier worldwide/associate/population and single-versus-four-quarter commencement, voluntary and mandatory exceptions | [official source](https://www-prd.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/registering-for-the-gst-and-qst/small-suppliers/), [official source](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/registering-for-the-gst-and-qst/) |2026-11-14|
| Read for actual FPZ-2034.G-V 2026-09 scope, joint/offset, field instructions, receipt, filing, records, penalties and separate special-purpose parts; not all specialist eligibility | https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/ |2026-11-14|
| Read for bounded IN-203-V 2026-03 supply/place/import, documentary/use/operating/capital/home office, claims, frequency, instalment, quick/electronic and meal distinctions; not the entire 92 page guide | https://www.revenuquebec.ca/documents/en/publications/in/IN-203-V(2026-03).pdf |2026-11-14|
| Read for complete assigned/expected-sale population and filing/payment/instalment schedule, with qualifying individual annual exception | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/filing-frequency/ |2026-11-14|
| Read for actual quick eligibility/population/exclusions; detailed French rates/40% goods criterion/annual credit and cumulative examples read separately | [official source](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/the-quick-method-of-accounting-for-calculating-gst-and-qst-remittances/who-can-use-the-quick-method/), [official source](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/) |2026-11-14|
| Read for actual printed-book ISBN/physical/excluded/bundled/electronic criteria, not every book-rebate claim | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/special-cases-gsthst-and-qst/printed-books/ |2026-11-14|
| Read for actual ordinary meal RTI method, revenue cap and exception boundary | https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/situations-particulieres-liees-a-la-tpstvh-et-a-la-tvq/frais-de-repas-et-de-representation-cti-et-rti/ |2026-11-14|

Not yet confirmed: current underlying QST Act consolidation/precise articles (retrieval 403/502); every exceptional/non-resident/platform/financial/property and special-claimant rule; actual service/intangible/export/children-product classification and place; full asset/vehicle/home-office and two-year ITR exception details for each claimant; currency conversion/rounding choice; each bad-debt/return/credit-note timing condition; current prescribed interest and case-specific penalty/relief. FPZ-2034.G-V line 207 says 'for each period' versus detailed quick-rate page/IN-203 annual cumulative credit; controlling law could not be read, so a disputed claim is held and no fresh per-period cap is assumed. Actual bank export schemas remain file-specific. Official guide PDF/HTML web text was read with bounded scopes; all attempted local QST source downloads failed 403, so no offline PDF cache, full Act read or visual PDF review is claimed. No approval/name is added or removed.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `qc-qst-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/qc-qst-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
