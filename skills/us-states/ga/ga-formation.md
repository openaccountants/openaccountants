---
name: ga-formation
description: Tier 2 Georgia content skill for entity formation covering tax year 2025. Includes the GA LLC $100 Articles of Organization, $50 Annual Registration due April 1 (administrative dissolution after 60 days non-compliance), GA C-Corp Certificate of Incorporation $100 plus $40 publication notice, PLLC for licensed professionals, foreign qualification Certificate of Authority $225, GA DOR sales tax and withholding registrations, the doing-business thresholds (post-Wayfair $100k sales / 200 transactions for sales tax + income tax sourcing), and Atlanta-specific local business license requirements.
jurisdiction: US-GA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# GA Formation

## Georgia Entity Formation Skill

**Scope statement.** This skill addresses the formation, registration, and ongoing compliance of business entities organized under or doing business in the State of Georgia for tax year 2025. It covers domestic Georgia LLCs, professional LLCs (PLLCs), C-corporations, S-corporation elections, and foreign qualification of non-Georgia entities. It addresses Georgia Secretary of State filings, Georgia Department of Revenue registrations, Georgia Department of Labor employer registrations, and the City of Atlanta business license (general business tax certificate). It does not address the federal income tax classification, the federal §1361 S-election mechanics, multi-state apportionment beyond Georgia sourcing, or the operation of Georgia's Pass-Through Entity Tax (PTET) — those topics are handled in companion skills (`us-s-corp-election-decision`, `us-federal-return-assembly`, `ga-corporate-and-ptet`, `ga-income-tax`).

**Reviewer signoff required.** Every output produced by this skill must be reviewed and signed off by a Georgia-admitted attorney (for entity-choice and operating-agreement matters) and/or a credentialed tax professional (CPA, EA, or attorney) under Circular 230 before it is delivered to the client or filed with the Georgia Secretary of State or the Georgia Department of Revenue. The skill is a workflow accelerator. It is not a substitute for professional judgment.

## 1. Scope, sources, and conservative defaults

### 1.1 Statutory and regulatory framework

- **Georgia Limited Liability Company Act** — O.C.G.A. Title 14, Chapter 11 (the "LLC Act"). The operative formation provision is O.C.G.A. § 14-11-203 (filing of Articles of Organization). The annual registration requirement sits at O.C.G.A. § 14-11-1103 (read together with the umbrella annual registration statute at O.C.G.A. § 14-2-1622 for corporations and § 14-11-210 for LLCs).  _(O.C.G.A. Title 14, Chapter 11; § 14-11-203; § 14-11-1103; § 14-2-1622; § 14-11-210)_
- **Georgia Business Corporation Code** — O.C.G.A. Title 14, Chapter 2. Formation under § 14-2-202. The publication notice requirement sits at O.C.G.A. § 14-2-201.1 (this is the provision that catches first-time corporation filers off-guard — see §3.4 below).  _(O.C.G.A. Title 14, Chapter 2; § 14-2-202; § 14-2-201.1)_
- **Georgia Professional Corporation Act** — O.C.G.A. Title 14, Chapter 7 (for traditional PCs) and the PLLC provisions woven into the LLC Act for limited liability companies practicing licensed professions.  _(O.C.G.A. Title 14, Chapter 7)_
- **Georgia Revenue Code** — O.C.G.A. Title 48. Sales and use tax registration mechanics live at O.C.G.A. § 48-8-59 (general dealer registration) and § 48-8-2(8)(M.1) (post-Wayfair economic nexus, enacted by HB 61 (2018) and amended by HB 182 (2019) to the current $100,000 / 200 transactions threshold). Income tax sourcing sits at O.C.G.A. § 48-7-31 (corporate apportionment under the single-sales-factor regime).  _(O.C.G.A. Title 48; § 48-8-59; § 48-8-2(8)(M.1); HB 61 (2018); HB 182 (2019); § 48-7-31)_
- **Georgia Secretary of State, Corporations Division** — administers all Title 14 filings through the eCorp online portal at https://ecorp.sos.ga.gov. Filing fees are set by O.C.G.A. § 14-2-122 (corporations) and § 14-11-1101 (LLCs), as amended.  _(O.C.G.A. § 14-2-122; § 14-11-1101)_
- **Georgia Department of Revenue** — administers tax-account registration through the Georgia Tax Center (GTC) at https://gtc.dor.ga.gov.  _(https://gtc.dor.ga.gov)_
- **Georgia Department of Labor** — administers withholding/UI registration through the DOL Employer Portal at https://www.dol.state.ga.us.  _(https://www.dol.state.ga.us)_
- **City of Atlanta, Office of Revenue** — administers the General Business Tax Certificate under Atlanta City Code §§ 30-61 through 30-91. Other Georgia municipalities operate parallel regimes under O.C.G.A. § 48-13-5 et seq. (Local Government Occupation Tax Act).  _(Atlanta City Code §§ 30-61 through 30-91; O.C.G.A. § 48-13-5 et seq.)_
- **Federal preemption layer** — the Corporate Transparency Act (31 U.S.C. § 5336) and FinCEN's Beneficial Ownership Information (BOI) reporting rule (31 C.F.R. § 1010.380). As of the last update of this skill (2025-11-15), the BOI reporting requirement is stayed by nationwide injunction following the Eleventh Circuit's ruling and FinCEN's subsequent enforcement pause. See §10 below for treatment.  _(31 U.S.C. § 5336; 31 C.F.R. § 1010.380)_

### 1.2 Conservative defaults

- **Default 1 — File rather than skip** — If it is unclear whether a particular filing is required, the skill assumes the filing is required and produces the form. The cost of overfiling in Georgia (typically $50 to $225) is materially smaller than the cost of administrative dissolution or a missed local license.  _(Skill conservative defaults, §1.2)_
- **Default 2 — Online rather than paper** — Online filing is cheaper ($100 vs. $110 for Articles of Organization), faster (7–10 business days vs. up to 15 for paper), and produces a machine-readable acknowledgment that the reviewer can attach to the file.  _(Skill conservative defaults, §1.2)_
- **Default 3 — Domestic entity per-state** — The skill does not recommend Series LLCs for Georgia operations because Georgia does not recognize series treatment (see §3.6). The default for clients with multiple business lines is multiple separate LLCs.  _(Skill conservative defaults, §1.2; see §3.6)_
- **Default 4 — Atlanta-specific local license assumed for Atlanta clients** — If the client's principal place of business is in Atlanta (city limits, not Fulton or DeKalb County generally), the skill assumes a General Business Tax Certificate is required.  _(Skill conservative defaults, §1.2)_

### 1.3 Out of scope — must be handed off

The following matters are out of scope for this skill and must be handed off to a Georgia-licensed attorney or specialist:

- Drafting of operating agreements, shareholder agreements, buy-sell agreements, or any document that defines economic rights among members or shareholders.
- Securities-law compliance (federal Regulation D, Georgia Uniform Securities Act of 2008, O.C.G.A. § 10-5-1 et seq.) for any entity raising capital from non-founders.
- Specific guidance on professional-licensure ownership restrictions beyond the general rule (see §5).
- Multi-state nexus analysis where the entity has operations in states other than Georgia.
- Trademark, trade-name, and "doing business as" (d/b/a) filings — these are county-level filings under O.C.G.A. § 10-1-490 et seq. and are separately handled.

## 2. Workflow runbook

The skill executes in the following sequence. Each step is gated — the skill does not advance until the prior step has produced an output the reviewer can confirm.

```
[ Step 1: Intake ]
    |
    v
[ Step 2: Entity choice confirmation (LLC vs. C-Corp vs. PLLC) ]
    |
    v
[ Step 3: Name availability check (eCorp name search) ]
    |
    v
[ Step 4: Registered agent confirmation ]
    |
    v
[ Step 5: Articles of Organization / Incorporation filing ]
    |
    v
[ Step 6a: Publication notice (corporations only — 1 newspaper, county of registered office) ]
    |
    v
[ Step 6b: Operating Agreement / Bylaws drafted (off-skill, attorney) ]
    |
    v
[ Step 7: Federal EIN application (IRS Form SS-4) ]
    |
    v
[ Step 8: S-election if applicable (Form 2553 — see us-s-corp-election-decision) ]
    |
    v
[ Step 9: GA DOR registration (sales tax / withholding / corporate income) ]
    |
    v
[ Step 10: GA DOL employer registration (if hiring) ]
    |
    v
[ Step 11: Local business license (Atlanta or other municipality) ]
    |
    v
[ Step 12: Initial Annual Registration (between January 1 and April 1 of year FOLLOWING formation) ]
    |
    v
[ Step 13: Calendar all annual deadlines and hand off to bookkeeping/tax skills ]
```

