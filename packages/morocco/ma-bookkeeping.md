---
name: ma-bookkeeping
description: Use this skill whenever asked about record-keeping, bookkeeping, or invoicing obligations for self-employed people and micro-businesses in Morocco — which books or registers each tax regime must keep, what must appear on an invoice, the ICE identifier, the move toward e-invoicing, document retention, and when a taxpayer must move up to full accounting. Trigger on phrases like "Morocco bookkeeping", "comptabilité Maroc", "facture ICE", "e-invoicing Morocco", "facturation électronique Maroc", "registre des recettes", "tenue de comptabilité Maroc", "mentions obligatoires facture", "محاسبة المغرب", "فاتورة ICE". Covers the auto-entrepreneur receipts register, the CPU register of receipts and purchases, RNS / RNR full accounting under the CGNC and Code de Commerce, mandatory invoice mentions, the DGI e-invoicing roadmap, the SIMPL teleservices, and the 10-year retention rule. Reply in the user's language (English, French, or Moroccan Arabic / Darija). Cross-reference ma-auto-entrepreneur, ma-cpu, and ma-income-tax for the tax computation.
version: 1.0
jurisdiction: MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Bookkeeping

## Morocco — Record-Keeping & Bookkeeping for the Self-Employed (Comptabilité)

This skill tells an AI agent what books, registers, and invoices a self-employed Moroccan taxpayer must keep, and for how long — organised by tax regime. It does not compute the tax (that is ma-auto-entrepreneur, ma-cpu, and ma-income-tax); it governs the underlying comptabilité and facturation.

The depth of obligation rises with the regime:

- Auto-entrepreneur (AE) — a simple register of receipts (registre des recettes); no double-entry accounting.
- Contribution Professionnelle Unique (CPU) — a register of receipts and purchases (registre des recettes et des achats), with supporting purchase vouchers; exempt from full accounting.
- Résultat Net Simplifié (RNS) / Résultat Net Réel (RNR) — full accounting (comptabilité régulière) under the Code Général de Normalisation Comptable (CGNC) and the Code de Commerce.

This skill replies in the user's language. Moroccan users mix English, French, and Darija — keep the native terms (comptabilité, CGNC, facture, ICE, registre, DGI, SIMPL) and explain them in the user's chosen language.

## 1. Quick Reference

