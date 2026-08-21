---
name: albania-income-tax
description: Use this skill whenever asked about Albania personal income tax for self-employed individuals and employees. Trigger on phrases like "how much tax do I pay in Albania", "Albanian income tax", "DIVA", "D1 annual return", "tatime.gov.al", "self-employed Albania", "ALL tax brackets", "0% small business tax", "social and health contributions Albania", "PAYE Albania", "13% 23% income tax", "dividend tax Albania", "disguised employment", or any question about filing or computing personal income tax for a resident or non-resident individual in Albania. Also trigger when preparing or reviewing an annual individual return, computing the 0%/15%/23% self-employed regime, applying the monthly PAYE withholding schedule, or advising on social/health contributions. This skill covers progressive employment rates, the self-employed business regime, investment income, social/health contributions, the per-child deduction, filing thresholds, penalties, and interaction with VAT. ALWAYS read this skill before touching any Albanian income tax work.
version: 0.1
jurisdiction: AL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Albania Personal Income Tax -- Self-Employed & Individuals

## Albania Personal Income Tax -- Self-Employed & Individuals Skill v0.1

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Albania (Republic of Albania) |
| Tax | Personal income tax (Tatimi mbi të Ardhurat Personale) |
| Currency | ALL only (Albanian lek) |
| Tax year | Calendar year (1 January -- 31 December) [PwC: Tax administration] |
| Primary legislation | Law No. 29/2023, dated 30.03.2023, "On Income Tax" (effective 1 Jan 2024; repealed Law No. 8438/1998) |
| Supporting legislation | General Instruction No. 26, dated 08.09.2023 (implementing); Law No. 7703/1993 "On Social Insurance" (as amended); Law No. 10383/2011 (health insurance); Law No. 9920/2008 "On Tax Procedures" (as amended) |
| Tax authority | General Directorate of Taxes / Albanian Tax Administration (Drejtoria e Përgjithshme e Tatimeve, DPT) |
| Filing portal | tatime.gov.al e-filing |
| Annual return deadline | 31 March of the following year (e.g. 31 March 2026 for 2025) [PwC; tatime.gov.al] |
| Validated by | Pending — requires sign-off by an Albanian-qualified accountant/tax advisor |
| Validation date | Pending |
| Skill version | 0.1 |
| Research confidence | Medium — several figures flagged [RESEARCH GAP] below require reviewer confirmation against current Council of Ministers (CoM) decisions and General Instruction No. 26/2023 |

### Tax Rate Brackets (2025)

**Employment income — ANNUAL (year-end reconciliation)**  _([Law 29/2023; PwC: Taxes on personal income])_

| Annual Taxable Income (ALL) | Rate | Cumulative Tax at Top |
| --- | --- | --- |
| 0 -- 2,040,000 | 13% | ALL 265,200 |
| 2,040,001+ | 23% | -- |

Cumulative check: 2,040,000 × 13% = ALL 265,200. Above the breakpoint, tax = 265,200 + 23% × (income − 2,040,000). A personal allowance reduces the taxable base at lower incomes — see the monthly schedule below.

**Employment income — MONTHLY withholding (PAYE) schedule (official tatime.gov.al table)**  _([tatime.gov.al: Tax on personal income; PwC])_

| Monthly Gross (ALL) | Tax |
| --- | --- |
| 0 -- 50,000 | 0% (fully exempt) |
| 50,001 -- 60,000 | 13% on the amount exceeding ALL 35,000 (transitional band — allowance partially phases out) |
| 60,001 -- 200,000 | 13% on the amount exceeding ALL 30,000 |
| 200,001+ | ALL 22,100 + 23% on the amount exceeding ALL 200,000 |

Arithmetic check on the ALL 22,100 base: at monthly gross ALL 200,000 the prior-band tax = 13% × (200,000 − 30,000) = 13% × 170,000 = ALL 22,100. Consistent.

[RESEARCH GAP — reviewer to confirm] The monthly 23% breakpoint (ALL 200,000/month = ALL 2,400,000/year) does NOT line up with the annual 23% breakpoint (ALL 2,040,000/year = ALL 170,000/month). The research notes two different official presentations of the monthly table (a simplified 0/13/23 version on tatime.gov.al vs. the allowance-phase-out version above from PwC). Reconcile both against General Instruction No. 26/2023 for the authoritative monthly algorithm before relying on month-by-month figures; the year-end reconciliation uses the annual 13%/23% brackets.

**Self-employed / business / trader income — ANNUAL taxable profit**  _([HLB Albania; PwC])_

| Annual Taxable Profit (ALL) | Statutory Rate | Effective Rate 2025 |
| --- | --- | --- |
| 0 -- 14,000,000 | 15% | **0% until 31 Dec 2029** |
| 14,000,001+ | 23% | 23% |

