---
name: us-sole-prop-bookkeeping
description: Tier 2 content skill for classifying business transactions into US federal Schedule C (Form 1040) line items for sole proprietors and single-member LLCs disregarded for federal tax. Covers tax year 2025 under OBBBA (P.L. 119-21) with post-OBBBA depreciation rules, permanent QBI framework, and new tip/overtime/auto loan interest deductions. Handles Schedule C Parts I-V, the §162 ordinary and necessary standard, §263 capitalization, §280A home office, §280F vehicle and listed property, §274 substantiation and meals, §168(k) bonus depreciation cutoff at January 19 2025, §179 expensing, §471(c) small business inventory exception, §183 hobby loss, and §6001 / §274(d) recordkeeping. Defers Schedule C net profit, Schedule SE, QBI, retirement contributions, and quarterly estimated tax to companion content skills. MUST be loaded alongside us-tax-workflow-base v0.1 or later. Federal only. No state tax.
version: 2.0
---

# US Sole Prop Bookkeeping Skill v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `us-tax-workflow-base` Section 1 — follow that runbook with this skill providing the federal Schedule C content.**

| Field | Value |
|---|---|
| Country | United States of America |
| Tax form | Schedule C (Form 1040), Profit or Loss From Business |
| Taxpayer type | Sole proprietor or single-member LLC disregarded for federal tax |
| Tax year | 2025 (returns due April 15, 2026 or October 15, 2026 with extension) |
| Key legislation | Internal Revenue Code; One Big Beautiful Bill Act (OBBBA, P.L. 119-21, July 4, 2025); TCJA 2017 provisions still in force |
| Currency | USD only |
| Companion skill (Tier 1, workflow) | **us-tax-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants |
| Currency date | April 2026 |

**Schedule C line structure (Part II — Expenses):**

| Line | Content |
|---|---|
| 1 | Gross receipts or sales |
| 2 | Returns and allowances |
| 4 | Cost of goods sold (from Part III line 42) |
| 6 | Other income |
| 8 | Advertising |
| 9 | Car and truck expenses |
| 10 | Commissions and fees |
| 11 | Contract labor |
| 12 | Depletion |
| 13 | Depreciation and §179 expense (Form 4562) |
| 14 | Employee benefit programs |
| 15 | Insurance (other than health) |
| 16a | Interest — mortgage |
| 16b | Interest — other |
| 17 | Legal and professional services |
| 18 | Office expense |
| 19 | Pension and profit-sharing plans (employees only) |
| 20a | Rent or lease — vehicles, machinery, equipment |
| 20b | Rent or lease — other business property |
| 21 | Repairs and maintenance |
| 22 | Supplies |
| 23 | Taxes and licenses |
| 24a | Travel |
| 24b | Meals (subject to 50% limit) |
| 25 | Utilities |
| 26 | Wages (employees, not owner) |
| 27a | Other expenses (from Part V line 48) |
| 27b | Reserved |

**Year-specific figures for tax year 2025:**

| Figure | Value | Primary source |
|---|---|---|
| §179 expensing limit | $2,500,000 | OBBBA P.L. 119-21 §70306; IRC §179(b)(1) as amended |
| §179 phase-out threshold | $4,000,000 | OBBBA P.L. 119-21 §70306; IRC §179(b)(2) as amended |
| §179 heavy SUV cap | $31,300 | IRC §179(b)(5); inflation-adjusted |
| §168(k) bonus depreciation, acquired on or before Jan 19, 2025 | 40% | IRC §168(k) pre-OBBBA phase-down |
| §168(k) bonus depreciation, acquired after Jan 19, 2025 | 100% | OBBBA P.L. 119-21; IRC §168(k) as amended |
| De minimis safe harbor (no AFS) | $2,500 per item | Treas. Reg. §1.263(a)-1(f)(1)(ii)(D) |
| De minimis safe harbor (with AFS) | $5,000 per item | Treas. Reg. §1.263(a)-1(f)(1)(i)(D) |
| Standard mileage rate (business) | 70 cents/mile | Notice 2025-5 |
| §280F first-year auto cap (with bonus) | $20,200 | Rev. Proc. 2025-16 Table 1 |
| §280F first-year auto cap (without bonus) | $12,200 | Rev. Proc. 2025-16 Table 2 |
| §280F year-2 cap | $19,600 | Rev. Proc. 2025-16 |
| §280F year-3 cap | $11,800 | Rev. Proc. 2025-16 |
| §280F succeeding years cap | $7,060 | Rev. Proc. 2025-16 |
| Heavy vehicle GVW threshold | >6,000 lbs | IRC §280F(d)(5)(A) |
| Simplified home office rate | $5.00/sq ft | Rev. Proc. 2013-13; Pub 587 (2025) |
| Simplified home office sq ft cap | 300 sq ft | Rev. Proc. 2013-13 |
| Simplified home office max deduction | $1,500 | Derived ($5 x 300) |
| Business meals deductibility | 50% | IRC §274(n)(1) |
| Entertainment deductibility | 0% | IRC §274(a)(1) post-TCJA |
| 1099-NEC filing threshold | $600 | IRC §6041A(a) |
| Social Security wage base | $176,100 | SSA; IRC §1402(b) |
| QBI deduction rate (2025) | 20% | IRC §199A(a); OBBBA made permanent |
| QBI deduction rate (2026 onward) | 23% | OBBBA; IRC §199A as amended |
| §471(c) small business gross receipts threshold | $31,000,000 | IRC §471(c); IRC §448(c)(1) |

**OBBBA depreciation note:** The 100% restaurant meal deduction is NOT available in 2025. The temporary 100% deduction under CAA 2021 §210 expired December 31, 2022. OBBBA did NOT reinstate it. The simplified home office rate remains $5/sq ft, NOT $6/sq ft.

**Conservative defaults — US-specific values:**

| Ambiguity | Default |
|---|---|
| Unknown business-use % for vehicle | 0% (no deduction) |
| Unknown business-use % for home office | 0% (no deduction) |
| Unknown business-use % for phone/internet | 0% (no deduction) |
| Unknown whether expense is business or personal | Personal (exclude) |
| Unknown whether meal has business purpose | Personal (exclude) |
| Unknown whether travel day is business or personal | Personal (exclude) |
| Unknown acquisition date near OBBBA cutoff (Jan 19, 2025) | Pre-cutoff (40% bonus, more conservative) |
| Unknown cost basis of depreciable asset | $0 (no deduction) |
| Unknown recovery period of asset | Longest plausible period |
| Unknown whether worker is employee or contractor | Contractor (Line 11) with classification risk flag |
| Unknown entity type of payee (LLC vs corp) | Assume 1099-NEC required |
| Amazon purchase without description | Personal (exclude) |
| Cash withdrawal | Owner draw (exclude) |
| Unknown whether payment processor fee is transaction vs subscription | Transaction fee (Line 27a bank charges) |

**Red flag thresholds — values for the reviewer brief:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | $5,000 |
| HIGH vehicle business-use claim without mileage log | Any amount |
| HIGH meals exceeding 20% of gross receipts | Any percentage above 20% |
| MEDIUM contractor payment without W-9/1099 status | $600+ cumulative |
| MEDIUM home office deduction without measurements | Any amount |
| MEDIUM conservative-default count | >5 across the return |
| LOW Schedule C net loss (hobby loss risk under §183) | Any net loss |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — full-year bank statement for the business checking account in CSV, PDF, or pasted text. Must cover January 1 through December 31 of the tax year. Acceptable from any US business bank: Chase Business, Wells Fargo Business, Bank of America Business, Capital One Spark, Mercury, Relay, Novo, Bluevine, or any other.

