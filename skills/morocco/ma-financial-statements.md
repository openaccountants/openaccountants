---
name: ma-financial-statements
description: "Use this skill whenever asked about financial statements, statutory accounts, or financial reporting obligations for self-employed people and small businesses in Morocco for tax year 2026: who has to prepare formal accounts and who does not, the etats de synthese (Bilan, CPC, ESG, Tableau de financement, ETIC), how accounts go to the DGI with the return, deposit at the court registry (depot legal), and when a statutory auditor (commissaire aux comptes) is required. Trigger on phrases like \"Morocco financial statements\", \"états de synthèse\", \"bilan CPC Maroc\", \"do I file accounts Morocco\", \"comptes annuels Maroc\", \"CGNC états de synthèse\", \"tableau de financement\", \"ETIC\", \"commissaire aux comptes Maroc\", \"dépôt des comptes Maroc\", \"القوائم المالية المغرب\", \"الميزانية المغرب\". Auto-entrepreneur and CPU taxpayers fall outside CGI Art. 145; RNS keeps the Art. 145-VI registers; RNR taxpayers and companies keep accounts under Art. 145-I. Reply in the user's language (English, French, or Moroccan Arabic / Darija). Cross-reference ma-bookkeeping, morocco-professional-income-tax, ma-cpu, and ma-auto-entrepreneur."
version: 1.1
jurisdiction: MA
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Financial Statements v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. Law: Code General des Impots (CGI), 2026 edition; Law 17-95 (SA); Law 5-96 (SARL and other companies). Currency: MAD.

## What this file is

This skill tells an AI agent who has to prepare formal financial statements in Morocco, what those statements are, and how they are filed, by tax regime and legal form. It loads on top of `income-tax-workflow-base`. It does not compute tax (`morocco-professional-income-tax`, `ma-cpu`, `ma-auto-entrepreneur`) and does not govern day-to-day books and invoices (`ma-bookkeeping`). It governs the output: the etats de synthese. The reviewer is the customer: the skill produces a working paper and a brief, not a filing.

Reply in the user's language. Moroccan users mix English, French and Darija; keep the native terms (CGNC, etats de synthese, bilan, CPC, ESG, tableau de financement, ETIC, commissaire aux comptes, depot legal, DGI) and explain them.

## Scope statement

Covered: auto-entrepreneur (AE), contribution professionnelle unique (CPU), resultat net simplifie (RNS), resultat net reel (RNR), and commercial companies (SARL, SA, SNC, SCS, SCA). Out of scope: tax computation, invoice rules, and bank, insurer or listed-group consolidated reporting, which go to a licensed Moroccan professional.

| Taxpayer | Tax code requirement | Output |
|---|---|---|
| AE | CGI Art. 145 does not apply (Art. 145-XI) | No bilan or CPC under the CGI; records go to `ma-bookkeeping` |
| CPU | CGI Art. 145 does not apply (Art. 145-XI) | No bilan or CPC under the CGI; records go to `ma-bookkeeping` |
| RNS | Registers, year-end lists, stock inventories, depreciation register (Art. 145-VI) | Result under Art. 38-II with the bridge to the tax result; closes 31 December (Art. 38-I) |
| RNR | Accounts under the law in force, in electronic format (Art. 145-I), year-end inventories (Art. 145-II) | Accounts and annexes with the IR return (Art. 82-I) |
| Company | Same (Art. 145-I), taxed or exempt (Art. 20-I) | Etats de synthese, IS return annexes, court deposit, audit if triggered |

Do not tell an RNS taxpayer the old line that a fixed "reduced set" of statements applies: the CGI sets registers and lists, and any commercial-law duty for a trader under Law 9-88 goes to the reviewer.

### What changes as a self-employed person grows

