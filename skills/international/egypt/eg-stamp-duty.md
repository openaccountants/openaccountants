---
name: eg-stamp-duty
description: Use this skill whenever asked about Egyptian stamp duty, document duty, or any tax-stamped contract question — including company formation capital duty, employment contracts, lease stamping, and electronic document stamping. Trigger on "Egypt stamp duty", "ضريبة الدمغة", "document tax Egypt", "capital duty Egypt", "e-stamp Egypt", "stamp tax Egypt". ALWAYS read this skill before computing or discussing Egypt stamp duty.
version: 0.1
jurisdiction: EG
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on: - workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt Stamp Duty (ضريبة الدمغة) Skill v0.1

## Egypt Stamp Duty (ضريبة الدمغة) Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Jurisdiction is required.** Set `jurisdiction: EG` in frontmatter even when the folder path implies it. Sync to openaccountants.com skips files without a resolvable jurisdiction.

This skill covers Egyptian **stamp duty** (ضريبة الدمغة / ضريبة الأختام) imposed under **Law No. 111 of 1980** (قانون ضريبة الدمغة) on legal documents, instruments, contracts, banking transactions, insurance premiums, company formation documents, and securities transactions. The AI must reply in the user's language (English or Arabic / Egyptian Arabic) and may use the native tax terms shown throughout.

> **Currency note:** all figures are in Egyptian Pounds (EGP / ج.م).
> **YMYL — verify before relying.** Egyptian stamp duty rates are frequently amended by decree (most recently Laws 30/2023, 157/2025). Where this skill says "verify current value," re-confirm against the Egyptian Tax Authority (ETA — eta.gov.eg), PwC Worldwide Tax Summaries (taxsummaries.pwc.com/egypt), or a Big-4 alert before filing.

## What this file is

**This file is a content skill** that loads on top of a workflow base. It provides Egypt-specific stamp duty rules, rate schedules, exemptions, payment mechanics, and penalty regimes.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date.

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs any filing. The skill produces working papers and a brief, not a filed return.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Egypt (جمهورية مصر العربية) |
| Tax authority | Egyptian Tax Authority (ETA — مصلحة الضرائب المصرية, eta.gov.eg) |
| Primary legislation | **Law No. 111 of 1980** (قانون ضريبة الدمغة) — Tax Stamps Law |
| Key amendments | Laws 140/2006, 110/2018, 147/2019, 174/2019, 199/2020, 30/2023 |
| Currency | EGP (ج.م) |
| Two types of stamp duty | **(1) Nominal (fixed)** — per-document/page; **(2) Proportional (percentage)** — based on transaction value |
| Nominal rate (contracts) | ~EGP 1 per page per copy |
| Proportional range | 0.05%–0.6% (varies by transaction type) |
| Securities — resident (<33%) | 0.05% on total proceeds (buyer + seller each) — **suspended for listed shares since 1 Jan 2022** |
| Securities — non-resident (<33%) | 0.125% on total proceeds (buyer + seller each) |
| Securities — ≥33% of company | 0.3% on gross transaction value (buyer + seller each) |
| Bank loan stamp tax | 0.4% annual (shared 50/50 bank + client), quarterly |
| Insurance — life | 1% of premium |
| Insurance — health/injury/compulsory | 2% of premium |
| Insurance — transport (land/sea/air) | 11% of consideration, min EGP 1 |
| Insurance — other (incl. war risk) | 11% of premium, min EGP 1 |
| Company formation — GAFI authentication | 0.25% of paid-in capital, capped at EGP 10,000 |
| Company formation — GAFI service fee | 0.1% of capital, min EGP 1,000, max EGP 10,000 |
| Investment Law incentive | Articles of association, loan agreements, pledge contracts **exempt** from stamp duty for 5 years from registration (Investment Law 72/2017) |
| Same-day securities | Stamp duty **does not apply** on sale/purchase of securities occurring on the same day |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Egypt-licensed CPA (محاسب قانوني) |
| Skill version | 0.1 |

