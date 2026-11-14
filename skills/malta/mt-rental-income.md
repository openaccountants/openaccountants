---
name: mt-rental-income
description: 'Use this skill whenever asked about Malta rental income tax for basis year 2026. Trigger on phrases like rental income Malta, letting property Malta, 15% final tax on rent, Article 31D, TA24, kiri, landlord tax Malta, Airbnb Malta tax, short let Malta, non-resident landlord Malta, Housing Authority lease rebate, or any question about computing, filing or choosing the route for tax on rent from Maltese immovable property. Covers the optional 15% final tax on gross rent (residential from 2014, commercial from 2016, commercial lets to or from a related body of persons excluded), the return route with the S.L. 123.26 deductions (interest, ground rent, licence fees and the 20% further deduction), the Housing Authority rates of 5% and 10%, the long-lease rebate, short lets, VAT on lettings, the 35% charge on undeclared rent, TA24 by 30 April and the return by 30 June. Read it before any Malta rental income work.'
version: "2.0"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - malta-income-tax
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Malta rental income: the 15% final tax or the tax return, basis year 2026

## Scope

This skill decides and computes how a landlord is taxed in Malta on rent from immovable property for **basis year 2026** (rent received in calendar 2026; year of assessment 2027). It covers individuals and companies, residents and non-residents, residential and commercial lets, long lets and MTA-licensed short lets.

Two routes exist for rent from a qualifying tenement:

1. **The 15% final tax on gross rent** (Income Tax Act, Cap. 123, art. 31D). Optional, chosen each year, covering all qualifying rent of that year, paid with form TA24 by 30 April 2027.
2. **The tax return route.** Net rent is added to chargeable income and taxed at the person's normal rates. The individual rate tables live in [malta-income-tax](malta-income-tax.md) and are not restated here.

Out of scope, linked instead: selling the property ([mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md)), provisional tax on rent declared in the return ([mt-estimated-tax](mt-estimated-tax.md)), VAT returns ([malta-vat-return](malta-vat-return.md)), foreign property and trusts (refer).

This file absorbed `how-to-account-for-rental-income-in-malta` on 14 November 2026: the order of work, the intake questions, the working paper and the traps from that file are below.

Built from the law: not yet approved by an accountant. Working paper only.

## Ask the client first

1. **What is let?** A dwelling or garage (art. 31D(8)(a)(i)), or a commercial tenement or club under Civil Code art. 1525 (art. 31D(8)(a)(ii))? Any ground rent received from an emphyteutical concession?
2. **For a commercial tenement or club: is it let to or from a related body of persons?** A body of persons is related to an individual if that individual owns or controls more than 25% of it, directly or indirectly; two bodies are related if the same persons own or control more than 25% of each. If yes, the 15% is not available for that let.
3. **Long let or short let?** Is the letting licensed by the MTA under the Malta Travel and Tourism Services Act, Cap. 409? Are services (cleaning, breakfast, transfers) priced separately?
4. **For a residential long let: is the lease registered with the Housing Authority under Cap. 604, for what original duration, and how many bedrooms does the contract state?** Is the property let to the Housing Authority itself, or to a tenant on a Housing Authority subsidy or scheme?
5. **Who owns it and in what shares?** Each owner reports their own share; a rebate is split by share.
6. **Other income and status** (single, married, parent; resident or not), to find the marginal rate on the return route. **Loan interest, ground rent paid and MTA licence fees** for each property.

## The method, step by step

