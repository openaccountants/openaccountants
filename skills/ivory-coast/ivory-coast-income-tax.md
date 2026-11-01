---
name: ivory-coast-income-tax
description: >
  Use this skill for Côte d'Ivoire (Ivory Coast) income tax in 2026: salary tax ITS with the RICF family reduction, business profit under BIC, BA and BNC, the entreprenant taxes, the microenterprise tax, RSI and RNI regimes, minimum tax IMF, withholding, dividends and patente. It covers employees, sole traders, professionals and companies. Trigger on "impôt sur les salaires", "ITS", "net pay Abidjan", "régime de l'entreprenant", "microentreprise", "BIC", "BNC", "IMF", "DGI", "e-impots" or "how much tax do I pay in Ivory Coast". It includes the Annexe fiscale 2026 changes: quarterly TEE and micro payments, mobile money deductibility, beneficial owner form and notes to the accounts.
version: 0.2
jurisdiction: CI
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

# Côte d'Ivoire (Ivory Coast) Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it without checking the cited official source or a licensed professional.

Tax year 2026 (calendar year). The Annexe fiscale 2026 took effect on 5 January 2026.

## Who this applies to

Employees taxed through ITS (salary tax), self-employed people and businesses under BIC, BA or BNC, and the four turnover regimes. Company profit tax sits here until a separate company skill exists. Employer charges and payroll steps are in [Payroll](ivory-coast-payroll.md); CNPS is in [Social contributions](ivory-coast-social-contributions.md); VAT is in [VAT](ivory-coast-vat.md).

The annual personal return (IGR) is suspended: "la déclaration de l'IGR est suspendue" (Art. 255 CGI). An employee of a Côte d'Ivoire employer has tax withheld. A person domiciled in Côte d'Ivoire paid by an employer abroad computes and declares ITS personally.

## Rates, bands and thresholds

| Item | Rate or amount | Conditions | Source |
|---|---|---|---|
| ITS band 0 to 75,000 XOF a month | 0% | Monthly taxable pay, Art. 119 bis | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page32.html |
| ITS band 75,001 to 240,000 | 16% | Same | same |
| ITS band 240,001 to 800,000 | 21% | Same | same |
| ITS band 800,001 to 2,400,000 | 24% | Same | same |
| ITS band 2,400,001 to 8,000,000 | 28% | Same | same |
| ITS above 8,000,000 | 32% | Same | same |
| RICF family reduction | 5,500 XOF a month per half part above 1 part; 44,000 at 5 parts | Deducted from gross ITS, maximum 5 parts, Art. 120 | https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf |
| Retirees over 70 | 75% abatement | On the tax after RICF | same |
| Dockers and dockers transit | 1.5% | Of total pay, Art. 120 | same |
| Pension or life annuity allowance | 320,000 XOF a month | Exempt at or below it, deducted above it | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page32.html |
| Taxe communale de l'entreprenant | 2% trade, 2.5% other | Turnover TTC up to 5,000,000 | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page4.html |
| Taxe d'Etat de l'entreprenant | 4% trade, 5% other, halved for CGA members | Turnover TTC 5,000,001 to 50,000,000, Art. 72-73 | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page5.html |
| Impôt des microentreprises | 6%, or 4% for CGA members or a convention expert-comptable | Turnover TTC 50,000,001 to 200,000,000, Art. 71 bis | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page7.html |
| Réel simplifié (RSI) | BIC rates below | Turnover TTC 200,000,001 to 500,000,000, Art. 45 | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page9.html |
| Réel normal (RNI) | BIC rates below | Turnover TTC above 500,000,000, Art. 34 | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page11.html |
| BIC and BA | 25% | Individuals and companies, Art. 51 | https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf |
| BIC telecoms and IT sector | 30% | Art. 51 | same |
| BIC gambling sector | 30% | Art. 51 | same |
| Foreign digital platforms | 30% of 10% of turnover TTC | No installation, Ivorian turnover at least 50,000,000, Art. 3-11, 21 ter, 51 | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page112.html |
| Minimum tax IMF, RNI and RSI | 0.5% of turnover TTC, floor 3,000,000, RNI cap 35,000,000 | 500,000 floor for service stations and butane distributors; new firms exempt in first year | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page16.html |
| IMF reduced rates | 0.10% petroleum, water, electricity; 0.15% banks, insurers | Art. 39 | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page17.html |
| BNC | 25% | Income under 1,000 XOF ignored | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page20.html |
| BNC minimum tax | 5% of gross receipts TTC, floor 400,000 | New firms exempt in first year | same |
| Withholding on BNC payments | 7.5% of gross | Listed payees, now including non-salaried radio, TV and film participants (Art. 96 as amended) | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page5.html |
| Withholding on BIC payments | 7.5% | Listed payees such as subcontractors in construction | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page17.html |
| Dividends, general | 15% or 17% for individuals | IRVM on sums not within Art. 182 | https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf |
| Dividends, listed on BRVM | 10% or 12% for individuals | Regularly paid by listed companies | same |
| Interest on claims | 18% general; current account 13.5% individuals, 16.5% companies | IRC, reduced rates apply | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page45.html |
| Patente, turnover duty | 0.5% of turnover HT, minimum 300,000 | Plus rental value duty at 18.5% (16% outside a commune) | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page23.html |

