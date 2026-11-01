---
name: eg-formation
description: Use this skill whenever asked about how to register, form, or set up a business in Egypt as a self-employed person, freelancer, professional, sole proprietor, or small company. Trigger on phrases like "register a business Egypt", "tax card Egypt", "how to start a business Egypt", "sole proprietor Egypt", "freelance registration Egypt", "GAFI LLC Egypt", "commercial register Egypt", "open a tax file Egypt", "register with the ETA", "البطاقة الضريبية", "السجل التجاري", "تسجيل منشأة فردية", "فتح ملف ضريبي", "تأسيس شركة ذات مسؤولية محدودة", "نقابة مهنية", "التأمينات الاجتماعية للعمل الحر". Covers obtaining a tax card and tax file with the Egyptian Tax Authority (ETA), the commercial register, professional syndicate (نقابة) membership, choosing the simplified vs general regime at registration, VAT and e-invoicing registration, social insurance registration, and forming an LLC via GAFI. AI replies in the user's language (English or Arabic).
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Formation

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026, law as read on 1 November 2026. Reply in the user's language (English or Arabic) and keep the native terms: البطاقة الضريبية (tax card), السجل التجاري (commercial register), منشأة فردية (sole proprietorship), نقابة (professional syndicate), الهيئة العامة للاستثمار (GAFI).

## Scope

This skill sets up a self-employed person in Egypt: tax card (البطاقة الضريبية) and tax file (ملف ضريبي) with the Egyptian Tax Authority (ETA), commercial register where the activity needs it, syndicate membership for regulated professions, regime choice, then VAT, e-invoicing and social insurance. It also outlines forming a limited liability company (شركة ذات مسؤولية محدودة) through GAFI.

Authorities: ETA (tax card, tax file, VAT, e-invoicing), GAFI (companies), the commercial register, NOSI (الهيئة القومية للتأمينات الاجتماعية), and the relevant syndicate. Currency: EGP. Laws: Income Tax Law No. 91 of 2005; Law No. 6 of 2025; VAT Law No. 67 of 2016; Social Insurance Law No. 148 of 2019; Law No. 152 of 2020 (MSME development).

Owned elsewhere: VAT figures in `egypt-vat`; Law 6 mechanics in `eg-sme-tax`; contribution rates in `eg-social-insurance`; books in `eg-bookkeeping`; company accounts in `eg-financial-statements`.

## Ask the client first

- What is the activity: trade or industry, craft, or a profession? Is it a regulated profession?
- Is the client an Egyptian national? If not, what passport, residence permit and approvals are held?
- What turnover is expected in the first year?
- One owner, or partners and outside investors?
- Does the client need to issue invoices before licensing is finished?
- Do 90% or more of expected consultancy fees come from one or two clients?

## The method, step by step

### Rates and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Law 6 turnover tax, turnover under EGP 500,000 | 0.4% of turnover | 2026 | Business asked for Law 6; turnover not above EGP 20 million (Art. 10) | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| Law 6, EGP 500,000 to under EGP 2,000,000 | 0.5% | 2026 | same conditions | same |
| Law 6, EGP 2,000,000 to under EGP 3,000,000 | 0.75% | 2026 | same conditions | same |
| Law 6, EGP 3,000,000 to under EGP 10,000,000 | 1% | 2026 | same conditions | same |
| Law 6, EGP 10,000,000 to EGP 20,000,000 | 1.5% | 2026 | same conditions | same |

### Sole proprietor registration

A sole proprietor has no separate legal personality. The person and the business are one, with unlimited personal liability.