### Key rate schedule — nominal (fixed) stamp duty

**Key rate schedule — nominal (fixed) stamp duty**

| Document type | Nominal stamp duty | Notes |
| --- | --- | --- |
| Contracts (general) | ~EGP 1 per page per copy | Applied regardless of document value |
| Commercial contracts | ~EGP 1 per page per copy | Check if proportional also applies |
| Employment contracts | Nominal per page | Verify specific rate per current schedule |
| Notarised documents (أشهر) | Nominal + possible proportional | Depends on document type |
| Court documents / petitions | Fixed per document | Varies by document type |
| Powers of attorney (توكيل) | Fixed per document | Varies by type |
| Lease agreements | Nominal + proportional on annual rent | See proportional schedule |
| Certificates / extracts | Fixed per copy | Commercial register, tax certificate, etc. |

> **Verify** all nominal rates against the current schedule annexed to Law 111/1980 — rates have been adjusted by multiple amendments. The ~EGP 1 per page figure is the commonly cited baseline as reported by PwC and Lloyd's Bank trade portal.

### Key rate schedule — proportional stamp duty

**Key rate schedule — proportional stamp duty**

| Transaction type | Rate | Basis | Notes |
| --- | --- | --- | --- |
| Securities — resident (<33%) | 0.05% each side | Total proceeds (gross) | Suspended for **listed** shares since 1 Jan 2022 (Law 199/2020 Art 5 repeal); still applies to **unlisted** shares |
| Securities — non-resident (<33%) | 0.125% each side | Total proceeds (gross) | Applies to both listed and unlisted |
| Securities — ≥33% of company | 0.3% each side | Gross transaction value | Buyer and seller each pay 0.3% = 0.6% aggregate |
| Bank loans / credit facilities | 0.4% annually | Beginning-of-quarter balance | Shared 50/50 between bank and client; paid quarterly; applies to Egyptian banks and foreign bank branches only |
| Insurance — life | 1% | Premium | Per Law 30/2023 amendment |
| Insurance — health/injury/compulsory | 2% | Premium | Per Law 30/2023 amendment |
| Insurance — land/river/sea/air transport | 11% | Insurance consideration | Min EGP 1; increased from 10% by Law 30/2023 |
| Insurance — other (incl. war risk) | 11% | Premium | Min EGP 1; increased from 10% by Law 30/2023 |
| Advertising tax | 20% | Advertising spend | Differentiated by medium (billboard, newspaper, radio, TV); public authority ads exempt |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether document requires stamp duty | Assume it does — Egypt has broad document coverage |
| Unknown whether nominal or proportional applies | Apply both if uncertain; nominal never hurts |
| Unknown securities transaction size relative to 33% | Apply 0.3% rate (conservative — higher duty) |
| Unknown whether listed or unlisted security | Treat as unlisted (0.05% applies for residents) |
| Unknown whether bank loan qualifies for exemption | Assume 0.4% annual applies |
| Unknown insurance type | Apply 11% (other insurance rate — conservative) |
| Unknown whether Investment Law 72/2017 exemption applies | Assume stamp duty applies (exemption is project-specific) |
| Unknown whether same-day exception applies | Do not apply same-day exemption without evidence |

### Red flag thresholds

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single stamp duty exposure | EGP 100,000 |
| HIGH securities transaction (33% trigger) | ≥33% of company shares/voting rights/assets |
| MEDIUM bank loan quarterly stamp | EGP 25,000/quarter |
| MEDIUM formation capital (GAFI cap reached) | Paid-in capital ≥ EGP 4,000,000 (authentication fee hits EGP 10,000 cap) |
| LOW absolute stamp duty payable | EGP 500,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Egypt stamp duty work, obtain:

