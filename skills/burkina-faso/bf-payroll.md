---
name: bf-payroll
description: Burkina Faso Payroll (IUTS & TPA) Skill v1.0
jurisdiction: BF
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burkina Faso Payroll (IUTS & TPA)

## Burkina Faso Payroll (IUTS & TPA) Skill v1.0

> AI-drafted from official sources (DGI Burkina Faso CGI — Loi 058-2017/AN, Art. 105–119 IUTS, Art. 227–230 TPA, Art. 760–769 penalties, OCR-verified from the official 2018 edition; SMIG 2024 decree). Pending accountant verification. The pre-2017 IUTS scale (2%–30%) is OUTDATED — use the Art. 110 scale below.

## Section 1 -- Quick reference

**Quick reference**  _(CGI Art. 105-119, 227-230, 760-769)_

| Field | Value |
| --- | --- |
| Country | Burkina Faso |
| Currency | FCFA (XOF) |
| Salary tax | IUTS — Impôt Unique sur les Traitements et Salaires |
| IUTS basis | Monthly taxable salary (after abatement), progressive (CGI Art. 110) |
| Professional-expenses abatement | 25% of base salary (20% for senior categories) (CGI Art. 111) |
| Pension/retirement deduction | Deductible within 8% of base salary (CGI Art. 111) |
| Family-charge reductions | 1 charge 8%, 2 charges 10%, 3 charges 12%, 4 charges 14% of computed tax; max 4 charges (CGI Art. 113) |
| Employer obligation | Withhold IUTS monthly for the Treasury (retenue à la source) (CGI Art. 112, 115) |
| IUTS payment deadline | First 10 days of the following month (CGI Art. 116) |
| Annual employer return | État nominatif of remunerations, before 30 April (CGI Art. 117) |
| TPA (employer payroll tax) | 3% of taxable remuneration incl. benefits in kind (CGI Art. 229) |
| TPA payment deadline | By the 10th of the following month (CGI Art. 230) |
| SMIG (minimum wage) | 45,000 FCFA/month (decree of 21 Jan 2024) |
| IUTS late/no withholding penalty | 50% of un-withheld amounts + 1% per month (CGI Art. 760) |
| Authority | Direction Générale des Impôts (DGI) |
| Primary legislation | CGI (Loi 058-2017/AN) Art. 105–119, 227–230, 760–769 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | June 2026 |

## Section 2 -- IUTS progressive scale (monthly taxable income)

**IUTS progressive scale (monthly taxable income)**  _(CGI Art. 110)_

| Monthly taxable income (FCFA) | Rate |
| --- | --- |
| 0 to 30,000 | 0% |
| 30,100 to 50,000 | 12.10% |
| 50,100 to 80,000 | 13.90% |
| 80,100 to 120,000 | 15.70% |
| 120,100 to 170,000 | 18.40% |
| 170,100 to 250,000 | 21.70% |
| 250,100 and above | 25% |

Per CGI Art. 110 (current scale; the older 2%–30% scale is repealed):

## Section 3 -- From gross to taxable, then to tax

- **Step 1 - Start point** — Start from gross salary including taxable allowances and benefits in kind.
- **Exempt-allowance caps** — Housing 20% of taxable salary, max 50,000 FCFA/mo; function 5%, max 30,000; transport 5%, max 20,000 FCFA  _(CGI Art. 106)_
- **Professional-expenses abatement and pension deduction** — Deduct the 25% professional-expenses abatement (20% for senior categories) and pension contributions within 8% of base salary.  _(CGI Art. 111)_
- **Apply Art. 110 scale** — Apply the Art. 110 scale to the monthly taxable income.  _(CGI Art. 110)_
- **Family-charge reduction** — Reduce the computed tax by the family-charge reduction (8/10/12/14% for 1–4 charges; max 4). Eligible charges: minor/infirm children or under-25 in study; supported orphans; a non-salaried spouse.  _(CGI Art. 113)_

## Section 4 -- TPA (Taxe Patronale d'Apprentissage)

- **TPA rate** — 3% % of total cash remuneration plus benefits in kind  _(CGI Art. 229)_
- **TPA base estimation** — Estimated as for IUTS.  _(CGI Art. 228)_
- **TPA payment deadline and semi-annual option** — Declared and paid by the 10th of the following month; semi-annual option if monthly TPA <= 2,500 FCFA.  _(CGI Art. 230)_
- **CGA member abatement** — CGA members get a 20% abatement on the base.  _(CGI Art. 228-2)_
- **TPA exemptions** — Exemptions: State and local authorities, diplomatic missions, private education/health, non-profits.  _(CGI Art. 227-2)_

## Section 5 -- Filing and penalties

- **IUTS and TPA filing deadline and semi-annual option** — IUTS and TPA declared and paid in the first 10 days of the following month. Small-amount semi-annual option: IUTS <= 5,000 FCFA/mo; TPA <= 2,500 FCFA/mo.  _(Art. 116, 230)_
- **IUTS penalties** — No/insufficient withholding 50% + 1%/month; withheld but paid late (<=60 days) 25%/month; >60 days late 100% + 1%/month; withheld but never paid 200% + 1%/month; employer-obligation breaches 25%, min 25,000 FCFA.  _(Art. 760-762)_
- **TPA late filing penalty** — 25% of duties due.  _(Art. 769)_

## Section 6 -- Prohibitions

- **Prohibition - outdated scale** — NEVER use the pre-2017 IUTS scale (2%–30%) — use the Art. 110 scale above.
- **Prohibition - family charges cap** — NEVER allow more than 4 family charges.
- **Prohibition - omit TPA or CNSS** — NEVER omit TPA (3%) or CNSS employer contributions (see bf-social-contributions).
- **Prohibition - compute numbers** — NEVER compute numbers — the engine handles arithmetic.
- **Confirm current sources** — Confirm the SMIG and every article number against current sources before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
