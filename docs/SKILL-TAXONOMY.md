# OpenAccountants — Global Skill Taxonomy

This document maps every skill the platform needs, worldwide. It is the master blueprint for contributors, coordinators, and the build pipeline.

---

## How to read this document

Every self-employed person in every jurisdiction faces the same five obligations. The specifics differ, but the structure doesn't. This taxonomy exploits that structure to make skill creation systematic and repeatable.

**Obligation categories (the columns):**

| Code | Obligation | What it answers |
|------|-----------|-----------------|
| **IT** | Income Tax | "How much income tax do I owe?" |
| **CT** | Consumption Tax (VAT / GST / Sales Tax) | "How much VAT/GST/sales tax do I collect and remit?" |
| **SC** | Social Contributions (SSC / NIC / SE Tax) | "What social security / pension / health contributions do I owe?" |
| **EF** | Entity Fees & Filings | "What registration fees, annual reports, or entity-level filings does my business structure require?" |
| **ET** | Estimated Tax & Payments | "What advance payments must I make during the year?" |

**Functional roles (the rows within each skill):**

| Role | What it does | Example |
|------|-------------|---------|
| **Intake** | Collects data, runs refusal sweep, hands off downstream | `us-ca-freelance-intake` |
| **Bookkeeping** | Classifies transactions into tax-line items | `us-sole-prop-bookkeeping` |
| **Computation** | Applies rates, thresholds, deductions to classified data | `us-schedule-c-and-se-computation` |
| **Return Assembly** | Builds the actual form/return from computed figures | `ny-it-201-resident-return` |
| **Decision Support** | Evaluates elections, optimisations, entity structure choices | `us-s-corp-election-decision` |

**Infrastructure skills (shared across jurisdictions):**

| Layer | Purpose | Example |
|-------|---------|---------|
| **Workflow Base** | Execution pipeline, output spec, self-checks, refusals | `us-tax-workflow-base`, `vat-workflow-base` |
| **Regional Directive** | Shared rules across a bloc | `eu-vat-directive` |
| **Orchestrator** | Entry point that sequences content skills | `us-ca-return-assembly` |

---

## Part 1 — The universal skill skeleton

Every country needs skills in this order. Not every country needs every slot (e.g., US states have no VAT; UAE has no income tax). But the skeleton is the same.

```
[Country] Intake Orchestrator
  └── [Country] Bookkeeping / Transaction Classification
        └── [Country] Income Tax Computation
              └── [Country] Income Tax Return Assembly
        └── [Country] Consumption Tax (VAT/GST/Sales Tax) Return
        └── [Country] Social Contributions Computation
        └── [Country] Entity Fees & Filing Requirements
        └── [Country] Estimated Tax / Advance Payments
        └── [Country] Contractor Reporting (1099 / equivalent)
  └── [Country] Decision Support (entity election, optimisation)
```

### Mandatory components of every Tier 2 content skill

Derived from the best existing skills (`us-sole-prop-bookkeeping`, `ny-it-201-resident-return`, `germany-vat-return`, `malta-income-tax`):

1. **Frontmatter** — name, description, version, jurisdiction, tax_year, depends_on
2. **Scope statement** — explicit in/out of scope, entity types covered
3. **Refusal catalogue** — coded refusals (R-XX-REASON) with explanations
4. **Year-specific figures table** — every rate, threshold, deadline with primary source citation
5. **Computation rules** — step-by-step mechanical logic
6. **Confidence tiers** — [T1] deterministic, [T2] reviewer judgment, [T3] escalate/refuse
7. **Edge cases & special rules** — elections, safe harbours, exceptions
8. **Worked examples** — at least 2 realistic scenarios
9. **Self-checks** — verification items before delivery
10. **Primary source library** — statutes, regulations, official guidance cited
11. **Disclaimer** — no liability, professional review required, openaccountants.com link

---

## Part 2 — Global skill map

### Legend

| Symbol | Status |
|--------|--------|
| **Done** | Skill exists in the repo, verified or near-verified |
| **Stub** | Placeholder in repo, content not yet exported |
| **Needed** | Skill does not exist yet — must be built |
| — | Not applicable for this jurisdiction |