**Recommended** — all 1099-NECs received, prior year Schedule C (to carry forward depreciation, vehicle method elections, and home office elections), receipts for any individual expense exceeding $75, credit card statements if business expenses run through a personal or separate business card.

**Ideal** — contemporaneous mileage log meeting §274(d) requirements, home office measurements (square footage of office and total home), complete invoice register, W-9s collected from all contractors paid $600+, prior Form 4562 for depreciation schedules, health insurance premium statements (Form 1095-A/B/C).

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement at all, hard stop. If bank statement only without 1099-NECs or prior return, proceed but record in the reviewer brief: "This Schedule C working paper was produced from bank statements alone. The reviewer must verify: (a) all 1099-NEC income is captured, (b) depreciation elections from prior years are correctly carried forward, (c) vehicle method elections from the first year of use are honored, and (d) §274(d) substantiation exists for travel, meals, and listed property."

### Refusal catalogue

These refusals are safety mechanisms. If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-US-PARTNERSHIP — Partnership or multi-member LLC.** *Trigger:* user mentions partners, partnership agreement, Form 1065, Schedule K-1, or more than one member of the LLC. *Message:* "This skill covers sole proprietors and single-member LLCs only. Partnerships and multi-member LLCs file Form 1065 and issue Schedule K-1s to partners. Please use a CPA or EA experienced in partnership taxation."

**R-US-RENTAL — Rental property income.** *Trigger:* user mentions rental income, landlord activities, Schedule E, Form 8825, rental properties. *Message:* "Rental real estate income is reported on Schedule E, not Schedule C (unless the taxpayer qualifies as a real estate professional providing substantial services). This skill does not cover Schedule E. Please use a CPA or EA experienced in rental property taxation."

**R-US-CRYPTO — Cryptocurrency transactions.** *Trigger:* user mentions crypto trading, DeFi, NFT sales, mining income, staking rewards, token swaps. *Message:* "Cryptocurrency transactions involve complex basis tracking, wash sale considerations (post-2025), and Form 8949 reporting. This skill does not cover crypto. Please use a CPA or EA experienced in digital asset taxation."

**R-US-EMPLOYEES — Employer with W-2 employees (payroll).** *Trigger:* user has W-2 employees (not contractors), mentions payroll, Form 941, Form 940, state unemployment. *Message:* "This skill covers the Schedule C expense classification side. The payroll compliance obligations (Form 941, 940, W-2 issuance, state withholding) are out of scope. The contractor payments on Line 11 and employee wages on Line 26 are classified by this skill, but payroll tax compliance requires a payroll service or specialist."

**R-US-SCORP — S-corporation elected.** *Trigger:* user mentions S-corp election, Form 2553, Form 1120-S, reasonable compensation, officer salary. *Message:* "S-corporations file Form 1120-S, not Schedule C. This skill covers sole proprietors and single-member LLCs that have NOT elected S-corp status. Please use the us-s-corp-election-decision skill for evaluation or a CPA for S-corp return preparation."

**R-US-CCORP — C-corporation.** *Trigger:* user mentions C-corp, Form 1120, corporate tax return, dividends from own corporation. *Message:* "C-corporations file Form 1120. This skill covers sole proprietors only. Please use a CPA experienced in corporate taxation."

**R-US-FARMING — Farm income.** *Trigger:* user mentions farming, Schedule F, crop income, livestock. *Message:* "Farm income is reported on Schedule F, not Schedule C. Different rules apply. Please use a CPA or EA experienced in agricultural taxation."

**R-US-DEPLETION — Natural resources.** *Trigger:* user mentions oil/gas royalties, mineral rights, timber, depletion deductions. *Message:* "Depletion deductions under IRC §611-§613 require specialist knowledge. Out of scope for this skill."

**R-US-FOREIGN-INCOME — Foreign earned income or FBAR.** *Trigger:* user mentions foreign bank accounts, FBAR, Form 8938, foreign earned income exclusion, Form 2555. *Message:* "Foreign income reporting and FBAR/FATCA compliance are out of scope. Please use a CPA or EA experienced in international tax."

**R-US-ESTATE-TRUST — Estate or trust income.** *Trigger:* user mentions estate, trust, Form 1041, fiduciary return. *Message:* "Estate and trust taxation is out of scope. Please use a CPA or attorney experienced in fiduciary taxation."

---

## Section 3 — Supplier pattern library (US vendors)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 US banks (fees = bank charges Line 27a)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| CHASE, JPMORGAN CHASE | Bank fees/charges → Line 27a "Bank charges" | 27a | Monthly service charges, wire fees, overdraft fees |
| WELLS FARGO, WFBNA | Bank fees/charges → Line 27a "Bank charges" | 27a | Same |
| BANK OF AMERICA, BOA, BOFA | Bank fees/charges → Line 27a "Bank charges" | 27a | Same |
| CAPITAL ONE | Bank fees/charges → Line 27a "Bank charges" | 27a | Distinguish from Capital One credit card purchases |
| MERCURY, RELAY, NOVO, BLUEVINE | Bank fees/charges → Line 27a "Bank charges" | 27a | Fintech business banking fees |
| INTEREST INCOME, INT EARNED | Line 6 Other income OR EXCLUDE | 6 | Bank interest is taxable but often reported on Schedule B, not Schedule C. Flag for reviewer. |
| LOAN, BUSINESS LOAN, LINE OF CREDIT | EXCLUDE | — | Loan proceeds are not income; principal repayments are not deductible. Interest portion → Line 16b. |

### 3.2 Payment processors (payout is NOT revenue recognition)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| STRIPE TRANSFER, STRIPE PAYOUT | EXCLUDE as internal transfer | — | Stripe payout to bank is NOT revenue. Revenue is the gross on the Stripe dashboard. Reconcile gross sales to Line 1, fees to Line 27a "Merchant processing fees". |
| PAYPAL TRANSFER, PAYPAL INST XFER | EXCLUDE as internal transfer | — | Same as Stripe. PayPal settlement is not revenue. |
| SQUARE, SQ *, SQUAREUP | EXCLUDE as internal transfer | — | Same. Square deposit is net of fees. |
| VENMO BUSINESS, VENMO CASHOUT | EXCLUDE as internal transfer | — | Business Venmo payouts. Gross is revenue. |
| STRIPE FEE, PAYPAL FEE, SQ FEE | Line 27a "Merchant processing fees" | 27a | If fees appear as separate line items on statement |

**Critical rule:** Payment processor payouts appear on the bank statement as deposits, but they are NOT the gross revenue figure. The gross revenue (before processor fees) is the correct Line 1 amount. Processor fees are deductible on Line 27a. If the user provides only bank statements, the deposits from Stripe/PayPal/Square represent NET revenue. The working paper must note: "Revenue from [processor] is reported net of fees. Reviewer should verify gross revenue from [processor] dashboard and add back fees to both Line 1 (gross) and Line 27a (fees)."

