---
name: br-income-tax
description: >
  Use this skill whenever asked about Brazilian individual income tax for self-employed individuals (autônomos / profissionais liberais). Trigger on phrases like "how much tax do I pay in Brazil", "DIRPF", "IRPF", "Carnê-Leão", "livro caixa", "imposto de renda", "CPF", "income tax return Brazil", "deductible expenses Brazil", "self-employed tax Brazil", "desconto simplificado", "INSS autônomo", "pró-labore", "DAS MEI", or any question about filing or computing income tax for a self-employed or freelance client in Brazil. This skill covers the DIRPF annual return, Carnê-Leão monthly estimated payments, progressive IRPF brackets, livro caixa, allowable deductions, simplified deduction (20% discount), mandatory filing thresholds, INSS contributions, and penalties. ALWAYS read this skill before touching any Brazilian income tax work.
version: 2.0
---

# Brazilian Income Tax — Autônomo / Profissional Liberal (IRPF) v2.0

## Section 1 — Quick Reference

### IRPF Brackets 2025 (Calendar Year January–December 2025)

| Annual Taxable Income (BRL) | Rate | Dedução (Annual) |
|---|---|---|
| Up to 26,963.60 | Exempt | 0 |
| 26,963.61 – 33,919.80 | 7.5% | 2,022.17 |
| 33,919.81 – 45,012.60 | 15% | 4,566.23 |
| 45,012.61 – 55,976.16 | 22.5% | 7,942.19 |
| Over 55,976.16 | 27.5% | 10,740.98 |

**Formula (annual):** Tax = (taxable income × rate) − dedução

**Monthly Carnê-Leão brackets** (divide annual thresholds by 12, different monthly table published by Receita Federal each year — always confirm current Carnê-Leão monthly table).

### Desconto Simplificado (Simplified Deduction)

Taxpayers may elect the **desconto simplificado** instead of livro caixa deductions:
- Deduction: **20% of gross income**, capped at **BRL 16,754.34 per year**
- No receipts required
- Cannot be combined with livro caixa deductions
- Beneficial when actual expenses < 20% of gross

### Livro Caixa (Actual Expense Deduction)

Under livro caixa, actual documented professional expenses are deducted from gross Carnê-Leão income. Requires contemporaneous records. Replaces the 20% desconto simplificado (must choose one).

### INSS Contributions for Autônomos

| Contributor Type | Rate | Cap (2025) |
|---|---|---|
| Autônomo (contribuinte individual) | 20% | BRL 908.46/month (teto INSS: BRL 7,786.02 × 11.67%) |
| Empregador retaining autônomo | 20% (employer) | On each payment |
| Microempreendedor Individual (MEI) | Fixed DAS ~BRL 75/month | Separate regime |

INSS contributions paid are **fully deductible** from IRPF taxable income (livro caixa or as separate deduction in DIRPF).

### Carnê-Leão (Monthly Estimated Payments)

Autônomos who receive income from Brazilian individuals (pessoas físicas) or foreign sources must pay Carnê-Leão monthly by the last business day of the following month.

Income from legal entities (pessoas jurídicas) → PJ withholds 1.5% or 11% IRRF (depending on service type) — credit against annual DIRPF.

| Source | Monthly Obligation |
|---|---|
| Income from PF (individuals) or abroad | Carnê-Leão required |
| Income from PJ (companies) | IRRF withheld at source (1.5% + INSS 11%) |

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Desconto simplificado vs. livro caixa — unclear | Compare both: if actual expenses < 20% of gross, simplificado is better; present both |
| INSS withheld by PJ vs. paid by autônomo unclear | Flag — depends on whether client is PJ or PF |
| Payment from PJ: IRRF rate unclear | Apply 1.5% (professional services) as default; flag |
| Foreign income | Treat as Carnê-Leão obligatory; flag for treaty analysis |
| MEI vs. autônomo status unclear | Do NOT proceed — status determines entire regime |
| Cash income without Recibo / NF | Taxable — flag; Receita Federal audits cash-heavy returns |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Gross receipts > BRL 81,000/year | Was MEI? — MEI threshold BRL 81,000; exceeding triggers deregistration |
| No Carnê-Leão payments made | Check if all income was from PJs (withheld at source) |
| Total receipts > BRL 33,888 | DIRPF filing mandatory |
| INSS contributions appear zero | Verify — autônomos have INSS obligations |
| Single PJ source > 90% of income | May indicate employment relationship |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