A frequent error pattern at Step 6a is for the principal to assume the filing is complete once the Secretary of State acknowledges the Certificate of Incorporation. It is not. The publication notice is a free-standing statutory requirement under O.C.G.A. § 14-2-201.1, and missing it can be raised as a defense by adverse parties to challenge corporate existence in a later dispute. The skill enforces a Step 6a checklist item that does not clear until the affidavit of publication is on file.

0. **Step 1** — Intake
0. **Step 2** — Entity choice confirmation (LLC vs. C-Corp vs. PLLC)
0. **Step 3** — Name availability check (eCorp name search)
0. **Step 4** — Registered agent confirmation
0. **Step 5** — Articles of Organization / Incorporation filing
0. **Step 6a** — Publication notice (corporations only — 1 newspaper, county of registered office)
0. **Step 6b** — Operating Agreement / Bylaws drafted (off-skill, attorney)
0. **Step 7** — Federal EIN application (IRS Form SS-4)
0. **Step 8** — S-election if applicable (Form 2553 — see us-s-corp-election-decision)
0. **Step 9** — GA DOR registration (sales tax / withholding / corporate income)
0. **Step 10** — GA DOL employer registration (if hiring)
0. **Step 11** — Local business license (Atlanta or other municipality)
0. **Step 12** — Initial Annual Registration (between January 1 and April 1 of year FOLLOWING formation)
0. **Step 13** — Calendar all annual deadlines and hand off to bookkeeping/tax skills

## 3. Georgia LLC formation — mechanics

### 3.1 Filing the Articles of Organization

**Articles of Organization filing fees and processing times**  _(O.C.G.A. § 14-11-1101)_

| Item | Online | Paper |
| --- | --- | --- |
| Filing fee | **$100** | **$110** |
| Processing time (standard) | 7 business days | 15 business days |
| Expedited (2 business days) | +$100 | +$100 |
| Same-day expedite | +$250 | +$250 |
| One-hour expedite | +$1,000 | +$1,000 |

