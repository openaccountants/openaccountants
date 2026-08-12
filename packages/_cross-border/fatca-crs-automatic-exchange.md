---
name: fatca-crs-automatic-exchange
description: "Use this skill whenever a Financial Institution (FI), trustee, or account holder asks about automatic exchange of financial account information. Trigger on phrases like \"FATCA\", \"CRS\", \"Common Reporting Standard\", \"automatic exchange of information\", \"AEOI\", \"Form W-9\", \"Form W-8BEN\", \"Form W-8BEN-E\", \"self-certification\", \"Reportable Account\", \"Reportable Person\", \"Controlling Person\", \"passive NFE\", \"active NFFE\", \"GIIN\", \"responsible officer certification\", \"FATCA 8966\", \"FBAR\", \"Form 8938\", \"DAC2\", \"CARF\", or any question about whether a financial account, entity, or person is reportable for AEOI purposes. Covers the US Foreign Account Tax Compliance Act (FATCA — IRC §1471-1474 and Treasury Regulations §§1.1471-1.1474, intergovernmental agreements Model 1 and Model 2), the OECD Common Reporting Standard (CRS — published 2014, updated 2023 with the Crypto-Asset Reporting Framework / CARF and CRS 2.0 amendments), and the EU's CRS implementation under DAC2 (Council Directive 2014/107/EU). Does NOT cover: FBAR (FinCEN 114) which is a US-only beneficial-owner disclosure; Form 8938 individual reporting; ultimate-beneficial-ownership (UBO) registers under EU AMLD; or the OECD MDR on CRS Avoidance Arrangements (see dac6-mdr-reportable-arrangements). ALWAYS read this skill before classifying an account as reportable or determining due diligence obligations."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FATCA CRS Automatic Exchange

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It implements three overlapping AEOI regimes:

- **FATCA (United States)** — IRC §1471-1474 and Treasury Regulations, with bilateral Intergovernmental Agreements (IGAs Model 1A, 1B, and Model 2) signed with 100+ jurisdictions.
- **CRS (OECD Common Reporting Standard)** — Multilateral Competent Authority Agreement (MCAA-CRS) and bilateral Competent Authority Agreements; ~120 committed jurisdictions; first exchanges 2017 (early adopters) and 2018 (rest).
- **DAC2 (EU CRS implementation)** — Council Directive 2014/107/EU; mandatory CRS adoption by all 27 EU Member States; first exchange 2017.

**Tax year coverage.** Current for **reportable period 2025** (information collected in 2025, exchanged in 2026), reflecting the **CRS 2.0 amendments** adopted by the OECD in 2023 (in force for reporting periods 2026+ but with many jurisdictions adopting earlier), and the **Crypto-Asset Reporting Framework (CARF)** for crypto reporting (first exchanges 2027 for most committed jurisdictions, 2026 for early adopters).

**The reviewer is the customer of this output.** FATCA / CRS classification of entities (e.g., Financial Institution vs Non-Financial Entity, Active vs Passive) is fact-specific and carries strict liability for misclassification. Every output must be reviewed by a credentialed practitioner (typically a Big 4 international tax / AEOI specialist or in-house FATCA Responsible Officer) before submission of a self-certification or filing of a return.

## Section 1 — Scope statement

This skill covers:

- **Entity classification** under FATCA, CRS, and DAC2.
- **Due diligence procedures** for new accounts (self-certification, reasonableness checks) and pre-existing accounts (indicia search, electronic search, paper-record search, residency address tests, curing procedures).
- **Account identification** — Financial Account types (Depository, Custodial, Cash Value Insurance, Annuity Contracts, Equity/Debt Interests), Reportable Accounts, Documented Accounts, Excluded Accounts.
- **Reportable Person and Controlling Person identification**.
- **Reporting mechanics** — XML schema, filing portals, deadlines, penalty exposure.
- **Withholding obligations** under FATCA (30% withholdable payments under §1471(a) and §1472(a)).
- **CARF / Crypto reporting** mechanics under the OECD framework and EU implementation in DAC8.
- **CRS 2.0 amendments** — broadened definition of Investment Entity, expanded due diligence on Controlling Persons, anti-avoidance test for joint accounts.