1. **AE.** Turnover collected up to MAD 500,000 (commercial, industrial, craft) or MAD 200,000 (services) (Art. 42 ter). No bilan, no CPC.
2. **CPU.** Turnover up to MAD 2,000,000 or MAD 500,000 (Art. 41-II). Still no bilan under the CGI.
3. **RNR.** Applies if the CPU limits are passed for two consecutive years, from 1 January of the following year (Art. 41-II), and to an AE in the same position unless RNS or CPU is chosen (Art. 43-4). Accounts now go with the IR return.
4. **Company.** Etats de synthese, IS return, court deposit, and an auditor if it is an SA or passes the turnover test. Incorporation is not freelancing with a logo: it brings deposited accounts and possibly audit, all absent for AE and CPU.

## Filing requirements

| Who | What | Deadline | Source |
|---|---|---|---|
| Company | Tax result return with annexes and sales statement by client | Within 3 months of year end | CGI Art. 20-I |
| Nil or loss-making company | Explanatory statement with the return; MAD 2,000 fine if still missing 15 days after a letter | With the return | CGI Art. 20-IV, 198 bis |
| RNR or RNS individual | Annual income return | Before 1 May | CGI Art. 82-I |
| Nil or loss-making RNR or RNS | Explanatory statement | With the return | CGI Art. 82-IV |
| SARL | Accounts approved by the members | Within 6 months of year end | Law 5-96 Art. 70 |
| SA | Ordinary general meeting; one extension by court order | Within 6 months of year end | Law 17-95 Art. 115 |
| SA | Two copies of the etats de synthese and the auditor's report to the court registry; electronic deposit allowed | Within 2 months of approval | Law 17-95 Art. 158 |
| SARL, SNC, SCS, SCA | Two copies of the etats de synthese and any auditor's report to the court registry | Within 30 days of approval | Law 5-96 Art. 95 |
| All taxpayers | Keep accounting documents | 10 years; electronically if accounts must be electronic | CGI Art. 211 |

E-filing with the DGI: Art. 155 governs electronic returns. SIMPL screens were not read; see Not yet confirmed.

## Rates and thresholds

| Item | Amount | Source | URL |
|---|---|---|---|
| RNS exit limit, commercial | MAD 2,000,000 | CGI Art. 39 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| RNS exit limit, services | MAD 500,000 | CGI Art. 39 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Auditor, SARL | Turnover above MAD 50,000,000 excluding taxes at a year end | Law 5-96 Art. 80 | http://web.archive.org/web/20200222125632/http://adala.justice.gov.ma:80/production/html/fr/69028.htm |
| Auditor, SNC and SCS | Turnover above MAD 50,000,000 excluding taxes at year end | Law 5-96 Art. 12, 21 | http://web.archive.org/web/20200222125632/http://adala.justice.gov.ma:80/production/html/fr/69028.htm |
| Late filing surcharge | 5% up to 30 days; 15% after; 20% on assessment | CGI Art. 184 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Missing deposit, SARL managers | MAD 10,000 to 50,000 | Law 5-96 Art. 108 | http://web.archive.org/web/20200222125632/http://adala.justice.gov.ma:80/production/html/fr/69028.htm |
| Missing deposit, SA directors | MAD 10,000 to 50,000; extra 2 months with MAD 5,000 late penalty | Law 17-95 Art. 420 | https://www.ammc.ma/sites/default/files/Loi%20n%C2%B0%2017-95.pdf |
| No etats de synthese, SARL managers | MAD 2,000 to 40,000 | Law 5-96 Art. 109 | http://web.archive.org/web/20200222125632/http://adala.justice.gov.ma:80/production/html/fr/69028.htm |
| No etats de synthese, SA directors | MAD 20,000 to 200,000 | Law 17-95 Art. 386 | https://www.ammc.ma/sites/default/files/Loi%20n%C2%B0%2017-95.pdf |

## Computation rules

