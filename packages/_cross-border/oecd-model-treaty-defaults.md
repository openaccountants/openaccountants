---
name: oecd-model-treaty-defaults
description: "OECD Model Tax Convention default provisions for cross-border tax allocation. Contains the baseline treaty rules that most bilateral Double Taxation Agreements (DTAs) follow. Use when interpreting treaty provisions, applying tie-breaker rules, determining PE thresholds, classifying income types under treaty articles, or understanding methods to eliminate double taxation. Trigger on: \"OECD model\", \"model tax convention\", \"treaty article\", \"Article 4 tie-breaker\", \"Article 5 PE\", \"Article 7 business profits\", \"Article 12 royalties\", \"Article 13 capital gains\", \"Article 15 employment income\", \"Article 23 double taxation relief\", \"credit method\", \"exemption method\", \"mutual agreement procedure\", \"MAP\", \"UN model differences\", or any reference to interpreting a bilateral tax treaty. Updated to reflect the 2025 OECD Model update (including remote work PE guidance in the Commentary on Article 5)."
version: 1.0
jurisdiction: INTL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oecd Model Treaty Defaults

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | International (OECD member and partner countries) |
| Primary Source | OECD Model Tax Convention on Income and on Capital (consolidated 2025 update) |
| Supporting Source | UN Model Double Taxation Convention (2021 update) |
| Scope | Default allocation of taxing rights between residence and source states; PE definition; income classification; double taxation elimination methods |
| Contributor | OpenAccountants |
| Validation Date | May 2026 |
| Skill Version | 1.0 |
| Key update | 2025 OECD update: new Commentary on Art 5 re home office PE; Art 9 transfer pricing clarifications; Art 25 Amount B signposting; Art 26 exchange of information |

### Model provision (Art 4(1))

- **Resident of a Contracting State (Art 4(1))** — "For the purposes of this Convention, the term 'resident of a Contracting State' means any person who, under the laws of that State, is liable to tax therein by reason of his domicile, residence, place of management or any other criterion of a similar nature."  _(Art 4(1) OECD Model Tax Convention)_

### Dual residence tie-breaker for individuals (Art 4(2))

**Dual residence tie-breaker for individuals (Art 4(2))**  _(Art 4(2) OECD Model Tax Convention)_

| Priority | Test | Key factors | Resolution |
| --- | --- | --- | --- |
| 1 | **Permanent home available** | Does the person have a home continuously available in one state? Includes owned or rented accommodation. A home rented OUT to others is NOT "available." | If permanent home in only ONE state → resident there |
| 2 | **Centre of vital interests** | Where are personal and economic relations closer? Family, social connections, employment, business activities, political/cultural activities, property, bank accounts | If centre of vital interests in only ONE state → resident there |
| 3 | **Habitual abode** | Where does the person stay habitually? Assessed over a sufficient period (not just the current year). Compares frequency/duration of presence in each state | If habitual abode in only ONE state → resident there |
| 4 | **Nationality** | Citizenship | If national of only ONE state → resident there |
| 5 | **Mutual Agreement Procedure** | Competent authorities negotiate | If all above fail → MAP between governments (typically 24–36 months) |

### Dual residence tie-breaker for entities (Art 4(3))

- **Entity dual residence tie-breaker** — For entities (companies) resident in both states, the 2017 update replaced the "place of effective management" (POEM) automatic tie-breaker with a MAP requirement: the competent authorities shall determine by mutual agreement the state of residence, having regard to: Place of effective management; Place of incorporation/constitution; Any other relevant factors. If no agreement → entity NOT entitled to treaty benefits (except as agreed).  _(Art 4(3) OECD Model Tax Convention (2017 update))_

### Practical guidance

- The tie-breaker cascade ONLY applies when BOTH states claim the person as a full tax resident under their domestic law
- Many older treaties still use the pre-2017 formulation for entities (POEM as automatic tie-breaker)
- The 2025 update did not change Article 4 — the remote work Commentary additions are under Article 5