This skill does NOT cover:

- **FBAR (FinCEN 114)** — see `us-fbar-individual.md` (forthcoming).
- **Form 8938 (Statement of Specified Foreign Financial Assets)** — see US federal individual skills.
- **Beneficial ownership registers** under EU AMLD5/6 or the US Corporate Transparency Act — see `us-fincen-cta-boi.md` and `eu-amld-boi.md` (forthcoming).
- **OECD MDR on CRS Avoidance Arrangements** — see `dac6-mdr-reportable-arrangements.md`.
- **Anti-money-laundering KYC requirements** beyond CRS due diligence overlap.

## Section 2 — Filing requirements

### FATCA — who reports

- **Reporting Financial Institutions (FIs) [T1]** — 1. **US FIs** report Foreign Account Holders to the IRS (Form 8966 for chapter 4) — payer-side reporting on the US payer. 2. **Foreign FIs (FFIs)** in Model 1 IGA jurisdictions report US account holders to their local tax authority, which exchanges with the IRS. 3. **FFIs in Model 2 IGA jurisdictions** report US account holders directly to the IRS under FATCA Form 8966, plus supplemental local reporting in some jurisdictions. 4. **Non-IGA FFIs** that have entered into an FFI Agreement with the IRS report directly to the IRS. 5. **Non-participating FFIs (NPFFIs)** face 30% withholding on US-source withholdable payments.

### CRS / DAC2 — who reports

- **Reporting FIs [T1]** — Reporting FIs in a CRS-committed jurisdiction identify and report **Reportable Accounts** held by **Reportable Persons** (tax residents of any other CRS jurisdiction). Reporting is to the local tax authority, which exchanges with each Reportable Jurisdiction.

### Deadlines (illustrative; verify per jurisdiction)

**Deadlines (illustrative; verify per jurisdiction)**  _(National AEOI rules)_

| Filing | Deadline | Source |
| --- | --- | --- |
| FATCA Form 8966 — US FIs | 31 March following reportable year | Treas. Reg. §1.1474-1(d)(1) |
| FATCA Form 8966 — Model 2 FFIs | 31 March (extended deadlines under IGA) | IGA Article 3 |
| FATCA Model 1 — to local tax authority | National deadline (varies; usually 30 June or 31 July) | National AEOI rules |
| CRS — to local tax authority | National deadline (e.g., 31 May Germany; 31 May UK; 30 June France; 31 May Australia; 31 May Singapore) | National AEOI rules |
| Late or non-filing penalty | Varies widely (e.g., UK: GBP 300 per failure plus up to GBP 60/day; Germany: up to EUR 50,000; Singapore: SGD 5,000 fine and/or 12 months imprisonment) | National AEOI rules |

### What to report (FATCA)

- **Article 3 IGA / §1.1474-1(i) Treas. Reg. [T1]** — 1. Name, address, US TIN of each Specified US Person (or for Controlling Persons of a Passive NFFE that is a US Specified Person, the Controlling Person details) 2. Account number 3. Name and identifying number (GIIN) of the Reporting FI 4. Account balance or value as of end of calendar year (or other reporting period) 5. **Custodial Accounts:** total gross interest, dividends, other income, and gross proceeds from sale or redemption 6. **Depository Accounts:** total gross interest 7. **Other accounts:** total gross amount paid or credited to the account holder  _(Article 3 IGA / §1.1474-1(i) Treas. Reg.)_

### What to report (CRS)

- **Section I CRS [T1]** — 1. Name, address, jurisdiction(s) of residence, TIN(s), date and place of birth of each Reportable Person (and each Controlling Person of a Passive NFE that is reportable) 2. Account number 3. Name and identifying number of Reporting FI 4. Account balance/value as of end of relevant calendar year (or, if closed, the closure) 5. **Custodial Accounts:** total gross interest, dividends, other income generated, gross proceeds from sale or redemption 6. **Depository Accounts:** total gross interest paid or credited 7. **Other accounts:** total gross amount paid or credited including aggregate amount of redemption payments  _(Section I CRS)_

