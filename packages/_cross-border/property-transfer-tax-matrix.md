---
name: property-transfer-tax-matrix
description: "Use this skill whenever a property transaction triggers a tax on the transfer of real estate. Trigger on phrases like \"SDLT\", \"stamp duty land tax\", \"ADS additional dwelling supplement\", \"LBTT\", \"LTT\", \"Grunderwerbsteuer\", \"GrESt\", \"DMTO droits de mutation\", \"imposta di registro\", \"ITP impuesto transmisiones patrimoniales\", \"AJD actos jurídicos documentados\", \"IVA on new build\", \"IMT Portugal\", \"transfer duty South Africa\", \"land transfer tax Ontario\", \"Welcome tax Quebec\", \"ABSD additional buyer's stamp duty\", \"BSD buyer's stamp duty\", \"Hong Kong AVD\", \"stamp duty NSW\", \"VIC\", \"QLD\", \"WA\", \"foreign buyer surcharge\", \"vacancy tax\", \"RETT\", or any request to compute property purchase or transfer tax. Maps every major property transfer tax regime including special foreign-buyer surcharges (Canada, Australia, Singapore, NZ), regional variation in Germany (16 Länder), Spain (17 CCAA), Italy (categories of buyer/property), and the UK's four-rate jurisdictional split (England SDLT, Scotland LBTT, Wales LTT, Northern Ireland SDLT). Does NOT cover: VAT/GST on commercial property (see VAT skills), property income tax, capital gains tax on property disposal, council/property tax (annual), or stamp duty on shares (see stamp-duty-matrix). ALWAYS read this skill before quoting purchase tax on a property transaction."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Property Transfer Tax Matrix

## Property / Real Estate Transfer Tax Matrix v0.1

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It implements every major real estate transfer tax regime globally as of mid-2025.

**Tax year coverage.** Current for **calendar 2025**, reflecting:
- **UK SDLT** post-1 April 2025 reform: residential 0% band reduced to GBP 125,000 (from GBP 250,000); first-time buyer threshold reduced; additional dwelling surcharge 5% (raised from 3% on 31 October 2024); non-resident surcharge 2%
- **Scotland LBTT** thresholds and ADS at 8% (from 5%)
- **Wales LTT** updated 2024-25
- **Germany Grunderwerbsteuer** rates vary by Land (3.5% Bayern/Sachsen → 6.5% NRW/SH/Brandenburg)
- **Spain ITP/AJD** vary by CCAA (6% Madrid → 10%+ Cataluña/Comunidad Valenciana)
- **Italy registration tax** at 2% (primary residence) or 9% (others) flat
- **Singapore ABSD** rates updated April 2023: 20% Singaporean second residential property; 30% PR; 60% foreign individual
- **Canada — provincial foreign buyer rules** + federal Underused Housing Tax (UHT)
- **Australia — state foreign-purchaser surcharges** (NSW 8%, VIC 8%, QLD 8%, WA 7%)
- **Hong Kong AVD** Scale 2 0.10%-4.25% for HK permanent resident first home; BSD 7.5% for non-PR / corporates; SSD up to 20% for disposal within 24 months
- **Portugal IMT** rates and exemptions

**The reviewer is the customer of this output.** Property transfer tax rates have material magnitude and often jurisdiction-specific surcharges. Every output must be reviewed by a credentialed local conveyancing solicitor / notary / tax practitioner before completion.

## Section 1 — Scope statement

This skill covers:

- **Buyer-side transfer tax** on real estate acquisitions (residential and commercial)
- **Foreign buyer surcharges**
- **Vacancy / second-home surcharges**
- **VAT vs transfer tax** election rules (Italy, Spain, France new-build vs second-hand)
- **Reliefs** — first-time buyer, multiple-dwellings relief (MDR repealed UK June 2024), intra-group transfers, mixed-use

This skill does NOT cover:

- **Annual property tax** (Council Tax UK, Taxe foncière FR, IBI ES, IMU IT, Grundsteuer DE)
- **Capital gains tax on disposal**
- **Property income tax**
- **VAT/GST on commercial new-build leases** beyond binary in/out scope
- **Stamp duty on shares** of property-owning companies (see `stamp-duty-matrix.md`)

