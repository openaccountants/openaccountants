---
name: nf-investment-withholding
description: >
  Establish selected Norfolk Island withholding on dividends, interest and
  royalties for 2026-27. Use for overseas payees, foreign lenders, franked
  distributions, royalty contracts, credited payments, intermediaries and
  annual non-resident reports. Covers the Australian territorial definition,
  domestic liability and payer triggers, ordinary rates, whole-dollar
  withholding rules, remittance classes and reporting distinctions. Includes
  primary legislation, current authority instructions, fictional components
  and boundary checks. Requires separate residence, treaty, exemption,
  permanent-establishment and actual-calendar evidence. Preserves applicable
  workflow outputs and holds specialised arrangements and actual financial
  submissions. This Tier 2 reference does not complete the country pack or
  provide professional sign-off.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Ordinary 1 July 2026 to 30 June 2027 financial year; sources checked 18 October 2026; payment and reporting periods must be established separately"
tier: 2
last_updated: 2026-10-18
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - nf-tax-system
  - nf-income-tax
  - nf-company-tax
---

# Norfolk Island: dividends, interest and royalty withholding

Establish the payer, recipient and intermediary, residence and permanent
establishments, payment character and source, gross amount, relevant
contract, payment/credit dates, franking and claimed relief. Record
reviewer-held evidence readiness; do not obtain private client, identity,
bank or ownership records through this reference.

Load `workflow-base`, `nf-tax-system` and the individual income-tax or
corporate income-tax workflow base and substantive references appropriate
to the entity. Preserve the confirmed profile, source and period gates,
refusals, four universal outputs and applicable domain outputs and checks.
Mandatory facts remain Needs Input; unresolved rules remain held. These
are selected components, not an actual withholding return, payment or
complete cross-border or country pack.

## Territory and source currency

The 1936 Assessment Act adopts the 1997 Act's geographical meaning of
Australia, which expressly includes **Norfolk Island**. Schedule 1 to the
Administration Act also adopts the 1997 Act's expressions. A Norfolk address
is therefore not, by itself, an overseas address for these provisions.
Establish actual tax residence; mainland/island movement is not proof of
becoming a foreign resident. [ASSESS1, section 6][ASSESS1]; [DICT, section
960-505][DICT]; [ADMIN, section 3AA][ADMIN]

The live source records checked were:

| Source | Current reading boundary |
|---|---|
| 1936 Assessment Act | C193, effective **1 October 2026**. Selected definitions and Division 11A were read. [ASSESS-RECORD]; [ASSESS1]; [ASSESS3] |
| Withholding Tax Act 1974 | Latest published compilation effective **24 September 2007**; its age does not make it superseded. Sections 6–7 impose the selected domestic tax and rates. [RATES-RECORD]; [RATES] |
| Administration Act | Latest published C226 covers **27 August–30 September 2026**. Its live amendment list also identifies October Acts 71 and 86. Their relevant targets were checked before using selected Schedule 1 provisions; C226 is not described as all-law current. [ADMIN-RECORD]; [ADMIN-VERSIONS]; [REFORM2]; [OCTOBER] |
| Administration Regulations | C17, effective **27 August 2026**, including sections 26 and 39–45. [REGS-RECORD]; [REGS] |
| Agreements Act | C47, effective **1 October 2026**, including treaty priority and royalty exclusions. Actual treaty texts and application are still required. [AGREEMENTS-RECORD]; [AGREEMENTS] |
| ATO annual report instructions | Live page dated **4 September 2026**, used instead of the older printable search result. [ANNUAL] |

The October Act's Schedule 8 credit-timing amendments expressly concern
**Subdivision 14-D capital gains withholding**. They do not supply a general
dividend, interest or royalty credit-timing rule. Its other selected
Administration Act targets concern foreign-property declarations and
giving funds; Act 71's target concerns loss carry-back instalment mechanics.
Neither replaces the selected Subdivision 12-F and Division 16 wording
used below. Use `nf-cgt` for selected capital-gains rules; actual capital
gains withholding remains a separate analysis. [OCTOBER]; [REFORM2]

## Classify the income and underlying liability first

Read payment substance rather than the invoice label:

- **Interest** includes amounts in the nature of, substituted for, or
  received in exchange for interest in the specified arrangements, and
  non-equity-share dividends. It excludes a return on a company equity
  interest. Qualifying securities, hire purchase, debt/equity and interposed
  entities require their own provisions. [ASSESS3, section 128A][ASSESS3]
- **Royalties** include specified rights, equipment, knowledge and ancillary
  assistance, as well as specified broadcasting and forbearance payments.
  A one-off payment can qualify. Software, services and equipment contracts
  require their actual rights and relevant treaty definition; do not label
  every foreign software or service invoice a royalty. [ASSESS1, section
  6][ASSESS1]; [TYPES]; [AGREEMENTS, section 17A][AGREEMENTS]
