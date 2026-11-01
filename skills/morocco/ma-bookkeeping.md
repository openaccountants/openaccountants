---
name: ma-bookkeeping
description: >
  Use this skill whenever asked about record-keeping, bookkeeping or invoicing obligations in
  Morocco for tax year 2026: which books or registers each tax regime must keep, what must appear
  on an invoice, the ICE identifier, electronic accounting, the invoicing system under CGI Art.
  145-IX, retention, audit production, and when a taxpayer moves to the real net income regime.
  Trigger on phrases like "Morocco bookkeeping", "comptabilite Maroc", "facture ICE",
  "e-invoicing Morocco", "facturation electronique Maroc", "registre des recettes", "tenue de
  comptabilite Maroc", "mentions obligatoires facture", "محاسبة المغرب", "فاتورة ICE". Covers
  auto-entrepreneur, CPU, RNS, RNR and companies. Reply in the user's language (English, French,
  or Moroccan Arabic / Darija). Cross-reference ma-auto-entrepreneur, ma-cpu,
  morocco-professional-income-tax and morocco-vat for the tax computation.
version: 2.0
jurisdiction: MA
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Bookkeeping v2.0

## Scope

This skill tells an AI what books, registers and invoices a Moroccan taxpayer must keep for 2026, and for how long, by tax regime. It does not compute the tax: that is ma-auto-entrepreneur, ma-cpu, morocco-professional-income-tax and morocco-vat. All article numbers refer to the Code General des Impots (CGI) 2026, DGI edition, which includes Finance Law 50-25. Reply in the user's language and keep the native terms (comptabilite, facture, ICE, registre, DGI).

Covered: individuals under the auto-entrepreneur regime (AE), the contribution professionnelle unique (CPU), the resultat net simplifie (RNS) and the resultat net reel (RNR), and companies. Non-resident companies with a permanent activity in Morocco are covered at Art. 147 level.

## Ask the client first

1. Which regime applies: company, RNR, RNS, CPU or AE?
2. Activity type: commercial, industrial or craft, or services?
3. Turnover for each of the last two years, and for AE, turnover collected.
4. Is the taxpayer subject to VAT?
5. Are the books kept by electronic process?
6. Are the customers businesses or private individuals?

If the regime is unknown, assume the higher standard: Art. 145 records, 10 years' retention. If turnover is near a ceiling, apply the two-year test below rather than assume a breach.

## The method, step by step

### Step 1. Figures and limits ([CGI 2026](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| RNS ceiling, trade, industry, craft, fishing vessel owners | MAD 2,000,000 excl. VAT | 2026 | Art. 39; option holds until exceeded for two consecutive years | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| RNS ceiling, services and Art. 30 (1 c, 2) | MAD 500,000 excl. VAT | 2026 | Art. 39; same test | same |
| CPU ceiling, trade, industry, craft | MAD 2,000,000 | 2026 | Art. 41-II-A; two consecutive years over means RNR from 1 January following | same |
| CPU ceiling, services | MAD 500,000 | 2026 | Art. 41-II-A; same test | same |
| AE ceiling, trade, industry, craft | MAD 500,000 collected | 2026 | Art. 42 ter-II-A, 43-4 | same |
| AE ceiling, services | MAD 200,000 collected | 2026 | Art. 42 ter-II-A; two consecutive years over means RNR from 1 January following, unless RNS or CPU is opted for, and AE is lost | same |
| Retention | 10 years | 2026 | Art. 211; all taxpayers and withholding agents, at the place of taxation | same |
| Loss of records notice | 15 days, 30 for force majeure | 2026 | Art. 211; registered letter to the inspector from the date the loss is found | same |
| No retention | MAD 50,000 per year | 2026 | Art. 185 bis-I; issued without procedure | same |
| ICE omitted or wrong | MAD 100 per item | 2026 | Art. 198 ter; breach of Art. 145-VIII | same |
| Books not on electronic support at audit | MAD 50,000 per year | 2026 | Art. 191 bis; those keeping books by electronic process | same |
| Documents not produced, or audit refused | MAD 2,000, plus MAD 100 a day up to MAD 1,000 | 2026 | Art. 191-I; for income tax the fine is MAD 500 to 2,000; procedure in Art. 229 | same |
| False invoices, false entries, repeated sales without invoice, destroying records | MAD 5,000 to 50,000, plus 1 to 3 months in prison | 2026 | Art. 192-I; intent to evade, procedure in Art. 231 | same |
| Non-traceable settlement | 6% of the transaction | 2026 | Art. 193; MAD 20,000 or more, charged on the seller, for example company to business | same |
| Cash expense limit | MAD 5,000 a day per supplier | 2026 | Art. 11-II, 106-II; the monthly cap is in morocco-vat | same |

### Step 2. Records by regime