---

### UNITED STATES — Federal

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| US Tax Workflow Base | infra | Workflow base | **Done** | `foundation/us-tax-workflow-base.md` |
| US Sole Prop Bookkeeping | IT | Bookkeeping | **Done** | `federal/us-sole-prop-bookkeeping.md` |
| US Schedule C + SE Computation | IT+SC | Computation | **Done** | `federal/us-schedule-c-and-se-computation.md` |
| US QBI Deduction (§199A) | IT | Computation | **Stub** | `federal/us-qbi-deduction.md` |
| US Self-Employed Retirement | IT | Computation | **Stub** | `federal/us-self-employed-retirement.md` |
| US Self-Employed Health Insurance | IT | Computation | **Stub** | `federal/us-self-employed-health-insurance.md` |
| US Quarterly Estimated Tax | ET | Computation | **Stub** | `federal/us-quarterly-estimated-tax.md` |
| US 1099-NEC Issuance | IT | Reporting | **Stub** | `federal/us-1099-nec-issuance.md` |
| US S-Corp Election Decision | — | Decision support | **Stub** | `federal/us-s-corp-election-decision.md` |
| US Federal Return Assembly | IT | Orchestrator | **Done** | `orchestrator/us-federal-return-assembly.md` |

### UNITED STATES — California

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| CA Freelance Intake | infra | Intake | **Done** | `orchestrator/us-ca-freelance-intake.md` |
| CA Form 540 Individual Return | IT | Return assembly | **Stub** | `california/ca-540-individual-return.md` |
| CA SMLLC Form 568 | EF | Entity filing | **Stub** | `california/ca-smllc-form-568.md` |
| CA Estimated Tax (540-ES) | ET | Computation | **Stub** | `california/ca-estimated-tax-540es.md` |
| CA Form 3853 Health Coverage | IT | Computation | **Stub** | `california/ca-form-3853-coverage.md` |
| CA Return Assembly | IT | Orchestrator | **Done** | `orchestrator/us-ca-return-assembly.md` |
| CA Sales & Use Tax | CT | Return | **Needed** | — |

### UNITED STATES — New York

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| NY IT-201 Resident Return | IT | Return assembly | **Done** | `newyork/ny-it-201-resident-return.md` |
| NY IT-204-LL LLC Filing Fee | EF | Entity filing | **Done** | `newyork/ny-llc-filing-fee-it-204-ll.md` |
| NY Freelance Intake | infra | Intake | **Needed** | — |
| NY Return Assembly | IT | Orchestrator | **Needed** | — |
| NYC Unincorporated Business Tax | IT | Computation | **Needed** | — |
| NY Estimated Tax (IT-2105) | ET | Computation | **Needed** | — |
| NY Sales Tax | CT | Return | **Needed** | — |

### UNITED STATES — Texas

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| TX Franchise Tax (Form 05-102) | EF | Entity filing | **Needed** | — |
| TX Sales & Use Tax (Form 01-114) | CT | Return | **Needed** | — |
| TX Return Assembly | — | Orchestrator | **Needed** | — |
| TX Freelance Intake | infra | Intake | **Needed** | — |

*Note: Texas has no state income tax. TX skills are entity fees + sales tax only.*

### UNITED STATES — Florida

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| FL Sales & Use Tax (DR-15) | CT | Return | **Needed** | — |
| FL Annual Report (Sunbiz) | EF | Entity filing | **Needed** | — |
| FL Return Assembly | — | Orchestrator | **Needed** | — |

*Note: Florida has no state income tax. FL skills are entity fees + sales tax only.*

### UNITED STATES — Washington State

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| WA Business & Occupation Tax | IT | Computation | **Needed** | — |
| WA Sales Tax | CT | Return | **Needed** | — |
| WA Return Assembly | — | Orchestrator | **Needed** | — |

*Note: WA has no income tax but has B&O tax (gross receipts tax on business activity).*

### UNITED STATES — Illinois

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| IL Individual Return (IL-1040) | IT | Return assembly | **Needed** | — |
| IL Estimated Tax (IL-1040-ES) | ET | Computation | **Needed** | — |
| IL LLC Annual Report | EF | Entity filing | **Needed** | — |
| IL Sales Tax (ST-1) | CT | Return | **Needed** | — |
| IL Return Assembly | IT | Orchestrator | **Needed** | — |

