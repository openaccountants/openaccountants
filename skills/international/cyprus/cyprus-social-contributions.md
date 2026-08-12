---
name: cyprus-social-contributions
description: Use this skill whenever asked about Cyprus social insurance and General Healthcare System (GHS/GESY) contributions for employees, employers, or self-employed individuals. Trigger on phrases like "how much social insurance do I pay in Cyprus", "Cyprus GESY contributions", "GHS rate", "employer on-cost Cyprus", "self-employed social insurance Cyprus", "Social Cohesion Fund", "Redundancy Fund", "HRDA contribution", "insurable earnings ceiling", "Cyprus payroll deductions", "Cyprus PAYE", or any question about Cyprus social-security or healthcare contribution obligations. Also trigger when classifying bank statement transactions that relate to Department of Social Insurance Services (Υπηρεσίες Κοινωνικών Ασφαλίσεων) debits, GHS/GESY payments, HIO (Health Insurance Organisation) payments, or government social-security remittances from Bank of Cyprus, Hellenic Bank, or other Cypriot banks. Also trigger when preparing a T.D.1 (TD1) personal income tax return where contribution deductibility or aggregate income caps are relevant. This skill covers social insurance employee/employer/self-employed rates, GHS/GESY rates across all income categories, employer-only funds (Social Cohesion, Redundancy, HRDA), insurable-earnings and GHS ceilings, payment schedule, registration, penalties, interaction with personal income tax, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Cyprus social-contribution work.
version: 0.1
jurisdiction: CY
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Christos Thoma
review_status: current
depends_on: - social-contributions-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus Social Insurance & GHS (GESY) Contributions

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Christos Thoma** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### cyprus-social-contributions

