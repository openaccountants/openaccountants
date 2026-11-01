---
name: ma-einvoice
description: >
  Use this skill whenever asked about Morocco e-invoicing, the system informatique de facturation
  under CGI Art. 145-IX, or invoice-conformity rules for tax year 2026. Covers who must hold a
  compliant invoicing system, the mandatory invoice mentions (identity, IF, TP, ICE, continuous
  numbering, VAT shown separately), the carve-out for CPU and auto-entrepreneur taxpayers, the
  ticket de caisse, retention, the deduction consequence of a bad invoice under Art. 146, and
  the penalties in force. Keeps press reports on the roadmap, platform and formats apart from the
  law. Trigger on phrases like "Morocco e-invoicing", "facturation electronique Maroc", "e-facture
  DGI", "facture electronique obligatoire", "mentions obligatoires facture Maroc", "ICE sur
  facture", "CGI 145-IX", "فاتورة إلكترونية المغرب". Applies to businesses and professionals in
  Morocco. Replies in the user's language: English, French or Darija. Cross-reference morocco-vat,
  ma-auto-entrepreneur, ma-cpu and ma-bookkeeping.
version: 1.1
jurisdiction: MA
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Morocco e-invoicing v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

Loads on top of `income-tax-workflow-base`. It tells the AI what a Moroccan invoice must carry today, who falls under the invoicing-system duty of CGI Art. 145-IX, and what the law does not yet settle. Tax year 2026. Law: Code General des Impots (CGI), 2026 edition, as amended by Finance Law 50-25. Authority: Direction Generale des Impots (DGI). Currency: MAD. The output is a conformity check and a brief for the reviewer, not a filing.

Keep the native terms (DGI, ICE, IF, TP, TVA, HT, TTC, SIMPL) and explain them once. HT is hors taxe, TTC is toutes taxes comprises, TVA is VAT.

**Read this first.** Art. 145-IX is in the code, but it leaves the technical criteria to the administration and the application rules to regulation, by sector. No go-live date, wave, turnover cut-off, format, platform or e-invoicing penalty appears in the CGI 2026. Do not tell a user they must e-invoice from a date. Check the Bulletin Officiel and the DGI decrees page first: we could not read either for this version, and press reports up to October 2026 report no published decree.

## Scope statement

In scope: invoice content (Art. 145-III to VIII), the system duty (Art. 145-IX), the carve-out (Art. 145-XI), deduction (Art. 146), retention (Art. 211), penalties.

Out of scope: VAT rates and returns (`morocco-vat`), the auto-entrepreneur regime (`ma-auto-entrepreneur`), the CPU regime (`ma-cpu`), the books (`ma-bookkeeping`), professional income (`morocco-professional-income-tax`).

## Filing requirements

- **System duty (Art. 145-IX):** taxpayers subject to corporate tax, taxpayers on professional income under the real net result or simplified net result, and those liable to VAT must have an invoicing system that meets the administration's technical criteria, in line with Art. 145-III and IV. Application rules are set by regulation, sector by sector.
- **Out of Art. 145 (Art. 145-XI):** individuals taxed under the CPU or the auto-entrepreneur regime. Only the Art. 145-X email duty applies to them. Their purchases still need Art. 146 invoices if they are on the CPU (Art. 146 bis).
- **Business buyers (Art. 146):** every purchase from a supplier subject to TP needs a regular invoice in the buyer's name with the Art. 145-III and VIII indications. A business client can therefore ask an auto-entrepreneur or CPU supplier for those indications even though Art. 145 itself does not bind that supplier.
- **Simplified net result (Art. 145-VI):** invoices go to buyers who are subject to corporate tax, VAT or professional income tax and act in the course of their business; keep the copies for ten years after the year they were issued.
- **Email (Art. 145-X):** every taxpayer holds an email address of their choice.
- **Electronic returns (Art. 155-I):** all businesses file by electronic means from 1 January 2017, under regulatory terms. Art. 145-I also requires the accounts in electronic format under the rules in force.

### Mandatory mentions (Art. 145-III)

Pre-numbered from a continuous series, or issued by a computer system in a continuous series, with the usual commercial details and:

1. the seller's identity;
2. the tax identification number (IF) from the local tax office and the TP article number;
3. the date of the operation;
4. the buyer's name or company name, address and ICE;
5. price, quantity and nature of goods, works or services;
6. VAT shown separately, whether charged on top or included. For Art. 91, 92 and 94 operations, show the exemption or suspensive regime instead;
7. references and method of payment;
8. anything else the law prescribes.

The seller's ICE goes on invoices and every tax return (Art. 145-VIII). Non-traders put the IF and TP number on all documents to clients or third parties (Art. 145-VII).

Clinics state the total fees and split them between clinic and doctors (Art. 145-IV). Touring sellers show the client's TP roll number, unless they file the sales statement by client of Art. 20-I or 82-I (Art. 145-V).

**Ticket de caisse:** on sales of goods by a business to private individuals it can replace the invoice. It shows at least the date, seller, product or service, quantity and price, with VAT where relevant (Art. 145-III).

## Rates and thresholds

