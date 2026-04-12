---
name: ch-federal-income-tax
description: >
  Use this skill whenever asked about Swiss federal income tax (direkte Bundessteuer / impot federal direct) for self-employed individuals. Trigger on phrases like "Bundessteuer", "direkte Bundessteuer", "impot federal direct", "Steuererklarung Schweiz", "selbstandig Steuern Schweiz", "Swiss federal income tax", "self-employed tax Switzerland", "AHV deduction", "Saule 3a", "BVG", "Geschaftsaufwand", or any question about computing or filing FEDERAL income tax for a self-employed person in Switzerland. This skill covers FEDERAL progressive brackets only (0--11.5%), Geschaftsaufwand, AHV/IV/EO deductibility, BVG/Saule 3a deductions, and federal filing. Cantonal and municipal taxes are out of scope. ALWAYS read this skill before touching any Swiss federal income tax work.
version: 2.0
jurisdiction: CH
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Switzerland Federal Income Tax (Direkte Bundessteuer) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Switzerland (Federal level only) |
| Tax | Direkte Bundessteuer (DBSt) |
| Currency | CHF only |
| Tax year | Calendar year |
| Primary legislation | Bundesgesetz uber die direkte Bundessteuer (DBG), SR 642.11 |
| Supporting legislation | AHVG; BVG; BVV 3 |
| Tax authority | ESTV / AFC |
| Filing portal | Cantonal tax portal (varies -- federal filed with cantonal return) |
| Filing deadline | 31 March (standard, varies by canton) / extensions routinely available |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Swiss Treuhnder or Steuerberater |
| Validation date | Pending |
| Skill version | 2.0 |

**IMPORTANT: This skill covers FEDERAL tax only. Cantonal and municipal taxes are separate and typically represent the majority of the total tax burden. They are out of scope.**

### Federal Tax Tariff -- Grundtarif (Single) -- Approximate

| Taxable Income (CHF) | Approx. Marginal Rate |
|---|---|
| 0 -- 17,800 | 0% |
| 17,801 -- 31,600 | 0.77% |
| 31,601 -- 41,400 | 0.88% -- 2.64% |
| 41,401 -- 55,200 | 2.97% |
| 55,201 -- 72,500 | 5.94% |
| 72,501 -- 78,100 | 6.60% |
| 78,101 -- 103,600 | 8.80% |
| 103,601 -- 134,600 | 11.00% |
| 134,601 -- 176,000 | 13.20% |
| 176,001+ | 11.50% max effective rate |

**NEVER compute Swiss federal tax from these approximate brackets. Use official ESTV tariff tables.**

### Verheiratetentarif (Married)

More favourable. Tax-free threshold ~CHF 30,800. Maximum effective rate 11.5% reached ~CHF 912,600.

### Saule 3a Limits (2025)

| Category | Maximum (CHF) |
|---|---|
| With BVG (Pensionskasse) | 7,258 |
| Without BVG | 20% of net earned income, max 36,288 |

### AHV/IV/EO (Self-Employed)

| Component | Rate |
|---|---|
| Total AHV/IV/EO | 10.0% |

Fully deductible. Rate 10.0% on income above CHF 10,100 (declining scale below).

### Key Deduction Lines

| Line | Description |
|---|---|
| Geschaftsaufwand | Business expenses |
| Abschreibungen | Depreciation |
| AHV/IV/EO | Social insurance contributions |
| BVG | Pillar 2 pension |
| Saule 3a | Pillar 3a |
| Kinderabzug | CHF 6,700 per child |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown marital status | STOP -- determines tariff |
| Unknown BVG status | Without BVG (higher 3a limit applies) |
| Unknown business-use % | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown cantonal question | ESCALATE -- federal only |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, marital status, canton of residence.

**Recommended** -- all invoices, AHV/IV/EO contribution statements, BVG certificate, Saule 3a statements, prior year Steuerveranlagung.

**Ideal** -- complete business accounts, Anlageverzeichnis, provisional tax notices.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement = hard stop. Unknown marital status = hard stop.

### Refusal Catalogue

