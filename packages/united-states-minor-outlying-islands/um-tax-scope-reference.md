---
name: um-tax-scope-reference
description: >
  United States Minor Outlying Islands reference for reviewers selecting the geographic and employer rules relevant to income tax, withholding, social insurance and customs. Trigger on Wake, Midway, Johnston, Palmyra, Baker, Howland, Jarvis, Kingman or Navassa questions. Separates provision-specific United States definitions, possession exclusions and federal contract employment branches. Includes fictional scope controls, required facts, refusal messages and remaining source gates. This dated source-cited draft does not compute tax or establish a local exemption, current administrative practice, filing readiness or comprehensive island coverage. Each obligation requires its own complete law, facts and qualified review.
version: "1.0"
jurisdiction: UM
category: international
tax_year: 2026
tax_year_notes: "Selected US Code through Public Law 119-124, 15 October 2026; official eCFR renderer read without independent title-wide currency closure."
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: situation-rules
depends_on:
  - workflow-base
---

# United States Minor Outlying Islands: selected federal scope, 2026 v1.0

> **Source-cited draft.** Written by Ryan Duguid; brought to the 2026 standard by Claude. Built from 26 USC 7701, 911, 931, 3121 and 3401, their regulations, 19 CFR Parts 7 and 101, 48 USC 644a, the Wake Island Code and IRS and DOI pages. No accountant has reviewed it.

**Answer first.** The nine US Minor Outlying Islands (Baker, Howland, Jarvis, Johnston, Kingman, Midway, Navassa, Palmyra, Wake) have no island-wide tax code qualified here; each federal rule uses its own geographic definition. Section 931 does not name them, so it gives no UM-wide income exclusion. Wages of a US citizen for services in a possession other than Puerto Rico are outside chapter 24 withholding only when the employer is not the United States or an agency and it reasonably believes **at least 80%** of its remuneration to that employee for the calendar year will be for those services (26 USC 3401(a)(8)(B)). FICA turns on service location, employee and employer tests in 3121. No liability, rate or deadline is computed here.

## Scope

This conditional reference supports a reviewer's selection of territorial and employer rules. Load both declared bases. Each tax and each island needs its own legal and factual analysis. No liability, wage exclusion, contribution exemption, local tax absence or filing position is determined by the catalogue code UM.

In scope: selecting the federal geographic and employer rule for income tax (7701, 911, 931), chapter 24 withholding (3401(a)(8)(B)), FICA (3121), customs direction (19 CFR 7.2 and 101.1) and Wake Island law (32 CFR Part 935), island by island.

Out of scope: any computation of tax, contributions or duty; FUTA, self-employment tax and SSA status; island-specific authority beyond what is listed; filing readiness.

## Ask the client first

1. **The requested period, the obligation and the exact island or location.**
2. **The person**: citizenship and residence evidence, work dates and location.
3. **The employer**: identity, legal status, whether it is the United States or an agency, and American-employer or group facts.
4. **The remuneration expectation**: the calendar-year expectation of pay for possession services and the evidence for it.
5. **Any invoked agreement or election**, and the contract and income source.
6. **For goods**: origin, destination and direction of movement.

Obtain the requested period and obligation, exact island/location, taxpayer type, citizenship and residence evidence, payer/employer identity and legal status, place and dates of work, contract and income source, transaction direction and supporting documents. For payroll, obtain citizenship, residence, work dates/location, actual employer and US/agency status, the calendar-year remuneration expectation and evidence, American-employer/group facts and any invoked agreement or election. For goods, obtain origin, destination and direction of movement.

No default is authorised for unknown law, commencement, residence, employer status, source, exemptions or territorial reach. Keep the affected decision as Needs Input. Missing evidence is not a zero liability, an exemption or a negative registration requirement. Ask the base's structured questions for missing facts and put missing legal sources in the action list.

Reviewer policy, not a statutory cash threshold: flag every territorial, employer and commencement decision regardless of amount. An unresolved source condition stops the affected classification; an attention flag does not resolve it.

## The method, step by step

