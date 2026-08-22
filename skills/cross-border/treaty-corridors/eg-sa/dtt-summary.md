---
name: eg-sa-dtt-corridor
description: >
  Use this skill whenever asked about the Egypt-Saudi Arabia Double Tax Treaty
  — for residents/companies with cross-border flows between the two jurisdictions.
  Trigger on "Egypt Saudi tax treaty", "DTT Egypt KSA", "ضريبة الازدواج مصر السعودية",
  "cross-border Egypt Saudi", "Egypt Saudi Arabia withholding". ALWAYS read this skill
  before applying treaty rates.
version: 1.0
jurisdiction: EG-SA
tax_year: 2025
last_updated: 2026-08-02
review_status: pending_review
depends_on:
  - eg-corporate-tax
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt ↔ Saudi Arabia Double Tax Treaty (DTT) Summary

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Quick Reference

| Field | Value |
|-------|-------|
| Treaty Name | Agreement between the Arab Republic of Egypt and the Kingdom of Saudi Arabia for the Avoidance of Double Taxation and the Prevention of Fiscal Evasion with Respect to Taxes on Income |
| Signed | 8 April 2016 (Cairo) |
| Published | Official Gazette No. 35, 5 September 2017 |
| In Force | Entry into force per Article 28: first day of the second month following exchange of ratification notifications |
| Current Version | 2016 Agreement (replaced any prior arrangement) |
| MLI Status | Both parties ratified — Egypt deposited 30 Sep 2020 (in force 1 Jan 2021), KSA deposited 23 Jan 2020 (in force 1 May 2020). MLI modifications effective for WHT from 1 Jan 2021, other taxes from 1 Jul 2021 |
| Jurisdictions Covered | Egypt (EG), Kingdom of Saudi Arabia (SA) |
| Last Verified | July 2026 |
| Key Note | Dividends 5%/10%, interest 10% (govt exempt), royalties 10% (govt exempt). MLI PPT replaces original main-purpose test. Saudi domestic WHT matches treaty rates for most items. |

----------|------------|----------------|----------------------|---------------------|-------|
| Dividends — portfolio | 10% | Art 10(2)(b) | 10% (unlisted) / 5% (listed) | 5% | Standard rate for non-substantial holdings |
| Dividends — substantial (≥20% capital) | 5% | Art 10(2)(a) | 10% (unlisted) / 5% (listed) | 5% | Beneficial owner must hold directly ≥20% of capital |
| Interest | 10% | Art 11(2) | 20% | 5% | Government of other state exempt (Art 11(3)) |
| Royalties | 10% | Art 12(2) | 20% | 15% | Government of other state exempt (Art 12(3)); definition includes technical assistance |
| Technical services | 10% (under royalties) | Art 12 | 20% | 15% | Technical assistance related to IP rights included in royalties definition (Art 12(4)); no separate FTS article — falls under business profits (Art 7) if not IP-related |
| Capital gains — immovable property | Source state | Art 13(1) | 22.5% | N/A (no CGT on immovable) | Source state may tax gains on immovable property |
| Capital gains — PE assets | Source state | Art 13(2) | 22.5% | 20% | Source state may tax gains on PE business assets |
| Capital gains — ships/aircraft | Management state | Art 13(3) | 22.5% | 20% | Only state of effective management may tax |
| Capital gains — shares | Source state | Art 13(4) | 22.5% | 20% | Source state may tax gains from alienation of shares; government of other state exempt (Art 13(5)) |
| Capital gains — other | Residence state only | Art 13(6) | 22.5% | 20% | Only residence state of alienator may tax |
| Pensions | Residence state only | Art 18 | Progressive | N/A | Taxable only in residence state |
| Directors' fees | Source state | Art 16 | Progressive | N/A | Source state (company's state) may tax |
| Employment income | Residence state (with 183-day exception) | Art 15 | Progressive | Progressive | Source state may tax if 183-day test met, employer is resident of source state, or remuneration borne by PE in source state |

---

## Article-by-Article Summary

### Article 2: Taxes Covered

- **Egypt:** Individual income tax (wages, commercial/industrial, professional, real estate), corporate income tax, withholding tax, additional percentage taxes
- **Saudi Arabia:** Zakat, income tax (including natural gas investment tax)
- The agreement follows the OECD Model Convention framework
- Note: Zakat applies to Saudi nationals/GCC persons; income tax applies to non-GCC persons

