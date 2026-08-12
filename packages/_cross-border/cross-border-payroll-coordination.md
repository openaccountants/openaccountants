---
name: cross-border-payroll-coordination
description: "Cross-border payroll compliance for companies with employees or contractors in multiple countries. Use when the user asks about: cross-border payroll, remote worker payroll, shadow payroll, hypothetical tax, employer of record, EOR, 183-day rule, economic employer, PE risk from employees, A1 certificate, social security certificate, bilateral social security, posted worker, business traveler tax, contractor vs employee cross-border, misclassification, equity compensation cross-border, RSU cross-border, stock options international, payroll obligations foreign employee, remote worker abroad, digital nomad payroll, cross-border withholding, or any question about payroll compliance when workers cross borders."
version: 1.0
jurisdiction: INTL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cross Border Payroll Coordination

## Cross-Border Payroll Coordination

> **Disclaimer:** This skill provides general guidance on cross-border payroll obligations. Employment law, tax, and social security rules are jurisdiction-specific and change frequently. Consult qualified employment tax and legal advisors before acting on this information.

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Multi-jurisdiction (EU, UK, US, Australia, India, Singapore, and general principles) |
| Primary Legislation | OECD Model Tax Convention Art 15; EU Regulation 883/2004 (social security coordination); country-specific employment and tax laws |
| Scope | Payroll tax, social security, and employment law obligations when employees or contractors work across borders |
| Contributor | OpenAccountants |
| Validation Date | May 2026 |
| Skill Version | 1.0 |
| Cross-references | `non-eu-export-services.md`, `permanent-establishment-risk.md`, country-specific payroll skills |

## Section 1: When Does a Foreign Employee Create Payroll Obligations?

### The Core Question [T1]

If your company is in Country A and you hire someone who works in Country B, you may owe:

**Obligations triggered table**

| Obligation | Triggered by |
| --- | --- |
| **Income tax withholding** in Country B | Employee performing work in Country B (subject to treaty exemptions) |
| **Social security contributions** in Country B | Employee working in Country B (subject to A1/bilateral agreements) |
| **Employment law compliance** in Country B | Employment relationship with a person habitually working in Country B |
| **Corporate tax (PE risk)** in Country B | Employee's activities may create a permanent establishment for the employer |

### Three Approaches to Employing Abroad [T1]

**Three approaches table**

| Approach | How It Works | When to Use |
| --- | --- | --- |
| **Set up a local entity** | Establish a subsidiary or branch in Country B. Full local payroll. | Long-term, multiple employees, need full legal presence |
| **Employer of Record (EOR)** | Third-party company becomes the legal employer in Country B. You manage the work; EOR handles payroll, tax, social security. | 1–10 employees, speed, no local entity desired. Cost: $300–$700/employee/month. |
| **Direct employment (no local entity)** | You employ the person from Country A. Run payroll from Country A + shadow payroll or local registration in Country B. | Single employee, short-term. High compliance risk — not recommended without expert advice. |

### PE Risk from Employees [T2]

An employee working in Country B can create a **permanent establishment** for the employer, triggering corporate tax in Country B:

**PE trigger table**

| PE Trigger | Risk Level |
| --- | --- |
| Employee has authority to conclude contracts on behalf of employer | **High** — "dependent agent" PE under OECD Art 5(5) |
| Employee works from a fixed location (home office) regularly | **Medium** — "fixed place of business" PE if employer consents to arrangement |
| Employee performs auxiliary activities only (e.g., market research) | **Low** — typically excluded under Art 5(4) |
| Employee works from Country B for >6 months on a project | **High** — construction/service PE threshold in many treaties |

## Section 2: Remote Worker Scenarios

### Employee in Country B, Employer in Country A [T1]

**Remote worker scenarios table**

