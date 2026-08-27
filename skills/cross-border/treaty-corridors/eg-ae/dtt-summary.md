---
name: eg-ae-dtt-corridor
description: >
  Use this skill whenever asked about the Egypt-UAE Double Tax Treaty
  — for residents/companies with cross-border flows between the two jurisdictions.
  Trigger on "Egypt UAE tax treaty", "DTT Egypt UAE", "ضريبة الازدواج مصر الإمارات",
  "cross-border Egypt UAE", "Egypt United Arab Emirates withholding". ALWAYS read this
  skill before applying treaty rates.
version: 1.0
jurisdiction: EG-AE
tax_year: 2025
last_updated: 2026-08-02
review_status: pending_review
depends_on:
  - eg-corporate-tax
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt ↔ UAE Double Tax Treaty (DTT) Summary

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Quick Reference

| Field | Value |
|-------|-------|
| Treaty Name | Agreement between the Arab Republic of Egypt and the United Arab Emirates for the Avoidance of Double Taxation and the Prevention of Fiscal Evasion with Respect to Taxes on Income |
| Old Treaty Signed | 2002 (original agreement) |
| Old Treaty In Force | 2003 |
| New Treaty Signed | 7 November 2021 (replaced the 2002 treaty) |
| New Treaty In Force | 19 April 2021 (entered into force); applies from 1 January 2022 |
| Current Version | New TT (2021) replacing Old TT (2002) |
| MLI Status | Egypt ratified MLI (30 Sep 2020). UAE ratified MLI (29 May 2019). MLI applies to this treaty. |
| Jurisdictions Covered | Egypt (EG), United Arab Emirates (AE) |
| Last Verified | July 2026 |
| Key Note | New treaty fundamentally changes dividend treatment (0% → 5%/10%), capital gains (residence → source state), and adds PPT. Interest remains 10%. UAE has 0% domestic WHT — treaty rates bind Egypt as source state only. |

----------|---------------------|-----------------------|----------------------|---------------------|----------------|-------|
| Dividends — portfolio | 10% | 0% (no WHT) | 10% (unlisted) / 5% (listed) | 0% | Art 10 | Source state may tax for the first time under new TT |
| Dividends — substantial (≥10% voting stock, 365-day holding) | 5% | 0% (no WHT) | 10% (unlisted) / 5% (listed) | 0% | Art 10 | 365-day holding period requirement (ending on dividend distribution date); branch profit tax ≤5% |
| Interest | 10% | 10% | 20% | 0% | Art 11 | Same rate under old and new treaty; government exemption removed from new TT |
| Royalties — copyright/know-how/patents | 10% | 10% | 20% | 0% | Art 12 | Same rate; varies by category |
| Royalties — film & TV | 15% | 10% | 20% | 0% | Art 12 | Increased from 10% to 15% under new TT |
| Technical services | Under Art 7 (business profits) | Under Art 7 | 20% | 0% | Art 7 | No separate FTS article; taxable only if PE in source state |
| Capital gains — immovable property | Source state | Source state | 22.5% | N/A | Art 13(1) | Source state may tax |
| Capital gains — PE assets | Source state | Source state | 22.5% | N/A | Art 13(2) | Source state may tax |
| Capital gains — shares | Source state | Residence state | 22.5% | N/A | Art 13 | **Major change:** source state may now tax gains from share transfers (unless immovable property exception) |
| Pensions — private | 0% (residence state only) | 0% (residence state only) | Progressive | N/A | Art 18 | Taxable only in residence state |
| Social security | 0% | 0% | N/A | N/A | Art 19 | Government benefits exempt |
| Directors' fees | Source state | Source state | Progressive | N/A | Art 16 | Source state (company's state) may tax |
| Employment income | Residence state (with 183-day exception) | Same | Progressive | 0% | Art 15 | Source state may tax if 183-day test met |

---

## Article-by-Article Summary

### Article 2: Taxes Covered

