---
name: canada-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Canada. Trigger on phrases like "set up a company in Canada", "Canadian incorporation", "Corporations Canada", "federal incorporation", "provincial incorporation", "CBCA", "Ontario corporation", "BC incorporation", "Inc. Canada", "Canadian company formation", "register a business Canada", or any question about starting a business entity in Canada. Covers federal vs provincial incorporation, entity types, registration process, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Canadian company formation.
version: 1.0
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Edgar Lautsyus
review_status: current
depends_on: - company-formation-workflow-base
category: formation
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada Formation

## Canada Company Formation Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Formation

- **Corporations Canada fee — online** — $200  _(Corporations Canada — corporationscanada.ic.gc.ca)_
- **Express service** — + $100 (4 business hours)  _(Corporations Canada)_
- **Processing time** — 1 business day (online)  _(Corporations Canada)_
- **Annual return** — $12 online / $20 paper; within 60 days of anniversary  _(Corporations Canada; CBCA s.263)_
- **Director residency** — 25% Canadian-resident (majority if <4)  _(CBCA s.105(3))_
- **Min share capital** — None  _(CBCA; OBCA; BCBCA)_
- **Ontario** — $300  _(ServiceOntario — Ontario Business Registry)_
- **British Columbia** — $350  _(BC Registry Services — bcregistry.gov.bc.ca)_
- **Alberta** — Alberta incorporation fee: $283.25.  _(Alberta Corporate Registry)_
- **Quebec** — Quebec incorporation fee: $397  _(Registraire des entreprises du Québec)_
- **Requirement** — Federal corp must register in each province of business  _(CBCA s.15; provincial equivalent legislation)_
- **Fee range** — Extra-provincial registration fees range $0 (Ontario)–$520 (NFL) per province.  _(Provincial corporate registries)_
- **CRA Business Number** — Free; online via BRO  _(CRA — Business Registration Online — canada.ca)_
- **GST/HST registration** — If taxable supplies > $30,000  _(ETA s.148)_
- **Corporate tax payment** — 2 months after year-end (3 months for small CCPC)  _(ITA s.157(1); CRA — Corporate payments — canada.ca)_
- **Foreign ownership restrictions** — None generally; Investment Canada Act for large/sensitive  _(Investment Canada Act)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD |
| Company registrar (federal) | Corporations Canada (ISED) -- corporationscanada.ic.gc.ca |
| Company registrar (provincial) | Varies by province (e.g., Ontario: ServiceOntario; BC: BC Registry Services; QC: Registraire des entreprises) |
| Key legislation | Canada Business Corporations Act (CBCA) -- federal; provincial equivalents (OBCA, BCBCA, etc.) |
| Typical formation time | 1 day (federal online); 1--5 days (most provinces online) |
| Corporate tax rate | 15% federal + provincial (combined ~26.5% general; ~12.2% small business on first $500K) |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Proprietorship | Partnership (GP/LP) | Federal Corporation (CBCA) | Provincial Corporation | Cooperative |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | No (GP) / LP has some | Yes | Yes | Yes |
| Liability | Unlimited | GP: Unlimited; LP: Limited for limited partners | Limited | Limited | Limited |
| Min. founders | 1 | 2 | 1 shareholder + 1 director | Varies by province | Per applicable Act |
| Min. share capital | N/A | N/A | No minimum | No minimum (most provinces) | Per applicable Act |
| Jurisdiction | Province of residence | Province | Canada-wide (right to carry on business nationally) | Province of incorporation (must extra-provincially register elsewhere) | Federal or provincial |
| Tax treatment | Personal | Partners taxed individually | Corporate | Corporate | Corporate (special rules) |
| Name protection | Province only | Province only | Canada-wide | Province only | Varies |

**Federal vs Provincial Incorporation -- Key Decision**