### Model definition (Art 5(1))

- **Permanent establishment (Art 5(1))** — "For the purposes of this Convention, the term 'permanent establishment' means a fixed place of business through which the business of an enterprise is wholly or partly carried on."  _(Art 5(1) OECD Model Tax Convention)_

### Three-element test

**Three-element test**  _(Art 5 OECD Model Tax Convention)_

| Element | Requirement | Assessment |
| --- | --- | --- |
| **Place of business** | A facility — office, room, factory, workshop, desk, even a pitch in a marketplace | Must be a tangible, identifiable location |
| **Fixed** | Established at a distinct spot with a degree of permanence (not merely temporary) | Generally requires more than 6 months; some treaties specify thresholds |
| **Business carried on through it** | The enterprise actually conducts its business activities at/through the place | Preparatory/auxiliary activities excluded (Art 5(4)) |

### Specific inclusion list (Art 5(2))

- **PE inclusion list** — The following are expressly included as PE examples: Place of management; Branch; Office; Factory; Workshop; Mine, oil/gas well, quarry, or other extraction site  _(Art 5(2) OECD Model Tax Convention)_

### Construction PE (Art 5(3))

- **Construction PE threshold** — A building site or construction or installation project constitutes a PE only if it lasts more than twelve months. Many bilateral treaties reduce this to 6 months (check specific treaty). The 12-month clock starts when preparatory work begins at the site and stops when work is permanently discontinued. months  _(Art 5(3) OECD Model Tax Convention)_

### Exclusions — NOT a PE (Art 5(4))

**Exclusions — NOT a PE (Art 5(4))**  _(Art 5(4) OECD Model Tax Convention)_

| Activity | Status |
| --- | --- |
| Storage, display, or delivery of goods belonging to the enterprise | NOT a PE |
| Maintenance of stock for processing by another enterprise | NOT a PE |
| Maintenance of a fixed place solely to purchase goods or collect information | NOT a PE |
| Maintenance of a fixed place solely for any preparatory or auxiliary activity | NOT a PE |
| Maintenance of a fixed place solely for any combination of the above | NOT a PE |

- **Anti-fragmentation rule** — These exclusions do NOT apply if: The activity is NOT of a preparatory or auxiliary character, OR the enterprise (or a closely related enterprise) carries on business at the same place or another place in the same state, and the combined activity is NOT preparatory/auxiliary.  _(Art 5(4.1) OECD Model Tax Convention (2017 Model))_

### Agent PE (Art 5(5)–(6))

**Agent PE (Art 5(5)–(6))**  _(Art 5(5)–(6) OECD Model Tax Convention)_

| Type | Creates PE? | Conditions |
| --- | --- | --- |
| **Dependent agent** | YES | Person habitually concludes contracts (or plays the principal role leading to conclusion without material modification) in the name of the enterprise |
| **Independent agent** | NO | Agent of independent status acting in ordinary course of business |
| **Closely related agent** | YES (per 2017 rules) | Agent acts exclusively or almost exclusively for closely related enterprises (>50% interest) — cannot be "independent" |

### 2025 Commentary update — remote work and home offices

**2025 Commentary update — remote work and home offices**  _(2025 update to the Commentary on Article 5)_

| Factor | Guidance |
| --- | --- |
| **Less than 50% rule** | If an individual works from a home office less than 50% of total working time over any 12-month period, this generally will NOT constitute a PE of the employer |
| **Commercial reasons test** | Even if ≥ 50%, a PE may not arise if the home office use is for the employee's convenience (not required by employer), has no commercial reason for the employer, and the employer has a suitable office available |
| **Employer-required** | If the employer requires the employee to work from home (no alternative office provided), and this exceeds 50% of working time, a PE is more likely |
| **Not a blanket rule** | The 50% threshold is an indicative guidance point in the Commentary, not a binding treaty rule — it is a factor in the overall assessment |

