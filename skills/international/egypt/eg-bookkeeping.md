---
name: eg-bookkeeping
description: Use this skill whenever asked about Egyptian record-keeping, bookkeeping, or the mandatory ETA digital systems for self-employed people, sole proprietors (منشأة فردية), and professionals (أصحاب المهن الحرة). Trigger on phrases like "Egypt e-invoicing", "الفاتورة الإلكترونية", "ETA e-receipt", "الإيصال الإلكتروني", "bookkeeping Egypt", "records sole proprietor Egypt", "EGS item coding", "digital signature ETA", "what books must I keep in Egypt", or any request to set up, review, or explain the books and records an Egyptian self-employed taxpayer must keep. ALWAYS read this skill before touching any Egyptian record-keeping or e-invoicing/e-receipt work.
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt record-keeping, e-invoices and e-receipts for the self-employed (2026)

This covers tax year 2026 and the law as it stands on 25 September 2026. It explains the books, records and mandatory digital systems that an Egyptian self-employed person, sole proprietor (منشأة فردية) or professional (صاحب مهنة حرة) must keep. The anchor is the Egyptian Tax Authority (ETA, مصلحة الضرائب المصرية) at eta.gov.eg, and the laws it publishes there:

- the Unified Tax Procedures Law No. 206 of 2020 (قانون الإجراءات الضريبية الموحد), as amended in 2025 and 2026;
- the Income Tax Law No. 91 of 2005;
- the VAT Law No. 67 of 2016;
- Law No. 6 of 2025, the simplified regime for businesses with annual turnover up to twenty million pounds.

Two changes matter most for 2026:

1. From 29 July 2026, every taxpayer in a commercial, industrial, craft or professional activity must keep regular books ([Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf)). Taxpayers in the Law 6 regime are the exception.
2. The Law 6 simplified regime has applied since 1 March 2025 ([Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf)).

Reply to the user in their own language (English or Arabic).

## Scope and who this is for

- Individuals running a trade, craft or business alone (sole proprietors), and professionals (doctors, lawyers, engineers, consultants, freelance developers) who must decide what books to keep and which ETA system to issue documents through.
- Small businesses deciding whether to request the Law 6 of 2025 simplified regime, and what records it still requires.
- Out of scope: companies and partnerships (except where noted), banks, regulated sectors, the detailed VAT and income tax computation, payroll tax, withholding tax, customs, and cross-border questions. See "When to refuse or refer".

## Ask the client first

