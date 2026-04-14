---
name: ch-cantonal-tax
description: >
  Use this skill whenever asked about Swiss cantonal and communal income tax (Staatssteuer / Gemeindesteuer / impot cantonal et communal) for self-employed individuals. Trigger on phrases like "Kantonssteuer", "Gemeindesteuer", "cantonal tax Switzerland", "Steuerfuss", "tax multiplier Swiss", "kirchensteuer Schweiz", "impot cantonal", "communal tax rate", "Steuerausscheidung", "Swiss income tax", "einfache Steuer", or any question about cantonal/communal income tax for a self-employed person in Switzerland. This skill covers the cantonal tax multiplier system (Steuerfuss), church tax, inter-cantonal allocation, and the interaction between cantonal and federal returns. MUST be loaded alongside ch-federal-income-tax for the complete picture. ALWAYS read this skill before touching any Swiss cantonal tax work.
version: 2.0
---

# Switzerland Cantonal and Communal Income Tax — Self-Employed v2.0

## Section 1 — Quick Reference

### Swiss Three-Level Tax System

| Level | Tax Name | Legislation | Rate Structure |
|---|---|---|---|
| Federal | Direkte Bundessteuer (dBSt) | DBG (SR 642.11) | Fixed progressive schedule, same nationwide |
| Cantonal | Staatssteuer / Kantonssteuer | Each canton's Steuergesetz | Base tariff x cantonal Steuerfuss |
| Communal | Gemeindesteuer | Each commune's Steuerfuss | Base tariff x communal Steuerfuss |

All three levels filed on a single combined Steuererklarung through the cantonal tax portal.

### The Steuerfuss / Multiplier System

```
Einfache Steuer = base tariff applied to steuerbares Einkommen
Kantonssteuer = Einfache Steuer x kantonaler Steuerfuss (%)
Gemeindesteuer = Einfache Steuer x Gemeindesteuerfuss (%)
Kirchensteuer = Einfache Steuer x Kirchensteuerfuss (%) [if church member]
Total cantonal/communal tax = sum of above
```

### Selected Cantonal/Municipal Steuerfuss (2025, Approximate)

| Canton | Capital City | Cantonal SF | Municipal SF (Capital) | Church (Reformed) | Effective Combined |
|---|---|---|---|---|---|
| Zurich (ZH) | Zurich | 100% | ~119% | ~11% | ~230% of Grundtarif |
| Bern (BE) | Bern | 3.06 units | 1.54 | 0.194 | ~4.79 units |
| Luzern (LU) | Luzern | 1.60 units | 1.75 | 0.24 | ~3.59 units |
| Zug (ZG) | Zug | 82% | 60% | ~8% | ~150% of Grundtarif |
| Basel-Stadt (BS) | Basel | Direct tariff | (included) | ~8% of Staatssteuer | N/A (direct) |
| Geneva (GE) | Geneva | 47.79% (centimes) | 45.5 centimes | N/A | N/A (centimes) |
| Vaud (VD) | Lausanne | 154.5% | 79% | ~10% | N/A (composite) |
| Schwyz (SZ) | Schwyz | 150% | ~130% | ~17% | ~297% of Grundtarif |
| Ticino (TI) | Bellinzona | 100% | ~95% | ~8% | ~203% of Grundtarif |

WARNING: Steuerfuss values change annually. Always verify the current year's values from the cantonal Steuerverwaltung or ESTV tax calculator.

### Exceptions to the Multiplier System

- **Basel-Stadt (BS):** Direct tariff, no multiplier. Canton and city merged.
- **Geneva (GE):** Centimes additionnels system.
- **Appenzell Innerrhoden (AI):** Simplified multiplier.
- **Graubunden (GR):** Multiplier plus municipal surtaxes.

### Key Cantonal Deduction Differences from Federal