Important: The 2025 Commentary guidance only applies to treaties that are interpreted consistently with the current OECD Commentary. Older treaties may be interpreted under the Commentary in force when concluded.

### Model rule

- **Business profits taxation rule** — "The profits of an enterprise of a Contracting State shall be taxable only in that State unless the enterprise carries on business in the other Contracting State through a permanent establishment situated therein."  _(Art 7 OECD Model Tax Convention)_

### Key principles

**Key principles**  _(Art 7 OECD Model Tax Convention)_

| Principle | Rule |
| --- | --- |
| **Exclusive residence taxation** | Business profits taxable ONLY in the residence state — unless there is a PE in the other state |
| **PE attribution** | If PE exists, the source state may tax ONLY the profits attributable to the PE |
| **Arm's length attribution** | Profits attributed to PE as if it were a separate, independent enterprise dealing at arm's length with the rest of the enterprise |
| **Expense deduction** | Expenses incurred for the PE are deductible, including executive and general administrative expenses (whether in the PE state or elsewhere) |
| **No force of attraction** | The source state cannot tax profits of the enterprise that are NOT attributable to the PE (even if the enterprise has other activities in that state) |

### Practical significance for freelancers

If a freelancer has NO PE in the client's country, business profits are taxable ONLY in the freelancer's residence country. The client's country has no right to tax under Article 7, even if the client is paying from that country.

**This is the single most important treaty article for cross-border freelancers.** Combined with the PE analysis under Article 5, it answers: "Do I owe tax in my client's country?"

### Model rule (OECD position: exclusive residence-state taxation)

- **Royalties taxation rule** — "Royalties arising in a Contracting State and paid to a resident of the other Contracting State shall be taxable only in that other State if such resident is the beneficial owner of the royalties."  _(Art 12 OECD Model Tax Convention)_

### OECD Model: 0% source-state WHT

- **Royalties source-state WHT under OECD Model** — 0%  _(Art 12 OECD Model Tax Convention — royalties taxable ONLY in the residence state of the beneficial owner)_

However: Many actual bilateral treaties deviate from the OECD Model and allow source-state WHT on royalties at negotiated rates (commonly 5%, 10%, or 15%). Always check the specific treaty.

### Definition of royalties (Art 12(2))

- **Royalties (Art 12(2))** — "Payments of any kind received as a consideration for the use of, or the right to use, any copyright of literary, artistic or scientific work including cinematograph films, any patent, trade mark, design or model, plan, secret formula or process, or for information concerning industrial, commercial or scientific experience."  _(Art 12(2) OECD Model Tax Convention)_

### Software payments — the contested classification

**Software payments — the contested classification**  _(Art 12 / Art 7 OECD Model Tax Convention)_

| Payment type | OECD position | Many countries' position |
| --- | --- | --- |
| Payment for a copy of software for personal/business use | **Business profits** (Art 7) — NOT a royalty | Some countries (India, Brazil) treat as royalty |
| Payment for the right to reproduce/distribute software | **Royalty** (Art 12) | Consistent with OECD |
| Payment for a site license (limited copies) | **Business profits** (Art 7) | Contested in some jurisdictions |
| SaaS subscription (no transfer of software) | **Business profits** (Art 7) | India treats as royalty (Explanation 4 to § 9(1)(vi)) |

### Allocation rules

**Allocation rules**  _(Art 13 OECD Model Tax Convention)_

| Asset type | Taxing right |
| --- | --- |
| Immovable property (Art 13(1)) | May be taxed in the state where the property is situated |
| Movable property of a PE (Art 13(2)) | May be taxed in the state where the PE is situated |
| Ships/aircraft in international traffic (Art 13(3)) | Taxable only in the state of effective management of the enterprise |
| Shares deriving value principally from immovable property (Art 13(4)) | May be taxed in the state where the property is situated |
| Other shares / securities (Art 13(5)) | Taxable only in the residence state of the alienator |

### Key practical points