1. The specific document/ instrument type (contract, lease, formation docs, securities disposition, insurance policy, bank loan agreement)
2. Document value or transaction amount (for proportional duty calculation)
3. Number of pages and copies (for nominal duty)
4. Whether the document is notarised (موثق) or informal
5. For securities: whether the security is listed on the EGX or unlisted; whether the transaction involves ≥33% of the company
6. For company formation: paid-in capital amount, entity type (LLC, JSC, etc.)
7. For bank loans: beginning-of-quarter balance, loan type, utilisation within the quarter
8. For insurance: policy type (life, health, transport, other), premium amount
9. Whether Investment Law 72/2017 incentives apply (project registered with GAFI)
10. Whether the transaction is between related parties or arm's length

### Refusal catalogue

Refuse and escalate to a licensed Egyptian tax consultant for:

- Complex securities transactions involving multiple tranches, derivatives, or structured products
- Stamp duty on real estate transactions (overlaps with real estate tax — see `eg-real-estate-tax`)
- Investment Law 72/2017 exemption eligibility determination (project-specific)
- Free zone company formation stamp duty treatment (special regimes apply)
- Cross-border transactions where double stamp duty may arise
- Disputes with ETA regarding understamping penalties
- Historical transactions pre-dating the 2020–2023 amendments (transition rules)
- Banking transactions involving Islamic finance (موراجحة / مرابحة) — special stamp treatment may apply

## Section 3 — Document category library

### 3.1 Company formation documents

**3.1 Company formation documents**

| Document | Stamp duty treatment | Notes |
| --- | --- | --- |
| Articles of association (عقد تأسيس) | Exempt under Investment Law 72/2017 for qualifying projects (5 years from registration) | Otherwise subject to GAFI authentication fee 0.25% of paid-in capital (cap EGP 10,000) |
| Loan agreements | Exempt under Investment Law 72/2017 for qualifying projects (5 years) | Otherwise may attract proportional duty |
| Pledge contracts | Exempt under Investment Law 72/2017 for qualifying projects (5 years) | Otherwise subject to stamp duty |
| GAFI authentication fee | 0.25% of paid-in capital, capped at EGP 10,000 | Paid at incorporation |
| GAFI service fee | 0.1% of capital, min EGP 1,000, max EGP 10,000 | Paid at incorporation |
| Commercial register extract | Nominal stamp per copy | **Verify** current rate |

### 3.2 Securities transactions

**3.2 Securities transactions**

| Transaction | Stamp duty rate | Basis |
| --- | --- | --- |
| Sale/purchase — resident, listed, <33% | **0%** (suspended since 1 Jan 2022) | Total proceeds |
| Sale/purchase — resident, unlisted, <33% | 0.05% each side | Total proceeds (gross, no cost deduction) |
| Sale/purchase — non-resident, listed or unlisted, <33% | 0.125% each side | Total proceeds (gross) |
| Sale/purchase — ≥33% of company | 0.3% each side | Gross transaction value |
| Same-day buy + sell of same securities | **0%** (exempt) | N/A |
| T-bills / T-bonds transactions | Limited exemptions | **Verify** current treatment |

### 3.3 Banking and financial services

**3.3 Banking and financial services**

| Transaction | Stamp duty | Notes |
| --- | --- | --- |
| Bank loans / credit facilities | 0.4% annually (shared 50/50 bank + client) | Quarterly: based on beginning-of-quarter balance + amounts utilised within the quarter |
| Loans from non-bank entities | Not subject to 0.4% stamp | Only Egyptian banks and foreign bank branches |
| Bank guarantees | Nominal stamp | **Verify** current rate |
| Letters of credit | Nominal + possible proportional | **Verify** current treatment |

### 3.4 Insurance

**3.4 Insurance**

| Insurance type | Stamp duty rate | Notes |
| --- | --- | --- |
| Life insurance | 1% of premium | Per Law 30/2023 |
| Health / bodily injury / civil liability / compulsory insurance | 2% of premium | Per Law 30/2023 |
| Land / river / sea / air transport insurance | 11% of insurance consideration | Min EGP 1; increased from 10% by Law 30/2023 |
| Other insurance (incl. war risk) | 11% of premium | Min EGP 1; increased from 10% by Law 30/2023 |