### UNITED STATES — Remaining states pattern

Every US state with an income tax needs:

| Skill type | Applies to |
|-----------|------------|
| State individual return | All states with income tax (41 states + DC) |
| State estimated tax | All states with income tax |
| State SMLLC / entity filing | States that treat SMLLCs as separate entities (CA, NY, TX, etc.) |
| State sales & use tax | 45 states + DC |
| State return assembly orchestrator | All states |
| State freelance intake | High-population states |

States with no income tax (no IT skill needed): AK, FL, NV, NH*, SD, TN*, TX, WA, WY
(*NH and TN tax interest/dividends only — may need limited skills)

---

### UNITED KINGDOM

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| UK Income Tax (Self Assessment SA100) | IT | Computation + Return | **Needed** | — |
| UK Self-Employment (SA103) | IT | Bookkeeping + Computation | **Needed** | — |
| UK National Insurance (Class 2 + Class 4) | SC | Computation | **Needed** | — |
| UK VAT Return (VAT100) | CT | Return | **Needed** | — |
| UK Payments on Account | ET | Computation | **Needed** | — |
| UK Student Loan Repayment | SC | Computation | **Needed** | — |
| UK Freelance Intake | infra | Intake | **Needed** | — |
| UK Return Assembly | IT | Orchestrator | **Needed** | — |

Workflow base: `us-tax-workflow-base` pattern, adapted for HMRC Self Assessment.
VAT base: `vat-workflow-base` (UK left EU but VAT structure is similar enough to share the base).

---

### CANADA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| CA-Fed T1 Individual Return | IT | Return assembly | **Needed** | — |
| CA-Fed Self-Employment Income (T2125) | IT | Bookkeeping + Computation | **Needed** | — |
| CA-Fed CPP/EI Self-Employed | SC | Computation | **Needed** | — |
| CA-Fed GST/HST Return (GST34) | CT | Return | **Needed** | — |
| CA-Fed Quarterly Instalments | ET | Computation | **Needed** | — |
| Ontario Individual Return | IT | Return assembly | **Needed** | — |
| British Columbia Individual Return | IT | Return assembly | **Needed** | — |
| Quebec Individual Return (TP-1) | IT | Return assembly | **Needed** | — |
| Quebec QST Return | CT | Return | **Needed** | — |
| Canada Freelance Intake | infra | Intake | **Needed** | — |
| Canada Return Assembly | IT | Orchestrator | **Needed** | — |

Needs: new `gst-hst-workflow-base` or extend `vat-workflow-base`.

---

### AUSTRALIA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| AU Individual Return (Tax Return for Individuals) | IT | Return assembly | **Needed** | — |
| AU Sole Trader Income (Business Schedule) | IT | Bookkeeping + Computation | **Needed** | — |
| AU GST (Business Activity Statement) | CT | Return | **Needed** | — |
| AU PAYG Instalments | ET | Computation | **Needed** | — |
| AU Superannuation Guarantee | SC | Computation | **Needed** | — |
| AU Medicare Levy + Surcharge | SC | Computation | **Needed** | — |
| AU Freelance Intake | infra | Intake | **Needed** | — |
| AU Return Assembly | IT | Orchestrator | **Needed** | — |

Needs: extend `vat-workflow-base` for GST or create `gst-workflow-base`.

---

### IRELAND

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| IE Income Tax (Form 11) | IT | Return assembly | **Needed** | — |
| IE Self-Employed PRSI (Class S) | SC | Computation | **Needed** | — |
| IE USC (Universal Social Charge) | SC | Computation | **Needed** | — |
| IE VAT Return (VAT3) | CT | Return | **Needed** | — |
| IE Preliminary Tax | ET | Computation | **Needed** | — |
| IE Return Assembly | IT | Orchestrator | **Needed** | — |

VAT layers: `vat-workflow-base` + `eu-vat-directive` + `ie-vat-return`.

---