### Article 4: Resident — Tie-Breaker Rules

A dual-resident individual's status is determined in sequence:
1. **Permanent home** — state where permanent home is available
2. **Centre of vital interests** — if permanent home in both states, state with closer personal/economic relations
3. **Habitual abode** — if centre of vital interests cannot be determined or no permanent home in either state
4. **Nationality** — if habitual abode in both or neither state
5. **Mutual agreement** — competent authorities settle if national of both or neither

Protocol item 1 extends "resident" to include legal persons organized under a Contracting State's laws and generally exempt from tax (religious, charitable, educational, scientific, pension-providing entities).

### Article 5: Permanent Establishment

- Fixed place of business (place of management, branch, office, factory, workshop, mine/quarry, sale point)
- Construction/building site: 6-month threshold (MLI adds anti-fragmentation — closely related enterprise periods >30 days are aggregated)
- Service PE: furnishing of services may constitute PE
- MLI modifies dependent agent definition (anti-commissionaire arrangements)
- Insurance enterprise collecting premiums = deemed PE
- Protocol: includes farms/plantations; equipment for natural resource exploration constitutes PE

### Article 6: Income from Immovable Property

Source state may tax income from immovable property (including agriculture/forestry). Ships and aircraft are excluded. Applies to direct use, letting, and other use forms. Also applies to income from immovable property used for business or independent personal services.

### Article 7: Business Profits

Profits taxable only in residence state unless PE in source state. Only profits attributable to PE may be taxed in source state. Standard OECD profit attribution rules apply. Protocol item 3: export profits not subject to tax in other state.

### Article 8: Shipping, Air and Road Transport

Taxable only in state of effective management. If management aboard a ship, state of home harbor or operator's residence. Pools/joint businesses: profits allocated proportionally.

### Article 9: Associated Enterprises

Arm's length principle applies. Transfer pricing adjustments allowed with corresponding adjustments. Time limit: no adjustment after 5 years from year-end. Paragraph 2 (corresponding adjustments) does not apply in cases of tax evasion.

### Article 10: Dividends

- Rate: **5%** if beneficial owner is a company (not partnership) holding directly ≥20% of capital
- Rate: **10%** in all other cases
- Beneficial ownership requirement
- Government exemption applies (see Article 10(3) also references Article 13(5))
- Article 10(6): source state cannot tax dividends paid to residents of other state, except where paid to a resident of source state or effectively connected to PE

### Article 11: Interest

- Rate: **10%** of gross amount
- **Government exemption:** Interest paid to the government of the other Contracting State is exempt from source-state tax (Art 11(3))
- Definition includes: government securities, bonds, debentures, premiums, prizes; penalty/late payment charges excluded
- Protocol item 4 defines "Government" to include: for KSA — SAMA, Public Pension Agency, GOSI, wholly government-owned entities; for Egypt — Central Bank of Egypt, Social Insurance Fund, wholly government-owned entities
- Protocol item 5: interest definition includes services for arranging/managing loans or guarantees related to loans

### Article 12: Royalties

- Rate: **10%** of gross amount
- **Government exemption:** Royalties paid to government of other state are exempt (Art 12(3))
- Definition includes: copyright (artistic, literary, scientific), cinematography films, radio/TV tapes, patents, trademarks, designs, models, computer software, processes, secret formulas, industrial/commercial/scientific equipment use, industrial/commercial/scientific experience (know-how), and **technical assistance related to these rights**
- No separate "Fees for Technical Services" (FTS) article — technical services fall under Art 7 (business profits) unless IP-related

### Article 13: Capital Gains

1. **Immovable property** (Art 13(1)): Source state may tax
2. **PE business assets** (Art 13(2)): Source state may tax (including gains from alienation of PE/fixed base itself)
3. **Ships/aircraft/road vehicles** (Art 13(3)): Only state of effective management may tax
4. **Shares** (Art 13(4)): Source state may tax gains from alienation of shares and financial instruments/options related to such shares
5. **Government exemption** (Art 13(5)): Gains are exempt if paid to government of other Contracting State
6. **Other property** (Art 13(6)): Only residence state of alienator may tax

### Article 14: Independent Personal Services

Taxable only in residence state unless:
- (a) Fixed base regularly available in source state (only income attributable to base taxed), OR
- (b) Stay in source state ≥183 days in any 12-month period (only income from activities in source state taxed)

