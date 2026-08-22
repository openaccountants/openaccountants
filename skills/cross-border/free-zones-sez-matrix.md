---
name: free-zones-sez-matrix
description: "Use this skill whenever a company asks about establishing or trading through a free zone, special economic zone (SEZ), free trade zone (FTZ), enterprise zone, or financial center. Trigger on phrases like \"SEZ\", \"free zone\", \"FTZ\", \"Mainland vs free zone UAE\", \"DIFC\", \"ADGM\", \"DMCC\", \"JAFZA\", \"QFC\", \"DAFZA\", \"DWC\", \"Saudi SEZ\", \"King Abdullah Economic City\", \"NEOM\", \"Singapore IDIs\", \"Hong Kong tax\", \"Shenzhen Qianhai\", \"Hainan FTP\", \"Shanghai FTZ\", \"Madeira IBC\", \"Madeira Free Zone\", \"Gibraltar\", \"Malta MFSA passporting\", \"Cyprus IBC\", \"Bahamas IBC\", \"BVI BC\", \"Cayman exempted company\", \"Mauritius GBL\", \"Labuan\", \"Jebel Ali\", \"RAK ICC\", \"ADGM RegLab\", or any request to assess the tax and operational rules of an SEZ. Maps ~50 zones across UAE, Saudi Arabia, China, India, Africa, Latin America, the Caribbean, and Europe. Does NOT cover: VAT/customs free-circulation rules within the zone beyond a summary, immigration / employment law, real-estate leasing, sector-specific licensing. ALWAYS read this skill before incorporating in a zone or advising on the tax incentives."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Free Zones Sez Matrix

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It maps the world's principal free zones, special economic zones, and offshore financial centers as of mid-2025.

**Tax year coverage.** Current for **fiscal year 2025**, reflecting:
- **UAE Corporate Tax Law (Federal Decree-Law No. 47 of 2022)** in full force; "Qualifying Free Zone Person" (QFZP) regime under Ministerial Decision 139/2023 and Cabinet Decision 100/2023
- **Saudi Arabia SEZs** (Riyadh ILBZ, NEOM, KAEC, Jazan, Ras Al Khair, Cloud Computing) under RFAGZ Authority 2023
- **Hainan Free Trade Port** corporate tax incentives extending through 31 December 2025
- **OECD BEPS Action 5** and Pillar Two interaction — many free-zone rates are below 15% and trigger top-up tax

**The reviewer is the customer of this output.** Free zone incorporation decisions are nearly impossible to reverse without exit cost. Every output must be reviewed by a credentialed local tax counsel before any incorporation, restructuring, or onshore-vs-zone election.

## Section 1 — Scope statement

This skill covers:

- **Tax rates** (CIT, withholding, indirect)
- **Qualifying activities** for the preferential regime
- **Substance requirements** (employees, premises, expenditure)
- **De minimis non-qualifying activity** thresholds
- **Onshore-mainland trading restrictions**
- **OECD BEPS Action 5 status**
- **Pillar Two interaction**

This skill does NOT cover:

- **Customs duty rates** within the zone beyond a summary
- **Employment / immigration law**
- **Real-estate leasing economics**
- **Sector-specific regulatory licensing** (DFSA, ADGM FSRA, MAS, etc.)
- **VAT mechanics** within designated zones — see country VAT skills

## Section 2 — UAE Free Zones

The UAE has ~45 free zones plus three financial center zones (DIFC, ADGM, QFC). Since the Federal Corporate Tax Law took effect for periods starting 1 June 2023 (most companies: FY 2024), all UAE entities (including free zone) are subject to CIT — but Qualifying Free Zone Persons (QFZPs) can benefit from a **0% rate on Qualifying Income**.

### 2.1 Qualifying Free Zone Person (QFZP) regime

- **QFZP qualification criteria [T1]** — 1. Maintain adequate substance in the UAE (Article 7 of the Corporate Tax Law) 2. Derive Qualifying Income (Ministerial Decision 139/2023) 3. Not have elected to be subject to the standard 9% rate 4. Comply with the arm's length principle and transfer pricing rules 5. Maintain audited financial statements 6. Meet the de minimis requirement (non-qualifying revenue ≤ AED 5m or 5% of total revenue, lower)  _(Cabinet Decision 100/2023 Article 4)_

