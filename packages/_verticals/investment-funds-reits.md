---
name: investment-funds-reits
description: "Use this skill whenever a regulated investment fund, hedge fund, private equity fund, real estate investment trust (REIT), UCITS, AIF, mutual fund, or fund manager asks about sector-specific tax. Trigger on phrases like \"UCITS tax\", \"AIFMD\", \"RAIF\", \"SIF\", \"SICAR\", \"FCP\", \"FCPR\", \"SLP\", \"ELTIF\", \"PE fund\", \"carried interest tax\", \"carry\", \"promote\", \"GP / LP allocation\", \"K-1\", \"PFIC\", \"QEF election\", \"CFC for funds\", \"REIT\", \"Section 856-860\", \"PID\", \"UK REIT\", \"SOCIMI\", \"S-REIT Singapore\", \"J-REIT Japan\", \"Master fund / feeder fund\", \"Investment Tax Act Germany\", \"tax-transparent fund\", \"blockers\", or any question on fund / REIT-specific tax. Covers UCITS / AIF tax interaction, fund-level vs investor-level taxation, REIT regimes globally (US, UK, France, Germany, Netherlands, Spain SOCIMI, Australia AREIT, Singapore S-REIT, Japan J-REIT), carried interest tax (US, UK, France, Italy), and PFIC vs QEF mechanics for US-taxable investors. Does NOT cover: fund formation, AIFMD authorisation, MIFID II compliance, or investment management agreement drafting."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - corporate-income-tax-workflow-base
category: vertical
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Investment Funds REITS

## What this file is

A sector overlay for investment funds and REITs covering fund-level, GP-level, and investor-level taxation.

## Section 1 — Fund taxation principles

**[T1] Two foundational models**

| Model | Fund-level tax | Investor-level tax |
| --- | --- | --- |
| **Tax-transparent** | None (the fund "looks through" to investors) | Investor taxed on its share of fund income as if directly held |
| **Tax-opaque (blocker)** | Fund pays CIT (usually with offset for distributions) | Investor taxed only on distributions / dispositions |

- US LP / LLC
- UK Partnership
- Cayman Exempted LP
- Luxembourg RAIF as SIF / SCSp (partnership)
- Irish ILP (Investment Limited Partnership)

### 2.1 UCITS

**[T1]** UCITS funds (Undertaking for the Collective Investment in Transferable Securities) under Directive 2009/65/EC are usually structured as:
- **Investment company with variable capital** (SICAV in Luxembourg, ICAV in Ireland)
- **Common contractual fund** (FCP in Luxembourg / France)
- **Unit trust** (UK)