### GERMANY

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| DE VAT Return (UStVA) | CT | Return | **Done** | `international/germany/germany-vat-return.md` |
| DE Income Tax (Einkommensteuererklärung) | IT | Computation + Return | **Needed** | — |
| DE Self-Employed Social Contributions | SC | Computation | **Needed** | — |
| DE Trade Tax (Gewerbesteuer) | IT | Computation | **Needed** | — |
| DE Estimated Tax (Vorauszahlung) | ET | Computation | **Needed** | — |
| DE Freelance Intake | infra | Intake | **Needed** | — |
| DE Return Assembly | IT | Orchestrator | **Needed** | — |

---

### FRANCE

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| FR VAT Return (CA3) | CT | Return | **Done** | `international/france/france-vat-return.md` |
| FR Income Tax (Déclaration de Revenus) | IT | Computation + Return | **Needed** | — |
| FR Self-Employed Social Contributions (URSSAF) | SC | Computation | **Needed** | — |
| FR CFE (Cotisation Foncière des Entreprises) | EF | Entity filing | **Needed** | — |
| FR Estimated Tax (Acomptes) | ET | Computation | **Needed** | — |
| FR Return Assembly | IT | Orchestrator | **Needed** | — |

---

### ITALY

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| IT VAT Return (LIPE) | CT | Return | **Done** | `international/italy/italy-vat-return.md` |
| IT Income Tax (Modello Redditi PF) | IT | Computation + Return | **Needed** | — |
| IT INPS Self-Employed Contributions | SC | Computation | **Needed** | — |
| IT IRAP (Regional Production Tax) | IT | Computation | **Needed** | — |
| IT Estimated Tax (Acconti) | ET | Computation | **Needed** | — |
| IT Return Assembly | IT | Orchestrator | **Needed** | — |

---

### SPAIN

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| ES Income Tax (IRPF — Modelo 100) | IT | Computation + Return | **Needed** | — |
| ES VAT Return (IVA — Modelo 303) | CT | Return | **Needed** | — |
| ES Self-Employed Social Contributions (RETA) | SC | Computation | **Needed** | — |
| ES Estimated Tax (Modelo 130) | ET | Computation | **Needed** | — |
| ES Annual Summary (Modelo 390) | CT | Return | **Needed** | — |
| ES Return Assembly | IT | Orchestrator | **Needed** | — |

---

### NETHERLANDS

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| NL Income Tax (Aangifte Inkomstenbelasting) | IT | Computation + Return | **Needed** | — |
| NL VAT Return (BTW-aangifte) | CT | Return | **Needed** | — |
| NL ZZP Self-Employed Deductions | IT | Computation | **Needed** | — |
| NL Estimated Tax (Voorlopige Aanslag) | ET | Computation | **Needed** | — |
| NL Return Assembly | IT | Orchestrator | **Needed** | — |

---

### PORTUGAL

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| PT Income Tax (IRS — Modelo 3) | IT | Computation + Return | **Needed** | — |
| PT VAT Return (IVA — Declaração Periódica) | CT | Return | **Needed** | — |
| PT Self-Employed Social Contributions | SC | Computation | **Needed** | — |
| PT Estimated Tax (Pagamentos por Conta) | ET | Computation | **Needed** | — |
| PT Return Assembly | IT | Orchestrator | **Needed** | — |

---

### BELGIUM

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| BE Income Tax (Personenbelasting) | IT | Computation + Return | **Needed** | — |
| BE VAT Return (BTW-aangifte) | CT | Return | **Needed** | — |
| BE Self-Employed Social Contributions | SC | Computation | **Needed** | — |
| BE Estimated Tax (Voorafbetalingen) | ET | Computation | **Needed** | — |
| BE Return Assembly | IT | Orchestrator | **Needed** | — |

---

### POLAND

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| PL Income Tax (PIT-36) | IT | Computation + Return | **Needed** | — |
| PL VAT Return (JPK_V7M) | CT | Return | **Needed** | — |
| PL ZUS Self-Employed Contributions | SC | Computation | **Needed** | — |
| PL Estimated Tax (Zaliczki) | ET | Computation | **Needed** | — |
| PL Return Assembly | IT | Orchestrator | **Needed** | — |

