---
name: iceland-income-tax
description: Use this skill whenever asked about Iceland (Ísland) personal income tax for self-employed individuals and employees. Trigger on phrases like "how much tax do I pay in Iceland", "skattframtal", "RSK 1.01", "income tax return Iceland", "staðgreiðsla", "reiknað endurgjald", "calculated remuneration", "persónuafsláttur", "personal tax credit", "útsvar", "municipal tax", "tryggingagjald", "lífeyrissjóður pension", "capital income tax 22%", "VSK / VAT registration", "Skatturinn", or any question about filing or computing income tax for a self-employed (sjálfstætt starfandi) or employed individual resident in Iceland. Also trigger when preparing or reviewing an annual return (skattframtal) or business income statement (rekstrarframtal RSK 4.11), computing deductible expenses, or advising on monthly withholding (staðgreiðsla). This skill covers the 3-bracket combined state + municipal income tax, personal tax credit, capital income tax, mandatory occupational pension, tryggingagjald, calculated remuneration, penalties, and interaction with VAT (VSK). ALWAYS read this skill before touching any Icelandic income tax work.
version: 0.1
jurisdiction: IS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland Income Tax -- Self-Employed and Individuals

## Iceland Income Tax -- Self-Employed and Individuals Skill v0.1

> **Tier 2 (research-verified) skill.** Figures are drawn from Skatturinn (Iceland Revenue and Customs) official 2025 pages and PwC Worldwide Tax Summaries. This skill has NOT yet been signed off by an Icelandic licensed accountant/tax adviser. All outputs require professional review before filing. Items marked **[RESEARCH GAP — reviewer to confirm]** were not pinned to an authoritative source in research and must be verified.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Iceland (Ísland / Republic of Iceland) |
| Tax | Personal Income Tax (tekjuskattur) + Municipal Income Tax (útsvar), combined |
| Currency | ISK only (Icelandic króna) |
| Tax year | Calendar year (1 January -- 31 December); income year 2025, assessed/filed 2026 |
| Primary legislation | Act No. 90/2003 on Income Tax (Lög um tekjuskatt nr. 90/2003) |
| Supporting legislation | Act No. 4/1995 on Municipalities' Revenue Base (útsvar); Act No. 113/1990 on Social Security Tax (tryggingagjald); Act No. 129/1997 on Mandatory Pension Insurance and Pension Funds; Act No. 50/1988 on VAT |
| Tax authority | Skatturinn — Iceland Revenue and Customs (Ríkisskattstjóri) |
| Filing portal | skattur.is (filing); skatturinn.is (info); island.is (citizen service) |
| Filing deadline | Mid-March of the following year — income year 2025 deadline was 13 March 2026 (Skatturinn) |
| Final assessment (álagning) | No later than 10 months after year-end; generally finalised 31 May (PwC) |
| Validated by | Pending — requires sign-off by an Icelandic licensed accountant/tax adviser |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rate Brackets — 2025 (combined state income tax + average municipal útsvar; withholding rates)

