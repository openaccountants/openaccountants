---
name: germany-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Germany. Trigger on phrases like "set up a company in Germany", "GmbH formation", "UG gründen", "Handelsregister", "German company formation", "register a business Germany", "Gesellschaft mit beschränkter Haftung", "Unternehmergesellschaft", "German notary", "Gewerbeanmeldung", or any question about starting a business entity in Germany. Covers entity types (GmbH, UG, AG, GbR, KG), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on German company formation.
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Formation

## Germany Company Formation Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Germany (Federal Republic of Germany) |
| Currency | EUR |
| Company registrar | Handelsregister (via local Amtsgericht / district court) |
| Key legislation | GmbH-Gesetz (GmbHG); Handelsgesetzbuch (HGB); Aktiengesetz (AktG) |
| Typical formation time | 3--6 weeks (notary to Handelsregister entry) |
| Corporate tax rate | ~30% effective (15% Körperschaftsteuer + 5.5% Solidaritätszuschlag + ~14% Gewerbesteuer) |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Einzelunternehmen (Sole Trader) | GmbH | UG (haftungsbeschränkt) | GbR / OHG / KG (Partnerships) | AG (Public Company) |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | Yes | Yes | GbR: No; OHG/KG: Yes | Yes |
| Liability | Unlimited | Limited to share capital | Limited to share capital | Unlimited (GbR/OHG); KG: limited for Kommanditist | Limited to share capital |
| Min. founders | 1 | 1 | 1 | 2 | 1 |
| Min. share capital | N/A | €25,000 | €1 | N/A | €50,000 |
| Min. paid-up at formation | N/A | €12,500 (50%) | 100% of stated capital | N/A | 25% (€12,500) |
| Tax treatment | Income tax | Corporate | Corporate | Partners taxed individually | Corporate |
| Notary required | No | Yes | Yes | No (except KG for Handelsregister) | Yes |
| Admin burden | Low | High | High | Low--Medium | Very High |

**Recommended default:** GmbH for established businesses; UG for bootstrapped startups with plan to convert to GmbH.

## Section 3 -- Registration Process

### Step 1: Draft Gesellschaftsvertrag (Articles of Association)

- **Musterprotokoll usage** — Use Musterprotokoll (standard template, §2 Abs. 1a GmbHG) for simple cases: max 3 founders, 1 Geschäftsführer, cash contributions only  _(§2 Abs. 1a GmbHG)_
- **Custom Satzung usage** — Custom Satzung for complex structures (multiple share classes, vesting, investor rights)

### Step 2: Notary Appointment (Beurkundung)

- **Notarisation requirement** — Articles must be notarised (§2 GmbHG)  _(§2 GmbHG)_
- **Video notarisation** — Video notarisation available since August 2022 for cash-only GmbH/UG
- **Notary prepares Handelsregister application** — Notary also prepares Handelsregister application

### Step 3: Open Bank Account and Deposit Capital

- **Geschäftskonto naming** — Open a Geschäftskonto in the name of "GmbH i.G." (in Gründung)
- **GmbH deposit requirement** — GmbH: deposit min. €12,500 (50% of €25,000 minimum)
- **UG deposit requirement** — UG: deposit 100% of stated share capital (min. €1)
- **Bank confirmation** — Obtain bank confirmation (Bankbestätigung) for notary

### Step 4: Handelsregister Filing

- **Electronic submission** — Notary submits electronically to the Amtsgericht
- **Registration fee** — €225 (cash contributions) or €360 (in-kind contributions) -- effective 1 June 2025  _(effective 1 June 2025)_
- **Legal existence date** — GmbH/UG legally exists from date of Handelsregister entry (§11 Abs. 1 GmbHG)  _(§11 Abs. 1 GmbHG)_

### Step 5: Gewerbeanmeldung (Trade Registration)

- **Registration requirement** — Register with local Gewerbeamt (§14 GewO)  _(§14 GewO)_
- **Fee** — €15--€65 depending on municipality

### Step 6: Tax Registration (Steuerliche Erfassung)

- **Fragebogen** — Complete Fragebogen zur steuerlichen Erfassung via ELSTER
- **Steuernummer** — Obtain Steuernummer from local Finanzamt
- **USt-IdNr** — Apply for USt-IdNr. (VAT identification number) if trading intra-EU

### Step 7: Transparenzregister (Beneficial Ownership Register)

- **Registration requirement** — Register beneficial owners with Transparenzregister (§20 GwG)  _(§20 GwG)_
- **Mandatory since 2021** — Mandatory since 2021 (no longer automatic from Handelsregister)

### Step 8: Further Registrations

