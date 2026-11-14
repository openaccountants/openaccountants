---
name: nv-formation
description: >
  Nevada entity formation and maintenance for 2026: LLC and profit-corporation articles, registered agent acceptance, initial and annual lists, business licence, authorized-capital fees and defaults. Covers charging-order limits, spendthrift trusts, series segregation, professional entities, public disclosures, formation versus residence, and other-state qualification. Retains the high-net-worth, rental and crypto cases with corrected costs and specialist referrals. Trigger on "Nevada LLC", "Nevada incorporation", "Nevada formation fees", "Nevada annual list", "Nevada series LLC", "Nevada asset protection" or "Nevada versus Wyoming or Delaware".
jurisdiction: US-NV
category: formation
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: filing-howto
version: "0.2"
---

# Nevada entity formation and maintenance, 2026

> **Source-cited draft.** Built from the Nevada statutes and Secretary of State pages identified in Sources, read on 2026-11-14 for the provisions stated here. No accountant has approved this version. General reference only: have the relevant tax professional and Nevada legal counsel review their respective parts before filing or transferring assets. Written tax advice must meet Circular 230 section 10.37.

**Answer first.** An ordinary nonexempt Nevada LLC pays **$425** in state formation charges: articles **$75**, initial list **$150**, state business licence **$200**. Ordinary annual list/licence renewal is **$350**. A Chapter 78 profit corporation pays a **$500** licence: minimum formation charges are **$725**, and minimum annual list/licence charges are **$650**. Its annual list is capital-dependent, not always the minimum. File the initial list with the articles unless the Secretary of State allows an alternative due date. Nevada formation does not determine the owner's tax residence. [NRS 86.561](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec561), [86.263](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec263), [78.150 and 78.760](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec150), [76.100 and 76.130](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec100).

## Scope

Nevada domestic LLCs under NRS Chapter 86 and profit corporations under Chapter 78: public filings, ordinary charges, maintenance, and the formation questions raised by asset holding or professional structures. The spendthrift-trust and series sections identify conditions and referrals; they do not draft instruments or guarantee creditor protection.

Limited partnerships, nonprofits, professional licensing, gaming, cannabis, mining, banking, insurance, securities offerings, bankruptcy and contested creditor matters require their governing forms and specialist review. Do not apply the ordinary fee totals to them without checking their chapter and exemptions. Professional LLCs need the Chapter 89 checks below.

Use `us-tax-workflow-base` for intake and reviewer outputs. Other computation owners are `nv-commerce-and-mbt`, `nv-payroll`, `nv-sales-tax`, `us-s-corp-election-decision`, `us-form-1065-partnership` and `us-federal-return-assembly`. Federal figures and election deadlines are not restated.

## Ask the client first

1. **Who owns and manages the business, and where do they actually live and work?** Identify Nevada and other-state property, employees, offices and operations.
2. **What entity exists or is proposed?** LLC, profit corporation, professional entity, foreign registration or parent/series; obtain existing articles, status and renewal dates.
3. **What stock is authorized?** Each class's share count, par or no-par terms and investor requirements. Share count alone cannot price a corporation.
4. **What will be contributed and when?** Title, value, basis, debt, lender/insurance restrictions and transfer dates; separate real estate, professional interests and crypto.
5. **What creditor exposure exists?** Actual/threatened claims, contracts, guarantees, judgments, family orders and solvency; proposed trust beneficiaries and retained powers.
6. **What permissions and exemptions are claimed?** Agent acceptance, actual authority, state-licence exemption evidence, local premises and professional/regulated approvals.

## The method, step by step

### 1. Decide the jurisdiction and legal form

