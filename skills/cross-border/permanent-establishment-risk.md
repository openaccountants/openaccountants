---
name: permanent-establishment-risk
description: Use this skill whenever a freelancer or small business has cross-border activity that might create a tax presence (Permanent Establishment / PE) in the client's country. Trigger on phrases like "permanent establishment", "PE risk", "tax presence", "183-day rule", "fixed place of business", "dependent agent", "service PE", "effectively connected income", "do I need to file taxes in my client's country", "working abroad for client", "remote work PE", or any request about whether a freelancer's cross-border activity triggers a filing obligation in another country. This skill contains the OECD model treaty PE definition, country-specific PE thresholds, the 183-day rule, remote work analysis, avoidance strategies, and consequences of PE creation. This is primarily T2/T3 material -- flag for professional review in all but the most straightforward cases. ALWAYS read this skill before advising on any PE-related question.
---

# Permanent Establishment Risk for Cross-Border Freelancers

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Multi-jurisdiction (OECD model + country-specific) |
| Primary Legislation | OECD Model Tax Convention on Income and on Capital, Article 5 (PE definition), Article 7 (business profits), Article 14 (independent personal services -- deleted in 2000 update, now subsumed by Art 7) |
| Supporting Legislation | UN Model Tax Convention Art 5 (broader PE definition, includes service PE); bilateral DTAs between specific country pairs |
| Scope | Whether a freelancer's cross-border activity creates a PE in the client's country, triggering a corporate/income tax filing obligation there |
| Contributor | OpenAccountants |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: basic PE definition, remote work non-PE, clearly short visits. Tier 2: extended on-site presence, service PE under UN model treaties, borderline fixed place situations. Tier 3: multi-country PE assessment, profit attribution, anti-avoidance rules, actual PE triggered -- full professional review required. |
| Cross-references | `withholding-tax-matrix.md`, `non-eu-export-services.md` |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a qualified international tax professional.

---

## Step 0: Pre-Check Questions [T1]

1. **Where is the freelancer tax-resident?** Home country for treaty purposes.
2. **Where is the client located?** The potential PE country.
3. **Does the freelancer travel to the client's country?** If yes: how many days per year? Do they have a fixed office/desk there?
4. **Does the freelancer work entirely remotely from their home country?** If yes, PE risk is generally very low.
5. **Does a double tax treaty (DTA) exist between the two countries?** The treaty PE definition overrides domestic law.
6. **Does the freelancer have authority to conclude contracts on behalf of the client?** Dependent agent PE risk.
7. **How long has the arrangement lasted or is expected to last?**

**If items 1-4 are unknown, STOP.**

---

## Step 1: What Constitutes a Permanent Establishment? [T1]

**Legislation:** OECD Model Tax Convention, Article 5.

### OECD Model Definition (Art 5(1))

A PE is a **fixed place of business** through which the business of an enterprise is wholly or partly carried on.

### The Three Tests [T1]

| Test | Requirement | Freelancer Application |
|------|-------------|----------------------|
| **Place of business** | A physical location: office, room, desk, workstation, construction site | Does the freelancer have an office, desk, or other fixed location in the client's country? |
| **Fixed** | The place must be established at a distinct location with a degree of permanence (not merely temporary) | Is the location available to the freelancer on a continuing basis (not just for a single short visit)? |
| **Business carried on through it** | The enterprise's business activities must be carried on through the fixed place | Does the freelancer actually perform their core service activities at this location? |

**All three must be met for a PE to exist under Art 5(1).**

### Specific PE Examples (Art 5(2)) [T1]

The following are expressly included as PEs if they meet the general definition:

- A place of management
- A branch
- An office
- A factory
- A workshop
- A mine, oil well, quarry, or other place of extraction

### Exclusions -- NOT a PE (Art 5(4)) [T1]

The following do NOT create a PE even if they involve a fixed place:

| Exclusion | Example |
|-----------|---------|
| Storage, display, or delivery of goods | Freelancer stores samples at client's warehouse |
| Maintenance of stock for processing by another | N/A for most service freelancers |
| Purchasing goods or collecting information | Freelancer visits client to gather requirements (no service delivery) |
| Preparatory or auxiliary activities | Administrative tasks, attending planning meetings |

**IMPORTANT:** The BEPS Action 6/7 anti-fragmentation rule (Art 5(4.1) of the 2017 OECD Model) may deny these exclusions if the overall activity is NOT preparatory or auxiliary. [T3]

---

## Step 2: Dependent Agent PE (Art 5(5)-(6)) [T2]

Even without a fixed place, a PE can be created through a **dependent agent:**

| Condition | Test |
|-----------|------|
| A person acts on behalf of the enterprise | The freelancer (or their employee/sub-contractor) acts in the client's country |
| Habitually concludes contracts | The person has authority to conclude contracts in the name of the enterprise AND habitually exercises it |
| Contracts are in the name of the enterprise | The contracts are binding on the enterprise |

### Does NOT Create Agent PE [T1]

- An **independent agent** (broker, general commission agent) acting in the ordinary course of their business.
- A person who merely **promotes or advertises** but does not conclude contracts.
- A freelancer who performs services under their own name and contract (i.e., the freelancer IS the enterprise, not an agent of the client).

**For most freelancers:** Agent PE is NOT a significant risk because the freelancer contracts in their own name, not the client's. However, if a freelancer is embedded in a client's team and signs deals on the client's behalf, agent PE risk increases. [T2]

---

## Step 3: The 183-Day Rule [T1]

### OECD Model -- Employment Income (Art 15)

The 183-day rule in the OECD Model applies to **employees**, not independent freelancers. However, many countries and treaties extend similar concepts to independent service providers.

**Standard employment rule (Art 15(2)):** Employment income is taxable ONLY in the employee's residence country if:
1. The employee is present in the other country for not more than 183 days in any 12-month period, AND
2. The remuneration is paid by an employer NOT resident in the other country, AND
3. The remuneration is NOT borne by a PE of the employer in the other country.

### For Freelancers -- Service PE Under UN Model [T2]

**Legislation:** UN Model Tax Convention, Art 5(3)(b).

Many treaties (especially those involving developing countries like India, Brazil, and countries in Africa/Asia) include a **service PE** provision:

> An enterprise shall be deemed to have a PE if it furnishes services through employees or other personnel in the other country, if such activities continue for a period exceeding **183 days** (or a shorter period in some treaties) within any 12-month period.

| Treaty Type | Service PE Threshold | Countries Using This |
|-------------|---------------------|---------------------|
| OECD Model (standard) | No service PE provision | Most developed-country treaties |
| UN Model | 183 days in 12 months | India, Brazil, many developing countries |
| India treaties | 90 days in many treaties | India-specific (see Step 5) |
| US domestic law | Any day of presence may count ("effectively connected income") | US -- see Step 5 |

---

## Step 4: Remote Work and PE [T1]

### The Core Question

**Does working remotely from your home country for a foreign client create a PE in the client's country?**

### Answer: Generally NO [T1]

| Factor | Analysis |
|--------|----------|
| Fixed place of business | The freelancer's office is in their HOME country, not the client's country. No fixed place exists in the client's country. |
| Physical presence | The freelancer does not travel to the client's country. No presence = no PE. |
| Dependent agent | The freelancer is not an agent of the client and does not conclude contracts in the client's country. |
| Conclusion | **Pure remote work from the freelancer's home country does NOT create a PE in the client's country.** |

### Exceptions / Risks [T2]

| Scenario | PE Risk Level | Notes |
|----------|--------------|-------|
| 100% remote, never visits client's country | **None** | Clearly no PE |
| Visits client's country 1-2 times/year for meetings (< 2 weeks total) | **Very low** | Preparatory/auxiliary, temporary visits |
| Visits client's country regularly, 1-2 days/month | **Low** | No fixed place, but pattern of presence may attract scrutiny in aggressive jurisdictions |
| Works at client's office 1-2 months/year | **Medium** | Approaching fixed place + permanence. Check treaty threshold. [T2] |
| Has a dedicated desk at client's office, visits 3+ months/year | **High** | Likely meets fixed place + permanence + business carried on. PE probable. [T2] |
| Relocates to client's country for 6+ months | **Very high** | Almost certainly creates PE (and likely tax residency shift). [T3] |