| Scenario | Tax Obligation | Social Security | Action Required |
| --- | --- | --- | --- |
| Short-term (<183 days, treaty conditions met) | Likely exempt from Country B tax | Country A (with A1/certificate) | Obtain social security certificate. Monitor day count. |
| Long-term (>183 days or treaty conditions not met) | Country B income tax withholding required | Country B (unless A1 applies) | Register for payroll in Country B or use EOR. Shadow payroll may be needed. |
| Permanent relocation to Country B | Full Country B tax and employment law | Country B | Establish local payroll. Update employment contract. |
| Digital nomad (moves between countries) | Depends on days in each country | Complex — may require multi-state determination | Track workdays meticulously. Assess each country's rules. |

### Practical Checklist for Remote Workers Abroad [T1]

1. **Before the employee starts working from Country B:**
   - Assess PE risk in Country B
   - Check tax treaty between Country A and Country B
   - Determine social security obligations (A1 if EU/EEA)
   - Review immigration/work permit requirements
   - Check Country B employment law implications (minimum wage, termination rules, benefits)

2. **During the arrangement:**
   - Track workdays in each country (use timesheets or travel records)
   - File required social security certificates
   - Run shadow payroll if needed (see Section 4)

3. **Common employer policies:**
   - Many companies limit remote work abroad to 30–90 days/year to avoid triggering obligations
   - Some companies maintain a list of "approved" vs "prohibited" countries

## Section 3: Short-Term Business Travelers

### The 183-Day Rule — OECD Model Art 15(2) [T1]

The "183-day rule" is the most cited — and most misunderstood — rule in cross-border employment tax. It provides an **exemption** from host-country tax, NOT an automatic right.

**All three conditions must be met for the exemption to apply:**

**Three conditions table**

| Condition | Requirement |
| --- | --- |
| (a) Days present | The employee is present in the host country for ≤183 days in the relevant period |
| (b) Employer not resident | The remuneration is paid by, or on behalf of, an employer who is NOT a resident of the host country |
| (c) Not borne by PE | The remuneration is NOT borne by a permanent establishment the employer has in the host country |

- **Condition failure consequence** — If ANY condition fails → host-country tax applies from day one.  _(OECD Model Art 15(2))_

### Counting the 183 Days [T1]

**Counting the 183 days table**

| Treaty Version | Counting Period | Days Counted |
| --- | --- | --- |
| OECD Model (current) | Any 12-month period starting or ending in the fiscal year | Days of physical presence (including arrival, departure, weekends, holidays, sick days) |
| Older treaties | Calendar year or fiscal year | Same |

### The Economic Employer Concept [T2]

Many countries now look beyond the formal employer to the **substance** of the relationship:

**Economic employer factors table**

| Factor | Question |
| --- | --- |
| Supervision | Who directs and controls the employee's daily work? |
| Risk | Who bears the risk of the employee's work product? |
| Integration | Is the employee integrated into the host entity's organisation? |
| Cost reallocation | Is the home entity cross-charging the employee's cost to the host entity? |

- **Economic employer effect on condition (b)** — If the host entity is the "economic employer," condition (b) of Art 15(2) fails — even if the employee is formally employed and paid by the home entity. Host-country tax withholding is then required from day one.  _(OECD Model Art 15(2))_

Countries actively applying economic employer concepts: **Germany, Sweden, Denmark, Norway, Finland, UK, Australia, India, Singapore.**

### Business Traveler Compliance Matrix [T1]

**Business traveler compliance matrix**

| Days in Host Country | Treaty Exemption Likely? | Recommended Action |
| --- | --- | --- |
| 1–30 days/year | Usually exempt | Track days. Obtain A1 if EU. |
| 31–60 days/year | Usually exempt | Track days carefully. Check local de minimis rules. |
| 61–90 days/year | Likely exempt if treaty conditions met | Track days. Consider shadow payroll registration as precaution. |
| 91–183 days/year | Exempt only if ALL three conditions met | Formal assessment required. Shadow payroll likely needed. |
| >183 days/year | Condition (a) fails — host tax applies | Full payroll registration in host country. |

## Section 4: Shadow Payroll / Hypothetical Tax

### What Is Shadow Payroll? [T1]

- **Shadow payroll** — Shadow payroll is a **parallel payroll record** in the host country that calculates and remits host-country income tax and (sometimes) social security, while the employee continues to be paid through home-country payroll.

**Home vs shadow payroll comparison table**

