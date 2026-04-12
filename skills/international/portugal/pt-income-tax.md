---
name: pt-income-tax
description: >
  Use this skill whenever asked about Portuguese individual income tax (IRS) for self-employed individuals (trabalhadores independentes). Trigger on phrases like "how much tax do I pay in Portugal", "IRS Portugal", "Modelo 3", "Anexo B", "Categoria B", "regime simplificado", "contabilidade organizada", "retenção na fonte", "trabalhador independente", "recibos verdes", "income tax return Portugal", "NIF", "coeficientes regime simplificado", "IRS Jovem", "adicional de solidariedade", or any question about filing or computing income tax for a self-employed or freelance client in Portugal. This skill covers the Modelo 3 + Anexo B annual return, Categoria B income, regime simplificado vs contabilidade organizada, progressive IRS brackets, adicional de solidariedade, allowable deductions, withholding (retenção na fonte), IRS Jovem, and filing deadlines. ALWAYS read this skill before touching any Portuguese income tax work.
version: 2.0
---

# Portuguese Income Tax — Trabalhador Independente (IRS Categoria B) v2.0

## Section 1 — Quick Reference

### IRS Brackets 2025 (Categoria B — Regime Simplificado)

| Taxable Income (EUR) | Rate | Cumulative Tax |
|---|---|---|
| 0 – 7,703 | 13.25% | 1,020.65 |
| 7,703 – 11,623 | 18% | 1,726.25 |
| 11,623 – 16,472 | 23% | 2,841.72 |
| 16,472 – 21,321 | 26% | 4,102.46 |
| 21,321 – 27,146 | 32.75% | 6,010.17 |
| 27,146 – 39,791 | 37% | 10,698.82 |
| 39,791 – 51,997 | 43.5% | 16,011.53 |
| 51,997 – 81,199 | 45% | 29,141.53 |
| Over 81,199 | 48% | — |

**Formula:** Tax = cumulative tax for lower bracket + (income − lower bracket threshold) × marginal rate

### Adicional de Solidariedade (Solidarity Surcharge)

| Taxable Income (EUR) | Rate |
|---|---|
| 80,000 – 250,000 | 2.5% on excess above EUR 80,000 |
| Over 250,000 | 2.5% on EUR 170,000 + 5% on excess above EUR 250,000 |

### Regime Simplificado — Coeficientes 2025

Under regime simplificado, taxable income = gross receipts × applicable coefficient (not actual expenses):

| Type of Income | Coefficient | Effective Tax Base |
|---|---|---|
| Sales of goods (vendas) | 0.15 | 15% of gross |
| Provision of services — general (prestação de serviços) | 0.35 | 35% of gross |
| Professional services (art. 151 CIRS — listed professions: lawyers, doctors, engineers, architects, consultants) | 0.35 | 35% of gross |
| Hotel/accommodation/tourism | 0.15 | 15% of gross |
| Other income Categoria B | 0.95 | 95% of gross |
| Intellectual property (if author is original creator) | 0.50 | 50% of gross |

**Note:** Regime simplificado is available only when gross receipts in the prior year (or estimated current year for new entrants) ≤ EUR 200,000.

### Regime de Contabilidade Organizada (Actual Expenses)

When gross receipts > EUR 200,000 (mandatory) or by election: taxable income = gross receipts − actual deductible expenses (requires certified accountant / TOC).

### Retenção na Fonte (Withholding by Clients)

| Recipient Type | Rate |
|---|---|
| General trabalhador independente — Categoria B | 25% |
| Profissões de elevado valor acrescentado (NHR/IFICI list) | Special rates |
| Non-resident (Categoria B) | 25% |

Clients paying a trabalhador independente with NIF must withhold 25% and remit to AT. The withheld amount is credited against final IRS liability.

**Isenção de retenção na fonte:** Taxpayers whose prior-year gross Categoria B income ≤ EUR 12,500 may submit declaration to clients to waive withholding.

### Segurança Social (Social Security Contributions)

| Scheme | Rate | Base |
|---|---|---|
| Trabalhador independente SS | 21.4% | 70% of quarterly gross receipts / 3 (monthly base) |
| Minimum monthly base | EUR 501.87 | If income very low |

