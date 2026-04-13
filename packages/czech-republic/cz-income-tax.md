---
name: cz-income-tax
description: >
  Use this skill whenever asked about Czech income tax for self-employed individuals (OSVČ). Trigger on phrases like "how much tax do I pay", "DPFO", "daňové přiznání", "income tax return", "výdajové paušály", "expense lump-sums", "paušální daň", "flat-rate tax", "sleva na dani", "tax credits", "self-employed tax Czech", or any question about filing or computing income tax for a self-employed or freelance client in the Czech Republic. ALWAYS read this skill before touching any Czech income tax work.
version: 2.0
jurisdiction: CZ
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Czech Republic Income Tax (DPFO) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Czech Republic (Česká republika) |
| Tax type | Daň z příjmů fyzických osob (DPFO -- personal income tax) |
| Primary legislation | Zákon č. 586/1992 Sb., o daních z příjmů |
| Supporting legislation | Zákon č. 589/1992 Sb. (social insurance); Zákon č. 592/1992 Sb. (health insurance); Zákon č. 540/2020 Sb. (paušální daň) |
| Tax authority | Finanční správa (Financial Administration) |
| Filing portal | EPO / Daňový portál |
| Currency | CZK only |
| Tax rates | 15% up to CZK 1,676,052; 23% above |
| Basic taxpayer credit | CZK 30,840/year (na poplatníka) |
| Expense lump-sums | 80%/60%/40%/30% depending on activity |
| Paušální daň | CZK 7,498--27,139/month (all-in) |
| Filing deadline (paper) | 1 April |
| Filing deadline (electronic) | 1 May |
| Filing deadline (via daňový poradce) | 1 July |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Czech daňový poradce sign-off |
| Validation date | Pending |

**Expense methods at a glance:**

| Activity | Lump-sum % | Cap (CZK) |
|---|---|---|
| Agriculture, craft trades (řemeslné živnosti) | 80% | 1,600,000 |
| Other trades (živnostenské podnikání) | 60% | 1,200,000 |
| Professional services (§ 7/1c, 7/2) | 40% | 800,000 |
| Rental of business property (§ 9) | 30% | 600,000 |

**Tax credits (slevy na dani, § 35ba):**

| Credit | Annual CZK |
|---|---|
| Basic taxpayer (na poplatníka) | 30,840 |
| Spouse (caring for child under 3) | 24,840 |
| Disability I/II | 2,520 |
| Disability III | 5,040 |
| ZTP/P holder | 16,140 |
| Student | 4,020 |
| 1st child | 15,204 |
| 2nd child | 22,320 |
| 3rd+ child | 27,840 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown expense method | STOP -- must determine before computing |
| Unknown expense category | Not deductible |
| Unknown business-use proportion | 0% business use |
| Unknown activity type for lump-sum | STOP -- rate depends on activity |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the tax year. Acceptable from: ČSOB, Komerční banka, Fio banka, Česká spořitelna, Raiffeisenbank, MONETA Money Bank, or fintech (Revolut, Wise).

**Recommended** -- sales invoices, purchase invoices (if real expenses), expense method choice, živnostenský list (trade licence).

**Ideal** -- complete daňová evidence or accounting records, prior year DPFO, Přehled ČSSZ/VZP.

### Refusal catalogue

**R-CZ-1 -- s.r.o. or a.s.** *Trigger:* client operates through a legal entity. *Message:* "This skill covers OSVČ only. s.r.o. files corporate income tax. Please use a separate skill."

**R-CZ-2 -- International income / tax treaties.** *Trigger:* significant foreign income. *Message:* "International income is outside scope. Consult a daňový poradce."

**R-CZ-3 -- Crypto taxation.** *Trigger:* significant crypto trading. *Message:* "Crypto classification is evolving. Escalate to daňový poradce."

**R-CZ-4 -- Expense method unknown.** *Trigger:* client has not confirmed real/lump-sum/paušální. *Message:* "I cannot compute without knowing your expense method. Please confirm."

