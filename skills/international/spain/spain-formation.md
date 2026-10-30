---
name: spain-formation
description: "Forming a company in Spain for tax year 2026, read from the Ley de Sociedades de Capital, Ley 14/2013, the Reglamento del Registro Mercantil, the Commercial Code, the tax and social security laws and AEAT pages. Covers entity types (autónomo, SL, SLU, SA), minimum capital (EUR 1 for an SL with the reserve and liability rules below EUR 3,000; EUR 60,000 for an SA, 25% paid), name reservation, the bank certificate, the notarial deed, the provisional NIF, registration times including the fast-track route, the 2026 company tax rates, the director's RETA registration, IAE, annual accounts, audit thresholds, deposit fines and foreign founders. Trigger on 'set up a company in Spain', 'SL formation', 'sociedad limitada', 'Registro Mercantil', 'Spanish company formation', 'register a business Spain', 'CIF Spain', 'autónomo societario', 'NIF', 'escritura de constitución'. For tax computations see es-corporate-tax, es-social-contributions and spain-tax-optimization."
version: 1.1
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Formation

## Spain Company Formation Skill v1.1

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Spain (Kingdom of Spain) |
| Currency | EUR; share capital is stated in euros (LSC art 4) |
| Company registrar | Registro Mercantil (Provincial) + Registro Mercantil Central (name reservation) |
| Key legislation | Real Decreto Legislativo 1/2010 (Ley de Sociedades de Capital, LSC); Ley 18/2022 (Crea y Crece); Ley 14/2013 (emprendedores); Reglamento del Registro Mercantil (RD 1784/1996, RRM); Código de Comercio |
| Typical formation time | Statutory limits: name certificate within 3 working days, registration within 15 days of filing. Fast track (standard bylaws, CIRCE/PAE): name certificate within 6 working hours, notary appointment within 12 working hours, registration within 6 working hours (see Section 10) |
| Corporate tax rate | Periods starting in 2026: 25% general; previous-year turnover under EUR 1 million 19% on the first EUR 50,000 and 21% on the rest; other small companies 23%; new companies 15% in the first profitable period and the next (LIS art 29.1, DT 44.2). Detail: [es-corporate-tax](es-corporate-tax.md) |
| Skill version | 1.1 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison table**

| Feature | Autónomo (Sole Trader) | S.L. (Sociedad Limitada) | S.L.U. (Unipersonal) | S.A. (Sociedad Anónima) |
| --- | --- | --- | --- | --- |
| Legal personality | No | Yes | Yes | Yes |
| Liability | Unlimited | Limited to contributions | Limited | Limited |
| Min. founders | 1 | 1 (S.L.U.) or 2+ | 1 | 1 (S.A.U.) |
| Min. share capital | N/A | €1 (since Ley Crea y Crece 2022) | €1 | €60,000 |
| Recommended capital | N/A | €3,000 (avoids the reserve and liability rules) | €3,000 | €60,000 (at least 25% paid up) |
| Tax treatment | IRPF (personal) | Impuesto sobre Sociedades | Impuesto sobre Sociedades | Impuesto sobre Sociedades |
| Admin burden | Low | Medium | Medium | High |
| Audit required | No | Only if thresholds exceeded | Only if thresholds exceeded | Only if thresholds exceeded |

Members of an S.L. or S.A. are not personally liable for the company's debts _(LSC art 1.2-1.3)_. A company with one member is a sociedad unipersonal (S.L.U. or S.A.U.) _(LSC art 12)_.

- **Recommended default entity** -- S.L. (Sociedad Limitada) with €3,000 capital for most commercial purposes.
- **Note on €1 capital** -- Since Ley 18/2022 (Crea y Crece), the minimum capital of an S.L. is €1. While capital is below €3,000: at least 20% of profit must go to the legal reserve until reserve plus capital reach €3,000; and if the company is wound up without enough assets to pay its debts, the members (socios) are jointly liable for the difference between €3,000 and the subscribed capital _(LSC art 4.1, as amended by Ley 18/2022 art 2.1)_. The old successive-formation regime of LSC art 4 bis was abolished by Ley 18/2022 art 2.2, so the rule is in art 4.1, not art 4 bis.
- **Audit thresholds** -- An S.L. or S.A. is exempt from audit if, on two consecutive year ends, it meets at least two of: total assets not over €2,850,000; net turnover not over €5,700,000; average staff not over 50. In its first year a company is exempt if it meets two of the three at that year end _(LSC art 263)_.

## Section 3 -- Registration Process