SS contributions are deductible from IRS taxable income (reduce gross before applying coefficient, or deducted as expense in contabilidade organizada).

### IRS Jovem (Youth IRS Exemption)

For taxpayers ≤ 35 years old (first 10 years of earning income in Portugal after completing education):

| Year | Exemption from Tax |
|---|---|
| Years 1–3 | 100% exempt (capped at EUR 28,737/year) |
| Years 4–6 | 75% exempt |
| Years 7–9 | 50% exempt |
| Year 10 | 25% exempt |

Confirm eligibility before applying. IRS Jovem applies on IRS brackets; SS contributions still apply.

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Service type unclear (goods vs services) | Apply coefficient 0.35 (services) — higher tax base; flag for client |
| Regime simplificado vs. contabilidade organizada | Regime simplificado (default for < EUR 200,000 receipts) |
| IRS Jovem eligibility unclear | Do NOT apply — flag for client to confirm eligibility years |
| NHR/IFICI status unclear | Do NOT apply special rates — apply standard brackets |
| SS contributions not provided | Estimate at 21.4% × 70% of gross; flag as estimated |
| Retenção na fonte amounts not confirmed | Do NOT assume — require withholding certificates from clients |
| Expense claimed under contabilidade organizada without receipt | Reject — cannot deduct without evidence |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Gross receipts > EUR 200,000 | Mandatory contabilidade organizada — stop if still on simplificado |
| Single client providing > 80% of receipts | Requalification risk as employment (falso recibo verde) |
| No retenções na fonte received but clients are companies | Verify — companies must withhold 25% |
| SS contributions appear absent or very low | Verify SS base calculation |
| IRS Jovem claimed beyond year 10 | Ineligible — flag immediately |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

Before computing Portuguese IRS, collect:

1. **Total gross receipts** (recibos verdes issued and received) — full Categoria B gross
2. **Client breakdown** — to identify service type and applicable coefficient
3. **Withholding certificates (declarações de retenção)** — from each client
4. **SS contribution payments** — quarterly SS payment receipts
5. **Regime status** — simplificado or contabilidade organizada (if elected)
6. **IRS Jovem status** — age + year number in Portugal income earnings
7. **Bank statements** — 12 months of the fiscal year
8. **NHR or IFICI status** — if non-habitual resident rules apply
9. **Other income categories** — Categoria A (employment), Categoria F (rental), Categoria G (capital gains)
10. **Marital status + dependants** — for quociente conjugal and deductions for dependants

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-PT-1 | Gross receipts > EUR 200,000 but client insists on regime simplificado | Stop — mandatory contabilidade organizada; TOC (certified accountant) required |
| R-PT-2 | NHR/IFICI status claimed but no AT registration confirmation | Do not apply NHR rates — request IFICI/NHR registration number |
| R-PT-3 | No retenção certificates but client paid by Portuguese companies | Flag — companies legally required to withhold 25%; gather certificates before finalising |
| R-PT-4 | Falso recibo verde risk (single client > 80% of receipts, regular schedule) | Flag — AT may reclassify as employment (Categoria A); advise legal review |
| R-PT-5 | Contabilidade organizada without a TOC certified accountant | Stop — contabilidade organizada legally requires a TOC signature; cannot proceed without one |

---

## Section 3 — Transaction Pattern Library

### Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `TRANSF DE [client name]` / `TRF DE [client]` | Gross receipts — Categoria B | Standard SEPA transfer from client |
| I-02 | `MB WAY [client]` / `MBWAY RECEBIDO` | Gross receipts — Categoria B | MBWay (Portuguese digital payment) from client |
| I-03 | `STRIPE PAYMENTS EUROPE` / `STRIPE PAYOUT` | Gross receipts — gross-up | Stripe net payout; gross-up to pre-fee; fee deductible |
| I-04 | `PAYPAL TRANSFER` / `PAYPAL RECEBIDO` | Gross receipts — gross-up | PayPal net payout; gross-up; fee deductible |
| I-05 | `TRANSFERÊNCIA RECEBIDA [client]` | Gross receipts — Categoria B | Generic bank transfer credit |
| I-06 | `IFTHENPAY PAYOUT` / `EUPAGO SETTLEMENT` | Gross receipts — gross-up | Portuguese payment gateway settlement |
| I-07 | `RETENÇÃO NA FONTE` (separate line or annotation) | Withholding credit | Gross-up: receipt = net after 25% withholding → gross = receipt / 0.75 |
| I-08 | `REEMBOLSO IRS AT` / `REEMBOLSO AT` | NOT income — tax refund | AT tax refund; not Categoria B income |
| I-09 | `DEVOLUÇÃO` / `REEMBOLSO [client]` | Non-taxable if client reimbursement | Must be documented; otherwise taxable |
| I-10 | `JUROS RECEBIDOS` / `JUROS CONTA` | Categoria E (capital income) | Not Categoria B — separate IRS treatment |

### Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `RENDA` / `ARRENDAMENTO ESCRITÓRIO` | Rent — deductible (contabilidade organizada only) | Regime simplificado: actual expenses not deductible (coefficient applies) |
| E-02 | `EDP` / `GALP ENERGIA` / `ENDESA` / `IBERDROLA` | Utilities — deductible (contab. organizada only) | Not deductible under regime simplificado |
| E-03 | `MEO` / `NOS` / `VODAFONE PT` / `NOWO` | Phone/internet — deductible (contab. organizada) | Regime simplificado: N/A |
| E-04 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — deductible (contab. organizada) | Regime simplificado: N/A |
| E-05 | `SEGURANÇA SOCIAL` / `TAXA SS` | SS contributions — deductible | Both regimes: SS contributions reduce IRS taxable income |
| E-06 | `CONTABILISTA` / `TOC` / `ROC` | Accountant fees — deductible (contab. organizada) | Required for contabilidade organizada |
| E-07 | `CP COMBOIO` / `COMBOIOS DE PORTUGAL` | Train travel — deductible (contab. organizada) | Business travel; require purpose note |
| E-08 | `TAP AIR PORTUGAL` / `RYANAIR` / `EASYJET` | Air travel — deductible (contab. organizada) | Business travel; require itinerary |
| E-09 | `SEGURO PROFISSIONAL` / `SEGURO RC` | Professional insurance — deductible | Both regimes (when specifically professional) |
| E-10 | `AT PAGAMENTO IRS` / `LIQUIDAÇÃO IRS` | IRS payment — NOT deductible | Tax payments are not expenses |
| E-11 | `AT IVA PAGAMENTO` / `IVA ENTREGUE` | VAT payment — NOT deductible | IVA is separate; not IRS expense |
| E-12 | `BANCO [name] COMISSÕES` / `COMISSÃO BANCÁRIA` | Bank fees — deductible (contab. organizada) | Business account commissions |
| E-13 | `FORMAÇÃO` / `CURSO` / `WORKSHOP` | Training — deductible (contab. organizada) | Professional development |
| E-14 | `COMBUSTÍVEL` / `GALP` / `BP` / `REPSOL` | Fuel — deductible (contab. organizada, partial) | Vehicle expenses: document business use |
| E-15 | `MBNET` / `TRANSFERÊNCIA MB` / `MULTIBANCO` | Generic payment — classify by purpose | Identify payee from bank detail; classify accordingly |
| E-16 | `SEGURO SAÚDE` / `MÉDIS` / `MULTICARE` | Health insurance — IRS deduction (Anexo H) | Not a Categoria B expense — separate personal deduction in Anexo H |
| E-17 | `DESCONTO RECIBO VERDE` / `RETENÇÃO CLIENTE` | Withholding by client (25%) | Not an expense — credit against IRS; verify with certificate |

---

## Section 4 — Worked Examples

### Example 1 — Millennium BCP (Lisbon, Consultant — Regime Simplificado)

**Bank:** Millennium BCP statement (PDF/CSV)
**Client:** Ana Ferreira, management consultant, Lisbon, NIF registered, regime simplificado

