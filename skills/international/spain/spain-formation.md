---
name: spain-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Spain. Trigger on phrases like "set up a company in Spain", "SL formation", "sociedad limitada", "Registro Mercantil", "Spanish company formation", "register a business Spain", "CIF Spain", "autónomo societario", "NIF", "escritura de constitución", or any question about starting a business entity in Spain. Covers entity types (SL, SA, autónomo, sociedad civil), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Spanish company formation.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Formation

## Spain Company Formation Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Spain (Kingdom of Spain) |
| Currency | EUR |
| Company registrar | Registro Mercantil (Provincial) + Registro Mercantil Central (name reservation) |
| Key legislation | Real Decreto Legislativo 1/2010 (Ley de Sociedades de Capital); Ley 18/2022 (Crea y Crece) |
| Typical formation time | 1--3 weeks (standard); 4--5 days (fast-track via PAE/CIRCE) |
| Corporate tax rate | 25% (standard); 15% (first 2 years with profits for new companies) |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison table**

| Feature | Autónomo (Sole Trader) | S.L. (Sociedad Limitada) | S.L.U. (Unipersonal) | S.A. (Sociedad Anónima) |
| --- | --- | --- | --- | --- |
| Legal personality | No | Yes | Yes | Yes |
| Liability | Unlimited | Limited to contributions | Limited | Limited |
| Min. founders | 1 | 1 (S.L.U.) or 2+ | 1 | 1 (non-listed) |
| Min. share capital | N/A | €1 (since Ley Crea y Crece 2022) | €1 | €60,000 |
| Recommended capital | N/A | €3,000 (avoid legal-reserve constraints) | €3,000 | €60,000 (25% paid up) |
| Tax treatment | IRPF (personal) | Impuesto sobre Sociedades | Impuesto sobre Sociedades | Impuesto sobre Sociedades |
| Admin burden | Low | Medium | Medium | High |
| Audit required | No | Only if thresholds exceeded | Only if thresholds exceeded | Yes (if thresholds exceeded) |

- **Recommended default entity** — S.L. (Sociedad Limitada) with €3,000 capital for most commercial purposes.
- **Note on €1 capital** — Since the Ley Crea y Crece (Ley 18/2022, 28 September 2022), the legal minimum capital for an S.L. is €1. However, if capital is below €3,000, special rules apply: 20% of profits must be allocated to legal reserves until reserves reach €3,000, and directors are jointly liable with the company for debts if the company is wound up with insufficient assets.  _(Ley 18/2022 (Crea y Crece), 28 September 2022)_

## Section 3 -- Registration Process

### Step 1: Reserve Company Name (Certificación Negativa de Denominación)

- **Reserve company name** — Apply to Registro Mercantil Central (rmc.es). Up to 5 name proposals. Cost: ~€16--€22; processing: 1--3 working days. Valid for 6 months (renewable for 3 more)

### Step 2: Open Bank Account and Deposit Capital

- **Open bank account and deposit capital** — Open account in the name of "sociedad en constitución". Deposit share capital (min. €1; recommended €3,000). Obtain certificado de ingreso (bank certificate) for notary

### Step 3: Draft Estatutos Sociales (Articles of Association)

- **Draft estatutos sociales** — Include: company name, registered office, objects, capital, share distribution, governance structure. Can use standard or custom estatutos

### Step 4: Sign Escritura de Constitución Before Notary

- **Sign escritura de constitución before notary** — All founders must appear (or be represented by poder notarial). Bring: NIE/DNI, bank certificate, name certificate, estatutos. Notary fee: €150--€600 depending on capital and complexity

### Step 5: Obtain CIF Provisional (Tax ID)

- **Obtain CIF provisional** — Apply at Agencia Tributaria (AEAT) with Modelo 036. Provisional CIF issued immediately; definitive CIF after Registro Mercantil registration

### Step 6: File with Registro Mercantil Provincial

- **File with Registro Mercantil Provincial** — Submit escritura to the provincial mercantile registry. Cost: €100--€400 depending on capital and region. Processing: 5--15 working days. Company legally exists upon registration

### Step 7: Register for Taxes and Social Security

- **Register for taxes and social security** — Modelo 036: register for Impuesto sobre Sociedades and IVA with AEAT. Autónomo societario: the administrador must register with Seguridad Social (~€370/month in 2026). Register as employer with Tesorería General de la Seguridad Social (if hiring)

## Section 4 -- Capital Requirements

**Capital Requirements table**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| S.L. | €1 (legal min. since 2022) | 100% of subscribed capital | At constitution | Permitted (founders liable for valuation accuracy for 5 years) |
| S.L. (recommended) | €3,000 | 100% | At constitution | Permitted |
| S.A. | €60,000 | 25% (€15,000) | At constitution | Permitted (independent expert report required) |