---

### MALTA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| MT Income Tax (TA24) | IT | Computation + Return | **Done** | `international/malta/malta-income-tax.md` |
| MT Social Security Contributions (Class 2) | SC | Computation | **Done** | `international/malta/malta-ssc.md` |
| MT VAT Return (VAT3) | CT | Return | **Done** | `international/malta/malta-vat-return.md` |
| MT Estimated Tax (Provisional Tax) | ET | Computation | **Needed** | — |
| MT Freelance Intake | infra | Intake | **Needed** | — |
| MT Return Assembly | IT | Orchestrator | **Needed** | — |

---

### INDIA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| IN Income Tax (ITR-3 / ITR-4) | IT | Computation + Return | **Needed** | — |
| IN GST Return (GSTR-3B + GSTR-1) | CT | Return | **Needed** | — |
| IN Advance Tax | ET | Computation | **Needed** | — |
| IN TDS on Freelance Payments | IT | Reporting | **Needed** | — |
| IN Return Assembly | IT | Orchestrator | **Needed** | — |

Needs: `gst-workflow-base` or extend `vat-workflow-base`.

---

### BRAZIL

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| BR Income Tax (IRPF — DIRPF) | IT | Computation + Return | **Needed** | — |
| BR Indirect Tax (ICMS/ISS/IPI) | CT | Return | **Needed** | — |
| BR INSS Self-Employed Contributions | SC | Computation | **Needed** | — |
| BR Simples Nacional | IT+CT+SC | Computation | **Needed** | — |
| BR Estimated Tax (Carnê-Leão) | ET | Computation | **Needed** | — |
| BR Return Assembly | IT | Orchestrator | **Needed** | — |

---

### MEXICO

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| MX Income Tax (ISR — Declaración Anual PF) | IT | Computation + Return | **Needed** | — |
| MX VAT (IVA — Declaración Mensual) | CT | Return | **Needed** | — |
| MX IMSS Self-Employed | SC | Computation | **Needed** | — |
| MX Estimated Tax (Pagos Provisionales) | ET | Computation | **Needed** | — |
| MX CFDI Electronic Invoicing | CT | Reporting | **Needed** | — |
| MX Return Assembly | IT | Orchestrator | **Needed** | — |

---

### JAPAN

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| JP Income Tax (Kakutei Shinkoku) | IT | Computation + Return | **Needed** | — |
| JP Consumption Tax (Shōhizei) | CT | Return | **Needed** | — |
| JP National Health Insurance + Pension | SC | Computation | **Needed** | — |
| JP Estimated Tax (Yotei Nōzei) | ET | Computation | **Needed** | — |
| JP Return Assembly | IT | Orchestrator | **Needed** | — |

---

### SINGAPORE

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| SG Income Tax (Form B / B1) | IT | Computation + Return | **Needed** | — |
| SG GST Return (GST F5) | CT | Return | **Needed** | — |
| SG CPF Self-Employed (MediSave) | SC | Computation | **Needed** | — |
| SG Return Assembly | IT | Orchestrator | **Needed** | — |

---

### UNITED ARAB EMIRATES

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| AE Corporate Tax Return | IT | Computation + Return | **Needed** | — |
| AE VAT Return | CT | Return | **Needed** | — |
| AE Return Assembly | IT | Orchestrator | **Needed** | — |

*Note: UAE has no personal income tax. Corporate tax (9%) applies to business profits above AED 375,000.*

---

### SOUTH KOREA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| KR Income Tax (종합소득세) | IT | Computation + Return | **Needed** | — |
| KR VAT Return (부가가치세) | CT | Return | **Needed** | — |
| KR National Pension + Health Insurance | SC | Computation | **Needed** | — |
| KR Estimated Tax | ET | Computation | **Needed** | — |
| KR Return Assembly | IT | Orchestrator | **Needed** | — |

---

### SWITZERLAND

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| CH Federal Income Tax | IT | Computation + Return | **Needed** | — |
| CH Cantonal/Communal Income Tax | IT | Computation + Return | **Needed** | — |
| CH VAT (MWST) | CT | Return | **Needed** | — |
| CH AHV/IV Self-Employed Contributions | SC | Computation | **Needed** | — |
| CH Return Assembly | IT | Orchestrator | **Needed** | — |

