---
name: saf-t-realtime-ereporting-matrix
description: "Use this skill whenever a tax preparer, ERP implementer, or e-invoicing project asks about country mandates for SAF-T (Standard Audit File for Tax), real-time invoice reporting, or e-receipt clearance. Trigger on phrases like \"SAF-T\", \"Standard Audit File\", \"SAF-T Poland\", \"SAF-T Portugal\", \"SAF-T Romania\", \"JPK\", \"SAF-T Norway\", \"real-time invoice reporting\", \"SII Spain\", \"RTIR Hungary\", \"KSeF Poland\", \"SDI Italy\", \"NF-e Brazil\", \"CFDI Mexico\", \"e-Fatura Turkey\", \"e-fapiao\", \"Peppol BIS\", \"ViDA\", \"DRR digital reporting requirements\", \"EN 16931\", \"structured invoice\", \"XRechnung\", \"Factur-X\", or any request to determine whether a country mandates SAF-T submission or real-time / near-real-time invoice transmission. Maps the mandate scope, file format, transmission method, threshold triggers, deadline, and penalty for 40+ countries. Does NOT cover: country-specific VAT rate determination (see country VAT skills); e-archiving requirements beyond minimums; structured invoice content beyond format references; software-vendor accreditation procedures. ALWAYS read this skill before scoping an e-invoicing or SAF-T implementation."
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

# Saf T Realtime Ereporting Matrix

## SAF-T and Real-Time E-Reporting Matrix v0.1

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It maps the global landscape of digital invoice and ledger reporting mandates as of mid-2025.

**Tax year coverage.** Current for **calendar 2025**, reflecting:
- The EU's **VAT in the Digital Age (ViDA)** package as politically agreed and published in Council Directive (EU) 2025/516 (with key Digital Reporting Requirements taking effect 1 July 2030 — earlier optional date 1 January 2027 for member states that wish to mandate)
- **Germany e-invoicing** mandatory receipt phase from 1 January 2025 (B2B receipt) and outbound phase from 1 January 2027 / 2028 (size-based)
- **France e-invoicing reform** rescheduled to begin September 2026 (receipt) / September 2027 (issue for SMEs)
- **Belgium e-invoicing** mandatory B2B from 1 January 2026
- **Poland KSeF** delayed; latest schedule has voluntary continuation through 2025 and mandatory 1 February 2026 for large taxpayers, 1 April 2026 for others
- **Spain Veri*Factu / Verifactu** for non-SII taxpayers in force from 1 January 2026
- **Romania e-Factura** B2B mandatory since 1 July 2024
- **Greece myDATA** B2B fully effective since 2024
- **Saudi Arabia ZATCA Fatoorah Phase 2** waves continuing rolling enrolment
- **Israel "Form Mandate"** for invoice clearance > ILS 5,000 in force since 5 May 2024 (threshold lowering 2025)

**The reviewer is the customer of this output.** E-reporting mandates carry steep penalties and ERP-blocking consequences. Every output must be reviewed by a credentialed e-invoicing / VAT specialist before any go-live decision.

## Section 1 — Scope statement

This skill covers:

- **SAF-T mandates** (Standard Audit File for Tax — OECD-aligned XML extract on demand or periodic)
- **Real-time / near-real-time invoice transmission** — clearance models (Italy SDI), pre-clearance models (Hungary RTIR), reporting models (Spain SII), centralised platform models (Poland KSeF, France PPF, Belgium PEPPOL)
- **CTC (Continuous Transaction Controls)** taxonomies — clearance, reporting, hybrid, decentralised
- **EU ViDA** alignment: by 2030 all intra-EU B2B invoices must be structured EN 16931 and digital reporting requirements (DRR) replace recapitulative statements

This skill does NOT cover:

- **VAT rate determination** (see country `*-vat-return.md` skills)
- **B2C e-receipt mandates** (Greek myDATA B2C, Italian corrispettivi telematici) unless overlapping with the B2B system
- **Software accreditation** procedures with national tax authorities
- **Detailed XSD schema field-level mapping** beyond format and core blocks
- **E-archiving retention beyond the minimum**

## Section 2 — SAF-T matrix

**SAF-T matrix**  _(Section 2 — SAF-T matrix)_