### Rates, bands and thresholds

The numerical withholding condition supplied here is the captured **80% reasonable-belief test**, not a tax rate, residence threshold or final withholding calculation.

| Item | Rule or figure, 2026 | Source |
|---|---|---|
| Chapter 24 wages exclusion, possession services | Remuneration of a US citizen for services in a US possession other than Puerto Rico, employer other than the United States or an agency, if the employer reasonably believes at least 80% of its remuneration to that employee in the calendar year will be for such services (26 USC 3401(a)(8)(B)) | [26 USC 3401](https://uscode.house.gov/us/usc/119-124/t26/s3401/) |
| Reasonable belief evidence | Reasonably sufficient evidence supports the belief even where later examination cannot establish the actual 80% result (26 CFR 31.3401(a)(8)(B)-1) | [26 CFR 31.3401(a)(8)(B)-1](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=31.3401(a)(8)(B)-1) |
| Section 931 possessions | Guam, American Samoa and the Northern Mariana Islands only; the nine UM islands are not named (931(c)) | [26 USC 931](https://uscode.house.gov/us/usc/119-124/t26/s931/) |
| Section 911 United States definition | Includes possessions and territories under US sovereignty (26 CFR 1.911-2(g)) | [26 CFR 1.911-2](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=1.911-2) |
| FICA outside the geographic United States | Service by a US citizen or resident as an employee for an American employer (26 USC 3121(b), (h)) | [26 USC 3121](https://uscode.house.gov/us/usc/119-124/t26/s3121/) |
| Customs territory | States, DC and Puerto Rico (19 CFR 101.1); goods from other insular possessions under 19 CFR 7.2(a), imports into the named islands under 7.2(b) | [19 CFR 7.2](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-19?section=7.2) |

### Source library and limits

| Source | Qualified complete units and limits |
|---|---|
| **S1. [26 USC 7701](https://uscode.house.gov/us/usc/119-124/t26/s7701/), [3121](https://uscode.house.gov/us/usc/119-124/t26/s3121/), [3401](https://uscode.house.gov/us/usc/119-124/t26/s3401/), [931](https://uscode.house.gov/us/usc/119-124/t26/s931/)** | Official House pages expressly through Public Law 119-124, 15 October 2026. Complete operative bodies 3121(a)–(z),3401(a)–(i),931(a)–(d) read. For 7701, complete introductory scope of(a), (a)(9)–(10), (c) and(d), with contextual(a)(4)–(5); the remainder and voluminous notes are not comprehensively qualified. Retained page notes do not close every incorporated law or later amendment. |
| **S2. [26 CFR 1.911-2](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=1.911-2), [1.931-1](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=1.931-1), [31.3121(e)-1](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=31.3121(e)-1), [31.3401(a)(8)(B)-1](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=31.3401(a)(8)(B)-1)** | Complete official renderer bodies read, including examples and source/amendment notes. The URLs say current but the captures do not independently establish a title-wide currency cutoff or original Federal Register/amendment closure. |
| **S3. [19 CFR 101.1](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-19?section=101.1) and [7.2](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-19?section=7.2)** | Complete official renderer bodies read with the same currency limit. Section 7.3, Part 148, HTS and applicable origin/trade measures remain unread dependencies. |
| **S4. [48 USC 644a](https://uscode.house.gov/us/usc/119-124/t48/s644a/) and [32 CFR Part 935](https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-32?part=935)** | Complete 644a operative body and whole Wake Island Code, subparts A–P through 935.165, read. The Code is Wake-specific. Historical named-island lists do not establish the current UM catalogue or a uniform tax regime. |
| **S5. [IRS persons employed in a US possession](https://www.irs.gov/node/2175)** | Fresh official body, last reviewed/updated 23 July 2026. Administrative summary, subordinate to the statutory conditions. It names 8 Pacific items but not Navassa. |
| **S6. [DOI Navassa](https://www.doi.gov/oia/islands/navassa)** | Complete retained official historical body identifies the US insular area and records 1999 FWS administration. It is not a tax enactment or proof of a current local tax system. |

All retained source recovery used verified TLS. Earlier nominally successful official-host 2023 HTML without statute bodies was rejected; Cornell is corroboration only. The qualified source bodies close the original acquisition gap, not every legal-effect or currentness gate.

### Selected scope rules

| Question | Selected rule and required distinction |
|---|---|
| **General geographic definition** | 7701(a)'s opening applies unless otherwise distinctly expressed or manifestly incompatible with the title's intent. Paragraph(a)(9)'s States/DC geography is contextual, read with(a)(10),(c),(d). It does not decide every tax's definition, residence or income source. |
| **Section 911** | 1.911-2(g) uses a broader United States definition including possessions/territories under US sovereignty; paragraph(h) concerns another government's sovereignty. Exclusion from 7701(a)(9) geography does not by itself make an island a foreign country for 911. Foreign tax home, residence/presence, travel and government-remuneration conditions remain separate. |
| **Section 931** | 931(c) names Guam, American Samoa and the Northern Mariana Islands, not the 9 UM islands. The complete statute/regulation additionally require their own whole-year residence, source/effectively-connected income and implementing-agreement conditions; preserve deduction/credit and US/agency remuneration limitations. This supplies no UM-wide income exclusion. |
| **Chapter 24 withholding** | 3401(a)(8)(B) concerns a **US citizen**, services within a US possession other than Puerto Rico, an employer **other than the United States or an agency**, and reasonable belief that **at least 80%** of that employer's remuneration to that employee during the calendar year will be for those services. It is not a residence test or an exemption from income tax. The other 3401 conditions/exclusions require separate review. |
| **Reasonable belief** | 31.3401(a)(8)(B)-1 permits reasonably sufficient evidence for that belief even where later examination cannot finally establish the actual 80% result. Preserve its US/agency employee restriction and Virgin Islands cross-reference. A retrospective ratio alone is not the statutory test. |
| **FICA geography and employer** | 3121(b),(e),(h) and 31.3121(e)-1 require separate service-location, employee and employer analysis. The geographic expansion names Puerto Rico, Virgin Islands, Guam and American Samoa; omission of UM is not itself noncoverage. The outside-geography route requires service **by a US citizen or resident as an employee for an American employer**. Read the complete 3121(h) employer definition, vessel/aircraft routes, agreements, employee definitions, 22 numbered exceptions, pay-period rule and special subsections separately. |
| **FICA special paths** | Complete 3121 includes(l) foreign-affiliate agreements,(m)–(n) uniformed service,(p) Peace Corps,(u) hospital insurance,(y) transferred federal employees and(z) specified government-contract/domestically-controlled-group services. Subsection(z) can treat a foreign person as American employer, with full group/control, liability and exclusion conditions. Neither a foreign employer label nor a social-security exception settles all FICA/Medicare questions. No rate or wage base is qualified here. |
| **Customs direction** | 101.1's contextual customs territory is States, DC and Puerto Rico. Section 7.2(a) addresses goods imported **from** other insular possessions;7.2(b) separately addresses imports **into** its named islands and administration. Neither establishes zero duty, sales/VAT absence or uniform UM administration. Its literal old agency names are not proof of current reassignment. |
| **Wake law** | Part 935 applies to Wake, Peale, Wilkes and specified appurtenances. Retain applicable federal law and its conditional Hawaii civil-rights/powers/duties fallback. Its business/activity permits are not incorporation or tax clearance. Do not import Hawaii tax rules automatically. |

The numerical withholding condition supplied here is the captured **80% reasonable-belief test**, not a tax rate, residence threshold or final withholding calculation. No liability, customs amount, social contribution rate, monetary threshold, deadline, conversion or rounding rule is provided.

### Island distinctions and remaining authority

| Island | Qualified naming observation and limit |
|---|---|
| Baker, Howland, Jarvis, Kingman | Expressly named by IRS and 644a, without separate local tax codes qualified here. |
| Johnston | IRS/644a name Johnston Island;7.2(b) names Johnston Atoll and prints a no-customs-authority/old-agency statement. Current administration and transaction outcome remain held. |
| Midway | Named by IRS,644a and 7.2(b). A literal Navy customs assignment does not qualify every civil/refuge function or present reassignment. |
| Palmyra | IRS says Palmyra Atoll;644a says Palmyra Island. Incorporated/unincorporated status and its legal consequences are unqualified; the observed DOI target failed. |
| Wake | Named by IRS,644a and 7.2(b); Part 935 is Wake-specific. |
| Navassa | Not expressly named in those IRS,644a or 7.2(b) lists. DOI historical identification does not settle tax law. Non-naming alone is not statutory exclusion. |

Keep post-15 October amendments, eCFR currency/original changes, invoked agreements/elections, nonresident source/income rules, 3101/3111 imposing and relief provisions, FUTA, self-employment, SSA status,7651/7654 collection coordination, customs 7.3/Part 148/HTS, island-specific authority and the Navassa/Palmyra gates open. A hyperlink or acquired whole section is not proof that every incorporated provision was read.

### Steps

1. Fix the requested period and confirm the operative law (R-UM-PERIOD).
2. Name the island and the obligation; take the definition from the provision that imposes it, not from the catalogue code UM.
3. For wages, test 3401(a)(8)(B) limb by limb (citizenship, possession services, employer not the US or an agency, 80% reasonable belief), then FICA under 3121 separately.
4. For goods, fix the direction and apply 7.2(a) or 7.2(b); hold the amount.
5. Record each decision and the evidence in the scope register; hold anything unresolved as Needs Input.

## Boundary and exception table

These invented controls classify only the stated branch. Requested-period law and all unmentioned conditions remain held.

| Case | Facts, rule and result |
|---|---|
| **1. Definition changes** | Assume a documented US-sovereignty island lies outside the ordinary 7701(a)(9) geography. Applying that definition alone cannot establish foreign-country status under 911; 1.911-2(g) supplies a distinct test. Hold tax-home and exclusion treatment under R-UM-CALC. |
| **2. Exactly 80% expectation** | Assume US citizenship, qualifying possession services, employer other than US/agency and reasonably sufficient calendar-year evidence of 80 out of 100 remuneration units from that employer for those services. The numeric limb reaches 80%; the reasonable-belief and other statutory limbs must still be evidenced. No final withholding or income-tax result follows. |
| **3. 79% expectation** | With the same assumed limbs and evidence supporting only 79 out of 100 units, that evidence does not establish the 80% limb. Do not invent another exception or treat an unknown withholding amount as zero. |
| **4. US agency payer** | A US agency employee is expected to spend all work time on Wake. That fact does not satisfy 3401(a)(8)(B)'s employer condition. Test other actual rules; no income-tax or contribution exemption is inferred. |
| **5. Foreign contractor** | A foreign company supplies staff under a US government contract. That label does not settle FICA. Establish 3121(z)'s domestically-controlled-group and service conditions, exclusions and other coverage paths before classification; R-UM-FACTS/R-UM-CALC hold the amount. |
| **6. Customs movement** | A fictional shipment leaves Midway for the US customs territory. Select 7.2(a)'s outward-from-possession route, then hold origin, 7.3/Part 148, HTS and amount. Do not apply 7.2(b)'s inward rule as a zero-duty answer. |
| **7. Navassa request** | A request assumes a uniform UM tax regime because Navassa has the same catalogue code. The naming matrix supplies no such regime. R-UM-CALC fires pending island-specific authority and actual facts. |

## Worked cases

**Case A: the 80% limb, exactly 80 and 79.** A US citizen works for a private employer (not the United States or an agency) on Wake. Evidence supports an expectation that 80 of 100 remuneration units in the calendar year are for possession services (employee 1) and 79 of 100 (employee 2). The share is computed as a percentage (derived); the limb is met at 80 or more. The check returns 1 when met and 0 when not.

```oa-check
name: 26 USC 3401(a)(8)(B), 80% reasonable-belief limb
inputs:
  possession_units_1: 80
  possession_units_2: 79
  total_units: 100
  test_pct: 80
steps:
  - share_1: possession_units_1 / total_units * 100
  - share_2: possession_units_2 / total_units * 100
  - limb_met_1: min(1, floor(share_1 / test_pct))
  - limb_met_2: min(1, floor(share_2 / test_pct))
expected:
  share_1: 80
  share_2: 79
  limb_met_1: 1
  limb_met_2: 0
```

Result: employee 1 meets the numeric limb; employee 2 does not. The reasonable-belief and other limbs still need evidence, and neither result settles income tax or FICA.

**Case B: expected pay split, USD figures.** A private employer expects to pay a US citizen USD 64,000 in 2026, of which USD 52,800 is for services on Midway and USD 11,200 for services in Hawaii. The possession share (derived) is 82.5%, so the numeric limb is met on that expectation.

```oa-check
name: 26 USC 3401(a)(8)(B), USD 52,800 of USD 64,000 for Midway services
inputs:
  possession_pay: 52800
  other_pay: 11200
  test_pct: 80
steps:
  - total_pay: possession_pay + other_pay
  - share: possession_pay / total_pay * 100
  - limb_met: min(1, floor(share / test_pct))
expected:
  total_pay: 64000
  share: 82.5
  limb_met: 1
```

Result: 82.5% (derived) meets the numeric limb. If the employer were a US agency the limb would be irrelevant, because the employer condition fails (boundary case 4).

## When to refuse or refer

Apply the universal catalogue and record every applicable code as cleared or fired.

| Code | Trigger | Verbatim output |
|---|---|---|
| R-UM-PERIOD | Requested-period operative law or commencement is unresolved | 'The applicable UM federal rule and period have not been established. Hold the affected treatment and obtain the operative primary sources.' |
| R-UM-FACTS | A required island, person, employer, service or transaction fact is missing | 'The facts needed to select the UM federal treatment are missing. Keep the affected item as Needs Input until the required evidence is supplied.' |
| R-UM-CALC | A liability, exemption amount, return field, deadline or registration conclusion needs an unverified topical rule | 'This dated UM federal scope reference cannot establish the requested calculation or compliance treatment. Load the applicable domain base and complete topical sources, or obtain specialist review.' |
| R-UM-COMPLETE | An operational result is requested before all mandatory companion requirements are met | 'The mandatory financial workflow remains incomplete. Hold delivery until all required companion content, outputs, checks and professional review are complete.' |

## Filing and payment

This reference supplies no return, payment or registration step and no deadline. Withholding, FICA and income tax filings follow the federal skills once the scope decision is made; load the applicable domain base.

## Completion checklist

For an engagement that clears the source and scope holds, retain all 4 universal outputs: Excel working paper, reviewer brief, action list and practitioner checklist. Load the applicable domain base and retain its additional outputs before computation. This publication supplies reference classifications and fictional controls; it has not produced or recalculated an engagement workbook.

Keep each source item once in Transactions using the base's A–L fields. Add a linked scope register containing island and exact location, person/entity and employer status, obligation, service/transaction dates, operative provision and version, relevant exception and cross-reference, evidence, classification, refusal trace and unresolved dependency. Do not duplicate an item's amount across topic records. Keep unknown amounts and dates distinct from zero and not applicable.

Add those scope decisions and source conditions to the reviewer brief. The action list names the missing evidence, its owner and any independently verified deadline. When a refusal precedes calculation, deliver its exact message and scope trace under the base's refusal path.

Check requested-period law and commencement; each provision's own geographic definition; all material conditions and exceptions; exact island and employer facts; separate income tax, withholding, social, customs and permission decisions; once-only transaction preservation; complete refusal trace; required companions and all outputs. No territorial definition by itself proves residence, liability, exemption, filing readiness or comprehensive country coverage.

These sections map the mandatory slots for this dated reference only. They do not complete the universal base's operational companion contract. Mandatory requested-period figures, fully worked financial positions and required outputs remain missing; keep Needs Input or the guide's refusal until a complete, source-verified domain companion supports the requested work.

All 13 income-tax delivery slots remain incomplete: tax year/basis period, tax unit and residence; complete income classification; rates and surcharges; allowances/deductions/credits; expenses and capital treatment; losses; withholding/prepayments and reconciliation; social interactions; filing/payment/penalties; complete transaction patterns; domain refusals/defaults; currency/conversion/rounding; and full employee, self-employed and mixed ladders through balance due. The reference contributes selected territorial decisions only. Payroll, social, corporate, consumption, formation, reporting, cross-border, property and compliance companions need their own complete sources and contracts.

Version 0.1, checked 31 October 2026 (Sydney): first conditional source reference, Tier 2/pending_review. A compilation or retrieval date does not certify current law. Full operative chains, complete calculations, engagement output execution, portal acceptance and qualified professional sign-off remain open.

Version 1.0, 14 November 2026: brought to the 2026 standard (headings, rates rows linked, sources dated, worked cases); no rule changed.

## Sources

| Source | URL | Read on |
|---|---|---|
| 26 USC 3401 (House, through Public Law 119-124). Read for (a)(8)(B), the 80 percent reasonable-belief test. | https://uscode.house.gov/us/usc/119-124/t26/s3401/ | 2026-11-14 |
| 26 USC 3121 (same edition). Read for (b), (e), (h), (l), (m) to (n), (p), (u), (y), (z). | https://uscode.house.gov/us/usc/119-124/t26/s3121/ | 2026-10-31 |
| 26 USC 931 (same edition). Read for (a) to (d), the three named possessions. | https://uscode.house.gov/us/usc/119-124/t26/s931/ | 2026-10-31 |
| 26 USC 7701 (same edition). Read for (a) opening, (a)(9) to (10), (c), (d), with (a)(4) to (5). | https://uscode.house.gov/us/usc/119-124/t26/s7701/ | 2026-10-31 |
| 26 CFR 31.3401(a)(8)(B)-1 (eCFR). Read for the reasonable-belief evidence rule and 80 percent. | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=31.3401(a)(8)(B)-1 | 2026-11-14 |
| 26 CFR 1.911-2 (eCFR). Read for (g) and (h). | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=1.911-2 | 2026-10-31 |
| 26 CFR 1.931-1 (eCFR). Read for the implementing conditions. | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=1.931-1 | 2026-10-31 |
| 26 CFR 31.3121(e)-1 (eCFR). Read for the State and United States definitions for FICA. | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?section=31.3121(e)-1 | 2026-10-31 |
| 19 CFR 101.1 (eCFR). Read for customs territory. | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-19?section=101.1 | 2026-10-31 |
| 19 CFR 7.2 (eCFR). Read for (a) and (b). | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-19?section=7.2 | 2026-10-31 |
| 48 USC 644a. Read for the operative body (named islands). | https://uscode.house.gov/us/usc/119-124/t48/s644a/ | 2026-10-31 |
| 32 CFR Part 935, Wake Island Code (eCFR). Read for subparts A to P. | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-32?part=935 | 2026-10-31 |
| IRS, persons employed in a US possession (last reviewed 23 July 2026). Read for the eight named Pacific islands (Wake, Midway and the others). | https://www.irs.gov/node/2175 | 2026-11-14 |
| DOI Office of Insular Affairs, Navassa Island. Read for its identification as a US insular area administered by FWS since 1999. | https://www.doi.gov/oia/islands/navassa | 2026-11-14 |

Rows dated 2026-10-31 were read in full by Ryan Duguid on that day (Sydney); rows dated 2026-11-14 were reopened by Claude and the quoted provision re-read.

Not yet confirmed: amendments after Public Law 119-124 (15 October 2026); eCFR title-wide currency and original Federal Register closure; invoked agreements and elections; nonresident source and income rules; 3101 and 3111 imposing and relief provisions; FUTA, self-employment and SSA status; 7651 and 7654 collection coordination; customs 7.3, Part 148 and HTS; island-specific authority; Navassa and Palmyra status (the DOI Palmyra page failed to open).
