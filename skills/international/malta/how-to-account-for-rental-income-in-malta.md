---
name: how-to-account-for-rental-income-in-malta
description: "Working method for an accountant deciding how a landlord with Malta rental income is taxed for basis year 2026: the optional 15% final tax on gross rent under article 31D of the Income Tax Act (residential from 2014, commercial from 2016, not rent from related parties), paid with form TA24 by 30 April of the following year, against declaring net rent in the tax return at normal rates by 30 June. Covers the annual all-or-nothing election, the limited deductions on the return route (interest, ground rent, licence fees, 20% further deduction), the Housing Authority long-lease rebate, late TA24 interest and undeclared rent. Trigger on: rental income Malta, 15% rent tax, TA24, landlord tax Malta, Housing Authority lease rebate."
jurisdiction: MT
category: international
tax_year: 2026
last_updated: 2026-10-23
version: 1.1
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# How to Account for Rental Income in Malta v1.1

Built by Michael Cutajar and the OpenAccountants team. **Source-cited draft: not reviewed by an accountant.**

Tax year 2026: rent received in basis year 2026 is reported by 30 April 2027 (TA24) or 30 June 2027 (tax return). The full computation, worked examples and short-let VAT points are in `mt-rental-income`.

## METHOD

### [method:scope_gate] Who this skill is for, and who to refuse

This skill covers a landlord with Malta **rental income** from residential or commercial property choosing whether to pay the flat 15% final tax on gross rent or add the net rent to their income at normal rates. The 15% option covers residential property (from 1 January 2014) and commercial property (from 1 January 2016), for residents and non-residents, individuals and companies. It is NOT for: rent from a related party (the 15% option does not apply); foreign-situs property; property held through a trust or other structure; or short-stay / serviced-apartment operations large enough to constitute a trade. Send those to a specialist. For a residential long let, check registration with the Housing Authority (Private Residential Leases Act, Cap. 604) before you file: the long-lease rebate depends on it, and an unregistered lease is a compliance problem in its own right.

### [method:sequence] Order of operations

1. Confirm the lease is registered with the Housing Authority under Cap. 604 (residential lets).
2. Confirm residential vs commercial, long-let vs short-stay, and that the tenant is not a related party.
3. Confirm legal ownership and each owner's share.
4. Only then model the two routes: 15% final tax on gross vs normal rates on net rent with the permitted deductions.
5. Select the route, record why, and file.

Never compute the flat rate first. Clients anchor on the low number, and if the tenant turns out to be related or the activity is actually a trade, the whole computation collapses and you have wasted the client's trust and your time.

### [method:intake_questions] Five questions before computing

- Residential or commercial? (both qualify for 15%, from 2014 and 2016)
- Long-let or short-stay? (short-stay may be trading income, not passive rent)
- Is the tenant a related party? (a company owned or controlled more than 25% by the landlord counts; the 15% option is then not available)
- Is a residential lease registered with the Housing Authority, and for how long was it agreed? (2 years or more gives the rebate)
- Sole or joint ownership? (each owner reports their own share; the rebate is split by share)

### [method:evidence] Documents to insist on

- Lease agreement and, for residential lets, Housing Authority registration confirmation.
- Ownership deed / evidence of share.
- Bank statements showing rent received.
Under the 15% route, expenses are irrelevant (tax is on gross), so take the client's word on costs. The moment the client wants the return route, every deduction needs a file-grade document: loan interest certificates, ground rent receipts, licence fee receipts.

### [method:judgment_rule] Choosing the route

Model both. The 15%-on-gross route wins on low-geared property for a landlord whose marginal rate is above 15%. The return route wins where there is large loan interest on the property or a low marginal rate. On the return route, deductions are limited to: interest on the loan that produces the rent; ground rent or similar burden; licence fees under the Guest Houses and Holiday Furnished Premises Act; and a further deduction of 20% of the rent left after ground rent and licence fees. The 20% covers everything else; repairs and agent fees are not deducted on top. Record both computations, the delta, the chosen route, and the client's reason in the working paper. The election is made annually and covers all the person's qualifying rent for that year: you cannot put part of the rent at 15% and part in the return.

### [method:trap] Most-missed items

- Clients believe they can deduct home-loan interest, agent fees, and repairs under the 15% route. They cannot. The 15% is on gross, final, with no set-off or refund.
- Software and AI default to netting expenses before applying the 15%. Wrong: the 15% applies to gross.
- On the return route, deducting actual repairs as well as the 20% further deduction. The 20% replaces them.
- Splitting rent between TA24 and the tax return in the same year. Not allowed.
- Short-stay lettings misclassified as passive rent, missing the VAT question entirely.
- Rent never declared cannot later use the 15%. Following an investigation it is taxed at 35% on gross rent plus interest and additional tax (MTCA FAQ Q11).

