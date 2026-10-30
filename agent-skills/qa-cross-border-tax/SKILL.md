---
name: qa-cross-border-tax
description: "Qatar mainland cross-border income tax for 2026, covering nonresident businesses, permanent establishments, service and royalty withholding, treaty refund routing, foreign income and foreign tax credits, registration, cessation notifications and capital-gains filing. Use for payments to overseas consultants or associated companies, Qatar projects, offshore services used in Qatar, tax residence, foreign branches, withholding gross-ups, or moving business activity abroad. Includes foreign-income inclusion and exemptions, substance screening, statutory credit computation, PE expense attribution and business cessation. Separates domestic source rules from treaty entitlement and documents the 2026 approved-payer direct-relief conditions. Qatar Financial Centre, free-zone relief, treaty-specific rate tables and global minimum tax calculations require separate analysis. Produces working papers for qualified professional review."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/qa-cross-border-tax"
  jurisdiction: "QA"
  tax_year: "2026"
  last_updated: "2026-10-28"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Qatar cross-border income tax v0.2

## Who this applies to

This Guide covers the ordinary General Tax Authority (GTA) income-tax regime,
including mainland taxpayers paying nonresidents and overseas businesses
operating in Qatar. It does not apply QFC tax rules to a mainland company, or
assume a free-zone exemption. All references below to the Income Tax Law (ITL)
and Executive Regulations (ER) refer to the [current Arabic ITL](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065)
and [current Arabic ER](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35).
The [GTA 2024 English compilation](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf)
provides a translation for the provisions it contains, but predates later
amendments and does not override the Arabic text.

ITL art. 1 defines an individual resident as someone with a permanent home
available in Qatar, present for more than 183 days in the year, or holding
Qatari nationality. Its amended entity definition links establishment in Qatar
with main and actual management and control in Qatar. A Qatari project is a
project managed by a resident. Determine residence under this amended text and
then the applicable treaty; a visa or commercial registration alone does not
settle treaty residence. Substantial-activity failures can prevent a residence
certificate: ITL art. 11 Bis.

For nonresidents, distinguish a Qatar permanent establishment (PE) from payments
not connected with a PE. Under ER art. 1, PE cases include a fixed business
location, a construction/installation project lasting **more than six months**,
and services through personnel exceeding **183 days within twelve months**.
Dependent-agent, insurance and anti-fragmentation rules also require analysis;
an independent agent exception is conditional. A parent/subsidiary relationship
alone does not create a PE. A treaty can change the applicable test; do not use
these domestic periods as a treaty conclusion.

## Rates, bands and thresholds

| Item | Amount or rule | Tax year | Official source and provision |
|---|---|---|---|
| Ordinary income tax | 10% of taxable income; exemptions and special rates require separate testing | 2026 | [ITL arts. 4 and 9](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf) |
| Nonresident final withholding | 5% of gross royalties, interest, commissions and qualifying service fees, where not connected with a Qatar PE; subject to treaty provisions | 2026 | [ITL art. 9, second paragraph (2)](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf) |
| Construction/installation PE | More than 6 months | 2026 | [ER art. 1(2)(a)](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf) |
| Personnel service PE | More than 183 days in a 12-month period starting or ending in the fiscal year concerned | 2026 | [ER art. 1(2)(b)](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf) |
| Withholding on unpaid accrued amounts | Deemed paid after at most 12 months from entitlement, except amounts owed **by** ministries, other government bodies, public authorities and institutions | 2026 | [Current Arabic ER art. 21(1)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35) |
| Foreign tax credit | Qualifying foreign income tax actually paid, net of refunds, capped at Qatar tax due; none on Qatar-exempt income | 2026 | [ITL art. 20](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf) |