## The base

ITS base: all gross pay including bonuses, overtime and benefits in cash or kind, with no 20% abatement since the 2024 reform. Exempt items include food at up to 30,000 XOF a month in a staff canteen arrangement and expense allowances up to one tenth of total pay (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page31.html).

Parts: single, divorced or widowed without children 1; married without children 2; single with one child 2; each extra child adds 0.5; maximum 5. Children count if minor, or under 27 and studying (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page32.html).

Business profit: net result of all operations. Since 2026 mobile money payments are outside the 250,000 XOF cash limit "quels que soient leurs montants" (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page52.html). A charge must also relate to a product not exempt from profit tax (Art. 18-A-11°, https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page124.html). Payments to foreign related parties are capped at 5% of turnover and 20% of overheads, and at 50% of gross for non-cooperative or low-tax places (Art. 38, https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page93.html).

From 2026 share gain IRVM uses the mathematical, stock market or financial value method (Art. 184-8, https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page49.html).

Labelled digital startups outside the free zone are exempt from BIC, micro tax or TEE for three years after the year of labelling (Art. 12 septies, 71 quinquies, 80 bis, https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page119.html).

## Deadlines and filing

Salary tax: see [Payroll](ivory-coast-payroll.md).

| Task | Who | Date | Where |
|---|---|---|---|
| TEE or micro declaration | TEE, micro | 15 January | Tax office, on the prescribed form |
| TEE or micro payment | TEE, micro | Four equal parts: 31 March, 30 June, 30 September, 30 November (changed from monthly by Art. 36, https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page121.html) | Recette of the place of activity |
| Patente | All liable | 15 March; half by 15 March and half by 15 July | Recette |
| BNC return | BNC | 15 April (20 April DGE or DME) | Tax office |
| Result return and financial statements | RSI, RNI, TEE, micro | 30 May; 30 June if audited | DGE and DME only on e-impot |
| BIC or IMF payment | Tax office clients | 15 April, 15 June, 15 September | Recette |
| Same, DGE or DME | Industry and oil 10th, trade 15th, services 20th of April, June, September | | e-impot |
| Foreign platforms | Annual return and payment | 30 June of next year | Online, simplified procedure (Art. 35-3, 170 tredecies LPF) |

How to file a company result: 1. Close under SYSCOHADA revised. 2. Prepare balance sheet, income statement, cash flow table and notes where mandatory (Art. 36 as amended). 3. Add the updated beneficial owner form (Art. 24, https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page90.html) and bank account numbers. 4. Log in to e-impots at https://e-impots.gouv.ci as Contribuable. 5. DGE and DME send electronically only; micro must from 1 January 2027 and TEE from 1 January 2028 (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page83.html). 6. Pay in three parts.

## Penalties and interest

- Financial statements or notes not sent on time: 1,000,000 XOF plus 100,000 for each further month or part (LPF 169, https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page83.html). For the small regimes under Art. 82 bis: 100,000 plus 10,000 a month.
- No beneficial owner form with the statements: 1,000,000 plus 100,000 a month (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page91.html).
- Patente declaration late or missing: the LPF 169 fines now apply (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page58.html).
- No secondary establishment statement: 1,000,000 (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page12.html).
- TEE or micro: no books, 50,000 (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page6.html).

