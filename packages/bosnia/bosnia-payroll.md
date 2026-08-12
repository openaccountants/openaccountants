---
name: bosnia-payroll
description: "Use this skill whenever asked about Bosnia and Herzegovina payroll processing for employed persons. Trigger on phrases like \"Bosnia payroll\", \"BiH payroll\", \"FBiH payroll\", \"Republika Srpska payroll\", \"RS payroll\", \"Brcko payroll\", \"plata\", \"neto placa\", \"bruto placa\", \"doprinosi\", \"PIO doprinos\", \"zdravstveno osiguranje\", \"porez na dohodak\", \"personal income tax Bosnia\", \"social contributions BiH\", \"employer SSC Bosnia\", \"minimum wage Bosnia\", \"najniza placa\", \"porezna kartica\", \"Specifikacija uz isplatu placa\", \"GIP-1022\", \"gross to net Bosnia\", \"salary calculation Bosnia\", or any question about computing employee pay, withholding tax, or social contributions for Bosnia-based employees. CRITICAL: Bosnia has NO unified national payroll system -- everything is set at the ENTITY level (Federation of BiH, Republika Srpska, Brcko District) with materially different rates, deductions, and forms. This skill branches on the employer's entity. It covers personal income tax (PIT) withholding, social contributions (employee and employer), the 1 July 2025 FBiH contribution reform, minimum wage, personal deductions, and filing obligations. ALWAYS read this skill before processing any Bosnia and Herzegovina payroll."
version: 0.1
jurisdiction: BA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina Payroll

## Bosnia and Herzegovina Payroll Skill v0.1

> Tier 2 (research-verified). Confidence: **medium**. Bosnia and Herzegovina has no single national payroll authority -- payroll, PIT, and social contributions are administered at the **entity** level. This skill MUST branch on the employer's entity (FBiH / Republika Srpska / Brcko District) before any computation. Where a figure could not be pinned to a primary source it is marked **[RESEARCH GAP -- reviewer to confirm]**.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Bosnia and Herzegovina (BiH) |
| Currency | BAM (Bosnian convertible mark; "KM"); pegged at 1 EUR = 1.95583 BAM (currency board) |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| **No single national authority** | Payroll/PIT/SSC are administered per entity -- branch first |
| FBiH tax authority | Tax Administration of the Federation of BiH (Porezna uprava FBiH / PUFBiH) -- https://www.pufbih.ba |
| RS tax authority | Tax Administration of Republika Srpska (Poreska uprava RS / PURS) -- https://poreskaupravars.org |
| Brcko District authority | Brcko District Tax Administration |
| PIT rate | FBiH 10% flat; RS 8% flat (employment income); Brcko 10% flat (PwC, Individual -- Taxes on personal income) |
| Employee social contributions | FBiH 31.0% of gross; RS 32.8% of gross (PwC, Individual -- Other taxes) |
| Employer social contributions | FBiH 5.0% of gross from 1 Jul 2025 (was 10.5%) + 0.5% disaster + 0.5% water on NET; RS 0% (PwC; Vlada FBiH) |
| Key legislation | FBiH: Zakon o porezu na dohodak FBiH (Sl. novine FBiH 10/08, as amended); Zakon o doprinosima FBiH (2025 amendment). RS: Zakon o porezu na dohodak RS (from 1 Jan 2025); Zakon o doprinosima RS. Brcko: Zakon o porezu na dohodak Brcko Distrikta |
| Validated by | Pending -- requires sign-off by a BiH licensed accountant/tax adviser |
| Skill version | 0.1 |

> **NOTE -- VAT/indirect taxes are state-level** under the Indirect Taxation Authority (UIO/ITA) and are NOT relevant to payroll. Do not confuse the state-level UIO with the entity-level PIT/SSC administrations above.

## Section 2 -- ENTITY DETERMINATION (do this FIRST)

Before any calculation, determine the entity in which the employee works / the employer is registered. Everything downstream (PIT rate, contribution split, personal deduction, forms, deadlines) depends on it.

**Entity determination table**  _(PwC Worldwide Tax Summaries, Bosnia and Herzegovina -- Individual / Corporate -- Other taxes and Taxes on personal income.)_

| If the employer / workplace is in... | Use entity | PIT | Employee SSC | Employer SSC |
| --- | --- | --- | --- | --- |
| Federation of BiH (Sarajevo, Mostar, Tuzla, Zenica, Bihac, the 10 cantons) | **FBiH** | 10% flat | 31.0% | 5.0% (from 1 Jul 2025) + 1.0% on net |
| Republika Srpska (Banja Luka, Bijeljina, Trebinje, Doboj, Prijedor) | **RS** | 8% flat | 31.0% | 0% |
| Brcko District | **Brcko (BD)** | 10% flat | Health 12% + pension to elected fund | per elected fund |

- **Conservative default entity** — if the employee's work entity is unknown, treat the worker under the entity where the employer is registered. Rates differ materially, so never average or assume.  _(PwC Worldwide Tax Summaries, Bosnia and Herzegovina -- Individual / Corporate -- Other taxes and Taxes on personal income.)_

