---
name: shipping-aviation-tonnage-tax
description: "Use this skill whenever a shipping company, vessel operator, ship owner, ship manager, or aviation lessor / airline asks about sector-specific tax regimes. Trigger on phrases like \"tonnage tax\", \"Greek tonnage tax\", \"Cyprus tonnage tax\", \"Malta tonnage tax\", \"UK tonnage tax\", \"Norwegian shipping regime\", \"Dutch tonnage tax\", \"Singapore MSI\", \"Hong Kong tonnage tax\", \"qualifying shipping income\", \"qualifying ancillary income\", \"strategic / commercial management test\", \"EU State Aid Guidelines on State Aid to Maritime Transport\", \"flag state requirement\", \"EU/EEA flag minimum\", \"aviation lessor tax\", \"Section 110 SPV Ireland\", \"Cape Town Convention\", \"Aircraft Lease Securitisation\", or any question on shipping or aviation tax/accounting. Maps tonnage tax regimes in 18+ jurisdictions plus aviation lessor regimes (Ireland Section 110, Singapore Aircraft Leasing Scheme). Does NOT cover: vessel registration, ship financing structures, IMO regulatory compliance, or aviation safety regulation."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Shipping Aviation Tonnage Tax

## What this file is

A sector overlay for shipping companies and aviation lessors / airlines.

## Section 1 — Tonnage tax regimes

- **[T1] Tonnage tax** — Tonnage tax is a presumptive tax based on a vessel's net tonnage, replacing regular corporate income tax on qualifying shipping activities. EU regimes operate under the Community Guidelines on State Aid to Maritime Transport (2004, updated 2024).  _(Community Guidelines on State Aid to Maritime Transport (2004, updated 2024))_

### Key EU regimes

**Key EU regimes**  _(FA 2000 Sch 22; Wet inkomstenbelasting 2001 ch. 3; German tonnage tax §5a EStG; CGI Art. 209-0 B; Articolo 156 TUIR; TCA 1997 Part 24; Decreto-Lei 92/2018)_

| Country | Effective rate | Min flag requirement | Notable |
| --- | --- | --- | --- |
| **Greece** | Article 75 Constitution-protected; rates set per vessel type | Greek flag (extensive Greek-flagged fleet) | World's largest tonnage tax regime; 80% of Greek-owned vessels under Greek flag |
| **Cyprus** | EUR rates per 100 net tonnes per day, banded by size | EU/EEA strategic management in Cyprus | Available for ship owners, ship managers, charterers |
| **Malta** | EUR rates per 100 net tonnes; banded | EU/EEA flag; commercial management in Malta | Includes ship management; recent state aid extension |
| **United Kingdom** | Daily profit per 100 net tonnes (bands 0.6, 0.45, 0.30 GBP) | UK / EU / EEA flag minimum 60% of qualifying group | FA 2000 Sch 22; reformed 2024 to permit non-UK flag in some cases |
| **Netherlands** | Daily profit per 1,000 net tonnes (banded) | EU/EEA flag; commercial management in NL | Wet inkomstenbelasting 2001 ch. 3 |
| **Belgium** | EUR per 100 net tonnes per day | EU/EEA flag | Belgian tonnage tax regime |
| **Denmark** | DKK per 100 net tonnes per day | EU/EEA flag | DIS (Danish International Shipping Register) |
| **Norway** | NOK per 100 net tonnes per day | NIS register | Norwegian Shipping Regime (NSR); requires distribution to shareholders to retain qualifying status |
| **Sweden** | SEK per 100 net tonnes per day | EU/EEA flag | Pre-EU State Aid approved |
| **Germany** | EUR per 100 net tonnes per day (banded) | EU/EEA flag | German tonnage tax §5a EStG |
| **France** | EUR per 100 net tonnes per day | EU/EEA flag | Tonnage tax regime CGI Art. 209-0 B |
| **Italy** | EUR per ton banded; tonnage tax option | EU/EEA flag | Articolo 156 TUIR |
| **Spain** | EUR per ton banded | EU/EEA flag; substantial Spanish presence | Régimen español de tributación por tonelaje |
| **Ireland** | EUR per 100 net tonnes per day | EU/EEA flag; commercial management in Ireland | TCA 1997 Part 24 |
| **Portugal** | EUR per ton banded | EU/EEA flag | Decreto-Lei 92/2018 |

### Asia-Pacific tonnage regimes

**Asia-Pacific tonnage regimes**