Includes: scientific, literary, artistic, educational, teaching activities, physicians, lawyers, engineers, architects, dentists, accountants.

### Article 15: Dependent Personal Services (Employment)

Taxable only in residence state UNLESS:
- Employment exercised in source state, AND
- Recipient present in source state ≥183 days in any 12-month period, AND
- Remuneration paid by employer who is not resident of source state, AND
- Remuneration not borne by PE in source state

If all conditions met → source state may tax. Otherwise residence state only.

### Article 16: Directors' Fees

Source state (where company is resident) may tax directors' fees and similar board payments.

### Article 17: Artistes and Sportspersons

Source state may tax income of artistes, musicians, actors, sportsmen from personal activities exercised therein, even if income accrues to another person.

### Article 18: Pensions and Annuities

- Pensions and similar remuneration for past employment: **taxable only in residence state**
- Annuities: defined as stated sum payable periodically during life or specified period, under obligation for adequate/full consideration

### Article 19: Government Service

- Salaries/wages from government service: taxable only by paying government
- Exception: if services rendered in other state and individual is resident/national of that other state
- Pensions from government service: taxable only by paying government
- Articles 15–18 apply to government business services

### Article 20: Students and Trainees

- Maintenance/education/training payments from sources outside host state: not taxed
- Remuneration from services connected with education/training: not taxed in host state for up to 3 years

### Article 21: Teachers and Researchers

- Teaching/research payments: not taxed in host state for up to 3 years
- Exception: research for private benefit of specific person

### Article 22: Other Income

Items not dealt with in other articles:
- Residence state may tax
- Source state may also tax (Art 22(3))
- If connected to PE/fixed base, Articles 7/14 apply instead

### Article 23: Methods for Elimination of Double Taxation

- **Credit method:** Resident state allows deduction for tax paid in other state
- Deduction limited to portion of tax attributable to income taxed in other state
- Protocol item 6: KSA elimination method does not prejudice Zakat collection for Saudi nationals
- Protocol item 7: Non-discrimination article applies only if KSA includes it in a treaty with a non-GCC country in the future

### Article 24: Mutual Agreement Procedure (MAP)

- Case must be presented within **3 years** from first notification (MLI modified)
- Competent authorities endeavour to resolve by mutual agreement
- Any agreement implemented notwithstanding domestic time limits
- Competent authorities may consult on interpretation/application and for cases not provided for

### Article 25: Exchange of Information

- Information exchanged for tax assessment/collection/enforcement/prosecution/appeals
- Treated as secret, disclosed only to relevant persons/authorities
- Cannot require administrative measures at variance with domestic law/practices
- Cannot require information not obtainable under normal administration
- Cannot require disclosure of professional secret/trade process/contrary to public policy
- Information must be obtained even if not needed for requesting state's own tax purposes

### Article 27: Anti-Avoidance (MLI PPT)

The original main-purpose test has been **replaced by the MLI Principal Purpose Test (PPT)** per Article 7 of the MLI:
- Treaty benefits denied if it is reasonable to conclude that obtaining the benefit was one of the principal purposes of the arrangement/transaction
- Benefits granted if it is established that granting them would be in accordance with the object and purpose of the relevant treaty provisions

### Article 28: Entry into Force

- Entry into force: first day of second month following exchange of ratification notifications
- WHT: applies to amounts paid on or after 1 January next following entry into force
- Other taxes: applies to taxable years beginning on or after 1 January next following entry into force

### Article 29: Termination

Either state may terminate by written notice through diplomatic channels on or before 30 June of any calendar year, from the fifth year following entry into force. Termination takes effect for WHT from end of calendar year, other taxes from taxable years beginning after end of that calendar year.

---

## Tax Residency Certificate (TRC) Requirements

### Egypt side
- **Format:** Original TRC issued by the Egyptian Tax Authority (ETA)
- **Authentication:** Legalisation (not apostille — Egypt is not an Apostille Convention party for most purposes; verify current status)
- **Validity:** 1 year from date of issue
- **Process:** Egypt applies **pay-and-refund mechanism** under Ministerial Decree 771/2009
  - The 20% domestic WHT rate is withheld at source
  - The non-resident recipient files a refund claim with the ETA special unit for interest/royalty WHT refunds
  - Controversial whether the decree was effectively abolished by 2015 amendments to executive regulations of Income Tax Law No. 91/2005
  - **Practical guidance:** Practically, the ETA still applies the pay-and-refund mechanism. Resident companies should continue to deduct 20% WHT and the non-resident party should claim the refund. Maintain beneficial ownership and TRC documentation at all times for audit defense.