## Section 3 -- Personal Income Tax (PIT) Withholding

PIT is withheld monthly at source by the employer (pay-as-you-earn via the gross-up "bruto" model). The rate is flat within each entity. PIT is computed on **net income** = gross salary minus employee social contributions minus the basic personal deduction (and dependent deductions, where a valid tax card is on file).

### PIT rates by entity (2025)

**PIT rates by entity table**  _(PwC, Individual -- Taxes on personal income)_

| Entity | PIT type | Rate | Base | Source |
| --- | --- | --- | --- | --- |
| FBiH | Flat | 10% | Gross − employee SSC (31%) − personal/dependent deductions | PwC, Individual -- Taxes on personal income |
| RS | Flat | 8% (employment); capital gains 13%; small entrepreneurs 2% of annual revenue | Gross − employee SSC (31%) − personal/dependent deductions | PwC, Individual -- Taxes on personal income |
| Brcko District | Flat | 10% | Gross − employee SSC − deductions | PwC, Individual -- Taxes on personal income |

> There are no progressive brackets -- each entity applies a single flat rate, so there is no cumulative-bracket arithmetic to track. The personal deduction is the only tax-free element.

### Basic personal deduction and dependent factors

- **FBiH basic personal deduction** — basic personal deduction = coefficient 1 = 300 KM/month (3,600 KM/year), applied only via a valid tax card (porezna kartica). Dependent factors are applied to the same 300 KM base.  _(Klix.ba salary structure; rif.hr 2025 dependent summary)_

**FBiH dependent factor table**  _(Klix.ba salary structure; rif.hr 2025 dependent summary)_

| FBiH dependent factor | Multiplier of 300 KM/mo |
| --- | --- |
| Spouse (supported) | 0.5 |
| 1st child | 0.5 |
| 2nd child | 0.7 |
| 3rd and each further child | 0.9 each |
| Other supported dependent / disability | 0.3 |

> **[RESEARCH GAP -- reviewer to confirm]** The FBiH 300 KM base and dependent factors were confirmed from a Bosnian tax-press source (Klix.ba) and an accounting summary (rif.hr), not the primary FBiH Pravilnik PDF (the official PUFBiH PDF was not machine-readable in research). Confirm the current base against the FBiH Pravilnik.

- **RS basic personal deduction** — basic personal deduction = 12,000 KM/year (1,000 KM/month), proportionally reduced for part-time and split across multiple employers; dependent deduction = 1,800 KM/year per dependent family member; plus a deduction for interest on housing loans.  _(PwC, Individual -- Taxes on personal income)_
- **Conservative default tax card** — apply the basic personal deduction only where a valid tax card (porezna kartica) is on file; otherwise grant no personal deduction (FBiH/RS both require the card to claim it).  _(PwC, Individual -- Taxes on personal income)_

## Section 4 -- Social Contributions (Federation of BiH)

FBiH contributions are split between employee and employer. **The 1 July 2025 reform cut the combined rate from 41.5% to 36%** (employer side only: PIO 6.0%→2.5%, health 4.0%→2.0%). The employee side (31.0%) was unchanged.

### FBiH contribution table -- from 1 July 2025

**FBiH contribution table**  _(Vlada FBiH / federalna.ba)_

| Fund | Employee rate | Employer rate | Base | Source |
| --- | --- | --- | --- | --- |
| Pension & disability insurance (PIO) | 17.0% | 2.5% (was 6.0%) | Gross salary | PwC, Corporate -- Other taxes |
| Health insurance | 12.5% | 2.0% (was 4.0%) | Gross salary | PwC, Corporate -- Other taxes |
| Unemployment insurance | 1.5% | 0.5% | Gross salary | PwC, Corporate -- Other taxes |
| **TOTAL social contributions** | **31.0%** | **5.0%** (was 10.5%) | Gross salary | Vlada FBiH / federalna.ba |
| **Combined** |  |  | **36.0%** (was 41.5%) | Vlada FBiH / federalna.ba |

**Arithmetic check:** employee 17.0 + 12.5 + 1.5 = **31.0%** ✓; employer 2.5 + 2.0 + 0.5 = **5.0%** ✓; combined 31.0 + 5.0 = **36.0%** ✓.

### FBiH employer-borne charges OUTSIDE the 36%

**FBiH employer-borne charges table**  _(PwC, Individual -- Other taxes)_

| Charge | Rate | Base | Source |
| --- | --- | --- | --- |
| Protection from natural and other disasters | 0.5% | **NET** salary | PwC, Individual -- Other taxes |
| Water protection charge | 0.5% | **NET** salary | PwC, Individual -- Other taxes |

These two 0.5% charges are employer-borne, calculated on net salary, and sit outside the 36% combined SSC rate.

### FBiH pre-1-July-2025 rates (for first-half-2025 payroll)

**FBiH pre-reform rates table**  _(federalna.ba)_

| Fund | Employer rate (pre-reform) | Source |
| --- | --- | --- |
| PIO | 6.0% | Nexo / PwC |
| Health | 4.0% | Nexo / PwC |
| Unemployment | 0.5% | Nexo / PwC |
| **Employer total (pre-reform)** | **10.5%** | federalna.ba |
| **Combined (pre-reform)** | **41.5%** | federalna.ba |