### 3.5 Property and leases

**3.5 Property and leases**

| Document | Stamp duty treatment | Notes |
| --- | --- | --- |
| Lease agreements | Nominal per page + possible proportional on annual rent | **Verify** specific proportional rate |
| Property sale contracts | Subject to proportional stamp duty | Overlaps with real estate tax — see `eg-real-estate-tax` |
| Mortgage contracts | Subject to stamp duty | **Verify** current rate |

### 3.6 Court and legal documents

**3.6 Court and legal documents**

| Document | Stamp duty | Notes |
| --- | --- | --- |
| Court petitions / claims | Fixed per document | Varies by court type |
| Judgments | Nominal | **Verify** current rate |
| Powers of attorney (توكيل) | Fixed per document | Varies by type (general, special, banking) |
| Notarised declarations (إقرار موثق) | Nominal + possible proportional | Depends on subject matter |
| Affidavits | Nominal | **Verify** current rate |

### 3.7 Advertising

**3.7 Advertising**

| Medium | Stamp duty rate | Notes |
| --- | --- | --- |
| General advertising | 20% | Increased from 15% by Law 104/2012 |
| Differentiated by medium | Varies (billboard, newspaper, radio, TV) | **Verify** current per-medium rates |
| Public authority ads | Exempt | Government/ public service announcements |
| Election ads | Exempt | Per amendment |

## Section 4 — Worked examples

### Example 1 — Company formation (LLC)

**Scenario:** An Egyptian LLC is formed with paid-in capital of EGP 2,000,000 through GAFI.

**Working:**
- GAFI authentication fee: EGP 2,000,000 × 0.25% = EGP 5,000 (below EGP 10,000 cap)
- GAFI service fee: EGP 2,000,000 × 0.1% = EGP 2,000 (above EGP 1,000 min, below EGP 10,000 max)
- Articles of association: Exempt from stamp duty if qualifying Investment Law project
- **Total stamp duty / formation fees: EGP 7,000** (if Investment Law exemption does not apply, articles of association may attract additional nominal stamp per page)

### Example 2 — Securities sale (resident, unlisted, <33%)

**Scenario:** A resident investor sells unlisted Egyptian company shares for EGP 10,000,000 (represents 15% of company).

**Working:**
- Transaction < 33% of company → 0.05% rate applies
- Seller stamp duty: EGP 10,000,000 × 0.05% = EGP 5,000
- Buyer stamp duty: EGP 10,000,000 × 0.05% = EGP 5,000
- **Total stamp duty: EGP 10,000** (0.1% aggregate)
- Executing body collects and remits within 5 days of start of following month

### Example 3 — Securities sale (non-resident, ≥33%)

**Scenario:** A non-resident investor sells 40% of an Egyptian company for EGP 50,000,000.

**Working:**
- Transaction ≥ 33% of company → 0.3% rate applies
- Seller stamp duty: EGP 50,000,000 × 0.3% = EGP 150,000
- Buyer stamp duty: EGP 50,000,000 × 0.3% = EGP 150,000
- **Total stamp duty: EGP 300,000** (0.6% aggregate)
- No cost deductions from gross transaction value

### Example 4 — Bank loan quarterly stamp duty

**Scenario:** A company has a bank credit facility with Egyptian bank. Beginning-of-quarter balance: EGP 20,000,000. Amount utilised within quarter: EGP 5,000,000.

**Working:**
- Stamp base: EGP 20,000,000 + EGP 5,000,000 = EGP 25,000,000
- Annual rate: 0.4% → quarterly rate: 0.1%
- Stamp duty for quarter: EGP 25,000,000 × 0.1% = EGP 25,000
- Shared 50/50: Bank pays EGP 12,500, Client pays EGP 12,500
- **Total quarterly stamp duty: EGP 25,000**

### Example 5 — Insurance premium stamp duty