---

### SWEDEN

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| SE Income Tax (Inkomstdeklaration 1) | IT | Computation + Return | **Needed** | — |
| SE VAT Return (Skattedeklaration) | CT | Return | **Needed** | — |
| SE Self-Employed Social Contributions (Egenavgifter) | SC | Computation | **Needed** | — |
| SE F-tax (Preliminary Tax) | ET | Computation | **Needed** | — |
| SE Return Assembly | IT | Orchestrator | **Needed** | — |

---

### DENMARK

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| DK Income Tax (Årsopgørelse) | IT | Computation + Return | **Needed** | — |
| DK VAT Return (Momsangivelse) | CT | Return | **Needed** | — |
| DK AM-bidrag (Labour Market Contribution) | SC | Computation | **Needed** | — |
| DK B-skat (Preliminary Tax) | ET | Computation | **Needed** | — |
| DK Return Assembly | IT | Orchestrator | **Needed** | — |

---

### NORWAY

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| NO Income Tax (Skattemelding) | IT | Computation + Return | **Needed** | — |
| NO VAT Return (MVA-melding) | CT | Return | **Needed** | — |
| NO Self-Employed Social Contributions (Trygdeavgift) | SC | Computation | **Needed** | — |
| NO Advance Tax (Forskuddsskatt) | ET | Computation | **Needed** | — |
| NO Return Assembly | IT | Orchestrator | **Needed** | — |

---

### AUSTRIA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| AT Income Tax (Einkommensteuererklärung E1) | IT | Computation + Return | **Needed** | — |
| AT VAT Return (UVA) | CT | Return | **Needed** | — |
| AT SVS Self-Employed Social Insurance | SC | Computation | **Needed** | — |
| AT Estimated Tax (Vorauszahlung) | ET | Computation | **Needed** | — |
| AT Return Assembly | IT | Orchestrator | **Needed** | — |

---

### CZECH REPUBLIC

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| CZ Income Tax (Přiznání k DPFO) | IT | Computation + Return | **Needed** | — |
| CZ VAT Return (Přiznání k DPH) | CT | Return | **Needed** | — |
| CZ Self-Employed Social + Health Insurance | SC | Computation | **Needed** | — |
| CZ Estimated Tax (Zálohy) | ET | Computation | **Needed** | — |
| CZ Return Assembly | IT | Orchestrator | **Needed** | — |

---

### ROMANIA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| RO Income Tax (Declarația Unică) | IT | Computation + Return | **Needed** | — |
| RO VAT Return (Decontul de TVA) | CT | Return | **Needed** | — |
| RO CAS/CASS Self-Employed Contributions | SC | Computation | **Needed** | — |
| RO Return Assembly | IT | Orchestrator | **Needed** | — |

---

### GREECE

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| GR Income Tax (Φορολογική Δήλωση E1) | IT | Computation + Return | **Needed** | — |
| GR VAT Return (ΦΠΑ) | CT | Return | **Needed** | — |
| GR EFKA Self-Employed Contributions | SC | Computation | **Needed** | — |
| GR Estimated Tax (Προκαταβολή) | ET | Computation | **Needed** | — |
| GR Return Assembly | IT | Orchestrator | **Needed** | — |

---

### HUNGARY

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| HU Income Tax (SZJA 2353) | IT | Computation + Return | **Needed** | — |
| HU VAT Return (ÁFA 2365) | CT | Return | **Needed** | — |
| HU Self-Employed Social Contributions (TB) | SC | Computation | **Needed** | — |
| HU Return Assembly | IT | Orchestrator | **Needed** | — |

---

### NEW ZEALAND

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| NZ Income Tax (IR3) | IT | Computation + Return | **Needed** | — |
| NZ GST Return (GST101A) | CT | Return | **Needed** | — |
| NZ ACC Levies | SC | Computation | **Needed** | — |
| NZ Provisional Tax | ET | Computation | **Needed** | — |
| NZ Return Assembly | IT | Orchestrator | **Needed** | — |

---