1. Identify the regime and legal form. If unknown, assume accounts are required until AE or CPU status is confirmed (CGI Art. 145-XI). Never call someone exempt on a guess.
2. AE or CPU confirmed: say no bilan or CPC is required by the CGI, and route records to `ma-bookkeeping`.
3. RNS: list the Art. 145-VI items: registers of receipts and payments, third-party list, stock inventory, depreciation register.
4. RNR or company: prepare the statements below for the return annexes (Art. 20-I, 82-I).
5. Company: compute the deadlines from year end and from approval, using the Filing table.
6. Test audit: SA always (Law 17-95 Art. 159); SA calling on public savings, banks, credit, investment, insurance, capitalisation and savings companies at least two auditors; SCA always (Law 5-96 Art. 34); SARL, SNC and SCS on the turnover line (SCS through Art. 21). Turnover near MAD 50,000,000: warn the user to line up an auditor.

### The statements

The official model 100/IS/N annex set (normal accounting model), as filed by a Moroccan issuer on the AMMC site, carries the ESG and the Tableau de financement alongside the bilan and CPC. CGI Art. 82-I names the bilan, the compte de produits et charges and the etat des informations complementaires for participation companies.

- **Bilan:** position at the closing date, assets against equity and liabilities, with actif immobilise, actif circulant and tresorerie-actif on one side and financement permanent, passif circulant and tresorerie-passif on the other.
- **CPC (compte de produits et charges):** revenue and charges for the year, split into exploitation, financier and non courant, ending in the net result.
- **ESG (etat des soldes de gestion):** how the net result forms, and the capacite d'autofinancement (CAF).
- **Tableau de financement:** resources and uses over the year.
- **ETIC (etat des informations complementaires):** notes that explain the bilan and CPC, such as methods, fixed assets and depreciation, debts, provisions and commitments.

The turnover line and content of the simplified model were not confirmed. Until they are, prepare the normal model and flag it. The statements are approved by members or shareholders, and the SA auditor certifies them as regular and fair (Law 17-95 Art. 175).

## Edge cases and special rules

- **Auditor v accountant:** the commissaire aux comptes certifies; the expert-comptable prepares or reviews. An auditor must be on the roll of the Ordre des Experts-Comptables (Law 17-95 Art. 160).
- **Term:** three financial years (Law 17-95 Art. 163). A company calling on public savings cannot keep the same auditor certifying for more than 12 years (Art. 163 as amended by Law 19-20).
- **Failure to appoint in an SA:** directors face one to six months' prison and MAD 10,000 to 50,000 fine, or either (Law 17-95 Art. 403).
- **SARL below the line:** members may appoint an auditor; holders of at least a quarter of the capital may ask the court president to order one (Law 5-96 Art. 80). The old one-tenth figure was wrong.
- **SNC below the line:** one member may ask the court (Law 5-96 Art. 12).
- **Individuals:** no sole proprietor is subject to these audit rules, which attach to company forms in Law 17-95 and Law 5-96. An expert-comptable may still be engaged voluntarily.
- **Listed SA:** publishes its statements in a legal notices journal with the meeting notice (Law 17-95 Art. 156).
- **IFRS:** a self-employed person or ordinary SARL is not told to use IFRS; bank, insurer and listed-group questions go to a professional. Consolidated accounts are where the old file placed IFRS (see Not yet confirmed).
- **Lost documents:** inform the inspector by registered letter within 15 days, 30 for force majeure (CGI Art. 211).

## Worked examples

### Example 1: Freelance developer, auto-entrepreneur

Software services, turnover collected MAD 190,000, under the MAD 200,000 limit (Art. 42 ter). **Result:** no bilan, no CPC, no court deposit, no auditor. Records go to `ma-bookkeeping`, returns to `ma-auto-entrepreneur`. Flag that RNR or incorporation changes this.

### Example 2: IT consultant on RNR, thinking of incorporating

