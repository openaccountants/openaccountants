---
name: mx-freelance-intake
description: Use this skill when onboarding a Mexican persona física con actividad empresarial or RESICO freelancer. Trigger on phrases like "Mexico freelance", "SAT registration", "persona física", "actividad empresarial", "RESICO", "régimen fiscal México", "RFC", "CFDI", "ISR provisional", "declaración anual México", or any initial client conversation involving a Mexican self-employed individual. This skill collects essential information to determine the correct tax régimen, validates SAT compliance, and routes to the appropriate computation skill. ALWAYS read this skill before beginning any Mexican freelance intake.
version: 1.0
jurisdiction: MX
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - mx-return-assembly
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MX Freelance Intake

## Mexico Freelance Intake -- Orchestrator Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Mexico (Estados Unidos Mexicanos) |
| Tax | ISR (Impuesto Sobre la Renta) |
| Currency | MXN (Peso Mexicano) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Ley del Impuesto Sobre la Renta (LISR), Código Fiscal de la Federación (CFF) |
| Supporting legislation | Ley del IVA (LIVA), Ley del Seguro Social (LSS), Resolución Miscelánea Fiscal (RMF) |
| Tax authority | Servicio de Administración Tributaria (SAT) |
| Filing portal | sat.gob.mx / Portal del contribuyente |
| Filing deadline | Declaración anual: April 30 following year (personas físicas) |
| Validated by | Pending — requires sign-off by a Mexican Contador Público |
| Skill version | 1.0 |

### Key Régimen Thresholds

**Key Régimen Thresholds**

| Régimen | Revenue Ceiling | ISR Method | Deductions Allowed |
| --- | --- | --- | --- |
| RESICO (Régimen Simplificado de Confianza) | ≤MXN$3,500,000 annual | 1%--2.5% on gross receipts | None (tasa sobre ingresos cobrados) |
| Actividad Empresarial y Profesional | No ceiling | Progressive 1.92%--35% | Full deductions allowed |

### RESICO Annual ISR Table (Art. 113-E LISR)

**RESICO Annual ISR Table**  _(Art. 113-E LISR)_

| Annual Income (MXN) | Rate |
| --- | --- |
| Up to $300,000 | 1.00% |
| Up to $600,000 | 1.10% |
| Up to $1,000,000 | 1.50% |
| Up to $2,500,000 | 2.00% |
| Up to $3,500,000 | 2.50% |

### RESICO Monthly Provisional ISR Table

**RESICO Monthly Provisional ISR Table**

| Monthly Income (MXN) | Rate |
| --- | --- |
| Up to $25,000 | 1.00% |
| Up to $50,000 | 1.10% |
| Up to $83,333.33 | 1.50% |
| Up to $208,333.33 | 2.00% |
| Up to $291,666.66 | 2.50% |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown régimen | STOP -- do not proceed without régimen determination |
| Unknown RFC status | STOP -- cannot file without active RFC |
| Unknown CFDI compliance | STOP -- all income must be invoiced via CFDI |
| Unknown IVA treatment | Assume 16% IVA applies unless exempt activity |
| Unknown IMSS status | Flag -- voluntary for self-employed |
| Unknown marital status | Use individual tables (no joint filing in Mexico) |

## Section 2 -- Intake Questionnaire

### Q1: Régimen Fiscal

**Ask:** "¿En qué régimen fiscal está inscrito ante el SAT? / Which tax régimen are you registered under with SAT?"

**Q1 Response/Action Table**

| Response | Action |
| --- | --- |
| RESICO | Verify annual income ≤MXN$3,500,000. Proceed with RESICO pathway. |
| Actividad Empresarial y Profesional (AEP) | Proceed with full progressive rate pathway. |
| Sueldos y Salarios (only) | Out of scope for freelance -- redirect to employment skill. |
| RIF (Régimen de Incorporación Fiscal) | Legacy régimen -- ceased accepting new registrations 2022. Must transition to RESICO or AEP. Flag for SAT portal update. |
| Persona Moral | REFUSE -- this skill is for personas físicas only. |
| Unknown / not sure | Guide client to check Constancia de Situación Fiscal on SAT portal. |

- **RESICO Eligibility Validation** — Only actividades empresariales, profesionales, or arrendamiento; Cannot be socio/accionista of a persona moral; Cannot invoice to related parties if they represent >50% revenue; Prior year income must not have exceeded MXN$3,500,000; Must issue CFDI for all income

### Q2: RFC Status

**Ask:** "¿Tiene RFC activo ante el SAT? / Do you have an active RFC with SAT?"

**Q2 Response/Action Table**