Before computing Brazilian IRPF, collect:

1. **Total gross receipts** — from PF and PJ sources separately (monthly breakdown)
2. **IRRF withholding certificates (Comprovantes de Rendimentos)** — from each PJ client
3. **Carnê-Leão payments made** — monthly receipts (DARF codes 0190/5936)
4. **INSS contributions paid** — annual summary from INSS or GPS receipts
5. **Livro caixa or expense records** — if claiming actual expenses
6. **Bank statements** — 12 months (January–December)
7. **Deductions for dependants** — BRL 2,275.08 per dependant per year
8. **Health/education expenses** — for personal deductions (deduções de saúde/educação)
9. **Mortgage interest / financing** — if deducting (only on primary residence)
10. **Other income** — Categoria I (work), salary (se houver vínculo), rendimentos isentos

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-BR-1 | Client is MEI (Microempreendedor Individual) — not autônomo | Stop — MEI pays DAS (INSS + ICMS/ISS) not IRPF on business income; IRPF only on salary drawn; refer to MEI-specific skill |
| R-BR-2 | No Comprovantes de Rendimentos from PJ clients | Stop — cannot compute IRRF credit without withholding certificates |
| R-BR-3 | Income from abroad with no FX conversion | Stop — all amounts must be in BRL at date of receipt (Banco Central PTAX rate) |
| R-BR-4 | Mixed Simples Nacional / autônomo income | Flag — Simples Nacional company income flows differently; do not mix |
| R-BR-5 | Client claims no Carnê-Leão needed despite PF or foreign income | Flag — if any PF or foreign source, Carnê-Leão is mandatory; non-payment triggers multa |

---

## Section 3 — Transaction Pattern Library

### Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `TED DE [client name]` / `PIX DE [client]` | Gross receipts — IRPF income | Standard TED/PIX credit from client |
| I-02 | `PIX RECEBIDO [client]` | Gross receipts — IRPF income | PIX (instant payment) from client |
| I-03 | `DOC DE [client]` | Gross receipts — IRPF income | DOC (legacy inter-bank transfer) |
| I-04 | `STRIPE PAYOUT` / `STRIPE PAGAMENTOS` | Gross receipts — foreign-source | Stripe Brazil or foreign payout; Carnê-Leão if from foreign entity; BRL conversion at PTAX |
| I-05 | `PAYPAL SAQUE` / `PAYPAL TRANSFERÊNCIA` | Gross receipts — foreign-source | PayPal; Carnê-Leão applies; BRL conversion at PTAX |
| I-06 | `PAGAMENTO MERCADO PAGO` / `MERCADOPAGO` | Gross receipts — IRPF income | Mercado Pago settlement; net payout — gross-up if fees deducted |
| I-07 | `PAGAMENTO HOTMART` / `HOTMART SAQUE` | Gross receipts — IRPF income | Hotmart (digital products platform) payout; gross-up |
| I-08 | `KIWIFY SAQUE` / `EDUZZ PAGAMENTO` | Gross receipts — IRPF income | Brazilian digital product platforms; gross-up |
| I-09 | `NOTA FISCAL [number]` / `NF SERVIÇOS` | Gross receipts — PJ withholding | If from PJ, IRRF and INSS may have been withheld; cross-check with Comprovante |
| I-10 | `RESTITUIÇÃO IRPF RECEITA` | NOT income — IRPF refund | Restituição is not taxable income |
| I-11 | `RENDIMENTO POUPANÇA` / `JUROS CDB` | Rendimentos isentos (up to certain limits) or tributados | Bank interest: LCA/LCI may be exempt; CDB subject to IOF/IR — flag |
| I-12 | `DIVIDENDOS` (from company) | Isentos (if PJ distributing dividends under current rules) | Dividends currently exempt from IRPF in Brazil (under reform discussion — verify) |

### Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `ALUGUEL ESCRITÓRIO` / `ALUGUEL SALA COMERCIAL` | Rent — livro caixa deductible | Home office: proportional — requires documented calculation |
| E-02 | `ENERGIA ELÉTRICA` / `CONTA DE LUZ` / `CPFL` / `CEMIG` | Utilities — proportional deductible | Office proportion only; home = mixed |
| E-03 | `TELEFONE` / `INTERNET` / `VIVO` / `CLARO` / `TIM` / `OI` | Phone/internet — deductible (business portion) | Document business percentage |
| E-04 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — livro caixa deductible | Professional software |
| E-05 | `CONTADOR` / `ESCRITÓRIO CONTÁBIL` | Accounting fees — livro caixa deductible | Mandatory for many autônomos |
| E-06 | `PASSAGEM AÉREA` / `LATAM` / `GOL` / `AZUL` | Air travel — deductible (business purpose) | Require destination and purpose |
| E-07 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation — deductible (business travel) | Business purpose required |
| E-08 | `GUIA GPS` / `INSS GPS` / `CONTRIBUIÇÃO INSS` | INSS contributions — fully deductible | GPS payment code; or payroll withholding |
| E-09 | `DARF CARNÊ-LEÃO` / `DARF 0190` | Carnê-Leão payments — NOT deductible | Tax prepayments; credit against annual IRPF |
| E-10 | `DARF IRPF` / `SALDO DIRPF` | Annual tax payment — NOT deductible | Tax payment |
| E-11 | `SEGURO PROFISSIONAL` / `SEGURO RC PROFISSIONAL` | Professional insurance — livro caixa deductible | |
| E-12 | `PLANO DE SAÚDE` | Health insurance — personal deduction (DIRPF) | Not livro caixa — separate deduction in DIRPF Ficha de Deduções |
| E-13 | `ESCOLA` / `MENSALIDADE ENSINO` | Education — personal deduction (cap BRL 3,561.50/year) | Not livro caixa; DIRPF personal deduction |
| E-14 | `COMBUSTÍVEL` / `GASOLINA` / `POSTO` | Fuel — deductible (vehicle used professionally) | Document business km; mixed use = proportion |
| E-15 | `MATERIAL DE ESCRITÓRIO` / `PAPELARIA` | Office supplies — livro caixa deductible | |
| E-16 | `TARIFA BANCÁRIA` / `TED ENVIADO` / `IOF` | Bank fees — livro caixa deductible | Service charges on professional account |
| E-17 | `ASSINATURA [platform]` / `MENSALIDADE` | Platform/tool subscriptions — deductible | Professional tools |
| E-18 | `CURSOS` / `TREINAMENTO` / `CAPACITAÇÃO` | Training — livro caixa deductible | Professional development |
| E-19 | `REEMBOLSO [client]` | Non-deductible (offset against non-taxable reimbursement) | If client reimbursement, also reduce income accordingly |
| E-20 | `NOTA DE DÉBITO [supplier]` / `NF COMPRAS` | Purchases for professional activity — livro caixa deductible | Require NF-e |

---

## Section 4 — Worked Examples

### Example 1 — Itaú Unibanco (São Paulo, IT Consultant)

**Bank:** Itaú Unibanco PDF/CSV statement
**Client:** Carlos Mendes, IT consultant, São Paulo, mixed PJ and PF clients

```
Data;Histórico;Valor;Tipo
05/01/2025;PIX RECEBIDO EMPRESA ALPHA LTDA;7.500,00;C
15/01/2025;TARIFA BANCÁRIA;12,00;D
10/02/2025;PIX RECEBIDO STARTUP BETA LTDA;5.500,00;C
28/02/2025;GUIA GPS INSS;1.557,60;D
15/03/2025;STRIPE PAYOUT;4.200,00;C
31/03/2025;DARF CARNÊ-LEÃO 0190;850,00;D
20/04/2025;TED DE FREELANCER PF PESSOA;1.800,00;C
05/06/2025;PIX RECEBIDO GAMMA TECH SA;8.200,00;C
10/07/2025;CONTADOR SILVA LTDA;800,00;D
10/10/2025;LATAM VIAGEM NEGÓCIOS;650,00;D
```

**Step 1 — Income Classification**

