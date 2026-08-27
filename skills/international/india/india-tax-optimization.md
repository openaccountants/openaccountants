---
name: india-tax-optimization
description: Use this skill when advising on LEGAL tax minimization strategies for Indian taxpayers — salaried individuals, self-employed professionals, and business owners. Trigger on phrases like "reduce my tax India", "tax planning", "80C", "80D", "old vs new regime", "HRA", "NPS", "Section 24", "presumptive taxation", "capital gains", "GST input credit", or any question about legally minimizing Indian income tax. Covers regime selection, deduction optimization, capital allowances, loss set-off, timing, GST planning, social security, and red lines. ALWAYS read this skill before giving Indian tax optimization advice.
version: 1.0
jurisdiction: IN
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mayur Deokar
review_status: current
depends_on:
  - bookkeeping-workflow-base
category: tax-optimization
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Tax Optimization

## India — Tax Optimization Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by Mayur Deokar on 2026-06-06. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.

### Tax Optimization

- **Annual exemption** — ₹1,25,000  _(ITA s 112A)_
- **s 80C (PPF, ELSS, LIC, EPF)** — ₹1,50,000 combined cap  _(ITA s 80C)_
- **s 80CCD(1B) (NPS extra)** — ₹50,000 over and above 80C  _(ITA s 80CCD(1B))_
- **s 80D (health insurance)** — ₹25,000 self + ₹25,000 parents (₹50,000 if senior)  _(ITA s 80D)_
- **s 24(b) (home loan interest)** — ₹2,00,000 (self-occupied)  _(ITA s 24(b))_
- **s 80E (education loan interest)** — No cap (up to 8 years)  _(ITA s 80E)_
- **s 80GG (rent, no HRA)** — ₹60,000/year cap is correct, but deduction is the least of: (a) ₹5,000/month (₹60,000/year), (b) 25% of total income, or (c) actual rent minus 10% of total income  _(ITA s 80GG)_
- **s 80TTA (savings interest)** — ₹10,000 (₹50,000 for seniors under 80TTB)  _(ITA s 80TTA/80TTB)_
- **Standard deduction** — ₹75,000  _(Finance Act 2024)_
- **Employer NPS (s 80CCD(2))** — Up to 14% of basic  _(ITA s 80CCD(2))_
- **Home loan interest (let-out)** — No limit (rented property)  _(ITA s 24(b))_
- **Everything else (80C, 80D, HRA)** — NOT available in new regime  _(ITA s 115BAC)_
- **Buildings (factory)** — 10%  _(ITA s 32)_
- **Buildings (other)** — 5%  _(ITA s 32)_
- **Plant and machinery (general)** — 15%
- **Computers and software** — 40%  _(ITA s 32)_
- **Motor vehicles** — 15% (30% commercial)  _(ITA s 32)_
- **Intangible assets (patents, know-how)** — 25%
- **Business loss** — Any head except salary; 8 years carry-forward  _(ITA s 72)_
- **STCL** — Against STCG or LTCG; 8 years  _(ITA s 74)_
- **LTCL** — Against LTCG only; 8 years  _(ITA s 74)_
- **House property loss** — Any income, capped ₹2,00,000/year; 8 years  _(ITA s 71B)_
- **Unabsorbed depreciation** — Unlimited carry-forward  _(ITA s 32(2))_
- **LTCG on Listed Equity – Annual exemption** — ₹1,25,000  _(ITA s 112A)_

## Section 1 — Quick Reference

**Section 1 — Quick Reference**

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR (₹) |
| Tax year | Financial Year: 1 April – 31 March (FY 2026-27) |
| Primary legislation | Income Tax Act, 2025 (replacing ITA 1961 from 1 April 2026); section references below show both old (1961) and new (2025) numbers |
| Anti-avoidance | GAAR (Chapter X-A / Chapter XIX of IT Act 2025); SAAR provisions throughout |
| Tax authority | Central Board of Direct Taxes (CBDT); Income Tax Department |
| Filing deadline | 31 July (individuals without audit); 31 October (businesses requiring audit) |
| Individual top rate | 30% + 4% health & education cess = 31.2% (old regime); surcharge up to 25% on high incomes |
| Corporate tax (domestic, new manufacturing) | 15% + cess (s 115BAB) |
| Corporate tax (domestic, general) | 22% + cess (s 115BAA) or 25%/30% under regular provisions |
| GST rates | 0%, 5%, 12%, 18%, 28% |

### New Regime Tax Slabs (Default from FY 2025-26 onwards)

**New Regime Tax Slabs (Default from FY 2025-26 onwards)**