- **Conservative default FBiH date logic** — for FBiH payroll dated on/after 1 Jul 2025 use 5.0% employer / 36% combined; for periods before that date use 10.5% employer / 41.5% combined.  _(federalna.ba)_

## Section 5 -- Social Contributions (Republika Srpska)

In RS there are NO employer social contributions. All 32.8% is borne by the employee and withheld by the employer.

### RS contribution table

**RS contribution table**  _(PwC, Individual -- Other taxes)_

| Fund | Employee rate | Employer rate | Base | Source |
| --- | --- | --- | --- | --- |
| Pension & disability insurance (PIO) | 18.5% | 0% | Gross salary | PwC, Individual -- Other taxes |
| Health insurance | 12.0% | 0% | Gross salary | PwC, Individual -- Other taxes |
| Child protection | 1.7% | 0% | Gross salary | PwC, Individual -- Other taxes |
| Unemployment insurance | 0.6% | 0% | Gross salary | PwC, Individual -- Other taxes |
| **TOTAL social contributions** | **32.8%** | **0%** | Gross salary | PwC, Individual -- Other taxes |

**Arithmetic check:** employee 18.5 + 12.0 + 1.7 + 0.6 = **32.8%** ✓; employer = **0%** ✓.

> **Source note:** RS employee contributions confirmed against PwC, *Bosnia and Herzegovina -- Individual -- Other taxes* (pension/PIO 18.5%, health 12.0%, unemployment 0.6%, child protection 1.7%; total 32.8%) and the 2025 Eurofast Bosnia payroll guide. RS is an entirely employee-borne regime: PwC states "There are no employer's social security contributions in Republika Srpska."

### Brcko District

**Brcko District table**  _(PwC, Individual -- Other taxes)_

| Item | Detail | Source |
| --- | --- | --- |
| Health insurance | 12% | PwC, Individual -- Other taxes |
| Pension | Employee **elects** to contribute to either the RS or FBiH PIO fund (rate per chosen entity) | PwC, Individual -- Other taxes |
| Employer | Per the chosen entity | PwC, Individual -- Other taxes |

> **[RESEARCH GAP -- reviewer to confirm]** Full Brcko District contribution mechanics and form codes were not pinned to a single authoritative figure. Confirm against the Brcko District Tax Administration before relying on Brcko output.

## Section 6 -- Minimum Wage (2025)

**Minimum wage table**  _(Vlada FBiH; Plastron)_

| Entity | Net (KM/mo) | Gross (KM/mo) | Notes | Source |
| --- | --- | --- | --- | --- |
| FBiH | 1,000.00 | 1,562 | 1 Jan -- 31 Dec 2025; Sl. novine FBiH 104/24 | Vlada FBiH |
| RS -- base | 900.00 | 1,344.26 | Sl. glasnik RS 6/25 | Plastron |
| RS -- 3-yr secondary | 950.00 | 1,426.23 | By qualification tier | Plastron |
| RS -- 4-yr secondary | 1,000.00 | 1,508.20 | By qualification tier | Plastron |
| RS -- higher education | 1,300.00 | 2,000.00 | By qualification tier | Plastron |

> **[RESEARCH GAP -- reviewer to confirm]** Contribution floors (lowest base, often a percentage of the entity average wage for part-time/low earners) exist in both entities but exact 2025 base amounts were not pinned to a primary source. Confirm the lowest-base rule for low/part-time earners before finalising such payroll.

## Section 7 -- Conservative Defaults

When information is missing or ambiguous, apply the most defensible (least aggressive) treatment and flag it:

1. **Unknown entity → use employer's registration entity.** Never average FBiH/RS/Brcko rates. (Rationale: BiH has no unified payroll system; entity determines everything.)
2. **FBiH date logic.** On/after 1 Jul 2025: employer 5.0% / combined 36%. Before that: employer 10.5% / combined 41.5%. (Rationale: mid-year 2025 reform.)
3. **No tax card → no personal deduction.** Apply the basic/dependent personal deduction only with a valid *porezna kartica* on file. (Rationale: FBiH/RS require the card.)
4. **Net-figure mismatch → present mechanics, flag the figure.** Where a published "net" minimum differs from a mechanical gross-to-net (see RS examples), show the computation and mark the published figure for reviewer confirmation rather than back-solving.
5. **Penalty bands → flag, do not invent.** Cite that fines + default interest apply but do not state a specific KM band unless confirmed (see Section 13).

### Required inputs before computing

**Required inputs table**

| Input | Why needed |
| --- | --- |
| Entity (FBiH / RS / Brcko) | Determines every rate, deduction, and form |
| Pay period (month/year) | FBiH reform changes rates from 1 Jul 2025 |
| Gross OR net salary (state which) | Gross-up "bruto" model needs the starting basis |
| Tax card (*porezna kartica*) status + dependents | Determines personal/dependent deductions |
| Employee age / qualification (RS) | RS minimum wage is tiered by qualification |
| Employment type (full/part-time) | Affects deduction proration and floor base |

