---
name: mf-business-licence-and-patente-filing
description: >
  French Saint-Martin business licence (droit de licence) and patente contribution for 2026 under the collectivity's tax code consolidated to 5 June 2026. Covers who is liable (habitual non-salaried professional activity), the article 1447-0A exemptions, the 300 euro fixed fee (150 euros for itinerant and market traders), the 5 euro per square metre area fee above 40 square metres with area rounded down and capped at 2,500 euros, the reference period, creation, cessation and operator changes, the new-enterprise patente abatements, and the annual declaration before 1 July with the patente balance by 30 November. Applies to French Saint-Martin. Trigger phrases include droit de licence Saint-Martin, patente Saint-Martin, DLCP, business licence Saint-Martin, licence fee per square metre.
version: "1.0"
jurisdiction: MF
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: computation
---

# French Saint-Martin: business licence and patente filing v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Law: CGI de la collectivite de Saint-Martin, consolidated to 5 June 2026 ([CGI Saint-Martin](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf)). Amounts in euros.

## Who this applies to

Article 1447-0 imposes the annual licence and patente contribution on habitual non-salaried professional activities in Saint-Martin. Bare-property letting without services is outside that charge; furnished/equipped letting or bare letting with services requires the separate analysis specified for each operator. [CGI article 1447-0, page 420](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

Article 1447-0A contains conditional exemptions, including farmers selling their own produce/animals, persons personally fishing, specified artists selling only their own art, qualifying associations and passenger transport by bus, coach or taxi. Record the precise qualifying activity; do not exempt all businesses described as agricultural, artistic or transport-related. [CGI article 1447-0A, pages 420–421](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

This Guide uses the official code consolidated through **5 June 2026**. Underlying deliberations remain authoritative; subsequent amendments and independent review are outstanding.

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Fixed licence fee (droit fixe) | 300 euros | Ordinary case; 0 in the creation year if the declaration is filed | 2026 | [CGI Saint-Martin, art. 1447-0B](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |
| Reduced fixed fee | 150 euros | Itinerant traders and retail exclusively on stalls and markets | 2026 | same |
| Area fee (droit indiciaire) | 5 euros per square metre above 40 square metres | Net floor area in the reference period; fractions of a square metre dropped | 2026 | same |
| Area fee cap | 2,500 euros | Per taxpayer and activity, for the area fee only | 2026 | same |
| New-enterprise patente abatement | 100% in the following year, 50% in the second following year | Declaration and state-aid conditions (art. 1447-0J bis) | 2026 | [CGI Saint-Martin, art. 1447-0J bis](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |
| Annual declaration | before 1 July | With the full licence, half the patente and the additional levies | 2026 | [CGI Saint-Martin, art. 1447-0K](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |
| Patente balance | by 30 November | With half the patente additional levy | 2026 | same |
| Start during the year | before 1 July if activity starts before 1 June; within one month if after 1 June | Art. 1447-0K II | 2026 | same |

## The base

Article 1447-0B sets an ordinary fixed component of **€300**, reduced to **€150** for itinerant traders and taxpayers trading retail exclusively on stalls/markets. The area component is **€5 per square metre above 40 m²**, using the statutory floor-area definition and reference period. A fractional square metre in total premises area is rounded down. The area component for the same taxpayer and activity is capped at **€2,500**. [CGI article 1447-0B, page 421](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

For a straightforward single-premises case with eligible area A, no exemption or start-up adjustment and the ordinary fixed fee:

**Licence = €300 + min(€2,500, €5 × max(floor(A) − 40, 0)).**

| Premises area | Area component | Licence before additional levies |
|---|---:|---:|
| 40 m² | €0 | €300 |
| 40.9 m² | €0 after rounding area down | €300 |
| 100 m² | 60 × €5 = €300 | €600 |
| 600 m² | €2,800 reduced to €2,500 cap | €2,800 |

These examples illustrate article 1447-0B only. They do not include patente or additional chamber levies. The official handbook's wording suggests an overall €2,500 cap, but the code explicitly caps the **area component**; the ordinary fixed component remains separate. Obtain reconciliation if an administrative assessment applies a different total. [CGI article 1447-0B](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

The normal reference is the preceding year or the last twelve-month accounting period closed in that year. Creation/operator-change rules modify it. Do not assume current floor area is automatically the correct reference-period area. [CGI articles 1447-0D and 1447-0H](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

### Creation, cessation and operator changes

For establishment creation, article 1447-0H(II) removes the area component and patente in the creation year; the fixed licence is **€0 conditional on the mandatory declaration**. This is not permission to omit filing. The following year's bases use first-year closing premises/assets and annualized receipts as specified there. [CGI article 1447-0H, page 423](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

An operator change effective **1 January** has an express exception: the new operator owes the €300 fixed component plus area and patente based on the predecessor's activity. Do not treat every takeover as a tax-free creation. For genuine cessation, the area component and patente have remaining-month relief subject to the article's restrictions; transfer or disposal of the activity is excluded from that relief. The fixed component remains annual for activity during any part of the year. [Same article](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

Article 1447-0J bis describes new-enterprise patente abatements of 100% in the following year and 50% in the second following year, with declaration and state-aid conditions. Its reference to Regulation 1407/2013 requires current aid-law reconciliation before claiming relief; this Guide does not treat the abatement as automatically available in 2026. Establishment creation and qualifying new-enterprise relief must be tested separately. [CGI article 1447-0J bis, page 425](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

## Deadlines and filing

Article 1447-0K(I) requires the annual declaration **before 1 July**. Filing accompanies the full licence amount, half the patente contribution, the licence additional levy and half the patente additional levy. The patente and related additional-levy balance is due **30 November**. Rates and relief for these other amounts require a separate calculation. Retain the receipt and display the prescribed annual licence/patente notice as the article requires. [CGI article 1447-0K, page 425](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

For a start during the year, paragraph II says before 1 July if activity starts before 1 June, and within one month if it starts after 1 June. The quoted wording does not expressly allocate a start **on 1 June** to either limb; confirm the treatment with the authority rather than inventing a boundary rule. [Same article](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

Use the official current digital filing procedure linked in the [TGCA Guide](mf-tgca-scope-and-compliance.md), with the appropriate DLCP form and tax reference. Maintain evidence of dates, activity, area, relief conditions and amounts paid.

From 1 January 2026 the DLCP declaration goes by email as a PDF to cfip.sxm.declarations-professionnels@dgfip.finances.gouv.fr, with payment by bank transfer and the proof attached ([impots-saint-martin.fr](https://www.impots-saint-martin.fr/)).

## Penalties and interest

If the declaration is not filed or is late, the licence and patente are assessed ex officio under art. 66 of the Livre des procedures fiscales, with the penalties of art. 1728; failing to display the annual notice brings the art. 1729 C sanction ([CGI Saint-Martin, art. 1447-0K](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf)). The penalty rates were not checked for this skill.

## Cross-border points

- Applies to activity carried on in French Saint-Martin; Dutch Sint Maarten has no equivalent in this skill.
- A business with premises on both sides of the island: refer.

## Two worked examples that recompute

The area table above illustrates article 1447-0B only; it excludes patente and chamber levies.

**Case 1: shop with 100.6 square metres.** Area rounded down to 100; 60 square metres over 40 at 5 euros = 300; licence 300 + 300 = 600 euros.

```oa-check
name: Saint-Martin licence, 100.6 square metres
inputs:
  area: 100.6
steps:
  - billable_m2: max(floor(area) - 40, 0)
  - area_fee: min(billable_m2 * 5, 2500)
  - licence: 300 + area_fee
expected:
  billable_m2: 60
  area_fee: 300.00
  licence: 600.00
```

**Case 2: warehouse with 600 square metres, and a market trader.** Area fee 560 x 5 = 2,800, capped at 2,500; licence 300 + 2,500 = 2,800 (the cap is on the area fee, not the total). A market-stall trader with no premises pays the 150 euro fixed fee only.

```oa-check
name: Saint-Martin licence, area cap and market trader
inputs:
  area: 600
steps:
  - area_fee_uncapped: max(floor(area) - 40, 0) * 5
  - area_fee: min(area_fee_uncapped, 2500)
  - licence: 300 + area_fee
  - market_trader: 150
expected:
  area_fee_uncapped: 2800.00
  area_fee: 2500.00
  licence: 2800.00
  market_trader: 150
```

## Ask the client first

1. What activity, and is it habitual and non-salaried? Any article 1447-0A exemption?
2. Who operates it, and when did it start (creation year, takeover on 1 January)?
3. Premises used in the reference period and their net floor area.
4. Itinerant or market trading only?
5. Any new-enterprise abatement claim and its state-aid conditions?

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI de la collectivite de Saint-Martin, consolidated to 5 June 2026: read for arts. 1447-0, 1447-0A, 1447-0B, 1447-0D, 1447-0H, 1447-0J bis and 1447-0K | https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf | 2026-11-14 |
| impots-saint-martin.fr home page notices: read for the January 2026 email-only DLCP filing and bank-transfer payment | https://www.impots-saint-martin.fr/ | 2026-11-14 |

Not yet confirmed: patente rates and bases, minimum charges, chamber additional-levy rates; whether a start on exactly 1 June falls under "before 1 July" or "within one month"; the state-aid conditions for the art. 1447-0J bis abatement in 2026; penalty rates; the business handbook's wording, which suggests a 2,500 euro cap on the total rather than on the area fee (the code caps the area fee).