```
Data;Descrição;Débito;Crédito;Saldo
05/01/2025;TRANSF DE EMPRESA ALPHA LDA;;3.750,00;
31/01/2025;COMISSÃO BANCÁRIA;4,50;;
10/02/2025;TRANSF DE STARTUP BETA LDA;;2.500,00;
28/02/2025;SEGURANÇA SOCIAL;350,00;;
15/03/2025;TRANSF DE GAMMA CONSULTING LDA;;4.200,00;
31/03/2025;SEGURANÇA SOCIAL;350,00;;
05/04/2025;STRIPE PAYMENTS EUROPE;;1.920,00;
30/04/2025;SEGURANÇA SOCIAL;350,00;;
15/06/2025;TRANSF DE DELTA SA;;3.100,00;
30/06/2025;SEGURANÇA SOCIAL;350,00;;
```

**Note:** Clients withheld 25% retenção. Gross amounts before retenção:
- EMPRESA ALPHA: EUR 3,750 received = EUR 5,000 gross (÷ 0.75)
- STARTUP BETA: EUR 2,500 = EUR 3,333.33 gross
- GAMMA CONSULTING: EUR 4,200 = EUR 5,600 gross
- DELTA SA: EUR 3,100 = EUR 4,133.33 gross

Stripe: EUR 1,920 net (no retenção — foreign payer). Gross-up to ~EUR 1,978 (after fees).

**Step 1 — Total Gross Receipts**

```
Grossed-up from retenção clients:  EUR 18,066.67
Stripe gross (no retenção):        EUR  1,978.00
Remaining months (extrapolated):   assume full year = EUR 52,000 gross (example)
Total gross Categoria B:           EUR 52,000
```

**Step 2 — Apply Regime Simplificado Coefficient**

```
Service type: management consulting → coefficient 0.35
Taxable income: EUR 52,000 × 0.35 = EUR 18,200
Less SS contributions paid (deductible): EUR 350 × 12 = EUR 4,200
Taxable income for IRS: EUR 18,200 − EUR 4,200 = EUR 14,000
```

**Step 3 — IRS Computation**

```
EUR 7,703 × 13.25% = EUR 1,020.65
(EUR 14,000 − EUR 7,703) × 18% = EUR 6,297 × 18% = EUR 1,133.46
Total IRS gross: EUR 2,154.11
Less retenções na fonte: receipts from PT clients × 25% of gross
  = EUR 18,066.67 × 25% (as withheld) = EUR 4,516.67 already withheld
IRS balance: EUR 2,154.11 − EUR 4,516.67 = **(EUR 2,362.56 refund)**
```

Refund scenario — confirm all retenção certificates match grossed-up amounts.

---

### Example 2 — Caixa Geral de Depósitos (Porto, Software Developer)

**Bank:** CGD (Caixa) online statement
**Client:** Pedro Costa, software developer, Porto, IRS Jovem year 2 (75% exempt)

Gross receipts: EUR 45,000 (services coefficient 0.35)
Taxable base: EUR 45,000 × 0.35 = EUR 15,750
Less SS: EUR 45,000 × 70% × 21.4% / 12 × 12 = EUR 6,741
Net taxable: EUR 15,750 − EUR 6,741 = EUR 9,009

IRS Jovem — year 2 (75% exempt): EUR 9,009 × 25% subject = EUR 2,252.25

IRS: EUR 2,252.25 × 13.25% = **EUR 298.42**

Flag: IRS Jovem requires AT confirmation of year number (anos de IRS Jovem). Pedro must submit declaration via Portal das Finanças.

---

### Example 3 — BPI (Algarve, Architect — Contabilidade Organizada)

**Bank:** BPI statement
**Client:** Sofia Pinto, architect, Algarve, gross receipts EUR 220,000 (mandatory contab. organizada)

Note: Mandatory contabilidade organizada — TOC signature required. This example shows structure only.

Gross receipts: EUR 220,000
Deductible expenses (actual):
- Office rent: EUR 12,000
- Utilities: EUR 2,400
- Phone/internet: EUR 1,200
- Software: EUR 2,400
- TOC accountant: EUR 4,800
- Professional insurance: EUR 1,500
- Travel: EUR 3,000
- SS contributions: EUR 32,817 (21.4% × 70% × EUR 220,000)
Total expenses: EUR 60,117

Net profit: EUR 220,000 − EUR 60,117 = EUR 159,883

IRS on EUR 159,883:
EUR 81,199 bracket: EUR 29,141.53 + (EUR 159,883 − EUR 81,199) × 48% = EUR 29,141.53 + EUR 42,569.52 = EUR 71,711.05