---

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 Czech banks (fees and interest)

| Pattern | Treatment | Notes |
|---|---|---|
| ČSOB, ČESKOSLOVENSKÁ OBCHODNÍ BANKA | Bank charges: deductible (if real expenses) | Monthly fees |
| KOMERČNÍ BANKA, KB | Bank charges: deductible | Same |
| FIO BANKA, FIO | Bank charges: deductible | Same |
| ČESKÁ SPOŘITELNA, ČS | Bank charges: deductible | Same |
| RAIFFEISENBANK | Bank charges: deductible | Same |
| MONETA MONEY BANK | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| ÚROK, INTEREST (credit) | EXCLUDE from § 7 | Interest = § 8 capital income |
| ÚROK, INTEREST (debit) | Deductible if business loan | Personal: EXCLUDE |
| SPLÁTKA ÚVĚRU (loan repayment) | EXCLUDE | Principal movement |

### 3.2 Czech government and statutory bodies

| Pattern | Treatment | Notes |
|---|---|---|
| FINANČNÍ ÚŘAD, FÚ | EXCLUDE | Tax payment |
| ČSSZ (social insurance) | NOT deductible from income tax base | Social insurance ≠ income deduction |
| VZP, OBOROVÁ ZP, ZPMV (health insurance) | NOT deductible from income tax base | Health insurance ≠ income deduction |
| ŽIVNOSTENSKÝ ÚŘAD | Deductible | Trade licence fees |
| Czech POINT | Deductible | Administrative fees |

### 3.3 Czech utilities and telecoms

| Pattern | Treatment | Notes |
|---|---|---|
| ČEZ, E.ON, PRE | Deductible if business premises | Electricity; apportion if home |
| INNOGY, PRAŽSKÁ PLYNÁRENSKÁ | Deductible if business premises | Gas |
| T-MOBILE CZ, O2, VODAFONE CZ | Deductible: business phone/internet | Mixed: apportion |
| UPC, UNET | Deductible: business internet | Mixed: apportion |

### 3.4 SaaS and software -- international

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | IE/LU entities | Deductible expense | Reverse charge DPH |
| GITHUB, OPENAI, ANTHROPIC | US entities | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Various | Deductible expense | Check entity |

### 3.5 Professional services (Czech)

| Pattern | Treatment | Notes |
|---|---|---|
| ÚČETNÍ, ÚČETNICTVÍ | Deductible | Accounting fees |
| ADVOKÁT, PRÁVNÍK | Deductible if business | Legal fees |
| DAŇOVÝ PORADCE | Deductible | Tax advisory |
| NOTÁŘ | Deductible if business | Notary fees |

### 3.6 Transport and travel

| Pattern | Treatment | Notes |
|---|---|---|
| ČESKÉ DRÁHY, ČD | Deductible if business travel | Train |
| REGIOJET, LEO EXPRESS | Deductible if business travel | Private rail |
| LÍTAČKA, DPP (Prague transport) | Deductible if business travel | Public transport |
| MOL, BENZINA, OMV, SHELL CZ | Deductible: business portion only | Fuel |
| LETADLO, RYANAIR, WIZZAIR | Deductible if business travel | Flights |

### 3.7 Office and supplies

| Pattern | Treatment | Notes |
|---|---|---|
| ALZA.CZ, CZC.CZ, DATART | Capital if significant; else expense | IT equipment |
| IKEA CZ, HORNBACH | Capital or expense depending on value | Office items |
| ČESKÁ POŠTA | Deductible | Postage |

### 3.8 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| ALBERT, TESCO, KAUFLAND, LIDL CZ, BILLA | Default: NOT deductible | Personal provisioning |
| RESTAURACE (any restaurant) | Deductible if documented business purpose | Document attendees and purpose |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| VLASTNÍ PŘEVOD, OWN TRANSFER | EXCLUDE | Internal movement |
| VÝBĚR, ATM | EXCLUDE (default: drawings) | Ask what cash used for |
| VKLAD | EXCLUDE | Owner deposit |

