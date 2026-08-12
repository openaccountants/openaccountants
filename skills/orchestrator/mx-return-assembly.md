---
name: mx-return-assembly
description: Use this skill when assembling or reviewing a Mexican persona física annual tax return (declaración anual). Trigger on phrases like "declaración anual México", "ISR anual", "return assembly Mexico", "cross-check CFDI", "IVA reconciliation", "provisional vs annual", "RESICO annual", "AEP annual return", or any task involving the compilation, verification, or filing of a Mexican individual's annual income tax return. This skill orchestrates cross-checks between ISR, IVA, IMSS, and CFDI data. ALWAYS read this skill before assembling any Mexican annual return.
version: 1.0
jurisdiction: MX
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - mx-freelance-intake
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MX Return Assembly

## Mexico Return Assembly -- Orchestrator Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Mexico (Estados Unidos Mexicanos) |
| Tax | ISR (Impuesto Sobre la Renta) -- Declaración Anual |
| Currency | MXN (Peso Mexicano) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Ley del Impuesto Sobre la Renta (LISR), Código Fiscal de la Federación (CFF) |
| Tax authority | Servicio de Administración Tributaria (SAT) |
| Filing portal | sat.gob.mx -- Declaraciones |
| Filing deadline | April 30 of following year (personas físicas) |
| Required credential | e.firma (FIEL) or Contraseña SAT |
| Validated by | Pending — requires sign-off by a Mexican Contador Público |
| Skill version | 1.0 |

### ISR Annual Table -- Actividad Empresarial y Profesional (Art. 152 LISR, 2025)

**ISR Annual Table -- Actividad Empresarial y Profesional (Art. 152 LISR, 2025)**  _(Art. 152 LISR, 2025)_

| Lower Limit (MXN) | Upper Limit (MXN) | Fixed Quota (MXN) | Rate on Excess |
| --- | --- | --- | --- |
| 0.01 | 8,952.49 | 0.00 | 1.92% |
| 8,952.50 | 75,984.55 | 171.88 | 6.40% |
| 75,984.56 | 133,536.07 | 4,461.94 | 10.88% |
| 133,536.08 | 155,229.80 | 10,723.55 | 16.00% |
| 155,229.81 | 185,852.57 | 14,194.54 | 17.92% |
| 185,852.58 | 374,837.88 | 19,682.13 | 21.36% |
| 374,837.89 | 590,795.99 | 60,049.40 | 23.52% |
| 590,796.00 | 1,127,926.84 | 110,842.74 | 30.00% |
| 1,127,926.85 | 1,503,902.46 | 271,981.99 | 32.00% |
| 1,503,902.47 | 4,511,707.37 | 392,294.17 | 34.00% |
| 4,511,707.38 | En adelante | 1,414,947.85 | 35.00% |

### RESICO Annual ISR Table (Art. 113-E LISR)

**RESICO Annual ISR Table (Art. 113-E LISR)**  _(Art. 113-E LISR)_

| Annual Income (MXN) | Rate |
| --- | --- |
| Up to $300,000 | 1.00% |
| Up to $600,000 | 1.10% |
| Up to $1,000,000 | 1.50% |
| Up to $2,500,000 | 2.00% |
| Up to $3,500,000 | 2.50% |

## Section 2 -- Assembly Workflow

### Phase 1: Data Gathering

1. Download CFDI emitidos (issued) from SAT portal -- full year XML set
2. Download CFDI recibidos (received) from SAT portal -- full year XML set
3. Obtain bank statements (all accounts, all institutions)
4. Obtain acuses de declaraciones provisionales (ISR + IVA, all months)
5. Obtain constancias de retenciones (employers, clients with retention, platforms)
6. Obtain IMSS payment receipts (if voluntary or employer)
7. Obtain prior year declaración anual (for comparison)

### Phase 2: CFDI Revenue Reconciliation

**Phase 2: CFDI Revenue Reconciliation**