| Item | Federal (DBG) | Cantonal (StHG) |
|---|---|---|
| Kinderabzug (child) | CHF 6,600/child | Varies: CHF 6,500 -- 13,000+ |
| Versicherungsabzug (insurance) | CHF 1,800 (single) / CHF 3,600 (married) | Often higher |
| Saeule 3a (Pillar 3a) | CHF 35,280 (self-employed without BVG) or CHF 7,056 (with BVG) | Same |
| AHV/IV/EO | Fully deductible | Fully deductible |
| BVG (Pillar 2) | Fully deductible | Fully deductible |

### Computation Steps

```
1. Determine steuerbares Einkommen (cantonal)
   = Gross self-employment income
   - Geschaeftsaufwand (business expenses)
   - AHV/IV/EO contributions
   - BVG contributions
   - Saeule 3a contributions
   - Cantonal-specific deductions (Kinderabzug, Versicherungsabzug, etc.)

2. Look up einfache Steuer from cantonal base tariff

3. Apply multipliers:
   Kantonssteuer = einfache_steuer x kantonaler_steuerfuss
   Gemeindesteuer = einfache_steuer x gemeinde_steuerfuss
   Kirchensteuer = einfache_steuer x kirchen_steuerfuss

4. Total = Kantonssteuer + Gemeindesteuer + Kirchensteuer + Bundessteuer
```

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Canton/municipality unknown | STOP — rates vary enormously |
| Church membership unknown | Assume member (higher tax); ask to confirm |
| Steuerfuss year uncertain | Verify current year with cantonal Steuerverwaltung |
| Cantonal deduction amounts | Use federal amounts as minimum; verify cantonal |
| Einfache Steuer computation | NEVER compute manually — use official tariff tables |
| Inter-cantonal allocation needed | Flag for Treuhaender review |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Canton/municipality not specified | Cannot compute — stop |
| Business in multiple cantons | Steuerausscheidung required |
| Real property in another canton | Inter-cantonal allocation triggered |
| Church membership not confirmed | Church tax may apply (5-15% of einfache Steuer) |
| Mid-year cantonal move | Only 31 December residence canton taxes full year |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

1. **Canton of tax residence** — determines cantonal law and base tariff
2. **Municipality (Gemeinde)** — determines communal Steuerfuss
3. **Marital status** — single, married, registered partnership
4. **Church membership** — member of recognised church? Which denomination?
5. **Steuerbares Einkommen** — after all deductions
6. **Business activity in multiple cantons?** — triggers Steuerausscheidung
7. **Real property in another canton?** — triggers allocation
8. **Children / dependants** — Kinderabzug varies by canton
9. **Prior year Steuerrechnung** — for provisional payment reconciliation
10. **Bank statements** — 12 months

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-CH-1 | Canton and municipality unknown | Stop — cannot compute without specific location |
| R-CH-2 | Quellensteuer (source tax) for foreign nationals | Escalate — different regime for non-C-permit holders |
| R-CH-3 | Inter-cantonal allocation dispute | Escalate — Doppelbesteuerungsverbot requires specialist |
| R-CH-4 | Wealth tax (Vermogenssteuer) computation | Flag — separate computation, filed on same return |
| R-CH-5 | Steuererlass (tax relief) application | Escalate — hardship case outside scope |

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `GUTSCHRIFT [client]` / `EINGANG [client]` | Gross self-employment income | Standard bank credit from client |
| I-02 | `VERGUTUNG [client]` / `ZAHLUNG VON [client]` | Gross self-employment income | Payment from client |
| I-03 | `TWINT EINGANG [client]` | Gross self-employment income | TWINT (Swiss mobile payment) receipt |
| I-04 | `QR-RECHNUNG EINGANG` / `QR ZAHLUNG ERHALTEN` | Gross self-employment income | QR-bill payment received |
| I-05 | `STRIPE PAYOUT CHF` / `STRIPE AUSZAHLUNG` | Gross income — gross-up | Stripe net payout; fee deductible |
| I-06 | `PAYPAL GUTSCHRIFT` / `PAYPAL AUSZAHLUNG` | Gross income — gross-up or foreign | PayPal receipt |
| I-07 | `STEUERRUCKERSTATTUNG` / `RUCKZAHLUNG STEUERN` | NOT income — tax refund | Tax refund from canton |
| I-08 | `ZINSEN` / `ZINSGUTSCHRIFT` / `KONTOZINS` | Financial income | Bank interest; subject to Verrechnungssteuer (35% WHT) |
| I-09 | `MIETEINNAHMEN` / `MIETE VON [tenant]` | Rental income | Separate treatment; includes in total income |
| I-10 | `DIVIDENDE` / `AUSSCHUTTUNG` | Dividend income | Subject to partial taxation (Teilbesteuerung if >10% holding) |

