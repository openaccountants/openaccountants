---
name: us-gilti-fdii-beat
description: Tier 2 US federal international tax content skill for the TCJA-era provisions §951A GILTI, §250 FDII, §59A BEAT, plus surviving Subpart F. Covers tax year 2025 including the 50% §250 GILTI deduction (effective 10.5% rate for C-corps), the 37.5% FDII deduction (effective 13.125%), and the BEAT 10% rate on modified taxable income for corps with >$500M average gross receipts and >3% base erosion percentage; for tax years beginning after Dec. 31, 2025, OBBBA shifts GILTI/FDII to NCTI/FDDEI with 40% and 33.34% §250 deductions and a 10.5% BEAT rate, the §962 election for individual US shareholders of CFCs, Form 5471 / 8992 / 8993 / 8991 compliance, the §965 transition-tax final installments through 2025, and the Pillar Two GloBE non-adoption with UTPR exposure.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US GILTI FDII BEAT

## US International Tax — GILTI / FDII / BEAT (Tax Year 2025)

> Tier 2 content skill. MUST be loaded alongside `us-tax-workflow-base` v0.2+.  
> Federal only. State tax (notably California's GILTI conformity quirks) is OUT of scope here.  
> Final reviewer signoff under Circular 230 is mandatory.

## 0. Scope

### 0.1 What this skill covers

This skill provides the technical content for the three flagship TCJA international anti-deferral / outbound provisions and the related compliance ecosystem, for the **2025 tax year (returns filed in 2026)**:

1. **GILTI — §951A** — Global Intangible Low-Taxed Income inclusion at the US shareholder level for income earned through CFCs.
2. **FDII — §250(a)(1)(A)** — Foreign-Derived Intangible Income deduction available to US C-corporations earning income from foreign customers.
3. **BEAT — §59A** — Base Erosion and Anti-Abuse Tax on large US corporations making deductible payments to foreign related parties.
4. **Subpart F surviving rules — §951(a)** — pre-TCJA CFC inclusions that continue to apply on top of GILTI.
5. **§965 transition tax wind-down** — the eight-installment regime ending for most taxpayers in 2025.
6. **§962 election** — individual US shareholder corporate-rate election on Subpart F / GILTI inclusions.
7. **Pillar Two / GloBE / UTPR exposure** — coverage of the OECD framework that the US has chosen not to adopt domestically but which still affects US-parented MNEs through other jurisdictions' top-up taxes.
8. **Compliance forms** — 5471, 8992, 8993, 8991, with cross-references to 8865 / 8858 for foreign partnerships and disregarded entities.

### 0.2 What this skill does NOT cover (refer-outs)

**Refer-outs table**

| Topic | Why deferred | Refer to |
| --- | --- | --- |
| §901(j) sanctioned country FTC denial | Country list shifts; sanctions law overlay | Treasury OFAC + specialist FTC skill |
| Foreign tax credit basket mechanics beyond GILTI basket | Full §904 limitation calc is its own skill | `us-foreign-tax-credit` (not yet authored) |
| Inbound (FDAP / ECI) taxation under §871, §881, §882 | Different conceptual frame | Inbound skill (not yet authored) |
| FIRPTA §897 | Real estate-specific | FIRPTA skill |
| Treaty analysis and LOB clauses | Treaty-by-treaty | Treaty-specific skills |
| Foreign partnership reporting (Form 8865) | Distinct entity classification | Refer-out; flag for human |
| Foreign disregarded entity reporting (Form 8858) | Often paired with 5471/8865 but distinct | Refer-out |
| Transfer pricing under §482 | Standalone discipline | `us-section-482-transfer-pricing` (not yet authored) |
| Pillar Two QDMTT computations in foreign jurisdictions | Foreign law content | Defer to foreign-jurisdiction skill |
| State tax conformity (CA, NJ, etc. on GILTI/FDII) | State-by-state | State-specific skill |
| Pass-through entity (S-corp, partnership) holding CFC interest with §962 layered analysis | Complex pass-through | Flag for human reviewer |
| Hybrid mismatch rules under §245A(e) / §267A | Highly technical; case-specific | Specialist review |

### 0.3 OBBBA 2025 caveat (IMPORTANT)

The One Big Beautiful Bill Act (P.L. 119-21, enacted July 4, 2025) made selective changes to TCJA international provisions. OBBBA P.L. 119-21 enacted the post-2025 mechanics now reflected in the Code:

- OBBBA replaced the old TCJA post-2025 sunset mechanics for these regimes: GILTI becomes NCTI with a 40% §250 deduction, FDII becomes FDDEI with a 33.34% §250 deduction, and BEAT becomes a 10.5% permanent rate for tax years beginning after Dec. 31, 2025.
- OBBBA did **not** adopt Pillar Two / GloBE domestically. US remains a non-adopter.
- BEAT credit ordering under §59A(b)(1)(B) for the research credit and a portion of applicable §38 credits was made permanent; use the enacted §59A credit rules and current Form 8991 instructions.

> **Reviewer must verify all rate/effective-date claims in §§2.4, 3.4, 4.3, and 4.7 of this document against the operative version of the IRC and final Treasury regulations before relying on them for a 2025 return.**

## 1. Background — From Worldwide to Quasi-Territorial

### 1.1 Pre-TCJA system (returns through 2017)

Before the Tax Cuts and Jobs Act of 2017 (P.L. 115-97), the United States operated a **worldwide income tax system**: a US corporation was taxed on its global income at 35%, with a credit for foreign taxes paid (§901, §902 deemed-paid credit), and **deferral** of US tax on active foreign-subsidiary income until the foreign subsidiary distributed a dividend back to the US parent.

The CFC anti-deferral regime under **Subpart F** (§§951–965, original enactment 1962) cracked down on passive and easily-shiftable income — interest, dividends, royalties, certain related-party services — by treating it as a deemed dividend to the US shareholder even without an actual distribution. But active manufacturing and services income earned abroad genuinely benefited from deferral.

This produced two well-documented distortions:

1. **Lock-out effect** — US MNEs accumulated >$2.6 trillion of unrepatriated foreign earnings by 2017 because bringing the cash home triggered US tax at 35%.
2. **Inversion incentive** — US corporations had a strong incentive to re-domicile abroad to escape the worldwide net.

### 1.2 TCJA's response (effective for tax years beginning after Dec 31, 2017)

**TCJA provisions table**

| Provision | What it does |
| --- | --- |
| **§245A** Participation Exemption | 100% DRD on the foreign-source portion of dividends from 10%-owned foreign corporations (so future repatriations are US-tax-free) |
| **§965** Transition Tax | One-time tax on accumulated post-1986 foreign E&P (15.5% on liquid assets / 8% on illiquid), payable in 8 installments — cleans up the legacy lock-out |
| **§951A** GILTI | Global minimum tax on foreign intangible-return income — anti-deferral expansion |
| **§250(a)(1)(A)** GILTI deduction | 50% deduction so corporate effective rate = 10.5% pre-FTC |
| **§250(a)(1)(B)** FDII deduction | 37.5% deduction on foreign-derived income retained in a US corporation for 2018–2025 — incentive to keep IP in the US |
| **§59A** BEAT | Anti-base-erosion minimum tax on large corporations making deductible cross-border related-party payments |

### 1.2 TCJA's response (effective for tax years beginning after Dec 31, 2017)

The combination — participation exemption + GILTI + FDII + BEAT — was designed to make the system **broadly territorial** for active foreign earnings while imposing a **global minimum tax** on intangible/mobile income, and to penalize base-eroding outbound payments. **Subpart F still exists**; GILTI is layered on top.

### 1.3 Where Pillar Two fits

In 2021, the OECD/G20 Inclusive Framework agreed on a global minimum tax framework (**Pillar Two / GloBE rules**) imposing a 15% minimum effective rate on MNE groups with consolidated revenue ≥ €750 million. Pillar Two has three operative mechanisms:

- **QDMTT** — Qualified Domestic Minimum Top-up Tax (jurisdiction taxes its own low-taxed entities)
- **IIR** — Income Inclusion Rule (parent jurisdiction tops up its low-taxed subsidiaries)
- **UTPR** — Undertaxed Profits Rule (denial of deductions or equivalent tax in jurisdictions where related entities are low-taxed and not already topped up)

**The US has not adopted Pillar Two domestically.** OBBBA 2025 explicitly did not enact IIR, QDMTT, or UTPR. The US administration position is that GILTI is a sufficient global minimum tax for US-parented groups. The result: US MNEs face significant uncertainty because foreign jurisdictions may apply **UTPR** to top up US-parented group entities they consider low-taxed — even though the US-side GILTI inclusion may already be taxing the same income. See §6 below.

## 2. CFC Fundamentals and the US Shareholder Test

### 2.1 What is a Controlled Foreign Corporation?

- **Controlled Foreign Corporation (CFC)** — A foreign corporation in which US Shareholders together own (directly, indirectly, or constructively) more than 50% of the total combined voting power OR more than 50% of the total value of the stock, on any day during the taxable year of the foreign corporation. Both the vote test and the value test are alternatives — a foreign corporation is a CFC if EITHER threshold is met.  _(§957(a))_

### 2.2 What is a US Shareholder?

- **US Shareholder** — A US person who owns 10% or more of the total combined voting power of all classes of stock entitled to vote, OR 10% or more of the total value of shares of all classes of stock.  _(§951(b))_
- **TCJA change to US Shareholder test** — Pre-TCJA, only the voting-power 10% test applied. TCJA added the value-based 10% test, expanding the US Shareholder population. This matters when foreign equity structures separate voting from economic rights (preferred shares, voting trusts).
- **US person** — Includes: US citizens (regardless of residence); US lawful permanent residents (green card holders); US resident aliens under the substantial presence test; domestic partnerships; domestic corporations; domestic trusts and estates meeting the §7701(a)(30)(E) tests.  _(§957(c) and §7701(a)(30))_

### 2.3 Constructive ownership — §958

- **§958(a) — direct + indirect ownership** — Ownership that triggers Subpart F and GILTI inclusion amounts.  _(§958(a))_
- **§958(b) — constructive ownership rules** — Modified §318 family/entity attribution used to determine status (Is the foreign corp a CFC? Is this person a US Shareholder?).  _(§958(b))_
- **§958(b)(4) repeal trap — sister CFC problem** — TCJA repealed §958(b)(4), which had blocked downward attribution from foreign persons to US persons. After repeal, a foreign parent's stock in a foreign sister company can be attributed downward to a US subsidiary, making that foreign sister a CFC of the US subsidiary even though the US subsidiary owns zero direct shares in it. This is the so-called "sister CFC" problem and produces many surprise Form 5471 filings. Notice 2018-13 and Rev. Proc. 2019-40 provide limited safe harbors for "no economic ownership" situations but the trap is real.  _(Notice 2018-13; Rev. Proc. 2019-40)_

### 2.4 Why the CFC test matters for this skill

- **Subpart F (§951(a))** — US Shareholders of a CFC must include their pro-rata share of CFC Subpart F income currently.
- **GILTI (§951A)** — US Shareholders of any CFC must include their pro-rata share of the CFC's "tested income" net of QBAI exclusion.
- **Form 5471** — Categories 4 (control) and 5 (US Shareholder of CFC) attach to the CFC determination.
- **§245A DRD** — Only available to US C-corp shareholders of "specified 10%-owned foreign corporations."

If a taxpayer is **NOT** a 10% US Shareholder, GILTI and Subpart F do not apply. Reporting may still be required (Categories 1, 2, 3 on Form 5471 for officer/director/transfer events).

## 3. GILTI — §951A

### 3.1 Conceptual overview

- **GILTI computation formula** — For tax years 2018-2025, compute GILTI as net CFC tested income minus net deemed tangible income return (NDTIR): NDTIR = 10% × pro-rata QBAI minus specified interest expense. For tax years beginning after December 31, 2025, OBBBA removes the QBAI/NDTIR reduction and §951A uses net CFC tested income (NCTI) mechanics instead. Do not use the 10% QBAI routine-return reduction for post-2025 NCTI forecasts.  _([IRC §951A as amended by OBBBA P.L. 119-21](https://uscode.house.gov/view.xhtml?req=(title:26%20section:951a%20edition:prelim)))_

GILTI is a minimum tax on the intangible return of CFCs. The statute does not actually try to measure intangible income directly. Instead, it: 1. Computes the CFC's "tested income" (broadly: gross income less ECI, less Subpart F, less high-taxed exclusion items, less allocable deductions). 2. Subtracts a deemed routine return on tangible assets equal to 10% × QBAI (Qualified Business Asset Investment). 3. Treats whatever is left as the deemed "intangible" return that the US Shareholder must include in income. Note that QBAI is calculated before the 10% multiplier — the 10% is applied to the QBAI basis to produce the routine-return floor.

### 3.2 Tested income — §951A(c)(2)

**Tested income exclusions table**  _(§951A(c)(2))_

| Exclusion | Statute | Notes |
| --- | --- | --- |
| Effectively connected income (ECI) | §951A(c)(2)(A)(i)(I) | ECI is already in the US net |
| Subpart F income | §951A(c)(2)(A)(i)(II) | Already picked up under §951 — no double inclusion |
| Income excluded from FBC income / insurance income by §954(b)(4) high-tax election | §951A(c)(2)(A)(i)(III) | GILTI high-tax exception |
| Dividends from related persons (under §954(d)(3)) | §951A(c)(2)(A)(i)(IV) | Avoids cascade |
| Foreign oil and gas extraction income (FOGEI) | §951A(c)(2)(A)(i)(V) | Carve-out for natural resource sector |

- **§954(b)(4) GILTI high-tax exception** — Allows a US Shareholder to elect to exclude tested income from a CFC where the foreign effective tax rate exceeds 18.9% (90% of the 21% US corporate rate). The election is made on a "tested unit" basis annually. Important planning lever for CFCs in high-tax jurisdictions — explicit election on the timely-filed return. After exclusions, allocable deductions reduce tested income to net tested income (or a tested loss).  _(Treas. Reg. §1.951A-2(c)(7))_

### 3.3 QBAI — §951A(d)

- **Qualified Business Asset Investment (QBAI)** — For tax years 2018-2025, QBAI is the average of the aggregate adjusted bases of specified tangible property used in producing tested income, computed on a quarterly average basis under the §951A(d) rules. OBBBA removes the QBAI/NDTIR reduction from §951A for tax years beginning after December 31, 2025, so QBAI is a historical/pre-2026 GILTI input and should not reduce post-2025 NCTI.  _([IRC §951A(d) for 2018-2025; OBBBA P.L. 119-21 amendments to §951A](https://uscode.house.gov/view.xhtml?req=(title:26%20section:951a%20edition:prelim)))_
- **ADS basis requirement for QBAI** — Adjusted basis is computed under the alternative depreciation system (ADS) of §168(g) (straight-line over class life), not regular MACRS. This usually produces a higher remaining basis (slower depreciation), which increases QBAI and decreases GILTI. The election is mandatory — there is no choice between methods for QBAI purposes.  _(§168(g))_
- **Excluded from QBAI** — Land (not depreciable); Inventory; Intangibles; Property held by a partnership unless the CFC's distributive share is computed through.  _(§951A(d))_

The 10% routine return is the legislative judgment that a normal-return business should not be taxed on its first 10% pretax return on tangible asset basis. Beyond that, the income is treated as intangible-derived.

### 3.4 §250 GILTI deduction (C-corps only)

**GILTI deduction and effective rate table**  _(§250(a)(1)(B))_

| Tax year beginning | GILTI deduction % | Effective rate (21% × (1 − %)) |
| --- | --- | --- |
| 2018–2025 | **50%** | **10.5%** |
| **After 2025 (OBBBA / NCTI)** | **40%** | **12.6%** |

- **Form 8993 filing** — This deduction is taken on Form 8993 ("Section 250 Deduction for Foreign-Derived Intangible Income (FDII) and Global Intangible Low-Taxed Income (GILTI)").  _(Form 8993)_
- **Taxable income limitation** — The combined GILTI + FDII deduction cannot exceed the corporation's taxable income (computed without regard to §250 itself). If the limitation bites, the deduction is reduced pro rata between GILTI and FDII components. This commonly affects loss-year corporations and is a place where small drafting errors produce wrong returns.  _(§250(a)(2))_

### 3.5 §960(d) GILTI foreign tax credit — IMPORTANT FEATURES

- **§960(d) deemed-paid FTC** — For 2018-2025 GILTI, a domestic C-corporation US shareholder is treated under §960(d) as having paid 80% of foreign income taxes properly attributable to the GILTI inclusion. For tax years beginning after December 31, 2025, OBBBA changes the NCTI deemed-paid credit percentage to 90%. Individuals do not receive deemed-paid credits unless they make a valid §962 election.  _([IRC §960(d) as amended by OBBBA P.L. 119-21](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section960&num=0&edition=prelim))_
- **GILTI/NCTI deemed-paid FTC haircut** — For 2018-2025 GILTI, only 80% of tested foreign income taxes are creditable. For post-2025 NCTI, 90% is creditable, so the haircut falls from 20% to 10%. This changes the approximate break-even foreign tax rate for a domestic corporation from 13.125% under pre-2026 GILTI to about 14% under post-2025 NCTI.  _([IRC §960(d); IRC §250; OBBBA P.L. 119-21](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section960&num=0&edition=prelim))_
- **Separate basket** — GILTI sits in its own §904 limitation basket (the "GILTI basket"). It cannot be averaged with general-basket or passive-basket income to soak up excess credits there.  _(§904)_
- **No carryback or carryforward** — Unlike the general and passive baskets (10-year carryforward, 1-year carryback), the GILTI basket has no carrybacks and no carryforwards. Excess GILTI FTCs are permanently lost in the year they arise.  _(§904)_
- **Deemed-paid tax formula** — Pre-2026 GILTI: deemed-paid tax = inclusion percentage × tested foreign income taxes; creditable amount = 80% × deemed-paid tax. Post-2025 NCTI: creditable amount = 90% × the taxes properly attributable to NCTI under §960(d), subject to the separate FTC basket and expense-allocation limitations.  _([IRC §960(d) as amended by OBBBA P.L. 119-21](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section960&num=0&edition=prelim))_
- **§78 gross-up** — The deemed-paid tax is "grossed up" into the GILTI inclusion under §78 (so the GILTI inclusion that hits Schedule J is the inclusion plus the deemed-paid tax, before the deduction and credit).  _(§78)_
- **Break-even foreign tax rate to fully offset US tax on GILTI/NCTI** — Pre-2026 GILTI: 21% × (1 - 50%) = 10.5% US tax; 80% × foreign rate must equal 10.5%, so the rough break-even foreign rate is 13.125%. Post-2025 NCTI: 21% × (1 - 40%) = 12.6% US tax; 90% × foreign rate must equal 12.6%, so the rough break-even foreign rate is 14%. Both are before expense allocation, FTC limitation, and basket issues.  _([IRC §250; IRC §960(d); OBBBA P.L. 119-21](https://uscode.house.gov/view.xhtml?req=(title:26%20section:250%20edition:prelim)))_

### 3.6 Expense allocation against the GILTI basket (the trap)

- **Expense apportionment to GILTI basket** — Under §861-§865 rules and Treas. Reg. §1.861-8, US Shareholder expenses (notably interest expense and stewardship/R&D expense) must be apportioned between baskets. Some of these expenses get apportioned to the GILTI basket, reducing the §904 limitation in that basket.  _(Treas. Reg. §1.861-8)_

The trap: a US C-corp parent with substantial debt at the US level may find that significant interest expense is allocated to GILTI, shrinking the GILTI §904 limitation below the GILTI inclusion. The deemed-paid foreign taxes are then capped, and because there's no carryforward, the unused FTC is gone forever. Net result: a residual US tax on GILTI even when the foreign effective rate well exceeds 13.125%.

Mitigation strategies (each requires its own analysis):
- §954(b)(4) high-tax exclusion election to exclude the high-taxed tested income from GILTI altogether
- Restructuring debt to push it offshore
- §163(j) interaction
- Restructuring CFC ownership chains to align expense

### 3.7 Individual US Shareholders — the problem and the §962 election

- **No §250 deduction for individuals** — §250 is explicitly limited to "domestic corporations." Individuals do not get the 50% (or 40%) deduction.  _(§250)_
- **No §960(d) deemed-paid credit for individuals** — The deemed-paid FTC under §960 is also corporate-only.  _(§960)_
- **Ordinary rates apply to individuals** — GILTI is includible as ordinary income, subject to graduated individual rates up to 37% (plus 3.8% NIIT under §1411 in many cases).  _(§1411)_

So an individual sitting on top of a CFC in, say, Singapore (17% statutory) can face a US federal rate of 37% + 3.8% = 40.8% on GILTI, with no foreign tax credit available for the corporate-level Singapore tax — a brutal mismatch.

### 3.8 The §962 election

- **§962 election** — Allows an individual US Shareholder to elect to be taxed as if a domestic corporation on §951(a) (Subpart F) and §951A (GILTI) inclusions.  _(§962)_

**§962 election effects table**  _([IRC §962; IRC §250; IRC §960(d)](https://uscode.house.gov/view.xhtml?req=(title:26%20section:250%20edition:prelim)))_

| Without §962 | With §962 |
| --- | --- |
| 37% top rate + 3.8% NIIT | 21% corporate rate on the §951A/§951 inclusion (no individual NIIT at inclusion stage under the guide default; flag CCA 202118008 / adviser review) |
| No §250 deduction | For 2025 GILTI, 50% §250 deduction available; for post-2025 NCTI, 40% §250 deduction applies |
| No §960 deemed-paid FTC | §960(d) deemed-paid FTC available: 80% creditable for 2018-2025 GILTI; 90% for post-2025 NCTI |

- **§962 PTEP distribution catch** — Distributions from the CFC that come from §962 PTEP (previously taxed earnings and profits) are NOT tax-free under §959 to the extent of the §962 tax paid. Specifically, the actual distribution of the underlying earnings to the individual is taxable as a qualified dividend (potentially) under the regular dividend rules to the extent it exceeds the original §962 tax paid. Under Smith v. Commissioner, T.C. Memo. 2018-127 (and subsequent guidance — see Rev. Rul. 62-165 and the 2019 proposed regs), the post-§962 distribution is generally taxed as a dividend but the underlying §962 tax paid creates a basis offset for the portion previously taxed.  _(§959; Smith v. Commissioner, T.C. Memo. 2018-127; Rev. Rul. 62-165)_

The §962 election is therefore most valuable when:
- The CFC pays significant foreign income tax (so the 80% deemed-paid credit substantially offsets the 21% rate);
- The individual does not expect to take large dividend distributions in the near term;
- The CFC is in a moderately-taxed jurisdiction.

It is less valuable (or harmful) when:
- The CFC pays no foreign tax (you've still effectively paid 21% with no credit and now face dividend tax on top later);
- Distributions are imminent (double-tax stacking).

- **§962 election mechanics** — Made annually on a statement attached to the timely-filed (with extensions) return. See Treas. Reg. §1.962-2. Cannot be made on an amended return. Election applies to all CFCs of the electing individual for that year — cannot pick and choose.  _(Treas. Reg. §1.962-2)_

## 4. FDII — §250(a)(1)(A)

### 4.1 Purpose

While GILTI taxes foreign-subsidiary income, FDII gives a deduction for US-corporation income earned from foreign customers, provided the foreign customer uses the property or services for foreign use. The economic intent: equalize the after-tax outcome of holding IP in a US corporation vs. holding it in a CFC. A US C-corp that earns export income on US-held IP gets the FDII deduction; if the same IP were in a CFC, the income would be GILTI. The two deductions (§250 GILTI deduction at 50% and §250 FDII deduction at 37.5% for 2018-2025) are calibrated so the US-domestic outcome (13.125%) is slightly better than the offshore outcome (10.5% pre-FTC haircut, but with FTC limits in practice often higher).

### 4.2 Eligibility

- **FDII eligibility** — FDII is available only to domestic C-corporations. Not S-corporations. Not partnerships. Not individuals. Not RICs / REITs. A US C-corp that is itself a CFC partner or has CFC subsidiaries can still claim FDII on its own foreign-derived income.

### 4.3 The formula

- **FDII computation steps** — 2018-2025 FDII computation: Step 1, compute DEI. Step 2, compute DII = DEI - 10% × domestic QBAI. Step 3, compute FDDEI from qualifying foreign-use sales/services. Step 4, FDII = DII × (FDDEI / DEI). Step 5, §250 deduction = 37.5% × FDII. Post-2025 OBBBA computation: FDII is replaced by FDDEI; the QBAI/DII routine-return construct is removed for post-2025 years; §250 deduction = 33.34% × FDDEI, subject to the §250 taxable-income limitation.  _([IRC §250 as amended by OBBBA P.L. 119-21; Treas. Reg. §1.250(b)-1 et seq. for 2018-2025 FDII mechanics](https://uscode.house.gov/view.xhtml?req=(title:26%20section:250%20edition:prelim)))_

**Effective rate on FDII-qualifying income table**

| Tax year beginning | FDII deduction % | Effective rate |
| --- | --- | --- |
| 2018–2025 | **37.5%** | **13.125%** |
| **After 2025 (OBBBA / FDDEI)** | **33.34%** | **approximately 14%** |

> Combined §250 deduction (GILTI + FDII) is taken on **Form 8993**.

### 4.4 "Foreign use" — the documentation problem

**Foreign use scenarios table**  _(Treas. Reg. §1.250(b)-4 and §1.250(b)-5)_

| Transaction | Foreign use? | Documentation challenge |
| --- | --- | --- |
| Sale of widgets to a foreign distributor for resale abroad | Yes | Need evidence buyer is foreign person + product leaves US |
| Sale to a foreign affiliate that then sells back into US | **No** (round-tripping disqualifies) | Need to trace ultimate end-use |
| Cloud services accessed by a foreign user | Yes if the user is located abroad | IP address logs, contract recitals, billing address — see §1.250(b)-5(d) |
| Sale of intangibles (license) to a foreign licensee using IP in mixed jurisdictions | Pro-rata | Allocate by territory of use |
| Sale of digital content to a consumer | Foreign use if delivered to non-US end consumer | Subject to specific "general services" vs. "advertising" vs. "intangible" classification rules |

- **Documentation requirements** — Documentation requirements under Treas. Reg. §1.250(b)-3(d) are substantial: for B2B sales and general services to a business recipient, the taxpayer needs contemporaneous documentation establishing the foreign person status and foreign use. The regulations distinguish "small business" (≤$25M FDII gross receipts) with reduced documentation rules from larger taxpayers.  _(Treas. Reg. §1.250(b)-3(d))_

**Common failure mode:** taxpayer claims FDII based on counterparty address but lacks the §1.250(b)-3 documentation. On audit, the FDDEI is disallowed. Reviewer should confirm the documentation file exists and is contemporaneous (not assembled at filing time).

### 4.5 FDII anti-stuffing rules

- **Related-party sales look-through** — Sales to a foreign related party qualify as FDDEI only if the related party then sells to an unrelated foreign person for foreign use (look-through).  _(Treas. Reg. §1.250(b)-6)_
- **Round-tripping disqualification** — Sales of property that ultimately return to US use are disqualified.
- **Manufactured-good carve-out** — Property "manufactured, produced, grown, or extracted" must satisfy the foreign-use rules at the end of the supply chain.

### 4.6 Interaction with R&D capitalization §174

For tax years beginning after Dec 31, 2021, §174 (post-TCJA) requires capitalization and amortization of R&E expenditures (5 years domestic, 15 years foreign). The OBBBA 2025 reinstated immediate expensing for domestic R&E for tax years beginning after Dec 31, 2024 (subject to confirmation). This affects FDII because:

- §174 capitalization shifts R&E expense from a current deduction into amortization over time.
- DEI for FDII purposes is gross income less allocable deductions, so R&E that is capitalized rather than deducted increases current-year DEI and therefore current-year FDII.
- The expensing reinstatement under OBBBA may reduce current FDII for taxpayers with heavy domestic R&E.

> **Reviewer must verify the operative §174 rules for the tax year being prepared.** This is a fast-moving area.

### 4.7 FDII §250(a)(2) taxable income limitation

- **§250(a)(2) taxable income limitation for FDII** — As noted for GILTI, the combined §250 deduction (GILTI + FDII) cannot exceed taxable income (computed without §250). Excess is allocated pro rata. A loss-year US C-corp gets no §250 deduction even if it has substantial FDDEI.  _(§250(a)(2))_

## 5. BEAT — §59A

### 5.1 Purpose

BEAT is an anti-base-erosion minimum tax. It addresses the practice of large US corporations making deductible payments (interest, royalties, services fees) to foreign related parties, eroding the US tax base. BEAT effectively says: if too much of your deductible expense goes to foreign related parties, you must compute a parallel minimum tax that adds back those payments and compare against regular tax.

### 5.2 Who is subject — the gateway tests

- **Applicable taxpayer gateway tests** — A taxpayer is an "applicable taxpayer" under §59A(e) if: 1. It is a corporation other than a RIC, REIT, or S-corporation; AND 2. Its average annual gross receipts for the 3 prior tax years are at least $500 million (the "gross receipts test"); AND 3. Its base erosion percentage for the tax year is at least: 3% for most corporations, or 2% for banks and registered securities dealers (and their affiliated groups). Aggregation rules under §59A(e)(3) apply: members of a §52(a)/(b) controlled group are aggregated for the gross receipts test.  _(§59A(e); §59A(e)(3))_
- **Average annual gross receipts threshold** — $500 million USD  _(§59A(e))_
- **Base erosion percentage threshold (most corporations)** — 3%  _(§59A(e))_
- **Base erosion percentage threshold (banks/securities dealers)** — 2%  _(§59A(e))_

> Small and mid-market US corporations (<$500M average gross receipts) are categorically **outside** BEAT and need not analyze it further. Most freelance / small-business engagements never touch BEAT. This skill covers it for completeness and for any engagements that involve a US sub of a foreign-parented MNE or a large US-parented group.

### 5.3 Base erosion payments — §59A(d)

- **Base erosion payment** — Any amount paid or accrued by the taxpayer to a foreign related party that is either: 1. Allowable as a deduction (interest, royalties, services fees, rent, etc.), OR 2. A payment to acquire depreciable or amortizable property (the deduction/amortization stream is treated as base-eroding), OR 3. A premium or other consideration for reinsurance, OR 4. Certain payments to expatriated entities under §7874 (always counted regardless of foreign-related status).  _(§59A(d))_
- **Foreign related party** — A party related under §267(b)/(c) or §707(b) modified, generally requiring 25% common ownership.  _(§59A(g))_

### 5.4 Carve-outs from base erosion payments

- **COGS carve-out** — Cost of goods sold is generally not a deduction (it's a reduction in gross receipts) and is therefore excluded from base erosion payments. This is a huge carve-out for goods-import businesses.
- **Services Cost Method (SCM) exception** — Services that qualify under the SCM under Treas. Reg. §1.482-9(b) and are charged at cost (no markup) are excluded — but ONLY the cost component; any markup is a base erosion payment.  _(§59A(d)(5); Treas. Reg. §1.482-9(b))_
- **Qualified derivative payments** — Mark-to-market derivative settlements meeting the regulatory criteria.  _(§59A(h))_
- **ECI of foreign related party carve-out** — Effectively connected income (ECI) of the foreign related party, where the recipient is itself paying US tax on the income — this prevents double-taxing.
- **Withholding-subject payments carve-out** — Payments subject to full US gross-basis withholding under §1441/§1442 are excluded to the extent withholding applies.  _(§1441; §1442)_

### 5.5 Base erosion percentage

- **Base Erosion Percentage formula** — Base Erosion Percentage = Base Erosion Tax Benefits (this year) ─────────────────────────────────────────────────────────────── All deductions allowed this year + base erosion tax benefits (with various exclusions per §59A(c)(4))  _(§59A(c)(4))_
- **Applicable taxpayer trigger percentage** — If this percentage ≥ 3% (2% for banks/securities dealers), the corporation is an applicable taxpayer.

### 5.6 BEAT computation — Modified Taxable Income and the BEAT rate

- **MTI and BEAT liability formula** — Modified Taxable Income (MTI): MTI = Taxable Income + Base Erosion Tax Benefits (the deductions / depreciation attributable to base erosion payments) + Base Erosion Percentage × NOL Deduction BEAT Minimum Tax Amount: BEAT MTA = (BEAT Rate × MTI) − (Regular Tax Liability − certain credits) BEAT liability = max(0, BEAT MTA)

**BEAT rate by tax year table**

| Tax year beginning | BEAT rate |
| --- | --- |
| 2018 | 5% |
| 2019–2025 | **10%** |
| **After 2025 (OBBBA)** | **10.5%** |

- **Bank/securities dealer surcharge** — Banks and registered securities dealers are subject to a +1 percentage point on each rate above.

### 5.7 Credits — the BEAT-credit haircut

**BEAT credit treatment table**  _([IRC §59A(b)(1); Draft 2025 Instructions for Form 8991](https://www.irs.gov/pub/irs-dft/i8991--dft.pdf))_

| Item | 2019-2025 | Post-2025 OBBBA |
| --- | --- | --- |
| §41 R&D credit | Protected in the BEAT regular-tax comparison | Protected in the BEAT regular-tax comparison under OBBBA/Form 8991 instructions |
| Applicable §38 credits other than R&D | 80% protected / 20% added back, within statutory limits | 80% protected / 20% added back, within statutory limits |
| BEAT rate | 10% for tax years beginning 2019-2025 | 10.5% for tax years beginning after 2025; add 1 percentage point for bank/securities-dealer affiliated groups |

When computing "regular tax liability" in the BEAT formula, you add back certain credits — i.e., credits do not count as offsetting regular tax for BEAT purposes — which effectively reduces the "regular tax" floor and INCREASES BEAT liability.

> **OBBBA enacted update.** For tax years beginning after 2025, use the 10.5% BEAT rate and the continuing §59A credit rules for the §41 research credit and applicable §38 credits; do not apply the old full-addback sunset assumption for 2026+.

### 5.8 BEAT and NOLs

- **NOL treatment for BEAT** — NOLs that arose in tax years beginning before Jan 1, 2018 are not subject to the BEAT-percentage haircut. NOLs from 2018-forward are subject to the §59A(c)(4) treatment: the base erosion percentage of the NOL deduction is added back to taxable income in computing MTI.  _(§59A(c)(4))_

### 5.9 BEAT reporting — Form 8991

- **Form 8991 filing requirement** — BEAT is reported on Form 8991, "Tax on Base Erosion Payments of Taxpayers with Substantial Gross Receipts." Filed with the corporate return (Form 1120). Required for any corporation meeting the gateway gross-receipts test, even if base erosion percentage is below 3% / 2%, to demonstrate non-application.  _(Form 8991)_

## 6. Subpart F — The Surviving Pre-TCJA Regime

### 6.1 GILTI does NOT replace Subpart F

- **Ordering rule between Subpart F and GILTI** — Subpart F (§§951–965) continues to apply on top of GILTI. The ordering rule: Subpart F applies first, and Subpart F income is excluded from tested income for GILTI purposes (§951A(c)(2)(A)(i)(II)). So a CFC's gross income is allocated: 1. First to Subpart F categories (currently taxable to US Shareholder) 2. Second, any non-Subpart F, non-excluded income becomes tested income for GILTI 3. Routine return on QBAI is excluded; the rest is the GILTI inclusion  _(§951A(c)(2)(A)(i)(II))_

### 6.2 Subpart F income categories

**Subpart F income categories table**  _(§952)_

| Category | What it captures |
| --- | --- |
| **Foreign Personal Holding Company Income (FPHCI) §954(c)** | Dividends, interest, rents, royalties, gains on property producing passive income, certain commodity transactions, certain currency gains |
| **Foreign Base Company Sales Income (FBCSI) §954(d)** | Sales income where the CFC purchases or sells property to/from a related party AND the property is manufactured/sold outside the CFC's country of organization |
| **Foreign Base Company Services Income (FBCSvI) §954(e)** | Services performed outside the CFC's country of organization for or on behalf of a related party |
| **Insurance income §953** | Income from insuring risks located outside the CFC's country |

- **High-tax exception** — Subpart F income subject to foreign effective tax ≥ 90% of US corporate rate (i.e., ≥18.9%) can be excluded by election.  _(§954(b)(4))_
- **Same-country exception** — Certain related-party dividends, interest, rents, royalties received from a related person in the same country.  _(§954(c)(3))_
- **Active financing exception (AFE)** — Permanent exception (since PATH Act 2015) for certain qualifying banking, financing, and insurance income.  _(§954(h))_
- **De minimis threshold** — lesser of 5% of gross income or $1M  _(§954(b)(3)(A))_
- **Full inclusion rule** — If gross FBC and insurance income is more than 70% of gross income, ALL gross income is Subpart F.  _(§954(b)(3)(B))_

### 6.3 Practical interaction with GILTI

In most modern post-TCJA fact patterns, Subpart F is comparatively narrow (it never picked up active income) while GILTI is broad (catches active income above QBAI floor). Subpart F still matters because:

- It is includible at the US Shareholder's regular rate without the §250 deduction.
- The §954(b)(4) high-tax exception is operative and produces an unusual planning lever: forcing income into Subpart F and then electing out under high-tax exception may be better than letting it sit in GILTI subject to FTC haircut + no carryforward.
- For individual US Shareholders without a §962 election, both Subpart F and GILTI hit at ordinary rates — but Subpart F has a longer line of case law and developed planning patterns.

## 7. §965 Transition Tax Wind-Down

### 7.1 What §965 was

- **§965 transition tax rates** — TCJA's §965 imposed a one-time tax on accumulated post-1986 foreign E&P of "specified foreign corporations" (broadly, CFCs and 10%-owned foreign corps), measured as of Nov 2, 2017 or Dec 31, 2017 (greater). The tax was at effective rates of: 15.5% on the portion attributable to liquid assets (cash-position); 8% on the illiquid portion. Computed via a deemed §965(a) inclusion with a corresponding §965(c) deduction calibrated to those effective rates.  _(§965(a); §965(c))_

### 7.2 The 8-installment election under §965(h)

**§965(h) 8-installment schedule table**  _(§965(h))_

| Installment # | % of liability |
| --- | --- |
| 1 | 8% |
| 2 | 8% |
| 3 | 8% |
| 4 | 8% |
| 5 | 8% |
| 6 | 15% |
| 7 | 20% |
| 8 | **25%** |

For a calendar-year taxpayer who made the election with the 2017 return:
- Installment 1 was due with the 2017 return (April 2018)
- ...
- **Installment 8** is due with the 2024 return (April 2025) — i.e., the **2025 filing season** is the **final** installment for calendar-year filers.
- Fiscal-year taxpayers with non-calendar inclusion years may have a later final installment.

### 7.3 §965(i) S-corporation deferred election

- **§965(i) S-corp deferral election** — S-corporation shareholders could elect under §965(i) to defer the §965 tax until a "triggering event" (sale of S-corp interest, S-corp ceasing to be a domestic corporation, etc.). Triggering events through 2025 are a meaningful tax exposure area — sale of an S-corp interest in 2025 by a shareholder who made a §965(i) election in 2017 can crystallize a large deferred tax liability.  _(§965(i))_

### 7.4 Reporting

- **§965 reporting forms** — §965 inclusions, deductions, and installment payments are reported on Form 965 and Form 965-A/B, attached to the Form 1040 or 1120 of the US Shareholder. Final installment year filers should ensure the installment schedule reconciles with prior years' Forms 965-A and the IRS systemic records.  _(Form 965; Form 965-A/B)_

## 8. Pillar Two / GloBE / UTPR

### 8.1 Framework recap

- **Pillar Two 15% minimum tax framework** — The OECD Inclusive Framework's Pillar Two establishes a 15% minimum effective tax rate for MNE groups with consolidated revenue ≥ €750 million in at least two of the last four fiscal years.

**Pillar Two mechanisms table**

| Rule | What it does | Where it operates |
| --- | --- | --- |
| **QDMTT** — Qualified Domestic Minimum Top-up Tax | Jurisdiction taxes its own constituent entities to 15% | The low-tax jurisdiction itself |
| **IIR** — Income Inclusion Rule | Parent jurisdiction tops up its low-taxed subsidiaries | UPE (ultimate parent entity) jurisdiction |
| **UTPR** — Undertaxed Profits Rule | Backstop: denial of deductions or equivalent in jurisdictions where related entities are low-taxed and not topped up | Any jurisdiction with constituent entities |

QDMTTs and IIRs went live in many jurisdictions (EU member states, UK, South Korea, Japan, Canada, Australia, etc.) for fiscal years beginning on or after Jan 1, 2024. UTPRs went live (or are scheduled live) for fiscal years beginning on or after Jan 1, 2025 in many of those jurisdictions.

### 8.2 US position

- **US non-adoption of Pillar Two** — The United States has not adopted Pillar Two as domestic law: No QDMTT; No IIR (the US position is that GILTI is a substitute, but GILTI does not meet the OECD's "qualified IIR" tests in several technical respects — notably the per-jurisdiction blending vs. global blending issue, and the 80% FTC haircut); No UTPR. OBBBA 2025 did not change this. The administration position (as of mid-2025) is to resist Pillar Two and oppose UTPR application to US groups, including threatening §891 retaliatory measures.

### 8.3 What this means for US-parented MNEs in 2025

Two distinct exposure tracks:

**Track A — UTPR exposure from foreign jurisdictions.** US-parented groups with consolidated revenue ≥ €750M have constituent entities (subsidiaries, branches) in jurisdictions that have enacted UTPR. For fiscal years starting on or after Jan 1, 2025, those foreign jurisdictions may impose UTPR top-up tax on the US-parented group to the extent any constituent entity is low-taxed (including potentially the US parent itself, if its US effective rate is below 15% — which is plausible for groups with heavy R&D credits, FDII deduction, GILTI deduction, etc.).

**Track B — QDMTT exposure in low-tax jurisdictions.** A US-parented group with a Hungarian, Singaporean, Irish (post-changes), or Swiss-canton subsidiary may face QDMTT top-up tax in those jurisdictions for 2024+ fiscal years.

> **Critical practical implication:** A US-parented group's 2025 federal tax computation does not include any Pillar Two top-up tax (because the US has not adopted). But the group's consolidated financial statement tax provision under ASC 740 must include any foreign QDMTT and IIR (and potentially UTPR). Cash tax payments may include foreign top-up taxes that have no US tax credit (because the US has not adopted creditability rules for Pillar Two and the OECD's "Qualified IIR" creditability is still developing). This is a major income-tax-accounting issue distinct from this skill's scope.

### 8.4 §891 retaliation overlay (flag for reviewer)

- **§891 retaliation threat** — In early 2025, the administration directed Treasury and IRS to identify foreign tax laws that violate US tax treaties or are extraterritorial / discriminatory. §891 authorizes the President to double US tax rates on residents and corporations of countries imposing discriminatory taxes on US persons. This power has never been formally invoked but the threat creates uncertainty. Reviewer should monitor IRS notices for any §891 finding affecting Pillar Two-adopting countries.  _(§891)_

## 9. Compliance Forms Catalog

### 9.1 Form 5471 — Information Return of US Persons with Respect to Certain Foreign Corporations

The flagship CFC information return. Five categories of filers (Cat. 1, 2, 3, 4, 5):

**Form 5471 filer categories table**

| Category | Who files |
| --- | --- |
| **Cat. 1** | US Shareholders of "Section 965 Specified Foreign Corporations" (largely historical, but residual application for §965(i) S-corp deferred shareholders) |
| **Cat. 2** | US person who is an officer or director of a foreign corp where any US person acquires the §1248 ownership threshold during the year |
| **Cat. 3** | US person acquiring or disposing of 10% or more, or whose ownership crosses the 10% threshold |
| **Cat. 4** | US person with **>50% control** of the foreign corp for an uninterrupted 30-day period |
| **Cat. 5** | US Shareholder (10%+ vote or value) of a CFC for an uninterrupted 30-day period and who owns stock on the last day of the tax year |

Each category triggers different schedules. The 2025 Form 5471 contains 15+ schedules (Schedules A through Q, plus M, etc.). Notably:

- **Schedule I-1** — Information for GILTI (tested income, QBAI, etc.) — fed into Form 8992
- **Schedule J** — Accumulated E&P / PTEP tracking
- **Schedule P** — PTEP balances of the US Shareholder
- **Schedule M** — Transactions between CFC and related parties
- **Schedule Q** — CFC Income by CFC Income Group (Subpart F categories)

- **§6038 penalty exposure** — $10,000 per form per year for failure to file, with continuation penalties up to $50,000 per form. Plus 10% reduction in FTCs available. The IRS automates assessment of these penalties — late or missing 5471s trigger systemic penalty notices. Reasonable-cause abatement is available but inconsistently granted; reviewer should ensure all 5471s are filed on time.  _(§6038)_

**Farhy v. Commissioner, 160 T.C. No. 6 (2023)** held that the IRS lacked statutory authority to assess §6038(b) penalties without going through the deficiency procedures. The D.C. Circuit reversed in 2024 (Farhy v. Commissioner, 100 F.4th 223 (D.C. Cir. 2024)), holding that §6038(b) penalties are assessable. Practical impact: the IRS continues to auto-assess. Don't rely on Farhy for a filing-position decision.

### 9.2 Form 8992 — US Shareholder Calculation of GILTI

Required for any US Shareholder with a positive GILTI inclusion. Aggregates the tested income, tested loss, and QBAI data from the underlying Forms 5471 (Schedule I-1) and computes the GILTI inclusion.

- Form 8992 Schedule A — by-CFC data
- Form 8992 Schedule B — calculation of net CFC tested income and inclusion

For US Shareholders that are members of a US consolidated group, Form 8992 computes group-level GILTI; the regulations under Treas. Reg. §1.1502-51 allocate GILTI inclusions among the consolidated group members.

### 9.3 Form 8993 — Section 250 Deduction (FDII + GILTI)

The form on which a domestic C-corporation computes its §250 deduction:

- Part I — Determining DEI and DII
- Part II — Foreign-Derived Ratio (FDDEI / DEI)
- Part III — Section 250 deduction (2025: 50% × GILTI + §78 gross-up portion, plus 37.5% × FDII; post-2025: 40% × NCTI + attributable §78 amount, plus 33.34% × FDDEI)
- Part IV — Taxable income limitation under §250(a)(2)

Critical reconciliation: the §250 deduction reported on Form 1120, line 29b should tie to Form 8993, Part III line.

### 9.4 Form 8991 — Tax on Base Erosion Payments

For BEAT. Required when the applicable-taxpayer gross-receipts test is met, regardless of whether BEAT liability actually arises (to document non-application).

- Schedule A — Base erosion payments and tax benefits
- Schedule B — Modified taxable income
- Schedule C — Base erosion minimum tax amount (BEAT tax)

### 9.5 Related forms (refer-outs)

**Related forms refer-out table**

| Form | Purpose | Status here |
| --- | --- | --- |
| **Form 8865** | US person interest in foreign partnership | Refer out — separate skill needed |
| **Form 8858** | US person owner of foreign disregarded entity or foreign branch | Refer out |
| **Form 8975 + Schedule A** | Country-by-Country (CbC) reporting for groups ≥$850M consolidated revenue | Refer out — Pillar Two-related but distinct |
| **Form 5472** | 25%+ foreign-owned US corp / foreign corp engaged in US trade or business | Inbound — separate analysis |
| **Form 1118** | FTC for corporations (general; required for any FTC claim including GILTI basket) | Coordination needed; this skill mentions GILTI basket but doesn't fully cover §904 |
| **Form 1116** | FTC for individuals (relevant for §962 electors and individual Subpart F inclusions) | Coordination needed |
| **Form 965 / 965-A / 965-B** | §965 transition tax tracking | Covered at §7 above; final installments through 2025 |
| **Form 8938** | Foreign financial asset reporting | FATCA — separate from Title 26 reporting |
| **FBAR (FinCEN 114)** | Foreign bank account reporting | Title 31, not Title 26 — separate filing |

## 10. Worked Examples

All examples assume calendar-year filers, tax year **2025** (returns due in 2026), no extensions, no Pillar Two complications at the US level. Foreign tax rates and basis figures are illustrative.

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

TechCo, Inc. is a Delaware C-corporation, calendar year, owns 100% of TechCo GmbH (Germany), a CFC.
TechCo GmbH 2025 results:
  - Gross income (active services to unrelated EU customers): €5,000,000
  - Operating deductions (salaries, rent, depreciation): €3,800,000
  - Net pretax income: €1,200,000
  - German corporate income tax + Gewerbesteuer combined effective rate: 30%
  - German tax: €360,000 → after-tax income €840,000
  - Average adjusted basis (ADS) of tangible business property (laptops, office equipment, leasehold improvements): €600,000
  - No Subpart F items; no ECI; no §954(b)(4) high-tax election in 2025.
Assume €1 = $1.10 for simplicity. Translate at year-average exchange rate (Treas. Reg. §1.985-3 / §989).
TechCo Inc. has no other CFCs and no specified interest expense apportioned to GILTI basket.

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 1: Translate to USD** — Tested income (after deductions, before German tax): €1,200,000 × 1.10 = $1,320,000; German tax: €360,000 × 1.10 = $396,000; QBAI: €600,000 × 1.10 = $660,000  _(Treas. Reg. §1.985-3 / §989)_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 2: Tested income** — Under §951A(c), tested income is gross tested income less allocable deductions, but foreign income tax is not deducted in computing tested income (layered in via §78 gross-up). Tested Income = $1,320,000  _(§951A(c))_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 3: QBAI and Net Deemed Tangible Income Return** — NDTIR = 10% × $660,000 = $66,000 (No interest-expense allocation in this simple fact pattern.)  _(§951A)_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 4: GILTI inclusion** — Net CFC Tested Income = $1,320,000; GILTI (pre-§78) = $1,320,000 − $66,000 = $1,254,000  _(§951A)_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 5: §78 gross-up** — Inclusion Percentage = $1,254,000 / $1,320,000 = 95.0%; Tested Foreign Income Tax = $396,000; Deemed-paid tax = 95.0% × $396,000 = $376,200; Creditable amount (80% haircut) = 80% × $376,200 = $300,960; §78 gross-up adds the deemed-paid tax ($376,200) to the GILTI inclusion. GILTI included in TechCo Inc. taxable income = $1,254,000 + $376,200 = $1,630,200  _(§78)_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 6: §250 deduction** — §250 GILTI deduction = 50% × $1,630,200 = $815,100 (Subject to §250(a)(2) taxable income limitation, which we assume does not bite — TechCo has ample other US income.)  _(§250)_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 7: US tax on GILTI before FTC** — Tax base attributable to GILTI = $1,630,200 − $815,100 = $815,100; Tax at 21% = $171,171  _(21% corporate rate)_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 8: GILTI basket FTC** — §904 limitation on GILTI basket = (Foreign-source taxable income in GILTI basket / Worldwide taxable income) × US tax. In a simple model where all of GILTI is foreign-source and no expenses are apportioned to GILTI basket: §904 limitation ≈ $171,171; Deemed-paid tax creditable = $300,960; FTC allowed = min($300,960, $171,171) = $171,171. Excess of $300,960 − $171,171 = $129,789 is LOST (no carryforward).  _(§904)_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

- **Step 9: Net US tax on GILTI** — Net US tax = $171,171 − $171,171 = $0  _(§951A)_

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

Because the German effective rate (30%) is well above the 13.125% break-even, the §960(d) deemed-paid credit fully covers US residual GILTI tax in this simple fact pattern. The $129,789 of excess credit is permanently lost.

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

Form 5471 (Category 4 + 5), with Schedule I-1 reporting Tested Income $1,320,000, QBAI $660,000, Tested Foreign Income Tax $396,000. Form 8992 with the GILTI inclusion of $1,254,000 (before §78 gross-up). Form 1118 with GILTI-basket FTC of $171,171. Form 8993 with §250 GILTI deduction of $815,100. Form 1120 Schedule C / Schedule J pulling the §78 gross-up onto Line 5 and the §250 deduction on Line 29b.

### Example 1 — Small US C-corp with German subsidiary (GILTI inclusion)

Confirm no §954(b)(4) high-tax election would be more favorable. At 30% effective rate, the election excludes the income from GILTI entirely. With the election: $0 GILTI, $0 §250 deduction, $0 FTC needed — same $0 US tax but no permanent loss of $129,789 of excess FTC. Election is materially better in this case. Reviewer should run both scenarios.

### Example 2 — US Individual with Singapore CFC, §962 election analysis

Sarah is a US citizen residing in San Francisco. She owns 100% of Sarah Trading Pte. Ltd. (Singapore), formed in 2022 to provide consulting services to Asia-Pacific clients.
2025 results of Sarah Trading Pte. Ltd.:
  - Gross income: SGD 800,000
  - Operating deductions (Sarah's salary as employee/director, office, travel, software): SGD 500,000
  - Net pretax income: SGD 300,000
  - Singapore CIT: 17% effective rate (partial-exemption regime, ignoring incentives) = SGD 51,000
  - After-tax income: SGD 249,000
  - QBAI (laptops, furniture, ADS basis): SGD 40,000
Sarah pays herself a SGD 120,000 salary that the CFC deducts. (Wage income — handled on Sarah's individual return separately; not relevant to the GILTI computation here, already deducted at the CFC.)
No actual dividend distributions in 2025.
USD/SGD year-average: 1.35 SGD = $1 USD (i.e., $1 SGD = $0.74).
Sarah's other 2025 US taxable income (wage + Subpart F-free) keeps her in the 37% top bracket plus 3.8% NIIT.

### Example 2 — US Individual with Singapore CFC, §962 election analysis

- **Step 1: Translate** — Tested income USD: SGD 300,000 ÷ 1.35 = $222,222; Singapore tax USD: SGD 51,000 ÷ 1.35 = $37,778; QBAI USD: SGD 40,000 ÷ 1.35 = $29,630

### Example 2 — US Individual with Singapore CFC, §962 election analysis

- **Step 2: GILTI inclusion (mechanically same for individual as for corp)** — NDTIR = 10% × $29,630 = $2,963; GILTI = $222,222 − $2,963 = $219,259

### Example 2 — US Individual with Singapore CFC, §962 election analysis

- **Step 3 — Scenario A: NO §962 election** — Sarah includes $219,259 as ordinary income on Schedule 1. No §250 deduction (individual). No §960(d) deemed-paid FTC (individual). Sarah's marginal rate: 37% federal + 3.8% NIIT = 40.8%. Federal tax on GILTI: $219,259 × 40.8% = $89,458. California state tax: California does not conform to GILTI deduction; CA taxes the inclusion at up to 13.3% — additional ~$29,159. (State out of scope here but flagging.) Singapore corporate tax already paid: $37,778 — no US credit available (individual can't claim §960(d)).

### Example 2 — US Individual with Singapore CFC, §962 election analysis

Scenario A total US federal tax on GILTI = $89,458. Plus the $37,778 Singapore tax already paid sits on top — total economic tax burden = $127,236 on $222,222 of CFC pretax income = 57.3% effective rate. Brutal.

### Example 2 — US Individual with Singapore CFC, §962 election analysis

- **Step 4 — Scenario B: §962 election** — Under §962, Sarah is taxed on the GILTI inclusion as if she were a domestic C-corp. §78 gross-up: Inclusion percentage = $219,259 / $222,222 = 98.67%. Deemed-paid tax = 98.67% × $37,778 = $37,275. Creditable at 80% = $29,820. Grossed-up GILTI inclusion = $219,259 + $37,275 = $256,534. §250 deduction = 50% × $256,534 = $128,267. Tax base = $256,534 − $128,267 = $128,267. US tax at 21% (§962 corporate rate) = $26,936. GILTI-basket FTC available = $29,820. §904 limitation on GILTI basket ≈ $26,936 (with no expense apportionment). FTC allowed = min($29,820, $26,936) = $26,936. Excess $2,884 LOST. Net US federal tax on GILTI inclusion under §962 = $0. NIIT does NOT apply to §962 income (because it is treated as corporate-rate income, not individual investment income — but this point is contested in some recent IRS positions; see CCA 202118008 — flag).  _(§962; CCA 202118008)_

### Example 2 — US Individual with Singapore CFC, §962 election analysis

Scenario B current-year US federal tax = $0.

### Example 2 — US Individual with Singapore CFC, §962 election analysis

- **Step 5 — Future distribution analysis (the §962 catch)** — Sarah's deferred PTEP from the 2025 §962 inclusion is previously taxed under §962, but §962(d) and Treas. Reg. §1.962-3 can still cause a later actual distribution to be taxed to the individual electing shareholder as a dividend to the extent it exceeds the §962 tax paid. In this Singapore example, do not assume qualified-dividend treatment on treaty grounds: Singapore is not on the IRS comprehensive income-tax treaty list. For a private Singapore Pte. Ltd., model the later §962 distribution as an ordinary dividend unless a separate qualified-dividend basis is documented. Singapore generally has no domestic dividend withholding tax, but US ordinary dividend/NIIT rates can make the future distribution cost materially higher than a 23.8% qualified-dividend estimate.  _([IRC §962(d); Treas. Reg. §1.962-3; IRS treaty list; IRC §1(h)(11)](https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z))_

### Example 2 — US Individual with Singapore CFC, §962 election analysis

**Comparing Scenarios A and B over time (assuming all earnings ultimately distributed)**

|  | Scenario A (no §962) | Scenario B (§962) |
| --- | --- | --- |
| Current US tax 2025 | $89,458 | $0 |
| Future US tax on $256,534 distribution | $0 (PTEP) | ~$61,055 (qualified div) |
| **Total US federal tax** | **$89,458** | **~$61,055** |

### Example 2 — US Individual with Singapore CFC, §962 election analysis

§962 is clearly preferable here — savings of approximately $28,403 (plus NIIT-on-distribution complications).

### Example 2 — US Individual with Singapore CFC, §962 election analysis

Form 5471 (Cat. 5), Schedule I-1 with tested income, QBAI. Form 8992 with Sarah's GILTI inclusion of $219,259. §962 election statement attached to Form 1040, citing Treas. Reg. §1.962-2(b), specifying the inclusion year, CFCs covered, and identifying information. Form 8993 for the §250 GILTI deduction (yes — an individual making a §962 election uses Form 8993 to claim the corporate deduction). Form 1116 for the GILTI-basket FTC at the individual level (§962 election permits the deemed-paid credit, but it's still reported on 1116 for individuals). Maintain PTEP tracking schedule for Sarah's §962 account.

### Example 2 — US Individual with Singapore CFC, §962 election analysis

1. Confirm the §962 election is timely (must be on a timely-filed return with extensions).
2. Confirm the basis-and-PTEP tracking. §962 PTEP accounts are notoriously poorly maintained and the consequences (in years 3, 5, 10 when distribution occurs) are severe.
3. State conformity: California has historically taxed GILTI inclusions at the individual level without the §250 deduction (CA non-conformity). The federal §962 election does not automatically flow into California — separate analysis needed. Consult `ca-540-individual-return`.
4. Watch the Singapore Pillar Two QDMTT situation — Singapore enacted a 15% QDMTT effective Jan 1, 2025 for groups within Pillar Two scope. Sarah's solo-shareholder CFC is well below €750M and not within Pillar Two, so this doesn't bite here, but is worth flagging for larger fact patterns.

### Example 3 — Large MNE BEAT computation

MegaCorp, Inc. is a publicly traded US C-corp with 2022–2024 average annual gross receipts of $2.4 billion. (Meets $500M gateway.)
2025 tax year results (US-only, simplified):
  - Gross receipts: $2,500M
  - COGS: $1,200M
  - Total deductions other than COGS: $1,000M, of which:
    - Salaries/G&A (US payees): $400M
    - Interest expense (third-party banks, US): $50M
    - Royalty paid to Foreign IP Co. (Bermuda, 100% related party — foreign related party): $150M [base erosion payment]
    - Management services fee paid to Foreign HQ Co. (Switzerland, related party), no SCM exception (priced cost-plus 8%): $80M [base erosion payment; the markup portion (~$5.9M) is the base eroding tax benefit only if SCM applied to cost portion — without SCM, the entire $80M is a base erosion payment]
    - Other US-domestic deductions: $320M
    - Depreciation on building acquired from foreign related party in 2023 (cost basis $200M, 39-year recovery): $5.1M annually [base erosion tax benefit — flowing from a base erosion payment as property acquisition]
Regular taxable income: $2,500M − $1,200M COGS − $1,000M deductions = $300M
Regular tax at 21% = $63M (before credits)
R&D credit (§41): $20M
Other GBC credits (§38 / §48 ITC / §45 PTC): $15M
Net regular tax liability after credits: $63M − $20M − $15M = $28M

### Example 3 — Large MNE BEAT computation

- **Step 1: Applicable taxpayer test** — Average gross receipts: $2,400M ≥ $500M ✓ Base erosion percentage: ``` Base Erosion Tax Benefits this year: - Royalty paid to Bermuda IP Co.: $150M - Services fee to Swiss HQ Co.: $80M - Depreciation on related-party-acquired building: $5.1M Total: $235.1M Total deductions allowed: $1,000M total deductions (above) excluding COGS (Note: COGS is NOT a deduction so neither numerator nor denominator) Base Erosion Percentage = $235.1M / $1,000M = 23.51% ``` 23.51% ≥ 3% threshold ✓ — MegaCorp is an applicable taxpayer.

### Example 3 — Large MNE BEAT computation

- **Step 2: Modified Taxable Income (MTI)** — ``` Regular Taxable Income:          $300.0M + Base Erosion Tax Benefits:     $235.1M + Base Erosion % × NOL deduction: $0  (no NOL used) ───────── Modified Taxable Income:         $535.1M ```

### Example 3 — Large MNE BEAT computation

- **Step 3: BEAT Minimum Tax Amount** — 2025 BEAT rate = 10%. ``` 10% × MTI                           = 10% × $535.1M  = $53.51M Regular tax liability for BEAT comparison: Regular tax before credits         = $63.00M Total credits                      = $35.00M Protected credits for BEAT         = $20.00M R&D + (80% × $15M) = $32.00M Disallowed credit add-back         = $3.00M Regular tax for BEAT comparison    = $63.00M - $3.00M = $60.00M BEAT Minimum Tax Amount = max(0, $53.51M - $60.00M) = $0 ```  _([IRC §59A; Form 8991 instructions](https://www.irs.gov/pub/irs-dft/i8991--dft.pdf))_
- **2025 BEAT rate** — 10%  _(§59A)_

### Example 3 — Large MNE BEAT computation

- **Step 4: Total federal tax** — ``` Regular tax after credits:         $28.00M BEAT add-on:                       $22.51M ───────── Total federal tax:                 $50.51M ```

### Example 3 — Large MNE BEAT computation

- **Step 5: 2026 projection (illustrative)** — If MegaCorp's 2026 facts are similar, OBBBA applies a 10.5% BEAT rate and continues protected-credit treatment for the §41 R&D credit and applicable §38 credits. ``` 10.5% × MTI                         = 10.5% × $535.1M = $56.19M Regular tax liability for BEAT comparison: Regular tax before credits         = $63.00M Total credits                      = $35.00M Protected credits for BEAT         = $20.00M R&D + (80% × $15M) = $32.00M Disallowed credit add-back         = $3.00M Regular tax for BEAT comparison    = $63.00M - $3.00M = $60.00M BEAT Minimum Tax Amount = max(0, $56.19M - $60.00M) = $0 Regular tax after credits remains    = $28.00M Total federal tax                    = $28.00M ```  _([IRC §59A as amended by OBBBA P.L. 119-21; Draft 2025 Instructions for Form 8991](https://www.irs.gov/pub/irs-dft/i8991--dft.pdf))_

### Example 3 — Large MNE BEAT computation

Counterintuitively, the 2026 BEAT add-on decreases in this fact pattern despite the higher rate, because the credit add-back raises the regular-tax floor. The 2026 result is sensitive: a different MTI/credit mix could produce the opposite outcome. Always re-run the BEAT model for each year.

### Example 3 — Large MNE BEAT computation

Form 8991, with Schedule A listing each base erosion payment by counterparty + payment type, Schedule B for MTI, Schedule C for the BEAT computation. Form 1120 with the BEAT add-on on Schedule J, Part I.

### Example 3 — Large MNE BEAT computation

1. Confirm Services Cost Method analysis: is any of the $80M Swiss management fee at-cost (no markup) and eligible for SCM exclusion? If so, the cost portion is excluded; only the markup is a BEAT payment. Materially changes the result.
2. Confirm no §59A(h) qualified derivative payments are misclassified.
3. Confirm Bermuda IP Co. royalty is not subject to full US gross-basis withholding — Bermuda has no income tax treaty with the US, so the royalty is subject to 30% statutory WHT under §1442 unless reduced. Withholding paid by the payor may exclude the payment from BEAT (§59A(c)(2)(A)(ii)) — but only to the extent withholding tax was actually paid. Verify Form 1042 withholding.
4. Confirm constructive ownership / aggregation under §59A(e)(3) — MegaCorp may need to aggregate with US sister entities.
5. Coordinate Pillar Two analysis: if MegaCorp's consolidated revenue is ≥ €750M (it is — $2.5B converts to >€2.3B), MegaCorp is within Pillar Two scope worldwide. Foreign jurisdictions where MegaCorp operates may impose QDMTT/IIR/UTPR on the group. The Swiss HQ Co. or Bermuda IP Co. low effective rates could trigger UTPR top-up tax in third-country jurisdictions starting 2025. Refer to Pillar Two specialist.

## 11. Process Notes for Reviewer

### 11.1 Order of operations for a return with all three regimes

- **Order of operations** — 1. Determine CFC status of each foreign corp (§957 vote/value test, §958 attribution including post-§958(b)(4)-repeal downward attribution). 2. Identify US Shareholders (§951(b) 10% vote OR 10% value). 3. For each CFC and US Shareholder, compute Subpart F first (§951(a) categories). 4. Compute tested income / tested loss / QBAI per CFC (§951A(c)(2), §951A(d), via Form 5471 Schedule I-1). 5. Consider §954(b)(4) high-tax election (per "tested unit"). Run with-and-without scenarios for material CFCs. 6. Aggregate to US Shareholder GILTI inclusion (Form 8992). 7. Compute deemed-paid taxes and the GILTI-basket §904 limitation (Form 1118 / 1116). 8. For C-corps: compute FDII (Form 8993). Run together with GILTI for §250(a)(2) limitation. 9. For C-corps with >$500M gross receipts: run BEAT applicable-taxpayer test, then BEAT computation if applicable (Form 8991). 10. For individuals: evaluate §962 election with side-by-side scenario comparison. 11. Track PTEP balances (Schedules J and P of Form 5471, plus §962 PTEP separately). 12. Track §965 installment status if still in 8-year stream (final installment typically 2025). 13. Pillar Two: flag exposure for groups ≥€750M consolidated revenue. Coordinate with international finance team and ASC 740 provision. 14. State conformity overlay (refer to state-specific skill). 15. Reviewer signoff under Circular 230.  _(§957; §958; §951(b); §951(a); §951A(c)(2); §951A(d); §954(b)(4); §904; §250(a)(2))_

### 11.2 Defaults under uncertainty

- **Defaults under uncertainty** — Per `us-tax-workflow-base` conservative defaults principle: When CFC status is unclear, assume CFC and require explicit ownership documentation to rebut. When §954(b)(4) high-tax election would be material, run both scenarios and present to client. When §962 election would be material, default to running the side-by-side. When base erosion payment characterization is unclear, default to including as BEAT payment and require taxpayer documentation to support exclusion. When foreign use documentation for FDII is missing or inadequate, default to excluding from FDDEI. When in doubt about whether a foreign affiliate is a CFC due to §958(b)(4) downward attribution, default to filing Form 5471 (penalty for unnecessary filing is $0; penalty for missed required filing is $10,000+ per form).  _(us-tax-workflow-base conservative defaults principle)_

### 11.3 Common errors observed in practice

**Common errors observed in practice**  _([IRC §250; IRC §960(d); IRC §59A](https://uscode.house.gov/view.xhtml?req=(title:26%20section:59A%20edition:prelim)))_

| Error | Consequence | Fix |
| --- | --- | --- |
| Computing QBAI under MACRS instead of ADS | Overstates QBAI, understates GILTI — IRS exam adjustment | Recompute under ADS straight-line over class life |
| Treating §250 deduction as available to individuals without §962 election | Wrong return; client owes back-tax + penalties | Verify §962 statement was filed |
| Using the wrong §960(d) haircut | Overstates or understates FTC depending on year | Apply 80% for 2018-2025 GILTI and 90% for post-2025 NCTI |
| Carrying forward GILTI-basket excess FTC | Wrong — no carryforward allowed | Recognize permanent loss |
| Claiming FDII without §1.250(b)-3 documentation | FDII disallowed on audit | Build documentation file before filing |
| Missing a §958(b)(4)-downward-attribution CFC | $10K-50K penalty per missed Form 5471 | Run downward-attribution check for every US sub of a foreign-parented group |
| Treating COGS as a base erosion payment | Overstates BEAT | COGS is not a deduction; exclude from numerator and denominator |
| Treating protected credits as fully disallowed for BEAT after 2025 | Overstates BEAT | Use enacted OBBBA §59A/Form 8991 credit treatment |
| Forgetting §250(a)(2) taxable income limit | Overstates §250 deduction | Compute taxable income before §250 first |
| Confusing §951 (Subpart F) and §951A (GILTI) inclusions | Wrong character; wrong FTC basket | Subpart F = general/passive basket; GILTI = own basket |

## 12. Provenance

### 12.1 Statutory authorities

- **IRC §951** — Amounts included in gross income of United States Shareholders (Subpart F).  _(IRC §951)_
- **IRC §951A** — Global Intangible Low-Taxed Income included in gross income of United States shareholders (enacted TCJA P.L. 115-97 §14201, effective tax years beginning after Dec 31, 2017).  _(IRC §951A)_
- **IRC §952** — Subpart F income defined.  _(IRC §952)_
- **IRC §954** — Foreign base company income; FPHCI, FBCSI, FBCSvI; high-tax exception §954(b)(4).  _(IRC §954)_
- **IRC §957** — Controlled foreign corporation; definition.  _(IRC §957)_
- **IRC §958** — Rules for determining stock ownership; §958(b)(4) repeal by TCJA §14213.  _(IRC §958)_
- **IRC §960** — Deemed-paid credit for subpart F inclusions and for GILTI under §960(d).  _(IRC §960)_
- **IRC §959** — Exclusion from gross income of previously taxed earnings and profits.  _(IRC §959)_
- **IRC §962** — Election by individuals to be subject to tax at corporate rates.  _(IRC §962)_
- **IRC §965** — Treatment of deferred foreign income upon transition to participation exemption system (one-time transition tax; TCJA §14103).  _(IRC §965)_
- **IRC §245A** — Deduction for foreign source-portion of dividends received by domestic corporations from specified 10-percent owned foreign corporations.  _(IRC §245A)_
- **IRC §250** — Foreign-derived intangible income and global intangible low-taxed income (the deduction).  _(IRC §250)_
- **IRC §59A** — Tax on base erosion payments of taxpayers with substantial gross receipts (BEAT).  _(IRC §59A)_
- **IRC §78** — Gross-up for deemed-paid foreign taxes.  _(IRC §78)_
- **IRC §904** — Limitation on foreign tax credit (basket rules including §904(d)(1)(A) GILTI basket).  _(IRC §904)_
- **IRC §6038** — Information returns with respect to foreign corporations; penalties.  _(IRC §6038)_
- **IRC §6038A / 6038C** — 25%-foreign-owned domestic corp reporting (Form 5472 — referenced, out of scope).  _(IRC §6038A / 6038C)_
- **IRC §174** — Research and experimental expenditures (TCJA capitalization rule; OBBBA 2025 domestic R&E expensing reinstatement — verify operative version).  _(IRC §174)_

### 12.2 Treasury Regulations

- **Treas. Reg. §1.951A-1 through §1.951A-7** — GILTI mechanics; tested income, QBAI, expense allocation, etc.  _(Treas. Reg. §1.951A-1 through §1.951A-7)_
- **Treas. Reg. §1.951A-2(c)(7)** — High-tax exclusion election.  _(Treas. Reg. §1.951A-2(c)(7))_
- **Treas. Reg. §1.250(a)-1, §1.250(b)-1 through §1.250(b)-6** — §250 deduction; FDII and GILTI deduction mechanics; foreign use rules; documentation rules.  _(Treas. Reg. §1.250(a)-1, §1.250(b)-1 through §1.250(b)-6)_
- **Treas. Reg. §1.59A-1 through §1.59A-10** — BEAT regulations.  _(Treas. Reg. §1.59A-1 through §1.59A-10)_
- **Treas. Reg. §1.1502-51** — GILTI in US consolidated groups.  _(Treas. Reg. §1.1502-51)_
- **Treas. Reg. §1.962-1 through §1.962-3** — §962 election mechanics, PTEP, distributions.  _(Treas. Reg. §1.962-1 through §1.962-3)_
- **Treas. Reg. §1.959-1 through §1.959-4** — PTEP ordering and distributions.  _(Treas. Reg. §1.959-1 through §1.959-4)_

### 12.3 IRS forms (2025 versions)

Form 5471 and Schedules A-Q + I-1 + M + P + Q
Form 8992 (GILTI computation) and Schedules A, B
Form 8993 (§250 deduction)
Form 8991 (BEAT)
Form 1118 (corporate FTC)
Form 1116 (individual FTC)
Form 965 / 965-A / 965-B (§965 transition tax)
Form 1120 (corporate return)
Form 1040 (individual return)
Form 8975 + Schedule A (Country-by-Country reporting — referenced)

### 12.4 Legislative authority

- **Tax Cuts and Jobs Act** — P.L. 115-97, Dec 22, 2017 — TCJA — origin of §951A, §250, §59A, §245A, §965, §958(b)(4) repeal.  _(P.L. 115-97)_
- **One Big Beautiful Bill Act** — P.L. 119-21, July 4, 2025 — OBBBA — selective changes; specific section-by-section verification required for any §250 / §59A / §174 question.  _(P.L. 119-21)_
- **PATH Act** — P.L. 114-113, Dec 2015 — made the §954(h) active financing exception permanent.  _(P.L. 114-113)_

### 12.5 Key administrative guidance

- **Notice 2018-13** — §958(b)(4) repeal transition / sister CFC safe harbor.  _(Notice 2018-13)_
- **Rev. Proc. 2019-40** — Limited safe harbor for "no information" §958(b)(4) downward-attribution CFCs.  _(Rev. Proc. 2019-40)_
- **Notice 2018-26** — §965 guidance.  _(Notice 2018-26)_
- **CCA 202118008** — §962 election and NIIT (informal IRS position).  _(CCA 202118008)_

Various Treasury / IRS Pillar Two notices (2023–2025) — US position on Pillar Two creditability and Article 9.1 transitional CbCR safe harbor.

### 12.6 Notable case law

- **Farhy v. Commissioner** — 160 T.C. No. 6 (2023), rev'd 100 F.4th 223 (D.C. Cir. 2024) — §6038(b) Form 5471 penalty assessability.  _(Farhy v. Commissioner, 160 T.C. No. 6 (2023), rev'd 100 F.4th 223 (D.C. Cir. 2024))_
- **Smith v. Commissioner** — T.C. Memo. 2018-127 — §962 distribution treatment.  _(Smith v. Commissioner, T.C. Memo. 2018-127)_
- **Whirlpool Financial Corp. v. Commissioner** — 19 F.4th 944 (6th Cir. 2021) — branch rule under §954(d)(2); subpart F income from manufacturing branch.  _(Whirlpool Financial Corp. v. Commissioner, 19 F.4th 944 (6th Cir. 2021))_

### 12.7 OECD / Pillar Two source documents

OECD/G20 Inclusive Framework Pillar Two Model Rules (December 2021)
OECD Commentary on GloBE Model Rules (March 2022, updated)
OECD Administrative Guidance — multiple releases (Feb 2023, July 2023, Dec 2023, June 2024).
EU Directive 2022/2523 (Pillar Two implementation in EU member states).

### 12.8 Skill metadata

Skill version: 0.1
Last updated: 2026-07-10
Authored under: us-tax-workflow-base v0.2 (Tier 1 workflow contract)
Verification status: pending — requires sign-off by a Circular 230 practitioner with international tax expertise (Enrolled Agent with international specialty, CPA with international concentration, or attorney with subspecialty). Verifier must specifically confirm:
1. The enacted OBBBA §250, §960(d), and §59A post-2025 mechanics reflected in this guide.
2. The operative §174 R&E rule for the return year.
3. The current Pillar Two adoption / non-adoption status and §891 retaliation guidance.
4. Any Treasury/IRS post-2025 guidance that materially changes the rules described herein.

### 12.9 Refusal catalogue additions (Tier 2 specific)

The following are out of scope for this skill and the assistant must refuse and refer out:

- **R-INTL-1** — Transfer pricing studies / §482 economic analysis — refer to qualified transfer pricing economist.  _(R-INTL-1)_
- **R-INTL-2** — Foreign tax credit basket optimization beyond GILTI basket — refer to specialist §904 analysis.  _(R-INTL-2)_
- **R-INTL-3** — Pillar Two QDMTT / IIR / UTPR computations in foreign jurisdictions — refer to foreign-jurisdiction skill or specialist.  _(R-INTL-3)_
- **R-INTL-4** — Treaty position analysis or LOB qualification — refer to treaty specialist.  _(R-INTL-4)_
- **R-INTL-5** — Inversion transaction planning (§7874) — refuse; not within freelance / small-business skill scope.  _(R-INTL-5)_
- **R-INTL-6** — Hybrid instrument analysis under §245A(e) / §267A — refer for specialist review.  _(R-INTL-6)_
- **R-INTL-7** — Multi-tier CFC chains with §959 / PTEP layering beyond two tiers — refer for specialist review.  _(R-INTL-7)_
- **R-INTL-8** — US trust / foreign trust / §6048 reporting — refer to international trust specialist.  _(R-INTL-8)_
- **R-INTL-9** — PFIC (§1291 / §1297) analysis or QEF / mark-to-market elections — refer to PFIC specialist skill (not yet authored).  _(R-INTL-9)_
- **R-INTL-10** — Cross-border M&A tax structuring — outside content-skill scope; full advisory engagement.  _(R-INTL-10)_

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