### Step 1: Reserve Company Name (Certificación Negativa de Denominación)

- **Reserve company name** -- Apply to the Registro Mercantil Central. An ordinary request may list up to three names (RRM art 410.1); the fast-track route allows up to five (Ley 14/2013 art 15.3.b). The Registrar decides within three working days (RRM art 411.1). The name is reserved for six months from the certificate (RRM art 412.1). The certificate itself is valid for three months to grant the deed; after that a new one is requested (RRM art 414.1).

### Step 2: Open Bank Account and Deposit Capital

- **Open bank account and deposit capital** -- Open an account in the company's name and deposit the cash capital. The notary attaches the bank's deposit certificate to the deed; the certificate is valid for two months (LSC art 62.1, 62.3). For an S.L. the founders may instead declare in the deed that they are jointly liable for the cash contributions, and then no certificate is needed (LSC art 62.2).

### Step 3: Draft Estatutos Sociales (Articles of Association)

- **Draft estatutos sociales** -- Include: company name, registered office, objects, capital, share distribution, governance structure. Standard bylaws (estatutos tipo) in standard format can be used with the fast-track route (Ley 14/2013 art 15.1-15.2).

### Step 4: Sign Escritura de Constitución Before Notary

- **Sign escritura de constitución before notary** -- All founders must appear (or be represented under a power of attorney). Bring: NIE/DNI, bank certificate (or the S.L. joint-liability declaration), name certificate, estatutos. Notary fees are set by the official tariff; see Not yet confirmed.

### Step 5: Obtain NIF Provisional (Tax ID)

- **Obtain NIF provisional** -- Apply to the Agencia Tributaria (AEAT) with Modelo 036. AEAT assigns the number within 10 days. The NIF stays provisional until the company provides the deed, the bylaws and the registration certificate, which it must do within one month of registration (RGAT arts 24.1-24.3). In the fast-track route the notary asks AEAT for the provisional NIF immediately through CIRCE (Ley 14/2013 art 15.4.b). "CIF" is the old name for a company's NIF.

### Step 6: File with Registro Mercantil Provincial

- **File with Registro Mercantil Provincial** -- Submit the escritura to the provincial mercantile registry. The registrar must register it within 15 days of the filing entry (Código de Comercio art 18.4). The company gains legal personality on registration (LSC art 33). Company formation is exempt from the capital-duty part of ITP-AJD (operaciones societarias), and the registry receives proof of the exemption (Ley 14/2013 art 15.5).

### Step 7: Register for Taxes and Social Security

- **Register for taxes and social security** -- Modelo 036: register for Impuesto sobre Sociedades and IVA with AEAT. Autónomo societario: a director or manager who works for the company for pay, habitually, personally and directly, and has effective control of it (at least half the capital, or the presumptions below) must register in RETA (LGSS art 305.2.b). Register as employer with the Tesorería General de la Seguridad Social if hiring.

## Section 4 -- Capital Requirements

**Capital Requirements table**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| S.L. | €1 (legal min. since 2022) | 100% of subscribed capital (LSC art 78) | At constitution | Permitted. Founders are jointly liable for the reality and stated value of in-kind contributions (LSC art 73); the liability lapses five years after the contribution (LSC art 75). An expert valuation removes it (LSC art 76). |
| S.L. (recommended) | €3,000 | 100% | At constitution | Permitted |
| S.A. | €60,000 (LSC art 4.2) | 25% of the nominal value of each share (€15,000 on €60,000) (LSC art 79) | At constitution | Permitted (independent expert report required, LSC art 67) |

## Section 5 -- Costs Breakdown

**Costs Breakdown table**

| Cost Component | Amount (EUR) | Notes |
| --- | --- | --- |
| Certificación negativa (name) | Registry fee | Registro Mercantil Central |
| Notary fees | Official tariff | Scales with capital amount |
| Registro Mercantil Provincial | Official tariff | Registration of escritura |
| AEAT registration (NIF) | Modelo 036 | |
| ITP-AJD on formation | Exempt | Operaciones societarias exemption (Ley 14/2013 art 15.5) |
| Share capital deposit | €3,000 (recommended) | Minimum €1 |
| Gestoría / legal fees (optional) | Market price | Full formation service |

The euro amounts of the fees are on the Not yet confirmed line.

### Annual Maintenance

**Annual Maintenance table**