| Country | Status | Trigger | Frequency | Source |
| --- | --- | --- | --- | --- |
| **Portugal** | Mandatory since 2008; expanded to invoicing 2013 | All entities with accounting obligations; threshold-based for invoicing module | Monthly transmission of invoicing SAF-T-PT; annual accounting SAF-T-PT | Decreto-Lei 28/2019; Portaria 302/2016 |
| **Poland — JPK_V7M / V7K** | Mandatory monthly/quarterly for all VAT-registered taxpayers since 2020 | All VAT taxpayers | Monthly (V7M) or quarterly (V7K) | Ustawa o VAT art. 99 ust. 11c; Rozporządzenie MF 2019 |
| **Poland — JPK_KR (general ledger)** | On-demand for all VAT taxpayers; mandatory periodic submission starting 2025–2026 for large taxpayers | Large taxpayers (revenue > EUR 50m); broader scope phased | Phased; periodic from 2025 | Ordynacja Podatkowa art. 193a |
| **Romania — D406 (SAF-T)** | Mandatory since 1 Jan 2022 for large taxpayers; 1 Jan 2023 medium; 1 Jan 2025 small | All taxpayers (final phase 2025) | Monthly | OMFP 1783/2021 |
| **Norway — SAF-T Financial** | Mandatory on demand since 1 Jan 2020 for entities with > NOK 5m revenue or > 600 vouchers | Trigger-based on tax authority request | On demand only | Skatteforvaltningsforskriften §7-3-7 |
| **Lithuania — i.SAF + i.MAS** | Mandatory since 2016 i.SAF (sales/purchase journals) for VAT taxpayers; i.MAS for transport data | All VAT-registered businesses | Monthly | Law on Tax Administration art. 42 |
| **Luxembourg — FAIA** | On demand for entities subject to Luxembourg Commercial Law accounting; FAIA is the local SAF-T variant | All commercial-law entities on request | On demand | Loi du 19 décembre 2008 |
| **France — FEC** | Mandatory on tax audit since 2014; not periodic | Audited entities | On audit | CGI Art. L47 A I; LPF |
| **Hungary — SAF-T Online (NAV)** | Voluntary now; mandatory tooling rollout 2025-2026 | Initially large taxpayers | Periodic upon mandate | Hungarian Tax Authority guidelines |
| **Austria — SAF-T (Datenträger)** | On demand during tax audits | Audited entities | On audit | BAO §131-132 |
| **Spain — TicketBAI (Basque)** | Mandatory in Basque Country since 2022 (phased entity-size) — region-specific | All entities in Basque Country | Real-time per invoice (CTC overlay) | Norma Foral 4/2020 (Bizkaia), parallel in Gipuzkoa/Álava |
| **Mexico — Pólizas / Catálogo de Cuentas** | Monthly upload of journal entries linked to electronic invoices since 2015 | All taxpayers with accounting obligations | Monthly | Artículo 28 fracción IV CFF |
| **Angola — SAF-T (AO)** | Mandatory since 2019 for VAT taxpayers | All VAT taxpayers | Monthly | Decreto Presidencial 312/18 |
| **Cape Verde — SAF-T (CV)** | Mandatory since 2017 | VAT taxpayers | Monthly | Decreto-Lei 41/2017 |

## Section 3 — Real-time / clearance e-invoice matrix

**Real-time / clearance e-invoice matrix**  _(Section 3 — Real-time / clearance e-invoice matrix)_