### Saudi Arabia side
- **Format:** Tax Residency Certificate issued by ZATCA (Zakat, Tax and Customs Authority)
- **Validity:** Typically 1 year from date of issue
- **Process:** ZATCA offers a choice:
  1. **Automatic treaty application** — apply reduced rate at time of payment via monthly WHT returns, submit TRC with request form, taxpayer bears full responsibility for understatement including penalties
  2. **Refund procedure** — withhold domestic rate, file refund claim later
- **Conditions:** Report full details of each payment to non-resident, file DTT request form with TRC

---

## Mutual Agreement Procedure (MAP)

| Field | Egypt | Saudi Arabia |
|-------|-------|-------------|
| Competent Authority | Ministry of Finance — Egyptian Tax Authority (ETA), Conflict Resolution Department | Ministry of Finance — ZATCA (Zakat, Tax and Customs Authority) |
| Time Limit | 3 years from first notification of action | 3 years from first notification (same per treaty) |
| Arbitration | Not included (standard MAP only) | Not included (standard MAP only) |
| MLI MAP | MLI Article 16 applies — enhancements to MAP procedure | MLI Article 16 applies — enhancements to MAP procedure |
| Effective Date (MLI MAP) | Cases presented on or after 1 January 2021 | Cases presented on or after 1 January 2021 |

### MAP Contact Points

- **Egypt:** Egyptian Tax Authority (ETA) — Conflict Resolution Department, Ministry of Finance, Cairo
- **Saudi Arabia:** ZATCA — International Tax/Treaty Department, Riyadh

---

## Anti-Treaty-Shopping / PPT (Principal Purpose Test)

The original Article 27 (main-purpose test) has been **replaced by the MLI Article 7 Principal Purpose Test (PPT)**:
- Treaty benefits are **denied** if it is reasonable to conclude, having regard to all relevant facts and circumstances, that obtaining the benefit was one of the principal purposes of the arrangement or transaction
- Benefits are **granted** if it is established that granting them in these circumstances would be in accordance with the object and purpose of the relevant treaty provisions
- This is a broader test than the original main-purpose clause and aligns with OECD BEPS Action 6 standards
- **Substance requirements:** Both authorities may examine whether the treaty claimant has genuine substance (offices, employees, business activities) in the residence state
- **Conduit arrangements:** Using a resident of one state to channel income to a resident of a third state for treaty benefits is likely to be caught by the PPT

---

## Cross-References to Upstream Skills

- **eg-corporate-tax** — Egypt's corporate income tax (22.5%) applies to resident companies and PEs of non-residents; treaty rates reduce WHT on outbound payments
- **eg-withholding-tax** — Egypt's domestic WHT rates (dividends 5%/10%, interest 20%, royalties 20%, services 20%); treaty provides reduced rates but pay-and-refund mechanism applies
- **sa-corporate-tax** — Saudi Arabia's income tax (20% for non-GCC, Zakat 2.5% for GCC nationals/Saudi entities); treaty rates cap WHT on outbound payments
- **oecd-model-treaty-defaults** — Reference for articles not individually summarized in this corridor file
- **withholding-tax-matrix** — Cross-reference for domestic WHT rates across jurisdictions

---

## Pitfalls and Practical Notes

1. **Egypt pay-and-refund trap:** Egypt does NOT automatically apply reduced treaty rates for interest and royalties. Domestic 20% WHT is withheld; refund claim filed later. Budget for cash flow impact. The 2015 amendment controversy leaves the decree's status unclear — practical approach: follow the pay-and-refund mechanism.

2. **Zakat vs. income tax:** Saudi nationals/GCC persons pay Zakat (2.5%), not income tax. The treaty covers both Zakat and income tax. Article 23(6) protocol: elimination method does not prejudice Zakat collection for Saudi nationals. This means Zakat is not creditable against Egyptian tax.

3. **Beneficial ownership:** Both ETA and ZATCA scrutinize whether the recipient is the true beneficial owner. Conduit companies with no substance in the residence state risk treaty denial under the PPT.

4. **TRC validity:** Ensure TRC is obtained before payment is made and covers the payment period. Expired TRCs invalidate treaty claims.

