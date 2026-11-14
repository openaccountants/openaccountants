---
name: spain-formation
description: "Forming a company in Spain for tax year 2026, read from the Ley de Sociedades de Capital, Ley 14/2013, the Reglamento del Registro Mercantil, the Commercial Code, the tax and social security laws and AEAT pages. Covers entity types (autónomo, SL, SLU, SA), minimum capital (EUR 1 for an SL with the reserve and liability rules below EUR 3,000; EUR 60,000 for an SA, 25% paid), name reservation, the bank certificate, the notarial deed, the provisional NIF, registration times including the fast-track route, the 2026 company tax rates, the director's RETA registration, IAE, annual accounts, audit thresholds, deposit fines and foreign founders. Trigger on 'set up a company in Spain', 'SL formation', 'sociedad limitada', 'Registro Mercantil', 'Spanish company formation', 'register a business Spain', 'CIF Spain', 'autónomo societario', 'NIF', 'escritura de constitución'. For tax computations see es-corporate-tax, es-social-contributions and spain-tax-optimization."
version: 2.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - company-formation-workflow-base
category: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Spain Formation

## Scope

**Spain Company Formation Skill v2.0.** Forming a company in Spain in 2026: entity choice, capital, registration in the order the founder meets it, first-year compliance and foreign founders. Tax computations belong to `es-corporate-tax`, `es-social-contributions` and `spain-tax-optimization`.

### Quick reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Spain (Kingdom of Spain) |
| Currency | EUR; share capital is stated in euros (LSC art 4) |
| Company registrar | Registro Mercantil (Provincial) + Registro Mercantil Central (name reservation) |
| Key legislation | Real Decreto Legislativo 1/2010 (Ley de Sociedades de Capital, LSC); Ley 18/2022 (Crea y Crece); Ley 14/2013 (emprendedores); Reglamento del Registro Mercantil (RD 1784/1996, RRM); Código de Comercio |
| Typical formation time | Statutory limits: name certificate within 3 working days, registration within 15 days of filing. Fast track (standard bylaws, CIRCE/PAE): name certificate within 6 working hours, notary appointment within 12 working hours, registration within 6 working hours (see Section 10) |
| Corporate tax rate | Periods starting in 2026: 25% general; previous-year turnover under EUR 1 million 19% on the first EUR 50,000 and 21% on the rest; other small companies 23%; new companies 15% in the first profitable period and the next (LIS art 29.1, DT 44.2). Detail: [es-corporate-tax](es-corporate-tax.md) |
| Skill version | 2.0 |

### Entity types compared

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

## Ask the client first

- Which entity: autónomo, S.L., S.L.U. or S.A.? With how many founders, and who holds what share of the capital?
- How much capital, and is it cash or in kind? Below EUR 3,000 the reserve and liability rules apply; in-kind contributions carry founder liability.
- Will a director work for the company for pay and hold effective control (half the capital, or the presumptions in LGSS art 305.2.b)? Then RETA registration and its cost follow.
- Are any founders or directors foreign, and do they already have an NIE or tax-assigned NIF? This is the usual bottleneck.
- Will the company use standard bylaws (estatutos tipo) through CIRCE, for the fast track, or bespoke bylaws?
- Will it hire staff, rent premises or pay professionals from day one? Each adds a withholding return.

## Rates, bands and thresholds

Every figure the method below uses, for formations and first periods in 2026. Each was found on the linked consolidated BOE text on 14 November 2026.

