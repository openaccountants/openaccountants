---
name: how-to-account-for-rental-income-in-malta
description: "Working method for an accountant deciding how a landlord with Malta rental income is taxed for basis year 2026: the optional 15% final tax on gross rent under article 31D of the Income Tax Act (residential from 2014, commercial from 2016, commercial lets to or from a related company excluded), paid with form TA24 by 30 April of the following year, against declaring net rent in the tax return at normal rates by 30 June. Covers the annual all-or-nothing election, the limited deductions on the return route (interest, ground rent, licence fees, 20% further deduction), the Housing Authority long-lease rebate, late TA24 interest and undeclared rent. Trigger on: rental income Malta, 15% rent tax, TA24, landlord tax Malta, Housing Authority lease rebate."
jurisdiction: MT
category: international
tax_year: 2026
last_updated: 2026-11-08
version: 1.3
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# How to Account for Rental Income in Malta v1.3

Tax year 2026: rent received in basis year 2026 is reported by 30 April 2027 (TA24) or 30 June 2027 (tax return). The full computation, worked examples and short-let VAT points are in `mt-rental-income`.

## METHOD

### [method:scope_gate] Who this skill is for, and who to refuse

This skill covers a landlord with Malta **rental income** from residential or commercial property choosing whether to pay the flat 15% final tax on gross rent or add the net rent to their income at normal rates. The 15% option covers residential property (from 1 January 2014) and commercial property (from 1 January 2016), for residents and non-residents, individuals and companies. It is NOT for: commercial rent to or from a related body of persons (the 15% option does not apply to it); foreign-situs property; property held through a trust or other structure; or a mixed accommodation/services business whose receipts cannot yet be separated into rent and other services. Refer the classification of those receipts. Trading classification alone does not remove the article 31D option for rental receipts: MTCA’s specific guidance allows it under both article 4(1)(a) and article 4(1)(e). For a residential long let, check registration with the Housing Authority (Private Residential Leases Act, Cap. 604) before you file. The long-lease rebate depends on it. The lessor must register the lease "within thirty (30) days of the commencement of the lease", a later registration carries an additional fee, and an unregistered private residential lease contract is "null and void" ([Cap. 604 art. 4(1), (2)](https://legislation.mt/eli/cap/604/eng/pdf)). Cap. 604 does not apply to "tenements let to any tourist, exclusively for tourism purposes" (art. 3(2)(b)), so a licensed holiday let has no Housing Authority registration duty. It still applies to licensed holiday premises let to someone who is not a tourist.

### [method:sequence] Order of operations

1. For a residential long let, confirm the lease is registered with the Housing Authority under Cap. 604. Lets to tourists exclusively for tourism are outside Cap. 604.
2. Confirm residential vs commercial, long-let vs short-stay, and, for a commercial let, that the tenant is not a related body of persons.
3. Confirm legal ownership and each owner's share.
4. Only then model the two routes: 15% final tax on gross vs normal rates on net rent with the permitted deductions.
5. Select the route, record why, and file.

Never compute the flat rate first. Clients anchor on the low number. If a commercial tenant turns out to be related, the 15% is not available and the whole computation collapses. If the activity turns out to be a trade, the 15% stays available, but the return-route computation changes to trading rules (expenses wholly and exclusively incurred, not the 20% rule).

### [method:intake_questions] Five questions before computing

- Residential or commercial? (both qualify for 15%, from 2014 and 2016)
- Long-let or short-stay? (short-stay is usually trading income under article 4(1)(a); that changes the return route, not whether the 15% is available)
- For a commercial let: is the tenant a related body of persons? (a company owned or controlled more than 25% by the landlord, or by the same persons; the 15% option is then not available for that commercial rent. The statutory exclusion sits only in the commercial limb of article 31D(8)(a))
- Is a residential lease registered with the Housing Authority, and for how long was it agreed? (2 years or more gives the rebate)
- Sole or joint ownership? (each owner reports their own share; the rebate is split by share)

### [method:evidence] Documents to insist on

- Lease agreement and, for residential lets, Housing Authority registration confirmation.
- Ownership deed / evidence of share.
- Bank statements showing rent received.
Under the 15% route, expenses are irrelevant (tax is on gross), so take the client's word on costs. The moment the client wants the return route, every deduction needs a file-grade document: loan interest certificates, ground rent receipts, licence fee receipts.

### [method:judgment_rule] Choosing the route

Model both. The 15%-on-gross route wins on low-geared property for a landlord whose marginal rate is above 15%. The return route wins where there is large loan interest on the property or a low marginal rate. On the return route for investment rent (article 4(1)(e)), MTCA limits deductions to: interest on the loan that produces the rent; ground rent or similar burden; the licence fee paid to the MTA under the Malta Travel and Tourism Services Act, Cap. 409 (formerly the Guest Houses and Holiday Furnished Premises Act); and a further deduction of 20% of the rent left after ground rent and licence fees. The 20% covers everything else; repairs and agent fees are not deducted on top. These deductions are in [S.L. 123.26 rule 3](https://legislation.mt/eli/sl/123.26/eng/pdf) (L.N. 100 of 1993). Rule 3 still refers to income under article 4(1)(f), which was "Repealed by Act XX of 1996"; rent is now charged under article 4(1)(e). MTCA's rental manual still applies the 20% to that rent, so follow it, and note that the rule's own cross-reference is out of date. Rent that is trading income under article 4(1)(a) is computed under the trading rules instead. Record both computations, the delta, the chosen route, and the client's reason in the working paper. The election is made annually and covers all the person's qualifying rent for that year: you cannot put part of the rent at 15% and part in the return.

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

Cleaning, linen and guest turnover require a facts-based review of the activity and its receipts. If the letting constitutes a trade, that does not itself exclude the 15% article 31D option on rental receipts: MTCA’s Guidance Note paragraph (b) includes both article 4(1)(a) trading rent and article 4(1)(e) investment rent. Separate non-rental service receipts and check VAT and MTA licensing independently; do not treat the rent election as resolving those questions.

**Short lets (MTA-licensed holiday lets).** An MTA-licensed host can choose the 15% on the gross rent. [Article 31D(1)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) applies "where, during a relevant year, any person rents a tenement", and article 31D(2) sets the tax "at the option of the person ... at the rate of fifteen cents (0.15) on every euro of the gross rental income received". A tenement includes "a dwelling house or part thereof which is to be occupied or is occupied as a home or residence by the occupier" (article 31D(8)(a)(i)). Nothing in article 31D excludes tourist or licensed lets. [MTCA's Guidance Note on article 31D](https://mtca.gov.mt/docs/default-source/documents/mtca-guidance-note-art31d.pdf), paragraph (b): "The final tax rate of 15% can be applied both on receipts of rental income that are chargeable to tax either under Article 4(1)(a) of the Income Tax Act or Article 4(1)(e) of the Income Tax Act." When the 15% is not chosen, short lets are usually trading income under article 4(1)(a). [MTCA's rental manual](https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf) says "short lets are considered as trading in nature and are taxable under Article 4(1)(a) ITA". They go in Section 2 of the return ("This includes short letting of holiday accommodation which is subject to MTA license requirements"), with expenses "wholly and exclusively incurred in the production of the rental income" deducted, not the S.L. 123.26 20% rule. Two limits: only rent qualifies for the 15%, so separately priced services (cleaning, breakfast, transfers) are not rent; and MTCA's reading of the dwelling limb for tourist stays is administrative guidance, not law.

### [method:filing_mechanics] How submission works

On the 15% route, form TA24 is submitted together with the payment by 30 April of the year following the year the rent was received. Individual residents use the online TA24 service; non-residents, companies and other entities use a separate online route. An individual who pays the 15% does not declare that rent in the tax return. A late TA24 is still accepted online. Interest runs at 0.6% "for every month or part thereof" during which the tax is unpaid, capped at the tax ([ITMA art. 44(2A)](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b)). The Housing Authority long-lease rebate is claimed through the online TA24. On the return route, the net rent goes into the individual's tax return, due with payment by 30 June of the following year. For 2025 rent (year of assessment 2026), MTCA extended the return and payment to 31 July 2026 ([MTCA notice, 3 June 2026](https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline)).

### [method:handback_protocol] Working paper contents

Both computations (15% vs return route), the route chosen and the reason, proof of Cap. 604 registration and lease length for any rebate, and the TA24 or tax return reference.

## FACT CORRECTIONS

**FACT CORRECTIONS**  _(MTCA "Rental Income Taxed at 15% - Article 31D" FAQ; MTCA Manual on the Taxation of Rental Income; MTCA Tax Return Cycle)_

| fact_key | current | correct | source |
| --- | --- | --- | --- |
| rate | (withheld) | 15% final tax on gross rent, no set-off or refund, optional, chosen yearly, and covering all qualifying rent of the year | ITA art. 31D(2), (4); MTCA art. 31D FAQ, Q13 |
| scope | residential only | Residential (dwelling or garage) from 1 January 2014; commercial tenements and clubs from 2016, but not when rented to or from a related body of persons (more than 25% common ownership or control); residents and non-residents; individuals and companies | ITA art. 31D(8)(a); Act XV of 2016, art. 19; MTCA art. 31D FAQ, Q1, Q3, Q4, Q7 |
| deadline_15 | (withheld) | Form TA24 with payment by 30 April of the following year | MTCA art. 31D FAQ, Q10 |
| late_ta24 | election lost | Late TA24 accepted online; interest at 0.6% for every month or part of a month, capped at the tax | MTCA Manual, Penalties; ITMA art. 44(2A) |
| return_route | progressive with deductions | Investment rent: normal rates on rent less interest, ground rent, licence fees and a 20% further deduction (S.L. 123.26 rule 3, as MTCA applies it to article 4(1)(e) rent); trading rent under article 4(1)(a): expenses wholly and exclusively incurred. Return and payment by 30 June; for 2025 rent, extended to 31 July 2026 | MTCA Manual; S.L. 123.26; MTCA Tax Return Cycle; MTCA notice of 3 June 2026 |
| undeclared | (none) | Undeclared rent found on enquiry: 35% on gross rent plus interest and additional tax; no later 15% option | ITA art. 31D(5); MTCA art. 31D FAQ, Q11. FAQ Q8 and the MTCA manual say progressive rates for individuals; the statute's 35% controls |
| ha_rebate | (none) | 15% payers with a residential lease registered with the Housing Authority for 2 years or more: rebate of EUR 200 / 300 / 400 (2 to under 3 years) or EUR 300 / 400 / 500 (3 years or more) for 1 / 2 / 3+ bedrooms, pro rata, capped at 15% of the year's rent | MTCA Manual, Table 2 |

## FLAGS

- [refer] VAT registration threshold and treatment for short-stay lettings: escalate; out of scope for this skill. See `mt-rental-income`.
- [unsettled] Boundary between a large short-let and a "trade" is judgment-based; do not finalise a borderline case without specialist review.
- [unsettled] MTCA's FAQ states the related-party exclusion without limiting it to commercial lets; the statute places it only in the commercial limb. A residential let to a related company: follow the statute, and confirm with MTCA before relying on it in a filing.

## NOTES

The 15% option is in article 31D of the Income Tax Act (Cap. 123). Undeclared rent is the biggest exposure: it loses the option and is taxed at 35% on gross. Check every year that all qualifying rent sits on one route.

Commercial start date: Act XV of 2016, art. 19 extended article 31D to commercial tenements with no separate commencement date (assented 15 March 2016), and article 31D applies by calendar year of receipt, so the law supports 2016, as MTCA's FAQ says. The manual's "basis year 2017" is not supported by the Act. Neither affects 2026.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 123, art. 31D | https://legislation.mt/eli/cap/123/eng | 2026-10-23 |
| Act XV of 2016 (Budget Measures Implementation Act 2016), art. 19 | https://legislation.mt/eli/act/2016/15/eng | 2026-10-23 |
| MTCA, Rental Income Taxed at 15% - Article 31D FAQ | https://mtca.gov.mt/personal-tax/legal-and-technical/faqs/rental-income-taxed-at-15----article-31d-of-the-income-tax-act | 2026-10-23 |
| MTCA, Manual on the Taxation of Rental Income (deductions, late TA24, Housing Authority rebate) | https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf | 2026-10-23 |
| MTCA, Tax on Rental Income (TA24) | https://mtca.gov.mt/personal-tax/individual/tax-on-rental-income-(ta24) | 2026-10-23 |
| MTCA, Tax Return Cycle (30 June, 0.6% per month) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-10-23 |

Not yet confirmed:
- The long-lease rebate comes from the rebate rules as quoted in the MTCA manual; those rules were not re-read.
- Budget 2027 is presented on 26 October 2026; any change to the 15% rent regime for 2027 is not reflected here.

## Targeted hypothetical checks

A trading landlord with EUR 24,000 of qualifying rent elects article 31D; trading status alone does not deny the election. A separate EUR 3,000 service receipt is not assumed to qualify. These cases assume the statutory tenement and unrelated-commercial conditions are met.

```oa-check
name: Trading rental receipts: article 31D election
inputs:
  rent: 24000
steps:
  - tax: pct(rent,15)
expected:
  tax: 3600
```

For EUR 24,000 rent and EUR 3,000 separately identified services, the rent-only illustration does not apply the final rate to the services. The services’ tax is outside this calculation.

```oa-check
name: Separate services are not silently added to rent election
inputs:
  rent: 24000
  services: 3000
steps:
  - tax_on_rent: pct(rent,15)
  - unsupported_combined_tax: pct(rent + services,15)
  - difference: unsupported_combined_tax - tax_on_rent
expected:
  tax_on_rent: 3600
  unsupported_combined_tax: 4050
  difference: 450
```


### Targeted audit source checks, 4 November 2026

Corrected the trading-rent exclusion only; immigration, tourism licensing, VAT and service-income classification remain separate gates. This is a source-cited draft; the targeted corrections do not certify every unchanged rule.

- MTCA Article 31D Guidance Note paragraph (b): https://mtca.gov.mt/docs/default-source/documents/mtca-guidance-note-art31d.pdf (read 2026-11-04).
- Cap. 123 article 31D(2): https://legislation.mt/eli/cap/123/eng/pdf (read 2026-11-04).

### Targeted audit source checks, 8 November 2026

Stated the short-let position (15% available to an MTA-licensed host; otherwise usually trading income), the Cap. 604 registration rule and its tourism carve-out, the interest rule, the 20% deduction's legal basis, the 2025-rent payment date and the undeclared-rent citation. This is a source-cited draft; the targeted corrections do not certify every unchanged rule.

- [Cap. 123 article 31D(1), (2), (5), (8)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) (read 2026-11-08).
- [Cap. 604 articles 3(2)(b), 4(1), 4(2)](https://legislation.mt/eli/cap/604/eng/pdf) (read 2026-11-08).
- [Cap. 372 article 44(2A)](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b) (read 2026-11-08).
- [S.L. 123.26 rule 3](https://legislation.mt/eli/sl/123.26/eng/pdf) (read 2026-11-08).
- MTCA Guidance Note on article 31D and MTCA rental manual (read 2026-11-08 in a browser).