| Item | Cost (EUR) |
| --- | --- |
| Autónomo societario (administrador) | Final 2026 base at least €1,424.40 a month once registered 90 days in the year (LGSS art 308.1.a.4ª; Orden PJC/297/2026 arts 3 and 18.4). At 31.50% that is €448.69 a month (12 × €448.69 = €5,384.28 a year). Detail: [es-social-contributions](es-social-contributions.md) |
| Asesoría fiscal / gestoría | Market price |
| Registro Mercantil (cuentas anuales deposit) | Registry fee |
| Impuesto sobre Actividades Económicas (IAE) | Exempt in the first two tax periods of a new activity, and for companies with net turnover under €1,000,000 (TRLRHL art 82.1.b-c) |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance table**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Cuentas anuales (annual accounts) | Directors prepare them within 3 months of year end (LSC art 253.1); the general meeting approves them within the first 6 months (LSC art 164.1); deposit within 1 month of approval (LSC art 279.1) | Registro Mercantil |
| Impuesto sobre Sociedades (corporate tax) | Within 25 calendar days after the 6 months following year end: 1-25 July for a calendar year (LIS art 124.1) | AEAT |
| IVA declarations | Quarterly Modelo 303 by the 20th of April, July and October and by 30 January (RIVA art 71.4) + annual summary Modelo 390 in January | AEAT |
| Retenciones (withholding returns) | Quarterly, first 20 days of April, July, October and January (Modelo 111 for salaries and professionals; Modelo 115 for rent); monthly for large companies (RIRPF art 108.1) | AEAT |
| Titularidad real (UBO) | The company must obtain, keep and update information on its beneficial owners (Ley 10/2010 art 4 bis.1) | Registro Mercantil / Registro de Titularidades Reales |
| Legalización de libros (book legalisation) | Electronically, within 4 months of year end (Ley 14/2013 art 18.1) | Registro Mercantil |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Documents typically required** -- Escritura de constitución (registered, or the unregistered deed for opening). NIF. NIE or DNI of all founders and directors. Proof of address. Business activity description. Banks must identify the beneficial owner before opening the relationship (Ley 10/2010 art 4.1).

### Typical Timeline

- **Typical timeline for bank account opening** -- Set by each bank; see Not yet confirmed. The capital deposit certificate is valid for two months (LSC art 62.3).

### Common Banks

Bank choice is commercial. Both traditional and digital banks issue the deposit certificate the notary needs. See Not yet confirmed.

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations table**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but each needs a Spanish tax number |
| NIE for incorporation | A foreign individual's tax number (NIF) is the NIE. A foreigner without an NIE asks AEAT to assign an NIF before any operation with tax effects (RGAT art 20.1-20.2) |
| Physical presence required? | Yes for the notary, or a power of attorney |
| Apostille requirements | Documents in a foreign language need a sworn translation into Spanish (or the other official language of the province), and foreign public documents need an apostille or legalisation, unless a law or treaty exempts them (Ley 14/2013 art 15.3.a) |
| Autónomo obligation | A director with effective control of the company who works for it for pay registers in RETA (LGSS art 305.2.b), if Spanish social security applies to them |
| EU/non-EU differences | See Not yet confirmed |

**Effective control presumptions (LGSS art 305.2.b):** control is assumed with at least half the capital, and presumed unless disproved where: half the capital is held by family members up to the second degree who live with the person; the person holds at least one third; or the person holds at least one quarter and has management functions.

## Section 9 -- Common Mistakes and Refusals

- **R-ES-F1 -- Capital of €1 without understanding consequences** -- €1 is the legal minimum since 2022, but below €3,000 at least 20% of profit goes to the legal reserve, and the members are jointly liable for up to €3,000 less the capital if the company is wound up short of assets (LSC art 4.1). Always advise on these constraints before proceeding.
- **R-ES-F2 -- Forgetting autónomo societario obligation** -- A director with effective control must register in RETA and pay contributions; from 90 days registered the final 2026 base is at least €1,424.40 a month (about €448.69 at 31.50%). This is a significant ongoing cost that founders frequently overlook.
- **R-ES-F3 -- Not depositing annual accounts** -- If the accounts are not deposited in time, the registry closes the company's sheet: no other document can be registered while the failure lasts, apart from listed exceptions such as director resignations (LSC art 282). The ICAC can also fine the company €1,200 to €60,000, or up to €300,000 a year of delay if turnover exceeds €6,000,000 (LSC art 283.1).
- **R-ES-F4 -- NIE not obtained before notary appointment** -- All founders and directors need a valid NIE or tax-assigned NIF for the deed (RGAT art 20). This is a common cause of delay for foreign founders.
- **R-ES-F5 -- Shell company request** -- This skill will not assist in forming a company without genuine economic substance. Spanish companies must obtain, keep and update their beneficial-owner information (Ley 10/2010 art 4 bis), and banks and notaries identify the beneficial owner before acting (art 4).