- What activity do you carry on (trade, industry, craft or profession), and do you hold a tax card and, if you are registered, a VAT registration?
- Do you sell to businesses or government (B2B/B2G), to final consumers (B2C), or both?
- Have you received an ETA decision requiring you to join the e-invoice system or the e-receipt system? The ETA inquiry pages show whether you are named in a mandatory-registration decision: [e-invoice inquiry](https://www.eta.gov.eg/ar/einvoice-inquiry) and [e-receipt inquiry](https://www.eta.gov.eg/ar/ereceipt-inquiry).
- What was your annual turnover in the last final assessment or last return? Have you asked to be taxed under Law No. 6 of 2025, and on what date?
- If you are a consultant, does 90% or more of your turnover come from one or two clients?
- How many invoices do you issue a month, and do you use accounting software (ERP) or none?
- Do you hold a digital signature certificate, and are your goods and services coded (GS1 or EGS)?
- Are you operating on a temporary tax card while completing set-up and licensing?
- Is any year under examination, in dispute, or subject to an ETA notice?

## The method, step by step

1. **Decide which record-keeping regime applies.** The default is regular books. Law No. 150 of 2026 replaced the first paragraph of Article 38 of the Unified Tax Procedures Law. Every taxpayer carrying on a commercial, industrial, craft or professional activity must now keep the regular accounting records and books required by the Commercial Law No. 17 of 1999, manually or electronically ([Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf)). The law applies from the day after its publication on 28 July 2026. The exception is a business taxed under Law No. 6 of 2025, which is exempt from the Unified Tax Procedures Law books. It must keep the simplified records set by Minister of Finance decision instead ([Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Article 13).
2. **Decide which ETA document system applies.** A sale to a business or government body needs an e-invoice (الفاتورة الإلكترونية), whatever its value. A sale to a final consumer needs an e-receipt (الإيصال الإلكتروني) ([ETA e-receipt FAQ](https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf)). A business serving both needs both. The same registered accounting system may issue both.
3. **Confirm the taxpayer's phase.** Joining is set by ETA decisions issued in phases. Check the named lists on the [e-invoice inquiry](https://www.eta.gov.eg/ar/einvoice-inquiry) and [e-receipt inquiry](https://www.eta.gov.eg/ar/ereceipt-inquiry) pages. If the taxpayer is not named, joining voluntarily is possible. Do not tell anyone they are exempt.
4. **Set up the digital identity.** Register on the system. Obtain a digital signature or seal for e-invoices, code every item, and choose the portal or an ERP integration (details below).
5. **Keep the books** (regular or simplified), and tie every sale and purchase to an ETA document and to the bank.
6. **Keep everything for five years** after the tax period whose return was filed.
7. **File and pay** on the regime's timetable.

### The e-invoice system (منظومة الفاتورة الإلكترونية), B2B and B2G

- **What it is.** The seller creates a structured electronic invoice, signs it digitally and submits it to the ETA, which validates it. An invoice the ETA has not validated is not a valid tax invoice. The buyer's tax registration number must be on the invoice.
- **Legal basis.** Invoices and receipts must be issued as electronic documents, in the form and under the rules set by the executive regulations. If an invoice or receipt is cancelled, the taxpayer must keep the original and all its copies. This is Unified Tax Procedures Law Article 37, as reproduced in the ETA's [parallel-text guide to the VAT and Unified Tax Procedures laws][vg].
- **Registering.** A taxpayer named in a mandatory-registration decision must register. Taxpayers the ETA handles directly (including individual proprietors) apply at their tax office, the Digital Transformation Support Centre or the Central Administration for Electronic Transactions. They bring the tax card (plus the VAT certificate if registered), the authorised person's national ID and, for professionals, the syndicate card or professional certificate. The invitation arrives by email, usually within a week ([ETA Services Guide, 2nd edition](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf), service 3/1). The form is on the ETA [e-invoice services page](https://www.eta.gov.eg/ar/content/e-invoice-services).
- **Digital signature or seal.** E-invoices must be signed. Certificates are sold by the licensed providers the ETA lists (Egypt Trust, Misr for Central Clearing, Delta and Fixed). An individual must attend in person with their national ID. The ETA Services Guide notes a 3-month seal option agreed with providers to spread the cost (service 3/6). A USB token suits low volumes. Automated or higher-volume issuing from an ERP needs an HSM or approved signing set-up.
- **Portal or ERP integration.** A taxpayer may issue invoices by hand on the ETA portal only if both conditions are met: it issues no more than 200 invoices a month, and it has no accounting system (ETA President's Decision 233 of 2021). A temporary portal approval of 6 months from registration is given to taxpayers finishing their integration. Everyone else integrates an ERP through the ETA interface (ETA Services Guide, service 3/2).
- **Item coding.** Every good or service must carry a code before it can be invoiced: either GS1 (GTIN) or an internal EGS code mapped to the GPC classification. The taxpayer uploads codes from its system account. The ETA reviews code requests and approves or rejects them with reasons, within 24 hours of upload (ETA Services Guide, service 3/3). Do not invent codes. Code the catalogue before the go-live date.

### The e-receipt system (منظومة الإيصال الإلكتروني), B2C

- **What it is.** At each sale to a final consumer, the seller issues an e-receipt from a registered point of sale (POS) or ERP and transmits it to the ETA. The receipt must carry a QR code; the ETA FAQ says the executive regulations of the Unified Tax Procedures Law require this ([ETA e-receipt FAQ](https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf), edition 24, 31 January 2024).
- **No signature on receipts.** An e-receipt does not need an electronic signature (same FAQ). E-invoices do.
- **Timing.** The rule is real-time transmission. The ETA FAQ says the system currently accepts receipts up to 24 hours after issue, that the taxpayer bears the consequences of late sending, and that later receipts go through a late-submission request on the portal. The window is set administratively and can change. Confirm it in the current ETA e-receipt guidance before promising a client a window. The legacy "72 hours" figure has no ETA source.
- **Big-ticket sales.** Under the FAQ, a consumer receipt whose value exceeds EGP 150 thousand must carry the buyer's national ID number ("currently", so check for changes) ([ETA e-receipt FAQ](https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf)).
- **POS devices.** Buy POS devices only from ETA-approved suppliers (list on the [e-receipt services page](https://www.eta.gov.eg/ar/content/e-receipt-services)). An ERP can be registered as a virtual POS where the taxpayer has a single branch or outlet.
- **Phases.** The mandate has been extended group by group by ETA decisions. Earlier versions of this Guide quoted specific 2025 decision numbers, dates and a lowered turnover threshold. None of these could be confirmed from a readable ETA document, so they are not repeated here (check). The only reliable test is whether the taxpayer is named on the [e-receipt inquiry](https://www.eta.gov.eg/ar/ereceipt-inquiry) list, or holds a decision addressed to them.

### Which system applies

| Sale | System | Key points |
| --- | --- | --- |
| To a business or government (B2B/B2G) | e-invoice | Required whatever the value; digital signature; ETA validation; buyer's registration number on the invoice ([ETA e-receipt FAQ](https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf)) |
| To a final consumer (B2C) | e-receipt | Real-time transmission (currently up to 24 hours accepted); QR code; no signature; buyer's national ID above EGP 150 thousand |
| Mixed customer base | Both | One registered accounting system can issue both documents |

### Books and records under the regular regime

- **Who.** From 29 July 2026, every taxpayer carrying on a commercial, industrial, craft or professional activity must keep regular accounting records and books under the Commercial Law, manually or electronically ([Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf), Article 1). Businesses in the Law 6 regime are the exception. Before this change, Article 38 applied the duty only to a taxpayer whose annual turnover exceeded five hundred thousand pounds. That condition is gone. A sole proprietor or professional below it who kept no regular books must start now.
- **Electronic accounts.** The paragraphs of Article 38 that were not replaced still require every taxpayer to keep electronic accounts showing annual revenue and costs, under rules set by Minister of Finance decision. They also let the Minister set simplified book-keeping rules for classes of taxpayers ([ETA parallel-text guide][vg], Article 38). Which MoF decisions currently set those rules could not be confirmed from a readable ETA document (check).
- **Typical set for a self-employed person:**
  - cash book and bank book (دفتر الصندوق / البنك);
  - sales or fee register listing every e-invoice and e-receipt issued;
  - purchases and expenses register listing every supplier e-invoice received;
  - fixed-asset register supporting depreciation;
  - inventory records where stock is held;
  - payroll records if there are employees;
  - supporting documents: contracts, bank statements, import papers, and cancelled invoices with all their copies.
- **Professionals** (مهن حرة): keep a fee register and an expense register that tie to the e-invoices or e-receipts issued and to bank deposits.
- **Why it matters.** Regular books let the taxpayer be taxed on actual profit (revenue less deductible costs). Without them the ETA can estimate.

### Retention: five years

- Keep records, books and documents, including copies of invoices, for five years following the tax period for which the return is filed ([ETA parallel-text guide][vg], Unified Tax Procedures Law Article 38). The legacy suggestion that some advisers cite seven years has no official basis and is dropped.
- Keep electronic documents in electronic form: the signed XML or JSON, the ETA validation (UUID), and any PDF view.
- Practice point (not a statutory rule): while a period is under examination, appeal or dispute, keep its records until it is closed, even if the five years have run.

### Documentation and deductions

- **VAT.** Purchases from a supplier must be documented by an e-invoice, or input tax on them will not be allowed in the return. A buyer holding only an e-receipt (with no buyer name) cannot deduct. The supplier must issue an e-invoice for such a sale ([ETA e-receipt FAQ](https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf)).
- **Income tax costs.** Earlier versions stated that costs without an e-invoice are not deductible for income tax. No readable ETA document confirming this rule was found (check). As a conservative default, treat undocumented costs as at risk on examination, and tell the client you are doing so.

### The Law No. 6 of 2025 simplified regime

Law No. 6 of 2025 was issued on 12 February 2025 and applies from the first day of the following month, 1 March 2025 ([Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Article 16). It covers businesses, including professional activities, registered or not, whose annual turnover does not exceed EGP 20 million and which **ask** to use it (Article 1) ([ETA Services Guide, 2nd edition](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf), service 2/18).

**Income tax rates on turnover (Article 10).** The rate applies to the whole turnover. The band edges follow the law's wording: "less than" or "reaches ... and less than". Tax year 2026 rates are unchanged from 2025.

| Annual turnover | Rate |
| --- | --- |
| Less than EGP 500,000 | 0.4% ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)) |
| EGP 500,000 or more, and less than EGP 2,000,000 | 0.5% |
| EGP 2,000,000 or more, and less than EGP 3,000,000 | 0.75% |
| EGP 3,000,000 or more, and less than EGP 10,000,000 | 1% |
| EGP 10,000,000 or more, and not more than EGP 20 million | 1.5% |

The ETA Services Guide prints the top band as ending at 25,000,000. Law No. 6 of 2025 itself says twenty million, and the same guide's overshoot example uses twenty million, so follow the law.

**Conditions and rules of the regime** ([Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf)):

- **How turnover is measured** (Article 2). For a business registered on 1 March 2025, turnover comes from the last final assessment, or failing that the last return. For a business registered later, it comes from its return (the expected first-year turnover when applying). Data from the e-invoice or e-receipt systems can also be used.
- **Two conditions** (Article 3). The business must file its returns on time. It must also join the ETA's electronic systems, including the e-invoice or e-receipt system under the phase decisions, and actually issue the invoices or receipts. A business outside these systems loses the regime.
- **Exclusions** (Article 4). The regime does not apply to a professional consultancy that earns at least 90% of its annual turnover from consultancy for one or two persons (the Minister may exempt some activities). Nor does it apply to anyone who enters the regime improperly, for example by splitting an existing business without an economic reason. The ETA bears the burden of proving that.
- **Lock-in** (Article 5). A business cannot leave the regime until five years have passed from the day after its request. After that it applies on form 11/1 to return to the normal Income Tax Law basis ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)).
- **One-time overshoot** (Article 10). If turnover exceeds EGP 20 million in any year within five years of the request, by no more than 20% and only once, the business stays in the regime at the 1.5% rate. The ETA Services Guide puts the margin at EGP 4,000,000. A larger overshoot, or a second one, ends the regime from the following year ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)).
- **Reliefs** (Articles 7 to 9 and 11). The regime exempts the business from:
  - stamp duty and the state resource-development fee;
  - notarisation and registration fees on incorporation, credit, mortgage and land-registration contracts;
  - tax on capital gains from disposing of fixed assets and production equipment;
  - tax on profit distributions;
  - the withholding and advance-payment systems, in both directions.
- **Returns** (Article 12). An annual income tax return on its own form (form 20), filed on the normal dates: for an individual, 1 January to 31 March. A VAT return every three months, within the month after the quarter ends, with payment. Payroll tax obligations are limited to the annual settlement return, with payment. The ETA examines returns only after five years from the request, for both income tax and VAT ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)).
- **Books** (Article 13). The business is exempt from the Unified Tax Procedures Law books, records and documents. It must follow the simplified systems for records, books, documents and procedures set by Minister of Finance decision. Even so, keep a revenue record, an expense record, bank statements and every e-invoice and e-receipt for the five-year retention period. They are the evidence of turnover.
- **How to apply.** Submit request form 1/10 through the ETA electronic tax system (merged tax offices) or the ETA e-services portal (other offices). No fee is charged. Enterprises already under the tax provisions of the SME Development Law No. 152 of 2020 moved into the regime automatically ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf), service 2/18).