### 3.3 SaaS/cloud (business expenses)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| AWS, AMAZON WEB SERVICES | Line 27a "Cloud hosting" | 27a | Hosting and infrastructure |
| GOOGLE WORKSPACE, GOOGLE CLOUD, GOOGLE *GSUITE | Line 27a "Software subscriptions" | 27a | Business productivity suite |
| MICROSOFT 365, MSFT *OFFICE, AZURE | Line 27a "Software subscriptions" | 27a | Office suite or cloud hosting |
| ADOBE, ADOBE *CREATIVE | Line 27a "Software subscriptions" | 27a | Creative Cloud, Acrobat |
| SLACK, SLACK TECHNOLOGIES | Line 27a "Software subscriptions" | 27a | Team communication |
| NOTION, NOTION LABS | Line 27a "Software subscriptions" | 27a | Workspace tool |
| GITHUB, GITHUB INC | Line 27a "Software subscriptions" | 27a | Developer tools |
| JETBRAINS | Line 27a "Software subscriptions" | 27a | IDE software |
| FIGMA | Line 27a "Software subscriptions" | 27a | Design tool |
| CANVA | Line 27a "Software subscriptions" | 27a | Design tool |
| ZOOM, ZOOM.US | Line 25 Utilities OR Line 27a | 25 or 27a | Communication platform; Line 25 if treating as telecom, Line 27a if treating as software. Skill defaults to Line 27a "Software subscriptions". |
| DROPBOX | Line 27a "Software subscriptions" | 27a | Cloud storage |
| MAILCHIMP, CONVERTKIT, CONSTANT CONTACT | Line 8 Advertising | 8 | Email marketing is advertising |
| HUBSPOT | Line 8 Advertising OR Line 27a | 8 or 27a | CRM/marketing = Line 8; general SaaS = Line 27a. Default Line 27a. |
| QUICKBOOKS, INTUIT *QB, XERO, FRESHBOOKS, WAVE | Line 27a "Accounting software" | 27a | Bookkeeping/accounting software |

### 3.4 Office/coworking (rent Line 20b)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| WEWORK | Line 20b Rent — other business property | 20b | Coworking space rent |
| REGUS, IWG, SPACES | Line 20b Rent — other business property | 20b | Coworking/serviced office |
| INDUSTRIOUS | Line 20b Rent — other business property | 20b | Coworking |
| OFFICE RENT, COMMERCIAL LEASE | Line 20b Rent — other business property | 20b | Traditional office lease |

### 3.5 Communication (utilities Line 25)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| VERIZON, VZ WIRELESS | Line 25 Utilities (business %) | 25 | Phone/internet — business portion only. If personal phone with some business use, Tier 2 (Section 6.4). |
| AT&T, ATT | Line 25 Utilities (business %) | 25 | Same |
| T-MOBILE, TMOBILE | Line 25 Utilities (business %) | 25 | Same |
| COMCAST, XFINITY | Line 25 Utilities (business %) | 25 | Internet service |
| SPECTRUM, CHARTER | Line 25 Utilities (business %) | 25 | Internet service |
| GOOGLE FI | Line 25 Utilities (business %) | 25 | Phone service |

### 3.6 Insurance

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| STATE FARM, GEICO, PROGRESSIVE, ALLSTATE, USAA (auto) | NOT deductible unless business vehicle | — | Personal auto insurance is not a business expense. If business vehicle with actual expense method, business % goes to Line 9. |
| HARTFORD, HISCOX, NEXT INSURANCE, THIMBLE | Line 15 Insurance | 15 | Business liability, E&O, professional indemnity insurance |
| GENERAL LIABILITY, E&O INSURANCE, PROFESSIONAL LIABILITY | Line 15 Insurance | 15 | Business insurance premiums |
| HEALTH INSURANCE, BLUE CROSS, AETNA, UNITED HEALTH, CIGNA, KAISER | EXCLUDE from Schedule C | — | Self-employed health insurance deduction goes on Schedule 1 line 17, NOT Schedule C. Handled by companion skill. |
| WORKERS COMP | Line 15 Insurance | 15 | Workers compensation insurance for employees |

### 3.7 Meals (Line 24b at 50%)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| Restaurant charges (any named restaurant) | Line 24b at 50% IF business purpose documented | 24b | Must have: (a) business purpose, (b) who was present, (c) business discussion. §274(d) substantiation required. |
| UBER EATS, DOORDASH, GRUBHUB, POSTMATES | Line 24b at 50% IF business purpose | 24b | Same substantiation requirements as restaurant meals. |
| STARBUCKS, DUNKIN, coffee shops | Line 24b at 50% IF business meeting | 24b | Solo coffee while working is generally NOT deductible. Must involve a client/prospect/business contact. |
| ENTERTAINMENT, CONCERTS, SPORTS TICKETS | NOT deductible (0%) | — | Entertainment is 0% deductible post-TCJA under IRC §274(a)(1). Not even 50%. |

**Critical rule:** There is NO 100% restaurant meal deduction in 2025. The temporary 100% deduction (CAA 2021 §210) expired December 31, 2022. Business meals are 50% deductible under §274(n)(1). Entertainment is 0% deductible under §274(a)(1). The only 100% meal deductions are de minimis fringes (office snacks/coffee under §132(e)) and meals provided for employer convenience under §119.

### 3.8 Travel (Line 24a)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| UNITED AIRLINES, DELTA, AMERICAN AIRLINES, SOUTHWEST, JETBLUE, ALASKA AIR, FRONTIER, SPIRIT | Line 24a Travel | 24a | Airfare for business travel. Must be primarily business purpose. Personal extension days → allocate and exclude personal portion. |
| MARRIOTT, HILTON, HYATT, IHG, BEST WESTERN, HOLIDAY INN | Line 24a Travel | 24a | Business lodging. Same allocation rule for mixed trips. |
| AIRBNB (lodging for business travel) | Line 24a Travel | 24a | Business travel accommodation. Distinguish from Airbnb hosting income (R-US-RENTAL). |
| HERTZ, ENTERPRISE, NATIONAL, AVIS, BUDGET | Line 24a Travel | 24a | Rental car for business travel |
| UBER, LYFT (out-of-town) | Line 24a Travel | 24a | Ground transportation during business travel. Local Uber/Lyft may be Line 9 or commuting (non-deductible). |
| AMTRAK | Line 24a Travel | 24a | Train fare for business travel |

### 3.9 Vehicle (car/truck expenses Line 9)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| SHELL, CHEVRON, BP, EXXON, MOBIL, SUNOCO, MARATHON, SPEEDWAY, WAWA (fuel) | Line 9 Car/truck (business % only) | 9 | Only if actual expense method AND business-use % is documented. If standard mileage method, fuel is already included in the 70 cents/mile rate. |
| JIFFY LUBE, VALVOLINE, MIDAS, PEP BOYS, AUTOZONE, O'REILLY | Line 9 Car/truck (business % only) | 9 | Vehicle maintenance/parts — same rules as fuel |
| CARWASH | Line 9 Car/truck (business % only) | 9 | Same |
| PARKING, PARKWHIZ, SPOTHERO | Line 9 Car/truck (separate from mileage) | 9 | Parking fees for business are deductible even with standard mileage method. Commute parking is NOT deductible. |
| TOLL, EZPASS, SUNPASS, IPASS | Line 9 Car/truck (separate from mileage) | 9 | Business tolls deductible even with standard mileage. Commute tolls NOT deductible. |

### 3.10 Professional services (Line 17)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| CPA, ACCOUNTING, TAX PREPARATION, ENROLLED AGENT | Line 17 Legal and professional | 17 | Tax prep fees for business return. Personal return prep is NOT deductible post-TCJA. If combined, allocate. |
| ATTORNEY, LAW OFFICE, LEGAL SERVICES, ESQ | Line 17 Legal and professional | 17 | Business legal matters only. Personal legal is not deductible. |
| BOOKKEEPER, BOOKKEEPING SERVICE | Line 17 Legal and professional | 17 | Business bookkeeping |
| CONSULTANT, CONSULTING | Line 17 Legal and professional OR Line 11 | 17 or 11 | Advisory = Line 17. Operational services = Line 11. Default Line 17. |
| LEGALZOOM, INCFILE, NORTHWEST REGISTERED AGENT | Line 17 Legal and professional | 17 | Business formation and registered agent services |

### 3.11 Contractors (Line 11, 1099-NEC threshold)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| FIVERR, UPWORK, TOPTAL | Line 11 Contract labor | 11 | Platform contractor payments. 1099-NEC obligation depends on payment method — if paid via platform (credit card), platform issues 1099-K. If paid off-platform via Zelle/ACH, taxpayer must issue 1099-NEC at $600. |
| Contractor names (individuals paid for services) | Line 11 Contract labor | 11 | Flag for 1099-NEC if $600+ cumulative for the year. Verify payment method (see Section 5 for Zelle/ACH rules). |