Consultancy, turnover MAD 3,000,000, above the MAD 500,000 services limit for two years, so RNR. **As an individual:** accounts under Art. 145-I, return before 1 May, no auditor. **As a SARL closing 31 December 2026:** IS return by 31 March 2027, approval by 30 June 2027, deposit within 30 days of approval. MAD 3,000,000 is below MAD 50,000,000, so no mandatory auditor. Model: flag as unconfirmed and prepare the normal model.

## Self-checks

1. *"I'm an auto-entrepreneur, do I file financial statements?"* No (Art. 145-XI).
2. *"CPU, do I prepare a bilan?"* No under the CGI.
3. *"RNS?"* Art. 145-VI registers and lists.
4. *"What are the etats de synthese?"* Bilan, CPC, ESG, Tableau de financement, ETIC.
5. *"Normal or simplified?"* Line unconfirmed: use normal, flag it.
6. *"Do I use IFRS?"* Not for a freelancer or ordinary SARL.
7. *"Where do company accounts go?"* With the return, and to the court registry: 2 months (SA), 30 days (others).
8. *"Do I need a commissaire aux comptes?"* All SA and SCA; SARL, SNC or SCS above MAD 50,000,000; never a sole proprietor.

Also check: inputs trace to documents; regime confirmed; figures match 2026; output names unconfirmed items.

**Prohibitions.** Do not tell an AE or CPU taxpayer they must prepare a bilan. Do not let an RNR taxpayer or company skip accounts. Do not state the simplified model as settled. Do not tell a sole proprietor they need an auditor. Do not compute tax here. Do not replace a licensed Moroccan expert-comptable or commissaire aux comptes.

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI 2026 (DGI), Art. 20, 38, 39, 41, 42 ter, 43, 82, 145, 155, 184, 198 bis, 211, read in the DGI PDF text | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |
| Law 17-95 consolidated to Law 78-12 (AMMC), Art. 115, 156, 158, 159, 160, 163, 175, 386, 403, 420 | https://www.ammc.ma/sites/default/files/Loi%20n%C2%B0%2017-95.pdf | 2026-11-01 |
| Law 19-20, BO 7014, amending Art. 163 of Law 17-95 | https://www.ammc.ma/sites/default/files/LOI%20N%C2%B019-20.pdf | 2026-11-01 |
| Law 96-21, BO 7376, amends Law 17-95 Art. 12, 130, 245 only as far as read (share form) | https://www.sgg.gov.ma/BO/FR/2873/2025/BO_7376_fr.pdf | 2026-11-01 |
| Law 5-96, Art. 12, 21, 34, 70, 80, 95, 108, 109, archived copy of Adala dated 22 Feb 2020 (live page refused, later amendments not checked) | http://web.archive.org/web/20200222125632/http://adala.justice.gov.ma:80/production/html/fr/69028.htm | 2026-11-01 |
| Model 100/IS/N annexes, normal model, CFG Marches 2024 filing on AMMC | https://www.ammc.ma/sites/default/files/CFG%20MARCHES%20ETATS%20FINANCIERS%202024.pdf | 2026-11-01 |

Not yet confirmed: simplified model turnover line (old file: MAD 10,000,000) and its component list (old file: ESG dropped, tableau de financement and ETIC disputed); the old file's CGNC points that the five statements form an inseparable whole and that individual accounts stay under the CGNC with IFRS only for consolidated accounts; an auditor required by the statutes; text of Law 9-88 and the CGNC, including any Law 9-88 duties of traders on RNS, AE and CPU; whether Law 19-20, Law 24-10 or later laws changed Law 5-96 Art. 12, 70, 80, 95, 108, 109; the electronic deposit platform; the list of return annexes set by regulation; SIMPL-IS and SIMPL-IR screens; IFRS scope (Bank Al-Maghrib Circular 56/G/2007 for banks, insurers from 2022, the AMMC option for listed groups); the AE and CPU register contents. Art. 145 bis, cited by the old files, is repealed in the 2026 CGI.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).

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