**Qualifying Income (Ministerial Decision 139/2023 / 265/2023 / 55/2023 amended)**  _(Ministerial Decision 139/2023 / 265/2023 / 55/2023 amended)_

| Income type | Status |
| --- | --- |
| Transactions with other Free Zone Persons (except excluded activities) | Qualifying |
| Qualifying activities with non-Free Zone persons | Qualifying (subject to list — manufacturing, processing, holding shares/securities, ship management, fund management, wealth management, headquarters services, treasury and financing to related parties, distribution from a Designated Zone, certain logistics, certain processing) |
| Excluded activities (treated as non-qualifying even if otherwise within list) | Banking, insurance, finance & leasing (with non-related parties), ownership/exploitation of immovable property other than commercial property within a Free Zone, intellectual property (with exceptions for qualifying patents per Article 8 MD 139/2023) |
| Other income | Non-qualifying |

- **Substance test (Article 7) [T1]** — - Premises in the UAE adequate to the level of activity - Adequate qualified employees - Adequate operating expenditure - The Core Income Generating Activities (CIGA) must be conducted in the UAE  _(Article 7)_

### 2.2 UAE Free Zone matrix

**UAE Free Zone matrix**

| Free Zone | Jurisdiction | Sector focus | CIT for QFZP | Notable |
| --- | --- | --- | --- | --- |
| **DIFC** | Dubai (independent financial regulator DFSA) | Financial services, asset management, family offices | 0% on Qualifying Income (else 9%) | English common law jurisdiction; ICC arbitration center |
| **ADGM** | Abu Dhabi (FSRA, common law) | Financial services, fintech, virtual assets | 0% on Qualifying Income (else 9%) | Common law direct application; Crypto regulator; Variable Capital Company structure |
| **DMCC** | Dubai (Jumeirah Lakes Towers) | Commodities trading, services | 0% / 9% | World's most-awarded FZ; gold/diamond/crypto licensing |
| **JAFZA** | Dubai (Jebel Ali Port) | Logistics, manufacturing | 0% / 9% | Designated Zone for VAT purposes |
| **DAFZA** | Dubai Airport | Light manufacturing, services | 0% / 9% | n/a |
| **DWC** | Dubai South (Al Maktoum Airport) | Aviation, logistics | 0% / 9% | Aerospace sector cluster |
| **Sharjah Media City (Shams)** | Sharjah | Media, creative | 0% / 9% | Low-cost license |
| **SHAMS / SAIF Zone / SAIF / Hamriyah** | Sharjah | Industrial, logistics | 0% / 9% | n/a |
| **RAKEZ** | Ras Al Khaimah | Industrial, services | 0% / 9% | Low-cost mainland-of-RAK regime |
| **RAK ICC** | Ras Al Khaimah | International Business Companies (offshore-style) | Not a typical FZ; international company regime; 0% CIT but separate from QFZP rules | Offshore holding vehicle |
| **Fujairah Free Zone** | Fujairah | Manufacturing, logistics | 0% / 9% | Indian Ocean oil terminal proximity |
| **Ajman FZ** | Ajman | Light manufacturing | 0% / 9% | n/a |
| **Umm Al Quwain FTZ** | UAQ | Light manufacturing | 0% / 9% | n/a |

- **Onshore-mainland trading [T2]** — A QFZP may sell to mainland UAE customers only through a mainland distributor OR via the QFZP de minimis (≤ AED 5m / 5%). Direct sales to mainland customers above de minimis convert the relevant revenue to standard 9%.

### 2.3 QFC (Qatar Financial Center)

**QFC (Qatar Financial Center)**

| Item | Detail |
| --- | --- |
| CIT | 10% on locally generated profits (not zero) |
| Common law jurisdiction | Yes |
| Sector focus | Financial services, asset management |
| Substance | Yes |

## Section 3 — Saudi Arabia SEZs

**[T1] Saudi Arabia's Royal Commission for AlUla / SEZ Authority** created four "general" SEZs in April 2023 (King Abdullah Economic City, Jazan, Ras Al Khair, Cloud Computing) plus NEOM and the Riyadh Integrated Logistics Bonded Zone (ILBZ).

**Saudi Arabia SEZs**