Adicional solidariedade: (EUR 80,000 limit applies to taxable income) — EUR 159,883 > EUR 80,000:
(EUR 159,883 − EUR 80,000) × 2.5% = EUR 79,883 × 2.5% = EUR 1,997.08

Total IRS: EUR 71,711.05 + EUR 1,997.08 = **EUR 73,708.13**

Flag: Gross > EUR 200,000 — mandatory TOC; adicional solidariedade applies.

---

### Example 4 — Santander Portugal (Lisbon, Designer, MB Way Heavy)

**Bank:** Santander Totta statement
**Client:** Margarida Santos, graphic designer, Lisbon, receives many MB Way payments

MB Way narrations in bank: `MBWAY RECEBIDO CLIENTE X` × multiple entries

Treatment: MB Way receipts are standard income. The key challenge is identifying the payer. Many micro-clients may not be registered companies and therefore may not withhold retenção.

Key rule: If payer is a non-company (individual consumer), no retenção obligation. If payer is a company with NIF, 25% withholding is mandatory.

For MB Way heavy designers: many small consumer payments = no retenção. Sum all MB Way credits as gross Categoria B receipts at face value (no gross-up needed).

Gross MB Way income: EUR 18,000 (all individual consumers)
Other TRANSF from company clients (with retenção): EUR 24,000 gross

Total gross: EUR 42,000
Coeficiente 0.35: EUR 42,000 × 0.35 = EUR 14,700
Less SS: ~EUR 6,300
Taxable: EUR 8,400

IRS: EUR 7,703 × 13.25% + EUR 697 × 18% = EUR 1,020.65 + EUR 125.46 = **EUR 1,146.11**

---

### Example 5 — Novo Banco (Lisbon, NHR Regime)

**Bank:** Novo Banco statement
**Client:** John Smith, UK national, registered NHR in Portugal, IT consultant

NHR (Non-Habitual Resident) — now IFICI (Incentivo Fiscal à Criatividade e Investigação):
- Foreign-source Categoria B income: may be exempt under NHR if taxed in source country
- Portuguese-source income from "high value-added activities": flat 20% rate

Do NOT apply standard brackets to NHR clients without confirming:
1. NHR/IFICI registration number and status
2. Source of each income stream (Portuguese source vs. foreign source)
3. Whether activity is on the list of qualifying professions

**Action for this client:** STOP — apply R-PT-2 (NHR status must be confirmed via AT). Do not apply standard rates; do not apply 20% flat rate without verification.

---

### Example 6 — ActivoBank / Moey (Coimbra, Translator)

**Bank:** ActivoBank/Moey statement (digital bank)
**Client:** Rita Alves, translator, Coimbra, first year trabalhador independente

First-year considerations:
- Regime simplificado applies (new entrant, estimated income < EUR 200,000)
- If estimated annual income ≤ EUR 12,500: may apply for isenção de retenção na fonte
- IRS Jovem: if Rita ≤ 35 years old, confirm year 1 eligibility for 100% exemption (capped EUR 28,737)

Gross receipts (full year): EUR 22,000
Coeficiente (translation = Categoria B services): 0.35
Taxable: EUR 22,000 × 0.35 = EUR 7,700
Less SS (first-year relief: 12 months free for new entrants, then normal): assume EUR 0 SS year 1
Taxable for IRS: EUR 7,700

IRS Jovem year 1 (100% exempt up to EUR 28,737): EUR 7,700 fully exempt
**IRS: EUR 0**

Note: First-year SS relief — new trabalhadores independentes are exempt from SS contributions for the first 12 months. Confirm AT/SS registration date.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-PT-1 — Regime simplificado: coefficient, not actual expenses**
Under regime simplificado, taxable income = gross receipts × coefficient. Individual expenses are NOT deductible (they are implicitly covered by the coefficient). Only SS contributions paid are separately deductible from the gross taxable base. Apply this mechanically — do not add expenses under simplificado.

**T1-PT-2 — Retenção na fonte is a prepayment, not income reduction**
The 25% withheld by clients is a tax prepayment credited against final IRS liability. It does not reduce gross Categoria B receipts. Always gross-up payments received net of retenção (divide by 0.75) to obtain gross income.