- **Foundational filing** — The foundational filing is Form CD 030 (Articles of Organization), lodged electronically through eCorp or on paper at the Corporations Division, 2 Martin Luther King Jr. Drive SE, Suite 313, West Tower, Atlanta GA 30334.  _(Form CD 030)_
- **Default filing mode** — The fees are set by O.C.G.A. § 14-11-1101 as amended (the paper differential was introduced in 2018 to push filers toward online filing). The skill defaults to online standard unless the client identifies a closing or contract deadline that requires expedited service.  _(O.C.G.A. § 14-11-1101)_
- **Required Articles content — item 1 name** — The name of the LLC, which must contain "limited liability company", "LLC", "L.L.C.", "limited company", or "LC". A reserved-words list under O.C.G.A. § 14-11-207 prohibits "bank", "trust", "insurance", "academy", "college", "university", and several others absent specific approval from the relevant regulator (Department of Banking and Finance, Insurance Commissioner, Board of Regents, etc.). The name must be distinguishable on the records from existing names — distinguishability is a stricter standard than the federal "likelihood of confusion" test, but is not as strict as a trademark search. The skill runs the name through the eCorp name search at https://ecorp.sos.ga.gov/BusinessSearch as Step 3 of the workflow.  _(O.C.G.A. § 14-11-207)_
- **Required Articles content — item 2 mailing address** — The mailing address of the principal office. This need not be in Georgia — a Delaware mailing address is acceptable for a Georgia LLC. (This is one of the cleanest features of the Georgia regime: the principal office, the mailing address, and the registered agent's office can all be different physical locations.)  _(§3.1)_
- **Required Articles content — item 3 registered agent** — The registered agent's name and Georgia street address (no P.O. boxes — see §3.3).  _(§3.3)_
- **Required Articles content — item 4 organizer** — The name and address of each organizer (typically the attorney or the founding member).  _(§3.1)_
- **Required Articles content — item 5 delayed effective date** — Optional: delayed effective date up to 90 days out, useful for fiscal-year planning when a December formation is desirable for the calendar year but the client doesn't want a short first year.  _(§3.1)_

The skill produces a draft of the Articles for reviewer signoff before submission. Once filed, the Secretary of State issues a Certificate of Organization (digitally signed PDF for online filings) — this is the document the bank will ask to see when opening the operating account.

### 3.2 Annual Registration — the $50 trap

**AUDIT FLASH POINT — missing Annual Registration is the #1 cause of administrative dissolution in Georgia.**

- **Annual Registration requirement and fee** — Every Georgia LLC (and every Georgia corporation, and every foreign LLC or corporation qualified to do business in Georgia) must file an Annual Registration between January 1 and April 1 of each year following the year of formation. The filing fee is $50 for an LLC (and $50 for a corporation; the corporate fee was $50 in 2025 — unchanged from prior years).  _(O.C.G.A. § 14-11-1103; § 14-2-1622)_
- **Annual Registration content** — The Annual Registration is a thin filing — it confirms the entity's name, principal office address, mailing address, registered agent, and the names of the LLC's chief executive (typically a designated member or manager). It does not require any financial disclosure.  _(O.C.G.A. § 14-11-1103; § 14-2-1622)_
- **Deadline and late penalty** — The deadline is April 1. There is no extension. Late filing carries a $25 late penalty added to the $50 filing fee, so the late cost is $75.  _(O.C.G.A. § 14-11-1103; § 14-2-1622)_
- **Administrative dissolution trigger** — The more serious consequence is administrative dissolution: if the LLC fails to file the Annual Registration and remains in default for 60 days after a notice of intent to administratively dissolve is issued by the Secretary of State, the LLC is administratively dissolved under O.C.G.A. § 14-11-603. (The corporate parallel is O.C.G.A. § 14-2-1421.)  _(O.C.G.A. § 14-11-603; § 14-2-1421)_
- **Consequences of administrative dissolution** — - The LLC loses limited liability protection prospectively — members may be held personally liable for obligations incurred after dissolution. - The LLC cannot maintain a lawsuit in Georgia courts until reinstated. - Contracts entered into post-dissolution are vulnerable to challenge. - Banks frequently freeze operating accounts when a Certificate of Existence cannot be produced.  _(O.C.G.A. § 14-11-603)_
- **Reinstatement** — Reinstatement is available under O.C.G.A. § 14-11-603(c) on payment of all accrued Annual Registration fees, the $25 late penalty for each year missed, and a $250 reinstatement fee. Reinstatement is retroactive — the LLC is treated as if it had never been dissolved — but the gap is on the public record and counterparties (especially commercial landlords and lenders) will see it on a Certificate of Good Standing.  _(O.C.G.A. § 14-11-603(c))_

The skill produces a calendar entry for January 15 of each year following formation, with an escalation to a hard-stop reminder on March 15 (two weeks before deadline). A common pattern the skill watches for: the registered agent's email address on file is stale, so the Secretary of State's annual reminder email bounces. The first year is particularly dangerous because the founder is focused on operations and assumes "annual" means "12 months after formation". It does not — it means by April 1 of the calendar year following formation. An LLC formed on December 15, 2025 must file its first Annual Registration by April 1, 2026 — only 3.5 months after formation.

### 3.3 Registered agent

- **Registered agent qualification** — A Georgia registered agent must: Be a natural person resident in Georgia with a Georgia street address, or Be a Georgia-domiciled entity authorized to do business in Georgia, with a Georgia street address.  _(O.C.G.A. § 14-11-209; § 14-2-501)_
- **Registered agent address and availability requirements** — The address must be a physical street address (no P.O. boxes, no virtual mailbox addresses, no UPS Store box addresses). The agent must be available during normal business hours (9am–5pm, Monday–Friday) to accept service of process. The statutory basis is O.C.G.A. § 14-11-209 (LLCs) and § 14-2-501 (corporations).  _(O.C.G.A. § 14-11-209; § 14-2-501)_

The owner of a closely-held LLC may serve as their own registered agent if they are a Georgia resident and willing to have their address on the public record. For founders who live outside Georgia or who want privacy, commercial registered agent services (Cogency Global, Northwest Registered Agent, Harvard Business Services, CT Corporation, etc.) charge between $100 and $300 per year. The skill flags two scenarios as requiring a commercial registered agent:

1. Founder is a non-Georgia resident — the LLC cannot use the founder's out-of-state address as the registered agent address. This is the most common reason foreign-resident GA LLCs need a commercial agent.
2. Founder operates from a virtual office or coworking space — these typically do not provide a stable physical address for service of process during business hours.

### 3.4 Operating Agreement

Georgia does not require the Operating Agreement to be filed with the Secretary of State, and the eCorp filing flow does not ask for it. However, the LLC Act expressly contemplates the Operating Agreement at O.C.G.A. § 14-11-101(18) and § 14-11-1107 (which permits the Operating Agreement to override most default rules of the LLC Act).

- **Default distribution rule** — Default distribution rule is per capita, not pro rata by capital contribution (O.C.G.A. § 14-11-403). This is rarely what the founders intend.  _(O.C.G.A. § 14-11-403)_
- **Default management rule** — Default management is by majority of all members (O.C.G.A. § 14-11-308). Manager-management requires affirmative election in the Operating Agreement.  _(O.C.G.A. § 14-11-308)_
- **Default voting rule** — Default voting is one vote per member regardless of capital contribution (O.C.G.A. § 14-11-308(b)).  _(O.C.G.A. § 14-11-308(b))_
- **Default transfer restrictions** — Default transfer restrictions are minimal — a member may freely assign their economic interest, though the assignee does not become a member without consent (O.C.G.A. § 14-11-503).  _(O.C.G.A. § 14-11-503)_

The skill does not draft the Operating Agreement. It does, however, produce a checklist of points the agreement must cover, including capital accounts (tax allocation), distribution waterfalls, manager designation if applicable, transfer restrictions including rights of first refusal and tag-along/drag-along rights, dissolution events, and indemnification of managers under O.C.G.A. § 14-11-306. The reviewer (typically a Georgia attorney) drafts the document.

For a single-member LLC, the skill produces a one-page template Operating Agreement that establishes the LLC as a sole-member entity, designates the member as the manager, confirms federal disregarded-entity classification (unless the member elects otherwise), and acknowledges the limited liability shield. Even single-member LLCs benefit from having a written Operating Agreement because lenders and counterparties will frequently ask for it as part of know-your-customer review.

### 3.5 GA DOR and DOL registrations

- **Sales and Use Tax registration trigger and output** — Georgia Department of Revenue (Sales and Use Tax) — required if the LLC sells tangible personal property in Georgia, or if it sells digital products or services that are taxable under O.C.G.A. § 48-8-2, or if it crosses the economic nexus threshold from out-of-state. Registration is via the Georgia Tax Center (GTC) at https://gtc.dor.ga.gov and is free. The output is a Sales and Use Tax Number (format: nine digits) and a Certificate of Registration that must be displayed at the place of business. (For SaaS specifically, Georgia exempts most software-as-a-service from sales tax as of 2025 because Georgia taxes only specified digital products under O.C.G.A. § 48-8-3.5 — but the SaaS exemption is fact-specific and the reviewer should confirm; see `ga-sales-tax`.)  _(O.C.G.A. § 48-8-2; § 48-8-3.5)_
- **Withholding and Unemployment registration** — Georgia Department of Labor (Withholding and Unemployment) — required only if the LLC has Georgia-resident W-2 employees. Registration is via the Georgia Tax Center for the withholding account (DOR-administered) and via the Department of Labor Employer Portal for the unemployment insurance account. The withholding account is free; the unemployment account opens with a default new-employer rate (2.7% in 2025 for most industries, with construction at a higher rate).

The skill does not automatically register the LLC for these accounts. It produces a recommendation in the output reviewer brief, and the reviewer or the client's payroll provider executes the registration. Premature registration triggers ongoing filing obligations (zero-return filings) that the client may not want.

### 3.6 Series LLCs — not available in Georgia

- **Georgia does not have a series LLC statute** — Georgia does not have a series LLC statute. As of the last update of this skill, only 15 states plus DC have enacted series LLC statutes (Delaware, Illinois, Iowa, Kansas, Missouri, Montana, Nevada, North Dakota, Oklahoma, Tennessee, Texas, Utah, Wyoming, Wisconsin, Indiana, plus DC). Georgia is not on the list.

The implication for Georgia clients with multiple business lines (e.g., a real estate investor with 8 rental properties, each of which the client wants in its own liability silo) is that each silo must be its own separate LLC. This means:

- 8 separate Articles of Organization filings ($800 total).
- 8 separate Annual Registrations every April 1 ($400/year).
- 8 separate registered agents (or one commercial agent serving all 8).
- 8 separate EINs (the IRS issues one per entity).
- 8 separate operating accounts.

A foreign series LLC (e.g., a Delaware series LLC) that does business in Georgia faces a particularly thorny question — Georgia has not formally taken a position on whether the individual series of a foreign series LLC must each qualify separately as foreign entities in Georgia, or whether the umbrella series LLC's foreign qualification covers all series. The skill's conservative default is to recommend separate foreign qualification of each series that has Georgia activity. The reviewer should confirm given the lack of authoritative guidance.

## 4. Georgia C-Corp formation

### 4.1 Certificate of Incorporation

- **Filing form** — The corporate parallel to Articles of Organization is the Certificate of Incorporation (sometimes called Articles of Incorporation — Georgia uses both terms interchangeably in the statute and on the forms). The filing form is Form CD 227 (Articles of Incorporation – Profit Corporation).  _(Form CD 227)_

**Certificate of Incorporation fees**  _(O.C.G.A. § 14-2-122)_

| Item | Online | Paper |
| --- | --- | --- |
| Filing fee | **$100** | **$110** |
| Publication notice (separate — see §4.2) | **$40** | **$40** |
| Total at formation | **$140** | **$150** |
| Annual Registration (each subsequent year) | **$50** | **$60** |

- **Required form content — item 1 corporate name** — The corporate name, which must include "corporation", "incorporated", "company", "limited", "Corp.", "Inc.", "Co.", or "Ltd." Reserved words mirror the LLC list (O.C.G.A. § 14-2-401).  _(O.C.G.A. § 14-2-401)_
- **Required form content — item 2 authorized shares** — The number of authorized shares. The skill defaults to 10,000,000 authorized common shares with $0.0001 par value (a common venture-startup convention) for any corporation contemplating a future financing round, or to 1,000 authorized shares with no par value for a closely-held corporation that will not raise outside capital.  _(§4.1)_
- **Required form content — item 3 registered agent** — The registered agent name and Georgia street address (same rules as LLC — §3.3).  _(§3.3)_
- **Required form content — item 4 principal office mailing address** — The principal office mailing address (need not be in Georgia).  _(§4.1)_
- **Required form content — item 5 incorporator** — The incorporator's name and address.  _(§4.1)_
- **Required form content — item 6 optional provisions** — Optional provisions: indemnification (O.C.G.A. § 14-2-851 et seq.), director exculpation (O.C.G.A. § 14-2-202(b)(4)), staggered board, preemptive rights, etc.  _(O.C.G.A. § 14-2-851 et seq.; § 14-2-202(b)(4))_

### 4.2 The publication notice — the most-missed step

**AUDIT FLASH POINT — Georgia is one of only three states that requires post-incorporation publication notice. Missing this step is the #1 vulnerability in newly-formed Georgia corporations.**

- **Publication timing and content requirement** — O.C.G.A. § 14-2-201.1 requires that no later than the next business day after delivery of the Articles of Incorporation to the Secretary of State, the incorporator must arrange for publication of a Notice of Intent to Incorporate in a newspaper that is the official legal organ of the county where the registered office is located, or another general-circulation newspaper in that county. The notice must run once a week for two consecutive weeks and must include: - The corporate name and intended principal office address. - The name and street address of the registered office and registered agent. - A statement that the Articles of Incorporation have been (or will be) delivered to the Secretary of State.  _(O.C.G.A. § 14-2-201.1)_
- **Typical publication cost** — $40 USD (typical cost; some smaller-county legal organs charge less; some Atlanta-region papers charge more)  _(O.C.G.A. § 14-2-201.1)_
- **Not filed with Secretary of State** — The publication notice is not filed with the Secretary of State. It is a stand-alone statutory requirement, and the absence of an affidavit of publication is a defect in the formation that opposing counsel can raise in litigation to challenge corporate existence or to pierce the corporate veil. The skill produces a Step 6a checklist item that must be cleared (affidavit on file in the minute book) before the formation is considered complete.  _(O.C.G.A. § 14-2-201.1)_

1. Wrong county. Filers based in Alpharetta sometimes publish in the Atlanta Journal-Constitution because it is the largest paper they know. But Alpharetta is in Fulton County (which the AJC does cover as the legal organ), so this is usually fine. But a client in Marietta (Cobb County) must publish in the Marietta Daily Journal (the Cobb County legal organ), not the AJC. The legal organ of each Georgia county is designated by the Superior Court clerk of that county and is listed at https://www.gpa.org.
2. Late publication. The statute says "no later than the next business day after delivery" of the Articles. In practice, the Secretary of State does not enforce this strict timing — many filers publish within the week or even within the month. But the more time elapses, the more vulnerable the filing is to challenge. The skill enforces a same-week target.

LLCs are not subject to the publication notice. This is an LLC-vs-corporation differentiator that is one reason Georgia attorneys often prefer LLCs for closely-held businesses that have no near-term need for corporate form.

### 4.3 Corporate Annual Registration

- **Corporate Annual Registration mechanics** — The Annual Registration mechanics for a Georgia corporation mirror the LLC mechanics (§3.2): file between January 1 and April 1 each year for $50, with a $25 late penalty and a 60-day grace period before administrative dissolution under O.C.G.A. § 14-2-1421. The form requires confirmation of the corporation's name, principal office address, registered agent, and the names and addresses of the chief executive officer, chief financial officer, and corporate secretary.  _(O.C.G.A. § 14-2-1421)_

For a closely-held corporation where one individual serves in all three officer roles, the form simply lists that person three times. The skill produces a reviewer note flagging this as acceptable but recommending that the corporation designate distinct officers for governance hygiene if and when there are multiple shareholders.

### 4.4 GA DOR corporate income tax registration

- **Automatic registration for domestic corporations** — Every Georgia corporation must register with the Georgia Department of Revenue for corporate income tax. This is automatic for corporations formed in Georgia — the Secretary of State transmits formation data to the DOR, which opens an account and assigns the corporation a state taxpayer identification number. The corporation must file Form 600 (or Form 600S for S-corporations) annually by the 15th day of the third month following the close of the corporation's fiscal year.  _(§4.4)_
- **Foreign corporation registration** — Foreign corporations doing business in Georgia must register separately by submitting Form CRF-002 (State Tax Registration Application) through the Georgia Tax Center. See §7 below.  _(Form CRF-002)_

## 5. Professional LLC (PLLC) and Professional Corporation (PC)

Georgia recognizes both Professional Limited Liability Companies (PLLCs) and traditional Professional Corporations (PCs) for the practice of licensed professions. The statutory basis for PLLCs is woven into the LLC Act (O.C.G.A. §§ 14-11-1101 through 14-11-1109 and the cross-reference to the Professional Corporation Act at § 14-7-3). The statutory basis for PCs is the Professional Corporation Act, O.C.G.A. Title 14, Chapter 7.

### 5.1 Who can use a PLLC

- **Eligible professions for PLLC** — A PLLC in Georgia is reserved for individuals licensed to practice a specific profession by a Georgia licensing board. The most common professions are: - Medicine — physicians licensed by the Georgia Composite Medical Board under O.C.G.A. § 43-34-1 et seq. (also dentists, podiatrists, physician assistants). - Law — attorneys admitted to the State Bar of Georgia. Note that attorneys may also use the older "law firm" structure under the Bar's rules, but the PLLC is becoming common. - Accounting — CPAs licensed by the Georgia State Board of Accountancy under O.C.G.A. § 43-3-1 et seq. - Architecture and engineering — licensed by the Georgia State Board of Architects and Interior Designers and the Georgia State Board of Professional Engineers and Land Surveyors. - Nursing — RNs and APRNs licensed by the Georgia Board of Nursing. - Mental health — psychologists (O.C.G.A. § 43-39-1), LPCs, LMFTs, LCSWs. - Veterinary medicine — veterinarians licensed by the Georgia State Board of Veterinary Medicine. - Pharmacy — pharmacists licensed by the Georgia State Board of Pharmacy. - Real estate brokerage — brokers licensed by the Georgia Real Estate Commission. (Real estate salespersons cannot form PLLCs; only brokers.)  _(O.C.G.A. § 43-34-1 et seq.; § 43-3-1 et seq.; § 43-39-1)_

### 5.2 Ownership restrictions

- **Every member must be licensed** — The general rule under O.C.G.A. § 14-7-3 (incorporated into the PLLC regime by cross-reference) is that every member of a PLLC must be licensed in Georgia to practice the profession the PLLC will offer. There are limited exceptions for non-licensed family members in certain estate-planning contexts, but the default is strict: a non-licensed business partner cannot be a member of the PLLC.  _(O.C.G.A. § 14-7-3)_

The implication for a medical PLLC is severe. A physician founder cannot bring in a non-physician business operations partner as a member. The non-physician can be an employee or an independent contractor providing services to the PLLC, but cannot hold an equity interest. This restriction is enforced by the Composite Medical Board, which can revoke licenses of physicians who participate in PLLCs with non-licensed equity holders.

### 5.3 PLLC formation mechanics

- **PLLC formation steps** — PLLC formation uses the same Articles of Organization form as a standard LLC (Form CD 030), with two additional steps: 1. The name must include "Professional Limited Liability Company", "P.L.L.C.", or "PLLC" — not just "LLC". 2. Before filing with the Secretary of State, the PLLC must obtain certification of compliance from the relevant licensing board. For a medical PLLC, this means submitting the proposed Articles to the Composite Medical Board (typically a 30–45 day review) and obtaining a Board Certificate of Need before filing with the Secretary of State. The licensing board confirms (a) all proposed members are licensed in good standing, (b) the proposed name does not mislead the public, and (c) any required malpractice insurance is in place.  _(Form CD 030)_
- **PLLC Secretary of State filing fee and board certification fee** — $100 online, $110 paper (Secretary of State); licensing board certification fee typically $50–$200 depending on the board USD  _(§5.3)_
- **PLLC Annual Registration and licensure maintenance** — The Annual Registration mechanics mirror the standard LLC ($50 by April 1). However, the PLLC must also maintain its licensure with the relevant board on an ongoing basis. Loss of licensure of all members triggers automatic dissolution of the PLLC under the Professional Corporation Act.  _(Professional Corporation Act)_

## 6. Doing business in Georgia — triggers

The phrase "doing business in Georgia" appears in three distinct contexts with three different thresholds. The skill produces a flowchart to determine which threshold applies.

### 6.1 Trigger 1: Secretary of State foreign qualification

- **Certificate of Authority requirement** — A non-Georgia entity (Delaware LLC, Nevada corporation, etc.) that "transacts business" in Georgia must obtain a Certificate of Authority from the Secretary of State under O.C.G.A. § 14-11-702 (LLCs) and § 14-2-1501 (corporations).  _(O.C.G.A. § 14-11-702; § 14-2-1501)_
- **Activities that do NOT constitute transacting business** — The statute does not define "transacts business" affirmatively, but lists 11 categories of activity that do not constitute transacting business: - Maintaining or defending a lawsuit. - Holding meetings of members or managers. - Maintaining bank accounts. - Maintaining offices for the transfer or registration of the entity's own securities. - Selling through independent contractors. - Soliciting or procuring orders (whether by mail or through employees) that require acceptance outside Georgia before becoming contracts. - Creating or acquiring indebtedness, mortgages, and security interests. - Securing or collecting debts. - Owning real or personal property without operating it as a business. - Conducting an isolated transaction that is completed within 30 days and is not part of a series of similar transactions. - Transacting business in interstate commerce.  _(O.C.G.A. § 14-11-702)_

The general inference from the negative list is that "transacting business" requires a physical presence in Georgia — an office, an employee, inventory in a Georgia warehouse, or a regular pattern of in-state sales activity. A pure e-commerce seller shipping into Georgia from Delaware does not trigger this Secretary of State threshold (because that is "interstate commerce") even though they may trigger the sales-tax threshold (Trigger 2 below) or the income tax sourcing threshold (Trigger 3 below).

The skill flags the following as triggering foreign qualification:

- A Georgia employee (W-2 or 1099).
- A Georgia office, store, or warehouse.
- A Georgia bank account used as the operating account (mere passive accounts are exempt).
- A Georgia-licensed activity (e.g., a non-Georgia LLC doing real estate brokerage in Georgia).
- A pattern of in-state contracts that are accepted in Georgia.

### 6.2 Trigger 2: Sales tax economic nexus (post-Wayfair)

- **Economic nexus threshold for sales tax** — More than $100,000 in gross revenue from retail sales of tangible personal property delivered into Georgia in the previous or current calendar year, OR 200 or more separate retail sales transactions delivered into Georgia in the previous or current calendar year.  _(O.C.G.A. § 48-8-2(8)(M.1))_
- **Enactment history and rate** — After South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018), Georgia enacted HB 61 (2018) and amended it via HB 182 (2019) to establish economic nexus for sales tax purposes. A seller that crosses either prong must register with the Georgia Department of Revenue, collect Georgia sales tax (state rate 4% plus local rates ranging from 2% to 5% depending on county and municipality), and file periodic sales tax returns. The exact taxability of digital products and SaaS is addressed in `ga-sales-tax`; this skill simply identifies the registration trigger.  _(O.C.G.A. § 48-8-2(8)(M.1); HB 61 (2018); HB 182 (2019))_
- **Independence from foreign qualification trigger** — Note that the sales-tax economic nexus threshold is independent of the foreign qualification threshold (Trigger 1). An out-of-state e-commerce seller crossing the $100k threshold must register with the GA DOR but does not need to obtain a Certificate of Authority from the Secretary of State (because shipping is interstate commerce and is exempt from "transacting business" under O.C.G.A. § 14-11-702).  _(O.C.G.A. § 14-11-702)_
- **Early warning threshold** — The skill produces a reviewer note when the client's projected Georgia sales exceed $80,000 — early-warning at 80% of threshold — so the registration can be in place before the threshold is crossed.  _(§6.2)_