1. **Identity.** Egyptian national: national ID (الرقم القومي). Foreign national: refer (see below).
2. **Place of activity.** Lease (عقد إيجار) or ownership document for the business address.
3. **Tax file and tax card.** Register at the competent tax office (المأمورية) for the address or through the ETA portal (eta.gov.eg, بوابة الممول). The tax card carries the tax registration number, needed to invoice and to register for VAT. Apply within 30 days of starting the activity; the office issues the card within 5 working days, it runs for five years and is renewable, and changes to your data are notified within 30 days ([Law No. 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf), Arts 25, 27, 28).
4. **Temporary tax card, if set-up is unfinished.** Ask the ETA for a temporary tax card valid for eight months to finish founding and licensing the activity ([Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf), new Article 27 bis of the Unified Tax Procedures Law, in force from 29 July 2026). It cannot be used to issue e-receipts or e-invoices. Amounts due to the ETA in its life are payable from its expiry.
5. **Commercial register or syndicate.** Commercial and industrial activity goes on the commercial register. Regulated professions join their syndicate first: lawyers (نقابة المحامين), doctors, dentists and pharmacists (their medical syndicates), engineers (نقابة المهندسين, Law No. 66 of 1974).
6. **Regime.** Compare Law 6 and the normal basis (below). To join Law 6, file form 10/1 (طلبات) on the ETA website ([MoF Decision No. 420 of 2025](https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf), Article 1).
7. **VAT.** Register within 30 days of total taxable and exempt sales reaching EGP 500,000 in 12 months ([VAT Law No. 67 of 2016](https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf), Art. 16; `egypt-vat`). Below that, UTPL Art. 25 still requires registration on the ETA electronic system for a fee of at most EGP 500 a year. It is measured on turnover, not profit.
8. **E-invoice or e-receipt.** Registration and onboarding are in `eg-bookkeeping`. A tax file does not by itself register anyone for these.
9. **Social insurance.** Register with NOSI as self-employed at a chosen contribution wage; see `eg-social-insurance`. It is separate from income tax and VAT, and Law 6 does not replace it.

Books start on day one: regular books under Article 38, or the simplified set in Law 6 (`eg-bookkeeping`). The first return filed counts as notice of starting the activity ([Law No. 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf), Article 31).

### Regime choice at registration

| Factor | Law 6 of 2025 | Normal basis, Law 91 of 2005 |
|---|---|---|
| Turnover | Up to EGP 20,000,000 | Any; required above the cap |
| Margin | High margin favours a tax on turnover | Thin margin or a loss favours a tax on profit |
| Records | Simplified set | Regular books under Commercial Law |
| Large documented costs | No benefit | Lower the tax |
| Commitment | No exit for five years | Year to year |

Enrolment is not automatic. Model both before filing form 10/1.

### Sole proprietor or company

| Factor | Sole proprietor | LLC through GAFI |
|---|---|---|
| Legal personality | None | Separate entity |
| Liability | Unlimited personal | Limited to capital contributed |
| Set-up | ETA, plus register or syndicate | GAFI electronic incorporation service |
| Income tax | Personal income tax or Law 6 | Corporate tax; Law 6 by its own conditions |
| Accounts | `eg-bookkeeping` | `eg-financial-statements` |

Choose an LLC for limited liability, partners or investors, or clients who require a company. Otherwise a solo freelancer starts as a sole proprietor.

### Forming an LLC through GAFI

