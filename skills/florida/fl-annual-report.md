---
name: fl-annual-report
description: >
  Florida Annual Report filing for LLCs and corporations registered with the Division of Corporations (Sunbiz). Covers the annual report requirement, $138.75 fee for LLCs, filing deadline, late filing penalties, and administrative dissolution risk. Primary source: Florida Statutes Chapter 605 (LLCs) and Chapter 607 (corporations).
version: 1.0
jurisdiction: US-FL
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# Florida Annual Report (Sunbiz) v1.0

## What this file is

**Obligation category:** EF (Entity Fees)
**Functional role:** Entity filing
**Status:** Complete

This is a Tier 2 content skill that loads on top of `us-tax-workflow-base`. It covers the Florida Division of Corporations annual report filing requirement for LLCs and corporations registered to do business in Florida. The annual report is NOT a tax return; it is an informational filing that keeps entity status active with the state.

**Tax year coverage.** This skill targets **reporting year 2025** (report due by May 1, 2025, for entities formed or qualified before January 1, 2025).

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs off on the filing. The skill produces working papers and a brief, not the filed report itself.

---

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

---

## Section 2 -- Filing requirements

### Who must file

Every LLC, corporation, and not-for-profit corporation registered with the Florida Division of Corporations must file an annual report each year to maintain active status. **Source:** §605.0212, F.S. (LLCs); §607.1622, F.S. (corporations).

### When to file

| Item | Detail | Source |
|------|--------|--------|
| Filing window opens | January 1 of each year | Sunbiz filing instructions |
| Filing deadline | May 1 of each year | §605.0212(5), F.S.; §607.1622, F.S. |
| Late filing (supplemental fee) | After May 1, $400 supplemental late fee applies | §605.0212(5)(b), F.S. |
| Administrative dissolution | If no annual report filed by the 3rd Friday in September | §605.0714, F.S. |

### How to file

The annual report must be filed electronically through the Division of Corporations website (sunbiz.org). Paper filings are not accepted for annual reports.

---

## Section 3 -- Fees

| Entity type | Annual report fee | Source |
|-------------|-------------------|--------|
| LLC (domestic or foreign) | $138.75 | §605.0212(5)(a), F.S. |
| For-profit corporation (domestic or foreign) | $150.00 | §607.0122(1), F.S. |
| Not-for-profit corporation | $61.25 | §617.0122, F.S. |
| Late fee (all entity types) | $400.00 | §605.0212(5)(b), F.S. |
| Registered agent fee (if changing) | $25.00 | §605.0212(5)(a), F.S. |

**Note on the $138.75 LLC fee:** This is a combined fee. It includes the $100 annual report fee plus the $38.75 registered agent fee when the registered agent remains the same. If the registered agent is changed, the total may differ.

---

## Section 4 -- Computation rules (Step format)

### Step 1: Determine filing obligation

- Confirm the entity is registered with the Florida Division of Corporations (search sunbiz.org by entity name or document number).
- Confirm the entity's status is Active or Inactive (if inactive, this skill does not cover reinstatement).
- If the entity was formed or qualified after January 1 of the current year, no annual report is due until the following year.

### Step 2: Gather required information

The annual report requires the following data points:

1. Entity name (as registered)
2. Federal Employer Identification Number (FEIN)
3. Principal office address (street address required; P.O. Box alone is insufficient)
4. Mailing address
5. Registered agent name and address (must be a Florida street address)
6. Name and address of each manager/managing member (LLCs) or officer/director (corporations)
7. For LLCs: name and address of each authorized person (if different from manager)

### Step 3: Verify registered agent

- The registered agent must be a Florida resident or a business entity authorized to transact business in Florida.
- The registered agent's address must be a Florida street address (not a P.O. Box).
- If changing the registered agent, the new agent must sign an acceptance.

### Step 4: Complete the filing

- Log in to sunbiz.org annual report filing system.
- Enter the entity's document number.
- Review pre-populated information and update any changes.
- Confirm all manager/member or officer/director information is current.
- Pay the filing fee electronically.

### Step 5: Document the filing

- Record the confirmation number provided by Sunbiz.
- Save/print the filing confirmation for the entity's records.
- Note the filing date for the reviewer brief.

---

## Section 5 -- Edge cases and special rules

### E-1: Entity formed mid-year

An LLC formed on July 15, 2024, must file its first annual report by May 1, 2025. The report covers the entity's current information as of the filing date, not a specific fiscal period. **Source:** §605.0212, F.S.

### E-2: Multiple LLCs under same ownership

Each LLC is a separate filing. There is no consolidated annual report. Each pays its own $138.75 fee. Flag for reviewer if client has many LLCs -- the aggregate cost may be significant.

### E-3: Address changes during the year

Address changes can be made on the annual report. If an address changes after the annual report is filed, a supplemental filing ($50 fee) can update the records before the next annual report cycle.

### E-4: Foreign LLC withdrawing from Florida

A foreign LLC that has filed a certificate of withdrawal is not required to file an annual report for the year following the effective date of withdrawal. However, the annual report for the year of withdrawal is still due. **Source:** §605.0906, F.S.

### E-5: Administrative dissolution risk

If the annual report is not filed by the third Friday in September, the entity will be administratively dissolved (LLCs) or revoked (corporations). This means the entity loses its legal authority to transact business in Florida. Reinstatement requires additional fees and filings. **Source:** §605.0714, F.S.

### E-6: Disregarded entity status

A single-member LLC that is disregarded for federal tax purposes is still treated as a separate legal entity under Florida law and must file the annual report. The federal tax classification does not affect the Sunbiz filing obligation.

---

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

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT file the annual report without confirming current manager/member or officer/director information with the client. Stale data creates legal liability.
- **P-2:** Do NOT use a P.O. Box as the registered agent address. Florida requires a street address.
- **P-3:** Do NOT assume a disregarded LLC is exempt from annual report filing.
- **P-4:** Do NOT advise on whether to let an entity dissolve for tax planning purposes. That is legal advice outside this skill's scope.
- **P-5:** Do NOT attempt to file a paper annual report. Sunbiz requires electronic filing.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Entity is confirmed as registered on sunbiz.org
- [ ] Entity type (LLC, corporation, not-for-profit) correctly identified
- [ ] Correct fee amount used for entity type
- [ ] Filing deadline (May 1) has not passed; if passed, late fee included
- [ ] Registered agent address is a Florida street address
- [ ] All manager/member or officer/director names and addresses are current
- [ ] FEIN is provided and matches IRS records
- [ ] Confirmation number documented after filing
- [ ] Reviewer brief includes any flags (late filing, address changes, dissolution risk)

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