| SEZ | Sector focus | CIT | Withholding | Customs |
| --- | --- | --- | --- | --- |
| **King Abdullah Economic City (KAEC) SEZ** | Manufacturing, ICT, logistics | **5%** CIT for 20 years | 0% on dividends, interest, royalties to non-residents (under conditions) | 0% customs on goods kept within zone |
| **Jazan SEZ** | Manufacturing, food, mining | **5%** CIT for 20 years | 0% withholding (conditions) | 0% customs within zone |
| **Ras Al Khair SEZ** | Maritime, shipbuilding, MRO | **5%** CIT for 20 years | 0% withholding (conditions) | 0% customs within zone |
| **Cloud Computing SEZ** | Cloud, data centers | **5%** CIT for 20 years | 0% withholding (conditions) | n/a |
| **NEOM** | Energy, tourism, urban tech, oxygen-based | Special bespoke regime — case-by-case | n/a yet | n/a |
| **Riyadh ILBZ** | Logistics, bonded re-export | 0% CIT for 50 years | 0% withholding (conditions) | 0% customs |

- **Saudi Pillar Two overlay [T1]** — Saudi has not yet adopted Pillar Two. For in-scope MNE groups, the low SEZ rate produces top-up tax exposure under IIR / UTPR in parent jurisdictions.

## Section 4 — China and Hong Kong

**China and Hong Kong**

| Zone | Detail |
| --- | --- |
| **Hainan Free Trade Port** | Encouraged industries: 15% CIT (vs 25% standard) through 31 December 2025; individual income tax cap at 15% for qualifying talent. The 15% rate may be extended — confirm 2025 budget. |
| **Shanghai Lin-gang FTZ** | Encouraged industries (integrated circuits, AI, biomedicine, civil aviation): 15% CIT for 5 years (case-by-case) |
| **Shenzhen Qianhai** | Modern services, FinTech: 15% CIT for qualifying industries through 31 Dec 2025 |
| **Hengqin (Guangdong-Macao)** | 15% CIT for encouraged industries |
| **General FTZs (Shanghai, Tianjin, Fujian, Guangdong)** | Standard 25% CIT but customs/foreign exchange relaxations |
| **Hong Kong** | Two-tier profits tax: 8.25% on first HKD 2m, 16.5% above. Territorial-source system. Offshore claim possible; FSIE regime since 2023 for passive income. Not a "zone" in the SEZ sense — Hong Kong is a separate jurisdiction. |

## Section 5 — India SEZs

**[T1] SEZ Act 2005** with phased reforms. **DESH Bill** (Development of Enterprise and Service Hubs) proposed in 2022–2023 to replace SEZs has not been enacted as of mid-2025.

**India SEZs**

| Item | Detail |
| --- | --- |
| Sunset clause | SEZ tax benefits (Section 10AA) progressively phased out for new units commencing operations after 30 June 2020 (100% deduction for 5 years, then 50% for 5 years, then 50% conditional). Most new SEZ units now have minimal CIT benefit. |
| GST | Supplies to SEZ units are zero-rated; SEZ unit pays customs duty on imports as "imports into India" upon clearance into DTA |
| GIFT City IFSC | Separate regime under IFSCA Act 2019; 10-year CIT holiday available for 10 of 15 years for qualifying units |

## Section 6 — Latin America and Caribbean

**Latin America and Caribbean**

| Zone | Detail |
| --- | --- |
| **Panama Colón Free Trade Zone** | 0% on re-export profits (territorial system); customs duty exemption on goods re-exported |
| **Panama City of Knowledge** | Tax incentives for IT, training, R&D |
| **Costa Rica Zonas Francas** | 0% CIT for 8-12 years for qualifying activities (manufacturing, services); 50% for next 4-6 years |
| **Dominican Republic Zonas Francas** | 100% exemption from CIT, withholding, customs duties for export-oriented activities; 100% during specified periods |
| **Honduras ZEDE** | Special zones with bespoke tax regimes (status politically contested) |
| **Uruguay Zonas Francas** | 100% CIT exemption for qualifying activities |
| **Cayman Islands** | No corporate income tax; no withholding; no capital gains. Exempted Company structure. Pillar Two: Cayman implementing QDMTT from 2025. |
| **BVI** | 0% CIT; no withholding. Business Companies Act. Economic substance per ESA 2018. Pillar Two: BVI implementing TBI tax responses. |
| **Bahamas** | No CIT; introduced 15% Domestic Top-up Tax effective 2024 for in-scope MNEs. |
| **Bermuda** | 0% CIT through 2024; introduced 15% Corporate Income Tax effective 1 January 2025 (Pillar Two-aligned) |
| **Barbados** | 9% standard CIT (since reform 2024); special economic substance and IP regime |