### SOUTH AFRICA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| ZA Income Tax (ITR12) | IT | Computation + Return | **Needed** | — |
| ZA VAT Return (VAT201) | CT | Return | **Needed** | — |
| ZA UIF Self-Employed | SC | Computation | **Needed** | — |
| ZA Provisional Tax (IRP6) | ET | Computation | **Needed** | — |
| ZA Return Assembly | IT | Orchestrator | **Needed** | — |

---

### NIGERIA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| NG Personal Income Tax | IT | Computation + Return | **Needed** | — |
| NG VAT Return | CT | Return | **Needed** | — |
| NG Return Assembly | IT | Orchestrator | **Needed** | — |

---

### KENYA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| KE Income Tax (Self-Assessment) | IT | Computation + Return | **Needed** | — |
| KE VAT Return | CT | Return | **Needed** | — |
| KE NHIF/NSSF Contributions | SC | Computation | **Needed** | — |
| KE Return Assembly | IT | Orchestrator | **Needed** | — |

---

### ARGENTINA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| AR Income Tax (Ganancias) | IT | Computation + Return | **Needed** | — |
| AR VAT (IVA) | CT | Return | **Needed** | — |
| AR Monotributo (Simplified Regime) | IT+CT+SC | Computation | **Needed** | — |
| AR Self-Employed Social Contributions | SC | Computation | **Needed** | — |
| AR Return Assembly | IT | Orchestrator | **Needed** | — |

---

### COLOMBIA

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| CO Income Tax (Renta PF) | IT | Computation + Return | **Needed** | — |
| CO VAT (IVA) | CT | Return | **Needed** | — |
| CO Self-Employed Social Contributions | SC | Computation | **Needed** | — |
| CO Return Assembly | IT | Orchestrator | **Needed** | — |

---

### CHILE

| Skill | Code | Role | Status | File |
|-------|------|------|--------|------|
| CL Income Tax (Renta AT) | IT | Computation + Return | **Needed** | — |
| CL VAT (IVA — Form 29) | CT | Return | **Needed** | — |
| CL AFP/Fonasa Self-Employed | SC | Computation | **Needed** | — |
| CL Return Assembly | IT | Orchestrator | **Needed** | — |

---

## Part 3 — Infrastructure skills still needed

| Skill | Purpose | Priority |
|-------|---------|----------|
| `gst-workflow-base` | Workflow base for GST systems (Canada, Australia, India, NZ, Singapore) — similar to VAT but different registration thresholds, input tax credit rules, and return structures | High — blocks Phase 1 |
| `income-tax-workflow-base` (international) | Workflow base for non-US income tax skills — adapt `us-tax-workflow-base` patterns for international use | High — blocks all international IT skills |
| `social-contributions-workflow-base` | Workflow base for social contribution computations — currently ad-hoc in Malta SSC | Medium |
| Additional EU VAT directive updates | Extend `eu-vat-directive` as new EU countries are added | Ongoing |

---

## Part 4 — Scoreboard

| Category | Done | Stub | Needed | Total |
|----------|------|------|--------|-------|
| Infrastructure (workflow bases, directives) | 3 | 0 | 3 | 6 |
| US Federal | 4 | 6 | 0 | 10 |
| US States (CA, NY, TX, FL, WA, IL + pattern) | 6 | 4 | 12+ | 22+ |
| EU (DE, FR, IT, ES, NL, PT, BE, PL, MT, IE, AT, CZ, RO, GR, HU, SE, DK, NO) | 6 | 0 | ~70 | ~76 |
| UK | 0 | 0 | 8 | 8 |
| Canada | 0 | 0 | 11 | 11 |
| Australia + NZ | 0 | 0 | 13 | 13 |
| Asia (JP, SG, KR, IN) | 0 | 0 | 18 | 18 |
| Americas (BR, MX, AR, CO, CL) | 0 | 0 | 24 | 24 |
| Middle East + Africa (AE, ZA, NG, KE) | 0 | 0 | 13 | 13 |
| Switzerland | 0 | 0 | 5 | 5 |
| **TOTAL** | **19** | **10** | **~177** | **~206** |

**19 skills done. ~177 to build. The skeleton is proven. Now it scales.**
