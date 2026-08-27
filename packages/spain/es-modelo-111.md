---
name: es-modelo-111
description: Use this skill whenever asked about Spanish Modelo 111 (quarterly withholdings on professional services). Trigger on phrases like "Modelo 111", "retenciones profesionales", "retención 15%", "retención 7%", "quarterly withholdings Spain", "IRPF withholding professionals", "Modelo 190", "certificado de retenciones", "pago fraccionado", "retenedor", or any question about withholding tax on payments to professionals in Spain. This skill covers Modelo 111 rates, filing deadlines, who must withhold, the relationship to Modelo 190 annual summary, interaction with Modelo 130, and compliance requirements. ALWAYS read this skill before touching any Spanish withholding tax work.
version: "1.0"
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ES Modelo 111

## Spain Modelo 111 -- Quarterly IRPF Withholdings Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Tax | IRPF Withholdings (Retenciones e ingresos a cuenta) |
| Form | Modelo 111 (quarterly) |
| Currency | EUR only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | Ley 35/2006 del IRPF, Art. 99-101; Real Decreto 439/2007, Art. 74-95 |
| Tax authority | Agencia Estatal de Administración Tributaria (AEAT) |
| Filing portal | Sede electrónica AEAT (sede.agenciatributaria.gob.es) |
| Annual summary | Modelo 190 (filed January of following year) |
| Skill version | 1.0 |

### Core Principle

Modelo 111 is the quarterly declaration used by businesses, professionals, and entities that WITHHOLD IRPF (retenciones) from payments made to:
- Employed workers (rendimientos del trabajo)
- Professionals / freelancers (rendimientos de actividades profesionales)
- Prize winners (premios)
- Certain other categories

This skill focuses on **retenciones on professional services** (pagos a profesionales), which is the most common scenario for small businesses and autónomos paying other autónomos.

### Standard Withholding Rates (2025)

**Standard Withholding Rates (2025)**

| Category | Rate | Notes |
| --- | --- | --- |
| Professional services (standard) | 15% | General rate for payments to autónomos/professionals |
| New professionals (first 3 years) | 7% | First 3 fiscal years of activity (must communicate to payer) |
| Training courses / conferences | 15% | Payments to speakers, trainers |
| Intellectual property (author, non-habitual) | 15% | Rights exploitation |
| Industrial property | 15% | Patent/trademark licensing |
| Agricultural/livestock (general) | 2% | Módulos estimación objetiva |
| Agricultural/livestock (engorde) | 1% | Fattening activities |
| Directors / board members (administradores) | 35% | Standard for board fees |
| Directors (entity < €100K turnover) | 19% | Reduced for small entities |

### Filing Calendar (2025)

**Filing Calendar (2025)**

| Quarter | Period | Due Date |
| --- | --- | --- |
| Q1 (1T) | January -- March | 1 -- 20 April |
| Q2 (2T) | April -- June | 1 -- 20 July |
| Q3 (3T) | July -- September | 1 -- 20 October |
| Q4 (4T) | October -- December | 1 -- 20 January (2026) |

- **Large companies (gran empresa) filing frequency** — Monthly filing by the 20th of the following month.

### Related Forms

**Related Forms**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Modelo 111 | Quarterly declaration of withholdings | Quarterly (see above) |
| Modelo 190 | Annual summary (all recipients) | January 1-31 of following year |
| Certificado de retenciones | Certificate issued to each professional | Before February 1 of following year |
| Modelo 130 | Quarterly estimated payment by professional (pago fraccionado) | Same quarterly dates |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether professional qualifies for 7% | Apply 15% (standard rate) |
| Unknown whether payer must withhold | If payer is a business/professional making payment to another professional for services -- must withhold |
| Unknown whether to file negative Modelo 111 | File with zero amount (declaración negativa) if registered but no payments in quarter |

## Section 2 -- Who Must Withhold (Obligados a Retener)

### 2.1 Entities That Must Withhold

**2.1 Entities That Must Withhold**

| Payer Type | Must Withhold? |
| --- | --- |
| Sociedades (SL, SA) | Yes -- always |
| Autónomos / professionals (individual) | Yes -- when paying other professionals for services |
| Public administration | Yes |
| Comunidades de propietarios (if paying professionals) | Yes |
| Individuals (not in economic activity) paying professionals | NO -- private individuals do not withhold |
| Foreign entities without permanent establishment in Spain | Generally NO (unless PE exists) |