**1099-NEC payment method trap:** Zelle is NOT a TPSO under §6050W. Zelle payments DO require the payor to issue 1099-NEC at $600. Same for Venmo personal, ACH, wire, check, and cash. Only credit cards, PayPal Business, Stripe, Square, Venmo Business, and Cash App Business are TPSOs that handle the 1099-K reporting.

### 3.12 Government (tax payments — exclude from Schedule C)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| IRS, UNITED STATES TREASURY, EFTPS, US TREASURY | EXCLUDE | — | Federal tax payments (income tax, SE tax, estimated tax) are NOT deductible on Schedule C. They are personal tax obligations. |
| FTB, FRANCHISE TAX BOARD (CA) | EXCLUDE | — | State income tax payments — personal, not Schedule C. May be deductible on Schedule A (SALT, subject to $10K cap). |
| EDD, EMPLOYMENT DEVELOPMENT (CA) | EXCLUDE from Schedule C OR Line 23 | — or 23 | State unemployment tax (employer portion) → Line 23. Personal income tax withholding → EXCLUDE. |
| STATE TAX PAYMENT, STATE ESTIMATED TAX | EXCLUDE | — | Personal state income tax, not Schedule C |
| BUSINESS LICENSE, CITY LICENSE, COUNTY LICENSE | Line 23 Taxes and licenses | 23 | Business license fees and permits |
| SECRETARY OF STATE, SOS FILING | Line 23 Taxes and licenses | 23 | LLC annual filing fee, business registration |
| SALES TAX REMITTANCE | EXCLUDE from expenses | — | Sales tax collected and remitted is pass-through, not income or expense. If the taxpayer includes sales tax in gross receipts (Line 1), the remittance goes to Line 23. |

### 3.13 Personal (EXCLUDE — not business)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| NETFLIX, HULU, DISNEY+, HBO MAX, PARAMOUNT+ | EXCLUDE | — | Personal entertainment streaming. Not deductible. |
| SPOTIFY (personal), APPLE MUSIC, PANDORA | EXCLUDE | — | Personal music. Not deductible. Exception: background music for a business location could be Line 27a, but must be documented. |
| GYM, PLANET FITNESS, EQUINOX, LA FITNESS, ORANGETHEORY | EXCLUDE | — | Personal fitness. Not deductible regardless of "stress relief" claims. |
| GROCERY, WHOLE FOODS, TRADER JOE, COSTCO (personal) | EXCLUDE | — | Personal groceries. Not business. |
| TARGET, WALMART (personal) | EXCLUDE | — | Personal shopping unless specific business supplies can be identified from receipt. Default: personal. |
| AMAZON (unspecified) | TIER 2 — see Section 6.5 | — | Amazon purchases require receipt review. Default: personal (exclude). |
| CLOTHING, NORDSTROM, ZARA, H&M, GAP | EXCLUDE | — | Personal clothing is never deductible even if worn to work, unless it is a uniform unsuitable for everyday wear (scrubs, hard hats, safety gear). |
| MORTGAGE, RENT (personal) | EXCLUDE | — | Personal housing. Home office portion handled separately via Form 8829 or simplified method. |
| UTILITIES (personal home) | EXCLUDE unless home office | — | Personal utility bills. If home office, business % via Form 8829. See Section 6.2. |
| MEDICAL, PHARMACY, CVS, WALGREENS (Rx) | EXCLUDE | — | Personal medical. Not Schedule C. May be Schedule A or health savings account. |
| CHARITABLE, DONATION, TITHE | EXCLUDE from Schedule C | — | Charitable contributions go to Schedule A, not Schedule C. Exception: sponsorships with advertising value (see Line 8). |
| VENMO (personal transfers), ZELLE (personal), CASH APP (personal) | EXCLUDE | — | Personal transfers between accounts or to friends/family |
| CHILD CARE, DAYCARE, TUITION (children) | EXCLUDE | — | Personal expenses. May qualify for child care credit (Form 2441), not Schedule C. |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Chase Business Checking statement for a US-based freelance software developer.

### Example 1 — Stripe payout (NOT revenue)

**Input line:**
`01/15/2025 ; STRIPE TRANSFER ; DEPOSIT ; STRIPE PAYOUT ; $4,827.50`

**Reasoning:**
Stripe payout is the net amount after Stripe fees. This is an internal settlement transfer, NOT the gross revenue. The gross revenue for this period (from the Stripe dashboard) may be $5,000 with $172.50 in fees. The bank deposit should be EXCLUDED as a transfer. Revenue is captured from 1099-K or Stripe reports at the gross level on Line 1. Stripe fees are deducted on Line 27a.

**Output:**

| Date | Counterparty | Amount | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|
| 01/15/2025 | STRIPE TRANSFER | +$4,827.50 | — | Y | Q1 | EXCLUDED: Stripe payout — reconcile to gross revenue from Stripe dashboard |

### Example 2 — SaaS subscription (clear business expense)

**Input line:**
`02/01/2025 ; GITHUB INC ; DEBIT ; GITHUB TEAM PLAN ; -$19.00`

**Reasoning:**
GitHub is a developer tool used for business. Pattern match to Section 3.3. Monthly subscription well under the $2,500 de minimis safe harbor. Expense directly on Line 27a as "Software subscriptions."

**Output:**

| Date | Counterparty | Amount | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|
| 02/01/2025 | GITHUB INC | -$19.00 | 27a "Software subscriptions" | N | — | — |

### Example 3 — Restaurant meal (needs substantiation)

**Input line:**
`03/12/2025 ; THE CAPITAL GRILLE ; DEBIT ; RESTAURANT ; -$187.42`

**Reasoning:**
Restaurant charge. Under §274(n)(1), business meals are 50% deductible. Under §274(d), the taxpayer must have: (a) the amount, (b) the date and place, (c) the business purpose, and (d) the business relationship of the people present. The bank statement alone provides (a) and (b) but NOT (c) or (d). Conservative default: exclude as personal until business purpose is confirmed. Flag as Tier 2.

**Output:**

| Date | Counterparty | Amount | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|
| 03/12/2025 | THE CAPITAL GRILLE | -$187.42 | 24b (50%) or EXCLUDE | Y | Q2 (HIGH if >$75) | "Meal: needs §274(d) substantiation — who was present and business purpose?" |

### Example 4 — Laptop purchase near OBBBA cutoff

**Input line:**
`01/22/2025 ; APPLE STORE ; DEBIT ; MACBOOK PRO 16 ; -$3,499.00`

**Reasoning:**
$3,499 exceeds the $2,500 de minimis safe harbor (assuming no AFS). This must be capitalized. Acquisition date is January 22, 2025 — three days AFTER the OBBBA cutoff of January 19, 2025. Eligible for 100% bonus depreciation under IRC §168(k) as amended by OBBBA. However, the bank transaction date is NOT necessarily the acquisition date — the order may have been placed earlier. This falls within the 30-day OBBBA cutoff window (Dec 20, 2024 through Feb 18, 2025). Both treatments must be prepared.

**Output:**

| Date | Counterparty | Amount | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|
| 01/22/2025 | APPLE STORE | -$3,499.00 | 13 (Form 4562) | Y | Q3 (HIGH) | "Asset in OBBBA cutoff window. 100% bonus if acquired after Jan 19; 40% if before. Verify order/purchase date." |

### Example 5 — Gas station (vehicle business use unknown)

**Input line:**
`04/08/2025 ; SHELL OIL ; DEBIT ; FUEL PURCHASE ; -$62.18`

