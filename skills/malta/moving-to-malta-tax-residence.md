---
name: moving-to-malta-tax-residence
description: "Cross-border skill for individuals moving to Malta, tax year 2026 (basis year 2026, year of assessment 2027). Maps the residence routes and what each one taxes, ordinary residence on the remittance basis for non-domiciled residents (EUR 5,000 minimum tax where foreign income is EUR 35,000 or more and not all brought to Malta), the Global Residence Programme and its EU twin (15% on remitted foreign income, EUR 15,000 minimum), the Malta Permanent Residence Programme as an immigration status, the 2026 Highly Skilled Individuals Rules (15% on qualifying employment, subject to approval, contract minima and elections), the Nomad Residence Permit (10% on authorised work, with a conditional initial twelve-month exemption) and the Malta Retirement Programme. Also lists what Malta does tax on arrival, Malta work, rent, property transfers and duty, and the traps on both ends of the corridor. Trigger on move to Malta, Malta non-dom, Malta GRP, Malta nomad tax, Malta HSI, Malta HQP."
jurisdiction: MT
category: international
tax_year: 2026
last_updated: 2026-11-26
version: 2.1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# Moving to Malta: residence routes, the remittance basis, and what Malta actually taxes v2.1

Built by the OpenAccountants team. **Source-cited draft: not reviewed by an accountant.** Figures are for tax year 2026 (basis year 2026, assessed in year of assessment 2027).

## Scope and who this is for

Individuals relocating to Malta (from the UK, the EU or further), and their accountants on the origin side. This skill is written from the Maltese end of the corridor.