| Item | Figure | Condition | Source |
|---|---|---|---|
| S.L. minimum capital | EUR 1 | LSC art 4.1, as amended by Ley 18/2022 | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| S.L. reserve and liability threshold | EUR 3 thousand ("tres mil euros", LSC art. 4) | While capital is below it: 20% of profit to the legal reserve until reserve plus capital reach EUR 3 thousand; members jointly liable on a short liquidation for EUR 3 thousand less capital (LSC art 4.1) | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| S.A. minimum capital | EUR 60,000 | LSC art 4.2 | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| S.A. minimum paid up at the deed | 25% of the nominal value of each share | LSC art 79; S.L. shares fully paid (art 78) | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| Audit exemption | Total assets up to EUR 2.85 million ("dos millones ochocientos cincuenta mil euros"); net turnover up to EUR 5.7 million ("cinco millones setecientos mil euros"); average staff up to 50 | Two of three, on two consecutive year ends (LSC art 263) | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| Fine for not depositing accounts | EUR 1,200 to EUR 60,000; up to EUR 300,000 a year of delay if turnover is above EUR 6,000,000 | LSC art 283.1, imposed by the ICAC | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| Corporate tax, general rate | 25% | LIS art 29.1 | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Corporate tax, prior year turnover under EUR 1 million, periods starting in 2026 | 19% on the first EUR 50,000; 21% on the rest | LIS DT 44.2.a | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Corporate tax, other small companies (art 101), periods starting in 2026 | 23% | LIS DT 44.2.b | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Corporate tax, new company | 15% in the first period with positive base and the next | LIS art 29.1, economic activity, not a continuation | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Autónomo societario minimum base, 2026 | EUR 1,424.40 a month | Group 7 minimum of the General regime, once 90 days registered in the year (LGSS art 308.1.a.4ª; Orden PJC/297/2026 art 3) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 ; https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| RETA rates, 2026 | 28.30% common, 1.30% professional, 0.90% intergenerational equity (MEI), 0.90% cessation, 0.10% training: 31.50% in all (computed) | Orden PJC/297/2026 arts 18.2 and 37 | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| IAE exemption | First two tax periods of a new activity; companies with net turnover under EUR 1,000,000 | TRLRHL art 82.1.b and c | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 |
| Name certificate | Up to 3 names; decided within 3 working days; reservation 6 months; certificate valid 3 months for the deed | RRM arts 410.1, 411.1, 412.1, 414.1 | https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533 |
| Fast track (estatutos tipo, CIRCE) | Up to 5 names, certificate within 6 working hours; notary within 12 working hours; registration within 6 working hours | Ley 14/2013 art 15.3 and 15.5 | https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074 |
| Bank deposit certificate | Valid 2 months | LSC art 62.3 | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 |
| Provisional NIF | Assigned within 10 days | RGAT art 24.1 | https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 |
| Registration of the deed | Within 15 days of the filing entry | Código de Comercio art 18.4 | https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627 |
| Legalisation of books | Within 4 months of year end | Ley 14/2013 art 18.1 | https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074 |

## The method, step by step

#### Step 1: Reserve Company Name (Certificación Negativa de Denominación)

- **Reserve company name** -- Apply to the Registro Mercantil Central. An ordinary request may list up to three names (RRM art 410.1); the fast-track route allows up to five (Ley 14/2013 art 15.3.b). The Registrar decides within three working days (RRM art 411.1). The name is reserved for six months from the certificate (RRM art 412.1). The certificate itself is valid for three months to grant the deed; after that a new one is requested (RRM art 414.1).

#### Step 2: Open Bank Account and Deposit Capital

- **Open bank account and deposit capital** -- Open an account in the company's name and deposit the cash capital. The notary attaches the bank's deposit certificate to the deed; the certificate is valid for two months (LSC art 62.1, 62.3). For an S.L. the founders may instead declare in the deed that they are jointly liable for the cash contributions, and then no certificate is needed (LSC art 62.2).

#### Step 3: Draft Estatutos Sociales (Articles of Association)

- **Draft estatutos sociales** -- Include: company name, registered office, objects, capital, share distribution, governance structure. Standard bylaws (estatutos tipo) in standard format can be used with the fast-track route (Ley 14/2013 art 15.1-15.2).

#### Step 4: Sign Escritura de Constitución Before Notary

- **Sign escritura de constitución before notary** -- All founders must appear (or be represented under a power of attorney). Bring: NIE/DNI, bank certificate (or the S.L. joint-liability declaration), name certificate, estatutos. Notary fees are set by the official tariff; see Not yet confirmed.

