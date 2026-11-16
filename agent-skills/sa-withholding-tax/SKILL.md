---
name: sa-withholding-tax
description: "Saudi Arabia withholding tax for 2026: identify the resident or Saudi PE payer, non-resident recipient, source and payment category before computing gross-basis withholding. Covers management, royalties, technical and advisory services, rent, dividends, financing, insurance, freight, telecommunications and residual services; treaty evidence, PE interaction, mixed contracts, gross-up, filing, records and penalties. Preserves the original UK, Cayman, German and French supplier cases with corrected classifications and conditions. Read before any Saudi WHT calculation or return workpaper."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sa-withholding-tax"
  jurisdiction: "SA"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Saudi Arabia withholding tax: 2026

## Scope

Read this skill before classifying, computing or preparing a Saudi withholding-tax (WHT) workpaper. It covers Saudi-source payments to non-residents by Saudi residents and Saudi PEs of non-residents under Income Tax Law (ITL) art. 68. A resident natural person is a withholding agent only for payments connected with that person's business activity; personal consumption is outside that obligation. Zakat status does not itself exempt a payer from WHT. [ITL arts. 1, 3, 5, 68](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [May 2026 WHT guideline pp. 10-17](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

**Quick reference:** determine payer, recipient, source, PE connection, legal payment category, gross amount, settlement date and treaty entitlement before selecting a rate. The rate table below is the **2026** domestic table. A missing fact is a hold, not a reason to deem a recipient non-resident or impose the highest rate. WHT is calculated on gross in-scope consideration, rather than the recipient's profit; paying WHT does not prove the payer's expense is deductible.

This is not a Zakat, CIT, VAT, e-invoicing, excise, RETT, work-permit levy, petroleum-concession or Pillar Two calculation. Load [Zakat](sa-zakat.md), [CIT](sa-corporate-tax.md), [VAT](saudi-arabia-vat.md), [e-invoicing](saudi-einvoice.md), [excise](sa-excise-tax.md), [RETT](sa-rett.md) or [GOSI/employment compliance](sa-gosi-saudization.md) for the separate job.

## Ask the client first

1. Payer's legal identity, form, Saudi residence or Saudi PE, business activity, ZATCA registration and financial year.
2. Recipient's legal identity, residence, beneficial ownership, relationship to the payer, Saudi presence/PE and whether this payment is effectively connected with that PE.
3. Signed contract, invoice, actual services/rights/goods supplied, place of performance and use, and any separately priced components or reimbursements.
4. Gross or net-of-tax agreement, currency, supported SAR conversion, consideration including non-cash settlements, actual payment and any offset/credit-account settlement dates. An invoice accrual alone must be distinguished from settlement.
5. Treaty claimed, applicable text/effective dates, residence certificate for the period, beneficial ownership, anti-abuse evidence, relief/refund application and any ZATCA ruling.
6. Monthly payments and returns, WHT certificates, annual reconciliation, outstanding principal/penalties and any eligible penalty-initiative application.

Do not compute without the first four groups of facts. Treaty relief also needs group 5. A proposed estimate must show its missing classification and evidence, and cannot be filed as the legal result.

## The method, step by step

### 1. Establish the withholding relationship