- **Egypt:** Individual income tax (wages, commercial/industrial, professional, real estate), corporate income tax, withholding tax, additional percentage taxes
- **UAE:** Corporate tax (Federal Decree-Law No. 47 of 2022, 9% from June 2023). UAE does not levy personal income tax. The treaty covers corporate tax but UAE's 0% personal income tax regime means the treaty is primarily relevant for corporate cross-border flows and WHT relief on Egyptian-source payments.
- Note: The old 2002 treaty predated UAE corporate tax; the new treaty explicitly covers the UAE CT regime.

### Article 4: Resident — Tie-Breaker Rules

A dual-resident individual's status is determined in sequence:
1. **Permanent home** — state where permanent home is available
2. **Centre of vital interests** — if permanent home in both states, state with closer personal/economic relations
3. **Habitual abode** — if centre of vital interests cannot be determined or no permanent home in either state
4. **Nationality** — if habitual abode in both or neither state
5. **Mutual agreement** — competent authorities settle if national of both or neither

For companies, the primary tie-breaker is the place of effective management. This is particularly relevant for UAE free zone entities that may have management in Egypt — the competent authorities will determine residence based on where board decisions are effectively made.

### Article 5: Permanent Establishment (PE)

The new treaty modernizes the PE definition with BEPS-aligned provisions:

- **Service PE:** Furnishing of services may give rise to a PE if certain conditions are met (specific provision added)
- **Dependent agent:** New definition tackles commissionaire arrangements and similar strategies (aligned with MLI Article 12)
- **Anti-avoidance for specific activity exemptions:** Anti-fragmentation rule prevents splitting activities to avoid PE status
- **Insurance companies:** Special PE provision for insurance enterprises

**Closely related enterprise:** An enterprise is closely related to another if one controls the other or both are under the same control. Control = owning directly/indirectly at least **50%** of beneficial interest. Protocol: states shall exchange information to identify closely related persons.

### Article 6: Income from Immovable Property

Source state may tax income from immovable property (including agriculture/forestry). Ships and aircraft are excluded. Applies to direct use, letting, and other use forms. Also applies to income from immovable property used for business or independent personal services.

### Article 7: Business Profits

- No taxation in source country unless non-resident carries on business through PE
- New rules on profit attribution to PEs (aligned with OECD Authorized OECD Approach)
- Profits attributable to PE are taxable in source state; balance is taxable only in residence state

### Article 8: Shipping and Air Transport

Taxable only in state of effective management. If management aboard a ship, state of home harbor or operator's residence. This is significant for UAE-based shipping lines and airlines operating to Egyptian ports — profits from such operations are taxable only in UAE (where management is located), not in Egypt.

### Article 9: Associated Enterprises