| Country | Status |
| --- | --- |
| **Singapore — MSI (Maritime Sector Incentive)** | Various awards: MSI-AIS (vessel owners), MSI-SSS (international shipping), MSI-ML (ship management) — tax exemption or concessionary rate |
| **Hong Kong** | Tonnage tax discussed; no formal regime as of 2025 — half-rate profits tax for shipping activities |
| **South Korea** | Tonnage tax option |
| **India** | Tonnage tax option since 2004 (Income Tax Act Chapter XII-G) |
| **Japan** | Tonnage tax option since 2008 — limited adoption |

### US — special exemptions

- **[T1] §883 IRC exemption** — Foreign corporations operating ships / aircraft in international transport may be exempt from US corporate income tax on shipping/aviation income if home country provides reciprocal exemption (treaty or equivalent regime).  _(§883 IRC)_

## Section 2 — Eligibility tests

- **[T1] Standard tests across regimes** — 1. Vessel type — typically excludes fishing vessels, dredgers (some included), ferries below threshold, leisure 2. Strategic and commercial management — must be carried out in the regime jurisdiction (EU State Aid guidelines) 3. Flag minimum — vessels under EU/EEA flag must constitute a minimum % of the qualifying fleet (typically 60% for fleet extensions; relief if increasing tonnage) 4. Activity scope — international transport (some regimes include cabotage) 5. Lock-in — 10-year minimum tenure in tonnage tax regime; exit penalty for early withdrawal  _(EU State Aid guidelines)_

## Section 3 — Aviation lessor regimes

### 3.1 Ireland — global aircraft leasing hub

- **[T1] Ireland aircraft leasing hub rules** — - Standard 12.5% trading rate applicable to leasing activity if commercial substance - Section 110 SPV (TCA 1997 s.110): securitisation vehicle for aircraft lease finance; effectively neutral CIT but profit-extraction via interest - 8% accelerated depreciation on aircraft (TCA s.284) until disposal - Lessor activity is a trade for CIT and treaty purposes - Pillar Two QDMTT in force from 2024 — affects in-scope groups  _(TCA 1997 s.110; TCA s.284)_

### 3.2 Singapore — Aircraft Leasing Scheme

- **[T1] Singapore Aircraft Leasing Scheme** — - ALS reduced rate (~8%) on qualifying aircraft leasing income; ALSI for aircraft investment manager - Maritime Sector Incentive equivalent in scope and benefit

### 3.3 Hong Kong — Aircraft Leasing Incentive

- **[T1] Hong Kong Aircraft Leasing Incentive** — - 8.25% concessionary rate on qualifying aircraft leasing - 50% gross income basis for asset depreciation

### 3.4 Bermuda

- **[T1] Bermuda aircraft rules** — - Aircraft Securitisation; flagging of aircraft via Cape Town Convention - New 15% CIT from 2025 for in-scope MNE groups

## Section 4 — Cape Town Convention

- **[T1] Cape Town Convention** — The Convention on International Interests in Mobile Equipment (Cape Town, 2001) + Aircraft Protocol provides a unified framework for security interests in aircraft. Most major aviation finance jurisdictions are signatories. Affects creditor priority in lessee insolvency, not tax directly, but interacts with sale-leaseback structures.  _(Convention on International Interests in Mobile Equipment (Cape Town, 2001) + Aircraft Protocol)_

## Section 5 — IFRS 16 Lessor (aircraft and ships)

- **[T1] IFRS 16 / US GAAP lessor accounting** — Lessor accounting under IFRS 16 substantially preserved IAS 17 — finance lease vs operating lease distinction at lessor. Most aircraft / vessel leases are operating leases for lessor, with rental income recognised straight-line. US GAAP ASC 842: substantially same lessor model.  _(IFRS 16; US GAAP ASC 842)_

## Section 6 — Self-checks

- [ ] Tonnage tax regime entry conditions met (vessel type, strategic management, flag minimum)
- [ ] Qualifying vs non-qualifying activities separated (only qualifying gets tonnage; rest at regular CIT)
- [ ] 10-year regime tenure tracked
- [ ] EU State Aid Guidelines compliance (where applicable)
- [ ] Ship management vs ship owner status distinct (each may have own regime)
- [ ] Aircraft lessor activity meets commercial substance for treaty access
- [ ] Section 110 SPV substance documented (Irish lessors)
- [ ] Pillar Two ETR analysis — tonnage tax presumptive amounts produce ETRs well below 15%; top-up tax exposure
- [ ] Cape Town Convention security interest considered for finance lease structuring
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 7 — Disclaimer

Maritime and aviation sector taxation is highly specialised. Outputs must be reviewed by credentialed shipping/aviation tax practitioners. The most up-to-date version is at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