**Start with the charge to tax, not the residence permit.** Establish residence, ordinary residence, domicile, spouse and immigration-status facts before applying the remittance basis under [Cap. 123 articles 2 and 4(1)](https://legislation.mt/eli/cap/123/eng/pdf). For wealth, inheritance, estate, gifts and departure taxes: Check this point with one of our partner accountants. Do not turn an absence of a named tax into an exemption from income tax or transfer duty.

In scope: which residence route fits, what each route taxes, the remittance-basis mechanics on arrival, what Malta taxes anyway, and the corridor discipline. Out of scope here, with the skill that owns it:

| Topic | Skill |
|---|---|
| Residence, domicile, remittance evidence and the EUR 5,000 minimum in full | `mt-non-dom` |
| Choosing between the four family routes, worked both ways | `mt-residence-programmes-for-wealthy-families` |
| Global Residence Programme and Residence Programme in full | `mt-global-residence-programme` |
| Malta Permanent Residence Programme (fees, contribution, property, capital) | `mt-permanent-residence-programme` (accountant-approved) |
| Nomad Residence Permit tax rule in full | `mt-nomad-residence-permit` (accountant-approved) |
| Resident rate tables, deductions, the return | `malta-income-tax` (accountant-approved) |
| Property sale tax (article 5A) | `mt-capital-gains`, `mt-property-transfer-tax-the-sale-immovable` |
| Duty on death and inheritance | `mt-inheritance-and-succession` |
| Companies, refunds, Pillar Two | `mt-corporate-tax`, `mt-holding-company-participation-exemption` |

## Ask the client first

1. Nationality of each family member, including any Maltese, EU, EEA or Swiss passport. This decides which programme is open at all.
2. The intended landing date, and whether Malta will be the permanent home (domicile) or a long but temporary base (ordinary residence without domicile).
3. Whether anyone holds, or will apply for, long-term resident status or a permanent residence certificate or card, and whether the spouse is ordinarily resident and domiciled in Malta. Check the defined status, not the wording on a residence-by-investment brochure. The exclusions below use statutory definitions.
4. How much foreign income (as opposed to capital and gains) will be brought to Malta each year, and how much will stay abroad.
5. Whether any work will be done physically in Malta, for whom (Malta employer, foreign employer, own clients), and the expected salary.
6. Whether the accounts holding pre-arrival capital are already separated from income and gains accounts.

## The method, step by step

1. **Fix the year.** Basis year 2026 is year of assessment 2027. Status tests apply to the basis year.
2. **Residence.** The Income Tax Act defines "resident in Malta" for an individual as one who "resides in Malta except for such temporary absences as to the Commissioner may seem reasonable" (Cap. 123 art. 2). It prints no day count. MTCA's practice: more than 183 days in a year makes a person resident for that year, and a person who comes to establish residence is resident from arrival. Detail in `mt-non-dom`.
3. **Ordinary residence and domicile.** MTCA's guidance: a person in Malta for more than 183 days a year over a long period, "say, for three consecutive years", or who comes regularly over about three years and builds personal and economic ties, may become ordinarily resident. Domicile is the permanent home; a domicile of origin is kept until a domicile of choice is acquired.
4. **Exclusions.** Check long-term resident status and permanent residence certificates/cards as defined specifically by S.L. 217.05 and S.L. 460.17, and a spouse ordinarily resident and domiciled in Malta ([Cap. 123 art. 4(1)](https://legislation.mt/eli/cap/123/eng/pdf)). The ordinary remittance-basis exclusions operate in the grant year and later years. GRP and Residence Programme definitions also include applications for their specified long-term/permanent status; check the programme rules separately. An MPRP certificate under S.L. 217.26 is not enough to identify one of the defined exclusions.
5. **Pick the route by arithmetic, not brochure.** Compare ordinary rates plus the non-dom minimum against the 15% programme rate with its EUR 15,000 minimum, using the expected remittances. The worked decision is in `mt-residence-programmes-for-wealthy-families`.
6. **Segregate the money before landing.** Clean capital, post-arrival foreign income and post-arrival gains in separate accounts.
7. **Register and file.** Get a Maltese tax number; the remittance basis is a filing position, not an exemption from filing.
8. **Close the origin country properly.** Exit rules, tie-breakers and estate reach on the origin side.

### Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Source |
|---|---|---|---|
| Non-dom minimum tax, Cap. 123 art. 56(27) | EUR 5,000 a year; ordinarily resident, not domiciled, provisos (i) and (ii) of art. 4(1) apply, not in a scheme with its own minimum | YA 2019 onwards, YA 2027 operative text read | https://legislation.mt/eli/cap/123/eng/pdf |
| Foreign income that triggers the minimum, art. 56(27)(ii) | at least EUR 35,000 arising outside Malta, "not received or not fully received in Malta"; a jointly taxed couple counts both spouses' income | same | https://legislation.mt/eli/cap/123/eng/pdf |
| Top ordinary resident rate, art. 56(1), 2026 income | 35% over EUR 60,000; EUR 9,400 single-table and EUR 10,550 married-joint deductions apply only where the child/parent sub-tables do not apply | YA 2027 (Act III of 2026) | https://legislation.mt/eli/cap/123/eng/pdf |
| Optional final tax on gross rent, art. 31D | 15% of gross qualifying tenement rent, final; commercial rent to/from a related body of persons excluded; election covers all qualifying tenements for that year. Check the long-private-residential-lease abatement and route other eligibility, form and deadline to `mt-rental-income` | Current | https://legislation.mt/eli/cap/123/eng/pdf |
| Tax residence practice | more than 183 days in a year; resident from arrival if coming to establish residence | MTCA practice, not in the Act | https://mtca.gov.mt/personal-tax/individual/tax-residence |
| Global Residence Programme, S.L. 123.148 rule 5(1) | For a granted and continuing eligible status: 15% on foreign income received in Malta; minimum EUR 15,000 per year of assessment for the beneficiary, spouse and rule 2(b)/(d) children together, including the full grant/cessation years | Current | https://legislation.mt/eli/sl/123.148/eng/pdf |
| GRP qualifying property, rule 2 | bought for at least EUR 275,000 (EUR 220,000 in Gozo or the south of Malta) or rented for at least EUR 9,600 a year (EUR 8,750 in Gozo or the south) | Current | https://legislation.mt/eli/sl/123.148/eng/pdf |
| GRP other chargeable income, rule 5(2) | 35 cents per euro, as separate income | Current | https://legislation.mt/eli/sl/123.148/eng/pdf |
| Residence Programme (EU, EEA, Swiss), S.L. 123.160 rule 5 | same 15% rate and EUR 15,000 minimum as the GRP | Current | https://legislation.mt/eli/sl/123.160/eng/pdf |
| Highly Skilled Individuals, L.N. 20 of 2026 rules 3-9 | 15% only following the eligibility determination and valid annual option described below; standard qualifying-contract income minimum EUR 65,000 excluding annual fringe-benefit value, subject to transitional minima and part-year adjustment; reduced-rate ceiling EUR 7,000,000, excess at otherwise applicable rates; standard minimum rises by EUR 10,000 every five years | From 1 Jan 2026 | https://legislation.mt/eli/ln/2026/20/eng/pdf |
| HSI end date, rule 7(3) | no benefit on income earned after 31 December 2040 | same | https://legislation.mt/eli/ln/2026/20/eng/pdf |
| HSI step-up years (guidance) | EUR 75,000 from basis year 2031, EUR 85,000 from basis year 2036 | MTCA guidance | https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/hqpr-new-amalgamated-rules---guidelines---branded-06-04-(002).pdf?sfvrsn=b605473e_1 |
| Nomad Residence Permit, S.L. 123.210 rules 2 and 3 | 10% on chargeable authorised-work income of the eligible main applicant, subject to double tax relief; initial 12 months from the later of permit issue/1 Jan 2024 exempt unless the written non-casual-residence declaration is filed. No new exemption for a replacement permit within two years of ceasing to hold the original | Current | https://legislation.mt/eli/sl/123.210/eng/pdf |
| Malta Retirement Programme, S.L. 123.134 rule 5(1) | 15% on foreign income received in Malta; minimum seven thousand five hundred euro for the beneficiary (as the rule writes it) plus EUR 500 for every dependant and every special carer | Current | https://legislation.mt/eli/sl/123.134/eng/pdf |
| MRP pension condition, rule 4(d) | the qualifying pension is all received in Malta and is at least 75% of chargeable income; rule 2 pension excludes an isolated lump sum and specified exempt capital sums | Current | https://legislation.mt/eli/sl/123.134/eng/pdf |
| MRP application fee, rule 3(1) | EUR 2,500 | Current | https://legislation.mt/eli/sl/123.134/eng/pdf |
| Duty on buying Malta property, Cap. 364 art. 32(1) | EUR 5 per EUR 100 or part of the higher of consideration and value, before applicable relief | Current | https://legislation.mt/eli/cap/364/eng/pdf |
| Sole ordinary residence duty relief, Cap. 364 art. 32(4)(a)-(d) | EUR 3.50 per EUR 100 or part on the first EUR 200,000; qualifying inter vivos acquisition/redemption, no required non-resident permit (including the special-designated-area counterfactual), no other property then owned carrying the specified prior relief, required notarial declaration; proportionate threshold for a partial share. This is not a general first-time-buyer exemption | Current | https://legislation.mt/eli/cap/364/eng/pdf |
| Provisional duty on a promise of sale, Cap. 364 art. 3(6) | 20% of the provisional duty chargeable under arts. 32 and 40, based on information available at the promise date; not necessarily 1% of price if value/relief changes the duty | Current | https://legislation.mt/eli/cap/364/eng/pdf |
| Duty on a transfer of shares, Cap. 364 art. 42(1) | Check this point with one of our partner accountants. Scope, exemptions, market value and property-company definitions must be established; see `selling-a-company-in-malta` | Current | https://legislation.mt/eli/cap/364/eng/pdf |
| Standard VAT rate | 18%; reduced rates 12%, 7%, 5% and 0% | Current | https://mtca.gov.mt/business-tax/vat1/vat-compliance/vat-rates/vat-rates |

### The residence routes

**1. Ordinary residence (the default, and often the best).** Immigration permission and tax residence are separate checks. For an immigration right to move, register or work: Check this point with one of our partner accountants. Taxed at progressive rates on Malta-source income and on remitted foreign income; the remittance basis applies by law when its conditions are met, but not to a long-term resident, a holder of a permanent residence certificate or card, or a person whose spouse is ordinarily resident and domiciled in Malta. Do not impose a programme property threshold on the ordinary tax-residence test in article 2; immigration and registration costs are a separate question. See `mt-non-dom`.

**2. The Residence Programme (EU, EEA and Swiss nationals) and the Global Residence Programme (third-country nationals).** Foreign income remitted to Malta is taxed at a flat 15% instead of progressive rates, with the EUR 15,000 minimum on the foreign income of the beneficiary, the spouse and minor or seriously disabled children. The special rate in rule 5 names only the beneficiary, spouse and rule 2(b)/(d) children; do not extend it to every person meeting the wider dependant definition. Full-year minimums apply in grant and cessation years. Conditions include the qualifying property in the table, not staying more than 183 days in any other single jurisdiction in a calendar year, sickness insurance, stable resources, travel documents, official-language communication, fit-and-proper status and an authorised registered mandatary. GRP excludes the rule 2 long-term resident (including an applicant for that status); the Residence Programme similarly excludes the defined permanent resident (including an applicant). Check the incompatible-benefit rules and the property occupancy/notification conditions in rules 2 and 4, not just the purchase price. Other chargeable income, including Malta-source income, is taxed at a flat 35%. If remitted income is modest, ordinary residence with progressive rates can be cheaper than the EUR 15,000 minimum. Full rules: `mt-global-residence-programme`.

**3. Malta Permanent Residence Programme (third-country nationals).** For administration fees, contributions, donations and capital requirements: Check this point with one of our partner accountants; `mt-permanent-residence-programme` owns those figures. A beneficiary must hold qualifying property for at least five years and residential property thereafter. Agency-consented substitutions have their own conditions (regulation 15(1)(c)). The figures live in `mt-permanent-residence-programme`. Its scope is permanent residency rights by investment ([S.L. 217.26 regulation 2](https://legislation.mt/eli/sl/217.26/eng/pdf)); it supplies no personal income-tax rate in this Guide. Establish the person’s actual residence, domicile and defined statutory statuses under Cap. 123 separately. For MPRP and GRP compatibility or the treatment of a particular certificate: Check this point with one of our partner accountants. Do not infer compatibility from silence in two lists.

**4. Highly Skilled Individuals (formerly Highly Qualified Persons) and similar employment regimes.** From 1 January 2026 the Tax Treatment of Highly Skilled Individuals Rules (L.N. 20 of 2026) provide the new route alongside the rule 12 transition from the Highly Qualified Persons, innovation and creativity, aviation, maritime and family-office employee rules. Prior beneficiaries need a transition application by 31 December 2028; the old regimes do not simply disappear on 1 January 2026, and rule 12(2) ends further old-regime benefits after YA 2030. A qualifying employee needs an eligible scheduled office, satisfaction of all rule 4 conditions (including non-domicile, professional qualifications, appropriate employment, resources, accommodation, travel document and insurance), a formal determination under rule 5, and the rule 6 annual option: signed declaration endorsed by the competent authority plus a fully/correctly declared return, both by the return date. Only then does the 15% apply to qualifying emoluments up to EUR 7 million; excess is taxed at the otherwise applicable rates. The standard EUR 65,000 contract-income test excludes annual fringe-benefit value. MTCA guidance adjusts the minimum pro rata for a contract starting or ending part-way through the year. For eligibility or a part-year calculation: Check this point with one of our partner accountants. The 15% applies with no relief, deduction, credit or set-off of any kind, other than tax deductions under article 23 of Cap. 372 (rule 8). Rule 3(1) raises the minimum by EUR 10,000 every five years "with effect from the year subsequent to the year in which these rules come into force"; MTCA guidance reads that as EUR 75,000 from basis year 2031 and EUR 85,000 from basis year 2036. Where a replaced regime had a lower minimum, that lower minimum applies in the first year, rises by EUR 10,000 in the second year, and the standard minimum applies from the third year (rule 3(1) second proviso). The benefit runs for five years with up to two five-year extensions, subject to continued compliance and an application in the preceding year, and never covers income earned after 31 December 2040 (rule 7). This overview does not decide an eligible-office or transitional case.

**5. Nomad Residence Permit (third-country remote workers).** A permit to live in Malta while working for foreign employers or clients; income from authorised work is taxed at a flat 10%, with no tax for the first 12 months from the later of the permit's issue and 1 January 2024 (the holder can waive that by the written non-casual-residence declaration to Residency Malta). Authorised work requires the rule 2 foreign employer/client and no Malta fixed-place-of-business conditions, remote telecommunications and agency approval. Rule 3(7) denies a fresh twelve-month exemption if a new permit is obtained within two years after ceasing to hold the original. Family members and other income remain under the ordinary Act. It is an explicit carve-out from the default that work done in Malta is Malta-source at progressive rates. Full rules: `mt-nomad-residence-permit`.

**6. Malta Retirement Programme.** This is a granted-status route, not automatic pension treatment. The beneficiary must not be employed, apart from the specific non-executive/public-character activities in rule 2, and must meet all rule 4 conditions including qualifying property, valid travel document, EU-wide sickness insurance, fit-and-proper status and incompatible-status restrictions. Rule 6(1)(b) ends status for a Maltese or third-country national; do not treat the absence of a third-country exclusion in rule 4(c) as eligibility. For eligibility and pension character: Check this point with one of our partner accountants. 15% on foreign income received in Malta by the beneficiary, the spouse and the paragraph (b) children (unmarried minor children under the specified custody/financial-dependence conditions, and adult children unable to maintain themselves through serious illness or disability; rule 2 also requires co-residence and no incompatible programme). Minimum tax EUR 7,500, plus EUR 500 for every dependant and every special carer, payable in full in the year of grant and the year status ends. The pension must all be received in Malta and be at least 75% of chargeable income. The beneficiary must satisfy the nationality restrictions just stated (rules 4(c), 6(1)(b)), must not be domiciled in Malta, nor intend to become so within five years of applying (rule 4(g)). Status ends if the person becomes domiciled in Malta, resides in Malta for less than 90 days a year averaged over any five-year period, or stays in any other jurisdiction for more than 183 days in a calendar year (rule 6(1)(e), (h) and (i), [S.L. 123.134](https://legislation.mt/eli/sl/123.134/eng/pdf)). Other income chargeable under rule 5(2) is separate income taxed at 35 cents per euro; do not turn that into a charge on income outside the Act. Defined long-term/permanent status (including applications) triggers rule 5(4).

**Citizenship by investment: judgment, not immigration advice.** In Case C-181/23 Commission v Malta, judgment of 29 April 2025, the Court of Justice held that Malta's citizenship by naturalisation for exceptional services by direct investment breached Article 20 TFEU and Article 4(3) TEU. The judgment concerns citizenship, not permanent residence; it does not deal with the MPRP. For a current citizenship or immigration route: Check this point with one of our partner accountants. The judgment does not establish MPRP eligibility.

### Remittance-basis mechanics (where the value lives)

An eligible resident non-dom, after the legal-status and spouse exclusions have been checked, is taxed on:

1. Malta-source income and taxable gains: within the charge under article 4, subject to applicable exemptions and treaty relief;
2. foreign-source income: only to the extent received in or remitted to Malta (Cap. 123 art. 4(1) proviso (i));
3. foreign-source capital gains: outside the charge under proviso (ii), including when remitted, after the exclusions above and the income-versus-gain classification are established.

For a foreign portfolio disposal, establish source and that the receipt is a capital gain rather than trading income before applying proviso (ii). Discipline still matters:

- **Segregate accounts before arriving.** Pre-arrival capital remits tax-free, but only if you can prove what was capital on the landing date. Keep three buckets: clean capital, post-arrival foreign income, post-arrival gains. MTCA guidance (section 5.3) presumes remittances "for ordinary expenses, such as living expenses" are income "unless proven otherwise, regardless of the foreign account out of which the remittance is made"; remittances for a capital purpose, such as buying property in Malta, are capital if shown to come from capital held abroad. It is a presumption, not a universal ordering rule.
- **"Remitted" is broad.** Income paid into a foreign account is received in Malta if later remitted (guidance 5.1). For card spending, payments of Maltese bills, brokerage transfers or loans secured on foreign income: Check this point with one of our partner accountants. This Guide makes no deemed-remittance determination for those arrangements.
- **The EUR 5,000 minimum** (Cap. 123 art. 56(27)) applies to a resident who is ordinarily resident but not domiciled in Malta, is not excluded from the remittance basis, and is not in a scheme with its own minimum. A resident who is not ordinarily resident is outside it. The EUR 35,000 is tested on total foreign income: partly remitted income still counts; only a person who brings all of it in is outside. Such a person pays at least EUR 5,000 a year even if they remit nothing. A jointly taxed couple tests the EUR 35,000 on combined income and pays one EUR 5,000. The tax compared with EUR 5,000 is tax before double tax relief; tax paid under the Act (including withholding) counts, and article 5A property-transfer tax does not. Anyone who proves that tax on the worldwide basis would be lower has the liability capped at that lower amount. The pre-relief comparison in article 56(27) does not itself decide a foreign-tax-credit computation. For double taxation relief and its effect on the final payable amount: Check this point with one of our partner accountants. Do not present statutory silence as a prohibition or as an entitlement.
- **No deemed-domicile clock.** Ordinary-residence duration does not by itself establish domicile. MTCA guidance describes domicile of choice by residence with the intention of making that country the permanent home. Acquiring long-term resident status excludes the remittance basis; merely living in Malta for many years is a different question. For succession or an origin-country estate charge: Check this point with one of our partner accountants; this Guide does not establish any foreign country’s taxing reach.

### What Malta actually taxes (the honest list)

| Item | Treatment |
|---|---|
| Malta employment or self-employment | Progressive to 35% (unless the Highly Skilled Individuals or nomad regime applies) |
| Malta rental income | Apply the conditional article 31D option described above, or check the ordinary computation with `mt-rental-income`; do not assume every lease qualifies |
| Sale of Malta immovable property | Check this point with one of our partner accountants. Route acquisition, residence/use, works, project and relationship facts to `mt-capital-gains` and `mt-property-transfer-tax-the-sale-immovable`; this Guide gives no sale rate |
| Buying Malta property | Apply the Cap. 364 rate, rounding, value and relief conditions in the table above; provisional payment is 20% of the duty based on the information then available |
| Foreign income remitted | Progressive, or 15% under the GRP, Residence Programme or MRP with their minimums |
| Foreign income kept offshore | Not taxed for an eligible non-dom (but counts toward the EUR 35,000 trigger for the EUR 5,000 minimum) |
| Foreign capital gains | Not taxed for an eligible non-dom, remitted or not |
| Wealth, inheritance, estate, gifts | Check this point with one of our partner accountants. Malta property and securities transfers can engage Cap. 364 duty, including transfers on death; route actual assets and relief conditions to `mt-inheritance-and-succession` |
| Social security | Check this point with one of our partner accountants. Determine coverage, class and cross-border coordination separately using `malta-ssc` or `malta-payroll` |
| VAT and daily life | Standard rate 18%; check the relevant supply, exemption and reduced-rate conditions |

**Companies, refunds, participation exemption, CFC and Pillar Two.** Check this point with one of our partner accountants. Load `mt-corporate-tax`, `mt-holding-company-participation-exemption` and `mt-company-residence-and-substance` for those topics; this personal-residence Guide gives no effective company rate or foreign CFC conclusion.

### The corridor discipline (both ends)

1. **Exit the origin country properly.** For UK temporary non-residence, French exit tax, Norwegian residence tails or any origin-country cessation: Check this point with one of our partner accountants. Load the origin-country Guide; no foreign conclusion is supplied here.
2. **Mind the treaty tie-breaker.** Check this point with one of our partner accountants. Record homes, habitual living arrangements, family/economic ties and the actual treaty; a permit or one fact does not decide a treaty tie-breaker.
3. **Get a Maltese tax number and actually file.** Returns declare Malta-source and remitted amounts; the minimum-tax computation rides on the return.
4. **Bank before you land.** Keep the evidence needed to distinguish capital and income; do not rely on an assumed bank onboarding time.
5. **Document the landing date.** Every bucket (clean capital against post-arrival income) keys off it, exactly as the origin country's cessation date keys its side.

## Boundary and exception table

| Situation | Result | Rule |
|---|---|---|
| Ordinarily resident non-dom, foreign income EUR 35,000 or more, part kept abroad | EUR 5,000 minimum applies, with a top-up if tax is lower | Cap. 123 art. 56(27) |
| Resident but not ordinarily resident, with no spouse or defined-status exclusion | Remittance basis applies; minimum does not | art. 4(1), art. 56(27)(i) |
| Spouse ordinarily resident and domiciled in Malta | Worldwide basis for both; no minimum | art. 4(1) proviso; MTCA guidance 1.2 |
| Long-term resident status or permanent residence card granted in 2026 | Worldwide basis for all of 2026 and later | art. 4(1) proviso |
| GRP, Residence Programme or MRP beneficiary | The scheme's own rate and minimum; not the EUR 5,000 | art. 56(27)(i); MTCA guidance 6.5 |
| Work done physically in Malta for a foreign client | Malta-source, progressive rates, unless the nomad or HSI regime applies | art. 4(1); MTCA guidance 4.1 |
| Occasional visits to Malta by someone whose business is based abroad | Income does not arise in Malta just because of the visits | MTCA guidance 4.3 |
| Inheritance or sale proceeds of a capital asset remitted | Capital, not income; not caught | MTCA guidance 5.2 |
| MPRP holder | Determine Cap. 123 residence, domicile and defined statuses separately; for certificate classification or GRP compatibility: Check this point with one of our partner accountants. | S.L. 217.26 reg. 2; Cap. 123 art. 4(1) |

### The trap list

| Trap | Why it bites |
|---|---|
| "Malta is tax-free, I'll just invoice my clients from here" | Work done in Malta is Malta-source: progressive rates up to 35%, unless the HSI or nomad regime applies. The remittance basis never shelters local work. |
| One mixed bank account for everything | Living-expense remittances are presumed income unless proved otherwise. Separate accounts are a recommended evidence control; mixing does not itself create an irrebuttable loss of the capital treatment. |
| Taking the GRP with modest remitted income | The EUR 15,000 minimum can exceed what ordinary progressive rates would have charged. Run both numbers first. |
| Forgetting the EUR 5,000 minimum | For an ordinarily resident non-dom outside any programme, foreign income of EUR 35,000 or more, not all brought to Malta, triggers it even with zero remittances. |
| Treating the MPRP as a tax deal | It is a residence permit. The tax outcome is whatever residence and non-dom status produce; some MPRP holders are not even Maltese tax residents. |
| Buying property in year one "to qualify" | Purchase duty and sale tax depend on reliefs and facts. Do not assume a five-year sale qualifies for a reduced rate or that renting is always cheaper. |
| Ignoring the origin country's estate reach | Check this point with one of our partner accountants. Record the assets and origin-country connections; no blanket exemption or foreign tax charge is inferred here. |
| Assuming the company refund is personal | Check this point with one of our partner accountants. The character and chargeability of a refund, distribution or foreign CFC inclusion require their own analysis. |

## Worked cases

These assume ordinary residence, foreign domicile, no legal-status or spouse exclusion, no special programme, no foreign tax credit, and evidence proving the stated income. Case 1 also assumes any evidenced worldwide liability is not below the minimum. Rates are the year of assessment 2027 tables in Cap. 123 art. 56(1) (owned by `malta-income-tax`).

**Case 1: eligible ordinary non-dom whose own tax is EUR 1,200.** A single non-dom has Malta tax of EUR 1,200 on Malta income and remittances, and EUR 50,000 of foreign income kept abroad. On the stated facts and assuming the proved worldwide-tax cap is not below EUR 5,000, the minimum applies, so the top-up is EUR 3,800 and the total EUR 5,000.

```oa-check
name: Eligible ordinary non-dom minimum with EUR 1,200 of Malta tax
inputs:
  eligible_minimum: 5000
  tax_counting_toward_minimum: 1200
steps:
  - top_up: max(eligible_minimum - tax_counting_toward_minimum, 0)
  - total: tax_counting_toward_minimum + top_up
expected:
  top_up: 3800
  total: 5000
```

**Case 2 (a decision): pay the minimum or prove the worldwide cap.** A jointly taxed couple, no qualifying children, with EUR 35,000 of foreign income in total and nothing remitted. The minimum is triggered (EUR 35,000 is "not less than" the threshold). Worldwide tax on the married joint table: 35,000 x 25% minus 4,550 = EUR 4,200. Choice: pay the EUR 5,000 minimum, or prove the worldwide computation and pay EUR 4,200. Proving the cap saves EUR 800 but needs a full worldwide computation with evidence. If worldwide income were EUR 40,000 instead (tax EUR 5,450), the cap would not help and the EUR 5,000 minimum stands.

```oa-check
name: Joint couple choose minimum or worldwide cap
inputs:
  worldwide_income: 35000
  minimum: 5000
steps:
  - worldwide_tax: worldwide_income * 0.25 - 4550
  - liability_if_cap_proved: min(minimum, worldwide_tax)
  - saving_from_cap: minimum - liability_if_cap_proved
  - worldwide_tax_at_40000: 40000 * 0.25 - 4550
  - liability_at_40000: min(minimum, worldwide_tax_at_40000)
expected:
  worldwide_tax: 4200
  liability_if_cap_proved: 4200
  saving_from_cap: 800
  worldwide_tax_at_40000: 5450
  liability_at_40000: 5000
```

## When to refuse or refer

- Refuse a final figure without the nationality, domicile, ordinary residence, spouse and long-term resident facts.
- Refer disputed domicile, ordinary residence, and arrival or departure years (`mt-non-dom`).
- Refer immigration eligibility (MPRP, nomad permit, GRP property conditions) to Residency Malta, a licensed agent or an authorised registered mandatary.
- For double tax relief and the final amount payable after the statutory pre-relief comparison: Check this point with one of our partner accountants.
- Refer whether the MPRP can be held with the GRP.
- Refer the origin country's exit, residence-tail and estate rules to an adviser in that country.
- Refer company structures and refunds (`mt-corporate-tax`).

## Filing and payment

| Item | Date or rule | Source |
|---|---|---|
| Individual return and tax, basis year 2026 (YA 2027) | Ordinary self-assessment: 30 June 2027, subject to statutory exceptions and any MTCA extension; a separate assessment election/notice route can change settlement timing | [S.L. 372.16 rules 2(c)(ii), 5](https://legislation.mt/eli/sl/372.16/eng/pdf); see `malta-income-tax` |
| Individual return and tax, basis year 2025 (YA 2026) | Extended by MTCA to 31 July 2026 for manual and electronic returns and the tax due | [MTCA notice](https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline) |
| GRP and Residence Programme minimum tax | By 30 April of the year before the year of assessment (30 April 2026 for YA 2027), with proof rule 4 remains satisfied. No continuation return in grant year; if status evidently cannot be granted before 30 April, pay before grant. Tax under rule 5(1) is not refundable | [S.L. 123.148 rule 5(3)](https://legislation.mt/eli/sl/123.148/eng/pdf) |
| Non-dom minimum top-up | Part of the self-assessment, due with the balance of tax | Cap. 123 art. 56(27) |
| Rental 15% final tax | See `mt-rental-income` | Cap. 123 art. 31D |

## Completion checklist

- Nationality, landing date, residence, ordinary residence and domicile recorded with the facts behind each.
- Exclusions checked: long-term resident or permanent residence status, spouse's domicile and ordinary residence.
- Route chosen by arithmetic, with the worked comparison kept on file.
- Clean capital, income and gains accounts separated before the landing date, with statements.
- Any Malta work identified and routed (progressive, HSI or nomad).
- Property, duty and rental questions routed to their skills.
- Origin-country exit handled by an adviser there.
- Output labelled as an estimate until reviewed.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 123: read for art. 2 (resident), art. 4(1) provisos, art. 31D(2) (15% rent), art. 56(1) YA 2027 single and married tables, art. 56(27) minimum tax | https://legislation.mt/eli/cap/123/eng/pdf | 2026-11-26 |
| Global Residence Programme Rules, S.L. 123.148: read for rules 2, 3(1), 4(b), 5(1) to 5(3) and 6(1)(f) | https://legislation.mt/eli/sl/123.148/eng/pdf | 2026-11-26 |
| Residence Programme Rules, S.L. 123.160: read for rules 2-6 | https://legislation.mt/eli/sl/123.160/eng/pdf | 2026-11-26 |
| L.N. 20 of 2026, Highly Skilled Individuals Rules: read for rules 1, 3-12 (EUR 65,000, EUR 10,000 step, 2040, EUR 7,000,000, no relief) | https://legislation.mt/eli/ln/2026/20/eng/pdf | 2026-11-26 |
| MTCA, Guidelines on the Highly Skilled Individuals Rules: read for sections A-G (step-up years, pro-rata minimum, determination and annual option) | https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/hqpr-new-amalgamated-rules---guidelines---branded-06-04-(002).pdf?sfvrsn=b605473e_1 | 2026-11-26 |
| Nomad Residence Permits (Income Tax) Rules, S.L. 123.210: read for rules 2 and 3 (authorised work, 10%, first 12 months and re-entry) | https://legislation.mt/eli/sl/123.210/eng/pdf | 2026-11-26 |
| Malta Retirement Programme Rules, S.L. 123.134: read for rules 3(1) (EUR 2,500 fee), 4(c), 4(d), 4(g), 5(1), 5(2) and 6(1)(e), (h), (i) | https://legislation.mt/eli/sl/123.134/eng/pdf | 2026-11-26 |
| Malta Permanent Residence Programme Regulations, S.L. 217.26: regulation 2 scope and regulation 15(1)(b) incompatible-benefit list; compatibility not inferred | https://legislation.mt/eli/sl/217.26/eng/pdf | 2026-11-26 |
| Duty on Documents and Transfers Act, Cap. 364: read for art. 3(6) (provisional 20%), art. 32(1) (5%), art. 32(4)(a) (first EUR 200,000 at 3.5%), art. 42(1) (2%, plus 3% for property companies) | https://legislation.mt/eli/cap/364/eng/pdf | 2026-11-26 |
| MTCA, Tax Residence page: read for the 183-day practice and ordinary residence after about three years | https://mtca.gov.mt/personal-tax/individual/tax-residence | 2026-11-26 |
| MTCA, Guidance Note on the Remittance Basis: read for sections 1.2, 2, 3, 4, 5 and 6 (presumption on living expenses, minimum tax, relief, excluded schemes) | https://mtca.gov.mt/docs/default-source/documents/mtca-guidelines-on-the-remittance-under-the-income-tax.pdf | 2026-11-26 |
| MTCA, notice of 3 June 2026: read for the 31 July 2026 deadline for YA 2026 individual returns and tax | https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline | 2026-11-26 |
| MTCA, VAT rates page: read for the 18% standard rate and the 12%, 7%, 5% and 0% rates | https://mtca.gov.mt/business-tax/vat1/vat-compliance/vat-rates/vat-rates | 2026-11-26 |
| Income Tax (Statutory Dates) Rules, S.L. 372.16: rules 2(c)(ii), 3 and 5 | https://legislation.mt/eli/sl/372.16/eng/pdf | 2026-11-26 |
| Court of Justice, Case C-181/23 Commission v Malta: operative part and judgment date read directly | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0181 | 2026-11-26 |

Not yet confirmed: none retained as usable guidance. The exact partner-accountant referrals above cover double tax relief, immigration/programme compatibility, particular certificate classification, remittance arrangements, origin-country/treaty rules, company distributions/CFC/Pillar Two and wealth/estate/gift/departure charges. HSI eligibility, transitional and part-year determinations remain expressly referred. Budget 2027 proposals are outside this 2026 Guide.
