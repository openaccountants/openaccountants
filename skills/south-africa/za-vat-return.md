---
name: za-vat-return
description: >
  Use this South Africa VAT return reference whenever asked about South African
  VAT returns for self-employed individuals or small businesses. Trigger on
  phrases like South Africa VAT, VAT201, SARS VAT, 15% VAT, eFiling VAT,
  zero-rated SA, VAT vendor, or any question about VAT filing, computation or
  registration for vendors in South Africa. Covers the enacted 15% rate,
  zero-rated and exempt supplies, the VAT201 return and bimonthly filing via
  SARS eFiling. The Act read prints R1 million and R50,000; R2.3 million and
  R120,000 are what SARS says it is administering from 1 April 2026, and they
  sit in Bill B34-2026, not in any Act read at 5 November 2026. ALWAYS read this
  skill before touching any South African VAT work. This Tier 2 draft supports
  source checking and reviewer questions; it does not authorise filing, payment
  or a tax position.
version: 2.3
jurisdiction: ZA
tax_year: 2026
tax_year_notes: "VAT tax periods in calendar 2026, read at 5 November 2026. VAT has no year of assessment: the Act applies period by period under s 27. Rate 15% enacted. R2.3 million and R120,000 are announced, administered by SARS from 1 April 2026 and in Bill B34-2026, not enacted in any Act read; the Act read prints R1 million and R50,000."
last_updated: 2026-11-05
depends_on:
  - vat-workflow-base
  - south-africa-vat
job: vat-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
---

# ZA VAT Return v2.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Self-employed individuals and small businesses that are vendors, or may have to register, under the Value-Added Tax Act 89 of 1991 ('the VAT Act'), and the reviewers working with them. The tax is administered by the South African Revenue Service (SARS). Supporting law is the Tax Administration Act 28 of 2011 (TAA). Currency is the South African rand (ZAR, R) only. The return is the VAT201, filed on SARS eFiling (https://www.sarsefiling.co.za). A legacy note in this guide said the `efiling.sars.gov.za` form of the address does not resolve; that was not tested in this conversion.

Figures apply to VAT tax periods in calendar 2026, read at 5 November 2026. VAT has no year of assessment; each vendor's periods come from s 27.

### What this file is

This is the return workflow file for South Africa (`job: vat-return`), a country slot file for `vat-workflow-base`. The base owns the workflow, output specification, question form and self-checks. Its status is Tier 2, pending review. It was contributed by the Open Accountants Community. No statement here has been approved by an accountant.

The sibling guide `south-africa-vat` (`job: vat-reference`) holds the wider law. This file does not repeat these, and they are not ruled out by being left out: the full limbs of s 11 and s 12 and Schedule 2 Part B item by item, the registration tests in s 23 in detail, the time of supply rules beyond those below, the rest of the s 17(2) detail, the s 18 formulas, s 22(3), the commercial accommodation threshold row, and the s 7(4) litigation. The 2 files use the same refusal codes R-ZA-1 to R-ZA-5. R-ZA-6 to R-ZA-8 apply to this return workflow only: they carry the legacy refusals and are limits of this workflow, not rules of law, so an answer in `south-africa-vat` does not lift them here. The split is provisional: one job in one country has one skill, so the owner may retire one file with an alias.

**Operational hold.** `vat-workflow-base` Step 1 requires a regional or directive layer as well as this file. None for South Africa was found in this repository at 5 November 2026, so Step 1 stops the workflow. Use this file as a reference only. Stop before producing a workbook, return or filing instruction until a regional layer or an approved non-EU exception exists.

Every classification is a working paper for reviewer checking. Input tax needs a document s 16(2) accepts, usually a valid s 20 tax invoice; treat all credits as provisional until it is checked.

### How to read the amounts

The words below carry a fixed meaning in this file.

- **Enacted:** printed in the VAT Act text read, or in an Act read.
- **Announced:** stated in the 2026 Budget. An announcement is not law.
- **Administered:** what SARS says it is administering, in the source named.
- **Bill:** in a Bill before Parliament. A Bill is not law.

Where these differ, both are shown. Do not merge them into a single current figure.

### Refusals and boundaries

These are the country refusals for `vat-workflow-base`. If a trigger fires, stop, output the message verbatim and end, as Step 5 of the base requires. There is no partial classification.

- **R-ZA-1, registration not confirmed.** Trigger: the profile does not show that the person is registered. Message: 'VAT registration is not confirmed. A vendor under section 1(1) is any person who is or is required to be registered, so a person required to register is liable even if unregistered. Confirm whether the person is registered or required to be registered, and from what date. This workflow cannot complete the return until that is confirmed.'
- **R-ZA-2, partial exemption and apportionment.** Trigger: an item is acquired or imported partly for making taxable supplies and partly for another intended use, such as exempt supplies, private use or another non-taxable purpose; tax on it or a notional input amount would be input tax to the extent of taxable use, with no s 17(2) denial; and its intended use in making taxable supplies is below 95% of its total intended use (s 17(1) and proviso (i)). The test runs item by item, not on the vendor's exempt share. A percentage the vendor supplies is not a ratio from an authorised method, so it cannot replace this stop. An item wholly for one use is directly attributed and does not fire it. Tax self-assessed on imported services does not fire it either: s 1 input tax does not include tax under s 7(1)(c), so no apportionment arises on that tax (see Imported services under Cross-border points). Interest alone does not fire it: BGR 16 leaves interest on a current account used for day-to-day operations and interest from SARS out of its formula, and other interest fires it only through an item acquired partly for it. Message: 'This item is used partly for taxable supplies and partly for another purpose, below the 95% test, so input tax must be apportioned under section 17(1) by a ratio from a method the Commissioner has authorised. This workflow cannot complete the return. Refer it to a CA(SA) or a registered tax practitioner.'
- **R-ZA-3, s 18 adjustments.** Trigger: a s 18 adjustment is needed, other than output tax on s 18(3) benefits, which is computed here. South Africa has no capital goods scheme of the EU kind. Message: 'This return needs a section 18 adjustment, which this workflow does not compute. This workflow cannot complete the return. Refer it to a CA(SA) or a registered tax practitioner.'
- **R-ZA-4, financial services.** Trigger: the vendor is a bank, an insurer, or a vendor whose main business is s 2 financial services (a working test, not a statutory one). Message: 'Banks, insurers and financial institutions need specialist handling under section 2. This workflow cannot complete the return. Refer it to a CA(SA) or a registered tax practitioner.'
- **R-ZA-5, property.** Trigger: the period includes a sale or purchase of fixed property or a going concern. Ordinary rent is not a trigger: use the rent rows. No option to tax appears in the Act read. Message: 'This property or going concern transaction is highly fact-sensitive. This workflow cannot complete the return. Refer it to a CA(SA) or a registered tax practitioner.'
- **R-ZA-6, cross-border services and customs VAT.** Trigger: the treatment of a cross-border service under s 11(2) or the 'imported services' definition cannot be settled from the contract and invoice, or the period has customs VAT other than an input claim backed by a bill of entry and payment receipt. Message: 'This cross-border or customs item needs specialist review. This workflow cannot complete the return. Refer it to a CA(SA) or a registered tax practitioner.'
- **R-ZA-7, branch or group registration.** Trigger: the vendor has, or wants, a separate registration for a branch, division or separate enterprise under s 50, or a branch registration for a foreign group member under s 23(2A). The sections read contain no VAT group registration of the UK kind; these are the nearest provisions read. Message: 'Branch and group registrations are outside this workflow. This workflow cannot complete the return. Refer it to a CA(SA) or a registered tax practitioner.'
- **R-ZA-8, construction and financial instruments.** Trigger: the period includes a contract under which the vendor builds, alters or repairs a building or other fixed works (a working test, not a statutory one), or dealing in financial instruments by a vendor outside R-ZA-4. Message: 'This transaction needs specialist review. This workflow cannot complete the return. Refer it to a CA(SA) or a registered tax practitioner.'

### Working limits

Kept from the prior version with their corrections.

- Never claim input tax on exempt supplies. Only taxable supplies, including zero-rated supplies, qualify.
- Never confuse zero-rated (input tax claimable) with exempt (input tax not claimable).
- Never charge VAT if not registered as a vendor, and see R-ZA-1 for a person required to register.
- Never use a rate other than 15% for standard-rated supplies.
- Never claim input tax without a document s 16(2) accepts. The prior wording, 'a valid tax invoice (for supplies over R50)', was too narrow.
- Never ignore a filing deadline. The 10% penalty attaches to late payment; for a late return alone see Penalties and interest. The prior wording, 'penalties apply from the first day late', was wider than that.
- Never apply the payments basis without the Commissioner's direction, unless s 15(2B) applies.
- Never claim notional input tax on second-hand goods without the s 20(8) records and proof of payment.
- Never claim input on the supply (purchase, lease, rental) of a motor car as defined, unless a proviso to s 17(2)(c) applies.
- Never claim input on entertainment unless a proviso to s 17(2)(a) applies. The test is that proviso, not whether the vendor is 'in the business of providing entertainment'.
- Never exclude a bank service fee as exempt where the fee proviso to s 2(1) applies.
- Never omit output tax on Seventh Schedule fringe benefits under s 18(3).
- Never present calculations as definitive. Always label them as estimated and direct the client to a SARS-registered tax practitioner, or a CA(SA).

### Required inputs

| Level | Items | Policy |
| --- | --- | --- |
| Minimum viable | Bank statement for the VAT period in CSV, PDF or pasted text, confirmation of registration, and the VAT registration number | HARD STOP without the statement or the registration fact |
| Recommended | Sales invoices, purchase invoices showing VAT, the prior period VAT201 | SOFT WARN |
| Ideal | Complete invoice register, confirmation of the filing category, prior year VAT reconciliation, debtors and creditors lists, bills of entry and the asset register | SOFT WARN |

Say: 'Input tax credits require a document section 16(2) of the VAT Act accepts, usually a valid section 20 tax invoice. All credits are provisional pending verification of that document.'

The VAT registration number is a 10-digit number allocated by SARS (VAT201 guide). Confirm a supplier's registration with the SARS VAT vendor search.

## Rates, bands and thresholds

Each row leads with the official source. 'Read in' names the unofficial consolidation where the provision's words were read; see the limit under Sources.