| Narration | Type | Gross Amount | Notes |
|---|---|---|---|
| PIX DE EMPRESA ALPHA (PJ) | PJ income | BRL 7,500 | IRRF and INSS likely withheld — check Comprovante |
| PIX DE STARTUP BETA (PJ) | PJ income | BRL 5,500 | Same — check Comprovante |
| STRIPE PAYOUT | Foreign/PJ | BRL 4,200 | Carnê-Leão unless Stripe Brazil PJ withheld |
| TED DE FREELANCER PF | PF income | BRL 1,800 | Carnê-Leão mandatory |
| PIX DE GAMMA TECH (PJ) | PJ income | BRL 8,200 | Check Comprovante |

Assume Comprovantes show IRRF withheld from PJ clients at 1.5% each. Total PJ gross receipts (annualised): BRL 65,000; PF + foreign: BRL 24,000. Total: BRL 89,000.

**Step 2 — Livro Caixa vs. Desconto Simplificado**

Desconto simplificado: 20% × BRL 89,000 = BRL 17,800 → capped at BRL 16,754.34
Livro caixa (actual): INSS BRL 18,691.20, accounting BRL 9,600, software BRL 3,600, bank fees BRL 144, travel BRL 650 = BRL 32,685.20

Livro caixa > simplificado → **livro caixa preferred** for Carlos.

**Step 3 — Taxable Income**

```
Gross income:           BRL 89,000.00
Less livro caixa:       BRL 32,685.20
Taxable income:         BRL 56,314.80
```

**Step 4 — IRPF**

```
BRL 56,314.80 × 27.5% − BRL 10,740.98 = BRL 15,486.57 − BRL 10,740.98 = BRL 4,745.59
```

**Step 5 — Credits**

```
IRRF withheld by PJs (1.5% × BRL 65,000):     BRL 975.00
Carnê-Leão paid:                               BRL 850.00 × months paid
IRPF balance due:                              BRL 4,745.59 − BRL 975 − BRL [carnê total]
```

---

### Example 2 — Bradesco (Rio de Janeiro, Architect — Desconto Simplificado)

**Bank:** Bradesco statement
**Client:** Ana Lima, architect, Rio de Janeiro

Gross income: BRL 48,000 (all from PJ clients)
IRRF withheld by PJs: 1.5% × BRL 48,000 = BRL 720

Desconto simplificado: 20% × BRL 48,000 = BRL 9,600 (< cap) — apply
Taxable income: BRL 48,000 − BRL 9,600 = BRL 38,400

IRPF: BRL 38,400 × 22.5% − BRL 7,942.19 = BRL 8,640 − BRL 7,942.19 = **BRL 697.81**
Less IRRF credit: BRL 720

Result: **BRL 22.19 refund** (IRRF > IRPF)

Note: Also deduct INSS separately in DIRPF (Ficha de Deduções). If INSS BRL 6,000 paid:
Taxable: BRL 38,400 − BRL 6,000 = BRL 32,400
IRPF: BRL 32,400 × 15% − BRL 4,566.23 = BRL 4,860 − BRL 4,566.23 = BRL 293.77
With IRRF credit: **refund BRL 426.23**

---

### Example 3 — Banco do Brasil (Brasília, Doctor)

**Bank:** BB statement
**Client:** Dr. Paulo Saraiva, physician, Brasília, receives from PJ hospital and PF patients

PJ hospital income (Comprovante shows): BRL 120,000 gross; IRRF withheld 1.5% = BRL 1,800; INSS withheld 11% = BRL 13,200
PF patients (cash/PIX): BRL 36,000 — Carnê-Leão obligation

Livro caixa: INSS BRL 13,200 (employer-withheld) + own INSS BRL 5,400 (contribuição complementar) + clinic rent BRL 18,000 + equipment BRL 8,000 = BRL 44,600

Total gross: BRL 156,000
Less livro caixa: BRL 44,600
Taxable: BRL 111,400

IRPF: BRL 111,400 × 27.5% − BRL 10,740.98 = BRL 30,635 − BRL 10,740.98 = **BRL 19,894.02**
Less IRRF: BRL 1,800 and Carnê-Leão payments

High-income flag: BRL 156,000 gross → verify all Carnê-Leão monthly payments made on PF income; penalised if late.

---

### Example 4 — Nubank (São Paulo, Digital Creator / Hotmart)

**Bank:** Nubank statement (PDF)
**Client:** Julia Torres, digital course creator, São Paulo