Self-employed and registered entrepreneurs with annual turnover up to ALL 14,000,000 enjoy a 0% rate until 31 December 2029 (statutory rate 15%); profit above ALL 14,000,000 is taxed at 23%. Subject to profession-based exclusions (CoM Decision No. 753) and the anti-disguised-employment rule below.

**Investment income**  _([PwC; HLB Albania])_

| Type | Rate |
| --- | --- |
| Dividends | 8% |
| Interest, royalties, rental income, capital gains (incl. real estate & securities), crypto, other investment income | 15% |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | Treat as Albanian tax resident (worldwide income); non-residents taxed on Albania-source income only [PwC] |
| Unknown self-employed eligibility for 0% band | Do NOT assume 0% — confirm turnover ≤ ALL 14m AND activity not on CoM Decision 753 excluded list AND no disguised-employment reclassification [PwC] |
| Single-client / few-client self-employment | Apply disguised-employment reclassification (employment rates 13%/23%) unless proven otherwise [HLB Albania] |
| Unknown contribution base ceiling | Use the year's official CoM-decision floor/ceiling; verify before computing; health insurance has NO ceiling [Eurofast Payroll Guide 2025] |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration status | Assume not registered unless turnover > ALL 10,000,000 evidenced [tatime.gov.al] |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) tax residency (resident/non-resident), (b) income type(s) (employment, self-employed/business, investment), and (c) for self-employed: annual turnover and whether the activity is eligible for the 0% small-business band.

**Recommended** -- all sales invoices, purchase invoices/receipts, monthly payroll/withholding declarations, social/health contribution payment records, prior-year annual return (D1/DIVA), VAT registration status.

**Ideal** -- complete income and expenditure account, list of clients with revenue share (to test the disguised-employment rule), dependent-children details (per-child deduction), education-expense receipts, prior-year tax assessment.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that income classification (employment vs self-employed vs investment) is correct."

### Refusal Catalogue

- **R-AL-1** — Residency unknown. "Residency determines whether the client is taxed on worldwide income (resident) or Albania-source income only (non-resident). This skill defaults to resident treatment but cannot finalise without confirmation. Please confirm before filing."
- **R-AL-2** — Self-employed eligibility for the 0% band unconfirmed. "The 0%-until-2029 rate applies only if turnover ≤ ALL 14,000,000, the activity is not on the CoM Decision No. 753 excluded-profession list, and the income is not reclassified as disguised employment. This skill cannot confirm eligibility without the client's activity code and client-concentration data. Escalate to an Albanian tax advisor."
- **R-AL-3** — Companies and partnerships. "This skill covers individuals and sole self-employed persons only. Corporate income tax (tatimi mbi fitimin) and partnership returns are out of scope. Escalate to an Albanian tax advisor."
- **R-AL-4** — Real-estate or securities capital gains. "Capital gains on real estate and securities are taxed at 15% but require specialised computation of acquisition cost and holding. Escalate to an Albanian tax advisor for material disposals."
- **R-AL-5** — Arrears / enforcement. "Client has outstanding tax arrears or is subject to DPT enforcement. Late-payment penalty is 10% plus 0.06%/day interest (capped at 365 days). Do not advise. Escalate immediately."
- **R-AL-6** — VAT return requested. "This skill covers personal income tax only. For Albanian VAT (TVSH), use the albania-vat skill. Standard VAT rate is 20%; registration is mandatory above ALL 10,000,000 turnover."
- **R-AL-7** — 2026 figures requested. "From 1 January 2026 the minimum wage rises to ALL 50,000/month (CoM Decision 776/2025) and Law No. 79/2025 amends tax procedures (automated VAT, e-communication, lower cash limits). This skill is built for the 2025 tax year — confirm the year-correct figures before applying to 2026."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Albanian statements mix Albanian and English; common Albanian terms are listed. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFERTE, PAGESE, ARKETIM, DEPOSIT, PAYMENT RECEIVED | Self-employed business income | Business income (0%/15%/23% regime) | If VAT-registered, extract net (excl. 20% TVSH) |
| FATURE, HONORAR, FEES, CONSULTANCY, SHERBIM | Self-employed business income | Business income | Professional/service fees |
| STRIPE PAYOUT, PAYPAL, WISE, REVOLUT PAYOUT | Self-employed business income | Business income | Platform payout — match to invoices; net of platform fee |
| UPWORK, FIVERR, TOPTAL | Self-employed business income | Business income | Freelance platform — TEST disguised-employment rule |
| PAGE, RROGA, SALARY, EMPLOYER [name] | Employment income | Employment (13%/23%) | Check whether PAYE already withheld |
| QIRA, RENT RECEIVED | Rental income | Investment income — 15% | Not self-employment |
| INTERES, INTERESI, INTEREST | Interest income | Investment income — 15% |  |
| DIVIDEND, DIVIDENT | Dividend income | Investment income — 8% |  |
| RIMBURSIM TATIMI, TAX REFUND | EXCLUDE | Not income | Refund from prior year |
| GRANT, SUBVENCION, GOVERNMENT GRANT | Check nature | Capital grants EXCLUDE; revenue grants = business income | Flag for reviewer |