## Section 7 — Europe and Mediterranean

**Europe and Mediterranean**

| Zone | Detail |
| --- | --- |
| **Madeira International Business Centre (Madeira Free Zone)** | 5% CIT through 31 December 2027 (EU State Aid extension); employment minimums; capped by annual taxable income ceilings |
| **Azores (Azores Tax Benefits)** | Reduced national CIT; not a classic IBC |
| **Cyprus** (not a free zone but offshore-style) | Standard 12.5% CIT; IP box at 80% deduction (see ip-patent-box-matrix); shipping tonnage tax |
| **Gibraltar** | 12.5% CIT (rising to 15% from 2025 for in-scope MNEs under Pillar Two); territorial-source system |
| **Malta** | Standard 35% CIT but 6/7 refund mechanism reduces effective rate to 5% for non-Malta shareholders. Pillar Two: 15% top-up subject to QDMTT for in-scope groups. |
| **Luxembourg** | Standard 17% CIT + ~7% municipal. SOPARFI holding regime. IP box at 80%. Pillar Two: QDMTT in force. |
| **Ireland (IFSC legacy / Section 110)** | Standard 12.5% CIT; Section 110 securitisation SPVs; KDB IP regime. Pillar Two: Ireland in-force from 2024. |
| **Isle of Man** | 0% CIT (standard) with 10% for banking and large retailers, 20% for property rental income. Pillar Two: 15% DMTT proposed for 2025. |
| **Jersey / Guernsey** | 0% CIT (standard); 10% for financial services; 20% for utilities. Pillar Two: 15% IIR / QDMTT proposed for 2025. |
| **Monaco** | 33.33% CIT but only on activities outside Monaco or > 25% non-Monaco turnover; residents (individuals) generally exempt from personal income tax |
| **Andorra** | 10% CIT |
| **San Marino** | 17% CIT; reduced rates for new enterprises |

## Section 8 — Africa

**Africa**

| Zone | Detail |
| --- | --- |
| **Mauritius Global Business Licence (GBL)** | 15% CIT but with partial exemption (effective 3% on qualifying activities); GBL2 abolished post-2018; substance requirements |
| **Mauritius Freeport** | 0% CIT for qualifying freeport activities (manufacturing, warehousing, distribution to non-Africa-mainland exports); customs duty exempt |
| **Labuan IBC (Malaysia)** | Trading companies: 3% of audited net profits OR MYR 20,000 flat (election); non-trading: 0% |
| **Tanger Free Zone (Morocco)** | 0% CIT for 5 years for export-oriented qualifying activities; 8.75% thereafter |
| **Egypt SEZs (Suez Canal Economic Zone, NUCA)** | Reduced CIT rates; customs and VAT incentives |
| **Nigeria FTZs (Lagos, Calabar, Lekki)** | 100% CIT exemption for activities within the FTZ; customs exemption |
| **Kenya EPZs / SEZs** | 10-year CIT holiday + reduced rates thereafter; customs duty waiver |
| **South Africa SEZs** | 15% CIT (vs 27% standard) for qualifying companies; section 12R Income Tax Act |
| **Botswana IFSC** | 15% CIT (vs 22% standard) for IFSC-certified companies in financial services |

## Section 9 — Mechanics — substance test (universal pattern)

**Substance test — universal pattern [T1]**

| Element | Typical requirement |
| --- | --- |
| Premises | Adequate to activity (rented lab/office in zone) |
| Employees | Adequate count + qualifications; CIGAs performed by employees in zone |
| Operating expenditure | Adequate in-zone OPEX; can include outsourced services subject to control |
| Decision-making | Strategic decisions taken in zone (board meetings, key personnel resident) |
| Records | Maintained in zone, available to regulator |

- **Economic Substance Regulations (ESA) [T1]** — Economic Substance Regulations (ESA) applied in BVI, Cayman, Bermuda, Bahamas, Jersey, Guernsey, Isle of Man, Anguilla, TCI, Mauritius — for "relevant activities" (banking, distribution, headquarters, finance/leasing, fund management, holding, IP, insurance, shipping). Failure to satisfy: penalties, public-register exposure, mandatory exchange to tax authorities of beneficial owner's country.