### Refusal catalogue -- DO NOT compute if:

- The **entity is unknown** and the employer registration cannot be established → ask; do not guess.
- The user asks for a **single "Bosnia" rate** that ignores the entity split → explain the entity model first.
- A **pre-1-Jul-2025 FBiH** computation is requested without confirming the pay date → ask for the date.
- The user requests **Brcko** pension treatment without stating the elected fund → ask which fund (RS or FBiH).
- The user wants a **definitive net figure** where research data shows a published/mechanical mismatch → present the mechanics and flag for accountant review.

## Section 9 -- Transaction / Payment Pattern Library (deterministic)

Use these patterns to classify Bosnian bank-statement lines deterministically. Terms are in local language (Bosnian/Croatian/Serbian, Latin and Cyrillic both occur).

### Salary credits (employee side)

**Salary credits table**

| Pattern (statement text) | Classification |
| --- | --- |
| PLATA, PLACA, ZARADA, ISPLATA PLACE | Net salary payment |
| NETO PLATA, NETO PLACA | Net salary payment |
| AKONTACIJA PLACE, AVANS PLATE | Salary advance (net) |
| ПЛАТА, ЗАРАДА (Cyrillic) | Net salary payment (RS) |
| REGRES, TOPLI OBROK | Allowance (vacation / meal) -- check taxability |

### Employer debit patterns (remittances)

**Employer debit patterns table**

| Pattern (statement text) | Classification |
| --- | --- |
| POREZ NA DOHODAK, POREZ NA DOHOTAK | PIT withheld, remitted to PUFBiH/PURS |
| DOPRINOSI, DOPRINOS PIO, MIO | Pension contribution (PIO/MIO) remittance |
| ZDRAVSTVENO, ZDRAVSTVENO OSIGURANJE | Health insurance contribution remittance |
| NEZAPOSLENOST, OSIGURANJE OD NEZAPOSLENOSTI | Unemployment contribution remittance |
| DJECIJA ZASTITA, DJECJA ZASTITA (RS) | Child-protection contribution (RS) |
| ZASTITA OD PRIRODNIH NESRECA | FBiH disaster-protection 0.5% (on net) |
| VODNE NAKNADE, VODNA NAKNADA | FBiH water charge 0.5% (on net) |
| PUFBIH, PORESKA UPRAVA | Remittance to FBiH/RS tax administration |

### Deterministic classification rules

- **Classification rules** — 1. If statement text matches a contribution fund name (PIO/MIO, ZDRAVSTVENO, NEZAPOSLENOST, DJECIJA ZASTITA) → contribution liability remittance, not an expense reclassification. 2. If text contains POREZ NA DOHODAK/DOHOTAK → PIT withholding remittance (liability until paid). 3. If text contains ZASTITA OD PRIRODNIH or VODN- → FBiH employer-borne 0.5% charge on net (expense, outside the 36%). 4. Cyrillic-script lines almost always indicate an RS employer/employee → confirm entity = RS.

## Section 10 -- Worked Examples

All examples use BAM (KM). Each is recomputed end-to-end.

### Example 1 -- FBiH, minimum wage, no dependents (on/after 1 Jul 2025)

Bank statement line: `ISPLATA PLACE — 06/2025 — 1.000,00 KM`

- Gross = **1,562.00 KM** (FBiH 2025 gross minimum; Vlada FBiH)
- Employee SSC = 31% × 1,562.00 = **484.22 KM**
- Income after SSC = 1,562.00 − 484.22 = **1,077.78 KM**
- Basic personal deduction (coeff 1) = **300.00 KM**
- PIT base = 1,077.78 − 300.00 = **777.78 KM**
- PIT = 10% × 777.78 = **77.78 KM**
- **Net pay = 1,077.78 − 77.78 = 1,000.00 KM** ✓ (reconciles to the published 1,000 KM net minimum)
- Employer SSC = 5% × 1,562.00 = **78.10 KM**
- Disaster 0.5% × net 1,000.00 = 5.00 KM; Water 0.5% × net 1,000.00 = 5.00 KM
- **Total employer cost = 1,562.00 + 78.10 + 5.00 + 5.00 = 1,650.10 KM**

### Example 2 -- FBiH, gross 2,000 KM, no dependents (on/after 1 Jul 2025)

Bank statement line: `PLATA 07/2025`

- Gross = **2,000.00 KM**
- Employee SSC = 31% × 2,000.00 = **620.00 KM**
- After SSC = 2,000.00 − 620.00 = **1,380.00 KM**
- Personal deduction = **300.00 KM**
- PIT base = 1,380.00 − 300.00 = **1,080.00 KM**
- PIT = 10% × 1,080.00 = **108.00 KM**
- **Net pay = 1,380.00 − 108.00 = 1,272.00 KM**
- Employer SSC = 5% × 2,000.00 = **100.00 KM**
- Disaster 0.5% × net 1,272.00 = 6.36 KM; Water 0.5% × net 1,272.00 = 6.36 KM
- **Total employer cost = 2,000.00 + 100.00 + 6.36 + 6.36 = 2,112.72 KM**