| Taxable Income (₹) | Rate |
| --- | --- |
| 0 – 4,00,000 | 0% |
| 4,00,001 – 8,00,000 | 5% |
| 8,00,001 – 12,00,000 | 10% |
| 12,00,001 – 16,00,000 | 15% |
| 16,00,001 – 20,00,000 | 20% |
| 20,00,001 – 24,00,000 | 25% |
| 24,00,001+ | 30% |

- **Section 87A rebate** — zero tax up to ₹12,00,000 taxable income (₹12,75,000 for salaried with standard deduction) under new regime.

### Old Regime Tax Slabs

**Old Regime Tax Slabs**

| Taxable Income (₹) | Rate |
| --- | --- |
| 0 – 2,50,000 | 0% |
| 2,50,001 – 5,00,000 | 5% |
| 5,00,001 – 10,00,000 | 20% |
| 10,00,001+ | 30% |

- **Old regime opt-in** — Old regime allows HRA, 80C, 80D, Section 24(b), and other deductions. Must opt in (new regime is default).

## Section 2 — Income Splitting & Structuring

### Old Regime vs New Regime Selection

- **New regime wins when** — total deductions (excluding standard deduction) are below ~₹4,50,000–₹5,50,000. Common for young professionals without home loans, low rent, minimal investments.
- **Old regime wins when** — total deductions exceed ~₹5,50,000. Typical triggers: Active home loan (₹2,00,000 interest under Section 24(b) / new s 55(1)); Metro rent with high HRA exemption (Section 10(13A)); Maxed 80C (₹1,50,000) + 80CCD(1B) NPS (₹50,000) + 80D health insurance (₹25,000+)
- **Decision rule** — compute tax under both regimes every year. The regime can be switched annually for salaried individuals (employees must inform employer at start of FY; ITR allows final choice).

### Sole Proprietor vs Company vs LLP

- **Sole proprietor** — presumptive taxation available under s 44AD (new s 68) — 6% of digital receipts / 8% of cash receipts deemed profit if turnover ≤₹3 crore. No books of account required. Profit taxed at individual slab rates.  _(s 44AD / new s 68)_
- **LLP** — no dividend distribution tax. Partners taxed on profit share (exempt under s 10(2A)). Remuneration to partners: deductible to LLP, taxable to partner. Effective combined rate can be lower than individual rates at higher profit levels.  _(s 10(2A))_
- **Private Limited Company (Pvt Ltd)** — 22% + cess (s 115BAA) = ~25.17% effective. Dividends taxed to shareholder at slab rates. DDT abolished from FY 2020-21.  _(s 115BAA)_

### Family Structuring

- **HUF (Hindu Undivided Family)** — separate taxable entity with its own ₹2,50,000 exemption and deductions. Useful for joint family assets. Can invest in 80C instruments independently.
- **Spouse salary** — pay spouse for genuine work in the business. Must be reasonable and documented. Otherwise clubbing provisions (s 64 / new s 14) apply.  _(s 64 / new s 14)_
- **Minor child income** — clubbed with higher-earning parent (exemption: ₹1,500/child). Exception: income from child's own manual work or special talent.

## Section 3 — Deductions Most People Miss

### Old Regime Deductions (New Section Numbers from IT Act 2025)

**Old Regime Deductions (New Section Numbers from IT Act 2025)**

| Deduction | Old s | New s | Limit | Notes |
| --- | --- | --- | --- | --- |
| PPF, ELSS, LIC, EPF, SSY, tuition fees | 80C | 123 | ₹1,50,000 | Combined cap across all instruments |
| NPS employee extra contribution | 80CCD(1B) | 124(3) | ₹50,000 | Over and above ₹1.5L cap. Old regime only |
| Employer NPS contribution | 80CCD(2) | 124(2) | 14% of basic (new regime) / 10% (old) | **Available in BOTH regimes** |
| Health insurance premium | 80D | 126 | ₹25,000 self + ₹25,000 parents (₹50,000 if senior) | Preventive health check-up ₹5,000 within limit |
| Home loan interest (self-occupied) | 24(b) | 55(1) | ₹2,00,000 | Old regime only for self-occupied |
| Education loan interest | 80E | 129 | No cap (up to 8 years) | Often overlooked. Interest component only |
| Rent paid (no HRA received) | 80GG | 134 | ₹60,000/year | For self-employed or those without HRA |
| Donations | 80G | 133 | 50% or 100% of donation | Qualifying institutions only |
| Disabled dependent | 80DD | 127 | ₹75,000/₹1,25,000 | Severe disability higher limit |
| Interest on savings account | 80TTA | 137 | ₹10,000 | ₹50,000 for senior citizens (80TTB/138) |

