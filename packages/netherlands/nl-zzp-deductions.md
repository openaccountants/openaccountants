---
name: nl-zzp-deductions
description: >
  Use this skill whenever asked about Dutch self-employed (zzp) tax deductions. Trigger on phrases like "zelfstandigenaftrek", "startersaftrek", "MKB-winstvrijstelling", "urencriterium", "1225 hours", "KIA", "kleinschaligheidsinvesteringsaftrek", "FOR", "fiscale oudedagsreserve", "meewerkaftrek", "willekeurige afschrijving", "zzp deductions", "Dutch freelancer deductions", "Netherlands self-employed tax benefits", or any question about tax deductions available to Dutch sole proprietors (eenmanszaak) and freelancers (zzp'ers). This skill covers all major ondernemersaftrek components, the MKB-winstvrijstelling, investment deductions, the hours criterion, and their interaction with Box 1 computation. ALWAYS read this skill before touching any Dutch self-employed deduction work.
version: 2.0
jurisdiction: NL
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Netherlands ZZP Deductions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

Read this whole section before computing anything.

| Field | Value |
|---|---|
| Country | Netherlands |
| Jurisdiction Code | NL |
| Primary Legislation | Wet inkomstenbelasting 2001 (Wet IB 2001), Articles 3.74-3.79a (ondernemersaftrek), Article 3.79a (MKB-winstvrijstelling), Articles 3.40-3.48 (investeringsaftrek) |
| Supporting Legislation | Uitvoeringsregeling inkomstenbelasting 2001; Belastingplan 2023 (FOR abolition); Belastingplan 2025 |
| Tax Authority | Belastingdienst (Dutch Tax and Customs Administration) |
| Filing Portal | Mijn Belastingdienst / Aangifte inkomstenbelasting |
| Tax Year | 2025 |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated By | Pending -- requires sign-off by qualified Dutch belastingadviseur or registeraccountant |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: zelfstandigenaftrek, startersaftrek, MKB-winstvrijstelling, urencriterium, KIA table, FOR abolition, computation order. Tier 2: urencriterium documentation disputes, mixed business/hobby, meewerkaftrek valuation, BV transition. Tier 3: international structures, fiscal unity, complex partnership allocations. |

**Key deduction amounts (2025):**

| Deduction | Amount | Requires Urencriterium? |
|---|---|---|
| Zelfstandigenaftrek (standard) | EUR 2,470 | YES |
| Zelfstandigenaftrek (AOW age) | EUR 1,235 (50%) | YES |
| Startersaftrek | EUR 2,123 (on top of zelfstandigenaftrek) | YES |
| MKB-winstvrijstelling | 12.7% of profit after ondernemersaftrek | NO |
| Meewerkaftrek | 1.25% - 4.00% of profit (by partner hours) | NO |

**Zelfstandigenaftrek declining schedule:**

| Year | Amount (EUR) |
|---|---|
| 2024 | 3,750 |
| 2025 | 2,470 |
| 2026 | 1,200 |
| 2027 | 900 |

**KIA table (2025):**

| Total Investment (EUR) | Deduction |
|---|---|
| 0 -- 2,900 | No deduction |
| 2,901 -- 70,602 | 28% of total investment |
| 70,603 -- 130,744 | EUR 19,769 (fixed) |
| 130,745 -- 392,230 | EUR 19,769 minus 7.56% of amount exceeding EUR 130,744 |
| > 392,230 | No deduction |

**Box 1 rates (2025):**

| Taxable Income (EUR) | Rate |
|---|---|
| 0 -- 38,441 | 35.82% |
| 38,442 -- 76,817 | 37.48% |
| 76,818+ | 49.50% |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown urencriterium status | Does NOT meet 1,225 hours (no zelfstandigenaftrek) |
| Unknown starter status | Not a starter (no startersaftrek) |
| Unknown FOR balance | No pre-2023 FOR balance |
| Unknown business structure | Eenmanszaak (sole proprietorship) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any ZZP deduction, you MUST know:

1. Business structure -- eenmanszaak, maatschap/VOF, or BV (BV is out of scope)
2. Does the client meet the urencriterium (1,225 hours)? -- required for zelfstandigenaftrek and startersaftrek
3. Is this a starter? -- determines startersaftrek eligibility
4. Gross profit from the enterprise (winst uit onderneming) -- needed to compute deduction order
5. Total business investments in the year -- needed for KIA
6. Does the fiscal partner work in the business unpaid or for less than EUR 5,000? -- meewerkaftrek
7. Does the client have an existing FOR balance from pre-2023? -- FOR release rules

If the urencriterium status is unknown, STOP. Many deductions depend on it.

### Refusal catalogue

**R-NL-ZZP-1 -- BV structure.** Trigger: client operates through a BV (besloten vennootschap). Message: "This skill covers eenmanszaak and partnership participants only. BV corporate tax and salary/dividend structuring is outside scope. Please escalate to a qualified belastingadviseur."

**R-NL-ZZP-2 -- International structure.** Trigger: client has cross-border business income or a permanent establishment in another country. Message: "International tax structures require treaty analysis. This skill covers domestic Dutch ZZP deductions only. Please escalate."

**R-NL-ZZP-3 -- Fiscal unity or complex partnership allocations.** Trigger: client is part of a fiscal unity or asks about complex partnership profit allocation. Message: "Fiscal unity and complex partnership allocations are outside this skill's scope. Please escalate to a qualified belastingadviseur."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to ZZP deductions. Match by case-insensitive substring.

### 3.1 Belastingdienst payments (tax authority)

| Pattern | Treatment | Notes |
|---|---|---|
| BELASTINGDIENST | TAX PAYMENT / REFUND | Income tax, VAT, or other -- verify assessment type |
| TOESLAGEN | SUBSIDY RECEIPT | Zorgtoeslag, huurtoeslag, etc. -- not a deduction item |
| IB AANSLAG, INKOMSTENBELASTING | INCOME TAX PAYMENT | Final assessment payment -- includes effect of ZZP deductions |
| VOORLOPIGE AANSLAG, VOORL. AANSLAG | PROVISIONAL ASSESSMENT | Advance income tax payment based on estimated profit |

### 3.2 Business investments (KIA-eligible)

| Pattern | Treatment | Notes |
|---|---|---|
| MEDIAMARKT, COOLBLUE, BOL.COM | POTENTIAL KIA ASSET | Verify: asset >= EUR 450, used in business, not excluded category |
| APPLE, DELL, LENOVO, HP | POTENTIAL KIA ASSET (COMPUTER) | Computers qualify if >= EUR 450; check business use % |
| IKEA, OFFICE DEPOT, STAPLES | POTENTIAL KIA ASSET (FURNITURE) | Office furniture qualifies if >= EUR 450 each |

### 3.3 Vehicle purchases (KIA exclusion check)

| Pattern | Treatment | Notes |
|---|---|---|
| AUTOTRADER, AUTOMOBILE, CAR DEALER | KIA EXCLUDED if catalogue value > EUR 12,000 | Cars above EUR 12,000 catalogue value excluded from KIA; normal depreciation applies |
| BOVAG, RDW | VEHICLE-RELATED | Registration/inspection -- not a KIA asset |

### 3.4 Pension/retirement (FOR-related)

| Pattern | Treatment | Notes |
|---|---|---|
| LIJFRENTE, ANNUITY, BRAND NEW DAY | LIJFRENTE PREMIUM | Deductible within jaarruimte; may relate to FOR conversion |
| PENSIOENFONDS, ABP | PENSION CONTRIBUTION | Not relevant for ZZP deductions (employee pension) |

### 3.5 Partner payments (meewerkaftrek check)

| Pattern | Treatment | Notes |
|---|---|---|
| Partner name appearing as salary/payment < EUR 5,000/year | MEEWERKAFTREK POSSIBLE | If partner works 525+ hours unpaid or < EUR 5,000, meewerkaftrek applies |
| Partner name appearing as salary/payment >= EUR 5,000/year | MEEWERKAFTREK EXCLUDED | Payment >= EUR 5,000 disqualifies meewerkaftrek; amount is deductible expense |

---

## Section 4 -- Deduction computation rules

### 4.1 Zelfstandigenaftrek (Tier 1)

Legislation: Wet IB 2001 Article 3.76

2025 amount: EUR 2,470 (standard); EUR 1,235 if AOW age reached at start of year.

Requirements: must qualify as ondernemer; must meet urencriterium (1,225 hours). The zelfstandigenaftrek cannot exceed profit before ondernemersaftrek, UNLESS the startersaftrek also applies (then no profit limitation).

### 4.2 Urencriterium (Tier 1 / Tier 2)

Legislation: Wet IB 2001 Article 3.6

Threshold: at least 1,225 hours per calendar year on enterprise activities. Counts: direct client work, administration, sales, professional development, purchasing, business meetings, strategic planning. Does NOT count: travel time, commuting, personal development unrelated to business, sick leave, vacation.

NOT pro-rated for part-year. Full 1,225 hours must be met even if business started mid-year. Flag for reviewer if hours are between 1,200 and 1,300 (borderline).

### 4.3 Startersaftrek (Tier 1)

Legislation: Wet IB 2001 Article 3.76 lid 3

2025 amount: EUR 2,123 on top of zelfstandigenaftrek. Requirements: qualifies for zelfstandigenaftrek; applied zelfstandigenaftrek in at most 2 of the preceding 5 years. Available in first 3 years of a 5-year window.

Special rule: when startersaftrek applies, the combined deduction (zelfstandigenaftrek + startersaftrek) is NOT limited to profit. Can create negative income from enterprise that offsets other Box 1 income.

### 4.4 MKB-winstvrijstelling (Tier 1)

Legislation: Wet IB 2001 Article 3.79a

2025 rate: 12.7% of qualifying profit. Calculated on profit AFTER ondernemersaftrek. Urencriterium is NOT required. All ondernemers qualify.

If qualifying profit is negative (loss), the MKB-winstvrijstelling reduces the loss by 12.7% (works against the taxpayer in loss years).

### 4.5 FOR -- abolished (Tier 1)

The Fiscale Oudedagsreserve has been abolished as of 1 January 2023. No new additions permitted. Existing balances from pre-2023 remain on the balance sheet. Can be converted to lijfrente at any time. Released at business cessation (stakingsaftrek max EUR 3,630 in 2025 may apply). NEVER compute a new FOR addition for 2023 or later.

### 4.6 KIA (Tier 1)

Legislation: Wet IB 2001 Article 3.41

Each individual asset must cost at least EUR 450. Total qualifying investment must be at least EUR 2,901. Urencriterium NOT required. Excluded: land, residential buildings, cars > EUR 12,000, assets for lease, animals, goodwill, assets from connected persons.

Disinvestment addition: if KIA-claimed asset sold within 5 years, proportional addition to profit applies.

### 4.7 Willekeurige afschrijving voor starters (Tier 1)

Legislation: Wet IB 2001 Article 3.34

Qualifying starters may depreciate business assets at any pace (up to 100% in year 1). Requires startersaftrek eligibility. Asset must cost >= EUR 450. Residual value floor still applies. For buildings, limited to WOZ value.

### 4.8 Meewerkaftrek (Tier 2)

Legislation: Wet IB 2001 Article 3.78

| Hours worked by partner per year | Deduction (% of profit) |
|---|---|
| 525 -- 874 | 1.25% |
| 875 -- 1,224 | 2.00% |
| 1,225 -- 1,749 | 3.00% |
| 1,750+ | 4.00% |

Partner must work unpaid or receive < EUR 5,000. Urencriterium for entrepreneur NOT required. Flag for reviewer -- partner hours must be documented. Being phased out from 2027.

---

## Section 5 -- Computation order

Legislation: Wet IB 2001 Article 3.2 et seq.

```
1. Winst uit onderneming (profit from enterprise)
     = Revenue - Costs - Depreciation - KIA
2. Minus: Ondernemersaftrek
     = Zelfstandigenaftrek + Startersaftrek + Meewerkaftrek + Stakingsaftrek
3. = Profit after ondernemersaftrek
4. Minus: MKB-winstvrijstelling (12.7% of line 3)
5. = Taxable profit from enterprise
6. Add: Other Box 1 income (employment, pension, periodic payments)
7. Minus: Personal deductions (hypotheekrenteaftrek, lijfrente, etc.)
8. = Belastbaar inkomen Box 1
9. Apply progressive Box 1 rates
```

Key interaction: zelfstandigenaftrek and startersaftrek reduce profit BEFORE MKB-winstvrijstelling, creating a multiplied effect. EUR 2,470 zelfstandigenaftrek reduces taxable income by EUR 2,470 + (12.7% x EUR 2,470) = EUR 2,784. KIA reduces profit at step 1, also included in MKB-winstvrijstelling base. The arbeidskorting (tax credit) is applied after computing gross tax.

---

## Section 6 -- FOR balance management and stakingsaftrek

### 6.1 Existing FOR balances (Tier 1)

| Situation | Treatment |
|---|---|
| FOR balance on 31 Dec 2022 | Remains on balance sheet; not immediately taxed |
| Conversion to lijfrente | Premium deductible within jaarruimte/reserveringsruimte limits |
| Release without lijfrente | Added to Box 1 taxable income at progressive rates |
| Business cessation | FOR must be released; stakingsaftrek (max EUR 3,630 in 2025) may apply if converted within 6 months |

### 6.2 What replaced FOR

Entrepreneurs use jaarruimte to make actual lijfrente contributions. Jaarruimte is based on profit and pension accrual.

---

## Section 7 -- Edge case registry

### EC1 -- Hours just below 1,225 (Tier 2)
Situation: Client claims 1,210 hours, wants to include 20 hours of travel time.
Resolution: Travel time does NOT count. Client does not qualify for zelfstandigenaftrek or startersaftrek. Still qualifies for MKB-winstvrijstelling and KIA (no hours requirement). Flag for reviewer.

### EC2 -- Loss year with startersaftrek (Tier 1)
Situation: Starter has profit of EUR 1,000 but qualifies for EUR 4,593 total deduction.
Resolution: Full EUR 4,593 deducted (no profit limitation for starters). Loss of EUR 3,593 offsets other Box 1 income. MKB-winstvrijstelling reduces loss by 12.7% (loss becomes EUR 3,137).

### EC3 -- Loss year without startersaftrek (Tier 1)
Situation: Non-starter has profit of EUR 1,500, zelfstandigenaftrek EUR 2,470.
Resolution: Zelfstandigenaftrek limited to EUR 1,500. Remaining EUR 970 is lost. MKB-winstvrijstelling on zero = zero.

### EC4 -- FOR balance from pre-2023, business continues (Tier 1)
Situation: Client has FOR balance of EUR 15,000 from 2022. Business still active.
Resolution: Balance remains. No new additions. No forced release while business continues. May convert to lijfrente voluntarily.

### EC5 -- KIA on personal car above EUR 12,000 (Tier 1)
Situation: Client purchases car with catalogue value EUR 25,000, 70% business use.
Resolution: Excluded from KIA regardless of business use. Normal depreciation (based on business %) does apply.

### EC6 -- Disinvestment addition triggered (Tier 1)
Situation: Machine purchased for EUR 5,000 in 2023, KIA EUR 1,400 (28%). Sold in 2025 for EUR 3,000.
Resolution: Disinvestment addition: EUR 3,000 x 28% = EUR 840 added to 2025 profit.

### EC7 -- Partner paid EUR 6,000 (Tier 1)
Situation: Fiscal partner works 900 hours, receives EUR 6,000.
Resolution: Meewerkaftrek requires < EUR 5,000 payment. EUR 6,000 exceeds threshold. No meewerkaftrek. The EUR 6,000 is deductible business expense; taxable for partner.

### EC8 -- Mid-year starter, urencriterium not met (Tier 1)
Situation: Business starts 1 September, client works 800 hours by 31 December.
Resolution: 1,225 hours NOT pro-rated. No zelfstandigenaftrek or startersaftrek in 2025. MKB-winstvrijstelling and KIA still available. Year 1 of startersaftrek is not used up.

---

## Section 8 -- Reviewer escalation protocol

When a Tier 2 situation is identified:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified belastingadviseur must confirm before filing.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified belastingadviseur. Document gap.
```

---

## Section 9 -- Test suite

### Test 1 -- Standard zzp'er, meets urencriterium, not a starter
Input: Eenmanszaak, winst EUR 50,000, meets 1,225 hours, not a starter, investments EUR 2,000, no partner.
Expected output: Zelfstandigenaftrek = EUR 2,470. No startersaftrek. No meewerkaftrek. KIA = EUR 0 (below EUR 2,901). MKB-winstvrijstelling = (EUR 50,000 - EUR 2,470) x 12.7% = EUR 6,036. Taxable profit = EUR 41,494.

### Test 2 -- Starter with low profit
Input: Eenmanszaak, first year, winst EUR 2,000, meets 1,225 hours, investments EUR 4,000.
Expected output: Zelfstandigenaftrek EUR 2,470 + startersaftrek EUR 2,123 = EUR 4,593. KIA = EUR 1,120. Profit after KIA = EUR 880. After ondernemersaftrek = -EUR 3,713. MKB-winstvrijstelling reduces loss by 12.7%. Taxable result = -EUR 3,241.

### Test 3 -- Does not meet urencriterium
Input: Eenmanszaak, winst EUR 30,000, 900 hours, investments EUR 8,000.
Expected output: No zelfstandigenaftrek. KIA = EUR 2,240. Profit after KIA = EUR 27,760. MKB-winstvrijstelling = EUR 3,526. Taxable profit = EUR 24,234.

### Test 4 -- Large investment, KIA fixed amount
Input: Total investments EUR 90,000.
Expected output: KIA = EUR 19,769 (fixed amount in EUR 70,603-130,744 bracket).

### Test 5 -- Very large investment, KIA phase-out
Input: Total investments EUR 200,000.
Expected output: KIA = EUR 19,769 - (7.56% x EUR 69,256) = EUR 14,533.

### Test 6 -- FOR balance, ongoing business
Input: FOR balance EUR 20,000 from 2022. Business active in 2025.
Expected output: No new addition. Balance stays. May convert to lijfrente voluntarily.

### Test 7 -- Meewerkaftrek
Input: Winst EUR 60,000, fiscal partner works 1,300 hours unpaid.
Expected output: Meewerkaftrek = 3% x EUR 60,000 = EUR 1,800. Total ondernemersaftrek = EUR 4,270. MKB-winstvrijstelling = EUR 7,078. Taxable profit = EUR 48,652.

### Test 8 -- AOW-age entrepreneur
Input: AOW age reached 1 Jan 2025. Winst EUR 25,000. Meets urencriterium.
Expected output: Zelfstandigenaftrek = EUR 1,235. MKB-winstvrijstelling = EUR 3,018. Taxable profit = EUR 20,747.

---

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER apply the zelfstandigenaftrek without confirming the urencriterium is met -- 1,225 hours is a hard threshold
- NEVER pro-rate the urencriterium for part-year businesses -- the full 1,225 hours must be met
- NEVER include travel time in the urencriterium count -- it is explicitly excluded
- NEVER compute a new FOR addition for 2023 or later -- the FOR has been abolished
- NEVER apply the startersaftrek beyond the first 3 qualifying years in a 5-year window
- NEVER forget that MKB-winstvrijstelling is calculated AFTER the ondernemersaftrek -- the order matters
- NEVER apply the profit limitation to the zelfstandigenaftrek when the startersaftrek also applies
- NEVER claim KIA on cars with catalogue value above EUR 12,000
- NEVER claim KIA on individual assets costing less than EUR 450
- NEVER ignore the disinvestment addition when a KIA-claimed asset is sold within 5 years
- NEVER present computed deductions as definitive -- always direct client to their belastingadviseur

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a belastingadviseur, registeraccountant, or equivalent licensed practitioner in the Netherlands) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