| Regime | Records | Source |
|---|---|---|
| Company, RNR | Accounting under the law in force, in Art. 145-I; year-end detailed stock inventories, in quantities and values (Art. 145-II); full invoices (III) | Art. 145 |
| RNS | One or more regular registers of all sums received from sales, works and services, and all sums paid for purchases, staff and other operating costs; invoices to business customers; year-end list of debtors and creditors; stock inventories; depreciation register | Art. 145-VI |
| CPU individual | Art. 145 does not apply. Purchases must be real and backed by a regular invoice in the taxpayer's name; on inspection DGI can ask for purchase invoices or other evidence | Art. 145-XI, 146 bis, 210 |
| AE individual | Art. 145 does not apply. Declares turnover collected monthly or quarterly | Art. 145-XI, 82 bis |
| Anyone subject to VAT | Regular accounting that shows turnover and deductible VAT; split by activity where VAT treatment differs | Art. 118 |
| Non-resident company with permanent activity | Accounts of all Moroccan operations at the main Moroccan establishment; livre-journal and livre d'inventaire numbered and initialled by the commercial court or, failing that, stamped by the local tax service | Art. 147-I |
| Non-resident on flat-rate option | Register of receipts and transfers, salary register stamped by the labour inspector, register of fees and commissions | Art. 147-II |

Art. 145 bis, once cited for a CPU register, is repealed. Do not cite it. Art. 145-VI is the tax rule for RNS: registers, not automatically full double entry. A merchant's duties under accounting law 9-88 are separate; see the Not yet confirmed line.

The RNS depreciation register is stamped by the head of the local tax service, has numbered pages, and shows for each asset: nature, use and location, purchase invoice reference, cost, rate, annual charge, and net value after each charge. A depreciation charge is deductible only if entered there (Art. 145-VI-3).

Art. 211 names the books DGI expects where they exist: grand livre, livre d'inventaire, detailed inventories, livre-journal, and customer and supplier cards.

### Step 3. The invoice (Art. 145-III and VIII)

Pre-numbered from a continuous series, or issued by a computer system in a continuous series, showing:

1. Seller's identity.
2. Tax identification number and business tax (taxe professionnelle) number.
3. Date of the operation.
4. Customer's name or company name, address and ICE.
5. Price, quantity and nature of goods, works or services.
6. VAT shown separately. For Art. 91, 92 and 94 operations, state the exemption or suspensive regime instead.
7. Payment references and method.
8. Any other mention required by law.
9. The seller's ICE, on invoices and on all tax returns.

A till receipt can replace the invoice for sales of goods to private individuals, showing date, seller, description, quantity and price with any VAT. Clinics split fees between clinic and doctors (Art. 145-IV). Tour sellers show the customer's business tax number unless they file the sales statement by customer (Art. 145-V). Non-merchants put their tax numbers on all documents (Art. 145-VII).

Purchase side: a purchase invoice must carry the same Art. 145-III and VIII mentions and be regular and probative (Art. 146). Deduction is refused for an invoice from a listed defaulting supplier with no real activity, or from an inactive company (Art. 146, 228 bis). Businesses need an ICE for exemptions (Art. 164-I). Annual returns attach a sales statement with ICE by customer (Art. 20-I, 82-I).

### Step 4. Electronic accounting and invoicing

- Art. 145-I: taxpayers must also keep accounts in electronic format under the law and regulations in force. Art. 247 ties this to criteria set by regulation. Those taxpayers hand over a copy of the accounting entries file at audit (Art. 210) and retain documents on electronic support (Art. 211).
- Art. 145-IX: companies, RNR and RNS taxpayers and those subject to VAT must have a computer invoicing system meeting DGI's technical criteria, with terms set by regulation for each sector. The law gives no date.
- Art. 145-X: every taxpayer must hold an email address of their choice. This one duty also binds CPU and AE individuals (Art. 145-XI).

### Step 5. Retention and audit

Keep sales invoice copies or till receipts, expense and investment evidence, and accounting documents 10 years. RNS invoice copies run 10 years after the year of issue (Art. 145-VI-1). The scope includes registers, invoices issued and received, and any other document required by law.

At audit, documents missing during a verification are requested with 30 days to produce, extendable to the end of the check, and cannot first appear before the commissions (Art. 210). Where no accounts are presented, Art. 229 gives 15 days, then a fine notice and 15 more days, then assessment by default. Serious irregularities let DGI set the base itself: no Art. 145 accounting, no inventories, hidden purchases or sales, serious repeated errors, missing evidence, unrecorded or fictitious operations (Art. 213). With computerised books the check covers data, processing and system documentation (Art. 212).

## Boundary and exception table

| Situation | Result | Source |
|---|---|---|
| Over ceiling in one year only | Regime stands | Art. 39, 41, 43-4 |
| Over ceiling two consecutive years, CPU | RNR from 1 January following | Art. 41-II |
| RNS or RNR wants CPU or RNS | Turnover under the limit for three consecutive years | Art. 43-2, 43-3 |
| Two activities, two limits | Each activity within its limit, or total within the main activity's limit | Art. 43-1, 43-5 |
| RNS sale to a private individual | Art. 145-VI-1 invoice duty is for business customers | Art. 145-VI |
| CPU or AE and ICE | Art. 145-VIII does not bind them; a business customer's own Art. 146 needs still apply | Art. 145-XI, 146 |