## Section 10 -- Timeline

**Timeline table**

| Step | Duration | Source |
| --- | --- | --- |
| Obtain NIE (if foreign founder) | See Not yet confirmed | |
| Name reservation (certificación negativa) | Within 3 working days (fast track: 6 working hours) | RRM art 411.1; Ley 14/2013 art 15.3.b |
| Draft estatutos and prepare documents | Founders' own time | |
| Open bank account and deposit capital | Set by the bank; certificate valid 2 months | LSC art 62.3 |
| Notary appointment (escritura) | Fast track: within 12 working hours of starting | Ley 14/2013 art 15.3.c |
| NIF provisional (AEAT) | Within 10 days | RGAT art 24.1 |
| Registro Mercantil registration | Within 15 days of filing (fast track: 6 working hours) | Código de Comercio art 18.4; Ley 14/2013 art 15.5.a |
| Social security registration | Before starting work | [es-social-contributions](es-social-contributions.md) |

The bottleneck for foreign founders is obtaining the NIE, which should be started well in advance.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Real Decreto Legislativo 1/2010, Ley de Sociedades de Capital, consolidated text (last update 03/01/2025), arts 1, 4, 4 bis (abolished), 12, 33, 62, 67, 73, 75, 76, 78, 79, 164, 253, 263, 279, 282, 283 | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 | 2026-10-30 |
| Ley 14/2013 de apoyo a los emprendedores, consolidated text, arts 15 and 18 | https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074 | 2026-10-30 |
| Real Decreto 1784/1996, Reglamento del Registro Mercantil, consolidated text, arts 410, 411, 412, 414 | https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533 | 2026-10-30 |
| Código de Comercio, consolidated text, art 18 | https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627 | 2026-10-30 |
| Real Decreto 1065/2007 (RGAT), consolidated text, arts 20 and 24 | https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 | 2026-10-30 |
| Ley 27/2014 del Impuesto sobre Sociedades, consolidated text, arts 29, 101, 124, DT 44 | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 | 2026-10-30 |
| Real Decreto 1624/1992 (RIVA), art 71 | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925 | 2026-10-30 |
| Real Decreto 439/2007 (RIRPF), art 108 | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 | 2026-10-30 |
| Real Decreto Legislativo 8/2015 (LGSS), consolidated text, arts 305 and 308 | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 | 2026-10-30 |
| Orden PJC/297/2026, 2026 contribution rules, arts 3, 18 and 37 | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 | 2026-10-30 |
| Real Decreto Legislativo 2/2004 (TRLRHL), consolidated text, art 82 | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 | 2026-10-30 |
| Ley 10/2010 de prevención del blanqueo de capitales, consolidated text, arts 4 and 4 bis | https://www.boe.es/buscar/act.php?id=BOE-A-2010-6737 | 2026-10-30 |
| AEAT, Modelo 390 filing period | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-390-iva-declaracion-resumen-anual_/plazos-presentacion.html | 2026-10-30 |

Not yet confirmed: (1) all euro fee amounts from the old file (name certificate about €16 to €22; notary €150 to €600; registry €100 to €400; gestoría €300 to €1,200; asesoría €100 to €300 a month; accounts deposit about €40 to €80; totals €270 to €2,200); the official notary and registry tariffs were not read. (2) The old practical times (name 1 to 3 days, registry 5 to 15 working days, overall 1 to 3 weeks or 4 to 5 days fast track, NIE 1 to 6 weeks, bank 1 to 5 days digital or 1 to 3 weeks traditional) have no official source; only the statutory limits are given. (3) The list of common banks (Santander, BBVA, CaixaBank, Sabadell, Qonto, Revolut Business) is commercial, not from an official source. (4) EU and non-EU differences for the NIE and any visa needed were not read. (5) How the beneficial-owner declaration is filed with the Registro Mercantil each year (the old file said "at constitution and on any change") was not read. (6) The old "around €370 a month in 2026" for the autónomo societario was replaced by the statutory floor; a director's provisional base in the first 90 days can be lower. (7) The old "Provisional CIF issued immediately" is replaced by the 10-day rule; no source says it is immediate outside the fast track. (8) The old "physical presence: power of attorney must be notarised and apostilled" is covered only by the general apostille rule in Ley 14/2013 art 15.3.a.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
