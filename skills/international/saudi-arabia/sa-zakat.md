---
name: sa-zakat
description: "Use this skill whenever asked about Saudi Arabian Zakat — the religious-origin wealth levy administered by ZATCA (Zakat, Tax and Customs Authority) on Saudi/GCC-owned business activity in the Kingdom of Saudi Arabia. Trigger on phrases like \"Saudi Zakat\", \"ZATCA Zakat\", \"Zakatable base Saudi\", \"2.5% Zakat KSA\", \"Implementing Regulations Zakat\", \"Saudi GCC zakat\", \"mixed entity Saudi\", \"Zakat return KSA\", \"Saudi Hijri filing\", \"Zakat working capital base\", \"Zakat net adjusted profit\", \"mixed ownership Saudi Zakat CIT split\", or \"ZATCA 120 days return\". Covers the 2.5% Hijri rate (2.577% Gregorian-equivalent), Zakatable persons (Saudi/GCC nationals and Saudi/GCC-owned share of capital), the higher-of net adjusted profit vs working capital base computation under the Implementing Regulations issued under Ministerial Resolution 2082 of 1438H (2017) as amended, mixed-entity Saudi/GCC vs foreign proportional split (Zakat on Saudi/GCC share; CIT 20% on foreign share — see sa-corporate-tax), passive entities, financing/banking sector specials, accounting-basis adjustments, and ZATCA portal annual filing within 120 days of fiscal year-end. Out of scope: pure CIT on 100%-foreign-owned entities (see sa-corporate-tax), Withholding Tax (see sa-wht), VAT (see saudi-arabia-vat), e-invoicing (see saudi-einvoice), Excise Tax, Real Estate Transaction Tax (RETT), Customs, oil and hydrocarbon sector special regimes, natural gas investment tax, Saudi Aramco special rate, and individual personal Zakat on non-commercial wealth (mosque/charitable Zakat al-mal outside ZATCA scope). ALWAYS read this skill before touching any Saudi Zakat work."
jurisdiction: SA
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# sa-zakat

## Saudi Arabia — Zakat — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill is for informational purposes only and does not constitute tax, legal, religious, or financial advice. All outputs must be reviewed and signed off by a Saudi-licensed Zakat advisor (SOCPA member or ZATCA-approved consultant) before filing or acting upon. Zakat carries both a fiscal and a religious dimension; this skill addresses only the fiscal compliance administered by ZATCA.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Mehran Habib** on 2026-06-06.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Zakat

- **Zakat rate (Hijri year)** — 2.5%  _(Section 1 Article 15(1) Percentage of Zakat - Zakat Implementing Regulation)_
- **Gregorian-equivalent rate** — 2.5772% (adjusted for 354/365 days)  _(Section 1 Article 15(2) Percentage of Zakat - Zakat Implementing Regulation)_
- **Saudi nationals — commercial activity** — Subject to Zakat  _(Royal Decree 8634; Zakat Collection in the Kingdom of Saudi Arabia - A FIQH based Perspective)_
- **GCC nationals — commercial in KSA** — Subject to Zakat (treated as Saudi)  _(Defined in Saudi Definition - Zakat Implementing Regulations)_
- **Foreign-owned companies** — NOT Zakat — CIT 20% instead  _(Chapter Three - Article 7(A) Tax Rates - Income Tax Law)_
- **Mixed ownership** — Saudi/GCC share → Zakat; foreign share → CIT 20%  _(Article 2 & 6 of Zakat Implementing Regulations)_
- **Deadline** — 120 days after fiscal year-end  _(Chapter Five - Article 102(1) Submission of Zakat Return - Zakat Implementing Regulations)_

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Kingdom of Saudi Arabia (KSA) |
| Tax | Zakat — religious wealth levy administered as a fiscal charge |
| Currency | SAR (Saudi Riyal) |
| Tax authority | **ZATCA** — Zakat, Tax and Customs Authority (merged from GAZT + Saudi Customs, 2021) |
| Primary legislation | Royal Decree No. 17/2/28/8634 of 1370H (1950G) establishing the Zakat charge |
| Implementing Regulations | Ministerial Resolution **No. 2082 of 1438H (2017G)** — Implementing Regulations for Collection of Zakat, as amended (notably amendments in 1442H/2020G, 1444H/2023G, and 1446H/2024-2025) |
| Standard rate | **2.5%** of the Zakatable base (Hijri lunar year) |
| Gregorian-equivalent rate | **2.5772%** for taxpayers filing on a Gregorian fiscal year (adjustment ≈ 354/365 inverted to reflect the ~11-day longer Gregorian year — *verify current ZATCA circular*) |
| Zakatable base | **Higher of**: (a) Net adjusted profit, or (b) Working capital base (capital + reserves + provisions + long-term liabilities + adjusted profit − long-term assets − deferred expenses, with prescribed adjustments) |
| Zakatable persons | (a) Saudi & GCC natural persons engaged in commercial activity; (b) companies wholly owned by Saudi/GCC nationals; (c) Saudi/GCC-owned share of capital in mixed-ownership companies |
| Mixed entity | Saudi/GCC share → Zakat 2.5%; foreign share → CIT 20% (see sa-corporate-tax). Same accounting profit, split adjustments |
| Annual return | Zakat Declaration via ZATCA portal |
| Filing deadline | Within **120 days** of fiscal year-end |
| Payment deadline | Same — within 120 days of FYE |
| Advance instalments | Quarterly advance Zakat may apply for larger taxpayers (threshold per ZATCA notice) |
| Late-payment penalty | **5% per month** of unpaid Zakat, capped at **25%** |
| Failure-to-file penalty | Per ZATCA penalty schedule (variable; verify current circular) |
| Calendar election | Taxpayer may elect Hijri or Gregorian fiscal year; most large taxpayers elect Gregorian (rate adjusted) |
| Validated by | Pending — sign-off by SOCPA-licensed Zakat advisor |
| Skill version | 1.0 |