## Worked cases

**Case 1. Freelance designer, AE.** MAD 150,000 collected, under the MAD 200,000 service limit. Art. 145 does not apply. She declares collected turnover under Art. 82 bis, holds an email address, and keeps her documents 10 years. No CGNC books are required by the CGI.

**Case 2. Neighbourhood shop, CPU.** Under MAD 2,000,000. Keeps purchase invoices in its name; those are what DGI asks for under Art. 210. No Art. 145 accounts.

**Case 3. IT consultant, CPU, over MAD 500,000 in 2024 and 2025.** RNR applies to income from 1 January 2026: Art. 145 accounting, inventories and full invoices. Recommend an expert-comptable.

**Case 4. Audit fines.** A company has 12 invoices without a correct ICE and did not keep records for 2 years.

```oa-check
name: ICE omissions and two years without retention
inputs:
  omissions: 12
  ice_fine: 100
  years: 2
  retention_fine: 50000
steps:
  - ice: omissions * ice_fine
  - retention: years * retention_fine
  - total: ice + retention
expected:
  total: 101200.00
```

**Case 5. Decision: take MAD 25,000 in cash or by transfer?** A company sells to a business for MAD 25,000. Cash means an Art. 193 fine on the seller of MAD 1,500. Bank transfer means none. Transfer wins by MAD 1,500.

```oa-check
name: Cash against transfer on MAD 25,000
inputs:
  amount: 25000
  rate: 0.06
steps:
  - cash_fine: amount * rate
  - transfer_fine: 0
  - saving: cash_fine - transfer_fine
expected:
  saving: 1500.00
```

## When to refuse or refer

Refer to a licensed Moroccan expert-comptable or comptable agree: a regime change, the RNS filing set, whether a merchant must keep 9-88 books, electronic archiving, and any VAT classification on an invoice (morocco-vat).

- Never state a go-live date or threshold for e-invoicing unless a published text gives it.
- Never tell a company or RNR taxpayer to skip Art. 145 accounting.
- Never tell an AE or CPU individual that Art. 145 binds them.
- Never confirm a business invoice as compliant if an Art. 145-III or VIII mention is missing.
- Never advise retention under 10 years.
- Never cite Art. 145 bis.
- Never compute the tax here.
- Never replace a licensed professional.

## Filing and payment

Bookkeeping feeds the returns. All businesses must file (Art. 155) and pay electronically on DGI's services from 1 January 2017, under regulatory terms. AE turnover goes to the designated body, monthly by the end of the following month or quarterly (Art. 82 bis). CPU files an annual return by 1 April, electronically or on paper (Art. 82 quater). Requests and certificates go through electronic teleservices (Art. 169 bis).

## Completion checklist

- Regime and two-year turnover test confirmed.
- Records match the Step 2 row.
- Sample invoices carry every Step 3 mention.
- Email address held.
- 10-year retention in place, electronic where required.
- Items on the Not yet confirmed line flagged.

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Code General des Impots 2026 (French), Art. 11, 20, 39, 41, 42 bis, 42 ter, 43, 82 bis, 82 quater, 118, 145, 146, 146 bis, 147, 155, 164, 169 bis, 185 bis, 191, 191 bis, 192, 193, 198 ter, 210 to 213, 229; these extracts read from a local text copy of the PDF | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |
| DGI home page; read for any e-invoicing notice, none shown | https://www.tax.gov.ma/wps/portal/DGI/Accueil | 2026-11-01 |
| ICE portal; page read, gives no digit count or legal basis | https://www.ice.gov.ma/ICE/ | 2026-11-01 |

Not yet confirmed: accounting law 9-88 and the Code de Commerce (official text could not be opened), so the old skill's rules that RNS must keep full CGNC accounts, the three commercial books, the plan comptable and the annual inventory under that law are out of the steps; the RNS reduced statements; an AE register of receipts and a CPU register of receipts and purchases and any official model (the CGI has neither, and Art. 145 bis is repealed; Loi 114-13 and regulations not read); ICE length and 9+4+2 structure; any annual cap on the ICE fine (Art. 198 ter states none); the wording "TVA non applicable" for AE and CPU invoices; the e-invoicing clearance model, UBL 2.1 and CII formats, phasing from large firms to SMEs and B2C, the free tool at fatourati.gov.ma, e-archiving rules, and whether the implementing decree is published (press only: under review in April 2026, no decree found on 1 November 2026); what Finance Law 50-25 changed in Art. 145-I and X; the regulatory criteria for electronic accounting; SIMPL-IR, SIMPL-TVA, SIMPL-IS portal steps, adhesion and data import; the AE filing channel; the body named under Art. 82 bis.

Removed and why: Secondary commentary list (not a permitted citation). Contributor, quality tier and last research rows (metadata). Conservative default that a near ceiling counts as breached (Art. 41 tests two actual years). Everything else is carried above or on the Not yet confirmed line.

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