| Country | Mandate | Effective date | Model | Format | Transmission |
| --- | --- | --- | --- | --- | --- |
| **Italy — SDI** | All B2B and B2C since 2019 (residents); cross-border via Esterometro merged into SDI 2022 | Live | Pre-clearance | FatturaPA XML | SDI portal (centralised) |
| **France — PPF + PDP** | Mandatory receipt 1 Sep 2026; outbound staged Sep 2026–Sep 2027 | 2026–2027 | Centralised + accredited PDPs | Factur-X (XML-PDF hybrid), Peppol BIS, UBL | PPF (Portail Public de Facturation) or via PDP |
| **Germany — XRechnung / B2G + ZUGFeRD / B2B** | B2B receipt mandatory 1 Jan 2025; issue mandatory 1 Jan 2027 (large), 1 Jan 2028 (others) | 2025–2028 | Pre-issue structured invoice (no central clearance) | XRechnung / ZUGFeRD / Factur-X / EN 16931-compliant | Direct (any agreed channel) — clearance NOT centralised |
| **Spain — SII** | Real-time near-time reporting since 2017 for ≥ EUR 6m turnover, voluntary for smaller | Live | Reporting (post-issue within 4 days) | XML JSON web service | AEAT web service |
| **Spain — Verifactu / Veri*Factu** | All non-SII VAT taxpayers from 1 Jan 2026 (corporates) / 1 Jul 2026 (others) | 2026 | Post-issue reporting (transactional) | Verifactu XML | AEAT |
| **Poland — KSeF** | Mandatory 1 Feb 2026 (large), 1 Apr 2026 (others) | 2026 | Pre-clearance | KSeF XML (FA(2)) | KSeF central platform |
| **Belgium** | B2B mandatory 1 Jan 2026 | 2026 | Decentralised via Peppol BIS | Peppol BIS / EN 16931 | Peppol-network |
| **Romania — e-Factura** | B2B mandatory since 1 Jul 2024 | Live | Pre-clearance | RO_CIUS_EN16931 | RO e-Factura portal (SPV) |
| **Greece — myDATA** | Fully effective since 2024 for B2B + B2C | Live | Reporting (real-time/near-real-time) | myDATA XML | AADE portal |
| **Hungary — RTIR (Online Számla)** | All B2B since 2018; B2C from 1 Jan 2021 | Live | Reporting near-real-time | NAV XML schema | NAV portal |
| **Portugal — ATCUD / QR code + SAF-T** | ATCUD/QR mandatory since 2023; SAF-T invoicing monthly | Live | Pre-issue ATCUD + post-issue SAF-T | SAF-T-PT XML | Authority on demand + monthly SAF-T |
| **Bulgaria** | SAF-T schedule TBD; VAT one-step return | Pending | TBD | TBD | TBD |
| **Croatia — Fiskalizacija** | All B2C since 2013; B2B coming in line with ViDA | Live (B2C); B2B in development | Pre-issue clearance (B2C) | Croatian fiscalisation XML | Porezna uprava |
| **Slovakia** | E-invoicing reform pending; 2026 target | 2026 (proposed) | TBD | TBD | TBD |
| **Czech Republic** | E-invoicing reform pending; 2027 target | 2027 (proposed) | TBD | TBD | TBD |
| **United Kingdom** | No B2B e-invoicing mandate as of 2025; consultation issued 2025 | Consultation | TBD | TBD | TBD |
| **Ireland** | No mandate as of 2025; consultation in progress | Consultation | TBD | TBD | TBD |
| **Norway — EHF** | Mandatory B2G since 2019; B2B voluntary | Live (B2G) | Decentralised | Peppol BIS / EHF | Peppol |
| **Denmark — OIOUBL / Peppol** | Mandatory B2G; B2B from 2026 (digital bookkeeping act) | 2026 (B2B) | Decentralised | Peppol BIS | Peppol |
| **Sweden** | Mandatory B2G since 2019; B2B in consultation | Live B2G | Decentralised | Peppol BIS | Peppol |
| **Finland** | Buyer can request e-invoice since 2020 (right to receive) | Live (right-to-receive) | Decentralised | Finvoice / Peppol | Various |

### Asia, Middle East, Latin America

**Asia, Middle East, Latin America matrix**  _(Asia, Middle East, Latin America)_

