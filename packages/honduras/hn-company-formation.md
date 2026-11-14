---
name: hn-company-formation
description: >
  Use this skill to set up a business in Honduras in 2026 and register it for tax. It
  walks through the choice between acting as a persona natural con obligaciones, a
  comerciante individual and a persona juridica (sociedad anonima or sociedad de
  responsabilidad limitada), the public deed before a notary and the Registro Mercantil,
  the SAR Registro Tributario Nacional (RTN) in person or by pre-registration on the
  Oficina Virtual, then ISV, pagos a cuenta, IHSS, RAP and the municipal operating
  permit, and the first-year tax calendar. Trigger phrases include abrir empresa
  Honduras, constituir sociedad, RTN persona juridica, comerciante individual and
  registro mercantil.
version: "2.0"
jurisdiction: HN
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Honduras company formation and tax registration, 2026

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed by a Honduran accountant or lawyer. Company formation needs a Honduran notary; do not rely on this skill to form a company.

## Scope

Setting up a business in Honduras and getting it registered with SAR. Covers the four RTN types SAR recognises, the order of steps from deed to first returns, and the tax consequences of the choice. Legal drafting of the deed, foreign investment registration, licensing of regulated sectors and special regimes (ZOLI, ZOLITUR, tourism) are out of scope.

The four RTN types (SAR RTN page):

| Type | Who | Typical use |
| --- | --- | --- |
| Persona natural sin obligaciones | Individuals with no economic activity, including employees whose ISR is withheld | Bank account, property, employment |
| Persona natural con obligaciones | Individuals who file and pay because they carry on an activity | Independent professionals, trades, informal selling, landlords |
| Comerciante individual | An individual trader formally constituted by public deed (Codigo de Comercio art. 6) | A business in one person's name with mercantile status |
| Persona juridica | A legal person validly constituted (Codigo Civil art. 56): sociedad anonima, sociedad de responsabilidad limitada and others | A company with its own rights and tax duties |

## Ask the client first

1. Who will own the business, how many owners, and are any foreign?
2. What activity, where, and expected annual sales (ISV simplified regime up to L250,000; pagos a cuenta)?
3. Will it employ staff from the start (IHSS, RAP, retentions)?
4. Is any special regime (free zone, tourism, export) wanted?
5. Does the client need limited liability, or is acting in their own name enough?

## The method, step by step

1. **Choose the form.** An individual with obligaciones files Form 102 on the progressive scale (see [honduras-income-tax](honduras-income-tax.md)); a company files Form 103 at 25%, plus 5% solidarity above L1,000,000 and the 1% net assets test (see [hn-corporate-income-tax](hn-corporate-income-tax.md)). Dividends then bear 10%.
2. **Deed.** For a comerciante individual or a company, a Honduran notary executes the public deed of constitution (escritura publica) with the by-laws and capital.
3. **Registro Mercantil.** Register the deed at the Registro Mercantil of the domicile; the legal person exists from valid constitution.
4. **RTN at SAR.** Apply for the RTN of the type that fits: in person at a SAR office, or pre-register on the Oficina Virtual and collect the certificate at the office. SAR publishes the documents required for each type on its requisitos templates. An RTN is personal; do not let others use it.
5. **Tax obligations at registration.** Declare the regimes: ISV responsable (monthly return) or simplified regime; pagos a cuenta (a new taxpayer files its manifestacion within 30 days of starting, LISR art. 29); retention agent duties if it pays salaries or fees.
6. **Fiscal documents.** Arrange authorised invoices (facturas with CAI) through an SAR-certified printer or system before the first sale.
7. **Employer registrations.** IHSS and RAP affiliation for employees (RAP must be told of new hires within 60 days, Decreto 47-2024).
8. **Municipal permit.** Obtain the municipal operating permit of the municipality where the business operates.
9. **First-year calendar.** ISV and retentions by the 10th of each following month; pagos a cuenta 30 June, 30 September, 31 December; annual return by 30 April.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Employee only, no other activity | Persona natural sin obligaciones; employer withholds |
| Freelancer without a deed | Persona natural con obligaciones; no Registro Mercantil step |
| Single shop, taxable sales up to L250,000 | ISV simplified regime possible, annual sales return by 31 January |
| Foreign shareholders | Company may be formed; foreign investment and immigration steps out of scope |
| Free zone or tourism incentives | Refer |

## Worked cases

### Case: when does the new company's first pago a cuenta fall

A company starts trading on 15 March 2026. It must file its manifestacion de pagos a cuenta within 30 days, so by 14 April 2026 (day 104 of the year counted from 1 January as day 1, plus 30 from day 74). Its first quota is due 30 June 2026.

```oa-check
name: HN new company, manifestacion within 30 days of start
inputs:
  start_day_of_year: 74
  days_allowed: 30
steps:
  - deadline_day_of_year: start_day_of_year + days_allowed
expected:
  deadline_day_of_year: 104
```

Day 104 of 2026 is 14 April 2026.

## When to refuse or refer

- Drafting or reviewing the deed, by-laws or shareholder agreements: refer to a Honduran notary or lawyer.
- Regulated activities (banking, insurance, telecoms, mining): refer.
- Special regimes (ZOLI, ZOLITUR, tourism, export incentives): refer.
- Company service provider duties for third parties: refer.

## Filing and payment

| Step | Where | Output |
| --- | --- | --- |
| Deed | Notary | Escritura publica |
| Commercial registration | Registro Mercantil | Registered deed |
| Tax registration | SAR office or Oficina Virtual pre-registration | RTN certificate |
| First returns | SAR Oficina Virtual | ISV, retentions, pagos a cuenta, Form 103 |

## Completion checklist

- RTN type matches the activity.
- Deed registered before applying for a persona juridica RTN.
- ISV regime, pagos a cuenta and retention duties declared.
- Authorised invoices in place before the first sale.
- IHSS and RAP affiliation for staff.
- Municipal permit obtained.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the SAR RTN page: four RTN types, in-person and virtual-presencial application, requirement templates | https://www.sar.gob.hn/registro-tributario-nacional-rtn/ | 2026-11-14 |
| Read for LISR consolidated text, arts. 27 to 29 and 34 (period, return, manifestacion within 30 days, pagos a cuenta) | https://www.sar.gob.hn/download/ley-isr-texto-consolidado-hasta-el-acuerdo-no-sar-014-2023/?wpdmdl=17388 | 2026-11-14 |
| Read for LISV consolidated text, arts. 11-A and 12 (simplified regime, monthly return) | https://www.sar.gob.hn/download/texto-consolidado-ley-del-impuesto-sobre-ventas-decreto-ley-numero-24-actualizado-hasta-el-decreto-legislativo-no-59-2022/?wpdmdl=15324 | 2026-11-14 |
| Read for Decreto 47-2024 (RAP), notice of new hires within 60 days | https://www.sar.gob.hn/download/decreto-no-47-2024-no-36545-de-fecha-28-de-mayo-2025-contentivo-ley-del-fondo-de-reserva-laboral-de-capitalizacion-individual-administrado-por-el-regimen-de-aportaciones-privadas-rap/?wpdmdl=23131 | 2026-11-14 |

Not yet confirmed: minimum capital of a sociedad anonima and a sociedad de responsabilidad limitada and the maximum number of partners (Codigo de Comercio not read; the old file's L25,000 and L5,000 came from a vendor site); Registro Mercantil fees and times; the municipal permit rules; the exact RTN document list (requirement templates not opened).