### 1.1 Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Ownership mix unclear | Treat as mixed entity — apply Saudi/GCC vs foreign split |
| GCC national status of shareholder unclear | Treat as non-GCC foreign (CIT 20% applies to that share) |
| Hijri vs Gregorian year unclear | Assume Gregorian (use 2.5772% — most common large-taxpayer filing) |
| Adjustment item categorisation unclear | Treat as **add-back to base** (conservative — increases Zakatable base) |
| Long-term vs short-term liability classification unclear | Treat as short-term (excluded from working capital additions) |
| Long-term vs short-term asset classification unclear | Treat as long-term (deducted from working capital base — but verify, this *reduces* base, so the conservative direction depends on which side of "higher of" you sit; default to **whichever yields the higher Zakatable base** as a conservative rule) |
| Provision deductibility for Zakat purposes unclear | Add to base (conservative) |
| Financing arrangement Sharia-compliance unclear | Apply standard adjustment rules; flag for advisor |
| Advance Zakat instalment obligation unknown | Assume required — verify with ZATCA notice |
| Recent regulation amendment status | Flag "verify latest ZATCA circular (2024-2025 amendments to Implementing Regulations re: financing arrangements and intangibles)" |

## Section 2 — Required Inputs and Refusal Catalogue

### 2.1 Required Inputs

- **Minimum viable** — Full-year financial statements (income statement, balance sheet) prepared under SOCPA-endorsed IFRS, a complete shareholder register identifying Saudi/GCC vs foreign ownership percentages at the FYE (and ideally throughout the year), prior-year Zakat return, and confirmation of (i) fiscal calendar election (Hijri vs Gregorian), (ii) advance instalment status, (iii) any sector-specific designation.
- **Recommended** — General ledger, fixed-asset register (with classification of long-term vs short-term), full schedule of provisions and reserves, related-party transaction schedule, financing arrangement schedule (Sharia-compliant and conventional), commercial registration (CR) and ZATCA Zakat registration certificate.
- **Ideal** — SOCPA-audited financial statements, full reconciliation from accounting profit to Zakatable net adjusted profit, working capital base worksheet with every line item supported, ownership percentage attestation, ZATCA prior-year assessment notice.
- **HARD STOP if minimum is missing** — Without financial statements and an ownership breakdown, no Zakat computation may be produced. Ownership identification is the gating fact — it determines Zakat-vs-CIT routing.

### 2.2 Refusal Catalogue