The salary exclusion is in art. 2(3) of the law's **promulgation articles**.
Do not turn that into a universal exemption for an individual's business income.
Petroleum/petrochemical and contractual special rates are outside this ordinary
business computation: ITL art. 9. [Qatar's global minimum tax](https://www.gta.gov.qa/en/global-minimum)
applies in addition to ordinary income tax and needs its own calculation.

## The base

### Payments to nonresidents

1. Identify the payer, recipient, residence, contract, actual services and any
   Qatar PE connection. ER art. 21 covers resident legal persons, people carrying
   on activities, government bodies and Qatar PEs as payers.
2. Classify the amount under ITL art. 9(2). Do not withhold merely because a
   supplier is foreign; equally, do not assume an offshore invoice is exempt.
3. ER art. 21(2) includes work necessary for completion performed in Qatar,
   including data collection and site inspection by another person. The official
   consolidated text also treats services **used, consumed or benefited from in
   Qatar** as performed there even when work is done outside Qatar. Mere delivery
   is not itself the completion test. Record the evidence of use and performance.
4. Apply the 5% rate to the **gross amount without cost deductions**. If the
   contract guarantees a net payment and the payer bears the tax, solve gross
   consideration as `net / (1 - 0.05)`. This is a contractual gross-up assumption,
   not a rule that every invoice must be grossed up.
5. Test exclusions. ER art. 21 excludes reinsurance, shipping/ticket sales,
   specified maritime oil transport and enumerated interest, including interest
   on transactions/facilities/loans with banks or financial institutions and
   interest paid by a Qatar PE to its foreign head office or affiliate. Head-office
   administrative/general expenses within ER art. 7 are also excluded by
   art. 21(1). Document the actual category before claiming an exclusion.
6. ER art. 23 excludes amounts paid to a person issued a tax card or registered
   with QFC. Check valid evidence and recipient identity; do not treat any foreign
   tax number as a Qatar tax card. Qatari/GCC ownership of a **nonresident**
   recipient company does not itself switch off withholding: ER art. 22(3).
7. Apply the treaty procedure below and preserve the withholding certificate.

Source for these rules: [ITL art. 9 and ER arts. 7, 21–24](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf).
The [GTA withholding summary](https://www.gta.gov.qa/en/taxes-info) is useful
operational guidance but does not reproduce every sentence of the consolidated ER.
For the twelve-month accrual exception, read the [Arabic ER art. 21(1)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35):
it concerns government **payers**, not a private payer's governmental recipient.
The English compilation's “due to” wording reverses that distinction.

### Qatar PE attribution

Under amended [ER art. 7](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35),
first apply the treaty. Domestic attribution includes the PE's own profit and
Qatar sales of the same/similar goods and other same/similar Qatar activities
specified in art. 7(1), rather than allocating only by the PE's invoices.
Attribute the profit of a distinct, separate enterprise performing the same
functions in comparable conditions, dealing independently with the enterprise.

Build the PE reconciliation from those attributable receipts less allowable
external operating costs and actual head-office executive/general administrative
costs incurred for the PE. Use a documented allocation tied to the underlying
costs and PE benefit. Do **not** apply the replaced generic 3% head-office cap.
Art. 7(3) disallows internal notional royalties, management/service commissions
and lending interest paid to the head office/other offices, other than actual
expense reimbursement; the banking exception must be tested separately. It also
ignores corresponding internal notional receipts charged by the PE, subject to
the same exception. Add back barred internal charges, apply the ordinary
[corporate deductions, depreciation and loss rules](qa-corporate-income-tax.md),
and use the same attribution method each year unless a justified acceptable
reason supports changing it: ER art. 7(4). Pricing documentation does not turn
an internally booked notional charge into a deductible payment.

### Foreign-income inclusion and exemptions

The amended law is **not** a blanket Qatar-source-only rule. A Qatari project
is a project managed by a resident under ITL art. 1. Make an income-by-income
schedule with payer/source state, foreign PE connection, gross receipt, associated
expenses, exemption conditions, foreign assessment, payment and refunds:

| Foreign category | Inclusion/exclusion step | Current provision |
|---|---|---|
| Real-estate use, letting or other exploitation | Art. 2 Bis includes it subject to its express conditions: the beneficiary does not operate through a PE in the property state and the property is not effectively connected to that PE | ITL art. 2 Bis |
| Foreign dividends, interest and royalties | Included under the analogous foreign-PE/effective-connection conditions; do not presume all foreign dividends exempt | ITL art. 2 Bis/1 |
| Foreign technical-service fees | Included subject to the specified foreign-PE and effective-connection conditions | ITL art. 2 Bis/2 |
| Disposal of foreign property | Included first; then test the specific gains exemption below | ITL art. 2 Bis/3 and art. 4(6) |
| Foreign PE profits | Excluded if attributable to that PE and subject to tax in that foreign state | ITL art. 2 Bis/4 |
| Distribution rights; marketing, procurement, financial brokerage, agency/other intermediary services; guarantees/similar financial support; telecom/broadcast services | Specified foreign income included, with the applicable PE exclusion and exemptions tested separately | ITL art. 2 Bis/5 |

Source: [current Arabic ITL arts. 1–4](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065).
Do not replace the two numbered conditions in arts. 2 Bis–2 Bis/2 with an
unsourced general foreign-PE rule. Preserve the particular category's facts and
apply art. 2 Bis/4 to actual foreign-PE profit.

ITL art. 4(6) covers a Qatari project's foreign real estate, movable property
forming part of its foreign PE including transfer of that PE, and foreign shares,
interests/rights. Art. 4(7) covers its foreign board-member fees. Under
[ER art. 2(5)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35),
these exemptions require the foreign tax condition and substantial activity
where applicable. Keep foreign assessment/payment and substance evidence before
removing the gain/fee. ITL art. 4(8)'s dividend exemption requires distributions
from profits taxed or exempt under the specified Qatar law conditions; it is
not an automatic participation exemption for every overseas dividend. Ownership,
listed-security and natural-person exemptions have their separate art. 4/ER
art. 2 conditions. Use the current Arabic numbering: the English compilation
misnumbers some exemption subclauses.

Remove expenses of Qatar-exempt income from the deductible base. Allocate shared
expenses using accurate regular records; absent those, ER art. 6 uses taxable
revenue divided by total revenue. The English translation suggesting deduction
of exempt-income expenses is wrong; the Arabic provision prohibits it. See the
[corporate Guide](qa-corporate-income-tax.md) for the full reconciliation.

### Substantial-activity working paper

[ER art. 34 Bis](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35)
implements ITL art. 11 Bis. Record each test for the preceding two financial
years rather than labelling every holding company a shell:

1. More than 75% of accrued revenue is relevant income (real-estate income,
   dividends, interest or royalties).
2. More than 60% of book assets are abroad **or** more than 60% of relevant
   income is earned/paid through foreign transactions.
3. Daily operations and significant decision-making functions were outsourced.

All three screening criteria are required. Then test the exclusions in
art. 34 Bis(2): qualifying regulated-market securities issuers, licensed financial
institutions, specified domestic-shareholding enterprises whose beneficial
owners are Qatar tax residents, Qatar-resident holding companies with the
specified resident owners/ultimate parent, and enterprises with at least five
full-time employees exclusively carrying out relevant-income activities.
Document the actual exclusion rather than treating five employees in unrelated
work as enough.

An in-scope project discloses in its annual income-tax return whether it has
its own/exclusively used Qatar premises, at least one active Qatar bank account,
and either (a) a Qatar-tax-resident director with actual, regular and independent
authority over relevant activities/assets who is not an employee/director of an
unrelated enterprise, or (b) a majority of full-time employees Qatar-tax-resident.
Retain the premises, bank, decision-making, director and payroll evidence.
Failure to report, meet the indicators or supply supporting evidence triggers
ITL art. 11 Bis's lack-of-substance consequences, including refusal of a residence
certificate; dependent foreign-income exemptions must be reconsidered. ITL
art. 24(9) provides a financial penalty of 15% of net income for breach of the
substantial-activity requirements. This is separate from the ordinary 10% rate.

### Foreign-tax-credit computation

Under [ITL art. 20](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065):

1. Finish the Qatar taxable-income reconciliation, including only taxable
   foreign receipts less allowable associated costs, and excluding exempt PE
   profits/gains and their costs. Apply eligible ordinary losses and the
   applicable ownership exemptions before computing Qatar tax.
2. For each taxable foreign income item, identify an income tax imposed by
   the foreign state, political subdivision or local authority, **actually paid
   by this taxpayer**, less any foreign refund. Exclude tax on Qatar-exempt
   income, unpaid accruals, penalties, VAT/customs and tax merely paid by a
   different company. Do not assume an underlying corporate-tax credit for a
   shareholder without a separate legal entitlement.
3. Sum the eligible net foreign income taxes. The statutory credit is
   `min(eligible foreign income tax actually paid net of refunds, Qatar tax due)`;
   remaining Qatar liability is `max(0, Qatar tax due - credit)`. Art. 20 states
   this Qatar-tax cap, not a per-country basket or a foreign-income fraction
   formula. Do not introduce either without a separately applicable source.
4. Keep the item-level eligibility schedule, assessment, payment/refund proof,
   currency reconciliation and credit-to-return bridge. No carryforward,
   carryback or refund of excess credit is asserted by this provision. A treaty
   credit article must be read independently for the specific case.

### Cessation, asset transfers and migration

A departure, branch closure or change in management location requires a
residence, source, PE and asset-by-asset analysis; it is not automatic clearance.
For an actual taxable business disposal, [ER art. 5(2)](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35)
measures proceeds at the higher of agreed price and market value, less cost for
non-depreciable assets or net book value for depreciable assets; shares use the
documented capital interest. Reconcile the tax basis and accumulated depreciation,
related-party pricing, ownership exemptions and allowable losses. Foreign gains
must first pass the inclusion and conditional exemptions above. A qualifying
in-kind contribution to a resident joint-stock company has the specific ITL
art. 4(5) exemption and five-year registered-share retention condition; it is
not a general exemption for every restructuring.

For a pure management/residence migration with no disposal, do not invent a
deemed-sale charge from the disposal formula or conclude that every asset escapes
tax. Record whether a legal/economic transfer, PE disposal, taxable receipt or
continuing Qatar-source business exists and apply those specific charges. These
ordinary provisions establish the actual-disposal/cessation computation, not a
universal residence-departure valuation rule. Specialist reorganisations and
regime-specific migration relief require their own law. Follow the notice and
cessation-return rules below even where an exemption removes the tax.

## Deadlines and filing

| Obligation | Statutory timing | Official provision |
|---|---|---|
| Income-tax registration | Within 60 days from the earliest approval to start, commercial registration or first income; same day if registration for another tax purpose applies | ER art. 25(1) |
| Ordinary resident/PE tax return | Within 4 months after the tax/accounting year ends | ER art. 29(1), (3) |
| Tax due on return | On the day the return is submitted | ITL art. 20 |
| Withholding return/payment | **Before the 16th** of the month following withholding; issue prescribed recipient certificate | ER art. 24 |
| Capital-gains return | Within 30 days of contract or disposal, whichever is earlier; determine the applicable asset/annual-return treatment | ER art. 29(2); GTA capital-gains guidance |
| Cessation/disposal notice | Within 30 days after disposal or cessation; return within that period removes separate notice requirement | ER art. 28 |
| Changes affecting tax obligations | Notify within 30 days | ER art. 27 |
| Accounting evidence | 10 years following the relevant year, longer for an ongoing dispute | ER art. 36 |

File via [Dhareeba](https://dhareeba.gov.qa/), keeping the tax type, period,
submitted forms, payment receipt and certificates. Sources: [law and
ER](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf),
[GTA tax guidance](https://www.gta.gov.qa/en/taxes-info) and
[GTA investor guide](https://www.gta.gov.qa/en/investors-guide).
An extension for an annual return is not automatically an extension for
withholding, a capital-gains return or a cessation return.

Business cessation includes partial cessation and branch closure; mergers and
demergers can constitute total cessation. ER art. 29(8) requires the return by
the notification deadline on cessation/transfer, with filing obligations
continuing until notification. Do not give someone departing Qatar an automatic
tax clearance or a universal zero exit-tax conclusion. This Guide establishes
these notice/filing duties alongside the actual-disposal valuation and conditional
foreign-gain exemption analysis above.

ER art. 37 also requires reporting contracts with nonresidents without a Qatar
PE regardless of value. Under art. 37(5), notify within **30 days** from the
GTA request or conclusion of the contract/agreement, as applicable; GTA can
extend that period for a similar period if necessary. Contract notification is
separate from withholding. Source: [GTA Arabic compilation, ER art. 37(5),
printed p. 36](https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%202024.pdf).
The register's rendered art. 37 omits paragraphs (5)–(6); [Decision 3/2023 art. 1](https://almeezan.qa/legislations/0291f2d0-b545-48e4-82b5-51480e807884)
replaces only paragraphs (3) and (4), not the whole article. The Arabic
compilation preserves the notification deadline. For cessation, see
[ER arts. 28–29](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35).

## Penalties and interest

| Breach | Financial penalty | Official provision |
|---|---|---|
| Late ordinary income-tax return | QAR 500/day, maximum QAR 180,000 | ITL art. 24(1) |
| Late tax/withholding remittance | 2% of due tax for each month or part, maximum that tax | ITL art. 24(2) |
| Registration/notification breach | QAR 20,000 | ITL art. 24(3) |
| Failure to withhold | Amount equal to tax not withheld, in addition to the tax | ITL art. 24(7) |
| Specified contract-notification breach, other than government entities | QAR 10,000 | ITL art. 24(6) |
| Specified failure to keep complete/accurate required records, supply them on time or avoid premature destruction | QAR 30,000 | ITL art. 24(10) |
| Requested information/document not supplied on time | QAR 200 per missing item/document, capped at QAR 72,000; includes another person possessing/controlling it | ITL art. 24(11) |
| Incomplete/incorrect information supplied | QAR 100 per item, capped at QAR 10,000 per registration, return, notice or application; where it causes incorrect tax, the provision imposes 50% of the resulting unpaid tax | ITL art. 24(12) |

Sources: [current ITL art. 24](https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065)
and [Law 22/2024 arts. 3 and 5](https://almeezan.qa/legislations/3643a42a-bdc0-4546-95d6-975557616a1b).
Art. 24(10)–(12) took effect on 1 January 2025 and are general ITL penalties,
not confined to Pillar Two. Art. 24(10) also penalises the last managers/persons
in charge in the specified failure to retain records for five years after
dissolution; it does not shorten an otherwise longer retention/dispute duty.
These are distinct offences. Do not describe failure to withhold as merely a
late-return fine. ITL art. 24(9) imposes 15% of net income for a substantial-activity
requirements breach; use the screening and evidence analysis above.

## Cross-border points

Use the [GTA treaty directory](https://www.gta.gov.qa/en/agreements) to identify
the treaty, then read its text, protocols, effective dates and any applicable
multilateral modifications. Determine residence, beneficial ownership where
required, PE connection and the income article before calculating relief.
A signature date alone does not prove a treaty applies to the payment period.

ER art. 22(1) provides a **refund application** by the nonresident or representative
where an effective treaty supports relief, using the GTA form; preserve the
withholding certificate, residence evidence, contract, payment and entitlement
analysis. An accepted claim is refunded. The refund route continues alongside
the following direct route; ordinary payers do not gain approved status merely
by holding a recipient residence certificate.

### Direct treaty benefits through an approved payer

[Cabinet Decision 4/2026](https://almeezan.qa/legislations/f6bfa17b-9d1d-47fc-97b3-873859357599)
inserted ER arts. 22 Bis–22 Bis/3, effective **16 March 2026** (art. 3:
the day after Gazette publication on 15 March). Before that amendment, this new
approved-payer mechanism was unavailable; ordinary withholding and the existing
refund route applied, subject to a separately applicable GTA treaty circular.
The domestic 5% WHT rate did not change. Read the current procedure with
[GTA President's Decision 8/2026, art. 1](https://www.gta.gov.qa/assets/pdf/Decision%20of%20the%20President%20of%20the%20General%20Tax%20Authority%20No.%20(8)%20of.pdf):

- **Payer threshold:** in the preceding year, at least **1,250 reported WHT
  transactions OR QAR 10,000,000 actually withheld**. The money test is tax
  withheld, not gross invoices or turnover. Decision 8 art. 2 exempts entities
  granted status by GTA for compliance purposes from these volume thresholds;
  it does not remove approval or the other conditions. Decision 8 art. 3 makes
  its thresholds effective from issuance on 2 April 2026; do not backdate those
  published operating thresholds to payments before that decision.
- **Approval:** the registered payer applies on the GTA form with the prescribed
  resource/compliance information and questionnaire. GTA decides within 60 days;
  silence is rejection. Status lasts three years; apply for renewal at least
  60 days before expiry. Withdrawal is reasoned and bars regrant for one year:
  ER art. 22 Bis/1. Keep the actual approval and validity period.
- **Eligible payment:** an approved payer's contract payment to a treaty-resident
  nonresident, not connected with a Qatar PE, within the covered WHT categories;
  the provisions also cover qualifying continuing payments under existing
  contracts: art. 22 Bis.
- **Recipient application:** before payment, apply to the approved payer with a
  residence certificate, beneficial-owner and no-PE-connection evidence, the
  applicable treaty article/rate and proof of all entitlement conditions at the
  benefit date. The recipient must declare that it has made no arrangement whose
  main purpose is obtaining treaty benefits: art. 22 Bis/2.
- **Payer review:** carry out and retain due diligence, establish the actual
  beneficial use of the services and absence of an intermediary financial
  arrangement, and respond to the recipient within 60 days. Silence rejects
  the application; the recipient has no appeal against that payer rejection
  under this direct procedure. Notify GTA of the nature/amount and recipient;
  provide requested information within 30 days: art. 22 Bis/3.
- **Liability:** the approved payer bears unwithheld tax and the applicable
  penalties if direct-benefit conditions are not met or the treaty is misused. Only apply the evidenced treaty
  benefit after the approval, payment and recipient tests pass; retain the
  domestic-rate computation and the precise relief calculation. If direct
  conditions fail, use ordinary withholding and examine the refund route.

Source: [current ER arts. 22–22 Bis/3](https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35),
Decision 4/2026 and Decision 8/2026 above. No treaty-specific rate is assumed.

Keep domestic and treaty PE tests separate. Assess foreign tax and filing duties
in the other country as well. TP documentation and nonresident withholding are
separate obligations: see [qa-transfer-pricing](qa-transfer-pricing.md).
The QFC, free-zone and Pillar Two regimes and treaty-specific rate tables are
out of scope. The [GTA minimum-tax framework](https://www.gta.gov.qa/en/global-minimum)
confirms that minimum tax operates in addition to ordinary income tax.

## Two worked examples that recompute

### 1. Consultancy performed in Qatar

A mainland company pays a nonresident consultant a gross QAR 100,000 for work
performed entirely in Qatar. Assume no Qatar PE, tax-card/QFC exclusion or
applicable treaty relief. ITL art. 9(2) and ER art. 21 give QAR 5,000 withholding
and QAR 95,000 cash to the consultant. If payment occurs in November 2026,
remit before 16 December 2026 and issue the prescribed certificate: ER art. 24.

```oa-check
name: Qatar nonresident consultancy gross fee
inputs:
  gross_fee: 100000
  withholding_rate: 0.05
steps:
  withholding: gross_fee * withholding_rate
  recipient_cash: gross_fee - withholding
expected:
  withholding: 5000
  recipient_cash: 95000
```

### 2. Taxable foreign royalty, exempt foreign PE and credit cap

Assume an ordinary wholly foreign-owned Qatar project earns QAR 1,000,000
foreign royalties with QAR 200,000 directly related allowable costs. The rights
are not connected to a foreign PE; art. 2 Bis/1 includes this income. Separately,
a foreign PE has QAR 300,000 net profit subject to foreign tax, satisfying the
art. 2 Bis/4 exclusion; its own costs are already inside that net figure and
are not deducted from the royalty. No other income, losses or exemptions apply.
The taxpayer has actually paid QAR 100,000 foreign income tax on the royalty,
received a QAR 5,000 refund, and paid QAR 30,000 on the exempt PE profit.

Qatar base is QAR 800,000, pre-credit tax QAR 80,000. Eligible royalty tax is
QAR 95,000; the PE's QAR 30,000 cannot enter the credit. Art. 20 caps the credit
at QAR 80,000, leaving no Qatar tax and QAR 15,000 excess for which no automatic
carryforward/refund is asserted. This illustrates actual eligibility and the
statutory cap without assuming a treaty or an invented allocation ratio.

```oa-check
name: Qatar foreign royalty credit excludes exempt PE tax and applies cap
inputs:
  royalty: 1000000
  royalty_cost: 200000
  foreign_pe_profit: 300000
  foreign_pe_exclusion: 300000
  royalty_tax_paid: 100000
  royalty_tax_refund: 5000
  exempt_pe_tax_paid: 30000
  exempt_pe_tax_ineligible: 30000
  qatar_rate: 0.10
steps:
  taxable_base: royalty - royalty_cost + foreign_pe_profit - foreign_pe_exclusion
  qatar_before_credit: taxable_base * qatar_rate
  eligible_foreign_tax: royalty_tax_paid - royalty_tax_refund + exempt_pe_tax_paid - exempt_pe_tax_ineligible
  credit: min(eligible_foreign_tax, qatar_before_credit)
  qatar_payable: max(0, qatar_before_credit - credit)
  excess_no_automatic_relief: eligible_foreign_tax - credit
expected:
  taxable_base: 800000
  qatar_before_credit: 80000
  eligible_foreign_tax: 95000
  credit: 80000
  qatar_payable: 0
  excess_no_automatic_relief: 15000
```

## Ask the client first

- What are the payer's and recipient's legal identity, tax regime, residence
  and ownership, and is there a Qatar PE or valid GTA/QFC registration?
- What does the contract pay for; where is work performed and used, by whom,
  and how long do Qatar personnel/projects remain?
- What are the payment, entitlement and contract dates, and is the price gross
  or guaranteed net of Qatar tax?
- Which treaty, residence certificate, beneficial-owner evidence and GTA relief
  mechanism support a claim?
- What foreign income, branches, tax paid/refunded and substantive activities
  exist, and what exemption or credit is being claimed?
- Is an activity/branch being sold, closed, merged or moved, and what contracts,
  assets, gains, notices and outstanding returns are involved?

## Sources

| Source | URL | Read on |
|---|---|---|
| GTA President Decision 8/2026, arts. 1–2, approved-payer thresholds and exception | https://www.gta.gov.qa/assets/pdf/Decision%20of%20the%20President%20of%20the%20General%20Tax%20Authority%20No.%20(8)%20of.pdf | 2026-10-24 |
| GTA consolidated ITL 24/2018 incorporating Law 11/2022 and ER 39/2019 incorporating Decision 3/2023, articles cited above | https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%20EN%202024.pdf | 2026-10-24 |
| Current Arabic ITL, including amended art. 24 | https://almeezan.qa/legislations/d444f6ad-68b1-4244-af96-6bf9ee39e065 | 2026-10-24 |
| Current Arabic ER, including WHT art. 21 and treaty mechanisms | https://almeezan.qa/legislations/afee272e-4654-41c7-9e76-2b42f13c9b35 | 2026-10-24 |
| GTA Arabic 2024 compilation, ER art. 37(5), printed p. 36; paragraph omitted from rendered register | https://www.gta.gov.qa/assets/pdf/Income%20Tax%20Law%202024.pdf | 2026-10-24 |
| Cabinet Decision 3/2023, art. 1; replaces ER art. 37(3)–(4) only | https://almeezan.qa/legislations/0291f2d0-b545-48e4-82b5-51480e807884 | 2026-10-24 |
| Law 22/2024, arts. 3 and 5; additional general penalties effective 1 January 2025 | https://almeezan.qa/legislations/3643a42a-bdc0-4546-95d6-975557616a1b | 2026-10-24 |
| Cabinet Decision 4/2026, direct treaty-benefit mechanism | https://almeezan.qa/legislations/f6bfa17b-9d1d-47fc-97b3-873859357599 | 2026-10-24 |
| GTA income, withholding and capital-gains guidance | https://www.gta.gov.qa/en/taxes-info | 2026-10-24 |
| GTA investor guide, tax portal routing and annual-return timing | https://www.gta.gov.qa/en/investors-guide | 2026-10-24 |
| GTA treaty directory | https://www.gta.gov.qa/en/agreements | 2026-10-24 |
| GTA global minimum-tax framework, separate regime | https://www.gta.gov.qa/en/global-minimum | 2026-10-24 |

Not yet confirmed: none within ordinary mainland foreign-income, PE attribution,
actual-disposal/cessation and nonresident-payment scope described here. Treaty
rates, specialist reorganisations, QFC/free-zone regimes and detailed Pillar Two
computations require separate sources and are outside this Guide.

General reference only. A qualified Qatar tax professional must review the
facts, contracts, treaty entitlement, records and operative filings before acting.
This is a source-cited draft, not professional attestation.

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-28. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `qa-cross-border-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/qa-cross-border-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
