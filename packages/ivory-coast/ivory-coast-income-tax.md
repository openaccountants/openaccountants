---
name: ivory-coast-income-tax
description: Use this skill whenever asked about Côte d'Ivoire (Ivory Coast) personal income tax, salary tax, or self-employed/business income tax. Trigger on phrases like "how much tax do I pay in Côte d'Ivoire", "Ivory Coast income tax", "ITS", "impôt sur les traitements et salaires", "salaire net", "net pay Abidjan", "CNPS contributions", "régime de l'entreprenant", "microentreprise tax", "BIC", "BNC", "taxe sur salaires", "RICF family reduction", "DGI", or any question about computing or filing income tax for an employee, self-employed person, or small business in Côte d'Ivoire. Also trigger when reading an Ivorian payslip or bank statement (FCFA / XOF), computing employer payroll tax, or advising on the entreprenant / microentreprise / réel regimes. This skill covers the post-2024-reform monthly ITS progressive scale, the RICF family-responsibility reduction, employer payroll tax, CNPS social security, business income regimes by turnover, withholding on BNC, filing deadlines, and penalties. ALWAYS read this skill before touching any Ivorian income tax work.
version: 0.1
jurisdiction: CI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Côte d'Ivoire (Ivory Coast) Income Tax

## Côte d'Ivoire (Ivory Coast) Income Tax -- Skill v0.1

> **Tier 2 — research-verified, NOT yet professionally verified.** All figures are sourced inline to primary law (Ordonnance n°2023-719; Loi de Finances 2025), the Direction Générale des Impôts (DGI), CNPS, and Big-4 commentary (PwC Worldwide Tax Summaries; Deloitte). Items with weak provenance are flagged `[RESEARCH GAP — reviewer to confirm]`. A warranted Ivorian tax practitioner (expert-comptable / conseil fiscal) must sign off before filing.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Côte d'Ivoire (Ivory Coast) |
| Tax | Personal income tax — **ITS** (Impôt sur les Traitements, Salaires, pensions et rentes viagères) on employment; BIC/BNC on business income |
| Currency | West African CFA franc — **XOF / FCFA** only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Code Général des Impôts (CGI); **Ordonnance n°2023-719 du 13 sept. 2023, Art. 119 bis** (merged ITS scale, effective 1 Jan 2024); **Loi de Finances 2025 (n°2024-1109 du 18 déc. 2024)** — no change to the salary scale (Deloitte) |
| Tax authority | **Direction Générale des Impôts (DGI)** — dgi.gouv.ci |
| Social security | **Caisse Nationale de Prévoyance Sociale (CNPS)** |
| Filing portal | DGI e-services (e-impots / SIGICI) |
| Salary tax collection | **PAYE** — withheld and remitted monthly by the employer |
| Annual business-profit deadline | **30 May** (standard) / **30 June** (companies subject to statutory audit) (PwC, tax administration) |
| Validated by | Pending — requires sign-off by a warranted Ivorian tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

> **Côte d'Ivoire DOES have a personal income tax.** Residents are taxed on worldwide income (PwC, taxes on personal income).

### CRITICAL — which scale is current

A 2023/2024 reform (**Ordonnance n°2023-719**, effective **1 Jan 2024**) **merged** the three former salary levies — *IS/ITS*, *Contribution Nationale (CN)*, and *Impôt Général sur le Revenu (IGR)* — into a **single monthly progressive tax on salaries ("ITS")**. Many calculator/SEO sites still publish the **pre-2024 (abolished)** barème (0/10/15/20/25/35/60% plus separate 1.5% IGR + 1.5% CN). **Do NOT use the old scale.** The scale below is confirmed against the Ordonnance legal text (loidici.biz) and PwC, which agree exactly; Deloitte confirms LF 2025 left it unchanged.

### ITS — Current Monthly Progressive Scale (per Art. 119 bis)

Applied **monthly**, per taxpayer (spouses taxed separately).