### 3.2 Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `MIETE BURO` / `MIETZINS GESCHAFT` / `LOYER BUREAU` | Office rent — Geschaeftsaufwand | Fully deductible |
| E-02 | `STROM` / `ELEKTRIZITAET` / `EW ZURICH` / `BKW` / `ALPIQ` | Electricity — deductible (business proportion) | Require invoice |
| E-03 | `SWISSCOM` / `SUNRISE` / `SALT` / `UPC` | Telecom/internet — deductible (business %) | Require invoice |
| E-04 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — fully deductible | Professional tools |
| E-05 | `TREUHANDER` / `STEUERBERATER` / `BUCHHALTER` / `FIDUCIAIRE` | Tax advisor/accountant — fully deductible | |
| E-06 | `SBB` / `BLS` / `SWISS FEDERAL RAILWAYS` | Train travel — deductible (business purpose) | Swiss Federal Railways |
| E-07 | `SWISS` / `EASYJET` / `HELVETIC AIRWAYS` | Air travel — deductible (business purpose) | Document purpose |
| E-08 | `AHV` / `AUSGLEICHSKASSE` / `AVS` / `CAISSE DE COMPENSATION` | AHV/IV/EO contributions — fully deductible | Social security; always deduct |
| E-09 | `BVG` / `PENSIONSKASSE` / `2. SAULE` / `LPP` / `CAISSE DE PENSION` | BVG (Pillar 2) — fully deductible | Pension fund contribution |
| E-10 | `SAEULE 3A` / `3A KONTO` / `PILIER 3A` | Pillar 3a — deductible (CHF 35,280 cap self-employed without BVG) | Verify cap |
| E-11 | `KRANKENKASSE` / `CSS` / `HELSANA` / `SWICA` / `SANITAS` | Health insurance — Versicherungsabzug | Cantonal deduction; verify cantonal limit |
| E-12 | `STEUERN` / `STEUERAMT` / `KANTONALE STEUERN` | Tax payment — NOT a Geschaeftsaufwand | Tax payments reduce Schulden (wealth), not income |
| E-13 | `MWST` / `UST` / `TVA PAIEMENT` | VAT payment — NOT deductible | VAT is separate |
| E-14 | `BENZIN` / `DIESEL` / `TANKSTELLE` / `MIGROL` / `COOP PRONTO` | Fuel — deductible (business proportion) | Document business use |
| E-15 | `BUROMATERIAL` / `PAPETERIE` | Office supplies — fully deductible | |
| E-16 | `WEITERBILDUNG` / `KURS` / `SEMINAR` / `FORMATION` | Training — deductible | Professional development |
| E-17 | `VERSICHERUNG` / `ASSURANCE` / `BERUFSHAFTPFLICHT` | Professional insurance — fully deductible | Liability/professional insurance |
| E-18 | `SPENDE` / `DONATION` / `GEMEINNUETZIGE` | Charitable donations — deductible | 20% of net income (federal); cantonal may differ |

### 3.3 Swiss Bank Fees (Deductible)

