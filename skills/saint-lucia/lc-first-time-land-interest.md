---
name: lc-first-time-land-interest
description: >
  Saint Lucia deduction for interest paid by first-time residential landowners, new
  section 59D of the Income Tax Act inserted by the Income Tax (Amendment) (No. 2) Act 10
  of 2026. Covers the resident first-time landowner test, the 22,000 square foot parcel
  limit, deeds registered from 2 May 2026, the 50% deduction of interest paid in the
  year, its exclusion from the EC$40,000 cap, and the same Act's company return
  extension and late payment penalty change to 6%. Trigger phrases include section 59D,
  Saint Lucia first-time landowner, land loan interest deduction St Lucia.
version: 1.0
jurisdiction: LC
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Lucia first-time landowner interest deduction

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Section 59D of the Income Tax Act, Cap. 15.02, inserted by section 3 of the Income Tax (Amendment) (No. 2) Act 10 of 2026 (assented 16 July 2026, dated 21 July 2026), for the 2026 income year. It is a deduction from income, not a tax credit, and not the owner-occupied mortgage interest deduction ([lc-personal-tax-deductions](lc-personal-tax-deductions.md)). It does not cover property transfer tax, registration charges, joint borrowers or the full return. Amounts are EC$.

## Ask the client first

1. Is the claimant a resident individual?
2. Has the claimant ever held a legal interest, alone or jointly, in residential land in Saint Lucia?
3. Size of the parcel in square feet and its intended use.
4. Date the deed was registered at the Registry of Land.
5. Was the loan the claimant's, and was it used to buy the land? Interest paid in the year (lender statement separating interest and principal).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Deduction, s.59D(1) | A fifty per cent deduction of interest paid during the year of income on money borrowed to purchase the land | [Act 10 of 2026, s.3](https://npc.govt.lc/laws/download/UjVlcXRvZTd3RG93ODVaQ0tsbWNwY3BZUU5uNEVJM3lpam1HV0lqRS9SRUNzTmp6YisvZFBmQTR2RUw1MFprRHJYRytQRkJMOUo0c0tWQ0YwY2ZoUzJNRUNWSVhnWjEvSll1MW9DSnBIUndsMTNkTDFVOWN0UHpZRk9XZmxhdWg=) |
| Parcel size | Land of not more than twenty two thousand square feet, for residential purposes | same |
| Deed registration | Registered at the Registry of Land from 2 May 2026 | same |
| Cap, s.59D(2) | Excluded from the overall cap of forty thousand dollars under section 44(4)(a) | same |
| First-time landowner, s.59D(3) | Never previously held a legal interest, solely or jointly, in residential land in Saint Lucia, and acquires a parcel intended for residential use | same |
| Company return extension, s.96(3) | Up to five months from the end of the year of assessment, on conditions | [Act 10 of 2026, s.4](https://npc.govt.lc/laws/download/UjVlcXRvZTd3RG93ODVaQ0tsbWNwY3BZUU5uNEVJM3lpam1HV0lqRS9SRUNzTmp6YisvZFBmQTR2RUw1MFprRHJYRytQRkJMOUo0c0tWQ0YwY2ZoUzJNRUNWSVhnWjEvSll1MW9DSnBIUndsMTNkTDFVOWN0UHpZRk9XZmxhdWg=) |
| Penalty for failure to pay tax by the due date, s.134(1) | "six per cent or such other rate as may be prescribed by the Minister" replaces the old rate | [Act 10 of 2026, s.5](https://npc.govt.lc/laws/download/UjVlcXRvZTd3RG93ODVaQ0tsbWNwY3BZUU5uNEVJM3lpam1HV0lqRS9SRUNzTmp6YisvZFBmQTR2RUw1MFprRHJYRytQRkJMOUo0c0tWQ0YwY2ZoUzJNRUNWSVhnWjEvSll1MW9DSnBIUndsMTNkTDFVOWN0UHpZRk9XZmxhdWg=) |

### Steps

1. **Resident individual** and **first-time landowner** (no prior sole or joint residential land interest).
2. **Parcel:** residential, 22,000 square feet or less; deed registered from 2 May 2026 (not the Act's July date).
3. **Loan:** the claimant's own borrowing, used to buy the land.
4. **Amount:** interest paid in the income year x 50%. Principal and purchase price are not interest.
5. **Cap:** claim outside the EC$40,000 aggregate cap.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Parcel exactly at the size limit | Meets it ("not more than"); one square foot more does not | [Act 10 of 2026, s.3](https://npc.govt.lc/laws/download/UjVlcXRvZTd3RG93ODVaQ0tsbWNwY3BZUU5uNEVJM3lpam1HV0lqRS9SRUNzTmp6YisvZFBmQTR2RUw1MFprRHJYRytQRkJMOUo0c0tWQ0YwY2ZoUzJNRUNWSVhnWjEvSll1MW9DSnBIUndsMTNkTDFVOWN0UHpZRk9XZmxhdWg=) |
| Deed registered 1 May 2026 | Fails the registration date | same |
| Buyer previously held a joint interest in a house plot | Not a first-time landowner | same |
| Same interest also claimed as owner-occupied mortgage interest | Do not claim twice without a legal basis | [lc-personal-tax-deductions](lc-personal-tax-deductions.md) |
| Joint purchasers, refinancing, mixed-use loans, interest before registration | Not settled by s.59D; refer | not covered |

## Worked cases

### Case 1: eligible purchase

A resident first-time buyer registers the deed for a 20,000 sq ft plot on 10 May 2026 and pays EC$12,000 of loan interest in 2026. The deduction is 6,000, outside the cap, so a resident already at the EC$40,000 cap can deduct 46,000 in total. It reduces chargeable income by 6,000; it is not a 6,000 tax credit.

```oa-check
name: Saint Lucia s.59D deduction on 12,000 of interest
inputs:
  interest: 12000
steps:
  - deduction: interest * 0.50
  - outside_cap_total: deduction + 40000
expected:
  deduction: 6000
  outside_cap_total: 46000
```

### Case 2 (decision): which spouse should take the loan?

A couple buys their first plot. Spouse A has never held residential land; spouse B jointly owned a house plot before. Only a loan taken by A can qualify, since B fails s.59D(3)(a). On EC$18,000 of interest a year, A's loan gives a deduction of 9,000 and B's gives none. The loan must really be A's and used for the purchase.

```oa-check
name: Saint Lucia s.59D, eligible against ineligible borrower
inputs:
  interest: 18000
steps:
  - deduction_a: interest * 0.50
  - deduction_b: interest * 0
  - difference: deduction_a - deduction_b
expected:
  deduction_a: 9000
  deduction_b: 0
  difference: 9000
```

## When to refuse or refer

- Joint borrowers, refinanced or mixed-use loans, interest paid before registration.
- Taxpayers with too little assessable income to use the deduction.
- Property transfer tax and land registration charges.

## Filing and payment

1. Claim the deduction on the 2026 individual return.
2. Keep the registered deed, survey, prior-title evidence, loan agreement, trace of the loan to the purchase and the lender's interest statement.
3. Record residential intent and residence evidence.

## Completion checklist

- Resident, first-time, 22,000 sq ft or less, deed from 2 May 2026.
- Only interest paid in the year; 50% taken; outside the cap.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment) (No. 2) Act 10 of 2026: read for s.3 inserting s.59D, s.4 company return extension, s.5 penalty rate 6%, and the assent date | https://npc.govt.lc/laws/download/UjVlcXRvZTd3RG93ODVaQ0tsbWNwY3BZUU5uNEVJM3lpam1HV0lqRS9SRUNzTmp6YisvZFBmQTR2RUw1MFprRHJYRytQRkJMOUo0c0tWQ0YwY2ZoUzJNRUNWSVhnWjEvSll1MW9DSnBIUndsMTNkTDFVOWN0UHpZRk9XZmxhdWg= | 2026-11-14 |

Not yet confirmed: the base of the s.134(1) penalty for failure to pay tax by the due date (only its title was read, in the Act's contents); any Ministerial order under s.134(1); the treatment of joint purchasers.