All rows: tax year 2026.

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Omitted or wrong ICE | MAD 100 per omission or inaccuracy | Art. 145-VIII breach. The code states no annual cap | [CGI Art. 198 ter](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Accounts or supporting documents not produced | MAD 2,000; MAD 500 to 2,000 for income tax | Art. 145 and 146 documents, or refusal of audit. Plus MAD 100 a day late, to MAD 1,000 | [CGI Art. 191-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Electronic records not produced at audit | MAD 50,000 per year | Taxpayers keeping electronic books under Art. 210, third paragraph | [CGI Art. 191 bis](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Fictitious invoices, or repeated sales without invoices | MAD 5,000 to 50,000, plus 1 to 3 months in prison | Intent to evade tax or obtain undue deductions or refunds, for oneself or another. Procedure of Art. 231 | [CGI Art. 192-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Retention of invoice copies and supporting documents | 10 years | Electronic support where books are electronic | [CGI Art. 211](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| VAT rates shown on invoices | 20% and 10% | See `morocco-vat` for what falls where | [CGI Art. 99](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| E-invoicing penalty | unverified: none in the CGI 2026 | Do not state an amount | unverified |

## Computation rules

This skill states rules and status; arithmetic goes to the engine. Run the check in order:

1. Identify the regime: corporate tax, real, simplified, CPU, auto-entrepreneur, and VAT status.
2. If CPU or auto-entrepreneur, Art. 145 does not bind the seller. Go to step 5.
3. Check the invoice against each mention above and the continuous series.
4. Confirm Art. 145-IX status from the Bulletin Officiel and the DGI before saying anything on the system duty.
5. For a purchase, test Art. 146: real purchase, regular invoice in the buyer's name, Art. 145-III and VIII indications. For VAT also see `morocco-vat` (Art. 106).
6. Report the defects and reissue a correct invoice.

## Edge cases and special rules

- **Bad invoice, lost deduction:** purchases not supported by an invoice are outside VAT deduction (Art. 106) and fail Art. 146. Conformity of the invoice protects the buyer's deduction, which often costs more than the fine.
- **Failed supplier:** no deduction where the invoice comes from a supplier that does not meet its filing and payment duties and has no real activity. The DGI publishes a list of such tax numbers after a final judgment. Same for an inactive company under Art. 228 bis (Art. 146).
- **VAT shown wrongly:** anyone who shows VAT on an invoice owes it, simply because it was invoiced (Art. 119-II). An exempt seller must not show it.
- **Exemptions need the ICE:** an exemption under the code needs an ICE and compliance with filing and payment duties (Art. 164-I).
- **Vendor claims:** software sold as "DGI 2026 certified" has no standing we could trace to a published criterion. Ask for the DGI text it relies on.
- **Client asks about a fake invoice:** Art. 192 applies. Refer it.
- **What to do now:** obtain the ICE and print it on every invoice; fix Art. 145 conformity first, the baseline under any later text; use a tool that keeps an unbroken series and can export structured data, not loose Word or Excel files; keep SIMPL credentials, email and payment mandate working; watch the Bulletin Officiel and tax.gov.ma.
- **Go-live decisions:** platform onboarding, provider choice or workflow change waits for the published text and an expert-comptable.

## Self-checks

- Regime identified before any rule is applied.
- Every mention tested against Art. 145-III and VIII.
- CPU and auto-entrepreneur sellers not told Art. 145 binds them.
- No date, wave, cut-off, platform name, format or e-invoicing penalty stated as law.
- Output matches the base skill spec.

Test questions: "When is e-invoicing mandatory for me?" gives no date, and says the text setting it could not be confirmed. "Is fatourati.gov.ma official?" is not asserted. "I forgot my client's ICE" gives MAD 100 per omission (Art. 198 ter), the buyer's Art. 146 risk, and reissue. "UBL or CII?" is unconfirmed. "Does this apply to my auto-entrepreneur business?" gives Art. 145-XI, and the email duty and client's Art. 146 needs.

Never assert an unconfirmed date, model, platform or threshold. Never accept a VAT-registered seller's invoice without IF and ICE as conforming. Never tell a user to onboard to a clearance platform before the text is published.

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Code General des Impots 2026 (French), Art. 99, 106, 119, 145, 146, 146 bis, 155, 164, 191, 191 bis, 192, 198 ter, 211; those articles read in a local text copy of the DGI PDF | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |
| DGI home page; read for news, no e-invoicing item shown. The decrees page redirected to the home page and was not read | https://www.tax.gov.ma/wps/portal/DGI/Accueil | 2026-11-01 |

Not yet confirmed: whether the Art. 145-IX decree or technical criteria are published (the Bulletin Officiel issue list and DGI decrees page could not be read; press reports to October 2026 report a draft at the Secretariat General du Gouvernement); the old skill's roadmap, all from secondary sources: clearance or CTC model, UBL 2.1 or CII formats, a national platform by xHub linked to Simpl-TVA, the name fatourati.gov.ma, waves from large B2B to SMEs, small firms and B2C, freelancers falling in later waves, future e-invoicing sanctions; ICE length of 15 digits; ICE start dates of 2016 for sellers and January 2019 for B2B clients; whether the buyer's ICE is needed for a private client (Art. 145-III-4 has no B2B limit in its words); the RC number on invoices (not listed in Art. 145); the SIMPL address portail.tax.gov.ma; invoice-sanction range of MAD 2,000 to 50,000 once given under Art. 146 and an ICE cap of about MAD 5,000, neither found in the CGI 2026, so both are removed from the rates.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