## Section 2 — UK — SDLT (England/NI), LBTT (Scotland), LTT (Wales)

### 2.1 England and Northern Ireland — SDLT

**[T1] Post-1 April 2025 residential rates (single dwelling, no surcharge)**  _([T1])_

| Band | Rate |
| --- | --- |
| 0 — GBP 125,000 | 0% |
| GBP 125,001 — 250,000 | 2% |
| GBP 250,001 — 925,000 | 5% |
| GBP 925,001 — 1.5m | 10% |
| > GBP 1.5m | 12% |

- **First-time buyer relief (post-1 April 2025)** — 0% to GBP 300,000 (cut from GBP 425,000); 5% on GBP 300,001 — 500,000; No relief if total consideration > GBP 500,000  _([T1])_
- **Additional dwelling surcharge** — +5% (raised from 3% on 31 October 2024; FA 2024 amendments; on each band for additional residential property)  _([T1])_
- **Non-resident surcharge** — +2% (on each band for non-UK residents)  _([T1])_
- **Maximum rate stacking** — 12% + 5% (ADS) + 2% (non-resident) = 19% top marginal rate on properties > GBP 1.5m for non-resident purchasers of additional dwellings  _([T1])_

**[T1] Non-residential / mixed-use rates**  _([T1])_

| Band | Rate |
| --- | --- |
| 0 — GBP 150,000 | 0% |
| GBP 150,001 — 250,000 | 2% |
| > GBP 250,000 | 5% |

- **Reliefs** — Multiple Dwellings Relief (MDR) — repealed for transactions on or after 1 June 2024 (FA(No.2) 2024); Group relief (Schedule 7) for 75%+ common-ownership groups; Charity relief; Acquisition relief (s.62); Sub-sale relief (s.45); Filing: SDLT1 within 14 days of effective date  _([T1])_

### 2.2 Scotland — LBTT

**[T1] Residential rates 2025/26**  _([T1])_

| Band | Rate |
| --- | --- |
| 0 — GBP 145,000 | 0% |
| GBP 145,001 — 250,000 | 2% |
| GBP 250,001 — 325,000 | 5% |
| GBP 325,001 — 750,000 | 10% |
| > GBP 750,000 | 12% |

- **Additional Dwelling Supplement (ADS)** — 8% (raised from 5% in 2024; on additional dwelling acquisitions > GBP 40,000)  _([T1])_
- **First-time buyer relief** — 0% to GBP 175,000  _([T1])_

### 2.3 Wales — LTT

**[T1] Residential rates from 11 December 2024**  _([T1])_

| Band | Rate (main) | Rate (higher rate / additional dwelling) |
| --- | --- | --- |
| 0 — GBP 225,000 | 0% | 5% |
| GBP 225,001 — 400,000 | 6% | 11% |
| GBP 400,001 — 750,000 | 7.5% | 12.5% |
| GBP 750,001 — 1.5m | 10% | 15% |
| > GBP 1.5m | 12% | 17% |

## Section 3 — Germany — Grunderwerbsteuer (GrESt)

**[T1] Rates by Land (set by each federal state; range 3.5% — 6.5%)**  _([T1])_

| Land | Rate |
| --- | --- |
| **Bayern, Sachsen** | 3.5% |
| **Hamburg** | 4.5% (raised from 5.5% as of 1 January 2024 — confirm direction) |
| **Bremen** | 5% |
| **Niedersachsen** | 5% |
| **Sachsen-Anhalt** | 5% |
| **Mecklenburg-Vorpommern** | 6% |
| **Thüringen** | 5% |
| **Rheinland-Pfalz** | 5% |
| **Berlin** | 6% |
| **Hessen** | 6% |
| **Baden-Württemberg** | 5% |
| **Saarland** | 6.5% |
| **Schleswig-Holstein** | 6.5% |
| **Nordrhein-Westfalen** | 6.5% |
| **Brandenburg** | 6.5% |