---

## Section 4 -- Worked examples

### Example 1 -- IT freelancer, 40% lump-sum

**Input:** Revenue CZK 1,200,000, 40% lump-sum (professional services), single.
**Computation:** Lump-sum = CZK 480,000. Tax base = CZK 720,000. Tax at 15% = CZK 108,000. Less basic credit CZK 30,840. Final tax = CZK 77,160.

### Example 2 -- Paušální daň eligibility

**Input:** Revenue CZK 900,000, not VAT registered, no employees, no partnership.
**Result:** Eligible for Band 1. Monthly payment CZK 7,498. Annual = CZK 89,976. No DPFO filing.

### Example 3 -- Lump-sum cap hit

**Input:** IT freelancer (40%), revenue CZK 2,500,000. Real expenses CZK 1,100,000.
**Lump-sum:** 40% = CZK 1,000,000, capped at CZK 800,000. Tax base = CZK 1,700,000.
**Real expenses:** CZK 1,100,000. Tax base = CZK 1,400,000.
**Conclusion:** Real expenses save CZK 300,000 in tax base. Recommend real expenses.

### Example 4 -- Parent with tax bonus

**Input:** Single parent, revenue CZK 400,000, 40% lump-sum, 3 children.
**Computation:** Tax base = CZK 240,000. Tax = CZK 36,000. Less basic CZK 30,840 = CZK 5,160. Less child credits CZK 65,364. Tax bonus (refund) = CZK 60,204 (capped at CZK 60,300).

---

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Tax rates
15% on first CZK 1,676,052 of tax base. 23% above. No tax-free band -- zero tax achieved through basic credit. **Legislation:** § 16.

### 5.2 Expense lump-sums
Cannot combine lump-sum and real expenses for the same activity. Lump-sum users need not keep expense receipts but MUST keep income records. **Legislation:** § 7 odst. 7.

### 5.3 Paušální daň
Single monthly payment (tax + social + health). Eligibility: revenue up to CZK 2,000,000, not VAT payer, no employees, no partnership, main activity. Registration by 10 January. No DPFO filing. **Legislation:** Zákon č. 540/2020 Sb.

### 5.4 Social and health insurance
Assessment base = 50% of § 7 partial tax base. Social: 29.2%. Health: 13.5%. NOT deductible from income tax base. **Legislation:** Zákon č. 589/1992, 592/1992.

### 5.5 Loss carry-forward
5 years. Only available with real expenses -- not lump-sum. **Legislation:** § 34.

### 5.6 Non-taxable deductions (§ 15)
Mortgage interest (max CZK 150,000), pension contributions (max CZK 24,000), life insurance (max CZK 24,000), charity (min CZK 1,000 or 2% of base, max 15%).

---

## Section 6 -- Tier 2 catalogue

### 6.1 Choosing real vs lump-sum expenses
*Why:* Depends on actual expense level vs lump-sum cap. *Default:* Present both computations. *Question:* "What are your total documented business expenses?"

### 6.2 Switching expense methods (transition adjustment)
*Why:* Receivables/payables must be adjusted. *Default:* Flag for reviewer. *Question:* "Did you switch from lump-sum to real expenses (or vice versa) this year?"

### 6.3 Spouse credit eligibility
*Why:* Since 2025, only when caring for child under 3. *Default:* Do not apply without confirmation. *Question:* "Do you care for a child under 3?"

### 6.4 VAT registration forcing paušální exit
*Why:* VAT registration terminates paušální daň. *Default:* If VAT-registered, paušální invalid. *Question:* "Are you VAT registered or approaching the CZK 2,000,000 threshold?"

---

## Section 7 -- Excel working paper template