5. **MLI modifications effective dates:** MLI provisions have different effective dates for WHT (1 Jan 2021) vs. other taxes (1 Jul 2021). Check which MLI article applies to which treaty article.

6. **Construction PE threshold:** 6-month threshold for building/construction sites, but MLI anti-fragmentation means closely related enterprise activities >30 days are aggregated. Structure contracts carefully.

7. **Technical services:** No separate FTS article in this treaty. IP-related technical assistance falls under royalties (Art 12 at 10%). Non-IP technical services fall under business profits (Art 7), taxable only if PE exists in source state. This is a significant advantage over Egypt's 20% domestic WHT on service payments to non-residents.

8. **Saudi non-discrimination article:** The non-discrimination article is NOT currently in force — it applies only prospectively if KSA includes a non-discrimination article in a treaty with a non-GCC country. Verify current status if relevant.

---

## Worked Examples

### Example 1: Saudi company paying dividends to Egyptian shareholder

**Facts:** A Saudi Arabian company (SA Co) distributes SAR 1,000,000 in dividends to its Egyptian parent company (EG HoldCo), which holds 25% of SA Co's capital directly.

**Analysis:**
- Treaty Article 10(2)(a): 5% rate applies because EG HoldCo holds directly ≥20% of capital
- Saudi domestic WHT on dividends: 5% (same as treaty rate)
- WHT = SAR 1,000,000 × 5% = SAR 50,000
- Note: Saudi domestic rate already matches treaty rate — no additional relief needed

### Example 2: Egyptian company paying interest to Saudi bank

**Facts:** An Egyptian company (EG Co) pays EGP 5,000,000 in interest to a Saudi commercial bank (SA Bank, not government-owned).

**Analysis:**
- Treaty Article 11(2): 10% rate applies
- Egyptian domestic WHT on interest: 20%
- Egypt applies pay-and-refund mechanism:
  1. EG Co withholds 20% at source = EGP 1,000,000
  2. SA Bank files refund claim with ETA for differential (20% - 10% = 10%)
  3. Refund amount = EGP 500,000
- Net WHT after refund = EGP 500,000 (10% treaty rate)
- Note: If SA Bank were government-owned (SAMA, GOSI, etc.), Article 11(3) would exempt the interest entirely

### Example 3: Egyptian company paying royalties to Saudi tech company

**Facts:** An Egyptian company (EG Co) pays EGP 2,000,000 in royalties (software licence + know-how) to a Saudi tech company (SA Tech).

**Analysis:**
- Treaty Article 12(2): 10% rate applies (royalties include software licences and technical assistance related to IP)
- Egyptian domestic WHT on royalties: 20%
- Pay-and-refund:
  1. EG Co withholds 20% = EGP 400,000
  2. SA Tech files refund claim for 10% differential = EGP 200,000
  3. Net WHT after refund = EGP 200,000 (10% treaty rate)
- Saudi side: SA Tech receives EGP 1,800,000, reports as business income. If Saudi-owned, Zakat 2.5% applies (not income tax). Article 23(6) protocol: Zakat is not creditable against Egyptian tax.

### Example 4: Construction PE — 7-month project

**Facts:** A Saudi construction company (SA Build) sends a team to Egypt for a 7-month building project for EG Co.

**Analysis:**
- Article 5(3): Construction PE threshold = 6 months
- 7 months > 6 months → PE exists in Egypt
- MLI anti-fragmentation: if SA Build splits the project into two 4-month contracts with a 1-month gap, the closely related enterprise periods (>30 days) are aggregated → PE still exists
- Consequence: Article 7 — profits attributable to PE are taxable in Egypt at 22.5% CIT
- If no PE (e.g., 5 months only): profits taxable only in Saudi Arabia

---

## Sources

- **Official treaty text (synthesised with MLI):** https://www.eta.gov.eg/sites/default/files/2021-07/SAUDI.pdf
- **PwC Saudi Arabia — Withholding taxes:** https://taxsummaries.pwc.com/saudi-arabia/corporate/withholding-taxes
- **PwC Egypt — Withholding taxes:** https://taxsummaries.pwc.com/egypt/corporate/withholding-taxes
- **TaxInPangea — Egypt-Saudi Arabia treaty:** https://www.taxinpangea.com/treaties/egypt-saudi-arabia
- **ZATCA Treaty Network:** https://zatca.gov.sa/en/RulesRegulations/Taxes/Pages/TaxTreaties.aspx

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