- **Exemptions (§3 GrEStG)** — Acquisitions ≤ EUR 2,500; Acquisitions by spouse / registered partner / descendants in direct line; Acquisitions on inheritance / division of estate; Restructuring and intra-group reorganisations under §§5-7 (75%+ common ownership; complex)  _([T1]; §3 GrEStG)_
- **Share deals — anti-abuse rule** — Transferring ≥ 90% of shares in a real-estate-owning company / partnership over a 10-year period triggers GrESt at the share-deal level (reduced from 95% in 2021 reform)  _([T1]; §1 Abs. 2a, 2b, 3 GrEStG)_
- **Filing** — Notary submits Verlangen to Finanzamt; tax assessment issued; payment within 1 month  _([T1])_

## Section 4 — Spain — ITP and AJD

### 4.1 ITP (Impuesto de Transmisiones Patrimoniales)

- **Applicability** — Applies to second-hand property purchases. Rates set by each Comunidad Autónoma.  _([T1])_

**[T1] Rate (illustrative) by CCAA**  _([T1])_

| CCAA | Rate (illustrative) |
| --- | --- |
| **Madrid** | 6% (one of lowest) |
| **Andalucía** | 7% |
| **Valencia** | 10% (raised from 6% in 2023) |
| **Cataluña** | 10% (11% above EUR 1m) |
| **Galicia** | 9% |
| **Aragón** | 8% |
| **Asturias** | 8% — 10% by band |
| **Murcia** | 8% |
| **Castilla-La Mancha** | 9% |
| **Extremadura** | 8% — 11% |
| **Baleares** | 8% — 13% |
| **Canarias** | 6.5% — 8% |

### 4.2 AJD (Actos Jurídicos Documentados)

- **AJD applicability and rate** — Applies to new-build (where VAT/IVA also applies) and certain documented transactions. Rate by CCAA: typically 0.5%-1.5% (max 2.5% in some CCAA)  _([T1])_

### 4.3 New-build (with IVA)

- **New-build residential taxes** — New-build residential: 10% IVA + 1.5% AJD typical (Madrid 0.75% AJD; some CCAA 2%)  _([T1])_

## Section 5 — France — DMTO (Droits de Mutation à Titre Onéreux)

- **Combined transfer tax** — Generally 5.81% of purchase price (with minor variation by département): Departmental rate: 4.50% (cap; can be reduced); Communal rate: 1.20%; "Frais d'assiette" 2.37% on departmental rate; Total typically ~5.81%  _([T1])_
- **Reduced rate for first-time purchases** — Not generally available  _([T1])_
- **New-build properties (< 5 years old, first sale)** — VAT (20%) applies; reduced DMTO at 0.715% of purchase price  _([T1])_
- **Reliefs** — Acquisitions by SCI familiale: certain registration relief; Transfers between spouses on divorce; Acquisitions of forests / agricultural land (specific reductions)  _([T1])_
- **Filing** — Notary handles all formalities; tax due at signing of acte authentique  _([T1])_

## Section 6 — Italy — Imposta di registro / IVA on new build

### 6.1 Second-hand residential

- **Primary residence ("prima casa")** — registration tax 2% of cadastral value (not purchase price); ipotecaria EUR 50; catastale EUR 50  _([T1])_
- **Non-primary residence** — registration tax 9% of cadastral value; ipotecaria EUR 50; catastale EUR 50  _([T1])_

### 6.2 New-build residential (with VAT)

- **Primary residence** — VAT 4% of purchase price; registration EUR 200; ipotecaria EUR 200; catastale EUR 200 EUR
- **Non-primary** — VAT 10% (luxury 22%) of purchase price; registration EUR 200; ipotecaria EUR 200; catastale EUR 200 EUR

### 6.3 Commercial

- **Commercial registration/VAT election** — Registration 9% of cadastral value, OR VAT 22% election available if seller is VAT-registered enterprise

### 6.4 Primary residence qualifying conditions

- **Qualifying conditions** — Buyer is not owner of another habitation in the same municipality; Buyer does not already own a "prima casa" anywhere (or sells within 1 year of acquisition); Property is not "of luxury" (categories A/1, A/8, A/9 of cadaster); Buyer is resident or becomes resident within 18 months

