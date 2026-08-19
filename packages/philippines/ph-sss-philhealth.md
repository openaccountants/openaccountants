---
name: ph-sss-philhealth
description: Use this skill whenever asked about Philippine social security contributions for self-employed individuals. Trigger on phrases like "SSS contribution", "PhilHealth premium", "Pag-IBIG", "self-employed Philippines contributions", "HDMF", "voluntary SSS", "PhilHealth self-employed", "social contributions Philippines", "mandatory contributions freelancer Philippines", or any question about computing, paying, or filing SSS, PhilHealth, or Pag-IBIG as a self-employed worker in the Philippines. This skill covers the 2025 contribution tables, registration, payment methods, and deadlines. ALWAYS read this skill before advising on Philippine social insurance obligations.
version: 1.0
jurisdiction: PH
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Jonathan I. Ruiz, CPA
review_status: current
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PH Sss Philhealth

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Philippines (Republika ng Pilipinas) |
| Coverage | SSS, PhilHealth, Pag-IBIG (HDMF) |
| Currency | PHP (Philippine Peso) only |
| Contribution period | Monthly |
| Primary legislation | RA 11199 (Social Security Act of 2018), RA 11223 (Universal Health Care Act), RA 9679 (HDMF Law) |
| Agencies | Social Security System (SSS), Philippine Health Insurance Corporation (PhilHealth), Home Development Mutual Fund (HDMF/Pag-IBIG) |
| SSS portal | my.sss.gov.ph |
| PhilHealth portal | memberinquiry.philhealth.gov.ph |
| Pag-IBIG portal | virtual.pagibigfund.gov.ph |
| Validated by | Pending — requires sign-off by a Philippine CPA or labour law practitioner |
| Skill version | 1.0 |

### 2025 Contribution Summary (Self-Employed)

**2025 Contribution Summary (Self-Employed)**

| Agency | Rate | Basis | Min Monthly | Max Monthly | Payment |
| --- | --- | --- | --- | --- | --- |
| SSS | 15% of MSC | Monthly Salary Credit (₱5,000--₱35,000) | ₱750 | ₱5,250 | Monthly |
| PhilHealth | 5% of monthly income | Declared monthly income | ₱500 | ₱5,000 | Monthly |
| Pag-IBIG | ₱200 (voluntary) | Fixed amount or up to ₱5,000 | ₱200 | ₱5,000 | Monthly |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown income for MSC | Declare at minimum MSC (₱5,000) until confirmed |
| Unknown PhilHealth income | Declare at minimum until income verified |
| Unknown Pag-IBIG membership | Assume not yet registered -- must register |
| Self-employed vs voluntary | Self-employed if active business; voluntary if no current income |
| Unknown employment history | Check SSS records for prior employment contributions |

## Section 2 -- SSS (Social Security System)

### 2.1 Legal Basis and Coverage

**2.1 Legal Basis and Coverage**

| Item | Detail |
| --- | --- |
| Law | Republic Act No. 11199 (Social Security Act of 2018) |
| Effective date (2025 rates) | January 1, 2025 (SSS Circular No. 2024-006) |
| Who must register | Self-employed earning ≥₱1,000/month, professionals, sole proprietors, partners |
| Benefits | Retirement, disability, death, maternity, sickness, unemployment (involuntary separation) |
| Mandatory | YES for self-employed with income |
| Voluntary | Available for those without current income (OFWs, non-working spouse) |

### 2.2 Contribution Rates (2025)

**2.2 Contribution Rates (2025)**

| Year | Total Rate | Min MSC | Max MSC |
| --- | --- | --- | --- |
| 2023 | 14% | ₱4,000 | ₱30,000 |
| 2024 | 14% | ₱4,000 | ₱30,000 |
| 2025 | 15% | ₱5,000 | ₱35,000 |

- **Self-employed SSS contribution rate** — Self-employed members pay the FULL 15% (no employer share).

### 2.3 MSC Contribution Table 2025 (Selected Brackets)

**MSC Contribution Table 2025 (Selected Brackets)**

| Range of Monthly Earnings (₱) | Monthly Salary Credit (₱) | Total Contribution (₱) |
| --- | --- | --- |
| Below 5,250 | 5,000 | 750 |
| 5,250 -- 5,749.99 | 5,500 | 825 |
| 5,750 -- 6,249.99 | 6,000 | 900 |
| 6,250 -- 6,749.99 | 6,500 | 975 |
| 6,750 -- 7,249.99 | 7,000 | 1,050 |
| 7,250 -- 7,749.99 | 7,500 | 1,125 |
| 7,750 -- 8,249.99 | 8,000 | 1,200 |
| 8,750 -- 9,249.99 | 9,000 | 1,350 |
| 9,750 -- 10,249.99 | 10,000 | 1,500 |
| 11,750 -- 12,249.99 | 12,000 | 1,800 |
| 14,750 -- 15,249.99 | 15,000 | 2,250 |
| 19,750 -- 20,249.99 | 20,000 | 3,000 |
| 24,750 -- 25,249.99 | 25,000 | 3,750 |
| 29,750 -- 30,249.99 | 30,000 | 4,500 |
| 34,750 and above | 35,000 | 5,250 |