- **Luxembourg UCITS fund-level tax** — Subscription tax (taxe d'abonnement) — 0.05% / 0.01% (annual on NAV); no CIT on UCITS profits  _(Luxembourg fund-level tax)_
- **Ireland UCITS fund-level tax** — ICAV / UCITS exempt CIT under TCA s.739D — Investment Undertaking Tax (IUT) only on Irish resident investors  _(TCA s.739D)_
- **France UCITS fund-level tax** — FCP transparent; SICAV with specific regime  _(Fund-level tax)_
- **UK UCITS fund-level tax** — Authorised funds with specific UK fund tax regime  _(Fund-level tax)_

### 2.2 AIF (Alternative Investment Fund)

**[T1]** AIFs under AIFMD (Directive 2011/61/EU) have wider product range:
- Hedge funds
- Private equity funds
- Real estate funds
- Infrastructure funds
- Hybrid funds

Tax treatment depends on legal form and jurisdiction; typically tax-transparent or low-tax-blocker.

### 2.3 Specific Luxembourg vehicles

**Specific Luxembourg vehicles**

| Vehicle | Tax |
| --- | --- |
| **SIF (Specialised Investment Fund)** | Subscription tax 0.01% NAV; no CIT (Lux Law 13 February 2007) |
| **RAIF (Reserved Alternative Investment Fund)** | Choice of SIF-style or SICAR-style; flexible (Law 23 July 2016) |
| **SICAR (Société d'Investissement en Capital à Risque)** | Subscription tax-exempt; CIT but with extensive participation exemption; capital risk |
| **SCSp (Special Limited Partnership)** | Tax-transparent (partnership) (Law 12 July 2013) |

## Section 3 — Carried interest tax

**[T1] By jurisdiction**

| Country | Treatment | Effective rate |
| --- | --- | --- |
| **United States** | §1061 ITA: carried interest classified as long-term capital gain only if 3-year holding period (raised from 1 year by TCJA 2017); otherwise short-term ordinary | ~20% LTCG vs 37% short-term/ordinary |
| **United Kingdom** | Carried Interest from April 2025: 32% effective rate (reformed from CGT-only treatment); Disguised Investment Management Fees (DIMF) since 2015 | 32% (proposed from April 2025; consultation ongoing) |
| **France** | Carried interest treated as employment income (and capital gain on disposal) for managers; specific holding period requirement | Effective marginal rate close to top income tax |
| **Italy** | Carried interest classified as investment income if specific conditions met (commitment / employment) | 26% capital gain rate possible |
| **Germany** | 60% of carried interest treated as employment income (Halbeinkünfteverfahren) — favourable | Reduced rate |
| **Spain** | New 2025 rules characterise carried interest as employment income absent specific conditions | Up to ~50% |

## Section 4 — PFIC mechanics (US investors)

- **§1297 ITA — Passive Foreign Investment Company** — A foreign corporation is a PFIC if: ≥75% of gross income is passive (income test), OR ≥50% of average assets produce passive income (asset test)  _(§1297 ITA)_
- **Tax consequences without election** — Excess distributions and dispositions taxed at maximum ordinary rate for prior years held; interest charge for deemed deferral  _([T1])_
- **QEF (Qualified Electing Fund) election** — US investor includes pro-rata share of fund's ordinary earnings and net capital gain annually; Annual PFIC Annual Information Statement required from fund; avoids excess distribution / interest charge regime  _([T1])_
- **MTM (Mark-to-Market) election** — Annual gain/loss recognised on PFIC shares treated as ordinary income; available for "marketable" PFIC shares  _([T1])_
- **PFIC exception — Active insurance corporation** — PFIC exception — Active insurance corporation under §1297(f) — see `insurance-sector.md`.  _(§1297(f))_

### 5.1 US REIT (§§856-860 ITA)

- **Requirements** — 75% gross income from real estate (rents, mortgages, gains on real estate); 95% gross income passive (75% real estate + interest, dividends, gains); 75% asset test (real estate, mortgages, cash, government securities); Distribute at least 90% of taxable income to shareholders; ≥ 100 shareholders; not closely held (5-or-fewer test); Operated as REIT election (§856)  _(§§856-860 ITA)_
- **Tax effect** — Distribution deduction at REIT level — effectively no CIT on distributed income; shareholders taxed on dividends at ordinary rate (except qualified REIT dividends get 20% §199A deduction post-TCJA — now confirmed permanent in OBBBA)  _(§199A; OBBBA)_

### 5.2 UK REIT

- **FA 2006 (now CTA 2010 Part 12) requirements** — 75% gross income from rental of UK property; 75% asset value in property rental business; Listed on recognised stock exchange (or with 35% rule for institutional ownership); 90% distribution requirement; 75% non-resident-investor cap during 3 years from entry; Property Income Distributions (PID) — gross-paid; income tax at 20% basic; 40% higher; 45% additional  _(FA 2006 (now CTA 2010 Part 12))_

### 5.3 French SIIC / OPCI

- **SIIC** — SIIC: listed real estate companies, 85% rental income distribution, 50% gain distribution; CIT exemption on rental and capital gains  _([T1])_
- **OPCI** — OPCI: non-listed open-ended collective investment in real estate  _([T1])_

### 5.4 German G-REIT

**[T1]** Less popular than other markets; ~5 G-REITs listed.

### 5.5 Spanish SOCIMI

- **SOCIMI requirements** — Sociedad Anónima Cotizada de Inversión en el Mercado Inmobiliario: Listed on recognised market; 80% asset and gross income in real estate; 80% distribution of rental income; 100% distribution of REIT-source distributions; 50% of capital gains over 3 years; 0% CIT but 19% specific levy on dividend distributions  _([T1])_

### 5.6 Singapore S-REIT

- **S-REIT requirements** — Tax-transparent for distributions to qualifying unitholders (no S-REIT corporate tax); 90% distribution requirement; Listed on SGX; Cross-border property investment common  _([T1])_

### 5.7 Japanese J-REIT

- **J-REIT requirements** — Investment corporations under Investment Trust Act; 90% distribution requirement; Reduced or zero CIT on distributed income  _([T1])_

### 5.8 Australian A-REIT

- **A-REIT structure** — Listed stapled trust + corporation structures common; Mostly tax-transparent at trust level; AMIT (Attribution Managed Investment Trust) regime since 2016  _([T1])_

## Section 6 — Blocker structures

- **Blocker entity purposes** — "Blocker" entities interpose tax-opaque vehicles to: Convert ordinary income to capital gains for US investors; Block US ECI for foreign LP investors; Prevent CFC consequences for US shareholders; Avoid PFIC exposure for US-taxable investors  _([T1])_

- US-blocker (C-corp) below partnership / LLC
- Cayman or BVI blocker above offshore investments
- Luxembourg SICAV/SCSp for EU fund families
- Multi-tier structures with hybrid mismatches (now constrained by ATAD II)

## Section 7 — Self-checks

- [ ] Fund legal form classified for tax (transparent vs opaque)
- [ ] UCITS / AIF status verified for regulatory regime
- [ ] Local fund-level tax computed (subscription tax / IUT / CIT)
- [ ] Investor-level tax mechanics documented per investor country
- [ ] PFIC test applied for US-taxable investors with appropriate election
- [ ] Carried interest classification per jurisdiction
- [ ] REIT distribution requirements met (75/95/90/etc.)
- [ ] Property Income Distribution (UK PID) gross-up treatment correct
- [ ] Blocker structures support business purpose
- [ ] Pillar Two GloBE Income excludes "Investment Entity" income per Article 7
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 8 — Disclaimer

Fund and REIT taxation is highly specialised and varies dramatically by structure. Outputs must be reviewed by credentialed fund-sector practitioners. The most up-to-date version is at [openaccountants.com](https://openaccountants.com).

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