- **Employee social insurance rate** — 8.8% of insurable earnings  _(KPMG Tax Card 2025 s.3.1; PwC; Law 59(I)/2010)_
- **Employer social insurance rate** — 8.8% of insurable earnings  _(KPMG Tax Card 2025 s.3.1; PwC; Law 59(I)/2010)_
- **Self-employed social insurance rate** — 16.6% of notional insurable income  _(KPMG Tax Card 2025 s.3.1)_
- **Self-employed social insurance rate (prior, stale — do not use)** — 15.6% (applicable 2019–2023; superseded from 1 Jan 2024)  _(PwC Worldwide Tax Summaries (stale figure — use 16.6% instead))_
- **SI rate effective period** — Set 1 Jan 2024 for 5 years  _(KPMG Tax Card 2025 s.3.1)_
- **GHS rate — employee** — 2.65% of gross emoluments  _(gesy.org.cy; KPMG Tax Card 2025 s.4; Law 89(I)/2001)_
- **GHS rate — employer (on employee emoluments)** — 2.90% of employee emoluments  _(gesy.org.cy; KPMG Tax Card 2025 s.4)_
- **GHS rate — self-employed** — 4.00% of own income  _(gesy.org.cy; KPMG Tax Card 2025 s.4)_
- **GHS rate — pensioner** — 2.65%  _(gesy.org.cy; KPMG Tax Card 2025 s.4)_
- **GHS rate — person holding/exercising an office** — 2.65%  _(gesy.org.cy; KPMG Tax Card 2025 s.4)_
- **GHS rate — government / payer of officer emoluments** — 2.90%  _(gesy.org.cy; KPMG Tax Card 2025 s.4)_
- **GHS rate — income earner (rent, interest, dividends)** — 2.65%  _(gesy.org.cy; KPMG Tax Card 2025 s.4)_
- **GHS rate — State (Republic's Consolidated Fund)** — 4.70%  _(gesy.org.cy; KPMG Tax Card 2025 s.4)_
- **Social Cohesion Fund rate** — 2.0% of actual employee emoluments (no cap)  _(KPMG Tax Card 2025 s.3.3)_
- **Redundancy Fund rate** — 1.2% of insurable earnings  _(KPMG Tax Card 2025 s.3.3)_
- **HRDA / Industrial Training Fund rate** — 0.5% of insurable earnings  _(KPMG Tax Card 2025 s.3.3)_
- **Central Holiday Fund rate (where not exempt)** — 8.0% of insurable earnings  _(KPMG Tax Card 2025 s.3.3)_
- **Total employer on-cost — excluding Central Holiday Fund** — 15.40% on capped earnings (8.8% SI + 2.90% GHS + 2.0% Social Cohesion + 1.2% Redundancy + 0.5% HRDA)  _(KPMG Tax Card 2025 s.3.1, s.3.3)_
- **Total employer on-cost — including Central Holiday Fund** — 23.40% on capped earnings (15.40% + 8.0% Holiday Fund)  _(KPMG Tax Card 2025 s.3.1, s.3.3)_
- **Total employee deduction (before PAYE income tax)** — 11.45% (8.8% SI + 2.65% GHS)  _(KPMG Tax Card 2025 s.3.1; gesy.org.cy)_
- **Insurable-earnings ceiling (SI funds) — annual (2025)** — EUR 66,612/yr  _(KPMG; MLSI)_
- **Insurable-earnings ceiling (SI funds) — monthly (2025)** — EUR 5,551/mo  _(KPMG; MLSI)_
- **Insurable-earnings ceiling (SI funds) — weekly (2025)** — EUR 1,281/wk  _(KPMG; MLSI)_
- **Insurable-earnings ceiling (SI funds) — annual (2024, prior year)** — EUR 62,868/yr  _(KPMG; MLSI)_
- **GHS/GESY income cap — aggregate annual (all sources)** — EUR 180,000 aggregate annual income  _(gesy.org.cy; KPMG Tax Card 2025 s.4)_
- **Redundancy Fund ceiling** — EUR 68,904/year for 2026 (EUR 5,742/month; EUR 1,325/week). EUR 66,612/year was the 2025 ceiling.  _(https://kpmg.com/cy/en/insights/tax-alerts/amendment-to-the-maximum-amount-of-insurable-earnings-for-2026.html ; https://taxsummaries.pwc.com/cyprus/individual/other-taxes)_
- **HRDA Fund ceiling** — EUR 68,904/year for 2026 (EUR 5,742/month; EUR 1,325/week). EUR 66,612/year was the 2025 ceiling.  _(https://kpmg.com/cy/en/insights/tax-alerts/amendment-to-the-maximum-amount-of-insurable-earnings-for-2026.html ; https://taxsummaries.pwc.com/cyprus/individual/other-taxes)_
- **Central Holiday Fund ceiling** — EUR 68,904/year for 2026 (EUR 5,742/month; EUR 1,325/week). EUR 66,612/year was the 2025 ceiling.  _(https://kpmg.com/cy/en/insights/tax-alerts/amendment-to-the-maximum-amount-of-insurable-earnings-for-2026.html ; https://taxsummaries.pwc.com/cyprus/individual/other-taxes)_
- **Social Cohesion Fund ceiling** — No cap (on actual earnings)  _(KPMG Tax Card 2025 s.3.3)_
- **Band 1 — tax-free threshold** — EUR 0 – EUR 19,500 @ 0%  _(KPMG Tax Card 2025 s.1.1; Law 118(I)/2002)_
- **Band 2** — EUR 19,501 – EUR 28,000 @ 20%  _(KPMG Tax Card 2025 s.1.1)_
- **Band 3** — EUR 28,001 – EUR 36,300 @ 25%  _(KPMG Tax Card 2025 s.1.1)_
- **Band 4** — EUR 36,301 – EUR 60,000 @ 30%  _(KPMG Tax Card 2025 s.1.1)_
- **Band 5 — top rate** — Over EUR 60,000 @ 35%  _(KPMG Tax Card 2025 s.1.1)_
- **Band 1 (2026)** — EUR 0 – EUR 22,000 @ 0%  _(KPMG Tax Card 2025 s.1.1)_
- **Band 2 (2026)** — EUR 22,001 – EUR 32,000 @ 20%  _(KPMG Tax Card 2025 s.1.1)_
- **Band 3 (2026)** — EUR 32,001 – EUR 42,000 @ 25%  _(https://taxsummaries.pwc.com/cyprus/individual/taxes-on-personal-income)_
- **Band 4 (2026)** — EUR 42,001 – EUR 72,000 @ 30%  _(https://taxsummaries.pwc.com/cyprus/individual/taxes-on-personal-income)_
- **Band 5 — top rate (2026)** — Over EUR 72,000 @ 35%  _(KPMG Tax Card 2025 s.1.1)_
- **Statutory minimum wage — after 6 months continuous employment (2025)** — EUR 1,000/month  _(MLSI via Cyprus Mail, Dec 2025)_
- **Statutory minimum wage — first 6 months (2025)** — EUR 900/month  _(MLSI via Cyprus Mail, Dec 2025)_
- **Statutory minimum wage — after 6 months continuous employment (2026)** — EUR 1,088/month  _(MLSI via Cyprus Mail, Dec 2025)_
- **Statutory minimum wage — first 6 months (2026)** — EUR 979/month  _(MLSI via Cyprus Mail, Dec 2025)_
- **Employer monthly contribution return — due date** — End of the calendar month following the month contributions relate to (e.g. January contributions due by end of February)  _(MLSI Deadlines page)_
- **Self-employed quarterly SI contribution — payment timing** — Quarterly (Jan–Mar, Apr–Jun, Jul–Sep, Oct–Dec), by end of the month following each quarter  _(MLSI/secondary)_
- **Late payment surcharge — employer contributions (SI Fund & Social Cohesion Fund) — first month** — 3% of contributions due for the first month of delay  _(MLSI/KPSA)_
- **Late payment surcharge — employer contributions — each additional month** — +3% per subsequent month  _(MLSI/KPSA)_
- **Late payment surcharge — employer contributions — maximum** — 27% of contributions due (maximum)  _(MLSI/KPSA)_
- **Insurable-earnings ceiling effective date (2025 figure)** — 2 January 2025 (from 2 Jan 2025; prior 2024 figure was EUR 62,868)  _(KPMG; MLSI)_
- **Employer registration requirement** — Must register with DSI and obtain an employer registration number BEFORE employing staff; each employee must have a Social Insurance number before contributions are reported  _(MLSI)_
- **Contribution filing system** — Filed via Social Insurance Services online system (Ergani / SISnet)  _(MLSI)_
- **Currency for all contributions** — EUR only
- **Funds to which the EUR 66,612/yr ceiling applies** — For 2026, the EUR 68,904/year ceiling applies to Social Insurance, Redundancy Fund, HRDA / Industrial Training Fund and Central Holiday Fund. Social Cohesion Fund remains uncapped.  _(https://kpmg.com/cy/en/insights/tax-alerts/amendment-to-the-maximum-amount-of-insurable-earnings-for-2026.html ; https://taxsummaries.pwc.com/cyprus/individual/other-taxes)_
- **Fund to which no earnings cap applies** — Social Cohesion Fund (2.0% on actual earnings, uncapped)  _(KPMG Tax Card 2025 s.3.3)_
- **Social Insurance primary law** — Social Insurance Law of 2010, Law 59(I)/2010 (as amended)  _(Law 59(I)/2010)_
- **GHS/GESY primary law** — General Healthcare System Law of 2001, Law 89(I)/2001 (as amended)  _(Law 89(I)/2001)_
- **Income Tax primary law** — Income Tax Law of 2002, Law 118(I)/2002 (as amended)  _(Law 118(I)/2002)_
- **Special Defence Contribution law** — Special Contribution for the Defence Law, Law 117(I)/2002 (as amended)  _(Law 117(I)/2002)_
- **Insurable-earnings ceiling (SI funds) — annual (2026)** — EUR 68,904/year  _(KPMG Cyprus; PwC Worldwide Tax Summaries)_
- **Insurable-earnings ceiling (SI funds) — monthly (2026)** — EUR 5,742/month  _(KPMG Cyprus; PwC Worldwide Tax Summaries)_
- **Insurable-earnings ceiling (SI funds) — weekly (2026)** — EUR 1,325/week  _(KPMG Cyprus; PwC Worldwide Tax Summaries)_

### Social Insurance rates

- **Insurable-earnings ceiling (SI funds) — annual (2026)** — EUR 68,904/year  _(KPMG Cyprus; PwC Worldwide Tax Summaries)_
- **Insurable-earnings ceiling (SI funds) — monthly (2026)** — EUR 5,742/month  _(KPMG Cyprus; PwC Worldwide Tax Summaries)_
- **Insurable-earnings ceiling (SI funds) — weekly (2026)** — EUR 1,325/week  _(KPMG Cyprus; PwC Worldwide Tax Summaries)_

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Section 1 quick reference field table**

**Section 1 quick reference field table**

| Field | Value |
| --- | --- |
| Country | Cyprus (Republic of Cyprus) |
| Primary Legislation | Social Insurance Law of 2010 (Law 59(I)/2010, as amended) |
| Supporting Legislation | General Healthcare System Law of 2001 (Law 89(I)/2001, as amended) — GHS/GESY contributions; Income Tax Law of 2002 (Law 118(I)/2002, as amended); Special Contribution for the Defence Law (Law 117(I)/2002, as amended) |
| Social-security Authority | Ministry of Labour and Social Insurance — Department of Social Insurance Services (DSI / Υπηρεσίες Κοινωνικών Ασφαλίσεων), mlsi.gov.cy/dsi |
| Healthcare Authority | Health Insurance Organisation (HIO), gesy.org.cy |
| Tax Authority | Tax Department (Τμήμα Φορολογίας), tax.mof.gov.cy |
| Social insurance — employee | 8.8% of insurable earnings (effective 1 Jan 2024 for 5 years) [KPMG Tax Card 2025 s.3.1; PwC] |
| Social insurance — employer | 8.8% of insurable earnings [KPMG Tax Card 2025 s.3.1; PwC] |
| Social insurance — self-employed | 16.6% of notional insurable income (effective 1 Jan 2024) [KPMG Tax Card 2025 s.3.1] |
| GHS/GESY — employee | 2.65% of gross emoluments [gesy.org.cy; KPMG Tax Card 2025 s.4] |
| GHS/GESY — employer | 2.90% of employee emoluments [gesy.org.cy; KPMG Tax Card 2025 s.4] |
| GHS/GESY — self-employed | 4.00% of own income [gesy.org.cy; KPMG Tax Card 2025 s.4] |
| Insurable-earnings ceiling (SI funds) 2025 | EUR 66,612/yr (EUR 5,551/mo; EUR 1,281/wk), from 2 Jan 2025 [KPMG; MLSI] |
| GHS/GESY income ceiling | EUR 180,000 aggregate annual income across all sources [gesy.org.cy; KPMG Tax Card 2025 s.4] |
| Payment frequency (employers) | Monthly [MLSI Deadlines page] |
| Payment frequency (self-employed) | Quarterly [MLSI/secondary] |
| Deadline (employer monthly) | End of the calendar month following the month contributions relate to [MLSI Deadlines page] |
| Currency | EUR only |
| Validated by | Pending — requires sign-off by a Cyprus-qualified accountant |
| Validation date | Verified by Christos Thoma (ACA (ICAEW)) on 2026-06-10 |

**Contribution overview (2025)**

| Contribution | Employee | Employer | Self-employed | Ceiling |
| --- | --- | --- | --- | --- |
| Social Insurance | 8.8% | 8.8% | 16.6% | EUR 66,612/yr [KPMG Tax Card 2025 s.3.1] |
| GHS/GESY | 2.65% | 2.90% | 4.00% | EUR 180,000/yr aggregate [gesy.org.cy; KPMG s.4] |
| Social Cohesion Fund | — | 2.0% | — | No cap (on actual earnings) [KPMG Tax Card 2025 s.3.3] |
| Redundancy Fund | — | 1.2% | — | EUR 68,904/yr [KPMG Tax Card 2025 s.3.3] |
| HRDA / Industrial Training Fund | — | 0.5% | — | EUR 68,904/yr [KPMG Tax Card 2025 s.3.3] |
| Central Holiday Fund | — | 8.0% (if not exempt) | — | EUR 68,904/yr [KPMG Tax Card 2025 s.3.3] |

- **Employer-side totals (verify the column sums)** — SI 8.8% + GHS 2.90% + Redundancy 1.2% + HRDA 0.5% = 13.40% on capped earnings, plus Social Cohesion 2.0% on uncapped gross = 15.40% on capped earnings; where the Central Holiday Fund applies, add 8.0% for a total of 23.40% on capped earnings. Arithmetic: 8.8 + 2.90 + 1.2 + 0.5 = 13.40; + 2.0 = 15.40; + 8.0 = 23.40.  _(KPMG Tax Card 2025 s.3.1, s.3.3)_

The State (Republic's Consolidated Fund) also contributes to the system. The research underpinning this skill confirms a **4.70%** State GHS rate on salaries/pensions/other income [gesy.org.cy; KPMG s.4]; it does NOT establish an authoritative State percentage for the Social Insurance Fund. Any "total SI funding" figure that adds a State share to the Social Insurance Fund (e.g. a 22.8% employer+employee+state total) is **[RESEARCH GAP — reviewer to confirm exact State contribution split to the Social Insurance Fund with DSI]**; do not rely on it for computation.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown employment status | Ask — do not assume; employee, employer, self-employed and office-holder rates differ materially. If forced, assume employee (employer withholds SI 8.8% + GHS 2.65%) [KPMG s.3.1; gesy.org.cy] |
| Unknown self-employed SI rate | Apply 16.6% (KPMG Tax Card 2025 — NOT the stale 15.6% still shown on PwC's other-taxes table) [KPMG Tax Card 2025 s.3.1] |
| Earnings above EUR 66,612 | Cap SI / Redundancy / HRDA / Holiday Fund at EUR 66,612; do NOT cap Social Cohesion (uncapped) [KPMG s.3.3] |
| Central Holiday Fund inclusion | Assume payable at 8.0% unless the employer evidences an approved private leave-scheme exemption; most established employers are exempt, so confirm status [KPMG s.3.3] |
| Unknown minimum wage applied | Apply EUR 1,000/month (after 6 months of continuous employment) [MLSI via Cyprus Mail, Dec 2025] |
| Unknown whether first 6 months | Use EUR 1,000/month; apply EUR 900/month only if first-6-months status confirmed [MLSI via Cyprus Mail, Dec 2025] |
| Unknown GHS scope on income | Apply 2.65% to rent/interest/dividend income up to the EUR 180,000 aggregate cap [gesy.org.cy] |
| Unknown whether DSI debit is contribution or surcharge | Classify as contribution; flag for reviewer |
| Unknown tax year | Default to 2025; flag that materially different rules apply from 1 Jan 2026 (see Rule 7 note) [KPMG s.1.1] |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable** — employment status (employee / employer / self-employed) and gross or insurable earnings. Without an earnings figure and status, STOP. Do not compute contributions.
- **Recommended** — monthly/annual gross emoluments, whether earnings exceed the EUR 66,612 insurable-earnings ceiling, whether aggregate income approaches the EUR 180,000 GHS cap, and (for self-employed) the occupational category used for the minimum insurable amount.
- **Ideal** — DSI annual statement, HIO/GESY contribution records, payroll register, bank statements showing monthly SI/GHS remittances, and the prior-year T.D.1 return.

### Refusal catalogue

- **R-CY-SC-1 -- Self-employed minimum insurable amount unknown** — Trigger: self-employed contribution requested without the occupational category. Message: "Self-employed social insurance is computed on notional (minimum) insurable amounts set quarterly by DSI per occupational category, not on actual declared income unless higher. The 2025 quarterly minimum insurable amounts per category were not enumerated in this skill. [RESEARCH GAP] Confirm the client's occupational category and the relevant DSI quarterly figure before computing."
- **R-CY-SC-2 -- Contribution arrears / surcharge computation** — Trigger: client has unpaid employer contributions from prior periods. Message: "Late employer contributions carry a surcharge of 3% for the first month, increasing by 3% per additional month, up to a maximum of 27% of contributions due. Do not attempt to quantify arrears without a DSI statement. Escalate to a Cyprus-qualified accountant."
- **R-CY-SC-3 -- Special Defence Contribution (SDC) and domicile** — Trigger: client asks about tax on dividends/interest/rents or non-domiciled status. Message: "SDC on passive income is OUTSIDE the scope of this contributions skill and its underlying 2025 research; specific SDC rates and the reported 1 Jan 2026 SDC reform were NOT confirmed from a primary authority here. [RESEARCH GAP] What IS established: GHS at 2.65% applies on rent/interest/dividend income up to the EUR 180,000 aggregate cap regardless of domicile [gesy.org.cy]. Domicile determination and any SDC liability require case-specific confirmation — escalate to a Cyprus-qualified accountant."
- **R-CY-SC-4 -- Personal income tax penalties/interest** — Trigger: client asks for late-filing or late-payment income tax penalties. Message: "Specific 2025/2026 personal income tax late-filing penalty and statutory interest figures were not confirmed from a primary authority in this research. [RESEARCH GAP] Verify directly with the Tax Department before quoting any figure."
- **R-CY-SC-5 -- Income tax bracket year ambiguity** — Trigger: tax year not stated, or computation spans 2025/2026. Message: "This skill is scoped to tax year 2025. From 1 Jan 2026 the personal income tax brackets change (0% to 22,000 / 20% to 32,000 / 25% to 42,000 / 30% to 72,000 / 35% above 72,000) [KPMG Tax Card 2025 s.1.1] and the minimum wage rises to EUR 979 / EUR 1,088 [MLSI via Cyprus Mail, Dec 2025]. The 2026 insurable-earnings ceiling was not established in this research [RESEARCH GAP]. Confirm the tax year before computing."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Cyprus social contributions. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Social insurance and GHS payments always EXCLUDE from any VAT return or revenue/expense classification at the individual level — they are statutory obligations. For an employer, the employer's own SI/GHS/fund contributions ARE deductible payroll on-costs; the employee's withheld share is part of gross payroll, not an extra cost.

### 3.1 Department of Social Insurance Services (SI) remittances

**DSI remittance patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DEPARTMENT OF SOCIAL INSURANCE, DSI | EXCLUDE -- social insurance remittance | Monthly employer remittance or self-employed quarterly |
| SOCIAL INSURANCE, SOC INS | EXCLUDE -- social insurance | Same |
| ΥΠΗΡΕΣΙΕΣ ΚΟΙΝΩΝΙΚΩΝ ΑΣΦΑΛΙΣΕΩΝ | EXCLUDE -- social insurance | Greek-language reference |
| ΚΟΙΝΩΝΙΚΕΣ ΑΣΦΑΛΙΣΕΙΣ | EXCLUDE -- social insurance | Greek-language reference |
| SI CONTRIB, KOINONIKES ASFALISEIS | EXCLUDE -- social insurance | Transliterated reference |

### 3.2 GHS / GESY (Health Insurance Organisation) remittances

**GHS/GESY remittance patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GHS, GESY, GENERAL HEALTHCARE | EXCLUDE -- GHS/GESY contribution | Healthcare system contribution |
| HIO, HEALTH INSURANCE ORGANISATION | EXCLUDE -- GHS/GESY | Administering body |
| ΓΕΣΥ, ΓΕΝΙΚΟ ΣΥΣΤΗΜΑ ΥΓΕΙΑΣ | EXCLUDE -- GHS/GESY | Greek-language reference |
| ΟΡΓΑΝΙΣΜΟΣ ΑΣΦΑΛΙΣΗΣ ΥΓΕΙΑΣ | EXCLUDE -- GHS/GESY | HIO in Greek |

### 3.3 Employer-only fund references (may appear bundled with SI)

**Employer-only fund patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SOCIAL COHESION, COHESION FUND | EXCLUDE -- employer Social Cohesion Fund (2.0%, uncapped) | Employer-only |
| REDUNDANCY FUND | EXCLUDE -- employer Redundancy Fund (1.2%, capped) | Employer-only |
| HRDA, HRDC, INDUSTRIAL TRAINING | EXCLUDE -- employer HRDA Fund (0.5%, capped) | Employer-only |
| Bundled "SOCIAL INSURANCE + FUNDS" lump sum | EXCLUDE -- combined employer remittance | Split by reviewer if breakdown needed |

### 3.4 Income tax payments (NOT contributions -- do not confuse)

**Income tax patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TAX DEPARTMENT, ΤΜΗΜΑ ΦΟΡΟΛΟΓΙΑΣ | EXCLUDE -- income tax, not a contribution | PAYE / income tax payment |
| PAYE, T.D.1, TD1 | EXCLUDE -- income tax withholding/assessment | Not SI or GHS |
| SDC, DEFENCE CONTRIBUTION, ΑΜΥΝΑ | EXCLUDE -- Special Defence Contribution | Separate from SI/GHS |

### 3.5 Salary and payroll (exclude from contribution classification)

**Salary/payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, MISTHOS, ΜΙΣΘΟΣ (outgoing) | EXCLUDE -- payroll expense | Not a contribution payment |
| SALARY, ΜΙΣΘΟΣ (incoming) | EXCLUDE -- employment income received | Not a contribution payment |

### 3.6 Benefits received (not contributions paid)

**Benefits received patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DSI PENSION, ΣΥΝΤΑΞΗ | EXCLUDE -- pension/benefit received | Not a contribution payment |
| UNEMPLOYMENT BENEFIT, SICKNESS BENEFIT | EXCLUDE -- benefit received | Not a contribution payment |

## Section 4 -- Worked examples

Six bank statement / payroll classifications showing Cyprus contribution transactions from a hypothetical Limassol-based software consultancy and its staff. All amounts in EUR.

### Example 1 -- Standard employee monthly deduction (mid-range salary)

**Input line (payroll):**
`Employee gross EUR 3,000/month`

**Reasoning:**
Below all ceilings (annual EUR 36,000 < EUR 66,612 SI cap and < EUR 180,000 GHS cap). Employee deduction = 8.8% SI + 2.65% GHS = 11.45% x EUR 3,000 = **EUR 343.50/month** (EUR 264.00 SI + EUR 79.50 GHS) before PAYE income tax. Employer on-cost (excl. Holiday Fund) = 8.8% + 2.9% + 2.0% + 1.2% + 0.5% = 15.4% x EUR 3,000 = **EUR 462.00/month**. If the employer is NOT exempt from the Central Holiday Fund, add 8.0% x EUR 3,000 = EUR 240.00, giving **EUR 702.00/month** (23.4%). Most established employers are exempt — confirm status. [KPMG Tax Card 2025 s.3.1, s.3.3]

**Classification:** EXCLUDE -- statutory contributions. Employee 11.45% withheld; employer 15.4% (or 23.4% incl. Holiday Fund) on-cost is a deductible payroll expense.

### Example 2 -- High earner hitting the insurable-earnings ceiling

**Input line (payroll):**
`Employee gross EUR 7,000/month (EUR 84,000/yr)`

**Reasoning:**
Annual gross EUR 84,000 exceeds the SI ceiling of EUR 66,612 but is below the EUR 180,000 GHS cap. SI is capped: employee SI = 8.8% x EUR 66,612/12 = 8.8% x EUR 5,551 = **EUR 488.49/month**. GHS is NOT capped here (gross < EUR 180,000): employee GHS = 2.65% x EUR 7,000 = **EUR 185.50/month**. Employer SI capped at EUR 5,551; employer Redundancy (1.2%) and HRDA (0.5%) and Holiday Fund (8.0%, if not exempt) also capped at EUR 5,551; Social Cohesion (2.0%) applies to the FULL EUR 7,000 (uncapped); employer GHS (2.9%) on full EUR 7,000. [KPMG Tax Card 2025 s.3.1, s.3.3; gesy.org.cy]

**Classification:** EXCLUDE -- statutory contributions. SI/Redundancy/HRDA/Holiday Fund capped at the insurable-earnings ceiling; GHS (to EUR 180,000) and Social Cohesion (uncapped) on actual earnings.

### Example 3 -- Self-employed quarterly social insurance debit (Bank of Cyprus)

**Input line:**
`30.04.2025 ; DEPARTMENT OF SOCIAL INSURANCE ; DEBIT ; Q1 2025 SELF EMPLOYED ; -1,200.00 ; EUR`

**Reasoning:**
Matches "DEPARTMENT OF SOCIAL INSURANCE" (pattern 3.1). Self-employed SI rate is 16.6% for 2025 on the notional insurable amount for the occupational category. EUR 1,200/quarter implies an annual SI of EUR 4,800, i.e. a notional insurable income of approximately EUR 28,915 (EUR 4,800 / 16.6%). The exact category figure must be confirmed against the DSI quarterly schedule. **[RESEARCH GAP — quarterly minimum insurable amounts per category not enumerated.]**

**Classification:** EXCLUDE -- self-employed social insurance. Flag the occupational-category figure for reviewer confirmation.

### Example 4 -- GHS / GESY remittance (Hellenic Bank)

**Input line:**
`31.05.2025 ; GESY HIO ; DEBIT ; GENERAL HEALTHCARE CONTRIB MAY ; -560.00 ; EUR`

**Reasoning:**
Matches "GESY HIO" (pattern 3.2). This is a GHS/GESY contribution. For an employer this bundles employee 2.65% (withheld) and employer 2.9%; for a self-employed person it would be 4.00% on own income. Subject to the single EUR 180,000 aggregate annual income cap.

**Classification:** EXCLUDE -- GHS/GESY contribution. Employer share deductible; employee share part of gross payroll.

### Example 5 -- Tax Department payment (NOT a contribution)

**Input line:**
`30.06.2025 ; TAX DEPARTMENT ; DEBIT ; PAYE JUN 2025 ; -2,100.00 ; EUR`

**Reasoning:**
Matches "TAX DEPARTMENT" (pattern 3.4). This is PAYE income tax withheld and remitted, NOT a social insurance or GHS contribution. Do not classify as a contribution.

**Classification:** EXCLUDE -- income tax (PAYE). NOT a social/health contribution.

### Example 6 -- Ambiguous DSI debit (surcharge or arrears)

**Input line:**
`15.09.2025 ; DEPARTMENT OF SOCIAL INSURANCE ; DEBIT ; ARREARS / SURCHARGE ; -3,810.00 ; EUR`

**Reasoning:**
Matches "DEPARTMENT OF SOCIAL INSURANCE" (pattern 3.1) but the amount is irregular and the reference says "ARREARS / SURCHARGE." Late employer contributions attract a 3% first-month surcharge increasing 3% per month up to 27%. Cannot separate contribution principal from surcharge without a DSI statement. Flag for reviewer.

**Classification:** EXCLUDE from VAT. Flag for reviewer — request a DSI breakdown to split contribution principal from the late-payment surcharge.

## Section 5 -- Tier 1 rules

These rules apply when payroll/bank statement data is clear and all required inputs are available. Apply exactly as written. All figures are tax year 2025.

### Rule 1 -- Employee/employer social insurance rate

- **Employee SI rate** — 8.8%  _(Rate set 1 Jan 2024 for 5 years)_
- **Employer SI rate** — 8.8%  _(Rate set 1 Jan 2024 for 5 years)_
- **Insurable-earnings ceiling** — EUR 66,612/yr; EUR 5,551/mo; EUR 1,281/wk  _(Rate set 1 Jan 2024 for 5 years)_
- **SI computation formula** — Employee SI  = min(gross, 66,612) x 8.8% Employer SI  = min(gross, 66,612) x 8.8%

### Rule 2 -- Self-employed social insurance rate

- **Self-employed SI rate 2025** — 16.6%  _(up from 15.6% in 2019-2023, effective 1 Jan 2024)_
- **Self-employed SI base and cap** — On notional/minimum insurable income by occupational category (set quarterly by DSI), capped at EUR 66,612/yr. Use 16.6% — do NOT use the 15.6% still shown on PwC Worldwide Tax Summaries (reviewed 18 May 2026).  _(**[RESEARCH GAP — reviewer to reconfirm against latest DSI circular.]**)_

### Rule 3 -- GHS / GESY rates and single aggregate cap

**GHS rate table**  _([gesy.org.cy; KPMG Tax Card 2025 s.4])_

| Category | GHS rate |
| --- | --- |
| Employee | 2.65% |
| Employer (on employee emoluments) | 2.90% |
| Self-employed | 4.00% |
| Pensioner | 2.65% |
| Person holding/exercising an office | 2.65% |
| Government / payer of officer emoluments | 2.90% |
| Income earner (rent, interest, dividends) | 2.65% |
| State (Republic's Consolidated Fund) | 4.70% |

- **GHS aggregate annual income cap** — EUR 180,000  _([gesy.org.cy; KPMG Tax Card 2025 s.4])_

### Rule 4 -- Employer-only funds

**Employer-only funds table**  _([KPMG s.3.3])_

| Fund | Rate | Base | Ceiling |
| --- | --- | --- | --- |
| Social Cohesion Fund | 2.0% | Actual employee emoluments | No cap [KPMG s.3.3] |
| Redundancy Fund | 1.2% | Insurable earnings | EUR 66,612/yr [KPMG s.3.3] |
| HRDA / Industrial Training | 0.5% | Insurable earnings | EUR 66,612/yr [KPMG s.3.3] |
| Central Holiday Fund | 8.0% (if not exempt) | Insurable earnings | EUR 66,612/yr [KPMG s.3.3] |

- **Central Holiday Fund exemption** — The Central Holiday Fund is payable unless the employer operates an approved private holiday/leave scheme and is formally exempt. Most established employers are exempt — confirm status before including it.  _([KPMG Tax Card 2025 s.3.3])_

### Rule 5 -- Total on-cost and total deduction

- **Total employer on-cost (excl Holiday)** — 15.40% above gross (8.8% SI + 2.9% GHS + 2.0% Social Cohesion + 1.2% Redundancy + 0.5% HRDA)  _([KPMG s.3.1, s.3.3; gesy.org.cy])_
- **Total employer on-cost (incl Holiday)** — 23.40% (add 8.0% Central Holiday Fund)  _([KPMG s.3.1, s.3.3; gesy.org.cy])_
- **Total employee deduction** — 11.45% (8.8% SI + 2.65% GHS) before PAYE income tax  _([KPMG s.3.1, s.3.3; gesy.org.cy])_
- **Arithmetic check and differing ceilings** — Arithmetic: 8.8 + 2.9 + 2.0 + 1.2 + 0.5 = 15.40; + 8.0 = 23.40; 8.8 + 2.65 = 11.45. Remember the differing ceilings: SI/Redundancy/HRDA/Holiday cap at EUR 66,612; GHS caps at EUR 180,000; Social Cohesion is uncapped.  _([KPMG s.3.1, s.3.3; gesy.org.cy])_

### Rule 6 -- Which base is capped where

- **Capped at EUR 68,904/yr group** — Capped at EUR 68,904/yr: Social Insurance (employee, employer, self-employed), Redundancy Fund, HRDA / Industrial Training Fund, Central Holiday Fund. Social Cohesion Fund is uncapped.  _([KPMG s.3.1, s.3.3])_
- **Capped at EUR 180,000/yr aggregate** — Capped at EUR 180,000/yr aggregate: GHS/GESY (all categories).  _([gesy.org.cy])_
- **No cap** — No cap: Social Cohesion Fund (2.0% on actual earnings).  _([KPMG s.3.3])_

### Rule 7 -- Personal income tax brackets (tax year 2025)

**Personal income tax brackets 2025**  _(KPMG Tax Card 2025 s.1.1)_

| Band | Rate |
| --- | --- |
| EUR 0 – EUR 19,500 | 0% (tax-free threshold) |
| EUR 19,501 – EUR 28,000 | 20% |
| EUR 28,001 – EUR 36,300 | 25% |
| EUR 36,301 – EUR 60,000 | 30% |
| over EUR 60,000 | 35% |

- **2026 bracket change (not for 2025)** — From 1 Jan 2026 the brackets change to 0% to 22,000 / 20% to 32,000 / 25% to 42,300 / 30% to 72,000 / 35% above 72,000 — not relevant for 2025 payroll.  _([KPMG Tax Card 2025 s.1.1])_

### Rule 8 -- Withholding method (PAYE)

- **PAYE withholding** — Employers withhold personal income tax monthly under PAYE and remit to the Tax Department. The employer also withholds the employee SI (8.8%) and GHS (2.65%) shares and remits them together with its own contributions.

### Rule 9 -- Employer payment schedule

- **Employer contribution due date** — Monthly SI, GHS, Social Cohesion, Redundancy and HRDA contributions are due by the end of the calendar month following the month they relate to (e.g. January contributions due by end of February).

### Rule 10 -- Self-employed payment schedule

- **Self-employed contribution schedule** — Self-employed social insurance is paid quarterly, by deadlines published by DSI, based on minimum insurable amounts per occupational category for each quarter of 2025.

### Rule 11 -- Employer registration and new-hire notification

- **Employer registration requirement** — Employers must register with the Department of Social Insurance Services and obtain an employer registration number BEFORE employing staff; each employee needs a Social Insurance number before contributions are reported. Contributions are filed via the Social Insurance Services online system (Ergani / SISnet).  _([MLSI])_
- **Registration form/timing gap** — The specific registration form number and the exact new-hire notification timing were not confirmed from a primary authority in this research.  _(**[RESEARCH GAP — reviewer to confirm the registration form and Ergani new-hire notification deadline with DSI]**)_

### Rule 12 -- Minimum wage (2025)

- **Minimum wage 2025 and 2026** — EUR 1,000/month for full-time employees after completing 6 months of continuous employment; EUR 900/month during the first 6 months. (Rises to EUR 1,088 / EUR 979 respectively from 1 Jan 2026.)  _([MLSI decision reported by Cyprus Mail, Dec 2025])_

## Section 6 -- Tier 2 catalogue

When payroll/bank statement data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- State contribution split / Central Holiday Fund

- **Trigger/Issue/Action** — Trigger: Client or modelling asks for the full SI funding picture including the State share, or for the total employer cost where the Holiday Fund may apply. Issue: The research underpinning this skill establishes a 4.70% State GHS rate [gesy.org.cy] but NOT an authoritative State percentage for the Social Insurance Fund. Separately, the Central Holiday Fund (8.0%) changes the employer total from 15.40% to 23.40% of capped earnings and applies only where the employer is not exempt. Action: Flag for reviewer. Confirm the exact State split to the Social Insurance Fund with DSI [RESEARCH GAP], and confirm Holiday Fund exemption status, before relying on a total-cost figure.  _([gesy.org.cy])_

### T2-2 -- Self-employed occupational category and minimum insurable amount

- **Trigger/Issue/Action** — Trigger: Self-employed client without a confirmed occupational category. Issue: SI is computed on notional minimum insurable amounts per occupational category, set quarterly by DSI, capped at EUR 66,612. The 2025 quarterly figures per category were not enumerated in this skill. Action: Flag for reviewer. Obtain the DSI quarterly schedule and the client's category before computing.

### T2-3 -- Aggregate GHS cap across multiple income sources

- **Trigger/Issue/Action** — Trigger: Client has employment plus pension, self-employment, dividends, interest, or rents. Issue: GHS applies on aggregate income from ALL sources up to a single EUR 180,000 cap. Multiple payers may each withhold without seeing the aggregate, causing over- or under-contribution. Action: Flag for reviewer to reconcile aggregate GHS against the EUR 180,000 cap.

### T2-4 -- Non-domiciled status and SDC

- **Trigger/Issue/Action** — Trigger: Client receives dividends, interest, or rents and may be non-domiciled. Issue: SDC rates and the reported 1 Jan 2026 SDC reform are OUTSIDE the scope of this contributions skill and were not confirmed from a primary authority [RESEARCH GAP]. What IS established: GHS at 2.65% applies on rent/interest/dividend income up to the EUR 180,000 aggregate cap regardless of domicile [gesy.org.cy]. Action: Flag for reviewer. Do not apply or omit SDC without confirming domicile and the current SDC rules with a Cyprus-qualified accountant.  _([gesy.org.cy])_

### T2-5 -- Contribution arrears and surcharges

- **Trigger/Issue/Action** — Trigger: Client has unpaid employer contributions from prior periods. Issue: Late employer contributions (Social Insurance Fund and Social Cohesion Fund) carry a surcharge of 3% for the first month, +3% per additional month, up to a maximum of 27% of contributions due. Action: Do not attempt to quantify arrears without a DSI statement. Escalate to a Cyprus-qualified accountant.

### T2-6 -- 2025 vs 2026 scope

- **Trigger/Issue/Action** — Trigger: Computation spans the 2025/2026 boundary or the year is unstated. Issue: From 1 Jan 2026: new income tax brackets (0% to 22,000 / 20% to 32,000 / 25% to 42,300 / 30% to 72,000 / 35% above 72,000) [KPMG s.1.1] and a higher minimum wage (EUR 979 / EUR 1,088) [MLSI via Cyprus Mail, Dec 2025]. A reported SDC reform and any 2026 insurable-earnings ceiling were NOT established in this research [RESEARCH GAP]. Action: Flag for reviewer. Confirm the applicable tax year and the 2026 figures before computing.  _([KPMG s.1.1]; [MLSI via Cyprus Mail, Dec 2025])_

## Section 7 -- Excel working paper template

When producing a Cyprus contributions computation, structure the working paper as follows:

```
CYPRUS SOCIAL CONTRIBUTIONS COMPUTATION -- WORKING PAPER
Client: [name]
Tax Year: 2025
Prepared: [date]

INPUT DATA
  Employment status:             [Employee / Employer / Self-employed]
  Monthly gross emoluments:      EUR [____]
  Annual gross emoluments:       EUR [____]
  Exceeds EUR 66,612 SI ceiling: [YES/NO]
  Aggregate income (GHS):        EUR [____]
  Exceeds EUR 180,000 GHS cap:   [YES/NO]
  Occupational category (SE):    [____]  (DSI quarterly minimum insurable amount)

EMPLOYEE DEDUCTIONS (per month)
  Social Insurance 8.8%:         EUR [____]  (base = min(gross, 5,551))
  GHS/GESY 2.65%:                EUR [____]  (base = min(gross, 180,000/12))
  Total employee deduction:      EUR [____]  (11.45% before PAYE)

EMPLOYER ON-COSTS (per month)
  Social Insurance 8.8%:         EUR [____]  (capped at 5,551)
  GHS/GESY 2.90%:                EUR [____]  (capped at 180,000/12)
  Social Cohesion 2.0%:          EUR [____]  (NO cap — actual earnings)
  Redundancy 1.2%:               EUR [____]  (capped at 5,551)
  HRDA 0.5%:                     EUR [____]  (capped at 5,551)
  Central Holiday Fund 8.0%:     EUR [____]  (capped at 5,551; only if NOT exempt)
  Total employer on-cost:        EUR [____]  (15.40% excl Holiday / 23.40% incl Holiday)

SELF-EMPLOYED (if applicable)
  Notional insurable income:     EUR [____]  (per DSI category, capped 66,612)
  Social Insurance 16.6%:        EUR [____]
  GHS/GESY 4.00%:                EUR [____]
  Quarterly SI payment:          EUR [____]

PAYMENT SCHEDULE
  Employer monthly remittance:   due end of following month
  Self-employed quarterly:       per DSI published deadlines

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How Cyprus contribution debits appear on bank statements

**Bank of Cyprus:**
- Description: "DEPARTMENT OF SOCIAL INSURANCE", "SOCIAL INSURANCE", "GESY", "HIO"
- Timing: Monthly for employers (end of following month); quarterly for self-employed
- Amount: Monthly employer remittance bundles SI + GHS + Social Cohesion + Redundancy + HRDA

**Hellenic Bank:**
- Description: "SOC INS", "GESY HIO", "GENERAL HEALTHCARE"
- Timing: Same monthly/quarterly cycle
- Amount: May appear as separate SI and GHS lines or as a bundled remittance

**Astrobank / Eurobank Cyprus / Alpha Bank Cyprus:**
- Description: "SOCIAL INSURANCE", "GESY", or Greek-language references (ΚΟΙΝΩΝΙΚΕΣ ΑΣΦΑΛΙΣΕΙΣ, ΓΕΣΥ)
- Timing: Same cycle

**Key identification tips:**
1. Contribution debits are always outgoing (DEBIT), never credits — incoming DSI credits are benefits/pensions received.
2. Employer remittances recur monthly with amounts tracking total payroll.
3. Distinguish SI (capped at EUR 66,612) from GHS (capped at EUR 180,000) from Social Cohesion (uncapped) when a breakdown is needed.
4. Do not confuse Tax Department / PAYE / SDC debits (income tax) with SI or GHS contributions.
5. Arrears/surcharge payments may appear as irregular lump sums with "ARREARS" or "SURCHARGE" in the reference.

### Greek-language terminology

**Greek-language terminology table**

| Greek term | Meaning |
| --- | --- |
| Κοινωνικές Ασφαλίσεις | Social Insurance |
| Υπηρεσίες Κοινωνικών Ασφαλίσεων | Department of Social Insurance Services (DSI) |
| ΓΕΣΥ / Γενικό Σύστημα Υγείας | GHS / General Healthcare System (GESY) |
| Οργανισμός Ασφάλισης Υγείας | Health Insurance Organisation (HIO) |
| Τμήμα Φορολογίας | Tax Department |
| Μισθός | Salary |
| Σύνταξη | Pension |
| Άμυνα | Defence (SDC) |

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for contribution debits** -- identify all outgoing payments matching Section 3 patterns (DSI, GESY/HIO, Social Cohesion/Redundancy/HRDA).
2. **Separate SI from GHS from employer funds** -- where the bank shows separate lines, tag each; where bundled, note that a breakdown is required.
3. **Reverse-engineer the profile:**
   - Monthly recurring DSI + GESY debits → employer or employee withholding profile; estimate gross from the 11.45% / 15.4% ratios.
   - Quarterly DSI debits with no GESY-employer line → likely self-employed (SI 16.6%, GHS 4.00%).
   - Debits exceeding the 8.8% x EUR 5,551 monthly SI cap signal a high earner above the insurable-earnings ceiling.
4. **Flag for reviewer:** "Contribution classification derived from bank statement amounts only. Employment status, occupational category, and aggregate income have not been independently verified. Reviewer must confirm before filing T.D.1 or relying on these figures."

## Section 10 -- Reference material

### Illustrative computations (2025)

- **Employer on-cost note** — Employer on-cost shown at 15.4% (excludes the Central Holiday Fund); add 8.0% of capped earnings where the employer is not exempt (23.4% total).  _([KPMG s.3.1, s.3.3])_

**Illustrative computations table**

| Profile | Monthly gross | Employee deduction (11.45%) | Employer on-cost (15.4%, excl. Holiday) | Notes |
| --- | --- | --- | --- | --- |
| Employee, mid salary | EUR 2,000 | EUR 229.00 | EUR 308.00 | Below all ceilings |
| Employee, mid salary | EUR 3,000 | EUR 343.50 | EUR 462.00 | Below all ceilings |
| Employee, high earner | EUR 7,000 | EUR 673.99 | see Example 2 | SI capped at EUR 5,551; GHS/Cohesion on actual |
| Self-employed | notional EUR 28,915/yr | SI 16.6% = EUR 4,800/yr | — | GHS 4.00% additionally; category-dependent [KPMG s.3.1] |

(High-earner employee deduction = EUR 488.49 SI capped + EUR 185.50 GHS = EUR 673.99. Check: 2,000 × 0.1145 = 229.00 and × 0.154 = 308.00; 3,000 × 0.1145 = 343.50 and × 0.154 = 462.00.)

### Special Defence Contribution (SDC) — passive income

- **SDC scope and GHS on passive income** — SDC rates and the reported 1 Jan 2026 SDC reform are OUTSIDE the scope of this contributions skill and were NOT confirmed from a primary authority in this research **[RESEARCH GAP — verify SDC rates and reform with a Cyprus-qualified accountant / the Tax Department]**. What IS established for contributions: GHS at 2.65% applies on rent/interest/dividend income up to the EUR 180,000 aggregate cap, regardless of domicile.  _([gesy.org.cy; KPMG s.4])_

### Key thresholds

**Key thresholds table**

| Threshold | Value | Source |
| --- | --- | --- |
| Insurable-earnings ceiling (SI funds) 2025 | EUR 66,612/yr; EUR 5,551/mo; EUR 1,281/wk (from 2 Jan 2025; was EUR 62,868 in 2024) | [KPMG; MLSI] |
| GHS/GESY income cap | EUR 180,000 aggregate annual income | [gesy.org.cy; KPMG s.4] |
| Social Cohesion Fund cap | No ceiling (full actual earnings) | [KPMG s.3.3] |
| Personal income tax tax-free threshold | EUR 19,500/yr | [KPMG s.1.1] |
| Statutory minimum wage 2025 | EUR 900/mo first 6 months, EUR 1,000/mo thereafter | [MLSI via Cyprus Mail, Dec 2025] |
| Statutory minimum wage 2026 (context) | EUR 979 / EUR 1,088 | [MLSI via Cyprus Mail, Dec 2025] |
| 2026 insurable-earnings ceiling | Not confirmed in this research | **[RESEARCH GAP]** |

### Forms

**Forms table**

| Form / filing | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Monthly contribution return (employers) | Declaration and payment of employer+employee SI, GHS, Social Cohesion, Redundancy, HRDA (and Holiday Fund where applicable), filed via the Social Insurance Services online system (Ergani / SISnet) | End of the calendar month following the month contributions relate to | [MLSI Deadlines page] |
| Self-employed quarterly contribution | Payment of self-employed SI (16.6%) and GHS (4.0%) on notional insurable income | Quarterly (Jan–Mar, Apr–Jun, Jul–Sep, Oct–Dec), by the end of the month following each quarter | [MLSI/secondary] |
| Employer registration (DSI) | Register and obtain an employer registration number; employees registered for a Social Insurance number | On commencement of employing staff | [MLSI] |
| T.D.1 (personal income tax) | Annual personal income tax self-assessment (PAYE context) | Annual filing deadline NOT confirmed in this research | **[RESEARCH GAP — verify with the Tax Department]** |
| Registration form number / new-hire notification timing | Specific DSI registration form and Ergani new-hire notification deadline | Not confirmed in this research | **[RESEARCH GAP — verify with DSI]** |

### Penalties

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| Late payment of employer contributions (SI Fund & Social Cohesion Fund) | Additional charge of 3% for the first month of delay, +3% per subsequent month, up to a maximum of 27% of contributions due | [MLSI/KPSA — reviewer to re-confirm against live MLSI page] |
| Failure / late registration | Administrative penalties apply; employer remains liable for unpaid contributions plus the late-payment additional charge | [MLSI] |
| Late filing / late payment of income tax | General Tax Department penalties and statutory interest apply; specific 2025/2026 figures NOT confirmed from an official source | **[RESEARCH GAP — verify with the Tax Department]** |

### Sources

- KPMG Limited (Cyprus), *Cyprus Tax Card 2025* (April 2025) — s.1.1 PIT bands, s.3 Social Insurance & employer funds, s.4 GHS: https://assets.kpmg.com/content/dam/kpmg/cy/pdf/2025/cyprus-tax-card-2025-en.pdf
- KPMG Cyprus, *Amendment to the maximum amount of insurable earnings for 2025*: https://kpmg.com/cy/en/home/insights/2025/01/amendment-to-the-maximum-amount-of-insurable-earnings-for-2025.html
- PwC, *Cyprus – Individual – Other taxes* (Worldwide Tax Summaries): https://taxsummaries.pwc.com/cyprus/individual/other-taxes — NOTE: shows a stale 15.6% self-employed SI rate; use 16.6%.
- Health Insurance Organisation (GeSY), *GHS Financing / Contribution Rates*: https://www.gesy.org.cy/en-us/hiofinancing
- Department of Social Insurance Services (MLSI), *Basic Insurable Earnings / Contributions*: https://www.mlsi.gov.cy/mlsi/sid/sidv2.nsf/page94_en/page94_en?OpenDocument=
- Department of Social Insurance Services (MLSI), *Deadlines for payment of contributions*: https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/D5322D5E5CD6F735C22586A10044EC34
- Cyprus Mail (reporting MLSI), *Labour Minister announces increase of monthly minimum wage to 1,088 euro* (Dec 2025): https://cyprus-mail.com/2025/12/23/labour-minister-announces-increase-of-monthly-minimum-wage-to-1088-euro

**Research caveats (reviewer attention):** The official MLSI government pages repeatedly failed to fetch (TLS certificate verification error); contribution rates, deadlines and penalties are corroborated via KPMG (Big-4 primary), PwC, the official GeSY site (fetched successfully) and KPSA citing MLSI. The reviewer should re-confirm the late-payment additional charge (3% rising to a max of 27%) and the exact deadlines against the live MLSI page when accessible. The per-category 2025 self-employed minimum insurable amounts were NOT enumerated — fetch the official table from mlsi.gov.cy. PwC's other-taxes table shows a stale 15.6% self-employed SI rate; use 16.6%. SDC, the 2026 insurable-earnings ceiling, the T.D.1 deadlines and the registration form/notification timing are all marked **[RESEARCH GAP]** above.

### Test suite

Employee, gross EUR 3,000/month, below all ceilings. → Employee deduction = 11.45% = EUR 343.50/month (EUR 264.00 SI + EUR 79.50 GHS). Employer on-cost (excl. Holiday) = 15.4% = EUR 462.00/month; incl. Holiday (8.0%) = 23.4% = EUR 702.00/month.

Employee, gross EUR 7,000/month (EUR 84,000/yr), above SI ceiling, below GHS cap. → Employee SI = 8.8% x EUR 5,551 = EUR 488.49; employee GHS = 2.65% x EUR 7,000 = EUR 185.50; total = EUR 673.99/month.

Self-employed, notional insurable income EUR 28,915/yr. → SI = 16.6% = EUR 4,800/yr (EUR 1,200/quarter). GHS = 4.00% on own income additionally. (16.6%, NOT 15.6%.)

Employer on-cost components for gross EUR 4,000/month (below ceilings). → SI 8.8% = EUR 352.00; GHS 2.9% = EUR 116.00; Social Cohesion 2.0% = EUR 80.00; Redundancy 1.2% = EUR 48.00; HRDA 0.5% = EUR 20.00; total = EUR 616.00 (15.4%).

Pensioner with pension income EUR 2,000/month, aggregate income below cap. → GHS = 2.65% = EUR 53.00/month. No SI on pension.

Cyprus tax resident, dividend income EUR 50,000, aggregate income below the GHS cap. → GHS = 2.65% x EUR 50,000 = EUR 1,325.00 (subject to the EUR 180,000 aggregate cap; applies regardless of domicile). SDC treatment is out of scope and a [RESEARCH GAP].

Personal income tax on taxable income EUR 40,000 (2025 brackets). → 0% on first 19,500 = 0; 20% on 8,500 (19,501–28,000) = EUR 1,700.00; 25% on 8,300 (28,001–36,300) = EUR 2,075.00; 30% on 3,700 (36,301–40,000) = EUR 1,110.00. Total = EUR 4,885.00. Check: 1,700 + 2,075 + 1,110 = 4,885.00. [KPMG s.1.1]

Employer cost on EUR 5,000/month, Holiday-Fund EXEMPT vs NOT exempt. → Exempt: 5,000 × 15.40% = EUR 770.00/month (SI 440 + GHS 145 + Cohesion 100 + Redundancy 60 + HRDA 25). Not exempt: add Holiday 5,000 × 8.0% = EUR 400.00, total 5,000 × 23.40% = EUR 1,170.00/month.

GHS on EUR 200,000 aggregate income (above the EUR 180,000 cap), employee rate. → GHS = 180,000 × 2.65% = EUR 4,770.00/year (capped); the EUR 20,000 above the cap bears no GHS.

Employer registers a new hire. → Register with DSI and obtain an employer registration number before employing staff; the employee needs a Social Insurance number before contributions are reported. (Specific form number / Ergani notification deadline = [RESEARCH GAP].)

### Prohibitions

- NEVER use 15.6% for self-employed social insurance — the current 2025 rate is 16.6% (effective 1 Jan 2024). [KPMG s.3.1]
- NEVER apply the EUR 66,612 SI ceiling to GHS — GHS uses the EUR 180,000 aggregate cap; Social Cohesion has NO cap.
- NEVER apply the Social Cohesion Fund (2.0%) to insurable earnings only — it is on actual earnings, uncapped.
- NEVER include the Central Holiday Fund (8.0%) without confirming the employer is not exempt; most established employers are exempt.
- NEVER omit the differing ceilings when computing high earners — SI/Redundancy/HRDA/Holiday cap at EUR 66,612 while GHS does not until EUR 180,000.
- NEVER mix 2025 and 2026 figures — new income tax brackets and a higher minimum wage take effect 1 Jan 2026.
- NEVER assert SDC rates or the SDC reform as confirmed — they are out of scope and a [RESEARCH GAP]; GHS at 2.65% still applies on rent/interest/dividend income regardless of domicile.
- NEVER compute self-employed SI without the DSI occupational-category minimum insurable amount — flag the research gap.
- NEVER quote income tax late-filing penalties or interest as definitive — these were not confirmed from a primary authority.
- NEVER present any contribution figure as definitive — label as estimated and direct the client to their DSI/HIO statements.
- NEVER compute contribution arrears or surcharges without a DSI statement — escalate to a Cyprus-qualified accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