| Element | Home Payroll | Shadow Payroll (Host) |
| --- | --- | --- |
| Salary payment | YES — employee is paid through home payroll | NO — no separate payment to employee |
| Tax withholding | May need adjustment (home country) | YES — calculates and remits host-country tax |
| Social security | Depends on A1/certificate | Depends on applicable legislation |
| Reporting | Home-country tax return | Host-country payroll filings |

### When Shadow Payroll Is Required [T1]

**Shadow payroll triggers table**

| Trigger | Example |
| --- | --- |
| Assignment exceeds treaty de minimis | Employee works 200 days in Germany but is paid from UK payroll |
| Cost recharged to host entity | US parent recharged employee cost to German subsidiary — condition (c) fails |
| Economic employer in host country | Swedish tax authority determines Swedish entity is the economic employer |
| Remote worker in a country with no employer entity | Employee relocates to Portugal; employer has no Portuguese entity but must withhold tax |

### Hypothetical Tax (Tax Equalisation) [T2]

**Tax equalisation concepts table**

| Concept | Explanation |
| --- | --- |
| Tax equalisation | Company ensures the employee pays no more (and no less) tax than they would have paid staying in their home country |
| Hypothetical tax | The home-country tax the employee "would have" paid — deducted from salary. Company pays the actual tax in both countries and absorbs any difference. |
| Tax protection | Employee pays actual taxes, but company reimburses if host-country tax exceeds what home-country tax would have been |

## Section 5: Social Security Certificates

### EU: A1 Certificate (Portable Document A1) [T1]

- **Legislation** — Legislation: Regulation (EC) No 883/2004, coordinated by Regulation (EC) No 987/2009.  _(Regulation (EC) No 883/2004; Regulation (EC) No 987/2009)_

**A1 certificate elements table**

| Element | Detail |
| --- | --- |
| Purpose | Proves which country's social security system applies, preventing double contributions |
| When needed | Any time a person works in an EU/EEA/Swiss country other than where they normally pay social security |
| Who applies | The employer or self-employed person, to the competent institution of the home country |
| Duration | Up to 24 months for posted workers (Art 12); renewable |
| Without A1 | The host country can demand social security contributions under its own rules |

### Key EU Social Security Rules [T1]

**Key EU social security rules table**

| Situation | Applicable Legislation |
| --- | --- |
| Posted worker (temporary, ≤24 months) | Home country (Art 12) — A1 required |
| Working in 2+ EU countries | Country of residence if ≥25% of activity there; otherwise employer's country (Art 13) |
| Teleworking (Multilateral Framework Agreement, 2023) | If 25–49.99% of working time in residence country, may remain under employer's country legislation |
| Self-employed person working temporarily in another EU state | Home country (Art 12(2)) — A1 required |

### 2026 Update

In April 2026, the EU reached a provisional agreement to modernize Regulation 883/2004:
- Proposed exemptions from A1 requirements for **short-term business trips**
- Initial A1 certificates can be issued for up to **24 months** subject to renewal
- Greater employer responsibility for documentation
- 24-month transitional period expected for certain elements

### Non-EU: Bilateral Social Security Agreements [T1]

**Bilateral social security agreements table**

| Countries | Agreement Covers |
| --- | --- |
| US–UK | Totalization agreement — prevents double social security |
| US–Germany, US–France, US–Italy, US–Japan | Same principle — worker pays into one system only |
| UK–EU (TCA Protocol) | 24-month posting limit; governed by Trade and Cooperation Agreement |
| Australia–numerous | Bilateral agreements with 30+ countries |
| India–select countries | Agreements with Germany, France, Belgium, Netherlands, and others |

- **No bilateral agreement risk** — Without a bilateral agreement: The employee may owe social security in both countries simultaneously — a potentially devastating cost for freelancers and small companies.

## Section 6: Contractor vs Employee Cross-Border

### The Misclassification Risk [T1]

- **Misclassification risk** — A worker can be a legitimate contractor under one country's law and a misclassified employee under another's. The host country's classification rules apply to work performed there, regardless of what the contract says.

### Classification Tests by Country [T1]

**Classification tests by country table**