## Section 3 — Entity classification

### Step 1 — Is the entity a Financial Institution (FI)?

**FI types (CRS §VIII(A) / FATCA §1.1471-5(e))**  _(CRS §VIII(A) / FATCA §1.1471-5(e))_

| Type | Definition |
| --- | --- |
| **Custodial Institution** | An entity that holds, as a substantial portion of its business (≥20% of gross income test over 3 years), Financial Assets for the account of others |
| **Depository Institution** | Accepts deposits in the ordinary course of a banking or similar business |
| **Investment Entity** | Two limbs: (a) primarily conducts as a business managed by an FI one or more of: trading in money market / FX / interest rate / index / transferable securities / commodity futures, individual or collective portfolio management; OR (b) gross income primarily attributable (≥50%) to investing, reinvesting, or trading in Financial Assets and the entity is managed by another FI (the "professionally managed" test) |
| **Specified Insurance Company** | An insurance company (or holding company of an insurance company) that issues or is obligated to make payments on Cash Value Insurance Contracts or Annuity Contracts |

- **CRS 2.0 broadening (2023 OECD amendments, in force 2026+) [T1]** — Investment Entity definition expanded to capture entities where a substantial activity is investing in Financial Assets *and* the entity is managed by another FI — closes the "passive holding company managed by a family office FI" gap. The professionally managed test is sharpened: the manager itself must be an FI as defined.

### Step 2 — If not an FI, classify as NFE/NFFE

- **Non-Financial Entity (NFE) / Non-Financial Foreign Entity (NFFE) [T1]** — - **Active NFE/NFFE (CRS §VIII(D)(9) / FATCA §1.1472-1(c)(1)(iv)):** Meets at least one of nine categories — broadly, an entity that is not primarily passive. Most common in scope: - Less than 50% of preceding-year gross income is passive AND less than 50% of assets produce passive income - Stock is regularly traded on an established securities market (or it is a Related Entity of such) - Governmental Entity, International Organisation, Central Bank - Holding NFE that is a non-financial group member - Start-up NFE (first 24 months) - NFE in liquidation or emerging from bankruptcy (24 months) - Treasury Center for a non-financial group - Non-profit entity meeting specific charity / public-benefit tests - **Passive NFE/NFFE:** Any NFE that is not Active. Passive NFE Controlling Persons must be looked through and reported if they are Reportable Persons.  _(CRS §VIII(D)(9) / FATCA §1.1472-1(c)(1)(iv))_

### Step 3 — Specific FI sub-classifications under FATCA

- **FI sub-classifications** — - **Participating FFI (PFFI)** — entered into FFI Agreement (rare under Model 1 IGAs; common in non-IGA jurisdictions) - **Reporting Model 1 FFI** — reports to local tax authority - **Reporting Model 2 FFI** — reports directly to IRS - **Registered Deemed-Compliant FFI** — limited categories (local FFI, qualified credit card issuer, etc.) - **Certified Deemed-Compliant FFI** — small jurisdictions, retirement funds, limited-life debt funds - **Exempt Beneficial Owner** — government entities, international organizations, central banks, treaty-qualified retirement funds - **Non-participating FFI (NPFFI)** — 30% withholding applies on US-source withholdable payments

### Step 4 — GIIN registration (FATCA only)

- **GIIN registration [T1]** — A Participating FFI, Registered Deemed-Compliant FFI, Reporting Model 1 or Model 2 FFI must register with the IRS via the FATCA Registration System and obtain a **Global Intermediary Identification Number (GIIN)**. The GIIN takes the form `XXXXXX.XXXXX.XX.NNN` where NNN is the FATCA country code.

## Section 4 — Due diligence procedures

### 4.1 New Accounts — Individuals

- **Self-certification at account opening [T1]** — - Identity, residence address, all jurisdictions of tax residence, TIN(s), date of birth. - Reasonableness check against AML/KYC information. - For US: a Form W-9 (if US person) or W-8BEN (if non-US person) under FATCA. - For CRS: a CRS Self-Certification Form. - Cure: if self-certification proves unreasonable or contradictory, obtain a corrected form within 90 days.