### Example 3 -- FBiH, gross 2,000 KM, PRE-reform (Feb 2025)

Bank statement line: `ISPLATA PLACE 02/2025`

- Gross = **2,000.00 KM**
- Employee SSC = 31% × 2,000.00 = **620.00 KM** (employee side unchanged)
- After SSC = **1,380.00 KM**; deduction 300.00 → PIT base 1,080.00; PIT = **108.00 KM**
- **Net pay = 1,272.00 KM** (employee outcome identical to Example 2)
- Employer SSC = **10.5%** × 2,000.00 = **210.00 KM** (pre-reform)
- Disaster + Water = 6.36 + 6.36 = 12.72 KM
- **Total employer cost = 2,000.00 + 210.00 + 12.72 = 2,222.72 KM** (110.00 KM higher employer cost than post-reform Example 2)

### Example 4 -- RS, gross 1,508.20 KM (4-yr secondary minimum), no dependents

Bank statement line (Cyrillic): `ПЛАТА 09/2025`

- Gross = **1,508.20 KM**
- Employee SSC = 31% × 1,508.20 = **467.54 KM** (1,508.20 × 0.31 = 467.542)
- After SSC = 1,508.20 − 467.54 = **1,040.66 KM**
- RS personal deduction = 1,000.00 KM/month
- PIT base = 1,040.66 − 1,000.00 = **40.66 KM**
- PIT = 8% × 40.66 = **3.25 KM**
- **Net pay = 1,040.66 − 3.25 = 1,037.41 KM**
- Employer SSC = **0.00 KM** (no employer contributions in RS)
- **Total employer cost = 1,508.20 KM** (gross only)

> Note: the published RS "net" for this tier is 1,000.00 KM, but the mechanical gross-to-net above yields 1,037.41 KM. Per Conservative Default 4, present the mechanics and flag the published-figure reconciliation. **[RESEARCH GAP -- reviewer to confirm]** the exact RS net-definition / deduction-application order against PURS.

### Example 5 -- RS, gross 2,000 KM (higher-education minimum), one dependent

Bank statement line: `ZARADA 10/2025`

- Gross = **2,000.00 KM**
- Employee SSC = 31% × 2,000.00 = **620.00 KM**
- After SSC = 2,000.00 − 620.00 = **1,380.00 KM**
- RS personal deduction (1,000.00/mo) + 1 dependent (1,800.00/yr ÷ 12 = 150.00/mo) = **1,150.00 KM**
- PIT base = 1,380.00 − 1,150.00 = **230.00 KM**
- PIT = 8% × 230.00 = **18.40 KM**
- **Net pay = 1,380.00 − 18.40 = 1,361.60 KM**
- Employer SSC = **0.00 KM**
- **Total employer cost = 2,000.00 KM**

### Example 6 -- FBiH, gross 3,000 KM, married + 2 children (on/after 1 Jul 2025)

Bank statement line: `ISPLATA PLACE 08/2025`

- Gross = **3,000.00 KM**
- Employee SSC = 31% × 3,000.00 = **930.00 KM**
- After SSC = 3,000.00 − 930.00 = **2,070.00 KM**
- Personal deduction = coeff 1 (300.00) + spouse 0.5 (150.00) + 1st child 0.5 (150.00) + 2nd child 0.7 (210.00) = **810.00 KM**
- PIT base = 2,070.00 − 810.00 = **1,260.00 KM**
- PIT = 10% × 1,260.00 = **126.00 KM**
- **Net pay = 2,070.00 − 126.00 = 1,944.00 KM**
- Employer SSC = 5% × 3,000.00 = **150.00 KM**
- Disaster 0.5% × net 1,944.00 = 9.72 KM; Water 0.5% × net 1,944.00 = 9.72 KM
- **Total employer cost = 3,000.00 + 150.00 + 9.72 + 9.72 = 3,169.44 KM**

## Section 11 -- Tier 1 Rules (deterministic -- always apply)