### [method:cross_check] Reconcile before signing

Rent credited to the bank must match the declared lease. Reconcile declared rent to the registered lease value up front, and check that rent paid through TA24 is not declared again in the tax return.

### [method:edge_case] When side income reshapes the return

A client presenting as a landlord but providing cleaning, linen, and guest turnover is running a trade, not earning passive rent. The whole return changes: business income, likely VAT registration, and no 15% option. Reclassify before computing anything.

### [method:filing_mechanics] How submission works

On the 15% route, form TA24 is submitted together with the payment by 30 April of the year following the year the rent was received. Individual residents use the online TA24 service; non-residents, companies and other entities use a separate online route. An individual who pays the 15% does not declare that rent in the tax return. A late TA24 is still accepted online with interest of 0.6% on the tax due, calculated to the actual submission date (MTCA's general rate for unpaid tax is 0.6% per month). The Housing Authority long-lease rebate is claimed through the online TA24. On the return route, the net rent goes into the individual's tax return, due with payment by 30 June of the following year.

### [method:handback_protocol] Working paper contents

Both computations (15% vs return route), the route chosen and the reason, proof of Cap. 604 registration and lease length for any rebate, and the TA24 or tax return reference.

## FACT CORRECTIONS

**FACT CORRECTIONS**  _(MTCA "Rental Income Taxed at 15% - Article 31D" FAQ; MTCA Manual on the Taxation of Rental Income; MTCA Tax Return Cycle)_

| fact_key | current | correct | source |
| --- | --- | --- | --- |
| rate | (withheld) | 15% final tax on gross rent, no set-off or refund, optional, chosen yearly | MTCA art. 31D FAQ, Q2, Q6, Q13 |
| scope | residential only | Residential from 1 January 2014, commercial from 1 January 2016; not rent from related parties; residents and non-residents; individuals and companies | MTCA art. 31D FAQ, Q1, Q3, Q4, Q7 |
| deadline_15 | (withheld) | Form TA24 with payment by 30 April of the following year | MTCA art. 31D FAQ, Q10 |
| late_ta24 | election lost | Late TA24 accepted online with 0.6% interest on the tax due to the submission date | MTCA Manual, Penalties |
| return_route | progressive with deductions | Normal rates on rent less interest, ground rent, licence fees and a 20% further deduction; return and payment by 30 June | MTCA Manual; MTCA Tax Return Cycle |
| undeclared | (none) | Undeclared rent: 35% on gross rent plus interest and additional tax after investigation; no later 15% option | MTCA art. 31D FAQ, Q8, Q11 |
| ha_rebate | (none) | 15% payers with a residential lease registered with the Housing Authority for 2 years or more: rebate of EUR 200 / 300 / 400 (2 to under 3 years) or EUR 300 / 400 / 500 (3 years or more) for 1 / 2 / 3+ bedrooms, pro rata, capped at 15% of the year's rent | MTCA Manual, Table 2 |

## FLAGS

- [refer] Cap. 604 lease-registration deadline and penalty for non-registration: not confirmed from an official source in this refresh (legislation.mt unavailable on 2026-10-23).
- [refer] VAT registration threshold and treatment for short-stay lettings: escalate; out of scope for this skill. See `mt-rental-income`.
- [unsettled] Boundary between a large short-let and a "trade" is judgment-based; do not finalise a borderline case without specialist review.
- [unsettled] MTCA's FAQ dates the commercial 15% option from 1 January 2016; its manual says basis year 2017. Neither affects 2026.

## NOTES

The 15% option is in article 31D of the Income Tax Act (Cap. 123). Undeclared rent is the biggest exposure: it loses the option and is taxed at 35% on gross. Check every year that all qualifying rent sits on one route.

## Sources

| Source | URL | Read on |
|---|---|---|
| MTCA, Rental Income Taxed at 15% - Article 31D FAQ | https://mtca.gov.mt/personal-tax/legal-and-technical/faqs/rental-income-taxed-at-15----article-31d-of-the-income-tax-act | 2026-10-23 |
| MTCA, Manual on the Taxation of Rental Income (deductions, late TA24, Housing Authority rebate) | https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf | 2026-10-23 |
| MTCA, Tax on Rental Income (TA24) | https://mtca.gov.mt/personal-tax/individual/tax-on-rental-income-(ta24) | 2026-10-23 |
| MTCA, Tax Return Cycle (30 June, 0.6% per month) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-10-23 |

Not yet confirmed:
- Cap. 604 registration deadline and penalty (legislation.mt unavailable).
- The period over which the 0.6% late-TA24 interest runs: the manual gives 0.6% without the period; the general MTCA rate is 0.6% per month.
- Budget 2027 is presented on 26 October 2026; any change to the 15% rent regime for 2027 is not reflected here.

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