| Factor | Federal (CBCA) | Provincial |
| --- | --- | --- |
| Name protection | Canada-wide | Province only |
| Right to operate | All provinces (must extra-provincially register) | Province of incorporation (must extra-provincially register in others) |
| Annual filing | With Corporations Canada + each province of registration | With provincial registry only |
| Cost | $200 + extra-provincial fees | Province-specific (e.g., Ontario $300 online) |
| Director residency | 25% Canadian-resident (or majority if <4 directors) | Varies: ON requires 25%; BC has no requirement; QC no requirement |

**Recommended default:** Federal incorporation for businesses operating in multiple provinces. Provincial for single-province operations.

## Section 3 -- Registration Process (Federal)

### Step 1: Choose Corporate Name or Number

- **Corporate name/number rules** — Numbered corporation: no name search required (e.g., "12345678 Canada Inc."). Named corporation: NUANS name search included in online filing process. Name must include a legal element: "Inc.", "Incorporated", "Corporation", "Corp.", "Ltd.", "Limited", "Ltée", "Limitée"

### Step 2: Prepare Articles of Incorporation

Share classes and rights
Restrictions on share transfers (if any)
Number of directors (fixed or min/max range)
Restrictions on business activities (if any)
Provisions for financial year-end

### Step 3: File Online with Corporations Canada

- **Filing process** — Use Online Filing Centre at corporationscanada.ic.gc.ca. Fee: $200 (online); $250 (email/mail); +$100 for express (4 business hours). Certificate of Incorporation issued typically within 1 business day (online)

### Step 4: Extra-Provincial Registration

- **Extra-provincial registration process** — Federal corporation must register in each province where it carries on business. E.g., Ontario: file Form 2 with ServiceOntario; BC: extra-provincial registration with BC Registry. Fees vary: typically $0--$520 per province

### Step 5: Obtain Business Number (BN) from CRA

- **Business Number process** — Apply to Canada Revenue Agency for a Business Number. Simultaneously register for: GST/HST, payroll deductions, corporate income tax, import/export. Free; done online via CRA Business Registration Online

### Step 6: Municipal Business Licence (if required)

Some municipalities require a business licence
Check with local municipality

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Federal Corporation (CBCA) | No minimum | No minimum | As per share terms | Permitted (no statutory valuation requirement, but directors have fiduciary duties) |
| Ontario Corporation (OBCA) | No minimum | No minimum | As per share terms | Permitted |
| BC Corporation (BCBCA) | No minimum | No minimum | As per share terms | Permitted |
| Quebec Corporation (QBCA) | No minimum | No minimum | As per share terms | Permitted |

Canada has no minimum capital requirements for private corporation formation at any level.

## Section 5 -- Costs Breakdown

### Federal Incorporation

**Federal Incorporation Costs**

| Cost Component | Amount (CAD) | Notes |
| --- | --- | --- |
| Corporations Canada (online) | $200 | Standard (1 business day) |
| Express service | +$100 | 4 business hours |
| Extra-provincial registration (per province) | $0--$520 | Varies; Ontario ~$0; BC ~$350; QC ~$400 |
| NUANS name search (if named) | Included online | Separate $25 if pre-ordered |
| **Total federal + 1 province** | **$280--$600** | Government fees only |

### Provincial Incorporation (Examples)

**Provincial Incorporation Fees**

| Province | Online Fee | Notes |
| --- | --- | --- |
| Ontario | $300 | ServiceOntario |
| British Columbia | $350 | BC Registry Services |
| Alberta | $283.25 | Alberta Corporate Registry |
| Quebec | $397 | Registraire des entreprises |

### Annual Maintenance

**Annual Maintenance Costs**