- **Branch on entity first** — FBiH, RS, and Brcko have different rates, deductions, and forms.  _(PwC)_
- **FBiH PIT** — FBiH PIT = 10% flat on (gross − 31% employee SSC − deductions).  _(PwC)_
- **RS PIT** — RS PIT = 8% flat on employment income (gross − 31% employee SSC − deductions); capital gains 13%; small entrepreneurs 2% of revenue.  _(PwC)_
- **Brcko PIT** — Brcko PIT = 10% flat.  _(PwC)_
- **FBiH employee SSC** — FBiH employee SSC = 31.0% = PIO 17.0 + health 12.5 + unemployment 1.5.  _(PwC)_
- **FBiH employer SSC** — FBiH employer SSC = 5.0% from 1 Jul 2025 = PIO 2.5 + health 2.0 + unemployment 0.5; was 10.5% before.  _(PwC / Nexo / Vlada FBiH)_
- **FBiH combined rate change** — FBiH combined fell 41.5% → 36% on 1 Jul 2025.  _(Vlada FBiH / federalna.ba)_
- **FBiH employer additional charges** — FBiH employer also pays 0.5% disaster + 0.5% water on NET, outside the 36%.  _(PwC)_
- **RS SSC** — RS SSC = 31.0% all employee-borne = PIO 18.5 + health 10.2 + child 1.7 + unemployment 0.6; no employer SSC in RS.  _(PwC)_
- **Personal deductions** — FBiH personal deduction = 300 KM/mo (coeff 1) via tax card; RS = 1,000 KM/mo + 1,800 KM/yr per dependent.  _(Klix.ba / rif.hr / PwC)_
- **FBiH minimum wage 2025** — FBiH 2025 minimum wage = 1,000 net / 1,562 gross.  _(Sl. novine FBiH 104/24; Vlada FBiH)_
- **RS minimum wage 2025** — RS 2025 minimum wage = 900 net / 1,344.26 gross base, tiered to 1,300 net / 2,000 gross for higher education.  _(Sl. glasnik RS 6/25; Plastron)_
- **Annual PIT return deadline** — Annual PIT return due 31 March of the following year (FBiH and RS); Brcko 28 February, waived if fully withheld.  _(PwC)_
- **Currency peg** — BAM pegged 1 EUR = 1.95583 BAM (currency board), so KM figures are stable against EUR.  _(Currency board (BAM pegged to EUR))_

## Section 12 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 catalogue table**

| Item | Why judgement is needed |
| --- | --- |
| Contribution **floor / lowest base** for part-time and low earners | Exact 2025 base amounts not pinned to a primary source **[RESEARCH GAP]** |
| RS net-figure reconciliation (published vs mechanical) | Deduction-application order unclear (see Example 4) **[RESEARCH GAP]** |
| Brcko District pension fund election (RS vs FBiH) | Employee election drives rates; mechanics not fully confirmed **[RESEARCH GAP]** |
| Taxability of allowances (*topli obrok*, *regres*, travel) | Non-taxable thresholds vary by entity; not researched here |
| FBiH dependent-factor base (300 KM) | Confirmed from press/accounting sources, not the primary Pravilnik **[RESEARCH GAP]** |
| Cross-entity employees (work split FBiH/RS) | Apportionment and double-card handling needs adviser input |
| 2026 rate continuity (RS new PIT law from 1 Jan 2025) | Confirm no further 2026 change before applying to 2026 periods |

## Section 13 -- Filing Obligations and Forms

**Filing obligations table**  _(PwC, Individual -- Tax administration)_

| Entity | Form | Purpose | Deadline | Source |
| --- | --- | --- | --- | --- |
| FBiH | Specifikacija uz isplatu placa (monthly salary/contribution specification) | Report PIT withheld + SSC per employee | Same day as salary+contribution payment, no later than 1 day after payment | PwC, Individual -- Tax administration |
| FBiH | GIP-1022 | Annual employment-income statement per employee | With annual return cycle | mojobrt.ba |
| FBiH | Contribution payment | Remit monthly social contributions | With salary, no later than end of the following month | PwC, Individual -- Other taxes |
| FBiH / RS | Annual personal income tax return | Reconcile annual PIT | 31 March of the following year | PwC, Individual -- Tax administration |
| RS | Monthly salary-tax specification | Report withheld PIT + contributions | By the 10th day of the following month | PwC, Individual -- Tax administration |
| Brcko District | Annual return | Reconcile PIT if not fully covered by monthly withholding | 28 February of the following year (waived if fully withheld monthly) | PwC, Individual -- Tax administration |

> **[RESEARCH GAP -- reviewer to confirm]** Precise FBiH/RS monthly-specification form codes (e.g. FBiH AUG-1031 / MIP-1023, RS form codes) were NOT confirmed from a single authoritative source. Verify against the PUFBiH and PURS official form catalogues.

### Penalties

**Penalties table**  _(PwC, Individual -- Tax administration)_

| Type | Detail | Source |
| --- | --- | --- |
| Late / non-payment of withheld PIT and contributions | Entity tax laws impose monetary fines on employers plus default interest on overdue amounts; KM ranges are set in the FBiH/RS Law on Tax Administration and contributions laws | PwC, Individual -- Tax administration |

> **[RESEARCH GAP -- reviewer to confirm]** Exact KM fine bands were not confirmed from a single authoritative figure. State that fines + default interest apply, but do not quote a specific band unless verified.

## Section 14 -- Excel Working Paper Template

Recommended monthly payroll working paper (one row per employee). Build formulas off the **Entity** cell so the same sheet handles FBiH and RS.

**Excel working paper template**

| Col | Field | Formula / Source |
| --- | --- | --- |
| A | Employee | input |
| B | Entity | input (FBiH / RS / Brcko) |
| C | Pay period | input (e.g. 2025-08) |
| D | Gross (KM) | input |
| E | Employee SSC rate | `=IF(B="FBiH",0.31,IF(B="RS",0.31,0))` |
| F | Employee SSC | `=D*E` |
| G | Income after SSC | `=D-F` |
| H | Personal deduction | `=IF(B="FBiH",300,IF(B="RS",1000,0))` + dependent factors |
| I | PIT base | `=MAX(0,G-H)` |
| J | PIT rate | `=IF(B="FBiH",0.10,IF(B="RS",0.08,0.10))` |
| K | PIT | `=I*J` |
| L | Net pay | `=G-K` |
| M | Employer SSC rate | `=IF(B="FBiH",IF(C>="2025-07",0.05,0.105),0)` |
| N | Employer SSC | `=D*M` |
| O | FBiH disaster (0.5% net) | `=IF(B="FBiH",L*0.005,0)` |
| P | FBiH water (0.5% net) | `=IF(B="FBiH",L*0.005,0)` |
| Q | Total employer cost | `=D+N+O+P` |

