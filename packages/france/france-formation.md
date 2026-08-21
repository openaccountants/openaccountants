---
name: france-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in France. Trigger on phrases like "set up a company in France", "SAS formation", "SARL création", "Guichet unique INPI", "French company formation", "register a business France", "société par actions simplifiée", "société à responsabilité limitée", "Kbis", "RCS registration", "annonce légale", or any question about starting a business entity in France. Covers entity types (SAS, SARL, EURL, SASU, SA, auto-entrepreneur), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on French company formation.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France Formation

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | France (French Republic) |
| Currency | EUR |
| Company registrar | Guichet unique des formalités d'entreprises (INPI) -- formalites.entreprises.gouv.fr |
| Key legislation | Code de commerce; Loi Pacte (2019); Code civil |
| Typical formation time | 7--15 working days |
| Corporate tax rate | 25% (standard); 15% on first €42,500 for SMEs |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Section 2 -- Entity Types Comparison**

| Feature | Auto-entrepreneur (Micro) | EURL/SARL | SASU/SAS | SA |
| --- | --- | --- | --- | --- |
| Legal personality | No (sole trader) | Yes | Yes | Yes |
| Liability | Unlimited | Limited to contributions | Limited to contributions | Limited to contributions |
| Min. founders | 1 | EURL: 1 / SARL: 2--100 | SASU: 1 / SAS: 2+ | 2 (non-listed) / 7 (listed) |
| Min. share capital | N/A | €1 | €1 | €37,000 |
| Governance flexibility | N/A | Low (law-defined) | Very high (statute-defined) | Low (law-defined, board required) |
| Social charges on director | ~22% on revenue | Gérant majoritaire: TNS (~45%) | Président: assimilé salarié (~80% on remuneration) | Assimilé salarié |
| Tax treatment | Income tax (micro-BIC/BNC) | IS by default (can elect IR for 5 years) | IS by default (can elect IR for 5 years) | IS |
| Admin burden | Very low | Medium | Medium | Very high |
| Audit required | No | Only if thresholds exceeded | Only if thresholds exceeded | Yes (commissaire aux comptes) |

**Recommended default:** SAS/SASU for maximum flexibility and investor compatibility. SARL/EURL for family businesses or cost-optimised structures.

## Section 3 -- Registration Process

### Step 1: Choose Company Name (Dénomination Sociale)

- **Name check and reservation** — Check availability via INPI trademark search (not mandatory but recommended); no formal name reservation process; name is secured upon RCS registration.  _(Section 3, Step 1)_

### Step 2: Draft Statuts (Articles of Association)

- **Drafting requirements** — SAS: high flexibility -- define governance, voting rights, transfer restrictions. SARL: more prescribed by Code de commerce. Can be drafted privately (sous seing privé) unless real estate contributions are involved (then notary required).  _(Section 3, Step 2)_

### Step 3: Deposit Share Capital

- **Capital deposit process** — Open a dedicated account (compte de dépôt) at a bank, notary, or Caisse des Dépôts. Deposit at least 20% (SARL) or 50% (SAS/SA) of share capital. Obtain certificat de dépôt des fonds.  _(Section 3, Step 3)_

### Step 4: Publish Annonce Légale (Legal Notice)

- **Annonce légale requirements** — Publish formation notice in a Journal d'Annonces Légales (JAL). Cost: €199 HT (€238.80 TTC) in metropolitan France for SAS (2026 rate). Must include: company name, form, capital, registered office, objects, duration, gérant/président details.  _(Section 3, Step 4)_

### Step 5: File on Guichet Unique (INPI)

- **Filing requirements** — All filings since 1 January 2023 must go through formalites.entreprises.gouv.fr. Upload: statuts, certificat de dépôt, attestation de parution JAL, identity documents, déclaration des bénéficiaires effectifs, proof of registered office. Pay fees online (card).  _(Section 3, Step 5)_

### Step 6: Obtain Kbis and SIRET

- **Kbis/SIRET issuance** — Greffe du Tribunal de commerce processes the filing. Issues Kbis (certificate of registration) and SIREN/SIRET numbers. INSEE assigns SIRET automatically (free).  _(Section 3, Step 6)_

### Step 7: Déclaration des Bénéficiaires Effectifs (UBO Register)

- **UBO declaration** — Mandatory filing concurrent with incorporation. Cost: €20.34 TTC.  _(Section 3, Step 7)_

### Step 8: Tax Registration

- **Tax registration process** — Company is automatically registered with the Service des impôts des entreprises (SIE). Obtain TVA intracommunautaire (EU VAT number) if applicable.  _(Section 3, Step 8)_

## Section 4 -- Capital Requirements

**Section 4 -- Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up at Formation | Remainder Due | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| SARL / EURL | €1 | 20% | Within 5 years | Permitted (commissaire aux apports required if value > €30,000 or > 50% of capital) |
| SAS / SASU | €1 | 50% | Within 5 years | Permitted (same apport rules) |
| SA | €37,000 | 50% | Within 5 years | Permitted (commissaire aux apports required) |