**R-CH-1 -- Cantonal / municipal tax.** "This skill covers FEDERAL tax only. Cantonal and municipal taxes require separate cantonal skills or Treuhnder consultation. Do not estimate."

**R-CH-2 -- Corporations (AG, GmbH, Verein).** "Corporate taxation is separate. Out of scope."

**R-CH-3 -- Non-resident / Quellensteuer.** "Source tax for non-residents has different rules. Escalate."

**R-CH-4 -- Interkantonale Steuerausscheidung.** "Multi-canton allocation is out of scope."

**R-CH-5 -- Steuererlass / tax relief applications.** "Escalate to Treuhnder."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| ZAHLUNG, UBERWEISUNG [client], HONORAR | Einkünfte selbstandige Erwerbstatigkeit | Business income | Extract net if MWST-registered |
| STRIPE PAYOUT, PAYPAL PAYOUT | Business income | Revenue | Platform payout |
| LOHN, GEHALT, ARBEITGEBER | Einkünfte unselbstandige Erwerbstatigkeit | NOT self-employment | Employment income |
| MIETEINNAHME, MIETZINS | Einkünfte Liegenschaft | NOT self-employment | Rental income |
| ZINSEN, KAPITALERTRAG, DIVIDENDE | Einkünfte Vermogen | NOT self-employment | Capital income (VSt 35%) |
| STEUERRUCKERSTATTUNG, RUCKZAHLUNG | EXCLUDE | Not income | Tax refund |

### 3.2 Expense Patterns (Debits) -- Fully Deductible (Geschaftsaufwand)

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| BÜROMIETE, GESCHÄFTSMIETE, OFFICE RENT | Raumkosten | Fully deductible | Dedicated premises |
| BERUFSHAFTPFLICHT, VERSICHERUNG (business) | Versicherung | Fully deductible | Professional insurance |
| TREUHAND, BUCHHALTER, STEUERBERATER | Beratungskosten | Fully deductible | |
| RECHTSANWALT, NOTAR (business) | Rechtskosten | Fully deductible | |
| BÜROMATERIAL | Bürobedarf | Fully deductible | |
| WERBUNG, MARKETING, GOOGLE ADS | Werbekosten | Fully deductible | |
| WEITERBILDUNG, KURS, SEMINAR | Weiterbildung | Fully deductible (up to CHF 12,900) | Job-related |
| VERBANDSBEITRAG, MITGLIEDSCHAFT | Beitrge | Fully deductible | Professional associations |
| BANKGEBÜHR, KONTOFÜHRUNG | Bankspesen | Fully deductible | Business account |
| STRIPE FEE, PAYPAL FEE | Transaktionskosten | Fully deductible | |
| SOFTWARE, LIZENZ, ABONNEMENT (under CHF 1,000) | IT-Kosten | Fully deductible | Low-value = immediate expense |

### 3.3 Expense Patterns -- Social Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| AHV, AUSGLEICHSKASSE, SVA | Fully deductible | AHV/IV/EO contributions |
| BVG, PENSIONSKASSE, AUFFANGEINRICHTUNG | Fully deductible | Pillar 2 |
| SÄULE 3A, VORSORGE 3A | Deductible within limits | CHF 7,258 or CHF 36,288 |

### 3.4 Expense Patterns -- Travel

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| FLUG, SWISS, EASYJET, RYANAIR | Reisekosten | Fully deductible | Business purpose |
| HOTEL, BOOKING.COM | Reisekosten | Fully deductible | Business travel |
| SBB, BLS, ZVV | Reisekosten | Fully deductible | Business travel |
| TAXI, UBER | Reisekosten | Fully deductible | Business purpose |
| TANKSTELLE, MIGROL, COOP PRONTO, BP | Fahrzeugkosten | T2 -- business % only | |

### 3.5 Expense Patterns -- NOT Deductible

| Pattern | Treatment | Notes |
|---|---|---|
| PRIVAT, LEBENSMITTEL, MIGROS, COOP (groceries) | NOT deductible | Lebenshaltungskosten |
| BUSSE, ORDNUNGSBUSSE | NOT deductible | Fines |
| BUNDESSTEUER, KANTONSSTEUER, STEUERN | NOT deductible | Income tax |
| PRIVATBEZUG | NOT deductible | Drawings |