| Country | Test | Key Factors |
| --- | --- | --- |
| **US** | Common-law (IRS) / ABC test (California AB5) | Behavioral control, financial control, type of relationship. CA: strict ABC test — B (outside usual course of business) is hardest to meet. |
| **UK** | IR35 off-payroll rules | Personal service, mutuality of obligation, control. Since April 2021, medium/large hirers determine status. |
| **Germany** | Deutsche Rentenversicherung | Integration into business, economic dependence, single-client >83% of income triggers mandatory pension |
| **France** | Code du Travail | Subordination link (lien de subordination) — fixed schedule, supervision, integration |
| **Netherlands** | DBA (Deregulering Beoordeling Arbeidsrelaties) | Enforcement moratorium lifted January 2025. Active auditing in 2026. |
| **Spain** | Estatuto de los Trabajadores | Reclassified contractors receive full employment rights retroactively |
| **Australia** | "Whole-of-relationship" test (Closing Loopholes reforms 2024) | Practical reality, not contract terms. Sham contracting penalties up to AUD 469,500. |
| **India** | Contract Labour (Regulation and Abolition) Act | Supervision, control, integration into principal employer's work |

### Penalties for Misclassification [T1]

**Penalties for misclassification table**

| Country | Penalty |
| --- | --- |
| Germany | Retroactive social security for 4 years (30 years if intentional); fines up to €500,000; criminal prosecution possible (§266a StGB) |
| France | Fines from €45,000; potential imprisonment for repeat offenders |
| UK | Employer pays back-tax, NICs, and penalties for IR35 failures |
| US (federal) | 20% of wages owed + 100% of unpaid FICA. California: $5,000–$25,000 per wilful violation |
| Netherlands | Retroactive corrections + penalties under resumed DBA enforcement |
| Australia | Up to AUD 469,500 per contravention + back superannuation + 6 years of back leave |
| Spain | Full retroactive employment rights (severance, paid leave, social security) |

### EU Platform Work Directive (2024/2831) [T1]

- **Platform Work Directive provisions** — Effective December 1, 2024. Member states must transpose by December 2, 2026: - Creates a rebuttable presumption of employment for platform workers - Platforms must rebut the presumption to maintain contractor status - Does not apply to tax, criminal, or social security proceedings (employment law only) - Member states will define penalties — must be "effective, dissuasive, and proportionate"  _(EU Platform Work Directive 2024/2831)_

## Section 7: Equity Compensation Cross-Border

### The Problem [T2]

When an employee receives stock options or RSUs and works in multiple countries during the vesting period, multiple countries may claim the right to tax the same income.

### Time-Based Apportionment Formula [T1]

- **Time-based apportionment formula** — Income sourced to Country X = (Days worked in Country X during vesting period ÷ Total days in vesting period) × Total vest value  _(Most jurisdictions and tax treaties)_

### Country-Specific Timing of Tax [T2]

**Country-specific timing of tax table**

| Country | RSUs Taxed At | Stock Options Taxed At | Character |
| --- | --- | --- | --- |
| US | Vesting | Exercise (NSO) or sale (ISO) | Ordinary income (RSU/NSO); capital gain (ISO at sale) |
| UK | Vesting | Exercise | Employment income; capital gains on sale |
| Germany | Vesting | Exercise | Employment income; Abgeltungsteuer on sale |
| France | Vesting (with qualified plan exceptions) | Exercise or sale (depending on plan) | Salary income + social charges; capital gains on sale |
| India | Vesting/allotment (perquisite) | Exercise (perquisite) | Salary income; capital gains on sale |
| Australia | Vesting (taxed upfront scheme) or sale (deferred scheme) | Exercise or sale | Employment income / capital gains |

### Double Taxation Relief [T2]

**Double taxation relief mechanisms table**

| Mechanism | How It Works |
| --- | --- |
| **Foreign Tax Credit** | Home country gives credit for tax paid abroad on the same equity income (limited to home-country tax on that income) |
| **Treaty allocation** | Tax treaty may allocate taxing rights based on where services were performed during vesting |
| **Tax equalisation** | Employer absorbs excess tax burden through hypothetical tax arrangement |