Hotmart payouts: BRL 85,000 (after Hotmart fees)
Gross-up: Hotmart charges ~9.9% + BRL 1; effective gross ~BRL 95,000

Kiwify: BRL 22,000 net → gross ~BRL 24,500

Total gross: BRL 119,500 — all from platforms (PJ)

Note: Hotmart and Kiwify are Brazilian PJs. They withhold IRRF on payouts. Collect platform Comprovante de Rendimentos.

Desconto simplificado: 20% × BRL 119,500 = BRL 23,900 (< BRL 16,754.34 cap → apply cap BRL 16,754.34)
Livro caixa (actual expenses ~BRL 8,000): simplificado better (cap BRL 16,754 > actual)

Taxable: BRL 119,500 − BRL 16,754.34 = BRL 102,745.66

IRPF: BRL 102,745.66 × 27.5% − BRL 10,740.98 = BRL 28,254.56 − BRL 10,740.98 = **BRL 17,513.58**

Less IRRF from platforms. Flag: mandatory DIRPF filing (gross > BRL 33,888).

---

### Example 5 — Santander Brasil (Porto Alegre, Engineer)

**Bank:** Santander statement
**Client:** Ricardo Gomes, civil engineer, Porto Alegre

Issue: Ricardo has both autônomo income (BRL 60,000) and salary from CLT employer (BRL 48,000). The IRPF return must consolidate both.

DIRPF consolidation:
- Salary (DIRF from employer): BRL 48,000 gross; IRRF BRL 4,800 withheld
- Autônomo (livro caixa): BRL 60,000 − BRL 22,000 (expenses) = BRL 38,000

Total taxable: BRL 48,000 + BRL 38,000 = BRL 86,000
IRPF: BRL 86,000 × 27.5% − BRL 10,740.98 = BRL 23,650 − BRL 10,740.98 = **BRL 12,909.02**
Less IRRF salary: BRL 4,800 + Carnê-Leão paid + employer INSS

Dual income — flag: complex DIRPF with Ficha de Rendimentos from both sources.

---

### Example 6 — Inter Bank (Belo Horizonte, Freelance Designer, MEI Check)

**Bank:** Inter statement
**Client:** Fernanda Rocha, designer, Belo Horizonte

First question: **Is Fernanda a MEI?** If so, R-BR-1 applies — stop.

Assuming NOT MEI (deregistered or never registered as MEI):
Gross: BRL 72,000 — note: BRL 72,000 < MEI limit BRL 81,000. If Fernanda is still MEI, she should be taxed under DAS not IRPF on this income. STOP — confirm status.

If confirmed autônomo: proceed. INSS: BRL 14,400 (20% × BRL 72,000 — simplified estimate; actual depends on monthly ceiling). Desconto simplificado: BRL 14,400 vs. 20% cap BRL 14,400 (same). Actual expenses ~BRL 6,000. Use simplificado (BRL 14,400 > BRL 6,000).

Taxable: BRL 72,000 − BRL 14,400 = BRL 57,600
IRPF: BRL 57,600 × 27.5% − BRL 10,740.98 = BRL 15,840 − BRL 10,740.98 = **BRL 5,099.02**

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-BR-1 — INSS is always deductible**
INSS contributions paid (GPS, DARF, or withheld by PJ) are 100% deductible from IRPF taxable income. Deduct in the DIRPF Ficha de Deduções regardless of which income source (livro caixa or simplificado) is used. Apply without escalating.

**T1-BR-2 — IRRF withheld by PJ is a tax credit, not income reduction**
The IRRF withheld by client PJs (typically 1.5% for professional services, 11% INSS) reduces the annual IRPF balance payable. The gross income (before withholding) is the taxable figure. Always gross up to pre-withholding amount.

**T1-BR-3 — Carnê-Leão is mandatory for PF and foreign income**
Any monthly receipt from a Brazilian individual (PF) or from abroad — regardless of amount — triggers the Carnê-Leão obligation (due last business day of following month). Not paying creates multa de mora (0.33%/day up to 20%). Apply this rule immediately when classifying income sources.

**T1-BR-4 — DARF payments (Carnê-Leão, IRPF) are not deductible**
Tax prepayments made via DARF (code 0190 for Carnê-Leão, code 1854 for IRPF final balance) are credits against the annual IRPF liability, not deductible expenses. Never include DARF payments in livro caixa deductions.