**Tax Rate Brackets — 2025**  _(Skatturinn, Tax-brackets 2025 (https://www.skatturinn.is/english/individuals/tax-brackets/2025/))_

| Bracket | Monthly income (ISK) | Annual income (ISK) | Combined rate | Cumulative tax at bracket top (monthly, before personal credit) |
| --- | --- | --- | --- | --- |
| 1 | 0 – 472,005 | 0 – ~5,664,060 | 31.49% | ISK 148,634.37 |
| 2 | 472,006 – 1,325,127 | ~5,664,072 – ~15,901,524 | 37.99% | ISK 472,735.42 |
| 3 | over 1,325,127 | over ~15,901,524 | 46.29% | — |

These are the **withholding (staðgreiðsla) rates** applied monthly at source. The municipal component (útsvar) is embedded in each combined rate (Skatturinn, Tax-brackets 2025). Source: Skatturinn, [Tax-brackets 2025](https://www.skatturinn.is/english/individuals/tax-brackets/2025/). Annual thresholds are arithmetic 12× the official monthly figures (Skatturinn publishes monthly). **[RESEARCH GAP — reviewer to confirm]** the state vs útsvar split inside the combined rates; Skatturinn does not itemise it on the brackets page.

**Cumulative tax check (monthly):** Bracket 1 top = 472,005 × 31.49% = **148,634.37**. Bracket 2 top = 148,634.37 + (1,325,127 − 472,005) × 37.99% = 148,634.37 + 853,122 × 37.99% = 148,634.37 + 324,101.05 = **472,735.42**.

### Personal Tax Credit (persónuafsláttur) — 2025

**Personal Tax Credit (persónuafsláttur) — 2025**  _(Skatturinn, Key rates and amounts 2025)_

| Item | Monthly (ISK) | Annual (ISK) |
| --- | --- | --- |
| Personal tax credit | 68,691 | 824,288 |

Subtracted from **computed tax** (not from income). Unused portion is transferable between spouses. Source: Skatturinn, [Key rates and amounts 2025](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2025/). (PwC/island.is round-figure cited as 824,292 — use the Skatturinn figure 824,288.)

### Other Income-Tax Rates — 2025

**Other Income-Tax Rates — 2025**

| Item | Rate | Notes | Source |
| --- | --- | --- | --- |
| Capital income tax (fjármagnstekjuskattur) | 22% (flat) | Capital gains (real estate, shares), dividends, interest. First ISK 300,000/yr of interest + shareholding income per person is tax-free. | Skatturinn key rates 2025 |
| Municipal tax component (útsvar) | 14.94% withheld; 12.44%–14.94% final by municipality | Embedded in combined bracket rates; final depends on residence municipality. | PwC, Taxes on personal income |
| Directors'/committee fees | 20% income tax + municipal tax | Special withholding category. | PwC, Taxes on personal income |
| Children born 2010 or later | 6% | On a child's income exceeding ISK 180,000/yr. | Skatturinn key rates 2025 |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown municipal tax rate | Use 14.94% (max/withholding rate); final assessment may be lower (PwC) |
| Unknown tryggingagjald rate | Use 6.35% general rate (Skatturinn / PwC) |
| Unknown minimum wage | No statutory minimum — confirm the applicable collective agreement; do NOT hard-code a figure |
| Unknown self-employed remuneration | STOP — calculated remuneration (reiknað endurgjald) must be set at market salary per Skatturinn's occupation table |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT (VSK) registration status | Assume registered if 12-month turnover > ISK 2,000,000; otherwise unregistered |
| Unknown residency | STOP — non-resident rules differ |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full income year in CSV, PDF, or pasted text, plus confirmation of residency status (resident/non-resident), employment status (employee vs self-employed sole proprietor), and (for self-employed) the occupation category for calculated remuneration (reiknað endurgjald).

**Recommended** -- all sales invoices, purchase invoices/receipts, monthly staðgreiðsla (withholding) records, pension fund (lífeyrissjóður) statements, prior-year skattframtal (RSK 1.01) or assessment (álagning), VAT (VSK) registration confirmation.

**Ideal** -- complete income and expenditure account (rekstrarframtal RSK 4.11), asset register, A1 certificate (if EEA worker), municipality of residence, spousal income (for personal-credit transfer).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the self-employed calculated remuneration (reiknað endurgjald) meets Skatturinn's minimum for the occupation category."

### Refusal Catalogue

- **R-IS-1 -- Residency unknown** — Residency determines whether Icelandic worldwide-income rules or limited non-resident rules apply. This skill cannot compute tax without confirming the client is resident in Iceland. Please confirm before proceeding.
- **R-IS-2 -- Companies / partnerships** — This skill covers individuals and sole proprietors (einstaklingar / sjálfstætt starfandi) only. Limited companies (ehf./hf.) and partnerships file separate corporate returns. Escalate to an Icelandic accountant.
- **R-IS-3 -- Calculated remuneration below occupation minimum** — Self-employed individuals must declare calculated remuneration (reiknað endurgjald) at the market salary level set in Skatturinn's annual occupation table. A figure below that minimum cannot be used. Escalate to confirm the correct category figure. (Skatturinn reiknað endurgjald table — **[RESEARCH GAP — reviewer to confirm]** the exact 2025 category amounts; not extracted in research.)
- **R-IS-4 -- Capital gains on property / shares** — Capital gains computations (real-estate disposals, share sales) under the 22% capital income regime require specialised analysis of cost base and exemptions. Escalate to an Icelandic accountant.
- **R-IS-5 -- Arrears / enforcement** — Client has outstanding tax arrears or is subject to Skatturinn collection. Late-payment interest (dráttarvextir) and the 2.5% assessment adjustment apply. Do not advise. Escalate to an Icelandic accountant immediately.
- **R-IS-6 -- VAT (VSK) return requested** — This skill covers income tax only. For Icelandic VAT (VSK), use the iceland-vat skill if available; otherwise escalate.
- **R-IS-7 -- Cross-border / A1 / expat** — EEA postings, A1 social-security certificates, and double-tax-treaty relief require cross-border analysis. Escalate to an Icelandic accountant.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. Icelandic terms appear alongside English.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + MILLIFÆRSLA (transfer), INNBORGUN (deposit), GREIÐSLA (payment) | Business income | If VSK-registered, extract net (excl. 24% / 11% VAT) |
| REIKNINGUR, ÞÓKNUN (fee), VERKTAKAGREIÐSLA (contractor payment) | Business income | Professional/contractor fees -- typical for self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Platform payout -- match to underlying invoices |
| PAYPAL PAYOUT, WISE PAYOUT, REVOLUT | Business income | International platform payout |
| UPWORK, FIVERR, TOPTAL | Business income | Freelance platform -- net of platform commission |
| LAUN (wages), STIPEND, EMPLOYER [name] | Employment income | NOT self-employment -- withholding already applied by employer |
| LEIGA, HÚSALEIGA (rent received) | Rental income | Capital/rental income — separate treatment |
| VEXTIR (interest received) | Investment income | Capital income — 22%; first ISK 300,000/yr/person tax-free |
| ARÐUR (dividend) | Investment income | Capital income — 22% |
| ENDURGREIÐSLA SKATTS, TAX REFUND | Not income | Refund from prior year — exclude |
| STYRKUR (grant), RÍKISSTYRKUR | Check nature | Capital grants exclude; revenue grants = business income |

### 3.2 Expense Patterns (Debits) -- Fully Deductible (business)

**3.2 Expense Patterns (Debits) -- Fully Deductible (business)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| HÚSALEIGA ATVINNUHÚSNÆÐI, OFFICE RENT | Office rent | Fully deductible | Dedicated business premises |
| TRYGGING (insurance, business) | Business insurance | Fully deductible | Must be business-related |
| ENDURSKOÐANDI, BÓKARI, ACCOUNTANT, AUDITOR | Accountancy fees | Fully deductible |  |
| LÖGMAÐUR, LAWYER, LEGAL (business) | Legal fees | Fully deductible | Must be business-related |
| SKRIFSTOFUVÖRUR, OFFICE SUPPLIES | Office supplies | Fully deductible |  |
| MARKAÐSSETNING, GOOGLE ADS, META ADS, AUGLÝSING | Marketing/advertising | Fully deductible |  |
| NÁMSKEIÐ, COURSE, RÁÐSTEFNA (conference) | Training/CPD | Fully deductible | Must relate to current business |
| BANKAGJALD, BANK FEE (business account) | Bank charges | Fully deductible | Business account only |
| STRIPE FEE, PAYPAL FEE | Payment processing fees | Fully deductible |  |
| LÉN (domain), HÝSING (hosting), AWS, CLOUDFLARE | IT infrastructure | Fully deductible | Recurring = expense |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**3.3 Expense Patterns (Debits) -- SaaS and Software**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Fully deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Fully deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Fully deductible |  |
| Perpetual software licence (high value) | Capital item | Capitalise / depreciate | Flag for reviewer — depreciation rate per Act 90/2003 **[RESEARCH GAP — reviewer to confirm rate]** |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ORKUVEITA, RAFMAGN (electricity), HITAVEITA (heating), VATN (water) | Utilities | T2 if home office | 100% if dedicated office; proportional if home |
| SÍMINN, VODAFONE (Sýn), NOVA, LJÓSLEIÐARI (fibre) | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| FARSÍMI, MOBILE | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**3.5 Expense Patterns (Debits) -- Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ICELANDAIR, PLAY, FLUG (flight) | Flights | Deductible if business travel | Must be wholly business purpose |
| HÓTEL, HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel | Per diem rules may apply |
| HOPP, BÍLALEIGA (car rental), LEIGUBÍLL (taxi), STRÆTÓ (bus) | Local transport | Deductible if business purpose |  |
| BENSÍN, ELDSNEYTI (fuel), N1, OLÍS, ORKAN | Vehicle fuel | T2 -- business % only | Verifiable km cost approx. ISK 83–142/km (PwC); requires mileage log |
| BÍLASTÆÐI (parking) | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| VEITINGASTAÐUR (restaurant), KVÖLDVERÐUR, CLIENT MEAL | Entertainment | Treat as NOT deductible | Flag for reviewer; default block |
| MATVÖRUVERSLUN, BÓNUS, KRÓNAN, NETTÓ, PERSONAL | Personal/groceries | NOT deductible | Private living costs |
| SEKT (fine), DRÁTTARVEXTIR (penalty interest) | Fines/penalties | NOT deductible | Public policy |
| TEKJUSKATTUR, STAÐGREIÐSLA (income tax payment) | Tax payments | NOT deductible | Income tax cannot reduce income |
| ÚTTEKT (drawings), PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (depreciate)

**3.7 Expense Patterns (Debits) -- Capital Items (depreciate)**

| Pattern | Category | Notes |
| --- | --- | --- |
| FARTÖLVA (laptop), TÖLVA (computer), MACBOOK | Computer hardware | Depreciate per Act 90/2003 — **[RESEARCH GAP — reviewer to confirm rate]** |
| PRENTARI (printer), SKANNI | Office equipment | Depreciate — **[RESEARCH GAP — reviewer to confirm rate]** |
| HÚSGÖGN (furniture), SKRIFBORÐ (desk) | Furniture/fittings | Depreciate — **[RESEARCH GAP — reviewer to confirm rate]** |
| BÍLL, VEHICLE (business) | Motor vehicle | Depreciate, business % only — **[RESEARCH GAP — reviewer to confirm rate]** |

> **Note on depreciation rates.** Icelandic depreciation (fyrningar) rates for business assets are set under Act No. 90/2003. The research data did not extract the per-asset percentages, so they are marked as research gaps. Do NOT invent rates — flag every capital item for reviewer to apply the correct fyrning rate.

### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MILLIFÆRSLA MILLI EIGIN REIKNINGA, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| LÁN (loan), AFBORGUN LÁNS (loan repayment, principal) | EXCLUDE | Loan principal movement |
| LÍFEYRISSJÓÐUR, PENSION FUND (employee 4%) | Pension deduction | Deductible from income tax base (Section 5.5), NOT a business expense |
| VSK GREIÐSLA, VAT PAYMENT | EXCLUDE | VAT liability payment, not expense |
| STAÐGREIÐSLA (withholding remitted) | EXCLUDE | Credit against final liability, not an expense |

### 3.9 Icelandic Banks -- Statement Format Reference

**3.9 Icelandic Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Landsbankinn | MILLIFÆRSLA, GREIÐSLA, KORTAFÆRSLA, GJALD | PDF/CSV; date format DD.MM.YYYY |
| Íslandsbanki | MILLIFÆRSLA, BEINGREIÐSLA, KORT | PDF/CSV; counterparty in description |
| Arion banki | FÆRSLA, KORTAFÆRSLA, GJALD | PDF; CSV export available |
| Kvika / indó / Auður | MILLIFÆRSLA, KORT | Digital-first; clean CSV |
| Revolut / Wise (business) | PAYMENT, TRANSFER, CARD PAYMENT | CSV; multi-currency -- use ISK amounts |

## Section 4 -- Worked Examples

All tax figures use the 2025 combined withholding brackets (31.49% / 37.99% / 46.29%) and the monthly personal tax credit of ISK 68,691 (Skatturinn). Arithmetic is recomputed end-to-end below.

### Example 1 -- Employee monthly withholding (single bracket)

**Input line:**
`25.01.2025 ; LANDSBANKINN ; LAUN — VINNUVEITANDI EHF ; +550,000.00 ; ISK`

**Reasoning:**
Monthly wage of ISK 550,000. Falls in brackets 1 and 2 (over 472,005).
- Bracket 1: 472,005 × 31.49% = 148,634.37
- Bracket 2: (550,000 − 472,005) = 77,995 × 37.99% = 29,630.30
- Gross tax = 178,264.67; less personal credit 68,691 = **net withholding 109,573.67**.

**Classification:** Employment income; withholding applied by employer. Net monthly tax = ISK 109,573.67.

### Example 2 -- Self-employed calculated remuneration (annual)

**Input:** Sole proprietor, calculated remuneration (reiknað endurgjald) ISK 9,000,000/yr = ISK 750,000/mo.

**Reasoning (monthly tax):**
- Bracket 1: 472,005 × 31.49% = 148,634.37
- Bracket 2: (750,000 − 472,005) = 277,995 × 37.99% = 105,610.30
- Gross monthly tax = 254,244.67; less credit 68,691 = **185,553.67/mo**.
- Annual income tax = 185,553.67 × 12 = **ISK 2,226,644.10**.

**Other levies on the same base:**
- Mandatory pension, employee 4%: 9,000,000 × 4% = ISK 360,000 (deductible from income tax base — see Section 5.5; example shown gross for illustration).
- Mandatory pension, employer 11.5% (self-employed pays both): 9,000,000 × 11.5% = ISK 1,035,000. Total pension 15.5% = ISK 1,395,000 (360,000 + 1,035,000 = 1,395,000 ✓).
- Tryggingagjald (general 6.35%): 9,000,000 × 6.35% = ISK 571,500.

**Classification:** Self-employed remuneration; income tax, pension, and tryggingagjald all due. Reviewer must confirm reiknað endurgjald meets the occupation minimum.

### Example 3 -- Capital income (interest above tax-free threshold)

**Input line:**
`31.12.2025 ; ARION BANKI ; VEXTIR — SPARNAÐUR ; +520,000.00 ; ISK`

**Reasoning:**
Interest income ISK 520,000. First ISK 300,000/yr per person is tax-free (Skatturinn). Taxable = 520,000 − 300,000 = 220,000 at 22% flat = **ISK 48,400**.

**Classification:** Capital income tax = ISK 48,400.

### Example 4 -- Employee net pay with pension deduction

**Input line:**
`25.03.2025 ; ÍSLANDSBANKI ; LAUN — STÚDÍÓ EHF ; +600,000.00 ; ISK`

**Reasoning:**
Gross wage ISK 600,000. Mandatory employee pension 4% = ISK 24,000 reduces the income tax base. Tax base = 600,000 − 24,000 = 576,000.
- Bracket 1: 472,005 × 31.49% = 148,634.37
- Bracket 2: (576,000 − 472,005) = 103,995 × 37.99% = 39,507.70
- Gross tax = 188,142.07; less credit 68,691 = net tax 119,451.07.
- Net pay = 600,000 − 24,000 (pension) − 119,451.07 (tax) = **ISK 456,548.93**.

**Classification:** Net pay ISK 456,548.93. Employer separately pays its 11.5% pension and 6.35% tryggingagjald on top of gross.

### Example 5 -- Top bracket (high earner)

**Input:** Monthly income ISK 1,500,000 (crosses into bracket 3).

**Reasoning:**
- Bracket 1: 472,005 × 31.49% = 148,634.37
- Bracket 2: (1,325,127 − 472,005) = 853,122 × 37.99% = 324,101.05
- Bracket 3: (1,500,000 − 1,325,127) = 174,873 × 46.29% = 80,948.71
- Gross tax = 553,684.13; less credit 68,691 = **net tax 484,993.13/mo**.

**Classification:** Monthly income tax = ISK 484,993.13. Capital and pension treated separately.

### Example 6 -- Internal transfer (exclude)

**Input line:**
`15.05.2025 ; LANDSBANKINN ; MILLIFÆRSLA — EIGIN SPARNAÐARREIKNINGUR ; -2,000,000.00 ; ISK`

**Reasoning:**
Transfer between the client's own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Combined Progressive Income Tax

- **Combined progressive income tax** — 2025 individual income tax is a combined state income tax + municipal income tax (útsvar) on a progressive 3-bracket scale (withholding rates): 31.49% up to ISK 472,005/month; 37.99% from 472,006 to 1,325,127/month; 46.29% above 1,325,127/month. Annual thresholds are 12× the monthly figures (~ISK 5,664,060 and ~ISK 15,901,524).  _(Act No. 90/2003 on Income Tax; Act No. 4/1995 (útsvar); Skatturinn, Tax-brackets 2025)_

### 5.2 Personal Tax Credit (persónuafsláttur)

- **Personal tax credit** — The personal tax credit for 2025 is ISK 68,691/month = ISK 824,288/year, subtracted from computed tax (not from income). Unused credit is transferable between spouses.  _(Skatturinn, Key rates 2025)_

### 5.3 Municipal Tax (útsvar)

- **Municipal tax (útsvar)** — The municipal component is withheld at 14.94% but the final municipal rate ranges 12.44%–14.94% depending on the municipality of residence. Use 14.94% for conservative withholding.  _(PwC)_

### 5.4 Capital Income Tax

- **Capital income tax** — Capital income (capital gains, dividends, interest) is taxed at a flat 22%. The first ISK 300,000/year of interest and shareholding income per person is tax-free.  _(Skatturinn, Key rates 2025)_

### 5.5 Mandatory Occupational Pension (lífeyrissjóður)

- **Mandatory pension** — Minimum total 15.5% of remuneration: 4% employee + 11.5% employer. Mandatory for ages 16–70. The 4% employee contribution is deductible from the income tax base. Self-employed pay both portions on their calculated remuneration. Employer contribution becomes taxable income to the employee only if it exceeds BOTH 12% of remuneration AND ISK 2,000,000/yr. Voluntary private pension (séreignarsparnaður): up to an additional 4% (employee), deductible within limits; employer match commonly up to 2%. Pension component check: 4% + 11.5% = 15.5% total ✓.  _(Act No. 129/1997; PwC)_

### 5.6 Social Security Tax (tryggingagjald)

- **Tryggingagjald** — General rate 6.35% on gross remuneration. +0.65% surcharge for fishermen (so 7.00% combined for that category). Reduced to 0.425% for workers covered by an A1 form (EEA). Employer pays it; self-employed pay it on calculated remuneration.  _(Act No. 113/1990; Skatturinn 2025 ("payroll tax 6.35%"); PwC corporate other-taxes)_

### 5.7 Calculated Remuneration (reiknað endurgjald)

- **Calculated remuneration** — Self-employed individuals must declare calculated remuneration at the market salary level for their occupation (Skatturinn's annual reiknað endurgjald table) and pay income tax, tryggingagjald, and pension on it. Withholding is generally remitted monthly. **[RESEARCH GAP — reviewer to confirm]** the exact 2025 occupation-category minimum amounts; not extracted in research. A secondary source (FreelancePay) indicates annual reiknað endurgjald under ISK 700,000 removes the employer-register obligation (tax still due) — **[RESEARCH GAP — reviewer to confirm with Skatturinn]**.  _(Act No. 90/2003; Skatturinn / island.is)_

### 5.8 VAT (VSK) Interaction

**5.8 VAT (VSK) Interaction**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (VSK-registered) | NOT income -- exclude from business income |
| Input VAT recovered (VSK-registered) | NOT an expense -- exclude |
| Non-recoverable / foreign VAT | IS an expense -- full gross is cost |
| Unregistered (below ISK 2,000,000 turnover) | All VAT paid on purchases is part of cost |

- **VAT registration threshold and rates** — VAT registration is mandatory once 12-month turnover exceeds ISK 2,000,000; register via Form RSK 5.02 within 8 days. Standard VAT rate 24%, reduced rate 11%.  _(Skatturinn, VAT page)_

### 5.9 Other Individual Levies (2025)

For income above ISK 2,474,942/yr, ages 16–69 (Skatturinn, Key rates 2025):

**5.9 Other Individual Levies (2025)**  _(Skatturinn, Key rates 2025)_

| Levy | Amount (ISK) |
| --- | --- |
| National Broadcasting Service fee (útvarpsgjald) | 21,400 |
| Senior Citizens' Construction Fund fee (gjald í Framkvæmdasjóð aldraðra) | 14,093 |

### 5.10 Filing, Assessment, and Penalties

**5.10 Filing, Assessment, and Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| Annual return (skattframtal RSK 1.01) | Pre-filled; filed online via skattur.is; deadline mid-March (13 March 2026 for income year 2025) | Skatturinn |
| Business income statement (rekstrarframtal RSK 4.11) | Filed with the annual return by sole proprietors | FreelancePay |
| Final assessment (álagning) | No later than 10 months after year-end; generally finalised 31 May | PwC |
| Under/over-payment on assessment | Shortfall increased by 2.5%; over-withholding refunded increased by 2.5% | PwC |
| Late payment after assessment | Collected over five due dates (1st of July–December), each payable within 30 days; late-payment interest (dráttarvextir) thereafter | PwC |
| Reassessment / statute of limitations | Tax authority may reassess within six years | PwC |
| Capital income / WHT returns (dividends, interest) | Quarterly: 20 Apr, 20 Jul, 20 Oct, 20 Jan; payment within 15 days | PwC |
| Late/non-filing penalty | **[RESEARCH GAP — reviewer to confirm]** — Skatturinn typically estimates income (áætlun) for non-filers and adds surcharges; exact fixed-fine mechanics not pinned to an authoritative source | Skatturinn |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home office deduction** — Calculate the proportion of the home used for business (dedicated room(s) as % of total floor area). Apply that percentage to: rent, electricity, heating (hitaveita), water, internet. A dual-use room does NOT qualify. Conservative default: 0% deduction until reviewer confirms a genuinely dedicated workspace and floor-area basis.  _(Act No. 90/2003)_

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Client must maintain a mileage log. PwC indicates verifiable car operating costs of approx. ISK 83–142/km. Conservative default: 0% business use until mileage log provided.  _(PwC)_

### 6.3 Phone / Internet Mixed Use

- **Phone / internet mixed use** — Business use portion only; client must provide a reasonable estimate. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 Per Diem / Travel Subsistence

- **Per diem / travel subsistence** — Per diem for travel outside the contractual workplace may be deductible. Flag for reviewer to confirm the applicable per-diem rates and that travel is genuinely business.  _(PwC)_

### 6.5 Depreciation of Capital Assets (fyrningar)

- **Depreciation of capital assets** — Business assets are depreciated under Act No. 90/2003 rather than fully expensed. **[RESEARCH GAP — reviewer to confirm]** the per-asset depreciation percentages (not extracted in research). Do not invent rates.  _(Act No. 90/2003)_

### 6.6 Voluntary Private Pension (séreignarsparnaður)

- **Voluntary private pension** — Up to 4% additional employee contribution, deductible within limits; employer match commonly up to 2%. Flag for reviewer to confirm the deductible limit actually applied.

### 6.7 A1 / EEA Social-Security Coordination

- **A1 / EEA social-security coordination** — EEA workers can avoid Icelandic pension contributions with an A1 certificate if equivalent contributions are made in the home country; tryggingagjald reduced to 0.425%. Flag for reviewer to confirm the A1 certificate and home-country coverage.  _(PwC)_

## Section 7 -- Excel Working Paper Template

```
ICELAND INCOME TAX -- WORKING PAPER
Income Year: 2025  (filed/assessed 2026)
Client: ___________________________
Status: Employee / Self-employed (sole proprietor)
Municipality: ____________  Residency: Resident / Non-resident

A. GROSS INCOME
  A1. Self-employment / calculated remuneration (reiknað endurgjald)  ___________
  A2. Employment wages (LAUN)                                          ___________
  A3. Platform / contractor income                                     ___________
  A4. TOTAL earned income                                              ___________

B. DEDUCTIONS FROM INCOME TAX BASE
  B1. Mandatory pension — employee 4%                                  ___________
  B2. Voluntary private pension (séreignarsparnaður, within limit)     ___________
  B3. Verifiable business expenses (self-employed)                     ___________
  B4. TOTAL deductions                                                 ___________

C. INCOME TAX BASE (A4 - B4)                                           ___________

D. INCOME TAX (combined withholding brackets, pass to engine)
  D1. Bracket 1  (up to 472,005/mo @ 31.49%)                           ___________
  D2. Bracket 2  (472,006–1,325,127/mo @ 37.99%)                       ___________
  D3. Bracket 3  (over 1,325,127/mo @ 46.29%)                          ___________
  D4. Gross income tax                                                 ___________
  D5. Less: personal tax credit (68,691/mo; 824,288/yr)                ___________
  D6. NET INCOME TAX (D4 - D5)                                         ___________

E. CAPITAL INCOME (separate 22% schedule)
  E1. Interest + shareholding income                                   ___________
  E2. Less: tax-free first 300,000/person                              ___________
  E3. Capital gains (property/shares)                                  ___________
  E4. Capital income tax = (E1-E2+E3) × 22%                            ___________

F. SOCIAL LEVIES (self-employed pays employer portions)
  F1. Tryggingagjald 6.35% × calculated remuneration                  ___________
  F2. Pension employer 11.5% × calculated remuneration                ___________

G. OTHER LEVIES (if income > 2,474,942; ages 16–69)
  G1. Útvarpsgjald (broadcasting)                21,400 (if applicable) ___________
  G2. Framkvæmdasjóður aldraðra (elderly fund)   14,093 (if applicable) ___________

H. RECONCILIATION
  H1. Less: staðgreiðsla withheld during year                          ___________
  H2. Assessment adjustment ±2.5%                                       ___________
  H3. TAX DUE / REFUND                                                 ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Calculated remuneration meets occupation minimum?
  [ ] Municipality útsvar rate confirmed (12.44%–14.94%)?
  [ ] Tryggingagjald rate confirmed (6.35% / 0.425% A1 / +0.65% fishermen)?
  [ ] Depreciation rates applied (research gap — reviewer to set)?
  [ ] Home office / vehicle / phone business % confirmed?
  [ ] Capital income tax-free 300,000 applied per person?
  [ ] VSK registration status confirmed?
  [ ] A1 certificate (if EEA)?
```

## Section 8 -- Bank Statement Reading Guide

### Icelandic Bank Statement Formats

**Icelandic Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Landsbankinn | PDF, CSV | Dagsetning (date), Skýring (description), Upphæð (amount), Staða (balance) | Most common; date format DD.MM.YYYY |
| Íslandsbanki | PDF, CSV | Dagsetning, Tilvísun (reference), Upphæð, Staða | Card transactions show merchant name |
| Arion banki | PDF, CSV | Dagsetning, Texti, Debet/Kredit, Staða | CSV export available |
| Kvika / indó / Auður | CSV | Date, Counterparty, Amount | Digital-first; clean data |
| Revolut / Wise (business) | CSV | Date, Counterparty, Amount, Currency | Multi-currency -- use ISK amounts |

### Key Icelandic Banking and Tax Terms

**Key Icelandic Banking and Tax Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| MILLIFÆRSLA | Transfer | Check direction for income/expense |
| BEINGREIÐSLA / DD | Direct debit | Regular expense (utility, subscription) |
| KORTAFÆRSLA / KORT | Card payment | Expense -- check merchant |
| INNBORGUN / GREIÐSLA | Deposit / payment | Potential income |
| LAUN | Wages | Employment income |
| ÞÓKNUN / VERKTAKAGREIÐSLA | Fee / contractor payment | Self-employment income |
| VEXTIR | Interest | Capital income (22%) — or a bank charge if a debit |
| ARÐUR | Dividend | Capital income (22%) |
| LEIGA / HÚSALEIGA | Rent | Rental income (in) or office rent (out) |
| GJALD / BANKAGJALD | Fee / bank charge | Deductible if business |
| LÍFEYRISSJÓÐUR | Pension fund | Pension deduction (4% employee) |
| STAÐGREIÐSLA | Withholding (PAYE) | Tax remittance — exclude as expense |
| TRYGGINGAGJALD | Social security tax | Employer/self-employed levy |
| VSK | VAT | Exclude VAT collected/recovered |
| ÚTTEKT | Withdrawal / drawings | Not an expense |
| SEKT / DRÁTTARVEXTIR | Fine / penalty interest | Not deductible |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ICELAND INCOME TAX
1. Are you tax-resident in Iceland? Which municipality?
2. Are you an employee, a self-employed sole proprietor, or both?
3. (Self-employed) What is your occupation category for calculated remuneration (reiknað endurgjald)?
4. Are you registered for VAT (VSK)? Is your 12-month turnover above ISK 2,000,000?
5. Home office: dedicated room or shared space? If dedicated, what % of floor area?
6. Vehicle: used for business? What % is business use? Do you keep a mileage log?
7. Phone/internet: what % is business use?
8. What pension fund (lífeyrissjóður) do you contribute to? Any voluntary private pension?
9. Are you an EEA worker with an A1 certificate?
10. Any capital income (interest, dividends, property/share gains)?
11. Is your spouse able to use any unused personal tax credit?
```

## Section 10 -- Reference Material

### Key Legislation References

**Key Legislation References**

| Topic | Reference |
| --- | --- |
| Income tax (state + framework) | Act No. 90/2003 on Income Tax |
| Municipal income tax (útsvar) | Act No. 4/1995 on Municipalities' Revenue Base |
| Social security tax (tryggingagjald) | Act No. 113/1990 |
| Mandatory pension | Act No. 129/1997 |
| VAT (VSK) | Act No. 50/1988 |
| Forms | RSK 1.01 (return), RSK 4.11 (business statement), RSK 5.02 (registration/VAT) |

### 2025 Key Figures (with provenance)

**2025 Key Figures (with provenance)**

| Item | Value (ISK) | Source |
| --- | --- | --- |
| Bracket 1 ceiling (monthly) | 472,005 @ 31.49% | Skatturinn, Tax-brackets 2025 |
| Bracket 2 ceiling (monthly) | 1,325,127 @ 37.99% | Skatturinn, Tax-brackets 2025 |
| Bracket 3 (monthly) | over 1,325,127 @ 46.29% | Skatturinn, Tax-brackets 2025 |
| Personal tax credit (monthly / annual) | 68,691 / 824,288 | Skatturinn, Key rates 2025 |
| Capital income tax | 22% flat | Skatturinn, Key rates 2025 |
| Tax-free interest/shareholding income | 300,000 / person / yr | Skatturinn, Key rates 2025 |
| Children (born 2010+) rate / threshold | 6% above 180,000/yr | Skatturinn, Key rates 2025 |
| Broadcasting fee / threshold | 21,400 above income 2,474,942/yr | Skatturinn, Key rates 2025 |
| Elderly fund fee | 14,093 above income 2,474,942/yr | Skatturinn, Key rates 2025 |
| Mandatory pension total / employee / employer | 15.5% / 4% / 11.5% | PwC, Other taxes |
| Tryggingagjald (general) | 6.35% (+0.65% fishermen; 0.425% A1) | Skatturinn / PwC |
| VAT standard / reduced | 24% / 11% | Skatturinn, VAT page |
| VAT registration threshold | 2,000,000 turnover / 12 months | Skatturinn, VAT page |
| Director/committee fees | 20% income tax + municipal | PwC, Taxes on personal income |
| Minimum wage | No statutory minimum — collective-agreement based; ~425,000–455,000/mo indicative only **[RESEARCH GAP — reviewer to confirm against the relevant collective agreement]** | commoner-law.com (secondary) |
| Self-employed employer-register exemption | annual reiknað endurgjald under 700,000 **[RESEARCH GAP — reviewer to confirm with Skatturinn]** | FreelancePay (secondary) |
| VIRK rehabilitation fund levy | 0.10% of salaries (employer) **[RESEARCH GAP — reviewer to confirm against collective agreement]** | Rivermate (secondary) |

### Source List

- Skatturinn — Tax-brackets 2025: https://www.skatturinn.is/english/individuals/tax-brackets/2025/
- Skatturinn — Key rates and amounts 2025: https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2025/
- Skatturinn — Filing a tax return: https://www.skatturinn.is/english/individuals/filing-a-tax-return/
- Skatturinn — Value Added Tax (VAT): https://www.skatturinn.is/english/companies/value-added-tax/
- PwC — Iceland Individual: Taxes on personal income / Other taxes / Deductions / Tax administration: https://taxsummaries.pwc.com/iceland/individual/
- PwC — Iceland Corporate: Other taxes (tryggingagjald, VAT): https://taxsummaries.pwc.com/iceland/corporate/other-taxes
- Ísland.is — Personal tax credit and income tax brackets / Self-employed: https://island.is/en/

### Test Suite

**Test 1 -- Employee, single bracket-2 wage.**
Input: Monthly wage ISK 550,000, no pension adjustment shown.
Expected: Gross tax = 472,005 × 31.49% + 77,995 × 37.99% = 148,634.37 + 29,630.30 = 178,264.67; less credit 68,691 = **net tax ISK 109,573.67/mo**.

**Test 2 -- Self-employed, calculated remuneration 9,000,000/yr.**
Input: reiknað endurgjald ISK 750,000/mo.
Expected: Monthly tax = 148,634.37 + (277,995 × 37.99%) − 68,691 = 148,634.37 + 105,610.30 − 68,691 = 185,553.67; annual = **ISK 2,226,644.10**. Pension total 15.5% = ISK 1,395,000 (4% employee 360,000 + 11.5% employer 1,035,000). Tryggingagjald 6.35% = ISK 571,500.

**Test 3 -- Capital interest above threshold.**
Input: Interest ISK 520,000.
Expected: (520,000 − 300,000) × 22% = **ISK 48,400**.

**Test 4 -- Employee net pay with 4% pension.**
Input: Gross wage ISK 600,000.
Expected: base 576,000; gross tax 188,142.07; net tax 119,451.07; **net pay ISK 456,548.93** (600,000 − 24,000 pension − 119,451.07).

**Test 5 -- Top bracket.**
Input: Monthly income ISK 1,500,000.
Expected: 148,634.37 + (853,122 × 37.99%) + (174,873 × 46.29%) − 68,691 = 148,634.37 + 324,101.05 + 80,948.71 − 68,691 = **net tax ISK 484,993.13/mo**.

**Test 6 -- Child income.**
Input: Child born 2012, income ISK 400,000.
Expected: (400,000 − 180,000) × 6% = **ISK 13,200**.

**Test 7 -- Personal tax credit cancels small wage.**
Input: Monthly wage ISK 200,000 (bracket 1 only).
Expected: 200,000 × 31.49% = 62,980; less credit 68,691 → tax floored at 0 (unused credit 5,711 may carry/transfer). **Net tax ISK 0**.

## PROHIBITIONS

- **Confirm tax residency before applying brackets** — NEVER apply the brackets without confirming Icelandic tax residency.
- **Self-employed calculated remuneration minimum** — NEVER use a self-employed calculated remuneration (reiknað endurgjald) below the Skatturinn occupation minimum.
- **No statutory minimum wage in Iceland** — NEVER hard-code a statutory minimum wage — Iceland has none; rates are set by collective agreements.
- **Personal tax credit application** — NEVER subtract the personal tax credit from income — it is subtracted from computed tax.
- **Tax-free interest and shareholding income threshold** — 300,000 ISK/yr (per person)
- **VAT exclusion from business income** — NEVER include VAT (VSK) collected on sales in business income for registered clients.
- **Non-deductible items** — NEVER treat income tax, fines, drawings, or loan principal as deductible expenses.
- **Depreciation rates must not be invented** — NEVER invent depreciation (fyrning) rates — flag capital items for the reviewer.
- **Tax calculations must be labeled estimated** — NEVER present tax calculations as definitive — always label as estimated and route through the deterministic engine.
- **Tryggingagjald rate** — 6.35% general (or 0.425% A1 / +0.65% fishermen) (without reviewer confirmation not to be varied)

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