### 3.6 Capital Items

| Pattern | Straight-Line | Reducing Balance | Notes |
|---|---|---|---|
| COMPUTER, LAPTOP, PC | 40% | 50% | |
| BÜROMÖBEL | 12.5% | 25% | |
| FAHRZEUG, AUTO (business) | 20% | 40% | |
| MASCHINE, EQUIPMENT | 12.5%-20% | 25%-40% | |
| GEBÄUDE (commercial) | 2%-4% | 3%-7% | |
| Low-value (under CHF 1,000) | 100% immediate | -- | |

### 3.7 Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| EIGENÜBERWEISUNG, INTERNAL | EXCLUDE | Own-account transfer |
| DARLEHEN, KREDIT, AMORTISATION | EXCLUDE | Loan principal |
| DARLEHENSZINS (business) | Deductible | Business loan interest |
| MWST ZAHLUNG | EXCLUDE from P&L | MWST liability |
| STEUERZAHLUNG | EXCLUDE | Tax payment |

### 3.8 Swiss Banks -- Statement Format Reference

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| UBS | CSV, PDF, MT940 | Buchungsdatum, Text, Betrag | UBS e-banking export |
| PostFinance | CSV, PDF | Datum, Buchungstext, Gutschrift/Belastung | PostFinance e-Finance |
| ZKB (Zurcher Kantonalbank) | CSV, PDF | Datum, Text, Betrag | |
| Credit Suisse / UBS (merged) | CSV, PDF | Datum, Beschreibung, Betrag | Post-merger formats |
| Raiffeisen CH | CSV, PDF | Datum, Buchungstext, Betrag | |
| Revolut, Wise | CSV | Date, Counterparty, Amount | Multi-currency |

---

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (MWST-registered)

**Input line:**
`15.03.2025 ; UBS Gutschrift ; AGENTUR ZURICH AG ; Honorar Mrz 2025 ; +8,100.00 ; CHF`

**Reasoning:**
Client payment. If MWST-registered (8.1% standard rate), CHF 8,100 may include MWST. Check invoice: if gross, net = CHF 7,493.06 + CHF 606.94 MWST. If Kleinunternehmer, full CHF 8,100.

**Classification:** Business income = CHF 7,493.06 (or CHF 8,100 if not MWST-registered).

### Example 2 -- AHV Contribution

**Input line:**
`15.02.2025 ; PostFinance Belastung ; AUSGLEICHSKASSE ZURICH ; AHV/IV/EO ; -4,800.00 ; CHF`

**Reasoning:**
AHV/IV/EO contributions. Fully deductible from taxable income.

**Classification:** Deductible. Reduces taxable income.

### Example 3 -- Saule 3a Contribution

**Input line:**
`30.06.2025 ; ZKB Überweisung ; CREDIT SUISSE SÄULE 3A ; Einzahlung 2025 ; -7,258.00 ; CHF`

**Reasoning:**
Saule 3a at maximum (CHF 7,258 with BVG). Fully deductible.

**Classification:** Deductible (within limit). If without BVG, could be up to CHF 36,288.

### Example 4 -- Software Subscription

**Input line:**
`01.04.2025 ; UBS Lastschrift ; ADOBE INC ; Creative Cloud ; -35.90 ; CHF`

**Reasoning:**
Monthly SaaS subscription. Under CHF 1,000. Fully deductible as Geschaftsaufwand.

**Classification:** Geschaftsaufwand -- IT. Fully deductible.

### Example 5 -- Cantonal Tax Payment (Exclude)

**Input line:**
`30.09.2025 ; PostFinance ; STEUERAMT ZH ; Kantonssteuer 2025 ; -5,000.00 ; CHF`

**Reasoning:**
Tax payment. Not deductible. Not a business expense.

**Classification:** EXCLUDE. Not deductible.

### Example 6 -- Low-Value Asset

**Input line:**
`03.06.2025 ; UBS Karte ; DIGITEC ; Drucker ; -890.00 ; CHF`

**Reasoning:**
Printer CHF 890. Under CHF 1,000 low-value threshold. Immediate full deduction.

