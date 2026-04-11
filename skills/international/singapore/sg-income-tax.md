---
name: sg-income-tax
description: >
  Singapore income tax return (Form B/B1) for self-employed individuals. Covers progressive brackets (0–22%), trade income computation, capital allowances, approved deductions, and NO filing season if income below threshold.
version: 0.1
jurisdiction: SG
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Singapore Income Tax (Form B) v0.1

## What this file is

**Obligation category:** IT (Income Tax)
**Functional role:** Computation + Return
**Status:** Stub — content not yet written. See SKILL-TAXONOMY.md for where this fits.

This file is a content skill that loads on top of `income-tax-workflow-base`.

**Tax year coverage.** This skill targets **tax year 2025**.

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers:

- **Forms:** Form B, Form B1
- **Entity types:** Self-employed individuals, sole proprietors, freelancers

This skill does NOT cover:

- Partnerships, corporations
- [Additional out-of-scope items to be defined]

---

## Section 2 — Filing requirements

[To be completed. Cite primary sources: ITA (Singapore)]

---

## Section 3 — Rates and thresholds

| Item | Amount | Source |
|------|--------|--------|
| [To be completed] | | |

---

## Section 4 — Computation rules

[To be completed. Step-by-step mechanical logic.]

---

## Section 5 — Edge cases and special rules

[To be completed.]

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] All input figures trace to source documents
- [ ] Rates and thresholds match the tax year
- [ ] Computation follows the steps in Section 4
- [ ] Edge cases from Section 5 are checked
- [ ] Output format matches the base skill spec

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
