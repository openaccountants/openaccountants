---
name: tx-formation
description: "Form a Texas business entity or register an out-of-state one in Texas, and set up its Texas tax side, for 2026. Covers the Texas LLC (Form 205, $300), the for-profit corporation (Form 201, $300), the series LLC, registering a foreign LLC or corporation (Forms 304 and 301, $750), registered agent changes ($15), the separate Comptroller side (franchise tax account, the annual Public Information Report due 15 May even when no tax is owed, forfeiture and personal liability), when an out-of-state entity has franchise tax nexus ($500,000 of Texas receipts or physical presence), the end of federal beneficial ownership reporting for US companies, and how to choose Texas or another state. Texas has no individual income tax. Trigger on \"form an LLC in Texas\", \"Texas LLC\", \"Certificate of Formation\", \"Form 205\", \"Texas series LLC\", \"foreign LLC Texas\", \"Form 304\", \"Texas registered agent\", \"Texas vs Delaware\", \"Public Information Report\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tx-formation"
  jurisdiction: "US-TX"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Texas entity formation and registration, 2026

> **Source-cited draft.** Built from Texas Secretary of State Forms 205 and 304, Business Organizations Code Chapter 4 (filing fees), the Texas Comptroller's 2026 franchise tax instructions (Form 05-915) and 2026 forms page, Comptroller Rule 3.586 (STAR 202601004R), Tax Code Chapter 171, Article 8 of the Texas Constitution and FinCEN's beneficial ownership page, read on 2026-11-13. No accountant or lawyer has reviewed it. Formation documents and operating agreements need a Texas-licensed attorney.

**Answer first.** A Texas LLC is formed by filing a Certificate of Formation (Form 205) with the Secretary of State for **$300**; a for-profit corporation also costs **$300**; an out-of-state LLC or corporation that transacts business in Texas registers for **$750**. Texas has **no annual Secretary of State report or fee** for these entities, but every LLC and corporation is a franchise tax entity with the Comptroller: each year by **15 May** it files a **Public Information Report** (Form 05-102), and pays franchise tax only if its annualized revenue is above **$2,650,000** (see `tx-franchise-tax`). Missing that report leads to forfeiture, and then the officers and directors become personally liable for the entity's new Texas debts. Since 2025, US-formed companies no longer file beneficial ownership reports with FinCEN.

## Who this applies to

In scope: a founder, owner or adviser forming a Texas LLC, series LLC or for-profit corporation, or registering an LLC or corporation formed elsewhere to transact business in Texas, in 2026: the Secretary of State filing and fee, the registered agent, the link to the Comptroller, the annual information report, nexus for franchise tax, and the choice of state.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Franchise tax computation, the no tax due test, E-Z and Long Form | `tx-franchise-tax` |
| Texas sales and use tax permit | the Texas sales tax skill named in this folder's README |
| Employer registration with the Texas Workforce Commission | `tx-payroll` |
| Federal classification (Form 8832) and the S corporation election (Form 2553) | `us-s-corp-election-decision` |
| A foreign-owned single-member LLC's Form 5472 | `us-form-5472-foreign-owned-us` |
| Formation rules of other states | `us-state-formation-matrix` |
| Nonprofit corporations, professional entities needing licensing-board approval, limited partnerships beyond a mention | Refer (see "When to refuse or refer") |

## Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Certificate of Formation, LLC (Form 205) | USD 300 | [Form 205, Texas Secretary of State](https://www.sos.state.tx.us/corp/forms/205_boc.pdf); [BOC 4.152(1), 4.154](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Certificate of Formation, for-profit corporation (Form 201) | USD 300 | [BOC 4.152(1)](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Registration of a foreign LLC (Form 304) | USD 750 | [Form 304, Texas Secretary of State](https://www.sos.state.tx.us/corp/forms/304_boc.pdf); [BOC 4.154](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Registration of a foreign corporation (Form 301) | USD 750 | [BOC 4.152(3)](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Certificate of formation or foreign registration, limited partnership | USD 750 | [BOC 4.155(1)](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Certificate of amendment (corporation; same fee for an LLC) | USD 150 | [BOC 4.152(2), 4.154](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Statement of change of registered office or agent (Form 401) | USD 15 | [BOC 4.152(6), 4.154](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Certificate of termination (corporation; same fee for an LLC) | USD 40 | [BOC 4.152(9), 4.154](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Name reservation | USD 40 | [BOC 4.151(2)](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Certificate of merger or conversion | USD 300 (plus any formation fee in a merger) | [BOC 4.151(5)](https://statutes.capitol.texas.gov/Docs/BO/htm/BO.4.htm) |
| Delayed effective date of a filing | Up to 90 days after signing | [Form 205, Effectiveness of Filing](https://www.sos.state.tx.us/corp/forms/205_boc.pdf) |
| Franchise tax no tax due threshold (2026 and 2027 reports) | USD 2,650,000 annualized total revenue | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/) |
| Franchise tax nexus for an out-of-state entity | USD 500,000 of Texas gross receipts in the federal accounting period, or physical presence | [Rule 3.586, STAR 202601004R](https://star.comptroller.texas.gov/view/202601004R) |
| Public Information Report, late filing penalty | USD 50 per report | [Texas Comptroller, franchise tax: penalties](https://comptroller.texas.gov/taxes/franchise/) |
| State tax on individuals' net income | None (prohibited) | [Texas Constitution, Article 8, Section 24-a](https://statutes.capitol.texas.gov/Docs/CN/htm/CN.8.htm) |

Franchise tax rates and the rest of its figures have one home: `tx-franchise-tax`.

## The base

### Forming a Texas LLC (Form 205)

1. **Name.** Must contain "limited liability company", "limited company" or an abbreviation of one of them, and must not falsely imply a link with a government entity (Form 205, Article 1 and Execution). Search availability on SOSPortal (USD 1 per search).
2. **Registered agent and office.** Either an organization (not the LLC itself) or an individual resident of Texas, at a Texas street address. The person filing affirms that the agent has consented (Form 205, Article 2 and Execution).
3. **Governing authority.** Manager-managed (list the initial managers) or member-managed (list the initial members), with names and addresses (Article 3). These names become public.
4. **Purpose.** The form's standard text: any lawful purpose under the Business Organizations Code (Article 4).
5. **Initial mailing address for franchise tax correspondence.** Form 205 asks for it: this is how the Comptroller first reaches the entity. Use an address someone reads.
6. **Supplemental provisions.** Anything else, including the series notice for a series LLC.
7. **Organizer, effectiveness and signature.** Effective on filing, at a later date up to 90 days after signing, or on a future event within 90 days.
8. File on SOSPortal or by mail to Secretary of State, P.O. Box 13697, Austin, TX 78711-3697, with USD 300.

After filing: get an EIN from the IRS; adopt a company agreement (not filed, but strongly advised, and essential for more than one member); open a bank account in the LLC's name; and register for any Texas taxes that apply (sales tax permit, TWC account). A single-member LLC is disregarded for federal income tax by default and a multi-member LLC is a partnership; either may elect corporate or S corporation treatment (`us-s-corp-election-decision`). None of this changes the Texas franchise tax treatment: the LLC is taxable for franchise tax whatever its federal status (Form 05-915, Disregarded Entities).

### Forming a for-profit corporation (Form 201)

The same steps, with: a name containing "corporation", "company", "incorporated", "limited" or an abbreviation; at least one initial director, named on the form; and the share structure. Fee USD 300 (BOC 4.152(1)). An S corporation election is federal only: for franchise tax an S corporation is taxable like any corporation (Form 05-915, Entities Subject to Tax).

### Series LLC

Texas allows an LLC to establish protected series (Business Organizations Code Chapter 101, Subchapter M). Each series can hold its own assets and members, and its debts can be enforced only against that series, but only if the certificate of formation gives notice of the limitation, the company agreement establishes the series, and each series keeps records accounting for its assets separately. Separate bank accounts, books, contracts and insurance in each series' name are what keep the shield; mixed records put it at risk. The series notice goes in Form 205's supplemental provisions; the fee is the same USD 300. For franchise tax, Form 05-915 lists "series LLCs" among taxable entities; how the Comptroller treats each protected series for reporting is not confirmed here (see Sources).

### Registering an out-of-state (foreign) entity (Forms 304 and 301)

An LLC or corporation formed elsewhere that transacts business in Texas registers with the Secretary of State: Form 304 (LLC) or Form 301 (corporation), USD 750 each. Form 304 asks for: the legal name, and an added identifier or an assumed name if the name lacks one or is taken in Texas; the EIN; the state and date of formation; a certificate that it exists validly at home; its purposes; the date it first transacted or will transact business in Texas (late fees may apply if that date has passed); the principal office; and a Texas registered agent. Registration with the Secretary of State and franchise tax nexus with the Comptroller are separate tests: an entity can owe franchise tax filings without being required to register, and the reverse. Transacting business without registering limits the entity's right to sue in Texas until it registers; refer the specifics to counsel.

### The Comptroller side: the annual information report

Every LLC and corporation formed in Texas or doing business in Texas is a franchise tax taxable entity. Each year by 15 May (17 May 2027, because 15 May 2027 is a Saturday):

- at or below USD 2,650,000 of annualized revenue: file only the **Public Information Report (Form 05-102)**, or the Ownership Information Report (Form 05-167) for entities that use it; no franchise tax report and no tax;
- above it: file the E-Z or Long Form report as well, under `tx-franchise-tax`.

The No Tax Due Report (Form 05-163) was discontinued for reports due from 1 January 2024. A pre-qualified new veteran-owned business files no PIR or OIR for its first five years ([2026 franchise forms page](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php)). The PIR names the officers, directors, managers or members and the registered agent, so this information is public.

**Forfeiture.** If the reports or payments are not made within 45 days of a Notice of Intent to Forfeit Right to Transact Business (Form 05-211), the entity's right to transact business may be forfeited; if it still does not file or pay within 120 days after that, its Secretary of State registration may be forfeited (Form 05-213). Once the right to transact business is forfeited, the officers and directors are personally liable for each debt created or incurred in Texas after the due date and before revival (Tax Code 171.255; Form 05-915, Forfeiture). An entity at or below the threshold cures this by filing its PIR or OIR (Comptroller franchise tax page, July/August 2026 notices).

### Franchise tax nexus for an out-of-state entity

A foreign entity has Texas nexus, and so a franchise tax filing duty, if it has physical presence in Texas (an office, employees, property, or acting as general partner of a partnership doing business in Texas, among others), or, for each federal accounting period ending in 2019 or later, Texas gross receipts of USD 500,000 or more ([Rule 3.586, STAR 202601004R](https://star.comptroller.texas.gov/view/202601004R)). There is no separate payroll or property dollar test in the rule. Nexus means it files a PIR or report; tax is owed only above the no tax due threshold. Sales tax registration has its own test, in the sales tax skill.

### Federal beneficial ownership (BOI) reporting

FinCEN's interim final rule of March 2025, made permanent by a final rule on 11 August 2026, exempts companies created in the United States from beneficial ownership reporting under the Corporate Transparency Act, and removes the need to report US persons as beneficial owners. Entities formed outside the US and registered to do business in a US state (formerly "foreign reporting companies") may still have to report ([FinCEN, Beneficial Ownership Information](https://www.fincen.gov/boi)). A Texas LLC or corporation files no BOI report.

### Texas or another state?

There is no Texas tax on individuals' net incomes (Constitution Art. 8, Sec. 24-a), and from Texas's side the cost of forming in Texas is the USD 300 formation fee, against USD 750 to register an entity formed elsewhere, on top of that other state's own fees and annual charges. The Texas franchise tax, the PIR and the Comptroller rules apply to both. So:

| Owner profile | Usual answer, for an attorney to confirm |
| --- | --- |
| Texas-based freelancer, consultant or small business, one owner | Texas LLC |
| Several owners, operating in Texas, no outside investors planned | Texas LLC with a written company agreement |
| Startup planning to raise institutional venture capital | Often a Delaware corporation registered in Texas, because investors ask for it; the legal reasons are outside this skill |
| Several rental properties, one owner, who will keep separate books for each | Texas series LLC, or one LLC per property |
| Non-US founder with no US presence | Texas LLC is possible; the federal Form 5472 duty follows (`us-form-5472-foreign-owned-us`) |

## Deadlines and filing

| What | When | Where |
| --- | --- | --- |
| Certificate of Formation or foreign registration | Before or when business starts; a foreign entity gives the date it first transacted business in Texas | SOSPortal or Secretary of State, P.O. Box 13697, Austin, TX 78711-3697 |
| Change of registered agent or office (Form 401) | When it changes | Secretary of State, USD 15 |
| Public Information Report or Ownership Information Report | Every year by 15 May (17 May 2027) | Comptroller Webfile |
| Franchise tax report, if above USD 2,650,000 | Same date | Comptroller (`tx-franchise-tax`) |
| Ending the entity | Clear all franchise tax first: get a certificate of account status from the Comptroller (Webfile or Form 05-359); documents to terminate must reach the Secretary of State by 5:00 p.m. on 31 December (or the last working day) to avoid the next annual report (Form 05-915, Final Reports) | Comptroller, then Secretary of State (USD 40 termination) |

## Penalties and interest

| Failure | Consequence | Source |
| --- | --- | --- |
| PIR or report filed late | USD 50 per report | Comptroller franchise tax page |
| Tax paid late | 5% (1 to 30 days) or 10% (over 30 days), plus interest from day 61 | Comptroller franchise tax page |
| Reports not filed within 45 days of Form 05-211 | Right to transact business forfeited; officers and directors personally liable for new Texas debts (171.255) | Form 05-915, Forfeiture |
| Still not filed 120 days after that | Secretary of State registration forfeited | Form 05-915, Forfeiture |

## Cross-border points

| Situation | Treatment |
| --- | --- |
| Entity formed in another state, operating from Texas | Register in Texas (USD 750); franchise tax and PIR apply as for a Texas entity |
| Out-of-state seller with Texas receipts under USD 500,000 and no physical presence | No franchise tax nexus for that period |
| Out-of-state seller at USD 500,000 or more of Texas receipts | Nexus: PIR, and a report if above USD 2,650,000; consider Secretary of State registration separately |
| Non-US founder of a Texas LLC | Texas side as for anyone; federal Form 5472 and pro forma Form 1120 (`us-form-5472-foreign-owned-us`); no BOI report for a US-formed company |
| Entity formed outside the US and registered in Texas | May still have BOI reporting (FinCEN) |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| No one reads mail at the franchise tax mailing address or registered office | Forfeiture notices go unread; personal liability follows |
| Several LLCs under common ownership | Franchise tax combined group rules apply one threshold to the group |
| Series LLC run from one bank account | The series shield may fail |
| Operating in Texas through an unregistered out-of-state entity | Late fees and limits on suing in Texas courts |
| Revenue heading over USD 2,650,000 | Franchise tax on the whole margin from that year (`tx-franchise-tax`) |

## Two worked examples that recompute

**Example 1, a decision: form in Texas, or form elsewhere and register?** A single owner in Austin will run a consulting business only in Texas. Texas Secretary of State cost of forming in Texas: USD 300. Cost of forming in another state and registering in Texas: USD 750 in Texas, plus the other state's formation fee and any annual fee there. The Texas-only difference is USD 450 before the other state's fees, and the franchise tax and PIR are the same either way. Unless investors require another state, form in Texas.

```oa-check
name: Texas fees, form in Texas against register a foreign LLC
inputs:
  texas_formation: 300
  foreign_registration: 750
steps:
  - extra_texas_cost: foreign_registration - texas_formation
expected:
  extra_texas_cost: 450.00
```

**Example 2, an out-of-state LLC selling into Texas.** A Colorado LLC with no office or staff in Texas has total revenue of USD 1,900,000 for calendar year 2026, of which USD 620,000 is Texas gross receipts. Its Texas receipts are USD 120,000 over the USD 500,000 nexus test, so it has nexus for 2026 and must file a 2027 PIR (and register with the Comptroller). Its total revenue is USD 750,000 under the USD 2,650,000 threshold, so it owes no franchise tax and files no franchise tax report.

```oa-check
name: Out-of-state LLC, nexus and the no tax due threshold (2027 report)
inputs:
  texas_receipts: 620000
  nexus_test: 500000
  total_revenue: 1900000
  threshold: 2650000
steps:
  - over_nexus: texas_receipts - nexus_test
  - under_threshold: threshold - total_revenue
expected:
  over_nexus: 120000.00
  under_threshold: 750000.00
```

## Ask the client first

1. **Who owns it, and will there be outside investors?** One owner, several, a company, or a non-US person; and whether venture investors are expected.
2. **Where does the business operate and sell?** Only Texas, or other states; for an out-of-state entity, Texas receipts in the year and any office, staff or property in Texas.
3. **Is there already an entity, formed in Texas or elsewhere?** If elsewhere, when it first did business in Texas.
4. **Who will be the registered agent, and at what Texas street address?** And which mailing address the Comptroller should use.
5. **Expected revenue, and any related entities?** For the franchise tax threshold and combined group rules.
6. **Several properties or business lines to keep apart?** For the series LLC question, and whether separate books will really be kept.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Texas Secretary of State, Form 205, Certificate of Formation, Limited Liability Company (revised 09/26). Read for the $300 fee, name words, registered agent, governing authority, purpose, the franchise tax mailing address, supplemental provisions, effectiveness (90 days) and the mailing address. | https://www.sos.state.tx.us/corp/forms/205_boc.pdf | 2026-11-13 |
| Texas Secretary of State, Form 304, Application for Registration of a Foreign Limited Liability Company. Read for the $750 fee and the required items, including the date business started and late fees. | https://www.sos.state.tx.us/corp/forms/304_boc.pdf | 2026-11-13 |
| Texas Secretary of State, Form 201, Certificate of Formation, For-Profit Corporation. Read for the name words and the minimum of one director. | https://www.sos.state.tx.us/corp/forms/201_boc.pdf | 2026-11-13 |
| Texas Business Organizations Code Chapter 4. Read for 4.151 (name reservation $40, merger or conversion $300), 4.152 (corporation: formation $300, amendment $150, foreign registration $750, change of agent $15, termination $40), 4.154 (LLC fees same as corporation) and 4.155 (limited partnership $750). | https://tcss.legis.texas.gov/resources/BO/htm/BO.4.htm | 2026-11-13 |
| Texas Secretary of State, SOSPortal. Read for the $1.00 search fee. | https://www.sos.state.tx.us/corp/sosda/index.shtml | 2026-11-13 |
| Texas Comptroller, Franchise Tax page. Read for the $2,650,000 threshold, the $50 late report penalty, payment penalties and the 2026 forfeiture notices. | https://comptroller.texas.gov/taxes/franchise/ | 2026-11-13 |
| Texas Comptroller, 2026 Franchise Tax Report Forms. Read for PIR/OIR-only filing at or below the threshold, the end of the No Tax Due Report and the new veteran-owned business exception. | https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php | 2026-11-13 |
| Form 05-915, 2026 Franchise Tax Report Information and Instructions. Read for entities subject to tax (including single member and series LLCs and S corporations), disregarded entities, final reports and termination timing, and forfeiture (45 and 120 days, personal liability). | https://comptroller.texas.gov/forms/05-915.pdf | 2026-11-13 |
| Comptroller Rule 3.586, Margin: Nexus (STAR 202601004R). Read for physical presence and the $500,000 receipts test. | https://star.comptroller.texas.gov/view/202601004R | 2026-11-13 |
| Texas Tax Code Chapter 171. Read for 171.255 (liability of directors and officers). | https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm | 2026-11-13 |
| Texas Constitution Article 8. Read for Section 24-a. | https://statutes.capitol.texas.gov/Docs/CN/htm/CN.8.htm | 2026-11-13 |
| FinCEN, Beneficial Ownership Information. Read for the March 2025 interim final rule and the 11 August 2026 final rule exempting US companies. | https://www.fincen.gov/boi | 2026-11-13 |

Not yet confirmed: the series LLC statute (Business Organizations Code Chapter 101, Subchapter M) was not reread for this version, so its three conditions are stated in outline; how the Comptroller requires protected series to report for franchise tax; the fee for Form 201 was read from the statute, as the form's fee line did not load; Secretary of State expedite fees and processing times were not read and are left out.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tx-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tx-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