| Item | Cost (CAD) |
| --- | --- |
| Corporations Canada annual return | $12 (online) / $20 (paper) |
| Provincial annual return | $0--$50 per province |
| Accountant fees | $1,500--$5,000/year |
| Corporate tax return (T2) | Included in accountant fees |
| Extra-provincial renewal fees | Varies by province |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Annual return (federal) | Within 60 days of anniversary date | Corporations Canada |
| Annual return (provincial) | Varies by province | Provincial registry |
| T2 corporate tax return | 6 months after fiscal year-end | CRA |
| Corporate tax payment | 2 months after year-end (3 months for small CCPC) | CRA |
| GST/HST returns | Quarterly or annually | CRA |
| Payroll remittances | Monthly or as required | CRA |
| T4/T5 information slips | By last day of February | CRA |
| Directors' register and minutes | Maintain at registered office | Internal |
| Shareholder register | Maintain at registered office | Internal |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Required documents** — Certificate of Incorporation (federal or provincial) Articles of Incorporation Directors' resolution authorising account opening Government-issued ID for all directors and signing authorities Business Number from CRA Proof of business address

### Typical Timeline

- **Bank account opening timeline** — 1--5 days (major Canadian banks for Canadian residents) 1--3 weeks (non-resident founders)

### Common Banks

Royal Bank of Canada (RBC), TD Bank, Scotiabank, BMO, CIBC (Big 5)
National Bank, Desjardins (QC) (large regional)
Wise Business, Airwallex (digital/international)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Federal (CBCA): Yes, but 25% must be Canadian-resident (majority if <4). BC: No residency requirement. Ontario: 25% Canadian-resident |
| Canadian-resident requirement workaround | Some provinces (BC, Nova Scotia, New Brunswick) have no director residency requirement |
| Nominee directors | Permitted but must comply with CBCA fiduciary duties |
| Physical presence required? | No -- online filing accepted |
| Apostille requirements | Foreign documents may require authentication for banking |
| Foreign ownership restrictions | No general restrictions; Investment Canada Act review for large acquisitions or sensitive sectors |
| Social Insurance Number | Not required for incorporation; required for payroll if personally employed by the corporation |
| Non-resident tax implications | Non-resident corporations carrying on business in Canada are subject to Canadian tax on Canadian-source income |

## Section 9 -- Common Mistakes and Refusals

- **R-CA-F1 -- Director residency non-compliance (federal)** — Under the CBCA, at least 25% of directors must be resident Canadians. If fewer than 4 directors, at least 1 must be Canadian-resident. Failure to comply can result in dissolution proceedings. If no Canadian resident is available, consider incorporating in BC or Nova Scotia (no residency requirement).
- **R-CA-F2 -- Missing extra-provincial registration** — A federal corporation must register in each province where it carries on business. Operating without registration can result in the corporation being unable to maintain legal proceedings in that province.
- **R-CA-F3 -- GST/HST threshold ignorance** — GST/HST registration is mandatory once worldwide taxable supplies exceed $30,000 in any four consecutive calendar quarters. Failure to register triggers penalties and interest.
- **R-CA-F4 -- Confusing incorporation with business registration** — Sole proprietors and partnerships register a business name; they do not incorporate. Incorporation creates a separate legal entity with limited liability. These are fundamentally different.
- **R-CA-F5 -- Shell company for non-resident tax avoidance** — A Canadian corporation is taxed on worldwide income. Using a Canadian corporation solely to hold passive investments or as a conduit without Canadian substance may attract CRA scrutiny and GAAR (General Anti-Avoidance Rule) application.

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Decide federal vs provincial | 1 day | Day 1 |
| Prepare articles of incorporation | 1--3 days | Day 2--4 |
| File online (federal or provincial) | 1 day | Day 3--5 |
| Certificate of Incorporation received | 1 day (federal online) | Day 3--6 |
| Extra-provincial registration(s) | 1--10 days per province | Day 4--16 |
| CRA Business Number and tax accounts | 1--5 days (online) | Day 4--11 |
| Open bank account | 1--5 days (resident) / 1--3 weeks (non-resident) | Day 5--32 |
| **Ready to trade** |  | **As fast as 3--5 days (Canadian-resident, federal online)** |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