- **IHK membership** — IHK (Chamber of Commerce) -- mandatory membership, automatic upon Gewerbeanmeldung
- **Berufsgenossenschaft** — Berufsgenossenschaft (employer's liability insurance, §192 SGB VII) -- mandatory even without employees  _(§192 SGB VII)_

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up at Filing | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| GmbH | €25,000 | €12,500 (50%) | Before Handelsregister filing | Permitted (triggers higher registration fee of €360) |
| UG (haftungsbeschränkt) | €1 | 100% of stated capital | Before Handelsregister filing | NOT permitted (§5a GmbHG) |
| AG | €50,000 | 25% (€12,500) | Before registration | Permitted (independent valuation required) |

- **UG profit retention rule** — 25% of annual net profit must be retained as reserves until €25,000 is accumulated, at which point the UG may convert to GmbH (§5a Abs. 3 GmbHG).  _(§5a Abs. 3 GmbHG)_

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | GmbH (EUR) | UG (EUR) | Notes |
| --- | --- | --- | --- |
| Notary fee (Musterprotokoll) | €115--€300 | €60--€150 | Based on GNotKG; scales with capital |
| Notary fee (custom Satzung) | €470--€1,500 | €300--€800 | VC-ready structures at higher end |
| Handelsregister fee | €225 | €225 | €360 if in-kind contributions |
| Gewerbeanmeldung | €15--€65 | €15--€65 | Municipality-dependent |
| Share capital deposit | €12,500 (min.) | €1 (min.) | Stays in company as working capital |
| Steuerberater (initial setup) | €500--€1,500 | €500--€1,500 | Tax registration and ELSTER |
| **Total (excl. capital)** | **€1,300--€3,600** | **€800--€2,800** |  |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (EUR) |
| --- | --- |
| IHK membership | €150--€500/year (minimum assessment) |
| Berufsgenossenschaft | From €100/year |
| Steuerberater | €2,000--€10,000/year |
| Bundesanzeiger (financial statement publication) | €50--€200 |
| Handelsregister changes | €90--€180 per entry |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Jahresabschluss (annual financial statements) | Within 6 months of year-end (11 months for small GmbH) | Bundesanzeiger (publication) |
| Offenlegung (disclosure) | Within 12 months of year-end | Bundesanzeiger |
| Körperschaftsteuererklärung (corporate tax return) | 31 July of following year (extended to Feb with Steuerberater) | Finanzamt |
| Gewerbesteuererklärung (trade tax return) | 31 July of following year | Finanzamt / municipality |
| Umsatzsteuervoranmeldung (VAT returns) | Monthly or quarterly | Finanzamt |
| Gesellschafterliste (shareholder list) | Update and file with Handelsregister on any change | Handelsregister |
| Transparenzregister | Update within 14 days of beneficial ownership changes | Transparenzregister |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Required documents** — - Handelsregisterauszug (commercial register extract) - Gesellschaftsvertrag (articles of association) - Notarised appointment of Geschäftsführer - ID (passport/Personalausweis) for all directors and shareholders (25%+) - Proof of address for all beneficial owners - Business plan or description of activities

### Typical Timeline

- **Traditional banks** — Traditional banks: 2--4 weeks (KYC process)
- **Neo-banks** — Neo-banks (Qonto, Penta/Qonto, Finom): 1--5 days
- **i.G. stage note** — Note: account can be opened in "GmbH i.G." stage before Handelsregister entry

### Common Banks

- Deutsche Bank, Commerzbank, Sparkasse, Volksbank (traditional)
- Qonto, Finom, N26 Business (digital)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident Geschäftsführer allowed? | Yes -- no residency requirement |
| Minimum German-resident director? | No legal requirement (but practical for banking and tax) |
| Video notarisation for foreigners? | Available since 2022 for cash-only formations; requires EU-compatible eID |
| Apostille requirements | Foreign documents require apostille or legalisation + certified German translation |
| Physical presence required? | Not strictly; power of attorney (Vollmacht) accepted for notary appointment |
| Foreign ownership restrictions | None for GmbH; specific sectors (defence, critical infrastructure) may require approval under AWV |

## Section 9 -- Common Mistakes and Refusals

- **R-DE-F1 -- UG with €1 capital and no plan** — While legally possible, forming a UG with only €1 capital is impractical. Banks may refuse to open accounts, and the entity cannot cover basic operating costs. Always advise a minimum of €2,000--€5,000 for credibility and operations.  _(R-DE-F1)_
- **R-DE-F2 -- Trading before Handelsregister entry** — The GmbH does not legally exist until entered in the Handelsregister. The Geschäftsführer is personally liable for obligations incurred during the 'i.G.' period. Flag this risk clearly.  _(R-DE-F2)_
- **R-DE-F3 -- Missing Transparenzregister filing** — Since 2021, automatic transfer from Handelsregister no longer applies. Failure to file with Transparenzregister can result in fines up to €150,000.  _(R-DE-F3)_
- **R-DE-F4 -- Sacheinlage in UG** — In-kind contributions (Sacheinlage) are prohibited for UG formations under §5a GmbHG. Only cash contributions are permitted.  _(R-DE-F4, §5a GmbHG)_
- **R-DE-F5 -- Ignoring Berufsgenossenschaft** — Registration with the Berufsgenossenschaft is mandatory even if the GmbH has no employees. Non-registration is an Ordnungswidrigkeit.  _(R-DE-F5)_

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Draft articles / Musterprotokoll | 1--5 days | Day 1--5 |
| Notary appointment | 1--7 days | Day 2--12 |
| Open bank account (i.G.) and deposit capital | 1--3 weeks | Day 9--33 |
| Notary files with Handelsregister | 1 day | Day 10--34 |
| Handelsregister entry | 1--3 weeks | Day 17--55 |
| Gewerbeanmeldung | 1--3 days | Day 18--58 |
| Tax registration (ELSTER) | 2--6 weeks | Day 32--100 |
| Transparenzregister | 1--2 days | Day 33--102 |
| **Ready to trade** |  | **~4--8 weeks** |

The main bottleneck is Handelsregister processing time, which varies significantly by court district.

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