**Reasoning:**
Gas station charge. Could be business vehicle fuel (Line 9) or personal vehicle. If the taxpayer uses the standard mileage method, fuel is already included and this is NOT separately deductible. If actual expense method, only the business-use % is deductible. Without a mileage log or confirmed vehicle method election, conservative default is 0% business use. Tier 2 flag.

**Output:**

| Date | Counterparty | Amount | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|
| 04/08/2025 | SHELL OIL | -$62.18 | 9 (0%) or EXCLUDE | Y | Q4 | "Vehicle expense: what vehicle, what method (standard mileage or actual), what business-use %? Mileage log?" |

### Example 6 — IRS estimated tax payment (always exclude)

**Input line:**
`06/15/2025 ; IRS USATAXPYMT ; DEBIT ; ESTIMATED TAX ; -$5,000.00`

**Reasoning:**
Federal estimated tax payment. This is a personal income tax obligation, NOT a business expense. Never deductible on Schedule C. Always exclude.

**Output:**

| Date | Counterparty | Amount | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|
| 06/15/2025 | IRS USATAXPYMT | -$5,000.00 | — | N | — | EXCLUDED: Federal tax payment — personal, not business |

---

## Section 5 — Tier 1 rules (when data is clear)

Each rule states the legal source and the Schedule C line assignment. Apply silently if the data is unambiguous. No inline tier tags.

### 5.1 Revenue recognition (Line 1)

Gross receipts include all income from the trade or business. Report on the CASH basis for most sole proprietors (unless the taxpayer has elected accrual or is required to use it under §448). Include: client payments, 1099-NEC amounts, 1099-K amounts, cash/barter income, tips. Do NOT net out expenses. Payment processor deposits must be reconciled to gross (see Section 3.2). IRC §61; §446; Schedule C Instructions Line 1.

### 5.2 Depreciation — the OBBBA framework (Line 13)

**Property acquired after January 19, 2025:** 100% bonus depreciation under §168(k) as amended by OBBBA. No phase-down. §179 expensing also available ($2.5M limit, $4M phase-out).

**Property acquired on or before January 19, 2025:** 40% bonus depreciation under pre-OBBBA phase-down schedule. §179 expensing available under OBBBA limits (applies to property placed in service in tax years beginning after Dec 31, 2024).

**The acquisition date** is the date of the binding written contract, or the date the property was ordered for retail purchases, or the date construction began for self-constructed property. The bank transaction date is NOT necessarily the acquisition date.

**30-day OBBBA cutoff window (Dec 20, 2024 through Feb 18, 2025):** Any asset acquired in this window requires dual treatment in the working paper — both 40% and 100% bonus calculated. Reviewer decides based on documentation.

**De minimis safe harbor:** Items costing $2,500 or less per item (no AFS) may be expensed directly to Line 18 (office expense) or Line 22 (supplies) rather than capitalized. Election made annually on the return.

**§179 vs bonus decision:** §179 is income-limited (cannot create NOL); bonus is not. §179 can be elected per-asset; bonus applies to all qualifying property in a class unless the taxpayer elects out of an entire class. The skill captures both options; the reviewer decides.

IRC §167; §168; §168(k); §179; §263; Treas. Reg. §1.263(a)-1(f); OBBBA P.L. 119-21; Pub 946 (2025); Form 4562 Instructions.

### 5.3 Home office (Form 8829 or simplified method)

**Two methods:**
- **Simplified method:** $5/sq ft, max 300 sq ft, max $1,500 deduction. No carryover. No depreciation of the home. Cannot exceed gross income from the business.
- **Actual method (Form 8829):** Allocate actual expenses (mortgage interest, rent, insurance, utilities, repairs, depreciation) by the business-use percentage (office sq ft / total home sq ft). Subject to gross income limitation; excess carries forward.

**Qualification:** The home office must be used REGULARLY and EXCLUSIVELY for business. It must be the taxpayer's PRINCIPAL place of business, a place where the taxpayer meets clients, or a separate structure. The "exclusively" test means no dual use (no guest bedroom that doubles as an office). IRC §280A; Pub 587 (2025).

**Conservative default:** If no home office measurements provided, deduction is $0. Do not estimate.

### 5.4 Vehicle expenses (Line 9)

**Standard mileage method:** 70 cents/mile for 2025 (Notice 2025-5). Multiply by business miles. Parking and tolls deductible separately. Depreciation is included in the rate.

**Actual expense method:** Gas, oil, repairs, insurance, registration, depreciation, lease payments — all multiplied by business-use %. Subject to §280F luxury auto caps for passenger vehicles under 6,000 lbs.

**Method lock-in:** If standard mileage was elected in the first year the vehicle was used for business, taxpayer may switch to actual later (with straight-line depreciation). If actual method with MACRS was elected first, taxpayer is LOCKED IN to actual for that vehicle's life.

**§274(d) substantiation:** A contemporaneous mileage log is required showing: date, destination, business purpose, and miles driven. Without the log, the deduction is $0 under the strict §274(d) rule. Reconstructed estimates are not sufficient.

**Commuting is NEVER deductible.** Treas. Reg. §1.162-2(e); Rev. Rul. 99-7. Exception: if the home office qualifies as the principal place of business, trips from home to client sites are business miles, not commuting.

**Heavy vehicles (>6,000 lbs GVW):** Not subject to §280F caps. Eligible for §179 (subject to $31,300 SUV cap) and 100% bonus depreciation if acquired after Jan 19, 2025.

### 5.5 Meals (Line 24b — 50% deductible)

Business meals are 50% deductible under §274(n)(1). Must satisfy §274(d) substantiation: amount, date, place, business purpose, business relationship of attendees. Entertainment is 0% deductible under §274(a)(1) post-TCJA — no exceptions.

De minimis fringes (office snacks, coffee for the workplace) are 100% deductible under §132(e).

The 100% restaurant meal deduction DOES NOT EXIST in 2025. Expired December 31, 2022.

### 5.6 Travel (Line 24a)

Business travel away from the tax home is deductible: airfare, lodging, rental car, ground transportation, tips, dry cleaning, and 50% of meals while traveling. The travel must be primarily for business. If a trip has both business and personal days, only the business-purpose portion of transportation is deductible (for domestic travel); lodging/meals only for business days. For international travel, special allocation rules apply if the trip exceeds 7 days and personal days exceed 25%.

IRC §162; §274(d); Pub 463 (2025).

### 5.7 Contract labor and 1099-NEC (Line 11)

Payments to independent contractors for services performed for the business. Every contractor paid $600+ in the calendar year via non-TPSO methods (Zelle, ACH, wire, check, cash, Venmo personal) requires a 1099-NEC by January 31 of the following year. Payments via credit card, PayPal, Stripe, Square, or Venmo Business are reported by the platform on 1099-K and do NOT require a 1099-NEC from the payor.

**Zelle is the most common trap.** Zelle is bank-to-bank, not a TPSO under §6050W. The payor must issue the 1099-NEC.

IRC §162; §6041A; §6050W; §6071(c); §3406; §6721; §6722.

### 5.8 Insurance (Line 15)

Business insurance premiums (general liability, professional liability, E&O, workers comp, business property, cyber liability). Personal insurance (auto, home, health, life) is NOT on Schedule C. Self-employed health insurance goes on Schedule 1 line 17. IRC §162; Schedule C Instructions Line 15.

### 5.9 Taxes and licenses (Line 23)

Business licenses, permits, state/local business taxes (NOT income tax), employer portion of FICA/FUTA, property tax on business assets. Federal income tax and state personal income tax are NEVER on Schedule C. Sales tax remittance: if included in Line 1 gross receipts, the remittance goes to Line 23; if excluded from Line 1, it does not appear. IRC §164; Schedule C Instructions Line 23.