| Step | Check | Action if Mismatch |
| --- | --- | --- |
| 2.1 | Sum all CFDI emitidos (subtotal, before IVA) | This = gross revenue for ISR |
| 2.2 | Compare CFDI total vs bank deposits | Bank > CFDI = possible undeclared income |
| 2.3 | Verify método de pago (PUE vs PPD) | PPD: income = when complemento de pago issued |
| 2.4 | Check for cancelled CFDI (status = cancelado) | Exclude cancelled from totals |
| 2.5 | Verify RFC of all clients on CFDI | Flag any RFC genérico (XAXX010101000) > $50,000 |
| 2.6 | Cross-reference CFDI vs client payments | Identify unpaid invoices (for PPD accounting) |

- **RESICO Special Rule** — Income is recognised on cash basis (efectivamente cobrado). Only CFDI with confirmed payment count. PPD CFDI without complemento de pago = not yet income.
- **AEP Rule** — Income recognised on accrual basis (devengado) for general regime, OR cash basis if elected under Art. 196 CFF. Verify which method the client uses.  _(Art. 196 CFF)_

### Phase 3: CFDI Expense Reconciliation (AEP Only)

**Phase 3: CFDI Expense Reconciliation (AEP Only)**

| Step | Check | Action if Mismatch |
| --- | --- | --- |
| 3.1 | Sum all CFDI recibidos (deductible expenses) | Verify each has valid RFC, correct régimen fiscal |
| 3.2 | Verify requisitos de deducibilidad (Art. 27 LISR) | Payment via banked method >$2,000 MXN |
| 3.3 | Check IVA on each CFDI recibido | IVA trasladado = IVA acreditable |
| 3.4 | Verify payment method | Cash payments >$2,000 = NOT deductible |
| 3.5 | Check timing | Expense must be in same fiscal year |
| 3.6 | Verify proportionality | If mixed use, apply proportion |

- **Deductibility Requirements (Art. 27 LISR)** — Strictly indispensable for the business activity; Backed by valid CFDI; Paid by transfer, cheque, credit/debit card, or electronic wallet (>$2,000); Withholding obligations met (if applicable); Properly registered in accounting  _(Art. 27 LISR)_

### Phase 4: Provisional ISR vs Annual ISR Cross-Check

**Phase 4: Provisional ISR vs Annual ISR Cross-Check**

| Step | Check | Expected Outcome |
| --- | --- | --- |
| 4.1 | Sum all provisional ISR payments made | Total from acuses |
| 4.2 | Sum all ISR retained by clients (retenciones) | From constancias de retenciones |
| 4.3 | Calculate annual ISR liability | Using Art. 152 table (AEP) or Art. 113-E (RESICO) |
| 4.4 | Annual ISR - provisionals - retentions | = ISR a cargo (to pay) or ISR a favor (refund) |
| 4.5 | If saldo a favor > 30% of ISR annual | Flag -- high refund ratio triggers SAT review |

- **RESICO Cross-Check** — Annual ISR = total income × applicable RESICO rate; Credit: sum of monthly provisional payments; Credit: retenciones (1.25% retained by personas morales); Result = a cargo or a favor
- **AEP Cross-Check** — Annual ISR = progressive table on (revenue - deductions - personal deductions); Credit: provisional payments (Art. 106 method); Credit: retenciones; Credit: estímulos fiscales (if applicable)  _(Art. 106 method)_

### Phase 5: IVA Monthly Reconciliation

**Phase 5: IVA Monthly Reconciliation**

| Step | Check | Expected Outcome |
| --- | --- | --- |
| 5.1 | IVA trasladado (charged to clients) | 16% × revenue (or 8% border, 0% applicable) |
| 5.2 | IVA acreditable (paid on expenses) | Sum IVA on deductible CFDI recibidos |
| 5.3 | IVA retenido (retained by clients) | From constancias de retenciones (2/3 IVA common) |
| 5.4 | Monthly: trasladado - acreditable - retenido | = IVA a cargo or a favor |
| 5.5 | Cross-check vs monthly declaraciones filed | Verify consistency |
| 5.6 | Annual IVA total | Should = sum of 12 monthly declarations |

- **Common IVA Retentions** — Persona moral paying persona física: retains 2/3 of IVA (Art. 1-A LIVA); Digital platform: retains 100% IVA; Government entities: retain 100% IVA  _(Art. 1-A LIVA)_

