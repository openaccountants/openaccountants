---
name: cyprus-income-tax
description: "Compute Cyprus individual income tax for 2026: residence, progressive bands, contribution caps, family deductions, special income, filing and provisional tax. Includes explicit holds for unproven eligibility and historical cases; use before preparing or reviewing a TD1 return."
version: 0.5
type: computation
jurisdiction: CY
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Cyprus personal income tax (tax year 2026)

Use this Guide to compute an individual's ordinary 2026 income tax and the deductions below. Confirm the tax year, residence, income categories, contribution certificates, family composition and total family income first. Do not use a held outcome to file, elect or determine eligibility.

The reform applies from 1 January 2026. Law 244(I)/2025 commencement is section 23 after the Gazette correction; the delayed securities provision starts in 2031. The 25% returning-resident exemption was enacted separately by Law 17(I)/2026 with effect from 1 January 2025. [Laws 243–245/2025, printed pp.1260–1316](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf); [Gazette correction](https://www.mof.gov.cy/mof/gpo/gazette.nsf/203DBFC78C778160C2258DAB0020F89D/%24file/5075%2027%202%202026%20PARARTIMA%201o%20MEROS%20I.pdf); [Law 17/2026](https://www.mof.gov.cy/mof/tax/taxdep.nsf/All/AFF8B2E8B2A07820C2258DB60033F251/%24file/5076%206%203%202026%20PARARTIMA%201o%20MEROS%20I.pdf?OpenElement=).

## Who this applies to

- Individuals: employees, sole traders, landlords and pensioners. Residents' worldwide income and non-residents' Cyprus-source income require different computations. This Guide's ordinary examples assume resident status and an established ordinary taxable-income base. [Tax Department, return scope](https://www.gov.cy/mof-tax/en/documents/forologiki-dilosi-eisodimatos-atomoy/).
- **183-day test:** more than 183 days in Cyprus in the tax year. Exactly 183 is insufficient under that test. **60-day alternative:** no stay exceeding 183 days in any other single state; at least 60 days in Cyprus; business, employment or office in a Cyprus tax-resident person during the year, without its termination during that year; and a permanent owned or rented home in Cyprus. Another country's tax residence is no longer an additional exclusion. Arrival counts inside, departure outside; arriving and departing on the same day counts inside, departing and returning on the same day outside. [ITL art.2, replaced by Law 244 s.2](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).
- **Filing from 2026:** a resident with gross income within ITL art.5(1), whatever their age; also every resident aged 25 to 70 inclusive on 31 December, even without income. A non-resident with art.5(2) gross income files. A zero-rate tax result is not a filing exemption. The Council of Ministers can exempt categories by decree. [ACL art.5(1), replaced by Law 243 s.4](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).
- Companies, partnerships, Cyprus property-disposal capital gains, dual-residence/treaty allocation, withholding and payroll are separate jobs. Use `cy-corporate-tax`, `cy-cross-border`, `cyprus-payroll`, `cyprus-social-contributions`, `cy-non-dom` and `cyprus-vat-return` as relevant; a link to another Guide does not release a hold here. Check this point with one of our partner accountants.

## Rates, bands and thresholds

Apply each percentage only to the slice of chargeable income in its band; do not round chargeable income to whole euros to choose a band.

| 2026 chargeable-income slice | Rate | Cumulative tax at top | Official source |
|---|---|---|---|
| Up to EUR 22,000 | 0% | EUR 0 (computed) | [ITL Second Schedule 1(γ), Law 244 s.22 as renumbered](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Above EUR 22,000 to EUR 32,000 | 20% | EUR 2,000 (computed) | [ITL Second Schedule 1(γ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Above EUR 32,000 to EUR 42,000 | 25% | EUR 4,500 (computed) | [ITL Second Schedule 1(γ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Above EUR 42,000 to EUR 72,000 | 30% | EUR 13,500 (computed) | [ITL Second Schedule 1(γ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Above EUR 72,000 | 35% | EUR 13,500 plus 35% of excess (computed) | [ITL Second Schedule 1(γ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |

The cumulative amounts are arithmetic. For a positive chargeable base `x`, ordinary tax is `0.20*max(0,min(x,32000)-22000) + 0.25*max(0,min(x,42000)-32000) + 0.30*max(0,min(x,72000)-42000) + 0.35*max(0,x-72000)`.

| Relief or separate item | 2026 figure and operative limits | Official source |
|---|---|---|
| Contributions/premiums, art.14 | Combined maximum 1/5 of taxable income **before** art.14 and art.14B deductions; individual limits below also apply | [Law 244 s.9, replacement art.14(2)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Life/disability insurance | Own-life or permanent/temporary, total/partial disability qualifying policy under Cyprus or comparable EU law; maximum 7% of insured death/disability amount, excluding additional bonuses | [Art.14(1)(α)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Approved pension/provident funds and pension/annuity plans | Aggregate 10% of non-exempt art.5 income; business income uses profit in this limit; fund/plan must meet art.14 approval and Cyprus/EU conditions | [Art.14(1)(γ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Approved medical insurance plans | Aggregate 2% of non-exempt art.5 income; business income uses profit; qualifying Cyprus/comparable EU policy and Commissioner approval required | [Art.14(1)(δ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Home disaster insurance | Up to EUR 500 for qualifying home insurance under Cyprus/comparable EU law; outside art.14, before measuring its 1/5 base | [Art.9(1)(ζ)(ββ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf); [Tax Department FAQ 42–46](https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf) |
| Approved cultural donations | Up to EUR 50,000; institution approved by Minister of Culture under Council conditions; loss attributable to the donation cannot be carried forward | [Art.9(1)(ν)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Child deduction | Per eligible parent: EUR 1,000 first dependent child, EUR 1,250 second, EUR 1,500 third and each further; single-parent/full-custody doubling subject to the definitions below | [Art.14B(1)(α)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Main-home loan interest/rent | One combined actual-spend cap EUR 2,000 per spouse/civil partner or qualifying single person, subject to art.14B conditions below | [Art.14B(1)(β)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Green expenditure | Actual qualifying capital expenditure, up to EUR 1,000 per spouse/civil partner or qualifying single person; excess carries to next 4 years, subject to cap each year | [Art.14B(1)(γ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Family income ceiling | No children/up to 2: EUR 100,000; 3–4: EUR 150,000; 5+: EUR 200,000; qualifying single person EUR 40,000. Exactly at ceiling qualifies; above it none of art.14B applies | [Art.14B(1)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Returning-resident exemption | 25%, maximum EUR 25,000 of Cyprus employment pay/business profit, only after every art.8(21B) condition below is met | [Law 17/2026 s.2](https://www.mof.gov.cy/mof/tax/taxdep.nsf/All/AFF8B2E8B2A07820C2258DB60033F251/%24file/5076%206%203%202026%20PARARTIMA%201o%20MEROS%20I.pdf?OpenElement=) |
| Individual interest | Exempt from income tax; SDC/GHS are separate | [Art.8(19), replaced by Law 244 s.4](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Foreign-services pension | Annual choice: ordinary bands or 5% on pension exceeding EUR 5,000; compare both without adding separately taxed pension to the ordinary deduction base | [Art.20, amended by Law 244 s.12](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf); [Ministry of Finance pension explanation](https://www.gov.cy/mof/en/documents/tax-incentives/) |
| Crypto disposal gains | 8% under art.20E, subject to the definition, loss restriction and mining exclusion below | [Law 244 s.13, art.20E](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Approved employee/director share plans | 8% within twice that employer's qualifying pay in vesting-expiry year and EUR 1,000,000 per rolling decade; full conditions below | [Art.20D](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf); [Law 67/2026 s.3](https://www.mof.gov.cy/mof/gpo/gazette.nsf/21F7154E05045B76C2258DD900389972/%24file/5086%2014%204%202026%20PARARTIMA%201o%20MEROS%20I.pdf) |

## The base

### Computation and evidence

Work in this order: establish ordinary income and allowable business/rental costs; apply an evidenced employment exemption if eligible; deduct qualifying art.9 items; measure the art.14 income base and individual contribution caps; deduct the allowed combined art.14 amount; deduct eligible art.14B amounts; apply the bands; compute separate income items independently; reconcile evidenced PAYE and provisional payments. Do not estimate the profit from net platform payouts alone or give a final return from a bank description. The ordinary-base inputs in the examples are stipulated; an unresolved income/expense classification blocks a real calculation.

**Business/rental base hold.** Current official base text for ITL arts.5, 8(20)/(22), 9(1)/(2), 10, 11 and 13 was not substantively recovered in this pass. The old automatic bank-pattern deductions, the 20% building-rent deduction, vehicle/home-office/phone allocation, bad debts, wear-and-tear rates (including the former 7%/20%/33⅓% energy figures), entertainment 1%/EUR 30,000, securities/dividend exemptions, and ordinary/foreign/business-transfer loss outcomes are **not usable here** until their retained conditions and amendment applicability are proven. Do not apply a percentage or assert deductibility from these historical statements. Check this point with one of our partner accountants.

This hold does not turn every credit into income or every debit into an expense. Reconcile invoices, gross platform sales and commissions, refunds, own-account transfers, loan principal and interest, capital purchases, grants, VAT and tax payments separately. Keep an unresolved schedule; do not silently use zero as a final tax-law answer.

### Contributions and insurance

Art.14 permits paid Social Insurance/Widows and Orphans Fund or comparable EU social-insurance contributions; qualifying approved pension/provident contributions and pension/annuity premiums; qualifying approved medical insurance; and GHS or comparable foreign-law contributions. Keep certificates and apply the table's individual limits before the combined 1/5 cap. Legacy qualifying spouse-life policies predating the Act are a separate eligibility hold. [Replacement art.14(1)–(4)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).

Full surrender of a life policy within 3 years adds back 30% of premiums previously relieved; surrender in years 4–6 adds back 20%. A **partial** surrender has a different rule: add 50% of the amount above the gross surrender value at 31 December of the fourth preceding year; that comparison value is zero where the policy had not then run for 4 years and is reduced by the excess of partial surrenders over premiums during the 3 preceding years. Obtain the insurer's certificate before computing either. [Art.14(1)(α)(ii)–(iii), (4)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).

### Family deductions

Art.14B is resident-only and sits outside the 1/5 cap without reducing the income on which that cap is measured. Check family income before granting **any** child, housing or green amount. The number of children for the ceiling is different from the number of **dependent** children eligible for a deduction. Use the statutory Child Benefit Law definitions incorporated by art.14B(3), including the express extension to student children up to age 24; do not infer qualification from age alone. For family composition, shared custody, the age-24 boundary or a claimant who shares a home, no eligibility conclusion is usable without resolving those definitions. The January FAQ's single-person and student-age shorthand differs from the literal Act; the Act controls. Check this point with one of our partner accountants. [Art.14B](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf); [FAQs 13–27](https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf).

Family-income evidence must cover all members and all sources, Cyprus and foreign. The Department's FAQ includes a cohabitant with common children and excludes full-time pupils'/students' employment income, child benefit, student grant/welfare/scholarships, and specified disability/chronic-illness assistance. For business income or a disputed family composition, confirm the statutory Child Benefit Law income calculation rather than equating tax chargeable income or bank credits to family income. [FAQ 14–16](https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf).

For an established qualifying family, apply the table's per-parent child amounts to dependent children at 31 December. Doubling requires the statutory single-parent or full-custody condition. Both spouses'/civil partners' returns, or the single person's return, must be on time under ACL art.5; the spouses/partners must consent to mutual disclosure of their tax data. A late return by either loses the deductions. [Art.14B(1)(α), (2)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).

**Housing:** Cyprus main home; actual qualifying serviced-loan interest or rent, one shared cap per claimant across both categories. For loan interest, at least one spouse/civil partner (or the single person) must own the home and hold the loan. A restructured loan counts when instalments are paid without fail. Deduct related public assistance from the spend. Rent paid contrary to ACL art.48A is not deductible: from 1 July 2026 payment/receipt must use bank transfer, debit/credit card or recognised electronic means. The Act's ownership-proviso wording spans both limbs, while the FAQ applies ownership to interest; **renter eligibility under that proviso remains a non-usable hold**, not a requirement that a tenant own the rented home. Check this point with one of our partner accountants. [Art.14B(1)(β)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf); [Gazette loan-definition correction](https://www.mof.gov.cy/mof/gpo/gazette.nsf/203DBFC78C778160C2258DAB0020F89D/%24file/5075%2027%202%202026%20PARARTIMA%201o%20MEROS%20I.pdf); [FAQ 28–33](https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf).

**Green:** Cyprus main-home energy-efficiency works, energy/renewable systems or storage batteries, or an electric vehicle registered with Road Transport. For works/systems, the home must belong to at least one spouse/civil partner or the single claimant. Reduce spend by related public assistance; both partners' total deductions cannot exceed actual spend; carry excess only within the table's time/cap. Art.14B incorporates the definitions in art.10(2)'s third proviso: unsupported technical asset eligibility remains held. Check this point with one of our partner accountants. [Art.14B(1)(γ)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).

### Employment exemptions and special income

**Art.8(21B), returning residents:** 25% of Cyprus pay/business profit capped at EUR 25,000. Start in 2025–2030; pay/profit exceeds EUR 30,000 in the first 12 months; no Cyprus residence in the preceding 7 tax years, but residence in an earlier year; and either a university degree recognised as equivalent by KY.S.A.T.S. plus at least 36 months' full-time foreign work for a non-resident employer within the 84 months before the **month** of starting, or 84 months of that full-time foreign work before that month. It runs in the start year and next 6 tax years, only where that year's Cyprus pay/profit exceeds EUR 30,000. Residence required except in the start year. Once per lifetime. No art.8(21A) exemption in a year granted this relief; art.8(23A) relief excludes it, as do the special carried-interest/performance-fee elections. [Law 17/2026 ss.2–5](https://www.mof.gov.cy/mof/tax/taxdep.nsf/All/AFF8B2E8B2A07820C2258DB60033F251/%24file/5076%206%203%202026%20PARARTIMA%201o%20MEROS%20I.pdf?OpenElement=).

**First-employment/legacy hold:** the former 20%/EUR 8,550 and 50%/EUR 55,000 descriptions, 3-/15-year histories, 5-/7-/10-/17-year periods, EUR 100,000 legacy threshold, 2016–2021 transition, pre-2023 wording, first-employment cessation and residence conditions are not usable eligibility instructions here. Current official base/transition texts were not recovered; no relief or stacking is inferred. Gather the full employment/residence history and original approval evidence. Check this point with one of our partner accountants.

**Crypto:** disposal includes sale, gift, crypto-to-crypto exchange and payment. Only assets within Regulation (EU) 2023/1114 art.3(1)(5) are within this rule. Losses offset only same-year crypto-disposal gains: no carry-forward or group transfer. Disposal of mined crypto is outside art.20E; gains outside the provision follow the ordinary charging/band rules, requiring a proven base. [Art.20E(1)–(5)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).

**Share options/awards:** Cyprus-resident employee or company director, per-person plan approved by the Commissioner; not connected with the company under art.33. Minimum 3-year vesting beginning no earlier than approval, no transfer before vesting, employer/parent ordinary-equivalent shares except voting rights, and exercise/acquisition price at least 50% of approval-date value. The 8% amount is separate, with the table's annual-pay/rolling-decade limits; excess is ordinary income. For pre-2026 vesting plans, Law 67 permits approval where minimum 3-year vesting had not expired by 30 June 2026 and the employer submitted by that date. Connection/valuation or transitional approval uncertainty blocks the special rate. Check this point with one of our partner accountants. [Art.20D](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf); [Law 67/2026 s.3](https://www.mof.gov.cy/mof/gpo/gazette.nsf/21F7154E05045B76C2258DD900389972/%24file/5086%2014%204%202026%20PARARTIMA%201o%20MEROS%20I.pdf).

**AIF carried interest/UCITS performance fees and employment termination gratuities:** the former 8%/EUR 10,000 minimum and art.20ΣΤ 20%/EUR 200,000 outcomes remain explicit non-usable holds pending complete eligibility/base proof. Do not apply a rate from the label alone. Check this point with one of our partner accountants.

## Deadlines and filing

| 2026 job | Statutory date/condition | Official source |
|---|---|---|
| Ordinary individual return and balancing tax, no audited/reviewed-accounts obligation | 31 July 2027 | [ACL arts.5(1A), 38(1), Law 243 ss.4/21](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Return and balancing tax where audited/reviewed accounts legally required | 31 January 2028 | [Same provisions](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |
| Rental-income provisional income tax | Two instalments, 31 July and 31 December of the tax year | [Tax Department FAQ 52](https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf) |
| Rent GHS not withheld by tenant | Self-assessment, 31 July and 31 December; legal-person tenant still withholds GHS | [FAQ 53–54](https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf) |
| Supporting records | 6 years from the later of the return/revised-return deadline or actual filing; final-year audit extends this until completion or 1 year after its start, whichever occurs first | [ACL art.5(7)(α), Law 243 s.4](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf) |

From 2026 the Tax Department specifies Tax For All for the return. Do not infer the future return's live screens or line numbers before they are available. Employees give the final deductible amounts by category on TD59 to their employer for PAYE, and reconcile the annual return to their certificates. Save acknowledgement, payment reference and supporting computation. [Return page](https://www.gov.cy/mof-tax/en/documents/forologiki-dilosi-eisodimatos-atomoy/); [FAQ 11](https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf).

The Council can extend the return deadline by decree. An announced Commissioner extension protects against late-filing charge and late-payment charge/interest where the return is filed within the notice's extended time and tax due is paid on submission. Check the actual notice for the relevant category/year. [ACL arts.5(1A), 39(8), 50A, amended Law 243](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).

**Accounts and non-rental provisional-tax procedure hold:** the old EUR 70,000/120,000 accounts shortcut omits the retained art.30 income scope and recordkeeping obligations. The EUR 200,000 turnover/EUR 500,000 assets/two-consecutive-year review condition cannot be certified from the amending substitution alone. The general art.24 estimate/revision dates, post-30-June start rule, code 0200, art.25 deemed assessment and missing-estimate treatment also require their complete current base/procedure. Do not assert that turnover alone means no books or audit. Check this point with one of our partner accountants.

## Penalties and interest

- Late return: EUR 150 for an individual, subject to the public-extension protection above. [Law 243 s.31, ACL art.50A(α)](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).
- The single public default rate is **3.50% during 2026**. This is not a promise that the same annual rate will apply when 2026 tax becomes late in 2027/2028. For 2026-year tax the statutory interest starts 1 August 2027 for July filers or 1 February 2028 for January filers, subject to the qualifying-extension protection. [Tax Department current rate](https://www.gov.cy/mof-tax/en/documents/default-interest-monetary-charges-administrative-fines-additional-tax/default-interest-monetary-charges-administrative-fines-additional-tax-general-information/); [Law 243 s.22, ACL art.39](https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf).
- Provisional understatement: the Department's computation notes compare provisional **income**, not provisional tax, with 75% of final taxable income. If below that, the additional tax is 10% of the difference between final tax and provisional tax paid or due. Foreign-tax cases require the proper adjustment; do not infer the trigger solely from two tax payments. [Tax Department computation note 6; unchanged trigger used for arithmetic only here](https://taxisnet.mof.gov.cy/static/help/epr1/taxNotes_2022ch_en.html). Complete current statutory/procedural confirmation for a real charge remains held. Check this point with one of our partner accountants.
- Written-notice noncompliance, late-payment 5% plus further 5%, SDC penalties, assessment-window 6/12-year exceptions and business suspension/sealing are **non-usable enforcement holds** here; the old amounts/durations do not settle a real notice's scope, service, challenge rights or dates. Check this point with one of our partner accountants.

## Cross-border points

Non-resident/dual-resident source allocation, treaty and unilateral foreign-tax credits, EU social-security coordination and foreign-pension treaty restrictions need their own current source proof. Do not infer a zero GHS/SDC result from an income-tax exemption. For SDC, the historical 5%/17% dividend transition, 17%/3% interest/refund, EUR 12,000 total-income limit and 17-of-20 domicile test are **not usable here** without the retained statutory residence/domicile definitions, exceptions and payment history. Never default a person to domiciled for a final computation. Check this point with one of our partner accountants.

SDC on rental income was abolished from 1 January 2026; income tax and GHS remain separate. [Tax Department FAQ 51–54](https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf). Keep the pension's annual ordinary-versus-special comparison separate from any treaty question.

## Two worked examples that recompute

### Example 1: employee with one child, salary EUR 50,000

Maria is resident and domiciled in Cyprus and has worked for a Cyprus employer for years, so no first-employment exemption applies. Her 2026 salary is EUR 50,000. Social Insurance and GHS deducted from her pay total EUR 5,725 (stipulated paid qualifying amounts, not a rate computation). She has one child stipulated to qualify under art.14B; her family composition and child status have been established. Family income is EUR 80,000, under the EUR 100,000 cap for one or two children, and both partners file on time and consent.

The one-fifth cap is EUR 10,000 (EUR 50,000 / 5), so all EUR 5,725 of contributions are deductible. Her child deduction is EUR 1,000. Chargeable income is EUR 43,275. Tax is EUR 4,500 to the top of the 25% band plus 30% of EUR 1,275, so EUR 4,882.50. Her PAYE is credited against this, and her return is due by 31 July 2027.

```oa-check
name: Maria, employee, salary EUR 50,000, one child (2026 bands)
inputs:
  salary: 50000
  contributions: 5725
  child_deduction: 1000
steps:
  - one_fifth_cap: salary / 5
  - contribution_deduction: min(contributions, one_fifth_cap)
  - chargeable: salary - contribution_deduction - child_deduction
  - tax: max(0, min(chargeable, 32000) - 22000) * 0.20 + max(0, min(chargeable, 42000) - 32000) * 0.25 + max(0, min(chargeable, 72000) - 42000) * 0.30 + max(0, chargeable - 72000) * 0.35
expected:
  one_fifth_cap: 10000
  contribution_deduction: 5725
  chargeable: 43275
  tax: 4882.50
```

### Example 2: self-employed, one-fifth cap binds, family income over the cap, provisional tax too low

Andreas is a resident self-employed consultant. His 2026 turnover is EUR 110,000; for this example his legally determined filing category is stipulated to be the 31 July 2027 category, rather than inferred from turnover alone and his profit is EUR 90,000. He paid EUR 16,000 of Social Insurance and GHS and EUR 3,000 of life premiums (within 7% of the sum insured). He has two children and a housing loan with EUR 2,500 of interest. His spouse earns EUR 15,000. The original family-income input of EUR 105,000 is retained as an established case input; do not derive statutory family income solely by adding tax profit and spouse pay. Both children are stipulated to qualify.

Contributions and premiums total EUR 19,000, but the one-fifth cap is EUR 18,000, so EUR 18,000 is deducted. Family income is over the EUR 100,000 cap for two children, so he gets no child or housing deduction (EUR 1,000 + 1,250 + 2,000 = 4,250 lost), and neither does his spouse. Chargeable income is EUR 72,000 and tax is EUR 13,500. In a counterfactual that also establishes all child and loan-interest eligibility conditions, had the family been within the cap, chargeable income would be EUR 67,750 and tax EUR 12,225: the cliff costs him EUR 1,275.

In July 2026 he declared provisional chargeable income of EUR 50,000 (provisional tax EUR 6,900, paid in two instalments). That is below three quarters of EUR 72,000 (EUR 54,000), so the original illustrative additional-tax arithmetic is one tenth of (13,500 - 6,900), which is EUR 660, alongside the EUR 6,600 tax balance. The EUR 660 is not a usable assessment of a real charge while the statutory/procedural hold above remains. Check this point with one of our partner accountants.

```oa-check
name: Andreas, self-employed, profit EUR 90,000, cap binds, family income over EUR 100,000, provisional tax charge
inputs:
  profit: 90000
  contributions: 16000
  life_premiums: 3000
  child_1: 1000
  child_2: 1250
  housing_cap: 2000
  provisional_chargeable: 50000
steps:
  - art14_total: contributions + life_premiums
  - one_fifth_cap: profit / 5
  - art14_deduction: min(art14_total, one_fifth_cap)
  - chargeable: profit - art14_deduction
  - tax: max(0, min(chargeable, 32000) - 22000) * 0.20 + max(0, min(chargeable, 42000) - 32000) * 0.25 + max(0, min(chargeable, 72000) - 42000) * 0.30 + max(0, chargeable - 72000) * 0.35
  - lost_14b: child_1 + child_2 + housing_cap
  - chargeable_if_within_cap: chargeable - lost_14b
  - tax_if_within_cap: max(0, min(chargeable_if_within_cap, 32000) - 22000) * 0.20 + max(0, min(chargeable_if_within_cap, 42000) - 32000) * 0.25 + max(0, min(chargeable_if_within_cap, 72000) - 42000) * 0.30 + max(0, chargeable_if_within_cap - 72000) * 0.35
  - cliff_cost: tax - tax_if_within_cap
  - provisional_tax: max(0, min(provisional_chargeable, 32000) - 22000) * 0.20 + max(0, min(provisional_chargeable, 42000) - 32000) * 0.25 + max(0, min(provisional_chargeable, 72000) - 42000) * 0.30 + max(0, provisional_chargeable - 72000) * 0.35
  - three_quarters: chargeable * 0.75
  - underestimate_charge: (tax - provisional_tax) / 10
  - balance_due: tax - provisional_tax
expected:
  art14_total: 19000
  one_fifth_cap: 18000
  art14_deduction: 18000
  chargeable: 72000
  tax: 13500
  lost_14b: 4250
  chargeable_if_within_cap: 67750
  tax_if_within_cap: 12225
  cliff_cost: 1275
  provisional_tax: 6900
  three_quarters: 54000
  underestimate_charge: 660
  balance_due: 6600
```

### Preserved bank cases and historical tests

The following original inputs stay in their original years. They are evidence-reconciliation cases, not automatic tax determinations. A bank description establishes neither VAT status nor deductibility. Every held conclusion below means: **Check this point with one of our partner accountants.**

| Original bank input | Evidence task; disposition |
|---|---|
| `15/03/2025 ; BANK OF CYPRUS EMBASMA ; ANDREOU TRADING LTD ; PLIROMI INV-2025-003 ; +1,190.00 ; EUR` | Client/invoice/VAT reconciliation. Original illustrative EUR 1,190 / 1.19 = EUR 1,000 net and EUR 190 VAT is arithmetic only; applicable supply/rate and PIT treatment held. |
| `01/04/2025 ; HELLENIC BANK DD ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD APR ; -29.99 ; EUR` | ADOBE EUR 29.99: obtain invoice, business purpose and revenue/capital treatment; deduction held. |
| `22/04/2025 ; BANK OF CYPRUS KARTA ; OPSO RESTAURANT ; CLIENT DINNER ; -85.00 ; EUR` | OPSO EUR 85 client dinner: obtain purpose/attendees/private split; neither blanket disallowance nor an allowance is usable from the description. |
| `10/01/2025 ; BANK OF CYPRUS DD ; SOCIAL INSURANCE SERVICES ; Q4 2024 CONTRIBUTION ; -2,490.00 ; EUR` | EUR 2,490 Q4 2024 contribution paid 2025: separate period, contribution type, payer and certificate; deduction year/category held. |
| `05/02/2025 ; EUROBANK CYPRUS EMBASMA ; UK PENSION PROVIDER ; MONTHLY PENSION x12 = 18,000/yr ; +1,500.00 ; EUR` | UK pension EUR 1,500 monthly / EUR 18,000 annually in 2025: original special arithmetic (18,000−3,420)×5% = EUR 729; historical eligibility/treaty held. |
| `15/03/2026 ; BANK OF CYPRUS EMBASMA ; ANDREOU TRADING LTD ; PLIROMI INV-2026-003 ; +1,190.00 ; EUR` | 2026 client payment: same EUR 1,190 / EUR 1,000 / EUR 190 reconciliation inputs; VAT/PIT outcome held pending invoice/supply evidence. |
| `01/04/2026 ; HELLENIC BANK DD ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD APR ; -29.99 ; EUR` | 2026 ADOBE EUR 29.99: same invoice/business-purpose hold. |
| `22/04/2026 ; BANK OF CYPRUS KARTA ; OPSO RESTAURANT ; CLIENT DINNER ; -85.00 ; EUR` | 2026 OPSO EUR 85: same private/business-entertainment hold. |
| `10/01/2026 ; BANK OF CYPRUS DD ; SOCIAL INSURANCE SERVICES ; Q4 CONTRIBUTION ; -2,490.00 ; EUR` | 2026 Q4 contribution EUR 2,490: payment type/certificate/period must be established. |
| `05/02/2026 ; EUROBANK CYPRUS EMBASMA ; UK PENSION PROVIDER ; MONTHLY PENSION ; +1,500.00 ; EUR` | 2026 UK pension EUR 1,500 monthly / EUR 18,000 annually: if art.20 foreign-services election applies, special tax = EUR 650; ordinary tax on this pension alone is EUR 0; compare before electing; treaty/GHS held. |

- Original 2025 Example 5 and Tests 1–3: chargeable EUR 30,000 / 45,000 / 70,000; using the original historical 19,500 / 28,000 / 36,300 / 60,000 boundaries gives EUR 2,200 / 6,385 / 14,385. The EUR 45,000 case is not replaced by a 2026 case. These are preserved arithmetic comparisons, not 2025 filing instructions; official historical base/application is held. Check this point with one of our partner accountants.
- Original Test 4 and later Example 5/Test A: 2026 chargeable EUR 50,000 → EUR 6,900, from the sourced 2026 bands. Test B: EUR 22,000 → zero; EUR 22,001 → EUR 0.20.
- Original Test 5: 2025 employee earning at least EUR 66,612; original stipulated 8.8% SI and 2.65% GHS, EUR 66,612 / EUR 180,000 ceilings. EUR 66,612×8.8% = EUR 5,861.86 and 8.8%+2.65% = 11.45% are arithmetic. The percentages apply to different bases; no total contribution or current ceiling is inferred. All SI/GHS eligibility/rate/base/occupational-category outcomes held. Check this point with one of our partner accountants.
- Original Test 6/Test C: resident, non-domiciled, dividends EUR 20,000. The old combined “tax EUR 0” outcome is not usable: PIT, SDC and GHS require separate proof. Check this point with one of our partner accountants.
- Original Test 7 and Example 6: annual foreign pension EUR 18,000, special election; retain 2025 EUR 729 arithmetic above. For the distinct 2026 case, (18,000−5,000)×5% = EUR 650; bands on the pension alone give zero. Do not replace the original year.
- Original Test 8: final tax EUR 10,000 and provisional tax EUR 6,000. These tax amounts alone cannot decide the 75% **income** trigger. If its legal trigger is established, illustrative difference EUR 4,000×10% = EUR 400; actual charge remains held. Check this point with one of our partner accountants.
- Later Test E: if all art.8(21B) conditions are established, the relief is min(25% of qualifying pay/profit, EUR 25,000), with the EUR 30,000 strict threshold and permitted years checked first. No invented pay figure substitutes for this original case.
- Later Test F: established two-child family income EUR 100,001 loses all art.14B deductions; at EUR 100,000 the ceiling itself does not disqualify, but all other conditions still apply.
- Later Test G: 2026 resident domiciled landlord; preserve the rental topic. No SDC on rent; income tax/GHS still apply. The 20% buildings allowance and rental base are held until their retained law is proven; no illustrative rent amount is invented. Check this point with one of our partner accountants.

```oa-check
name: Preserved 2025 arithmetic inputs only, no historical filing clearance
inputs:
  income_1: 30000
  income_2: 45000
  income_3: 70000
  pension: 18000
  ceiling: 66612
  final_tax: 10000
  temporary_tax: 6000
steps:
  - old_tax_1: max(0,min(income_1,28000)-19500)*0.20 + max(0,min(income_1,36300)-28000)*0.25 + max(0,min(income_1,60000)-36300)*0.30 + max(0,income_1-60000)*0.35
  - old_tax_2: max(0,min(income_2,28000)-19500)*0.20 + max(0,min(income_2,36300)-28000)*0.25 + max(0,min(income_2,60000)-36300)*0.30 + max(0,income_2-60000)*0.35
  - old_tax_3: max(0,min(income_3,28000)-19500)*0.20 + max(0,min(income_3,36300)-28000)*0.25 + max(0,min(income_3,60000)-36300)*0.30 + max(0,income_3-60000)*0.35
  - old_pension: (pension-3420)*0.05
  - old_si: round(ceiling*0.088,2)
  - conditional_charge: (final_tax-temporary_tax)*0.10
expected:
  old_tax_1: 2200
  old_tax_2: 6385
  old_tax_3: 14385
  old_pension: 729
  old_si: 5861.86
  conditional_charge: 400
```

```oa-check
name: 2026 preserved rate and pension comparisons
inputs:
  chargeable: 50000
  pension: 18000
  threshold: 22000
steps:
  - tax: max(0,min(chargeable,32000)-22000)*0.20 + max(0,min(chargeable,42000)-32000)*0.25 + max(0,min(chargeable,72000)-42000)*0.30 + max(0,chargeable-72000)*0.35
  - tax_at_zero_boundary: max(0,threshold-22000)*0.20
  - tax_next_euro: max(0,threshold+1-22000)*0.20
  - pension_special: max(0,pension-5000)*0.05
  - pension_ordinary: max(0,min(pension,32000)-22000)*0.20
expected:
  tax: 6900
  tax_at_zero_boundary: 0
  tax_next_euro: 0.20
  pension_special: 650
  pension_ordinary: 0
```

### Bank patterns: original matrix retained on hold

**Every row in this historical matrix is non-usable for tax treatment.** It preserves the original candidate, conclusion and caveat for review; it is not an instruction to apply that conclusion. Missing current retained ITL arts.5/8/9/10/11/13 proof prevents automatic deductions/exclusions. The documented art.14 computation above governs evidenced qualifying contributions. For each unresolved row: **Check this point with one of our partner accountants.**

| Original pattern | Original candidate | Original treatment (HELD) | Original caveat (HELD) |
|---|---|---|---|
| Client name + TRANSFER, DEPOSIT, EMBASMA, PAYMENT | Self-employment income | Business income | If VAT-registered, extract net (excl. 19% VAT) |
| FEES, PROFESSIONAL FEES, CONSULTANCY, AMOIVI | Self-employment income | Business income | Professional fees -- typical for self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Self-employment income | Business income | Platform payout -- match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Self-employment income | Business income | Platform payout -- verify against invoices |
| WISE PAYOUT, REVOLUT PAYOUT | Self-employment income | Business income | Check if business or personal |
| UPWORK, FIVERR, TOPTAL | Self-employment income | Business income | Freelance platform -- net of commission |
| MISTHOS, SALARY, PAYROLL, EMPLOYER [name] | Employment income (PAYE) | Employment income | NOT self-employment -- emoluments under PAYE |
| ENOIKIO, RENT RECEIVED | Rental income | Rental income | Subject to PIT (+ SDC if domiciled) -- see 5.3 |
| TOKOS, INTEREST RECEIVED | Investment income | EXEMPT from PIT | Taxed under SDC if domiciled, otherwise nil |
| MERISMA, DIVIDEND | Investment income | EXEMPT from PIT | Taxed under SDC if domiciled, otherwise nil |
| TAX REFUND, EPISTROFI FOROU | EXCLUDE | Not income | Tax refund from prior year |
| GOVERNMENT GRANT, EPIDOMA | Check nature | Capital grants EXCLUDE; revenue grants = income | Confirm grant nature |
| OFFICE RENT, ENOIKIO GRAFEIOU | Office rent | Deductible | Dedicated business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible | None recorded |
| ACCOUNTANT, AUDITOR, BOOKKEEP, LOGISTIS | Accountancy/audit fees | Deductible | None recorded |
| LAWYER, LEGAL, DIKIGOROS (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible | None recorded |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | Deductible | None recorded |
| TRAINING, CPD, COURSE, SEMINAR, CONFERENCE | Training/CPD | Deductible | Must relate to current business |
| PROFESSIONAL BODY, ICPAC SUBSCRIPTION | Professional subscriptions | Deductible | None recorded |
| BANK CHARGE, MAINTENANCE FEE, SPEXODA | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible | None recorded |
| DOMAIN, HOSTING, CLOUDFLARE, AWS | IT infrastructure | Deductible | If capital, use capital allowances |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible | None recorded |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible | None recorded |
| SOFTWARE LICENCE (perpetual, high value) | Capital item | Capital allowance | Capitalise per wear-and-tear schedule |
| EAC, AHK, ELECTRICITY, ILEKTRISMOS | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| WATER BOARD, YDREFSI | Water | T2 if home office | Proportional if home |
| CYTA, PRIMETEL, EPIC, CABLENET | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| RYANAIR, WIZZ AIR, AEGEAN, CYPRUS AIRWAYS, EASYJET | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel | None recorded |
| BOLT, TAXI, UBER | Local transport | Deductible if business purpose | None recorded |
| FUEL, PETROLINA, EKO, PETROL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING | Parking | T2 -- business % only | None recorded |
| RESTAURANT, DINNER, LUNCH, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private/non-business |
| PERSONAL, GROCERIES, SUPERMARKET, ALPHAMEGA, LIDL | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, PROSTIMO, PARKING FINE | Fines/penalties | NOT deductible | Public policy |
| INCOME TAX, FOROS, TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | See 5.4 [RESEARCH GAP -- reviewer to confirm exact wear-and-tear rate] | Capital allowance, not expense |
| PRINTER, SCANNER, COPIER | Office equipment | See 5.4 [RESEARCH GAP -- reviewer to confirm] | Capital allowance |
| FURNITURE, DESK, CHAIR | Furniture/fittings | See 5.4 [RESEARCH GAP -- reviewer to confirm] | Capital allowance |
| VEHICLE, CAR (business) | Motor vehicle | See 5.4 [RESEARCH GAP -- reviewer to confirm] | Business % only |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer | None recorded |
| LOAN REPAYMENT, PERSONAL LOAN | EXCLUDE | Loan principal movement | None recorded |
| SOCIAL INSURANCE, KOINONIKES ASFALISEIS | Deduction (within 1/5 cap) | Deductible against chargeable income, NOT a business expense | None recorded |
| GHS, GESY, GENIKO SYSTIMA YGEIAS | Deduction (within 1/5 cap) | Deductible against chargeable income | None recorded |
| VAT PAYMENT, FPA | EXCLUDE | VAT liability payment, not expense | None recorded |
| PROVISIONAL TAX, TEMPORARY TAX, PROSORINI FORO | Credit against final liability | Not an expense | None recorded |

Bank-format assertions are held: Bank of Cyprus, Hellenic Bank, Eurobank Cyprus, Astrobank/Alpha Bank Cyprus, Revolut Business and Wise Business; obtain the actual statement rather than assuming PDF/CSV columns, date format or EUR conversion. Retain date, original text, debit/credit, currency, counterparty, invoice and exchange-rate evidence. Greek/transliterated search vocabulary: METAFORA/EMBASMA (transfer), AMESI CHREOSI/DD (direct debit), PAGIA ENTOLI/SO (standing order), KARTA/CARD, KATATHESI/DEPOSIT, SPEXODA/CHARGES, TOKOS/INTERESSI, MISTHOS, ENOIKIO and FPA. These are search aids, not proof of tax character.

## Ask the client first

Read the existing file and correspondence before requesting missing facts. Minimum evidence: full-year bank records and invoices; tax year; residence/day log; employment/business status; age at 31 December; income by category; PAYE/provisional-payment and contribution certificates. Obtain asset register, losses, VAT records and exemption history where relevant.

Ask for every family member's income, full family/child/custody facts, housing ownership/loan/rent receipts and payment method, green assets/grants, filing/consent status. For SDC collect domicile of origin and residence history without assuming status. For reliefs collect employment start and cessation dates, prior residence/work, employer residence, recognised-degree evidence and annual pay/profit. For special income collect contracts, approvals, vesting, connection, disposals, loss records, pension origin and treaty facts.

The working paper keeps: gross business receipts and evidenced costs; independently established ordinary profit; employment/rent/pension/other income; separate exempt/held categories; art.9 deductions; each art.14 cap and the combined cap; art.14B eligibility and amounts; chargeable income; ordinary/separate tax; evidenced credits and unresolved reconciliation. Keep SDC/GHS separate. If onboarding is incomplete, prepare an evidence schedule only and mark held outputs **not usable**. Do not file or claim a relief on default assumptions.

Historical minimum wage and employer-fund figures, all contribution ceilings and occupational-category calculations remain outside this computation pending their own current official-source proof. Check this point with one of our partner accountants.

## Sources

| Source and exact scope read | URL | Read on |
|---|---|---|
| Gazette 5070: Law 243 ss.4,17,18,21,22,29,31,35; Law 244 ss.2,4,5,7,9,10,12,13,22/23 as renumbered; retained old base provisions not established merely by substitutions. SDC amendment read for dependency assessment, not domicile clearance | https://www.mof.gov.cy/mof/gpo/gazette.nsf/540837D7F45A1D53C2258D710034BB74/%24file/5070%2031%2012%202025%20PARART%CE%97MA%201o%20MEROS%20I.pdf | 2026-11-27 |
| Gazette 5075 correction: Law 244 section renumbering and serviced-loan definition correction; the printed reference to art.14B(3)(a) does not change the nature of the correction | https://www.mof.gov.cy/mof/gpo/gazette.nsf/203DBFC78C778160C2258DAB0020F89D/%24file/5075%2027%202%202026%20PARARTIMA%201o%20MEROS%20I.pdf | 2026-11-27 |
| Law 17/2026 ss.2–5: complete new art.8(21B), non-stacking changes and commencement | https://www.mof.gov.cy/mof/tax/taxdep.nsf/All/AFF8B2E8B2A07820C2258DB60033F251/%24file/5076%206%203%202026%20PARARTIMA%201o%20MEROS%20I.pdf?OpenElement= | 2026-11-27 |
| Gazette 5086: Law 66 s.2 and Law 67 ss.2–4, checking effects on this Guide; art.20D transition amended by Law 67 | https://www.mof.gov.cy/mof/gpo/gazette.nsf/21F7154E05045B76C2258DD900389972/%24file/5086%2014%204%202026%20PARARTIMA%201o%20MEROS%20I.pdf | 2026-11-27 |
| Tax Department January FAQ: questions 1–33, 42–55. Used for explanation/rent obligations; conflicts or incorporated definitions are held rather than inferred. Not a claim to read the inaccessible May revision | https://www.gov.cy/media/sites/29/2026/01/FAQs_last.pdf | 2026-11-27 |
| Individual return page: indexed Tax Department text on residence/income filing scope, 2026/2008–2025 bands and TFA. Direct reader returned 403; no future TFA screens certified | https://www.gov.cy/mof-tax/en/documents/forologiki-dilosi-eisodimatos-atomoy/ | 2026-11-27 (indexed text only) |
| Ministry pension explanation, read for annual choice and threshold: indexed official statement of annual choice and EUR 5,000 threshold; direct reader returned 403; treaty outcome not established | https://www.gov.cy/mof/en/documents/tax-incentives/ | 2026-11-27 (indexed text only) |
| Tax Department 2022 computation notes 2, 15–19: historical arithmetic and income-based temporary-tax trigger; not current-year procedural clearance | https://taxisnet.mof.gov.cy/static/help/epr1/taxNotes_2022ch_en.html | 2026-11-27 |
| Tax Department current default-rate explanation, read for current annual rate: indexed official 3.50% from 1 January 2026; not a 2027/2028 rate | https://www.gov.cy/mof-tax/en/documents/default-interest-monetary-charges-administrative-fines-additional-tax/default-interest-monetary-charges-administrative-fines-additional-tax-general-information/ | 2026-11-27 (indexed text only) |

Not yet confirmed: **non-usable holds only**, each carrying the partner-accountant referral above: current retained income/expense/rent/loss/exemption base and transition identity; pension treaty/application; technical green eligibility; family-definition/student boundary/cohabitation and rent-ownership conflicts; spouse legacy policies; tax-account registration and live TFA/provisional-payment procedure; accounts scope; real temporary-tax charges/foreign credits; SDC domicile/interest/dividend/penalty outcomes; GHS/SI/employer funds/ceilings/occupational minima and minimum wage; asset allowances; AIF/UCITS and termination payments; enforcement/assessment exceptions; original 2025 tax/contribution outcomes and bank-format assertions. CyLaw is a reproduction, not the Gazette: direct and browser access were blocked, and its URL alone was not treated as a read. The Tax Department base PDF was identified in the browser but its retained operative provisions were not extracted/read; it does not close these holds. The core bands, replacement art.14/art.14B, residence and filing/payment dates above are supported by the actual enacted replacement/new clauses read in the Gazette. This local draft has no independent-check or publication clearance.
