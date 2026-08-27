---
name: fr-capital-gains
description: French capital gains, investment income, and equity compensation tax rules. Trigger on phrases like "plus-values mobilières", "PFU", "flat tax", "prélèvement forfaitaire unique", "dividendes France", "intérêts", "revenus de capitaux mobiliers", "RCM", "PEA", "plan d'épargne en actions", "assurance-vie", "rachat assurance-vie", "abattement 40% dividendes", "option barème", "prélèvements sociaux", "RSU France", "actions gratuites", "AGA", "BSPCE", "stock-options", "PEE", "PERCO", "épargne salariale", "abondement employeur", "gain d'acquisition", "equity salarial", "PER sortie capital", "PV mobilières", "cession de titres", "compte-titres ordinaire", "CTO". Covers PFU vs barème arbitrage, dividends, interest, capital gains on securities, PEA, assurance-vie rachats, RSU/BSPCE/stock-options, PEE/PERCO, and the differentiated PS rates under LFSS 2026. For crypto see fr-crypto-tax.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FR Capital Gains

## France — Capital Gains, Investment Income & Equity Compensation v1.0

> **Based on work by [Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable or avocat fiscaliste before filing. Get this reviewed at **openaccountants.com**.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | France |
| Taxes covered | PFU (flat tax), prélèvements sociaux (PS), barème option on capital income |
| Currency | EUR only |
| Tax year | Calendar year |
| Key forms | 2042, 2042-C, 2074, 2042-IFI |
| Primary legislation | art. 200 A CGI (PFU), art. 158-3° CGI (40% abattement), art. 150-0 A CGI (PV mobilières) |

## Section 2 — PFU vs Barème: The Fundamental Arbitrage

### Default: PFU (Prélèvement Forfaitaire Unique / Flat Tax)

**Default PFU rates by income type**

| Income type | IR component | PS component (revenus 2025) | Total PFU |
| --- | --- | --- | --- |
| Dividends | 12.8% | 17.2% | **30.0%** |
| Interest (RCM) | 12.8% | 17.2% | **30.0%** |
| Capital gains on securities (PV mobilières) | 12.8% | 18.6% | **31.4%** |
| PEA gains (exit after 5 yr) | 0% (exempt) | 17.2% → 18.6% from 01/01/2026 | 17.2% or 18.6% |

### Differentiated PS rates (LFSS 2026)

**Differentiated PS rates**

| Category | Legal basis | PS on 2025 income | PS on 2026+ income | Effective PFU 2025 |
| --- | --- | --- | --- | --- |
| **Revenus du patrimoine** (capital gains, crypto, LMNP) | L. 136-6 CSS | **18.6%** | 18.6% | **31.4%** |
| **Produits de placement** (dividends, interest, PEA exit, PER capital) | L. 136-7 CSS | 17.2% | **18.6% from 01/01/2026** | 30.0% |
| **Unchanged** (AV, bare rental, SCPI, old PEL/CEL) | — | 17.2% | 17.2% | — |

- **LFSS 2026 CSG increase** — LFSS 2026 (loi n° 2025-1403, art. 12) raised CSG from 9.2% to 10.6% (PS total: 17.2% → 18.6%), with two different effective dates  _(loi n° 2025-1403, art. 12)_

### Option barème (progressive rates)

On election (global and irrevocable for the year), all capital income is taxed at the progressive IR schedule instead of 12.8%.

**Benefits of barème:**
- 40% abattement on dividends (art. 158-3° CGI)
- CSG déductible 6.8% in N+1 (economy = 6.8% × base × TMI in N+1)

**Quick guidance TMI**

| TMI | Recommendation | Reason |
| --- | --- | --- |
| 0% or 11% | Barème | Low bracket + 40% dividend abattement + deductible CSG |
| 30% | Compute both | Depends on composition (dividends vs interest vs gains) |
| 41% or 45% | PFU | Flat 12.8% < 41%/45% bracket |

- **Critical rule on barème option** — the barème option is global (all capital income for the year) and irrevocable. Never recommend without checking the full composition.

### Worked comparison — Single, TMI 30%, EUR 10,000 dividends (2025)

**Under PFU (dividends = produits de placement, PS 17.2%):**

**PFU calculation**

| Component | Amount |
| --- | --- |
| IR: 10,000 × 12.8% | 1,280 |
| PS: 10,000 × 17.2% | 1,720 |
| **Total** | **3,000** |

**Under barème:**

**Barème calculation**

| Component | Amount |
| --- | --- |
| Taxable base: 10,000 × (1 − 40%) | 6,000 |
| IR: 6,000 × 30% | 1,800 |
| PS: 10,000 × 17.2% | 1,720 |
| CSG déductible N+1: 10,000 × 6.8% × 30% | −204 |
| **Net total** | **3,316** |

→ PFU more favourable (EUR 3,000 < EUR 3,316) despite the 40% abattement.

## Section 3 — Types of Capital Income

### Dividends (case 2DC)

- **Dividends PFU/barème rules** — Default PFU 30% (2025); rising to 31.4% from dividends received in 2026. Option barème: 40% abattement + progressive IR + PS. Foreign dividends: may carry withholding tax from source country — credit under tax treaty

### Interest / RCM (case 2TR)

- **Interest / RCM rules** — Bonds, crowdfunding interest, taxable savings accounts, term deposits. PFU or barème on option. No abattement (unlike dividends). Crowdfunding immobilier: taxed as RCM, not rental income. Livrets réglementés (Livret A, LDDS, LEP): fully exempt from IR and PS

### Capital gains on securities (case 3VG)

- **Capital gains on securities rules** — Net gain on sale of shares, partnership interests, UCITS. PFU or barème on option. Holding period abattements: only for shares acquired before 2018 AND barème option. Director retirement abattement: EUR 500,000 lump sum under strict conditions

## Section 4 — PEA (Plan d'Épargne en Actions)

### Contribution ceilings

**PEA contribution ceilings**

| Plan | Ceiling |
| --- | --- |
| PEA classique | EUR 150,000 |
| PEA-PME | Combined PEA + PEA-PME ≤ EUR 225,000 |
| PEA jeune (adult child attached to household) | EUR 20,000 |

- **Ceiling application** — Ceilings apply to contributions, not plan value. A plan can exceed EUR 150,000 through gains.

### Tax treatment by plan age

**Tax treatment by plan age (PEA)**

| Plan age | Withdrawal effect | IR | PS |
| --- | --- | --- | --- |
| < 5 years | **Closure** of plan | PFU 12.8% (or barème) | 17.2% |
| ≥ 5 years | Free withdrawals, no closure | **Exempt** | 17.2% (→ 18.6% from 01/01/2026) |

- **PEA exemption after 5 years** — After 5 years: total IR exemption on gains. Only PS are due at each withdrawal. PS from 01/01/2026: 18.6% on total gain at withdrawal (including gain accrued before 2026). PEA gains are "produits de placement" (L. 136-7 CSS).  _(L. 136-7 CSS)_
- **Eligible/non-eligible PEA assets** — Eligible assets: European equities (EU + EEA), UCITS with ≥75% European equities, eligible European ETFs. Non-eligible: US/Asian stocks, bonds, gold, crypto.

## Section 5 — Assurance-Vie (Life Insurance) — Taxation of Withdrawals (Rachats)

### Proportionality principle

- **Taxable gain portion on partial withdrawal** — taxable_gain_portion = (total_gains / total_contract_value) × withdrawal_amount
- **Proportionality rule** — A partial withdrawal does not extract only non-taxable capital. It extracts a proportional fraction of gains and capital.

### Annual abattement after 8 years

**Annual abattement after 8 years**

| Situation | Annual abattement |
| --- | --- |
| Single, widowed, divorced | EUR 4,600 |
| Couple (joint filing) | EUR 9,200 |

- **8-year abattement condition** — Condition: 8 years of contract age (not contribution age). Renewable each calendar year.

### Tax rates by contribution date

**Contributions after 27 September 2017:**

**Tax rates by contribution date (post-2017)**

| Situation | Rate |
| --- | --- |
| Contract < 8 years | PFU 30% (12.8% IR + 17.2% PS) |
| Contract ≥ 8 years, total contributions < EUR 150,000 | 24.7% (7.5% IR + 17.2% PS) after abattement |
| Contract ≥ 8 years, total contributions ≥ EUR 150,000 | 30% on fraction above EUR 150,000 of **net contributions** |

- **150k threshold household basis** — The EUR 150,000 threshold is assessed across all AV contracts of the household.
- **Contributions before 27 September 2017** — Degressive PFL rates (35% / 15% / 7.5%) by contract age.
- **PS rate on AV unchanged** — PS rate on AV: 17.2% unchanged (excluded from LFSS 2026 increase).

### Strategy: optimised withdrawals after 8 years

Spread withdrawals to stay within the annual abattement (EUR 9,200 couple). Example: need EUR 50,000 over 5 years → EUR 10,000/year optimises the abattement if gain portion ≤ abattement per withdrawal.

## Section 6 — RSU / AGA (Restricted Stock Units / Actions Gratuites)

### Two distinct taxable events

**1. Gain d'acquisition (at vesting)**

| Attribute | Detail |
| --- | --- |
| Nature | **Salary income** (traitements et salaires) |
| 2042 box | 1TT / 1UT |
| Tax | Progressive IR schedule (after 10% salary abattement on total salaries) |
| Social contributions | CSG/CRDS 9.7% + salarial contribution 10% (qualifying plans, within caps) |

### Two distinct taxable events

**2. Plus-value de cession (at sale)**  _(L. 136-6 CSS)_

| Attribute | Detail |
| --- | --- |
| Nature | PV mobilière |
| Tax | PFU **31.4%** for disposals from 2025 (12.8% IR + 18.6% PS) or barème on option |
| Qualification | "Revenus du patrimoine" (L. 136-6 CSS) → PS 18.6% from 2025 |

- **Classic trap and strategy for RSU** — Classic trap: treating the acquisition gain as a standard capital gain. It is first and foremost salary (barème), subject to CSG 9.7% and salarial contribution 10%. Only the subsequent appreciation (vesting value → sale price) is a capital gain. Strategy: for massive vesting (> 1.5× annual salary), consider the quotient pour revenus exceptionnels (coefficient 4) to smooth across brackets. Useless if already at TMI 45%.

## Section 7 — BSPCE (Bons de Souscription de Parts de Créateur d'Entreprise)

**Key difference vs RSU:** no acquisition gain taxed as salary. The gain is only realised and taxed **at sale** of the underlying shares.

### Tax rate on disposal gain

**Tax rate on disposal gain by tenure**

| Tenure in the company at sale date | Total rate (2025 disposals) |
| --- | --- |
| **≥ 3 years** | **31.4%** (12.8% IR + 18.6% PS — PV mobilière) |
| **< 3 years** | **50%** (30% IR + 20% PS — specific salarial contribution) |

- **Early departure penalty** — Early departure penalty (< 3 years) is severe. Factor into departure decisions.

### Issuing company eligibility

- **BSPCE issuing company eligibility criteria** — SA or SAS incorporated in France; Registered < 15 years; Unlisted or listed on SME compartment; Subject to IS; Capital ≥ 25% held by natural persons; No restructuring history (merger, demerger, takeover). If conditions not met: requalification as salary → progressive IR + full social contributions.

## Section 8 — Stock-Options

**Stock-option regime by plan period**

| Plan period | Regime |
| --- | --- |
| Before 2012 | Favourable specific schedule (by holding period) |
| 2012–2016 | Salary (IR barème + specific social contributions) |
| After 2017 | Salary (barème) + salarial contribution 10% on qualifying plans |

- **Excess discount rule** — Excess discount (rabais excédentaire): difference between market price at grant and exercise price, above 5% → taxed as salary at exercise. Always consult the plan to determine the applicable regime.

## Section 9 — PEE / PERCO / Employee Savings

### PEE (Plan d'Épargne Entreprise)

**PEE features**

| Feature | Detail |
| --- | --- |
| Employer match (abondement) | IR-exempt + PS-exempt within caps |
| Match cap | ~EUR 3,709 per beneficiary (8% PASS — verify annually) |
| Lock-up | 5 years (early exit for marriage, 3rd child birth, home purchase, job loss, etc.) |
| Exit after 5 years | **IR-exempt**, only PS 17.2% on gains |

### PERCO / PERO (Company PER)

**PERCO/PERO features**

| Feature | Detail |
| --- | --- |
| Exit | At retirement — annuity or lump sum |
| Tax at exit | Same as individual PER (contributions at barème, gains at PFU) |
| Match cap | ~EUR 7,418 (distinct from PEE cap) |

### Priority rule

**Priority order for employee savings envelopes**

| Priority | Envelope | Why |
| --- | --- | --- |
| 1st | PEE + employer match | Match = 50–300% instant return — unbeatable |
| 2nd | PERCO/PERO + employer match | Same logic, retirement lock |
| 3rd | Individual PER | Only TMI deduction, no match |

- **Golden rule on employer match priority** — never contribute to an individual PER before saturating the employer match on PEE + PERCO. The match is free money.

## Section 10 — PER Sortie en Capital (Exit Taxation)

**PER lump sum exit taxation**

| Component | Tax treatment |
| --- | --- |
| **Contributions (previously deducted)** | Progressive IR schedule (barème) — treated as income |
| **Investment gains** | PFU: 12.8% IR + PS (17.2% before 01/01/2026; 18.6% from 01/01/2026) |

- **PER gains classification and trap** — PER gains are "produits de placement" (L. 136-7 CSS). Trap: a lump-sum exit on contributions at TMI 45% is nearly neutral — same tax as a normal income year. Fractionate the exit over multiple years if possible.  _(L. 136-7 CSS)_

## Section 11 — Conservative Defaults

**Conservative default assumptions**

| Ambiguity | Default |
| --- | --- |
| PFU vs barème unclear | Apply PFU (simpler, no global commitment) |
| RSU gain classification unclear | Treat as salary (acquisition gain) |
| BSPCE tenure unclear | Assume < 3 years (50% rate — conservative) |
| PEA age unclear | Assume < 5 years (taxable) |
| AV abattement eligibility unclear | No abattement applied |
| PS rate unclear for 2025 income | Apply 18.6% for PV mobilières, 17.2% for dividends/interest |

## Section 12 — Key Legal References

**Key legal references table**

| Rule | Article |
| --- | --- |
| PFU | art. 200 A CGI |
| Option barème | art. 200 A-2 CGI |
| Dividend 40% abattement | art. 158-3° CGI |
| Capital gains on securities | art. 150-0 A to 150-0 D CGI |
| Prélèvements sociaux | art. L. 136-1 et seq. CSS |
| PS differentiation (patrimoine vs placement) | art. L. 136-6 and L. 136-7 CSS |
| LFSS 2026 CSG increase | loi n° 2025-1403, art. 12 |
| RSU / AGA | art. 80 quaterdecies CGI |
| BSPCE | art. 163 bis G CGI |
| Stock-options | art. 80 bis CGI |
| PEA | art. 163 quinquies D CGI, art. L. 221-30 CMF |
| Assurance-vie rachats | art. 125-0 A CGI |
| AV abattement | art. 125-0 A-I-2° CGI |
| AV 150k threshold | art. 125-0 A-I-2° bis CGI |
| PEE | art. L. 3332-1 et seq. Code du travail |

## Footer disclaimers

*OpenAccountants — open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: **openaccountants.com** | Report errors: **github.com/openaccountants/openaccountants***

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