**Classification:** Geschaftsaufwand. Fully deductible in year of purchase.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Business Income

All self-employment income is Einkünfte aus selbstandiger Erwerbstatigkeit (Art. 18 DBG). For MWST-registered, report net.

### 5.2 Geschaftsaufwand

Business expenses deductible under DBG Art. 27-31. Must be business-related.

### 5.3 Abschreibungen (Depreciation)

Choose straight-line or reducing balance (consistent per asset). ESTV guideline rates apply. Low-value under CHF 1,000 may be expensed immediately.

### 5.4 AHV/IV/EO Deductibility

Fully deductible. Self-employed pay 10.0% on income above CHF 10,100 (declining scale below). Circular calculation resolved by Ausgleichskasse.

### 5.5 Saule 3a and BVG

- With BVG: max CHF 7,258
- Without BVG: 20% of net earned income, max CHF 36,288
- Hard cap -- excess not deductible

### 5.6 Personal Deductions (Federal)

| Deduction | CHF |
|---|---|
| Married couple | 2,800 |
| Kinderabzug | 6,700 per child |
| Unterstützungsabzug | Up to 7,050 |

### 5.7 Non-Deductible

| Expense | Reason |
|---|---|
| Personal living expenses | Art. 34 DBG |
| Fines (Bussen) | Public policy |
| Income tax (all levels) | Tax on income |
| Capital expenditure | Through Abschreibungen |

### 5.8 Filing and Penalties

| Item | Detail |
|---|---|
| Standard deadline | 31 March (varies by canton) |
| Extensions | Routinely available |
| Late filing | Reminder + fee; estimated assessment |
| Persistent non-filing | Fine up to CHF 1,000 |
| Tax evasion | 33.3%-300% of evaded tax |

### 5.9 Provisional Tax

Billed by canton based on prior assessment. Interest on under/overpayment (Ausgleichszins).

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office (Arbeitszimmer)

Deductible if predominantly business use AND no separate business premises. Proportion by floor area. Flag for reviewer.

### 6.2 Vehicle Business Use

Business vs private split required. Private use of business vehicle = taxable benefit (Naturallohn). Flag for reviewer.

### 6.3 Phone / Internet Mixed Use

Business portion only. Default 0%.

### 6.4 BVG Voluntary Contributions

Self-employed may voluntarily join BVG. Contributions fully deductible. Flag for reviewer to confirm BVG status.

### 6.5 AHV Declining Scale

For income CHF 10,100-58,800, rate is less than 10%. Use official AHV table.

---

## Section 7 -- Excel Working Paper Template

```
SWITZERLAND FEDERAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Marital Status: Single / Married
Canton: ___________ (for filing only -- cantonal tax is OUT OF SCOPE)

A. SELF-EMPLOYMENT INCOME
  A1. Business revenue (net of MWST)              ___________
  A2. Other business income                        ___________
  A3. Total                                        ___________

B. GESCHÄFTSAUFWAND
  B1. Raumkosten                                   ___________
  B2. Versicherungen (business)                    ___________
  B3. Beratungskosten                              ___________
  B4. IT / Software                                ___________
  B5. Marketing                                    ___________
  B6. Reisekosten                                  ___________
  B7. Fahrzeugkosten (business %)                  ___________
  B8. Abschreibungen                               ___________
  B9. Bankspesen                                   ___________
  B10. Übrige Geschäftsaufwand                     ___________
  B11. Total                                       ___________

C. NET SELF-EMPLOYMENT INCOME (A3 - B11)           ___________

D. DEDUCTIONS
  D1. AHV/IV/EO                                    ___________
  D2. BVG                                          ___________
  D3. Säule 3a                                     ___________
  D4. Kinderabzug                                  ___________
  D5. Other personal deductions                    ___________
  D6. Total deductions                             ___________

E. STEUERBARES EINKOMMEN (C - D6)                  ___________

F. DIREKTE BUNDESSTEUER (use ESTV tariff)          ___________

NOTE: This is FEDERAL TAX ONLY. Cantonal/municipal = separate.

REVIEWER FLAGS:
  [ ] Marital status confirmed (Grundtarif/Verheiratetentarif)?
  [ ] BVG status confirmed (affects Säule 3a limit)?
  [ ] Home office eligibility confirmed?
  [ ] Vehicle business % confirmed?
  [ ] AHV contribution rate confirmed (declining scale)?
```

