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

Use for tax year 2026 and the entity’s actual financial year. This method covers recording, vouchers, reconciliation, correction, archiving and an ordinary K1/K2 annual close. Official BFN sources were retrieved for this update.


## Ask the client first

The Book-keeping Act and Annual Accounts Act are the framework for Swedish accounting; BFN issues the guidance that expresses generally accepted accounting principles. All business activity must maintain accounting records, and limited companies, partnerships and co-operatives are generally book-keeping entities even without business activity. [BFN source](https://www.bfn.se/english/regulations/)

Use this method for the legal entity’s own Swedish activity. It does not select tax treatment, a BAS account number, VAT result, payroll calculation or specialised accounting policies outside the ordinary K1/K2 branches below. A BAS chart can be a useful internal mapping but is not a statutory substitute for a system that can show the required journal and ledger information.

Before processing entries, record:

- Legal form, registration date, financial year, group/branch facts and whether the entity is a book-keeping entity.
- The required closing output: simplified annual accounts, annual financial statements or annual report; the applicable K framework and any elected policy.
- Bank/cash accounts, sales channels, VAT/PAYE registrations, payment providers, credit facilities, fixed assets, inventory and every source system that creates accounting information.
- The chosen accounting system, who can post/approve/export, voucher-number series, chart/account mapping, accounting periods, backup/location and access plan.
- Whether the entity normally has annual net turnover of no more than SEK 3 million and qualifies to defer recording until payment. Do not use this simplification until the statutory conditions and year-end conversion are met. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## 2. Build a compliant record for every business event

A business event includes changes to the size or composition of assets caused by economic dealings with outsiders, including payments, receivables, liabilities and owner contributions/withdrawals. An order alone is not necessarily a business event. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

For each event, create or retain a voucher that establishes:

| Required record | Control |
| --- | --- |
| When the voucher was compiled and when the event occurred | Keep document and transaction dates separately if they differ. |
| What happened, amount and counterparty | Invoice, receipt, agreement, bank support and explanation must tell a reviewer what was booked. |
| Voucher number or other unique identifier | Link the identifier from source document to journal and ledger. |
| Account coding and accounting period | The continuous record must show registration order, period, voucher identifier, coding and booked amount. |
| VAT/payroll/tax classification evidence where relevant | Retain the tax evidence separately; a ledger account cannot establish tax treatment by itself. |

The BFN guide requires the core voucher information to be durable and not erased or made illegible. If an externally received voucher is incomplete, add missing information without changing the received content; record when, by whom and how it was supplemented. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## 3. Record on time and present the complete accounting trail

Maintain both:

* a **registration-order** presentation (journal) that shows when postings were added; and
* a **systematic** presentation (ledger) that groups transactions by their nature and supports a running view of financial position/result and the year-end statements.

For each posting, those presentations must make available registration order, accounting period, voucher identifier, account coding and amount. Separate sales, purchase, payroll, cash and bank systems must feed one systematic accounting record; isolated ledgers are not enough. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

### Timing decision

1. Record cash receipts and cash payments no later than the next working day. The next working day means the next day work is performed; where that delay would exceed a few days, record by the day after the event. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
2. Record other business events as soon as possible.
3. An ordinary non-financial business normally having annual net turnover of **SEK 3 million or less** may defer recording business events until payment, but must record all unpaid receivables and liabilities at financial year-end. This does not remove source-document, cash-record or closing obligations. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
4. Complete each accounting period by reconciling relevant balances and posting corrections found in the reconciliation. Do not silently reopen a completed period.

## The method, step by step

1. **Collect and index source documents.** Download sales invoices, supplier invoices/receipts, bank and card statements, payment-provider reports, cash records, payroll reports, asset documentation, loan notices and VAT/PAYE evidence. Give each voucher a unique identifier.
2. **Validate the voucher.** Confirm counterparty, date, amount, business explanation, currency and whether required VAT/payroll evidence is present. Create an internal voucher for a legitimate event with no external document, such as an owner withdrawal or year-end adjustment; it needs the same statutory facts and evidence trail. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
3. **Post the event.** Enter debit and credit using the entity’s documented account mapping, period and voucher identifier. Keep principal, interest, VAT, cash movement and owner/equity movements distinguishable where they differ. Do not treat a bank feed’s auto-categorisation as a completed posting without voucher review.
4. **Reconcile.** Match every bank/card/payment-provider movement to a voucher and ledger posting; reconcile cash, accounts receivable, accounts payable, payroll liabilities, VAT/PAYE control balances, loans and intercompany/owner accounts as applicable. Investigate duplicate, missing or unmatched items.
5. **Review completeness.** Compare the journal count to source-document count, review unusual manual journals and zero/negative control-account balances, and preserve the system export and reconciliation evidence.

## 5. Correct, do not erase

Do not delete or make an original booked record illegible. In computerised bookkeeping, correct a booked posting with a separate correction posting. It is a new posting with its own voucher and must make the original and correction traceable. A manual record can only be struck through where it has not affected totals; otherwise use a correction posting. If the earlier period is completed, the correction belongs in the discovery period. If an error is found while reconciling an unfinished period, correct that unfinished period; do not confuse reconciliation performed the following month with a completed-period error. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

When correcting a voucher, preserve the original information and record when and by whom the correction was made. If a correction changes VAT, PAYE, tax return or filed financial-statement results, follow the separate return/amendment process as well; changing the ledger alone does not amend a filed tax return. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## 6. Close the financial year

1. Freeze the operational source list and reconcile bank, cash, receivables, payables, loans, payroll, VAT/PAYE, inventory and fixed-asset records to supporting evidence.
2. Post closing transactions needed to determine the year’s income, expenses and financial position, such as accruals and depreciation, by the time continuous bookkeeping is closed. The ongoing record is not required to be fully accrued throughout the year, but closing postings must complete the financial-year result. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)
3. Select the required closing form based on entity and size:
   * a sole trader normally at or below SEK 3 million turnover may use K1 simplified annual accounts; [BFN threshold](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/)
   * a sole trader outside/declining that route prepares annual financial statements under the BFN annual-accounts framework, with specified K2/K3 possibilities;
   * a sole trader that is a larger entity must prepare an annual report under K3;
   * a limited company prepares an annual report every financial year. Only eligible smaller limited companies may choose K2; smaller entities excluded from K2, entities declining K2 and larger entities use K3. Check the current framework eligibility before selecting policies. [BFN source](https://www.bfn.se/redovisningsregler/vad-galler-for/aktiebolag/) [BFN source](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/)
4. Tie the closing statements back to final journal/ledger balances and reconcile their tax-return inputs separately. A published/filing deadline is entity- and filing-specific; obtain it from the relevant authority notice rather than using an old generic deadline.

## 7. Archive, access and system controls

Keep accounting information orderly, secure, accessible and in Sweden through the end of the seventh year after the calendar year in which the financial year ended, subject to the statutory conditions for permitted foreign electronic storage. Keep the systems/equipment needed to present the information available. [BFN source](https://www.bfn.se/redovisningsregler/vad-galler-for/aktiebolag/) [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

For electronic records, make regular backups suited to the business’s volume and keep a backup separate from the copied records. Maintain an archive plan where needed that says what is stored, where it is stored and how the archive is structured. A cloud provider or accountant may hold data, but the book-keeping entity must retain access during the full archive period, including after a software/provider change. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

Maintain system documentation and processing history sufficient for an external reviewer to understand the chart/account mapping, voucher identification, data flows, automated posting rules and how electronic records can be produced. A spreadsheet whose entries can be changed afterwards, such as Excel, is not an acceptable bookkeeping system for a sole trader. [BFN source](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/) [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Choose the ordinary annual-close branch

Use the whole selected framework consistently. This section covers a normal sole trader using K1 and an eligible smaller private limited company using K2. A different legal form, K3 or a regulated financial entity needs its own framework. The linked consolidated K1 and K2 editions contain the current changes; select by the financial year’s start date rather than assuming that the filing year alone selects the rules. [BFN current guide catalogue](https://www.bfn.se/informationsmaterial/vagledningar/)

### K1 sole trader

A sole trader with normal net turnover no more than SEK 3 million may choose simplified annual accounts. Use the K1 balance-sheet and income-statement layout, with its own recognition rules rather than borrowing K2 accrual simplifications. [K1](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)

- Revenue: start with customer payments, add the change in unpaid customer receivables that were invoiced or commercially should have been invoiced, and adjust for opening versus closing customer advances. Exclude VAT from revenue. A customer advance for work/delivery not started is a liability where it exceeds SEK 5,000; test each payment/invoice and clearly separable unstarted part under the K1 rule. An invoice is not automatically earned revenue. [K1, revenue and customer advances](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)
- Costs and liabilities: reconcile payments and unpaid supplier invoices; distinguish expense from inventory, equipment, advances and private withdrawals. Include unpaid trade receivables and liabilities in the close even when current posting uses the payment method. Use the K1 closing schedule rather than assuming cash payments equal profit. [K1](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)
- Inventory: count goods the business owns and has received, remove sold/dispatched goods, and document quantities and unit costs. The normal latest purchase invoice may support cost where its price is normal; otherwise use FIFO, weighted average or a comparable permitted method. Screen impairment and the K1 low-total-inventory simplification separately. [K1, inventory](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)
- Machinery/equipment: retain the acquisition schedule and group naturally connected purchases. An item with expected economic life at most three years may be expensed immediately. Otherwise apply K1 acquisition/valuation rules: equipment is collectively carried at its tax value, capped as prescribed by opening value plus acquisitions; the depreciation posting bridges the pre-depreciation book amount to that supported tax value. Do not invent a fixed currency low-value limit: the rule depends on the applicable price-base amount and grouping. Obtain the actual tax-value calculation before finalising that schedule. [K1, equipment](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf)

### K2 eligibility for a financial year starting after December 2025

First establish that the entity is smaller under the Annual Accounts Act. A larger entity exceeds more than one of: average employees 50, balance sheet SEK 40 million, net turnover SEK 80 million, with the relevant criterion exceeded in each of the two preceding years. Listed entities are also larger. [BFN framework selection](https://www.bfn.se/om-bokforingsnamnden/k-projektet/)

K2 excludes public limited companies; parents of larger groups; parents preparing consolidated accounts; individuals/estates; housing associations; businesses with foreign branches during the year; acquisitions of goods/services for share-based consideration; issued convertible or similar compound financial instruments; and crypto holdings during the year other than occasional use/receipt as payment. [K2 scope](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)

It also excludes material deferred-tax-liability cases and buildings generating at least 75% of turnover, subject to the specific small-entity and temporary-condition exceptions. Assess these additional exclusions using the latest financial year for which a completed annual report exists. The small-entity exception applies where no more than one of these is exceeded in each of the two preceding years: employees 3, balance sheet SEK 1.5 million, net turnover SEK 3 million. The other exception requires K2 in the preceding year and conditions not normally falling within those additional exclusions. These exceptions do not override the preceding exclusion list. Document the screen and source financial statements. [K2 scope](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)

A new business starting after June 2025 with an extended first financial year ending December 2026 or later also uses the new edition. A business failing the screen uses the appropriate K3 route; do not apply the following K2 policies to it. [BFN edition dates](https://www.bfn.se/informationsmaterial/vagledningar/)

### Ordinary K2 recognition and close

- Goods revenue: recognise when material risks/rewards have passed, the amount is reliably measurable and economic benefits are probable; determine transfer using the delivery arrangement. Separate customer advances from earned revenue. Time-and-material services earn revenue as work/materials are performed/delivered at agreed prices; record earned unbilled revenue at close. Fixed-price contracts require the framework’s consistent main/alternative contract method and loss review. [K2 revenue](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)
- Expenses and accruals: assign income/cost to the financial year it concerns. Record unpaid earned costs as accrued liabilities and future-period payments as prepaid assets. K2 permits specified small-item simplifications; using full accrual for these ordinary cases avoids relying on an untested threshold. Do not net unrelated items merely to fall below a simplification limit. [K2 basic principles and operating expenses](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)
- Equipment: capitalise qualifying acquisition cost, record the asset’s in-use date and useful-life evidence, and depreciate systematically from the year it enters use. Connected parts form one depreciation unit. K2 permits a five-year useful-life simplification for machinery/equipment; select/document it or support the actual useful life. Straight-line is a common choice, not the only permissible K2 method. Keep book depreciation separate from the tax depreciation/untaxed-reserve calculation. [K2 equipment](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)
- Inventory: perform count and ownership cut-off, establish acquisition cost and compare with net realisable value under the applicable individual-item/grouping rules. Record a supported write-down rather than assume all stock sells at cost. Reconcile opening stock, purchases, cost consumed and closing stock to the ledger. [K2 inventory](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)
- Statements: prepare the K2 management report, income statement, balance sheet and notes, using its layouts and required comparisons. Map net turnover, operating costs, depreciation, financial items, appropriations and tax to the income statement; reconcile assets, equity, untaxed reserves, provisions and liabilities to balance-sheet schedules. Carry current profit into equity once; verify total assets equal equity plus untaxed reserves/provisions/liabilities. The ledger is not itself the completed annual report. [K2 annual-report form and layouts](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)

## Worked debit/credit close

The following are hypothetical SEK amounts with no VAT unless explicitly stated; VAT status/amounts are assumed already resolved by the separate VAT method. Account names are illustrative classifications, not prescribed BAS codes. [BFN bookkeeping](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

| Case | Journal and control |
| --- | --- |
| Invoice and payment | Supported K2 operating-service invoice SEK 12,000 for this year: debit service expense 12,000; credit supplier payable 12,000. On payment debit supplier payable 12,000; credit bank 12,000. Expense is booked once and payable clears. [K2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| Wrong expense coding | The same invoice was wrongly debited to travel. Separate correction: debit service expense 12,000; credit travel expense 12,000; link original and correction vouchers. Bank/payable do not change. Use the completed/unfinished-period rule above. [BFN corrections](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf) |
| Unpaid K2 cost | December services received SEK 12,000; invoice arrives January. At close debit service expense 12,000; credit accrued liability 12,000. When invoice is recorded, debit that accrual and credit payable; resolve any estimate difference without duplicating the expense. [K2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K2 prepaid service | Pay SEK 24,000 for an even service covering December and January; initially debit prepayment 24,000/credit bank 24,000. At December close debit expense 12,000/credit prepayment 12,000, leaving asset 12,000 for January. [K2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K2 equipment | Eligible equipment costs SEK 100,000, enters use at start of a normal full financial year, supported straight-line useful life five years and no residual value. Debit equipment 100,000/credit bank 100,000. Annual debit depreciation 20,000/credit accumulated depreciation 20,000; carrying amount 80,000. Assumptions are illustrative, not a mandatory life or tax method. [K2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K1 unpaid sale | Customer paid 100,000 during year; closing unpaid earned invoice 20,000; no opening receivable or advances. Revenue 120,000. Add year-end debit receivable 20,000/credit revenue 20,000; subsequent payment debits bank and clears receivable, not new revenue. [K1](https://www.bfn.se/wp-content/uploads/vl06-1-k1enskilda-kons2025.pdf) |
| Archive expiry | A financial year ends in June 2026. Retain its accounting information through December 2033: count seven calendar years after the calendar year in which it ended. An agreement spanning later financial years can have a later expiry. [BFN archive](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf) |

## Deliverables and closing decisions

Produce a journal, ledger, trial balance, supporting-voucher index, balance reconciliations, open-item list, corrections log and a closing checklist identifying the selected framework and the still-needed accounting policies. Map ledger balances to the applicable framework’s income-statement and balance-sheet headings; check that each closing figure reconciles to the ledger and its supporting schedule. Use the entity’s approved chart of accounts; no account number establishes VAT liability, deductibility or revenue recognition by itself.

For revenue, obtain the contract, delivery/performance evidence, invoice and any deferred-income schedule. For inventory, obtain count, ownership and cost/valuation evidence. For fixed assets, obtain acquisition documents, commissioning date, useful-life assessment, chosen depreciation policy and disposal records. For tax, payroll and VAT controls, use the separately supported computation and reconcile its liability to postings/payments. When those inputs or a framework decision are missing, mark the relevant closing entry unresolved. Do not fill the gap with an old generic capitalization threshold, tax rate or merchant classification.

These working-paper controls operationalize the requirement to record closing entries establishing the period’s income, expenses and financial position. [BFN bookkeeping guide](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Worked checks

## Case 1 — ordinary supplier invoice and bank payment

**Facts:** A limited company receives a supplier invoice for a business purchase and pays it by bank transfer. The VAT treatment is already separately established.

**Method:** Retain the invoice as voucher, assign voucher identifier, record the liability/event as soon as possible with documented account coding and period, then post/reconcile the bank payment to the same supplier liability and support. The journal and ledger must expose the voucher identifier, period, coding and amount. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 2 — cash sale timing boundary

**Facts:** A shop takes cash on Saturday and is closed Sunday; the next day work is performed is Monday.

**Method:** Record the cash receipt no later than Monday. Preserve the cash-report/voucher trail and reconcile the cash balance. A cash movement cannot wait for the ordinary supplier-invoice workflow. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 3 — small-business payment deferral and year end

**Facts:** A sole trader normally has annual net turnover below SEK 3 million, meets the conditions for payment-based deferral, and has an unpaid customer invoice at year end. [BFN threshold](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/)

**Method:** The business may defer ordinary event recording until payment, but must include all unpaid receivables and liabilities at year end before closing. Preserve invoice/voucher information throughout; this is not permission to omit bookkeeping. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 4 — discovered coding error in computerised records

**Facts:** A March posting was coded to the wrong expense category and discovered in April after March was reconciled.

**Method:** Do not overwrite/delete it. Post a separate correction in April with its own voucher and clear link to the original, keeping both records readable. Assess VAT/PAYE/return amendment separately if the error affected a filed result. [BFN source](https://www.bfn.se/wp-content/uploads/vl13-2-bokforing.pdf)

## Case 5 — framework route

**Facts:** A sole trader normally has turnover below SEK 3 million and chooses a simplified annual close. [BFN threshold](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/)

**Method:** Confirm K1 eligibility and prepare simplified annual accounts under the K1 framework. A sole trader not using that route follows the annual-financial-statement/annual-report route applicable to its circumstances; a limited company prepares an annual report and selects K2 only if currently eligible, otherwise K3. [BFN source](https://www.bfn.se/redovisningsregler/vad-galler-for/aktiebolag/) [BFN source](https://www.bfn.se/redovisningsregler/vad-galler-for/enskilda-naringsidkare/)

## When to refuse or refer

- Missing legal-entity identity, financial year, source vouchers, access to original records or a reliable ledger: list missing evidence and do not present a complete close.
- Unselected framework or uncertain K2 eligibility: obtain the entity-specific BFN route before applying recognition or measurement.
- Specialised transactions outside the ordinary branches above, including complex revenue contracts, foreign currency, consolidation, audit, insolvency or filing questions: obtain the specific authoritative policy before posting the close.
- A software migration or foreign archive that cannot preserve readable access and a complete audit trail: resolve the archive conditions before retiring the old system.
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
