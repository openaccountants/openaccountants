---
name: gt-company-formation
description: >
  Use this Guatemala guide to set up a company in 2026, from the notarial deed
  to the Registro Mercantil, SAT and IGSS. Match requests such as register a
  company in Guatemala, constituir sociedad anónima, sociedad de
  responsabilidad limitada, escritura constitutiva, Registro Mercantil
  inscripción, patente de sociedad, capital mínimo Q200, arancel Registro
  Mercantil, sucursal de sociedad extranjera, NIT empresa, RTU, and branch of a
  foreign company Guatemala. It walks the steps in order, states the capital
  rules of Código de Comercio articles 90 and 92 as the Registro Mercantil
  applies them, the registry fee codes, and the tax registrations that follow.
  This Tier 2 draft supports source checking and reviewer questions; it does
  not authorise filing, payment or a legal position.
version: 1.0
jurisdiction: GT
tax_year: 2026
tax_year_notes: "Procedure as published by the Registro Mercantil (registral guide for new companies and the 2024 fee list) and SAT, read on 14 November 2026."
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Guatemala Company Formation v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders setting up a Guatemalan company, and foreign companies opening a branch, in 2026. The usual forms are the sociedad anónima (S.A., with shares, run by an administrador único or a consejo de administración, Código de Comercio art 162) and the sociedad de responsabilidad limitada (no shares; decisions in the Junta General de Socios). The company is formed by public deed before a Guatemalan notary and registered at the Registro Mercantil, then with SAT (Registro Mercantil, Guía de Sociedades Nuevas). A foreign company can register a branch, permanent or for two years.