---

## Step 5: Country-Specific PE Thresholds and Rules [T2]

### United States [T2]

| Rule | Detail |
|------|--------|
| Domestic law | US taxes foreign persons on "effectively connected income" (ECI) -- income connected with a US trade or business. Even a single day of business activity in the US COULD create ECI. |
| Treaty override | Most US treaties include an Art 5 PE definition. Without a PE, business profits are exempt. |
| Key threshold | OECD-standard 183-day rule for employees; no specific service PE for independent contractors under most US treaties. BUT: US domestic law is aggressive -- if no treaty exists, any US-source business income may be taxed. |
| Form required | If PE exists: file Form 1120-F (corporations) or Form 1040-NR (individuals). |
| Practical risk for freelancers | A freelancer who works entirely remotely from outside the US for a US client has NO PE risk. A freelancer who works on-site at a US client's office for extended periods may create a PE. |

### India [T2]

| Rule | Detail |
|------|--------|
| Domestic law | India taxes non-residents on income that "accrues or arises in India." Services performed in India trigger Indian tax. |
| Treaty provision | Many Indian treaties include a **90-day service PE** (shorter than the standard 183 days). India-US treaty: service PE at 90 days in a fiscal year. India-UK treaty: 90 days. |
| Key threshold | 90 days in many treaties (check specific treaty). |
| Practical risk | A freelancer who visits India for a project exceeding 90 days in a year will likely trigger a service PE. Remote work from outside India: no PE. |
| Note | India also imposes WHT on service fees (see `withholding-tax-matrix.md`), which is SEPARATE from PE. WHT applies even without PE. |

### United Arab Emirates [T1]

| Rule | Detail |
|------|--------|
| Domestic law | UAE federal corporate tax (effective June 2023) applies to businesses with a PE or nexus in the UAE. BUT: 0% rate for taxable income up to AED 375,000; 9% thereafter. No personal income tax. |
| Treaty provision | UAE has treaties with many countries. PE defined per OECD model. |
| Practical risk | **Minimal.** Even if PE exists, the tax rate is 0% (below AED 375,000) or 9%. For a freelancer earning below the threshold, PE is irrelevant. No personal income tax in UAE. |

### Germany [T2]

| Rule | Detail |
|------|--------|
| Domestic law | Non-residents are taxed on income from a PE in Germany (Betriebsstätte). |
| Treaty provision | Standard OECD Art 5 PE. No service PE in most German treaties. |
| Key threshold | 6 months for construction PE. No specific day count for services in OECD-model treaties. |
| Practical risk | Low for remote freelancers. Medium if working on-site in Germany for extended periods. A desk at a German client's office for 6+ months = likely PE. |

### United Kingdom [T2]

| Rule | Detail |
|------|--------|
| Domestic law | Non-residents taxed on UK-source trading income if they have a PE in the UK. |
| Treaty provision | Standard OECD Art 5. No service PE in most UK treaties. |
| Practical risk | Low for remote work. Medium-high if freelancer has a UK office or works at client's premises for extended periods. |

### Australia [T2]

| Rule | Detail |
|------|--------|
| Domestic law | Non-residents taxed on Australian-source income. A PE creates a tax presence. |
| Treaty provision | Standard OECD Art 5 in most treaties. Some treaties (e.g., Australia-India) include service PE at 183 days. |
| Practical risk | Low for remote. Medium if on-site 3+ months. |

### Singapore [T1]

| Rule | Detail |
|------|--------|
| Domestic law | Non-residents taxed on Singapore-source income. PE defined under s2 of the Income Tax Act. |
| Treaty provision | Standard OECD Art 5. Some treaties include service PE. |
| Practical risk | Low. Singapore is generally business-friendly and does not aggressively pursue PE claims against short-term visitors. |