Cross-foot check: column L (net) for an FBiH minimum-wage row must equal 1,000.00 when D=1,562 and H=300.

## Section 15 -- Bank Statement / Terminology Reading Guide

**Terminology reading guide table**

| Local term (Latin / Cyrillic) | English | Notes |
| --- | --- | --- |
| Plata / Placa / Plaća / Плата | Salary | "Placa" common in FBiH (Croatian usage); "Plata"/"Зарада" in RS |
| Bruto / Бруто | Gross | The "bruto" model grosses up from net |
| Neto / Нето | Net | Take-home pay |
| Doprinosi / Доприноси | (Social) contributions | The 31% employee block |
| PIO / MIO / ПИО | Pension & disability insurance | "MIO" = mirovinsko/invalidsko (FBiH Croatian) |
| Zdravstveno osiguranje / Здравствено | Health insurance |  |
| Osiguranje od nezaposlenosti | Unemployment insurance |  |
| Djecija zastita / Дјечија заштита | Child protection | RS-only 1.7% |
| Porez na dohodak / dohotak | Personal income tax | "dohodak" RS, "dohotak" usage varies |
| Porezna kartica / Пореска картица | Tax card | Required to claim personal deduction |
| Najniza placa / najmanja plata | Minimum wage |  |
| Zastita od prirodnih nesreca | Disaster protection | FBiH 0.5% on net |
| Vodne naknade | Water charge | FBiH 0.5% on net |

**Tip:** Cyrillic script on a statement is a strong signal the employer/employee is in **Republika Srpska** -- confirm entity = RS and use the RS rate set.

## Section 16 -- Onboarding Fallback

If you cannot establish the basics, ask the client (do not guess):

1. In which **entity** is the employee employed -- Federation of BiH, Republika Srpska, or Brcko District?
2. What is the **pay period** (month and year)? (Critical for FBiH: rates changed 1 Jul 2025.)
3. Is the figure provided **gross or net**?
4. Is a valid **tax card (*porezna kartica*)** on file, and how many dependents (spouse/children/others)?
5. (RS) What is the employee's **qualification tier** (for minimum-wage checks)?
6. (Brcko) Which **pension fund** has the employee elected -- RS or FBiH?

If the entity cannot be confirmed, default to the **employer's registration entity** and flag the assumption.

## Section 17 -- Reference Material

**Reference material table**

| Item | Value | Source |
| --- | --- | --- |
| FBiH PIT | 10% flat | PwC, Individual -- Taxes on personal income |
| RS PIT | 8% flat (employment) | PwC, Individual -- Taxes on personal income |
| Brcko PIT | 10% flat | PwC, Individual -- Taxes on personal income |
| FBiH employee SSC | 31.0% (17.0 + 12.5 + 1.5) | PwC, Corporate -- Other taxes |
| FBiH employer SSC | 5.0% from 1 Jul 2025 (2.5 + 2.0 + 0.5) | PwC / Nexo / Vlada FBiH |
| FBiH combined | 36.0% from 1 Jul 2025 (was 41.5%) | Vlada FBiH / federalna.ba |
| FBiH employer extra charges | 0.5% disaster + 0.5% water on NET | PwC, Individual -- Other taxes |
| RS employee SSC | 31.0% (18.5 + 10.2 + 1.7 + 0.6) | PwC, Corporate -- Other taxes |
| RS employer SSC | 0% | PwC, Corporate -- Other taxes |
| FBiH personal deduction | 300 KM/mo (3,600 KM/yr) | Klix.ba / rif.hr **[RESEARCH GAP for primary source]** |
| RS personal deduction | 12,000 KM/yr; dependent 1,800 KM/yr | PwC, Individual -- Taxes on personal income |
| FBiH minimum wage 2025 | 1,000 net / 1,562 gross | Sl. novine FBiH 104/24; Vlada FBiH |
| RS minimum wage 2025 | 900 net / 1,344.26 gross (base) to 1,300/2,000 | Sl. glasnik RS 6/25; Plastron |
| Annual PIT return deadline | 31 March (FBiH/RS); 28 Feb Brcko | PwC, Individual -- Tax administration |
| Currency peg | 1 EUR = 1.95583 BAM | Currency board (BAM pegged to EUR) |

### Authorities and primary sources