### 6.3 Trigger 3: Income tax sourcing

- **Single-sales-factor apportionment** — The third "doing business" trigger is the corporate income tax sourcing rule under O.C.G.A. § 48-7-31 and the parallel personal-income-tax sourcing rule under O.C.G.A. § 48-7-1 et seq. Georgia uses a single-sales-factor apportionment for most industries — the percentage of the entity's nationwide income that is subject to Georgia tax equals the percentage of the entity's nationwide sales that are "sourced" to Georgia.  _(O.C.G.A. § 48-7-31; § 48-7-1 et seq.)_
- **Market-based sourcing for services** — Sales of tangible personal property are sourced to the destination (the customer's location). Sales of services are sourced under the market-based sourcing rule (where the customer receives the benefit), which Georgia adopted for tax years beginning on or after January 1, 2013 (O.C.G.A. § 48-7-31(d)(2)(B)).  _(O.C.G.A. § 48-7-31(d)(2)(B))_
- **No dollar threshold; P.L. 86-272 safe harbor** — The income tax sourcing trigger does not have a dollar threshold — even $1 of Georgia-sourced income creates a Georgia filing obligation for a non-Georgia entity (if the entity is otherwise subject to corporate income tax). However, P.L. 86-272 (15 U.S.C. § 381) provides a federal safe harbor: a non-Georgia entity whose only Georgia activity is the solicitation of orders for sales of tangible personal property, where the orders are approved outside Georgia and shipped from outside Georgia, is exempt from Georgia corporate income tax. P.L. 86-272 protects sellers of tangible goods only — it does not protect service sellers, SaaS providers, or digital-product sellers, who are subject to Georgia income tax on any Georgia-sourced sales.  _(15 U.S.C. § 381 (P.L. 86-272))_

This skill flags the P.L. 86-272 question for the reviewer when a non-Georgia client has any Georgia-sourced sales but no physical Georgia presence — the reviewer applies the safe harbor and decides whether a Form 600/600S filing is required. See `ga-corporate-and-ptet` for full income-tax mechanics.

## 7. Foreign qualification — Certificate of Authority

- **Filing forms** — A non-Georgia entity that crosses Trigger 1 (§6.1) must obtain a Certificate of Authority. The filing is Form CD 235 (Application for Certificate of Authority – Foreign LLC) or Form CD 233 (Application for Certificate of Authority – Foreign Profit Corporation).  _(Form CD 235; Form CD 233)_

**Certificate of Authority fees**  _(§7)_

| Item | Online | Paper |
| --- | --- | --- |
| Initial Certificate of Authority filing fee | **$225** | **$235** |
| Annual Registration (each subsequent year) | **$50** | **$60** |
| Certificate of Existence from home state (required attachment) | varies by home state ($50–$200) | varies |

- **Application requirements** — The application requires: 1. The entity's legal name in its home state. If that name is not available in Georgia (because a Georgia entity already has it), the foreign entity must adopt a fictitious name for use in Georgia under O.C.G.A. § 14-11-703. 2. The home state of formation and the date of formation. 3. The Certificate of Existence (or Good Standing) issued by the home state's Secretary of State, dated no more than 90 days before the Georgia application. 4. The Georgia registered agent name and Georgia street address (same rules as for a Georgia LLC — §3.3). 5. The principal office address (which can be the out-of-state address). 6. A list of the LLC's managers or the corporation's directors and officers.  _(O.C.G.A. § 14-11-703)_
- **Consequences of unauthorized activity** — The Certificate of Authority is not retroactive. A non-Georgia entity that has been doing business in Georgia without a Certificate of Authority is subject to: - A prohibition on maintaining a lawsuit in Georgia courts until qualified (O.C.G.A. § 14-2-1502(a) and § 14-11-711(a)). The entity cannot sue on a Georgia contract until it qualifies and pays back-filing fees for each year of unauthorized activity. - Civil penalties of up to $500 per year of unauthorized activity (O.C.G.A. § 14-2-1502(d) and § 14-11-711(d)). - No corporate-level voidness, however — contracts entered into by the unauthorized entity remain enforceable, the entity remains liable on its obligations, and counterparties can still sue the entity. The disability runs against the unauthorized entity's right to be a plaintiff, not against its substantive obligations.  _(O.C.G.A. § 14-2-1502(a); § 14-2-1502(d); § 14-11-711(a); § 14-11-711(d))_

After obtaining the Certificate of Authority, the foreign entity is subject to all the same annual obligations as a domestic Georgia entity: Annual Registration by April 1, registered agent maintenance, and any applicable DOR/DOL registrations.

## 8. Atlanta business license and other local taxes

**AUDIT FLASH POINT — the Atlanta business license is a separate municipal obligation that the Secretary of State filing does not satisfy. Many founders assume the state filing is the only license they need; for an Atlanta-based business it is not.**

The City of Atlanta requires every business operating within the city limits to obtain a General Business Tax Certificate (sometimes called an "occupation tax certificate" or, colloquially, a "business license") under Atlanta City Code §§ 30-61 through 30-91. The statutory authority for the city to impose this requirement is the Georgia Local Government Occupation Tax Act, O.C.G.A. § 48-13-5 et seq.

### 8.1 Atlanta General Business Tax Certificate mechanics

- **Administering authority** — The General Business Tax Certificate is administered by the City of Atlanta Office of Revenue, 55 Trinity Avenue SW, Suite 1350, Atlanta GA 30303. Applications are accepted in person, by mail, and (since 2023) through the Atlanta Business License Online Portal at https://business.atlantaga.gov.  _(Atlanta City Code §§ 30-61 through 30-91)_
- **Administrative fee** — $75 flat USD (every business, every year)  _(Atlanta City Code §§ 30-61 through 30-91)_
- **Regulatory fee** — varies by business classification ($0 for most professional services; up to $500+ for regulated activities like alcohol sales, adult entertainment, and certain food-service operations) USD  _(Atlanta City Code §§ 30-61 through 30-91)_
- **Occupation tax** — graduated by gross receipts and by NAICS classification. The tax is computed on a worksheet that the applicant submits annually. For a small professional-services business (under $100,000 gross receipts), the occupation tax is typically $50–$150. For a business with $1M gross receipts, the occupation tax can range from $500 to $2,000+ depending on classification. USD  _(Atlanta City Code §§ 30-61 through 30-91)_
- **Renewal deadline and late penalty** — The Certificate must be renewed annually by January 31 (note: this is a different deadline than the April 1 Secretary of State Annual Registration). Late renewal carries a penalty of 10% of the prior year's tax, plus 1.5% per month interest.  _(Atlanta City Code §§ 30-61 through 30-91)_
- **Display requirement** — The Certificate must be prominently displayed at the business premises. For home-based businesses, the Certificate must be available for inspection on request.  _(Atlanta City Code §§ 30-61 through 30-91)_

### 8.2 Home-based businesses

- **Home Occupation Permit requirements** — Atlanta allows home-based businesses subject to zoning restrictions (Atlanta Zoning Ordinance § 16-29). Most home occupations require a separate Home Occupation Permit in addition to the General Business Tax Certificate. The Home Occupation Permit costs $25 and requires affirmations that: - The home is the operator's primary residence. - No more than 25% of the residence floor area is used for business. - No non-resident employees work at the home. - No retail sales occur at the home. - No outdoor signage advertises the business. - Vehicular traffic and parking do not exceed residential norms.  _(Atlanta Zoning Ordinance § 16-29)_

A home-based software developer or consultant typically qualifies easily. A home-based business that holds inventory, has client visits, or has employees may not.

### 8.3 Other Georgia municipalities

**Other Georgia municipality occupation tax authorities**  _(O.C.G.A. § 48-13-5)_

| Municipality | Authority / Administering Department | Structure |
| --- | --- | --- |
| Savannah (Chatham County) | Revenue Department | Business Tax Certificate, gross-receipts-based, renewal by April 1 each year |
| Augusta (Richmond County) | Planning & Development Department | Occupation Tax Certificate |
| Athens (Athens-Clarke County) | Finance Department | Occupation Tax Certificate |
| Macon (Macon-Bibb County) | Business License Division | Business License |
| Columbus (Muscogee County) | Revenue Division | Business License |
| Unincorporated county areas | varies by county | most Georgia counties also impose occupation taxes on businesses located in unincorporated county areas; fee and structure varies by county |

Every Georgia municipality has parallel occupation-tax authority under O.C.G.A. § 48-13-5. The skill produces a reviewer note identifying the applicable municipality (or unincorporated county) and the corresponding licensing authority. The reviewer or the client executes the local registration.

## 9. S-Corporation election (Georgia overlay)

- **Automatic Georgia conformity to federal S-election** — A Georgia corporation that has made a valid federal S-election under IRC § 1362 is automatically treated as an S-corporation for Georgia income tax purposes — Georgia conforms to the federal classification under O.C.G.A. § 48-7-21(b)(7) and does not require a separate state-level S-election. This is a contrast to states like New York, New Jersey, and California, which require a separate state S-election (or have non-conforming treatment).  _(O.C.G.A. § 48-7-21(b)(7); IRC § 1362)_
- **Form 600S filing and shareholder inclusion rules** — The Georgia S-corporation files Form 600S annually, reporting the pass-through income that is sourced to Georgia. Resident shareholders include the Georgia-sourced and non-Georgia-sourced income on their Form 500 (individual return). Non-resident shareholders include only the Georgia-sourced income.  _(Form 600S; Form 500)_

The skill defers full S-election analysis to `us-s-corp-election-decision` and Georgia-specific S-corp mechanics to `ga-corporate-and-ptet`. For purposes of this formation skill, the only Georgia-side step at formation is to note in the client's calendar that, once the Form 2553 federal election is accepted by the IRS (typically a 60–90 day acknowledgment cycle), the Georgia DOR account should be updated to flag the corporation as an S-corporation so that the DOR sends Form 600S instead of Form 600.

A common error is for a freshly-formed Georgia C-corporation to file Form 2553 with the IRS, receive the federal acceptance, and then continue to receive Form 600 (C-corp return) notices from the GA DOR because the DOR has not been informed. The skill produces a checklist item to update the DOR account after federal acceptance.

## 10. BOI / Corporate Transparency Act — current status

- **CTA/BOI requirement description** — The federal Corporate Transparency Act (CTA), 31 U.S.C. § 5336, and FinCEN's Beneficial Ownership Information (BOI) reporting rule, 31 C.F.R. § 1010.380, would require every newly-formed LLC, corporation, and similar entity to report its beneficial owners (individuals who own 25% or more, or who exercise substantial control) to FinCEN within 30 days of formation. The rule became effective January 1, 2024.  _(31 U.S.C. § 5336; 31 C.F.R. § 1010.380)_
- **Current stay status** — As of the last update of this skill (2025-11-15), the BOI reporting requirement is stayed by federal court injunction. The Eleventh Circuit's decision in Texas Top Cop Shop, Inc. v. Garland and FinCEN's subsequent enforcement pause mean that newly-formed entities are not, at the time of this skill's last update, required to file a BOI report. The Treasury and FinCEN have indicated they are working on revised regulations that would narrow the scope of the reporting requirement (likely limiting it to foreign-formed entities), but the final rule is not in place.  _(Texas Top Cop Shop, Inc. v. Garland (Eleventh Circuit))_
- **Skill's current position** — The skill's current position is to: 1. Inform the client that the BOI reporting requirement is currently stayed. 2. Collect and retain the beneficial ownership information that would be required (name, date of birth, residential address, ID document) so that if the stay is lifted or the rule is amended, the client can file promptly. 3. Calendar a check-in for the date the next scheduled court action is expected. 4. Not file a BOI report unless and until the stay is lifted. The reviewer must confirm the current status of the CTA at the time the formation is executed — the skill's information is current only to the last_updated date in the frontmatter.

## 11. Common errors and audit flash points

**Common errors and audit flash points**  _(§11)_

| # | Error pattern | Consequence | Detection rule |
| --- | --- | --- | --- |
| 1 | Missed Annual Registration by April 1 | 60-day window, then administrative dissolution; $250 reinstatement + back fees | Calendar entry on January 15 + March 15; verify Secretary of State email on file is current |
| 2 | Missing publication notice for new corp | Defect in formation; vulnerable to challenge | Step 6a checklist; require affidavit of publication in minute book |
| 3 | Atlanta business license not obtained | Civil penalties; cannot enforce contracts; potential lien | Atlanta address check at intake; calendar January 31 deadline |
| 4 | Sales tax registration after $100k threshold crossed | Back-tax assessment + interest + penalties (failure-to-collect) | Quarterly review of GA sales; alert at $80k |
| 5 | Foreign entity transacting business without Certificate of Authority | Cannot sue in Georgia until qualified; $500/year penalty | Identify physical Georgia presence at intake |
| 6 | PLLC with non-licensed equity holder | License revocation; veil-piercing exposure | Verify all members are licensed at intake; check board roster |
| 7 | Treating series LLC as recognized in GA | Each series may be separately liable; foreign qualification ambiguous | Per-state recognition check at intake |
| 8 | Registered agent address goes stale | Notice of dissolution doesn't reach LLC | Annual confirmation of agent contact details |
| 9 | Operating Agreement never adopted (single-member LLC) | Default rules apply (per-capita distribution, etc.); bank may refuse account | Confirm OA on file at Step 6b |
| 10 | Federal S-election made but GA DOR not updated | Receives wrong tax forms; mismatched filings | Step 9 update to DOR account |
| 11 | December formation, first Annual Registration mis-calendared | Administrative dissolution within 8 months of formation | First-year calendar entry by January 15 of year following formation |
| 12 | Reserved-word name (e.g., "Atlanta Bank LLC") rejected | Filing rejected; delay to operations | eCorp name search + reserved-word check at Step 3 |

## 12. Worked examples

### 12.1 Example A — Atlanta SaaS LLC (single member, Georgia resident)

**Facts.** Maria, a Georgia resident living in Midtown Atlanta, has been freelancing as a software developer with annual revenue of $185,000. She wants to form an LLC to (a) shield personal assets, (b) open a business operating account, and (c) be in position to elect S-corporation treatment in the future. She has no employees and no plans to hire. She sells SaaS subscriptions to clients across the US, with about 12% of her revenue from Georgia-based clients. She works from her home office.

**Workflow.**

1. **Intake.** Confirm Maria is a single-member operation, no current employees, no inventory, no real estate, no licensed profession (software is not licensed in Georgia). Confirm she wants federal disregarded-entity treatment.
2. **Entity choice.** LLC (standard, not PLLC). C-corp not needed — no outside capital, no equity comp plan.
3. **Name check.** "Atlanta Cloud Solutions LLC" — run through eCorp name search. Confirmed available.
4. **Registered agent.** Maria's home address (Midtown Atlanta, Fulton County). She is the registered agent. (Note privacy implication — address will be on public record. Discuss with Maria whether she wants a commercial agent for privacy.)
5. **Articles of Organization.** File Form CD 030 online. Fee $100. Effective immediately.
6. **No publication notice required** (this is an LLC, not a corp).
7. **Operating Agreement.** Single-member template signed.
8. **EIN.** Apply via IRS online EIN application, same day issuance.
9. **GA DOR registration.** Maria's SaaS revenue from Georgia clients is approximately $22,000, well under the $100,000 economic nexus threshold. Georgia's SaaS taxability is narrow (most SaaS is exempt) — defer to `ga-sales-tax` for fact-specific analysis. **Conservative default: do not register for sales tax now.** Calendar a review at $80,000 Georgia-sourced revenue.
10. **GA DOL registration.** Not required (no employees).
11. **Atlanta business license.** **REQUIRED.** Maria operates from a home in Atlanta city limits. File General Business Tax Certificate via the Atlanta Business License Online Portal. Administrative fee $75 + occupation tax (estimated $150 based on $185k revenue, professional services classification) + Home Occupation Permit $25 = **$250 total**. Renewal annually by January 31.
12. **Annual Registration.** Calendar for January 15 each year. First filing due April 1, 2027 (if formation is 2026) — Maria should be reminded that the first Annual Registration is the year *after* formation.
13. **S-election decision.** Defer to `us-s-corp-election-decision`. At $185k revenue, an S-election is potentially beneficial. The skill recommends Maria consider S-election after formation — Form 2553 within 75 days of formation, or by March 15 of any subsequent year.

### 12.1 Example A — Atlanta SaaS LLC (single member, Georgia resident)

- Articles of Organization filed: $100.
- General Business Tax Certificate (Atlanta): $250 (first year).
- Home Occupation Permit: included above.
- Total first-year Georgia/Atlanta costs: **$350**.
- Annual recurring: **$50** (Annual Registration) + **$225** (Atlanta business license recurring, estimated) = **$275/year**.

### 12.2 Example B — Georgia real estate investment LLC

**Facts.** Robert is an out-of-state investor (Florida resident) who has just purchased two Atlanta rental properties (one in Inman Park, one in East Atlanta Village) and is under contract on a third in Decatur (DeKalb County, outside Atlanta city limits). He wants each property in a separate LLC for liability segregation. He has no other Georgia activity and will not visit the properties; a Georgia-based property manager handles operations.

**Workflow.**

1. **Intake.** Three properties, three LLCs (because Georgia does not recognize series LLCs — see §3.6). Robert is non-Georgia resident. Properties are passive rental real estate. No employees.
2. **Entity choice.** Standard LLCs (not PLLCs, not corporations). Each LLC will be a disregarded entity for federal tax, with Robert as the single member. (Federal classification is governed by `us-sole-prop-bookkeeping`; for state purposes, the LLC is treated as a flow-through.)
3. **Name check.** "Inman Park Holdings LLC", "EAV Holdings LLC", "Decatur Holdings LLC" — run all three through eCorp. Confirmed available. (Avoid names like "Robert Smith Real Estate LLC" that tie back to the investor's identity for litigation-protection reasons — pure-asset names are stronger.)
4. **Registered agent.** Robert is a Florida resident, so he cannot serve as his own Georgia registered agent. He retains a commercial registered agent (Northwest Registered Agent, $125/year per entity = $375/year total). The agent's Georgia address is in Decatur.
5. **Articles of Organization.** Three filings, $100 each = $300. File online.
6. **No publication notice** (LLCs).
7. **Operating Agreement.** Three single-member templates, each identifying Robert as sole member.
8. **EIN.** Three EINs from IRS.
9. **GA DOR registration.** Rental income from real property is not subject to sales tax (real property is exempt). **No sales tax registration.** However, Robert's Georgia-sourced rental income is subject to Georgia personal income tax under O.C.G.A. § 48-7-30 (nonresident sourcing). Robert will file **Form 500 (Georgia Nonresident Individual Income Tax Return)** annually, reporting the Georgia-sourced rental income. The LLCs themselves do not file Georgia returns (because they are federally disregarded and Georgia conforms). Defer to `ga-income-tax`.
10. **GA DOL registration.** Not required (no employees; property manager is an independent contractor).
11. **Atlanta business license.** Inman Park and EAV properties are in Atlanta city limits — **two Atlanta business licenses required**, one for each property's LLC. Decatur property is in unincorporated DeKalb (assuming it's outside Decatur city limits — must confirm by zip code) and may require a DeKalb County occupation tax certificate. The skill flags this as requiring municipal confirmation by the reviewer.
12. **Annual Registration.** Three filings due April 1, 2027, $50 each = $150/year.

- **Georgia nonresident rental income sourcing** — Georgia-sourced rental income is subject to Georgia personal income tax under nonresident sourcing rules; nonresident files Form 500 (Georgia Nonresident Individual Income Tax Return) annually.  _(O.C.G.A. § 48-7-30)_

### 12.2 Example B — Georgia real estate investment LLC

- Articles of Organization: $300 (three LLCs).
- Commercial registered agent (year 1): $375.
- Atlanta business licenses (estimated, two properties): $300 (year 1).
- DeKalb County occupation tax certificate (estimated): $75–$150.
- Total first-year Georgia costs: approximately **$1,075**.
- Annual recurring: $150 (Annual Registration) + $375 (registered agent) + $300 (Atlanta licenses) + $100 (DeKalb) = **$925/year**.

### 12.2 Example B — Georgia real estate investment LLC

- Robert should also confirm that his property insurance carrier permits LLC ownership; some homeowner-style policies do not cover LLC-owned rentals.
- The skill flags Robert's foreign-investor status as raising a separate FinCEN BOI question if the stay is lifted — Robert is a US resident (Florida), so the BOI status is the standard US-person status, but his offshore exposure (if any) should be confirmed.
- Robert may benefit from a **Georgia Series LLC alternative structure** — see §3.6 — but Georgia's lack of series LLC recognition makes this approach require separate LLCs. The skill does not recommend forming a Delaware series LLC and qualifying it in Georgia, because the Georgia treatment is unsettled (see §3.6).

### 12.3 Example C — Foreign-resident Georgia LLC (UK founder)

**Facts.** Alex is a UK citizen and UK resident, with no US residency status (no green card, no substantial presence). Alex runs a software-consulting business serving US clients and wants to form a Georgia LLC because Alex's largest client is an Atlanta-based fintech. Alex will not relocate to Georgia and will not physically visit on more than an occasional basis (under 20 days per year).

**Workflow.**

1. **Intake.** Single foreign-resident member. No US tax residency. Software consulting (not a licensed profession). No US employees. Client concentration in Georgia (~60% of revenue), other clients in NY and CA.
2. **Entity choice.** Standard Georgia LLC. The disregarded-entity default would treat the LLC as a transparent foreign-owned single-member LLC for US federal tax purposes — which triggers Form 5472 / Form 1120 protective filings under IRS Notice 2017-26 and the regulations under § 6038A. The federal classification analysis is outside this skill's scope; defer to a US international tax specialist.
3. **Name check.** "Alex Consulting LLC" or similar.
4. **Registered agent.** Alex is not a Georgia resident, so a commercial registered agent is required. Recommend Northwest Registered Agent or Cogency Global, $125–$200/year.
5. **Articles of Organization.** File online, $100. Use Alex's UK address as the principal office mailing address (this is permissible — see §3.1).
6. **No publication notice** (LLC).
7. **Operating Agreement.** Single-member template. Note that Alex's foreign status may make certain US tax elections (e.g., S-corporation election) **unavailable** — IRC § 1361(b)(1)(C) restricts S-corp shareholders to US individuals (and certain trusts), so Alex cannot make an S-election. The OA should not contemplate an S-election absent change in residency.
8. **EIN.** Alex applies via IRS Form SS-4 by mail or fax (because Alex does not have an SSN, the online EIN portal is unavailable). Processing time is 4–8 weeks.
9. **GA DOR registration.** Alex's Georgia client revenue exceeds the sales-tax economic nexus threshold ($100k) *if* the software consulting services are taxable in Georgia. Software consulting services are generally **not** subject to Georgia sales tax (Georgia taxes only specified services under O.C.G.A. § 48-8-3.5 — see `ga-sales-tax`). **Conservative default: register for sales tax to be safe, then claim service-revenue exemption on filings.** This is debatable — the reviewer should make the call. Alternative: do not register, monitor at the threshold.
10. **GA income tax sourcing.** Software services are sourced under the market-based rule to where the customer receives the benefit (O.C.G.A. § 48-7-31(d)(2)(B)). Alex's Atlanta fintech client receives the benefit in Georgia, so 60% of Alex's revenue is Georgia-sourced. The LLC itself, being a federal disregarded entity owned by a non-resident alien, has Georgia-source income that flows through to the foreign owner. The Georgia tax treatment of this flow-through to a non-resident alien owner is **unsettled** and depends on whether Georgia treats the LLC as the taxpayer or follows federal disregarded-entity treatment. The reviewer must consult `ga-corporate-and-ptet` and a US international tax specialist. **This skill does not opine on the foreign-flow-through question.**
11. **GA DOL.** Not required (no employees).
12. **Atlanta business license.** Required only if Alex has a physical Atlanta presence. Since the LLC has no Atlanta office (registered agent address is not a business premises in the licensing sense), **probably not required**, but the reviewer should confirm with the Atlanta Office of Revenue.
13. **Annual Registration.** Calendar April 1.
14. **BOI / CTA.** Alex is a foreign individual — under the proposed revised CTA rule (per FinCEN's 2025 enforcement pause statements), foreign-controlled US entities may remain subject to BOI reporting even if the rule is generally rolled back. The skill flags this as requiring monitoring.

- **S-corp shareholder eligibility restriction** — S-corporation shareholders must be US individuals (and certain trusts); a foreign individual like Alex cannot make an S-election.  _(IRC § 1361(b)(1)(C))_
- **Foreign-owned disregarded entity federal filing trigger** — A foreign-owned single-member disregarded entity triggers Form 5472 / Form 1120 protective filings.  _(IRS Notice 2017-26 and regulations under § 6038A)_
- **Georgia sales tax scope on services** — Georgia taxes only specified services under O.C.G.A. § 48-8-3.5; software consulting services are generally not subject to Georgia sales tax.  _(O.C.G.A. § 48-8-3.5)_
- **Georgia income tax market-based sourcing for services** — Software services are sourced under the market-based rule to where the customer receives the benefit.  _(O.C.G.A. § 48-7-31(d)(2)(B))_

### 12.3 Example C — Foreign-resident Georgia LLC (UK founder)

- Articles of Organization: $100.
- Commercial registered agent: $150 (year 1).
- US international tax specialist consultation (one-time): estimate $1,500–$3,000 to handle Form 5472 / 1120, ITIN application for Alex, treaty position (US-UK treaty under Article 7).
- Total first-year direct GA costs: approximately **$250**; total including US tax specialist: **$1,750–$3,250**.

This example illustrates that the Georgia formation itself is straightforward and cheap. The US federal tax compliance for a foreign-owned LLC is the cost driver. The skill explicitly defers that compliance to a US international tax specialist and does not produce federal positions for foreign-owned LLCs.

### 12.4 Example D — PLLC for a medical practice

**Facts.** Dr. Lisa Chen is a Georgia-licensed physician (internal medicine), currently employed as a W-2 employee at a hospital. She wants to open a solo private practice in Decatur. She is the sole shareholder, will be the sole physician, and will hire one medical assistant (W-2 employee) and one receptionist (W-2 employee). She will accept insurance.

**Workflow.**

1. **Intake.** Dr. Chen is licensed by the Georgia Composite Medical Board, license in good standing. Solo practitioner. Two non-physician W-2 employees. Medical practice — licensed profession.
2. **Entity choice.** **PLLC required** (or a Professional Corporation, but PLLC is generally preferred for tax flexibility — allows S-election when scale justifies it). The PLLC must be exclusively owned by licensed physicians; Dr. Chen as sole owner is fine.
3. **Pre-formation board certification.** Submit proposed Articles to the Composite Medical Board for certification of compliance. Wait time 30–45 days. Fee approximately $100. The Board confirms Dr. Chen is licensed in good standing and the proposed name does not mislead the public.
4. **Name check.** "Chen Internal Medicine PLLC" — confirm available on eCorp. The name must include "PLLC" (or "Professional Limited Liability Company"). The Board may have name-style preferences for medical practices (e.g., the practice name should reflect the practitioner's name or the practice specialty).
5. **Registered agent.** Dr. Chen as a Georgia resident can be her own registered agent (her practice address in Decatur). Alternative: commercial agent for privacy.
6. **Articles of Organization.** File Form CD 030 online with the Board's certification attached. Fee $100.
7. **No publication notice** (PLLC is an LLC variant, not a corporation).
8. **Operating Agreement.** Required. Even as a single-member PLLC, the OA must (a) confirm sole-member ownership by Dr. Chen, (b) restrict transfers to other licensed physicians, (c) address what happens on Dr. Chen's death or loss of licensure (typically: 12-month wind-down period during which the practice can be sold to another licensed physician or dissolved), and (d) confirm malpractice insurance coverage.
9. **EIN.** Apply via IRS online — same day.
10. **GA DOR registration.** Medical services are not subject to Georgia sales tax. **No sales tax registration.** Income tax registration is automatic on formation.
11. **GA DOL registration.** **REQUIRED.** Dr. Chen will have two W-2 employees. Register for withholding via GTC. Register for unemployment via DOL Employer Portal. New-employer UI rate 2.7%. (Worker's compensation insurance is also required for any Georgia employer with three or more employees — O.C.G.A. § 34-9-2 — but Dr. Chen with two employees plus herself is at three, so coverage is required. WC is procured through a private carrier or the assigned-risk pool.)
12. **Atlanta business license.** Decatur is in DeKalb County. If Dr. Chen's practice is within the City of Decatur, she needs a Decatur business license. If she's in unincorporated DeKalb, a DeKalb County occupation tax certificate is required. The skill confirms address vs. city limits.
13. **Medical-specific licensure.** Dr. Chen needs:
    - DEA registration for the practice (separate from her personal DEA — required for the entity to prescribe controlled substances under her authority).
    - State controlled substance registration with the Georgia Drugs and Narcotics Agency.
    - Medicare provider enrollment (if accepting Medicare).
    - Medicaid provider enrollment (if accepting Georgia Medicaid).
    - Private payor contracts and credentialing (BCBS, Aetna, UnitedHealthcare, etc.).
14. **HIPAA compliance.** The practice is a HIPAA covered entity. Privacy policies, business associate agreements with vendors, security policies, and breach response plans must be in place before the practice opens. **The skill does not handle HIPAA compliance** — defer to a healthcare-compliance specialist.
15. **Annual Registration.** Calendar April 1.
16. **S-election consideration.** At sufficient profitability (>$80k net), an S-election is potentially beneficial for SE-tax purposes. Defer to `us-s-corp-election-decision`.

- **Georgia workers' compensation requirement threshold** — Worker's compensation insurance is required for any Georgia employer with three or more employees.  _(O.C.G.A. § 34-9-2)_
- **New-employer UI rate** — 2.7% percent

### 12.4 Example D — PLLC for a medical practice

- Composite Medical Board certification: $100.
- Articles of Organization: $100.
- Decatur or DeKalb business license: estimated $150–$300.
- Workers' compensation insurance (annual premium estimate): $1,500–$3,000 depending on payroll and classification.
- Medical malpractice insurance (annual premium): $4,000–$15,000 depending on specialty and coverage limits.
- HIPAA compliance setup (one-time): $2,000–$5,000.
- Healthcare-specific licensing and credentialing: $1,500–$5,000 (one-time and ongoing).
- Total first-year setup costs: approximately **$9,000–$28,000** for a solo practice.
- Annual recurring (excluding insurance and clinical costs): **$50** (Annual Registration) + **$300** (Decatur license, estimated) = **$350/year** in pure entity-maintenance costs.

This example illustrates that the entity formation itself is straightforward — the substantial cost of opening a medical practice is in the regulatory and insurance overlay, not in the Secretary of State filing.

## 13. Reviewer brief — output template

When the skill completes, it produces a reviewer brief for the credentialed reviewer to sign off on. The brief includes:

1. **Client identification and entity intent** — name, residency, intended entity type, intended principal place of business in Georgia.
2. **Entity-choice memo** — LLC vs. PLLC vs. C-Corp recommendation, with reasoning grounded in §3 through §5 above.
3. **Filings produced** — draft Articles, registered agent confirmation, name availability search results.
4. **Federal coordination** — EIN application status, S-election decision status (if applicable), BOI/CTA status.
5. **State tax registrations** — GA DOR (sales tax, withholding, corporate income) status, GA DOL status.
6. **Local registrations** — Atlanta General Business Tax Certificate or other municipal license status.
7. **Annual compliance calendar** — Annual Registration deadlines, business license renewal deadlines, federal tax deadlines, state tax deadlines.
8. **Audit flash points** — explicit list of the items most likely to be missed, drawn from §11.
9. **Hand-offs to other skills** — identification of which companion skills will pick up downstream work (`us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, `us-s-corp-election-decision`, `ga-income-tax`, `ga-sales-tax`, `ga-corporate-and-ptet`).
10. **Open questions for the reviewer** — anything the skill flagged as fact-specific or as requiring credentialed judgment.

The reviewer signs off on the brief before any document is filed with the Secretary of State or the Department of Revenue. The skill does not file documents directly — it produces drafts and the reviewer (or the client) executes the filing.

## 14. Hand-offs to companion skills

**Hand-offs to companion skills**  _(Section 14 table)_

| Downstream concern | Companion skill | Trigger |
| --- | --- | --- |
| Bookkeeping and Schedule C classification | `us-sole-prop-bookkeeping` | Single-member LLC formed and operating |
| Federal income tax computation, SE tax | `us-schedule-c-and-se-computation` | Year-end of formation year |
| Federal S-election decision | `us-s-corp-election-decision` | Profitability projections justify analysis |
| Federal return assembly | `us-federal-return-assembly` | Form 1040 preparation |
| Quarterly estimated tax | `us-quarterly-estimated-tax` | Each quarterly cycle |
| Self-employed retirement | `us-self-employed-retirement` | Annual retirement-contribution decision |
| Self-employed health insurance | `us-self-employed-health-insurance` | Marketplace coverage in place |
| 1099-NEC issuance | `us-1099-nec-issuance` | Year-end contractor payments review |
| Georgia personal income tax | `ga-income-tax` | Annual Form 500 preparation |
| Georgia corporate income tax, PTET | `ga-corporate-and-ptet` | Annual Form 600 or 600S preparation |
| Georgia sales tax | `ga-sales-tax` | Sales nexus reached or product taxability question |

## End of Georgia Entity Formation skill.

End of Georgia Entity Formation skill.

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