### 3.2 Expense Patterns (Debits) -- Fully Deductible (self-employed business expenses)

**Fully deductible expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| QIRA ZYRE, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| SIGURIM PROFESIONAL, PROFESSIONAL INDEMNITY | Professional insurance | Deductible |  |
| KONTABILIST, AUDITOR, BOOKKEEP, ACCOUNTANT | Accountancy fees | Deductible |  |
| AVOKAT, LAWYER, LEGAL, NOTER | Legal/notary fees | Deductible | Must be business-related |
| KANCELARI, OFFICE SUPPLIES, STATIONERY | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | Deductible |  |
| TRAJNIM, KURS, SEMINAR, CONFERENCE, CPD | Training/CPD | Deductible | Must relate to current business |
| TARIFE BANKE, BANK FEE, KOMISION | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, AWS, CLOUDFLARE, DIGITALOCEAN | IT infrastructure | Deductible | High-value items may be capital — flag |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and software expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| PERPETUAL SOFTWARE LICENCE (high value) | Capital item | Capitalise/depreciate | Flag for reviewer — depreciation rate per tax law |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities expense patterns table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| OSHEE, KESH, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home; default 0% if mixed |
| UJESJELLES, WATER | Water | T2 if home office | Apportion |
| VODAFONE, ONE, ALBTELECOM, DIGICOM | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR ALBANIA, WIZZ AIR, RYANAIR, FLIGHT | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| TAXI, BOLT, UBER | Local transport | Deductible if business purpose |  |
| KARBURANT, FUEL, PETROL, GAZOIL | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARKIM, PARKING | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**Not deductible expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORANT, DINNER, LUNCH, ENTERTAINMENT | Entertainment | NOT deductible (or strictly limited) | Flag for reviewer — entertainment generally blocked |
| PERSONAL, USHQIME, SUPERMARKET, GROCERIES | Personal expenses | NOT deductible | Private living costs |
| GJOBE, FINE, PENALTY, PENALITET | Fines/penalties | NOT deductible | Public policy |
| TATIM, INCOME TAX, TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| TERHEQJE PERSONALE, DRAWINGS, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERTE E BRENDSHME, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| KESTI KREDISE, LOAN REPAYMENT | EXCLUDE (principal) | Loan principal movement; interest may be separately deductible |
| SIGURIME SHOQERORE, SIGURIME SHENDETESORE, SOCIAL/HEALTH CONTRIBUTION | Contributions (separate line) | Self-employed contributions — see Section 5; NOT a business deduction |
| PAGESE TVSH, VAT PAYMENT | EXCLUDE | VAT liability payment, not expense |

### 3.8 Albanian Banks -- Statement Format Reference

**Albanian banks statement format reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BKT (Banka Kombëtare Tregtare) | TRANSFERTE, PAGESE, KOMISION | PDF/CSV; date DD/MM/YYYY |
| Raiffeisen Bank Albania | PAGESE, TRANSFER, TARIFE | PDF/CSV; counterparty in description |
| Credins Bank | TRANSFERTE, ARKETIM, KOMISION | PDF |
| Intesa Sanpaolo Bank Albania | PAGESE, TRANSFER, FEE | PDF/CSV |
| OTP Bank Albania | TRANSFERTE, PAGESE | PDF/CSV |
| Revolut / Wise (business) | PAYMENT, TRANSFER, CONVERSION | CSV; multi-currency — convert to ALL |

## Section 4 -- Worked Examples

All examples are for the 2025 tax year and use the figures cited in Sections 1 and 5. Tax figures are estimates and must be reviewer-confirmed.

### Example 1 -- Employee, mid-range salary (monthly PAYE)

**Input line:**
`31/03/2025 ; BKT TRANSFERTE ; EMPLOYER ALPHA SHPK ; RROGA MARS 2025 ; +90,000.00 ; ALL`

**Reasoning:**
Monthly employment income ALL 90,000 (gross). This falls in the 60,001–200,000 band: PAYE = 13% on the amount exceeding ALL 30,000.
- Taxable above allowance = 90,000 − 30,000 = ALL 60,000
- PIT withheld = 13% × 60,000 = ALL 7,800
- Employee social + health = 11.2% × 90,000 = ALL 10,080 (90,000 is within the 2025 floor ALL 40,000 / ceiling ~ALL 176,416 [RESEARCH GAP — confirm ceiling])
- Net pay = 90,000 − 7,800 − 10,080 = **ALL 72,120**