| Pattern | Treatment | Notes |
|---|---|---|
| UBS, UBS SWITZERLAND | Deductible for business account fees | |
| CREDIT SUISSE, CS (now UBS) | Deductible for business account fees | |
| ZKB, ZURCHER KANTONALBANK | Deductible for business account fees | Cantonal bank |
| RAIFFEISEN | Deductible for business account fees | Cooperative bank |
| POSTFINANCE | Deductible for business account fees | |
| BCGE, BANQUE CANTONALE DE GENEVE | Deductible for business account fees | |
| BCV, BANQUE CANTONALE VAUDOISE | Deductible for business account fees | |
| BERNER KB, BLKB, LUKB, SGKB | Deductible — cantonal banks | Various cantonal banks |
| KONTOGEBUHR, FRAIS DE COMPTE | Deductible | Account maintenance fee |
| ZAHLUNGSVERKEHR, TRAFIC DES PAIEMENTS | Deductible | Payment transaction fees |

### 3.4 Government and Statutory (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| STEUERAMT, STEUERVERWALTUNG | EXCLUDE | Cantonal tax authority payment |
| EIDG. STEUERVERWALTUNG | EXCLUDE | Federal tax authority |
| AUSGLEICHSKASSE (if tax portion) | Separate AHV (deductible) from other payments | |
| GEMEINDE (if tax payment) | EXCLUDE | Communal tax payment |
| HANDELSREGISTERAMT | Deductible | Commercial registry fee |

### 3.5 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| EIGENE UBERTRAGUNG, UMBUCHUNG | EXCLUDE | Internal movement |
| BARGELDBEZUG, RETRAIT | TIER 2 — ask | Default exclude; determine purpose |
| HYPOTHEK, HYPOTHEQUE | EXCLUDE | Mortgage payment (interest may be wealth deduction) |

---

## Section 4 — Worked Examples

### Example 1 — ZKB (Zurich City, Single Freelancer, Reformed Church)

**Bank:** Zurcher Kantonalbank (ZKB) statement
**Client:** Thomas Muller, freelance software developer, Zurich, single, Reformed church member

```
Datum;Text;Belastung;Gutschrift;Saldo
05.01.2025;GUTSCHRIFT TECH AG;;12'500.00;
15.01.2025;KONTOGEBUHR;5.00;;
10.02.2025;GUTSCHRIFT STARTUP GMBH;;8'200.00;
28.02.2025;AHV AUSGLEICHSKASSE;1'800.00;;
15.03.2025;STRIPE AUSZAHLUNG;;4'350.00;
01.04.2025;SWISSCOM;89.00;;
05.06.2025;SAEULE 3A EINZAHLUNG;7'056.00;;
10.07.2025;TREUHANDER MEIER;1'500.00;;
10.10.2025;SBB REISE BERN;85.00;;
```

**Computation:**

Gross income (annualised): CHF 100,000
Geschaeftsaufwand: CHF 20,000 (telecom, travel, accountant, software, supplies)
AHV/IV/EO: CHF 7,200 (self-employed rate ~9.7% of net earnings)
Saeule 3a: CHF 7,056 (with BVG)

Steuerbares Einkommen (cantonal): ~CHF 65,744

Zurich Grundtarif lookup: einfache Steuer ~CHF 4,800
- Kantonssteuer: CHF 4,800 x 100% = CHF 4,800
- Gemeindesteuer: CHF 4,800 x 119% = CHF 5,712
- Kirchensteuer: CHF 4,800 x 11% = CHF 528
- Total cantonal/communal: ~CHF 11,040
- Plus Bundessteuer: ~CHF 1,900
- **Grand total: ~CHF 12,940**

### Example 2 — Raiffeisen (Zug, Married, No Church)

**Bank:** Raiffeisen Zug
**Client:** Andrea and Marco Bianchi, married (single income), Zug city, no church

Gross: CHF 150,000. Geschaeftsaufwand: CHF 30,000. AHV: CHF 10,800. Saeule 3a: CHF 7,056. 2 children.

Steuerbares Einkommen (cantonal): ~CHF 87,000 (after Zug-specific Kinderabzug)
Zug Verheiratetentarif: very low base tariff.
- Kantonssteuer: einfache Steuer x 82%
- Gemeindesteuer: einfache Steuer x 60%
- No Kirchensteuer
- Total: significantly lower than Zurich (Zug is known for very low rates)