**T1-PT-3 — SS contributions always deductible**
SS contributions paid are deductible from the IRS taxable base under both regimes. Under regime simplificado: deduct from the coefficient-reduced taxable base. Under contabilidade organizada: deduct as an expense. Apply without escalating.

**T1-PT-4 — IRS Jovem: confirm year number before applying**
Never assume IRS Jovem applies. The taxpayer must be ≤ 35 years old AND must be able to confirm the year number (year 1 = first year of Categoria A or B income after completing education). Always request confirmation before applying any exemption.

**T1-PT-5 — Mandatory contabilidade organizada at EUR 200,000**
Gross receipts exceeding EUR 200,000 in the prior year trigger mandatory contabilidade organizada from the following year. Apply regime simplificado only when confirmed gross ≤ EUR 200,000 in prior year (or current year for new entrants).

**T1-PT-6 — IRS payments and IVA are not IRS expenses**
Pagamentos AT for IRS (pagamento por conta, saldo IRS) and IVA entregue are tax payments, not Categoria B expenses. Exclude all AT payment narrations from income computation.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-PT-1 | NHR / IFICI regime | Complex foreign income exemptions and 20% flat rate — varies by income source and activity | Flag — do not compute without AT registration confirmation |
| T2-PT-2 | Multiple income categories (A + B, or B + F) | Joint filing rules (englobamento) vs. separate taxation choices | Flag — taxpayer may choose to englobar or not for certain categories |
| T2-PT-3 | Married couple filing (tributação conjunta) | Joint vs. separate filing produces different results — quociente conjugal | Present both options; do not default to one |
| T2-PT-4 | Falso recibo verde (single client > 80%) | AT may reclassify income as Categoria A (employment); different tax treatment | Flag for legal review; do not reclassify unilaterally |
| T2-PT-5 | Deduction for health, education, home expenses (Anexo H) | Personal deductions outside Categoria B — subject to AT e-fatura matching | Confirm e-fatura invoices are attributed to NIF; flag unclaimed deductions |
| T2-PT-6 | Partial-year residency or non-resident | Different tax rates and treaty rules for non-residents | Flag — do not apply resident rates to non-residents |

---

## Section 7 — Excel Working Paper Template

```
PORTUGUESE IRS WORKING PAPER (CATEGORIA B — REGIME SIMPLIFICADO)
Taxpayer: _______________  NIF: _______________  FY: 2025

SECTION A — GROSS RECEIPTS (Categoria B)
                                        EUR
Total invoiced (recibos verdes gross)  ___________
Gross-up of withheld amounts           ___________
Online platform payouts (grossed up)   ___________
Other Categoria B receipts             ___________
TOTAL GROSS RECEIPTS                   ___________

SECTION B — REGIME SIMPLIFICADO COEFFICIENT
Service type: _______________
Coefficient applied: _______________
Taxable base (gross × coefficient)     ___________
Less: SS contributions paid            (___________)
IRS TAXABLE INCOME                     ___________

SECTION C — IRS COMPUTATION (STANDARD BRACKETS)
Tax at bracket rates                   ___________
IRS Jovem exemption (if applicable)    (___________)
IRS before credits                     ___________
Less: retenções na fonte               (___________)
Less: pagamentos por conta IRS         (___________)
IRS BALANCE DUE / (REFUND)             ___________

SECTION D — ADICIONAL DE SOLIDARIEDADE
(Only if taxable income > EUR 80,000)  ___________

SECTION E — SEGURANÇA SOCIAL
Quarterly SS base: 70% × quarterly gross ÷ 3 ___________
Annual SS due: monthly base × 21.4% × 12    ___________
Less: SS already paid                        (___________)
SS balance due                               ___________

SECTION F — REVIEWER FLAGS
[ ] Regime simplificado confirmed (gross ≤ EUR 200,000 prior year)?
[ ] Coefficient correct for service type?
[ ] All retenção certificates collected?
[ ] SS payments verified against receipts
[ ] IRS Jovem — year number confirmed?
[ ] NHR/IFICI status confirmed (if applicable)?
[ ] Falso recibo verde risk assessed (single client > 80%)?
[ ] e-fatura personal deductions checked (Anexo H)?
```

---