**Classification:** Employment income; PIT withheld ALL 7,800; employee contributions ALL 10,080; net ALL 72,120.

### Example 2 -- High earner, monthly PAYE in the 23% band

**Input line:**
`30/04/2025 ; Raiffeisen ; EMPLOYER BETA SHA ; RROGA PRILL ; +250,000.00 ; ALL`

**Reasoning:**
Monthly gross ALL 250,000 → top band (200,001+): PIT = ALL 22,100 + 23% on the amount exceeding ALL 200,000.
- Excess = 250,000 − 200,000 = ALL 50,000
- PIT = 22,100 + (23% × 50,000) = 22,100 + 11,500 = **ALL 33,600**
- Employee contributions: social 9.5% capped at the ceiling; health 1.7% uncapped. Using the reported ceiling ~ALL 176,416 [RESEARCH GAP — confirm]: social = 9.5% × 176,416 = ALL 16,759.52; health = 1.7% × 250,000 = ALL 4,250 → contributions = ALL 21,009.52

**Classification:** Employment income; PIT withheld ALL 33,600; contributions ALL 21,009.52 (ceiling-dependent — reviewer to confirm ceiling figure).

### Example 3 -- Self-employed, within the 0% small-business band

**Input lines (full year, summarised):**
`Total business income (credits): +9,500,000.00 ALL`
`Total allowable expenses (debits): -3,200,000.00 ALL`

**Reasoning:**
Annual turnover ALL 9,500,000 ≤ ALL 14,000,000, activity confirmed eligible (not on CoM Decision 753 list) and no disguised-employment reclassification.
- Taxable profit = 9,500,000 − 3,200,000 = ALL 6,300,000
- PIT rate = **0% until 31 Dec 2029** → income tax = **ALL 0**
- Note: self-employed social insurance 23% and health 3.4% still apply on their statutory bases (Section 5). On a monthly base of ALL 50,000: social = 23% × 50,000 = ALL 11,500/month; health = 3.4% × 100,000 = ALL 3,400/month [PwC: other taxes].

**Classification:** Self-employed business profit ALL 6,300,000; income tax ALL 0 (0% band); contributions due separately.

### Example 4 -- Self-employed, profit above ALL 14,000,000

**Input lines (full year, summarised):**
`Total business income: +20,000,000.00 ALL`
`Total allowable expenses: -3,000,000.00 ALL`

**Reasoning:**
Taxable profit = 20,000,000 − 3,000,000 = ALL 17,000,000.
- Band 0 – 14,000,000: 0% (until 2029) → ALL 0
- Band above 14,000,000: 23% × (17,000,000 − 14,000,000) = 23% × 3,000,000 = **ALL 690,000**
- Total income tax = 0 + 690,000 = **ALL 690,000**

**Classification:** Self-employed business profit ALL 17,000,000; income tax ALL 690,000.

### Example 5 -- Dividend received (8%)

**Input line:**
`15/06/2025 ; Credins ; SHPK GAMMA ; DIVIDENT 2024 ; +500,000.00 ; ALL`

**Reasoning:**
Dividend income taxed at 8% (typically withheld at source).
- Tax = 8% × 500,000 = **ALL 40,000**
- Net = 500,000 − 40,000 = ALL 460,000

**Classification:** Investment income (dividend); tax ALL 40,000.

### Example 6 -- Rental income (15%)

**Input line:**
`05/07/2025 ; Intesa ; TENANT D. HOXHA ; QIRA KORRIK ; +60,000.00 ; ALL`

**Reasoning:**
Rental income is investment income taxed at 15%.
- Tax = 15% × 60,000 = **ALL 9,000**
- Net = 60,000 − 9,000 = ALL 51,000

**Classification:** Investment income (rental); tax ALL 9,000. (Where allowable expenses against rent apply, reviewer to confirm method per Law 29/2023.)

### Example 7 -- Disguised employment reclassification

**Input lines (full year, summarised):**
`Self-employed income from ONE client: +4,000,000.00 ALL (100% from a single client)`

**Reasoning:**
Because ≥80% of the self-employed income is from a single client, the anti-disguised-employment rule reclassifies the income as employment income, taxed at 13%/23% (NOT 0%). [HLB Albania]
- Annual taxable income ALL 4,000,000 → first 2,040,000 at 13% = ALL 265,200; excess 1,960,000 at 23% = ALL 450,800
- Income tax = 265,200 + 450,800 = **ALL 716,000**

**Classification:** Reclassified to employment income; income tax ALL 716,000 (the 0% band does NOT apply). Flag for reviewer.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Tax Year and Residency