- Art 13(4) is an anti-avoidance rule preventing the use of interposed entities to avoid taxation on real estate gains
- "Principally" means >50% of the share value derives from immovable property (in many treaties; wording varies)
- Art 13(5) means that a freelancer selling shares in a foreign company (that is NOT a property company) owes capital gains tax ONLY in their residence country — not in the company's country

### Historical note

Article 14 covered income from independent personal services (freelancers, professionals). It was deleted from the OECD Model in 2000 — such income is now covered by Article 7 (business profits).

### Why this still matters

Many existing bilateral treaties were concluded before 2000 and still contain Article 14. Under those treaties:

**Old Article 14 provisions and effects**  _(Old Art 14 (pre-2000 OECD Model))_

| Old Article 14 provision | Effect |
| --- | --- |
| Income taxable only in residence state UNLESS individual has a "fixed base" regularly available in the other state | Lower threshold than PE — a "fixed base" is easier to establish than a "fixed place of business" |
| If fixed base exists → income attributable to the fixed base taxable in that state | Similar to PE attribution but under different terminology |

### Why this still matters

**Check the specific treaty.** If it has an Article 14, apply it. If it doesn't (post-2000 treaties), apply Article 7.

### Model rule

- **Employment income taxation rule** — Employment income is taxable in the state where the employment is exercised — BUT a short-term exemption applies.  _(Art 15 OECD Model Tax Convention)_

### Short-term assignment exemption (Art 15(2))

**Short-term assignment exemption (Art 15(2))**  _(Art 15(2) OECD Model Tax Convention)_

| Condition | Requirement |
| --- | --- |
| **Days** | Employee is present in State B for not more than **183 days** in any 12-month period commencing or ending in the fiscal year concerned |
| **Employer** | Remuneration is paid by, or on behalf of, an employer who is NOT a resident of State B |
| **PE not bearing cost** | Remuneration is NOT borne by a PE which the employer has in State B |

- **All three conditions must be met** — All three must be met. If any one fails, State B may tax the employment income.  _(Art 15(2) OECD Model Tax Convention)_

### 183-day counting

- **183-day counting rules** — The OECD Model uses a "12-month period" (rolling, not calendar year). Many actual treaties use "calendar year" or "fiscal year" instead — check the specific treaty. "Days of presence" includes days of arrival, departure, weekends, holidays, sick days, and any other day spent in the country (not just working days). A fraction of a day counts as a full day of presence.  _(Art 15 OECD Model Tax Convention)_

### Practical example

UK employee sent to Germany for a project:
- Present 150 days in a 12-month period ✓ (< 183)
- Paid by UK employer (not German resident) ✓
- UK employer has no German PE ✓
→ Germany cannot tax. Only UK taxes.

If any condition fails (e.g., employee is present 190 days), Germany may tax the employment income earned there.

### The problem

When both the residence state and source state have taxing rights (e.g., source state taxes under Art 13(1) for immovable property gains, and residence state taxes worldwide income), double taxation occurs.

### Two methods

**Two methods**  _(Art 23A/23B OECD Model Tax Convention)_

| Method | Article | How it works | Effect |
| --- | --- | --- | --- |
| **Exemption method** | 23A | Residence state exempts the income that the source state may tax (often with progression — the exempt income affects the rate applied to other income) | Income taxed only once, at the source-state rate |
| **Credit method** | 23B | Residence state taxes worldwide income but grants a credit for the tax paid in the source state | Income taxed at the higher of the two rates |

### Credit method — practical mechanics

- **Credit method mechanics** — 1. Residence state computes tax on worldwide income (including the foreign-source income) 2. Residence state allows a credit equal to the tax paid in the source state 3. Credit is limited to the amount of residence-state tax attributable to the foreign income (no excess credit refund) 4. Excess foreign tax (where source-state rate > residence-state rate) is a real cost — not recoverable  _(Art 23B OECD Model Tax Convention)_

### Which method do countries use?

**Which method do countries use?**