**Quick Reference Table**

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Scope | Record-keeping, registers, invoicing, retention by regime |
| Currency | MAD (dirham marocain, DH) |
| Authority | **Direction Générale des Impôts (DGI)** — tax.gov.ma |
| AE records | **Register of receipts** (registre des recettes) — receipts only, no expenses |
| CPU records | **Register of receipts and purchases** + purchase vouchers (CGI Art. 145 bis) *(verify model/format set by regulation)* |
| RNS / RNR records | **Full accounting** under the **CGNC** + Code de Commerce (livre-journal, grand-livre, livre d'inventaire) |
| Trigger to full accounts | Turnover exceeds the CPU/RNS ceiling for **2 consecutive years**, or option for RNR/RNS, or company form *(verify thresholds below)* |
| Mandatory invoice ID | **ICE** — Identifiant Commun de l'Entreprise, **15 digits** *(verify length 9+4+2)* |
| Invoice legal basis | **CGI Art. 145** (mandatory mentions) *(verify article)* |
| E-invoicing (facturation électronique) | Legal basis **CGI Art. 145-IX**; **CTC / pre-clearance** model via DGI platform; **implementing decree not yet published as of April 2026 — dates and thresholds pending** *(verify on publication)* |
| Free e-invoice tool (small businesses) | `fatourati.gov.ma` *(verify)* |
| Teleservices | **SIMPL** (SIMPL-IR, SIMPL-TVA, SIMPL-IS) on tax.gov.ma; e-filing/e-payment mandatory since **1 Jan 2017** *(verify)* |
| Retention period | **10 years** — accounting records & supporting documents (CGI Art. 211) *(verify)* |
| Retention penalty | Fixed fine **MAD 50,000 per fiscal year** for failure to retain *(verify amount)* |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Moroccan accountant (expert-comptable)** |
| Version | 1.0 |
| Last research update | May 2026 |

### Conservative defaults

- **Regime unknown** — Assume the taxpayer must keep the higher standard (register of receipts and purchases, retain everything 10 years) until the regime is confirmed.
- **Turnover near a ceiling** — Assume the ceiling is breached and warn that full accounting under the CGNC may become mandatory next year.
- **Invoice missing the client ICE (B2B)** — Treat the invoice as non-compliant; warn that the buyer may lose deductibility of the charge and VAT.
- **E-invoicing dates** — Never state a firm go-live date for a category; say the implementing decree is pending and the user must verify with the DGI.
- **Any figure marked (verify)** — Present as provisional; the reviewer confirms against the current CGI / Loi de Finances 2026 before relying on it.

## 2. Records by Regime

**Records by Regime Table**

| Regime | Core records required | Double-entry? | Legal frame |
| --- | --- | --- | --- |
| **Auto-entrepreneur (AE)** | Register of receipts (registre des recettes), invoices issued | No | Loi 114-13; CGI |
| **CPU** | Register of receipts **and** purchases + purchase vouchers | No | CGI Art. 145 bis *(verify)* |
| **RNS** | Full accounting (simplified presentation of statements) | Yes | CGNC; Code de Commerce |
| **RNR** | Full accounting (complete financial statements) | Yes | CGNC; Code de Commerce |

### 2.1 Auto-entrepreneur — register of receipts (registre des recettes)

- Keep a chronological register of receipts (turnover collected, day by day).
- No expense deduction — the impôt libératoire is on gross collected turnover, so there is no obligation to book purchases for tax.
- Still issue invoices / receipts to clients and keep copies; the ICE applies (see §3).
- No livre-journal, grand-livre, balance sheet, or income statement.

### 2.2 CPU — register of receipts and purchases (registre des recettes et des achats)

- **CPU register content** — Keep a register recording, day by day, both: sums collected from sales, works, and services; and sums paid for purchases, supported by probative vouchers (pièces justificatives probantes).  _(CGI Art. 145 bis (verify article))_

- The model of the register and the recording rules are set by regulation (voie réglementaire) — confirm the current official form *(verify)*.
- CPU taxpayers are exempt from the full accounting of CGI Art. 145, but the register and the duty to justify purchases remain.
- No double-entry accounting, balance sheet, or CGNC financial statements.

### 2.3 RNS / RNR — full accounting under the CGNC

- **RNS/RNR accounting requirements** — Taxpayers under Résultat Net Simplifié (RNS) or Résultat Net Réel (RNR) must keep a régulière comptabilité under the CGNC (made mandatory by the accounting law, Loi 9-88, dahir 25 Dec 1992) and the Code de Commerce: Livre-journal (general journal) — entries recorded day by day; Grand-livre (general ledger) — postings by account; Livre d'inventaire (inventory book) — balance sheet and income statement of each year transcribed; Supporting auxiliary journals and ledgers as the size of the business needs; A plan comptable conforming to the CGNC; an annual inventory.  _(Loi 9-88; CGNC; Code de Commerce)_
- **Difference between RNR and RNS** — RNR — complete financial statements and full accounting entries. RNS — same accounting foundation but a simplified presentation of the annual statements (abbreviated balance sheet / income statement) *(verify the exact reduced filing set against the current CGI)*.

An expert-comptable or comptable agréé is typically engaged for RNS/RNR; the agent prepares and organises but does not substitute for the professional.

## 3. Invoicing Rules (ICE, Mandatory Mentions, E-Invoicing Roadmap)

- **Invoicing rules section intro** — Section header only; content in subsections 3.1-3.3.

### 3.1 The ICE — Identifiant Commun de l'Entreprise

- **ICE digit structure** — 15-digit identifier (commonly 9 enterprise + 4 establishment + 2 control key) digits ((verify structure))
- **ICE mandatory scope** — Mandatory for the seller and, in B2B, for the client as well.
- **Consequence of missing/invalid ICE** — A missing or invalid ICE can cost the buyer the deductibility of the charge (IS/IR) and of the related VAT, and exposes the seller to a fine (reported as MAD 100 per omission, capped per fiscal year) *(verify amounts and article)*.

### 3.2 Mandatory mentions on an invoice (facture)

- **Mandatory invoice mentions list** — A compliant facture under CGI Art. 145 generally carries *(verify the full official list against the current CGI)*: 1. Seller identity — name / raison sociale, address, IF (identifiant fiscal), taxe professionnelle (TP), RC (registre de commerce) where applicable, and ICE. 2. Client identity — name, address, and ICE in B2B. 3. A sequential invoice number (numérotation chronologique et continue). 4. Date of issue. 5. Description, quantity, unit price of goods/services. 6. Price excl. VAT, VAT rate and amount, price incl. VAT (HT / TVA / TTC), or the exemption / non-applicability mention where relevant. 7. Payment terms and any other regulated mention.  _(CGI Art. 145)_

Auto-entrepreneurs and CPU taxpayers who are outside VAT still issue invoices but mark them accordingly (e.g. "TVA non applicable") *(verify the correct wording and VAT status against ma-auto-entrepreneur / morocco-vat)*.

### 3.3 E-invoicing roadmap (facturation électronique) — STATUS PENDING

- **E-invoicing legal basis** — Legal basis — CGI Art. 145-IX *(verify)*.  _(CGI Art. 145-IX)_
- **E-invoicing model** — Model — a clearance / CTC (Continuous Transaction Controls) system: invoices are pre-validated by the DGI platform before they reach the client *(verify)*.
- **E-invoicing formats** — Formats — structured XML (UBL 2.1 and CII); a plain PDF is not sufficient *(verify)*.
- **E-invoicing phasing** — Phasing — expected to start with large enterprises (B2B), then extend to SMEs / TPEs and finally B2C.
- **Critical status of decree** — As of April 2026 the implementing decree was not yet published — so the exact go-live dates, the category calendar, and the turnover thresholds are NOT confirmed. Do not state a firm date for any taxpayer category. Tell the user the decree is pending and to verify with the DGI *(verify on publication of the décret / Loi de Finances texts)*.

### 4.1 Document retention — 10 years

- **Retention obligation** — Taxpayers subject to IS, IR, or TVA must keep all accounting documents and supporting documents used to determine the tax base for 10 years.  _(CGI Art. 211 (verify))_
- **Scope of retained documents** — This covers the registers (AE, CPU), the CGNC books (RNS/RNR), invoices issued and received, purchase vouchers, bank statements, and contracts.
- **Retention penalty** — Reported penalty for failure to retain: a fixed fine of MAD 50,000 per fiscal year *(verify amount and article)*.
- **Audit-ready form** — Keep records in a form that can be produced on tax audit (contrôle fiscal); for e-invoiced documents, retain the structured electronic original *(verify e-archiving rules once the decree publishes)*.

### 4.2 SIMPL teleservices (tax.gov.ma)

SIMPL is the DGI's online portal for télédéclaration and télépaiement: SIMPL-IR (income tax), SIMPL-TVA (VAT), SIMPL-IS (corporate tax). E-filing and e-payment have been mandatory since 1 January 2017 *(verify)*. The taxpayer adheres (adhésion) to obtain access codes; the portal lets users import accounting data to generate and file returns. Bookkeeping feeds SIMPL: the registers/accounts produce the figures that are télédéclarés. Auto-entrepreneurs file via the dedicated AE channel (see ma-auto-entrepreneur), not necessarily the general SIMPL flow *(verify)*.

## 5. Worked Examples

### Example 1 — Freelance graphic designer, auto-entrepreneur

Activity: design services; turnover collected ≈ MAD 150,000/year (below the services ceiling).
Records: a register of receipts only (date, client, amount collected). Issues invoices marked "TVA non applicable" with her ICE and IF; keeps copies. No purchase register required for tax, no CGNC accounts.
Retention: keep the register and invoice copies 10 years.
Agent output: confirms AE register suffices; flags that if turnover exceeds the ceiling for two consecutive years she moves up a regime (verify ceiling in ma-auto-entrepreneur).

### Example 2 — Small retailer under CPU

Activity: neighbourhood shop (commercial); under the CPU ceiling.
Records: a register of receipts and purchases recording sales collected and purchases paid day by day, with purchase vouchers retained (CGI Art. 145 bis). Exempt from CGNC full accounting.
Issues invoices/tickets with ICE; in B2B sales must also carry the client's ICE.
Retention: register + vouchers + invoices 10 years.
Agent output: confirms register + purchase justification; warns that missing purchase vouchers undermine the regime and that breaching the ceiling two years running triggers RNS/RNR full accounts *(verify thresholds)*.

### Example 3 — Consultant who exceeded the ceiling → RNR

Activity: IT consultant; turnover exceeded the service ceiling for two consecutive years, now under RNR.
Records: must now keep full accounting under the CGNC — livre-journal, grand-livre, livre d'inventaire, a CGNC-compliant plan comptable, annual inventory, and complete financial statements; compliant invoices with ICE.
Files via SIMPL-IR (and SIMPL-TVA if VAT-registered).
Retention: all books and supporting documents 10 years.
Agent output: flags the upgrade trigger, recommends engaging an expert-comptable, and prepares the books for the professional to review and sign off.

## 6. Tier 2 — Reviewer Judgement Required

Escalate to the human expert-comptable / comptable agréé (do not auto-decide):

- Which regime applies and whether a ceiling was breached for two consecutive years — the trigger that forces CGNC full accounting.
- The exact RNS reduced filing set vs full RNR statements.
- The official CPU register model and acceptable purchase vouchers.
- The exact, current ICE structure, invoice-mention list, and penalty amounts — confirm against the live CGI / Loi de Finances 2026.
- E-invoicing applicability and dates — pending the implementing decree; never commit a taxpayer to a go-live date without DGI confirmation.
- E-archiving of electronic invoices and the audit-readiness of digital records.
- Any VAT classification on invoices — defer to morocco-vat.

### Legal & source references

- CGI (Code Général des Impôts) — Art. 145 (tenue de comptabilité / facture mentions), 145 bis (register for forfait/CPU purchases), 145-IX (e-invoicing basis), 211 (retention) — all article numbers to verify against the current consolidated CGI and Loi de Finances 2026.
- CGNC (Code Général de Normalisation Comptable) — accounting law Loi 9-88, dahir 25 Dec 1992 (livre-journal, grand-livre, livre d'inventaire).
- Code de Commerce — commercial books and registre de commerce.
- Loi 114-13 — auto-entrepreneur status (see ma-auto-entrepreneur).
- DGI — tax.gov.ma; SIMPL teleservices; e-invoicing platform (fatourati.gov.ma) *(verify)*.
- Secondary commentary (PwC Morocco, Upsilon, Baker Tilly, Deloitte LF 2026) used for cross-checking — not primary authority.

### Short test suite

1. "I'm an auto-entrepreneur — what do I need to keep?" → register of receipts + invoice copies; no CGNC accounts; retain 10 years.
2. "CPU shopkeeper — do I need full accounting?" → no; register of receipts and purchases + vouchers (Art. 145 bis); exempt from CGNC full accounts.
3. "When am I forced into full accounting?" → broadly, when the CPU/RNS ceiling is exceeded two consecutive years, or on option/company form → CGNC books (verify thresholds).
4. "What must be on my invoice?" → CGI Art. 145 mentions incl. ICE (seller + B2B client), sequential number, date, HT/TVA/TTC.
5. "Is e-invoicing mandatory now?" → moving to mandatory CTC e-invoicing under CGI Art. 145-IX, but the implementing decree is pending (April 2026) — dates and thresholds not confirmed; verify with DGI.
6. "How long do I keep records?" → 10 years (CGI Art. 211).
7. "What is SIMPL?" → DGI teleservices (SIMPL-IR/TVA/IS) for télédéclaration and télépaiement; e-filing mandatory since 2017.

## PROHIBITIONS

- **Prohibitions list** — - Do NOT state a firm e-invoicing go-live date or category threshold — the implementing decree was unpublished as of April 2026; say it is pending and direct the user to the DGI. - Do NOT tell an RNS/RNR taxpayer they may skip CGNC double-entry accounting. - Do NOT tell an auto-entrepreneur they must keep CGNC books, a balance sheet, or a purchase ledger for tax — the AE keeps a register of receipts only. - Do NOT confirm an invoice as compliant if the ICE (seller, or B2B client) is missing or invalid. - Do NOT advise retention shorter than 10 years. - Do NOT quote ICE structure, invoice-mention lists, penalty amounts, or thresholds as settled — present items marked (verify) as provisional pending reviewer confirmation against the current CGI / Loi de Finances 2026. - Do NOT compute the tax itself here — defer to ma-auto-entrepreneur, ma-cpu, ma-income-tax, and morocco-vat. - Do NOT replace a licensed Moroccan expert-comptable / comptable agréé.

## Disclaimer

This skill is research-verified from public sources (DGI / tax.gov.ma, the CGNC, the CGI, the Code de Commerce, the Loi de Finances 2026, and reputable professional commentary) and is pending sign-off by a licensed Moroccan expert-comptable. It is general information, not accounting or tax advice, and does not create a professional engagement. Figures, article numbers, thresholds, penalty amounts, and especially the e-invoicing roadmap change with each Loi de Finances and implementing decree — every item marked (verify) must be confirmed against current DGI texts before reliance. Always have a licensed Moroccan expert-comptable or the DGI review before filing or relying on this output. Part of openaccountants.com — open-source tax skills for the self-employed.

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