### Example 3 — PostFinance (Bern, Inter-Cantonal PE)

**Bank:** PostFinance
**Client:** Sophie Gerber, freelance architect, lives in Bern, studio in Zurich

Total income: CHF 200,000. CHF 120,000 attributable to Zurich PE, CHF 80,000 to Bern.

Steuerausscheidung required:
- Zurich taxes CHF 120,000 at the rate applicable to CHF 200,000 (Progressionsvorbehalt)
- Bern taxes CHF 80,000 at the rate applicable to CHF 200,000 (Progressionsvorbehalt)
- Federal tax allocated proportionally

Flag for Treuhaender: allocation methodology must be documented.

### Example 4 — UBS (Schwyz/Wollerau, Low-Tax Municipality)

**Bank:** UBS
**Client:** Daniel Meier, IT consultant, Wollerau (SZ)

Wollerau total Steuerfuss: ~90%. Schwyz cantonal base tariff with Wollerau multiplier.
Total effective rate may be less than half of Zurich city.
This is legitimate — municipalities compete on Steuerfuss.

### Example 5 — BCGE (Geneva, Centimes System)

**Bank:** BCGE (Banque Cantonale de Geneve)
**Client:** Marie Dupont, consultant, Geneva

Geneva uses centimes additionnels, not the multiplier system. Cantonal rate applied directly; communal rate as percentage of cantonal tax. Different computation mechanics — verify with Geneva tax calculator (ge.ch/impots).

### Example 6 — BCV (Lausanne, Church Exit Mid-Year)

**Bank:** BCV (Banque Cantonale Vaudoise)
**Client:** Pierre Blanc, Lausanne, exits Reformed church 1 April 2025

Most cantons prorate: church tax Jan-March only.
Some cantons: exit effective following year.
Verify Vaud-specific church tax proration rules.

Saving: ~10% of einfache Steuer for remaining 9 months.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-CH-1 — Only 31 December residence canton taxes the full year**
For Praenumerando cantons (most cantons since 2003), the canton where the taxpayer resides on 31 December is the sole tax canton for the entire year. A mid-year move means the new canton taxes all income.

**T1-CH-2 — NEVER compute einfache Steuer manually**
Always use official cantonal tariff tables or the ESTV calculator. The base tariffs are complex progressive schedules that vary by canton and marital status.

**T1-CH-3 — AHV/IV/EO and BVG are always fully deductible**
Social security contributions (AHV/IV/EO) and pension fund contributions (BVG, Pillar 2) are deductible at both federal and cantonal level. Apply without escalating.

**T1-CH-4 — Cantonal deductions differ from federal**
Kinderabzug, Versicherungsabzug, and other personal deductions have different amounts at cantonal vs federal level. The cantonal amounts are often higher. Use the correct deduction for each level.

**T1-CH-5 — Church tax only applies to church members**
Only members of recognised churches (Evangelisch-Reformiert, Romisch-Katholisch, Christkatholisch, and in some cantons Jewish communities) pay Kirchensteuer. Confirm membership before applying.

**T1-CH-6 — Saeule 3a cap: CHF 35,280 (self-employed without BVG) or CHF 7,056 (with BVG)**
The Pillar 3a contribution limit depends on whether the taxpayer has BVG coverage. Self-employed without BVG can contribute up to 20% of net income, capped at CHF 35,280. With BVG: CHF 7,056.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-CH-1 | Inter-cantonal Steuerausscheidung | Complex allocation of income between cantons; Doppelbesteuerungsverbot | Flag for Treuhaender — document allocation methodology |
| T2-CH-2 | Cantonal-specific deduction amounts | Each canton sets own Kinderabzug, Versicherungsabzug, etc. | Verify with cantonal Steuerverwaltung before applying |
| T2-CH-3 | Basel-Stadt or Geneva computation | Different mechanics from standard multiplier system | Use canton-specific calculator; do not apply generic formula |
| T2-CH-4 | Married couple dual-income (Zweiverdienerabzug) | Available in some cantons; mitigates marriage penalty | Check cantonal availability and limits |
| T2-CH-5 | Wealth tax (Vermogenssteuer) | Separate tax on net assets; filed on same return | Flag — separate computation required; out of scope |
| T2-CH-6 | Quellensteuer for foreign nationals without C permit | Different tax regime entirely | Escalate — this skill does not cover Quellensteuer |