| Method | Countries typically using |
| --- | --- |
| Exemption (for business profits/employment) | Germany, France, Netherlands, Belgium, Austria, Luxembourg |
| Credit (general) | US, UK, Japan, Canada, Australia, India, Singapore |
| Mixed (exemption for some, credit for others) | Most EU countries (exemption for active income, credit for passive income) |

### Practical significance

- **Exemption countries** (e.g., Germany): If you pay 10% WHT in India on consulting fees, and Germany exempts the Indian income → your effective rate on that income is 10% (only India taxes)
- **Credit countries** (e.g., UK): If you pay 10% WHT in India, and UK rate on the income would be 40% → UK taxes at 40% but gives a 10% credit → effective rate is 40% (you pay 10% to India + 30% to UK)

### When MAP applies

- **When MAP applies** — - Taxation not in accordance with the treaty - Difficulties in interpretation or application - Elimination of double taxation not otherwise provided for  _(Art 25 OECD Model Tax Convention)_

### Process

- **MAP process steps** — 1. **Taxpayer initiates:** Present case to competent authority of residence state within 3 years of first notification of the taxation 2. **Competent authority attempts resolution:** If it cannot resolve unilaterally, it shall endeavour to resolve by mutual agreement with the other state 3. **No obligation to reach agreement:** Under the standard OECD Model, there is no mandatory binding arbitration 4. **Mandatory binding arbitration (Art 25(5)):** Added in 2008 update — if competent authorities cannot resolve within 2 years, either state may submit to arbitration. NOT all treaties include this.  _(Art 25 OECD Model Tax Convention)_

### Timeline expectations

**Timeline expectations**  _(Art 25 OECD Model Tax Convention)_

| Phase | Typical duration |
| --- | --- |
| Filing MAP request | Within 3 years of adverse tax action |
| Competent authority initial review | 3–6 months |
| Inter-state negotiation | 12–36 months |
| Arbitration (if applicable) | Additional 6–12 months |
| **Total MAP resolution** | **18–48 months** typical |

### OECD Model default rates (what the Model Convention says)

**OECD Model default rates**  _(OECD Model Tax Convention Articles 7, 10, 11, 12, 13, 15, 18, 19)_

| Income type | Source state right | Residence state right |
| --- | --- | --- |
| Business profits (Art 7) | 0% (unless PE) | Full taxation |
| Dividends — portfolio (Art 10(2)(b)) | Max 15% WHT | Full (with credit/exemption) |
| Dividends — substantial holding ≥25% (Art 10(2)(a)) | Max 5% WHT | Full (with credit/exemption) |
| Interest (Art 11) | Max 10% WHT | Full (with credit/exemption) |
| Royalties (Art 12) | **0% (exclusive residence)** | Full taxation |
| Capital gains — immovable (Art 13(1)) | Full taxation | Credit/exemption |
| Capital gains — shares (Art 13(5)) | 0% | Full taxation |
| Employment income (Art 15) | Full if >183 days or local employer/PE | Full (with credit/exemption) |
| Pensions (Art 18) | 0% | Full taxation |
| Government service (Art 19) | Full (paying state) | Exempt (unless national of residence state) |

### What countries typically negotiate (deviations from OECD Model)

**What countries typically negotiate (deviations from OECD Model)**

| Provision | OECD default | Common treaty deviation |
| --- | --- | --- |
| Royalties | 0% source | 5–15% source WHT (especially with developing countries) |
| Interest | 10% source | 0–15% (many developed-country treaties achieve 0%) |
| Dividends (portfolio) | 15% source | 10–15% (some achieve 0% for pension funds) |
| Dividends (substantial) | 5% source | 0–5% (EU PSD achieves 0% without treaty) |
| Construction PE | 12 months | 6–9 months in many treaties |
| Service PE | Not in OECD Model | 90–183 days (in UN-model influenced treaties) |
| Art 14 (independent services) | Deleted (2000) | Still present in pre-2000 treaties |
| Arbitration (Art 25(5)) | Optional | Increasingly included in newer treaties |