- **Tax year and residency** — The tax year is the calendar year (1 Jan – 31 Dec). Residents are taxed on worldwide income; non-residents on Albania-source income only.  _(Law No. 29/2023, "On Income Tax" [PwC: Taxes on personal income])_

### 5.2 Employment Income — Progressive Rates

- **Employment progressive rates** — Annual taxable employment income: 13% up to ALL 2,040,000; 23% on the excess (cumulative tax at the breakpoint = ALL 265,200). In-year withholding uses the monthly PAYE schedule (Section 1); year-end reconciliation applies the annual brackets.  _(Law 29/2023 (effective 1 Jan 2024, continuing 2025) [Law 29/2023; PwC; tatime.gov.al])_

### 5.3 Self-Employed / Business Income

- **Self-employed / business income rate** — Statutory rate 15% on profit up to ALL 14,000,000 and 23% above — BUT a 0% rate applies to the up-to-ALL-14m band until 31 December 2029. Profit above ALL 14,000,000 is taxed at 23%.  _(Law 29/2023; HLB Albania commentary [HLB Albania; PwC])_

### 5.4 Anti-Disguised-Employment Rule

- **Anti-disguised-employment rule** — If ≥80% of self-employed income is from a single client, OR ≥90% from fewer than three clients, the income is reclassified as employment income and taxed at 13%/23% (the 0% band does not apply).  _(Law 29/2023 / implementing rules [HLB Albania])_

### 5.5 Investment Income

**Investment income table**

| Type | Rate |
| --- | --- |
| Dividends | 8% [PwC; HLB] |
| Interest, royalties, rental income, capital gains (real estate & securities), crypto, other | 15% [PwC: income determination; HLB] |

### 5.6 Social and Health Contributions — Employees

**Social and health contributions — employees table**  _(Law No. 7703/1993 (social insurance); Law No. 10383/2011 (health) [PwC: other taxes])_

| Contribution | Employee | Employer |
| --- | --- | --- |
| Social insurance (pension/disability/maternity) | 9.5% | 15.0% |
| Health insurance | 1.7% | 1.7% |
| **TOTAL** | **11.2%** | **16.7%** |

*Column checks: employee 9.5 + 1.7 = 11.2%; employer 15.0 + 1.7 = 16.7%; combined employer + employee = 11.2 + 16.7 = 27.9%.* [PwC: other taxes]

Social insurance is computed on a gross monthly base between an annual floor and ceiling set by Council of Ministers decision (2025 floor aligned with the minimum wage ALL 40,000; ceiling reported ~ALL 176,416 in payroll guides **[RESEARCH GAP — reviewer to confirm exact 2025 ceiling against the current CoM decision]**). Health insurance (1.7% each side) has **no ceiling** — it applies to full gross. [PwC; Eurofast Payroll Guide 2025]

### 5.7 Social and Health Contributions — Self-Employed (non-agricultural)

**Social and health contributions — self-employed table**  _([PwC: other taxes])_

| Contribution | Rate | Base |
| --- | --- | --- |
| Social insurance | 23% | on a monthly base of at least ALL 50,000 (≈ ALL 11,500/month minimum) |
| Health insurance | 3.4% | on at least ALL 100,000 (double the minimum salary base) |

### 5.8 Per-Child and Education Deductions (from 2025)

- **Per-child and education deductions** — ALL 48,000 per year per dependent child under 18; plus up to ALL 100,000/year for children's education. Both available only to taxpayers with annual income below ALL 1,200,000.  _(Law 29/2023 (2025 changes); HLB Albania [HLB Albania])_

### 5.9 Filing Thresholds

- **Annual filing thresholds** — The annual individual return is mandatory if ANY of: Annual income > ALL 1,200,000 from all sources; OR the taxpayer had multiple employers (any income level); OR more than ALL 50,000 of income not subject to final withholding. Self-employed persons must always file.  _([PwC: tax administration; tatime.gov.al; HLB])_

### 5.10 Deadlines and Penalties

**Deadlines and penalties table**  _(Law No. 9920/2008 "On Tax Procedures")_

| Item | Detail |
| --- | --- |
| Annual return (D1 / DIVA) | 31 March of the following year; final tax due same date [PwC; tatime.gov.al] |
| Monthly payroll & withholding declaration | E-filed by the 20th of the following month [PwC] |
| Late filing — individual taxpayer | ALL 3,000 (plus interest) [HLB; tatime.gov.al] |
| Late filing — income-tax-registered taxpayer | ALL 10,000 [tatime.gov.al] |
| Late filing — other taxpayers (non-individual) | ALL 5,000 [tatime.gov.al] |
| Late payment penalty | 10% of the unpaid liability [tatime.gov.al] |
| Late payment interest | 0.06% per day, capped at 365 days (max 21.9%) [tatime.gov.al] |