| Country | Mandate | Effective | Model | Format | Transmission |
| --- | --- | --- | --- | --- | --- |
| **Saudi Arabia — Fatoorah** | All VAT-registered; Phase 1 (Dec 2021) + Phase 2 integration in waves (Jan 2023 onwards) | Live (waves) | Pre-clearance (Phase 2) | XML / hybrid PDF/A-3 | ZATCA Fatoora platform |
| **UAE** | E-invoicing scheme planned 2026 | 2026 | TBD | EN 16931-aligned | TBD |
| **Egypt — ETA** | Mandatory B2B since 2021 | Live | Pre-clearance | ETA XML / JSON | ETA portal |
| **Turkey — e-Fatura / e-Arşiv Fatura** | All VAT taxpayers ≥ TRY 5m turnover; lower thresholds in specific sectors | Live | Pre-clearance | UBL-TR | GİB |
| **Israel — Form Mandate / Hashbonit** | Invoices > ILS 5,000 require pre-clearance number since 5 May 2024 (threshold reduces 2025/2026) | Live | Pre-clearance | XML | ITA portal |
| **Vietnam** | All VAT taxpayers since 1 Jul 2022 | Live | Pre-clearance / pre-issue | XML | GDT |
| **India — IRP / GSTN** | All taxpayers ≥ INR 5 crore turnover since 1 Aug 2023 (threshold lowered from 10 crore) | Live | Pre-clearance (IRN generation) | IRP JSON | IRP portals (NIC, etc.) |
| **Indonesia — e-Faktur** | All VAT taxpayers since 2016 | Live | Pre-clearance | XML | DGT portal |
| **Philippines** | EIS (Electronic Invoicing System) for top 100 taxpayers since 2022; phased expansion | Phased | Reporting near-real-time | JSON | EIS portal |
| **Mexico — CFDI 4.0** | All VAT taxpayers since 2014; CFDI 4.0 from 2022 | Live | Pre-clearance via PAC | XML CFDI 4.0 | PAC (private certified provider) → SAT |
| **Chile — DTE** | All VAT taxpayers since 2018 | Live | Pre-clearance | XML | SII |
| **Brazil — NF-e / NFS-e / NFC-e** | All taxpayers (NF-e since 2008 for goods; NFS-e municipal services; NFC-e consumer goods) | Live | Pre-clearance | XML | SEFAZ (state) / municipal |
| **Argentina — Comprobantes Electrónicos** | All VAT taxpayers since 2015 | Live | Pre-clearance | XML / web service | AFIP |
| **Colombia — Factura Electrónica DIAN** | All taxpayers phased 2018-2020 | Live | Pre-clearance | XML | DIAN |
| **Peru — SEE Sunat** | Phased rollout completed 2024 for all taxpayers | Live | Pre-clearance | XML UBL 2.1 | SUNAT or accredited PSE |
| **Ecuador — Comprobantes Electrónicos** | All taxpayers since 2018 | Live | Pre-clearance | XML | SRI |
| **Uruguay — CFE** | All taxpayers since 2019 | Live | Pre-clearance | XML | DGI |

## Section 4 — EU ViDA — Digital Reporting Requirements

**[T1] Council Directive (EU) 2025/516 elements**  _(Council Directive (EU) 2025/516 amending Directive 2006/112/EC and Regulation (EU) 282/2011)_

| Element | Date | Detail |
| --- | --- | --- |
| Optional national e-invoicing without Article 232 derogation | 1 January 2027 | Member States may mandate B2B e-invoicing without prior Council authorisation; ViDA-aligned format required |
| Recapitulative statements abolished | 1 July 2030 | Replaced by Digital Reporting Requirements (DRR) |
| Mandatory structured EU intra-Community e-invoice | 1 July 2030 | EN 16931-compliant; 10-day issuance deadline; transactional reporting to each Member State of supplier and customer |
| Single EU VAT identification + OSS expansion | 1 July 2028 | Extension of OSS to B2C movements of own goods |
| Platform economy deemed-supplier | 1 July 2028 (with optional 2030) | Short-term accommodation and passenger transport platforms become deemed supplier |

- **[T2] EN 16931 alignment and pre-clearance prohibition** — Member States must align national e-invoicing systems with EN 16931 by 1 July 2030. Pre-clearance models that block invoice transmission are NOT permitted under ViDA (post-clearance reporting only). Italy's SDI and France's PPF have explicit transition paths.  _([T2])_

## Section 5 — Decision flow

### Step 1 — Determine taxpayer status in each jurisdiction

- **Taxpayer status determination steps** — For each country where the taxpayer issues invoices to local customers OR receives invoices from local suppliers OR has VAT registration: 1. VAT-registered? → check the country's e-invoicing scope 2. Threshold-based exemption? → check turnover thresholds 3. Sector-specific carve-out? → check (e.g., Italian SDI exempts certain micro-businesses under EUR 65k revenue with forfettario regime; Spanish SII exempts < EUR 6m turnover)  _(Step 1 — Determine taxpayer status in each jurisdiction)_

### Step 2 — Select format