## Cross-border points

- Pay for services used in Côte d'Ivoire to persons with no installation there is BNC income, subject to treaties (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page19.html).
- Transfer pricing: Art. 38 was rewritten for 2026; the company carries the burden of proof through the Art. 36 bis statement (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page93.html). An advance pricing mechanism was added (Art. 23).
- Reinsurance premiums to non-residents are exempt from withholding until 30 April 2027 (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page122.html).
- Domiciled employees are taxed on pay even for work abroad; non-domiciled employees on work done in Côte d'Ivoire (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page31.html).

## Two worked examples that recompute

Example 1. Employee, 500,000 XOF a month, 3 parts. Gross ITS is 26,400 + 21% of 260,000 = 81,000. RICF is 22,000. Net ITS is 59,000.

```oa-check
name: ITS on 500000 with 3 parts
inputs:
  pay: 500000
  ricf: 22000
steps:
  - b16: (min(pay, 240000) - 75000) * 0.16
  - b21: (min(pay, 800000) - 240000) * 0.21
  - gross: b16 + b21
  - net: gross - ricf
expected:
  gross: 81000
  net: 59000
```

Example 2, a decision. Consultant, turnover TTC 120,000,000, profit 30,000,000: stay micro or opt for BNC by 1 February? Micro at 6% is 7,200,000; with a CGA, 4,800,000. BNC is 7,500,000, above the minimum of 6,000,000. Micro costs less. The option lasts three years.

```oa-check
name: Micro against BNC
inputs:
  turnover: 120000000
  profit: 30000000
steps:
  - micro: turnover * 0.06
  - micro_cga: turnover * 0.04
  - bnc: max(profit * 0.25, turnover * 0.05)
  - saving: bnc - micro
expected:
  micro: 7200000
  micro_cga: 4800000
  bnc: 7500000
  saving: 300000
```

## Working material carried from the earlier version

Pattern library for bank statements. Its treatments are classification aids; the rates above win.

Deterministic pre-classifier. Match by case-insensitive substring on the counterparty/description as it appears in the FCFA bank statement. If multiple match, use the most specific. If none match, ask the client.

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, REMUNERATION, [employer name] VIREMENT | Employment income (ITS, PAYE) | Already net if PAYE withheld; reconcile to gross |
| HONORAIRES, PRESTATION, FACTURE, CONSULTING | Business income (BNC/BIC) | Professional fees, self-employed |
| VIREMENT CLIENT, REGLEMENT FACTURE | Business income | If TVA-registered, extract net of 18% TVA |
| STRIPE, PAYPAL, WISE, FLUTTERWAVE, PAYSTACK PAYOUT | Business income | Platform payout, match to invoices |
| WAVE, ORANGE MONEY, MTN MOMO, MOOV MONEY (received) | Business income (if business) | Mobile-money inflow, confirm business vs personal |
| LOYER RECU, LOCATION | Rental income | Not business income, separate schedule |
| INTERETS, INTERET CREDITEUR | Investment income | Interest |
| DIVIDENDES | Investment income | Dividend |
| REMBOURSEMENT DGI, RISTOURNE IMPOT | EXCLUDE | Tax refund, not income |
| SUBVENTION (capital) | EXCLUDE unless revenue grant | Capital grants exclude; revenue grants = income |

### 3.2 Expense Patterns (Debits) -- Deductible business expenses (réel regimes)

**Deductible business expenses**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LOYER BUREAU, LOCATION LOCAL | Office rent | Deductible | Dedicated business premises |
| ASSURANCE PRO, RC PRO | Professional insurance | Deductible |  |
| EXPERT-COMPTABLE, COMPTABLE, AUDIT, CGA | Accountancy fees | Deductible | CGA membership also halves certain regime rates |
| AVOCAT, NOTAIRE, JURIDIQUE (business) | Legal fees | Deductible | Business-related only |
| FOURNITURES BUREAU, PAPETERIE | Office supplies | Deductible |  |
| PUBLICITE, MARKETING, GOOGLE ADS, META ADS | Marketing | Deductible |  |
| FORMATION, SEMINAIRE | Training | Deductible | Relating to current activity |
| FRAIS BANCAIRES, COMMISSION BANCAIRE | Bank charges | Deductible | Business account |
| HEBERGEMENT WEB, NOM DE DOMAINE, AWS, OVH | IT infrastructure | Deductible |  |