### Phase 6: IMSS Cuotas Check

**Phase 6: IMSS Cuotas Check**  _(Art. 151-V)_

| Item | Check |
| --- | --- |
| Voluntary (Modalidad 40) | Verify 12 monthly payments made |
| Employer (patrón) | Verify SUA/IDSE bimestral payments (6 periods) |
| Cuotas amount | Verify base declared × contribution rate |
| Deductibility | AEP: deductible as personal deduction (Art. 151-V). RESICO: NOT deductible. |

### Phase 7: Personal Deductions (AEP Annual Return)

**Phase 7: Personal Deductions (AEP Annual Return)**  _(Art. 151 LISR)_

| Deduction (Art. 151 LISR) | Limit | Notes |
| --- | --- | --- |
| Medical/dental/hospital expenses | No global limit per item | Must be for taxpayer, spouse, ascendants, descendants |
| Funeral expenses | 1 UMA anual ($41,273.52) | Per event |
| Donations | Up to 7% of prior year base (4% to gobierno) | Must be to donatarias autorizadas |
| Mortgage interest (real, vivienda) | Up to 750,000 UDIS of credit | Only habitual residence |
| Voluntary retirement savings (Afore/PPR) | 10% of income, max 5 UMA anuales ($206,367.60) | Deductible contribution to Plan Personal de Retiro |
| Health insurance premiums | No specific sub-limit | Complementary medical insurance |
| School transportation | Per child | Only if mandatory |
| Local taxes on property | Actual paid | Predial on property owned |

- **Global Personal Deduction Limit** — The lesser of 15% of total income OR 5 UMA anuales (MXN$206,367.60 for 2025).

## Section 3 -- Computation Engine

### RESICO Annual Computation

- **RESICO Annual Computation** — A. Total CFDI emitidos efectivamente cobrados (excl. IVA)     ___________ B. Apply RESICO annual table rate                              ___________ C. ISR del ejercicio (A × rate from table)                     ___________ D. Less: Pagos provisionales ISR                               ___________ E. Less: Retenciones ISR (1.25% from personas morales)         ___________ F. ISR a cargo / (a favor) = C - D - E                         ___________

### AEP Annual Computation

- **AEP Annual Computation** — A. INGRESOS ACUMULABLES A1. CFDI emitidos (net of IVA)                              ___________ A2. Other income (interest, etc.)                           ___________ A3. Total income                                            ___________ B. DEDUCCIONES AUTORIZADAS B1. Purchases and cost of sales                             ___________ B2. Operating expenses (backed by CFDI)                     ___________ B3. Depreciation (inversiones -- Art. 31--38 LISR)          ___________ B4. Insurance premiums                                      ___________ B5. Sueldos y salarios (employees)                          ___________ B6. Cuotas IMSS patronales                                  ___________ B7. Total deducciones autorizadas                           ___________ C. UTILIDAD FISCAL (A3 - B7)                                   ___________ D. PÉRDIDAS FISCALES DE EJERCICIOS ANTERIORES                  ___________ E. BASE GRAVABLE (C - D)                                       ___________ F. DEDUCCIONES PERSONALES (Art. 151)                           ___________ G. BASE PARA TARIFA (E - F)                                    ___________ H. ISR (apply Art. 152 table to G)                             ___________ I. Less: Subsidio para el empleo (if applicable)               ___________ J. Less: Pagos provisionales                                   ___________ K. Less: Retenciones                                           ___________ L. ISR A CARGO / (A FAVOR) = H - I - J - K                    ___________  _(Art. 31-38 LISR; Art. 151; Art. 152)_

## Section 4 -- Cross-Check Matrix

**Cross-Check Matrix**