| Response | Action |
| --- | --- |
| Yes -- RFC with homoclave | Record RFC. Proceed. |
| Yes -- but suspended (suspensión de actividades) | Must reactivate via SAT office (cita previa). PAUSE until reactivated. |
| No RFC | Cannot file. Must register at SAT (requires e.firma/FIEL or SAT ID). PAUSE. |
| RFC without obligaciones fiscales | Must add obligations via Portal del SAT. PAUSE. |

### Q3: Revenue Range (Annual)

**Ask:** "¿Cuál fue su ingreso bruto anual (antes de IVA) en el ejercicio anterior? / What was your gross annual income (before IVA) last fiscal year?"

**Q3 Response/Action Table**

| Response | Action |
| --- | --- |
| ≤MXN$3,500,000 | RESICO eligible (if other criteria met) |
| >MXN$3,500,000 | Must use Actividad Empresarial y Profesional |
| First year (sin ejercicio anterior) | RESICO eligible if projected income ≤MXN$3,500,000 |
| Exceeds $3.5M mid-year | Must transition to AEP from month of exceedance |

### Q4: CFDI Invoicing Compliance

**Ask:** "¿Emite CFDI (factura electrónica) por todos sus ingresos? / Do you issue CFDI for all income?"

**Q4 Response/Action Table**

| Response | Action |
| --- | --- |
| Yes -- all income invoiced via CFDI 4.0 | Proceed. |
| Partially -- some cash/informal | HIGH RISK. SAT cross-references bank deposits. Flag for regularisation. |
| No -- does not issue CFDI | STOP. Cannot be in RESICO. Must register PAC (Proveedor Autorizado de Certificación). |
| Uses complemento de pago | Good practice -- verify PPD/PUE method selection. |

### Q5: Filing Status

**Ask:** "¿Cuál es su estado civil para efectos fiscales? / What is your marital status for tax purposes?"

**Q5 Response/Action Table**

| Response | Action |
| --- | --- |
| Soltero/a (single) | Individual filing. Mexico has no joint returns. |
| Casado/a en sociedad conyugal | Each spouse declares 50% of joint property income (Art. 142 LISR). Flag if applicable. |
| Casado/a en separación de bienes | Each spouse files individually on own income. |
| Unión libre | Individual filing. |

**Note:** Mexico does NOT allow joint filing. Marital status only matters for sociedad conyugal income splitting.

### Q6: Other Income Sources

**Ask:** "¿Tiene otros ingresos además de su actividad empresarial? / Do you have income from other sources?"

**Q6 Response/Action Table**

| Response | Action |
| --- | --- |
| Sueldos y salarios (employment) | Accumulates in declaración anual. Employer withholds ISR. Get constancia de retenciones. |
| Arrendamiento (rental) | May be in RESICO if total ≤$3.5M. Separate chapter in LISR (Cap. III). |
| Intereses (interest) | Banks withhold ISR provisional. Report in anual. |
| Dividendos | Report in anual. ISR piramidado credit. |
| Plataformas tecnológicas | ISR retained by platform (Art. 113-A LISR). Verify if already in RESICO. |
| Enajenación de bienes | Capital gains -- Art. 119--128 LISR. Flag for specialist. |
| None | Proceed with single-source computation. |

### Q7: ISR Provisional Payments

**Ask:** "¿Está al corriente con sus pagos provisionales de ISR? / Are your provisional ISR payments up to date?"

**Q7 Response/Action Table**

| Response | Action |
| --- | --- |
| Yes -- monthly filings current | Verify via 32D Opinión de Cumplimiento. Record amounts paid. |
| Behind 1--3 months | Calculate recargos (late interest) at CCP rate + 50% surcharge. |
| Behind >3 months | HIGH RISK. SAT may issue requerimiento. Recommend regularisation. |
| First year / never filed | Set up provisional schedule. RESICO: monthly by 17th. AEP: monthly by 17th. |
| Presentó en ceros | Verify -- if income received, must amend (declaración complementaria). |

### Q8: IMSS Voluntary Registration

**Ask:** "¿Está inscrito voluntariamente al IMSS (Régimen Voluntario) o tiene seguro privado? / Are you voluntarily enrolled in IMSS or do you have private insurance?"

**Q8 Response/Action Table**

| Response | Action |
| --- | --- |
| IMSS Régimen Voluntario (Modalidad 40 or Continuación Voluntaria) | Record cuotas paid -- NOT deductible for RESICO; deductible for AEP. |
| Private health insurance | Deductible in AEP (Art. 151 LISR personal deduction, up to 15% income or 5 UMA anuales). Not relevant for RESICO. |
| No coverage | Inform -- IMSS voluntary available. Not required for filing. |
| IMSS as empleador (has employees) | Different -- employer obligations apply. Verify cuotas patronales current. |

