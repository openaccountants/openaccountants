---
name: fl-annual-report
description: "Florida Annual Report filing for LLCs and corporations registered with the Division of Corporations (Sunbiz). Covers the annual report requirement, $138.75 fee for LLCs, filing deadline, late filing penalties, and administrative dissolution risk. Primary source: Florida Statutes Chapter 605 (LLCs) and Chapter 607 (corporations)."
version: 1.1
jurisdiction: US-FL
tax_year: 2025
last_updated: 2026-11-25
depends_on:
  - us-tax-workflow-base
category: state
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Rob Hoffman"
reviewed_on: 2026-11-03
tier: 1
domain: formation
---

# FL Annual Report

## Florida Annual Report (Sunbiz) v1.1

## What this file is

**Obligation category:** EF (Entity Fees)
**Functional role:** Entity filing
**Status:** Correction draft; independent source review and accountant approval of this changed version pending. Retained approval fields do not certify these changes.

This is a Tier 2 content skill that loads on top of `us-tax-workflow-base`. It covers the Florida Division of Corporations annual report filing requirement for LLCs and corporations registered to do business in Florida. The annual report is NOT a tax return; it is an informational filing that keeps entity status active with the state.

**Tax year coverage.** This guide targets reporting year 2025: ordinarily due May 1, 2025 for entities whose effective organization/incorporation or qualification year precedes 2025. An entity effective on January 1, 2025 first reports in 2026.

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs off on the filing. The skill produces working papers and a brief, not the filed report itself.

## Section 1 -- Scope statement

**In scope:**

- Florida domestic LLCs (Chapter 605, F.S.)
- Florida domestic corporations (for-profit, Chapter 607, F.S.)
- Florida domestic not-for-profit corporations (Chapter 617, F.S.)
- Foreign LLCs and corporations registered to transact business in Florida
- The Sunbiz annual report form (filed online at sunbiz.org)
- Supplemental report for changes made between annual reports

**Out of scope (refused):**

- Limited partnerships (Chapter 620, F.S.) -- separate filing regime
- Sole proprietors with no LLC -- no annual report requirement
- Fictitious name (DBA) renewals -- separate process under §865.09, F.S.
- Federal tax return preparation
- Florida corporate income tax (Form F-1120) -- separate skill
- Reinstatement of administratively dissolved entities

## Section 2 -- Filing requirements

### Who must file

- **Who must file** — Every LLC, corporation, and not-for-profit corporation registered with the Florida Division of Corporations must file an annual report each year to maintain active status.  _(§605.0212, F.S. (LLCs); §607.1622, F.S. (corporations).)_

### When to file

**When to file**  _(See table)_