- **R-SA-Z-1** — 100%-foreign-owned entity. No Zakat applies; route entirely to sa-corporate-tax (CIT 20%). Out of scope here.
- **R-SA-Z-2** — Oil and hydrocarbon sector. Saudi Aramco and upstream oil/gas concessionaires are subject to special tax regimes (rates up to 85% historically; Aramco at 20%/50%/85% tiered post-IPO restructuring). Out of scope. Escalate to a Saudi tax specialist.
- **R-SA-Z-3** — Natural gas investment tax. Separate regime — out of scope.
- **R-SA-Z-4** — Banking and insurance sector specials. Certain Zakat base adjustments specific to financial institutions (statutory deposits with SAMA, regulatory capital treatment, technical reserves for insurers) are outside the general Implementing Regulations framework and require specialist sign-off. Skill produces a preliminary computation only; final return MUST be reviewed by a financial-services Zakat specialist.
- **R-SA-Z-5** — Real Estate Transaction Tax (RETT) interactions. RETT is a separate 5% transactional charge — out of scope.
- **R-SA-Z-6** — Personal Zakat al-mal on non-commercial wealth. Religious obligation outside ZATCA fiscal scope (personal savings, gold, agricultural Zakat, livestock Zakat). Refer the taxpayer to a religious scholar; not a ZATCA filing.
- **R-SA-Z-7** — Group / consolidated Zakat. Saudi tax group regime (introduced under amended regulations) and consolidated returns for related Zakat payers are out of scope of v1.0.
- **R-SA-Z-8** — Permanent establishments / treaty positions. PE attribution under tax treaty rules is out of scope (and largely a CIT question, not Zakat).
- **R-SA-Z-9** — Disputed assessments / objections. ZATCA appeals before the Tax Violations and Disputes Resolution Committee require licensed representation. Out of scope.
- **R-SA-Z-10** — Stale regulation reliance. The Implementing Regulations have been amended several times since 2017G, including in 2024-2025G affecting financing arrangements and intangibles. The skill MUST flag "verify latest ZATCA circular" in every output and refuse to finalise without confirmation that the cited regulation version is current.

## Section 3 — Tier 1: The Zakat Charge

### 3.1 Nature of the Charge

- **Nature of the charge** — Zakat in Saudi Arabia is a hybrid religious-fiscal levy. Its origin is the third Pillar of Islam (obligation to purify wealth by paying 2.5% of qualifying assets held for a lunar year, hawl). The Kingdom has since 1370H (1950G) codified the collection of Zakat from commercial enterprises owned by Saudi nationals as a fiscal charge administered by the state. Since 2021G this is administered by ZATCA (Zakat, Tax and Customs Authority), formed by the merger of the former General Authority of Zakat and Tax (GAZT) and Saudi Customs. The legal basis is Royal Decree No. 17/2/28/8634 of 1370H, with detailed computation rules in the Implementing Regulations for Collection of Zakat issued under Ministerial Resolution No. 2082 of 1438H (2017G), as amended.  _(Royal Decree No. 17/2/28/8634 of 1370H; Ministerial Resolution No. 2082 of 1438H (2017G))_

### 3.2 The Rate

- **Hijri rate** — 2.5% under the Hijri lunar calendar (one hawl = one lunar year ≈ 354.36 days).
- **Gregorian rate** — 2.5772% (commonly rounded to 2.577% or 2.578%) for taxpayers electing a Gregorian fiscal year — the rate is grossed up to reflect the ~11-day longer Gregorian year so that the effective annualised charge matches the lunar-year obligation. The exact percentage published by ZATCA from time to time should be verified.

### 3.3 Persons Subject to Zakat

**Persons Subject to Zakat**

| Person | Treatment |
| --- | --- |
| Saudi natural person — commercial activity | Subject to Zakat on Zakatable base of the business |
| GCC national (Bahrain, Kuwait, Oman, Qatar, UAE) natural person — commercial activity in KSA | Subject to Zakat (treated as Saudi for Zakat purposes) |
| Company wholly owned by Saudi/GCC nationals | Subject to Zakat on entire Zakatable base |
| Company wholly owned by non-GCC foreign persons | **NOT** Zakat — subject to CIT 20% (see sa-corporate-tax) |
| Mixed-ownership company | **Split**: Saudi/GCC share % → Zakat 2.5%; foreign share % → CIT 20%. Same accounting profit, proportional split with separately computed adjustments |
| Listed company shares — Saudi/GCC shareholders | Saudi/GCC-owned proportion of the listed company subject to Zakat |
| Listed company shares — non-GCC foreign shareholders | Foreign-owned proportion subject to CIT 20% |
| Government-owned entities | Generally exempt; specific treatment per ZATCA notice |
| Charitable / non-profit organisations | Generally outside scope; verify registration |

- **GCC** — GCC = Gulf Cooperation Council: Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, United Arab Emirates. GCC nationals are treated as Saudi nationals for Zakat purposes under reciprocal arrangements.