**T1-BR-5 — Foreign income: PTAX conversion mandatory**
All income received in foreign currency must be converted to BRL using the Banco Central PTAX selling rate for the date of receipt. Do not use any other conversion rate.

**T1-BR-6 — Desconto simplificado cap: BRL 16,754.34**
The 20% simplificado deduction is capped at BRL 16,754.34 regardless of how large the gross income is. Always check the cap before applying the percentage.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-BR-1 | MEI vs. autônomo classification | Entire tax regime differs — MEI pays DAS; autônomo pays IRPF + INSS separately | Confirm registration at Portal do Empreendedor before proceeding |
| T2-BR-2 | Income from abroad (crypto, foreign clients) | Foreign income requires Carnê-Leão in BRL at PTAX; may trigger Imposto sobre Operações Financeiras (IOF) | Flag — PTAX conversion + Carnê-Leão on all foreign receipts |
| T2-BR-3 | Rental income (Renda de Aluguel) | Separate tax treatment; CARNÊ-Leão with different deductions | Flag — rental income separate Ficha; different deductions (IPTU, maintenance) |
| T2-BR-4 | Capital gains (Ganho de Capital) | Separate Programa GCAP; 15%/17.5%/20%/22.5% rates | Flag — do not include in Ficha de Rendimentos Tributáveis |
| T2-BR-5 | Crypto income / digital assets | RFB IN 1888/2019 and subsequent normatives; complex reporting | Flag — crypto gains taxed as capital gains; monthly apuração if gains > BRL 35,000/month |
| T2-BR-6 | Dividend income from own company | Currently exempt (under reform review) | Flag — verify current dividend exemption status before filing |

---

## Section 7 — Excel Working Paper Template

```
BRAZILIAN IRPF WORKING PAPER (AUTÔNOMO / PROFISSIONAL LIBERAL)
Taxpayer: _______________  CPF: _______________  FY: 2025 (Calendar Year)

SECTION A — INCOME (Rendimentos Tributáveis)
                                        BRL
PJ clients — gross (pre-IRRF):        ___________
PF clients / Carnê-Leão income:       ___________
Foreign income (converted PTAX):       ___________
Platform payouts (grossed up):         ___________
TOTAL GROSS INCOME                     ___________

SECTION B — DEDUCTION METHOD
[ ] Desconto Simplificado: 20% × gross = ___________  (cap: BRL 16,754.34)
[ ] Livro Caixa (actual expenses):

  Rent (professional share):           ___________
  Utilities (professional):            ___________
  Phone/internet (business %):         ___________
  Software:                            ___________
  Accounting fees:                     ___________
  Travel (professional):               ___________
  Equipment/supplies:                  ___________
  Other documented expenses:           ___________
  TOTAL LIVRO CAIXA:                   ___________

SECTION C — INSS DEDUCTION (separate from above)
INSS paid (GPS / withheld by PJ):      ___________

SECTION D — TAXABLE INCOME
Gross − [B] − [C] (+ other DIRPF deductions):  ___________

SECTION E — IRPF CALCULATION
Tax at bracket rates:                  ___________
Less: IRRF withheld by PJs:            (___________)
Less: Carnê-Leão payments (DARF 0190): (___________)
IRPF BALANCE DUE / (REFUND)            ___________

SECTION F — REVIEWER FLAGS
[ ] All Comprovantes de Rendimentos collected from PJ clients?
[ ] Carnê-Leão payments reconciled (PF and foreign income months)?
[ ] Foreign income converted at PTAX selling rate on receipt date?
[ ] MEI status confirmed as NOT applicable?
[ ] Desconto simplificado vs. livro caixa comparison done?
[ ] INSS deduction entered in Ficha de Deduções (not livro caixa)?
[ ] Gross-up applied for platform payouts (Hotmart, Kiwify, etc.)?
```

---

## Section 8 — Bank Statement Reading Guide

### Itaú Unibanco
- Export: PDF or CSV via "Extrato" in app/portal
- CSV columns: `Data;Histórico;Valor;Tipo` (Tipo: C = crédito, D = débito)
- Amount format: comma decimal, period thousands (e.g., `7.500,00`)
- Date: DD/MM/YYYY
- PIX receipts: `PIX RECEBIDO [sender name]`; TED receipts: `TED DE [sender]`