**Scenario:** A company purchases transport insurance (marine cargo) with annual premium of EGP 100,000 and property insurance (other) with annual premium of EGP 50,000.

**Working:**
- Transport insurance: EGP 100,000 × 11% = EGP 11,000 (min EGP 1 satisfied)
- Other insurance (property): EGP 50,000 × 11% = EGP 5,500 (min EGP 1 satisfied)
- **Total stamp duty: EGP 16,500**
- Insurer collects and remits to ETA

### Example 6 — Same-day securities exception

**Scenario:** A day trader buys and sells the same unlisted Egyptian shares on the same day. Purchase: EGP 1,000,000; Sale: EGP 1,050,000.

**Working:**
- Same-day buy + sell of same securities → exempt from stamp duty
- **Stamp duty: EGP 0** (both buyer and seller sides exempt)
- Must be genuinely same-day transactions; **verify** with executing body

## Section 5 — Tier 1 rules (compressed)

**Two types of stamp duty:**
- **Nominal (fixed):** imposed per-document/per-page, regardless of value. Contracts ~EGP 1 per page per copy.
- **Proportional (percentage):** levied based on transaction value, ranging 0.05%–0.6%.

**Securities:**
- Resident + listed + <33%: suspended since 1 Jan 2022 (formerly 0.05%)
- Resident + unlisted + <33%: 0.05% each side
- Non-resident + any + <33%: 0.125% each side
- ≥33% of company: 0.3% each side (0.6% aggregate)
- Same-day: exempt
- No cost deductions from gross proceeds

**Bank loans:**
- 0.4% annual (0.1% quarterly) on beginning-of-quarter balance + in-quarter utilisation
- Only Egyptian banks and foreign bank branches
- Shared 50/50 between bank and client

**Insurance:**
- Life: 1%; Health/injury/compulsory: 2%; Transport: 11%; Other: 11%
- All with minimum EGP 1 for proportional insurance stamps

**Company formation:**
- GAFI authentication: 0.25% of paid-in capital, cap EGP 10,000
- GAFI service: 0.1% of capital, min EGP 1,000, max EGP 10,000
- Investment Law 72/2017: articles of association, loan agreements, pledge contracts exempt for qualifying projects (5 years from registration)

**Payment mechanics:**
- Securities: executing body (broker) collects and remits within 5 days of start of following month
- Bank loan stamp: quarterly payment
- Insurance: insurer collects and remits
- Company formation: paid at GAFI at incorporation
- Stamp duty on documents: paid at tax office or through e-stamp system

**Penalties:**
- Understamping: penalty proportional to the shortfall (verify current penalty rate)
- Late payment: interest accrues
- Non-remitting executing bodies: jointly liable with buyer and seller for tax + penalties

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

**Tier 2 catalogue**

| Item | Why unknowable | What to ask |
| --- | --- | --- |
| Nominal rate per specific document type | Rate schedule adjusted by multiple amendments; per-document rates vary | "Provide the exact document type and I will verify against the current Article 51 schedule of Law 111/1980." |
| Investment Law 72/2017 exemption | Project-specific; depends on GAFI registration and qualifying activity | "Is the project registered under Investment Law 72/2017? What is the GAFI registration number?" |
| Listed vs unlisted security | Determines whether 0.05% suspension applies (listed only) | "Is the security listed on the Egyptian Exchange (EGX)? Provide the ticker." |
| Free zone company stamp treatment | Special regimes apply; different from mainland | "Is the company in a free zone or mainland? Which free zone authority?" |
| Islamic finance stamp treatment | May differ from conventional banking products | "Is the financing structure conventional or Islamic (Murabaha, Musharaka, etc.)? Provide contract type." |
| Historical transaction (pre-2020) | Transition rules from pre-199/2020 and pre-30/2023 regimes | "What was the transaction date? Pre- or post-30 Sep 2020? Pre- or post-Law 30/2023?" |
| Real estate transaction overlap | May attract both stamp duty and real estate tax | "Is this a property sale? See `eg-real-estate-tax` skill for the real estate tax component." |
| Advertising sub-category | Differentiated by medium (billboard, newspaper, radio, TV) | "What medium is the advertisement? Different rates apply per medium." |