- **Dividends** require the distribution and equity classification. The
  franked and unfranked portions, conduit foreign income, non-share
  dividends and any anti-avoidance determination require separate evidence.
  A foreign payee is not entitled to an automatic refund of a franking
  credit through this guide. [ASSESS3, sections 128AAA, 128A and
  128B][ASSESS3]; [TYPES]; `nf-company-tax`.

The main domestic liability branches are:

| Payment | Selected section 128B branch |
|---|---|
| Resident-company dividend to a non-resident | Subsection (1), subject to its exclusions. The franked part is generally excluded under (3)(ga), with the stated determination and financing exceptions. An attributable Australian PE dividend has its separate (3E) conditions. [ASSESS3] |
| Interest to a non-resident from a resident payer | Subsection (2)(b)(i); the wholly foreign-business/foreign-PE outgoing exclusion and the partial-outgoing rules must be considered. A private loan is not automatically excluded merely because the borrower is not a business. [ASSESS3]; [WHO] |
| Interest to a non-resident from a non-resident payer | Subsection (2)(b)(ii), where the outgoing is incurred wholly or partly in the payer's Australian PE business; subsection (7) limits the amount for a partial outgoing. [ASSESS3] |
| Royalty to a non-resident | Subsection (2B), with resident-payer/foreign-PE and non-resident-payer/Australian-PE branches. Do not omit the equity-return exclusion in (2D) or treaty analysis. [ASSESS3] |
| Interest or royalties derived by a resident through a foreign PE | Subsections (2A) and (2C) can apply despite the recipient's residence. Do not replace these with a rule that every resident recipient is outside withholding. [ASSESS3] |

Section 128B contains further exemptions and special rules. Temporary
resident interest, public-offer debt, foreign superannuation funds,
sovereign entities, charitable bodies, shipping, trusts and conduit income
are not established by a label or an ABN. In particular, the foreign-fund
exception has additional participation, historical holding and influence
conditions. Keep unverified eligibility held. [ASSESS3]; [TYPES]; [WHEN]

## Identify who must withhold and when

Liability and the collection trigger are separate tests. Subject to section
12-300's limits:

| Payer or intermediary | Trigger |
|---|---|
| Australian resident company | Dividend holder's overseas address in its register, or authority/direction to pay an entity at an overseas place: section 12-210. Part dividends are also covered. [ADMIN, sections 12-210, 12-220][ADMIN] |
| Interest or royalty payer | Overseas address in the relevant transaction records, or authority to pay at an overseas place: sections 12-245 and 12-280. A domestic bank payment destination does not erase an overseas-address trigger. [ADMIN] |
| Australian person/government agency receiving for a foreign resident | Sections 12-215, 12-250 and 12-285; withhold immediately after receipt if the foreign resident is already entitled, otherwise immediately after that entitlement arises. [ADMIN] |
| Interest derived by a resident lender through a foreign PE | Sections 12-255–12-260 include the lender's written notification branch and separate Commissioner notification. Obtain the actual transaction and notice conditions. [ADMIN] |

Constructive payment matters. Applying or dealing with an amount on the
recipient's behalf or as directed can constitute payment. Interest or
royalty reinvestment, accumulation or capitalisation is not automatically
deferred until cash is transferred. Crediting or distributing a dividend
can also count. A bare accounting accrual is not automatically the same
as every statutory credit or constructive payment. [ADMIN, section 11-5][ADMIN];
[ASSESS1, section 6 definition of paid][ASSESS1]; [ASSESS3, section 128A(2)][ASSESS3];
[WHEN]

For a jointly held account, do not simply halve the foreign-resident
withholding. The ATO distinguishes the resident holder's TFN/ABN or
exemption compliance: if satisfied, non-resident withholding applies to
the whole relevant payment; if not, the TFN/ABN provisions apply to the
whole payment. Their actual rate and eligibility require separate
verification. Do not collect a TFN through this guide. [ATO-RATES]

Section **12-300** requires no withholding under Subdivision 12-F where no
withholding tax is payable, and caps withholding at the tax payable less
amounts already withheld from that payment **under that Subdivision**.
Do not offset an unrelated wage, GST, instalment or capital-gains amount.
Absence of this withholding does not prove absence of assessment tax.
[ADMIN]; [ASSESS3, sections 128B and 128D][ASSESS3]

## Domestic amounts, relief and rounding

For a confirmed ordinary taxable payment with no applicable lower rate,
exemption, variation or special branch:

| Payment component | Domestic rate |
|---|---:|
| Taxable unfranked dividend | **30%** |
| Interest | **10%** |
| Royalty | **30%** |

These rates follow Withholding Tax Act section 7 and the corresponding
Administration Regulations sections 40–42; they are not a universal rate
table for all overseas payments. Dividend and royalty regulations include
their treaty/tax-sharing branches. Section 12-300's liability cap also
applies. [RATES]; [REGS]; [ADMIN]; [ATO-RATES]

Before treaty relief, verify the actual agreement and protocols, force and
payment dates, its territorial definition and covered taxpayer/tax,
residence and any dual-residence resolution, beneficial ownership,
income article, PE connection, special relationship and anti-abuse/MLI
conditions. A treaty with another country or an information-exchange
agreement alone does not prove a reduced rate for this payment. The
Agreements Act gives applicable provisions force according to their tenor
and priority subject to its exceptions. Section 17A also excludes certain
domestic royalties where the applicable agreement does not treat the
amount as a royalty; the result need not be a reduced royalty percentage.
No particular treaty outcome is selected here. [AGREEMENTS, sections 4,
5 and 17A][AGREEMENTS]; [REGS, sections 40–45][REGS]

Regulation **26** applies to payment amounts dealt with under Part 3's
Divisions 2–3 and the amounts worked out under those divisions: disregard
an amount below **A$1** and discard cents above a whole dollar. It is not
rounding to the nearest dollar or a general tax-liability exemption.
Apply the correct gross payment/component, the regulations and the
section 12-300 cap; retain the difference between the original gross cash
payment, the withholding working and net cash. Contractual gross-up,
foreign currency and non-cash payments need further analysis. [REGS]

## Registration, remittance and reports

An entity required to remit within section 16-140 must apply to register,
in the approved form, by its first withholding/payment obligation unless
the Commissioner allows more time. Norfolk supplier no-ABN relief is not
an exemption from this separate regime. Do not submit a registration or
use private identifiers through this reference. [ADMIN]; `nf-tax-system`.

Amounts withheld under Division 12 must be paid to the Commissioner.
Select the actual withholder class, deferred-BAS status, statement,
variations and calendar before a due date. Statutory section 16-75 branches
include:

| Withholder | Statutory timing, subject to the applicable branch |
|---|---|
| Medium, not deferred BAS | **21st day of the following month**. |
| Medium, deferred BAS | **28th day of the following month**, except December amounts use the following **February**. |
| Small, not deferred BAS | **21st day of the month after the quarter**. |
| Small, deferred BAS | September quarter: **28 October**; December: **28 February**; March: **28 April**; June: **28 July**. |
| Large | Separate weekday-dependent table; not the ordinary monthly or quarterly rule. |

These are statutory branches, not an engagement calendar. Confirm actual
class, permitted extensions, weekend/public-holiday treatment and any
current notification before finalising. Notification under section 16-150
is generally due by payment due date even if the amount has not been paid.
The annual report deadline is not permission to retain withholding until
October. [ADMIN, sections 16-70, 16-75 and 16-150][ADMIN]

The ATO's **NAT 7187** report covers interest and unfranked dividends not
reported on an AIIR, and royalties. The live instructions specify
**31 October each year**, online or paper reporting, and a private-investor/
non-enterprise exclusion where both stated conditions apply. Correctly
reported interest/dividends on the AIIR need not be duplicated on NAT 7187;
that is not a royalty, payment or all-reporting exemption. The current
online route uses the published template and authorised online services;
no old electronic-storage-media specification is adopted here. [ANNUAL];
[OBLIGATIONS]; [ADMIN, section 16-153][ADMIN]

Issue the required payment summary separately. Section 16-155's ordinary
annual rule is **within 14 days after the financial year**, subject to its
coverage and exclusions; section 16-170 specifies content and allows
particular variations. A certificate of payment for a payee's foreign
authority is additional to the payment summary, and requires the ATO's
own application and reporting conditions. Do not confuse a certificate
with withholding remittance or a summary. [ADMIN]; [OBLIGATIONS]

Interest/royalty deductibility has a separate compliance gate. Section
26-25 denies a deduction in the specified withholding/remittance failures;
subsection (3) restores an otherwise allowable deduction **for that income
year** when the withholding tax is paid. Payment does not itself create a
deduction or move it automatically into the later payment year. Ordinary
deductibility, related-party, debt and other limitations still apply.
[CORE]; `nf-company-tax`.

Section 128D makes selected withholding income non-assessable non-exempt,
with express exclusions including the foreign-PE resident branches. The
ATO explains the ordinary foreign payee's final-tax position where the
correct withholding has been made and there is no other assessable
Australian income. Do not turn that into a universal no-return rule for
every foreign recipient or additional income. [ASSESS3]; [OBLIGATIONS]