### New Regime Deductions (Limited)

**New Regime Deductions (Limited)**

| Deduction | Available? | Notes |
| --- | --- | --- |
| Standard deduction | Yes — ₹75,000 | Salaried and pensioners |
| Employer NPS (80CCD(2)/124(2)) | Yes | Up to 14% of basic |
| Home loan interest (let-out property) | Yes | No limit on interest for rented property |
| Family pension deduction | Yes | ₹15,000 or 1/3 of pension, whichever is lower |
| Agniveer Corpus (80CCH(2)) | Yes | Specific to Agniveer scheme |
| Everything else (80C, 80D, HRA, etc.) | No | Forfeited in exchange for lower rates |

## Section 4 — Capital Allowances Optimization

### Depreciation (Business Income)

**Depreciation (Business Income)**

| Asset Block | Rate (WDV) |
| --- | --- |
| Buildings (factory) | 10% |
| Buildings (other) | 5% |
| Furniture and fittings | 10% |
| Plant and machinery (general) | 15% |
| Computers and software | 40% |
| Motor vehicles | 15% (30% for commercial vehicles in certain cases) |
| Intangible assets (patents, know-how) | 25% |

- **Additional depreciation** — 20% in the first year on new plant and machinery (manufacturing sector, cost >₹25,000). Not available for second-hand assets, office equipment, or vehicles.

### Presumptive Taxation (s 44AD / new s 68)

- **Presumptive taxation businesses** — Businesses with turnover ≤₹3 crore (if digital receipts ≥95% of total): deemed profit at 6% of digital and 8% of cash receipts. No requirement to maintain books. No depreciation claim needed — already factored into deemed rate.  _(s 44AD / new s 68)_
- **Professionals (s 44ADA / new s 69)** — gross receipts ≤₹75 lakh → deemed profit at 50%. Covers doctors, lawyers, architects, CAs, engineers, etc.  _(s 44ADA / new s 69)_

## Section 5 — Loss Utilization

### Set-Off Rules

**Set-Off Rules**

| Loss Type | Set Off Against |
| --- | --- |
| Business loss | Any head of income EXCEPT salary (within same year) |
| Capital loss — short-term | Short-term or long-term capital gains |
| Capital loss — long-term | Long-term capital gains only |
| House property loss | Any income, capped at ₹2,00,000 per year |
| Speculation business loss | Speculation business income only |

### Carry Forward

**Carry Forward**

| Loss Type | Carry Forward Period |
| --- | --- |
| Business loss | 8 years |
| Capital loss | 8 years |
| Unabsorbed depreciation | Unlimited |
| House property loss | 8 years |

- **Filing deadline requirement** — Return must be filed by the due date (s 139(1)) to carry forward losses (except house property loss and unabsorbed depreciation). Missing the deadline forfeits carry-forward.  _(s 139(1))_

## Section 6 — Timing Strategies

**Section 6 — Timing Strategies**

| Strategy | Detail |
| --- | --- |
| Invest in 80C by 31 March | ELSS (3-year lock-in), PPF, LIC premiums, SSY, NPS. Last-minute investments still qualify for current FY deduction |
| Advance tax instalments | Due 15 June (15%), 15 Sept (45%), 15 Dec (75%), 15 March (100%). Defer to later instalments if income is seasonal — avoids unnecessary early payments |
| Harvesting LTCG exemption (listed equity) | LTCG on listed shares/equity MFs: ₹1,25,000 exempt annually (s 112A). Sell and rebuy annually to crystallise gains within exemption |
| Rent receipts | Collect and preserve rent receipts. If HRA claimed, landlord PAN mandatory if rent >₹1,00,000/year |
| Medical bills | Aggregate family medical expenses before 31 March for 80D claims. Preventive health check-up within ₹5,000 sub-limit |
| Capital gains reinvestment | s 54 (residential house from house sale), s 54EC (specified bonds — ₹50 lakh cap, 5-year lock-in). Invest within specified timelines to defer/exempt gains |
| NPS contribution timing | Employer NPS: ensure reflected in Form 16 / Form 130 (new). Self-contribution: invest by 31 March for current-year deduction |

## Section 7 — GST Optimization

**Section 7 — GST Optimization**