| Item | Amount or rule | Position at 5 November 2026 | Source and limit |
| --- | --- | --- | --- |
| Standard rate | 15% | Enacted. The announced rise did not take effect: Act 3 of 2026, s 13(1), assented 31 March 2026, Gazette 54446 of 1 April 2026. SARS's rates guide gives 15% from 1 April 2018. | [Act 3 of 2026](https://www.sars.gov.za/legal-lprim-aa-2026-01-rates-and-monetary-amounts-and-amendment-of-revenue-laws-act-3-of-2026-gg-54446-1-april-2026/); [SARS rates guide](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-Gen02-Guide-for-Tax-Rates-Duties-Levies.pdf). Section 7(1) read in the unofficial consolidation. |
| Reduced rates | None. Supplies are standard-rated, zero-rated or exempt. | Enacted | [SARS VAT 404](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf). Sections 7, 11 and 12 read in the unofficial consolidation. |
| Zero rate | 0% | Enacted | same |
| Tax fraction at 15% | 15/115 | Enacted | [SARS VAT201 guide](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-ELEC-04-G01-Guide-for-completing-the-Value-Added-Tax-VAT201-Declaration-External-Guide.pdf), r/(100+r) |
| Compulsory registration | R1,000,000 (s 23(1)(a), (1)(b), (1A)) | Not changed by an Act read. Announced R2,300,000 from 1 April 2026; administered by SARS on new applications from that date; Bill B34-2026 clause 21, deemed from 1 April 2026. | [B34-2026](https://www.sars.gov.za/legal-lprep-bills-2026-03-rates-and-monetary-amounts-and-amendment-of-revenue-laws-bill-b34-2026-21-october-2026/), which reprints R1 million as the current text; [SARS Budget 2026 FAQ](https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/). Section 23 read in the unofficial consolidation. |
| Voluntary registration | R50,000 (s 23(3)(b)) | Not changed by an Act read. Announced R120,000 from 1 April 2026; SARS FAQ applies it; Bill B34-2026 clause 21. | same |
| Long-stay accommodation | 60% of an all-inclusive charge for an unbroken period exceeding 28 days | Enacted (s 10(10)) | [SARS VAT201 guide](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-ELEC-04-G01-Guide-for-completing-the-Value-Added-Tax-VAT201-Declaration-External-Guide.pdf), Field 6. Section 10 read in the unofficial consolidation. |
| Category C compulsory | Above R30,000,000 in any consecutive 12 months, actual or likely | Enacted | [SARS tax periods page](https://www.sars.gov.za/types-of-tax/value-added-tax/tax-periods-for-vat-vendors/) |
| Category D farming | SARS: less than R1,500,000 for 12 months. The consolidation of s 27(4)(a) prints R1,250,000. | SARS's statement is shown. The difference is held. | same |
| Category F | unverified: R1,200,000 in the consolidation of s 27(4B) only. SARS's tax periods page lists 5 categories, A to E. | Held | No official text read |
| Payments basis, natural person | Taxable supplies not above R2,500,000 | Enacted (s 15(2)(b)) | [SARS VAT 404](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf), Chapter 4. Section 15 read in the unofficial consolidation. |
| Payments basis, large supply | Consideration in money of R100,000 or more goes on the invoice basis, except fixed property and the vendors s 15(2A) lists | Enacted | same |
| Payments to invoice basis, s 23(3)(b)(ii) registrant | R50,000 (s 15(2B), proviso) | Enacted. Bill B34-2026 clause 21 as read amends s 23 and does not change this amount. | same |
| Full tax invoice | Consideration in money above R5,000 (s 20(4)) | Enacted | [SARS VAT 404](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf). Section 20 read in the unofficial consolidation. |
| Abridged tax invoice | Consideration in money not above R5,000 (s 20(5)) | Enacted | same |
| No tax invoice needed | Total consideration in money not above R50 (s 20(6)), with a document acceptable to the Commissioner | Enacted | same |
| Imported services de minimis | Value not above R100 per invoice (s 14(5)(e)) | Enacted | [SARS VAT-ELEC-01-G01](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/VAT-ELEC-01-G01-Manage-Value-Added-Tax-on-Imported-Services-External-Guide.pdf) |
| Late payment penalty | 10% of the tax paid late (VAT Act s 39(1); TAA s 213) | Enacted | [SARS FAQs for VAT vendors](https://www.sars.gov.za/types-of-tax/value-added-tax/faqs-for-vat-vendors/) |
| Interest on late VAT | 10.50% a year from 1 September 2026; 10.25% from 1 March to 31 August 2026 | SARS Table 1. Read the current table for later periods. | [SARS Table 1](https://www.sars.gov.za/wp-content/uploads/Legal/Rates/Legal-Pub-IRT-01-Interest-Rates-Table-1.pdf) |

**Thresholds.** No Act read changes s 23. SARS says: 'Although the amendments have not yet been promulgated, the Minister of Finance announced these amendments to be effective from 1 April 2026', and that it is administering new applications on the increased threshold. B34-2026 was introduced on 21 October 2026 and is not law on the sources read. Where the result differs between the amounts, show both and flag the gap:

- Above R1,000,000 and not above R2,300,000 of taxable supplies in the 12 months: compulsory on the Act as printed; SARS says it is not administering new applications that way from 1 April 2026. Refer to the reviewer. Do not state either result as settled.
- Above R50,000 and not above R120,000: voluntary on the Act as printed; below the threshold SARS says it is administering. Refer to the reviewer.

The test counts one person's taxable supplies, including zero-rated supplies, across all that person's enterprises, excluding tax, exempt supplies and s 11(2)(n) services. The legacy words 'in any 12-month period' were looser than s 23(1)(a), which looks at the 12 months ending at the end of a month.

**Zero rate, s 11.** Each limb needs the proof s 11(3) requires. Covered here, with the words used in the prior version:

- Exports of goods, s 11(1)(a), with the Export Regulation (GN R. 316 of 2014) documents.
- Services to a non-resident, s 11(2)(l), with its exceptions under Cross-border points. The legacy phrase 'to a non-resident outside SA' was narrower and looser than the paragraph.
- Basic foodstuffs: s 11(1)(j) and Part B of Schedule 2, item by item. The goods must match the item's wording. Brown bread, maize meal, rice, raw hens' eggs and milk are listed on the terms of their items. Sardines in tins or cans are excluded by item 8, although the VAT201 guide's example list says 'Pilchards/ sardines'.
- Fuel levy goods, s 11(1)(h), with the Fuel Item Levy numbers it lists. The legacy words 'petrol/diesel' refer to these.
- International transport, s 11(2)(a).
- Agricultural inputs: farming goods in Part A of Schedule 2, s 11(1)(g), subject to its conditions.
- Going concern, s 11(1)(e): R-ZA-5.
- Gold to the South African Reserve Bank, the South African Mint Company or a registered bank, s 11(1)(f), in the listed forms.
- Illuminating kerosene (marked), s 11(1)(l). The legacy word was 'paraffin'; unmarked paraffin is not within it (VAT 404).

Other limbs of s 11(1) and s 11(2) are left to `south-africa-vat`. Municipal property rates are a zero-rated limb that this file does use: s 11(2)(w), under Municipal bills.

**Exempt, s 12.** No output tax, and no input tax on related costs. Report in Field 3. The paragraphs are: (a) financial services; (b) donated goods or services, and goods made with at least 80% donated materials by value, supplied by an association not for gain; (c) a dwelling under a letting agreement, retirement scheme rights of occupation, and employer lodging; (d) leasehold land used mainly for dwellings; (e) land outside South Africa; (f) services to members in managing a sectional title body corporate, share block company, retirement housing scheme or qualifying residential association; (g) passenger transport by road or railway; (h) educational services by the listed colleges, higher education institutions and approved public benefit organisations, related supplies to students, and supplies by registered schools, with the carve-out from 1 January 2026 set out in `south-africa-vat`; (i) employee organisations to members; (j) caring for children by a creche or after-school care centre; (k) goods supplied by a non-resident non-vendor, not entered for home consumption; (l) bargaining councils to members; and (m) registered political parties to members. The legacy 'recognised institutions' and 'childcare' were looser than (h) and (j).

**Financial services, s 2.** Interest, exchange margins and dealing in securities are s 2 services. The proviso to s 2(1) takes out paragraphs (a), (b), (c), (d), (f) and (o) to the extent the consideration is a fee, commission, merchant's discount or similar charge, excluding discounting cost. So a fee is standard-rated. Life insurance policies are s 2(1)(i) and the proviso does not reach them. Whether a legacy 'income-protection' premium is exempt turns on the policy: VAT 421 lists a disability policy as a long-term policy and, in its glossary, disability income replacement under accident and health cover. Read the policy; this is held.

## The base

Tax is levied on the consideration for a taxable supply in the course of an enterprise (s 7(1)(a)), on imported goods (s 7(1)(b)) and on imported services (s 7(1)(c)). Value follows s 10. Agents and principals follow s 54.

**Accounting basis, s 15.** The invoice basis is the default. The payments basis needs the Commissioner's direction on written application. It is open to the bodies in s 15(2)(a): public authorities; the listed water boards; municipal entities supplying electricity, gas, water, sewage or refuse services; municipalities; associations not for gain; electronic services suppliers and intermediaries; and the SABC. It is also open under s 15(2)(b) to a natural person, not a trustee, or an unincorporated body of only natural persons, within the amount in the rates table. A s 23(3)(b)(ii) registrant is on the payments basis from registration under s 15(2B). VAT117 is the change form.

**Change from payments to invoice basis.** The legacy trigger, 'when turnover exceeds R2,500,000', is one case. Under s 15(3) the Commissioner directs the invoice basis where the conditions in s 15(2) have ceased to be satisfied, or on the vendor's written application (s 15(3)(b)). A proviso disregards excess caused by cessation, replacing plant or abnormal circumstances. A vendor must notify the change within 21 days (s 25(c)) and, on any change of basis, furnish particulars in the prescribed form (s 15(4)). Output and input on the changeover follow s 15(5) to (7), with debtors and creditors lists under s 15(9), and the VAT201 guide puts the resulting adjustments in Fields 12 and 18. Flag for a tax practitioner.

**Time of supply, s 9.** The general rule is the earlier of an invoice being issued and any payment of consideration being received (s 9(1)). A deposit, other than on a returnable container, is not payment until the supplier applies it as consideration or it is forfeited (s 1, 'consideration'). Rental, progressive supplies, instalment credit agreements, fixed property, connected persons and deemed supplies have their own rules in `south-africa-vat`. On the payments basis, output follows payments actually received, subject to the R100,000 rule, and input follows s 16(3)(b).

### Conservative defaults

These apply the Tier 2 rule and the permitted factual defaults rule in `vat-workflow-base`. A default stands only where the law read fixes the result of the missing fact. Unknown rates, legal scope, counterparty jurisdiction or evidence conditions are otherwise Needs Input.

| Ambiguity | Default |
| --- | --- |
| Registration status unknown | Stop: R-ZA-1. Do not compute. |
| Accounting basis unknown | Needs Input. The law does not fix it from the bank data: a direction or s 15(2B) may apply. The legacy 'invoice basis' default is replaced. |
| Supply classification unknown | Needs Input. The legacy 'standard-rated at 15%' default is replaced, because a receipt can be zero-rated, exempt or no supply at all. |
| Unknown rate on a sale or purchase | Needs Input |
| Unknown counterparty country, or whether a sale is an export | Needs Input |
| Export shown, but s 11(3) documentary proof not held | Indirect export zero-rated by election under Part Two of the Export Regulations: reg 16 decides, see Cross-border points. Any other export: no zero rate. 15% under s 7(1)(a) only where the sale is verified as a supply in the course of the enterprise and not exempt under s 12. Disclose the missing proof, the zero-rated alternative and the output tax. Otherwise Needs Input. Unknown whether the export is indirect: Needs Input. |
| Business share of a mixed use item unknown | Needs Input. Section 17(1) allows input tax only to the extent of use in making taxable supplies, so the law read fixes neither 0% nor the full amount. |
| Vehicle type unknown, or whether an item is entertainment | Needs Input. Whether s 17(2)(c) or (a) applies depends on the s 1 definitions and, for a vehicle, the IN 82 test. |
| Item known to be a motor car as defined, or known to be entertainment, with no proviso shown | Denied under s 17(2)(c) or (a). For a motor car, business use does not matter. Disclose the fact and the proviso that would allow the input. Quantify the input tax denied only from evidence: the VAT the document shows, or the tax fraction of an amount confirmed as VAT-inclusive at the standard rate. Otherwise the denial stands and that amount is Needs Input; never apply the tax fraction to a zero-rated or mixed-rate total. |
| Unknown whether a document s 16(2) accepts is held | Needs Input. No deduction is entered until one is held: see Input tax documents. |
| Second-hand goods claim, records unknown | Needs Input. No deduction until the s 20(8) records and proof of payment are held (s 16(2)(c)). |
| Cross-border sale, unknown B2B or B2C | Needs Input |

### Red flag thresholds

Working review settings for the reviewer brief, not legal amounts. They match `south-africa-vat`.

| Flag | Value |
| --- | --- |
| HIGH single transaction | ZAR 50,000 |
| HIGH tax delta on a single default | ZAR 7,500 |
| MEDIUM counterparty concentration | More than 40% of output or input |
| MEDIUM conservative default count | More than 4 a period |
| LOW absolute net VAT position | ZAR 30,000 |
| Tier 2 question threshold | ZAR 0: no row is filtered on amount, as no South African floor was set |

### VAT201 fields

The source is the SARS VAT201 guide, GEN-ELEC-04-G01, revision 11, effective 12 May 2025. Valid codes for the working paper's box column are the fields below.

| Field | Meaning |
| --- | --- |
| 1 | Standard-rated supplies excluding capital goods and services and accommodation, VAT inclusive |
| 1A | Standard-rated capital goods and services, VAT inclusive, including assets on termination of registration |
| 2 | Zero-rated supplies excluding exported goods |
| 2A | Zero-rated exported goods; Customs Code mandatory |
| 3 | Exempt and non-supplies |
| 4 | Output tax on Field 1: Field 1 x r/(100+r), 15/115 at 15% |
| 4A | Output tax on Field 1A |
| 5 | Commercial accommodation for an unbroken period exceeding 28 days at an all-inclusive charge, VAT excluded (s 10(10)). A charge that is not all-inclusive goes to Field 1, VAT inclusive. The legacy '28+ days (value)' was wrong on both points. |
| 6 | Field 5 x 60% |
| 7 | Commercial accommodation not exceeding 28 days, VAT excluded. The legacy 'Field 6 x 15/115' was wrong. |
| 8 | Field 6 + Field 7 |
| 9 | Field 8 x r/100, the rate and not the tax fraction |
| 10 | Change in use and export of second-hand goods, consideration VAT inclusive |
| 11 | Field 10 x r/(100+r) |
| 12 | Other and imported services: debit notes issued, credit notes received, recovery of irrecoverable debts, barter, services imported for non-taxable supplies, going concern acquisition adjustments, change in accounting basis. Fringe benefit output goes here per VAT 404 Example 9. |
| 13 | Total output tax: 4 + 4A + 9 + 11 + 12 |
| 14 | Input tax on capital goods and services supplied to you |
| 14A | Input tax on capital goods imported; Customs Code and bill of entry |
| 15 | Input tax on other goods and services. The guide's examples include second-hand goods (notional input tax). |
| 15A | Input tax on other goods imported. Goods only: the legacy 'goods/services' was wider. |
| 16 | Change in use: goods previously non-taxable now taxable, or increased taxable use |
| 17 | Bad debts, invoice basis only |
| 18 | Other: credit notes issued, debit notes received, accounting basis change |
| 19 | Total input tax: 14 + 14A + 15 + 15A + 16 + 17 + 18 |
| 20 | Field 13 - Field 19. A minus sign means a refund. |
| 21 to 37 | Diesel refund fields, out of scope here. |
| 38 | Field 20 net of the diesel totals (Fields 25, 29, 33 and 37). Below zero means a refund. |

**Diesel refund.** Out of scope; refer to a specialist. The VAT201 guide shows the concessions as On Land (farming, forestry and mining), Offshore (commercial fishing, coastal shipping, offshore mining and the National Sea Rescue Institute), Rail and Harbour Services (rail freight hauliers and specific harbour service operators) and Peak Power Plant. Elsewhere it also names electricity generators. The boxes are prepopulated from the activity code. VAT 404 places the refund under s 75 and Note 6 to Part 3 of Schedule No. 6 to the Customs and Excise Act; the legacy 'VAT Act s 75' named the wrong Act. The legacy 'foreign-going ships' was not found in a source read and is held.

### Input tax documents

A deduction needs one of these held when the return is furnished (s 16(2)):

- (a) a tax invoice, debit note or credit note under s 20 or s 21;
- (b) a document acceptable to the Commissioner under s 20(6), or a document under s 20(7) or s 21(5);
- (c) the records s 20(8) or (8A) requires, for second-hand goods or s 8(10) goods;
- (d) a bill of entry or other prescribed customs document with the receipt for payment, or (dA) the agent's statement where the agent holds them;
- (e) the agent's tax invoice or note with a s 54(3)(a) statement;
- (f) the documentary proof the Commissioner prescribes, for the listed s 16(3) deductions; or
- (g) a ruling confirming the document held is acceptable, requested no later than 2 months before the 5-year period ends, with the ruling and document held when the return is furnished. It may issue only if the vendor took reasonable steps to obtain a document the paragraphs above require, could not because of circumstances beyond its control, and no other provision of the Act can be applied.

An amount deductible but not deducted may go against a later period ending no later than 5 years after the relevant period (s 16(3), proviso (i)); see `south-africa-vat` for proviso (ii).

| Consideration in money | Requirement |
| --- | --- |
| Total consideration in money not above R50 | No tax invoice, but a document acceptable to the Commissioner (s 20(6)), such as a till slip |
| Consideration in money not above R5,000 and above R50 | Abridged invoice permitted (s 20(5)). Not for s 11 supplies. |
| Above R5,000 | Full tax invoice (s 20(4)) |

A full tax invoice carries the words 'tax invoice', 'VAT invoice' or 'invoice'; the supplier's name, address and VAT number; the recipient's name, address and, where the recipient is a vendor, VAT number; a serial number and date; a full description, indicating second-hand goods; quantity or volume; and either value, tax and consideration, or the consideration with the tax or a statement that it includes tax and the rate. Amounts are in rand, except for a s 11 supply. An abridged invoice carries the words, the supplier's details, serial number and date, a description and the same amount particulars. It does not need the recipient's details or quantity. A vendor issues a tax invoice within 21 days of the supply (s 20(1)).

### Input tax denied

**Entertainment, s 17(2)(a).** Input is denied to the extent goods or services are acquired for entertainment, which s 1 defines as any food, beverages, accommodation, entertainment, amusement, recreation or hospitality of any kind provided by a vendor, directly or indirectly, to anyone in connection with its enterprise. An item known to be entertainment is denied unless an exception applies; Conservative defaults covers the unknown cases. Test these exceptions:

- (i)(aa) taxable supplies of entertainment in the ordinary course of an enterprise continuously or regularly supplying it to clients or customers, to the extent charged at a price covering all direct and indirect costs or at open market value;
- (i)(bb) entertainment to an employee, office holder or connected person, to the extent charged at a price covering all direct and indirect costs, which covers the legacy 'canteen';
- (ii) a meal, refreshment or accommodation for the vendor, a partner, an employee, an office holder or a self-employed natural person, for a night away from both usual residence and usual working place because of the enterprise or duties; and
- (iv) a meal or refreshment supplied by a seminar organiser, for a charge covering its cost.

Left to `south-africa-vat`: (iii) conveyance operators, (v) municipalities, (vi) welfare organisations, (vii) medical admission, (viii) ships' crews and (ix) prizes. The legacy exception for long-distance road transport operators' meals for their personnel is within (iii) only on those words.

SARS VAT 411 treats year-end lunches and parties, complimentary staff tea, coffee and snacks, and client entertainment, including business lunches and golf days, as usually denied. Promotional items such as diaries, pens, mouse pads, clothing and samples, acquired to promote taxable supplies, are generally deductible. Wine, chocolates, hampers, tickets, computer games and music CDs are entertainment and denied unless the vendor normally supplies them. The legacy cited 'BGR conditions', BGR 16 and IN 70 here. BGR 16 is the apportionment ruling, and IN 70 was not read. VAT 411 is the source read.

**Club subscriptions, s 17(2)(b).** Denied for membership of a club, association or society of a sporting, social or recreational nature.

**Motor cars, s 17(2)(c).** Input is denied on any motor car supplied to or imported by the vendor, whatever the business use. The s 1 definition includes a motor car, station wagon, minibus, double cab light delivery vehicle and any other motor vehicle normally used on public roads, with 3 or more wheels, constructed or converted wholly or mainly for carrying passengers. It excludes vehicles for only one person or suitable for more than 16 persons, vehicles of unladen mass 3,500 kg or more, caravans and ambulances, special purpose vehicles with accommodation for persons only incidental to that purpose, qualifying game viewing vehicles, and hearses used exclusively as such.

IN 82 applies an objective test, more than 50% for carrying passengers, by comparing the length of the passenger area with the dedicated load area. Do not treat a body style as settled without the measurement. The block does not apply where the car is acquired exclusively for a taxable supply of it in the ordinary course of an enterprise continuously or regularly supplying motor cars by sale, instalment credit agreement or rental at an economic rental, or for demonstration or temporary use before such a supply; the prize proviso is in `south-africa-vat`.

Repairs, maintenance and insurance on a motor car are deductible to the extent of taxable use (IN 82, para 3.7). Where that use is mixed, the Mixed use row under Transaction questions and defaults decides. The legacy 'running costs (fuel, repairs)' overstated fuel: fuel levy goods are zero-rated, so there is no VAT to claim on them.

**Apportionment and mixed use.** VAT directly attributable follows its use: wholly taxable, in full; wholly exempt or other non-taxable purposes, none (VAT 404, direct attribution). The rest is apportioned by a ratio the Commissioner determines by ruling (s 17(1)), whether the other use is exempt supplies, private use or another non-taxable purpose (BGR 16, para 2). If the intended use for taxable supplies is 95% or more, it is treated as wholly taxable (s 17(1)(i)). Below 95%, a share the vendor states is not that ratio, so R-ZA-2 applies: see Example 7. The legacy test, 'taxable supplies are at least 95% of total supplies', stated the fraction rather than the intended use.

BGR 16 Issue 3 is the default for vendors with no alternative approved by ruling, for financial years commencing on or after 1 January 2024: y = a / (a + b + c) x 100, where a is all taxable supplies, including deemed supplies, b is all exempt supplies and c is other income, subject to its exclusions and adjustments. The legacy description left out c. The vendor must first determine that the method is fair and reasonable to its business. Vendors using the previous year's turnover adjust within 9 months after the financial year end (N7). At the time of that adjustment the vendor must send vatrulings@sars.gov.za its name, VAT registration number, method and formula, and the ratio for the year; the first time the formula is applied, the method and ratio for the past 3 years (N8). Another method needs a ruling; the legacy examples of transaction count, headcount and floor area are not in BGR 16 and are not settled methods.

The legacy cited *CSARS v African Bank Ltd* [2025] ZASCA 101 for the method. That judgment (8 July 2025) is about jurisdiction: a ruling approving a method other than the one requested is a refusal under s 32(1)(a)(iv), so objection and appeal lie. It does not decide which method is right. Tax Court VAT 22498 (27 July 2026) dismissed an appeal against a ruling of 23 September 2021, treating the s 17(1) enquiry as intended use, a question of fact, tested for being fair and reasonable. The link between that case and the bank is an inference from the case number, dates and ruling. The computation stays with R-ZA-2.

### Second-hand goods, s 16(3)(a)(ii)

Notional input tax is paragraph (b) of 'input tax'. It is the tax fraction of the lesser of the consideration in money and the open market value. All of these must be met:

- the goods are second-hand goods as s 1 defines them, which excludes animals, the conditional gold items, mining rights and the specified land;
- they are situated in South Africa and supplied by way of a sale by a resident of South Africa, other than the foreign diplomatic or consular persons the definition excludes;
- the sale is not a taxable supply, so a vendor's sale of its business asset carries ordinary VAT instead; and
- they are acquired wholly or partly for making taxable supplies.

The deduction is limited to the extent payment was made in the period, on the invoice basis too (s 16(3)(a)(ii)(aa)). Fixed property and share block shares have their own timing rule and a cap at the transfer or stamp duty; R-ZA-5 applies to a sale or purchase. Section 20(8) requires the seller's name and identity details, address, date acquired, description, quantity, consideration, and proof and date of payment, usually on form VAT264. The legacy 'VAT264 declaration (modernised 2023)' is replaced: VAT 404 says the Act was amended from 1 April 2023 to clarify that VAT264 is only for second-hand goods. Flag for reviewer. A zero rate under s 11(1)(a), (b), (c), (d) or (i) is lost where notional input tax was deducted, and export of such goods goes in Field 10.

### Fringe benefits, s 18(3)

An employer vendor granting a Seventh Schedule benefit that consists of a supply of goods or services makes a deemed supply, at the end of the month the cash equivalent goes into remuneration (s 9(7)), on the cash equivalent (s 10(13)). Common items: the right of use of a company vehicle, free or cheap services, and assets given below market value. The proviso excludes a benefit that is an exempt supply, a zero-rated supply or entertainment, and a further proviso excludes a benefit granted in the course of making exempt supplies. A low-interest loan is an exempt financial service and residential accommodation is within s 12(c). The right to use a motor car is not one of those exclusions.

For a vehicle, the consideration is not the Seventh Schedule's income tax value. The legacy gave that as 3.5% of the determined value a month, or 3.25% with a maintenance plan; those percentages were not read and are held. GN 2835 of 22 November 1991 sets the VAT amount: 0.3% of the determined value for each month or part where the vehicle is a motor car and the vendor could not deduct the full input tax under s 17(2); 0.6% otherwise, reduced by the lesser of what the employee pays for the right of use and the amount itself. Further reductions are in `south-africa-vat`. Output tax is the tax fraction of that amount, in Field 12.

### Bad debts, s 22

Section 22(1) allows a deduction where a taxable supply was made for consideration in money, a return was furnished accounting for output tax, and the debt has been written off as irrecoverable. The legacy 12-month test was wrong: s 22(1) has none. The amount is the tax fraction of the debt written off, in Field 17, on the invoice basis. The payments basis is barred, except supplies under s 9(2)(b) or s 9(3)(c). Instalment credit agreements and transferred receivables have further limits; see `south-africa-vat`. A later recovery goes in Field 12 (s 22(2)).

### Municipal bills

Municipal property rates are zero-rated under s 11(2)(w), not outside VAT and not a non-supply as the legacy guide said. A 'municipal rate' excludes a single charge for rates and other supplies. Split the bill by line. Electricity, water and refuse charges carry input tax where the tax invoice shows VAT. A single charge is not a municipal rate: send it to the reviewer.

### Supplier discovery library

The patterns are matching aids. Naming a business does not establish its VAT status, its billing entity or what any invoice shows. No supplier's status was read for this conversion. Always apply the condition. 'Input 15%' below means: claim only with a document s 16(2) accepts, from a registered vendor showing VAT, for taxable use.

**Receipts.** A bank credit is not a VAT classifier.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| EFT FROM [client], EFT CREDIT | Candidate taxable supply | Trace to the invoice or agreement. Field 1 only once classified. |
| INSTANT MONEY, CASH DEPOSIT | Candidate taxable supply | Cash receipt; trace to the sale |
| PAYFAST PAYOUT, PAYFAST SETTLEMENT | Candidate taxable supply | Gateway settlement. The gross sale is the amount, with fees treated below; trace to the sales record. |
| YOCO SETTLEMENT, YOCO PAYOUT | Candidate taxable supply | same |
| SNAPSCAN PAYOUT | Candidate taxable supply | same |
| ZAPPER SETTLEMENT | Candidate taxable supply | same |
| CAPITEC, FNB, ABSA, NEDBANK, STD BANK CREDIT | Classify by the character of the receipt | The same credit can be a taxable sale, rent of a dwelling (exempt), or a loan drawdown or capital injection (outside VAT) |
| SWIFT, FOREIGN CURRENCY CREDIT | Candidate zero rate | Goods exported under s 11(1)(a), Field 2A; services within s 11(2)(l) or (k), Field 2. Proof under s 11(3). Otherwise the default for an export without proof. |
| EXPORT, INTERNATIONAL SHIPMENT | Candidate zero rate | Goods exported from South Africa; same |
| BROWN BREAD, MAIZE MEAL, RICE, EGGS, MILK | Candidate zero rate | Match the Part B item wording; Field 2 |
| FUEL LEVY, PETROL, DIESEL (sold) | Candidate zero rate | Fuel levy goods within s 11(1)(h); Field 2 |
| INSURANCE PAYOUT, CLAIM SETTLEMENT | Deemed supply, s 8(8) | Output tax at the tax fraction where the payment relates to a loss in carrying on an enterprise. Not where the contract is outside s 7(1)(a), where it is paid to another person for goods or services being reinstated, or where s 17(2) denied input on the goods or services. VAT 404 Example 10. The return field is not stated in the sources read: Needs Input. |
| INTEREST, INT EARNED | Exempt; Field 3 | s 12(a), s 2(1)(f). Enters apportionment on BGR 16's terms. |
| SARS REFUND | Exclude | Tax refund |
| LOAN DRAWDOWN | Exclude | Loan proceeds |

**Banks and payment processors.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| BANK CHARGES, SERVICE FEE, FNB FEE, ABSA FEE | Input 15% | Fee within the s 2(1) proviso. The legacy statement that banks issue monthly tax invoices was not read for any bank. |
| PAYFAST FEE, PAYFAST CHARGE | Input 15% | Fee or merchant's discount within the s 2(1) proviso |
| YOCO FEE, YOCO CHARGE | Input 15% | same |
| PEACH PAYMENTS FEE | Input 15% | same |

**Rent, utilities and communications.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| OFFICE RENT, COMMERCIAL LEASE | Input 15% | Only where the landlord is a vendor and a document s 16(2) accepts shows VAT. No VAT charged, no input. Residential rent is exempt whatever the landlord's status (s 12(c)). |
| ESKOM, CITY POWER, CITY OF CAPE TOWN | Split by line | Electricity, water and refuse: Input 15%. Rates: zero-rated, no input. See Municipal bills. |
| TELKOM, VODACOM, MTN, CELL C, RAIN | Input 15%, by use | Mixed use: Needs Input until the business share is known, then see Mixed use under Transaction questions and defaults |

**Fuel, motor and travel.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| ENGEN, SHELL, CALTEX, SASOL | Check slip | Fuel levy goods are zero-rated, so no input on them. VAT 404 says 'aviation kerosene, motor oil and oil lubricants are subject to the standard rate'. Car wash and shop items: Input 15% only on the VAT the document shows, and food and drink for staff or clients is entertainment. |
| MOTOR CAR PURCHASE, LEASE, RENTAL (AVIS, EUROPCAR, HERTZ, BIDVEST) | Denied, s 17(2)(c) | Motor car as defined, unless a proviso applies. Vehicle type unknown: Needs Input. Otherwise Input 15%. |
| FLYSAFAIR, LIFT, CEMAIR | Check invoice | Standard-rated if a domestic flight, per the VAT201 guide's 'local air travel'. Claim only the VAT the document shows. |
| SA AIRLINK | Check route and invoice | Domestic: as above. International transport within s 11(2)(a): zero-rated. |
| UBER SA, BOLT SA, TAXI | Exempt where s 12(g) applies | The exemption is for the person transporting fare-paying passengers by road in a vehicle it operates, in a transport business. Who that is depends on the document. Input only on VAT a document shows, such as a separately shown booking fee. |
| GREYHOUND, INTERCAPE | Exempt where s 12(g) applies | VAT 404 names mainline and luxury bus services. No input; check that the supply is not zero-rated under s 11(2)(a). |

**Food and restaurants.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| CHECKERS, SHOPRITE, PICK N PAY, WOOLWORTHS, SPAR | Mixed 15% and 0% | Office tea, coffee and the staff fridge are entertainment: denied whatever the rate, unless a s 17(2)(a) exception applies. Disclose only the VAT the slip shows: on an R800 slip with R230 standard-rated and R570 zero-rated, R30, not the tax fraction of R800. Stock for resale: split on the itemised slip. |
| CLIENT LUNCHES, ENTERTAINMENT, CORPORATE GIFTS, RESTAURANT | Denied, s 17(2)(a) | Unless an exception applies; gifts per VAT 411 |
| HOTEL, GUEST HOUSE, LODGE | Denied, s 17(2)(a) | Unless exception (ii) applies, with a document showing VAT |

**Office, software and other costs.** Generic rows state conditions only.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| TAKEALOT, MAKRO, GAME, STATIONERY, OFFICE SUPPLIES | Input 15% | Business purchases |
| GOOGLE ADS, META, LINKEDIN | Check invoice | An invoice showing SA VAT from a registered supplier is an ordinary input. The legacy statement that these bill through a South African entity or as registered suppliers was not read and is held. No SA VAT: imported services test. |
| MICROSOFT, ADOBE, AWS, APPLE, SLACK, DROPBOX | Check invoice | same |
| ZOOM, ATLASSIAN, ANTHROPIC, OPENAI | Check invoice | same |
| SANTAM, HOLLARD, OUTSURANCE, DISCOVERY INSURE (premiums) | Input 15% | Short-term insurance is standard-rated (VAT 421). Life insurance is exempt (s 2(1)(i)), no input. Income-protection cover: read the policy. |
| COWORKING, SHARED OFFICE | Check invoice | Input 15%, on commercial premises |
| POST OFFICE, COURIER, POSTAGE | Check invoice | Input 15%. International transport of goods may be zero-rated under s 11(2)(a). |
| LICENCE FEE, PERMIT, GOVERNMENT FEE | Check document | Input only where a document shows VAT |

**Exclusions.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| SARS INCOME TAX, SARS PAYE, RECEIVER OF REVENUE | Exclude | Tax payment |
| SARS VAT PAYMENT | Exclude | VAT payment, not input tax |
| OWN TRANSFER, PERSONAL | Exclude | Drawings |
| LOAN, BOND REPAYMENT | Exclude | Principal only |
| SALARY, WAGES, PAYROLL | Exclude | Check any fringe benefit |
| ATM, CASH WITHDRAWAL | Tier 2, ask | Needs Input: see Cash withdrawal under Transaction questions and defaults |

### Bank exports and narrations

Column layouts are from the prior version and were not checked against any bank's documents. They differ from those in `south-africa-vat`. Confirm against the file supplied.

| Bank | Format | Key fields |
| --- | --- | --- |
| FNB | CSV, PDF | Date, Description, Amount, Balance |
| ABSA | CSV | Date, Description, Debit, Credit, Balance |
| Standard Bank | CSV | Date, Description, Debit, Credit, Balance |
| Nedbank | CSV | Date, Description, Debit, Credit, Balance |
| Capitec | CSV | Date, Description, Debit, Credit, Balance |
| Investec | CSV | Date, Description, Debit, Credit, Balance |

| Narration | Meaning | Hint |
| --- | --- | --- |
| EFT CREDIT, INWARD PAYMENT | Bank transfer in | Potential income |
| DEBIT ORDER, DEBI CHECK | Direct debit | Regular expense |
| POS, CARD PURCHASE | Point of sale | Expense |
| CASH DEPOSIT | Cash received | Potential income; trace it |
| SARS, RECEIVER OF REVENUE | Tax payment or refund | Exclude |
| BANK CHARGES, SERVICE FEE | Bank fee | s 2(1) proviso; Input 15% |

### Transaction questions and defaults

Tier 2 catalogue for the structured form in `vat-workflow-base`.

| Item | What is missing | Default | Question |
| --- | --- | --- | --- |
| Motor vehicle | Whether it is a motor car as defined | Needs Input. Once answered, a motor car on purchase, lease or rental is denied unless a proviso is shown, with the disclosure under Conservative defaults. | 'What type of vehicle is it: sedan, SUV, hatchback, single cab bakkie, club or extended cab, double cab bakkie, minibus, panel van or truck? What is its unladen mass, and is the dedicated load area longer than the passenger area, ignoring the engine and counting fold-up seat areas as passenger area? Is it for resale or rental in your trade?' |
| Entertainment | Whether it is entertainment, and whether a s 17(2)(a) exception applies | Unknown whether it is entertainment: Needs Input. Known entertainment with no exception shown: denied, with the disclosure under Conservative defaults. | 'Do you supply this in the ordinary course for a charge covering all costs? If not, was it a night away from home and work, a canteen charging at least full cost, a seminar meal, or a non-entertainment promotional item?' |
| Fringe benefits | Whether any benefit was granted | Flag | 'Do you employ staff and grant any benefits: company car, low-interest loan, assets below market value, free or cheap services, accommodation?' |
| Tax invoices | Whether the document meets s 20 | Needs Input | 'Do all supplier tax invoices meet the requirements above? Has SARS queried any?' |
| Second-hand goods | Records | Needs Input | 'Did you buy used goods in South Africa from a resident in a non-taxable sale? Do you hold VAT264 or equivalent records, proof of the seller's identity and proof of payment, and what was paid in this period?' |
| Imported services | Exempt or private use | Needs Input. Once answered: fully taxable use, nothing to declare; otherwise Field 12 on that part, with no input. That tax alone does not fire R-ZA-2. | 'Does the business have any exempt income or private use of this service, and does the invoice show SA VAT?' |
| Mixed use | Business share of the item | Needs Input. Once answered: wholly for taxable supplies, full input; wholly for another use, none; partly, with taxable use at 95% or more, full input (s 17(1)(i)); partly, below 95%, R-ZA-2, with no input calculated from the share. | 'What share of this item is used for your taxable sales, what share privately and what share for exempt income, and what is that based on?' |
| Cash withdrawal | What the cash paid for | Needs Input. Nothing is entered until the purchase and a document s 16(2) accepts are shown. | 'What did this cash pay for, and do you hold a document for it?' |
| Insurance receipt | Loss, contract and field | Needs Input | 'What loss does this payment settle, on what policy, and was input denied on the goods or services?' |
| Large purchases | Capital or other | Needs Input on the field | 'Is this a capital item? Is it new or second-hand, and how will it be used?' |

### Onboarding fallback

If the client provides a bank statement but cannot answer the questions at once, list receipts as candidates only and enter nothing on the unknown items. Registration still has to be confirmed (R-ZA-1). The legacy fallback of classifying all credits as taxable on the invoice basis at 15% is replaced by the defaults above. Claim input only where the document is held. Flag all large purchases for capital goods review.

### Excel working paper

Working paper only. Layout for Sheet 'Box Summary' under `vat-workflow-base`.

```
SOUTH AFRICA VAT WORKING PAPER (VAT201)
Vendor: _______________  VAT Number: ___________
Period: ___________  Category: A / B / C / D / E / F
Basis: Invoice / Payments

A. OUTPUT (SALES)
  A1. Standard-rated supplies, VAT inclusive, excl. capital -> Field 1         ___________
  A2. Standard-rated capital goods and services, VAT inclusive -> Field 1A     ___________
  A3. Output tax: A1 x 15/115 -> Field 4; A2 x 15/115 -> Field 4A              ___________
  A4. Zero-rated supplies -> Field 2 (other) / Field 2A (exported goods)       ___________
  A5. Exempt and non-supplies -> Field 3                                       ___________
  A6. Commercial accommodation, VAT excluded -> Fields 5 to 9                  ___________
  A7. Change in use and second-hand goods exported -> Field 10 / Field 11      ___________
  A8. Other output adjustments and imported services -> Field 12               ___________
  A9. Total output tax (4 + 4A + 9 + 11 + 12) -> Field 13                      ___________

B. INPUT (PURCHASES)
  B1. Input tax on capital goods and services -> Field 14 (imported: 14A)      ___________
  B2. Input tax on other goods and services -> Field 15 (imported goods: 15A)  ___________
  B3. Change in use input adjustment -> Field 16                               ___________
  B4. Bad debts (s 22) -> Field 17                                             ___________
  B5. Other input adjustments -> Field 18                                      ___________
  B6. Denied input (entertainment, motor cars): excluded, no field             ___________
  B7. Total input tax (14 + 14A + 15 + 15A + 16 + 17 + 18) -> Field 19         ___________

C. NET VAT
  C1. Net VAT payable / (refundable): Field 13 - Field 19 -> Field 20          ___________
  C2. Prior period credit carried forward (per the SARS statement of account)  ___________

REVIEWER FLAGS:
  [ ] Registration and vendor number confirmed?
  [ ] Filing category confirmed?
  [ ] Accounting basis confirmed?
  [ ] Document s 16(2) accepts held for all input claims (full, abridged or till slip by value band)?
  [ ] Second-hand goods documentation complete (s 20(8) records, identity, proof of payment)?
  [ ] Zero-rated vs exempt correctly distinguished; export documents held?
  [ ] Motor car and entertainment inputs denied unless an exception applies?
  [ ] Output tax on fringe benefits (s 18(3)) included; s 18 change in use checked (R-ZA-3)?
  [ ] Registration threshold position flagged where enacted and administered amounts differ?
```

### Key legislation

| Topic | Section |
| --- | --- |
| Definitions ('motor car', 'entertainment', 'tax fraction') | VAT Act s 1 |
| Financial services and the fee proviso | VAT Act s 2 |
| Imposition of VAT; imported services | VAT Act s 7, s 14 |
| Deemed supplies (insurance payouts, fringe benefits) | VAT Act s 8(8), s 18(3) |
| Time and value of supply | VAT Act s 9, s 10 |
| Zero-rated supplies | VAT Act s 11 |
| Exempt supplies | VAT Act s 12 |
| Accounting basis | VAT Act s 15 |
| Input tax; denied input; apportionment | VAT Act s 16, s 17 |
| Change in use adjustments | VAT Act s 18 |
| Tax invoices | VAT Act s 20 |
| Bad debts | VAT Act s 22 |
| Registration | VAT Act s 23 |
| Filing | VAT Act s 27, s 28 |
| Agents and principals | VAT Act s 54 |
| Interest, penalties, understatement | TAA s 187, s 210, s 213, ss 222 to 224 |

### Known gaps

- Cross-border services where the position is not plain: R-ZA-6.
- Customs VAT on imports beyond an input claim on a bill of entry and receipt: R-ZA-6.
- Branch and group registrations: R-ZA-7.
- Large-value property transactions: R-ZA-5.

## Deadlines and filing

### Tax periods, s 27

The legacy category table was wrong in most rows and is replaced. There is no quarterly category. Bimonthly filing is Category A or B; the Commissioner determines which. SARS's tax periods page says 5 categories are available and lists A to E; Category F appears in the consolidation of s 27 only.

| Category | Period | Who |
| --- | --- | --- |
| A | Two months ending January, March, May, July, September, November | Commissioner determines A or B (s 27(2); SARS page) |
| B | Two months ending February, April, June, August, October, December | Commissioner determines A or B (s 27(2); SARS page) |
| C | One month | Taxable supplies above R30 million, or likely to be, in any consecutive 12 months; or written application; or repeated failure of obligations; in each case only where the Commissioner has directed it (s 27(3)). Must file and pay on eFiling (VAT 404). |
| D | Six months ending the last day of February and August, or another month approved in writing | Farming within the limit in the rates table (the consolidation of s 27(4)(a) says solely farming), or a micro business under the Sixth Schedule to the Income Tax Act, each on written application (s 27(4); SARS page) |
| E | Twelve months to the end of the year of assessment, or another month approved in writing | A company or trust fund solely letting fixed property or renting movable goods to, or administering or managing, connected companies, where the recipients are all vendors with a full deduction, invoices and payment are annual, and it has applied in writing (s 27(4A); VAT 404) |
| F | Four months ending June, October and February | Other than a s 50 vendor, taxable supplies within the limit in the rates table, and a written application (s 27(4B)). Held. |

Micro businesses on turnover tax fall under Category D, not F as the legacy guide said, and only on application. Under s 27(6)(ii) the Commissioner may approve a fixed day within 10 days before or after the month end (VAT 404, 3.3). The s 28(1) due date follows that period end: a period ending on 20 June is due on 25 June, and a period ending on 5 July is due on 25 July.

### Returns and payment, s 28

| Route | Due |
| --- | --- |
| Standard rule | 25th day of the first month after the period ends, or that 25th where the period ends on or after the 1st and before the 25th (s 28(1)). SARS's FAQ reads 'the 25th (or the last business day before the 25th)'. |
| Registered to submit electronically | Last business day of the month in which that 25th falls, where the return and the full payment are both made electronically (s 28(1), proviso (iii)) |
| Debit order | Last business day, as s 28(1) proviso (ii) provides. The VAT201 guide says the debit order facility no longer applies for eFilers; do not rely on this route without checking. |

The last business day is therefore not unconditional, as the legacy table implied: it needs electronic filing and full electronic payment. For a period ending 30 September 2026, the 25th of October is a Sunday, so the SARS FAQ points to Friday 23 October; on eFiling with full electronic payment the date is Friday 30 October 2026.

Returns go through eFiling or a SARS office by appointment; SARS does not accept faxed or emailed returns, printed eFiling copies or photocopies. A nil return is still required (s 28(2)).

### Filing on SARS eFiling

The steps are from the VAT201 guide. This workflow does not file or pay.

1. On SARS eFiling, activate the VAT tax type under Organisation, Tax Types, Manage Tax Types, if not yet active.
2. Select Returns, Returns Issued, then Value Added Tax (VAT201). Choose the period and Request Return. The VAT filing control table is under Request VAT Control Table and covers up to 12 months.
3. Open the VAT201 from the VAT201 Work Page, complete the fields, then Save or Submit VAT201.
4. Pay with the pre-populated 19-digit Payment Reference Number (PRN), whose first 10 digits are the VAT number. Use the PRN for that period only. Payment can be through eFiling, by EFT or at an approved bank. A credit push counts only once authorised in the banking product.
5. Without diesel registration, the payment Total is Field 20 plus penalties and interest, where they apply.

To revise a return, request the period again; the guide says the same PRN and the prior financial data are pre-populated.

### Refunds

A minus sign in Field 20 means a refund. SARS says a refund due is payable within 21 business days after a correct return or all required supporting documents, without interest for that period (FAQs; VAT 404, 10.7). SARS may withhold or delay it, including for a defect, wrong bank details, outstanding returns or verification. Under TAA s 190(2) SARS need not authorise a refund until a verification, inspection, audit or criminal investigation is finalised, unless acceptable security is given (s 190(3)). Under s 191 refunds are subject to set-off, and a refund under R100, or any other amount the Commissioner may determine by public notice, is carried forward (read in the unofficial consolidation). The legacy statement that a refund position 'almost always triggers' a verification or audit was not found in a source read: a refund may be selected.

## Penalties and interest

| Item | Rule | Status |
| --- | --- | --- |
| Late payment | 10% of the tax paid late (VAT Act s 39(1), which the Commissioner must impose under TAA Chapter 15; TAA s 213). | Read in SARS FAQ; sections read in the unofficial consolidation |
| Late return, tax paid on time | SARS FAQ: 'Currently, there is no penalty imposed on the late submission of a VAT return'. Fixed amount penalties under TAA ss 210 and 211 apply only to non-compliance listed in a public notice (s 210(2)); s 211 scales them by assessed loss or taxable income. A return late with its tax late carries the 10% and interest. | SARS's stated practice, not a statutory exemption |
| Interest | SARS Table 1 rates, from the first day of the month after the month the payment was due, per month or part of a month (VAT 404, 11.3). The rate follows the Public Finance Management Act s 80(1)(b) rate. | Read |
| Compounding | Held. TAA s 187(2) provides for daily balance and monthly compounding, with the Commissioner to prescribe by public notice the date it applies to a tax type. VAT 404 says it applies only once a notice is published, and IN 68 Issue 3 lists these provisions as not commenced. The legacy 'compounding monthly (TAA s 187)' was wrong as a present statement. No notice applying it to VAT was read and no complete search of SARS notices was made. | Held, with the search limit stated |
| Understatement | TAA ss 222 to 224. The s 223 table percentages are 0% to 200%. Standard case: 10% substantial understatement, 25% reasonable care not taken, 50% no reasonable grounds, 75% impermissible avoidance arrangement, 100% gross negligence, 150% intentional tax evasion. | Read in the unofficial consolidation |

The legacy range of 10% to 200% left out the 0% and 5% voluntary disclosure cells. The full table is in `south-africa-vat`.

A tension remains on interest. IN 68 Issue 3 of 8 December 2020 says the earlier wording of s 39 continues to apply to interest on late payment under s 28(1), whilst the unofficial consolidation prints s 39(2) as deleted. The rule above follows VAT 404.

## Cross-border points

**Exports.** Services: s 11(2)(l) excludes services supplied directly in connection with land or improvements in South Africa, or movable property in South Africa when rendered, or to the non-resident or another person who is in South Africa when the services are rendered, with the exceptions in that paragraph. Keep the contract showing the foreign client and its location, with payment records, as s 11(3) proof; the Act requires proof acceptable to the Commissioner and does not list these. Report in Field 2. Goods go in Field 2A with the Customs Code.

Under reg 15(1) of the Export Regulations (GN R. 316 of 2014), movable goods supplied under Part One or Part Two must leave within 90 days of the earlier of invoice and payment; under Part One the 90 days run from the date of the tax invoice instead. Part One is the standard-rated route with a refund to the qualifying purchaser, not a direct export (VAT 404, 12.1). The connected persons rule in reg 15(1)(b) applies. Reg 15(2) sets these exceptions: an advance payment, 30 days from the contract's export dates; precious metals exported by air, 30 days from the export release; goods timed under s 9(1) or s 9(3)(b)(i) or (ii) that undergo repair, improvement, erection, manufacture, assembly or alteration, 90 days from completion of that process; part of a hunted animal for preservation or mounting as a trophy, 7 months from the earlier of invoice and payment; tank containers for bulk carriage on a foreign-going ship, 6 months from completion of manufacture or reconditioning; and, for Part Two only, an extension by the Commissioner for circumstances beyond the vendor's control or exceptional commercial delays, on a timely written application (reg 15(2)(f)). The vendor keeps proof of any exception it relies on (reg 15(3)). For an indirect export zero-rated by election under Part Two (Sections A and B), reg 16 requires the documentary proof within 90 days of the date the goods had to be exported. Without it, s 11(3) is not met (reg 16(2)), and the vendor accounts for output tax at the tax fraction of the consideration in Field 12 of the period in which those 90 days end (reg 16(3)). If the proof arrives within 5 years from the end of the tax period in which the original tax invoice should have been issued, the amount may be deducted in Field 18 of the period in which it arrives, provided the vendor can prove it made the taxable supply for a consideration in money, furnished the return and properly accounted for that output tax (reg 16(4)). The Commissioner may extend the 90 days for circumstances beyond the vendor's control, on a written ruling application made before they expire (reg 16(5)). Where only proof of payment is missing, read reg 16(6) to (10) first: the listed cases, such as written deferred payment terms, carry their own periods. For other exports, follow the default under Conservative defaults.

**Imported services.** Section 1 defines these as a supply of services by a supplier who is resident or carries on business outside South Africa to a recipient who is a resident of South Africa, to the extent the services are utilised or consumed in South Africa otherwise than for making taxable supplies. Tax arises under s 7(1)(c), on the greater of consideration and open market value (s 14(3)).

- A service utilised or consumed wholly outside South Africa is outside the definition.
- A fully taxable vendor using it for taxable supplies has nothing to declare.
- A vendor with exempt or private use declares tax on that portion in Field 12, with no input on it. That tax is not input tax: paragraph (a) of the s 1 definition covers tax payable by a supplier, on an importation of goods or under s 7(3), and s 7(2) puts tax under s 7(1)(c) on the recipient. So no s 17(1) apportionment arises on it and R-ZA-2 does not fire on it. Example: a R10,000 service at open market value with 40% exempt use gives R4,000 x 15% = R600 in Field 12.
- A non-vendor completes VAT215, keeps it, and pays within 30 days (s 14(1)).
- No tax is payable on a supply chargeable under s 7(1)(a); one that would be zero-rated or exempt if made in South Africa; education by a regulated institution in an export country; an employee's or office holder's services within proviso (iii)(aa) to 'enterprise'; or a value not above R100 per invoice (s 14(5)).

Where a registered foreign electronic services supplier charges SA VAT on an invoice, it is an ordinary input, subject to the invoice particulars in Notice 1583 of 2021. Regulations on what counts as electronic services are in `south-africa-vat`.

**Imported goods.** Tax arises under s 7(1)(b); the input needs a bill of entry and payment receipt, reported in Field 14A or 15A. Anything further is R-ZA-6.

## Two worked examples that recompute

All examples are hypothetical and apply 15%. Each is checked by CI. Each states what it depends on. Dates assume a Category A vendor on eFiling, period ending 30 September 2026, with the operational hold lifted.

### Example 1: standard bimonthly return

**Input.** Standard-rated supplies R500,000, VAT exclusive, from the sales invoices. Purchases R200,000, VAT exclusive, all standard-rated, for taxable use, valid tax invoices held.

```oa-check
name: ZA VAT201 standard return on VAT exclusive and VAT inclusive facts
inputs:
  sales_excl: 500000
  purchases_excl: 200000
  bank_sales_incl: 500000
  bank_purchases_incl: 200000
  rate: 15
steps:
  - field_4: pct(sales_excl, rate)
  - field_1: sales_excl + field_4
  - field_15: pct(purchases_excl, rate)
  - purchases_incl: purchases_excl + field_15
  - field_20: field_4 - field_15
  - alt_field_4: round(bank_sales_incl * rate / (100 + rate), 2)
  - alt_field_15: round(bank_purchases_incl * rate / (100 + rate), 2)
  - alt_field_20: alt_field_4 - alt_field_15
expected:
  field_4: 75000
  field_1: 575000
  field_15: 30000
  purchases_incl: 230000
  field_20: 45000
  alt_field_4: 65217.39
  alt_field_15: 26086.96
  alt_field_20: 39130.43
```

**Result.** VAT payable R45,000 (Field 20) on the VAT exclusive facts. Bank statements show VAT inclusive amounts, so state which basis the figures are on: had R500,000 and R200,000 been VAT inclusive bank totals, payable would be R39,130.43. Payment and filing are due by Friday 30 October 2026 with full electronic payment. Otherwise the standard rule applies.

### Example 2: exporter in a refund position

**Input.** Goods exports R800,000 with s 11(3) proof held. Purchases R300,000, VAT exclusive, standard-rated, documents held. In the second case, R100,000 of the exports are direct exports with no s 11(3) proof; the sale is verified as a supply in the course of the enterprise and not exempt under s 12. In the third case, R100,000 of the exports were indirect exports zero-rated by election under Part Two, the 90 days under reg 16 have ended and no proof is held.

```oa-check
name: ZA exporter refund with and without export proof
inputs:
  exports: 800000
  unproven: 100000
  purchases_excl: 300000
  rate: 15
steps:
  - field_15: pct(purchases_excl, rate)
  - field_2a: exports
  - field_20: 0 - field_15
  - case2_field_2a: exports - unproven
  - case2_field_1: unproven
  - case2_field_4: round(case2_field_1 * rate / (100 + rate), 2)
  - case2_field_20: case2_field_4 - field_15
  - case3_field_12: round(unproven * rate / (100 + rate), 2)
  - case3_field_18_on_proof: case3_field_12
expected:
  field_15: 45000
  field_2a: 800000
  field_20: -45000
  case2_field_2a: 700000
  case2_field_1: 100000
  case2_field_4: 13043.48
  case2_field_20: -31956.52
  case3_field_12: 13043.48
  case3_field_18_on_proof: 13043.48
```

**Result.** Proof held: refund R45,000. Customs Code entered in Field 2A. Flag the export documents; the prescribed documents under GN R. 316 for each export go to the reviewer before any refund claim. Proof not held: the R100,000 is standard-rated at the tax fraction, because a vendor's price must include VAT (VAT 404, principle 1), and the refund falls to R31,956.52. Disclose the missing proof, the zero-rated alternative and the output tax of R13,043.48. If the sale is not verified, it is Needs Input and nothing is entered. Indirect export without proof: nothing goes in Field 1. R13,043.48 goes in Field 12 of the period in which the 90 days end, and the same amount may go in Field 18 of the period in which the proof arrives, on the reg 16(4) conditions. SARS may hold a refund under TAA s 190(2) pending verification.

### Example 3: second-hand goods from a non-vendor

**Input.** A vendor on the invoice basis buys used equipment for R50,000 from a resident non-vendor, for taxable use, in a sale that is not a taxable supply. Open market value is R55,000. All of it is paid in the period and the s 20(8) records are held. Other cases: open market value R40,000; or only R20,000 paid in the period at the R55,000 value.

```oa-check
name: ZA notional input tax limited by value and by payment
inputs:
  consideration: 50000
  market_value: 55000
  low_market_value: 40000
  paid_in_period: 20000
  rate: 15
steps:
  - notional: round(min(consideration, market_value) * rate / (100 + rate), 2)
  - notional_low_value: round(min(consideration, low_market_value) * rate / (100 + rate), 2)
  - notional_part_paid: round(min(paid_in_period, min(consideration, market_value)) * rate / (100 + rate), 2)
expected:
  notional: 6521.74
  notional_low_value: 5217.39
  notional_part_paid: 2608.70
```

**Result.** Input tax R6,521.74, R5,217.39 at the lower value, or R2,608.70 in the part-paid period, with the balance as it is paid. The legacy put this in Field 15, and the VAT201 guide lists second-hand goods (notional input tax) there, although its Field 14 examples include office equipment. Use Field 15 and flag the capital question for the reviewer. Records not held: Needs Input, and no deduction is entered. A seller who is a vendor making a taxable sale: ordinary input on its tax invoice, not notional input.

### Example 4: bad debt relief

**Input.** An invoice for R23,000, VAT inclusive, on which output tax was returned, is written off as irrecoverable after 14 months. R11,500 of it is recovered in a later period.

```oa-check
name: ZA bad debt relief and later recovery
inputs:
  written_off: 23000
  recovered: 11500
  rate: 15
steps:
  - field_17_invoice_basis: written_off * rate / (100 + rate)
  - field_12_on_recovery: recovered * rate / (100 + rate)
  - field_17_payments_basis: written_off * 0
expected:
  field_17_invoice_basis: 3000
  field_12_on_recovery: 1500
  field_17_payments_basis: 0
```

**Result.** Input tax deduction R3,000 in Field 17 on the invoice basis, in the period of the write-off, whether or not 12 months have passed. On the payments basis, no deduction, because s 22(1) bars it, except supplies under s 9(2)(b) or s 9(3)(c). Debt not written off: no deduction. The later recovery gives output tax of R1,500 in Field 12.

### Example 5: advertising from a large platform

`08 Sep 2026  DEBIT  GOOGLE ADS  Ads September  -R 50,000.00  R 377,700.00`

Check the invoice first. Cases: invoice shows SA VAT from a registered supplier, R50,000 inclusive; foreign billed with no SA VAT, fully taxable vendor; foreign billed with no SA VAT, 40% exempt use.

```oa-check
name: ZA advertising with SA VAT and as imported services
inputs:
  amount: 50000
  exempt_share_percent: 40
  rate: 15
steps:
  - field_15_with_sa_vat: round(amount * rate / (100 + rate), 2)
  - field_12_fully_taxable: pct(amount, 0)
  - imported_value: pct(amount, exempt_share_percent)
  - field_12_partly_exempt: pct(imported_value, rate)
expected:
  field_15_with_sa_vat: 6521.74
  field_12_fully_taxable: 0
  imported_value: 20000
  field_12_partly_exempt: 3000
```

**Result.** With SA VAT shown on a document s 16(2) accepts: input R6,521.74 in Field 15. Document unknown: Needs Input. Foreign billed, fully taxable: nothing to declare. Foreign billed, 40% exempt use: R3,000 in Field 12 on the greater of consideration and open market value, here taken as the R20,000 share, with no input on it. Because that tax is not input tax, R-ZA-2 does not fire on this item; it still fires on any other item that meets its trigger. The legacy statement that Google bills through a South African entity is held.

### Example 6: invoice or payments basis

**Input.** A natural person vendor invoiced R230,000 of sales and received R115,000 of it in the period. It was invoiced R69,000 of purchases and paid R34,500. All amounts are VAT inclusive, standard-rated, with documents held, and each supply is under R100,000. Taxable supplies are within the R2,500,000 amount.

```oa-check
name: ZA Field 20 on the invoice and payments bases
inputs:
  sales_invoiced: 230000
  sales_received: 115000
  purchases_invoiced: 69000
  purchases_paid: 34500
  rate: 15
steps:
  - invoice_output: sales_invoiced * rate / (100 + rate)
  - invoice_input: purchases_invoiced * rate / (100 + rate)
  - invoice_field_20: invoice_output - invoice_input
  - payments_output: sales_received * rate / (100 + rate)
  - payments_input: purchases_paid * rate / (100 + rate)
  - payments_field_20: payments_output - payments_input
  - deferred: invoice_field_20 - payments_field_20
expected:
  invoice_output: 30000
  invoice_input: 9000
  invoice_field_20: 21000
  payments_output: 15000
  payments_input: 4500
  payments_field_20: 10500
  deferred: 10500
```

**Result.** R21,000 payable on the invoice basis. R10,500 on the payments basis, a timing difference of R10,500, not a saving. The payments basis needs the Commissioner's direction, unless s 15(2B) applies; a basis not confirmed is Needs Input and neither figure is entered. A supply at R100,000 or more would stay on the invoice basis under s 15(2A).

### Example 7: telephone account, taxable and private use

`30 Sep 2026  DEBIT  TELKOM  Telephone account  -R 1,150.00  R 376,550.00`

One account, with a document s 16(2) accepts showing VAT of R150. All the vendor's turnover is taxable. The vendor says 60% of use is for taxable supplies and 40% is private, and shows no ruling.

```oa-check
name: ZA telephone account at and below the 95% test
inputs:
  amount: 1150
  rate: 15
  taxable_share_percent: 60
steps:
  - vat: round(amount * rate / (100 + rate), 2)
  - proportional_share_not_entered: pct(vat, taxable_share_percent)
  - field_15_at_60_percent: pct(vat, 0)
  - field_15_at_95_percent: vat
expected:
  vat: 150
  proportional_share_not_entered: 90
  field_15_at_60_percent: 0
  field_15_at_95_percent: 150
```

**Result.** The account cannot be directly attributed, so s 17(1) applies, and 60% is below 95%. The R90 is not entered: the vendor's share is not an authorised ratio, and BGR 16's formula gives 100% here because private use is not turnover, a result VAT 404 treats as a sign that the formula may be inappropriate. R-ZA-2 fires and the workflow stops. With taxable use of exactly 95%, the test is met and the full R150 goes in Field 15 (s 17(1)(i)). At 94.99%, R-ZA-2 fires.

### Transaction patterns

From a hypothetical Johannesburg consultant's FNB account. Each pattern tests both cases.

**Domestic revenue.** `15 Sep 2026  CREDIT  ABC TECHNOLOGY (PTY) LTD  INV-2026-041  R 115,000.00`. Traced to a standard-rated invoice: Field 1 R115,000; output R115,000 x 15/115 = R15,000 in Field 4. Not traced: Needs Input.

**Export of services, proof held.** `22 Sep 2026  CREDIT  ACME CORP USA  USD 5,000 (R 92,500)`. Within s 11(2)(l), with the contract, the client's location abroad and payment records held: Field 2 R92,500. Output R0.

**Export, proof not held.** `24 Sep 2026  CREDIT  ACME CORP USA  USD 1,000 (R 18,400)`. No s 11(3) proof is held, so no zero rate. Verified as a supply in the course of the enterprise and not exempt under s 12: Field 1 R18,400; output R18,400 x 15/115 = R2,400 in Field 4, disclosing the missing proof, the zero-rated alternative and that output tax. Not verified: Needs Input, and nothing is entered.

**Indirect export, proof not held.** `26 Sep 2026  CREDIT  OVERSEAS BUYER LTD  Goods collected  R 23,000.00`. Zero-rated by election under Part Two of the Export Regulations, and the reg 16 proof has not arrived when the 90 days end: R23,000 x 15/115 = R3,000 in Field 12 of the period in which they end, not Field 1. The same R3,000 may go in Field 18 of the period in which the proof arrives, on the reg 16(4) conditions. Not known to be indirect: Needs Input.

**Purchase, document in doubt.** `25 Sep 2026  DEBIT  HARDWARE SUPPLIES  Shelving  -R 2,300.00`. A document s 16(2) accepts is held and supports the VAT, for taxable use: input R2,300 x 15/115 = R300 in Field 15. Otherwise Needs Input, and no deduction is entered.

**Rent.** `01 Sep 2026  DEBIT  CITY PROP MANAGEMENT  September office rent  -R 23,000.00`. Commercial premises with a tax invoice from a registered landlord: input R23,000 x 15/115 = R3,000. Unregistered landlord: no VAT, no input. Dwelling: exempt under s 12(c), no input.

**Fuel.** `10 Sep 2026  DEBIT  ENGEN GERMISTON  Fuel  -R 1,500.00`. Fuel levy goods only: no VAT, no input. A separately itemised service with VAT shown on the document, for taxable use, and not for a denied purpose: Input 15% on that item.

**Ride.** `12 Sep 2026  DEBIT  UBER SA  Trip  -R 230.00`. Fare exempt where s 12(g) applies: no input. A booking fee shown separately with VAT on a document s 16(2) accepts: Input 15% on the fee.

**Motor car lease.** `01 Sep 2026  DEBIT  AVIS  Sedan rental  -R 4,600.00`. A sedan is a motor car as defined: denied, disclosing that no proviso is shown and the input tax denied: R600 if the document shows it or the R4,600 is confirmed as VAT-inclusive at the standard rate, otherwise that amount is Needs Input. A vehicle outside the definition, such as one of unladen mass 3,500 kg or more, with a document showing VAT: Input 15%.

**Client lunch.** `18 Sep 2026  DEBIT  NANDO'S  Client lunch  -R 690.00`. Entertainment with no exception shown: denied, disclosing that and the input tax denied, quantified the same way: R90 on the R690. A meal on a night away within exception (ii), with a document showing VAT: Input 15%.

## Ask the client first

Ask these 6 groups at the start. The workflow base's confirmation step carries them.

1. **Registration.** Are you registered as a VAT vendor, and what is your VAT number? What filing category are you (A to F) and what is the tax period of this statement? Are you on the invoice or payments basis?
2. **Sales.** What types of goods or services do you sell? Do you make any zero-rated supplies, such as exports or basic foodstuffs, with evidence held? Do you make any exempt supplies (financial, residential rent, education)?
3. **Purchases.** Do you buy anything used partly for taxable supplies and partly for exempt supplies or private use? Do you purchase second-hand goods from non-vendors? Do you import services from non-resident suppliers, and do their invoices show SA VAT? Do all your supplier tax invoices meet the s 20 requirements, and has SARS queried any?
4. **Vehicles.** Do you have any motor cars, including double cabs, station wagons, SUVs and minibuses, in the business? Have you claimed input tax on the purchase, lease or rental of any vehicle?
5. **Staff and entertainment.** Do you employ staff and grant any fringe benefits (company car, low-interest loan, assets below market value, free or cheap services, accommodation)? Do you incur entertainment, meals, accommodation or social functions for clients or staff?
6. **Balances.** What is the prior period credit on the SARS statement of account? Have any debts been written off?

### Completion checks

- Registration and vendor number confirmed, with filing category and accounting basis.
- Tax fraction 15/115 used consistently.
- Zero-rated and exempt correctly distinguished.
- Input claims hold a document s 16(2) accepts.
- Second-hand goods claims properly documented.
- Bad debt relief claimed on the s 22 conditions, with no 12-month rule applied.
- Motor car inputs denied (s 17(2)(c)) and entertainment inputs denied (s 17(2)(a)) unless an exception applies.
- Output tax on fringe benefits (s 18(3)) included, and any other s 18 adjustment sent to R-ZA-3.
- Export zero rating has s 11(3) proof. Without it, an indirect export follows reg 16. For any other export, 15% applies only to a sale verified as a supply in the course of the enterprise and not exempt; otherwise the sale is Needs Input.
- Any result that turns on a threshold shows both the enacted and administered amounts.

## Sources

Read on means the date read for this conversion. Limits follow each source. The VAT Act and TAA were read in an unofficial consolidation at source.acts.co.za, because the SARS legislation page links only to a subscription service. Where it conflicts with a SARS guide, the conflict is shown.

| Source | URL | Read on |
| --- | --- | --- |
| VAT Act s 1, definitions, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/1__definitions.php | 2026-11-05 |
| VAT Act s 2, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/2__financial_services.php | 2026-11-05 |
| VAT Act s 7, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/7__imposition_of_value_added_tax.php | 2026-11-05 |
| VAT Act s 8, unofficial consolidation, read in part: s 8(8) | https://source.acts.co.za/value-added-tax-act-1991/8__certain_supplies_of_goods_or_services_deemed_to_be_made_or_not_made.php | 2026-11-05 |
| VAT Act s 9, unofficial consolidation, read in part: s 9(1) and (7) | https://source.acts.co.za/value-added-tax-act-1991/9__time_of_supply.php | 2026-11-05 |
| VAT Act s 10, unofficial consolidation, read in part: s 10(5), (7), (10) and (13) | https://source.acts.co.za/value-added-tax-act-1991/10__value_of_supply_of_goods_or_services.php | 2026-11-05 |
| VAT Act s 11, unofficial consolidation, read in part: the paragraphs cited and s 11(3) | https://source.acts.co.za/value-added-tax-act-1991/11__zero_rating.php | 2026-11-05 |
| VAT Act s 12, unofficial consolidation, read in part: the paragraphs | https://source.acts.co.za/value-added-tax-act-1991/12__exempt_supplies.php | 2026-11-05 |
| VAT Act s 14, unofficial consolidation | https://source.acts.co.za/value-added-tax-act-1991/14__collection_of_value_added_tax_on_imported_services_determination_of_value_thereof_and_exemptions_from_tax.php | 2026-11-05 |
| VAT Act s 15, unofficial consolidation | https://source.acts.co.za/value-added-tax-act-1991/15__accounting_basis.php | 2026-11-05 |
| VAT Act s 16, unofficial consolidation, read in part: s 16(2), (3)(a) to (c) and proviso (i) | https://source.acts.co.za/value-added-tax-act-1991/16__calculation_of_tax_payable.php | 2026-11-05 |
| VAT Act s 17, unofficial consolidation, read in part: s 17(1) and (2)(a) to (c) | https://source.acts.co.za/value-added-tax-act-1991/17__permissible_deductions_in_respect_of_input_tax.php | 2026-11-05 |
| VAT Act s 18, unofficial consolidation, read in part: s 18(3) | https://source.acts.co.za/value-added-tax-act-1991/18__change_in_use_adjustments.php | 2026-11-05 |
| VAT Act s 20, unofficial consolidation, read in part: s 20(1) to (8) | https://source.acts.co.za/value-added-tax-act-1991/20__tax_invoices.php | 2026-11-05 |
| VAT Act s 22, unofficial consolidation, read in part: s 22(1) and (2) | https://source.acts.co.za/value-added-tax-act-1991/22__irrecoverable_debts.php | 2026-11-05 |
| VAT Act s 23, unofficial consolidation, read in part: s 23(1) to (3) | https://source.acts.co.za/value-added-tax-act-1991/23__registration_of_persons_making_supplies_in_the_course_of_enterprises.php | 2026-11-05 |
| VAT Act s 25, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/25__vendor_to_notify_change_of_status.php | 2026-11-05 |
| VAT Act s 27, unofficial consolidation, read in part: s 27(1) to (6) | https://source.acts.co.za/value-added-tax-act-1991/27__tax_period.php | 2026-11-05 |
| VAT Act s 28, unofficial consolidation, read in part: s 28(1) and (2) | https://source.acts.co.za/value-added-tax-act-1991/28__returns_and_payments_of_tax.php | 2026-11-05 |
| VAT Act s 39, unofficial consolidation | https://source.acts.co.za/value-added-tax-act-1991/39__penalty_and_interest_for_failure_to_pay_tax_when_due.php | 2026-11-05 |
| VAT Act s 50, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/50__separate_enterprises_branches_and_divisions.php | 2026-11-05 |
| VAT Act s 54, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/54__agents_and_auctioneers.php | 2026-11-05 |
| VAT Act Schedule 2 Part A, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/vatsch_part_a__zero_rate_.php | 2026-11-05 |
| VAT Act Schedule 2 Part B, unofficial consolidation, read in part: items 1, 2, 8, 11, 15 and 18 | https://source.acts.co.za/value-added-tax-act-1991/vatsch_part_b__zero_rate_.php | 2026-11-05 |
| GN 2835 of 22 November 1991, s 10(8) and (13) directions, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/vatregs_gnn_2835_notice_no__2935_of.php | 2026-11-05 |
| Notice 1583 of 2021, s 20(5B) tax invoices, unofficial consolidation, read in part | https://source.acts.co.za/value-added-tax-act-1991/n1583_3__tax_invoices.php | 2026-11-05 |
| GN R. 316 of 2014, Export Regulations, unofficial consolidation, read in part: reg 15 | https://source.acts.co.za/value-added-tax-act-1991/r_316_15__export_time_periods_.php | 2026-11-05 |
| GN R. 316 of 2014, Export Regulations, unofficial consolidation, read in part: reg 16 | https://source.acts.co.za/value-added-tax-act-1991/r_316_16__time_period_to_obtai.php | 2026-11-05 |
| TAA ss 187, 210, 211, 213, 222, 223 and 224, unofficial consolidation, read in part, each on its own page; URL is s 187 | https://source.acts.co.za/tax-administration-act-2011/187__general_interest_rules.php | 2026-11-05 |
| TAA s 190, unofficial consolidation, read in part: s 190(1) to (5) | https://source.acts.co.za/tax-administration-act-2011/190__refunds_of_excess_payments.php | 2026-11-05 |
| TAA s 191, unofficial consolidation, read in part: s 191(1) and (3) | https://source.acts.co.za/tax-administration-act-2011/191__refunds_subject_to_set_off_and_deferral.php | 2026-11-05 |
| Act 3 of 2026, Gazette 54446, read in part: s 13 | https://www.sars.gov.za/legal-lprim-aa-2026-01-rates-and-monetary-amounts-and-amendment-of-revenue-laws-act-3-of-2026-gg-54446-1-april-2026/ | 2026-11-05 |
| Bill B34-2026, read in part: clauses 20 and 21 | https://www.sars.gov.za/legal-lprep-bills-2026-03-rates-and-monetary-amounts-and-amendment-of-revenue-laws-bill-b34-2026-21-october-2026/ | 2026-11-05 |
| Bill B33-2026, read in part: clause 10 | https://www.sars.gov.za/legal-lprep-bills-2026-02-tax-administration-laws-amendment-bill-b33-2026-21-october-2026/ | 2026-11-05 |
| SARS Budget 2026 FAQ, read in part: VAT threshold items | https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/ | 2026-11-05 |
| SARS tax periods page, read in part | https://www.sars.gov.za/types-of-tax/value-added-tax/tax-periods-for-vat-vendors/ | 2026-11-05 |
| SARS FAQs for VAT vendors, page modified 14 April 2026, read in part | https://www.sars.gov.za/types-of-tax/value-added-tax/faqs-for-vat-vendors/ | 2026-11-05 |
| SARS BGR 16 Issue 3, 27 November 2023, read in part: background, ruling, formula and notes | https://www.sars.gov.za/legal-intr-r-bgr-16-standard-turnover-based-method-of-apportionment/ | 2026-11-05 |
| CSARS v African Bank Ltd (242/2024) [2025] ZASCA 101, read in part | https://www.sars.gov.za/wp-content/uploads/Legal/Judgments/SCA/Legal-DRJ-SCA-2025-07-CSARS-v-African-Bank-Limited-242-2024-2025-ZASCA-101-8-July-2025.pdf | 2026-11-05 |
| SCA media summary of African Bank, read in part | https://www.sars.gov.za/wp-content/uploads/Legal/Judgments/SCA/Legal-DRJ-SCA-2025-07a-CSARS-v-African-Bank-Limited-242-2024-2025-ZASCA-101-8-July-2025-MS.pdf | 2026-11-05 |
| Tax Court VAT 22498, 27 July 2026, read in part: paras 1 to 12 and 57 | https://www.sars.gov.za/wp-content/uploads/Legal/Judgments/TC/Legal-DRJ-TC-2026-07-SARSTC-VAT-22498-VAT-2026-ZATC-CPT-27-July-2026.pdf | 2026-11-05 |
| SARS VAT 404 Guide for Vendors, Issue 15, read in part; law to Acts of 2023 per its preface | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf | 2026-11-05 |
| SARS VAT201 guide GEN-ELEC-04-G01, revision 11, read in part: sections 2 to 10 | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-ELEC-04-G01-Guide-for-completing-the-Value-Added-Tax-VAT201-Declaration-External-Guide.pdf | 2026-11-05 |
| SARS VAT 411, entertainment, read in part | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/VAT-411-Guide-for-Entertainment-Accommodation-and-Catering-External-Guide.pdf | 2026-11-05 |
| SARS VAT 421, short-term insurance, read in part | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/LAPD-VAT-G10-VAT-421-Guide-for-Short-Term-Insurance.pdf | 2026-11-05 |
| SARS VAT-ELEC-01-G01, imported services, read in part | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/VAT-ELEC-01-G01-Manage-Value-Added-Tax-on-Imported-Services-External-Guide.pdf | 2026-11-05 |
| SARS Interest Rates Table 1, September 2026, read in part: the 2025 and 2026 rows | https://www.sars.gov.za/wp-content/uploads/Legal/Rates/Legal-Pub-IRT-01-Interest-Rates-Table-1.pdf | 2026-11-05 |
| SARS Interpretation Note 82, motor cars, read in part | https://www.sars.gov.za/wp-content/uploads/Legal/Notes/LAPD-IntR-IN-2015-02-IN82-Input-tax-on-motor-cars.pdf | 2026-11-05 |
| SARS Interpretation Note 68 Issue 3, read in part | https://www.sars.gov.za/wp-content/uploads/Legal/Notes/LAPD-IntR-IN-2013-01-IN68-Provisions-Tax-Administration-Act-Not-Commenced.pdf | 2026-11-05 |
| SARS Guide for Tax Rates, Duties and Levies, read in part: VAT table | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-Gen02-Guide-for-Tax-Rates-Duties-Levies.pdf | 2026-11-05 |

Not yet confirmed: enactment of R2,300,000 in s 23(1)(a), (1)(b) and (1A); enactment of R120,000 in s 23(3)(b); whether an announced threshold has any legal effect before enactment; whether B34-2026 has passed; the Category D farming limit in the Act's official text (R1,250,000 in the consolidation, R1,500,000 from SARS); the Category F limit of R1,200,000 and its status, given SARS's list of 5 categories; every legacy statement of a named supplier's billing entity or VAT status, and that banks issue monthly tax invoices; any notice applying compounded interest to VAT; the status of s 39(2); B33-2026 clause 10, which would make the last business day apply to all vendors from 1 April 2027 and is a Bill only; whether income-protection premiums are exempt; the legacy 'foreign-going ships' in the diesel refund; the VAT201 field for a s 8(8) indemnity receipt; whether notional input on capital goods goes in Field 14 or Field 15; whether Tax Court VAT 22498 is the African Bank matter and whether any further appeal exists; the date of the s 20(8) wording, given 1 January 2023 in the consolidation and 1 April 2023 in VAT 404; the Seventh Schedule 3.5% and 3.25% vehicle percentages; and the bank column layouts.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.3 | 2026-11-05 | Converted to the upstream template. `reviewed_by` removed and tier set to 2 because this text has not been reviewed. Separated enacted, announced and administered thresholds. Replaced the s 27 category table and corrected VAT201 fields 5, 7 and 15A, s 28 conditions, s 22 conditions, interest compounding, municipal rates, entertainment exceptions, apportionment, the African Bank citation, defaults and the diesel citation. Added refusal triggers and messages, the operational hold, s 16(2) documents and supplier conditions. Supplier statuses held. After an independent check: mixed use, vehicle, entertainment, imported services and cash rows made Needs Input or disclosed; refusal triggers made objective; reg 16 stated for indirect exports; `south-africa-vat` added to `depends_on`; `job` declared. After Alcuin round 1: R-ZA-2 tied to an actual input tax apportionment and extended to private and other non-taxable use; no proportional input below 95%; denied input disclosure limited to evidenced VAT; reg 15 Part One deadline and exceptions added. |
| 2.2 | November 2026 | Legacy: interest rate updated to SARS Table 1. |
| 2.1 | May 2026 | Legacy: threshold, bank charge, processor fee, field, motor car, transport, fuel and entertainment changes; a defunct airline removed. |
| 2.0 | April 2026 | Legacy: rewrite to the v2.0 structure, South African bank formats, local payment patterns and worked examples. |
| 1.0 | 2025 | Initial. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, chartered accountant (CA(SA)), or equivalent licensed practitioner in South Africa) before filing or acting upon.