1. **Registration first.** For a residential long let, confirm the lease is registered with the Housing Authority. The lessor registers it "within thirty (30) days of the commencement of the lease"; an unregistered private residential lease contract is "null and void" ([Cap. 604 art. 4](https://legislation.mt/eli/cap/604/eng/pdf)). Cap. 604 does not apply to tenements let to tourists exclusively for tourism purposes (art. 3(2)(b)), so a licensed holiday let has no Housing Authority registration duty; it still applies to licensed premises let to someone who is not a tourist.
2. **Classify the tenement** (residential or commercial) and, for a commercial let, test the related-party bar. The bar sits only in the commercial limb, art. 31D(8)(a)(ii); a dwelling or garage qualifies whoever the tenant is.
3. **Check the special Housing Authority rates** before art. 31D: rent from a lease to the Housing Authority for at least ten years is taxed at 5% final, deducted by the Authority (art. 31A); rent from a tenant on a Housing Authority rent subsidy, owner registered, at 10% final (art. 31B); rent to the same person for more than seven years under a Housing Authority scheme, owner registered, at 5% final (art. 31E). Restored scheduled or urban-conservation-area property under a MEPA scheme: 10% residential, 15% commercial, final, remitted by 30 June of the following year (art. 31C).
4. **Confirm ownership and shares.**
5. **Model both routes.** Never present the 15% first: clients anchor on the low number.
   - 15% route: tax = 15% x gross rent received in the year, final, "no set-off or refund" (art. 31D(2)). For a registered long private residential lease of two years or more, deduct the S.L. 123.201 rebate.
   - Return route, investment rent (art. 4(1)(e)): gross rent less interest on the loan for that property, less ground rent or similar burden, less MTA licence fees, less a further 20% of what remains after ground rent and licence fees (S.L. 123.26 rule 3). The 20% replaces every other expense. Each property is a separate source: a property whose deductions exceed its rent gives nil, and the loss is not set against other property, other income or later years (MTCA rental manual).
   - Return route, trading rent (art. 4(1)(a), including most MTA-licensed short lets): expenses wholly and exclusively incurred, declared in Section 2 of the return. The 20% rule does not apply.
   - Compare the extra tax the net rent causes at the marginal rate with the 15% of gross. Choose for **all** qualifying rent of the year: the option, once exercised, "shall apply to the total rental income received in the said year from all the tenements" (art. 31D(4)).
6. **Record** both computations, the difference, the route chosen and the client's reason in the working paper.
7. **File and pay** (see Filing and payment). Check that rent paid through TA24 is not declared again in the return, and reconcile rent credited to the bank to the registered lease value.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Final tax on rent, art. 31D | 15% of gross rental income received | Optional, chosen yearly; final, no set-off or refund; covers all qualifying rent of the year; residents and non-residents, individuals and companies | Cap. 123 art. 31D(2), (4): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Start of the 15% option | Residential 1 January 2014; commercial 1 January 2016 | By calendar year of receipt (art. 31D(8)(b)) | MTCA art. 31D FAQ, Q1 and Q7: https://mtca.gov.mt/personal-tax/legal-and-technical/faqs/rental-income-taxed-at-15----article-31d-of-the-income-tax-act |
| Related body of persons, commercial lets | More than 25% ownership or control | Commercial tenement or club only; the 15% is then not available | Cap. 123 art. 31D(8)(a)(ii): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Undeclared rent found on enquiry | 35% of gross rent, plus interest and additional tax | Whether or not the 15% was exercised; final | same |
| Lease to the Housing Authority, 10 years or more | 5% of gross rent, final, deducted by the Authority | Art. 31A | same |
| Tenant on a Housing Authority rent subsidy | 10% of gross rent, final, deducted by the Authority | Owner registered with the Authority; art. 31B | same |
| Housing Authority scheme, same tenant more than 7 years | 5% of gross rent, final | Owner registered; art. 31E | same |
| Restored scheduled or UCA property, MEPA scheme | 10% residential, 15% commercial, final | Remitted with the forms by 30 June of the following year; art. 31C | same |
| Further deduction, return route | 20% of rent remaining after ground rent and licence fees | Investment rent only; not on income from emphyteutical concessions; replaces all other expenses | S.L. 123.26 rule 3: https://legislation.mt/eli/sl/123.26/eng/pdf |
| Long-lease rebate, 2 to under 3 years | EUR 200 (1 bedroom), EUR 300 (2), EUR 400 (3 or more) | Lease registered as a long private residential lease, original duration; 15% option exercised; pro rata by days in the first and last year; capped at 15% of the year's rent from that lease | S.L. 123.201 rule 5: https://legislation.mt/eli/sl/123.201/eng/pdf |
| Long-lease rebate, 3 years or more | EUR 300 (1 bedroom), EUR 400 (2), EUR 500 (3 or more) | same conditions | same |
| TA24 with payment | 30 April of the year after the year of receipt | 15% route; 30 April 2027 for 2026 rent | MTCA art. 31D FAQ, Q10: https://mtca.gov.mt/personal-tax/legal-and-technical/faqs/rental-income-taxed-at-15----article-31d-of-the-income-tax-act |
| Tax return and tax settlement date | 30 June of the following year; online return by 31 July | Return route | MTCA Tax Return Cycle: https://mtca.gov.mt/personal-tax/individual/tax-return-cycle |
| Interest on late tax | 0.6% for every month or part of a month, capped at the tax | Tax payable on or after 31 August 2022 | Cap. 372 art. 44(2A): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| VAT on licensed tourist accommodation | 7% | Article 10 registered supplier; where the price includes other goods or services, 80% of the price is accommodation and 20% the other supplies | Cap. 406 Eighth Schedule item 1: https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 |
| Records | At least nine years | Anyone carrying on a trade, business, profession or vocation; gives way to Companies Act art. 163(5) | Cap. 372 art. 19(5): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |

### What counts as rent

- "Rents" include ground rents, urban or rural (art. 31D(8)(c)). MTCA's guidance note lets the 15% apply to ground rent from an emphyteutical concession of a residential or commercial tenement (note para. (a)).
- Premiums paid in the same way as the rent they relate to may go to the 15% in the year received, or into the return (MTCA rental manual). Key money (*rigal*), recognition fees (*lawdemju*) and ground rent (*cens*) are "other profits arising from property" under art. 4(1)(e).
- Recharges of common costs are not rent for art. 31D (note para. (d)). A refundable security deposit is not income unless forfeited.
- Platform payouts: the base is the rent before the platform's fee, net of any VAT collected (method carried from earlier versions; see Not yet confirmed).
- A person who would have claimed wear and tear and opts for the 15% is deemed to have claimed it, for a later balancing charge under art. 24 (note para. (e)).
- A company allocates distributable profits from 15% rent to its final tax account (art. 31D(6)), and declares the rent in its company return (MTCA rental manual).

### Short lets

An MTA-licensed host can choose the 15% on gross rent. Art. 31D(1) applies "where, during a relevant year, any person rents a tenement", and a tenement includes "a dwelling house or part thereof which is to be occupied or is occupied as a home or residence by the occupier" (art. 31D(8)(a)(i)); nothing in art. 31D excludes tourist lets. MTCA's guidance note para. (b): "The final tax rate of 15% can be applied both on receipts of rental income that are chargeable to tax either under Article 4(1)(a) of the Income Tax Act or Article 4(1)(e) of the Income Tax Act." Without the 15%, MTCA treats short lets as trading: Section 2 of the return, "This includes short letting of holiday accommodation which is subject to MTA license requirements", with expenses wholly and exclusively incurred. Two limits: only rent qualifies, so separately priced services are not rent; and MTCA's reading of the dwelling limb for tourist stays is administrative guidance.

A licence is needed to "provide accommodation in a house to tourists" (Cap. 409 art. 18(2)); a tourist is a person staying outside their usual environment "for not more than one consecutive year" (art. 2). There is no 30-day test in the licensing law; the 30-day figure is a VAT rule.

## Boundary and exception table

| Situation | Treatment | Why |
|---|---|---|
| Office let to a company the landlord owns 60% of | 15% not available; return route | Commercial tenement, related body (art. 31D(8)(a)(ii)) |
| Flat or garage let to the landlord's own company | 15% available | The related-party bar sits only in the commercial limb; MTCA's FAQ states it without that limit, so confirm with MTCA before filing |
| Two flats: one on 15%, one in the return, same year | Not allowed | Art. 31D(4): the option covers all qualifying rent of the year |
| 15% one year, return the next | Allowed | Chosen annually (MTCA FAQ Q13); 15% paid cannot be claimed back (Q12) |
| Repairs, agent fees, insurance claimed with the 15% | Not deductible | Tax on gross (art. 31D(2)) |
| Repairs claimed on top of the 20% | Not deductible | The 20% covers all other expenses (S.L. 123.26 rule 3; MTCA manual) |
| Loss on one property in the return | Nil for that property, no carry-forward | MTCA rental manual |
| Rent never declared, found on enquiry | 35% of gross plus interest and additional tax | Art. 31D(5); MTCA FAQ Q8 says normal rates for individuals, the statute controls |
| Trading short let | 15% still available on the rent | MTCA guidance note para. (b) |
| Mixed accommodation and services, receipts not separable | Refer | Only rent qualifies |
| Lease registered for 2 years and renewed for 2 more | Rebate band by the original duration only | S.L. 123.201 rule 4 |
| Spouses filing separately under art. 49A | Each may still use the 15% | MTCA rental manual |
| Non-resident landlord | 15% available; or the return at non-resident rates with the S.L. 123.26 deductions | MTCA FAQ Q3; MTCA rental manual |

### VAT on lettings ([Cap. 406 Fifth Schedule Part Two item 1](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4))

| Letting | VAT |
|---|---|
| Letting of immovable property generally | Exempt without credit |
| Accommodation that must be licensed under Cap. 409, or in a holiday camp or camping site | Taxable; 7% for an Article 10 supplier |
| Designated vehicle parking premises or sites | Taxable |
| Permanently installed equipment and machinery; hire of safes | Taxable |
| Letting by a limited liability company to an Article 10 person for that person's economic activity | Taxable |
| Letting for not more than thirty days by a taxable person in the course of an economic activity | Taxable, except: the cases above, space for artistic and cultural activities, habitation premises not needing a Cap. 409 licence, garages and stores, and poker rooms |

VAT collected is not rent. Registration under Article 10 or 11 depends on turnover: see [malta-vat-return](malta-vat-return.md).

### Defaults when a fact is missing

| Missing fact | Default |
|---|---|
| Route not chosen | Stop and ask; compute both |
| Commercial tenant, relationship unknown | Treat as related (15% blocked) |
| Residential or commercial unknown | Stop and ask |
| Residence of the landlord unknown | Stop and ask |
| Short or long let unknown | Stop: VAT and the return section depend on it |
| Furnished or not | No effect on either route |

### Red flags

- Software that nets expenses before applying the 15%.
- Rent split between TA24 and the return in one year.
- Short lets treated as passive rent, with the VAT and eco-contribution questions missed.
- A residential lease not registered with the Housing Authority: the contract may be void and no rebate is due.
- A rebate claimed that was not due is repayable with interest from 1 May of the year of assessment (S.L. 123.201 rule 9).

## Worked cases

All taxpayers are invented; rates are the 2026 law.

### Case 1: which route, single landlord with a salary (a decision)

A single resident earns chargeable income of EUR 30,000 from salary, in the 25% band of the 2026 single table ([malta-income-tax](malta-income-tax.md); [MTCA 2026 rates](https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026): 25% less EUR 3,400 from EUR 16,001 to EUR 60,000). She receives EUR 12,000 rent in 2026 from one flat. With a loan, interest is EUR 3,000; without one, nil. No ground rent or licence fee.

With the loan: 20% further deduction EUR 2,400, net rent EUR 6,600, extra tax at 25% EUR 1,650 against EUR 1,800 on the 15%. The return is cheaper by EUR 150. Without the loan: net rent EUR 9,600, extra tax EUR 2,400, so the 15% is cheaper by EUR 600. The loan interest decides it.

```oa-check
name: Rent EUR 12,000, single at 25 percent, 15 percent versus return, with and without loan interest (2026)
inputs:
  salary: 30000
  gross_rent: 12000
  interest_loan: 3000
  ground_rent: 0
steps:
  - further: pct(gross_rent - ground_rent, 20)
  - net_loan: max(0, gross_rent - interest_loan - ground_rent - further)
  - extra_loan: (salary + net_loan) * 0.25 - 3400 - (salary * 0.25 - 3400)
  - net_noloan: max(0, gross_rent - ground_rent - further)
  - extra_noloan: (salary + net_noloan) * 0.25 - 3400 - (salary * 0.25 - 3400)
  - final_tax: pct(gross_rent, 15)
  - return_saves_with_loan: final_tax - extra_loan
  - final_saves_without_loan: extra_noloan - final_tax
expected:
  further: 2400.00
  net_loan: 6600.00
  extra_loan: 1650.00
  net_noloan: 9600.00
  extra_noloan: 2400.00
  final_tax: 1800.00
  return_saves_with_loan: 150.00
  final_saves_without_loan: 600.00
```

### Case 2: 15% with the long-lease rebate, lease starting in the year

A two-bedroom flat is let from 1 April 2026 on a three-year lease registered with the Housing Authority, at EUR 800 a month. Rent received in 2026 is EUR 7,200; the lease runs 275 days of 2026. The owner opts for the 15%. Rebate: EUR 400 x 275 / 365 = EUR 301.37, below the cap of 15% of the year's rent (EUR 1,080). Tax payable with the TA24 by 30 April 2027: EUR 778.63.

```oa-check
name: Article 31D with S.L. 123.201 rebate, 2 bedrooms, 3-year lease from 1 April 2026
inputs:
  rent_received: 7200
  full_rebate: 400
  days_in_force: 275
  days_in_year: 365
steps:
  - tax_15: pct(rent_received, 15)
  - rebate_prorata: round(full_rebate * days_in_force / days_in_year, 2)
  - rebate_cap: pct(rent_received, 15)
  - rebate: min(rebate_prorata, rebate_cap)
  - tax_payable: tax_15 - rebate
expected:
  tax_15: 1080.00
  rebate_prorata: 301.37
  rebate: 301.37
  tax_payable: 778.63
```

### Further cases (prose)

- **Non-resident, 15%.** A UK resident receives EUR 18,000 rent from a flat in Sliema: 15% is EUR 2,700 via the non-resident TA24 route. The treaty credit in the UK is for the UK adviser.
- **Licensed short let with VAT.** Gross bookings before the platform fee EUR 20,619, VAT at 7% included: VAT 7/107 = EUR 1,349; rent EUR 19,270; 15% = EUR 2,891 (whole euros). The platform fee is not deducted.
- **Related commercial let.** Office let for EUR 6,000 to a company the landlord owns 60% of: 15% blocked; return route net rent EUR 4,800 after the 20%; at 25%, EUR 1,200 extra tax.
- **MTCA's own example.** Gross rent EUR 400, ground rent payable EUR 40: 20% of EUR 360 is EUR 72; net EUR 288 (boxes 11a, 16a and 16b).

## When to refuse or refer

| Code | Trigger | Action |
|---|---|---|
| R-MTR-1 | Route not chosen by the client | Compute both and stop for the client's choice |
| R-MTR-2 | Commercial tenement or club, related body of persons | Return route only; confirm the relationship first |
| R-MTR-3 | Sale or transfer of the property | Use [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md) |
| R-MTR-4 | Trusts, nominees, foreign holding structures, foreign-situs property | Refer to a warranted accountant |
| R-MTR-5 | Part of the year's rent on 15% and part in the return | Refuse; one route for all qualifying rent |
| R-MTR-6 | Accommodation and services that cannot be separated; borderline trade | Refer for a facts-based review |
| R-MTR-7 | Residential let to a related company relying on the statute against the FAQ | Confirm with MTCA before filing |

## Filing and payment

**15% route.** Form TA24 with payment by 30 April of the year after receipt (30 April 2027 for 2026 rent). Individual Malta tax residents file on [myTax](https://mytax.mtca.gov.mt/) with e-ID; individual non-residents, companies and other entities use the [TA24 online form](https://irdpubserv.gov.mt/TA24/Form.aspx) (MTCA TA24 page). The long-lease rebate is claimed on the online TA24, submitted with the payment (S.L. 123.201 rule 6). A manual TA24 can be paid in cash at Malta Post with the completed form; Malta Post does not accept late payments (MTCA rental manual). An individual paying the 15% does not declare that rent in the return (art. 31D(3)). Late tax carries 0.6% interest a month or part, capped at the tax (Cap. 372 art. 44(2A)).

**Return route.** Investment rent: gross rents in box 11a, ground rents received in box 11b, deductions in section 16 (16a ground rent payable, 16b the 20%); deductions per property cannot exceed that property's rent. Trading rent: Section 2. Tax settlement date 30 June 2027; online return by 31 July 2027 (MTCA Tax Return Cycle). Provisional tax may apply on rent declared in the return: see [mt-estimated-tax](mt-estimated-tax.md). A correction to a filed return is made on form AF1.

**Working paper:** both computations, the route and the reason, Cap. 604 registration proof and lease length for any rebate, and the TA24 or return reference.

## Completion checklist

- [ ] Housing Authority registration checked for every residential long let.
- [ ] Each property classified; related-party test done for every commercial let.
- [ ] Special Housing Authority and art. 31C rents identified and kept out of art. 31D.
- [ ] Both routes computed; one route for all qualifying rent.
- [ ] Rebate computed by original duration, bedrooms, days and the 15% cap.
- [ ] No 15% rent declared again in an individual's return.
- [ ] VAT status of every short let checked.
- [ ] TA24 by 30 April or return by 30 June; reference filed.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for Cap. 123 arts 31A, 31B, 31C, 31D(1) to (8) and 31E (rates, related party, undeclared rent, final tax account) | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-14 |
| Read for Cap. 372 art. 19(5) (nine-year records) and art. 44(2A) (0.6% interest from 31 August 2022, capped) | https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b | 2026-11-14 |
| Read for S.L. 123.26 rule 3 (interest, ground rent, licence fee, 20% further deduction, emphyteusis exclusion) | https://legislation.mt/eli/sl/123.26/eng/pdf | 2026-11-14 |
| Read for S.L. 123.201 rules 3 to 9 (rebate table, original duration, pro rata, 15% cap, claim on TA24, forfeiture) | https://legislation.mt/eli/sl/123.201/eng/pdf | 2026-11-14 |
| Read for Cap. 604 arts 3(2)(b) and 4 (registration within 30 days, null and void, tourism carve-out) | https://legislation.mt/eli/cap/604/eng/pdf | 2026-11-14 |
| Read for Cap. 409 arts 2 and 18(2) (tourist definition, licence to provide accommodation) | https://legislation.mt/eli/cap/409/eng/pdf | 2026-11-14 |
| Read for Cap. 406 Fifth Schedule Part Two item 1 (letting exemption and its exclusions) and Eighth Schedule item 1 (7% accommodation, 80/20 split) | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | 2026-11-14 |
| Read for MTCA art. 31D FAQ, Q1 to Q13 (start dates, final, non-residents, companies, annual option, 30 April, 35%) | https://mtca.gov.mt/personal-tax/legal-and-technical/faqs/rental-income-taxed-at-15----article-31d-of-the-income-tax-act | 2026-11-14 |
| Read for MTCA Guidance Note on art. 31D, paras (a) to (e) | https://mtca.gov.mt/docs/default-source/documents/mtca-guidance-note-art31d.pdf | 2026-11-14 |
| Read for MTCA Manual on the Taxation of Rental Income (deductions, per-property nil rule, return boxes, short lets in Section 2, rebate, Malta Post, premiums) | https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf | 2026-11-14 |
| Read for MTCA TA24 page (myTax for residents, separate online form for non-residents and companies) | https://mtca.gov.mt/personal-tax/individual/tax-on-rental-income-(ta24) | 2026-11-14 |
| Read for MTCA Tax Return Cycle (30 June settlement date, 31 July online return, 0.6% interest, AF1) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-11-14 |
| Read for MTCA Tax Rates 2026, single table (25% less EUR 3,400 band used in Case 1) | https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 | 2026-11-14 |

Not yet confirmed: whether MTCA has extended the 2027 return or payment date for 2026 rent (the 3 June 2026 extension to 31 July 2026 was for 2025 rent and was not re-read); treating platform fees as not deductible from the 15% base; MTCA's wider reading of "tenement" (land, roof tops, note para. (c)) against the art. 31D(8)(a) definition; the manual's line that gross rent under the 15% is "declared by end of June", against FAQ Q5 for individuals; the manual's EUR 9,100 and EUR 10,500 separate-return thresholds, which are older figures and are not used here; the UK treaty position in the non-resident case; any Budget 2027 change for rent received from 2027.