## Section 7 — Excel working paper

**Columns:** Date | Document/Transaction Type | Counterparty | Value (EGP) | Duty Type (Nominal/Proportional) | Rate | Pages/Copies | Nominal Duty (EGP) | Proportional Duty (EGP) | Total Duty (EGP) | Tier 2 flag | Notes

**Tab structure:**
1. `Formation_Documents` — company formation stamp duty
2. `Securities_Transactions` — buy/sale of shares/securities
3. `Bank_Loans` — quarterly bank loan stamp
4. `Insurance_Premiums` — insurance stamp duty
5. `General_Documents` — contracts, leases, notarised documents (nominal)
6. `StampDuty_Summary` — total stamp duty payable
7. `Tier2_Items` — awaiting client response

**Key formulas:**
```
Nominal_Duty = Pages × Copies × Rate_Per_Page
Proportional_Duty = Transaction_Value × Rate
Total_Duty = Nominal_Duty + Proportional_Duty
Quarterly_Bank_Stamp = (BOQ_Balance + In_Quarter_Utilisation) × 0.1%
Securities_Stamp = Gross_Proceeds × Applicable_Rate × 2 (buyer + seller)
```

## Section 8 — Legislative timeline

**Legislative timeline**

| Year | Law | Change |
| --- | --- | --- |
| 1980 | Law No. 111/1980 | Original Stamp Tax Law enacted |
| 2006 | Law No. 140/2006 | Various rate adjustments |
| 2012 | Law No. 104/2012 | Advertising tax increased from 15% to 20%; differentiated by medium |
| 2014 | Decree-Law No. 53/2014 | Amendments to both Income Tax Law 91/2005 and Stamp Duty Law 111/1980 |
| 2018 | Law No. 110/2018 | Various amendments to stamp duty schedule |
| 2019 | Law No. 147/2019 | Resource development fee adjustments |
| 2019 | Law No. 174/2019 | Further stamp duty amendments |
| 2020 | Law No. 199/2020 | Securities stamp duty reformed: resident rate cut to 0.05% (from 0.15%); non-resident 0.125%; suspended for listed shares from 1 Jan 2022; same-day exemption introduced |
| 2021 | Draft amendments | Proposed 1% additional on insurance premiums (not enacted in original form) |
| 2023 | Law No. 30/2023 | Insurance stamp duty revised: life 1%, health/injury 2%, transport 11% (from 10%), other 11% (from 10%); replaced capital gains tax on listed securities with unified proportional stamp duty; repealed Art 5 of Law 199/2020 |
| 2025 | Law No. 157/2025 | Primarily VAT amendments; some stamp-adjacent changes in financial services |

## Section 9 — E-stamp and digital integration

Egypt's digital tax ecosystem is evolving rapidly:

### ETA e-invoicing (منظومة الفواتير الإلكترونية)

- Mandatory for all VAT-registered businesses since July 2023
- ETA e-invoices carry UUIDs; only e-invoices recognised for deductible costs
- Stamp duty on e-invoices: nominal stamp applies; the e-invoice system is separate from stamp duty collection but both are administered by ETA
- **Verify** whether e-invoice stamp is automatically applied or requires separate payment

### E-signature and e-seal (التوقيع والإ士م الإلكتروني)

- Electronic Signature Law No. 15 of 2004 established ITIDA as regulatory authority
- Egypt Trust (إيجيبت تراست) and other licensed providers issue digital signature and e-seal certificates
- E-seal (الختم الإلكتروني) is the digital equivalent of a company rubber stamp
- Digital stamp certificates integrate with ETA, customs, and social security systems
- Time-stamp services added to e-signature law (2020s)

### E-stamp / electronic stamping