## Section 5 -- Costs Breakdown

**Section 5 -- Costs Breakdown**

| Cost Component | Amount (EUR TTC) | Notes |
| --- | --- | --- |
| Greffe / INPI registration fee | €35.59 | Commercial activity (RCS) |
| Annonce légale (SAS, metropolitan) | €238.80 | 2026 forfait; €284.40 for Réunion/Mayotte |
| Déclaration bénéficiaires effectifs | €20.34 | Mandatory |
| Bank capital deposit | €0--€100 | Varies by bank |
| **Total incompressible (government fees)** | **€294.73** | Minimum legal costs |
| Legal / accountant fees (optional) | €500--€2,000 | Statuts drafting, filing assistance |
| **Total with professional help** | **€800--€2,500** |  |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (EUR) |
| --- | --- |
| Accountant (expert-comptable) | €1,500--€5,000/year |
| Greffe annual fee (Kbis renewal) | Free (Kbis available online via MonIdenum) |
| CFE (Cotisation Foncière des Entreprises) | Variable (municipality-based) |
| Commissaire aux comptes (if required) | €3,000--€10,000/year |

## Section 6 -- Post-Formation Compliance

**Section 6 -- Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Dépôt des comptes annuels (annual accounts) | Within 6 months of year-end (7 months if filed online) | Greffe du Tribunal de commerce |
| Déclaration de résultats (corporate tax return) | Within 3 months of year-end (4 months for 31 Dec year-end) | SIE / impots.gouv.fr |
| TVA declarations | Monthly or quarterly | SIE |
| Déclaration sociale (DSN) | Monthly (if employees) | URSSAF / Net-entreprises |
| Bénéficiaires effectifs update | Within 30 days of any change | Greffe / INPI |
| Assemblée générale ordinaire | Within 6 months of year-end | Internal |
| PV d'assemblée filing | With annual accounts | Greffe |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Documents for bank account opening** — Kbis (less than 3 months old); Statuts; ID and proof of address for all dirigeants and UBOs; Certificat de dépôt (at formation stage: pre-Kbis, bank may accept draft statuts).  _(Section 7)_

### Typical Timeline

- **Bank account opening timeline** — Online banks (Qonto, Shine, Blank): 1--3 days. Traditional banks (BNP, SG, Crédit Agricole, LCL): 1--3 weeks.  _(Section 7)_

### Common Banks

- **Common Banks** — BNP Paribas, Société Générale, Crédit Agricole, LCL (traditional); Qonto, Shine (Société Générale), Blank (Crédit Agricole) (digital)  _(Section 7)_

## Section 8 -- Foreign Founder Considerations

**Section 8 -- Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident président/gérant allowed? | Yes -- no nationality or residency requirement |
| Physical presence required? | No -- power of attorney (procuration) accepted |
| Apostille requirements | Foreign documents require apostille + sworn translation (traduction assermentée) |
| Foreign ownership restrictions | None for SAS/SARL; regulated sectors may require authorisation |
| Registered office | Must be in France (domiciliation service companies permitted) |
| Numéro de sécurité sociale | Président of SAS must obtain one to pay social charges |

## Section 9 -- Common Mistakes and Refusals

- **R-FR-F1 -- Ignoring social charges on président SAS** — The président of a SAS is assimilé salarié and social charges (~80% of gross remuneration) apply even if the président is the sole shareholder. This is significantly higher than SARL gérant majoritaire TNS charges. Always model both structures before choosing.  _(R-FR-F1)_
- **R-FR-F2 -- Capital of €1 without substance** — While €1 capital is legal, it signals undercapitalisation to banks, clients, and creditors. Recommend at least €1,000--€5,000 for credibility.  _(R-FR-F2)_
- **R-FR-F3 -- Missing annonce légale** — Publication in a JAL is mandatory and must occur before filing with the Guichet unique. Omission will cause the filing to be rejected.  _(R-FR-F3)_
- **R-FR-F4 -- Failing to appoint commissaire aux comptes** — A CAC is mandatory when two of three thresholds are exceeded: total assets €5M, revenue €10M, 50 employees. SAS companies sometimes overlook this.  _(R-FR-F4)_
- **R-FR-F5 -- Auto-entrepreneur trying to raise investment** — The auto-entrepreneur regime does not support equity investment, multiple shareholders, or limited liability. Advise conversion to SAS/SARL if the client needs these features.  _(R-FR-F5)_

## Section 10 -- Timeline

**Section 10 -- Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Draft statuts | 1--5 days | Day 1--5 |
| Open bank account and deposit capital | 1--5 days | Day 2--10 |
| Publish annonce légale | 1--2 days | Day 3--12 |
| File on Guichet unique (INPI) | 1 day | Day 4--13 |
| Greffe processing | 5--10 working days | Day 9--23 |
| Kbis and SIRET received | 1--3 days after registration | Day 10--26 |
| Tax and social registrations | Automatic with Guichet unique | Day 10--26 |
| **Ready to trade** |  | **~2--4 weeks** |

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
