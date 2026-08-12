---
name: ph-withholding
description: Use this skill whenever asked about Philippines withholding tax, especially Expanded Withholding Tax (EWT) on professional fees and other payments. Trigger on phrases like "EWT Philippines", "expanded withholding tax", "creditable withholding tax", "BIR Form 2307", "final withholding tax", "Form 1601-EQ", "Form 1604-E", "withholding on professional fees", "5% 10% 15% withholding", "tax withheld at source Philippines", or any question about Philippine withholding tax rates, certificates, or remittance. Covers EWT rates, final withholding tax, BIR Forms 2307/1601-EQ/1604-E, and compliance. ALWAYS read this skill before advising on Philippine withholding taxes.
version: 1.0
jurisdiction: PH
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Jonathan I. Ruiz, CPA
review_status: current
depends_on: - ph-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PH Withholding

## Philippines Withholding Tax Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Philippines |
| Tax | Withholding Tax (Creditable and Final) |
| Currency | PHP (₱) only |
| Tax year | Calendar year |
| Primary legislation | NIRC Sections 57-58, as amended; RR 2-98, as amended by RR 11-2018 and RR 14-2023 |
| Tax authority | Bureau of Internal Revenue (BIR) |
| Validated by | Pending |
| Validation date | Pending |
| Skill version | 1.0 |

### Key Distinction

**Key Distinction**

| Type | Treatment |
| --- | --- |
| Creditable Withholding Tax (CWT / EWT) | Withheld tax is creditable against final income tax liability; payee reports gross income and claims credit |
| Final Withholding Tax (FWT) | Tax withheld constitutes the full and final tax; payee does NOT report this income in the ITR |

## Section 2 -- Expanded Withholding Tax (EWT) on Professional Fees

### 2.1 Rates -- Individual Payees

**Rates -- Individual Payees**

| Annual Gross Income of Payee | EWT Rate |
| --- | --- |
| ≤₱3,000,000 | 5% |
| >₱3,000,000 | 10% |

### 2.2 Rates -- Non-Individual (Corporate) Payees

**Rates -- Non-Individual (Corporate) Payees**

| Annual Gross Income of Payee | EWT Rate |
| --- | --- |
| ≤₱720,000 | 10% |
| >₱720,000 | 15% |

### 2.3 Applying the Lower Rate

To apply the lower EWT rate (5% for individuals, 10% for corporates):

**Requirements table**

| Requirement | Detail |
| --- | --- |
| Sworn Declaration | Payee must submit Annex B-1 (multiple payors), B-2 (single payor), or B-3 (non-individual) |
| With COR | Attach copy of BIR Certificate of Registration (Form 2303) |
| Deadline | By 15 January of each year, or before first payment for new engagements |
| Default if not submitted | Higher rate applies (10% for individuals, 15% for corporates) |

### 2.4 Covered Professionals

EWT on professional fees applies to licensed professionals under PRC and Supreme Court, including:
- CPAs, lawyers, engineers, architects, doctors
- Real estate service practitioners (RESP)
- Professional entertainers, athletes
- Management and technical consultants
- Insurance agents and adjusters
- Bookkeeping agents
- Directors of corporations (not employees)
- Independent sales representatives and marketing agents

## Section 3 -- Other Common EWT Rates

**Other Common EWT Rates**

| Payment Type | Rate |
| --- | --- |
| Rentals -- real property | 5% |
| Rentals -- personal property (≥₱10,000) | 5% |
| Income payments to contractors/subcontractors | 2% |
| Income payments by top withholding agents (goods) | 1% |
| Income payments by top withholding agents (services) | 2% |
| Commission payments to agents | 5%/10% (individual) |
| Interest on deposits and deposit substitutes | 20% (final) |
| Royalties | 20% (final) |
| Prizes (>₱10,000) | 20% (final) |
| Dividends (from domestic corp to individual) | 10% (final) |

## Section 4 -- BIR Form 2307 (Certificate of Creditable Tax Withheld at Source)

### 4.1 Purpose

- **Form 2307 Purpose** — Form 2307 is the certificate issued by the withholding agent (payor) to the payee, documenting the tax withheld. The payee uses this to claim creditable withholding tax against their income tax liability.

### 4.2 Key Information on Form 2307

**Key Information on Form 2307**

| Field | Content |
| --- | --- |
| Withholding Agent TIN | Payor's Tax Identification Number |
| Payee TIN | Recipient's Tax Identification Number |
| Period covered | Quarter/year of the payments |
| Income payment | Gross amount paid |
| Tax withheld | Amount withheld at the applicable EWT rate |
| ATC (Alphanumeric Tax Code) | Identifies the type of income and applicable rate |

### 4.3 Common ATCs for Professional Fees

**Common ATCs for Professional Fees**

| ATC | Description | Rate |
| --- | --- | --- |
| WI100 | Professional fees -- individual (≤₱3M) | 5% |
| WI010 | Professional fees -- individual (>₱3M) | 10% |
| WC100 | Professional fees -- corporate (≤₱720K) | 10% |
| WC010 | Professional fees -- corporate (>₱720K) | 15% |

### 4.4 Importance for Payees

- Form 2307 is ESSENTIAL for claiming tax credits on the annual ITR
- Without Form 2307, the withholding tax paid cannot be credited
- Payees should collect Form 2307 from all payors every quarter
- Attach all Forms 2307 to the annual ITR (Form 1701/1701A)