- **Format selection by jurisdiction** — - Cross-border within EU → Peppol BIS billing 3.0 or EN 16931-aligned XML - Italy → FatturaPA - France → Factur-X (hybrid PDF/A-3 + UBL or CII) OR Peppol BIS - Germany → XRechnung (B2G) / ZUGFeRD or Factur-X / EN 16931 (B2B) - Spain → Verifactu XML for SII / Verifactu - Poland → KSeF FA(2) XML - Saudi Arabia → ZATCA XML or PDF/A-3 with embedded XML - LATAM → country-specific (CFDI Mexico, DTE Chile, etc.)  _(Step 2 — Select format)_

### Step 3 — Select transmission channel

- **Transmission channel selection** — - Centralised → Italy SDI, Poland KSeF, France PPF, Romania SPV, Spain Verifactu/SII web service - Decentralised via Peppol → Belgium, Norway, Denmark, Sweden, EU intra-Community by 2030 - Direct B2B without clearance → Germany B2B - LATAM PAC/PSE intermediaries → Mexico, Brazil, Peru, Chile  _(Step 3 — Select transmission channel)_

### Step 4 — Plot deadlines and penalties

**Typical penalty by country**  _(Step 4 — Plot deadlines and penalties)_

| Country | Typical penalty |
| --- | --- |
| Italy SDI | EUR 250–2,000 per non-compliant invoice; deductibility disallowed |
| Poland KSeF | Up to 100% of VAT shown on non-compliant invoice (initial 6-month grace) |
| Germany B2B | Loss of input VAT recovery for non-EN-16931 invoice receipt |
| Romania e-Factura | RON 1,000–10,000 per missing invoice |
| Greece myDATA | EUR 5,000–100,000 fines |
| Hungary RTIR | HUF 500,000 per missing report |
| Saudi Arabia ZATCA Phase 2 | SAR 1,000+ per invoice; escalating |
| India IRN | INR 25,000 per invoice without IRN; ITC disallowance |
| Spain SII | EUR 0.5% of unreported amount, min EUR 300 / max EUR 6,000 per quarter |

## Section 6 — Output specification

The reviewer brief must include:

1. **Jurisdiction inventory** — every country with mandate exposure for the entity.
2. **Mandate status per country** — in-force / pending / proposed; effective date for the entity.
3. **Format and transmission selection** per country.
4. **Implementation roadmap** — ERP changes, intermediary selection (PAC / PDP), accreditation status, go-live dates.
5. **Data residency and archiving** — required retention period per country (commonly 10 years), location restrictions.
6. **Penalty exposure** if go-live missed.
7. **EU ViDA alignment** — for EU-registered taxpayers, the 1 July 2030 DRR transition plan.
8. **Reviewer questions** — open items flagged as [T2] or [T3].

## Section 7 — Self-checks

- [ ] Every country of registration / supply / receipt mapped to a mandate status.
- [ ] Threshold tests applied (turnover, sector) before assuming in-scope.
- [ ] Format selected per country, not assumed by analogy.
- [ ] Transmission channel matches model (centralised / decentralised / PAC).
- [ ] Pre-clearance model identified where invoice transmission is blocking.
- [ ] ViDA DRR transition plotted for 1 July 2030 deadline.
- [ ] Italy SDI cross-border replacement of Esterometro reflected.
- [ ] Mexico Pólizas + CFDI 4.0 + Catálogo de Cuentas integration documented.
- [ ] Penalty schedule per country in the brief.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 8 — Prohibitions

- **Do not** assume Peppol BIS is universally accepted — Italy SDI, Mexico CFDI, Brazil NF-e use proprietary formats and Peppol is NOT the local mandate.
- **Do not** treat a "B2G mandate" as equivalent to a "B2B mandate" — Norway, Sweden, Denmark have B2G mandates but B2B is still voluntary in 2025.
- **Do not** rely on the EU ViDA 2030 dates as locked — Member State adoption pace varies and derogations may persist.
- **Do not** propose a centralised-clearance go-live for ViDA-compliant intra-Community invoicing — post-clearance only is permitted under ViDA.
- **Do not** advise on circumventing mandates (e.g., issuing PDF invoices in a clearance regime) — penalties and VAT recovery loss apply.

## Section 9 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax or implementation advice. E-invoicing and SAF-T mandates change frequently with national budget cycles and EU directives. Every output must be reviewed and signed off by a credentialed e-invoicing / VAT specialist before any go-live decision.

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