### Penalties and limits

- **Books and documents.** The Unified Tax Procedures Law punishes, with a fine of not less than twenty thousand and not more than one hundred thousand Egyptian pounds, anyone who breaches specified articles. These include Article 37 (first and fourth paragraphs, on issuing invoices and receipts, including electronically) and Article 38 (first, second and third paragraphs, on books and records). A separate fine of up to fifty thousand pounds applies for failing to keep paper or electronic books and records for the legal period (Article 71, as reproduced in the [ETA parallel-text guide][vg]). This is the 2021 consolidated text. Confirm that no later amendment changed the amounts before quoting them to a client (check).
- **Cap on late charges.** Since February 2025, a late-payment charge or additional tax cannot exceed the amount of the tax on which it is charged. The Minister may also settle offences that involve no unpaid tax, for a payment within statutory limits ([Law No. 7 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf), new Articles 45 bis and 75 bis).
- Earlier versions mentioned new "tiered penalties for 2026" for late e-document submission. No ETA source was found, so the claim is not repeated (check).

### Temporary tax card (new in 2026)

A new Article 27 bis lets the ETA grant a temporary tax card for eight months, so a taxpayer can finish setting up and licensing the activity. A temporary tax card **cannot** be used to issue e-receipts or e-invoices ([Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf), Article 2). A client on a temporary card who needs to invoice must get the permanent card and register on the systems first.