| Topic | Detail |
| --- | --- |
| Registration threshold | ₹40 lakh for goods (₹20 lakh in special category states); ₹20 lakh for services (₹10 lakh in special category states) |
| Composition scheme | Turnover ≤₹1.5 crore: pay 1% (manufacturers/traders), 5% (restaurants), 6% (services). No input tax credit. No inter-state supply |
| Input Tax Credit (ITC) | Claim GST on business purchases. Must be reflected in GSTR-2B. Reverse charge on specified goods/services |
| E-invoicing | Mandatory for turnover >₹5 crore (from 1 Aug 2023). Generates IRN via NIC portal. Ensures ITC accuracy |
| Inverted duty structure refund | If input GST rate > output GST rate, claim refund of accumulated ITC |
| Export — zero-rated | Exports are zero-rated. Option: export under LUT (Letter of Undertaking) without paying IGST, or pay IGST and claim refund |
| Place of supply rules | Critical for services: B2B services generally taxed at recipient location. Optimise for IGST vs SGST+CGST |

## Section 8 — Social Security Optimization

### EPF (Employees' Provident Fund)

- **Contribution structure** — Employee contributes 12% of basic + DA; employer matches 12% (8.33% to EPS, 3.67% to EPF)
- **Tax treatment** — employee contribution deductible under 80C. Employer contribution exempt up to ₹7.5 lakh/year (combined with NPS, superannuation)
- **Interest taxability** — Interest taxable if employee contribution exceeds ₹2.5 lakh/year (from FY 2021-22)

### NPS (National Pension System)

- **Employer contribution (80CCD(2)/124(2))** — deductible up to 14% of basic (central govt) or 10% (others). Available in BOTH regimes — the single most powerful deduction in the new regime.  _(80CCD(2)/124(2))_
- **Employee self-contribution (80CCD(1B)/124(3))** — additional ₹50,000 deduction. Old regime only.  _(80CCD(1B)/124(3))_
- **At retirement** — 60% lump sum tax-free; 40% must buy annuity (annuity income taxable)

### ESI (Employees' State Insurance)

- **Applicability and contribution** — Applicable if salary ≤₹21,000/month. Employee 0.75%, employer 3.25%
- **Coverage** — Medical coverage. Contributions reduce take-home but provide insurance

### Optimization

- **Maximise employer NPS** — to benefit in both regimes (14% of basic for new regime)
- **Voluntary PF contribution** — up to 80C limit if not already maxed
- **Salary structuring** — optimise basic vs allowances. Higher basic = higher EPF/NPS employer contribution (deductible) but higher PF outflow. Balance based on individual needs.

## Section 9 — Investment & Retirement

**Section 9 — Investment & Retirement**

| Instrument | Tax Treatment | Notes |
| --- | --- | --- |
| PPF | EEE (exempt-exempt-exempt) | ₹1.5L/year cap. 15-year lock-in. Interest tax-free |
| ELSS | Deduction under 80C. LTCG >₹1.25L taxed at 12.5% | 3-year lock-in. Shortest among 80C options |
| NPS | Deduction on contribution. 60% lump sum tax-free at retirement | Annuity portion taxable |
| Sukanya Samriddhi (SSY) | EEE | For girl child. ₹1.5L/year within 80C cap |
| NSC | Deduction under 80C. Interest accrued qualifies for 80C in subsequent years | 5-year lock-in |
| ULIPs | 80C deduction. Tax-free maturity if premium ≤₹2.5L/year | >₹2.5L premium: LTCG on maturity |
| Direct equity / equity MFs | STCG: 20%. LTCG >₹1.25L: 12.5%. No indexation | Annual LTCG harvesting strategy applies |
| Debt MFs | Taxed at slab rates | No indexation benefit (post FY 2023-24 rules) |
| Real estate | LTCG: 12.5% (without indexation from FY 2024-25). STCG: slab rates | s 54/54EC reinvestment exemptions available |

### Annual LTCG Harvesting

- **Harvesting strategy** — Sell listed equity/MF units showing gains up to ₹1,25,000 LTCG (exempt) on 31 March, rebuy on 1 April. Resets cost base. Zero tax on harvested gains. Repeat annually.

### GAAR (General Anti-Avoidance Rule)

- **GAAR definition and application** — Chapter X-A (old ITA) / Chapter XIX (IT Act 2025). Effective from 1 April 2017. Applies if an arrangement: (i) creates a tax benefit, (ii) the main purpose is to obtain tax benefit, and (iii) it lacks commercial substance. Consequence: tax benefit denied; income recharacterised.  _(Chapter X-A / Chapter XIX IT Act 2025)_
- **GAAR trigger threshold** — tax benefit must exceed ₹3 crore to trigger. Impermissible avoidance agreements defined broadly.

### Scrutiny Triggers

**Scrutiny Triggers**