#### Step 5: Obtain NIF Provisional (Tax ID)

- **Obtain NIF provisional** -- Apply to the Agencia Tributaria (AEAT) with Modelo 036. AEAT assigns the number within 10 days. The NIF stays provisional until the company provides the deed, the bylaws and the registration certificate, which it must do within one month of registration (RGAT arts 24.1-24.3). In the fast-track route the notary asks AEAT for the provisional NIF immediately through CIRCE (Ley 14/2013 art 15.4.b). "CIF" is the old name for a company's NIF.

#### Step 6: File with Registro Mercantil Provincial

- **File with Registro Mercantil Provincial** -- Submit the escritura to the provincial mercantile registry. The registrar must register it within 15 days of the filing entry (Código de Comercio art 18.4). The company gains legal personality on registration (LSC art 33). Company formation is exempt from the capital-duty part of ITP-AJD (operaciones societarias), and the registry receives proof of the exemption (Ley 14/2013 art 15.5).

#### Step 7: Register for Taxes and Social Security

- **Register for taxes and social security** -- Modelo 036: register for Impuesto sobre Sociedades and IVA with AEAT. Autónomo societario: a director or manager who works for the company for pay, habitually, personally and directly, and has effective control of it (at least half the capital, or the presumptions below) must register in RETA (LGSS art 305.2.b). Register as employer with the Tesorería General de la Seguridad Social if hiring.

### Capital requirements

**Capital Requirements table**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| S.L. | €1 (legal min. since 2022) | 100% of subscribed capital (LSC art 78) | At constitution | Permitted. Founders are jointly liable for the reality and stated value of in-kind contributions (LSC art 73); the liability lapses five years after the contribution (LSC art 75). An expert valuation removes it (LSC art 76). |
| S.L. (recommended) | €3,000 | 100% | At constitution | Permitted |
| S.A. | €60,000 (LSC art 4.2) | 25% of the nominal value of each share (€15,000 on €60,000) (LSC art 79) | At constitution | Permitted (independent expert report required, LSC art 67) |

### Costs

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

#### Annual Maintenance

**Annual Maintenance table**

| Item | Cost (EUR) |
| --- | --- |
| Autónomo societario (administrador) | Final 2026 base at least €1,424.40 a month once registered 90 days in the year (LGSS art 308.1.a.4ª; Orden PJC/297/2026 arts 3 and 18.4). At 31.50% that is €448.69 a month (12 × €448.69 = €5,384.28 a year). Detail: [es-social-contributions](es-social-contributions.md) |
| Asesoría fiscal / gestoría | Market price |
| Registro Mercantil (cuentas anuales deposit) | Registry fee |
| Impuesto sobre Actividades Económicas (IAE) | Exempt in the first two tax periods of a new activity, and for companies with net turnover under €1,000,000 (TRLRHL art 82.1.b-c) |

### Post-formation compliance

**Post-Formation Compliance table**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Cuentas anuales (annual accounts) | Directors prepare them within 3 months of year end (LSC art 253.1); the general meeting approves them within the first 6 months (LSC art 164.1); deposit within 1 month of approval (LSC art 279.1) | Registro Mercantil |
| Impuesto sobre Sociedades (corporate tax) | Within 25 calendar days after the 6 months following year end: 1-25 July for a calendar year (LIS art 124.1) | AEAT |
| IVA declarations | Quarterly Modelo 303 by the 20th of April, July and October and by 30 January (RIVA art 71.4) + annual summary Modelo 390 in January | AEAT |
| Retenciones (withholding returns) | Quarterly, first 20 days of April, July, October and January (Modelo 111 for salaries and professionals; Modelo 115 for rent); monthly for large companies (RIRPF art 108.1) | AEAT |
| Titularidad real (UBO) | The company must obtain, keep and update information on its beneficial owners (Ley 10/2010 art 4 bis.1) | Registro Mercantil / Registro de Titularidades Reales |
| Legalización de libros (book legalisation) | Electronically, within 4 months of year end (Ley 14/2013 art 18.1) | Registro Mercantil |