### 5.10 Interest (Lines 16a/16b)

Business mortgage interest (Line 16a) and other business interest (Line 16b). Vehicle loan interest (business-use %) goes to Line 16b. The OBBBA personal auto loan interest deduction flows to Schedule 1-A, NOT Schedule C. Only the business-use portion of vehicle loan interest belongs on Line 16b. IRC §163; §163(j).

### 5.11 Rent (Lines 20a/20b)

Vehicle/equipment leases → Line 20a. Office rent, coworking → Line 20b. Personal rent is NOT deductible (home office is handled separately via Form 8829). IRC §162.

### 5.12 Advertising (Line 8)

Costs of promoting the business: digital ads (Google, Meta, LinkedIn), print ads, business cards, website hosting/design, domain registration, SEO, email marketing, trade show booths, promotional items. Political contributions and lobbying are NOT deductible (§162(e)). Client gifts are limited to $25/recipient/year under §274(b)(1) — excess is nondeductible. IRC §162; §274(b).

### 5.13 Supplies and office expense (Lines 18/22)

Office supplies, postage, printing, small equipment under the de minimis safe harbor ($2,500). Line 18 vs Line 22 distinction is flexible; the skill defaults to Line 18 for office/admin items and Line 22 for operational supplies used in delivering the service/product. IRC §162; Treas. Reg. §1.162-3.

### 5.14 Hobby loss rule (§183)

If Schedule C shows a net loss, the IRS may challenge the activity as a hobby under §183. The presumption of profit-motive is met if the activity is profitable in 3 of the last 5 years. Nine factors under Treas. Reg. §1.183-2 are considered. If hobby: income is reported but deductions are limited to hobby income amount. The skill flags any net loss for reviewer awareness.

### 5.15 Items that NEVER go on Schedule C

- Federal income tax payments (personal obligation)
- State income tax payments (personal; Schedule A if itemizing)
- Owner draws / distributions (not an expense)
- Owner's health insurance premiums (Schedule 1 line 17)
- Owner's retirement contributions (Schedule 1 line 16)
- Personal expenses of any kind (§262)
- Charitable contributions (Schedule A)
- Commuting expenses (§262; Treas. Reg. §1.162-2(e))
- Political contributions (§162(e))
- Fines and penalties paid to government (§162(f))
- Clothing suitable for everyday wear
- Personal loan payments
- Personal credit card payments

---

## Section 6 — Tier 2 catalogue (when data is insufficient)

For each ambiguity type: pattern, why the bank statement alone is insufficient, conservative default, question for the structured form.

### 6.1 Vehicle business-use percentage

*Pattern:* SHELL, CHEVRON, BP, EXXON, car wash, Jiffy Lube, any fuel/vehicle maintenance charge. *Why insufficient:* The bank statement shows the charge but not: (a) which vehicle, (b) whether it is used for business, (c) what percentage is business vs personal, (d) whether the taxpayer uses standard mileage or actual expense method, (e) whether a §274(d) mileage log exists. *Default:* 0% business use (no deduction). *Question:* "Do you use a vehicle for business? Which method do you use — standard mileage (70 cents/mile) or actual expenses? What percentage of total miles are business? Do you have a contemporaneous mileage log?"

### 6.2 Home office

*Pattern:* home utility bills (electric, gas, internet at home address), home insurance, home mortgage interest. *Why insufficient:* The bank statement shows the utility payment but not: (a) whether the taxpayer has a qualifying home office, (b) the square footage of the office, (c) the total square footage of the home, (d) whether the space is used regularly and exclusively for business. *Default:* 0% (no deduction). *Question:* "Do you have a dedicated home office used regularly and exclusively for business? What is the square footage of the office space? What is the total square footage of your home? Do you prefer the simplified method ($5/sq ft, max $1,500) or the actual expense method (Form 8829)?"

### 6.3 Meals (business purpose unknown)

*Pattern:* any restaurant, cafe, bar, food delivery (Uber Eats, DoorDash, Grubhub). *Why insufficient:* §274(d) requires documentation of business purpose and attendees. A bank statement charge at a restaurant could be: (a) a business meal with a client (50% deductible), (b) a solo working lunch (generally NOT deductible unless traveling away from tax home), (c) a personal meal (not deductible). *Default:* personal (exclude). *Question:* "For each restaurant charge, was it a business meal? If yes: who was present, and what was the business purpose?"

### 6.4 Phone/internet business percentage

*Pattern:* VERIZON, AT&T, T-MOBILE, COMCAST, XFINITY — personal phone or home internet plan. *Why insufficient:* A single phone line or home internet plan shared between personal and business use. The business % is not determinable from the statement. *Default:* 0% (no deduction). *Question:* "Is this a dedicated business phone/internet line, or a personal plan with some business use? If shared, what percentage do you estimate is business use?"

### 6.5 Amazon purchases

*Pattern:* AMAZON, AMZN, AMAZON.COM, AMZN MKTP. *Why insufficient:* Amazon sells everything from office supplies to personal groceries. The bank statement description rarely identifies the specific product. *Default:* personal (exclude). *Question:* "Could you check your Amazon order history for these dates and identify which purchases were for business? For each business item, what was it and how is it used in your business?"

### 6.6 Cash withdrawals

*Pattern:* ATM WITHDRAWAL, CASH WITHDRAWAL, ATM FEE. *Why insufficient:* Unknown what the cash was spent on. Could be business supplies, could be personal. *Default:* owner draw (exclude). *Question:* "What was the cash used for? If business, do you have receipts?"

### 6.7 Mixed business/personal subscriptions

*Pattern:* ADOBE, MICROSOFT, Apple (iCloud, Apple One), Google (YouTube Premium). *Why insufficient:* Some subscriptions are clearly business (Adobe Creative Cloud for a designer), others are clearly personal (Netflix), but many are mixed (Adobe plan that includes personal Lightroom use). *Default:* if the pattern matches Section 3.3 (SaaS/cloud), treat as business. If not in Section 3.3, treat as personal. *Question:* "Is the [subscription name] used primarily for business? If mixed, what percentage is business use?"

### 6.8 Travel with personal days

*Pattern:* a flight + hotel sequence where the trip duration suggests personal extension (e.g., departing Friday, returning the following Sunday — a weekend trip tacked onto a business meeting). *Why insufficient:* The allocation between business and personal days is fact-dependent. For domestic travel, transportation is 100% deductible if the trip is primarily business. Lodging and meals are deductible only for business days. *Default:* exclude the entire trip until the business/personal day split is documented. *Question:* "For this trip to [destination]: how many days were for business? How many were personal? What was the business purpose?"

---

## Section 7 — Excel working paper template

The base specification is in `us-tax-workflow-base` Section 3. This section provides the US Schedule C overlay.

### Sheet "Transactions"

Columns:

| Column | Content |
|---|---|
| A | Date |
| B | Counterparty (as on statement) |
| C | Description |
| D | Amount (negative for debits, positive for credits) |
| E | Schedule C Line |
| F | Gross amount (before any limitation, e.g., before 50% meals limit) |
| G | Deductible amount (after limitations — e.g., 50% of meals, business-use % of vehicle) |
| H | §274(d) substantiation status (YES / NO / N/A) |
| I | Default applied? (Y/N) |
| J | Question for client (blank if none) |
| K | Reviewer attention reason (blank if none) |
| L | Notes |

### Sheet "Schedule C Summary"

One row per Schedule C line. Column A is the line number, Column B is the description, Column C is the formula summing from Transactions.