**ITS Monthly Progressive Scale**  _(Source: PwC Worldwide Tax Summaries (Ivory Coast, taxes on personal income); Ordonnance n°2023-719, Art. 119 bis (loidici.biz).)_

| Monthly taxable income (FCFA) | Rate | Cumulative tax at top of band (FCFA) |
| --- | --- | --- |
| 0 -- 75,000 | 0% | 0 |
| 75,001 -- 240,000 | 16% | 26,400 |
| 240,001 -- 800,000 | 21% | 144,000 |
| 800,001 -- 2,400,000 | 24% | 528,000 |
| 2,400,001 -- 8,000,000 | 28% | 2,096,000 |
| Above 8,000,000 | 32% | — |

**Cumulative-tax check (recomputed):**
- 75,000 → 0
- 240,000 → 0 + (240,000−75,000)×16% = 165,000×0.16 = **26,400** ✓
- 800,000 → 26,400 + (800,000−240,000)×21% = 560,000×0.21 = 117,600 → **144,000** ✓
- 2,400,000 → 144,000 + (2,400,000−800,000)×24% = 1,600,000×0.24 = 384,000 → **528,000** ✓
- 8,000,000 → 528,000 + (8,000,000−2,400,000)×28% = 5,600,000×0.28 = 1,568,000 → **2,096,000** ✓

### RICF — Family-Responsibility Reduction (replaces old quotient familial)

A flat **monthly reduction** of the computed gross ITS, by number of "parts" (shares), capped at 5 parts.

**RICF reduction by parts**  _(Source: PwC (deductions); loidici.biz (reform note).)_

| Parts | Monthly reduction (FCFA) |
| --- | --- |
| 1.0 | 0 |
| 2.0 | 11,000 |
| 3.0 | 22,000 |
| 4.0 | 33,000 |
| 5.0 (max) | 44,000 |

**Shares (parts) allocation:**

**Shares (parts) allocation**  _(Source: PwC (deductions); loidici.biz.)_

| Situation | Parts |
| --- | --- |
| Single / divorced / widowed, no children | 1.0 |
| Married, no children | 2.0 |
| Single / divorced, 1 child | 2.0 |
| Married / widowed, 1 child | 2.5 |
| Each additional dependent child | +0.5 |
| Minor/infirm adult dependent | +1.0 |
| **Maximum** | **5.0** |

- **Over-70 retirees additional reduction** — 75% reduction of the tax computed after the RICF; exempt pension portion raised from 200,000 to 320,000 FCFA  _(loidici.biz; PwC)_

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown number of parts / family situation | Use **1.0 part** (zero RICF reduction) — never inflate parts without proof |
| Unknown resident vs non-resident | STOP — do not compute (see Refusal R-CI-3) |
| Unknown local vs expatriate (employer payroll tax) | Treat as **local** (2.8%) and flag for reviewer |
| Unknown business regime | Classify by turnover; if turnover unknown, STOP |
| Unknown whether allowance is taxable | Treat as **taxable** (reform removed most abatements) |
| Unknown benefit-in-kind value | Flag for reviewer (use DGI scheduled deemed values) |
| Unknown CNPS ceiling applicability | Apply the relevant ceiling; never exceed it |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable (employee)** — full-year payslips (bulletins de paie) or a bank statement showing net salary, plus family situation (parts) and local/expat status.