---

## Section 7 — Excel Working Paper Template

```
SWISS CANTONAL/COMMUNAL TAX WORKING PAPER (SELF-EMPLOYED)
Taxpayer: _______________  AHV-Nr: _______________  FY: 2025
Canton: _______________  Municipality: _______________

SECTION A — SELF-EMPLOYMENT INCOME
                                        CHF
Gross self-employment income:          ___________
Less: Geschaeftsaufwand:               ___________
Net self-employment income:            ___________

SECTION B — DEDUCTIONS
AHV/IV/EO contributions:              ___________
BVG (Pillar 2) contributions:         ___________
Saeule 3a (Pillar 3a):                ___________
Cantonal Kinderabzug (per child):      ___________
Cantonal Versicherungsabzug:           ___________
Other cantonal deductions:             ___________
TOTAL DEDUCTIONS                       ___________

SECTION C — STEUERBARES EINKOMMEN
                                        CHF
Cantonal:                              ___________
Federal:                               ___________

SECTION D — TAX COMPUTATION
Einfache Steuer (cantonal tariff):     ___________
Kantonssteuer (x Steuerfuss ____%):    ___________
Gemeindesteuer (x Steuerfuss ____%):   ___________
Kirchensteuer (x Steuerfuss ____%):    ___________
Total cantonal/communal:               ___________
Direkte Bundessteuer:                  ___________
TOTAL INCOME TAX                       ___________

SECTION E — PROVISIONAL PAYMENTS
Vorauszahlungen paid:                  ___________
Remaining balance due / (overpayment): ___________

SECTION F — REVIEWER FLAGS
[ ] Canton and municipality confirmed?
[ ] Current year Steuerfuss verified?
[ ] Church membership confirmed?
[ ] Cantonal deductions used (not federal)?
[ ] Einfache Steuer from official tariff table?
[ ] Inter-cantonal allocation checked (if multi-canton)?
[ ] Saeule 3a within cap (CHF 7,056 or CHF 35,280)?
[ ] Vermogenssteuer (wealth tax) obligation assessed?
[ ] 31 December residence rule applied for mid-year moves?
[ ] Provisional payments reconciled?
```

---

## Section 8 — Bank Statement Reading Guide

### UBS
- Export: CSV/Excel from UBS e-Banking / UBS key4
- Columns: `Datum;Text;Belastung;Gutschrift;Saldo`
- Amount format: apostrophe thousands, period decimal (e.g., `12'500.00`)
- Date: DD.MM.YYYY
- Credits: `GUTSCHRIFT [sender]`, `EINGANG [sender]`

### ZKB (Zurcher Kantonalbank)
- Export: CSV from ZKB eBanking
- Same Swiss format as UBS
- Credits: `GUTSCHRIFT [sender]`, `VERGUTUNG [sender]`

### Raiffeisen
- Export: CSV from Raiffeisen e-Banking
- Standard Swiss format
- Credits: `EINZAHLUNG [sender]`, `GUTSCHRIFT [sender]`

### PostFinance
- Export: CSV/XML from PostFinance e-Finance
- Columns: `Buchungsdatum;Text;Gutschrift;Lastschrift;Saldo`
- Credits: `GUTSCHRIFT [sender]`

### Credit Suisse (now UBS)
- Export: CSV from CS Direct / migrated to UBS
- Standard Swiss format

### Cantonal Banks (BCGE, BCV, BLKB, LUKB, SGKB, etc.)
- Export varies; typically CSV with Swiss format
- Each cantonal bank serves its region; narration language matches canton (DE/FR/IT)