### Bradesco
- Export: CSV or PDF from Internet Banking Bradesco
- Columns: `Data;Documento;Histórico;Valor;Saldo`
- Positive Valor = credit; negative = debit (parentheses or negative sign)

### Banco do Brasil
- Export: CSV from BB Internet Banking ("Extrato")
- Columns vary; typically `Data;Lançamento;Débito;Crédito;Saldo`
- PIX narrations: `PIX TRANSF DE [CPF/name]` or `PIX CRED DE [name]`

### Santander Brasil
- Export: PDF/CSV from Santander Online (portal/app)
- Standard format; PIX: `TRANSF PIX DE [name]`, TED: `TED/DOC RECEBIDA`

### Nubank
- Export: PDF statement from app ("Ver extrato completo" → PDF)
- No native CSV; third-party tools exist; narrations include: `Pix recebido de [name]`, `Transferência recebida de [name]`

### Inter Bank (Banco Inter)
- Export: CSV/PDF from Inter app → "Extrato" → "Baixar"
- Columns: `Data;Tipo de Transação;Valor`
- PIX: `Pix Recebido` with sender detail in description

### PIX Identification
- PIX is the Brazilian instant payment system; identifies transactions by CPF/CNPJ/phone/email key
- Bank statement PIX narrations: `PIX RECEBIDO`, `PIX CREDIT`, `TRANSF PIX ENTRADA`
- Sender's name/CPF usually included — critical for classifying PF (→ Carnê-Leão) vs. PJ (→ IRRF withheld)

---

## Section 9 — Onboarding Fallback

**Missing Comprovantes de Rendimentos:**
> "To accurately compute your IRPF, I need the Comprovante de Rendimentos from every PJ client who paid you in 2025. These documents show the gross amount and the IRRF withheld at source. You can request them directly from your clients, or check your Receita Federal account at gov.br/receitafederal → 'Consultar Informações Prestadas por Terceiros' — your clients' DIMEs/DIRFs may already be on file."

**MEI status verification:**
> "Before I can proceed, I need to confirm whether you are registered as a Microempreendedor Individual (MEI). If yes, your business income is taxed under the DAS regime, not standard IRPF, and a different skill applies. Please check your status at portaldoempreendedor.gov.br or inform me of your CNPJ if you have one."

**Carnê-Leão gap:**
> "I see you received income from individual clients (PF) or from abroad, which triggers the Carnê-Leão obligation. Do you have records of your monthly DARF payments (code 0190)? If Carnê-Leão was not paid in any month where PF/foreign income was received, a multa de mora applies. Let's identify which months had gaps."

**Foreign income FX:**
> "For income received from foreign clients in USD or other currencies, I need to convert each receipt to BRL using the Banco Central PTAX selling rate for the exact date of receipt. Could you provide the dates and foreign currency amounts? Alternatively, if you received income regularly, the annual average PTAX rate can be used — confirm if this is acceptable."

---

## Section 10 — Reference Material

### Key Legislation
- **RIR/2018 (Regulamento do Imposto de Renda)** — Decreto 9.580/2018
- **Lei 7.713/1988** — income exempt from IRPF
- **IN RFB 2.178/2024** — Carnê-Leão and DIRPF rules for 2024 calendar year
- **Instrução Normativa RFB 1.888/2019** — crypto assets reporting

### Filing and Payment Calendar 2025 (FY 2024)
| Deadline | Event |
|---|---|
| Last business day each month | Carnê-Leão DARF due for prior month receipts |
| 28 February 2025 | PJ clients must issue Comprovantes de Rendimentos |
| 31 March 2025 | DIRPF 2025 (base year 2024) filing opens |
| 30 May 2025 | DIRPF 2025 filing deadline |
| 30 May 2025 | 1st instalment of IRPF balance (or single payment for discount) |

### Useful References
- Receita Federal: gov.br/receitafederal
- PGFN (voluntary disclosure): gov.br/pgfn
- PIX chave lookup: bacen.gov.br
- PTAX rates: bcb.gov.br/estabilidadefinanceira/fechamentodolar