---

## Step 6: How to Avoid PE [T1]

| Strategy | How It Helps |
|----------|-------------|
| **Work remotely from your home country** | No physical presence = no PE. This is the strongest protection. |
| **Limit travel to the client's country** | Keep visits short (under 2 weeks) and infrequent. Avoid patterns of regular presence. |
| **Do NOT have a fixed office/desk in the client's country** | Use meeting rooms, hotel lobbies, co-working spaces for short visits. Do not accept a dedicated desk. |
| **Do NOT sign contracts on behalf of the client** | Sign only in your own name, from your own country. Avoid authority to bind the client. |
| **Keep visits preparatory/auxiliary** | Meetings, planning sessions, and requirement gathering are preparatory. Do not deliver core services on-site if avoidable. |
| **Monitor cumulative days** | Track days spent in each country per calendar year (and per 12-month rolling period for treaties using that measure). |
| **Contract structure** | Contract directly with the client from your home country. Invoice from your home country. Maintain your home country business registration. |

---

## Step 7: What Happens If PE IS Triggered [T3]

**This section is entirely T3. If PE is triggered, the freelancer MUST engage a qualified tax professional in BOTH countries. Do not attempt to self-resolve.**

### General Consequences

| Consequence | Detail |
|-------------|--------|
| **Register for tax in the PE country** | File with the local tax authority. Obtain a tax identification number. |
| **File a local tax return** | Report profits attributable to the PE. Profit attribution follows the "separate entity" principle (OECD Art 7). |
| **Pay local income/corporate tax** | On the portion of profits attributable to activities performed through the PE. |
| **Claim treaty credit in home country** | The home country taxes worldwide income but grants a credit for tax paid in the PE country under the treaty (Art 23A or 23B). Avoid double taxation. |
| **VAT/GST registration may be required** | PE may trigger VAT/GST registration in the PE country (separate from income tax). |
| **Potential penalties for late registration** | If PE existed for prior periods and was not reported, penalties and interest may apply. Voluntary disclosure may mitigate penalties. |

### Profit Attribution to PE [T3]

Under OECD Art 7, the profits attributable to a PE are those that the PE would have earned if it were a **separate and independent enterprise** performing the same functions, using the same assets, and assuming the same risks.

**This is complex.** For a freelancer, the attribution might be based on:
- Days worked in the PE country vs total days worked
- Revenue from clients in the PE country
- Functions performed at the PE

**Escalate to a tax professional. Do not compute.**

---

## PROHIBITIONS

1. **NEVER** tell a freelancer that PE is "nothing to worry about" when they are spending significant time in a foreign country. PE risk is real and the consequences are material.
2. **NEVER** attempt to compute profit attribution to a PE. This is T3 material requiring professional input.
3. **NEVER** assume that a treaty exists between two countries. Verify.
4. **NEVER** assume that the OECD 183-day threshold applies universally. Many treaties (especially UN-model treaties with developing countries) use 90 days or other thresholds.
5. **NEVER** ignore domestic law. Even if a treaty protects against PE, domestic anti-avoidance rules may override treaty provisions in some countries.
6. **NEVER** advise a freelancer that remote work from Country A while physically present in Country B does not create risk in Country B. Physical presence in Country B creates risk in Country B, regardless of where the client is.
7. **NEVER** conflate PE risk with WHT. A country can impose WHT on service fees (see `withholding-tax-matrix.md`) WITHOUT PE, and PE can exist WITHOUT WHT.

---

## Edge Cases

### EC1 -- Digital nomad working from multiple countries [T3]
**Situation:** A freelancer works from Portugal for 3 months, then Thailand for 3 months, then Bali for 3 months, serving clients in the US, UK, and Australia.
**Resolution:** Each country where the freelancer is physically present may assert taxing rights on income earned while present there, depending on domestic law and treaty provisions. This is a complex multi-jurisdiction question involving tax residency, PE, and source rules in each country. Escalate to an international tax professional. Do not advise.