| Item | Detail | Source |
| --- | --- | --- |
| Filing window opens | January 1 of each year | Sunbiz filing instructions |
| Filing deadline | May 1 of each year | [605.0212](https://www.flsenate.gov/Laws/Statutes/2025/605.0212), subsection (3); [607.1622](https://www.flsenate.gov/Laws/Statutes/2025/607.1622) |
| Late filing (supplemental fee) | $400 after May 1 for covered LLC/profit reports; Chapter 617 nonprofits exempt | [607.193](https://www.flsenate.gov/Laws/Statutes/2025/607.193), subsection (2)(b) |
| Administrative dissolution/revocation | Third-Friday 5 p.m. Eastern filing cutoff; fourth-Friday legal event. In 2025: September 19 cutoff, September 26 event | [605.0714](https://www.flsenate.gov/Laws/Statutes/2025/605.0714); [607.1420](https://www.flsenate.gov/Laws/Statutes/2025/607.1420); [607.1530](https://www.flsenate.gov/Laws/Statutes/2025/607.1530) |

### How to file

**Non-usable hold:** The absolute paper-ban assertion below is not cleared. The online route is operational, but the statutes permit electronic forms and the nonprofit statute recognizes timely mail; the full operational/statutory conflict remains unresolved.

- **How to file** — The annual report must be filed electronically through the Division of Corporations website (sunbiz.org). Paper filings are not accepted for annual reports.  _(sunbiz.org)_

## Section 3 -- Fees

**Fees**  _(See table)_

| Entity type | Annual report fee | Source |
| --- | --- | --- |
| LLC (domestic or foreign) | $138.75 = $50 + $88.75 | [605.0213](https://www.flsenate.gov/Laws/Statutes/2025/605.0213), subsection (5); [607.193](https://www.flsenate.gov/Laws/Statutes/2025/607.193) |
| For-profit corporation (domestic or foreign) | $150.00 | [607.0122](https://www.flsenate.gov/Laws/Statutes/2025/607.0122), subsection (17); [607.193](https://www.flsenate.gov/Laws/Statutes/2025/607.193) |
| Not-for-profit corporation | $61.25 | [617.0122](https://www.flsenate.gov/Laws/statutes/2025/617.0122) |
| Late fee (covered LLC/profit entities; not Chapter 617 nonprofits) | $400.00 | [607.193](https://www.flsenate.gov/Laws/Statutes/2025/607.193) |
| Standalone registered-agent change | LLC $25; corporation $35 when outside its annual report. Do not infer an extra annual-report charge | [605.0213](https://www.flsenate.gov/Laws/Statutes/2025/605.0213), subsection (7); [607.0122](https://www.flsenate.gov/Laws/Statutes/2025/607.0122), subsection (4); [617.0122](https://www.flsenate.gov/Laws/statutes/2025/617.0122) |

## Section 3 -- Fees

- **Note on the $138.75 LLC fee** — The $138.75 consists of the $50 annual-report fee and $88.75 supplemental corporate fee; it is not a $100 report plus $38.75 agent charge. Annual-report agent changes are permitted; standalone change fees do not establish an extra charge on that report. [605.0213](https://www.flsenate.gov/Laws/Statutes/2025/605.0213); [607.193](https://www.flsenate.gov/Laws/Statutes/2025/607.193); [605.0114](https://www.flsenate.gov/Laws/Statutes/2025/605.0114).

## Section 4 -- Computation rules (Step format)

### Step 1: Determine filing obligation

- **Determine filing obligation** — - Confirm the entity is registered with the Florida Division of Corporations (search sunbiz.org by entity name or document number). - Confirm the entity's status is Active or Inactive (if inactive, this skill does not cover reinstatement). - The first report is due in the calendar year after the effective year of organization/incorporation or qualification, including an entity effective on January 1. Distinguish effective date from submission date. [605.0212](https://www.flsenate.gov/Laws/Statutes/2025/605.0212); [607.1622](https://www.flsenate.gov/Laws/Statutes/2025/607.1622); [617.1622](https://www.flsenate.gov/Laws/Statutes/2025/617.1622).  _(unsure)_

### Step 2: Gather required information

- **Gather required information**: entity name; organization/incorporation jurisdiction and date, and foreign qualification particulars where applicable; FEIN or the permitted no-number/applied-for status; principal and mailing addresses; registered-agent name/street address; for an LLC, name/title/address of at least one person authorized to manage, not a mandatory census of every manager/member/authorized person; for a corporation, the required directors and principal officers. Keep supplied information true and current. [605.0212](https://www.flsenate.gov/Laws/Statutes/2025/605.0212)(1); [607.1622](https://www.flsenate.gov/Laws/Statutes/2025/607.1622)(1); [617.1622](https://www.flsenate.gov/Laws/Statutes/2025/617.1622)(1).

### Step 3: Verify registered agent

- **Verify registered agent** — - The registered agent must be a Florida resident or a business entity authorized to transact business in Florida. - The registered agent's address must be a Florida street address (not a P.O. Box). - If changing the registered agent, the new agent must sign an acceptance.  _(unsure)_

### Step 4: Complete the filing

- **Complete the filing** — - Log in to sunbiz.org annual report filing system. - Enter the entity's document number. - Review pre-populated information and update any changes. - Confirm all manager/member or officer/director information is current. - Pay electronically or use the permitted mailed/courier check or money order with the required voucher. [Sunbiz instructions](https://efile.sunbiz.org/sbs_ar_instr.html).  _(unsure)_

### Step 5: Document the filing

- **Document the filing** — - Record the confirmation number provided by Sunbiz. - Save/print the filing confirmation for the entity's records. - Note the filing date for the reviewer brief.  _(unsure)_

## Section 5 -- Edge cases and special rules

### E-1: Entity formed mid-year

- **Entity formed mid-year** — An LLC formed on July 15, 2024, must file its first annual report by May 1, 2025. The report covers the entity's current information as of the filing date, not a specific fiscal period.  _(§605.0212, F.S.)_

### E-2: Multiple LLCs under same ownership

- **Multiple LLCs under same ownership** — Each LLC is a separate filing. There is no consolidated annual report. Each pays its own $138.75 fee. Flag for reviewer if client has many LLCs -- the aggregate cost may be significant.  _(unsure)_

### E-3: Address changes during the year

- **Address changes during the year** — Address changes can be made on the annual report. If an address changes after the annual report is filed, an amended filing (LLC $50; profit/nonprofit corporation $61.25) can update the records before the next annual report cycle.  _(unsure)_

### E-4: Foreign LLC withdrawing from Florida

- **Foreign LLC withdrawing from Florida** — A foreign LLC that has filed a certificate of withdrawal is not required to file an annual report for the year following the effective date of withdrawal. However, the annual report for the year of withdrawal is still due.  ([605.0910](https://www.flsenate.gov/Laws/Statutes/2025/605.0910)); section 605.0906 concerns a noncomplying foreign-company name, not withdrawal. **Non-usable hold:** the blanket assertion that the withdrawal-year report is always due is not established; confirm effective date, prior liabilities and withdrawal processing.

### E-5: Administrative dissolution risk

- **Administrative dissolution risk**: distinguish the third-Friday 5 p.m. Eastern filing cutoff from the fourth-Friday September legal event. In 2025 the dates were September 19 and September 26. Domestic LLCs and domestic profit/nonprofit corporations are dissolved; foreign corporate authority is revoked. Domestic dissolution preserves existence for winding up rather than an unrestricted right to continue ordinary business. [605.0714](https://www.flsenate.gov/Laws/Statutes/2025/605.0714); [607.1420](https://www.flsenate.gov/Laws/Statutes/2025/607.1420); [617.1421](https://www.flsenate.gov/Laws/Statutes/2025/0617.1421); [607.1530](https://www.flsenate.gov/Laws/Statutes/2025/607.1530).

### E-6: Disregarded entity status

- **Disregarded entity status** — A single-member LLC that is disregarded for federal tax purposes is still treated as a separate legal entity under Florida law and must file the annual report. The federal tax classification does not affect the Sunbiz filing obligation.  _(unsure)_

## Section 6 -- Test suite

### Test 1: Standard LLC annual report

- **Input:** Active Florida domestic LLC, formed 2020, no changes to officers or address.
- **Expected output:** File annual report by May 1, 2025. Fee: $138.75. No late fee.
- **Verify:** Confirmation number documented.

### Test 2: Late filing

- **Input:** Active Florida domestic LLC, annual report not yet filed as of May 15, 2025.
- **Expected output:** File immediately. Fee: $138.75 + $400.00 late fee = $538.75.
- **Verify:** Flag for reviewer that late fee applies.

### Test 3: Corporation annual report

- **Input:** Active Florida for-profit corporation, standard filing.
- **Expected output:** Fee: $150.00 by May 1, 2025.
- **Verify:** Officer/director information current.

### Test 4: New LLC formed in current year

- **Input:** LLC formed March 15, 2025.
- **Expected output:** No annual report due until May 1, 2026. Flag for reviewer.

### Test 5: Multiple LLCs

- **Input:** Same owner operates 3 Florida LLCs.
- **Expected output:** 3 separate filings. Total fees: 3 x $138.75 = $416.25.

```oa-check
name: Existing standard LLC fee
inputs:
  annual_report: 50
  supplemental_fee: 88.75
steps:
  fee: annual_report + supplemental_fee
expected:
  fee: 138.75
```

```oa-check
name: Existing late LLC fee example
inputs:
  ordinary_fee: 138.75
  late_fee: 400
steps:
  total: ordinary_fee + late_fee
expected:
  total: 538.75
```

```oa-check
name: Existing three-LLC example
inputs:
  entities: 3
  each_fee: 138.75
steps:
  total: entities * each_fee
expected:
  total: 416.25
```

## Section 7 -- Prohibitions

- **P-1:** Do NOT file the annual report without confirming current manager/member or officer/director information with the client. Stale data creates legal liability.
- **P-2:** Do NOT use a P.O. Box as the registered agent address. Florida requires a street address.
- **P-3:** Do NOT assume a disregarded LLC is exempt from annual report filing.
- **P-4:** Do NOT advise on whether to let an entity dissolve for tax planning purposes. That is legal advice outside this skill's scope.
- **P-5:** Use the supported Sunbiz online workflow. Do not treat the unverified absolute paper ban as resolved law; confirm the permitted route for any exception.

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Entity is confirmed as registered on sunbiz.org
- [ ] Entity type (LLC, corporation, not-for-profit) correctly identified
- [ ] Correct fee amount used for entity type
- [ ] Apply the May 1 deadline and covered-entity late charge; do not charge Chapter 617 nonprofits $400
- [ ] Registered agent address is a Florida street address
- [ ] Required principals' information is true/current; LLC statute requires at least one person with authority to manage, while corporation fields follow their own statute
- [ ] FEIN or permitted no-number/applied-for status is recorded; do not claim an actual IRS reconciliation without source evidence
- [ ] Confirmation number documented after filing
- [ ] Reviewer brief includes any flags (late filing, address changes, dissolution risk)

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## Sources

These bounded 2025-law and operational-page reads were completed on 2026-11-22 and reused for this correction. They do not establish whole-current-2026-law or actual-entity clearance.

| Authority | Actual read scope and short wording | Read on |
| --- | --- | --- |
| [LLC annual report](https://www.flsenate.gov/Laws/Statutes/2025/605.0212) | Read in the linked authority (bounded scope): Full operative annual-report section read, including first-report/effective-year rule, fields, agent change, missing-field cure and electronic-form wording. Quote: “between January 1 and May 1”. 2025 version. | 2026-11-22 |
| [Profit annual report](https://www.flsenate.gov/Laws/Statutes/2025/607.1622) | Read in the linked authority (bounded scope): Operative subsections(1)–(7) read; remaining merger/conversion text not relied upon. Quote: “directors and principal officers”. 2025 version. | 2026-11-22 |
| [Nonprofit annual report](https://www.flsenate.gov/Laws/Statutes/2025/617.1622) | Read in the linked authority (bounded scope): Entire operative section read. Postal-compliance subsection(2) is a real counterpoint to the absolute paper ban. Quote: “deposit of such report”. 2025 version. | 2026-11-22 |
| [LLC fees](https://www.flsenate.gov/Laws/Statutes/2025/605.0213) | Read in the linked authority (bounded scope): Whole operative fee section read. Quote: “For filing an annual report, $50.” 2025 version. | 2026-11-22 |
| [Profit fees](https://www.flsenate.gov/Laws/Statutes/2025/607.0122) | Read in the linked authority (bounded scope): Whole operative fee section read. Annual base and standalone agent-change provisions distinguished. Quote: “Annual report: $61.25.” 2025 version. | 2026-11-22 |
| [Nonprofit fees](https://www.flsenate.gov/Laws/statutes/2025/617.0122) | Read in the linked authority (bounded scope): Whole operative 2025 section read through lower-case statutes URL after uppercase attempts timed out. Quote: “Annual report: $61.25.” Current unpinned Online Sunshine counterpart also read and expressly labelled2026, not used as sole historical authority. | 2026-11-22 |
| [Supplemental fee and late charge](https://www.flsenate.gov/Laws/Statutes/2025/607.193) | Read in the linked authority (bounded scope): Entire operative 2025 section read in follow-up positioned at150; initial excerpt omitted late-charge clause. Quote: “an annual supplemental corporate fee of $88.75”. Statutory reinstatement exception read. | 2026-11-22 |
| [Sunbiz annual-report overview and filing steps](https://efile.sunbiz.org/sbs_ar_instr.html) | Read in the linked authority (bounded scope): All100extracted lines read, including nonprofit exemption, amended-report distinction, payment options, document number, addresses, principals, review/signature and fee steps. Quote: “Not for profit corporations are not subject to the $400 late fee.” Current undated operational page, supported by year-pinned statutes for historical amounts/dates. | 2026-11-22 |
| [LLC dissolution](https://www.flsenate.gov/Laws/Statutes/2025/605.0714) | Read in the linked authority (bounded scope): Entire operative 2025 section read in follow-up, including fourth-Friday event and winding-up limit. Quote: “on the fourth Friday in September”. Other-ground notice/60day route not confused with annual-report dissolution. | 2026-11-22 |
| [Domestic profit dissolution](https://www.flsenate.gov/Laws/Statutes/2025/607.1420) | Read in the linked authority (bounded scope): Whole operative 2025 section read, including third-Friday5pm threshold, fourth-Friday event and continued existence/winding up. Quote: “continues in existence”. Guessed607.1421 resolved to statute index; no operative support claimed from index. | 2026-11-22 |
| [Nonprofit dissolution](https://www.flsenate.gov/Laws/Statutes/2025/0617.1421) | Read in the linked authority (bounded scope): Whole operative 2025 section read after unpadded URL429 and alternatezero-padded path success. Quote: “fourth Friday in September”. Companion617.1420 attempts unsuccessful; no false complete companion read. | 2026-11-22 |
| [Foreign profit revocation](https://www.flsenate.gov/Laws/Statutes/2025/607.1530) | Read in the linked authority (bounded scope): Whole operative 2025 section read, including annual-report timing and continued agent authority. Quote: “on the fourth Friday in September”. No independent foreign-LLC revocation-procedure audit claimed. | 2026-11-22 |
| [LLC reinstatement](https://www.flsenate.gov/Laws/Statutes/2025/605.0715) | Read in the linked authority (bounded scope): Opening subsection(1), including application and fees/penalties, actually read; remainder not claimed. Quote: “may apply to the department for reinstatement”. Reinstatement computation remains out of skill scope. | 2026-11-22 |
| [LLC agent change](https://www.flsenate.gov/Laws/Statutes/2025/605.0114) | Read in the linked authority (bounded scope): Whole operative 2025 section read; annual-report change route retained. Quote: “annual report”. Does not by itself establish an extra invoice. | 2026-11-22 |
| [LLC registered agent](https://www.flsenate.gov/Laws/Statutes/2025/605.0113) | Read in the linked authority (bounded scope): Entire operative 2025 section read, including resident, eligible entity types and written successor acceptance. Quote: “Another domestic entity that is an authorized entity”. No human signature verified. | 2026-11-22 |
| [Original withdrawal citation](https://www.flsenate.gov/Laws/Statutes/2025/605.0906) | Read in the linked authority (bounded scope): Actual2025 name-compliance provision read sufficiently to establish wrong topic, not a withdrawal annual-report rule. Quote: “Noncomplying name of foreign limited liability company”. | 2026-11-22 |
| [LLC withdrawal](https://www.flsenate.gov/Laws/Statutes/2025/605.0910) | Read in the linked authority (bounded scope): Entire operative 2025 section read in follow-up. Authority cancellation/effectiveness and process-service details read; no current-year report condition found here. Quote: “canceled when the notice becomes effective”. | 2026-11-22 |

Not yet confirmed; non-usable holds: the absolute paper-filing prohibition and its statutory/operational conflict; unconditional withdrawal-year filing; actual registration, FEIN, principals, authorized signer and filing receipt; and complete current-2026-law/operational/special-case application. No actual filing or receipt has been tested. Independent changed-line source review and accountant approval of this changed version remain pending.