### 2.4 Mandatory Provident Fund (MPF)

- **MPF applicability** — For earnings above ₱20,000 MSC, an additional MPF contribution applies: MPF rate: 15% of MSC exceeding ₱20,000. Example: MSC ₱35,000 → MPF on ₱15,000 = ₱2,250. Total at max: ₱3,000 (Regular SS on ₱20,000) + ₱2,250 (MPF on ₱15,000) = ₱5,250

### 2.5 Payment Deadlines

**Payment Deadlines**

| Last digit of SSS number | Deadline (day of month following contribution month) |
| --- | --- |
| 1 and 2 | 10th |
| 3 and 4 | 15th |
| 5 and 6 | 20th |
| 7 and 8 | 25th |
| 9 and 0 | Last day |

### 2.6 Payment Methods

- SSS online (my.sss.gov.ph) via bank transfer
- Over-the-counter at accredited banks (BDO, BPI, Landbank, etc.)
- Payment centres (Bayad Center, SM Bills Payment, 7-Eleven)
- GCash, Maya (PayMaya)
- SSS Mobile App

### 2.7 Penalties for Late Payment

**Penalties for Late Payment**

| Infraction | Penalty |
| --- | --- |
| Late contribution | 2% per month of unpaid amount |
| Non-registration | Criminal liability under RA 11199 Sec. 28(e) |
| Under-declaration of income | Back-payment of differential + 2%/month penalty |

## Section 3 -- PhilHealth (Philippine Health Insurance Corporation)

### 3.1 Legal Basis and Coverage

**3.1 Legal Basis and Coverage**

| Item | Detail |
| --- | --- |
| Law | Republic Act No. 11223 (Universal Health Care Act of 2019) |
| Who must register | ALL Filipino citizens (mandatory universal coverage) |
| Classification | Self-employed: Direct Contributors (individually paying members) |
| Benefits | Inpatient, outpatient, Z-benefits (catastrophic), primary care |
| Mandatory | YES for all citizens and permanent residents |

### 3.2 Contribution Rate (2025)

**3.2 Contribution Rate (2025)**

| Item | Detail |
| --- | --- |
| Premium rate | 5% of monthly basic salary/income |
| Employer/employee split (employed) | 50/50 (2.5% each) |
| Self-employed | Pays FULL 5% |
| Income floor | ₱10,000/month |
| Income ceiling | ₱100,000/month |
| Minimum monthly premium | ₱500 (5% × ₱10,000) |
| Maximum monthly premium | ₱5,000 (5% × ₱100,000) |

### 3.3 PhilHealth Premium Table 2025 (Self-Employed)

**PhilHealth Premium Table 2025 (Self-Employed)**

| Monthly Income (₱) | Monthly Premium (₱) |
| --- | --- |
| ₱10,000 and below | 500 |
| ₱15,000 | 750 |
| ₱20,000 | 1,000 |
| ₱25,000 | 1,250 |
| ₱30,000 | 1,500 |
| ₱40,000 | 2,000 |
| ₱50,000 | 2,500 |
| ₱60,000 | 3,000 |
| ₱70,000 | 3,500 |
| ₱80,000 | 4,000 |
| ₱90,000 | 4,500 |
| ₱100,000 and above | 5,000 |

### 3.4 Payment Schedule

**Payment Schedule**

| Payment Frequency | Due Date |
| --- | --- |
| Monthly | Before the last day of the applicable month |
| Quarterly | Before the last day of the first month of the applicable quarter |
| Semi-annual | Before the last day of the first month of the applicable semester |
| Annual | Before the last day of January |

### 3.5 Payment Methods

- PhilHealth online (memberinquiry.philhealth.gov.ph)
- Banks (Landbank, BDO, BPI, RCBC, UnionBank)
- GCash, Maya
- Bayad Center, SM Bills Payment
- PhilHealth Local Health Insurance Offices (LHIOs)

### 3.6 Penalties

**Penalties**

| Infraction | Penalty |
| --- | --- |
| Late payment | 2% per month of unpaid premium |
| Non-registration | Loss of benefits; back-payment required for reinstatement |
| Fraudulent claims | Criminal liability under RA 11223 |

## Section 4 -- Pag-IBIG / HDMF (Home Development Mutual Fund)

### 4.1 Legal Basis and Coverage

**4.1 Legal Basis and Coverage**