## Section 7 — Netherlands — Overdrachtsbelasting

- **First-home buyer (Starters)** — 0% if buyer 18-35 years old, purchase ≤ EUR 525,000, first home, declared to use as own residence  _([T1])_
- **Owner-occupier non-starter** — 2%  _([T1])_
- **All other (investor, second home, commercial)** — 10.4% (raised from 8% in 2023)  _([T1])_
- **Filing** — Notary handles; collected at execution of deed  _([T1])_

## Section 8 — Portugal — IMT (Imposto Municipal sobre as Transmissões Onerosas)

**[T1] Urban property for permanent residence — progressive rates**  _([T1])_

| Value | Marginal Rate |
| --- | --- |
| 0 — EUR 104,261 | 0% |
| EUR 104,261 — EUR 142,618 | 2% |
| EUR 142,618 — EUR 194,458 | 5% |
| EUR 194,458 — EUR 324,058 | 7% |
| EUR 324,058 — EUR 648,022 | 8% |
| EUR 648,022 — EUR 1,128,287 | 10% (Madeira / Açores adjusted) |
| > EUR 1,128,287 | 6% flat (yes — it goes down at the top; quirk of regime) |

- **Second residential / investment** — 1% to 8% progressive plus flat 8% above EUR 1.13m  _([T1])_
- **Commercial / rustic** — 5% / 6.5% / others  _([T1])_
- **Imposto do Selo on real estate transactions** — 0.8%  _([T1])_

## Section 9 — Asia-Pacific

### 9.1 Singapore — BSD + ABSD + SSD

**[T1] Buyer's Stamp Duty (BSD) — applies to all buyers**  _([T1])_

| Value | Residential | Non-residential |
| --- | --- | --- |
| 0 — SGD 180,000 | 1% | 1% |
| 180,001 — 360,000 | 2% | 2% |
| 360,001 — 1,000,000 | 3% | 3% |
| 1,000,001 — 1,500,000 | 4% | 4% |
| 1,500,001 — 3,000,000 | 5% | 5% |
| > 3,000,000 | 6% | 5% |

**[T1] Additional Buyer's Stamp Duty (ABSD) — applies in addition to BSD**  _([T1])_

| Buyer profile | Residential ABSD rate |
| --- | --- |
| Singapore citizen — first home | 0% |
| Singapore citizen — second home | 20% |
| Singapore citizen — third+ home | 30% |
| Permanent resident — first home | 5% |
| Permanent resident — second home | 30% |
| Permanent resident — third+ home | 35% |
| Foreign individual | **60%** |
| Trust acquisition | 65% |
| Entities (corporates, etc.) | 65% |
| Housing developers (after qualifying conditions) | 35% remitted on completion within 5 years |

- **Seller's Stamp Duty (SSD) — disposal within holding period** — ≤ 1 year: 12% on residential / 5% on industrial; ≤ 2 years: 8%; ≤ 3 years: 4%; > 3 years: 0%  _([T1])_

### 9.2 Hong Kong — AVD + BSD + SSD

**[T1] Ad Valorem Stamp Duty (AVD) — Scale 1 abolished October 2023; Scale 2 applies now to all individual buyers**  _([T1])_

| Value | Rate (Scale 2 / Standard) |
| --- | --- |
| ≤ HKD 3m | HKD 100 |
| HKD 3,000,001 — 3,528,240 | sliding |
| HKD 3,528,240 — 4,500,000 | 1.5% |
| HKD 4,500,000 — 6,000,000 | 2.25% |
| HKD 6,000,000 — 9,000,000 | 3.00% |
| HKD 9,000,000 — 20,000,000 | 3.75% |
| > HKD 20,000,000 | 4.25% |