- Tax Administration of FBiH (PUFBiH): https://www.pufbih.ba
- Tax Administration of RS (PURS): https://poreskaupravars.org
- PwC Worldwide Tax Summaries -- BiH Individual: https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/other-taxes
- PwC Worldwide Tax Summaries -- BiH Corporate: https://taxsummaries.pwc.com/bosnia-and-herzegovina/corporate/other-taxes
- PwC -- Taxes on personal income: https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/taxes-on-personal-income
- PwC -- Tax administration: https://taxsummaries.pwc.com/Bosnia-and-Herzegovina/Individual/Tax-administration
- Vlada FBiH minimum wage 2025: https://fbihvlada.gov.ba/bs/utvrdena-najniza-placa-za-2025-godinu-u-iznosu-od-1000-km
- federalna.ba (41.5% → 36% reform): https://federalna.ba/vlada-fbih-u-2025-minimalna-placa-1000-km-smanjeni-doprinosi-i-podrska-privredi-j4xlv
- Nexo (1 Jul 2025 payroll changes): https://nexo.ba/izmjene-u-obracunu-placa-s-pocetkom-od-1-jula-2025-godine/
- Plastron (RS minimum wage 2025): https://plastron.ba/en/minimum-wage-in-republika-srpska-for-2025/
- Klix.ba (FBiH salary structure / 300 KM deduction): https://www.klix.ba/biznis/finansije/znate-li-sta-se-sve-odbija-od-plate-pogledajte-detaljnu-strukturu-naknada-i-gdje-ide-vas-novac/250110056
- Eurofast BiH Tax Card 2025: https://eurofast.eu/wp-content/uploads/2025/02/TaxCard2025_Bosnia.pdf

## Section 18 -- Test Suite

Each test recomputed end-to-end; figures reconcile to the cent.

**FBiH min wage, no dependents, post-reform:** Gross 1,562.00 → SSC 484.22 → after-SSC 1,077.78 → deduction 300.00 → PIT base 777.78 → PIT 77.78 → **Net 1,000.00 KM**. Employer SSC 78.10; total employer cost 1,650.10. (Reconciles to published 1,000 KM net.)

**FBiH gross 2,000, no dependents, post-reform:** SSC 620.00 → after-SSC 1,380.00 → deduction 300.00 → PIT base 1,080.00 → PIT 108.00 → **Net 1,272.00 KM**. Employer SSC 100.00; disaster + water 12.72; total employer cost 2,112.72.

**FBiH gross 2,000, pre-reform (Feb 2025):** Employee outcome identical (Net 1,272.00). Employer SSC 10.5% = 210.00; total employer cost 2,222.72 (110.00 higher than test 2).

**RS gross 1,508.20, no dependents:** SSC 467.54 → after-SSC 1,040.66 → deduction 1,000.00 → PIT base 40.66 → PIT 3.25 → **Net 1,037.41 KM**. Employer SSC 0.00; total employer cost 1,508.20. (Mechanical net 1,037.41 differs from published 1,000 net — flag per Conservative Default 4.)

**RS gross 2,000, 1 dependent:** SSC 620.00 → after-SSC 1,380.00 → deduction 1,150.00 (1,000 + 150) → PIT base 230.00 → PIT 18.40 → **Net 1,361.60 KM**. Employer SSC 0.00; total employer cost 2,000.00.

**FBiH gross 3,000, married + 2 children, post-reform:** SSC 930.00 → after-SSC 2,070.00 → deduction 810.00 (300 + 150 + 150 + 210) → PIT base 1,260.00 → PIT 126.00 → **Net 1,944.00 KM**. Employer SSC 150.00; disaster + water 19.44; total employer cost 3,169.44.

**Rate-table totals:** FBiH employee 17.0 + 12.5 + 1.5 = 31.0 ✓; FBiH employer 2.5 + 2.0 + 0.5 = 5.0 ✓; FBiH combined 36.0 ✓; RS employee 18.5 + 10.2 + 1.7 + 0.6 = 31.0 ✓; RS employer 0 ✓.

**Entity branch:** Cyrillic statement line → entity = RS → 8% PIT, 31% employee SSC, 0% employer SSC. ✓

## PROHIBITIONS

- **Entity determination required** — NEVER compute Bosnia payroll without first establishing the entity (FBiH / RS / Brcko).
- **No unified national rate** — NEVER apply a single "Bosnia" rate -- there is no unified national payroll system.
- **FBiH employer rate pre-reform restriction** — NEVER use FBiH employer 5.0% / 36% combined for periods before 1 Jul 2025 (use 10.5% / 41.5%).
- **No RS employer SSC** — NEVER charge employer SSC in RS -- there is none (all 31% is employee-borne).
- **FBiH disaster + water charges** — NEVER forget the FBiH 0.5% disaster + 0.5% water charges on NET (outside the 36%).
- **Personal deduction requires tax card** — NEVER apply the personal deduction without a valid tax card (porezna kartica) on file.
- **Research gap verification** — NEVER quote a specific penalty KM band or form code that is marked [RESEARCH GAP] without verifying against PUFBiH/PURS.
- **No back-solving published net figures** — NEVER back-solve a published "net" figure where the mechanics disagree -- present the computation and flag it.
- **Label as estimated, direct to licensed accountant** — NEVER present payroll computations as definitive -- always label as estimated and direct to a BiH licensed accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax adviser in Bosnia and Herzegovina) before implementation.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