## Section 10 — Pillar Two interaction

- **Pillar Two Top-up Tax trigger [T1]** — Free zone regimes producing ETRs below 15% trigger Pillar Two Top-up Tax for MNE groups with consolidated revenue ≥ EUR 750m (see `pillar-two-globe-minimum-tax.md`).

**Pillar Two interaction by zone family**

| Zone family | Pillar Two response |
| --- | --- |
| **UAE** | UAE introduced Domestic Minimum Top-up Tax (DMTT) effective 1 January 2025 (Cabinet Decision 142/2024). QFZPs continue at 0% but DMTT applies to bring jurisdictional ETR to 15% for in-scope groups. |
| **Bermuda** | New 15% Corporate Income Tax from 2025 (Pillar Two-aligned). |
| **Bahamas** | 15% DMTT from 2024. |
| **Cayman** | Cayman QDMTT effective 2025. |
| **Saudi Arabia SEZs** | Not yet Pillar Two-implemented; top-up exposure remains at parent IIR / UTPR level. |
| **Hong Kong** | Hong Kong DMTT effective 2025 for in-scope MNEs; tax on Mainland-China-sourced income may also enter scope. |
| **Singapore** | DTT (QDMTT) and IIR from 2025; UTPR not yet enacted. |
| **Madeira IBC** | Portugal QDMTT under EU Directive; benefits clawed back for in-scope groups. |
| **Mauritius** | Pillar Two QDMTT considered but not yet enacted; top-up at parent level. |

## Section 11 — Output specification

The reviewer brief must include:

1. **Zone selection rationale** — why this zone vs alternatives; commercial fit.
2. **Qualifying activity confirmation** — every revenue stream classified within the zone's qualifying list.
3. **Substance plan** — premises, employees, OPEX, decision-making with named individuals and minimum headcount.
4. **De minimis tracking** — non-qualifying revenue forecast and headroom under cap.
5. **Onshore-mainland trading plan** — distributor structure (UAE) or DTA mechanics (India).
6. **Withholding tax position** on inbound and outbound flows; treaty access analysis.
7. **Pillar Two analysis** — group revenue test; if in-scope, model the top-up tax under DMTT and at parent level.
8. **Economic Substance Regulations compliance** (where applicable).
9. **Reviewer questions** — open items flagged as [T2] or [T3].

## Section 12 — Self-checks

- [ ] Zone regime tested for OECD FHTP harmful-tax-practice status (not removed from approved list).
- [ ] Qualifying activity confirmed against the zone's published qualifying list, not assumed by analogy.
- [ ] De minimis cap applied (UAE QFZP 5%/AED 5m, others as specified).
- [ ] Substance plan documents adequate premises, headcount, OPEX.
- [ ] Pillar Two scope test (EUR 750m) applied; DMTT and top-up modelled.
- [ ] Onshore-mainland sale routing documented; arm's length pricing confirmed.
- [ ] Treaty access (LOB, beneficial ownership, principal purpose test) tested for major withholding flows.
- [ ] Economic Substance Regulations compliance documented for ESA-relevant zones.
- [ ] Audited financials and TP documentation obligations noted.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 13 — Prohibitions

- **Do not** advise on incorporating in a zone whose regime has been removed from the OECD FHTP approved list without confirming current status.
- **Do not** treat a non-qualifying activity as qualifying because related activities are listed — the regime is enumeration-based.
- **Do not** assume the de minimis cap allows mainland sales — the cap is on revenue, not transactions.
- **Do not** ignore Pillar Two top-up tax for groups above the EUR 750m threshold — the zone benefit may be clawed back in full.
- **Do not** advise on holding IP in a free zone without checking the country's IP-box overlay rules and BEPS Action 5 nexus requirements.
- **Do not** promise treaty access without testing the relevant LOB / PPT clauses.

## Section 14 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Zone regimes evolve with national budgets and OECD peer review. Pillar Two implementation has materially altered the benefit calculus for in-scope groups. Every output must be reviewed and signed off by a credentialed local tax counsel before any incorporation, restructuring, or election decision.

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
