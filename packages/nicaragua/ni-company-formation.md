---
name: ni-company-formation
description: >
  Use this skill to set up a business in Nicaragua in 2026 and register it with the DGI.
  It walks through the choice of vehicle (sociedad anonima, other commercial companies,
  branch, individual trader), the notarial deed and the Registro Publico Mercantil, the
  RUC at the DGI and access to the Ventanilla Electronica Tributaria, INSS employer
  registration, and the tax consequences of the first three years, when a business set
  up with new investment is excepted from the pago minimo definitivo (Ley 822 art. 59 as
  reformed by Ley 987). Trigger phrases include constituir empresa Nicaragua, sociedad
  anonima, RUC DGI, VET, registro mercantil and pago minimo definitivo primeros tres anos.
version: "1.0"
jurisdiction: NI
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Nicaragua company formation and tax registration, 2026

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed by a Nicaraguan accountant or lawyer. Company formation needs a Nicaraguan notary.

## Scope

Setting up a business in Nicaragua and registering it for tax: the steps from deed to first returns and the tax facts that differ in the first years. Drafting by-laws, foreign investment registration, licences for regulated sectors and incentive regimes (free zones, tourism) are out of scope.

## Ask the client first

1. Who owns the business, and are any owners foreign?
2. What activity, where, and expected gross income (above or below C$12,000,000 changes the income tax table)?
3. Is the business built on new investment, or on used local assets or an existing business (PMD exception)?
4. Will it employ staff from the start (INSS)?
5. Is any incentive regime sought?

## The method, step by step

1. **Choose the vehicle.** The sociedad anonima is the usual company under the Codigo de Comercio; other forms are partnerships, branches of foreign companies and individual traders. Business income of all of them is taxed under the rentas de actividades economicas rules ([ni-corporate-income-tax](ni-corporate-income-tax.md)).
2. **Deed.** A Nicaraguan notary executes the deed of incorporation and by-laws.
3. **Registro Publico Mercantil.** Register the company and its books.
4. **DGI registration.** Obtain the RUC and the user for the Ventanilla Electronica Tributaria (VET); register the obligations (IR advances or PMD, IVA, retentions).
5. **First months.** File the monthly declaration of recaudos y anticipos by the 15th of the following month, even with no activity (LCT art. 69.4).
6. **PMD exception.** During the first three years of operations, a business set up with new investment is excepted from the pago minimo definitivo (art. 59.1). It still pays monthly advances of 1% of gross income on account of annual IR when it is excepted from the PMD (DGI FAQ). Not covered: consortia, businesses moved from the simplified regime, and investments in used local assets.
7. **Employer registration** with the INSS if hiring ([nicaragua-social-contributions](nicaragua-social-contributions.md)).
8. **Municipal registration** with the municipality (local taxes not covered here).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| New company with new investment, years 1 to 3 | No PMD; IR on profit at 30%; 1% advances on account |
| Company formed to take over an existing business with used assets | No PMD exception |
| Small trader | Cuota fija or the art. 52 table; refer |
| Annual return | By the last day of February (art. 69.1 as reformed) |

## Worked cases

### Case: a new company in its second year, PMD or not

Gross income C$20,000,000, renta neta C$200,000, new investment, second year of operations. Without the exception the tax would be the PMD of 1%, C$200,000. With the art. 59.1 exception the tax is IR of 30% on profit, C$60,000. The exception is worth C$140,000 this year.

```oa-check
name: NI 2026 new company PMD exception
inputs:
  gross: 20000000
  net: 200000
steps:
  - ir: net * 0.30
  - pmd: gross * 0.01
  - tax_without_exception: max(ir, pmd)
  - tax_with_exception: ir
  - value_of_exception: tax_without_exception - tax_with_exception
expected:
  ir: 60000
  pmd: 200000
  tax_without_exception: 200000
  tax_with_exception: 60000
  value_of_exception: 140000
```

## When to refuse or refer

- Drafting the deed, by-laws or shareholder agreements: refer to a notary or lawyer.
- Free zone, tourism or other incentive applications: refer.
- Regulated activities: refer.

## Filing and payment

| Step | Where |
| --- | --- |
| Deed | Notary |
| Commercial registration | Registro Publico Mercantil |
| Tax registration and returns | DGI, Ventanilla Electronica Tributaria |
| Social security | INSS |

## Completion checklist

- Deed registered and books stamped.
- RUC issued and VET user active.
- Monthly declaration filed from the first month, including nil months.
- PMD exception documented (proof of new investment).
- INSS registration for staff.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Ley 987 (La Gaceta 41, 28 Feb 2019): reformed arts. 59, 61 and 69 | https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf | 2026-11-14 |
| Read for DGI FAQ, Anticipos a cuenta: 1% advances for those excepted from PMD, due by the 15th, nil returns | https://www.dgi.gob.ni/FAQ/anticipos_a_cuenta.htm | 2026-11-14 |
| Read for DGI FAQ, Pago minimo definitivo: art. 59 exceptions, start of operations | https://www.dgi.gob.ni/FAQ/pago_minimo_definitivo.htm | 2026-11-14 |

Not yet confirmed: minimum shareholders and capital of a sociedad anonima and registry fees (the old file's figures came from a vendor site); RUC document list; municipal taxes (the old file cited 1% monthly and 2% annual registration); incorporation times.