### 3.3 Expense Patterns (Debits) -- Software / SaaS

**Software / SaaS expenses**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| MICROSOFT 365, GOOGLE WORKSPACE | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, ZOOM, SLACK, NOTION | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB | Software subscription | Deductible |  |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| CIE (Compagnie Ivoirienne d'Électricité) | Electricity | T2 if home office | 100% if dedicated premises; apportion if home |
| SODECI | Water | T2 if home office | Apportion if mixed |
| ORANGE CI, MTN CI, MOOV AFRICA | Telecoms / internet | T2 | Business-use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) -- Travel & vehicle

**Travel & vehicle**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR COTE D'IVOIRE, ASKY, AIR FRANCE | Flights | Deductible if business travel | Wholly business purpose |
| HOTEL, BOOKING.COM | Accommodation | Deductible if business |  |
| YANGO, UBER, TAXI, WORO-WORO, GBAKA | Local transport | Deductible if business |  |
| TOTAL, SHELL, PETROCI, CARBURANT | Vehicle fuel | T2, business % only | Requires log |

### 3.6 Expense Patterns (Debits) -- NOT deductible

**Not deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, MAQUIS, DEJEUNER CLIENT | Entertainment / meals | Not deductible | Personal/representation |
| SUPERMARCHE, PROSUMA, CARREFOUR, CASH CENTER | Personal / groceries | Not deductible | Private living costs |
| AMENDE, PENALITE, CONTRAVENTION | Fines/penalties | Not deductible | Public policy |
| IMPOT, DGI PAIEMENT, ITS, TVA | Tax payments | Not deductible | Tax cannot reduce income |
| PRELEVEMENT PERSONNEL, RETRAIT GAB (personal) | Drawings | Not deductible | Not an expense |

### 3.7 Exclusions (neither income nor expense)

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VIREMENT INTERNE, ENTRE MES COMPTES | EXCLUDE | Own-account transfer |
| REMBOURSEMENT PRET, PRINCIPAL CREDIT | EXCLUDE | Loan principal movement |
| CNPS, COTISATION SOCIALE | CNPS deduction line | Employee CNPS is a payroll item, not a business expense line |
| TVA PAIEMENT, DGI TVA | EXCLUDE | VAT liability payment |

### 3.8 Ivorian Banks & Mobile Money -- Statement Format Reference

**Bank/mobile money formats**

| Provider | Common patterns | Notes |
| --- | --- | --- |
| SGBCI / Société Générale CI | VIREMENT, PRELEVEMENT, COMMISSION | PDF/CSV; description holds counterparty |
| Ecobank CI | TRANSFER, FRAIS, CARTE | PDF/CSV |
| NSIA Banque / BICICI | VIREMENT, AGIOS | PDF |
| Orange Money / MTN MoMo / Moov Money / Wave | DEPOT, RETRAIT, TRANSFERT, PAIEMENT MARCHAND | Mobile-money; confirm business vs personal |

### Ivorian formats

**Bank statement / payslip formats**

| Source | Format | Key fields | Notes |
| --- | --- | --- | --- |
| SGBCI / Société Générale | PDF, CSV | Date, Libellé, Débit, Crédit, Solde | Date DD/MM/YYYY; counterparty in Libellé |
| Ecobank CI | PDF, CSV | Date, Description, Amount, Balance |  |
| NSIA / BICICI | PDF | Date, Libellé, Montant | Shorter descriptions |
| Mobile money (Orange/MTN/Moov/Wave) | CSV/PDF | Date, Type, Montant, Numéro | DEPOT/RETRAIT/TRANSFERT; confirm business vs personal |
| Payslip (bulletin de paie) | PDF | Salaire brut, ITS, CNPS, Net à payer | ITS = withheld income tax; CNPS = social security |