| Cross-Check | Source A | Source B | Tolerance | Flag If |
| --- | --- | --- | --- | --- |
| Revenue integrity | CFDI emitidos total | Bank deposits total | ±5% | Bank > CFDI by >5% |
| Expense backing | CFDI recibidos total | Declared deductions | Exact | Deduction without CFDI |
| IVA consistency | Monthly IVA filed | CFDI-derived IVA | Exact | Mismatch any month |
| Provisional ISR | Sum of acuses | SAT portal query | Exact | Missing month |
| Retentions | Constancias received | Annual pre-filled data | Exact | Amount differs |
| IMSS cuotas | SUA receipts | Declared personal deduction | Exact | Over-claimed |
| DIOT consistency | Monthly DIOT filed through SAT online platform | CFDI recibidos | ±1% | Material difference |

## Section 5 -- Filing Procedure

### Pre-Filing Checklist

[ ] All 12 provisional ISR declarations filed (or complementarias submitted)
[ ] All 12 IVA monthly declarations filed
[ ] All 12 DIOT submissions filed through SAT online DIOT platform (mandatory since Aug. 1, 2025)
[ ] All constancias de retenciones obtained
[ ] CFDI emitidos reconciled to bank
[ ] CFDI recibidos reconciled to expenses
[ ] Personal deductions verified with documentation
[ ] Prior year pérdidas fiscales confirmed (if carrying forward)
[ ] Opinión de cumplimiento 32D positive (recommended)

### Filing Steps (SAT Portal)

1. Log into sat.gob.mx with e.firma or Contraseña
2. Navigate to Declaraciones > Anuales > Personas Físicas
3. Select ejercicio fiscal
4. SAT pre-fills income from CFDI and retentions -- VERIFY
5. Enter deductions, personal deductions, other income
6. System calculates ISR a cargo / a favor
7. If a cargo: generate línea de captura (payment reference)
8. If a favor: elect devolución (refund via CLABE) or compensación
9. Sign with e.firma and submit
10. Download acuse de recibo (proof of filing)

### Payment Options (ISR a Cargo)

**Payment Options (ISR a Cargo)**

| Method | Deadline | Notes |
| --- | --- | --- |
| Single payment | April 30 | Full amount, no surcharge |
| Pago en parcialidades | Within 30 days of filing | Up to 6 instalments; generates recargos |
| Línea de captura | Valid 5 business days | Generated at filing; must pay before expiry |

### Refund Process (ISR a Favor)

**Refund Process (ISR a Favor)**

| Amount | Process | Timeline |
| --- | --- | --- |
| ≤MXN$150,000 | Automatic via Contraseña | 5--40 business days |
| >MXN$150,000 | Requires e.firma signature | 40 business days max (legal) |
| >MXN$500,000 | SAT may request additional documentation | Up to 90 days with audit |
| Refund not received | Verify CLABE matches RFC holder | Check estatus at sat.gob.mx |

## Section 6 -- Edge Cases

### Dual Régimen in Same Year (RESICO → AEP Transition)

- **Dual Régimen in Same Year (RESICO → AEP Transition)** — If income exceeds $3.5M mid-year, recalculate entire year under AEP; Credit all RESICO provisional payments against AEP annual liability; File declaración complementaria for all provisional months; Update Constancia de Situación Fiscal

### Multiple Income Chapters (Acumulación)

- **Multiple Income Chapters (Acumulación)** — When taxpayer has income from multiple chapters: Sueldos y salarios (Cap. I) + AEP (Cap. II): accumulate both in annual; RESICO + Sueldos: RESICO is separate (no accumulation unless >$300,000 combined); Arrendamiento + AEP: both accumulate in annual declaration; Apply progressive table to total accumulated base

### Pérdidas Fiscales (Tax Losses)

- **Pérdidas Fiscales (Tax Losses)** — AEP losses carry forward up to 10 years (Art. 109 LISR); Update for inflation annually (factor de actualización); Cannot offset losses against RESICO income; RESICO does NOT generate tax losses (no deductions allowed)  _(Art. 109 LISR)_

### Estímulos Fiscales (Tax Incentives)

**Estímulos Fiscales (Tax Incentives)**

| Incentive | Article | Benefit |
| --- | --- | --- |
| Technological research/development | Art. 202 LISR | 30% credit on R&D spending |
| Film/theatre production | Art. 189-190 LISR | Credit against ISR |
| Northern border region | Decree 2019 | ISR rate reduced to 20%; IVA 8% |
| Donations to trusts | Art. 151 LISR | 7% limit |