## Boundaries and exceptions

| Situation | Rule | Source |
| --- | --- | --- |
| Turnover below five hundred thousand pounds, not in Law 6 | Before 29 July 2026, no regular-books duty under Article 38. From 29 July 2026, regular books are required | [Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf) |
| Business in the Law 6 regime | Exempt from UTPL books; simplified records by MoF decision; e-invoice or e-receipt still required | [Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) Arts 3, 13 |
| Turnover exactly EGP 500,000 (Law 6) | "Reaches" the second band, so 0.5% applies, not 0.4% | [ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf) |
| Turnover exactly EGP 20 million (Law 6) | Still inside ("does not exceed"); 1.5% | [Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) Art. 1 |
| Consultant with at least 90% of turnover from one or two clients | Excluded from Law 6 unless the Minister exempts the activity | [Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) Art. 4 |
| No more than 200 invoices a month but uses an accounting system | Not eligible for permanent portal use; must integrate | [ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf) |
| Sale to a business paid in cash, small value | Still an e-invoice; an e-receipt does not support the buyer's VAT deduction | [ETA e-receipt FAQ](https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf) |
| Taxpayer on a temporary tax card | Cannot issue e-invoices or e-receipts | [Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf) Art. 2 |
| Cancelled invoice or receipt | Keep the original and all copies | [ETA parallel-text guide][vg] Art. 37 |