- **BSD (Buyer's Stamp Duty for non-permanent-resident / corporate)** — Abolished October 2023 (was 7.5%)  _([T1])_
- **SSD (Special Stamp Duty) on disposal within 24 months** — Also abolished October 2023  _([T1])_

Hong Kong property transfer tax for non-residents is now identical to residents, at Scale 2 rates.

### 9.3 Australia — state-level transfer duty

**[T1] Each state and territory has its own duty**  _([T1])_

| State | Standard duty | Foreign buyer surcharge |
| --- | --- | --- |
| **NSW** | 1.25% — 7% progressive | 8% (raised from 8% 2023) |
| **Victoria** | 2.4% — 6.5% | 8% |
| **Queensland** | 1.5% — 5.75% | 8% |
| **WA** | 1.9% — 5.15% | 7% |
| **SA** | 1% — 5.5% | 7% |
| **Tasmania** | 1.75% — 4.5% | 8% (additional 8% land tax surcharge) |
| **ACT** | 1.5% — 4.5% (currently being phased out) | 0% |
| **NT** | 1.5% — 5.95% | 0% |

- **Land Tax Surcharge** — Separate annual tax on foreign owners in NSW (4%), VIC (4%), QLD (3%), WA, Tasmania  _([T1])_

### 9.4 New Zealand

- **NZ property tax rules** — No stamp duty on property since 1999. Bright-line test (income tax on disposal within 2 years; 10 years for property acquired between 27/3/2021 and 30/6/2024). Foreign buyer ban under Overseas Investment Act 2018 with limited exemptions.  _([T1])_

### 9.5 Japan

- **Real Estate Acquisition Tax (不動産取得税)** — 3% land / 4% buildings (prefecture-administered). Plus registration tax (登録免許税) 1.5%-2%. Cadastral value × rate.  _([T1])_

## Section 10 — Canada — provincial transfer duty + UHT

### 10.1 Provincial land transfer tax (LTT)

**Rate by province**

| Province | Rate |
| --- | --- |
| **Ontario** | 0.5% — 2.5% progressive; **plus Toronto MLTT** (additional 0.5%-2.5% in Toronto); plus **NRST 25%** for non-residents (raised from 20% in March 2022) |
| **British Columbia** | 1% — 5% progressive; **plus Additional Property Transfer Tax (APTT) 20%** for foreign buyers in specified regions |
| **Quebec — "Welcome Tax"** | 0.5% — 3% progressive; municipally administered |
| **Alberta** | No LTT (registration fees only) |
| **Saskatchewan** | Title transfer fees only |
| **Manitoba** | 0.5% — 2% progressive |
| **Nova Scotia** | 0.5% — 1.5% municipally |
| **PEI, NB, NL** | Various; relatively low |

### 10.2 Federal — Underused Housing Tax (UHT)

- **UHT** — 1% annual tax on the assessed value of underused / vacant residential property in Canada owned by non-resident, non-Canadian persons. Filing required even when exemption applies. Specific exemptions for: trust ownership, corporate Canadian ownership (≥10%), primary place of residence, qualifying occupancy.  _([T1]; Act CRA, 2022)_

### 10.3 BC — Speculation and Vacancy Tax

- **Speculation and Vacancy Tax** — 0.5% (Canadian) / 2% (non-Canadian) annual tax on residential property in specified regions left vacant > 6 months  _([T1])_

### 10.4 Toronto / Vancouver / Montreal — vacant home taxes

- **Municipal vacant home taxes** — Municipal: Toronto 3%, Vancouver 3%, etc.

### 11.1 Multiple dwellings relief (UK) — REPEALED 2024

- **MDR repeal** — MDR was previously available where a transaction involved more than one dwelling, allowing the buyer to compute SDLT on the average price. Abolished for transactions with effective date on or after 1 June 2024 (FA(No.2) 2024). Pre-1 June 2024 transactions may still claim.

### 11.2 Share-deal anti-abuse

- **Share-deal anti-abuse rules by jurisdiction** — Major jurisdictions tax indirect transfer of real estate via share transfer: - **UK** — no equivalent at federal level but "land-rich" SDLT charge exists at restructuring level via group relief abuse rules - **Germany** — §1 Abs. 2a, 2b, 3 GrEStG: 90%+ share transfer over 10 years - **France** — Article 726 CGI: SCI/SCPI partnership-style entities are subject to 5% droits d'enregistrement on share transfer if real-estate-rich - **Spain** — Article 314 LMV anti-abuse: share transfer of real-estate-rich companies treated as direct property transfer for ITP - **Singapore — ACD**: Up to 65% top duty for property-rich entity transfers - **Australia — Landholder duty** in NSW, VIC, QLD, WA on acquisitions of "landholder" entities

### 11.3 Intra-group relief

- **Intra-group relief conditions** — Most jurisdictions allow exemption / reduced rate for intra-group transfers within 75%+ commonly owned groups. Documentary and continuing-ownership requirements (typically 3-7 years post-transfer) apply. Failure to maintain triggers clawback.

### 11.4 First-time buyer reliefs

- **First-time buyer reliefs by jurisdiction** — - **UK** (England/NI): 0% to GBP 300,000 (post-1 April 2025) - **Scotland LBTT**: 0% to GBP 175,000 - **Ireland**: Help-to-Buy income tax rebate up to EUR 30,000 - **Netherlands**: 0% if age 18-35, ≤ EUR 525,000 - **France**: Reduced DMTO in certain départements (rare)

### 11.5 Foreign buyer overlay — fast-changing

- **Foreign buyer surcharge landscape** — Many jurisdictions have introduced foreign buyer surcharges since 2017. The landscape changes annually. Confirm before quoting: - UK: 2% non-resident SDLT - Singapore: 60% ABSD - Hong Kong: abolished October 2023 - Canada: 25% (ON) / 20% (BC) NRST plus federal UHT - Australia: 7-8% state surcharges - New Zealand: outright purchase ban

## Section 12 — Output specification

The reviewer brief must include:

1. **Property classification** — residential / commercial / agricultural / mixed-use
2. **Purchaser profile** — resident / non-resident, first-time buyer, individual / corporate / trust
3. **Existing portfolio** — does the buyer already own additional dwellings?
4. **Rate analysis** per jurisdiction with bracket-by-bracket SDLT/LBTT/LTT/Grunderwerbsteuer/ITP/etc
5. **Foreign buyer surcharge** if applicable
6. **Relief analysis** — first-time buyer, intra-group, charity, MDR (pre-1 June 2024 UK only)
7. **VAT vs transfer tax election** for new-build properties
8. **Anti-abuse for share deals** if relevant
9. **Annual ongoing surcharges** (UK ATED, BC SVT, Toronto vacant home, etc.) — flag for separate scope
10. **Filing schedule and deadlines** per jurisdiction
11. **Reviewer questions** — open items flagged as [T2] or [T3]

## Section 13 — Self-checks

- [ ] UK SDLT post-1 April 2025 thresholds and ADS at 5% applied
- [ ] MDR not claimed for transactions effective 1 June 2024 or later
- [ ] German Land-specific rate applied
- [ ] Spanish CCAA-specific ITP rate applied
- [ ] Italian primary-residence test confirmed against four conditions
- [ ] Singapore ABSD by buyer profile (citizen/PR/foreign) and dwelling sequence applied
- [ ] Hong Kong BSD/SSD treated as abolished from October 2023
- [ ] Australian state surcharge applied for foreign purchasers
- [ ] Canadian NRST / UHT applied for non-resident purchasers
- [ ] Share-deal anti-abuse considered (Germany 90% / France SCI / Spain Article 314 / Singapore ACD / Australia landholder)
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 14 — Prohibitions

- **Do not** quote pre-1-April-2025 SDLT thresholds for England/NI residential — they have changed.
- **Do not** apply pre-31-October-2024 ADS rate of 3% — current rate is 5%.
- **Do not** claim Multiple Dwellings Relief for transactions effective 1 June 2024 or later.
- **Do not** quote Hong Kong's BSD or SSD as in force — both were abolished October 2023.
- **Do not** advise that a German share-deal escapes Grunderwerbsteuer if ≥90% of shares change over 10 years — the §1 Abs. 2a/2b/3 anti-abuse rule applies.
- **Do not** treat trusts and corporates the same as individual buyers for ABSD / land surcharges — special, usually higher rates apply.

## Section 15 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Property transfer tax rules change frequently with budget cycles and have material magnitude in transactions. Every output must be reviewed and signed off by a credentialed local conveyancing solicitor / notary / tax practitioner before completion.

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
