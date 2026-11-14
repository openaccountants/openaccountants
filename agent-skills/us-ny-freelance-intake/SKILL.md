---
name: us-ny-freelance-intake
description: "Entry point for a New York resident freelancer, sole proprietor or single-member LLC owner who wants help with a 2026 federal and New York return. Runs a scope check (entity, residence, multi-state income, open years), asks for the documents, reads them, fills the gaps, and hands a confirmed fact sheet to us-ny-return-assembly, naming which federal and New York skills apply (IT-201, NYC UBT, MCTMT, estimated tax, LLC fee). Carries no rates of its own; every figure is in the linked skill. Trigger on \"I'm a freelancer in New York\", \"NYC self-employed taxes\", \"I have an LLC in NY\", \"New York freelance tax return\", \"I live in Manhattan and do contracting\". Full-year New York residents only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-ny-freelance-intake"
  jurisdiction: "US-NY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# New York freelancer intake, tax year 2026

> **Source-cited draft.** Routing built from the New York Tax Department's IT-201 and IT-2105 instructions, the residency FAQ and the NYC Department of Finance UBT page, read on 2026-11-13 and 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** This skill decides whether the client is in scope, gathers the documents and facts, and routes them. A full-year New York resident who is a sole proprietor or a single-member LLC disregarded for federal tax goes through the federal skills, then `ny-it-201-resident-return`, plus `nyc-ubt` if the business is carried on in New York City, the MCTMT if self-employment earnings are allocated to the MCTD, and `ny-estimated-tax` for 2027 payments, and finally `us-ny-return-assembly`. It states no tax figures: each threshold lives in the skill that owns it.

## Scope and who this is for

In scope: a full-year New York State resident (New York City, Yonkers or rest of state) who is a sole proprietor or the owner of a single-member LLC disregarded for federal tax, filing Form 1040 and Form IT-201 for tax year 2026.

Out of scope, and where it goes:

| Situation | Skill or action |
| --- | --- |
| Moved into or out of New York State or New York City during 2026, or lives outside New York | `ny-residency-leaving-new-york` (Form IT-203); refer the return |
| Multi-member LLC or partnership | `us-form-1065-partnership`; refer |
| S corporation or C corporation | refer (New York Article 9-A is `ny-corporate-franchise-article-9a`) |
| Should the client become an S corporation? | `us-s-corp-election-decision` |
| Income taxed by another state | `us-multi-state-residency-and-allocation`; refer |

## Ask the client first

1. **Business structure:** sole proprietor, single-member LLC, multi-member LLC, S corporation, C corporation, or not sure. If not sure: did they file Form 2553, or receive a W-2 from their own business? Either means an S corporation.
2. **Where did they live all of 2026,** and did they move? New York City (the five boroughs), Yonkers, rest of New York State, part-year, or outside New York.
3. **Where is the work done?** Home office or office address, and whether any work is done outside New York City or outside the MCTD counties.
4. **Filing status and dependents** for 2026.
5. **Any 2026 income from other states, K-1s, rental property, active trading, foreign accounts, or employees on payroll?**
6. **Were the 2025 returns filed, and is any year under audit or amended?**

## The method, step by step

1. **Open with one message:** a one-line greeting, a one-line summary of the flow (scope check, upload, gaps, handoff), and a reminder that everything produced must be reviewed by a credentialed tax professional (EA, CPA or tax attorney) before filing. Then ask the scope questions at once, using the host's structured question tool where it has one.
2. **Scope check, first batch:** structure (question 1), residence (question 2), revenue range for 2026 (record it; it tells `nyc-ubt` whether a return may be due). Stop on any answer in the refusal table below.
3. **Scope check, second batch:** filing status (question 4), the 2025 return (question 6), the special items (question 5), whether New York estimated payments were made in 2026 (all four, some, none, not sure), and income from outside New York.
4. **Ask for the documents in one list:**
   - business bank and card statements for 2026 (CSV or PDF);
   - every 1099-NEC, 1099-MISC and 1099-K, and any W-2 from side employment;
   - 1095-A, B or C;
   - year-end retirement account statements;
   - federal, New York State and New York City estimated payment confirmations for 2026;
   - the 2025 federal return, Form IT-201 and, if filed, Form NYC-202 or NYC-202S;
   - any Tax Department or NYC Department of Finance notices;
   - LLC formation papers (Articles of Organization filed with the New York Department of State).