## Fictional 2026–27 components and boundary checks

All amounts below are Australian dollars. The examples stipulate ordinary
taxable cash payments, no treaty relief or special exemption, correct
classification and no variation. They are not completed withholding
statements or actual tax liabilities.

| Stipulated payment | Selected working |
|---|---|
| Interest of A$20,000 | A$20,000 × 10% = **A$2,000 withheld**; cash after withholding **A$18,000**. |
| Dividend of A$10,000, with A$6,000 validly franked and A$4,000 taxable unfranked; no determination/financing exception | A$4,000 × 30% = **A$1,200 withheld**; total cash after withholding **A$8,800**. Do not add the franking credit to the withholding base. |
| Royalty of A$8,000 | A$8,000 × 30% = **A$2,400 withheld**; cash after withholding **A$5,600**. An unresolved treaty classification instead holds the actual outcome. |
| Tax payable on one payment is A$1,200; A$500 already withheld from it under Subdivision 12-F | Section 12-300 caps further withholding at **A$700**, not another A$1,200. |
| Interest amount A$19.99, applying ordinary regulation 26 mechanics | Discard payment cents: **A$19**; 10% gives A$1.90; discard resulting cents: **A$1**. This is a withholding working, not a finding that the recipient's tax liability is A$1. |
| Same interest payment below A$1 | Disregard it for the regulations' amount working. Do not promote this rule to every tax or reporting obligation. |
| Joint resident/foreign-resident interest account; resident satisfies TFN/ABN obligations; interest A$1,000 | Ordinary non-resident withholding on the **whole A$1,000** is **A$100**, not A$50. With missing resident compliance, select the different TFN/ABN branch and hold its amount. |
| Interest capitalised as directed for a foreign lender | Test constructive payment at capitalisation; do not wait automatically for a later bank transfer. |
| Medium, non-deferred payer with a September 2026 withholding amount | Statutory monthly branch points to **21 October 2026**, subject to actual classification and calendar checks; the annual report date is separate. |
| Only a Norfolk address, foreign passport or overseas payment account is known | Needs Input on actual tax residence and the relevant payer/recipient and transaction conditions. No automatic zero or 30% result. |

## Review checks and remaining country requirements

Check liability before rate; payer versus recipient; ordinary versus
constructive payment; franked versus taxable unfranked portions; treaty
classification before a percentage; prior withholding on the same payment;
input and output whole-dollar treatment; remittance versus annual report
and payment summary; AIIR overlap; and deduction restoration for the
otherwise eligible income year. Do not apply the CGT withholding credit
amendment to this regime by analogy.

Keep actual treaties, MLI/protocol interaction, residence disputes, PE
attribution, conduit calculations, special funds and public debt,
interposed/deemed payments, AMIT/MIT, natural-resource, foreign-worker,
entertainment/construction, non-cash, foreign currency, gross-up,
refund/variation, notices, exact forms and actual lodgment calendars held
until their own primary evidence and workflow gates are satisfied.
Transfer pricing, CFC/hybrid rules, foreign credits, comprehensive company
and individual returns and the other open country slots remain separate
work. Neither these examples nor repository checks confer professional
sign-off or comprehensive-country acceptance.

[ASSESS-RECORD]: https://www.legislation.gov.au/C1936A00027/latest/details
[ASSESS1]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[ASSESS3]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[CORE]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[RATES-RECORD]: https://www.legislation.gov.au/C2004A00086/latest/details
[RATES]: https://www.legislation.gov.au/C2004A00086/2007-09-24/2007-09-24/text/original/epub/OEBPS/document_1/document_1.html
[ADMIN-RECORD]: https://www.legislation.gov.au/C1953A00001/latest/details
[ADMIN-VERSIONS]: https://www.legislation.gov.au/C1953A00001/latest/versions
[ADMIN]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[OCTOBER]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html
[REGS-RECORD]: https://www.legislation.gov.au/F2017L01227/latest/details
[REGS]: https://www.legislation.gov.au/F2017L01227/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[AGREEMENTS-RECORD]: https://www.legislation.gov.au/C1953A00082/latest/details
[AGREEMENTS]: https://www.legislation.gov.au/C1953A00082/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[TYPES]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/interest-dividends-royalties-and-mit-payments
[WHO]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/who-withholds
[WHEN]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/when-to-withhold
[ATO-RATES]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/withholding-rate
[OBLIGATIONS]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/obligations
[ANNUAL]: https://www.ato.gov.au/forms-and-instructions/payg-withholding-from-interest-dividend-and-royalty-payments-to-non-residents-annual-report

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network