Arm's length principle applies. Transfer pricing adjustments allowed with corresponding adjustments. If one enterprise adjusts profits based on arm's length pricing, the other state must make a corresponding adjustment. Time limit: no adjustment after 5 years from year-end (aligning with Egypt's TP decree timelines). Disputes may be resolved through MAP (Article 24/MLI Article 16).

### Article 10: Dividends — Key Changes

**Old TT:** Exclusive taxing rights to residence state (0% WHT in source state; both states restricted on branch profit tax).

**New TT:** Shared taxing rights:
- **5% WHT** if beneficial owner is a company holding ≥10% of voting stock for **365 days** including the dividend distribution date
- **10% WHT** in all other cases
- Branch profit tax allowed at up to **5%**

**Practical impact:** UAE-resident companies receiving dividends from Egyptian subsidiaries now face Egyptian WHT (previously 0%). The only relief: ≥10% holding → reduced to 5%.

### Article 11: Interest — Minor Changes

- Rate remains **10%** WHT in source state
- Government exemption removed from new treaty
- Same rate functionally for most taxpayers, but government/government-owned entities lose the previous exemption

### Article 13: Capital Gains — Key Changes

**Old TT:** Residence state had exclusive taxing rights on capital gains from share transfers (unless shares derive value from immovable property in source state).

**New TT:** **Source state can tax** gains from transfer of shares — specifically, the country where the entity whose shares are being transferred is a resident may tax the gains.

- Exception: gains from immovable property (Art 13(1) — source state taxes)
- Ships/aircraft (Art 13(3) — management state taxes)

### Article 14: Independent Personal Services

Taxable only in residence state unless:
- (a) Fixed base regularly available in source state (only income attributable to base taxed), OR
- (b) Stay in source state ≥183 days in any 12-month period (only income from activities in source state taxed)

Includes: scientific, literary, artistic, educational, teaching activities, physicians, lawyers, engineers, architects, dentists, accountants. Relevant for UAE-based consultants providing services in Egypt — without a fixed base or 183-day presence, their income is taxable only in UAE (0% personal income tax).

### Article 17: Artistes and Sportspersons

Source state may tax income of artistes, musicians, actors, sportsmen from personal activities exercised therein, even if income accrues to another person. This overrides the 183-day threshold for employment income — any performance in the source state is taxable.

### Article 15: Dependent Personal Services (Employment)

- 183-day threshold: source state may tax if employment exercised in source state ≥183 days in any 12-month period
- UAE has 0% personal income tax — UAE residents working in Egypt may trigger Egyptian taxation if the 183-day threshold is met

### Article 16: Directors' Fees

Source state (where company is resident) may tax directors' fees.

### Article 18: Pensions

- Private pension distributions: **0%** — taxable only in country of residence
- Government social security benefits: **0%** — exempt from source-country withholding

### Article 19: Government Service

- Government salaries: taxable only by paying government
- Government pensions: taxable only by paying government

### Article 21: Other Income

- New clarification for immovable property effectively connected to PE
- Items not dealt with in other articles: residence state may tax
- If connected to PE/fixed base, Articles 7/14 apply instead

### Article 20: Students and Trainees

- Maintenance/education/training payments from sources outside host state: not taxed
- Remuneration from services connected with education/training: not taxed in host state for up to 3 years

### Article 22: Methods for Elimination of Double Taxation

- **Credit method:** Egypt allows deduction for tax paid in UAE (including the 0% rate, meaning no credit) against Egyptian tax on the same income
- **UAE approach:** UAE introduced Corporate Tax (9% from June 2023). Foreign tax credits for Egyptian tax suffered may be available under UAE CT law — verify against UAE Federal Decree-Law No. 47 of 2022 provisions
- Previously (pre-2023), UAE had no income tax; the treaty operated as a one-way relief mechanism (preventing Egyptian WHT). Now that UAE has CT, the relief is more reciprocal

### Article 24: Mutual Agreement Procedure (MAP)

- Case must be presented within **3 years** from first notification (MLI modified)
- Competent authorities endeavour to resolve by mutual agreement
- Any agreement implemented notwithstanding domestic time limits
- Competent authorities may consult on interpretation/application and for cases not provided for
- No mandatory arbitration included in the treaty

### Article 25: Exchange of Information

- Information exchanged for tax assessment/collection/enforcement/prosecution/appeals
- Treated as secret, disclosed only to relevant persons/authorities
- Cannot require administrative measures at variance with domestic law/practices
- Cannot require information not obtainable under normal administration
- Cannot require disclosure of professional secret/trade process/contrary to public policy
- Information must be obtained even if not needed for requesting state's own tax purposes
- **UAE significance:** UAE FTA cooperates with ETA on cross-border tax information exchange, including for free zone entities

### Article 29: Entry into Force

- Entry into force: 19 April 2021 (entered into force)
- Applies from 1 January 2022 for all taxes covered
- WHT: applies to amounts paid on or after 1 January 2022
- Other taxes: applies to taxable years beginning on or after 1 January 2022

### Article 28: Savings Clause for Hydrocarbons

The new treaty narrows the savings clause to income/profits from the **extraction of hydrocarbons** only. National laws regarding hydrocarbon extraction taxes are unaffected by the treaty.

### Article 30: Principal Purpose Test (PPT) — NEW

The new treaty adds a **Principal Purpose Test (PPT)** (not in the old treaty):
- Treaty benefits are **denied** when obtaining benefits is the objective or one of the objectives of the arrangement or transaction
- This aligns with OECD BEPS Action 6 and MLI Article 7 standards
- Substance and beneficial ownership requirements must be met to pass the PPT

---

## Tax Residency Certificate (TRC) Requirements

### Egypt side
- **Format:** Original TRC issued by the Egyptian Tax Authority (ETA)
- **Authentication:** Legalisation (Egypt is not an Apostille Convention party)
- **Validity:** 1 year from date of issue
- **Process:** Egypt applies **pay-and-refund mechanism** under Ministerial Decree 771/2009
  - 20% domestic WHT rate withheld at source for interest and royalties
  - Non-resident recipient files refund claim with ETA for differential between domestic rate and treaty rate

### UAE side
- **Format:** Tax Residency Certificate issued by UAE Federal Tax Authority (FTA) or Ministry of Finance (MoF)
- **Validity:** Typically 1 year from date of issue
- **Process:** UAE residents apply to FTA/MoF for TRC; UAE does not withhold tax domestically (0% WHT)
- **Corporate tax:** UAE Corporate Tax Law (Federal Decree-Law No. 47 of 2022) introduced 9% CT from June 2023. TRC must confirm status under this regime. Free zone entities must confirm qualifying free zone person status.
- **Economic Substance Regulations (ESR):** UAE residents claiming treaty benefits must comply with ESR requirements; substance is increasingly linked to treaty access.

---

## Mutual Agreement Procedure (MAP)

| Field | Egypt | UAE |
|-------|-------|-----|
| Competent Authority | Ministry of Finance — Egyptian Tax Authority (ETA), Conflict Resolution Department | Ministry of Finance (MoF) — International Tax Relations |
| Time Limit | 3 years from first notification (if MLI MAP applies) | 3 years from first notification (if MLI MAP applies) |
| Arbitration | Not included (standard MAP only) | Not included (standard MAP only) |
| MLI MAP | MLI Article 16 — enhanced MAP (Egypt ratified 30 Sep 2020) | MLI Article 16 — enhanced MAP (UAE ratified 29 May 2019) |

### MAP Contact Points

- **Egypt:** Egyptian Tax Authority (ETA) — Conflict Resolution Department, Ministry of Finance, Cairo
- **UAE:** Ministry of Finance (MoF) — International Tax Relations / Tax Treaty Department

---

## Anti-Treaty-Shopping / PPT (Principal Purpose Test)

The new treaty includes a standalone **Principal Purpose Test (PPT)** (Article 30):
- Treaty benefits are **denied** when obtaining benefits is the objective or one of the objectives of the arrangement or transaction
- This is a **new provision** — the old 2002 treaty did not have a PPT
- **Substance requirements:** Both ETA and UAE FTA may examine whether the treaty claimant has genuine economic substance in the residence state
- **Free zone considerations:** UAE free zone entities must demonstrate real substance (offices, employees, genuine business activities) to pass PPT scrutiny. Letterbox companies in free zones risk benefit denial.
- **Economic Substance Regulations (ESR):** UAE ESR compliance is linked to treaty access — entities failing ESR tests may face scrutiny under PPT when claiming treaty benefits against Egypt
- **MLI application:** Both states adopted MLI Article 7 PPT, which may also apply to the treaty independently of Article 30

---

## Cross-References to Upstream Skills

- **eg-corporate-tax** — Egypt's corporate income tax (22.5%) applies to resident companies and PEs of non-residents; treaty rates reduce WHT on outbound payments
- **eg-withholding-tax** — Egypt's domestic WHT rates (dividends 5%/10%, interest 20%, royalties 20%, services 20%); treaty provides reduced rates but pay-and-refund mechanism applies
- **oecd-model-treaty-defaults** — Reference for articles not individually summarized in this corridor file
- **withholding-tax-matrix** — Cross-reference for domestic WHT rates across jurisdictions
- **cross-border-tax-router** — Entry point for multi-jurisdictional personal tax routing

---

## Pitfalls and Practical Notes

1. **New treaty dividend shock:** The new treaty fundamentally changes dividend treatment for UAE residents — from 0% to 5%/10%. UAE investors in Egyptian companies must now budget for Egyptian WHT on dividends. The 5% rate requires ≥10% voting stock held for 365 days including distribution date.

2. **Capital gains reversal:** The residence-state exemption for share gains is eliminated. Egyptian-source share disposals may now be taxed in Egypt at 22.5%. This is a major change for UAE residents holding shares in Egyptian companies. Plan share disposals carefully.

3. **Egypt pay-and-refund trap:** Egypt does NOT automatically apply reduced treaty rates for interest and royalties. Domestic 20% WHT is withheld; refund claim filed later with the ETA. Budget for cash flow timing impact of up to 12+ months for refund processing.

4. **Film & TV royalty increase:** Royalty rate for film and TV rights increased from 10% to 15% under the new treaty. Media companies should verify which royalty category applies to their specific income streams (know-how 10%, film/TV 15%).

5. **365-day holding period for 5% dividend:** The 365-day holding period must include the date of dividend distribution. If shares are acquired shortly before distribution, the 10% rate applies instead of 5%.

6. **Technical services — no FTS article:** There is no separate Fees for Technical Services (FTS) article. Non-IP technical services fall under business profits (Art 7), taxable only if PE exists in source state. This is a significant advantage over Egypt's 20% domestic WHT on service payments — but requires careful PE analysis.

7. **UAE corporate tax interaction:** UAE introduced Corporate Tax (9% from June 2023). Previously, UAE entities had no income tax, meaning treaty benefits were primarily about avoiding Egyptian WHT. Now, foreign tax credits (FTC) may be available in UAE for Egyptian tax suffered — verify UAE CT law provisions.

8. **Free zone substance:** UAE free zone entities must have genuine substance to claim treaty benefits. PPT + ESR scrutiny means that entities established in free zones for the sole purpose of obtaining treaty benefits risk denial. Verify that the free zone entity conducts core income-generating activities in the UAE.

9. **Government exemption removed:** The government/central bank exemption for interest has been removed from the new treaty. Government-owned entities that previously enjoyed 0% interest must now verify their position under the new treaty.

10. **MLI effective dates:** MLI provisions apply to WHT from dates on or after 1 January 2021 (Egypt) / dates per UAE MLI position. Check whether MLI PPT or treaty PPT applies first depending on effective dates.

---

## Worked Examples

### Example 1: Egyptian company paying dividends to UAE shareholder (post-2022 treaty)

**Facts:** An Egyptian company (EG Co) distributes EGP 10,000,000 in dividends to its UAE parent company (UAE HoldCo), which holds 15% of EG Co's voting stock. UAE HoldCo has held the shares for 400 days including the dividend distribution date.

**Analysis:**
- New treaty Article 10: 5% rate applies if beneficial owner holds ≥10% of voting stock for 365 days including distribution date
- UAE HoldCo holds 15% > 10% threshold AND 400 days > 365-day holding period → 5% rate applies
- Egyptian domestic WHT: 10% (unlisted company)
- Egypt applies treaty rate directly for dividends (unlike interest/royalties where pay-and-refund applies):
  - WHT = EGP 10,000,000 × 5% = EGP 500,000 (treaty rate used directly)
- Under the old treaty (pre-2022): 0% WHT — this is a **new cost** for UAE investors
- UAE side: UAE HoldCo receives EGP 9,500,000. UAE CT at 9% applies if taxable income aggregate exceeds AED 375,000 threshold. Foreign tax credit for Egyptian WHT may be available under UAE CT law.

### Example 2: Egyptian company paying interest to UAE bank (new treaty)

**Facts:** An Egyptian company (EG Co) pays EGP 8,000,000 in interest to a UAE commercial bank (UAE Bank, not government-owned).

**Analysis:**
- New treaty Article 11: 10% rate in source state
- Egyptian domestic WHT on interest: 20%
- Pay-and-refund mechanism applies:
  1. EG Co withholds 20% at source = EGP 1,600,000
  2. UAE Bank files refund claim with ETA for 10% differential = EGP 800,000
  3. Net WHT after refund = EGP 800,000 (10% treaty rate)
- Under the old treaty: the rate was also 10%, but government-owned banks were exempt. Under the new treaty, the government exemption is removed — UAE government-owned entities (e.g., Emirates NBD with sovereign ownership) may now face the 10% WHT where they were previously exempt.

### Example 3: UAE shareholder selling Egyptian company shares (new treaty)

**Facts:** A UAE investment company (UAE Inv) sells shares in an Egyptian listed company for EGP 50,000,000. The shares were acquired for EGP 30,000,000 (gain = EGP 20,000,000). UAE Inv is the beneficial owner and has held the shares for 2 years.

**Analysis:**
- **Old treaty:** Residence state (UAE) had exclusive taxing rights → 0% Egyptian tax on the gain
- **New treaty Article 13:** Source state (Egypt) may tax gains from alienation of shares
- Egyptian tax = EGP 20,000,000 × 22.5% (CIT rate) = EGP 4,500,000
- This is a **major change** — UAE investors must now budget for Egyptian CGT on share disposals
- UAE CT side: Foreign tax credit for EGP 4,500,000 Egyptian tax against UAE CT on the same gain
  - UAE CT = EGP 20,000,000 × 9% = EGP 1,800,000
  - Since Egyptian tax (EGP 4.5M) > UAE CT (EGP 1.8M), no additional UAE tax is due, but the excess is not refundable
  - Effective total tax rate = 22.5% (capped at Egyptian rate)

### Example 4: Film & TV royalties — split rate under new treaty

**Facts:** An Egyptian broadcasting company (EG Broadcast) pays AED 5,000,000 to a UAE media company (UAE Media) for: (a) AED 3,000,000 in software/know-how royalties, and (b) AED 2,000,000 in film & TV broadcasting rights.

**Analysis:**
- Software/know-how: Article 12 → 10% treaty rate (vs 20% domestic)
- Film & TV: Article 12 → 15% treaty rate (vs 20% domestic) — **increased from 10% under old treaty**
- Pay-and-refund:
  1. EG Broadcast withholds 20% on total = AED 1,000,000
  2. UAE Media files refund claims:
     - Software/know-how refund: AED 3,000,000 × (20% - 10%) = AED 300,000
     - Film/TV refund: AED 2,000,000 × (20% - 15%) = AED 100,000
  3. Total refund = AED 400,000
  4. Net WHT = AED 600,000 (AED 300,000 at 10% + AED 300,000 at 15%)

---

## Sources

- **Deloitte Middle East — New UAE-Egypt Tax Treaty analysis:** https://www.deloitte.com/middle-east/en/services/tax/perspectives/update-on-the-new-uae-and-egypt-tax-treaty.html
- **PwC Egypt — Withholding taxes:** https://taxsummaries.pwc.com/egypt/corporate/withholding-taxes
- **TaxInPangea — UAE-Egypt treaty:** https://www.taxinpangea.com/treaties/united-arab-emirates-egypt
- **UAE Ministry of Finance — Tax Treaties:** https://www.mof.gov.ae/en/resourcesAndBudget/Pages/TaxTreaties.aspx
- **Egypt ETA — Bilateral agreements:** https://eta.gov.eg/en/content/bilateral-agreements

**Last verified:** July 2026

> Contributed by Ahmed Hassan.

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