GAFI lists these digital services: electronic incorporation, certificate of non-confusion for the company name, digital submission of required documents, and approved investor representatives ([GAFI Digital Services](https://gafi.gov.eg/en/contenttemplate/b208989f-efbc-486f-9f92-761ac716007f)). "Register Your Company" on the GAFI site starts the process.

1. Get the certificate of non-confusion for the name.
2. Submit the incorporation application and documents digitally.
3. After incorporation, complete the commercial register entry and company tax card.
4. Register for VAT, e-invoicing and social insurance as they apply.

### Closing down

Tell the ETA and close the tax file, file final returns and settle income tax and VAT. Cancel the commercial register entry or syndicate membership and stop contributions with NOSI. An LLC follows liquidation.

## Boundary and exception table

| Situation | Rule | Source |
|---|---|---|
| Needs to invoice while on a temporary card | Permanent card and system registration first | [Law 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf) Art. 2 |
| Exactly EGP 20,000,000 turnover | Still inside Law 6 ("does not exceed") | [Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) Art. 10 |
| Consultant, 90% or more from one or two clients | Excluded from Law 6 | [Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) Art. 4 |
| Splitting a business to stay under a cap | Improper entry to Law 6 | [Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) Art. 4 |
| Leaving Law 6 | Form 1/11, after at least five years from the day after the request | [MoF 420 of 2025](https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf) Art. 1 |

## Worked cases

**Case 1: freelance designer, EGP 180,000 a year.** Tax file and card. No syndicate. Under EGP 500,000, so Law 6 tax would be 0.4%: EGP 720. VAT per `egypt-vat`. Register with NOSI.

```oa-check
name: Designer, Law 6 tax at EGP 180,000
inputs:
  turnover: 180000
  rate: 0.004
steps:
  - tax: turnover * rate
expected:
  tax: 720.00
```

**Case 2: decision, Law 6 or normal basis for a developer, EGP 900,000 a year.** Law 6 tax at 0.5% is EGP 4,500. If tax on actual profit under `eg-income-tax` is EGP 60,000 (illustration), Law 6 saves EGP 55,500 a year, or EGP 277,500 over the five-year lock-in. If the developer has one client paying consultancy fees of 90% or more, Law 6 is closed and the question falls away. VAT and e-invoicing follow `egypt-vat` and `eg-bookkeeping`.

```oa-check
name: Decision, developer, five-year saving under Law 6
inputs:
  turnover: 900000
  rate: 0.005
  normal_tax: 60000
  years: 5
steps:
  - law6_tax: turnover * rate
  - saving: normal_tax - law6_tax
  - five_year: saving * years
expected:
  law6_tax: 4500.00
  five_year: 277500.00
```

**Case 3: licensed engineer.** Engineers Syndicate membership first, then tax file and card. Confirm the activity is not an excluded consultancy before choosing Law 6.

**Case 4: two founders with investors.** LLC through GAFI: multiple owners and outside capital rule out a sole proprietorship.

## When to refuse or refer

Refer to a credentialed Egyptian accountant or lawyer when the activity sits between commercial and professional, a regulated profession raises licensing questions, the client is a foreign national or in a free zone or special economic zone, turnover is near a threshold, the client is choosing sole proprietor or LLC, there is single-client concentration or fragmentation, or there are unregistered prior years, back taxes or penalties.

Never tell anyone they can operate without a tax card and tax file. Never tell a regulated professional they can practise without syndicate membership. Never advise splitting a business to stay under a threshold. Never recommend an LLC by default.

## Filing and payment

Annual return: individuals before 1 April; companies before 1 May or within four months of the financial year end ([Law No. 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf), Article 31).

## Completion checklist

- [ ] National ID (or passport and residence permit).
- [ ] Proof of business address.
- [ ] Tax file opened and tax card issued, or temporary card with its eight-month limit noted.
- [ ] Commercial register entry or syndicate membership.
- [ ] Regime modelled; form 10/1 filed if Law 6.
- [ ] VAT, e-document and NOSI registrations done as they apply.
- [ ] LLC only: name certificate, GAFI incorporation, company tax card, bank account.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law No. 150 of 2026 (Arts 1 to 3), gazette, rendered pages read | https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf | 2026-11-01 |
| Correction notice for Laws 149, 150, 151 of 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-01 |
| Unified Tax Procedures Law No. 206 of 2020, Arts 25, 27, 28, 31, 38, 69 to 71, gazette text | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-01 |
| Law No. 6 of 2025, Arts 7 to 10, 12, 13 | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-01 |
| MoF Decision No. 420 of 2025, Arts 1 to 4 | https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf | 2026-11-01 |
| GAFI Digital Services page, real browser | https://gafi.gov.eg/en/contenttemplate/b208989f-efbc-486f-9f92-761ac716007f | 2026-11-01 |

Not yet confirmed: EGP 250,000 VAT threshold and 31 March 2026 deadline attributed to Resolution No. 281 of 2025 (VAT Law Art. 16 reads EGP 500,000, the figure both skills use; the decision is not on ETA's VAT law list and its text was not found); age 21 and other eligibility rules; ETA document checklist and which steps are online; whether a residential address is allowed; commercial register and GAFI fees; "low hundreds of USD" incorporation fees; absence of minimum LLC capital; single-member LLC rule under Law 159 of 1981; GAFI step order and articles of association rules (the GAFI portal page failed to load on 2026-11-01); accountants' registration path (Ministry of Finance register, Syndicate of Commercial Professions, ESAA); the rule that a professional needs no commercial register entry; VAT voluntary registration; e-invoice penalty figures; deregistration clearances. Rates of 21% for the self-employed were not reread here; see `eg-social-insurance`.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).

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
