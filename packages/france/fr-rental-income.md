---
name: fr-rental-income
description: "French rental income taxation: revenus fonciers, LMNP, LMP, and SCI à l'IR. Trigger on phrases like \"revenus fonciers\", \"location nue\", \"location meublée\", \"LMNP\", \"LMP\", \"meublé de tourisme\", \"micro-foncier\", \"régime réel foncier\", \"déficit foncier\", \"micro-BIC location\", \"amortissement LMNP\", \"SCI à l'IR\", \"SCI transparence fiscale\", \"Airbnb France impôts\", \"déclaration 2044\", \"déclaration 2031\", \"liasse BIC meublé\", \"charges déductibles location\", \"travaux déductibles foncier\", \"bascule LMP LMNP\", \"loi Le Meur meublé tourisme\", \"location saisonnière fiscalité\", \"déficit imputable revenu global\". Covers bare rental (micro-foncier and réel), furnished rental (LMNP micro-BIC and réel with amortisation), LMP status, SCI à l'IR, and déficit foncier rules."
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FR Rental Income

## France — Rental Income (Revenus Fonciers, LMNP, SCI) v1.0

> **Based on work by [Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable or avocat fiscaliste before filing. Get this reviewed at **openaccountants.com**.

## Section 1 — Quick Reference

**Quick Reference**

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | France |
| Taxes covered | IR on rental income, prélèvements sociaux |
| Currency | EUR only |
| Tax year | Calendar year |
| Key forms | 2042 (case 4BE), 2044, 2044-SPE, 2042-C-PRO, 2031, 2033, 2072 |
| Primary legislation | art. 14–33 quater CGI (fonciers), art. 35-I-5° bis CGI (LMNP), art. 155-IV CGI (LMP), art. 8 CGI (SCI) |

## Section 2 — Fundamental Distinction

**Fundamental Distinction**

| Type of rental | Tax regime | Income category |
| --- | --- | --- |
| Bare / unfurnished (location nue) | Revenus fonciers | Revenus fonciers (micro or réel) |
| Furnished non-professional (LMNP) | **BIC** | LMNP (micro-BIC or réel) |
| Furnished professional (LMP) | **BIC** | LMP (réel obligatory) |
| SCI at IR | Revenus fonciers | Fiscal transparency |
| SCI at IS | IS | **Out of scope** — see business accounting skill |

**Classic error:** declaring furnished rental as revenus fonciers. Furnished = BIC. The tax consequences are very different (amortisation possible under réel).

## Section 3 — Bare Rental (Location Nue) — Revenus Fonciers

### 3.1 Micro-foncier (simplified regime)

**Micro-foncier parameters**

| Parameter | Value |
| --- | --- |
| Condition | Gross rental income ≤ EUR 15,000 |
| Abattement | 30% automatic |
| 2042 box | 4BE |
| Exclusions | SCI, monuments historiques, Pinel, Borloo, Malraux |

**Advantage:** simplicity, no bookkeeping required.
**Disadvantage:** no déficit possible. If actual charges > 30%, you overpay.

### 3.2 Régime réel

- **Régime réel obligatory threshold** — Obligatory above EUR 15,000 gross, or on irrevocable 3-year option.

**Deductible charges**

| Charge | Deductible? | Notes |
| --- | --- | --- |
| Mortgage interest (intérêts d'emprunt) | Yes — foncier income only | Never against global income |
| Maintenance / repair works (travaux d'entretien) | Yes | Not construction, not extension |
| Improvement works (travaux d'amélioration) | Yes |  |
| Taxe foncière | Yes | Exclude TEOM (recoverable from tenant) |
| Insurance premiums (PNO, GLI) | Yes |  |
| Management fees (agency, syndic non-recoverable) | Yes |  |
| Provisions for co-ownership charges | Yes |  |

- **Construction/extension works not deductible** — Construction / extension / reconstruction works are NOT deductible — they only increase the acquisition cost for future capital gains computation.

### 3.3 Déficit foncier (rental loss)

**Déficit foncier rules**

| Rule | Value |
| --- | --- |
| Imputable on global income | Up to **EUR 10,700**/year |
| Energy renovation exception | Up to EUR 21,400 (temporary device) |
| Excess beyond cap | Reportable on rental income for **10 years** |
| Mortgage interest | **NEVER** imputable on global income — only on rental income |

**Optimisation strategy:** concentrate major works in one year to maximise the global income deduction.

- **Critical constraint — 3-year holding after déficit imputation** — Do not sell the property within 3 years after imputing a déficit on global income — otherwise the déficit is clawed back.

## Section 4 — Furnished Rental: LMNP (Location Meublée Non Professionnelle)

### 4.1 Micro-BIC regime

- **Post loi Le Meur reform** — Post loi Le Meur reform (Nov 2024), applicable revenus 2025 — the key distinction is now classified vs unclassified tourism.

**Micro-BIC ceilings and abattements**

| Type of furnished rental | Revenue ceiling | Abattement |
| --- | --- | --- |
| Long-term furnished (LMNP longue durée) | EUR 77,700 | 50% |
| Classified furnished tourism (meublé de tourisme classé) | EUR 77,700 | 50% |
| **Unclassified furnished tourism** | **EUR 15,000** | **30%** |

- **Régime réel obligatory above ceiling** — Above the ceilings: régime réel is obligatory.
- **2042-C-PRO boxes** — 5ND (long-term / unclassified), 5NG (classified tourism)

### 4.2 Régime réel LMNP

- **BIC result formula** — BIC result = receipts − charges − amortisation

**Amortisation schedules**

| Asset | Rate | Duration |
| --- | --- | --- |
| Building (excluding land) | 2–3%/year | 25–40 years |
| Land | Non-amortisable | — |
| Furniture / equipment | 10–20%/year | 5–10 years |
| Major works | Per useful life | Variable |

**Fiscal result** is often nil or negative thanks to amortisation → no IR on rents for years.

- **LMNP deficit rule** — LMNP deficit: NOT imputable on global income (unlike LMP). Reportable on furnished BIC income for 10 years.

### 4.3 Prélèvements sociaux on LMNP

- **PS rate on LMNP** — 18.6% % (from 2025 income, LFSS 2026)  _(L. 136-6 CSS)_

## Section 5 — LMP (Location Meublée Professionnelle)

### Conditions (cumulative)

- **LMP conditions** — 1. Furnished rental receipts > EUR 23,000 per year 2. AND furnished rental receipts > 50% of total professional income of the household (salaries + BNC + BIC + director compensation)

### Consequences of LMP status

**LMP vs LMNP consequences**

| Feature | LMP | LMNP |
| --- | --- | --- |
| Deficit imputation | On global income | Only on furnished BIC (10-year report) |
| Capital gains | Professional regime (exemption possible after 5 yrs under revenue conditions) | Private capital gains regime |
| Social contributions | TNS contributions on profit (SSI) — significant | PS only |
| IFI | Potentially exempt as professional asset | Taxable |

**Involuntary reclassification trap:** a drop in professional income (unemployment, retirement) can trigger LMP status despite unchanged rents. Monitor annually.

## Section 6 — SCI à l'IR (Real Estate Company at Income Tax)

- **Default regime** — Default regime: fiscal transparency. Income and charges flow directly to each partner's personal tax return pro rata to their shares.

**SCI at IR features**

| Feature | SCI at IR |
| --- | --- |
| Income category | Revenus fonciers (micro or réel, depending on total rental income of household) |
| Amortisation | **Not available** (unlike SCI at IS) |
| Capital gains on sale | Private real estate capital gains regime (exemption: 22 years IR / 30 years PS) |
| Typical use | Heritage transmission (démembrement, donation of shares), long-term bare rental |

**Meublé in SCI = risk of IS reclassification.** Furnished rental in an SCI exposes it to IS regime reclassification.

### SCI at IS (out of scope)

Allows amortisation but capital gains at sale are computed on net book value (after amortisation) → much heavier taxation. See business accounting skill.

## Section 7 — Forms Summary

**Forms Summary**

| Regime | Form |
| --- | --- |
| Micro-foncier | 2042 case 4BE |
| Régime réel foncier | 2044 (or 2044 spéciale) |
| Micro-BIC LMNP | 2042-C-PRO (cases 5ND, 5NG, etc.) |
| Réel LMNP / LMP | 2031 + 2033 (liasse BIC) + 2042-C-PRO |
| SCI at IR | 2072 (SCI declaration) + report on 2044 (partners) |

## Section 8 — Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Furnished vs bare unclear | Classify as bare rental (revenus fonciers — no amortisation; conservative) |
| Regime unknown | Micro (simplest; check ceiling) |
| LMP vs LMNP unclear | LMNP (no TNS contributions) |
| Déficit foncier eligibility unclear | Do not impute on global income |
| Tourism classification unclear | Unclassified (30% abattement — most conservative) |

## Section 9 — Key Legal References

**Key Legal References**

| Rule | Article |
| --- | --- |
| Revenus fonciers | art. 14 to 33 quater CGI |
| Déficit foncier | art. 156-I-3° CGI |
| LMNP | art. 35-I-5° bis CGI |
| LMP | art. 155-IV CGI |
| SCI transparency | art. 8 CGI |
| PS on LMNP (revenus du patrimoine) | art. L. 136-6 CSS |

## Footer

*OpenAccountants — open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: **openaccountants.com** | Report errors: **github.com/openaccountants/openaccountants***

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