| Trigger | Risk |
| --- | --- |
| HRA claimed without genuine rent payment | Disallowed; penalty |
| Bogus 80C/80D receipts | Prosecution possible. LIC/health insurer reports to IT dept |
| Cash deposits >₹10 lakh in savings or ₹2.5 lakh in current account | Automatic SFT reporting to IT department |
| High-value transactions (immovable property >₹30 lakh, securities >₹10 lakh) | Statement of Financial Transactions (SFT) cross-matching |
| Income mismatch with AIS (Annual Information Statement) | Most common trigger for notice u/s 148 |
| Capital gains without payment of advance tax | Interest u/s 234B and 234C |
| Gift from non-relatives exceeding ₹50,000 | Taxable as income u/s 56(2)(x) / new equivalent |
| Benami property transactions | Benami Transactions (Prohibition) Act — severe penalties including confiscation |
| Clubbing provisions violations | Transferring income-generating assets to spouse/minor → income attributed back |
| Presumptive tax with inconsistent lifestyle | Risk of scrutiny if declared income is disproportionately low |

### Absolute Prohibitions

- **NEVER advise fabricating rent receipts for HRA claims** — Prohibited
- **NEVER advise backdating investments to claim deductions in a prior year** — Prohibited
- **NEVER advise cash transactions exceeding ₹2 lakh** — penalty equal to amount, s 271DA  _(s 271DA)_
- **NEVER advise accepting or paying cash exceeding ₹10,000 for expenses** — unless specific exceptions
- **NEVER advise structuring transactions solely to stay below GAAR thresholds** — Prohibited
- **NEVER advise ignoring AIS discrepancies** — resolve before filing

## Section 11 — Annual Tax Planning Calendar

**Section 11 — Annual Tax Planning Calendar**

| When | Action |
| --- | --- |
| April | New FY begins. Choose tax regime with employer (Form 12BBA). Start SIP in ELSS/PPF. Review salary structure with HR |
| May–June | Advance tax 1st instalment due 15 June (15%). Declare HRA, LTA with employer. Submit investment declaration |
| July 31 | ITR filing deadline (non-audit individuals). Prior-year return must be filed to carry forward losses |
| September | Advance tax 2nd instalment due 15 Sept (45%). Mid-year investment review |
| October 31 | Audit report filing deadline (businesses). Review capital gains position |
| November | Execute LTCG harvesting strategy. Review medical expenses for 80D |
| December | Advance tax 3rd instalment due 15 Dec (75%). Final push on 80C investments |
| January–February | Collect rent receipts, medical bills, donation receipts. HRA landlord PAN confirmation |
| March (before 31 March) | **Critical month.** Complete 80C, 80D, NPS investments. Final advance tax instalment due 15 March (100%). Pay pending insurance premiums. Sell/rebuy for LTCG harvesting. Submit investment proofs to employer |

## Section 12 — Cash Impact Examples

### Example 1 — Old vs New Regime (Salaried, ₹15 lakh CTC)

New regime: ₹15,00,000 – ₹75,000 (standard deduction) = ₹14,25,000 taxable. Tax: ₹1,57,500 + cess = ₹1,63,800.

Old regime with deductions: ₹15,00,000 – ₹50,000 (standard) – ₹1,50,000 (80C) – ₹50,000 (80CCD(1B)) – ₹25,000 (80D) – ₹2,00,000 (home loan s 24(b)) – ₹2,40,000 (HRA) = ₹8,85,000 taxable. Tax: ₹77,000 + cess = ₹80,080.

Saving under old regime: ~₹83,720. Old regime clearly wins with ₹6.65L deductions.

### Example 2 — NPS Employer Contribution (New Regime)

Salary restructure: basic ₹8,00,000. Employer contributes 14% to NPS = ₹1,12,000.

This ₹1,12,000 is deductible in BOTH regimes. At 20% marginal rate: ₹22,400 tax saving + retirement corpus growth.

### Example 3 — LTCG Harvesting (Listed Equity)

Portfolio unrealised gains: ₹3,00,000. Sell units showing ₹1,25,000 LTCG → zero tax (exempt). Rebuy next day. Reset cost base. Remaining ₹1,75,000 deferred to next year.

Without harvesting: eventual ₹3,00,000 – ₹1,25,000 exempt = ₹1,75,000 × 12.5% = ₹21,875 tax.
With annual harvesting over 3 years: ₹0 tax. Saving: ₹21,875.

### Example 4 — Presumptive Taxation (s 44AD)

Small trader, ₹1.5 crore turnover (all digital). Deemed profit: 6% = ₹9,00,000. Tax under old regime with 80C: ~₹52,000 + cess.

Actual profit: ₹12,00,000 (8%). Electing regular taxation: higher tax + audit + compliance cost. Presumptive saves ~₹40,000+ in tax and ₹50,000+ in compliance costs.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant (CA), tax consultant, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