## Section 3 -- Decision Tree

```
START
│
├─ Q1: Régimen Fiscal?
│   ├─ RESICO → Verify income ≤$3.5M → Q2
│   ├─ AEP → Q2
│   ├─ RIF → Transition required → PAUSE
│   ├─ Persona Moral → REFUSE (R-MX-1)
│   └─ Unknown → Check Constancia → Loop Q1
│
├─ Q2: RFC Active?
│   ├─ Yes → Q3
│   ├─ Suspended → PAUSE until reactivated
│   └─ No → PAUSE until registered
│
├─ Q3: Revenue Range?
│   ├─ ≤$3.5M + RESICO → Q4
│   ├─ >$3.5M + AEP → Q4
│   └─ >$3.5M + RESICO → Must transition to AEP → Flag
│
├─ Q4: CFDI Compliant?
│   ├─ Yes → Q5
│   ├─ Partial → Flag + continue with caution
│   └─ No → PAUSE until PAC configured
│
├─ Q5: Filing Status → Record → Q6
│
├─ Q6: Other Income?
│   ├─ None → Q7
│   ├─ Sueldos → Get constancia retenciones → Q7
│   └─ Other → Flag chapter → Q7
│
├─ Q7: Provisionals Current?
│   ├─ Yes → Q8
│   ├─ Behind → Calculate recargos → Q8
│   └─ Never filed → Set up schedule → Q8
│
├─ Q8: IMSS?
│   └─ Record status → ROUTE
│
└─ ROUTE:
    ├─ RESICO → mx-return-assembly (RESICO pathway)
    └─ AEP → mx-return-assembly (AEP pathway)
```

## Section 4 -- Refusal Catalogue

- **R-MX-1 -- Persona Moral** — This skill covers personas físicas (individuals) only. Personas morales (corporations, S de RL, SA de CV, SC, AC) file separate returns under Título II LISR. Escalate to a Contador Público with corporate tax experience.  _(Título II LISR)_
- **R-MX-2 -- Maquiladora / IMMEX** — Maquiladora/IMMEX operations involve transfer pricing, customs, and corporate structures outside the scope of individual freelance taxation. Escalate to specialist.
- **R-MX-3 -- RIF Legacy without Transition Plan** — The Régimen de Incorporación Fiscal (RIF) no longer accepts new registrations (ceased 2022). Existing RIF taxpayers who have not transitioned to RESICO or AEP must do so. This skill cannot process returns under a legacy RIF structure without SAT portal updates.
- **R-MX-4 -- No RFC** — Filing is impossible without an active RFC (Registro Federal de Contribuyentes). The client must first obtain or reactivate their RFC at sat.gob.mx or a SAT office before this skill can proceed.
- **R-MX-5 -- Multinational / PE in Mexico** — Foreign residents with permanent establishment in Mexico or cross-border structures require specialist treatment under Título V LISR and applicable tax treaties. Out of scope.  _(Título V LISR)_
- **R-MX-6 -- Declaraciones en ceros with actual income** — Client filed provisional returns in zero but received income. This constitutes a fiscal irregularity. Must file declaraciones complementarias before proceeding with annual return. High audit risk.
- **R-MX-7 -- Régimen Fiscal Mismatch** — Client's Constancia de Situación Fiscal shows a régimen that does not match their actual activity. Must update obligaciones fiscales at SAT before filing.

## Section 5 -- IVA Quick Reference for Intake

**IVA Quick Reference for Intake**

| Activity Type | IVA Rate | Notes |
| --- | --- | --- |
| Professional services (general) | 16% | Standard rate |
| Professional services (border region) | 8% | Northern border stimulus |
| Food and medicine sales | 0% | Tasa 0% -- still file IVA returns |
| Medical services (individual practitioner) | Exempt | Art. 15 LIVA |
| Education services | Exempt | Art. 15 LIVA |
| Software development / tech | 16% | Standard rate |
| Digital platforms (foreign) | 16% | Withheld by platform since 2020 |

### IVA Filing Obligations

**IVA Filing Obligations**

| Régimen | IVA Filing | Deadline |
| --- | --- | --- |
| RESICO | Monthly declaración de IVA | 17th of following month |
| AEP | Monthly declaración de IVA | 17th of following month |
| Both | DIOT (Declaración Informativa de Operaciones con Terceros) | Monthly, by last day of following month |

## Section 6 -- IMSS / Social Security Reference