### Bank account opening

#### Documents Typically Required

- **Documents typically required** -- Escritura de constitución (registered, or the unregistered deed for opening). NIF. NIE or DNI of all founders and directors. Proof of address. Business activity description. Banks must identify the beneficial owner before opening the relationship (Ley 10/2010 art 4.1).

#### Typical Timeline

- **Typical timeline for bank account opening** -- Set by each bank; see Not yet confirmed. The capital deposit certificate is valid for two months (LSC art 62.3).

#### Common Banks

Bank choice is commercial. Both traditional and digital banks issue the deposit certificate the notary needs. See Not yet confirmed.

### Foreign founders

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

### Timeline

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

## Worked cases

### Case 1: EUR 1 capital or EUR 3,000? (a decision)

Two founders form an S.L. that makes a profit of EUR 10,000 in its first year. With EUR 1 of capital, LSC art 4.1 sends at least 20% of profit, EUR 2,000, to the legal reserve, and that continues until reserve plus capital reach EUR 3,000 (a further EUR 999 the next year). On a short liquidation meanwhile, the members answer jointly for EUR 2,999. With EUR 3,000 of capital paid in, none of this applies. The figure that decides is the EUR 2,999 gap: a founder who can put in EUR 3,000 at the deed avoids both rules; one who cannot accepts a reserve that locks up EUR 2,999 of profit over two years.

```oa-check
name: Spain 2026 S.L. EUR 1 capital legal reserve
inputs:
  capital: 1
  floor: 3000
  profit_year1: 10000
  reserve_rate: 0.20
steps:
  - gap: floor - capital
  - reserve_year1: min(profit_year1 * reserve_rate, gap)
  - reserve_still_needed: gap - reserve_year1
expected:
  gap: 2999
  reserve_year1: 2000
  reserve_still_needed: 999
```

### Case 2: the controlling director's RETA cost

A director with 60% of the capital works for the company for pay, so registers in RETA (LGSS art 305.2.b). After 90 days in the year the base cannot be below EUR 1,424.40 a month. At 31.50% (Orden PJC/297/2026 arts 18.2 and 37) that is EUR 448.69 a month and EUR 5,384.28 a year.

```oa-check
name: Spain 2026 autonomo societario minimum RETA cost
inputs:
  base: 1424.40
  rate: 0.3150
steps:
  - monthly: round(base * rate, 2)
  - yearly: monthly * 12
expected:
  monthly: 448.69
  yearly: 5384.28
```

## When to refuse or refer

- **R-ES-F1 -- Capital of €1 without understanding consequences** -- €1 is the legal minimum since 2022, but below €3,000 at least 20% of profit goes to the legal reserve, and the members are jointly liable for up to €3,000 less the capital if the company is wound up short of assets (LSC art 4.1). Always advise on these constraints before proceeding.
- **R-ES-F2 -- Forgetting autónomo societario obligation** -- A director with effective control must register in RETA and pay contributions; from 90 days registered the final 2026 base is at least €1,424.40 a month (about €448.69 at 31.50%). This is a significant ongoing cost that founders frequently overlook.
- **R-ES-F3 -- Not depositing annual accounts** -- If the accounts are not deposited in time, the registry closes the company's sheet: no other document can be registered while the failure lasts, apart from listed exceptions such as director resignations (LSC art 282). The ICAC can also fine the company €1,200 to €60,000, or up to €300,000 a year of delay if turnover exceeds €6,000,000 (LSC art 283.1).
- **R-ES-F4 -- NIE not obtained before notary appointment** -- All founders and directors need a valid NIE or tax-assigned NIF for the deed (RGAT art 20). This is a common cause of delay for foreign founders.
- **R-ES-F5 -- Shell company request** -- This skill will not assist in forming a company without genuine economic substance. Spanish companies must obtain, keep and update their beneficial-owner information (Ley 10/2010 art 4 bis), and banks and notaries identify the beneficial owner before acting (art 4).