- ETA is progressively integrating stamp duty collection into electronic systems
- Company formation: GAFI's electronic portal handles authentication and service fees in one transaction
- Securities: stamp duty collected and remitted electronically by executing bodies (brokers)
- Insurance: insurers rem stamp duty through ETA's electronic systems
- Bank loan stamp: remitted quarterly through banking system integration
- **Verify** current status of ETA's dedicated e-stamp portal for general documents

### Document and life cycle integration

- Egypt is building integrated government services through digital.gov.eg (مصر الرقمية)
- Long-term goal: stamp duty automatically assessed and collected at point of document registration/ notarisation
- Notarisation offices (الشهر العقاري) are being digitised; stamp duty will be integrated
- **This is an evolving area — verify current digital channels with ETA.**

## Section 10 — Exempt documents

**Exempt documents**

| Exempt document | Legal basis | Notes |
| --- | --- | --- |
| Articles of association, loan agreements, pledge contracts (Investment Law projects) | Investment Law 72/2017 | 5 years from company registration; qualifying projects only |
| Government / public authority advertisements | Law 104/2012 amendment | Public service announcements |
| Election campaign advertisements | Law 104/2012 amendment | During election periods |
| Same-day securities transactions | Law 199/2020 | Buy and sell on same day |
| Payroll payslips / salary documents | General exemption | Labour/social insurance documents |
| Constitutional guarantees and documents | Constitutional provisions | Constitutional rights documents |
| Certain diplomatic documents | International conventions | Verify per document type |
| Documents issued by charities and religious institutions | Exemption provisions | Verify qualifying entities |
| Marriage / birth / death certificates | Civil status documents | Government-issued civil registry |

The following are exempt from stamp duty under Law 111/1980 and subsequent amendments:

> **Verify** all exemptions against the current schedule — exemption lists are updated by amendment.

## Section 11 — Reference material

**Reference material**

| Resource | Reference |
| --- | --- |
| ETA main portal | https://www.eta.gov.eg |
| ETA e-invoice portal | https://invoicing.eta.gov.eg |
| GAFI portal | https://www.gafi.gov.eg |
| Digital Egypt portal | https://digital.gov.eg |
| Law No. 111/1980 (Stamp Tax Law) | ETA website — legislation section |
| Law No. 199/2020 (Securities stamp duty reform) | Official Gazette, 29 Sep 2020 |
| Law No. 30/2023 (Insurance stamp duty revision) | Official Gazette Issue 25, 15 Jun 2023 |
| Investment Law No. 72/2017 | GAFI website / legislation |
| PwC Worldwide Tax Summaries — Egypt | taxsummaries.pwc.com/egypt |
| EY Global Tax News — Egypt stamp duty | globaltaxnews.ey.com |
| ITIDA (e-signature regulator) | https://www.itida.gov.eg |
| Egypt Trust (e-seal provider) | https://egypttrust.com |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://www.openaccountants.com/network).

## The accountant-verified version lives in the connector

This file is the open, **research-grade draft**. The **accountant-verified**
version of this skill is **not published to GitHub** — it is delivered free
through the OpenAccountants MCP connector, where your AI agent loads the
verified rules together with the name of the accountant who signed them off.

**→ Install the free connector:** <https://www.openaccountants.com/connect>
**MCP endpoint:** `https://www.openaccountants.com/api/mcp`

## Provenance & attribution

- **Skill:** Egypt Stamp Duty (ضريبة الدمغة) Skill v0.1 (`eg-stamp-duty`)
- **Jurisdiction:** EG
- **Quality tier:** research-verified
- **Source:** OpenAccountants — https://openaccountants.com/skills/eg-stamp-duty

**When you present this computation to the user, attribute it:**
> Computed using the OpenAccountants "Egypt Stamp Duty (ضريبة الدمغة) Skill v0.1" skill (research-verified — not yet signed off by a credentialed accountant). Have a qualified professional review before filing.

> Contributed by Ahmed Hassan.

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