**IMSS / Social Security Reference**

| Concept | Detail |
| --- | --- |
| Voluntary regime (Modalidad 40) | For previously IMSS-registered individuals. Covers all benefits. |
| Continuación Voluntaria | Must elect within 5 years of last employment. |
| Self-employed base | Client declares between 1--25 UMA diario as base |
| UMA 2025 | $113.14/day (updated February 2025 by INEGI) |
| UMA mensual 2025 | $3,439.46 |
| UMA anual 2025 | $41,273.52 |
| Cuota fija (Modalidad 40) | Approximately 10.075% of declared base (varies by branch) |
| Deductibility (AEP) | Cuotas IMSS voluntarias = personal deduction (Art. 151 fracción V) |
| Deductibility (RESICO) | NOT deductible -- RESICO has zero deductions |

## Section 7 -- Document Checklist

```
MEXICO FREELANCE INTAKE -- DOCUMENT CHECKLIST

Client: ___________________________
RFC: ___________________________
Régimen: RESICO / AEP
Tax Year: ___________________________

REQUIRED:
[ ] Constancia de Situación Fiscal (current, from SAT portal)
[ ] e.firma (FIEL) or SAT ID credentials (for filing)
[ ] Bank statements (all accounts, full year)
[ ] CFDI emitidos (issued invoices) -- XML or portal download
[ ] CFDI recibidos (received invoices) -- for AEP deductions
[ ] Acuses de declaraciones provisionales (proof of provisional filings)
[ ] Constancia de retenciones (if employed or platform income)

RECOMMENDED (AEP only):
[ ] Estado de cuenta bancario conciliado
[ ] Registro de inversiones (asset register)
[ ] Nómina (if employer with employees)
[ ] IMSS cuotas paid (receipts from SUA/IDSE)
[ ] Pólizas contables (accounting entries)

FOR REGULARISATION (if behind):
[ ] Opinión de cumplimiento 32D
[ ] Declaraciones complementarias filed
[ ] Convenio de pago a plazos (if applicable)
```

## Section 8 -- Annual Calendar of Obligations

**Annual Calendar of Obligations**

| Deadline | Obligation | Régimen |
| --- | --- | --- |
| 17th of each month | Pago provisional ISR | RESICO + AEP |
| 17th of each month | Declaración mensual IVA | RESICO + AEP |
| Last day of following month | DIOT | RESICO + AEP |
| January 15 | Declaración Informativa de Clientes y Proveedores (>$50,000) | AEP |
| March 31 | Declaración anual personas morales (if has PM) | N/A |
| April 30 | Declaración anual personas físicas | RESICO + AEP |
| June 30 | First PTU payment deadline (if employer) | AEP with employees |

## Section 9 -- Edge Cases

### RESICO to AEP Mid-Year Transition

- **Transition steps** — If income exceeds MXN$3,500,000 during the year: 1. The month income exceeds the threshold, taxpayer must file under general AEP tables. 2. Recalculate all prior months under AEP progressive rates. 3. Credit RESICO provisional payments already made. 4. Update obligaciones fiscales at SAT portal. 5. Cannot return to RESICO until income drops below threshold for a full year.

### Sociedad Conyugal Income Split

- **Income split rules** — When married under sociedad conyugal: Each spouse may declare 50% of income from joint property; Both must issue CFDI for their respective 50%; Both need active RFC and matching régimen; This does NOT apply to purely personal professional services income.

### Platform Income (Art. 113-A)

- **Platform income treatment** — For income via digital platforms (Uber, Rappi, Airbnb, etc.): Platform retains ISR + IVA; If in RESICO, platform retention is definitive (no annual filing needed for platform income alone); If total income >$300,000/year or has other income sources, must file annual return.  _(Art. 113-A)_

## Section 10 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| RESICO personas físicas | LISR Art. 113-E to 113-J |
| AEP general | LISR Título IV, Capítulo II, Sección I |
| ISR annual tables | LISR Art. 152 |
| Personal deductions | LISR Art. 151 |
| IVA general | LIVA Art. 1--7 |
| CFDI requirements | CFF Art. 29, 29-A |
| Provisional payments | LISR Art. 106 (AEP), Art. 113-E (RESICO) |
| IMSS voluntary | LSS Art. 218--231 |
| UMA | Ley para Determinar el Valor de la UMA |
| RMF 2025 | DOF publication, updated annually |

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

## Section 3 -- Decision Tree

0. **Route to RESICO pathway** — ROUTE RESICO taxpayers to mx-return-assembly
0. **Route to AEP pathway** — ROUTE AEP taxpayers to mx-return-assembly

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