### 4.2 New Accounts — Entities

- **Determine FI vs NFE status [T1]** — Determine FI vs NFE status from self-certification + AML/KYC + publicly available information. If FI: confirm GIIN (for FATCA) or non-participating status; no further look-through for FATCA chapter 4 generally. If Passive NFE: identify Controlling Persons (>25% beneficial owner under AML standards, plus settlors/trustees/protectors/beneficiaries of trusts) and obtain self-certification from each.

### 4.3 Pre-existing Accounts — Individuals

- **Lower Value Accounts threshold [T1]** — ≤ USD 1m at 30 June 2014 for FATCA; ≤ USD 1m at 31 Dec 2015 for CRS USD
- **Lower Value Accounts procedures [T1]** — - **Residence address test** — current residence address based on documentary evidence - If no current residence address → **electronic indicia search** for indicia of US (FATCA) or other CRS jurisdiction residence - Indicia: identification as US/CRS-jurisdiction resident; current mailing/residence address; current telephone number; standing instructions to transfer funds; current effective POA / signatory authority granted to a person with a US/CRS-jurisdiction address; "in-care-of" or "hold mail" address - **Cure**: obtain self-certification + documentary evidence
- **High Value Accounts (> USD 1m) [T1]** — Electronic search PLUS paper record search PLUS Relationship Manager inquiry (does the RM have actual knowledge of US/CRS-jurisdiction residence?). Annual rerun until cured.

### 4.4 Pre-existing Accounts — Entities

- **Two-step process [T1]** — 1. Is the entity itself reportable? (Specified US Person under FATCA, or Reportable Person under CRS — usually applies only if directly tax resident in a Reportable Jurisdiction) 2. If a Passive NFE → identify Controlling Persons and apply individual due diligence to each
- **Pre-existing entity accounts review threshold** — ≤ USD 250,000 are not required to be reviewed under FATCA (some IGAs follow this; CRS has a similar threshold) USD

### 4.5 Aggregation rules

- **Aggregation of accounts [T1]** — Aggregate accounts of the same Account Holder at the same FI to determine threshold tests (Section VII CRS / §1.1471-5(b)(4)). Includes financial accounts where the same Account Holder is on AML/KYC records as the holder (including joint accounts at the relevant proportional share for CRS pre-2.0; CRS 2.0 imposes joint-account aggregation across both holders).  _(Section VII CRS / §1.1471-5(b)(4))_

## Section 5 — Reportable accounts and reporting

### 5.1 Reportable Person — CRS

- **Reportable Person [T1]** — A Reportable Person is an individual or entity that is a tax resident of a Reportable Jurisdiction other than: a corporation whose stock is regularly traded on a securities market; a corporation that is a Related Entity of a publicly traded corporation; a Governmental Entity, International Organization, Central Bank, or FI. Reportable Jurisdictions: any jurisdiction with which the FI's jurisdiction has an active CRS exchange relationship. Maintained on the OECD AEOI portal.

### 5.2 Specified US Person — FATCA

- **Specified US Person [T1]** — A US Person other than (§1.1471-5(f)(2)): Publicly traded corporation; Tax-exempt organisation (§501(a)); US, any state, DC, US possession, agency or instrumentality; Bank under §581; REIT; RIC, Common Trust Fund (§584(a)), or Trust exempt under §664(c) or §4947(a)(1); Dealer in securities/commodities; Broker.  _(§1.1471-5(f)(2))_

### 5.3 Cash Value Insurance and Annuity Contracts

- **Cash Value Insurance Contract reporting threshold** — Cash Value Insurance Contracts with cash value > USD 50,000 are reportable. Group Cash Value Insurance Contracts and Group Annuity Contracts have specific look-through requirements to certificate holders. USD

### 5.4 Currency reporting

All amounts reported in the currency of the account. The receiving Reportable Jurisdiction's tax authority may translate at year-end exchange rates.

## Section 6 — Withholding under FATCA (chapter 4)