### Sheet "Transactions"
Columns: Date, Counterparty, Description, Amount (CZK), Category (Revenue/Expense/Depreciation/EXCLUDE), Deductible amount, Default?, Question, Notes.

### Sheet "Tax Computation"
Step-by-step per Section 5, branching by expense method.

---

## Section 8 -- Bank statement reading guide

**CSV formats.** ČSOB uses semicolons with DD.MM.YYYY. Komerční banka uses CSV with various delimiters. Fio banka offers clean CSV with YYYY-MM-DD. Common columns: Datum (Date), Protiúčet (Counterparty), Částka (Amount), Poznámka (Note).

**Czech language variants.** Common: příjem (income), výdaj (expense), poplatek (fee), úrok (interest), převod (transfer), vklad (deposit), výběr (withdrawal).

**Insurance payments.** ČSSZ (social) and health insurance payments are separate from income tax. They are NOT deductible from the income tax base (unlike Poland).

---

## Section 9 -- Onboarding fallback

### 9.1 Entity type
*Inference:* OSVČ from bank account type. *Fallback:* "Are you OSVČ or operating through an s.r.o.?"

### 9.2 Expense method
*Inference:* Not inferable. Always ask. *Fallback:* "Real expenses, lump-sum, or paušální daň?"

### 9.3 Activity type
*Inference:* From counterparty mix. *Fallback:* "What is your živnost type? Řemeslná, volná, or professional?"

### 9.4 VAT status
*Inference:* DPH payments in statement. *Fallback:* "Are you a DPH payer?"

### 9.5 Family status
*Inference:* Not inferable. *Fallback:* "Married? Children? (Affects credits.)"

---

## Section 10 -- Reference material

### Test suite

**Test 1 -- IT freelancer, lump-sum.** Revenue CZK 1,200,000, 40%, single. Tax = CZK 77,160.
**Test 2 -- Craftsman near cap.** Revenue CZK 2,200,000, 80%, cap CZK 1,600,000. Tax = CZK 59,160.
**Test 3 -- High earner, 23% band.** Revenue CZK 4,000,000, real expenses CZK 1,500,000. Tax = CZK 410,076.
**Test 4 -- Paušální daň.** Revenue CZK 900,000. Band 1, CZK 89,976/year.
**Test 5 -- Tax bonus.** Parent, 3 children, CZK 400,000 revenue, 40% lump-sum. Bonus CZK 60,204.

### Edge case registry

**EC1 -- Lump-sum cap exceeded.** Apply cap, not computed percentage.
**EC2 -- Paušální daň revenue exceeded.** Band shift or full exit.
**EC3 -- VAT forces paušální exit.** Must file standard DPFO.
**EC4 -- Employment + freelance combined.** Both partial bases on one return.
**EC5 -- Student + parent credits.** Both claimable (separate credits).
**EC6 -- Expense method switch.** Transition adjustment mandatory.
**EC7 -- Losses with lump-sum.** Cannot carry forward losses under lump-sum.
**EC8 -- Health insurance minimum.** Must pay minimum even if below threshold.

### Prohibitions

- NEVER compute without determining expense method
- NEVER exceed lump-sum caps
- NEVER file DPFO for valid paušální daň taxpayer
- NEVER apply basic credit more than once
- NEVER allow both parents to claim same child credit
- NEVER treat social/health insurance as income tax deductible
- NEVER carry forward losses under lump-sum expenses
- NEVER advise on crypto, international structures, or tax treaties
- NEVER present calculations as definitive
- NEVER skip transition adjustment when switching expense methods

### Sources

1. Zákon č. 586/1992 Sb. (Income Tax Act)
2. Zákon č. 540/2020 Sb. (Paušální daň)
3. Zákon č. 589/1992 Sb. (Social insurance)
4. Zákon č. 592/1992 Sb. (Health insurance)
5. Finanční správa -- https://www.financnisprava.cz

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a daňový poradce or equivalent licensed practitioner in the Czech Republic) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