Out of scope: banks, insurers and financial companies (special laws and Superintendencia de Bancos approval); the choice of a specific trade licence; individual traders (empresa mercantil only); company law disputes. Refer them.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Minimum paid-in capital at formation | Q200.00 | Código de Comercio art 90 as amended by Decreto 18-2017 | [Registro Mercantil, Guía de Sociedades Nuevas](https://principal.registromercantil.gob.gt/wp-content/uploads/2024/01/Guia-Registral-de-Sociedades-Nuevas.pdf) |
| Cash contributions up to | Q2,000.00 may be handed to an administrator named in the deed | Above Q2,000.00 a bank deposit in the company's name is compulsory (art 92) | same |
| Registry fee, inscription of an empresa or comerciante | Q100 (code 1) | Arancel del Registro Mercantil | [Registro Mercantil, arancel](https://principal.registromercantil.gob.gt/wp-content/uploads/2024/04/arancel_rm.pdf) |
| Registry fee, other inscriptions, appointments | Q150 (code 2) | Including the legal representative's appointment | same |
| Registry fee, inscription of a company | Variable (code 7) | Amount depends on capital; not stated on the list | same |
| Registry fee, edict | Q30 (code 9) | One slip per fee | same |
| Registry fee, publication of a new company | Q200 (code 11) | Electronic publication by the Registro | same |
| Registry fee, certification | Q50 (code 8) | | same |
| Foreign branch, base fee | Q1,500.00 plus a variable amount per thousand of assigned capital | Plus Q30 edict, Q200 publication, Q150 mandate | [Registro Mercantil, inscripción de sociedades](https://principal.registromercantil.gob.gt/inscripcion-de-sociedades-mercantiles/) |

## The base

The steps in the order a founder meets them.

1. **Name.** The denomination of an S.A. is free (Código de Comercio art 87) and must include the main object; it may use a founder's name or two founders' surnames. It must not be identical to one already registered (art 26). "Banco", "financiera" and similar words need the authorisations of the financial laws.
2. **Deed (escritura constitutiva).** Signed before a notary on protocol paper, with the formal requirements of the Código de Notariado arts 29 and 31. The deed sets the object, the capital (it may be in a foreign currency, with shares issued in that currency), the contributions (cash, or non-cash items of art 27 valued by the partners), the administration and legal representative, and the reserva legal clause exactly as Código de Comercio art 37 states it after Decreto 18-2017.
3. **Capital.** At least Q200 paid in. Cash up to Q2,000 may go to an administrator named in the deed; above Q2,000 deposit it in a bank account in the company's name and the notary records seeing the slip (arts 90 and 92).
4. **Registro Mercantil.** File the inscription request (paper or electronic through the Sede Virtual with advanced electronic signature of the notary; arts 340 and 351) with the deed and the legal representative's appointment. Pay each fee with its own slip at Banrural or online: company inscription (code 7), edict (code 9), publication (code 11), appointment (code 2). The provisional and definitive inscription stages no longer exist since Decreto 18-2017. The Registro publishes the edict in its electronic medium and issues the patente de sociedad; the object printed on it must be copied word for word from the deed.
5. **Empresa mercantil.** Register at least one empresa mercantil through which the company trades; other activities in the object need further empresas later (art 655). For SAT one economic activity is stated, the one done through that empresa.
6. **SAT.** Register the company in the Registro Tributario Unificado (RTU) to get its NIT; choose the ISR regime (profit or simplified, see `gt-corporate-income-tax`) and the IVA regime (see `guatemala-iva`); enable FEL electronic invoicing; give a domicile proof; the legal representative and the registered accountant need Agencia Virtual users and current RTU data (SAT requisitos page).
7. **Books.** Have the accounting and corporate books authorised (Registro Mercantil procedure "Autorización de libros"; SAT authorises the tax books).
8. **IGSS.** Register as an employer when hiring the first worker; see `guatemala-social-contributions`.

Assembly calls of an S.A. must be published in the Registro's electronic medium even if the deed allows electronic notice to shareholders (art 138).

## Deadlines and filing

| Step | Where | Timing |
| --- | --- | --- |
| Registro Mercantil inscription | Sede Virtual or Registro office | After the deed is signed and fees paid |
| RTU and NIT | SAT Agencia Virtual or office | After the patente is issued, before invoicing |
| First IVA and ISR returns | Declaraguate | From the first period after RTU registration: SAT-2237 within the following month, ISR as the regime requires |
| IGSS employer registration | IGSS | When the first worker is hired |

## Penalties and interest

The Registro's fee list includes a fine code (code 15, Q25). Tax penalties for late registration or returns are in the Código Tributario, not opened in this pass. Business started without RTU registration cannot issue valid FEL invoices, so buyers lose their IVA credit (LIVA art 18; see `guatemala-iva`).

## Cross-border points

- A foreign company may register a branch, indefinite or temporary for two years, with a base fee of Q1,500 plus a variable amount on the capital assigned, an edict, publication and the mandate inscription (Registro Mercantil).
- A branch is a permanent establishment for ISR (LAT art 7) and pays 5% on profit remittances to its head office (LAT art 104.1 e), see `gt-corporate-income-tax`.
- Capital may be stated in a foreign currency (Ley de Libre Negociación de Divisas, as the Registro applies it).

## Two worked examples that recompute

### Worked case 1: an S.A. with Q5,000 cash capital

Two founders sign a deed with Q5,000 paid in cash. Cash exceeds Q2,000, so the bank deposit in the company's name is compulsory. Fixed registry fees for the edict, publication and the legal representative's appointment are Q30 + Q200 + Q150 = Q380, plus Q100 for the empresa mercantil; the company inscription fee (code 7) is variable and comes on top.

```oa-check
name: S.A. formation, capital test and fixed registry fees
inputs:
  cash_capital: 5000
  minimum_capital: 200
  cash_handover_limit: 2000
  fee_edict: 30
  fee_publication: 200
  fee_appointment: 150
  fee_empresa: 100
steps:
  - headroom_over_minimum: cash_capital - minimum_capital
  - cash_over_handover_limit: max(cash_capital - cash_handover_limit, 0)
  - fixed_fees: fee_edict + fee_publication + fee_appointment + fee_empresa
expected:
  headroom_over_minimum: 4800
  cash_over_handover_limit: 3000
  fixed_fees: 480
```

## Ask the client first

1. S.A., limitada or a branch of a foreign company?
2. Founders, their identity documents and who will be administrator and legal representative?
3. Capital, currency and form of each contribution?
4. Business activity and where it will be carried on?
5. Expected turnover and margin, for the ISR and IVA regime choice?
6. Will it hire staff at the start?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Registro Mercantil, Guía de calificación registral de sociedades nuevas. Read in full for the request form, deed requirements, capital (arts 90 and 92 after Decreto 18-2017), names, objects, administration, the end of provisional inscription and publication rules | https://principal.registromercantil.gob.gt/wp-content/uploads/2024/01/Guia-Registral-de-Sociedades-Nuevas.pdf | 2026-11-14 |
| Registro Mercantil, listado de nuevos códigos de arancel (2024). Read in full for fee codes and amounts | https://principal.registromercantil.gob.gt/wp-content/uploads/2024/04/arancel_rm.pdf | 2026-11-14 |
| Registro Mercantil, inscripción de sociedades mercantiles page. Read for the foreign branch fees | https://principal.registromercantil.gob.gt/inscripcion-de-sociedades-mercantiles/ | 2026-11-14 |
| SAT, requisitos, actualización ISR régimen opcional simplificado (RTU procedure). Read for the domicile proofs, FEL and the Agencia Virtual users of the legal representative and accountant | https://portal.sat.gob.gt/portal/requisitos-tramites-agencias/actualizacion-del-impuesto-sobre-la-renta-regimen-opcional-simplificado-opcion-pago-directo/ | 2026-11-14 |
| Decreto 10-2012, LAT, TSE consolidated copy through web.archive.org. Read for arts 7 and 104 | https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf | 2026-11-14 |

Not yet confirmed: the Código de Comercio text itself (read only as the Registro quotes it), including the minimum number of founders (legacy said two); the amount of the variable company inscription fee (code 7) and the per-thousand rate for branches; the time the Registro takes (legacy said 4 to 6 weeks); legacy's Q1,200 total registry cost and its Q5,000 capital figure, both replaced by the official figures above; the Sociedad de Emprendimiento under the entrepreneurship law; the annual corporate compliance calendar at the Registro.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-11-14 | Full rewrite to the standard: steps in order from the Registro Mercantil's own guide, Q200 capital and Q2,000 deposit rule, official fee codes, SAT and IGSS steps, one recomputing case; secondary sources removed |