Nevada Constitution article 10 section 1(9) prohibits a tax on natural persons' wages or personal income but expressly permits taxes on business income or revenue. It does not exempt another state's resident or source income. [Nevada Constitution](https://www.leg.state.nv.us/Const/NvConst.html#Art10Sec1).

Compare home-state formation, Nevada, Wyoming and Delaware using current total costs, actual investor requirements, governance, public disclosures, forum needs, asset location and qualification elsewhere. Load `wy-formation` and `de-formation` for their figures. Do not repeat unsourced rankings of privacy, creditor protection, courts or universal venture-capital acceptance, or invent redomestication fees.

**AUDIT FLASH POINT.** Nevada articles and a registered agent do not move a California owner's tax residence. Where California is involved, run `ca-residency-leaving-california`, `ca-llc-fee-and-tax` and `ca-smllc-form-568`; for other states, run their residence/business-tax/formation skills. Qualification, tax nexus and jurisdiction are separate questions. Obtain the facts before claiming savings.

### 2. Check name, registered agent and management

| Item | Requirement | Official source |
| --- | --- | --- |
| LLC name | Distinguishable name; allowed designator: Limited-Liability Company, Limited Liability Company, Limited Company, Limited, Ltd., L.L.C., L.C., LLC or LC; Company may be Co. Restricted professional/banking/trust words need applicable approval | [NRS 86.171](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec171) |
| Corporation name | Distinguishability; a name appearing to be a natural person's name requires an identifying addition under 78.035(1). Do not say every name requires one particular suffix | [NRS 78.035, 78.039](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec035) |
| Agent and acceptance | Commercial agent's name, or the specified noncommercial agent/office-holder information; obtain certificate of acceptance | [NRS 77.310](https://www.leg.state.nv.us/NRS/NRS-077.html#NRS077Sec310) |
| Service address | LLC agent must have a street address; corporate agent resides or is located in Nevada with a street address. Separate mailing address may be used, but a mailbox alone is not the service office | [NRS 86.231](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec231); [78.090](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec090) |
| Management | LLC default is member management, subject to law/governing documents. Articles can provide manager management; managers need not be members | [NRS 86.291](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec291) |

A commercial agent and manager management are choices to evaluate, not compulsory defaults for every founder. Record actual authority; do not select nominees to conceal control.

### 3. Prepare articles, list and licence

| Filing | Information and timing | Official source |
| --- | --- | --- |
| LLC articles | Name, agent, signing organizers' names/addresses; initial managers or initial members if member-managed; series-authorization statement if applicable; restricted-LLC statement if applicable | [NRS 86.161](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec161) |
| LLC duration | Perpetual unless articles or operating agreement provide otherwise | [NRS 86.155](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec155) |
| Corporation articles | Name, agent, authorized stock/classes/series or permitted board determination, first directors' names/addresses, signing incorporators' names/addresses | [NRS 78.035](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec035) |
| Corporate management | At least one natural-person director aged at least 18; president, secretary and treasurer or equivalents; one natural person may hold multiple offices | [NRS 78.115, 78.130](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec115) |
| LLC initial list | With articles unless SOS allows alternative due date; all managers or, if none, managing members; residence or business addresses; authorized signature and declarations | [NRS 86.263(1)-(4), (12)](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec263) |
| Corporate initial list | With articles unless alternative due date allowed; president, secretary, treasurer or equivalents and all directors; residence or business addresses, signature and declarations/public-company information | [NRS 78.150](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec150) |
| State licence | Obtain with required initial/annual list. Domestic organization itself can constitute conducting business. Local licences are additional | [NRS 76.100](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec100) |
| Claimed exemption | Apply actual exclusion/exemption and application/renewal rules; do not assume a nonprofit, rental or home-business exclusion applies to an ordinary for-profit LLC | [NRS 76.020, 76.105](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec105) |
| Professional entity | Additional profession/owner information, regulating-board certificates, naming and ownership/service restrictions | [NRS 89.040, 89.050, 89.070](https://www.leg.state.nv.us/NRS/NRS-089.html#NRS089Sec040) |

Counsel should settle stock rights, optional governance/indemnification provisions, bylaws or operating agreement and transfer restrictions. NRS 78.037 permits lawful optional provisions; it does not replace required articles information.

**Public-record privacy.** Manager-managed articles name the initial managers rather than every passive member; lists identify managers or managing members as applicable. Private member/manager records must still be maintained, and NRS 86.246 provides for custodian information and law-enforcement requests. Do not promise anonymity from agencies, banks, courts or creditors. Residence or business addresses are allowed for the listed persons; the old blanket prohibition on a legitimate agent business address for every manager was not in the cited list statute. [NRS 86.161, 86.241, 86.246, 86.263](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec241).

### Rates, bands and thresholds: ordinary state charges in 2026

Exclude optional services, processing charges, private agent/legal/trustee fees, local/professional licences, transfers and other states. Substantiated statutory exemptions can change totals.

| Item | Amount and condition | Official source |
| --- | --- | --- |
| LLC articles / foreign LLC registration | $75 | [NRS 86.561(1)(a)](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec561) |
| LLC initial list / annual list | $150 each | [NRS 86.263(4)](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec263) |
| Ordinary LLC state licence | $200 application / $200 renewal | [NRS 76.100(2)(c), 76.130(1)](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec100) |
| Ordinary LLC totals | $425 formation = $75 + $150 + $200; $350 annual = $150 + $200 | [NRS 86.561](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec561); [86.263](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec263); [76.100, 76.130](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec100) |
| Chapter 78 corporation initial list | $150, independently of articles fee | [NRS 78.150(4)(a)](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec150) |
| Chapter 78 corporation licence | $500 application / $500 renewal | [NRS 76.100(2)(c), 76.130(2)](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec100) |
| Minimum profit-corporation totals | $725 formation = $75 minimum articles + $150 initial list + $500 licence; $650 annual = $150 minimum list + $500 licence | [NRS 78.760, 78.150](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec760); [76.100, 76.130](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec100) |
| LLC amendment/restatement/correction | $175 for specified filings; agent changes have separate rules | [NRS 86.561(1)(b)](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec561) |
| Corporate capital increase | Difference in articles fee computed before/after increase; minimum $175 | [NRS 78.765(1)](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec765) |
| Specified certificate of corporate existence | $50; obtain certificate/recency required by receiving state | [NRS 78.785(5)-(7)](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec785); [86.561(3)](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec561) |

### Corporation capital fees

For articles fees, aggregate par value is subject to a **$0.001 per-share floor**. A no-par share, including no prescribed par value, is valued at **$1**. Combine par/no-par components. This is a statutory fee measure, not the issue price. For multiple classes with different par values or unlimited stock, obtain the SOS calculation. [NRS 78.760(3)-(4)](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec760); [SOS calculator scope note](https://www.nvsos.gov/businesses/commercial-recordings/forms-fees/all-business-forms/filing-fee-calculator).

| Statutory amount represented by authorized stock | Articles fee | Annual list fee | Official source |
| --- | --- | --- | --- |
| $75,000 or less | $75 | $150 | [NRS 78.760(1), 78.150(4)(b)](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec760) |
| Over $75,000 to $200,000 | $175 | $200 | [NRS 78.760(1), 78.150(4)(b)](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec150) |
| Over $200,000 to $500,000 | $275 | $300 | same |
| Over $500,000 to $1,000,000 | $375 | $400 | same |
| Over $1,000,000 | $375 for first $1,000,000 plus $275 per additional $500,000 or fraction | $400 for first $1,000,000 plus $275 per additional $500,000 or fraction | same |
| Maximum | $35,000 original articles; $34,925 subsequent stock-increase instrument, subject to applicable minimum | $11,125 annual list | [NRS 78.760(2), 78.765, 78.150(4)(b)](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec760) |

Do not substitute raw share count, add $375 per extra million shares, or quote a flat annual corporate list. These correct old errors; they are not claimed as 2026 legislative changes.

### 4. Submit through the current route and check acceptance

The [SOS LLC page](https://www.nvsos.gov/sos/businesses/start-a-business/limited-liability-company) and [Business Hub forms](https://bizhub.nv.gov/business-forms) now direct online filings to **ORION**, https://orion.nv.gov/. Use their current links; the SilverFlume-only instruction is outdated. The SOS page limits online articles to Chapter 86 LLCs and states conditions for online list filing, including the exemption limitation.

For paper filing, select the Business Hub's **Formation - Limited-Liability Company** or **Formation - Profit Corporation** packet, combining articles, initial list and state licence; include its **Customer Order Form** and payment as directed. Use the statutory information in steps 2-3 and inspect the current complete packet before submission. This pass did not inspect authenticated ORION screens or all PDF fields, so it does not invent numbered boxes or guaranteed service times.

Review entity/name, agent acceptance, management, stock and exemption evidence; reconcile the charges. After filing, retain articles/certificate, list, licence or exemption evidence, receipt and entity identifier; check public status and record the actual renewal date. The LLC filing/payment certificate is provided under 86.151; signing as organizer or being named manager does not alone make someone a member. List/payment evidence is addressed by 86.266 and 78.155. [NRS 86.151, 86.266](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec151); [78.155](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec155).

### 5. Set up records and tax handoffs

Document ownership, contributions, stock, authority, distribution decisions, transfer restrictions and any right of first refusal in the operating agreement/bylaws and records. Keep company accounts separate and record contributions/distributions, including property values and dates. These controls support separation; they do not guarantee a litigation outcome. [NRS 86.241, 86.286, 86.311, 86.321, 86.376](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec241).

Determine federal classification, EIN and filing needs through the federal owners in Scope. Do not promise every single-member LLC needs a separate EIN or every receipt goes on one schedule. Use `us-crypto-tax` for digital assets, `us-fbar-and-fatca-8938` for relevant foreign accounts, and `us-form-1041-trust-and-estate-income` / `us-estate-gift-706-709` for trust filing and gifts, with `us-form-1040-individual-return` for grantor income. Rental classification belongs with the applicable rental/federal return skills.

Run the Nevada business, payroll and sales-tax skills for activities actually triggered. Formation charges are separate from those taxes. In particular, the old assertion that every entity below the Commerce threshold must file a zero return is not retained: use `nv-commerce-and-mbt` for its actual filing test.

## Boundary and exception table

### Charging orders: personal creditor versus company debt

| Situation | Rule or response | Official source |
| --- | --- | --- |
| Personal judgment against member | Court may charge member's interest; creditor has only assignee rights to that extent | [NRS 86.401(1)](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec401) |
| One or multiple members | Exclusive remedy expressly covers both; subsection 2(a) prohibits foreclosure and its other specified remedies against the membership interest | [NRS 86.401(2)(a)](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec401) |
| Written creditor agreement | Statute does not supersede a written member/creditor agreement not conflicting with articles/operating agreement; applicable exemptions preserved | [NRS 86.401(2)(b)-(c)](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec401) |
| Transfer / management | Assignee does not obtain management/membership merely through transfer; governing documents and required approval matter | [NRS 86.351](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec351) |
| Company's own debt | Member-liability limitation does not erase company debts or a signed assumption of liability | [NRS 86.371](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec371) |
| Alter ego | Influence/control, inseparable unity of interest/ownership, and fraud or manifest injustice from respecting separation are the statutory elements; court determines | [NRS 86.376](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec376) |
| Creditor-sensitive transfer | Assess intent, value, solvency and statutory circumstances, including existing/later creditors; refer before transferring | [NRS 112.160, 112.180, 112.190](https://www.leg.state.nv.us/NRS/NRS-112.html#NRS112Sec180) |
| Bankruptcy, federal liens, guarantees or another state's enforcement | Separate review; the Nevada membership-interest provision is not a conclusion under those regimes | [NRS 86.401, scope](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec401) |

**AUDIT FLASH POINT.** Review distribution discretion, transfer restrictions, authority and actual separate records with counsel. Do not promise that a charging-order creditor must bear "phantom K-1 income": the old Rev. Rul. 77-137/Tax Court characterization was not verified. The old Florida/Olmstead comparison was not reverified either. A commingling incident must be evaluated under the legal test; it is not an automatic statutory loss of every shield.

### Spendthrift trust / DAPT conditions and referral

| Question | Statutory condition | Official source |
| --- | --- | --- |
| Nevada connection and trustee | 166.015(1) states alternative connections. If settlor is beneficiary, at least one trustee must meet subsection 2: Nevada-resident/domiciled individual, qualifying trust company with Nevada office, or qualifying bank with Nevada office and trust powers. Solicitation-only foreign independent trust company is excluded as specified | [NRS 166.015](https://www.leg.state.nv.us/NRS/NRS-166.html#NRS166Sec015) |
| Records / administration | Assess powers to maintain records/prepare tax returns and Nevada administration where relying on subsection 1(d); do not require every alternative connection to exist | same |
| Writing / retained powers | Self-benefiting writing must be irrevocable, meet distribution conditions, and not be intended to hinder, delay or defraud known creditors. Subsections 2-3 preserve specified veto, appointment, use, investment and other powers, not unilateral distributions to self without another person's consent | [NRS 166.020, 166.040](https://www.leg.state.nv.us/NRS/NRS-166.html#NRS166Sec040) |
| Side agreements | Greater retained powers than the instrument confers cannot be created by an express or implied side agreement | [NRS 166.045](https://www.leg.state.nv.us/NRS/NRS-166.html#NRS166Sec045) |
| Creditor existing at transfer | Later of two years from transfer and six months from actual/reasonably discoverable discovery. No universal two-year outside cap. Qualifying public record counts as discovery | [NRS 166.170(1)(a), (2)](https://www.leg.state.nv.us/NRS/NRS-166.html#NRS166Sec170) |
| Creditor arising later | Two years from transfer under subsection 1(b) | [NRS 166.170(1)(b)](https://www.leg.state.nv.us/NRS/NRS-166.html#NRS166Sec170) |
| Several contributions | Later transfer does not restart earlier transfer's clock; distributions deemed from latest transfer under subsection 7 | [NRS 166.170(7)](https://www.leg.state.nv.us/NRS/NRS-166.html#NRS166Sec170) |
| Grounds for challenge | Clear and convincing proof of Chapter 112 fraudulent transfer OR violation of enforceable contractual/court-ordered legal obligation owed to that creditor; apply time-bar provisions too | [NRS 166.170(3), (8)](https://www.leg.state.nv.us/NRS/NRS-166.html#NRS166Sec170) |
| General fraudulent-transfer limitation | Chapter 112's general limitation section does not apply to Chapter 166 spendthrift-trust transfers | [NRS 112.230(2)](https://www.leg.state.nv.us/NRS/NRS-112.html#NRS112Sec230) |

Counsel must check the instrument, voluntary/involuntary transfer restraint and the specific exceptions to distribution limits in 166.040(2). Do not reduce them to "all mandatory interests prohibited." NRS 166.050 does not require a particular magic phrase; the instrument must actually create the intended trust.

Keep assets, debt, values, solvency before/after, retained assets, purpose, known/threatened claims, contracts/orders, transfer/perfection/discovery dates and distribution decisions in the funding file. Insider transfers, retained control, concealment, substantially all assets and insolvency are among the fraud indicators. A CPA solvency report is a review aid, not a statutory universal condition. Do not recommend transferring everything at once merely to simplify clocks. [NRS 112.160, 112.180](https://www.leg.state.nv.us/NRS/NRS-112.html#NRS112Sec180).

The old claims of blanket protection after two years, no relevant exception obligations, fraud as the only claim and fraud always escaping the trust limitation period were overbroad. Do not promise protection from one's own malpractice, family orders or enforcement outside Nevada. Federal grantor/non-grantor, completed/incomplete gift, estate inclusion and California ING/NING questions require the tax handoffs above and counsel.

### Series LLCs and professional entities

A series may be authorized under 86.296(2) and created by members adopting an operating agreement without separate articles. Parent articles need the series-authorization statement in 86.161(1)(e). The liability limitation in **86.296(3)** needs separate/distinct records and separately accounted assets, plus the limitation provision in articles or operating agreement. **86.1255 is a definition**, not the operative shield. [NRS 86.1255, 86.161, 86.296](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec296).

For rental, investment-asset or family series, identify each series' members/managers, assets, obligations and business purpose. Property may be held/conveyed in the series' name; the parent agent serves each series. Separate books, accounts, insurance identification and documented inter-series transfers help evidence the statutory segregation; naming cells alone does not. [NRS 86.236, 86.311](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec236).

Check deeds, lender consent, title insurance, other-state recognition and bankruptcy with counsel. Obtain federal classification/EIN advice; do not declare every series disregarded or rely on a proposed regulation as final. Creation without articles does not establish every series' licence, maintenance or other-state charge; that specific uncertainty remains in Sources.

Chapter 89 professional entities need board approvals, authorized owners and profession/service restrictions. NRS 89.060 preserves the professional relationship and associated liability; entity formation does not erase the practitioner's own liability. Do not transfer a professional interest into a holding company or DAPT without checking ownership/transfer restrictions and exceptions. [NRS 89.025, 89.030, 89.040, 89.060, 89.070](https://www.leg.state.nv.us/NRS/NRS-089.html#NRS089Sec060).

### Other-state qualification and defaults

For activities outside Nevada, obtain that state's actual qualification and separate tax tests. Record offices, employees, property, management and recurring transactions. Obtain its required certificate and recency, agent, authority application, fee and renewal calendar; do not extrapolate a universal safe harbour or fee.

For the reverse direction, Nevada foreign-LLC qualification excludes specified proceedings, internal meetings, bank accounts, passive ownership without more and isolated transactions completed within **30 days**, not part of similar transactions. Read regulated exceptions and preservation of other laws/jurisdiction in subsections 3-4. This is not a universal tax-nexus exemption. NRS 86.548's court-access restriction preserves contracts and ability to defend. [NRS 86.548, 86.5483](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec5483).

| Missing fact | Working-paper default |
| --- | --- |
| Residence / operating states | No Nevada tax-saving estimate; obtain facts and run relevant state skills |
| Stock classes/par value | No quote from share count alone; request capital schedule |
| Licence exemption | Budget ordinary charges until actual exemption/evidence established |
| Management/authority | Obtain founder decision; do not silently choose nominees or share count |
| Creditor/trust/series facts | No transfer recommendation; list missing facts and refer |
| Private or other-state costs | Obtain actual quote/official fee, not an old market range |

## Worked cases

### Case 1: original high-net-worth example, separate costs from legal implementation

**Original illustrative facts retained.** Dr. Sarah Chen, a Nevada-resident orthopedic surgeon, age 52, married with two adult children, has $1.2 million annual practice net income; a $2.5 million Henderson residence with $400,000 mortgage and no other debts; $4 million liquid securities; an $800,000 Reno commercial rental leased to a tenant unrelated to her practice; and $500,000 crypto in a hardware wallet. She reports no current litigation, $3 million umbrella and $1 million malpractice coverage, and worries future malpractice claims may exceed coverage. These invented inputs do not establish solvency or insurance recovery.

The old alternatives remain **Chen Family Holdings LLC**, **Chen Reno Commercial LLC**, **Chen Digital Asset LLC**, and a professional practice LLC, with possible Chapter 166 trust ownership. Counsel decides each formation and transfer. Residence/lender/title issues, rental liabilities and professional-entity restrictions need separate treatment. There is no categorical instruction to transfer the residence, keep the rental outside the trust, or stack two guaranteed shields. Preserve Sarah's own professional-liability exposure.

If counsel approves four nonexempt ordinary LLC/PLLC filings and no special extra state charges apply: **4 x $425 = $1,700** formation and **4 x $350 = $1,400** recurring lists/licences. Professional LLCs use the Chapter 86 fee linkage in [NRS 89.025, 89.030](https://www.leg.state.nv.us/NRS/NRS-089.html#NRS089Sec025). Agent, lawyer, trustee, professional/local licensing, mortgage, title and transfer costs remain separately quoted.

```oa-check
name: Nevada four approved LLC formations, state charges only
inputs:
  companies: 4
  articles: 75
  initial_list: 150
  licence: 200
  annual_list: 150
steps:
  - each_first: articles + initial_list + licence
  - total_first: companies * each_first
  - each_annual: annual_list + licence
  - total_annual: companies * each_annual
expected:
  each_first: 425
  total_first: 1700
  each_annual: 350
  total_annual: 1400
```

### Case 2: original rental example, distinguish known charges from a series quote

**Original illustrative facts retained.** Marcus Rivera, Nevada resident, personally owns five Las Vegas-area single-family rental homes worth $3.2 million, with $200,000 combined annual rent. He worries a tenant-injury claim at one home could reach the other four. **Rivera Real Estate Holdings, LLC**, Series A-E, is an alternative to five separately filed LLCs.

The series option needs the governing documents, limitation provision and actual records/asset segregation above. Deeds, tenant contracts, banking and insurance must identify the appropriate owner and be reviewed. New operations/property in another state need that state's law; a sale merely to an out-of-state buyer is not this skill's automatic foreign-qualification test. Federal return/EIN treatment needs its own determination.

Five separate ordinary LLCs have **$2,125** state formation charges and **$1,750** recurring lists/licences. One ordinary LLC has **$425/$350**. That comparison is not a confirmed series-package price: per-series licence/maintenance and all asset-transfer, lending, insurance, federal and other-state costs must be resolved before claiming series savings.

```oa-check
name: Nevada rentals, separately filed LLC count comparison
inputs:
  separate_companies: 5
  one_company: 1
  articles: 75
  initial_list: 150
  licence: 200
  annual_list: 150
steps:
  - first_each: articles + initial_list + licence
  - annual_each: annual_list + licence
  - five_first: separate_companies * first_each
  - five_annual: separate_companies * annual_each
  - one_first: one_company * first_each
  - one_annual: one_company * annual_each
expected:
  five_first: 2125
  five_annual: 1750
  one_first: 425
  one_annual: 350
```

### Case 3: original crypto example, preserve custody and tax referrals

**Original illustrative facts retained.** Jordan Park, a Nevada-resident software engineer employed by a Nevada tech company, has approximately $4.5 million crypto accumulated over eight years in two hardware wallets (Ledger and Trezor) and a Coinbase Custody account. Jordan reports no current creditors and concerns about a future failed startup, hacking/key loss and transferring assets to children at death. **Park Digital Assets LLC** is the proposed manager-managed single-member vehicle, with Jordan sole member and manager, subject to the actual decision.

One ordinary nonexempt LLC costs **$425** in listed state formation charges and **$350** in annual list/licence charges. Private costs are quoted separately. A DAPT decision is based on the actual legal/cost analysis, not a holdings threshold.

If approved, document contributed assets, values, transfer dates, transaction hashes, ownership/authority, agreed capital and authorized key access. Match entity account terms and separately document personal distributions/spending. A device label, safe-deposit box or key location alone does not determine title or alter ego; apply [NRS 86.311, 86.321 and 86.376](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec311). Obtain the custodian's actual onboarding requirements.

Use `us-crypto-tax` for disposals and broker reporting; contributions of appreciated property and any investment-company exception need separate federal entity-tax advice, `us-fbar-and-fatca-8938` for relevant foreign accounts, and the trust/gift skills above for a trust transfer. Do not assert every disposal is capital, every foreign wallet reportable, every contribution tax-free or Nevada formation determinative of sales tax.

```oa-check
name: Nevada digital-asset LLC, state charges only
inputs:
  articles: 75
  initial_list: 150
  licence: 200
  annual_list: 150
steps:
  - first_state: articles + initial_list + licence
  - annual_state: annual_list + licence
  - first_two_years_state: first_state + annual_state
expected:
  first_state: 425
  annual_state: 350
  first_two_years_state: 775
```

### Case 4: stock terms change the corporate filing bill, both ways

For **10,000,000 shares at $0.0001 par**, fee par is floored at **$0.001**: fee capital **$10,000**, articles **$75**, initial list **$150**, licence **$500**, total **$725**. For **10,000,000 no-par shares**, fee capital is **$10,000,000**. Above the first $1,000,000 are **18** additional $500,000 units: articles **$375 + 18 x $275 = $5,325**, total **$5,975** with list/licence. The **$5,250** difference comes from the stock terms, not business valuation or an income-tax saving. Counsel settles suitable stock rights before optimizing a filing charge.

The official SOS calculator reproduced **$725** for 10,000,000 par shares using fee par 0.001 and **$5,975** for 10,000,000 no-par shares on 2026-11-14. [NRS 78.760](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec760); [SOS calculator](https://www.nvsos.gov/businesses/commercial-recordings/forms-fees/all-business-forms/filing-fee-calculator).

```oa-check
name: Nevada corporate articles, par floor versus no-par
inputs:
  shares: 10000000
  stated_par: 0.0001
  fee_par_floor: 0.001
  no_par_value: 1
  initial_list: 150
  corporation_licence: 500
steps:
  - par_capital: shares * max(stated_par, fee_par_floor)
  - par_articles: 75
  - par_total: par_articles + initial_list + corporation_licence
  - no_par_capital: shares * no_par_value
  - additional_units: ceil((no_par_capital - 1000000) / 500000)
  - no_par_articles: min(35000, 375 + additional_units * 275)
  - no_par_total: no_par_articles + initial_list + corporation_licence
  - difference: no_par_total - par_total
expected:
  par_capital: 10000
  par_total: 725
  no_par_capital: 10000000
  additional_units: 18
  no_par_articles: 5325
  no_par_total: 5975
  difference: 5250
```

## When to refuse or refer

- Refuse illegal concealment or tax-evasion assistance. NRS 86.141 and 78.030 prohibit illegal purpose/fraudulent concealment intent.
- Refer actual/threatened creditor, divorce/support, guarantee or insolvency facts before asset-protection advice. A known creditor is not automatically proof every transfer is fraudulent; apply the law.
- Refer DAPT drafting, retained powers, transfer validity, spouse/community property, estate/gift/income-tax coordination and outside-Nevada enforcement.
- Refer professional/regulated business approvals and ownership; ordinary articles do not license a profession.
- Refer series licence/maintenance, federal classification, recognition elsewhere and bankruptcy before quoting a complete structure cost.
- Refer institutional finance, multiple stock classes, unusual par/unlimited stock and conversion/redomestication; obtain actual investor requirements.
- If no Nevada activity, residence or formation objective is identified, document the missing business rationale and compare home-state formation. Lack of Nevada activity alone is not a statutory sham finding.
- Resolve Sources' open items before implementing an exempt entity, specialist structure or authenticated portal transaction.

## Filing and payment

| Event | Deadline or consequence | Official source |
| --- | --- | --- |
| Initial list | With articles unless SOS allows alternative due date | [NRS 86.263](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec263); [78.150](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec150) |
| Annual list | Last day of applicable anniversary month; record allowed alternative due date | same |
| Licence | With applicable initial list; renew with annual list, subject to substantiated exemption | [NRS 76.100, 76.105, 76.130](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec130) |
| List default | $75 penalty in addition to applicable list fee | [NRS 86.272](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec272); [78.170](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec170) |
| Missing initial licence / late renewal | $100 penalty under applicable provision plus licence fee; missing licences can require fees/penalties for each unlicensed year. Not "$100 per month capped at $100" | [NRS 76.110, 76.130](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec110) |
| Willful failure or neglect | A person conducting business in Nevada who willfully fails or neglects to obtain/renew the required licence and pay the required fees is subject to a $1,000-$10,000 fine recovered in court. NRS 76.180 also provides enforcement and prevailing-prosecutor costs; it does not label this a misdemeanor | [NRS 76.180](https://www.leg.state.nv.us/NRS/NRS-076.html#NRS076Sec180) |
| Continued default | Revocation/forfeiture on first day of first anniversary of month following month filing was required | [NRS 86.274](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec274); [78.175](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec175) |
| Ordinary reinstatement | Required information, delinquent lists/fees/penalties plus $300; stated procedure does not allow reinstatement after five consecutive revoked years | [NRS 86.276](https://www.leg.state.nv.us/NRS/NRS-086.html#NRS086Sec276); [78.180](https://www.leg.state.nv.us/NRS/NRS-078.html#NRS078Sec180) |

Reconcile licence/list penalty interaction under NRS 76.110(1)(a)(3) and 76.130(4)(a)(3); do not double-charge a substituted penalty. Entity revocation, licence status and taxes are distinct.

## Completion checklist

- [ ] Residence, operating states, purpose, owners/authority and investor needs documented.
- [ ] Correct type/name, agent street address/acceptance, articles, initial list and licence/exemption matched.
- [ ] Corporate capital measure, par floor, articles fee, initial list and annual-list band recomputed.
- [ ] Filed documents, receipts, identifier, public status and actual renewal date retained.
- [ ] Governing documents, contributions, books, banking/custody and distribution/transfer controls recorded.
- [ ] Charging-order limits, alter ego, guarantees and claims surfaced; no promised creditor immunity.
- [ ] Trust referral includes instrument, qualifying trustee/connection, transfer/discovery dates, solvency, obligations and contribution clocks.
- [ ] Series referral includes governing provisions, distinct assets/records, deeds/contracts, insurance and unresolved licence/federal/other-state questions.
- [ ] Board approvals, local licences, other-state qualification and federal/Nevada tax handoffs completed or expressly deferred.
- [ ] Reviewer package contains entity-choice memo, formation checklist, first-year/recurring cost schedules, governance questions, trust/qualification supplements where relevant, and open-item/signoff record. Verified charges and unpriced services are distinct.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Nevada Legislature, Chapter 86. Read for 86.1255; 86.141-86.171; 86.231-86.276; 86.286-86.321; 86.351, 86.371, 86.376, 86.401; 86.548-86.5483; 86.561, with neighbouring conditions, series/disclosure and reinstatement exceptions. | https://www.leg.state.nv.us/NRS/NRS-086.html | 2026-11-14 |
| Nevada Legislature, Chapter 78. Read for 78.030-78.039, 78.090, 78.115-78.130, 78.150, 78.155, 78.170-78.180, 78.760-78.785: articles, lists, capital measures, fee bands/caps and default rules. | https://www.leg.state.nv.us/NRS/NRS-078.html | 2026-11-14 |
| Nevada Legislature, Chapter 76. Read for definitions/exclusions and 76.100, 76.105, 76.110, 76.130, 76.180: corporate fees, exemptions, local-licence distinction, penalties and willful-failure fine/enforcement. | https://www.leg.state.nv.us/NRS/NRS-076.html | 2026-11-14 |
| Nevada Legislature, Chapter 77. Read for 77.300/77.310 address and acceptance rules with commercial/noncommercial definitions and neighbouring registration provisions. | https://www.leg.state.nv.us/NRS/NRS-077.html | 2026-11-14 |
| Nevada Legislature, Chapter 89. Read for 89.025-89.040, 89.060 and ordinary ownership/transfer restrictions in 89.070; profession-specific exceptions need counsel. | https://www.leg.state.nv.us/NRS/NRS-089.html | 2026-11-14 |
| Nevada Legislature, Chapter 166. Read for 166.015-166.050, restraints and 166.170: existing/later creditors, discovery, enforceable obligations, multiple transfers and time bars. | https://www.leg.state.nv.us/NRS/NRS-166.html | 2026-11-14 |
| Nevada Legislature, Chapter 112. Read for definitions/solvency, 112.180-112.190 fraud tests and 112.230(2)'s trust exception. | https://www.leg.state.nv.us/NRS/NRS-112.html | 2026-11-14 |
| Nevada Constitution art.10 section1(9). Read for natural-person prohibition and express business-income/revenue qualification. | https://www.leg.state.nv.us/Const/NvConst.html#Art10Sec1 | 2026-11-14 |
| SOS LLC start page, ordinary browser. Read for ORION route, Chapter86 online-articles limitation, list/exemption condition and professional/foreign routes. | https://www.nvsos.gov/sos/businesses/start-a-business/limited-liability-company | 2026-11-14 |
| Business Hub forms, ordinary browser. Read for LLC/corporation packet entries, Customer Order Form instruction and ORION route. Only first LLC PDF page visually inspected; no packet fee figure relied on. | https://bizhub.nv.gov/business-forms | 2026-11-14 |
| SOS corporate fee calculator, ordinary browser. Read for scope/minimum-par field; tested 10,000,000 par shares at fee par0.001 ($725 total) and 10,000,000 no-par shares ($5,975), including list/licence. | https://www.nvsos.gov/businesses/commercial-recordings/forms-fees/all-business-forms/filing-fee-calculator | 2026-11-14 |

Not yet confirmed: complete current PDF fields and authenticated ORION screens; expedite/service/payment-processing charges and turnaround times; per-series Nevada licence/annual-maintenance treatment; full profession-specific exceptions and regulated licences; local fees; other states' current formation/qualification fees, penalties, series recognition and trust-creditor outcomes; federal series/EIN, charging-order income, crypto contribution/reporting, trust income/gift/estate and California ING/NING rules. Resolve through routed skills and counsel before implementation. Old private-agent/legal/trustee market prices, foreign-processing estimates, automatic state rankings and universal creditor-protection promises are not usable official guidance. Figures with another owner are linked above.