## Section 8 — Bank Statement Reading Guide

### Millennium BCP
- Export: CSV via "Consultas" → "Movimentos" → "Exportar"
- Columns: `Data;Descrição;Débito;Crédito;Saldo`
- Amount format: thousands separator = `.`, decimal = `,` (e.g., `3.750,00`)
- Date format: DD/MM/YYYY
- Credit narrations: `TRANSF DE [sender]`, `TRANSFERÊNCIA RECEBIDA`
- Debit narrations: `TRANSF PARA [recipient]`, `COMISSÃO`, `SEGURANÇA SOCIAL`

### Caixa Geral de Depósitos (CGD)
- Export: PDF or CSV from e.caixa.pt
- Format similar to Millennium; columns: `Data;Descrição;Movimento;Saldo`
- Positive movement = credit; negative = debit

### BPI (Banco BPI)
- Export: CSV from BPINet
- Columns: `Data movimento;Descrição;Valor;Saldo`
- Positive Valor = credit; negative = debit

### Santander Portugal
- Export: CSV from NetBanco Santander
- Columns: `Fecha;Concepto;Importe;Saldo` (note: Spanish headers due to parent company)
- Amount: positive = credit; negative = debit; comma decimal

### Novo Banco
- Export: CSV or Excel from Novo Banco Online
- Columns: `Data;Descrição;Débito;Crédito;Saldo`
- Standard Portuguese bank format

### ActivoBank / Moey (digital)
- Export: CSV/PDF from app
- Simple format; credit amounts in dedicated column

### MB Way / Multibanco
- Not a bank statement — payments appear as narrations in primary bank statement
- Look for: `MBWAY RECEBIDO`, `MULTIBANCO RECEBIMENTO`, `TPA [merchant]`

---

## Section 9 — Onboarding Fallback

**Missing retenção certificates:**
> "To compute your IRS accurately, I need the withholding certificates (declarações de retenção na fonte) from each client who withheld 25% from your payments. You can request these from your clients by January/February — companies are legally required to issue them. Alternatively, check Portal das Finanças → 'Consultar' → 'Retenções na Fonte' where AT may have the data directly."

**Service type unclear:**
> "To apply the correct regime simplificado coefficient, I need to know the nature of your services. Are you selling goods (coefficient 0.15), providing general services (0.35), or do you work in a listed profession under Artigo 151º CIRS (also 0.35)? Please confirm so I can apply the correct taxable base."

**IRS Jovem:**
> "Based on your age, you may qualify for IRS Jovem. This exempts 100% of tax in years 1–3, 75% in years 4–6, 50% in years 7–9, and 25% in year 10. To apply it, I need to confirm: (1) that you are 35 years old or younger, and (2) the year number of your Portuguese income-earning career. Can you confirm when you started receiving Categoria A or B income in Portugal after completing your studies?"

**SS contributions unknown:**
> "Segurança Social contributions are deductible from your IRS taxable base and can significantly reduce your tax liability. Do you have your quarterly SS payment receipts? If not, I can estimate based on your declared gross receipts: your SS base is 70% of your quarterly gross divided by 3, taxed at 21.4%."

---

## Section 10 — Reference Material

### Key Legislation
- **CIRS (Código do IRS)** — primary income tax code; Art. 28 (Categoria B), Art. 31 (coeficientes), Art. 101 (retenção na fonte)
- **Lei n.º 24-D/2022** — introduced IRS Jovem reforms
- **Portaria 1011/2001** — Artigo 151º CIRS list of high-value professions

### Filing Deadlines 2025 (FY 2024 return)
| Deadline | Event |
|---|---|
| April 2025 | Modelo 3 filing window opens |
| 30 June 2025 | Deadline for submission of Modelo 3 (IRS 2024) |
| August 2025 | AT issues assessments; payments due within notice |
| 31 August 2025 | Pagamento por conta — 1st advance payment for 2025 |
| 30 November 2025 | Pagamento por conta — 2nd advance payment for 2025 |

### Useful References
- AT Portal das Finanças: portaldasfinancas.gov.pt
- Segurança Social Direta: app.seg-social.pt
- CIRS: dre.pt (Diário da República)
- IRS Jovem confirmation: Portal das Finanças → "IRS Jovem"