### 3.4 Zakatable Base — The "Higher Of" Rule

- **Zakatable base — higher of** — The Zakatable base is the higher of: (a) Net Adjusted Profit — accounting net profit adjusted per the Implementing Regulations (add-backs for non-deductible items; deductions for already-Zakated items, dividend income from Zakat-paying subsidiaries, etc.). (b) Working Capital Base — a balance-sheet-derived computation: ``` Working Capital Base = Capital (paid-up) + Retained earnings (opening) + Reserves (general, statutory, other) + Provisions (per regulations — most added back) + Long-term liabilities (debt > 1 year, certain financing arrangements) + Adjusted net profit for the year − Net book value of long-term assets (fixed assets, intangibles, investments in long-term subsidiaries) − Deferred expenses / prepayments long-term − Investments in Zakat-paying subsidiaries (to avoid double-Zakat) ± Other adjustments per Implementing Regulations ``` The taxpayer pays Zakat on whichever of (a) or (b) is higher.

Rationale: net adjusted profit captures the income dimension; working capital base captures the wealth dimension (consistent with the religious origin of Zakat as a wealth purification). The "higher of" rule prevents avoidance by either suppressing profit or by structuring capital out of the base.

### 3.5 Filing & Payment in Brief

- **Annual Zakat Declaration** — Annual Zakat Declaration via ZATCA portal.
- **Filing due date** — Within 120 days of fiscal year-end (≈ 4 months). For a Gregorian calendar-year taxpayer with FYE 31 December, the deadline is 30 April of the following year.
- **Payment same window** — Payment same window.
- **Advance Zakat instalments** — Advance Zakat instalments (quarterly) may apply for larger taxpayers per ZATCA notice — verify thresholds.
- **Late-payment penalty** — 5% per month, capped at 25%.

## Section 4 — Tier 2: Computation Details

### 4.1 Mixed Entities — Saudi/GCC vs Foreign Split

- **The mechanics** — 1. Compute the entity's full accounting net profit and full working capital base as if it were a single taxpayer. 2. Identify the ownership percentages at FYE (and ideally weighted across the year if changes occurred — verify ZATCA position). 3. Compute the Saudi/GCC adjusted base and apply 2.5% (or 2.577% Gregorian) Zakat. 4. Compute the foreign adjusted base and apply 20% CIT (cross-reference sa-corporate-tax). 5. Adjustments specific to each regime may differ — for example, the working-capital-base "higher of" rule applies on the Zakat side; CIT applies a profit-only computation.
- **Where ownership changes mid-year** — The conservative default is time-apportionment of the base, but ZATCA practice on this point has evolved — verify current circular.
- **Listed companies** — Saudi/GCC-owned float subject to Zakat; foreign-owned float subject to CIT. Practical apportionment usually based on year-end Tadawul shareholder registry, with weighted-average if material movement.

### 4.2 Passive Entities

- **Holding companies — general** — Holding companies whose income is predominantly dividends/interest from subsidiaries face specific Zakat treatment.
- **Investments in Zakat-paying Saudi/GCC subsidiaries** — Deducted from the working capital base of the parent to avoid double-Zakat (the subsidiary has already paid Zakat on its own base).
- **Investments in non-Zakat (foreign-owned or non-Zakatable) entities** — NOT deducted — remain in the parent's working capital base.
- **Dividend income** — Net adjusted profit adjustments depend on the nature of the source.

The skill flags any holding/passive structure as requiring specialist sign-off (R-SA-Z-4 adjacent).

### 4.3 Financing and Banking Sector Specials

- **Banks** — Statutory deposits with SAMA (Saudi Central Bank), regulatory capital, and specific provisioning rules (ECL / IFRS 9 provisions) interact non-trivially with the Zakat base. Recent ZATCA guidance (post-2020) on financing arrangements affects how Murabaha, Ijarah, and Sukuk are treated in the long-term liability and long-term asset categorisation.
- **Insurers** — Technical reserves, unearned premium reserves, and Takaful pool treatment differ from conventional accounting reserve treatment under the Implementing Regulations.
- **Both sectors** — Out of scope for autonomous computation by this skill — preliminary indicative only; require specialist sign-off (R-SA-Z-4).

### 4.4 Accounting Basis Adjustments

- **Accounting basis** — Saudi entities prepare statements under SOCPA-endorsed IFRS (mandatory for listed companies and large entities; IFRS-SME for smaller). The Zakat computation starts from these statements and applies fiscal adjustments.