### Key French / Ivorian terms

**Key French / Ivorian terms**

| Term | English | Classification hint |
| --- | --- | --- |
| VIREMENT | Transfer | Check direction (income/expense) |
| PRELEVEMENT | Direct debit | Recurring expense |
| SALAIRE BRUT / NET | Gross / net salary | Reconcile gross → net via ITS + CNPS |
| ITS | Income tax on salary | Tax withheld (not a deductible expense) |
| CNPS / COTISATION | Social security | Employee 6.3% pension reduces net pay |
| HONORAIRES | Professional fees | Business income (BNC) |
| AGIOS / FRAIS / COMMISSION | Bank charges | Deductible (business account) |
| RETENUE A LA SOURCE | Withholding tax | BNC WHT (7.5%) |
| TVA | VAT (18%) | Liability/recoverable, not income/expense |


## Judgement points

- Parts: use 1 part until the family situation is documented.
- Local or expatriate: use local and flag it until the contract is seen; the employer tax moves from 2.8% to 12%.
- Regime: flag turnover near a band limit or unconfirmed CGA membership.
- Home and mixed-use utilities, and vehicle costs: 0% business use until a documented basis or log is provided.

## Ask the client first

1. Employee, self-employed or company?
2. Annual turnover TTC, and trade or services?
3. Marital status, number of children, dates of change?
4. CGA member or convention expert-comptable?
5. Tax office, DGE or DME, and sector?
6. Domicile, and where the work is done?

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Annexe fiscale 2026 (loi n° 2025-987), note de service and arts. 1 to 41 headings; articles quoted here read in full | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page2.html | 2026-11-01 |
| DGI, Le système fiscal ivoirien (undated e-book, predates the 2026 annex; the annex wins where they differ), pp. 3-51 read | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page3.html | 2026-11-01 |
| DGI, Impôts et taxes en Côte d'Ivoire, édition 2025 (art. 146 table, regimes, IRVM, VAT sections read) | https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf | 2026-11-01 |
| DGI, Calendrier des obligations fiscales (VAT and BIC parts read) | https://www.dgi.gouv.ci/assets/documents/CALENDRIER.pdf | 2026-11-01 |
| DGI note n° 00026 of 3 Jan 2024, employer contribution part read | https://www.dgi.gouv.ci/assets/documents/DOCTRINE%20FISCALE%202024/IMPOTS%20DIRECTS/IMPOT%20SUR%20LES%20TRAITEMENTS,%20SALAIRES,%20PENSIONS%20ET%20RENTES%20VIAGERES/N%C2%B0%2000026%20MFB%20DGI%20DLCD%20DU%2003%20JAN%202024%20Pr%C3%A9cisions%20relatives%20aux%20am%C3%A9nagements%20...%20des%20salari%C3%A9s.pdf | 2026-11-01 |
| DGI note n° 01248 on VAT credit refunds, opening part read | https://www.dgi.gouv.ci/assets/documents/PROCEDURE_DE_REMBOURSEMENT_DE_CREDIT_TVA.pdf | 2026-11-01 |
| CNPS, communiqué on ceilings from 1 Jan 2023 (whole notice read) | https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf | 2026-11-01 |
| CNPS, employer page (paying contributions read; its SMIG and pension ceiling are out of date, the communiqué wins) | https://www.cnps.ci/employeur | 2026-11-01 |

Not yet confirmed: the full consolidated Code général des Impôts and Livre de Procédures fiscales 2026 (DGI lists them in its paid kiosk; the text was not opened), so article numbers come from the DGI documents above; whether employee CNPS reduces the ITS base (the DGI texts read do not say; this skill uses gross); whether Art. 36 quarterly payment wording for the micro tax sits in Art. 79 or a micro article (the article heading and motives name both, the quoted text amends Art. 79); the DGI late filing and late payment rates carried by the earlier version (5%, 10%, 100%, monthly interest; LPF arts. 161 to 169 not opened); capital gains on buildings 17% and on shares; deductible optional social contributions limit; the SMAG; non-resident withholding 20% (Art. 92 not opened); RSI IMF cap (the 2025 DGI table shows none for RSI).

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