## Worked cases

Figures are for tax year 2026. Turnover amounts are illustrations.

**Case 1: freelance developer, B2B only, in Law 6.** A Cairo developer invoices three Egyptian companies and asked to join Law 6. Turnover for 2026 is EGP 1,200,000, issued as about ten invoices a month, with no accounting software. Rates: [ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf).

- Turnover reaches EGP 500,000 and is less than EGP 2,000,000, so the rate is 0.5% ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)).
- Income tax: 1,200,000 x 0.5% = EGP 6,000, on the Law 6 annual return, filed 1 January to 31 March 2027 ([Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Articles 10 and 12).
- Documents: e-invoices (B2B) with a digital signature and EGS codes for the services. Permanent portal use is allowed because the developer issues no more than 200 invoices a month and has no accounting system.
- Records: the simplified records, plus every e-invoice, purchase e-invoice and bank statement, kept for five years.

**Case 2: beauty salon, consumers only, regular regime.** The salon is named on the ETA e-receipt list.

- It connects an approved POS, codes its services, and prints a QR code on each receipt.
- It transmits each receipt in real time (currently accepted up to 24 hours) ([ETA e-receipt FAQ](https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf)).
- Not being in Law 6, it keeps regular books under Article 38 as amended from 29 July 2026, and retains them for five years.
- If a corporate client books a staff event, that sale needs an e-invoice, not a receipt.

**Case 3: small trader in Law 6.** A retailer with 2026 turnover of EGP 6,000,000 is in the 1% band (EGP 3,000,000 or more and less than EGP 10,000,000) ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)).

- Income tax: 6,000,000 x 1% = EGP 60,000 ([Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Article 10).
- It files VAT quarterly, within the month after each quarter, with payment.
- It issues e-receipts to consumers and e-invoices to trade buyers.
- Customers do not withhold tax from payments to it.

**Case 4: one-time overshoot.** The Case 3 trader grows, and 2027 turnover is EGP 23,500,000, the first overshoot within five years of its request ([Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Article 10).

- The ceiling for staying in is EGP 20 million plus the ETA's EGP 4,000,000 margin, which is EGP 24,000,000 ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)).
- The trader stays in at 1.5%: 23,500,000 x 1.5% = EGP 352,500 ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)).
- A second overshoot in the five years, or any overshoot above EGP 24,000,000, ends the regime from the next year ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)). Regular books are then required.