5. **Read the documents and extract:**
   - bank: total deposits (gross receipts), client payments, IRS (EFTPS) payments, New York State DTF payments, NYC Department of Finance payments, retirement contributions, health insurance premiums, business expenses by type, contractor payments, any New York LLC filing fee paid;
   - each 1099: payer, TIN, amount, matched to deposits;
   - the 2025 returns: federal AGI and total tax; IT-201 New York AGI, taxable income, state tax, city taxable income and city tax; the household credit; UBT paid. These feed the 2026 estimated tax safe harbour (`ny-estimated-tax`) and the federal one (`us-quarterly-estimated-tax`);
   - retirement statements: plan type, contributions and dates (limits in `us-self-employed-retirement`).
6. **Confirm in one compact summary:** identity, filing status, dependents, residence (city, Yonkers or rest of state), structure; gross receipts by client; expenses by category; the New York flags (UBT likely or not, MCTMT zone, state and city estimates paid). Ask "Is any of this wrong?"
7. **Fill the gaps** that documents rarely answer: home office (exclusive use, square feet); the share of work done in New York City if any is done outside; the source of health insurance (NY State of Health marketplace, employer, COBRA); commuter benefits from any W-2 job; the MCTD county where the business is carried on.
8. **Route and hand off.** Set the flags and pass the fact sheet to `us-ny-return-assembly`, which runs the skills in order:

| Flag | Set when | Skill |
| --- | --- | --- |
| Federal core | always | `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, `us-self-employed-retirement`, `us-self-employed-health-insurance`, `us-qbi-deduction`, `us-federal-return-assembly`, `us-quarterly-estimated-tax` |
| Contractors paid | the client paid contractors | `us-1099-nec-issuance` |
| State return | always | `ny-it-201-resident-return` |
| NYC UBT | business carried on wholly or partly in New York City | `nyc-ubt` |
| MCTMT | business carried on in an MCTD county (the five boroughs, Dutchess, Nassau, Orange, Putnam, Rockland, Suffolk, Westchester) | `ny-mctmt` (the IT-201 lines are in `ny-it-201-resident-return`) |
| State estimates | always, for 2027 | `ny-estimated-tax` |
| LLC fee | single-member LLC | `ny-llc-filing-fee-it-204-ll` |
| PTET question | the client asks about the pass-through entity tax | `ny-pte-tax-ptet` |

9. **Handoff message:** "Intake complete. Handing off to the return assembly workflow. You will receive: a working paper (federal, New York State and New York City lines), a reviewer brief with positions, citations and flags, the form packages (1040, IT-201, NYC-202 if it applies), 2027 estimated tax schedules (federal, New York State, New York City), and an action list with deadlines."

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Single-member LLC taxed as an S corporation (Form 2553 filed) | Not a disregarded entity: refuse under R-NYI-2 |
| Single-member LLC owned by a married couple in New York (not a community property state) | Two owners make it a partnership for federal tax: refuse under R-NYI-1 |
| Lives in New York State all year but moved between New York City and the rest of the state | Part-year New York City resident: refuse under R-NYI-3 |
| Domiciled elsewhere but kept a permanent place of abode in New York for substantially all of 2026 and spent 184 days or more there | A statutory resident, taxed as a full-year resident; in scope, but record the day count and send the residency question to `ny-residency-leaving-new-york` for the reviewer ([residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm)) |
| Lives outside New York City but the business is carried on in New York City | UBT can still apply (it follows where the business is carried on): set the UBT flag |
| Lives in Yonkers | In scope; the Yonkers lines are in `ny-it-201-resident-return` |
| Business carried on outside the MCTD (for example Albany or Erie County) | No MCTMT flag |
| W-2 job as well as the business | In scope; the W-2 feeds the federal and IT-201 lines; no refusal |

### Defaults when a fact is missing

| Missing fact | Default | Flag for the reviewer |
| --- | --- | --- |
| Where the work is done | The home or office address the client gave | Yes, if any client is outside New York City |
| MCTD county | The county of the business address | No |
| Whether 2026 New York estimates were paid | None paid, until a confirmation or a bank debit shows otherwise | Yes |
| The 2025 IT-201 | Ask for it; without it the prior-year safe harbour in `ny-estimated-tax` cannot be used | Yes |
| Health insurance source | Ask; do not assume the self-employed health insurance deduction | Yes |

### Red flags to raise before the handoff

| Red flag | Why it matters |
| --- | --- |
| Bank deposits well above the 1099 total | Clients who send no 1099 still paid income; the gap is income unless shown to be a transfer, a loan or a refund (Case 1) |
| A Tax Department or NYC Department of Finance notice | May mean an open year (R-NYI-4) |
| Payments to the NYC Department of Finance but no NYC-202 on file | UBT estimates paid without a return; check `nyc-ubt` |
| No LLC filing fee paid for a single-member LLC with New York source income | Check `ny-llc-filing-fee-it-204-ll` |

## Worked cases

The client is invented.

**Case 1, the gross receipts check before the handoff.** A Manhattan designer with a single-member LLC shows total 2026 business account deposits of USD 148,900. Of these, USD 6,000 is a transfer from her personal savings and USD 400 is a refund from a supplier; neither is income. Her 1099-NEC forms total USD 121,500 and one 1099-K from a payment platform shows USD 18,000. Gross receipts from the bank are 148,900 minus 6,000 minus 400 = USD 142,500. The forms cover 121,500 + 18,000 = USD 139,500. The gap of USD 3,000 is income from clients who sent no 1099; it goes into gross receipts, and the fact sheet records USD 142,500 with the gap explained. Intake records the figure and the flag; it does not test it against any threshold (that is for `nyc-ubt` and `us-schedule-c-and-se-computation`).

```oa-check
name: NY freelancer intake, bank deposits to 1099 reconciliation (2026)
inputs:
  deposits: 148900
  owner_transfers: 6000
  supplier_refunds: 400
  form_1099_nec: 121500
  form_1099_k: 18000