**[RESEARCH GAP — reviewer to confirm]** Penalty figures cited are pre-amendment. Law No. 79/2025 amended tax procedures effective Jan 2026; re-check before applying to 2026 periods.

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Self-Employed 0% Band Eligibility

- **0% band eligibility checklist** — Confirm turnover ≤ ALL 14,000,000 for the year. Confirm the activity is NOT on the CoM Decision No. 753 excluded-profession list. **[RESEARCH GAP — the excluded list is not enumerated here; reviewer must check Decision 753.]** Confirm no disguised-employment reclassification (Section 5.4). Conservative default: Do not apply 0% until all three are confirmed.

### 6.2 Disguised-Employment Test

- **Disguised-employment test** — Compute revenue share per client. If ≥80% from one client or ≥90% from <3 clients, reclassify to employment income. Flag for reviewer with the client-concentration figures.

### 6.3 Contribution Base Floor/Ceiling

- **Contribution base floor/ceiling** — The floor and ceiling are reset annually by CoM decision. Verify the year-correct figures before computing social insurance. Health insurance has no ceiling. Conservative default: Use the year's official figures; flag the ceiling for confirmation.

### 6.4 Home Office / Mixed-Use Expenses

- **Home office / mixed-use expenses** — Only the business-use proportion of rent, electricity, water, internet is deductible (for self-employed). Must be a genuinely dedicated workspace. Conservative default: 0% deduction until the reviewer confirms the arrangement.

### 6.5 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel, insurance, maintenance is deductible; requires a mileage log. Conservative default: 0% business use until a log is provided.

### 6.6 Capital Asset Depreciation

- **Capital asset depreciation** — High-value business assets should be capitalised and depreciated rather than expensed. **[RESEARCH GAP — depreciation rates/method under Law 29/2023 not enumerated here; reviewer to confirm.]** Flag for reviewer.

### 6.7 Residency Determination

- **Residency determination** — Confirm days-present and permanent-home tests for residents vs non-residents. Flag for reviewer where the client has cross-border ties.

## Section 7 -- Excel Working Paper Template

```
ALBANIA PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident (worldwide) / Non-resident (Albania-source)
Income type: Employment / Self-employed / Investment / Mixed

A. EMPLOYMENT INCOME (if applicable)
  A1. Annual gross employment income            ___________
  A2. PIT (13% to 2,040,000; 23% above)         ___________
  A3. Employee social 9.5% (capped at ceiling)  ___________
  A4. Employee health 1.7% (no ceiling)         ___________
  A5. Net employment income (A1-A2-A3-A4)       ___________

B. SELF-EMPLOYED / BUSINESS INCOME (if applicable)
  B1. Annual business turnover                   ___________
  B2. Less: allowable expenses                   ___________
  B3. Taxable profit (B1 - B2)                   ___________
  B4. 0%-band eligible? (Y/N) [confirm]          ___________
  B5. Income tax (0% to 14m if eligible;
       23% above 14m)                            ___________
  B6. Self-employed social 23% (base ≥50,000)    ___________
  B7. Self-employed health 3.4% (base ≥100,000)  ___________

C. INVESTMENT INCOME (if applicable)
  C1. Dividends                  x 8%  =         ___________
  C2. Interest/royalties/rent/CG x 15% =         ___________

D. DEDUCTIONS (income < ALL 1,200,000 only)
  D1. Per child (ALL 48,000 x children)          ___________
  D2. Education (up to ALL 100,000)              ___________

E. TOTAL INCOME TAX (A2 + B5 + C1 + C2)          ___________
F. Less: tax already withheld / paid             ___________
G. Tax due / refund (E - F)                      ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Self-employed 0%-band eligibility confirmed (turnover, Decision 753, disguised employment)?
  [ ] Contribution ceiling figure confirmed against CoM decision?
  [ ] Per-child/education deduction income limit (<ALL 1,200,000) met?
  [ ] Filing threshold met (return required)?
  [ ] All T2 items flagged for review?
  [ ] Monthly vs annual PAYE reconciliation done?
```

## Section 8 -- Bank Statement Reading Guide

### Albanian Bank Statement Formats

**Albanian bank statement formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BKT | PDF, CSV | Data, Përshkrim, Debi, Kredi, Gjendje | Most common; description holds counterparty + reference |
| Raiffeisen Bank Albania | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant |
| Credins Bank | PDF | Data, Përshkrim, Hyrje, Dalje | Shorter descriptions |
| Intesa Sanpaolo Bank Albania | PDF, CSV | Date, Description, Amount, Balance |  |
| OTP Bank Albania | PDF, CSV | Data, Përshkrim, Shumë, Gjendje |  |
| Revolut / Wise (business) | CSV | Date, Counterparty, Amount, Currency | Multi-currency — convert to ALL |