### Example: Employee Moves Mid-Vest [T2]

**Facts:** Employee granted 1,000 RSUs with 4-year vest. Works in Germany for years 1–2, then moves to UK for years 3–4. Vest value: €200,000.

**Apportionment table**

| Country | Apportionment | Taxable Amount |
| --- | --- | --- |
| Germany | 730 / 1,460 days = 50% | €100,000 at German income tax rates |
| UK | 730 / 1,460 days = 50% | £85,000 (converted) at UK income tax rates |

Both countries tax their portion. Employee claims Foreign Tax Credit in whichever country is the residence at vest to avoid double taxation. Coordination between German and UK advisors is essential.

## Section 8: Practical Scenarios

### Scenario 1 — Remote Developer, Employer US, Worker in Portugal [T1]

**Facts:** US tech company hires a developer who lives and works from Portugal. No EOR. No Portuguese entity.

**Issues:**
- Portugal requires income tax withholding on employment income earned there
- Portuguese social security contributions are owed (no US-Portugal totalization agreement)
- The developer's home office could create a PE for the US company in Portugal
- Portuguese employment law may apply (termination protections, minimum benefits)

**Recommendation:** Use an EOR in Portugal, or register the US company for Portuguese payroll. Do NOT ignore local obligations.

### Scenario 2 — Business Traveler, UK Employee Visits Germany 80 Days [T1]

**Facts:** UK employee travels to the German subsidiary for 80 days in a 12-month period.

**Assessment:**
- 80 days < 183 days ✓
- Paid by UK employer ✓
- BUT: Is cost recharged to German subsidiary? If yes, condition (c) fails.
- Does Germany apply economic employer concept? Yes — if German entity supervises and benefits, tax may be due from day one.

**Recommendation:** Assess economic employer status. If recharge exists, set up shadow payroll in Germany. Obtain A1 certificate for social security.

### Scenario 3 — Contractor in India for UK Client [T1]

**Facts:** UK company engages an Indian independent contractor for software development. Paid monthly in GBP.

**Assessment:**
- If genuinely independent (own clients, own tools, no integration): legitimate contractor
- India's contract labour rules and withholding requirements still apply
- UK IR35 does NOT apply to overseas contractors (only UK-based engagements)
- Indian contractor must invoice with GST if registered, or without if below threshold

**Key risk:** If the Indian "contractor" works exclusively for the UK company, Indian authorities may reclassify as employment.

### Scenario 4 — EU Posted Worker, Malta to Germany [T1]

**Facts:** Maltese company sends an employee to Germany for 18 months.

**Assessment:**
- A1 certificate needed: apply to Malta's social security authority
- Employee remains under Maltese social security (Art 12, ≤24 months)
- German income tax withholding required (>183 days)
- Shadow payroll needed in Germany
- EU Posted Workers Directive: employee must receive at least German minimum wage, working time limits, and other core conditions

## PROHIBITIONS

- **Prohibition 1** — NEVER assume the 183-day rule is an automatic exemption. All three conditions must be met.
- **Prohibition 2** — NEVER ignore the economic employer concept in countries that apply it — host-country tax can be triggered from day one.
- **Prohibition 3** — NEVER rely on the contract label (contractor vs employee) to determine classification. Host-country substance-over-form rules apply.
- **Prohibition 4** — NEVER skip the A1 certificate for EU/EEA cross-border work. Without it, the host country can demand contributions.
- **Prohibition 5** — NEVER assume equity compensation is only taxed in the country where the employee is at vest. Multi-country apportionment applies.
- **Prohibition 6** — NEVER let an employee work remotely from a foreign country without assessing PE risk, tax obligations, and social security.
- **Prohibition 7** — NEVER ignore employment law in the host country. Local minimum wage, termination rules, and benefits may apply regardless of what the contract says.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. Employment tax, social security, and employment law rules vary by jurisdiction and change frequently. All outputs must be reviewed by a qualified professional before acting upon.

*Data reflects 2025–2026 rules. OpenAccountants — open-source accounting skills for AI — info@openaccountants.com*

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