**Case 5: consultant with one main client.** A management consultant earns 95% of turnover from one company. The exclusion test is in [Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Article 4.

- The 90% exclusion applies, so Law 6 is not available ([Law No. 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Article 4).
- The consultant keeps regular books under the Commercial Law, and has done so since 29 July 2026 even if turnover is below the old threshold.
- The consultant issues signed e-invoices to the company and is taxed under the normal Income Tax Law rules.

## When to refuse or refer

Hand off to a qualified Egyptian accountant (محاسب قانوني) or tax adviser when:

- The taxpayer is not an individual, sole proprietor or professional (companies, partnerships, banks, regulated sectors).
- There is an examination, assessment, penalty notice or dispute with the ETA, or a settlement request. [Law No. 152 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.152.of_.2026.pdf) renewed the tax dispute-ending law.
- The client has open years from 1 January 2022 to before March 2025 and turnover up to ten million pounds. Article 4 of [Law No. 151 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf) sets a special turnover-based assessment for those periods, unless the taxpayer chooses the normal rules. Applying it needs a professional.
- The client needs a specific phase date, decision number or penalty amount that you cannot confirm on eta.gov.eg.
- The work involves ERP-to-ETA integration, HSM set-up, bulk EGS catalogue coding, or late-submission requests.
- There are cross-border, non-resident, withholding, transfer-pricing or e-commerce platform questions.

## Filing and payment

- **Normal regime, individuals.** The annual income tax return for the calendar year is filed 1 January to 31 March of the next year ([ETA Services Guide](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf)). The 2026 return is due by 31 March 2027. VAT-registered taxpayers outside Law 6 file VAT returns on the normal (monthly) timetable. The VAT computation is outside this Guide.
- **Law 6 regime.** The annual return on form 20 is due on the same dates. The VAT return is quarterly, within the month after the quarter, with payment. Payroll obligations are limited to the annual settlement return. There are no advance payments.
- **E-documents.** E-invoices are submitted and validated as issued. E-receipts are transmitted in real time (currently accepted up to 24 hours).
- **Returns filed now for 2025.** The 2025 individual returns were due by 31 March 2026. The Law 6 rates above also applied for 2025, from 1 March 2025. Article 38's old turnover condition for regular books still governs the books for 2025 and for 2026 up to 28 July 2026.

## Completion checklist

- [ ] Identified the regime: regular books (Article 38 as amended from 29 July 2026) or Law 6 simplified records.
- [ ] Identified the documents: e-invoice for B2B/B2G, e-receipt for B2C, or both.
- [ ] Checked the ETA e-invoice and e-receipt inquiry lists for the taxpayer's phase, or told the client to.
- [ ] Covered the digital signature (e-invoices only), item coding (GS1 or EGS), and the portal-vs-integration test (200 invoices a month and no accounting system).
- [ ] Stated the VAT rule that purchases need an e-invoice, and flagged income tax cost documentation as a conservative default.
- [ ] Stated five-year retention from the tax period whose return was filed. Electronic documents are kept electronically.
- [ ] For Law 6: checked the turnover band, the 90% consultancy exclusion, the five-year lock, and the one-time 20% overshoot.
- [ ] Flagged every point marked "check" in this Guide as unconfirmed.
- [ ] Replied in the user's language.

## Prohibitions

- Do not state an e-invoice or e-receipt phase date, decision number, registration threshold or submission window as settled unless it is confirmed on eta.gov.eg.
- Do not advise deducting input VAT on purchases not supported by an e-invoice.
- Do not tell a taxpayer they are exempt from e-invoicing or e-receipts. Direct them to the ETA inquiry lists.
- Do not invent GS1 or EGS codes. EGS codes need ETA approval.
- Do not obtain signature certificates, set up an HSM or register on the ETA portal on the user's behalf.
- Do not present this as filed advice. A qualified human must review it before anyone acts.

[vg]: https://eta.gov.eg/sites/default/files/2021-04/%D8%AF%D9%84%D9%8A%D9%84%20%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%D8%B9%D9%84%D9%89%20%D8%A7%D9%84%D9%82%D9%8A%D9%85%D8%A9%20%D8%A7%D9%84%D9%85%D8%B6%D8%A7%D9%81%D8%A9%20%D9%88%D8%A7%D9%84%D9%86%D8%B5%20%D8%A7%D9%84%D9%85%D9%82%D8%A7%D8%A8%D9%84%20%D8%A3%D9%88%D8%A7%D9%84%D9%85%D9%83%D9%85%D9%84%20%D9%85%D9%86%20%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D8%A5%D8%AC%D8%B1%D8%A7%D8%A1%D8%A7%D8%AA%20%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D9%8A%D8%A9%20%D8%A7%D9%84%D9%85%D9%88%D8%AD%D8%AF.pdf

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