### Key Albanian Banking / Tax Terms

**Key Albanian banking / tax terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFERTE / TRANSFER | Transfer | Check direction for income/expense |
| PAGESE | Payment | Outgoing payment — likely expense |
| ARKETIM | Collection/receipt | Incoming — likely income |
| RROGA / PAGE | Salary/wage | Employment income |
| QIRA | Rent | Rental income (in) or office rent (out) |
| INTERES / INTERESI | Interest | Investment income (15%) |
| DIVIDENT | Dividend | Investment income (8%) |
| KOMISION / TARIFE | Commission/fee | Bank charge — deductible (business) |
| FATURE | Invoice | Supporting doc for income/expense |
| TVSH | VAT | VAT amount — exclude from income/expense base |
| SIGURIME SHOQERORE / SHENDETESORE | Social / health insurance | Contributions — handle separately |
| TATIM | Tax | Tax payment — not deductible |
| GJOBE | Fine/penalty | Not deductible |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ALBANIA INCOME TAX
1. Tax residency: resident (worldwide income) or non-resident (Albania-source only)?
2. Income type: employment, self-employed/business, investment, or mixed?
3. If self-employed: total annual turnover? Is your activity on the CoM Decision 753 excluded list?
4. If self-employed: what % of your income comes from your largest client? From your top 3 clients?
5. Are you VAT-registered (turnover > ALL 10,000,000)?
6. Did you have more than one employer during the year?
7. Any income NOT taxed at source above ALL 50,000?
8. Dependent children under 18? Any children's education costs? (relevant if income < ALL 1,200,000)
9. Social/health contributions paid during the year (amount and basis)?
10. Any dividends, interest, rent, capital gains, or crypto income?
```

### Key Legislation / Authority References

**Key Legislation / Authority References**  _(Section 10 -- Reference Material)_

| Topic | Reference |
| --- | --- |
| Income tax (all rates) | Law No. 29/2023 "On Income Tax" (eff. 1 Jan 2024) |
| Implementing rules | General Instruction No. 26, dated 08.09.2023 |
| Social insurance contributions | Law No. 7703/1993 (as amended) |
| Health insurance contributions | Law No. 10383/2011 |
| Tax procedures / penalties | Law No. 9920/2008 (as amended; note Law No. 79/2025 from Jan 2026) |
| Minimum wage 2025 | ALL 40,000/month [ARS; HLB] |
| Minimum wage 2026 | ALL 50,000/month (CoM Decision No. 776, dated 19.12.2025) [ARS; HLB] |
| VAT registration threshold | Turnover > ALL 10,000,000 (register within 15 days); standard VAT 20% [PwC; tatime.gov.al] |
| Filing portal & monthly table | tatime.gov.al |

### Forms

**Forms**  _(Section 10 -- Reference Material)_

| Form | Purpose | Deadline |
| --- | --- | --- |
| Annual Individual Income Declaration (Deklarata Individuale Vjetore e të Ardhurave — D1 / "DIVA") | Annual PIT return (residents worldwide, certain non-residents; high earners, multiple-employer cases, untaxed income) | 31 March of the following year [PwC; tatime.gov.al] |
| Monthly payroll & withholding declaration | Employer reports/remits withheld PIT and social/health contributions | 20th of the following month [PwC] |

### Key Thresholds (with provenance)

**Key Thresholds (with provenance)**  _(Section 10 -- Reference Material)_

| Threshold | Value | Source |
| --- | --- | --- |
| Tax-free monthly employment income | ALL 50,000/month | tatime.gov.al |
| Employment 23% breakpoint (annual) | ALL 2,040,000 | Law 29/2023; PwC |
| Self-employed 0% PIT turnover ceiling | ALL 14,000,000/year (0% until 31 Dec 2029) | HLB Albania |
| Annual return mandatory filing | income > ALL 1,200,000 OR multiple employers OR > ALL 50,000 untaxed | PwC; tatime.gov.al; HLB |
| Per-child deduction | ALL 48,000/year/child <18 (income < ALL 1,200,000) | HLB Albania |
| Children's education deduction | up to ALL 100,000/year (income < ALL 1,200,000) | HLB Albania |
| VAT registration | turnover > ALL 10,000,000 | PwC; tatime.gov.al |
| 2025 contribution floor | ALL 40,000/month (= minimum wage) | Eurofast; ARS; HLB |
| 2025 contribution ceiling | ~ALL 176,416/month **[RESEARCH GAP — confirm]** | Eurofast Payroll Guide 2025 |

### Sources

1. PwC Worldwide Tax Summaries — Albania, Individual: Taxes on personal income — https://taxsummaries.pwc.com/albania/individual/taxes-on-personal-income (reviewed 19 Feb 2026)
2. PwC — Albania, Individual: Other taxes (social/health contributions) — https://taxsummaries.pwc.com/albania/individual/other-taxes
3. PwC — Albania, Individual: Tax administration — https://taxsummaries.pwc.com/albania/individual/tax-administration
4. PwC — Albania, Individual: Income determination — https://taxsummaries.pwc.com/albania/individual/income-determination
5. General Directorate of Taxes (tatime.gov.al) — Tax on personal income (official monthly bracket table) — https://www.tatime.gov.al/eng/c/4/96/108/tax-on-personal-income
6. tatime.gov.al — Value Added Tax — https://www.tatime.gov.al/eng/c/4/96/110/value-added-tax
7. tatime.gov.al — Key amendments to the law "On tax procedures" (penalties) — https://www.tatime.gov.al/eng/d/8/45/0/627/on-the-key-amendments-to-the-law-on-tax-procedures
8. HLB Albania — Legal tax changes from January 1, 2025 — https://www.hlb.al/legal-tax-changes-from-january-1-2025/
9. HLB Albania — Increase of the Minimum Wage from 1 January 2026 — https://www.hlb.al/increase-of-the-minimum-wage-in-albania-from-1-january-2026-what-changes-for-employers-and-employees/
10. ARS Firm — CoM Decision No. 776/2025 on the National Minimum Wage — https://arsfirm.al/en/council-of-ministers-decision-no-776-dated-december-19-2025-on-the-determination-of-the-minimum-wage-at-the-national-level/
11. Eurofast — Albania Payroll Guide 2025 (contribution floor/ceiling) — https://eurofast.eu/wp-content/uploads/2025/02/Payroll-Guide-2025_Albania-1.pdf
12. Karanovic & Partners — Albania Implementing New Income Tax Law (Law 29/2023, effective 2024) — https://www.karanovicpartners.com/news/albania-implementing-new-income-tax-law/

### Test Suite

**Test 1 -- Employee, monthly PAYE in the 13% band.**
Input: monthly gross ALL 90,000.
Expected: PIT = 13% × (90,000 − 30,000) = ALL 7,800. Employee contributions 11.2% × 90,000 = ALL 10,080. Net = ALL 72,120.

**Test 2 -- Employee, monthly PAYE in the 23% band.**
Input: monthly gross ALL 250,000.
Expected: PIT = 22,100 + 23% × (250,000 − 200,000) = 22,100 + 11,500 = ALL 33,600.

**Test 3 -- Self-employed within the 0% band.**
Input: turnover ALL 9,500,000, expenses ALL 3,200,000, eligible activity, no disguised employment.
Expected: taxable profit ALL 6,300,000; income tax = ALL 0 (0% until 2029). Contributions due separately.

**Test 4 -- Self-employed above ALL 14m.**
Input: profit ALL 17,000,000.
Expected: income tax = 23% × (17,000,000 − 14,000,000) = ALL 690,000.

**Test 5 -- Dividend.**
Input: dividend ALL 500,000.
Expected: tax = 8% × 500,000 = ALL 40,000; net ALL 460,000.

**Test 6 -- Rental income.**
Input: monthly rent received ALL 60,000.
Expected: tax = 15% × 60,000 = ALL 9,000; net ALL 51,000.

**Test 7 -- Disguised employment.**
Input: ALL 4,000,000 self-employed income, 100% from one client.
Expected: reclassified to employment; tax = 265,200 + 23% × (4,000,000 − 2,040,000) = 265,200 + 450,800 = ALL 716,000. The 0% band does NOT apply.

**Test 8 -- Annual employment reconciliation, top band.**
Input: annual employment income ALL 3,000,000.
Expected: tax = 265,200 + 23% × (3,000,000 − 2,040,000) = 265,200 + 220,800 = ALL 486,000.

## PROHIBITIONS

- NEVER apply the self-employed 0% rate without confirming turnover ≤ ALL 14m, activity eligibility (CoM Decision 753), AND no disguised-employment reclassification
- NEVER ignore the disguised-employment rule for single-client or few-client self-employed income
- NEVER apply the per-child / education deduction to a taxpayer with income ≥ ALL 1,200,000
- NEVER apply social-insurance contributions above the ceiling, or apply a ceiling to health insurance (health has none)
- NEVER mix 2025 and 2026 minimum-wage / contribution figures — use the year-correct figure
- NEVER allow income tax itself, fines, penalties, drawings, or VAT payments as business deductions
- NEVER include VAT collected on sales in business income for VAT-registered clients
- NEVER treat a non-resident as taxed on worldwide income — non-residents are Albania-source only
- NEVER rely on the [RESEARCH GAP] figures (contribution ceiling, monthly-table reconciliation, Decision 753 list, depreciation rates) without reviewer confirmation
- NEVER present tax calculations as definitive -- always label as estimated

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