## Section 5 -- Remittance by Withholding Agents

### 5.1 Quarterly Remittance

**Quarterly Remittance**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Form 1601-EQ | Quarterly Remittance Return of Creditable Income Taxes Withheld (Expanded) | Last day of the month following the close of the quarter |
| Attachments | Quarterly Alphalist of Payees (QAP) | Filed with Form 1601-EQ |

### 5.2 Monthly Remittance

**Monthly Remittance**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Form 0619-E | Monthly Remittance Return of Creditable Income Taxes Withheld (Expanded) | 10th day of the following month (for months 1 and 2 of each quarter) |

### 5.3 Annual Information Return

**Annual Information Return**  _(BIR guidance on Form 1604-E. Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Form | Purpose | Deadline |
| --- | --- | --- |
| Form 1604-E | Annual Information Return of Creditable Income Taxes Withheld (Expanded) | **On or before 1 March** of the following year (NOT 31 January — that is the 1604-C / 1604-F deadline) |
| Attachments | Annual Alphalist of Payees | Filed with Form 1604-E |

## Section 6 -- Final Withholding Tax (FWT)

- **FWT nature** — Final withholding tax is withheld at source and constitutes the full tax on the income. The payee does NOT include this income in the regular ITR.

### 6.1 Common FWT Rates

**Common FWT Rates**

| Income Type | Rate |
| --- | --- |
| Interest on bank deposits (PHP) | 20% |
| Interest on long-term deposits (>5 years) | Exempt |
| Royalties (books, literary, musical) | 10% |
| Royalties (other) | 20% |
| Prizes (>₱10,000) | 20% |
| PCSO/lotto winnings (>₱10,000) | 20% |
| Dividends from domestic corporation | 10% |
| Capital gains on sale of shares (not traded) | 15% |
| Capital gains tax on real property | 6% |

### 6.2 FWT Forms

**FWT Forms**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Form 1601-FQ | Quarterly Final Withholding Tax | Last day of month following quarter end |
| Form 1604-F | Annual Final Withholding Tax | 31 January of following year |

## Section 7 -- Worked Examples

### Example 1 -- Professional Fee with EWT

**Situation:** CPA bills client ₱100,000 for consulting. CPA's annual gross receipts are under ₱3M and sworn declaration has been submitted.

**Withholding:** ₱100,000 × 5% = ₱5,000 withheld. Client pays ₱95,000 net and issues Form 2307 for ₱5,000.

**CPA's ITR:** Reports ₱100,000 gross income. Claims ₱5,000 creditable tax.

### Example 2 -- No Sworn Declaration Submitted

**Situation:** Same CPA, but did not submit Annex B-1.

**Withholding:** Higher rate applies: ₱100,000 × 10% = ₱10,000. Client pays ₱90,000 net.

### Example 3 -- Corporate Payee

**Situation:** Accounting firm (corporation) bills ₱500,000. Annual gross >₱720,000.

**Withholding:** ₱500,000 × 15% = ₱75,000 withheld.

## Section 8 -- Penalties

**Penalties**  _(NIRC ss.248–250, 255; RR 21-2018. Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Offence | Penalty |
| --- | --- |
| Failure to withhold | Withholding agent liable for the amount not withheld + 25% surcharge + 12% interest per annum |
| Failure to remit | 25% surcharge + 12% interest per annum (NIRC s.249 as amended by TRAIN; RR 21-2018 — the old 20% has not applied since 2018) |
| Failure to issue Form 2307 | Fine PHP 1,000 per failure |
| Failure to file Form 1604-E (an INFORMATION return) | NIRC s.250: PHP 1,000 per failure, capped at PHP 25,000 per calendar year |
| Failure to file Form 1601-EQ (a REMITTANCE return, tax due) | Ordinary failure-to-file exposure: 25% surcharge + 12% interest on the unremitted tax, plus potential NIRC s.255 criminal liability for wilful non-filing — NOT a flat PHP 1,000 |
| Late filing | 25% surcharge on tax due |

## Section 9 -- Reference Material

### Key BIR Issuances

**Key BIR Issuances**

| Issuance | Topic |
| --- | --- |
| RR 2-98 | Original withholding tax regulations |
| RR 11-2018 | TRAIN Law amendments to withholding |
| RR 14-2023 | Further amendments |
| RMO 23-2018 | Guidelines on 8% income tax rate election |

### Key Forms Summary

**Key Forms Summary**

| Form | Who Files | Purpose |
| --- | --- | --- |
| 2307 | Withholding agent → payee | Certificate of creditable tax withheld |
| 0619-E | Withholding agent | Monthly remittance (months 1, 2 of quarter) |
| 1601-EQ | Withholding agent | Quarterly remittance |
| 1604-E | Withholding agent | Annual information return |
| 1601-FQ | Withholding agent | Quarterly final withholding tax |
| 1604-F | Withholding agent | Annual final withholding tax |

## Prohibitions

- NEVER ignore Form 2307 collection -- without it, creditable taxes cannot be claimed
- NEVER apply the lower EWT rate without the payee's sworn declaration on file
- NEVER include final withholding tax income in the regular ITR
- NEVER confuse creditable (EWT) with final (FWT) withholding tax
- NEVER miss monthly remittance (Form 0619-E) -- it is separate from the quarterly return
- NEVER present calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