steps:
  - gross_receipts: deposits - owner_transfers - supplier_refunds
  - reported_on_forms: form_1099_nec + form_1099_k
  - unreported_gap: gross_receipts - reported_on_forms
expected:
  gross_receipts: 142500.00
  reported_on_forms: 139500.00
  unreported_gap: 3000.00
```

## When to refuse or refer

| Code | Trigger | What to say |
| --- | --- | --- |
| R-NYI-1 | Multi-member LLC | "Multi-member LLCs file Form 1065 as partnerships. You need a CPA familiar with partnership returns and New York PTET elections." |
| R-NYI-2 | S corporation or C corporation | "I do not cover corporate returns. Form 1120-S or 1120 and New York Form CT-3 or CT-3-S need a CPA." |
| R-NYI-3 | Lives outside New York, or moved into or out of New York State or New York City in 2026 | "I am set up for full-year New York residents only. A part-year or nonresident return (Form IT-203, with IT-360.1 for the city) needs a CPA who handles them." See `ny-residency-leaving-new-york`. |
| R-NYI-4 | A skipped year, an amended return or an open audit | "Skipped years or returns under audit need a CPA who can assess penalty exposure and represent you." |
| R-NYI-5 | Income from other states | "Multi-state allocation and the credit for tax paid to another state need a CPA who handles multi-state returns." |
| R-NYI-6 | Rental property, active crypto or day trading, foreign accounts over USD 10,000, employees on payroll, or K-1 income | Stop, name the item, and refer: these are outside the freelancer workflow. |

When a refusal fires: stop, state the specific reason, say what to do next, and do not work around it.

## Completion checklist

- [ ] Structure, residence and filing status confirmed, and no refusal fired
- [ ] Every document on the list received, or its absence recorded
- [ ] Gross receipts reconciled from the bank to the 1099s, the gap explained (Case 1)
- [ ] 2025 federal and IT-201 figures recorded for the safe harbours
- [ ] New York State, New York City and federal 2026 estimates listed by date and amount
- [ ] Flags set: UBT, MCTMT zone, LLC fee, contractors, PTET question
- [ ] Fact sheet confirmed by the client and handed to `us-ny-return-assembly`

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IT-201-I (2025). Read for who files Form IT-201 (full-year residents) and the New York City, Yonkers and MCTMT lines. | https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf | 2026-11-13 |
| IT-2105-I (2026). Read for the MCTD counties and zones and who must pay estimated tax. | https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf | 2026-11-13 |
| NYC Department of Finance, Unincorporated business tax. Read for who is subject to the UBT. | https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page | 2026-11-13 |
| Residency FAQ. Read for domicile, the statutory resident test (permanent place of abode and 184 days) and New York City residence. | https://www.tax.ny.gov/pit/file/nonresident-faqs.htm | 2026-11-14 |

Not yet confirmed: the 2026 Form IT-201 instructions are not published; this skill carries no tax figures (the 184-day count is from the residency FAQ), so nothing here depends on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-ny-freelance-intake` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-ny-freelance-intake. If neither is available, confirm every figure against the official source pages cited above before relying on it.