## Section 5 -- Costs Breakdown

**Costs Breakdown table**

| Cost Component | Amount (EUR) | Notes |
| --- | --- | --- |
| Certificación negativa (name) | ~€16 | Registro Mercantil Central |
| Notary fees | €150--€600 | Scales with capital amount |
| Registro Mercantil Provincial | €100--€400 | Registration of escritura |
| AEAT registration (CIF) | Free | Modelo 036 |
| Share capital deposit | €3,000 (recommended) | Minimum €1 |
| **Total government/notary fees** | **€270--€1,000** | Excluding capital |
| Gestoría / legal fees (optional) | €300--€1,200 | Full formation service |
| **Total with professional help** | **€600--€2,200** | Excluding capital |

### Annual Maintenance

**Annual Maintenance table**

| Item | Cost (EUR) |
| --- | --- |
| Autónomo societario (administrador) | ~€370/month (~€4,440/year) |
| Asesoría fiscal / gestoría | €100--€300/month |
| Registro Mercantil (cuentas anuales deposit) | ~€40--€80 |
| Impuesto sobre Actividades Económicas (IAE) | Exempt if turnover < €1M |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance table**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Cuentas anuales (annual accounts) | Approve within 6 months of year-end; deposit within 1 month of approval | Registro Mercantil |
| Impuesto sobre Sociedades (corporate tax) | 25 July (for calendar year-end) | AEAT |
| IVA declarations | Quarterly (Modelo 303) + annual summary (Modelo 390) | AEAT |
| Retenciones (withholding returns) | Quarterly (Modelo 111 for salaries; Modelo 115 for rent) | AEAT |
| Titularidad real (UBO register) | At constitution and on any change | Registro Mercantil |
| Legalización de libros (book legalisation) | Within 4 months of year-end | Registro Mercantil |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Documents typically required** — Escritura de constitución inscrita en Registro Mercantil (or provisional for opening). CIF / NIF. NIE or DNI of all founders and directors. Proof of address. Business activity description

### Typical Timeline

- **Typical timeline for bank account opening** — 1--5 days (digital banks). 1--3 weeks (traditional banks)

### Common Banks

Santander, BBVA, CaixaBank, Sabadell (traditional). Qonto Spain, Revolut Business (digital)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations table**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but NIE (Número de Identidad de Extranjero) required |
| NIE for incorporation | Mandatory before notary appointment; obtainable at Spanish consulate or police station |
| Physical presence required? | Yes for notary (power of attorney possible but must be notarised and apostilled) |
| Apostille requirements | Foreign documents require apostille + sworn Spanish translation |
| Autónomo obligation | Foreign administradores must register as autónomo societario with Seguridad Social |
| EU/non-EU differences | EU citizens: simpler NIE process; non-EU: may need visa depending on activity |

## Section 9 -- Common Mistakes and Refusals

- **R-ES-F1 -- Capital of €1 without understanding consequences** — While €1 is the legal minimum since 2022, capitals below €3,000 trigger mandatory profit-reserve rules and potential joint director liability. Always advise on these constraints before proceeding.
- **R-ES-F2 -- Forgetting autónomo societario obligation** — The administrador of an S.L. must register as autónomo societario and pay social security contributions (~€370/month in 2026). This is a significant ongoing cost that founders frequently overlook.
- **R-ES-F3 -- Not depositing annual accounts** — Failure to deposit cuentas anuales with the Registro Mercantil results in the company being unable to file new deeds (cierre registral) and potential fines up to €60,000.
- **R-ES-F4 -- NIE not obtained before notary appointment** — All founders and directors must have a valid NIE before the notary can execute the escritura. This is the most common cause of delay for foreign founders.
- **R-ES-F5 -- Shell company request** — This skill will not assist in forming a company without genuine economic substance. Spanish anti-money-laundering regulations require identification of beneficial owners and real business activity.

## Section 10 -- Timeline

**Timeline table**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Obtain NIE (if foreign founder) | 1--6 weeks | Day 1--42 |
| Name reservation (certificación negativa) | 1--3 days | Day 2--45 |
| Draft estatutos and prepare documents | 1--3 days | Day 3--48 |
| Open bank account and deposit capital | 1--5 days | Day 4--53 |
| Notary appointment (escritura) | 1 day | Day 5--54 |
| CIF provisional (AEAT) | 1 day | Day 6--55 |
| Registro Mercantil registration | 5--15 days | Day 11--70 |
| Social security registration | 1--3 days | Day 12--73 |
| **Ready to trade** |  | **~2--4 weeks (with NIE already in hand)** |

The bottleneck for foreign founders is obtaining the NIE, which should be started well in advance.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