## Section 11 — UN Model differences

The UN Model Tax Convention deviates from the OECD Model to preserve source-state taxing rights for developing countries.

## Section 11 — UN Model differences

**UN Model differences table**  _(UN Model Double Taxation Convention (2021 update))_

| Article | OECD Model | UN Model Difference |
| --- | --- | --- |
| Art 5 (PE) | No service PE | **Service PE at 183 days in 12 months** (Art 5(3)(b)) — service PE triggered by furnishing services through employees or other personnel |
| Art 12 (Royalties) | 0% source (exclusive residence) | **Source state MAY tax** royalties — rate negotiated bilaterally |
| Art 12A (Fees for Technical Services) | Does not exist | **NEW article** — source state may tax fees for technical services (added 2017 UN update). Rate negotiated. |
| Art 13 (Capital Gains) | Only immovable + PE assets in source | **Broader source-state rights** on share sales |
| Art 14 (Independent Services) | Deleted | **Retained** — allows source taxation if individual has a "fixed base" OR is present >183 days |

### Practical impact

When a freelancer in a developed country (e.g., UK) works for a client in a developing country (e.g., India), the treaty between them is likely UN-model influenced — meaning:
- Service PE thresholds are lower (90 days in India's treaties)
- Source-state WHT on services may apply (India: 10% on technical/professional services)
- Article 12A (fees for technical services) may give India taxing rights even without PE

Always check the specific bilateral treaty to determine which model it follows.

### Interaction with `withholding-tax-matrix.md`

The WHT matrix provides specific rates for specific country pairs. This skill provides the default OECD framework. When they interact:
- Treaty rates in the WHT matrix override the OECD Model defaults (because they are the actual negotiated rates)
- For country pairs NOT in the WHT matrix, use the OECD Model default as the starting assumption, then verify against the actual treaty text

### Interaction with `permanent-establishment-risk.md`

The PE risk skill provides practical assessment guidance. This skill provides the treaty-law framework (Art 5 definition). When they interact:
- Use Article 5 from this skill for the legal test
- Use the PE risk skill for practical risk assessment and country-specific thresholds

### Interaction with `tax-residency-planning.md`

The residency planning skill provides country-specific domestic rules. This skill provides the treaty tie-breaker (Art 4(2)). When they interact:
- Country skill determines whether domestic law claims the person as resident
- If two countries BOTH claim → this skill's Art 4(2) cascade applies

### Interaction with `cross-border-workflow-base.md`

The orchestrator calls this skill in Steps 4, 5, and 7 of the cross-border workflow:
- Step 4 (residency): Art 4 tie-breaker
- Step 5 (PE assessment): Art 5 definition
- Step 7 (WHT): Art 10–12 default rates

## PROHIBITIONS

- **Prohibitions list** — 1. NEVER assume a specific bilateral treaty matches the OECD Model exactly. All treaties are negotiated and many deviate significantly. 2. NEVER apply Article 14 (independent services) unless the specific treaty still contains it. It was deleted from the OECD Model in 2000. 3. NEVER assume the 183-day rule uses a "12-month period" — many treaties use "calendar year" or "fiscal year." 4. NEVER ignore the 2017/2025 updates when interpreting PE risk — the anti-fragmentation rule and remote-work Commentary are critical for modern work arrangements. 5. NEVER assume royalties are 0% in the source state without checking the specific treaty. The OECD Model says 0%, but most actual treaties allow some source WHT. 6. NEVER advise that MAP resolves quickly. Typical timeframes are 18–48 months. 7. NEVER treat the OECD Model as binding law. It is a template that countries use to negotiate bilateral treaties. The treaty itself is the law.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. Treaty interpretation is complex and fact-specific; the actual bilateral treaty text governs, not the OECD Model. All outputs must be reviewed and signed off by a qualified international tax professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability on either side until you and the accountant sign a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

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