**Typical Zakat treatment of items**

| Item | Typical Zakat treatment |
| --- | --- |
| Provisions (general, doubtful debts, etc.) | Added back to working capital base (conservative); reversal on utilisation may reduce base |
| Depreciation | Accounting depreciation generally accepted; specific limits per regulations on certain asset classes |
| Loans to related parties (non-Zakatable) | Treated as long-term asset deduction from base (reducing Zakatable base) — but flag for anti-avoidance review |
| Loans from related parties | Long-term liability addition only if genuine long-term financing |
| Intangibles (goodwill, brands, software) | Recent 2024-2025 amendments — **verify latest ZATCA circular** |
| Sharia-compliant financing (Murabaha, Ijarah, Sukuk) | Re-characterised per ZATCA guidance; substance-over-form approach |
| Foreign-currency translation differences | Per Implementing Regulations; generally follow accounting treatment |
| Deferred tax assets/liabilities | Generally not adjusted into Zakat base (Zakat is not a profit tax) |

- **Critical flag — 2024-2025 amendments** — Recent amendments to the Implementing Regulations have clarified treatment of certain financing arrangements and intangibles. Every output of this skill MUST include the line: "Treatment of [financing arrangement / intangible item] requires verification against the latest ZATCA circular (2024-2025 amendments to Implementing Regulations)."

## Section 5 — Worked Examples

### 5.1 Example A — 100% Saudi-Owned LLC (Simple Trading Company)

**Example A facts and figures**

| Item | SAR |
| --- | --- |
| Paid-up capital | 5,000,000 |
| Retained earnings (opening) | 3,200,000 |
| Statutory reserve | 500,000 |
| General provisions (added back) | 200,000 |
| Long-term bank loan (Sharia-compliant Murabaha) | 4,000,000 |
| Adjusted net profit for the year | 1,800,000 |
| Net book value of fixed assets (long-term) | 6,500,000 |
| Long-term prepayments | 300,000 |

Riyadh-based Saudi LLC, 100% Saudi-owned, FYE 31 December 2025G (Gregorian — rate 2.577%).

- **Working capital base calculation** — = 5,000,000 + 3,200,000 + 500,000 + 200,000 + 4,000,000 + 1,800,000 − 6,500,000 − 300,000 = 7,900,000

**Net adjusted profit**: 1,800,000

**Higher of**: 7,900,000

**Zakat at 2.577%**: 7,900,000 × 2.577% = **SAR 203,583**

Filing deadline: 30 April 2026G. Pay via ZATCA portal. Late-payment penalty 5%/month capped 25% if missed.

### 5.2 Example B — 60/40 Saudi/Foreign Mixed Entity

**Facts**: KSA LLC, 60% Saudi national / 40% Cayman-resident shareholder. FYE 31 December 2025G. Same balance-sheet facts as Example A.

**Step 1 — Single-entity base**: as Example A, working capital base = 7,900,000; net adjusted profit = 1,800,000.

**Step 2 — Saudi/GCC share (60%)**:
- Saudi-share working capital base = 7,900,000 × 60% = 4,740,000
- Saudi-share net adjusted profit = 1,800,000 × 60% = 1,080,000
- Higher of = 4,740,000
- Zakat at 2.577% = **SAR 122,150**

**Step 3 — Foreign share (40%) — CIT (see sa-corporate-tax)**:
- Foreign-share taxable profit = 1,800,000 × 40% = 720,000 (with foreign-specific CIT adjustments — *not* the working-capital-base method, which is Zakat-only)
- CIT at 20% = **SAR 144,000** (illustrative — see sa-corporate-tax for full adjustments)

**Step 4 — Combined liability**: Zakat 122,150 + CIT 144,000 = **SAR 266,150 total**.

Both filed via ZATCA portal within 120 days of FYE. Zakat declaration and CIT declaration are typically filed together as a unified Mixed Entity Declaration.

### 5.3 Example C — Individual Saudi National Sole Trader

**Facts**: Saudi individual operating a sole-trader trading business under a Commercial Registration. FYE 31 December 2025G. Net adjusted profit SAR 450,000; working capital base SAR 380,000.

- Higher of: 450,000 (net adjusted profit wins).
- Zakat at 2.577% = **SAR 11,597**.
- Personal non-commercial Zakat al-mal on the individual's personal savings/gold/etc. is **outside ZATCA scope** (R-SA-Z-6) — refer to a religious scholar.
- Filing deadline: 30 April 2026G.