---

## Section 8 -- Bank Statement Reading Guide

### Swiss Bank Statement Formats

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| UBS | CSV, PDF, MT940 | Buchungsdatum, Text, Betrag | E-banking export |
| PostFinance | CSV, PDF | Datum, Buchungstext, Gutschrift/Belastung | E-Finance export |
| ZKB | CSV, PDF | Datum, Text, Betrag | |
| Raiffeisen CH | CSV, PDF | Datum, Buchungstext, Betrag | |
| Credit Suisse (now UBS) | CSV, PDF | Datum, Beschreibung, Betrag | Legacy format |
| Revolut, Wise | CSV | Date, Counterparty, Amount | Multi-currency |

### Key Swiss Banking Terms

| Term | English | Hint |
|---|---|---|
| Gutschrift | Credit | Potential income |
| Belastung / Lastschrift | Debit | Potential expense |
| Überweisung | Transfer | Check direction |
| Dauerauftrag | Standing order | Regular expense |
| Kartenzahlung | Card payment | Expense |
| Bargeldbezug | Cash withdrawal | Ask purpose |
| Kontoführung | Account maintenance | Bank charge |
| Vergütung | Payment/remuneration | Often income |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- SWITZERLAND FEDERAL INCOME TAX
1. Marital status: single or married?
2. Canton and municipality of residence?
3. BVG (Pensionskasse) member? (Affects Säule 3a limit)
4. Säule 3a contributions made?
5. Home office: dedicated room? Separate business premises?
6. Vehicle: business use %?
7. Phone/internet: business use %?
8. AHV/IV/EO contributions paid?
9. Other income (employment, rental, securities)?
10. Children / dependants?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Self-employment income | DBG Art. 18 |
| Business expenses | DBG Art. 27-31 |
| Non-deductible | DBG Art. 34 |
| Depreciation | DBG Art. 28; ESTV Merkblatt |
| AHV/IV/EO deduction | DBG Art. 33 Abs. 1 lit. d, f |
| BVG / Saule 3a | BVG; BVV 3; DBG Art. 33 |
| Federal tariff | DBG Art. 214 |
| Personal deductions | DBG Art. 33, 33a, 35 |
| Filing | DBG Art. 124 |
| Penalties | DBG Art. 175 (evasion: 33.3%-300%) |

### Test Suite

**Test 1 -- Single, federal only.**
Input: Single, net income CHF 100,000, AHV CHF 10,000, Saule 3a CHF 7,258 (has BVG).
Expected: Taxable CHF 82,742. Apply Grundtarif. Federal tax ~CHF 3,500-4,000.

**Test 2 -- Married, joint.**
Input: Married, combined CHF 180,000, AHV CHF 12,000, Saule 3a CHF 14,516 total, 2 children.
Expected: Taxable ~CHF 140,084. Apply Verheiratetentarif.

**Test 3 -- Saule 3a without BVG.**
Input: Without BVG, net earned income CHF 200,000.
Expected: Max 20% = CHF 40,000 but capped CHF 36,288.

**Test 4 -- Saule 3a without BVG, income cap.**
Input: Without BVG, net earned CHF 30,000.
Expected: 20% x CHF 30,000 = CHF 6,000.

**Test 5 -- Low-value asset.**
Input: CHF 900 printer.
Expected: Immediate expense.

**Test 6 -- Cantonal question.**
Input: "How much tax in Zurich?"
Expected: ESCALATE. Federal only.

---

## PROHIBITIONS

- NEVER compute Swiss federal tax from approximate brackets -- use ESTV tariff tables
- NEVER apply Grundtarif to married or Verheiratetentarif to single
- NEVER estimate cantonal or municipal taxes -- FEDERAL ONLY
- NEVER allow Saule 3a above applicable maximum
- NEVER allow income tax as a deduction
- NEVER allow fines as deductions
- NEVER allow capital expenditure directly as expense
- NEVER present federal tax as total tax burden
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Treuhnder or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