## Sources

| Source | What was read | URL | Read on |
| --- | --- | --- | --- |
| Real Decreto Legislativo 1/2010, Ley de Sociedades de Capital | Read for arts 1, 4, 12, 33, 62, 67, 73, 75, 76, 78, 79, 164, 253, 263, 279, 282, 283 (capital, audit, deposit and fines) | https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544 | 2026-11-14 |
| Ley 14/2013 de apoyo a los emprendedores | Read for arts 15 (fast track: 5 names, 6 and 12 working hours) and 18 (books within 4 months) | https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074 | 2026-11-14 |
| Real Decreto 1784/1996, Reglamento del Registro Mercantil | Read for arts 410, 411, 412, 414 (names, 3 working days, 6 and 3 months) | https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533 | 2026-11-14 |
| Código de Comercio | Read for art 18.4 (15 days to register) | https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627 | 2026-11-14 |
| Real Decreto 1065/2007 (RGAT) | Read for arts 20 and 24 (NIF for foreigners, provisional NIF in 10 days) | https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 | 2026-11-14 |
| Ley 27/2014 del Impuesto sobre Sociedades | Read for art 29.1 and DT 44.2 (25%, 19%/21%, 23%, 15%), arts 101 and 124 | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 | 2026-11-14 |
| Real Decreto 1624/1992 (RIVA) | Read for art 71.4 (Modelo 303 periods) | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925 | 2026-11-14 |
| Real Decreto 439/2007 (RIRPF) | Read for art 108 (withholding return periods) | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 | 2026-11-14 |
| Real Decreto Legislativo 8/2015 (LGSS) | Read for arts 305.2.b (control presumptions) and 308.1.a rule 4ª (group 7 floor after 90 days) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 | 2026-11-14 |
| Orden PJC/297/2026, 2026 contribution rules | Read for arts 3 (group 7 EUR 1,424.40), 18.2 and 37 (RETA rates) | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 | 2026-11-14 |
| Real Decreto Legislativo 2/2004 (TRLRHL) | Read for art 82.1.b and c (IAE exemptions, EUR 1,000,000) | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 | 2026-11-14 |
| Ley 10/2010 de prevención del blanqueo de capitales | Read for arts 4 and 4 bis (beneficial owner) | https://www.boe.es/buscar/act.php?id=BOE-A-2010-6737 | 2026-11-14 |
| AEAT, Modelo 390 filing period | Read for the January filing period of the annual VAT summary | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-390-iva-declaracion-resumen-anual_/plazos-presentacion.html | 2026-11-14 |

Not yet confirmed: (1) all euro fee amounts from the old file (name certificate about €16 to €22; notary €150 to €600; registry €100 to €400; gestoría €300 to €1,200; asesoría €100 to €300 a month; accounts deposit about €40 to €80; totals €270 to €2,200); the official notary and registry tariffs were not read. (2) The old practical times (name 1 to 3 days, registry 5 to 15 working days, overall 1 to 3 weeks or 4 to 5 days fast track, NIE 1 to 6 weeks, bank 1 to 5 days digital or 1 to 3 weeks traditional) have no official source; only the statutory limits are given. (3) The list of common banks (Santander, BBVA, CaixaBank, Sabadell, Qonto, Revolut Business) is commercial, not from an official source. (4) EU and non-EU differences for the NIE and any visa needed were not read. (5) How the beneficial-owner declaration is filed with the Registro Mercantil each year (the old file said "at constitution and on any change") was not read. (6) The old "around €370 a month in 2026" for the autónomo societario was replaced by the statutory floor; a director's provisional base in the first 90 days can be lower. (7) The old "Provisional CIF issued immediately" is replaced by the 10-day rule; no source says it is immediate outside the fast track. (8) The old "physical presence: power of attorney must be notarised and apostilled" is covered only by the general apostille rule in Ley 14/2013 art 15.3.a.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.