### 2.2 Payments Subject to Withholding

**2.2 Payments Subject to Withholding**

| Payment Type | Withholding? | Rate |
| --- | --- | --- |
| Invoice from professional autónomo (abogado, consultor, diseñador, etc.) | Yes | 15% (or 7% if new) |
| Invoice from SL/SA (company) | NO -- companies do not have retenciones on services (they pay Impuesto de Sociedades) |  |
| Invoice for goods (not services) | NO |  |
| Invoice from agricultural module regime | Yes | 2% (or 1%) |
| Board member fees (administrador) | Yes | 35% (or 19%) |
| Salary to employees | Yes | Variable IRPF rate per employee (calculated per tables) |

### 2.3 How Withholding Works on a Professional Invoice

A professional's invoice includes:

```
Base imponible (fee):              €1,000.00
IVA (21%):                         +€210.00
Retención IRPF (15%):             -€150.00
───────────────────────────────────────────
Total a pagar:                     €1,060.00
```

The payer:
1. Pays the professional €1,060.00
2. Retains €150.00 (which they must deposit to AEAT via Modelo 111)
3. The professional declares the full €1,000 as income and credits the €150 retained against their annual IRPF

## Section 3 -- The 7% Reduced Rate (New Professionals)

### 3.1 Conditions for 7% Rate

**3.1 Conditions for 7% Rate**

| Condition | Requirement |
| --- | --- |
| First activity | Professional has not been in an economic activity in the prior year |
| Time limit | Applies during the tax year of commencement + following 2 tax years (3 years total) |
| Communication | Professional must communicate in writing to the payer that they qualify for 7% |
| Verification | Payer is entitled to rely on the professional's written communication |

### 3.2 Communication Requirements

The professional must provide a signed document (comunicación) stating:
- Full name and NIF/NIE
- Statement that they are in the first 3 fiscal years of activity (alta in IAE)
- Date of alta (start of activity)
- Declaration that 7% retention applies

If no communication is received, the payer must apply 15%.

## Section 4 -- Modelo 111 Filing

### 4.1 Form Structure

**4.1 Form Structure**

| Section | Content |
| --- | --- |
| Sección A | Identification (NIF, name, period) |
| Sección B | Rendimientos del trabajo (employee salaries) |
| Sección C | Rendimientos de actividades profesionales |
| Sección D | Premios (prizes) |
| Sección E | Ganancias patrimoniales (forest exploitation) |
| Sección F | Imputaciones de renta (certain income attributions) |
| Total | Sum of all retenciones to deposit |

### 4.2 Section C Detail (Professional Services)

**4.2 Section C Detail (Professional Services)**

| Field | Content |
| --- | --- |
| Number of recipients (perceptores) | Count of distinct professionals paid in the quarter |
| Base of withholdings (base de retenciones) | Total value of professional invoices (base imponible, not including IVA) |
| Retenciones (amounts withheld) | Total retenciones withheld (base × rate) |
| Ingresos a cuenta | Amounts paid on behalf where retención not possible (less common) |

### 4.3 Filing Method

**4.3 Filing Method**

| Method | Detail |
| --- | --- |
| Electronic (certificado digital) | Most common; mandatory for SLs and larger entities |
| Electronic (Cl@ve PIN) | Available for autónomos and individuals |
| Paper | Only for specific cases (pre-printed forms) |
| Negative declaration | Must file even if no payments made (declaración negativa) if registered as retenedor |

### 4.4 Payment

**4.4 Payment**

| Method | Detail |
| --- | --- |
| Direct debit (domiciliación) | Must file by 15th of month (5 days before deadline) |
| NRC (electronic bank payment) | Available up to last day |
| Bank in person | With payment letter from AEAT |

## Section 5 -- Modelo 190 (Annual Summary)

### 5.1 Purpose

Modelo 190 is the annual informative declaration summarizing ALL withholdings declared via Modelo 111 during the year. It provides recipient-by-recipient detail.

### 5.2 Content per Recipient

**5.2 Content per Recipient**

| Field | Detail |
| --- | --- |
| NIF of recipient | Professional's tax ID |
| Name | Full name or company name |
| Province code | Province of recipient |
| Clave (type code) | G = professional activities; A = employment; etc. |
| Total payments (percepciones) | Total base of invoices in the year |
| Total retenciones | Total withholding for the year |

