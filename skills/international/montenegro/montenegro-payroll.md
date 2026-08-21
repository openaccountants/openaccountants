---
name: montenegro-payroll
description: Use this skill whenever asked about Montenegro payroll processing for employed persons. Trigger on phrases like "Montenegro payroll", "Crna Gora plata", "porez na dohodak fizičkih lica", "PIT Montenegro", "withholding tax Montenegro", "IOPPD form", "IOPPD obrazac", "social contributions Montenegro", "doprinosi za socijalno osiguranje", "PIO pension Montenegro", "Fond PIO", "penziono i invalidsko osiguranje", "unemployment contribution Montenegro", "health insurance Montenegro", "prirez Montenegro", "municipal surtax Montenegro", "Europe Now 2", "Evropa sad 2", "net salary Montenegro", "neto plata", "bruto neto Crna Gora", "PAYE Montenegro", "employer contributions Montenegro", "minimum wage Montenegro", "minimalna zarada", "gross to net Montenegro", "Uprava prihoda i carina", or any question about computing employee pay, withholding personal income tax, or mandatory social contributions for Montenegro-based employees. This skill covers progressive PIT withholding on gross salary, the municipal surtax (prirez) on assessed PIT, employee social contributions (PIO + unemployment), the residual employer contributions, the dual-tier minimum wage, and IOPPD filing obligations under the post-October-2024 "Europe Now 2.0" reform. ALWAYS read this skill before processing any Montenegro payroll.
version: 0.1
jurisdiction: ME
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro Payroll

## Montenegro Payroll Skill v0.1

**Tier 2 — research-verified. Figures below are sourced from PwC Worldwide Tax Summaries, KPMG Montenegro (October 2024 Tax Alert), Eurofast (Montenegro Tax Card 2025), Karanovic & Partners and Perfectum, referencing the Revenue and Customs Administration of Montenegro (Uprava prihoda i carina Crne Gore), the Fund for Pension and Disability Insurance (Fond PIO) and the Ministry of Labour. NOT yet signed off by a licensed Montenegrin accountant or tax adviser. The figures incorporate the "Europe Now 2.0" (Evropa sad 2) reform effective 1 October 2024. Treat every computation as an estimate pending professional review.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Montenegro (Crna Gora) — ISO 3166-1 alpha-2: ME |
| Currency | EUR only (Montenegro uses the euro unilaterally) |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) (PwC — Tax administration) |
| Tax withholding system | Monthly PAYE — the employer withholds personal income tax (porez na dohodak fizičkih lica) and all contributions at source on the gross salary (PwC; Eurofast 2025) |
| Income / contributions authority | Revenue and Customs Administration of Montenegro (Uprava prihoda i carina Crne Gore), under the Ministry of Finance — https://www.upravaprihoda.gov.me/ |
| Pension authority | Fund for Pension and Disability Insurance (Fond PIO) |
| Employment / minimum-wage authority | Ministry of Labour and Social Welfare |
| Key legislation | Personal Income Tax Law (Zakon o porezu na dohodak fizičkih lica); Law on Mandatory Social Security Contributions (Zakon o obaveznom socijalnom osiguranju, amended Oct 2024); Labour Law (Zakon o radu); Law on Surtax on Personal Income Tax (municipal surtax) |
| Reform package | "Europe Now 2.0" (Evropa sad 2), effective 1 October 2024 (KPMG Oct 2024 Tax Alert) |
| Filing form | IOPPD (Obrazac IOPPD) — integrated monthly return of calculated/paid PIT and contributions, filed to the Revenue and Customs Administration (Perfectum; payroll guides) |
| Validated by | Pending -- requires sign-off by a licensed Montenegrin accountant / tax adviser |
| Skill version | 0.1 |

**Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` — follow that runbook with this skill supplying the Montenegro-specific content.**

### The two most important Montenegro facts

- **Fact 1 — PIT computed on gross salary** — PIT is computed on GROSS salary, not on a reduced base. Unlike many neighbouring jurisdictions, Montenegro's progressive PIT bands apply directly to the gross monthly salary (0% up to EUR 700, 9% on EUR 700.01–1,000, 15% above EUR 1,000.01). Social contributions are NOT subtracted before computing PIT.  _(PwC — Taxes on personal income; Eurofast 2025 p.3)_
- **Fact 2 — Europe Now 2.0 reform effect** — The "Europe Now 2.0" reform (1 October 2024) gutted the contribution wedge. The employer pension share fell from 5.5% to 0%, the employee pension share fell from 15% to 10%, and the mandatory health contribution is 0% for both sides. Post-reform the employee social wedge is 10.5% and the employer wedge is ~1.17%. Eurofast's 2025 card still PRINTS stale pre-reform column totals (15.5% employee / 6.47% employer) — those are WRONG; use the itemised post-reform rows.  _(KPMG Oct 2024 Tax Alert; PwC; Eurofast 2025 p.4 — see Section 4 source conflict)_

## Section 2 -- Income Tax Withholding (porez na dohodak fizičkih lica)

The employer withholds personal income tax (PIT) monthly at source on the gross monthly salary using progressive, marginal bands, then applies the municipal surtax (prirez) to the assessed PIT. PIT and surtax are withheld and remitted monthly. (PwC; Eurofast 2025)

### Employment-income PIT bands (2025) — applied to GROSS monthly salary

**Employment-income PIT bands (2025) — applied to GROSS monthly salary**  _(PwC — Taxes on personal income; Eurofast Tax Card 2025 p.3)_

| Band | Monthly gross salary | Marginal rate |
| --- | --- | --- |
| 1 | EUR 0.00 – 700.00 | 0% |
| 2 | EUR 700.01 – 1,000.00 | 9% |
| 3 | over EUR 1,000.01 | 15% |

- **Marginal band application** — The bands are marginal: only the slice of gross within each band is taxed at that band's rate. The 0% band IS the tax-free allowance — there is no separate personal allowance applied on top.  _(PwC — Taxes on personal income; Eurofast Tax Card 2025 p.3)_

### Monthly withholding method (deterministic)

- **Monthly withholding steps** — 1. Start with gross monthly salary (bruto plata). 2. Compute PIT by applying each marginal band to the slice of gross within it: 0% on the portion up to EUR 700.00; 9% on the portion from EUR 700.01 to EUR 1,000.00 (max EUR 27.00 in this band — verify: 300 × 9% = 27.00 ✓); 15% on the portion above EUR 1,000.01. 3. Compute the municipal surtax (prirez) = surtax rate × assessed PIT (NOT × income) — see below. 4. Total tax withheld = PIT + surtax. 5. Separately withhold employee social contributions at 10.5% of gross (Section 3). 6. Net pay = gross − employee social contributions − PIT − surtax.  _(PwC; Eurofast 2025)_

Note the order does not matter for the arithmetic because every deduction is computed on gross independently: contributions on gross, PIT on gross, surtax on the PIT amount. There is no "income after contributions" intermediate base for PIT.

### Municipal surtax (prirez) on assessed PIT

**Municipal surtax (prirez) on assessed PIT**  _(PwC — Taxes on personal income)_

| Location | Surtax rate (× assessed PIT) |
| --- | --- |
| Podgorica and Cetinje | 15% |
| All other municipalities (national default) | 13% |

- **Surtax range source conflict** — Eurofast states a wider 10%–15% range depending on municipality (Eurofast 2025 p.10); the specific municipality's by-law governs. [T2-1 — reviewer to confirm the exact surtax rate for the employee's municipality of residence.] The surtax is charged on the assessed PIT amount, not on the income.  _(Eurofast 2025 p.10)_

### Other personal-income rates (context — not employment payroll)

**Other personal-income rates (context — not employment payroll)**

| Income type | Rate | Note |
| --- | --- | --- |
| Self-employment / entrepreneurial (annual, marginal) | 0% to EUR 8,400; 9% EUR 8,400.01–12,000; 15% above EUR 12,000.01 | Annual entrepreneurial income — out of scope for employer payroll (PwC) |
| Capital gains, rental, interest, dividends, royalties | 15% flat | Not employment income (PwC; Eurofast 2025) |

## Section 3 -- Contributions: Employee Deductions

Employees bear a total social-contribution wedge of 10.5% of gross, withheld at source. (PwC — Other taxes; KPMG Oct 2024 Tax Alert; Eurofast 2025 p.4)

**Employee contributions table**  _(PwC — Other taxes; KPMG Oct 2024 Tax Alert; Eurofast 2025 p.4)_

| Contribution | Employee rate | Base | Authority | Note |
| --- | --- | --- | --- | --- |
| Pension and Disability Insurance (PIO) | 10.0% | Gross salary (capped — see ceiling) | Fond PIO | Cut from 15% to 10% on 1 Oct 2024 (KPMG) |
| Unemployment insurance | 0.5% | Gross salary | Revenue & Customs Admin | (Eurofast 2025 p.4; PwC) |
| Health insurance | 0.0% | — | — | Mandatory employee health contribution abolished (Eurofast 2025 p.4 — Health Fund 0.0%) |
| **Total employee contributions** | **10.5%** | Gross | — | 10.0% + 0.5% + 0.0% — verify: 10.0 + 0.5 = 10.5 ✓ |

### PIO contribution base ceiling

**PIO contribution base ceiling**  _(PwC — Other taxes)_

| Cap | Amount | Year | Note |
| --- | --- | --- | --- |
| Annual PIO contribution base ceiling | EUR 68,765 | 2024 published figure (reset annually) | PwC — Other taxes |
| Implied monthly PIO base cap | EUR 5,730.42 | derived | = 68,765 ÷ 12 (verify: 68,765 / 12 = 5,730.4166… ≈ 5,730.42) |

Source conflict flagged. PwC publishes the annual PIO base ceiling as EUR 68,765 (2024); the ceiling is reset annually and the 2025/2026 figure was NOT independently confirmed from Fond PIO / the Official Gazette in this research. One secondary source (TaxRavens) cites a conflicting ~EUR 54,533. [RESEARCH GAP — reviewer to confirm the current-year PIO base ceiling with the Tax Administration / Fond PIO before relying on it.] Whether the EUR 0.5% unemployment contribution is also subject to the PIO ceiling, or applies to uncapped gross, is not confirmed — this skill applies unemployment to full gross and flags it. [T2-2]

## Section 4 -- Contributions: Employer Contributions

Post-reform the employer wedge is small — the employer pays no PIO and no health contribution. The residual employer-borne contributions total ~1.17% of gross. (Eurofast 2025 p.4 itemised; KPMG Oct 2024 Tax Alert)

**Employer contributions table**  _(Eurofast 2025 p.4 itemised; KPMG Oct 2024 Tax Alert)_

| Contribution | Employer rate | Base | Note |
| --- | --- | --- | --- |
| Unemployment insurance | 0.5% | Gross salary | Matches the 0.5% employee unemployment line (Eurofast 2025 p.4) |
| Labour Fund (Fond rada) | 0.2% | Gross salary | Employer-only (Eurofast 2025 p.4) |
| Chamber of Commerce membership contribution | 0.27% | Gross salary | Employer-only (Eurofast 2025 p.4) |
| Prevention of Disability Fund | 0.2% | Gross salary | Employer-only (Eurofast 2025 p.4) |
| Pension and Disability Insurance (PIO) | 0.0% | — | Employer share cut from 5.5% to 0% on 1 Oct 2024 (KPMG) |
| Health insurance | 0.0% | — | Abolished (Eurofast 2025 p.4 — Health Fund 0.0%) |
| **Total employer contributions** | **1.17%** | Gross | 0.5% + 0.2% + 0.27% + 0.2% — verify: 0.5 + 0.2 + 0.27 + 0.2 = 1.17 ✓ |

- **Total employer cost formula** — Total employer cost = gross salary + (1.17% × gross) = gross × 1.0117.  _(Derived from Eurofast itemised rates + KPMG reform)_

Source conflict flagged — do NOT use Eurofast's printed totals. The Eurofast 2025 Tax Card prints column totals "Employees 15.5%" and "Employer 6.47%". These are internally inconsistent with the itemised rows in the same table: the 15.5% reflects the PRE-reform employee pension of 15% (now 10%), and the 6.47% reflects pre-reform employer rates (PIO employer 5.5%, now 0%). PwC and KPMG confirm the post-1-Oct-2024 employee total is 10.5% and the employer PIO is 0%. This skill uses the itemised post-reform figures (employee 10.5%, employer 1.17%). [T2-3 — an accountant should confirm against the consolidated Law on Mandatory Social Security Contributions in the Official Gazette.]

### Combined wage wedge

**Combined wage wedge**

| Component | Rate |
| --- | --- |
| Employee social contributions | 10.5% |
| Employer social contributions | 1.17% |
| **Combined social-contribution wedge** | **11.67%** (verify: 10.5 + 1.17 = 11.67 ✓) |

(PIT and municipal surtax are on top of the social wedge.)

## Section 5 -- Minimum Wage and Working Conditions

### National minimum wage (from 1 October 2024) — dual NET tier

**National minimum wage (from 1 October 2024) — dual NET tier**  _(KPMG Oct 2024 Tax Alert; Karanovic & Partners)_

| Qualification tier | Net monthly minimum |
| --- | --- |
| Jobs requiring up to a high-school diploma | EUR 600 net |
| Jobs requiring higher qualifications | EUR 800 net |

- **Dual net wage structure** — The Europe Now 2.0 reform replaced a single minimum with this dual NET-wage structure tied to the qualification level of the job.  _(KPMG Oct 2024 Tax Alert; Karanovic & Partners)_

Source conflict flagged. Some 2025 trackers (Trading Economics, minimum-wage.org) report a single figure of ~EUR 670 net / ~EUR 700 gross rather than the EUR 600/EUR 800 net tiers. The exact 2025/2026 gross-up of the net minima, and whether the EUR 600/800 tiers were further indexed, were not confirmed from a primary source. [RESEARCH GAP — reviewer to confirm the current gross/net minimum wage and tier structure with the Ministry of Labour.]

### Working hours and overtime

[RESEARCH GAP — reviewer to confirm] Statutory overtime multipliers, maximum weekly hours, and night/Sunday/holiday premiums under the Montenegrin Labour Law (Zakon o radu) were not part of this research dataset. A reviewer should populate these from the Labour Law and any applicable collective agreement before relying on overtime figures.

## Section 6 -- Conservative Defaults

- **Conservative default policy** — When an input is unknown, the skill MUST apply the conservative default below and flag the assumption in its output rather than guessing a more favourable figure.

**Conservative defaults table**

| Field | Default | Rationale |
| --- | --- | --- |
| Employee social-contribution rate | **10.5% of gross** (PIO 10% + unemployment 0.5%; health 0%) | Confirmed by PwC, KPMG (Oct 2024 reform) and Eurofast itemised table; use itemised figures, NOT Eurofast's printed 15.5% total. |
| Employer social-contribution rate | **1.17% of gross** (unemployment 0.5% + Labour Fund 0.2% + Chamber 0.27% + Prevention of Disability 0.2%; PIO and health 0%) | Itemised from Eurofast 2025 card; the card's printed 6.47% total is a stale pre-reform aggregate. |
| Municipal surtax | **13% of assessed PIT** (15% if the employee resides in Podgorica or Cetinje) | PwC; surtax is on the PIT amount, not on income. Use the employee's municipality of residence. (Eurofast cites a 10–15% range.) |
| PIO base ceiling | **EUR 68,765/yr → ~EUR 5,730.42/month** (apply the cap to the PIO base only) | PwC 2024 figure; reset annually — flag for reviewer confirmation. **[RESEARCH GAP]** |
| Unemployment-contribution base | **Full gross (uncapped)** | The PIO ceiling's application to unemployment is unconfirmed; applying to full gross is the conservative assumption. **[T2-2]** |
| PIT base | **Gross salary (no deduction of contributions before PIT)** | Montenegro applies PIT bands directly to gross. (PwC) |
| Monthly filing | **File IOPPD and remit PIT + surtax + contributions by the 15th of the following month** | Eurofast tax calendar + payroll guides + Perfectum. |

## Section 7 -- Required Inputs and Refusal Catalogue

### Required inputs before any computation

- **Required inputs list** — 1. Gross monthly salary (bruto plata) in EUR. 2. Employee's municipality of residence — to select the correct surtax rate (15% Podgorica/Cetinje vs 13% default). If unknown, default to 13% and flag it. 3. Pay period (month and year) — to pick the correct minimum wage, PIO ceiling and band figures, and to confirm the post-1-Oct-2024 reform applies. 4. Whether the employee's gross exceeds the monthly PIO base cap (~EUR 5,730.42) — triggers the contribution ceiling. 5. The qualification tier of the job — to check against the dual-tier minimum wage (EUR 600 / EUR 800 net).

### Refusal Catalogue — DO NOT attempt; route to a licensed accountant

**Refusal Catalogue table**

| Scenario | Why it is out of scope |
| --- | --- |
| Posted workers / A1-equivalent / cross-border social-security coordination | Requires bilateral social-security agreement analysis and Fond PIO determinations — see `cross-border-payroll-coordination`. |
| Non-resident employees, double-tax-treaty relief, expat tax-equalisation | Treaty residency and tie-breaker analysis is beyond a domestic payroll run. |
| Withholding tax on payments to non-residents (dividends, interest, royalties, services) | 15% (30% for low-tax jurisdictions), reducible by treaty — out of scope for employee payroll (Eurofast 2025 p.7). |
| Benefits in kind / company cars / stock options valuation | Montenegrin BIK valuation rules were not in this research dataset. **[RESEARCH GAP]** |
| Self-employed / entrepreneurial income (annual 0/9/15% bands) | Different regime — out of scope for employer payroll. |
| Sickness, maternity and disability benefit reimbursement mechanics | Not covered here. |
| Severance / termination payment taxation | Not in scope; route to a reviewer. |
| Exact penalty quantification per offence | Penalty ranges are statutory bands (Section 13); apply judgement and confirm the specific charge with the Tax Administration. |

## Section 8 -- Transaction / Payment Pattern Library

Deterministic classification of Montenegrin bank-statement lines for payroll. Match on the uppercased description fragment.

### Salary credits (what lands in the employee's account)

**Salary credits table**

| Bank statement text (ME / EN) | Classification |
| --- | --- |
| `PLATA`, `ZARADA`, `NETO PLATA`, `ISPLATA ZARADE` | Net salary payment |
| `PLACA`, `SALARY`, `WAGES` | Net salary payment (ASCII / English variant) |
| `AKONTACIJA ZARADE`, `AVANS` | Salary advance (not final pay) |
| `NAKNADA`, `TOPLI OBROK`, `REGRES` | Allowance / meal / holiday allowance (check taxability) |
| `DNEVNICA` | Per-diem / travel allowance (may be tax-exempt up to limits) |
| `POVRAĆAJ POREZA` | Income tax refund — NOT income |

### Employer debits (what leaves the employer's account)

**Employer debits table**

| Bank statement text (ME / EN) | Classification |
| --- | --- |
| `POREZ NA DOHODAK`, `UPRAVA PRIHODA`, `UPiC` | Personal income tax (and surtax) remittance to the Revenue & Customs Administration |
| `PRIREZ` | Municipal surtax remittance |
| `DOPRINOS PIO`, `PENZIJSKO`, `FOND PIO` | Pension & Disability (PIO) contribution remittance |
| `DOPRINOS NEZAPOSLENOST`, `OSIGURANJE NEZAPOSLENOSTI` | Unemployment-insurance contribution remittance |
| `FOND RADA`, `KOMORA`, `FOND ZA INVALIDE` | Labour Fund / Chamber of Commerce / Prevention-of-Disability remittances (employer-only) |
| `IOPPD` | Reference tag for an IOPPD-linked payment batch |
| `ISPLATA ZARADA`, `PAYROLL`, `OBRAČUN ZARADE` | Net wages disbursed to employees |

PIT, surtax and all contributions are reported together on the IOPPD form (Section 12) and remitted simultaneously, due by the 15th of the following month.

## Section 9 -- Worked Examples

All examples use 2025 figures and the post-1-Oct-2024 "Europe Now 2.0" rates: employee contributions 10.5% of gross, employer 1.17% of gross, PIT on gross (0% / 9% / 15% marginal). Surtax defaults to 13% unless the employee resides in Podgorica/Cetinje (15%). Every line below was recomputed end-to-end.

### Example 1 — Mid-low earner, EUR 800 gross/month, non-Podgorica (13% surtax)

Bank statement context: `ISPLATA ZARADE … 705,83 EUR` credited to the employee; `UPRAVA PRIHODA … 10,17 EUR` and `FOND PIO … 80,00 EUR` debited from the employer.

**Example 1 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 800.00 |
| PIT — band 1 (0% on first 700) | 700 × 0% | 0.00 |
| PIT — band 2 (9% on 700.01–800) | (800 − 700) × 9% | 9.00 |
| Total PIT | 0 + 9.00 | 9.00 |
| Municipal surtax (13% of PIT) | 9.00 × 13% | 1.17 |
| Employee contributions (10.5% of 800) | PIO 10% (80.00) + unemployment 0.5% (4.00) | 84.00 |
| **Net pay** | 800 − 84.00 − 9.00 − 1.17 | **705.83** |
| Employer contributions (1.17% of 800) | on top of gross | 9.36 |
| **Total employer cost** | 800 + 9.36 | **809.36** |

### Example 2 — Higher earner in Podgorica, EUR 1,500 gross/month (15% surtax)

**Example 2 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 1,500.00 |
| PIT — band 1 (0% on first 700) | 700 × 0% | 0.00 |
| PIT — band 2 (9% on 700.01–1,000) | 300 × 9% | 27.00 |
| PIT — band 3 (15% on 1,000.01–1,500) | 500 × 15% | 75.00 |
| Total PIT | 0 + 27.00 + 75.00 | 102.00 |
| Municipal surtax (15% Podgorica) | 102.00 × 15% | 15.30 |
| Employee contributions (10.5% of 1,500) | — | 157.50 |
| **Net pay** | 1,500 − 157.50 − 102.00 − 15.30 | **1,225.20** |
| Employer contributions (1.17% of 1,500) | on top | 17.55 |
| **Total employer cost** | 1,500 + 17.55 | **1,517.55** |

### Example 3 — At the 0% ceiling, EUR 700 gross/month, 13% surtax

**Example 3 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 700.00 |
| PIT — band 1 (0% on first 700) | 700 × 0% | 0.00 |
| Total PIT | — | 0.00 |
| Municipal surtax (13% of 0) | 0 × 13% | 0.00 |
| Employee contributions (10.5% of 700) | — | 73.50 |
| **Net pay** | 700 − 73.50 − 0 | **626.50** |
| Employer contributions (1.17% of 700) | on top | 8.19 |
| **Total employer cost** | 700 + 8.19 | **708.19** |

At EUR 700 gross the PIT is exactly zero (the 0% band IS the tax-free allowance) — but contributions still apply. The 9% band bites only on gross above EUR 700.00.

### Example 4 — At the 9% ceiling, EUR 1,000 gross/month, 13% surtax

**Example 4 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 1,000.00 |
| PIT — band 1 (0% on first 700) | 700 × 0% | 0.00 |
| PIT — band 2 (9% on 700.01–1,000) | 300 × 9% | 27.00 |
| Total PIT | 0 + 27.00 | 27.00 |
| Municipal surtax (13% of PIT) | 27.00 × 13% | 3.51 |
| Employee contributions (10.5% of 1,000) | — | 105.00 |
| **Net pay** | 1,000 − 105.00 − 27.00 − 3.51 | **864.49** |
| Employer contributions (1.17% of 1,000) | on top | 11.70 |
| **Total employer cost** | 1,000 + 11.70 | **1,011.70** |

At exactly EUR 1,000 gross the whole salary sits within bands 1 and 2; the 15% band applies only to gross above EUR 1,000.01.

### Example 5 — High earner under the PIO cap, EUR 3,000 gross/month, 13% surtax

**Example 5 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 3,000.00 |
| PIT — band 1 (0% on first 700) | 700 × 0% | 0.00 |
| PIT — band 2 (9% on 700.01–1,000) | 300 × 9% | 27.00 |
| PIT — band 3 (15% on 1,000.01–3,000) | 2,000 × 15% | 300.00 |
| Total PIT | 0 + 27.00 + 300.00 | 327.00 |
| Municipal surtax (13% of PIT) | 327.00 × 13% | 42.51 |
| Employee contributions (10.5% of 3,000) | gross below the monthly PIO cap (~5,730.42) | 315.00 |
| **Net pay** | 3,000 − 315.00 − 327.00 − 42.51 | **2,315.49** |
| Employer contributions (1.17% of 3,000) | on top | 35.10 |
| **Total employer cost** | 3,000 + 35.10 | **3,035.10** |

### Example 6 — Above the PIO base cap, EUR 6,000 gross/month, Podgorica (15% surtax)

**Example 6 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 6,000.00 |
| PIT — band 1 (0% on first 700) | 700 × 0% | 0.00 |
| PIT — band 2 (9% on 700.01–1,000) | 300 × 9% | 27.00 |
| PIT — band 3 (15% on 1,000.01–6,000) | 5,000 × 15% | 750.00 |
| Total PIT | 0 + 27.00 + 750.00 | 777.00 |
| Municipal surtax (15% Podgorica) | 777.00 × 15% | 116.55 |
| PIO base after cap | min(6,000, 5,730.42) | 5,730.42 |
| PIO contribution (10% of capped base) | 5,730.42 × 10% | 573.04 |
| Unemployment (0.5% of full gross) | 6,000 × 0.5% — applied to full gross **[T2-2]** | 30.00 |
| Total employee contributions | 573.04 + 30.00 | 603.04 |
| **Net pay** | 6,000 − 603.04 − 777.00 − 116.55 | **4,503.41** |
| Employer contributions (1.17% of 6,000) | on top | 70.20 |
| **Total employer cost** | 6,000 + 70.20 | **6,070.20** |

The PIO contribution base is capped at ~EUR 5,730.42/month (= EUR 68,765/yr ÷ 12, 2024 figure), so PIO = EUR 573.04 rather than 10% of full gross. Whether unemployment is also capped is unconfirmed [T2-2] — this example applies unemployment to full gross. [RESEARCH GAP — confirm the current-year PIO ceiling and the unemployment-base treatment with the Tax Administration.]

## Section 10 -- Tier 1 Rules (deterministic — the skill applies these directly)

- **Tax year** — Tax year = calendar year (1 Jan – 31 Dec).  _(PwC — Tax administration)_
- **Employment-income PIT bands (marginal, on gross monthly salary)** — 0% up to EUR 700.00, 9% on EUR 700.01–1,000.00, 15% above EUR 1,000.01. Social contributions are NOT deducted before computing PIT.  _(PwC; Eurofast 2025 p.3)_
- **0% band nature** — The 0% band is the tax-free allowance — there is no separate personal allowance.  _(PwC)_
- **Municipal surtax (prirez)** — Charged on the assessed PIT amount: 13% nationwide, 15% in Podgorica and Cetinje. Eurofast cites a 10–15% municipal range. [T2-1]  _(PwC)_
- **Employee social contributions total** — 10.5% of gross: PIO 10.0% + unemployment 0.5% + health 0.0%  _(PwC; KPMG; Eurofast 2025 p.4)_
- **Employer social contributions total** — ~1.17% of gross: unemployment 0.5% + Labour Fund 0.2% + Chamber of Commerce 0.27% + Prevention of Disability Fund 0.2%; PIO and health both 0%  _(Eurofast 2025 p.4 itemised; KPMG)_
- **Europe Now 2.0 reform** — The "Europe Now 2.0" reform (1 Oct 2024) cut PIO from 20.5% to 10% total (employer 5.5%→0%, employee 15%→10%) and confirmed health at 0%/0%.  _(KPMG Oct 2024 Tax Alert)_
- **Stale totals prohibition** — Do NOT use Eurofast's printed column totals (15.5% employee / 6.47% employer) — they are stale pre-reform aggregates. Use the itemised rows (10.5% / 1.17%).  _(KPMG; PwC)_
- **PIO contribution base cap** — EUR 68,765/yr (2024 published; ≈ EUR 5,730.42/month). The ceiling resets annually.  _(PwC [RESEARCH GAP — confirm current-year cap.])_
- **Total employer cost** — Total employer cost = gross × 1.0117 (gross + 1.17% contributions). PIT and surtax are withheld from the employee, not added to employer cost.
- **Net pay** — Net pay = gross − employee contributions (10.5%) − PIT − surtax. Each is computed independently on its own base.  _(PwC; Eurofast)_
- **IOPPD filing/remittance** — Employers file the integrated monthly IOPPD return and remit PIT + surtax + all contributions simultaneously, due by the 15th of the following month.  _(Eurofast tax calendar; Perfectum; payroll guides)_
- **Annual PIT return deadline** — Annual PIT return due 30 April; single-employer employees with only employment income need not file.  _(Eurofast 2025 p.10; PwC)_
- **Minimum wage (dual net tier) from 1 Oct 2024** — EUR 600 net (jobs up to high-school qualification) and EUR 800 net (higher qualification).  _(KPMG; Karanovic & Partners [RESEARCH GAP — current gross-up unconfirmed.])_
- **Currency** — Montenegro uses EUR only.

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue (reviewer judgement required)**  _(Section 11)_

| Ref | Issue | What the reviewer must resolve |
| --- | --- | --- |
| **[T2-1]** | Exact municipal surtax rate | PwC states 13% (15% Podgorica/Cetinje); Eurofast states a 10–15% range by municipality. Confirm the specific municipality's surtax by-law. |
| **[T2-2]** | Unemployment-contribution base vs the PIO ceiling | Whether the 0.5% unemployment contribution is subject to the PIO base ceiling or applies to uncapped gross is unconfirmed; this skill applies it to full gross. Confirm with the Tax Administration. |
| **[T2-3]** | Post-reform contribution totals vs Eurofast printed totals | Eurofast prints 15.5% / 6.47% (pre-reform); itemised rows give 10.5% / 1.17% (post-reform, per PwC/KPMG). Confirm against the consolidated Law on Mandatory Social Security Contributions in the Official Gazette. |
| **[T2-4]** | Current-year PIO base ceiling | PwC publishes EUR 68,765 (2024); TaxRavens cites ~EUR 54,533. Confirm the current-year cap with Fond PIO / the Official Gazette. **[RESEARCH GAP]** |
| **[T2-5]** | Minimum wage gross/net and tier structure | EUR 600/EUR 800 net (KPMG) vs ~EUR 670 net / ~EUR 700 gross single figure (trackers). Confirm with the Ministry of Labour. **[RESEARCH GAP]** |
| **[T2-6]** | Overtime / night / holiday premiums and maximum hours | Not in this research dataset — confirm from the Labour Law (Zakon o radu) and any collective agreement. **[RESEARCH GAP]** |
| **[T2-7]** | Benefits in kind, severance, per-diem/travel-allowance tax limits | Not in this research dataset — reviewer to populate. **[RESEARCH GAP]** |
| **[T2-8]** | IOPPD exact form code/version and submission channel | Corroborated by Eurofast calendar + Perfectum + payroll guides; confirm the current form code/version on the Tax Administration portal. |

## Section 12 -- Filing Obligations

### Monthly — IOPPD

**Monthly — IOPPD**  _(Eurofast 2025 p.10; Perfectum)_

| Form | Purpose | Deadline |
| --- | --- | --- |
| **IOPPD (Obrazac IOPPD)** | Integrated monthly return of calculated and paid personal income tax (and surtax) and mandatory social security contributions on salaries; filed online (or in person) to the Revenue and Customs Administration. There is no separate contributions report — IOPPD covers PIT and all contributions. | By the 15th of the month following the reporting month; tax and contributions are paid simultaneously with filing. (Eurofast 2025 p.10 tax calendar; Perfectum; payroll guides) **[T2-8 — confirm exact form code/version.]** |
| Payment of PIT + surtax + contributions | Remittance of withheld amounts | Same as IOPPD (15th of the following month). (Eurofast 2025 p.10) |

### Annual and other returns (employer-entity context)

**Annual and other returns (employer-entity context)**  _(Eurofast 2025 p.10)_

| Form | Purpose | Deadline |
| --- | --- | --- |
| Annual personal income tax return (GPP-FL / godišnja prijava) | Annual PIT reconciliation. Individuals with only single-employer employment income are NOT obliged to file. | 30 April for the previous year. (Eurofast 2025 p.10; PwC — Tax administration) |
| Withholding tax on dividends/distributions | Declaration and payment of dividend-distribution withholding | 28 February for the previous year. (Eurofast 2025 p.10) |
| Annual corporate income tax return | CIT return (employer entity) | 31 March for the previous year. (Eurofast 2025 p.10) |
| VAT return | Declaration and payment of VAT | 15th of the following month. (Eurofast 2025 p.10) |

- **Corporate income tax (employer-entity context)** — Progressive: 9% up to EUR 100,000 taxable profit, 12% to EUR 1,500,000, 15% above.  _(Eurofast 2025 p.5)_
- **VAT rates and registration threshold** — Standard 21%, reduced 7% and 15%, zero 0%; registration threshold EUR 30,000 turnover in a 12-month period.  _(Eurofast 2025 p.8)_

## Section 13 -- Penalties

Statutory fine bands per the relevant laws (Eurofast 2025 p.10). Default interest may also apply to late payments.

**Penalties table**  _(Eurofast 2025 p.10)_

| Area | Trigger | Fine band |
| --- | --- | --- |
| Personal Income Tax Law | Failure to submit the annual PIT return within the legal deadline; late or incorrect payment; other related offences | EUR 2,000 – EUR 10,000 (Eurofast 2025 p.10) |
| Corporate Income Tax / withholding | Late submission of a withholding or CIT return; late payment of CIT or withholding; other related offence | EUR 550 – EUR 16,500 (Eurofast 2025 p.10) |
| VAT | Failure to register; failure to submit a VAT return; fiscalisation / other VAT offences | EUR 3,000 – EUR 40,000 (Eurofast 2025 p.10) |

**[RESEARCH GAP — reviewer to confirm]** The specific penalty band for late IOPPD filing or late remittance of payroll PIT/contributions, and the default-interest rate, were not isolated from a primary source in this research. The PIT-Law band above (EUR 2,000–10,000) is the closest published range. Confirm the applicable charge with the Tax Administration. Record-keeping retention periods were also not confirmed. **[RESEARCH GAP]**

## Section 14 -- Excel Working Paper Template

A reviewer-ready monthly payroll working paper should contain the following columns (one row per employee per month). Inputs are entered; computed cells follow the Section 2 / Section 3 order exactly.

**Excel Working Paper Template columns**  _(Section 14)_

| Col | Heading | Type | Formula / source |
| --- | --- | --- | --- |
| A | Employee name | Input | — |
| B | JMBG / tax ID | Input | personal identification number |
| C | Municipality of residence | Input | drives surtax rate (15% Podgorica/Cetinje, else 13%) |
| D | Gross salary (EUR) | Input | bruto plata |
| E | PIT — band 1 (0%) | Computed | `0` (on `MIN(D,700)`) |
| F | PIT — band 2 (9%) | Computed | `MAX(MIN(D,1000)-700,0) * 9%` |
| G | PIT — band 3 (15%) | Computed | `MAX(D-1000,0) * 15%` |
| H | Total PIT | Computed | `E + F + G` |
| I | Surtax rate | Input | `0.15` if Podgorica/Cetinje else `0.13` |
| J | Municipal surtax | Computed | `H * I` |
| K | PIO base (capped) | Computed | `MIN(D, 5730.42)` (2024 cap — confirm current year) |
| L | PIO contribution (10%) | Computed | `K * 10%` |
| M | Unemployment (0.5%) | Computed | `D * 0.5%` (full gross — see [T2-2]) |
| N | Total employee contributions | Computed | `L + M` |
| O | Net pay | Computed | `D - N - H - J` |
| P | Employer contributions (1.17%) | Computed | `D * 1.17%` |
| Q | Total employer cost | Computed | `D + P` |

Footer checks: sum of column H ties to the IOPPD income-tax line; sum of J ties to the surtax remittance; sum of L + M ties to the PIO + unemployment remittance; sum of O ties to the total net wages disbursed; sum of P ties to the employer-contribution remittance.

## Section 15 -- Montenegrin Bank Statement & Terminology Reading Guide

**Terminology Reading Guide**  _(Section 15)_

| Montenegrin term | English | Relevance |
| --- | --- | --- |
| Bruto plata / bruto zarada | Gross salary | Starting figure for all computations |
| Neto plata / neto zarada | Net salary | What the employee receives |
| Porez na dohodak fizičkih lica | Personal income tax | Withheld monthly on gross |
| Prirez | Municipal surtax | 13% (15% Podgorica/Cetinje) of assessed PIT |
| Doprinosi | Contributions | PIO + unemployment (employee); residual (employer) |
| Penziono i invalidsko osiguranje (PIO) | Pension & disability insurance | 10% employee, 0% employer |
| Osiguranje od nezaposlenosti | Unemployment insurance | 0.5% employee + 0.5% employer |
| Zdravstveno osiguranje | Health insurance | 0% / 0% — abolished |
| Fond rada | Labour Fund | 0.2% employer-only |
| Privredna komora | Chamber of Commerce | 0.27% employer-only membership contribution |
| Fond za profesionalnu rehabilitaciju / invalide | Prevention of Disability Fund | 0.2% employer-only |
| Fond PIO | Fund for Pension and Disability Insurance | Receives PIO contributions |
| Uprava prihoda i carina | Revenue and Customs Administration | Receives PIT, surtax and contributions |
| IOPPD | Integrated monthly payroll return | PIT + surtax + all contributions in one filing |
| Evropa sad 2 | "Europe Now 2.0" | The 1 Oct 2024 reform package |
| Minimalna zarada | Minimum wage | EUR 600 / EUR 800 net (dual tier) |
| JMBG | Unique personal identification number | Required for every employee |

## Section 16 -- Onboarding Fallback

When key facts are missing, ask the user these questions before computing. If a question is unanswered, apply the Section 6 conservative default and clearly flag the assumption.

1. What is the employee's **gross monthly salary** in EUR?
2. In which **municipality** does the employee reside? (Podgorica/Cetinje → 15% surtax; otherwise → 13%. If unknown → default 13% and flag it.)
3. Which **month and year** is this pay run for? (Confirms the post-1-Oct-2024 reform applies and selects the correct minimum wage / PIO ceiling.)
4. Does the gross exceed the **monthly PIO base cap** (~EUR 5,730.42)? (Triggers the contribution ceiling — confirm the current-year cap.)
5. What is the **qualification tier of the job**? (To check against the EUR 600 / EUR 800 net minimum wage.)

## Section 17 -- Interaction with Other Skills

**Interaction with Other Skills**  _(Section 17)_

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (PIT + surtax + contributions) | **This skill (montenegro-payroll.md)** |
| Montenegro personal income tax (annual / self-employment) | montenegro-income-tax.md |
| Montenegro social contributions (detailed contribution mechanics) | montenegro-social-contributions.md |
| Cross-border / posted workers / treaty coordination | cross-border-payroll-coordination.md |
| Montenegro VAT (PDV) returns | montenegro-vat.md |
| Shared workflow runbook | payroll-workflow-base.md |

### Key handoff points

- **Payroll → Bookkeeping:** Gross wages and the 1.17% employer contributions are expenses; withheld PIT, surtax and the 10.5% employee contributions are liabilities until remitted via IOPPD.
- **Payroll → Income tax:** Single-employer employees with only employment income need not file an annual PIT return; otherwise the IOPPD-reported income feeds the annual return (due 30 April).
- **Payroll → Pension:** PIO contributions paid through payroll build the employee's Fond PIO pension entitlement.

## Section 18 -- Reference Material

**Reference Material**  _(Section 18)_

| # | Source | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Montenegro — Individual — Taxes on personal income (PIT bands 0/9/15%, 15% other income, 13%/15% surtax) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/montenegro/individual/taxes-on-personal-income |
| 2 | Montenegro — Individual — Other taxes (PIO 10% employee, unemployment 0.5%/0.5%, PIO annual cap EUR 68,765) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/montenegro/individual/other-taxes |
| 3 | Montenegro — Corporate — Other taxes / Taxes on corporate income (VAT 21/15/7/0%; CIT context) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/montenegro/corporate/other-taxes |
| 4 | Montenegro Tax Card 2025 (itemised SSC table, PIT bands, CIT 9/12/15%, VAT, tax calendar, penalties) | Eurofast | https://eurofast.eu/wp-content/uploads/2025/02/MontenegroTaxCard2025.pdf |
| 5 | Amendments to the Montenegrin Labor Law and Law on Mandatory Social Security Contributions — Oct 2024 Tax Alert (PIO 20.5%→10%; min wage EUR 600/EUR 800 net; effective 1 Oct 2024) | KPMG Montenegro | https://assets.kpmg.com/content/dam/kpmg/me/pdf/2024/10/Amendments-to-the-Montenegrin-Labor-Law-and-Law-on-Mandatory-Social-Security-Contributions.pdf |
| 6 | Recent Changes in the Montenegrin Labour Regulations (Europe Now 2; dual-tier minimum wage; Oct 2024 contributions) | Karanovic & Partners | https://www.karanovicpartners.com/news/recent-changes-in-the-montenegrin-labour-regulations/ |
| 7 | Social Security Contributions – Montenegro (employee 10.5%, employer 0% + Labour Fund 0.2%; conflicting PIO cap ~EUR 54,533) | TaxRavens | https://taxravens.com/en/montenegro/social-contributions |
| 8 | IOPPD Form (integrated monthly PIT + contributions report) | Perfectum | https://www.perfectum.me/en/important-documents/ioppd-form/ |

### Primary authorities note

Primary authorities: Revenue and Customs Administration of Montenegro (https://www.upravaprihoda.gov.me/); Fund for Pension and Disability Insurance (Fond PIO); Ministry of Labour and Social Welfare. **[RESEARCH GAP — no direct primary-source (Official Gazette / upravaprihoda.gov.me) page was machine-readable in this research; figures rest on Big-4 (PwC, KPMG) and Eurofast secondary summaries and should be confirmed against the in-force legislation.]**

### Test Suite

Run these to validate any implementation of this skill. Expected results use 2025 post-reform figures (employee 10.5%, employer 1.17%, PIT 0/9/15% on gross) and the 13% default surtax unless Podgorica/Cetinje (15%) is named.

1. **Mid-low earner.** EUR 800 gross, 13% surtax. Expect: PIT EUR 9.00, surtax EUR 1.17, employee contributions EUR 84.00, net EUR 705.83, employer contributions EUR 9.36, total employer cost EUR 809.36.
2. **Higher earner, Podgorica.** EUR 1,500 gross, 15% surtax. Expect: PIT EUR 102.00, surtax EUR 15.30, employee contributions EUR 157.50, net EUR 1,225.20, employer cost EUR 1,517.55.
3. **At the 0% ceiling.** EUR 700 gross, 13% surtax. Expect: PIT EUR 0.00, surtax EUR 0.00, employee contributions EUR 73.50, net EUR 626.50, employer cost EUR 708.19.
4. **At the 9% ceiling.** EUR 1,000 gross, 13% surtax. Expect: PIT EUR 27.00, surtax EUR 3.51, employee contributions EUR 105.00, net EUR 864.49, employer cost EUR 1,011.70.
5. **High earner under the PIO cap.** EUR 3,000 gross, 13% surtax. Expect: PIT EUR 327.00, surtax EUR 42.51, employee contributions EUR 315.00, net EUR 2,315.49, employer cost EUR 3,035.10.
6. **Above the PIO cap.** EUR 6,000 gross, Podgorica (15% surtax). Expect: PIT EUR 777.00, surtax EUR 116.55, PIO base capped at EUR 5,730.42, PIO EUR 573.04, unemployment EUR 30.00 (full gross), employee contributions EUR 603.04, net EUR 4,503.41, employer cost EUR 6,070.20.
7. **Marginal-band check.** Confirm PIT is computed marginally on gross — only the slice above EUR 700 is taxed at 9%, only the slice above EUR 1,000 at 15% — and that social contributions are NOT deducted before computing PIT.
8. **Surtax-on-PIT check.** Confirm the surtax is applied to the assessed PIT amount, not to income.
9. **Stale-total check.** Confirm the implementation uses the itemised post-reform rates (employee 10.5%, employer 1.17%) and NOT Eurofast's printed 15.5% / 6.47% totals.
10. **Employer-cost check.** Confirm employer cost = gross × 1.0117 and that PIT, surtax and employee contributions are withheld from the employee (never added to employer cost).
11. **Filing check.** Confirm PIT, surtax and all contributions are reported together on a single monthly IOPPD, due by the 15th of the following month.
12. **Surtax-default check.** Municipality unknown — confirm the skill applies the 13% surtax and flags the assumption rather than guessing 15%.

## PROHIBITIONS

- NEVER deduct social contributions before computing PIT — Montenegro applies the PIT bands directly to GROSS salary.
- NEVER apply the 9% or 15% PIT rate to the whole salary — the bands are marginal; only the slice within each band is taxed at that rate.
- NEVER apply the surtax to income — it is charged on the assessed PIT amount (13% default, 15% Podgorica/Cetinje).
- NEVER use Eurofast's printed contribution totals (15.5% employee / 6.47% employer) — they are stale pre-reform aggregates; use the itemised post-reform rates (10.5% / 1.17%).
- NEVER apply a PIO employer contribution or an employee/employer health contribution — both are 0% after the 1 Oct 2024 reform.
- NEVER exceed the PIO base ceiling (~EUR 5,730.42/month, EUR 68,765/yr 2024 figure) when computing the PIO contribution — but confirm the current-year cap before relying on it.
- NEVER assume the EUR 600 / EUR 800 net minimum-wage figure without confirming the qualification tier and the current gross-up — it is a flagged RESEARCH GAP.
- NEVER quote a specific late-IOPPD penalty without confirming it — the exact payroll-penalty band is an unconfirmed RESEARCH GAP.
- NEVER file contributions separately from PIT — both go on the single monthly IOPPD to the Revenue and Customs Administration.
- NEVER present payroll computations as definitive — always label them as estimated and direct the user to a licensed Montenegrin accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax adviser in Montenegro) before implementation.

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