**Minimum viable (self-employed/business)** — bank statement for the full tax year (CSV/PDF/text) **and** annual turnover (chiffre d'affaires TTC), which determines the regime.

**Recommended** — employer's monthly ITS returns (état 301 / déclaration), CNPS statements, invoices, prior-year DGI assessment, CGA membership status (halves several rates).

**Ideal** — complete income/expenditure account, asset register, benefit-in-kind schedule (housing/water/electricity/A-C), withholding certificates (BNC).

**Refusal if minimum is missing — SOFT WARN.** No bank statement or payslips at all = hard stop. Bank statement only, no invoices = proceed with reviewer warning: "Produced from bank statement alone — reviewer must verify all deductions are supported and the wholly-and-exclusively / professional-purpose test is met."

### Refusal Catalogue

- **R-CI-1** — Family situation (parts) unknown. "The RICF reduction depends on the number of parts. Compute provisionally at 1.0 part (no reduction) and flag, or obtain the family situation before finalising."
- **R-CI-2** — Companies / partnerships. "This skill covers individuals (employees, sole proprietors, liberal professions). Sociétés (SA, SARL, SAS) file corporate IS returns. Escalate to an expert-comptable."
- **R-CI-3** — Non-resident / expatriate complex cases. "Non-resident taxation, treaty relief, and split-year residence have distinct rules. Out of scope. Escalate."
- **R-CI-4** — Capital gains on property/shares. "Building-sale gains (17%) and certain share-sale gains need specialised analysis. Escalate."
- **R-CI-5** — Arrears / DGI enforcement (mise en demeure, taxation d'office). "Penalties escalate to a 100% surcharge plus interest. Do not advise — escalate to an expert-comptable immediately."
- **R-CI-6** — VAT (TVA) return requested. "This skill covers income tax only. TVA standard rate is 18% (PwC) — use a dedicated VAT skill."

## Section 3 -- Transaction Pattern Library

Deterministic pre-classifier. Match by case-insensitive substring on the counterparty/description as it appears in the FCFA bank statement. If multiple match, use the most specific. If none match, fall through to Tier 1 rules (Section 5).

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, REMUNERATION, [employer name] VIREMENT | Employment income (ITS, PAYE) | Already net if PAYE withheld; reconcile to gross |
| HONORAIRES, PRESTATION, FACTURE, CONSULTING | Business income (BNC/BIC) | Professional fees — self-employed |
| VIREMENT CLIENT, REGLEMENT FACTURE | Business income | If TVA-registered, extract net of 18% TVA |
| STRIPE, PAYPAL, WISE, FLUTTERWAVE, PAYSTACK PAYOUT | Business income | Platform payout — match to invoices |
| WAVE, ORANGE MONEY, MTN MOMO, MOOV MONEY (received) | Business income (if business) | Mobile-money inflow — confirm business vs personal |
| LOYER RECU, LOCATION | Rental income | Not business income — separate schedule |
| INTERETS, INTERET CREDITEUR | Investment income | Interest |
| DIVIDENDES | Investment income | Dividend |
| REMBOURSEMENT DGI, RISTOURNE IMPOT | EXCLUDE | Tax refund — not income |
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
| TOTAL, SHELL, PETROCI, CARBURANT | Vehicle fuel | T2 — business % only | Requires log |

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
| CNPS, COTISATION SOCIALE | CNPS deduction line | Employee CNPS reduces taxable base via payroll — not a business expense line |
| TVA PAIEMENT, DGI TVA | EXCLUDE | VAT liability payment |

### 3.8 Ivorian Banks & Mobile Money -- Statement Format Reference

**Bank/mobile money formats**

| Provider | Common patterns | Notes |
| --- | --- | --- |
| SGBCI / Société Générale CI | VIREMENT, PRELEVEMENT, COMMISSION | PDF/CSV; description holds counterparty |
| Ecobank CI | TRANSFER, FRAIS, CARTE | PDF/CSV |
| NSIA Banque / BICICI | VIREMENT, AGIOS | PDF |
| Orange Money / MTN MoMo / Moov Money / Wave | DEPOT, RETRAIT, TRANSFERT, PAIEMENT MARCHAND | Mobile-money; confirm business vs personal |

## Section 4 -- Worked Examples

All amounts in **FCFA (XOF)**. ITS scale and RICF per Section 1.

### Example 1 -- Mid-range salaried employee, single (1 part)

**Input line:**
`30/04/2025 ; SGBCI VIREMENT ; EMPLOYEUR SARL TECHCI ; SALAIRE AVRIL ; +280 825 ; XOF`

**Reasoning.** Monthly taxable salary **350,000** (gross taxable; the credit shown is net after PAYE+CNPS — reconcile to gross of 350,000).
- ITS gross = 26,400 + (350,000 − 240,000) × 21% = 26,400 + 110,000 × 0.21 = 26,400 + 23,100 = **49,500**
- RICF, 1 part = **0** → net ITS = **49,500**
- CNPS pension employee 6.3% × 350,000 = **22,050** (below 3,375,000 ceiling)
- Net pay = 350,000 − 49,500 − 22,050 = **278,450**

**Classification:** ITS withheld 49,500; CNPS employee 22,050; net pay 278,450.

> (The bank credit 280,825 differs from 278,450 only if employer also reimburses a non-taxable allowance — flag if material.)

### Example 2 -- Same salary, married with 2 children (3.0 parts)

**Input:** Monthly taxable salary **350,000**; married, 2 dependent children → parts = 2.0 (married, 1 child = 2.5) + 0.5 (2nd child) = **3.0 parts**.
- ITS gross = **49,500** (as Example 1)
- RICF, 3 parts = **22,000** → net ITS = 49,500 − 22,000 = **27,500**
- CNPS employee 6.3% × 350,000 = **22,050**
- Net pay = 350,000 − 27,500 − 22,050 = **300,450**

**Classification:** ITS 27,500; CNPS 22,050; net pay 300,450.

### Example 3 -- Higher earner, married no children (2.0 parts)

**Input:** Monthly taxable salary **1,000,000**; married, no children → **2.0 parts**.
- ITS gross = 144,000 + (1,000,000 − 800,000) × 24% = 144,000 + 200,000 × 0.24 = 144,000 + 48,000 = **192,000**
- RICF, 2 parts = **11,000** → net ITS = **181,000**
- CNPS pension employee 6.3% × 1,000,000 = **63,000** (below 3,375,000 ceiling)
- Net pay = 1,000,000 − 181,000 − 63,000 = **756,000**

**Classification:** ITS 181,000; CNPS 63,000; net pay 756,000.

### Example 4 -- Employer payroll tax (taxe sur salaires), expatriate

**Input:** Employer employs one expatriate on monthly taxable remuneration **1,000,000**.
- Expatriate employer payroll tax = 12% × 1,000,000 = **120,000** (PwC; former 20% abatement removed)
- (Local employee equivalent would be 2.8% × 1,000,000 = **28,000**)

**Classification:** Employer-borne taxe sur salaires = 120,000 (expat) — this is an employer cost, NOT withheld from the employee.

### Example 5 -- Self-employed consultant, BNC, resident withholding

**Input line:**
`15/06/2025 ; ECOBANK VIREMENT ; CLIENT BTP CI ; HONORAIRES FACTURE 2025-014 ; +925 000 ; XOF`

**Reasoning.** Registered resident liberal professional (BNC). The payer withholds **7.5%** WHT at source on the gross fee (PwC / arcop.ci). If the gross invoice was 1,000,000, then WHT = 75,000 and the net received = 925,000. The BNC profit is taxed under the réel regime at the BIC/standard rate of **25%** on net profit; the 7.5% is a creditable advance, not final, for residents.

**Classification:** Gross fee 1,000,000; WHT credit 75,000; net received 925,000. Annual BNC profit taxed at 25% with WHT credited.

### Example 6 -- Régime de l'entreprenant, Taxe d'État (TEE)

**Input:** Service provider, annual turnover **30,000,000 FCFA TTC**, NOT a CGA member.
- Falls in entreprenant TEE band (5,000,001–50,000,000). Services rate = **5%** (commerce/retail would be 4%).
- Annual TEE = 5% × 30,000,000 = **1,500,000**
- Paid monthly at 1/12 = **125,000/month**, due by the **10th** (blog.ivoire-juriste.com; ccesp.ci)
- If a CGA member: rate halved (50%) → 2.5% → annual **750,000** (125,000... i.e. 62,500/month)

**Classification:** TEE 1,500,000/year (125,000/month); 750,000/year if CGA member.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 ITS taxable base

- **ITS taxable base composition** — Includes all cash remuneration — base salary, living/housing allowances, bonuses, and employer-paid social contributions. The 2024 reform eliminated the former 20% abatement / standard employment-expense deduction. Benefits in kind (housing, electricity, water, A/C) are taxed at DGI deemed scheduled values.  _(PwC, deductions & other taxes; PwC, income determination)_

**Some non-taxable thresholds**  _(PwC, income determination)_

| Item | Exempt up to |
| --- | --- |
| Food allowance | 30,000 FCFA/month |
| Business-expense allowance | 10% of taxable cash income |
| Non-mandatory social contributions | ≤10% of gross income and ≤3,800,000 FCFA/year |

### 5.2 ITS computation order

- **ITS computation order** — 1. Determine monthly taxable income (Section 5.1). 2. Apply the progressive scale (Section 1) → gross ITS. 3. Subtract the RICF reduction for the number of parts (max 5). 4. If retiree over 70: apply the further 75% reduction (Section 1). 5. Result = monthly ITS withheld by employer (PAYE).

### 5.3 Employer payroll tax (taxe sur salaires, employer-borne)

**Employer payroll tax rates**  _(Source: PwC (corporate & individual, other taxes).)_

| Workforce | Rate on total taxable remuneration |
| --- | --- |
| Local employees | **2.8%** |
| Expatriate employees | **12%** |

- **Former reduction eliminated / employer cost note** — Former 20% reduction eliminated. This is an employer cost — not withheld from the employee.  _(PwC (corporate & individual, other taxes))_

### 5.4 CNPS social security

**CNPS contribution branches**  _(Source: PwC (individual & corporate, other taxes).)_

| Branch | Employee | Employer | Combined | Monthly ceiling (FCFA) |
| --- | --- | --- | --- | --- |
| Retirement / pension | 6.3% | 7.7% | **14.0%** | 3,375,000 |
| Family allowances (incl. maternity) | — | 5.75% | 5.75% | 70,000 |
| Work-injury (accidents du travail) | — | 2% to 5% (by risk) | 2%–5% | 70,000 |

**Arithmetic check:** pension employee 6.3% + employer 7.7% = **14.0%** combined ✓. Note the two ceilings: pension capped at **3,375,000/month**; family-allowance and work-injury capped at **70,000/month**.

### 5.5 Minimum wage (SMIG)

- **SMIG** — 75,000 FCFA/month FCFA/month  _(Décret n°2022-986, in force since 1 Jan 2023; no revaluation as of 2026 (guidedufonctionnaire.com; sikafinance.com))_
- **SMAG (agricultural minimum)** — 39,960 FCFA/month FCFA/month  _(guidedufonctionnaire.com; sikafinance.com)_
- **SMIG equals 0% ITS band ceiling** — SMIG equals the 0% ITS band ceiling, so minimum-wage earners pay no ITS.

### 5.6 Business income regimes (by annual turnover, CA TTC)

**Business income regimes by turnover**  _(Sources: blog.ivoire-juriste.com; ccesp.ci; ivoire-juriste.com.)_

| Regime | Turnover band (FCFA TTC) | Tax |
| --- | --- | --- |
| **Entreprenant — TCE (Taxe Communale)** | < 5,000,000 | <1.2M: fixed daily forfait set by the local authority. 1.2M–5M: **2.5%** (commerce/retail) or **2%** (services/crafts) |
| **Entreprenant — TEE (Taxe d'État)** | 5,000,001 – 50,000,000 | **4%** (commerce/retail), **5%** (services); halved (50%) for CGA members. Paid monthly (1/12), due 10th |
| **Microentreprises** | 50,000,001 – 200,000,000 | **7%** of CA TTC; **5%** for CGA members |
| **Réel Simplifié (RSI)** | option from ~100M; standard ≥200M up to 500M `[RESEARCH GAP — reviewer to confirm exact RSI/RNI boundary in CGI]` | BIC/BNC at standard rate |
| **Réel Normal (RNI)** | > 500,000,000 | BIC/BNC at standard rate |

The entreprenant ≤50M and microentreprise 50,000,001–200,000,000 bands are consistently reported; RSI/RNI exact boundaries vary between secondary sources — **flagged as a research gap**.

### 5.7 Profit-tax rates (réel regimes) and minimum tax

**Profit-tax rates and minimum tax**  _(Source: PwC (taxes on corporate income).)_

| Item | Rate |
| --- | --- |
| BIC / standard profit tax (general) | **25%** |
| Telecom / IT / communications | **30%** |
| BNC (liberal professions) | taxed at the BIC rate (**25%**) under the réel regimes |
| Minimum tax (IMF) | **0.5% of turnover**, floor **3,000,000**, cap **35,000,000** FCFA |

### 5.8 Withholding on BNC service payments

**Withholding on BNC service payments**  _(Source: arcop.ci; fideca.com.)_

| Payee | WHT rate | Final? |
| --- | --- | --- |
| Registered resident | **7.5%** of gross | Creditable advance (not final) |
| Non-resident / no professional establishment in CI | **20%** of gross | **Final (libératoire)** |

### 5.9 Other individual taxes

**Other individual taxes**

| Tax | Rate |
| --- | --- |
| VAT (TVA), standard | **18%** (PwC, other taxes) |
| Capital gains — buildings sold by individuals | **17%** (PwC, other taxes) |
| Capital gains — generally (other) | Generally not taxable for individuals; certain share gains taxable (PwC) |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Number of parts (RICF)

- Confirm marital status, number and ages of dependent children, and any infirm/adult dependents.
- **Conservative default:** 1.0 part (no reduction) until family situation documented.
- Flag: max 5.0 parts; over-70 retiree 75% second reduction.

### 6.2 Benefits in kind

- Housing, electricity, water, A/C valued at DGI scheduled deemed amounts, added to the ITS base.
- **Conservative default:** flag for reviewer to apply the correct deemed value. `[RESEARCH GAP — DGI deemed BIK scale values not reproduced here; reviewer to source.]`

### 6.3 Local vs expatriate (employer payroll tax)

- 2.8% (local) vs 12% (expat) materially changes employer cost.
- **Conservative default:** local (2.8%) and flag.

### 6.4 Business regime classification

- Driven by turnover TTC and CGA membership. CGA membership halves entreprenant TEE and microentreprise rates.
- Flag if turnover is near a band boundary or CGA status is unconfirmed.

### 6.5 Home-office / mixed-use utilities (réel regimes)

- CIE (electricity), SODECI (water), telecoms apportioned to business-use %.
- **Conservative default:** 0% until a documented, reasonable basis is provided.

### 6.6 Vehicle business use

- Fuel/insurance/maintenance apportioned to business %; requires a log.
- **Conservative default:** 0% until log provided.

### 6.7 BNC withholding credit vs final tax

- 7.5% resident WHT is creditable; 20% non-resident WHT is final. Confirm payee status.

## Section 7 -- Excel Working Paper Template

```
CÔTE D'IVOIRE INCOME TAX -- WORKING PAPER (FCFA)
Tax Year: 2025
Client: ___________________________
Type: Employee (ITS) / Self-employed (BNC/BIC) / Entreprenant / Microentreprise
Family parts (RICF): ______   Local / Expatriate: ______   CGA member: Y / N

==== A. EMPLOYEE — MONTHLY ITS ====
  A1. Gross taxable salary (incl. taxable allowances, BIK)   ___________
  A2. ITS gross (progressive scale)                          ___________
  A3. Less RICF reduction (by parts)                         ___________
  A4. Less over-70 retiree reduction (75%, if applicable)    ___________
  A5. ITS withheld = A2 - A3 - A4                            ___________
  A6. CNPS employee pension (6.3%, ceiling 3,375,000)        ___________
  A7. NET PAY = A1 - A5 - A6                                 ___________

  Employer-borne (memo):
  A8. Taxe sur salaires (2.8% local / 12% expat)             ___________
  A9. CNPS employer pension 7.7%                             ___________
  A10. CNPS family allowance 5.75% (ceiling 70,000)          ___________
  A11. CNPS work-injury 2%-5% (ceiling 70,000)               ___________

==== B. SELF-EMPLOYED — BUSINESS INCOME ====
  B1. Annual turnover TTC                                    ___________
  B2. Regime (TCE/TEE/Micro/RSI/RNI)                         ___________
  B3a. Entreprenant/Micro turnover tax (rate x B1)           ___________
  B3b. OR réel net profit                                    ___________
  B3c. Profit tax @25% (or 30% telecom/IT)                   ___________
  B4. Minimum tax IMF (0.5% turnover; floor 3,000,000;
      cap 35,000,000) — pay the higher of B3c and B4         ___________
  B5. Less BNC WHT credit (7.5% resident, advance)           ___________
  B6. Tax due                                                ___________

REVIEWER FLAGS:
  [ ] Family parts confirmed (max 5)?
  [ ] Local vs expatriate confirmed?
  [ ] CGA membership confirmed?
  [ ] Benefits in kind valued per DGI scale?
  [ ] Correct business regime by turnover?
  [ ] CNPS ceilings applied (3,375,000 / 70,000)?
  [ ] BNC WHT credit vs final tax determined?
  [ ] Pre-2024 (abolished) salary scale NOT used?
```

## Section 8 -- Bank Statement / Payslip Reading Guide

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
| RETENUE A LA SOURCE | Withholding tax | BNC WHT (7.5% / 20%) |
| TVA | VAT (18%) | Liability/recoverable — not income/expense |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement/payslips but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1) — including **1.0 part** for RICF.
4. Generate the working paper (Section 7) with flags.
5. Present these questions:

```
ONBOARDING QUESTIONS -- CÔTE D'IVOIRE INCOME TAX
1. Are you an employee (ITS via payroll) or self-employed/business owner?
2. Family situation: single/married/divorced/widowed? Number and ages of dependent children? Any infirm adult dependents?
3. Are you a local employee or an expatriate?
4. (Self-employed) What is your annual turnover (chiffre d'affaires TTC)?
5. Are you a member of a Centre de Gestion Agréé (CGA)?
6. Any benefits in kind (housing, electricity, water, A/C provided by employer)?
7. Any non-salary income (rental, interest, dividends)?
8. (Self-employed) Any withholding tax (retenue à la source) suffered on your fees?
9. Are you resident in Côte d'Ivoire for the full tax year?
10. Are you over 70 and receiving a pension?
```

## Section 10 -- Reference Material

### Key legislation / authority references

**Key legislation / authority references**

| Topic | Reference |
| --- | --- |
| Merged ITS salary scale (current) | Ordonnance n°2023-719 du 13 sept. 2023, Art. 119 bis (eff. 1 Jan 2024) |
| No change to scale for 2025 | Loi de Finances 2025, n°2024-1109 du 18 déc. 2024 (Deloitte) |
| Salary scale & RICF figures | PwC Worldwide Tax Summaries — Ivory Coast (individual) |
| Employer payroll tax (2.8%/12%) | PwC — other taxes (corporate & individual) |
| CNPS contributions & ceilings | PwC — other taxes; CNPS |
| Business regimes by turnover | blog.ivoire-juriste.com; ccesp.ci; ivoire-juriste.com |
| Corporate/BIC rate & IMF minimum tax | PwC — taxes on corporate income |
| BNC withholding (7.5%/20%) | arcop.ci; fideca.com |
| SMIG / SMAG | Décret n°2022-986; guidedufonctionnaire.com; sikafinance.com |
| Filing deadlines (30 May / 30 June) | PwC — tax administration |
| Penalties | DGI (dgi.gouv.ci); CGI / Livre des Procédures Fiscales |

### Filing, payment, administration

- **Tax year = calendar year.** Salary tax is **withheld monthly by the employer (PAYE)**; the employer files monthly returns for both employee and employer payroll taxes. Employees with a local employer generally do not file a separate return; **spouses are taxed and file separately** (PwC, tax administration).
- **Monthly payment due dates (for the preceding month):** industrial/mining/oil — **10th**; sales companies — **15th**; service providers — **20th**; other registered entities — **15th**; entreprenant & micro-enterprise — **10th** (PwC, tax administration).
- **Annual business-profit deadlines:** companies subject to statutory audit — **30 June**; other companies — **30 May** (PwC).

### Penalties (DGI / CGI / Livre des Procédures Fiscales)

**Penalties table**  _(Source: DGI (dgi.gouv.ci); DGI "IMPÔTS ET TAXES EN CÔTE D'IVOIRE" PDF.)_

| Situation | Charge |
| --- | --- |
| Late filing before formal notice (mise en demeure) | **5%** of duties declared |
| Filed within 7 days after mise en demeure | **10%** of duties |
| No filing after mise en demeure | Taxation d'office **+ 100%** surcharge |
| Late payment | **10%** flat from day 1, **plus monthly interest** `[RESEARCH GAP — exact monthly interest % not confirmed against primary CGI; reviewer to confirm]` |

### Test Suite

**Test 1 — Single employee, 1 part.**
Input: monthly taxable salary 350,000; single (1 part).
Expected: ITS gross = 49,500; RICF = 0; ITS = **49,500**; CNPS employee = 22,050; net pay = **278,450**.

**Test 2 — Married, 2 children (3 parts).**
Input: monthly taxable salary 350,000; 3 parts.
Expected: ITS gross 49,500; RICF 22,000; ITS = **27,500**; CNPS 22,050; net pay = **300,450**.

**Test 3 — Higher earner, married no children (2 parts).**
Input: monthly taxable salary 1,000,000; 2 parts.
Expected: ITS gross = 192,000; RICF 11,000; ITS = **181,000**; CNPS 63,000; net pay = **756,000**.

**Test 4 — Minimum-wage earner.**
Input: monthly salary 75,000 (SMIG); any parts.
Expected: falls in 0% band → ITS = **0**. CNPS employee 6.3% × 75,000 = 4,725.

**Test 5 — Expatriate employer payroll tax.**
Input: expat, monthly taxable remuneration 1,000,000.
Expected: employer taxe sur salaires = 12% × 1,000,000 = **120,000** (vs 28,000 if local).

**Test 6 — BNC resident withholding.**
Input: registered resident, gross fee 1,000,000.
Expected: WHT = 7.5% × 1,000,000 = **75,000** (creditable advance); net received 925,000; annual profit taxed at 25% with WHT credited.

**Test 7 — Entreprenant TEE, services, non-CGA.**
Input: services, turnover 30,000,000 TTC, not CGA.
Expected: TEE = 5% × 30,000,000 = **1,500,000/year** (125,000/month); 750,000/year if CGA.

**Test 8 — Pre-2024 scale rejection.**
Input: a worksheet applying 0/10/15/20/25/35/60% + 1.5% IGR + 1.5% CN.
Expected: **REJECT** — that is the abolished pre-2024 system. Recompute with the Art. 119 bis monthly scale.

## PROHIBITIONS

- NEVER use the **pre-2024 (abolished)** salary barème (0/10/15/20/25/35/60% + IGR + CN). Use the Art. 119 bis monthly scale only.
- NEVER inflate the number of **parts** for RICF without documented proof — default to 1.0.
- NEVER exceed the RICF cap of **5.0 parts** or the monthly reduction of **44,000**.
- NEVER ignore the **CNPS ceilings** (3,375,000 pension; 70,000 family/work-injury).
- NEVER apply the **20% expatriate** employer payroll tax to a local employee, or vice versa, without confirmation.
- NEVER apply the old **20% employment-expense abatement** — the 2024 reform removed it.
- NEVER treat ITS or TVA payments as deductible business expenses.
- NEVER treat the **7.5% resident BNC WHT** as final — it is a creditable advance (only the 20% non-resident WHT is final).
- NEVER classify a business regime without the **annual turnover (CA TTC)**.
- NEVER present tax calculations as definitive — always label as estimated, pending professional sign-off.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable, conseil fiscal, CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