### 5.3 Filing

**5.3 Filing**

| Item | Detail |
| --- | --- |
| Deadline | 1 -- 31 January of the following year |
| Method | Electronic (mandatory for >15 recipients or SL/SA) |
| Penalty for late filing | €20 per recipient record (minimum €300, maximum €20,000) |

## Section 6 -- Interaction with Modelo 130 (Pago Fraccionado)

### 6.1 What is Modelo 130?

Modelo 130 is the professional's own quarterly estimated tax payment. The professional reports:
- Gross income from activities (accumulated in the year)
- Deductible expenses (accumulated)
- Net income × 20% = tax due
- Less: retenciones already withheld by clients (from Modelo 111)
- Less: prior quarters' Modelo 130 payments
- = Amount to pay (or zero)

### 6.2 Exemption from Modelo 130

- **Exemption from Modelo 130 filing** — A professional is EXEMPT from filing Modelo 130 if at least 70% of their income from the prior year was subject to withholding (retención). This is common for professionals who invoice mainly to companies.

### 6.3 Credit Mechanism

**6.3 Credit Mechanism**

| Step | Detail |
| --- | --- |
| 1 | Payer withholds 15% and deposits via Modelo 111 |
| 2 | Professional claims withheld amounts as credit in annual IRPF return (Modelo 100) |
| 3 | If quarterly Modelo 130 payments + retenciones withheld > final IRPF liability → refund |

## Section 7 -- Certificado de Retenciones

### 7.1 Obligation

**7.1 Obligation**

| Field | Content |
| --- | --- |
| Payer details | Name, NIF, address |
| Recipient details | Name, NIF |
| Tax year | Year covered |
| Total payments | Sum of base amounts paid |
| Total retenciones | Sum of amounts withheld |
| Breakdown | By type if applicable |

- **Deadline to issue certificado de retenciones** — Every payer (retenedor) must issue a certificado de retenciones to each professional before February 1 of the following year.

### 7.2 Use by Professional

The professional uses the certificado to:
- Verify amounts withheld match their records
- Include in annual Modelo 100 (IRPF return) as tax credits
- Support any discrepancy claims with AEAT

## Section 8 -- Edge Cases

### 8.1 Mixed Invoice (Goods + Services)

- **Mixed Invoice (Goods + Services)** — If a single invoice includes both goods (no retención) and professional services (retención), withholding applies ONLY to the services portion. Must be clearly separated on the invoice.

### 8.2 Professional SL (Sociedad Profesional)

- **Professional SL (Sociedad Profesional)** — When a Sociedad Limitada Profesional (SLP) renders professional services, retención may apply if the activity is listed in Section 2/3 of the IAE (actividades profesionales). Regular SLs providing services are generally NOT subject to retención.

### 8.3 Non-Resident Professional

- **Non-Resident Professional withholding** — Payments to non-resident professionals: withhold at 24% (or treaty rate) under IRNR. File on Modelo 216 (not 111). Treaty may reduce/eliminate.

### 8.4 No Activity in Quarter

- **No Activity in Quarter** — If registered as retenedor but made no payments subject to withholding in a quarter: file declaración negativa (Modelo 111 with all zeros). Failure to file may trigger penalty.

### 8.5 Late Filing Penalties

**8.5 Late Filing Penalties**

| Situation | Penalty |
| --- | --- |
| Filed late, no AEAT notification | 1% surcharge + 1% per month (up to 12 months); 15%+ after 12 months |
| Filed after AEAT notification (requerimiento) | 5%/10%/15%/20% depending on delay |
| Omission of withholding | 150% of amount not withheld (sanción grave) |

## Section 9 -- Prohibitions

- **Prohibitions list** — - NEVER apply 7% rate without written communication from the professional confirming eligibility - NEVER withhold on invoices from Sociedades Limitadas (SL) for regular services -- only professional partnerships or specific cases - NEVER apply retención to the IVA portion of an invoice -- only to the base imponible - NEVER miss a quarterly filing deadline -- file negative if no activity - NEVER issue a certificado de retenciones with amounts that don't match the Modelo 190 filing - NEVER confuse Modelo 111 (payer's obligation) with Modelo 130 (professional's own estimated tax) - NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
