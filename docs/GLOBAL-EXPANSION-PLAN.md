# Global Expansion Plan — OpenAccountants

How to build high-quality tax skills for every jurisdiction, fast.

---

## 1. Architecture: the three-tier model

Every jurisdiction follows the same layered pattern already proven in the repo:

| Tier | Purpose | Example |
|------|---------|---------|
| **Tier 1 — Workflow base** | Execution pipeline, output spec, self-checks, refusal catalogue | `us-tax-workflow-base`, `vat-workflow-base` |
| **Tier 1.5 — Regional layer** (where applicable) | Shared rules across a bloc of countries | `eu-vat-directive` (covers all 27 EU states) |
| **Tier 2 — Content skill** | One form, one computation, one jurisdiction | `germany-vat-return`, `malta-income-tax` |

**To add a new country, you need at minimum:**
1. The relevant workflow base (already exists for income tax and VAT)
2. A regional layer if applicable (already exists for EU VAT)
3. One or more Tier 2 content skills for that country

---

## 2. Prioritisation framework

Score each jurisdiction on three factors to decide build order:

| Factor | Weight | How to measure |
|--------|--------|----------------|
| **Freelancer population** | 40% | Number of self-employed / sole proprietors (OECD, Eurostat, national stats) |
| **Tax complexity for sole props** | 30% | Number of forms, filing frequency, VAT obligations |
| **English-language source availability** | 30% | Whether statutes, guides, and rate tables are available in English or need translation |

### Phase 1 — High-impact, English-speaking or well-documented (Q2–Q3 2026)

| Jurisdiction | Why | Skills needed |
|---|---|---|
| **United Kingdom** | Large freelancer economy, English sources, VAT + income tax + NIC | `uk-income-tax`, `uk-nic`, `uk-vat-return` (VAT started) |
| **United States — remaining states** | NY, TX, FL, WA, IL cover ~40% of US freelancers | `ny-individual-return`, `tx-franchise-tax` (started), `fl-*` (no income tax — just confirm), `wa-b-and-o-tax`, `il-individual-return` |
| **Canada** | Large freelancer base, English/French sources, GST/HST + federal + provincial | `ca-federal-t1`, `ca-gst-hst`, `on-individual-return`, `bc-individual-return`, `qc-individual-return` |
| **Australia** | English sources, GST + income tax, BAS | `au-individual-return`, `au-gst-bas`, `au-super-guarantee` |
| **Ireland** | EU member, English sources, growing tech freelancer base | `ie-income-tax`, `ie-vat-return` (EU VAT directive layer already exists) |

### Phase 2 — EU core (Q3–Q4 2026)

The EU VAT directive layer already exists. Each country needs only a Tier 2 VAT skill + income tax skill.

| Jurisdiction | Skills needed |
|---|---|
| **Germany** | `germany-income-tax` (VAT done) |
| **France** | `france-income-tax`, `france-vat-return` (started) |
| **Netherlands** | `nl-income-tax`, `nl-vat-return` |
| **Spain** | `es-irpf`, `es-vat-return` |
| **Italy** | `it-income-tax`, `it-vat-return` (started) |
| **Portugal** | `pt-irs`, `pt-vat-return` |
| **Belgium** | `be-income-tax`, `be-vat-return` |
| **Poland** | `pl-pit`, `pl-vat-return` |

### Phase 3 — High-growth markets (Q1–Q2 2027)

| Jurisdiction | Skills needed |
|---|---|
| **India** | `in-itr`, `in-gst` |
| **Brazil** | `br-irpf`, `br-indirect-tax` (started) |
| **Mexico** | `mx-isr`, `mx-iva` |
| **Singapore** | `sg-income-tax`, `sg-gst` |
| **UAE** | `ae-corporate-tax`, `ae-vat` |
| **Japan** | `jp-income-tax`, `jp-consumption-tax` (started) |
| **South Korea** | `kr-income-tax`, `kr-vat` |

### Phase 4 — Long tail (2027+)

All remaining jurisdictions, prioritised by contributor interest and freelancer demand.

---

## 3. Quality at scale — the production pipeline

### 3a. Skill authoring process

```
Step 1: Research         → Gather primary sources (statutes, tax authority guides, rate tables)
Step 2: Draft            → Write the skill following skill-template.md
Step 3: Self-check       → Author runs all self-checks from the template
Step 4: Peer review      → Another contributor or Claude reviews for completeness
Step 5: Practitioner     → Licensed practitioner in that jurisdiction verifies every T1 rule
        verification       and signs off
Step 6: Publish          → Merged to repo, goes live on openaccountants.com with "verified" badge
```

### 3b. Using Claude to accelerate drafting

Claude can draft Tier 2 skills from primary sources, but every skill MUST be verified by a local practitioner. The workflow:

1. **Contributor provides primary sources** — statutes, tax authority PDFs, official rate tables
2. **Claude drafts the skill** using the skill template, citing every figure to the provided sources
3. **Contributor reviews and corrects** — catches hallucinated thresholds, missing edge cases
4. **Local practitioner signs off** — no skill ships without this step

This cuts authoring time from days to hours while maintaining quality.

### 3c. Quality gates (non-negotiable)

| Gate | Requirement |
|------|-------------|
| **Citation coverage** | Every rate, threshold, and deadline cites a primary source (statute, regulation, or official notice) |
| **Mechanical computation** | Every step can be executed without judgment — if Claude needs to "use professional judgment," the rule is underspecified |
| **Scope clarity** | Explicit "covers" and "does not cover" lists |
| **Practitioner sign-off** | Warranted/licensed practitioner in the jurisdiction has reviewed and approved |
| **Disclaimer present** | Standard disclaimer block (no liability, professional review required, openaccountants.com link) |
| **Self-checks pass** | All self-check items verified before publication |

---

## 4. Scaling the contributor base

### 4a. Who writes skills

| Contributor type | What they do | Incentive |
|---|---|---|
| **Tax professionals** | Write and verify skills in their jurisdiction | Professional visibility, contributor profile, client acquisition via openaccountants.com |
| **Tax students / academics** | Draft skills from textbooks and statutes | Portfolio piece, academic credit potential |
| **Developers who do their own taxes** | Draft skills for their own jurisdiction | Scratch their own itch, public recognition |
| **Accounting firms** | Verify and sign off on skills | Brand visibility, demonstrate expertise |

### 4b. Reducing friction for contributors

- **Skill template is ready** — `skill-template.md` provides the exact structure
- **Existing skills serve as examples** — Malta, Germany, US federal skills show the pattern
- **Two submission paths** — GitHub PR for developers, web form at openaccountants.com for everyone else
- **Immediate publication as "unverified"** — contributors don't wait; verification happens in parallel
- **Claude assists drafting** — contributors can use Claude with the skill-creator skill to scaffold their work

### 4c. Regional coordinator model

For each major region, recruit a **regional coordinator** — a licensed practitioner who:
- Maintains the regional layer (e.g., EU VAT directive)
- Reviews and approves country-specific skills in their region
- Recruits local practitioners to verify country skills
- Keeps skills current when rates/thresholds change annually

| Region | Coordinator scope |
|---|---|
| **North America** | US (federal + 50 states), Canada (federal + provinces) |
| **EU/EEA** | 27 EU members + UK, Norway, Switzerland, Iceland |
| **Asia-Pacific** | Australia, NZ, Japan, South Korea, Singapore, India |
| **Latin America** | Brazil, Mexico, Argentina, Colombia, Chile |
| **Middle East & Africa** | UAE, Saudi Arabia, South Africa, Kenya, Nigeria |

---

## 5. Keeping skills current

Tax law changes every year. Skills rot if not maintained.

| Mechanism | Frequency | Who |
|---|---|---|
| **Annual rate/threshold update** | Once per tax year (Jan–Feb) | Regional coordinator or original author |
| **Legislative watch** | Ongoing | Flag new legislation that affects existing skills; update within 30 days of enactment |
| **Version bumps** | Per change | Every update increments the version and adds a changelog entry |
| **Stale skill alerts** | Automated | If a skill hasn't been updated for its current tax year by Feb 1, flag it as "needs update" on openaccountants.com |

---

## 6. New workflow bases needed

As we expand beyond sole props and VAT, new Tier 1 workflow bases will be needed:

| Workflow base | Covers | When |
|---|---|---|
| `payroll-workflow-base` | Employer withholding, payroll tax, social contributions | When skills expand to employers |
| `corporate-tax-workflow-base` | Corporate income tax returns | When skills expand beyond sole props |
| `gst-workflow-base` | GST/HST systems (Canada, Australia, India, NZ, Singapore) | Phase 1 — similar to VAT but different enough to warrant its own base |
| `social-contributions-workflow-base` | National insurance, social security, pension contributions | Phase 2 — currently handled ad-hoc in Malta SSC |

---

## 7. Metrics — how we know it's working

| Metric | Target (end of 2026) | Target (end of 2027) |
|--------|---------------------|---------------------|
| Jurisdictions covered | 15 | 40+ |
| Total skills published | 60 | 200+ |
| Skills with practitioner verification | 80%+ | 90%+ |
| Active contributors | 30+ | 100+ |
| Regional coordinators | 3 | 5 |

---

## 8. Immediate next steps

1. **Finish exporting the 8 stub US federal skills** — these are "installed in Claude" but not in the repo
2. **Complete Phase 1 jurisdictions** — UK, top 5 US states, Canada, Australia, Ireland
3. **Recruit first 3 regional coordinators** — North America, EU, Asia-Pacific
4. **Build the contributor onboarding flow** on openaccountants.com — account creation, skill submission, verification tracking
5. **Create a "skill bounty" board** — list the most-needed skills so contributors know where to focus
