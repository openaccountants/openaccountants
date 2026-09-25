---
name: sweden-bookkeeping
description: Use this skill whenever asked about Swedish bookkeeping, chart of accounts, BAS kontoplan, financial statements, or accounting standards in Sweden. Trigger on phrases like "Swedish bookkeeping", "bokföring Sverige", "BAS kontoplan", "kontoplan", "årsredovisning", "K2", "K3", "BFL", "ÅRL", "resultaträkning", "balansräkning", "enskild firma bokföring", "årsbokslut", "Bokföringsnämnden", "BFN", "avskrivning", "förenklat årsbokslut", or any question about recording transactions, financial reporting, or accounting standards for Swedish entities.
version: 1.0
jurisdiction: SE
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden: bookkeeping — 2026 editorial draft

Use for tax year 2026 and the entity’s actual financial year. This method covers who must keep books, recording, vouchers, timing, reconciliation, correction, archiving and an ordinary K1/K2 annual close with its deadlines. It draws on the Book-keeping Act (BFL), the Annual Accounts Act (ÅRL) and BFN guidance.


## Ask the client first

The Book-keeping Act and Annual Accounts Act are the framework for Swedish accounting; BFN issues the guidance that expresses generally accepted accounting principles. [BFN source](https://www.bfn.se/english/regulations/)

### Who must keep books

- A natural person who carries on a business (näringsverksamhet) is book-keeping liable for that business. Renting out a private dwelling property is not business for this rule. [Bokföringslagen 2 kap. 6 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)
- A legal person is book-keeping liable unless the Act makes an exception. Limited companies (AB), trading partnerships (HB) and economic associations are liable even without business activity; an AB becomes liable on the day it is registered with Bolagsverket. [BFN source](https://www.bfn.se/english/regulations/) [BFN, aktiebolag](https://www.bfn.se/redovisningsregler/vad-galler-for/aktiebolag/)
- Non-profit associations (ideella föreningar), registered religious communities and some other associations are liable only if their assets exceed SEK 1.5 million (market value; real property at assessed value), or if they carry on business activity or are the parent of a group. Foundations follow the same SEK 1.5 million asset test, but fundraising foundations, foundations carrying on business, parent foundations and several other listed kinds are always liable. Liability under the asset test ends only when assets have been below the limit at the end of the three latest financial years. A foundation whose assets may be used only for the benefit of specified natural persons is outside the Act entirely. [Bokföringslagen 2 kap. 2–5 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)
- A foreign company doing business in Sweden through a branch, and a person resident abroad doing business in Sweden, are liable for that Swedish business and must keep it in separate books. [Bokföringslagen 2 kap. 7 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)

Use this method for the legal entity’s own Swedish activity. It does not select tax treatment, a BAS account number, VAT result, payroll calculation or specialised accounting policies outside the ordinary K1/K2 branches below. A BAS chart can be a useful internal mapping but is not a statutory substitute for a system that can show the required journal and ledger information.

Before processing entries, record:

- Legal form, registration date, financial year, group/branch facts and whether the entity is book-keeping liable under the tests above.
- The financial year. A natural person, and a trading partnership where a natural person is taxed on all or part of its income, must use the calendar year. Other entities may use a broken twelve-month year. A first year, or a year when the financial year is changed, may be shorter than twelve months or extended to at most eighteen months. Companies in the same group must share one financial year. Skatteverket may allow a natural person or such a partnership a different twelve-month year only for exceptional reasons (synnerliga skäl). Changing the financial year needs Skatteverket's permission, except a change to the calendar year or to a shared group year. [Bokföringslagen 3 kap.](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)
- The required closing output: simplified annual accounts, annual financial statements or annual report (see the closing step); the applicable K framework and any elected policy.
- Bank/cash accounts, sales channels, VAT/PAYE registrations, payment providers, certified cash registers, credit facilities, fixed assets, inventory and every source system that creates accounting information.
- The chosen accounting system, who can post/approve/export, voucher-number series, chart/account mapping, accounting periods, archive location (Sweden or abroad) and access plan.
- Whether the entity's annual net turnover is normally at most SEK 3 million, which opens the payment-based (cash) method and a longer recording deferral. Net turnover excludes VAT. [Bokföringslagen 5 kap. 2 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)

## Build a compliant record for every business event

A business event includes changes to the size or composition of assets caused by economic dealings with outsiders, including payments, receivables, liabilities and owner contributions/withdrawals. An order alone is not a business event. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

For each event, create or retain a voucher that establishes:

| Required record | Control |
| --- | --- |
| When the voucher was compiled and when the event occurred | Keep document and transaction dates separately if they differ. |
| What happened, amount and counterparty | Invoice, receipt, agreement, bank support and explanation must tell a reviewer what was booked. |
| Voucher number or other unique identifier | Link the identifier from source document to journal and ledger. |
| Account coding and accounting period | The continuous record must show registration order, period, voucher identifier, coding and booked amount. |
| VAT/payroll/tax classification evidence where relevant | Retain the tax evidence separately; a ledger account cannot establish tax treatment by itself. |

A document received about the event must itself be used as the voucher, supplemented where needed. [Bokföringslagen 5 kap. 6–7 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/) The BFN guide requires the core voucher information to be durable and not erased or made illegible. If an externally received voucher is incomplete, add missing information without changing the received content; record when, by whom and how it was supplemented. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Record on time and present the complete accounting trail

Maintain both:

* a **registration-order** presentation (journal) that shows when postings were added; and
* a **systematic** presentation (ledger) that groups transactions by their nature and supports a running view of financial position/result and the year-end statements.

For each posting, those presentations must make available registration order, accounting period, voucher identifier, account coding and amount. Separate sales, purchase, payroll, cash and bank systems must feed one systematic accounting record; isolated ledgers are not enough. An event counts as booked only when it can be presented in both orders. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

### Timing decision

1. **Cash receipts and cash payments** (notes, coins, cheques and similar; in some cases paper meal vouchers and gift cards count as cash) must be booked for the registration-order presentation no later than the next working day. The next working day is the first day after the event on which work is performed in the business. If there are more than a few days between the event and that next working day, book by the day after the event. A shop closed on Sunday books Saturday's cash by Monday. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
2. **Other business events** must be booked as soon as the entity has enough information to book them acceptably. Receivables and liabilities may wait until the invoice is issued or received (or commercially should have been); if used, apply this consistently during the year to both issued and received invoices. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
3. **Permitted deferral.** Only if the vouchers are kept in order as they arrive, BFN allows booking later, at the latest: [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
   * any entity: 50 days after the end of the month in which the event occurred;
   * annual net turnover normally at most SEK 3 million: 50 days after the end of the quarter; [BFN guide, point 3.7](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
   * normally at most 50 vouchers covering at most 250 events a year **and** annual net turnover normally at most SEK 1 million: 60 days after the end of the financial year (adjust the voucher and event counts for a year that is not twelve months); [BFN guide, point 3.8](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
   * a sole trader meeting those same voucher, event and SEK 1 million limits, and not carrying out the cross-border EU transactions referred to in 26 kap. 33 a § of the Tax Procedure Act: the date the income-tax return for that year is due, or the later date in a Skatteverket decision granting an extension (anstånd) for that return. [BFN guide, point 3.9](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

   These deferrals do **not** apply to cash for the registration-order presentation, which stays next working day. Two exceptions: cash recorded in a certified cash register may be booked in registration order up to 50 days after month end; and an entity that is book-keeping liable only under Bokföringslagen 2 kap. 2 or 3 § (non-profit associations, registered religious communities, joint-property associations, foundations and similar) whose cash receipts are normally below one price base amount a year may book cash in registration order up to four weeks after the event. For sales from a coin-operated vending machine, cash may be booked in registration order the day after the machine is emptied (or the day after the emptying company reports); machines must be emptied close to year end. Anything later is allowed only for a special obstacle of a temporary nature, such as acute illness, and then only for a day or a few days. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
4. **Payment-based (cash) method.** An entity whose annual net turnover is normally at most SEK 3 million may wait to book business events until payment, but must book all receivables and liabilities still unpaid at the end of the financial year. This is not open to credit institutions, securities companies or insurance companies, or to financial holding companies that must prepare group accounts under those Acts. Vouchers must still be kept in order while waiting, and the month, quarter and year-end deferral windows in step 3 (BFN points 3.6–3.8) run from the payment date; the sole trader's tax-return date is not moved. This does not remove source-document, cash-record or closing obligations. [Bokföringslagen 5 kap. 2 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/) [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
5. Complete each accounting period by reconciling relevant balances and posting corrections found in the reconciliation. Do not silently reopen a completed period.

## The method, step by step

1. **Collect and index source documents.** Download sales invoices, supplier invoices/receipts, bank and card statements, payment-provider reports, cash records, payroll reports, asset documentation, loan notices and VAT/PAYE evidence. Give each voucher a unique identifier.
2. **Validate the voucher.** Confirm counterparty, date, amount, business explanation, currency and whether required VAT/payroll evidence is present. Create an internal voucher for a legitimate event with no external document, such as an owner withdrawal or year-end adjustment; it needs the same statutory facts and evidence trail. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
3. **Post the event within the timing rule above.** Enter debit and credit using the entity’s documented account mapping, period and voucher identifier. Keep principal, interest, VAT, cash movement and owner/equity movements distinguishable where they differ. Do not treat a bank feed’s auto-categorisation as a completed posting without voucher review.
4. **Reconcile.** Match every bank/card/payment-provider movement to a voucher and ledger posting; reconcile cash, accounts receivable, accounts payable, payroll liabilities, VAT/PAYE control balances, loans and intercompany/owner accounts as applicable. Investigate duplicate, missing or unmatched items.
5. **Review completeness.** Compare the journal count to source-document count, review unusual manual journals and zero/negative control-account balances, and preserve the system export and reconciliation evidence.

## Correct, do not erase

Do not delete or make an original booked record illegible. In computerised bookkeeping, correct a booked posting with a separate correction posting. It is a new posting with its own voucher and must make the original and correction traceable. A manual record can only be struck through where it has not affected totals; otherwise use a correction posting. If the earlier period is completed, the correction belongs in the discovery period. If an error is found while reconciling an unfinished period, correct that unfinished period; do not confuse reconciliation performed the following month with a completed-period error. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

When correcting a posting or a voucher, record when the correction was made and by whom. [Bokföringslagen 5 kap. 5 och 9 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/) If a correction changes VAT, PAYE, tax return or filed financial-statement results, follow the separate return/amendment process as well; changing the ledger alone does not amend a filed tax return. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Close the financial year

1. Freeze the operational source list and reconcile bank, cash, receivables, payables, loans, payroll, VAT/PAYE, inventory and fixed-asset records to supporting evidence.
2. Post closing transactions needed to determine the year’s income, expenses and financial position, such as accruals and depreciation, when continuous bookkeeping is closed. The ongoing record is not required to be fully accrued throughout the year, but closing postings must complete the financial-year result. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
3. Select the required closing form by entity type and size: [Bokföringslagen 6 kap. 1–3 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)
   * **Annual report (årsredovisning), always:** AB; economic associations; trading partnerships with one or more legal persons as partners; book-keeping liable foundations (except certain family foundations); credit institutions, securities companies and insurance companies; holders of a gaming licence (except certain small licence holders); and any entity that is a larger company or the parent of a larger group (see the size test below).
   * **Annual financial statements (årsbokslut):** every other entity that does not prepare an annual report, such as a sole trader or a partnership with only natural-person partners. BFN's framework for these is K2/K3 Årsbokslut (BFNAR 2017:3). [BFN, enskilda näringsidkare](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/) [BFN, handelsbolag](https://www.bfn.se/redovisningsregler/vad-galler-for/handelsbolag/)
   * **Simplified annual accounts (förenklat årsbokslut):** allowed by the Act for an entity not required to prepare an annual report whose annual net turnover is normally at most SEK 3 million. BFN's K1 for sole traders applies only to natural persons, not to a natural person who is the parent of a group, and the turnover limit counts all of that person's businesses together. BFN's page for trading partnerships names only årsbokslut (K2/K3) or an annual report, so do not put a partnership on the sole-trader K1. [K1](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf) [BFN, handelsbolag](https://www.bfn.se/redovisningsregler/vad-galler-for/handelsbolag/)
   * A sole trader that is a larger company must prepare an annual report under K3; other sole traders may choose one voluntarily. [BFN, enskilda näringsidkare](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/)
   * A limited company prepares an annual report every financial year. Only eligible smaller companies may choose K2; smaller companies excluded from K2, companies declining K2 and larger companies use K3. [BFN, aktiebolag](https://www.bfn.se/redovisningsregler/vad-galler-for/aktiebolag/)
4. Tie the closing statements back to final journal/ledger balances and reconcile their tax-return inputs separately.

### Closing deadlines

| Output | Deadline |
| --- | --- |
| Annual financial statements or simplified annual accounts | As soon as possible, and no later than six months after the financial year ends (four months for a foundation). [Bokföringslagen 6 kap. 7 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/) |
| AB or economic association: annual report to the auditors | At least six weeks before the annual general meeting that deals with it. Other entities: within four months after year end. [ÅRL 8 kap. 2 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arsredovisningslag-19951554_sfs-1995-1554/) |
| AB or economic association: filing with Bolagsverket | Certified copies of the annual report and audit report must reach Bolagsverket within one month after the meeting adopts the balance sheet and income statement. If they have not arrived within seven months after year end, a late-filing fee is charged: SEK 7,500 for a private AB or an economic association, SEK 15,000 for a public AB. The fee repeats: if the documents still have not arrived within two months after notice of the fee decision, a second fee is charged (SEK 7,500; public AB SEK 15,000), and if they are still missing two months after that notice, a third fee (SEK 15,000; public AB SEK 30,000). The seven months become nine months only if, within the seven months, the company has notified a continued meeting, paid its registration fee and filed the auditor's written confirmation. [ÅRL 8 kap. 3, 5 och 6 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arsredovisningslag-19951554_sfs-1995-1554/) |
| Partnership with a legal-person partner; foundation | Copies to Bolagsverket (a foundation files with its supervisory authority) within six months after year end. A foundation that must file and misses the six months pays a SEK 7,500 late fee, with the same repeat fees (SEK 7,500, then SEK 15,000) if it still does not file. [ÅRL 8 kap. 1, 3, 6 och 6 a §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arsredovisningslag-19951554_sfs-1995-1554/) |
| Other entities preparing an annual report | Keep copies available to anyone from six months after year end; a larger company must file them with Bolagsverket within six months even without a request. [ÅRL 8 kap. 3 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arsredovisningslag-19951554_sfs-1995-1554/) |

The meeting date itself, and the tax-return dates, come from company law and the tax rules, not from this method; confirm them for the entity before relying on a date.

## Archive, access and system controls

Keep accounting information durable, easily accessible, orderly and secure in Sweden up to and including the seventh year after the end of the calendar year in which the financial year ended. Keep the equipment and systems needed to print it out on paper available in Sweden for the whole period. The Sweden rule does not apply to records of a foreign branch with its own administration if the company is book-keeping liable in that other country. [Bokföringslagen 7 kap. 2 och 5 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)

- **Keep what you received in the form you received it.** Paper documents are kept in the condition they had when they arrived or were compiled; electronic documents in the format and with the content they had. [Bokföringslagen 7 kap. 1 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)
- **Scanning and destroying originals (rule in force from 1 July 2024).** Since the amending Act (2024:342) took effect on 1 July 2024, an entity may destroy a paper or electronic document once its accounting information has been transferred to another paper or electronic document, but only if the transfer, given the technical methods, organisational measures and other circumstances, carries no risk that the information is changed or lost. The document transferred to must then be kept for the rest of the retention period. Destroying records early without a transfer needs Skatteverket's permission in the individual case. [Bokföringslagen 7 kap. 6–7 §§ and transitional rules](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/) [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
- **Storing abroad.** Only electronic records may be kept abroad without special permission, and only in another EU country (or a non-EU country with equivalent mutual-assistance instruments) if all three conditions are met: the storage place and every change of it are notified to Skatteverket (Finansinspektionen for supervised firms); Skatteverket or Customs can get immediate electronic access on request; and the information can be printed out on paper in Sweden immediately. Otherwise Skatteverket's permission is needed. Paper records must stay in Sweden, except that a paper voucher may be kept abroad temporarily for special reasons. [Bokföringslagen 7 kap. 3–4 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)

For electronic records, make regular backups suited to the business’s volume and keep a backup separate from the copied records. Maintain an archive plan where needed that says what is stored, where it is stored and how the archive is structured. A cloud provider or accountant may hold data, but the book-keeping entity must retain access during the full archive period, including after a software/provider change; an online bookkeeping service that stores the data abroad is foreign storage and triggers the notification above. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

Maintain system documentation and processing history sufficient for an external reviewer to understand the chart/account mapping, voucher identification, data flows, automated posting rules and how electronic records can be produced. A spreadsheet whose entries can be changed afterwards, such as Excel, is not an acceptable bookkeeping system for a sole trader. [BFN source](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/) [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Choose the ordinary annual-close branch

Use the whole selected framework consistently. This section covers a normal sole trader using K1 and an eligible smaller private limited company using K2. A different legal form, K3 or a regulated financial entity needs its own framework. The linked consolidated K1 and K2 editions contain the current changes; select by the financial year’s start date rather than assuming that the filing year alone selects the rules. [BFN current guide catalogue](https://www.bfn.se/informationsmaterial/vagledningar/)

### K1 sole trader

A sole trader (a natural person, not the parent of a group; an estate carrying on business counts as a natural person) whose net turnover across all of the person's businesses is normally at most SEK 3 million may choose simplified annual accounts. A person with several businesses may use K1 only if it is applied to all of them. Use the K1 balance-sheet and income-statement layout, with its own recognition rules rather than borrowing K2 accrual simplifications. [K1](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)

- Revenue: start with customer payments, add the change in unpaid customer receivables that were invoiced or commercially should have been invoiced, and adjust for opening versus closing customer advances. Exclude VAT from revenue. A customer advance for work/delivery not started is a liability where it exceeds SEK 5,000; test each payment/invoice and clearly separable unstarted part under the K1 rule. An invoice is not automatically earned revenue. [K1, revenue and customer advances](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)
- Costs and liabilities: reconcile payments and unpaid supplier invoices; distinguish expense from inventory, equipment, advances and private withdrawals. Include unpaid trade receivables and liabilities in the close even when current posting uses the payment method. Advances to suppliers of more than SEK 5,000 are shown as other receivables, and accrued interest income or unpaid interest expense for the year is shown only if it totals more than SEK 5,000 (K1 points 6.59, 6.60, 6.73). Use the K1 closing schedule rather than assuming cash payments equal profit. [K1](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)
- Inventory: count goods the business owns and has received, remove sold/dispatched goods, and document quantities and unit costs. The normal latest purchase invoice may support cost where its price is normal; otherwise use FIFO, weighted average or a comparable permitted method. Screen impairment separately. An inventory whose total value is at most half a price base amount need not be shown in the balance sheet and may be expensed (K1 point 6.47). [K1, inventory](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)
- Machinery/equipment: retain the acquisition schedule and group naturally connected purchases. An item with expected economic life at most three years may be expensed immediately. Otherwise apply K1 acquisition/valuation rules: equipment is collectively carried at its tax value, capped as prescribed by opening value plus acquisitions; the depreciation posting bridges the pre-depreciation book amount to that supported tax value. The K1 low-value limit is set as half a price base amount, applied across all of the person's businesses and to grouped purchases, not as a fixed currency figure; obtain the actual tax-value calculation before finalising that schedule. [K1, equipment](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)

### K2 eligibility for a financial year starting after December 2025

First establish that the entity is smaller under the Annual Accounts Act. A larger company is a listed company, or one that meets more than one of these in each of the two latest financial years: more than 50 employees on average, a balance-sheet total of more than SEK 40 million, net turnover of more than SEK 80 million. [ÅRL 1 kap. 3 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arsredovisningslag-19951554_sfs-1995-1554/) [BFN framework selection](https://www.bfn.se/om-bokforingsnamnden/k-projektet/)

K2 excludes public limited companies; parents of larger groups; parents preparing consolidated accounts; individuals/estates; housing associations; businesses with foreign branches during the year; acquisitions of goods/services for share-based consideration; issued convertible or similar compound financial instruments; and crypto holdings during the year other than occasional use/receipt as payment. [K2 scope](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)

It also excludes material deferred-tax-liability cases and buildings generating at least 75% of turnover, subject to the specific small-entity and temporary-condition exceptions. Assess these additional exclusions using the latest financial year for which a completed annual report exists. The small-entity exception applies where no more than one of these is exceeded in each of the two preceding years: employees 3, balance sheet SEK 1.5 million, net turnover SEK 3 million. The other exception requires K2 in the preceding year and conditions not normally falling within those additional exclusions. These exceptions do not override the preceding exclusion list. Document the screen and source financial statements. [K2 scope](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)

A new business starting after June 2025 with an extended first financial year ending December 2026 or later also uses the new edition. A business failing the screen uses the appropriate K3 route; do not apply the following K2 policies to it. [BFN edition dates](https://www.bfn.se/informationsmaterial/vagledningar/)

### Ordinary K2 recognition and close

- Goods revenue: recognise when material risks/rewards have passed, the amount is reliably measurable and economic benefits are probable; determine transfer using the delivery arrangement. Separate customer advances from earned revenue. Time-and-material services earn revenue as work/materials are performed/delivered at agreed prices; record earned unbilled revenue at close. Fixed-price contracts require the framework’s consistent main/alternative contract method and loss review. [K2 revenue](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)
- Expenses and accruals: assign income/cost to the financial year it concerns. Record unpaid earned costs as accrued liabilities and future-period payments as prepaid assets. For financial years starting after 31 December 2025 (BFNAR 2025:2), K2 lets a company skip accruing income and expenses that are each below SEK 7,000, and lets it take a received or paid advance for goods or services below SEK 7,000 straight to income or expense. Test each item on its own; do not split or net items to get under the limit. For an earlier financial year, use the limit in the K2 edition that applied to that year. [K2 points 2.4 and 2.4A](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)
- Equipment: capitalise qualifying acquisition cost, record the asset’s in-use date and useful-life evidence, and depreciate systematically from the year it enters use. Connected parts form one depreciation unit. An item may be expensed if its acquisition cost is below half a price base amount (plus any input VAT the company cannot deduct), judging naturally connected items, or purchases forming part of a larger investment, on their combined cost; or if its expected economic life is at most three years. For a financial year that uses the 2026 price base amount of SEK 59,200, half is SEK 29,600; for a year that straddles two calendar years, confirm which year's amount applies. K2 permits a five-year useful-life simplification for machinery/equipment; select/document it or support the actual useful life. Straight-line is a common choice. Keep book depreciation separate from the tax depreciation/untaxed-reserve calculation. [K2 points 10.5, 10.6 and 10.27](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) [Skatteverket price base amount 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html)
- Inventory: perform count and ownership cut-off, establish acquisition cost and compare with net realisable value under the applicable individual-item/grouping rules. Record a supported write-down rather than assume all stock sells at cost. Reconcile opening stock, purchases, cost consumed and closing stock to the ledger. [K2 inventory](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)
- Statements: prepare the K2 management report, income statement, balance sheet and notes, using its layouts and required comparisons. Map net turnover, operating costs, depreciation, financial items, appropriations and tax to the income statement; reconcile assets, equity, untaxed reserves, provisions and liabilities to balance-sheet schedules. Carry current profit into equity once; verify total assets equal equity plus untaxed reserves/provisions/liabilities. The ledger is not itself the completed annual report. [K2 annual-report form and layouts](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)

## Worked debit/credit close

The following are hypothetical SEK amounts with no VAT unless explicitly stated; VAT status/amounts are assumed already resolved by the separate VAT method. Account names are illustrative classifications, not prescribed BAS codes. [BFN bookkeeping](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

| Case | Journal and control |
| --- | --- |
| Invoice and payment | Supported K2 operating-service invoice SEK 12,000 for this year: debit service expense 12,000; credit supplier payable 12,000. On payment debit supplier payable 12,000; credit bank 12,000. Expense is booked once and payable clears. [K2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| Wrong expense coding | The same invoice was wrongly debited to travel. Separate correction: debit service expense 12,000; credit travel expense 12,000; link original and correction vouchers. Bank/payable do not change. Use the completed/unfinished-period rule above. [BFN corrections](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf) |
| Unpaid K2 cost | December services received SEK 12,000; invoice arrives January. At close debit service expense 12,000; credit accrued liability 12,000. When invoice is recorded, debit that accrual and credit payable; resolve any estimate difference without duplicating the expense. The item is not below the K2 accrual limit, so it must be accrued. [K2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K2 prepaid service | Pay SEK 24,000 for an even service covering December and January; initially debit prepayment 24,000/credit bank 24,000. At December close debit expense 12,000/credit prepayment 12,000, leaving asset 12,000 for January. [K2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K2 equipment | Eligible equipment costs SEK 100,000, above the half-price-base-amount limit, enters use at start of a normal full financial year, supported straight-line useful life five years and no residual value. Debit equipment 100,000/credit bank 100,000. Annual debit depreciation 20,000/credit accumulated depreciation 20,000; carrying amount 80,000. Assumptions are illustrative, not a mandatory life or tax method. [K2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K1 unpaid sale | Customer paid 100,000 during year; closing unpaid earned invoice 20,000; no opening receivable or advances. Revenue 120,000. Add year-end debit receivable 20,000/credit revenue 20,000; subsequent payment debits bank and clears receivable, not new revenue. [K1](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf) |
| Archive expiry | A financial year ends in June 2026. Retain its accounting information through December 2033: count seven calendar years after the calendar year in which it ended. An agreement spanning later financial years can have a later expiry. [BFN archive](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf) |

## Deliverables and closing decisions

Produce a journal, ledger, trial balance, supporting-voucher index, balance reconciliations, open-item list, corrections log and a closing checklist identifying the selected framework, the closing deadline and the still-needed accounting policies. Map ledger balances to the applicable framework’s income-statement and balance-sheet headings; check that each closing figure reconciles to the ledger and its supporting schedule. Use the entity’s approved chart of accounts; no account number establishes VAT liability, deductibility or revenue recognition by itself.

For revenue, obtain the contract, delivery/performance evidence, invoice and any deferred-income schedule. For inventory, obtain count, ownership and cost/valuation evidence. For fixed assets, obtain acquisition documents, commissioning date, useful-life assessment, chosen depreciation policy and disposal records. For tax, payroll and VAT controls, use the separately supported computation and reconcile its liability to postings/payments. When those inputs or a framework decision are missing, mark the relevant closing entry unresolved. Do not fill the gap with an old generic capitalization threshold, tax rate or merchant classification.

These working-paper controls operationalize the requirement to record closing entries establishing the period’s income, expenses and financial position. [BFN bookkeeping guide](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Worked checks

## Case 1 — ordinary supplier invoice and bank payment

**Facts:** A limited company receives a supplier invoice for a business purchase and pays it by bank transfer. The VAT treatment is already separately established.

**Method:** Retain the invoice as voucher, assign voucher identifier, record the liability/event within the timing rule with documented account coding and period, then post/reconcile the bank payment to the same supplier liability and support. The journal and ledger must expose the voucher identifier, period, coding and amount. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 2 — cash sale timing boundary

**Facts:** A shop takes cash on Saturday and is closed Sunday; the next day work is performed is Monday. It does not record the sales in a certified cash register.

**Method:** Record the cash receipt in registration order no later than Monday. Preserve the cash-report/voucher trail and reconcile the cash balance. The 50-day deferral does not help here: for cash it covers only the systematic (ledger) presentation, or the registration-order presentation only when the takings are recorded in a certified cash register. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 3 — small-business payment method and year end

**Facts:** A sole trader's annual net turnover is normally at most SEK 3 million, the business is not a financial company, and it has an unpaid customer invoice at year end. [Bokföringslagen 5 kap. 2 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)

**Method:** The business may defer ordinary event recording until payment, but must include all unpaid receivables and liabilities at year end before closing. Keep the invoice and other vouchers in order throughout; this is not permission to omit bookkeeping. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 4 — discovered coding error in computerised records

**Facts:** A March posting was coded to the wrong expense category and discovered in April after March was reconciled.

**Method:** Do not overwrite/delete it. Post a separate correction in April with its own voucher and clear link to the original, keeping both records readable, and record when and by whom it was made. Assess VAT/PAYE/return amendment separately if the error affected a filed result. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 5 — framework route

**Facts:** A sole trader's turnover is normally at most SEK 3 million and the owner chooses a simplified annual close. A second client is a trading partnership owned by two individuals with the same turnover. [BFN, enskilda näringsidkare](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/)

**Method:** Confirm K1 eligibility for the sole trader (a natural person, not a group parent, turnover counted across all businesses) and prepare simplified annual accounts under K1. The partnership prepares annual financial statements under K2/K3 Årsbokslut, not the sole-trader K1. A limited company prepares an annual report and selects K2 only if currently eligible, otherwise K3. [BFN, enskilda näringsidkare](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/) [BFN, handelsbolag](https://www.bfn.se/redovisningsregler/vad-galler-for/handelsbolag/) [BFN, aktiebolag](https://www.bfn.se/redovisningsregler/vad-galler-for/aktiebolag/)

## Case 6 — how late may a supplier invoice be booked

**Facts:** Company A has annual net turnover of about SEK 10 million; Company B's turnover is normally at most SEK 3 million. Each receives a supplier invoice on 12 February 2026 and keeps it filed in order. Neither is a cash transaction. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

**Method:** Company A may book it no later than 50 days after the end of February: 19 April 2026. Company B may use the quarterly rule: 50 days after the end of March, which is 20 May 2026. If either paid in cash from the till, that payment would still be booked in registration order by the next working day. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 7 — annual report filing deadline for a private AB

**Facts:** A private AB's financial year ends 31 December 2026. Its meeting adopts the accounts on 15 May 2027.

**Method:** Certified copies must reach Bolagsverket within one month after adoption, by 15 June 2027. If they have not arrived by 31 July 2027 (seven months after year end), the company pays a SEK 7,500 late-filing fee. If it still does not file, further fees follow: SEK 7,500 two months after notice of that decision, then SEK 15,000 two months after the next notice. [ÅRL 8 kap. 3, 6 och 6 a §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arsredovisningslag-19951554_sfs-1995-1554/)

## Case 8 — scanning paper receipts

**Facts:** In 2026 a company scans its paper supplier receipts into its accounting system and wants to shred the paper.

**Method:** Since 1 July 2024 it may destroy the paper once the scan is a transfer that carries no risk of the information being changed or lost (legible, complete, controlled routine), and it must keep the scanned documents for the rest of the retention period. If the scans are stored with a service in another EU country, notify Skatteverket of the storage place and keep immediate electronic access and printout in Sweden. [Bokföringslagen 7 kap. 3 a och 6 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)

## When to refuse or refer

- Missing legal-entity identity, financial year, source vouchers, access to original records or a reliable ledger: list missing evidence and do not present a complete close.
- Unclear book-keeping liability for a non-profit association or foundation (asset value near SEK 1.5 million, or possible business activity): obtain the asset valuation and activity facts first. [Bokföringslagen 2 kap. 2–3 §§](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/bokforingslag-19991078_sfs-1999-1078/)
- Unselected framework or uncertain K2 eligibility: obtain the entity-specific BFN route before applying recognition or measurement.
- Specialised transactions outside the ordinary branches above, including complex revenue contracts, foreign currency, consolidation, audit, insolvency or filing questions: obtain the specific authoritative policy before posting the close.
- A software migration, scanning routine or foreign archive that cannot preserve readable access and a complete audit trail: resolve the archive conditions before retiring the old system or destroying originals.
- Booking later than the deferral windows allow: record the backlog now and note the breach; only a temporary special obstacle justifies a short further delay.
- Missing VAT, payroll or income-tax analysis: keep the accounting working paper separate from the return decision; a ledger correction alone does not amend a filed return.

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