## Section 7 -- Red Flags and Audit Triggers

**Red Flags and Audit Triggers**

| Indicator | SAT Risk Level | Action |
| --- | --- | --- |
| Bank deposits > CFDI revenue by >20% | HIGH | Investigate -- potential discrepancia fiscal |
| ISR refund > 40% of annual liability | MEDIUM | Document thoroughly; expect SAT query |
| Zero CFDI for months with bank activity | HIGH | File complementarias or explain |
| CFDI to RFC genérico > $50,000 individual | MEDIUM | SAT flags for review |
| Provisional payments all in ceros despite income | HIGH | Immediate regularisation needed |
| Deductions > 60% of revenue | MEDIUM | Verify each deduction meets Art. 27 |
| Personal deductions near global limit | LOW | Normal -- just document properly |
| Year-over-year revenue drop > 50% | MEDIUM | SAT may compare to CFDI history |

## Section 8 -- Penalties Reference

**Penalties Reference**

| Infraction | Penalty | Legal Basis |
| --- | --- | --- |
| Late annual filing | MXN$1,810 -- $22,400 per requerimiento | CFF Art. 82 |
| Omitted income (discovered by SAT) | 55% -- 75% of omitted tax | CFF Art. 76 |
| Failure to issue CFDI | MXN$19,700 -- $112,650 per CFDI | CFF Art. 84 |
| Late payment (recargos) | CCP rate × 1.5 (approximately 1.47%/month in 2025) | CFF Art. 21 |
| False CFDI (operations simuladas) | 55% -- 75% + criminal liability | CFF Art. 69-B, 113 Bis |
| Failure to file DIOT | MXN$10,490 -- $20,970 | CFF Art. 81-82 |

## Section 9 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| ISR personas físicas | LISR Título IV |
| RESICO | LISR Art. 113-E to 113-J |
| AEP | LISR Título IV, Cap. II, Sección I |
| Annual progressive table | LISR Art. 152 |
| Deductibility requirements | LISR Art. 27, 28 |
| Personal deductions | LISR Art. 151 |
| Tax losses | LISR Art. 109, 110 |
| IVA | LIVA Art. 1--43 |
| CFDI | CFF Art. 29, 29-A; RMF 2.7.x |
| Penalties | CFF Art. 76--82 |
| Recargos | CFF Art. 21 |
| DIOT | LIVA Art. 32 |
| SAT portal | sat.gob.mx |
| RMF 2025 | Resolución Miscelánea Fiscal 2025 (DOF) |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público Certificado, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

## Section 2 -- Assembly Workflow

0. **Data Gathering** — Download CFDI emitidos/recibidos, bank statements, acuses, constancias, IMSS receipts, prior year return

### Phase 2: CFDI Revenue Reconciliation

0. **CFDI Revenue Reconciliation** — Reconcile CFDI emitidos against bank deposits and payment methods

### Phase 3: CFDI Expense Reconciliation (AEP Only)

0. **CFDI Expense Reconciliation** — Reconcile CFDI recibidos against deductibility requirements

### Phase 4: Provisional ISR vs Annual ISR Cross-Check

0. **Provisional vs Annual ISR Cross-Check** — Cross-check provisional payments and retentions against annual ISR liability

### Phase 5: IVA Monthly Reconciliation

0. **IVA Monthly Reconciliation** — Reconcile IVA trasladado, acreditable, and retenido monthly and annually

### Phase 6: IMSS Cuotas Check

0. **IMSS Cuotas Check** — Verify IMSS cuotas payments and deductibility

### Phase 7: Personal Deductions (AEP Annual Return)

0. **Personal Deductions Verification** — Verify personal deductions against Art. 151 limits

## Section 3 -- Computation Engine

0. **Computation Engine** — Run RESICO or AEP annual computation as applicable

## Section 4 -- Cross-Check Matrix

0. **Cross-Check Matrix** — Apply full cross-check matrix across all data sources

## Section 5 -- Filing Procedure

0. **Filing Procedure** — Complete pre-filing checklist and file via SAT portal

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