### EC2 -- Freelancer's employee works at client's premises [T2]
**Situation:** A freelancer hires a subcontractor who works on-site at the client's office in another country for 6 months.
**Resolution:** Under Art 5(5)-(6) and the service PE provisions in some treaties, the subcontractor's presence may create a PE for the freelancer's enterprise. The key question is whether the subcontractor habitually exercises authority to conclude contracts. If they simply perform technical work without contract authority, PE risk is lower but service PE thresholds still apply. Flag for review.

### EC3 -- Client provides equipment (laptop, desk, badge) [T2]
**Situation:** A freelancer visits a client's office and is given a badge, a desk, and a company laptop for the duration of a 2-month project.
**Resolution:** Having a dedicated desk and badge increases "fixed place" risk. If the desk is available for the freelancer's exclusive use on a continuing basis, this weighs toward PE. However, 2 months alone may not meet the "permanence" requirement in many jurisdictions. The overall picture matters. Flag for review.

### EC4 -- Construction site supervision abroad [T2]
**Situation:** A freelance engineer supervises a construction project in another country for 10 months.
**Resolution:** OECD Art 5(3) provides a specific construction PE rule: a building site or construction/installation project constitutes a PE only if it lasts more than 12 months (some treaties use 6 months). At 10 months, this may or may not exceed the treaty threshold. Check the specific treaty. Flag for review.

### EC5 -- Country with no income tax (UAE, Bahamas) [T1]
**Situation:** A freelancer creates a PE in the UAE (e.g., has an office there for 8 months serving local clients).
**Resolution:** UAE corporate tax applies at 0% for income up to AED 375,000 and 9% above that. For small freelancers, the tax impact may be negligible. There is no personal income tax. PE risk is technically present but practically inconsequential for low earners. For larger operations, 9% corporate tax applies and filing is required. No personal income tax countries (e.g., Bahamas, Cayman Islands) have no PE consequence from an income tax perspective (but other regulatory obligations may exist).

---

## Test Suite

### Test 1 -- Pure remote, no travel
**Input:** UK freelancer works 100% remotely from London for a US client. Never visits the US.
**Expected:** No PE risk in the US. No filing obligation in the US. US does not withhold on service fees.

### Test 2 -- Short business visits
**Input:** Maltese developer visits client's office in Germany for 5 days twice a year (10 days total). No dedicated desk. Meetings and planning only.
**Expected:** No PE risk. Visits are short, temporary, and preparatory/auxiliary. No filing obligation in Germany.

### Test 3 -- Extended on-site, India (90-day service PE)
**Input:** Australian consultant works on-site at an Indian client's office for 100 days in a 12-month period. India-Australia treaty includes a 90-day service PE.
**Expected:** Service PE likely triggered (100 days > 90-day threshold). Flag T2/T3. Australian consultant should engage an Indian tax advisor. Must file Indian return and pay Indian tax on attributable profits. Claim credit in Australia.

### Test 4 -- Dedicated desk at client's office, 4 months
**Input:** French designer works at a Dutch client's Amsterdam office 4 days/week for 4 months. Has a dedicated desk and building pass.
**Expected:** PE risk is MEDIUM-HIGH. Fixed place (dedicated desk), permanence (4 months), business carried on through it (core design work). Under the France-Netherlands treaty (OECD model), this may constitute a PE. Flag T2. Professional review required.

### Test 5 -- UAE client, no income tax
**Input:** Indian freelancer has a fixed office in Dubai, works there 6 months/year serving UAE and India clients.
**Expected:** PE exists in UAE. UAE corporate tax applies (0% up to AED 375,000, 9% above). Minimal tax impact for small freelancers. No personal income tax. Indian tax on worldwide income still applies; claim credit for any UAE tax paid.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. Permanent establishment analysis is inherently fact-specific and depends on the precise terms of the applicable bilateral tax treaty. All PE assessments must be reviewed by a qualified international tax professional before acting upon.

If you would like a licensed accountant to review your PE risk, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