```
Part I — Income:
| 1  | Gross receipts | =SUMIFS(Transactions!G:G, Transactions!E:E, "1") |
| 2  | Returns and allowances | =SUMIFS(Transactions!G:G, Transactions!E:E, "2") |
| 4  | Cost of goods sold | =SUMIFS(Transactions!G:G, Transactions!E:E, "4") |
| 6  | Other income | =SUMIFS(Transactions!G:G, Transactions!E:E, "6") |

Part II — Expenses:
| 8  | Advertising | =SUMIFS(Transactions!G:G, Transactions!E:E, "8") |
| 9  | Car and truck | =SUMIFS(Transactions!G:G, Transactions!E:E, "9") |
| 10 | Commissions and fees | =SUMIFS(Transactions!G:G, Transactions!E:E, "10") |
| 11 | Contract labor | =SUMIFS(Transactions!G:G, Transactions!E:E, "11") |
| 13 | Depreciation / §179 | =SUMIFS(Transactions!G:G, Transactions!E:E, "13") |
| 14 | Employee benefits | =SUMIFS(Transactions!G:G, Transactions!E:E, "14") |
| 15 | Insurance | =SUMIFS(Transactions!G:G, Transactions!E:E, "15") |
| 16a| Interest — mortgage | =SUMIFS(Transactions!G:G, Transactions!E:E, "16a") |
| 16b| Interest — other | =SUMIFS(Transactions!G:G, Transactions!E:E, "16b") |
| 17 | Legal and professional | =SUMIFS(Transactions!G:G, Transactions!E:E, "17") |
| 18 | Office expense | =SUMIFS(Transactions!G:G, Transactions!E:E, "18") |
| 20a| Rent — vehicles/equip | =SUMIFS(Transactions!G:G, Transactions!E:E, "20a") |
| 20b| Rent — other property | =SUMIFS(Transactions!G:G, Transactions!E:E, "20b") |
| 21 | Repairs and maintenance | =SUMIFS(Transactions!G:G, Transactions!E:E, "21") |
| 22 | Supplies | =SUMIFS(Transactions!G:G, Transactions!E:E, "22") |
| 23 | Taxes and licenses | =SUMIFS(Transactions!G:G, Transactions!E:E, "23") |
| 24a| Travel | =SUMIFS(Transactions!G:G, Transactions!E:E, "24a") |
| 24b| Meals (50% applied) | =SUMIFS(Transactions!G:G, Transactions!E:E, "24b") |
| 25 | Utilities | =SUMIFS(Transactions!G:G, Transactions!E:E, "25") |
| 26 | Wages | =SUMIFS(Transactions!G:G, Transactions!E:E, "26") |
| 27a| Other expenses | =SUMIFS(Transactions!G:G, Transactions!E:E, "27a") |
```

### Sheet "Return Form"

Final Schedule C-ready figures:
```
Line 7  = Gross income = (Line 1 - Line 2 - Line 4) + Line 6
Line 28 = Total expenses = SUM(Lines 8 through 27a)
Line 29 = Tentative profit/loss = Line 7 - Line 28
Line 30 = Business use of home (from Form 8829 or simplified method)
Line 31 = Net profit or loss = Line 29 - Line 30
```

Positive Line 31 = net profit (flows to Form 1040 Schedule 1 and Schedule SE).
Negative Line 31 = net loss (flag for §183 hobby loss risk).

### Sheet "Asset Register" (for Form 4562)

One row per depreciable asset:

| Column | Content |
|---|---|
| A | Asset description |
| B | Date acquired |
| C | Date placed in service |
| D | Cost/basis |
| E | Recovery period (5-yr, 7-yr, etc.) |
| F | Convention (half-year / mid-quarter) |
| G | Method (200DB, 150DB, SL) |
| H | §179 election amount |
| I | Bonus depreciation % (40% or 100%) |
| J | Current year depreciation |
| K | OBBBA cutoff flag (Y/N) |
| L | Notes |

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values from the bank statement (Columns A-D of Transactions), black for formulas (everything in Schedule C Summary and Return Form), green for cross-sheet references, yellow background for any row in Transactions where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/schedule-c-<year>-working-paper.xlsx
```

Check the JSON output. If `status` is `errors_found`, fix and re-run. If `status` is `success`, present via `present_files`.

---

## Section 8 — US bank statement reading guide

Follow the universal exclusion rules in `us-tax-workflow-base` Step 6, plus these US-specific patterns.

### Chase Business Checking CSV format

Typical columns: `Details, Posting Date, Description, Amount, Type, Balance, Check or Slip #`. Dates in MM/DD/YYYY. Debits are negative amounts. Credits are positive. Description field contains the counterparty name, often with terminal codes or reference numbers appended.

Common Chase patterns:
- `ORIG CO NAME:STRIPE TRANSFER` — Stripe payout
- `CHASE CREDIT CRD AUTOPAY` — personal credit card payment from business account (EXCLUDE as owner draw)
- `GUSTO` or `ADP` — payroll service (Line 26 for wages, Line 23 for employer taxes)
- `ONLINE TRANSFER TO CHK...` — internal transfer between Chase accounts (EXCLUDE)

### Wells Fargo Business CSV format

Typical columns: `Date, Amount, *, Check Number, Description`. Dates in MM/DD/YYYY. Debits are negative. Description is usually `PURCHASE AUTHORIZED ON MM/DD [COUNTERPARTY] CARD XXXX` or `ONLINE TRANSFER REF [number]`.

Common Wells Fargo patterns:
- `PURCHASE AUTHORIZED ON` — card purchase; counterparty name follows the date
- `BILL PAY` — scheduled payment; payee name follows
- `WIRE TYPE:WIRE IN` — incoming wire (could be client payment)

### Mercury CSV format

Typical columns: `Date, Description, Amount, Status, Bank Description, Running Balance`. Clean, fintech-friendly format. Dates in YYYY-MM-DD. Description is usually clear. Stripe/PayPal payouts clearly labeled.

### Internal transfers and exclusions

Own-account transfers between the taxpayer's bank accounts. Labeled "transfer," "online transfer," "ACH transfer" between accounts with similar ownership. Always exclude. Credit card payments from the business account: if paying a personal card, exclude as owner draw. If paying a business credit card, the individual charges on the card are the deductible items (not the lump payment).

### Owner draws and personal use

Any payment to the owner personally, transfer to a personal account, or use of business funds for personal expenses is an owner draw. Exclude. Not a business expense. Not a deduction.

### Refunds and returns

Identify by "refund", "return", "credit", "reversal", "chargeback". Book as a negative against the original line item. If the original classification is unknown, default to Line 2 (returns and allowances) if it appears to be a customer refund, or reduce the relevant expense line if it is a vendor refund.

### Credit card statements as supplementary data

If the taxpayer provides credit card statements in addition to bank statements, the credit card charges are the line-item transactions to classify. The bank statement will show a lump credit card payment — that payment is NOT a deductible expense (it is a debt payment). The individual charges on the credit card are the deductible items.

### Duplicate detection

Watch for the same transaction appearing on both the bank statement (as a card purchase) and a credit card statement. This is the same expense and must not be double-counted. The credit card statement is the detail; the bank statement payment is the settlement.

---

## Section 9 — Onboarding fallback

The workflow in `us-tax-workflow-base` mandates inferring the client profile from the data first and only confirming with the client when inference fails. The questionnaire below is a fallback — ask only the questions the data could not answer.

### 9.1 Entity type
*Inference rule:* "DBA" or individual name = sole prop. "LLC" in the business name = single-member LLC. Multiple names = possible partnership (trigger R-US-PARTNERSHIP if confirmed). *Fallback:* "Are you a sole proprietor, single-member LLC, partnership, S-corp, or C-corp?"

### 9.2 Accounting method
*Inference rule:* most sole props use cash basis. If the taxpayer has inventory and gross receipts above $31M, accrual may be required. *Fallback:* "Do you use the cash or accrual method of accounting?"