Apply the residence conditions in ITL art. 3, not a mailing address, bank account, VAT number or assumed nationality. Saudi residents, including Zakat-paying entities and governmental bodies, can be withholding agents. A Saudi PE is also an agent on its own in-scope payments to non-residents, including its head office where the category/source test is met. [ITL arts. 3, 5(c), 68(a)](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [guideline pp. 11-15](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

Payments between Saudi residents are outside art. 68. A recipient's Saudi PE does not make all its worldwide receipts resident payments: establish **effective connection with that PE's activity**. Connected income is included in the PE's return under art. 68(f); actual WHT deducted from income included in a taxpayer's base is credited under art. 68(g). Route net-profit computation to CIT. The old references to art. 68(d) as the PE exclusion were incorrect. [ITL art. 68(f)-(g)](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [guideline pp. 15-17, 31, 42](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

The withholding agent is liable for failure to withhold/remit and for the required statements. ITL art. 68(d) also preserves recovery from the non-resident beneficiary or its representative/guarantor when withholding was not made. Do not promise that ZATCA can pursue only the payer. Contractual recovery between the parties is a separate question. [ITL art. 68(b)-(d)](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

### 2. Apply the actual Saudi-source rule

Use ITL art. 5 and IR arts. 5-6 by category. The place where money is paid does not determine source. Relevant sources include Saudi business activity; use or disposal of Saudi immovable property; Saudi company shares; movable property used in Saudi Arabia; industrial/intellectual property and royalties; dividends and management/directors' fees from a resident company; head-office/related-company services; services performed wholly or partly in Saudi Arabia; and resource and PE-connected income. The appropriate collection method may still be CIT rather than WHT. [ITL art. 5](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [guideline pp. 17-27, 37-42](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

Technical/advisory services supplied to a Saudi resident or connected with Saudi activity are Saudi-source even when performed offshore. The definition covers technical, technological, scientific, research, survey, consultancy, supervisory and engineering work, including related designs. Merely delivering an ordinary service through technology does not make it technical. Do not replace this category-specific rule with a universal “benefit used in Saudi Arabia” test for every offshore service. Related-company/head-office source rules must also be checked. [IR arts. 5(3), 6, 63(3)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [guideline pp. 22-24, 39-41](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

Pure imports of goods are not WHT services. A goods contract with installation, maintenance, training or other associated works needs the associated consideration identified; a separate customs/VAT charge is not WHT. Where a service is partly performed inside the Kingdom, the service-source rule may bring the whole service consideration into scope: an unsupported days/users split is not automatically permissible. Genuine separate supplies require a supportable allocation. [IR art. 5(7)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [guideline pp. 24-27, 40-41](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

### 3. Classify the payment and use the current domestic table

| Payment class, after scope/source tests | 2026 domestic WHT | Official source |
|---|---|---|
| Management-service contracts, including hotel/ship and comparable management | 20% | ITL art. 68; IR art. 63; guideline p. 28 and pp. 38-39, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Royalty: use/right to use intellectual property, know-how and the rights within the statutory definition | 15% | ITL art. 1; IR art. 63; guideline pp. 28, 33-36, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Technical/advisory services, including related-party/head-office services when actually in this class | 5% | Amended IR art. 63(1), [gazette old/new comparison dated 12 September 2023](https://www.uqn.gov.sa/details?p=23668); [guideline p. 28](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Rent, within the relevant Saudi-source rule | 5% | IR art. 63; guideline pp. 25, 28, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Dividends, including qualifying branch-profit transfers and excess-over-capital liquidation distributions | 5%, subject to the oil/gas dividend exclusion below | IR art. 63(6); guideline pp. 28-29, 37-38, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Loan returns/income from debt claims | 5%, subject to the specified interbank exclusion | IR arts. 5(1), 63; guideline pp. 6, 21-22, 28, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Insurance/reinsurance premiums within the source rules | 5% | IR arts. 5(2), 63; guideline pp. 22, 28, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| International departure travel tickets and relevant air/sea freight; inbound goods freight excluded | 5% | IR art. 63(4), [2023 amendment](https://www.uqn.gov.sa/details?p=23668); [guideline pp. 5, 26-28](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| International telephone communications within the statutory definition; check exclusions | 5% | Amended IR art. 63(1), [gazette](https://www.uqn.gov.sa/details?p=23668); [guideline pp. 6, 28](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Land transport within the Kingdom | 15% | Guideline p. 28, residual-service treatment, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Other in-scope service payments not in a specified class | 15% | IR art. 63(7); guideline p. 28, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |

**Reconciliation of the old related-party rate:** the older official regulation compilation still displays 15% for technical/advisory/telephone services to a head office or related company. The **2023 gazetted amendment removes that distinction**, leaving those specified services at 5%; the May 2026 guideline confirms it. Related-party status remains relevant to source, pricing and disclosure, but does not turn a correctly classified technical service into a management fee or royalty. The amendment also excludes capitalised construction financing from the separate CIT limitation; do not confuse that deduction change with WHT relief. [Gazette amendment to IR arts. 9(2), 63(1), 63(4)](https://www.uqn.gov.sa/details?p=23668).

### 4. Test definitions and exclusions before applying a percentage

- **Software, SaaS and know-how:** read the actual rights. A right to exploit IP, reproduce/modify qualifying software, a protected know-how transfer or access to the specified technical/scientific information can be a royalty. Separate support/development/maintenance may be technical services. Personal/recreational software, magazine subscriptions, advertising space and some distribution rights are not automatically royalties. The guideline's classification table is not a blanket rule that every SaaS subscription is a royalty. [Guideline pp. 23, 33-36](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
- **Management versus professional service:** classification follows the actual functions, management contract and commercial value, not the invoice title, related-party status or the largest available rate. Directors' fees also need their actual legal category; do not label all board remuneration as management. [Guideline pp. 6, 28, 37-39](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
- **Loan returns:** the interbank exception is limited to deposits with the resident borrowing bank for a maximum of **90 days**, with the annual SAMA-approved statement identifying lending banks, addresses, duration and returns. It is not a general exemption for foreign bank interest. [IR art. 5(1)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [guideline pp. 6, 21-22](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
- **Telecommunications:** the specified network use for passing/transmitting/delivering international calls and international roaming payments are excluded as described in the guideline; satellite, cable, internet-capacity and interconnection arrangements require the underlying contract. Do not exempt all telecom payments. [Guideline pp. 6, 28](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
- **Transport:** inbound goods freight to Saudi ports is excluded from the specified air/sea freight class; qualifying outbound transport and connected onward transport can be in scope. Determine whether a separately undertaken foreign onward leg is part of the original Saudi carriage. The ship's flag does not by itself determine the operator's residence or exemption. [Guideline pp. 5, 26-28](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
- **Distributions:** CIT paid by a company does not remove WHT from a subsequent in-scope distribution. Distributions by companies operating in natural-gas/oil/hydrocarbon investment have the specific exemption. Estimated-profit assessments are not automatically distributions: apply the actual payment/offset and listed deemed-profit circumstances in the guideline, including estimated returns, undeclared revenue, missing books/returns/bank accounts, evasion cases or written agreement. [IR art. 63(6)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [guideline pp. 29, 37-38](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
- **Capital gains:** disposal of Saudi property, shares or assets is not the residual WHT-service category. It follows the general income-tax rules and any exemption/treaty conditions. Refer for cost basis, valuation, listed-securities conditions and treaty analysis; never withhold the ordinary CIT percentage from gross sale proceeds. [IR art. 1(2)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [guideline pp. 8, 18-20, 25](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
- **GCC:** a recipient's GCC residence or ownership does not itself establish Saudi residence or a blanket WHT exemption. Test the actual law/treaty and the payment. Do not transplant the Saudi/GCC Zakat ownership rule into an offshore-payment exemption. [ITL arts. 3, 5, 68](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

### 5. Determine gross consideration, settlement and gross-up

WHT is on the gross in-scope consideration without deducting the recipient's costs. Include cash or in-kind consideration and settlements/offsets/book adjustments that discharge the liability. A booked invoice or ordinary unpaid accrual is not automatically a payment merely because the payer uses accrual accounting; identify whether a credit-account entry actually settles the amount. [ITL art. 68](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [guideline pp. 9-10, 17](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

Read the contract to determine whether the price is gross or guarantees a net receipt. For a contractually guaranteed net amount **N** and applicable decimal rate **r**, derive **gross = N ÷ (1 − r)** and **WHT = gross × r**. Do not assume a gross-up clause, deduct the recipient's expenses, net unrelated receivables or strip a VAT/reimbursement amount without establishing its legal character. VAT and WHT are different liabilities, but that does not decide every composite-invoice base. Convert the determined consideration to SAR using a documented permissible tax conversion basis and retain the rate/date evidence; the old universal earlier-of-accrual/SAMA-date rule is not established here. [ITL art. 68](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [IR art. 63(8)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).

There is no monetary small-payment exception in art. 68 itself; that does not bring a payment outside its residence/source/service conditions into scope. Apply classification before amount.

### 6. Test the particular treaty and relief route

Confirm the agreement exists, is effective for this payment, covers the tax and recipient, and as modified by any applicable MLI provisions gives the claimed treatment. Determine whether the income is royalty, business profit, transport, rent, debt income, dividend or another class under **that treaty's definitions**. A treaty cap is a maximum, not permission to increase a lower domestic tax. Residence evidence alone does not establish beneficial ownership, an absence of a connected PE/fixed base, arm's-length amount or anti-abuse compliance. [WHT guideline p. 29](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf); [UK synthesised treaty, arts. 1-5, 7, 10-12, 28](https://www.gov.uk/government/publications/saudi-arabia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2007-uk-saudi-arabia-double-taxation-convention-and-protocol-in-force).

| UK treaty provision, only for an entitled UK resident | Maximum source-state treatment | Official source |
|---|---|---|
| Ordinary dividends beneficially owned by a UK resident | 5%; specified property-investment-vehicle dividends have a 15% treaty ceiling, without raising lower domestic tax | UK treaty art. 10(2), [synthesised text](https://www.gov.uk/government/publications/saudi-arabia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2007-uk-saudi-arabia-double-taxation-convention-and-protocol-in-force) |
| Income from debt claims beneficially owned by an entitled UK resident | Taxable only in residence state; connected-PE/fixed-base and special-relationship excess rules remain | UK treaty art. 11, [synthesised text](https://www.gov.uk/government/publications/saudi-arabia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2007-uk-saudi-arabia-double-taxation-convention-and-protocol-in-force) |
| Royalty for industrial/commercial/scientific equipment | 5% gross ceiling, subject to entitlement and connection/excess conditions | UK treaty art. 12(2)(a), [synthesised text](https://www.gov.uk/government/publications/saudi-arabia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2007-uk-saudi-arabia-double-taxation-convention-and-protocol-in-force) |
| Other qualifying royalties | 8% gross ceiling; beneficial owner, relevant residence, no overriding connected-PE/fixed-base rule, arm's-length amount and anti-abuse conditions | UK treaty art. 12(2)(b), (4)-(6), art. 28 as replaced by MLI art. 7, [synthesised text](https://www.gov.uk/government/publications/saudi-arabia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2007-uk-saudi-arabia-double-taxation-convention-and-protocol-in-force) |

The original UK debt-income 7.5% entry is not supported by art. 11. The UK principal-purpose test denies a benefit where obtaining it was one principal purpose of the arrangement unless granting it accords with the provision's object and purpose. Do not claim this exact provision applies to every Saudi treaty. [UK synthesised treaty arts. 11, 28/MLI art. 7](https://www.gov.uk/government/publications/saudi-arabia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2007-uk-saudi-arabia-double-taxation-convention-and-protocol-in-force).

ZATCA's **“Request to apply double-taxation agreements”** service uses **form Q7B (ق 7ب)**. The service page instructs the user to enter tax services, select the treaty application, complete/submit the form, print it, obtain the other tax authority's signature/authentication and deliver it to ZATCA. It serves the non-resident/authorised representative and the resident withholding agent, for rate application **or a refund**. Keep the signed form, TRC, entitlement analysis, WHT certificate, contract and payment records and follow the actual application outcome. Do not treat a TRC as automatic authority to apply a reduced rate; nor assert that every treaty-rate claim follows an identical pre-approval route. [Official service instructions](https://zatca.gov.sa/ar/eServices/Pages/eServices-219.aspx).

If entitlement/application is unresolved, show the domestic liability separately from a potential recoverable difference. Do not promise a refund, unilaterally reopen a historical rate or equate final domestic WHT with an absolute prohibition on treaty refunds. Art. 68(e)'s finality is subject to its PE/credit provisions and the applicable international instrument. [ITL art. 68(e)-(g)](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [guideline pp. 29-31](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

## Boundary and exception table

| Facts | Action |
|---|---|
| Resident recipient or income effectively connected with a Saudi PE | Test the connection and CIT-return treatment; preserve any actual WHT credit evidence. |
| Foreign entity uses Saudi staff/sites/agents | Test domestic and applicable treaty PE before assuming a final gross-basis tax; no universal service-day/construction threshold. |
| Related offshore service | Test actual source and payment class; do not reintroduce the superseded related-party technical rate. |
| Goods plus on-site work | Identify separately priced work, contract scope and PE risk; no automatic whole-contract or unsupported zero allocation. |
| Reimbursement or cost recharge | Establish the original obligation, agency, supplier, documents and whether it is consideration for a service; invoice names alone do not decide it. |
| Royalty, SaaS, software support or know-how | Read rights and actual performance; route ambiguous classification for an opinion. |
| Private ruling, settlement, treaty or foreign credit | Obtain the actual instrument and conditions; do not reconstruct it from a summary. |

## Worked cases

These retain the original **Saudi LLC** and counterparties. Monetary amounts and exchange rates are illustrative inputs; the legal table is current for **2026**. No actual historical return is approved by recomputing an example.

### 1. UK software company: decide royalty classification and relief eligibility

Saudi LLC pays **SAR 500,000** for the original annual SaaS licence. First inspect the rights: the label “SaaS” alone does not prove a royalty. The following arithmetic applies **only if** the payment is a statutory and treaty **other royalty**, with no effective PE connection. Without established treaty entitlement/application, domestic WHT is **SAR 75,000**, net **SAR 425,000**. Where an entitled UK beneficial owner has the applicable residence/anti-abuse evidence and the relief route is properly satisfied, the art. 12(2)(b) ceiling gives **SAR 40,000**, net **SAR 460,000**. The **SAR 35,000** difference is a potential claim, not an automatic receivable. A service or business-profits classification must be analysed separately; do not force the royalty treatment to preserve the old answer. [Guideline pp. 33-36](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf); [UK treaty art. 12](https://www.gov.uk/government/publications/saudi-arabia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2007-uk-saudi-arabia-double-taxation-convention-and-protocol-in-force).

```oa-check
name: Saudi LLC UK royalty domestic versus entitled treaty treatment
inputs:
  gross_qualifying_royalty: 500000
steps:
  - domestic_wht: gross_qualifying_royalty * 0.15
  - domestic_net: gross_qualifying_royalty - domestic_wht
  - entitled_treaty_wht: gross_qualifying_royalty * 0.08
  - treaty_net: gross_qualifying_royalty - entitled_treaty_wht
  - potential_difference: domestic_wht - entitled_treaty_wht
expected:
  domestic_wht: 75000
  domestic_net: 425000
  entitled_treaty_wht: 40000
  treaty_net: 460000
  potential_difference: 35000
```

### 2. Cayman parent: actual management contract

Saudi LLC pays its Cayman parent **SAR 1,000,000** under an actual management-services agreement. On the stated domestic classification, with no established treaty/incentive relief, WHT is **SAR 200,000** and net remittance **SAR 800,000**. The category follows the actual management functions, not the parent's location. Obtain the related-party benefit, cost, pricing and performance evidence separately for CIT/Zakat deductibility; the WHT rate does not impose a universal benchmarking-study requirement or prove deductibility. The original claim that no Cayman treaty exists is not used as a verified current treaty-network statement. [Guideline pp. 28, 38-39](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

```oa-check
name: Saudi LLC Cayman parent management fee
inputs:
  gross_management_fee: 1000000
steps:
  - wht: gross_management_fee * 0.20
  - net_remittance: gross_management_fee - wht
expected:
  wht: 200000
  net_remittance: 800000
```

### 3. German parent: related-party engineering correction

Saudi LLC pays its German parent **SAR 600,000** for genuine remote technical-engineering services, with no established treaty relief or connected Saudi PE. The domestic source rule covers the specified technical service even though it is performed in Germany. The amended class is **5%**, so WHT is **SAR 30,000** and net **SAR 570,000**. The old **SAR 90,000/net SAR 510,000** used the superseded related-party distinction; the difference is **SAR 60,000**. Do not infer a general Germany DTT or a royalty/management class from the missing TRC. [IR art. 63(1), 2023 amendment](https://www.uqn.gov.sa/details?p=23668); [guideline pp. 22-23, 28](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

```oa-check
name: Saudi LLC German parent technical engineering rate reconciliation
inputs:
  gross_technical_fee: 600000
steps:
  - current_wht: gross_technical_fee * 0.05
  - current_net: gross_technical_fee - current_wht
  - superseded_rate_comparison: gross_technical_fee * 0.15
  - difference: superseded_rate_comparison - current_wht
expected:
  current_wht: 30000
  current_net: 570000
  difference: 60000
```

### 4. French supplier: goods versus associated installation/training

Saudi LLC's contract separately prices equipment **CIF Jeddah EUR 2,000,000**, Saudi on-site installation/training **EUR 500,000**, total **EUR 2,500,000**. For this illustration only, the supported conversion input is **SAR 4.10/EUR**; it is not a sourced current exchange rate. Assume a non-resident supplier with no Saudi PE, services qualifying as technical work, a gross-of-WHT price and no established treaty relief. Goods remain outside the service base; the **SAR 2,050,000** service component gives **SAR 102,500 WHT**. Relationship alone does not increase this technical-service rate. [Guideline pp. 24-27, 40-41](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

If the contract fails to separate the work, the guideline requires the associated work to be estimated from the contract facts/value. The old automatic **SAR 10,250,000 whole-contract base/SAR 512,500 WHT** is not established by that rule. Hold the filing allocation until the contract, technical scope, valuation and PE facts support it; do not call the entire goods price a service merely to be conservative.

```oa-check
name: Saudi LLC French supplier separately priced equipment and technical works
inputs:
  equipment_eur: 2000000
  services_eur: 500000
  illustrative_sar_per_eur: 4.10
steps:
  - contract_sar: (equipment_eur + services_eur) * illustrative_sar_per_eur
  - service_base_sar: services_eur * illustrative_sar_per_eur
  - wht: service_base_sar * 0.05
  - service_net_sar: service_base_sar - wht
expected:
  contract_sar: 10250000
  service_base_sar: 2050000
  wht: 102500
  service_net_sar: 1947500
```

### 5. Net royalty contract: gross-up is a contract decision

Preserve the original **SAR 100,000 net** royalty illustration. Where the contract guarantees that amount and the actual domestic royalty rate applies, gross consideration is **SAR 117,647.06** and WHT **SAR 17,647.06**. If the stated amount is gross instead, WHT is deducted from it and the net differs. Determine the contract before choosing either method. [ITL art. 68](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

```oa-check
name: Net-of-WHT royalty versus gross contract decision
inputs:
  agreed_amount: 100000
  royalty_rate: 0.15
steps:
  - gross_if_net_guaranteed: agreed_amount / (1 - royalty_rate)
  - wht_if_net_guaranteed: gross_if_net_guaranteed * royalty_rate
  - wht_if_price_is_gross: agreed_amount * royalty_rate
  - net_if_price_is_gross: agreed_amount - wht_if_price_is_gross
expected:
  gross_if_net_guaranteed: 117647.06
  wht_if_net_guaranteed: 17647.06
  wht_if_price_is_gross: 15000
  net_if_price_is_gross: 85000
```

## When to refuse or refer

- **R-SA-WHT-1:** Zakat computation: load Zakat.
- **R-SA-WHT-2:** resident/PE net-profit CIT: load CIT, preserving actual WHT credit evidence.
- **R-SA-WHT-3:** VAT, e-invoicing or excise: load the relevant sibling.
- **R-SA-WHT-4:** upstream petroleum/concession or special-sector entitlement: specialist review.
- **R-SA-WHT-5:** treaty claim without period-specific residence/entitlement evidence and a proper application route: do not claim relief; show domestic and unresolved treaty positions separately.
- **R-SA-WHT-6:** effectively connected Saudi PE income: route to the PE's CIT analysis; determine connection rather than exempting all recipient income.
- **R-SA-WHT-7:** non-resident capital gains: refer for ordinary income-tax, exemption, valuation and treaty analysis; not a residual WHT calculation.
- **R-SA-WHT-8:** contested mixed-contract/source allocation: hold until supporting contracts and an allocation are available.
- **R-SA-WHT-9:** undocumented reimbursements: require the original obligations, invoices and agency/service evidence.
- **R-SA-WHT-10:** private ruling/settlement claimed: obtain the original instrument and confirm its taxpayer, facts and period.
- **R-SA-WHT-11:** Pillar Two/GloBE credit/top-up modelling: refer; no automatic allocation or enacted Saudi DMTT is asserted here.
- **R-SA-WHT-12:** expatriate levy/work-permit fees: employment-compliance job, not art. 68 WHT.

Also hold for missing residence, payment character, gross/net terms, FX basis, effective settlement date or a disputed catch-all classification. Do not select a higher rate to replace the inquiry. Refund inconvenience does not make over-withholding legally correct. PE registration, treaty thresholds, director exposure and foreign-credit relief need the actual law and facts; no generic numerical threshold or personal liability opinion is supplied.

## Filing and payment

1. Register the withholding agent before the first required payment and establish the taxpayer's authorised ZATCA account. [IR art. 55(1)(b)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).
2. Reconcile actual in-scope settlements for the month to the payment ledger, contract, beneficiary, country/address/tax ID where available, class, gross SAR amount, supported conversion, rate, WHT and treaty application. Use the approved monthly WHT statement for that period; do not invent current box IDs. [ITL art. 68(b)](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [guideline pp. 30-31](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
3. File the monthly statement and remit WHT within the first **10 days of the following month**. No monthly statement is required where there are no amounts subject to WHT. Give the beneficiary the required certificate showing the paid amount and WHT, and retain submission/payment evidence. [IR art. 63(9)(a)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [guideline p. 30](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
4. Prepare the annual statement within **120 days** of fiscal year-end; a partnership has **60 days**. Reconcile to the monthly statements and books. A zero annual amount does not remove the annual statement where withholding cases existed during the year. The annual statement is a summary, not a second charge on the same payments. [IR art. 63(9)(b)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [guideline p. 30](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).
5. Keep at least the beneficiary's name/address, payment class, value, amount withheld and supporting documents for **10 years after payment**, extending retention while the matter remains under competent-authority consideration until completion/final decision. [IR art. 63(9)(c)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [guideline p. 31](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

### Penalties, disputes and temporary relief

| Provision | Amount/condition | Official source |
|---|---|---|
| Late remittance | 1% of unpaid tax per 30 days of delay, from the applicable due date; not a tax-specific monthly cap invented from VAT/CIT tables | ITL art. 77(a); IR art. 68(1)(e), [guideline p. 32](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| False information/fraud intended to evade | 25% of the resulting tax difference, in addition to applicable delay consequences and subject to the actual statutory conditions | ITL art. 77(b); IR art. 69, [guideline p. 32](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |

The old generic SAR 1,000-10,000 penalty **per monthly return** is not a verified WHT rule; do not reuse the registration-penalty table as that charge. ITL art. 65's assessment framework and formal objections require the correct filing deadline and facts, not the old blanket “5 years after payment-year-end” assumption. Preserve notices and obtain a dispute opinion through the CIT/dispute handoff. [ITL arts. 65, 68, 77](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

The current penalty initiative is a separate eligibility check: **1 July-31 December 2026**, subject to registration, required returns and principal settlement or an approved adhered-to instalment plan. Returns due after **30 June 2026**, evasion, already-paid fines and the listed VAT art. 45 fines are excluded. It does not waive principal or authorise a late payment. Keep the authority's account/approval evidence before recording relief. [Initiative guideline pp. 3-9](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf).

## Completion checklist

- Payer/recipient, source, PE connection, actual payment class and settlement date are evidenced.
- Current amended rates are used; technical services are not automatically related-party management/royalty payments.
- Gross/net, non-cash consideration, allocation, FX and treaty conditions reconcile to the contracts and ledger.
- Monthly and annual statements, beneficiary certificates and tax-account payments agree; no annual double charge or duplicate PE credit.
- Records and unresolved items remain available for the professional reviewer; no missing evidence became a default tax result.

## Sources

| Official source | Actual reading on 2026-11-16 |
|---|---|
| [Income Tax Law, official Arabic consolidation](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) | Read on 2026-11-16. Read for arts. 1-5, 65, 68 and 77: person, residence/source, payer liability, finality, PE/credit exceptions, assessment boundary and penalties. |
| [Income Tax IR, official historical compilation](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf) | Read on 2026-11-16. Read arts. 1(2), 5-6, 55, 63, 68-69 and neighboring definitions. Its old related-party rate wording is superseded by the next row. |
| [Official Gazette amendment, 12 September 2023](https://www.uqn.gov.sa/details?p=23668) | Read on 2026-11-16. Read old/new art. 63(1) and (4), plus neighboring art. 9(2): removes the related-party distinction for specified technical/advisory/telephone payments and clarifies departure-ticket scope. |
| [General WHT Guideline, second version May 2026](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) | Read on 2026-11-16. Read pp. 5-42, including source examples, category/exclusion table, software/know-how distinctions, records and penalty provisions. |
| [UK-Saudi treaty synthesised with the MLI](https://www.gov.uk/government/publications/saudi-arabia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2007-uk-saudi-arabia-double-taxation-convention-and-protocol-in-force) | Read on 2026-11-16. Read arts. 1-5, 7, 10-12 and 28/MLI art. 7 and the surrounding connection/special-relationship provisions. The exact treaty, not a generic network table, supports the UK case. |
| [ZATCA treaty-application service](https://zatca.gov.sa/ar/eServices/Pages/eServices-219.aspx) | Read on 2026-11-16. Read the service purpose, Q7B form, filing/authentication steps and eligible applicant/rate-or-refund descriptions. No taxpayer account or application was accessed. |
| [Penalty initiative, effective July 2026](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf) | Read on 2026-11-16. Read pp. 3-11, particularly exclusions, pre-July return boundary, principal settlement and instalment-plan consequences. |

**Not yet confirmed:** the old global/regional management-fee ranking, general GAZT/Customs merger chronology and corporate-calendar prevalence, unspecified significant-economic-presence/digital-services guidance; the old non-UK treaty-rate matrix for France, China, India, Pakistan, Singapore, South Korea, Japan, Germany, Netherlands, Spain, Russia and Turkey, and the broader legacy treaty-network list (including the remaining European, Asian, African, Central Asian and American counterparts) have not been reverified agreement by agreement; no rate, existence, ratification, MLI coverage or current applicability from those lists is usable here. In particular, the alleged general Germany 2007 treaty and unconditional Cayman no-treaty statement are not established. Also unconfirmed are a universal TRC/pre-approval rule, current portal box identifiers, a universal SAMA/accrual-date conversion rule, automatic VAT/reimbursement treatment, fixed monthly-return administrative fines, transaction-specific criminal referral/exposure, generic service-day/construction PE thresholds, director-level personal exposure, and any Saudi DMTT/GloBE credit-allocation conclusion. Each remains a source/evidence boundary rather than an assumed tax result.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sa-withholding-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sa-withholding-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