## Section 6 — Filing and Payment

### 6.1 Process

- **Filing process steps** — 1. **Register / verify Zakat Number** — taxpayers should be registered with ZATCA at incorporation (Commercial Registration triggers ZATCA registration). 2. **Prepare financial statements** under SOCPA-endorsed IFRS. 3. **Compute Zakat base** — both net adjusted profit and working capital base; take higher. 4. **Mixed entities** — also compute CIT for foreign share (cross-reference sa-corporate-tax). 5. **File Zakat Declaration** on the ZATCA portal (https://zatca.gov.sa) — login via taxpayer credentials or licensed representative. 6. **Upload supporting documents** — financial statements, ownership schedule, base computation worksheet. 7. **Pay** via SADAD (Saudi national payments system) or other ZATCA-approved channel within 120 days of FYE. 8. **Obtain Zakat Certificate** (شهادة الزكاة) — required to renew Commercial Registration, bid for government contracts, and clear customs.

### 6.2 Advance Instalments

- **Advance instalments detail** — Larger taxpayers (threshold per ZATCA notice — verify current) may be required to pay quarterly advance Zakat instalments based on prior-year liability, with reconciliation in the annual return. Penalties for missed instalments apply per ZATCA penalty schedule.

### 6.3 Penalties

- **Late payment** — 5% per month of unpaid Zakat, capped at 25%.
- **Failure to file** — variable penalty per ZATCA schedule.
- **Inaccurate return / under-declaration** — ZATCA assessment with penalty (verify current circular).
- **Failure to register** — separate penalty.

### 6.4 Zakat Certificate

- **Uses of Zakat Certificate** — A current-year Zakat Certificate from ZATCA is required to: - Renew the Commercial Registration (annually). - Bid for or be paid on government contracts. - Clear goods through customs (linked to ZATCA's unified ID). - Transfer real estate (interaction with RETT). The certificate is issued upon successful filing and payment.

## Section 7 — Conservative Defaults (Reprise)

When in doubt:

1. **Treat as mixed entity** with foreign-share default — produces both a Zakat number and a CIT number; reviewer can collapse to pure Zakat if pure Saudi ownership is later confirmed.
2. **Use Gregorian rate 2.577%** as the default — the most common large-taxpayer filing basis.
3. **For each adjustment**, ask: "Does this increase or decrease the Zakatable base?" Default to the direction that **increases the base** unless a clear regulation or ruling supports the reduction.
4. **Always flag**: "Treatment of [item] requires verification against the latest ZATCA circular (2024-2025 amendments)."
5. **Refuse to finalise** banking/insurance computations — preliminary only; route to a financial-services Zakat specialist.
6. **Refuse to finalise** any return without sign-off by a SOCPA-licensed Zakat advisor.

## Section 8 — Sources

### 8.1 Primary Legislation

- **Primary legislation list** — - Royal Decree No. 17/2/28/8634 of 1370H (1950G) — establishment of the Zakat charge on commercial activity in the Kingdom. - Ministerial Resolution No. 2082 of 1438H (2017G) — Implementing Regulations for the Collection of Zakat, as amended. - Subsequent amendments — notably 1442H/2020G, 1444H/2023G, and 1446H/2024-2025G (clarifications on financing arrangements and intangibles — verify latest published version on the ZATCA portal).

### 8.2 Administering Body

- **ZATCA** — ZATCA — Zakat, Tax and Customs Authority (Hay'at al-Zakat wa al-Dareeba wa al-Jamarik). Formed 2021G from merger of GAZT and Saudi Customs. Portal: https://zatca.gov.sa.

### 8.3 Related Skills

- **Related skills list** — - sa-corporate-tax — CIT 20% on foreign-owned share of mixed entities and on 100%-foreign-owned entities. - sa-wht — Withholding Tax on payments to non-residents. - saudi-arabia-vat — VAT 15% (since July 2020). - saudi-einvoice — FATOORAH e-invoicing. - foundation — OpenAccountants foundation skill.

### 8.4 Verification Discipline

Every output of this skill MUST end with:

> "This Zakat computation is preliminary. The Zakat base is provisional pending verification against the latest ZATCA circular (most recently amended 1446H/2024-2025G affecting financing arrangements and intangibles). The final return MUST be reviewed and signed off by a SOCPA-licensed Zakat advisor or ZATCA-approved consultant before submission to the ZATCA portal."

## End of sa-zakat skill v1.0.

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