### 6.1 30% withholding on US-source withholdable payments

- **Withholdable payment (§1.1473-1) [T1]** — - Interest, dividends, rents, royalties, premiums, annuities, compensation, remuneration, and other FDAP income from US sources - Gross proceeds from the sale or other disposition of property of a type that can produce US-source interest or dividends (foreign passthru payment grandfathering remains in effect; passthru payment withholding has been deferred multiple times — confirm current status)  _(§1.1473-1)_

### 6.2 Withholding when payee is

- **Withholding scenarios** — - A non-participating FFI (NPFFI) → 30% withhold - A passive NFFE that fails to provide Controlling Person info → 30% withhold on the proportionate share - A recalcitrant account holder of a PFFI in certain cases

### 6.3 Forms

- Form W-8BEN — individual non-US persons
- Form W-8BEN-E — non-US entities
- Form W-8IMY — intermediaries and flow-through entities (with attached withholding statements)
- Form W-8ECI — non-US person with US ECI
- Form W-8EXP — government, international organization, foreign central bank, foreign tax-exempt org

## Section 7 — CARF and DAC8 — crypto-asset reporting

- **OECD Crypto-Asset Reporting Framework (CARF, March 2023) [T1]** — - Reporting Crypto-Asset Service Providers (RCASPs) report transactions with Reportable Users. - Reportable Crypto-Assets: crypto-assets used as means of payment or investment; excludes Central Bank Digital Currencies (which fall under CRS 2.0) and certain closed-loop assets. - Transactions reported: crypto-to-fiat exchanges, crypto-to-crypto exchanges, reportable retail payment transactions ≥ USD 50,000. - First reporting period: 2026 for early adopters; 2027 for most committed jurisdictions.
- **EU DAC8 (Council Directive (EU) 2023/2226) [T1]** — - Transposes CARF into EU law. - Entry into force: 1 January 2026 (reporting from 2026 reference period, first exchange 2027). - Crypto-Asset Service Providers (CASPs) authorised under MiCA report to their Member State of authorization.  _(Council Directive (EU) 2023/2226)_

## Section 8 — Edge cases and special rules

### 8.1 Joint accounts (CRS 2.0)

- **Joint accounts treatment [T1]** — Pre-CRS-2.0: each holder's share was reported separately. CRS 2.0 (in force 2026+): the **full account balance** is reported for each holder unless the FI can establish proportional ownership through documentary evidence. Plan for system upgrade.

### 8.2 Trusts as FIs

- **Trust as Investment Entity / TDT** — A trust qualifies as an Investment Entity if its income is primarily from Financial Assets AND it is managed by a professional trustee that is itself an FI. **Trustee-Documented Trust** (TDT) status allows the trustee FI to absorb the trust's reporting obligation.

### 8.3 Non-Profit NFEs

- **Non-profit NFE active status test** — To qualify as Active NFE on non-profit grounds, must meet all of: established and operated in jurisdiction of residence exclusively for religious, charitable, scientific, artistic, cultural, athletic, or educational purposes / or as a professional organisation; tax-exempt; no shareholders/owners with proprietary or beneficial interest; applicable law / governing documents preclude distribution other than for charitable/non-profit purposes; require distribution of assets on liquidation to a Governmental Entity or another Active NFE.

### 8.4 Pre-existing entity accounts under USD 250,000

- **Threshold election** — Optional review — many FIs document the choice to apply or not apply this threshold and operate accordingly. CRS allows the threshold; some Member States (e.g., Netherlands) require all accounts to be reviewed.

### 8.5 Anti-avoidance — using third-country residence to escape reporting

- **Anti-avoidance rules** — Both FATCA (§1.1471-4(f)(2) RO certification) and CRS (Section IX) contain anti-avoidance rules. If an arrangement's primary purpose is to avoid reporting, the FI must treat the relevant account as if the arrangement did not exist. The OECD MDR on CRS Avoidance Arrangements (2018) creates a parallel intermediary disclosure regime. See `dac6-mdr-reportable-arrangements.md`.  _(§1.1471-4(f)(2); CRS Section IX)_