### TWINT
- Not a bank — TWINT payments appear in primary bank statement
- Look for: `TWINT EINGANG [sender]`, `TWINT GUTSCHRIFT`
- Increasingly used for small business payments

### QR-Rechnung (QR-Bill)
- Swiss standard payment slip; receipts appear as `QR-RECHNUNG EINGANG`
- Reference number allows matching to invoices

### Key Swiss Banking Notes
- Amounts in CHF; apostrophe as thousands separator (e.g., `12'500.00`), period decimal
- German-speaking cantons: `Gutschrift`, `Belastung`
- French-speaking cantons: `Credit`, `Debit`, `Versement`
- Italian-speaking cantons: `Accredito`, `Addebito`
- Swiss banks are multilingual; narration language may vary

---

## Section 9 — Onboarding Fallback

**Canton and municipality:**
> "To compute your Swiss cantonal and communal tax, I need to know your exact canton and municipality (Gemeinde) of residence. The Steuerfuss (tax multiplier) varies enormously between municipalities — for example, Zurich city has a combined multiplier of ~230%, while Wollerau (SZ) is ~90%. Where do you live as of 31 December of the tax year?"

**Church membership:**
> "Are you a member of a recognised church in Switzerland (Evangelisch-Reformierte, Romisch-Katholische, or Christkatholische Kirche)? Church members pay Kirchensteuer, typically 5-15% of the einfache Steuer. If you have formally exited (Kirchenaustritt), no church tax applies. This can significantly reduce your total tax burden."

**Steuerfuss verification:**
> "The municipal and cantonal Steuerfuss can change each year. I will use the most recently published values, but please confirm by checking with your Gemeinde or at the ESTV calculator (swisstaxcalculator.estv.admin.ch). Small changes in Steuerfuss can affect your tax by hundreds or thousands of francs."

**Inter-cantonal activity:**
> "Do you conduct business activities in a canton other than your residence, or do you own real property in another canton? If so, an inter-cantonal Steuerausscheidung (tax allocation) is required to determine which canton taxes which portion of your income. This is a complex area that typically requires a Treuhaender."

---

## Section 10 — Reference Material

### Key Legislation
- **StHG (SR 642.14)** — Federal Tax Harmonisation Act (Steuerharmonisierungsgesetz)
- **DBG (SR 642.11)** — Federal Direct Tax Act (for federal tax; companion to cantonal)
- **Individual cantonal Steuergesetze** — each of 26 cantons has its own tax law
- **BGE (Federal Supreme Court)** — rulings on inter-cantonal allocation and Doppelbesteuerungsverbot
- **Bundesverfassung Art. 127 Abs. 3** — prohibition of double taxation between cantons

### Filing Deadlines

| Canton | Standard Deadline | Extension |
|---|---|---|
| Most cantons | 31 March following year | Yes — typically to 30 September or 30 November |
| Zurich (ZH) | 31 March | Online Fristverlaengerung |
| Bern (BE) | 15 March | Extension available |
| Geneva (GE) | 31 March | Extension available |
| Vaud (VD) | 15 March | Extension available |
| Ticino (TI) | 30 April | Extension available |

### Provisional Payments
- Most cantons issue provisional tax invoices based on prior year
- 9-12 monthly or 3-4 quarterly instalments
- Overpayment: Vergutungszins (credit interest) ~0-1%
- Underpayment: Verzugszins (arrears interest) ~3-5%

### Where to Find Current Steuerfuss
- ESTV tax calculator: swisstaxcalculator.estv.admin.ch
- SSK cantonal comparison: www.steuerkonferenz.ch
- Individual cantonal portals (ZH: steuern.zh.ch, BE: taxme.ch, GE: ge.ch/impots)

### Record Keeping
- Steuererklarung and Beilagen: 10 years
- Business records (Buchfuhrung): 10 years (OR Art. 958f)
- Church exit documentation: retain permanently


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