### 9.3 Principal business activity
*Inference rule:* counterparty mix, 1099-NEC descriptions, nature of income. IT, consulting, design, writing, photography, construction are recognizable from transaction patterns. *Fallback:* "What does your business do? (Need the NAICS code for Schedule C line B.)"

### 9.4 EIN or SSN
*Inference rule:* not inferable from bank statements. *Fallback:* "Do you have an EIN for the business, or do you use your SSN?"

### 9.5 Prior year return
*Inference rule:* not inferable. Always ask. *Question:* "Do you have last year's Schedule C and Form 4562? (Needed for depreciation carry-forward and vehicle method elections.)"

### 9.6 Home office
*Inference rule:* if the taxpayer's address is residential and there is no separate office rent payment, a home office is possible. *Fallback:* "Do you have a home office? Is it used regularly and exclusively for business?"

### 9.7 Vehicle use
*Inference rule:* presence of fuel/vehicle maintenance charges. *Fallback:* "Do you use a vehicle for business? Do you have a mileage log? What method do you use — standard mileage or actual expenses?"

### 9.8 Employees
*Inference rule:* presence of payroll service charges (Gusto, ADP), multiple large regular payments to individuals. *Fallback:* "Do you have any employees (W-2)?"

### 9.9 Inventory
*Inference rule:* presence of wholesale supplier payments, COGS-like patterns. *Fallback:* "Do you sell physical products? Do you maintain inventory?" If yes and gross receipts are under $31M, the §471(c) small business exception likely applies (treat inventory as non-incidental materials and supplies, deduct when used/sold).

### 9.10 Health insurance
*Inference rule:* presence of health insurance premium payments. *Fallback:* "Do you pay for your own health insurance? Were you eligible for employer-sponsored coverage from a spouse's employer at any time during the year?" (Affects the self-employed health insurance deduction on Schedule 1.)

---

## Section 10 — Reference material

### Primary legislation

1. **Internal Revenue Code** (Title 26 USC) — all sections cited throughout this skill
2. **One Big Beautiful Bill Act (OBBBA)** — Public Law 119-21, signed July 4, 2025. Key provisions: §179 limit increase to $2.5M/$4M, 100% bonus depreciation restoration for property acquired after Jan 19, 2025, permanent QBI deduction at 20% (rising to 23% in 2026), new tip/overtime/auto loan interest deductions on Schedule 1-A

### Treasury Regulations (26 CFR)

3. Treas. Reg. §1.162-1 through §1.162-5 — Business expenses, traveling expenses, materials and supplies, repairs, education
4. Treas. Reg. §1.179-1 through §1.179-6 — Section 179 elections
5. Treas. Reg. §1.183-1, §1.183-2 — Hobby loss factors
6. Treas. Reg. §1.263(a)-1(f) — De minimis safe harbor
7. Treas. Reg. §1.263(a)-2, §1.263(a)-3 — Tangible property, improvements (betterments, restorations, adaptations)
8. Treas. Reg. §1.274-2, §1.274-5T, §1.274-12 — Entertainment disallowance, substantiation, meals limitation
9. Treas. Reg. §1.280A-1, §1.280A-2 — Business use of home
10. Treas. Reg. §1.280F-6 — Listed property
11. Treas. Reg. §1.471-1 — Inventories

### Revenue Procedures, Notices, Revenue Rulings

12. Rev. Proc. 2013-13 — Simplified method for home office deduction
13. Rev. Proc. 2024-40 — 2025 inflation adjustments
14. Rev. Proc. 2025-16 — 2025 luxury auto depreciation caps and lease inclusion
15. Notice 2024-80 — 2025 retirement plan limitations
16. Notice 2025-5 — 2025 standard mileage rates
17. Rev. Rul. 99-7 — Commuting expenses

### IRS Publications and Form Instructions

18. Pub 334 (2025) — Tax Guide for Small Business
19. Pub 463 (2025) — Travel, Gift, and Car Expenses
20. Pub 587 (2025) — Business Use of Your Home
21. Pub 946 (2025) — How to Depreciate Property
22. Schedule C (Form 1040) Instructions (2025)
23. Form 4562 Instructions (2025)
24. Form 8829 Instructions (2025)
25. Form 1099-NEC Instructions (2025)

### Court decisions

26. Welch v. Helvering, 290 U.S. 111 (1933) — "Ordinary and necessary" standard
27. Cohan v. Commissioner, 39 F.2d 540 (2d Cir. 1930) — Estimation of expenses (substantially limited by §274(d))
28. Commissioner v. Soliman, 506 U.S. 168 (1993) — Principal place of business for home office

### Known gaps

1. The supplier pattern library in Section 3 covers common US vendors but does not cover every regional or niche business. Add patterns as they emerge.
2. The worked examples are drawn from a hypothetical freelance software developer. They do not cover retail, e-commerce, construction, or professional services specifically.
3. OBBBA implementation guidance was still being issued in early 2026. Some positions (particularly the acquisition-date test for the Jan 19, 2025 cutoff) may be clarified by future Treasury guidance.
4. The standard mileage rate, §179 limits, §280F caps, and QBI thresholds are 2025-specific. Verify annually before use.
5. State tax implications are entirely out of scope. Every state has its own conformity rules for OBBBA provisions.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. Quick reference with year-specific figures and conservative defaults table moved to Section 1. Required inputs and refusal catalogue restructured (Section 2, 10 refusals). Supplier pattern library with 13 US vendor categories (Section 3). Six worked examples from Chase Business Checking (Section 4). Tier 1 rules as sections without inline tags (Section 5, 15 rules). Tier 2 catalogue with 8 ambiguity types (Section 6). Excel working paper template with asset register (Section 7). US bank statement reading guide with Chase/Wells Fargo/Mercury formats (Section 8). Onboarding fallback with inference rules (Section 9, 10 items). Reference material consolidated (Section 10).
- **v0.2 (prior):** Added 1099-NEC payment method trap (Zelle/ACH), OBBBA 30-day cutoff dual treatment, expanded contract labor section.
- **v0.1 (initial):** Initial skill covering Schedule C classification, OBBBA depreciation, §274 substantiation.

### Self-check (v2.0 of this document)

1. Quick reference at top with Schedule C line table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 13 sub-tables).
3. Worked examples from hypothetical bank statement: yes (Section 4, 6 examples).
4. Tier 1 rules as sections without inline tags: yes (Section 5, 15 rules).
5. Tier 2 catalogue with conservative defaults and questions: yes (Section 6, 8 items).
6. Excel template specification with mandatory recalc: yes (Section 7).
7. Onboarding as fallback with inference rules first: yes (Section 9, 10 items).
8. All 10 refusals present: yes (Section 2, R-US-PARTNERSHIP through R-US-ESTATE-TRUST).
9. Reference material at bottom: yes (Section 10).
10. §179 limit $2.5M explicit: yes (Section 1 table).
11. 100% bonus depreciation post-OBBBA explicit: yes (Sections 1, 5.2).
12. Standard mileage 70 cents explicit: yes (Section 1 table).
13. Simplified home office $5/sqft max $1,500 explicit: yes (Section 1 table).
14. No 100% restaurant meal deduction warning explicit: yes (Sections 1, 3.7, 5.5).
15. Zelle/1099-NEC trap explicit: yes (Sections 3.11, 5.7).
16. OBBBA 30-day cutoff window explicit: yes (Sections 5.2, Example 4).
17. Entertainment 0% deductible post-TCJA explicit: yes (Sections 1, 3.7, 5.5).
18. Payment processor payout NOT revenue explicit: yes (Sections 3.2, Example 1).

## End of US Sole Prop Bookkeeping Skill v2.0

This skill is incomplete without the companion workflow file loaded alongside it: `us-tax-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a Schedule C working paper without the base loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