### 8.6 US-EU IGA developments

The CJEU has confirmed (Joined Cases C-457/21 P and others) that Member States can transmit FATCA data to the US under Model 1 IGAs notwithstanding GDPR concerns, subject to the data protection guarantees in the IGA itself.

### 8.7 Penalty exposure — examples

**Penalty exposure — examples**

| Jurisdiction | Penalty |
| --- | --- |
| **US** (FATCA) | Up to USD 250 per failure (cap USD 3m); higher for intentional disregard. 30% withholding loss to Account Holder. |
| **UK** | Up to GBP 3,000 per failure + GBP 600/day continuing |
| **Germany** | Up to EUR 50,000 per failure |
| **Singapore** | SGD 5,000 and/or 12 months imprisonment |
| **Australia** | Up to AUD 12,500 base + indexation |
| **Switzerland** | Up to CHF 50,000 per failure (FATCA), separate sanctions under AEOIA |

## Section 9 — Output specification

The reviewer brief must include:

1. **FI vs NFE classification** for the entity with supporting evidence and code references.
2. **GIIN status** (if FI) — registered? lapsed? sponsoring vs sponsored?
3. **Active vs Passive NFE** determination with the gross income/asset test or specific category.
4. **Account inventory** — every Financial Account with type (Depository / Custodial / Cash Value / Annuity / Equity-Debt), holder, Controlling Persons (if any), aggregated balance.
5. **Reportable Account determination** per account, with the reasoning (which Reportable Jurisdiction, which indicium triggered).
6. **Due diligence completion log** — self-certifications received, indicia search results, cures performed.
7. **Reporting schedule** — XML payloads by jurisdiction with deadlines.
8. **FATCA withholding exposure** — any payments at risk of 30% chapter 4 withholding.
9. **CARF / DAC8 readiness** — whether the entity is a Reporting Crypto-Asset Service Provider.
10. **Reviewer questions** — open items flagged as [T2] or [T3].

## Section 10 — Self-checks

Before delivering output, verify:

- [ ] FI status tested against all four FI categories under CRS §VIII(A) and §1.1471-5(e).
- [ ] Investment Entity test correctly applies the >50% passive gross income test AND the "managed by an FI" test (post-CRS-2.0 broadening).
- [ ] Active NFE test against the nine categories with documentary evidence.
- [ ] Controlling Persons identified for every Passive NFE following AML/KYC, settlor/trustee/protector/beneficiary rules for trusts.
- [ ] Indicia search completed for pre-existing individual accounts.
- [ ] Aggregation rules applied to determine threshold tests.
- [ ] CRS 2.0 joint-account treatment applied for reporting periods 2026+.
- [ ] GIIN registration verified on FATCA portal and not lapsed.
- [ ] XML schema for the receiving jurisdiction matched (e.g., CRS XML 3.0; FATCA XML v2.0; jurisdiction-specific overlays).
- [ ] Deadlines plotted for every receiving jurisdiction.
- [ ] CARF / DAC8 status reviewed for any crypto-asset activity.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 11 — Prohibitions

- **Do not** classify an entity as Active NFE without testing against the specific nine categories — the gross income/asset test is one of nine, not the only one.
- **Do not** treat absence of indicia as conclusive — Relationship Manager actual knowledge can override electronic and paper searches.
- **Do not** rely on a self-certification that contradicts AML/KYC information without curing.
- **Do not** treat an account under threshold as out of scope without explicitly documenting the threshold election.
- **Do not** ignore CARF / DAC8 just because the entity is not a traditional FI — crypto-asset service providers face independent registration and reporting.
- **Do not** advise on FATCA / CRS structuring to reduce reporting (e.g., reorganising to qualify as Active NFE) without explicit escalation — anti-avoidance rules apply, and intermediaries face DAC6 / OECD MDR exposure.

## Section 12 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. FATCA and CRS classification is fact-specific, strict-liability, and varies between IGA partners and committed CRS jurisdictions. Every output must be reviewed and signed off by a credentialed AEOI specialist before any self-certification, filing, or onboarding decision is made.

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