| Item | Detail |
| --- | --- |
| Law | Republic Act No. 9679 (Home Development Mutual Fund Law of 2009) |
| Agency | HDMF (Home Development Mutual Fund), commonly called Pag-IBIG Fund |
| Who must register | Employed (mandatory); self-employed (voluntary but strongly encouraged) |
| Benefits | Housing loan, multi-purpose loan, calamity loan, savings (with dividends) |
| Mandatory for self-employed | NO -- voluntary for self-employed and informal sector |

### 4.2 Contribution Rates

**4.2 Contribution Rates**  _(HDMF Circular No. 460 (eff. Feb 2024). Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Monthly Compensation | Employee Share | Employer Share | Total |
| --- | --- | --- | --- |
| ≤₱1,500 | 1% | 2% | 3% |
| >₱1,500 | 2% | 2% | 4% |
| Maximum Fund Salary (MFS) cap | ₱10,000 (HDMF Circular 460, eff. Feb 2024 — DOUBLED from ₱5,000) | ₱10,000 | Each share capped at ₱200 (2% × ₱10,000) |
| Self-employed (pays BOTH shares) | 2% | 2% | **Up to ₱400/month** at or above the MFS cap — NOT ₱200 |

**Self-employed contribution:**
- Minimum: ₱200/month
- May voluntarily contribute up to ₱5,000/month
- Higher contributions = higher savings + higher loan eligibility

### 4.3 Modified Pag-IBIG 2 (MP2) Savings

**Modified Pag-IBIG 2 (MP2) Savings**

| Feature | Detail |
| --- | --- |
| Minimum savings | ₱500/month (or lump sum) |
| Term | 5 years |
| Dividends | Tax-free; historically 6%--7% per annum |
| Withdrawal | After 5-year lock-in or upon qualified events |
| Additional benefit | Increases housing loan eligibility |

### 4.4 Payment Schedule

- Monthly contribution due by the 15th of the following month
- Can pay quarterly, semi-annually, or annually in advance
- Minimum 24 monthly contributions required for loan eligibility

### 4.5 Payment Methods

- Pag-IBIG Virtual (virtual.pagibigfund.gov.ph)
- Banks (BDO, BPI, Landbank, Metrobank)
- GCash, Maya
- Bayad Center, SM Bills Payment, 7-Eleven
- Pag-IBIG Fund branches

## Section 5 -- Registration Requirements

### 5.1 SSS Registration (Self-Employed)

**SSS Registration (Self-Employed)**

| Requirement | Detail |
| --- | --- |
| Form | SSS Form RS-1 (Self-Employed Registration) |
| Documents | Valid ID (2 government-issued), proof of income/business registration |
| Where | SSS branch or online (my.sss.gov.ph) |
| SSS Number | Issued upon registration; lifetime number |
| Income declaration | Must declare estimated monthly earnings |
| Change of MSC | Submit request at SSS branch or online to increase/decrease |

### 5.2 PhilHealth Registration (Self-Employed)

**PhilHealth Registration (Self-Employed)**

| Requirement | Detail |
| --- | --- |
| Form | PhilHealth Member Registration Form (PMRF) |
| Documents | Valid ID, proof of income, birth certificate (first-time) |
| Where | PhilHealth LHIO or online |
| PhilHealth Number | Issued upon registration; lifetime number |
| Income declaration | Self-declare monthly income for premium computation |

### 5.3 Pag-IBIG Registration (Self-Employed/Voluntary)

**Pag-IBIG Registration (Self-Employed/Voluntary)**

| Requirement | Detail |
| --- | --- |
| Form | HDMF Member's Data Form (MDF) |
| Documents | Valid ID, proof of income (if self-employed) |
| Where | Pag-IBIG branch or virtual.pagibigfund.gov.ph |
| Pag-IBIG MID Number | 12-digit Member ID issued upon registration |
| Loyalty Card | Free Pag-IBIG Loyalty Card (UMID equivalent) |

## Section 6 -- Computation Examples

### Example 1 -- Freelancer Earning ₱30,000/month

**Example 1 -- Freelancer Earning ₱30,000/month**

| Agency | Basis | Rate | Monthly Contribution |
| --- | --- | --- | --- |
| SSS | MSC ₱30,000 | 15% | ₱4,500 |
| PhilHealth | Income ₱30,000 | 5% | ₱1,500 |
| Pag-IBIG | Minimum voluntary | Fixed | ₱200 |
| **Total** |  |  | **₱6,200** |

Annual total: ₱6,200 × 12 = **₱74,400**

### Example 2 -- Freelancer Earning ₱15,000/month

**Example 2 -- Freelancer Earning ₱15,000/month**

| Agency | Basis | Rate | Monthly Contribution |
| --- | --- | --- | --- |
| SSS | MSC ₱15,000 | 15% | ₱2,250 |
| PhilHealth | Income ₱15,000 | 5% | ₱750 |
| Pag-IBIG | Minimum voluntary | Fixed | ₱200 |
| **Total** |  |  | **₱3,200** |

Annual total: ₱3,200 × 12 = **₱38,400**

### Example 3 -- Maximum Contributions

**Example 3 -- Maximum Contributions**

| Agency | Basis | Rate | Monthly Contribution |
| --- | --- | --- | --- |
| SSS | MSC ₱35,000 (max) | 15% | ₱5,250 |
| PhilHealth | Income ₱100,000+ (ceiling) | 5% | ₱5,000 |
| Pag-IBIG | Maximum voluntary | Fixed | ₱5,000 |
| **Total** |  |  | **₱15,250** |

Annual total: ₱15,250 × 12 = **₱183,000**

## Section 7 -- Tax Deductibility

**Tax Deductibility**  _(RA 10963 (TRAIN) repealing NIRC s.34(M). Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Contribution | Tax Deductible? | Basis |
| --- | --- | --- |
| SSS — self-employed person's OWN contribution | **NO** | Not deductible. Under OSD no additional deductions are allowed at all; under itemised deductions a person's own government contributions are personal in nature, not an ordinary-and-necessary business expense. |
| PhilHealth — self-employed person's OWN contribution | **NO** | Not deductible (same reasoning). The old NIRC s.34(M) health-premium deduction (PHP 2,400/yr) was **repealed by the TRAIN Law (RA 10963), effective 2018** — do not cite it. |
| Pag-IBIG — self-employed person's OWN contribution | **NO** | Not deductible (same reasoning). |
| EMPLOYER's contribution for its employees (SSS/PhilHealth/Pag-IBIG) | YES | A legitimate business expense of the employer. This is a different case from the self-employed person's own contribution — do not conflate them. |
| Pag-IBIG MP2 | NO | Savings programme, not a premium. |

## Section 8 -- Edge Cases

### 8.1 Multiple Income Sources

If a person is both employed AND self-employed:
- SSS: employer handles employed portion; self-employed contribution is separate
- PhilHealth: only one membership -- employer deducts; no double contribution
- Pag-IBIG: employer handles mandatory; may add voluntary on top

### 8.2 Overseas Filipino Workers (OFWs)

- SSS: Voluntary member; can choose MSC ₱5,000--₱35,000
- PhilHealth: OFW category; separate premium schedule
- Pag-IBIG: Voluntary; same ₱200 minimum

### 8.3 Kasambahay (Domestic Workers)

- SSS: Employer pays if salary ≤₱5,000; shared above
- PhilHealth: Employer pays full premium if salary ≤₱5,000
- Pag-IBIG: Employer pays if salary ≤₱5,000

### 8.4 Senior Citizens (60+)

- SSS: Can continue voluntary contributions until retirement claim
- PhilHealth: Lifetime member after 120 monthly contributions; no further payments needed
- Pag-IBIG: May continue voluntary contributions; eligible for retirement claim after age 65

### 8.5 Gaps in Payment

**Gaps in Payment**

| Agency | Effect of Gap | Remedy |
| --- | --- | --- |
| SSS | No benefit eligibility until minimum contributions met | Pay arrears with 2%/month penalty |
| PhilHealth | Benefits suspended after 9 months non-payment | Pay 3 months to reactivate (within qualifying period) |
| Pag-IBIG | Loan eligibility lost until 24 contributions met | Resume payments; no back-payment required |

## Section 9 -- Online Portal Reference

**Online Portal Reference**

| Portal | URL | Key Functions |
| --- | --- | --- |
| My.SSS | my.sss.gov.ph | View contributions, generate PRN, file claims |
| PhilHealth Member | memberinquiry.philhealth.gov.ph | Check status, update info, print MDR |
| Pag-IBIG Virtual | virtual.pagibigfund.gov.ph | View savings, apply for loans, update info |
| SSS Mobile | SSS Mobile App (iOS/Android) | Same as My.SSS |
| BIR (for deductions) | bir.gov.ph | eFPS, annual ITR filing |

## Section 10 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| SSS contribution rates 2025 | SSS Circular No. 2024-006 (December 19, 2024) |
| SSS law | Republic Act No. 11199 (Social Security Act of 2018) |
| SSS rate schedule (RA 11199) | Section 18-A (phased increase 2019--2025) |
| PhilHealth premium rate | RA 11223 Sec. 10; PhilHealth Circular 2024-0009 |
| PhilHealth UHC | Republic Act No. 11223 (Universal Health Care Act of 2019) |
| Pag-IBIG law | Republic Act No. 9679 (HDMF Law of 2009) |
| Pag-IBIG contributions | HDMF Circular No. 274 (amended rates) |
| Tax deductibility | NIRC Sec. 34(M); RR 11-2018 |
| BIR self-employed registration | BIR RR 7-2012 |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, labour law practitioner, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
